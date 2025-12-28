"""
Function: $func72
Name: aggregate_costs
Category: pathfinding
Depth: 0
Status: done

Calls: none
Called by: 9 functions ($func505, $func87, $func66, $func30, $Sb, $oc,
                        $func688, $func911, $fd)

Aggregate pathfinding costs from multiple sources (players/units).

Structure layout (per player, stride = 286704 bytes):
- offset 283848: cost direction 0 (int32)
- offset 283852: cost direction 1 (int32)
- offset 283856: cost direction 2 (int32)
- offset 283860: cost direction 3 (int32)
- offset 283908: visibility/access flags pointer

Global addresses:
- 9142892: player count
- 9561692: base data offset
- 9143016: visibility table offset

2147483647 (INT_MAX) represents infinite/unreachable cost.

Args:
    $var0: Source structure pointer
    $var1: Output costs array (4 x int32)
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store

# Constants
INT_MAX = 2147483647
PLAYER_STRIDE = 286704

# Global addresses
PLAYER_COUNT_ADDR = 9142892
BASE_DATA_ADDR = 9561692
VISIBILITY_TABLE_ADDR = 9143016


def aggregate_costs(source_ptr: int, output_ptr: int) -> None:
    """
    Aggregate pathfinding costs from all players/sources.

    Reads base costs from source_ptr and adds costs from all active players
    based on visibility flags. Writes aggregated costs (4 directions) to output.

    Args:
        source_ptr: Pointer to source cost structure
        output_ptr: Pointer to output array (4 x int32)
    """
    # Read initial costs from source
    cost0 = i32_load(source_ptr, offset=283848)
    cost1 = i32_load(source_ptr, offset=283852)
    cost2 = i32_load(source_ptr, offset=283856)
    cost3 = i32_load(source_ptr, offset=283860)

    # Store initial values
    i32_store(output_ptr, cost0)
    i32_store(output_ptr, cost1, offset=4)
    i32_store(output_ptr, cost2, offset=8)
    i32_store(output_ptr, cost3, offset=12)

    # Get global info
    player_count = i32_load(PLAYER_COUNT_ADDR)

    if player_count < 2:
        return

    base_data = i32_load(BASE_DATA_ADDR)
    vis_table = i32_load(VISIBILITY_TABLE_ADDR)

    # Iterate through players (starting from 1)
    for player_idx in range(1, player_count):
        player_offset = player_idx * PLAYER_STRIDE

        # Get flags pointer
        flags_base = i32_load(source_ptr, offset=283908)
        flag_offset = vis_table + player_idx * player_count + flags_base
        flags = i32_load8_u(flag_offset)

        # Direction 0 (flag bit 0)
        if flags & 1:
            if cost0 != INT_MAX:
                add_cost = i32_load(base_data + player_offset, offset=283848)
                if add_cost != INT_MAX:
                    cost0 = cost0 + add_cost
                else:
                    cost0 = INT_MAX
                i32_store(output_ptr, cost0)

        # Direction 1 (flag bit 1)
        if flags & 2:
            if cost1 != INT_MAX:
                add_cost = i32_load(base_data + player_offset, offset=283852)
                if add_cost != INT_MAX:
                    cost1 = cost1 + add_cost
                else:
                    cost1 = INT_MAX
                i32_store(output_ptr, cost1, offset=4)

        # Direction 2 (flag bit 2)
        if flags & 4:
            if cost2 != INT_MAX:
                add_cost = i32_load(base_data + player_offset, offset=283856)
                if add_cost != INT_MAX:
                    cost2 = cost2 + add_cost
                else:
                    cost2 = INT_MAX
                i32_store(output_ptr, cost2, offset=8)

        # Direction 3 (flag bit 3)
        if flags & 8:
            if cost3 != INT_MAX:
                add_cost = i32_load(base_data + player_offset, offset=283860)
                if add_cost != INT_MAX:
                    cost3 = cost3 + add_cost
                else:
                    cost3 = INT_MAX
                i32_store(output_ptr, cost3, offset=12)


# Alias for WASM function name
func72 = aggregate_costs
