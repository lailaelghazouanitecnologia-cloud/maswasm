"""
Tzar Engine - Core module (part 6).
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
# $func1114
# ----------------------------------------------------------
def func1114(arg0):
    arg0 = load32(arg0 + 40)
    store32(arg0 + 40, 0)

# ----------------------------------------------------------
# $func1115
# ----------------------------------------------------------
def func1115(arg0):
    while True:  # $label0
        v1 = load32(arg0 + 40)
        v4 = load32(load32(load32(arg0 + 40)))
        v3 = (load32(load32(load32(arg0 + 40))) - 1)
        if (u32((load32(load32(load32(arg0 + 40))) - 1)) < u32(12)):
            if (((2077 & 0xFFFFFFFF) >> v3) & 1):
                break
        break
    v3 = (u32((v4 - 7)) < u32(4))
    store64(v1 + 40, 0)
    store64(v1 + 48, 0)
    while True:  # $label1
        if not func447(load32(v1 + 20), arg0, (11 if v3 else 12)):
            break
        while True:  # $label2
            if (u32((v4 - 11)) < u32(-4)):
                break
            if not v3:
                break
            func448()
            break
        while True:  # $label10
            while True:  # $label4
                while True:  # $label3
                    while True:  # $label6
                        while True:  # $label5
                            if load32(arg0 + 92):
                                v3 = load32(v1)
                                v7 = load32(load32(v1))
                                v2 = (load32(load32(v1)) - 1)
                                if (u32(v4) <= u32(10)):
                                    if (u32(v2) >= u32(12)):
                                        break
                                    v4 = 0
                                    if not (((2077 & 0xFFFFFFFF) >> v2) & 1):
                                        break
                                    break
                                if (u32(v2) >= u32(12)):
                                    break
                                v4 = 0
                                if not (((2077 & 0xFFFFFFFF) >> v2) & 1):
                                    break
                                break
                            while True:  # $label7
                                if (u32(v4) <= u32(10)):
                                    v2 = load32(52304)
                                    if (load32(52304) != load32(52332)):
                                        store32(9687992, 399)
                                        store32(9687988, 400)
                                        store32(9687984, 401)
                                        store32(9687980, 402)
                                        store32(9687976, 403)
                                        store32(9687972, 399)
                                        store32(9687968, 400)
                                        store32(9687964, 401)
                                        store32(9687960, 404)
                                        store32(9687956, 402)
                                        store32(9687952, 405)
                                        store32(52332, v2)
                                    store32(v1 + 44, 265)
                                    if not load32(arg0 + 56):
                                        break
                                    v2 = load32(arg0 + 12)
                                    v7 = (load32(arg0 + 12) + 1)
                                    v2 = func58(1, (((load32(arg0 + 12) + 1) & -2) + v2))
                                    store32(v1 + 40, func58(1, (((load32(arg0 + 12) + 1) & -2) + v2)))
                                    if not v2:
                                        break
                                    store32(v1 + 4, v2)
                                    arg0 = load32(arg0 + 12)
                                    store32(v1 + 44, 266)
                                    arg0 = (arg0 + v2)
                                    store32(v1 + 8, (arg0 + v2))
                                    store32(v1 + 12, (arg0 + (v7 >> 1)))
                                    func448()
                                    break
                                store32(v1 + 44, 267)
                                break
                            v5 = 1
                            if not v3:
                                break
                            while True:  # $label9
                                while True:  # $label8
                                    # br_table (v4 - 5)
                                    break
                                    break
                                store32(v1 + 48, 268)
                                break
                                break
                            arg0 = (u32(v4) > u32(10))
                            store32(v1 + 48, (269 if (u32(v4) > u32(10)) else 270))
                            if arg0:
                                break
                            break
                            break
                        v4 = (u32((v7 - 11)) < u32(-4))
                        break
                    v7 = load32(arg0 + 96)
                    v10 = (load32(arg0 + 96) << 1)
                    v15 = i32((load32(arg0 + 96) << 1))
                    v8 = (v7 + 1)
                    v9 = ((v7 + 1) & -2)
                    v11 = (((v7 + 1) & -2) << 1)
                    v15 = (((((0 if v4 else i32((load32(arg0 + 96) << 1))) + v15) + i32((((v7 + 1) & -2) << 1))) << 2) + (283 if v4 else 367))
                    if (u32((((((0 if v4 else i32((load32(arg0 + 96) << 1))) + v15) + i32((((v7 + 1) & -2) << 1))) << 2) + (283 if v4 else 367))) > u32(4294967295)):
                        break
                    v12 = load32(arg0 + 16)
                    v13 = load32(arg0 + 12)
                    v6 = load32(arg0 + 100)
                    v14 = i32(v15)
                    v2 = func58(1, i32(v15))
                    store32(v1 + 40, func58(1, i32(v15)))
                    if not v2:
                        break
                    v5 = ((((v2 + v14) + (-283 if v4 else -367)) + 31) & -32)
                    store32(v1 + 24, ((((v2 + v14) + (-283 if v4 else -367)) + 31) & -32))
                    store32(v1 + 32, (v5 + 168))
                    store32(v1 + 28, (v5 + 84))
                    store32(v1 + 36, (0 if v4 else (v5 + 252)))
                    if not func90(v5, load32(arg0 + 12), load32(arg0 + 16), load32(v3 + 16), v7, v6, load32(v3 + 32), 1, v2):
                        return 0
                    v13 = ((v13 + 1) >> 1)
                    v12 = ((v12 + 1) >> 1)
                    v8 = (v8 >> 1)
                    v14 = ((v6 + 1) >> 1)
                    v2 = (v2 + (v10 << 2))
                    if not func90(load32(v1 + 28), ((v13 + 1) >> 1), ((v12 + 1) >> 1), load32(v3 + 20), (v8 >> 1), ((v6 + 1) >> 1), load32(v3 + 36), 1, (v2 + (v10 << 2))):
                        return 0
                    v5 = 1
                    if not func90(load32(v1 + 32), v13, v12, load32(v3 + 24), v8, v14, load32(v3 + 40), 1, (v2 + (v9 << 2))):
                        return 0
                    store32(v1 + 44, 271)
                    if v4:
                        break
                    v5 = 0
                    if not func90(load32(v1 + 36), load32(arg0 + 12), load32(arg0 + 16), load32(v3 + 28), v7, v6, load32(v3 + 44), 1, (v2 + (v11 << 2))):
                        break
                    store32(v1 + 48, 272)
                    break
                    break
                v4 = (u32((v7 - 11)) < u32(-4))
                break
            v6 = (252 if v4 else 336)
            v15 = (3 if v4 else 4)
            v3 = load32(arg0 + 96)
            v10 = (v3 << 1)
            v15 = (i32((v3 << 1)) * v15)
            v16 = ((i32(((252 if v4 else 336) + 31)) + ((3 if v4 else 4) * i32(load32(arg0 + 96)))) + ((i32((v3 << 1)) * v15) << 2))
            if (u32(((i32(((252 if v4 else 336) + 31)) + ((3 if v4 else 4) * i32(load32(arg0 + 96)))) + ((i32((v3 << 1)) * v15) << 2))) > u32(4294967295)):
                break
            v8 = load32(arg0 + 16)
            v9 = load32(arg0 + 12)
            v7 = load32(arg0 + 100)
            v11 = i32(v16)
            v2 = func58(1, i32(v16))
            store32(v1 + 40, func58(1, i32(v16)))
            if not v2:
                break
            v6 = (((v2 + v11) - v6) & -32)
            store32(v1 + 24, (((v2 + v11) - v6) & -32))
            store32(v1 + 32, (v6 + 168))
            store32(v1 + 28, (v6 + 84))
            store32(v1 + 36, (0 if v4 else (v6 + 252)))
            v6 = (v2 + (i32(v15) << 2))
            if not func90(v6, load32(arg0 + 12), load32(arg0 + 16), (v2 + (i32(v15) << 2)), v3, v7, 0, 1, v2):
                break
            v9 = ((v9 + 1) >> 1)
            v8 = ((v8 + 1) >> 1)
            if not func90(load32(v1 + 28), ((v9 + 1) >> 1), ((v8 + 1) >> 1), (v3 + v6), v3, v7, 0, 1, (v2 + (v10 << 2))):
                break
            if not func90(load32(v1 + 32), v9, v8, (v6 + v10), v3, v7, 0, 1, (v2 + (v3 << 4))):
                break
            store32(v1 + 44, 273)
            v5 = load32(52304)
            if (load32(52304) != load32(52324)):
                store32(9687900, 392)
                store32(9687892, 393)
                store32(9687928, 394)
                store32(9687924, 395)
                store32(9687920, 392)
                store32(9687916, 393)
                store32(9687912, 396)
                store32(9687908, 394)
                store32(9687904, 395)
                store32(9687896, 397)
                store32(9687888, 398)
                store32(52324, v5)
            v5 = 1
            if v4:
                break
            v5 = 0
            if not func90(load32(v1 + 36), load32(arg0 + 12), load32(arg0 + 16), (v6 + (v3 * 3)), v3, v7, 0, 1, (v2 + (v3 * 24))):
                break
            store32(v1 + 48, 274)
            arg0 = load32(load32(v1))
            store32(v1 + 52, (275 if (arg0 == 5) else (275 if (load32(load32(v1)) == 10) else 276)))
            break
        func188()
        v5 = 1
        break
    return v5

# ----------------------------------------------------------
# $func1116
# ----------------------------------------------------------
def func1116(arg0):
    if not (load8u(arg0 + 8) & 1):
        while True:  # $label0
            if (load32(arg0 + 12) <= 0):
                break
            if (load32(arg0 + 16) <= 0):
                break
            v1 = load32(arg0 + 40)
            v2 = call_table(load32(v1 + 44))
            v3 = load32(v1 + 48)
            if load32(v1 + 48):
            store32(v1 + 16, (load32(v1 + 16) + v2))
            v1 = 1
            break
        return v1
    a_c()
    raise Unreachable()
    return 2396

# ----------------------------------------------------------
# $func1117
# ----------------------------------------------------------
def func1117(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if (arg2 <= 0):
            break
        v5 = (arg2 & 1)
        if (arg2 != 1):
            v6 = (arg2 & -2)
            arg2 = 0
            while True:  # $label1
                store8((arg1 + v4), ((((((load8u(arg0) * 16839) + (load8u(arg0 + 1) * 33059)) + (load8u(arg0 + 2) * 6420)) + 1081344) & 0xFFFFFFFF) >> 16))
                arg0 = (arg0 + arg3)
                store8((arg1 + (v4 | 1)), ((((((load8u((arg0 + arg3)) * 16839) + (load8u(arg0 + 1) * 33059)) + (load8u(arg0 + 2) * 6420)) + 1081344) & 0xFFFFFFFF) >> 16))
                v4 = (v4 + 2)
                arg0 = (arg0 + arg3)
                arg2 = (arg2 + 2)
                if ((arg2 + 2) != v6):
                    continue
                break
        if not v5:
            break
        store8((arg1 + v4), ((((((load8u(arg0) * 16839) + (load8u(arg0 + 1) * 33059)) + (load8u(arg0 + 2) * 6420)) + 1081344) & 0xFFFFFFFF) >> 16))
        break

# ----------------------------------------------------------
# $func1118
# ----------------------------------------------------------
def func1118(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if (arg2 <= 0):
            break
        v5 = (arg2 & 1)
        if (arg2 != 1):
            v6 = (arg2 & -2)
            arg2 = 0
            while True:  # $label1
                store8((arg1 + v4), ((((((load8u(arg0 + 2) * 16839) + (load8u(arg0 + 1) * 33059)) + (load8u(arg0) * 6420)) + 1081344) & 0xFFFFFFFF) >> 16))
                arg0 = (arg0 + arg3)
                store8((arg1 + (v4 | 1)), ((((((load8u((arg0 + arg3) + 2) * 16839) + (load8u(arg0 + 1) * 33059)) + (load8u(arg0) * 6420)) + 1081344) & 0xFFFFFFFF) >> 16))
                v4 = (v4 + 2)
                arg0 = (arg0 + arg3)
                arg2 = (arg2 + 2)
                if ((arg2 + 2) != v6):
                    continue
                break
        if not v5:
            break
        store8((arg1 + v4), ((((((load8u(arg0 + 2) * 16839) + (load8u(arg0 + 1) * 33059)) + (load8u(arg0) * 6420)) + 1081344) & 0xFFFFFFFF) >> 16))
        break

# ----------------------------------------------------------
# $func1119
# ----------------------------------------------------------
def func1119(arg0, arg1, arg2):
    if (arg2 > 0):
        while True:  # $label0
            v4 = load32((arg0 + (v3 << 2)))
            store8((arg1 + v3), (((((((load32((arg0 + (v3 << 2))) & 255) * 6420) + ((((v4 & 0xFFFFFFFF) >> 16) & 255) * 16839)) + ((((v4 & 0xFFFFFFFF) >> 8) & 255) * 33059)) + 1081344) & 0xFFFFFFFF) >> 16))
            v3 = (v3 + 1)
            if ((v3 + 1) != arg2):
                continue
            break

# ----------------------------------------------------------
# $func1120
# ----------------------------------------------------------
def func1120(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label0
        if (arg3 <= 0):
            break
        if (arg2 <= 0):
            break
        v9 = (0 if arg1 else 3)
        v10 = (arg1 != 0)
        while True:  # $label2
            v11 = (arg0 + v9)
            v7 = (arg0 + v10)
            v12 = (arg3 - 1)
            arg1 = 0
            while True:  # $label1
                v5 = (arg1 << 2)
                v6 = load8u((v11 + (arg1 << 2)))
                if (load8u((v11 + (arg1 << 2))) != 255):
                    v8 = (v5 + v7)
                    v6 = (v6 * 32897)
                    store8((v5 + v7), ((((v6 * 32897) * load8u(v8)) & 0xFFFFFFFF) >> 23))
                    v8 = (v7 + (v5 | 1))
                    store8((v7 + (v5 | 1)), (((v6 * load8u(v8)) & 0xFFFFFFFF) >> 23))
                    v5 = (v7 + (v5 | 2))
                    store8((v7 + (v5 | 2)), (((v6 * load8u(v5)) & 0xFFFFFFFF) >> 23))
                arg1 = (arg1 + 1)
                if ((arg1 + 1) != arg2):
                    continue
                break
            arg0 = (arg0 + arg4)
            arg1 = (arg3 > 1)
            arg3 = v12
            if arg1:
                continue
            break
        break

# ----------------------------------------------------------
# $func1121
# ----------------------------------------------------------
def func1121(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if (arg1 <= 0):
            break
        if (arg2 <= 0):
            break
        while True:  # $label2
            v5 = 0
            while True:  # $label1
                v4 = (arg0 + (v5 << 1))
                v6 = load8u(v4 + 1)
                v8 = (load8u(v4 + 1) & 15)
                v7 = ((load8u(v4 + 1) & 15) * 4369)
                store8(((arg0 + (v5 << 1)) + 1), (((((((load8u(v4 + 1) & 15) * 4369) * ((v6 & 240) | ((v6 & 0xFFFFFFFF) >> 4))) & 0xFFFFFFFF) >> 16) & 240) | v8))
                v4 = load8u(v4)
                store8(v4, (((((v7 * ((load8u(v4) & 240) | ((v4 & 0xFFFFFFFF) >> 4))) & 0xFFFFFFFF) >> 16) & 240) | (((v7 * (((v4 & 15) | (v4 << 4)) & 255)) & 0xFFFFFFFF) >> 20)))
                v5 = (v5 + 1)
                if ((v5 + 1) != arg1):
                    continue
                break
            arg0 = (arg0 + arg3)
            v5 = (arg2 > 1)
            arg2 = (arg2 - 1)
            if v5:
                continue
            break
        break

# ----------------------------------------------------------
# $func1122
# ----------------------------------------------------------
def func1122(arg0, arg1, arg2):
    while True:  # $label0
        if (arg1 <= 0):
            break
        if (u32(arg1) >= u32(4)):
            v8 = (arg1 & -4)
            while True:  # $label1
                v4 = (v3 << 2)
                v5 = (arg0 + (v3 << 2))
                if (u32(load32((arg0 + (v3 << 2)))) <= u32(16777215)):
                    store32(v5, arg2)
                v5 = (arg0 + (v4 | 4))
                if (u32(load32((arg0 + (v4 | 4)))) <= u32(16777215)):
                    store32(v5, arg2)
                v5 = (arg0 + (v4 | 8))
                if (u32(load32((arg0 + (v4 | 8)))) <= u32(16777215)):
                    store32(v5, arg2)
                v4 = (arg0 + (v4 | 12))
                if (u32(load32((arg0 + (v4 | 12)))) <= u32(16777215)):
                    store32(v4, arg2)
                v3 = (v3 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v8):
                    continue
                break
        arg1 = (arg1 & 3)
        if not (arg1 & 3):
            break
        while True:  # $label2
            v4 = (arg0 + (v3 << 2))
            if (u32(load32((arg0 + (v3 << 2)))) <= u32(16777215)):
                store32(v4, arg2)
            v3 = (v3 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != arg1):
                continue
            break
        break

# ----------------------------------------------------------
# $func1123
# ----------------------------------------------------------
def func1123(arg0):