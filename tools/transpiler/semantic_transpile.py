#!/usr/bin/env python3
"""
Semantic batch transpiler - generates clean Python modules with structure awareness.
"""

import sys
from pathlib import Path
from typing import Dict, List
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))

from wat_parser import parse_wat_file, WatModule
from analyzer import analyze_module
from semantic_codegen import SemanticCodeGen


def categorize(name: str, func, analysis) -> str:
    """Categorize function based on metadata."""
    export = func.export_name or ''

    # Memory management
    if name in ('$func26', '$af', '$func28', '$func29', '$Ua', '$func30'):
        return 'memory'

    # Math functions (small, pure, numeric operations)
    if name.startswith('$func7') or name.startswith('$func8'):
        if name in analysis.functions:
            a = analysis.functions[name]
            if a.is_pure and a.instruction_count < 100:
                return 'math'

    # Check analysis
    if name in analysis.functions:
        a = analysis.functions[name]

        # Accessors: small, leaf, simple
        if a.is_leaf and a.instruction_count < 20:
            return 'accessors'

        # Check for structure usage
        if any('PLAYER' in str(x) for x in a.known_addresses):
            return 'player'
        if any('ENTITY' in str(x) for x in a.known_addresses):
            return 'entity'
        if any('HEAP' in str(x) or 'ALLOC' in str(x) for x in a.known_addresses):
            return 'memory'

    # By export pattern
    if export:
        if export[0].isupper():
            return 'api'

    return 'core'


def generate_header(category: str) -> str:
    """Generate module header."""
    return f'''"""
Tzar Engine - {category.title()} module.
Auto-generated from WebAssembly.
"""
from tzar.runtime import (
    load32, load64, load8u, load8s, load16u, load16s,
    loadf32, loadf64,
    store32, store64, store8, store16, storef32, storef64,
    atomic_load, atomic_store,
    i32, i64, u32, u64, f32,
    rotl, rotr, clz, ctz, popcnt,
    sqrt, abs, ceil, floor, trunc,
    G, mem_size, mem_grow, call_table,
)

# Known addresses
GAME_STATE = 9142424
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892
PLAYERS = 9561692
ENTITY_TYPES = 9568096
ENTITIES = 9671128
HEAP_FREELIST = 9690464
HEAP_TREE = 9690468
FREE_SIZE = 9690472
HEAP_TOTAL = 9690476
HEAP_BASE = 9690480
HEAP_TOP = 9690484
HEAP_END = 9690488
ALLOC_COUNT = 9690496
MEM_FLAGS = 9690908
MEM_MUTEX = 9690912
ALLOC_HANDLER = 9690984

class Unreachable(Exception):
    pass

'''


def batch_transpile(wat_file: str, output_dir: str, max_lines: int = 2000):
    """Transpile all functions into organized modules."""

    print(f"Parsing {wat_file}...")
    module = parse_wat_file(wat_file)
    print(f"  {len(module.functions)} functions")

    print("Analyzing...")
    analysis = analyze_module(module)
    print(f"  {len(analysis.functions)} analyzed")

    # Group by category
    categories: Dict[str, List[str]] = defaultdict(list)
    for name, func in module.functions.items():
        if func.is_import:
            continue
        cat = categorize(name, func, analysis)
        categories[cat].append(name)

    print("\nCategories:")
    for cat, funcs in sorted(categories.items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(funcs)}")

    # Create output
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    gen = SemanticCodeGen(module)
    stats = {'total': 0, 'ok': 0, 'err': 0, 'files': 0}

    for cat, func_names in categories.items():
        print(f"\n{cat}/")
        cat_path = out / cat
        cat_path.mkdir(exist_ok=True)
        (cat_path / '__init__.py').write_text(f'"""Tzar {cat}."""\n')

        lines = []
        file_idx = 0

        for name in func_names:
            func = module.functions[name]
            stats['total'] += 1

            try:
                code = gen.generate(func)
                lines.append(f"\n# {'-'*58}")
                lines.append(f"# {name}")
                if func.export_name:
                    lines.append(f"# Export: {func.export_name}")
                lines.append(f"# {'-'*58}")
                lines.append(code)
                stats['ok'] += 1

                if len(lines) > max_lines:
                    _write(cat_path, file_idx, lines, cat, stats)
                    lines = []
                    file_idx += 1

            except Exception as e:
                stats['err'] += 1
                lines.append(f"\n# Error: {name}: {e}")

        if lines:
            _write(cat_path, file_idx, lines, cat, stats)

    # Main init
    init_lines = ['"""Tzar Engine."""', '']
    for cat in sorted(categories.keys()):
        init_lines.append(f'from . import {cat}')
    (out / '__init__.py').write_text('\n'.join(init_lines) + '\n')

    print(f"\n{'='*60}")
    print(f"Done: {stats['ok']}/{stats['total']} ok, {stats['err']} errors, {stats['files']} files")


def _write(cat_path: Path, idx: int, lines: List[str], cat: str, stats: dict):
    name = f"mod_{idx}.py" if idx else "mod.py"
    path = cat_path / name
    content = generate_header(cat) + '\n'.join(lines)
    path.write_text(content)
    stats['files'] += 1
    print(f"  {name}")


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('wat_file')
    p.add_argument('--output', '-o', default='tzar')
    p.add_argument('--max-lines', type=int, default=2000)
    args = p.parse_args()
    batch_transpile(args.wat_file, args.output, args.max_lines)
