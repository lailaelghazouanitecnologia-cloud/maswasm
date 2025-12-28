"""
Function: $func43
Name: crc32
Category: memory
Depth: 0
Status: done

Calls: none
Called by: 4 functions ($func399, $func178, $func407, $func298)

CRC32 checksum calculation using a lookup table at address 18224.
Standard CRC32 algorithm with table-based optimization.

Args:
    $var0: Initial CRC value (usually 0 or -1)
    $var1: Pointer to data buffer
    $var2: Length of data

Returns:
    CRC32 checksum (inverted)
"""

from tzar._runtime import memory, i32_load, i32_load8_u

# CRC32 lookup table address in memory
CRC32_TABLE_ADDR = 18224


def crc32(initial_crc: int, data_ptr: int, length: int) -> int:
    """
    Calculate CRC32 checksum.

    Args:
        initial_crc: Initial CRC value (0 for new calculation)
        data_ptr: Pointer to data in memory
        length: Number of bytes to process

    Returns:
        CRC32 checksum
    """
    if length == 0:
        return 0

    # Start with inverted CRC (standard CRC32 initialization)
    crc = initial_crc ^ 0xFFFFFFFF

    # Process each byte
    for i in range(length):
        byte = i32_load8_u(data_ptr + i)
        # table[(crc ^ byte) & 0xFF] ^ (crc >> 8)
        table_idx = (crc ^ byte) & 0xFF
        table_value = i32_load(CRC32_TABLE_ADDR + table_idx * 4)
        crc = table_value ^ ((crc >> 8) & 0x00FFFFFF)

    # Return inverted result
    return crc ^ 0xFFFFFFFF


# Alias for WASM function name
func43 = crc32
