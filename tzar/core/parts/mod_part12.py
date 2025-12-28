"""
Tzar Engine - Core module (part 12).
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
# $func400
# ----------------------------------------------------------
def func400(arg0):
    while True:  # $label0
        if not arg0:
            break
        if not load32(arg0 + 32):
            break
        v2 = load32(arg0 + 36)
        if not load32(arg0 + 36):
            break
        v1 = load32(arg0 + 28)
        if not load32(arg0 + 28):
            break
        if (load32(v1) != arg0):
            break
        while True:  # $label1
            while True:  # $label2
                v3 = load32(v1 + 4)
                # br_table (load32(v1 + 4) - 57)
                break
                break
            if (v3 == 666):
                break
            if (v3 != 42):
                break
            break
        v3 = load32(v1 + 8)
        if load32(v1 + 8):
            v1 = load32(arg0 + 28)
        v2 = load32(v1 + 68)
        if load32(v1 + 68):
            v1 = load32(arg0 + 28)
        v2 = load32(v1 + 64)
        if load32(v1 + 64):
            v1 = load32(arg0 + 28)
        v2 = load32(v1 + 56)
        if load32(v1 + 56):
            v1 = load32(arg0 + 28)
        store32(arg0 + 28, 0)
        break

# ----------------------------------------------------------
# $func401
# ----------------------------------------------------------
def func401(arg0, arg1, arg2):
    v5 = load32(9681936)
    if load32(load32(9681936) + 8):
        v9 = (arg1 + arg2)
        v13 = (arg0 + arg2)
        v10 = load32(9684500)
        v11 = load32(9684496)
        while True:  # $label9
            v12 = (load32(v5) + (v4 << 2))
            v6 = load32((load32(v5) + (v4 << 2)))
            arg2 = 0
            while True:  # $label0
                v8 = load32((v11 - 16))
                if load32((v11 - 16)):
                    while True:  # $label1
                        v3 = (v11 + (arg2 * 60))
                        if (load32((v11 + (arg2 * 60)) + 52) == v6):
                            break
                        arg2 = (arg2 + 1)
                        if ((arg2 + 1) != v8):
                            continue
                        break
                arg2 = 0
                v3 = v10
                if (load32(v10 + 52) == v6):
                    break
                while True:  # $label2
                    arg2 = (arg2 + 1)
                    v3 = (v10 + ((arg2 + 1) * 60))
                    if (load32((v10 + ((arg2 + 1) * 60)) + 52) != v6):
                        continue
                    break
                break
            v6 = (load32(v3 + 4) // (load32(v3 + 20) * load32(v3 + 16)))
            v7 = (load32(v12 + 8) - load32(v3 + 12))
            while True:  # $label7
                while True:  # $label4
                    while True:  # $label3
                        arg2 = (load32(v12 + 4) - load32(v3 + 8))
                        v8 = (((load32(v12 + 4) - load32(v3 + 8)) > arg0) & (arg2 < v13))
                        if not (((load32(v12 + 4) - load32(v3 + 8)) > arg0) & (arg2 < v13)):
                            break
                        if (arg1 >= v7):
                            break
                        if (v7 < v9):
                            break
                        break
                    arg2 = (load32(v3) + arg2)
                    arg2 = (((load32(v3) + arg2) > arg0) & (arg2 < v13))
                    while True:  # $label5
                        if (arg1 >= v7):
                            break
                        if not arg2:
                            break
                        if (v7 < v9):
                            break
                        break
                    while True:  # $label6
                        if not arg2:
                            break
                        arg2 = (v6 + v7)
                        if ((v6 + v7) <= arg1):
                            break
                        if (arg2 < v9):
                            break
                        break
                    if not v8:
                        break
                    arg2 = (v6 + v7)
                    if ((v6 + v7) <= arg1):
                        break
                    if (arg2 >= v9):
                        break
                    break
                func38(load32(v12 + 12))
                v5 = load32(9681936)
                arg2 = (load32(v5 + 8) - 4)
                store32(load32(9681936) + 8, (load32(v5 + 8) - 4))
                v10 = load32(9684500)
                v11 = load32(9684496)
                if (u32(arg2) > u32(v4)):
                    v8 = load32(v5)
                    arg2 = v4
                    while True:  # $label8
                        v3 = (v8 + (arg2 << 2))
                        store32((v8 + (arg2 << 2)), load32(v3 + 16))
                        arg2 = (arg2 + 1)
                        if (u32((arg2 + 1)) < u32(load32(v5 + 8))):
                            continue
                        break
                v4 = (v4 - 4)
                break
            v4 = (v4 + 4)
            if (u32((v4 + 4)) < u32(load32(v5 + 8))):
                continue
            break

# ----------------------------------------------------------
# $func402
# ----------------------------------------------------------
def func402(arg0):
    store32(9142440, arg0)
    store32(9142852, 0)
    v5 = (arg0 * arg0)
    v9 = ((arg0 * arg0) << 1)
    v1 = func26(((arg0 * arg0) << 1))
    # TODO: memory.fill
    store32(9142436, v1)
    v1 = (arg0 + 2)
    v10 = ((arg0 + 2) * v1)
    v2 = func26((-1 if (u32((v10 * 3)) > u32(1073741823)) else (((arg0 + 2) * v1) * 12)))
    if v1:
        v12 = (v1 & -2)
        v13 = (arg0 & 1)
        v8 = (arg0 + 1)
        v7 = (v1 << 1)
        v14 = ((v1 << 1) * v1)
        while True:  # $label3
            while True:  # $label1
                if not v4:
                    v3 = 0
                    v6 = 0
                    if v8:
                        while True:  # $label0
                            store32((v2 + ((v1 * v3) << 2)), -1)
                            store32((v2 + (((v1 + v3) * v1) << 2)), -1)
                            store32((v2 + (((v3 + v7) * v1) << 2)), -1)
                            v11 = (v3 | 1)
                            store32((v2 + (((v3 | 1) * v1) << 2)), -1)
                            store32((v2 + (((v1 + v11) * v1) << 2)), -1)
                            store32((v2 + (((v7 + v11) * v1) << 2)), -1)
                            v3 = (v3 + 2)
                            v6 = (v6 + 2)
                            if ((v6 + 2) != v12):
                                continue
                            break
                    if not v13:
                        break
                    store32((v2 + ((v1 * v3) << 2)), -1)
                    store32((v2 + (((v1 + v3) * v1) << 2)), -1)
                    store32((v2 + (((v3 + v7) * v1) << 2)), -1)
                    break
                store32((v2 + (v4 << 2)), -1)
                store32((v2 + ((v4 + v10) << 2)), -1)
                store32((v2 + ((v4 + v14) << 2)), -1)
                v3 = 1
                if (v1 == 1):
                    break
                while True:  # $label2
                    v6 = (0 - ((v3 == v8) | (v4 == v8)))
                    store32((v2 + (((v1 * v3) + v4) << 2)), (0 - ((v3 == v8) | (v4 == v8))))
                    store32((v2 + ((((v1 + v3) * v1) + v4) << 2)), v6)
                    store32((v2 + ((((v3 + v7) * v1) + v4) << 2)), v6)
                    v3 = (v3 + 1)
                    if ((v3 + 1) != v1):
                        continue
                    break
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != v1):
                continue
            break
    store32(9142840, v2)
    if not load8u(9216060):
        v1 = (-1 if (u32(v5) > u32(1073741823)) else (v5 << 2))
        v2 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
        # TODO: memory.fill
        store32(9142432, v2)
    while True:  # $label4
        if load8u(9147152):
            break
        v2 = load32(GAME_STATE)
        if not load32(load32(GAME_STATE) + 48):
            break
        if load32(9147376):
            break
        v3 = (v9 | 4)
        v1 = func26((v9 | 4))
        # TODO: memory.fill
        store32(9147376, v1)
        if not load32(v2 + 172):
            break
        if (load32(v2 + 48) != 2):
            break
        if not arg0:
            break
        v2 = (1 if (u32(v5) <= u32(1)) else v5)
        v3 = ((1 if (u32(v5) <= u32(1)) else v5) & 5)
        v4 = 0
        arg0 = 0
        if (u32((v2 - 1)) >= u32(7)):
            v5 = (v2 & 2147483640)
            while True:  # $label5
                v2 = (arg0 << 1)
                store16((v1 + (arg0 << 1)), 1)
                store16((v1 + (v2 | 2)), 1)
                store16((v1 + (v2 | 4)), 1)
                store16((v1 + (v2 | 6)), 1)
                store16((v1 + (v2 | 8)), 1)
                store16((v1 + (v2 | 10)), 1)
                store16((v1 + (v2 | 12)), 1)
                store16((v1 + (v2 | 14)), 1)
                arg0 = (arg0 + 8)
                v15 = (v15 + 8)
                if ((v15 + 8) != v5):
                    continue
                break
        if not v3:
            break
        while True:  # $label6
            store16((v1 + (arg0 << 1)), 1)
            arg0 = (arg0 + 1)
            v4 = (v4 + 1)
            if ((v4 + 1) != v3):
                continue
            break
        break
    store32(9147360, -1)
    store32(9147344, 1)
    arg0 = load32(9142440)
    store32(9147368, load32(9142440))
    store32(9147372, (arg0 + 1))
    store32(9147364, (arg0 - 1))
    store32(9147356, (arg0 ^ -1))
    store32(9147352, (0 - arg0))
    store32(9147348, (1 - arg0))

# ----------------------------------------------------------
# $func403
# ----------------------------------------------------------
def func403(arg0):
    v4 = load32(9142440)
    v5 = (load32(9142440) + 2)
    v9 = load32(9215884)
    v6 = load32(arg0 + 28)
    v7 = load32(ENTITIES)
    v10 = load32(9142840)
    v11 = load16u(arg0 + 114)
    v12 = load16u(arg0 + 112)
    v13 = load16u(arg0 + 110)
    while True:  # $label4
        while True:  # $label3
            while True:  # $label0
                v8 = v1
                v2 = (v1 << 2)
                v1 = (load32((((v1 << 2) | 4) + 8611904)) + v11)
                if (u32(v4) <= u32((load32((((v1 << 2) | 4) + 8611904)) + v11))):
                    break
                v2 = (load32((v2 + 8611904)) + v12)
                if (u32(v4) <= u32((load32((v2 + 8611904)) + v12))):
                    break
                if ((v1 | v2) < 0):
                    break
                while True:  # $label1
                    while True:  # $label2
                        v2 = load32((((v2 + (((v1 + v5) + 1) * v5)) << 2) + v10) + 4)
                        v1 = (v7 + (load32((((v2 + (((v1 + v5) + 1) * v5)) << 2) + v10) + 4) * 132))
                        v3 = load8u((v7 + (load32((((v2 + (((v1 + v5) + 1) * v5)) << 2) + v10) + 4) * 132)) + 122)
                        # br_table (load8u((v7 + (load32((((v2 + (((v1 + v5) + 1) * v5)) << 2) + v10) + 4) * 132)) + 122) + -64)
                        break
                        break
                    if (v3 != 10):
                        break
                    break
                if (load16u(v1 + 110) != v13):
                    break
                if (load32(v1 + 32) == v6):
                    break
                if (load8u(v1 + 129) != 10):
                    break
                v3 = load32(v1 + 44)
                if not ((load32((v9 + (load32(v1 + 44) << 4)) + 4) == 22) | not v3):
                    break
                if load8u(v1 + 125):
                    break
                if load32(v1 + 36):
                    break
                v1 = (v7 + (v2 * 132))
                store32(arg0 + 96, load32(v1 + 28))
                return
                break
            v1 = (v8 + 2)
            if (u32(v8) < u32(2734)):
                continue
            break
        break

# ----------------------------------------------------------
# $func404
# ----------------------------------------------------------
def func404(arg0):
    v13 = load32(ENTITIES)
    v1 = entities[arg0]
    store8(entities[arg0] + 129, 10)
    v5 = load32(9142440)
    v14 = (load32(9142440) + 2)
    v16 = load32(38984)
    v17 = ((load32(9142440) + 2) * load32(((load32(38984) * 404) + ENTITY_TYPES) + 208))
    v9 = load16u(v1 + 112)
    v18 = (load16u(v1 + 112) + 29)
    v10 = load16u(v1 + 114)
    v19 = (load16u(v1 + 114) + 29)
    v11 = (v10 - 30)
    v2 = (v9 - 30)
    v8 = load32(ENTITIES)
    v15 = load32(9142840)
    v6 = 2147483647
    while True:  # $label2
        v3 = (v2 + 1)
        if (u32(v2) < u32(v5)):
            v1 = (v9 - v2)
            v20 = ((v9 - v2) * v1)
            v1 = v11
            while True:  # $label1
                while True:  # $label0
                    v4 = v1
                    if (u32(v5) <= u32(v1)):
                        break
                    if ((v2 | v4) < 0):
                        break
                    v1 = (v10 - v4)
                    v12 = (((v10 - v4) * v1) + v20)
                    if ((((v10 - v4) * v1) + v20) >= v6):
                        break
                    v1 = load32((v15 + (((((v4 + v17) + 1) * v14) + v3) << 2)))
                    if not load32((v15 + (((((v4 + v17) + 1) * v14) + v3) << 2))):
                        break
                    v12 = (v16 == load8u((v8 + (v1 * 132)) + 122))
                    v6 = (v12 if (v16 == load8u((v8 + (v1 * 132)) + 122)) else v6)
                    v7 = (v1 if v12 else v7)
                    break
                v1 = (v4 + 1)
                if (v4 != v19):
                    continue
                break
        v1 = (v2 != v18)
        v2 = v3
        if v1:
            continue
        break
    v4 = (v13 + (arg0 * 132))
    if v7:
        return
    v11 = (v5 + 3)
    v6 = load32(38528)
    v7 = load16u((v13 + (arg0 * 132)) + 110)
    v1 = 0
    while True:  # $label6
        while True:  # $label5
            while True:  # $label4
                while True:  # $label3
                    v2 = v1
                    v3 = (v1 << 2)
                    v1 = (load32((((v1 << 2) | 4) + 8611904)) + v10)
                    if (u32(v5) <= u32((load32((((v1 << 2) | 4) + 8611904)) + v10))):
                        break
                    v3 = (load32((v3 + 8611904)) + v9)
                    if (u32(v5) <= u32((load32((v3 + 8611904)) + v9))):
                        break
                    if ((v1 | v3) < 0):
                        break
                    v3 = load32((((v3 + ((v1 + v11) * v14)) << 2) + v15) + 4)
                    v1 = (v8 + (load32((((v3 + ((v1 + v11) * v14)) << 2) + v15) + 4) * 132))
                    if (v6 != load8u((v8 + (load32((((v3 + ((v1 + v11) * v14)) << 2) + v15) + 4) * 132)) + 122)):
                        break
                    if (u32(load32(v1 + 72)) < u32(50)):
                        break
                    if (load8u(v1 + 125) == 12):
                        break
                    if (load16u(v1 + 110) != v7):
                        break
                    if not load32(v1 + 96):
                        break
                    break
                v1 = (v2 + 2)
                if (u32(v2) <= u32(16557)):
                    continue
                break
                break
            break
        v1 = load32((v8 + (v3 * 132)) + 28)
        if not load32((v8 + (v3 * 132)) + 28):
            break
        store32((v8 + (v1 * 132)) + 96, arg0)
        return
        break
    func29(v4, 1)

# ----------------------------------------------------------
# $func406
# ----------------------------------------------------------
def func406(arg0, arg1, arg2):
    while True:  # $label0
        if not load32(arg0 + 5792):
            v3 = load32(arg0 + 5820)
            break
        v9 = (arg0 + 5817)
        while True:  # $label6
            v11 = (v4 + 3)
            v4 = (load32(arg0 + 5784) + v4)
            v5 = load8u((load32(arg0 + 5784) + v4) + 2)
            while True:  # $label5
                while True:  # $label1
                    v6 = load16u(v4)
                    if not load16u(v4):
                        v3 = (arg1 + (v5 << 2))
                        v4 = load16u((arg1 + (v5 << 2)) + 2)
                        v5 = load16u(v3)
                        v3 = load32(arg0 + 5820)
                        v6 = (load16u(arg0 + 5816) | (load16u(v3) << load32(arg0 + 5820)))
                        store16(arg0 + 5816, (load16u(arg0 + 5816) | (load16u(v3) << load32(arg0 + 5820))))
                        if ((16 - v4) < v3):
                            v3 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v3 + load32(arg0 + 8)), v6)
                            v3 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v3 + load32(arg0 + 8)), load8u(v9))
                            v3 = load32(arg0 + 5820)
                            store16(arg0 + 5816, ((v5 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                            break
                        break
                    v10 = load8u((v5 + 23984))
                    v7 = (load8u((v5 + 23984)) << 2)
                    v4 = ((load8u((v5 + 23984)) << 2) + arg1)
                    v3 = load16u((((load8u((v5 + 23984)) << 2) + arg1) + 1030))
                    v12 = load16u((v4 + 1028))
                    v8 = load32(arg0 + 5820)
                    v4 = (load16u(arg0 + 5816) | (load16u((v4 + 1028)) << load32(arg0 + 5820)))
                    store16(arg0 + 5816, (load16u(arg0 + 5816) | (load16u((v4 + 1028)) << load32(arg0 + 5820))))
                    while True:  # $label2
                        if ((16 - v3) < v8):
                            v8 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v8 + load32(arg0 + 8)), v4)
                            v4 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v4 + load32(arg0 + 8)), load8u(v9))
                            v8 = load32(arg0 + 5820)
                            v4 = ((v12 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                            store16(arg0 + 5816, ((v12 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                            break
                        break
                    v3 = (v3 + v8)
                    store32(((v3 + v8) - 16) + 5820, (v3 + v8))
                    if (u32((v10 - 28)) >= u32(-20)):
                        v5 = (v5 - load32((v7 + 25952)))
                        while True:  # $label3
                            v7 = load32((v7 + 25584))
                            if ((16 - load32((v7 + 25584))) < v3):
                                v4 = (v4 | (v5 << v3))
                                store16(arg0 + 5816, (v4 | (v5 << v3)))
                                v3 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v3 + load32(arg0 + 8)), v4)
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), load8u(v9))
                                v3 = load32(arg0 + 5820)
                                v4 = (((v5 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                                store16(arg0 + 5816, (((v5 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                break
                            v4 = (v4 | (v5 << v3))
                            store16(arg0 + 5816, (v4 | (v5 << v3)))
                            break
                        v3 = (v3 + v7)
                        store32(((v3 + v7) - 16) + 5820, (v3 + v7))
                    v7 = (v6 - 1)
                    v8 = load8u((((v6 - 1) if (u32(v6) < u32(257)) else (((v7 & 0xFFFFFFFF) >> 7) + 256)) + 23472))
                    v6 = (load8u((((v6 - 1) if (u32(v6) < u32(257)) else (((v7 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)
                    v10 = (arg2 + (load8u((((v6 - 1) if (u32(v6) < u32(257)) else (((v7 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2))
                    v5 = load16u((arg2 + (load8u((((v6 - 1) if (u32(v6) < u32(257)) else (((v7 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2)
                    v10 = load16u(v10)
                    v4 = (v4 | (load16u(v10) << v3))
                    store16(arg0 + 5816, (v4 | (load16u(v10) << v3)))
                    while True:  # $label4
                        if ((16 - v5) < v3):
                            v3 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v3 + load32(arg0 + 8)), v4)
                            v4 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v4 + load32(arg0 + 8)), load8u(v9))
                            v3 = load32(arg0 + 5820)
                            v4 = ((v10 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                            store16(arg0 + 5816, ((v10 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                            break
                        break
                    v3 = (v3 + v5)
                    store32(((v3 + v5) - 16) + 5820, (v3 + v5))
                    if (u32(v8) < u32(4)):
                        break
                    v5 = (v7 - load32((v6 + 26080)))
                    v6 = load32((v6 + 25712))
                    if ((16 - load32((v6 + 25712))) < v3):
                        v4 = (v4 | (v5 << v3))
                        store16(arg0 + 5816, (v4 | (v5 << v3)))
                        v3 = load32(arg0 + 20)
                        store32(arg0 + 20, (load32(arg0 + 20) + 1))
                        store8((v3 + load32(arg0 + 8)), v4)
                        v4 = load32(arg0 + 20)
                        store32(arg0 + 20, (load32(arg0 + 20) + 1))
                        store8((v4 + load32(arg0 + 8)), load8u(v9))
                        v4 = load32(arg0 + 5820)
                        store16(arg0 + 5816, (((v5 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                        break
                    store16(arg0 + 5816, (v4 | (v5 << v3)))
                    break
                v3 = (v3 + v6)
                store32(((v4 + v6) - 16) + 5820, (v3 + v6))
                break
            v4 = v11
            if (u32(v11) < u32(load32(arg0 + 5792))):
                continue
            break
        break
    arg2 = load16u((arg1 + 1026))
    arg1 = load16u(arg1 + 1024)
    v4 = (load16u(arg0 + 5816) | (load16u(arg1 + 1024) << v3))
    store16(arg0 + 5816, (load16u(arg0 + 5816) | (load16u(arg1 + 1024) << v3)))
    if ((16 - arg2) < v3):
        v11 = load32(arg0 + 20)
        store32(arg0 + 20, (load32(arg0 + 20) + 1))
        store8((v11 + load32(arg0 + 8)), v4)
        v4 = load32(arg0 + 20)
        store32(arg0 + 20, (load32(arg0 + 20) + 1))
        store8((v4 + load32(arg0 + 8)), load8u((arg0 + 5817)))
        arg1 = load32(arg0 + 5820)
        store16(arg0 + 5816, ((arg1 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
        store32(arg0 + 5820, ((arg1 + arg2) - 16))
        return arg0
    store32(arg0 + 5820, (arg2 + v3))
    return arg0

# ----------------------------------------------------------
# $func407
# ----------------------------------------------------------
def func407(arg0, arg1, arg2, arg3, arg4):
    v10 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v14 = load32(arg1)
    store32(arg1, 0)
    store32(v10 + 48, 0)
    store64(v10 + 40, 0)
    while True:  # $label3
        v5 = (v10 + 8)
        v7 = -6
        while True:  # $label0
            if (load8u(7784) != 49):
                break
            v7 = -2
            if not v5:
                break
            store32(v5 + 24, 0)
            v8 = load32(v5 + 32)
            if not load32(v5 + 32):
                store32(v5 + 40, 0)
                store32(v5 + 32, 417)
                v8 = 417
            if not load32(v5 + 36):
                store32(v5 + 36, 418)
            v9 = (6 if (arg4 == -1) else arg4)
            if (u32((6 if (arg4 == -1) else arg4)) > u32(9)):
                break
            v7 = -4
            arg4 = call_table(v8)
            if not call_table(v8):
                break
            store32(v5 + 28, arg4)
            store32(arg4 + 28, 0)
            store32(arg4 + 24, 1)
            store32(arg4 + 4, 42)
            store32(arg4, v5)
            store32(arg4 + 80, 15)
            store32(arg4 + 76, 32768)
            store32(arg4 + 48, 15)
            store32(arg4 + 84, 32767)
            store32(arg4 + 44, 32768)
            store32(arg4 + 88, 5)
            store32(arg4 + 52, 32767)
            store32(2 + 56, call_table(load32(v5 + 32)))
            store32(2 + 64, call_table(load32(v5 + 32)))
            v7 = call_table(load32(v5 + 32))
            store32(arg4 + 5824, 0)
            store32(arg4 + 68, v7)
            store32(arg4 + 5788, 16384)
            v7 = call_table(load32(v5 + 32))
            store32(4 + 8, call_table(load32(v5 + 32)))
            v8 = load32(arg4 + 5788)
            store32(arg4 + 12, (load32(arg4 + 5788) << 2))
            while True:  # $label2
                while True:  # $label1
                    if not load32(arg4 + 56):
                        break
                    if not load32(arg4 + 64):
                        break
                    if not load32(arg4 + 68):
                        break
                    if v7:
                        break
                    break
                store32(arg4 + 4, 666)
                store32(v5 + 24, load32(28712))
                func400(v5)
                break
                break
            store32(arg4 + 136, 0)
            store32(arg4 + 132, v9)
            store8(arg4 + 36, 8)
            store32(arg4 + 5784, (v7 + v8))
            store32(arg4 + 5796, ((v8 * 3) - 3))
            v7 = -2
            while True:  # $label4
                if not v5:
                    break
                if not load32(v5 + 32):
                    break
                if not load32(v5 + 36):
                    break
                arg4 = load32(v5 + 28)
                if not load32(v5 + 28):
                    break
                if (load32(arg4) != v5):
                    break
                while True:  # $label5
                    while True:  # $label6
                        v8 = load32(arg4 + 4)
                        # br_table (load32(arg4 + 4) - 57)
                        break
                        break
                    if (v8 == 666):
                        break
                    if (v8 != 42):
                        break
                    break
                store32(v5 + 44, 2)
                store32(v5 + 8, 0)
                store64(v5 + 20, 0)
                store32(arg4 + 20, 0)
                store32(arg4 + 16, load32(arg4 + 8))
                v7 = load32(arg4 + 24)
                if (load32(arg4 + 24) < 0):
                    v7 = (0 - v7)
                    store32(arg4 + 24, (0 - v7))
                v7 = (v7 == 2)
                store32(arg4 + 4, (57 if (v7 == 2) else 42))
                while True:  # $label7
                    if v7:
                        break
                    break
                store32(func43(0, 0, 0) + 48, func89(0, 0, 0))
                store32(arg4 + 40, -2)
                store32(arg4 + 5820, 0)
                store16(arg4 + 5816, 0)
                store32((arg4 + 2872), 24280)
                store32(arg4 + 2864, (arg4 + 2684))
                store32((arg4 + 2860), 24260)
                store32(arg4 + 2852, (arg4 + 2440))
                store32((arg4 + 2848), 24240)
                store32(arg4 + 2840, (arg4 + 148))
                func367(arg4)
                v7 = 0
                break
            if not v7:
                arg4 = load32(v5 + 28)
                store32(load32(v5 + 28) + 60, (load32(arg4 + 44) << 1))
                v5 = load32(arg4 + 68)
                v8 = ((load32(arg4 + 76) << 1) - 2)
                store16((load32(arg4 + 68) + ((load32(arg4 + 76) << 1) - 2)), 0)
                func98(v5, 0, v8)
                store32(arg4 + 5812, 0)
                store64(arg4 + 116, 8589934592)
                store64(arg4 + 104, 0)
                store64(arg4 + 92, 8589934592)
                store32(arg4 + 72, 0)
                v5 = (load32(arg4 + 132) * 12)
                store32(arg4 + 144, load16u(((load32(arg4 + 132) * 12) + 23348)))
                store32(arg4 + 140, load16u((v5 + 23344)))
                store32(arg4 + 128, load16u((v5 + 23346)))
                store32(arg4 + 124, load16u((v5 + 23350)))
            break
        break
    if not v7:
        store32(v10 + 24, 0)
        store32(v10 + 20, arg0)
        store32(v10 + 12, 0)
        store32(v10 + 8, arg2)
        while True:  # $label85
            if not v6:
                store32(v10 + 24, v14)
                v14 = 0
            while True:  # $label15
                v5 = (v10 + 8)
                while True:  # $label9
                    while True:  # $label8
                        if not load32(v10 + 12):
                            store32(v10 + 12, arg3)
                            break
                        if arg3:
                            break
                        break
                    arg3 = 0
                    break
                v9 = 4
                v8 = 0
                arg4 = -2
                while True:  # $label19
                    while True:  # $label16
                        while True:  # $label10
                            if not v5:
                                break
                            if not load32(v5 + 32):
                                break
                            if not load32(v5 + 36):
                                break
                            arg2 = load32(v5 + 28)
                            if not load32(v5 + 28):
                                break
                            if (load32(arg2) != v5):
                                break
                            while True:  # $label11
                                while True:  # $label12
                                    v7 = load32(arg2 + 4)
                                    # br_table (load32(arg2 + 4) - 57)
                                    break
                                    break
                                if (v7 == 666):
                                    break
                                if (v7 != 42):
                                    break
                                break
                            if (u32(v9) > u32(5)):
                                break
                            while True:  # $label14
                                while True:  # $label13
                                    if not load32(v5 + 12):
                                        break
                                    arg4 = load32(v5 + 4)
                                    if load32(v5 + 4):
                                        if not load32(v5):
                                            break
                                    if (v9 == 4):
                                        break
                                    if (v7 != 666):
                                        break
                                    break
                                store32(v5 + 24, load32(28704))
                                break
                                break
                            if not load32(v5 + 16):
                                break
                            arg0 = load32(arg2 + 40)
                            store32(arg2 + 40, v9)
                            while True:  # $label18
                                if load32(arg2 + 20):
                                    while True:  # $label17
                                        v8 = load32(arg2 + 20)
                                        v7 = load32(v5 + 16)
                                        arg0 = (load32(arg2 + 20) if (u32(v7) > u32(v8)) else load32(v5 + 16))
                                        if not (load32(arg2 + 20) if (u32(v7) > u32(v8)) else load32(v5 + 16)):
                                            break
                                        store32(v5 + 12, (load32(v5 + 12) + arg0))
                                        store32(arg2 + 16, (load32(arg2 + 16) + arg0))
                                        store32(v5 + 20, (load32(v5 + 20) + arg0))
                                        v7 = (load32(v5 + 16) - arg0)
                                        store32(v5 + 16, (load32(v5 + 16) - arg0))
                                        arg4 = load32(arg2 + 20)
                                        v8 = (load32(arg2 + 20) - arg0)
                                        store32(arg2 + 20, (load32(arg2 + 20) - arg0))
                                        if (arg0 != arg4):
                                            break
                                        store32(arg2 + 16, load32(arg2 + 8))
                                        break
                                    if v7:
                                        v7 = load32(arg2 + 4)
                                        break
                                    break
                                if arg4:
                                    break
                                if (v9 == 4):
                                    break
                                if (((v9 << 1) + (-9 if (u32(v9) > u32(4)) else 0)) > ((arg0 << 1) + (-9 if (arg0 > 4) else 0))):
                                    break
                                break
                                break
                            while True:  # $label47
                                while True:  # $label46
                                    while True:  # $label21
                                        while True:  # $label22
                                            while True:  # $label20
                                                if (v7 != 42):
                                                    if (v7 != 666):
                                                        break
                                                    if not load32(v5 + 4):
                                                        break
                                                    break
                                                if not load32(arg2 + 24):
                                                    store32(arg2 + 4, 113)
                                                    break
                                                v6 = ((load32(arg2 + 48) << 12) - 30720)
                                                arg4 = 0
                                                while True:  # $label23
                                                    if (load32(arg2 + 136) > 1):
                                                        break
                                                    arg0 = load32(arg2 + 132)
                                                    if (load32(arg2 + 132) < 2):
                                                        break
                                                    arg4 = 64
                                                    if (u32(arg0) < u32(6)):
                                                        break
                                                    arg4 = (128 if (arg0 == 6) else 192)
                                                    break
                                                store32(arg2 + 20, (v8 + 1))
                                                arg0 = (arg4 | v6)
                                                arg0 = (((arg4 | v6) | 32) if load32(arg2 + 108) else arg0)
                                                store8((load32(arg2 + 8) + v8), (((((arg4 | v6) | 32) if load32(arg2 + 108) else arg0) & 0xFFFFFFFF) >> 8))
                                                arg4 = load32(arg2 + 20)
                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                store8((arg4 + load32(arg2 + 8)), (((arg0 % 31) | arg0) ^ 31))
                                                if load32(arg2 + 108):
                                                    arg0 = load32(v5 + 48)
                                                    arg4 = load32(arg2 + 20)
                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                    store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 24))
                                                    arg4 = load32(arg2 + 20)
                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                    store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 16))
                                                    arg0 = load32(v5 + 48)
                                                    arg4 = load32(arg2 + 20)
                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                    store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 8))
                                                    arg4 = load32(arg2 + 20)
                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                    store8((arg4 + load32(arg2 + 8)), arg0)
                                                store32(v5 + 48, func89(0, 0, 0))
                                                store32(arg2 + 4, 113)
                                                func130(v5)
                                                if load32(arg2 + 20):
                                                    break
                                                v7 = load32(arg2 + 4)
                                                break
                                            while True:  # $label28
                                                while True:  # $label27
                                                    while True:  # $label26
                                                        while True:  # $label25
                                                            if (v7 == 57):
                                                                store32(v5 + 48, func43(0, 0, 0))
                                                                arg0 = load32(arg2 + 20)
                                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                store8((arg0 + load32(arg2 + 8)), 31)
                                                                arg0 = load32(arg2 + 20)
                                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                store8((arg0 + load32(arg2 + 8)), 139)
                                                                arg0 = load32(arg2 + 20)
                                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                store8((arg0 + load32(arg2 + 8)), 8)
                                                                while True:  # $label24
                                                                    arg0 = load32(arg2 + 28)
                                                                    if not load32(arg2 + 28):
                                                                        arg0 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg0 + load32(arg2 + 8)), 0)
                                                                        arg0 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg0 + load32(arg2 + 8)), 0)
                                                                        arg0 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg0 + load32(arg2 + 8)), 0)
                                                                        arg0 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg0 + load32(arg2 + 8)), 0)
                                                                        arg0 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg0 + load32(arg2 + 8)), 0)
                                                                        arg4 = 2
                                                                        arg0 = load32(arg2 + 132)
                                                                        if (load32(arg2 + 132) != 9):
                                                                            arg4 = (4 if (load32(arg2 + 136) > 1) else ((arg0 < 2) << 2))
                                                                        arg0 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg0 + load32(arg2 + 8)), arg4)
                                                                        arg0 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg0 + load32(arg2 + 8)), 3)
                                                                        store32(arg2 + 4, 113)
                                                                        func130(v5)
                                                                        if not load32(arg2 + 20):
                                                                            break
                                                                        break
                                                                    v6 = load32(arg0 + 36)
                                                                    v7 = load32(arg0 + 28)
                                                                    v8 = load32(arg0 + 16)
                                                                    v11 = load32(arg0 + 44)
                                                                    arg0 = load32(arg0)
                                                                    v12 = load32(arg2 + 20)
                                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                    arg4 = 2
                                                                    store8((v12 + load32(arg2 + 8)), ((((((v11 != 0) << 1) | (arg0 != 0)) | ((v8 != 0) << 2)) | ((v7 != 0) << 3)) | ((v6 != 0) << 4)))
                                                                    arg0 = load32(load32(arg2 + 28) + 4)
                                                                    v6 = load32(arg2 + 20)
                                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                    store8((v6 + load32(arg2 + 8)), arg0)
                                                                    arg0 = load32(load32(arg2 + 28) + 4)
                                                                    v6 = load32(arg2 + 20)
                                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                    store8((v6 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 8))
                                                                    arg0 = load16u(load32(arg2 + 28) + 6)
                                                                    v6 = load32(arg2 + 20)
                                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                    store8((v6 + load32(arg2 + 8)), arg0)
                                                                    arg0 = load8u(load32(arg2 + 28) + 7)
                                                                    v6 = load32(arg2 + 20)
                                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                    store8((v6 + load32(arg2 + 8)), arg0)
                                                                    arg0 = load32(arg2 + 132)
                                                                    if (load32(arg2 + 132) != 9):
                                                                        arg4 = (4 if (load32(arg2 + 136) > 1) else ((arg0 < 2) << 2))
                                                                    arg0 = load32(arg2 + 20)
                                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                    store8((arg0 + load32(arg2 + 8)), arg4)
                                                                    arg0 = load32(load32(arg2 + 28) + 12)
                                                                    arg4 = load32(arg2 + 20)
                                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                    store8((arg4 + load32(arg2 + 8)), arg0)
                                                                    arg0 = load32(arg2 + 28)
                                                                    if load32(load32(arg2 + 28) + 16):
                                                                        arg0 = load32(arg0 + 20)
                                                                        arg4 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg4 + load32(arg2 + 8)), arg0)
                                                                        arg0 = load32(load32(arg2 + 28) + 20)
                                                                        arg4 = load32(arg2 + 20)
                                                                        store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                                        store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 8))
                                                                    else:
                                                                    if load32(arg0 + 44):
                                                                        store32(v5 + 48, func43(load32(v5 + 48), load32(arg2 + 8), load32(arg2 + 20)))
                                                                    store32(arg2 + 4, 69)
                                                                    store32(arg2 + 32, 0)
                                                                    break
                                                                    break
                                                            else:
                                                            # br_table (v7 - 69)
                                                            break
                                                            break
                                                        arg0 = load32(arg2 + 28)
                                                        v8 = load32(load32(arg2 + 28) + 16)
                                                        if load32(load32(arg2 + 28) + 16):
                                                            v11 = load32(arg2 + 12)
                                                            arg4 = load32(arg2 + 20)
                                                            v7 = load32(arg2 + 32)
                                                            v6 = (load16u(arg0 + 20) - load32(arg2 + 32))
                                                            if (u32(load32(arg2 + 12)) < u32((load32(arg2 + 20) + (load16u(arg0 + 20) - load32(arg2 + 32))))):
                                                                v7 = (v11 - arg4)
                                                                arg0 = load32(arg2 + 12)
                                                                store32(arg2 + 20, load32(arg2 + 12))
                                                                while True:  # $label29
                                                                    if not load32(load32(arg2 + 28) + 44):
                                                                        break
                                                                    if (u32(arg0) <= u32(arg4)):
                                                                        break
                                                                    store32(v5 + 48, func43(load32(v5 + 48), (load32(arg2 + 8) + arg4), (arg0 - arg4)))
                                                                    break
                                                                store32(arg2 + 32, (load32(arg2 + 32) + v7))
                                                                arg0 = load32(v5 + 28)
                                                                while True:  # $label30
                                                                    arg4 = load32(arg0 + 20)
                                                                    v8 = load32(v5 + 16)
                                                                    arg4 = (load32(arg0 + 20) if (u32(arg4) < u32(v8)) else load32(v5 + 16))
                                                                    if not (load32(arg0 + 20) if (u32(arg4) < u32(v8)) else load32(v5 + 16)):
                                                                        break
                                                                    store32(v5 + 12, (load32(v5 + 12) + arg4))
                                                                    store32(arg0 + 16, (load32(arg0 + 16) + arg4))
                                                                    store32(v5 + 20, (load32(v5 + 20) + arg4))
                                                                    store32(v5 + 16, (load32(v5 + 16) - arg4))
                                                                    v8 = load32(arg0 + 20)
                                                                    store32(arg0 + 20, (load32(arg0 + 20) - arg4))
                                                                    if (arg4 != v8):
                                                                        break
                                                                    store32(arg0 + 16, load32(arg0 + 8))
                                                                    break
                                                                if load32(arg2 + 20):
                                                                    break
                                                                v6 = (v6 - v7)
                                                                v8 = load32(arg2 + 12)
                                                                if (u32((v6 - v7)) > u32(load32(arg2 + 12))):
                                                                    while True:  # $label33
                                                                        arg0 = load32(arg2 + 12)
                                                                        store32(arg2 + 20, load32(arg2 + 12))
                                                                        while True:  # $label31
                                                                            if not load32(load32(arg2 + 28) + 44):
                                                                                break
                                                                            if not arg0:
                                                                                break
                                                                            store32(v5 + 48, func43(load32(v5 + 48), load32(arg2 + 8), arg0))
                                                                            break
                                                                        store32(arg2 + 32, (load32(arg2 + 32) + v8))
                                                                        arg0 = load32(v5 + 28)
                                                                        while True:  # $label32
                                                                            arg4 = load32(arg0 + 20)
                                                                            v7 = load32(v5 + 16)
                                                                            arg4 = (load32(arg0 + 20) if (u32(arg4) < u32(v7)) else load32(v5 + 16))
                                                                            if not (load32(arg0 + 20) if (u32(arg4) < u32(v7)) else load32(v5 + 16)):
                                                                                break
                                                                            store32(v5 + 12, (load32(v5 + 12) + arg4))
                                                                            store32(arg0 + 16, (load32(arg0 + 16) + arg4))
                                                                            store32(v5 + 20, (load32(v5 + 20) + arg4))
                                                                            store32(v5 + 16, (load32(v5 + 16) - arg4))
                                                                            v7 = load32(arg0 + 20)
                                                                            store32(arg0 + 20, (load32(arg0 + 20) - arg4))
                                                                            if (arg4 != v7):
                                                                                break
                                                                            store32(arg0 + 16, load32(arg0 + 8))
                                                                            break
                                                                        if load32(arg2 + 20):
                                                                            break
                                                                        v6 = (v6 - v8)
                                                                        v8 = load32(arg2 + 12)
                                                                        if (u32((v6 - v8)) > u32(load32(arg2 + 12))):
                                                                            continue
                                                                        break
                                                                v7 = load32(arg2 + 32)
                                                                v8 = load32(load32(arg2 + 28) + 16)
                                                                arg4 = 0
                                                            arg0 = (load32(arg2 + 20) + v6)
                                                            store32(arg2 + 20, (load32(arg2 + 20) + v6))
                                                            while True:  # $label34
                                                                if not load32(load32(arg2 + 28) + 44):
                                                                    break
                                                                if (u32(arg0) <= u32(arg4)):
                                                                    break
                                                                store32(v5 + 48, func43(load32(v5 + 48), (load32(arg2 + 8) + arg4), (arg0 - arg4)))
                                                                break
                                                            store32(arg2 + 32, 0)
                                                        store32(arg2 + 4, 73)
                                                        break
                                                    if load32(load32(arg2 + 28) + 28):
                                                        v6 = load32(arg2 + 20)
                                                        while True:  # $label38
                                                            while True:  # $label35
                                                                arg4 = load32(arg2 + 20)
                                                                if (load32(arg2 + 20) != load32(arg2 + 12)):
                                                                    break
                                                                while True:  # $label36
                                                                    if not load32(load32(arg2 + 28) + 44):
                                                                        break
                                                                    if (u32(arg4) <= u32(v6)):
                                                                        break
                                                                    store32(v5 + 48, func43(load32(v5 + 48), (load32(arg2 + 8) + v6), (arg4 - v6)))
                                                                    break
                                                                arg0 = load32(v5 + 28)
                                                                while True:  # $label37
                                                                    arg4 = load32(arg0 + 20)
                                                                    v6 = load32(v5 + 16)
                                                                    arg4 = (load32(arg0 + 20) if (u32(arg4) < u32(v6)) else load32(v5 + 16))
                                                                    if not (load32(arg0 + 20) if (u32(arg4) < u32(v6)) else load32(v5 + 16)):
                                                                        break
                                                                    store32(v5 + 12, (load32(v5 + 12) + arg4))
                                                                    store32(arg0 + 16, (load32(arg0 + 16) + arg4))
                                                                    store32(v5 + 20, (load32(v5 + 20) + arg4))
                                                                    store32(v5 + 16, (load32(v5 + 16) - arg4))
                                                                    v6 = load32(arg0 + 20)
                                                                    store32(arg0 + 20, (load32(arg0 + 20) - arg4))
                                                                    if (arg4 != v6):
                                                                        break
                                                                    store32(arg0 + 16, load32(arg0 + 8))
                                                                    break
                                                                arg4 = 0
                                                                v6 = 0
                                                                if not load32(arg2 + 20):
                                                                    break
                                                                break
                                                                break
                                                            arg0 = load32(load32(arg2 + 28) + 28)
                                                            v7 = load32(arg2 + 32)
                                                            store32(arg2 + 32, (load32(arg2 + 32) + 1))
                                                            arg0 = load8u((arg0 + v7))
                                                            store32(arg2 + 20, (arg4 + 1))
                                                            store8((load32(arg2 + 8) + arg4), arg0)
                                                            if arg0:
                                                                continue
                                                            break
                                                        while True:  # $label39
                                                            if not load32(load32(arg2 + 28) + 44):
                                                                break
                                                            arg0 = load32(arg2 + 20)
                                                            if (u32(load32(arg2 + 20)) <= u32(v6)):
                                                                break
                                                            store32(v5 + 48, func43(load32(v5 + 48), (load32(arg2 + 8) + v6), (arg0 - v6)))
                                                            break
                                                        store32(arg2 + 32, 0)
                                                    store32(arg2 + 4, 91)
                                                    break
                                                while True:  # $label40
                                                    if not load32(load32(arg2 + 28) + 36):
                                                        break
                                                    v6 = load32(arg2 + 20)
                                                    while True:  # $label44
                                                        while True:  # $label41
                                                            arg4 = load32(arg2 + 20)
                                                            if (load32(arg2 + 20) != load32(arg2 + 12)):
                                                                break
                                                            while True:  # $label42
                                                                if not load32(load32(arg2 + 28) + 44):
                                                                    break
                                                                if (u32(arg4) <= u32(v6)):
                                                                    break
                                                                store32(v5 + 48, func43(load32(v5 + 48), (load32(arg2 + 8) + v6), (arg4 - v6)))
                                                                break
                                                            arg0 = load32(v5 + 28)
                                                            while True:  # $label43
                                                                arg4 = load32(arg0 + 20)
                                                                v6 = load32(v5 + 16)
                                                                arg4 = (load32(arg0 + 20) if (u32(arg4) < u32(v6)) else load32(v5 + 16))
                                                                if not (load32(arg0 + 20) if (u32(arg4) < u32(v6)) else load32(v5 + 16)):
                                                                    break
                                                                store32(v5 + 12, (load32(v5 + 12) + arg4))
                                                                store32(arg0 + 16, (load32(arg0 + 16) + arg4))
                                                                store32(v5 + 20, (load32(v5 + 20) + arg4))
                                                                store32(v5 + 16, (load32(v5 + 16) - arg4))
                                                                v6 = load32(arg0 + 20)
                                                                store32(arg0 + 20, (load32(arg0 + 20) - arg4))
                                                                if (arg4 != v6):
                                                                    break
                                                                store32(arg0 + 16, load32(arg0 + 8))
                                                                break
                                                            arg4 = 0
                                                            v6 = 0
                                                            if not load32(arg2 + 20):
                                                                break
                                                            break
                                                            break
                                                        arg0 = load32(load32(arg2 + 28) + 36)
                                                        v7 = load32(arg2 + 32)
                                                        store32(arg2 + 32, (load32(arg2 + 32) + 1))
                                                        arg0 = load8u((arg0 + v7))
                                                        store32(arg2 + 20, (arg4 + 1))
                                                        store8((load32(arg2 + 8) + arg4), arg0)
                                                        if arg0:
                                                            continue
                                                        break
                                                    if not load32(load32(arg2 + 28) + 44):
                                                        break
                                                    arg0 = load32(arg2 + 20)
                                                    if (u32(load32(arg2 + 20)) <= u32(v6)):
                                                        break
                                                    store32(v5 + 48, func43(load32(v5 + 48), (load32(arg2 + 8) + v6), (arg0 - v6)))
                                                    break
                                                store32(arg2 + 4, 103)
                                                break
                                            while True:  # $label45
                                                if load32(load32(arg2 + 28) + 44):
                                                    arg4 = load32(arg2 + 20)
                                                    if (u32(load32(arg2 + 12)) < u32((load32(arg2 + 20) + 2))):
                                                        func130(v5)
                                                        if load32(arg2 + 20):
                                                            break
                                                        arg4 = 0
                                                    arg0 = load32(v5 + 48)
                                                    store32(arg2 + 20, (arg4 + 1))
                                                    store8((load32(arg2 + 8) + arg4), arg0)
                                                    arg0 = load32(v5 + 48)
                                                    arg4 = load32(arg2 + 20)
                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                    store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 8))
                                                    store32(v5 + 48, func43(0, 0, 0))
                                                store32(arg2 + 4, 113)
                                                func130(v5)
                                                if not load32(arg2 + 20):
                                                    break
                                                break
                                                break
                                            break
                                            break
                                        if load32(v5 + 4):
                                            break
                                        break
                                    if load32(arg2 + 116):
                                        break
                                    if not v9:
                                        break
                                    if (load32(arg2 + 4) == 666):
                                        break
                                    break
                                while True:  # $label48
                                    arg0 = load32(arg2 + 132)
                                    if not load32(arg2 + 132):
                                        break
                                    while True:  # $label51
                                        while True:  # $label50
                                            while True:  # $label49
                                                # br_table (load32(arg2 + 136) - 2)
                                                break
                                                break
                                            while True:  # $label54
                                                while True:  # $label53
                                                    while True:  # $label55
                                                        while True:  # $label52
                                                            if load32(arg2 + 116):
                                                                break
                                                            if load32(arg2 + 116):
                                                                break
                                                            if v9:
                                                                break
                                                            break
                                                            break
                                                        store32(arg2 + 96, 0)
                                                        arg0 = load8u((load32(arg2 + 56) + load32(arg2 + 108)))
                                                        arg4 = load32(arg2 + 5792)
                                                        store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                        store8((arg4 + load32(arg2 + 5784)), 0)
                                                        arg4 = load32(arg2 + 5792)
                                                        store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                        store8((arg4 + load32(arg2 + 5784)), 0)
                                                        arg4 = load32(arg2 + 5792)
                                                        store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                        store8((arg4 + load32(arg2 + 5784)), arg0)
                                                        arg0 = (arg2 + (arg0 << 2))
                                                        store16((arg2 + (arg0 << 2)) + 148, (load16u(arg0 + 148) + 1))
                                                        store32(arg2 + 116, (load32(arg2 + 116) - 1))
                                                        arg4 = (load32(arg2 + 108) + 1)
                                                        store32(arg2 + 108, (load32(arg2 + 108) + 1))
                                                        if (load32(arg2 + 5792) != load32(arg2 + 5796)):
                                                            continue
                                                        arg0 = load32(arg2 + 92)
                                                        if (load32(arg2 + 92) >= 0):
                                                        else:
                                                        store32(arg2 + 92, load32(arg2 + 108))
                                                        arg0 = load32(arg2)
                                                        arg4 = load32(load32(arg2) + 28)
                                                        while True:  # $label56
                                                            v6 = load32(arg4 + 20)
                                                            v7 = load32(arg0 + 16)
                                                            v6 = (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16))
                                                            if not (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16)):
                                                                break
                                                            store32(arg0 + 12, (load32(arg0 + 12) + v6))
                                                            store32(arg4 + 16, (load32(arg4 + 16) + v6))
                                                            store32(arg0 + 20, (load32(arg0 + 20) + v6))
                                                            store32(arg0 + 16, (load32(arg0 + 16) - v6))
                                                            arg0 = load32(arg4 + 20)
                                                            store32(arg4 + 20, (load32(arg4 + 20) - v6))
                                                            if (arg0 != v6):
                                                                break
                                                            store32(arg4 + 16, load32(arg4 + 8))
                                                            break
                                                        if load32(load32(arg2) + 16):
                                                            continue
                                                        break
                                                    break
                                                    break
                                                store32(arg2 + 5812, 0)
                                                if (v9 == 4):
                                                    arg0 = load32(arg2 + 92)
                                                    if (load32(arg2 + 92) >= 0):
                                                    else:
                                                    store32(arg2 + 92, load32(arg2 + 108))
                                                    arg0 = load32(arg2)
                                                    arg4 = load32(load32(arg2) + 28)
                                                    while True:  # $label57
                                                        v6 = load32(arg4 + 20)
                                                        v7 = load32(arg0 + 16)
                                                        v6 = (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16))
                                                        if not (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16)):
                                                            break
                                                        store32(arg0 + 12, (load32(arg0 + 12) + v6))
                                                        store32(arg4 + 16, (load32(arg4 + 16) + v6))
                                                        store32(arg0 + 20, (load32(arg0 + 20) + v6))
                                                        store32(arg0 + 16, (load32(arg0 + 16) - v6))
                                                        arg0 = load32(arg4 + 20)
                                                        store32(arg4 + 20, (load32(arg4 + 20) - v6))
                                                        if (arg0 != v6):
                                                            break
                                                        store32(arg4 + 16, load32(arg4 + 8))
                                                        break
                                                    break
                                                while True:  # $label58
                                                    if not load32(arg2 + 5792):
                                                        break
                                                    arg0 = load32(arg2 + 92)
                                                    if (load32(arg2 + 92) >= 0):
                                                    else:
                                                    store32(arg2 + 92, load32(arg2 + 108))
                                                    arg0 = load32(arg2)
                                                    arg4 = load32(load32(arg2) + 28)
                                                    while True:  # $label59
                                                        v6 = load32(arg4 + 20)
                                                        v7 = load32(arg0 + 16)
                                                        v6 = (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16))
                                                        if not (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16)):
                                                            break
                                                        store32(arg0 + 12, (load32(arg0 + 12) + v6))
                                                        store32(arg4 + 16, (load32(arg4 + 16) + v6))
                                                        store32(arg0 + 20, (load32(arg0 + 20) + v6))
                                                        store32(arg0 + 16, (load32(arg0 + 16) - v6))
                                                        arg0 = load32(arg4 + 20)
                                                        store32(arg4 + 20, (load32(arg4 + 20) - v6))
                                                        if (arg0 != v6):
                                                            break
                                                        store32(arg4 + 16, load32(arg4 + 8))
                                                        break
                                                    if load32(load32(arg2) + 16):
                                                        break
                                                    break
                                                    break
                                                break
                                            break
                                            break
                                        while True:  # $label62
                                            while True:  # $label75
                                                while True:  # $label74
                                                    while True:  # $label63
                                                        while True:  # $label60
                                                            v8 = load32(arg2 + 116)
                                                            if (u32(load32(arg2 + 116)) >= u32(259)):
                                                                store32(arg2 + 96, 0)
                                                                break
                                                            v8 = load32(arg2 + 116)
                                                            while True:  # $label61
                                                                if v9:
                                                                    break
                                                                if (u32(v8) >= u32(259)):
                                                                    break
                                                                break
                                                                break
                                                            if v8:
                                                                store32(arg2 + 96, 0)
                                                                if (u32(v8) > u32(2)):
                                                                    break
                                                                v12 = load32(arg2 + 108)
                                                                break
                                                            store32(arg2 + 5812, 0)
                                                            if (v9 == 4):
                                                                arg0 = load32(arg2 + 92)
                                                                if (load32(arg2 + 92) >= 0):
                                                                else:
                                                                store32(arg2 + 92, load32(arg2 + 108))
                                                                arg0 = load32(arg2)
                                                                arg4 = load32(load32(arg2) + 28)
                                                                while True:  # $label64
                                                                    v6 = load32(arg4 + 20)
                                                                    v7 = load32(arg0 + 16)
                                                                    v6 = (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16))
                                                                    if not (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16)):
                                                                        break
                                                                    store32(arg0 + 12, (load32(arg0 + 12) + v6))
                                                                    store32(arg4 + 16, (load32(arg4 + 16) + v6))
                                                                    store32(arg0 + 20, (load32(arg0 + 20) + v6))
                                                                    store32(arg0 + 16, (load32(arg0 + 16) - v6))
                                                                    arg0 = load32(arg4 + 20)
                                                                    store32(arg4 + 20, (load32(arg4 + 20) - v6))
                                                                    if (arg0 != v6):
                                                                        break
                                                                    store32(arg4 + 16, load32(arg4 + 8))
                                                                    break
                                                                break
                                                            while True:  # $label65
                                                                if not load32(arg2 + 5792):
                                                                    break
                                                                arg0 = load32(arg2 + 92)
                                                                if (load32(arg2 + 92) >= 0):
                                                                else:
                                                                store32(arg2 + 92, load32(arg2 + 108))
                                                                arg0 = load32(arg2)
                                                                arg4 = load32(load32(arg2) + 28)
                                                                while True:  # $label66
                                                                    v6 = load32(arg4 + 20)
                                                                    v7 = load32(arg0 + 16)
                                                                    v6 = (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16))
                                                                    if not (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16)):
                                                                        break
                                                                    store32(arg0 + 12, (load32(arg0 + 12) + v6))
                                                                    store32(arg4 + 16, (load32(arg4 + 16) + v6))
                                                                    store32(arg0 + 20, (load32(arg0 + 20) + v6))
                                                                    store32(arg0 + 16, (load32(arg0 + 16) - v6))
                                                                    arg0 = load32(arg4 + 20)
                                                                    store32(arg4 + 20, (load32(arg4 + 20) - v6))
                                                                    if (arg0 != v6):
                                                                        break
                                                                    store32(arg4 + 16, load32(arg4 + 8))
                                                                    break
                                                                if load32(load32(arg2) + 16):
                                                                    break
                                                                break
                                                                break
                                                            break
                                                            break
                                                        v12 = load32(arg2 + 108)
                                                        if not load32(arg2 + 108):
                                                            v12 = 0
                                                            break
                                                        v13 = (load32(arg2 + 56) + v12)
                                                        arg0 = ((load32(arg2 + 56) + v12) - 1)
                                                        v7 = load8u(((load32(arg2 + 56) + v12) - 1))
                                                        if (load8u(((load32(arg2 + 56) + v12) - 1)) != load8u(v13)):
                                                            break
                                                        if (v7 != load8u(arg0 + 2)):
                                                            break
                                                        if (v7 != load8u(arg0 + 3)):
                                                            break
                                                        v15 = (v13 + 258)
                                                        arg4 = -1
                                                        while True:  # $label71
                                                            while True:  # $label67
                                                                while True:  # $label68
                                                                    while True:  # $label69
                                                                        while True:  # $label70
                                                                            while True:  # $label72
                                                                                while True:  # $label73
                                                                                    v6 = (arg4 + v13)
                                                                                    if (v7 != load8u((arg4 + v13) + 4)):
                                                                                        break
                                                                                    if (v7 != load8u(v6 + 5)):
                                                                                        break
                                                                                    if (v7 != load8u(v6 + 6)):
                                                                                        break
                                                                                    if (v7 != load8u(v6 + 7)):
                                                                                        break
                                                                                    arg0 = (arg4 + 8)
                                                                                    v11 = (v13 + (arg4 + 8))
                                                                                    if (v7 != load8u((v13 + (arg4 + 8)))):
                                                                                        break
                                                                                    if (v7 != load8u(v6 + 9)):
                                                                                        break
                                                                                    if (load8u(v6 + 10) == v7):
                                                                                        v11 = (v6 + 11)
                                                                                        if (v7 != load8u((v6 + 11))):
                                                                                            break
                                                                                        v6 = (arg4 < 247)
                                                                                        arg4 = arg0
                                                                                        if v6:
                                                                                            continue
                                                                                        break
                                                                                    break
                                                                                v11 = (v6 + 10)
                                                                                break
                                                                                break
                                                                            v11 = (v6 + 9)
                                                                            break
                                                                            break
                                                                        v11 = (v6 + 7)
                                                                        break
                                                                        break
                                                                    v11 = (v6 + 6)
                                                                    break
                                                                    break
                                                                v11 = (v6 + 5)
                                                                break
                                                                break
                                                            v11 = (v6 + 4)
                                                            break
                                                        arg0 = ((v11 - v15) + 258)
                                                        arg0 = (((v11 - v15) + 258) if (u32(arg0) < u32(v8)) else v8)
                                                        store32(arg2 + 96, (((v11 - v15) + 258) if (u32(arg0) < u32(v8)) else v8))
                                                        if (u32(arg0) < u32(3)):
                                                            break
                                                        arg4 = load32(arg2 + 5792)
                                                        store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                        store8((arg4 + load32(arg2 + 5784)), 1)
                                                        arg4 = load32(arg2 + 5792)
                                                        store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                        store8((arg4 + load32(arg2 + 5784)), 0)
                                                        arg4 = load32(arg2 + 5792)
                                                        store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                        arg0 = (arg0 - 3)
                                                        store8((arg4 + load32(arg2 + 5784)), (arg0 - 3))
                                                        arg0 = (((load8u(((arg0 & 255) + 23984)) << 2) + arg2) + 1176)
                                                        store16((((load8u(((arg0 & 255) + 23984)) << 2) + arg2) + 1176), (load16u(arg0) + 1))
                                                        arg0 = ((arg2 + (load8u(23472) << 2)) + 2440)
                                                        store16(((arg2 + (load8u(23472) << 2)) + 2440), (load16u(arg0) + 1))
                                                        arg0 = load32(arg2 + 96)
                                                        store32(arg2 + 96, 0)
                                                        store32(arg2 + 116, (load32(arg2 + 116) - arg0))
                                                        v8 = (arg0 + load32(arg2 + 108))
                                                        store32(arg2 + 108, (arg0 + load32(arg2 + 108)))
                                                        break
                                                        break
                                                    arg0 = load8u((load32(arg2 + 56) + v12))
                                                    arg4 = load32(arg2 + 5792)
                                                    store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                    store8((arg4 + load32(arg2 + 5784)), 0)
                                                    arg4 = load32(arg2 + 5792)
                                                    store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                    store8((arg4 + load32(arg2 + 5784)), 0)
                                                    arg4 = load32(arg2 + 5792)
                                                    store32(arg2 + 5792, (load32(arg2 + 5792) + 1))
                                                    store8((arg4 + load32(arg2 + 5784)), arg0)
                                                    arg0 = (arg2 + (arg0 << 2))
                                                    store16((arg2 + (arg0 << 2)) + 148, (load16u(arg0 + 148) + 1))
                                                    store32(arg2 + 116, (load32(arg2 + 116) - 1))
                                                    v8 = (load32(arg2 + 108) + 1)
                                                    store32(arg2 + 108, (load32(arg2 + 108) + 1))
                                                    break
                                                if (load32(arg2 + 5792) != load32(arg2 + 5796)):
                                                    continue
                                                arg0 = load32(arg2 + 92)
                                                if (load32(arg2 + 92) >= 0):
                                                else:
                                                store32(arg2 + 92, load32(arg2 + 108))
                                                arg0 = load32(arg2)
                                                arg4 = load32(load32(arg2) + 28)
                                                while True:  # $label76
                                                    v6 = load32(arg4 + 20)
                                                    v7 = load32(arg0 + 16)
                                                    v6 = (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16))
                                                    if not (load32(arg4 + 20) if (u32(v6) < u32(v7)) else load32(arg0 + 16)):
                                                        break
                                                    store32(arg0 + 12, (load32(arg0 + 12) + v6))
                                                    store32(arg4 + 16, (load32(arg4 + 16) + v6))
                                                    store32(arg0 + 20, (load32(arg0 + 20) + v6))
                                                    store32(arg0 + 16, (load32(arg0 + 16) - v6))
                                                    arg0 = load32(arg4 + 20)
                                                    store32(arg4 + 20, (load32(arg4 + 20) - v6))
                                                    if (arg0 != v6):
                                                        break
                                                    store32(arg4 + 16, load32(arg4 + 8))
                                                    break
                                                if load32(load32(arg2) + 16):
                                                    continue
                                                break
                                            break
                                        break
                                        break
                                    break
                                arg0 = call_table(load32(((arg0 * 12) + 23352)))
                                if ((call_table(load32(((arg0 * 12) + 23352))) & -2) == 2):
                                    store32(arg2 + 4, 666)
                                if not (arg0 & -3):
                                    arg4 = 0
                                    if load32(v5 + 16):
                                        break
                                    break
                                if (arg0 != 1):
                                    break
                                while True:  # $label79
                                    while True:  # $label78
                                        while True:  # $label77
                                            # br_table (v9 - 1)
                                            break
                                            break
                                        arg0 = load32(arg2 + 5820)
                                        arg4 = (load16u(arg2 + 5816) | (2 << load32(arg2 + 5820)))
                                        store16(arg2 + 5816, (load16u(arg2 + 5816) | (2 << load32(arg2 + 5820))))
                                        while True:  # $label80
                                            if (arg0 >= 14):
                                                arg0 = load32(arg2 + 20)
                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                store8((arg0 + load32(arg2 + 8)), arg4)
                                                arg0 = load32(arg2 + 20)
                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                store8((arg0 + load32(arg2 + 8)), load8u((arg2 + 5817)))
                                                arg0 = load32(arg2 + 5820)
                                                arg4 = ((2 & 0xFFFFFFFF) >> (16 - load32(arg2 + 5820)))
                                                store16(arg2 + 5816, ((2 & 0xFFFFFFFF) >> (16 - load32(arg2 + 5820))))
                                                break
                                            break
                                        arg0 = (arg0 + 3)
                                        store32((arg0 - 13) + 5820, (arg0 + 3))
                                        while True:  # $label81
                                            if (arg0 >= 10):
                                                arg0 = load32(arg2 + 20)
                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                store8((arg0 + load32(arg2 + 8)), arg4)
                                                arg0 = load32(arg2 + 20)
                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                store8((arg0 + load32(arg2 + 8)), load8u((arg2 + 5817)))
                                                arg4 = 0
                                                store16(arg2 + 5816, 0)
                                                break
                                            break
                                        arg0 = (arg0 + 7)
                                        store32((load32(arg2 + 5820) - 9) + 5820, (arg0 + 7))
                                        while True:  # $label83
                                            while True:  # $label82
                                                if (arg0 == 16):
                                                    arg0 = load32(arg2 + 20)
                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                    store8((arg0 + load32(arg2 + 8)), arg4)
                                                    arg0 = load32(arg2 + 20)
                                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                    store8((arg0 + load32(arg2 + 8)), load8u((arg2 + 5817)))
                                                    store16(arg2 + 5816, 0)
                                                    break
                                                if (arg0 < 8):
                                                    break
                                                arg0 = load32(arg2 + 20)
                                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                                store8((arg0 + load32(arg2 + 8)), arg4)
                                                store16(arg2 + 5816, load8u((arg2 + 5817)))
                                                break
                                            store32(0 + 5820, (load32(arg2 + 5820) - 8))
                                            break
                                        break
                                        break
                                    if (v9 != 3):
                                        break
                                    arg0 = load32(arg2 + 68)
                                    arg4 = ((load32(arg2 + 76) << 1) - 2)
                                    store16((load32(arg2 + 68) + ((load32(arg2 + 76) << 1) - 2)), 0)
                                    func98(arg0, 0, arg4)
                                    if load32(arg2 + 116):
                                        break
                                    store32(arg2 + 5812, 0)
                                    store32(arg2 + 92, 0)
                                    store32(arg2 + 108, 0)
                                    break
                                func130(v5)
                                if load32(v5 + 16):
                                    break
                                break
                                break
                            arg4 = 0
                            if (v9 != 4):
                                break
                            arg4 = 1
                            v6 = load32(arg2 + 24)
                            if (load32(arg2 + 24) <= 0):
                                break
                            arg0 = load32(v5 + 48)
                            while True:  # $label84
                                if (v6 == 2):
                                    arg4 = load32(arg2 + 20)
                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                    store8((arg4 + load32(arg2 + 8)), arg0)
                                    arg0 = load32(v5 + 48)
                                    arg4 = load32(arg2 + 20)
                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                    store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 8))
                                    arg0 = load16u(v5 + 50)
                                    arg4 = load32(arg2 + 20)
                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                    store8((arg4 + load32(arg2 + 8)), arg0)
                                    arg0 = load8u(v5 + 51)
                                    arg4 = load32(arg2 + 20)
                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                    store8((arg4 + load32(arg2 + 8)), arg0)
                                    arg0 = load32(v5 + 8)
                                    arg4 = load32(arg2 + 20)
                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                    store8((arg4 + load32(arg2 + 8)), arg0)
                                    arg0 = load32(v5 + 8)
                                    arg4 = load32(arg2 + 20)
                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                    store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 8))
                                    arg0 = load16u(v5 + 10)
                                    arg4 = load32(arg2 + 20)
                                    store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                    store8((arg4 + load32(arg2 + 8)), arg0)
                                    arg4 = load8u(v5 + 11)
                                    break
                                arg4 = load32(arg2 + 20)
                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 24))
                                arg4 = load32(arg2 + 20)
                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                store8((arg4 + load32(arg2 + 8)), ((arg0 & 0xFFFFFFFF) >> 16))
                                arg4 = load32(v5 + 48)
                                arg0 = load32(arg2 + 20)
                                store32(arg2 + 20, (load32(arg2 + 20) + 1))
                                store8((arg0 + load32(arg2 + 8)), ((arg4 & 0xFFFFFFFF) >> 8))
                                break
                            arg0 = load32(arg2 + 20)
                            store32(arg2 + 20, (load32(arg2 + 20) + 1))
                            store8((arg0 + load32(arg2 + 8)), arg4)
                            func130(v5)
                            arg0 = load32(arg2 + 24)
                            if (load32(arg2 + 24) > 0):
                                store32(arg2 + 24, (0 - arg0))
                            arg4 = not load32(arg2 + 20)
                            break
                        break
                        break
                    store32(v5 + 24, load32(28716))
                    break
                    break
                store32(arg2 + 40, -1)
                break
            if not 0:
                v6 = load32(v10 + 24)
                continue
            break
        store32(arg1, load32(v10 + 28))
        func400((v10 + 8))
    G.global0 = (v10 - -64)
    return -5

# ----------------------------------------------------------
# $func408
# ----------------------------------------------------------
def func408(arg0, arg1):
    v8 = load16u(arg1 + 114)
    v5 = (load16u(arg1 + 114) - 1)
    v4 = ((arg0 * 404) + ENTITY_TYPES)
    v15 = load32(((arg0 * 404) + ENTITY_TYPES) + 220)
    v9 = load16u(arg1 + 112)
    arg0 = (load16u(arg1 + 112) - 1)
    v3 = ((load16u(arg1 + 112) - 1) - load32(v4 + 216))
    arg1 = ((load8u(arg1 + 122) * 404) + ENTITY_TYPES)
    v16 = load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 220)
    v10 = (load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 220) + v8)
    while True:  # $label0
        v11 = load32(arg1 + 216)
        v12 = (load32(arg1 + 216) + v9)
        if (((load32(arg1 + 216) + v9) + 1) < v9):
            break
        v7 = (v10 + 1)
        if ((v10 + 1) < v8):
            break
        while True:  # $label5
            v4 = (arg0 + 1)
            arg1 = v5
            while True:  # $label4
                while True:  # $label3
                    while True:  # $label2
                        while True:  # $label1
                            v2 = load32(9142440)
                            if (u32(load32(9142440)) <= u32(arg1)):
                                break
                            if ((arg0 | arg1) < 0):
                                break
                            if (u32(arg0) < u32(v2)):
                                break
                            break
                        arg1 = (arg1 + 1)
                        break
                        break
                    arg1 = (arg1 + 1)
                    v2 = (v2 + 2)
                    v2 = entities[load32((load32(9142840) + ((v4 + (((arg1 + 1) + (v2 + 2)) * v2)) << 2)))]
                    if (load32(38448) != load8u(entities[load32((load32(9142840) + ((v4 + (((arg1 + 1) + (v2 + 2)) * v2)) << 2)))].sub_state)):
                        break
                    v13 = func26(4)
                    v14 = (func26(4) + 4)
                    v6 = load32(v2)
                    if load32(v2):
                        store32(v2 + 4, v6)
                    store32(v2 + 8, v14)
                    store32(v2 + 4, v13)
                    store32(v2, v13)
                    # TODO: memory.fill
                    break
                if (arg1 != v7):
                    continue
                break
            arg1 = (arg0 != v12)
            arg0 = v4
            if arg1:
                continue
            break
        break
    v13 = (v11 + 1)
    while True:  # $label6
        arg0 = (v3 - 2)
        v14 = (v3 + v11)
        if ((v3 - 2) >= (v3 + v11)):
            break
        v2 = (v8 - 2)
        if ((v8 - 2) >= v10):
            break
        while True:  # $label11
            v4 = (arg0 + 1)
            arg1 = v2
            while True:  # $label10
                while True:  # $label9
                    while True:  # $label8
                        while True:  # $label7
                            v3 = load32(9142440)
                            if (u32(load32(9142440)) <= u32(arg1)):
                                break
                            if ((arg0 | arg1) < 0):
                                break
                            if (u32(arg0) < u32(v3)):
                                break
                            break
                        arg1 = (arg1 + 1)
                        break
                        break
                    arg1 = (arg1 + 1)
                    v3 = (v3 + 2)
                    v3 = entities[load32((load32(9142840) + ((v4 + (((arg1 + 1) + (v3 + 2)) * v3)) << 2)))]
                    if (load32(38448) != load8u(entities[load32((load32(9142840) + ((v4 + (((arg1 + 1) + (v3 + 2)) * v3)) << 2)))].sub_state)):
                        break
                    v6 = func26(4)
                    v17 = (func26(4) + 4)
                    v7 = load32(v3)
                    if load32(v3):
                        store32(v3 + 4, v7)
                    store32(v3 + 8, v17)
                    store32(v3 + 4, v6)
                    store32(v3, v6)
                    # TODO: memory.fill
                    break
                if (arg1 != v10):
                    continue
                break
            arg0 = v4
            if (v4 != v14):
                continue
            break
        break
    v3 = (v9 + v13)
    while True:  # $label12
        arg0 = (v9 - 2)
        if ((v9 - 2) >= v12):
            break
        arg1 = (v5 - v15)
        v4 = ((v5 - v15) - 2)
        v15 = (arg1 + v16)
        if (((v5 - v15) - 2) >= (arg1 + v16)):
            break
        while True:  # $label17
            v5 = (arg0 + 1)
            arg1 = v4
            while True:  # $label16
                while True:  # $label15
                    while True:  # $label14
                        while True:  # $label13
                            v2 = load32(9142440)
                            if (u32(load32(9142440)) <= u32(arg1)):
                                break
                            if ((arg0 | arg1) < 0):
                                break
                            if (u32(arg0) < u32(v2)):
                                break
                            break
                        arg1 = (arg1 + 1)
                        break
                        break
                    arg1 = (arg1 + 1)
                    v2 = (v2 + 2)
                    v2 = entities[load32((load32(9142840) + ((v5 + (((arg1 + 1) + (v2 + 2)) * v2)) << 2)))]
                    if (load32(38448) != load8u(entities[load32((load32(9142840) + ((v5 + (((arg1 + 1) + (v2 + 2)) * v2)) << 2)))].sub_state)):
                        break
                    v6 = func26(4)
                    v14 = (func26(4) + 4)
                    v7 = load32(v2)
                    if load32(v2):
                        store32(v2 + 4, v7)
                    store32(v2 + 8, v14)
                    store32(v2 + 4, v6)
                    store32(v2, v6)
                    # TODO: memory.fill
                    break
                if (arg1 != v15):
                    continue
                break
            arg0 = v5
            if (v5 != v12):
                continue
            break
        break
    while True:  # $label18
        arg0 = (v3 - 2)
        v6 = (v3 + v11)
        if ((v3 - 2) >= (v3 + v11)):
            break
        v4 = (v8 - 2)
        if ((v8 - 2) >= v10):
            break
        while True:  # $label23
            v5 = (arg0 + 1)
            arg1 = v4
            while True:  # $label22
                while True:  # $label21
                    while True:  # $label20
                        while True:  # $label19
                            v2 = load32(9142440)
                            if (u32(load32(9142440)) <= u32(arg1)):
                                break
                            if ((arg0 | arg1) < 0):
                                break
                            if (u32(arg0) < u32(v2)):
                                break
                            break
                        arg1 = (arg1 + 1)
                        break
                        break
                    arg1 = (arg1 + 1)
                    v2 = (v2 + 2)
                    v2 = entities[load32((load32(9142840) + ((v5 + (((arg1 + 1) + (v2 + 2)) * v2)) << 2)))]
                    if (load32(38448) != load8u(entities[load32((load32(9142840) + ((v5 + (((arg1 + 1) + (v2 + 2)) * v2)) << 2)))].sub_state)):
                        break
                    v3 = func26(4)
                    v7 = (func26(4) + 4)
                    v11 = load32(v2)
                    if load32(v2):
                        store32(v2 + 4, v11)
                    store32(v2 + 8, v7)
                    store32(v2 + 4, v3)
                    store32(v2, v3)
                    # TODO: memory.fill
                    break
                if (arg1 != v10):
                    continue
                break
            arg0 = v5
            if (v5 != v6):
                continue
            break
        break
    while True:  # $label24
        arg0 = (v9 - 2)
        if ((v9 - 2) >= v12):
            break
        arg1 = (v8 + v13)
        v4 = ((v8 + v13) - 2)
        v9 = (arg1 + v16)
        if (((v8 + v13) - 2) >= (arg1 + v16)):
            break
        while True:  # $label29
            v5 = (arg0 + 1)
            arg1 = v4
            while True:  # $label28
                while True:  # $label27
                    while True:  # $label26
                        while True:  # $label25
                            v2 = load32(9142440)
                            if (u32(load32(9142440)) <= u32(arg1)):
                                break
                            if ((arg0 | arg1) < 0):
                                break
                            if (u32(arg0) < u32(v2)):
                                break
                            break
                        arg1 = (arg1 + 1)
                        break
                        break
                    arg1 = (arg1 + 1)
                    v2 = (v2 + 2)
                    v2 = entities[load32((load32(9142840) + ((v5 + (((arg1 + 1) + (v2 + 2)) * v2)) << 2)))]
                    if (load32(38448) != load8u(entities[load32((load32(9142840) + ((v5 + (((arg1 + 1) + (v2 + 2)) * v2)) << 2)))].sub_state)):
                        break
                    v3 = func26(4)
                    v10 = (func26(4) + 4)
                    v8 = load32(v2)
                    if load32(v2):
                        store32(v2 + 4, v8)
                    store32(v2 + 8, v10)
                    store32(v2 + 4, v3)
                    store32(v2, v3)
                    # TODO: memory.fill
                    break
                if (arg1 != v9):
                    continue
                break
            arg0 = v5
            if (v5 != v12):
                continue
            break
        break

# ----------------------------------------------------------
# $func410
# ----------------------------------------------------------
def func410(arg0, arg1):
    v5 = load32(9147288)
    v3 = load32(9142440)
    # TODO: i32.div_u
    v9 = load32(9142440)
    v7 = (load32(9142440) + 1)
    v6 = ((load32(9142440) + 1) * v3)
    v10 = (v3 * v9)
    v4 = (arg0 - (v3 * v9))
    v14 = (arg0 + (((load32(9142440) + 1) * v3) + (arg0 - (v3 * v9))))
    v8 = (v9 - 1)
    v11 = ((v9 - 1) * v3)
    v15 = (v5 + (((v9 - 1) * v3) + v4))
    v12 = (u32(v3) > u32(v7))
    v16 = ((u32(v3) > u32(v7)) & ((v4 | v7) >= 0))
    arg0 = (v4 - 1)
    v17 = (v5 + (v6 + (v4 - 1)))
    v18 = (v5 + (arg0 + v10))
    v19 = (v5 + (arg0 + v11))
    v13 = (u32(v3) > u32(v8))
    v20 = ((u32(v3) > u32(v8)) & ((v4 | v8) >= 0))
    v4 = (v4 + 1)
    v11 = (v5 + (v11 + (v4 + 1)))
    v10 = (v5 + (v4 + v10))
    v21 = (v5 + (v4 + v6))
    v5 = (u32(v3) > u32(v4))
    v22 = (v12 & ((u32(v3) > u32(v4)) & ((v4 | v7) >= 0)))
    v6 = (u32(arg0) < u32(v3))
    v7 = (v12 & ((u32(arg0) < u32(v3)) & ((arg0 | v7) >= 0)))
    v3 = (u32(v3) > u32(v9))
    v12 = ((u32(v3) > u32(v9)) & (v6 & ((arg0 | v9) >= 0)))
    v6 = (v13 & (v6 & ((arg0 | v8) >= 0)))
    v8 = (v13 & (v5 & ((v4 | v8) >= 0)))
    v3 = (v3 & (v5 & ((v4 | v9) >= 0)))
    while True:  # $label8
        while True:  # $label9
            while True:  # $label1
                while True:  # $label0
                    if not v3:
                        break
                    arg0 = load32(((v2 * 36) + 51812))
                    if (load32(((v2 * 36) + 51812)) == -3):
                        break
                    if ((-1 if (arg0 >= -1) else arg0) != (-2 if (load8s(v10) == arg1) else -1)):
                        break
                    break
                while True:  # $label2
                    if not v8:
                        break
                    arg0 = load32(((v2 * 36) + 51792) + 8)
                    if (load32(((v2 * 36) + 51792) + 8) == -3):
                        break
                    if ((-1 if (arg0 >= -1) else arg0) != (-2 if (load8s(v11) == arg1) else -1)):
                        break
                    break
                while True:  # $label3
                    if not v20:
                        break
                    arg0 = load32(((v2 * 36) + 51792) + 4)
                    if (load32(((v2 * 36) + 51792) + 4) == -3):
                        break
                    if ((-1 if (arg0 >= -1) else arg0) != (-2 if (load8s(v15) == arg1) else -1)):
                        break
                    break
                while True:  # $label4
                    if not v6:
                        break
                    arg0 = load32(((v2 * 36) + 51792))
                    if (load32(((v2 * 36) + 51792)) == -3):
                        break
                    if ((-1 if (arg0 >= -1) else arg0) != (-2 if (load8s(v19) == arg1) else -1)):
                        break
                    break
                while True:  # $label5
                    if not v12:
                        break
                    arg0 = load32(((v2 * 36) + 51792) + 12)
                    if (load32(((v2 * 36) + 51792) + 12) == -3):
                        break
                    if ((-1 if (arg0 >= -1) else arg0) != (-2 if (load8s(v18) == arg1) else -1)):
                        break
                    break
                while True:  # $label6
                    if not v7:
                        break
                    arg0 = load32(((v2 * 36) + 51792) + 24)
                    if (load32(((v2 * 36) + 51792) + 24) == -3):
                        break
                    if ((-1 if (arg0 >= -1) else arg0) != (-2 if (load8s(v17) == arg1) else -1)):
                        break
                    break
                while True:  # $label7
                    if not v16:
                        break
                    arg0 = load32(((v2 * 36) + 51820))
                    if (load32(((v2 * 36) + 51820)) == -3):
                        break
                    if ((-1 if (arg0 >= -1) else arg0) != (-2 if (load8s(v14) == arg1) else -1)):
                        break
                    break
                if not v22:
                    break
                arg0 = load32(((v2 * 36) + 51824))
                if (load32(((v2 * 36) + 51824)) == -3):
                    break
                if ((-1 if (arg0 >= -1) else arg0) == (-2 if (load8s(v21) == arg1) else -1)):
                    break
                break
            v2 = (v2 + 1)
            if ((v2 + 1) != 14):
                continue
            break
        v2 = 55
        break
    return v2

# ----------------------------------------------------------
# $func411
# ----------------------------------------------------------
def func411(arg0, arg1):
    while True:  # $label0
        v3 = load32(9142840)
        arg0 = (arg0 + 1)
        v4 = (arg1 + 1)
        arg1 = (load32(9142440) + 2)
        v2 = load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))
        if (u32(load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))) < u32(3)):
            break
        v2 = entities[v2]
        if load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 264):
            if (load32(load32(GAME_STATE) + 48) != 3):
                break
        func158(v2)
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # $label1
        v2 = load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))
        if (u32(load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))) < u32(3)):
            break
        v2 = entities[v2]
        if load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 264):
            if (load32(load32(GAME_STATE) + 48) != 3):
                break
        func158(v2)
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # $label2
        arg0 = load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))
        if (u32(load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))) < u32(3)):
            break
        arg0 = entities[arg0]
        if load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 264):
            if (load32(load32(GAME_STATE) + 48) != 3):
                break
        func158(arg0)
        break

# ----------------------------------------------------------
# $jc
# Export: jc
# ----------------------------------------------------------
def jc(arg0):
    """Export: jc"""
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        if load8u(9142917):
            break
        if not load32(9299864):
            break
        while True:  # $label3
            while True:  # $label1
                v1 = load32(9299856)
                v3 = (v5 << 2)
                v4 = (load32(9299856) + (v5 << 2))
                v6 = load32((load32(9299856) + (v5 << 2)))
                if not load32((load32(9299856) + (v5 << 2))):
                    break
                if (u32(arg0) <= u32(v6)):
                    break
                store32(v4, 0)
                v1 = load32((v1 + (v3 | 4)))
                if (u32(load32((v1 + (v3 | 4)))) >= u32(2147483647)):
                    while True:  # $label2
                        v3 = entities[(v1 - 2147483647)]
                        if not load32(entities[(v1 - 2147483647)].flags):
                            break
                        v1 = load32(v3 + 40)
                        if not load32(v3 + 40):
                            break
                        if not load8u(9142906):
                            break
                        if load8u(9142916):
                            store32(v2 + 52, v1)
                            store32(v2 + 48, -65281)
                            a_b()
                            break
                        store32(v2 + 36, v1)
                        store32(v2 + 32, 13)
                        a_b()
                        break
                        break
                    v1 = load8u(v3 + 127)
                    if not load8u(v3 + 127):
                        v1 = load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 156)
                    store8(v3 + 127, v1)
                    v4 = load32(v3 + 40)
                    if not load32(v3 + 40):
                        break
                    v3 = (v1 if v1 else (load16u(v3 + 110) + 16))
                    if load8u(9142916):
                        v1 = 0
                        if (u32(v3) <= u32(15)):
                            v1 = (v3 << 4)
                            v1 = ((((load32(((v3 << 4) + 1748)) << 8) + load32((v1 + 1744))) + (load32((v1 + 1752)) << 16)) + (load32((v1 + 1756)) << 24))
                        store32(v2 + 20, v4)
                        store32(v2 + 16, v1)
                        a_b()
                        break
                    store32(v2 + 4, v4)
                    store32(v2, v3)
                    a_b()
                    break
                func38(v1)
                break
            v5 = (v5 + 2)
            if (u32((v5 + 2)) < u32(load32(9299864))):
                continue
            break
        break
    G.global0 = (v2 - -64)

# ----------------------------------------------------------
# $func413
# ----------------------------------------------------------
def func413():
    while True:  # $label0
        if not load8u(9142388):
            break
        if not load8u(9140304):
            break
        v2 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) >= u32(2)):
            v3 = load32(CURRENT_PLAYER)
            v4 = load32(PLAYERS)
            v0 = 1
            while True:  # $label2
                while True:  # $label1
                    v1 = (v4 + (v0 * 286704))
                    if not load32((v4 + (v0 * 286704)) + 284616):
                        break
                    if load32(v1 + 284632):
                        break
                    if (load32(v1 + 283908) != v3):
                        break
                    break
                v0 = (v0 + 1)
                if ((v0 + 1) != v2):
                    continue
                break
        a_b()
        func397(load32(9561744), load32(9561736), load32(9561740))
        v3 = load32(9561748)
        v1 = load32(59176)
        if (u32(load32(9561748)) < u32(load32(59176))):
            while True:  # $label3
                v1 = load32(9561704)
                if load32(9561704):
                    v0 = 0
                    v2 = load32(9561696)
                    while True:  # $label4
                        v4 = ((v0 << 2) + v2)
                        if (u32(v3) <= u32(load32(((v0 << 2) + v2) + 4))):
                            v1 = (v1 - v0)
                            break
                        v0 = (load32(v4 + 8) + v0)
                        if (u32(v1) > u32((load32(v4 + 8) + v0))):
                            continue
                        break
                v1 = 0
                break
            func71((v2 + (v0 << 2)), 0, v1, 59176, 1, 1)
        else:
        v1 = (v1 + 10)
        store32(load32(59176), (v1 + 10))
        v0 = load32(9561704)
        store32(9561716, load32(9561704))
        store32(9561712, v1)
        while True:  # $label5
            if (load32(9561700) != v0):
                v1 = load32(9561696)
                break
            v1 = (load32(9561708) + v0)
            store32(9561700, (load32(9561708) + v0))
            v2 = load32(9561696)
            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
            if v0:
                # TODO: memory.copy
            if v2:
                v0 = load32(9561704)
            store32(9561696, v1)
            break
        store32(9561704, (v0 + 1))
        store32((v1 + (v0 << 2)), 0)
        v3 = load32(59176)
        while True:  # $label6
            v0 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                v2 = v1
                break
            v2 = (load32(9561708) + v0)
            store32(9561700, (load32(9561708) + v0))
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if v0:
                # TODO: memory.copy
            store32(9561696, v2)
            v0 = load32(9561704)
            break
        store32(9561704, (v0 + 1))
        store32((v2 + (v0 << 2)), v3)
        while True:  # $label7
            v0 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                v1 = v2
                break
            v1 = (load32(9561708) + v0)
            store32(9561700, (load32(9561708) + v0))
            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
            if v0:
                # TODO: memory.copy
            store32(9561696, v1)
            v0 = load32(9561704)
            break
        store32(9561704, (v0 + 1))
        store32((v1 + (v0 << 2)), 3)
        store8(9140304, 0)
        break
    return af(v2)

# ----------------------------------------------------------
# $func414
# ----------------------------------------------------------
def func414(arg0, arg1, arg2, arg3, arg4):
    v5 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        if not arg2:
            break
        if (arg2 == arg3):
            break
        v6 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) <= u32(arg2)):
            break
        v10 = (arg4 ^ 1)
        v11 = ((arg4 ^ 1) & (arg1 != 0))
        if ((arg4 ^ 1) & (arg1 != 0)):
            if load8u((load32(9143004) + ((arg2 * v6) + arg3))):
                break
        v7 = load8u(9147210)
        v9 = (v10 & not load8u(9147210))
        if (v10 & not load8u(9147210)):
            v8 = (load32(CURRENT_PLAYER) == arg3)
        while True:  # $label1
            while True:  # $label2
                while True:  # $label3
                    # br_table (arg0 - 1)
                    break
                    break
                while True:  # $label4
                    if load32(9147132):
                        break
                    if not v7:
                        break
                    if not arg4:
                        break
                    break
                while True:  # $label5
                    arg0 = ((arg2 * v6) + arg3)
                    v6 = (((arg2 * v6) + arg3) + load32(9143012))
                    if (load8u((((arg2 * v6) + arg3) + load32(9143012))) == arg1):
                        break
                    if arg1:
                        store8(v6, 1)
                    if (arg2 == load32(CURRENT_PLAYER)):
                        func374(arg3, arg1)
                    if not arg1:
                        store8((load32(9143012) + arg0), 0)
                    if (load32(CURRENT_PLAYER) != arg2):
                        break
                    a_b()
                    break
                v6 = (918 if arg1 else 919)
                if (arg2 == load32(CURRENT_PLAYER)):
                    arg0 = players[arg3]
                    v9 = load32(players[arg3] + 284628)
                    v7 = load32(arg0 + 284616)
                    store32(v5 + 48, v6)
                    store32(v5 + 52, arg0)
                    store32(v5 + 56, (v7 if v7 else v9))
                    a_b()
                if not v8:
                    break
                while True:  # $label8
                    arg0 = arg3
                    if not arg3:
                        break
                    if (arg0 == arg2):
                        break
                    arg3 = load32(PLAYER_COUNT)
                    if (u32(load32(PLAYER_COUNT)) <= u32(arg0)):
                        break
                    if v11:
                        if load8u((load32(9143004) + ((arg0 * arg3) + arg2))):
                            break
                    while True:  # $label6
                        v7 = load8u(9147210)
                        if (not load8u(9147210) & v10):
                            v8 = (load32(CURRENT_PLAYER) == arg2)
                            break
                        v8 = 0
                        if load32(9147132):
                            break
                        if not v7:
                            break
                        if not arg4:
                            break
                        break
                    while True:  # $label7
                        arg3 = ((arg0 * arg3) + arg2)
                        v7 = (((arg0 * arg3) + arg2) + load32(9143012))
                        if (load8u((((arg0 * arg3) + arg2) + load32(9143012))) == arg1):
                            break
                        if arg1:
                            store8(v7, 1)
                        if (arg0 == load32(CURRENT_PLAYER)):
                            func374(arg2, arg1)
                        if not arg1:
                            store8((load32(9143012) + arg3), 0)
                        if (load32(CURRENT_PLAYER) != arg0):
                            break
                        a_b()
                        break
                    if (arg0 == load32(CURRENT_PLAYER)):
                        arg3 = players[arg2]
                        v9 = load32(players[arg2] + 284628)
                        v7 = load32(arg3 + 284616)
                        store32(v5 + 32, v6)
                        store32(v5 + 36, arg3)
                        store32(v5 + 40, (v7 if v7 else v9))
                        a_b()
                    arg3 = arg2
                    arg2 = arg0
                    if v8:
                        continue
                    break
                break
                break
            arg0 = load32(9143008)
            arg4 = (load32(9143008) + ((arg3 * v6) + arg2))
            if (load8u((load32(9143008) + ((arg3 * v6) + arg2))) == arg1):
                break
            if load32(9147132):
                if (load32(9142440) == 4096):
                    break
            arg4 = (arg1 != 0)
            store8(arg4, (arg1 != 0))
            if v8:
                store8((arg0 + ((arg2 * v6) + arg3)), arg4)
            if (load32(CURRENT_PLAYER) != arg2):
                break
            arg0 = players[arg3]
            arg3 = load32(players[arg3] + 284628)
            arg2 = load32(arg0 + 284616)
            store32(v5 + 16, (450 if arg1 else 532))
            store32(v5 + 20, arg0)
            store32(v5 + 24, (arg2 if arg2 else arg3))
            a_b()
            break
            break
        arg0 = (load32(9143016) + ((arg3 * v6) + arg2))
        if (load8u((load32(9143016) + ((arg3 * v6) + arg2))) == arg1):
            break
        arg4 = load32(GAME_STATE)
        if load32(load32(GAME_STATE) + 180):
            if (u32(load32(9142848)) < u32((load32(arg4 + 72) * 2400))):
                break
        if load32(9147132):
            if (load32(9142440) == 4096):
                break
        store8(arg0, arg1)
        if (v9 & (arg1 != 0)):
            arg0 = (load32(9143016) + ((arg2 * v6) + arg3))
            store8((load32(9143016) + ((arg2 * v6) + arg3)), (load8u(arg0) | arg1))
        arg0 = load32(PLAYERS)
        store8(players[arg2] + 286701, 1)
        if (load32(CURRENT_PLAYER) != arg2):
            break
        arg0 = (arg0 + (arg3 * 286704))
        arg3 = load32((arg0 + (arg3 * 286704)) + 284628)
        arg2 = load32(arg0 + 284616)
        store32(v5 + 4, arg0)
        store32(v5, arg1)
        store32(v5 + 8, (arg2 if arg2 else arg3))
        a_b()
        break
    G.global0 = (v5 - -64)

# ----------------------------------------------------------
# $func415
# ----------------------------------------------------------
def func415(arg0, arg1):
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        if load8u(9142916):
            if (u32(arg0) <= u32(15)):
                arg0 = (arg0 << 4)
                v3 = ((((load32(((arg0 << 4) + 1748)) << 8) + load32((arg0 + 1744))) + (load32((arg0 + 1752)) << 16)) + (load32((arg0 + 1756)) << 24))
            store32(v2 + 20, arg1)
            store32(v2 + 16, v3)
            a_b()
            break
        store32(v2 + 4, arg1)
        store32(v2, arg0)
        a_b()
        break
    G.global0 = (v2 + 32)

# ----------------------------------------------------------
# $func416
# ----------------------------------------------------------
def func416(arg0, arg1, arg2, arg3):
    v7 = (load32(PLAYER_COUNT) * arg2)
    v20 = load32(9142440)
    v11 = (load32(9142440) + 2)
    v22 = ((load32(9142440) + 2) << 1)
    v13 = load32(38564)
    v14 = load32(38620)
    v15 = load32(38560)
    v8 = load32(9143004)
    v16 = load32(38500)
    v17 = load32(ENTITIES)
    v18 = load32(9142840)
    arg2 = 0
    while True:  # $label3
        while True:  # $label7
            while True:  # $label0
                v21 = arg2
                v5 = (arg2 << 2)
                arg2 = (load32((((arg2 << 2) | 4) + 8611904)) + arg1)
                if (u32(v20) <= u32((load32((((arg2 << 2) | 4) + 8611904)) + arg1))):
                    break
                v5 = (load32((v5 + 8611904)) + arg0)
                if (u32(v20) <= u32((load32((v5 + 8611904)) + arg0))):
                    break
                if ((arg2 | v5) < 0):
                    break
                while True:  # $label1
                    v9 = (v5 + 1)
                    v12 = (arg2 + 1)
                    arg2 = load32((v18 + (((v5 + 1) + ((arg2 + 1) * v11)) << 2)))
                    if (u32(load32((v18 + (((v5 + 1) + ((arg2 + 1) * v11)) << 2)))) < u32(3)):
                        break
                    v4 = (v17 + (arg2 * 132))
                    v6 = load8u((v17 + (arg2 * 132)) + 122)
                    v10 = ((load8u((v17 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES)
                    if not load32(((load8u((v17 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES) + 316):
                        break
                    if (v6 == v16):
                        break
                    v5 = load16u(v4 + 110)
                    while True:  # $label2
                        v19 = load16u(v4 + 120)
                        if load16u(v4 + 120):
                        else:
                        if not load8u(((v19 if load8u((v8 + (v5 + v7))) else v5) + (v5 + v7))):
                            if (load8u(v4 + 127) != 6):
                                break
                            if not load8u(v4 + 128):
                                break
                            break
                        if load8u(v4 + 128):
                            break
                        break
                    if (load8u(v4 + 125) == 10):
                        break
                    if (load8u(v4 + 126) == 2):
                        break
                    if (load32(v4 + 64) == -1):
                        break
                    if (load32(v10 + 264) == 2):
                        break
                    if (load32(v10 + 188) != 55):
                        break
                    if (v6 == v15):
                        break
                    if (v6 == v14):
                        break
                    if (v6 == v13):
                        break
                    if ((arg3 == -1) | (arg3 == v6)):
                        break
                    break
                while True:  # $label4
                    arg2 = load32((v18 + ((v9 + ((v11 + v12) * v11)) << 2)))
                    if (u32(load32((v18 + ((v9 + ((v11 + v12) * v11)) << 2)))) < u32(3)):
                        break
                    v4 = (v17 + (arg2 * 132))
                    v6 = load8u((v17 + (arg2 * 132)) + 122)
                    v10 = ((load8u((v17 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES)
                    if not load32(((load8u((v17 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES) + 316):
                        break
                    if (v6 == v16):
                        break
                    v5 = load16u(v4 + 110)
                    while True:  # $label5
                        v19 = load16u(v4 + 120)
                        if load16u(v4 + 120):
                        else:
                        if load8u(((v19 if load8u((v8 + (v5 + v7))) else v5) + (v5 + v7))):
                            if not load8u(v4 + 128):
                                break
                            break
                        if (load8u(v4 + 127) != 6):
                            break
                        if load8u(v4 + 128):
                            break
                        break
                    if (load8u(v4 + 125) == 10):
                        break
                    if (load8u(v4 + 126) == 2):
                        break
                    if (load32(v4 + 64) == -1):
                        break
                    if (load32(v10 + 264) == 2):
                        break
                    if (load32(v10 + 188) != 55):
                        break
                    if (v6 == v15):
                        break
                    if (v6 == v14):
                        break
                    if (v6 == v13):
                        break
                    if ((arg3 == -1) | (arg3 == v6)):
                        break
                    break
                arg2 = load32((v18 + ((v9 + ((v12 + v22) * v11)) << 2)))
                if (u32(load32((v18 + ((v9 + ((v12 + v22) * v11)) << 2)))) < u32(3)):
                    break
                v5 = (v17 + (arg2 * 132))
                v4 = load8u((v17 + (arg2 * 132)) + 122)
                v9 = ((load8u((v17 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES)
                if not load32(((load8u((v17 + (arg2 * 132)) + 122) * 404) + ENTITY_TYPES) + 316):
                    break
                if (v4 == v16):
                    break
                v6 = load16u(v5 + 110)
                while True:  # $label6
                    v12 = load16u(v5 + 120)
                    if load16u(v5 + 120):
                    else:
                    if load8u(((v12 if load8u((v8 + (v6 + v7))) else v6) + (v6 + v7))):
                        if not load8u(v5 + 128):
                            break
                        break
                    if (load8u(v5 + 127) != 6):
                        break
                    if load8u(v5 + 128):
                        break
                    break
                if (load8u(v5 + 125) == 10):
                    break
                if (load8u(v5 + 126) == 2):
                    break
                if (load32(v5 + 64) == -1):
                    break
                if (load32(v9 + 264) == 2):
                    break
                if (load32(v9 + 188) != 55):
                    break
                if (v4 == v15):
                    break
                if (v4 == v14):
                    break
                if (v4 == v13):
                    break
                if ((arg3 == -1) | (arg3 == v4)):
                    break
                break
            arg2 = (v21 + 2)
            if (u32(v21) < u32(1678)):
                continue
            break
        arg2 = 0
        break
    return arg2

# ----------------------------------------------------------
# $func417
# ----------------------------------------------------------
def func417(arg0, arg1, arg2):
    while True:  # $label0
        if not arg0:
            break
        if not arg1:
            break
        v4 = load32(PLAYERS)
        v5 = load16u(entities[load32(arg1)] + 110)
        v13 = players[load16u(entities[load32(arg1)] + 110)]
        v9 = load32(arg0 + 8)
        v6 = load32(arg0)
        arg0 = load32(arg0 + 4)
        if (load32(arg0 + 4) == -1):
            if not arg2:
                break
            while True:  # $label1
                v3 = (v3 + 1)
                if ((v3 + 1) != arg2):
                    continue
                break
            break
        v17 = (1 if (u32(arg0) > u32(100)) else arg0)
        if not (1 if (u32(arg0) > u32(100)) else arg0):
            break
        if not arg2:
            break
        v18 = (-2147483647 if v9 else 2147483647)
        v19 = ((v4 + (v5 * 286704)) + 281796)
        while True:  # $label12
            v15 = load32(ENTITIES)
            v11 = 0
            v5 = 0
            arg0 = v18
            while True:  # $label11
                while True:  # $label8
                    while True:  # $label4
                        while True:  # $label2
                            while True:  # $label3
                                v12 = (v15 + (load32((arg1 + (v11 << 2))) * 132))
                                v4 = load8u((v15 + (load32((arg1 + (v11 << 2))) * 132)) + 125)
                                # br_table load8u((v15 + (load32((arg1 + (v11 << 2))) * 132)) + 125)
                                break
                                break
                            if ((v4 & 254) == 6):
                                break
                            # br_table (v4 - 4)
                            break
                            break
                        while True:  # $label5
                            v3 = load32(v19)
                            if not load32(v19):
                                break
                            v8 = load32(v3 + 8)
                            if not load32(v3 + 8):
                                break
                            v4 = load32(v12 + 28)
                            v7 = load32(v3)
                            v3 = 0
                            while True:  # $label7
                                while True:  # $label6
                                    v10 = (v3 << 2)
                                    if (v4 == load32((v7 + (v3 << 2)))):
                                        if (load32((v7 + (v10 | 4))) == v6):
                                            break
                                    v3 = (v3 + 2)
                                    if (u32(v8) > u32((v3 + 2))):
                                        continue
                                    break
                                    break
                                break
                            v5 = v4
                            break
                            break
                        v4 = 0
                        while True:  # $label9
                            v3 = load32(v12 + 20)
                            if not load32(v12 + 20):
                                break
                            v7 = load32(v3 + 8)
                            if not load32(v3 + 8):
                                break
                            v8 = load32(v3)
                            v3 = 0
                            if (v7 != 1):
                                v20 = (v7 & -2)
                                v10 = 0
                                while True:  # $label10
                                    v21 = (v3 << 2)
                                    v16 = load32((v8 + (v3 << 2)))
                                    v4 = load32((v8 + (v21 | 4)))
                                    v4 = ((v4 + (((load32((v8 + (v3 << 2))) - 2147483647) if (u32(v16) > u32(2147483646)) else v16) == v6)) + (((load32((v8 + (v21 | 4))) - 2147483647) if (u32(v4) > u32(2147483646)) else v4) == v6))
                                    v3 = (v3 + 2)
                                    v10 = (v10 + 2)
                                    if ((v10 + 2) != v20):
                                        continue
                                    break
                            if not (v7 & 1):
                                break
                            v3 = load32((v8 + (v3 << 2)))
                            v4 = (v4 + (((load32((v8 + (v3 << 2))) - 2147483647) if (u32(v3) > u32(2147483646)) else v3) == v6))
                            break
                        if ((arg0 >= v4) if v9 else (arg0 <= v4)):
                            break
                        v5 = load32(v12 + 28)
                        arg0 = v4
                        break
                    v11 = (v11 + 1)
                    if ((v11 + 1) != arg2):
                        continue
                    break
                break
            if not v5:
                break
            v14 = (v14 + 1)
            if ((v14 + 1) != v17):
                continue
            break
        break

# ----------------------------------------------------------
# $func418
# ----------------------------------------------------------
def func418(arg0, arg1):
    v10 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v2 = load32(ENTITIES)
        arg1 = entities[arg0]
        v3 = load32(entities[arg0].z)
        if not load32(entities[arg0].z):
            break
        if not load32(v3 + 8):
            break
        v4 = load16u(arg1 + 110)
        v6 = load32(PLAYERS)
        while True:  # $label6
            while True:  # $label7
                v8 = load32(load32(v3))
                v11 = ((load32(load32(v3)) - 2147483647) if (u32(v8) > u32(2147483646)) else v8)
                v9 = ((((load32(load32(v3)) - 2147483647) if (u32(v8) > u32(2147483646)) else v8) * 404) + ENTITY_TYPES)
                if (load32(((((load32(load32(v3)) - 2147483647) if (u32(v8) > u32(2147483646)) else v8) * 404) + ENTITY_TYPES) + 264) != 3):
                    while True:  # $label1
                        if not load32(v9 + 280):
                            break
                        while True:  # $label3
                            while True:  # $label2
                                v3 = (v6 + (v4 * 286704))
                                v5 = (load32((v6 + (v4 * 286704)) + 283976) + 1)
                                if (u32((load32((v6 + (v4 * 286704)) + 283976) + 1)) > u32((load32((v3 + 284136)) + load32(v3 + 283980)))):
                                    arg1 = 57101
                                    if (load32(v3 + 283908) == load32(CURRENT_PLAYER)):
                                        break
                                    break
                                if (u32(v5) <= u32(load32((v3 + 284000)))):
                                    break
                                arg1 = 57113
                                if (load32((v6 + (v4 * 286704)) + 283908) != load32(CURRENT_PLAYER)):
                                    break
                                break
                            a_b()
                            break
                        v3 = (v2 + (arg0 * 132))
                        v11 = load32((v2 + (arg0 * 132)) + 28)
                        while True:  # $label4
                            arg0 = (v6 + (v4 * 286704))
                            v2 = load32((v6 + (v4 * 286704)) + 281788)
                            if not load32((v6 + (v4 * 286704)) + 281788):
                                arg1 = func26(16)
                                store32(func26(16) + 4, 20)
                                store32(arg1, func26(80))
                                store64(arg1 + 8, 85899345920)
                                store32(arg0 + 281788, arg1)
                                v4 = (arg1 + 8)
                                arg0 = 0
                                arg1 = load32(arg1)
                                break
                            v4 = (v2 + 8)
                            arg1 = load32(v2 + 8)
                            arg0 = load32(v2 + 4)
                            if (load32(v2 + 8) != load32(v2 + 4)):
                                arg0 = arg1
                                arg1 = load32(v2)
                                break
                            arg1 = (load32(v2 + 12) + arg0)
                            store32(v2 + 4, (load32(v2 + 12) + arg0))
                            v6 = load32(v2)
                            arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                            if arg0:
                                # TODO: memory.copy
                            if v6:
                                arg0 = load32(v2 + 8)
                            store32(v2, arg1)
                            break
                        store32(v4, (arg0 + 1))
                        store32((arg1 + (arg0 << 2)), v11)
                        arg0 = load32(v3 + 44)
                        if load32(v3 + 44):
                            store32((load32(9215884) + (arg0 << 4)), 0)
                        store32(v3 + 44, 0)
                        store8(v3 + 125, 7)
                        break
                        break
                    while True:  # $label5
                        v3 = (v2 + (arg0 * 132))
                        v5 = (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264) == 1)
                        v7 = (load16u((v2 + (arg0 * 132)) + 118) if (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264) == 1) else 0)
                        v3 = (load16u(v3 + 116) if v5 else 0)
                        if ((load16u((v2 + (arg0 * 132)) + 118) if (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264) == 1) else 0) | (load16u(v3 + 116) if v5 else 0)):
                            if func337((v10 + 12), (v10 + 8), arg1, v9, v3, v7):
                                break
                            break
                        if not func338((v10 + 12), (v10 + 8), arg1, v9):
                            break
                        break
                    arg1 = (((v6 + (v4 * 286704)) + (v11 << 2)) + 282828)
                    store32((((v6 + (v4 * 286704)) + (v11 << 2)) + 282828), (load32(arg1) - 1))
                    v2 = (arg0 * 132)
                    v9 = func34(v11, load16u(((arg0 * 132) + load32(ENTITIES)) + 110), load32(v10 + 12), load32(v10 + 8), 0, 1)
                    if not func34(v11, load16u(((arg0 * 132) + load32(ENTITIES)) + 110), load32(v10 + 12), load32(v10 + 8), 0, 1):
                        break
                    while True:  # $label10
                        arg1 = load32(ENTITIES)
                        v3 = load32((v2 + load32(ENTITIES)) + 28)
                        while True:  # $label8
                            v2 = load32(9215928)
                            if not load32(9215928):
                                break
                            v5 = load32(v2 + 8)
                            if not load32(v2 + 8):
                                break
                            v7 = load32(v2)
                            v2 = 0
                            while True:  # $label9
                                if (v3 != load32((arg1 + (load32((v7 + (v2 << 2))) * 132)) + 28)):
                                    v2 = (v2 + 1)
                                    if (v5 != (v2 + 1)):
                                        continue
                                    break
                                break
                            break
                            break
                        while True:  # $label11
                            v2 = load32(9215932)
                            if not load32(9215932):
                                break
                            v5 = load32(v2 + 8)
                            if not load32(v2 + 8):
                                break
                            v7 = load32(v2)
                            v2 = 0
                            while True:  # $label12
                                if (v3 == load32((arg1 + (load32((v7 + (v2 << 2))) * 132)) + 28)):
                                    break
                                v2 = (v2 + 1)
                                if ((v2 + 1) != v5):
                                    continue
                                break
                            break
                        while True:  # $label13
                            v2 = load32(9215936)
                            if not load32(9215936):
                                break
                            v5 = load32(v2 + 8)
                            if not load32(v2 + 8):
                                break
                            v7 = load32(v2)
                            v2 = 0
                            while True:  # $label14
                                if (v3 == load32((arg1 + (load32((v7 + (v2 << 2))) * 132)) + 28)):
                                    break
                                v2 = (v2 + 1)
                                if ((v2 + 1) != v5):
                                    continue
                                break
                            break
                        while True:  # $label15
                            v2 = load32(9215940)
                            if not load32(9215940):
                                break
                            v5 = load32(v2 + 8)
                            if not load32(v2 + 8):
                                break
                            v7 = load32(v2)
                            v2 = 0
                            while True:  # $label16
                                if (v3 == load32((arg1 + (load32((v7 + (v2 << 2))) * 132)) + 28)):
                                    break
                                v2 = (v2 + 1)
                                if ((v2 + 1) != v5):
                                    continue
                                break
                            break
                        break
                    v2 = 0
                    if (u32(0) >= u32(6)):
                        func105(load32(((v2 << 2) + 9215904)), v9)
                        arg1 = load32(ENTITIES)
                    v2 = (arg0 * 132)
                    if (load32(CURRENT_PLAYER) == load16u((arg1 + (arg0 * 132)) + 110)):
                        store32(v10, load32(39236))
                        a_b()
                    else:
                    func69((arg1 + v2), v9)
                    break
                func238(v11, v4, load32((v2 + (arg0 * 132)) + 28))
                break
            v3 = 0
            v7 = load32(ENTITIES)
            v9 = entities[arg0]
            v2 = load32(entities[arg0].z)
            arg1 = (load32(v2 + 8) - 1)
            store32(load32(entities[arg0].z) + 8, (load32(v2 + 8) - 1))
            if arg1:
                v5 = load32(v2)
                arg1 = 0
                while True:  # $label17
                    arg1 = (arg1 + 1)
                    store32((v5 + (arg1 << 2)), load32((v5 + ((arg1 + 1) << 2))))
                    v3 = load32(v2 + 8)
                    if (u32(arg1) < u32(load32(v2 + 8))):
                        continue
                    break
            while True:  # $label18
                if (u32(v8) < u32(2147483647)):
                    break
                while True:  # $label19
                    v5 = load32(((v11 * 404) + ENTITY_TYPES) + 180)
                    if not load8u(load32(((v11 * 404) + ENTITY_TYPES) + 180) + 23):
                        break
                    arg1 = load32(v5 + 4)
                    if (load32(((load32(v5 + 4) * 404) + ENTITY_TYPES) + 264) != 3):
                        break
                    if load32((((v6 + (v4 * 286704)) + (arg1 << 2)) + 281808)):
                        break
                    break
                v15 = load32(v5 + 68)
                if load32(v5 + 68):
                    arg1 = 0
                    v8 = 1
                    v16 = (v6 + (v4 * 286704))
                    v6 = 0
                    v4 = 0
                    while True:  # $label22
                        v12 = load32((v5 + (arg1 << 2)) + 28)
                        v13 = load32(((load32((v5 + (arg1 << 2)) + 28) * 404) + ENTITY_TYPES) + 264)
                        v14 = (load32(((load32((v5 + (arg1 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) == 1)
                        while True:  # $label21
                            while True:  # $label20
                                v12 = load32(((v16 + (v12 << 2)) + 281808))
                                if (load32(((v16 + (v12 << 2)) + 281808)) == 1):
                                    break
                                v8 = ((v13 != 3) & v8)
                                if v12:
                                    break
                                v8 = ((v13 != 0) & v8)
                                break
                                break
                            v4 = (v4 | v14)
                            break
                        v6 = (v6 | v14)
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != v15):
                            continue
                        break
                    if not (((v4 & v8) if (v6 & 1) else v8) & 1):
                        break
                v6 = (v11 + 2147483647)
                while True:  # $label23
                    if (load32(v2 + 4) != v3):
                        arg1 = load32(v2)
                        break
                    arg1 = (load32(v2 + 12) + v3)
                    store32(v2 + 4, (load32(v2 + 12) + v3))
                    v4 = load32(v2)
                    arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                    if v3:
                        # TODO: memory.copy
                    if v4:
                        v3 = load32(v2 + 8)
                    store32(v2, arg1)
                    break
                v4 = load32(v9 + 20)
                store32(v2 + 8, (v3 + 1))
                store32((arg1 + (v3 << 2)), v6)
                v3 = load32(v4 + 8)
                break
            while True:  # $label24
                if v3:
                    func230(v9)
                    break
                func29(v9, 1)
                break
            while True:  # $label25
                arg1 = (v7 + (arg0 * 132))
                if not load32((v7 + (arg0 * 132)) + 92):
                    break
                v2 = load8u(9147141)
                if load32(9140316):
                    if (load32(9140320) != load32((v7 + (arg0 * 132)) + 28)):
                        break
                break
            if (load32(CURRENT_PLAYER) != load16u(arg1 + 110)):
                break
            arg0 = load32(((v11 * 404) + ENTITY_TYPES) + 180)
            if not load32(((v11 * 404) + ENTITY_TYPES) + 180):
                break
            break
            break
        store32((load32(9215884) + (load32((v2 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
        break
    G.global0 = (v10 + 16)
    return func53(load32(arg0 + 12))

# ----------------------------------------------------------
# $func419
# ----------------------------------------------------------
def func419(arg0, arg1):
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v5 = 1
    while True:  # $label0
        while True:  # $label5
            while True:  # $label4
                while True:  # $label3
                    while True:  # $label2
                        while True:  # $label1
                            # br_table ((arg1 - arg0) // 28)
                            break
                            break
                        arg1 = (arg1 - 28)
                        if ((load32((arg1 - 28) + 12) * load32(arg1 + 8)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
                            break
                        store32(v2 + 24, load32(arg0 + 24))
                        store64(v2 + 16, load64(arg0 + 16))
                        store64(v2 + 8, load64(arg0 + 8))
                        store64(v2, load64(arg0))
                        store32(arg0 + 24, load32(arg1 + 24))
                        store64(arg0 + 16, load64(arg1 + 16))
                        store64(arg0 + 8, load64(arg1 + 8))
                        store64(arg0, load64(arg1))
                        store32(arg1 + 24, load32(v2 + 24))
                        store64(arg1 + 16, load64(v2 + 16))
                        store64(arg1 + 8, load64(v2 + 8))
                        store64(arg1, load64(v2))
                        break
                        break
                    v3 = (arg1 - 28)
                    v4 = (load32(((arg1 - 28) + 12)) * load32(v3 + 8))
                    arg1 = (arg0 + 28)
                    v6 = (load32(arg0 + 40) * load32(arg0 + 36))
                    if ((load32(arg0 + 40) * load32(arg0 + 36)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
                        if (v4 <= v6):
                            break
                        store32(v2 + 24, load32(arg1 + 24))
                        store64(v2 + 16, load64(arg1 + 16))
                        store64(v2 + 8, load64(arg1 + 8))
                        store64(v2, load64(arg1))
                        store32(arg1 + 24, load32(v3 + 24))
                        store64(arg1 + 16, load64(v3 + 16))
                        store64(arg1 + 8, load64(v3 + 8))
                        store64(arg1, load64(v3))
                        store32(v3 + 24, load32(v2 + 24))
                        store64(v3 + 16, load64(v2 + 16))
                        store64(v3 + 8, load64(v2 + 8))
                        store64(v3, load64(v2))
                        if ((load32(arg0 + 40) * load32(arg0 + 36)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
                            break
                        store32(v2 + 24, load32(arg0 + 24))
                        store64(v2 + 16, load64(arg0 + 16))
                        store64(v2 + 8, load64(arg0 + 8))
                        store64(v2, load64(arg0))
                        store32(arg0 + 24, load32(arg1 + 24))
                        store64(arg0 + 16, load64(arg1 + 16))
                        store64(arg0 + 8, load64(arg1 + 8))
                        store64(arg0, load64(arg1))
                        store32(arg1 + 24, load32(v2 + 24))
                        store64(arg1 + 16, load64(v2 + 16))
                        store64(arg1 + 8, load64(v2 + 8))
                        store64(arg1, load64(v2))
                        break
                    if (v4 > v6):
                        store32(v2 + 24, load32(arg0 + 24))
                        store64(v2 + 16, load64(arg0 + 16))
                        store64(v2 + 8, load64(arg0 + 8))
                        store64(v2, load64(arg0))
                        store32(arg0 + 24, load32(v3 + 24))
                        store64(arg0 + 16, load64(v3 + 16))
                        store64(arg0 + 8, load64(v3 + 8))
                        store64(arg0, load64(v3))
                        store32(v3 + 24, load32(v2 + 24))
                        store64(v3 + 16, load64(v2 + 16))
                        store64(v3 + 8, load64(v2 + 8))
                        store64(v3, load64(v2))
                        break
                    store32(v2 + 24, load32(arg0 + 24))
                    store64(v2 + 16, load64(arg0 + 16))
                    store64(v2 + 8, load64(arg0 + 8))
                    store64(v2, load64(arg0))
                    store32(arg0 + 24, load32(arg1 + 24))
                    store64(arg0 + 16, load64(arg1 + 16))
                    store64(arg0 + 8, load64(arg1 + 8))
                    store64(arg0, load64(arg1))
                    store32(arg1 + 24, load32(v2 + 24))
                    store64(arg1 + 16, load64(v2 + 16))
                    store64(arg1 + 8, load64(v2 + 8))
                    store64(arg1, load64(v2))
                    if ((load32(v3 + 12) * load32(v3 + 8)) <= (load32(arg0 + 40) * load32(arg0 + 36))):
                        break
                    store32(v2 + 24, load32(arg1 + 24))
                    store64(v2 + 16, load64(arg1 + 16))
                    store64(v2 + 8, load64(arg1 + 8))
                    store64(v2, load64(arg1))
                    store32(arg1 + 24, load32(v3 + 24))
                    store64(arg1 + 16, load64(v3 + 16))
                    store64(arg1 + 8, load64(v3 + 8))
                    store64(arg1, load64(v3))
                    store32(v3 + 24, load32(v2 + 24))
                    store64(v3 + 16, load64(v2 + 16))
                    store64(v3 + 8, load64(v2 + 8))
                    store64(v3, load64(v2))
                    break
                    break
                break
                break
            break
            break
        v6 = (load32(arg0 + 68) * load32((arg0 - -64)))
        v4 = (arg0 + 28)
        v3 = (arg0 + 56)
        while True:  # $label6
            v7 = (load32(arg0 + 40) * load32(arg0 + 36))
            v8 = (load32(arg0 + 12) * load32(arg0 + 8))
            if ((load32(arg0 + 40) * load32(arg0 + 36)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
                if (v6 <= v7):
                    break
                store32(v2 + 24, load32(v4 + 24))
                store64(v2 + 16, load64(v4 + 16))
                store64(v2 + 8, load64(v4 + 8))
                store64(v2, load64(v4))
                store32(v4 + 24, load32((v3 + 24)))
                store64(v4 + 16, load64((v3 + 16)))
                store64(v4 + 8, load64((v3 + 8)))
                store64(v4, load64(v3))
                store32(v3 + 24, load32(v2 + 24))
                store64(v3 + 16, load64(v2 + 16))
                store64(v3 + 8, load64(v2 + 8))
                store64(v3, load64(v2))
                if ((load32(arg0 + 40) * load32(arg0 + 36)) <= v8):
                    break
                store32(v2 + 24, load32(arg0 + 24))
                store64(v2 + 16, load64(arg0 + 16))
                store64(v2 + 8, load64(arg0 + 8))
                store64(v2, load64(arg0))
                store32(arg0 + 24, load32(v4 + 24))
                store64(arg0 + 16, load64(v4 + 16))
                store64(arg0 + 8, load64(v4 + 8))
                store64(arg0, load64(v4))
                store32(v4 + 24, load32(v2 + 24))
                store64(v4 + 16, load64(v2 + 16))
                store64(v4 + 8, load64(v2 + 8))
                store64(v4, load64(v2))
                break
            if (v6 > v7):
                store32(v2 + 24, load32(arg0 + 24))
                store64(v2 + 16, load64(arg0 + 16))
                store64(v2 + 8, load64(arg0 + 8))
                store64(v2, load64(arg0))
                store32(arg0 + 24, load32((v3 + 24)))
                store64(arg0 + 16, load64((v3 + 16)))
                store64(arg0 + 8, load64((v3 + 8)))
                store64(arg0, load64(v3))
                store32(v3 + 24, load32(v2 + 24))
                store64(v3 + 16, load64(v2 + 16))
                store64(v3 + 8, load64(v2 + 8))
                store64(v3, load64(v2))
                break
            store32(v2 + 24, load32(arg0 + 24))
            store64(v2 + 16, load64(arg0 + 16))
            store64(v2 + 8, load64(arg0 + 8))
            store64(v2, load64(arg0))
            store32(arg0 + 24, load32(v4 + 24))
            store64(arg0 + 16, load64(v4 + 16))
            store64(arg0 + 8, load64(v4 + 8))
            store64(arg0, load64(v4))
            store32(v4 + 24, load32(v2 + 24))
            store64(v4 + 16, load64(v2 + 16))
            store64(v4 + 8, load64(v2 + 8))
            store64(v4, load64(v2))
            if (v6 <= (load32(arg0 + 40) * load32(arg0 + 36))):
                break
            store32(v2 + 24, load32(v4 + 24))
            store64(v2 + 16, load64(v4 + 16))
            store64(v2 + 8, load64(v4 + 8))
            store64(v2, load64(v4))
            store32(v4 + 24, load32((v3 + 24)))
            store64(v4 + 16, load64((v3 + 16)))
            store64(v4 + 8, load64((v3 + 8)))
            store64(v4, load64(v3))
            store32(v3 + 24, load32(v2 + 24))
            store64(v3 + 16, load64(v2 + 16))
            store64(v3 + 8, load64(v2 + 8))
            store64(v3, load64(v2))
            break
        v4 = (arg0 + 84)
        if ((arg0 + 84) == arg1):
            break
        v7 = 0
        while True:  # $label10
            while True:  # $label7
                v8 = load32(v4 + 12)
                v9 = load32(v4 + 8)
                v10 = (load32(v4 + 12) * load32(v4 + 8))
                if ((load32(v4 + 12) * load32(v4 + 8)) <= (load32(v3 + 12) * load32(v3 + 8))):
                    break
                v11 = load64(v4)
                store32(v2 + 8, load32(v4 + 24))
                store64(v2, load64(v4 + 16))
                v6 = v4
                while True:  # $label9
                    while True:  # $label8
                        v5 = v3
                        store64(v6, load64(v3))
                        store32(v6 + 24, load32(v3 + 24))
                        store64(v6 + 16, load64(v3 + 16))
                        store64(v6 + 8, load64(v3 + 8))
                        if (arg0 == v3):
                            v5 = arg0
                            break
                        v6 = v5
                        v3 = (v5 - 28)
                        if (v10 > (load32((v5 - 28) + 12) * load32(v3 + 8))):
                            continue
                        break
                    break
                store32(v5 + 12, v8)
                store32(v5 + 8, v9)
                store64(v5, v11)
                store64(v5 + 16, load64(v2))
                store32(v5 + 24, load32(v2 + 8))
                v7 = (v7 + 1)
                if ((v7 + 1) != 8):
                    break
                v5 = ((v4 + 28) == arg1)
                break
                break
            v3 = v4
            v5 = (v4 + 28)
            v4 = (v4 + 28)
            if (arg1 != v5):
                continue
            break
        v5 = 1
        break
    G.global0 = (v2 + 32)
    return v5

# ----------------------------------------------------------
# $func420
# ----------------------------------------------------------
def func420(arg0):
    v7 = load32(PLAYERS)
    store32(arg0 + 88, 0)
    v6 = load16u(arg0 + 110)
    v2 = load8u(arg0 + 122)
    v3 = ((v7 + (load16u(arg0 + 110) * 286704)) + (load8u(arg0 + 122) << 2))
    v1 = (((v7 + (load16u(arg0 + 110) * 286704)) + (load8u(arg0 + 122) << 2)) + 281808)
    v5 = load32(v1)
    v4 = (load32(v1) + 1)
    store32((((v7 + (load16u(arg0 + 110) * 286704)) + (load8u(arg0 + 122) << 2)) + 281808), (load32(v1) + 1))
    while True:  # $label0
        if load8u(9142905):
            break
        v1 = (v3 + 278576)
        store32((v3 + 278576), (load32(v1) + 1))
        v1 = (v3 + 279596)
        v3 = load32((v3 + 279596))
        if (u32(v4) <= u32(load32((v3 + 279596)))):
            break
        store32(v1, (v3 + 1))
        if v3:
            break
        while True:  # $label1
            if (load32(38468) == v2):
                break
            if (load32(38668) == v2):
                break
            if (load32(38664) == v2):
                break
            if (load32(38488) == v2):
                break
            if (load32(38848) == v2):
                break
            if (load32(38916) == v2):
                break
            if (load32(38516) == v2):
                break
            if (load32(38844) == v2):
                break
            if (load32(38912) == v2):
                break
            if (load32(38464) == v2):
                break
            if (load32(38836) == v2):
                break
            if (load32(38904) == v2):
                break
            if (load32(38484) == v2):
                break
            if (load32(38840) == v2):
                break
            if (load32(38908) == v2):
                break
            if (load32(38476) == v2):
                break
            if (load32(38820) == v2):
                break
            if (load32(38700) == v2):
                break
            if (load32(38520) == v2):
                break
            if (load32(38808) == v2):
                break
            if (load32(38884) == v2):
                break
            if (load32(38564) == v2):
                break
            if (load32(38852) != v2):
                break
            break
        store32((((v7 + (v6 * 286704)) + (v2 << 2)) + 280616), (load32(9142848) * 25))
        break
    while True:  # $label2
        if v5:
            break
        if (load32((v7 + (v6 * 286704)) + 283908) != load32(CURRENT_PLAYER)):
            break
        v9 = ((v2 * 404) + ENTITY_TYPES)
        if not load32(((v2 * 404) + ENTITY_TYPES) + 244):
            break
        while True:  # $label6
            v5 = load32((load32(v9 + 240) + (v8 << 2)))
            while True:  # $label3
                if load8u(9147141):
                    break
                v1 = 0
                v4 = load32(9671120)
                if not load32(9671120):
                    break
                while True:  # $label5
                    while True:  # $label4
                        v3 = load32(((v1 << 2) + 9263072))
                        if not load32(((v1 << 2) + 9263072)):
                            break
                        if (load32(v3 + 12) != v5):
                            break
                        if load8u(v3 + 24):
                            break
                        break
                        break
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v4):
                        continue
                    break
                break
            v8 = (v8 + 1)
            if (u32((v8 + 1)) < u32(load32(v9 + 244))):
                continue
            break
        break
    while True:  # $label7
        v1 = load32(((v2 * 404) + ENTITY_TYPES) + 176)
        if not load32(((v2 * 404) + ENTITY_TYPES) + 176):
            break
        v5 = (v7 + (v6 * 286704))
        store32((v7 + (v6 * 286704)) + 283980, (load32(v5 + 283980) + v1))
        v4 = load32(v5 + 283976)
        if (v1 > 0):
            store8(v5 + 286700, 1)
        v1 = (v5 + 281748)
        if (u32(load32((v5 + 281748))) >= u32(v4)):
            break
        store32(v1, v4)
        break
    while True:  # $label8
        if load8u(9147152):
            break
        while True:  # $label9
            v1 = load8u(arg0 + 122)
            if (load8u(arg0 + 122) == load32(38540)):
                break
            if (load32(38812) == v1):
                break
            if (load32(38888) != v1):
                break
            break
        break
    v10 = load8u(arg0 + 122)
    while True:  # $label10
        if not load32((v7 + (v6 * 286704)) + 286684):
            break
        if (v10 != load32(38512)):
            if (load32(38792) != v10):
                break
        v1 = ((v2 * 404) + ENTITY_TYPES)
        v5 = (load32(((v2 * 404) + ENTITY_TYPES) + 216) + 2)
        if ((load32(((v2 * 404) + ENTITY_TYPES) + 216) + 2) <= 0):
            break
        v4 = (load32(v1 + 220) + 2)
        if ((load32(v1 + 220) + 2) <= 0):
            break
        v14 = load32(9142440)
        v15 = (load32(9142440) + 2)
        v1 = (v7 + (v6 * 286704))
        v16 = ((v7 + (v6 * 286704)) + 283876)
        v11 = (v1 + 283872)
        v12 = load32(arg0 + 28)
        v13 = load32(9142840)
        v3 = load16u(arg0 + 112)
        v6 = (load16u(arg0 + 112) - 1)
        v1 = (v5 + (load16u(arg0 + 112) - 1))
        v2 = ((v5 + (load16u(arg0 + 112) - 1)) if (v1 > v3) else v3)
        v3 = load16u(arg0 + 114)
        v5 = (load16u(arg0 + 114) - 1)
        v1 = (v4 + (load16u(arg0 + 114) - 1))
        v7 = ((v4 + (load16u(arg0 + 114) - 1)) if (v1 > v3) else v3)
        v9 = 2147483647
        while True:  # $label13
            v3 = (v6 + 1)
            v1 = v5
            if (u32(v6) < u32(v14)):
                while True:  # $label12
                    v8 = v1
                    v1 = (v1 + 1)
                    while True:  # $label11
                        if (u32(v8) >= u32(v14)):
                            break
                        if ((v6 | v8) < 0):
                            break
                        if (load32((v13 + ((v3 + ((v1 + v15) * v15)) << 2))) == v12):
                            break
                        v4 = (v8 - load32(v16))
                        v4 = (v6 - load32(v11))
                        v4 = (((v8 - load32(v16)) * v4) + ((v6 - load32(v11)) * v4))
                        if ((((v8 - load32(v16)) * v4) + ((v6 - load32(v11)) * v4)) >= v9):
                            break
                        store16(arg0 + 118, v8)
                        store16(arg0 + 116, v6)
                        v9 = v4
                        break
                    if (v1 != v7):
                        continue
                    break
            v6 = v3
            if (v3 != v2):
                continue
            break
        break
    while True:  # $label14
        v1 = ((v10 * 404) + ENTITY_TYPES)
        if not load8u(((v10 * 404) + ENTITY_TYPES) + 377):
            break
        v11 = load32(v1 + 216)
        if (load32(v1 + 216) <= 0):
            break
        v3 = load16u(arg0 + 114)
        v12 = (load16u(arg0 + 114) + load32(v1 + 220))
        if ((load16u(arg0 + 114) + load32(v1 + 220)) <= v3):
            break
        v5 = load16u(arg0 + 112)
        v13 = (v11 + load16u(arg0 + 112))
        v2 = load32(v1 + 372)
        v7 = ((v10 * 404) + 9568308)
        v1 = v5
        while True:  # $label17
            v4 = (v1 + 1)
            v6 = (v1 - v5)
            v8 = load32(9142840)
            v1 = v3
            while True:  # $label16
                while True:  # $label15
                    if load8u((v2 + (v6 + ((v1 - v3) * v11)))):
                        v1 = (v1 + 1)
                        break
                    v9 = (load32(9142440) + 2)
                    v1 = (v1 + 1)
                    store32((v8 + (((((load32(9142440) + 2) + (v1 + 1)) * v9) + v4) << 2)), load32(v7))
                    break
                if (v1 != v12):
                    continue
                break
            v1 = v4
            if (v4 < v13):
                continue
            break
        break
    while True:  # $label18
        if (load32(CURRENT_PLAYER) != load16u(arg0 + 110)):
            break
        arg0 = load32(((v10 * 404) + ENTITY_TYPES) + 180)
        if not load32(((v10 * 404) + ENTITY_TYPES) + 180):
            break
        break

# ----------------------------------------------------------
# $func421
# ----------------------------------------------------------
def func421(arg0, arg1):
    v15 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v4 = load32(ENTITIES)
    v16 = (arg0 >= 0)
    v9 = (arg0 if (arg0 >= 0) else (arg0 - 2147483647))
    v6 = entities[(arg0 if (arg0 >= 0) else (arg0 - 2147483647))]
    v5 = load32(entities[(arg0 if (arg0 >= 0) else (arg0 - 2147483647))].target_x)
    v10 = load32(9215884)
    if not v16:
        store32((v10 + ((v5 << 4) | 8)), v9)
    while True:  # $label0
        v11 = load8u(v6 + 129)
        if (u32(((load8u(v6 + 129) - 11) & 255)) <= u32(1)):
            store32((v4 + (arg1 * 132)) + 100, 0)
            func29(v6, 1)
            store8(v6 + 129, (6 if (v11 == 12) else 0))
            break
        v21 = (v4 + (v9 * 132))
        v16 = load8u((v4 + (v9 * 132)) + 122)
        v7 = ((load8u((v4 + (v9 * 132)) + 122) * 72) + 9263856)
        v25 = load32(((load8u((v4 + (v9 * 132)) + 122) * 72) + 9263856) + 8)
        if not load32(((load8u((v4 + (v9 * 132)) + 122) * 72) + 9263856) + 8):
            v25 = load32(v7)
        v28 = (v4 + (arg1 * 132))
        v7 = load8u((v4 + (arg1 * 132)) + 122)
        v29 = load32((v10 + (v5 << 4)) + 12)
        v5 = load8u(v28 + 125)
        v10 = load32(38564)
        while True:  # $label2
            while True:  # $label1
                if (u32(load32(9142848)) >= u32((load32(load32(GAME_STATE) + 72) * 2400))):
                    break
                if (v7 == v10):
                    break
                while True:  # $label3
                    # br_table (v5 - 4)
                    break
                    break
                if (load32((v4 + (v9 * 132)) + 56) == 1):
                    if (load32(((v16 * 404) + ENTITY_TYPES) + 268) == 1):
                        break
                func29(v6, 1)
                break
                break
            v2 = (v5 == 3)
            if (v5 != 3):
                break
            if (v7 != v10):
                break
            arg0 = (v4 + (arg1 * 132))
            arg0 = func250(load16u((v4 + (arg1 * 132)) + 112), load16u(arg0 + 114), load32((v4 + (v9 * 132)) + 28))
            if func250(load16u((v4 + (arg1 * 132)) + 112), load16u(arg0 + 114), load32((v4 + (v9 * 132)) + 28)):
                break
            func29(v6, 1)
            break
            break
        while True:  # $label12
            while True:  # $label5
                while True:  # $label4
                    if v2:
                        break
                    v2 = (v4 + (arg1 * 132))
                    if load32((v4 + (arg1 * 132)) + 36):
                        break
                    if load8u(v2 + 128):
                        break
                    if (v5 == 10):
                        break
                    if not load32(((v16 * 404) + ENTITY_TYPES) + 184):
                        break
                    v5 = load32((v4 + (arg1 * 132)) + 100)
                    if not load32((v4 + (arg1 * 132)) + 100):
                        break
                    if ((v5 == v9) & (arg0 >= 0)):
                        break
                    arg0 = (v4 + (v5 * 132))
                    # TODO: i32.div_u
                    if (u32((load32((((load8u((v4 + (v5 * 132)) + 122) * 1020) + 9299904) + (v7 << 2))) * load32(arg0 + 52))) >= u32(100)):
                        break
                    if (v7 == v10):
                        break
                    break
                while True:  # $label7
                    while True:  # $label6
                        if load8u(((v7 * 404) + ENTITY_TYPES) + 380):
                            store8(v6 + 129, 9)
                            break
                        if (v11 != 9):
                            break
                        break
                    break
                v5 = func106(v6, v7, -1, -1)
                if not func106(v6, v7, -1, -1):
                    func29(v6, 1)
                    arg0 = (v4 + (arg1 * 132))
                    if (load32((v4 + (arg1 * 132)) + 100) != v9):
                        break
                    store32(arg0 + 100, 0)
                    break
                while True:  # $label8
                    v10 = load32(ENTITIES)
                    v11 = load8u(entities[v5].sub_state)
                    arg0 = ((load8u(entities[v5].sub_state) * 404) + ENTITY_TYPES)
                    if (load32(((load8u(entities[v5].sub_state) * 404) + ENTITY_TYPES) + 264) == 1):
                        break
                    v3 = load32(arg0 + 216)
                    if not load32(arg0 + 216):
                        break
                    v2 = load8u(v21 + 122)
                    arg0 = ((load8u(v21 + 122) * 404) + ENTITY_TYPES)
                    v17 = ((load8u(v21 + 122) * 404) + ENTITY_TYPES)
                    v8 = (v10 + (v5 * 132))
                    v12 = load16u((v10 + (v5 * 132)) + 114)
                    v13 = (v4 + (v9 * 132))
                    v14 = load16u((v4 + (v9 * 132)) + 114)
                    v18 = load16u(v8 + 112)
                    v20 = load16u(v13 + 112)
                    arg0 = load32(arg0 + 224)
                    v24 = (load32(arg0 + 224) * arg0)
                    v8 = 0
                    v13 = 1
                    while True:  # $label11
                        arg0 = (v14 - (v8 + v12))
                        v26 = ((v14 - (v8 + v12)) * arg0)
                        arg0 = 0
                        while True:  # $label9
                            while True:  # $label10
                                v22 = (v20 - (arg0 + v18))
                                v22 = (((v20 - (arg0 + v18)) * v22) + v26)
                                if (v24 >= ((((v20 - (arg0 + v18)) * v22) + v26) - 1)):
                                    v23 = load32(v17 + 228)
                                    if (u32(v22) >= u32((load32(v17 + 228) * v23))):
                                        break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v3):
                                    continue
                                break
                            v8 = (v8 + 1)
                            v13 = (u32((v8 + 1)) < u32(v3))
                            if (v3 != v8):
                                continue
                            break
                        break
                    if not (v13 & 1):
                        break
                    arg0 = (v4 + (arg1 * 132))
                    if (v9 == load32((v4 + (arg1 * 132)) + 100)):
                        store32(arg0 + 100, 0)
                    store32((load32(9215884) + (load32(v6 + 44) << 4)) + 12, v5)
                    break
                    break
                arg0 = (v4 + (v9 * 132))
                if (load8u((v4 + (v9 * 132)) + 125) == 1):
                    store8(arg0 + 125, 0)
                break
                break
            v2 = v16
            v11 = v7
            v10 = v4
            v5 = arg1
            break
        v17 = (v10 + (v5 * 132))
        v26 = ((v16 * 404) + ENTITY_TYPES)
        if (load32(((v16 * 404) + ENTITY_TYPES) + 264) != 1):
            arg0 = ((v7 * 404) + ENTITY_TYPES)
            v14 = load32(((v7 * 404) + ENTITY_TYPES) + 220)
            arg1 = load16u(v17 + 114)
            v3 = (load32(((v7 * 404) + ENTITY_TYPES) + 220) + load16u(v17 + 114))
            v18 = load32(arg0 + 216)
            v13 = load16u(v17 + 112)
            v12 = (load32(arg0 + 216) + load16u(v17 + 112))
            v8 = (v4 + (v9 * 132))
            arg0 = load16u((v4 + (v9 * 132)) + 114)
            while True:  # $label14
                while True:  # $label13
                    v8 = load16u(v8 + 112)
                    v20 = (u32(load16u(v8 + 112)) < u32(v13))
                    if (u32(load16u(v8 + 112)) < u32(v13)):
                        break
                    if (v8 >= v12):
                        break
                    if (u32(arg0) < u32(arg1)):
                        break
                    if (arg0 >= v3):
                        break
                    arg1 = ((v14 // 2) + arg1)
                    arg1 = (-1 if (arg0 > arg1) else (((v14 // 2) + arg1) != arg0))
                    arg0 = ((v18 // 2) + v13)
                    break
                    break
                arg1 = (1 if (u32(arg0) < u32(arg1)) else (-1 if (arg0 >= v3) else 0))
                break
            arg0 = (((1 if v20 else (-1 if (v8 >= v12) else 0)) + (arg1 * 3)) + 4)
            if (u32((((1 if v20 else (-1 if (v8 >= v12) else 0)) + (arg1 * 3)) + 4)) <= u32(8)):
            else:
            store8(load8u((arg0 + 10184)) + 124, 6)
        while True:  # $label27
            while True:  # $label28
                while True:  # $label29
                    while True:  # $label26
                        if load32(((v7 * 404) + ENTITY_TYPES) + 260):
                            v12 = (v10 + (v5 * 132))
                            v13 = load16u((v10 + (v5 * 132)) + 114)
                            v3 = load16u(v12 + 112)
                            while True:  # $label18
                                v8 = load32(((v11 * 404) + ENTITY_TYPES) + 216)
                                if load32(((v11 * 404) + ENTITY_TYPES) + 216):
                                    arg0 = ((v2 * 404) + ENTITY_TYPES)
                                    v2 = ((v2 * 404) + ENTITY_TYPES)
                                    arg1 = (v4 + (v9 * 132))
                                    v14 = load16u((v4 + (v9 * 132)) + 114)
                                    v18 = load16u(arg1 + 112)
                                    arg0 = load32(arg0 + 224)
                                    v20 = (load32(arg0 + 224) * arg0)
                                    arg1 = 0
                                    v11 = 1
                                    while True:  # $label17
                                        arg0 = (v14 - (arg1 + v13))
                                        v24 = ((v14 - (arg1 + v13)) * arg0)
                                        arg0 = 0
                                        while True:  # $label15
                                            while True:  # $label16
                                                v22 = (v18 - (arg0 + v3))
                                                v22 = (((v18 - (arg0 + v3)) * v22) + v24)
                                                if (v20 >= ((((v18 - (arg0 + v3)) * v22) + v24) - 1)):
                                                    v23 = load32(v2 + 228)
                                                    if (u32(v22) >= u32((load32(v2 + 228) * v23))):
                                                        break
                                                arg0 = (arg0 + 1)
                                                if ((arg0 + 1) != v8):
                                                    continue
                                                break
                                            arg1 = (arg1 + 1)
                                            v11 = (u32((arg1 + 1)) < u32(v8))
                                            if (arg1 != v8):
                                                continue
                                            break
                                        break
                                    arg0 = 0
                                    if (v11 & 1):
                                        break
                                if (load8u(v12 + 125) == 1):
                                    arg0 = (load8u((v10 + (v5 * 132)) + 124) << 3)
                                    v13 = (v13 - load32(((load8u((v10 + (v5 * 132)) + 124) << 3) + 8996)))
                                    v3 = (v3 - load32((arg0 + 8992)))
                                while True:  # $label19
                                    v11 = load32(((v7 * 404) + ENTITY_TYPES) + 216)
                                    if not load32(((v7 * 404) + ENTITY_TYPES) + 216):
                                        arg1 = 0
                                        break
                                    v22 = (v11 & -2)
                                    v23 = (v11 & 1)
                                    v24 = (v11 - 1)
                                    arg0 = ((v16 * 404) + ENTITY_TYPES)
                                    v12 = ((v16 * 404) + ENTITY_TYPES)
                                    arg1 = (v4 + (v9 * 132))
                                    v27 = load16u((v4 + (v9 * 132)) + 114)
                                    v14 = load16u(arg1 + 112)
                                    arg0 = load32(arg0 + 224)
                                    v18 = (load32(arg0 + 224) * arg0)
                                    arg1 = 1
                                    v8 = 0
                                    while True:  # $label22
                                        arg0 = (v27 - (v8 + v13))
                                        v20 = ((v27 - (v8 + v13)) * arg0)
                                        arg0 = 0
                                        v2 = 0
                                        if v24:
                                            while True:  # $label20
                                                v19 = (v14 - (arg0 + v3))
                                                v19 = (v20 + ((v14 - (arg0 + v3)) * v19))
                                                if (v18 >= ((v20 + ((v14 - (arg0 + v3)) * v19)) - 1)):
                                                    arg1 = load32(v12 + 228)
                                                    arg1 = (arg1 if (u32(v19) < u32((load32(v12 + 228) * arg1))) else 0)
                                                v19 = (v14 - ((arg0 | 1) + v3))
                                                v19 = (v20 + ((v14 - ((arg0 | 1) + v3)) * v19))
                                                if (v18 >= ((v20 + ((v14 - ((arg0 | 1) + v3)) * v19)) - 1)):
                                                    arg1 = load32(v12 + 228)
                                                    arg1 = (arg1 if (u32(v19) < u32((load32(v12 + 228) * arg1))) else 0)
                                                arg0 = (arg0 + 2)
                                                v2 = (v2 + 2)
                                                if ((v2 + 2) != v22):
                                                    continue
                                                break
                                        while True:  # $label21
                                            if not v23:
                                                break
                                            arg0 = (v14 - (arg0 + v3))
                                            arg0 = (v20 + ((v14 - (arg0 + v3)) * arg0))
                                            if (((v20 + ((v14 - (arg0 + v3)) * arg0)) - 1) > v18):
                                                break
                                            arg1 = load32(v12 + 228)
                                            arg1 = (arg1 if (u32(arg0) < u32((load32(v12 + 228) * arg1))) else 0)
                                            break
                                        v8 = (v8 + 1)
                                        if ((v8 + 1) != v11):
                                            continue
                                        break
                                    arg0 = 0
                                    if not (arg1 & 1):
                                        break
                                    if not v11:
                                        arg1 = 0
                                        break
                                    v22 = (v11 & -2)
                                    v23 = (v11 & 1)
                                    arg0 = ((v16 * 404) + ENTITY_TYPES)
                                    v12 = ((v16 * 404) + ENTITY_TYPES)
                                    arg1 = (v4 + (v9 * 132))
                                    v27 = load16u((v4 + (v9 * 132)) + 114)
                                    v14 = load16u(arg1 + 112)
                                    arg0 = (load32(arg0 + 224) + 1)
                                    v18 = ((load32(arg0 + 224) + 1) * arg0)
                                    arg1 = 0
                                    v8 = 0
                                    while True:  # $label25
                                        arg0 = (v27 - (v8 + v13))
                                        v20 = ((v27 - (v8 + v13)) * arg0)
                                        arg0 = 0
                                        v2 = 0
                                        if v24:
                                            while True:  # $label23
                                                v19 = (v14 - (arg0 + v3))
                                                v19 = (v20 + ((v14 - (arg0 + v3)) * v19))
                                                if (v18 >= ((v20 + ((v14 - (arg0 + v3)) * v19)) - 1)):
                                                    arg1 = load32(v12 + 228)
                                                    arg1 = (1 if (u32(v19) >= u32((load32(v12 + 228) * arg1))) else arg1)
                                                v19 = (v14 - ((arg0 | 1) + v3))
                                                v19 = (v20 + ((v14 - ((arg0 | 1) + v3)) * v19))
                                                if (v18 >= ((v20 + ((v14 - ((arg0 | 1) + v3)) * v19)) - 1)):
                                                    arg1 = load32(v12 + 228)
                                                    arg1 = (1 if (u32(v19) >= u32((load32(v12 + 228) * arg1))) else arg1)
                                                arg0 = (arg0 + 2)
                                                v2 = (v2 + 2)
                                                if ((v2 + 2) != v22):
                                                    continue
                                                break
                                        while True:  # $label24
                                            if not v23:
                                                break
                                            arg0 = (v14 - (arg0 + v3))
                                            arg0 = (v20 + ((v14 - (arg0 + v3)) * arg0))
                                            if (((v20 + ((v14 - (arg0 + v3)) * arg0)) - 1) > v18):
                                                break
                                            arg1 = load32(v12 + 228)
                                            arg1 = (1 if (u32(arg0) >= u32((load32(v12 + 228) * arg1))) else arg1)
                                            break
                                        v8 = (v8 + 1)
                                        if ((v8 + 1) != v11):
                                            continue
                                        break
                                    break
                                arg0 = (arg1 & 1)
                                if not (arg1 & 1):
                                    break
                                break
                        else:
                        v8 = 0
                        v11 = (v4 + (v9 * 132))
                        if (load8u((v4 + (v9 * 132)) + 125) == 3):
                            break
                        if not load8u(v11 + 128):
                            break
                        arg0 = (v4 + (v9 * 132))
                        store8((v4 + (v9 * 132)) + 127, 0)
                        arg1 = load32(arg0 + 40)
                        if not load32(arg0 + 40):
                            break
                        if not load8u(9142916):
                            break
                        store32(v15 + 36, arg1)
                        store32(v15 + 32, 0)
                        a_b()
                        break
                        break
                    if load32(((v16 * 404) + ENTITY_TYPES) + 260):
                        break
                    func29(v6, 1)
                    break
                    break
                arg0 = load16u(arg0 + 110)
                store32(v15 + 20, arg1)
                store32(v15 + 16, (arg0 + 16))
                a_b()
                break
            store8(v11 + 128, 0)
            break
        if (load32((v10 + (v5 * 132)) + 64) == -1):
            func29(v6, 1)
            break
        v2 = load8u(v21 + 122)
        arg0 = load32(((load8u(v21 + 122) * 404) + ENTITY_TYPES) + 96)
        arg0 = (load32(((load8u(v21 + 122) * 404) + ENTITY_TYPES) + 96) - (arg0 % 25))
        arg1 = (25 if (u32(arg0) <= u32(25)) else (load32(((load8u(v21 + 122) * 404) + ENTITY_TYPES) + 96) - (arg0 % 25)))
        arg0 = ((v8 ^ 1) & (load8u(v11 + 125) == 1))
        while True:  # $label30
            if (u32(v29) < u32(2)):
                break
            if not arg0:
                break
            v2 = ((v2 * 404) + ENTITY_TYPES)
            if (load32(((v2 * 404) + ENTITY_TYPES) + 268) != 2):
                break
            v2 = load32(v2 + 276)
            v2 = (load32(v2 + 276) if v2 else 25)
            v3 = (32000 // load32(((v16 * 404) + ENTITY_TYPES) + 260))
            arg1 = (((load32(v2 + 276) if v2 else 25) - (32000 // load32(((v16 * 404) + ENTITY_TYPES) + 260))) if (u32(v2) > u32((arg1 + v3))) else arg1)
            break
        while True:  # $label31
            if v8:
                break
            while True:  # $label32
                # br_table load32(v26 + 264)
                break
                break
            break
        if arg0:
            arg0 = (v10 + (v5 * 132))
            func63(func37(v6, v25, (0.0 if arg0 else i32(((load32(9142848) * 25) - arg1))), 0), v6, 6, load32((v10 + (v5 * 132)) + 28), arg1)
            if load32(arg0 + 100):
                break
            store32(arg0 + 100, load32((v4 + (v9 * 132)) + 28))
            break
        arg0 = (v10 + (v5 * 132))
        if not load32((v10 + (v5 * 132)) + 100):
            store32(arg0 + 100, load32((v4 + (v9 * 132)) + 28))
        while True:  # $label39
            while True:  # $label40
                while True:  # $label41
                    while True:  # $label38
                        while True:  # $label33
                            if not load8u(((load8u(v21 + 122) * 404) + ENTITY_TYPES) + 333):
                                break
                            arg0 = (v10 + (v5 * 132))
                            if (load32(38564) != load8u((v10 + (v5 * 132)) + 122)):
                                break
                            while True:  # $label34
                                # br_table (load8u(arg0 + 125) - 4)
                                break
                                break
                            while True:  # $label35
                                arg0 = func106(v6, -1, -1, -1)
                                if not func106(v6, -1, -1, -1):
                                    break
                                if (load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 264) == 1):
                                    break
                                break
                                break
                            arg0 = 0
                            while True:  # $label36
                                v12 = load32(v6 + 84)
                                arg1 = load32(PLAYERS)
                                v2 = load16u(v6 + 110)
                                v3 = players[load16u(v6 + 110)]
                                if (u32(load32(v6 + 84)) >= u32(load32((players[load16u(v6 + 110)] + 284316)))):
                                    break
                                v14 = load32((v3 + 284012))
                                v13 = 10
                                while True:  # $label37
                                    if load32(((v3 + (load32(38488) << 2)) + 281808)):
                                        break
                                    v3 = (arg1 + (v2 * 286704))
                                    if load32((((arg1 + (v2 * 286704)) + (load32(38848) << 2)) + 281808)):
                                        break
                                    v13 = (10 if load32(((v3 + (load32(38916) << 2)) + 281808)) else 0)
                                    break
                                if (u32(v12) >= u32((v13 + v14))):
                                    break
                                arg0 = (load32(((arg1 + (v2 * 286704)) + 284008)) != 0)
                                break
                            if not arg0:
                                break
                            arg0 = (v4 + (v9 * 132))
                            arg1 = (load32(arg0 + 80) + (load32(arg0 + 52) << 1))
                            store32((v4 + (v9 * 132)) + 80, (load32(arg0 + 80) + (load32(arg0 + 52) << 1)))
                            arg0 = load32(arg0 + 84)
                            if (u32(arg1) < u32(((1 if (u32(arg0) <= u32(1)) else load32(arg0 + 84)) * 100))):
                                break
                            func198(v6)
                            break
                        arg0 = (v4 + (v9 * 132))
                        v3 = ((v16 * 404) + ENTITY_TYPES)
                        v13 = load32(((v16 * 404) + ENTITY_TYPES) + 32)
                        if not load32(((v16 * 404) + ENTITY_TYPES) + 32):
                            break
                        arg1 = load16u(arg0 + 112)
                        v2 = ((load16u(arg0 + 112) << 5) - load32(9142952))
                        v2 = load16u(arg0 + 114)
                        v12 = ((load16u(arg0 + 114) << 5) - load32(9142956))
                        if ((((((load16u(arg0 + 112) << 5) - load32(9142952)) * v2) + (((load16u(arg0 + 114) << 5) - load32(9142956)) * v12)) - 1) > 9000000):
                            break
                        v12 = load32(v3 + 28)
                        v14 = load32(load32(GAME_STATE) + 48)
                        if not load32(load32(GAME_STATE) + 48):
                            break
                        if load8u(9147152):
                            break
                        v3 = load16u((load32(9147376) + (((load32(9142440) * v2) + arg1) << 1)))
                        if (v14 != 2):
                            break
                        if (u32(v3) > u32(1)):
                            break
                        break
                        break
                    arg0 = (v4 + (v9 * 132))
                    store32(v15 + 44, load16u((v4 + (v9 * 132)) + 112))
                    store32(v15 + 40, load16u(arg0 + 114))
                    while True:  # $label44
                        v16 = load32(arg0 + 28)
                        arg0 = 0
                        v11 = load32(9142440)
                        v5 = (load32(9142440) + 2)
                        v7 = load32(9142840)
                        v9 = load32(v15 + 40)
                        v8 = load32(v15 + 44)
                        while True:  # $label45
                            while True:  # $label42
                                v4 = arg0
                                arg0 = (arg0 << 2)
                                v2 = (load32((((arg0 << 2) | 4) + 8611904)) + v9)
                                if (u32(v11) <= u32((load32((((arg0 << 2) | 4) + 8611904)) + v9))):
                                    break
                                v10 = (load32((arg0 + 8611904)) + v8)
                                if (u32(v11) <= u32((load32((arg0 + 8611904)) + v8))):
                                    break
                                if ((v2 | v10) < 0):
                                    break
                                arg0 = (v10 - 1)
                                arg1 = (v2 + v5)
                                v21 = ((v2 + v5) * v5)
                                v3 = ((arg1 + 2) * v5)
                                v13 = ((arg1 + 1) * v5)
                                while True:  # $label43
                                    arg1 = (arg0 + 1)
                                    v17 = load32((v7 + ((v21 + (arg0 + 1)) << 2)))
                                    if (load32((v7 + ((v21 + (arg0 + 1)) << 2))) if (v16 != v17) else 0):
                                        break
                                    v17 = load32((v7 + ((arg1 + v13) << 2)))
                                    if (load32((v7 + ((arg1 + v13) << 2))) if (v16 != v17) else 0):
                                        break
                                    v17 = load32((v7 + ((arg1 + v3) << 2)))
                                    if (load32((v7 + ((arg1 + v3) << 2))) if (v16 != v17) else 0):
                                        break
                                    v17 = (arg0 <= v10)
                                    arg0 = arg1
                                    if v17:
                                        continue
                                    break
                                store32(v15 + 44, v10)
                                store32(v15 + 40, v2)
                                break
                                break
                            arg0 = (v4 + 2)
                            if (u32(v4) < u32(878)):
                                continue
                            break
                        break
                    if 0:
                        break
                    func29(v6, 1)
                    break
                    break
                if not v3:
                    break
                break
            store32(v15, load32((v12 + (((load32(9142848) + arg1) % v13) << 2))))
            store32(v15 + 4, arg1)
            store32(v15 + 8, v2)
            a_b()
            break
        while True:  # $label51
            v2 = ((v16 * 404) + ENTITY_TYPES)
            if load32(((v16 * 404) + ENTITY_TYPES) + 184):
                arg1 = ((v7 * 404) + ENTITY_TYPES)
                v7 = load32(((v7 * 404) + ENTITY_TYPES) + 216)
                v11 = (v10 + (v5 * 132))
                v3 = load16u((v10 + (v5 * 132)) + 112)
                v36 = ((i32(load32(v2 + 216)) * 0.5) + i32(load16u(arg0 + 112)))
                v33 = ((((i32(load32(((v7 * 404) + ENTITY_TYPES) + 216)) * 0.5) + i32(load16u((v10 + (v5 * 132)) + 112))) - ((i32(load32(v2 + 216)) * 0.5) + i32(load16u(arg0 + 112)))) * 32.0)
                arg1 = load32(arg1 + 220)
                v11 = load16u(v11 + 114)
                v37 = ((i32(load32(v2 + 220)) * 0.5) + i32(load16u(arg0 + 114)))
                v32 = ((((i32(load32(arg1 + 220)) * 0.5) + i32(load16u(v11 + 114))) - ((i32(load32(v2 + 220)) * 0.5) + i32(load16u(arg0 + 114)))) * 32.0)
                v30 = sqrt(((((((i32(load32(((v7 * 404) + ENTITY_TYPES) + 216)) * 0.5) + i32(load16u((v10 + (v5 * 132)) + 112))) - ((i32(load32(v2 + 216)) * 0.5) + i32(load16u(arg0 + 112)))) * 32.0) * v33) + (((((i32(load32(arg1 + 220)) * 0.5) + i32(load16u(v11 + 114))) - ((i32(load32(v2 + 220)) * 0.5) + i32(load16u(arg0 + 114)))) * 32.0) * v32)))
                arg0 = (((arg1 & 0xFFFFFFFF) >> 1) + v11)
                v7 = (((v7 & 0xFFFFFFFF) >> 1) + v3)
                while True:  # $label47
                    arg1 = load32(v2 + 272)
                    if not load32(v2 + 272):
                        while True:  # $label46
                            v30 = (v30 / 451.0)
                            v31 = ((v30 / 451.0) * 1000.0)
                            v31 = (((((v30 / 451.0) * 1000.0) + -25.0) if (v31 > 25.0) else v31) + 25.0)
                            if (((((((v30 / 451.0) * 1000.0) + -25.0) if (v31 > 25.0) else v31) + 25.0) < 4294967300.0) & (v31 >= 0.0)):
                                break
                            break
                        arg1 = 0
                        v31 = (v32 / v30)
                        v34 = (v33 / v30)
                        if (load32(38648) == load8u(v21 + 122)):
                            v30 = 0.0
                            break
                        v30 = 0.0
                        break
                    v31 = ((i32(arg1) * 3.14159274) / 180.0)
                    v34 = func48(((i32(arg1) * 3.14159274) / 180.0))
                    while True:  # $label48
                        v31 = func49(v31)
                        v30 = (v34 * v31)
                        v34 = (func49(v31) * sqrt(((v30 * 580.0) / ((v34 * v31) + v30))))
                        v31 = (v30 / (func49(v31) * sqrt(((v30 * 580.0) / ((v34 * v31) + v30)))))
                        v30 = (((v30 / (func49(v31) * sqrt(((v30 * 580.0) / ((v34 * v31) + v30))))) * 1000.0) + 25.0)
                        if (((((v30 / (func49(v31) * sqrt(((v30 * 580.0) / ((v34 * v31) + v30))))) * 1000.0) + 25.0) < 4294967300.0) & (v30 >= 0.0)):
                            break
                        break
                    arg1 = 0
                    v30 = func423(neg(v33), neg(v32))
                    # TODO: f64.promote_f32
                    v35 = func48(v30)
                    v30 = ((func48(v30) * -0.49999997) * 580.0)
                    v30 = (neg(((func48(v30) * -0.49999997) * 580.0)) if (v30 < 0.0) else v30)
                    # TODO: f64.promote_f32
                    # TODO: f64.promote_f32
                    # TODO: f32.demote_f64
                    v31 = ((v32 + ((v31 * (v31 * (neg(((func48(v30) * -0.49999997) * 580.0)) if (v30 < 0.0) else v30))) * -0.5)) / v31)
                    v34 = (v34 * neg(v35))
                    break
                v35 = 0.0
                while True:  # $label49
                    arg0 = load8u(v21 + 122)
                    if (load8u(v21 + 122) == load32(38644)):
                        break
                    if (load32(38568) == arg0):
                        break
                    if (load32(38576) == arg0):
                        break
                    v35 = ((func423(v32, v33) + (0.0 if load8u(9142916) else 10.0)) + 1.57079637)
                    break
                while True:  # $label50
                    if load8u(9142917):
                        break
                    if not func293(v17):
                        if not func293(v6):
                            break
                    arg0 = func244(load32(load32(v2 + 184)))
                    break
                arg0 = load32(((load8u(v21 + 122) * 404) + ENTITY_TYPES) + 276)
                if (u32(arg1) <= u32((load32(((load8u(v21 + 122) * 404) + ENTITY_TYPES) + 276) if arg0 else 25))):
                    break
                store32((load32(9215884) + (load32(v6 + 44) << 4)) + 8, (load32((v4 + (v9 * 132)) + 28) + 2147483647))
                break
            while True:  # $label52
                if (load32(38932) != load8u(v21 + 122)):
                    break
                arg1 = (v4 + (v9 * 132))
                if not load32((v4 + (v9 * 132)) + 48):
                    break
                if not load32(arg1 + 40):
                    break
                v2 = func245()
                v7 = load32(9142772)
                v13 = (load32(load32(9142772)) // 2)
                arg1 = load32(arg1 + 48)
                v12 = (load32(load32(arg1 + 48)) // 2)
                v3 = (load32(arg1 + 20) * load32(arg1 + 16))
                if (load32(arg1 + 20) * load32(arg1 + 16)):
                    v32 = i32(((load32(arg1 + 4) // v3) // 2))
                v3 = (load32(v7 + 20) * load32(v7 + 16))
                if (load32(v7 + 20) * load32(v7 + 16)):
                    v33 = i32(((load32(v7 + 4) // v3) // 2))
                v3 = load8u((v4 + (v9 * 132)) + 124)
                v14 = (load8u((v4 + (v9 * 132)) + 124) << 3)
                v18 = load32(((load8u((v4 + (v9 * 132)) + 124) << 3) + 8996))
                v30 = (i32(load16u(arg0 + 114)) * 32.0)
                v31 = (((i32(load16u(arg0 + 114)) * 32.0) + (i32(load32(9142440)) * 32.0)) + 128.0)
                while True:  # $label53
                    v32 = (0.707106769 if (v3 & 1) else 1.0)
                    v30 = (v32 * (0.707106769 if (v3 & 1) else 1.0))
                    if (abs((v32 * (0.707106769 if (v3 & 1) else 1.0))) < 2147483650.0):
                        break
                    break
                v33 = ((v30 + ((i32(v30) + i32((-2147483648 * v18))) - i32(load32(arg1 + 12)))) - v33)
                v14 = load32((v14 + 8992))
                while True:  # $label54
                    v32 = i32(v12)
                    v30 = (v32 * i32(v12))
                    if (abs((v32 * i32(v12))) < 2147483650.0):
                        break
                    break
                func254(load32(9142772), v2)
                break
            arg1 = load32((v4 + (v9 * 132)) + 52)
            while True:  # $label55
                arg0 = (v10 + (v5 * 132))
                v13 = load32(((load8u((v10 + (v5 * 132)) + 122) * 404) + ENTITY_TYPES) + 324)
                if not load32(((load8u((v10 + (v5 * 132)) + 122) * 404) + ENTITY_TYPES) + 324):
                    break
                if (load32(38676) != load8u(v21 + 122)):
                    break
                v7 = (v4 + (v9 * 132))
                v12 = load32((v4 + (v9 * 132)) + 72)
                v2 = players[load16u(v7 + 110)]
                v3 = load32((players[load16u(v7 + 110)] + 284300))
                if (u32(load32((v4 + (v9 * 132)) + 72)) < u32(load32((players[load16u(v7 + 110)] + 284300)))):
                    break
                arg1 = (v2 + 281668)
                store32((v2 + 281668), (load32(arg1) + v3))
                arg1 = load32((v2 + 284308))
                store32(v7 + 72, (v12 - v3))
                # TODO: i32.div_u
                arg1 = 100
                break
            arg1 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 400)
            if load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 400):
                v7 = load32((v10 + (v5 * 132)) + 52)
                # TODO: i32.div_u
                if (load8u(v11 + 125) == 3):
                    break
            if (load8u((v10 + (v5 * 132)) + 125) != 3):
                break
            if load8u(((load8u(v28 + 122) * 404) + ENTITY_TYPES) + 380):
                store8(v6 + 129, 9)
            arg0 = load8u(arg0 + 122)
            if (load8u(arg0 + 122) == load32(38564)):
                arg0 = (v10 + (v5 * 132))
                func117(v6, func250(load16u((v10 + (v5 * 132)) + 112), load16u(arg0 + 114), load32((v4 + (v9 * 132)) + 28)), 6)
                break
            func117(v6, func106(v6, (-1 if (load8u(v6 + 129) != 9) else arg0), -1, -1), 6)
            break
            break
        if v8:
            if load32(((v16 * 404) + ENTITY_TYPES) + 260):
                break
            func29(v6, 1)
            break
        arg0 = load32(((load8u(v21 + 122) * 404) + ENTITY_TYPES) + 276)
        # TODO: i32.div_u
        store32(load32(9142848), (load32(((load8u(v21 + 122) * 404) + ENTITY_TYPES) + 276) + (25 if arg0 else 1)))
        break
    G.global0 = (v15 + 48)
    return (load32(9215884) + (load32(v6 + 44) << 4))

# ----------------------------------------------------------
# $func422
# ----------------------------------------------------------
def func422(arg0):
    # TODO: i32.reinterpret_f32
    v2 = arg0
    v1 = (arg0 & 2147483647)
    if (u32((arg0 & 2147483647)) >= u32(1283457024)):
        # TODO: f32.copysign
        # TODO: i32.reinterpret_f32
        return (1.57079625 if (u32((arg0 & 2147483647)) > u32(2139095040)) else arg0)
    while True:  # $label1
        while True:  # $label0
            if (u32(v1) <= u32(1054867455)):
                if (u32(v1) >= u32(964689920)):
                    break
                break
            arg0 = abs(arg0)
            if (u32(v1) <= u32(1066926079)):
                if (u32(v1) <= u32(1060110335)):
                    arg0 = (((arg0 + arg0) + -1.0) / (arg0 + 2.0))
                    break
                arg0 = ((arg0 + -1.0) / (arg0 + 1.0))
                break
            if (u32(v1) <= u32(1075576831)):
                arg0 = ((arg0 + -1.5) / ((arg0 * 1.5) + 1.0))
                break
            arg0 = (-1.0 / arg0)
            break
        v3 = 3
        v5 = (arg0 * arg0)
        v4 = ((arg0 * arg0) * v5)
        v6 = (((arg0 * arg0) * v5) * ((v4 * -0.106480174) + -0.199991584))
        v4 = (v5 * ((v4 * ((v4 * 0.0616876073) + 0.142536357)) + 0.333333284))
        if (u32(v1) <= u32(1054867455)):
            return (arg0 - (arg0 * (v6 + v4)))
        v1 = (v3 << 2)
        arg0 = (loadf32(((v3 << 2) + 28896)) - (((arg0 * (v6 + v4)) - loadf32((v1 + 28912))) - arg0))
        arg0 = (neg((loadf32(((v3 << 2) + 28896)) - (((arg0 * (v6 + v4)) - loadf32((v1 + 28912))) - arg0))) if (v2 < 0) else arg0)
        break
    return arg0

# ----------------------------------------------------------
# $func423
# ----------------------------------------------------------
def func423(arg0, arg1):
    # TODO: i32.reinterpret_f32
    # TODO: i32.reinterpret_f32
    if not ((u32((arg0 & 2147483647)) < u32(2139095041)) & (u32((arg1 & 2147483647)) <= u32(2139095040))):
        return (arg0 + arg1)
    # TODO: i32.reinterpret_f32
    v2 = arg1
    if (arg1 == 1065353216):
        return func422(arg0)
    v5 = (((v2 & 0xFFFFFFFF) >> 30) & 2)
    # TODO: i32.reinterpret_f32
    v3 = arg0
    v4 = ((((v2 & 0xFFFFFFFF) >> 30) & 2) | ((arg0 & 0xFFFFFFFF) >> 31))
    while True:  # $label7
        while True:  # $label2
            v3 = (v3 & 2147483647)
            if not (v3 & 2147483647):
                while True:  # $label1
                    while True:  # $label0
                        # br_table (v4 - 2)
                        break
                        break
                    return 3.14159274
                    break
                return -3.14159274
            v2 = (v2 & 2147483647)
            if ((v2 & 2147483647) != 2139095040):
                if not v2:
                    # TODO: f32.copysign
                    return arg0
                if not ((v3 != 2139095040) & (u32((v2 + 218103808)) >= u32(v3))):
                    # TODO: f32.copysign
                    return arg0
                while True:  # $label3
                    if v5:
                        if (u32((v3 + 218103808)) < u32(v2)):
                            break
                    break
                arg0 = func422(abs((arg0 / arg1)))
                while True:  # $label6
                    while True:  # $label5
                        while True:  # $label4
                            # br_table v4
                            break
                            break
                        return neg(arg0)
                        break
                    return (3.14159274 - (arg0 + 8.74227766e-08))
                    break
                return ((arg0 + 8.74227766e-08) + -3.14159274)
            if (v3 == 2139095040):
                break
            arg0 = loadf32(((v4 << 2) + 28880))
            break
        return arg0
        break
    return loadf32(((v4 << 2) + 28864))

# ----------------------------------------------------------
# $func424
# ----------------------------------------------------------
def func424(arg0):
    # TODO: i64.reinterpret_f64
    v6 = arg0
    v4 = (i32(((arg0 & 0xFFFFFFFF) >> 32)) & 2147483647)
    if (u32((i32(((arg0 & 0xFFFFFFFF) >> 32)) & 2147483647)) >= u32(1141899264)):
        # TODO: f64.copysign
        # TODO: i64.reinterpret_f64
        return (1.5707963267948966 if (u32((arg0 & 9223372036854775807)) > u32(9218868437227405312)) else arg0)
    while True:  # $label1
        while True:  # $label0
            if (u32(v4) <= u32(1071382527)):
                if (u32(v4) >= u32(1044381696)):
                    break
                break
            arg0 = abs(arg0)
            if (u32(v4) <= u32(1072889855)):
                if (u32(v4) <= u32(1072037887)):
                    arg0 = (((arg0 + arg0) + -1.0) / (arg0 + 2.0))
                    break
                arg0 = ((arg0 + -1.0) / (arg0 + 1.0))
                break
            if (u32(v4) <= u32(1073971199)):
                arg0 = ((arg0 + -1.5) / ((arg0 * 1.5) + 1.0))
                break
            arg0 = (-1.0 / arg0)
            break
        v5 = 3
        v2 = (arg0 * arg0)
        v1 = ((arg0 * arg0) * v2)
        v3 = (((arg0 * arg0) * v2) * ((v1 * ((v1 * ((v1 * ((v1 * -0.036531572744216916) + -0.058335701337905735)) + -0.0769187620504483)) + -0.11111110405462356)) + -0.19999999999876483))
        v1 = (v2 * ((v1 * ((v1 * ((v1 * ((v1 * ((v1 * 0.016285820115365782) + 0.049768779946159324)) + 0.06661073137387531)) + 0.09090887133436507)) + 0.14285714272503466)) + 0.3333333333333293))
        if (u32(v4) <= u32(1071382527)):
            return (arg0 - (arg0 * (v3 + v1)))
        v4 = (v5 << 3)
        arg0 = (loadf64(((v5 << 3) + 28736)) - (((arg0 * (v3 + v1)) - loadf64((v4 + 28768))) - arg0))
        arg0 = (neg((loadf64(((v5 << 3) + 28736)) - (((arg0 * (v3 + v1)) - loadf64((v4 + 28768))) - arg0))) if (v6 < 0) else arg0)
        break
    return arg0

# ----------------------------------------------------------
# $func425
# ----------------------------------------------------------
def func425(arg0):
    while True:  # $label1
        while True:  # $label0
            v1 = load32(9681952)
            v2 = (arg0 + (load32(9681952) << 2))
            if (load32(((arg0 + (load32(9681952) << 2)) + 282828)) != (0 - load32((v2 + 281808)))):
                break
            v1 = load32(9681956)
            v2 = (arg0 + (load32(9681956) << 2))
            if (load32(((arg0 + (load32(9681956) << 2)) + 282828)) != (0 - load32((v2 + 281808)))):
                break
            v1 = load32(9681960)
            v2 = (arg0 + (load32(9681960) << 2))
            if (load32(((arg0 + (load32(9681960) << 2)) + 282828)) != (0 - load32((v2 + 281808)))):
                break
            v1 = load32(9681964)
            v2 = (arg0 + (load32(9681964) << 2))
            if (load32(((arg0 + (load32(9681964) << 2)) + 282828)) != (0 - load32((v2 + 281808)))):
                break
            v1 = load32(9681968)
            v2 = (arg0 + (load32(9681968) << 2))
            if (load32(((arg0 + (load32(9681968) << 2)) + 282828)) != (0 - load32((v2 + 281808)))):
                break
            v1 = load32(9681972)
            v2 = (arg0 + (load32(9681972) << 2))
            if (load32(((arg0 + (load32(9681972) << 2)) + 282828)) != (0 - load32((v2 + 281808)))):
                break
            v2 = load32(arg0 + 283960)
            break
            break
        v2 = load32(((v1 * 404) + ENTITY_TYPES) + 196)
        store32(arg0 + 283960, load32(((v1 * 404) + ENTITY_TYPES) + 196))
        break
    while True:  # $label2
        if (u32(v2) > u32(2)):
            break
        v5 = load32(9671136)
        if not load32(9671136):
            break
        v6 = ((v2 << 2) + 9681964)
        v7 = load32(arg0 + 283908)
        v1 = 0
        v3 = load32(ENTITIES)
        while True:  # $label4
            while True:  # $label5
                while True:  # $label3
                    v4 = (v3 + (v1 * 132))
                    if (v7 != load16u((v3 + (v1 * 132)) + 110)):
                        break
                    if (load32(v6) != load8u(v4 + 122)):
                        break
                    if (load8u(v4 + 125) == 3):
                        break
                    v1 = (v3 + (v1 * 132))
                    store32(arg0 + 283872, load16u((v3 + (v1 * 132)) + 112))
                    break
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v5):
                    continue
                break
            if not v5:
                break
            v4 = ((v2 << 2) + 9681952)
            v6 = load32(arg0 + 283908)
            v1 = 0
            v2 = load32(ENTITIES)
            while True:  # $label7
                while True:  # $label6
                    v3 = (v2 + (v1 * 132))
                    if (v6 != load16u((v2 + (v1 * 132)) + 110)):
                        break
                    if (load32(v4) != load8u(v3 + 122)):
                        break
                    if (load8u(v3 + 125) == 3):
                        break
                    v1 = (v2 + (v1 * 132))
                    store32(arg0 + 283872, load16u((v2 + (v1 * 132)) + 112))
                    break
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v5):
                    continue
                break
            break
            break
        v1 = (v1 + 114)
        store32(arg0 + 283876, load16u(v1))
        break

# ----------------------------------------------------------
# $func426
# ----------------------------------------------------------
def func426(arg0, arg1):
    while True:  # $label0
        v8 = load32(PLAYERS)
        v2 = players[arg0]
        v4 = load32(players[arg0] + 281792)
        if load32(players[arg0] + 281792):
            arg1 = load32(v4)
            break
        v4 = func26(16)
        store32(func26(16) + 4, 8)
        arg1 = func26(32)
        store32(v4, func26(32))
        store64(v4 + 8, 4294967296)
        store32((v2 + 281792), v4)
        break
    v9 = load64(arg1 + 8)
    store64(arg1 + 4, load64(arg1))
    v10 = load64(arg1 + 16)
    store64(arg1 + 12, v9)
    v2 = load32(arg1 + 24)
    store64(arg1 + 20, v10)
    store32(arg1 + 28, v2)
    v6 = load32(9147316)
    v2 = load32(9147320)
    while True:  # $label1
        v7 = load32(9147312)
        v3 = load32(9147324)
        v3 = ((load32(9147324) << 11) ^ v3)
        v3 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v7) ^ v3)
        v5 = ((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v7) ^ v3) & 3)
        if (u32(((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v7) ^ v3) & 3)) <= u32(1)):
            v2 = ((v2 << 11) ^ v2)
            v2 = (((((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v3)
            v5 = load32(((((((((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v3) % 18) << 2) + 9681984))
            store32(9147320, v3)
            store32(9147324, v7)
            store32(9147316, v2)
            v3 = ((v6 << 11) ^ v6)
            v2 = (((((((v6 << 11) ^ v6) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v2)
            store32(9147312, (((((((v6 << 11) ^ v6) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v2))
            v2 = (v2 % 11)
            break
        v2 = ((v2 << 11) ^ v2)
        v2 = (((((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v3)
        if (v5 == 2):
            v5 = load32((((v2 % 5) << 2) + 9682064))
            store32(9147324, v7)
            store32(9147320, v3)
            store32(9147316, v2)
            v3 = ((v6 << 11) ^ v6)
            v2 = (((((((v6 << 11) ^ v6) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v2)
            store32(9147312, (((((((v6 << 11) ^ v6) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v2))
            while True:  # $label2
                if (v5 == load32(38964)):
                    break
                if (v5 == load32(38980)):
                    break
                break
                break
            break
        v5 = load32((((v2 % 3) << 2) + 9682084))
        store32(9147320, v3)
        store32(9147324, v7)
        store32(9147316, v2)
        v3 = ((v6 << 11) ^ v6)
        v2 = (((((((v6 << 11) ^ v6) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v2)
        store32(9147312, (((((((v6 << 11) ^ v6) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v2))
        break
    v2 = ((v2 % 21) + 5)
    store32(arg1, ((v2 << 16) + v5))
    arg1 = load32(v4 + 8)
    if (u32(load32(v4 + 8)) <= u32(7)):
        store32(v4 + 8, (arg1 + 1))
    while True:  # $label3
        if (load32(9671124) != 240):
            break
        if (load32(CURRENT_PLAYER) != arg0):
            break
        func221(arg1)
        break
    return ((v2 % 71) + 30)

# ----------------------------------------------------------
# $func429
# ----------------------------------------------------------
def func429():
    while True:  # $label0
        if G.global5:
            if atomic_load(9688028):
                break
            func794()
        return
        break
    a_r(atomic_load(9688028))
    a_p()
    raise Unreachable()

# ----------------------------------------------------------
# $func430
# ----------------------------------------------------------
def func430(arg0):
    store32(arg0 + 120, func393(arg0))
    atomic_store(arg0 + 124, 1)
    atomic_store(arg0 + 128, 0)

# ----------------------------------------------------------
# $hf
# Export: hf
# ----------------------------------------------------------
def hf(arg0, param1, param2):
    """Export: hf"""
    v1 = G.global3
    store8(G.global3 + 40, 1)
    store32(v1 + 64, arg0)
    store8(v1 + 41, 0)
    # TODO: i32.atomic.rmw.sub
    arg0 = (1 - 1)
    if (1 - 1):
        v2 = (v1 + 124)
        while True:  # $label0
            arg0 = atomic_load(v2)
            if atomic_load(v2):
                continue
            break
    func394(v1, load32(v1 + 120))
    while True:  # $label1
        arg0 = load32(v1 + 120)
        if not atomic_load(load32(v1 + 120)):
            func390(arg0)
            break
        store32(arg0 + 56, 52368)
        store32(arg0 + 52, load32(52420))
        store32(52420, arg0)
        store32(load32(arg0 + 52) + 56, arg0)
        func54(52372)
        break
    v2 = G.global3
    while True:  # $label2
        arg0 = load32(v2 + 68)
        if load32(v2 + 68):
            v3 = load32(arg0 + 4)
            v4 = load32(arg0)
            store32(v2 + 68, load32(arg0 + 8))
            continue
        break
    v2 = 0
    while True:  # $label3
        arg0 = G.global3
        if not (load8u(G.global3 + 42) & 1):
            break
        while True:  # $label6
            func437(9688848)
            store8(arg0 + 42, (load8u(arg0 + 42) & 254))
            v3 = 0
            while True:  # $label5
                v5 = (v3 << 2)
                v4 = load32(((v3 << 2) + 9688880))
                v6 = (load32(arg0 + 72) + v5)
                v5 = load32((load32(arg0 + 72) + v5))
                store32(v6, 0)
                while True:  # $label4
                    if not v5:
                        break
                    if not v4:
                        break
                    if (v4 == 425):
                        break
                    func266(9688848)
                    func437(9688848)
                    break
                v3 = (v3 + 1)
                if ((v3 + 1) != 128):
                    continue
                break
            func266(9688848)
            if not (load8u(arg0 + 42) & 1):
                break
            v3 = (u32(v2) < u32(3))
            v2 = (v2 + 1)
            if v3:
                continue
            break
        break
    arg0 = (load32(9688040) - 1)
    store32(9688040, (load32(9688040) - 1))
    if not arg0:
        store8(9688039, 0)
    func264()
    arg0 = load32(v1 + 12)
    store32(load32(v1 + 12) + 8, load32(v1 + 8))
    store32(load32(v1 + 8) + 12, arg0)
    store32(v1 + 8, v1)
    store32(v1 + 12, v1)
    func263()
    if not G.global5:
        G.global3 = 0
        G.global4 = 0
        G.global5 = 0
        G.global6 = 1
        arg0 = (v1 + 32)
        # TODO: i32.atomic.rmw.cmpxchg
        if (1 == 3):
            a_z(v1)
            return
        atomic_store(arg0, 0)
        func97(arg0)
        return
    a_k(0)
    raise Unreachable()

# ----------------------------------------------------------
# $func432
# ----------------------------------------------------------
def func432(arg0, param1, param2, param3):
    while True:  # $label1
        while True:  # $label25
            while True:  # $label24
                while True:  # $label23
                    while True:  # $label21
                        while True:  # $label20
                            while True:  # $label19
                                while True:  # $label18
                                    while True:  # $label17
                                        while True:  # $label16
                                            while True:  # $label14
                                                while True:  # $label13
                                                    while True:  # $label15
                                                        while True:  # $label10
                                                            while True:  # $label9
                                                                while True:  # $label12
                                                                    while True:  # $label6
                                                                        while True:  # $label5
                                                                            while True:  # $label8
                                                                                while True:  # $label2
                                                                                    while True:  # $label0
                                                                                        while True:  # $label4
                                                                                            v1 = load32(arg0)
                                                                                            if (load32(arg0) <= 201326591):
                                                                                                if (v1 <= 100663327):
                                                                                                    if (v1 <= 67108863):
                                                                                                        while True:  # $label3
                                                                                                            # br_table (v1 - 33554432)
                                                                                                            break
                                                                                                            break
                                                                                                        if (v1 == -2129657856):
                                                                                                            break
                                                                                                        if v1:
                                                                                                            break
                                                                                                        break
                                                                                                    while True:  # $label7
                                                                                                        # br_table (v1 - 67108872)
                                                                                                        break
                                                                                                        break
                                                                                                    if (v1 == 67108864):
                                                                                                        break
                                                                                                    if (v1 != 100663296):
                                                                                                        break
                                                                                                    break
                                                                                                if (v1 <= 134217759):
                                                                                                    while True:  # $label11
                                                                                                        # br_table (v1 - 100663336)
                                                                                                        break
                                                                                                        break
                                                                                                    if (v1 == 100663328):
                                                                                                        break
                                                                                                    if (v1 != 134217728):
                                                                                                        break
                                                                                                    break
                                                                                                if (v1 <= 167772159):
                                                                                                    # br_table (v1 - 134217896)
                                                                                                    break
                                                                                                if (v1 == 167772160):
                                                                                                    break
                                                                                                if (v1 != 167772840):
                                                                                                    break
                                                                                                break
                                                                                            if (v1 <= 603979775):
                                                                                                if (v1 <= 335544319):
                                                                                                    if (v1 <= 268435455):
                                                                                                        if (v1 == 201326592):
                                                                                                            break
                                                                                                        if (v1 != 234881024):
                                                                                                            break
                                                                                                        break
                                                                                                    if (v1 == 268435456):
                                                                                                        break
                                                                                                    if (v1 != 301989888):
                                                                                                        break
                                                                                                    break
                                                                                                if (v1 <= 536870911):
                                                                                                    if (v1 == 335544320):
                                                                                                        break
                                                                                                    if (v1 != 369098752):
                                                                                                        break
                                                                                                    break
                                                                                                if (v1 == 536870912):
                                                                                                    break
                                                                                                if (v1 != 570425344):
                                                                                                    break
                                                                                                store32(load32(arg0 + 16) + 176, call_table(load32(arg0 + 4)))
                                                                                                break
                                                                                            while True:  # $label22
                                                                                                if (v1 <= 704643071):
                                                                                                    if (v1 <= 654311423):
                                                                                                        if (v1 == 603979776):
                                                                                                            break
                                                                                                        if (v1 != 637534208):
                                                                                                            break
                                                                                                        store32(load32(arg0 + 32) + 176, call_table(load32(arg0 + 4)))
                                                                                                        break
                                                                                                    if (v1 == 654311424):
                                                                                                        break
                                                                                                    if (v1 != 671088640):
                                                                                                        break
                                                                                                    store32(load32(arg0 + 40) + 176, call_table(load32(arg0 + 4)))
                                                                                                    break
                                                                                                if (v1 <= 771751935):
                                                                                                    if (v1 == 704643072):
                                                                                                        break
                                                                                                    if (v1 != 738197504):
                                                                                                        break
                                                                                                    store32(load32(arg0 + 56) + 176, call_table(load32(arg0 + 4)))
                                                                                                    break
                                                                                                if (v1 == 771751936):
                                                                                                    break
                                                                                                if (v1 == 805306368):
                                                                                                    break
                                                                                                if (v1 != 838860800):
                                                                                                    break
                                                                                                store32(load32(arg0 + 80) + 176, call_table(load32(arg0 + 4)))
                                                                                                break
                                                                                                break
                                                                                            store32(load32(arg0 + 32) + 176, a_t())
                                                                                            break
                                                                                            break
                                                                                        storef64((arg0 + 24) + 176, a_o())
                                                                                        break
                                                                                        break
                                                                                    break
                                                                                    break
                                                                                break
                                                                                break
                                                                            break
                                                                            break
                                                                        break
                                                                        break
                                                                    break
                                                                    break
                                                                break
                                                                break
                                                            break
                                                            break
                                                        break
                                                        break
                                                    if (v1 != 134217760):
                                                        break
                                                    break
                                                    break
                                                break
                                                break
                                            break
                                            break
                                        break
                                        break
                                    break
                                    break
                                break
                                break
                            break
                            break
                        store32(arg0 + 176, call_table(load32(arg0 + 4)))
                        break
                        break
                    store32(load32(arg0 + 24) + 176, call_table(load32(arg0 + 4)))
                    break
                    break
                store32(load32(arg0 + 48) + 176, call_table(load32(arg0 + 4)))
                break
                break
            store32(load32((arg0 - -64)) + 176, call_table(load32(arg0 + 4)))
            break
            break
        store32(load32(arg0 + 72) + 176, call_table(load32(arg0 + 4)))
        break
    if load32(arg0 + 188):
        if arg0:
        return af(arg0)
    atomic_store(arg0 + 8, 1)
    func111((arg0 + 8), 2147483647)
    return af(load32(arg0 + 184))

# ----------------------------------------------------------
# $func433
# ----------------------------------------------------------
def func433(arg0):
    v1 = load32(arg0 + 72)
    store32(arg0 + 72, ((load32(arg0 + 72) - 1) | v1))
    v1 = load32(arg0)
    if (load32(arg0) & 8):
        store32(arg0, (v1 | 32))
        return -1
    store64(arg0 + 4, 0)
    v1 = load32(arg0 + 44)
    store32(arg0 + 28, load32(arg0 + 44))
    store32(arg0 + 20, v1)
    store32(arg0 + 16, (v1 + load32(arg0 + 48)))
    return 0
