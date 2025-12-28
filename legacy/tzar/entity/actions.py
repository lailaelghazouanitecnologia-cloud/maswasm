"""
Entity action and animation functions - batch 22.

High-impact functions related to entity movement, animation, and actions.
These are called by 5-14 other functions each.
"""

from tzar._runtime import (
    i32_load, i32_load8_u, i32_load16_u, i32_store,
    f32_const
)


# ============================================================================
# func62: Entity animation/action dispatcher (14 callers)
# ============================================================================

def func62(var0: int, var1: int, var2: int, var3: int) -> None:
    """
    $func62: Dispatch entity animation or action.

    Compares current animation state with requested state and dispatches
    to appropriate handler (func37 for movement, func63 for actions, func29 for state).

    Args:
        var0: Entity pointer
        var1: Target animation/action ID
        var2: Parameter value
        var3: Mode flag
    """
    from tzar.unknown.func37 import func37
    from tzar.unknown.func63 import func63
    from tzar.unknown.func29 import func29

    var4 = i32_load16_u(var0 + 114)  # Current animation frame
    var5 = i32_load16_u(var0 + 112)  # Current animation ID

    # Check if already in requested state
    if var5 == var1 and var2 <= var4 and var2 >= var4:
        # Same state, check if we need to do anything
        if var2 != var4:
            return
        # In exact state, potentially early return
        if var3:
            return

    # Different state or need transition
    if var5 != var1 or var2 > var4:
        # Need to change animation
        entity_type = i32_load8_u(var0 + 122)
        type_offset = entity_type * 404 + 9568096

        # Get animation parameters
        anim_ptr = i32_load(type_offset + 276)
        anim_value = 25 if anim_ptr else anim_ptr

        # Call movement handler
        func37(var0, var1, f32_const(float(var2)), 0)

        if var3:
            return

        # Dispatch action
        func63(var0, 10, 0, anim_value)
        return

    # Fallback - update state
    func29(var0, 1)


# ============================================================================
# func86: Entity animation lookup (5 callers)
# ============================================================================

def func86(var0: int) -> None:
    """
    $func86: Look up and apply entity animation based on type.

    Uses entity type (offset 122) to look up animation parameters
    and calls func37 for movement.

    Args:
        var0: Entity pointer
    """
    from tzar.unknown.func37 import func37

    var1 = i32_load8_u(var0 + 122)  # Entity type
    var2 = 0  # Animation pointer
    var3 = f32_const(-1.0)  # Default parameter

    # Check if entity has animation state
    if i32_load16_u(var0 + 108) != 0:
        # Type-based animation selection using br_table logic
        # Types 64-79 and type 10 have special handling
        if var1 >= 64 and var1 < 80:
            # Special type range
            pass
        elif var1 == 10:
            # Type 10 special case
            pass
        else:
            # Default type lookup
            type_offset = var1 * 404 + 9568096
            var2 = i32_load(type_offset + 276)

    # Check against special entity slots
    slot1 = i32_load(38472)
    slot2 = i32_load(38600)

    if var1 != slot1 and var1 != slot2:
        # Apply animation
        anim_target = i32_load(var2) if var2 else 0
        func37(var0, anim_target, var3, 0)


# ============================================================================
# func119: Entity reset/cleanup (6 callers)
# ============================================================================

def func119(var0: int, var1: int, var2: int) -> None:
    """
    $func119: Reset entity state and animations.

    Clears entity slot assignments, resets position, and applies default animation.

    Args:
        var0: Entity pointer
        var1: Reset mode
        var2: Additional parameter
    """
    from tzar.unknown.func86 import func86
    from tzar.unknown.func92 import func92
    from tzar.unknown.func60 import func60
    from tzar.unknown.func160 import func160

    # Get entity slot from global table
    table_base = i32_load(9215884)
    entity_slot = i32_load(var0 + 44)
    slot_ptr = table_base + entity_slot * 16

    # Get animation data
    anim_idx = i32_load(slot_ptr + 4)
    anim_ptr = anim_idx * 40 + 9671200
    anim_state = i32_load(anim_ptr + 32)

    if anim_state:
        # Get entity from global entity table
        entity_base = i32_load(9671128)
        entity_id = i32_load(var0 + 28)
        entity_ptr = entity_base + entity_id * 132

        # Apply animation based on mode
        if var1:
            func86(var0)
        else:
            func160(entity_ptr)

    # Clear slot assignment
    slot_id = i32_load(var0 + 44)
    if slot_id:
        slot_table = i32_load(9215884)
        i32_store(slot_table + slot_id * 16, 0)

    i32_store(var0 + 44, 0)

    # Reset position and animation
    func92(var0, f32_const(0.0), f32_const(0.0))
    func60(var0, f32_const(1.0))


# ============================================================================
# Aliases
# ============================================================================

entity_anim_dispatch = func62
entity_anim_lookup = func86
entity_reset = func119
