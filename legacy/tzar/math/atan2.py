"""
Function: $func262
Name: atan2
Category: math
Depth: 1
Status: done

Calls: $func424 (atan)
Called by: 3 functions ($func350, $func61, $func126)

Two-argument arctangent - returns angle in radians between
the positive x-axis and the point (x, y).

Handles all quadrants and special cases (infinities, zeros).

Lookup tables:
- 28800: angles for infinity cases
- 28832: various angle constants

Constants:
- PI = 3.141592653589793
- PI/2 = 1.5707963267948966
- PI_LO = 1.2246467991473532e-16 (low-order correction)
"""

import struct
import math

from tzar.math.atan import atan


# Constants
PI = 3.141592653589793
PI_2 = 1.5707963267948966  # PI/2
PI_LO = 1.2246467991473532e-16  # Low-order correction for PI

# Lookup tables for infinity cases (angles for each quadrant)
ATAN2_PI = [
    0.7853981633974483,   # pi/4 (both positive inf)
    2.356194490192345,    # 3*pi/4 (y pos, x neg inf)
    -0.7853981633974483,  # -pi/4 (y neg, x pos inf)
    -2.356194490192345,   # -3*pi/4 (both negative inf)
]


def atan2(y: float, x: float) -> float:
    """
    Compute angle theta from rectangular coordinates (x, y).

    Args:
        y: Y coordinate
        x: X coordinate

    Returns:
        Angle in radians from -PI to PI
    """
    # Get IEEE 754 bits
    y_bits = struct.unpack('Q', struct.pack('d', y))[0]
    x_bits = struct.unpack('Q', struct.pack('d', x))[0]

    # Check for NaN
    y_abs = y_bits & 0x7FFFFFFFFFFFFFFF
    x_abs = x_bits & 0x7FFFFFFFFFFFFFFF

    # If either is NaN (exponent all 1s, mantissa non-zero)
    if y_abs > 0x7FF0000000000000 or x_abs > 0x7FF0000000000000:
        return y + x  # Propagate NaN

    # Extract high words for magnitude comparison
    x_hi = (x_bits >> 32) & 0xFFFFFFFF
    y_hi = (y_bits >> 32) & 0xFFFFFFFF
    x_lo = x_bits & 0xFFFFFFFF
    y_lo = y_bits & 0xFFFFFFFF

    # If x = 1.0 exactly, return atan(y)
    if x_hi == 0x3FF00000 and x_lo == 0:
        return atan(y)

    # Compute quadrant code: bit 1 = sign of x, bit 0 = sign of y
    x_sign = (x_hi >> 30) & 2  # 2 if x negative, 0 otherwise
    y_sign = y_bits >> 63      # 1 if y negative, 0 otherwise
    quad = x_sign | y_sign

    # Absolute values of high words
    y_hi_abs = y_hi & 0x7FFFFFFF
    x_hi_abs = x_hi & 0x7FFFFFFF

    # Case: y = 0
    if y_hi_abs == 0 and y_lo == 0:
        if quad == 2:
            return PI      # y=0, x<0 -> PI
        elif quad == 3:
            return -PI     # y=-0, x<0 -> -PI
        else:
            return y       # y=0, x>=0 -> ±0

    # Case: x = 0
    if x_hi_abs == 0 and x_lo == 0:
        return math.copysign(PI_2, y)

    # Case: both infinite
    if x_hi_abs == 0x7FF00000:
        if y_hi_abs == 0x7FF00000:
            return ATAN2_PI[quad]

    # Case: y is infinite but x is not
    if y_hi_abs == 0x7FF00000:
        return math.copysign(PI_2, y)

    # Case: magnitudes differ by more than 2^26
    if x_hi_abs + 0x04000000 < y_hi_abs:
        return math.copysign(PI_2, y)

    # Compute atan(|y/x|)
    if x_sign != 0 and y_hi_abs + 0x04000000 < x_hi_abs:
        # x is negative and |y| << |x|
        z = 0.0
    else:
        z = atan(abs(y / x))

    # Adjust for quadrant
    if quad == 0:
        return z            # First quadrant
    elif quad == 1:
        return -z           # Fourth quadrant
    elif quad == 2:
        return PI - (z - PI_LO)  # Second quadrant
    else:
        return (z - PI_LO) - PI  # Third quadrant


# Alias for WASM function name
func262 = atan2
