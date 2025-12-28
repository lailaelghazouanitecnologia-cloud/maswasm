#!/usr/bin/env python3
"""
Function extractor for Tzar WASM
Extracts individual functions to separate files
"""

import re
import json
import sys
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class FunctionInfo:
    name: str
    index: int
    is_import: bool
    is_export: bool
    params: list
    result: Optional[str]
    line_start: int
    line_end: int
    calls: list
    size_lines: int

def extract_functions(filepath: Path, output_dir: Path, limit: Optional[int] = None):
    """Extract functions from WAT file."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')
    lines = content.split('\n')

    output_dir.mkdir(parents=True, exist_ok=True)

    functions = []
    current_func = None
    func_lines = []
    brace_depth = 0
    start_depth = 0

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Update brace depth
        brace_depth += line.count('(') - line.count(')')

        # Detect function start
        if stripped.startswith('(func '):
            current_func = parse_func_header(stripped, i)
            func_lines = [line]
            start_depth = brace_depth

        elif current_func is not None:
            func_lines.append(line)

            # Check function end
            if brace_depth < start_depth:
                current_func.line_end = i
                current_func.size_lines = len(func_lines)

                # Extract calls from body
                body = '\n'.join(func_lines)
                current_func.calls = extract_calls(body)

                functions.append(current_func)

                # Save to file
                if limit is None or len(functions) <= limit:
                    save_function(output_dir, current_func, func_lines)

                current_func = None
                func_lines = []

    # Save index
    index = [asdict(f) for f in functions]
    index_path = output_dir / '_index.json'
    index_path.write_text(json.dumps(index, indent=2))

    print(f"Extracted {len(functions)} functions to {output_dir}")
    return functions

def parse_func_header(line: str, line_num: int) -> FunctionInfo:
    """Parse function header line."""
    info = FunctionInfo(
        name='',
        index=0,
        is_import='(import ' in line,
        is_export='(export ' in line,
        params=[],
        result=None,
        line_start=line_num,
        line_end=line_num,
        calls=[],
        size_lines=1
    )

    # Extract name
    name_match = re.search(r'\$([^\s(]+)', line)
    if name_match:
        info.name = '$' + name_match.group(1)

    # Extract index
    index_match = re.search(r'\(;(\d+);\)', line)
    if index_match:
        info.index = int(index_match.group(1))

    # Extract params
    for match in re.finditer(r'\(param[^)]*\)', line):
        param_str = match.group(0)
        types = re.findall(r'(i32|i64|f32|f64)', param_str)
        info.params.extend(types)

    # Extract result
    result_match = re.search(r'\(result\s+(\w+)\)', line)
    if result_match:
        info.result = result_match.group(1)

    return info

def extract_calls(body: str) -> list:
    """Extract function calls from body."""
    calls = set()

    # Find direct calls
    for match in re.finditer(r'call\s+(\$[^\s)]+)', body):
        target = match.group(1)
        if not target.startswith('$var') and not target.startswith('$label'):
            calls.add(target)

    return sorted(list(calls))

def save_function(output_dir: Path, func: FunctionInfo, lines: list):
    """Save function to file."""
    # Sanitize filename
    name = func.name.replace('$', '').replace('.', '_').replace('/', '_')
    filename = f"{name}.wat"
    filepath = output_dir / filename

    # Write with metadata header
    header = f""";; ============================================
;; Function: {func.name}
;; Index: {func.index}
;; Lines: {func.line_start} - {func.line_end}
;; Import: {func.is_import}
;; Export: {func.is_export}
;; Params: {', '.join(func.params)}
;; Result: {func.result or 'void'}
;; Calls: {', '.join(func.calls[:10])}{'...' if len(func.calls) > 10 else ''}
;; ============================================

"""

    content = header + '\n'.join(lines)
    filepath.write_text(content)

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_functions.py <wat_file> [output_dir] [limit]")
        sys.exit(1)

    wat_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('output/functions')
    limit = int(sys.argv[3]) if len(sys.argv) > 3 else None

    if not wat_file.exists():
        print(f"Error: {wat_file} not found")
        sys.exit(1)

    extract_functions(wat_file, output_dir, limit)

if __name__ == '__main__':
    main()
