"""
Runtime support for transpiled WAT code.

Provides memory operations, globals, and helper functions
needed by the generated Python code.
"""

import struct
from typing import Optional

# Memory - shared bytearray
# Default 880 pages = 880 * 64KB = 56MB
MEMORY_PAGES = 880
memory = bytearray(MEMORY_PAGES * 65536)

# Globals
global0 = 9756528  # Stack pointer
global1 = 0
global2 = 0
global3 = 0
global4 = 0
global5 = 0
global6 = 0
global7 = 0
global8 = 0


# Memory load operations
def i32_load(addr: int) -> int:
    """Load a 32-bit signed integer from memory."""
    val = struct.unpack_from('<i', memory, addr)[0]
    return val


def i32_load_u(addr: int) -> int:
    """Load a 32-bit unsigned integer from memory."""
    val = struct.unpack_from('<I', memory, addr)[0]
    return val


def i64_load(addr: int) -> int:
    """Load a 64-bit signed integer from memory."""
    return struct.unpack_from('<q', memory, addr)[0]


def f32_load(addr: int) -> float:
    """Load a 32-bit float from memory."""
    return struct.unpack_from('<f', memory, addr)[0]


def f64_load(addr: int) -> float:
    """Load a 64-bit float from memory."""
    return struct.unpack_from('<d', memory, addr)[0]


def i32_load8_s(addr: int) -> int:
    """Load a signed 8-bit integer and extend to 32-bit."""
    return struct.unpack_from('<b', memory, addr)[0]


def i32_load8_u(addr: int) -> int:
    """Load an unsigned 8-bit integer and extend to 32-bit."""
    return memory[addr]


def i32_load16_s(addr: int) -> int:
    """Load a signed 16-bit integer and extend to 32-bit."""
    return struct.unpack_from('<h', memory, addr)[0]


def i32_load16_u(addr: int) -> int:
    """Load an unsigned 16-bit integer and extend to 32-bit."""
    return struct.unpack_from('<H', memory, addr)[0]


def i64_load8_s(addr: int) -> int:
    """Load a signed 8-bit integer and extend to 64-bit."""
    return struct.unpack_from('<b', memory, addr)[0]


def i64_load8_u(addr: int) -> int:
    """Load an unsigned 8-bit integer and extend to 64-bit."""
    return memory[addr]


def i64_load16_s(addr: int) -> int:
    """Load a signed 16-bit integer and extend to 64-bit."""
    return struct.unpack_from('<h', memory, addr)[0]


def i64_load16_u(addr: int) -> int:
    """Load an unsigned 16-bit integer and extend to 64-bit."""
    return struct.unpack_from('<H', memory, addr)[0]


def i64_load32_s(addr: int) -> int:
    """Load a signed 32-bit integer and extend to 64-bit."""
    return struct.unpack_from('<i', memory, addr)[0]


def i64_load32_u(addr: int) -> int:
    """Load an unsigned 32-bit integer and extend to 64-bit."""
    return struct.unpack_from('<I', memory, addr)[0]


# Atomic loads (simplified - no actual atomicity in Python)
def i32_atomic_load(addr: int) -> int:
    """Atomic load of 32-bit integer."""
    return i32_load(addr)


def i64_atomic_load(addr: int) -> int:
    """Atomic load of 64-bit integer."""
    return i64_load(addr)


# Memory store operations
def i32_store(addr: int, val: int):
    """Store a 32-bit integer to memory."""
    struct.pack_into('<i', memory, addr, val & 0xFFFFFFFF)


def i64_store(addr: int, val: int):
    """Store a 64-bit integer to memory."""
    struct.pack_into('<q', memory, addr, val)


def f32_store(addr: int, val: float):
    """Store a 32-bit float to memory."""
    struct.pack_into('<f', memory, addr, val)


def f64_store(addr: int, val: float):
    """Store a 64-bit float to memory."""
    struct.pack_into('<d', memory, addr, val)


def i32_store8(addr: int, val: int):
    """Store the low 8 bits of a 32-bit integer."""
    memory[addr] = val & 0xFF


def i32_store16(addr: int, val: int):
    """Store the low 16 bits of a 32-bit integer."""
    struct.pack_into('<H', memory, addr, val & 0xFFFF)


def i64_store8(addr: int, val: int):
    """Store the low 8 bits of a 64-bit integer."""
    memory[addr] = val & 0xFF


def i64_store16(addr: int, val: int):
    """Store the low 16 bits of a 64-bit integer."""
    struct.pack_into('<H', memory, addr, val & 0xFFFF)


def i64_store32(addr: int, val: int):
    """Store the low 32 bits of a 64-bit integer."""
    struct.pack_into('<I', memory, addr, val & 0xFFFFFFFF)


# Atomic stores (simplified)
def i32_atomic_store(addr: int, val: int):
    """Atomic store of 32-bit integer."""
    i32_store(addr, val)


def i64_atomic_store(addr: int, val: int):
    """Atomic store of 64-bit integer."""
    i64_store(addr, val)


# Type conversions
def i32(val: int) -> int:
    """Wrap value to 32-bit signed integer."""
    val = val & 0xFFFFFFFF
    if val >= 0x80000000:
        val -= 0x100000000
    return val


def i64(val: int) -> int:
    """Wrap value to 64-bit signed integer."""
    val = val & 0xFFFFFFFFFFFFFFFF
    if val >= 0x8000000000000000:
        val -= 0x10000000000000000
    return val


def i64_extend_s(val: int) -> int:
    """Sign-extend 32-bit to 64-bit."""
    if val & 0x80000000:
        return val | 0xFFFFFFFF00000000
    return val


def i64_extend_u(val: int) -> int:
    """Zero-extend 32-bit to 64-bit."""
    return val & 0xFFFFFFFF


# Bit manipulation
def rotl32(val: int, shift: int) -> int:
    """32-bit rotate left."""
    val = val & 0xFFFFFFFF
    shift = shift & 31
    return ((val << shift) | (val >> (32 - shift))) & 0xFFFFFFFF


def rotr32(val: int, shift: int) -> int:
    """32-bit rotate right."""
    val = val & 0xFFFFFFFF
    shift = shift & 31
    return ((val >> shift) | (val << (32 - shift))) & 0xFFFFFFFF


def rotl64(val: int, shift: int) -> int:
    """64-bit rotate left."""
    val = val & 0xFFFFFFFFFFFFFFFF
    shift = shift & 63
    return ((val << shift) | (val >> (64 - shift))) & 0xFFFFFFFFFFFFFFFF


def rotr64(val: int, shift: int) -> int:
    """64-bit rotate right."""
    val = val & 0xFFFFFFFFFFFFFFFF
    shift = shift & 63
    return ((val >> shift) | (val << (64 - shift))) & 0xFFFFFFFFFFFFFFFF


def clz32(val: int) -> int:
    """Count leading zeros in 32-bit value."""
    if val == 0:
        return 32
    val = val & 0xFFFFFFFF
    count = 0
    while (val & 0x80000000) == 0:
        count += 1
        val <<= 1
    return count


def ctz32(val: int) -> int:
    """Count trailing zeros in 32-bit value."""
    if val == 0:
        return 32
    val = val & 0xFFFFFFFF
    count = 0
    while (val & 1) == 0:
        count += 1
        val >>= 1
    return count


def popcnt32(val: int) -> int:
    """Population count (number of 1 bits) in 32-bit value."""
    return bin(val & 0xFFFFFFFF).count('1')


def clz64(val: int) -> int:
    """Count leading zeros in 64-bit value."""
    if val == 0:
        return 64
    val = val & 0xFFFFFFFFFFFFFFFF
    count = 0
    while (val & 0x8000000000000000) == 0:
        count += 1
        val <<= 1
    return count


def ctz64(val: int) -> int:
    """Count trailing zeros in 64-bit value."""
    if val == 0:
        return 64
    val = val & 0xFFFFFFFFFFFFFFFF
    count = 0
    while (val & 1) == 0:
        count += 1
        val >>= 1
    return count


def popcnt64(val: int) -> int:
    """Population count in 64-bit value."""
    return bin(val & 0xFFFFFFFFFFFFFFFF).count('1')


# Reinterpret casts
def i32_reinterpret_f32(val: float) -> int:
    """Reinterpret f32 bits as i32."""
    return struct.unpack('<i', struct.pack('<f', val))[0]


def i64_reinterpret_f64(val: float) -> int:
    """Reinterpret f64 bits as i64."""
    return struct.unpack('<q', struct.pack('<d', val))[0]


def f32_reinterpret_i32(val: int) -> float:
    """Reinterpret i32 bits as f32."""
    return struct.unpack('<f', struct.pack('<i', val & 0xFFFFFFFF))[0]


def f64_reinterpret_i64(val: int) -> float:
    """Reinterpret i64 bits as f64."""
    return struct.unpack('<d', struct.pack('<q', val))[0]


# Memory operations
def memory_size() -> int:
    """Return current memory size in pages."""
    return len(memory) // 65536


def memory_grow(pages: int) -> int:
    """Grow memory by specified pages. Returns old size or -1 on failure."""
    global memory
    old_size = len(memory) // 65536
    try:
        new_size = len(memory) + pages * 65536
        if new_size > 65536 * 65536:  # Max 4GB
            return -1
        memory.extend(bytearray(pages * 65536))
        return old_size
    except:
        return -1


# Memory copy operations
def memory_copy(dest: int, src: int, length: int):
    """Copy memory region."""
    memory[dest:dest+length] = memory[src:src+length]


def memory_fill(dest: int, val: int, length: int):
    """Fill memory region with value."""
    memory[dest:dest+length] = bytes([val & 0xFF]) * length


# Function table support
_function_table = {}


def register_function(idx: int, func):
    """Register a function in the table."""
    _function_table[idx] = func


def call_indirect(idx: int, *args):
    """Call a function by table index."""
    if idx in _function_table:
        return _function_table[idx](*args)
    raise RuntimeError(f"Function not in table: {idx}")


def ref_func(name: str) -> int:
    """Get reference to a function (placeholder)."""
    return hash(name) & 0xFFFFFFFF


# Load initial memory from file if available
def load_memory_from_file(filepath: str):
    """Load memory contents from a binary file."""
    global memory
    with open(filepath, 'rb') as f:
        data = f.read()
    memory[:len(data)] = data


def save_memory_to_file(filepath: str):
    """Save memory contents to a binary file."""
    with open(filepath, 'wb') as f:
        f.write(memory)
