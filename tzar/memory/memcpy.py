"""
Function: $func35
Name: memcpy
Category: memory
Depth: 0
Status: done

Calls: none
Called by: 12 functions ($func130, $func407, $func811, $func399, $func121,
                         $func823, $func128, $func178, $func822, $func391, ...)

Memory copy function - copies $var2 bytes from $var1 (src) to $var0 (dst).
Returns the destination pointer.

The original WAT has optimizations for:
- Large copies (>=512 bytes): uses native memory.copy
- Aligned copies: copies 4 bytes at a time, unrolled to 64 bytes per iteration
- Unaligned copies: byte-by-byte with 4-byte unrolling
"""

from tzar._runtime import memory


def memcpy(dst: int, src: int, size: int) -> int:
    """
    Copy memory from src to dst.

    Args:
        dst: Destination address
        src: Source address
        size: Number of bytes to copy

    Returns:
        Destination address (for chaining)
    """
    if size <= 0:
        return dst

    # Direct slice copy - Python handles this efficiently
    memory[dst:dst + size] = memory[src:src + size]

    return dst


# Alias for WASM function name
func35 = memcpy
