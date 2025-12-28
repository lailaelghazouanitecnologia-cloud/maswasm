"""
Function: $func79
Name: string_object_equal
Category: string
Depth: 0
Status: done

Calls: none
Called by: 8 functions ($func946, $func951, $func949, $func952, etc.)

Compares two string objects for equality.
Objects have a string pointer at offset 4.

If mode=0: Compare string pointers only (identity check)
If mode=1: Compare actual string contents (deep comparison)
"""

from tzar._runtime import i32_load, i32_load8_u


def string_object_equal(obj1: int, obj2: int, mode: int) -> int:
    """
    Compare two string objects for equality.

    Args:
        obj1: Pointer to first string object
        obj2: Pointer to second string object
        mode: 0 for pointer comparison, non-zero for content comparison

    Returns:
        1 if equal, 0 if not equal
    """
    if mode == 0:
        # Pointer comparison mode
        ptr1 = i32_load(obj1 + 4)
        ptr2 = i32_load(obj2 + 4)
        return 1 if ptr1 == ptr2 else 0

    # Same object - always equal
    if obj1 == obj2:
        return 1

    # Get string pointers
    str1 = i32_load(obj1 + 4)
    str2 = i32_load(obj2 + 4)

    # Compare strings byte by byte
    while True:
        c1 = i32_load8_u(str1)
        c2 = i32_load8_u(str2)

        # End of string
        if c1 == 0:
            return 1 if c2 == 0 else 0

        # Characters differ
        if c1 != c2:
            return 0

        str1 += 1
        str2 += 1


# Alias
func79 = string_object_equal
