#!/usr/bin/env python3
"""
Context viewer for manual transpilation.

Shows complete context for a function:
- The function's WAT code
- All functions it calls (with their code if already transpiled)
- All functions that call it
- Dependencies status
- Suggested category and name
"""

import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

# Colors for terminal
class C:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

def load_tree(path: Path) -> dict:
    """Load the processing tree."""
    if not path.exists():
        print(f"{C.RED}Error: {path} not found{C.END}")
        print(f"Run: python tools/generate_tree.py first")
        sys.exit(1)
    return json.loads(path.read_text())

def load_wat(path: Path) -> str:
    """Load the WAT file."""
    return path.read_text()

def extract_function(wat_content: str, func_name: str) -> Optional[str]:
    """Extract a single function from WAT content."""
    lines = wat_content.split('\n')

    in_func = False
    func_lines = []
    brace_depth = 0
    start_depth = 0

    # Normalize name (handle both $name and name)
    search_name = func_name if func_name.startswith('$') else f'${func_name}'

    for line in lines:
        if f'(func {search_name} ' in line or f'(func {search_name}(' in line:
            in_func = True
            brace_depth = line.count('(') - line.count(')')
            start_depth = brace_depth
            func_lines = [line]
        elif in_func:
            brace_depth += line.count('(') - line.count(')')
            func_lines.append(line)

            if brace_depth < start_depth:
                return '\n'.join(func_lines)

    return None

def get_function_signature(wat_code: str) -> dict:
    """Parse function signature from WAT code."""
    sig = {
        'params': [],
        'result': None,
        'locals': [],
    }

    first_line = wat_code.split('\n')[0]

    # Extract params
    for match in re.finditer(r'\(param\s+(\$\w+)?\s*(\w+)\)', first_line):
        name = match.group(1) or ''
        typ = match.group(2)
        sig['params'].append({'name': name, 'type': typ})

    # Extract result
    result_match = re.search(r'\(result\s+(\w+)\)', first_line)
    if result_match:
        sig['result'] = result_match.group(1)

    # Extract locals
    for match in re.finditer(r'\(local\s+(\$\w+)\s+(\w+)\)', wat_code):
        sig['locals'].append({'name': match.group(1), 'type': match.group(2)})

    return sig

def analyze_function_body(wat_code: str) -> dict:
    """Analyze function body for patterns."""
    analysis = {
        'calls': [],
        'memory_ops': 0,
        'branches': 0,
        'loops': 0,
        'blocks': 0,
        'if_count': 0,
        'math_ops': 0,
        'line_count': len(wat_code.split('\n')),
    }

    for line in wat_code.split('\n'):
        stripped = line.strip()

        # Calls
        if 'call ' in stripped and 'call_indirect' not in stripped:
            match = re.search(r'call\s+(\$[\w.]+)', stripped)
            if match:
                analysis['calls'].append(match.group(1))

        # Memory
        if '.load' in stripped or '.store' in stripped:
            analysis['memory_ops'] += 1

        # Control flow
        if stripped.startswith('br') or 'br_if' in stripped:
            analysis['branches'] += 1
        if 'loop ' in stripped:
            analysis['loops'] += 1
        if 'block ' in stripped:
            analysis['blocks'] += 1
        if stripped == 'if' or stripped.startswith('if '):
            analysis['if_count'] += 1

        # Math
        if any(op in stripped for op in ['.add', '.sub', '.mul', '.div', '.sqrt']):
            analysis['math_ops'] += 1

    return analysis

def suggest_category(func_name: str, analysis: dict, calls: list) -> str:
    """Suggest a category based on analysis."""
    name_lower = func_name.lower()

    # Check name patterns
    if any(x in name_lower for x in ['vp8', 'webp', 'huffman', 'decode']):
        return 'webp'
    if 'func26' in name_lower or 'alloc' in name_lower:
        return 'memory'
    if 'af' == func_name.replace('$', '') or 'free' in name_lower:
        return 'memory'
    if any(x in name_lower for x in ['terrain', 'tile', 'map']):
        return 'terrain'
    if any(x in name_lower for x in ['unit', 'soldier', 'peasant']):
        return 'units'
    if any(x in name_lower for x in ['building', 'construct']):
        return 'buildings'
    if any(x in name_lower for x in ['path', 'astar', 'find']):
        return 'pathfinding'
    if any(x in name_lower for x in ['ai', 'enemy', 'target']):
        return 'ai'
    if any(x in name_lower for x in ['render', 'draw', 'sprite']):
        return 'render'
    if any(x in name_lower for x in ['sound', 'audio', 'music']):
        return 'audio'
    if any(x in name_lower for x in ['net', 'sync', 'fetch']):
        return 'network'

    # Check by what it calls
    call_names = ' '.join(calls).lower()
    if 'vp8' in call_names or 'webp' in call_names:
        return 'webp'
    if 'alloc' in call_names or 'func26' in call_names:
        return 'memory'

    # Check by characteristics
    if analysis['math_ops'] > 10 and analysis['memory_ops'] < 5:
        return 'math'
    if analysis['memory_ops'] > 20:
        return 'memory'

    # Is it an import?
    if '.' in func_name:
        return 'imports'

    return 'unknown'

def show_context(func_name: str, tree_path: Path, wat_path: Path, tzar_path: Path):
    """Show complete context for a function."""
    tree = load_tree(tree_path)
    wat_content = load_wat(wat_path)

    # Normalize name
    if not func_name.startswith('$'):
        func_name = f'${func_name}'

    # Get function info from tree
    func_info = tree['functions'].get(func_name)
    if not func_info:
        print(f"{C.RED}Function {func_name} not found in tree{C.END}")
        print(f"\nAvailable functions matching pattern:")
        for fid in tree['functions']:
            if func_name.replace('$', '') in fid:
                print(f"  {fid}")
        return

    # Extract WAT code
    wat_code = extract_function(wat_content, func_name)
    if not wat_code:
        print(f"{C.RED}Could not extract WAT code for {func_name}{C.END}")
        return

    sig = get_function_signature(wat_code)
    analysis = analyze_function_body(wat_code)
    category = suggest_category(func_name, analysis, func_info['calls'])

    # Check transpilation status of dependencies
    deps_status = {}
    for dep in func_info['calls']:
        py_file = find_transpiled(dep, tzar_path)
        deps_status[dep] = 'done' if py_file else 'pending'

    all_deps_done = all(s == 'done' for s in deps_status.values()) if deps_status else True

    # Print context
    print(f"\n{'='*70}")
    print(f"{C.BOLD}{C.CYAN}  CONTEXT: {func_name}{C.END}")
    print(f"{'='*70}")

    # Status
    print(f"\n{C.BOLD}📋 Status:{C.END}")
    status_color = C.GREEN if func_info['status'] == 'done' else C.YELLOW
    print(f"   Function status: {status_color}{func_info['status']}{C.END}")
    deps_color = C.GREEN if all_deps_done else C.RED
    print(f"   Dependencies:    {deps_color}{'all done' if all_deps_done else 'PENDING'}{C.END}")
    print(f"   Depth:           {func_info['depth']}")
    print(f"   Suggested cat:   {C.BLUE}{category}{C.END}")

    if func_info['is_import']:
        print(f"   {C.DIM}[IMPORT - external function]{C.END}")
    if func_info['is_export']:
        print(f"   {C.GREEN}[EXPORT - entry point]{C.END}")
    if func_info['scc_id'] is not None:
        print(f"   {C.YELLOW}[IN CYCLE - SCC {func_info['scc_id']}]{C.END}")

    # Signature
    print(f"\n{C.BOLD}📝 Signature:{C.END}")
    params_str = ', '.join([f"{p['name']}: {p['type']}" for p in sig['params']]) or 'none'
    result_str = sig['result'] or 'void'
    print(f"   Params:  {params_str}")
    print(f"   Returns: {result_str}")
    if sig['locals']:
        locals_str = ', '.join([f"{l['name']}: {l['type']}" for l in sig['locals']])
        print(f"   Locals:  {locals_str}")

    # Analysis
    print(f"\n{C.BOLD}🔍 Analysis:{C.END}")
    print(f"   Lines:       {analysis['line_count']}")
    print(f"   Memory ops:  {analysis['memory_ops']}")
    print(f"   Math ops:    {analysis['math_ops']}")
    print(f"   Branches:    {analysis['branches']}")
    print(f"   Loops:       {analysis['loops']}")
    print(f"   Blocks:      {analysis['blocks']}")
    print(f"   If/else:     {analysis['if_count']}")

    # Calls (dependencies)
    print(f"\n{C.BOLD}📞 Calls ({len(func_info['calls'])}):{C.END}")
    if func_info['calls']:
        for dep in func_info['calls']:
            status = deps_status.get(dep, 'pending')
            icon = '✅' if status == 'done' else '⏳'
            dep_info = tree['functions'].get(dep, {})
            depth = dep_info.get('depth', '?')
            print(f"   {icon} {dep} (depth {depth})")
    else:
        print(f"   {C.GREEN}(none - this is a leaf!){C.END}")

    # Called by
    print(f"\n{C.BOLD}📥 Called by ({len(func_info['called_by'])}):{C.END}")
    if func_info['called_by']:
        for caller in func_info['called_by'][:10]:
            caller_info = tree['functions'].get(caller, {})
            depth = caller_info.get('depth', '?')
            print(f"   ← {caller} (depth {depth})")
        if len(func_info['called_by']) > 10:
            print(f"   ... and {len(func_info['called_by']) - 10} more")
    else:
        print(f"   {C.DIM}(none - entry point or unused){C.END}")

    # WAT Code
    print(f"\n{C.BOLD}📄 WAT Code:{C.END}")
    print(f"{C.DIM}{'─'*70}{C.END}")
    # Limit output
    lines = wat_code.split('\n')
    if len(lines) > 50:
        for line in lines[:25]:
            print(f"  {line}")
        print(f"\n  {C.DIM}... ({len(lines) - 50} lines omitted) ...{C.END}\n")
        for line in lines[-25:]:
            print(f"  {line}")
    else:
        for line in lines:
            print(f"  {line}")
    print(f"{C.DIM}{'─'*70}{C.END}")

    # Ready to transpile?
    print(f"\n{C.BOLD}🚀 Ready to Transpile?{C.END}")
    if not all_deps_done:
        print(f"   {C.RED}NO - Process these first:{C.END}")
        for dep, status in deps_status.items():
            if status == 'pending':
                print(f"      → {dep}")
    else:
        print(f"   {C.GREEN}YES - All dependencies are done!{C.END}")
        print(f"\n   Suggested file: tzar/{category}/{func_name.replace('$', '')}.py")

    print(f"\n{'='*70}\n")

def find_transpiled(func_name: str, tzar_path: Path) -> Optional[Path]:
    """Find if a function has been transpiled."""
    name = func_name.replace('$', '').replace('.', '_')

    # Search in tzar directory
    for py_file in tzar_path.rglob(f'{name}.py'):
        return py_file

    return None

def show_next(tree_path: Path, tzar_path: Path):
    """Show next functions ready to transpile."""
    tree = load_tree(tree_path)

    ready = []
    for func_id, func_info in tree['functions'].items():
        if func_info['status'] != 'pending':
            continue
        if func_info['is_import']:
            continue

        # Check if all dependencies are done
        all_done = True
        for dep in func_info['calls']:
            dep_info = tree['functions'].get(dep, {})
            if dep_info.get('status') != 'done' and not dep_info.get('is_import', False):
                # Check if transpiled
                if not find_transpiled(dep, tzar_path):
                    all_done = False
                    break

        if all_done:
            ready.append(func_info)

    # Sort by depth (leaves first)
    ready.sort(key=lambda x: (x['depth'], len(x['calls'])))

    print(f"\n{'='*60}")
    print(f"{C.BOLD}  NEXT FUNCTIONS READY TO TRANSPILE{C.END}")
    print(f"{'='*60}")
    print(f"\nTotal ready: {len(ready)}")

    for i, func in enumerate(ready[:20]):
        print(f"\n  {i+1}. {C.CYAN}{func['id']}{C.END}")
        print(f"     Depth: {func['depth']} | Calls: {len(func['calls'])} | Called by: {len(func['called_by'])}")

    if len(ready) > 20:
        print(f"\n  ... and {len(ready) - 20} more")

    print(f"\n{'='*60}\n")

def main():
    tree_path = Path('tzar/_tree.json')
    wat_path = Path('mgame')
    tzar_path = Path('tzar')

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tools/context.py <function_name>  - Show context for function")
        print("  python tools/context.py --next           - Show next functions ready")
        print("\nExamples:")
        print("  python tools/context.py func26")
        print("  python tools/context.py '$af'")
        print("  python tools/context.py --next")
        sys.exit(1)

    if sys.argv[1] == '--next':
        show_next(tree_path, tzar_path)
    else:
        show_context(sys.argv[1], tree_path, wat_path, tzar_path)

if __name__ == '__main__':
    main()
