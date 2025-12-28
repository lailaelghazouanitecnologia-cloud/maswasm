"""
Tzar Engine - Core module (part 15).
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
# $td
# Export: td
# ----------------------------------------------------------
def td():
    """Export: td"""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label3
        if not load8u(9147141):
            while True:  # $label0
                v3 = load32(9671120)
                if not load32(9671120):
                    break
                if (u32(v3) >= u32(4)):
                    v7 = (v3 & -4)
                    while True:  # $label1
                        v0 = (v1 << 2)
                        store32(((v1 << 2) + 9684512), load32(load32((v0 + 9263072)) + 12))
                        v5 = (v0 | 4)
                        store32(((v0 | 4) + 9684512), load32(load32((v5 + 9263072)) + 12))
                        v5 = (v0 | 8)
                        store32(((v0 | 8) + 9684512), load32(load32((v5 + 9263072)) + 12))
                        v0 = (v0 | 12)
                        store32(((v0 | 12) + 9684512), load32(load32((v0 + 9263072)) + 12))
                        v1 = (v1 + 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v7):
                            continue
                        break
                v0 = (v3 & 3)
                if not (v3 & 3):
                    break
                while True:  # $label2
                    v4 = (v1 << 2)
                    store32(((v1 << 2) + 9684512), load32(load32((v4 + 9263072)) + 12))
                    v1 = (v1 + 1)
                    v6 = (v6 + 1)
                    if ((v6 + 1) != v0):
                        continue
                    break
                break
            store32(v2 + 4, v3)
            store32(v2, 9684512)
            break
        break
    G.global0 = (v2 + 16)

# ----------------------------------------------------------
# $func563
# ----------------------------------------------------------
def func563(arg0, arg1, arg2):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if arg2:
        v3 = load32(PLAYER_COUNT)
        v6 = load32(PLAYERS)
        while True:  # $label3
            v7 = (v5 << 2)
            arg0 = 0
            while True:  # $label0
                if (u32(v3) < u32(2)):
                    break
                v8 = load32((arg1 + v7))
                arg0 = 1
                while True:  # $label1
                    if (load32((v6 + (arg0 * 286704)) + 284616) == v8):
                        break
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v3):
                        continue
                    break
                arg0 = 0
                break
            while True:  # $label2
                if (u32(arg0) >= u32(v3)):
                    break
                arg0 = (v6 + (arg0 * 286704))
                if not load32((v6 + (arg0 * 286704)) + 283908):
                    break
                store32(arg0 + 284604, load32((arg1 + (v7 | 4))))
                v3 = load32(PLAYER_COUNT)
                break
            v5 = (v5 + 2)
            if (u32((v5 + 2)) < u32(arg2)):
                continue
            break
    while True:  # $label4
        if load8u(9147213):
            if not load32(9687276):
                break
            arg1 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            arg2 = load32(PLAYERS)
            arg0 = 1
            while True:  # $label6
                v3 = (arg2 + (arg0 * 286704))
                if not load8u((arg2 + (arg0 * 286704)) + 286699):
                    arg1 = load32(v3 + 284604)
                    while True:  # $label5
                        if not load8u(9147210):
                            break
                        if (load32(v3 + 284616) != load32(9561844)):
                            if (load32(CURRENT_PLAYER) != arg0):
                                break
                            if not load8u(9142388):
                                break
                        arg1 = 2147483647
                        break
                    store32(v4 + 4, arg1)
                    store32(v4, arg0)
                    a_b()
                    arg2 = load32(PLAYERS)
                    arg1 = load32(PLAYER_COUNT)
                arg0 = (arg0 + 1)
                if (u32((arg0 + 1)) < u32(arg1)):
                    continue
                break
            break
        break
    G.global0 = (v4 + 16)

# ----------------------------------------------------------
# $db
# Export: db
# ----------------------------------------------------------
def db(arg0, arg1, arg2, arg3):
    """Export: db"""
    while True:  # $label0
        if (arg0 == 54):
            break
        if load8u(((arg0 * 404) + ENTITY_TYPES) + 378):
            break
        while True:  # $label1
            if arg1:
                if not (load32(((arg0 * 404) + ENTITY_TYPES) + 264) & -5):
                    break
                break
            if arg2:
                if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) != 1):
                    break
            if not arg3:
                break
            if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) != 2):
                break
            break
        v4 = (load32(((arg0 * 404) + ENTITY_TYPES) + 144) * -48)
        break
    return v4

# ----------------------------------------------------------
# $cb
# Export: cb
# ----------------------------------------------------------
def cb(arg0, arg1, arg2, arg3):
    """Export: cb"""
    while True:  # $label0
        while True:  # $label1
            if arg1:
                arg0 = ((arg0 * 404) + ENTITY_TYPES)
                if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) & -5):
                    arg1 = 0
                    if not arg2:
                        break
                arg1 = -48
                break
            if arg2:
                arg1 = 0
                if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) != 1):
                    break
            if arg3:
                arg1 = 0
                arg2 = ((arg0 * 404) + ENTITY_TYPES)
                if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) != 3):
                    break
                if (load32(arg2 + 368) == 55):
                    break
            arg0 = load32(((arg0 * 404) + ENTITY_TYPES) + 180)
            if not load32(((arg0 * 404) + ENTITY_TYPES) + 180):
                return 0
            arg1 = 48
            break
        arg0 = (arg0 + 8)
        arg1 = (load32(arg0) * arg1)
        break
    return arg1

# ----------------------------------------------------------
# $sa
# Export: sa
# ----------------------------------------------------------
def sa(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    """Export: sa"""
    store8(59184, arg1)
    store32(59168, arg0)
    store8(59185, arg2)
    store32(9561840, arg3)
    store8(9142916, arg4)
    store8(9142917, arg5)
    store8(9142918, arg6)

# ----------------------------------------------------------
# $func573
# ----------------------------------------------------------
def func573(arg0, arg1, arg2):
    while True:  # $label0
        v3 = load32(arg0 + 4)
        v11 = load32(arg0 + 8)
        if (load32(arg0 + 4) == load32(arg0 + 8)):
            break
        v4 = load32(ENTITIES)
        v3 = entities[v3]
        v7 = ((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES)
        v5 = (v4 + (v11 * 132))
        v6 = ((load8u((v4 + (v11 * 132)) + 122) * 404) + ENTITY_TYPES)
        v9 = ((((load32(((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v3 + 112)) - (((load32(((load8u((v4 + (v11 * 132)) + 122) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v5 + 112)))
        v3 = ((load16u(v3 + 114) + ((load32(v7 + 220) & 0xFFFFFFFF) >> 1)) - (load16u(v5 + 114) + ((load32(v6 + 220) & 0xFFFFFFFF) >> 1)))
        if ((((((((load32(((load8u(entities[v3].sub_state) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v3 + 112)) - (((load32(((load8u((v4 + (v11 * 132)) + 122) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v5 + 112))) * v9) + (((load16u(v3 + 114) + ((load32(v7 + 220) & 0xFFFFFFFF) >> 1)) - (load16u(v5 + 114) + ((load32(v6 + 220) & 0xFFFFFFFF) >> 1))) * v3)) - 1) < 82):
            break
        if not arg2:
            break
        v9 = load32(arg0)
        v3 = load32(PLAYERS)
        while True:  # $label11
            while True:  # $label1
                v7 = (v4 + (load32((arg1 + (v12 << 2))) * 132))
                v6 = load32(((load8u((v4 + (load32((arg1 + (v12 << 2))) * 132)) + 122) * 404) + ENTITY_TYPES) + 124)
                if not load32(((load8u((v4 + (load32((arg1 + (v12 << 2))) * 132)) + 122) * 404) + ENTITY_TYPES) + 124):
                    break
                v5 = (v3 + (load16u(v7 + 110) * 286704))
                if not load32((((v3 + (load16u(v7 + 110) * 286704)) + (load32(39104) << 2)) + 281808)):
                    break
                v3 = load32((v5 + 284340))
                v13 = (v9 if (u32(v3) < u32(v9)) else load32((v5 + 284340)))
                v14 = (u32(v6) < u32(v9))
                while True:  # $label4
                    while True:  # $label3
                        while True:  # $label2
                            v4 = load32(v7 + 20)
                            if not load32(v7 + 20):
                                v4 = func26(16)
                                store32(func26(16) + 4, 7)
                                v3 = func26(28)
                                store32(v4 + 12, 16)
                                store32(v4, v3)
                                store32(v7 + 20, v4)
                                store32(v4 + 8, 0)
                                v8 = (v4 + 8)
                                break
                            store32(v4 + 8, 0)
                            v8 = (v4 + 8)
                            if not load32(v4 + 4):
                                break
                            break
                        v5 = load32(v4)
                        v3 = 0
                        break
                        break
                    v3 = load32(v4 + 12)
                    store32(v4 + 4, load32(v4 + 12))
                    v10 = load32(v4)
                    v5 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                    if v10:
                    else:
                    v3 = 0
                    store32(v4, v5)
                    v4 = load32(v7 + 20)
                    break
                v10 = (v6 if v14 else v13)
                store32(v8, (v3 + 1))
                store32((v5 + (v3 << 2)), 0)
                while True:  # $label5
                    v3 = load32(v4 + 8)
                    if (load32(v4 + 8) != load32(v4 + 4)):
                        v5 = load32(v4)
                        break
                    v5 = (load32(v4 + 12) + v3)
                    store32(v4 + 4, (load32(v4 + 12) + v3))
                    v6 = load32(v4)
                    v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy
                    if v6:
                        v3 = load32(v4 + 8)
                    store32(v4, v5)
                    break
                v6 = load32(v7 + 20)
                store32(v4 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v10)
                v8 = load32(arg0 + 4)
                while True:  # $label6
                    v3 = load32(v6 + 8)
                    if (load32(v6 + 8) != load32(v6 + 4)):
                        v5 = load32(v6)
                        break
                    v5 = (load32(v6 + 12) + v3)
                    store32(v6 + 4, (load32(v6 + 12) + v3))
                    v4 = load32(v6)
                    v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy
                    if v4:
                        v3 = load32(v6 + 8)
                    store32(v6, v5)
                    break
                v4 = load32(v7 + 20)
                store32(v6 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v8)
                v8 = load32(arg0 + 8)
                while True:  # $label7
                    v3 = load32(v4 + 8)
                    if (load32(v4 + 8) != load32(v4 + 4)):
                        v5 = load32(v4)
                        break
                    v5 = (load32(v4 + 12) + v3)
                    store32(v4 + 4, (load32(v4 + 12) + v3))
                    v6 = load32(v4)
                    v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy
                    if v6:
                        v3 = load32(v4 + 8)
                    store32(v4, v5)
                    break
                v6 = load32(v7 + 20)
                store32(v4 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v8)
                v8 = load32(arg0 + 12)
                while True:  # $label8
                    v3 = load32(v6 + 8)
                    if (load32(v6 + 8) != load32(v6 + 4)):
                        v5 = load32(v6)
                        break
                    v5 = (load32(v6 + 12) + v3)
                    store32(v6 + 4, (load32(v6 + 12) + v3))
                    v4 = load32(v6)
                    v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy
                    if v4:
                        v3 = load32(v6 + 8)
                    store32(v6, v5)
                    break
                v4 = load32(v7 + 20)
                store32(v6 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v8)
                v8 = load32(arg0 + 16)
                while True:  # $label9
                    v3 = load32(v4 + 8)
                    if (load32(v4 + 8) != load32(v4 + 4)):
                        v5 = load32(v4)
                        break
                    v5 = (load32(v4 + 12) + v3)
                    store32(v4 + 4, (load32(v4 + 12) + v3))
                    v6 = load32(v4)
                    v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy
                    if v6:
                        v3 = load32(v4 + 8)
                    store32(v4, v5)
                    break
                v6 = load32(v7 + 20)
                store32(v4 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v8)
                while True:  # $label10
                    v4 = load32(v6 + 8)
                    if (load32(v6 + 8) != load32(v6 + 4)):
                        v3 = load32(v6)
                        break
                    v3 = (load32(v6 + 12) + v4)
                    store32(v6 + 4, (load32(v6 + 12) + v4))
                    v5 = load32(v6)
                    v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                    if v4:
                        # TODO: memory.copy
                    if v5:
                        v4 = load32(v6 + 8)
                    store32(v6, v3)
                    break
                store32(v6 + 8, (v4 + 1))
                store32((v3 + (v4 << 2)), 1)
                v3 = load32(PLAYERS)
                v4 = load32(ENTITIES)
                break
            v12 = (v12 + 1)
            if ((v12 + 1) != arg2):
                continue
            break
        break
    return (v4 << 2)

# ----------------------------------------------------------
# $wc
# Export: wc
# ----------------------------------------------------------
def wc(arg0, arg1, arg2, arg3, arg4):
    """Export: wc"""
    arg4 = players[arg4]
    store32(players[arg4] + 283848, (load32(arg4 + 283848) + arg0))
    arg0 = (arg4 + 283852)
    store32((arg4 + 283852), (load32(arg0) + arg1))
    arg0 = (arg4 + 283856)
    store32((arg4 + 283856), (load32(arg0) + arg2))
    arg0 = (arg4 + 283860)
    store32((arg4 + 283860), (load32(arg0) + arg3))

# ----------------------------------------------------------
# $func579
# ----------------------------------------------------------
def func579(arg0):
    store32(40604, arg0)

# ----------------------------------------------------------
# $func580
# ----------------------------------------------------------
def func580(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if load8u(9163793):
            store32(v1 + 8, arg0)
            store32(v1 + 12, load8u(9163792))
            arg0 = load32(9213808)
            if load8u(9147210):
                func41(42, 9173808, arg0, (v1 + 8), 2)
                break
            v3 = (arg0 << 2)
            v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg0:
                # TODO: memory.copy
            break
        store32(40604, arg0)
        break
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func581
# ----------------------------------------------------------
def func581(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if (arg0 != 18):
            store32(40604, arg0)
            break
        if not load8u(9163793):
            store32(40604, 18)
            if load32(9216064):
                break
            store32(41088, 10)
            store64(v1, 10)
            break
        store32(v1 + 12, 0)
        arg0 = load32(9213808)
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
# $rd
# Export: rd
# ----------------------------------------------------------
def rd(arg0, arg1, arg2, arg3, arg4):
    """Export: rd"""
    v7 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    store32(9163784, arg1)
    store32(9163788, arg1)
    store8(9142906, arg4)
    store8(59181, (arg2 == 3))
    store8(9568060, (arg3 != 0))
    arg1 = load8u(9142916)
    storef32(9671164, (1.0 if load8u(9142916) else arg0))
    if (u32(arg2) <= u32(2)):
        store32(51788, load32(((arg2 << 2) + 10152)))
    if arg1:
        arg4 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        arg1 = func26(8160)
        while True:  # $label0
            arg2 = (v5 << 2)
            arg3 = ((v6 * 404) + ENTITY_TYPES)
            store32((arg1 + (v5 << 2)), load32(((v6 * 404) + ENTITY_TYPES) + 200))
            store32((arg1 + (arg2 | 4)), load32(arg3 + 216))
            store32((arg1 + (arg2 | 8)), load32(arg3 + 220))
            store32((arg1 + (arg2 | 12)), not (load32(arg3 + 264) & -5))
            store32((arg1 + (arg2 | 16)), load32(arg3 + 384))
            store32((arg1 + (arg2 | 20)), load32(arg3 + 388))
            store32((arg1 + (arg2 | 24)), load32(arg3 + 392))
            store32((arg1 + (arg2 | 28)), load32(arg3 + 396))
            v5 = (v5 + 8)
            v6 = (v6 + 1)
            if ((v6 + 1) != 255):
                continue
            break
        store32(arg4 + 4, 2040)
        store32(arg4, arg1)
        G.global0 = (arg4 + 16)
    func320(0)
    while True:  # $label2
        while True:  # $label3
            if load8u(9147212):
                while True:  # $label1
                    if not load8u(9147152):
                        break
                    arg1 = load32(9561752)
                    if not load32(9561752):
                        break
                    if (arg1 == load32(9561756)):
                        break
                    store32(9147288, 0)
                    store32(PLAYER_COUNT, 0)
                    break
                    break
                func319()
                break
            while True:  # $label4
                arg1 = load32(9671136)
                if (u32(load32(9671136)) < u32(4)):
                    break
                arg4 = load32(ENTITIES)
                arg2 = 3
                while True:  # $label6
                    while True:  # $label5
                        arg3 = (arg4 + (arg2 * 132))
                        if (load8u((arg4 + (arg2 * 132)) + 125) == 3):
                            break
                        if not load32(arg3 + 28):
                            break
                        if not load32(load32(GAME_STATE) + 48):
                            break
                        arg1 = load32(9671136)
                        arg4 = load32(ENTITIES)
                        break
                    arg2 = (arg2 + 1)
                    if (u32((arg2 + 1)) < u32(arg1)):
                        continue
                    break
                arg2 = 3
                if (u32(arg1) <= u32(3)):
                    break
                while True:  # $label14
                    while True:  # $label7
                        arg3 = (arg4 + (arg2 * 132))
                        if (load8u((arg4 + (arg2 * 132)) + 125) == 3):
                            break
                        if not load32(arg3 + 28):
                            break
                        v5 = 0
                        v6 = load8u(arg3 + 122)
                        while True:  # $label9
                            while True:  # $label8
                                arg1 = load32(load32(GAME_STATE) + 48)
                                if not load32(load32(GAME_STATE) + 48):
                                    break
                                arg4 = load32(((v6 * 404) + ENTITY_TYPES) + 216)
                                if not load32(((v6 * 404) + ENTITY_TYPES) + 216):
                                    break
                                if load8u(9147152):
                                    break
                                v9 = load32(9142440)
                                v12 = load32(9147376)
                                v13 = load16u(arg3 + 112)
                                v8 = load16u(arg3 + 114)
                                if (arg1 == 2):
                                    while True:  # $label11
                                        v14 = (v5 + v13)
                                        arg1 = 0
                                        while True:  # $label10
                                            if (u32(load16u((v12 + ((v14 + (v9 * (arg1 + v8))) << 1)))) > u32(1)):
                                                break
                                            arg1 = (arg1 + 1)
                                            if ((arg1 + 1) != arg4):
                                                continue
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != arg4):
                                            continue
                                        break
                                        break
                                    raise Unreachable()
                                while True:  # $label13
                                    v14 = (v5 + v13)
                                    arg1 = 0
                                    while True:  # $label12
                                        if load16u((v12 + ((v14 + (v9 * (arg1 + v8))) << 1))):
                                            break
                                        arg1 = (arg1 + 1)
                                        if ((arg1 + 1) != arg4):
                                            continue
                                        break
                                    v5 = (v5 + 1)
                                    if ((v5 + 1) != arg4):
                                        continue
                                    break
                                break
                                break
                            break
                        arg1 = load32(9671136)
                        arg4 = load32(ENTITIES)
                        break
                    arg2 = (arg2 + 1)
                    if (u32((arg2 + 1)) < u32(arg1)):
                        continue
                    break
                break
            if not load32(PLAYER_COUNT):
                break
            arg3 = load32(GAME_STATE)
            arg4 = load32(PLAYERS)
            arg1 = 0
            while True:  # $label15
                arg2 = (arg4 + (arg1 * 286704))
                store32((arg4 + (arg1 * 286704)) + 283868, load32(9561460))
                # TODO: memory.copy
                store32((arg2 + 284000), load32(arg3 + 40))
                store32((arg2 + 284136), load32(arg3 + 36))
                arg1 = (arg1 + 1)
                if (u32((arg1 + 1)) < u32(load32(PLAYER_COUNT))):
                    continue
                break
            break
        arg4 = 0
        while True:  # $label16
            arg3 = load32(9140328)
            if not load32(9140328):
                break
            arg1 = load32(9142440)
            arg1 = (load32(9142440) * arg1)
            arg2 = 0
            if (u32(arg3) >= u32(4)):
                v6 = (arg3 & -4)
                while True:  # $label17
                    v5 = (arg2 << 2)
                    arg4 = ((((arg1 * load32(load32((((arg2 << 2) | 12) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + ((((((arg1 * load32(load32((v5 + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + arg4) + (((arg1 * load32(load32(((v5 | 4) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)) + (((arg1 * load32(load32(((v5 | 8) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)))
                    arg2 = (arg2 + 4)
                    v10 = (v10 + 4)
                    if ((v10 + 4) != v6):
                        continue
                    break
            arg3 = (arg3 & 3)
            if not (arg3 & 3):
                break
            while True:  # $label18
                arg4 = ((((arg1 * load32(load32(((arg2 << 2) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + arg4)
                arg2 = (arg2 + 1)
                v11 = (v11 + 1)
                if ((v11 + 1) != arg3):
                    continue
                break
            break
        arg1 = load32(9681936)
        if not load32(9681936):
            arg1 = func26(16)
            arg2 = (arg4 << 2)
            store32(func26(16) + 4, (arg4 << 2))
            store32(arg1, func26((-1 if (u32(arg2) > u32(1073741823)) else (arg4 << 4))))
            store64(arg1 + 8, 206158430208)
            store32(9681936, arg1)
        while True:  # $label19
            if not (load8u(9147212) | load8u(9147152)):
                func169()
                break
            if not load32(arg1 + 8):
                break
            v5 = load32(arg1)
            v10 = load32(9684500)
            arg3 = load32(9684496)
            v11 = 0
            while True:  # $label24
                v6 = (v11 << 2)
                v9 = load32((v5 + (v11 << 2)))
                v12 = load32((v5 + (v6 | 8)))
                v13 = load32((v5 + (v6 | 4)))
                arg2 = 0
                while True:  # $label22
                    while True:  # $label20
                        v8 = load32((arg3 - 16))
                        if load32((arg3 - 16)):
                            while True:  # $label21
                                arg4 = (arg3 + (arg2 * 60))
                                if (load32((arg3 + (arg2 * 60)) + 52) == v9):
                                    break
                                arg2 = (arg2 + 1)
                                if ((arg2 + 1) != v8):
                                    continue
                                break
                        arg2 = 0
                        v8 = load32((v10 - 16))
                        if not load32((v10 - 16)):
                            break
                        while True:  # $label23
                            arg4 = (v10 + (arg2 * 60))
                            if (load32((v10 + (arg2 * 60)) + 52) == v9):
                                break
                            arg2 = (arg2 + 1)
                            if ((arg2 + 1) != v8):
                                continue
                            break
                        break
                        break
                    arg2 = func370(arg4, v13, v12)
                    arg1 = load32(9681936)
                    v5 = load32(load32(9681936))
                    store32((load32(load32(9681936)) + (v6 | 12)), arg2)
                    v10 = load32(9684500)
                    arg3 = load32(9684496)
                    break
                v11 = (v11 + 4)
                if (u32((v11 + 4)) < u32(load32(arg1 + 8))):
                    continue
                break
            break
        while True:  # $label25
            if not load8u(9147212):
                break
            if not load32(load32(GAME_STATE) + 32):
                break
            arg1 = load32(9684368)
            store32(v7 + 24, load32(9684368))
            store32(v7 + 60, load32(9684364))
            arg0 = loadf32(9684356)
            # TODO: f64.promote_f32
            storef64(v7 + 16, loadf32(9684356))
            store32(v7 + 56, (load32(9684372) - arg1))
            v15 = loadf32(9684340)
            # TODO: f64.promote_f32
            storef64(v7 + 32, (loadf32(9684348) - loadf32(9684340)))
            v16 = loadf32(9684344)
            # TODO: f64.promote_f32
            storef64(v7 + 40, (loadf32(9684352) - loadf32(9684344)))
            # TODO: f64.promote_f32
            storef64(v7 + 48, (loadf32(9684360) - arg0))
            # TODO: f64.promote_f32
            storef64(v7, v15)
            # TODO: f64.promote_f32
            storef64(v7 + 8, v16)
            a_b()
            break
        func152()
        break
    G.global0 = (v7 - -64)

# ----------------------------------------------------------
# $ye
# Export: ye
# ----------------------------------------------------------
def ye(arg0):
    """Export: ye"""
    store8(9147152, 1)
    if not load8u(9147212):
        store32(PLAYER_COUNT, 3)
        v1 = load32(GAME_STATE)
        if load32(GAME_STATE):
            store32(GAME_STATE, 0)
        v2 = (arg0 << 2)
        v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        store32(9142428, arg0)
        store32(GAME_STATE, v1)
        if arg0:
            # TODO: memory.copy
        else:
        store32(load32(v1), arg0)
    return v2

# ----------------------------------------------------------
# $func586
# ----------------------------------------------------------
def func586(arg0, arg1, arg2):
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    arg2 = 0
    while True:  # $label0
        if (load8u(9142917) | load8u(9147152)):
            break
        v4 = load32(59164)
        v5 = load32(PLAYERS)
        while True:  # $label1
            v6 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            arg1 = 1
            while True:  # $label2
                v7 = (v5 + (arg1 * 286704))
                if (v4 == load32((v5 + (arg1 * 286704)) + 284616)):
                    arg2 = arg1
                    break
                if (v4 == load32(v7 + 284628)):
                    arg2 = arg1
                    break
                arg1 = (arg1 + 1)
                if ((arg1 + 1) != v6):
                    continue
                break
            break
        v7 = load32(arg0 + 8)
        if not load32(arg0 + 8):
            if load8u((load32(9143004) + (load32((v5 + (arg2 * 286704)) + 283908) + (load32(CURRENT_PLAYER) * v6)))):
                break
        arg2 = load32(arg0 + 4)
        v8 = load32(arg0)
        arg0 = 0
        while True:  # $label3
            if (u32(v6) < u32(2)):
                break
            arg1 = 1
            while True:  # $label4
                v9 = (v5 + (arg1 * 286704))
                if (v4 == load32((v5 + (arg1 * 286704)) + 284616)):
                    arg0 = arg1
                    break
                if (v4 == load32(v9 + 284628)):
                    arg0 = arg1
                    break
                arg1 = (arg1 + 1)
                if ((arg1 + 1) != v6):
                    continue
                break
            break
        store32(v3 + 16, v4)
        store32(v3 + 4, arg2)
        store32(v3, v8)
        store32(v3 + 12, not v7)
        store32(v3 + 8, (v5 + (arg0 * 286704)))
        break
    G.global0 = (v3 + 32)

# ----------------------------------------------------------
# $func587
# ----------------------------------------------------------
def func587(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg1 = 0
    v3 = load32(PLAYER_COUNT)
    v4 = load32(arg0)
    while True:  # $label0
        if load8u(9147210):
            if (u32(v3) < u32(2)):
                break
            v5 = load32(59164)
            v6 = load32(PLAYERS)
            arg1 = 1
            while True:  # $label1
                v7 = (v6 + (arg1 * 286704))
                if (load32((v6 + (arg1 * 286704)) + 284616) == v5):
                    break
                if (load32(v7 + 284628) == v5):
                    break
                arg1 = (arg1 + 1)
                if ((arg1 + 1) != v3):
                    continue
                break
            arg1 = 0
            break
        arg1 = load32(CURRENT_PLAYER)
        break
    while True:  # $label2
        if not v4:
            break
        if (arg1 == v4):
            break
        if (u32(v3) <= u32(v4)):
            break
        v3 = load32(GAME_STATE)
        if load32(load32(GAME_STATE) + 180):
            if (u32(load32(9142848)) < u32((load32(v3 + 72) * 2400))):
                break
        store32(arg2, load32(arg0 + 4))
        store32(arg2 + 4, load32(arg0 + 8))
        store32(arg2 + 8, load32(arg0 + 12))
        store32(arg2 + 12, load32(arg0 + 16))
        func322(v4, arg1, arg2)
        break
    G.global0 = (arg2 + 16)

# ----------------------------------------------------------
# $func588
# ----------------------------------------------------------
def func588(arg0, arg1):

# ----------------------------------------------------------
# $pb
# Export: pb
# ----------------------------------------------------------
def pb(arg0):
    """Export: pb"""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg0 = entities[arg0]
    v2 = load16u(entities[arg0] + 114)
    v3 = load16u(arg0 + 112)
    store32(v1, load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 84))
    store32(v1 + 4, v3)
    store32(v1 + 8, v2)
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $mb
# Export: mb
# ----------------------------------------------------------
def mb(arg0):
    """Export: mb"""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store8(9681824, arg0)
    if not load32(9216064):
        store32(41088, 7)
        store64(v1, 7)
    store32(9216064, 58)
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func591
# ----------------------------------------------------------
def func591(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func326(arg0)

# ----------------------------------------------------------
# $func592
# ----------------------------------------------------------
def func592(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func332(-1)

# ----------------------------------------------------------
# $func593
# ----------------------------------------------------------
def func593(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func327(arg0)

# ----------------------------------------------------------
# $func594
# ----------------------------------------------------------
def func594(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func328(arg0)

# ----------------------------------------------------------
# $func595
# ----------------------------------------------------------
def func595(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func329(arg0)

# ----------------------------------------------------------
# $func596
# ----------------------------------------------------------
def func596(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        store32(9143000, 0)
        arg0 = load32(9213820)
        if load32(9213820):
            func47(entities[arg0])
            store32(9213820, 0)
        func45()
        v10 = players[load32(CURRENT_PLAYER)]
        while True:  # $label13
            arg0 = 0
            while True:  # $label0
                arg1 = ((v5 * 404) + ENTITY_TYPES)
                if load32(((v5 * 404) + ENTITY_TYPES) + 264):
                    break
                if (load32(arg1 + 268) == 1):
                    break
                arg0 = (load32(arg1 + 92) != 0)
                break
            while True:  # $label1
                if not arg0:
                    break
                if (v5 == load32(38456)):
                    break
                if (v5 == load32(38764)):
                    break
                v7 = load32(((v10 + (v5 << 2)) + 284636))
                if not load32(((v10 + (v5 << 2)) + 284636)):
                    break
                v8 = 0
                v9 = load32(v7 + 8)
                if not load32(v7 + 8):
                    break
                while True:  # $label12
                    while True:  # $label2
                        arg0 = load32((load32(v7) + (v8 << 2)))
                        if not load32((load32(v7) + (v8 << 2))):
                            break
                        v2 = load32(ENTITIES)
                        arg1 = entities[arg0]
                        if not load8u(9147152):
                            if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(arg1 + 110))))):
                                break
                            if (load32((load32(9215884) + (load32(arg1 + 44) << 4)) + 4) == 20):
                                break
                            if (load8u(arg1 + 127) == 6):
                                break
                        v6 = load32(arg1 + 28)
                        while True:  # $label3
                            arg0 = load32(9215928)
                            if not load32(9215928):
                                break
                            v3 = load32(arg0 + 8)
                            if not load32(arg0 + 8):
                                break
                            v4 = load32(arg0)
                            arg0 = 0
                            while True:  # $label4
                                if (load32((v2 + (load32((v4 + (arg0 << 2))) * 132)) + 28) == v6):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v3):
                                    continue
                                break
                            break
                        while True:  # $label5
                            arg0 = load32(9215932)
                            if not load32(9215932):
                                break
                            v3 = load32(arg0 + 8)
                            if not load32(arg0 + 8):
                                break
                            v4 = load32(arg0)
                            arg0 = 0
                            while True:  # $label6
                                if (load32((v2 + (load32((v4 + (arg0 << 2))) * 132)) + 28) == v6):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v3):
                                    continue
                                break
                            break
                        while True:  # $label7
                            arg0 = load32(9215936)
                            if not load32(9215936):
                                break
                            v3 = load32(arg0 + 8)
                            if not load32(arg0 + 8):
                                break
                            v4 = load32(arg0)
                            arg0 = 0
                            while True:  # $label8
                                if (load32((v2 + (load32((v4 + (arg0 << 2))) * 132)) + 28) == v6):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v3):
                                    continue
                                break
                            break
                        while True:  # $label9
                            arg0 = load32(9215940)
                            if not load32(9215940):
                                break
                            v3 = load32(arg0 + 8)
                            if not load32(arg0 + 8):
                                break
                            v4 = load32(arg0)
                            arg0 = 0
                            while True:  # $label10
                                if (load32((v2 + (load32((v4 + (arg0 << 2))) * 132)) + 28) == v6):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v3):
                                    continue
                                break
                            break
                        if load32(arg1 + 36):
                            break
                        while True:  # $label11
                            if (load8u(arg1 + 125) == 8):
                                v2 = load32((load32(9215884) + (load32(arg1 + 44) << 4)) + 4)
                                if (load32((load32(9215884) + (load32(arg1 + 44) << 4)) + 4) == 43):
                                    break
                                arg0 = load8u(arg1 + 123)
                                if (load8u(arg1 + 123) == 43):
                                    break
                                if (v2 == 15):
                                    break
                                if (arg0 == 15):
                                    break
                                if (v2 == 28):
                                    break
                                if (arg0 == 28):
                                    break
                                if (v2 == 27):
                                    break
                                if (arg0 == 27):
                                    break
                                if (arg0 != 63):
                                    break
                                break
                            if (load8u(arg1 + 123) == 63):
                                break
                            break
                        func44(arg1, 0)
                        v9 = load32(v7 + 8)
                        break
                    v8 = (v8 + 1)
                    if (u32((v8 + 1)) < u32(v9)):
                        continue
                    break
                break
            v5 = (v5 + 1)
            if ((v5 + 1) != 255):
                continue
            break

# ----------------------------------------------------------
# $func597
# ----------------------------------------------------------
def func597(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        arg1 = 0
        store32(9143000, 0)
        arg0 = load32(9213820)
        if load32(9213820):
            func47(entities[arg0])
            store32(9213820, 0)
        func45()
        v10 = players[load32(CURRENT_PLAYER)]
        while True:  # $label13
            arg0 = 0
            while True:  # $label0
                v2 = ((arg1 * 404) + ENTITY_TYPES)
                if load32(((arg1 * 404) + ENTITY_TYPES) + 264):
                    break
                if (load32(v2 + 268) == 1):
                    break
                arg0 = (load32(v2 + 92) != 0)
                break
            while True:  # $label1
                if not arg0:
                    break
                if (arg1 == load32(38428)):
                    break
                if (arg1 == load32(38456)):
                    break
                if (arg1 == load32(38764)):
                    break
                if (arg1 == load32(38440)):
                    break
                if (arg1 == load32(38772)):
                    break
                if (arg1 == load32(38928)):
                    break
                v7 = load32(((v10 + (arg1 << 2)) + 284636))
                if not load32(((v10 + (arg1 << 2)) + 284636)):
                    break
                v8 = 0
                v9 = load32(v7 + 8)
                if not load32(v7 + 8):
                    break
                while True:  # $label12
                    while True:  # $label2
                        arg0 = load32((load32(v7) + (v8 << 2)))
                        if not load32((load32(v7) + (v8 << 2))):
                            break
                        v3 = load32(ENTITIES)
                        v2 = entities[arg0]
                        if not load8u(9147152):
                            if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(v2 + 110))))):
                                break
                            if (load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) == 20):
                                break
                            if (load8u(v2 + 127) == 6):
                                break
                        v6 = load32(v2 + 28)
                        while True:  # $label3
                            arg0 = load32(9215928)
                            if not load32(9215928):
                                break
                            v4 = load32(arg0 + 8)
                            if not load32(arg0 + 8):
                                break
                            v5 = load32(arg0)
                            arg0 = 0
                            while True:  # $label4
                                if (load32((v3 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v4):
                                    continue
                                break
                            break
                        while True:  # $label5
                            arg0 = load32(9215932)
                            if not load32(9215932):
                                break
                            v4 = load32(arg0 + 8)
                            if not load32(arg0 + 8):
                                break
                            v5 = load32(arg0)
                            arg0 = 0
                            while True:  # $label6
                                if (load32((v3 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v4):
                                    continue
                                break
                            break
                        while True:  # $label7
                            arg0 = load32(9215936)
                            if not load32(9215936):
                                break
                            v4 = load32(arg0 + 8)
                            if not load32(arg0 + 8):
                                break
                            v5 = load32(arg0)
                            arg0 = 0
                            while True:  # $label8
                                if (load32((v3 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v4):
                                    continue
                                break
                            break
                        while True:  # $label9
                            arg0 = load32(9215940)
                            if not load32(9215940):
                                break
                            v4 = load32(arg0 + 8)
                            if not load32(arg0 + 8):
                                break
                            v5 = load32(arg0)
                            arg0 = 0
                            while True:  # $label10
                                if (load32((v3 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v4):
                                    continue
                                break
                            break
                        if load32(v2 + 36):
                            break
                        while True:  # $label11
                            if (load8u(v2 + 125) == 8):
                                v3 = load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4)
                                if (load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) == 43):
                                    break
                                arg0 = load8u(v2 + 123)
                                if (load8u(v2 + 123) == 43):
                                    break
                                if (v3 == 15):
                                    break
                                if (arg0 == 15):
                                    break
                                if (v3 == 28):
                                    break
                                if (arg0 == 28):
                                    break
                                if (v3 == 27):
                                    break
                                if (arg0 == 27):
                                    break
                                if (arg0 != 63):
                                    break
                                break
                            if (load8u(v2 + 123) == 63):
                                break
                            break
                        func44(v2, 0)
                        v9 = load32(v7 + 8)
                        break
                    v8 = (v8 + 1)
                    if (u32((v8 + 1)) < u32(v9)):
                        continue
                    break
                break
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != 255):
                continue
            break

# ----------------------------------------------------------
# $func598
# ----------------------------------------------------------
def func598(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func325(arg0)