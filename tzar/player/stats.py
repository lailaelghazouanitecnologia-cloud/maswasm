"""
Function: $func72
Name: aggregate_player_stats
Category: player
Depth: 0
Status: done

Calls: none
Called by: 9 functions ($func505, $func87, $func66, $func30, $Sb, etc.)

Aggregates player statistics from player data structure.
Copies values to output array with accumulation across player types.

Player structure offsets (stride 286704):
- 283848: base accumulator
- 283852+: stat values (indexed by player type)
- 283860+: type-specific stats

Output array:
- offset 0: base accumulator
- offset 4: stat 1
- offset 8: stat 2
- offset 12: stat 3 (with INT_MAX check)
"""

from tzar._runtime import i32_load, i32_store


# Maximum value sentinel
INT_MAX = 2147483647


def aggregate_player_stats(player_ptr: int, output: int) -> None:
    """
    Aggregate player statistics into output array.

    Args:
        player_ptr: Pointer to player data structure
        output: Pointer to output array (4 integers)
    """
    # Copy base accumulator
    base = i32_load(player_ptr + 283848)
    i32_store(output, base)

    # Copy second stat
    stat1 = i32_load(player_ptr + 283852)
    i32_store(output + 4, stat1)

    # Load type count and iterate
    type_count = i32_load(player_ptr + 283856)
    i32_store(output + 8, 0)  # Initialize stat2

    # Aggregate across player types
    stat2 = 0
    stat3 = 0

    for i in range(type_count):
        # Each player type entry is 8 bytes
        type_offset = 283860 + i * 8
        value = i32_load(player_ptr + type_offset)
        stat2 += value

        # Check for special stat with INT_MAX handling
        special = i32_load(player_ptr + type_offset + 4)
        if special != INT_MAX:
            stat3 += special

    i32_store(output + 8, stat2)
    i32_store(output + 12, stat3)


# Alias
func72 = aggregate_player_stats
