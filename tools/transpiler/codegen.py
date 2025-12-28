"""
Python Code Generator from WAT AST.

Generates Python code from parsed WAT functions.
Uses stack simulation to produce readable Python.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from enum import Enum

from wat_parser import WatModule, WatFunction, WatInstruction, WatType, WatParam, WatLocal


# Instruction mappings
BINARY_OPS = {
    'i32.add': '+',
    'i64.add': '+',
    'f32.add': '+',
    'f64.add': '+',
    'i32.sub': '-',
    'i64.sub': '-',
    'f32.sub': '-',
    'f64.sub': '-',
    'i32.mul': '*',
    'i64.mul': '*',
    'f32.mul': '*',
    'f64.mul': '*',
    'i32.div_s': '//',
    'i64.div_s': '//',
    'i32.div_u': '//',  # Note: need unsigned handling
    'i64.div_u': '//',
    'f32.div': '/',
    'f64.div': '/',
    'i32.rem_s': '%',
    'i64.rem_s': '%',
    'i32.rem_u': '%',
    'i64.rem_u': '%',
    'i32.and': '&',
    'i64.and': '&',
    'i32.or': '|',
    'i64.or': '|',
    'i32.xor': '^',
    'i64.xor': '^',
    'i32.shl': '<<',
    'i64.shl': '<<',
    'i32.shr_s': '>>',
    'i64.shr_s': '>>',
    'i32.shr_u': '>>',  # Note: need unsigned handling
    'i64.shr_u': '>>',
    'i32.rotl': 'rotl32',  # Custom function
    'i64.rotl': 'rotl64',
    'i32.rotr': 'rotr32',
    'i64.rotr': 'rotr64',
}

COMPARISON_OPS = {
    'i32.eq': '==',
    'i64.eq': '==',
    'f32.eq': '==',
    'f64.eq': '==',
    'i32.ne': '!=',
    'i64.ne': '!=',
    'f32.ne': '!=',
    'f64.ne': '!=',
    'i32.lt_s': '<',
    'i64.lt_s': '<',
    'i32.lt_u': '<',  # Note: unsigned
    'i64.lt_u': '<',
    'f32.lt': '<',
    'f64.lt': '<',
    'i32.gt_s': '>',
    'i64.gt_s': '>',
    'i32.gt_u': '>',
    'i64.gt_u': '>',
    'f32.gt': '>',
    'f64.gt': '>',
    'i32.le_s': '<=',
    'i64.le_s': '<=',
    'i32.le_u': '<=',
    'i64.le_u': '<=',
    'f32.le': '<=',
    'f64.le': '<=',
    'i32.ge_s': '>=',
    'i64.ge_s': '>=',
    'i32.ge_u': '>=',
    'i64.ge_u': '>=',
    'f32.ge': '>=',
    'f64.ge': '>=',
}

UNARY_OPS = {
    'i32.eqz': '== 0',
    'i64.eqz': '== 0',
    'i32.clz': 'clz32',
    'i64.clz': 'clz64',
    'i32.ctz': 'ctz32',
    'i64.ctz': 'ctz64',
    'i32.popcnt': 'popcnt32',
    'i64.popcnt': 'popcnt64',
    'f32.abs': 'abs',
    'f64.abs': 'abs',
    'f32.neg': '-',
    'f64.neg': '-',
    'f32.sqrt': 'math.sqrt',
    'f64.sqrt': 'math.sqrt',
    'f32.ceil': 'math.ceil',
    'f64.ceil': 'math.ceil',
    'f32.floor': 'math.floor',
    'f64.floor': 'math.floor',
    'f32.trunc': 'math.trunc',
    'f64.trunc': 'math.trunc',
    'f32.nearest': 'round',
    'f64.nearest': 'round',
}

CONVERT_OPS = {
    'i32.wrap_i64': 'i32',
    'i32.trunc_f32_s': 'int',
    'i32.trunc_f64_s': 'int',
    'i32.trunc_f32_u': 'int',
    'i32.trunc_f64_u': 'int',
    'i64.extend_i32_s': 'i64_extend_s',
    'i64.extend_i32_u': 'i64_extend_u',
    'i64.trunc_f32_s': 'int',
    'i64.trunc_f64_s': 'int',
    'f32.convert_i32_s': 'float',
    'f32.convert_i64_s': 'float',
    'f32.convert_i32_u': 'float',
    'f32.convert_i64_u': 'float',
    'f64.convert_i32_s': 'float',
    'f64.convert_i64_s': 'float',
    'f64.promote_f32': 'float',
    'f32.demote_f64': 'f32',
    'i32.reinterpret_f32': 'i32_reinterpret_f32',
    'i64.reinterpret_f64': 'i64_reinterpret_f64',
    'f32.reinterpret_i32': 'f32_reinterpret_i32',
    'f64.reinterpret_i64': 'f64_reinterpret_i64',
}

LOAD_OPS = {
    'i32.load': ('i32_load', 4),
    'i64.load': ('i64_load', 8),
    'f32.load': ('f32_load', 4),
    'f64.load': ('f64_load', 8),
    'i32.load8_s': ('i32_load8_s', 1),
    'i32.load8_u': ('i32_load8_u', 1),
    'i32.load16_s': ('i32_load16_s', 2),
    'i32.load16_u': ('i32_load16_u', 2),
    'i64.load8_s': ('i64_load8_s', 1),
    'i64.load8_u': ('i64_load8_u', 1),
    'i64.load16_s': ('i64_load16_s', 2),
    'i64.load16_u': ('i64_load16_u', 2),
    'i64.load32_s': ('i64_load32_s', 4),
    'i64.load32_u': ('i64_load32_u', 4),
    'i32.atomic.load': ('i32_atomic_load', 4),
    'i64.atomic.load': ('i64_atomic_load', 8),
}

STORE_OPS = {
    'i32.store': ('i32_store', 4),
    'i64.store': ('i64_store', 8),
    'f32.store': ('f32_store', 4),
    'f64.store': ('f64_store', 8),
    'i32.store8': ('i32_store8', 1),
    'i32.store16': ('i32_store16', 2),
    'i64.store8': ('i64_store8', 1),
    'i64.store16': ('i64_store16', 2),
    'i64.store32': ('i64_store32', 4),
    'i32.atomic.store': ('i32_atomic_store', 4),
    'i64.atomic.store': ('i64_atomic_store', 8),
}


@dataclass
class StackValue:
    """Represents a value on the simulated stack."""
    expr: str
    type: WatType = WatType.I32


@dataclass
class BlockContext:
    """Context for a block/loop/if."""
    kind: str  # 'block', 'loop', 'if'
    label: Optional[str]
    result_type: Optional[WatType]
    depth: int
    break_label: str  # Python label to break to


class CodeGenerator:
    """Generates Python code from WAT functions."""

    def __init__(self, module: WatModule, function_mapping: Optional[Dict[str, str]] = None):
        self.module = module
        # Map from WAT function name to Python function name
        self.function_mapping = function_mapping or {}
        self.imports_needed: Set[str] = set()

    def generate_function(self, func: WatFunction) -> str:
        """Generate Python code for a single function."""
        if func.is_import:
            return self._generate_import_stub(func)

        gen = FunctionGenerator(func, self.module, self.function_mapping)
        code = gen.generate()
        self.imports_needed.update(gen.imports_needed)
        return code

    def _generate_import_stub(self, func: WatFunction) -> str:
        """Generate a stub for an imported function."""
        params = ', '.join(p.name.lstrip('$') for p in func.params)
        result = func.results[0].value if func.results else 'None'
        py_name = self._func_name(func.name)

        lines = [
            f"def {py_name}({params}):",
            f"    # Import: {func.import_module}.{func.import_name}",
            f"    raise NotImplementedError('Import {func.import_module}.{func.import_name}')"
        ]
        return '\n'.join(lines)

    def _func_name(self, wat_name: str) -> str:
        """Convert WAT function name to Python name."""
        if wat_name in self.function_mapping:
            return self.function_mapping[wat_name]
        # Remove $ prefix
        name = wat_name.lstrip('$')
        # Replace dots with underscores
        name = name.replace('.', '_')
        return name

    def generate_module(self, functions: List[str] = None,
                       category: str = None,
                       max_functions: int = None) -> str:
        """Generate a Python module with multiple functions."""
        if functions is None:
            functions = [name for name, f in self.module.functions.items()
                        if not f.is_import]

        if max_functions:
            functions = functions[:max_functions]

        lines = [
            '"""',
            'Auto-generated Python code from WAT.',
            '"""',
            '',
            'from runtime import (',
            '    memory, i32_load, i64_load, f32_load, f64_load,',
            '    i32_store, i64_store, f32_store, f64_store,',
            '    i32_load8_s, i32_load8_u, i32_load16_s, i32_load16_u,',
            '    i64_load8_s, i64_load8_u, i64_load16_s, i64_load16_u,',
            '    i64_load32_s, i64_load32_u,',
            '    i32_store8, i32_store16, i64_store8, i64_store16, i64_store32,',
            '    global0, global1, global2, global3,',
            '    i32, i64, i64_extend_s, i64_extend_u,',
            '    rotl32, rotr32, rotl64, rotr64,',
            '    clz32, ctz32, popcnt32, clz64, ctz64, popcnt64,',
            ')',
            '',
        ]

        for func_name in functions:
            if func_name not in self.module.functions:
                continue
            func = self.module.functions[func_name]
            try:
                code = self.generate_function(func)
                lines.append(code)
                lines.append('')
                lines.append('')
            except Exception as e:
                lines.append(f"# Error generating {func_name}: {e}")
                lines.append('')

        return '\n'.join(lines)


class FunctionGenerator:
    """Generates Python code for a single WAT function."""

    def __init__(self, func: WatFunction, module: WatModule,
                 function_mapping: Dict[str, str] = None):
        self.func = func
        self.module = module
        self.function_mapping = function_mapping or {}

        self.stack: List[StackValue] = []
        self.lines: List[str] = []
        self.indent = 1
        self.temp_counter = 0
        self.block_stack: List[BlockContext] = []
        self.block_counter = 0
        self.imports_needed: Set[str] = set()

    def generate(self) -> str:
        """Generate Python code for the function."""
        # Function signature
        params = ', '.join(self._local_name(p.name) for p in self.func.params)
        result_type = self.func.results[0].value if self.func.results else None

        py_name = self._func_name(self.func.name)
        self.lines.append(f"def {py_name}({params}):")

        # Add docstring with original name if different
        if self.func.export_name:
            self._emit(f'"""Export: {self.func.export_name}"""')
        elif self.func.name != f"${py_name}":
            self._emit(f'# WAT: {self.func.name}')

        # Declare locals
        for local in self.func.locals:
            init_val = '0' if local.type in (WatType.I32, WatType.I64) else '0.0'
            self._emit(f"{self._local_name(local.name)} = {init_val}")

        # Generate body
        self._generate_block(self.func.body)

        # Handle return
        if self.func.results and self.stack:
            val = self.stack.pop()
            self._emit(f"return {val.expr}")
        elif self.func.results:
            self._emit("return 0  # Stack underflow")

        return '\n'.join(self.lines)

    def _generate_block(self, instructions: List[WatInstruction]):
        """Generate code for a block of instructions."""
        for instr in instructions:
            self._generate_instruction(instr)

    def _generate_instruction(self, instr: WatInstruction):
        """Generate code for a single instruction."""
        opcode = instr.opcode

        # Constants
        if opcode == 'i32.const':
            val = instr.operands[0] if instr.operands else 0
            self.stack.append(StackValue(str(val), WatType.I32))
            return
        if opcode == 'i64.const':
            val = instr.operands[0] if instr.operands else 0
            self.stack.append(StackValue(str(val), WatType.I64))
            return
        if opcode in ('f32.const', 'f64.const'):
            val = instr.operands[0] if instr.operands else 0.0
            typ = WatType.F32 if opcode.startswith('f32') else WatType.F64
            self.stack.append(StackValue(str(float(val)), typ))
            return

        # Local operations
        if opcode == 'local.get':
            name = instr.operands[0] if instr.operands else '$var0'
            local = self.func.get_local_by_name(name)
            typ = local.type if local else WatType.I32
            self.stack.append(StackValue(self._local_name(name), typ))
            return
        if opcode == 'local.set':
            name = instr.operands[0] if instr.operands else '$var0'
            val = self._pop()
            self._emit(f"{self._local_name(name)} = {val.expr}")
            return
        if opcode == 'local.tee':
            name = instr.operands[0] if instr.operands else '$var0'
            val = self._peek()
            self._emit(f"{self._local_name(name)} = {val.expr}")
            return

        # Global operations
        if opcode == 'global.get':
            name = instr.operands[0] if instr.operands else '$global0'
            self.stack.append(StackValue(self._global_name(name), WatType.I32))
            return
        if opcode == 'global.set':
            name = instr.operands[0] if instr.operands else '$global0'
            val = self._pop()
            self._emit(f"global {self._global_name(name)}")
            self._emit(f"{self._global_name(name)} = {val.expr}")
            return

        # Binary operations
        if opcode in BINARY_OPS:
            b = self._pop()
            a = self._pop()
            op = BINARY_OPS[opcode]
            if op in ('rotl32', 'rotr32', 'rotl64', 'rotr64'):
                self.stack.append(StackValue(f"{op}({a.expr}, {b.expr})", a.type))
            else:
                # Handle unsigned operations
                if '_u' in opcode and (opcode.endswith('shr_u') or opcode.endswith('div_u')):
                    if opcode.startswith('i32'):
                        self.stack.append(StackValue(f"(({a.expr} & 0xFFFFFFFF) {op} {b.expr})", WatType.I32))
                    else:
                        self.stack.append(StackValue(f"(({a.expr} & 0xFFFFFFFFFFFFFFFF) {op} {b.expr})", WatType.I64))
                else:
                    self.stack.append(StackValue(f"({a.expr} {op} {b.expr})", a.type))
            return

        # Comparison operations
        if opcode in COMPARISON_OPS:
            b = self._pop()
            a = self._pop()
            op = COMPARISON_OPS[opcode]
            self.stack.append(StackValue(f"(1 if {a.expr} {op} {b.expr} else 0)", WatType.I32))
            return

        # Unary operations
        if opcode in UNARY_OPS:
            a = self._pop()
            op = UNARY_OPS[opcode]
            if op == '== 0':
                self.stack.append(StackValue(f"(1 if {a.expr} == 0 else 0)", WatType.I32))
            elif op.startswith('-'):
                self.stack.append(StackValue(f"(-{a.expr})", a.type))
            elif op in ('clz32', 'ctz32', 'popcnt32', 'clz64', 'ctz64', 'popcnt64'):
                self.stack.append(StackValue(f"{op}({a.expr})", WatType.I32))
            elif op.startswith('math.'):
                self.imports_needed.add('math')
                self.stack.append(StackValue(f"{op}({a.expr})", a.type))
            else:
                self.stack.append(StackValue(f"{op}({a.expr})", a.type))
            return

        # Conversion operations
        if opcode in CONVERT_OPS:
            a = self._pop()
            op = CONVERT_OPS[opcode]
            result_type = WatType.I32
            if opcode.startswith('i64') or 'i64' in opcode:
                result_type = WatType.I64
            elif opcode.startswith('f32'):
                result_type = WatType.F32
            elif opcode.startswith('f64'):
                result_type = WatType.F64
            self.stack.append(StackValue(f"{op}({a.expr})", result_type))
            return

        # Load operations
        if opcode in LOAD_OPS:
            func_name, size = LOAD_OPS[opcode]
            addr = self._pop()
            offset = self._get_offset(instr.operands)
            if offset:
                self.stack.append(StackValue(f"{func_name}({addr.expr} + {offset})", WatType.I32))
            else:
                self.stack.append(StackValue(f"{func_name}({addr.expr})", WatType.I32))
            return

        # Store operations
        if opcode in STORE_OPS:
            func_name, size = STORE_OPS[opcode]
            val = self._pop()
            addr = self._pop()
            offset = self._get_offset(instr.operands)
            if offset:
                self._emit(f"{func_name}({addr.expr} + {offset}, {val.expr})")
            else:
                self._emit(f"{func_name}({addr.expr}, {val.expr})")
            return

        # Call operations
        if opcode == 'call':
            target = instr.operands[0] if instr.operands else '$func0'
            self._generate_call(target)
            return

        if opcode == 'call_indirect':
            # Pop the function index from stack
            idx = self._pop()
            # For now, generate a placeholder
            self._emit(f"# call_indirect via table[{idx.expr}]")
            self.stack.append(StackValue(f"call_indirect({idx.expr})", WatType.I32))
            return

        # Control flow
        if opcode == 'block':
            self._enter_block('block', instr.label, instr.block_type)
            self._generate_block(instr.children)
            self._exit_block()
            return

        if opcode == 'loop':
            self._enter_block('loop', instr.label, instr.block_type)
            label = self.block_stack[-1].break_label
            self._emit(f"while True:  # loop {instr.label or ''}")
            self.indent += 1
            self._generate_block(instr.children)
            self._emit("break  # end loop")
            self.indent -= 1
            self._exit_block()
            return

        if opcode == 'if':
            cond = self._pop()
            has_else = len(instr.else_children) > 0

            self._enter_block('if', instr.label, instr.block_type)

            self._emit(f"if {cond.expr}:")
            self.indent += 1
            if instr.children:
                self._generate_block(instr.children)
            else:
                self._emit("pass")
            self.indent -= 1

            if has_else:
                self._emit("else:")
                self.indent += 1
                self._generate_block(instr.else_children)
                self.indent -= 1

            self._exit_block()
            return

        if opcode == 'br':
            target = instr.operands[0] if instr.operands else 0
            self._generate_branch(target, conditional=False)
            return

        if opcode == 'br_if':
            target = instr.operands[0] if instr.operands else 0
            self._generate_branch(target, conditional=True)
            return

        if opcode == 'br_table':
            # Branch table - complex, generate switch-like code
            idx = self._pop()
            self._emit(f"# br_table {instr.operands}")
            self._emit(f"_br_idx = {idx.expr}")
            # For now, just break
            self._emit("break  # br_table")
            return

        if opcode == 'return':
            if self.func.results and self.stack:
                val = self._pop()
                self._emit(f"return {val.expr}")
            else:
                self._emit("return")
            return

        # Stack operations
        if opcode == 'drop':
            self._pop()
            return

        if opcode == 'select':
            cond = self._pop()
            b = self._pop()
            a = self._pop()
            self.stack.append(StackValue(f"({a.expr} if {cond.expr} else {b.expr})", a.type))
            return

        if opcode == 'unreachable':
            self._emit("raise RuntimeError('unreachable')")
            return

        if opcode == 'nop':
            return

        # Memory operations
        if opcode == 'memory.size':
            self.stack.append(StackValue("memory_size()", WatType.I32))
            return

        if opcode == 'memory.grow':
            pages = self._pop()
            self.stack.append(StackValue(f"memory_grow({pages.expr})", WatType.I32))
            return

        # Atomic operations (simplified)
        if 'atomic' in opcode:
            if 'load' in opcode:
                addr = self._pop()
                offset = self._get_offset(instr.operands)
                if offset:
                    self.stack.append(StackValue(f"i32_atomic_load({addr.expr} + {offset})", WatType.I32))
                else:
                    self.stack.append(StackValue(f"i32_atomic_load({addr.expr})", WatType.I32))
            elif 'store' in opcode:
                val = self._pop()
                addr = self._pop()
                offset = self._get_offset(instr.operands)
                if offset:
                    self._emit(f"i32_atomic_store({addr.expr} + {offset}, {val.expr})")
                else:
                    self._emit(f"i32_atomic_store({addr.expr}, {val.expr})")
            return

        # Reference operations
        if opcode == 'ref.func':
            target = instr.operands[0] if instr.operands else '$func0'
            self.stack.append(StackValue(f"ref_func('{target}')", WatType.I32))
            return

        # Unknown instruction
        self._emit(f"# Unknown: {opcode} {instr.operands}")

    def _generate_call(self, target: str):
        """Generate a function call."""
        # Get the target function to know param count
        target_func = self.module.functions.get(target)
        if target_func:
            param_count = len(target_func.params)
            has_result = len(target_func.results) > 0
        else:
            # Assume it's an import, guess params from stack
            param_count = 0
            has_result = True

        # Pop arguments in reverse order
        args = []
        for _ in range(param_count):
            if self.stack:
                args.insert(0, self._pop().expr)
            else:
                args.insert(0, '0  # stack underflow')

        py_name = self._func_name(target)
        call_expr = f"{py_name}({', '.join(args)})"

        if has_result:
            result_type = target_func.results[0] if target_func and target_func.results else WatType.I32
            self.stack.append(StackValue(call_expr, result_type))
        else:
            self._emit(call_expr)

    def _generate_branch(self, target: Union[str, int], conditional: bool):
        """Generate a branch instruction."""
        # Find target block
        if isinstance(target, str) and target.startswith('$'):
            # Named label
            for i, ctx in enumerate(reversed(self.block_stack)):
                if ctx.label == target:
                    target_idx = i
                    break
            else:
                target_idx = 0
        elif isinstance(target, int):
            target_idx = target
        else:
            target_idx = 0

        if target_idx < len(self.block_stack):
            target_ctx = self.block_stack[-(target_idx + 1)]
        else:
            target_ctx = None

        if conditional:
            cond = self._pop()
            self._emit(f"if {cond.expr}:")
            self.indent += 1

        if target_ctx and target_ctx.kind == 'loop':
            self._emit("continue")
        else:
            self._emit("break")

        if conditional:
            self.indent -= 1

    def _enter_block(self, kind: str, label: Optional[str], result_type: Optional[WatType]):
        """Enter a new block context."""
        self.block_counter += 1
        break_label = f"_block{self.block_counter}"
        ctx = BlockContext(
            kind=kind,
            label=label,
            result_type=result_type,
            depth=len(self.block_stack),
            break_label=break_label
        )
        self.block_stack.append(ctx)

    def _exit_block(self):
        """Exit the current block context."""
        if self.block_stack:
            self.block_stack.pop()

    def _pop(self) -> StackValue:
        """Pop a value from the stack."""
        if self.stack:
            return self.stack.pop()
        return StackValue("0  # stack underflow", WatType.I32)

    def _peek(self) -> StackValue:
        """Peek at the top of the stack."""
        if self.stack:
            return self.stack[-1]
        return StackValue("0  # stack underflow", WatType.I32)

    def _emit(self, line: str):
        """Emit a line of Python code."""
        indent = '    ' * self.indent
        self.lines.append(f"{indent}{line}")

    def _local_name(self, wat_name: str) -> str:
        """Convert WAT local name to Python name."""
        name = wat_name.lstrip('$')
        # Replace invalid chars
        name = name.replace('.', '_')
        # Avoid Python keywords
        if name in ('if', 'for', 'while', 'return', 'def', 'class', 'import', 'from', 'as', 'in', 'is', 'and', 'or', 'not', 'True', 'False', 'None'):
            name = f"_{name}"
        return name

    def _global_name(self, wat_name: str) -> str:
        """Convert WAT global name to Python name."""
        return wat_name.lstrip('$')

    def _func_name(self, wat_name: str) -> str:
        """Convert WAT function name to Python name."""
        if wat_name in self.function_mapping:
            return self.function_mapping[wat_name]
        name = wat_name.lstrip('$')
        name = name.replace('.', '_')
        return name

    def _get_offset(self, operands: List[Any]) -> Optional[int]:
        """Extract offset from operands."""
        for op in operands:
            if isinstance(op, tuple) and op[0] == 'offset':
                return op[1]
        return None

    def _new_temp(self) -> str:
        """Generate a new temporary variable name."""
        self.temp_counter += 1
        return f"_t{self.temp_counter}"


def generate_function(module: WatModule, func_name: str) -> str:
    """Generate Python code for a single function."""
    if func_name not in module.functions:
        raise ValueError(f"Function {func_name} not found")

    func = module.functions[func_name]
    gen = CodeGenerator(module)
    return gen.generate_function(func)


if __name__ == '__main__':
    import sys
    from wat_parser import parse_wat_file

    if len(sys.argv) < 2:
        print("Usage: codegen.py <wat_file> [function_name]")
        sys.exit(1)

    module = parse_wat_file(sys.argv[1])

    if len(sys.argv) > 2:
        func_name = sys.argv[2]
        if not func_name.startswith('$'):
            func_name = f"${func_name}"
        code = generate_function(module, func_name)
        print(code)
    else:
        # Generate first 5 non-import functions
        gen = CodeGenerator(module)
        count = 0
        for name, func in module.functions.items():
            if func.is_import:
                continue
            print(f"# {'='*60}")
            print(f"# {name}")
            print(f"# {'='*60}")
            try:
                code = gen.generate_function(func)
                print(code)
            except Exception as e:
                print(f"# Error: {e}")
            print()
            count += 1
            if count >= 5:
                break
