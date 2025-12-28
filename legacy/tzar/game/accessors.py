"""
Game state accessor functions - simple getters and setters.

These are exported functions that provide access to game state.
Most are very simple - just reading/writing to fixed memory addresses.

Global addresses:
- 9147336: game mode byte
- 9163776: map data pointer
- 9163780: player count
- 9563904: current player struct
- 9563944: current player index
- 9568088: active player pointer
"""

from tzar._runtime import i32_load, i32_store, i32_store8


# ============================================================================
# Simple Getters - return values from fixed addresses
# ============================================================================

def Cc() -> int:
    """
    $Cc: Get player count.
    Returns value at address 9163780.
    """
    return i32_load(9163780)


def Dc() -> int:
    """
    $Dc: Get map data pointer.
    Returns value at address 9163776.
    """
    return i32_load(9163776)


def Da() -> int:
    """
    $Da: Get constant 41104.
    Returns the constant value 41104 (likely a struct size or offset).
    """
    return 41104


# ============================================================================
# Simple Setters - store values at fixed/computed addresses
# ============================================================================

def E(value: int) -> None:
    """
    $E: Set game mode byte.
    Stores byte value at address 9147336.
    """
    i32_store8(9147336, value)


def Db(player_index: int) -> int:
    """
    $Db: Set current player index and return player struct address.
    Stores player_index at 9563944, returns 9563904.
    """
    i32_store(9563944, player_index)
    return 9563904


# ============================================================================
# Player Structure Setters - store to player struct with offset
# ============================================================================

def Bd(index: int, value: int) -> None:
    """
    $Bd: Set value in player struct at offset 80 + index*4.
    Uses active player from 9568088.

    Player struct offset 80 appears to be an indexed array.
    """
    player_ptr = i32_load(9568088)
    array_base = i32_load(player_ptr + 80)
    i32_store(array_base + index * 4, value)


def Dd(index: int, value: int) -> None:
    """
    $Dd: Set value in player struct at offset 96 + index*4.
    Uses active player from 9568088.

    Player struct offset 96 appears to be another indexed array.
    """
    player_ptr = i32_load(9568088)
    array_base = i32_load(player_ptr + 96)
    i32_store(array_base + index * 4, value)


# ============================================================================
# Aliases for WASM function names
# ============================================================================

# Export all as their original names
func_Cc = Cc
func_Dc = Dc
func_Da = Da
func_E = E
func_Db = Db
func_Bd = Bd
func_Dd = Dd
