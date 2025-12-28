"""
Game state accessor functions - part 2.

More simple getters and setters for game state.

Global addresses used:
- 9147208: game state byte
- 9147212: another game state byte
- 9147392: active types array pointer (constant)
- 9142440: map width
- 9215892: selection pointer
- 9671136: entity count
- 40616: float parameter storage
"""

from tzar._runtime import i32_load, i32_load8_u, f32_store


# ============================================================================
# Simple Getters
# ============================================================================

def Eb() -> int:
    """
    $Eb: Get game state byte at 9147212.
    """
    return i32_load8_u(9147212)


def Ec() -> int:
    """
    $Ec: Get entity count at 9671136.
    """
    return i32_load(9671136)


def Fc() -> int:
    """
    $Fc: Return constant address 9147392.
    This is the active types array address.
    """
    return 9147392


def Gc(unused1: int, unused2: int) -> int:
    """
    $Gc: Get selection pointer at 9215892.
    Parameters are unused (possibly for API compatibility).
    """
    return i32_load(9215892)


def Ge() -> int:
    """
    $Ge: Get game state byte at 9147208.
    """
    return i32_load8_u(9147208)


# ============================================================================
# Simple Setters
# ============================================================================

def F(value: float) -> None:
    """
    $F: Store float value at address 40616.
    Likely a game parameter (speed, zoom, etc).
    """
    f32_store(40616, value)


# ============================================================================
# Utility Functions
# ============================================================================

def G(x: int, y: int) -> int:
    """
    $G: Check if coordinates are within map bounds.

    Args:
        x: X coordinate
        y: Y coordinate

    Returns:
        1 if valid (within bounds and non-negative), 0 otherwise
    """
    map_width = i32_load(9142440)

    # Check: y < map_width AND x < map_width AND (x|y) >= 0
    y_valid = map_width > y
    x_valid = x < map_width
    non_negative = (x | y) >= 0

    return 1 if (y_valid and x_valid and non_negative) else 0


# ============================================================================
# Aliases
# ============================================================================

func_Eb = Eb
func_Ec = Ec
func_Fc = Fc
func_Gc = Gc
func_Ge = Ge
func_F = F
func_G = G
