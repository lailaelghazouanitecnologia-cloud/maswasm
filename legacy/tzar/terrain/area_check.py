"""
Function: $func108
Name: check_square_area
Category: terrain
Depth: 0
Status: done

Calls: none
Called by: 3 functions ($func142, $func87, $func461)

Checks if a square area is clear/passable on the map.
Uses edge-only checking for efficiency (perimeter of square).

Args:
    x, y: Center coordinates
    map_ptr: Pointer to map data
    radius: Check radius (creates (2*r+1)^2 - 2 perimeter cells)

Returns 1 if area is clear, 0 if blocked.
"""

from tzar._runtime import i32_load, i32_load8_u


def check_square_area(x: int, y: int, map_ptr: int, radius: int) -> int:
    """
    Check if square area perimeter is clear.

    Args:
        x: Center X coordinate
        y: Center Y coordinate
        map_ptr: Map data pointer
        radius: Radius of square to check

    Returns:
        1 if clear, 0 if blocked
    """
    # Calculate diameter and perimeter size
    diameter = radius * 2 + 1
    perimeter = diameter * diameter * 2 - 2

    if perimeter == 0:
        return 1

    # Get map dimensions
    map_width = i32_load(map_ptr, offset=4)
    map_data = i32_load(map_ptr)

    # Check perimeter cells (step by 2 for efficiency)
    for i in range(0, perimeter, 2):
        # Calculate cell coordinates from perimeter index
        cell_x = x + (i % diameter) - radius
        cell_y = y + (i // diameter) - radius

        # Bounds check
        if cell_x < 0 or cell_y < 0:
            continue
        if cell_x >= map_width or cell_y >= map_width:
            continue

        # Check if cell is blocked
        cell_offset = cell_y * map_width + cell_x
        if i32_load8_u(map_data + cell_offset) != 0:
            return 0

    return 1


# Alias
func108 = check_square_area
