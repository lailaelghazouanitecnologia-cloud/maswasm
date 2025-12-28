#!/usr/bin/env python3
"""
Smart batch transpiler - generates clean, organized Python modules.
"""

import sys
import os
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent))

from wat_parser import parse_wat_file, WatModule, WatFunction
from analyzer import analyze_module, DependencyGraph, FunctionCategory
from smart_codegen import SmartCodeGen


# Function categorization based on metadata and patterns
def categorize_function(name: str, func: WatFunction, analysis) -> str:
    """Determine the best category for a function."""

    # Check export name for clues
    export = func.export_name or ''

    # Memory management
    if name in ('$func26', '$af', '$func28', '$func29', '$Ua'):
        return 'memory'
    if 'malloc' in export.lower() or 'free' in export.lower() or 'alloc' in export.lower():
        return 'memory'

    # Math functions
    if any(x in name for x in ('$func75', '$func76', '$func77', '$func78', '$func79',
                                '$func80', '$func81', '$func82', '$func83', '$func84',
                                '$func85', '$func86', '$func87', '$func88')):
        return 'math'

    # Check the analysis if available
    if name in analysis.functions:
        func_analysis = analysis.functions[name]

        # Small, pure functions are likely accessors or math
        if func_analysis.instruction_count < 30 and func_analysis.is_pure:
            if func_analysis.is_leaf:
                return 'accessors'
            return 'math'

        # Check for known addresses
        if 'PLAYER' in str(func_analysis.known_addresses):
            return 'player'
        if 'ENTITY' in str(func_analysis.known_addresses):
            return 'entity'
        if 'HEAP' in str(func_analysis.known_addresses) or 'ALLOC' in str(func_analysis.known_addresses):
            return 'memory'

    # Default based on export name patterns
    if export:
        first_char = export[0] if export else ''
        # Group by first letter for now
        if first_char.isupper():
            return 'exports'

    return 'core'


def generate_module_header(category: str) -> str:
    """Generate module header with appropriate imports."""
    return f'''"""
Tzar Game Engine - {category.title()} functions.
Auto-generated from WAT.
"""
from tzar.runtime import (
    G, M, load32, load64, load8u, load8s, load16u, load16s, load32u,
    loadf32, loadf64, store32, store64, store8, store16, storef32, storef64,
    atomic_load, atomic_store, i32, i64, u, u64,
    rotl, rotr, clz, ctz, popcnt, f32, sqrt, ceil, floor, trunc,
    mem_size, mem_grow, mem_copy, mem_fill, indirect_call,
)

'''


def batch_transpile(wat_file: str, output_dir: str, max_lines: int = 1500):
    """Transpile all functions into organized modules."""

    print(f"Parsing {wat_file}...")
    module = parse_wat_file(wat_file)
    print(f"  {len(module.functions)} functions")

    print("Analyzing...")
    analysis = analyze_module(module)
    print(f"  {len(analysis.functions)} analyzed")

    # Group functions by category
    categories: Dict[str, List[str]] = defaultdict(list)

    for name, func in module.functions.items():
        if func.is_import:
            continue
        cat = categorize_function(name, func, analysis)
        categories[cat].append(name)

    print("\nCategories:")
    for cat, funcs in sorted(categories.items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(funcs)} functions")

    # Create output directory
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Generate each category
    gen = SmartCodeGen(module)
    stats = {'total': 0, 'success': 0, 'failed': 0, 'files': 0}

    for cat, func_names in categories.items():
        print(f"\nGenerating {cat}/...")

        cat_path = out_path / cat
        cat_path.mkdir(exist_ok=True)

        # Write __init__.py
        (cat_path / '__init__.py').write_text(f'"""Tzar {cat.title()} module."""\n')

        # Group into files by estimated size
        current_lines = []
        current_file_idx = 0
        current_count = 0

        for func_name in func_names:
            func = module.functions[func_name]
            stats['total'] += 1

            try:
                code = gen.generate(func)
                code_lines = code.count('\n') + 1

                # Check if we need a new file
                if current_count > 0 and len(current_lines) + code_lines > max_lines:
                    _write_file(cat_path, current_file_idx, current_lines, cat, stats)
                    current_lines = []
                    current_file_idx += 1
                    current_count = 0

                current_lines.append(f"\n# {'-'*60}")
                current_lines.append(f"# {func_name}")
                if func.export_name:
                    current_lines.append(f"# Export: {func.export_name}")
                current_lines.append(f"# {'-'*60}")
                current_lines.append(code)
                current_count += 1
                stats['success'] += 1

            except Exception as e:
                stats['failed'] += 1
                current_lines.append(f"\n# Error: {func_name}: {e}")

        # Write remaining
        if current_lines:
            _write_file(cat_path, current_file_idx, current_lines, cat, stats)

    # Generate main __init__.py
    _generate_init(out_path, categories)

    print(f"\n{'='*60}")
    print(f"Transpilation complete!")
    print(f"  Total: {stats['total']}")
    print(f"  Success: {stats['success']}")
    print(f"  Failed: {stats['failed']}")
    print(f"  Files: {stats['files']}")


def _write_file(cat_path: Path, idx: int, lines: List[str], category: str, stats: dict):
    """Write a module file."""
    filename = f"funcs_{idx}.py" if idx > 0 else "funcs.py"
    filepath = cat_path / filename

    content = generate_module_header(category) + '\n'.join(lines)
    filepath.write_text(content)

    stats['files'] += 1
    print(f"  {filepath.name}: ~{len(lines)} lines")


def _generate_init(out_path: Path, categories: Dict[str, List[str]]):
    """Generate main __init__.py."""
    lines = ['"""Tzar Game Engine - Transpiled from WAT."""', '']

    for cat in sorted(categories.keys()):
        lines.append(f'from . import {cat}')

    (out_path / '__init__.py').write_text('\n'.join(lines) + '\n')


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Smart WAT to Python transpiler")
    parser.add_argument('wat_file', help='Path to WAT file')
    parser.add_argument('--output', '-o', default='tzar', help='Output directory')
    parser.add_argument('--max-lines', type=int, default=1500, help='Max lines per file')

    args = parser.parse_args()
    batch_transpile(args.wat_file, args.output, args.max_lines)


if __name__ == '__main__':
    main()
