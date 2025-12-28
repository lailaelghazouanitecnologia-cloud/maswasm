"""
Simple wrapper and utility functions - batch 18.

These are thin wrapper functions that delegate to other functions
with minimal logic.
"""

from tzar._runtime import i32_load, i32_store, i64_store
from tzar.unknown.func309 import func309
from tzar.memory.af import af


# ============================================================================
# func122: Simple call wrapper
# ============================================================================

def func122(var0: int, var1: int, var2: int) -> None:
    """
    $func122: Wrapper that calls func309 with reordered args.

    Reorders arguments and calls func309, discarding the result.
    """
    func309(var1, var2, var0)


# ============================================================================
# func104: Offset calculator + func309 call
# ============================================================================

def func104(var0: int, var1: int) -> int:
    """
    $func104: Calculate offset and call func309.

    Computes address at 32304 + (var1 * 2) and calls func309.

    Returns:
        Result from func309
    """
    offset = (var1 << 1) + 32304  # var1 * 2 + 32304
    return func309(offset, 2, var0)


# ============================================================================
# func136: Conditional free with null
# ============================================================================

def func136(var0: int) -> None:
    """
    $func136: Free memory at pointer and null it.

    If var0 is non-zero, loads the pointer at var0,
    frees it via af, then stores 0 at var0.
    """
    if var0:
        ptr = i32_load(var0)
        af(ptr)
        i32_store(var0, 0)


# ============================================================================
# func116: Free linked list
# ============================================================================

def func116(var0: int) -> None:
    """
    $func116: Free a linked list structure.

    Frees the head allocation at [var0], then iterates through
    the linked list at offset 8, freeing each node and its data.

    Structure:
    - [var0 + 0]: Main data pointer
    - [var0 + 8]: Linked list head (offset 8 = next, offset 0 = data)
    """
    if var0 == 0:
        return

    # Load and free main data
    var1 = i32_load(var0 + 8)
    main_ptr = i32_load(var0)
    af(main_ptr)

    # Clear the structure
    i32_store(var0, 0)
    i64_store(var0 + 8, 0)  # Clear 8 bytes at offset 8

    if var1 == 0:
        return

    # Free linked list nodes
    while var1:
        next_node = i32_load(var1 + 8)
        node_data = i32_load(var1)
        af(node_data)
        af(var1)
        var1 = next_node


# ============================================================================
# func117: Conditional path dispatcher
# ============================================================================

def func117(var0: int, var1: int, var2: int) -> None:
    """
    $func117: Dispatch to func30 or func29 based on var1.

    If var1 is non-zero, calls func30 with multiple params.
    Otherwise, calls func29 with (var0, 1).
    """
    from tzar.unknown.func30 import func30
    from tzar.unknown.func29 import func29

    if var1:
        func30(var0, var1, var2, 0, 0, 0, -1, 25, 0)
        return
    func29(var0, 1)


# ============================================================================
# func150: Direct free wrapper (batch 19)
# ============================================================================

def func150(var0: int) -> None:
    """
    $func150: Direct wrapper for af (free).

    Simply calls af with the given pointer.
    """
    af(var0)


# ============================================================================
# func151: Conditional free (batch 19)
# ============================================================================

def func151(var0: int) -> None:
    """
    $func151: Conditional free.

    Frees the pointer only if it's non-zero.
    """
    if var0:
        af(var0)


# ============================================================================
# func190: Cleanup and free structure (batch 19)
# ============================================================================

def func190(var0: int) -> None:
    """
    $func190: Cleanup structure and free.

    Calls func191 for cleanup, then frees the structure itself.
    """
    if var0:
        func191(var0)
        af(var0)


# ============================================================================
# func191: Structure cleanup (batch 19)
# ============================================================================

def func191(var0: int) -> None:
    """
    $func191: Clean up a complex structure.

    Frees multiple nested allocations and clears the structure fields.
    Structure layout:
    - offset 12: sub-structure pointer
    - offset 120: ptr to free (func136)
    - offset 124: ptr to free (func136)
    - offset 136: ptr to free (func136)
    - offset 160: direct free ptr
    - offset 168: conditional free ptr (func151)
    - offset 172: linked list (func116)
    - offset 188: array of sub-structures
    - offset 192: count of sub-structures
    - offset 276: cleared to 0
    - offset 280: ptr to free and clear
    """
    # Free direct pointer at offset 160
    af(i32_load(var0 + 160))

    # Free linked list at offset 172
    func116(var0 + 172)

    # Conditional free at offset 168
    func151(i32_load(var0 + 168))

    # Free pointers via func136
    func136(var0 + 124)
    func136(var0 + 136)

    # Clear offset 120 area (storing 0 with offset and bitops)
    i32_store(var0 + 120, 0)

    # Iterate through sub-structures at offset 188
    count = i32_load(var0 + 192)
    if count > 0:
        array_base = i32_load(var0 + 188)
        for i in range(count):
            sub_ptr = i32_load(array_base + i * 4)
            if sub_ptr:
                sub_sub = i32_load(sub_ptr + 12)
                af(sub_sub)
                af(sub_ptr)

    # Clear remaining fields
    i32_store(var0 + 276, 0)
    i32_store(var0 + 192, 0)

    # Free and clear offset 280
    af(i32_load(var0 + 280))
    i32_store(var0 + 12, 0)
    i32_store(var0 + 280, 0)


# ============================================================================
# func51: Conditional result selection (batch 19)
# ============================================================================

def func51(var0: int, var1: int) -> int:
    """
    $func51: Get bits with conditional sign.

    Calls func33 twice and returns result with conditional negation.
    If func33(var0, 1) is non-zero, returns result as-is.
    Otherwise, returns negated result.
    """
    from tzar.unknown.func33 import func33

    result = func33(var0, var1)
    # select(0 - result, result, func33(var0, 1))
    # = result if condition != 0 else (0 - result)
    condition = func33(var0, 1)
    if condition:
        return result
    else:
        return 0 - result


# ============================================================================
# func187: Iterator with counter (batch 19)
# ============================================================================

def func187(var0: int) -> int:
    """
    $func187: Iterate func91 until condition met.

    Calls func91 repeatedly while offset 64 < offset 56 and offset 24 <= 0.
    Returns count of iterations.
    """
    from tzar.unknown.func91 import func91

    var1 = 0  # counter
    var2 = var0 + 64  # pointer to offset 64

    # Check if offset 64 >= offset 56
    if i32_load(var2) >= i32_load(var0 + 56):
        return var1

    while True:
        # Check if offset 24 > 0
        if i32_load(var0 + 24) > 0:
            break

        func91(var0)
        var1 += 1

        # Check if offset 64 >= offset 56
        if i32_load(var2) >= i32_load(var0 + 56):
            break

    return var1


# ============================================================================
# Aliases for exports
# ============================================================================

wrapper_func122 = func122
wrapper_func104 = func104
wrapper_func136 = func136
wrapper_func116 = func116
wrapper_func117 = func117
wrapper_func150 = func150
wrapper_func151 = func151
wrapper_func190 = func190
wrapper_func191 = func191
wrapper_func51 = func51
wrapper_func187 = func187
