"""
WAT (WebAssembly Text) Parser for automatic transpilation to Python.

This module parses WAT code and produces an AST that can be used
for code generation. Handles the full WAT instruction set.
"""

import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, Any, Union
from enum import Enum


class WatType(Enum):
    I32 = "i32"
    I64 = "i64"
    F32 = "f32"
    F64 = "f64"
    VOID = "void"


@dataclass
class WatParam:
    name: str
    type: WatType
    index: int = 0


@dataclass
class WatLocal:
    name: str
    type: WatType
    index: int = 0


@dataclass
class WatInstruction:
    opcode: str
    operands: List[Any] = field(default_factory=list)
    block_type: Optional[WatType] = None
    label: Optional[str] = None
    children: List['WatInstruction'] = field(default_factory=list)
    else_children: List['WatInstruction'] = field(default_factory=list)

    def __repr__(self):
        if self.children:
            return f"WatInstruction({self.opcode}, {self.operands}, children={len(self.children)})"
        return f"WatInstruction({self.opcode}, {self.operands})"


@dataclass
class WatFunction:
    name: str
    index: int
    export_name: Optional[str]
    params: List[WatParam]
    results: List[WatType]
    locals: List[WatLocal]
    body: List[WatInstruction]
    is_import: bool = False
    import_module: Optional[str] = None
    import_name: Optional[str] = None

    @property
    def all_locals(self) -> List[Union[WatParam, WatLocal]]:
        """Get all local variables (params + locals) in order."""
        return list(self.params) + list(self.locals)

    def get_local_by_name(self, name: str) -> Optional[Union[WatParam, WatLocal]]:
        """Get a local variable by name."""
        for p in self.params:
            if p.name == name:
                return p
        for l in self.locals:
            if l.name == name:
                return l
        return None

    def get_local_by_index(self, idx: int) -> Optional[Union[WatParam, WatLocal]]:
        """Get a local variable by index."""
        all_locals = self.all_locals
        if 0 <= idx < len(all_locals):
            return all_locals[idx]
        return None


@dataclass
class WatGlobal:
    name: str
    type: WatType
    mutable: bool
    init_value: Any


@dataclass
class WatModule:
    functions: Dict[str, WatFunction]
    globals: Dict[str, WatGlobal]
    imports: List[WatFunction]
    exports: Dict[str, str]  # export_name -> func_name
    memory_pages: int = 880
    function_table: List[str] = field(default_factory=list)


class WatTokenizer:
    """Tokenizer for WAT format."""

    def __init__(self, content: str):
        self.content = content
        self.pos = 0
        self.length = len(content)

    def skip_whitespace(self):
        while self.pos < self.length:
            c = self.content[self.pos]
            if c in ' \t\n\r':
                self.pos += 1
            elif c == ';':
                # Skip comment
                if self.pos + 1 < self.length and self.content[self.pos + 1] == ';':
                    # Line comment
                    while self.pos < self.length and self.content[self.pos] != '\n':
                        self.pos += 1
                else:
                    # Block comment (;...;)
                    self.pos += 1
                    while self.pos < self.length - 1:
                        if self.content[self.pos] == ';' and self.content[self.pos + 1] == ')':
                            self.pos += 2
                            break
                        self.pos += 1
            elif self.pos + 1 < self.length and c == '(' and self.content[self.pos + 1] == ';':
                # Block comment
                self.pos += 2
                depth = 1
                while self.pos < self.length - 1 and depth > 0:
                    if self.content[self.pos] == '(' and self.content[self.pos + 1] == ';':
                        depth += 1
                        self.pos += 2
                    elif self.content[self.pos] == ';' and self.content[self.pos + 1] == ')':
                        depth -= 1
                        self.pos += 2
                    else:
                        self.pos += 1
            else:
                break

    def peek(self) -> str:
        self.skip_whitespace()
        if self.pos >= self.length:
            return ''
        return self.content[self.pos]

    def read_token(self) -> str:
        self.skip_whitespace()
        if self.pos >= self.length:
            return ''

        c = self.content[self.pos]

        if c == '(' or c == ')':
            self.pos += 1
            return c

        if c == '"':
            # String literal
            self.pos += 1
            start = self.pos
            while self.pos < self.length and self.content[self.pos] != '"':
                if self.content[self.pos] == '\\':
                    self.pos += 1
                self.pos += 1
            result = self.content[start:self.pos]
            self.pos += 1
            return f'"{result}"'

        # Regular token
        start = self.pos
        while self.pos < self.length:
            c = self.content[self.pos]
            if c in ' \t\n\r()";':
                break
            self.pos += 1

        return self.content[start:self.pos]


class WatParser:
    """Parser for WebAssembly Text format."""

    def __init__(self, wat_content: str):
        self.content = wat_content
        self.tokenizer = WatTokenizer(wat_content)
        self.functions: Dict[str, WatFunction] = {}
        self.globals: Dict[str, WatGlobal] = {}
        self.imports: List[WatFunction] = []
        self.exports: Dict[str, str] = {}
        self.func_index = 0

    def parse(self) -> WatModule:
        """Parse the entire WAT module."""
        # Parse module structure using regex for reliability
        self._parse_globals()
        self._parse_functions()
        self._extract_exports()

        return WatModule(
            functions=self.functions,
            globals=self.globals,
            imports=self.imports,
            exports=self.exports,
            function_table=[]
        )

    def _parse_globals(self):
        """Parse global variable declarations."""
        pattern = r'\(global\s+(\$\w+)\s+\(mut\s+(i32|i64|f32|f64)\)\s+\((i32|i64|f32|f64)\.const\s+([^\)]+)\)\)'
        for match in re.finditer(pattern, self.content):
            name = match.group(1)
            type_ = WatType(match.group(2))
            init_val = int(match.group(4))
            self.globals[name] = WatGlobal(
                name=name,
                type=type_,
                mutable=True,
                init_value=init_val
            )

    def _parse_functions(self):
        """Parse all function definitions."""
        # Find function boundaries using balanced parentheses
        func_starts = []
        for match in re.finditer(r'\(func\s+(\$[\w.]+)', self.content):
            func_starts.append((match.start(), match.group(1)))

        for i, (start, func_name) in enumerate(func_starts):
            func_code = self._extract_balanced(start)
            try:
                func = self._parse_function(func_name, func_code)
                if func.is_import:
                    self.imports.append(func)
                self.functions[func_name] = func
            except Exception as e:
                # Log error but continue
                print(f"Warning: Failed to parse {func_name}: {e}")

    def _extract_balanced(self, start: int) -> str:
        """Extract balanced parentheses starting from position."""
        depth = 0
        i = start
        while i < len(self.content):
            if self.content[i] == '(':
                depth += 1
            elif self.content[i] == ')':
                depth -= 1
                if depth == 0:
                    return self.content[start:i+1]
            i += 1
        return self.content[start:]

    def _parse_function(self, name: str, code: str) -> WatFunction:
        """Parse a single function definition."""
        # Extract function index from comment if present (;N;)
        idx_match = re.search(r'\(;(\d+);\)', code)
        func_idx = int(idx_match.group(1)) if idx_match else self.func_index
        self.func_index = max(self.func_index, func_idx + 1)

        # Check if import
        import_match = re.search(r'\(import\s+"([^"]+)"\s+"([^"]+)"\)', code)
        if import_match:
            return WatFunction(
                name=name,
                index=func_idx,
                export_name=None,
                params=self._parse_params(code),
                results=self._parse_results(code),
                locals=[],
                body=[],
                is_import=True,
                import_module=import_match.group(1),
                import_name=import_match.group(2)
            )

        # Check for export
        export_match = re.search(r'\(export\s+"([^"]+)"\)', code)
        export_name = export_match.group(1) if export_match else None

        # Parse params, results, locals
        params = self._parse_params(code)
        results = self._parse_results(code)
        locals_ = self._parse_locals(code, len(params))

        # Parse body
        body = self._parse_body(code, params, locals_)

        return WatFunction(
            name=name,
            index=func_idx,
            export_name=export_name,
            params=params,
            results=results,
            locals=locals_,
            body=body
        )

    def _parse_params(self, code: str) -> List[WatParam]:
        """Parse function parameters."""
        params = []
        # Match (param $name type) or (param type)
        for match in re.finditer(r'\(param\s+(\$\w+)?\s*(i32|i64|f32|f64)\)', code):
            name = match.group(1) or f"$param{len(params)}"
            type_ = WatType(match.group(2))
            params.append(WatParam(name=name, type=type_, index=len(params)))
        return params

    def _parse_results(self, code: str) -> List[WatType]:
        """Parse function results."""
        results = []
        for match in re.finditer(r'\(result\s+(i32|i64|f32|f64)\)', code):
            results.append(WatType(match.group(1)))
        return results

    def _parse_locals(self, code: str, param_count: int) -> List[WatLocal]:
        """Parse local variables."""
        locals_ = []
        for match in re.finditer(r'\(local\s+(\$\w+)\s+(i32|i64|f32|f64)\)', code):
            locals_.append(WatLocal(
                name=match.group(1),
                type=WatType(match.group(2)),
                index=param_count + len(locals_)
            ))
        return locals_

    def _parse_body(self, code: str, params: List[WatParam], locals_: List[WatLocal]) -> List[WatInstruction]:
        """Parse function body instructions with proper nesting."""
        # Find the start of actual instructions
        # Skip past func declaration, params, results, locals
        lines = code.split('\n')

        instructions = []
        block_stack = [instructions]  # Stack for nested blocks

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            i += 1

            # Skip declarations and empty lines
            if not line or line.startswith('(func') or line.startswith('(param') or \
               line.startswith('(result') or line.startswith('(local') or \
               line.startswith('(export') or line.startswith('(import') or \
               line == ')' or re.match(r'^\(;\d+;\)$', line):
                continue

            # Remove inline comments (;...;)
            line = re.sub(r'\(;[^;]*;\)', '', line).strip()
            if not line:
                continue

            # Parse the instruction
            instr = self._parse_instruction_line(line)
            if instr is None:
                continue

            # Handle block structure
            if instr.opcode in ('block', 'loop', 'if'):
                block_stack[-1].append(instr)
                block_stack.append(instr.children)
            elif instr.opcode == 'else':
                if len(block_stack) > 1:
                    block_stack.pop()
                    # Find the parent if instruction
                    parent_block = block_stack[-1]
                    if parent_block and len(parent_block) > 0:
                        parent_if = parent_block[-1]
                        if parent_if.opcode == 'if':
                            block_stack.append(parent_if.else_children)
            elif instr.opcode == 'end':
                if len(block_stack) > 1:
                    block_stack.pop()
            else:
                block_stack[-1].append(instr)

        return instructions

    def _parse_instruction_line(self, line: str) -> Optional[WatInstruction]:
        """Parse a single instruction line."""
        line = line.strip()
        if not line:
            return None

        # Clean up trailing parentheses
        while line.endswith(')') and line.count(')') > line.count('('):
            line = line[:-1].strip()

        # Handle block instructions with labels and types
        block_match = re.match(r'(block|loop)\s*(\$\w+)?(?:\s+\(result\s+(i32|i64|f32|f64)\))?', line)
        if block_match:
            opcode = block_match.group(1)
            label = block_match.group(2)
            result_type = WatType(block_match.group(3)) if block_match.group(3) else None
            return WatInstruction(opcode=opcode, label=label, block_type=result_type)

        if line.startswith('if'):
            # Check for result type
            result_match = re.search(r'\(result\s+(i32|i64|f32|f64)\)', line)
            result_type = WatType(result_match.group(1)) if result_match else None
            return WatInstruction(opcode='if', block_type=result_type)

        if line.startswith('else'):
            return WatInstruction(opcode='else')

        if line.startswith('end'):
            label_match = re.match(r'end\s*(\$\w+)?', line)
            label = label_match.group(1) if label_match else None
            return WatInstruction(opcode='end', label=label)

        # Handle regular instructions
        parts = self._tokenize_instruction(line)
        if not parts:
            return None

        opcode = parts[0]
        operands = self._parse_operands(parts[1:])

        return WatInstruction(opcode=opcode, operands=operands)

    def _tokenize_instruction(self, line: str) -> List[str]:
        """Tokenize an instruction line into parts."""
        parts = []
        current = ''
        in_paren = 0

        for c in line:
            if c == '(':
                in_paren += 1
                current += c
            elif c == ')':
                in_paren -= 1
                current += c
            elif c in ' \t' and in_paren == 0:
                if current:
                    parts.append(current)
                    current = ''
            else:
                current += c

        if current:
            parts.append(current)

        return parts

    def _parse_operands(self, parts: List[str]) -> List[Any]:
        """Parse instruction operands."""
        operands = []

        for part in parts:
            if part.startswith('$'):
                operands.append(part)  # Variable or label reference
            elif part.startswith('offset='):
                operands.append(('offset', int(part.split('=')[1])))
            elif part.startswith('align='):
                operands.append(('align', int(part.split('=')[1])))
            elif part.startswith('('):
                # Nested instruction - parse it
                operands.append(('nested', part))
            else:
                # Try to parse as number
                try:
                    if '.' in part or 'e' in part.lower():
                        operands.append(float(part))
                    else:
                        operands.append(int(part))
                except ValueError:
                    operands.append(part)

        return operands

    def _extract_exports(self):
        """Extract export mappings."""
        # Match (export "name") inside function definitions
        for name, func in self.functions.items():
            if func.export_name:
                self.exports[func.export_name] = name


def parse_wat_file(filepath: str) -> WatModule:
    """Parse a WAT file and return the module."""
    with open(filepath, 'r') as f:
        content = f.read()
    parser = WatParser(content)
    return parser.parse()


def analyze_function(func: WatFunction) -> Dict[str, Any]:
    """Quick analysis of a function."""
    stats = {
        'name': func.name,
        'export': func.export_name,
        'params': len(func.params),
        'results': len(func.results),
        'locals': len(func.locals),
        'instructions': 0,
        'calls': [],
        'loads': 0,
        'stores': 0,
        'branches': 0,
        'loops': 0,
        'blocks': 0,
    }

    def count_instructions(instrs: List[WatInstruction]):
        for instr in instrs:
            stats['instructions'] += 1

            if instr.opcode.startswith('call'):
                if instr.operands:
                    stats['calls'].append(instr.operands[0])
            elif 'load' in instr.opcode:
                stats['loads'] += 1
            elif 'store' in instr.opcode:
                stats['stores'] += 1
            elif instr.opcode.startswith('br'):
                stats['branches'] += 1
            elif instr.opcode == 'loop':
                stats['loops'] += 1
            elif instr.opcode == 'block':
                stats['blocks'] += 1

            if instr.children:
                count_instructions(instr.children)
            if instr.else_children:
                count_instructions(instr.else_children)

    count_instructions(func.body)
    return stats


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        module = parse_wat_file(sys.argv[1])
        print(f"Parsed {len(module.functions)} functions")
        print(f"  - Imports: {len(module.imports)}")
        print(f"  - Exports: {len(module.exports)}")
        print(f"  - Globals: {len(module.globals)}")

        print("\nSample functions:")
        count = 0
        for name, func in module.functions.items():
            if not func.is_import:
                stats = analyze_function(func)
                print(f"  {name}: {stats['params']} params, {stats['instructions']} instrs, calls: {stats['calls'][:3]}")
                count += 1
                if count >= 10:
                    break
