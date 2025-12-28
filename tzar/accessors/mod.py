"""
Tzar Engine - Accessor Functions.
Property getters/setters for game state.
"""

from tzar.runtime import (
    load32, load8u, load16u,
    store32, store8, storef32,
    G,
)

# =============================================================================
# Memory Addresses
# =============================================================================

# Game state
GAME_STATE = 9142424
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892

# Arrays
PLAYERS = 9561692
ENTITY_TYPES = 9568096
ENTITIES = 9671128

# Strides
PLAYER_STRIDE = 286704
ENTITY_STRIDE = 132
ENTITY_TYPE_STRIDE = 404


# =============================================================================
# Stack Management (Emscripten ABI)
# =============================================================================

def get_stack_ptr() -> int:
    """Get current stack pointer."""
    return G.global0


def set_stack_ptr(ptr: int) -> None:
    """Set stack pointer."""
    G.global0 = ptr


def stack_alloc(size: int) -> int:
    """Allocate aligned space on stack, return pointer."""
    aligned = (G.global0 - size) & ~15  # 16-byte alignment
    G.global0 = aligned
    return aligned


# =============================================================================
# Player Access
# =============================================================================

def get_player(player_id: int) -> int:
    """Get pointer to player struct by ID."""
    return load32(PLAYERS) + (player_id * PLAYER_STRIDE)


def get_player_count() -> int:
    """Get number of players."""
    return load32(PLAYER_COUNT)


def get_current_player_id() -> int:
    """Get current player ID."""
    return load32(CURRENT_PLAYER)


# =============================================================================
# Entity Access
# =============================================================================

def get_entity(entity_id: int) -> int:
    """Get pointer to entity struct by ID."""
    return load32(ENTITIES) + (entity_id * ENTITY_STRIDE)


def get_entity_type(type_id: int) -> int:
    """Get pointer to entity type definition."""
    return ENTITY_TYPES + (type_id * ENTITY_TYPE_STRIDE)


def get_entity_type_id(entity_ptr: int) -> int:
    """Get type ID from entity pointer."""
    return load32(entity_ptr + 4)


# =============================================================================
# Game State Access
# =============================================================================

def get_game_state() -> int:
    """Get pointer to game state struct."""
    return load32(GAME_STATE)


def get_game_time() -> int:
    """Get current game time/tick."""
    return load32(load32(GAME_STATE) + 48)


def is_game_paused() -> bool:
    """Check if game is paused."""
    return bool(load8u(9147210))


# =============================================================================
# Map/Terrain Access
# =============================================================================

def get_map_width() -> int:
    """Get map width in tiles."""
    return load32(9147292)


def get_map_height() -> int:
    """Get map height in tiles."""
    return load32(9147296)


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


# =============================================================================
# Selection Access
# =============================================================================

def get_selection_count() -> int:
    """Get number of selected entities."""
    return load32(9215892)


def get_selection_list() -> int:
    """Get pointer to selection list."""
    return load32(9215884)


# =============================================================================
# Resource Constants
# =============================================================================

# Entity type IDs
UNIT_TYPE_PEASANT = 3749
UNIT_TYPE_WARRIOR = 4188
UNIT_TYPE_ARCHER = 5158


def get_peasant_type_id() -> int:
    return UNIT_TYPE_PEASANT


def get_warrior_type_id() -> int:
    return UNIT_TYPE_WARRIOR


def get_archer_type_id() -> int:
    return UNIT_TYPE_ARCHER


# =============================================================================
# Flags and State
# =============================================================================

def set_render_flag(flag: int) -> None:
    """Set rendering flag."""
    store8(9147336, flag)


def mark_entity_dirty(entity_ptr: int) -> None:
    """Mark entity as needing update."""
    store8(entity_ptr + 28, 1)


# =============================================================================
# Legacy Aliases (for compatibility)
# =============================================================================

# Exported function names
lf = get_stack_ptr
mf = set_stack_ptr
nf = stack_alloc
O = get_player
Hc = get_game_time
te = get_map_width
ue = get_map_height
Jd = set_camera
Gc = get_selection_count
E = set_render_flag

# Internal function names
func535 = get_entity_type_id
func536 = get_peasant_type_id
func537 = get_warrior_type_id
func538 = get_archer_type_id
