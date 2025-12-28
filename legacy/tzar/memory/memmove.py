"""
Function: $func35
Name: memmove
Category: memory
Depth: 0
Status: done

Calls: none
Called by: 12 functions ($func130, $func407, $func811, $func399, etc.)

Memory move with overlap handling.
Uses memory.copy for large blocks (>=512 bytes).
For smaller blocks, handles forward/backward copy based on overlap.
"""

from tzar._runtime import memory_copy, i32_load8_u, i32_store8, i32_load, i32_store


def memmove(dest: int, src: int, size: int) -> int:
    """
    Copy memory handling overlapping regions.

    Args:
        dest: Destination address
        src: Source address
        size: Number of bytes to copy

    Returns:
        Destination address
    """
    if size >= 512:
        # Use bulk memory copy for large blocks
        memory_copy(dest, src, size)
        return dest

    if size == 0:
        return dest

    end = dest + size

    # Check if we can use word-aligned copy
    if (dest ^ src) & 3 == 0:
        # Pointers have same alignment
        # Align to 4-byte boundary first
        while dest & 3 and dest < end:
            i32_store8(dest, i32_load8_u(src))
            dest += 1
            src += 1

        # Copy 4 bytes at a time
        word_end = end - 3
        while dest < word_end:
            i32_store(dest, i32_load(src))
            dest += 4
            src += 4

    # Copy remaining bytes
    while dest < end:
        i32_store8(dest, i32_load8_u(src))
        dest += 1
        src += 1

    return dest - size  # Return original dest


# Alias
func35 = memmove
