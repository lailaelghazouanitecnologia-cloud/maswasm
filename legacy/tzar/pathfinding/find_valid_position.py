"""
Function: $func167
Name: find_valid_position
Category: pathfinding
Depth: 0
Status: done

Calls: none
Called by: 4 functions ($func690, $func840, $func489, $func786)

Searches for a valid position near a target using expanding spiral.
Checks up to 40 tiles out from center. Uses passability grid.

Key addresses:
- 9142440: map width
- 9142840: passability grid

Args:
    x_ptr: Pointer to x coordinate (input/output)
    y_ptr: Pointer to y coordinate (input/output)
    passability_value: Required passability value
    size: Check size (0 for edge check, >0 for area check)

Returns:
    1 if valid position found within 40 tiles, 0 otherwise
"""

from tzar._runtime import i32_load, i32_store


# Global addresses
MAP_WIDTH = 9142440
PASSABILITY_GRID = 9142840


def find_valid_position(x_ptr: int, y_ptr: int, passability_value: int, size: int) -> int:
    """
    Find a valid position near the given coordinates.

    Args:
        x_ptr: Pointer to x coordinate (modified if found)
        y_ptr: Pointer to y coordinate (modified if found)
        passability_value: Value to check in passability grid
        size: Area size to check (0=edge only, >0=area)

    Returns:
        1 if found valid position, 0 if not found within range
    """
    map_width = i32_load(MAP_WIDTH)
    center_x = i32_load(x_ptr)
    center_y = i32_load(y_ptr)

    if size == 0:
        # Simple edge-only check
        for radius in range(40):
            diameter = radius * 2 + 1
            min_x = center_x - radius
            max_x = min_x + diameter - 1
            min_y = center_y - radius
            max_y = min_y + diameter - 1

            for y in range(min_y, min_x + diameter):
                if y >= map_width:
                    continue

                for x in range(min_y, min_y + diameter):
                    # Only check edges
                    if y != min_y and y != max_y:
                        if x != min_x and x != max_x:
                            continue

                    if x >= map_width:
                        continue

                    if x < 0 or y < 0:
                        continue

                    # Found valid position
                    i32_store(x_ptr, x)
                    i32_store(y_ptr, y)
                    return 0  # Early exit found

        return 1  # Searched all 40 radii
    else:
        # Area check with passability grid
        grid = i32_load(PASSABILITY_GRID)
        grid_stride = map_width + 2

        for radius in range(40):
            diameter = radius * 2 + 1
            min_x = center_x - radius
            max_x = min_x + diameter - 1
            min_y = center_y - radius
            max_y = min_y + diameter - 1

            for y in range(min_y, min_x + diameter):
                y_next = y + 1
                if y >= map_width:
                    continue

                is_y_edge = (y == min_y) or (y == max_y)

                for x in range(min_y, min_y + diameter):
                    # Check if on edge
                    is_x_edge = (x == min_x) or (x == max_x)
                    if not (is_y_edge or is_x_edge):
                        continue

                    if x >= map_width or x < 0 or y < 0:
                        continue

                    # Check area passability
                    valid = True
                    base_offset = (x + 1) + (y + 1) * grid_stride

                    for dy in range(size):
                        for dx in range(size):
                            cell = i32_load(grid + (base_offset + (y_next + dy) * grid_stride + dx) * 4)
                            if cell != passability_value:
                                valid = False
                                break
                        if not valid:
                            break

                    if valid:
                        i32_store(x_ptr, x)
                        i32_store(y_ptr, y)
                        return 0

        return 1  # Not found


# Alias for WASM function name
func167 = find_valid_position
