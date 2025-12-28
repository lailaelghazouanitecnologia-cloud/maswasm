"""
Function: $func162
Name: can_attack
Category: entity
Depth: 0
Status: done

Calls: none
Called by: 4 functions ($func200, $func919, $func351, $func921)

Determines if an entity can attack a target player.
Checks diplomacy status, unit types, visibility, and alliance flags.

Key addresses:
- 9142848: game timer
- 9142424: game state pointer
- 9561692: player data base
- 9568096: player type data base (stride 404)
- 9671128: entity array base

Player data stride: 286704
Player type stride: 404
Entity stride: 132
"""

from tzar._runtime import i32_load, i32_load8_u, i32_load16_u


# Global addresses
GAME_TIMER = 9142848
GAME_STATE_PTR = 9142424
PLAYER_DATA_BASE = 9561692
PLAYER_TYPE_BASE = 9568096
ENTITY_ARRAY = 9671128

# Strides
PLAYER_DATA_STRIDE = 286704
PLAYER_TYPE_STRIDE = 404
ENTITY_STRIDE = 132


def can_attack(entity_ptr: int, target_player: int, action_type: int, target_entity_idx: int) -> int:
    """
    Check if entity can attack a target player.

    Args:
        entity_ptr: Pointer to attacking entity
        target_player: Target player index
        action_type: Type of action (4-12 valid range)
        target_entity_idx: Target entity index

    Returns:
        1 if can attack, 0 otherwise
    """
    # Check game timer limit
    game_state = i32_load(GAME_STATE_PTR)
    if i32_load(GAME_TIMER) < i32_load(game_state, offset=72) * 2400:
        return 0

    # Check if attacker is of specific type
    if i32_load(entity_ptr, offset=56) == 1:
        owner = i32_load8_u(entity_ptr, offset=122)
        player_type = PLAYER_TYPE_BASE + owner * PLAYER_TYPE_STRIDE
        if i32_load(player_type, offset=268) == 1:
            return 0

    # Check if target is special neutral player
    if i32_load(38564) == target_player:
        return 0

    # Check action type (4-12 valid, 14 invalid)
    if action_type < 4 or action_type > 12:
        if action_type == 14:
            return 0
        # Continue with other checks
    else:
        if target_entity_idx == 0:
            return 0
        # Position-based checks
        entity_array = i32_load(ENTITY_ARRAY)
        target_entity = entity_array + target_entity_idx * ENTITY_STRIDE
        owner = i32_load16_u(target_entity, offset=110)
        player_data = i32_load(PLAYER_DATA_BASE) + owner * PLAYER_DATA_STRIDE

        # Check position tolerance
        expected_x = i32_load(player_data, offset=283872)
        if expected_x == 0:
            return 0

        actual_x = i32_load16_u(entity_array + target_entity_idx * ENTITY_STRIDE, offset=112)
        diff = abs(actual_x - expected_x)
        if diff > 30:
            return 0

        expected_y = i32_load(player_data, offset=283876)
        actual_y = i32_load16_u(entity_array + target_entity_idx * ENTITY_STRIDE, offset=114)
        diff = abs(actual_y - expected_y)
        if diff >= 31:
            return 0

        return 1

    target_type = PLAYER_TYPE_BASE + target_player * PLAYER_TYPE_STRIDE
    diplo_type = i32_load(target_type, offset=264)
    attacker_owner = i32_load8_u(entity_ptr, offset=122)

    # Check if target is ally type
    if i32_load(target_type, offset=188) != 55:
        if diplo_type == 1 and i32_load(38500) != target_player:
            return 0

    # Check if target is spectator type
    if diplo_type == 4:
        attacker_type = PLAYER_TYPE_BASE + attacker_owner * PLAYER_TYPE_STRIDE
        if i32_load(attacker_type, offset=224) == 1:
            return 1

    # Check ally list
    attacker_type = PLAYER_TYPE_BASE + attacker_owner * PLAYER_TYPE_STRIDE
    if i32_load(attacker_type, offset=272) == 0:
        if i32_load(38648) != attacker_owner:
            if i32_load(target_type, offset=208) == 2:
                return 1

    # Check special player flags
    if i32_load(38564) == target_player:
        if not i32_load8_u(attacker_type, offset=334):
            if i32_load(attacker_type, offset=268) == 2:
                return 1

    # Check player-specific flags
    if attacker_owner == i32_load(38728) or attacker_owner == i32_load(38996):
        if diplo_type == 0 and i32_load(target_type, offset=268) != 2:
            return 1

    # Check blocking flags
    if i32_load8_u(attacker_type, offset=379):
        return 1

    # Check ally array
    ally_array = i32_load(attacker_type, offset=24)
    if ally_array == 0:
        return 1

    ally_count = i32_load(attacker_type, offset=364)
    if ally_count == 0:
        return 1

    for i in range(ally_count):
        if i32_load(ally_array + i * 4) == target_player:
            return 1

    return 0


# Alias for WASM function name
func162 = can_attack
