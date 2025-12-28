"""
Tzar Engine - Core module (part 4).
Auto-generated from WebAssembly.
"""
from tzar.runtime import (
    load32, load64, load8u, load8s, load16u, load16s,
    loadf32, loadf64,
    store32, store64, store8, store16, storef32, storef64,
    atomic_load, atomic_store,
    i32, i64, u32, u64, f32,
    rotl, rotr, clz, ctz, popcnt,
    sqrt, abs, ceil, floor, trunc,
    G, mem_size, mem_grow, call_table,
)

from tzar.core.templates import (
    ENTITIES, PLAYERS, ENTITY_TYPES,
    EntityField, PlayerField, EntityTypeField,
    get_entity_ptr, get_player_ptr, get_entity_type_ptr,
    entity_hp, entity_state, entity_action, entity_owner,
    entity_x, entity_y, entity_type_id,
    iter_entities, iter_entity_ptrs,
)

# Known addresses
GAME_STATE = 9142424
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892
HEAP_FREELIST = 9690464
HEAP_TREE = 9690468
FREE_SIZE = 9690472
HEAP_TOTAL = 9690476
HEAP_BASE = 9690480
HEAP_TOP = 9690484
HEAP_END = 9690488
ALLOC_COUNT = 9690496
MEM_FLAGS = 9690908
MEM_MUTEX = 9690912
ALLOC_HANDLER = 9690984

class Unreachable(Exception):
    pass

# ----------------------------------------------------------
# $func880
# ----------------------------------------------------------
def func880(arg0, arg1, arg2):
    while True:  # $label0
        v7 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v3 = load32(59164)
        v4 = load32(PLAYERS)
        arg0 = 1
        while True:  # $label1
            while True:  # $label2
                v5 = (v4 + (arg0 * 286704))
                if (load32((v4 + (arg0 * 286704)) + 284616) == v3):
                    break
                if (load32(v5 + 284628) == v3):
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v7):
                    continue
                break
            v3 = 0
            break
            break
        if not arg2:
            v3 = 1
            break
        v4 = load32(arg1)
        v8 = load32(9671136)
        v6 = ((u32(load32(arg1)) < u32(3)) | (u32(v4) >= u32(load32(9671136))))
        v3 = 0
        if not load8u(9147152):
            v5 = 0
            if v6:
                break
            v6 = load32(9215884)
            v9 = load32(9143008)
            v10 = load32(ENTITIES)
            while True:  # $label3
                v4 = (v10 + (v4 * 132))
                if not load8u((v9 + ((v7 * load16u((v10 + (v4 * 132)) + 110)) + arg0))):
                    break
                if (load32((v6 + (load32(v4 + 44) << 4)) + 4) == 20):
                    break
                if (load8u(v4 + 127) == 6):
                    break
                v5 = (v5 + 1)
                v3 = (u32((v5 + 1)) >= u32(arg2))
                if (arg2 == v5):
                    break
                v4 = load32((arg1 + (v5 << 2)))
                if (u32(load32((arg1 + (v5 << 2)))) < u32(3)):
                    break
                if (u32(v4) < u32(v8)):
                    continue
                break
            break
        if v6:
            break
        v4 = (arg2 - 1)
        arg0 = 0
        while True:  # $label5
            while True:  # $label4
                v3 = (arg0 + 1)
                if (arg0 == v4):
                    break
                v5 = load32((arg1 + (v3 << 2)))
                if (u32(load32((arg1 + (v3 << 2)))) < u32(3)):
                    break
                arg0 = v3
                if (u32(v5) < u32(v8)):
                    continue
                break
            break
        v3 = (u32(arg2) <= u32(v3))
        break
    return v3

# ----------------------------------------------------------
# $func881
# ----------------------------------------------------------
def func881(arg0, arg1, arg2):
    while True:  # $label0
        v7 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v3 = load32(59164)
        v4 = load32(PLAYERS)
        arg0 = 1
        while True:  # $label1
            while True:  # $label2
                v5 = (v4 + (arg0 * 286704))
                if (load32((v4 + (arg0 * 286704)) + 284616) == v3):
                    break
                if (load32(v5 + 284628) == v3):
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v7):
                    continue
                break
            v3 = 0
            break
            break
        if not arg2:
            v3 = 1
            break
        v4 = load32(arg1)
        v8 = load32(9671136)
        v6 = ((u32(load32(arg1)) < u32(3)) | (u32(v4) >= u32(load32(9671136))))
        v3 = 0
        if not load8u(9147152):
            v5 = 0
            if v6:
                break
            v9 = load32(9215884)
            v10 = load32(9143008)
            v6 = load32(ENTITIES)
            while True:  # $label3
                v4 = (v6 + (load32((v6 + (v4 * 132)) + 36) * 132))
                if not load8u((v10 + ((v7 * load16u((v6 + (load32((v6 + (v4 * 132)) + 36) * 132)) + 110)) + arg0))):
                    break
                if (load32((v9 + (load32(v4 + 44) << 4)) + 4) == 20):
                    break
                if (load8u(v4 + 127) == 6):
                    break
                v5 = (v5 + 1)
                v3 = (u32((v5 + 1)) >= u32(arg2))
                if (arg2 == v5):
                    break
                v4 = load32((arg1 + (v5 << 2)))
                if (u32(load32((arg1 + (v5 << 2)))) < u32(3)):
                    break
                if (u32(v4) < u32(v8)):
                    continue
                break
            break
        if v6:
            break
        v4 = (arg2 - 1)
        arg0 = 0
        while True:  # $label5
            while True:  # $label4
                v3 = (arg0 + 1)
                if (arg0 == v4):
                    break
                v5 = load32((arg1 + (v3 << 2)))
                if (u32(load32((arg1 + (v3 << 2)))) < u32(3)):
                    break
                arg0 = v3
                if (u32(v5) < u32(v8)):
                    continue
                break
            break
        v3 = (u32(arg2) <= u32(v3))
        break
    return v3

# ----------------------------------------------------------
# $func883
# ----------------------------------------------------------
def func883(arg0, arg1, arg2):
    while True:  # $label0
        v3 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        arg0 = load32(59164)
        v4 = load32(PLAYERS)
        arg2 = 1
        while True:  # $label1
            while True:  # $label2
                v5 = (v4 + (arg2 * 286704))
                if (load32((v4 + (arg2 * 286704)) + 284616) == arg0):
                    break
                if (load32(v5 + 284628) == arg0):
                    break
                arg2 = (arg2 + 1)
                if ((arg2 + 1) != v3):
                    continue
                break
            return 0
            break
        if load8u(9147152):
            break
        arg2 = load32(ENTITIES)
        arg1 = load32((arg2 + (load32(arg1) * 132)) + 36)
        if not load8u((load32(9143008) + (arg2 + (v3 * load16u(entities[load32((arg2 + (load32(arg1)] + 110))))):
            break
        arg1 = (arg2 + (arg1 * 132))
        if (load32((load32(9215884) + (load32((arg2 + (arg1 * 132)) + 44) << 4)) + 4) == 20):
            break
        break
    return (load8u(arg1 + 127) != 6)

# ----------------------------------------------------------
# $func886
# ----------------------------------------------------------
def func886(arg0, arg1, arg2):
    arg2 = load32(arg0 + 8)
    v3 = load32(arg0 + 4)
    v4 = load32(arg0)
    while True:  # $label0
        if load8u(9147210):
            arg0 = 0
            v5 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            arg1 = load32(59164)
            v6 = load32(PLAYERS)
            arg0 = 1
            while True:  # $label1
                v7 = (v6 + (arg0 * 286704))
                if (load32((v6 + (arg0 * 286704)) + 284616) == arg1):
                    break
                if (load32(v7 + 284628) == arg1):
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v5):
                    continue
                break
            arg0 = 0
            break
        arg0 = load32(CURRENT_PLAYER)
        break
    func414(v4, v3, arg2, arg0, 0)

# ----------------------------------------------------------
# $ud
# Export: ud
# ----------------------------------------------------------
def ud(arg0):
    """Export: ud"""
    while True:  # $label0
        v2 = load32(9143000)
        v3 = (not load32(9143000) & (arg0 < 0))
        if not (not load32(9143000) & (arg0 < 0)):
            break
        if (load32(9671124) != 1):
            break
        arg0 = 0
        while True:  # $label5
            while True:  # $label3
                while True:  # $label2
                    while True:  # $label1
                        # br_table load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 196)
                        break
                        break
                    store32(9671124, 1)
                    while True:  # $label4
                        v2 = (arg0 << 2)
                        v1 = ((load32(((arg0 << 2) + 1072)) * 132) + 9216080)
                        store32(((load32(((arg0 << 2) + 1072)) * 132) + 9216080) + 116, 0)
                        store32(v1 + 16, 0)
                        store16(v1 + 21, 0)
                        store64(v1 + 124, 0)
                        store32((v2 + 9263072), v1)
                        store8(v1 + 24, (u32(arg0) > u32(7)))
                        v1 = 28
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != 28):
                            continue
                        break
                    break
                    break
                store32(9671124, 1)
                while True:  # $label6
                    v2 = (arg0 << 2)
                    v1 = ((load32(((arg0 << 2) + 1312)) * 132) + 9216080)
                    store32(((load32(((arg0 << 2) + 1312)) * 132) + 9216080) + 116, 0)
                    store32(v1 + 16, 0)
                    store16(v1 + 21, 0)
                    store64(v1 + 124, 0)
                    store32((v2 + 9263072), v1)
                    store8(v1 + 24, (u32(arg0) > u32(7)))
                    v1 = 28
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != 28):
                        continue
                    break
                break
                break
            store32(9671124, 1)
            while True:  # $label7
                v2 = (arg0 << 2)
                v1 = ((load32(((arg0 << 2) + 1184)) * 132) + 9216080)
                store32(((load32(((arg0 << 2) + 1184)) * 132) + 9216080) + 116, 0)
                store32(v1 + 16, 0)
                store16(v1 + 21, 0)
                store64(v1 + 124, 0)
                store32((v2 + 9263072), v1)
                store8(v1 + 24, (u32(arg0) > u32(7)))
                v1 = 30
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != 30):
                    continue
                break
            break
        store32(9671120, v1)
        return func46(8, 1)
        break
    v1 = load32(9681836)
    while True:  # $label8
        v4 = load8u(9147141)
        if not load8u(9147141):
            break
        break
    v5 = load32(load32(entities[load32(9173808)].y) + 8)
    while True:  # $label9
        if v3:
            break
        arg0 = (arg0 + v2)
        if (u32(((arg0 + v2) * load32(9147120))) >= u32(v5)):
            break
        store32(9143000, arg0)
        if v1:
            func172(0)
            return (v1 if v1 else load32(9671120))
        if v4:
            Ya(1)
            return
        if load8u(9684768):
            a_b()
            return func57(load32(9143000))
        break
    return func46(0, 1)

# ----------------------------------------------------------
# $func889
# ----------------------------------------------------------
def func889(arg0, arg1):
    while True:  # $label0
        if (load8u(arg1 + 125) == 3):
            break
        while True:  # $label4
            while True:  # $label3
                while True:  # $label1
                    arg0 = load32(arg0 + 36)
                    if (load32(arg0 + 36) != 2147483646):
                        break
                    arg0 = 0
                    v2 = load32(PLAYER_COUNT)
                    if not load32(PLAYER_COUNT):
                        break
                    v3 = load32(9142420)
                    while True:  # $label2
                        if load32((v3 + (arg0 << 2))):
                            break
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != v2):
                            continue
                        break
                    arg0 = 2147483646
                    if (u32(v2) >= u32(2147483647)):
                        break
                    break
                    break
                if (arg0 == 2147483647):
                    store8(arg1 + 126, 2)
                    arg0 = 0
                    if not load32(PLAYER_COUNT):
                        break
                    v2 = 0
                    if load16u(arg1 + 110):
                        break
                    break
                if (u32(arg0) >= u32(load32(PLAYER_COUNT))):
                    break
                if (arg0 == load16u(arg1 + 110)):
                    break
                break
            v2 = 0
            if (load8u(arg1 + 126) != 2):
                break
            if load8u(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 332):
                break
            store8(arg1 + 126, 0)
            v2 = 1
            break
        func78(arg1, arg0, 0, 1)
        if (load8u(arg1 + 126) == 2):
            if (load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 264) != 2):
            func29(arg1, 1)
        if not v2:
            break
        func156(0, arg1, 500)
        break

# ----------------------------------------------------------
# $_
# Export: _
# ----------------------------------------------------------
def _(arg0, arg1):
    """Export: _"""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg0 = players[arg0]
    store8(players[arg0] + 283972, ((arg1 & 0xFFFFFFFF) >> 16))
    v3 = (arg0 + 283974)
    store8((arg0 + 283974), arg1)
    v4 = (arg0 + 283973)
    store8((arg0 + 283973), ((arg1 & 0xFFFFFFFF) >> 8))
    if load8u(9147210):
        store32(v2, load32(arg0 + 283908))
        store32(v2 + 4, ((load8u(v3) | (load8u(v4) << 8)) | (load8u((arg0 + 283972)) << 16)))
        store32(v2 + 8, load32(arg0 + 284608))
        store32(v2 + 12, load32(arg0 + 283960))
        func71(16, 0, 0, v2, 4, 1)
    G.global0 = (v2 + 16)

# ----------------------------------------------------------
# $func893
# ----------------------------------------------------------
def func893(arg0, arg1):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if not arg0:
            break
        if not load32(9213808):
            break
        arg0 = load8u(9142917)
        while True:  # $label1
            v2 = load32(9140320)
            if load32(9140320):
                if arg0:
                    break
                arg0 = load32(ENTITIES)
                arg0 = (arg0 + (v2 * 132))
                v2 = load32((arg0 + (v2 * 132)) + 36)
                v2 = entities[(load32((arg0 + (v2]
                arg0 = load8u(entities[(load32((arg0 + (v2].sub_state)
                v3 = (((load32(((load8u(entities[(load32((arg0 + (v2].sub_state) * 404) + ENTITY_TYPES) + 220) << 4) & 2147483632) + (load16u(v2 + 114) << 5))
                break
            if arg0:
                break
            arg0 = load32(ENTITIES)
            arg0 = (arg0 + (load32(9173808) * 132))
            v2 = load32((arg0 + (load32(9173808) * 132)) + 36)
            v2 = entities[(load32((arg0 + (load32(9173808)]
            arg0 = load8u(entities[(load32((arg0 + (load32(9173808)].sub_state)
            v3 = (((load32(((load8u(entities[(load32((arg0 + (load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 220) << 4) & 2147483632) + (load16u(v2 + 114) << 5))
            break
        v2 = (v2 + 112)
        arg0 = load32(((arg0 * 404) + ENTITY_TYPES) + 216)
        v2 = load16u(v2)
        store32(arg1 + 4, v3)
        store32(arg1, (((arg0 << 4) & 2147483632) + (v2 << 5)))
        break
    G.global0 = (arg1 + 16)
    return arg1

# ----------------------------------------------------------
# $func894
# ----------------------------------------------------------
def func894(arg0, arg1):
    v4 = entities[arg1]
    v12 = ((load32(38572) != load8u(entities[arg1].sub_state)) << 1)
    v10 = load32(v4 + 52)
    v4 = 0
    while True:  # $label0
        v2 = load32(9142440)
        # TODO: i32.div_u
        arg0 = load32(9142440)
        v8 = (arg0 - (load32(9142440) * v2))
        if (((arg0 - (load32(9142440) * v2)) | arg0) < 0):
            break
        v2 = load32(9142440)
        v6 = (arg0 if (u32(arg0) > u32(v8)) else v8)
        if (u32(load32(9142440)) <= u32((arg0 if (u32(arg0) > u32(v8)) else v8))):
            break
        v3 = load32(ENTITIES)
        v11 = entities[arg1]
        v5 = (v8 + 1)
        v9 = (arg0 + 1)
        arg1 = load32((load32(9142840) + (((v8 + 1) + ((arg0 + 1) * (v2 + 2))) << 2)))
        if (u32(load32((load32(9142840) + (((v8 + 1) + ((arg0 + 1) * (v2 + 2))) << 2)))) >= u32(3)):
            v4 = (v3 + (arg1 * 132))
            v2 = load8u((v3 + (arg1 * 132)) + 125)
            v7 = (((load8u((v3 + (arg1 * 132)) + 125) == 4) | (v2 == 14)) & (load32(v4 + 64) == 1))
            if (v2 != 10):
            if v7:
                break
            store32(59200, load32((v3 + (arg1 * 132)) + 28))
            v2 = load32(9142440)
            v4 = 1
        if (u32(v2) <= u32(v6)):
            break
        v3 = load32(9142840)
        arg1 = (v2 + 2)
        v6 = load32((load32(9142840) + ((v5 + ((v9 + (v2 + 2)) * arg1)) << 2)))
        if (u32(load32((load32(9142840) + ((v5 + ((v9 + (v2 + 2)) * arg1)) << 2)))) >= u32(3)):
            v3 = load32(ENTITIES)
            arg1 = entities[v6]
            v2 = load8u(entities[v6].unit_class)
            v7 = (((load8u(entities[v6].unit_class) == 4) | (v2 == 14)) & (load32(arg1 + 64) == 1))
            if (v2 != 10):
            if v7:
                break
            store32(((v4 << 2) + 59200), load32((v3 + (v6 * 132)) + 28))
            v4 = (v4 + 1)
            v3 = load32(9142840)
            v2 = load32(9142440)
            arg1 = (load32(9142440) + 2)
        while True:  # $label1
            if (load32((v3 + (((arg1 * v9) + v5) << 2))) != 1):
                break
            if (load32((v3 + ((((arg1 + v9) * arg1) + v5) << 2))) == 1):
                break
            v6 = 0
            v7 = load32(((load32(PLAYERS) + (load32(38560) << 2)) + 284636))
            if not load32(((load32(PLAYERS) + (load32(38560) << 2)) + 284636)):
                break
            v13 = load32(v7 + 8)
            if not load32(v7 + 8):
                break
            while True:  # $label3
                while True:  # $label2
                    arg1 = load32((load32(v7) + (v6 << 2)))
                    if not load32((load32(v7) + (v6 << 2))):
                        break
                    arg1 = entities[arg1]
                    v2 = load16u(entities[arg1].rally_y)
                    if (load16u(entities[arg1].rally_y) >= v8):
                        break
                    v3 = load16u(arg1 + 114)
                    if (load16u(arg1 + 114) >= arg0):
                        break
                    v14 = ((load32(38560) * 404) + ENTITY_TYPES)
                    if (u32((v2 + load32(((load32(38560) * 404) + ENTITY_TYPES) + 216))) <= u32(v8)):
                        break
                    if (u32((load32(v14 + 220) + v3)) <= u32(arg0)):
                        break
                    v13 = load32(v7 + 8)
                    break
                v6 = (v6 + 1)
                if (u32((v6 + 1)) < u32(v13)):
                    continue
                break
            v2 = load32(9142440)
            arg1 = (load32(9142440) + 2)
            v3 = load32(9142840)
            break
        if not v12:
            break
        if (load32((v3 + ((((arg1 + v9) * arg1) + v5) << 2))) == 1):
            break
        arg1 = ((v12 << 1) | 1)
        v9 = (((((v12 << 1) | 1) * arg1) << 1) - 2)
        if not (((((v12 << 1) | 1) * arg1) << 1) - 2):
            break
        v6 = 0
        while True:  # $label8
            while True:  # $label4
                v3 = (v6 << 2)
                arg1 = (load32((((v6 << 2) | 4) + 8611904)) + arg0)
                if (u32(v2) <= u32((load32((((v6 << 2) | 4) + 8611904)) + arg0))):
                    break
                v5 = (load32((v3 + 8611904)) + v8)
                if (u32(v2) <= u32((load32((v3 + 8611904)) + v8))):
                    break
                if ((arg1 | v5) < 0):
                    break
                while True:  # $label5
                    v3 = load32(9142840)
                    v7 = (v5 + 1)
                    v13 = (arg1 + 1)
                    arg1 = load32((load32(9142840) + (((v5 + 1) + ((arg1 + 1) * (v2 + 2))) << 2)))
                    if (u32(load32((load32(9142840) + (((v5 + 1) + ((arg1 + 1) * (v2 + 2))) << 2)))) < u32(3)):
                        break
                    v5 = entities[arg1]
                    if (load8u(entities[arg1].unit_class) == 10):
                        break
                    arg1 = ((load8u(v5 + 122) * 404) + ENTITY_TYPES)
                    if (load32(((load8u(v5 + 122) * 404) + ENTITY_TYPES) + 188) != 55):
                        if (load32(arg1 + 264) == 1):
                            break
                    if v4:
                        v14 = load32(v5 + 28)
                        arg1 = 0
                        while True:  # $label6
                            if (load32(((arg1 << 2) + 59200)) == v14):
                                break
                            arg1 = (arg1 + 1)
                            if ((arg1 + 1) != v4):
                                continue
                            break
                    # TODO: i32.div_u
                    arg1 = v12
                    if not v12:
                        break
                    store32(((v4 << 2) + 59200), load32(v5 + 28))
                    v4 = (v4 + 1)
                    v3 = load32(9142840)
                    v2 = load32(9142440)
                    break
                arg1 = (v2 + 2)
                arg1 = load32((v3 + ((v7 + ((v13 + (v2 + 2)) * arg1)) << 2)))
                if (u32(load32((v3 + ((v7 + ((v13 + (v2 + 2)) * arg1)) << 2)))) < u32(3)):
                    break
                v3 = entities[arg1]
                if (load8u(entities[arg1].unit_class) == 10):
                    break
                arg1 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                if (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 188) != 55):
                    if (load32(arg1 + 264) == 1):
                        break
                if v4:
                    v5 = load32(v3 + 28)
                    arg1 = 0
                    while True:  # $label7
                        if (load32(((arg1 << 2) + 59200)) == v5):
                            break
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != v4):
                            continue
                        break
                # TODO: i32.div_u
                arg1 = v12
                if not v12:
                    break
                store32(((v4 << 2) + 59200), load32(v3 + 28))
                v4 = (v4 + 1)
                v2 = load32(9142440)
                break
            v6 = (v6 + 2)
            if (u32((v6 + 2)) < u32(v9)):
                continue
            break
        break

# ----------------------------------------------------------
# $func895
# ----------------------------------------------------------
def func895(arg0, arg1, param2):
    v6 = load32(ENTITIES)
    v10 = entities[arg1]
    v2 = load8u(entities[arg1].sub_state)
    while True:  # $label2
        v7 = (v6 + (arg0 * 132))
        if (load8u((v6 + (arg0 * 132)) + 125) == 1):
            v2 = ((v2 * 404) + ENTITY_TYPES)
            v12 = load32(((v2 * 404) + ENTITY_TYPES) + 220)
            v4 = load16u(v10 + 114)
            v5 = (load32(((v2 * 404) + ENTITY_TYPES) + 220) + load16u(v10 + 114))
            v14 = load32(v2 + 216)
            v10 = load16u(v10 + 112)
            v13 = (load32(v2 + 216) + load16u(v10 + 112))
            v2 = load16u(v7 + 114)
            while True:  # $label1
                while True:  # $label0
                    v3 = load16u(v7 + 112)
                    v15 = (u32(load16u(v7 + 112)) < u32(v10))
                    if (u32(load16u(v7 + 112)) < u32(v10)):
                        break
                    if (v3 >= v13):
                        break
                    if (u32(v2) < u32(v4)):
                        break
                    if (v2 >= v5):
                        break
                    v4 = ((v12 // 2) + v4)
                    v2 = (-1 if (v2 > v4) else (((v12 // 2) + v4) != v2))
                    v4 = ((v14 // 2) + v10)
                    break
                    break
                v2 = (1 if (u32(v2) < u32(v4)) else (-1 if (v2 >= v5) else 0))
                break
            v3 = (1 if v15 else (-1 if (v3 >= v13) else 0))
            v4 = 6
            v2 = (((v2 * 3) + v3) + 4)
            if (u32((((v2 * 3) + v3) + 4)) <= u32(8)):
                v4 = load8u((v2 + 10184))
            v2 = (v6 + (arg0 * 132))
            store8((v6 + (arg0 * 132)) + 124, v4)
            v3 = load32(((load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            if (load8u(v7 + 125) == 3):
                break
            v4 = load32(v2 + 44)
            if load32(v2 + 44):
                v7 = load32(9142848)
                v3 = load32(9215884)
                store32((load32(9215884) + (v4 << 4)) + 4, 54)
                store32((v3 + (load32(v2 + 44) << 4)) + 8, load32((v6 + (arg0 * 132)) + 28))
                store32((v3 + (load32(v2 + 44) << 4)) + 12, arg1)
                store32((v3 + (load32(v2 + 44) << 4)), (v7 + 40))
                return call_table(v3)
            store32(v2 + 44, ((Ua(1000, 54, load32((v6 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            return entities[load32(v2 + 28)]
        while True:  # $label3
            if (load8u(v10 + 125) != 3):
                v3 = load16u((v6 + (arg0 * 132)) + 110)
                v4 = load16u((v6 + (arg1 * 132)) + 110)
                if load8u((load32(9143004) + (load16u((v6 + (arg0 * 132)) + 110) + (load16u((v6 + (arg1 * 132)) + 110) * load32(PLAYER_COUNT))))):
                    break
            func29(v7, 1)
            return func37(v7, load32(((load8u(v2 + 122) * 72) + 9263856) + 16), 0.0, 0)
            break
        while True:  # $label6
            while True:  # $label5
                while True:  # $label4
                    if (v3 == v4):
                        v4 = load32((v6 + (arg1 * 132)) + 84)
                        break
                    func103(v10)
                    v3 = (v6 + (arg1 * 132))
                    v4 = load32((v6 + (arg1 * 132)) + 84)
                    if (u32(load32((v6 + (arg1 * 132)) + 84)) < u32(6)):
                        break
                    v2 = load8u(v10 + 122)
                    break
                v3 = -5
                v5 = (v6 + (arg1 * 132))
                v3 = (v3 + v4)
                store32((v6 + (arg1 * 132)) + 84, (v3 + v4))
                v2 = load32(((v2 * 404) + ENTITY_TYPES) + 112)
                if (u32(v3) <= u32(load32(((v2 * 404) + ENTITY_TYPES) + 112))):
                    break
                store32(v5 + 84, v2)
                while True:  # $label7
                    if not load32(v5 + 92):
                        break
                    if load32(9140316):
                        if (load32(9140320) != load32((v6 + (arg1 * 132)) + 28)):
                            break
                    break
                func29(v7, 1)
                return func28(1, 1)
                break
            store32(v3 + 84, 1)
            v13 = load32(PLAYER_COUNT)
            if load32(PLAYER_COUNT):
                # TODO: memory.fill
            while True:  # $label8
                v3 = ((v2 * 404) + ENTITY_TYPES)
                v20 = load32(((v2 * 404) + ENTITY_TYPES) + 216)
                v7 = (v6 + (arg0 * 132))
                v4 = load16u((v6 + (arg0 * 132)) + 112)
                v21 = (load32(((v2 * 404) + ENTITY_TYPES) + 216) + load16u((v6 + (arg0 * 132)) + 112))
                if ((load32(((v2 * 404) + ENTITY_TYPES) + 216) + load16u((v6 + (arg0 * 132)) + 112)) <= v4):
                    break
                v7 = load16u(v7 + 114)
                v22 = (load16u(v7 + 114) + load32(v3 + 220))
                if ((load16u(v7 + 114) + load32(v3 + 220)) <= v7):
                    break
                v14 = (v6 + (arg1 * 132))
                v15 = load32(9215884)
                v16 = load32(ENTITIES)
                v17 = load32(9142840)
                v19 = load32(9142440)
                v12 = (load32(9142440) + 2)
                v23 = ((load32(9142440) + 2) << 1)
                v24 = load32(((v2 * 404) + ENTITY_TYPES) + 372)
                v2 = v4
                while True:  # $label14
                    v25 = (v2 - v4)
                    v3 = v7
                    while True:  # $label13
                        v5 = 0
                        if load8u((v24 + (v25 + ((v3 - v7) * v20)))):
                            while True:  # $label12
                                while True:  # $label9
                                    v11 = (v5 << 3)
                                    v9 = (load32(((v5 << 3) + 8932)) + v3)
                                    if (u32(v19) <= u32((load32(((v5 << 3) + 8932)) + v3))):
                                        break
                                    v11 = (load32((v11 + 8928)) + v2)
                                    if (u32(v19) <= u32((load32((v11 + 8928)) + v2))):
                                        break
                                    if ((v9 | v11) < 0):
                                        break
                                    while True:  # $label10
                                        v11 = (v11 + 1)
                                        v9 = (v9 + 1)
                                        v8 = load32((v17 + (((v11 + 1) + ((v9 + 1) * v12)) << 2)))
                                        if (u32(load32((v17 + (((v11 + 1) + ((v9 + 1) * v12)) << 2)))) < u32(3)):
                                            break
                                        if (arg1 == v8):
                                            break
                                        v8 = (v16 + (v8 * 132))
                                        v18 = load16u((v16 + (v8 * 132)) + 110)
                                        if not load16u((v16 + (v8 * 132)) + 110):
                                            break
                                        if (load8u(v8 + 123) != 54):
                                            break
                                        if (load32((v15 + (load32(v8 + 44) << 4)) + 12) != load32(v14 + 28)):
                                            break
                                        v8 = ((v18 << 2) + 59200)
                                        store32(((v18 << 2) + 59200), (load32(v8) + 1))
                                        break
                                    while True:  # $label11
                                        v8 = load32((v17 + ((v11 + ((v9 + v12) * v12)) << 2)))
                                        if (u32(load32((v17 + ((v11 + ((v9 + v12) * v12)) << 2)))) < u32(3)):
                                            break
                                        if (arg1 == v8):
                                            break
                                        v8 = (v16 + (v8 * 132))
                                        v18 = load16u((v16 + (v8 * 132)) + 110)
                                        if not load16u((v16 + (v8 * 132)) + 110):
                                            break
                                        if (load8u(v8 + 123) != 54):
                                            break
                                        if (load32((v15 + (load32(v8 + 44) << 4)) + 12) != load32(v14 + 28)):
                                            break
                                        v8 = ((v18 << 2) + 59200)
                                        store32(((v18 << 2) + 59200), (load32(v8) + 1))
                                        break
                                    v9 = load32((v17 + ((v11 + ((v9 + v23) * v12)) << 2)))
                                    if (u32(load32((v17 + ((v11 + ((v9 + v23) * v12)) << 2)))) < u32(3)):
                                        break
                                    if (arg1 == v9):
                                        break
                                    v9 = (v16 + (v9 * 132))
                                    v11 = load16u((v16 + (v9 * 132)) + 110)
                                    if not load16u((v16 + (v9 * 132)) + 110):
                                        break
                                    if (load8u(v9 + 123) != 54):
                                        break
                                    if (load32((v15 + (load32(v9 + 44) << 4)) + 12) != load32(v14 + 28)):
                                        break
                                    v9 = ((v11 << 2) + 59200)
                                    store32(((v11 << 2) + 59200), (load32(v9) + 1))
                                    break
                                v5 = (v5 + 1)
                                if ((v5 + 1) != 8):
                                    continue
                                break
                        v3 = (v3 + 1)
                        if ((v3 + 1) != v22):
                            continue
                        break
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v21):
                        continue
                    break
                break
            if not v13:
                break
            v4 = 0
            v5 = 0
            v2 = 0
            if (u32(v13) >= u32(4)):
                v7 = (v13 & -4)
                v3 = 0
                while True:  # $label15
                    v12 = (v5 | 3)
                    v14 = (v5 | 2)
                    v15 = (v5 | 1)
                    v2 = (v5 if (u32(load32(((v5 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else v2)
                    v2 = ((v5 | 1) if (u32(load32(((v15 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else (v5 if (u32(load32(((v5 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else v2))
                    v2 = ((v5 | 2) if (u32(load32(((v14 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else ((v5 | 1) if (u32(load32(((v15 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else (v5 if (u32(load32(((v5 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else v2)))
                    v2 = ((v5 | 3) if (u32(load32(((v12 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else ((v5 | 2) if (u32(load32(((v14 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else ((v5 | 1) if (u32(load32(((v15 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else (v5 if (u32(load32(((v5 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else v2))))
                    v5 = (v5 + 4)
                    v3 = (v3 + 4)
                    if ((v3 + 4) != v7):
                        continue
                    break
            v3 = (v13 & 3)
            if (v13 & 3):
                while True:  # $label16
                    v2 = (v5 if (u32(load32(((v5 << 2) + 59200))) > u32(load32(((v2 << 2) + 59200)))) else v2)
                    v5 = (v5 + 1)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v3):
                        continue
                    break
            if not v2:
                break
            func78(v10, v2, 1, 1)
            if not load32((v6 + (arg1 * 132)) + 92):
                break
            v2 = load8u(9147141)
            if load32(9140316):
                if (load32(9140320) != load32((v6 + (arg1 * 132)) + 28)):
                    break
            break
        while True:  # $label17
            if not load32((v6 + (arg1 * 132)) + 92):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v6 + (arg1 * 132)) + 28)):
                    break
            break
        store32((load32(9215884) + (load32((v6 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
        break
    return func28(1, 1)

# ----------------------------------------------------------
# $func896
# ----------------------------------------------------------
def func896(arg0, arg1, arg2, arg3, arg4):
    arg2 = 1
    while True:  # $label0
        while True:  # $label1
            arg3 = load32(ENTITIES)
            arg1 = load32(arg1)
            arg4 = entities[load32(arg1)]
            # br_table (load8u(entities[load32(arg1)].unit_class) - 4)
            break
            break
        arg4 = ((load8u(arg4 + 122) * 404) + ENTITY_TYPES)
        if (load32(((load8u(arg4 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
            break
        if not load32(arg4 + 112):
            break
        if (u32(load32(9142848)) <= u32((load32(load32(GAME_STATE) + 72) * 2400))):
            break
        arg0 = load16u((arg3 + (arg0 * 132)) + 110)
        arg1 = load16u((arg3 + (arg1 * 132)) + 110)
        arg2 = (not load8u((load32(9143004) + (load16u((arg3 + (arg0 * 132)) + 110) + (load16u((arg3 + (arg1 * 132)) + 110) * load32(PLAYER_COUNT))))) & (arg0 != arg1))
        break
    return arg2

# ----------------------------------------------------------
# $func897
# ----------------------------------------------------------
def func897(arg0, arg1):
    while True:  # $label0
        v7 = load32(ENTITIES)
        v15 = entities[arg0]
        if (load8u(entities[arg0].unit_class) == 3):
            break
        v9 = load8u(v15 + 122)
        while True:  # $label1
            v18 = load16u(v15 + 110)
            if not load16u(v15 + 110):
                break
            if load8u(((v9 * 404) + ENTITY_TYPES) + 332):
                break
            arg0 = (v7 + (arg0 * 132))
            if (load8u((v7 + (arg0 * 132)) + 126) != 2):
                break
            store8(arg0 + 126, 0)
            break
            break
        v4 = ((v9 * 404) + ENTITY_TYPES)
        v10 = load32(((v9 * 404) + ENTITY_TYPES) + 216)
        arg1 = (v7 + (arg0 * 132))
        v3 = load16u((v7 + (arg0 * 132)) + 114)
        arg1 = load16u(arg1 + 112)
        while True:  # $label4
            while True:  # $label11
                while True:  # $label2
                    if not load8u(9216060):
                        break
                    if load32(v4 + 264):
                        break
                    v4 = load32(PLAYERS)
                    while True:  # $label3
                        v8 = load32(9142840)
                        v13 = (arg1 + 2)
                        v11 = (load32(9142440) + 2)
                        v14 = (v3 + (load32(9142440) + 2))
                        v16 = (((v3 + (load32(9142440) + 2)) + 1) * v11)
                        v2 = load32((load32(9142840) + (((arg1 + 2) + (((v3 + (load32(9142440) + 2)) + 1) * v11)) << 2)))
                        if (u32((load32((load32(9142840) + (((arg1 + 2) + (((v3 + (load32(9142440) + 2)) + 1) * v11)) << 2))) - 3)) > u32(-5)):
                            break
                        v10 = (v7 + (v2 * 132))
                        v3 = load16u((v7 + (v2 * 132)) + 110)
                        if not load16u((v7 + (v2 * 132)) + 110):
                            break
                        if (u32(load32((((v4 + (v3 * 286704)) + (v9 << 2)) + 281808))) > u32(1500)):
                            break
                        arg1 = (v10 + 110)
                        break
                        break
                    while True:  # $label5
                        v10 = (v11 * v14)
                        v2 = load32((v8 + ((v13 + (v11 * v14)) << 2)))
                        if (u32((load32((v8 + ((v13 + (v11 * v14)) << 2))) - 3)) > u32(-5)):
                            break
                        v5 = (v7 + (v2 * 132))
                        v3 = load16u((v7 + (v2 * 132)) + 110)
                        if not load16u((v7 + (v2 * 132)) + 110):
                            break
                        if (u32(load32((((v4 + (v3 * 286704)) + (v9 << 2)) + 281808))) >= u32(1501)):
                            break
                        arg1 = (v5 + 110)
                        break
                        break
                    while True:  # $label6
                        v5 = (arg1 + 1)
                        v2 = load32((v8 + (((arg1 + 1) + v10) << 2)))
                        if (u32((load32((v8 + (((arg1 + 1) + v10) << 2))) - 3)) > u32(-5)):
                            break
                        v12 = (v7 + (v2 * 132))
                        v3 = load16u((v7 + (v2 * 132)) + 110)
                        if not load16u((v7 + (v2 * 132)) + 110):
                            break
                        if (u32(load32((((v4 + (v3 * 286704)) + (v9 << 2)) + 281808))) >= u32(1501)):
                            break
                        arg1 = (v12 + 110)
                        break
                        break
                    while True:  # $label7
                        v2 = load32((v8 + ((arg1 + v10) << 2)))
                        if (u32((load32((v8 + ((arg1 + v10) << 2))) - 3)) > u32(-5)):
                            break
                        v10 = (v7 + (v2 * 132))
                        v3 = load16u((v7 + (v2 * 132)) + 110)
                        if not load16u((v7 + (v2 * 132)) + 110):
                            break
                        if (u32(load32((((v4 + (v3 * 286704)) + (v9 << 2)) + 281808))) >= u32(1501)):
                            break
                        arg1 = (v10 + 110)
                        break
                        break
                    while True:  # $label8
                        v2 = load32((v8 + ((arg1 + v16) << 2)))
                        if (u32((load32((v8 + ((arg1 + v16) << 2))) - 3)) > u32(-5)):
                            break
                        v10 = (v7 + (v2 * 132))
                        v3 = load16u((v7 + (v2 * 132)) + 110)
                        if not load16u((v7 + (v2 * 132)) + 110):
                            break
                        if (u32(load32((((v4 + (v3 * 286704)) + (v9 << 2)) + 281808))) >= u32(1501)):
                            break
                        arg1 = (v10 + 110)
                        break
                        break
                    while True:  # $label9
                        arg1 = ((v14 + 2) * v11)
                        v2 = load32((v8 + ((arg1 + ((v14 + 2) * v11)) << 2)))
                        if (u32((load32((v8 + ((arg1 + ((v14 + 2) * v11)) << 2))) - 3)) > u32(-5)):
                            break
                        v11 = (v7 + (v2 * 132))
                        v3 = load16u((v7 + (v2 * 132)) + 110)
                        if not load16u((v7 + (v2 * 132)) + 110):
                            break
                        if (u32(load32((((v4 + (v3 * 286704)) + (v9 << 2)) + 281808))) >= u32(1501)):
                            break
                        arg1 = (v11 + 110)
                        break
                        break
                    while True:  # $label10
                        v2 = load32((v8 + ((arg1 + v5) << 2)))
                        if (u32((load32((v8 + ((arg1 + v5) << 2))) - 3)) > u32(-5)):
                            break
                        v11 = (v7 + (v2 * 132))
                        v3 = load16u((v7 + (v2 * 132)) + 110)
                        if not load16u((v7 + (v2 * 132)) + 110):
                            break
                        if (u32(load32((((v4 + (v3 * 286704)) + (v9 << 2)) + 281808))) >= u32(1501)):
                            break
                        arg1 = (v11 + 110)
                        break
                        break
                    v2 = load32((v8 + ((arg1 + v13) << 2)))
                    if (u32((load32((v8 + ((arg1 + v13) << 2))) - 3)) > u32(-5)):
                        break
                    arg1 = (v7 + (v2 * 132))
                    v3 = load16u((v7 + (v2 * 132)) + 110)
                    if not load16u((v7 + (v2 * 132)) + 110):
                        break
                    if (u32(load32((((v4 + (v3 * 286704)) + (v9 << 2)) + 281808))) >= u32(1501)):
                        break
                    arg1 = (arg1 + 110)
                    break
                    break
                v11 = load32(PLAYER_COUNT)
                if load32(PLAYER_COUNT):
                    # TODO: memory.fill
                while True:  # $label12
                    v19 = (arg1 + v10)
                    if ((arg1 + v10) <= arg1):
                        break
                    v20 = (load32(((v9 * 404) + ENTITY_TYPES) + 220) + v3)
                    if ((load32(((v9 * 404) + ENTITY_TYPES) + 220) + v3) <= v3):
                        break
                    v14 = load32(9142840)
                    v16 = load32(9142440)
                    v13 = (load32(9142440) + 2)
                    v21 = ((load32(9142440) + 2) << 1)
                    v22 = load32(((v9 * 404) + ENTITY_TYPES) + 372)
                    v4 = arg1
                    while True:  # $label24
                        v23 = (v4 - arg1)
                        v8 = v3
                        while True:  # $label23
                            v2 = 0
                            if load8u((v22 + (v23 + ((v8 - v3) * v10)))):
                                while True:  # $label22
                                    while True:  # $label13
                                        v12 = (v2 << 3)
                                        v5 = (load32(((v2 << 3) + 8932)) + v8)
                                        if (u32(v16) <= u32((load32(((v2 << 3) + 8932)) + v8))):
                                            break
                                        v12 = (load32((v12 + 8928)) + v4)
                                        if (u32(v16) <= u32((load32((v12 + 8928)) + v4))):
                                            break
                                        if ((v5 | v12) < 0):
                                            break
                                        while True:  # $label14
                                            v12 = (v12 + 1)
                                            v5 = (v5 + 1)
                                            v6 = load32((v14 + (((v12 + 1) + ((v5 + 1) * v13)) << 2)))
                                            if (u32(load32((v14 + (((v12 + 1) + ((v5 + 1) * v13)) << 2)))) < u32(3)):
                                                break
                                            if (arg0 == v6):
                                                break
                                            v6 = (v7 + (v6 * 132))
                                            v17 = load16u((v7 + (v6 * 132)) + 110)
                                            if not load16u((v7 + (v6 * 132)) + 110):
                                                break
                                            v6 = load8u(v6 + 122)
                                            if load32(((load8u(v6 + 122) * 404) + ENTITY_TYPES) + 264):
                                                break
                                            while True:  # $label15
                                                while True:  # $label16
                                                    # br_table (v6 + -64)
                                                    break
                                                    break
                                                if (v6 == 10):
                                                    break
                                                break
                                            v6 = ((v17 << 2) + 59200)
                                            store32(((v17 << 2) + 59200), (load32(v6) + 1))
                                            break
                                        while True:  # $label17
                                            v6 = load32((v14 + ((v12 + ((v5 + v13) * v13)) << 2)))
                                            if (u32(load32((v14 + ((v12 + ((v5 + v13) * v13)) << 2)))) < u32(3)):
                                                break
                                            if (arg0 == v6):
                                                break
                                            v6 = (v7 + (v6 * 132))
                                            v17 = load16u((v7 + (v6 * 132)) + 110)
                                            if not load16u((v7 + (v6 * 132)) + 110):
                                                break
                                            v6 = load8u(v6 + 122)
                                            if load32(((load8u(v6 + 122) * 404) + ENTITY_TYPES) + 264):
                                                break
                                            while True:  # $label18
                                                while True:  # $label19
                                                    # br_table (v6 + -64)
                                                    break
                                                    break
                                                if (v6 == 10):
                                                    break
                                                break
                                            v6 = ((v17 << 2) + 59200)
                                            store32(((v17 << 2) + 59200), (load32(v6) + 1))
                                            break
                                        v5 = load32((v14 + ((v12 + ((v5 + v21) * v13)) << 2)))
                                        if (u32(load32((v14 + ((v12 + ((v5 + v21) * v13)) << 2)))) < u32(3)):
                                            break
                                        if (arg0 == v5):
                                            break
                                        v5 = (v7 + (v5 * 132))
                                        v12 = load16u((v7 + (v5 * 132)) + 110)
                                        if not load16u((v7 + (v5 * 132)) + 110):
                                            break
                                        v5 = load8u(v5 + 122)
                                        if load32(((load8u(v5 + 122) * 404) + ENTITY_TYPES) + 264):
                                            break
                                        while True:  # $label20
                                            while True:  # $label21
                                                # br_table (v5 + -64)
                                                break
                                                break
                                            if (v5 == 10):
                                                break
                                            break
                                        v5 = ((v12 << 2) + 59200)
                                        store32(((v12 << 2) + 59200), (load32(v5) + 1))
                                        break
                                    v2 = (v2 + 1)
                                    if ((v2 + 1) != 8):
                                        continue
                                    break
                            v8 = (v8 + 1)
                            if ((v8 + 1) != v20):
                                continue
                            break
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v19):
                            continue
                        break
                    break
                if not v11:
                    break
                v3 = 0
                v2 = 0
                arg1 = 0
                if (u32(v11) >= u32(4)):
                    v8 = (v11 & -4)
                    v4 = 0
                    while True:  # $label25
                        v13 = (v2 | 3)
                        v14 = (v2 | 2)
                        v10 = (v2 | 1)
                        arg1 = (v2 if (u32(load32(((v2 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else arg1)
                        arg1 = ((v2 | 1) if (u32(load32(((v10 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else (v2 if (u32(load32(((v2 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else arg1))
                        arg1 = ((v2 | 2) if (u32(load32(((v14 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else ((v2 | 1) if (u32(load32(((v10 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else (v2 if (u32(load32(((v2 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else arg1)))
                        arg1 = ((v2 | 3) if (u32(load32(((v13 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else ((v2 | 2) if (u32(load32(((v14 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else ((v2 | 1) if (u32(load32(((v10 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else (v2 if (u32(load32(((v2 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else arg1))))
                        v2 = (v2 + 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v8):
                            continue
                        break
                v4 = (v11 & 3)
                if (v11 & 3):
                    while True:  # $label26
                        arg1 = (v2 if (u32(load32(((v2 << 2) + 59200))) > u32(load32(((arg1 << 2) + 59200)))) else arg1)
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        if ((v3 + 1) != v4):
                            continue
                        break
                if (arg1 == v18):
                    break
                if not arg1:
                    break
                v3 = load8u(((v9 * 404) + ENTITY_TYPES) + 332)
                v4 = (v7 + (arg0 * 132))
                store8((v7 + (arg0 * 132)) + 126, 0)
                arg1 = not v3
                func78(v15, arg1, not v3, 1)
                if arg1:
                    break
                store8(v4 + 126, 2)
                break
            return
            break
        v4 = (v7 + (arg0 * 132))
        store8((v7 + (arg0 * 132)) + 126, 0)
        func78(v15, v3, 1, 1)
        arg0 = (v7 + (v2 * 132))
        while True:  # $label27
            if (load32(CURRENT_PLAYER) != load16u(arg1)):
                break
            if not load32(arg0 + 92):
                break
            func44(v15, 0)
            break
        arg0 = load32(arg0 + 32)
        if (load32(arg0 + 32) == load32(v4 + 28)):
            break
        arg1 = (v7 + (v2 * 132))
        v3 = load16u((v7 + (v2 * 132)) + 118)
        v4 = load16u(arg1 + 116)
        while True:  # $label28
            if arg0:
                break
            if v4:
                break
            if not v3:
                break
            break
        break

# ----------------------------------------------------------
# $ed
# Export: ed
# ----------------------------------------------------------
def ed(arg0, arg1, arg2, arg3, arg4, arg5):
    """Export: ed"""
    v6 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    store32(9142860, arg1)
    store32(9142856, arg0)
    store32(9142864, arg2)
    store32(9142868, arg3)
    while True:  # $label0
        if (u32(arg3) > u32(489)):
            break
        arg0 = load32(9142884)
        if load8u(9142916):
            store32(v6 + 32, arg0)
            a_b()
            break
        store32(v6 + 24, arg0)
        store64(v6 + 16, -4602115869219225600)
        store64(v6 + 8, 0)
        store64(v6, 0)
        a_b()
        break
    store32(9147148, arg5)
    store32(9147144, arg4)
    G.global0 = (v6 + 48)

# ----------------------------------------------------------
# $func900
# ----------------------------------------------------------
def func900(arg0):
    func394(0, arg0)

# ----------------------------------------------------------
# $func901
# ----------------------------------------------------------
def func901(arg0, arg1):
    arg1 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v2 = load32(ENTITIES)
        v3 = entities[arg0]
        if (load8u(entities[arg0].unit_class) == 3):
            break
        if not load8u(v3 + 128):
            break
        arg0 = (v2 + (arg0 * 132))
        store8((v2 + (arg0 * 132)) + 127, 0)
        while True:  # $label1
            v2 = load32(arg0 + 40)
            if not load32(arg0 + 40):
                break
            if load8u(9142916):
                store32(arg1 + 20, v2)
                store32(arg1 + 16, 0)
                a_b()
                break
            arg0 = load16u(arg0 + 110)
            store32(arg1 + 4, v2)
            store32(arg1, (arg0 + 16))
            a_b()
            break
        store8(v3 + 128, 0)
        break
    G.global0 = (arg1 + 32)

# ----------------------------------------------------------
# $func902
# ----------------------------------------------------------
def func902(arg0):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v1 = load32(9173808)
    store32(arg0 + 12, load32(9173808))
    store32(arg0 + 8, load32(9213816))
    while True:  # $label0
        if load8u(9147210):
            func41(23, (arg0 + 12), 1, (arg0 + 8), 1)
            break
        v2 = func26(4)
        store32(func26(4), v1)
        break
    G.global0 = (arg0 + 16)

# ----------------------------------------------------------
# $func903
# ----------------------------------------------------------
def func903(arg0, arg1, arg2):
    arg2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v8 = entities[load32(arg1)]
        v6 = players[load16u(entities[load32(arg1)] + 110)]
        v3 = load32(players[load16u(entities[load32(arg1)] + 110)] + 281792)
        if not load32(players[load16u(entities[load32(arg1)] + 110)] + 281792):
            break
        arg0 = load32(arg0)
        if (u32(load32(arg0)) >= u32(load32(v3 + 8))):
            break
        store64(arg2 + 8, 0)
        store64(arg2, 0)
        v9 = (v6 + 281792)
        v3 = load32((load32(load32((v6 + 281792))) + (arg0 << 2)))
        v7 = ((load32((load32(load32((v6 + 281792))) + (arg0 << 2))) & 0xFFFFFFFF) >> 16)
        while True:  # $label4
            while True:  # $label3
                while True:  # $label1
                    while True:  # $label2
                        v3 = (v3 & 65535)
                        v4 = (((v3 & 65535) * 404) + ENTITY_TYPES)
                        # br_table load32((((v3 & 65535) * 404) + ENTITY_TYPES) + 268)
                        break
                        break
                    v5 = (v7 * 150)
                    # TODO: i32.div_u
                    store32(((v7 * 150) * load32(v4 + 68)), 100)
                    # TODO: i32.div_u
                    store32((load32(v4 + 72) * v5) + 4, 100)
                    # TODO: i32.div_u
                    store32((load32(v4 + 76) * v5) + 8, 100)
                    # TODO: i32.div_u
                    store32((load32(v4 + 80) * v5) + 12, 100)
                    break
                    break
                while True:  # $label6
                    while True:  # $label5
                        if (load32(38972) == v3):
                            break
                        if (load32(38976) == v3):
                            break
                        break
                        break
                    break
                store32((20 if (load32(38968) == v3) else 4), (8 * v7))
                break
                break
            store32(arg2, (v7 << 4))
            break
        if func66(v6, arg2, 1, 1):
            break
        if not func59((arg2 + 28), (arg2 + 24), v8, ((v3 * 404) + ENTITY_TYPES)):
            break
        v5 = func34(v3, load16u(v8 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
        if not func34(v3, load16u(v8 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1):
            break
        v6 = load32(ENTITIES)
        v10 = entities[v5]
        store32(entities[v5].attack, load16u(v8 + 110))
        while True:  # $label11
            while True:  # $label9
                while True:  # $label8
                    while True:  # $label7
                        if (load32(v4 + 268) == 1):
                            break
                        if (v3 == load32(38972)):
                            break
                        if (v3 == load32(38952)):
                            break
                        if (v3 != load32(38960)):
                            break
                        break
                    break
                    break
                while True:  # $label10
                    if (load32(38976) != v3):
                        if (v3 != load32(38956)):
                            break
                    break
                    break
                if (load32(38968) == v3):
                    break
                if (load32(38964) == v3):
                    break
                if (v3 != load32(38980)):
                    break
                break
            store32(((v6 + (v5 * 132)) + 72), v7)
            break
        v3 = load32(v9)
        v4 = (load32(v3 + 8) - 1)
        store32(load32(v9) + 8, (load32(v3 + 8) - 1))
        if (u32(arg0) < u32(v4)):
            v4 = load32(v3)
            while True:  # $label12
                arg0 = (arg0 + 1)
                store32((v4 + (arg0 << 2)), load32((v4 + ((arg0 + 1) << 2))))
                if (u32(arg0) < u32(load32(v3 + 8))):
                    continue
                break
        if (load32(9671124) != 240):
            break
        if (load32(CURRENT_PLAYER) != load16u((v6 + (load32(arg1) * 132)) + 110)):
            break
        func221(arg0)
        break
    G.global0 = (arg2 + 32)
    return ((v6 + (v5 * 132)) + 60)

# ----------------------------------------------------------
# $func905
# ----------------------------------------------------------
def func905(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label1
        while True:  # $label0
            arg2 = load32(ENTITIES)
            arg3 = entities[load32(arg1)]
            if (load32(38564) != load8u(entities[load32(arg1)].sub_state)):
                break
            arg1 = 1
            # br_table (load8u(arg3 + 125) - 4)
            break
            break
        arg1 = 1
        while True:  # $label2
            while True:  # $label3
                arg0 = load8u((arg2 + (arg0 * 132)) + 122)
                # br_table (load8u((arg2 + (arg0 * 132)) + 122) + -64)
                break
                break
            if (arg0 != 10):
                break
            break
        arg1 = 0
        break
    return arg1

# ----------------------------------------------------------
# $func906
# ----------------------------------------------------------
def func906(arg0, arg1, param2):
    v12 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v6 = load32(ENTITIES)
    v3 = entities[arg0]
    while True:  # $label0
        v8 = (v6 + (arg1 * 132))
        v4 = load8u((v6 + (arg1 * 132)) + 125)
        if (load8u((v6 + (arg1 * 132)) + 125) == 3):
            arg0 = func336(load16u(v3 + 112), load16u(v3 + 114), load16u(v3 + 110))
            if func336(load16u(v3 + 112), load16u(v3 + 114), load16u(v3 + 110)):
                break
            func29(v3, 1)
            break
        v5 = load8u(v8 + 122)
        if (load8u(v3 + 125) == 1):
            v2 = ((v5 * 404) + ENTITY_TYPES)
            v14 = load32(((v5 * 404) + ENTITY_TYPES) + 220)
            v4 = (v6 + (arg1 * 132))
            v5 = load16u((v6 + (arg1 * 132)) + 114)
            v8 = (load32(((v5 * 404) + ENTITY_TYPES) + 220) + load16u((v6 + (arg1 * 132)) + 114))
            v15 = load32(v2 + 216)
            v10 = load16u(v4 + 112)
            v7 = (load32(v2 + 216) + load16u(v4 + 112))
            v9 = (v6 + (arg0 * 132))
            v2 = load16u((v6 + (arg0 * 132)) + 114)
            v4 = 6
            while True:  # $label2
                while True:  # $label1
                    v9 = load16u(v9 + 112)
                    v11 = (u32(load16u(v9 + 112)) < u32(v10))
                    if (u32(load16u(v9 + 112)) < u32(v10)):
                        break
                    if (v7 <= v9):
                        break
                    if (u32(v2) < u32(v5)):
                        break
                    if (v2 >= v8):
                        break
                    v5 = ((v14 // 2) + v5)
                    v5 = (-1 if (v2 > v5) else (((v14 // 2) + v5) != v2))
                    v2 = ((v15 // 2) + v10)
                    break
                    break
                v5 = (1 if (u32(v2) < u32(v5)) else (-1 if (v2 >= v8) else 0))
                break
            v2 = (((1 if v11 else (-1 if (v7 <= v9) else 0)) + (v5 * 3)) + 4)
            if (u32((((1 if v11 else (-1 if (v7 <= v9) else 0)) + (v5 * 3)) + 4)) <= u32(8)):
                v4 = load8u((v2 + 10184))
            v2 = (v6 + (arg0 * 132))
            store8((v6 + (arg0 * 132)) + 124, v4)
            v4 = load32(((load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            if (load8u(v3 + 125) == 3):
                break
            v4 = load32(v2 + 44)
            if load32(v2 + 44):
                v5 = load32(9142848)
                v3 = load32(9215884)
                store32((load32(9215884) + (v4 << 4)) + 4, 4)
                store32((v3 + (load32(v2 + 44) << 4)) + 8, load32((v6 + (arg0 * 132)) + 28))
                store32((v3 + (load32(v2 + 44) << 4)) + 12, arg1)
                store32((v3 + (load32(v2 + 44) << 4)), (v5 + 40))
                break
            store32(v2 + 44, ((Ua(1000, 4, load32((v6 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        if (v4 == 14):
            store32((load32(9215884) + (load32((v6 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
            break
        v2 = load32(((v5 * 404) + ENTITY_TYPES) + 116)
        v17 = (v6 + (arg0 * 132))
        v14 = load16u((v6 + (arg0 * 132)) + 110)
        v15 = load32(PLAYERS)
        if (v4 == 4):
            # TODO: i32.div_u
            v2 = 100
        v7 = (v6 + (arg1 * 132))
        if v2:
            # TODO: i32.div_u
            # TODO: i32.div_u
        else:
        v2 = 2147483647
        v2 = (2147483647 if (v4 == 4) else ((v2 & 0xFFFFFFFF) >> 2))
        v10 = (load32(((v15 + (v14 * 286704)) + 284004)) + ((load32((v6 + (arg1 * 132)) + 68) * v2) if (load32(((v5 * 404) + ENTITY_TYPES) + 268) == 2) else (100 if (u32(v2) <= u32(1)) else (2147483647 if (v4 == 4) else ((v2 & 0xFFFFFFFF) >> 2)))))
        store32(1 + 64, (load32(((v15 + (v14 * 286704)) + 284004)) + ((load32((v6 + (arg1 * 132)) + 68) * v2) if (load32(((v5 * 404) + ENTITY_TYPES) + 268) == 2) else (100 if (u32(v2) <= u32(1)) else (2147483647 if (v4 == 4) else ((v2 & 0xFFFFFFFF) >> 2))))))
        v11 = (v7 - -64)
        while True:  # $label3
            v9 = (v6 + (arg0 * 132))
            v2 = load16u((v6 + (arg0 * 132)) + 112)
            v13 = ((load16u((v6 + (arg0 * 132)) + 112) << 5) - load32(9142952))
            v13 = load16u(v9 + 114)
            v16 = ((load16u(v9 + 114) << 5) - load32(9142956))
            if ((((((load16u((v6 + (arg0 * 132)) + 112) << 5) - load32(9142952)) * v13) + (((load16u(v9 + 114) << 5) - load32(9142956)) * v16)) - 1) > 9000000):
                break
            while True:  # $label4
                v18 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v16 = load16u((load32(9147376) + (((load32(9142440) * v13) + v2) << 1)))
                if (v18 == 2):
                    if (u32(v16) > u32(1)):
                        break
                    break
                if not v16:
                    break
                break
            store32(v12 + 40, v13)
            store32(v12 + 36, v2)
            store32(v12 + 32, load32(((((load32(9142848) + v2) % 7) << 2) + 57248)))
            a_b()
            v10 = load32(v11)
            break
        while True:  # $label21
            v7 = load32(v7 + 68)
            if (u32(load32(v7 + 68)) <= u32(v10)):
                store32(v11, v7)
                v2 = 0
                while True:  # $label5
                    if (u32(load32(((load8u(v8 + 122) * 404) + ENTITY_TYPES) + 192)) > u32(3)):
                        v10 = 4
                        break
                    while True:  # $label6
                        v7 = (v6 + (arg0 * 132))
                        v10 = load32((v6 + (arg0 * 132)) + 20)
                        if not load32((v6 + (arg0 * 132)) + 20):
                            break
                        v11 = load32(v10 + 8)
                        if (u32(load32(v10 + 8)) < u32(3)):
                            break
                        v13 = load32(v10)
                        if (u32((load32(load32(v10)) - 1)) > u32(1)):
                            break
                        v10 = 4
                        if ((load32(v13 + 4) + 7) != v11):
                            break
                        break
                    v11 = load8u(v7 + 129)
                    while True:  # $label8
                        while True:  # $label9
                            while True:  # $label7
                                if load32(players[load16u(v17 + 110)] + 286684):
                                    v7 = 0
                                    v10 = 4
                                    # br_table (v11 - 1)
                                    break
                                v7 = 0
                                # br_table (v11 - 1)
                                break
                                break
                            v7 = load32(38504)
                            break
                            break
                        v7 = load32(38508)
                        break
                    v10 = 4
                    v3 = func224(v3, load32(((v5 * 404) + ENTITY_TYPES) + 192), v7)
                    if not func224(v3, load32(((v5 * 404) + ENTITY_TYPES) + 192), v7):
                        break
                    store32(entities[v3].direction, load32(9142848))
                    v10 = 1
                    v2 = v3
                    break
                while True:  # $label19
                    if (v4 == 4):
                        v3 = (v6 + (arg1 * 132))
                        v17 = load16u((v6 + (arg1 * 132)) + 110)
                        v18 = load32(PLAYERS)
                        store8(v8 + 125, 0)
                        while True:  # $label10
                            v4 = load32(v3 + 40)
                            if not load32(v3 + 40):
                                break
                            if not load8u(9142916):
                                break
                            v5 = load32((v6 + (arg1 * 132)) + 92)
                            store32(v12 + 20, v4)
                            store32(v12 + 16, (v5 != 0))
                            a_b()
                            break
                        while True:  # $label11
                            if load32((v15 + (v14 * 286704)) + 286684):
                                break
                            v4 = 0
                            while True:  # $label12
                                v5 = load32((v6 + (arg0 * 132)) + 20)
                                if not load32((v6 + (arg0 * 132)) + 20):
                                    break
                                if (u32(load32(v5 + 8)) < u32(3)):
                                    break
                                v4 = (u32((load32(load32(v5)) - 1)) < u32(2))
                                break
                            if v2:
                                break
                            if v4:
                                break
                            v19 = load16u(v3 + 110)
                            v7 = 0
                            v15 = load16u(v9 + 112)
                            v20 = (load16u(v9 + 112) + 29)
                            v11 = load16u(v9 + 114)
                            v21 = (load16u(v9 + 114) + 29)
                            v9 = (v11 - 30)
                            v3 = (v15 - 30)
                            v13 = load32(9142440)
                            v16 = (load32(9142440) + 2)
                            v22 = load32(ENTITIES)
                            v23 = load32(9142840)
                            v14 = 2147483647
                            while True:  # $label15
                                v5 = (v3 + 1)
                                if (u32(v3) < u32(v13)):
                                    v2 = (v3 - v15)
                                    v24 = ((v3 - v15) * v2)
                                    v2 = v9
                                    while True:  # $label14
                                        while True:  # $label13
                                            v4 = v2
                                            if (u32(v13) <= u32(v2)):
                                                break
                                            if ((v3 | v4) < 0):
                                                break
                                            v2 = (v4 - v11)
                                            v2 = (((v4 - v11) * v2) + v24)
                                            if ((((v4 - v11) * v2) + v24) >= v14):
                                                break
                                            v2 = (v22 + (load32((v23 + ((v5 + (((v4 + v16) + 1) * v16)) << 2))) * 132))
                                            v25 = ((load8u((v22 + (load32((v23 + ((v5 + (((v4 + v16) + 1) * v16)) << 2))) * 132)) + 125) == 4) & (load16u(v2 + 110) == v19))
                                            v14 = (v2 if ((load8u((v22 + (load32((v23 + ((v5 + (((v4 + v16) + 1) * v16)) << 2))) * 132)) + 125) == 4) & (load16u(v2 + 110) == v19)) else v14)
                                            v7 = (load32(v2 + 28) if v25 else v7)
                                            break
                                        v2 = (v4 + 1)
                                        if (v4 < v21):
                                            continue
                                        break
                                v2 = (v3 < v20)
                                v3 = v5
                                if v2:
                                    continue
                                break
                            v2 = v7
                            break
                        v4 = 0
                        while True:  # $label16
                            v3 = load8u(v8 + 122)
                            v5 = load32(((load8u(v8 + 122) * 72) + 9263856))
                            if not load32(((load8u(v8 + 122) * 72) + 9263856)):
                                break
                            v9 = load32(v5 + 20)
                            if not load32(v5 + 20):
                                break
                            if (load32(38604) == v3):
                                break
                            v4 = (load32((v6 + (arg1 * 132)) + 28) % v9)
                            break
                        store8((v6 + (arg1 * 132)) + 124, v4)
                        while True:  # $label18
                            while True:  # $label17
                                if (v3 != load32(38600)):
                                    if (load32(38472) != v3):
                                        break
                                func286(v8)
                                break
                                break
                            break
                        func420(v8)
                        v3 = load32(ENTITIES)
                        v4 = (arg1 * 132)
                        if (load32(CURRENT_PLAYER) == load16u(entities[arg1] + 110)):
                            store32(v12, load32(39228))
                            a_b()
                        else:
                        v3 = (v3 + v4)
                        v4 = ((load32(ENTITIES) + (load8u((v3 + v4) + 122) << 2)) + 282828)
                        store32(((load32(ENTITIES) + (load8u((v3 + v4) + 122) << 2)) + 282828), (load32(v4) - 1))
                        v4 = load32(v3 + 20)
                        if not load32(v3 + 20):
                            break
                        if not load32(v4 + 8):
                            break
                        func230(v3)
                        break
                    v5 = 0
                    while True:  # $label20
                        v3 = load32((v6 + (arg0 * 132)) + 20)
                        if not load32((v6 + (arg0 * 132)) + 20):
                            break
                        if (u32(load32(v3 + 8)) < u32(3)):
                            break
                        v5 = (u32((load32(load32(v3)) - 1)) < u32(2))
                        break
                    if v2:
                        break
                    if v5:
                        break
                    v2 = func336(load16u(v9 + 112), load16u(v9 + 114), load16u((v6 + (arg1 * 132)) + 110))
                    break
                arg0 = entities[arg0]
                if v2:
                    break
                func29(arg0, 1)
                break
            while True:  # $label22
                if (v4 != 4):
                    break
                v2 = (v6 + (arg1 * 132))
                store32((v6 + (arg1 * 132)) + 88, load32(9142848))
                v3 = load8u(v8 + 122)
                # TODO: i32.div_u
                v3 = v7
                if (u32(v7) <= u32(load8u(v2 + 124))):
                    break
                store8(v2 + 124, v3)
                break
            store32((load32(9215884) + (load32((v6 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
            break
        arg0 = load32(ENTITIES)
        if not load32(entities[arg1].flags):
            break
        if load32(9140316):
            if (load32(9140320) != load32((arg0 + (arg1 * 132)) + 28)):
                break
        break
    G.global0 = (v12 + 48)
    return func28(1, 1)

# ----------------------------------------------------------
# $func907
# ----------------------------------------------------------
def func907(arg0):
    while True:  # $label0
        v6 = load32(ENTITIES)
        v2 = load32(arg0 + 32)
        v3 = entities[load32(arg0 + 32)]
        v4 = load8u(entities[load32(arg0 + 32)].sub_state)
        if (load32(((load8u(entities[load32(arg0 + 32)].sub_state) * 404) + ENTITY_TYPES) + 188) != 55):
            break
        if (u32(load32(v3 + 64)) < u32(load32(v3 + 68))):
            if (load8u((v6 + (v2 * 132)) + 125) != 3):
                break
        while True:  # $label1
            v4 = load32(((v4 * 404) + ENTITY_TYPES) + 192)
            if (u32(load32(((v4 * 404) + ENTITY_TYPES) + 192)) > u32(3)):
                break
            while True:  # $label2
                v1 = load32(arg0 + 20)
                if not load32(arg0 + 20):
                    break
                if (u32(load32(v1 + 8)) < u32(3)):
                    break
                if (u32((load32(load32(v1)) - 1)) < u32(2)):
                    break
                break
            v1 = 0
            v2 = load8u(arg0 + 129)
            while True:  # $label4
                while True:  # $label5
                    while True:  # $label3
                        if load32(players[load16u(arg0 + 110)] + 286684):
                            # br_table (v2 - 1)
                            break
                        # br_table (v2 - 1)
                        break
                        break
                    v1 = load32(38504)
                    break
                    break
                v1 = load32(38508)
                break
            v1 = func224(v3, v4, v1)
            if not func224(v3, v4, v1):
                break
            store8(arg0 + 123, 1)
            store32(arg0 + 32, v1)
            store32((v6 + (v1 * 132)) + 88, load32(9142848))
            return 0
            break
        v8 = load16u(arg0 + 112)
        v12 = (load16u(arg0 + 112) + 29)
        v9 = load16u(arg0 + 114)
        v13 = (load16u(arg0 + 114) + 29)
        v10 = load32(9142440)
        v11 = (load32(9142440) + 2)
        v14 = (v9 - 30)
        v3 = (v8 - 30)
        v15 = load32(9142840)
        v7 = 2147483647
        v16 = load16u(arg0 + 110)
        while True:  # $label8
            v4 = (v3 + 1)
            if (u32(v3) < u32(v10)):
                v1 = (v3 - v8)
                v17 = ((v3 - v8) * v1)
                v1 = v14
                while True:  # $label7
                    while True:  # $label6
                        v2 = v1
                        if (u32(v10) <= u32(v1)):
                            break
                        if ((v2 | v3) < 0):
                            break
                        v1 = (v2 - v9)
                        v1 = (((v2 - v9) * v1) + v17)
                        if ((((v2 - v9) * v1) + v17) >= v7):
                            break
                        v1 = (v6 + (load32((v15 + (((((v2 + v11) + 1) * v11) + v4) << 2))) * 132))
                        v18 = ((load8u((v6 + (load32((v15 + (((((v2 + v11) + 1) * v11) + v4) << 2))) * 132)) + 125) == 4) & (load16u(v1 + 110) == v16))
                        v7 = (v1 if ((load8u((v6 + (load32((v15 + (((((v2 + v11) + 1) * v11) + v4) << 2))) * 132)) + 125) == 4) & (load16u(v1 + 110) == v16)) else v7)
                        v5 = (load32(v1 + 28) if v18 else v5)
                        break
                    v1 = (v2 + 1)
                    if (v2 != v13):
                        continue
                    break
            v1 = (v3 == v12)
            v3 = v4
            if not v1:
                continue
            break
        if not v5:
            return 1
        store32(arg0 + 32, v5)
        break
    return 0

# ----------------------------------------------------------
# $func908
# ----------------------------------------------------------
def func908(arg0):
    store32(9681476, 9681696)
    store32(9681464, 0)
    store32(9681468, 0)
    store32(9681472, load32(((load32(9681696) * 404) + ENTITY_TYPES) + 68))

# ----------------------------------------------------------
# $func911
# ----------------------------------------------------------
def func911(arg0, arg1, param2):
    v4 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        v5 = load32(ENTITIES)
        v9 = entities[arg0]
        if (load8u(entities[arg0].unit_class) == 3):
            break
        if not load8u(v9 + 128):
            break
        v2 = (v5 + (arg0 * 132))
        store8((v5 + (arg0 * 132)) + 127, 0)
        while True:  # $label1
            v3 = load32(v2 + 40)
            if not load32(v2 + 40):
                break
            if load8u(9142916):
                store32(v4 + 20, v3)
                store32(v4 + 16, 0)
                a_b()
                break
            v2 = load16u(v2 + 110)
            store32(v4 + 4, v3)
            store32(v4, (v2 + 16))
            a_b()
            break
        store8(v9 + 128, 0)
        break
    store64(v4 + 40, load64(9672))
    store64(v4 + 32, load64(9664))
    while True:  # $label4
        if (load8u(v9 + 125) == 1):
            v10 = (v5 + (arg0 * 132))
            v2 = load16u((v5 + (arg0 * 132)) + 114)
            v7 = (v5 + (arg1 * 132))
            v3 = load16u((v5 + (arg1 * 132)) + 114)
            while True:  # $label3
                while True:  # $label2
                    v7 = load16u(v7 + 112)
                    v10 = load16u(v10 + 112)
                    if (load16u(v7 + 112) != load16u(v10 + 112)):
                        break
                    if (u32(v2) < u32(v3)):
                        break
                    if (u32(v2) > u32(v3)):
                        break
                    v6 = (v2 != v3)
                    break
                    break
                v6 = (1 if (u32(v2) < u32(v3)) else (-1 if (u32(v2) > u32(v3)) else 0))
                break
            v2 = (1 if (u32(v7) > u32(v10)) else (-1 if (u32(v7) < u32(v10)) else 0))
            v3 = 6
            v2 = (((v6 * 3) + v2) + 4)
            if (u32((((v6 * 3) + v2) + 4)) <= u32(8)):
                v3 = load8u((v2 + 10184))
            v2 = (v5 + (arg0 * 132))
            store8((v5 + (arg0 * 132)) + 124, v3)
            v3 = load32(((load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            if (load8u(v9 + 125) == 3):
                break
            v9 = load32(v2 + 44)
            if load32(v2 + 44):
                v7 = load32(9142848)
                v3 = load32(9215884)
                store32((load32(9215884) + (v9 << 4)) + 4, 62)
                store32((v3 + (load32(v2 + 44) << 4)) + 8, load32((v5 + (arg0 * 132)) + 28))
                store32((v3 + (load32(v2 + 44) << 4)) + 12, arg1)
                store32((v3 + (load32(v2 + 44) << 4)), (v7 + 20))
                break
            store32(v2 + 44, ((Ua(500, 62, load32((v5 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        v2 = (v5 + (arg0 * 132))
        v17 = (v5 + (arg0 * 132))
        while True:  # $label5
            v2 = load16u(v2 + 110)
            if (load16u(v2 + 110) == load16u((v5 + (arg1 * 132)) + 110)):
                break
            if (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
                break
            if func66(players[v2], (v4 + 32), 1, 1):
                break
            v2 = (v5 + (arg1 * 132))
            if (load8u((v5 + (arg1 * 132)) + 125) == 3):
                break
            func78((v5 + (arg1 * 132)), load16u(v17 + 110), 1, 0)
            while True:  # $label6
                if not load32(v2 + 92):
                    break
                v2 = load8u(9147141)
                if load32(9140316):
                    if (load32(9140320) != load32((v5 + (arg1 * 132)) + 28)):
                        break
                break
            v2 = (v5 + (arg1 * 132))
            v7 = load16u((v5 + (arg1 * 132)) + 114)
            v10 = load16u(v2 + 112)
            while True:  # $label9
                while True:  # $label8
                    while True:  # $label7
                        v12 = load32(load32(GAME_STATE) + 48)
                        if load32(load32(GAME_STATE) + 48):
                            if not load8u(9147152):
                                break
                        v3 = load32(9142440)
                        break
                        break
                    v3 = load32(9142440)
                    v6 = load16u((load32(9147376) + (((load32(9142440) * v7) + v10) << 1)))
                    if (v12 == 2):
                        if (u32(v6) > u32(1)):
                            break
                        break
                    if not v6:
                        break
                    break
                func80(i32(v10), i32(v7), load32(9142776), 32.0, i32((v3 * 96)))
                v7 = load16u(v2 + 114)
                v10 = load16u(v2 + 112)
                break
            v12 = (v5 + (arg1 * 132))
            v2 = 0
            while True:  # $label18
                while True:  # $label10
                    v8 = load32(9142440)
                    v3 = v2
                    v6 = (v2 << 2)
                    v2 = (load32((((v2 << 2) | 4) + 8611904)) + v7)
                    if (u32(load32(9142440)) <= u32((load32((((v2 << 2) | 4) + 8611904)) + v7))):
                        break
                    v11 = (load32((v6 + 8611904)) + v10)
                    if (u32(v8) <= u32((load32((v6 + 8611904)) + v10))):
                        break
                    if ((v2 | v11) < 0):
                        break
                    while True:  # $label11
                        v6 = load32(9142840)
                        v11 = (v11 + 1)
                        v14 = (v2 + 1)
                        v2 = load32((load32(9142840) + (((v11 + 1) + ((v2 + 1) * (v8 + 2))) << 2)))
                        if (u32(load32((load32(9142840) + (((v11 + 1) + ((v2 + 1) * (v8 + 2))) << 2)))) < u32(3)):
                            break
                        v2 = entities[v2]
                        v15 = (load32(entities[v2].target_x) << 2)
                        v13 = ((load32(entities[v2].target_x) << 2) | 1)
                        v8 = load32(9215884)
                        while True:  # $label12
                            v16 = load32(v12 + 28)
                            if (load32(v12 + 28) != load32(v2 + 32)):
                                break
                            if load32((v8 + (v13 << 2))):
                                break
                            if (load8u(v2 + 123) != 6):
                                break
                            store32(v2 + 116, load32(v2 + 112))
                            store32(v2 + 32, 0)
                            store8(v2 + 123, 0)
                            break
                            break
                        if (load32((v8 + (v13 << 2))) != 6):
                            break
                        if (load32((v8 + ((v15 << 2) | 12))) != v16):
                            break
                        func29(v2, 1)
                        v6 = load32(9142840)
                        break
                    while True:  # $label13
                        v2 = (load32(9142440) + 2)
                        v2 = load32((v6 + ((v11 + ((v14 + (load32(9142440) + 2)) * v2)) << 2)))
                        if (u32(load32((v6 + ((v11 + ((v14 + (load32(9142440) + 2)) * v2)) << 2)))) < u32(3)):
                            break
                        v2 = entities[v2]
                        v15 = (load32(entities[v2].target_x) << 2)
                        v13 = ((load32(entities[v2].target_x) << 2) | 1)
                        v8 = load32(9215884)
                        while True:  # $label15
                            while True:  # $label14
                                v16 = load32(v12 + 28)
                                if (load32(v12 + 28) != load32(v2 + 32)):
                                    break
                                if load32((v8 + (v13 << 2))):
                                    break
                                if (load8u(v2 + 123) == 6):
                                    break
                                break
                            if (load32((v8 + (v13 << 2))) != 6):
                                break
                            if (load32((v8 + ((v15 << 2) | 12))) != v16):
                                break
                            func29(v2, 1)
                            v6 = load32(9142840)
                            break
                            break
                        store32(v2 + 116, load32(v2 + 112))
                        store32(v2 + 32, 0)
                        store8(v2 + 123, 0)
                        break
                    v2 = (load32(9142440) + 2)
                    v2 = load32((v6 + ((v11 + ((v14 + ((load32(9142440) + 2) << 1)) * v2)) << 2)))
                    if (u32(load32((v6 + ((v11 + ((v14 + ((load32(9142440) + 2) << 1)) * v2)) << 2)))) < u32(3)):
                        break
                    v2 = entities[v2]
                    v11 = (load32(entities[v2].target_x) << 2)
                    v8 = ((load32(entities[v2].target_x) << 2) | 1)
                    v6 = load32(9215884)
                    while True:  # $label17
                        while True:  # $label16
                            v14 = load32(v12 + 28)
                            if (load32(v12 + 28) != load32(v2 + 32)):
                                break
                            if load32((v6 + (v8 << 2))):
                                break
                            if (load8u(v2 + 123) == 6):
                                break
                            break
                        if (load32((v6 + (v8 << 2))) != 6):
                            break
                        if (load32((v6 + ((v11 << 2) | 12))) != v14):
                            break
                        func29(v2, 1)
                        break
                        break
                    store32(v2 + 116, load32(v2 + 112))
                    store32(v2 + 32, 0)
                    store8(v2 + 123, 0)
                    break
                v2 = (v3 + 2)
                if (u32(v3) < u32(13118)):
                    continue
                break
            break
        v2 = load16u(v17 + 110)
        while True:  # $label19
            v3 = load32(v4 + 32)
            if load32(v4 + 32):
                if (load32(v4 + 48) < v3):
                    break
            v3 = load32(v4 + 36)
            if load32(v4 + 36):
                if (load32(v4 + 52) < v3):
                    break
            v3 = load32(v4 + 40)
            if load32(v4 + 40):
                if (load32(v4 + 56) < v3):
                    break
            v3 = load32(v4 + 44)
            if load32(v4 + 44):
                if (load32(v4 + 60) < v3):
                    break
            v3 = (v5 + (arg0 * 132))
            v7 = load8u((v5 + (arg0 * 132)) + 129)
            if ((load8u((v5 + (arg0 * 132)) + 129) & 254) != 14):
                break
            while True:  # $label20
                if not load32(v3 + 96):
                    if (load8u(v9 + 125) != 1):
                        break
                store8(v9 + 125, 0)
                break
            arg0 = (v5 + (arg0 * 132))
            store32((v5 + (arg0 * 132)) + 44, 0)
            arg0 = func416(load16u(arg0 + 112), load16u(arg0 + 114), v2, (-1 if (v7 != 15) else load8u((v5 + (arg1 * 132)) + 122)))
            if func416(load16u(arg0 + 112), load16u(arg0 + 114), v2, (-1 if (v7 != 15) else load8u((v5 + (arg1 * 132)) + 122))):
                break
            func29(v9, 1)
            break
            break
        func29(v9, 1)
        break
    G.global0 = (v4 - -64)
    return func28((v2 != 0), 1)

# ----------------------------------------------------------
# $func913
# ----------------------------------------------------------
def func913(arg0):
    while True:  # $label0
        v1 = load8u(arg0 + 129)
        if ((load8u(arg0 + 129) & 254) != 14):
            break
        v1 = func416(load16u(arg0 + 112), load16u(arg0 + 114), load16u(arg0 + 110), (-1 if (v1 != 15) else load8u(entities[load32(arg0 + 32)].sub_state)))
        if not func416(load16u(arg0 + 112), load16u(arg0 + 114), load16u(arg0 + 110), (-1 if (v1 != 15) else load8u(entities[load32(arg0 + 32)].sub_state))):
            break
        store32(arg0 + 32, v1)
        break
    return 0

# ----------------------------------------------------------
# $func916
# ----------------------------------------------------------
def func916(arg0, arg1):
    v4 = entities[arg0]
    v7 = load16u(v4 + 116)
    v8 = load16u(v4 + 118)
    while True:  # $label0
        arg0 = load32((players[load16u(v4 + 110)] + 284140))
        arg1 = (v7 - load32((players[load16u(v4 + 110)] + 284140)))
        v5 = (arg0 << 1)
        v10 = (v7 + (arg0 << 1))
        if ((v7 - load32((players[load16u(v4 + 110)] + 284140))) >= (v7 + (arg0 << 1))):
            break
        v11 = (v8 - arg0)
        v12 = (v5 + v8)
        if ((v8 - arg0) >= (v5 + v8)):
            break
        v13 = (arg0 * arg0)
        while True:  # $label5
            v5 = (arg1 + 1)
            arg0 = (arg1 - v7)
            v14 = (((arg1 - v7) * arg0) - 1)
            arg0 = v11
            while True:  # $label4
                while True:  # $label1
                    v2 = (arg0 - v8)
                    if ((v14 + ((arg0 - v8) * v2)) > v13):
                        break
                    v2 = load32(9142440)
                    if (u32(load32(9142440)) <= u32(arg0)):
                        break
                    if ((arg0 | arg1) < 0):
                        break
                    if (u32(arg1) >= u32(v2)):
                        break
                    while True:  # $label2
                        v6 = load32(9142840)
                        v9 = (arg0 + 1)
                        v2 = (v2 + 2)
                        v3 = load32((load32(9142840) + ((v5 + ((arg0 + 1) * (v2 + 2))) << 2)))
                        if (u32(load32((load32(9142840) + ((v5 + ((arg0 + 1) * (v2 + 2))) << 2)))) <= u32(2)):
                            break
                        v3 = entities[v3]
                        if not load32(((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES) + 296):
                            break
                        if load8u((load32(9143004) + (load16u(v4 + 110) + (load32(PLAYER_COUNT) * load16u(v3 + 110))))):
                            break
                        func206(v3)
                        v2 = (load32(9142440) + 2)
                        v6 = load32(9142840)
                        break
                    while True:  # $label3
                        v3 = load32((v6 + ((v5 + ((v2 + v9) * v2)) << 2)))
                        if (u32(load32((v6 + ((v5 + ((v2 + v9) * v2)) << 2)))) < u32(3)):
                            break
                        v3 = entities[v3]
                        if not load32(((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES) + 296):
                            break
                        if load8u((load32(9143004) + (load16u(v4 + 110) + (load32(PLAYER_COUNT) * load16u(v3 + 110))))):
                            break
                        func206(v3)
                        v2 = (load32(9142440) + 2)
                        v6 = load32(9142840)
                        break
                    v2 = load32((v6 + ((v5 + ((v9 + (v2 << 1)) * v2)) << 2)))
                    if (u32(load32((v6 + ((v5 + ((v9 + (v2 << 1)) * v2)) << 2)))) < u32(3)):
                        break
                    v2 = entities[v2]
                    if not load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 296):
                        break
                    if load8u((load32(9143004) + (load16u(v4 + 110) + (load32(PLAYER_COUNT) * load16u(v2 + 110))))):
                        break
                    func206(v2)
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v12):
                    continue
                break
            arg1 = v5
            if (v5 != v10):
                continue
            break
        break

# ----------------------------------------------------------
# $func917
# ----------------------------------------------------------
def func917(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v1 + 12, arg0)
    arg0 = load32(9213808)
    while True:  # $label0
        if load8u(9147210):
            func41(13, 9173808, arg0, (v1 + 12), 1)
            break
        v3 = (arg0 << 2)
        v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy
        break
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func918
# ----------------------------------------------------------
def func918(arg0, arg1, arg2):
    v3 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v5 = load32(arg0 + 4)
    v4 = 38932
    while True:  # $label2
        while True:  # $label5
            while True:  # $label3
                while True:  # $label4
                    while True:  # $label0
                        while True:  # $label1
                            v7 = load32(arg0)
                            # br_table (load32(arg0) - 15)
                            break
                            break
                        v4 = 38728
                        break
                        break
                    v4 = 38724
                    break
                    break
                v4 = 38936
                break
                break
            v4 = 38940
            break
        if (load32(v4) == -1):
            break
        if not arg2:
            break
        v5 = ((v3 + 16) | (not v5 << 3))
        arg0 = 0
        while True:  # $label6
            v4 = load32((arg1 + (arg0 << 2)))
            v6 = load32(ENTITIES)
            store64(v3 + 16, 8589934591)
            v4 = (v6 + (v4 * 132))
            store32(v3 + 24, load16u((v6 + (v4 * 132)) + 112))
            v6 = load16u(v4 + 114)
            store32(v3 + 48, 0)
            store64(v3 + 40, 0)
            store32(v3 + 36, v7)
            store32(v3 + 32, 0)
            store32(v3 + 28, v6)
            store32(v3 + 12, load32(v4 + 28))
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break
        break
    G.global0 = (v3 - -64)

# ----------------------------------------------------------
# $func919
# ----------------------------------------------------------
def func919(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label0
        arg2 = load32(arg1)
        if (arg0 == load32(arg1)):
            break
        arg3 = load32(ENTITIES)
        v6 = entities[arg0]
        if not load32(entities[arg0].speed):
            break
        v7 = load8u(v6 + 122)
        arg1 = (arg3 + (arg2 * 132))
        arg4 = load8u((arg3 + (arg2 * 132)) + 122)
        if not func162(v6, load8u((arg3 + (arg2 * 132)) + 122), load8u(arg1 + 125), arg2):
            break
        arg1 = 0
        while True:  # $label1
            if load32(((v7 * 404) + ENTITY_TYPES) + 260):
                break
            if not arg2:
                break
            arg1 = 1
            while True:  # $label2
                v10 = (arg3 + (arg0 * 132))
                # br_table (load8u((arg3 + (arg0 * 132)) + 125) - 4)
                break
                break
            while True:  # $label3
                v8 = load32(((arg4 * 404) + ENTITY_TYPES) + 216)
                if not load32(((arg4 * 404) + ENTITY_TYPES) + 216):
                    break
                arg1 = ((v7 * 404) + ENTITY_TYPES)
                v11 = ((v7 * 404) + ENTITY_TYPES)
                arg4 = (arg3 + (arg2 * 132))
                v12 = load16u((arg3 + (arg2 * 132)) + 114)
                v5 = (arg3 + (arg0 * 132))
                v13 = load16u((arg3 + (arg0 * 132)) + 114)
                v14 = load16u(arg4 + 112)
                v15 = load16u(v5 + 112)
                arg1 = load32(arg1 + 224)
                v16 = (load32(arg1 + 224) * arg1)
                arg4 = 0
                v5 = 1
                while True:  # $label6
                    arg1 = (v13 - (arg4 + v12))
                    v17 = ((v13 - (arg4 + v12)) * arg1)
                    arg1 = 0
                    while True:  # $label4
                        while True:  # $label5
                            v9 = (v15 - (arg1 + v14))
                            v9 = (((v15 - (arg1 + v14)) * v9) + v17)
                            if (v16 >= ((((v15 - (arg1 + v14)) * v9) + v17) - 1)):
                                v18 = load32(v11 + 228)
                                if (u32(v9) >= u32((load32(v11 + 228) * v18))):
                                    break
                            arg1 = (arg1 + 1)
                            if ((arg1 + 1) != v8):
                                continue
                            break
                        arg4 = (arg4 + 1)
                        v5 = (u32((arg4 + 1)) < u32(v8))
                        if (arg4 != v8):
                            continue
                        break
                    break
                if not v5:
                    break
                arg4 = load32(9215884)
                arg0 = (arg3 + (arg0 * 132))
                arg1 = load32((arg3 + (arg0 * 132)) + 44)
                if (load32((load32(9215884) + (load32((arg3 + (arg0 * 132)) + 44) << 4)) + 4) == 6):
                    store32((arg4 + ((arg1 << 4) | 12)), arg2)
                    arg1 = 1
                    arg0 = load32(arg0 + 44)
                    if not load32(arg0 + 44):
                        break
                    arg0 = (arg4 + (arg0 << 4))
                    arg2 = load32((arg4 + (arg0 << 4)))
                    if (load32((arg4 + (arg0 << 4))) != load32(9142848)):
                        break
                    arg0 = load32(((v7 * 404) + ENTITY_TYPES) + 276)
                    # TODO: i32.div_u
                    store32(load32(((v7 * 404) + ENTITY_TYPES) + 276), ((25 if arg0 else 1) + arg2))
                    break
                store8(v10 + 125, 1)
                store8(v10 + 125, 0)
                break
                break
            arg1 = 1
            func29(v6, 1)
            break
        return arg1
        break
    return 1

# ----------------------------------------------------------
# $func920
# ----------------------------------------------------------
def func920(arg0, arg1):
    v2 = load32(ENTITIES)
    arg1 = entities[arg1]
    if (load8u(entities[arg1].unit_class) != 3):
        arg0 = (v2 + (arg0 * 132))

# ----------------------------------------------------------
# $func921
# ----------------------------------------------------------
def func921(arg0):
    v9 = load8u(arg0 + 122)
    v5 = 1
    while True:  # $label0
        v12 = load32(ENTITIES)
        v13 = load32(arg0 + 32)
        v1 = entities[load32(arg0 + 32)]
        v14 = load8u(entities[load32(arg0 + 32)].sub_state)
        v15 = load8u(v1 + 125)
        if not func162(arg0, load8u(entities[load32(arg0 + 32)].sub_state), load8u(v1 + 125), load32(v1 + 28)):
            break
        while True:  # $label1
            if (load32(38564) != v14):
                break
            if (load32(((v9 * 404) + ENTITY_TYPES) + 268) == 2):
                break
            v8 = load32(arg0 + 84)
            v1 = load32(PLAYERS)
            v6 = load16u(arg0 + 110)
            v3 = players[load16u(arg0 + 110)]
            if (u32(load32(arg0 + 84)) >= u32(load32((players[load16u(arg0 + 110)] + 284316)))):
                break
            v7 = load32((v3 + 284012))
            v2 = 10
            while True:  # $label2
                if load32(((v3 + (load32(38488) << 2)) + 281808)):
                    break
                v3 = (v1 + (v6 * 286704))
                if load32((((v1 + (v6 * 286704)) + (load32(38848) << 2)) + 281808)):
                    break
                v2 = (10 if load32(((v3 + (load32(38916) << 2)) + 281808)) else 0)
                break
            if (u32(v8) >= u32((v2 + v7))):
                break
            if not load32(((v1 + (v6 * 286704)) + 284008)):
                break
            v1 = (v12 + (v13 * 132))
            v6 = load16u((v12 + (v13 * 132)) + 112)
            while True:  # $label3
                if (v15 == 3):
                    v2 = load16u(v1 + 114)
                    v1 = load32(arg0 + 28)
                    break
                v5 = load32(9142840)
                v3 = (load32(9142440) + 2)
                v2 = load16u(v1 + 114)
                v8 = ((load32(9142440) + 2) + load16u(v1 + 114))
                v7 = (((load32(9142440) + 2) + load16u(v1 + 114)) * v3)
                v4 = load32((load32(9142840) + (((((load32(9142440) + 2) + load16u(v1 + 114)) * v3) + v6) << 2)))
                if not load32((load32(9142840) + (((((load32(9142440) + 2) + load16u(v1 + 114)) * v3) + v6) << 2))):
                    break
                v1 = load32(arg0 + 28)
                if (v4 == load32(arg0 + 28)):
                    break
                v10 = (((v2 + 1) + v3) * v3)
                v4 = load32((v5 + (((((v2 + 1) + v3) * v3) + v6) << 2)))
                if not load32((v5 + (((((v2 + 1) + v3) * v3) + v6) << 2))):
                    break
                if (v1 == v4):
                    break
                v4 = load32((v5 + ((((v8 + 2) * v3) + v6) << 2)))
                if not load32((v5 + ((((v8 + 2) * v3) + v6) << 2))):
                    break
                if (v1 == v4):
                    break
                v4 = (v6 + 1)
                v11 = load32((v5 + (((v6 + 1) + v7) << 2)))
                if not load32((v5 + (((v6 + 1) + v7) << 2))):
                    break
                if (v1 == v11):
                    break
                v4 = load32((v5 + ((((v8 + 2) * v3) + v4) << 2)))
                if not load32((v5 + ((((v8 + 2) * v3) + v4) << 2))):
                    break
                if (v1 == v4):
                    break
                v4 = (v6 + 2)
                v7 = load32((v5 + ((v7 + (v6 + 2)) << 2)))
                if not load32((v5 + ((v7 + (v6 + 2)) << 2))):
                    break
                if (v1 == v7):
                    break
                v7 = load32((v5 + ((v4 + v10) << 2)))
                if not load32((v5 + ((v4 + v10) << 2))):
                    break
                if (v1 == v7):
                    break
                v5 = load32((v5 + ((((v8 + 2) * v3) + v4) << 2)))
                if not load32((v5 + ((((v8 + 2) * v3) + v4) << 2))):
                    break
                if (v1 == v5):
                    break
                if (load32(((v9 * 404) + ENTITY_TYPES) + 224) > 1):
                    break
                break
            v1 = func250(v6, v2, v1)
            if not func250(v6, v2, v1):
                break
            store32(arg0 + 32, v1)
            store32(arg0 + 56, 0)
            return 0
            break
        v5 = 0
        while True:  # $label4
            v1 = load32(((v9 * 404) + ENTITY_TYPES) + 228)
            if not load32(((v9 * 404) + ENTITY_TYPES) + 228):
                break
            v4 = load32(((v14 * 404) + ENTITY_TYPES) + 216)
            if not load32(((v14 * 404) + ENTITY_TYPES) + 216):
                break
            v16 = (v4 & -4)
            v11 = (v4 & 3)
            v2 = (v12 + (v13 * 132))
            v17 = load16u((v12 + (v13 * 132)) + 114)
            v6 = load16u(v2 + 112)
            v3 = (v1 * v1)
            v18 = load16u(arg0 + 114)
            v9 = load16u(arg0 + 112)
            v19 = (u32(v4) < u32(4))
            v10 = 0
            v2 = 1
            while True:  # $label7
                v1 = (v18 - (v10 + v17))
                v8 = ((v18 - (v10 + v17)) * v1)
                v1 = 0
                v7 = 0
                if not v19:
                    while True:  # $label5
                        v2 = (v9 - (v1 + v6))
                        v2 = (v9 - ((v1 | 1) + v6))
                        v2 = (v9 - ((v1 | 2) + v6))
                        v2 = (v9 - ((v1 | 3) + v6))
                        v2 = ((((v2 if (u32((v8 + ((v9 - (v1 + v6)) * v2))) < u32(v3)) else 0) if (u32((v8 + ((v9 - ((v1 | 1) + v6)) * v2))) < u32(v3)) else 0) if (u32((v8 + ((v9 - ((v1 | 2) + v6)) * v2))) < u32(v3)) else 0) if (u32((v8 + ((v9 - ((v1 | 3) + v6)) * v2))) < u32(v3)) else 0)
                        v1 = (v1 + 4)
                        v7 = (v7 + 4)
                        if ((v7 + 4) != v16):
                            continue
                        break
                v7 = 0
                if v11:
                    while True:  # $label6
                        v2 = (v9 - (v1 + v6))
                        v2 = (v2 if (u32((v8 + ((v9 - (v1 + v6)) * v2))) < u32(v3)) else 0)
                        v1 = (v1 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v10 = (v10 + 1)
                if ((v10 + 1) != v4):
                    continue
                break
            break
        v2 = (v2 & 1)
        v1 = (v12 + (v13 * 132))
        while True:  # $label8
            if (v15 == 10):
                break
            if (v15 == 3):
                break
            if load32(v1 + 36):
                break
            if load8u(v1 + 128):
                break
            if not v2:
                break
            break
        v1 = func106(arg0, (-1 if (load8u(arg0 + 129) != 9) else v14), load16u(v1 + 112), load16u(v1 + 114))
        if func106(arg0, (-1 if (load8u(arg0 + 129) != 9) else v14), load16u(v1 + 112), load16u(v1 + 114)):
            store32(arg0 + 32, v1)
            store32(arg0 + 56, 0)
            if load8u(arg0 + 129):
                break
            store8(arg0 + 129, 5)
            return 0
        if (load8u(arg0 + 129) == 5):
            if func200(arg0, 0, 1, 0):
                break
        v5 = 1
        break
    return v5

# ----------------------------------------------------------
# $func922
# ----------------------------------------------------------
def func922(arg0, arg1, arg2):
    arg2 = 0
    v3 = load32(PLAYERS)
    while True:  # $label0
        v5 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v4 = load32(59164)
        arg1 = 1
        while True:  # $label1
            v6 = (v3 + (arg1 * 286704))
            if (v4 == load32((v3 + (arg1 * 286704)) + 284616)):
                arg2 = arg1
                break
            if (v4 == load32(v6 + 284628)):
                arg2 = arg1
                break
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != v5):
                continue
            break
        break
    arg1 = (v3 + (arg2 * 286704))
    store32((v3 + (arg2 * 286704)) + 283928, load32(arg0))
    store32(arg1 + 283932, load32(arg0 + 4))

# ----------------------------------------------------------
# $func923
# ----------------------------------------------------------
def func923(arg0, arg1):
    v6 = load32(ENTITIES)
    v5 = entities[arg0]
    if (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
        func29(v5, 1)
        return
    v2 = (v6 + (arg1 * 132))
    v4 = ((load8u((v6 + (arg1 * 132)) + 122) * 404) + ENTITY_TYPES)
    v10 = load32(((load8u((v6 + (arg1 * 132)) + 122) * 404) + ENTITY_TYPES) + 220)
    v3 = load16u(v2 + 114)
    v7 = (load32(((load8u((v6 + (arg1 * 132)) + 122) * 404) + ENTITY_TYPES) + 220) + load16u(v2 + 114))
    v11 = load32(v4 + 216)
    v8 = load16u(v2 + 112)
    v9 = (load32(v4 + 216) + load16u(v2 + 112))
    v2 = load16u(v5 + 114)
    while True:  # $label1
        while True:  # $label0
            v4 = load16u(v5 + 112)
            v12 = (u32(load16u(v5 + 112)) < u32(v8))
            if (u32(load16u(v5 + 112)) < u32(v8)):
                break
            if (v4 >= v9):
                break
            if (u32(v2) < u32(v3)):
                break
            if (v2 >= v7):
                break
            v3 = ((v10 // 2) + v3)
            v2 = (-1 if (v2 > v3) else (((v10 // 2) + v3) != v2))
            v3 = ((v11 // 2) + v8)
            break
            break
        v2 = (1 if (u32(v2) < u32(v3)) else (-1 if (v2 >= v7) else 0))
        break
    v4 = (1 if v12 else (-1 if (v4 >= v9) else 0))
    v3 = 6
    arg0 = (v6 + (arg0 * 132))
    v2 = (((v2 * 3) + v4) + 4)
    if (u32((((v2 * 3) + v4) + 4)) <= u32(8)):
    else:
    store8(load8u((v2 + 10184)) + 124, 6)
    arg0 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 276)
    func63(func37(v5, load32(((load8u(arg0 + 122) * 72) + 9263856) + 8), 0.0, 0), v5, 50, arg1, (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 276) if arg0 else 25))
    return (v6 + (arg0 * 132))

# ----------------------------------------------------------
# $func926
# ----------------------------------------------------------
def func926(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label0
        arg0 = load32(arg1)
        if load32(arg1):
            if load8u(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 335):
                break
        break
    return 1

# ----------------------------------------------------------
# $func927
# ----------------------------------------------------------
def func927(arg0, arg1):
    while True:  # $label0
        if (load8u(arg1 + 125) != 13):
            break
        while True:  # $label1
            v6 = load16u(arg1 + 112)
            v3 = load16u(arg1 + 114)
            v7 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
            v8 = load16u(arg1 + 110)
            if func56(load16u(arg1 + 112), load16u(arg1 + 114), ((load8u(arg1 + 122) * 404) + ENTITY_TYPES), load16u(arg1 + 110), 0, 0, 1, 1, 0):
                v2 = v6
                arg0 = v3
                break
            v4 = load32(9142440)
            arg0 = 0
            while True:  # $label3
                while True:  # $label2
                    v5 = arg0
                    v2 = (arg0 << 2)
                    arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v3)
                    if (u32(v4) <= u32((load32((((arg0 << 2) | 4) + 8611904)) + v3))):
                        break
                    v2 = (load32((v2 + 8611904)) + v6)
                    if (u32(v4) <= u32((load32((v2 + 8611904)) + v6))):
                        break
                    if ((arg0 | v2) < 0):
                        break
                    if func56(v2, arg0, v7, v8, 0, 0, 1, 1, 0):
                        break
                    v4 = load32(9142440)
                    break
                arg0 = (v5 + 2)
                if (u32(v5) < u32(5198)):
                    continue
                break
            break
            break
        store8(arg1 + 125, 0)
        store16(arg1 + 114, arg0)
        store16(arg1 + 112, v2)
        while True:  # $label4
            arg0 = load8u(arg1 + 122)
            if not load8u(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 377):
                break
            v5 = ((arg0 * 404) + ENTITY_TYPES)
            v4 = load32(((arg0 * 404) + ENTITY_TYPES) + 216)
            if (load32(((arg0 * 404) + ENTITY_TYPES) + 216) <= 0):
                break
            v2 = load16u(arg1 + 114)
            v7 = (load16u(arg1 + 114) + load32(v5 + 220))
            if ((load16u(arg1 + 114) + load32(v5 + 220)) <= v2):
                break
            v6 = load16u(arg1 + 112)
            v8 = (v4 + load16u(arg1 + 112))
            v9 = load32(v5 + 372)
            arg0 = v6
            while True:  # $label7
                v3 = (arg0 + 1)
                v10 = (arg0 - v6)
                v11 = load32(9142840)
                arg0 = v2
                while True:  # $label6
                    while True:  # $label5
                        if load8u((v9 + (v10 + ((arg0 - v2) * v4)))):
                            arg0 = (arg0 + 1)
                            break
                        v12 = (load32(9142440) + 2)
                        arg0 = (arg0 + 1)
                        store32((v11 + (((((load32(9142440) + 2) + (arg0 + 1)) * v12) + v3) << 2)), load32(v5 + 212))
                        break
                    if (arg0 != v7):
                        continue
                    break
                arg0 = v3
                if (v3 < v8):
                    continue
                break
            break
        func29(arg1, 1)
        while True:  # $label8
            if load32(arg1 + 40):
                break
            while True:  # $label9
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                arg0 = load8u(arg1 + 122)
                v3 = load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 216)
                if (load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 216) <= 0):
                    break
                arg0 = load32(((arg0 * 404) + ENTITY_TYPES) + 220)
                if (load32(((arg0 * 404) + ENTITY_TYPES) + 220) <= 0):
                    break
                v6 = load16u(arg1 + 114)
                v5 = (arg0 + load16u(arg1 + 114))
                v2 = load16u(arg1 + 112)
                v4 = (v3 + load16u(arg1 + 112))
                v7 = load32(9147376)
                v3 = load32(9142440)
                while True:  # $label11
                    arg0 = v6
                    if (u32(v2) < u32(v3)):
                        while True:  # $label10
                            if (u32(arg0) < u32(v3)):
                                if load16u((v7 + (((arg0 * v3) + v2) << 1))):
                                    break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) < v5):
                                continue
                            break
                    v2 = (v2 + 1)
                    if ((v2 + 1) < v4):
                        continue
                    break
                break
                break
            break
        while True:  # $label13
            while True:  # $label12
                arg0 = load8u(arg1 + 122)
                if (load8u(arg1 + 122) != load32(38600)):
                    if (load32(38472) != arg0):
                        break
                func286(arg1)
                break
                break
            if not load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 20):
                break
            break
        if not load8u(9142916):
            break
        break

# ----------------------------------------------------------
# $func928
# ----------------------------------------------------------
def func928(arg0, arg1):
    v2 = load32(ENTITIES)
    arg0 = (v2 + (arg0 * 132))
    func376(entities[load32((v2 + (arg0], (v2 + (arg1 * 132)))
    func29(arg0, 1)

# ----------------------------------------------------------
# $id
# Export: id
# ----------------------------------------------------------
def id():
    """Export: id"""
    v0 = load32(9142440)
    if (load32(9142440) * v0):
        while True:  # $label0
            v0 = (load32(9147288) + v1)
            store8((load32(9147288) + v1), load32((9147296 if load8u(v0) else 9147292)))
            v1 = (v1 + 1)
            v0 = load32(9142440)
            if (u32((v1 + 1)) < u32((load32(9142440) * v0))):
                continue
            break
    v1 = 0
    while True:  # $label1
        v3 = load32(9684496)
        v0 = load32((load32(9684496) - 16))
        if not load32((load32(9684496) - 16)):
            break
        if (u32(v0) >= u32(4)):
            v5 = (v0 & -4)
            while True:  # $label2
                v2 = ((v1 * 60) + v3)
                store32(((v1 * 60) + v3) + 208, 2147483647)
                store32(v2 + 148, 2147483647)
                store32(v2 + 88, 2147483647)
                store32(v2 + 28, 2147483647)
                v1 = (v1 + 4)
                v4 = (v4 + 4)
                if ((v4 + 4) != v5):
                    continue
                break
        v2 = (v0 & 3)
        if not (v0 & 3):
            break
        v0 = 0
        while True:  # $label3
            store32(((v1 * 60) + v3) + 28, 2147483647)
            v1 = (v1 + 1)
            v0 = (v0 + 1)
            if ((v0 + 1) != v2):
                continue
            break
        break
    store32(9140308, 0)
    hd()

# ----------------------------------------------------------
# $bf
# Export: bf
# ----------------------------------------------------------
def bf():
    """Export: bf"""
    v0 = G.global1
    v2 = G.global3
    v1 = load32(G.global3 + 116)
    if load32(G.global3 + 116):
        store32(v2 + 116, 0)
        G.global1 = v1
        # TODO: memory.fill
        return v1
    if (G.global2 if v0 else 1):
        G.global2 = 1
        v0 = e()
    G.global1 = v0
    # TODO: memory.fill
    return v0

# ----------------------------------------------------------
# $gf
# Export: gf
# ----------------------------------------------------------
def gf(arg0):
    """Export: gf"""
    arg0 = load32(arg0 + 44)
    func98(load32(arg0 + 44), 0, 136)

# ----------------------------------------------------------
# $ff
# Export: ff
# ----------------------------------------------------------
def ff(arg0, arg1, arg2, arg3):
    """Export: ff"""
    v4 = (G.global0 - 192)
    G.global0 = (G.global0 - 192)
    while True:  # $label0
        if arg3:
            atomic_store(v4 + 8, 0)
            store32(v4 + 184, 0)
            break
        break
    v5 = func799()
    store32(func799() + 16, arg1)
    store32(v5 + 4, arg0)
    store32(v5, -2129657856)
    store32(v5 + 188, (1 - arg3))
    arg0 = 0
    if (arg1 > 0):
        while True:  # $label1
            v6 = (arg0 + 1)
            store64((v5 + ((arg0 + 1) << 3)) + 16, load64((arg2 + (arg0 << 3))))
            arg0 = v6
            if (v6 != arg1):
                continue
            break
    while True:  # $label5
        if arg3:
            func384(v4)
            while True:  # $label2
                if atomic_load(v4 + 8):
                    break
                v7 = a_f()
                v8 = (v7 + inf)
                if (a_f() < (v7 + inf)):
                    arg0 = (v4 + 8)
                    while True:  # $label4
                        while True:  # $label3
                            arg1 = atomic_load(arg0)
                            v7 = a_f()
                            if arg1:
                                break
                            if (v7 < v8):
                                continue
                            break
                        break
                    if arg1:
                        break
                break
            break
        func384(v5)
        break
    v7 = 0.0
    G.global0 = (v4 + 192)
    return v7

# ----------------------------------------------------------
# $jf
# Export: jf
# ----------------------------------------------------------
def jf():
    """Export: jf"""
    v0 = load32(G.global3 + 120)
    atomic_store(load32(G.global3 + 120), 1)
    func248(0, v0)
    # TODO: i32.atomic.rmw.cmpxchg

# ----------------------------------------------------------
# $func939
# ----------------------------------------------------------
def func939():
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                # TODO: i32.atomic.rmw.cmpxchg
                # br_table 1
                break
                break
            G.global1 = 1024
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            # TODO: memory.init
            # TODO: memory.fill
            atomic_store(9690988, 2)
            # TODO: memory.atomic.notify
            break
            break
        # TODO: memory.atomic.wait32
        break
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop
    # TODO: data.drop

# ----------------------------------------------------------
# $func941
# ----------------------------------------------------------
def func941(arg0, arg1, arg2):
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v4 = load32(arg0 + 28)
    store32(v3 + 16, load32(arg0 + 28))
    v5 = load32(arg0 + 20)
    store32(v3 + 28, arg2)
    store32(v3 + 24, arg1)
    arg1 = (v5 - v4)
    store32(v3 + 20, (v5 - v4))
    v5 = (arg1 + arg2)
    v7 = 2
    while True:  # $label4
        while True:  # $label2
            while True:  # $label1
                while True:  # $label0
                    arg1 = (v3 + 16)
                    v4 = a_h()
                    if a_h():
                        store32(G.global3 + 28, v4)
                    else:
                    if 0:
                        v4 = arg1
                        break
                    while True:  # $label3
                        v6 = load32(v3 + 12)
                        if (v5 == load32(v3 + 12)):
                            break
                        if (v6 < 0):
                            v4 = arg1
                            break
                        v8 = load32(arg1 + 4)
                        v9 = (u32(v6) > u32(load32(arg1 + 4)))
                        v4 = (arg1 + ((u32(v6) > u32(load32(arg1 + 4))) << 3))
                        v8 = (v6 - (v8 if v9 else 0))
                        store32((arg1 + ((u32(v6) > u32(load32(arg1 + 4))) << 3)), ((v6 - (v8 if v9 else 0)) + load32(v4)))
                        arg1 = (arg1 + (12 if v9 else 4))
                        store32((arg1 + (12 if v9 else 4)), (load32(arg1) - v8))
                        v5 = (v5 - v6)
                        arg1 = v4
                        v7 = (v7 - v9)
                        v6 = a_h()
                        if a_h():
                            store32(G.global3 + 28, v6)
                        else:
                        if not 0:
                            continue
                        break
                    break
                if (v5 != -1):
                    break
                break
            arg1 = load32(arg0 + 44)
            store32(arg0 + 28, load32(arg0 + 44))
            store32(arg0 + 20, arg1)
            store32(arg0 + 16, (arg1 + load32(arg0 + 48)))
            break
            break
        store32(arg0 + 28, 0)
        store64(arg0 + 16, 0)
        store32(arg0, (load32(arg0) | 32))
        if (v7 == 2):
            break
        break
    arg0 = (arg2 - load32(v4 + 4))
    G.global0 = (v3 + 32)
    return arg0

# ----------------------------------------------------------
# $func942
# ----------------------------------------------------------
def func942(arg0, arg1, arg2):
    v3 = load32(arg0 + 60)
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg2 = a_j()
    if a_j():
        store32(G.global3 + 28, arg2)
    else:
    arg2 = 0
    arg1 = load64(arg0 + 8)
    G.global0 = (arg0 + 16)
    return (-1 if arg2 else arg1)

# ----------------------------------------------------------
# $func943
# ----------------------------------------------------------
def func943(arg0):
    return a_x(load32(arg0 + 60))

# ----------------------------------------------------------
# $func946
# ----------------------------------------------------------
def func946(arg0, arg1, arg2, arg3, arg4):
    if func79(arg0, load32(arg1 + 8), arg4):
        while True:  # $label0
            if (load32(arg1 + 4) != arg2):
                break
            if (load32(arg1 + 28) == 1):
                break
            store32(arg1 + 28, arg3)
            break
        return
    while True:  # $label2
        if func79(arg0, load32(arg1), arg4):
            while True:  # $label1
                if (arg2 != load32(arg1 + 16)):
                    if (load32(arg1 + 20) != arg2):
                        break
                if (arg3 != 1):
                    break
                store32(arg1 + 32, 1)
                return
                break
            store32(arg1 + 32, arg3)
            while True:  # $label3
                if (load32(arg1 + 44) == 4):
                    break
                store16(arg1 + 52, 0)
                arg0 = load32(arg0 + 8)
                if load8u(arg1 + 53):
                    store32(arg1 + 44, 3)
                    if not load8u(arg1 + 52):
                        break
                    break
                store32(arg1 + 44, 4)
                break
            store32(arg1 + 20, arg2)
            store32(arg1 + 40, (load32(arg1 + 40) + 1))
            if (load32(arg1 + 36) != 1):
                break
            if (load32(arg1 + 24) != 2):
                break
            store8(arg1 + 54, 1)
            return
        arg0 = load32(arg0 + 8)
        break

# ----------------------------------------------------------
# $func947
# ----------------------------------------------------------
def func947(arg0, arg1, arg2, arg3, arg4, arg5):
    if func79(arg0, load32(arg1 + 8), arg5):
        func441(arg1, arg2, arg3, arg4)
        return
    arg0 = load32(arg0 + 8)

# ----------------------------------------------------------
# $func948
# ----------------------------------------------------------
def func948(arg0, arg1, arg2, arg3):
    if func79(arg0, load32(arg1 + 8), 0):
        func442(arg1, arg2, arg3)
        return
    arg0 = load32(arg0 + 8)

# ----------------------------------------------------------
# $func949
# ----------------------------------------------------------
def func949(arg0, arg1, arg2, arg3, arg4):
    if func79(arg0, load32(arg1 + 8), arg4):
        while True:  # $label0
            if (load32(arg1 + 4) != arg2):
                break
            if (load32(arg1 + 28) == 1):
                break
            store32(arg1 + 28, arg3)
            break
        return
    while True:  # $label1
        if not func79(arg0, load32(arg1), arg4):
            break
        while True:  # $label2
            if (arg2 != load32(arg1 + 16)):
                if (load32(arg1 + 20) != arg2):
                    break
            if (arg3 != 1):
                break
            store32(arg1 + 32, 1)
            return
            break
        store32(arg1 + 20, arg2)
        store32(arg1 + 32, arg3)
        store32(arg1 + 40, (load32(arg1 + 40) + 1))
        while True:  # $label3
            if (load32(arg1 + 36) != 1):
                break
            if (load32(arg1 + 24) != 2):
                break
            store8(arg1 + 54, 1)
            break
        store32(arg1 + 44, 4)
        break

# ----------------------------------------------------------
# $func950
# ----------------------------------------------------------
def func950(arg0, arg1, arg2, arg3, arg4, arg5):
    if func79(arg0, load32(arg1 + 8), arg5):
        func441(arg1, arg2, arg3, arg4)

# ----------------------------------------------------------
# $func951
# ----------------------------------------------------------
def func951(arg0, arg1, arg2, arg3):
    if func79(arg0, load32(arg1 + 8), 0):
        func442(arg1, arg2, arg3)

# ----------------------------------------------------------
# $func952
# ----------------------------------------------------------
def func952(arg0, arg1, arg2):
    v3 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        if func79(arg0, arg1, 0):
            break
        if not arg1:
            break
        arg1 = func440(arg1, 32588)
        if not func440(arg1, 32588):
            break
        # TODO: memory.fill
        store32(v3 + 56, 1)
        store32(v3 + 20, -1)
        store32(v3 + 16, arg0)
        store32(v3 + 8, arg1)
        arg0 = load32(v3 + 32)
        if (load32(v3 + 32) == 1):
            store32(arg2, load32(v3 + 24))
        break
    arg0 = (arg0 == 1)
    G.global0 = (v3 - -64)
    return arg0

# ----------------------------------------------------------
# $func953
# ----------------------------------------------------------
def func953(arg0):
    if (load8s(9681935) < 0):

# ----------------------------------------------------------
# $func954
# ----------------------------------------------------------
def func954(arg0):
    arg0 = load32(9568064)
    if load32(9568064):
        v3 = load32(9568068)
        v1 = arg0
        if (load32(9568068) != arg0):
            while True:  # $label0
                v1 = (v3 - 128)
                v2 = load32((v3 - 128) + 12)
                if load32((v3 - 128) + 12):
                    store32((v3 - 112), v2)
                v2 = load32(v1)
                if load32(v1):
                    store32((v3 - 124), v2)
                v3 = v1
                if (v1 != arg0):
                    continue
                break
            v1 = load32(9568064)
        store32(9568068, arg0)

# ----------------------------------------------------------
# $of
# Export: of
# ----------------------------------------------------------
def of(arg0):
    """Export: of"""
    if not arg0:
        return 0
    return (func440(arg0, 32684) != 0)

# ----------------------------------------------------------
# $func956
# ----------------------------------------------------------
def func956(arg0, arg1, arg2, arg3, arg4):
    v7 = ((arg4 << 2) & -8)
    if ((arg4 << 2) & -8):
        v7 = (arg3 + v7)
        while True:  # $label0
            v5 = load8u(arg2)
            v8 = load8u(arg1)
            v6 = load8u(arg0)
            store8(arg3 + 3, 255)
            v9 = (((v8 * 33050) & 0xFFFFFFFF) >> 8)
            v6 = (((v6 * 19077) & 0xFFFFFFFF) >> 8)
            v10 = ((((v8 * 33050) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8))
            v11 = (((((v8 * 33050) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg3 + 2, ((((((((v8 * 33050) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (u32(v10) >= u32(17685)) else 0)))
            v10 = (((v5 * 26149) & 0xFFFFFFFF) >> 8)
            v11 = ((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6)
            v12 = (((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6) - 14234)
            store8(arg3, ((((((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (u32(v11) >= u32(14234)) else 0)))
            v8 = ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))
            v5 = (v6 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8)))
            v6 = ((v6 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg3 + 1, (((((v6 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (v5 >= -8708) else 0)))
            v5 = load8u(arg0 + 1)
            store8(arg3 + 7, 255)
            v5 = (((v5 * 19077) & 0xFFFFFFFF) >> 8)
            v6 = ((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9)
            v9 = (((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9) - 17685)
            store8(arg3 + 6, ((((((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v6) >= u32(17685)) else 0)))
            v8 = (v5 - v8)
            v6 = ((v5 - v8) + 8708)
            store8(arg3 + 5, (((((v5 - v8) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (v8 >= -8708) else 0)))
            v5 = (v5 + v10)
            v8 = ((v5 + v10) - 14234)
            store8(arg3 + 4, (((((v5 + v10) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v8) < u32(16384)) else (255 if (u32(v5) >= u32(14234)) else 0)))
            arg2 = (arg2 + 1)
            arg1 = (arg1 + 1)
            arg0 = (arg0 + 2)
            arg3 = (arg3 + 8)
            if ((arg3 + 8) != v7):
                continue
            break
        arg3 = v7
    if (arg4 & 1):
        arg2 = load8u(arg2)
        arg1 = load8u(arg1)
        arg0 = load8u(arg0)
        store8(arg3 + 3, 255)
        arg0 = (((arg0 * 19077) & 0xFFFFFFFF) >> 8)
        arg4 = ((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg1 * 33050) & 0xFFFFFFFF) >> 8))
        v7 = (((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg3 + 2, ((((((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
        arg4 = ((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0)
        v7 = (((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0) - 14234)
        store8(arg3, ((((((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
        arg0 = (arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
        arg1 = ((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg3 + 1, (((((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))

# ----------------------------------------------------------
# $func957
# ----------------------------------------------------------
def func957(arg0, arg1, arg2, arg3, arg4):
    v7 = ((arg4 << 1) & -4)
    if ((arg4 << 1) & -4):
        v7 = (arg3 + v7)
        while True:  # $label0
            v5 = load8u(arg2)
            v6 = load8u(arg1)
            v9 = (((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8)
            v8 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
            v10 = ((((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8))
            v11 = (((((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg3 + 1, (((((((((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (240 if (u32(v10) >= u32(17685)) else 0)) | 15))
            v10 = (((v5 * 26149) & 0xFFFFFFFF) >> 8)
            v11 = ((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v8)
            v12 = (((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v8) - 14234)
            v8 = ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v6 * 6419) & 0xFFFFFFFF) >> 8))
            v5 = (v8 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v6 * 6419) & 0xFFFFFFFF) >> 8)))
            v6 = ((v8 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v6 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg3, ((((((((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v8) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (240 if (u32(v11) >= u32(14234)) else 0)) & 240) | (((((v8 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v6 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v6) < u32(16384)) else (15 if (v5 >= -8708) else 0))))
            v5 = (((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8)
            v6 = ((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9)
            v9 = (((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9) - 17685)
            store8(arg3 + 3, (((((((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (240 if (u32(v6) >= u32(17685)) else 0)) | 15))
            v6 = (v5 + v10)
            v9 = ((v5 + v10) - 14234)
            v5 = (v5 - v8)
            v8 = ((v5 - v8) + 8708)
            store8(arg3 + 2, (((((((v5 + v10) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (240 if (u32(v6) >= u32(14234)) else 0)) & 240) | (((((v5 - v8) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v8) < u32(16384)) else (15 if (v5 >= -8708) else 0))))
            arg2 = (arg2 + 1)
            arg1 = (arg1 + 1)
            arg0 = (arg0 + 2)
            arg3 = (arg3 + 4)
            if ((arg3 + 4) != v7):
                continue
            break
        arg3 = v7
    if (arg4 & 1):
        arg2 = load8u(arg2)
        arg0 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
        arg1 = load8u(arg1)
        arg4 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8))
        v7 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg3 + 1, (((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (240 if (u32(arg4) >= u32(17685)) else 0)) | 15))
        arg3 = ((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0)
        arg4 = (((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0) - 14234)
        arg0 = (arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
        arg1 = ((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg3, ((((((((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0) - 14234) & 0xFFFFFFFF) >> 6) if (u32(arg4) < u32(16384)) else (240 if (u32(arg3) >= u32(14234)) else 0)) & 240) | (((((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(arg1) < u32(16384)) else (15 if (arg0 >= -8708) else 0))))

# ----------------------------------------------------------
# $func958
# ----------------------------------------------------------
def func958(arg0, arg1, arg2, arg3, arg4):
    v6 = (arg4 & -2)
    if (arg4 & -2):
        v6 = (arg3 + (v6 * 3))
        while True:  # $label0
            v5 = load8u(arg2)
            v8 = load8u(arg1)
            v9 = (((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8)
            v7 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
            v10 = ((((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8))
            v11 = (((((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg3 + 2, ((((((((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (u32(v10) >= u32(17685)) else 0)))
            v10 = (((v5 * 26149) & 0xFFFFFFFF) >> 8)
            v11 = ((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v7)
            v12 = (((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v7) - 14234)
            store8(arg3, ((((((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v7) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (u32(v11) >= u32(14234)) else 0)))
            v7 = ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))
            v5 = (v7 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8)))
            v8 = ((v7 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg3 + 1, (((((v7 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v8) < u32(16384)) else (255 if (v5 >= -8708) else 0)))
            v5 = (((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8)
            v8 = ((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9)
            v9 = (((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9) - 17685)
            store8(arg3 + 5, ((((((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v8) >= u32(17685)) else 0)))
            v7 = (v5 - v7)
            v8 = ((v5 - v7) + 8708)
            store8(arg3 + 4, (((((v5 - v7) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v8) < u32(16384)) else (255 if (v7 >= -8708) else 0)))
            v5 = (v5 + v10)
            v7 = ((v5 + v10) - 14234)
            store8(arg3 + 3, (((((v5 + v10) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (u32(v5) >= u32(14234)) else 0)))
            arg2 = (arg2 + 1)
            arg1 = (arg1 + 1)
            arg0 = (arg0 + 2)
            arg3 = (arg3 + 6)
            if ((arg3 + 6) != v6):
                continue
            break
        arg3 = v6
    if (arg4 & 1):
        arg2 = load8u(arg2)
        arg0 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
        arg1 = load8u(arg1)
        arg4 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8))
        v6 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg3 + 2, ((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
        arg4 = ((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0)
        v6 = (((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0) - 14234)
        store8(arg3, ((((((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
        arg0 = (arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
        arg1 = ((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg3 + 1, (((((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))

# ----------------------------------------------------------
# $func959
# ----------------------------------------------------------
def func959(arg0, arg1, arg2, arg3, arg4):
    v8 = ((arg4 << 1) & -4)
    if ((arg4 << 1) & -4):
        v8 = (arg3 + v8)
        while True:  # $label0
            v6 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
            v5 = load8u(arg2)
            v9 = load8u(arg1)
            v10 = ((((load8u(arg2) * 13320) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8))
            v7 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) - ((((load8u(arg2) * 13320) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8)))
            v11 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) - ((((load8u(arg2) * 13320) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            v7 = ((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) - ((((load8u(arg2) * 13320) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (v7 >= -8708) else 0))
            v5 = (((v5 * 26149) & 0xFFFFFFFF) >> 8)
            v11 = ((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6)
            v12 = (((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6) - 14234)
            store8(arg3, (((((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) - ((((load8u(arg2) * 13320) & 0xFFFFFFFF) >> 8) + (((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (v7 >= -8708) else 0)) & 0xFFFFFFFF) >> 5) | (((((((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (248 if (u32(v11) >= u32(14234)) else 0)) & 248)))
            v9 = (((v9 * 33050) & 0xFFFFFFFF) >> 8)
            v6 = ((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v6)
            v7 = (((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v6) - 17685)
            store8(arg3 + 1, (((v7 << 3) & 224) | ((((((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v6) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v7) < u32(16384)) else (31 if (u32(v6) >= u32(17685)) else 0))))
            v6 = (((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8)
            v5 = ((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v5)
            v7 = (((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v5) - 14234)
            v5 = (v6 - v10)
            v10 = ((v6 - v10) + 8708)
            v5 = (((((v6 - v10) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (v5 >= -8708) else 0))
            store8(arg3 + 2, ((((((((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v5) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (248 if (u32(v5) >= u32(14234)) else 0)) & 248) | (((((((v6 - v10) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (v5 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
            v6 = (v6 + v9)
            v5 = ((v6 + v9) - 17685)
            store8(arg3 + 3, (((v5 << 3) & 224) | (((((v6 + v9) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v5) < u32(16384)) else (31 if (u32(v6) >= u32(17685)) else 0))))
            arg2 = (arg2 + 1)
            arg1 = (arg1 + 1)
            arg0 = (arg0 + 2)
            arg3 = (arg3 + 4)
            if ((arg3 + 4) != v8):
                continue
            break
        arg3 = v8
    if (arg4 & 1):
        arg0 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
        arg2 = load8u(arg2)
        arg4 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8))
        v8 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        arg1 = load8u(arg1)
        arg2 = (arg0 - ((((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
        arg4 = ((arg0 - ((((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        arg2 = (((((arg0 - ((((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg4) < u32(16384)) else (255 if (arg2 >= -8708) else 0))
        store8(arg3, ((((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v8) < u32(16384)) else (248 if (u32(arg4) >= u32(14234)) else 0)) & 248) | (((((((arg0 - ((((load8u(arg1) * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg4) < u32(16384)) else (255 if (arg2 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
        arg0 = ((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0)
        arg1 = (((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0) - 17685)
        store8(arg3 + 1, (((arg2 << 3) & 224) | ((((((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0) - 17685) & 0xFFFFFFFF) >> 9) if (u32(arg1) < u32(16384)) else (31 if (u32(arg0) >= u32(17685)) else 0))))

# ----------------------------------------------------------
# $func960
# ----------------------------------------------------------
def func960(arg0, arg1, arg2, arg3, arg4):
    v7 = ((arg4 << 2) & -8)
    if ((arg4 << 2) & -8):
        v7 = (arg3 + v7)
        while True:  # $label0
            v5 = load8u(arg1)
            v8 = load8u(arg2)
            v6 = load8u(arg0)
            store8(arg3 + 3, 255)
            v9 = (((v8 * 26149) & 0xFFFFFFFF) >> 8)
            v6 = (((v6 * 19077) & 0xFFFFFFFF) >> 8)
            v10 = ((((v8 * 26149) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8))
            v11 = (((((v8 * 26149) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg3 + 2, ((((((((v8 * 26149) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (u32(v10) >= u32(14234)) else 0)))
            v10 = (((v5 * 33050) & 0xFFFFFFFF) >> 8)
            v11 = ((((v5 * 33050) & 0xFFFFFFFF) >> 8) + v6)
            v12 = (((((v5 * 33050) & 0xFFFFFFFF) >> 8) + v6) - 17685)
            store8(arg3, ((((((((v5 * 33050) & 0xFFFFFFFF) >> 8) + v6) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (u32(v11) >= u32(17685)) else 0)))
            v8 = ((((v8 * 13320) & 0xFFFFFFFF) >> 8) + (((v5 * 6419) & 0xFFFFFFFF) >> 8))
            v5 = (v6 - ((((v8 * 13320) & 0xFFFFFFFF) >> 8) + (((v5 * 6419) & 0xFFFFFFFF) >> 8)))
            v6 = ((v6 - ((((v8 * 13320) & 0xFFFFFFFF) >> 8) + (((v5 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg3 + 1, (((((v6 - ((((v8 * 13320) & 0xFFFFFFFF) >> 8) + (((v5 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (v5 >= -8708) else 0)))
            v5 = load8u(arg0 + 1)
            store8(arg3 + 7, 255)
            v5 = (((v5 * 19077) & 0xFFFFFFFF) >> 8)
            v6 = ((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9)
            v9 = (((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9) - 14234)
            store8(arg3 + 6, ((((((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v6) >= u32(14234)) else 0)))
            v8 = (v5 - v8)
            v6 = ((v5 - v8) + 8708)
            store8(arg3 + 5, (((((v5 - v8) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (v8 >= -8708) else 0)))
            v5 = (v5 + v10)
            v8 = ((v5 + v10) - 17685)
            store8(arg3 + 4, (((((v5 + v10) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v8) < u32(16384)) else (255 if (u32(v5) >= u32(17685)) else 0)))
            arg2 = (arg2 + 1)
            arg1 = (arg1 + 1)
            arg0 = (arg0 + 2)
            arg3 = (arg3 + 8)
            if ((arg3 + 8) != v7):
                continue
            break
        arg3 = v7
    if (arg4 & 1):
        arg1 = load8u(arg1)
        arg2 = load8u(arg2)
        arg0 = load8u(arg0)
        store8(arg3 + 3, 255)
        arg0 = (((arg0 * 19077) & 0xFFFFFFFF) >> 8)
        arg4 = ((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg2 * 26149) & 0xFFFFFFFF) >> 8))
        v7 = (((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg2 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        store8(arg3 + 2, ((((((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg2 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
        arg4 = ((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0)
        v7 = (((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0) - 17685)
        store8(arg3, ((((((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
        arg0 = (arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
        arg1 = ((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg3 + 1, (((((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))

# ----------------------------------------------------------
# $func961
# ----------------------------------------------------------
def func961(arg0, arg1, arg2, arg3, arg4):
    v6 = (arg4 & -2)
    if (arg4 & -2):
        v6 = (arg3 + (v6 * 3))
        while True:  # $label0
            v5 = load8u(arg1)
            v8 = load8u(arg2)
            v9 = (((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8)
            v7 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
            v10 = ((((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8))
            v11 = (((((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(arg3 + 2, ((((((((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8) + (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (u32(v10) >= u32(14234)) else 0)))
            v10 = (((v5 * 33050) & 0xFFFFFFFF) >> 8)
            v11 = ((((v5 * 33050) & 0xFFFFFFFF) >> 8) + v7)
            v12 = (((((v5 * 33050) & 0xFFFFFFFF) >> 8) + v7) - 17685)
            store8(arg3, ((((((((v5 * 33050) & 0xFFFFFFFF) >> 8) + v7) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (u32(v11) >= u32(17685)) else 0)))
            v7 = ((((v8 * 13320) & 0xFFFFFFFF) >> 8) + (((v5 * 6419) & 0xFFFFFFFF) >> 8))
            v5 = (v7 - ((((v8 * 13320) & 0xFFFFFFFF) >> 8) + (((v5 * 6419) & 0xFFFFFFFF) >> 8)))
            v8 = ((v7 - ((((v8 * 13320) & 0xFFFFFFFF) >> 8) + (((v5 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg3 + 1, (((((v7 - ((((v8 * 13320) & 0xFFFFFFFF) >> 8) + (((v5 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v8) < u32(16384)) else (255 if (v5 >= -8708) else 0)))
            v5 = (((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8)
            v8 = ((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9)
            v9 = (((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9) - 14234)
            store8(arg3 + 5, ((((((((load8u(arg0 + 1) * 19077) & 0xFFFFFFFF) >> 8) + v9) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v8) >= u32(14234)) else 0)))
            v7 = (v5 - v7)
            v8 = ((v5 - v7) + 8708)
            store8(arg3 + 4, (((((v5 - v7) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v8) < u32(16384)) else (255 if (v7 >= -8708) else 0)))
            v5 = (v5 + v10)
            v7 = ((v5 + v10) - 17685)
            store8(arg3 + 3, (((((v5 + v10) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (u32(v5) >= u32(17685)) else 0)))
            arg2 = (arg2 + 1)
            arg1 = (arg1 + 1)
            arg0 = (arg0 + 2)
            arg3 = (arg3 + 6)
            if ((arg3 + 6) != v6):
                continue
            break
        arg3 = v6
    if (arg4 & 1):
        arg1 = load8u(arg1)
        arg0 = (((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8)
        arg2 = load8u(arg2)
        arg4 = ((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8))
        v6 = (((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
        store8(arg3 + 2, ((((((((load8u(arg0) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u(arg2) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
        arg4 = ((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0)
        v6 = (((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0) - 17685)
        store8(arg3, ((((((((arg1 * 33050) & 0xFFFFFFFF) >> 8) + arg0) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
        arg0 = (arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
        arg1 = ((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg3 + 1, (((((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))

# ----------------------------------------------------------
# $func962
# ----------------------------------------------------------
def func962(arg0, arg1, arg2, arg3, arg4):
    v7 = ((arg4 << 2) & -8)
    if ((arg4 << 2) & -8):
        v7 = (arg3 + v7)
        while True:  # $label0
            v5 = load8u(arg2)
            v8 = load8u(arg1)
            v6 = load8u(arg0)
            store8(arg3, 255)
            v9 = (((v8 * 33050) & 0xFFFFFFFF) >> 8)
            v6 = (((v6 * 19077) & 0xFFFFFFFF) >> 8)
            v10 = ((((v8 * 33050) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8))
            v11 = (((((v8 * 33050) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(arg3 + 3, ((((((((v8 * 33050) & 0xFFFFFFFF) >> 8) + (((v6 * 19077) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (255 if (u32(v10) >= u32(17685)) else 0)))
            v10 = (((v5 * 26149) & 0xFFFFFFFF) >> 8)
            v11 = ((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6)
            v12 = (((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6) - 14234)
            store8(arg3 + 1, ((((((((v5 * 26149) & 0xFFFFFFFF) >> 8) + v6) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v12) < u32(16384)) else (255 if (u32(v11) >= u32(14234)) else 0)))
            v8 = ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))
            v5 = (v6 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8)))
            v6 = ((v6 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(arg3 + 2, (((((v6 - ((((v5 * 13320) & 0xFFFFFFFF) >> 8) + (((v8 * 6419) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (v5 >= -8708) else 0)))
            v5 = load8u(arg0 + 1)
            store8(arg3 + 4, 255)
            v5 = (((v5 * 19077) & 0xFFFFFFFF) >> 8)
            v6 = ((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9)
            v9 = (((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9) - 17685)
            store8(arg3 + 7, ((((((((v5 * 19077) & 0xFFFFFFFF) >> 8) + v9) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v6) >= u32(17685)) else 0)))
            v8 = (v5 - v8)
            v6 = ((v5 - v8) + 8708)
            store8(arg3 + 6, (((((v5 - v8) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v6) < u32(16384)) else (255 if (v8 >= -8708) else 0)))
            v5 = (v5 + v10)
            v8 = ((v5 + v10) - 14234)
            store8(arg3 + 5, (((((v5 + v10) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v8) < u32(16384)) else (255 if (u32(v5) >= u32(14234)) else 0)))
            arg2 = (arg2 + 1)
            arg1 = (arg1 + 1)
            arg0 = (arg0 + 2)
            arg3 = (arg3 + 8)
            if ((arg3 + 8) != v7):
                continue
            break
        arg3 = v7
    if (arg4 & 1):
        arg2 = load8u(arg2)
        arg1 = load8u(arg1)
        arg0 = load8u(arg0)
        store8(arg3, 255)
        arg0 = (((arg0 * 19077) & 0xFFFFFFFF) >> 8)
        arg4 = ((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg1 * 33050) & 0xFFFFFFFF) >> 8))
        v7 = (((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
        store8(arg3 + 3, ((((((((arg0 * 19077) & 0xFFFFFFFF) >> 8) + (((arg1 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (u32(arg4) >= u32(17685)) else 0)))
        arg4 = ((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0)
        v7 = (((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0) - 14234)
        store8(arg3 + 1, ((((((((arg2 * 26149) & 0xFFFFFFFF) >> 8) + arg0) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (u32(arg4) >= u32(14234)) else 0)))
        arg0 = (arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8)))
        arg1 = ((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
        store8(arg3 + 2, (((((arg0 - ((((arg1 * 6419) & 0xFFFFFFFF) >> 8) + (((arg2 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(arg1) < u32(16384)) else (255 if (arg0 >= -8708) else 0)))

# ----------------------------------------------------------
# $func963
# ----------------------------------------------------------
def func963(arg0, arg1, arg2, arg3, arg4):
    if (arg4 > 0):
        while True:  # $label0
            v7 = load8u((arg2 + v5))
            v11 = load8u((arg1 + v5))
            v8 = load8u((arg0 + v5))
            v6 = (arg3 + (v5 << 2))
            store8((arg3 + (v5 << 2)) + 3, 255)
            v8 = (((v8 * 19077) & 0xFFFFFFFF) >> 8)
            v9 = ((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 33050) & 0xFFFFFFFF) >> 8))
            v10 = (((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(v6 + 2, ((((((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (u32(v9) >= u32(17685)) else 0)))
            v9 = ((((v7 * 26149) & 0xFFFFFFFF) >> 8) + v8)
            v10 = (((((v7 * 26149) & 0xFFFFFFFF) >> 8) + v8) - 14234)
            store8(v6, ((((((((v7 * 26149) & 0xFFFFFFFF) >> 8) + v8) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (u32(v9) >= u32(14234)) else 0)))
            v6 = (v8 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v7 * 13320) & 0xFFFFFFFF) >> 8)))
            v7 = ((v8 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v7 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(v6 + 1, (((((v8 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v7 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (v6 >= -8708) else 0)))
            v5 = (v5 + 1)
            if ((v5 + 1) != arg4):
                continue
            break

# ----------------------------------------------------------
# $func964
# ----------------------------------------------------------
def func964(arg0, arg1, arg2, arg3, arg4):
    if (arg4 > 0):
        while True:  # $label0
            v6 = load8u((arg2 + v5))
            v8 = (arg3 + (v5 << 1))
            v7 = (((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8)
            v10 = load8u((arg1 + v5))
            v9 = ((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg1 + v5)) * 33050) & 0xFFFFFFFF) >> 8))
            v11 = (((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg1 + v5)) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8((arg3 + (v5 << 1)) + 1, (((((((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg1 + v5)) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v11) < u32(16384)) else (240 if (u32(v9) >= u32(17685)) else 0)) | 15))
            v8 = ((((v6 * 26149) & 0xFFFFFFFF) >> 8) + v7)
            v9 = (((((v6 * 26149) & 0xFFFFFFFF) >> 8) + v7) - 14234)
            v6 = (v7 - ((((v10 * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8)))
            v7 = ((v7 - ((((v10 * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(v8, ((((((((((v6 * 26149) & 0xFFFFFFFF) >> 8) + v7) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (240 if (u32(v8) >= u32(14234)) else 0)) & 240) | (((((v7 - ((((v10 * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 10) if (u32(v7) < u32(16384)) else (15 if (v6 >= -8708) else 0))))
            v5 = (v5 + 1)
            if ((v5 + 1) != arg4):
                continue
            break

# ----------------------------------------------------------
# $func965
# ----------------------------------------------------------
def func965(arg0, arg1, arg2, arg3, arg4):
    if (arg4 > 0):
        while True:  # $label0
            v6 = load8u((arg2 + v5))
            v7 = (arg3 + (v5 * 3))
            v10 = (((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8)
            v11 = load8u((arg1 + v5))
            v8 = ((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg1 + v5)) * 33050) & 0xFFFFFFFF) >> 8))
            v9 = (((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg1 + v5)) * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8((arg3 + (v5 * 3)) + 2, ((((((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg1 + v5)) * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v8) >= u32(17685)) else 0)))
            v8 = ((((v6 * 26149) & 0xFFFFFFFF) >> 8) + v10)
            v9 = (((((v6 * 26149) & 0xFFFFFFFF) >> 8) + v10) - 14234)
            store8(v7, ((((((((v6 * 26149) & 0xFFFFFFFF) >> 8) + v10) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v8) >= u32(14234)) else 0)))
            v6 = (v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8)))
            v7 = ((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(v7 + 1, (((((v10 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (v6 >= -8708) else 0)))
            v5 = (v5 + 1)
            if ((v5 + 1) != arg4):
                continue
            break

# ----------------------------------------------------------
# $func966
# ----------------------------------------------------------
def func966(arg0, arg1, arg2, arg3, arg4):
    if (arg4 > 0):
        while True:  # $label0
            v8 = (arg3 + (v5 << 1))
            v7 = (((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8)
            v6 = load8u((arg2 + v5))
            v9 = ((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg2 + v5)) * 26149) & 0xFFFFFFFF) >> 8))
            v10 = (((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg2 + v5)) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            v9 = load8u((arg1 + v5))
            v6 = (v7 - ((((load8u((arg1 + v5)) * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8)))
            v10 = ((v7 - ((((load8u((arg1 + v5)) * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            v6 = (((((v7 - ((((load8u((arg1 + v5)) * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (v6 >= -8708) else 0))
            store8((arg3 + (v5 << 1)), ((((((((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg2 + v5)) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (248 if (u32(v9) >= u32(14234)) else 0)) & 248) | (((((((v7 - ((((load8u((arg1 + v5)) * 6419) & 0xFFFFFFFF) >> 8) + (((v6 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (v6 >= -8708) else 0)) & 0xFFFFFFFF) >> 5)))
            v7 = ((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v7)
            v8 = (((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v7) - 17685)
            store8(v8 + 1, (((v6 << 3) & 224) | ((((((((v9 * 33050) & 0xFFFFFFFF) >> 8) + v7) - 17685) & 0xFFFFFFFF) >> 9) if (u32(v8) < u32(16384)) else (31 if (u32(v7) >= u32(17685)) else 0))))
            v5 = (v5 + 1)
            if ((v5 + 1) != arg4):
                continue
            break

# ----------------------------------------------------------
# $func967
# ----------------------------------------------------------
def func967(arg0, arg1, arg2, arg3, arg4):
    if (arg4 > 0):
        while True:  # $label0
            v7 = load8u((arg1 + v5))
            v11 = load8u((arg2 + v5))
            v8 = load8u((arg0 + v5))
            v6 = (arg3 + (v5 << 2))
            store8((arg3 + (v5 << 2)) + 3, 255)
            v8 = (((v8 * 19077) & 0xFFFFFFFF) >> 8)
            v9 = ((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 26149) & 0xFFFFFFFF) >> 8))
            v10 = (((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8(v6 + 2, ((((((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (u32(v9) >= u32(14234)) else 0)))
            v9 = ((((v7 * 33050) & 0xFFFFFFFF) >> 8) + v8)
            v10 = (((((v7 * 33050) & 0xFFFFFFFF) >> 8) + v8) - 17685)
            store8(v6, ((((((((v7 * 33050) & 0xFFFFFFFF) >> 8) + v8) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (u32(v9) >= u32(17685)) else 0)))
            v6 = (v8 - ((((v7 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8)))
            v7 = ((v8 - ((((v7 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(v6 + 1, (((((v8 - ((((v7 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (v6 >= -8708) else 0)))
            v5 = (v5 + 1)
            if ((v5 + 1) != arg4):
                continue
            break

# ----------------------------------------------------------
# $func968
# ----------------------------------------------------------
def func968(arg0, arg1, arg2, arg3, arg4):
    if (arg4 > 0):
        while True:  # $label0
            v6 = load8u((arg1 + v5))
            v7 = (arg3 + (v5 * 3))
            v10 = (((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8)
            v11 = load8u((arg2 + v5))
            v8 = ((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg2 + v5)) * 26149) & 0xFFFFFFFF) >> 8))
            v9 = (((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg2 + v5)) * 26149) & 0xFFFFFFFF) >> 8)) - 14234)
            store8((arg3 + (v5 * 3)) + 2, ((((((((load8u((arg0 + v5)) * 19077) & 0xFFFFFFFF) >> 8) + (((load8u((arg2 + v5)) * 26149) & 0xFFFFFFFF) >> 8)) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v8) >= u32(14234)) else 0)))
            v8 = ((((v6 * 33050) & 0xFFFFFFFF) >> 8) + v10)
            v9 = (((((v6 * 33050) & 0xFFFFFFFF) >> 8) + v10) - 17685)
            store8(v7, ((((((((v6 * 33050) & 0xFFFFFFFF) >> 8) + v10) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v9) < u32(16384)) else (255 if (u32(v8) >= u32(17685)) else 0)))
            v6 = (v10 - ((((v6 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8)))
            v7 = ((v10 - ((((v6 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(v7 + 1, (((((v10 - ((((v6 * 6419) & 0xFFFFFFFF) >> 8) + (((v11 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (v6 >= -8708) else 0)))
            v5 = (v5 + 1)
            if ((v5 + 1) != arg4):
                continue
            break

# ----------------------------------------------------------
# $func969
# ----------------------------------------------------------
def func969(arg0, arg1, arg2, arg3, arg4):
    if (arg4 > 0):
        while True:  # $label0
            v7 = load8u((arg2 + v5))
            v11 = load8u((arg1 + v5))
            v8 = load8u((arg0 + v5))
            v6 = (arg3 + (v5 << 2))
            store8((arg3 + (v5 << 2)), 255)
            v8 = (((v8 * 19077) & 0xFFFFFFFF) >> 8)
            v9 = ((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 33050) & 0xFFFFFFFF) >> 8))
            v10 = (((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 33050) & 0xFFFFFFFF) >> 8)) - 17685)
            store8(v6 + 3, ((((((((v8 * 19077) & 0xFFFFFFFF) >> 8) + (((v11 * 33050) & 0xFFFFFFFF) >> 8)) - 17685) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (u32(v9) >= u32(17685)) else 0)))
            v9 = ((((v7 * 26149) & 0xFFFFFFFF) >> 8) + v8)
            v10 = (((((v7 * 26149) & 0xFFFFFFFF) >> 8) + v8) - 14234)
            store8(v6 + 1, ((((((((v7 * 26149) & 0xFFFFFFFF) >> 8) + v8) - 14234) & 0xFFFFFFFF) >> 6) if (u32(v10) < u32(16384)) else (255 if (u32(v9) >= u32(14234)) else 0)))
            v6 = (v8 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v7 * 13320) & 0xFFFFFFFF) >> 8)))
            v7 = ((v8 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v7 * 13320) & 0xFFFFFFFF) >> 8))) + 8708)
            store8(v6 + 2, (((((v8 - ((((v11 * 6419) & 0xFFFFFFFF) >> 8) + (((v7 * 13320) & 0xFFFFFFFF) >> 8))) + 8708) & 0xFFFFFFFF) >> 6) if (u32(v7) < u32(16384)) else (255 if (v6 >= -8708) else 0)))
            v5 = (v5 + 1)
            if ((v5 + 1) != arg4):
                continue
            break

# ----------------------------------------------------------
# $func970
# ----------------------------------------------------------
def func970(arg0, arg1):
    while True:  # $label3
        if (load32(arg0 + 60) < load32(arg0 + 48)):
            while True:  # $label0
                while True:  # $label1
                    if not load32(arg0):
                        v4 = load32(arg0 + 8)
                        if (load32(arg0 + 8) <= 0):
                            break
                        v11 = (load32(arg0 + 52) * v4)
                        break
                    a_c()
                    raise Unreachable()
                    break
                while True:  # $label7
                    while True:  # $label6
                        if (v7 < v11):
                            v12 = load32(arg0 + 36)
                            v2 = 0
                            v5 = 0
                            v8 = v7
                            v6 = v7
                            while True:  # $label5
                                while True:  # $label2
                                    v2 = (v2 + v12)
                                    if ((v2 + v12) <= 0):
                                        v9 = load32(arg0 + 40)
                                        v10 = 0
                                        break
                                    v13 = (load32(arg0 + 44) * v4)
                                    if (v6 >= (load32(arg0 + 44) * v4)):
                                        break
                                    v3 = (v4 + v6)
                                    v10 = load8u((arg1 + v6))
                                    v5 = (v5 + load8u((arg1 + v6)))
                                    v9 = load32(arg0 + 40)
                                    v2 = (v2 - load32(arg0 + 40))
                                    if ((v2 - load32(arg0 + 40)) <= 0):
                                        v6 = v3
                                        break
                                    while True:  # $label4
                                        if (v3 >= v13):
                                            break
                                        v10 = load8u((arg1 + v3))
                                        v5 = (v5 + load8u((arg1 + v3)))
                                        v6 = (v3 + v4)
                                        v3 = (v3 + v4)
                                        v2 = (v2 - v9)
                                        if ((v2 - v9) > 0):
                                            continue
                                        break
                                    break
                                v3 = (v2 * v10)
                                store32((load32(arg0 + 80) + (v8 << 2)), ((v2 * v10) + (v5 * v9)))
                                v5 = i32(((((load32(arg0 + 12) * i32((0 - v3))) + 2147483648) & 0xFFFFFFFF) >> 32))
                                v8 = (v4 + v8)
                                if ((v4 + v8) < v11):
                                    continue
                                break
                            if v2:
                                break
                        v7 = (v7 + 1)
                        if (v4 != (v7 + 1)):
                            continue
                        break
                        break
                    break
                a_c()
                raise Unreachable()
                break
            return
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func971
# ----------------------------------------------------------
def func971(arg0, arg1):
    while True:  # $label1
        while True:  # $label0
            while True:  # $label3
                while True:  # $label5
                    while True:  # $label7
                        if (load32(arg0 + 60) < load32(arg0 + 48)):
                            if not load32(arg0):
                                break
                            v4 = load32(arg0 + 8)
                            if (load32(arg0 + 8) <= 0):
                                break
                            v10 = (load32(arg0 + 52) * v4)
                            v2 = load32(arg0 + 44)
                            v13 = (load32(arg0 + 44) * v4)
                            v11 = load32(arg0 + 80)
                            v7 = load32(arg0 + 36)
                            if (v2 > 1):
                                while True:  # $label6
                                    v5 = (v3 + v4)
                                    v6 = load8u((arg1 + (v3 + v4)))
                                    v9 = load8u((arg1 + v3))
                                    store32((v11 + (v3 << 2)), (v7 * load8u((arg1 + v3))))
                                    while True:  # $label2
                                        if (v5 >= v10):
                                            v12 = load32(arg0 + 40)
                                            v2 = v7
                                            break
                                        v12 = load32(arg0 + 40)
                                        v2 = v7
                                        v8 = v5
                                        while True:  # $label4
                                            v2 = (v2 - v12)
                                            if ((v2 - v12) < 0):
                                                v8 = (v4 + v8)
                                                if ((v4 + v8) >= v13):
                                                    break
                                                v9 = v6
                                                v6 = load8u((arg1 + v8))
                                                v2 = (v2 + v7)
                                            store32((v11 + (v5 << 2)), (((v9 - v6) * v2) + (v6 * v7)))
                                            v5 = (v4 + v5)
                                            if ((v4 + v5) < v10):
                                                continue
                                            break
                                        break
                                    if (v12 if v2 else 0):
                                        break
                                    v3 = (v3 + 1)
                                    if ((v3 + 1) != v4):
                                        continue
                                    break
                                break
                            arg0 = load32(arg0 + 40)
                            break
                        a_c()
                        raise Unreachable()
                        break
                    while True:  # $label9
                        v6 = load8u((arg1 + v3))
                        store32((v11 + (v3 << 2)), (v7 * load8u((arg1 + v3))))
                        v9 = v6
                        v2 = v7
                        v5 = (v3 + v4)
                        v8 = (v3 + v4)
                        if (v5 < v10):
                            while True:  # $label8
                                v2 = (v2 - arg0)
                                if ((v2 - arg0) < 0):
                                    v8 = (v4 + v8)
                                    if ((v4 + v8) >= v13):
                                        break
                                    v9 = v6
                                    v6 = load8u((arg1 + v8))
                                    v2 = (v2 + v7)
                                store32((v11 + (v5 << 2)), (((v9 - v6) * v2) + (v6 * v7)))
                                v5 = (v4 + v5)
                                if ((v4 + v5) < v10):
                                    continue
                                break
                        if (arg0 if v2 else 0):
                            break
                        v3 = (v3 + 1)
                        if (v4 != (v3 + 1)):
                            continue
                        break
                    break
                    break
                a_c()
                raise Unreachable()
                break
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break

# ----------------------------------------------------------
# $func972
# ----------------------------------------------------------
def func972(arg0):
    while True:  # $label1
        while True:  # $label0
            if (load32((arg0 - -64)) < load32(arg0 + 56)):
                v1 = load32(arg0 + 24)
                if (load32(arg0 + 24) > 0):
                    break
                if load32(arg0 + 4):
                    break
                v3 = (load32(arg0 + 8) * load32(arg0 + 52))
                v6 = load32(arg0 + 76)
                v7 = load32(arg0 + 68)
                while True:  # $label2
                    v1 = (v1 * load32(arg0 + 16))
                    if (v1 * load32(arg0 + 16)):
                        if (v3 <= 0):
                            break
                        v8 = load32(arg0 + 80)
                        v9 = i32((0 - v1))
                        v1 = 0
                        while True:  # $label3
                            v4 = (v1 << 2)
                            v2 = (v6 + (v1 << 2))
                            v4 = i32((((load32((v4 + v8)) * v9) & 0xFFFFFFFF) >> 32))
                            v5 = i32(((((load32(arg0 + 20) * i32((load32((v6 + (v1 << 2))) - i32((((load32((v4 + v8)) * v9) & 0xFFFFFFFF) >> 32))))) + 2147483648) & 0xFFFFFFFF) >> 32))
                            store8((v1 + v7), (-1 if (v5 > 255) else i32(((((load32(arg0 + 20) * i32((load32((v6 + (v1 << 2))) - i32((((load32((v4 + v8)) * v9) & 0xFFFFFFFF) >> 32))))) + 2147483648) & 0xFFFFFFFF) >> 32))))
                            store32(v2, v4)
                            v1 = (v1 + 1)
                            if ((v1 + 1) != v3):
                                continue
                            break
                        break
                    if (v3 <= 0):
                        break
                    v1 = 0
                    if (v3 != 1):
                        v4 = (v3 & -2)
                        while True:  # $label4
                            v2 = (v6 + (v1 << 2))
                            v5 = i32(((((load32(arg0 + 20) * load32((v6 + (v1 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))
                            store8((v1 + v7), (-1 if (v5 > 255) else i32(((((load32(arg0 + 20) * load32((v6 + (v1 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))))
                            store32(v2, 0)
                            v2 = (v1 | 1)
                            v2 = (v6 + (v2 << 2))
                            v5 = i32(((((load32(arg0 + 20) * load32((v6 + (v2 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))
                            store8((v7 + (v1 | 1)), (-1 if (v5 > 255) else i32(((((load32(arg0 + 20) * load32((v6 + (v2 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))))
                            store32(v2, 0)
                            v1 = (v1 + 2)
                            v8 = (v8 + 2)
                            if ((v8 + 2) != v4):
                                continue
                            break
                    if not (v3 & 1):
                        break
                    arg0 = (v6 + (v1 << 2))
                    v1 = i32(((((load32(arg0 + 20) * load32((v6 + (v1 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))
                    store8((v1 + v7), (-1 if (v1 > 255) else i32(((((load32(arg0 + 20) * load32((v6 + (v1 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))))
                    store32(arg0, 0)
                    break
                return
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func973
# ----------------------------------------------------------
def func973(arg0):
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                if (load32((arg0 - -64)) < load32(arg0 + 56)):
                    v2 = load32(arg0 + 24)
                    if (load32(arg0 + 24) > 0):
                        break
                    if not load32(arg0 + 4):
                        break
                    v3 = load32(arg0 + 32)
                    if not load32(arg0 + 32):
                        break
                    v4 = (load32(arg0 + 8) * load32(arg0 + 52))
                    v6 = load32(arg0 + 80)
                    v7 = load32(arg0 + 68)
                    while True:  # $label3
                        if not v2:
                            if (v4 <= 0):
                                break
                            if (v4 != 1):
                                v3 = (v4 & -2)
                                v2 = 0
                                while True:  # $label4
                                    v5 = i32(((((load32(arg0 + 16) * load32((v6 + (v1 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))
                                    store8((v1 + v7), (-1 if (v5 > 255) else i32(((((load32(arg0 + 16) * load32((v6 + (v1 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))))
                                    v5 = (v1 | 1)
                                    v5 = i32(((((load32(arg0 + 16) * load32((v6 + (v5 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))
                                    store8((v7 + (v1 | 1)), (-1 if (v5 > 255) else i32(((((load32(arg0 + 16) * load32((v6 + (v5 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))))
                                    v1 = (v1 + 2)
                                    v2 = (v2 + 2)
                                    if ((v2 + 2) != v3):
                                        continue
                                    break
                            if not (v4 & 1):
                                break
                            arg0 = i32(((((load32(arg0 + 16) * load32((v6 + (v1 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))
                            store8((v1 + v7), (-1 if (arg0 > 255) else i32(((((load32(arg0 + 16) * load32((v6 + (v1 << 2)))) + 2147483648) & 0xFFFFFFFF) >> 32))))
                            return
                        # TODO: i64.div_u
                        v8 = i32(v3)
                        if (v4 <= 0):
                            break
                        v2 = load32(arg0 + 76)
                        v9 = (v8 & 4294967295)
                        v8 = ((0 - v8) & 4294967295)
                        while True:  # $label5
                            v3 = (v1 << 2)
                            v3 = i32(((((load32(arg0 + 16) * (((((v8 * load32((v6 + (v1 << 2)))) + (v9 * load32((v2 + v3)))) + 2147483648) & 0xFFFFFFFF) >> 32)) + 2147483648) & 0xFFFFFFFF) >> 32))
                            store8((v1 + v7), (-1 if (v3 > 255) else i32(((((load32(arg0 + 16) * (((((v8 * load32((v6 + (v1 << 2)))) + (v9 * load32((v2 + v3)))) + 2147483648) & 0xFFFFFFFF) >> 32)) + 2147483648) & 0xFFFFFFFF) >> 32))))
                            v1 = (v1 + 1)
                            if ((v1 + 1) != v4):
                                continue
                            break
                        break
                    return
                a_c()
                raise Unreachable()
                break
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func974
# ----------------------------------------------------------
def func974(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if (arg2 <= 0):
            break
        if not arg3:
            while True:  # $label2
                while True:  # $label1
                    arg3 = load8u((arg1 + v4))
                    if (load8u((arg1 + v4)) == 255):
                        break
                    if not arg3:
                        store8((arg0 + v4), 0)
                        break
                    v5 = (arg0 + v4)
                    store8((arg0 + v4), (((((arg3 * load8u(v5)) * 65793) + 8388608) & 0xFFFFFFFF) >> 24))
                    break
                v4 = (v4 + 1)
                if ((v4 + 1) != arg2):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label4
            while True:  # $label3
                arg3 = load8u((arg1 + v4))
                if (load8u((arg1 + v4)) == 255):
                    break
                if not arg3:
                    store8((arg0 + v4), 0)
                    break
                v5 = (arg0 + v4)
                # TODO: i32.div_u
                store8(load8u(v5), ((((-16777216 * arg3) + 8388608) & 0xFFFFFFFF) >> 24))
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != arg2):
                continue
            break
        break

# ----------------------------------------------------------
# $func975
# ----------------------------------------------------------
def func975(arg0, arg1, arg2):
    while True:  # $label0
        if (arg1 <= 0):
            break
        if not arg2:
            while True:  # $label1
                v5 = (arg0 + (v4 << 2))
                arg2 = load32((arg0 + (v4 << 2)))
                if (u32(load32((arg0 + (v4 << 2)))) <= u32(-16777217)):
                    v3 = 0
                    if (u32(arg2) >= u32(16777216)):
                        v3 = (((arg2 & 0xFFFFFFFF) >> 24) * 65793)
                    else:
                    store32(((((arg2 & -16777216) | (((((((arg2 & 0xFFFFFFFF) >> 24) * 65793) * (arg2 & 255)) + 8388608) & 0xFFFFFFFF) >> 24)) | (((((v3 * (((arg2 & 0xFFFFFFFF) >> 8) & 255)) + 8388608) & 0xFFFFFFFF) >> 16) & 65280)) | (((((v3 * (((arg2 & 0xFFFFFFFF) >> 16) & 255)) + 8388608) & 0xFFFFFFFF) >> 8) & 16711680)), 0)
                v4 = (v4 + 1)
                if ((v4 + 1) != arg1):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label2
            v5 = (arg0 + (v4 << 2))
            arg2 = load32((arg0 + (v4 << 2)))
            if (u32(load32((arg0 + (v4 << 2)))) <= u32(-16777217)):
                v3 = 0
                if (u32(arg2) >= u32(16777216)):
                    # TODO: i32.div_u
                    v3 = ((arg2 & 0xFFFFFFFF) >> 24)
                else:
                store32((((-16777216 | ((((((arg2 & 0xFFFFFFFF) >> 24) * (arg2 & 255)) + 8388608) & 0xFFFFFFFF) >> 24)) | (((((v3 * (((arg2 & 0xFFFFFFFF) >> 8) & 255)) + 8388608) & 0xFFFFFFFF) >> 16) & 65280)) | (((((v3 * (((arg2 & 0xFFFFFFFF) >> 16) & 255)) + 8388608) & 0xFFFFFFFF) >> 8) & 16711680)), 0)
            v4 = (v4 + 1)
            if ((v4 + 1) != arg1):
                continue
            break
        break
    return (arg2 & -16777216)

# ----------------------------------------------------------
# $func976
# ----------------------------------------------------------
def func976(arg0, arg1, arg2, arg3):
    if (arg3 > 0):
        while True:  # $label0
            v5 = load16u(arg0 + 2)
            v6 = load16u(arg0)
            v7 = load16u(arg0 + 4)
            v8 = (((load16u(arg0 + 2) * -19081) + (load16u(arg0) * -9719)) + (load16u(arg0 + 4) * 28800))
            v9 = ((((load16u(arg0 + 2) * -19081) + (load16u(arg0) * -9719)) + (load16u(arg0 + 4) * 28800)) + 33685504)
            store8((arg1 + v4), (((((((load16u(arg0 + 2) * -19081) + (load16u(arg0) * -9719)) + (load16u(arg0 + 4) * 28800)) + 33685504) & 0xFFFFFFFF) >> 18) if (u32(v9) < u32(67108864)) else (-33685504 if (v8 < -33685504) else 255)))
            v5 = (((v5 * -24116) + (v6 * 28800)) + (v7 * -4684))
            v6 = ((((v5 * -24116) + (v6 * 28800)) + (v7 * -4684)) + 33685504)
            store8((arg2 + v4), (((((((v5 * -24116) + (v6 * 28800)) + (v7 * -4684)) + 33685504) & 0xFFFFFFFF) >> 18) if (u32(v6) < u32(67108864)) else (-33685504 if (v5 < -33685504) else 255)))
            arg0 = (arg0 + 8)
            v4 = (v4 + 1)
            if ((v4 + 1) != arg3):
                continue
            break

# ----------------------------------------------------------
# $func977
# ----------------------------------------------------------
def func977(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label0
        if (arg3 < 2):
            break
        v5 = (arg3 >> 1)
        v8 = (1 if (v5 <= 1) else (arg3 >> 1))
        v5 = 0
        if not arg4:
            while True:  # $label1
                v6 = (arg1 + v5)
                v7 = (arg0 + (v5 << 3))
                v6 = load32((arg0 + (v5 << 3)) + 4)
                v7 = load32(v7)
                v9 = ((((load32((arg0 + (v5 << 3)) + 4) & 0xFFFFFFFF) >> 15) & 510) + (((load32(v7) & 0xFFFFFFFF) >> 15) & 510))
                v10 = ((((v6 & 0xFFFFFFFF) >> 7) & 510) + (((v7 & 0xFFFFFFFF) >> 7) & 510))
                v6 = (((v6 << 1) & 510) + ((v7 << 1) & 510))
                store8((arg1 + v5), ((((load8u(v6) + ((((((((((load32((arg0 + (v5 << 3)) + 4) & 0xFFFFFFFF) >> 15) & 510) + (((load32(v7) & 0xFFFFFFFF) >> 15) & 510)) * -9719) + (((((v6 & 0xFFFFFFFF) >> 7) & 510) + (((v7 & 0xFFFFFFFF) >> 7) & 510)) * -19081)) + ((((v6 << 1) & 510) + ((v7 << 1) & 510)) * 28800)) + 33685504) & 0xFFFFFFFF) >> 18)) + 1) & 0xFFFFFFFF) >> 1))
                v7 = (arg2 + v5)
                store8((arg2 + v5), ((((load8u(v7) + ((((((v9 * 28800) + (v10 * -24116)) + (v6 * -4684)) + 33685504) & 0xFFFFFFFF) >> 18)) + 1) & 0xFFFFFFFF) >> 1))
                v5 = (v5 + 1)
                if ((v5 + 1) != v8):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label2
            v7 = (arg0 + (v5 << 3))
            v6 = load32((arg0 + (v5 << 3)) + 4)
            v7 = load32(v7)
            v9 = ((((load32((arg0 + (v5 << 3)) + 4) & 0xFFFFFFFF) >> 15) & 510) + (((load32(v7) & 0xFFFFFFFF) >> 15) & 510))
            v10 = ((((v6 & 0xFFFFFFFF) >> 7) & 510) + (((v7 & 0xFFFFFFFF) >> 7) & 510))
            v6 = (((v6 << 1) & 510) + ((v7 << 1) & 510))
            store8((arg1 + v5), ((((((((((load32((arg0 + (v5 << 3)) + 4) & 0xFFFFFFFF) >> 15) & 510) + (((load32(v7) & 0xFFFFFFFF) >> 15) & 510)) * 67099145) + (((((v6 & 0xFFFFFFFF) >> 7) & 510) + (((v7 & 0xFFFFFFFF) >> 7) & 510)) * 67089783)) + ((((v6 << 1) & 510) + ((v7 << 1) & 510)) * 28800)) + 33685504) & 0xFFFFFFFF) >> 18))
            store8((arg2 + v5), ((((((v9 * 28800) + (v10 * 67084748)) + (v6 * 67104180)) + 33685504) & 0xFFFFFFFF) >> 18))
            v5 = (v5 + 1)
            if ((v5 + 1) != v8):
                continue
            break
        break
    if (arg3 & 1):
        arg0 = load32((arg0 + (v8 << 3)))
        arg3 = (((load32((arg0 + (v8 << 3))) & 0xFFFFFFFF) >> 14) & 1020)
        v5 = (((arg0 & 0xFFFFFFFF) >> 6) & 1020)
        v6 = ((arg0 << 2) & 1020)
        arg0 = (((((((((load32((arg0 + (v8 << 3))) & 0xFFFFFFFF) >> 14) & 1020) * 28800) + ((((arg0 & 0xFFFFFFFF) >> 6) & 1020) * -24116)) + (((arg0 << 2) & 1020) * -4684)) + 33685504) & 0xFFFFFFFF) >> 18)
        arg3 = ((((((arg3 * -9719) + (v5 * -19081)) + (v6 * 28800)) + 33685504) & 0xFFFFFFFF) >> 18)
        if arg4:
            store8((arg1 + v8), arg3)
            store8((arg2 + v8), arg0)
            return
        arg1 = (arg1 + v8)
        store8((arg1 + v8), ((((arg3 + load8u(arg1)) + 1) & 0xFFFFFFFF) >> 1))
        arg1 = (arg2 + v8)
        store8((arg2 + v8), ((((arg0 + load8u(arg1)) + 1) & 0xFFFFFFFF) >> 1))

# ----------------------------------------------------------
# $func978
# ----------------------------------------------------------
def func978(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if arg0:
            if (arg3 <= 0):
                break
            v7 = (arg3 & 1)
            if (arg3 != 1):
                v8 = (arg3 & -2)
                arg3 = 0
                while True:  # $label1
                    store8((arg2 + v4), (load8u((arg1 + v4)) + load8u((arg0 + v4))))
                    v5 = (v4 | 1)
                    store8((arg2 + (v4 | 1)), (load8u((arg1 + v5)) + load8u((arg0 + v5))))
                    v4 = (v4 + 2)
                    arg3 = (arg3 + 2)
                    if ((arg3 + 2) != v8):
                        continue
                    break
            if not v7:
                break
            store8((arg2 + v4), (load8u((arg1 + v4)) + load8u((arg0 + v4))))
            return
        if (arg3 <= 0):
            break
        v7 = (arg3 & 3)
        arg0 = 0
        if (u32(arg3) >= u32(4)):
            v8 = (arg3 & -4)
            arg3 = 0
            while True:  # $label2
                v5 = (load8u((arg1 + v4)) + v5)
                store8((arg2 + v4), (load8u((arg1 + v4)) + v5))
                v6 = (v4 | 1)
                v5 = (load8u((arg1 + v6)) + v5)
                store8((arg2 + (v4 | 1)), (load8u((arg1 + v6)) + v5))
                v6 = (v4 | 2)
                v5 = (load8u((arg1 + v6)) + v5)
                store8((arg2 + (v4 | 2)), (load8u((arg1 + v6)) + v5))
                v6 = (v4 | 3)
                v5 = (load8u((arg1 + v6)) + v5)
                store8((arg2 + (v4 | 3)), (load8u((arg1 + v6)) + v5))
                v4 = (v4 + 4)
                arg3 = (arg3 + 4)
                if ((arg3 + 4) != v8):
                    continue
                break
        if not v7:
            break
        while True:  # $label3
            v5 = (load8u((arg1 + v4)) + v5)
            store8((arg2 + v4), (load8u((arg1 + v4)) + v5))
            v4 = (v4 + 1)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != v7):
                continue
            break
        break

# ----------------------------------------------------------
# $func979
# ----------------------------------------------------------
def func979(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label4
        while True:  # $label3
            while True:  # $label2
                while True:  # $label1
                    while True:  # $label0
                        if arg0:
                            if not arg4:
                                break
                            if (arg0 == arg4):
                                break
                            if (arg1 <= 0):
                                break
                            if (arg2 <= 0):
                                break
                            if (arg1 > arg3):
                                break
                            store8(arg4, load8u(arg0))
                            while True:  # $label5
                                v10 = (arg1 - 1)
                                if not (arg1 - 1):
                                    break
                                v6 = (arg4 + 1)
                                v7 = (arg0 + 1)
                                if (arg1 != 2):
                                    v11 = (v10 & -2)
                                    while True:  # $label6
                                        store8((v5 + v6), (load8u((v5 + v7)) - load8u((arg0 + v5))))
                                        v9 = (v5 | 1)
                                        store8((v6 + (v5 | 1)), (load8u((v7 + v9)) - load8u((arg0 + v9))))
                                        v5 = (v5 + 2)
                                        v8 = (v8 + 2)
                                        if ((v8 + 2) != v11):
                                            continue
                                        break
                                if not (v10 & 1):
                                    break
                                store8((v5 + v6), (load8u((v5 + v7)) - load8u((arg0 + v5))))
                                break
                            if (arg2 >= 2):
                                v9 = (arg1 & -2)
                                v11 = (arg1 & 1)
                                v6 = 1
                                while True:  # $label8
                                    arg1 = (arg0 + arg3)
                                    arg4 = (arg3 + arg4)
                                    v5 = 0
                                    v7 = 0
                                    if v10:
                                        while True:  # $label7
                                            store8((arg4 + v5), (load8u((arg1 + v5)) - load8u((arg0 + v5))))
                                            v8 = (v5 | 1)
                                            store8((arg4 + (v5 | 1)), (load8u((arg1 + v8)) - load8u((arg0 + v8))))
                                            v5 = (v5 + 2)
                                            v7 = (v7 + 2)
                                            if ((v7 + 2) != v9):
                                                continue
                                            break
                                    if v11:
                                        store8((arg4 + v5), (load8u((arg1 + v5)) - load8u((arg0 + v5))))
                                    arg0 = arg1
                                    v6 = (v6 + 1)
                                    if ((v6 + 1) != arg2):
                                        continue
                                    break
                            return
                        a_c()
                        raise Unreachable()
                        break
                    a_c()
                    raise Unreachable()
                    break
                a_c()
                raise Unreachable()
                break
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func980
# ----------------------------------------------------------
def func980(arg0):
    v2 = load8u((arg0 - 32))
    v3 = (load8u((arg0 - 32)) + 1)
    v1 = load8u((arg0 - 33))
    v4 = ((((load8u((arg0 - 32)) + 1) + load8u((arg0 - 33))) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 65, ((((load8u((arg0 - 32)) + 1) + load8u((arg0 - 33))) & 0xFFFFFFFF) >> 1))
    v5 = load8u((arg0 - 31))
    v6 = (((v3 + load8u((arg0 - 31))) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 66, (((v3 + load8u((arg0 - 31))) & 0xFFFFFFFF) >> 1))
    store8(arg0, v4)
    v3 = load8u((arg0 - 30))
    v4 = ((((v5 + load8u((arg0 - 30))) + 1) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 67, ((((v5 + load8u((arg0 - 30))) + 1) & 0xFFFFFFFF) >> 1))
    store8(arg0 + 1, v6)
    v6 = load8u((arg0 - 29))
    store8(arg0 + 3, ((((v3 + load8u((arg0 - 29))) + 1) & 0xFFFFFFFF) >> 1))
    store8(arg0 + 2, v4)
    v4 = load8u((arg0 - 1))
    v7 = (load8u((arg0 - 1)) + 2)
    v8 = load8u(arg0 + 31)
    store8(arg0 + 96, (((((load8u((arg0 - 1)) + 2) + load8u(arg0 + 63)) + (load8u(arg0 + 31) << 1)) & 0xFFFFFFFF) >> 2))
    v7 = (((v2 + (v7 + (v1 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 97, (((v2 + (v7 + (v1 << 1))) & 0xFFFFFFFF) >> 2))
    v1 = (v1 + 2)
    store8(arg0 + 64, ((((v8 + (v1 + 2)) + (v4 << 1)) & 0xFFFFFFFF) >> 2))
    v1 = (((v5 + (v1 + (v2 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 98, (((v5 + (v1 + (v2 << 1))) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 32, v7)
    v2 = ((((v3 + (v2 + (v5 << 1))) + 2) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 99, ((((v3 + (v2 + (v5 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 33, v1)
    store8(arg0 + 35, ((((v6 + (v5 + (v3 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 34, v2)

# ----------------------------------------------------------
# $func981
# ----------------------------------------------------------
def func981(arg0, arg1, arg2, arg3):
    if (arg2 > 0):
        v5 = load8s(arg0 + 2)
        v6 = load8s(arg0 + 1)
        v7 = load8s(arg0)
        arg0 = 0
        while True:  # $label0
            v4 = (arg0 << 2)
            v4 = load32((arg1 + v4))
            v8 = ((load32((arg1 + v4)) << 16) >> 24)
            v9 = (((((load32((arg1 + v4)) << 16) >> 24) * v7) >> 5) + ((v4 & 0xFFFFFFFF) >> 16))
            store32((arg3 + (arg0 << 2)), (((((((((load32((arg1 + v4)) << 16) >> 24) * v7) >> 5) + ((v4 & 0xFFFFFFFF) >> 16)) << 16) & 16711680) | (v4 & -16711936)) | ((((((v6 * v8) & 0xFFFFFFFF) >> 5) + v4) + (((i32(v9) * v5) & 0xFFFFFFFF) >> 5)) & 255)))
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break

# ----------------------------------------------------------
# $func986
# ----------------------------------------------------------
def func986(arg0, arg1):
    v2 = load32(arg1 + 4)
    arg0 = load32(arg0)
    arg0 = (((((load32(arg1 + 4) ^ load32(arg0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & v2))
    arg1 = load32(arg1)
    return ((((((((((load32(arg1 + 4) ^ load32(arg0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & v2)) ^ load32(arg1)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & arg1))

# ----------------------------------------------------------
# $func991
# ----------------------------------------------------------
def func991(arg0, arg1):
    v2 = load32(arg1)
    arg0 = load32(arg0)
    arg0 = (((((load32(arg1) ^ load32(arg0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & v2))
    v2 = (((((((load32(arg1) ^ load32(arg0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & v2)) & 0xFFFFFFFF) >> 24)
    arg1 = load32((arg1 - 4))
    v2 = ((((((((load32(arg1) ^ load32(arg0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & v2)) & 0xFFFFFFFF) >> 24) + i32(((v2 - ((load32((arg1 - 4)) & 0xFFFFFFFF) >> 24)) // 2)))
    v2 = (arg0 & 255)
    v2 = ((arg0 & 255) + i32(((v2 - (arg1 & 255)) // 2)))
    v2 = (((arg0 & 0xFFFFFFFF) >> 16) & 255)
    v2 = ((((arg0 & 0xFFFFFFFF) >> 16) & 255) + i32(((v2 - (((arg1 & 0xFFFFFFFF) >> 16) & 255)) // 2)))
    arg0 = (((arg0 & 0xFFFFFFFF) >> 8) & 255)
    arg0 = ((((arg0 & 0xFFFFFFFF) >> 8) & 255) + i32(((arg0 - (((arg1 & 0xFFFFFFFF) >> 8) & 255)) // 2)))
    return (((((((((((((load32(arg1) ^ load32(arg0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & v2)) & 0xFFFFFFFF) >> 24) + i32(((v2 - ((load32((arg1 - 4)) & 0xFFFFFFFF) >> 24)) // 2))) if (u32(v2) < u32(256)) else (((v2 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | (((arg0 & 255) + i32(((v2 - (arg1 & 255)) // 2))) if (u32(v2) < u32(256)) else (((v2 ^ -1) & 0xFFFFFFFF) >> 24))) | ((((((arg0 & 0xFFFFFFFF) >> 16) & 255) + i32(((v2 - (((arg1 & 0xFFFFFFFF) >> 16) & 255)) // 2))) if (u32(v2) < u32(256)) else (((v2 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | ((((((arg0 & 0xFFFFFFFF) >> 8) & 255) + i32(((arg0 - (((arg1 & 0xFFFFFFFF) >> 8) & 255)) // 2))) if (u32(arg0) < u32(256)) else (((arg0 ^ -1) & 0xFFFFFFFF) >> 24)) << 8))

# ----------------------------------------------------------
# $func992
# ----------------------------------------------------------
def func992(arg0, arg1):
    v3 = load32(arg1)
    arg0 = load32(arg0)
    arg1 = load32((arg1 - 4))
    v2 = ((((load32(arg1) & 0xFFFFFFFF) >> 24) + ((load32(arg0) & 0xFFFFFFFF) >> 24)) - ((load32((arg1 - 4)) & 0xFFFFFFFF) >> 24))
    v2 = (((v3 & 255) + (arg0 & 255)) - (arg1 & 255))
    v2 = (((((v3 & 0xFFFFFFFF) >> 16) & 255) + (((arg0 & 0xFFFFFFFF) >> 16) & 255)) - (((arg1 & 0xFFFFFFFF) >> 16) & 255))
    arg0 = (((((v3 & 0xFFFFFFFF) >> 8) & 255) + (((arg0 & 0xFFFFFFFF) >> 8) & 255)) - (((arg1 & 0xFFFFFFFF) >> 8) & 255))
    return (((((((((load32(arg1) & 0xFFFFFFFF) >> 24) + ((load32(arg0) & 0xFFFFFFFF) >> 24)) - ((load32((arg1 - 4)) & 0xFFFFFFFF) >> 24)) if (u32(v2) < u32(256)) else (((v2 ^ -1) & 0xFFFFFFFF) >> 24)) << 24) | ((((v3 & 255) + (arg0 & 255)) - (arg1 & 255)) if (u32(v2) < u32(256)) else (((v2 ^ -1) & 0xFFFFFFFF) >> 24))) | (((((((v3 & 0xFFFFFFFF) >> 16) & 255) + (((arg0 & 0xFFFFFFFF) >> 16) & 255)) - (((arg1 & 0xFFFFFFFF) >> 16) & 255)) if (u32(v2) < u32(256)) else (((v2 ^ -1) & 0xFFFFFFFF) >> 24)) << 16)) | (((((((v3 & 0xFFFFFFFF) >> 8) & 255) + (((arg0 & 0xFFFFFFFF) >> 8) & 255)) - (((arg1 & 0xFFFFFFFF) >> 8) & 255)) if (u32(arg0) < u32(256)) else (((arg0 ^ -1) & 0xFFFFFFFF) >> 24)) << 8))

# ----------------------------------------------------------
# $func993
# ----------------------------------------------------------
def func993(arg0, arg1):
    v4 = load32(arg1)
    arg0 = load32(arg0)
    arg1 = load32((arg1 - 4))
    v2 = (load32((arg1 - 4)) & 255)
    v3 = ((arg0 & 255) - (load32((arg1 - 4)) & 255))
    v3 = (v3 >> 31)
    v3 = ((arg1 & 0xFFFFFFFF) >> 24)
    v5 = (((arg0 & 0xFFFFFFFF) >> 24) - ((arg1 & 0xFFFFFFFF) >> 24))
    v5 = (v5 >> 31)
    v5 = (((arg1 & 0xFFFFFFFF) >> 8) & 255)
    v6 = ((((arg0 & 0xFFFFFFFF) >> 8) & 255) - (((arg1 & 0xFFFFFFFF) >> 8) & 255))
    v6 = (v6 >> 31)
    v3 = (((v4 & 0xFFFFFFFF) >> 24) - v3)
    v3 = (v3 >> 31)
    v2 = ((v4 & 255) - v2)
    v2 = (v2 >> 31)
    v2 = ((((v4 & 0xFFFFFFFF) >> 8) & 255) - v5)
    v2 = (v2 >> 31)
    arg1 = (((arg1 & 0xFFFFFFFF) >> 16) & 255)
    v4 = ((((v4 & 0xFFFFFFFF) >> 16) & 255) - (((arg1 & 0xFFFFFFFF) >> 16) & 255))
    v4 = (v4 >> 31)
    arg0 = ((((arg0 & 0xFFFFFFFF) >> 16) & 255) - arg1)
    arg0 = (arg0 >> 31)
    return (load32(arg1) if (((((((((arg0 & 255) - (load32((arg1 - 4)) & 255)) ^ (v3 >> 31)) - v3) + (((((arg0 & 0xFFFFFFFF) >> 24) - ((arg1 & 0xFFFFFFFF) >> 24)) ^ (v5 >> 31)) - v5)) + ((((((arg0 & 0xFFFFFFFF) >> 8) & 255) - (((arg1 & 0xFFFFFFFF) >> 8) & 255)) ^ (v6 >> 31)) - v6)) - ((((((((v4 & 0xFFFFFFFF) >> 24) - v3) ^ (v3 >> 31)) - v3) + ((((v4 & 255) - v2) ^ (v2 >> 31)) - v2)) + ((((((v4 & 0xFFFFFFFF) >> 8) & 255) - v5) ^ (v2 >> 31)) - v2)) + ((((((v4 & 0xFFFFFFFF) >> 16) & 255) - (((arg1 & 0xFFFFFFFF) >> 16) & 255)) ^ (v4 >> 31)) - v4))) + ((((((arg0 & 0xFFFFFFFF) >> 16) & 255) - arg1) ^ (arg0 >> 31)) - arg0)) <= 0) else load32(arg0))

# ----------------------------------------------------------
# $func994
# ----------------------------------------------------------
def func994(arg0, arg1):
    v2 = load32(arg1 + 4)
    v3 = load32(arg1)
    v2 = (((((load32(arg1 + 4) ^ load32(arg1)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v2 & v3))
    arg1 = load32((arg1 - 4))
    arg0 = load32(arg0)
    arg0 = (((((load32((arg1 - 4)) ^ load32(arg0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & arg1))
    return ((((((((((load32(arg1 + 4) ^ load32(arg1)) & 0xFFFFFFFF) >> 1) & 2139062143) + (v2 & v3)) ^ (((((load32((arg1 - 4)) ^ load32(arg0)) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & arg1))) & 0xFFFFFFFF) >> 1) & 2139062143) + (arg0 & v2))

# ----------------------------------------------------------
# $func996
# ----------------------------------------------------------
def func996(arg0, arg1, arg2):
    if (arg1 > 0):
        v3 = (arg0 + (arg1 << 2))
        while True:  # $label0
            arg1 = load32(arg0)
            store8(arg2 + 2, load32(arg0))
            store8(arg2 + 1, ((arg1 & 0xFFFFFFFF) >> 8))
            store8(arg2, ((arg1 & 0xFFFFFFFF) >> 16))
            arg2 = (arg2 + 3)
            arg0 = (arg0 + 4)
            if (u32((arg0 + 4)) < u32(v3)):
                continue
            break

# ----------------------------------------------------------
# $func997
# ----------------------------------------------------------
def func997(arg0, arg1, arg2):
    if (arg1 > 0):
        v3 = (arg0 + (arg1 << 2))
        while True:  # $label0
            arg1 = load32(arg0)
            store8(arg2 + 2, load32(arg0))
            store8(arg2 + 3, ((arg1 & 0xFFFFFFFF) >> 24))
            store8(arg2 + 1, ((arg1 & 0xFFFFFFFF) >> 8))
            store8(arg2, ((arg1 & 0xFFFFFFFF) >> 16))
            arg2 = (arg2 + 4)
            arg0 = (arg0 + 4)
            if (u32((arg0 + 4)) < u32(v3)):
                continue
            break

# ----------------------------------------------------------
# $func998
# ----------------------------------------------------------
def func998(arg0, arg1, arg2):
    if (arg1 > 0):
        v3 = (arg0 + (arg1 << 2))
        while True:  # $label0
            arg1 = load32(arg0)
            store8(arg2 + 1, ((load32(arg0) & 240) | ((arg1 & 0xFFFFFFFF) >> 28)))
            store8(arg2, ((((arg1 & 0xFFFFFFFF) >> 16) & 240) | (((arg1 & 0xFFFFFFFF) >> 12) & 15)))
            arg2 = (arg2 + 2)
            arg0 = (arg0 + 4)
            if (u32((arg0 + 4)) < u32(v3)):
                continue
            break

# ----------------------------------------------------------
# $func999
# ----------------------------------------------------------
def func999(arg0, arg1, arg2):
    if (arg1 > 0):
        v3 = (arg0 + (arg1 << 2))
        while True:  # $label0
            arg1 = load32(arg0)
            store8(arg2 + 1, ((((load32(arg0) & 0xFFFFFFFF) >> 5) & 224) | (((arg1 & 0xFFFFFFFF) >> 3) & 31)))
            store8(arg2, ((((arg1 & 0xFFFFFFFF) >> 16) & 248) | (((arg1 & 0xFFFFFFFF) >> 13) & 7)))
            arg2 = (arg2 + 2)
            arg0 = (arg0 + 4)
            if (u32((arg0 + 4)) < u32(v3)):
                continue
            break

# ----------------------------------------------------------
# $func1000
# ----------------------------------------------------------
def func1000(arg0, arg1, arg2):
    if (arg1 > 0):
        v3 = (arg0 + (arg1 << 2))
        while True:  # $label0
            arg1 = load32(arg0)
            store8(arg2, load32(arg0))
            store8(arg2 + 2, ((arg1 & 0xFFFFFFFF) >> 16))
            store8(arg2 + 1, ((arg1 & 0xFFFFFFFF) >> 8))
            arg2 = (arg2 + 3)
            arg0 = (arg0 + 4)
            if (u32((arg0 + 4)) < u32(v3)):
                continue
            break

# ----------------------------------------------------------
# $func1001
# ----------------------------------------------------------
def func1001(arg0, arg1, arg2):
    while True:  # $label0
        if (arg1 <= 0):
            break
        if (arg1 != 1):
            v7 = (arg1 & -2)
            while True:  # $label1
                v3 = (v4 << 2)
                v5 = load32((arg0 + v3))
                v8 = ((load32((arg0 + v3)) & 0xFFFFFFFF) >> 8)
                store32((arg2 + (v4 << 2)), (((((((load32((arg0 + v3)) & 0xFFFFFFFF) >> 8) & 255) + (v5 & 16711935)) + (v8 << 16)) & 16711935) | (v5 & -16711936)))
                v3 = (v3 | 4)
                v3 = load32((arg0 + v3))
                v5 = ((load32((arg0 + v3)) & 0xFFFFFFFF) >> 8)
                store32((arg2 + (v3 | 4)), (((((((load32((arg0 + v3)) & 0xFFFFFFFF) >> 8) & 255) + (v3 & 16711935)) + (v5 << 16)) & 16711935) | (v3 & -16711936)))
                v4 = (v4 + 2)
                v6 = (v6 + 2)
                if ((v6 + 2) != v7):
                    continue
                break
        if not (arg1 & 1):
            break
        arg1 = (v4 << 2)
        arg0 = load32((arg0 + arg1))
        arg1 = ((load32((arg0 + arg1)) & 0xFFFFFFFF) >> 8)
        store32((arg2 + (v4 << 2)), (((((((load32((arg0 + arg1)) & 0xFFFFFFFF) >> 8) & 255) + (arg0 & 16711935)) + (arg1 << 16)) & 16711935) | (arg0 & -16711936)))
        break

# ----------------------------------------------------------
# $func1002
# ----------------------------------------------------------
def func1002(arg0):
    v5 = load8u((arg0 - 31))
    v1 = (load8u((arg0 - 31)) + 1)
    v2 = load8u((arg0 - 30))
    v3 = ((((load8u((arg0 - 31)) + 1) + load8u((arg0 - 30))) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 64, ((((load8u((arg0 - 31)) + 1) + load8u((arg0 - 30))) & 0xFFFFFFFF) >> 1))
    v6 = load8u((arg0 - 32))
    store8(arg0, (((v1 + load8u((arg0 - 32))) & 0xFFFFFFFF) >> 1))
    v1 = load8u((arg0 - 29))
    v4 = ((((v2 + load8u((arg0 - 29))) + 1) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 65, ((((v2 + load8u((arg0 - 29))) + 1) & 0xFFFFFFFF) >> 1))
    store8(arg0 + 1, v3)
    v3 = load8u((arg0 - 28))
    v7 = ((((v1 + load8u((arg0 - 28))) + 1) & 0xFFFFFFFF) >> 1)
    store8(arg0 + 66, ((((v1 + load8u((arg0 - 28))) + 1) & 0xFFFFFFFF) >> 1))
    store8(arg0 + 2, v4)
    store8(arg0 + 3, v7)
    v4 = (v1 + 2)
    v7 = ((((v5 + (v1 + 2)) + (v2 << 1)) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 96, ((((v5 + (v1 + 2)) + (v2 << 1)) & 0xFFFFFFFF) >> 2))
    v2 = (v2 + 2)
    store8(arg0 + 32, ((((v6 + (v2 + 2)) + (v5 << 1)) & 0xFFFFFFFF) >> 2))
    v5 = (((v3 + (v2 + (v1 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 97, (((v3 + (v2 + (v1 << 1))) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 33, v7)
    v6 = load8u((arg0 - 25))
    v2 = load8u((arg0 - 26))
    v1 = load8u((arg0 - 27))
    v4 = (((load8u((arg0 - 27)) + (v4 + (v3 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 98, (((load8u((arg0 - 27)) + (v4 + (v3 << 1))) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 34, v5)
    store8(arg0 + 99, ((((v6 + (v1 + (v2 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 67, ((((v2 + (v3 + (v1 << 1))) + 2) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 35, v4)

# ----------------------------------------------------------
# $func1003
# ----------------------------------------------------------
def func1003(arg0, arg1, arg2, arg3, arg4, arg5):
    v6 = (arg2 << 2)

# ----------------------------------------------------------
# $func1004
# ----------------------------------------------------------
def func1004(arg0, arg1, arg2, arg3, arg4, arg5):
    func137(arg0, arg2, 1, 8, arg3, arg4, arg5)
    func137(arg1, arg2, 1, 8, arg3, arg4, arg5)

# ----------------------------------------------------------
# $func1005
# ----------------------------------------------------------
def func1005(arg0, arg1, arg2, arg3, arg4):
    v5 = (arg1 << 2)
    arg0 = (arg0 + (arg1 << 2))
    arg0 = (arg0 + v5)

# ----------------------------------------------------------
# $func1006
# ----------------------------------------------------------
def func1006(arg0, arg1, arg2, arg3, arg4):
    func137(arg0, arg1, 1, 16, arg2, arg3, arg4)

# ----------------------------------------------------------
# $func1007
# ----------------------------------------------------------
def func1007(arg0):
    v1 = load64((arg0 - 32))
    store64(arg0 + 224, load64((arg0 - 32)))
    store64(arg0 + 192, v1)
    store64(arg0 + 160, v1)
    store64(arg0 + 128, v1)
    store64(arg0 + 96, v1)
    store64(arg0 + 64, v1)
    store64(arg0 + 32, v1)
    store64(arg0, v1)

# ----------------------------------------------------------
# $func1008
# ----------------------------------------------------------
def func1008(arg0):
    v2 = load8u((arg0 - 30))
    v3 = (load8u((arg0 - 30)) + 2)
    v1 = load8u((arg0 - 29))
    v4 = (((load8u((arg0 - 28)) + ((load8u((arg0 - 30)) + 2) + (load8u((arg0 - 29)) << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 99, (((load8u((arg0 - 28)) + ((load8u((arg0 - 30)) + 2) + (load8u((arg0 - 29)) << 1))) & 0xFFFFFFFF) >> 2))
    v5 = load8u((arg0 - 31))
    v6 = (load8u((arg0 - 31)) + 2)
    v2 = (((v1 + ((load8u((arg0 - 31)) + 2) + (v2 << 1))) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 98, (((v1 + ((load8u((arg0 - 31)) + 2) + (v2 << 1))) & 0xFFFFFFFF) >> 2))
    v1 = load8u((arg0 - 32))
    v3 = ((((v3 + load8u((arg0 - 32))) + (v5 << 1)) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 97, ((((v3 + load8u((arg0 - 32))) + (v5 << 1)) & 0xFFFFFFFF) >> 2))
    v1 = ((((v6 + load8u((arg0 - 33))) + (v1 << 1)) & 0xFFFFFFFF) >> 2)
    store8(arg0 + 96, ((((v6 + load8u((arg0 - 33))) + (v1 << 1)) & 0xFFFFFFFF) >> 2))
    store8(arg0 + 67, v4)
    store8(arg0 + 66, v2)
    store8(arg0 + 65, v3)
    store8(arg0 + 64, v1)
    store8(arg0 + 35, v4)
    store8(arg0 + 34, v2)
    store8(arg0 + 33, v3)
    store8(arg0 + 32, v1)
    store8(arg0 + 3, v4)
    store8(arg0 + 2, v2)
    store8(arg0 + 1, v3)
    store8(arg0, v1)

# ----------------------------------------------------------
# $func1009
# ----------------------------------------------------------
def func1009(arg0):
    v3 = (arg0 - 32)
    v1 = load64((arg0 - 32))
    store64(arg0, load64((arg0 - 32)))
    store64(arg0 + 32, v1)
    store64(arg0 + 64, v1)
    store64(arg0 + 96, v1)
    store64(arg0 + 128, v1)
    store64(arg0 + 160, v1)
    store64(arg0 + 192, v1)
    store64(arg0 + 224, v1)
    v1 = load64(v3 + 8)
    store64(arg0 + 8, load64(v3 + 8))
    store64(arg0 + 40, v1)
    store64(arg0 + 72, v1)
    store64(arg0 + 104, v1)
    store64(arg0 + 136, v1)
    store64(arg0 + 168, v1)
    store64(arg0 + 200, v1)
    store64(arg0 + 232, v1)
    v1 = load64(v3 + 8)
    store64(arg0 + 264, load64(v3 + 8))
    v2 = load64(v3)
    store64(arg0 + 256, load64(v3))
    store64(arg0 + 296, v1)
    store64(arg0 + 288, v2)
    store64(arg0 + 328, v1)
    store64(arg0 + 320, v2)
    store64(arg0 + 360, v1)
    store64(arg0 + 352, v2)
    store64(arg0 + 384, v2)
    store64(arg0 + 392, v1)
    store64(arg0 + 424, v1)
    store64(arg0 + 416, v2)
    store64(arg0 + 448, v2)
    store64(arg0 + 456, v1)
    store64(arg0 + 488, v1)
    store64(arg0 + 480, v2)
