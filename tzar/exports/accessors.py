"""
Simple accessor and state functions - batch 26.

Leaf functions that get/set global state values.
"""

from tzar._runtime import i32_load, i32_load8_u, i32_store, i32_store8


# ============================================================================
# zc: Get game state pointer (leaf, 0 callers)
# ============================================================================

def zc() -> int:
    """
    $zc: Returns constant game state pointer.

    Returns:
        Pointer to game state structure at 9684400
    """
    return 9684400


# ============================================================================
# kc: Get current frame count (leaf, 0 callers)
# ============================================================================

def kc() -> int:
    """
    $kc: Get current frame/tick count.

    Returns:
        Current frame count from global at 51776
    """
    return i32_load(51776)


# ============================================================================
# yc: Set global flag at 9147211 (leaf, 0 callers)
# ============================================================================

def yc(var0: int) -> None:
    """
    $yc: Store byte value to global flag.

    Args:
        var0: Value to store (as byte)
    """
    i32_store8(9147211, var0)


# ============================================================================
# ie: Set selection flag and get entity table (leaf, 0 callers)
# ============================================================================

def ie(var0: int, var1: int, var2: int) -> int:
    """
    $ie: Set selection flag based on var1, return entity table.

    Args:
        var0: Unused parameter
        var1: Flag value (converted to bool)
        var2: Unused parameter

    Returns:
        Entity table pointer from 9215884
    """
    # Store whether var1 is non-zero
    i32_store8(59180, 1 if var1 != 0 else 0)
    return i32_load(9215884)


# ============================================================================
# re: Check if any pending operations (leaf, 0 callers)
# ============================================================================

def re() -> int:
    """
    $re: Check if there are pending operations.

    Checks two memory locations and returns 1 if either is non-zero.

    Returns:
        1 if pending operations, 0 otherwise
    """
    val1 = i32_load(9213820)
    val2 = i32_load(9213808)
    return 1 if (val1 | val2) != 0 else 0


# ============================================================================
# mc: Set ready flags conditionally (leaf, 0 callers)
# ============================================================================

def mc() -> None:
    """
    $mc: Conditionally set ready flags.

    If global flag at 9147210 is set and game state offset 48 is non-zero,
    does nothing. Otherwise sets ready flags at 9684336 and 9215872.
    """
    if i32_load8_u(9147210):
        game_state = i32_load(9142424)
        if i32_load(game_state + 48):
            return  # Early exit - game is busy

    # Set ready flags
    i32_store8(9684336, 1)
    i32_store8(9215872, 1)


# ============================================================================
# gb: Get entity type build time (leaf, 0 callers)
# ============================================================================

def gb(var0: int) -> int:
    """
    $gb: Get build time for entity type.

    Looks up entity type data and returns build time if type is 3.

    Args:
        var0: Entity type index

    Returns:
        Build time in milliseconds, or 0 if not applicable
    """
    type_offset = var0 * 404 + 9568096

    # Check if entity type category is 3 (building?)
    if i32_load(type_offset + 264) == 3:
        return i32_load(type_offset + 116) * 1000
    else:
        return 0


# ============================================================================
# ob: Update rotation direction (leaf, 0 callers)
# ============================================================================

def ob(var0: int, var1: int) -> int:
    """
    $ob: Update rotation direction counter.

    Adds var0 to one of two rotation counters based on var1,
    masked to 0-3 range.

    Args:
        var0: Rotation amount to add
        var1: Direction flag (0 or non-zero)

    Returns:
        New rotation value (0-3)
    """
    if var1:
        # Use counter at 9681816
        new_val = (i32_load(9681816) + var0) & 3
        i32_store(9681816, new_val)
    else:
        # Use counter at 9681820
        new_val = (i32_load(9681820) + var0) & 3
        i32_store(9681820, new_val)

    return new_val


# ============================================================================
# va: Set player value (leaf, 0 callers)
# ============================================================================

def va(var0: int, var1: int) -> None:
    """
    $va: Store value to player-related global.

    Args:
        var0: Value to store
        var1: Unused parameter
    """
    i32_store(9561844, var0)


# ============================================================================
# ta: Get player data pointer (leaf, 0 callers)
# ============================================================================

def ta() -> int:
    """
    $ta: Returns constant player data pointer.

    Returns:
        Pointer to player data structure at 9142960
    """
    return 9142960


# ============================================================================
# sa: Set multiple game state values (leaf, 0 callers)
# ============================================================================

def sa(var0: int, var1: int, var2: int, var3: int, var4: int, var5: int, var6: int) -> None:
    """
    $sa: Initialize multiple game state values.

    Sets various flags and values across different memory locations.

    Args:
        var0: Value for 59168
        var1: Flag byte for 59184
        var2: Flag byte for 59185
        var3: Value for 9561840
        var4: Flag byte for 9142916
        var5: Flag byte for 9142917
        var6: Flag byte for 9142918
    """
    i32_store8(59184, var1)
    i32_store(59168, var0)
    i32_store8(59185, var2)
    i32_store(9561840, var3)
    i32_store8(9142916, var4)
    i32_store8(9142917, var5)
    i32_store8(9142918, var6)


# ============================================================================
# ea: Find player index by ID (leaf, 0 callers)
# ============================================================================

def ea(var0: int) -> int:
    """
    $ea: Find player index matching given ID.

    Iterates through player data to find player with matching ID.

    Args:
        var0: Player ID to find

    Returns:
        Player index (1-based), or 0 if not found
    """
    player_count = i32_load(9142892)

    if player_count < 2:
        return 0

    player_base = i32_load(9561692)

    for i in range(1, player_count):
        player_ptr = player_base + i * 286704
        player_id = i32_load(player_ptr + 284616)
        if player_id == var0:
            return i

    return 0


# ============================================================================
# Aliases
# ============================================================================

get_game_state_ptr = zc
get_frame_count = kc
set_global_flag = yc
set_selection_get_table = ie
has_pending_operations = re
set_ready_flags = mc
get_build_time = gb
update_rotation = ob
set_player_value = va
get_player_data_ptr = ta
init_game_state = sa
find_player_by_id = ea
