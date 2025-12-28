"""
Game state accessor functions - part 5.

M-Z series simple getters and setters.
17 functions, all <=20 lines.

Global addresses:
- 9142440: Map width
- 9142872: Current view player
- 9147213: Game state flag
- 9561692: Player data base
- 9561856: Player names array
- 9685864: Selection state
- 9687216: UI counter
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store


# Player data stride
PLAYER_STRIDE = 286704


# ============================================================================
# M-Series Functions
# ============================================================================

def Me() -> int:
    """$Me: Get UI counter at 9687216."""
    return i32_load(9687216)


# ============================================================================
# N-Series Functions
# ============================================================================

def Na() -> int:
    """$Na: Return player names array address (9561856)."""
    return 9561856


# ============================================================================
# O-Series Functions
# ============================================================================

def O(player_idx: int) -> int:
    """
    $O (also exported as Ob): Get player data pointer.

    Args:
        player_idx: Player index

    Returns:
        Pointer to player data structure
    """
    player_base = i32_load(9561692)
    return player_base + player_idx * PLAYER_STRIDE


# Alias for Ob export
Ob = O


def Oa(var0: int, var1: int) -> None:
    """$Oa (also Kd, Ld): No-op function."""
    pass


# Aliases for alternate exports
Kd = Oa
Ld = Oa


def Oe() -> int:
    """$Oe: Get map width at 9142440."""
    return i32_load(9142440)


# ============================================================================
# P-Series Functions
# ============================================================================

def Pa() -> int:
    """$Pa: Get game state flag byte at 9147213."""
    return i32_load8_u(9147213)


def Pb() -> int:
    """$Pb: Get current view player index at 9142872."""
    return i32_load(9142872)


# ============================================================================
# Q-Series Functions
# ============================================================================

def Qb(player_idx: int) -> None:
    """$Qb: Set current view player index."""
    i32_store(9142872, player_idx)


def Qe(mode: int) -> None:
    """$Qe: Set game mode at offset 48 of game state (masked to 0-3)."""
    state_ptr = i32_load(9142424)
    i32_store(state_ptr + 48, mode & 3)


# ============================================================================
# R-Series Functions
# ============================================================================

def Ra(player_idx: int) -> int:
    """$Ra: Get player team/alliance value at offset 283964."""
    player_base = i32_load(9561692)
    return i32_load(player_base + player_idx * PLAYER_STRIDE + 283964)


# ============================================================================
# T-Series Functions
# ============================================================================

def Ta() -> int:
    """$Ta: Return constant 255 (max player count or color)."""
    return 255


# ============================================================================
# V-Series Functions
# ============================================================================

def V(player_idx: int, value: int, slot: int) -> None:
    """$V: Set player resource/stat value at offset 283848 + slot*4."""
    player_base = i32_load(9561692)
    offset = player_idx * PLAYER_STRIDE + 283848 + slot * 4
    i32_store(player_base + offset, value)


def Vd() -> int:
    """$Vd: Get selection data at 9685864."""
    return i32_load(9685864)


# ============================================================================
# W-Series Functions
# ============================================================================

def Wa(entity_id: int, mode: int, param: float) -> None:
    """$Wa: Set entity action parameters."""
    from tzar._runtime import i32_store8, f32_store
    i32_store8(9143020, mode)
    i32_store(9671160, entity_id)
    f32_store(42160, param)


# ============================================================================
# X-Series Functions
# ============================================================================

def X(value: int) -> int:
    """$X: Check if value matches current player's control flag."""
    if value == 0:
        return 0
    player_base = i32_load(9561692)
    view_player = i32_load(9142872)
    player_ctrl = i32_load(player_base + view_player * PLAYER_STRIDE + 284608)
    return 1 if player_ctrl == value else 0


def Xa(pos_x: int, pos_y: int) -> None:
    """$Xa: Set selection/cursor position."""
    i32_store(9142952, pos_x)
    i32_store(9142956, pos_y)


# ============================================================================
# Aliases
# ============================================================================

func_Me = Me
func_Na = Na
func_O = O
func_Oa = Oa
func_Oe = Oe
func_Pa = Pa
func_Pb = Pb
func_Qb = Qb
func_Qe = Qe
func_Ra = Ra
func_Ta = Ta
func_V = V
func_Vd = Vd
func_Wa = Wa
func_X = X
func_Xa = Xa
