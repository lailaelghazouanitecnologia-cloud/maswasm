"""
Tzar Engine - Python Interface.

A transpiled Python version of the Tzar RTS game engine.

Usage:
    from tzar import api

    # Get player resources
    gold = api.get_player_gold(player_id=0)

    # Damage an entity
    api.damage_entity(entity_id, damage=50)

    # Check game state
    if not api.is_paused():
        tick = api.get_game_tick()

Modules:
    api       - High-level game operations
    accessors - Low-level property getters/setters
    math      - Math utilities (sin, cos approximations)
    memory    - Memory allocation (malloc, free)
    core      - Core game logic (internal)
    runtime   - WebAssembly runtime emulation
"""

__version__ = "0.1.0"
__author__ = "Transpiled from WebAssembly"

# Main API
from tzar import api

# Submodules
from tzar import accessors
from tzar import math
from tzar import memory
from tzar import core
from tzar import runtime

# Convenience re-exports from api
from tzar.api import (
    # Random
    random,

    # Game state
    get_game_tick,
    is_paused,
    pause_game,
    resume_game,

    # Player resources
    get_player_gold,
    get_player_wood,
    get_player_food,
    get_player_stone,

    # Entity access
    get_entity_hp,
    get_entity_x,
    get_entity_y,
    damage_entity,
    heal_entity,

    # Camera
    get_camera_x,
    get_camera_y,
    set_camera,

    # Map
    get_map_width,
    get_map_height,
)
