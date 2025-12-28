"""
Game state accessor functions - part 6.

Lowercase letter series and underscore functions.
Simple getters and setters (<=30 lines each).
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store


PLAYER_STRIDE = 286704


# ============================================================================
# P Function (uppercase P that wasn't in accessors5)
# ============================================================================

def P() -> int:
    """
    $P: Calculate screen offset from player position.
    Returns: map_width * player_y + player_x
    """
    map_width = i32_load(9142440)
    player_base = i32_load(9561692)
    view_player = i32_load(9142872)
    player_ptr = player_base + view_player * PLAYER_STRIDE
    y_pos = i32_load(player_ptr + 283876)
    x_pos = i32_load(player_ptr + 283872)
    return map_width * y_pos + x_pos


# ============================================================================
# Underscore Functions
# ============================================================================

def _a() -> int:
    """$_a: Get value at 9681472."""
    return i32_load(9681472)


def _d() -> int:
    """$_d: Get byte at 9142388."""
    return i32_load8_u(9142388)


# ============================================================================
# Lowercase 'a' Series
# ============================================================================

def aa() -> int:
    """$aa: Get entity state at 9681968."""
    return i32_load(9681968)


def ab() -> int:
    """$ab: Get entity data at 9681972."""
    return i32_load(9681972)


def ad() -> int:
    """$ad: Get compound value from entity data."""
    v1 = i32_load(9681976)
    v2 = i32_load(9681980)
    return (v1 << 16) | (v2 & 0xFFFF)


# ============================================================================
# Lowercase 'b' Series
# ============================================================================

def ba() -> int:
    """$ba: Get selection array at 9681484."""
    return i32_load(9681484)


def bb() -> int:
    """$bb: Return constant 9681488 (selection buffer address)."""
    return 9681488


def bc(value: int) -> None:
    """$bc: Set value at 9682196."""
    i32_store(9682196, value)


# ============================================================================
# Lowercase 'c' Series
# ============================================================================

def cf() -> int:
    """$cf: Return constant for buffer address."""
    return i32_load(9682200)


# ============================================================================
# Lowercase 'd' Series
# ============================================================================

def da() -> int:
    """$da: Get entity type info."""
    return i32_load(9671140)


def dc() -> int:
    """$dc: Get entity attribute at 9142960."""
    return i32_load(9142960)


def df() -> int:
    """$df: Get current frame/tick at 9142968."""
    return i32_load(9142968)


# ============================================================================
# Lowercase 'e' Series
# ============================================================================

def eb() -> int:
    """$eb: Get entity action at 9142972."""
    return i32_load(9142972)


def ec() -> int:
    """$ec: Get entity direction at 9142976."""
    return i32_load(9142976)


def ef() -> int:
    """$ef: Return constant 9142984."""
    return 9142984


# ============================================================================
# Lowercase 'f' Series
# ============================================================================

def fa() -> int:
    """$fa: Get entity speed factor."""
    return i32_load(9142988)


# ============================================================================
# Aliases
# ============================================================================

func_P = P
func__a = _a
func__d = _d
func_aa = aa
func_ab = ab
func_ad = ad
func_ba = ba
func_bb = bb
func_bc = bc
func_cf = cf
func_da = da
func_dc = dc
func_df = df
func_eb = eb
func_ec = ec
func_ef = ef
func_fa = fa
