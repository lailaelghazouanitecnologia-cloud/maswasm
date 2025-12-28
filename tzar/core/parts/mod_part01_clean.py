"""
Tzar Engine - Core module (part 1) - Clean Version.
Entity tick/update functions.
"""

from tzar.runtime import (
    load32, load64, load8u, load16u,
    store32, store64, store8, storef32,
    u32, G,
)

from tzar.core.templates import (
    # Constants
    ENTITIES, PLAYERS, ENTITY_TYPES,
    ENTITY_STRIDE, ENTITY_TYPE_STRIDE,
    GAME_STATE,

    # Entity access
    EntityField, EntityTypeField,
    get_entity_ptr, get_entity_type_ptr,
    entity_x, entity_y, entity_hp, entity_state, entity_action,

    # Control groups
    CONTROL_GROUPS, find_in_control_groups,

    # Camera/viewport
    is_on_screen, get_viewport_offset,

    # Game flags
    is_game_paused, is_ai_enabled, are_animations_enabled,
    FLAG_PAUSED, FLAG_AI_ENABLED, FLAG_ANIMATIONS,
)


# =============================================================================
# Entity Field Offsets (from analysis)
# =============================================================================

class EntityExt:
    """Extended entity field offsets not in base EntityField."""
    OWNER_16 = 110       # Owner ID (16-bit)
    TILE_X = 112         # Tile X position (16-bit)
    TILE_Y = 114         # Tile Y position (16-bit)
    TYPE_ID_8 = 122      # Entity type ID (8-bit, same as sub_state)
    ANIM_FRAME = 124     # Animation frame
    UNIT_CLASS = 125     # Unit class (3 = building?)


# =============================================================================
# Entity Type Field Offsets (from analysis)
# =============================================================================

class EntityTypeExt:
    """Extended entity type field offsets."""
    COST_WOOD = 40       # Wood cost
    COST_GOLD_ALT = 36   # Alternative gold cost location
    SOMETHING_216 = 216  # Unknown
    SOMETHING_220 = 220  # Unknown
    FORMATION = 264      # Formation type (1 = special?)
    UPGRADE_PTR = 360    # Pointer to upgrade data


# =============================================================================
# Known Memory Addresses
# =============================================================================

# Animation data table
ANIM_DATA_TABLE = 9263856
ANIM_DATA_STRIDE = 72

# Map/terrain data
MAP_WIDTH_TILES = 9142440
TERRAIN_DATA = 9147376

# Game tick
GAME_TICK = 9142848

# Entity type for special check
SPECIAL_TYPE = 38448

# Upgrade default
DEFAULT_UPGRADE = 9142632


# =============================================================================
# Helper Functions
# =============================================================================

def get_entity_type_id(entity_ptr: int) -> int:
    """Get entity type ID from entity."""
    return load8u(entity_ptr + EntityExt.TYPE_ID_8)


def get_entity_tile_pos(entity_ptr: int) -> tuple:
    """Get entity tile position."""
    return (
        load16u(entity_ptr + EntityExt.TILE_X),
        load16u(entity_ptr + EntityExt.TILE_Y)
    )


def get_entity_owner_16(entity_ptr: int) -> int:
    """Get entity owner (16-bit version)."""
    return load16u(entity_ptr + EntityExt.OWNER_16)


def get_anim_data(type_id: int, offset: int) -> int:
    """Get animation data for entity type."""
    return load32(ANIM_DATA_TABLE + (type_id * ANIM_DATA_STRIDE) + offset)


def check_entity_in_any_control_group(entity_id: int, entities_base: int) -> bool:
    """Check if entity is in any of the 10 control groups."""
    for group_addr in CONTROL_GROUPS:
        group_ptr = load32(group_addr)
        if not group_ptr:
            continue

        count = load32(group_ptr + 8)
        if not count:
            continue

        entities_arr = load32(group_ptr)
        for i in range(count):
            eid = load32(entities_arr + (i * 4))
            entity_ptr = entities_base + (eid * ENTITY_STRIDE)
            if load32(entity_ptr + 28) == entity_id:
                return True

    return False


# =============================================================================
# Main Entity Update Function
# =============================================================================

def entity_tick(entity_ptr: int, skip_ai: int, param2: int):
    """
    Main entity update/tick function.
    Called each frame for each entity.

    Args:
        entity_ptr: Pointer to entity being updated
        skip_ai: If true, skip AI processing
        param2: Additional parameter (unused?)
    """
    # Allocate stack space
    stack_frame = G.global0 - 16
    G.global0 = stack_frame

    try:
        # Skip buildings (unit_class == 3)
        unit_class = load8u(entity_ptr + EntityExt.UNIT_CLASS)
        if unit_class == 3:
            return

        # Get entity type info
        type_id = get_entity_type_id(entity_ptr)
        type_ptr = get_entity_type_ptr(type_id)
        owner = get_entity_owner_16(entity_ptr)
        players_base = load32(PLAYERS)
        anim_data = get_anim_data(type_id, 28)

        # --- Screen visibility check ---
        if not skip_ai:
            if not is_game_paused() and is_ai_enabled():
                type_ptr_alt = get_entity_type_ptr(type_id)
                wood_cost = load32(type_ptr_alt + EntityTypeExt.COST_WOOD)

                if wood_cost:
                    tile_x, tile_y = get_entity_tile_pos(entity_ptr)

                    # Check if on screen (within threshold)
                    if is_on_screen(tile_x, tile_y):
                        # Get terrain value
                        map_width = load32(MAP_WIDTH_TILES)
                        terrain_ptr = load32(TERRAIN_DATA)
                        terrain_idx = (map_width * tile_y + tile_x) << 1
                        terrain_val = load16u(terrain_ptr + terrain_idx)

                        # Check game state for special handling
                        game_state_ptr = load32(GAME_STATE)
                        game_mode = load32(game_state_ptr + 48)

                        if game_mode == 2:
                            if u32(terrain_val) > 1:
                                pass  # Skip
                        elif not terrain_val:
                            pass  # Skip

                        # Queue some operation
                        cost_gold = load32(type_ptr_alt + EntityTypeExt.COST_GOLD_ALT)
                        game_tick = load32(GAME_TICK)

                        store32(stack_frame, load32(cost_gold + (((game_tick + tile_x) % wood_cost) << 2)))
                        store32(stack_frame + 4, tile_x)
                        store32(stack_frame + 8, tile_y)
                        # a_b() call would go here

        # --- Animation frame handling ---
        anim_frame = load8u(entity_ptr + EntityExt.ANIM_FRAME)

        # Check formation type
        formation = load32(type_ptr + EntityTypeExt.FORMATION)
        if formation == 1:
            upgrade_ptr = load32(type_ptr + EntityTypeExt.UPGRADE_PTR)
            if upgrade_ptr:
                anim_data = load32(upgrade_ptr)
            else:
                # Complex calculation for default animation
                v1 = load32(type_ptr + EntityTypeExt.SOMETHING_216)
                v2 = load32(type_ptr + EntityTypeExt.SOMETHING_220)
                result = v1 if u32(v2) < u32(v1) else v2

                # br_table logic simplified
                if u32(result) > 5:
                    anim_data = load32(DEFAULT_UPGRADE)

                store8(entity_ptr + EntityExt.ANIM_FRAME, 0)

        # --- Paused state handling ---
        if is_game_paused():
            # func77(entity_ptr)  # Would call render function
            store32(entity_ptr + EntityField.MAX_HP, 0)

        # --- Animation updates ---
        if are_animations_enabled():
            if skip_ai or is_game_paused():
                target_id = load32(entity_ptr + EntityField.TARGET_ID)
                if target_id:
                    pass  # func38(target_id)

            # Check for special entity type
            if load32(SPECIAL_TYPE) == type_id:
                entity_id = load32(entity_ptr + EntityField.MAX_HP)
                store8(entity_ptr + EntityExt.ANIM_FRAME, entity_id % 3)
            elif anim_data:
                store8(entity_ptr + EntityExt.ANIM_FRAME, 0)
                # func92(entity_ptr, 0.0, 0.0)

                if load32(anim_data + 24):
                    target = load32(entity_ptr + EntityField.TARGET_ID)
                    if target:
                        pass  # func254(anim_data, target)
            else:
                target = load32(entity_ptr + EntityField.TARGET_ID)
                if target:
                    pass  # func38(target)

        # --- Control group check ---
        action = load32(entity_ptr + EntityField.ACTION)
        if action:
            pass  # Has action

        # Check selection data
        selection_ptr = load32(9215884)
        entity_idx = load32(entity_ptr + 44)
        selection_data = load32(selection_ptr + (entity_idx << 4) + 4)
        derived_ptr = load32((selection_data * 40) + 9671200 + 32)

        if derived_ptr:
            pass  # Has derived data

        # Check if entity is in any control group
        if load32(9147132):  # Some flag
            entity_id = load32(entity_ptr + EntityField.MAX_HP)
            entities_base = load32(ENTITIES)

            if check_entity_in_any_control_group(entity_id, entities_base):
                pass  # Found in control group

    finally:
        # Restore stack
        G.global0 = stack_frame + 16


# =============================================================================
# Bit Stream / Compression Functions
# =============================================================================

def bitstream_read(stream_ptr: int, num_bits: int) -> int:
    """
    Read bits from a bit stream (arithmetic/range decoder).

    Args:
        stream_ptr: Pointer to stream state structure
        num_bits: Number of bits to read

    Returns:
        Decoded value

    Stream structure:
        +0: 8-byte buffer
        +8: range value
        +12: code value
        +16: current read position
        +20: buffer end
        +24: buffer limit
        +28: EOF flag
    """
    if num_bits <= 0:
        return 0

    code = load32(stream_ptr + 12)
    range_val = load32(stream_ptr + 8)
    result = 0

    while num_bits > 0:
        # Refill buffer if code < 0
        while code < 0:
            pos = load32(stream_ptr + 16)
            if not pos:
                break
            if u32(load32(stream_ptr + 24)) > u32(pos):
                # Bulk read with byte swap
                data = load64(pos)
                store32(stream_ptr + 16, pos + 7)
                swapped = (
                    ((data << 56) & 0xFF00000000000000) |
                    ((data << 40) & 0x00FF000000000000) |
                    ((data << 24) & 0x0000FF0000000000) |
                    ((data << 8) & 0x000000FF00000000) |
                    ((data >> 8) & 0x00000000FF000000) |
                    ((data >> 24) & 0x0000000000FF0000) |
                    ((data >> 40) & 0x000000000000FF00)
                )
                store64(stream_ptr, (load64(stream_ptr) << 56) | (swapped >> 8))
                break

            if u32(load32(stream_ptr + 20)) > u32(pos):
                store32(stream_ptr + 16, pos + 1)
                store64(stream_ptr, load8u(pos) | (load64(stream_ptr) << 8))
                break

            if not load32(stream_ptr + 28):
                store32(stream_ptr + 28, 1)  # EOF
                store64(stream_ptr, load64(stream_ptr) << 8)
            break

        # Range decode one bit
        shift = code + 8
        half_range = (range_val >> 1) & 0xFFFFFF
        buffer = load64(stream_ptr)
        threshold = i32((buffer >> shift) & 0xFFFFFFFF)

        if u32(half_range) < u32(threshold):
            store64(stream_ptr, buffer - (i32(half_range + 1) << shift))
            result = (1 << (num_bits - 1)) | result
        # else bit is 0

        # Update range
        range_val = half_range + 1
        normalize_bits = clz(range_val) ^ 24
        code = (range_val - half_range) - normalize_bits
        store32(stream_ptr + 12, code)
        range_val = (range_val << normalize_bits) - 1
        store32(stream_ptr + 8, range_val)

        num_bits -= 1

    return result


# =============================================================================
# Entity Queue System
# =============================================================================

# Queue base addresses
QUEUE_NORMAL = 9299872   # Normal entity queue
QUEUE_SPECIAL = 9299888  # Special/high-value queue

QUEUE_THRESHOLD = 1073741823  # 0x3FFFFFFF


class QueueOffsets:
    """Offsets within queue structure."""
    ARRAY_PTR = 0
    CAPACITY = 4
    COUNT = 8
    GROWTH = 12


def queue_push(value: int):
    """
    Add value to appropriate entity queue.

    Values >= QUEUE_THRESHOLD go to special queue.
    """
    stack_frame = G.global0 - 48
    G.global0 = stack_frame

    try:
        # Select queue based on value
        if u32(value) >= u32(QUEUE_THRESHOLD):
            adjusted_value = value - QUEUE_THRESHOLD
            queue = QUEUE_SPECIAL
        else:
            adjusted_value = value
            queue = QUEUE_NORMAL

        # Get queue state
        count = load32(queue + QueueOffsets.COUNT)
        capacity = load32(queue + QueueOffsets.CAPACITY)
        arr = load32(queue + QueueOffsets.ARRAY_PTR)

        # Grow if at capacity
        if count == capacity:
            growth = load32(queue + QueueOffsets.GROWTH)
            new_cap = growth + count
            store32(queue + QueueOffsets.CAPACITY, new_cap)

            old_arr = arr
            if u32(new_cap) > u32(QUEUE_THRESHOLD):
                arr = 0  # Overflow error
            else:
                from tzar.memory.mod import malloc
                arr = malloc(new_cap << 2)

            # TODO: memory.copy old data
            if count and old_arr:
                pass

            store32(queue + QueueOffsets.ARRAY_PTR, arr)

        # Push value
        store32(queue + QueueOffsets.COUNT, count + 1)
        store32(arr + (count << 2), adjusted_value)

        # Notify system
        if load8u(9142916):  # Network mode
            store32(stack_frame + 32, value)
        else:
            store32(stack_frame + 24, value)
            store64(stack_frame + 16, -4602115869219225600)
            store64(stack_frame + 8, 0)
            store64(stack_frame, 0)
        # a_b() external call here

    finally:
        G.global0 = stack_frame + 48


# =============================================================================
# Entity Destruction
# =============================================================================

def entity_destroy(entity_ptr: int):
    """
    Destroy entity - cleanup and queue for removal.

    Args:
        entity_ptr: Pointer to entity to destroy
    """
    stack_frame = G.global0 - 48
    G.global0 = stack_frame

    try:
        # Multiplayer sync check
        if load8u(9142906):
            target = load32(entity_ptr + 40)
            if not target:
                return

            color_idx = load8u(entity_ptr + 127) or 16

            if load8u(9142916):  # Network mode
                if u32(color_idx) <= 15:
                    idx = color_idx << 4
                    color = (
                        load32(1744 + idx) |
                        (load32(1748 + idx) << 8) |
                        (load32(1752 + idx) << 16) |
                        (load32(1756 + idx) << 24)
                    )
                    store32(stack_frame + 36, target)
                    store32(stack_frame + 32, color)
                return

            store32(stack_frame + 20, target)
            store32(stack_frame + 16, color_idx)
            return

        # Local/single player destruction
        if load8u(9142916):
            target = load32(entity_ptr + 40)
            if target:
                unit_class = load8u(entity_ptr + 125)
                store32(stack_frame + 4, target)
                store32(stack_frame, unit_class << 8)
            return

        # Check for child entities to destroy
        type_id = load8u(entity_ptr + 122)
        type_ptr = ENTITY_TYPES + (type_id * 404)

        if load32(type_ptr + 264) == 1:  # Formation type
            if u32(load32(type_ptr + 216)) >= 2:
                children = load32(entity_ptr + 12)
                if children:
                    count = load32(children + 8)
                    if count:
                        i = 0
                        while u32(i) < u32(count):
                            arr = load32(children)
                            entry = arr + (i << 2)

                            if load32(entry + 4) == 1:
                                queue_push(load32(entry))

                                # Remove entry
                                new_count = load32(children + 8) - 2
                                store32(children + 8, new_count)

                                # Shift array
                                if u32(i) < u32(new_count):
                                    j = i
                                    while u32(j) < u32(new_count):
                                        store32(arr + (j << 2),
                                               load32(arr + ((j + 2) << 2)))
                                        j += 1

                                i -= 2
                            i += 2

        # Queue entity reference for cleanup
        ref = load32(entity_ptr + 92)
        if ref:
            queue_push(ref)

    finally:
        store32(entity_ptr + 92, 0)

        # Additional reference cleanup
        other_ref = load32(entity_ptr + 80)
        if other_ref:
            pass  # Further cleanup needed

        G.global0 = stack_frame + 48


# =============================================================================
# Bitstream Refill
# =============================================================================

def bitstream_refill(stream_ptr: int):
    """
    Refill bitstream buffer with one byte.

    Args:
        stream_ptr: Pointer to stream state

    Stream offsets:
        +0: 8-byte buffer
        +12: bits available
        +16: read position
        +20: end position
        +28: EOF flag
    """
    if not stream_ptr:
        raise RuntimeError("Null stream")

    pos = load32(stream_ptr + 16)
    if not pos:
        raise RuntimeError("Null position")

    end = load32(stream_ptr + 20)
    if u32(end) > u32(pos):
        # Read one byte
        store32(stream_ptr + 16, pos + 1)
        store32(stream_ptr + 12, load32(stream_ptr + 12) + 8)
        store64(stream_ptr, load8u(pos) | (load64(stream_ptr) << 8))
        return

    # At end of buffer
    if not load32(stream_ptr + 28):
        # Set EOF, shift buffer
        store32(stream_ptr + 28, 1)
        store64(stream_ptr, load64(stream_ptr) << 8)
        store32(stream_ptr + 12, load32(stream_ptr + 12) + 8)
        return

    # Already at EOF
    store32(stream_ptr + 12, 0)


# =============================================================================
# Entity Rendering/Animation
# =============================================================================

def entity_render_update(entity_ptr: int, sprite_data: int, arg2: int, is_selected: int):
    """
    Update entity rendering/animation state.

    Args:
        entity_ptr: Entity to update
        sprite_data: Sprite/animation data pointer
        arg2: Additional parameter
        is_selected: Whether entity is selected
    """
    if not sprite_data:
        return

    stack_frame = G.global0 - 128
    G.global0 = stack_frame

    try:
        target = load32(entity_ptr + 40)
        if not target:
            return

        game_tick = load32(GAME_TICK)
        store32(entity_ptr + 48, sprite_data)

        owner = load16u(entity_ptr + 110)
        sub_owner = load16u(entity_ptr + 120)
        type_id = load8u(entity_ptr + 122)

        # Determine color index
        if load32(entity_ptr + 92):  # Has reference
            color_idx = 13
            if load8u(9142906):  # Multiplayer
                pass  # Keep color_idx = 13
        else:
            base_color = sub_owner if sub_owner else owner
            color_idx = (base_color & 0xFFFF) + 16

            if not load8u(9142916):  # Not network mode
                player_color = load8u(entity_ptr + 127)
                type_ptr = get_entity_type_ptr(type_id)

                if player_color or load32(type_ptr + 156):
                    color_idx = load32(type_ptr + 156) or player_color
            else:
                player_color = load8u(entity_ptr + 127)
                if player_color:
                    color_idx = player_color

        # Get entity type info
        type_ptr = get_entity_type_ptr(type_id)
        formation = load32(type_ptr + 264)

        # Get sprite info
        sprite_flags = load32(sprite_data + 32)
        sprite_scale = load32(sprite_data + 24)
        sprite_id = load32(sprite_data)
        frame_count = load32(sprite_data + 16)
        frame_size = frame_count * load32(sprite_data + 20)

        frame_idx = 0
        if frame_size:
            # Calculate frame from tick
            frame_idx = i32(load32(sprite_data + 4) // frame_size)

        # Handle selection state
        if not is_selected:
            if is_game_paused():
                unit_class = load8u(entity_ptr + 125)
            else:
                player_id = load32(CURRENT_PLAYER)
                if player_id:
                    visibility_ptr = load32(9143012)
                    owner = load16u(entity_ptr + 110)
                    player_count = load32(PLAYER_COUNT)
                    if load8u(visibility_ptr + owner + (player_count * player_id)):
                        unit_class = load8u(entity_ptr + 125)
                        if unit_class == 3:
                            pass  # Building - special handling

            # Calculate animation frame based on type
            v1 = load32(type_ptr + 216)
            v2 = load32(type_ptr + 220)

            # Complex frame calculation would go here
            # Involves formation type and unit state

    finally:
        G.global0 = stack_frame + 128


# =============================================================================
# Legacy Aliases
# =============================================================================

func32 = entity_tick
func33 = bitstream_read
func36 = bitstream_refill
func37 = entity_render_update
func38 = queue_push
func47 = entity_destroy
