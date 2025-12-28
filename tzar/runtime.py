"""
Tzar Game Engine Runtime - Memory and utility operations.
"""
import struct
from typing import Tuple

# Memory - 56MB shared buffer
MEMORY_SIZE = 880 * 65536  # 880 pages * 64KB
_mem = bytearray(MEMORY_SIZE)


# =============================================================================
# Global state
# =============================================================================
class G:
    """Global variables."""
    global0 = 9756528  # Stack pointer
    global1 = 0
    global2 = 0
    global3 = 0
    global4 = 0
    global5 = 0
    global6 = 0
    global7 = 0
    global8 = 0


# =============================================================================
# Known memory addresses (semantic names)
# =============================================================================
class M:
    """Memory-mapped values with semantic names."""

    @property
    def game_state(self) -> int:
        return load32(9142424)

    @property
    def current_player(self) -> int:
        return load32(9142872)

    @property
    def player_count(self) -> int:
        return load32(9142892)

    @property
    def heap_base(self) -> int:
        return load32(9690480)

    @property
    def heap_top(self) -> int:
        return load32(9690484)

    @property
    def alloc_handler(self) -> int:
        return load32(9690984)


M = M()


# =============================================================================
# Memory operations - compact and efficient
# =============================================================================
def load32(addr: int) -> int:
    """Load 32-bit signed integer."""
    return struct.unpack_from('<i', _mem, addr)[0]


def load64(addr: int) -> int:
    """Load 64-bit signed integer."""
    return struct.unpack_from('<q', _mem, addr)[0]


def load8u(addr: int) -> int:
    """Load unsigned byte."""
    return _mem[addr]


def load8s(addr: int) -> int:
    """Load signed byte."""
    return struct.unpack_from('<b', _mem, addr)[0]


def load16u(addr: int) -> int:
    """Load unsigned 16-bit."""
    return struct.unpack_from('<H', _mem, addr)[0]


def load16s(addr: int) -> int:
    """Load signed 16-bit."""
    return struct.unpack_from('<h', _mem, addr)[0]


def load32u(addr: int) -> int:
    """Load unsigned 32-bit."""
    return struct.unpack_from('<I', _mem, addr)[0]


def loadf32(addr: int) -> float:
    """Load 32-bit float."""
    return struct.unpack_from('<f', _mem, addr)[0]


def loadf64(addr: int) -> float:
    """Load 64-bit float."""
    return struct.unpack_from('<d', _mem, addr)[0]


def store32(addr: int, val: int):
    """Store 32-bit integer."""
    struct.pack_into('<i', _mem, addr, val & 0xFFFFFFFF)


def store64(addr: int, val: int):
    """Store 64-bit integer."""
    struct.pack_into('<q', _mem, addr, val)


def store8(addr: int, val: int):
    """Store byte."""
    _mem[addr] = val & 0xFF


def store16(addr: int, val: int):
    """Store 16-bit."""
    struct.pack_into('<H', _mem, addr, val & 0xFFFF)


def storef32(addr: int, val: float):
    """Store 32-bit float."""
    struct.pack_into('<f', _mem, addr, val)


def storef64(addr: int, val: float):
    """Store 64-bit float."""
    struct.pack_into('<d', _mem, addr, val)


# Atomic operations (single-threaded Python - just aliases)
atomic_load = load32
atomic_load64 = load64
atomic_store = store32
atomic_store64 = store64


# =============================================================================
# Type operations
# =============================================================================
def i32(val: int) -> int:
    """Wrap to 32-bit signed."""
    val = val & 0xFFFFFFFF
    return val - 0x100000000 if val >= 0x80000000 else val


def i64(val: int) -> int:
    """Wrap to 64-bit signed."""
    val = val & 0xFFFFFFFFFFFFFFFF
    return val - 0x10000000000000000 if val >= 0x8000000000000000 else val


def u(val: int) -> int:
    """Interpret as unsigned for comparisons."""
    if val < 0:
        return val + 0x100000000
    return val

# Alias for clarity
u32 = u


def u64(val: int) -> int:
    """Interpret as unsigned 64-bit."""
    if val < 0:
        return val + 0x10000000000000000
    return val


# =============================================================================
# Bit operations
# =============================================================================
def rotl(val: int, shift: int, bits: int = 32) -> int:
    """Rotate left."""
    mask = (1 << bits) - 1
    val &= mask
    shift &= (bits - 1)
    return ((val << shift) | (val >> (bits - shift))) & mask


def rotr(val: int, shift: int, bits: int = 32) -> int:
    """Rotate right."""
    mask = (1 << bits) - 1
    val &= mask
    shift &= (bits - 1)
    return ((val >> shift) | (val << (bits - shift))) & mask


def clz(val: int, bits: int = 32) -> int:
    """Count leading zeros."""
    if val == 0:
        return bits
    count = 0
    mask = 1 << (bits - 1)
    while (val & mask) == 0:
        count += 1
        mask >>= 1
    return count


def ctz(val: int, bits: int = 32) -> int:
    """Count trailing zeros."""
    if val == 0:
        return bits
    count = 0
    while (val & 1) == 0:
        count += 1
        val >>= 1
    return count


def popcnt(val: int) -> int:
    """Population count."""
    return bin(val).count('1')


# =============================================================================
# Math operations
# =============================================================================
from math import sqrt, ceil, floor, trunc, copysign


def f32(val: float) -> float:
    """Truncate to f32 precision."""
    return struct.unpack('<f', struct.pack('<f', val))[0]


# =============================================================================
# Memory management
# =============================================================================
def mem_size() -> int:
    """Memory size in pages."""
    return len(_mem) // 65536


def mem_grow(pages: int) -> int:
    """Grow memory."""
    global _mem
    old = len(_mem) // 65536
    try:
        _mem.extend(bytearray(pages * 65536))
        return old
    except:
        return -1


def mem_copy(dst: int, src: int, n: int):
    """Copy memory region."""
    _mem[dst:dst+n] = _mem[src:src+n]


def mem_fill(dst: int, val: int, n: int):
    """Fill memory region."""
    _mem[dst:dst+n] = bytes([val & 0xFF]) * n


# =============================================================================
# Indirect call table
# =============================================================================
_func_table = {}


def register_func(idx: int, fn):
    """Register function in table."""
    _func_table[idx] = fn


def indirect_call(idx: int, *args):
    """Call function by table index."""
    if idx in _func_table:
        return _func_table[idx](*args)
    raise RuntimeError(f'indirect call to unregistered function {idx}')

# Alias
call_table = indirect_call


# =============================================================================
# Debug utilities
# =============================================================================
def dump_mem(addr: int, size: int = 64) -> str:
    """Hex dump of memory region."""
    lines = []
    for i in range(0, size, 16):
        hex_part = ' '.join(f'{_mem[addr+i+j]:02x}' for j in range(min(16, size-i)))
        lines.append(f'{addr+i:08x}: {hex_part}')
    return '\n'.join(lines)


def load_snapshot(path: str):
    """Load memory snapshot from file."""
    global _mem
    with open(path, 'rb') as f:
        data = f.read()
    _mem[:len(data)] = data


def save_snapshot(path: str):
    """Save memory snapshot to file."""
    with open(path, 'wb') as f:
        f.write(_mem)
