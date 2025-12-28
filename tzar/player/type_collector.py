"""
Function: $Bb
Name: collect_active_player_types
Category: player
Depth: 0
Status: done

Calls: none
Called by: none (export/entry point)

Collects active player type pointers into an array at 9147392.
Iterates through player's unit types and adds ones that are active
(have non-zero count and are enabled).

Player types array: 9568096 (stride 404 bytes per type)
Output array: 9147392
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store


# Player types base address
PLAYER_TYPES_BASE = 9568096

# Player type stride
PLAYER_TYPE_STRIDE = 404

# Output array for active types
ACTIVE_TYPES_ARRAY = 9147392

# Player-specific flags base
PLAYER_FLAGS_BASE = 9216080


def Bb(player_index: int) -> None:
    """
    Collect active player types into the active types array.

    Iterates through a player's unit types, checks if each is active
    (count > 0 and enabled), and adds the pointer to the output array.
    Terminates the array with -1.

    Args:
        player_index: Index of the player to collect types for
    """
    # Get player type struct
    player_type = PLAYER_TYPES_BASE + player_index * PLAYER_TYPE_STRIDE

    # Get count of types for this player
    type_count = i32_load(player_type + 236)

    if type_count == 0:
        # No types - just write terminator
        i32_store(ACTIVE_TYPES_ARRAY, -1)
        return

    output_index = 0
    current_type = player_type

    # Iterate through types
    for i in range(type_count):
        if type_count <= 1:
            # Single type - just check enabled flag
            enabled = i32_load8_u(PLAYER_FLAGS_BASE + player_index * 24 + 23)
            if enabled:
                i32_store(ACTIVE_TYPES_ARRAY + output_index * 4, current_type)
                output_index += 1
        else:
            # Multiple types - check count at offset 236
            count = i32_load(current_type + 236)
            if count > 0:
                enabled = i32_load8_u(PLAYER_FLAGS_BASE + player_index * 24 + 23)
                if enabled:
                    i32_store(ACTIVE_TYPES_ARRAY + output_index * 4, current_type)
                    output_index += 1

        current_type += PLAYER_TYPE_STRIDE

    # Terminate array with -1
    i32_store(ACTIVE_TYPES_ARRAY + output_index * 4, -1)


# Alias
func_Bb = Bb
