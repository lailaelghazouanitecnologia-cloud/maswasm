"""
Function: $func88
Name: calculate_score
Category: player
Depth: 0
Status: done

Calls: none
Called by: 5 functions ($Rb, $func346, $func361, $func849, $func688)

Calculates a player's game score based on resources, units, buildings.
Uses offsets in player data structure (stride 286704).

Key offsets from player base:
- 281676: resource A
- 281692: resource B
- 283848: value accumulator
- 283956: penalty
- 283976: multiplier flag
- 284616: active flag
- 286696: disabled flag

Score formula: (accumulator + resource_B - penalty + 100000) / 850 + resource_A / 50
"""

from tzar._runtime import i32_load, i32_load8_u


def calculate_score(player_ptr: int) -> int:
    """
    Calculate player's game score.

    Args:
        player_ptr: Pointer to player data structure

    Returns:
        Calculated score (minimum 0)
    """
    # Check if scoring is enabled (global flag at 9216060)
    if i32_load8_u(9216060) == 0:
        return 0

    # Check if player is disabled
    if i32_load8_u(player_ptr, offset=286696):
        return 0

    # Check if player is active
    if i32_load(player_ptr, offset=284616) == 0:
        return 0

    # Check multiplier
    if i32_load(player_ptr, offset=283976) == 0:
        return 0

    # Calculate score components
    accumulator = i32_load(player_ptr, offset=283848)
    resource_b = i32_load(player_ptr + 281692)
    penalty = i32_load(player_ptr, offset=283956)
    resource_a = i32_load(player_ptr + 281676)

    # Score = (accumulator + resource_B - penalty + 100000) / 850 + resource_A / 50
    raw_score = accumulator + resource_b - penalty + 100000
    score = (raw_score // 850) + (resource_a // 50)

    # Return max(0, score)
    return score if score > 0 else 0


# Alias
func88 = calculate_score
