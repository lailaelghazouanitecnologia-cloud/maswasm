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
# Legacy Aliases
# =============================================================================

func32 = entity_tick
