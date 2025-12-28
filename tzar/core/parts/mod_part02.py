"""
Tzar Engine - Core module (part 2).
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
# $func68
# ----------------------------------------------------------
def func68():
    v0 = func443(4)
    store32(func443(4), 32876)
    store32(v0, 32836)
    store32(v0, 32856)
    a_i()
    raise Unreachable()

# ----------------------------------------------------------
# $func69
# ----------------------------------------------------------
def func69(arg0, arg1):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v8 = load16u(arg0 + 116)
        if not load16u(arg0 + 116):
            break
        v9 = load16u(arg0 + 118)
        if not load16u(arg0 + 118):
            break
        v5 = load32(ENTITIES)
        v10 = entities[arg1]
        while True:  # $label7
            while True:  # $label2
                while True:  # $label1
                    v3 = load32(9142840)
                    v2 = (v8 + 1)
                    v4 = (load32(9142440) + 2)
                    v6 = (v9 + 1)
                    arg0 = load32((load32(9142840) + (((v8 + 1) + ((load32(9142440) + 2) * (v9 + 1))) << 2)))
                    if (u32(load32((load32(9142840) + (((v8 + 1) + ((load32(9142440) + 2) * (v9 + 1))) << 2)))) > u32(2)):
                        break
                    arg0 = load32((v3 + ((((v4 + v6) * v4) + v2) << 2)))
                    if (u32(load32((v3 + ((((v4 + v6) * v4) + v2) << 2)))) > u32(2)):
                        break
                    v6 = load8u((v5 + (arg0 * 132)) + 122)
                    v3 = 0
                    break
                    break
                v4 = (v5 + (arg0 * 132))
                v6 = load8u((v5 + (arg0 * 132)) + 122)
                v2 = load32(((load8u((v5 + (arg0 * 132)) + 122) * 404) + ENTITY_TYPES) + 192)
                while True:  # $label4
                    while True:  # $label3
                        while True:  # $label5
                            v11 = load8u(v10 + 122)
                            # br_table (load8u(v10 + 122) + -64)
                            break
                            break
                        if (v11 != 10):
                            break
                        break
                    if (u32(v2) > u32(1)):
                        break
                    while True:  # $label6
                        # br_table (load8u((v5 + (arg0 * 132)) + 125) - 4)
                        break
                        break
                    v3 = 0
                    v4 = func224(v4, v2, 0)
                    if not func224(v4, v2, 0):
                        break
                    v2 = -1
                    v3 = 1
                    arg0 = v4
                    break
                    break
                store32(v7 + 12, arg1)
                v3 = 0
                if (load32(38528) == v11):
                    break
                v2 = -1
                v3 = func161(v4, (v7 + 12), 1)
                # br_table func161(v4, (v7 + 12), 1)
                break
                break
            v2 = -1
            if (load32(38564) == v6):
                break
            v2 = (5 if load32((v5 + (arg1 * 132)) + 52) else 0)
            v3 = 0
            arg0 = 0
            break
        break
    G.global0 = (v7 + 16)

# ----------------------------------------------------------
# $func70
# ----------------------------------------------------------
def func70(arg0, arg1, arg2, arg3):
    while True:  # $label18
        while True:  # $label17
            if (load32(arg0 + 132) > 0):
                v7 = load32(arg0)
                if (load32(load32(arg0) + 44) == 2):
                    v4 = -201342849
                    while True:  # $label1
                        while True:  # $label3
                            while True:  # $label0
                                if not (v4 & 1):
                                    break
                                if not load16u((arg0 + (v5 << 2)) + 148):
                                    break
                                v4 = 0
                                break
                                break
                            while True:  # $label2
                                if not (v4 & 2):
                                    break
                                if not load16u((arg0 + ((v5 << 2) | 4)) + 148):
                                    break
                                v4 = 0
                                break
                                break
                            v4 = ((v4 & 0xFFFFFFFF) >> 2)
                            v5 = (v5 + 2)
                            if ((v5 + 2) != 32):
                                continue
                            break
                        while True:  # $label4
                            if load16u(arg0 + 184):
                                break
                            if load16u(arg0 + 188):
                                break
                            if load16u(arg0 + 200):
                                break
                            v5 = 32
                            while True:  # $label5
                                v4 = (v5 << 2)
                                if load16u((arg0 + (v5 << 2)) + 148):
                                    break
                                if load16u((arg0 + (v4 | 4)) + 148):
                                    break
                                if load16u((arg0 + (v4 | 8)) + 148):
                                    break
                                if load16u((arg0 + (v4 | 12)) + 148):
                                    break
                                v4 = 0
                                v5 = (v5 + 4)
                                if ((v5 + 4) != 256):
                                    continue
                                break
                            break
                            break
                        v4 = 1
                        break
                    store32(v7 + 44, v4)
                v4 = load16u(arg0 + 150)
                v13 = (arg0 + 148)
                v11 = load32((arg0 + 2844))
                store16(((arg0 + 148) + (load32((arg0 + 2844)) << 2)) + 6, 65535)
                if (v11 >= 0):
                    v12 = (7 if v4 else 138)
                    v10 = (4 if v4 else 3)
                    v8 = -1
                    v7 = 0
                    while True:  # $label10
                        v5 = v4
                        v14 = v7
                        v7 = (v7 + 1)
                        v4 = load16u((v13 + ((v7 + 1) << 2)) + 2)
                        while True:  # $label7
                            while True:  # $label6
                                v9 = (v6 + 1)
                                if ((v6 + 1) >= v12):
                                    break
                                if (v4 != v5):
                                    break
                                v6 = v9
                                break
                                break
                            while True:  # $label8
                                if (v9 < v10):
                                    v6 = ((arg0 + (v5 << 2)) + 2684)
                                    store16(((arg0 + (v5 << 2)) + 2684), (load16u(v6) + v9))
                                    break
                                if v5:
                                    if (v5 != v8):
                                        v6 = ((arg0 + (v5 << 2)) + 2684)
                                        store16(((arg0 + (v5 << 2)) + 2684), (load16u(v6) + 1))
                                    store16(arg0 + 2748, (load16u(arg0 + 2748) + 1))
                                    break
                                if (v6 <= 9):
                                    store16(arg0 + 2752, (load16u(arg0 + 2752) + 1))
                                    break
                                store16(arg0 + 2756, (load16u(arg0 + 2756) + 1))
                                break
                            v6 = 0
                            while True:  # $label9
                                if not v4:
                                    v10 = 3
                                    break
                                v8 = (v4 == v5)
                                v10 = (3 if (v4 == v5) else 4)
                                break
                            v12 = (6 if v8 else 7)
                            v8 = v5
                            break
                        if (v11 != v14):
                            continue
                        break
                v4 = load16u((arg0 + 2442))
                v13 = (arg0 + 2440)
                v11 = load32((arg0 + 2856))
                store16(((arg0 + 2440) + (load32((arg0 + 2856)) << 2)) + 6, 65535)
                v6 = 0
                if (v11 >= 0):
                    v12 = (7 if v4 else 138)
                    v10 = (4 if v4 else 3)
                    v8 = -1
                    v7 = 0
                    while True:  # $label15
                        v5 = v4
                        v14 = v7
                        v7 = (v7 + 1)
                        v4 = load16u((v13 + ((v7 + 1) << 2)) + 2)
                        while True:  # $label12
                            while True:  # $label11
                                v9 = (v6 + 1)
                                if ((v6 + 1) >= v12):
                                    break
                                if (v4 != v5):
                                    break
                                v6 = v9
                                break
                                break
                            while True:  # $label13
                                if (v9 < v10):
                                    v6 = ((arg0 + (v5 << 2)) + 2684)
                                    store16(((arg0 + (v5 << 2)) + 2684), (load16u(v6) + v9))
                                    break
                                if v5:
                                    if (v5 != v8):
                                        v6 = ((arg0 + (v5 << 2)) + 2684)
                                        store16(((arg0 + (v5 << 2)) + 2684), (load16u(v6) + 1))
                                    store16(arg0 + 2748, (load16u(arg0 + 2748) + 1))
                                    break
                                if (v6 <= 9):
                                    store16(arg0 + 2752, (load16u(arg0 + 2752) + 1))
                                    break
                                store16(arg0 + 2756, (load16u(arg0 + 2756) + 1))
                                break
                            v6 = 0
                            while True:  # $label14
                                if not v4:
                                    v10 = 3
                                    break
                                v8 = (v4 == v5)
                                v10 = (3 if (v4 == v5) else 4)
                                break
                            v12 = (6 if v8 else 7)
                            v8 = v5
                            break
                        if (v11 != v14):
                            continue
                        break
                while True:  # $label16
                    if load16u((arg0 + 2746)):
                        break
                    if load16u((arg0 + 2690)):
                        break
                    if load16u((arg0 + 2742)):
                        break
                    if load16u((arg0 + 2694)):
                        break
                    if load16u((arg0 + 2738)):
                        break
                    if load16u((arg0 + 2698)):
                        break
                    if load16u((arg0 + 2734)):
                        break
                    if load16u((arg0 + 2702)):
                        break
                    if load16u((arg0 + 2730)):
                        break
                    if load16u((arg0 + 2706)):
                        break
                    if load16u((arg0 + 2726)):
                        break
                    if load16u((arg0 + 2710)):
                        break
                    if load16u((arg0 + 2722)):
                        break
                    if load16u((arg0 + 2714)):
                        break
                    if load16u((arg0 + 2718)):
                        break
                    break
                v7 = (3 if load16u((arg0 + 2686)) else 2)
                v4 = (load32(arg0 + 5800) + ((3 if load16u((arg0 + 2686)) else 2) * 3))
                store32(arg0 + 5800, ((load32(arg0 + 5800) + ((3 if load16u((arg0 + 2686)) else 2) * 3)) + 17))
                v5 = (((load32(arg0 + 5804) + 10) & 0xFFFFFFFF) >> 3)
                v4 = (((v4 + 27) & 0xFFFFFFFF) >> 3)
                if (u32((((load32(arg0 + 5804) + 10) & 0xFFFFFFFF) >> 3)) <= u32((((v4 + 27) & 0xFFFFFFFF) >> 3))):
                    break
                if (load32(arg0 + 136) == 4):
                    break
                break
            v5 = (arg2 + 5)
            break
        v4 = v5
        break
    while True:  # $label20
        while True:  # $label19
            if not arg1:
                break
            if (u32((arg2 + 4)) > u32(v4)):
                break
            break
            break
        arg1 = load32(arg0 + 5820)
        if (v4 == v5):
            arg2 = (arg3 + 2)
            while True:  # $label21
                if (arg1 >= 14):
                    arg1 = (load16u(arg0 + 5816) | (arg2 << arg1))
                    store16(arg0 + 5816, (load16u(arg0 + 5816) | (arg2 << arg1)))
                    v4 = load32(arg0 + 20)
                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                    store8((v4 + load32(arg0 + 8)), arg1)
                    arg1 = load32(arg0 + 20)
                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                    store8((arg1 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                    arg1 = load32(arg0 + 5820)
                    store16(arg0 + 5816, (((arg2 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                    break
                store16(arg0 + 5816, (load16u(arg0 + 5816) | (arg2 << arg1)))
                break
            store32((arg1 - 13) + 5820, (arg1 + 3))
            break
        arg2 = (arg3 + 4)
        while True:  # $label22
            if (arg1 >= 14):
                arg1 = (load16u(arg0 + 5816) | (arg2 << arg1))
                store16(arg0 + 5816, (load16u(arg0 + 5816) | (arg2 << arg1)))
                v4 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v4 + load32(arg0 + 8)), arg1)
                arg1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((arg1 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                arg1 = load32(arg0 + 5820)
                v6 = (((arg2 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                break
            v6 = (load16u(arg0 + 5816) | (arg2 << arg1))
            break
        v4 = (arg1 + 3)
        store32((arg1 - 13) + 5820, (arg1 + 3))
        v8 = load32((arg0 + 2844))
        arg1 = (load32((arg0 + 2844)) + 65280)
        arg2 = load32((arg0 + 2856))
        while True:  # $label23
            if (v4 >= 12):
                v4 = (v6 | (arg1 << v4))
                store16(arg0 + 5816, (v6 | (arg1 << v4)))
                v6 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v6 + load32(arg0 + 8)), v4)
                v4 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v4 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                arg1 = load32(arg0 + 5820)
                v4 = (((arg1 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                v5 = (arg1 - 11)
                break
            v5 = (v4 + 5)
            v4 = (v6 | (arg1 << v4))
            break
        store32(arg0 + 5820, v5)
        while True:  # $label24
            if (v5 >= 12):
                arg1 = (v4 | (arg2 << v5))
                store16(arg0 + 5816, (v4 | (arg2 << v5)))
                v4 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v4 + load32(arg0 + 8)), arg1)
                arg1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((arg1 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                arg1 = load32(arg0 + 5820)
                v6 = (((arg2 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                break
            v6 = (v4 | (arg2 << v5))
            break
        arg1 = (v5 + 5)
        store32((arg1 - 11) + 5820, (v5 + 5))
        v5 = (v7 + 65533)
        while True:  # $label25
            if (arg1 >= 13):
                arg1 = (v6 | (v5 << arg1))
                store16(arg0 + 5816, (v6 | (v5 << arg1)))
                v4 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v4 + load32(arg0 + 8)), arg1)
                arg1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((arg1 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                v4 = load32(arg0 + 5820)
                arg1 = (((v5 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                v4 = (v4 - 12)
                break
            v4 = (arg1 + 4)
            arg1 = (v6 | (v5 << arg1))
            break
        store32(arg0 + 5820, v4)
        v5 = 0
        v6 = (arg0 + 5817)
        while True:  # $label27
            v9 = load16u(((arg0 + (load8u((v5 + 25920)) << 2)) + 2686))
            arg1 = (arg1 | (load16u(((arg0 + (load8u((v5 + 25920)) << 2)) + 2686)) << v4))
            store16(arg0 + 5816, (arg1 | (load16u(((arg0 + (load8u((v5 + 25920)) << 2)) + 2686)) << v4)))
            while True:  # $label26
                if (v4 >= 14):
                    v4 = load32(arg0 + 20)
                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                    store8((v4 + load32(arg0 + 8)), arg1)
                    arg1 = load32(arg0 + 20)
                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                    store8((arg1 + load32(arg0 + 8)), load8u(v6))
                    v4 = load32(arg0 + 5820)
                    arg1 = ((v9 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                    store16(arg0 + 5816, ((v9 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                    break
                break
            v4 = (v4 + 3)
            store32((v4 - 13) + 5820, (v4 + 3))
            v9 = (v5 != v7)
            v5 = (v5 + 1)
            if v9:
                continue
            break
        arg1 = (arg0 + 148)
        v4 = (arg0 + 2440)
        break
    func367(arg0)
    if arg3:
        while True:  # $label28
            arg1 = load32(arg0 + 5820)
            if (load32(arg0 + 5820) >= 9):
                arg1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((arg1 + load32(arg0 + 8)), load8u(arg0 + 5816))
                arg1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((arg1 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                break
            if (arg1 <= 0):
                break
            arg1 = load32(arg0 + 20)
            store32(arg0 + 20, (load32(arg0 + 20) + 1))
            store8((arg1 + load32(arg0 + 8)), load8u(arg0 + 5816))
            break
        store32(arg0 + 5820, 0)
        store16(arg0 + 5816, 0)
    return func406(arg0, arg1, v4)

# ----------------------------------------------------------
# $func71
# ----------------------------------------------------------
def func71(arg0, arg1, arg2, arg3, arg4, arg5):
    v6 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v9 = ((arg2 + arg4) + 6)
    v7 = func26((-1 if (u32(v9) > u32(1073741823)) else (((arg2 + arg4) + 6) << 2)))
    store64(func26((-1 if (u32(v9) > u32(1073741823)) else (((arg2 + arg4) + 6) << 2))), -4294967296)
    v8 = load32(9142384)
    store32(v7 + 20, arg4)
    store32(v7 + 16, arg2)
    store32(v7 + 12, arg0)
    store32(v7 + 8, v8)
    if arg2:
        # TODO: memory.copy
    if arg4:
        # TODO: memory.copy
    while True:  # $label0
        if not load8u(9147125):
            store32(v6 + 4, v9)
            store32(v6, v7)
            break
        v10 = load32((PLAYER_COUNT if load8u(9147212) else 41092))
        if (u32(load32((PLAYER_COUNT if load8u(9147212) else 41092))) >= u32(2)):
            v8 = load32(PLAYERS)
            arg4 = 1
            while True:  # $label1
                v11 = load32((v8 + (arg4 * 286704)) + 284616)
                if load32((v8 + (arg4 * 286704)) + 284616):
                    store32(v6 + 24, v11)
                    store32(v6 + 20, v9)
                    store32(v6 + 16, v7)
                    v8 = load32(PLAYERS)
                arg4 = (arg4 + 1)
                if ((arg4 + 1) != v10):
                    continue
                break
        break
    if not arg5:
        store32(59164, load32(9142384))
        store32(59164, 0)
    G.global0 = (v6 + 48)

# ----------------------------------------------------------
# $func72
# ----------------------------------------------------------
def func72(arg0, arg1):
    v8 = load32(arg0 + 283848)
    store32(arg1, load32(arg0 + 283848))
    v9 = load32((arg0 + 283852))
    store32(arg1 + 4, load32((arg0 + 283852)))
    v10 = load32((arg0 + 283856))
    store32(arg1 + 8, load32((arg0 + 283856)))
    v2 = load32((arg0 + 283860))
    store32(arg1 + 12, load32((arg0 + 283860)))
    v12 = load32(PLAYER_COUNT)
    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
        v3 = load32(PLAYERS)
        v11 = load32(9143016)
        v4 = 1
        while True:  # $label4
            v5 = v3
            v3 = v8
            v6 = v9
            v7 = v10
            v13 = v2
            while True:  # $label0
                v14 = (v4 * v12)
                v2 = ((v4 * v12) + load32(arg0 + 283908))
                if not (load8u((v11 + ((v4 * v12) + load32(arg0 + 283908)))) & 1):
                    break
                v8 = 2147483647
                if (v3 == 2147483647):
                    break
                v3 = load32((v5 + (v4 * 286704)) + 283848)
                v8 = (2147483647 if (v3 == 2147483647) else (v3 + load32((v5 + (v4 * 286704)) + 283848)))
                store32(arg1, (2147483647 if (v3 == 2147483647) else (v3 + load32((v5 + (v4 * 286704)) + 283848))))
                v12 = load32(PLAYER_COUNT)
                v14 = (load32(PLAYER_COUNT) * v4)
                v2 = ((load32(PLAYER_COUNT) * v4) + load32(arg0 + 283908))
                break
            v3 = load32(PLAYERS)
            while True:  # $label1
                v2 = load8u((v2 + v11))
                if not (load8u((v2 + v11)) & 2):
                    break
                v9 = 2147483647
                if (v6 == 2147483647):
                    break
                v6 = load32(((v5 + (v4 * 286704)) + 283852))
                v9 = (2147483647 if (v6 == 2147483647) else (v6 + load32(((v5 + (v4 * 286704)) + 283852))))
                store32(arg1 + 4, (2147483647 if (v6 == 2147483647) else (v6 + load32(((v5 + (v4 * 286704)) + 283852)))))
                v2 = load8u((v11 + (v14 + load32(arg0 + 283908))))
                break
            while True:  # $label2
                if not (v2 & 4):
                    break
                v10 = 2147483647
                if (v7 == 2147483647):
                    break
                v7 = load32(((v5 + (v4 * 286704)) + 283856))
                v10 = (2147483647 if (v7 == 2147483647) else (v7 + load32(((v5 + (v4 * 286704)) + 283856))))
                store32(arg1 + 8, (2147483647 if (v7 == 2147483647) else (v7 + load32(((v5 + (v4 * 286704)) + 283856)))))
                v2 = load8u((v11 + (v14 + load32(arg0 + 283908))))
                break
            while True:  # $label3
                if not (v2 & 8):
                    v2 = v13
                    break
                v2 = 2147483647
                if (v13 == 2147483647):
                    break
                v5 = load32(((v5 + (v4 * 286704)) + 283860))
                v2 = (2147483647 if (v5 == 2147483647) else (load32(((v5 + (v4 * 286704)) + 283860)) + v13))
                store32(arg1 + 12, (2147483647 if (v5 == 2147483647) else (load32(((v5 + (v4 * 286704)) + 283860)) + v13)))
                break
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(v12)):
                continue
            break
    return v5

# ----------------------------------------------------------
# $func73
# ----------------------------------------------------------
def func73(arg0, arg1, arg2, arg3, arg4, arg5):
    v7 = load32(arg2 + 216)
    v16 = load32(arg2 + 208)
    v11 = load32(arg2 + 372)
    while True:  # $label4
        while True:  # $label0
            if not arg5:
                break
            if (v7 <= 0):
                break
            v9 = (load32(arg2 + 220) + arg1)
            if ((load32(arg2 + 220) + arg1) <= arg1):
                break
            v17 = (arg0 + v7)
            v10 = load32(9142440)
            v13 = (load32(9142440) + 2)
            v18 = ((load32(9142440) + 2) * v16)
            v14 = load32(arg2 + 212)
            v15 = load32(9142840)
            if (load32(arg2 + 264) == 1):
                v6 = arg0
                while True:  # $label6
                    v8 = (v6 + 1)
                    v12 = (v6 - arg0)
                    arg5 = arg1
                    while True:  # $label2
                        if (u32(v6) >= u32(v10)):
                            while True:  # $label1
                                if load8u((v11 + (v12 + ((arg5 - arg1) * v7)))):
                                    return 0
                                arg5 = (arg5 + 1)
                                if ((arg5 + 1) != v9):
                                    continue
                                break
                                break
                            raise Unreachable()
                        while True:  # $label5
                            while True:  # $label3
                                if not load8u((v11 + (v12 + ((arg5 - arg1) * v7)))):
                                    arg5 = (arg5 + 1)
                                    break
                                if (u32(arg5) >= u32(v10)):
                                    break
                                if ((arg5 | v6) < 0):
                                    break
                                arg5 = (arg5 + 1)
                                if (load32((v15 + ((((v18 + (arg5 + 1)) * v13) + v8) << 2))) != v14):
                                    break
                                if (load32((v15 + (((arg5 * v13) + v8) << 2))) != v14):
                                    break
                                break
                            if (arg5 != v9):
                                continue
                            break
                        break
                    v6 = v8
                    if (v8 < v17):
                        continue
                    break
                break
            v6 = arg0
            while True:  # $label11
                v8 = (v6 + 1)
                v12 = (v6 - arg0)
                arg5 = arg1
                while True:  # $label9
                    if (u32(v6) < u32(v10)):
                        while True:  # $label8
                            while True:  # $label7
                                if not load8u((v11 + (v12 + ((arg5 - arg1) * v7)))):
                                    arg5 = (arg5 + 1)
                                    break
                                if (u32(arg5) >= u32(v10)):
                                    break
                                if ((arg5 | v6) < 0):
                                    break
                                arg5 = (arg5 + 1)
                                if (load32((v15 + ((((v18 + (arg5 + 1)) * v13) + v8) << 2))) != v14):
                                    break
                                break
                            if (arg5 != v9):
                                continue
                            break
                            break
                        raise Unreachable()
                    while True:  # $label10
                        if not load8u((v11 + (v12 + ((arg5 - arg1) * v7)))):
                            arg5 = (arg5 + 1)
                            if (v9 != (arg5 + 1)):
                                continue
                            break
                        break
                    return 0
                    break
                v6 = v8
                if (v8 < v17):
                    continue
                break
            break
        v19 = 1
        if not arg3:
            break
        if (v7 <= 0):
            break
        arg3 = (load32(arg2 + 220) + arg1)
        if ((load32(arg2 + 220) + arg1) <= arg1):
            break
        v6 = (arg0 + v7)
        arg5 = arg0
        while True:  # $label14
            arg2 = (arg5 + 1)
            v8 = (arg5 - arg0)
            v9 = load32(9142840)
            arg5 = arg1
            while True:  # $label13
                while True:  # $label12
                    if not load8u((v11 + (v8 + ((arg5 - arg1) * v7)))):
                        arg5 = (arg5 + 1)
                        break
                    arg5 = (arg5 + 1)
                    v10 = (load32(9142440) + 2)
                    store32((v9 + ((arg2 + (((arg5 + 1) + ((load32(9142440) + 2) * v16)) * v10)) << 2)), arg4)
                    break
                if (arg3 != arg5):
                    continue
                break
            arg5 = arg2
            if (arg2 < v6):
                continue
            break
        break
    return v19

# ----------------------------------------------------------
# $func74
# ----------------------------------------------------------
def func74(arg0, arg1, arg2):
    while True:  # $label0
        if load8u(9147152):
            break
        v5 = load16u(arg0 + 114)
        v4 = load16u(arg0 + 112)
        while True:  # $label1
            if (arg1 == -1):
                break
            if not load8u(59181):
                break
            v3 = load32(arg0 + 44)
            if not load32(arg0 + 44):
                break
            v6 = load32(9215884)
            if (load32((load32(9215884) + (v3 << 4)) + 12) == 1):
                break
            if (load8u(arg0 + 125) == 7):
                break
            if load32((v6 + ((v3 << 4) | 4))):
                break
            arg1 = (arg1 << 3)
            v5 = (v5 - load32(((arg1 << 3) + 8996)))
            v4 = (v4 - load32((arg1 + 8992)))
            break
        while True:  # $label2
            v3 = load32(CURRENT_PLAYER)
            if not load32(CURRENT_PLAYER):
                break
            if not load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(PLAYER_COUNT) * v3)))):
                break
            break
        if not ((load8u(arg0 + 125) != 3) | arg2):
            break
        v3 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        arg1 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 220)
        arg2 = load32(v3 + 216)
        while True:  # $label5
            while True:  # $label4
                while True:  # $label3
                    # br_table (load8u(arg0 + 125) - 4)
                    break
                    break
                break
                break
            break
        arg0 = load32(v3 + 200)
        if not load32(v3 + 200):
            break
        if (u32(load32(load32(GAME_STATE) + 48)) < u32(2)):
            break
        v6 = (load32(9142836) + (arg0 * 80))
        v7 = load32((load32(9142836) + (arg0 * 80)) + 324)
        if not load32((load32(9142836) + (arg0 * 80)) + 324):
            break
        v8 = (((arg1 & 0xFFFFFFFF) >> 1) + v5)
        v9 = (((arg2 & 0xFFFFFFFF) >> 1) + v4)
        arg1 = load32(9142440)
        v10 = (arg0 * arg0)
        arg0 = 0
        while True:  # $label7
            while True:  # $label6
                v4 = load32(v6 + 320)
                v3 = (arg0 << 2)
                arg2 = load32((load32(v6 + 320) + ((arg0 << 2) | 4)))
                v5 = (v8 + load32((load32(v6 + 320) + ((arg0 << 2) | 4))))
                if (u32(arg1) <= u32((v8 + load32((load32(v6 + 320) + ((arg0 << 2) | 4)))))):
                    break
                v4 = load32((v3 + v4))
                v3 = (v9 + load32((v3 + v4)))
                if (u32(arg1) <= u32((v9 + load32((v3 + v4))))):
                    break
                if ((v3 | v5) < 0):
                    break
                if ((((v4 * v4) + (arg2 * arg2)) - 1) > v10):
                    break
                arg1 = load32(9142440)
                break
            arg0 = (arg0 + 2)
            if (u32((arg0 + 2)) < u32(v7)):
                continue
            break
        break
    return func129(v3, v5, 0)

# ----------------------------------------------------------
# $func77
# ----------------------------------------------------------
def func77(arg0):
    while True:  # $label0
        if not load32(arg0 + 92):
            break
        while True:  # $label1
            v3 = load32(arg0 + 28)
            if (load32(arg0 + 28) != load32(9213820)):
                v2 = load32(9213808)
                if not load32(9213808):
                    break
                while True:  # $label2
                    v4 = ((v1 << 2) + 9173808)
                    if (load32(((v1 << 2) + 9173808)) == v3):
                        break
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v2):
                        continue
                    break
                break
            store32(9213820, 0)
            if not load8u(9147152):
                func52((207 if load8u(9143020) else 0), 0)
                a_b()
            func47(arg0)
            return
            break
        store32(v4, 0)
        v3 = (v2 - 1)
        store32(9213808, (v2 - 1))
        while True:  # $label3
            if (u32(v1) >= u32(v3)):
                break
            v4 = ((v2 - v1) - 2)
            v5 = ((v3 - v1) & 3)
            if ((v3 - v1) & 3):
                v2 = 0
                while True:  # $label4
                    v1 = (v1 + 1)
                    store32(((v1 << 2) + 9173808), load32((((v1 + 1) << 2) + 9173808)))
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v5):
                        continue
                    break
            if (u32(v4) <= u32(2)):
                break
            while True:  # $label5
                v2 = ((v1 << 2) + 9173808)
                v6 = load64(((v1 << 2) + 9173808) + 4)
                store32(v2 + 8, load32(v2 + 12))
                store64(v2, v6)
                v1 = (v1 + 4)
                store32(v2 + 12, load32((((v1 + 4) << 2) + 9173808)))
                if (v1 != v3):
                    continue
                break
            break
        func47(arg0)
        if load32(9213808):
            return
        func45()
        if load8u(9147152):
            break
        func52((207 if load8u(9143020) else 0), 0)
        a_b()
        break

# ----------------------------------------------------------
# $func78
# ----------------------------------------------------------
def func78(arg0, arg1, arg2, arg3):
    v15 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v11 = load16u(arg0 + 110)
        if (load16u(arg0 + 110) == arg1):
            break
        v12 = load8u(arg0 + 122)
        v5 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) == 2):
            break
        if (load32(v5 + 188) != 55):
            if (load32(38528) != v12):
                break
        v10 = load8u(arg0 + 125)
        if (load8u(arg0 + 125) == 3):
            break
        v4 = ((v12 * 404) + ENTITY_TYPES)
        v16 = load32(((v12 * 404) + ENTITY_TYPES) + 176)
        v13 = load32(PLAYERS)
        v14 = players[v11]
        v9 = load32(v4 + 280)
        v6 = (load32(v14 + 283976) - load32(v4 + 280))
        store32(players[v11].total_resources, (load32(v14 + 283976) - load32(v4 + 280)))
        store32(v14 + 283980, (load32(v14 + 283980) - v16))
        if not (((v9 - 1) < 0) & (u32(v16) < u32(-2147483647))):
            store8(v14 + 286700, 1)
        v4 = ((v13 + (v11 * 286704)) + 281748)
        if (u32(v6) > u32(load32(((v13 + (v11 * 286704)) + 281748)))):
            store32(v4, v6)
        while True:  # $label3
            while True:  # $label2
                while True:  # $label1
                    # br_table (v10 - 4)
                    break
                    break
                v5 = (((v13 + (v11 * 286704)) + (v12 << 2)) + 282828)
                store32((((v13 + (v11 * 286704)) + (v12 << 2)) + 282828), (load32(v5) - 1))
                break
                break
            v4 = (((v13 + (v11 * 286704)) + (v12 << 2)) + 281808)
            v4 = (load32(v4) - 1)
            store32((((v13 + (v11 * 286704)) + (v12 << 2)) + 281808), (load32(v4) - 1))
            if v4:
                break
            while True:  # $label4
                if (load32(v14 + 283908) != load32(CURRENT_PLAYER)):
                    break
                if not load32(v5 + 244):
                    break
                while True:  # $label8
                    v10 = load32((load32(v5 + 240) + (v7 << 2)))
                    while True:  # $label5
                        if load8u(9147141):
                            break
                        v8 = 0
                        v4 = load32(9671120)
                        if not load32(9671120):
                            break
                        while True:  # $label7
                            while True:  # $label6
                                v6 = load32(((v8 << 2) + 9263072))
                                if not load32(((v8 << 2) + 9263072)):
                                    break
                                if (load32(v6 + 12) != v10):
                                    break
                                if load8u(v6 + 24):
                                    break
                                break
                                break
                            v8 = (v8 + 1)
                            if ((v8 + 1) != v4):
                                continue
                            break
                        break
                    v7 = (v7 + 1)
                    if (u32((v7 + 1)) < u32(load32(v5 + 244))):
                        continue
                    break
                break
            break
        while True:  # $label9
            v5 = load32(arg0 + 20)
            if not load32(arg0 + 20):
                break
            if not load32(v5 + 8):
                break
            func157(arg0)
            while True:  # $label10
                v5 = load32(9215884)
                v4 = load32(arg0 + 44)
                # br_table (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) - 2)
                break
                break
            if v4:
                store32((v5 + (v4 << 4)), 0)
            store32(arg0 + 44, 0)
            break
        while True:  # $label11
            v8 = load32((v13 + (v11 * 286704)) + 281796)
            if not load32((v13 + (v11 * 286704)) + 281796):
                break
            v7 = load32(v8 + 8)
            if not load32(v8 + 8):
                break
            v6 = load32(v8)
            v5 = 0
            v10 = (v13 + (v11 * 286704))
            while True:  # $label14
                v4 = (v6 + (v5 << 2))
                if (load32((v6 + (v5 << 2))) == load32(arg0 + 28)):
                    v4 = ((v10 + (load32(v4 + 4) << 2)) + 282828)
                    store32(((v10 + (load32(v4 + 4) << 2)) + 282828), (load32(v4) - 1))
                    v7 = (load32(v8 + 8) - 1)
                    store32(v8 + 8, (load32(v8 + 8) - 1))
                    v4 = v5
                    if (u32(v5) < u32(v7)):
                        while True:  # $label12
                            v4 = (v4 + 1)
                            store32((v6 + (v4 << 2)), load32((v6 + ((v4 + 1) << 2))))
                            v7 = load32(v8 + 8)
                            if (u32(v4) < u32(load32(v8 + 8))):
                                continue
                            break
                    v7 = (v7 - 1)
                    store32(v8 + 8, (v7 - 1))
                    v4 = v5
                    if (u32(v5) < u32(v7)):
                        while True:  # $label13
                            v4 = (v4 + 1)
                            store32((v6 + (v4 << 2)), load32((v6 + ((v4 + 1) << 2))))
                            v7 = load32(v8 + 8)
                            if (u32(v4) < u32(load32(v8 + 8))):
                                continue
                            break
                    v5 = (v5 - 2)
                v5 = (v5 + 2)
                if (u32((v5 + 2)) < u32(v7)):
                    continue
                break
            break
        store16(arg0 + 110, arg1)
        v7 = load32(PLAYERS)
        v8 = load16u(arg0 + 110)
        v6 = players[load16u(arg0 + 110)]
        v5 = (load32(v6 + 283976) + v9)
        store32(players[load16u(arg0 + 110)].total_resources, (load32(v6 + 283976) + v9))
        store32(v6 + 283980, (load32(v6 + 283980) + v16))
        if not ((v16 <= 0) & (v9 >= 0)):
            store8((v7 + (v8 * 286704)) + 286700, 1)
        arg1 = ((v7 + (v8 * 286704)) + 281748)
        if (u32(v5) > u32(load32(((v7 + (v8 * 286704)) + 281748)))):
            store32(arg1, v5)
        v4 = load32(arg0 + 28)
        while True:  # $label15
            arg1 = load32((((v13 + (v11 * 286704)) + (load8u(arg0 + 122) << 2)) + 284636))
            if not load32((((v13 + (v11 * 286704)) + (load8u(arg0 + 122) << 2)) + 284636)):
                break
            v10 = load32(arg1 + 8)
            if not load32(arg1 + 8):
                break
            v5 = load32(arg1)
            v9 = 0
            while True:  # $label16
                arg1 = (v5 + (v9 << 2))
                if (v4 != load32((v5 + (v9 << 2)))):
                    v9 = (v9 + 1)
                    if ((v9 + 1) != v10):
                        continue
                    break
                break
            if (v9 < 0):
                break
            store32(arg1, 0)
            v4 = load32(arg0 + 28)
            break
        func144(v6, v4, 1)
        if load32(9147132):
            arg1 = (v13 + (v11 * 286704))
            if load32((v13 + (v11 * 286704)) + 283908):
                store32(arg1 + 283956, (load32(arg1 + 283956) + load32(((v12 * 404) + ENTITY_TYPES) + 68)))
            arg1 = (v7 + (v8 * 286704))
            store32((v7 + (v8 * 286704)) + 283956, (load32(arg1 + 283956) - load32(((v12 * 404) + ENTITY_TYPES) + 68)))
        while True:  # $label17
            if not load8u(9142916):
                break
            v4 = load32(arg0 + 40)
            if not load32(arg0 + 40):
                break
            v5 = load8u(arg0 + 122)
            arg1 = load16u(arg0 + 110)
            store32(v15 + 4, v4)
            store32(v15, (v5 | (arg1 << 16)))
            a_b()
            break
        while True:  # $label20
            while True:  # $label19
                while True:  # $label18
                    # br_table (load8u(arg0 + 125) - 4)
                    break
                    break
                arg1 = (((v7 + (v8 * 286704)) + (load8u(arg0 + 122) << 2)) + 282828)
                store32((((v7 + (v8 * 286704)) + (load8u(arg0 + 122) << 2)) + 282828), (load32(arg1) + 1))
                break
                break
            v5 = (v7 + (v8 * 286704))
            arg1 = (((v7 + (v8 * 286704)) + (load8u(arg0 + 122) << 2)) + 281808)
            arg1 = load32(arg1)
            store32((((v7 + (v8 * 286704)) + (load8u(arg0 + 122) << 2)) + 281808), (load32(arg1) + 1))
            if arg1:
                break
            if (load32(v5 + 283908) != load32(CURRENT_PLAYER)):
                break
            v6 = ((v12 * 404) + ENTITY_TYPES)
            if not load32(((v12 * 404) + ENTITY_TYPES) + 244):
                break
            v5 = 0
            while True:  # $label24
                v4 = load32((load32(v6 + 240) + (v5 << 2)))
                while True:  # $label21
                    if load8u(9147141):
                        break
                    v9 = 0
                    arg1 = load32(9671120)
                    if not load32(9671120):
                        break
                    while True:  # $label23
                        while True:  # $label22
                            v10 = load32(((v9 << 2) + 9263072))
                            if not load32(((v9 << 2) + 9263072)):
                                break
                            if (load32(v10 + 12) != v4):
                                break
                            if load8u(v10 + 24):
                                break
                            break
                            break
                        v9 = (v9 + 1)
                        if ((v9 + 1) != arg1):
                            continue
                        break
                    break
                v5 = (v5 + 1)
                if (u32((v5 + 1)) < u32(load32(v6 + 244))):
                    continue
                break
            break
        if arg3:
        func77(arg0)
        if load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 20):
        func387(v14)
        if not arg2:
            break
        while True:  # $label25
            arg1 = load32(arg0 + 44)
            if not load32(arg0 + 44):
                break
            if load32((load32(9215884) + (arg1 << 4)) + 4):
                break
            store8(arg0 + 123, 0)
            store32(arg0 + 32, 0)
            store32(arg0 + 116, load32(arg0 + 112))
            break
            break
        func29(arg0, 1)
        break
    G.global0 = (v15 + 16)

# ----------------------------------------------------------
# $func79
# ----------------------------------------------------------
def func79(arg0, arg1, arg2):
    if not arg2:
        return (load32(arg0 + 4) == load32(arg1 + 4))
    if (arg0 == arg1):
        return 1
    arg2 = load32(arg1 + 4)
    arg1 = load8u(load32(arg1 + 4))
    while True:  # $label0
        v3 = load32(arg0 + 4)
        arg0 = load8u(load32(arg0 + 4))
        if not load8u(load32(arg0 + 4)):
            break
        if (arg0 != arg1):
            break
        while True:  # $label1
            arg1 = load8u(arg2 + 1)
            arg0 = load8u(v3 + 1)
            if not load8u(v3 + 1):
                break
            arg2 = (arg2 + 1)
            v3 = (v3 + 1)
            if (arg0 == arg1):
                continue
            break
        break
    return (arg0 == arg1)

# ----------------------------------------------------------
# $func80
# ----------------------------------------------------------
def func80(arg0, arg1, arg2, arg3, arg4):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if load8u(9142917):
            break
        v5 = load32(9299880)
        if load32(9299880):
            v5 = (v5 - 1)
            store32(9299880, (v5 - 1))
            v5 = load32((load32(9299872) + (v5 << 2)))
            break
        v5 = load32(9163776)
        v6 = (load32(9163776) + 1)
        store32(9163776, (load32(9163776) + 1))
        v9 = load32(9163784)
        if (u32(v6) < u32(load32(9163784))):
            break
        store32(v7, v9)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    while True:  # $label1
        if not arg2:
            break
        v6 = load32(arg2 + 16)
        arg2 = load32(arg2 + 24)
        if (load32(arg2 + 24) >= 100):
            arg0 = loadf32((((arg2 + v6) << 2) + 32700))
            if not ((loadf32((((arg2 + v6) << 2) + 32700)) < 4294967300.0) & (arg0 >= 0.0)):
                break
            v8 = i32(arg0)
            break
        v8 = ((v6 * 1000) // arg2)
        break
    G.global0 = (v7 + 16)

# ----------------------------------------------------------
# $func81
# ----------------------------------------------------------
def func81(arg0, arg1, arg2, arg3):
    v16 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v5 = load8u(arg0 + 122)
        v6 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 188) != 55):
            if (load32(v6 + 264) == 1):
                break
        v8 = load8u(arg1 + 122)
        arg2 = (load32((((load8u(arg1 + 122) * 1020) + 9299904) + (v5 << 2))) * arg2)
        # TODO: i32.div_u
        v6 = 100
        if (u32(arg2) < u32(100)):
            break
        while True:  # $label1
            v4 = load8u(arg0 + 125)
            if (load8u(arg0 + 125) == 9):
                arg2 = 0
                if (load32(38452) == v5):
                    break
                if (load32(38496) == v5):
                    break
                if (load32(38756) == v5):
                    break
                if (load32(38692) == v5):
                    break
                if (load32(38696) == v5):
                    break
                if (load32(38776) == v5):
                    break
                if (load32(38752) == v5):
                    break
                if (load32(38704) == v5):
                    break
            arg2 = load32(arg0 + 60)
            break
        v7 = (v6 * v6)
        arg2 = (arg2 + v6)
        # TODO: i32.div_u
        v7 = load32(arg0 + 64)
        arg2 = (((v6 * v6) if (u32(arg2) > u32(v7)) else (arg2 + v6)) if (load32(arg0 + 64) != -1) else 0)
        v10 = load32(PLAYERS)
        v11 = load16u(arg1 + 110)
        v6 = players[load16u(arg1 + 110)]
        while True:  # $label2
            if (load32(38564) == v5):
                break
            v7 = (arg2 if (u32(arg2) < u32(v7)) else v7)
            v9 = load16u(arg0 + 110)
            v12 = load32(v6 + 278556)
            if load32(v6 + 278556):
                v8 = (v12 + (((v9 * 255) + v8) << 2))
                store32((v12 + (((v9 * 255) + v8) << 2)), (load32(v8) + v7))
            v9 = load32(((v10 + (v9 * 286704)) + 278564))
            if not load32(((v10 + (v9 * 286704)) + 278564)):
                break
            v5 = (v9 + (((v11 * 255) + v5) << 2))
            store32((v9 + (((v11 * 255) + v5) << 2)), (load32(v5) + v7))
            break
        while True:  # $label3
            if (v4 == 3):
                break
            v5 = load32(arg0 + 64)
            if (u32(arg2) < u32(load32(arg0 + 64))):
                store32(arg0 + 64, (v5 - arg2))
                if not load32(arg0 + 92):
                    break
                if load8u(9147141):
                    break
                store32(v16, arg2)
                a_b()
                break
            v5 = ((v4 == 4) | (v4 == 14))
            store32(arg0 + 64, 0)
            while True:  # $label4
                if (load32(load32(GAME_STATE) + 120) != 3):
                    break
                if not load8u((load32(9143004) + (load16u(arg1 + 110) + (load32(PLAYER_COUNT) * load16u(arg0 + 110))))):
                    break
                if load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264):
                    break
                arg2 = 1
                store8(v6 + 286701, 1)
                while True:  # $label5
                    v4 = load32(PLAYER_COUNT)
                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                        break
                    v12 = (v4 - 1)
                    v14 = ((v4 - 1) & 1)
                    v7 = (load32(v6 + 283908) * v4)
                    v9 = load32(PLAYERS)
                    v8 = load32(9143016)
                    if (v4 != 2):
                        v4 = (v12 & -2)
                        v6 = 0
                        while True:  # $label6
                            if load8u((v8 + (arg2 + v7))):
                                store8((v9 + (arg2 * 286704)) + 286701, 1)
                            v12 = (arg2 + 1)
                            if load8u((v8 + (v7 + (arg2 + 1)))):
                                store8((v9 + (v12 * 286704)) + 286701, 1)
                            arg2 = (arg2 + 2)
                            v6 = (v6 + 2)
                            if ((v6 + 2) != v4):
                                continue
                            break
                    if not v14:
                        break
                    if not load8u((v8 + (arg2 + v7))):
                        break
                    store8((v9 + (arg2 * 286704)) + 286701, 1)
                    break
                arg2 = (v10 + (v11 * 286704))
                v6 = load32(GAME_STATE)
                store32((v10 + (v11 * 286704)) + 283848, (load32(arg2 + 283848) + load32(load32(GAME_STATE) + 100)))
                v4 = (arg2 + 283852)
                store32((arg2 + 283852), (load32(v4) + load32(v6 + 104)))
                v4 = (arg2 + 283856)
                store32((arg2 + 283856), (load32(v4) + load32(v6 + 108)))
                arg2 = (arg2 + 283860)
                store32((arg2 + 283860), (load32(arg2) + load32(v6 + 112)))
                break
            func155(arg1, arg0, v5)
            while True:  # $label7
                v6 = load8u(arg0 + 122)
                if not load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264):
                    arg2 = load32(38472)
                    break
                arg2 = load32(38472)
                if ((load32(38600) != v6) & (load32(38472) != v6)):
                    break
                if not v5:
                    break
                break
            while True:  # $label8
                if not (v5 & (arg2 == v6)):
                    v9 = load16u(arg0 + 110)
                    break
                store32(59200, load32(arg0 + 28))
                v6 = load32(ENTITIES)
                arg2 = 1
                v4 = 0
                while True:  # $label13
                    v10 = (v6 + (load32(((v4 << 2) + 59200)) * 132))
                    v8 = load16u(v10 + 112)
                    v14 = (load16u(v10 + 112) + 1)
                    v7 = load32(9142440)
                    v5 = (load32(9142440) + 2)
                    v9 = load16u(arg0 + 110)
                    v11 = load32(38472)
                    v6 = load32(ENTITIES)
                    v12 = load32(9142840)
                    while True:  # $label9
                        v10 = load16u(v10 + 114)
                        v17 = (u32(v7) <= u32(load16u(v10 + 114)))
                        if (u32(v7) <= u32(load16u(v10 + 114))):
                            break
                        if (u32(v7) <= u32(v14)):
                            break
                        v13 = (v6 + (load32((((v8 + (((v5 + v10) + 1) * v5)) << 2) + v12) + 8) * 132))
                        if (v11 != load8u((v6 + (load32((((v8 + (((v5 + v10) + 1) * v5)) << 2) + v12) + 8) * 132)) + 122)):
                            break
                        if (load8u(v13 + 125) != 4):
                            break
                        if (load16u(v13 + 110) != v9):
                            break
                        store32(((arg2 << 2) + 59200), load32(v13 + 28))
                        arg2 = (arg2 + 1)
                        break
                    while True:  # $label10
                        if not v10:
                            break
                        if (u32(v7) <= u32((v10 - 1))):
                            break
                        if (u32(v7) <= u32(v8)):
                            break
                        v13 = (v6 + (load32((v12 + ((v14 + ((v5 + v10) * v5)) << 2))) * 132))
                        if (v11 != load8u((v6 + (load32((v12 + ((v14 + ((v5 + v10) * v5)) << 2))) * 132)) + 122)):
                            break
                        if (load8u(v13 + 125) != 4):
                            break
                        if (load16u(v13 + 110) != v9):
                            break
                        store32(((arg2 << 2) + 59200), load32(v13 + 28))
                        arg2 = (arg2 + 1)
                        break
                    v15 = (v10 + 1)
                    while True:  # $label11
                        if v17:
                            break
                        if (u32(v7) <= u32((v8 - 1))):
                            break
                        if not v8:
                            break
                        v13 = (v6 + (load32((v12 + ((((v5 + v15) * v5) + v8) << 2))) * 132))
                        if (v11 != load8u((v6 + (load32((v12 + ((((v5 + v15) * v5) + v8) << 2))) * 132)) + 122)):
                            break
                        if (load8u(v13 + 125) != 4):
                            break
                        if (load16u(v13 + 110) != v9):
                            break
                        store32(((arg2 << 2) + 59200), load32(v13 + 28))
                        arg2 = (arg2 + 1)
                        break
                    while True:  # $label12
                        if (u32(v7) <= u32(v15)):
                            break
                        if (u32(v7) <= u32(v8)):
                            break
                        v5 = (v6 + (load32((v12 + ((v14 + (((v5 + v10) + 2) * v5)) << 2))) * 132))
                        if (v11 != load8u((v6 + (load32((v12 + ((v14 + (((v5 + v10) + 2) * v5)) << 2))) * 132)) + 122)):
                            break
                        if (load8u(v5 + 125) != 4):
                            break
                        if (load16u(v5 + 110) != v9):
                            break
                        store32(((arg2 << 2) + 59200), load32(v5 + 28))
                        arg2 = (arg2 + 1)
                        break
                    if (u32(v4) > u32(34)):
                        break
                    v4 = (v4 + 1)
                    if (u32((v4 + 1)) < u32(arg2)):
                        continue
                    break
                break
            if not load8u((load32(9143004) + (load16u(arg1 + 110) + (load32(PLAYER_COUNT) * v9)))):
                break
            if not arg3:
                break
            while True:  # $label14
                arg0 = load32(PLAYERS)
                v6 = load16u(arg1 + 110)
                if not load32((players[load16u(arg1 + 110)] + 284008)):
                    break
                if not load8u(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 334):
                    break
                arg2 = (load32(arg1 + 80) + 100)
                store32(arg1 + 80, (load32(arg1 + 80) + 100))
                while True:  # $label15
                    arg3 = load32(arg1 + 84)
                    v5 = (arg0 + (v6 * 286704))
                    if (u32(load32(arg1 + 84)) < u32(load32(((arg0 + (v6 * 286704)) + 284388)))):
                        break
                    if (load32(((v5 + (load32(39180) << 2)) + 281808)) != 1):
                        break
                    v12 = load16u(arg1 + 114)
                    v17 = load32(arg1 + 28)
                    while True:  # $label16
                        v15 = load16u(arg1 + 112)
                        arg0 = load32((players[v6] + 284336))
                        arg2 = (load16u(arg1 + 112) - load32((players[v6] + 284336)))
                        arg3 = (arg0 << 1)
                        v18 = ((arg0 << 1) + v15)
                        if ((load16u(arg1 + 112) - load32((players[v6] + 284336))) >= ((arg0 << 1) + v15)):
                            break
                        v5 = (v12 - arg0)
                        v19 = (arg3 + v12)
                        if ((v12 - arg0) >= (arg3 + v12)):
                            break
                        v20 = (arg0 * arg0)
                        v21 = (v6 * 286704)
                        while True:  # $label24
                            arg3 = (arg2 + 1)
                            arg0 = (arg2 - v15)
                            v22 = (((arg2 - v15) * arg0) - 1)
                            arg0 = v5
                            while True:  # $label23
                                while True:  # $label17
                                    v4 = (arg0 - v12)
                                    if ((v22 + ((arg0 - v12) * v4)) > v20):
                                        break
                                    v4 = load32(9142440)
                                    if (u32(load32(9142440)) <= u32(arg0)):
                                        break
                                    if ((arg0 | arg2) < 0):
                                        break
                                    if (u32(arg2) >= u32(v4)):
                                        break
                                    v23 = (arg0 + 1)
                                    v14 = 0
                                    while True:  # $label22
                                        while True:  # $label18
                                            v4 = (load32(9142440) + 2)
                                            v4 = load32((load32(9142840) + ((arg3 + ((v23 + ((load32(9142440) + 2) * v14)) * v4)) << 2)))
                                            if (u32(load32((load32(9142840) + ((arg3 + ((v23 + ((load32(9142440) + 2) * v14)) * v4)) << 2)))) < u32(3)):
                                                break
                                            if (v4 == v17):
                                                break
                                            v4 = entities[v4]
                                            if (load16u(entities[v4] + 110) != v6):
                                                break
                                            v10 = load8u(v4 + 122)
                                            if not load8u(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 334):
                                                break
                                            v8 = load32(v4 + 84)
                                            if (u32(load32(v4 + 84)) > u32(10)):
                                                break
                                            v7 = (load32(v4 + 80) + 100)
                                            store32(v4 + 80, (load32(v4 + 80) + 100))
                                            v9 = (load32(PLAYERS) + v21)
                                            # TODO: i32.div_u
                                            if (u32((v8 * 100)) < u32(load32(((load32(PLAYERS) + v21) + 284008)))):
                                                break
                                            v11 = load32((v9 + 284012))
                                            v7 = 10
                                            while True:  # $label19
                                                if load32(((v9 + (load32(38488) << 2)) + 281808)):
                                                    break
                                                if load32(((v9 + (load32(38848) << 2)) + 281808)):
                                                    break
                                                v7 = (10 if load32(((v9 + (load32(38916) << 2)) + 281808)) else 0)
                                                break
                                            if (u32(v8) >= u32((v7 + v11))):
                                                break
                                            store32(v4 + 80, 0)
                                            v7 = (v8 + 1)
                                            store32(v4 + 84, (v8 + 1))
                                            v8 = (v9 + 281672)
                                            store32((v9 + 281672), (load32(v8) + 1))
                                            if (load32((v9 + 284388)) == v7):
                                                v7 = load32(v4 + 24)
                                                if not load32(v4 + 24):
                                                    v7 = func26(16)
                                                    store64(func26(16), 0)
                                                    store64(v7 + 8, 0)
                                                    store32(v4 + 24, v7)
                                                if not load32(v7 + 8):
                                                    v8 = func26(16)
                                                    store32(func26(16) + 4, 20)
                                                    store32(v8, func26(80))
                                                    store64(v8 + 8, 8589934592)
                                                    store32(v7 + 8, v8)
                                                    v10 = 0
                                                    v7 = load32(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 196)
                                                    v24 = ((load32(players[load16u(v4 + 110)] + 283936) * 20) % load16u(((load32(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 196) << 1) + 9142944)))
                                                    v25 = ((v7 << 2) + 9142928)
                                                    while True:  # $label21
                                                        v26 = load16u((load32(v25) + ((v10 + v24) << 1)))
                                                        if load16u((load32(v25) + ((v10 + v24) << 1))):
                                                            while True:  # $label20
                                                                v8 = load32(load32(v4 + 24) + 8)
                                                                v7 = load32(load32(load32(v4 + 24) + 8) + 8)
                                                                if (load32(load32(load32(v4 + 24) + 8) + 8) != load32(v8 + 4)):
                                                                    v11 = load32(v8)
                                                                    break
                                                                v11 = (load32(v8 + 12) + v7)
                                                                store32(v8 + 4, (load32(v8 + 12) + v7))
                                                                v13 = load32(v8)
                                                                v11 = func26((-1 if (u32(v11) > u32(1073741823)) else (v11 << 2)))
                                                                if v7:
                                                                    # TODO: memory.copy
                                                                if v13:
                                                                    v7 = load32(v8 + 8)
                                                                store32(v8, v11)
                                                                break
                                                            store32(v8 + 8, (v7 + 1))
                                                            store32((v11 + (v7 << 2)), v26)
                                                        v10 = (v10 + 1)
                                                        if ((v10 + 1) != 20):
                                                            continue
                                                        break
                                                store32(v9 + 283936, (load32(v9 + 283936) + 1))
                                                v7 = (v9 + 281636)
                                                store32((v9 + 281636), (load32(v7) + 1))
                                                v10 = load8u(v4 + 122)
                                            v7 = (v9 + 284020)
                                            store32(v4 + 64, (load32(v4 + 64) + load32((v9 + 284020))))
                                            store32(v4 + 68, (load32(v4 + 68) + load32(v7)))
                                            v7 = load32(v4 + 84)
                                            v9 = (load32(v4 + 84) & 1)
                                            v8 = (load32(((v10 * 404) + ENTITY_TYPES) + 224) > 1)
                                            store32(v4 + 52, (load32(v4 + 52) + ((load32(v4 + 84) & 1) if (load32(((v10 * 404) + ENTITY_TYPES) + 224) > 1) else 1)))
                                            store32(v4 + 60, (load32(v4 + 60) + (((v7 & 3) == 1) if v8 else v9)))
                                            if not load32(v4 + 92):
                                                break
                                            if load32(9140316):
                                                if (load32(9140320) != load32(v4 + 28)):
                                                    break
                                            break
                                        v14 = (v14 + 1)
                                        if ((v14 + 1) != 3):
                                            continue
                                        break
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v19):
                                    continue
                                break
                            arg2 = arg3
                            if (arg3 != v18):
                                continue
                            break
                        break
                    v6 = load16u(arg1 + 110)
                    arg3 = load32(arg1 + 84)
                    arg2 = load32(arg1 + 80)
                    arg0 = load32(PLAYERS)
                    break
                # TODO: i32.div_u
                if (u32((arg3 * 100)) < u32(load32(((arg0 + (v6 * 286704)) + 284008)))):
                    break
                v5 = (arg0 + (v6 * 286704))
                v4 = load32(((arg0 + (v6 * 286704)) + 284012))
                arg2 = 10
                while True:  # $label25
                    if load32(((v5 + (load32(38488) << 2)) + 281808)):
                        break
                    if load32(((v5 + (load32(38848) << 2)) + 281808)):
                        break
                    arg2 = (10 if load32((((arg0 + (v6 * 286704)) + (load32(38916) << 2)) + 281808)) else 0)
                    break
                if (u32(arg3) >= u32((arg2 + v4))):
                    break
                func198(arg1)
                break
            break
            break
        while True:  # $label26
            arg2 = load32(ENTITIES)
            arg3 = load32(arg1 + 28)
            if not load8u((load32(9143004) + (load16u(arg0 + 110) + (load32(PLAYER_COUNT) * load16u(entities[load32(arg1 + 28)] + 110))))):
                break
            if (load8u(arg0 + 126) == 2):
                break
            while True:  # $label28
                while True:  # $label27
                    v4 = load32(9215884)
                    v5 = load32(arg0 + 44)
                    v6 = load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4)
                    if not ((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 22) | not v5):
                        break
                    if load8u(arg0 + 125):
                        break
                    if load32(arg0 + 36):
                        break
                    arg1 = load8u(arg0 + 122)
                    if load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 260):
                        break
                    break
                if (load8u(arg0 + 129) != 5):
                    break
                if (v6 != 6):
                    break
                v7 = load16u(arg0 + 114)
                v6 = (arg2 + (arg3 * 132))
                arg1 = (load16u(arg0 + 114) - load16u((arg2 + (arg3 * 132)) + 114))
                v9 = load16u(arg0 + 112)
                arg1 = (load16u(arg0 + 112) - load16u(v6 + 112))
                arg1 = (((load16u(arg0 + 114) - load16u((arg2 + (arg3 * 132)) + 114)) * arg1) + ((load16u(arg0 + 112) - load16u(v6 + 112)) * arg1))
                v6 = ((load8u(v6 + 122) * 404) + ENTITY_TYPES)
                if (load32(((load8u(v6 + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                    arg1 = (arg1 if (load32(v6 + 268) == 1) else (arg1 + 100))
                v6 = (arg2 + (load32((v4 + ((v5 << 4) | 12))) * 132))
                v5 = (v7 - load16u((arg2 + (load32((v4 + ((v5 << 4) | 12))) * 132)) + 114))
                v5 = (v9 - load16u(v6 + 112))
                v5 = (((v7 - load16u((arg2 + (load32((v4 + ((v5 << 4) | 12))) * 132)) + 114)) * v5) + ((v9 - load16u(v6 + 112)) * v5))
                v6 = load8u(v6 + 122)
                if (load32(((load8u(v6 + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                else:
                if (v5 <= arg1):
                    break
                arg1 = load8u(arg0 + 122)
                break
            while True:  # $label29
                arg1 = ((arg1 * 404) + ENTITY_TYPES)
                if not load32(((arg1 * 404) + ENTITY_TYPES) + 228):
                    if load32(arg1 + 260):
                        break
                v6 = load32(arg0 + 28)
                v5 = load32(((load8u((arg2 + (load32(arg0 + 28) * 132)) + 122) * 404) + ENTITY_TYPES) + 228)
                if not load32(((load8u((arg2 + (load32(arg0 + 28) * 132)) + 122) * 404) + ENTITY_TYPES) + 228):
                    break
                arg1 = load32(((load8u((arg2 + (arg3 * 132)) + 122) * 404) + ENTITY_TYPES) + 216)
                if not load32(((load8u((arg2 + (arg3 * 132)) + 122) * 404) + ENTITY_TYPES) + 216):
                    break
                v4 = (arg2 + (arg3 * 132))
                v7 = load16u((arg2 + (arg3 * 132)) + 114)
                arg2 = (arg2 + (v6 * 132))
                v9 = load16u((arg2 + (v6 * 132)) + 114)
                v8 = load16u(v4 + 112)
                v10 = load16u(arg2 + 112)
                v5 = (v5 * v5)
                v6 = 0
                v4 = 1
                while True:  # $label32
                    arg2 = (v9 - (v6 + v7))
                    v11 = ((v9 - (v6 + v7)) * arg2)
                    arg2 = 0
                    while True:  # $label31
                        while True:  # $label30
                            v12 = (v10 - (arg2 + v8))
                            if (u32(v5) > u32((((v10 - (arg2 + v8)) * v12) + v11))):
                                arg2 = (arg2 + 1)
                                if (arg1 != (arg2 + 1)):
                                    continue
                                break
                            break
                        if not v4:
                            break
                        break
                        break
                    v6 = (v6 + 1)
                    v4 = (u32((v6 + 1)) < u32(arg1))
                    if (arg1 != v6):
                        continue
                    break
                break
                break
            break
        func103(arg0)
        break
    G.global0 = (v16 + 16)
    return arg2

# ----------------------------------------------------------
# $func82
# ----------------------------------------------------------
def func82(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if (arg1 <= 0):
            break
        v6 = (arg0 - -64)
        while True:  # $label3
            if (load32(v6) < load32(arg0 + 56)):
                if (load32(arg0 + 24) <= 0):
                    break
            if load32(arg0 + 4):
                store64(arg0 + 76, rotl(load64(arg0 + 76), 32))
            if (load32(arg0 + 60) >= load32(arg0 + 48)):
                a_c()
                raise Unreachable()
            while True:  # $label1
                if load32(arg0 + 4):
                    break
                if ((load32(arg0 + 52) * load32(arg0 + 8)) <= 0):
                    break
                v7 = load32(arg0 + 76)
                v8 = load32(arg0 + 80)
                v4 = 0
                while True:  # $label2
                    v9 = (v4 << 2)
                    v10 = (v7 + (v4 << 2))
                    store32((v7 + (v4 << 2)), (load32(v10) + load32((v8 + v9))))
                    v4 = (v4 + 1)
                    if ((v4 + 1) < (load32(arg0 + 52) * load32(arg0 + 8))):
                        continue
                    break
                break
            store32(arg0 + 60, (load32(arg0 + 60) + 1))
            store32(arg0 + 24, (load32(arg0 + 24) - load32(arg0 + 32)))
            arg2 = (arg2 + arg3)
            v5 = (v5 + 1)
            if ((v5 + 1) != arg1):
                continue
            break
        v5 = arg1
        break
    return v5

# ----------------------------------------------------------
# $func83
# ----------------------------------------------------------
def func83(arg0, arg1, arg2, arg3):
    v8 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    v6 = (arg1 + 24)
    v7 = func39((arg1 + 24), 1)
    # TODO: memory.fill
    while True:  # $label10
        while True:  # $label9
            while True:  # $label0
                if v7:
                    v7 = func39(v6, 1)
                    store32((arg2 + (func39(v6, (8 if func39(v6, 1) else 1)) << 2)), 1)
                    if (v7 != 1):
                        break
                    store32((arg2 + (func39(v6, 8) << 2)), 1)
                    break
                # TODO: memory.fill
                v7 = (func39(v6, 4) + 4)
                if ((func39(v6, 4) + 4) <= 19):
                    if (v7 > 0):
                        while True:  # $label1
                            store32((v8 + (load8u((v4 + 13808)) << 2)), func39(v6, 3))
                            v4 = (v4 + 1)
                            if ((v4 + 1) != v7):
                                continue
                            break
                    while True:  # $label2
                        if not func452(128, (v8 + 76)):
                            break
                        if not func457((v8 + 76), 7, v8, 19):
                            break
                        v10 = arg0
                        if func39(v6, 1):
                            v10 = (func39(v6, ((func39(v6, 3) << 1) + 2)) + 2)
                            if ((func39(v6, ((func39(v6, 3) << 1) + 2)) + 2) > arg0):
                                break
                        while True:  # $label3
                            if (arg0 <= 0):
                                break
                            v11 = 8
                            while True:  # $label7
                                if not v10:
                                    break
                                v4 = load32(arg1 + 44)
                                if (load32(arg1 + 44) >= 32):
                                    func135(v6)
                                    v4 = load32(arg1 + 44)
                                v7 = (load32(load32(v8 + 92)) + ((i32(((load64(arg1 + 24) & 0xFFFFFFFF) >> i32((v4 & 63)))) & 127) << 2))
                                store32(arg1 + 44, (v4 + load8u((load32(load32(v8 + 92)) + ((i32(((load64(arg1 + 24) & 0xFFFFFFFF) >> i32((v4 & 63)))) & 127) << 2)))))
                                while True:  # $label4
                                    v4 = load16u(v7 + 2)
                                    if (u32(load16u(v7 + 2)) <= u32(15)):
                                        store32((arg2 + (v5 << 2)), v4)
                                        v11 = (v4 if v4 else v11)
                                        v5 = (v5 + 1)
                                        break
                                    v12 = (load8u((v4 + 13814)) + func39(v6, load8u((v4 + 13811))))
                                    v7 = ((load8u((v4 + 13814)) + func39(v6, load8u((v4 + 13811)))) + v5)
                                    if (((load8u((v4 + 13814)) + func39(v6, load8u((v4 + 13811)))) + v5) > arg0):
                                        break
                                    if (v12 <= 0):
                                        break
                                    v9 = (v11 if (v4 == 16) else 0)
                                    v13 = 0
                                    v4 = (v12 & 7)
                                    if (v12 & 7):
                                        while True:  # $label5
                                            store32((arg2 + (v5 << 2)), v9)
                                            v5 = (v5 + 1)
                                            v13 = (v13 + 1)
                                            if ((v13 + 1) != v4):
                                                continue
                                            break
                                    if (u32((v12 - 1)) >= u32(7)):
                                        while True:  # $label6
                                            v4 = (arg2 + (v5 << 2))
                                            store32((arg2 + (v5 << 2)), v9)
                                            store32(v4 + 28, v9)
                                            store32(v4 + 24, v9)
                                            store32(v4 + 20, v9)
                                            store32(v4 + 16, v9)
                                            store32(v4 + 12, v9)
                                            store32(v4 + 8, v9)
                                            store32(v4 + 4, v9)
                                            v5 = (v5 + 8)
                                            if ((v5 + 8) != v7):
                                                continue
                                            break
                                    v5 = v7
                                    break
                                v10 = (v10 - 1)
                                if (arg0 > v5):
                                    continue
                                break
                            break
                        func116((v8 + 76))
                        break
                        break
                    func116((v8 + 76))
                    while True:  # $label8
                        # br_table load32(arg1)
                        break
                        break
                    store32(arg1, 3)
                    break
                a_c()
                raise Unreachable()
                break
            if load32(arg1 + 48):
                break
            v4 = func457(arg3, 8, arg2, arg0)
            if func457(arg3, 8, arg2, arg0):
                break
            break
        v4 = 0
        while True:  # $label11
            # br_table load32(arg1)
            break
            break
        store32(arg1, 3)
        break
    G.global0 = (v8 + 96)
    return v4

# ----------------------------------------------------------
# $func84
# ----------------------------------------------------------
def func84(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    if (arg3 > 0):
        v17 = ((arg4 << 1) | 1)
        v18 = (arg1 * 3)
        v19 = (0 - arg1)
        v20 = (arg1 * -3)
        v21 = (0 - (arg1 << 2))
        v22 = (arg1 << 1)
        v23 = (0 - (arg1 << 1))
        v24 = load32(16076)
        v10 = load32(17088)
        v11 = load32(16308)
        v8 = load32(17616)
        while True:  # $label2
            arg4 = arg3
            while True:  # $label0
                v25 = (arg0 + v23)
                v9 = load8u((arg0 + v23))
                v12 = (arg0 + arg1)
                v14 = load8u((arg0 + arg1))
                v15 = (load8u((arg0 + v23)) - load8u((arg0 + arg1)))
                v16 = (arg0 + v19)
                arg3 = load8u((arg0 + v19))
                v13 = load8u(arg0)
                if ((load8u((v8 + (load8u((arg0 + v23)) - load8u((arg0 + arg1))))) + (load8u((v8 + (load8u((arg0 + v19)) - load8u(arg0)))) << 2)) > v17):
                    break
                v7 = load8u((arg0 + v20))
                if (load8u((v8 + (load8u((arg0 + v21)) - load8u((arg0 + v20))))) > arg5):
                    break
                if (load8u((v8 + (v7 - v9))) > arg5):
                    break
                v26 = load8u((v8 + (v9 - arg3)))
                if (load8u((v8 + (v9 - arg3))) > arg5):
                    break
                v7 = load8u((arg0 + v22))
                if (load8u((v8 + (load8u((arg0 + v18)) - load8u((arg0 + v22))))) > arg5):
                    break
                if (load8u((v8 + (v7 - v14))) > arg5):
                    break
                v27 = load8u((v8 + (v14 - v13)))
                if (load8u((v8 + (v14 - v13))) > arg5):
                    break
                v7 = ((v13 - arg3) * 3)
                while True:  # $label1
                    if not ((arg6 >= v26) & (arg6 >= v27)):
                        v12 = (v7 + load8s((v15 + v24)))
                        v9 = load8s((v11 + (((v7 + load8s((v15 + v24))) + 4) >> 3)))
                        store8(v16, load8u((v10 + (load8s((v11 + ((v12 + 3) >> 3))) + arg3))))
                        v12 = arg0
                        break
                    v15 = load8s((v11 + ((v7 + 3) >> 3)))
                    v9 = load8s((v11 + ((v7 + 4) >> 3)))
                    v7 = ((load8s((v11 + ((v7 + 4) >> 3))) + 1) >> 1)
                    store8(v25, load8u((v10 + (v9 + ((load8s((v11 + ((v7 + 4) >> 3))) + 1) >> 1)))))
                    store8(v16, load8u((v10 + (arg3 + v15))))
                    store8(arg0, load8u((v10 + (v13 - v9))))
                    break
                arg3 = (v14 - v7)
                store8(v12, load8u((arg3 + v10)))
                break
            arg3 = (arg4 - 1)
            arg0 = (arg0 + arg2)
            if (u32(arg4) > u32(1)):
                continue
            break
    return (v13 - v9)

# ----------------------------------------------------------
# $func85
# ----------------------------------------------------------
def func85(arg0, arg1, param2):
    store8(arg0 + 125, 1)
    while True:  # $label0
        v4 = load32(9142840)
        v6 = load16u(arg0 + 112)
        v8 = load16u(arg0 + 114)
        v2 = (load32(9142440) + 2)
        v3 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        if (load32((load32(9142840) + ((load16u(arg0 + 112) + (((load16u(arg0 + 114) + ((load32(9142440) + 2) * load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 208))) + 1) * v2)) << 2)) + 4) != load32(v3 + 212)):
            break
        if not load32(v3 + 216):
            break
        while True:  # $label2
            v5 = (v5 + 1)
            v9 = ((v5 + 1) + v6)
            v2 = 0
            while True:  # $label1
                v2 = (v2 + 1)
                v7 = (load32(9142440) + 2)
                store32((v4 + ((v9 + ((((v2 + 1) + v8) + ((load32(9142440) + 2) * load32(v3 + 208))) * v7)) << 2)), load32(arg0 + 28))
                v7 = load32(v3 + 216)
                if (u32(v2) < u32(load32(v3 + 216))):
                    continue
                break
            if (u32(v5) < u32(v7)):
                continue
            break
        break
    func92(arg0, 0.0, 0.0)
    if load8u(9142916):
    while True:  # $label8
        while True:  # $label11
            while True:  # $label3
                v2 = load8u(arg0 + 123)
                if not load8u(arg0 + 123):
                    break
                if not arg1:
                    break
                while True:  # $label5
                    arg1 = load32(arg0 + 96)
                    if load32(arg0 + 96):
                        while True:  # $label4
                            v3 = load32(ENTITIES)
                            v2 = entities[arg1]
                            if (load32(entities[arg1].action) != load32(arg0 + 28)):
                                break
                            if (load8u(v2 + 125) == 3):
                                break
                            arg1 = (v3 + (arg1 * 132))
                            if load32(((load8u((v3 + (arg1 * 132)) + 122) * 404) + ENTITY_TYPES) + 268):
                                arg1 = load32(arg1 + 52)
                                store32(arg1 + 52, (load32(arg1 + 52) - 1))
                                if (u32(arg1) >= u32(2)):
                                    break
                            break
                            break
                        func29(arg0, 0)
                        return func32(func60(arg0, 1.0), v2, 0)
                    v3 = load32(PLAYERS)
                    v5 = load16u(arg0 + 110)
                    arg1 = players[load16u(arg0 + 110)]
                    while True:  # $label6
                        v4 = ((v2 * 40) + 9671200)
                        if not load8u(((v2 * 40) + 9671200) + 18):
                            break
                        while True:  # $label7
                            v6 = (load32(arg1 + 283976) + 1)
                            if (u32((load32(arg1 + 283976) + 1)) > u32((load32((arg1 + 284136)) + load32(arg1 + 283980)))):
                                v2 = 57101
                                if (load32((v3 + (v5 * 286704)) + 283908) == load32(CURRENT_PLAYER)):
                                    break
                                break
                            v3 = (v3 + (v5 * 286704))
                            if (u32(v6) <= u32(load32(((v3 + (v5 * 286704)) + 284000)))):
                                break
                            v2 = 57113
                            if (load32(v3 + 283908) != load32(CURRENT_PLAYER)):
                                break
                            break
                        a_b()
                        break
                        break
                    v3 = load32(v4 + 12)
                    if load32(v4 + 12):
                        if func66(arg1, v3, 1, 1):
                            break
                    else:
                    v2 = load32(((v2 * 40) + 9671200) + 8)
                    arg1 = (G.global0 - 16)
                    G.global0 = (G.global0 - 16)
                    v3 = 1
                    while True:  # $label9
                        if not v2:
                            break
                        v5 = load32(arg0 + 72)
                        v4 = players[load16u(arg0 + 110)]
                        v2 = load32(((players[load16u(arg0 + 110)] + (v2 << 2)) + 283984))
                        if (u32(load32(arg0 + 72)) < u32(load32(((players[load16u(arg0 + 110)] + (v2 << 2)) + 283984)))):
                            while True:  # $label10
                                if (u32(v2) <= u32(load32(arg0 + 76))):
                                    break
                                store8(arg0 + 127, 1)
                                v2 = load32(arg0 + 40)
                                if not load32(arg0 + 40):
                                    break
                                if not load8u(9142916):
                                    break
                                store32(arg1 + 4, v2)
                                store32(arg1, -16776961)
                                a_b()
                                break
                            v2 = load32(arg0 + 44)
                            if load32(arg0 + 44):
                                store32((load32(9215884) + (v2 << 4)), 0)
                            store8(arg0 + 125, 8)
                            v3 = 0
                            store32(arg0 + 44, 0)
                            break
                        v4 = (v4 + 281668)
                        store32((v4 + 281668), (load32(v4) + v2))
                        store32(arg0 + 72, (v5 - v2))
                        if not load32(arg0 + 92):
                            break
                        if load32(9140316):
                            if (load32(9140320) != load32(arg0 + 28)):
                                break
                        break
                    G.global0 = (arg1 + 16)
                    if not v3:
                        break
                    break
                if (load8u(arg0 + 125) == 10):
                    break
                if (load8u(arg0 + 123) == 63):
                    break
                store8(arg0 + 125, 0)
                return call_table(load32(((load8u(arg0 + 123) * 40) + 9671200) + 20))
                break
            arg1 = load32(((v2 * 40) + 9671200) + 36)
            if load32(((v2 * 40) + 9671200) + 36):
                if call_table(arg1):
                    break
            func29(arg0, 1)
            break
        return load32(arg0 + 28)
        break
    func29(arg0, 1)
    return load32(arg0 + 32)

# ----------------------------------------------------------
# $func86
# ----------------------------------------------------------
def func86(arg0):
    v1 = load8u(arg0 + 122)
    while True:  # $label3
        while True:  # $label1
            while True:  # $label0
                if not load16u(arg0 + 108):
                    break
                while True:  # $label2
                    # br_table (v1 + -64)
                    break
                    break
                if (v1 == 10):
                    break
                break
            v2 = ((v1 * 72) + 9263856)
            break
            break
        while True:  # $label5
            while True:  # $label4
                v2 = load32(arg0 + 20)
                if not load32(arg0 + 20):
                    break
                if (u32(load32(v2 + 8)) < u32(3)):
                    break
                if load32(load32(v2)):
                    break
                v2 = ((v1 * 72) + 9263856)
                if not load32(((v1 * 72) + 9263856) + 68):
                    break
                break
                break
            while True:  # $label9
                while True:  # $label6
                    while True:  # $label8
                        while True:  # $label7
                            v2 = load32(arg0 + 88)
                            # br_table (load32(arg0 + 88) & 65535)
                            break
                            break
                        break
                        break
                    v2 = ((v2 & 0xFFFFFFFF) >> 16)
                    if (((v2 & 0xFFFFFFFF) >> 16) == load32(38984)):
                        break
                    if (load32(38528) == v2):
                        break
                    break
                    break
                break
                break
            break
        v2 = ((v1 * 72) + 9263908)
        break
    v3 = -1.0
    while True:  # $label10
        if (load32(38472) == v1):
            break
        if (load32(38600) == v1):
            break
        break
    return func37(arg0, load32(v2), v3, 0)

# ----------------------------------------------------------
# $func87
# ----------------------------------------------------------
def func87(arg0, arg1):
    v4 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v19 = load32(PLAYERS)
    v17 = (1 if (load32(38504) == arg1) else 4)
    store8(arg0 + 129, (1 if (load32(38504) == arg1) else 4))
    while True:  # $label0
        arg1 = load32(((v19 + (arg1 << 2)) + 284636))
        if not load32(((v19 + (arg1 << 2)) + 284636)):
            break
        v20 = load32(arg1 + 8)
        if not load32(arg1 + 8):
            break
        v21 = load16u(arg0 + 110)
        v22 = (v19 + (load16u(arg0 + 110) * 286704))
        v9 = ((v19 + (load16u(arg0 + 110) * 286704)) + 283872)
        v10 = (v22 + 283876)
        v11 = load32(v22 + 283960)
        v14 = (((v19 + (v21 * 286704)) + (load32(((load32(v22 + 283960) << 2) + 9940)) << 2)) + 284636)
        v13 = load32(9215884)
        v15 = load32(ENTITIES)
        v8 = load32(arg1)
        v24 = -1.0
        while True:  # $label5
            while True:  # $label1
                arg1 = load32((v8 + (v16 << 2)))
                if not load32((v8 + (v16 << 2))):
                    break
                v18 = (v15 + (arg1 * 132))
                if (load8u((v15 + (arg1 * 132)) + 125) == 3):
                    break
                arg1 = (load32(v10) - load16u(v18 + 114))
                arg1 = (load32(v9) - load16u(v18 + 112))
                # TODO: i32.div_u
                # TODO: f64.promote_f32
                # TODO: f32.demote_f64
                v25 = ((load32(v18 + 68) - load32(v18 + 64)) + i32(100))
                if not (sqrt(i32((((load32(v10) - load16u(v18 + 114)) * arg1) + ((load32(v9) - load16u(v18 + 112)) * arg1)))) | (((load32(v18 + 68) - load32(v18 + 64)) + i32(100)) < v24)):
                    break
                v7 = 0
                while True:  # $label2
                    arg1 = load32(v14)
                    if not load32(v14):
                        break
                    v2 = load32(arg1 + 8)
                    if not load32(arg1 + 8):
                        break
                    v6 = load32(arg1)
                    arg1 = 0
                    while True:  # $label4
                        while True:  # $label3
                            v5 = load32((v6 + (arg1 << 2)))
                            if not load32((v6 + (arg1 << 2))):
                                break
                            v5 = (v15 + (v5 * 132))
                            if (load8u((v15 + (v5 * 132)) + 129) != v17):
                                break
                            v3 = load32(v18 + 28)
                            if (load32(v18 + 28) != load32(v5 + 32)):
                                v5 = load32(v5 + 44)
                                if (load32((v13 + (load32(v5 + 44) << 4)) + 4) != 1):
                                    break
                                if (load32((v13 + ((v5 << 4) | 12))) != v3):
                                    break
                            v7 = (v7 + 1)
                            break
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != v2):
                            continue
                        break
                    break
                arg1 = (u32(v7) < u32(20))
                v12 = (load32(v18 + 28) if (u32(v7) < u32(20)) else v12)
                v24 = (v25 if arg1 else v24)
                v23 = (v7 if arg1 else v23)
                break
            v16 = (v16 + 1)
            if ((v16 + 1) != v20):
                continue
            break
        if not v12:
            v2 = 0
            break
        v7 = 0
        v17 = load32(ENTITIES)
        v2 = load8u(entities[v12].sub_state)
        while True:  # $label15
            while True:  # $label8
                while True:  # $label6
                    v20 = load32(((v11 << 2) + 9687164))
                    v9 = load32((((v19 + (v21 * 286704)) + (load32(((v11 << 2) + 9687164)) << 2)) + 284636))
                    if not load32((((v19 + (v21 * 286704)) + (load32(((v11 << 2) + 9687164)) << 2)) + 284636)):
                        break
                    v10 = load32(v9 + 8)
                    if not load32(v9 + 8):
                        break
                    v6 = (v17 + (v12 * 132))
                    arg1 = 0
                    while True:  # $label9
                        while True:  # $label7
                            v11 = load32((load32(v9) + (arg1 << 2)))
                            if not load32((load32(v9) + (arg1 << 2))):
                                break
                            v14 = load32(ENTITIES)
                            v8 = entities[v11]
                            v3 = load8u(entities[v11].unit_class)
                            if (load8u(entities[v11].unit_class) == 3):
                                break
                            v5 = load32(v8 + 96)
                            if (load32(v8 + 96) == load32(v6 + 28)):
                                if v3:
                                    break
                                v7 = (v7 + 1)
                                break
                            if (load8u((v14 + (v5 * 132)) + 125) != 3):
                                break
                            v10 = load32(v9 + 8)
                            break
                        arg1 = (arg1 + 1)
                        if (u32((arg1 + 1)) < u32(v10)):
                            continue
                        break
                    break
                # TODO: i32.div_u
                if not (v7 & (u32(v23) <= u32(6))):
                    v2 = 1
                    break
                v2 = load32(((v2 * 404) + ENTITY_TYPES) + 216)
                v13 = ((v20 * 404) + ENTITY_TYPES)
                arg1 = load32(((v20 * 404) + ENTITY_TYPES) + 216)
                v15 = ((v19 + (v21 * 286704)) + 283908)
                while True:  # $label11
                    while True:  # $label10
                        v8 = (v17 + (v12 * 132))
                        v6 = load16u((v17 + (v12 * 132)) + 112)
                        v3 = load16u(v8 + 114)
                        v5 = (load16u(v8 + 114) + (load32(v13 + 220) ^ -1))
                        if not func73(load16u((v17 + (v12 * 132)) + 112), (load16u(v8 + 114) + (load32(v13 + 220) ^ -1)), v13, 0, 0, 1):
                            break
                        if not func108(v6, v5, load32(v15), 7):
                            break
                        arg1 = v6
                        break
                        break
                    while True:  # $label12
                        v2 = (v2 + 1)
                        v5 = ((v2 + 1) + v3)
                        if not func73(v6, ((v2 + 1) + v3), v13, 0, 0, 1):
                            break
                        if not func108(v6, v5, load32(v15), 7):
                            break
                        arg1 = v6
                        break
                        break
                    while True:  # $label13
                        arg1 = ((arg1 ^ -1) + v6)
                        if not func73(((arg1 ^ -1) + v6), v3, v13, 0, 0, 1):
                            break
                        if not func108(arg1, v3, load32(v15), 7):
                            break
                        v5 = v3
                        break
                        break
                    while True:  # $label14
                        arg1 = (v2 + v6)
                        if not func73((v2 + v6), v3, v13, 0, 0, 1):
                            break
                        if not func108(arg1, v3, load32(v15), 7):
                            break
                        v5 = v3
                        break
                        break
                    if v7:
                        break
                    v16 = load32(9142440)
                    v14 = 2147483647
                    v2 = 0
                    while True:  # $label17
                        while True:  # $label16
                            v8 = v2
                            v2 = (v2 << 2)
                            v9 = load32((((v2 << 2) | 4) + 8611904))
                            v10 = (load32((((v2 << 2) | 4) + 8611904)) + v3)
                            if (u32(v16) <= u32((load32((((v2 << 2) | 4) + 8611904)) + v3))):
                                break
                            v2 = load32((v2 + 8611904))
                            v11 = (load32((v2 + 8611904)) + v6)
                            if (u32(v16) <= u32((load32((v2 + 8611904)) + v6))):
                                break
                            if ((v10 | v11) < 0):
                                break
                            v2 = ((v9 * v9) + (v2 * v2))
                            if (((v9 * v9) + (v2 * v2)) >= v14):
                                break
                            v9 = func73(v11, v10, v13, 0, 0, 1)
                            v16 = load32(9142440)
                            if not v9:
                                break
                            if not func108(v11, v10, load32(v15), 7):
                                break
                            arg1 = v11
                            v5 = v10
                            v14 = v2
                            break
                        v2 = (v8 + 2)
                        if (u32(v8) < u32(1918)):
                            continue
                        break
                    v2 = 0
                    if (v14 == 2147483647):
                        break
                    break
                while True:  # $label19
                    while True:  # $label18
                        v6 = ((v20 * 404) + ENTITY_TYPES)
                        v3 = load32(((v20 * 404) + ENTITY_TYPES) + 68)
                        if load32(((v20 * 404) + ENTITY_TYPES) + 68):
                            if (load32(v4 + 16) < v3):
                                break
                        v3 = load32(v6 + 72)
                        if load32(v6 + 72):
                            if (load32(v4 + 20) < v3):
                                break
                        v3 = load32(v6 + 76)
                        if load32(v6 + 76):
                            if (load32(v4 + 24) < v3):
                                break
                        v3 = load32(v6 + 80)
                        if not load32(v6 + 80):
                            break
                        if (load32(v4 + 28) >= v3):
                            break
                        break
                    v2 = 0
                    break
                    break
                v3 = load32(arg0 + 28)
                store32(v4 + 24, v5)
                store32(v4 + 20, arg1)
                store32(v4 + 16, v20)
                arg0 = load16u(arg0 + 110)
                store64(v4 + 48, 4294967297)
                store64(v4 + 40, 4294967297)
                store64(v4 + 32, 4294967297)
                store32(v4 + 28, arg0)
                store32(v4 + 56, 0)
                store32(v4 + 12, v3)
                v2 = 1
                if load32(load32(GAME_STATE) + 156):
                    func29(entities[v3], 1)
                arg0 = (load32(9142440) + 2)
                arg0 = load32((load32(9142840) + ((arg1 + (((v5 + (load32(9142440) + 2)) + 1) * arg0)) << 2)) + 4)
                if (u32(load32((load32(9142840) + ((arg1 + (((v5 + (load32(9142440) + 2)) + 1) * arg0)) << 2)) + 4)) < u32(3)):
                    break
                store32(entities[arg0].garrison_id, v12)
                break
                break
            v2 = 1
            break
            break
        v2 = 1
        break
    G.global0 = (v4 - -64)
    return v2

# ----------------------------------------------------------
# $func88
# ----------------------------------------------------------
def func88(arg0):
    while True:  # $label0
        if load8u(9216060):
            if load8u(arg0 + 286696):
                break
            if not load32(arg0 + 284616):
                break
            if not load32(arg0 + 283976):
                break
            arg0 = (((load32(arg0 + 283848) + load32((arg0 + 281692))) - load32(arg0 + 283956)) + 100000)
            return ((((load32(arg0 + 283848) + load32((arg0 + 281692))) - load32(arg0 + 283956)) + 100000) if (arg0 > 0) else 0)
        # TODO: i32.div_u
        v5 = load32(PLAYER_COUNT)
        if load32(PLAYER_COUNT):
            v10 = load32((arg0 + 281784))
            v6 = (load32((arg0 + 281784)) * 255)
            v7 = (v5 * v10)
            arg0 = 0
            v8 = load32(PLAYERS)
            v9 = load32(9143004)
            while True:  # $label3
                if load8u((v9 + (arg0 + v7))):
                    v2 = ((v8 + (arg0 * 286704)) + 278564)
                    v1 = 0
                    while True:  # $label2
                        while True:  # $label1
                            v3 = ((v1 * 404) + ENTITY_TYPES)
                            if (load32(((v1 * 404) + ENTITY_TYPES) + 264) != 1):
                                break
                            if (load32(v3 + 268) == 1):
                                break
                            # TODO: i32.div_u
                            v11 = (100 + v11)
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v5):
                    continue
                break
            arg0 = 0
            v3 = 0
            while True:  # $label6
                if load8u((v9 + (arg0 + v7))):
                    v4 = ((v8 + (arg0 * 286704)) + 278564)
                    v1 = 0
                    while True:  # $label5
                        while True:  # $label4
                            v2 = ((v1 * 404) + ENTITY_TYPES)
                            if (load32(((v1 * 404) + ENTITY_TYPES) + 264) == 1):
                                if (load32(v2 + 268) != 1):
                                    break
                            # TODO: i32.div_u
                            v3 = (100 + v3)
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v5):
                    continue
                break
            v2 = 0
            arg0 = 0
            while True:  # $label10
                while True:  # $label7
                    if load8u((v9 + (v2 + v7))):
                        break
                    if (v2 == v10):
                        break
                    v12 = ((v8 + (v2 * 286704)) + 278564)
                    v1 = 0
                    while True:  # $label9
                        while True:  # $label8
                            v4 = ((v1 * 404) + ENTITY_TYPES)
                            if (load32(((v1 * 404) + ENTITY_TYPES) + 264) == 1):
                                if (load32(v4 + 268) != 1):
                                    break
                            # TODO: i32.div_u
                            arg0 = (100 + arg0)
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                    break
                v2 = (v2 + 1)
                if ((v2 + 1) != v5):
                    continue
                break
            v4 = (v3 - arg0)
            arg0 = 0
            v3 = 0
            while True:  # $label14
                while True:  # $label11
                    if load8u((v9 + (arg0 + v7))):
                        break
                    if (arg0 == v10):
                        break
                    v12 = ((v8 + (arg0 * 286704)) + 278564)
                    v1 = 0
                    while True:  # $label13
                        while True:  # $label12
                            v2 = ((v1 * 404) + ENTITY_TYPES)
                            if (load32(((v1 * 404) + ENTITY_TYPES) + 264) != 1):
                                break
                            if (load32(v2 + 268) == 1):
                                break
                            # TODO: i32.div_u
                            v3 = (100 + v3)
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v5):
                    continue
                break
        else:
        arg0 = ((((v11 - v3) // 850) + (v4 // 50)) + 0)
        v1 = (((((v11 - v3) // 850) + (v4 // 50)) + 0) if (arg0 > 0) else 0)
        break
    return v1

# ----------------------------------------------------------
# $func89
# ----------------------------------------------------------
def func89(arg0, arg1, arg2):
    while True:  # $label0
        v3 = (arg0 & 65535)
        v4 = ((arg0 & 0xFFFFFFFF) >> 16)
        if (arg2 == 1):
            arg0 = (v3 + load8u(arg1))
            arg0 = (((v3 + load8u(arg1)) - 65521) if (u32(arg0) > u32(65520)) else arg0)
            arg1 = ((((v3 + load8u(arg1)) - 65521) if (u32(arg0) > u32(65520)) else arg0) + v4)
            arg2 = (((((v3 + load8u(arg1)) - 65521) if (u32(arg0) > u32(65520)) else arg0) + v4) << 16)
            break
        if arg1:
            if (u32(arg2) >= u32(16)):
                while True:  # $label3
                    while True:  # $label6
                        while True:  # $label4
                            if (u32(arg2) > u32(5551)):
                                while True:  # $label2
                                    arg2 = (arg2 - 5552)
                                    v5 = 347
                                    arg0 = arg1
                                    while True:  # $label1
                                        v3 = (v3 + load8u(arg0))
                                        v3 = (v3 + load8u(arg0 + 1))
                                        v3 = (v3 + load8u(arg0 + 2))
                                        v3 = (v3 + load8u(arg0 + 3))
                                        v3 = (v3 + load8u(arg0 + 4))
                                        v3 = (v3 + load8u(arg0 + 5))
                                        v3 = (v3 + load8u(arg0 + 6))
                                        v3 = (v3 + load8u(arg0 + 7))
                                        v3 = (v3 + load8u(arg0 + 8))
                                        v3 = (v3 + load8u(arg0 + 9))
                                        v3 = (v3 + load8u(arg0 + 10))
                                        v3 = (v3 + load8u(arg0 + 11))
                                        v3 = (v3 + load8u(arg0 + 12))
                                        v3 = (v3 + load8u(arg0 + 13))
                                        v3 = (v3 + load8u(arg0 + 14))
                                        v3 = (v3 + load8u(arg0 + 15))
                                        v4 = (((((((((((((((((v3 + load8u(arg0)) + v4) + (v3 + load8u(arg0 + 1))) + (v3 + load8u(arg0 + 2))) + (v3 + load8u(arg0 + 3))) + (v3 + load8u(arg0 + 4))) + (v3 + load8u(arg0 + 5))) + (v3 + load8u(arg0 + 6))) + (v3 + load8u(arg0 + 7))) + (v3 + load8u(arg0 + 8))) + (v3 + load8u(arg0 + 9))) + (v3 + load8u(arg0 + 10))) + (v3 + load8u(arg0 + 11))) + (v3 + load8u(arg0 + 12))) + (v3 + load8u(arg0 + 13))) + (v3 + load8u(arg0 + 14))) + (v3 + load8u(arg0 + 15)))
                                        arg0 = (arg0 + 16)
                                        v5 = (v5 - 1)
                                        if (v5 - 1):
                                            continue
                                        break
                                    v4 = (v4 % 65521)
                                    v3 = (v3 % 65521)
                                    arg1 = (arg1 + 5552)
                                    if (u32(arg2) > u32(5551)):
                                        continue
                                    break
                                if not arg2:
                                    break
                                if (u32(arg2) < u32(16)):
                                    break
                            while True:  # $label5
                                arg0 = (v3 + load8u(arg1))
                                arg0 = (arg0 + load8u(arg1 + 1))
                                arg0 = (arg0 + load8u(arg1 + 2))
                                arg0 = (arg0 + load8u(arg1 + 3))
                                arg0 = (arg0 + load8u(arg1 + 4))
                                arg0 = (arg0 + load8u(arg1 + 5))
                                arg0 = (arg0 + load8u(arg1 + 6))
                                arg0 = (arg0 + load8u(arg1 + 7))
                                arg0 = (arg0 + load8u(arg1 + 8))
                                arg0 = (arg0 + load8u(arg1 + 9))
                                arg0 = (arg0 + load8u(arg1 + 10))
                                arg0 = (arg0 + load8u(arg1 + 11))
                                arg0 = (arg0 + load8u(arg1 + 12))
                                arg0 = (arg0 + load8u(arg1 + 13))
                                arg0 = (arg0 + load8u(arg1 + 14))
                                v3 = (arg0 + load8u(arg1 + 15))
                                v4 = (((((((((((((((((v3 + load8u(arg1)) + v4) + (arg0 + load8u(arg1 + 1))) + (arg0 + load8u(arg1 + 2))) + (arg0 + load8u(arg1 + 3))) + (arg0 + load8u(arg1 + 4))) + (arg0 + load8u(arg1 + 5))) + (arg0 + load8u(arg1 + 6))) + (arg0 + load8u(arg1 + 7))) + (arg0 + load8u(arg1 + 8))) + (arg0 + load8u(arg1 + 9))) + (arg0 + load8u(arg1 + 10))) + (arg0 + load8u(arg1 + 11))) + (arg0 + load8u(arg1 + 12))) + (arg0 + load8u(arg1 + 13))) + (arg0 + load8u(arg1 + 14))) + (arg0 + load8u(arg1 + 15)))
                                arg1 = (arg1 + 16)
                                arg2 = (arg2 - 16)
                                if (u32((arg2 - 16)) > u32(15)):
                                    continue
                                break
                            if not arg2:
                                break
                            break
                        v6 = (arg2 - 1)
                        v7 = (arg2 & 3)
                        if (arg2 & 3):
                            v5 = 0
                            arg0 = arg1
                            while True:  # $label7
                                arg2 = (arg2 - 1)
                                v3 = (v3 + load8u(arg0))
                                v4 = ((v3 + load8u(arg0)) + v4)
                                arg1 = (arg0 + 1)
                                arg0 = (arg0 + 1)
                                v5 = (v5 + 1)
                                if ((v5 + 1) != v7):
                                    continue
                                break
                        if (u32(v6) < u32(3)):
                            break
                        while True:  # $label8
                            arg0 = (v3 + load8u(arg1))
                            v5 = ((v3 + load8u(arg1)) + load8u(arg1 + 1))
                            v6 = (((v3 + load8u(arg1)) + load8u(arg1 + 1)) + load8u(arg1 + 2))
                            v3 = ((((v3 + load8u(arg1)) + load8u(arg1 + 1)) + load8u(arg1 + 2)) + load8u(arg1 + 3))
                            v4 = (((((v3 + load8u(arg1)) + load8u(arg1 + 1)) + load8u(arg1 + 2)) + load8u(arg1 + 3)) + (v6 + (v5 + (arg0 + v4))))
                            arg1 = (arg1 + 4)
                            arg2 = (arg2 - 4)
                            if (arg2 - 4):
                                continue
                            break
                        break
                    v4 = (v4 % 65521)
                    v3 = (v3 % 65521)
                    break
                break
            while True:  # $label9
                if not arg2:
                    break
                while True:  # $label10
                    v7 = (arg2 & 3)
                    if not (arg2 & 3):
                        arg0 = arg2
                        break
                    arg0 = arg2
                    v5 = arg1
                    while True:  # $label11
                        arg0 = (arg0 - 1)
                        v3 = (v3 + load8u(v5))
                        v4 = ((v3 + load8u(v5)) + v4)
                        arg1 = (v5 + 1)
                        v5 = (v5 + 1)
                        v6 = (v6 + 1)
                        if ((v6 + 1) != v7):
                            continue
                        break
                    break
                if (u32(arg2) < u32(4)):
                    break
                while True:  # $label12
                    arg2 = (v3 + load8u(arg1))
                    v5 = ((v3 + load8u(arg1)) + load8u(arg1 + 1))
                    v6 = (((v3 + load8u(arg1)) + load8u(arg1 + 1)) + load8u(arg1 + 2))
                    v3 = ((((v3 + load8u(arg1)) + load8u(arg1 + 1)) + load8u(arg1 + 2)) + load8u(arg1 + 3))
                    v4 = (((((v3 + load8u(arg1)) + load8u(arg1 + 1)) + load8u(arg1 + 2)) + load8u(arg1 + 3)) + (v6 + (v5 + (arg2 + v4))))
                    arg1 = (arg1 + 4)
                    arg0 = (arg0 - 4)
                    if (arg0 - 4):
                        continue
                    break
                break
        else:
        break
    return 1

# ----------------------------------------------------------
# $func90
# ----------------------------------------------------------
def func90(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    v9 = ((i32(arg4) * i32(arg7)) << 3)
    if (u32(((i32(arg4) * i32(arg7)) << 3)) <= u32(4294967295)):
        store32(arg0 + 72, arg6)
        store32(arg0 + 68, arg3)
        store64(arg0 + 60, 0)
        store32(arg0 + 56, arg5)
        store32(arg0 + 52, arg4)
        store32(arg0 + 48, arg2)
        store32(arg0 + 44, arg1)
        store32(arg0 + 76, arg8)
        store32(arg0 + 8, arg7)
        store32(arg0 + 4, (arg2 < arg5))
        store32(arg0, (arg1 < arg4))
        store32(arg0 + 80, (arg8 + ((arg4 * arg7) << 2)))
        # TODO: memory.fill
        arg3 = load32(arg0)
        arg6 = ((arg1 - 1) if load32(arg0) else arg4)
        store32(arg0 + 40, ((arg1 - 1) if load32(arg0) else arg4))
        arg1 = ((arg4 - 1) if arg3 else arg1)
        store32(arg0 + 36, ((arg4 - 1) if arg3 else arg1))
        if not arg3:
            # TODO: i64.div_u
            store32(4294967296 + 12, i32(arg6))
        arg3 = load32(arg0 + 4)
        arg6 = (load32(arg0 + 4) != 0)
        arg4 = (arg5 - (load32(arg0 + 4) != 0))
        store32(arg0 + 32, (arg5 - (load32(arg0 + 4) != 0)))
        arg2 = (arg2 - arg6)
        store32(arg0 + 28, (arg2 - arg6))
        while True:  # $label0
            if not arg3:
                store32(arg0 + 24, arg2)
                # TODO: i64.div_u
                v9 = (i32(arg2) * i32(arg1))
                store32(4294967296 + 20, ((i32(arg5) << 32) if (u32(v9) >= u32(4294967296)) else (i32(arg2) * i32(arg1))))
                break
            store32(arg0 + 24, arg4)
            arg4 = arg1
            break
        # TODO: i64.div_u
        store32(4294967296 + 16, i32(arg4))
        arg0 = load32(52304)
        if (load32(52304) != load32(52320)):
            store32(9687812, 381)
            store32(9687808, 382)
            store32(9687804, 383)
            store32(9687800, 384)
            store32(52320, arg0)
    else:
    return 0

# ----------------------------------------------------------
# $func91
# ----------------------------------------------------------
def func91(arg0, param1):
    while True:  # $label3
        while True:  # $label2
            while True:  # $label0
                if (load32(arg0 + 24) <= 0):
                    v2 = load32(arg0 + 56)
                    if (load32(arg0 + 56) <= load32((arg0 - -64))):
                        break
                    v1 = 9687808
                    while True:  # $label4
                        while True:  # $label1
                            if load32(arg0 + 4):
                                break
                            v1 = 9687812
                            if load32(arg0 + 20):
                                break
                            if (load32(arg0 + 48) != v2):
                                break
                            if (load32(arg0 + 36) != 1):
                                break
                            if (load32(arg0 + 44) != 1):
                                break
                            v1 = load32(arg0 + 52)
                            if (load32(arg0 + 52) > 2):
                                break
                            if ((v1 * load32(arg0 + 8)) <= 0):
                                break
                            v2 = load32(arg0 + 76)
                            v1 = 0
                            while True:  # $label5
                                v3 = (v1 << 2)
                                store8((load32(arg0 + 68) + v1), load32((v2 + (v1 << 2))))
                                v2 = load32(arg0 + 76)
                                store32((load32(arg0 + 76) + v3), 0)
                                v1 = (v1 + 1)
                                if ((v1 + 1) < (load32(arg0 + 52) * load32(arg0 + 8))):
                                    continue
                                break
                            break
                            break
                        break
                    store32(arg0 + 24, (load32(arg0 + 24) + load32(arg0 + 28)))
                    store32(arg0 + 68, (load32(arg0 + 68) + load32(arg0 + 72)))
                    arg0 = (arg0 - -64)
                    store32((arg0 - -64), (load32(arg0) + 1))
                return
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
# $func92
# ----------------------------------------------------------
def func92(arg0, arg1, arg2):
    v3 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    v4 = load32(arg0 + 40)
    if load32(arg0 + 40):
        # TODO: f64.promote_f32
        v5 = arg2
        # TODO: f64.promote_f32
        v6 = arg1
        while True:  # $label0
            if load8u(9142916):
                store32(v3 + 120, v4)
                store64(v3 + 112, 0)
                storef64(v3 + 104, v5)
                storef64(v3 + 96, v6)
                a_b()
                break
            store64((v3 - -64), 0)
            store32(v3 + 80, v4)
            # TODO: f64.promote_f32
            storef64(v3 + 72, i32((load32(9142848) * 25)))
            storef64(v3 + 48, v6)
            storef64(v3 + 56, v5)
            a_b()
            break
        while True:  # $label1
            if load8u(9142916):
                break
            v4 = load32(arg0 + 92)
            if not load32(arg0 + 92):
                break
            if load8u(9142906):
                break
            store64(v3 + 16, 0)
            store32(v3 + 32, v4)
            # TODO: f64.promote_f32
            storef64(v3 + 24, i32((load32(9142848) * 25)))
            storef64(v3, v6)
            storef64(v3 + 8, v5)
            a_b()
            break
        func288(arg0, arg1, arg2)
    G.global0 = (v3 + 128)

# ----------------------------------------------------------
# $func93
# ----------------------------------------------------------
def func93(arg0, arg1, arg2):
    v6 = (arg1 - 1)
    v7 = (arg0 - 1)
    v3 = load32(arg2 + 216)
    while True:  # $label1
        while True:  # $label0
            if not ((arg0 > 0) & (arg1 > 0)):
                v5 = load32(arg2 + 220)
                break
            v5 = load32(arg2 + 220)
            if (u32(v3) <= u32(v7)):
                break
            if (u32(v5) <= u32(v6)):
                break
            if load8u(arg2 + 377):
                break
            if load8u((load32(arg2 + 372) + ((v3 * v6) + v7))):
                break
            break
        v4 = ((arg1 > 0) & (arg0 >= 0))
        while True:  # $label9
            if load8u(arg2 + 377):
                while True:  # $label2
                    if not v4:
                        break
                    if (u32(arg0) >= u32(v3)):
                        break
                    v4 = 1
                    if (u32(v5) > u32(v6)):
                        break
                    break
                while True:  # $label3
                    if (arg0 <= 0):
                        break
                    if (arg1 < 2):
                        break
                    if (u32(v3) <= u32(v7)):
                        break
                    v4 = 1
                    if (u32((arg1 - 2)) < u32(v5)):
                        break
                    break
                while True:  # $label4
                    if (arg0 < 2):
                        break
                    v4 = 1
                    if (arg1 <= 0):
                        break
                    if (u32((arg0 - 2)) >= u32(v3)):
                        break
                    if (u32(v5) > u32(v6)):
                        break
                    break
                while True:  # $label5
                    if (arg0 <= 0):
                        break
                    if (arg1 < 0):
                        break
                    if (u32(v3) <= u32(v7)):
                        break
                    v4 = 1
                    if (u32(arg1) < u32(v5)):
                        break
                    break
                while True:  # $label6
                    if (arg0 < 0):
                        break
                    if (arg1 < 2):
                        break
                    if (u32(arg0) >= u32(v3)):
                        break
                    v4 = 1
                    if (u32((arg1 - 2)) < u32(v5)):
                        break
                    break
                while True:  # $label7
                    arg2 = (arg0 < 2)
                    if (arg0 < 2):
                        break
                    if (arg1 < 2):
                        break
                    if (u32((arg0 - 2)) >= u32(v3)):
                        break
                    v4 = 1
                    if (u32((arg1 - 2)) < u32(v5)):
                        break
                    break
                while True:  # $label8
                    if arg2:
                        break
                    if (arg1 < 0):
                        break
                    if (u32((arg0 - 2)) >= u32(v3)):
                        break
                    v4 = 1
                    if (u32(arg1) < u32(v5)):
                        break
                    break
                if ((arg0 | arg1) < 0):
                    break
                if (u32(arg0) >= u32(v3)):
                    break
                v4 = 1
                if (u32(arg1) >= u32(v5)):
                    break
                break
            arg2 = load32(arg2 + 372)
            while True:  # $label10
                if not v4:
                    break
                if (u32(arg0) >= u32(v3)):
                    break
                if (u32(v5) <= u32(v6)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v6) + arg0))):
                    break
                break
            v8 = (arg1 - 2)
            while True:  # $label11
                if (arg0 <= 0):
                    break
                if (arg1 < 2):
                    break
                if (u32(v3) <= u32(v7)):
                    break
                if (u32(v5) <= u32(v8)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v8) + v7))):
                    break
                break
            v9 = (arg0 - 2)
            while True:  # $label12
                if (arg0 < 2):
                    break
                if (arg1 <= 0):
                    break
                if (u32(v3) <= u32(v9)):
                    break
                if (u32(v5) <= u32(v6)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v6) + v9))):
                    break
                break
            while True:  # $label13
                if (arg0 <= 0):
                    break
                if (arg1 < 0):
                    break
                if (u32(v3) <= u32(v7)):
                    break
                if (u32(arg1) >= u32(v5)):
                    break
                v4 = 1
                if load8u((arg2 + ((arg1 * v3) + v7))):
                    break
                break
            while True:  # $label14
                if (arg0 < 0):
                    break
                if (arg1 < 2):
                    break
                if (u32(arg0) >= u32(v3)):
                    break
                if (u32(v5) <= u32(v8)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v8) + arg0))):
                    break
                break
            while True:  # $label15
                v6 = (arg0 < 2)
                if (arg0 < 2):
                    break
                if (arg1 < 2):
                    break
                if (u32(v3) <= u32(v9)):
                    break
                if (u32(v5) <= u32(v8)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v8) + v9))):
                    break
                break
            while True:  # $label16
                if v6:
                    break
                if (arg1 < 0):
                    break
                if (u32(v3) <= u32(v9)):
                    break
                if (u32(arg1) >= u32(v5)):
                    break
                v4 = 1
                if load8u((arg2 + ((arg1 * v3) + v9))):
                    break
                break
            if ((arg0 | arg1) < 0):
                break
            if (u32(arg0) >= u32(v3)):
                break
            if (u32(arg1) >= u32(v5)):
                break
            v4 = 1
            if load8u((arg2 + ((arg1 * v3) + arg0))):
                break
            break
        v4 = 0
        break
    return v4

# ----------------------------------------------------------
# $func94
# ----------------------------------------------------------
def func94(arg0, arg1, arg2):
    v12 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # $label0
        if not load32(arg0 + 283908):
            break
        while True:  # $label1
            if not arg1:
                break
            if arg2:
                break
            v3 = load32(arg0 + 284628)
            arg2 = load32(arg0 + 284616)
            store32(v12 + 68, arg0)
            store32(v12 + 64, 94)
            store32(v12 + 72, (arg2 if arg2 else v3))
            a_b()
            arg2 = 1
            store8(arg0 + 286699, 1)
            if load8u(9147125):
                store32(v12 + 48, load32(arg0 + 283908))
                a_b()
                arg2 = load8u(arg0 + 286699)
            v3 = load32(arg0 + 283908)
            v4 = load8u(arg0 + 286696)
            store32(v12 + 40, arg2)
            store32(v12 + 36, v4)
            store32(v12 + 32, v3)
            a_b()
            if load8u(9147125):
                break
            break
        arg2 = load32(arg0 + 283908)
        while True:  # $label2
            v3 = load8u(arg0 + 286696)
            if load8u(arg0 + 286696):
                break
            if load8u(9147152):
                break
            if load8u(9142905):
                break
            while True:  # $label3
                if (arg2 != load32(CURRENT_PLAYER)):
                    break
                a_b()
                if not load32(load32(GAME_STATE) + 160):
                    if load8u(9147210):
                        break
                func227()
                break
            v3 = load32(arg0 + 284628)
            arg2 = load32(arg0 + 284616)
            store32(v12 + 20, arg0)
            store32(v12 + 16, 118)
            store32(v12 + 24, (arg2 if arg2 else v3))
            a_b()
            if not load32(arg0 + 283956):
                # TODO: i32.div_u
                store32((load32(9142848) * 25) + 283956, 1000)
            if not arg1:
                store8(arg0 + 286696, 1)
            if load8u(9147127):
                arg1 = 0
                v3 = (G.global0 - 16)
                G.global0 = (G.global0 - 16)
                while True:  # $label4
                    v4 = load32(PLAYER_COUNT)
                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                        break
                    v6 = load32(9143004)
                    v5 = load32(arg0 + 283908)
                    v14 = load32(PLAYERS)
                    arg2 = 1
                    while True:  # $label6
                        while True:  # $label5
                            v16 = (v14 + (arg2 * 286704))
                            v9 = load32((v14 + (arg2 * 286704)) + 283908)
                            if load8u((v6 + ((load32((v14 + (arg2 * 286704)) + 283908) * v4) + v5))):
                                break
                            if load8u(v16 + 286696):
                                break
                            arg1 = (arg1 + (v5 != v9))
                            break
                        arg2 = (arg2 + 1)
                        if ((arg2 + 1) != v4):
                            continue
                        break
                    if not arg1:
                        break
                    store32(v3, (load32(arg0 + 283848) // arg1))
                    store32(v3 + 4, (load32((arg0 + 283852)) // arg1))
                    store32(v3 + 8, (load32((arg0 + 283856)) // arg1))
                    store32(v3 + 12, (load32((arg0 + 283860)) // arg1))
                    if (u32(v4) < u32(2)):
                        break
                    arg1 = load32(9143004)
                    v5 = load32(PLAYERS)
                    arg2 = 1
                    while True:  # $label8
                        while True:  # $label7
                            v6 = load32(arg0 + 283908)
                            v16 = (v5 + (arg2 * 286704))
                            v14 = load32((v5 + (arg2 * 286704)) + 283908)
                            if load8u((arg1 + (load32(arg0 + 283908) + (load32((v5 + (arg2 * 286704)) + 283908) * v4)))):
                                break
                            if load8u(v16 + 286696):
                                break
                            if (v6 == v14):
                                break
                            func322(v14, v6, v3)
                            v4 = load32(PLAYER_COUNT)
                            arg1 = load32(9143004)
                            v5 = load32(PLAYERS)
                            break
                        arg2 = (arg2 + 1)
                        if (u32((arg2 + 1)) < u32(v4)):
                            continue
                        break
                    break
                G.global0 = (v3 + 16)
            v16 = 0
            v14 = (G.global0 - 32)
            G.global0 = (G.global0 - 32)
            while True:  # $label9
                arg2 = load32(PLAYER_COUNT)
                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                    break
                v6 = load32(PLAYERS)
                v4 = 1
                while True:  # $label14
                    while True:  # $label10
                        if (u32(arg2) < u32(2)):
                            arg2 = 1
                            break
                        v3 = (v6 + (v4 * 286704))
                        v9 = (arg2 * v4)
                        v5 = 0
                        v7 = load32(9143004)
                        arg1 = 1
                        while True:  # $label13
                            while True:  # $label12
                                while True:  # $label11
                                    if (arg1 == v4):
                                        break
                                    v10 = load8u((v7 + (arg1 + v9)))
                                    v15 = (v6 + (arg1 * 286704))
                                    v18 = load8u((v6 + (arg1 * 286704)) + 286699)
                                    v5 = (((load8u((v7 + (arg1 + v9))) != 0) | v5) if load8u((v6 + (arg1 * 286704)) + 286699) else v5)
                                    if not v10:
                                        break
                                    if v18:
                                        break
                                    if not load8u(v15 + 286696):
                                        break
                                    v5 = 1
                                    arg1 = (arg1 + 1)
                                    if ((arg1 + 1) != arg2):
                                        continue
                                    break
                                    break
                                arg1 = (arg1 + 1)
                                if ((arg1 + 1) != arg2):
                                    continue
                                break
                            if not (v5 & 1):
                                break
                            break
                        store32(9561720, load32(v3 + 284608))
                        v16 = 1
                        if load8u(v3 + 286696):
                            break
                        if load8u(v3 + 286697):
                            break
                        store8((v3 + 286697), 1)
                        if (load32(v3 + 283908) == load32(CURRENT_PLAYER)):
                            a_b()
                        arg2 = load32(v3 + 284628)
                        arg1 = load32(v3 + 284616)
                        store32(v14 + 20, v3)
                        store32(v14 + 16, 119)
                        store32(v14 + 24, (arg1 if arg1 else arg2))
                        a_b()
                        func227()
                        arg2 = load32(PLAYER_COUNT)
                        v6 = load32(PLAYERS)
                        break
                    v4 = (v4 + 1)
                    if (u32((v4 + 1)) < u32(arg2)):
                        continue
                    break
                if not (v16 & not load8u(9142905)):
                    break
                store8(9142905, 1)
                arg1 = (load32(9142848) * 25)
                # TODO: i32.div_u
                store32(1, ((load32(9142848) * 25) if (u32(arg1) < u32(1000)) else 1000))
                if (u32(arg2) >= u32(2)):
                    v3 = load32(PLAYERS)
                    arg1 = 1
                    while True:  # $label15
                        v4 = (v3 + (arg1 * 286704))
                        if not load32((v3 + (arg1 * 286704)) + 283956):
                            store32((v4 + 283956), load32(9561724))
                            arg2 = load32(PLAYER_COUNT)
                        arg1 = (arg1 + 1)
                        if (u32((arg1 + 1)) < u32(arg2)):
                            continue
                        break
                if load8u(9147127):
                    func361()
                    arg2 = load32(PLAYER_COUNT)
                    v18 = ((load32(PLAYER_COUNT) * 54) - 54)
                    v19 = func26((-1 if (u32(v18) > u32(1073741823)) else (((load32(PLAYER_COUNT) * 54) - 54) << 2)))
                    while True:  # $label19
                        while True:  # $label18
                            if (u32(arg2) >= u32(2)):
                                v3 = load32(PLAYERS)
                                arg1 = 1
                                while True:  # $label17
                                    while True:  # $label16
                                        if (load32((v3 + (arg1 * 286704)) + 283944) == 1):
                                            v20 = load32((v3 + (arg1 * 286704)) + 283884)
                                            break
                                        arg1 = (arg1 + 1)
                                        if ((arg1 + 1) != arg2):
                                            continue
                                        break
                                    break
                                if (u32(arg2) > u32(1)):
                                    break
                            v7 = load32(9561720)
                            break
                            break
                        v16 = 1
                        while True:  # $label59
                            v5 = 0
                            arg1 = load32(PLAYERS)
                            v4 = players[v16]
                            if v20:
                                # TODO: i32.div_u
                            else:
                            store32(v20 + 283884, 0)
                            v3 = ((v16 * 216) + v19)
                            store32((((v16 * 216) + v19) - 216), load32(v4 + 283944))
                            store32((v3 - 212), load32(v4 + 283960))
                            store32((v3 - 208), load32(v4 + 284608))
                            store32((v3 - 204), load32(v4 + 283892))
                            v17 = (v4 + 283884)
                            while True:  # $label33
                                v6 = load32(PLAYER_COUNT)
                                if load32(PLAYER_COUNT):
                                    v10 = (v4 + 281784)
                                    arg1 = load32((v4 + 281784))
                                    v7 = (load32((v4 + 281784)) * 255)
                                    v13 = (arg1 * v6)
                                    v15 = load32(PLAYERS)
                                    v9 = load32(9143004)
                                    arg2 = 0
                                    while True:  # $label22
                                        while True:  # $label20
                                            if not load8u((v9 + (v5 + v13))):
                                                break
                                            v8 = ((v15 + (v5 * 286704)) + 278568)
                                            arg1 = 0
                                            while True:  # $label21
                                                if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) != 1):
                                                    arg2 = (load32((load32(v8) + ((arg1 + v7) << 2))) + arg2)
                                                v11 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v11 * 404) + ENTITY_TYPES) + 264) != 1):
                                                    arg2 = (load32((load32(v8) + ((v7 + v11) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise Unreachable()
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != v6):
                                            continue
                                        break
                                    store32((v3 - 200), arg2)
                                    v8 = load32((v4 + 278568))
                                    v5 = 0
                                    v11 = load32(38528)
                                    arg2 = 0
                                    while True:  # $label26
                                        v13 = (v5 * 255)
                                        arg1 = 0
                                        while True:  # $label25
                                            while True:  # $label23
                                                if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) == 1):
                                                    break
                                                if (arg1 == v11):
                                                    break
                                                arg2 = (load32((v8 + ((arg1 + v13) << 2))) + arg2)
                                                break
                                            v7 = (arg1 | 1)
                                            if ((arg1 | 1) != 255):
                                                while True:  # $label24
                                                    if (load32(((v7 * 404) + ENTITY_TYPES) + 264) == 1):
                                                        break
                                                    if (v7 == v11):
                                                        break
                                                    arg2 = (load32((v8 + ((v7 + v13) << 2))) + arg2)
                                                    break
                                                arg1 = (arg1 + 2)
                                                continue
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != v6):
                                            continue
                                        break
                                    store32((v3 - 196), arg2)
                                    arg1 = load32(v10)
                                    v7 = (load32(v10) * 255)
                                    v13 = (arg1 * v6)
                                    v5 = 0
                                    arg2 = 0
                                    while True:  # $label29
                                        while True:  # $label27
                                            if not load8u((v9 + (v5 + v13))):
                                                break
                                            v8 = ((v15 + (v5 * 286704)) + 278564)
                                            arg1 = 0
                                            while True:  # $label28
                                                if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) != 1):
                                                    arg2 = (load32((load32(v8) + ((arg1 + v7) << 2))) + arg2)
                                                v11 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v11 * 404) + ENTITY_TYPES) + 264) != 1):
                                                    arg2 = (load32((load32(v8) + ((v7 + v11) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise Unreachable()
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != v6):
                                            continue
                                        break
                                    store32((v3 - 192), arg2)
                                    v8 = (load32(v10) * v6)
                                    v7 = load32((v4 + 278564))
                                    v5 = 0
                                    arg2 = 0
                                    while True:  # $label32
                                        while True:  # $label30
                                            if not load8u((v9 + (v5 + v8))):
                                                break
                                            v10 = (v5 * 255)
                                            arg1 = 0
                                            while True:  # $label31
                                                if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) != 1):
                                                    arg2 = (load32((v7 + ((arg1 + v10) << 2))) + arg2)
                                                v15 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v15 * 404) + ENTITY_TYPES) + 264) != 1):
                                                    arg2 = (load32((v7 + ((v10 + v15) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise Unreachable()
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != v6):
                                            continue
                                        break
                                    break
                                arg2 = 0
                                store32((v3 - 192), 0)
                                store64((v3 - 200), 0)
                                break
                            v15 = (v4 + 284608)
                            store32((v3 - 188), arg2)
                            v8 = (v4 + 281676)
                            store32((v3 - 184), (load32((v4 + 281676)) + load32((v4 + 281640))))
                            v11 = (v4 + 281680)
                            store32((v3 - 180), (load32((v4 + 281680)) + load32((v4 + 281644))))
                            v13 = (v4 + 281684)
                            v21 = (v4 + 281656)
                            v22 = (v4 + 281660)
                            v23 = (v4 + 281652)
                            v24 = (v4 + 281648)
                            store32((v3 - 176), (load32((v4 + 281684)) + (load32((v4 + 281656)) + (load32((v4 + 281660)) + (load32((v4 + 281652)) + load32((v4 + 281648)))))))
                            v25 = (v4 + 281688)
                            store32((v3 - 172), (load32((v4 + 281688)) + load32((v4 + 281664))))
                            store32((v3 - 168), load32(v4 + 283872))
                            store32((v3 - 164), load32(v4 + 283876))
                            store32((v3 - 160), load32(v4 + 283948))
                            store32((v3 - 156), load32(v4 + 283956))
                            store32((v3 - 152), load32(v17))
                            while True:  # $label34
                                if not v6:
                                    arg2 = 0
                                    store32((v3 - 148), 0)
                                    break
                                arg1 = load32((v4 + 281784))
                                v9 = (load32((v4 + 281784)) * 255)
                                v17 = (arg1 * v6)
                                v5 = 0
                                v26 = load32(PLAYERS)
                                v27 = load32(9143004)
                                arg2 = 0
                                while True:  # $label37
                                    while True:  # $label35
                                        if not load8u((v27 + (v5 + v17))):
                                            break
                                        v7 = ((v26 + (v5 * 286704)) + 278568)
                                        arg1 = 0
                                        while True:  # $label36
                                            if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) == 1):
                                                arg2 = (load32((load32(v7) + ((arg1 + v9) << 2))) + arg2)
                                            v10 = (arg1 | 1)
                                            if ((arg1 | 1) == 255):
                                                break
                                            if (load32(((v10 * 404) + ENTITY_TYPES) + 264) == 1):
                                                arg2 = (load32((load32(v7) + ((v9 + v10) << 2))) + arg2)
                                            arg1 = (arg1 + 2)
                                            continue
                                            break
                                        raise Unreachable()
                                        break
                                    v5 = (v5 + 1)
                                    if ((v5 + 1) != v6):
                                        continue
                                    break
                                store32((v3 - 148), arg2)
                                v9 = load32((v4 + 278568))
                                v5 = 0
                                arg2 = 0
                                while True:  # $label39
                                    v7 = (v5 * 255)
                                    arg1 = 0
                                    while True:  # $label38
                                        if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) == 1):
                                            arg2 = (load32((v9 + ((arg1 + v7) << 2))) + arg2)
                                        v10 = (arg1 | 1)
                                        if ((arg1 | 1) != 255):
                                            if (load32(((v10 * 404) + ENTITY_TYPES) + 264) == 1):
                                                arg2 = (load32((v9 + ((v7 + v10) << 2))) + arg2)
                                            arg1 = (arg1 + 2)
                                            continue
                                        break
                                    v5 = (v5 + 1)
                                    if ((v5 + 1) != v6):
                                        continue
                                    break
                                break
                            store32((v3 - 144), arg2)
                            store32((v3 - 140), load32((v4 + 281740)))
                            store32((v3 - 136), load32((v4 + 281724)))
                            store32((v3 - 132), load32((v4 + 281728)))
                            store32((v3 - 128), load32((v4 + 281732)))
                            store32((v3 - 124), load32((v4 + 281736)))
                            store32((v3 - 120), load32((v4 + 281744)))
                            store32((v3 - 116), load32((v4 + 281668)))
                            store32((v3 - 112), load32((v4 + 281748)))
                            store32((v3 - 108), load32((v4 + 281636)))
                            v7 = load32(9561720)
                            while True:  # $label40
                                arg1 = load32(v15)
                                if load32(v15):
                                    if (arg1 == v7):
                                        break
                                break
                            store32((v3 - 104), (load8u(v4 + 286697) != 0))
                            store32((v3 - 100), ((load8u((v4 + 283974)) | (load8u((v4 + 283973)) << 8)) | (load8u(v4 + 283972) << 16)))
                            store32((v3 - 96), load32(v8))
                            store32((v3 - 92), load32(v11))
                            store32((v3 - 88), load32(v13))
                            store32((v3 - 84), load32(v25))
                            store32((v3 - 80), load32(v23))
                            store32((v3 - 76), load32(v24))
                            store32((v3 - 72), load32(v21))
                            store32((v3 - 68), load32(v22))
                            store32((v3 + -64), load32((v4 + 281708)))
                            store32((v3 - 60), load32((v4 + 281712)))
                            store32((v3 - 56), load32((v4 + 281716)))
                            store32((v3 - 52), load32((v4 + 281720)))
                            store32((v3 - 48), load32((v4 + 281692)))
                            store32((v3 - 44), load32((v4 + 281696)))
                            store32((v3 - 40), load32((v4 + 281700)))
                            store32((v3 - 36), load32((v4 + 281704)))
                            arg1 = 0
                            v9 = load32(38528)
                            arg2 = 0
                            while True:  # $label43
                                while True:  # $label41
                                    if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) & -5):
                                        break
                                    if (arg1 == v9):
                                        break
                                    arg2 = (load32(((v4 + (arg1 << 2)) + 278576)) + arg2)
                                    break
                                v5 = (arg1 | 1)
                                if ((arg1 | 1) != 255):
                                    while True:  # $label42
                                        if (load32(((v5 * 404) + ENTITY_TYPES) + 264) & -5):
                                            break
                                        if (v5 == v9):
                                            break
                                        arg2 = (load32(((v4 + (v5 << 2)) + 278576)) + arg2)
                                        break
                                    arg1 = (arg1 + 2)
                                    continue
                                break
                            store32((v3 - 32), arg2)
                            store32((v3 - 28), load32(v4 + 283888))
                            store32((v3 - 24), load32((v4 + 281672)))
                            while True:  # $label58
                                if v6:
                                    v10 = (v4 + 281784)
                                    arg1 = load32((v4 + 281784))
                                    v8 = (load32((v4 + 281784)) * 255)
                                    v17 = (arg1 * v6)
                                    v5 = 0
                                    v15 = load32(PLAYERS)
                                    v9 = load32(9143004)
                                    arg2 = 0
                                    while True:  # $label46
                                        while True:  # $label44
                                            if not load8u((v9 + (v5 + v17))):
                                                break
                                            v11 = ((v15 + (v5 * 286704)) + 278564)
                                            arg1 = 0
                                            while True:  # $label45
                                                if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) == 1):
                                                    arg2 = (load32((load32(v11) + ((arg1 + v8) << 2))) + arg2)
                                                v13 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v13 * 404) + ENTITY_TYPES) + 264) == 1):
                                                    arg2 = (load32((load32(v11) + ((v8 + v13) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise Unreachable()
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != v6):
                                            continue
                                        break
                                    store32((v3 - 20), arg2)
                                    v13 = (load32(v10) * v6)
                                    v4 = load32((v4 + 278564))
                                    v5 = 0
                                    arg2 = 0
                                    while True:  # $label49
                                        while True:  # $label47
                                            if not load8u((v9 + (v5 + v13))):
                                                break
                                            v8 = (v5 * 255)
                                            arg1 = 0
                                            while True:  # $label48
                                                if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) == 1):
                                                    arg2 = (load32((v4 + ((arg1 + v8) << 2))) + arg2)
                                                v11 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v11 * 404) + ENTITY_TYPES) + 264) == 1):
                                                    arg2 = (load32((v4 + ((v8 + v11) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise Unreachable()
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != v6):
                                            continue
                                        break
                                    v5 = 0
                                    store32((v3 - 12), 0)
                                    store32((v3 - 16), arg2)
                                    v4 = load32(v10)
                                    v11 = (load32(v10) * 255)
                                    v13 = (v4 * v6)
                                    arg2 = 0
                                    while True:  # $label53
                                        while True:  # $label50
                                            if load8u((v9 + (v5 + v13))):
                                                break
                                            if (v4 == v5):
                                                break
                                            v17 = ((v15 + (v5 * 286704)) + 278564)
                                            arg1 = 0
                                            while True:  # $label52
                                                while True:  # $label51
                                                    v8 = ((arg1 * 404) + ENTITY_TYPES)
                                                    if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) == 1):
                                                        if (load32(v8 + 268) != 1):
                                                            break
                                                    # TODO: i32.div_u
                                                    arg2 = (100 + arg2)
                                                    break
                                                arg1 = (arg1 + 1)
                                                if ((arg1 + 1) != 255):
                                                    continue
                                                break
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != v6):
                                            continue
                                        break
                                    store32((v3 - 8), arg2)
                                    v5 = load32(v10)
                                    v8 = (load32(v10) * 255)
                                    v11 = (v5 * v6)
                                    v4 = 0
                                    arg2 = 0
                                    while True:  # $label57
                                        while True:  # $label54
                                            if load8u((v9 + (v4 + v11))):
                                                break
                                            if (v4 == v5):
                                                break
                                            v13 = ((v15 + (v4 * 286704)) + 278564)
                                            arg1 = 0
                                            while True:  # $label56
                                                while True:  # $label55
                                                    v10 = ((arg1 * 404) + ENTITY_TYPES)
                                                    if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) != 1):
                                                        break
                                                    if (load32(v10 + 268) == 1):
                                                        break
                                                    # TODO: i32.div_u
                                                    arg2 = (100 + arg2)
                                                    break
                                                arg1 = (arg1 + 1)
                                                if ((arg1 + 1) != 255):
                                                    continue
                                                break
                                            break
                                        v4 = (v4 + 1)
                                        if ((v4 + 1) != v6):
                                            continue
                                        break
                                    break
                                store64((v3 - 12), 0)
                                store64((v3 - 20), 0)
                                arg2 = 0
                                break
                            store32((v3 - 4), arg2)
                            v16 = (v16 + 1)
                            if (u32((v16 + 1)) < u32(v6)):
                                continue
                            break
                        break
                    store32(v14 + 8, v7)
                    store32(v14 + 4, v18)
                    store32(v14, v19)
                break
            G.global0 = (v14 + 32)
            v3 = load8u(arg0 + 286696)
            arg2 = load32(arg0 + 283908)
            break
        store32(v12 + 8, load8u(arg0 + 286699))
        store32(v12 + 4, v3)
        store32(v12, arg2)
        a_b()
        break
    G.global0 = (v12 + 80)
    return v12

# ----------------------------------------------------------
# $func95
# ----------------------------------------------------------
def func95(arg0, arg1, arg2):
    while True:  # $label9
        while True:  # $label0
            v3 = load32(9142440)
            v4 = ((load32(9142440) * arg1) + arg0)
            v6 = (((load32(9142440) * arg1) + arg0) + load32(9147288))
            v7 = load8u((((load32(9142440) * arg1) + arg0) + load32(9147288)))
            v8 = i32(load8u((((load32(9142440) * arg1) + arg0) + load32(9147288))))
            if (i32(load8u((((load32(9142440) * arg1) + arg0) + load32(9147288)))) != arg2):
                break
            v5 = func373(arg0, arg1, arg2)
            if (func373(arg0, arg1, arg2) < 0):
                break
            if (arg2 <= v5):
                break
            if (func410(v4, v5) != 55):
                break
            while True:  # $label1
                if (v8 < 0):
                    break
                if (load32(load32((load32(9140332) + (v7 << 2))) + 32) != 23):
                    break
                v4 = load32(9142840)
                v7 = (arg0 + 1)
                v8 = (arg1 + 1)
                store32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (v3 + 2))) << 2)), 0)
                v3 = (load32(9142440) + 2)
                store32((v4 + (((((load32(9142440) + 2) + v8) * v3) + v7) << 2)), 0)
                break
            store8(v6, v5)
            v5 = (arg0 + 1)
            while True:  # $label2
                v3 = load32(9142440)
                if (u32(load32(9142440)) <= u32(arg1)):
                    break
                if (u32(v3) <= u32(v5)):
                    break
                if ((arg1 | v5) < 0):
                    break
                func95(v5, arg1, arg2)
                v3 = load32(9142440)
                break
            while True:  # $label3
                v6 = (arg1 - 1)
                if (u32(v3) <= u32((arg1 - 1))):
                    break
                if (u32(v3) <= u32(v5)):
                    break
                if ((v5 | v6) < 0):
                    break
                func95(v5, v6, arg2)
                v3 = load32(9142440)
                break
            while True:  # $label4
                if (u32(v3) <= u32(v6)):
                    break
                if (u32(arg0) >= u32(v3)):
                    break
                if ((arg0 | v6) < 0):
                    break
                func95(arg0, v6, arg2)
                v3 = load32(9142440)
                break
            v4 = (arg0 - 1)
            while True:  # $label5
                if (u32(v3) <= u32(v6)):
                    break
                if (u32(v3) <= u32(v4)):
                    break
                if ((v4 | v6) < 0):
                    break
                func95(v4, v6, arg2)
                v3 = load32(9142440)
                break
            while True:  # $label6
                if (u32(arg1) >= u32(v3)):
                    break
                if (u32(v3) <= u32(v4)):
                    break
                if ((arg1 | v4) < 0):
                    break
                func95(v4, arg1, arg2)
                v3 = load32(9142440)
                break
            while True:  # $label7
                arg1 = (arg1 + 1)
                if (u32(v3) <= u32((arg1 + 1))):
                    break
                if (u32(v3) <= u32(v4)):
                    break
                if ((arg1 | v4) < 0):
                    break
                func95(v4, arg1, arg2)
                v3 = load32(9142440)
                break
            while True:  # $label8
                if (u32(arg1) >= u32(v3)):
                    break
                if (u32(arg0) >= u32(v3)):
                    break
                if ((arg0 | arg1) < 0):
                    break
                func95(arg0, arg1, arg2)
                v3 = load32(9142440)
                break
            if (u32(arg1) >= u32(v3)):
                break
            if (u32(v3) <= u32(v5)):
                break
            arg0 = v5
            if ((v5 | arg1) >= 0):
                continue
            break
        break

# ----------------------------------------------------------
# $func96
# ----------------------------------------------------------
def func96(arg0, arg1, arg2, arg3):
    while True:  # $label17
        while True:  # $label0
            v6 = load32(9142440)
            v13 = (load32(9142440) * arg1)
            v23 = ((load32(9142440) * arg1) + arg0)
            v15 = (load32(9142436) + (((load32(9142440) * arg1) + arg0) << 1))
            if (load16u((load32(9142436) + (((load32(9142440) * arg1) + arg0) << 1))) == arg3):
                break
            v7 = (arg0 + 1)
            v16 = ((arg0 + 1) | arg1)
            v12 = load32(9147288)
            v4 = -1
            while True:  # $label1
                v8 = (u32(arg1) >= u32(v6))
                if (u32(arg1) >= u32(v6)):
                    break
                if (u32(v6) <= u32(v7)):
                    break
                if (v16 < 0):
                    break
                v4 = load8s((v12 + (v7 + v13)))
                v4 = (-1 if (v4 < 0) else (-1 if (arg2 == v4) else load8s((v12 + (v7 + v13)))))
                break
            v10 = (arg1 - 1)
            v17 = ((arg1 - 1) | v7)
            v11 = 0
            while True:  # $label2
                v14 = (u32(v6) <= u32(v10))
                if (u32(v6) <= u32(v10)):
                    break
                if (u32(v6) <= u32(v7)):
                    break
                if (v17 < 0):
                    break
                v5 = load8s((v12 + ((v6 * v10) + v7)))
                if (load8s((v12 + ((v6 * v10) + v7))) < 0):
                    break
                if (arg2 == v5):
                    break
                if (v4 == -1):
                    v4 = v5
                    break
                v11 = (v4 != v5)
                break
            v18 = (arg0 | v10)
            while True:  # $label3
                if v14:
                    break
                if (u32(arg0) >= u32(v6)):
                    break
                if (v18 < 0):
                    break
                v5 = load8s((v12 + ((v6 * v10) + arg0)))
                if (load8s((v12 + ((v6 * v10) + arg0))) < 0):
                    break
                if (arg2 == v5):
                    break
                if (v4 == -1):
                    v4 = v5
                    break
                v11 = (1 if (v4 != v5) else v11)
                break
            v9 = (arg0 - 1)
            v19 = (v10 | (arg0 - 1))
            while True:  # $label4
                if v14:
                    break
                if (u32(v6) <= u32(v9)):
                    break
                if (v19 < 0):
                    break
                v5 = load8s((v12 + ((v6 * v10) + v9)))
                if (load8s((v12 + ((v6 * v10) + v9))) < 0):
                    break
                if (arg2 == v5):
                    break
                if (v4 == -1):
                    v4 = v5
                    break
                v11 = (1 if (v4 != v5) else v11)
                break
            v20 = (arg1 | v9)
            while True:  # $label5
                if v8:
                    break
                if (u32(v6) <= u32(v9)):
                    break
                if (v20 < 0):
                    break
                v5 = load8s((v12 + (v9 + v13)))
                if (load8s((v12 + (v9 + v13))) < 0):
                    break
                if (arg2 == v5):
                    break
                if (v4 == -1):
                    v4 = v5
                    break
                v11 = (1 if (v4 != v5) else v11)
                break
            v8 = (arg1 + 1)
            v21 = ((arg1 + 1) | v9)
            while True:  # $label6
                v22 = (u32(v6) <= u32(v8))
                if (u32(v6) <= u32(v8)):
                    break
                if (u32(v6) <= u32(v9)):
                    break
                if (v21 < 0):
                    break
                v5 = load8s((v12 + ((v6 * v8) + v9)))
                if (load8s((v12 + ((v6 * v8) + v9))) < 0):
                    break
                if (arg2 == v5):
                    break
                if (v4 == -1):
                    v4 = v5
                    break
                v11 = (1 if (v4 != v5) else v11)
                break
            v13 = (arg0 | v8)
            while True:  # $label7
                if v22:
                    break
                if (u32(arg0) >= u32(v6)):
                    break
                if (v13 < 0):
                    break
                v5 = load8s((v12 + ((v6 * v8) + arg0)))
                if (load8s((v12 + ((v6 * v8) + arg0))) < 0):
                    break
                if (arg2 == v5):
                    break
                if (v4 == -1):
                    v4 = v5
                    break
                v11 = (1 if (v4 != v5) else v11)
                break
            v14 = (v7 | v8)
            while True:  # $label8
                if v22:
                    break
                if (u32(v6) <= u32(v7)):
                    break
                if (v14 < 0):
                    break
                v5 = load8s((v12 + ((v6 * v8) + v7)))
                if (load8s((v12 + ((v6 * v8) + v7))) < 0):
                    break
                if (arg2 == v5):
                    break
                if (v4 == -1):
                    break
                v11 = (1 if (v4 != v5) else v11)
                break
            if not v11:
                break
            if (load32(9147292) >= arg2):
                break
            store16(v15, arg3)
            while True:  # $label9
                v15 = (v12 + v23)
                v4 = load8s((v12 + v23))
                if (load8s((v12 + v23)) < 0):
                    break
                if (load32(load32((load32(9140332) + ((v4 & 255) << 2))) + 32) != 23):
                    break
                v5 = load32(9142840)
                store32((load32(9142840) + ((((v6 + 2) * v8) + v7) << 2)), 0)
                v4 = (load32(9142440) + 2)
                store32((v5 + (((((load32(9142440) + 2) + v8) * v4) + v7) << 2)), 0)
                break
            store8(v15, load32(9147292))
            while True:  # $label10
                v4 = load32(9142440)
                if (u32(load32(9142440)) <= u32(v7)):
                    break
                if (u32(arg1) >= u32(v4)):
                    break
                if (v16 < 0):
                    break
                if (load8s((load32(9147288) + ((arg1 * v4) + v7))) != arg2):
                    break
                func96(v7, arg1, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # $label11
                if (u32(v4) <= u32(v7)):
                    break
                if (u32(v4) <= u32(v10)):
                    break
                if (v17 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v10) + v7))) != arg2):
                    break
                func96(v7, v10, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # $label12
                if (u32(arg0) >= u32(v4)):
                    break
                if (u32(v4) <= u32(v10)):
                    break
                if (v18 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v10) + arg0))) != arg2):
                    break
                func96(arg0, v10, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # $label13
                if (u32(v4) <= u32(v9)):
                    break
                if (u32(v4) <= u32(v10)):
                    break
                if (v19 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v10) + v9))) != arg2):
                    break
                func96(v9, v10, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # $label14
                if (u32(v4) <= u32(v9)):
                    break
                if (u32(arg1) >= u32(v4)):
                    break
                if (v20 < 0):
                    break
                if (load8s((load32(9147288) + ((arg1 * v4) + v9))) != arg2):
                    break
                func96(v9, arg1, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # $label15
                if (u32(v4) <= u32(v9)):
                    break
                if (u32(v4) <= u32(v8)):
                    break
                if (v21 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v8) + v9))) != arg2):
                    break
                func96(v9, v8, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # $label16
                if (u32(arg0) >= u32(v4)):
                    break
                if (u32(v4) <= u32(v8)):
                    break
                if (v13 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v8) + arg0))) != arg2):
                    break
                func96(arg0, v8, arg2, arg3)
                v4 = load32(9142440)
                break
            if (u32(v4) <= u32(v7)):
                break
            if (u32(v4) <= u32(v8)):
                break
            if (v14 < 0):
                break
            arg0 = v7
            arg1 = v8
            if (load8s((load32(9147288) + (v7 + (v8 * v4)))) == arg2):
                continue
            break
        break

# ----------------------------------------------------------
# $func97
# ----------------------------------------------------------
def func97(arg0):
    func111(arg0, 1)

# ----------------------------------------------------------
# $func98
# ----------------------------------------------------------
def func98(arg0, arg1, arg2):
    if (u32(arg2) >= u32(512)):
        # TODO: memory.fill
        return
    while True:  # $label0
        if not arg2:
            break
        store8(arg0, arg1)
        v3 = (arg0 + arg2)
        store8(((arg0 + arg2) - 1), arg1)
        if (u32(arg2) < u32(3)):
            break
        store8(arg0 + 2, arg1)
        store8(arg0 + 1, arg1)
        store8((v3 - 3), arg1)
        store8((v3 - 2), arg1)
        if (u32(arg2) < u32(7)):
            break
        store8(arg0 + 3, arg1)
        store8((v3 - 4), arg1)
        if (u32(arg2) < u32(9)):
            break
        v4 = ((0 - arg0) & 3)
        v3 = (arg0 + ((0 - arg0) & 3))
        arg0 = ((arg1 & 255) * 16843009)
        store32((arg0 + ((0 - arg0) & 3)), ((arg1 & 255) * 16843009))
        arg2 = ((arg2 - v4) & -4)
        arg1 = (v3 + ((arg2 - v4) & -4))
        store32(((v3 + ((arg2 - v4) & -4)) - 4), arg0)
        if (u32(arg2) < u32(9)):
            break
        store32(v3 + 8, arg0)
        store32(v3 + 4, arg0)
        store32((arg1 - 8), arg0)
        store32((arg1 - 12), arg0)
        if (u32(arg2) < u32(25)):
            break
        store32(v3 + 24, arg0)
        store32(v3 + 20, arg0)
        store32(v3 + 16, arg0)
        store32(v3 + 12, arg0)
        store32((arg1 - 16), arg0)
        store32((arg1 - 20), arg0)
        store32((arg1 - 24), arg0)
        store32((arg1 - 28), arg0)
        arg2 = ((v3 & 4) | 24)
        arg1 = (arg2 - ((v3 & 4) | 24))
        if (u32((arg2 - ((v3 & 4) | 24))) < u32(32)):
            break
        v5 = (i32(arg0) * 4294967297)
        arg0 = (arg2 + v3)
        while True:  # $label1
            store64(arg0 + 24, v5)
            store64(arg0 + 16, v5)
            store64(arg0 + 8, v5)
            store64(arg0, v5)
            arg0 = (arg0 + 32)
            arg1 = (arg1 - 32)
            if (u32((arg1 - 32)) > u32(31)):
                continue
            break
        break

# ----------------------------------------------------------
# $func99
# ----------------------------------------------------------
def func99(arg0, arg1, arg2):
    while True:  # $label0
        if (arg1 == 5):
            if not load32(arg0 + 48):
                break
        if not load32(arg0):
            store32(arg0 + 8, arg2)
            store32(arg0, arg1)
            store32(arg0 + 4, 0)
        return 0
        break
    a_c()
    raise Unreachable()
    return 3476

# ----------------------------------------------------------
# $func100
# ----------------------------------------------------------
def func100(arg0, arg1, arg2):
    v6 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    while True:  # $label0
        if load8u(9142906):
            arg0 = load32(arg0 + 40)
            if not load32(arg0 + 40):
                break
            if load8u(9142916):
                store32(v6 + 84, arg0)
                store32(v6 + 80, -65281)
                a_b()
                break
            store32(v6 + 68, arg0)
            store32(v6 + 64, 13)
            a_b()
            break
        if load8u(9142916):
            arg1 = load32(arg0 + 40)
            if not load32(arg0 + 40):
                break
            arg0 = load8u(arg0 + 125)
            store32(v6 + 52, arg1)
            store32(v6 + 48, ((arg0 << 8) | 1))
            a_b()
            break
        v4 = load16u(arg0 + 114)
        v9 = load16u(arg0 + 112)
        v10 = load8u(arg0 + 122)
        while True:  # $label2
            while True:  # $label1
                v3 = load32(arg0 + 44)
                if not load32(arg0 + 44):
                    break
                v5 = load32(9215884)
                if (load32((load32(9215884) + (v3 << 4)) + 12) == 1):
                    break
                if (load8u(arg0 + 125) == 7):
                    break
                v3 = (v3 << 4)
                if load32((v5 + ((v3 << 4) | 4))):
                    break
                v7 = load32(((v10 * 404) + ENTITY_TYPES) + 260)
                v3 = (1 if (u32(v7) <= u32(1)) else load32(((v10 * 404) + ENTITY_TYPES) + 260))
                v5 = (((load32((v3 + v5)) - load32(9142848)) * -25) + (32000 // (1 if (u32(v7) <= u32(1)) else load32(((v10 * 404) + ENTITY_TYPES) + 260))))
                v8 = (load8u(arg0 + 124) << 3)
                v11 = load32(((load8u(arg0 + 124) << 3) + 8996))
                v12 = (load32(((load8u(arg0 + 124) << 3) + 8996)) * v3)
                v7 = (((((load32((v3 + v5)) - load32(9142848)) * -25) + (32000 // (1 if (u32(v7) <= u32(1)) else load32(((v10 * 404) + ENTITY_TYPES) + 260)))) * (load32(((load8u(arg0 + 124) << 3) + 8996)) * v3)) // 1000)
                v8 = load32((v8 + 8992))
                v13 = (load32((v8 + 8992)) * v3)
                v3 = ((v5 * (load32((v8 + 8992)) * v3)) // 1000)
                v14 = i32(v12)
                v4 = (v4 - v11)
                v9 = (v9 - v8)
                break
                break
            v3 = 0
            break
        v15 = 0.0
        v5 = ((v10 * 404) + ENTITY_TYPES)
        v8 = load32(((v10 * 404) + ENTITY_TYPES) + 216)
        while True:  # $label3
            if (load32(v5 + 264) != 1):
                break
            if (u32(v8) < u32(2)):
                break
            while True:  # $label4
                v5 = ((v10 * 404) + ENTITY_TYPES)
                v11 = load32(((v10 * 404) + ENTITY_TYPES) + 392)
                if load32(((v10 * 404) + ENTITY_TYPES) + 392):
                    v3 = (v3 - load32(v5 + 384))
                    v8 = load32(v5 + 396)
                    break
                v3 = (v3 - 5)
                v11 = ((v8 << 5) | 10)
                v8 = ((load32(v5 + 220) << 5) | 10)
                break
            v7 = (v7 - 5)
            func120(arg0, arg1, 1)
            v5 = 0
            v16 = i32((v3 + (v9 << 5)))
            v17 = i32((v7 + (v4 << 5)))
            v19 = i32(v4)
            v20 = (i32(v4) * 32.0)
            v7 = ((v10 * 404) + ENTITY_TYPES)
            v18 = i32(v11)
            v4 = 0
            while True:  # $label5
                if load8u(9142917):
                    break
                arg1 = load32(9299880)
                if load32(9299880):
                    arg1 = (arg1 - 1)
                    store32(9299880, (arg1 - 1))
                    v4 = load32((load32(9299872) + (arg1 << 2)))
                    break
                v4 = load32(9163776)
                arg1 = (load32(9163776) + 1)
                store32(9163776, (load32(9163776) + 1))
                v3 = load32(9163784)
                if (u32(arg1) < u32(load32(9163784))):
                    break
                store32(v6 + 32, v3)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            v21 = i32(v8)
            func120(arg0, v4, 1)
            v18 = (v18 + v16)
            while True:  # $label6
                if load8u(9142917):
                    break
                arg1 = load32(9299880)
                if load32(9299880):
                    arg1 = (arg1 - 1)
                    store32(9299880, (arg1 - 1))
                    v5 = load32((load32(9299872) + (arg1 << 2)))
                    break
                v5 = load32(9163776)
                arg1 = (load32(9163776) + 1)
                store32(9163776, (load32(9163776) + 1))
                v4 = load32(9163784)
                if (u32(arg1) < u32(load32(9163784))):
                    break
                store32(v6 + 16, v4)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            func120(arg0, v5, 1)
            v16 = (v21 + v17)
            v17 = (v19 * 32.0)
            v4 = 0
            while True:  # $label7
                if load8u(9142917):
                    break
                arg1 = load32(9299880)
                if load32(9299880):
                    arg1 = (arg1 - 1)
                    store32(9299880, (arg1 - 1))
                    v4 = load32((load32(9299872) + (arg1 << 2)))
                    break
                v4 = load32(9163776)
                arg1 = (load32(9163776) + 1)
                store32(9163776, (load32(9163776) + 1))
                v3 = load32(9163784)
                if (u32(arg1) < u32(load32(9163784))):
                    break
                store32(v6, v3)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            func120(arg0, v4, 1)
            break
            break
        break
    G.global0 = (v6 + 96)
    return func40(i32((v3 + (v9 << 5))), i32((v7 + (v4 << 5))), (((i32(v4) * 32.0) + ((i32(load32(9142440)) * 32.0) * i32(load32(v5 + 208)))) + -1.0), v15, v14, 0.0, 0.0, 0.0, -1.0, load32((9142744 if (u32(v8) > u32(1)) else 9142448)), arg2, arg1, 0, 0, 0, 0.0)

# ----------------------------------------------------------
# $func101
# ----------------------------------------------------------
def func101(arg0):
    v3 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # $label0
        if not load32(arg0 + 40):
            break
        v10 = load32(38560)
        v11 = load16u(arg0 + 114)
        v6 = load16u(arg0 + 112)
        v9 = load8u(arg0 + 122)
        v12 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
        while True:  # $label1
            v1 = load32(arg0 + 12)
            if not load32(arg0 + 12):
                break
            v7 = load32(v1 + 8)
            if not load32(v1 + 8):
                break
            while True:  # $label3
                v4 = (load32(v1) + (v2 << 2))
                if not load32((load32(v1) + (v2 << 2)) + 4):
                    func38(load32(v4))
                    v1 = load32(arg0 + 12)
                    v7 = (load32(v1 + 8) - 2)
                    store32(load32(arg0 + 12) + 8, (load32(v1 + 8) - 2))
                    if (u32(v2) < u32(v7)):
                        v8 = load32(v1)
                        v4 = v2
                        while True:  # $label2
                            v5 = (v8 + (v4 << 2))
                            store32((v8 + (v4 << 2)), load32(v5 + 8))
                            v4 = (v4 + 1)
                            v7 = load32(v1 + 8)
                            if (u32((v4 + 1)) < u32(load32(v1 + 8))):
                                continue
                            break
                    v2 = (v2 - 2)
                v2 = (v2 + 2)
                if (u32((v2 + 2)) < u32(v7)):
                    continue
                break
            break
        if not load32(v12 + 20):
            break
        v16 = (i32(v11) * 32.0)
        v17 = (((i32(v11) * 32.0) + 192.0) if (v9 == v10) else v16)
        v18 = ((((i32(v11) * 32.0) + 192.0) if (v9 == v10) else v16) + -1.0)
        v14 = ((v9 * 404) + 9568304)
        # TODO: f64.promote_f32
        v20 = v16
        v19 = (i32(v6) * 32.0)
        # TODO: f64.promote_f32
        v21 = (i32(v6) * 32.0)
        v11 = (v3 - -64)
        v7 = 0
        while True:  # $label8
            while True:  # $label5
                while True:  # $label4
                    v1 = load32((v12 + (v7 << 2)))
                    if (load32(load32((v12 + (v7 << 2))) + 32) == 6):
                        v2 = 7
                        if load8u(40588):
                            break
                        break
                    v4 = load8u(arg0 + 127)
                    v2 = (load8u(arg0 + 127) if v4 else (load16u(arg0 + 110) + 16))
                    break
                v15 = ((((i32(load32(9142440)) * 32.0) * i32(load32(v14))) + v17) + 1.0)
                v9 = func244(v1)
                func120(arg0, func244(v1), 0)
                v13 = load32(v1 + 32)
                if load8u(9142916):
                    if (v13 == 6):
                        v15 = (((i32(load32(9142440)) * 32.0) * i32(load32(v14))) + v17)
                    if load32(v1 + 20):
                        v6 = load8u(arg0 + 124)
                        v2 = load32(v1 + 28)
                        if (load32(v1 + 28) == 2147483647):
                            v2 = load32(59152)
                            store32(59152, (load32(59152) + 1))
                            v8 = load32(9568052)
                            store32(v1 + 28, v2)
                            v5 = load32(v1)
                            v10 = load32(v1 + 4)
                            v4 = load32(9568048)
                            store32(9568048, (load32(9568048) + 1))
                            store32(((v4 << 2) + 9563952), v1)
                            store32(9568052, (v8 + ((v5 * (v10 + 2)) << 2)))
                            v4 = load32(9568056)
                            store32(v1 + 56, load32(9568056))
                            store32(9568056, (v4 + ((v10 * load32(v1)) << 2)))
                    else:
                    v2 = 0
                    v15 = (v15 + 1.0)
                    v4 = load16u(arg0 + 110)
                    v1 = 1
                    while True:  # $label6
                        v5 = load8u(arg0 + 122)
                        if (load8u(arg0 + 122) == load32(38604)):
                            break
                        if (load32(38608) == v5):
                            break
                        if (load32(38612) == v5):
                            break
                        if (load32(38616) == v5):
                            break
                        if (load32(38624) == v5):
                            break
                        if (load32(38628) == v5):
                            break
                        if (load32(38632) == v5):
                            break
                        v1 = (load32(39056) == v5)
                        break
                    if (v15 > 0.0):
                        v15 = (((v15 * 0.5) / i32((load32(9142440) * 96))) + 0.25)
                    store32(v3 + 76, v9)
                    store32(v3 + 72, 0)
                    store32(v11, (2130706431 if (v13 == 6) else 0))
                    store64(v3 + 56, 0)
                    store32(v3 + 52, (0 - v1))
                    store32(v3 + 48, v2)
                    store64(v3 + 40, 0)
                    store64(v3 + 32, 0)
                    store64(v3 + 24, 0)
                    # TODO: f64.promote_f32
                    storef64(v3 + 16, v15)
                    store32(v3 + 68, ((v4 << 16) | 65535))
                    storef64(v3 + 8, v20)
                    storef64(v3, v21)
                    a_b()
                    break
                v5 = (v13 == 22)
                v4 = load8u(arg0 + 124)
                v8 = 1
                while True:  # $label7
                    v6 = load8u(arg0 + 122)
                    if (load8u(arg0 + 122) == load32(38604)):
                        break
                    if (load32(38608) == v6):
                        break
                    if (load32(38612) == v6):
                        break
                    if (load32(38616) == v6):
                        break
                    if (load32(38624) == v6):
                        break
                    if (load32(38628) == v6):
                        break
                    if (load32(38632) == v6):
                        break
                    v8 = (load32(39056) == v6)
                    break
                break
            v7 = (v7 + 1)
            if (u32((v7 + 1)) < u32(load32(v12 + 20))):
                continue
            break
        break
    G.global0 = (v3 + 80)
    return func40(v19, v16, v15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, v1, v2, v9, v5, v4, v8, 0.0)

# ----------------------------------------------------------
# $func102
# ----------------------------------------------------------
def func102(arg0, arg1, arg2):
    v3 = (G.global0 - 192)
    G.global0 = (G.global0 - 192)
    while True:  # $label0
        if load8u(9142917):
            break
        v7 = load8u(arg0 + 122)
        v5 = load8u(arg0 + 122)
        v6 = load32(arg0 + 40)
        if not load32(arg0 + 40):
            while True:  # $label1
                v4 = load32(9299880)
                if load32(9299880):
                    v4 = (v4 - 1)
                    store32(9299880, (v4 - 1))
                    v6 = load32((load32(9299872) + (v4 << 2)))
                    break
                v6 = load32(9163776)
                v4 = (load32(9163776) + 1)
                store32(9163776, (load32(9163776) + 1))
                v5 = load32(9163784)
                if (u32(v4) < u32(load32(9163784))):
                    break
                store32(v3 + 176, v5)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            v5 = load8u(arg0 + 122)
            store32(arg0 + 40, v6)
        if not (arg1 | load32(((v5 * 72) + 9263856))):
            arg0 = ((v5 << 2) + 9560016)
            if load32(((v5 << 2) + 9560016)):
                break
            store32(arg0, load32(9671136))
            break
        while True:  # $label3
            if load8u(9142916):
                store32(arg0 + 48, arg1)
                v4 = load8u(arg0 + 127)
                if (u32(((load8u(arg0 + 127) - 1) & 255)) <= u32(13)):
                    v4 = (v4 << 4)
                    v8 = ((((load32(((v4 << 4) + 1748)) << 8) + load32((v4 + 1744))) + (load32((v4 + 1752)) << 16)) + (load32((v4 + 1756)) << 24))
                v4 = load16u(arg0 + 114)
                v10 = (load16u(arg0 + 114) << 5)
                v11 = (load16u(arg0 + 112) << 5)
                v14 = load32(9142440)
                v17 = i32(((((load32(9142440) * load32(((v5 * 404) + ENTITY_TYPES) + 208)) + v4) << 5) | 1))
                while True:  # $label2
                    if not arg1:
                        break
                    if not load32(arg1 + 20):
                        break
                    v12 = load8u(arg0 + 124)
                    v4 = load32(arg1 + 28)
                    if (load32(arg1 + 28) == 2147483647):
                        v4 = load32(59152)
                        store32(59152, (load32(59152) + 1))
                        v13 = load32(9568052)
                        store32(arg1 + 28, v4)
                        v15 = load32(arg1)
                        v9 = load32(arg1 + 4)
                        v16 = load32(9568048)
                        store32(9568048, (load32(9568048) + 1))
                        store32(((v16 << 2) + 9563952), arg1)
                        store32(9568052, (v13 + ((v15 * (v9 + 2)) << 2)))
                        v13 = load32(9568056)
                        store32(arg1 + 56, load32(9568056))
                        store32(9568056, (v13 + ((v9 * load32(arg1)) << 2)))
                    break
                v4 = (v4 + (v12 << 16))
                v9 = load16u(arg0 + 110)
                v12 = load8u(arg0 + 125)
                store32(v3 + 172, v6)
                store32(v3 + 160, v8)
                store64(v3 + 152, 0)
                store32(v3 + 148, 0)
                store32(v3 + 144, v4)
                store64(v3 + 136, 0)
                store64(v3 + 128, 0)
                store64(v3 + 120, 0)
                store32(v3 + 168, (v12 << 8))
                store32(v3 + 164, ((v9 << 16) | v5))
                # TODO: f64.promote_f32
                storef64(v3 + 112, (((v17 * 0.5) / i32((v14 * 96))) + 0.25))
                storef64(v3 + 104, i32(v10))
                storef64(v3 + 96, i32(v11))
                a_b()
                break
            if arg1:
            func92(arg0, 0.0, 0.0)
            break
        if arg2:
            break
        if not load32(((v7 * 404) + ENTITY_TYPES) + 20):
            break
        while True:  # $label4
            if (arg1 == load32(9142592)):
                v4 = 4
                break
            if (arg1 == load32(9142596)):
                v4 = 14
                break
            if (arg1 == load32(9142600)):
                v4 = 16
                break
            if (arg1 == load32(9142604)):
                v4 = 9
                break
            if (arg1 == load32(9142636)):
                v4 = 35
                break
            if (load32(9142500) != arg1):
                break
            v4 = 15
            break
        arg2 = 37
        arg1 = 0
        while True:  # $label5
            if load8u(9142917):
                break
            arg1 = load32(9299880)
            if load32(9299880):
                arg1 = (arg1 - 1)
                store32(9299880, (arg1 - 1))
                arg1 = load32((load32(9299872) + (arg1 << 2)))
                break
            arg1 = load32(9163776)
            v6 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v5 = load32(9163784)
            if (u32(v6) < u32(load32(9163784))):
                break
            store32(v3 + 80, v5)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        func120(arg0, arg1, 0)
        v9 = load32(9142440)
        v6 = (load16u(arg0 + 114) << 5)
        v17 = (((i32(load32(9142440)) * 32.0) * i32(load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 208))) + i32((load16u(arg0 + 114) << 5)))
        v4 = (v4 + v6)
        v5 = ((load16u(arg0 + 112) << 5) + arg2)
        if load8u(9142916):
            v17 = (v17 + 30.0)
            v6 = 0
            while True:  # $label6
                arg2 = load32(9142740)
                if not load32(9142740):
                    break
                if not load32(arg2 + 20):
                    break
                v6 = load32(arg2 + 28)
                if (load32(arg2 + 28) != 2147483647):
                    break
                v6 = load32(59152)
                store32(59152, (load32(59152) + 1))
                v8 = load32(9568052)
                store32(arg2 + 28, v6)
                v10 = load32(arg2)
                v7 = load32(arg2 + 4)
                v11 = load32(9568048)
                store32(9568048, (load32(9568048) + 1))
                store32(((v11 << 2) + 9563952), arg2)
                store32(9568052, (v8 + ((v10 * (v7 + 2)) << 2)))
                v8 = load32(9568056)
                store32(arg2 + 56, load32(9568056))
                store32(9568056, (v8 + ((v7 * load32(arg2)) << 2)))
                break
            arg0 = load16u(arg0 + 110)
            store32(v3 + 76, arg1)
            store32(v3 + 72, 0)
            store32((v3 - -64), 0)
            store64(v3 + 56, 0)
            store32(v3 + 52, 0)
            store32(v3 + 48, v6)
            store64(v3 + 40, 0)
            store64(v3 + 32, 0)
            store64(v3 + 24, 0)
            if (v17 > 0.0):
            else:
            # TODO: f64.promote_f32
            storef64((((v17 * 0.5) / i32((v9 * 96))) + 0.25) + 16, v17)
            store32(v3 + 68, ((arg0 << 16) | 65535))
            storef64(v3 + 8, i32(v4))
            storef64(v3, i32(v5))
            a_b()
            break
        break
    G.global0 = (v3 + 192)
    return func40(i32(v5), i32(v4), v17, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, load32(9142740), (load16u(arg0 + 110) + 16), arg1, 1, 0, 0, 0.0)

# ----------------------------------------------------------
# $func103
# ----------------------------------------------------------
def func103(arg0):
    v4 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v1 = load32(CURRENT_PLAYER)
        if not load32(CURRENT_PLAYER):
            break
        if (v1 != load16u(arg0 + 110)):
            break
        v10 = load8u(arg0 + 122)
        if (load8u(arg0 + 122) == load32(38564)):
            break
        if load8u(9142917):
            break
        v11 = load16u(arg0 + 112)
        v1 = ((v10 * 404) + ENTITY_TYPES)
        v12 = load16u(arg0 + 114)
        v7 = ((load16u(arg0 + 112) + ((load32(((v10 * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1)) + ((load16u(arg0 + 114) + ((load32(v1 + 220) & 0xFFFFFFFF) >> 1)) << 16))
        v2 = load32(9216048)
        if load32(9216048):
            v5 = load32(9142848)
            v6 = load32(9216040)
            while True:  # $label2
                v1 = (v3 << 2)
                v8 = load32((v6 + (v3 << 2)))
                while True:  # $label1
                    v1 = ((v5 - load32((v6 + (v1 | 4)))) * 25)
                    if (u32(((v5 - load32((v6 + (v1 | 4)))) * 25)) <= u32(19999)):
                        v1 = ((v8 & 65535) - v11)
                        v1 = (((v8 & 0xFFFFFFFF) >> 16) - v12)
                        if ((((((v8 & 65535) - v11) * v1) + ((((v8 & 0xFFFFFFFF) >> 16) - v12) * v1)) - 1) >= 3601):
                            break
                        break
                    v9 = (((v7 == v8) & (u32(v1) < u32(35000))) | v9)
                    break
                v3 = (v3 + 2)
                if (u32((v3 + 2)) < u32(v2)):
                    continue
                break
            v3 = 0
            v6 = load32(9216040)
            v5 = load32(9142848)
            while True:  # $label3
                v1 = (v6 + ((v3 << 2) | 4))
                if (u32(((v5 - load32((v6 + ((v3 << 2) | 4)))) * 25)) >= u32(35001)):
                    store32((v6 + (v3 << 2)), v7)
                    store32(v1, load32(9142848))
                    arg0 = load32(((v10 * 404) + ENTITY_TYPES) + 264)
                    store32(v4 + 28, (v9 & 1))
                    store32(v4 + 20, v12)
                    store32(v4 + 16, v11)
                    store32(v4 + 24, (arg0 == 1))
                    break
                v3 = (v3 + 2)
                if (u32((v3 + 2)) < u32(v2)):
                    continue
                break
        while True:  # $label4
            if (load32(9216044) != v2):
                v1 = load32(9216040)
                break
            v1 = (load32(9216052) + v2)
            store32(9216044, (load32(9216052) + v2))
            v5 = load32(9216040)
            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
            if v2:
                # TODO: memory.copy
            if v5:
                v2 = load32(9216048)
            store32(9216040, v1)
            break
        store32(9216048, (v2 + 1))
        store32((v1 + (v2 << 2)), v7)
        v5 = load32(9142848)
        while True:  # $label5
            v3 = load32(9216048)
            if (load32(9216048) != load32(9216044)):
                v2 = v1
                break
            v2 = (load32(9216052) + v3)
            store32(9216044, (load32(9216052) + v3))
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if v3:
                # TODO: memory.copy
            store32(9216040, v2)
            v3 = load32(9216048)
            break
        store32(9216048, (v3 + 1))
        store32((v2 + (v3 << 2)), v5)
        v2 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264)
        v1 = load16u(arg0 + 112)
        arg0 = load16u(arg0 + 114)
        store32(v4 + 12, (v9 & 1))
        store32(v4 + 4, arg0)
        store32(v4, v1)
        store32(v4 + 8, (v2 == 1))
        break
    G.global0 = (v4 + 32)

# ----------------------------------------------------------
# $func104
# ----------------------------------------------------------
def func104(arg0, arg1):
    return func309(((arg1 << 1) + 32304), 2, arg0)

# ----------------------------------------------------------
# $func105
# ----------------------------------------------------------
def func105(arg0, arg1):
    while True:  # $label0
        v2 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            v3 = load32(arg0)
            break
        v3 = (load32(arg0 + 12) + v2)
        store32(arg0 + 4, (load32(arg0 + 12) + v2))
        v4 = load32(arg0)
        v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
        if v2:
            # TODO: memory.copy
        if v4:
            v2 = load32(arg0 + 8)
        store32(arg0, v3)
        break
    store32(arg0 + 8, (v2 + 1))
    store32((v3 + (v2 << 2)), arg1)

# ----------------------------------------------------------
# $func106
# ----------------------------------------------------------
def func106(arg0, arg1, arg2, arg3):
    v10 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label1
        while True:  # $label2
            while True:  # $label0
                if (u32(load32(9142848)) >= u32((load32(load32(GAME_STATE) + 72) * 2400))):
                    break
                v5 = load8u(arg0 + 122)
                if (load32(arg0 + 56) == 1):
                    if (load32(((v5 * 404) + ENTITY_TYPES) + 268) == 1):
                        break
                if not load8u(((v5 * 404) + ENTITY_TYPES) + 336):
                    break
                if not load16u(arg0 + 120):
                    break
                break
                break
            if load16u(arg0 + 120):
                break
            v5 = load8u(arg0 + 122)
            break
        store32(v10 + 12, 0)
        v4 = ((v5 * 404) + ENTITY_TYPES)
        v14 = load32(((v5 * 404) + ENTITY_TYPES) + 200)
        v7 = load32(((v5 * 404) + ENTITY_TYPES) + 200)
        if (load32(v4 + 268) == 1):
            v7 = load32(v4 + 224)
        v8 = load16u(arg0 + 114)
        v11 = load16u(arg0 + 112)
        v15 = load16u(arg0 + 110)
        v16 = (load16u(arg0 + 110) * 286704)
        v6 = load32(PLAYERS)
        while True:  # $label5
            while True:  # $label3
                while True:  # $label4
                    # br_table load32(v4 + 264)
                    break
                    break
                v4 = ((v5 * 404) + ENTITY_TYPES)
                v9 = load32(((v5 * 404) + ENTITY_TYPES) + 216)
                if not load32(((v5 * 404) + ENTITY_TYPES) + 216):
                    break
                v13 = load32(v4 + 220)
                if not load32(v4 + 220):
                    break
                v4 = load32(9215880)
                if not load32(9215880):
                    break
                v17 = load32(9142432)
                if not load32(9142432):
                    break
                v18 = load32(9142440)
                v19 = load32(v4)
                v5 = 0
                while True:  # $label7
                    v20 = (v5 + v11)
                    v4 = 0
                    while True:  # $label6
                        v12 = load32((v17 + ((v20 + ((v4 + v8) * v18)) << 2)))
                        if not load32((v19 + (load32((v17 + ((v20 + ((v4 + v8) * v18)) << 2))) << 2))):
                            break
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v13):
                            continue
                        break
                    v12 = 0
                    v5 = (v5 + 1)
                    if ((v5 + 1) != v9):
                        continue
                    break
                break
                break
            v4 = load32(9142432)
            if not load32(9142432):
                break
            v12 = load32((v4 + (((load32(9142440) * v8) + v11) << 2)))
            break
        v16 = (v6 + v16)
        v4 = load8u(arg0 + 127)
        store32(v10 + 8, 2147483647)
        while True:  # $label9
            while True:  # $label8
                if load8u(9216060):
                    v5 = load8u(9671158)
                    v6 = load8u(9671157)
                    break
                v6 = load8u(9671157)
                v5 = load8u(9671158)
                if (u32(load32((v6 + (v15 * 286704)) + 283924)) > u32((((v7 * v7) * (((load8u(9671157) + load8u(9671158)) + 1) & 255)) * 3))):
                    break
                if (v4 == 6):
                    break
                v6 = 0
                v4 = load32(PLAYER_COUNT)
                if not load32(PLAYER_COUNT):
                    break
                while True:  # $label14
                    if load8u((load32(9143004) + ((v4 * v15) + v6))):
                        v7 = load32(PLAYERS)
                        arg2 = 0
                        while True:  # $label13
                            while True:  # $label10
                                arg3 = ((arg2 * 404) + ENTITY_TYPES)
                                if (load32(((arg2 * 404) + ENTITY_TYPES) + 264) == 2):
                                    break
                                if (load32(arg3 + 188) != 55):
                                    break
                                v5 = load32((((v7 + (v6 * 286704)) + (arg2 << 2)) + 284636))
                                if not load32((((v7 + (v6 * 286704)) + (arg2 << 2)) + 284636)):
                                    break
                                v4 = 0
                                v8 = load32(v5 + 8)
                                if not load32(v5 + 8):
                                    break
                                while True:  # $label12
                                    while True:  # $label11
                                        arg3 = load32((load32(v5) + (v4 << 2)))
                                        if not load32((load32(v5) + (v4 << 2))):
                                            break
                                        arg3 = entities[arg3]
                                        if load32(entities[arg3].action):
                                            break
                                        v11 = load16u(arg3 + 112)
                                        v9 = (load16u(arg0 + 112) - load16u(arg3 + 112))
                                        v9 = (v9 >> 31)
                                        if ((((load16u(arg0 + 112) - load16u(arg3 + 112)) ^ (v9 >> 31)) - v9) > v14):
                                            break
                                        v9 = load16u(arg3 + 114)
                                        v13 = (load16u(arg0 + 114) - load16u(arg3 + 114))
                                        v13 = (v13 >> 31)
                                        if ((((load16u(arg0 + 114) - load16u(arg3 + 114)) ^ (v13 >> 31)) - v13) > v14):
                                            break
                                        break
                                    v4 = (v4 + 1)
                                    if ((v4 + 1) != v8):
                                        continue
                                    break
                                break
                            arg2 = (arg2 + 1)
                            if ((arg2 + 1) != 255):
                                continue
                            break
                        v4 = load32(PLAYER_COUNT)
                    v6 = (v6 + 1)
                    if (u32((v6 + 1)) < u32(v4)):
                        continue
                    break
                break
                break
            v14 = (load32(9142836) + (v7 * 80))
            v9 = load32((load32(9142836) + (v7 * 80)) + 4)
            if not load32((load32(9142836) + (v7 * 80)) + 4):
                break
            v13 = (v8 if (arg3 == -1) else arg3)
            v11 = (v11 if (arg2 == -1) else arg2)
            v17 = (v5 | 2)
            arg2 = not (v6 & 255)
            v18 = (v4 == 6)
            v5 = load32(9142440)
            v6 = 0
            while True:  # $label17
                while True:  # $label15
                    arg3 = load32(v14)
                    v4 = (v6 << 2)
                    v7 = (load32((load32(v14) + ((v6 << 2) | 4))) + v13)
                    if (u32(v5) <= u32((load32((load32(v14) + ((v6 << 2) | 4))) + v13))):
                        break
                    v8 = (load32((arg3 + v4)) + v11)
                    if (u32(v5) <= u32((load32((arg3 + v4)) + v11))):
                        break
                    if ((v7 | v8) < 0):
                        break
                    v19 = (v8 + 1)
                    v20 = (v7 + 1)
                    arg3 = load32(9142840)
                    v4 = arg2
                    while True:  # $label16
                        v21 = (v5 + 2)
                        v21 = load32((arg3 + ((v19 + ((v20 + ((v5 + 2) * v4)) * v21)) << 2)))
                        if (u32(load32((arg3 + ((v19 + ((v20 + ((v5 + 2) * v4)) * v21)) << 2)))) >= u32(3)):
                            v5 = load32(9142440)
                            arg3 = load32(9142840)
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v17):
                            continue
                        break
                    break
                v6 = (v6 + 2)
                if (u32((v6 + 2)) < u32(v9)):
                    continue
                break
            break
        v4 = load32(v10 + 12)
        break
    G.global0 = (v10 + 16)
    return v4
