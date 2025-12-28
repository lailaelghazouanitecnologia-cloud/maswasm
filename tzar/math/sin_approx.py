"""
Function: $func75
Name: sin_approx
Category: math
Depth: 0
Status: done

Calls: none
Called by: 2 functions ($func49, $func48)

Fast sine approximation using Taylor series polynomial.
sin(x) ≈ x - x³/3! + x⁵/5! - x⁷/7! + x⁹/9!

Coefficients used:
- x³: -0.16666666641626524  ≈ -1/6
- x⁵: 0.008333329385889463  ≈ 1/120
- x⁷: -0.00019839334836096632 ≈ -1/5040
- x⁹: 0.000002718311493989822 ≈ 1/362880
"""


def sin_approx(x: float) -> float:
    """
    Calculate sine using Taylor series approximation.

    Args:
        x: Angle in radians (f64)

    Returns:
        Approximate sin(x) as f32
    """
    x2 = x * x      # x²
    x3 = x2 * x     # x³
    x4 = x2 * x2    # x⁴

    # Horner's method for efficiency:
    # x + x³(-1/6 + x²(1/120 + x²(-1/5040 + x²/362880)))
    result = (
        x +
        x3 * (-0.16666666641626524 + x2 * 0.008333329385889463) +
        x3 * x4 * (-0.00019839334836096632 + x2 * 0.000002718311493989822)
    )

    return float(result)  # demote to f32


# Alias for WASM function name
func75 = sin_approx
