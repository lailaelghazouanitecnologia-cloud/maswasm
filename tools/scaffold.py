#!/usr/bin/env python3
"""
Create scaffold structure for tzar/ project.

Creates:
- Directory structure by category
- Stub files for all functions
- Runtime module with memory and helpers
- Progress tracking file
"""

import json
import sys
from pathlib import Path
from datetime import datetime

CATEGORIES = [
    'imports',    # System imports ($a.*)
    'memory',     # Memory allocation
    'math',       # Math utilities
    'webp',       # WebP decoder
    'terrain',    # Terrain/map system
    'units',      # Unit logic
    'buildings',  # Building logic
    'resources',  # Resource management
    'pathfinding',# Pathfinding
    'ai',         # AI system
    'combat',     # Combat system
    'render',     # Rendering
    'audio',      # Audio system
    'network',    # Networking
    'ui',         # User interface
    'game',       # Game loop/main
    'unknown',    # Uncategorized
]

def create_runtime(tzar_path: Path):
    """Create the runtime module with memory and helpers."""

    runtime_content = '''"""
Tzar WASM Runtime - Memory and helper functions for transpiled code.
"""

import struct
from typing import Callable, Optional

# Memory: 880 pages * 64KB = ~57MB
MEMORY_PAGES = 880
MEMORY_SIZE = MEMORY_PAGES * 65536
memory = bytearray(MEMORY_SIZE)

# Global variables (from WASM globals)
globals = {
    'global0': 9756528,  # Stack pointer
    'global1': 0,
    'global2': 0,
    'global3': 0,
    'global4': 0,
    'global5': 0,
    'global6': 0,
    'global7': 0,
    'global8': 0,
}

# Function table for indirect calls
func_table: list[Optional[Callable]] = [None] * 452


# ============================================
# Memory Operations
# ============================================

def i32_load(addr: int, offset: int = 0) -> int:
    """Load 32-bit integer from memory."""
    ptr = addr + offset
    return struct.unpack_from('<i', memory, ptr)[0]

def i32_load8_s(addr: int, offset: int = 0) -> int:
    """Load 8-bit signed integer from memory."""
    ptr = addr + offset
    val = memory[ptr]
    return val if val < 128 else val - 256

def i32_load8_u(addr: int, offset: int = 0) -> int:
    """Load 8-bit unsigned integer from memory."""
    return memory[addr + offset]

def i32_load16_s(addr: int, offset: int = 0) -> int:
    """Load 16-bit signed integer from memory."""
    ptr = addr + offset
    return struct.unpack_from('<h', memory, ptr)[0]

def i32_load16_u(addr: int, offset: int = 0) -> int:
    """Load 16-bit unsigned integer from memory."""
    ptr = addr + offset
    return struct.unpack_from('<H', memory, ptr)[0]

def i32_store(addr: int, value: int, offset: int = 0):
    """Store 32-bit integer to memory."""
    ptr = addr + offset
    struct.pack_into('<i', memory, ptr, value & 0xFFFFFFFF)

def i32_store8(addr: int, value: int, offset: int = 0):
    """Store 8-bit integer to memory."""
    memory[addr + offset] = value & 0xFF

def i32_store16(addr: int, value: int, offset: int = 0):
    """Store 16-bit integer to memory."""
    ptr = addr + offset
    struct.pack_into('<H', memory, ptr, value & 0xFFFF)

def f32_load(addr: int, offset: int = 0) -> float:
    """Load 32-bit float from memory."""
    ptr = addr + offset
    return struct.unpack_from('<f', memory, ptr)[0]

def f32_store(addr: int, value: float, offset: int = 0):
    """Store 32-bit float to memory."""
    ptr = addr + offset
    struct.pack_into('<f', memory, ptr, value)

def f64_load(addr: int, offset: int = 0) -> float:
    """Load 64-bit float from memory."""
    ptr = addr + offset
    return struct.unpack_from('<d', memory, ptr)[0]

def f64_store(addr: int, value: float, offset: int = 0):
    """Store 64-bit float to memory."""
    ptr = addr + offset
    struct.pack_into('<d', memory, ptr, value)


# ============================================
# WASM Operations
# ============================================

def i32_clz(value: int) -> int:
    """Count leading zeros in 32-bit integer."""
    if value == 0:
        return 32
    n = 0
    if value & 0xFFFF0000 == 0:
        n += 16
        value <<= 16
    if value & 0xFF000000 == 0:
        n += 8
        value <<= 8
    if value & 0xF0000000 == 0:
        n += 4
        value <<= 4
    if value & 0xC0000000 == 0:
        n += 2
        value <<= 2
    if value & 0x80000000 == 0:
        n += 1
    return n

def i32_ctz(value: int) -> int:
    """Count trailing zeros in 32-bit integer."""
    if value == 0:
        return 32
    n = 0
    if value & 0x0000FFFF == 0:
        n += 16
        value >>= 16
    if value & 0x000000FF == 0:
        n += 8
        value >>= 8
    if value & 0x0000000F == 0:
        n += 4
        value >>= 4
    if value & 0x00000003 == 0:
        n += 2
        value >>= 2
    if value & 0x00000001 == 0:
        n += 1
    return n

def i32_popcnt(value: int) -> int:
    """Count number of 1 bits in 32-bit integer."""
    count = 0
    while value:
        count += value & 1
        value >>= 1
    return count

def i32_rotl(value: int, shift: int) -> int:
    """Rotate left 32-bit integer."""
    shift &= 31
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def i32_rotr(value: int, shift: int) -> int:
    """Rotate right 32-bit integer."""
    shift &= 31
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF

def i32_wrap(value: int) -> int:
    """Wrap value to 32-bit signed integer."""
    value &= 0xFFFFFFFF
    if value >= 0x80000000:
        return value - 0x100000000
    return value

def i32_trunc_f32_s(value: float) -> int:
    """Truncate f32 to signed i32."""
    return int(value) & 0xFFFFFFFF

def i32_trunc_f32_u(value: float) -> int:
    """Truncate f32 to unsigned i32."""
    return int(value) & 0xFFFFFFFF


# ============================================
# Import Stubs (to be implemented)
# ============================================

def import_a_b(p0: int, p1: int, p2: int):
    """Import $a.b - TODO: identify purpose."""
    pass

def import_a_c(p0: int, p1: int, p2: int, p3: int):
    """Import $a.c - TODO: identify purpose."""
    pass

def import_a_d(p0: int, p1: int, p2: int) -> int:
    """Import $a.d - TODO: identify purpose."""
    return 0

def import_a_e(p0: int, p1: int, p2: int) -> int:
    """Import $a.e - TODO: identify purpose."""
    return 0

def import_a_f() -> float:
    """Import $a.f - likely time or random."""
    import time
    return time.time()

def import_a_g():
    """Import $a.g - unreachable/trap."""
    raise RuntimeError("Unreachable code executed")


# ============================================
# Helpers
# ============================================

def select(cond: int, val_true: int, val_false: int) -> int:
    """WASM select instruction."""
    return val_true if cond else val_false

def call_indirect(table_idx: int, *args):
    """Call function from table."""
    func = func_table[table_idx]
    if func is None:
        raise RuntimeError(f"Null function at table index {table_idx}")
    return func(*args)
'''

    (tzar_path / '_runtime.py').write_text(runtime_content)


def create_stub(func_info: dict, category: str, tzar_path: Path):
    """Create a stub file for a function."""
    func_name = func_info['id'].replace('$', '')
    safe_name = func_name.replace('.', '_')

    # Determine directory
    cat_dir = tzar_path / category
    cat_dir.mkdir(parents=True, exist_ok=True)

    stub_content = f'''"""
Function: {func_info['id']}
Category: {category}
Depth: {func_info['depth']}
Status: stub

Calls: {', '.join(func_info['calls']) or 'none'}
Called by: {len(func_info['called_by'])} functions

TODO: Transpile from WAT
"""

from tzar._runtime import *


def {safe_name}():
    """
    TODO: Implement this function.

    Run: python tools/context.py {func_info['id']}
    To see the full WAT code and context.
    """
    raise NotImplementedError("{func_info['id']} not yet transpiled")
'''

    filepath = cat_dir / f'{safe_name}.py'
    if not filepath.exists():
        filepath.write_text(stub_content)

    return filepath


def categorize_function(func_info: dict) -> str:
    """Categorize a function."""
    name = func_info['id'].lower()

    if '.' in func_info['id']:
        return 'imports'
    if 'func26' in name or func_info['id'] == '$af':
        return 'memory'
    if any(x in name for x in ['vp8', 'webp', 'huffman']):
        return 'webp'

    # Use calls to determine category
    calls_str = ' '.join(func_info['calls']).lower()
    if 'vp8' in calls_str or 'webp' in calls_str:
        return 'webp'

    return 'unknown'


def create_progress_file(tree: dict, tzar_path: Path):
    """Create progress tracking file."""
    progress = {
        'created': datetime.now().isoformat(),
        'updated': datetime.now().isoformat(),
        'total': len(tree['functions']),
        'by_status': {
            'pending': len(tree['functions']),
            'stub': 0,
            'wip': 0,
            'done': 0,
            'verified': 0,
        },
        'by_category': {},
        'functions': {}
    }

    for func_id, func_info in tree['functions'].items():
        category = categorize_function(func_info)
        progress['functions'][func_id] = {
            'status': 'pending',
            'category': category,
            'file': None,
            'notes': '',
        }

        if category not in progress['by_category']:
            progress['by_category'][category] = {'total': 0, 'done': 0}
        progress['by_category'][category]['total'] += 1

    (tzar_path / '_progress.json').write_text(json.dumps(progress, indent=2))


def scaffold(tree_path: Path, tzar_path: Path):
    """Create the full scaffold."""
    tree = json.loads(tree_path.read_text())

    # Create directories
    tzar_path.mkdir(exist_ok=True)
    for cat in CATEGORIES:
        (tzar_path / cat).mkdir(exist_ok=True)

    # Create runtime
    print("Creating runtime...")
    create_runtime(tzar_path)

    # Create __init__.py files
    (tzar_path / '__init__.py').write_text('"""Tzar WASM transpiled to Python."""\n')
    for cat in CATEGORIES:
        (tzar_path / cat / '__init__.py').write_text(f'"""{cat.title()} module."""\n')

    # Create stubs for all functions
    print("Creating function stubs...")
    created = 0
    for func_id, func_info in tree['functions'].items():
        if func_info.get('is_import'):
            continue
        category = categorize_function(func_info)
        create_stub(func_info, category, tzar_path)
        created += 1

    # Create progress file
    print("Creating progress file...")
    create_progress_file(tree, tzar_path)

    # Summary
    print(f"\n{'='*60}")
    print(f"  SCAFFOLD CREATED")
    print(f"{'='*60}")
    print(f"\n✅ Created tzar/ with:")
    print(f"   - Runtime module (_runtime.py)")
    print(f"   - {len(CATEGORIES)} category directories")
    print(f"   - {created} function stubs")
    print(f"   - Progress tracking (_progress.json)")
    print(f"\n📁 Structure:")
    for cat in CATEGORIES:
        count = len(list((tzar_path / cat).glob('*.py'))) - 1  # exclude __init__
        if count > 0:
            print(f"   tzar/{cat}/ ({count} files)")
    print(f"\n🚀 Next steps:")
    print(f"   1. python tools/context.py --next")
    print(f"   2. Pick a function and view its context")
    print(f"   3. Transpile manually to the stub file")
    print(f"   4. python tools/progress.py mark <func> done")
    print(f"\n{'='*60}\n")


def main():
    tree_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('tzar/_tree.json')
    tzar_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('tzar')

    if not tree_path.exists():
        print(f"Error: {tree_path} not found")
        print("Run: python tools/generate_tree.py first")
        sys.exit(1)

    scaffold(tree_path, tzar_path)


if __name__ == '__main__':
    main()
