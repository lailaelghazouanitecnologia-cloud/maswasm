"""
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
