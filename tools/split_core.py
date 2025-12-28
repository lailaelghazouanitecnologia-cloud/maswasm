#!/usr/bin/env python3
"""
Split large core module files into ~5000 line chunks.
Respects function boundaries.
"""

import re
import os
from pathlib import Path

CHUNK_SIZE = 5000  # Target lines per file

HEADER = '''"""
Tzar Engine - Core module (part {part}).
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

from tzar.core.templates import (
    ENTITIES, PLAYERS, ENTITY_TYPES,
    EntityField, PlayerField, EntityTypeField,
    get_entity_ptr, get_player_ptr, get_entity_type_ptr,
    entity_hp, entity_state, entity_action, entity_owner,
    entity_x, entity_y, entity_type_id,
    iter_entities, iter_entity_ptrs,
)

# Known addresses
GAME_STATE = 9142424
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892
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


def find_function_starts(content: str) -> list:
    """Find line numbers where functions start."""
    starts = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('def ') or line.startswith('# ------'):
            starts.append(i)
    return starts


def split_file(filepath: str, output_dir: str):
    """Split a file into chunks."""
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    total_lines = len(lines)

    # Find all function boundaries
    func_starts = []
    in_header = True
    header_end = 0

    for i, line in enumerate(lines):
        if in_header:
            if line.startswith('# ------') or line.startswith('def '):
                in_header = False
                header_end = i
        if line.startswith('# ------'):
            func_starts.append(i)

    if not func_starts:
        print(f"No functions found in {filepath}")
        return

    print(f"Found {len(func_starts)} functions in {filepath}")
    print(f"Header ends at line {header_end}")
    print(f"Total lines: {total_lines}")

    # Split into chunks
    chunks = []
    current_chunk_start = func_starts[0]
    current_chunk_lines = 0

    for i, start in enumerate(func_starts):
        # Find end of this function
        if i + 1 < len(func_starts):
            end = func_starts[i + 1]
        else:
            end = total_lines

        func_lines = end - start
        current_chunk_lines += func_lines

        # Check if we should start a new chunk
        if current_chunk_lines >= CHUNK_SIZE and i + 1 < len(func_starts):
            chunks.append((current_chunk_start, start + func_lines))
            current_chunk_start = func_starts[i + 1] if i + 1 < len(func_starts) else end
            current_chunk_lines = 0

    # Add final chunk
    if current_chunk_start < total_lines:
        chunks.append((current_chunk_start, total_lines))

    print(f"Splitting into {len(chunks)} chunks")

    # Write chunks
    base_name = Path(filepath).stem
    os.makedirs(output_dir, exist_ok=True)

    for i, (start, end) in enumerate(chunks):
        chunk_lines = lines[start:end]
        chunk_content = HEADER.format(part=i+1) + '\n'.join(chunk_lines)

        output_path = os.path.join(output_dir, f"{base_name}_part{i+1:02d}.py")
        with open(output_path, 'w') as f:
            f.write(chunk_content)

        print(f"  Part {i+1}: lines {start}-{end} ({end-start} lines) -> {output_path}")

    return chunks


def main():
    core_dir = Path(__file__).parent.parent / "tzar" / "core"
    output_dir = core_dir / "parts"

    # Split mod.py
    mod_path = core_dir / "mod.py"
    if mod_path.exists():
        print(f"\nSplitting {mod_path}...")
        split_file(str(mod_path), str(output_dir))

    # Split mod_1.py
    mod1_path = core_dir / "mod_1.py"
    if mod1_path.exists():
        print(f"\nSplitting {mod1_path}...")
        split_file(str(mod1_path), str(output_dir))


if __name__ == "__main__":
    main()
