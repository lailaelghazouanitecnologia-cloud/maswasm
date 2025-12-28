"""
Trigonometric functions - Taylor series approximations.

These are optimized polynomial approximations for sin/cos.
"""


def func75(var0: float) -> float:
    """
    $func75: Sine approximation using Taylor series.

    Computes sin(x) for input x in radians using polynomial approximation.
    sin(x) ≈ x - x³/3! + x⁵/5! - x⁷/7! + ...

    Coefficients are optimized Chebyshev approximations for accuracy.

    Args:
        var0: Angle in radians (f64)

    Returns:
        Approximate sine value (f32)
    """
    var1 = var0 * var0  # x²
    var2 = var1 * var0  # x³

    result = (
        var0 +  # x
        var2 * (var1 * 0.008333329385889463 + (-0.16666666641626524)) +  # -x³/6 + x⁵/120
        (var1 * var1) * var2 * (var1 * 0.000002718311493989822 + (-0.00019839334836096632))  # higher terms
    )

    return float(result)


def func76(var0: float) -> float:
    """
    $func76: Cosine approximation using Taylor series.

    Computes cos(x) for input x in radians using polynomial approximation.
    cos(x) ≈ 1 - x²/2! + x⁴/4! - x⁶/6! + ...

    Coefficients are optimized Chebyshev approximations for accuracy.

    Args:
        var0: Angle in radians (f64)

    Returns:
        Approximate cosine value (f32)
    """
    var0 = var0 * var0  # x² (reuse var0)
    var1 = var0 * var0  # x⁴

    result = (
        1.0 +
        var0 * (-0.499999997251031) +  # -x²/2
        var1 * 0.04166662332373906 +   # x⁴/24
        var0 * var1 * (var0 * 0.00002439044879627741 + (-0.001388676377460993))  # higher terms
    )

    return float(result)


# Aliases
sin_approx = func75
cos_approx = func76
