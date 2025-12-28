"""
Tzar Game Engine - Structure definitions and memory layout.

This module defines all known game structures with their fields,
allowing the transpiled code to use semantic names instead of raw offsets.
"""
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Any


# =============================================================================
# Structure Definitions
# =============================================================================

@dataclass
class Field:
    """A field in a structure."""
    offset: int
    name: str
    type: str  # 'i32', 'i16', 'i8', 'f32', 'ptr', etc.
    size: int = 4
    comment: str = ""


class Struct:
    """Base class for game structures."""
    name: str = "Unknown"
    size: int = 0
    fields: Dict[int, Field] = {}

    @classmethod
    def get_field(cls, offset: int) -> Optional[Field]:
        """Get field at offset."""
        return cls.fields.get(offset)

    @classmethod
    def field_name(cls, offset: int) -> str:
        """Get field name or offset string."""
        field = cls.get_field(offset)
        return field.name if field else f"field_{offset}"


# -----------------------------------------------------------------------------
# Player Structure (stride = 286704 bytes)
# -----------------------------------------------------------------------------
class Player(Struct):
    name = "Player"
    size = 286704
    base = 9561692  # Player array base address

    fields = {
        0: Field(0, "id", "i32", comment="Player ID"),
        4: Field(4, "team", "i32", comment="Team number"),
        8: Field(8, "gold", "i32", comment="Gold resource"),
        12: Field(12, "wood", "i32", comment="Wood resource"),
        16: Field(16, "food", "i32", comment="Food resource"),
        20: Field(20, "stone", "i32", comment="Stone resource"),
        24: Field(24, "population", "i32", comment="Current population"),
        28: Field(28, "max_population", "i32", comment="Max population"),
        32: Field(32, "score", "i32", comment="Player score"),
        36: Field(36, "kills", "i32", comment="Kill count"),
        40: Field(40, "deaths", "i32", comment="Death count"),
        44: Field(44, "buildings_built", "i32"),
        48: Field(48, "units_trained", "i32"),
        52: Field(52, "is_ai", "i32", comment="1 if AI controlled"),
        56: Field(56, "difficulty", "i32", comment="AI difficulty"),
        60: Field(60, "civilization", "i32", comment="Civilization type"),
        64: Field(64, "color", "i32", comment="Player color"),
        68: Field(68, "name_ptr", "ptr", comment="Pointer to name string"),
        # Building counts at offset 100+
        100: Field(100, "num_houses", "i32"),
        104: Field(104, "num_barracks", "i32"),
        108: Field(108, "num_stables", "i32"),
        # Technology flags at offset 1000+
        1000: Field(1000, "tech_flags", "i32", comment="Technology bitmask"),
    }


# -----------------------------------------------------------------------------
# Entity Structure (stride = 132 bytes)
# -----------------------------------------------------------------------------
class Entity(Struct):
    name = "Entity"
    size = 132
    base = 9671128  # Entity array base address

    fields = {
        0: Field(0, "id", "i32", comment="Entity ID"),
        4: Field(4, "type_id", "i32", comment="Entity type ID"),
        8: Field(8, "owner", "i32", comment="Owner player ID"),
        12: Field(12, "x", "f32", comment="X position"),
        16: Field(16, "y", "f32", comment="Y position"),
        20: Field(20, "z", "f32", comment="Z position"),
        24: Field(24, "hp", "i32", comment="Current health"),
        28: Field(28, "max_hp", "i32", comment="Max health"),
        32: Field(32, "state", "i32", comment="Entity state"),
        36: Field(36, "action", "i32", comment="Current action"),
        40: Field(40, "target_id", "i32", comment="Target entity ID"),
        44: Field(44, "target_x", "f32", comment="Target X"),
        48: Field(48, "target_y", "f32", comment="Target Y"),
        52: Field(52, "speed", "f32", comment="Movement speed"),
        56: Field(56, "attack", "i32", comment="Attack damage"),
        60: Field(60, "defense", "i32", comment="Defense value"),
        64: Field(64, "range", "i32", comment="Attack range"),
        68: Field(68, "vision", "i32", comment="Vision range"),
        72: Field(72, "selected", "i32", comment="Is selected"),
        76: Field(76, "group", "i32", comment="Control group"),
        80: Field(80, "animation", "i32", comment="Animation state"),
        84: Field(84, "frame", "i32", comment="Animation frame"),
        88: Field(88, "direction", "f32", comment="Facing direction"),
        92: Field(92, "flags", "i32", comment="Entity flags"),
        96: Field(96, "garrison_id", "i32", comment="Garrisoned in"),
        100: Field(100, "cargo", "i32", comment="Carried resource"),
        104: Field(104, "cargo_amount", "i32", comment="Resource amount"),
        108: Field(108, "rally_x", "f32", comment="Rally point X"),
        112: Field(112, "rally_y", "f32", comment="Rally point Y"),
        116: Field(116, "queue_count", "i32", comment="Queue length"),
        120: Field(120, "queue_ptr", "ptr", comment="Production queue"),
        124: Field(124, "next_entity", "i32", comment="Linked list next"),
        128: Field(128, "prev_entity", "i32", comment="Linked list prev"),
    }


# -----------------------------------------------------------------------------
# Entity Type Structure (stride = 404 bytes)
# -----------------------------------------------------------------------------
class EntityType(Struct):
    name = "EntityType"
    size = 404
    base = 9568096  # Entity type table base

    fields = {
        0: Field(0, "id", "i32", comment="Type ID"),
        4: Field(4, "name_ptr", "ptr", comment="Name string"),
        8: Field(8, "category", "i32", comment="Unit/Building/Resource"),
        12: Field(12, "base_hp", "i32", comment="Base health"),
        16: Field(16, "base_attack", "i32", comment="Base attack"),
        20: Field(20, "base_defense", "i32", comment="Base defense"),
        24: Field(24, "base_speed", "f32", comment="Base speed"),
        28: Field(28, "base_range", "i32", comment="Base range"),
        32: Field(32, "base_vision", "i32", comment="Base vision"),
        36: Field(36, "cost_gold", "i32"),
        40: Field(40, "cost_wood", "i32"),
        44: Field(44, "cost_food", "i32"),
        48: Field(48, "cost_stone", "i32"),
        52: Field(52, "build_time", "i32", comment="Build time in ticks"),
        56: Field(56, "population", "i32", comment="Population cost"),
        60: Field(60, "sprite_id", "i32", comment="Sprite resource ID"),
        64: Field(64, "icon_id", "i32", comment="Icon resource ID"),
        68: Field(68, "sound_id", "i32", comment="Sound set ID"),
        72: Field(72, "size_x", "i32", comment="Collision width"),
        76: Field(76, "size_y", "i32", comment="Collision height"),
        80: Field(80, "flags", "i32", comment="Type flags"),
    }


# -----------------------------------------------------------------------------
# Game State Structure
# -----------------------------------------------------------------------------
class GameState(Struct):
    name = "GameState"
    base = 9142424

    fields = {
        0: Field(0, "tick", "i32", comment="Current game tick"),
        4: Field(4, "state", "i32", comment="Game state enum"),
        8: Field(8, "paused", "i32", comment="Is paused"),
        12: Field(12, "speed", "i32", comment="Game speed"),
        16: Field(16, "map_width", "i32"),
        20: Field(20, "map_height", "i32"),
        24: Field(24, "seed", "i32", comment="Random seed"),
        448: Field(448, "current_player", "i32", comment="Current player index"),
        468: Field(468, "player_count", "i32", comment="Number of players"),
    }


# -----------------------------------------------------------------------------
# Heap/Memory Management
# -----------------------------------------------------------------------------
class HeapMeta(Struct):
    name = "HeapMeta"
    base = 9690464

    fields = {
        0: Field(0, "free_list", "i32", comment="Free block bitmap"),
        4: Field(4, "tree_root", "i32", comment="Large block tree"),
        8: Field(8, "free_size", "i32", comment="Total free bytes"),
        16: Field(16, "heap_base", "ptr", comment="Heap start"),
        20: Field(20, "heap_top", "ptr", comment="Current allocation"),
        24: Field(24, "heap_end", "ptr", comment="Heap end"),
        32: Field(32, "alloc_count", "i32", comment="Allocation count"),
    }


# =============================================================================
# Global Constants
# =============================================================================

GLOBALS = {
    # Game state
    9142424: ("GAME_STATE", "GameState base"),
    9142872: ("CURRENT_PLAYER", "Current player index"),
    9142892: ("PLAYER_COUNT", "Number of players"),

    # Arrays
    9561692: ("PLAYERS", "Player array base"),
    9568096: ("ENTITY_TYPES", "Entity type table"),
    9671128: ("ENTITIES", "Entity array base"),

    # Memory management
    9690464: ("HEAP_FREELIST", "Free block bitmap"),
    9690468: ("HEAP_TREE", "Large block tree root"),
    9690472: ("FREE_SIZE", "Total free bytes"),
    9690476: ("HEAP_TOTAL", "Total heap size"),
    9690480: ("HEAP_BASE", "Heap base pointer"),
    9690484: ("HEAP_TOP", "Heap top pointer"),
    9690488: ("HEAP_END", "Heap end pointer"),
    9690496: ("ALLOC_COUNT", "Allocation counter"),
    9690504: ("SMALL_BINS", "Small block bins"),
    9690768: ("LARGE_BINS", "Large block bins"),
    9690908: ("MEM_FLAGS", "Memory flags"),
    9690912: ("MEM_MUTEX", "Memory mutex"),
    9690984: ("ALLOC_HANDLER", "OOM handler callback"),
}


# =============================================================================
# Array Access Helpers
# =============================================================================

def get_player(index: int) -> int:
    """Get player address by index."""
    return Player.base + index * Player.size


def get_entity(index: int) -> int:
    """Get entity address by index."""
    return Entity.base + index * Entity.size


def get_entity_type(index: int) -> int:
    """Get entity type address by index."""
    return EntityType.base + index * EntityType.size


# =============================================================================
# Pattern Detection
# =============================================================================

def detect_struct_access(base_addr: int, offset: int) -> Optional[Tuple[str, str]]:
    """
    Detect if an address + offset is accessing a known structure.
    Returns (struct_name, field_name) or None.
    """
    # Check against known bases
    if base_addr == Player.base or (Player.base <= base_addr < Player.base + 8 * Player.size):
        field = Player.get_field(offset)
        if field:
            return ("Player", field.name)

    if base_addr == Entity.base or (Entity.base <= base_addr < Entity.base + 10000 * Entity.size):
        field = Entity.get_field(offset)
        if field:
            return ("Entity", field.name)

    if base_addr == EntityType.base:
        field = EntityType.get_field(offset)
        if field:
            return ("EntityType", field.name)

    if base_addr == GameState.base:
        field = GameState.get_field(offset)
        if field:
            return ("GameState", field.name)

    return None


def detect_array_pattern(base: int, index_expr: str, stride: int) -> Optional[str]:
    """
    Detect array access pattern: base + index * stride
    Returns semantic expression or None.
    """
    if base == Player.base and stride == Player.size:
        return f"players[{index_expr}]"

    if base == Entity.base and stride == Entity.size:
        return f"entities[{index_expr}]"

    if base == EntityType.base and stride == EntityType.size:
        return f"entity_types[{index_expr}]"

    return None


def get_constant_name(addr: int) -> Optional[str]:
    """Get symbolic name for a known address."""
    if addr in GLOBALS:
        return GLOBALS[addr][0]
    return None
