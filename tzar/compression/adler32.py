"""
Function: $func89
Name: adler32
Category: compression
Depth: 0
Status: done

Calls: none
Called by: 4 functions ($func399, $func178, $func407, $func298)

Adler-32 checksum algorithm - used by zlib/deflate compression.
This is a rolling checksum that's faster than CRC32 but less robust.

The checksum consists of two 16-bit values:
- s1 (low 16 bits): sum of all bytes + 1
- s2 (high 16 bits): sum of all s1 values

Both are taken modulo 65521 (largest prime < 2^16).

Constants:
- MOD_ADLER = 65521 (modulus for both sums)
- NMAX = 5552 (max bytes before modulo overflow possible)
"""

from tzar._runtime import memory


# Adler-32 constants
MOD_ADLER = 65521  # Largest prime smaller than 65536
NMAX = 5552        # Largest n such that 255*n*(n+1)/2 + (n+1)*(BASE-1) <= 2^32-1


def adler32(adler: int, buf: int, length: int) -> int:
    """
    Compute Adler-32 checksum.

    Args:
        adler: Initial/running checksum value
        buf: Pointer to data buffer
        length: Number of bytes to process

    Returns:
        Updated Adler-32 checksum
    """
    # Split into two 16-bit components
    s1 = adler & 0xFFFF         # Low 16 bits
    s2 = (adler >> 16) & 0xFFFF  # High 16 bits

    # Handle single byte case efficiently
    if length == 1:
        s1 = s1 + memory[buf]
        if s1 > 65520:
            s1 -= MOD_ADLER
        s2 = s2 + s1
        if s2 > 65520:
            s2 -= MOD_ADLER
        return (s2 << 16) | s1

    # Handle empty buffer
    if buf == 0:
        return 1

    # Process data
    if length >= 16:
        # Process in NMAX chunks to avoid overflow
        while length > NMAX:
            length -= NMAX
            # Process 347 iterations of 16 bytes = 5552 bytes
            ptr = buf
            for _ in range(347):
                # Unrolled loop: process 16 bytes
                for offset in range(16):
                    s1 += memory[ptr + offset]
                    s2 += s1
                ptr += 16
            # Apply modulo after chunk
            s1 = s1 % MOD_ADLER
            s2 = s2 % MOD_ADLER
            buf += NMAX

        # Process remaining 16-byte blocks
        if length > 0:
            while length >= 16:
                for offset in range(16):
                    s1 += memory[buf + offset]
                    s2 += s1
                buf += 16
                length -= 16

            # Process remaining bytes
            while length > 0:
                s1 += memory[buf]
                s2 += s1
                buf += 1
                length -= 1

            # Final modulo
            s1 = s1 % MOD_ADLER
            s2 = s2 % MOD_ADLER

        return (s2 << 16) | s1

    # Short buffer (< 16 bytes)
    if length == 0:
        # Just apply modulo to existing checksum
        s2 = s2 % MOD_ADLER
        if s1 > 65520:
            s1 -= MOD_ADLER
        return (s2 << 16) | s1

    # Process remaining bytes one at a time
    for i in range(length):
        s1 += memory[buf + i]
        s2 += s1

    # Final reduction
    s2 = s2 % MOD_ADLER
    if s1 > 65520:
        s1 -= MOD_ADLER

    return (s2 << 16) | s1


# Alias for WASM function name
func89 = adler32
