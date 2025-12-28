"""
Smart Python Code Generator from WAT AST.

Generates clean, readable Python code that looks hand-written.
Uses pattern recognition and semantic analysis.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from collections import defaultdict

from wat_parser import WatModule, WatFunction, WatInstruction, WatType


# Known memory structures for semantic naming
MEMORY_SEMANTICS = {
    # Game state
    9142424: ('GAME_STATE', 'game_state'),
    9142872: ('CURRENT_PLAYER_IDX', 'current_player'),
    9142892: ('PLAYER_COUNT', 'player_count'),
    # Player array
    9561692: ('PLAYER_BASE', 'players'),
    # Entity structures
    9568096: ('ENTITY_TYPE_TABLE', 'entity_types'),
    9671128: ('ENTITY_BASE', 'entities'),
    # Memory management
    9690464: ('HEAP_META', 'heap_meta'),
    9690480: ('HEAP_BASE', 'heap_base'),
    9690484: ('HEAP_TOP', 'heap_top'),
    9690908: ('MEM_FLAGS', 'mem_flags'),
    9690912: ('MUTEX', 'mutex'),
    9690984: ('ALLOC_HANDLER', 'alloc_handler'),
}

# Struct field offsets for semantic naming
PLAYER_FIELDS = {
    0: 'id', 4: 'team', 8: 'gold', 12: 'wood', 16: 'food', 20: 'stone',
    24: 'population', 28: 'max_pop', 32: 'score', 36: 'kills', 40: 'deaths',
}

ENTITY_FIELDS = {
    0: 'id', 4: 'type_id', 8: 'owner', 12: 'x', 16: 'y', 20: 'z',
    24: 'hp', 28: 'max_hp', 32: 'state', 36: 'target_id', 40: 'action',
}

PLAYER_STRIDE = 286704
ENTITY_STRIDE = 132
ENTITY_TYPE_STRIDE = 404


class SmartCodeGen:
    """Generates clean, semantic Python from WAT."""

    def __init__(self, module: WatModule):
        self.module = module
        self.func: WatFunction = None
        self.lines: List[str] = []
        self.indent = 0
        self.stack: List[str] = []  # Expression stack
        self.var_types: Dict[str, str] = {}  # var -> inferred type
        self.var_names: Dict[str, str] = {}  # var -> semantic name
        self.declared: Set[str] = set()
        self.block_depth = 0
        self.loop_stack: List[str] = []
        self.block_stack: List[Tuple[str, str]] = []  # (kind, label)
        self.param_mapping: Dict[str, str] = {}

    def generate(self, func: WatFunction) -> str:
        """Generate Python code for a function."""
        self.func = func
        self.lines = []
        self.stack = []
        self.declared = set()
        self.indent = 0
        self.block_depth = 0
        self.loop_stack = []
        self.block_stack = []

        # Analyze function to determine semantic context
        context = self._analyze_context(func)

        # Generate signature with proper parameter names
        self.param_mapping = {}  # Map WAT name -> Python name
        params = []
        for i, p in enumerate(func.params):
            py_name = self._param_name(p, i, context)
            params.append(py_name)
            self.param_mapping[p.name] = py_name

        sig = f"def {self._func_name(func)}({', '.join(params)}):"
        self.lines.append(sig)
        self.indent = 1

        # Add docstring if exported
        if func.export_name:
            self._emit(f'"""Exported as {func.export_name}."""')

        # Generate body
        if not func.body:
            self._emit("pass")
        else:
            self._gen_block(func.body)

        # Handle return
        if func.results and self.stack:
            result = self.stack.pop()
            self._emit(f"return {result}")

        return '\n'.join(self.lines)

    def _analyze_context(self, func: WatFunction) -> Dict[str, Any]:
        """Analyze function to determine semantic context."""
        context = {
            'is_player': False,
            'is_entity': False,
            'is_memory': False,
            'is_math': False,
            'accesses': set(),
        }

        def scan(instrs):
            for instr in instrs:
                if 'load' in instr.opcode or 'store' in instr.opcode:
                    for op in instr.operands:
                        if isinstance(op, tuple) and op[0] == 'offset':
                            addr = op[1]
                            if addr in MEMORY_SEMANTICS:
                                context['accesses'].add(MEMORY_SEMANTICS[addr][0])
                            if 9561692 <= addr < 9568096:
                                context['is_player'] = True
                            elif 9671128 <= addr < 9690464:
                                context['is_entity'] = True
                            elif addr >= 9690464:
                                context['is_memory'] = True
                if instr.children:
                    scan(instr.children)
                if instr.else_children:
                    scan(instr.else_children)

        scan(func.body)

        # Math functions are pure and small
        if not context['is_player'] and not context['is_entity'] and not context['is_memory']:
            if len(func.body) < 50:
                context['is_math'] = True

        return context

    def _param_name(self, p, idx: int, context: Dict) -> str:
        """Generate semantic parameter name."""
        name = p.name.lstrip('$')
        if name.startswith('var'):
            # Try to infer from context
            if context['is_player'] and idx == 0:
                return 'player_idx'
            if context['is_entity'] and idx == 0:
                return 'entity_id'
            if idx == 0:
                return 'arg0'
            return f'arg{idx}'
        return self._clean_name(name)

    def _func_name(self, func: WatFunction) -> str:
        """Get Python function name."""
        if func.export_name:
            return func.export_name
        name = func.name.lstrip('$')
        return self._clean_name(name)

    def _clean_name(self, name: str) -> str:
        """Clean a name for Python."""
        name = name.replace('.', '_').replace('-', '_')
        if name in ('if', 'for', 'while', 'return', 'def', 'class', 'import',
                    'from', 'as', 'in', 'is', 'and', 'or', 'not', 'True', 'False', 'None'):
            return f'_{name}'
        return name

    def _emit(self, line: str):
        """Emit a line of code."""
        self.lines.append('    ' * self.indent + line)

    def _push(self, expr: str):
        """Push expression onto stack."""
        self.stack.append(expr)

    def _pop(self) -> str:
        """Pop expression from stack."""
        if self.stack:
            return self.stack.pop()
        return '0'

    def _gen_block(self, instrs: List[WatInstruction]):
        """Generate code for instruction block."""
        for instr in instrs:
            self._gen_instr(instr)

    def _gen_instr(self, instr: WatInstruction):
        """Generate code for single instruction."""
        op = instr.opcode

        # Constants - push directly
        if op == 'i32.const':
            val = instr.operands[0] if instr.operands else 0
            # Use numeric values - semantics can be added as comments later
            self._push(str(val))
            return

        if op == 'i64.const':
            self._push(str(instr.operands[0] if instr.operands else 0))
            return

        if op in ('f32.const', 'f64.const'):
            self._push(str(float(instr.operands[0] if instr.operands else 0.0)))
            return

        # Local operations
        if op == 'local.get':
            name = self._local_name(instr.operands[0])
            self._push(name)
            return

        if op == 'local.set':
            name = self._local_name(instr.operands[0])
            val = self._pop()
            self._emit(f"{name} = {val}")
            self.declared.add(name)
            return

        if op == 'local.tee':
            name = self._local_name(instr.operands[0])
            val = self.stack[-1] if self.stack else '0'
            self._emit(f"{name} = {val}")
            self.declared.add(name)
            return

        # Global operations
        if op == 'global.get':
            name = instr.operands[0].lstrip('$') if instr.operands else 'global0'
            self._push(f"G.{name}")
            return

        if op == 'global.set':
            name = instr.operands[0].lstrip('$') if instr.operands else 'global0'
            val = self._pop()
            self._emit(f"G.{name} = {val}")
            return

        # Arithmetic - generate clean expressions
        if op in ('i32.add', 'i64.add', 'f32.add', 'f64.add'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} + {b})")
            return

        if op in ('i32.sub', 'i64.sub', 'f32.sub', 'f64.sub'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} - {b})")
            return

        if op in ('i32.mul', 'i64.mul', 'f32.mul', 'f64.mul'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} * {b})")
            return

        if op in ('i32.div_s', 'i64.div_s'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} // {b})")
            return

        if op in ('f32.div', 'f64.div'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} / {b})")
            return

        if op in ('i32.rem_s', 'i64.rem_s', 'i32.rem_u', 'i64.rem_u'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} % {b})")
            return

        # Bitwise
        if op in ('i32.and', 'i64.and'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} & {b})")
            return

        if op in ('i32.or', 'i64.or'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} | {b})")
            return

        if op in ('i32.xor', 'i64.xor'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} ^ {b})")
            return

        if op in ('i32.shl', 'i64.shl'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} << {b})")
            return

        if op in ('i32.shr_s', 'i64.shr_s'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} >> {b})")
            return

        if op in ('i32.shr_u', 'i64.shr_u'):
            b, a = self._pop(), self._pop()
            mask = '0xFFFFFFFF' if 'i32' in op else '0xFFFFFFFFFFFFFFFF'
            self._push(f"(({a} & {mask}) >> {b})")
            return

        # Comparisons - return bool directly, no (1 if x else 0)
        if op in ('i32.eq', 'i64.eq', 'f32.eq', 'f64.eq'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} == {b})")
            return

        if op in ('i32.ne', 'i64.ne', 'f32.ne', 'f64.ne'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} != {b})")
            return

        if op in ('i32.lt_s', 'i64.lt_s', 'f32.lt', 'f64.lt'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} < {b})")
            return

        if op in ('i32.le_s', 'i64.le_s', 'f32.le', 'f64.le'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} <= {b})")
            return

        if op in ('i32.gt_s', 'i64.gt_s', 'f32.gt', 'f64.gt'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} > {b})")
            return

        if op in ('i32.ge_s', 'i64.ge_s', 'f32.ge', 'f64.ge'):
            b, a = self._pop(), self._pop()
            self._push(f"({a} >= {b})")
            return

        if op in ('i32.eqz', 'i64.eqz'):
            a = self._pop()
            self._push(f"({a} == 0)")
            return

        if op in ('i32.lt_u', 'i64.lt_u'):
            b, a = self._pop(), self._pop()
            self._push(f"(u({a}) < u({b}))")
            return

        if op in ('i32.le_u', 'i64.le_u'):
            b, a = self._pop(), self._pop()
            self._push(f"(u({a}) <= u({b}))")
            return

        if op in ('i32.gt_u', 'i64.gt_u'):
            b, a = self._pop(), self._pop()
            self._push(f"(u({a}) > u({b}))")
            return

        if op in ('i32.ge_u', 'i64.ge_u'):
            b, a = self._pop(), self._pop()
            self._push(f"(u({a}) >= u({b}))")
            return

        # Memory operations - generate semantic code
        if 'load' in op:
            self._gen_load(instr)
            return

        if 'store' in op:
            self._gen_store(instr)
            return

        # Control flow
        if op == 'block':
            label = instr.label or f'$block{self.block_depth}'
            self.block_stack.append(('block', label))
            self.block_depth += 1
            # Use while True + break for blocks that have br targets
            has_branch = self._has_branch_to_block(instr.children, label, 0)
            if has_branch:
                self._emit(f"while True:  # block {label}")
                self.indent += 1
                self._gen_block(instr.children)
                self._emit("break")
                self.indent -= 1
            else:
                self._emit(f"# {label}")
                self._gen_block(instr.children)
            self.block_stack.pop()
            self.block_depth -= 1
            return

        if op == 'loop':
            label = instr.label or f'loop{self.block_depth}'
            self.block_stack.append(('loop', label))
            self.loop_stack.append(label)
            self.block_depth += 1
            self._emit(f"while True:  # {label}")
            self.indent += 1
            self._gen_block(instr.children)
            self._emit("break")
            self.indent -= 1
            self.loop_stack.pop()
            self.block_stack.pop()
            self.block_depth -= 1
            return

        if op == 'if':
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
            return

        if op == 'br':
            target = instr.operands[0] if instr.operands else 0
            self._gen_branch(target)
            return

        if op == 'br_if':
            target = instr.operands[0] if instr.operands else 0
            cond = self._pop()
            self._emit(f"if {cond}:")
            self.indent += 1
            self._gen_branch(target)
            self.indent -= 1
            return

        if op == 'br_table':
            idx = self._pop()
            self._emit(f"# br_table[{idx}]")
            self._emit("break")
            return

        if op == 'return':
            if self.func.results and self.stack:
                result = self._pop()
                self._emit(f"return {result}")
            else:
                self._emit("return")
            return

        # Function calls
        if op == 'call':
            self._gen_call(instr.operands[0] if instr.operands else '$func0')
            return

        if op == 'call_indirect':
            idx = self._pop()
            self._emit(f"# call_indirect[{idx}]")
            self._push(f"indirect_call({idx})")
            return

        # Stack operations
        if op == 'drop':
            self._pop()
            return

        if op == 'select':
            cond = self._pop()
            b = self._pop()
            a = self._pop()
            self._push(f"({a} if {cond} else {b})")
            return

        if op == 'unreachable':
            self._emit("raise RuntimeError('unreachable')")
            return

        if op == 'nop':
            return

        # Conversions
        if op == 'i32.wrap_i64':
            a = self._pop()
            self._push(f"i32({a})")
            return

        if op in ('i64.extend_i32_s', 'i64.extend_i32_u'):
            a = self._pop()
            self._push(f"i64({a})")
            return

        if op in ('f32.convert_i32_s', 'f64.convert_i32_s', 'f64.convert_i64_s'):
            a = self._pop()
            self._push(f"float({a})")
            return

        if op in ('i32.trunc_f32_s', 'i32.trunc_f64_s'):
            a = self._pop()
            self._push(f"int({a})")
            return

        # Rotations
        if op in ('i32.rotl', 'i64.rotl'):
            b, a = self._pop(), self._pop()
            bits = 32 if 'i32' in op else 64
            self._push(f"rotl({a}, {b}, {bits})")
            return

        if op in ('i32.rotr', 'i64.rotr'):
            b, a = self._pop(), self._pop()
            bits = 32 if 'i32' in op else 64
            self._push(f"rotr({a}, {b}, {bits})")
            return

        # Bit counting
        if op in ('i32.clz', 'i64.clz'):
            a = self._pop()
            self._push(f"clz({a})")
            return

        if op in ('i32.ctz', 'i64.ctz'):
            a = self._pop()
            self._push(f"ctz({a})")
            return

        if op in ('i32.popcnt', 'i64.popcnt'):
            a = self._pop()
            self._push(f"popcnt({a})")
            return

        # Float operations
        if op in ('f32.abs', 'f64.abs'):
            a = self._pop()
            self._push(f"abs({a})")
            return

        if op in ('f32.neg', 'f64.neg'):
            a = self._pop()
            self._push(f"(-{a})")
            return

        if op in ('f32.sqrt', 'f64.sqrt'):
            a = self._pop()
            self._push(f"sqrt({a})")
            return

        if op in ('f32.ceil', 'f64.ceil'):
            a = self._pop()
            self._push(f"ceil({a})")
            return

        if op in ('f32.floor', 'f64.floor'):
            a = self._pop()
            self._push(f"floor({a})")
            return

        if op in ('f32.trunc', 'f64.trunc'):
            a = self._pop()
            self._push(f"trunc({a})")
            return

        # Memory size
        if op == 'memory.size':
            self._push("mem_size()")
            return

        if op == 'memory.grow':
            a = self._pop()
            self._push(f"mem_grow({a})")
            return

        # Unknown - emit comment
        self._emit(f"# TODO: {op} {instr.operands}")

    def _gen_load(self, instr: WatInstruction):
        """Generate semantic load operation."""
        op = instr.opcode
        addr = self._pop()
        offset = self._get_offset(instr.operands)

        # Determine load type
        if 'i32.load8_u' in op:
            fn = 'load8u'
        elif 'i32.load8_s' in op:
            fn = 'load8s'
        elif 'i32.load16_u' in op:
            fn = 'load16u'
        elif 'i32.load16_s' in op:
            fn = 'load16s'
        elif 'i64.load32_u' in op:
            fn = 'load32u'
        elif 'i64.load32_s' in op:
            fn = 'load32s'
        elif 'i64.load' in op:
            fn = 'load64'
        elif 'atomic' in op:
            fn = 'atomic_load'
        else:
            fn = 'load32'

        # Generate clean load expression
        if offset:
            self._push(f"{fn}({addr} + {offset})")
        else:
            self._push(f"{fn}({addr})")

    def _gen_store(self, instr: WatInstruction):
        """Generate semantic store operation."""
        op = instr.opcode
        val = self._pop()
        addr = self._pop()
        offset = self._get_offset(instr.operands)

        # Determine store type
        if 'store8' in op:
            fn = 'store8'
        elif 'store16' in op:
            fn = 'store16'
        elif 'i64.store32' in op:
            fn = 'store32'
        elif 'i64.store' in op:
            fn = 'store64'
        elif 'atomic' in op:
            fn = 'atomic_store'
        else:
            fn = 'store32'

        if offset:
            self._emit(f"{fn}({addr} + {offset}, {val})")
        else:
            self._emit(f"{fn}({addr}, {val})")

    def _gen_call(self, target: str):
        """Generate function call."""
        target_func = self.module.functions.get(target)
        param_count = len(target_func.params) if target_func else 0
        has_result = bool(target_func.results) if target_func else True

        # Pop arguments
        args = []
        for _ in range(param_count):
            args.insert(0, self._pop())

        name = self._clean_name(target.lstrip('$'))
        call = f"{name}({', '.join(args)})"

        if has_result:
            self._push(call)
        else:
            self._emit(call)

    def _gen_branch(self, target):
        """Generate branch to target."""
        if isinstance(target, str) and target.startswith('$'):
            # Named label - find it in stack
            for i, (kind, label) in enumerate(reversed(self.block_stack)):
                if label == target:
                    if kind == 'loop':
                        self._emit("continue")
                    else:
                        self._emit("break")
                    return
        elif isinstance(target, int):
            if target < len(self.block_stack):
                kind, label = self.block_stack[-(target + 1)]
                if kind == 'loop':
                    self._emit("continue")
                else:
                    self._emit("break")
                return
        self._emit("break")

    def _local_name(self, wat_name) -> str:
        """Get clean local variable name."""
        if isinstance(wat_name, int):
            # Index-based access
            all_locals = self.func.all_locals
            if wat_name < len(all_locals):
                local = all_locals[wat_name]
                wat_name = local.name
            else:
                return f"v{wat_name}"

        # Check if it's a parameter
        if wat_name in self.param_mapping:
            return self.param_mapping[wat_name]

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

    def _has_branch_to_block(self, instrs: List[WatInstruction], label: str, depth: int) -> bool:
        """Check if any instruction branches to the block with given label at given depth."""
        for instr in instrs:
            if instr.opcode in ('br', 'br_if'):
                target = instr.operands[0] if instr.operands else 0
                # Check if target matches - either by label name or by depth index
                if isinstance(target, str) and target == label:
                    return True
                if isinstance(target, int) and target == depth:
                    return True
            if instr.opcode == 'br_table':
                return True  # Assume it could target this block
            # Recurse into children, adjusting depth for nested blocks
            if instr.children:
                child_depth = depth + 1 if instr.opcode in ('block', 'loop', 'if') else depth
                if self._has_branch_to_block(instr.children, label, child_depth):
                    return True
            if instr.else_children:
                if self._has_branch_to_block(instr.else_children, label, depth):
                    return True
        return False


def generate_clean(module: WatModule, func_name: str) -> str:
    """Generate clean Python for a function."""
    if func_name not in module.functions:
        raise ValueError(f"Function {func_name} not found")

    gen = SmartCodeGen(module)
    return gen.generate(module.functions[func_name])


if __name__ == '__main__':
    import sys
    from wat_parser import parse_wat_file

    if len(sys.argv) < 2:
        print("Usage: smart_codegen.py <wat_file> [func_name]")
        sys.exit(1)

    module = parse_wat_file(sys.argv[1])

    if len(sys.argv) > 2:
        func_name = sys.argv[2]
        if not func_name.startswith('$'):
            func_name = f"${func_name}"
        print(generate_clean(module, func_name))
    else:
        # Show first 5 non-imports
        gen = SmartCodeGen(module)
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
