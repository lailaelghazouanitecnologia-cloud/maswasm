"""
Function: $func50
Name: flush_bits
Category: compression
Depth: 0
Status: done

Calls: none
Called by: 5 functions ($func130, $func407, $func399, $func823, $func822)

Flushes pending bits from bit buffer to output stream.
Part of deflate/zlib compression implementation.

Stream structure offsets:
- offset 8: output buffer pointer
- offset 20: output position
- offset 5816: bit buffer (2 bytes)
- offset 5820: bit count
"""

from tzar._runtime import i32_load, i32_store, i32_load8_u, i32_store8


def flush_bits(stream: int) -> None:
    """
    Flush pending bits from compression stream's bit buffer.

    Args:
        stream: Pointer to compression stream structure
    """
    bit_count = i32_load(stream + 5820)

    if bit_count == 16:
        # Full 16 bits - write both bytes
        out_pos = i32_load(stream + 20)
        out_buf = i32_load(stream + 8)

        # Write low byte
        i32_store8(out_buf + out_pos, i32_load8_u(stream + 5816))
        i32_store(stream + 20, out_pos + 1)

        # Write high byte
        out_pos = i32_load(stream + 20)
        i32_store8(out_buf + out_pos, i32_load8_u(stream + 5817))
        i32_store(stream + 20, out_pos + 1)

        # Clear bit buffer
        i32_store(stream + 5820, 0)
    elif bit_count >= 8:
        # At least 8 bits - write low byte
        out_pos = i32_load(stream + 20)
        out_buf = i32_load(stream + 8)

        i32_store8(out_buf + out_pos, i32_load8_u(stream + 5816))
        i32_store(stream + 20, out_pos + 1)

        # Shift high byte to low position
        high_byte = i32_load8_u(stream + 5817)
        i32_store(stream + 5816, high_byte)

        # Reduce bit count by 8
        i32_store(stream + 5820, bit_count - 8)


# Alias
func50 = flush_bits
