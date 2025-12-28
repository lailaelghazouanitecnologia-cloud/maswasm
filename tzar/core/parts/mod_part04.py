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
# $func154
# ----------------------------------------------------------
def func154(arg0):
    # TODO: i32.atomic.rmw.xchg
    if (0 == 2):
        func97(arg0)

# ----------------------------------------------------------
# $func155
# ----------------------------------------------------------
def func155(arg0, arg1, arg2):
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v4 = load32(PLAYERS)
    v6 = load16u(arg0 + 110)
    while True:  # $label0
        if not load32(9147132):
            break
        if (load32(9671152) != load8u(arg1 + 122)):
            break
        v5 = load16u(arg1 + 110)
        if (v6 == load16u(arg1 + 110)):
            break
        if not v6:
            break
        v8 = (v4 + (v5 * 286704))
        v5 = (v4 + (v5 * 286704))
        v9 = load32((v4 + (v5 * 286704)) + 284628)
        v5 = load32(v5 + 284616)
        v7 = (v4 + (v6 * 286704))
        v10 = load32((v4 + (v6 * 286704)) + 284616)
        store32(v3 + 16, (load32((v4 + (v6 * 286704)) + 284616) if v10 else load32(v7 + 284628)))
        store32(v3 + 12, v7)
        store32(v3 + 4, v8)
        store32(v3, 927)
        store32(v3 + 8, (v5 if v5 else v9))
        a_b()
        break
    while True:  # $label1
        if arg2:
            break
        while True:  # $label2
            v4 = load32(((v4 + (v6 * 286704)) + 278560))
            if not load32(((v4 + (v6 * 286704)) + 278560)):
                arg2 = load16u(arg1 + 110)
                break
            arg2 = load16u(arg1 + 110)
            v4 = (v4 + ((load8u(arg0 + 122) + (load16u(arg1 + 110) * 255)) << 2))
            store32((v4 + ((load8u(arg0 + 122) + (load16u(arg1 + 110) * 255)) << 2)), (load32(v4) + 1))
            break
        arg2 = load32((players[arg2] + 278568))
        if not load32((players[arg2] + 278568)):
            break
        arg2 = (arg2 + ((load8u(arg1 + 122) + (load16u(arg0 + 110) * 255)) << 2))
        store32((arg2 + ((load8u(arg1 + 122) + (load16u(arg0 + 110) * 255)) << 2)), (load32(arg2) + 1))
        break
    store16(arg1 + 116, load32(arg0 + 28))
    G.global0 = (v3 + 32)

# ----------------------------------------------------------
# $func156
# ----------------------------------------------------------
def func156(arg0, arg1, param2):
    v2 = load8u(arg0 + 125)
    while True:  # $label3
        while True:  # $label4
            while True:  # $label0
                while True:  # $label2
                    while True:  # $label1
                        v3 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
                        v4 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264)
                        # br_table load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264)
                        break
                        break
                    if (load32(v3 + 268) != 1):
                        break
                    if load32(arg0 + 52):
                        break
                    break
                    break
                if (v4 != 4):
                    break
                if not load32(arg0 + 52):
                    break
                break
                break
            if not load32(arg0 + 52):
                break
            break
        if (load8u(arg0 + 126) == 2):
            break
        if load32(arg0 + 36):
            break
        if (v2 == 13):
            break
        func63(0, arg0, 22, 0, arg1)
        return
        break
    arg1 = load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
    store32(arg0 + 44, 0)

# ----------------------------------------------------------
# $func157
# ----------------------------------------------------------
def func157(arg0):
    while True:  # $label0
        v2 = load8u(arg0 + 122)
        if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
            break
        v3 = load32(arg0 + 20)
        if not load32(arg0 + 20):
            break
        if (load32(38540) == v2):
            break
        if (load32(38812) == v2):
            break
        if (load32(38888) == v2):
            break
        if load32(v3 + 8):
            v2 = players[load16u(arg0 + 110)]
            v18 = (players[load16u(arg0 + 110)] + 283908)
            v19 = (v2 + 286701)
            v9 = (v2 + 281704)
            v10 = (v2 + 281700)
            v11 = (v2 + 281696)
            v12 = (v2 + 281692)
            v13 = (v2 + 283860)
            v14 = (v2 + 283856)
            v15 = (v2 + 283852)
            v16 = (v2 + 283848)
            v5 = load32(9143016)
            v20 = load32(v3)
            v21 = (load8u(arg0 + 125) - 4)
            while True:  # $label4
                arg0 = load32((v20 + (v4 << 2)))
                v1 = (u32(arg0) > u32(2147483646))
                v17 = ((load32((v20 + (v4 << 2))) - 2147483647) if (u32(arg0) > u32(2147483646)) else arg0)
                while True:  # $label2
                    while True:  # $label1
                        if not v4:
                            if (u32(arg0) < u32(2147483647)):
                                break
                            # br_table v21
                            break
                        if v1:
                            break
                        break
                    arg0 = ((v17 * 404) + 9568164)
                    v1 = load32(v16)
                    if (load32(v16) != 2147483647):
                        store32(v16, (load32(arg0) + v1))
                    v1 = load32(v15)
                    if (load32(v15) != 2147483647):
                        store32(v15, (load32(arg0 + 4) + v1))
                    v1 = load32(v14)
                    if (load32(v14) != 2147483647):
                        store32(v14, (load32(arg0 + 8) + v1))
                    v1 = load32(v13)
                    if (load32(v13) != 2147483647):
                        store32(v13, (load32(arg0 + 12) + v1))
                    store32(v12, (load32(v12) - load32(arg0)))
                    store32(v11, (load32(v11) - load32(arg0 + 4)))
                    store32(v10, (load32(v10) - load32(arg0 + 8)))
                    store32(v9, (load32(v9) - load32(arg0 + 12)))
                    store8(v19, 1)
                    v1 = load32(PLAYER_COUNT)
                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                        break
                    arg0 = 1
                    v6 = (v1 - 1)
                    v22 = ((v1 - 1) & 1)
                    v7 = (load32(v18) * v1)
                    v8 = load32(PLAYERS)
                    if (v1 != 2):
                        v6 = (v6 & -2)
                        v1 = 0
                        while True:  # $label3
                            if load8u((v5 + (arg0 + v7))):
                                store8((v8 + (arg0 * 286704)) + 286701, 1)
                            v23 = (arg0 + 1)
                            if load8u((v5 + ((arg0 + 1) + v7))):
                                store8((v8 + (v23 * 286704)) + 286701, 1)
                            arg0 = (arg0 + 2)
                            v1 = (v1 + 2)
                            if ((v1 + 2) != v6):
                                continue
                            break
                    if not v22:
                        break
                    if not load8u((v5 + (arg0 + v7))):
                        break
                    store8((v8 + (arg0 * 286704)) + 286701, 1)
                    break
                arg0 = ((v2 + (v17 << 2)) + 282828)
                store32(((v2 + (v17 << 2)) + 282828), (load32(arg0) - 1))
                v4 = (v4 + 1)
                if (u32((v4 + 1)) < u32(load32(v3 + 8))):
                    continue
                break
        store32(v3 + 8, 0)
        break

# ----------------------------------------------------------
# $func158
# ----------------------------------------------------------
def func158(arg0):
    func77(arg0)
    if load32(arg0 + 40):
        v1 = load32(arg0 + 12)
        if load32(arg0 + 12):
            if load32(v1 + 8):
                while True:  # $label0
                    func38(load32((load32(v1) + (v2 << 2))))
                    v2 = (v2 + 2)
                    v1 = load32(arg0 + 12)
                    if (u32((v2 + 2)) < u32(load32(load32(arg0 + 12) + 8))):
                        continue
                    break
            store32(v1 + 8, 0)
        while True:  # $label1
            v1 = load32(arg0 + 24)
            if not load32(arg0 + 24):
                break
            v3 = load32(v1 + 4)
            if not load32(v1 + 4):
                break
            v1 = load32(v3 + 8)
            if not load32(v3 + 8):
                break
            v4 = load32(v3)
            v2 = 0
            while True:  # $label2
                v5 = ((v2 | 1) << 2)
                v6 = load32((v4 + ((v2 | 1) << 2)))
                if load32((v4 + ((v2 | 1) << 2))):
                    func38(v6)
                    v4 = load32(v3)
                    store32((load32(v3) + v5), 0)
                    v1 = load32(v3 + 8)
                v2 = (v2 + 2)
                if (u32((v2 + 2)) < u32(v1)):
                    continue
                break
            break
        func38(load32(arg0 + 40))
        store32(arg0 + 40, 0)

# ----------------------------------------------------------
# $func159
# ----------------------------------------------------------
def func159(arg0):
    v3 = load32(arg0 + 28)
    v5 = load32(ENTITIES)
    while True:  # $label1
        while True:  # $label0
            arg0 = load32(9215928)
            if not load32(9215928):
                break
            v1 = load32(arg0 + 8)
            if not load32(arg0 + 8):
                break
            v2 = load32(arg0)
            arg0 = 0
            while True:  # $label2
                if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v3):
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v1):
                    continue
                break
            break
        while True:  # $label3
            arg0 = load32(9215932)
            if not load32(9215932):
                break
            v1 = load32(arg0 + 8)
            if not load32(arg0 + 8):
                break
            v2 = load32(arg0)
            arg0 = 0
            while True:  # $label4
                if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v3):
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v1):
                    continue
                break
            break
        while True:  # $label5
            arg0 = load32(9215936)
            if not load32(9215936):
                break
            v1 = load32(arg0 + 8)
            if not load32(arg0 + 8):
                break
            v2 = load32(arg0)
            arg0 = 0
            while True:  # $label6
                if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v3):
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v1):
                    continue
                break
            break
        v4 = 1
        arg0 = load32(9215940)
        if not load32(9215940):
            break
        v1 = load32(arg0 + 8)
        if not load32(arg0 + 8):
            break
        v2 = load32(arg0)
        arg0 = 0
        while True:  # $label7
            v6 = load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28)
            v4 = (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) != v3)
            if (v3 == v6):
                break
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != v1):
                continue
            break
        break
    return v4

# ----------------------------------------------------------
# $func160
# ----------------------------------------------------------
def func160(arg0, arg1, arg2):
    v3 = load8u(59181)
    v8 = load16u(arg0 + 114)
    v9 = load16u(arg0 + 112)
    while True:  # $label1
        while True:  # $label0
            if load8u(9147152):
                v4 = load8u(arg0 + 125)
                break
            v4 = load32(CURRENT_PLAYER)
            if not load32(CURRENT_PLAYER):
                break
            if not load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(PLAYER_COUNT) * v4)))):
                break
            v4 = load8u(arg0 + 125)
            if (load8u(arg0 + 125) == 3):
                break
            break
        v7 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        v5 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 220)
        arg0 = ((v8 - (arg2 if v3 else 0)) + ((load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 220) & 0xFFFFFFFF) >> 1))
        v3 = load32(v7 + 216)
        v8 = ((v9 - (arg1 if v3 else 0)) + ((load32(v7 + 216) & 0xFFFFFFFF) >> 1))
        while True:  # $label4
            while True:  # $label3
                while True:  # $label2
                    # br_table (v4 - 4)
                    break
                    break
                break
                break
            break
        v7 = load32(v7 + 200)
        while True:  # $label5
            if not load32(load32(GAME_STATE) + 48):
                break
            v10 = (((arg1 + (arg2 * 3)) + 4) << 2)
            v3 = load32(9142836)
            v4 = ((((arg1 + (arg2 * 3)) + 4) << 2) + (load32(9142836) + (v7 * 80)))
            v11 = load32(((((arg1 + (arg2 * 3)) + 4) << 2) + (load32(9142836) + (v7 * 80))) + 44)
            if load32(((((arg1 + (arg2 * 3)) + 4) << 2) + (load32(9142836) + (v7 * 80))) + 44):
                v5 = load32(v4 + 8)
                v4 = load32(9142440)
                v3 = 0
                while True:  # $label7
                    while True:  # $label6
                        v6 = (v3 << 2)
                        v9 = (load32((v5 + ((v3 << 2) | 4))) + arg0)
                        if (u32(v4) <= u32((load32((v5 + ((v3 << 2) | 4))) + arg0))):
                            break
                        v6 = (load32((v5 + v6)) + v8)
                        if (u32(v4) <= u32((load32((v5 + v6)) + v8))):
                            break
                        if ((v6 | v9) < 0):
                            break
                        v4 = load32(9142440)
                        break
                    v3 = (v3 + 2)
                    if (u32((v3 + 2)) < u32(v11)):
                        continue
                    break
                v3 = load32(9142836)
            v3 = ((v3 + ((v7 + 4) * 80)) + v10)
            v10 = load32(((v3 + ((v7 + 4) * 80)) + v10) + 44)
            if load32(((v3 + ((v7 + 4) * 80)) + v10) + 44):
                v5 = load32(v3 + 8)
                v4 = load32(9142440)
                v3 = 0
                while True:  # $label9
                    while True:  # $label8
                        v6 = (v3 << 2)
                        v9 = (load32((v5 + ((v3 << 2) | 4))) + arg0)
                        if (u32(v4) <= u32((load32((v5 + ((v3 << 2) | 4))) + arg0))):
                            break
                        v6 = (load32((v5 + v6)) + v8)
                        if (u32(v4) <= u32((load32((v5 + v6)) + v8))):
                            break
                        if ((v6 | v9) < 0):
                            break
                        func258(v6, v9)
                        v4 = load32(9142440)
                        break
                    v3 = (v3 + 2)
                    if (u32((v3 + 2)) < u32(v10)):
                        continue
                    break
            if (load32(load32(GAME_STATE) + 48) == 1):
                break
            v3 = ((load32(9142836) + (v7 * 80)) + ((((1 - arg2) * 3) - arg1) << 2))
            v7 = load32(((load32(9142836) + (v7 * 80)) + ((((1 - arg2) * 3) - arg1) << 2)) + 48)
            if not load32(((load32(9142836) + (v7 * 80)) + ((((1 - arg2) * 3) - arg1) << 2)) + 48):
                break
            v5 = (arg0 + arg2)
            v8 = (arg1 + v8)
            arg0 = load32(v3 + 12)
            v4 = load32(9142440)
            v3 = 0
            while True:  # $label11
                while True:  # $label10
                    arg2 = (v3 << 2)
                    arg1 = (v5 + load32((arg0 + ((v3 << 2) | 4))))
                    if (u32(v4) <= u32((v5 + load32((arg0 + ((v3 << 2) | 4)))))):
                        break
                    arg2 = (v8 + load32((arg0 + arg2)))
                    if (u32(v4) <= u32((v8 + load32((arg0 + arg2))))):
                        break
                    if ((arg1 | arg2) < 0):
                        break
                    v4 = load32(9142440)
                    break
                v3 = (v3 + 2)
                if (u32((v3 + 2)) < u32(v7)):
                    continue
                break
            break
        break
    return func129(arg2, arg1, 0)

# ----------------------------------------------------------
# $func161
# ----------------------------------------------------------
def func161(arg0, arg1, arg2):
    v8 = load32(ENTITIES)
    v11 = entities[load32(arg1)]
    v9 = load8u(entities[load32(arg1)].sub_state)
    v3 = load8u(arg0 + 122)
    v13 = 1
    while True:  # $label0
        if not arg2:
            v12 = 1
            break
        v12 = 1
        while True:  # $label4
            while True:  # $label1
                while True:  # $label2
                    while True:  # $label3
                        v5 = (v8 + (load32((arg1 + (v4 << 2))) * 132))
                        v6 = load8u((v8 + (load32((arg1 + (v4 << 2))) * 132)) + 122)
                        # br_table (load8u((v8 + (load32((arg1 + (v4 << 2))) * 132)) + 122) + -64)
                        break
                        break
                    if (v6 == 10):
                        break
                    break
                v13 = 0
                break
            if load32(((v6 * 404) + ENTITY_TYPES) + 264):
                v12 = 0
                v7 = (v7 | not load32(v5 + 52))
            v9 = (-1 if (v6 != v9) else v9)
            v4 = (v4 + 1)
            if ((v4 + 1) != arg2):
                continue
            break
        break
    v4 = load16u(v11 + 110)
    v6 = load8u(arg0 + 128)
    while True:  # $label5
        v11 = load32(38768)
        if (v3 == load32(38768)):
            arg2 = 55
            if (v9 == load32(38712)):
                break
        arg2 = 35
        v8 = load32(((v3 * 404) + ENTITY_TYPES) + 264)
        if ((load32(((v3 * 404) + ENTITY_TYPES) + 264) == 2) & v12):
            break
        while True:  # $label6
            v15 = load8u(9216060)
            if not (not load8u(9216060) & v13):
                break
            if (v8 != 1):
                break
            v14 = load32(((v3 * 404) + ENTITY_TYPES) + 112)
            if not load32(((v3 * 404) + ENTITY_TYPES) + 112):
                break
            arg1 = load16u(arg0 + 110)
            while True:  # $label9
                while True:  # $label7
                    if (load32(38500) == v3):
                        break
                    v5 = (load32(PLAYER_COUNT) * v4)
                    v10 = load32(9143004)
                    while True:  # $label8
                        arg2 = load16u(arg0 + 120)
                        if load16u(arg0 + 120):
                        else:
                        if not load8u(((arg2 if load8u((v10 + (arg1 + v5))) else arg1) + (arg1 + v5))):
                            if v6:
                                break
                            if (load8u(arg0 + 127) == 6):
                                break
                            break
                        if v6:
                            break
                        break
                    v5 = load8u(arg0 + 125)
                    if (load8u(arg0 + 125) == 10):
                        break
                    if (load8u(arg0 + 126) == 2):
                        break
                    if (load32(arg0 + 64) == -1):
                        break
                    if (load32(((v3 * 404) + ENTITY_TYPES) + 188) != 55):
                        break
                    if (load32(38560) == v3):
                        break
                    if (load32(38620) == v3):
                        break
                    if (load32(38564) != v3):
                        break
                    break
                if (arg1 != v4):
                    break
                if (u32(v14) <= u32(load32(arg0 + 84))):
                    break
                v5 = load8u(arg0 + 125)
                break
            arg2 = 54
            # br_table (v5 - 4)
            break
            break
        arg1 = load16u(arg0 + 110)
        while True:  # $label13
            while True:  # $label12
                while True:  # $label10
                    if (load32(38500) == v3):
                        break
                    v5 = (load32(PLAYER_COUNT) * v4)
                    v10 = load32(9143004)
                    arg2 = arg1
                    while True:  # $label11
                        v14 = load16u(arg0 + 120)
                        if load16u(arg0 + 120):
                        else:
                        if not load8u(((v14 if load8u((v10 + (arg1 + v5))) else arg1) + (arg2 + v5))):
                            if v6:
                                break
                            if (load8u(arg0 + 127) == 6):
                                break
                            break
                        if v6:
                            break
                        break
                    if (load8u(arg0 + 125) == 10):
                        break
                    if (load8u(arg0 + 126) == 2):
                        break
                    if (load32(arg0 + 64) == -1):
                        break
                    if (v8 == 2):
                        break
                    if (load32(((v3 * 404) + ENTITY_TYPES) + 188) != 55):
                        break
                    if (load32(38560) == v3):
                        break
                    if (load32(38620) == v3):
                        break
                    if (load32(38564) != v3):
                        break
                    break
                if ((v7 | (load32(38564) != v3)) & 1):
                    break
                arg2 = 6
                # br_table (load8u(arg0 + 125) - 4)
                break
                break
            arg2 = 6
            if not (v7 & 1):
                break
            break
        while True:  # $label14
            if not v13:
                break
            while True:  # $label15
                if (load32(38528) != v3):
                    break
                if not load8u((load32(9143004) + ((load32(PLAYER_COUNT) * arg1) + v4))):
                    break
                arg2 = 61
                if (load32(((players[v4] + (load32(39188) << 2)) + 281808)) == 1):
                    break
                break
            arg2 = load8u(arg0 + 125)
            while True:  # $label17
                while True:  # $label16
                    if not v15:
                        if (arg2 == 10):
                            break
                        if (load32(((v3 * 404) + ENTITY_TYPES) + 188) == 55):
                            break
                        arg2 = 1
                        if (v3 == v11):
                            break
                        break
                    if (arg2 == 10):
                        break
                    if load32(((v3 * 404) + ENTITY_TYPES) + 188):
                        break
                    return 1
                    break
                arg2 = 1
                if (v3 != v11):
                    break
                break
            if (u32(load32(arg0 + 64)) >= u32(load32(arg0 + 68))):
                break
            arg2 = 4
            while True:  # $label18
                # br_table v8
                break
                break
            if (load32(((v3 * 404) + ENTITY_TYPES) + 268) == 2):
                break
            break
        arg2 = 0
        if load8u(9147152):
        else:
            if not load8u((load32(9143008) + ((load32(PLAYER_COUNT) * arg1) + v4))):
                break
            if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                break
        if (load8u(arg0 + 127) == 6):
            return 0
        if (v3 == v9):
            return 0
        arg1 = ((v3 * 404) + ENTITY_TYPES)
        if not load32(((v3 * 404) + ENTITY_TYPES) + 136):
            break
        if not ((load32(arg1 + 140) != 0) & v12):
            break
        arg0 = load8u(arg0 + 125)
        arg2 = ((25 if (load8u(arg0 + 125) != 4) else 0) if (arg0 != 14) else 0)
        break
    return arg2

# ----------------------------------------------------------
# $func162
# ----------------------------------------------------------
def func162(arg0, arg1, arg2, arg3):
    while True:  # $label2
        while True:  # $label0
            if (u32(load32(9142848)) >= u32((load32(load32(GAME_STATE) + 72) * 2400))):
                break
            if (load32(arg0 + 56) == 1):
            else:
            if 0:
                break
            if (load32(38564) == arg1):
                break
            while True:  # $label1
                # br_table (arg2 - 4)
                break
                break
            if not arg3:
                break
            arg2 = load32(PLAYERS)
            v5 = load32(ENTITIES)
            v4 = entities[arg3]
            v6 = load16u(entities[arg3] + 110)
            v7 = load32(players[load16u(entities[arg3] + 110)] + 283872)
            if not load32(players[load16u(entities[arg3] + 110)] + 283872):
                break
            v4 = (load16u(v4 + 112) - v7)
            v4 = (v4 >> 31)
            if (u32((((load16u(v4 + 112) - v7) ^ (v4 >> 31)) - v4)) > u32(30)):
                break
            v4 = 0
            arg2 = (load16u((v5 + (arg3 * 132)) + 114) - load32((arg2 + (v6 * 286704)) + 283876))
            arg2 = (arg2 >> 31)
            if (u32((((load16u((v5 + (arg3 * 132)) + 114) - load32((arg2 + (v6 * 286704)) + 283876)) ^ (arg2 >> 31)) - arg2)) < u32(31)):
                break
            break
        arg3 = ((arg1 * 404) + ENTITY_TYPES)
        arg2 = load32(((arg1 * 404) + ENTITY_TYPES) + 264)
        arg0 = load8u(arg0 + 122)
        while True:  # $label3
            if (load32(arg3 + 188) == 55):
                break
            if (arg2 != 1):
                break
            if (load32(38500) == arg1):
                break
            return 0
            break
        if (arg2 == 4):
            v4 = 0
            if (load32(((arg0 * 404) + ENTITY_TYPES) + 224) == 1):
                break
        v4 = 0
        while True:  # $label4
            if not load32(((arg0 * 404) + ENTITY_TYPES) + 272):
                if (load32(38648) != arg0):
                    break
            if (load32(((arg1 * 404) + ENTITY_TYPES) + 208) == 2):
                break
            break
        while True:  # $label5
            if (load32(38564) != arg1):
                break
            arg3 = ((arg0 * 404) + ENTITY_TYPES)
            if load8u(((arg0 * 404) + ENTITY_TYPES) + 334):
                break
            if (load32(arg3 + 268) != 2):
                break
            break
        while True:  # $label6
            if (arg0 != load32(38728)):
                if (load32(38996) != arg0):
                    break
            if arg2:
                break
            if (load32(((arg1 * 404) + ENTITY_TYPES) + 268) == 2):
                break
            break
        arg2 = ((arg0 * 404) + ENTITY_TYPES)
        if load8u(((arg0 * 404) + ENTITY_TYPES) + 379):
            break
        arg2 = load32(arg2 + 24)
        if not load32(arg2 + 24):
            return 1
        arg3 = load32(((arg0 * 404) + ENTITY_TYPES) + 364)
        if not load32(((arg0 * 404) + ENTITY_TYPES) + 364):
            break
        arg0 = 0
        while True:  # $label7
            v4 = (load32((arg2 + (arg0 << 2))) == arg1)
            if (load32((arg2 + (arg0 << 2))) == arg1):
                break
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg3):
                continue
            break
        break
    return v4

# ----------------------------------------------------------
# $func163
# ----------------------------------------------------------
def func163(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    v8 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if (u32(arg2) <= u32(((arg1 ^ -1) + 2147483631))):
        while True:  # $label0
            if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
                break
            break
        v9 = arg0
        if (u32(arg1) < u32(1073741799)):
            store32(v8 + 12, (arg1 << 1))
            store32(v8 + 4, (arg1 + arg2))
            arg2 = (G.global0 - 16)
            G.global0 = (G.global0 - 16)
            v10 = (v8 + 4)
            v11 = (v8 + 12)
            v12 = (u32(load32((v8 + 4))) < u32(load32((v8 + 12))))
            G.global0 = (arg2 + 16)
            arg2 = load32((v11 if v12 else v10))
            if (u32(load32((v11 if v12 else v10))) >= u32(11)):
                arg2 = ((arg2 + 16) & -16)
                arg2 = (arg2 - 1)
            else:
        else:
        func314((((arg2 + 16) & -16) if (arg2 == 11) else (arg2 - 1)), 11, 2147483631)
        arg2 = load32(v8 + 4)
        if arg4:
            func122(arg2, v9, arg4)
        if arg6:
            func122((arg2 + arg4), arg7, arg6)
        v10 = (arg4 + arg5)
        arg7 = (arg3 - (arg4 + arg5))
        if (arg3 != v10):
            func122(((arg2 + arg4) + arg6), ((arg4 + v9) + arg5), arg7)
        if (arg1 != 10):
        store32(arg0, arg2)
        store32(arg0 + 8, ((load32(arg0 + 8) & -2147483648) | (load32(v8 + 8) & 2147483647)))
        store32(arg0 + 8, (load32(arg0 + 8) | -2147483648))
        arg0 = ((arg4 + arg6) + arg7)
        store32(arg0 + 4, ((arg4 + arg6) + arg7))
        store8(v8 + 12, 0)
        store8((arg0 + arg2), load8u(v8 + 12))
        G.global0 = (v8 + 16)
        return af(v9)
    func212()
    raise Unreachable()
    return arg0

# ----------------------------------------------------------
# $func164
# ----------------------------------------------------------
def func164():
    while True:  # $label0
        v2 = ((v0 * 132) + 9216080)
        if load8u(((v0 * 132) + 9216080) + 23):
            store32(((load32(v2 + 4) * 404) + ENTITY_TYPES) + 180, v2)
        store32(v2 + 68, 0)
        store32(v2 + 112, 0)
        v0 = (v0 + 1)
        if ((v0 + 1) != 356):
            continue
        break
    v8 = load8u(9216060)
    while True:  # $label7
        v2 = ((v4 * 404) + ENTITY_TYPES)
        if not load32(((v4 * 404) + ENTITY_TYPES) + 148):
            store32(v2 + 148, 9)
        while True:  # $label1
            v0 = load32(v2 + 244)
            if not load32(v2 + 244):
                break
            v3 = load32(v2 + 240)
            v1 = 0
            if (v0 != 1):
                v9 = (v0 & -2)
                v6 = 0
                while True:  # $label2
                    v7 = (v1 << 2)
                    v5 = ((load32((v3 + (v1 << 2))) * 132) + 9216080)
                    v10 = load32(v5 + 68)
                    store32(((load32((v3 + (v1 << 2))) * 132) + 9216080) + 68, (load32(v5 + 68) + 1))
                    store32((v5 + (v10 << 2)) + 28, v4)
                    v5 = ((load32((v3 + (v7 | 4))) * 132) + 9216080)
                    v7 = load32(v5 + 68)
                    store32(((load32((v3 + (v7 | 4))) * 132) + 9216080) + 68, (load32(v5 + 68) + 1))
                    store32((v5 + (v7 << 2)) + 28, v4)
                    v1 = (v1 + 2)
                    v6 = (v6 + 2)
                    if ((v6 + 2) != v9):
                        continue
                    break
            if not (v0 & 1):
                break
            v1 = ((load32((v3 + (v1 << 2))) * 132) + 9216080)
            v0 = load32(v1 + 68)
            store32(((load32((v3 + (v1 << 2))) * 132) + 9216080) + 68, (load32(v1 + 68) + 1))
            store32((v1 + (v0 << 2)) + 28, v4)
            break
        while True:  # $label3
            v1 = load32(v2 + 180)
            if not load32(v2 + 180):
                break
            v0 = load32(v2 + 264)
            if (load32(v2 + 264) == 1):
                while True:  # $label4
                    v0 = load32(v2 + 196)
                    if not (not v8 & (load32(v2 + 196) != 3)):
                        v0 = load32(v1 + 112)
                        store32(v1 + 112, (load32(v1 + 112) + 1))
                        v3 = (v1 + 72)
                        store32(((v1 + 72) + (v0 << 2)), 10)
                        v0 = load32(v1 + 112)
                        store32(v1 + 112, (load32(v1 + 112) + 1))
                        store32((v3 + (v0 << 2)), 79)
                        break
                    break
                v0 = load32(((v0 << 2) + 9940))
                v3 = load32(v1 + 112)
                store32(v1 + 112, (load32(v1 + 112) + 1))
                store32((v1 + (v3 << 2)) + 72, v0)
            else:
            if (v0 == 3):
                break
            v0 = load32(v2 + 236)
            if not load32(v2 + 236):
                break
            v6 = load32(v2 + 232)
            v1 = 0
            while True:  # $label6
                while True:  # $label5
                    v3 = ((load32((v6 + (v1 << 2))) * 132) + 9216080)
                    if not load8u(((load32((v6 + (v1 << 2))) * 132) + 9216080) + 23):
                        break
                    v3 = load32(((load32(v3 + 4) * 404) + ENTITY_TYPES) + 180)
                    if not load32(((load32(v3 + 4) * 404) + ENTITY_TYPES) + 180):
                        break
                    v0 = load32(v3 + 112)
                    store32(v3 + 112, (load32(v3 + 112) + 1))
                    store32((v3 + (v0 << 2)) + 72, v4)
                    v0 = load32(v2 + 236)
                    break
                v1 = (v1 + 1)
                if (u32((v1 + 1)) < u32(v0)):
                    continue
                break
            break
        v4 = (v4 + 1)
        if ((v4 + 1) != 255):
            continue
        break
    return load32(v2 + 264)

# ----------------------------------------------------------
# $func165
# ----------------------------------------------------------
def func165(arg0, arg1):
    while True:  # $label9
        while True:  # $label1
            while True:  # $label3
                while True:  # $label2
                    while True:  # $label0
                        # br_table load32(arg0 + 4)
                        break
                        break
                    if not load32(arg0 + 88):
                        break
                    v7 = load32(arg0 + 32)
                    v8 = not load32(arg0 + 32)
                    while True:  # $label8
                        while True:  # $label7
                            v4 = load32((load32(arg0 + 80) + (v6 << 2)))
                            if (call_table(arg1) != (load8u(arg0 + 45) != 0)):
                                v3 = load32(9140300)
                                while True:  # $label5
                                    while True:  # $label4
                                        if (u32(load32(9684388)) >= u32(2)):
                                            v2 = 0
                                            if not v3:
                                                break
                                            while True:  # $label6
                                                if (load32(((v2 << 2) + 8451904)) == v4):
                                                    break
                                                v2 = (v2 + 1)
                                                if ((v2 + 1) != v3):
                                                    continue
                                                break
                                        v2 = v3
                                        if (u32(v3) > u32(39999)):
                                            break
                                        break
                                    store32(9140300, (v2 + 1))
                                    store32(((v2 << 2) + 8451904), v4)
                                    break
                                store32((load32(9142420) + (load16u(entities[v4] + 110) << 2)), 1)
                                v5 = (v5 | v8)
                                break
                            if v7:
                                break
                            break
                        v6 = (v6 + 1)
                        if (u32((v6 + 1)) < u32(load32(arg0 + 88))):
                            continue
                        break
                    v7 = ((v7 != 0) | v5)
                    break
                    break
                v8 = load32(9140300)
                v4 = load32(arg0 + 32)
                store32(9140300, 0)
                if load32(PLAYER_COUNT):
                    v3 = load32(9142420)
                    while True:  # $label10
                        store32((v3 + (v2 << 2)), 0)
                        v2 = (v2 + 1)
                        if (u32((v2 + 1)) < u32(load32(PLAYER_COUNT))):
                            continue
                        break
                if v8:
                    v9 = not v4
                    while True:  # $label15
                        while True:  # $label14
                            v7 = load32(((v6 << 2) + 8451904))
                            if (call_table(arg1) != (load8u(arg0 + 45) != 0)):
                                v3 = load32(9140300)
                                while True:  # $label12
                                    while True:  # $label11
                                        if (u32(load32(9684388)) >= u32(2)):
                                            v2 = 0
                                            if not v3:
                                                break
                                            while True:  # $label13
                                                if (load32(((v2 << 2) + 8451904)) == v7):
                                                    break
                                                v2 = (v2 + 1)
                                                if ((v2 + 1) != v3):
                                                    continue
                                                break
                                        v2 = v3
                                        if (u32(v3) > u32(39999)):
                                            break
                                        break
                                    store32(9140300, (v2 + 1))
                                    store32(((v2 << 2) + 8451904), v7)
                                    break
                                store32((load32(9142420) + (load16u(entities[v7] + 110) << 2)), 1)
                                v5 = (v5 | v9)
                                break
                            if v4:
                                break
                            break
                        v6 = (v6 + 1)
                        if ((v6 + 1) != v8):
                            continue
                        break
                v7 = ((v4 != 0) | v5)
                break
                break
            v7 = 0
            break
            break
        v2 = load32(PLAYER_COUNT)
        if not load32(PLAYER_COUNT):
            break
        v3 = load32(arg0 + 32)
        v13 = (u32(load32(arg0 + 32)) > u32(3))
        v14 = (v3 - 1)
        v15 = ((v3 - 4) << 2)
        while True:  # $label38
            v3 = load32(arg0 + 48)
            v2 = load32((load32(arg0 + 48) + (v2 << 2)))
            while True:  # $label16
                while True:  # $label18
                    while True:  # $label17
                        v9 = (v8 << 2)
                        if not load32((v3 + (v8 << 2))):
                            if not v2:
                                break
                            if load32((load32(9142420) + v9)):
                                break
                            break
                        if not v2:
                            break
                        break
                    store32((load32(9142420) + v9), 0)
                    break
                v6 = 0
                v16 = load32(9140300)
                v10 = load32(PLAYERS)
                v4 = 0
                while True:  # $label37
                    while True:  # $label36
                        while True:  # $label35
                            while True:  # $label30
                                while True:  # $label29
                                    if not v13:
                                        while True:  # $label28
                                            while True:  # $label23
                                                while True:  # $label22
                                                    while True:  # $label20
                                                        while True:  # $label21
                                                            while True:  # $label19
                                                                # br_table v14
                                                                break
                                                                break
                                                            v2 = ((v4 * 404) + ENTITY_TYPES)
                                                            if load32(((v4 * 404) + ENTITY_TYPES) + 264):
                                                                break
                                                            if (load32(v2 + 268) == 1):
                                                                break
                                                            if not load32(v2 + 92):
                                                                break
                                                            if (load32(38456) == v4):
                                                                break
                                                            if (load32(38764) != v4):
                                                                break
                                                            break
                                                            break
                                                        if (load32(((v4 * 404) + ENTITY_TYPES) + 264) == 1):
                                                            break
                                                        break
                                                        break
                                                    if load32(((v4 * 404) + ENTITY_TYPES) + 264):
                                                        break
                                                    break
                                                v11 = load32((((v10 + (v8 * 286704)) + 284636) + (v4 << 2)))
                                                if not load32((((v10 + (v8 * 286704)) + 284636) + (v4 << 2))):
                                                    break
                                                v5 = 0
                                                v17 = load32(v11 + 8)
                                                if not load32(v11 + 8):
                                                    break
                                                while True:  # $label27
                                                    while True:  # $label24
                                                        v2 = load32((load32(v11) + (v5 << 2)))
                                                        if not load32((load32(v11) + (v5 << 2))):
                                                            break
                                                        v2 = entities[v2]
                                                        if (call_table(arg1) == (load8u(arg0 + 45) != 0)):
                                                            break
                                                        v6 = (v6 + 1)
                                                        v3 = load32(9140300)
                                                        v12 = load32(v2 + 28)
                                                        while True:  # $label25
                                                            if (u32(load32(9684388)) >= u32(2)):
                                                                v2 = 0
                                                                if not v3:
                                                                    break
                                                                while True:  # $label26
                                                                    if (load32(((v2 << 2) + 8451904)) == v12):
                                                                        break
                                                                    v2 = (v2 + 1)
                                                                    if ((v2 + 1) != v3):
                                                                        continue
                                                                    break
                                                            v2 = v3
                                                            if (u32(v3) > u32(39999)):
                                                                break
                                                            break
                                                        store32(9140300, (v2 + 1))
                                                        store32(((v2 << 2) + 8451904), v12)
                                                        break
                                                    v5 = (v5 + 1)
                                                    if ((v5 + 1) != v17):
                                                        continue
                                                    break
                                                break
                                            v4 = (v4 + 1)
                                            if ((v4 + 1) != 255):
                                                continue
                                            break
                                            break
                                        raise Unreachable()
                                    v4 = load32((((v10 + (v8 * 286704)) + 284636) + v15))
                                    if not load32((((v10 + (v8 * 286704)) + 284636) + v15)):
                                        break
                                    v5 = 0
                                    v11 = load32(v4 + 8)
                                    if not load32(v4 + 8):
                                        break
                                    while True:  # $label34
                                        while True:  # $label31
                                            v2 = load32((load32(v4) + (v5 << 2)))
                                            if not load32((load32(v4) + (v5 << 2))):
                                                break
                                            v2 = entities[v2]
                                            if (call_table(arg1) == (load8u(arg0 + 45) != 0)):
                                                break
                                            v6 = (v6 + 1)
                                            v3 = load32(9140300)
                                            v10 = load32(v2 + 28)
                                            while True:  # $label32
                                                if (u32(load32(9684388)) >= u32(2)):
                                                    v2 = 0
                                                    if not v3:
                                                        break
                                                    while True:  # $label33
                                                        if (load32(((v2 << 2) + 8451904)) == v10):
                                                            break
                                                        v2 = (v2 + 1)
                                                        if ((v2 + 1) != v3):
                                                            continue
                                                        break
                                                v2 = v3
                                                if (u32(v3) > u32(39999)):
                                                    break
                                                break
                                            store32(9140300, (v2 + 1))
                                            store32(((v2 << 2) + 8451904), v10)
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != v11):
                                            continue
                                        break
                                    break
                                v2 = load32(arg0 + 12)
                                v5 = load32(arg0 + 16)
                                if load32(arg0 + 16):
                                    break
                                if (u32(v2) < u32(v6)):
                                    break
                                break
                                break
                            v2 = load32(arg0 + 12)
                            v5 = load32(arg0 + 16)
                            break
                        if not v5:
                            break
                        if (u32(v2) <= u32(v6)):
                            break
                        break
                    v7 = 1
                    store32((load32(9142420) + v9), 1)
                    v2 = load32(arg0 + 12)
                    v5 = load32(arg0 + 16)
                    break
                if not v5:
                    break
                if (u32(v2) > u32(v6)):
                    break
                store32(9140300, v16)
                break
            v8 = (v8 + 1)
            v2 = load32(PLAYER_COUNT)
            if (u32((v8 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
        break
    return (v7 & 1)

# ----------------------------------------------------------
# $func166
# ----------------------------------------------------------
def func166(arg0, arg1, arg2, arg3):
    while True:  # $label5
        v7 = load32(9142432)
        if load32(9142432):
            v10 = (arg1 << 1)
            v11 = (arg0 << 1)
            v12 = load32(9142440)
            v13 = load32((v7 + (((load32(9142440) * arg1) + arg0) << 2)))
            v14 = load32(ENTITIES)
            arg0 = 2147483647
            v16 = players[arg2]
            while True:  # $label4
                while True:  # $label0
                    v9 = ((v6 * 404) + ENTITY_TYPES)
                    arg1 = load32(((v6 * 404) + ENTITY_TYPES) + 192)
                    if ((arg3 != load32(((v6 * 404) + ENTITY_TYPES) + 192)) & (arg1 != 4)):
                        break
                    arg1 = load32(((v16 + (v6 << 2)) + 284636))
                    if not load32(((v16 + (v6 << 2)) + 284636)):
                        break
                    v17 = load32(arg1 + 8)
                    if not load32(arg1 + 8):
                        break
                    v18 = load32(arg1)
                    arg1 = 0
                    while True:  # $label3
                        while True:  # $label1
                            v4 = load32((v18 + (arg1 << 2)))
                            if not load32((v18 + (arg1 << 2))):
                                break
                            v5 = (v14 + (v4 * 132))
                            v19 = load16u((v14 + (v4 * 132)) + 114)
                            v4 = (v10 - (load32(v9 + 220) + (load16u((v14 + (v4 * 132)) + 114) << 1)))
                            v15 = load16u(v5 + 112)
                            v4 = (v11 - (load32(v9 + 216) + (load16u(v5 + 112) << 1)))
                            v4 = (((v10 - (load32(v9 + 220) + (load16u((v14 + (v4 * 132)) + 114) << 1))) * v4) + ((v11 - (load32(v9 + 216) + (load16u(v5 + 112) << 1))) * v4))
                            if ((((v10 - (load32(v9 + 220) + (load16u((v14 + (v4 * 132)) + 114) << 1))) * v4) + ((v11 - (load32(v9 + 216) + (load16u(v5 + 112) << 1))) * v4)) >= arg0):
                                break
                            v15 = ((load8u(v5 + 122) * 404) + ENTITY_TYPES)
                            if (load32((v7 + (((v15 + ((load32(((load8u(v5 + 122) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1)) + (v12 * (((load32(v15 + 220) & 0xFFFFFFFF) >> 1) + v19))) << 2))) != v13):
                                break
                            if (load16u(v5 + 110) != arg2):
                                break
                            while True:  # $label2
                                # br_table (load8u(v5 + 125) - 4)
                                break
                                break
                            v8 = load32(v5 + 28)
                            arg0 = v4
                            break
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != v17):
                            continue
                        break
                    break
                v6 = (v6 + 1)
                if ((v6 + 1) != 255):
                    continue
                break
            break
        v9 = (arg1 << 1)
        v10 = (arg0 << 1)
        v11 = load32(ENTITIES)
        arg0 = 2147483647
        v12 = players[arg2]
        while True:  # $label10
            while True:  # $label6
                v7 = ((v5 * 404) + ENTITY_TYPES)
                arg1 = load32(((v5 * 404) + ENTITY_TYPES) + 192)
                if ((arg3 != load32(((v5 * 404) + ENTITY_TYPES) + 192)) & (arg1 != 4)):
                    break
                arg1 = load32(((v12 + (v5 << 2)) + 284636))
                if not load32(((v12 + (v5 << 2)) + 284636)):
                    break
                v13 = load32(arg1 + 8)
                if not load32(arg1 + 8):
                    break
                v14 = load32(arg1)
                arg1 = 0
                while True:  # $label9
                    while True:  # $label7
                        v4 = load32((v14 + (arg1 << 2)))
                        if not load32((v14 + (arg1 << 2))):
                            break
                        v6 = (v11 + (v4 * 132))
                        v4 = (v9 - (load32(v7 + 220) + (load16u((v11 + (v4 * 132)) + 114) << 1)))
                        v4 = (v10 - (load32(v7 + 216) + (load16u(v6 + 112) << 1)))
                        v4 = (((v9 - (load32(v7 + 220) + (load16u((v11 + (v4 * 132)) + 114) << 1))) * v4) + ((v10 - (load32(v7 + 216) + (load16u(v6 + 112) << 1))) * v4))
                        if ((((v9 - (load32(v7 + 220) + (load16u((v11 + (v4 * 132)) + 114) << 1))) * v4) + ((v10 - (load32(v7 + 216) + (load16u(v6 + 112) << 1))) * v4)) >= arg0):
                            break
                        if (load16u(v6 + 110) != arg2):
                            break
                        while True:  # $label8
                            # br_table (load8u(v6 + 125) - 4)
                            break
                            break
                        v8 = load32(v6 + 28)
                        arg0 = v4
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v13):
                        continue
                    break
                break
            v5 = (v5 + 1)
            if ((v5 + 1) != 255):
                continue
            break
        break
    return v8

# ----------------------------------------------------------
# $func167
# ----------------------------------------------------------
def func167(arg0, arg1, arg2, arg3, arg4):
    v8 = load32(9142440)
    v20 = load32(arg1)
    v21 = load32(arg0)
    while True:  # $label8
        while True:  # $label2
            if not arg4:
                v11 = 1
                while True:  # $label7
                    arg4 = ((v7 << 1) | 1)
                    arg3 = (v21 - v7)
                    v12 = (((v7 << 1) | 1) + (v21 - v7))
                    v13 = ((((v7 << 1) | 1) + (v21 - v7)) - 1)
                    arg2 = (v20 - v7)
                    arg4 = (arg4 + (v20 - v7))
                    v14 = ((arg4 + (v20 - v7)) - 1)
                    v6 = arg3
                    while True:  # $label6
                        while True:  # $label0
                            if (u32(v6) >= u32(v8)):
                                break
                            v5 = arg2
                            while True:  # $label1
                                if (v6 != v13):
                                    if (arg3 != v6):
                                        break
                                while True:  # $label3
                                    if ((u32(v5) < u32(v8)) & ((v5 | v6) >= 0)):
                                        break
                                    v5 = (v5 + 1)
                                    if ((v5 + 1) < arg4):
                                        continue
                                    break
                                break
                                break
                            while True:  # $label5
                                while True:  # $label4
                                    if ((arg2 != v5) & (v5 != v14)):
                                        break
                                    if (u32(v5) >= u32(v8)):
                                        break
                                    if ((v5 | v6) >= 0):
                                        break
                                    break
                                v5 = (v5 + 1)
                                if ((v5 + 1) < arg4):
                                    continue
                                break
                            break
                        v6 = (v6 + 1)
                        if ((v6 + 1) < v12):
                            continue
                        break
                    v11 = (u32(v7) < u32(39))
                    v7 = (v7 + 1)
                    if ((v7 + 1) != 40):
                        continue
                    break
                break
            v22 = (arg4 & -2)
            v23 = (arg4 & 1)
            v15 = (v8 + 2)
            v24 = ((v8 + 2) * arg2)
            v16 = load32(9142840)
            v11 = 1
            while True:  # $label14
                arg2 = ((v9 << 1) | 1)
                v12 = (v21 - v9)
                v25 = (((v9 << 1) | 1) + (v21 - v9))
                v26 = ((((v9 << 1) | 1) + (v21 - v9)) - 1)
                v13 = (v20 - v9)
                v27 = (arg2 + (v20 - v9))
                v28 = ((arg2 + (v20 - v9)) - 1)
                v6 = v12
                while True:  # $label13
                    v14 = (v6 + 1)
                    if (u32(v6) < u32(v8)):
                        v29 = (v6 == v26)
                        v30 = (v6 == v12)
                        v5 = v13
                        while True:  # $label12
                            while True:  # $label9
                                if not (v29 | ((v30 | (v5 == v13)) | (v5 == v28))):
                                    break
                                if (u32(v5) >= u32(v8)):
                                    break
                                if ((v5 | v6) < 0):
                                    break
                                v10 = 1
                                v17 = ((v5 + v24) + 1)
                                v18 = 0
                                while True:  # $label11
                                    v19 = (v14 + v18)
                                    arg2 = 0
                                    v7 = 0
                                    if (arg4 != 1):
                                        while True:  # $label10
                                            v10 = (((load32((v16 + ((v19 + ((v17 + (arg2 | 1)) * v15)) << 2))) == arg3) & (load32((v16 + ((v19 + ((arg2 + v17) * v15)) << 2))) == arg3)) & v10)
                                            arg2 = (arg2 + 2)
                                            v7 = (v7 + 2)
                                            if ((v7 + 2) != v22):
                                                continue
                                            break
                                    if v23:
                                        v10 = ((load32((v16 + ((v19 + ((arg2 + v17) * v15)) << 2))) == arg3) & v10)
                                    v18 = (v18 + 1)
                                    if ((v18 + 1) != arg4):
                                        continue
                                    break
                                if v10:
                                    break
                                break
                            v5 = (v5 + 1)
                            if ((v5 + 1) < v27):
                                continue
                            break
                    v6 = v14
                    if (v14 < v25):
                        continue
                    break
                v11 = (u32(v9) < u32(39))
                v9 = (v9 + 1)
                if ((v9 + 1) != 40):
                    continue
                break
            break
            break
        store32(arg0, v6)
        store32(arg1, v5)
        break
    return v11

# ----------------------------------------------------------
# $func168
# ----------------------------------------------------------
def func168(arg0, arg1):
    while True:  # $label0
        if (arg1 >= 1024):
            arg0 = (arg0 * 8.98846567431158e+307)
            if (u32(arg1) < u32(2047)):
                arg1 = (arg1 - 1023)
                break
            arg0 = (arg0 * 8.98846567431158e+307)
            arg1 = ((3069 if (arg1 >= 3069) else arg1) - 2046)
            break
        if (arg1 > -1023):
            break
        arg0 = (arg0 * 2.004168360008973e-292)
        if (u32(arg1) > u32(-1992)):
            arg1 = (arg1 + 969)
            break
        arg0 = (arg0 * 2.004168360008973e-292)
        arg1 = ((-2960 if (arg1 <= -2960) else arg1) + 1938)
        break
    # TODO: f64.reinterpret_i64
    return (arg0 * (i32((arg1 + 1023)) << 52))

# ----------------------------------------------------------
# $func169
# ----------------------------------------------------------
def func169():
    v14 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v0 = load32(9140328)
    if load32(9140328):
        v5 = load32(9142440)
        while True:  # $label7
            v1 = load32(((v15 << 2) + 9140336))
            v17 = load32(load32(((v15 << 2) + 9140336)) + 44)
            if (u32(((v5 * load32(load32(((v15 << 2) + 9140336)) + 44)) * v5)) >= u32(65536)):
                v2 = load32(9147316)
                v0 = load32(9147320)
                v18 = 0
                v4 = load32(9147312)
                v3 = load32(9147324)
                while True:  # $label6
                    v10 = load32(v1 + 8)
                    v11 = load32(v1)
                    store32(9147320, v2)
                    store32(9147324, v0)
                    store32(9147316, v4)
                    v12 = load32(v1 + 12)
                    v13 = load32(v1 + 4)
                    v16 = load32(v1 + 20)
                    v8 = load32(v1 + 16)
                    store32(9147320, v4)
                    store32(9147324, v2)
                    v6 = ((v3 << 11) ^ v3)
                    v9 = (((((v4 & 0xFFFFFFFF) >> 19) ^ ((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v4) ^ v6)
                    store32(9147316, (((((v4 & 0xFFFFFFFF) >> 19) ^ ((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v4) ^ v6))
                    v0 = ((v0 << 11) ^ v0)
                    v6 = (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v9 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v9)
                    store32(9147312, (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v9 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v9))
                    v0 = (v5 << 5)
                    v8 = (v8 * v16)
                    v19 = (v6 % (v12 + ((v5 << 5) - (v13 // (v8 * v16)))))
                    v3 = (((v6 % (v12 + ((v5 << 5) - (v13 // (v8 * v16))))) - load32(v1 + 12)) // 32)
                    while True:  # $label3
                        v10 = (v9 % (v10 + (v0 - v11)))
                        v7 = (((v9 % (v10 + (v0 - v11))) - load32(v1 + 8)) // 32)
                        v0 = load32(v1)
                        v11 = ((v7 + (load32(v1) // 32)) + ((v0 & 31) != 0))
                        if ((((v9 % (v10 + (v0 - v11))) - load32(v1 + 8)) // 32) < ((v7 + (load32(v1) // 32)) + ((v0 & 31) != 0))):
                            v12 = 0
                            v0 = (load32(v1 + 4) // v8)
                            v0 = ((((load32(v1 + 4) // v8) // 32) + v3) + ((v0 & 31) != 0))
                            v16 = (v3 if (v0 < v3) else ((((load32(v1 + 4) // v8) // 32) + v3) + ((v0 & 31) != 0)))
                            v13 = (v5 + 2)
                            v8 = load32(9142840)
                            while True:  # $label2
                                v7 = (v7 + 1)
                                v0 = v3
                                while True:  # $label1
                                    while True:  # $label0
                                        if (v0 != v16):
                                            v0 = (v0 + 1)
                                            if (load32((v8 + (((((v0 + 1) + v13) * v13) + v7) << 2))) != 1):
                                                continue
                                            break
                                        break
                                    v12 = (v7 >= v11)
                                    if (v7 != v11):
                                        continue
                                    break
                                break
                            if not v12:
                                break
                        v0 = 0
                        v3 = load32(v1 + 52)
                        v6 = load32(9681936)
                        while True:  # $label4
                            if not (load8u(9568060) | load8u(9147152)):
                                break
                            if load8u(9142917):
                                break
                            while True:  # $label5
                                v2 = load32(9299880)
                                if load32(9299880):
                                    v2 = (v2 - 1)
                                    store32(9299880, (v2 - 1))
                                    v0 = load32((load32(9299872) + (v2 << 2)))
                                    break
                                v0 = load32(9163776)
                                v4 = (load32(9163776) + 1)
                                store32(9163776, (load32(9163776) + 1))
                                v2 = load32(9163784)
                                if (u32(v4) < u32(load32(9163784))):
                                    break
                                store32(v14, v2)
                                a_b()
                                store32(9163784, (load32(9163784) + 40000))
                                break
                            break
                        func216(v6, v3, v10, v19, v0)
                        v5 = load32(9142440)
                        v17 = load32(v1 + 44)
                        v9 = load32(9147316)
                        v4 = load32(9147320)
                        v6 = load32(9147312)
                        v2 = load32(9147324)
                        break
                    v3 = v2
                    v2 = v9
                    v0 = v4
                    v4 = v6
                    v18 = (v18 + 1)
                    if (u32((v18 + 1)) < u32(((((v5 * v17) * v5) & 0xFFFFFFFF) >> 16))):
                        continue
                    break
                v0 = load32(9140328)
            v15 = (v15 + 1)
            if (u32((v15 + 1)) < u32(v0)):
                continue
            break
    G.global0 = (v14 + 16)

# ----------------------------------------------------------
# $func170
# ----------------------------------------------------------
def func170(arg0):
    if load32(9142912):
        v3 = load32(9142908)
        v9 = load32(load32(9142908) + 60)
        v6 = load32(v3)
        v7 = (v6 + (load32(v3 + 4) * 60))
        if (u32(load32(v3)) < u32((v6 + (load32(v3 + 4) * 60)))):
            v4 = v7
            while True:  # $label6
                v8 = load32(9142908)
                v1 = (load32(9142908) + (v6 << 2))
                v10 = load32((load32(9142908) + (v6 << 2)))
                v2 = ((load32((load32(9142908) + (v6 << 2))) * 404) + ENTITY_TYPES)
                v3 = load32(v1 + 4)
                store32(((load32((load32(9142908) + (v6 << 2))) * 404) + ENTITY_TYPES) + 108, load32(v1 + 4))
                store32(v2 + 104, v3)
                store32(v2 + 92, load32(v1 + 8))
                store32(v2 + 100, load32(v1 + 12))
                store32(v2 + 68, load32(v1 + 16))
                store32(v2 + 72, load32(v1 + 20))
                store32(v2 + 76, load32(v1 + 24))
                store32(v2 + 80, load32(v1 + 28))
                v3 = load32(v1 + 32)
                store32(v2 + 128, load32(v1 + 32))
                store32(v2 + 120, v3)
                store32(v2 + 116, load32(v1 + 36))
                store32(v2 + 276, load32(v1 + 40))
                store32(v2 + 96, load32(v1 + 44))
                store32(v2 + 224, load32(v1 + 48))
                store32(v2 + 260, load32(v1 + 52))
                store32(v2 + 204, load32(v1 + 56))
                store32(v2 + 200, load32(v1 + 60))
                v5 = load32((v1 - -64))
                store32(v2 + 236, load32((v1 - -64)))
                store32(v2 + 228, load32(v1 + 68))
                store32(v2 + 208, load32(v1 + 72))
                v3 = load32(v1 + 76)
                store32(v2 + 216, load32(v1 + 76))
                v11 = (v6 + 20)
                while True:  # $label0
                    if (v3 == load32(v2 + 220)):
                        break
                    store32(v2 + 220, v3)
                    v3 = (v3 * v3)
                    v12 = func26((v3 * v3))
                    store32(v2 + 372, func26((v3 * v3)))
                    if not v3:
                        break
                    # TODO: memory.fill
                    break
                store32(v2 + 192, load32((v8 + (v11 << 2))))
                store32(v2 + 188, load32(v1 + 84))
                store32(v2 + 84, load32(v1 + 88))
                store32(v2 + 136, load32(v1 + 92))
                store32(v2 + 140, load32(v1 + 96))
                store32(v2 + 176, load32(v1 + 100))
                v3 = load32(v1 + 104)
                store32(v2 + 364, load32(v1 + 104))
                store32(v2 + 272, load32(v1 + 108))
                store32(v2 + 212, load32(v1 + 112))
                store32(v2 + 124, load32(v1 + 116))
                v8 = load32(v1 + 120)
                store32(v2 + 280, load32(v1 + 124))
                store32(v2 + 328, load32(v1 + 128))
                store8(v2 + 353, (load32(v1 + 132) != 0))
                store8(v2 + 335, (load32(v1 + 136) != 0))
                store8(v2 + 333, (load32(v1 + 140) != 0))
                store8(v2 + 334, (load32(v1 + 144) != 0))
                store8(v2 + 336, (load32(v1 + 148) != 0))
                store32(v2 + 284, load32(v1 + 152))
                store32(v2 + 288, load32(v1 + 156))
                store32(v2 + 292, load32(v1 + 160))
                store32(v2 + 296, load32(v1 + 164))
                store32(v2 + 300, load32(v1 + 168))
                store32(v2 + 308, load32(v1 + 172))
                store32(v2 + 312, load32(v1 + 176))
                store32(v2 + 324, load32(v1 + 180))
                store32(v2 + 320, load32(v1 + 184))
                store32(v2 + 340, load32(v1 + 188))
                store32(v2 + 344, load32(v1 + 192))
                store32(v2 + 348, load32(v1 + 196))
                store32(v2 + 304, load32(v1 + 200))
                store32(v2 + 316, load32(v1 + 204))
                store8(v2 + 352, (load32(v1 + 208) != 0))
                store8(v2 + 354, (load32(v1 + 212) != 0))
                if v5:
                    store32(v2 + 232, func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2))))
                if v3:
                    store32(v2 + 24, func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2))))
                if load32(v2 + 236):
                    v3 = load32(v2 + 232)
                    v1 = 0
                    v5 = load32(9142908)
                    while True:  # $label1
                        store32((v3 + (v1 << 2)), load32((v5 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v2 + 236))):
                            continue
                        break
                if load32(v2 + 364):
                    v3 = load32(v2 + 24)
                    v1 = 0
                    v5 = load32(9142908)
                    while True:  # $label2
                        store32((v3 + (v1 << 2)), load32((v5 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v2 + 364))):
                            continue
                        break
                v1 = 0
                while True:  # $label3
                    v2 = ((v10 * 1020) + 9299904)
                    v3 = (((v10 * 1020) + 9299904) + (v1 << 2))
                    store64((((v10 * 1020) + 9299904) + (v1 << 2)), 429496729700)
                    store32(v3 + 16, 100)
                    store64(v3 + 8, 429496729700)
                    v1 = (v1 + 5)
                    if ((v1 + 5) != 255):
                        continue
                    break
                while True:  # $label4
                    if not v8:
                        break
                    v1 = ((((v8 - 1) & 0xFFFFFFFF) >> 1) + 1)
                    v10 = (((((v8 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                    v5 = load32(9142908)
                    if (u32(v8) >= u32(3)):
                        v8 = (v1 & -2)
                        v3 = 0
                        while True:  # $label5
                            v1 = (v5 + (v4 << 2))
                            store32((v2 + (load32((v5 + (v4 << 2))) << 2)), load32(v1 + 4))
                            store32((v2 + (load32(v1 + 8) << 2)), load32(v1 + 12))
                            v4 = (v4 + 4)
                            v3 = (v3 + 2)
                            if ((v3 + 2) != v8):
                                continue
                            break
                    if not v10:
                        break
                    v1 = (v5 + (v4 << 2))
                    store32((v2 + (load32((v5 + (v4 << 2))) << 2)), load32(v1 + 4))
                    v4 = (v4 + 2)
                    break
                v6 = (v6 + 60)
                if (u32((v6 + 60)) < u32(v7)):
                    continue
                break
            v3 = load32(9142908)
        v6 = load32(v3 + 8)
        v7 = (v6 + (load32(v3 + 12) * 55))
        if (u32(load32(v3 + 8)) < u32((v6 + (load32(v3 + 12) * 55)))):
            v11 = (u32(v9) < u32(623))
            v12 = (u32(v9) > u32(622))
            v4 = v7
            while True:  # $label16
                v1 = (load32(9142908) + (v6 << 2))
                v13 = load32((load32(9142908) + (v6 << 2)))
                v2 = ((load32((load32(9142908) + (v6 << 2))) * 404) + ENTITY_TYPES)
                v3 = load32(v1 + 4)
                store32(((load32((load32(9142908) + (v6 << 2))) * 404) + ENTITY_TYPES) + 108, load32(v1 + 4))
                store32(v2 + 104, v3)
                store32(v2 + 68, load32(v1 + 8))
                store32(v2 + 72, load32(v1 + 12))
                store32(v2 + 76, load32(v1 + 16))
                store32(v2 + 80, load32(v1 + 20))
                store32(v2 + 116, load32(v1 + 24))
                v3 = load32(v1 + 28)
                store32(v2 + 236, load32(v1 + 28))
                store32(v2 + 92, load32(v1 + 32))
                store32(v2 + 276, load32(v1 + 36))
                store32(v2 + 96, load32(v1 + 40))
                store32(v2 + 224, load32(v1 + 44))
                store32(v2 + 204, load32(v1 + 48))
                store32(v2 + 200, load32(v1 + 52))
                store32(v2 + 228, load32(v1 + 56))
                store32(v2 + 208, load32(v1 + 60))
                v9 = load32((v1 - -64))
                store32(v2 + 216, load32((v1 - -64)))
                v10 = load32(v1 + 68)
                store32(v2 + 220, load32(v1 + 68))
                store32(v2 + 192, load32(v1 + 76))
                store32(v2 + 188, load32(v1 + 80))
                store32(v2 + 84, load32(v1 + 84))
                store32(v2 + 136, load32(v1 + 88))
                store32(v2 + 140, load32(v1 + 92))
                store32(v2 + 176, load32(v1 + 96))
                store32(v2 + 112, load32(v1 + 100))
                v5 = load32(v1 + 104)
                store32(v2 + 364, load32(v1 + 104))
                store32(v2 + 272, load32(v1 + 108))
                store32(v2 + 212, load32(v1 + 112))
                v8 = load32(v1 + 116)
                store32(v2 + 280, load32(v1 + 120))
                store32(v2 + 328, load32(v1 + 124))
                store8(v2 + 332, (load32(v1 + 128) != 0))
                store8(v2 + 353, (load32(v1 + 132) != 0))
                store8(v2 + 335, (load32(v1 + 136) != 0))
                store8(v2 + 336, (load32(v1 + 140) != 0))
                store32(v2 + 284, load32(v1 + 144))
                store32(v2 + 288, load32(v1 + 148))
                store32(v2 + 292, load32(v1 + 152))
                store32(v2 + 296, load32(v1 + 156))
                store32(v2 + 300, load32(v1 + 160))
                store32(v2 + 308, load32(v1 + 164))
                store32(v2 + 312, load32(v1 + 168))
                store32(v2 + 324, load32(v1 + 172))
                store32(v2 + 320, load32(v1 + 176))
                store32(v2 + 340, load32(v1 + 180))
                store32(v2 + 344, load32(v1 + 184))
                store8(v2 + 354, (load32(v1 + 188) != 0))
                if not v11:
                    store32(v2 + 244, load32(v1 + 192))
                if v3:
                    store32(v2 + 232, func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2))))
                v3 = func26((v9 * v10))
                store32(v2 + 372, func26((v9 * v10)))
                if v5:
                    store32(v2 + 24, func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2))))
                if load32(v2 + 236):
                    v5 = load32(v2 + 232)
                    v1 = 0
                    v9 = load32(9142908)
                    while True:  # $label7
                        store32((v5 + (v1 << 2)), load32((v9 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v2 + 236))):
                            continue
                        break
                while True:  # $label8
                    v5 = (load32(v2 + 220) * load32(v2 + 216))
                    if not (load32(v2 + 220) * load32(v2 + 216)):
                        break
                    v1 = 0
                    v9 = load32(9142908)
                    if (v5 != 1):
                        v14 = (v5 & -2)
                        v10 = 0
                        while True:  # $label9
                            v15 = (v9 + (v4 << 2))
                            store8((v1 + v3), (load32((v9 + (v4 << 2))) != 0))
                            store8((v3 + (v1 | 1)), (load32(v15 + 4) != 0))
                            v1 = (v1 + 2)
                            v4 = (v4 + 2)
                            v10 = (v10 + 2)
                            if ((v10 + 2) != v14):
                                continue
                            break
                    if not (v5 & 1):
                        break
                    store8((v1 + v3), (load32((v9 + (v4 << 2))) != 0))
                    v4 = (v4 + 1)
                    break
                if load32(v2 + 364):
                    v3 = load32(v2 + 24)
                    v1 = 0
                    v5 = load32(9142908)
                    while True:  # $label10
                        store32((v3 + (v1 << 2)), load32((v5 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v2 + 364))):
                            continue
                        break
                v1 = 0
                while True:  # $label11
                    v5 = ((v13 * 1020) + 9299904)
                    v3 = (((v13 * 1020) + 9299904) + (v1 << 2))
                    store64((((v13 * 1020) + 9299904) + (v1 << 2)), 429496729700)
                    store32(v3 + 16, 100)
                    store64(v3 + 8, 429496729700)
                    v1 = (v1 + 5)
                    if ((v1 + 5) != 255):
                        continue
                    break
                while True:  # $label12
                    if not v8:
                        break
                    v1 = ((((v8 - 1) & 0xFFFFFFFF) >> 1) + 1)
                    v10 = (((((v8 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                    v9 = load32(9142908)
                    if (u32(v8) >= u32(3)):
                        v8 = (v1 & -2)
                        v3 = 0
                        while True:  # $label13
                            v1 = (v9 + (v4 << 2))
                            store32((v5 + (load32((v9 + (v4 << 2))) << 2)), load32(v1 + 4))
                            store32((v5 + (load32(v1 + 8) << 2)), load32(v1 + 12))
                            v4 = (v4 + 4)
                            v3 = (v3 + 2)
                            if ((v3 + 2) != v8):
                                continue
                            break
                    if not v10:
                        break
                    v1 = (v9 + (v4 << 2))
                    store32((v5 + (load32((v9 + (v4 << 2))) << 2)), load32(v1 + 4))
                    v4 = (v4 + 2)
                    break
                while True:  # $label14
                    if not v12:
                        break
                    v1 = load32(v2 + 244)
                    if not load32(v2 + 244):
                        break
                    v3 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                    store32(v2 + 240, func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2))))
                    v2 = load32(v2 + 244)
                    v1 = 0
                    v5 = load32(9142908)
                    while True:  # $label15
                        store32((v3 + (v1 << 2)), load32((v5 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(v2)):
                            continue
                        break
                    break
                v6 = (v6 + 55)
                if (u32((v6 + 55)) < u32(v7)):
                    continue
                break
            v3 = load32(9142908)
        v6 = load32(v3 + 16)
        v7 = (v6 + (load32(v3 + 20) * 23))
        if (u32(load32(v3 + 16)) < u32((v6 + (load32(v3 + 20) * 23)))):
            v4 = v7
            while True:  # $label19
                v1 = (v3 + (v6 << 2))
                v2 = ((load32((v3 + (v6 << 2))) * 404) + ENTITY_TYPES)
                v5 = load32(v1 + 4)
                if (u32(load32(v1 + 4)) <= u32(4)):
                else:
                store32(load32(((v5 << 2) + 10164)) + 368, 0)
                store32(v2 + 68, load32((v3 + ((v6 + 2) << 2))))
                store32(v2 + 116, load32(v1 + 12))
                v8 = load32(v1 + 16)
                store32(v2 + 244, load32(v1 + 16))
                store32(v2 + 72, load32(v1 + 20))
                store32(v2 + 76, load32(v1 + 24))
                store32(v2 + 80, load32(v1 + 28))
                v5 = load32(v1 + 32)
                store32(v2 + 236, load32(v1 + 32))
                store8(v2 + 354, (load32(v1 + 36) != 0))
                store32(v2 + 212, load32(v1 + 40))
                store32(v2 + 104, load32(v1 + 44))
                store32(v2 + 92, load32(v1 + 48))
                store32(v2 + 100, load32(v1 + 52))
                store32(v2 + 120, load32(v1 + 56))
                store32(v2 + 112, load32(v1 + 60))
                if v5:
                    store32(v2 + 232, func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2))))
                if v8:
                    v5 = func26((-1 if (u32(v8) > u32(1073741823)) else (v8 << 2)))
                    store32(v2 + 240, func26((-1 if (u32(v8) > u32(1073741823)) else (v8 << 2))))
                    v8 = load32(v2 + 244)
                    v1 = 0
                    while True:  # $label17
                        store32((v5 + (v1 << 2)), load32((v3 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(v8)):
                            continue
                        break
                else:
                if v5:
                    v5 = load32(v2 + 232)
                    v1 = 0
                    while True:  # $label18
                        store32((v5 + (v1 << 2)), load32((v3 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u32((v1 + 1)) < u32(load32(v2 + 236))):
                            continue
                        break
                v6 = (v6 + 23)
                if (u32((v6 + 23)) < u32(v7)):
                    continue
                break
        v4 = (v3 + (load32(v3 + 24) << 2))
        v3 = 0
        while True:  # $label20
            v7 = (v3 << 2)
            store32(((v3 << 2) + 9561072), load32((v4 + v7)))
            v2 = (v7 + 4)
            store32(((v7 + 4) + 9561072), load32((v2 + v4)))
            v2 = (v7 + 8)
            store32(((v7 + 8) + 9561072), load32((v2 + v4)))
            v2 = (v7 + 12)
            store32(((v7 + 12) + 9561072), load32((v2 + v4)))
            v7 = (v7 + 16)
            store32(((v7 + 16) + 9561072), load32((v4 + v7)))
            v3 = (v3 + 5)
            if ((v3 + 5) != 155):
                continue
            break
        while True:  # $label21
            if load8u(9147152):
                break
            if ((arg0 ^ 1) & (load8u(9147212) != 0)):
                break
            if not load32(PLAYER_COUNT):
                break
            v2 = load32(PLAYERS)
            v6 = 0
            while True:  # $label23
                v3 = 0
                while True:  # $label22
                    v7 = (v2 + (v6 * 286704))
                    v4 = ((v2 + (v6 * 286704)) + 283984)
                    arg0 = (v3 << 2)
                    store32((((v2 + (v6 * 286704)) + 283984) + (v3 << 2)), load32((arg0 + 9561072)))
                    v1 = (arg0 + 4)
                    store32((v4 + (arg0 + 4)), load32((v1 + 9561072)))
                    v1 = (arg0 + 8)
                    store32((v4 + (arg0 + 8)), load32((v1 + 9561072)))
                    v1 = (arg0 + 12)
                    store32((v4 + (arg0 + 12)), load32((v1 + 9561072)))
                    arg0 = (arg0 + 16)
                    store32((v4 + (arg0 + 16)), load32((arg0 + 9561072)))
                    v3 = (v3 + 5)
                    if ((v3 + 5) != 155):
                        continue
                    break
                store32(v7 + 283868, load32((v7 + 284372)))
                v6 = (v6 + 1)
                if (u32((v6 + 1)) < u32(load32(PLAYER_COUNT))):
                    continue
                break
            break
    return func164()

# ----------------------------------------------------------
# $md
# Export: md
# ----------------------------------------------------------
def md(arg0):
    """Export: md"""
    v2 = load32(9142440)
    v1 = (load32(9142440) * v2)
    while True:  # $label8
        while True:  # $label0
            while True:  # $label1
                while True:  # $label2
                    while True:  # $label3
                        while True:  # $label4
                            while True:  # $label5
                                while True:  # $label6
                                    while True:  # $label7
                                        # br_table ((arg0 - 1) if arg0 else load32(load32(GAME_STATE) + 28))
                                        break
                                        break
                                    while True:  # $label9
                                        if not v1:
                                            break
                                        v2 = 0
                                        arg0 = 0
                                        if (u32((v1 - 1)) >= u32(3)):
                                            v4 = (v1 & -4)
                                            while True:  # $label10
                                                store8((load32(9147288) + arg0), load32(9147292))
                                                store8((load32(9147288) + (arg0 | 1)), load32(9147292))
                                                store8((load32(9147288) + (arg0 | 2)), load32(9147292))
                                                store8((load32(9147288) + (arg0 | 3)), load32(9147292))
                                                arg0 = (arg0 + 4)
                                                v3 = (v3 + 4)
                                                if ((v3 + 4) != v4):
                                                    continue
                                                break
                                        v1 = (v1 & 3)
                                        if not (v1 & 3):
                                            break
                                        while True:  # $label11
                                            store8((load32(9147288) + arg0), load32(9147292))
                                            arg0 = (arg0 + 1)
                                            v2 = (v2 + 1)
                                            if ((v2 + 1) != v1):
                                                continue
                                            break
                                        break
                                    v2 = 0
                                    if load32(9147300):
                                        while True:  # $label12
                                            arg0 = load32(9684504)
                                            v1 = (v2 << 2)
                                            v2 = (v2 + 8)
                                            if (u32((v2 + 8)) < u32(load32(9147300))):
                                                continue
                                            break
                                    break
                                    break
                                while True:  # $label13
                                    if not v1:
                                        break
                                    v2 = 0
                                    arg0 = 0
                                    if (u32((v1 - 1)) >= u32(3)):
                                        v4 = (v1 & -4)
                                        while True:  # $label14
                                            store8((load32(9147288) + arg0), load32(9147292))
                                            store8((load32(9147288) + (arg0 | 1)), load32(9147292))
                                            store8((load32(9147288) + (arg0 | 2)), load32(9147292))
                                            store8((load32(9147288) + (arg0 | 3)), load32(9147292))
                                            arg0 = (arg0 + 4)
                                            v3 = (v3 + 4)
                                            if ((v3 + 4) != v4):
                                                continue
                                            break
                                    v1 = (v1 & 3)
                                    if not (v1 & 3):
                                        break
                                    while True:  # $label15
                                        store8((load32(9147288) + arg0), load32(9147292))
                                        arg0 = (arg0 + 1)
                                        v2 = (v2 + 1)
                                        if ((v2 + 1) != v1):
                                            continue
                                        break
                                    break
                                v2 = 0
                                if load32(9147300):
                                    while True:  # $label16
                                        arg0 = load32(9684504)
                                        v1 = (v2 << 2)
                                        v2 = (v2 + 8)
                                        if (u32((v2 + 8)) < u32(load32(9147300))):
                                            continue
                                        break
                                break
                                break
                            while True:  # $label17
                                if not v1:
                                    break
                                v2 = 0
                                arg0 = 0
                                if (u32((v1 - 1)) >= u32(3)):
                                    v4 = (v1 & -4)
                                    while True:  # $label18
                                        store8((load32(9147288) + arg0), load32(9147292))
                                        store8((load32(9147288) + (arg0 | 1)), load32(9147292))
                                        store8((load32(9147288) + (arg0 | 2)), load32(9147292))
                                        store8((load32(9147288) + (arg0 | 3)), load32(9147292))
                                        arg0 = (arg0 + 4)
                                        v3 = (v3 + 4)
                                        if ((v3 + 4) != v4):
                                            continue
                                        break
                                v1 = (v1 & 3)
                                if not (v1 & 3):
                                    break
                                while True:  # $label19
                                    store8((load32(9147288) + arg0), load32(9147292))
                                    arg0 = (arg0 + 1)
                                    v2 = (v2 + 1)
                                    if ((v2 + 1) != v1):
                                        continue
                                    break
                                break
                            v2 = 0
                            if load32(9147300):
                                while True:  # $label20
                                    arg0 = load32(9684504)
                                    v1 = (v2 << 2)
                                    v2 = (v2 + 8)
                                    if (u32((v2 + 8)) < u32(load32(9147300))):
                                        continue
                                    break
                            break
                            break
                        while True:  # $label21
                            if not v1:
                                break
                            v2 = 0
                            arg0 = 0
                            if (u32((v1 - 1)) >= u32(3)):
                                v4 = (v1 & -4)
                                while True:  # $label22
                                    store8((load32(9147288) + arg0), load32(9147296))
                                    store8((load32(9147288) + (arg0 | 1)), load32(9147296))
                                    store8((load32(9147288) + (arg0 | 2)), load32(9147296))
                                    store8((load32(9147288) + (arg0 | 3)), load32(9147296))
                                    arg0 = (arg0 + 4)
                                    v3 = (v3 + 4)
                                    if ((v3 + 4) != v4):
                                        continue
                                    break
                            v1 = (v1 & 3)
                            if not (v1 & 3):
                                break
                            while True:  # $label23
                                store8((load32(9147288) + arg0), load32(9147296))
                                arg0 = (arg0 + 1)
                                v2 = (v2 + 1)
                                if ((v2 + 1) != v1):
                                    continue
                                break
                            break
                        v2 = 0
                        if not load32(9147300):
                            break
                        while True:  # $label24
                            arg0 = load32(9684504)
                            v1 = (v2 << 2)
                            v2 = (v2 + 8)
                            if (u32((v2 + 8)) < u32(load32(9147300))):
                                continue
                            break
                        break
                        break
                    while True:  # $label25
                        if not v1:
                            break
                        v2 = 0
                        arg0 = 0
                        if (u32((v1 - 1)) >= u32(3)):
                            v4 = (v1 & -4)
                            while True:  # $label26
                                store8((load32(9147288) + arg0), load32(9147296))
                                store8((load32(9147288) + (arg0 | 1)), load32(9147296))
                                store8((load32(9147288) + (arg0 | 2)), load32(9147296))
                                store8((load32(9147288) + (arg0 | 3)), load32(9147296))
                                arg0 = (arg0 + 4)
                                v3 = (v3 + 4)
                                if ((v3 + 4) != v4):
                                    continue
                                break
                        v1 = (v1 & 3)
                        if not (v1 & 3):
                            break
                        while True:  # $label27
                            store8((load32(9147288) + arg0), load32(9147296))
                            arg0 = (arg0 + 1)
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v1):
                                continue
                            break
                        break
                    v2 = 0
                    if load32(9147300):
                        while True:  # $label28
                            arg0 = load32(9684504)
                            v1 = (v2 << 2)
                            v2 = (v2 + 8)
                            if (u32((v2 + 8)) < u32(load32(9147300))):
                                continue
                            break
                    break
                    break
                while True:  # $label29
                    if not v1:
                        break
                    v2 = 0
                    arg0 = 0
                    if (u32((v1 - 1)) >= u32(3)):
                        v4 = (v1 & -4)
                        while True:  # $label30
                            store8((load32(9147288) + arg0), load32(9147292))
                            store8((load32(9147288) + (arg0 | 1)), load32(9147292))
                            store8((load32(9147288) + (arg0 | 2)), load32(9147292))
                            store8((load32(9147288) + (arg0 | 3)), load32(9147292))
                            arg0 = (arg0 + 4)
                            v3 = (v3 + 4)
                            if ((v3 + 4) != v4):
                                continue
                            break
                    v1 = (v1 & 3)
                    if not (v1 & 3):
                        break
                    while True:  # $label31
                        store8((load32(9147288) + arg0), load32(9147292))
                        arg0 = (arg0 + 1)
                        v2 = (v2 + 1)
                        if ((v2 + 1) != v1):
                            continue
                        break
                    break
                v2 = 0
                if load32(9147300):
                    while True:  # $label32
                        arg0 = load32(9684504)
                        v1 = (v2 << 2)
                        v2 = (v2 + 8)
                        if (u32((v2 + 8)) < u32(load32(9147300))):
                            continue
                        break
                break
                break
            while True:  # $label33
                if not v1:
                    break
                v2 = 0
                arg0 = 0
                if (u32((v1 - 1)) >= u32(3)):
                    v4 = (v1 & -4)
                    while True:  # $label34
                        store8((load32(9147288) + arg0), load32(9147292))
                        store8((load32(9147288) + (arg0 | 1)), load32(9147292))
                        store8((load32(9147288) + (arg0 | 2)), load32(9147292))
                        store8((load32(9147288) + (arg0 | 3)), load32(9147292))
                        arg0 = (arg0 + 4)
                        v3 = (v3 + 4)
                        if ((v3 + 4) != v4):
                            continue
                        break
                v1 = (v1 & 3)
                if not (v1 & 3):
                    break
                while True:  # $label35
                    store8((load32(9147288) + arg0), load32(9147292))
                    arg0 = (arg0 + 1)
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v1):
                        continue
                    break
                break
            v2 = 0
            if load32(9147300):
                while True:  # $label36
                    arg0 = load32(9684504)
                    v1 = (v2 << 2)
                    v2 = (v2 + 8)
                    if (u32((v2 + 8)) < u32(load32(9147300))):
                        continue
                    break
            break
            break
        while True:  # $label37
            if not v1:
                break
            v2 = 0
            arg0 = 0
            if (u32((v1 - 1)) >= u32(3)):
                v4 = (v1 & -4)
                while True:  # $label38
                    store8((load32(9147288) + arg0), load32(9147292))
                    store8((load32(9147288) + (arg0 | 1)), load32(9147292))
                    store8((load32(9147288) + (arg0 | 2)), load32(9147292))
                    store8((load32(9147288) + (arg0 | 3)), load32(9147292))
                    arg0 = (arg0 + 4)
                    v3 = (v3 + 4)
                    if ((v3 + 4) != v4):
                        continue
                    break
            v1 = (v1 & 3)
            if not (v1 & 3):
                break
            while True:  # $label39
                store8((load32(9147288) + arg0), load32(9147292))
                arg0 = (arg0 + 1)
                v2 = (v2 + 1)
                if ((v2 + 1) != v1):
                    continue
                break
            break
        v2 = 0
        if not load32(9147300):
            break
        while True:  # $label40
            arg0 = load32(9684504)
            v1 = (v2 << 2)
            v2 = (v2 + 8)
            if (u32((v2 + 8)) < u32(load32(9147300))):
                continue
            break
        break
    while True:  # $label41
        if not load32(load32(GAME_STATE) + 64):
            break
        v1 = load32(9142440)
        if (load32(9142440) <= 0):
            break
        v8 = (v1 & -2)
        v9 = (v1 & 1)
        v3 = ((v1 & 0xFFFFFFFF) >> 1)
        arg0 = (((v1 & 0xFFFFFFFF) >> 1) - 20)
        v4 = ((((v1 & 0xFFFFFFFF) >> 1) - 20) * arg0)
        v2 = 0
        while True:  # $label44
            arg0 = (v2 - v3)
            v6 = (((v2 - v3) * arg0) - 1)
            arg0 = 0
            v5 = 0
            if (v1 != 1):
                while True:  # $label42
                    v7 = (arg0 - v3)
                    if (v4 < (v6 + ((arg0 - v3) * v7))):
                        store8((load32(9147288) + ((load32(9142440) * arg0) + v2)), load32(9147296))
                    v7 = (arg0 | 1)
                    v10 = ((arg0 | 1) - v3)
                    if (v4 < (v6 + (((arg0 | 1) - v3) * v10))):
                        store8((load32(9147288) + ((load32(9142440) * v7) + v2)), load32(9147296))
                    arg0 = (arg0 + 2)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v8):
                        continue
                    break
            while True:  # $label43
                if not v9:
                    break
                v5 = (arg0 - v3)
                if ((v6 + ((arg0 - v3) * v5)) <= v4):
                    break
                store8((load32(9147288) + ((load32(9142440) * arg0) + v2)), load32(9147296))
                break
            v2 = (v2 + 1)
            if ((v2 + 1) != v1):
                continue
            break
        break
    return load32(9147288)

# ----------------------------------------------------------
# $func172
# ----------------------------------------------------------
def func172(arg0):
    v1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    if arg0:
        store32(9143000, 0)
    arg0 = 0
    a_b()
    store32(9671120, 0)
    while True:  # $label0
        v2 = load32(9147120)
        if not load32(9147120):
            break
        while True:  # $label1
            v2 = ((load32(9143000) * v2) + arg0)
            if (u32(((load32(9143000) * v2) + arg0)) >= u32(load32(9681836))):
                break
            store32(9671120, (load32(9671120) + 1))
            v2 = load32(((load8u(entities[load32((load32(9681828) + (v2 << 2)))].sub_state) * 404) + ENTITY_TYPES) + 144)
            store64(v1 + 32, 1)
            store64(v1 + 40, 0)
            store64(v1 + 48, 0)
            store64(v1 + 56, 4294967295)
            store64(v1 + 24, 1)
            store32(v1 + 20, (0 - v2))
            store32(v1 + 16, arg0)
            a_b()
            arg0 = (arg0 + 1)
            v2 = load32(9147120)
            if (u32((arg0 + 1)) < u32(load32(9147120))):
                continue
            break
        break
    store32(v1, load32(9143000))
    store32(v1 + 4, load32(9681836))
    a_b()
    G.global0 = (v1 - -64)

# ----------------------------------------------------------
# $func174
# ----------------------------------------------------------
def func174(arg0, arg1, arg2):
    v3 = load32(arg0)
    if (load32(arg0) == -1):
        v12 = 2
        v13 = load32(arg0 + 4)
        v3 = load32(arg0 + 8)
    v4 = load32(9142440)
    v5 = (load32(9142440) - 1)
    v6 = (v12 << 2)
    v16 = load32((arg0 + ((v12 << 2) | 4)))
    v17 = (u32(load32((arg0 + ((v12 << 2) | 4)))) < u32(v4))
    v6 = (arg0 + v6)
    v18 = load32((arg0 + v6) + 8)
    v21 = load32(9671136)
    v11 = (u32(load32((arg0 + v6) + 8)) > u32(load32(9671136)))
    v7 = (v12 | 5)
    v10 = load32(v6 + 12)
    if (load32(v6 + 12) == 69):
        store32((arg0 + (v7 << 2)), 1)
    v16 = (v16 if v17 else v5)
    v17 = (v3 if (u32(v3) < u32(v4)) else v5)
    v19 = load32(v6 + 16)
    v20 = load32((arg0 + (v7 << 2)))
    v3 = ((v11 | (load32((arg0 + (v7 << 2))) != 0)) & (v10 != 40))
    v8 = (5 if ((v11 | (load32((arg0 + (v7 << 2))) != 0)) & (v10 != 40)) else 0)
    v9 = load32(v6 + 24)
    if arg2:
        v14 = (1 if v3 else (1 if v11 else v13))
        v22 = (-1 if (u32(v14) > u32(1073741823)) else ((1 if v3 else (1 if v11 else v13)) << 2))
        v6 = (v14 * 7)
        v23 = (1 if (u32(v6) <= u32(1)) else (v14 * 7))
        v24 = (2 if v11 else 1)
        v13 = 0
        while True:  # $label16
            while True:  # $label0
                v7 = entities[load32((arg1 + (v13 << 2)))]
                if (load32(((load8u(entities[load32((arg1 + (v13 << 2)))].sub_state) * 404) + ENTITY_TYPES) + 264) == 1):
                    break
                while True:  # $label1
                    if (u32(v18) <= u32(v21)):
                        break
                    if (v17 != load16u(v7 + 112)):
                        break
                    if (v16 == load16u(v7 + 114)):
                        break
                    break
                if (load32((load32(9215884) + (load32(v7 + 44) << 4)) + 4) == 20):
                    break
                if ((load8u(v7 + 125) & -2) == 12):
                    break
                v3 = load32(v7 + 20)
                while True:  # $label15
                    if v14:
                        while True:  # $label4
                            while True:  # $label3
                                while True:  # $label2
                                    if not v3:
                                        v3 = func26(16)
                                        store32(func26(16) + 4, v14)
                                        v6 = func26(v22)
                                        store32(v3 + 12, 1)
                                        store32(v3, v6)
                                        store32(v7 + 20, v3)
                                        store32(v3 + 8, 0)
                                        v6 = (v3 + 8)
                                        break
                                    store32(v3 + 8, 0)
                                    v6 = (v3 + 8)
                                    if not load32(v3 + 4):
                                        break
                                    break
                                v5 = load32(v3)
                                v4 = 0
                                break
                                break
                            v5 = load32(v3 + 12)
                            store32(v3 + 4, load32(v3 + 12))
                            v4 = load32(v3)
                            v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                            if v4:
                            else:
                            v4 = 0
                            store32(v3, v5)
                            v3 = load32(v7 + 20)
                            break
                        store32(v6, (v4 + 1))
                        store32((v5 + (v4 << 2)), v24)
                        while True:  # $label5
                            v4 = load32(v3 + 8)
                            if (load32(v3 + 8) != load32(v3 + 4)):
                                v5 = load32(v3)
                                break
                            v5 = (load32(v3 + 12) + v4)
                            store32(v3 + 4, (load32(v3 + 12) + v4))
                            v6 = load32(v3)
                            v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                            if v4:
                                # TODO: memory.copy
                            if v6:
                                v4 = load32(v3 + 8)
                            store32(v3, v5)
                            break
                        store32(v3 + 8, (v4 + 1))
                        store32((v5 + (v4 << 2)), 2)
                        v5 = 0
                        while True:  # $label7
                            v25 = load32((arg0 + ((v5 + v12) << 2)))
                            while True:  # $label6
                                v4 = load32(v7 + 20)
                                v3 = load32(load32(v7 + 20) + 8)
                                if (load32(load32(v7 + 20) + 8) != load32(v4 + 4)):
                                    v6 = load32(v4)
                                    break
                                v6 = (load32(v4 + 12) + v3)
                                store32(v4 + 4, (load32(v4 + 12) + v3))
                                v15 = load32(v4)
                                v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
                                if v3:
                                    # TODO: memory.copy
                                if v15:
                                    v3 = load32(v4 + 8)
                                store32(v4, v6)
                                break
                            store32(v4 + 8, (v3 + 1))
                            store32((v6 + (v3 << 2)), v25)
                            v5 = (v5 + 1)
                            if ((v5 + 1) != v23):
                                continue
                            break
                        v4 = load32(v7 + 20)
                        v3 = load32(load32(v7 + 20))
                        store32(load32(load32(v7 + 20)) + 28, v8)
                        if not v11:
                            break
                        store32(v3 + 16, 0)
                        v15 = load16u(v7 + 112)
                        while True:  # $label8
                            v5 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v6 = v3
                                break
                            v6 = (load32(v4 + 12) + v5)
                            store32(v4 + 4, (load32(v4 + 12) + v5))
                            v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy
                            store32(v4, v6)
                            v5 = load32(v4 + 8)
                            break
                        v3 = load32(v7 + 20)
                        store32(v4 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), v15)
                        v15 = load16u(v7 + 114)
                        while True:  # $label9
                            v5 = load32(v3 + 8)
                            if (load32(v3 + 8) != load32(v3 + 4)):
                                v6 = load32(v3)
                                break
                            v6 = (load32(v3 + 12) + v5)
                            store32(v3 + 4, (load32(v3 + 12) + v5))
                            v4 = load32(v3)
                            v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy
                            if v4:
                                v5 = load32(v3 + 8)
                            store32(v3, v6)
                            break
                        v4 = load32(v7 + 20)
                        store32(v3 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), v15)
                        while True:  # $label10
                            v5 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v6 = load32(v4)
                                break
                            v6 = (load32(v4 + 12) + v5)
                            store32(v4 + 4, (load32(v4 + 12) + v5))
                            v3 = load32(v4)
                            v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy
                            if v3:
                                v5 = load32(v4 + 8)
                            store32(v4, v6)
                            break
                        v3 = load32(v7 + 20)
                        store32(v4 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), 0)
                        while True:  # $label11
                            v5 = load32(v3 + 8)
                            if (load32(v3 + 8) != load32(v3 + 4)):
                                v6 = load32(v3)
                                break
                            v6 = (load32(v3 + 12) + v5)
                            store32(v3 + 4, (load32(v3 + 12) + v5))
                            v4 = load32(v3)
                            v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy
                            if v4:
                                v5 = load32(v3 + 8)
                            store32(v3, v6)
                            break
                        v4 = load32(v7 + 20)
                        store32(v3 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), 0)
                        while True:  # $label12
                            v5 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v6 = load32(v4)
                                break
                            v6 = (load32(v4 + 12) + v5)
                            store32(v4 + 4, (load32(v4 + 12) + v5))
                            v3 = load32(v4)
                            v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy
                            if v3:
                                v5 = load32(v4 + 8)
                            store32(v4, v6)
                            break
                        v3 = load32(v7 + 20)
                        store32(v4 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), 0)
                        while True:  # $label13
                            v5 = load32(v3 + 8)
                            if (load32(v3 + 8) != load32(v3 + 4)):
                                v6 = load32(v3)
                                break
                            v6 = (load32(v3 + 12) + v5)
                            store32(v3 + 4, (load32(v3 + 12) + v5))
                            v4 = load32(v3)
                            v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy
                            if v4:
                                v5 = load32(v3 + 8)
                            store32(v3, v6)
                            break
                        v4 = load32(v7 + 20)
                        store32(v3 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), 5)
                        while True:  # $label14
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
                        store32(v4 + 8, (v3 + 1))
                        break
                    if not v3:
                        break
                    break
                store32((v3 + 8), 0)
                break
            v13 = (v13 + 1)
            if ((v13 + 1) != arg2):
                continue
            break
    v7 = (0 if v11 else v18)
    v12 = (((9 if (v10 == 6) else v8) if (0 if v11 else v18) else v8) if v9 else v8)
    while True:  # $label17
        if not v20:
            break
        if not v7:
            break
        if ((v10 != 62) & (v10 != 40)):
            break
        v12 = 14
        break
    while True:  # $label20
        while True:  # $label19
            while True:  # $label18
                if not v20:
                    break
                if not v9:
                    break
                if not v7:
                    break
                if ((v10 != 62) & (v10 != 40)):
                    break
                v12 = 15
                break
                break
            v6 = v16
            if not v7:
                break
            break
        arg0 = entities[v7]
        v6 = load16u(entities[v7] + 114)
        break
    v13 = load16u(arg0 + 112)
    while True:  # $label23
        while True:  # $label22
            while True:  # $label21
                if not v9:
                    break
                if (v10 == 6):
                    break
                if (v12 != 15):
                    break
                break
            if not arg2:
                break
            # TODO: memory.fill
            arg0 = 0
            while True:  # $label25
                v11 = load32(ENTITIES)
                v3 = 2147483647
                v4 = 0
                while True:  # $label24
                    if not load8u((v4 + 9163808)):
                        v8 = (v11 + (load32((arg1 + (v4 << 2))) * 132))
                        v14 = (load16u((v11 + (load32((arg1 + (v4 << 2))) * 132)) + 114) - v6)
                        v8 = (load16u(v8 + 112) - v13)
                        v8 = (((load16u((v11 + (load32((arg1 + (v4 << 2))) * 132)) + 114) - v6) * v14) + ((load16u(v8 + 112) - v13) * v8))
                        v8 = (v3 > v8)
                        v3 = ((((load16u((v11 + (load32((arg1 + (v4 << 2))) * 132)) + 114) - v6) * v14) + ((load16u(v8 + 112) - v13) * v8)) if (v3 > v8) else v3)
                        v5 = (v4 if v8 else v5)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != arg2):
                        continue
                    break
                store8((v5 + 9163808), 1)
                v3 = (v11 + (load32((arg1 + (v5 << 2))) * 132))
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != arg2):
                    continue
                break
            break
            break
        if not arg2:
            break
        v11 = ((v10 * 40) + 9671208)
        v4 = 0
        v8 = load32(PLAYERS)
        v14 = load32(ENTITIES)
        v5 = 2147483647
        v3 = 0
        while True:  # $label27
            while True:  # $label26
                arg0 = (v14 + (load32((arg1 + (v4 << 2))) * 132))
                if (v10 == load8u((v14 + (load32((arg1 + (v4 << 2))) * 132)) + 123)):
                    break
                v9 = load32(v11)
                if load32(v11):
                    if (u32(load32((((v8 + (load16u(arg0 + 110) * 286704)) + (v9 << 2)) + 283984))) > u32(load32(arg0 + 72))):
                        break
                v9 = (load16u(arg0 + 114) - v6)
                v9 = (load16u(arg0 + 112) - v13)
                v9 = (((load16u(arg0 + 114) - v6) * v9) + ((load16u(arg0 + 112) - v13) * v9))
                v9 = (v5 > v9)
                v5 = ((((load16u(arg0 + 114) - v6) * v9) + ((load16u(arg0 + 112) - v13) * v9)) if (v5 > v9) else v5)
                v3 = (load32(arg0 + 28) if v9 else v3)
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != arg2):
                continue
            break
        if not v3:
            break
        break
    return 9163808

# ----------------------------------------------------------
# $func175
# ----------------------------------------------------------
def func175(arg0):
    # TODO: i32.atomic.rmw.cmpxchg
    if 1:
        # TODO: i32.atomic.rmw.cmpxchg
        while True:  # $label0
            # TODO: i32.atomic.rmw.cmpxchg
            if 2:
                continue
            break

# ----------------------------------------------------------
# $func176
# ----------------------------------------------------------
def func176(arg0, arg1, arg2):
    v7 = load32(PLAYERS)
    v3 = load32(9143004)
    v4 = load32(PLAYER_COUNT)
    v5 = ((load32(PLAYER_COUNT) * arg1) + arg0)
    v6 = (arg2 != 0)
    store8((load32(9143004) + ((load32(PLAYER_COUNT) * arg1) + arg0)), (arg2 != 0))
    store8((v3 + ((arg0 * v4) + arg1)), v6)
    v6 = load32(CURRENT_PLAYER)
    v8 = (load32(CURRENT_PLAYER) == arg0)
    v9 = ((load32(CURRENT_PLAYER) == arg0) | (arg1 == v6))
    if arg2:
        while True:  # $label0
            if not v9:
                break
            v3 = 0
            arg2 = (arg1 if v8 else arg0)
            if not load8u((load32(9143012) + ((arg1 if v8 else arg0) + (v4 * v6)))):
                break
            v8 = (v7 + (arg2 * 286704))
            while True:  # $label4
                while True:  # $label1
                    v4 = load32(((v8 + (v3 << 2)) + 284636))
                    if not load32(((v8 + (v3 << 2)) + 284636)):
                        break
                    arg2 = 0
                    v6 = load32(v4 + 8)
                    if not load32(v4 + 8):
                        break
                    while True:  # $label3
                        while True:  # $label2
                            v5 = load32((load32(v4) + (arg2 << 2)))
                            if not load32((load32(v4) + (arg2 << 2))):
                                break
                            v5 = entities[v5]
                            if load32(entities[v5].action):
                                break
                            func118(v5)
                            v6 = load32(v4 + 8)
                            break
                        arg2 = (arg2 + 1)
                        if (u32((arg2 + 1)) < u32(v6)):
                            continue
                        break
                    break
                v3 = (v3 + 1)
                if ((v3 + 1) != 255):
                    continue
                break
            v5 = ((load32(PLAYER_COUNT) * arg1) + arg0)
            break
        store8((load32(9143016) + v5), 0)
        store8((load32(9143016) + ((load32(PLAYER_COUNT) * arg0) + arg1)), 0)
        arg2 = load32(9143012)
        v3 = load32(PLAYER_COUNT)
        v4 = ((load32(PLAYER_COUNT) * arg1) + arg0)
        store8((load32(9143012) + ((load32(PLAYER_COUNT) * arg1) + arg0)), 0)
        v3 = ((arg0 * v3) + arg1)
        store8((arg2 + ((arg0 * v3) + arg1)), 0)
        arg2 = load32(9143008)
        store8((load32(9143008) + v4), 0)
        store8((arg2 + v3), 0)
    arg2 = load32((v7 + (arg0 * 286704)) + 281800)
    if load32((v7 + (arg0 * 286704)) + 281800):
        store32((arg2 + (arg1 << 2)), 0)
    arg1 = load32((v7 + (arg1 * 286704)) + 281800)
    if load32((v7 + (arg1 * 286704)) + 281800):
        store32((arg1 + (arg0 << 2)), 0)
    if v9:
        la()
        a_b()

# ----------------------------------------------------------
# $func177
# ----------------------------------------------------------
def func177(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
    v36 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label67
        if (arg8 >= 2):
            while True:  # $label21
                arg10 = arg0
                arg8 = arg1
                v15 = arg2
                arg11 = arg6
                v20 = arg7
                arg0 = 0
                arg1 = 0
                while True:  # $label18
                    v19 = arg9
                    arg6 = load32(arg9)
                    if load32(arg9):
                        arg2 = ((arg6 & 0xFFFFFFFF) >> 16)
                        while True:  # $label2
                            while True:  # $label1
                                while True:  # $label0
                                    arg6 = (arg6 & 65535)
                                    if (arg10 == (arg6 & 65535)):
                                        v14 = ((arg2 == arg8) | ((arg8 + 1) == arg2))
                                        if ((arg10 + 1) == arg6):
                                            break
                                        if not v14:
                                            break
                                        break
                                    if ((arg10 + 1) != arg6):
                                        break
                                    break
                                if (arg2 == arg8):
                                    break
                                if ((arg8 + 1) == arg2):
                                    break
                                if v14:
                                    break
                                break
                            arg7 = load32(ENTITIES)
                            arg9 = load32(9142840)
                            v16 = (arg6 + 1)
                            v12 = (load32(9142440) + 2)
                            v14 = (arg2 + ((load32(9142440) + 2) * arg5))
                            v21 = (((arg2 + ((load32(9142440) + 2) * arg5)) + 1) * v12)
                            v13 = load32((load32(9142840) + (((arg6 + 1) + (((arg2 + ((load32(9142440) + 2) * arg5)) + 1) * v12)) << 2)))
                            if (arg4 != load32((load32(9142840) + (((arg6 + 1) + (((arg2 + ((load32(9142440) + 2) * arg5)) + 1) * v12)) << 2)))):
                                if (v13 == -1):
                                    break
                                if (load8u((arg7 + (v13 * 132)) + 125) != 1):
                                    break
                            v27 = (arg6 + 2)
                            v13 = load32((arg9 + ((v21 + (arg6 + 2)) << 2)))
                            if (arg4 != load32((arg9 + ((v21 + (arg6 + 2)) << 2)))):
                                if (v13 == -1):
                                    break
                                if (load8u((arg7 + (v13 * 132)) + 125) != 1):
                                    break
                            v13 = ((v14 + 2) * v12)
                            v12 = load32((arg9 + ((v16 + ((v14 + 2) * v12)) << 2)))
                            if (arg4 != load32((arg9 + ((v16 + ((v14 + 2) * v12)) << 2)))):
                                if (v12 == -1):
                                    break
                                if (load8u((arg7 + (v12 * 132)) + 125) != 1):
                                    break
                            arg9 = load32((arg9 + ((v13 + v27) << 2)))
                            if (arg4 != load32((arg9 + ((v13 + v27) << 2)))):
                                if (arg9 == -1):
                                    break
                                if (load8u((arg7 + (arg9 * 132)) + 125) != 1):
                                    break
                            v14 = 1
                            while True:  # $label12
                                v27 = 0
                                arg7 = load16u(40596)
                                arg9 = (load16u(40596) + 2)
                                store16(40596, (load16u(40596) + 2))
                                v16 = load32(9142440)
                                while True:  # $label3
                                    if (u32((arg9 & 65535)) < u32(65534)):
                                        break
                                    store16(40596, 1)
                                    arg9 = (v16 * v16)
                                    if not (v16 * v16):
                                        break
                                    # TODO: memory.fill
                                    break
                                v17 = (arg7 + 1)
                                store32(59200, ((arg2 << 16) + arg6))
                                v23 = load32(9142436)
                                v21 = 1
                                while True:  # $label17
                                    v31 = (v17 & 65535)
                                    arg2 = load32(((v27 << 2) + 59200))
                                    arg7 = ((load32(((v27 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                                    arg9 = (arg2 & 65535)
                                    arg2 = (v23 + (((((load32(((v27 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * v16) + (arg2 & 65535)) << 1))
                                    if ((v17 & 65535) != load16u((v23 + (((((load32(((v27 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * v16) + (arg2 & 65535)) << 1)))):
                                        store16(arg2, v17)
                                        while True:  # $label13
                                            v22 = 0
                                            v33 = (load32(9142440) + 2)
                                            v32 = ((load32(9142440) + 2) * arg5)
                                            v26 = load32(ENTITIES)
                                            v24 = load32(9142840)
                                            while True:  # $label9
                                                arg2 = (v22 << 3)
                                                v12 = (load32(((v22 << 3) + 8928)) + arg9)
                                                while True:  # $label8
                                                    while True:  # $label4
                                                        v13 = (load32((arg2 + 8932)) + arg7)
                                                        v25 = ((load32((arg2 + 8932)) + arg7) + 2)
                                                        if (((load32((arg2 + 8932)) + arg7) + 2) <= v13):
                                                            break
                                                        v28 = 0
                                                        arg6 = v13
                                                        v29 = (v12 + 2)
                                                        if ((v12 + 2) <= v12):
                                                            break
                                                        while True:  # $label7
                                                            arg6 = (arg6 + 1)
                                                            v34 = (((arg6 + 1) + v32) * v33)
                                                            arg2 = v12
                                                            while True:  # $label5
                                                                while True:  # $label6
                                                                    arg2 = (arg2 + 1)
                                                                    v18 = load32((v24 + (((arg2 + 1) + v34) << 2)))
                                                                    if (arg4 != load32((v24 + (((arg2 + 1) + v34) << 2)))):
                                                                        if (v18 == -1):
                                                                            break
                                                                        if (load8u((v26 + (v18 * 132)) + 125) != 1):
                                                                            break
                                                                    if (arg2 != v29):
                                                                        continue
                                                                    break
                                                                v28 = (arg6 >= v25)
                                                                if (arg6 != v25):
                                                                    continue
                                                                break
                                                            break
                                                        if not v28:
                                                            break
                                                        break
                                                    if (load16u((v23 + (((v13 * v16) + v12) << 1))) == v31):
                                                        break
                                                    arg2 = (v12 - arg10)
                                                    arg2 = (v13 - arg8)
                                                    if (((((v12 - arg10) * arg2) + ((v13 - arg8) * arg2)) - 1) > 1156):
                                                        break
                                                    store32(((v21 << 2) + 59200), ((v13 << 16) + v12))
                                                    v21 = (v21 + 1)
                                                    break
                                                v22 = (v22 + 1)
                                                if ((v22 + 1) != 8):
                                                    continue
                                                break
                                            arg2 = (arg8 - arg7)
                                            while True:  # $label10
                                                arg6 = (arg10 - arg9)
                                                if not (arg10 - arg9):
                                                    break
                                                if (arg7 == arg8):
                                                    break
                                                arg6 = (arg2 // arg6)
                                                arg6 = (arg6 >> 31)
                                                arg6 = (arg6 if (u32((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u32(1)) else 0)
                                                arg2 = ((arg6 if (u32((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u32(1)) else 0) // arg2)
                                                arg2 = (arg2 >> 31)
                                                arg2 = (arg2 if (u32(((((arg6 if (u32((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u32(1)) else 0) // arg2) ^ (arg2 >> 31)) - arg2)) <= u32(1)) else 0)
                                                break
                                            arg2 = (-1 if (arg2 < 0) else (arg2 != 0))
                                            arg7 = ((-1 if (arg2 < 0) else (arg2 != 0)) + arg7)
                                            while True:  # $label11
                                                arg6 = (-1 if (arg6 < 0) else (arg6 != 0))
                                                arg9 = ((-1 if (arg6 < 0) else (arg6 != 0)) + arg9)
                                                if (((-1 if (arg6 < 0) else (arg6 != 0)) + arg9) != arg10):
                                                    break
                                                if (arg7 != arg8):
                                                    break
                                                store32(arg11, (0 - arg6))
                                                store32(v20, (0 - arg2))
                                                break
                                                break
                                            store16((v23 + (((arg7 * v16) + arg9) << 1)), v17)
                                            v13 = (arg7 + 2)
                                            if ((arg7 + 2) <= arg7):
                                                continue
                                            v25 = (arg9 + 2)
                                            if ((arg9 + 2) <= arg9):
                                                continue
                                            arg6 = 0
                                            v28 = (load32(9142440) + 2)
                                            v18 = ((load32(9142440) + 2) * arg5)
                                            v33 = load32(ENTITIES)
                                            v32 = load32(9142840)
                                            v12 = arg7
                                            while True:  # $label16
                                                v12 = (v12 + 1)
                                                v26 = (((v12 + 1) + v18) * v28)
                                                arg2 = arg9
                                                while True:  # $label14
                                                    while True:  # $label15
                                                        arg2 = (arg2 + 1)
                                                        v22 = load32((v32 + (((arg2 + 1) + v26) << 2)))
                                                        if (arg4 != load32((v32 + (((arg2 + 1) + v26) << 2)))):
                                                            if (v22 == -1):
                                                                break
                                                            if (load8u((v33 + (v22 * 132)) + 125) != 1):
                                                                break
                                                        if (arg2 != v25):
                                                            continue
                                                        break
                                                    arg6 = (v12 >= v13)
                                                    if (v12 != v13):
                                                        continue
                                                    break
                                                break
                                            if (arg6 & 1):
                                                continue
                                            break
                                    v27 = (v27 + 1)
                                    if (u32((v27 + 1)) < u32(v21)):
                                        continue
                                    break
                                break
                            if 0:
                                break
                            break
                        store32(v19, 0)
                    arg2 = (arg3 - arg8)
                    v23 = load32(9142440)
                    while True:  # $label19
                        arg6 = (v15 - arg10)
                        if not (v15 - arg10):
                            break
                        if (arg3 == arg8):
                            break
                        arg6 = (arg2 // arg6)
                        arg6 = (arg6 >> 31)
                        arg6 = (arg6 if (u32((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u32(1)) else 0)
                        arg2 = ((arg6 if (u32((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u32(1)) else 0) // arg2)
                        arg2 = (arg2 >> 31)
                        arg2 = (arg2 if (u32(((((arg6 if (u32((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u32(1)) else 0) // arg2) ^ (arg2 >> 31)) - arg2)) <= u32(1)) else 0)
                        break
                    arg6 = (-1 if (arg6 < 0) else (arg6 != 0))
                    store32(arg11, (-1 if (arg6 < 0) else (arg6 != 0)))
                    arg2 = (-1 if (arg2 < 0) else (arg2 != 0))
                    store32(v20, (-1 if (arg2 < 0) else (arg2 != 0)))
                    arg6 = (arg6 + arg10)
                    arg2 = (arg2 + arg8)
                    v16 = load32(9142440)
                    v21 = (load32(9142440) + 2)
                    v27 = ((load32(9142440) + 2) * arg5)
                    arg9 = load32(ENTITIES)
                    v12 = load32(9142840)
                    v13 = 0
                    while True:  # $label26
                        while True:  # $label20
                            if (arg6 != v15):
                                break
                            if (arg2 != arg3):
                                break
                            break
                            break
                        while True:  # $label23
                            while True:  # $label22
                                if (arg2 > 2147483645):
                                    break
                                if (arg6 > 2147483645):
                                    break
                                v14 = (arg6 + 1)
                                v17 = (arg2 + 1)
                                v22 = (((arg2 + 1) + v27) * v21)
                                arg7 = load32((v12 + (((arg6 + 1) + (((arg2 + 1) + v27) * v21)) << 2)))
                                if (arg4 != load32((v12 + (((arg6 + 1) + (((arg2 + 1) + v27) * v21)) << 2)))):
                                    if (arg7 == -1):
                                        break
                                    if (load8u((arg9 + (arg7 * 132)) + 125) != 1):
                                        break
                                v25 = (arg6 + 2)
                                arg7 = load32((v12 + ((v22 + (arg6 + 2)) << 2)))
                                if (arg4 != load32((v12 + ((v22 + (arg6 + 2)) << 2)))):
                                    if (arg7 == -1):
                                        break
                                    if (load8u((arg9 + (arg7 * 132)) + 125) != 1):
                                        break
                                while True:  # $label24
                                    v22 = (arg2 + 2)
                                    v28 = (((arg2 + 2) + v27) * v21)
                                    arg7 = load32((v12 + ((v14 + (((arg2 + 2) + v27) * v21)) << 2)))
                                    if (arg4 != load32((v12 + ((v14 + (((arg2 + 2) + v27) * v21)) << 2)))):
                                        if (arg7 == -1):
                                            break
                                        if (load8u((arg9 + (arg7 * 132)) + 125) != 1):
                                            break
                                    arg7 = load32((v12 + ((v25 + v28) << 2)))
                                    if (arg4 != load32((v12 + ((v25 + v28) << 2)))):
                                        if (arg7 == -1):
                                            break
                                        if (load8u((arg9 + (arg7 * 132)) + 125) != 1):
                                            break
                                    break
                                    break
                                if (v17 < v22):
                                    break
                                break
                            v14 = (arg3 - arg2)
                            while True:  # $label25
                                arg7 = (v15 - arg6)
                                if not (v15 - arg6):
                                    break
                                if (arg2 == arg3):
                                    break
                                arg7 = (v14 // arg7)
                                arg7 = (arg7 >> 31)
                                arg7 = (arg7 if (u32((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u32(1)) else 0)
                                v14 = ((arg7 if (u32((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u32(1)) else 0) // v14)
                                v14 = (v14 >> 31)
                                v14 = (v14 if (u32(((((arg7 if (u32((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u32(1)) else 0) // v14) ^ (v14 >> 31)) - v14)) <= u32(1)) else 0)
                                break
                            arg6 = ((-1 if (arg7 < 0) else (arg7 != 0)) + arg6)
                            arg2 = ((-1 if (v14 < 0) else (v14 != 0)) + arg2)
                            v14 = 1
                            v13 = (v13 + 1)
                            if ((v13 + 1) != 32):
                                continue
                            break
                            break
                        break
                    v21 = load16u(40596)
                    arg7 = (load16u(40596) + 2)
                    store16(40596, (load16u(40596) + 2))
                    v26 = (arg6 + (arg2 << 16))
                    while True:  # $label27
                        if (u32((arg7 & 65535)) < u32(65534)):
                            break
                        store16(40596, 1)
                        arg7 = (v16 * v16)
                        if not (v16 * v16):
                            break
                        # TODO: memory.fill
                        break
                    v33 = (v21 + 1)
                    store32(59200, v26)
                    v17 = load32(9142436)
                    store16((load32(9142436) + ((arg6 + (arg2 * v23)) << 1)), v21)
                    v27 = 2147483647
                    v18 = 1
                    arg2 = 0
                    v25 = 0
                    while True:  # $label44
                        v35 = (3000 if (u32(v25) <= u32(3000)) else v25)
                        v12 = (arg2 + 1)
                        arg2 = load32(((arg2 << 2) + 59200))
                        arg9 = ((load32(((arg2 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                        v16 = (arg2 & 65535)
                        while True:  # $label28
                            while True:  # $label43
                                if (v25 == v35):
                                    break
                                v25 = (v25 + 1)
                                v14 = 0
                                v31 = 0
                                while True:  # $label42
                                    while True:  # $label29
                                        arg2 = (v14 << 4)
                                        arg6 = (load32(((v14 << 4) + 8932)) + arg9)
                                        if ((load32(((v14 << 4) + 8932)) + arg9) > 2147483645):
                                            break
                                        arg7 = (load32((arg2 + 8928)) + v16)
                                        if ((load32((arg2 + 8928)) + v16) > 2147483645):
                                            break
                                        v13 = load32(ENTITIES)
                                        while True:  # $label31
                                            while True:  # $label30
                                                v22 = load32(9142840)
                                                v29 = (arg7 + 1)
                                                v34 = (arg6 + 1)
                                                v28 = (load32(9142440) + 2)
                                                v32 = ((load32(9142440) + 2) * arg5)
                                                v24 = (((arg6 + 1) + ((load32(9142440) + 2) * arg5)) * v28)
                                                arg2 = load32((load32(9142840) + (((arg7 + 1) + (((arg6 + 1) + ((load32(9142440) + 2) * arg5)) * v28)) << 2)))
                                                if (load32((load32(9142840) + (((arg7 + 1) + (((arg6 + 1) + ((load32(9142440) + 2) * arg5)) * v28)) << 2))) == arg4):
                                                    break
                                                if (arg2 == -1):
                                                    break
                                                if (load8u((v13 + (arg2 * 132)) + 125) != 1):
                                                    break
                                                break
                                            while True:  # $label33
                                                while True:  # $label32
                                                    v38 = (arg7 + 2)
                                                    v24 = load32((v22 + (((arg7 + 2) + v24) << 2)))
                                                    if (load32((v22 + (((arg7 + 2) + v24) << 2))) == arg4):
                                                        break
                                                    if (v24 == -1):
                                                        break
                                                    if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                        break
                                                    break
                                                while True:  # $label35
                                                    while True:  # $label34
                                                        v37 = (arg6 + 2)
                                                        v39 = (((arg6 + 2) + v32) * v28)
                                                        v24 = load32((v22 + ((v29 + (((arg6 + 2) + v32) * v28)) << 2)))
                                                        if (load32((v22 + ((v29 + (((arg6 + 2) + v32) * v28)) << 2))) == arg4):
                                                            break
                                                        if (v24 == -1):
                                                            break
                                                        if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                            break
                                                        break
                                                    while True:  # $label36
                                                        v24 = load32((v22 + ((v38 + v39) << 2)))
                                                        if (load32((v22 + ((v38 + v39) << 2))) == arg4):
                                                            break
                                                        if (v24 == -1):
                                                            break
                                                        if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                            break
                                                        break
                                                    break
                                                    break
                                                if (v34 >= v37):
                                                    break
                                                if (arg2 != -1):
                                                    break
                                                break
                                                break
                                            if (arg2 == -1):
                                                break
                                            break
                                        arg2 = 0
                                        v38 = (v17 + (((arg6 * v23) + arg7) << 1))
                                        if (load16u((v17 + (((arg6 * v23) + arg7) << 1))) == v21):
                                            break
                                        while True:  # $label40
                                            while True:  # $label37
                                                v29 = (arg2 << 3)
                                                v24 = (load32(((arg2 << 3) + 8932)) + arg6)
                                                if ((load32(((arg2 << 3) + 8932)) + arg6) > 2147483645):
                                                    break
                                                v29 = (load32((v29 + 8928)) + arg7)
                                                if ((load32((v29 + 8928)) + arg7) > 2147483645):
                                                    break
                                                while True:  # $label38
                                                    v37 = (v29 + 1)
                                                    v39 = (v24 + 1)
                                                    v40 = (((v24 + 1) + v32) * v28)
                                                    v34 = load32((v22 + (((v29 + 1) + (((v24 + 1) + v32) * v28)) << 2)))
                                                    if (arg4 != load32((v22 + (((v29 + 1) + (((v24 + 1) + v32) * v28)) << 2)))):
                                                        if (v34 == -1):
                                                            break
                                                        if (load8u((v13 + (v34 * 132)) + 125) != 1):
                                                            break
                                                    v34 = (v29 + 2)
                                                    v29 = load32((v22 + (((v29 + 2) + v40) << 2)))
                                                    if (arg4 != load32((v22 + (((v29 + 2) + v40) << 2)))):
                                                        if (v29 == -1):
                                                            break
                                                        if (load8u((v13 + (v29 * 132)) + 125) != 1):
                                                            break
                                                    while True:  # $label39
                                                        v29 = (v24 + 2)
                                                        v40 = (((v24 + 2) + v32) * v28)
                                                        v24 = load32((v22 + ((v37 + (((v24 + 2) + v32) * v28)) << 2)))
                                                        if (arg4 != load32((v22 + ((v37 + (((v24 + 2) + v32) * v28)) << 2)))):
                                                            if (v24 == -1):
                                                                break
                                                            if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                                break
                                                        v24 = load32((v22 + ((v34 + v40) << 2)))
                                                        if (arg4 != load32((v22 + ((v34 + v40) << 2)))):
                                                            if (v24 == -1):
                                                                break
                                                            if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                                break
                                                        break
                                                        break
                                                    if (v29 <= v39):
                                                        break
                                                    break
                                                arg2 = (arg2 + 1)
                                                if ((arg2 + 1) != 8):
                                                    continue
                                                break
                                                break
                                            break
                                        arg2 = ((arg6 << 16) + arg7)
                                        while True:  # $label41
                                            if not v31:
                                                arg0 = arg7
                                                arg1 = arg6
                                                break
                                            store32(((v18 << 2) + 59200), arg2)
                                            v18 = (v18 + 1)
                                            break
                                        store16(v38, v21)
                                        arg6 = (arg6 - arg3)
                                        arg6 = (arg7 - v15)
                                        arg6 = (((arg6 - arg3) * arg6) + ((arg7 - v15) * arg6))
                                        arg6 = (arg6 < v27)
                                        v27 = ((((arg6 - arg3) * arg6) + ((arg7 - v15) * arg6)) if (arg6 < v27) else v27)
                                        v30 = (arg2 if arg6 else v30)
                                        v31 = (v31 + 1)
                                        break
                                    v14 = (v14 + 1)
                                    if ((v14 + 1) != 4):
                                        continue
                                    break
                                v16 = arg0
                                arg9 = arg1
                                if v31:
                                    continue
                                break
                            if (u32(v12) >= u32(v18)):
                                break
                            arg2 = v12
                            if (u32(v25) < u32(3001)):
                                continue
                            break
                        break
                    arg6 = 0
                    v12 = (load32(9142440) + 2)
                    v16 = ((load32(9142440) + 2) * arg5)
                    arg7 = 2147483647
                    arg0 = (v26 if (v27 == 2147483647) else v30)
                    v27 = (((v26 if (v27 == 2147483647) else v30) & 0xFFFFFFFF) >> 16)
                    v22 = (arg0 & 65535)
                    arg1 = load32(ENTITIES)
                    arg2 = load32(9142840)
                    v13 = 55
                    while True:  # $label48
                        arg9 = (arg6 << 3)
                        arg0 = (load32(((arg6 << 3) + 8928)) + v22)
                        while True:  # $label46
                            while True:  # $label45
                                arg9 = (load32((arg9 + 8932)) + v27)
                                if ((load32((arg9 + 8932)) + v27) > 2147483645):
                                    break
                                if (arg0 > 2147483645):
                                    break
                                v25 = (arg0 + 1)
                                v28 = (arg9 + 1)
                                v18 = (((arg9 + 1) + v16) * v12)
                                v14 = load32((arg2 + (((arg0 + 1) + (((arg9 + 1) + v16) * v12)) << 2)))
                                if (arg4 != load32((arg2 + (((arg0 + 1) + (((arg9 + 1) + v16) * v12)) << 2)))):
                                    if (v14 == -1):
                                        break
                                    if (load8u((arg1 + (v14 * 132)) + 125) != 1):
                                        break
                                v30 = (arg0 + 2)
                                v14 = load32((arg2 + ((v18 + (arg0 + 2)) << 2)))
                                if (arg4 != load32((arg2 + ((v18 + (arg0 + 2)) << 2)))):
                                    if (v14 == -1):
                                        break
                                    if (load8u((arg1 + (v14 * 132)) + 125) != 1):
                                        break
                                while True:  # $label47
                                    v18 = (arg9 + 2)
                                    v31 = (((arg9 + 2) + v16) * v12)
                                    v14 = load32((arg2 + ((v25 + (((arg9 + 2) + v16) * v12)) << 2)))
                                    if (arg4 != load32((arg2 + ((v25 + (((arg9 + 2) + v16) * v12)) << 2)))):
                                        if (v14 == -1):
                                            break
                                        if (load8u((arg1 + (v14 * 132)) + 125) != 1):
                                            break
                                    v14 = load32((arg2 + ((v30 + v31) << 2)))
                                    if (arg4 != load32((arg2 + ((v30 + v31) << 2)))):
                                        if (v14 == -1):
                                            break
                                        if (load8u((arg1 + (v14 * 132)) + 125) != 1):
                                            break
                                    break
                                    break
                                if (v18 > v28):
                                    break
                                break
                            v14 = (arg9 - arg3)
                            v14 = (arg0 - v15)
                            v14 = (((arg9 - arg3) * v14) + ((arg0 - v15) * v14))
                            v14 = (arg7 > v14)
                            arg7 = ((((arg9 - arg3) * v14) + ((arg0 - v15) * v14)) if (arg7 > v14) else arg7)
                            v13 = (((arg9 << 16) + arg0) if v14 else v13)
                            break
                        arg6 = (arg6 + 1)
                        if ((arg6 + 1) != 8):
                            continue
                        break
                    store32(59200, v13)
                    store16((v17 + (((((v13 & 0xFFFFFFFF) >> 16) * v23) + (v13 & 65535)) << 1)), v33)
                    v27 = 1
                    arg0 = 0
                    while True:  # $label66
                        arg1 = arg0
                        arg0 = (arg0 + 1)
                        v15 = load32(((arg1 << 2) + 59200))
                        v25 = ((load32(((arg1 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                        v28 = (v15 & 65535)
                        arg9 = 0
                        while True:  # $label65
                            arg1 = (arg9 << 3)
                            v14 = load32(((arg9 << 3) + 8928))
                            arg6 = (load32(((arg9 << 3) + 8928)) + v28)
                            while True:  # $label50
                                while True:  # $label49
                                    v16 = load32((arg1 + 8932))
                                    arg2 = (load32((arg1 + 8932)) + v25)
                                    if ((load32((arg1 + 8932)) + v25) > 2147483645):
                                        break
                                    if (arg6 > 2147483645):
                                        break
                                    arg1 = load32(ENTITIES)
                                    arg3 = load32(9142840)
                                    v13 = (arg6 + 1)
                                    v22 = (arg2 + 1)
                                    arg7 = (load32(9142440) + 2)
                                    v18 = ((load32(9142440) + 2) * arg5)
                                    v30 = (((arg2 + 1) + ((load32(9142440) + 2) * arg5)) * arg7)
                                    v12 = load32((load32(9142840) + (((arg6 + 1) + (((arg2 + 1) + ((load32(9142440) + 2) * arg5)) * arg7)) << 2)))
                                    if (arg4 != load32((load32(9142840) + (((arg6 + 1) + (((arg2 + 1) + ((load32(9142440) + 2) * arg5)) * arg7)) << 2)))):
                                        if (v12 == -1):
                                            break
                                        if (load8u((arg1 + (v12 * 132)) + 125) != 1):
                                            break
                                    v31 = (arg6 + 2)
                                    v12 = load32((arg3 + ((v30 + (arg6 + 2)) << 2)))
                                    if (arg4 != load32((arg3 + ((v30 + (arg6 + 2)) << 2)))):
                                        if (v12 == -1):
                                            break
                                        if (load8u((arg1 + (v12 * 132)) + 125) != 1):
                                            break
                                    while True:  # $label51
                                        v12 = (arg2 + 2)
                                        v18 = (((arg2 + 2) + v18) * arg7)
                                        arg7 = load32((arg3 + ((v13 + (((arg2 + 2) + v18) * arg7)) << 2)))
                                        if (arg4 != load32((arg3 + ((v13 + (((arg2 + 2) + v18) * arg7)) << 2)))):
                                            if (arg7 == -1):
                                                break
                                            if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                break
                                        arg3 = load32((arg3 + ((v18 + v31) << 2)))
                                        if (arg4 != load32((arg3 + ((v18 + v31) << 2)))):
                                            if (arg3 == -1):
                                                break
                                            if (load8u((arg1 + (arg3 * 132)) + 125) != 1):
                                                break
                                        break
                                        break
                                    if (v12 > v22):
                                        break
                                    break
                                v13 = (arg2 * v23)
                                v18 = (v17 + (((arg2 * v23) + arg6) << 1))
                                if (load16u((v17 + (((arg2 * v23) + arg6) << 1))) == (v33 & 65535)):
                                    break
                                arg3 = (arg6 + 1)
                                while True:  # $label53
                                    while True:  # $label52
                                        arg1 = load32(9142440)
                                        v30 = (u32(load32(9142440)) <= u32(arg2))
                                        if (u32(load32(9142440)) <= u32(arg2)):
                                            break
                                        if (u32(arg1) <= u32(arg3)):
                                            break
                                        if ((arg2 | arg3) < 0):
                                            break
                                        if (load16u((v17 + ((arg3 + v13) << 1))) == v21):
                                            break
                                        break
                                    while True:  # $label54
                                        v12 = (arg2 - 1)
                                        v22 = (u32(arg1) <= u32((arg2 - 1)))
                                        if (u32(arg1) <= u32((arg2 - 1))):
                                            break
                                        if (u32(arg1) <= u32(arg3)):
                                            break
                                        if ((arg3 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg3) << 1))) == v21):
                                            break
                                        break
                                    while True:  # $label55
                                        if v22:
                                            break
                                        if (u32(arg1) <= u32(arg6)):
                                            break
                                        if ((arg6 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg6) << 1))) == v21):
                                            break
                                        break
                                    arg7 = (arg6 - 1)
                                    while True:  # $label56
                                        if v22:
                                            break
                                        if (u32(arg1) <= u32(arg7)):
                                            break
                                        if ((arg7 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg7) << 1))) == v21):
                                            break
                                        break
                                    while True:  # $label57
                                        if v30:
                                            break
                                        if (u32(arg1) <= u32(arg7)):
                                            break
                                        if ((arg2 | arg7) < 0):
                                            break
                                        if (load16u((v17 + ((arg7 + v13) << 1))) == v21):
                                            break
                                        break
                                    while True:  # $label58
                                        v12 = (arg2 + 1)
                                        v13 = (u32(arg1) <= u32((arg2 + 1)))
                                        if (u32(arg1) <= u32((arg2 + 1))):
                                            break
                                        if (u32(arg1) <= u32(arg7)):
                                            break
                                        if ((arg7 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg7) << 1))) == v21):
                                            break
                                        break
                                    while True:  # $label59
                                        if v13:
                                            break
                                        if (u32(arg1) <= u32(arg6)):
                                            break
                                        if ((arg6 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg6) << 1))) == v21):
                                            break
                                        break
                                    if v13:
                                        break
                                    if (u32(arg1) <= u32(arg3)):
                                        break
                                    if ((arg3 | v12) < 0):
                                        break
                                    if (load16u((v17 + (((v12 * v23) + arg3) << 1))) != v21):
                                        break
                                    break
                                store32(((v27 << 2) + 59200), ((arg2 << 16) + arg6))
                                while True:  # $label60
                                    arg3 = (arg6 - arg10)
                                    arg3 = (arg2 - arg8)
                                    if (((((arg6 - arg10) * arg3) + ((arg2 - arg8) * arg3)) - 1) > 1089):
                                        break
                                    if not ((arg6 == arg10) & (arg2 == arg8)):
                                        v13 = (arg2 == arg8)
                                        v12 = (arg1 + 2)
                                        v22 = ((arg1 + 2) * arg5)
                                        arg1 = load32(ENTITIES)
                                        arg3 = load32(9142840)
                                        while True:  # $label64
                                            v14 = (arg8 - arg2)
                                            while True:  # $label61
                                                arg7 = (arg10 - arg6)
                                                if not (arg10 - arg6):
                                                    break
                                                if (v13 & 1):
                                                    break
                                                arg7 = (v14 // arg7)
                                                arg7 = (arg7 >> 31)
                                                arg7 = (arg7 if (u32((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u32(1)) else 0)
                                                v13 = ((arg7 if (u32((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u32(1)) else 0) // v14)
                                                v13 = (v13 >> 31)
                                                v14 = (v14 if (u32(((((arg7 if (u32((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u32(1)) else 0) // v14) ^ (v13 >> 31)) - v13)) <= u32(1)) else 0)
                                                break
                                            while True:  # $label62
                                                v16 = (-1 if (v14 < 0) else (v14 != 0))
                                                arg2 = ((-1 if (v14 < 0) else (v14 != 0)) + arg2)
                                                v14 = (-1 if (arg7 < 0) else (arg7 != 0))
                                                arg6 = ((-1 if (arg7 < 0) else (arg7 != 0)) + arg6)
                                                if (load16u((v17 + (((((-1 if (v14 < 0) else (v14 != 0)) + arg2) * v23) + ((-1 if (arg7 < 0) else (arg7 != 0)) + arg6)) << 1))) != v21):
                                                    break
                                                if (arg2 > 2147483645):
                                                    break
                                                if (arg6 > 2147483645):
                                                    break
                                                v13 = (arg6 + 1)
                                                v30 = (arg2 + 1)
                                                v31 = (((arg2 + 1) + v22) * v12)
                                                arg7 = load32((arg3 + (((arg6 + 1) + (((arg2 + 1) + v22) * v12)) << 2)))
                                                if (arg4 != load32((arg3 + (((arg6 + 1) + (((arg2 + 1) + v22) * v12)) << 2)))):
                                                    if (arg7 == -1):
                                                        break
                                                    if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                        break
                                                v32 = (arg6 + 2)
                                                arg7 = load32((arg3 + ((v31 + (arg6 + 2)) << 2)))
                                                if (arg4 != load32((arg3 + ((v31 + (arg6 + 2)) << 2)))):
                                                    if (arg7 == -1):
                                                        break
                                                    if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                        break
                                                while True:  # $label63
                                                    v31 = (arg2 + 2)
                                                    v26 = (((arg2 + 2) + v22) * v12)
                                                    arg7 = load32((arg3 + ((v13 + (((arg2 + 2) + v22) * v12)) << 2)))
                                                    if (arg4 != load32((arg3 + ((v13 + (((arg2 + 2) + v22) * v12)) << 2)))):
                                                        if (arg7 == -1):
                                                            break
                                                        if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                            break
                                                    arg7 = load32((arg3 + ((v26 + v32) << 2)))
                                                    if (arg4 != load32((arg3 + ((v26 + v32) << 2)))):
                                                        if (arg7 == -1):
                                                            break
                                                        if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                            break
                                                    break
                                                    break
                                                if (v30 < v31):
                                                    break
                                                break
                                            v13 = (arg2 == arg8)
                                            if (arg6 != arg10):
                                                continue
                                            if (arg2 != arg8):
                                                continue
                                            break
                                    store32(arg11, (0 - v14))
                                    store32(v20, (0 - v16))
                                    store32(v19, v15)
                                    break
                                    break
                                v27 = (v27 + 1)
                                store16(v18, v33)
                                break
                            arg9 = (arg9 + 1)
                            if ((arg9 + 1) != 8):
                                continue
                            break
                        v14 = 0
                        if (u32(arg0) < u32(v27)):
                            continue
                        break
                    break
                break
            v20 = v14
            break
        arg8 = load32(arg9)
        if load32(arg9):
            v20 = 1
            if func365(arg0, arg1, (arg8 & 65535), ((arg8 & 0xFFFFFFFF) >> 16), arg4, arg5, arg6, arg7, load8u(arg10)):
                break
            store32(arg9, 0)
        store32(arg6, (-1 if (arg0 > arg2) else (arg0 != arg2)))
        store32(arg7, (-1 if (arg1 > arg3) else (arg1 != arg3)))
        v24 = (load32(9142440) + 2)
        v14 = ((load32(9142440) + 2) * arg5)
        v32 = load32(ENTITIES)
        v26 = load32(9142840)
        v20 = 1
        arg8 = arg0
        v12 = arg1
        while True:  # $label69
            v27 = ((-1 if (arg2 < arg8) else (arg2 != arg8)) + arg8)
            v21 = ((-1 if (arg3 < v12) else (arg3 != v12)) + v12)
            if ((arg2 == ((-1 if (arg2 < arg8) else (arg2 != arg8)) + arg8)) & (((-1 if (arg3 < v12) else (arg3 != v12)) + v12) == arg3)):
                break
            while True:  # $label68
                v15 = load32((((v27 + (((v14 + v21) + 1) * v24)) << 2) + v26) + 4)
                if (arg4 != load32((((v27 + (((v14 + v21) + 1) * v24)) << 2) + v26) + 4)):
                    if (v15 == -1):
                        break
                    if (load8u((v32 + (v15 * 132)) + 125) != 1):
                        break
                arg8 = v27
                v12 = v21
                v16 = (v16 + 1)
                if ((v16 + 1) != 32):
                    continue
                break
                break
            break
        store32(v36 + 8, v12)
        store32(v36 + 12, arg8)
        while True:  # $label81
            while True:  # $label80
                while True:  # $label78
                    while True:  # $label77
                        v28 = arg4
                        v20 = (load32(9142440) + 2)
                        v12 = ((load32(9142440) + 2) * arg5)
                        v15 = load32(ENTITIES)
                        v13 = load32(9142840)
                        while True:  # $label73
                            while True:  # $label71
                                while True:  # $label70
                                    v19 = load32(v36 + 8)
                                    arg4 = (v21 - load32(v36 + 8))
                                    v22 = ((v21 - load32(v36 + 8)) * arg4)
                                    arg4 = v27
                                    v16 = (v27 + 1)
                                    v17 = load32(v36 + 12)
                                    arg8 = ((v27 + 1) - load32(v36 + 12))
                                    if (u32((((v21 - load32(v36 + 8)) * arg4) + (((v27 + 1) - load32(v36 + 12)) * arg8))) > u32(2)):
                                        break
                                    arg8 = load32((((arg4 + (((v12 + v21) + 1) * v20)) << 2) + v13) + 8)
                                    if (v28 != load32((((arg4 + (((v12 + v21) + 1) * v20)) << 2) + v13) + 8)):
                                        if (arg8 == -1):
                                            break
                                        if (load8u((v15 + (arg8 * 132)) + 125) != 1):
                                            break
                                    break
                                    break
                                while True:  # $label72
                                    arg8 = (arg4 - v17)
                                    v25 = ((arg4 - v17) * arg8)
                                    arg8 = (v21 - 1)
                                    v23 = ((v21 - 1) - v19)
                                    if (u32((((arg4 - v17) * arg8) + (((v21 - 1) - v19) * v23))) > u32(2)):
                                        break
                                    v23 = load32((v13 + ((v16 + ((v12 + v21) * v20)) << 2)))
                                    if (load32((v13 + ((v16 + ((v12 + v21) * v20)) << 2))) == v28):
                                        break
                                    if (v23 == -1):
                                        break
                                    if (load8u((v15 + (v23 * 132)) + 125) == 1):
                                        break
                                    break
                                arg8 = (v21 + 1)
                                while True:  # $label75
                                    while True:  # $label74
                                        v23 = (arg4 - 1)
                                        v17 = ((arg4 - 1) - v17)
                                        if (u32((v22 + (((arg4 - 1) - v17) * v17))) > u32(2)):
                                            break
                                        v17 = load32((v13 + ((((arg8 + v12) * v20) + arg4) << 2)))
                                        if (load32((v13 + ((((arg8 + v12) * v20) + arg4) << 2))) == v28):
                                            break
                                        if (v17 == -1):
                                            break
                                        if (load8u((v15 + (v17 * 132)) + 125) == 1):
                                            break
                                        break
                                    while True:  # $label76
                                        v19 = (arg8 - v19)
                                        if (u32((((arg8 - v19) * v19) + v25)) > u32(2)):
                                            break
                                        v20 = load32((v13 + ((v16 + (((v12 + v21) + 2) * v20)) << 2)))
                                        if (load32((v13 + ((v16 + (((v12 + v21) + 2) * v20)) << 2))) == v28):
                                            break
                                        if (v20 == -1):
                                            break
                                        if (load8u((v15 + (v20 * 132)) + 125) == 1):
                                            break
                                        break
                                    break
                                    break
                                break
                            arg4 = v23
                            arg8 = v21
                            break
                        store32(v36 + 12, arg4)
                        store32(v36 + 8, arg8)
                        break
                    if 1:
                        arg4 = load32(v36 + 12)
                        v13 = load32(v36 + 8)
                        break
                    arg4 = load32(v36 + 12)
                    v12 = (load32(v36 + 12) + 1)
                    while True:  # $label79
                        v13 = load32(v36 + 8)
                        arg8 = (load32(v36 + 8) + 1)
                        v19 = (((v14 + (load32(v36 + 8) + 1)) * v24) + arg4)
                        v20 = load32((((((v14 + (load32(v36 + 8) + 1)) * v24) + arg4) << 2) + v26) + 8)
                        if (load32((((((v14 + (load32(v36 + 8) + 1)) * v24) + arg4) << 2) + v26) + 8) == v28):
                            break
                        if (v20 != -1):
                            if (load8u((v32 + (v20 * 132)) + 125) == 1):
                                break
                        v15 = v12
                        break
                        break
                    v17 = (v13 + v14)
                    v16 = load32((v26 + ((((v13 + v14) * v24) + v12) << 2)))
                    if (v28 != load32((v26 + ((((v13 + v14) * v24) + v12) << 2)))):
                        v20 = (v13 - 1)
                        if (v16 == -1):
                            v15 = arg4
                            break
                        v15 = arg4
                        if (load8u((v32 + (v16 * 132)) + 125) != 1):
                            break
                    v16 = load32((v26 + (v19 << 2)))
                    if (v28 != load32((v26 + (v19 << 2)))):
                        v15 = (arg4 - 1)
                        if (v16 == -1):
                            break
                        v20 = v13
                        if (load8u((v32 + (v16 * 132)) + 125) != 1):
                            break
                    v12 = load32((v26 + ((((v17 + 2) * v24) + v12) << 2)))
                    if (load32((v26 + ((((v17 + 2) * v24) + v12) << 2))) == v28):
                        break
                    if (v12 == -1):
                        v15 = arg4
                        v20 = arg8
                        break
                    v15 = arg4
                    v20 = arg8
                    if (load8u((v32 + (v12 * 132)) + 125) != 1):
                        break
                    break
                v20 = v21
                v15 = v27
                break
                break
            v20 = v13
            break
        v19 = (v13 - v20)
        v30 = (arg4 - v15)
        v29 = (v14 + 1)
        v14 = v13
        v16 = arg4
        v12 = v20
        arg8 = v15
        while True:  # $label95
            while True:  # $label94
                v17 = (v14 + v30)
                v23 = (v16 + v19)
                while True:  # $label82
                    v22 = (arg8 + v19)
                    v25 = (v12 + v30)
                    v35 = load32(((((arg8 + v19) + (v24 * (v29 + (v12 + v30)))) << 2) + v26) + 4)
                    if (load32(((((arg8 + v19) + (v24 * (v29 + (v12 + v30)))) << 2) + v26) + 4) == v28):
                        break
                    if (v35 != -1):
                        if (load8u((v32 + (v35 * 132)) + 125) == 1):
                            break
                    break
                v35 = 0
                while True:  # $label87
                    while True:  # $label86
                        while True:  # $label83
                            while True:  # $label85
                                while True:  # $label84
                                    v38 = load32((((v23 + ((v17 + v29) * v24)) << 2) + v26) + 4)
                                    if (v28 != load32((((v23 + ((v17 + v29) * v24)) << 2) + v26) + 4)):
                                        if (v38 == -1):
                                            break
                                        if v35:
                                            break
                                        if (load8u((v32 + (v38 * 132)) + 125) != 1):
                                            break
                                        break
                                    if not v35:
                                        break
                                    break
                                v19 = ((v18 << 2) + 59200)
                                store32(((v18 << 2) + 59200), v23)
                                store32(v19 + 8, v33)
                                store32(v19 + 4, v17)
                                store32(v19 + 12, (((arg8 - v23) + ((v12 - v17) * 3)) + 4))
                                v30 = (v12 - v14)
                                v19 = (arg8 - v16)
                                v18 = (v18 + 4)
                                v14 = v25
                                v16 = v22
                                break
                                break
                            v19 = ((v18 << 2) + 59200)
                            store32(((v18 << 2) + 59200), v16)
                            store32(v19 + 8, v33)
                            store32(v19 + 4, v14)
                            store32(v19 + 12, (((v22 - v16) + ((v25 - v14) * 3)) + 13))
                            v30 = (v14 - v12)
                            v19 = (v16 - arg8)
                            v18 = (v18 + 4)
                            v12 = v17
                            arg8 = v23
                            break
                            break
                        v33 = 0
                        store32(59208, 0)
                        store32(59204, v14)
                        store32(59200, v16)
                        store32(59212, (((arg8 - v16) + ((v12 - v14) * 3)) + 13))
                        v25 = (0 - v30)
                        v30 = (0 - v19)
                        v13 = v14
                        arg4 = v16
                        v18 = 4
                        v19 = v12
                        v20 = arg8
                        while True:  # $label93
                            v15 = (v13 + v25)
                            v17 = (arg4 + v30)
                            while True:  # $label88
                                v23 = (v20 + v30)
                                v22 = (v19 + v25)
                                v34 = load32(((((v20 + v30) + (v24 * (v29 + (v19 + v25)))) << 2) + v26) + 4)
                                if (load32(((((v20 + v30) + (v24 * (v29 + (v19 + v25)))) << 2) + v26) + 4) == v28):
                                    break
                                if (v34 != -1):
                                    if (load8u((v32 + (v34 * 132)) + 125) == 1):
                                        break
                                break
                            v34 = 0
                            while True:  # $label89
                                while True:  # $label92
                                    while True:  # $label91
                                        while True:  # $label90
                                            v35 = load32((((v17 + ((v15 + v29) * v24)) << 2) + v26) + 4)
                                            if (v28 != load32((((v17 + ((v15 + v29) * v24)) << 2) + v26) + 4)):
                                                if (v35 == -1):
                                                    break
                                                if v34:
                                                    break
                                                if (load8u((v32 + (v35 * 132)) + 125) == 1):
                                                    break
                                                v25 = ((v18 << 2) + 59200)
                                                store32(((v18 << 2) + 59200), arg4)
                                                store32(v25 + 8, v33)
                                                store32(v25 + 4, v13)
                                                store32(v25 + 12, (((v23 - arg4) + ((v22 - v13) * 3)) + 13))
                                                v25 = (v13 - v19)
                                                v30 = (arg4 - v20)
                                                v18 = (v18 + 4)
                                                v19 = v15
                                                v20 = v17
                                                break
                                            if not v34:
                                                break
                                            break
                                        v25 = ((v18 << 2) + 59200)
                                        store32(((v18 << 2) + 59200), v17)
                                        store32(v25 + 8, v33)
                                        store32(v25 + 4, v15)
                                        store32(v25 + 12, (((v20 - v17) + ((v19 - v15) * 3)) + 4))
                                        v25 = (v19 - v13)
                                        v30 = (v20 - arg4)
                                        v18 = (v18 + 4)
                                        v13 = v22
                                        arg4 = v23
                                        break
                                        break
                                    v13 = v15
                                    arg4 = v17
                                    v19 = v22
                                    v20 = v23
                                    break
                                v34 = 1
                                v33 = (v33 + 1)
                                if (arg8 != v20):
                                    continue
                                if (v12 != v19):
                                    continue
                                if (arg4 != v16):
                                    continue
                                if (v13 != v14):
                                    continue
                                break
                                break
                            break
                        arg8 = ((v18 << 2) + 59200)
                        store32(((v18 << 2) + 59200), arg4)
                        store32(arg8 + 8, v33)
                        store32(arg8 + 4, v13)
                        store32(arg8 + 12, (((v20 - arg4) + ((v19 - v13) * 3)) + 13))
                        v18 = (v18 + 4)
                        v34 = 1
                        break
                        break
                    v14 = v17
                    v16 = v23
                    v12 = v25
                    arg8 = v22
                    break
                v33 = (v33 + 1)
                if (arg8 != v15):
                    continue
                if (v12 != v20):
                    continue
                if (arg4 != v16):
                    continue
                if (v13 != v14):
                    continue
                break
            break
        v20 = 0
        if not v18:
            break
        v39 = (v18 - 4)
        v40 = ((v18 - 4) if v34 else v18)
        if not ((v18 - 4) if v34 else v18):
            break
        v14 = ((arg2 << 1) | 1)
        v43 = ((v27 << 1) | 1)
        v23 = (((arg2 << 1) | 1) - ((v27 << 1) | 1))
        v17 = ((arg3 << 1) | 1)
        v44 = ((v21 << 1) | 1)
        v22 = (((arg3 << 1) | 1) - ((v21 << 1) | 1))
        v45 = ((arg0 << 1) | 1)
        v25 = (v14 - ((arg0 << 1) | 1))
        v46 = ((arg1 << 1) | 1)
        v32 = (v17 - ((arg1 << 1) | 1))
        v30 = 2147483647
        v27 = 2147483647
        while True:  # $label102
            arg4 = v20
            v20 = (v20 + 4)
            v12 = ((((v20 + 4) % v18) << 2) + 59200)
            v15 = load32(((((v20 + 4) % v18) << 2) + 59200) + 12)
            v21 = (v15 << 2)
            v13 = load32(v12 + 4)
            arg8 = ((((((3591 & 0xFFFFFFFF) >> load32(((((v20 + 4) % v18) << 2) + 59200) + 12)) & 1) + load32(((v15 << 2) + 9344))) + load32(v12 + 4)) << 1)
            v16 = load32(v12)
            v21 = ((load32(v12) + (load32((v21 + 9264)) + (((37449 & 0xFFFFFFFF) >> v15) & 1))) << 1)
            v12 = (arg4 << 2)
            v26 = load32((((arg4 << 2) | 12) + 59200))
            v29 = (v26 << 2)
            v15 = load32((v12 + 59200))
            v41 = ((((((37449 & 0xFFFFFFFF) >> load32((((arg4 << 2) | 12) + 59200))) & 1) + load32(((v26 << 2) + 9264))) + load32((v12 + 59200))) << 1)
            v24 = (((load32(v12) + (load32((v21 + 9264)) + (((37449 & 0xFFFFFFFF) >> v15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> load32((((arg4 << 2) | 12) + 59200))) & 1) + load32(((v26 << 2) + 9264))) + load32((v12 + 59200))) << 1))
            v12 = load32(((v12 | 4) + 59200))
            v42 = ((load32(((v12 | 4) + 59200)) + (load32((v29 + 9344)) + (((3591 & 0xFFFFFFFF) >> v26) & 1))) << 1)
            v26 = (arg8 - ((load32(((v12 | 4) + 59200)) + (load32((v29 + 9344)) + (((3591 & 0xFFFFFFFF) >> v26) & 1))) << 1))
            v29 = (((((((((3591 & 0xFFFFFFFF) >> load32(((((v20 + 4) % v18) << 2) + 59200) + 12)) & 1) + load32(((v15 << 2) + 9344))) + load32(v12 + 4)) << 1) - v17) * (((load32(v12) + (load32((v21 + 9264)) + (((37449 & 0xFFFFFFFF) >> v15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> load32((((arg4 << 2) | 12) + 59200))) & 1) + load32(((v26 << 2) + 9264))) + load32((v12 + 59200))) << 1))) + ((arg8 - ((load32(((v12 | 4) + 59200)) + (load32((v29 + 9344)) + (((3591 & 0xFFFFFFFF) >> v26) & 1))) << 1)) * (v14 - v21)))
            v35 = ((((((((((3591 & 0xFFFFFFFF) >> load32(((((v20 + 4) % v18) << 2) + 59200) + 12)) & 1) + load32(((v15 << 2) + 9344))) + load32(v12 + 4)) << 1) - v17) * (((load32(v12) + (load32((v21 + 9264)) + (((37449 & 0xFFFFFFFF) >> v15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> load32((((arg4 << 2) | 12) + 59200))) & 1) + load32(((v26 << 2) + 9264))) + load32((v12 + 59200))) << 1))) + ((arg8 - ((load32(((v12 | 4) + 59200)) + (load32((v29 + 9344)) + (((3591 & 0xFFFFFFFF) >> v26) & 1))) << 1)) * (v14 - v21))) > 0)
            v38 = (v29 != 0)
            v29 = not v29
            while True:  # $label97
                while True:  # $label96
                    v47 = (v17 - arg8)
                    v48 = (v21 - v14)
                    v37 = (((v17 - arg8) * v25) + ((v21 - v14) * v32))
                    v42 = (v17 - v42)
                    v41 = (v41 - v14)
                    v49 = (((v17 - v42) * v25) + ((v41 - v14) * v32))
                    if not ((((((v17 - arg8) * v25) + ((v21 - v14) * v32)) != 0) & (((((v17 - v42) * v25) + ((v41 - v14) * v32)) <= 0) ^ (v37 > 0))) if v49 else not v37):
                        v37 = (((arg8 - v46) * v24) + (v26 * (v45 - v21)))
                        if not ((v38 & (((((arg8 - v46) * v24) + (v26 * (v45 - v21))) <= 0) ^ v35)) if v37 else v29):
                            break
                    v37 = ((v23 * v47) + (v22 * v48))
                    v41 = ((v23 * v42) + (v22 * v41))
                    if (((((v23 * v47) + (v22 * v48)) != 0) & ((((v23 * v42) + (v22 * v41)) <= 0) ^ (v37 > 0))) if v41 else not v37):
                        break
                    arg8 = (((arg8 - v44) * v24) + (v26 * (v43 - v21)))
                    if ((v38 & (((((arg8 - v44) * v24) + (v26 * (v43 - v21))) <= 0) ^ v35)) if arg8 else v29):
                        break
                    break
                while True:  # $label100
                    while True:  # $label99
                        while True:  # $label98
                            if (v12 == v13):
                                arg8 = (v15 > v16)
                                v13 = (v15 if (v15 > v16) else v16)
                                v21 = (v16 if arg8 else v15)
                                if ((v16 if arg8 else v15) > arg0):
                                    break
                                if (arg0 > v13):
                                    break
                                arg8 = (arg1 - v12)
                                break
                            arg8 = 0
                            if (v15 != v16):
                                break
                            arg8 = (arg0 - v15)
                            arg8 = ((arg0 - v15) * arg8)
                            v16 = (v12 > v13)
                            v21 = (v12 if (v12 > v13) else v13)
                            v16 = (v13 if v16 else v12)
                            if not (((v12 if (v12 > v13) else v13) >= arg1) & (arg1 >= (v13 if v16 else v12))):
                                v26 = (arg1 - v13)
                                v26 = (((arg1 - v13) * v26) + arg8)
                                v24 = (arg1 - v12)
                                arg8 = (arg8 + ((arg1 - v12) * v24))
                                arg8 = ((((arg1 - v13) * v26) + arg8) if (u32(arg8) > u32(v26)) else (arg8 + ((arg1 - v12) * v24)))
                            v15 = (arg2 - v15)
                            v15 = ((arg2 - v15) * v15)
                            if ((arg3 <= v21) & (arg3 >= v16)):
                                break
                            v13 = (arg3 - v13)
                            v13 = (((arg3 - v13) * v13) + v15)
                            v12 = (arg3 - v12)
                            v12 = (v15 + ((arg3 - v12) * v12))
                            break
                            break
                        arg8 = (arg1 - v12)
                        arg8 = ((arg1 - v12) * arg8)
                        v26 = (arg0 - v16)
                        v26 = (((arg1 - v12) * arg8) + ((arg0 - v16) * v26))
                        v24 = (arg0 - v15)
                        arg8 = (arg8 + ((arg0 - v15) * v24))
                        break
                    arg8 = ((((arg1 - v12) * arg8) + ((arg0 - v16) * v26)) if (u32(arg8) > u32(v26)) else (arg8 + ((arg0 - v15) * v24)))
                    while True:  # $label101
                        if (arg2 < v21):
                            break
                        if (arg2 > v13):
                            break
                        v12 = (arg3 - v12)
                        break
                        break
                    v12 = (arg3 - v12)
                    v12 = ((arg3 - v12) * v12)
                    v13 = (arg2 - v16)
                    v13 = (((arg3 - v12) * v12) + ((arg2 - v16) * v13))
                    v15 = (arg2 - v15)
                    v12 = (v12 + ((arg2 - v15) * v15))
                    break
                v12 = ((((arg3 - v12) * v12) + ((arg2 - v16) * v13)) if (u32(v12) > u32(v13)) else (v12 + ((arg2 - v15) * v15)))
                v12 = (v12 < v30)
                v30 = (((((arg3 - v12) * v12) + ((arg2 - v16) * v13)) if (u32(v12) > u32(v13)) else (v12 + ((arg2 - v15) * v15))) if (v12 < v30) else v30)
                v19 = (arg4 if v12 else v19)
                arg8 = (arg8 < v27)
                v27 = (arg8 if (arg8 < v27) else v27)
                v31 = (arg4 if arg8 else v31)
                break
            if (u32(v20) < u32(v40)):
                continue
            break
        v20 = 0
        if (v30 == 2147483647):
            break
        v20 = (v19 != v31)
        if (v19 == v31):
            break
        if arg11:
            break
        v15 = ((v19 << 2) + 59200)
        v12 = load32(((v19 << 2) + 59200))
        v16 = load32(v15 + 8)
        arg4 = load32(((((v19 + 4) % v18) << 2) + 59200))
        v22 = ((v31 + 4) % v18)
        arg8 = load32(((((v31 + 4) % v18) << 2) + 59200))
        v14 = ((v31 << 2) + 59200)
        arg11 = load32(((v31 << 2) + 59200))
        v20 = 0
        while True:  # $label104
            v13 = load32(v15 + 4)
            v15 = load32(((((v19 + 5) % v18) << 2) + 59200))
            if (load32(v15 + 4) == load32(((((v19 + 5) % v18) << 2) + 59200))):
                while True:  # $label103
                    if ((arg4 if (arg4 < v12) else v12) > arg2):
                        break
                    if ((v12 if (arg4 < v12) else arg4) < arg2):
                        break
                    arg2 = (arg2 - v12)
                    arg2 = (arg2 >> 31)
                    break
                    break
                while True:  # $label105
                    if (arg4 >= v12):
                        break
                    if (arg2 >= arg4):
                        break
                    break
                    break
                break
            if (arg4 != v12):
                break
            while True:  # $label106
                if ((v15 if (v13 > v15) else v13) > arg3):
                    break
                if ((v13 if (v13 > v15) else v15) < arg3):
                    break
                arg2 = (arg3 - v13)
                arg2 = (arg2 >> 31)
                break
                break
            while True:  # $label107
                if (v13 <= v15):
                    break
                if (arg3 >= v15):
                    break
                break
                break
            break
        arg4 = ((((v15 - v13) if (arg3 > v15) else 0) if (v13 < v15) else 0) + v16)
        while True:  # $label109
            arg3 = load32(v14 + 4)
            arg2 = load32(((((v31 + 5) % v18) << 2) + 59200))
            if (load32(v14 + 4) == load32(((((v31 + 5) % v18) << 2) + 59200))):
                while True:  # $label108
                    if ((arg8 if (arg8 < arg11) else arg11) > arg0):
                        break
                    if ((arg11 if (arg8 < arg11) else arg8) < arg0):
                        break
                    arg2 = (arg0 - arg11)
                    arg2 = (arg2 >> 31)
                    break
                    break
                while True:  # $label110
                    if (arg8 >= arg11):
                        break
                    if (arg0 >= arg8):
                        break
                    break
                    break
                break
            if (arg8 != arg11):
                break
            while True:  # $label111
                if ((arg2 if (arg2 < arg3) else arg3) > arg1):
                    break
                if ((arg3 if (arg2 < arg3) else arg2) < arg1):
                    break
                arg2 = (arg1 - arg3)
                arg2 = (arg2 >> 31)
                break
                break
            while True:  # $label112
                if (arg2 >= arg3):
                    break
                if (arg1 >= arg2):
                    break
                break
                break
            break
        arg2 = ((((arg2 - arg3) if (arg1 > arg2) else 0) if (arg2 > arg3) else 0) + load32(((v31 << 2) + 59208)))
        arg2 = (arg2 - arg4)
        arg3 = ((((arg1 - arg3) ^ (arg2 >> 31)) - arg2) if ((arg2 - arg4) < 0) else (((arg3 - arg2) != ((((arg2 - arg3) if (arg1 > arg2) else 0) if (arg2 > arg3) else 0) + load32(((v31 << 2) + 59208)))) << 2))
        arg3 = (arg2 >> 31)
        arg2 = ((arg2 ^ (arg2 >> 31)) - arg3)
        arg2 = (v33 - arg2)
        arg2 = (arg2 >> 31)
        v15 = (((((arg1 - arg3) ^ (arg2 >> 31)) - arg2) if ((arg2 - arg4) < 0) else (((arg3 - arg2) != ((((arg2 - arg3) if (arg1 > arg2) else 0) if (arg2 > arg3) else 0) + load32(((v31 << 2) + 59208)))) << 2)) if v34 else (arg3 if (u32(((arg2 ^ (arg2 >> 31)) - arg3)) < u32((((v33 - arg2) ^ (arg2 >> 31)) - arg2))) else (0 - arg3)))
        if not (((((arg1 - arg3) ^ (arg2 >> 31)) - arg2) if ((arg2 - arg4) < 0) else (((arg3 - arg2) != ((((arg2 - arg3) if (arg1 > arg2) else 0) if (arg2 > arg3) else 0) + load32(((v31 << 2) + 59208)))) << 2)) if v34 else (arg3 if (u32(((arg2 ^ (arg2 >> 31)) - arg3)) < u32((((v33 - arg2) ^ (arg2 >> 31)) - arg2))) else (0 - arg3))):
            break
        while True:  # $label118
            while True:  # $label119
                while True:  # $label117
                    while True:  # $label113
                        arg2 = ((v19 << 2) + 59200)
                        arg3 = load32(((v19 << 2) + 59200) + 12)
                        if (load32(((v19 << 2) + 59200) + 12) > 8):
                            break
                        while True:  # $label114
                            arg4 = (v12 - arg0)
                            arg4 = (arg4 >> 31)
                            arg4 = (((v12 - arg0) ^ (arg4 >> 31)) - arg4)
                            arg2 = load32(arg2 + 4)
                            arg8 = (load32(arg2 + 4) - arg1)
                            arg8 = (arg8 >> 31)
                            arg8 = (((load32(arg2 + 4) - arg1) ^ (arg8 >> 31)) - arg8)
                            if (u32(((((v12 - arg0) ^ (arg4 >> 31)) - arg4) if (u32(arg4) > u32(arg8)) else (((load32(arg2 + 4) - arg1) ^ (arg8 >> 31)) - arg8))) < u32(56)):
                                break
                            if (v19 == v31):
                                break
                            if (v19 == v22):
                                break
                            arg4 = (v19 - v31)
                            arg4 = (arg4 >> 31)
                            arg4 = (((v19 - v31) ^ (arg4 >> 31)) - arg4)
                            if ((((v19 - v31) ^ (arg4 >> 31)) - arg4) == 4):
                                break
                            if (arg4 != v39):
                                break
                            break
                        v20 = ((arg0 << 8) | 128)
                        arg4 = (arg3 << 2)
                        v25 = load32(((arg3 << 2) + 9264))
                        v30 = (load32(((arg3 << 2) + 9264)) + (((((37449 & 0xFFFFFFFF) >> arg3) & 1) + v12) << 8))
                        v21 = (((arg0 << 8) | 128) - (load32(((arg3 << 2) + 9264)) + (((((37449 & 0xFFFFFFFF) >> arg3) & 1) + v12) << 8)))
                        v13 = ((arg1 << 8) | 128)
                        v33 = load32((arg4 + 9344))
                        v32 = (load32((arg4 + 9344)) + (((((3591 & 0xFFFFFFFF) >> arg3) & 1) + arg2) << 8))
                        v27 = (((arg1 << 8) | 128) - (load32((arg4 + 9344)) + (((((3591 & 0xFFFFFFFF) >> arg3) & 1) + arg2) << 8)))
                        arg3 = (v19 - v15)
                        v26 = ((v18 if (arg3 < 0) else (0 - (v18 if ((v19 - v15) >= v18) else 0))) + arg3)
                        arg4 = ((v18 if (arg3 < 0) else (0 - (v18 if ((v19 - v15) >= v18) else 0))) + arg3)
                        arg8 = load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((v19 - v15) >= v18) else 0))) + arg3) << 2) + 59200))
                        while True:  # $label115
                            arg3 = (arg4 + v15)
                            arg3 = ((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3)
                            arg11 = ((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200)
                            v14 = load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)
                            v17 = (v14 << 2)
                            v16 = ((((((3591 & 0xFFFFFFFF) >> load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)) & 1) + load32(((v14 << 2) + 9344))) + load32(arg11 + 4)) << 8)
                            arg11 = load32(arg11)
                            v14 = ((load32(arg11) + (load32((v17 + 9264)) + (((37449 & 0xFFFFFFFF) >> v14) & 1))) << 8)
                            v17 = (((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)) & 1) + load32(((v14 << 2) + 9344))) + load32(arg11 + 4)) << 8)) * v21) + ((((load32(arg11) + (load32((v17 + 9264)) + (((37449 & 0xFFFFFFFF) >> v14) & 1))) << 8) - v20) * v27))
                            v24 = ((arg4 << 2) + 59200)
                            v23 = load32(((arg4 << 2) + 59200) + 12)
                            v29 = (v23 << 2)
                            v24 = ((((((3591 & 0xFFFFFFFF) >> load32(((arg4 << 2) + 59200) + 12)) & 1) + load32(((v23 << 2) + 9344))) + load32(v24 + 4)) << 8)
                            arg8 = (((load32((v29 + 9264)) + (((37449 & 0xFFFFFFFF) >> v23) & 1)) + arg8) << 8)
                            v23 = (((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((arg4 << 2) + 59200) + 12)) & 1) + load32(((v23 << 2) + 9344))) + load32(v24 + 4)) << 8)) * v21) + (((((load32((v29 + 9264)) + (((37449 & 0xFFFFFFFF) >> v23) & 1)) + arg8) << 8) - v20) * v27))
                            v17 = (v14 - arg8)
                            v23 = (v16 - v24)
                            arg8 = (((v14 - arg8) * (v16 - v13)) + ((v16 - v24) * (v20 - v14)))
                            v16 = (((v16 - v32) * v17) + (v23 * (v30 - v14)))
                            v16 = (((((((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)) & 1) + load32(((v14 << 2) + 9344))) + load32(arg11 + 4)) << 8)) * v21) + ((((load32(arg11) + (load32((v17 + 9264)) + (((37449 & 0xFFFFFFFF) >> v14) & 1))) << 8) - v20) * v27)) != 0) & (((((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((arg4 << 2) + 59200) + 12)) & 1) + load32(((v23 << 2) + 9344))) + load32(v24 + 4)) << 8)) * v21) + (((((load32((v29 + 9264)) + (((37449 & 0xFFFFFFFF) >> v23) & 1)) + arg8) << 8) - v20) * v27)) <= 0) ^ (v17 > 0))) if v23 else not v17) | ((((((v14 - arg8) * (v16 - v13)) + ((v16 - v24) * (v20 - v14))) != 0) & (((((v16 - v32) * v17) + (v23 * (v30 - v14))) <= 0) ^ (arg8 > 0))) if v16 else not arg8))
                            if ((((((((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)) & 1) + load32(((v14 << 2) + 9344))) + load32(arg11 + 4)) << 8)) * v21) + ((((load32(arg11) + (load32((v17 + 9264)) + (((37449 & 0xFFFFFFFF) >> v14) & 1))) << 8) - v20) * v27)) != 0) & (((((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((arg4 << 2) + 59200) + 12)) & 1) + load32(((v23 << 2) + 9344))) + load32(v24 + 4)) << 8)) * v21) + (((((load32((v29 + 9264)) + (((37449 & 0xFFFFFFFF) >> v23) & 1)) + arg8) << 8) - v20) * v27)) <= 0) ^ (v17 > 0))) if v23 else not v17) | ((((((v14 - arg8) * (v16 - v13)) + ((v16 - v24) * (v20 - v14))) != 0) & (((((v16 - v32) * v17) + (v23 * (v30 - v14))) <= 0) ^ (arg8 > 0))) if v16 else not arg8)) == 1):
                                v14 = (arg4 != v31)
                                arg8 = arg11
                                arg4 = arg3
                                if v14:
                                    continue
                            break
                        if (v16 ^ 1):
                            break
                        while True:  # $label116
                            if (not v19 & v34):
                                arg8 = v12
                                v12 = arg2
                                break
                            arg3 = ((v26 << 2) + 59200)
                            arg4 = load32(((v26 << 2) + 59200))
                            arg8 = ((-1 if (arg4 < v12) else (load32(((v26 << 2) + 59200)) != v12)) + v12)
                            arg3 = load32(arg3 + 4)
                            v12 = ((-1 if (arg2 > arg3) else (load32(arg3 + 4) != arg2)) + arg2)
                            store8(arg10, (((((-1 if (arg4 < v12) else (load32(((v26 << 2) + 59200)) != v12)) + v12) - (v12 + v25)) + ((((-1 if (arg2 > arg3) else (load32(arg3 + 4) != arg2)) + arg2) - (arg2 + v33)) * 3)) + 4))
                            break
                        store32(arg9, ((v12 << 16) + arg8))
                        if (arg0 != arg8):
                            break
                        if (arg1 != v12):
                            break
                        store32(arg9, 0)
                        break
                        break
                    if (v19 == v31):
                        v20 = 0
                        break
                    else:
                        arg2 = (((v19 if v19 else v18) if (v15 < 0) else v19) + v15)
                        v19 = ((((v19 if v19 else v18) if (v15 < 0) else v19) + v15) if (arg2 != v18) else 0)
                        v12 = load32(((((((v19 if v19 else v18) if (v15 < 0) else v19) + v15) if (arg2 != v18) else 0) << 2) + 59200))
                        continue
                    raise Unreachable()
                    break
                break
            break
        v20 = 1
        break
    G.global0 = (v36 + 16)
    return v20

# ----------------------------------------------------------
# $func178
# ----------------------------------------------------------
def func178(arg0):
    v8 = load32(arg0 + 44)
    v11 = (load32(arg0 + 44) - 262)
    v2 = load32(arg0 + 116)
    while True:  # $label10
        v7 = load32(arg0 + 108)
        v6 = (load32(arg0 + 60) - (v2 + load32(arg0 + 108)))
        if (u32((v11 + load32(arg0 + 44))) <= u32(v7)):
            v1 = load32(arg0 + 56)
            store32(arg0 + 112, (load32(arg0 + 112) - v8))
            v7 = (load32(arg0 + 108) - v8)
            store32(arg0 + 108, (load32(arg0 + 108) - v8))
            store32(arg0 + 92, (load32(arg0 + 92) - v8))
            if (u32(v7) < u32(load32(arg0 + 5812))):
                store32(arg0 + 5812, v7)
            v1 = load32(arg0 + 76)
            v5 = (load32(arg0 + 76) - 1)
            v4 = (load32(arg0 + 68) + (v1 << 1))
            v3 = load32(arg0 + 44)
            v2 = 0
            v9 = (v1 & 3)
            if (v1 & 3):
                while True:  # $label0
                    v4 = (v4 - 2)
                    v10 = load16u(v4)
                    v12 = (load16u(v4) - v3)
                    store16((v4 - 2), ((load16u(v4) - v3) if (u32(v10) >= u32(v12)) else 0))
                    v1 = (v1 - 1)
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v9):
                        continue
                    break
            if (u32(v5) >= u32(3)):
                while True:  # $label1
                    v2 = (v4 - 2)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 2), ((load16u(v2) - v3) if (u32(v2) >= u32(v5)) else 0))
                    v2 = (v4 - 4)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 4), ((load16u(v2) - v3) if (u32(v2) >= u32(v5)) else 0))
                    v2 = (v4 - 6)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 6), ((load16u(v2) - v3) if (u32(v2) >= u32(v5)) else 0))
                    v4 = (v4 - 8)
                    v2 = load16u(v4)
                    v5 = (load16u(v4) - v3)
                    store16((v4 - 8), ((load16u(v4) - v3) if (u32(v2) >= u32(v5)) else 0))
                    v1 = (v1 - 4)
                    if (v1 - 4):
                        continue
                    break
            v4 = (load32(arg0 + 64) + (v3 << 1))
            v2 = 0
            v1 = v3
            v5 = (v3 & 3)
            if (v3 & 3):
                while True:  # $label2
                    v4 = (v4 - 2)
                    v9 = load16u(v4)
                    v10 = (load16u(v4) - v3)
                    store16((v4 - 2), ((load16u(v4) - v3) if (u32(v9) >= u32(v10)) else 0))
                    v1 = (v1 - 1)
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v5):
                        continue
                    break
            if (u32((v3 - 1)) >= u32(3)):
                while True:  # $label3
                    v2 = (v4 - 2)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 2), ((load16u(v2) - v3) if (u32(v2) >= u32(v5)) else 0))
                    v2 = (v4 - 4)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 4), ((load16u(v2) - v3) if (u32(v2) >= u32(v5)) else 0))
                    v2 = (v4 - 6)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 6), ((load16u(v2) - v3) if (u32(v2) >= u32(v5)) else 0))
                    v4 = (v4 - 8)
                    v2 = load16u(v4)
                    v5 = (load16u(v4) - v3)
                    store16((v4 - 8), ((load16u(v4) - v3) if (u32(v2) >= u32(v5)) else 0))
                    v1 = (v1 - 4)
                    if (v1 - 4):
                        continue
                    break
            v6 = (v6 + v8)
        while True:  # $label4
            v1 = load32(arg0)
            v4 = load32(load32(arg0) + 4)
            if not load32(load32(arg0) + 4):
                break
            v2 = load32(arg0 + 116)
            v3 = (v4 if (u32(v4) < u32(v6)) else v6)
            if (v4 if (u32(v4) < u32(v6)) else v6):
                v6 = load32(arg0 + 56)
                store32(v1 + 4, (v4 - v3))
                v4 = func35(((v6 + v7) + v2), load32(v1), v3)
                while True:  # $label7
                    while True:  # $label6
                        while True:  # $label5
                            # br_table (load32(load32(v1 + 28) + 24) - 1)
                            break
                            break
                        store32(v1 + 48, func89(load32(v1 + 48), v4, v3))
                        break
                        break
                    store32(v1 + 48, func43(load32(v1 + 48), v4, v3))
                    break
                store32(v1, (load32(v1) + v3))
                store32(v1 + 8, (load32(v1 + 8) + v3))
            else:
            v2 = (v2 + v3)
            store32(load32(arg0 + 116) + 116, (v2 + v3))
            while True:  # $label8
                v4 = load32(arg0 + 5812)
                if (u32((load32(arg0 + 5812) + v2)) < u32(3)):
                    break
                v7 = load32(arg0 + 56)
                v3 = (load32(arg0 + 108) - v4)
                v1 = (load32(arg0 + 56) + (load32(arg0 + 108) - v4))
                v6 = load8u((load32(arg0 + 56) + (load32(arg0 + 108) - v4)))
                store32(arg0 + 72, load8u((load32(arg0 + 56) + (load32(arg0 + 108) - v4))))
                v5 = load32(arg0 + 84)
                v6 = load32(arg0 + 88)
                v1 = (load32(arg0 + 84) & (load8u(v1 + 1) ^ (v6 << load32(arg0 + 88))))
                store32(arg0 + 72, (load32(arg0 + 84) & (load8u(v1 + 1) ^ (v6 << load32(arg0 + 88)))))
                while True:  # $label9
                    if not v4:
                        break
                    v1 = ((load8u((v3 + v7) + 2) ^ (v1 << v6)) & v5)
                    store32(arg0 + 72, ((load8u((v3 + v7) + 2) ^ (v1 << v6)) & v5))
                    v9 = (load32(arg0 + 68) + (v1 << 1))
                    store16((load32(arg0 + 64) + ((load32(arg0 + 52) & v3) << 1)), load16u((load32(arg0 + 68) + (v1 << 1))))
                    store16(v9, v3)
                    v4 = (v4 - 1)
                    store32(arg0 + 5812, (v4 - 1))
                    v3 = (v3 + 1)
                    if (u32((v2 + v4)) > u32(2)):
                        continue
                    break
                break
            if (u32(v2) > u32(261)):
                break
            if load32(load32(arg0) + 4):
                continue
            break
        break
    while True:  # $label11
        v4 = load32(arg0 + 60)
        v1 = load32(arg0 + 5824)
        if (u32(load32(arg0 + 60)) <= u32(load32(arg0 + 5824))):
            break
        while True:  # $label12
            v3 = (load32(arg0 + 116) + load32(arg0 + 108))
            if (u32((load32(arg0 + 116) + load32(arg0 + 108))) > u32(v1)):
                v1 = (v4 - v3)
                v1 = (258 if (u32(v1) >= u32(258)) else (v4 - v3))
                func98((load32(arg0 + 56) + v3), 0, (258 if (u32(v1) >= u32(258)) else (v4 - v3)))
                break
            v3 = (v3 + 258)
            if (u32((v3 + 258)) <= u32(v1)):
                break
            v3 = (v3 - v1)
            v1 = (v4 - v1)
            v1 = ((v3 - v1) if (u32(v1) > u32(v3)) else (v4 - v1))
            func98((load32(arg0 + 56) + v1), 0, ((v3 - v1) if (u32(v1) > u32(v3)) else (v4 - v1)))
            break
        store32((v1 + v3) + 5824, (load32(arg0 + 5824) + v1))
        break
    return arg0

# ----------------------------------------------------------
# $func179
# ----------------------------------------------------------
def func179(arg0, arg1):
    while True:  # $label6
        while True:  # $label0
            if not arg0:
                break
            if not arg1:
                break
            if (G.global4 if (load32(arg0 + 52) & 64) else 0):
                break
            v2 = func252(1, 208)
            if not func252(1, 208):
                break
            v3 = load32(52364)
            store32(52364, (load32(52364) + 1))
            store32(v2, v3)
            store32(v2 + 4, load32(arg0 + 32))
            store32(v2 + 168, load32(arg0 + 56))
            store32(v2 + 164, load32(arg0 + 52))
            store32(v2 + 172, load32(arg0 + 60))
            store32(v2 + 196, load32(arg0 + 84))
            store32(v2 + 200, load32(arg0 + 88))
            while True:  # $label2
                while True:  # $label1
                    v5 = (v2 + 112)
                    v3 = arg0
                    if (((v2 + 112) ^ arg0) & 3):
                        v4 = load8u(v3)
                        break
                    if (v3 & 3):
                        while True:  # $label3
                            v4 = load8u(v3)
                            store8(v5, load8u(v3))
                            if not v4:
                                break
                            v5 = (v5 + 1)
                            v3 = (v3 + 1)
                            if ((v3 + 1) & 3):
                                continue
                            break
                    v4 = load32(v3)
                    if (((load32(v3) ^ -1) & (v4 - 16843009)) & -2139062144):
                        break
                    while True:  # $label4
                        store32(v5, v4)
                        v4 = load32(v3 + 4)
                        v5 = (v5 + 4)
                        v3 = (v3 + 4)
                        if not (((v4 - 16843009) & (v4 ^ -1)) & -2139062144):
                            continue
                        break
                    break
                store8(v5, v4)
                if not (v4 & 255):
                    break
                while True:  # $label5
                    v4 = load8u(v3 + 1)
                    store8(v5 + 1, load8u(v3 + 1))
                    v5 = (v5 + 1)
                    v3 = (v3 + 1)
                    if v4:
                        continue
                    break
                break
            store32(v2 + 152, load32(arg0 + 40))
            store32(v2 + 148, load32(arg0 + 36))
            store32(v2 + 156, load32(arg0 + 44))
            store32(v2 + 160, load32(arg0 + 48))
            arg1 = func121(arg1)
            store32(v2 + 8, func121(arg1))
            if not arg1:
                func246(v2)
                return
            arg1 = load32(arg0 + 64)
            if load32(arg0 + 64):
                arg1 = func121(arg1)
                store32(v2 + 176, func121(arg1))
                if not arg1:
                    break
            arg1 = load32(arg0 + 68)
            if load32(arg0 + 68):
                arg1 = func121(arg1)
                store32(v2 + 180, func121(arg1))
                if not arg1:
                    break
            arg1 = load32(arg0 + 72)
            if load32(arg0 + 72):
                arg1 = func121(arg1)
                store32(v2 + 184, func121(arg1))
                if not arg1:
                    break
            arg1 = load32(arg0 + 80)
            if load32(arg0 + 80):
                arg1 = func121(arg1)
                store32(v2 + 192, func121(arg1))
                if not arg1:
                    break
            v5 = load32(arg0 + 76)
            if load32(arg0 + 76):
                arg1 = 0
                while True:  # $label7
                    arg0 = arg1
                    arg1 = (arg1 + 1)
                    if load32((v5 + (arg0 << 2))):
                        continue
                    break
                v3 = func252(1, ((arg0 << 2) + 4))
                if not func252(1, ((arg0 << 2) + 4)):
                    break
                if arg0:
                    arg1 = 0
                    while True:  # $label9
                        v4 = (arg1 << 2)
                        v4 = func121(load32((v4 + v5)))
                        store32((v3 + (arg1 << 2)), func121(load32((v4 + v5))))
                        if not v4:
                            if arg1:
                                arg0 = 0
                                while True:  # $label8
                                    arg0 = (arg0 + 1)
                                    if ((arg0 + 1) != arg1):
                                        continue
                                    break
                            break
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != arg0):
                            continue
                        break
                store32((v3 + (arg0 << 2)), 0)
                store32(v2 + 188, v3)
            a_m(v2)
            break
        return
        break
    func246(v2)

# ----------------------------------------------------------
# $func180
# ----------------------------------------------------------
def func180(arg0, arg1):
    while True:  # $label1
        while True:  # $label0
            if (load32(38604) == arg1):
                break
            if (load32(38608) == arg1):
                break
            if (load32(38612) == arg1):
                break
            if (load32(38616) == arg1):
                break
            if (load32(38624) == arg1):
                break
            if (load32(38628) == arg1):
                break
            if (load32(38632) == arg1):
                break
            if (load32(39056) != arg1):
                break
            break
        arg1 = (arg0 + 281808)
        v2 = (load32(9561068) << 2)
        v3 = (load32(9561064) << 2)
        v4 = (load32(9561060) << 2)
        v5 = (load32(9561056) << 2)
        v6 = (load32(9561052) << 2)
        v7 = (load32(9561048) << 2)
        v8 = (load32(9561044) << 2)
        v9 = (load32(9561040) << 2)
        arg0 = (arg0 + 282828)
        return ((load32(((arg0 + 281808) + (load32(9561068) << 2))) + ((load32((arg1 + (load32(9561064) << 2))) + ((load32((arg1 + (load32(9561060) << 2))) + ((load32((arg1 + (load32(9561056) << 2))) + ((load32((arg1 + (load32(9561052) << 2))) + ((load32((arg1 + (load32(9561048) << 2))) + ((load32((arg1 + (load32(9561044) << 2))) + (load32((arg1 + (load32(9561040) << 2))) + load32(((arg0 + 282828) + v9)))) + load32((arg0 + v8)))) + load32((arg0 + v7)))) + load32((arg0 + v6)))) + load32((arg0 + v5)))) + load32((arg0 + v4)))) + load32((arg0 + v3)))) + load32((arg0 + v2)))
        break
    arg0 = (arg0 + (arg1 << 2))
    return (load32(((arg0 + (arg1 << 2)) + 282828)) + load32((arg0 + 281808)))

# ----------------------------------------------------------
# $func181
# ----------------------------------------------------------
def func181(arg0, arg1, arg2):
    while True:  # $label0
        v4 = load32(arg0 + 281796)
        if not load32(arg0 + 281796):
            v3 = func26(16)
            store32(func26(16) + 4, 20)
            store32(v3, func26(80))
            store64(v3 + 8, 85899345920)
            store32(arg0 + 281796, v3)
            v8 = (v3 + 8)
            v6 = load32(v3)
            break
        v8 = (v4 + 8)
        v3 = load32(v4 + 8)
        v5 = load32(v4 + 4)
        if (load32(v4 + 8) != load32(v4 + 4)):
            v5 = v3
            v3 = v4
            v6 = load32(v4)
            break
        v3 = (load32(v4 + 12) + v5)
        store32(v4 + 4, (load32(v4 + 12) + v5))
        v7 = load32(v4)
        v6 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
        if v5:
            # TODO: memory.copy
        v3 = v4
        if v7:
            v5 = load32(v4 + 8)
            v3 = load32(arg0 + 281796)
        store32(v4, v6)
        break
    store32(v8, (v5 + 1))
    store32((v6 + (v5 << 2)), arg1)
    while True:  # $label1
        arg0 = load32(v3 + 8)
        if (load32(v3 + 8) != load32(v3 + 4)):
            v5 = load32(v3)
            break
        arg1 = (load32(v3 + 12) + arg0)
        store32(v3 + 4, (load32(v3 + 12) + arg0))
        v4 = load32(v3)
        v5 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if arg0:
            # TODO: memory.copy
        if v4:
            arg0 = load32(v3 + 8)
        store32(v3, v5)
        break
    store32(v3 + 8, (arg0 + 1))
    store32((v5 + (arg0 << 2)), arg2)

# ----------------------------------------------------------
# $func182
# ----------------------------------------------------------
def func182():
    v0 = 3
    if (u32(load32(9671136)) > u32(3)):
        while True:  # $label0
            v0 = (v0 + 1)
            if (u32((v0 + 1)) < u32(load32(9671136))):
                continue
            break
    while True:  # $label1
        v6 = load32(PLAYER_COUNT)
        if not load32(PLAYER_COUNT):
            break
        v4 = load32(PLAYERS)
        while True:  # $label2
            v0 = 0
            while True:  # $label3
                v2 = (v4 + (v5 * 286704))
                v3 = ((v4 + (v5 * 286704)) + (v0 << 2))
                v1 = load32((((v4 + (v5 * 286704)) + (v0 << 2)) + 285656))
                if load32((((v4 + (v5 * 286704)) + (v0 << 2)) + 285656)):
                    store32(v1 + 8, 0)
                v1 = load32((v3 + 284636))
                if load32((v3 + 284636)):
                    store32(v1 + 8, 0)
                v1 = (v0 | 1)
                if ((v0 | 1) == 255):
                    v5 = (v5 + 1)
                    if ((v5 + 1) != v6):
                        continue
                    break
                v3 = (v2 + (v1 << 2))
                v1 = load32(((v2 + (v1 << 2)) + 285656))
                if load32(((v2 + (v1 << 2)) + 285656)):
                    store32(v1 + 8, 0)
                v1 = load32((v3 + 284636))
                if load32((v3 + 284636)):
                    store32(v1 + 8, 0)
                v0 = (v0 + 2)
                continue
                break
            raise Unreachable()
            break
        raise Unreachable()
        break
    v4 = load32(ENTITIES)
    if load32(ENTITIES):
        v3 = (v4 - 4)
        v1 = load32((v4 - 4))
        if load32((v4 - 4)):
            v0 = (v4 + (v1 * 132))
            while True:  # $label4
                v1 = (v0 - 132)
                v2 = load32((v0 - 132))
                if load32((v0 - 132)):
                    store32((v0 - 128), v2)
                v0 = v1
                if (v1 != v4):
                    continue
                break
        store32(ENTITIES, 0)
    store32(9671132, 10000)
    v1 = func26(1320004)
    store32(func26(1320004), 10000)
    v3 = (v1 + 1320004)
    v1 = (v1 + 4)
    v0 = (v1 + 4)
    while True:  # $label5
        # TODO: memory.fill
        v2 = func26(4)
        store32(v0 + 4, func26(4))
        store32(v0, v2)
        store32(v0 + 8, (v2 + 4))
        v0 = (v0 + 132)
        if ((v0 + 132) != v3):
            continue
        break
    store32(ENTITIES, v1)
    store64(9671136, 42949672960003)
    store32(9163776, 4)
    store32(9684796, 0)
    store32(load32(9681936) + 8, 0)
    store32(9299880, 0)

# ----------------------------------------------------------
# $func183
# ----------------------------------------------------------
def func183(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    v13 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v9 = 1
    while True:  # $label0
        v20 = load8u(arg0 + 125)
        if (load8u(arg0 + 125) == 3):
            break
        v9 = load32(((arg1 + (arg2 * 36)) + 269376))
        v9 = (load32(((arg1 + (arg2 * 36)) + 269376)) if v9 else 100)
        v12 = ((arg2 * 404) + ENTITY_TYPES)
        store32(v13, (((load32(((arg1 + (arg2 * 36)) + 269376)) if v9 else 100) * load32(((arg2 * 404) + ENTITY_TYPES) + 68)) // 100))
        store32(v13 + 4, ((load32(v12 + 72) * v9) // 100))
        store32(v13 + 8, ((load32(v12 + 76) * v9) // 100))
        store32(v13 + 12, ((load32(v12 + 80) * v9) // 100))
        while True:  # $label32
            while True:  # $label2
                if not arg3:
                    while True:  # $label1
                        if (load32(v12 + 264) != 3):
                            break
                        if arg5:
                            break
                        v9 = 0
                        arg3 = (arg1 + (arg2 << 2))
                        if load32(((arg1 + (arg2 << 2)) + 282828)):
                            break
                        if load32((arg3 + 281808)):
                            break
                        break
                    arg7 = load32(arg0 + 20)
                    if not load32(arg0 + 20):
                        arg7 = func26(16)
                        store32(func26(16) + 4, 16)
                        store32(arg7, func26(64))
                        store64(arg7 + 8, 68719476736)
                        store32(arg0 + 20, arg7)
                        break
                    if not arg4:
                        break
                    if not arg6:
                        break
                    arg3 = load32(arg7 + 8)
                    if not load32(arg7 + 8):
                        break
                    v11 = (arg2 + 2147483647)
                    v10 = load32(arg7)
                    v9 = 0
                    arg6 = 0
                    while True:  # $label3
                        if (load32((v10 + (arg6 << 2))) == v11):
                            break
                        arg6 = (arg6 + 1)
                        if (arg3 != (arg6 + 1)):
                            continue
                        break
                    break
                arg5 = load32(arg0 + 20)
                if not load32(arg0 + 20):
                    v9 = 0
                    break
                while True:  # $label4
                    arg4 = load32(arg5 + 8)
                    if not load32(arg5 + 8):
                        arg8 = 0
                        v11 = -1
                        break
                    v14 = (arg4 & 1)
                    arg6 = load32(arg5)
                    while True:  # $label5
                        if (arg4 == 1):
                            v11 = -1
                            v9 = 0
                            arg8 = 0
                            break
                        v16 = (arg4 & -2)
                        v11 = -1
                        v9 = 0
                        arg8 = 0
                        arg4 = 0
                        while True:  # $label6
                            v15 = (v9 | 1)
                            v10 = load32((arg6 + ((v9 | 1) << 2)))
                            v17 = (u32(load32((arg6 + ((v9 | 1) << 2)))) > u32(2147483646))
                            v12 = load32((arg6 + (v9 << 2)))
                            v20 = (u32(load32((arg6 + (v9 << 2)))) > u32(2147483646))
                            v12 = (((v12 - 2147483647) if v20 else v12) == arg2)
                            v10 = (((v10 - 2147483647) if v17 else v10) == arg2)
                            arg8 = ((u32(load32((arg6 + ((v9 | 1) << 2)))) > u32(2147483646)) if (((v10 - 2147483647) if v17 else v10) == arg2) else ((u32(load32((arg6 + (v9 << 2)))) > u32(2147483646)) if (((v12 - 2147483647) if v20 else v12) == arg2) else arg8))
                            v11 = (v15 if v10 else (v9 if v12 else v11))
                            v9 = (v9 + 2)
                            arg4 = (arg4 + 2)
                            if ((arg4 + 2) != v16):
                                continue
                            break
                        break
                    if not v14:
                        break
                    arg4 = load32((arg6 + (v9 << 2)))
                    arg6 = (u32(load32((arg6 + (v9 << 2)))) > u32(2147483646))
                    arg4 = (((arg4 - 2147483647) if arg6 else arg4) == arg2)
                    arg8 = ((u32(load32((arg6 + (v9 << 2)))) > u32(2147483646)) if (((arg4 - 2147483647) if arg6 else arg4) == arg2) else arg8)
                    v11 = (v9 if arg4 else v11)
                    break
                while True:  # $label7
                    arg4 = load32(arg1 + 281796)
                    if not load32(arg1 + 281796):
                        break
                    arg6 = load32(arg4 + 8)
                    if not load32(arg4 + 8):
                        break
                    v10 = load32(arg0 + 28)
                    v12 = load32(arg4)
                    v9 = 0
                    while True:  # $label11
                        while True:  # $label8
                            v14 = (v9 << 2)
                            if (load32((v12 + (v9 << 2))) != v10):
                                break
                            if (load32((v12 + (v14 | 4))) != arg2):
                                break
                            v10 = (arg6 - 1)
                            store32(arg4 + 8, (arg6 - 1))
                            if (u32(v9) < u32(v10)):
                                arg6 = v9
                                while True:  # $label9
                                    arg6 = (arg6 + 1)
                                    store32((v12 + (arg6 << 2)), load32((v12 + ((arg6 + 1) << 2))))
                                    v10 = load32(arg4 + 8)
                                    if (u32(arg6) < u32(load32(arg4 + 8))):
                                        continue
                                    break
                            arg6 = (v10 - 1)
                            store32(arg4 + 8, (v10 - 1))
                            if (u32(arg6) > u32(v9)):
                                while True:  # $label10
                                    v9 = (v9 + 1)
                                    store32((v12 + (v9 << 2)), load32((v12 + ((v9 + 1) << 2))))
                                    if (u32(v9) < u32(load32(arg4 + 8))):
                                        continue
                                    break
                            arg6 = ((arg1 + (arg2 << 2)) + 282828)
                            store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg6) - 1))
                            break
                            break
                        v9 = (v9 + 2)
                        if (u32((v9 + 2)) < u32(arg6)):
                            continue
                        break
                    break
                while True:  # $label12
                    v14 = ((arg2 * 404) + ENTITY_TYPES)
                    if (load32(((arg2 * 404) + ENTITY_TYPES) + 264) != 3):
                        break
                    arg6 = load32(v14 + 244)
                    if not load32(v14 + 244):
                        break
                    v17 = load32(((arg2 * 404) + ENTITY_TYPES) + 240)
                    v16 = 0
                    while True:  # $label18
                        while True:  # $label13
                            if not arg4:
                                break
                            v10 = load32(arg4 + 8)
                            if not load32(arg4 + 8):
                                break
                            v15 = load32(((load32((v17 + (v16 << 2))) * 132) + 9216080) + 4)
                            v20 = load32(arg0 + 28)
                            v12 = load32(arg4)
                            v9 = 0
                            while True:  # $label17
                                while True:  # $label14
                                    v18 = (v9 << 2)
                                    if (load32((v12 + (v9 << 2))) != v20):
                                        break
                                    if (load32((v12 + (v18 | 4))) != v15):
                                        break
                                    v10 = (v10 - 1)
                                    store32(arg4 + 8, (v10 - 1))
                                    arg6 = v9
                                    if (u32(v9) < u32(v10)):
                                        while True:  # $label15
                                            arg6 = (arg6 + 1)
                                            store32((v12 + (arg6 << 2)), load32((v12 + ((arg6 + 1) << 2))))
                                            v10 = load32(arg4 + 8)
                                            if (u32(arg6) < u32(load32(arg4 + 8))):
                                                continue
                                            break
                                    arg6 = (v10 - 1)
                                    store32(arg4 + 8, (v10 - 1))
                                    if (u32(arg6) > u32(v9)):
                                        while True:  # $label16
                                            v9 = (v9 + 1)
                                            store32((v12 + (v9 << 2)), load32((v12 + ((v9 + 1) << 2))))
                                            if (u32(v9) < u32(load32(arg4 + 8))):
                                                continue
                                            break
                                    arg6 = ((arg1 + (v15 << 2)) + 282828)
                                    store32(((arg1 + (v15 << 2)) + 282828), (load32(arg6) - 1))
                                    arg6 = load32(v14 + 244)
                                    break
                                    break
                                v9 = (v9 + 2)
                                if (u32((v9 + 2)) < u32(v10)):
                                    continue
                                break
                            break
                        v16 = (v16 + 1)
                        if (u32((v16 + 1)) < u32(arg6)):
                            continue
                        break
                    break
                while True:  # $label19
                    if (v11 == -1):
                        break
                    arg4 = ((arg1 + (arg2 << 2)) + 282828)
                    store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg4) - 1))
                    v9 = load32(arg5 + 8)
                    while True:  # $label20
                        if (load32(v14 + 264) != 3):
                            break
                        v10 = 0
                        if not v9:
                            v9 = 0
                            break
                        while True:  # $label24
                            while True:  # $label22
                                while True:  # $label21
                                    arg4 = load32((load32(arg5) + (v10 << 2)))
                                    arg4 = ((load32((load32(arg5) + (v10 << 2))) - 2147483647) if (u32(arg4) > u32(2147483646)) else arg4)
                                    arg6 = ((((load32((load32(arg5) + (v10 << 2))) - 2147483647) if (u32(arg4) > u32(2147483646)) else arg4) * 404) + ENTITY_TYPES)
                                    # br_table load32(((((load32((load32(arg5) + (v10 << 2))) - 2147483647) if (u32(arg4) > u32(2147483646)) else arg4) * 404) + ENTITY_TYPES) + 264)
                                    break
                                    break
                                v9 = 0
                                arg6 = load32(arg6 + 180)
                                v12 = load32(load32(arg6 + 180) + 68)
                                if not load32(load32(arg6 + 180) + 68):
                                    break
                                while True:  # $label23
                                    if (arg2 != load32((arg6 + (v9 << 2)) + 28)):
                                        v9 = (v9 + 1)
                                        if (v12 != (v9 + 1)):
                                            continue
                                        break
                                    break
                                v10 = (v10 - 1)
                                arg5 = load32(arg0 + 20)
                                break
                            v10 = (v10 + 1)
                            v9 = load32(arg5 + 8)
                            if (u32((v10 + 1)) < u32(load32(arg5 + 8))):
                                continue
                            break
                        break
                    arg6 = (v9 - 1)
                    store32(arg5 + 8, (v9 - 1))
                    if (u32(arg6) > u32(v11)):
                        arg3 = load32(arg5)
                        v9 = v11
                        while True:  # $label25
                            v9 = (v9 + 1)
                            store32((arg3 + (v9 << 2)), load32((arg3 + ((v9 + 1) << 2))))
                            arg6 = load32(arg5 + 8)
                            if (u32(v9) < u32(load32(arg5 + 8))):
                                continue
                            break
                    while True:  # $label30
                        while True:  # $label28
                            while True:  # $label29
                                while True:  # $label26
                                    if not arg7:
                                        break
                                    while True:  # $label27
                                        # br_table (load8u(arg0 + 125) - 4)
                                        break
                                        break
                                    if arg6:
                                        if v11:
                                            break
                                        func230(arg0)
                                        break
                                    arg3 = load32(arg0 + 44)
                                    if load32(arg0 + 44):
                                        store32((load32(9215884) + (arg3 << 4)), 0)
                                    store32(arg0 + 44, 0)
                                    func29(arg0, 1)
                                    break
                                if v11:
                                    break
                                break
                            if not (arg8 & 1):
                                break
                            # br_table (load8u(arg0 + 125) - 4)
                            break
                            break
                        if (arg8 & 1):
                            break
                        break
                    arg3 = load32(arg1 + 283848)
                    if (load32(arg1 + 283848) != 2147483647):
                        store32(arg1 + 283848, (load32(v13) + arg3))
                    arg3 = load32((arg1 + 283852))
                    if (load32((arg1 + 283852)) != 2147483647):
                        store32(arg1 + 283852, (load32(v13 + 4) + arg3))
                    arg3 = load32((arg1 + 283856))
                    if (load32((arg1 + 283856)) != 2147483647):
                        store32(arg1 + 283856, (load32(v13 + 8) + arg3))
                    arg3 = load32(v13 + 12)
                    arg4 = load32((arg1 + 283860))
                    if (load32((arg1 + 283860)) != 2147483647):
                        store32(arg1 + 283860, (arg3 + arg4))
                    arg4 = (arg1 + 281692)
                    store32((arg1 + 281692), (load32(arg4) - load32(v13)))
                    arg4 = (arg1 + 281696)
                    store32((arg1 + 281696), (load32(arg4) - load32(v13 + 4)))
                    arg4 = load32(v13 + 8)
                    arg5 = (arg1 + 281704)
                    store32((arg1 + 281704), (load32(arg5) - arg3))
                    v9 = 1
                    store8(arg1 + 286701, 1)
                    arg3 = (arg1 + 281700)
                    store32((arg1 + 281700), (load32(arg3) - arg4))
                    arg3 = load32(PLAYER_COUNT)
                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                        break
                    arg6 = (arg3 - 1)
                    arg7 = ((arg3 - 1) & 1)
                    arg1 = (load32(arg1 + 283908) * arg3)
                    arg4 = load32(PLAYERS)
                    arg5 = load32(9143016)
                    if (arg3 != 2):
                        arg3 = (arg6 & -2)
                        v10 = 0
                        while True:  # $label31
                            if load8u((arg5 + (arg1 + v9))):
                                store8((arg4 + (v9 * 286704)) + 286701, 1)
                            arg6 = (v9 + 1)
                            if load8u((arg5 + ((v9 + 1) + arg1))):
                                store8((arg4 + (arg6 * 286704)) + 286701, 1)
                            v9 = (v9 + 2)
                            v10 = (v10 + 2)
                            if ((v10 + 2) != arg3):
                                continue
                            break
                    if not arg7:
                        break
                    if not load8u((arg5 + (arg1 + v9))):
                        break
                    store8((arg4 + (v9 * 286704)) + 286701, 1)
                    break
                arg1 = ((arg2 * 404) + ENTITY_TYPES)
                if not load32(arg1 + 244):
                    break
                v9 = 0
                while True:  # $label33
                    v9 = (v9 + 1)
                    if (u32((v9 + 1)) < u32(load32(arg1 + 244))):
                        continue
                    break
                break
                break
            while True:  # $label34
                if arg4:
                    break
                arg3 = load32(arg7 + 8)
                if not load32(arg7 + 8):
                    break
                v11 = (arg2 + 2147483647)
                v10 = load32(arg7)
                v9 = 0
                arg6 = 0
                while True:  # $label35
                    if (load32((v10 + (arg6 << 2))) == v11):
                        break
                    arg6 = (arg6 + 1)
                    if ((arg6 + 1) != arg3):
                        continue
                    break
                break
            while True:  # $label36
                arg3 = load32(arg1 + 281796)
                if not load32(arg1 + 281796):
                    break
                if arg5:
                    break
                arg6 = load32(arg3 + 8)
                if not load32(arg3 + 8):
                    break
                v11 = load32(arg0 + 28)
                arg3 = load32(arg3)
                v9 = 0
                while True:  # $label38
                    while True:  # $label37
                        v10 = (v9 << 2)
                        if (load32((arg3 + (v9 << 2))) != v11):
                            break
                        if (load32((arg3 + (v10 | 4))) != arg2):
                            break
                        v9 = 0
                        break
                        break
                    v9 = (v9 + 2)
                    if (u32((v9 + 2)) < u32(arg6)):
                        continue
                    break
                break
            while True:  # $label48
                while True:  # $label39
                    if not arg4:
                        break
                    while True:  # $label40
                        if not load32(arg7 + 8):
                            v10 = 0
                            break
                        arg6 = (arg7 + 8)
                        v14 = ((arg2 * 404) + ENTITY_TYPES)
                        v18 = ((arg1 + (arg2 << 2)) + 282828)
                        arg3 = 0
                        v11 = 0
                        while True:  # $label47
                            while True:  # $label41
                                arg7 = load32(arg7)
                                v9 = load32((load32(arg7) + (arg3 << 2)))
                                if (((load32((load32(arg7) + (arg3 << 2))) - 2147483647) if (u32(v9) > u32(2147483646)) else v9) != arg2):
                                    break
                                if not arg3:
                                    store32(arg7, (load32(arg7) + 2147483647))
                                    while True:  # $label42
                                        if not load32(arg0 + 92):
                                            break
                                        arg3 = load8u(9147141)
                                        if load32(9140316):
                                            if (load32(9140320) != load32(arg0 + 28)):
                                                break
                                        break
                                    arg3 = 0
                                    v9 = 0
                                    if not load32(v14 + 244):
                                        v11 = 1
                                        break
                                    while True:  # $label43
                                        v11 = 1
                                        v9 = (v9 + 1)
                                        if (u32((v9 + 1)) < u32(load32(v14 + 244))):
                                            continue
                                        break
                                    break
                                v9 = load32(arg1 + 283848)
                                if (load32(arg1 + 283848) != 2147483647):
                                    store32(arg1 + 283848, (load32(v13) + v9))
                                v9 = load32(arg1 + 283852)
                                if (load32(arg1 + 283852) != 2147483647):
                                    store32(arg1 + 283852, (load32(v13 + 4) + v9))
                                v9 = load32(arg1 + 283856)
                                if (load32(arg1 + 283856) != 2147483647):
                                    store32(arg1 + 283856, (load32(v13 + 8) + v9))
                                v9 = load32(v13 + 12)
                                v10 = load32(arg1 + 283860)
                                if (load32(arg1 + 283860) != 2147483647):
                                    store32(arg1 + 283860, (v9 + v10))
                                store32(arg1 + 281692, (load32(arg1 + 281692) - load32(v13)))
                                store32(arg1 + 281696, (load32(arg1 + 281696) - load32(v13 + 4)))
                                v10 = load32(v13 + 8)
                                store32(arg1 + 281704, (load32(arg1 + 281704) - v9))
                                store8(arg1 + 286701, 1)
                                store32(arg1 + 281700, (load32(arg1 + 281700) - v10))
                                while True:  # $label44
                                    v10 = load32(PLAYER_COUNT)
                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                        break
                                    v9 = 1
                                    v19 = (v10 - 1)
                                    v21 = ((v10 - 1) & 1)
                                    v16 = (load32(arg1 + 283908) * v10)
                                    v15 = load32(PLAYERS)
                                    v17 = load32(9143016)
                                    if (v10 != 2):
                                        v19 = (v19 & -2)
                                        v10 = 0
                                        while True:  # $label45
                                            if load8u((v17 + (v9 + v16))):
                                                store8((v15 + (v9 * 286704)) + 286701, 1)
                                            v22 = (v9 + 1)
                                            if load8u((v17 + ((v9 + 1) + v16))):
                                                store8((v15 + (v22 * 286704)) + 286701, 1)
                                            v9 = (v9 + 2)
                                            v10 = (v10 + 2)
                                            if ((v10 + 2) != v19):
                                                continue
                                            break
                                    if not v21:
                                        break
                                    if not load8u((v17 + (v9 + v16))):
                                        break
                                    store8((v15 + (v9 * 286704)) + 286701, 1)
                                    break
                                v10 = (load32(arg6) - 1)
                                store32(arg6, (load32(arg6) - 1))
                                v9 = arg3
                                if (u32(v10) > u32(arg3)):
                                    while True:  # $label46
                                        v9 = (v9 + 1)
                                        store32((arg7 + (v9 << 2)), load32((arg7 + ((v9 + 1) << 2))))
                                        if (u32(v9) < u32(load32(arg6))):
                                            continue
                                        break
                                store32(v18, (load32(v18) - 1))
                                arg3 = (arg3 - 1)
                                break
                            arg7 = load32(arg0 + 20)
                            arg6 = (load32(arg0 + 20) + 8)
                            arg3 = (arg3 + 1)
                            v10 = load32(arg7 + 8)
                            if (u32((arg3 + 1)) < u32(load32(arg7 + 8))):
                                continue
                            break
                        v9 = 1
                        if (v11 & 1):
                            break
                        break
                    if v10:
                        break
                    # br_table (v20 - 4)
                    break
                    break
                arg3 = (arg4 ^ 1)
                if not func66(arg1, v13, (arg4 ^ 1), 1):
                    break
                if not (arg3 | arg5):
                    func181(arg1, load32(arg0 + 28), arg2)
                    arg1 = ((arg1 + (arg2 << 2)) + 282828)
                    store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg1) + 1))
                v9 = 0
                func294(arg0)
                arg0 = ((arg2 * 404) + ENTITY_TYPES)
                if not load32(arg0 + 244):
                    break
                arg7 = 0
                while True:  # $label49
                    arg7 = (arg7 + 1)
                    if (u32((arg7 + 1)) < u32(load32(arg0 + 244))):
                        continue
                    break
                break
                break
            while True:  # $label50
                if not arg8:
                    break
                v9 = 0
                while True:  # $label66
                    while True:  # $label57
                        arg6 = 0
                        v10 = 0
                        v14 = 0
                        v16 = load16u(arg0 + 110)
                        v15 = load32(PLAYERS)
                        while True:  # $label53
                            while True:  # $label52
                                while True:  # $label51
                                    arg8 = load32(((arg2 * 404) + ENTITY_TYPES) + 180)
                                    if not load8u(load32(((arg2 * 404) + ENTITY_TYPES) + 180) + 23):
                                        break
                                    arg3 = load32(arg8 + 4)
                                    if (load32(((load32(arg8 + 4) * 404) + ENTITY_TYPES) + 264) != 3):
                                        break
                                    if not load32((((v15 + (v16 * 286704)) + (arg3 << 2)) + 281808)):
                                        break
                                    v11 = load32(arg8 + 68)
                                    break
                                    break
                                arg7 = 1
                                v11 = load32(arg8 + 68)
                                if not load32(arg8 + 68):
                                    break
                                v18 = (v15 + (v16 * 286704))
                                arg3 = 1
                                while True:  # $label56
                                    v19 = load32((arg8 + (arg6 << 2)) + 28)
                                    arg7 = load32(((load32((arg8 + (arg6 << 2)) + 28) * 404) + ENTITY_TYPES) + 264)
                                    v17 = (load32(((load32((arg8 + (arg6 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) == 1)
                                    while True:  # $label55
                                        while True:  # $label54
                                            v19 = load32(((v18 + (v19 << 2)) + 281808))
                                            if (load32(((v18 + (v19 << 2)) + 281808)) == 1):
                                                break
                                            arg3 = ((arg7 != 3) & arg3)
                                            if v19:
                                                break
                                            arg3 = ((arg7 != 0) & arg3)
                                            break
                                            break
                                        v10 = (v10 | v17)
                                        break
                                    v14 = (v14 | v17)
                                    arg6 = (arg6 + 1)
                                    if ((arg6 + 1) != v11):
                                        continue
                                    break
                                arg7 = 1
                                if (((arg3 & v10) if (v14 & 1) else arg3) & 1):
                                    break
                                break
                            if not v11:
                                break
                            v10 = (v15 + (v16 * 286704))
                            v14 = ((v15 + (v16 * 286704)) + 281796)
                            v16 = load32(arg0 + 28)
                            arg3 = 0
                            v15 = load32(arg0 + 20)
                            if not load32(arg0 + 20):
                                while True:  # $label60
                                    while True:  # $label58
                                        v15 = load32((arg8 + (arg3 << 2)) + 28)
                                        if load32(((v10 + (load32((arg8 + (arg3 << 2)) + 28) << 2)) + 281808)):
                                            break
                                        arg7 = 0
                                        arg6 = load32(v14)
                                        if not load32(v14):
                                            break
                                        v17 = load32(arg6 + 8)
                                        if not load32(arg6 + 8):
                                            break
                                        arg7 = load32(arg6)
                                        arg6 = 0
                                        while True:  # $label59
                                            v18 = (arg6 << 2)
                                            if (v16 == load32((arg7 + (arg6 << 2)))):
                                                if (load32((arg7 + (v18 | 4))) == v15):
                                                    break
                                            arg6 = (arg6 + 2)
                                            if (u32((arg6 + 2)) < u32(v17)):
                                                continue
                                            break
                                        break
                                        break
                                    arg7 = 2
                                    arg3 = (arg3 + 1)
                                    if ((arg3 + 1) != v11):
                                        continue
                                    break
                                    break
                                raise Unreachable()
                            while True:  # $label65
                                while True:  # $label61
                                    v17 = load32((arg8 + (arg3 << 2)) + 28)
                                    if load32(((v10 + (load32((arg8 + (arg3 << 2)) + 28) << 2)) + 281808)):
                                        break
                                    while True:  # $label62
                                        v18 = load32(v15 + 8)
                                        if not load32(v15 + 8):
                                            break
                                        v19 = load32(v15)
                                        arg7 = 0
                                        while True:  # $label63
                                            arg6 = load32((v19 + (arg7 << 2)))
                                            if (v17 != ((load32((v19 + (arg7 << 2))) - 2147483647) if (u32(arg6) > u32(2147483646)) else arg6)):
                                                arg7 = (arg7 + 1)
                                                if (v18 != (arg7 + 1)):
                                                    continue
                                                break
                                            break
                                        break
                                        break
                                    arg7 = 0
                                    arg6 = load32(v14)
                                    if not load32(v14):
                                        break
                                    v18 = load32(arg6 + 8)
                                    if not load32(arg6 + 8):
                                        break
                                    arg7 = load32(arg6)
                                    arg6 = 0
                                    while True:  # $label64
                                        v19 = (arg6 << 2)
                                        if (v16 == load32((arg7 + (arg6 << 2)))):
                                            if (load32((arg7 + (v19 | 4))) == v17):
                                                break
                                        arg6 = (arg6 + 2)
                                        if (u32((arg6 + 2)) < u32(v18)):
                                            continue
                                        break
                                    break
                                    break
                                arg7 = 2
                                arg3 = (arg3 + 1)
                                if ((arg3 + 1) != v11):
                                    continue
                                break
                            break
                        break
                    # br_table arg7
                    break
                    break
                func181(arg1, load32(arg0 + 28), arg2)
                arg1 = ((arg1 + (arg2 << 2)) + 282828)
                store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg1) + 1))
                func294(arg0)
                arg0 = ((arg2 * 404) + ENTITY_TYPES)
                if not load32(arg0 + 244):
                    break
                arg7 = 0
                while True:  # $label67
                    arg7 = (arg7 + 1)
                    if (u32((arg7 + 1)) < u32(load32(arg0 + 244))):
                        continue
                    break
                break
                break
            arg8 = ((2147483647 if arg4 else 0) + arg2)
            while True:  # $label68
                arg3 = load32(arg0 + 20)
                arg7 = load32(load32(arg0 + 20) + 8)
                if (load32(load32(arg0 + 20) + 8) != load32(arg3 + 4)):
                    arg6 = load32(arg3)
                    break
                arg6 = (load32(arg3 + 12) + arg7)
                store32(arg3 + 4, (load32(arg3 + 12) + arg7))
                arg4 = load32(arg3)
                arg6 = func26((-1 if (u32(arg6) > u32(1073741823)) else (arg6 << 2)))
                if arg7:
                    # TODO: memory.copy
                if arg4:
                    arg7 = load32(arg3 + 8)
                store32(arg3, arg6)
                break
            store32(arg3 + 8, (arg7 + 1))
            store32((arg6 + (arg7 << 2)), arg8)
            if not arg5:
                arg1 = ((arg1 + (arg2 << 2)) + 282828)
                store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg1) + 1))
            while True:  # $label69
                if (load32(load32(arg0 + 20) + 8) != 1):
                    break
                while True:  # $label70
                    # br_table (v20 - 4)
                    break
                    break
                store8(arg0 + 125, 6)
                # TODO: i32.div_u
                func63(arg0, 2, 0, ((load32(((arg2 * 404) + ENTITY_TYPES) + 116) * load32((load32(GAME_STATE) + (132 if load32(v12 + 264) else 128)))) * 1000), 100)
                break
            arg1 = ((arg2 * 404) + ENTITY_TYPES)
            if not load32(arg1 + 244):
                break
            v9 = 0
            while True:  # $label71
                v9 = (v9 + 1)
                if (u32((v9 + 1)) < u32(load32(arg1 + 244))):
                    continue
                break
            break
        v9 = 1
        if not load32(arg0 + 92):
            break
        arg1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break
    G.global0 = (v13 + 16)
    return v9
