"""
Function: $func159
Name: is_selection_unique
Category: entity
Depth: 0
Status: done

Calls: none
Called by: 4 functions ($func330, $func326, $func328, $func331)

Checks if an entity's group ID is unique across all selection groups.
Searches 4 selection lists at addresses 9215928, 9215932, 9215936, 9215940.

Returns 1 if the entity is NOT in any selection, 0 if found.

Entity structure:
- offset 28: group ID

Selection list structure:
- offset 0: array pointer
- offset 8: count
"""

from tzar._runtime import i32_load, i32_load16_u


# Selection list addresses
SELECTION_LISTS = [9215928, 9215932, 9215936, 9215940]

# Entity array base
ENTITY_ARRAY_ADDR = 9671128

# Entity size
ENTITY_SIZE = 132


def is_selection_unique(entity_ptr: int) -> int:
    """
    Check if entity's group is unique across all selections.

    Args:
        entity_ptr: Pointer to entity structure

    Returns:
        1 if not found in any selection, 0 if found
    """
    group_id = i32_load(entity_ptr, offset=28)
    entity_array = i32_load(ENTITY_ARRAY_ADDR)

    for list_addr in SELECTION_LISTS:
        selection = i32_load(list_addr)
        if selection == 0:
            continue

        count = i32_load(selection, offset=8)
        if count == 0:
            continue

        array_ptr = i32_load(selection)

        for i in range(count):
            entity_idx = i32_load(array_ptr + i * 4)
            entity = entity_array + entity_idx * ENTITY_SIZE
            if i32_load(entity, offset=28) == group_id:
                return 0  # Found in selection

    return 1  # Not found


# Alias for WASM function name
func159 = is_selection_unique
