"""
Semantic Code Generator - Generates readable Python with structure awareness.

Uses metadata about game structures to produce code like:
    player.gold += 100
instead of:
    store32(load32(9561692) + 8, load32(load32(9561692) + 8) + 100)
"""

import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Set, Optional, Tuple, Any
from collections import defaultdict

# Add tzar to path for structures
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from tools.transpiler.wat_parser import WatModule, WatFunction, WatInstruction, WatType


# =============================================================================
# Structure Metadata (embedded for standalone use)
# =============================================================================

PLAYER_STRIDE = 286704
ENTITY_STRIDE = 132
ENTITY_TYPE_STRIDE = 404

PLAYER_BASE = 9561692
ENTITY_BASE = 9671128
ENTITY_TYPE_BASE = 9568096
GAME_STATE_BASE = 9142424

PLAYER_FIELDS = {
    0: "id", 4: "team", 8: "gold", 12: "wood", 16: "food", 20: "stone",
    24: "population", 28: "max_pop", 32: "score", 36: "kills", 40: "deaths",
    44: "buildings_built", 48: "units_trained", 52: "is_ai", 56: "difficulty",
    60: "civilization", 64: "color", 68: "name_ptr",
    # Economy/resource tracking
    283976: "total_resources", 283980: "spent_resources",
    284636: "building_queue_ptr",
    # End-of-struct flags
    286700: "dirty_flag",
}

ENTITY_FIELDS = {
    0: "id", 4: "type_id", 8: "owner", 12: "x", 16: "y", 20: "z",
    24: "hp", 28: "max_hp", 32: "state", 36: "action", 40: "target_id",
    44: "target_x", 48: "target_y", 52: "speed", 56: "attack", 60: "defense",
    64: "range", 68: "vision", 72: "selected", 76: "group",
    80: "animation", 84: "frame", 88: "direction", 92: "flags",
    96: "garrison_id", 100: "cargo", 104: "cargo_amount",
    108: "rally_x", 112: "rally_y", 116: "queue_count", 120: "queue_ptr",
    122: "sub_state", 124: "link_next", 125: "unit_class", 128: "link_prev",
}

ENTITY_TYPE_FIELDS = {
    0: "id", 4: "name_ptr", 8: "category", 12: "base_hp", 16: "base_attack",
    20: "base_defense", 24: "base_speed", 28: "base_range", 32: "base_vision",
    36: "cost_gold", 40: "cost_wood", 44: "cost_food", 48: "cost_stone",
    52: "build_time", 56: "pop_cost", 60: "sprite_id", 64: "icon_id",
    188: "unit_ai_type", 264: "formation_type",
}

GLOBALS = {
    9142424: "GAME_STATE",
    9142872: "CURRENT_PLAYER",
    9142892: "PLAYER_COUNT",
    9561692: "PLAYERS",
    9568096: "ENTITY_TYPES",
    9671128: "ENTITIES",
    9690464: "HEAP_FREELIST",
    9690468: "HEAP_TREE",
    9690472: "FREE_SIZE",
    9690476: "HEAP_TOTAL",
    9690480: "HEAP_BASE",
    9690484: "HEAP_TOP",
    9690488: "HEAP_END",
    9690496: "ALLOC_COUNT",
    9690908: "MEM_FLAGS",
    9690912: "MEM_MUTEX",
    9690984: "ALLOC_HANDLER",
}


# =============================================================================
# Expression Types
# =============================================================================

@dataclass
class Expr:
    """Base expression."""
    code: str
    type: str = "i32"

    def __str__(self):
        return self.code


@dataclass
class ConstExpr(Expr):
    """Constant value."""
    value: int = 0

    def __str__(self):
        if self.value in GLOBALS:
            return GLOBALS[self.value]
        return str(self.value)


@dataclass
class VarExpr(Expr):
    """Variable reference."""
    name: str = ""

    def __str__(self):
        return self.name


@dataclass
class FieldExpr(Expr):
    """Structure field access: obj.field"""
    obj: str = ""
    field: str = ""
    struct_type: str = ""

    def __str__(self):
        return f"{self.obj}.{self.field}"


@dataclass
class ArrayExpr(Expr):
    """Array access: arr[index]"""
    array: str = ""
    index: str = ""

    def __str__(self):
        return f"{self.array}[{self.index}]"


@dataclass
class BinaryExpr(Expr):
    """Binary operation."""
    left: str = ""
    op: str = ""
    right: str = ""

    def __str__(self):
        return f"({self.left} {self.op} {self.right})"


# =============================================================================
# Semantic Code Generator
# =============================================================================

class SemanticCodeGen:
    """Generates semantic Python code from WAT."""

    def __init__(self, module: WatModule):
        self.module = module
        self.func: WatFunction = None
        self.lines: List[str] = []
        self.indent = 0
        self.stack: List[Expr] = []
        self.vars: Dict[str, str] = {}  # var name -> semantic name
        self.param_map: Dict[str, str] = {}
        self.block_stack: List[Tuple[str, str]] = []
        self.block_id = 0

    def generate(self, func: WatFunction) -> str:
        """Generate Python code for a function."""
        self.func = func
        self.lines = []
        self.stack = []
        self.indent = 0
        self.block_stack = []
        self.block_id = 0

        # Analyze function context
        context = self._analyze_function(func)

        # Generate signature
        self.param_map = {}
        params = []
        for i, p in enumerate(func.params):
            py_name = self._infer_param_name(p, i, context)
            params.append(py_name)
            self.param_map[p.name] = py_name

        fn_name = func.export_name or self._clean_name(func.name)
        self.lines.append(f"def {fn_name}({', '.join(params)}):")
        self.indent = 1

        # Docstring
        if func.export_name:
            self._emit(f'"""Export: {func.export_name}"""')

        # Generate body
        if func.body:
            self._gen_block(func.body)
        else:
            self._emit("pass")

        # Return if needed
        if func.results and self.stack:
            self._emit(f"return {self.stack.pop()}")

        return '\n'.join(self.lines)

    def _analyze_function(self, func: WatFunction) -> Dict[str, Any]:
        """Analyze function to understand its purpose."""
        ctx = {
            'uses_players': False,
            'uses_entities': False,
            'uses_heap': False,
            'is_getter': False,
            'is_setter': False,
            'accesses': [],
        }

        def scan(instrs):
            for instr in instrs:
                if 'load' in instr.opcode or 'store' in instr.opcode:
                    for op in instr.operands:
                        if isinstance(op, tuple) and op[0] == 'offset':
                            addr = op[1]
                            ctx['accesses'].append(addr)
                            if PLAYER_BASE <= addr < PLAYER_BASE + 8 * PLAYER_STRIDE:
                                ctx['uses_players'] = True
                            elif ENTITY_BASE <= addr < ENTITY_BASE + 10000 * ENTITY_STRIDE:
                                ctx['uses_entities'] = True
                            elif 9690464 <= addr <= 9690984:
                                ctx['uses_heap'] = True
                if instr.children:
                    scan(instr.children)
                if instr.else_children:
                    scan(instr.else_children)

        scan(func.body)

        # Detect getter/setter patterns
        if len(func.body) < 10:
            if func.results and not any('store' in str(i.opcode) for i in func.body):
                ctx['is_getter'] = True
            elif not func.results and any('store' in str(i.opcode) for i in func.body):
                ctx['is_setter'] = True

        return ctx

    def _infer_param_name(self, param, idx: int, ctx: Dict) -> str:
        """Infer semantic parameter name."""
        name = param.name.lstrip('$')

        if name.startswith('var'):
            if ctx['uses_players'] and idx == 0:
                return 'player_id'
            if ctx['uses_entities'] and idx == 0:
                return 'entity_id'
            if ctx['uses_heap'] and idx == 0:
                return 'size'
            return f'arg{idx}'

        return self._clean_name(name)

    def _clean_name(self, name: str) -> str:
        """Clean identifier name."""
        name = name.lstrip('$').replace('.', '_').replace('-', '_')
        keywords = {'if', 'for', 'while', 'return', 'def', 'class', 'import',
                   'from', 'as', 'in', 'is', 'and', 'or', 'not', 'True', 'False', 'None'}
        if name in keywords:
            return f'_{name}'
        return name

    def _emit(self, line: str):
        """Emit a line of code."""
        self.lines.append('    ' * self.indent + line)

    def _push(self, expr: Expr):
        """Push expression onto stack."""
        self.stack.append(expr)

    def _pop(self) -> Expr:
        """Pop expression from stack."""
        if self.stack:
            return self.stack.pop()
        return Expr("0")

    def _gen_block(self, instrs: List[WatInstruction]):
        """Generate code for instruction block."""
        for instr in instrs:
            self._gen_instr(instr)

    def _gen_instr(self, instr: WatInstruction):
        """Generate code for single instruction."""
        op = instr.opcode

        # Constants
        if op == 'i32.const':
            val = instr.operands[0] if instr.operands else 0
            self._push(ConstExpr(str(val) if val not in GLOBALS else GLOBALS[val], value=val))
            return

        if op == 'i64.const':
            val = instr.operands[0] if instr.operands else 0
            self._push(ConstExpr(str(val), value=val))
            return

        if op in ('f32.const', 'f64.const'):
            val = float(instr.operands[0] if instr.operands else 0.0)
            self._push(Expr(str(val), 'f32' if 'f32' in op else 'f64'))
            return

        # Locals
        if op == 'local.get':
            name = self._var_name(instr.operands[0])
            self._push(VarExpr(name, name=name))
            return

        if op == 'local.set':
            name = self._var_name(instr.operands[0])
            val = self._pop()
            self._emit(f"{name} = {val}")
            return

        if op == 'local.tee':
            name = self._var_name(instr.operands[0])
            val = self.stack[-1] if self.stack else Expr("0")
            self._emit(f"{name} = {val}")
            return

        # Globals
        if op == 'global.get':
            name = instr.operands[0].lstrip('$') if instr.operands else 'global0'
            self._push(Expr(f"G.{name}"))
            return

        if op == 'global.set':
            name = instr.operands[0].lstrip('$') if instr.operands else 'global0'
            val = self._pop()
            self._emit(f"G.{name} = {val}")
            return

        # Arithmetic
        if op in ('i32.add', 'i64.add', 'f32.add', 'f64.add'):
            b, a = self._pop(), self._pop()
            self._push(self._simplify_add(a, b))
            return

        if op in ('i32.sub', 'i64.sub', 'f32.sub', 'f64.sub'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} - {b})"))
            return

        if op in ('i32.mul', 'i64.mul', 'f32.mul', 'f64.mul'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} * {b})"))
            return

        if op in ('i32.div_s', 'i64.div_s'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} // {b})"))
            return

        if op in ('f32.div', 'f64.div'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} / {b})"))
            return

        if op in ('i32.rem_s', 'i64.rem_s', 'i32.rem_u', 'i64.rem_u'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} % {b})"))
            return

        # Bitwise
        if op in ('i32.and', 'i64.and'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} & {b})"))
            return

        if op in ('i32.or', 'i64.or'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} | {b})"))
            return

        if op in ('i32.xor', 'i64.xor'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} ^ {b})"))
            return

        if op in ('i32.shl', 'i64.shl'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} << {b})"))
            return

        if op in ('i32.shr_s', 'i64.shr_s'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} >> {b})"))
            return

        if op in ('i32.shr_u', 'i64.shr_u'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"(({a} & 0xFFFFFFFF) >> {b})"))
            return

        # Comparisons
        if op in ('i32.eq', 'i64.eq', 'f32.eq', 'f64.eq'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} == {b})"))
            return

        if op in ('i32.ne', 'i64.ne', 'f32.ne', 'f64.ne'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} != {b})"))
            return

        if op in ('i32.lt_s', 'i64.lt_s', 'f32.lt', 'f64.lt'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} < {b})"))
            return

        if op in ('i32.le_s', 'i64.le_s', 'f32.le', 'f64.le'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} <= {b})"))
            return

        if op in ('i32.gt_s', 'i64.gt_s', 'f32.gt', 'f64.gt'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} > {b})"))
            return

        if op in ('i32.ge_s', 'i64.ge_s', 'f32.ge', 'f64.ge'):
            b, a = self._pop(), self._pop()
            self._push(Expr(f"({a} >= {b})"))
            return

        if op in ('i32.eqz', 'i64.eqz'):
            a = self._pop()
            self._push(Expr(f"not {a}"))
            return

        if op in ('i32.lt_u', 'i64.lt_u', 'i32.le_u', 'i64.le_u',
                  'i32.gt_u', 'i64.gt_u', 'i32.ge_u', 'i64.ge_u'):
            b, a = self._pop(), self._pop()
            cmp = {'lt_u': '<', 'le_u': '<=', 'gt_u': '>', 'ge_u': '>='}
            for k, v in cmp.items():
                if k in op:
                    self._push(Expr(f"(u32({a}) {v} u32({b}))"))
                    return

        # Memory - detect patterns
        if 'load' in op:
            self._gen_load(instr)
            return

        if 'store' in op:
            self._gen_store(instr)
            return

        # Control flow
        if op == 'block':
            self._gen_block_ctrl(instr)
            return

        if op == 'loop':
            self._gen_loop(instr)
            return

        if op == 'if':
            self._gen_if(instr)
            return

        if op == 'br':
            self._gen_branch(instr.operands[0] if instr.operands else 0, False)
            return

        if op == 'br_if':
            self._gen_branch(instr.operands[0] if instr.operands else 0, True)
            return

        if op == 'br_table':
            idx = self._pop()
            self._emit(f"# br_table {idx}")
            self._emit("break")
            return

        if op == 'return':
            if self.func.results and self.stack:
                self._emit(f"return {self._pop()}")
            else:
                self._emit("return")
            return

        # Calls
        if op == 'call':
            self._gen_call(instr.operands[0] if instr.operands else '$func0')
            return

        if op == 'call_indirect':
            idx = self._pop()
            self._push(Expr(f"call_table({idx})"))
            return

        # Stack ops
        if op == 'drop':
            self._pop()
            return

        if op == 'select':
            c = self._pop()
            b = self._pop()
            a = self._pop()
            self._push(Expr(f"({a} if {c} else {b})"))
            return

        if op == 'unreachable':
            self._emit("raise Unreachable()")
            return

        if op == 'nop':
            return

        # Type conversions
        if 'wrap' in op or 'extend' in op or 'trunc' in op or 'convert' in op:
            a = self._pop()
            self._push(Expr(f"i32({a})" if 'i32' in op else f"i64({a})" if 'i64' in op else f"float({a})"))
            return

        # Rotations
        if 'rotl' in op or 'rotr' in op:
            b, a = self._pop(), self._pop()
            fn = 'rotl' if 'rotl' in op else 'rotr'
            self._push(Expr(f"{fn}({a}, {b})"))
            return

        # Bit counting
        if 'clz' in op or 'ctz' in op or 'popcnt' in op:
            a = self._pop()
            fn = 'clz' if 'clz' in op else 'ctz' if 'ctz' in op else 'popcnt'
            self._push(Expr(f"{fn}({a})"))
            return

        # Float math
        if any(x in op for x in ['abs', 'neg', 'sqrt', 'ceil', 'floor', 'trunc']):
            a = self._pop()
            fn = op.split('.')[1]
            self._push(Expr(f"{fn}({a})"))
            return

        # Unknown
        self._emit(f"# TODO: {op}")

    def _simplify_add(self, a: Expr, b: Expr) -> Expr:
        """Simplify addition, detecting struct/array access patterns."""
        # Check for struct field access: base + offset
        if isinstance(b, ConstExpr) and isinstance(a, ConstExpr):
            # Two constants - compute statically
            result = a.value + b.value
            if result in GLOBALS:
                return Expr(GLOBALS[result])
            return ConstExpr(str(result), value=result)

        if isinstance(b, ConstExpr):
            offset = b.value
            # Only detect fields if we know the base is an array element
            if isinstance(a, ArrayExpr):
                field = self._detect_field(a.array, offset)
                if field:
                    return FieldExpr(f"{a}.{field}", obj=str(a), field=field)

        # Check for array access: base + (index * stride)
        array_expr = self._detect_array_access(a, b)
        if array_expr:
            return array_expr

        return Expr(f"({a} + {b})")

    def _detect_array_access(self, a: Expr, b: Expr) -> Optional[Expr]:
        """Detect array[index] patterns."""
        import re

        a_str = str(a)
        b_str = str(b)

        # Pattern: base + (index * stride)
        # Check for multiplication with known strides
        mul_match = re.search(r'\((.+?) \* (\d+)\)', b_str)
        if mul_match:
            idx_expr = mul_match.group(1)
            stride = int(mul_match.group(2))

            # Direct base or load32(BASE) patterns
            if stride == ENTITY_STRIDE:
                if a_str == "ENTITIES" or a_str == "load32(ENTITIES)":
                    return ArrayExpr(f"entities[{idx_expr}]", array="entities", index=idx_expr)

            if stride == PLAYER_STRIDE:
                if a_str == "PLAYERS" or a_str == "load32(PLAYERS)":
                    return ArrayExpr(f"players[{idx_expr}]", array="players", index=idx_expr)

            if stride == ENTITY_TYPE_STRIDE:
                if a_str == "ENTITY_TYPES" or a_str == "load32(ENTITY_TYPES)":
                    return ArrayExpr(f"entity_types[{idx_expr}]", array="entity_types", index=idx_expr)

        return None

    def _detect_field(self, array_type: str, offset: int) -> Optional[str]:
        """Detect if array element + offset is a known struct field."""
        if array_type == "players" and offset in PLAYER_FIELDS:
            return PLAYER_FIELDS[offset]
        if array_type == "entities" and offset in ENTITY_FIELDS:
            return ENTITY_FIELDS[offset]
        if array_type == "entity_types" and offset in ENTITY_TYPE_FIELDS:
            return ENTITY_TYPE_FIELDS[offset]
        return None

    def _gen_load(self, instr: WatInstruction):
        """Generate semantic load."""
        op = instr.opcode
        addr = self._pop()
        offset = self._get_offset(instr.operands)

        # Determine load function
        if '8_u' in op:
            fn = 'load8u'
        elif '8_s' in op:
            fn = 'load8s'
        elif '16_u' in op:
            fn = 'load16u'
        elif '16_s' in op:
            fn = 'load16s'
        elif 'i64.load32' in op:
            fn = 'load32'
        elif 'i64.load' in op:
            fn = 'load64'
        elif 'f32.load' in op:
            fn = 'loadf32'
        elif 'f64.load' in op:
            fn = 'loadf64'
        elif 'atomic' in op:
            fn = 'atomic_load'
        else:
            fn = 'load32'

        # Check for semantic access
        if offset:
            if offset in GLOBALS:
                self._push(Expr(GLOBALS[offset]))
                return

            # Try to detect struct field from array access
            if isinstance(addr, ArrayExpr):
                field = self._detect_field(addr.array, offset)
                if field:
                    self._push(Expr(f"{fn}({addr}.{field})"))
                    return

            self._push(Expr(f"{fn}({addr} + {offset})"))
        else:
            self._push(Expr(f"{fn}({addr})"))

    def _gen_store(self, instr: WatInstruction):
        """Generate semantic store."""
        op = instr.opcode
        val = self._pop()
        addr = self._pop()
        offset = self._get_offset(instr.operands)

        # Determine store function
        if 'store8' in op:
            fn = 'store8'
        elif 'store16' in op:
            fn = 'store16'
        elif 'i64.store32' in op:
            fn = 'store32'
        elif 'i64.store' in op:
            fn = 'store64'
        elif 'f32.store' in op:
            fn = 'storef32'
        elif 'f64.store' in op:
            fn = 'storef64'
        elif 'atomic' in op:
            fn = 'atomic_store'
        else:
            fn = 'store32'

        # Check for semantic access
        if offset:
            # Try to detect struct field from array access
            if isinstance(addr, ArrayExpr):
                field = self._detect_field(addr.array, offset)
                if field:
                    self._emit(f"{fn}({addr}.{field}, {val})")
                    return

            self._emit(f"{fn}({addr} + {offset}, {val})")
        else:
            self._emit(f"{fn}({addr}, {val})")

    def _gen_block_ctrl(self, instr: WatInstruction):
        """Generate block control structure."""
        label = instr.label or f'$block{self.block_id}'
        self.block_id += 1
        self.block_stack.append(('block', label))

        # Check if block is targeted by branches
        if self._has_branch(instr.children, label, 0):
            self._emit(f"while True:  # {label}")
            self.indent += 1
            self._gen_block(instr.children)
            self._emit("break")
            self.indent -= 1
        else:
            self._gen_block(instr.children)

        self.block_stack.pop()

    def _gen_loop(self, instr: WatInstruction):
        """Generate loop structure."""
        label = instr.label or f'$loop{self.block_id}'
        self.block_id += 1
        self.block_stack.append(('loop', label))

        self._emit(f"while True:  # {label}")
        self.indent += 1
        self._gen_block(instr.children)
        self._emit("break")
        self.indent -= 1

        self.block_stack.pop()

    def _gen_if(self, instr: WatInstruction):
        """Generate if structure."""
        cond = self._pop()

        self._emit(f"if {cond}:")
        self.indent += 1
        if instr.children:
            self._gen_block(instr.children)
        else:
            self._emit("pass")
        self.indent -= 1

        if instr.else_children:
            self._emit("else:")
            self.indent += 1
            self._gen_block(instr.else_children)
            self.indent -= 1

    def _gen_branch(self, target, conditional: bool):
        """Generate branch."""
        if conditional:
            cond = self._pop()
            self._emit(f"if {cond}:")
            self.indent += 1

        # Find target
        if isinstance(target, str):
            for i, (kind, lbl) in enumerate(reversed(self.block_stack)):
                if lbl == target:
                    if kind == 'loop':
                        self._emit("continue")
                    else:
                        self._emit("break")
                    break
            else:
                self._emit("break")
        elif isinstance(target, int) and target < len(self.block_stack):
            kind, _ = self.block_stack[-(target + 1)]
            if kind == 'loop':
                self._emit("continue")
            else:
                self._emit("break")
        else:
            self._emit("break")

        if conditional:
            self.indent -= 1

    def _gen_call(self, target: str):
        """Generate function call."""
        target_func = self.module.functions.get(target)
        param_count = len(target_func.params) if target_func else 0
        has_result = bool(target_func.results) if target_func else True

        args = []
        for _ in range(param_count):
            args.insert(0, str(self._pop()))

        name = self._clean_name(target)
        call = f"{name}({', '.join(args)})"

        if has_result:
            self._push(Expr(call))
        else:
            self._emit(call)

    def _var_name(self, wat_name) -> str:
        """Get variable name."""
        if isinstance(wat_name, int):
            all_locals = self.func.all_locals
            if wat_name < len(all_locals):
                wat_name = all_locals[wat_name].name
            else:
                return f"v{wat_name}"

        if wat_name in self.param_map:
            return self.param_map[wat_name]

        name = wat_name.lstrip('$')
        if name.startswith('var'):
            return f"v{name[3:]}"
        return self._clean_name(name)

    def _get_offset(self, operands: List) -> Optional[int]:
        """Extract offset from operands."""
        for op in operands:
            if isinstance(op, tuple) and op[0] == 'offset':
                return op[1]
        return None

    def _has_branch(self, instrs: List[WatInstruction], label: str, depth: int) -> bool:
        """Check if any instruction branches to label."""
        for instr in instrs:
            if instr.opcode in ('br', 'br_if'):
                target = instr.operands[0] if instr.operands else 0
                if target == label or (isinstance(target, int) and target == depth):
                    return True
            if instr.opcode == 'br_table':
                return True
            if instr.children:
                child_depth = depth + 1 if instr.opcode in ('block', 'loop', 'if') else depth
                if self._has_branch(instr.children, label, child_depth):
                    return True
            if instr.else_children:
                if self._has_branch(instr.else_children, label, depth):
                    return True
        return False


# =============================================================================
# Main
# =============================================================================

def generate(module: WatModule, func_name: str) -> str:
    """Generate semantic code for a function."""
    if func_name not in module.functions:
        raise ValueError(f"Function {func_name} not found")

    gen = SemanticCodeGen(module)
    return gen.generate(module.functions[func_name])


if __name__ == '__main__':
    from wat_parser import parse_wat_file

    if len(sys.argv) < 2:
        print("Usage: semantic_codegen.py <wat_file> [func_name]")
        sys.exit(1)

    module = parse_wat_file(sys.argv[1])

    if len(sys.argv) > 2:
        func_name = sys.argv[2]
        if not func_name.startswith('$'):
            func_name = f"${func_name}"
        print(generate(module, func_name))
    else:
        gen = SemanticCodeGen(module)
        count = 0
        for name, func in module.functions.items():
            if func.is_import:
                continue
            print(f"# {'='*60}")
            print(f"# {name}")
            try:
                print(gen.generate(func))
            except Exception as e:
                print(f"# Error: {e}")
            print()
            count += 1
            if count >= 5:
                break
