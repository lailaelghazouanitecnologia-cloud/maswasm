"""
Tzar Engine - Code Templates and Abstractions.

Provides high-level patterns to simplify transpiled code:
- Block control flow
- Entity iteration
- Resource operations
- State machines
"""

from typing import Callable, Iterator, Optional, List, Any
from tzar.runtime import load32, store32, load8u, store8, load16u, u32


# =============================================================================
# Memory Constants
# =============================================================================

ENTITIES = 9671128
PLAYERS = 9561692
ENTITY_TYPES = 9568096
GAME_STATE = 9142424

ENTITY_STRIDE = 132
PLAYER_STRIDE = 286704
ENTITY_TYPE_STRIDE = 404


# =============================================================================
# Block Control Flow
# =============================================================================

class Block:
    """
    WASM block control flow abstraction.

    Replaces nested `while True:` patterns with cleaner control.

    Usage:
        with Block() as b:
            if condition:
                b.break_()
            do_something()
    """

    def __init__(self, label: str = ""):
        self.label = label
        self._should_break = False
        self._should_continue = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def break_(self):
        """Exit this block."""
        self._should_break = True
        return True

    def continue_(self):
        """Continue to next iteration (for loops)."""
        self._should_continue = True
        return True


class Loop:
    """
    WASM loop control flow abstraction.

    Usage:
        for _ in Loop():
            if done:
                break
            process()
    """

    def __init__(self, max_iter: int = 1000000):
        self.max_iter = max_iter

    def __iter__(self):
        for _ in range(self.max_iter):
            yield
        raise RuntimeError("Loop exceeded max iterations")


def block_switch(value: int, cases: dict, default: Callable = None):
    """
    WASM br_table abstraction.

    Usage:
        block_switch(state, {
            0: handle_idle,
            1: handle_moving,
            2: handle_attacking,
        }, default=handle_unknown)
    """
    handler = cases.get(value, default)
    if handler:
        return handler()
    return None


# =============================================================================
# Entity Operations
# =============================================================================

def get_entity_ptr(entity_id: int) -> int:
    """Get pointer to entity by ID."""
    return load32(ENTITIES) + (entity_id * ENTITY_STRIDE)


def get_entity_field(entity_id: int, offset: int) -> int:
    """Get entity field value."""
    return load32(get_entity_ptr(entity_id) + offset)


def set_entity_field(entity_id: int, offset: int, value: int):
    """Set entity field value."""
    store32(get_entity_ptr(entity_id) + offset, value)


def iter_entities(start: int = 0, count: int = None) -> Iterator[int]:
    """
    Iterate over entity IDs.

    Usage:
        for entity_id in iter_entities():
            hp = get_entity_field(entity_id, 24)
    """
    if count is None:
        count = load32(9213808)  # Entity count address

    base = load32(ENTITIES)
    for i in range(start, count):
        yield i


def iter_entity_ptrs(start: int = 0, count: int = None) -> Iterator[int]:
    """Iterate over entity pointers."""
    if count is None:
        count = load32(9213808)

    base = load32(ENTITIES)
    for i in range(start, count):
        yield base + (i * ENTITY_STRIDE)


def find_entity(predicate: Callable[[int], bool]) -> Optional[int]:
    """Find first entity matching predicate."""
    for entity_id in iter_entities():
        if predicate(entity_id):
            return entity_id
    return None


def filter_entities(predicate: Callable[[int], bool]) -> List[int]:
    """Get all entities matching predicate."""
    return [eid for eid in iter_entities() if predicate(eid)]


# =============================================================================
# Entity Field Helpers
# =============================================================================

# Entity field offsets
class EntityField:
    ID = 0
    TYPE_ID = 4
    OWNER = 8
    X = 12
    Y = 16
    Z = 20
    HP = 24
    MAX_HP = 28
    STATE = 32
    ACTION = 36
    TARGET_ID = 40
    TARGET_X = 44
    TARGET_Y = 48
    SPEED = 52
    ATTACK = 56
    DEFENSE = 60
    RANGE = 64
    VISION = 68
    SELECTED = 72
    GROUP = 76
    ANIMATION = 80
    FRAME = 84
    DIRECTION = 88
    FLAGS = 92
    SUB_STATE = 122


def entity_hp(entity_ptr: int) -> int:
    return load32(entity_ptr + EntityField.HP)


def entity_max_hp(entity_ptr: int) -> int:
    return load32(entity_ptr + EntityField.MAX_HP)


def entity_state(entity_ptr: int) -> int:
    return load32(entity_ptr + EntityField.STATE)


def entity_action(entity_ptr: int) -> int:
    return load32(entity_ptr + EntityField.ACTION)


def entity_owner(entity_ptr: int) -> int:
    return load32(entity_ptr + EntityField.OWNER)


def entity_type_id(entity_ptr: int) -> int:
    return load32(entity_ptr + EntityField.TYPE_ID)


def entity_x(entity_ptr: int) -> int:
    return load32(entity_ptr + EntityField.X)


def entity_y(entity_ptr: int) -> int:
    return load32(entity_ptr + EntityField.Y)


def set_entity_hp(entity_ptr: int, value: int):
    store32(entity_ptr + EntityField.HP, value)


def set_entity_state(entity_ptr: int, value: int):
    store32(entity_ptr + EntityField.STATE, value)


def set_entity_action(entity_ptr: int, value: int):
    store32(entity_ptr + EntityField.ACTION, value)


# =============================================================================
# Player Operations
# =============================================================================

def get_player_ptr(player_id: int) -> int:
    """Get pointer to player by ID."""
    return load32(PLAYERS) + (player_id * PLAYER_STRIDE)


class PlayerField:
    ID = 0
    TEAM = 4
    GOLD = 8
    WOOD = 12
    FOOD = 16
    STONE = 20
    POPULATION = 24
    MAX_POP = 28
    SCORE = 32
    KILLS = 36
    DEATHS = 40


def player_gold(player_ptr: int) -> int:
    return load32(player_ptr + PlayerField.GOLD)


def player_wood(player_ptr: int) -> int:
    return load32(player_ptr + PlayerField.WOOD)


def player_food(player_ptr: int) -> int:
    return load32(player_ptr + PlayerField.FOOD)


def player_stone(player_ptr: int) -> int:
    return load32(player_ptr + PlayerField.STONE)


def add_player_gold(player_ptr: int, amount: int):
    store32(player_ptr + PlayerField.GOLD,
            load32(player_ptr + PlayerField.GOLD) + amount)


def add_player_wood(player_ptr: int, amount: int):
    store32(player_ptr + PlayerField.WOOD,
            load32(player_ptr + PlayerField.WOOD) + amount)


# =============================================================================
# Entity Type Operations
# =============================================================================

def get_entity_type_ptr(type_id: int) -> int:
    """Get pointer to entity type definition."""
    return ENTITY_TYPES + (type_id * ENTITY_TYPE_STRIDE)


class EntityTypeField:
    ID = 0
    NAME_PTR = 4
    CATEGORY = 8
    BASE_HP = 12
    BASE_ATTACK = 16
    BASE_DEFENSE = 20
    BASE_SPEED = 24
    BASE_RANGE = 28
    BASE_VISION = 32
    COST_GOLD = 36
    COST_WOOD = 40
    COST_FOOD = 44
    COST_STONE = 48
    BUILD_TIME = 52
    POP_COST = 56
    SPRITE_ID = 60
    ICON_ID = 64
    AI_TYPE = 188
    FORMATION = 264
    UPGRADE_PTR = 360


def type_base_hp(type_ptr: int) -> int:
    return load32(type_ptr + EntityTypeField.BASE_HP)


def type_cost_gold(type_ptr: int) -> int:
    return load32(type_ptr + EntityTypeField.COST_GOLD)


def type_ai_type(type_ptr: int) -> int:
    return load32(type_ptr + EntityTypeField.AI_TYPE)


# =============================================================================
# Selection Operations
# =============================================================================

SELECTION_LIST = 9215884
SELECTION_COUNT = 9215892


def get_selection_count() -> int:
    """Get number of selected entities."""
    return load32(SELECTION_COUNT)


def get_selected(index: int) -> int:
    """Get entity ID from selection."""
    list_ptr = load32(SELECTION_LIST)
    return load32(list_ptr + (index * 4))


def iter_selected() -> Iterator[int]:
    """Iterate over selected entity IDs."""
    count = get_selection_count()
    list_ptr = load32(SELECTION_LIST)
    for i in range(count):
        yield load32(list_ptr + (i * 4))


def clear_selection():
    """Clear selection."""
    store32(SELECTION_COUNT, 0)


# =============================================================================
# Array/List Helpers
# =============================================================================

def array_get(base: int, index: int, stride: int = 4) -> int:
    """Get value from array."""
    return load32(base + (index * stride))


def array_set(base: int, index: int, value: int, stride: int = 4):
    """Set value in array."""
    store32(base + (index * stride), value)


def array_iter(base_ptr_addr: int, count_addr: int, stride: int = 4) -> Iterator[int]:
    """Iterate over array values."""
    base = load32(base_ptr_addr)
    count = load32(count_addr)
    for i in range(count):
        yield load32(base + (i * stride))


def list_find(base_ptr_addr: int, count_addr: int, value: int, stride: int = 4) -> int:
    """Find value in list, return index or -1."""
    base = load32(base_ptr_addr)
    count = load32(count_addr)
    for i in range(count):
        if load32(base + (i * stride)) == value:
            return i
    return -1


def list_remove_at(base_ptr_addr: int, count_addr: int, index: int, stride: int = 4):
    """Remove element at index by shifting."""
    base = load32(base_ptr_addr)
    count = load32(count_addr)

    for i in range(index, count - 1):
        store32(base + (i * stride), load32(base + ((i + 1) * stride)))

    store32(count_addr, count - 1)


# =============================================================================
# State Machine
# =============================================================================

class StateMachine:
    """
    Entity state machine abstraction.

    Usage:
        sm = StateMachine(entity_ptr)
        sm.on_state(0, handle_idle)
        sm.on_state(1, handle_moving)
        sm.run()
    """

    def __init__(self, entity_ptr: int):
        self.entity_ptr = entity_ptr
        self.handlers = {}
        self.default_handler = None

    def on_state(self, state: int, handler: Callable):
        self.handlers[state] = handler
        return self

    def on_default(self, handler: Callable):
        self.default_handler = handler
        return self

    def run(self) -> Any:
        state = entity_state(self.entity_ptr)
        handler = self.handlers.get(state, self.default_handler)
        if handler:
            return handler(self.entity_ptr)
        return None


# =============================================================================
# Common Patterns
# =============================================================================

def for_each_in_range(center_x: int, center_y: int, range_: int,
                      callback: Callable[[int], None]):
    """
    Call callback for each entity in range.

    Common pattern in combat/AI code.
    """
    range_sq = range_ * range_

    for entity_ptr in iter_entity_ptrs():
        dx = entity_x(entity_ptr) - center_x
        dy = entity_y(entity_ptr) - center_y
        dist_sq = dx * dx + dy * dy

        if dist_sq <= range_sq:
            callback(entity_ptr)


def find_nearest(x: int, y: int, predicate: Callable[[int], bool] = None) -> Optional[int]:
    """Find nearest entity, optionally matching predicate."""
    nearest = None
    nearest_dist_sq = 0x7FFFFFFF

    for entity_ptr in iter_entity_ptrs():
        if predicate and not predicate(entity_ptr):
            continue

        dx = entity_x(entity_ptr) - x
        dy = entity_y(entity_ptr) - y
        dist_sq = dx * dx + dy * dy

        if dist_sq < nearest_dist_sq:
            nearest = entity_ptr
            nearest_dist_sq = dist_sq

    return nearest
