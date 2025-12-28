"""
Tzar Engine - Math module.
Taylor series approximations for trigonometric functions.
"""


def sin_approx(x: float) -> float:
    """
    Fast sine approximation using Taylor series.
    sin(x) ≈ x - x³/3! + x⁵/5! - x⁷/7! + ...
    """
    x2 = x * x
    x3 = x2 * x
    x5 = x2 * x3
    x7 = x5 * x2

    # Coefficients from Taylor expansion
    c5 = 0.008333329385889463      # ≈ 1/120 = 1/5!
    c3 = -0.16666666641626524      # ≈ -1/6 = -1/3!
    c7 = -0.00019839334836096632   # ≈ -1/5040 = -1/7!
    c9 = 2.718311493989822e-06     # ≈ 1/362880 = 1/9!

    return x + x3 * (c3 + x2 * c5) + x7 * (c7 + x2 * c9)


def cos_approx(x: float) -> float:
    """
    Fast cosine approximation using Taylor series.
    cos(x) ≈ 1 - x²/2! + x⁴/4! - x⁶/6! + ...
    """
    x2 = x * x
    x4 = x2 * x2
    x8 = x4 * x4

    # Coefficients from Taylor expansion
    c2 = -0.499999997251031        # ≈ -1/2 = -1/2!
    c4 = 0.04166662332373906       # ≈ 1/24 = 1/4!
    c6 = -0.001388676377460993     # ≈ -1/720 = -1/6!
    c8 = 2.439044879627741e-05     # ≈ 1/40320 = 1/8!

    return 1.0 + x2 * c2 + x4 * c4 + x8 * (c6 + x2 * c8)


def clamp_i32(value: int, min_val: int, max_val: int) -> int:
    """Clamp integer value to range [min_val, max_val]."""
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value


# Legacy function aliases for compatibility
func75 = sin_approx
func76 = cos_approx
