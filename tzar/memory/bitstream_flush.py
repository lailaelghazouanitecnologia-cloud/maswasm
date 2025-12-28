"""
Function: $func50
Name: bitstream_flush
Category: memory
Depth: 0
Status: done

Calls: none
Called by: 5 functions ($func130, $func407, $func399, $func823, $func822)

Flush pending bits from a bitstream buffer to output.
Part of compression/decompression system (likely zlib/deflate).

Structure layout at $var0:
- offset 8:    output buffer pointer
- offset 20:   current output position
- offset 5816: bit buffer (16-bit, little-endian)
- offset 5820: number of valid bits in buffer
"""

from tzar._runtime import (
    i32_load, i32_load8_u, i32_store, i32_store8, i32_store16
)


def bitstream_flush(stream_ptr: int) -> None:
    """
    Flush pending bits from bitstream to output buffer.

    If 16 bits are pending, writes both bytes and clears buffer.
    If 8+ bits are pending, writes low byte and shifts buffer.

    Args:
        stream_ptr: Pointer to bitstream structure
    """
    bit_count = i32_load(stream_ptr, offset=5820)

    if bit_count == 16:
        # Write both bytes
        output_ptr = i32_load(stream_ptr, offset=8)
        pos = i32_load(stream_ptr, offset=20)

        # Write low byte
        low_byte = i32_load8_u(stream_ptr, offset=5816)
        i32_store8(output_ptr + pos, low_byte)
        i32_store(stream_ptr, pos + 1, offset=20)

        # Write high byte
        pos = i32_load(stream_ptr, offset=20)
        high_byte = i32_load8_u(stream_ptr + 5817)
        i32_store8(output_ptr + pos, high_byte)
        i32_store(stream_ptr, pos + 1, offset=20)

        # Clear buffer
        i32_store16(stream_ptr, 0, offset=5816)
        i32_store(stream_ptr, 0, offset=5820)

    elif bit_count >= 8:
        # Write low byte only
        output_ptr = i32_load(stream_ptr, offset=8)
        pos = i32_load(stream_ptr, offset=20)

        low_byte = i32_load8_u(stream_ptr, offset=5816)
        i32_store8(output_ptr + pos, low_byte)
        i32_store(stream_ptr, pos + 1, offset=20)

        # Shift buffer: move high byte to low position
        high_byte = i32_load8_u(stream_ptr + 5817)
        i32_store16(stream_ptr, high_byte, offset=5816)
        i32_store(stream_ptr, bit_count - 8, offset=5820)

    # If bit_count < 8, do nothing


# Alias for WASM function name
func50 = bitstream_flush
