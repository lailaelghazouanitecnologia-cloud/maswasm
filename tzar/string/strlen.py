"""
Function: $func209
Name: strlen
Category: string
Depth: 0
Status: done

Calls: none
Called by: 3 functions ($func121, $func313, $func211)

Standard C strlen - returns length of null-terminated string.
Uses SIMD-like optimization to check 4 bytes at a time.

The "magic" constants:
- 0x01010101 (16843009): When subtracted, borrows propagate if any byte is 0
- 0x80808080 (2139062144): Masks high bits to detect borrowed bytes

The trick: ((x - 0x01010101) & ~x & 0x80808080) != 0 if x has a zero byte.
"""

from tzar._runtime import memory, i32_load, i32_load8_u


# Magic constants for null-byte detection
MAGIC_LO = 0x01010101  # 16843009
MAGIC_HI = 0x80808080  # 2139062144 (or -2139062144 as signed)


def strlen(s: int) -> int:
    """
    Calculate length of null-terminated string.

    Args:
        s: Pointer to null-terminated string

    Returns:
        Number of bytes before the null terminator
    """
    ptr = s

    # Handle unaligned start - byte by byte until aligned to 4
    while ptr & 3:
        if i32_load8_u(ptr) == 0:
            return ptr - s
        ptr += 1

    # Fast path: check 4 bytes at a time
    while True:
        word = i32_load(ptr)
        # Check if any byte in word is zero:
        # (word - 0x01010101) & ~word & 0x80808080
        if ((word - MAGIC_LO) & (~word) & MAGIC_HI) != 0:
            break
        ptr += 4

    # Found a zero byte in the word - find exact position
    while i32_load8_u(ptr) != 0:
        ptr += 1

    return ptr - s


# Alias for WASM function name
func209 = strlen
