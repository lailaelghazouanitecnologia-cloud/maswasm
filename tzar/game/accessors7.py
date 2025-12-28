"""
Game state accessor functions - part 7.

Dollar-prefixed functions and misc.
"""

from tzar._runtime import i32_load, i32_load8_u


PLAYER_STRIDE = 286704


# ============================================================================
# Dollar-prefixed Functions
# ============================================================================

def dollar_b() -> int:
    """
    $$b (exported as "$b"): Get player resource pointer or global.

    Returns pointer to player+283984 if game flag at 9147212 is 0,
    otherwise returns global 9561072.
    """
    flag = i32_load8_u(9147212)
    if flag != 0:
        return 9561072

    player_base = i32_load(9561692)
    view_player = i32_load(9142872)
    return player_base + view_player * PLAYER_STRIDE + 283984


def dollar_d() -> int:
    """
    $$d (exported as "$d"): Get game time/tick value.

    Loads value from game state offset 72, multiplies and divides by 2400.
    This seems to normalize time to frames.
    """
    state_ptr = i32_load(9142424)
    raw_val = i32_load(state_ptr + 72)
    # Note: * 2400 / 2400 = identity, but this might be handling overflow
    return (raw_val * 2400) // 2400


# ============================================================================
# Aliases (using valid Python identifiers)
# ============================================================================

# Export as $b and $d would be invalid Python, so we use these aliases
func_dollar_b = dollar_b
func_dollar_d = dollar_d
