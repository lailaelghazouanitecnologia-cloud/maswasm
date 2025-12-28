"""
Function: $func76
Name: cos_approx
Category: math
Depth: 0
Status: done

Calls: none
Called by: 2 functions ($func49, $func48)

Fast cosine approximation using Taylor series polynomial.
cos(x) ≈ 1 - x²/2! + x⁴/4! - x⁶/6! + x⁸/8!

Coefficients used:
- x²: -0.499999997251031     ≈ -1/2
- x⁴: 0.04166662332373906    ≈ 1/24
- x⁶: -0.001388676377460993  ≈ -1/720
- x⁸: 0.00002439044879627741 ≈ 1/40320
"""


def cos_approx(x: float) -> float:
    """
    Calculate cosine using Taylor series approximation.

    Args:
        x: Angle in radians (f64)

    Returns:
        Approximate cos(x) as f32
    """
    x2 = x * x      # x²
    x4 = x2 * x2    # x⁴

    # Horner's method:
    # 1 + x²(-1/2 + x²(1/24 + x²(-1/720 + x²/40320)))
    result = (
        1.0 +
        x2 * -0.499999997251031 +
        x4 * 0.04166662332373906 +
        x4 * x2 * (-0.001388676377460993 + x2 * 0.00002439044879627741)
    )

    return float(result)  # demote to f32


# Alias for WASM function name
func76 = cos_approx
