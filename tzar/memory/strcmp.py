"""
Function: $func79
Name: strcmp
Category: memory
Depth: 0
Status: done

Calls: none
Called by: 8 functions ($func946, $func951, $func949, $func952, $func947,
                        $func948, $func440, $func950)

String comparison function.

String structure:
- offset 4: pointer to null-terminated string data

Args:
    $var0: First string structure pointer
    $var1: Second string structure pointer
    $var2: Comparison mode (0 = pointer compare only, 1 = content compare)

Returns:
    1 if strings are equal, 0 otherwise
"""

from tzar._runtime import i32_load, i32_load8_u


def strcmp(str1_ptr: int, str2_ptr: int, mode: int) -> int:
    """
    Compare two strings.

    Args:
        str1_ptr: Pointer to first string structure
        str2_ptr: Pointer to second string structure
        mode: 0 = compare string pointers only, 1 = compare content

    Returns:
        1 if equal, 0 if not equal
    """
    if mode == 0:
        # Just compare the string pointers
        ptr1 = i32_load(str1_ptr, offset=4)
        ptr2 = i32_load(str2_ptr, offset=4)
        return 1 if ptr1 == ptr2 else 0

    # If same object, they're equal
    if str1_ptr == str2_ptr:
        return 1

    # Get string data pointers
    data1 = i32_load(str1_ptr, offset=4)
    data2 = i32_load(str2_ptr, offset=4)

    # Compare byte by byte
    offset = 0
    while True:
        char1 = i32_load8_u(data1 + offset)
        char2 = i32_load8_u(data2 + offset)

        # End of first string
        if char1 == 0:
            return 1 if char2 == 0 else 0

        # Characters don't match
        if char1 != char2:
            return 0

        offset += 1

    return 1


# Alias for WASM function name
func79 = strcmp
