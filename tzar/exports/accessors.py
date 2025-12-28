"""
Simple accessor and state functions - batch 26.

Leaf functions that get/set global state values.
"""

from tzar._runtime import (
    i32_load, i32_load8_u, i32_store, i32_store8,
    i64_load, i64_store, f32_store
)


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
# oa: Get viewport offset (leaf, 0 callers)
# ============================================================================

def oa() -> int:
    """
    $oa: Get viewport offset value + 10.

    Returns:
        Viewport value from 59176 plus 10
    """
    return i32_load(59176) + 10


# ============================================================================
# ub: Get entity count (leaf, 0 callers)
# ============================================================================

def ub() -> int:
    """
    $ub: Get current entity count.

    Returns:
        Entity count from 9671176
    """
    return i32_load(9671176)


# ============================================================================
# ua: Set player selection value (leaf, 0 callers)
# ============================================================================

def ua(var0: int) -> None:
    """
    $ua: Store player selection value.

    Args:
        var0: Value to store
    """
    i32_store(9561844, var0)


# ============================================================================
# ib: Set cursor/selection mode (leaf, 0 callers)
# ============================================================================

def ib(var0: int) -> None:
    """
    $ib: Set cursor selection mode.

    Sets different cursor behavior based on mode:
    - Mode 0: Use unit type table at 9681696
    - Mode 1: Use table at 9681776 with value 100
    - Mode 2: Use table at 9681792 with value 100

    Args:
        var0: Cursor mode (0, 1, or 2)
    """
    i32_store(9681464, var0)

    if var0 == 0:
        # Mode 0 - use unit type table
        i32_store(9681476, 9681696)
        i32_store(9681468, 0)
        # Get value from entity type table
        unit_type = i32_load(9681696)
        type_offset = unit_type * 404 + 9568096
        value = i32_load(type_offset + 68)
        i32_store(9681472, value)
    elif var0 == 1:
        # Mode 1 - default table
        i32_store(9681476, 9681776)
        i32_store(9681468, 0)
        i32_store(9681472, 100)
    else:
        # Mode 2 - alternate table
        i32_store(9681476, 9681792)
        i32_store(9681468, 0)
        i32_store(9681472, 100)


# ============================================================================
# ja: Find player and set color values (leaf, 0 callers)
# ============================================================================

def ja(var0: int, var1: int, var2: int, var3: int) -> int:
    """
    $ja: Find player by ID and set color components.

    Searches player data for matching ID and sets RGB color values.

    Args:
        var0: Player ID to find
        var1: Red color value
        var2: Green color value
        var3: Blue color value

    Returns:
        Player index (1-based) if found, 0 otherwise
    """
    player_count = i32_load(9142892)

    if player_count < 2:
        return 0

    player_base = i32_load(9561692)

    for i in range(1, player_count):
        player_ptr = player_base + i * 286704
        player_id = i32_load(player_ptr + 284616)
        if player_id == var0:
            # Found player - set color values
            i32_store8(player_ptr + 283972, var1)  # Red
            i32_store8(player_ptr + 283973, var2)  # Green
            i32_store8(player_ptr + 283974, var3)  # Blue
            return i

    return 0


# ============================================================================
# ia: Find player and set alliance value (leaf, 0 callers)
# ============================================================================

def ia(var0: int, var1: int) -> int:
    """
    $ia: Find player by ID and set alliance value.

    Searches player data for matching ID and sets alliance status.

    Args:
        var0: Player ID to find
        var1: Alliance value to set

    Returns:
        Player index (1-based) if found, 0 otherwise
    """
    player_count = i32_load(9142892)

    if player_count < 2:
        return 0

    player_base = i32_load(9561692)

    for i in range(1, player_count):
        player_ptr = player_base + i * 286704
        player_id = i32_load(player_ptr + 284616)
        if player_id == var0:
            # Found player - set alliance value
            i32_store(player_ptr + 283960, var1)
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
get_viewport_offset = oa
get_entity_count = ub
set_player_selection = ua
set_cursor_mode = ib
set_player_color = ja
set_player_alliance = ia


# ============================================================================
# wb: Clear selection flag (leaf, 0 callers)
# ============================================================================

def wb() -> None:
    """
    $wb: Clear selection active flag.

    Clears the flag at 9681884 to indicate no active selection.
    """
    i32_store8(9681884, 0)


# ============================================================================
# vb: Set selection state (leaf, 0 callers)
# ============================================================================

def vb(var0: int, var1: int) -> None:
    """
    $vb: Set active selection state.

    Sets selection entity ID, active flag, and mode.

    Args:
        var0: Entity ID for selection
        var1: Selection mode
    """
    i32_store(9681892, var0)
    i32_store8(9681884, 1)
    i32_store8(9681885, var1)


# ============================================================================
# zb: Set selection parameter 1 (leaf, 0 callers)
# ============================================================================

def zb(var0: int) -> None:
    """
    $zb: Store selection parameter 1.

    Args:
        var0: Value to store at 9681896
    """
    i32_store(9681896, var0)


# ============================================================================
# yb: Set selection parameter 2 (leaf, 0 callers)
# ============================================================================

def yb(var0: int) -> None:
    """
    $yb: Store selection parameter 2.

    Args:
        var0: Value to store at 9681900
    """
    i32_store(9681900, var0)


# ============================================================================
# Q: Get/set player resource value (leaf, 0 callers)
# ============================================================================

def Q(var0: int, var1: int, var2: int) -> int:
    """
    $Q: Get player resource value, optionally setting it first.

    If var2 is non-zero, sets the resource before returning.
    If var1 >= 97, updates a derived value.

    Player structure offsets:
    - 283984 + (var1 * 4): Resource array
    - 284372: Derived value source
    - 283868: Derived value destination

    Args:
        var0: Player index
        var1: Resource index
        var2: Value to set (0 to skip setting)

    Returns:
        Resource value at the specified index
    """
    player_base = i32_load(9561692)
    player_ptr = player_base + var0 * 286704

    if var2:
        # Set the resource value (var2 - 1)
        i32_store(player_ptr + 283984 + var1 * 4, var2 - 1)

    if var1 >= 97:
        # Update derived value
        derived = i32_load(player_ptr + 284372)
        i32_store(player_ptr + 283868, derived)

    return i32_load(player_ptr + 283984 + var1 * 4)


# ============================================================================
# R: Get/set player percentage value (leaf, 0 callers)
# ============================================================================

def R(var0: int, var1: int, var2: int, var3: int) -> int:
    """
    $R: Get player percentage value with optional setting.

    Manages two percentage values at offsets 286684 and 286688.

    Args:
        var0: Player index
        var1: Value to set (0 to skip setting, uses formula 100 - (var1 - 1))
        var2: Offset selector (0 for 286684, non-zero for 286688)
        var3: Auto-reset flag for alternate offset

    Returns:
        Percentage value at selected offset
    """
    player_base = i32_load(9561692)
    player_ptr = player_base + var0 * 286704

    # Select offset based on var2
    offset = 286688 if var2 else 286684

    if var1:
        # Set value: 100 - (var1 - 1)
        i32_store(player_ptr + offset, 100 - (var1 - 1))

        if var3 and not i32_load(player_ptr + 286688):
            # Auto-reset alternate offset to 100
            i32_store(player_ptr + 286688, 100)

    return i32_load(player_ptr + offset)


# ============================================================================
# Batch 28 Aliases
# ============================================================================

clear_selection = wb
set_selection = vb
set_selection_param1 = zb
set_selection_param2 = yb
get_set_resource = Q
get_set_percentage = R


# ============================================================================
# lc: Set FPS limit (leaf, 0 callers)
# ============================================================================

def lc(var0: int) -> None:
    """
    $lc: Set game FPS limit.

    Only sets value if global flag at 9147210 is not set.
    Clamps value to maximum of 30.

    Args:
        var0: Target FPS (clamped to max 30)
    """
    if not i32_load8_u(9147210):
        # Use min(var0, 30) but WAT uses max via select with ge_u
        clamped = 30 if var0 >= 30 else var0
        i32_store(40592, clamped)


# ============================================================================
# fa: Set player game info (leaf, 0 callers)
# ============================================================================

def fa(var0: int, var1: int, var2: int) -> None:
    """
    $fa: Set player game info values.

    Sets player information if player index is valid.

    Args:
        var0: Player index
        var1: Value for offset 284608
        var2: Value for offset 284620 (stored as var2 + 1)
    """
    player_count = i32_load(9142892)

    if var0 < player_count:
        player_base = i32_load(9561692)
        player_ptr = player_base + var0 * 286704
        i32_store(player_ptr + 284620, var2 + 1)
        i32_store(player_ptr + 284608, var1)


# ============================================================================
# ga: Get/set game speed (leaf, 0 callers)
# ============================================================================

def ga(var0: int, var1: int) -> int:
    """
    $ga: Get or set game speed value.

    Behavior depends on global flag at 9147152:
    - If flag is 0: returns whether speed is non-zero
    - If flag is set and var0 is 0: returns current speed
    - If flag is set and var0 is non-zero: sets and returns new speed

    Args:
        var0: Set flag (0 to get, non-zero to set)
        var1: New speed value (if setting)

    Returns:
        Speed value or boolean based on mode
    """
    if not i32_load8_u(9147152):
        # Return whether speed is non-zero
        return 1 if i32_load(9561752) != 0 else 0

    if not var0:
        # Just return current speed
        return i32_load(9561752)

    # Set new speed
    i32_store(9561752, var1)
    return var1


# ============================================================================
# ha: Track mouse clicks (leaf, 0 callers)
# ============================================================================

def ha(var0: int) -> int:
    """
    $ha: Track mouse click events for double-click detection.

    Stores click position and increments counter.
    Returns comparison result for double-click detection.

    Args:
        var0: Click position/target

    Returns:
        2 if counter > 7, otherwise comparison result
    """
    i32_store(9561756, var0)

    # Increment click counter
    counter = i32_load(9561764) + 1
    i32_store(9561764, counter)

    if counter <= 7:
        prev_click = i32_load(9561760)
        if prev_click:
            # Compare with previous click
            return 1 if var0 == prev_click else 0
        # Compare with stored value
        return 1 if i32_load(9561752) == var0 else 0
    else:
        return 2


# ============================================================================
# aa: Set camera/view parameters (leaf, 0 callers)
# ============================================================================

def aa(var0: int, var1: int, var2: int, var3: int, var4: int) -> None:
    """
    $aa: Set multiple camera/view parameters.

    Stores 5 values to consecutive memory locations for camera state.

    Args:
        var0: Value for 9147125 (byte)
        var1: Value for 9147126 (byte)
        var2: Value for 9147127 (byte)
        var3: Value for 9147128 (i32)
        var4: Value for 9147132 (i32)
    """
    i32_store8(9147126, var1)
    i32_store8(9147125, var0)
    i32_store8(9147127, var2)
    i32_store(9147128, var3)
    i32_store(9147132, var4)


# ============================================================================
# Ie: Set diplomacy matrix value (leaf, 0 callers)
# ============================================================================

def Ie(var0: int, var1: int, var2: int, var3: int) -> None:
    """
    $Ie: Set diplomacy/alliance matrix value.

    Sets values in diplomacy matrices based on mode.
    Mode 0: Sets bidirectional alliance
    Mode 3: Sets unidirectional value

    Args:
        var0: Value to set (boolean)
        var1: Player 1 index
        var2: Player 2 index
        var3: Mode (0 for bidirectional, 3 for unidirectional)
    """
    player_count = i32_load(9142892)
    value = 1 if var0 != 0 else 0

    if var3 == 0:
        # Bidirectional alliance matrix
        matrix_base = i32_load(9143004)
        # Set [var1][var2]
        offset1 = player_count * var1 + var2
        i32_store8(matrix_base + offset1, value)
        # Set [var2][var1]
        offset2 = player_count * var2 + var1
        i32_store8(matrix_base + offset2, value)
    elif var3 == 3:
        # Unidirectional matrix
        matrix_base = i32_load(9143012)
        offset = player_count * var1 + var2
        i32_store8(matrix_base + offset, value)


# ============================================================================
# Batch 29 Aliases
# ============================================================================

set_fps_limit = lc
set_player_info = fa
get_set_game_speed = ga
track_click = ha
set_camera_params = aa
set_diplomacy = Ie


# ============================================================================
# se: Get terrain/map value (leaf, 0 callers)
# ============================================================================

def se() -> int:
    """
    $se: Get terrain/map pointer or value.

    Returns:
        Value at 9140328 (likely map data pointer)
    """
    return i32_load(9140328)


# ============================================================================
# kf: Set global7 and global8 (leaf, 0 callers)
# ============================================================================

def kf(var0: int, var1: int) -> None:
    """
    $kf: Set two global values.

    Args:
        var0: Value for global8
        var1: Value for global7
    """
    from tzar._runtime import global_set
    global_set('global8', var0)
    global_set('global7', var1)


# ============================================================================
# lf: Get stack pointer (leaf, 0 callers)
# ============================================================================

def lf() -> int:
    """
    $lf: Get current stack pointer (global0).

    Returns:
        Current stack pointer value
    """
    from tzar._runtime import get_stack_pointer
    return get_stack_pointer()


# ============================================================================
# mf: Set stack pointer (leaf, 0 callers)
# ============================================================================

def mf(var0: int) -> None:
    """
    $mf: Set stack pointer (global0).

    Args:
        var0: New stack pointer value
    """
    from tzar._runtime import set_stack_pointer
    set_stack_pointer(var0)


# ============================================================================
# nf: Allocate stack space (leaf, 0 callers)
# ============================================================================

def nf(var0: int) -> int:
    """
    $nf: Allocate aligned stack space.

    Subtracts var0 from stack pointer and aligns to 16-byte boundary.

    Args:
        var0: Number of bytes to allocate

    Returns:
        New aligned stack pointer
    """
    from tzar._runtime import get_stack_pointer, set_stack_pointer
    new_sp = (get_stack_pointer() - var0) & ~15  # Align to 16 bytes
    set_stack_pointer(new_sp)
    return new_sp


# ============================================================================
# Qa: Check alliance status for entity (leaf, 0 callers)
# ============================================================================

def Qa(var0: int) -> int:
    """
    $Qa: Check if current player is allied with entity's owner.

    Looks up entity owner and checks alliance matrix.

    Args:
        var0: Entity type or ID to check

    Returns:
        1 if allied, 0 if not or not found
    """
    player_count = i32_load(9142892)

    if player_count < 2:
        return 1

    player_base = i32_load(9561692)

    for i in range(1, player_count):
        player_ptr = player_base + i * 286704
        # Check if entity belongs to this player
        if var0 == i32_load(player_ptr + 283908):
            # Get alliance matrix base
            alliance_matrix = i32_load(9143004)
            current_player = i32_load(9142872)
            # Check alliance status
            offset = player_ptr + 283908
            owner = i32_load(offset)
            matrix_offset = alliance_matrix + current_player * player_count + owner
            return 1 if i32_load8_u(matrix_offset) != 0 else 0

    return 1


# ============================================================================
# Batch 30 Aliases
# ============================================================================

get_map_value = se
set_globals_7_8 = kf
get_stack_ptr = lf
set_stack_ptr = mf
alloc_stack = nf
check_alliance = Qa


# ============================================================================
# ma: Set multiple boolean flags (leaf, 0 callers)
# ============================================================================

def ma(var0: int, var1: int, var2: int, var3: int, var4: int) -> None:
    """
    $ma: Set 5 boolean flags at consecutive memory locations.

    Args:
        var0: Flag for 9561800
        var1: Flag for 9561802
        var2: Flag for 9561803
        var3: Flag for 9561804
        var4: Flag for 9561801
    """
    i32_store8(9561804, 1 if var3 != 0 else 0)
    i32_store8(9561803, 1 if var2 != 0 else 0)
    i32_store8(9561802, 1 if var1 != 0 else 0)
    i32_store8(9561800, 1 if var0 != 0 else 0)
    i32_store8(9561801, 1 if var4 != 0 else 0)


# ============================================================================
# vd: Get game mode value (leaf, 0 callers)
# ============================================================================

def vd() -> int:
    """
    $vd: Get game mode or configuration value.

    Returns:
        Value at 9143000
    """
    return i32_load(9143000)


# ============================================================================
# wa: Find player and set status (leaf, 0 callers)
# ============================================================================

def wa(var0: int, var1: int) -> None:
    """
    $wa: Find player by ID and set status value.

    Searches for player with matching ID and sets offset 284604.

    Args:
        var0: Player ID to find
        var1: Status value to set
    """
    player_base = i32_load(9561692)
    player_count = i32_load(9142892)

    if player_count < 2:
        # No players to search, set on player 0
        i32_store(player_base + 284604, var1)
        return

    found_idx = 0
    for i in range(1, player_count):
        player_ptr = player_base + i * 286704
        if var0 == i32_load(player_ptr + 284616):
            found_idx = i
            break

    # Set value at found player (or player 0 if not found)
    target_ptr = player_base + found_idx * 286704
    i32_store(target_ptr + 284604, var1)


# ============================================================================
# fb: Get entity type size/cost (leaf, 0 callers)
# ============================================================================

def fb(var0: int, var1: int) -> int:
    """
    $fb: Get entity type size or cost value.

    Returns calculated value based on entity type and direction flag.

    Args:
        var0: Entity type index (must be <= 254)
        var1: Direction flag (0 or non-zero)

    Returns:
        Calculated size/cost value, or 0 if invalid type
    """
    if var0 > 254:
        return 0

    type_base = var0 * 404 + 9568096

    if var1:
        # Get value at offset 180 + 8, multiply by 48
        ptr = i32_load(type_base + 180) + 8
        return i32_load(ptr) * 48
    else:
        # Get value at offset 144 (9568240 = 9568096 + 144), multiply by -48
        ptr = type_base + 144
        return i32_load(ptr) * -48


# ============================================================================
# rb: Get entity type category (leaf, 0 callers)
# ============================================================================

def rb(var0: int) -> int:
    """
    $rb: Get entity type category.

    Args:
        var0: Entity type index

    Returns:
        Category value at offset 264
    """
    type_base = var0 * 404 + 9568096
    return i32_load(type_base + 264)


# ============================================================================
# qb: Get entity type attribute (leaf, 0 callers)
# ============================================================================

def qb(var0: int) -> int:
    """
    $qb: Get entity type attribute.

    Args:
        var0: Entity type index

    Returns:
        Attribute value at offset 84
    """
    type_base = var0 * 404 + 9568096
    return i32_load(type_base + 84)


# ============================================================================
# Batch 31 Aliases
# ============================================================================

set_flags = ma
get_game_mode = vd
set_player_status = wa
get_entity_size = fb
get_entity_category = rb
get_entity_attribute = qb


# ============================================================================
# ic: Clear UI flag (leaf, 0 callers)
# ============================================================================

def ic() -> None:
    """
    $ic: Clear UI/dialog flag.

    Clears flag at 9140304.
    """
    i32_store8(9140304, 0)


# ============================================================================
# da: Set dialog/UI state (leaf, 0 callers)
# ============================================================================

def da(var0: int, var1: int, var2: int) -> None:
    """
    $da: Set dialog/UI state values.

    If previous value exists and var1 is set, enables the flag.

    Args:
        var0: Main value for 9142384
        var1: Flag value for 9142388
        var2: Unused
    """
    prev_val = i32_load(9142384)

    if prev_val and var1:
        i32_store8(9140304, 1)

    i32_store8(9142388, var1)
    i32_store(9142384, var0)


# ============================================================================
# wc: Add to player resource counters (leaf, 0 callers)
# ============================================================================

def wc(var0: int, var1: int, var2: int, var3: int, var4: int) -> None:
    """
    $wc: Add values to player resource counters.

    Adds to 4 consecutive counter values for specified player.

    Args:
        var0: Amount to add to offset 283848
        var1: Amount to add to offset 283852
        var2: Amount to add to offset 283856
        var3: Amount to add to offset 283860
        var4: Player index
    """
    player_base = i32_load(9561692)
    player_ptr = player_base + var4 * 286704

    # Add to each counter
    curr = i32_load(player_ptr + 283848)
    i32_store(player_ptr + 283848, curr + var0)

    curr = i32_load(player_ptr + 283852)
    i32_store(player_ptr + 283852, curr + var1)

    curr = i32_load(player_ptr + 283856)
    i32_store(player_ptr + 283856, curr + var2)

    curr = i32_load(player_ptr + 283860)
    i32_store(player_ptr + 283860, curr + var3)


# ============================================================================
# xc: Find entity by type and owner (leaf, 0 callers)
# ============================================================================

def xc(var0: int, var1: int) -> int:
    """
    $xc: Find entity matching type and owner.

    Searches entity table for matching entity.

    Args:
        var0: Entity type to find
        var1: Owner player index

    Returns:
        Entity index if found, 0 otherwise
    """
    entity_count = i32_load(9142844)

    if entity_count < 4:
        return 3 if entity_count >= 3 else 0

    entity_base = i32_load(9671128)

    for i in range(3, entity_count):
        entity_ptr = entity_base + i * 132
        entity_type = i32_load(entity_ptr + 110) & 0xFFFF  # i32.load16_u
        if var0 == entity_type:
            entity_owner = i32_load8_u(entity_ptr + 122)
            if entity_owner == var1:
                return i

    return 0


# ============================================================================
# Xa: Set map dimensions (leaf, 0 callers)
# ============================================================================

def Xa(var0: int, var1: int) -> None:
    """
    $Xa: Set map dimension values.

    Args:
        var0: Value for 9142952 (width?)
        var1: Value for 9142956 (height?)
    """
    i32_store(9142956, var1)
    i32_store(9142952, var0)


# ============================================================================
# C: Set random seed (leaf, 0 callers)
# ============================================================================

def C(var0: int) -> None:
    """
    $C: Initialize random number generator seed.

    Sets seed and derived XOR values for PRNG.

    Args:
        var0: Seed value
    """
    i32_store(9147312, var0)
    i32_store(9147324, var0 ^ 0xFFFFFFFF)  # -1 xor = bitwise NOT
    i32_store(9147320, var0 ^ 0xA5A5A5A5)  # -1515870811
    i32_store(9147316, var0 ^ 0x5A5A5A5A)  # 1515870810


# ============================================================================
# Batch 32 Aliases
# ============================================================================

clear_ui_flag = ic
set_dialog_state = da
add_resources = wc
find_entity = xc
set_map_dims = Xa
set_random_seed = C


# ============================================================================
# BATCH 33: More exported accessor functions
# ============================================================================

# ============================================================================
# F: Store float value (leaf, 0 callers)
# ============================================================================

def F(var0: float) -> None:
    """
    $F: Store float value at address 40616.

    Likely a game setting/configuration value.

    Args:
        var0: Float value to store
    """
    f32_store(40616, var0)


# ============================================================================
# E: Store byte value (leaf, 0 callers)
# ============================================================================

def E(var0: int) -> None:
    """
    $E: Store byte at address 9147336.

    Single byte store, likely a flag or small value.

    Args:
        var0: Byte value (0-255)
    """
    i32_store8(9147336, var0)


# ============================================================================
# O: Get player data pointer (leaf, exported as O and Ob)
# ============================================================================

def O(var0: int) -> int:
    """
    $O: Get player data pointer by index.

    Calculates pointer to player data structure.
    Player stride = 286704 bytes.

    Args:
        var0: Player index

    Returns:
        Pointer to player data
    """
    return i32_load(9561692) + var0 * 286704


# Alias for second export name
Ob = O


# ============================================================================
# ba: Get player count (leaf, 0 callers)
# ============================================================================

def ba() -> int:
    """
    $ba: Get player count from appropriate address.

    Uses select pattern to choose between two addresses based on flag.
    If flag at 9147212 is non-zero: loads from 9142892
    Otherwise: loads from 41092

    Returns:
        Player count value
    """
    addr = 9142892 if i32_load8_u(9147212) else 41092
    return i32_load(addr)


# ============================================================================
# bb: Return constant address (leaf, 0 callers)
# ============================================================================

def bb() -> int:
    """
    $bb: Return constant address 9681488.

    Likely a pointer to a static data structure.

    Returns:
        Constant 9681488
    """
    return 9681488


# ============================================================================
# D: XorShift random number generator (leaf, 1 caller)
# ============================================================================

def D(var0: int) -> int:
    """
    $D: XorShift random number generator.

    Implements XorShift PRNG algorithm using 128-bit state
    stored at addresses 9147312-9147324.

    Args:
        var0: Upper bound (exclusive) for result

    Returns:
        Random value in range [0, var0)
    """
    # Load state
    var3 = i64_load(9147316)
    var1 = i32_load(9147312)
    i32_store(9147316, var1)  # Shift state
    var2 = i32_load(9147324)
    i64_store(9147320, var3)  # Shift state

    # XorShift operations
    var2 = (var2 ^ (var2 << 11)) & 0xFFFFFFFF
    var1 = (var1 ^ (var1 >> 19) ^ (var2 >> 8) ^ var2) & 0xFFFFFFFF
    i32_store(9147312, var1)

    # Return result mod var0 (avoid division by zero)
    return var1 % var0 if var0 != 0 else 0


# ============================================================================
# Batch 33 Aliases
# ============================================================================

store_float_setting = F
set_byte_flag = E
get_player_ptr = O
get_player_count = ba
get_static_data_ptr = bb
random = D


# ============================================================================
# BATCH 34: Stubs and simple accessors
# ============================================================================

# ============================================================================
# No-op stub functions (exported but do nothing)
# ============================================================================

def Ga(var0: int, var1: int, var2: int) -> None:
    """$Ga: No-op stub function."""
    pass


def Se(var0: int) -> None:
    """$Se: No-op stub function."""
    pass


def Ba() -> None:
    """$Ba: No-op stub function. Also exported as Fa, Jb, he."""
    pass


# Multiple export aliases for Ba
Fa = Ba
Jb = Ba
he = Ba


def Oa(var0: int, var1: int) -> None:
    """$Oa: No-op stub function. Also exported as Kd, Ld."""
    pass


# Multiple export aliases for Oa
Kd = Oa
Ld = Oa


# ============================================================================
# Hc: Get game state offset 48 (leaf, exported as Hc, Pe)
# ============================================================================

def Hc() -> int:
    """
    $Hc: Get value from game state offset 48.

    Returns i32_load(i32_load(9142424) + 48).

    Returns:
        Value at game state offset 48
    """
    return i32_load(i32_load(9142424) + 48)


# Alias for Pe export
Pe = Hc


# ============================================================================
# V: Set player resource value (leaf, 0 callers)
# ============================================================================

def V(var0: int, var1: int, var2: int) -> None:
    """
    $V: Set player resource value.

    Sets resource at index var2 for player var0 to value var1.
    Resource offset: 283848 + var2 * 4

    Args:
        var0: Player index
        var1: Value to set
        var2: Resource index
    """
    player_ptr = i32_load(9561692) + var0 * 286704
    i32_store(player_ptr + 283848 + var2 * 4, var1)


# ============================================================================
# Batch 34 Aliases
# ============================================================================

set_player_resource = V
get_game_state_48 = Hc


# ============================================================================
# BATCH 35: More simple exported accessors
# ============================================================================

# ============================================================================
# I: Return constant 356 (likely entity struct size or similar)
# ============================================================================

def I() -> int:
    """
    $I: Return constant 356.

    Likely returns a struct size or constant value.

    Returns:
        356
    """
    return 356


# ============================================================================
# H: Get value from 9142848
# ============================================================================

def H() -> int:
    """
    $H: Get value from address 9142848.

    Returns:
        Value at 9142848
    """
    return i32_load(9142848)


# ============================================================================
# Ja: Get max player index (count - 1)
# ============================================================================

def Ja() -> int:
    """
    $Ja: Get maximum player index.

    Returns player count - 1 (i.e., max valid index).

    Returns:
        Maximum player index
    """
    return i32_load(41092) - 1


# ============================================================================
# Na: Return constant 9561856 (pointer)
# ============================================================================

def Na() -> int:
    """
    $Na: Return constant address 9561856.

    Likely a pointer to a data structure.

    Returns:
        9561856
    """
    return 9561856


# ============================================================================
# G: Bounds check function
# ============================================================================

def G(var0: int, var1: int) -> int:
    """
    $G: Check if coordinates are within map bounds.

    Returns 1 if var0 and var1 are valid coordinates within map size.
    Map size is stored at 9142440.

    Args:
        var0: X coordinate
        var1: Y coordinate

    Returns:
        1 if in bounds, 0 otherwise
    """
    var2 = i32_load(9142440)  # Map size
    return int(
        (var2 > var1) and
        (var0 < var2) and
        ((var0 | var1) >= 0)
    )


# ============================================================================
# P: Get current player map position
# ============================================================================

def P() -> int:
    """
    $P: Calculate current player's position on map.

    Computes: map_size * player[current].offset_y + player[current].offset_x

    Returns:
        Position index on map
    """
    map_size = i32_load(9142440)
    current_player = i32_load(9142872)
    player_ptr = i32_load(9561692) + current_player * 286704
    offset_x = i32_load(player_ptr + 283872)
    offset_y = i32_load(player_ptr + 283876)
    return map_size * offset_y + offset_x


# ============================================================================
# X: Check if entity is selected
# ============================================================================

def X(var0: int) -> int:
    """
    $X: Check if entity ID matches current selection.

    Args:
        var0: Entity ID to check

    Returns:
        1 if entity is selected, 0 otherwise
    """
    if var0 == 0:
        return 0
    current_player = i32_load(9142872)
    player_ptr = i32_load(9561692) + current_player * 286704
    selected = i32_load(player_ptr + 284608)
    return int(selected == var0)


# ============================================================================
# Batch 35 Aliases
# ============================================================================

get_struct_size = I
get_value_9142848 = H
get_max_player_idx = Ja
get_ptr_9561856 = Na
is_in_bounds = G
get_player_map_pos = P
is_selected = X


# ============================================================================
# BATCH 36: More simple exported accessors
# ============================================================================

# ============================================================================
# Ta: Return constant 255 (max byte value)
# ============================================================================

def Ta() -> int:
    """
    $Ta: Return constant 255.

    Returns:
        255 (max unsigned byte value)
    """
    return 255


# ============================================================================
# Pb: Get current player index
# ============================================================================

def Pb() -> int:
    """
    $Pb: Get current player index.

    Returns:
        Current player index from 9142872
    """
    return i32_load(9142872)


# ============================================================================
# Wa: Set camera/view parameters
# ============================================================================

def Wa(var0: int, var1: int, var2: float) -> None:
    """
    $Wa: Set camera or view parameters.

    Stores byte at 9143020, int at 9671160, float at 42160.

    Args:
        var0: Entity ID or target (stored at 9671160)
        var1: Mode flag (byte stored at 9143020)
        var2: Zoom or distance value (float stored at 42160)
    """
    i32_store8(9143020, var1)
    i32_store(9671160, var0)
    f32_store(42160, var2)


# ============================================================================
# ab: Get entity type field 152
# ============================================================================

def ab() -> int:
    """
    $ab: Get entity type field at offset 152.

    Accesses entity type table using current selection.

    Returns:
        Value at entity_type + 152
    """
    type_table_ptr = i32_load(9681476)
    idx = i32_load(9681468)
    type_id = i32_load(type_table_ptr + idx * 4)
    return i32_load(9568096 + type_id * 404 + 152)


# ============================================================================
# Lb: Load value from 9142912
# ============================================================================

def Lb() -> int:
    """
    $Lb: Get value from address 9142912.

    Returns:
        Value at 9142912
    """
    return i32_load(9142912)


# ============================================================================
# Ra: Get player field at offset 283964
# ============================================================================

def Ra(var0: int) -> int:
    """
    $Ra: Get player field at offset 283964.

    Args:
        var0: Player index

    Returns:
        Player field value at offset 283964
    """
    player_ptr = i32_load(9561692) + var0 * 286704
    return i32_load(player_ptr + 283964)


# ============================================================================
# Batch 36 Aliases
# ============================================================================

get_max_byte = Ta
get_current_player = Pb
set_camera_params = Wa
get_entity_type_152 = ab
get_value_9142912 = Lb
get_player_field_283964 = Ra


# ============================================================================
# BATCH 37: More simple load/store accessors
# ============================================================================

# ============================================================================
# Hb: Get game state offset 24
# ============================================================================

def Hb() -> int:
    """
    $Hb: Get value from game state offset 24.

    Returns i32_load(i32_load(9142424) + 24).

    Returns:
        Value at game state offset 24
    """
    return i32_load(i32_load(9142424) + 24)


# ============================================================================
# Dc: Load from 9163776
# ============================================================================

def Dc() -> int:
    """
    $Dc: Get value from address 9163776.

    Returns:
        Value at 9163776
    """
    return i32_load(9163776)


# ============================================================================
# Ec: Load from 9671136
# ============================================================================

def Ec() -> int:
    """
    $Ec: Get value from address 9671136.

    Returns:
        Value at 9671136
    """
    return i32_load(9671136)


# ============================================================================
# Pa: Load byte from 9147213
# ============================================================================

def Pa() -> int:
    """
    $Pa: Get byte from address 9147213.

    Returns:
        Byte value at 9147213
    """
    return i32_load8_u(9147213)


# ============================================================================
# Cc: Load from 9163780
# ============================================================================

def Cc() -> int:
    """
    $Cc: Get value from address 9163780.

    Returns:
        Value at 9163780
    """
    return i32_load(9163780)


# ============================================================================
# Qb: Set current player index
# ============================================================================

def Qb(var0: int) -> None:
    """
    $Qb: Set current player index.

    Stores value at 9142872 (current player).

    Args:
        var0: Player index to set as current
    """
    i32_store(9142872, var0)


# ============================================================================
# Batch 37 Aliases
# ============================================================================

get_game_state_24 = Hb
get_value_9163776 = Dc
get_value_9671136 = Ec
get_byte_9147213 = Pa
get_value_9163780 = Cc
set_current_player = Qb


# ============================================================================
# BATCH 38: More constants and accessors
# ============================================================================

# ============================================================================
# Jc: Get player count
# ============================================================================

def Jc() -> int:
    """
    $Jc: Get player count.

    Returns:
        Player count from 9142892
    """
    return i32_load(9142892)


# ============================================================================
# bc: Store to 9682196
# ============================================================================

def bc(var0: int) -> None:
    """
    $bc: Store value at 9682196.

    Args:
        var0: Value to store
    """
    i32_store(9682196, var0)


# ============================================================================
# Fc: Return constant 9147392
# ============================================================================

def Fc() -> int:
    """
    $Fc: Return constant address 9147392.

    Returns:
        9147392
    """
    return 9147392


# ============================================================================
# Ac: Return constant 33104
# ============================================================================

def Ac() -> int:
    """
    $Ac: Return constant 33104.

    Returns:
        33104
    """
    return 33104


# ============================================================================
# eb: Get entity type field at offset 196
# ============================================================================

def eb(var0: int) -> int:
    """
    $eb: Get entity type field at offset 196.

    Args:
        var0: Entity type ID

    Returns:
        Value at entity_type + 196
    """
    return i32_load(9568096 + var0 * 404 + 196)


# ============================================================================
# Eb: Load byte from 9147212
# ============================================================================

def Eb() -> int:
    """
    $Eb: Get byte from address 9147212.

    This is a game mode/state flag.

    Returns:
        Byte value at 9147212
    """
    return i32_load8_u(9147212)


# ============================================================================
# Batch 38 Aliases
# ============================================================================

get_player_count = Jc
store_9682196 = bc
get_ptr_9147392 = Fc
get_const_33104 = Ac
get_entity_type_196 = eb
get_mode_flag = Eb


# ============================================================================
# BATCH 39: Conditional flags and pointers
# ============================================================================

# ============================================================================
# dc: Set flag conditionally
# ============================================================================

def dc() -> None:
    """
    $dc: Set flag at 9140312 to 1 if certain conditions met.

    Sets flag if both bytes at 9147210 and 9147152 are 0.
    """
    if (i32_load8_u(9147210) | i32_load8_u(9147152)) == 0:
        i32_store8(9140312, 1)


# ============================================================================
# ec: Clear flag conditionally
# ============================================================================

def ec() -> None:
    """
    $ec: Clear flag at 9140312 if certain conditions met.

    Clears flag if both bytes at 9147210 and 9147152 are 0.
    """
    if (i32_load8_u(9147210) | i32_load8_u(9147152)) == 0:
        i32_store8(9140312, 0)


# ============================================================================
# $b: Get player resources pointer conditionally
# ============================================================================

def dollar_b() -> int:
    """
    $$b: Get player resources pointer based on mode.

    If mode flag (9147212) is non-zero: returns player + 283984
    Otherwise: returns constant 9561072

    Returns:
        Pointer to resource data
    """
    if i32_load8_u(9147212):
        player_ptr = i32_load(9561692) + i32_load(9142872) * 286704
        return player_ptr + 283984
    return 9561072


# ============================================================================
# ad: Set three game fields conditionally
# ============================================================================

def ad(var0: int, var1: int, var2: int) -> None:
    """
    $ad: Set three game state fields if values are non-negative.

    Stores to offsets 108, 112, 116 from pointer at 9568076.

    Args:
        var0: Value for offset 108 (if >= 0)
        var1: Value for offset 112 (if >= 0)
        var2: Value for offset 116 (if >= 0)
    """
    base = i32_load(9568076)
    if var0 >= 0:
        i32_store(base + 108, var0)
    if var1 >= 0:
        i32_store(base + 112, var1)
    if var2 >= 0:
        i32_store(base + 116, var2)


# ============================================================================
# $d: Get game state offset 72
# ============================================================================

def dollar_d() -> int:
    """
    $$d: Get game state offset 72.

    Note: The mul/div 2400 is a no-op mathematically.

    Returns:
        Value at game state offset 72
    """
    return i32_load(i32_load(9142424) + 72)


# ============================================================================
# Da: Return constant 41104
# ============================================================================

def Da() -> int:
    """
    $Da: Return constant 41104.

    Returns:
        41104
    """
    return 41104


# ============================================================================
# Batch 39 Aliases
# ============================================================================

set_flag_conditional = dc
clear_flag_conditional = ec
get_resources_ptr = dollar_b
set_game_fields = ad
get_game_state_72 = dollar_d
get_const_41104 = Da


# ============================================================================
# BATCH 40: More simple load accessors
# ============================================================================

# ============================================================================
# _a: Load from 9681472
# ============================================================================

def _a() -> int:
    """
    $_a: Get value from address 9681472.

    Returns:
        Value at 9681472
    """
    return i32_load(9681472)


# ============================================================================
# He: Load from 9147220
# ============================================================================

def He() -> int:
    """
    $He: Get value from address 9147220.

    Returns:
        Value at 9147220
    """
    return i32_load(9147220)


# ============================================================================
# Ke: Load from 9681976
# ============================================================================

def Ke() -> int:
    """
    $Ke: Get value from address 9681976.

    Returns:
        Value at 9681976
    """
    return i32_load(9681976)


# ============================================================================
# Le: Load from 9687224
# ============================================================================

def Le() -> int:
    """
    $Le: Get value from address 9687224.

    Returns:
        Value at 9687224
    """
    return i32_load(9687224)


# ============================================================================
# Me: Load from 9687216
# ============================================================================

def Me() -> int:
    """
    $Me: Get value from address 9687216.

    Returns:
        Value at 9687216
    """
    return i32_load(9687216)


# ============================================================================
# Je: Get player color (RGB)
# ============================================================================

def Je(var0: int) -> int:
    """
    $Je: Get player color as RGB value.

    Reads three bytes from player data and combines into RGB.

    Args:
        var0: Player index

    Returns:
        RGB color value (R << 16 | G << 8 | B)
    """
    player_ptr = i32_load(9561692) + var0 * 286704
    r = i32_load8_u(player_ptr + 283972)
    g = i32_load8_u(player_ptr + 283973)
    b = i32_load8_u(player_ptr + 283974)
    return (r << 16) | (g << 8) | b


# ============================================================================
# Batch 40 Aliases
# ============================================================================

get_value_9681472 = _a
get_value_9147220 = He
get_value_9681976 = Ke
get_value_9687224 = Le
get_value_9687216 = Me
get_player_color = Je
