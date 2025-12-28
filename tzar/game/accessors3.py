"""
Game state accessor functions - part 3.

More simple getters and setters (H, I series).

Global addresses:
- 9142424: Game state pointer
- 9142848: Resource/terrain data
- 9147212: Game flags
- 9147220: Timer/counter
- 9568096: Player types base (stride 404)
- 38528, 38768: Special player indices
"""

from tzar._runtime import i32_load, i32_load8_u


# ============================================================================
# H-Series Getters
# ============================================================================

def H() -> int:
    """
    $H: Get resource/terrain data from 9142848.
    """
    return i32_load(9142848)


def Hb() -> int:
    """
    $Hb: Get value from game state + offset 24.
    Dereferences pointer at 9142424, then loads offset 24.
    """
    state_ptr = i32_load(9142424)
    return i32_load(state_ptr + 24)


def Hc() -> int:
    """
    $Hc (also exported as Pe): Get value from game state + offset 48.
    Dereferences pointer at 9142424, then loads offset 48.
    """
    state_ptr = i32_load(9142424)
    return i32_load(state_ptr + 48)


# Alias for Pe export
Pe = Hc


def He() -> int:
    """
    $He: Get timer/counter value at 9147220.
    """
    return i32_load(9147220)


# ============================================================================
# I-Series Functions
# ============================================================================

def I() -> int:
    """
    $I: Return constant 356.
    Likely a struct size or offset constant.
    """
    return 356


def Ia() -> int:
    """
    $Ia: Count inactive players.

    Iterates through players (stride 286704) and counts those
    with 0 at offset 284616 (active flag).

    Returns:
        Number of inactive players
    """
    # Check game flags
    if i32_load8_u(9147212):
        return 0

    player_count = i32_load(41092)
    if player_count < 2:
        return 0

    player_base = i32_load(41096)  # Player data base
    count = 0

    for i in range(1, player_count):
        player_ptr = player_base + i * 286704
        if i32_load(player_ptr + 284616) == 0:
            count += 1

    return count


def Ib(check_a: int, check_b: int, player_idx: int) -> int:
    """
    $Ib: Get player type value with validation.

    Checks if player type matches criteria, then returns value.

    Args:
        check_a: Value to match against offset 196
        check_b: Value to match against offset 264
        player_idx: Player type index

    Returns:
        Value at offset 84 if criteria match, else 0
    """
    player_type = 9568096 + player_idx * 404

    # Check criteria at offset 196 and 264
    if i32_load(player_type + 196) != check_a:
        return 0
    if i32_load(player_type + 264) != check_b:
        return 0

    # Additional validation checks
    if i32_load8_u(player_type + 332):
        # Check against special player indices
        special1 = i32_load(38528)
        special2 = i32_load(38768)
        if player_idx != special1 and player_idx != special2:
            return 0

    # Check disabled flag
    if i32_load8_u(player_type + 378):
        return 0

    # Return the value at offset 84
    return i32_load(9568096 + player_idx * 404 + 84)


# ============================================================================
# Aliases
# ============================================================================

func_H = H
func_Hb = Hb
func_Hc = Hc
func_He = He
func_I = I
func_Ia = Ia
func_Ib = Ib
