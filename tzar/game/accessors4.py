"""
Game state accessor functions - part 4.

J, K, L series getters and setters.

Global addresses:
- 41092: Player count
- 9142892: Current player count/index
- 9142912: Game state counter
- 9561692: Player data base
- 9681976: Selection count
- 9684804, 9684808: Camera/view position
- 9687224: UI state
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store


# Player data stride
PLAYER_STRIDE = 286704


# ============================================================================
# J-Series Functions
# ============================================================================

def Ja() -> int:
    """
    $Ja: Get max player index (player count - 1).
    """
    return i32_load(41092) - 1


def Jc() -> int:
    """
    $Jc: Get current player count/index at 9142892.
    """
    return i32_load(9142892)


def Jd(x: int, y: int) -> None:
    """
    $Jd: Set camera/view position.
    Stores X at 9684804, Y at 9684808.
    """
    i32_store(9684804, x)
    i32_store(9684808, y)


def Je(player_idx: int) -> int:
    """
    $Je: Get player color as RGB value.

    Reads 3 bytes from player data and combines into RGB.
    Bytes at offsets 283972, 283973, 283974.

    Args:
        player_idx: Player index

    Returns:
        RGB color value (R << 16 | G << 8 | B)
    """
    player_base = i32_load(9561692)
    player_ptr = player_base + player_idx * PLAYER_STRIDE

    r = i32_load8_u(player_ptr + 283972)
    g = i32_load8_u(player_ptr + 283973)
    b = i32_load8_u(player_ptr + 283974)

    return (r << 16) | (g << 8) | b


# ============================================================================
# K-Series Functions
# ============================================================================

def Ke() -> int:
    """
    $Ke: Get selection count at 9681976.
    """
    return i32_load(9681976)


# ============================================================================
# L-Series Functions
# ============================================================================

def Lb() -> int:
    """
    $Lb: Get game state counter at 9142912.
    """
    return i32_load(9142912)


def Le() -> int:
    """
    $Le: Get UI state at 9687224.
    """
    return i32_load(9687224)


# ============================================================================
# Aliases
# ============================================================================

func_Ja = Ja
func_Jc = Jc
func_Jd = Jd
func_Je = Je
func_Ke = Ke
func_Lb = Lb
func_Le = Le
