#!/usr/bin/env python3
"""
Main CLI for WAT to Python transpilation.

Usage:
    python transpile.py mgame --output tzar/
    python transpile.py mgame --function func26
    python transpile.py mgame --analyze-only
    python transpile.py mgame --batch --lines-per-module 2000
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, List, Set, Optional
from collections import defaultdict

from wat_parser import parse_wat_file, WatModule, WatFunction
from analyzer import analyze_module, DependencyGraph, FunctionCategory, print_analysis_summary
from codegen import CodeGenerator, generate_function


def transpile_single(module: WatModule, func_name: str) -> str:
    """Transpile a single function."""
    if not func_name.startswith('$'):
        func_name = f"${func_name}"

    if func_name not in module.functions:
        raise ValueError(f"Function {func_name} not found")

    return generate_function(module, func_name)


def create_project_structure(output_dir: Path):
    """Create the output project structure."""
    dirs = [
        output_dir,
        output_dir / "core",
        output_dir / "memory",
        output_dir / "entities",
        output_dir / "players",
        output_dir / "game",
        output_dir / "render",
        output_dir / "input",
        output_dir / "utils",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    # Create __init__.py files
    for d in dirs:
        init_file = d / "__init__.py"
        if not init_file.exists():
            init_file.write_text("")


def get_module_for_function(analysis, func_name: str) -> str:
    """Determine which module a function belongs to."""
    if func_name not in analysis.functions:
        return "game"

    func_analysis = analysis.functions[func_name]
    category = func_analysis.category

    if category == FunctionCategory.MEMORY:
        return "memory"
    elif category == FunctionCategory.PLAYER:
        return "players"
    elif category == FunctionCategory.ENTITY:
        return "entities"
    elif category == FunctionCategory.ACCESSOR:
        return "utils"
    elif category == FunctionCategory.MATH:
        return "utils"
    elif category == FunctionCategory.WRAPPER:
        return "utils"
    else:
        return "game"


def estimate_lines(module: WatModule, func: WatFunction) -> int:
    """Estimate number of Python lines for a function."""
    def count_instrs(instrs):
        total = len(instrs)
        for i in instrs:
            if i.children:
                total += count_instrs(i.children)
            if i.else_children:
                total += count_instrs(i.else_children)
        return total

    instr_count = count_instrs(func.body)
    # Rough estimate: 1.5 lines per instruction + overhead
    return int(instr_count * 1.5) + 5 + len(func.params) + len(func.locals)


def batch_transpile(module: WatModule, analysis: DependencyGraph,
                   output_dir: Path, lines_per_module: int = 2000):
    """Batch transpile all functions into organized modules."""

    create_project_structure(output_dir)

    # Group functions by category
    modules: Dict[str, List[str]] = defaultdict(list)

    # Process in topological order (leaves first)
    for func_name in analysis.get_topological_order():
        if func_name not in module.functions:
            continue
        func = module.functions[func_name]
        if func.is_import:
            continue

        mod_name = get_module_for_function(analysis, func_name)
        modules[mod_name].append(func_name)

    # Generate each module
    gen = CodeGenerator(module)
    stats = {
        'total_functions': 0,
        'successful': 0,
        'failed': 0,
        'modules_created': 0,
    }

    for mod_name, func_names in modules.items():
        print(f"\nGenerating {mod_name}/...")

        # Split into sub-modules if too large
        current_lines = 0
        current_funcs = []
        sub_module_idx = 0

        for func_name in func_names:
            func = module.functions[func_name]
            est_lines = estimate_lines(module, func)

            if current_lines + est_lines > lines_per_module and current_funcs:
                # Write current module
                _write_module(gen, module, current_funcs,
                            output_dir / mod_name / f"funcs_{sub_module_idx}.py",
                            stats)
                sub_module_idx += 1
                current_funcs = []
                current_lines = 0

            current_funcs.append(func_name)
            current_lines += est_lines

        # Write remaining functions
        if current_funcs:
            if sub_module_idx == 0:
                filename = f"funcs.py"
            else:
                filename = f"funcs_{sub_module_idx}.py"
            _write_module(gen, module, current_funcs,
                        output_dir / mod_name / filename,
                        stats)
            stats['modules_created'] += 1

    # Generate exports.py
    _generate_exports(module, output_dir)

    # Copy runtime
    runtime_src = Path(__file__).parent / "runtime.py"
    runtime_dst = output_dir / "runtime.py"
    if runtime_src.exists():
        runtime_dst.write_text(runtime_src.read_text())

    print(f"\n{'='*60}")
    print(f"Transpilation complete!")
    print(f"  Total functions: {stats['total_functions']}")
    print(f"  Successful: {stats['successful']}")
    print(f"  Failed: {stats['failed']}")
    print(f"  Modules created: {stats['modules_created']}")
    print(f"  Output directory: {output_dir}")


def _write_module(gen: CodeGenerator, module: WatModule, func_names: List[str],
                 filepath: Path, stats: dict):
    """Write a module file with multiple functions."""
    filepath.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        '"""',
        f'Auto-generated from WAT. Contains {len(func_names)} functions.',
        '"""',
        '',
        'import sys',
        'from pathlib import Path',
        'sys.path.insert(0, str(Path(__file__).parent.parent))',
        '',
        'from runtime import (',
        '    memory, i32_load, i64_load, f32_load, f64_load,',
        '    i32_store, i64_store, f32_store, f64_store,',
        '    i32_load8_s, i32_load8_u, i32_load16_s, i32_load16_u,',
        '    i64_load8_s, i64_load8_u, i64_load16_s, i64_load16_u,',
        '    i64_load32_s, i64_load32_u,',
        '    i32_store8, i32_store16, i64_store8, i64_store16, i64_store32,',
        '    i32_atomic_load, i64_atomic_load,',
        '    i32_atomic_store, i64_atomic_store,',
        '    global0, global1, global2, global3, global4,',
        '    global5, global6, global7, global8,',
        '    i32, i64, i64_extend_s, i64_extend_u,',
        '    rotl32, rotr32, rotl64, rotr64,',
        '    clz32, ctz32, popcnt32, clz64, ctz64, popcnt64,',
        '    call_indirect,',
        ')',
        '',
    ]

    for func_name in func_names:
        stats['total_functions'] += 1
        func = module.functions[func_name]
        try:
            code = gen.generate_function(func)
            lines.append(f"# {'='*58}")
            lines.append(f"# {func_name}")
            if func.export_name:
                lines.append(f"# Export: {func.export_name}")
            lines.append(f"# {'='*58}")
            lines.append(code)
            lines.append('')
            lines.append('')
            stats['successful'] += 1
        except Exception as e:
            lines.append(f"# Error generating {func_name}: {e}")
            lines.append(f"def {func_name.lstrip('$').replace('.', '_')}(*args):")
            lines.append(f"    raise NotImplementedError('{func_name}')")
            lines.append('')
            stats['failed'] += 1

    filepath.write_text('\n'.join(lines))
    print(f"  Wrote {filepath.name}: {len(func_names)} functions")


def _generate_exports(module: WatModule, output_dir: Path):
    """Generate exports.py with all exported functions."""
    exports = []
    for name, func in module.functions.items():
        if func.export_name:
            exports.append((func.export_name, name))

    lines = [
        '"""',
        'Exported functions from the WAT module.',
        '"""',
        '',
        '# Export name -> internal function name',
        'EXPORTS = {',
    ]

    for export_name, internal_name in sorted(exports):
        py_name = internal_name.lstrip('$').replace('.', '_')
        lines.append(f'    "{export_name}": "{py_name}",')

    lines.append('}')
    lines.append('')
    lines.append(f'# Total exports: {len(exports)}')

    (output_dir / "exports.py").write_text('\n'.join(lines))
    print(f"\nGenerated exports.py with {len(exports)} exports")


def main():
    parser = argparse.ArgumentParser(
        description="Transpile WAT to Python",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python transpile.py mgame --output tzar/
  python transpile.py mgame --function func26
  python transpile.py mgame --analyze-only
  python transpile.py mgame --batch --lines-per-module 2000
"""
    )
    parser.add_argument('wat_file', help='Path to WAT file')
    parser.add_argument('--output', '-o', help='Output directory for batch mode')
    parser.add_argument('--function', '-f', help='Transpile a single function')
    parser.add_argument('--analyze-only', action='store_true',
                       help='Only analyze, do not generate code')
    parser.add_argument('--batch', action='store_true',
                       help='Batch transpile all functions')
    parser.add_argument('--lines-per-module', type=int, default=2000,
                       help='Target lines per output module (default: 2000)')
    parser.add_argument('--category', help='Only transpile functions of this category')
    parser.add_argument('--depth', type=int, help='Only transpile functions at this depth')
    parser.add_argument('--max-functions', type=int,
                       help='Maximum number of functions to transpile')

    args = parser.parse_args()

    print(f"Parsing {args.wat_file}...")
    module = parse_wat_file(args.wat_file)
    print(f"Parsed {len(module.functions)} functions")

    print("\nAnalyzing...")
    analysis = analyze_module(module)

    if args.analyze_only:
        print_analysis_summary(analysis)
        return

    if args.function:
        code = transpile_single(module, args.function)
        print(code)
        return

    if args.batch or args.output:
        output_dir = Path(args.output or 'tzar')
        batch_transpile(module, analysis, output_dir, args.lines_per_module)
        return

    # Default: show summary and sample
    print_analysis_summary(analysis)
    print("\n" + "="*60)
    print("Sample transpilation (first 3 non-import functions):")
    print("="*60)

    gen = CodeGenerator(module)
    count = 0
    for name, func in module.functions.items():
        if func.is_import:
            continue
        try:
            code = gen.generate_function(func)
            print(f"\n# {name}")
            print(code)
        except Exception as e:
            print(f"\n# {name}: Error - {e}")
        count += 1
        if count >= 3:
            break


if __name__ == '__main__':
    main()
