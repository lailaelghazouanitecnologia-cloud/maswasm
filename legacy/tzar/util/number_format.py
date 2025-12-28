"""
Number formatting and utility functions - batch 20.

Functions for breaking down large numbers into display components.
"""

from tzar.util.simple_wrappers import func104


# ============================================================================
# func251: Constant zero
# ============================================================================

def func251(var0: int) -> int:
    """
    $func251: Always returns 0.

    A no-op function that ignores input and returns 0.
    Possibly a stub or placeholder.
    """
    return 0


# ============================================================================
# func215: Format hundreds
# ============================================================================

def func215(var0: int, var1: int) -> int:
    """
    $func215: Break number into hundreds and ones, format both.

    Divides var1 by 100, formats the quotient and remainder.

    Args:
        var0: Base pointer/context
        var1: Number to format (0-9999)

    Returns:
        Result from formatting the remainder
    """
    quotient = var1 // 100
    func104(var0, quotient)
    remainder = var1 - (quotient * 100)
    return func104(var0, remainder)


# ============================================================================
# func214: Format ten-thousands
# ============================================================================

def func214(var0: int, var1: int) -> int:
    """
    $func214: Break number into ten-thousands and hundreds, format recursively.

    Divides var1 by 10000, formats quotient, then calls func215 for remainder.

    Args:
        var0: Base pointer/context
        var1: Number to format (0-999999999)

    Returns:
        Result from formatting the remainder
    """
    quotient = var1 // 10000
    func104(var0, quotient)
    remainder = var1 - (quotient * 10000)
    return func215(var0, remainder)


# ============================================================================
# func213: Format millions
# ============================================================================

def func213(var0: int, var1: int) -> int:
    """
    $func213: Break number into millions and format recursively.

    Divides var1 by 1000000, formats quotient, then calls func214 for remainder.

    Args:
        var0: Base pointer/context
        var1: Number to format

    Returns:
        Result from formatting the remainder
    """
    quotient = var1 // 1000000
    func104(var0, quotient)
    remainder = var1 - (quotient * 1000000)
    return func214(var0, remainder)


# ============================================================================
# func254: Calculate and format rate/progress value
# ============================================================================

def func254(var0: int, var1: int) -> None:
    """
    $func254: Calculate and format a rate/progress value.

    Uses offset 16 and 24 of the input structure.
    If offset 24 >= 100, uses floating point lookup table at 32700.
    Otherwise calculates (offset_16 * 1000) / offset_24.

    Args:
        var0: Structure pointer with offsets 16 and 24
        var1: Output parameter for func113
    """
    from tzar._runtime import i32_load, f32_load
    from tzar.unknown.func113 import func113

    var2 = 0  # Result

    if var0 == 0:
        func113(var2 - 33, var1)
        return

    var3 = i32_load(var0 + 16)  # offset 16
    offset_24 = i32_load(var0 + 24)  # offset 24

    if offset_24 >= 100:
        # Use float lookup table
        table_offset = (offset_24 + var3) * 4 + 32700
        var4 = f32_load(table_offset)

        # Check if 0.0 <= var4 < 1000.0
        if var4 >= 0.0 and var4 < 1000.0:
            var2 = int(var4)  # truncate to unsigned int
    else:
        # Direct calculation
        var2 = (var3 * 1000) // offset_24

    func113(var2 - 33, var1)


# ============================================================================
# Aliases
# ============================================================================

fmt_zero = func251
fmt_hundreds = func215
fmt_ten_thousands = func214
fmt_millions = func213
fmt_rate = func254
