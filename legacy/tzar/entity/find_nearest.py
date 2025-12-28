"""
Function: $func166
Name: find_nearest_entity
Category: entity
Depth: 0
Status: done

Calls: none
Called by: 3 functions ($func826, $func824, $func654)

Finds the nearest entity of a given type for a player.
Uses squared distance to avoid sqrt. Searches all 255 player types.

Key addresses:
- 9142432: visibility grid base (optional)
- 9142440: map width
- 9561692: player data base
- 9568096: player type base
- 9671128: entity array

Returns entity group ID (offset 28) or 0 if none found.
"""

from tzar._runtime import i32_load, i32_load8_u, i32_load16_u


# Global addresses
VISIBILITY_GRID = 9142432
MAP_WIDTH = 9142440
PLAYER_DATA_BASE = 9561692
PLAYER_TYPE_BASE = 9568096
ENTITY_ARRAY = 9671128

# Strides
PLAYER_DATA_STRIDE = 286704
PLAYER_TYPE_STRIDE = 404
ENTITY_STRIDE = 132


def find_nearest_entity(x: int, y: int, player_id: int, target_type: int) -> int:
    """
    Find the nearest entity of a type for a player.

    Args:
        x: X coordinate to search from
        y: Y coordinate to search from
        player_id: Player ID to search for
        target_type: Unit type to find (or 4 for any)

    Returns:
        Group ID of nearest entity, or 0 if none found
    """
    vis_grid = i32_load(VISIBILITY_GRID)
    map_width = i32_load(MAP_WIDTH)
    entity_array = i32_load(ENTITY_ARRAY)
    player_data = i32_load(PLAYER_DATA_BASE) + player_id * PLAYER_DATA_STRIDE

    x2 = x * 2
    y2 = y * 2
    best_dist = 0x7FFFFFFF  # Max int
    best_group = 0

    # Check with visibility grid
    if vis_grid != 0:
        grid_cell = i32_load(vis_grid + (y * map_width + x) * 4)

        for player_type_idx in range(255):
            type_ptr = PLAYER_TYPE_BASE + player_type_idx * PLAYER_TYPE_STRIDE
            unit_type = i32_load(type_ptr, offset=192)

            if unit_type != target_type and unit_type != 4:
                continue

            # Get unit list for this player/type
            unit_list_ptr = player_data + player_type_idx * 4 + 284636
            unit_list = i32_load(unit_list_ptr)
            if unit_list == 0:
                continue

            unit_count = i32_load(unit_list, offset=8)
            if unit_count == 0:
                continue

            unit_array = i32_load(unit_list)

            for i in range(unit_count):
                entity_idx = i32_load(unit_array + i * 4)
                if entity_idx == 0:
                    continue

                entity = entity_array + entity_idx * ENTITY_STRIDE
                ey = i32_load16_u(entity, offset=114)
                ex = i32_load16_u(entity, offset=112)

                # Squared distance
                dx = x2 - (i32_load(type_ptr, offset=216) + ex * 2)
                dy = y2 - (i32_load(type_ptr, offset=220) + ey * 2)
                dist = dx * dx + dy * dy

                if dist >= best_dist:
                    continue

                # Check visibility grid match
                owner = i32_load8_u(entity, offset=122)
                owner_type = PLAYER_TYPE_BASE + owner * PLAYER_TYPE_STRIDE
                cell_x = ex + (i32_load(owner_type, offset=216) >> 1)
                cell_y = ey + (i32_load(owner_type, offset=220) >> 1)
                cell_idx = cell_x + cell_y * map_width
                if i32_load(vis_grid + cell_idx * 4) != grid_cell:
                    continue

                # Check owner matches
                if i32_load16_u(entity, offset=110) != player_id:
                    continue

                # Check state (5-13 valid, not 14)
                state = i32_load8_u(entity, offset=125)
                if state < 5 or state > 13 or state == 14:
                    continue

                best_group = i32_load(entity, offset=28)
                best_dist = dist
    else:
        # No visibility grid - simpler search
        for player_type_idx in range(255):
            type_ptr = PLAYER_TYPE_BASE + player_type_idx * PLAYER_TYPE_STRIDE
            unit_type = i32_load(type_ptr, offset=192)

            if unit_type != target_type and unit_type != 4:
                continue

            unit_list_ptr = player_data + player_type_idx * 4 + 284636
            unit_list = i32_load(unit_list_ptr)
            if unit_list == 0:
                continue

            unit_count = i32_load(unit_list, offset=8)
            if unit_count == 0:
                continue

            unit_array = i32_load(unit_list)

            for i in range(unit_count):
                entity_idx = i32_load(unit_array + i * 4)
                if entity_idx == 0:
                    continue

                entity = entity_array + entity_idx * ENTITY_STRIDE
                ey = i32_load16_u(entity, offset=114)
                ex = i32_load16_u(entity, offset=112)

                dx = x2 - (i32_load(type_ptr, offset=216) + ex * 2)
                dy = y2 - (i32_load(type_ptr, offset=220) + ey * 2)
                dist = dx * dx + dy * dy

                if dist >= best_dist:
                    continue

                if i32_load16_u(entity, offset=110) != player_id:
                    continue

                state = i32_load8_u(entity, offset=125)
                if state < 5 or state > 13 or state == 14:
                    continue

                best_group = i32_load(entity, offset=28)
                best_dist = dist

    return best_group


# Alias for WASM function name
func166 = find_nearest_entity
