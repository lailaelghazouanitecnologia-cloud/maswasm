"""
Tzar Engine - API Module.

Provides high-level game operations.
"""

# Clean API
from tzar.api.game_api import (
    # Random
    random,

    # Game state
    get_game_tick,
    is_paused,
    pause_game,
    resume_game,

    # Player
    get_player_ptr,
    get_player_gold,
    get_player_wood,
    get_player_food,
    get_player_stone,
    set_player_gold,
    add_player_gold,

    # Entity
    get_entity_ptr,
    get_entity_x,
    get_entity_y,
    get_entity_hp,
    get_entity_max_hp,
    get_entity_owner,
    get_entity_type_id,
    set_entity_hp,
    damage_entity,
    heal_entity,

    # Entity types
    get_entity_type_ptr,
    get_type_name_ptr,
    get_type_base_hp,
    get_type_cost_gold,
    get_type_cost_wood,
    get_type_cost_food,

    # Selection
    get_selection_count,
    get_selected_entity,
    clear_selection,

    # Camera
    get_camera_x,
    get_camera_y,
    set_camera,
    center_camera_on_entity,

    # Map
    get_map_width,
    get_map_height,
)

# Raw exports (for advanced use)
from tzar.api import mod as raw
