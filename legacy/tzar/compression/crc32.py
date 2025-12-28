"""
Function: $func43
Name: crc32
Category: compression
Depth: 0
Status: done

Calls: none
Called by: 4 functions ($func399, $func178, $func407, $func298)

CRC-32 checksum calculation using lookup table at address 18224.
Used for data integrity verification in compressed data streams.
"""

from tzar._runtime import i32_load, i32_load8_u


# CRC32 lookup table address
CRC32_TABLE = 18224


def crc32(data_ptr: int, initial: int, length: int) -> int:
    """
    Calculate CRC-32 checksum.

    Args:
        data_ptr: Pointer to data buffer
        initial: Initial CRC value (typically 0)
        length: Number of bytes to process

    Returns:
        CRC-32 checksum
    """
    if initial == 0:
        return 0

    # Start with inverted initial value
    crc = initial ^ 0xFFFFFFFF

    # Process bytes with table lookup
    if length >= 23:
        # Unrolled loop for performance - process 8 bytes at a time
        aligned_end = length & ~7
        i = 0
        while i < aligned_end:
            for _ in range(8):
                byte = i32_load8_u(data_ptr + i)
                index = (crc ^ byte) & 0xFF
                crc = i32_load(CRC32_TABLE + index * 4) ^ (crc >> 8)
                i += 1

    # Process remaining bytes
    remaining = length & 7
    offset = length - remaining
    for i in range(remaining):
        byte = i32_load8_u(data_ptr + offset + i)
        index = (crc ^ byte) & 0xFF
        crc = i32_load(CRC32_TABLE + index * 4) ^ (crc >> 8)

    # Return inverted result
    return crc ^ 0xFFFFFFFF


# Alias
func43 = crc32
