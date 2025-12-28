"""
Function: $func168
Name: scalbn
Category: math
Depth: 0
Status: done

Calls: none
Called by: 1 function ($func435)

Scalbn - scale by power of 2 (ldexp equivalent).
Computes x * 2^n efficiently using IEEE 754 exponent manipulation.

This is a common math library function used by:
- ldexp(x, n) = x * 2^n
- scalbn(x, n) = x * 2^n
- frexp/modf operations

Key constants:
- 8.98846567431158e+307 = 2^1023 (max normal exponent)
- 2.004168360008973e-292 = 2^-969 (for denormals)
- 1023 = IEEE 754 double exponent bias
- 52 = mantissa bits in double
"""

import struct


# Constants for scaling
TWO_POW_1023 = 8.98846567431158e+307   # 2^1023
TWO_POW_NEG969 = 2.004168360008973e-292  # 2^-969


def scalbn(x: float, n: int) -> float:
    """
    Scale x by 2^n (compute x * 2^n).

    Args:
        x: The value to scale
        n: The power of 2 exponent

    Returns:
        x * 2^n
    """
    # Handle large positive exponent (risk of overflow)
    if n >= 1024:
        x = x * TWO_POW_1023
        if n < 2047:
            n = n - 1023
        else:
            # Very large exponent - multiply again
            x = x * TWO_POW_1023
            # Clamp n to max 3069
            if n >= 3069:
                n = 3069
            n = n - 2046
    # Handle large negative exponent (risk of underflow)
    elif n <= -1023:
        x = x * TWO_POW_NEG969
        if n > -1992:
            n = n + 969
        else:
            # Very small exponent - multiply again
            x = x * TWO_POW_NEG969
            # Clamp n to min -2960
            if n <= -2960:
                n = -2960
            n = n + 1938

    # Construct 2^n by building IEEE 754 double:
    # exponent field = n + 1023 (bias), shifted to bits 52-62
    exp_bits = (n + 1023) << 52
    # Reinterpret as float
    two_pow_n = struct.unpack('d', struct.pack('Q', exp_bits))[0]

    return x * two_pow_n


# Alias for WASM function name
func168 = scalbn
