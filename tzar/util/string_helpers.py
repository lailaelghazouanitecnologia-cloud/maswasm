"""
String and memory helper functions - batch 21.

Functions for string manipulation and memory management helpers.
"""

from tzar._runtime import (
    i32_load, i32_load8_u, i32_store, i32_store8,
    i32_atomic_rmw_add
)
from tzar.memory.af import af


# ============================================================================
# func312: Set string length (leaf)
# ============================================================================

def func312(var0: int, var1: int) -> None:
    """
    $func312: Set string length with small-string optimization.

    If high bit of offset 11 is set (long string), stores at offset 4.
    Otherwise, modifies the byte at offset 11 to encode length.

    Args:
        var0: String structure pointer
        var1: New length value
    """
    if (i32_load8_u(var0 + 11) >> 7) != 0:
        # Long string - store length at offset 4
        i32_store(var0 + 4, var1)
        return

    # Short string - encode in byte at offset 11
    # Set high bit (128) and combine with length
    current = i32_load8_u(var0 + 11)
    i32_store8(var0 + 11, (current & 128) | var1)
    # Clear high bit
    current = i32_load8_u(var0 + 11)
    i32_store8(var0 + 11, current & 127)


# ============================================================================
# func307: Reference counting decrement
# ============================================================================

def func307(var0: int) -> int:
    """
    $func307: Decrement reference count and potentially free.

    Decrements atomic counter at (offset_4 - 12 + 8).
    If counter goes below 0, frees the object.

    Args:
        var0: Object pointer

    Returns:
        var0 (for chaining)
    """
    # Set vtable pointer
    i32_store(var0, 32988)

    # Calculate ref count location
    var1 = i32_load(var0 + 4) - 12

    # Atomic decrement at offset 8 from var1
    ref_addr = var1 + 8
    old_count = i32_atomic_rmw_add(ref_addr, -1)

    # If old_count - 1 < 0, free the object
    if (old_count - 1) < 0:
        af(var1)

    return var0


# ============================================================================
# func306: Cleanup and free object
# ============================================================================

def func306(var0: int) -> None:
    """
    $func306: Clean up object and free memory.

    Calls func307 (ref count decrement) then frees var0.
    """
    func307(var0)
    af(var0)


# ============================================================================
# func314: Allocate and store size
# ============================================================================

def func314(var0: int, var1: int, var2: int) -> None:
    """
    $func314: Allocate memory and store size.

    Allocates var2 bytes via func26, stores result at var0,
    and stores size at var0 + 4.

    Args:
        var0: Output structure pointer
        var1: Unused
        var2: Size to allocate
    """
    from tzar.memory.func26 import func26

    allocated = func26(var2)
    i32_store(var0 + 4, var2)
    i32_store(var0, allocated)


# ============================================================================
# func294: Conditional callback dispatch
# ============================================================================

def func294(var0: int) -> None:
    """
    $func294: Dispatch callback based on game state flags.

    Checks offset 92 and various global flags, then calls func28.

    Args:
        var0: Entity/object pointer
    """
    from tzar.unknown.func28 import func28

    # Check if offset 92 is zero
    if i32_load(var0 + 92) == 0:
        return

    # Load global flag
    var1 = i32_load8_u(9147141)

    # Check another global at 9140316
    if i32_load(9140316) != 0:
        # Compare with object's offset 28
        if i32_load(9140320) != i32_load(var0 + 28):
            return

    # Call func28 with boolean flag
    flag = 1 if var1 != 0 else 0
    func28(flag, 1)


# ============================================================================
# func291: Entity position update or callback
# ============================================================================

def func291(var0: int, var1: int, var2: int, var3: int) -> None:
    """
    $func291: Update entity position or dispatch to callback.

    If offset 125 byte is 1, calls func63.
    Otherwise, updates position data at global table.

    Args:
        var0: Entity pointer
        var1, var2, var3: Position/parameters
    """
    from tzar.unknown.func63 import func63

    if i32_load8_u(var0 + 125) == 1:
        func63(var0, var1, var2, var3)
        return

    # Calculate table offset
    table_base = i32_load(9215884)
    entity_slot = i32_load(var0 + 44) * 16

    # Calculate terrain position
    terrain_base = i32_load(9142848)
    terrain_offset = var3 // 25

    # Store result
    i32_store(table_base + entity_slot, terrain_base + terrain_offset)


# ============================================================================
# Aliases
# ============================================================================

set_string_length = func312
ref_count_dec = func307
cleanup_and_free = func306
alloc_and_store = func314
conditional_callback = func294
entity_position_update = func291
