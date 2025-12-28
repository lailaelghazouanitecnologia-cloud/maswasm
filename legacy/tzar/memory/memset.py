"""
Function: $func98
Name: memset
Category: memory
Depth: 0
Status: done

Calls: none
Called by: 6 functions ($func107, $func407, $func186, $gf, $func178, $func252)

Memory fill function - fills $var2 bytes at $var0 with value $var1.
Optimized for large fills (>=512) using native memory.fill,
otherwise uses 64-bit writes for efficiency.
"""

from tzar._runtime import memory


def memset(dst: int, value: int, size: int) -> None:
    """
    Fill memory with a byte value.

    Args:
        dst: Destination address
        value: Byte value to fill (signed, extended from 8 bits)
        size: Number of bytes to fill
    """
    if size == 0:
        return

    # Sign extend from 8 bits
    byte_val = value & 0xFF

    # Fill memory using Python's efficient slice assignment
    memory[dst:dst + size] = bytes([byte_val]) * size


# Alias for WASM function name
func98 = memset
