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
