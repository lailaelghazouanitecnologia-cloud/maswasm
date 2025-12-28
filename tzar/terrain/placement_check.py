"""
Function: $func73
Name: placement_check
Category: terrain
Depth: 0
Status: done

Calls: none
Called by: 5 functions ($func350, $func87, $func317, $func142, $func56)

Check if a rectangular area is valid for placement (buildings/units).
Validates against collision grid and ownership data.

Structure at $var2 (entity/building definition):
- offset 208: width (stride)
- offset 212: owner ID
- offset 216: height
- offset 220: offset delta
- offset 264: type (1 = special case)
- offset 372: collision mask data

Global addresses:
- 9142440: map width
- 9142840: terrain/ownership grid

Args:
    $var0: start X position
    $var1: start Y position
    $var2: entity structure pointer
    $var3: (iteration counter, internal)
    $var4: value to store on success
    $var5: check mode flag

Returns:
    0 if collision detected, otherwise returns internal counter
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store

# Global addresses
MAP_WIDTH_ADDR = 9142440
TERRAIN_GRID_ADDR = 9142840


def placement_check(
    start_x: int,
    start_y: int,
    entity_ptr: int,
    counter: int,
    store_value: int,
    check_mode: int
) -> int:
    """
    Check if a rectangular area is valid for placement.

    Iterates through the area defined by the entity's width/height and
    checks for collisions in the terrain grid. Returns 0 if any collision
    is found.

    Args:
        start_x: Starting X coordinate
        start_y: Starting Y coordinate
        entity_ptr: Pointer to entity/building structure
        counter: Internal iteration counter
        store_value: Value to store in grid on success
        check_mode: Mode flag (0 = skip check)

    Returns:
        0 if collision, otherwise internal counter value
    """
    # Early exit if check mode is 0
    if check_mode == 0:
        return counter

    # Load entity dimensions
    height = i32_load(entity_ptr, offset=216)
    width = i32_load(entity_ptr, offset=208)
    collision_mask = i32_load(entity_ptr, offset=372)

    if height <= 0:
        return counter

    y_offset = i32_load(entity_ptr, offset=220)
    end_y = start_y + y_offset
    if end_y <= start_y:
        return counter

    # Get map info
    map_width = i32_load(MAP_WIDTH_ADDR)
    grid_stride = (map_width + 2) * width
    owner_id = i32_load(entity_ptr, offset=212)
    terrain_grid = i32_load(TERRAIN_GRID_ADDR)

    entity_type = i32_load(entity_ptr, offset=264)
    end_x = start_x + height

    # Check each cell in the rectangle
    for x in range(start_x, end_x):
        x_offset = x - start_x
        for y in range(start_y, end_y):
            y_offset_local = y - start_y

            # Check collision mask
            mask_idx = x_offset + y_offset_local * height + collision_mask
            if i32_load8_u(mask_idx):
                if x >= map_width:
                    return 0

                # Type 1 has special handling
                if entity_type != 1:
                    if x < 0 or y < 0:
                        return counter

                    # Check terrain grid
                    grid_idx = terrain_grid + ((y + 1 + grid_stride) * (map_width + 2) + (x + 1)) * 4
                    if i32_load(grid_idx) != owner_id:
                        return counter

                    # Check adjacent cell
                    grid_idx2 = terrain_grid + ((y + 1) * (map_width + 2) + (x + 1)) * 4
                    if i32_load(grid_idx2) != owner_id:
                        return counter

    return counter


# Alias for WASM function name
func73 = placement_check
