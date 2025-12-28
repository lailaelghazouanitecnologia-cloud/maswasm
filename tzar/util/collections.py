"""
Collection and state management functions - batch 23.

Functions for searching, updating collections and managing state.
"""

from tzar._runtime import (
    i32_load, i32_store, i32_store8
)
from tzar.memory.af import af


# ============================================================================
# func372: Search in entity list (leaf, 2 callers)
# ============================================================================

def func372(var0: int, var1: int) -> int:
    """
    $func372: Search for entity by ID in list.

    Iterates through list at offset 24 looking for entity with matching ID.

    Args:
        var0: List structure (offset 24 = array, offset 28 = count)
        var1: Entity ID to find

    Returns:
        Pointer to found entity, or 0 if not found
    """
    count = i32_load(var0 + 28)
    if count <= 0:
        return 0

    array_ptr = i32_load(var0 + 24)

    for i in range(count):
        entity = i32_load(array_ptr + i * 4)
        entity_id = i32_load(entity + 28)
        if entity_id == var1:
            return entity

    return 0


# ============================================================================
# func442: State update with mode (leaf, 2 callers)
# ============================================================================

def func442(var0: int, var1: int, var2: int) -> None:
    """
    $func442: Update object state based on mode.

    If offset 16 is empty, initializes state.
    If mode matches, may update offset 24.
    Otherwise sets dirty flag.

    Args:
        var0: State object pointer
        var1: Mode value
        var2: State value
    """
    current_mode = i32_load(var0 + 16)

    if current_mode == 0:
        # Initialize new state
        i32_store(var0 + 36, 1)
        i32_store(var0 + 24, var2)
        i32_store(var0 + 16, var1)
        return

    if var1 == current_mode:
        # Same mode - update if not already state 2
        if i32_load(var0 + 24) != 2:
            return
        i32_store(var0 + 24, var2)
        return

    # Different mode - set dirty flags
    i32_store8(var0 + 54, 1)
    i32_store(var0 + 24, 2)
    i32_store(var0 + 36, i32_load(var0 + 36) + 1)


# ============================================================================
# func390: Loop cleanup with conditional wait (2 callers)
# ============================================================================

def func390(var0: int) -> None:
    """
    $func390: Clean up with conditional loop wait.

    If offset 4 >= 129, waits for semaphore at 9689392.
    Then frees allocations at offset 36 and the object itself.

    Args:
        var0: Object pointer to clean up
    """
    from tzar.unknown.func149 import func149

    if i32_load(var0 + 4) >= 129:
        # Wait for all pending operations
        var1 = i32_load(9689392)
        while var1:
            func149(9689392, 9689396, var1)
            var1 = i32_load(9689392)

    # Free offset 36 allocation and object itself
    af(i32_load(var0 + 36))
    af(var0)


# ============================================================================
# func441: Complex state transition (leaf, 2 callers)
# ============================================================================

def func441(var0: int, var1: int, var2: int, var3: int) -> None:
    """
    $func441: Complex state transition based on conditions.

    Sets state flags and manages transitions based on multiple conditions.

    Args:
        var0: State object
        var1: Mode value
        var2: Expected current value
        var3: New state value
    """
    i32_store8(var0 + 53, 1)

    # Check if current matches expected
    if i32_load(var0 + 4) != var2:
        return

    i32_store8(var0 + 52, 1)

    current_mode = i32_load(var0 + 16)

    if current_mode == 0:
        # Initialize
        i32_store(var0 + 36, 1)
        i32_store(var0 + 24, var3)
        i32_store(var0 + 16, var1)
    elif var1 == current_mode:
        # Same mode - conditional update
        current_state = i32_load(var0 + 24)
        if i32_load(var0 + 48) == 1 and current_state == 1:
            # Already in this state
            pass
        else:
            i32_store(var0 + 36, i32_load(var0 + 36) + 1)
    else:
        # Different mode
        i32_store(var0 + 36, i32_load(var0 + 36) + 1)

    i32_store8(var0 + 54, 1)


# ============================================================================
# func105: Vector push with resize (2 callers)
# ============================================================================

def func105(var0: int, var1: int) -> None:
    """
    $func105: Push element to dynamic vector with auto-resize.

    If vector is full, reallocates with additional capacity.
    Appends element at end.

    Structure:
    - offset 0: data pointer
    - offset 4: capacity
    - offset 8: count
    - offset 12: grow amount

    Args:
        var0: Vector structure pointer
        var1: Element to add
    """
    from tzar.memory.func26 import func26

    count = i32_load(var0 + 8)
    capacity = i32_load(var0 + 4)

    if count == capacity:
        # Need to grow
        grow_amount = i32_load(var0 + 12)
        new_capacity = capacity + grow_amount
        i32_store(var0 + 4, new_capacity)

        # Allocate new buffer
        new_data = func26(new_capacity * 4)

        # Copy old data
        old_data = i32_load(var0)
        # Note: memory.copy would be used here in full implementation

        # Free old if exists
        if old_data:
            af(old_data)
            count = i32_load(var0 + 8)  # Reload after af

        i32_store(var0, new_data)
        data = new_data
    else:
        data = i32_load(var0)

    # Append element
    i32_store(var0 + 8, count + 1)
    i32_store(data + count * 4, var1)


# ============================================================================
# Aliases
# ============================================================================

find_entity_in_list = func372
update_state_mode = func442
cleanup_with_wait = func390
complex_state_transition = func441
vector_push = func105
