"""
Function: $func424
Name: atan
Category: math
Depth: 0
Status: done

Calls: none
Called by: 1 function ($func262)

Arctangent (atan) implementation using polynomial approximation.
Uses argument reduction and rational polynomial for accuracy.

The function reduces the argument to a small range and uses
lookup tables for offset values at specific points.

Lookup tables at addresses:
- 28736: atan values at reduction points
- 28768: low-order correction terms

Polynomial coefficients for Pade approximant of atan(x)/x.
"""

import struct
import math


# Precomputed atan values for reduction
# atanhi[i] = atan(reduction_point[i])
ATAN_HI = [
    0.4636476090008061,   # atan(0.5)
    0.7853981633974483,   # atan(1) = pi/4
    0.9827937232473290,   # atan(1.5)
    1.5707963267948966,   # atan(inf) = pi/2
]

# Low-order correction terms
ATAN_LO = [
    2.2698777452961687e-17,
    3.0616169978683830e-17,
    1.3903311031230998e-17,
    6.1232339957367660e-17,
]

# Polynomial coefficients for odd powers (negative)
A_COEFFS = [
    -0.036531572744216916,
    -0.058335701337905735,
    -0.0769187620504483,
    -0.11111110405462356,
    -0.19999999999876483,
]

# Polynomial coefficients for even powers (positive)
B_COEFFS = [
    0.016285820115365782,
    0.049768779946159324,
    0.06661073137387531,
    0.09090887133436507,
    0.14285714272503466,
    0.3333333333333293,
]


def atan(x: float) -> float:
    """
    Compute arctangent of x.

    Args:
        x: Input value

    Returns:
        atan(x) in radians
    """
    # Get IEEE 754 bits
    bits = struct.unpack('Q', struct.pack('d', x))[0]
    high = (bits >> 32) & 0x7FFFFFFF  # Absolute value of high word
    sign = bits >> 63  # Sign bit

    # Check for special cases: |x| >= 2^26 (very large)
    if high >= 0x44100000:  # 1141899264
        # Check for NaN
        abs_bits = bits & 0x7FFFFFFFFFFFFFFF
        if abs_bits > 0x7FF0000000000000:
            return x  # NaN
        # Return ±pi/2 for infinity or very large
        result = 1.5707963267948966  # pi/2
        return -result if sign else result

    # Determine reduction range
    if high <= 0x3FDC0000:  # |x| <= 0.4375
        if high < 0x3E200000:  # |x| < 2^-29, return x
            return x
        idx = -1
    else:
        x_abs = abs(x)
        if high <= 0x3FF30000:  # |x| <= 1.1875
            if high <= 0x3FE60000:  # |x| <= 0.6875
                # Reduce: x = (2x - 1) / (2 + x)
                x = (2.0 * x_abs - 1.0) / (2.0 + x_abs)
                idx = 0
            else:
                # Reduce: x = (x - 1) / (x + 1)
                x = (x_abs - 1.0) / (x_abs + 1.0)
                idx = 1
        elif high <= 0x40038000:  # |x| <= 2.4375
            # Reduce: x = (x - 1.5) / (1 + 1.5*x)
            x = (x_abs - 1.5) / (1.0 + 1.5 * x_abs)
            idx = 2
        else:
            # Reduce: x = -1/x
            x = -1.0 / x_abs
            idx = 3

    # Compute polynomial approximation
    x2 = x * x
    x4 = x2 * x2

    # Odd power terms
    s = x4 * (x4 * (x4 * (x4 * A_COEFFS[0] + A_COEFFS[1]) + A_COEFFS[2]) + A_COEFFS[3]) + A_COEFFS[4]

    # Even power terms
    t = x2 * (x4 * (x4 * (x4 * (x4 * (x4 * B_COEFFS[0] + B_COEFFS[1]) + B_COEFFS[2]) + B_COEFFS[3]) + B_COEFFS[4]) + B_COEFFS[5])

    if idx < 0:
        # No reduction needed
        result = x - x * (s + t)
    else:
        # Apply reduction offset
        result = ATAN_HI[idx] - (x * (s + t) + ATAN_LO[idx] - x)

    return -result if sign else result


# Alias for WASM function name
func424 = atan
