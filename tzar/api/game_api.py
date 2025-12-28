"""
Tzar Engine - High-Level Game API.
Clean Python interface for game operations.

This module provides semantic function names for the exported
WASM functions. The raw implementations are in mod.py.
"""

from tzar.runtime import load32, store32, load8u, store8

# Import raw implementations
from tzar.api import mod as _raw

# =============================================================================
# Memory Addresses
# =============================================================================

GAME_STATE = 9142424
ENTITIES = 9671128
PLAYERS = 9561692
ENTITY_TYPES = 9568096
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892

PLAYER_STRIDE = 286704
ENTITY_STRIDE = 132
ENTITY_TYPE_STRIDE = 404

# RNG state
RNG_STATE = 9147312


# =============================================================================
# Random Number Generation
# =============================================================================

def random(max_val: int) -> int:
    """
    Generate random integer in range [0, max_val).
    Uses XORShift algorithm.
    """
    return _raw.D(max_val)


# =============================================================================
# Game State
# =============================================================================

def get_game_tick() -> int:
    """Get current game tick/frame."""
    return load32(load32(GAME_STATE) + 48)


def is_paused() -> bool:
    """Check if game is paused."""
    return bool(load8u(9147210))


def pause_game() -> None:
    """Pause the game."""
    store8(9147210, 1)


def resume_game() -> None:
    """Resume the game."""
    store8(9147210, 0)


# =============================================================================
# Player Operations
# =============================================================================

def get_player_ptr(player_id: int) -> int:
    """Get pointer to player data structure."""
    return load32(PLAYERS) + (player_id * PLAYER_STRIDE)


def get_player_gold(player_id: int) -> int:
    """Get player's gold amount."""
    player = get_player_ptr(player_id)
    return load32(player + 8)


def get_player_wood(player_id: int) -> int:
    """Get player's wood amount."""
    player = get_player_ptr(player_id)
    return load32(player + 12)


def get_player_food(player_id: int) -> int:
    """Get player's food amount."""
    player = get_player_ptr(player_id)
    return load32(player + 16)


def get_player_stone(player_id: int) -> int:
    """Get player's stone amount."""
    player = get_player_ptr(player_id)
    return load32(player + 20)


def set_player_gold(player_id: int, amount: int) -> None:
    """Set player's gold amount."""
    player = get_player_ptr(player_id)
    store32(player + 8, amount)


def add_player_gold(player_id: int, amount: int) -> None:
    """Add to player's gold."""
    player = get_player_ptr(player_id)
    store32(player + 8, load32(player + 8) + amount)


# =============================================================================
# Entity Operations
# =============================================================================

def get_entity_ptr(entity_id: int) -> int:
    """Get pointer to entity data structure."""
    return load32(ENTITIES) + (entity_id * ENTITY_STRIDE)


def get_entity_x(entity_id: int) -> int:
    """Get entity X position."""
    entity = get_entity_ptr(entity_id)
    return load32(entity + 12)


def get_entity_y(entity_id: int) -> int:
    """Get entity Y position."""
    entity = get_entity_ptr(entity_id)
    return load32(entity + 16)


def get_entity_hp(entity_id: int) -> int:
    """Get entity current HP."""
    entity = get_entity_ptr(entity_id)
    return load32(entity + 24)


def get_entity_max_hp(entity_id: int) -> int:
    """Get entity max HP."""
    entity = get_entity_ptr(entity_id)
    return load32(entity + 28)


def get_entity_owner(entity_id: int) -> int:
    """Get entity owner player ID."""
    entity = get_entity_ptr(entity_id)
    return load32(entity + 8)


def get_entity_type_id(entity_id: int) -> int:
    """Get entity type ID."""
    entity = get_entity_ptr(entity_id)
    return load32(entity + 4)


def set_entity_hp(entity_id: int, hp: int) -> None:
    """Set entity HP."""
    entity = get_entity_ptr(entity_id)
    store32(entity + 24, hp)


def damage_entity(entity_id: int, damage: int) -> None:
    """Apply damage to entity."""
    entity = get_entity_ptr(entity_id)
    current = load32(entity + 24)
    new_hp = max(0, current - damage)
    store32(entity + 24, new_hp)


def heal_entity(entity_id: int, amount: int) -> None:
    """Heal entity."""
    entity = get_entity_ptr(entity_id)
    current = load32(entity + 24)
    max_hp = load32(entity + 28)
    new_hp = min(max_hp, current + amount)
    store32(entity + 24, new_hp)


# =============================================================================
# Entity Type Info
# =============================================================================

def get_entity_type_ptr(type_id: int) -> int:
    """Get pointer to entity type definition."""
    return ENTITY_TYPES + (type_id * ENTITY_TYPE_STRIDE)


def get_type_name_ptr(type_id: int) -> int:
    """Get pointer to entity type name string."""
    return load32(get_entity_type_ptr(type_id) + 4)


def get_type_base_hp(type_id: int) -> int:
    """Get base HP for entity type."""
    return load32(get_entity_type_ptr(type_id) + 12)


def get_type_cost_gold(type_id: int) -> int:
    """Get gold cost for entity type."""
    return load32(get_entity_type_ptr(type_id) + 36)


def get_type_cost_wood(type_id: int) -> int:
    """Get wood cost for entity type."""
    return load32(get_entity_type_ptr(type_id) + 40)


def get_type_cost_food(type_id: int) -> int:
    """Get food cost for entity type."""
    return load32(get_entity_type_ptr(type_id) + 44)


# =============================================================================
# Selection
# =============================================================================

def get_selection_count() -> int:
    """Get number of selected entities."""
    return load32(9215892)


def get_selected_entity(index: int) -> int:
    """Get entity ID from selection by index."""
    selection_list = load32(9215884)
    return load32(selection_list + (index * 4))


def clear_selection() -> None:
    """Clear current selection."""
    store32(9215892, 0)


# =============================================================================
# Camera
# =============================================================================

def get_camera_x() -> int:
    """Get camera X position."""
    return load32(9684804)


def get_camera_y() -> int:
    """Get camera Y position."""
    return load32(9684808)


def set_camera(x: int, y: int) -> None:
    """Set camera position."""
    store32(9684804, x)
    store32(9684808, y)


def center_camera_on_entity(entity_id: int) -> None:
    """Center camera on entity."""
    x = get_entity_x(entity_id)
    y = get_entity_y(entity_id)
    set_camera(x, y)


# =============================================================================
# Map Info
# =============================================================================

def get_map_width() -> int:
    """Get map width in tiles."""
    return load32(9147292)


def get_map_height() -> int:
    """Get map height in tiles."""
    return load32(9147296)


# =============================================================================
# Exported Function Name Mapping
# =============================================================================

# This maps the cryptic WASM export names to their purposes
EXPORT_MAP = {
    'D': random,
    # Add more mappings as they're discovered
}
