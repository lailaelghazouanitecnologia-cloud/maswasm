"""
Function: $func180
Name: get_resource_total
Category: player
Depth: 0
Status: done

Calls: none
Called by: 4 functions ($func133, $func53, $Pd, $func46)

Gets total resources for a player, handling special player types.
Checks against special player indices at 38604, 38608, 38612.

Player data offsets:
- 281676-281804: resource types (32 values * 4 bytes)
- 281808-282824: resource modifiers
- 282828-283844: resource storage
"""

from tzar._runtime import i32_load


# Special player indices
SPECIAL_PLAYERS = [38604, 38608, 38612]


def get_resource_total(player_ptr: int, resource_type: int) -> int:
    """
    Get total resources of a type for a player.

    Args:
        player_ptr: Pointer to player data
        resource_type: Resource type index

    Returns:
        Total resource amount
    """
    # Check if this is a special player type
    for addr in SPECIAL_PLAYERS:
        if i32_load(addr) == resource_type:
            # Use alternate calculation path
            # Sum across all resource slots
            total = 0
            for i in range(32):
                offset = i * 4
                base = i32_load(player_ptr + 281676 + offset)
                modifier = i32_load(player_ptr + 281808 + offset)
                storage = i32_load(player_ptr + 282828 + offset)
                total += base + modifier + storage
            return total

    # Standard calculation
    offset = resource_type * 4
    base = i32_load(player_ptr + 281808 + offset)
    storage = i32_load(player_ptr + 282828 + offset)
    return base + storage


# Alias
func180 = get_resource_total
