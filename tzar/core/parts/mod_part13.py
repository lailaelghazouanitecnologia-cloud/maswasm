"""
Tzar Engine - Core module (part 13).
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
# $func434
# ----------------------------------------------------------
def func434(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = G.global3
    v4 = (arg2 + 12)
    if (arg2 + 12):
        store32(v4, load8u(v3 + 40))
    store8(v3 + 40, 1)
    arg0 = func265(arg0, arg1, arg2)
    arg1 = load32(arg2 + 12)
    if (u32(load32(arg2 + 12)) <= u32(2)):
        store8(G.global3 + 40, arg1)
    else:
    G.global0 = (arg2 + 16)
    return arg0

# ----------------------------------------------------------
# $func435
# ----------------------------------------------------------
def func435(arg0, arg1):
    v11 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label1
        # TODO: i32.reinterpret_f32
        v17 = arg0
        v3 = (arg0 & 2147483647)
        if (u32((arg0 & 2147483647)) <= u32(1305022426)):
            # TODO: f64.promote_f32
            v23 = arg0
            v22 = (((v23 * 0.6366197723675814) + 6755399441055744.0) + -6755399441055744.0)
            v24 = ((arg0 + ((((v23 * 0.6366197723675814) + 6755399441055744.0) + -6755399441055744.0) * -1.5707963109016418)) + (v22 * -1.5893254773528196e-08))
            storef64(arg1, ((arg0 + ((((v23 * 0.6366197723675814) + 6755399441055744.0) + -6755399441055744.0) * -1.5707963109016418)) + (v22 * -1.5893254773528196e-08)))
            v2 = (v24 < -0.7853981852531433)
            while True:  # $label0
                if (abs(v22) < 2147483648.0):
                    break
                break
            v3 = -2147483648
            if v2:
                v22 = (v22 + -1.0)
                storef64(arg1, ((v23 + ((v22 + -1.0) * -1.5707963109016418)) + (v22 * -1.5893254773528196e-08)))
                v3 = (v3 - 1)
                break
            if not (v24 > 0.7853981852531433):
                break
            v22 = (v22 + 1.0)
            storef64(arg1, ((v23 + ((v22 + 1.0) * -1.5707963109016418)) + (v22 * -1.5893254773528196e-08)))
            v3 = (v3 + 1)
            break
        if (u32(v3) >= u32(2139095040)):
            # TODO: f64.promote_f32
            storef64(arg1, (arg0 - arg0))
            v3 = 0
            break
        v3 = (((v3 & 0xFFFFFFFF) >> 23) - 150)
        # TODO: f32.reinterpret_i32
        # TODO: f64.promote_f32
        storef64(v11 + 8, (v3 - ((((v3 & 0xFFFFFFFF) >> 23) - 150) << 23)))
        v14 = (v11 + 8)
        v5 = (G.global0 - 560)
        G.global0 = (G.global0 - 560)
        v2 = ((v3 - 3) // 24)
        v13 = (((v3 - 3) // 24) if (v2 > 0) else 0)
        v6 = (v3 + ((((v3 - 3) // 24) if (v2 > 0) else 0) * -24))
        v7 = load32(28928)
        if (load32(28928) >= 0):
            v3 = (v7 + 1)
            v2 = v13
            while True:  # $label2
                if (v2 < 0):
                else:
                storef64(0.0, i32(load32(((v2 << 2) + 28944))))
                v2 = (v2 + 1)
                v4 = (v4 + 1)
                if ((v4 + 1) != v3):
                    continue
                break
        v8 = (v6 - 24)
        v3 = 0
        v4 = (v7 if (v7 > 0) else 0)
        while True:  # $label4
            v2 = 0
            v22 = 0.0
            while True:  # $label3
                v22 = ((loadf64((v14 + (v2 << 3))) * loadf64(((v5 + 320) + ((v3 - v2) << 3)))) + v22)
                v2 = (v2 + 1)
                if ((v2 + 1) != 1):
                    continue
                break
            storef64((v5 + (v3 << 3)), v22)
            v2 = (v3 == v4)
            v3 = (v3 + 1)
            if not v2:
                continue
            break
        v18 = (47 - v6)
        v15 = (48 - v6)
        v19 = (v6 - 25)
        v3 = v7
        while True:  # $label22
            while True:  # $label26
                v22 = loadf64((v5 + (v3 << 3)))
                v2 = 0
                v4 = v3
                v9 = (v3 <= 0)
                if not (v3 <= 0):
                    while True:  # $label7
                        while True:  # $label6
                            while True:  # $label5
                                v23 = (v22 * 5.960464477539063e-08)
                                if (abs((v22 * 5.960464477539063e-08)) < 2147483648.0):
                                    break
                                break
                            v23 = i32(-2147483648)
                            v22 = ((i32(-2147483648) * -16777216.0) + v22)
                            if (abs(((i32(-2147483648) * -16777216.0) + v22)) < 2147483648.0):
                                break
                            break
                        store32(i32(v22), -2147483648)
                        v4 = (v4 - 1)
                        v22 = (loadf64((v5 + ((v4 - 1) << 3))) + v23)
                        v2 = (v2 + 1)
                        if ((v2 + 1) != v3):
                            continue
                        break
                while True:  # $label8
                    v22 = func168(v22, v8)
                    v22 = (func168(v22, v8) + (floor((v22 * 0.125)) * -8.0))
                    if (abs((func168(v22, v8) + (floor((v22 * 0.125)) * -8.0))) < 2147483648.0):
                        break
                    break
                v10 = -2147483648
                v22 = (v22 - i32(v10))
                while True:  # $label11
                    while True:  # $label12
                        while True:  # $label10
                            while True:  # $label9
                                v20 = (v8 <= 0)
                                if not (v8 <= 0):
                                    v2 = ((v3 << 2) + v5)
                                    v2 = load32(v2 + 476)
                                    v2 = (v2 >> v15)
                                    v4 = (load32(v2 + 476) - ((v2 >> v15) << v15))
                                    store32(((v3 << 2) + v5) + 476, (load32(v2 + 476) - ((v2 >> v15) << v15)))
                                    v10 = (v2 + v10)
                                    break
                                if v8:
                                    break
                                break
                            v12 = (load32(((v3 << 2) + v5) + 476) >> 23)
                            if ((load32(((v3 << 2) + v5) + 476) >> 23) <= 0):
                                break
                            break
                            break
                        v12 = 2
                        if (v22 >= 0.5):
                            break
                        v12 = 0
                        break
                        break
                    v2 = 0
                    v4 = 0
                    if not v9:
                        while True:  # $label15
                            v21 = ((v5 + 480) + (v2 << 2))
                            v9 = load32(((v5 + 480) + (v2 << 2)))
                            v16 = 16777215
                            while True:  # $label14
                                while True:  # $label13
                                    if v4:
                                        break
                                    v16 = 16777216
                                    if v9:
                                        break
                                    break
                                    break
                                store32(v21, (v16 - v9))
                                break
                            v4 = 1
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v3):
                                continue
                            break
                    while True:  # $label16
                        if v20:
                            break
                        v2 = 8388607
                        while True:  # $label17
                            while True:  # $label18
                                # br_table v19
                                break
                                break
                            v2 = 4194303
                            break
                        v9 = ((v3 << 2) + v5)
                        store32(((v3 << 2) + v5) + 476, (load32(v9 + 476) & v2))
                        break
                    v10 = (v10 + 1)
                    if (v12 != 2):
                        break
                    v22 = (1.0 - v22)
                    v12 = 2
                    if not v4:
                        break
                    v22 = (v22 - func168(1.0, v8))
                    break
                if (v22 == 0.0):
                    v4 = 0
                    while True:  # $label19
                        v2 = v3
                        if (v7 >= v3):
                            break
                        while True:  # $label20
                            v2 = (v2 - 1)
                            v4 = (load32(((v5 + 480) + ((v2 - 1) << 2))) | v4)
                            if (v2 > v7):
                                continue
                            break
                        if not v4:
                            break
                        v6 = v8
                        while True:  # $label21
                            v6 = (v6 - 24)
                            v3 = (v3 - 1)
                            if not load32(((v5 + 480) + ((v3 - 1) << 2))):
                                continue
                            break
                        break
                        break
                    v2 = 1
                    while True:  # $label23
                        v4 = v2
                        v2 = (v2 + 1)
                        if not load32(((v5 + 480) + ((v7 - v4) << 2))):
                            continue
                        break
                    v4 = (v3 + v4)
                    while True:  # $label25
                        v3 = (v3 + 1)
                        storef64(((v5 + 320) + ((v3 + 1) << 3)), i32(load32((((v3 + v13) << 2) + 28944))))
                        v2 = 0
                        v22 = 0.0
                        while True:  # $label24
                            v22 = ((loadf64((v14 + (v2 << 3))) * loadf64(((v5 + 320) + ((v3 - v2) << 3)))) + v22)
                            v2 = (v2 + 1)
                            if ((v2 + 1) != 1):
                                continue
                            break
                        storef64((v5 + (v3 << 3)), v22)
                        if (v3 < v4):
                            continue
                        break
                    v3 = v4
                    continue
                break
            while True:  # $label29
                v22 = func168(v22, (24 - v6))
                if (func168(v22, (24 - v6)) >= 16777216.0):
                    while True:  # $label28
                        while True:  # $label27
                            v23 = (v22 * 5.960464477539063e-08)
                            if (abs((v22 * 5.960464477539063e-08)) < 2147483648.0):
                                break
                            break
                        v2 = -2147483648
                        v22 = ((i32(-2147483648) * -16777216.0) + v22)
                        if (abs(((i32(-2147483648) * -16777216.0) + v22)) < 2147483648.0):
                            break
                        break
                    store32(i32(v22), -2147483648)
                    v3 = (v3 + 1)
                    break
                while True:  # $label30
                    if (abs(v22) < 2147483648.0):
                        break
                    break
                v2 = -2147483648
                v6 = v8
                break
            store32(((v5 + 480) + (v3 << 2)), v2)
            break
        v22 = func168(1.0, v6)
        while True:  # $label31
            if (v3 < 0):
                break
            v2 = v3
            while True:  # $label32
                v4 = v2
                storef64((v5 + (v2 << 3)), (v22 * i32(load32(((v5 + 480) + (v2 << 2))))))
                v2 = (v2 - 1)
                v22 = (v22 * 5.960464477539063e-08)
                if v4:
                    continue
                break
            if (v3 < 0):
                break
            v4 = v3
            while True:  # $label34
                v22 = 0.0
                v2 = 0
                v6 = (v3 - v4)
                v8 = (v7 if (v6 > v7) else (v3 - v4))
                if ((v7 if (v6 > v7) else (v3 - v4)) >= 0):
                    while True:  # $label33
                        v22 = ((loadf64(((v2 << 3) + 31712)) * loadf64((v5 + ((v2 + v4) << 3)))) + v22)
                        v13 = (v2 != v8)
                        v2 = (v2 + 1)
                        if v13:
                            continue
                        break
                storef64(((v5 + 160) + (v6 << 3)), v22)
                v2 = (v4 > 0)
                v4 = (v4 - 1)
                if v2:
                    continue
                break
            break
        v22 = 0.0
        if (v3 >= 0):
            while True:  # $label35
                v2 = v3
                v3 = (v3 - 1)
                v22 = (v22 + loadf64(((v5 + 160) + (v2 << 3))))
                if v2:
                    continue
                break
        storef64(v11, (neg(v22) if v12 else v22))
        G.global0 = (v5 + 560)
        v3 = (v10 & 7)
        v22 = loadf64(v11)
        if (v17 < 0):
            storef64(arg1, neg(v22))
            v3 = (0 - v3)
            break
        storef64(arg1, v22)
        break
    G.global0 = (v11 + 16)
    return v3

# ----------------------------------------------------------
# $func436
# ----------------------------------------------------------
def func436(arg0):
    while True:  # $label0
        if (func267(arg0) != 10):
            break
        v2 = 100
        while True:  # $label2
            while True:  # $label1
                if not v2:
                    break
                if not load32(arg0):
                    break
                v2 = (v2 - 1)
                if not load32(arg0 + 4):
                    continue
                break
            break
        if (func267(arg0) != 10):
            break
        v2 = (arg0 + 4)
        while True:  # $label4
            while True:  # $label3
                v1 = load32(arg0)
                if ((load32(arg0) & 2147483647) != 2147483647):
                    break
                # TODO: i32.atomic.rmw.add
                v1 = (v1 | -2147483648)
                # TODO: i32.atomic.rmw.cmpxchg
                v1 = func434(arg0, v1, (load32(arg0 + 8) ^ 128))
                # TODO: i32.atomic.rmw.sub
                if not v1:
                    break
                if (v1 != 27):
                    break
                break
            if (func267(arg0) == 10):
                continue
            break
        break

# ----------------------------------------------------------
# $func437
# ----------------------------------------------------------
def func437(arg0):
    func436(arg0)

# ----------------------------------------------------------
# $func438
# ----------------------------------------------------------
def func438():
    v0 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v0 + 24, 0)
    store64(v0 + 16, 0)
    store64(v0 + 8, 0)
    if G.global4:
        a_q()
    while True:  # $label0
        if (load8u(9684264) & 15):
            if (load32(G.global3 + 24) != (load32(9684268) & 2147483647)):
                break
        while True:  # $label1
            v5 = load32(9684288)
            if load32(9684288):
                v2 = load32(9684296)
                # TODO: i32.atomic.rmw.add
                break
            func175(9684320)
            v2 = 2
            store32(v0 + 20, 2)
            store32(v0 + 16, 0)
            v1 = load32(9684292)
            store32(v0 + 12, load32(9684292))
            v3 = (v0 + 8)
            store32(9684292, (v0 + 8))
            store32((v1 if load32(9684308) else 9684308), v3)
            func154(9684320)
            break
        v3 = (v0 + 20)
        func54(9684264)
        v4 = G.global3
        v1 = (v0 + 4)
        if (v0 + 4):
            store32(v1, load8u(v4 + 40))
        store8(v4 + 40, 2)
        if (load32(v0 + 4) == 1):
            store8(G.global3 + 40, 1)
        v4 = not v5
        v1 = func265(v3, v2, not v5)
        while True:  # $label2
            if (load32(v3) != v2):
                break
            while True:  # $label3
                if ((v1 != 27) if v1 else 0):
                    break
                v1 = func265(v3, v2, v4)
                if (load32(v3) == v2):
                    continue
                break
            break
        v1 = (v1 if (v1 != 27) else 0)
        while True:  # $label9
            while True:  # $label4
                if v5:
                    if (v1 == 11):
                        v1 = (11 if (load32(9684296) == v2) else 0)
                    # TODO: i32.atomic.rmw.add
                    if (-1 != -2147483647):
                        break
                    func97(9684300)
                    break
                # TODO: i32.atomic.rmw.cmpxchg
                if not 2:
                    func175(9684320)
                    while True:  # $label5
                        if (load32(9684292) == (v0 + 8)):
                            store32(9684292, load32(v0 + 12))
                            break
                        v2 = load32(v0 + 8)
                        if not load32(v0 + 8):
                            break
                        store32(v2 + 4, load32(v0 + 12))
                        break
                    while True:  # $label6
                        if (load32(9684308) == (v0 + 8)):
                            store32(9684308, load32(v0 + 8))
                            break
                        v2 = load32(v0 + 12)
                        if not load32(v0 + 12):
                            break
                        store32(v2, load32(v0 + 8))
                        break
                    func154(9684320)
                    v2 = load32(v0 + 24)
                    if not load32(v0 + 24):
                        break
                    # TODO: i32.atomic.rmw.add
                    if (-1 != 1):
                        break
                    func97(load32(v0 + 24))
                    break
                func175((v0 + 20))
                while True:  # $label7
                    if load32(v0 + 12):
                        break
                    if (load8u(9684264) & 8):
                        break
                    # TODO: i32.atomic.rmw.add
                    break
                while True:  # $label8
                    v2 = load32(v0 + 8)
                    if load32(v0 + 8):
                        v1 = load32(9684268)
                        if (load32(9684268) > 0):
                            # TODO: i32.atomic.rmw.cmpxchg
                        v1 = (v2 + 12)
                        atomic_store((v2 + 12), 0)
                        func111(v1, 2147483647)
                        break
                    if (load8u(9684264) & 8):
                        break
                    # TODO: i32.atomic.rmw.sub
                    break
                break
                break
            v2 = func55(9684264)
            v3 = load32(v0 + 4)
            if (u32(load32(v0 + 4)) <= u32(2)):
                store8(G.global3 + 40, v3)
            else:
            if ((v2 if v2 else v1) != 11):
                break
            break
        v1 = 1
        if (u32(1) <= u32(2)):
            store8(G.global3 + 40, v1)
        else:
        break
    G.global0 = (v0 + 32)
    return 0

# ----------------------------------------------------------
# $func439
# ----------------------------------------------------------
def func439(arg0, arg1):

# ----------------------------------------------------------
# $func440
# ----------------------------------------------------------
def func440(arg0, arg1):
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v3 = load32(arg0)
    v4 = load32((load32(arg0) - 4))
    v3 = load32((v3 - 8))
    store64(v2 + 32, 0)
    store64(v2 + 40, 0)
    store64(v2 + 48, 0)
    store64(v2 + 55, 0)
    store64(v2 + 24, 0)
    store32(v2 + 20, 0)
    store32(v2 + 16, 32540)
    store32(v2 + 12, arg0)
    store32(v2 + 8, arg1)
    arg0 = (arg0 + v3)
    v3 = 0
    while True:  # $label0
        if func79(v4, arg1, 0):
            store32(v2 + 56, 1)
            v3 = (arg0 if (load32(v2 + 32) == 1) else 0)
            break
        while True:  # $label2
            while True:  # $label1
                # br_table load32(v2 + 44)
                break
                break
            v3 = (((load32(v2 + 28) if (load32(v2 + 40) == 1) else 0) if (load32(v2 + 36) == 1) else 0) if (load32(v2 + 48) == 1) else 0)
            break
            break
        if (load32(v2 + 32) != 1):
            if load32(v2 + 48):
                break
            if (load32(v2 + 36) != 1):
                break
            if (load32(v2 + 40) != 1):
                break
        v3 = load32(v2 + 24)
        break
    G.global0 = (v2 - -64)
    return v3

# ----------------------------------------------------------
# $func441
# ----------------------------------------------------------
def func441(arg0, arg1, arg2, arg3):
    store8(arg0 + 53, 1)
    while True:  # $label0
        if (load32(arg0 + 4) != arg2):
            break
        store8(arg0 + 52, 1)
        while True:  # $label1
            arg2 = load32(arg0 + 16)
            if not load32(arg0 + 16):
                store32(arg0 + 36, 1)
                store32(arg0 + 24, arg3)
                store32(arg0 + 16, arg1)
                if (arg3 != 1):
                    break
                if (load32(arg0 + 48) == 1):
                    break
                break
            if (arg1 == arg2):
                arg2 = load32(arg0 + 24)
                if (load32(arg0 + 24) == 2):
                    store32(arg0 + 24, arg3)
                    arg2 = arg3
                if (load32(arg0 + 48) != 1):
                    break
                if (arg2 == 1):
                    break
                break
            store32(arg0 + 36, (load32(arg0 + 36) + 1))
            break
        store8(arg0 + 54, 1)
        break

# ----------------------------------------------------------
# $func442
# ----------------------------------------------------------
def func442(arg0, arg1, arg2):
    v3 = load32(arg0 + 16)
    if not load32(arg0 + 16):
        store32(arg0 + 36, 1)
        store32(arg0 + 24, arg2)
        store32(arg0 + 16, arg1)
        return
    while True:  # $label0
        if (arg1 == v3):
            if (load32(arg0 + 24) != 2):
                break
            store32(arg0 + 24, arg2)
            return
        store8(arg0 + 54, 1)
        store32(arg0 + 24, 2)
        store32(arg0 + 36, (load32(arg0 + 36) + 1))
        break

# ----------------------------------------------------------
# $func443
# ----------------------------------------------------------
def func443(arg0):
    return (e() + 80)

# ----------------------------------------------------------
# $func444
# ----------------------------------------------------------
def func444(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if arg2:
            if not arg3:
                break
            v4 = load32(arg3)
            v5 = load32(arg2)
            while True:  # $label1
                if (arg1 <= 0):
                    break
                if v5:
                    break
                v6 = i32(arg1)
                # TODO: i64.div_u
                v5 = i32(v6)
                break
            while True:  # $label2
                if (arg0 <= 0):
                    break
                if v4:
                    break
                v6 = i32(arg0)
                # TODO: i64.div_u
                v4 = i32(v6)
                break
            arg1 = 0
            while True:  # $label3
                if (u32((v5 - 1073741824)) < u32(-1073741823)):
                    break
                if (v4 <= 0):
                    break
                if (v4 > 1073741823):
                    break
                store32(arg2, v5)
                store32(arg3, v4)
                arg1 = 1
                break
            return arg1
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 3204

# ----------------------------------------------------------
# $func445
# ----------------------------------------------------------
def func445(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    while True:  # $label0
        if (arg5 <= 0):
            break
        v7 = (arg5 & 1)
        if (arg5 != 1):
            v8 = (arg5 & -2)
            arg5 = 0
            while True:  # $label1
                arg0 = (arg0 + arg1)
                arg2 = (arg2 + arg3)
                arg2 = (arg2 + arg3)
                arg0 = (arg0 + arg1)
                arg5 = (arg5 + 2)
                if ((arg5 + 2) != v8):
                    continue
                break
        if not v7:
            break
        break

# ----------------------------------------------------------
# $func446
# ----------------------------------------------------------
def func446(arg0, arg1, arg2, arg3):
    while True:  # $label0
        if (arg3 <= 0):
            break
        v4 = (arg3 & 3)
        if (u32(arg3) >= u32(4)):
            v5 = (arg3 & -4)
            arg3 = 0
            while True:  # $label1
                arg0 = (arg0 + arg1)
                arg0 = (arg0 + arg1)
                arg0 = (arg0 + arg1)
                arg0 = (arg0 + arg1)
                arg3 = (arg3 + 4)
                if ((arg3 + 4) != v5):
                    continue
                break
        if not v4:
            break
        arg3 = 0
        while True:  # $label2
            arg0 = (arg0 + arg1)
            arg3 = (arg3 + 1)
            if ((arg3 + 1) != v4):
                continue
            break
        break

# ----------------------------------------------------------
# $func447
# ----------------------------------------------------------
def func447(arg0, arg1, arg2):
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v9 = load32(arg1 + 4)
    v10 = load32(arg1)
    while True:  # $label1
        while True:  # $label3
            while True:  # $label2
                while True:  # $label0
                    if arg0:
                        v6 = load32(arg0 + 8)
                        store32(arg1 + 72, (load32(arg0 + 8) != 0))
                        v7 = v10
                        v8 = v9
                        if not v6:
                            break
                        v6 = 0
                        v7 = load32(arg0 + 20)
                        if (load32(arg0 + 20) <= 0):
                            break
                        v8 = load32(arg0 + 24)
                        if (load32(arg0 + 24) <= 0):
                            break
                        v3 = load32(arg0 + 16)
                        arg2 = (u32(arg2) > u32(10))
                        v3 = ((load32(arg0 + 16) & -2) if (u32(arg2) > u32(10)) else v3)
                        v4 = load32(arg0 + 12)
                        v4 = ((load32(arg0 + 12) & -2) if arg2 else v4)
                        if ((((load32(arg0 + 16) & -2) if (u32(arg2) > u32(10)) else v3) | ((load32(arg0 + 12) & -2) if arg2 else v4)) < 0):
                            break
                        if (v8 > v9):
                            break
                        if (v3 >= v9):
                            break
                        if (v7 > v10):
                            break
                        if (v4 >= v10):
                            break
                        if ((v10 - v4) < v7):
                            break
                        if ((v9 - v3) >= v8):
                            break
                        break
                    store32(arg1 + 72, 0)
                    v7 = v10
                    v8 = v9
                    break
                store32(arg1 + 84, v3)
                store32(arg1 + 76, v4)
                store32(arg1 + 16, v8)
                store32(arg1 + 12, v7)
                store32(arg1 + 88, (v3 + v8))
                store32(arg1 + 80, (v4 + v7))
                if not arg0:
                    break
                arg2 = load32(arg0 + 28)
                store32(arg1 + 92, (load32(arg0 + 28) != 0))
                v6 = 1
                v3 = 1
                if arg2:
                    store32(v5 + 12, load32(arg0 + 32))
                    store32(v5 + 8, load32(arg0 + 36))
                    if not func444(v7, v8, (v5 + 12), (v5 + 8)):
                        break
                    store32(arg1 + 96, load32(v5 + 12))
                    store32(arg1 + 100, load32(v5 + 8))
                    v3 = not load32(arg1 + 92)
                arg2 = (load32(arg0) != 0)
                store32(arg1 + 68, (load32(arg0) != 0))
                store32(arg1 + 56, not load32(arg0 + 4))
                if v3:
                    break
                arg0 = 0
                if (load32(arg1 + 96) < ((v10 * 3) // 4)):
                    arg0 = (load32(arg1 + 100) < ((v9 * 3) // 4))
                store32(arg1 + 56, 0)
                store32(arg1 + 68, (arg0 | arg2))
                break
                break
            v6 = 0
            break
            break
        store32(arg1 + 68, 0)
        store32(arg1 + 92, 0)
        v6 = 1
        store32(arg1 + 56, 1)
        break
    G.global0 = (v5 + 16)
    return v6

# ----------------------------------------------------------
# $func448
# ----------------------------------------------------------
def func448():
    v0 = load32(52304)
    if (load32(52304) != load32(52328)):
        store32(9687856, 385)
        store32(9687852, 386)
        store32(9687836, 385)
        store32(9687828, 386)
        store32(9687864, 387)
        store32(9687860, 388)
        store32(9687848, 389)
        store32(9687844, 387)
        store32(9687840, 388)
        store32(9687832, 390)
        store32(9687824, 391)
        store32(52328, v0)

# ----------------------------------------------------------
# $func449
# ----------------------------------------------------------
def func449(arg0, arg1, arg2, arg3, arg4, param5, param6, param7, param8, param9, param10, param11, param12, param13, param14, param15):
    v23 = (G.global0 - 144)
    G.global0 = (G.global0 - 144)
    while True:  # $label0
        if not arg2:
            break
        v7 = (v23 + 4)
        if (v23 + 4):
            # TODO: memory.fill
        else:
        if not 0:
            break
        store32(v23 + 140, 0)
        store64(v23 + 132, 0)
        store64(v23 + 124, 0)
        store64(v23 + 116, 0)
        store64(v23 + 108, 0)
        store64(v23 + 100, 0)
        store32(v23 + 28, arg3)
        store32(v23 + 24, arg4)
        store64(v23 + 92, 0)
        store32(v23 + 4, 1)
        store32(v23 + 16, 1)
        store32(v23 + 88, (v23 + 4))
        store32(v23 + 20, arg2)
        v26 = (v23 + 88)
        v14 = (G.global0 - 160)
        G.global0 = (G.global0 - 160)
        store32(v14 + 20, 1)
        store32(v14 + 16, arg1)
        store32(v14 + 12, arg0)
        store32(v14 + 156, 0)
        while True:  # $label25
            v7 = (v14 + 156)
            v9 = (G.global0 + -64)
            G.global0 = (G.global0 + -64)
            store32(v9 + 56, arg1)
            arg2 = arg0
            store32(v9 + 60, arg0)
            v17 = (v14 + 12)
            if (v14 + 12):
            else:
            arg4 = 0
            while True:  # $label24
                while True:  # $label1
                    if not arg2:
                        arg3 = 7
                        break
                    if (u32(arg1) < u32(12)):
                        arg3 = 7
                        break
                    store32(v9 + 44, 0)
                    store64(v9 + 36, 0)
                    store64(v9 + 28, 0)
                    store64(v9 + 20, 0)
                    store32(v9 + 16, arg1)
                    store32(v9 + 12, arg2)
                    while True:  # $label2
                        v13 = func358(arg2, 6935)
                        if func358(arg2, 6935):
                            break
                        arg3 = 3
                        if (load32(arg2 + 8) != 1346520407):
                            break
                        v12 = load32(arg2 + 4)
                        if (u32((load32(arg2 + 4) + 9)) < u32(21)):
                            break
                        while True:  # $label3
                            if not arg4:
                                break
                            if (u32(v12) <= u32((arg1 - 8))):
                                break
                            arg3 = 7
                            break
                            break
                        store32(v9 + 40, v12)
                        arg2 = (arg2 + 12)
                        store32(v9 + 60, (arg2 + 12))
                        arg1 = (arg1 - 12)
                        store32(v9 + 56, (arg1 - 12))
                        if (u32(arg1) >= u32(8)):
                            break
                        arg3 = 7
                        break
                        break
                    v8 = func358(arg2, 5741)
                    if not func358(arg2, 5741):
                        if (load32(arg2 + 4) != 10):
                            arg3 = 3
                            break
                        arg3 = 7
                        if (u32(arg1) < u32(18)):
                            break
                        v16 = ((load16u(arg2 + 12) | (load8u(arg2 + 14) << 16)) + 1)
                        v15 = ((load16u(arg2 + 15) | (load8u(arg2 + 17) << 16)) + 1)
                        if ((((i32(((load16u(arg2 + 12) | (load8u(arg2 + 14) << 16)) + 1)) * i32(((load16u(arg2 + 15) | (load8u(arg2 + 17) << 16)) + 1))) & 0xFFFFFFFF) >> 32) != 0):
                            arg3 = 3
                            break
                        arg0 = load32(arg2 + 8)
                        arg1 = (arg1 - 18)
                        store32(v9 + 56, (arg1 - 18))
                        arg2 = (arg2 + 18)
                        store32(v9 + 60, (arg2 + 18))
                        arg3 = 3
                        if v13:
                            break
                        v18 = (((arg0 & 2) & 0xFFFFFFFF) >> 1)
                    if v7:
                        store32(v7, v18)
                    store32(v9 + 48, v15)
                    store32(v9 + 52, v16)
                    while True:  # $label4
                        if (not v17 & v18):
                            break
                        arg0 = 7
                        while True:  # $label5
                            if (u32(arg1) < u32(4)):
                                break
                            while True:  # $label20
                                v21 = (v9 + 56)
                                while True:  # $label6
                                    if (v8 | v13):
                                        if not v13:
                                            break
                                        if not v8:
                                            break
                                        if (load32(arg2) != 1213221953):
                                            break
                                    while True:  # $label10
                                        v11 = (v9 + 56)
                                        v13 = (v9 + 28)
                                        v7 = (v9 + 32)
                                        while True:  # $label9
                                            while True:  # $label8
                                                while True:  # $label7
                                                    if (v9 + 60):
                                                        if not v11:
                                                            break
                                                        if not v13:
                                                            break
                                                        if not v7:
                                                            break
                                                        arg1 = load32(v11)
                                                        arg2 = load32(v9 + 60)
                                                        store32(v13, 0)
                                                        store32(v7, 0)
                                                        store32(v9 + 60, arg2)
                                                        store32(v11, arg1)
                                                        if (u32(arg1) < u32(8)):
                                                            break
                                                        while True:  # $label11
                                                            if not v12:
                                                                while True:  # $label12
                                                                    arg3 = load32(arg2 + 4)
                                                                    if (u32(load32(arg2 + 4)) > u32(-10)):
                                                                        break
                                                                    v18 = 0
                                                                    if (load32(arg2) == 540561494):
                                                                        break
                                                                    if (load32(arg2) == 1278758998):
                                                                        break
                                                                    arg0 = ((arg3 + 9) & -2)
                                                                    if (u32(((arg3 + 9) & -2)) > u32(arg1)):
                                                                        break
                                                                    if (load32(arg2) == 1213221953):
                                                                        store32(v13, (arg2 + 8))
                                                                        store32(v7, arg3)
                                                                    arg2 = (arg0 + arg2)
                                                                    store32(v9 + 60, (arg0 + arg2))
                                                                    arg1 = (arg1 - arg0)
                                                                    store32(v11, (arg1 - arg0))
                                                                    if (u32(arg1) >= u32(8)):
                                                                        continue
                                                                    break
                                                                break
                                                            v29 = 22
                                                            while True:  # $label13
                                                                v18 = 3
                                                                arg0 = load32(arg2 + 4)
                                                                if (u32(load32(arg2 + 4)) > u32(-10)):
                                                                    break
                                                                arg3 = ((arg0 + 9) & -2)
                                                                v29 = (((arg0 + 9) & -2) + v29)
                                                                if (u32((((arg0 + 9) & -2) + v29)) > u32(v12)):
                                                                    break
                                                                v18 = 0
                                                                if (load32(arg2) == 540561494):
                                                                    break
                                                                if (load32(arg2) == 1278758998):
                                                                    break
                                                                if (u32(arg1) < u32(arg3)):
                                                                    break
                                                                if (load32(arg2) == 1213221953):
                                                                    store32(v13, (arg2 + 8))
                                                                    store32(v7, arg0)
                                                                arg2 = (arg2 + arg3)
                                                                store32(v9 + 60, (arg2 + arg3))
                                                                arg1 = (arg1 - arg3)
                                                                store32(v11, (arg1 - arg3))
                                                                v18 = 7
                                                                if (u32(arg1) > u32(7)):
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
                                        a_c()
                                        raise Unreachable()
                                        break
                                    arg0 = 3290
                                    if 3290:
                                        break
                                    break
                                arg2 = load32(v9 + 40)
                                v13 = (v9 + 36)
                                v7 = (v9 + 44)
                                while True:  # $label16
                                    while True:  # $label15
                                        while True:  # $label14
                                            v11 = load32(v9 + 60)
                                            if load32(v9 + 60):
                                                if not v21:
                                                    break
                                                if not v13:
                                                    break
                                                if not v7:
                                                    break
                                                while True:  # $label17
                                                    arg1 = load32(v21)
                                                    if (u32(load32(v21)) < u32(8)):
                                                        break
                                                    while True:  # $label18
                                                        arg0 = load32(v11)
                                                        if not ((load32(v11) != 540561494) & (arg0 != 1278758998)):
                                                            arg3 = load32(v11 + 4)
                                                            if (u32(arg2) >= u32(12)):
                                                                if (u32(arg3) > u32((arg2 - 12))):
                                                                    break
                                                            if arg4:
                                                                if (u32(arg3) > u32((arg1 - 8))):
                                                                    break
                                                            store32(v13, arg3)
                                                            store32(v9 + 60, (v11 + 8))
                                                            store32(v21, (load32(v21) - 8))
                                                            store32(v7, (arg0 == 1278758998))
                                                            break
                                                        arg0 = 0
                                                        while True:  # $label19
                                                            if (u32(arg1) < u32(5)):
                                                                break
                                                            if (load8u(v11) != 47):
                                                                break
                                                            arg0 = (u32(load8u(v11 + 4)) < u32(32))
                                                            break
                                                        store32(v7, arg0)
                                                        store32(v13, load32(v21))
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
                                a_c()
                                raise Unreachable()
                                break
                            arg0 = 3702
                            if 3702:
                                break
                            arg3 = 3
                            arg2 = load32(v9 + 36)
                            if (u32(load32(v9 + 36)) > u32(-10)):
                                break
                            v13 = load32(v9 + 56)
                            while True:  # $label22
                                if not load32(v9 + 44):
                                    arg0 = 7
                                    if (u32(v13) < u32(10)):
                                        break
                                    v7 = (v9 + 52)
                                    arg4 = (v9 + 48)
                                    arg0 = 0
                                    while True:  # $label21
                                        v11 = load32(v9 + 60)
                                        if not load32(v9 + 60):
                                            break
                                        if (u32(v13) < u32(10)):
                                            break
                                        if (load8u(v11 + 3) != 157):
                                            break
                                        if (load8u(v11 + 4) != 1):
                                            break
                                        if (load8u(v11 + 5) != 42):
                                            break
                                        arg1 = load8u(v11)
                                        if ((load8u(v11) & 25) != 16):
                                            break
                                        if (u32((((((load8u(v11 + 1) << 8) | (load8u(v11 + 2) << 16)) | arg1) & 0xFFFFFFFF) >> 5)) >= u32(arg2)):
                                            break
                                        arg2 = (load8u(v11 + 6) | ((load8u(v11 + 7) << 8) & 16128))
                                        if not (load8u(v11 + 6) | ((load8u(v11 + 7) << 8) & 16128)):
                                            break
                                        arg1 = (load8u(v11 + 8) | ((load8u(v11 + 9) << 8) & 16128))
                                        if not (load8u(v11 + 8) | ((load8u(v11 + 9) << 8) & 16128)):
                                            break
                                        if v7:
                                            store32(v7, arg2)
                                        arg0 = 1
                                        if not arg4:
                                            break
                                        store32(arg4, arg1)
                                        break
                                    if arg0:
                                        break
                                    break
                                arg0 = 7
                                if (u32(v13) < u32(5)):
                                    break
                                arg1 = load32(v9 + 60)
                                v7 = (v9 + 52)
                                arg4 = (v9 + 48)
                                arg0 = 0
                                v11 = (G.global0 - 32)
                                G.global0 = (G.global0 - 32)
                                while True:  # $label23
                                    if not arg1:
                                        break
                                    if (u32(v13) < u32(5)):
                                        break
                                    if (load8u(arg1) != 47):
                                        break
                                    if (u32(load8u(arg1 + 4)) > u32(31)):
                                        break
                                    if (func39(v11, 8) != 47):
                                        break
                                    arg2 = func39(v11, 14)
                                    arg1 = func39(v11, 14)
                                    if (func39(v11, 3) | load32(v11 + 24)):
                                        break
                                    if v7:
                                        store32(v7, (arg2 + 1))
                                    if arg4:
                                        store32(arg4, (arg1 + 1))
                                    arg0 = 1
                                    break
                                G.global0 = (v11 + 32)
                                if not arg0:
                                    break
                                break
                            if not v8:
                                if (v16 != load32(v9 + 52)):
                                    break
                                if (v15 != load32(v9 + 48)):
                                    break
                            if not v17:
                                break
                            v40 = load64(v9 + 12)
                            store64(v17, load64(v9 + 12))
                            store32(v17 + 32, load32(v9 + 44))
                            store64(v17 + 24, load64(v9 + 36))
                            store64(v17 + 16, load64(v9 + 28))
                            store64(v17 + 8, load64(v9 + 20))
                            arg0 = (load32(v9 + 60) - i32(v40))
                            store32(v17 + 12, (load32(v9 + 60) - i32(v40)))
                            if (arg0 < 0):
                                break
                            if (arg0 == (load32(v17 + 4) - load32(v9 + 56))):
                                break
                            a_c()
                            raise Unreachable()
                            break
                        if v17:
                            arg3 = arg0
                            break
                        if v8:
                            arg3 = arg0
                            break
                        arg3 = arg0
                        if (arg0 != 7):
                            break
                        break
                    arg3 = 0
                    break
                G.global0 = (v9 - -64)
                break
                break
            a_c()
            raise Unreachable()
            break
        store32(399 + 48, 4033)
        while True:  # $label26
            while True:  # $label27
                if load32(v14 + 48):
                    if (load32(v14 + 48) != 7):
                        break
                    if load32(v14 + 156):
                        break
                    break
                if not load32(v14 + 156):
                    break
                break
            store32(v14 + 48, 4)
            break
        while True:  # $label167
            while True:  # $label29
                while True:  # $label28
                    if load32(v14 + 48):
                        break
                    if not v26:
                        break
                    arg0 = (v14 + 48)
                    if (v14 + 48):
                        # TODO: memory.fill
                    arg0 = load32(v14 + 24)
                    store32(v14 + 112, (load32(v14 + 24) + load32(v14 + 12)))
                    store32(v14 + 108, (load32(v14 + 16) - arg0))
                    store32(v14 + 100, 262)
                    store32(v14 + 96, 263)
                    store32(v14 + 92, 264)
                    store32(v14 + 88, v26)
                    while True:  # $label142
                        if not load32(v14 + 44):
                            while True:  # $label30
                                v5 = func134(1, 2424)
                                if not func134(1, 2424):
                                    break
                                store32(v5 + 8, 6932)
                                store32(v5, 0)
                                store32(v5 + 324, 0)
                                store32(v5 + 4, 0)
                                arg0 = load32(52304)
                                if (load32(52304) == load32(52296)):
                                    break
                                while True:  # $label31
                                    if arg0:
                                        if call_table(arg0):
                                            break
                                    break
                                store32(279, 280)
                                store32(52296, load32(52304))
                                break
                            if not v5:
                                break
                            store32(v5 + 2392, load32(v14 + 28))
                            store32(v5 + 2396, load32(v14 + 32))
                            while True:  # $label32
                                if func458(v5, (v14 + 48)):
                                    arg3 = func451(load32(v14 + 48), load32(v14 + 52), load32(v26 + 20), load32(v26))
                                    if func451(load32(v14 + 48), load32(v14 + 52), load32(v26 + 20), load32(v26)):
                                        break
                                    arg1 = (v14 + 12)
                                    while True:  # $label33
                                        arg0 = load32(v26 + 20)
                                        if not load32(v26 + 20):
                                            break
                                        if not arg1:
                                            break
                                        if not load32(arg0 + 40):
                                            break
                                        if not load32(arg1 + 32):
                                            break
                                        a_c()
                                        raise Unreachable()
                                        break
                                    store32(v5 + 160, 0)
                                    arg2 = load32(v26 + 20)
                                    while True:  # $label34
                                        if v5:
                                            if not arg2:
                                                break
                                            while True:  # $label35
                                                arg0 = load32(arg2 + 44)
                                                if (load32(arg2 + 44) < 0):
                                                    break
                                                arg3 = 255
                                                if (u32(arg0) <= u32(100)):
                                                    # TODO: i32.div_u
                                                    arg3 = 100
                                                    if not (arg0 & 65535):
                                                        break
                                                while True:  # $label36
                                                    arg0 = load32(v5 + 844)
                                                    if (load32(v5 + 844) >= 12):
                                                        arg1 = load32(v5 + 848)
                                                        break
                                                    arg1 = (((arg3 * load8u(((arg0 if (arg0 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                                                    store32(v5 + 848, (((arg3 * load8u(((arg0 if (arg0 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                                                    break
                                                while True:  # $label37
                                                    arg0 = load32(v5 + 876)
                                                    if (load32(v5 + 876) >= 12):
                                                        v10 = load32(v5 + 880)
                                                        break
                                                    v10 = (((arg3 * load8u(((arg0 if (arg0 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                                                    store32(v5 + 880, (((arg3 * load8u(((arg0 if (arg0 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                                                    break
                                                arg0 = (arg1 | v10)
                                                while True:  # $label38
                                                    arg1 = load32(v5 + 908)
                                                    if (load32(v5 + 908) >= 12):
                                                        v10 = load32(v5 + 912)
                                                        break
                                                    v10 = (((arg3 * load8u(((arg1 if (arg1 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                                                    store32(v5 + 912, (((arg3 * load8u(((arg1 if (arg1 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                                                    break
                                                arg0 = (arg0 | v10)
                                                while True:  # $label39
                                                    arg1 = load32(v5 + 940)
                                                    if (load32(v5 + 940) >= 12):
                                                        arg3 = load32(v5 + 944)
                                                        break
                                                    arg3 = (((arg3 * load8u(((arg1 if (arg1 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                                                    store32(v5 + 944, (((arg3 * load8u(((arg1 if (arg1 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                                                    break
                                                if not (arg0 | arg3):
                                                    break
                                                # TODO: memory.copy
                                                store64(v5 + 588, 133143986176)
                                                store32(v5 + 816, 256)
                                                store32(v5 + 584, 1)
                                                break
                                            arg0 = load32(arg2 + 52)
                                            store32(v5 + 2416, load32(arg2 + 52))
                                            if (arg0 <= 100):
                                                if (arg0 >= 0):
                                                    break
                                            else:
                                            store32(0 + 2416, 100)
                                            break
                                        a_c()
                                        raise Unreachable()
                                        break
                                    arg3 = 0
                                    v22 = (v14 + 48)
                                    v12 = 0
                                    v18 = 0
                                    while True:  # $label40
                                        if not v5:
                                            break
                                        while True:  # $label141
                                            while True:  # $label41
                                                if not v22:
                                                    if load32(v5):
                                                        break
                                                    store32(v5 + 8, 8496)
                                                    store32(v5, 2)
                                                    v39 = (v5 + 4)
                                                    break
                                                v39 = (v5 + 4)
                                                while True:  # $label68
                                                    while True:  # $label77
                                                        while True:  # $label130
                                                            while True:  # $label42
                                                                if not load32(v5 + 4):
                                                                    if not func458(v5, v22):
                                                                        break
                                                                    if not load32(v5 + 4):
                                                                        break
                                                                while True:  # $label44
                                                                    while True:  # $label43
                                                                        arg0 = load32(v22 + 48)
                                                                        if not load32(v22 + 48):
                                                                            break
                                                                        if call_table(arg0):
                                                                            break
                                                                        break
                                                                        break
                                                                    while True:  # $label47
                                                                        while True:  # $label48
                                                                            while True:  # $label46
                                                                                while True:  # $label45
                                                                                    if load32(v22 + 68):
                                                                                        store32(v5 + 2352, 0)
                                                                                        break
                                                                                    arg0 = 2
                                                                                    arg1 = load32(v5 + 2352)
                                                                                    v12 = load8u((load32(v5 + 2352) + 10321))
                                                                                    if (arg1 == 2):
                                                                                        break
                                                                                    break
                                                                                arg0 = arg1
                                                                                arg2 = (load32(v22 + 76) - v12)
                                                                                store32(v5 + 308, ((load32(v22 + 76) - v12) >> 4))
                                                                                arg1 = (load32(v22 + 84) - v12)
                                                                                store32(v5 + 312, ((load32(v22 + 84) - v12) >> 4))
                                                                                if (arg2 < 0):
                                                                                    store32(v5 + 308, 0)
                                                                                if (arg1 >= 0):
                                                                                    break
                                                                                break
                                                                                break
                                                                            store32(v5 + 308, 0)
                                                                            break
                                                                        store32((v5 + 312), 0)
                                                                        break
                                                                    arg1 = (v12 + 15)
                                                                    arg4 = (((v12 + 15) + load32(v22 + 88)) >> 4)
                                                                    store32(v5 + 320, (((v12 + 15) + load32(v22 + 88)) >> 4))
                                                                    arg2 = ((arg1 + load32(v22 + 80)) >> 4)
                                                                    arg1 = load32(v5 + 300)
                                                                    store32(v5 + 316, (((arg1 + load32(v22 + 80)) >> 4) if (arg1 > arg2) else load32(v5 + 300)))
                                                                    arg1 = load32(v5 + 304)
                                                                    if (load32(v5 + 304) < arg4):
                                                                        store32(v5 + 320, arg1)
                                                                    while True:  # $label50
                                                                        if (arg0 > 0):
                                                                            v13 = load32(v5 + 116)
                                                                            if not load32(v5 + 80):
                                                                                while True:  # $label49
                                                                                    if v13:
                                                                                        arg0 = load8s(v5 + 132)
                                                                                        if load32(v5 + 124):
                                                                                            break
                                                                                        break
                                                                                    break
                                                                                arg0 = load32(v5 + 72)
                                                                                v7 = ((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72))
                                                                                arg0 = (((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72)) > 0)
                                                                                if not (((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72)) > 0):
                                                                                    store8(v5 + 2356, 0)
                                                                                    store8((v5 + 2360), 0)
                                                                                    store8((v5 + 2358), 0)
                                                                                    break
                                                                                arg1 = (v7 if arg0 else 0)
                                                                                arg4 = (2 if (u32(arg1) > u32(39)) else (u32((v7 if arg0 else 0)) > u32(14)))
                                                                                arg2 = (arg1 << 1)
                                                                                arg0 = load32(v5 + 76)
                                                                                if (load32(v5 + 76) <= 0):
                                                                                    store8((v5 + 2359), arg4)
                                                                                    arg0 = (arg2 + v7)
                                                                                    store8(v5 + 2356, (arg2 + v7))
                                                                                    store8((v5 + 2357), v7)
                                                                                    store8((v5 + 2361), v7)
                                                                                    store8((v5 + 2358), 0)
                                                                                    store8((v5 + 2363), arg4)
                                                                                    store8((v5 + 2360), arg0)
                                                                                    break
                                                                                store8((v5 + 2359), arg4)
                                                                                store8((v5 + 2358), 0)
                                                                                store8((v5 + 2363), arg4)
                                                                                arg1 = ((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1))
                                                                                arg0 = (9 - arg0)
                                                                                arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0))
                                                                                arg0 = (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0)))
                                                                                store8((v5 + 2357), (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0))))
                                                                                store8((v5 + 2361), arg0)
                                                                                arg0 = (arg0 + arg2)
                                                                                store8(v5 + 2356, (arg0 + arg2))
                                                                                store8((v5 + 2360), arg0)
                                                                                break
                                                                            v16 = load32(v5 + 84)
                                                                            if not v13:
                                                                                v7 = (load32(v5 + 72) + v16)
                                                                                v15 = (63 if (v7 >= 63) else (load32(v5 + 72) + v16))
                                                                                arg0 = (v15 > 0)
                                                                                arg2 = ((63 if (v7 >= 63) else (load32(v5 + 72) + v16)) if (v15 > 0) else 0)
                                                                                while True:  # $label51
                                                                                    if arg0:
                                                                                        arg0 = arg2
                                                                                        arg4 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg1 = ((arg2 & 0xFFFFFFFF) >> (2 if (u32(arg4) > u32(4)) else 1))
                                                                                            arg0 = (9 - arg4)
                                                                                            arg0 = (((arg2 & 0xFFFFFFFF) >> (2 if (u32(arg4) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg4))
                                                                                        store8((v5 + 2359), (2 if (u32(arg2) > u32(39)) else (u32(arg2) > u32(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2357), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2356, (arg0 + (arg2 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2356, 0)
                                                                                    break
                                                                                store8((v5 + 2358), 0)
                                                                                arg0 = (load32(v5 + 100) + v7)
                                                                                v13 = (63 if (arg0 >= 63) else (load32(v5 + 100) + v7))
                                                                                arg0 = (v13 > 0)
                                                                                arg1 = ((63 if (arg0 >= 63) else (load32(v5 + 100) + v7)) if (v13 > 0) else 0)
                                                                                while True:  # $label52
                                                                                    if arg0:
                                                                                        arg0 = arg1
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg1 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2363), (2 if (u32(arg1) > u32(39)) else (u32(arg1) > u32(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2361), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2360, (arg0 + (arg1 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2360, 0)
                                                                                    break
                                                                                store8((v5 + 2362), 1)
                                                                                while True:  # $label53
                                                                                    if (v15 > 0):
                                                                                        arg0 = arg2
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg2 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg2 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2367), (2 if (u32(arg2) > u32(39)) else (u32(arg2) > u32(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2365), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2364, (arg0 + (arg2 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2364, 0)
                                                                                    break
                                                                                store8((v5 + 2366), 0)
                                                                                while True:  # $label54
                                                                                    if (v13 > 0):
                                                                                        arg0 = arg1
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg1 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2371), (2 if (u32(arg1) > u32(39)) else (u32(arg1) > u32(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2369), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2368, (arg0 + (arg1 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2368, 0)
                                                                                    break
                                                                                store8((v5 + 2370), 1)
                                                                                while True:  # $label55
                                                                                    if (v15 > 0):
                                                                                        arg0 = arg2
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg2 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg2 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2375), (2 if (u32(arg2) > u32(39)) else (u32(arg2) > u32(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2373), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2372, (arg0 + (arg2 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2372, 0)
                                                                                    break
                                                                                store8((v5 + 2374), 0)
                                                                                while True:  # $label56
                                                                                    if (v13 > 0):
                                                                                        arg0 = arg1
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg1 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2379), (2 if (u32(arg1) > u32(39)) else (u32(arg1) > u32(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2377), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2376, (arg0 + (arg1 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2376, 0)
                                                                                    break
                                                                                store8((v5 + 2378), 1)
                                                                                while True:  # $label57
                                                                                    if (v15 > 0):
                                                                                        arg0 = arg2
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg2 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg2 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2383), (2 if (u32(arg2) > u32(39)) else (u32(arg2) > u32(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2381), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2380, (arg0 + (arg2 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2380, 0)
                                                                                    break
                                                                                store8((v5 + 2382), 0)
                                                                                while True:  # $label58
                                                                                    if (v13 > 0):
                                                                                        arg0 = arg1
                                                                                        arg4 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg2 = ((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg4) > u32(4)) else 1))
                                                                                            arg0 = (9 - arg4)
                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg4) > u32(4)) else 1)) if (arg0 > arg2) else (9 - arg4))
                                                                                        store8((v5 + 2387), (2 if (u32(arg1) > u32(39)) else (u32(arg1) > u32(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2385), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2384, (arg0 + (arg1 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2384, 0)
                                                                                    break
                                                                                store8((v5 + 2386), 1)
                                                                                break
                                                                            arg4 = load32(v5 + 100)
                                                                            arg2 = load32(v5 + 124)
                                                                            v12 = 0
                                                                            while True:  # $label61
                                                                                arg0 = load8s((v5 + v12) + 132)
                                                                                v11 = (v5 + (v12 << 3))
                                                                                v13 = ((v5 + (v12 << 3)) + 2356)
                                                                                while True:  # $label59
                                                                                    if arg2:
                                                                                    else:
                                                                                    v15 = ((load32(v5 + 72) + arg0) + v16)
                                                                                    arg0 = (arg0 if (v15 >= 63) else ((load32(v5 + 72) + arg0) + v16))
                                                                                    if ((arg0 if (v15 >= 63) else ((load32(v5 + 72) + arg0) + v16)) > 0):
                                                                                        v8 = (arg0 if (arg0 > 0) else 0)
                                                                                        arg0 = (arg0 if (arg0 > 0) else 0)
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg1 = ((v8 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((v8 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1)) if (arg0 > arg1) else (9 - v7))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v11 + 2357), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v13, (arg0 + (v8 << 1)))
                                                                                        store8((v11 + 2359), (2 if (u32(v8) > u32(39)) else (u32(v8) > u32(14))))
                                                                                        break
                                                                                    store8(v13, 0)
                                                                                    break
                                                                                store8((v11 + 2358), 0)
                                                                                v13 = (v11 + 2360)
                                                                                while True:  # $label60
                                                                                    arg0 = (arg4 + v15)
                                                                                    arg0 = (63 if (arg0 >= 63) else (arg4 + v15))
                                                                                    if ((63 if (arg0 >= 63) else (arg4 + v15)) > 0):
                                                                                        v15 = (arg0 if (arg0 > 0) else 0)
                                                                                        arg0 = (arg0 if (arg0 > 0) else 0)
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg1 = ((v15 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((v15 & 0xFFFFFFFF) >> (2 if (u32(v7) > u32(4)) else 1)) if (arg0 > arg1) else (9 - v7))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v11 + 2361), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v13, (arg0 + (v15 << 1)))
                                                                                        store8((v11 + 2363), (2 if (u32(v15) > u32(39)) else (u32(v15) > u32(14))))
                                                                                        break
                                                                                    store8(v13, 0)
                                                                                    break
                                                                                store8((v11 + 2362), 1)
                                                                                v12 = (v12 + 1)
                                                                                if ((v12 + 1) != 4):
                                                                                    continue
                                                                                break
                                                                        break
                                                                        break
                                                                    store8((v5 + 2362), 1)
                                                                    while True:  # $label63
                                                                        while True:  # $label62
                                                                            if v13:
                                                                                arg0 = load8s(v5 + 133)
                                                                                if load32(v5 + 124):
                                                                                    break
                                                                                break
                                                                            break
                                                                        arg0 = load32(v5 + 72)
                                                                        v7 = ((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72))
                                                                        if (((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72)) > 0):
                                                                            arg1 = (v7 if (v7 > 0) else 0)
                                                                            arg4 = (2 if (u32(arg1) > u32(39)) else (u32((v7 if (v7 > 0) else 0)) > u32(14)))
                                                                            arg2 = (arg1 << 1)
                                                                            arg0 = load32(v5 + 76)
                                                                            if (load32(v5 + 76) <= 0):
                                                                                store8((v5 + 2367), arg4)
                                                                                arg0 = (arg2 + v7)
                                                                                store8((v5 + 2364), (arg2 + v7))
                                                                                store8((v5 + 2365), v7)
                                                                                store8((v5 + 2369), v7)
                                                                                store8((v5 + 2366), 0)
                                                                                store8((v5 + 2371), arg4)
                                                                                store8((v5 + 2368), arg0)
                                                                                break
                                                                            store8((v5 + 2367), arg4)
                                                                            store8((v5 + 2366), 0)
                                                                            store8((v5 + 2371), arg4)
                                                                            arg1 = ((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1))
                                                                            arg0 = (9 - arg0)
                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0))
                                                                            arg0 = (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0)))
                                                                            store8((v5 + 2365), (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0))))
                                                                            store8((v5 + 2369), arg0)
                                                                            arg0 = (arg0 + arg2)
                                                                            store8((v5 + 2364), (arg0 + arg2))
                                                                            store8((v5 + 2368), arg0)
                                                                            break
                                                                        store8((v5 + 2368), 0)
                                                                        store8((v5 + 2366), 0)
                                                                        store8((v5 + 2364), 0)
                                                                        break
                                                                    store8((v5 + 2370), 1)
                                                                    while True:  # $label65
                                                                        while True:  # $label64
                                                                            if v13:
                                                                                arg0 = load8s(v5 + 134)
                                                                                if load32(v5 + 124):
                                                                                    break
                                                                                break
                                                                            break
                                                                        arg0 = load32(v5 + 72)
                                                                        v7 = ((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72))
                                                                        if (((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72)) > 0):
                                                                            arg1 = (v7 if (v7 > 0) else 0)
                                                                            arg4 = (2 if (u32(arg1) > u32(39)) else (u32((v7 if (v7 > 0) else 0)) > u32(14)))
                                                                            arg2 = (arg1 << 1)
                                                                            arg0 = load32(v5 + 76)
                                                                            if (load32(v5 + 76) <= 0):
                                                                                store8((v5 + 2375), arg4)
                                                                                arg0 = (arg2 + v7)
                                                                                store8((v5 + 2372), (arg2 + v7))
                                                                                store8((v5 + 2373), v7)
                                                                                store8((v5 + 2377), v7)
                                                                                store8((v5 + 2374), 0)
                                                                                store8((v5 + 2379), arg4)
                                                                                store8((v5 + 2376), arg0)
                                                                                break
                                                                            store8((v5 + 2375), arg4)
                                                                            store8((v5 + 2374), 0)
                                                                            store8((v5 + 2379), arg4)
                                                                            arg1 = ((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1))
                                                                            arg0 = (9 - arg0)
                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0))
                                                                            arg0 = (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0)))
                                                                            store8((v5 + 2373), (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0))))
                                                                            store8((v5 + 2377), arg0)
                                                                            arg0 = (arg0 + arg2)
                                                                            store8((v5 + 2372), (arg0 + arg2))
                                                                            store8((v5 + 2376), arg0)
                                                                            break
                                                                        store8((v5 + 2376), 0)
                                                                        store8((v5 + 2374), 0)
                                                                        store8((v5 + 2372), 0)
                                                                        break
                                                                    store8((v5 + 2378), 1)
                                                                    while True:  # $label67
                                                                        while True:  # $label66
                                                                            if v13:
                                                                                arg0 = load8s(v5 + 135)
                                                                                if load32(v5 + 124):
                                                                                    break
                                                                                break
                                                                            break
                                                                        arg0 = load32(v5 + 72)
                                                                        v7 = ((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72))
                                                                        if (((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72)) > 0):
                                                                            arg1 = (v7 if (v7 > 0) else 0)
                                                                            arg4 = (2 if (u32(arg1) > u32(39)) else (u32((v7 if (v7 > 0) else 0)) > u32(14)))
                                                                            arg2 = (arg1 << 1)
                                                                            arg0 = load32(v5 + 76)
                                                                            if (load32(v5 + 76) <= 0):
                                                                                store8((v5 + 2383), arg4)
                                                                                arg0 = (arg2 + v7)
                                                                                store8((v5 + 2380), (arg2 + v7))
                                                                                store8((v5 + 2381), v7)
                                                                                store8((v5 + 2385), v7)
                                                                                store8((v5 + 2382), 0)
                                                                                store8((v5 + 2387), arg4)
                                                                                store8((v5 + 2384), arg0)
                                                                                break
                                                                            store8((v5 + 2383), arg4)
                                                                            store8((v5 + 2382), 0)
                                                                            store8((v5 + 2387), arg4)
                                                                            arg1 = ((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1))
                                                                            arg0 = (9 - arg0)
                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0))
                                                                            arg0 = (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0)))
                                                                            store8((v5 + 2381), (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u32(arg0) > u32(4)) else 1)) if (arg0 > arg1) else (9 - arg0))))
                                                                            store8((v5 + 2385), arg0)
                                                                            arg0 = (arg0 + arg2)
                                                                            store8((v5 + 2380), (arg0 + arg2))
                                                                            store8((v5 + 2384), arg0)
                                                                            break
                                                                        store8((v5 + 2384), 0)
                                                                        store8((v5 + 2382), 0)
                                                                        store8((v5 + 2380), 0)
                                                                        break
                                                                    store8((v5 + 2386), 1)
                                                                    break
                                                                if 0:
                                                                    break
                                                                while True:  # $label71
                                                                    arg1 = 0
                                                                    store32(v5 + 164, 0)
                                                                    v12 = 1
                                                                    while True:  # $label70
                                                                        while True:  # $label69
                                                                            if (load32(v5 + 160) > 0):
                                                                                if not call_table(load32(52344)):
                                                                                    break
                                                                                store32(v5 + 152, (v5 + 192))
                                                                                store32(v5 + 148, v5)
                                                                                store32(v5 + 144, 261)
                                                                                v12 = (3 if (load32(v5 + 2352) > 0) else 2)
                                                                            store32(v5 + 168, v12)
                                                                            break
                                                                            break
                                                                        if not func99(v5, 1, 8437):
                                                                            break
                                                                        v12 = load32(v5 + 168)
                                                                        break
                                                                    v9 = load32(v5 + 300)
                                                                    arg2 = load32(v5 + 160)
                                                                    v19 = load32(v5 + 2352)
                                                                    v15 = (((load32(v5 + 300) << (load32(v5 + 160) > 0)) << 2) if (load32(v5 + 2352) > 0) else 0)
                                                                    arg4 = (v9 << 5)
                                                                    v13 = (v12 << 4)
                                                                    v11 = ((v9 << 5) * ((((v12 << 4) + load8u((v19 + 10321))) * 3) // 2))
                                                                    v17 = (v9 << 2)
                                                                    v21 = ((v9 << 1) + 2)
                                                                    v8 = ((v9 << (arg2 == 2)) * 800)
                                                                    while True:  # $label75
                                                                        while True:  # $label72
                                                                            if load32(v5 + 2392):
                                                                            else:
                                                                            v41 = 0
                                                                            v40 = (0 + (i32(v11) + (i32(v15) + (i32(v8) + (i32(v21) + (i32(arg4) + i32(v17)))))))
                                                                            if (u32((0 + (i32(v11) + (i32(v15) + (i32(v8) + (i32(v21) + (i32(arg4) + i32(v17)))))))) > u32(4294966432)):
                                                                                break
                                                                            v10 = load32(v5 + 2332)
                                                                            while True:  # $label76
                                                                                while True:  # $label73
                                                                                    v40 = (v40 + 863)
                                                                                    arg1 = load32(v5 + 2336)
                                                                                    if (u32((v40 + 863)) > u32(i32(load32(v5 + 2336)))):
                                                                                        arg1 = 0
                                                                                        store32(v5 + 2336, 0)
                                                                                        v10 = func58(v40, 1)
                                                                                        store32(v5 + 2332, func58(v40, 1))
                                                                                        if not v10:
                                                                                            break
                                                                                        arg1 = i32(v40)
                                                                                        store32(v5 + 2336, i32(v40))
                                                                                        v19 = load32(v5 + 2352)
                                                                                        arg2 = load32(v5 + 160)
                                                                                    store32(v5 + 2288, v10)
                                                                                    store32(v5 + 172, 0)
                                                                                    arg0 = (v10 + v17)
                                                                                    store32(v5 + 2296, (v10 + v17))
                                                                                    arg0 = (arg0 + arg4)
                                                                                    v7 = ((arg0 + arg4) + 2)
                                                                                    store32(v5 + 2300, ((arg0 + arg4) + 2))
                                                                                    arg0 = (arg0 + v21)
                                                                                    arg4 = ((arg0 + v21) if v15 else 0)
                                                                                    store32(v5 + 2304, ((arg0 + v21) if v15 else 0))
                                                                                    store32(v5 + 184, arg4)
                                                                                    arg0 = (arg0 + v15)
                                                                                    while True:  # $label74
                                                                                        if (v19 > 0):
                                                                                            if (arg2 <= 0):
                                                                                                v25 = ((arg0 + 31) & -32)
                                                                                                store32(v5 + 2308, ((arg0 + 31) & -32))
                                                                                                arg2 = (v25 + 832)
                                                                                                store32(v5 + 2348, (v25 + 832))
                                                                                                break
                                                                                            store32(v5 + 184, (arg4 + (v9 << 2)))
                                                                                        v25 = ((arg0 + 31) & -32)
                                                                                        store32(v5 + 2308, ((arg0 + 31) & -32))
                                                                                        arg0 = (v25 + 832)
                                                                                        store32(v5 + 2348, (v25 + 832))
                                                                                        arg2 = (arg0 + ((v9 if (arg2 == 2) else 0) * 800))
                                                                                        break
                                                                                    store32(v5 + 164, 0)
                                                                                    v16 = (v9 << 3)
                                                                                    store32(v5 + 2328, (v9 << 3))
                                                                                    v15 = (v9 << 4)
                                                                                    store32(v5 + 2324, (v9 << 4))
                                                                                    store32(v5 + 188, arg2)
                                                                                    arg4 = ((v8 + v25) + 832)
                                                                                    arg2 = load8u((v19 + 10321))
                                                                                    arg0 = (((v8 + v25) + 832) + (v15 * load8u((v19 + 10321))))
                                                                                    store32(v5 + 2312, (((v8 + v25) + 832) + (v15 * load8u((v19 + 10321)))))
                                                                                    arg4 = (arg4 + v11)
                                                                                    store32(v5 + 2408, (0 if not v41 else (arg4 + v11)))
                                                                                    arg2 = (((arg2 & 0xFFFFFFFF) >> 1) * v16)
                                                                                    arg0 = ((((arg2 & 0xFFFFFFFF) >> 1) * v16) + (arg0 + (v13 * v15)))
                                                                                    store32(v5 + 2316, ((((arg2 & 0xFFFFFFFF) >> 1) * v16) + (arg0 + (v13 * v15))))
                                                                                    store32(v5 + 2320, ((arg0 + ((v12 * v16) << 3)) + arg2))
                                                                                    if (u32((arg4 + i32(v41))) > u32((arg1 + v10))):
                                                                                        break
                                                                                    # TODO: memory.fill
                                                                                    store16((load32(v5 + 2300) - 2), 0)
                                                                                    store32(v5 + 2340, 0)
                                                                                    store32(v5 + 2292, 0)
                                                                                    # TODO: memory.fill
                                                                                    break
                                                                                    break
                                                                                if not func99(v5, 1, 8229):
                                                                                    break
                                                                                break
                                                                            store32(v22 + 8, 0)
                                                                            store32(v22 + 20, load32(v5 + 2312))
                                                                            store32(v22 + 24, load32(v5 + 2316))
                                                                            store32(v22 + 28, load32(v5 + 2320))
                                                                            store32(v22 + 32, load32(v5 + 2324))
                                                                            arg0 = load32(v5 + 2328)
                                                                            store32(v22 + 104, 0)
                                                                            store32(v22 + 36, arg0)
                                                                            if (load32(52304) != load32(52308)):
                                                                                store32(9687452, 294)
                                                                                store32(9687332, 295)
                                                                                store32(9687464, 296)
                                                                                store32(9687456, 297)
                                                                                store32(9687460, 298)
                                                                                store32(9687468, 299)
                                                                                store32(9687472, 300)
                                                                                store32(9687488, 301)
                                                                                store32(9687476, 302)
                                                                                store32(9687480, 303)
                                                                                store32(9687496, 304)
                                                                                store32(9687504, 305)
                                                                                store32(9687508, 306)
                                                                                store32(9687512, 307)
                                                                                store32(9687516, 308)
                                                                                store32(9687492, 309)
                                                                                store32(9687484, 310)
                                                                                store32(9687500, 311)
                                                                                store32(9687400, 312)
                                                                                store32(9687392, 313)
                                                                                store32(9687384, 314)
                                                                                store32(9687380, 315)
                                                                                store32(9687376, 316)
                                                                                store32(9687412, 317)
                                                                                store32(9687408, 318)
                                                                                store32(9687404, 319)
                                                                                store32(9687396, 320)
                                                                                store32(9687388, 321)
                                                                                store32(9687368, 322)
                                                                                store32(9687364, 323)
                                                                                store32(9687360, 324)
                                                                                store32(9687356, 325)
                                                                                store32(9687352, 326)
                                                                                store32(9687348, 327)
                                                                                store32(9687344, 328)
                                                                                store32(9687448, 329)
                                                                                store32(9687444, 330)
                                                                                store32(9687440, 331)
                                                                                store32(9687436, 332)
                                                                                store32(9687432, 333)
                                                                                store32(9687428, 334)
                                                                                store32(9687424, 335)
                                                                                store32(9687520, 336)
                                                                                store32(52308, load32(52304))
                                                                            arg1 = 1
                                                                            break
                                                                        break
                                                                        break
                                                                    a_c()
                                                                    raise Unreachable()
                                                                    break
                                                                if not 2020:
                                                                    break
                                                                store32(v5 + 2344, 0)
                                                                if (load32(v5 + 320) > 0):
                                                                    v6 = (v5 + 16)
                                                                    while True:  # $label139
                                                                        v15 = load32(v5 + 324)
                                                                        while True:  # $label129
                                                                            v17 = 0
                                                                            while True:  # $label80
                                                                                if (load32(v5 + 300) > 0):
                                                                                    v16 = (v5 + 2292)
                                                                                    while True:  # $label128
                                                                                        v13 = load32(v5 + 2288)
                                                                                        v7 = load32(v5 + 2348)
                                                                                        while True:  # $label78
                                                                                            if not load32(v5 + 120):
                                                                                                break
                                                                                            arg1 = load32(v6 + 8)
                                                                                            arg0 = load8u(v5 + 948)
                                                                                            while True:  # $label79
                                                                                                arg2 = load32(v6 + 12)
                                                                                                if (load32(v6 + 12) >= 0):
                                                                                                    break
                                                                                                arg4 = load32(v6 + 16)
                                                                                                if not load32(v6 + 16):
                                                                                                    break
                                                                                                if (u32(load32(v6 + 24)) > u32(arg4)):
                                                                                                    v40 = load64(arg4)
                                                                                                    store32(v6 + 16, (arg4 + 7))
                                                                                                    store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # $label81
                                                                                                v11 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                v41 = load64(v6)
                                                                                                v40 = i32(arg2)
                                                                                                arg4 = i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2)))
                                                                                                if (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                    v41 = (v41 - (i32((v11 + 1)) << v40))
                                                                                                    store64(v6, (v41 - (i32((v11 + 1)) << v40)))
                                                                                                    break
                                                                                                break
                                                                                            arg1 = (v11 + 1)
                                                                                            arg0 = (clz((v11 + 1)) ^ 24)
                                                                                            arg2 = ((arg1 - v11) - (clz((v11 + 1)) ^ 24))
                                                                                            store32(arg2 + 12, ((arg1 - v11) - (clz((v11 + 1)) ^ 24)))
                                                                                            v8 = ((arg1 << arg0) - 1)
                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                            if (u32(arg4) <= u32(v11)):
                                                                                                arg0 = load8u(v5 + 949)
                                                                                                while True:  # $label82
                                                                                                    if (arg2 >= 0):
                                                                                                        break
                                                                                                    arg1 = load32(v6 + 16)
                                                                                                    if not load32(v6 + 16):
                                                                                                        break
                                                                                                    if (u32(load32(v6 + 24)) > u32(arg1)):
                                                                                                        v40 = load64(arg1)
                                                                                                        store32(v6 + 16, (arg1 + 7))
                                                                                                        v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                        store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                        arg2 = (arg2 + 56)
                                                                                                        break
                                                                                                    func36(v6)
                                                                                                    v41 = load64(v6)
                                                                                                    arg2 = load32(v6 + 12)
                                                                                                    break
                                                                                                while True:  # $label83
                                                                                                    arg4 = (((arg0 * v8) & 0xFFFFFFFF) >> 8)
                                                                                                    v40 = i32(arg2)
                                                                                                    arg2 = i32(((v41 & 0xFFFFFFFF) >> i32(arg2)))
                                                                                                    if (u32((((arg0 * v8) & 0xFFFFFFFF) >> 8)) < u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                        store64(v6, (v41 - (i32((arg4 + 1)) << v40)))
                                                                                                        break
                                                                                                    break
                                                                                                arg1 = (arg4 + 1)
                                                                                                arg0 = (clz((arg4 + 1)) ^ 24)
                                                                                                store32(arg2 + 12, ((v8 - arg4) - (clz((arg4 + 1)) ^ 24)))
                                                                                                store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                break
                                                                                            arg0 = load8u(v5 + 950)
                                                                                            while True:  # $label84
                                                                                                if (arg2 >= 0):
                                                                                                    break
                                                                                                arg1 = load32(v6 + 16)
                                                                                                if not load32(v6 + 16):
                                                                                                    break
                                                                                                if (u32(load32(v6 + 24)) > u32(arg1)):
                                                                                                    v40 = load64(arg1)
                                                                                                    store32(v6 + 16, (arg1 + 7))
                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                v41 = load64(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # $label85
                                                                                                arg4 = (((arg0 * v8) & 0xFFFFFFFF) >> 8)
                                                                                                v40 = i32(arg2)
                                                                                                arg2 = i32(((v41 & 0xFFFFFFFF) >> i32(arg2)))
                                                                                                if (u32((((arg0 * v8) & 0xFFFFFFFF) >> 8)) < u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                    store64(v6, (v41 - (i32((arg4 + 1)) << v40)))
                                                                                                    break
                                                                                                break
                                                                                            arg1 = (arg4 + 1)
                                                                                            arg0 = (clz((arg4 + 1)) ^ 24)
                                                                                            store32(arg2 + 12, ((v8 - arg4) - (clz((arg4 + 1)) ^ 24)))
                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                            break
                                                                                        arg0 = ((u32(arg2) > u32(arg4)) | 2)
                                                                                        v9 = (v7 + (v17 * 800))
                                                                                        store8((v7 + (v17 * 800)) + 798, arg0)
                                                                                        while True:  # $label86
                                                                                            if not load32(v5 + 2280):
                                                                                                arg2 = load32(v6 + 12)
                                                                                                v10 = load32(v6 + 8)
                                                                                                break
                                                                                            arg1 = load32(v6 + 8)
                                                                                            arg0 = load8u(v5 + 2284)
                                                                                            while True:  # $label87
                                                                                                arg2 = load32(v6 + 12)
                                                                                                if (load32(v6 + 12) >= 0):
                                                                                                    break
                                                                                                arg4 = load32(v6 + 16)
                                                                                                if not load32(v6 + 16):
                                                                                                    break
                                                                                                if (u32(load32(v6 + 24)) > u32(arg4)):
                                                                                                    v40 = load64(arg4)
                                                                                                    store32(v6 + 16, (arg4 + 7))
                                                                                                    store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # $label88
                                                                                                v7 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                v41 = load64(v6)
                                                                                                v40 = i32(arg2)
                                                                                                arg4 = i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2)))
                                                                                                if (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                    store64(v6, (v41 - (i32((v7 + 1)) << v40)))
                                                                                                    break
                                                                                                break
                                                                                            arg1 = (v7 + 1)
                                                                                            arg0 = (clz((v7 + 1)) ^ 24)
                                                                                            arg2 = ((arg1 - v7) - (clz((v7 + 1)) ^ 24))
                                                                                            store32(arg2 + 12, ((arg1 - v7) - (clz((v7 + 1)) ^ 24)))
                                                                                            v10 = ((arg1 << arg0) - 1)
                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                            store8(v9 + 797, (u32(arg4) > u32(v7)))
                                                                                            break
                                                                                        while True:  # $label89
                                                                                            if (arg2 >= 0):
                                                                                                break
                                                                                            arg0 = load32(v6 + 16)
                                                                                            if not load32(v6 + 16):
                                                                                                break
                                                                                            if (u32(load32(v6 + 24)) > u32(arg0)):
                                                                                                v40 = load64(arg0)
                                                                                                store32(v6 + 16, (arg0 + 7))
                                                                                                store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                arg2 = (arg2 + 56)
                                                                                                break
                                                                                            func36(v6)
                                                                                            arg2 = load32(v6 + 12)
                                                                                            break
                                                                                        v8 = ((v17 << 2) + v13)
                                                                                        while True:  # $label90
                                                                                            arg0 = (((v10 * 145) & 0xFFFFFFFF) >> 8)
                                                                                            v41 = load64(v6)
                                                                                            v40 = i32(arg2)
                                                                                            arg4 = (u32((((v10 * 145) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2)))))
                                                                                            if not (u32((((v10 * 145) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                break
                                                                                            break
                                                                                        arg1 = (arg0 + 1)
                                                                                        arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                        arg2 = ((v10 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                        store32(arg2 + 12, ((v10 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                        arg0 = ((arg1 << arg0) - 1)
                                                                                        store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                        store8(v9 + 768, arg4)
                                                                                        while True:  # $label98
                                                                                            if not arg4:
                                                                                                while True:  # $label91
                                                                                                    if (arg2 >= 0):
                                                                                                        break
                                                                                                    arg1 = load32(v6 + 16)
                                                                                                    if not load32(v6 + 16):
                                                                                                        break
                                                                                                    if (u32(load32(v6 + 24)) > u32(arg1)):
                                                                                                        v40 = load64(arg1)
                                                                                                        store32(v6 + 16, (arg1 + 7))
                                                                                                        store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                        arg2 = (arg2 + 56)
                                                                                                        break
                                                                                                    func36(v6)
                                                                                                    arg2 = load32(v6 + 12)
                                                                                                    break
                                                                                                while True:  # $label92
                                                                                                    arg1 = (((arg0 * 156) & 0xFFFFFFFF) >> 8)
                                                                                                    v41 = load64(v6)
                                                                                                    v40 = i32(arg2)
                                                                                                    arg4 = (u32((((arg0 * 156) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2)))))
                                                                                                    if not (u32((((arg0 * 156) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                        v41 = (v41 - (i32((arg1 + 1)) << v40))
                                                                                                        store64(v6, (v41 - (i32((arg1 + 1)) << v40)))
                                                                                                        break
                                                                                                    break
                                                                                                arg1 = (arg1 + 1)
                                                                                                arg0 = (clz((arg1 + 1)) ^ 24)
                                                                                                arg2 = ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24))
                                                                                                store32(arg2 + 12, ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24)))
                                                                                                arg1 = ((arg1 << arg0) - 1)
                                                                                                store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                while True:  # $label95
                                                                                                    if not arg4:
                                                                                                        while True:  # $label93
                                                                                                            if (arg2 >= 0):
                                                                                                                break
                                                                                                            arg0 = load32(v6 + 16)
                                                                                                            if not load32(v6 + 16):
                                                                                                                break
                                                                                                            if (u32(load32(v6 + 24)) > u32(arg0)):
                                                                                                                v40 = load64(arg0)
                                                                                                                store32(v6 + 16, (arg0 + 7))
                                                                                                                v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                arg2 = (arg2 + 56)
                                                                                                                break
                                                                                                            func36(v6)
                                                                                                            v41 = load64(v6)
                                                                                                            arg2 = load32(v6 + 12)
                                                                                                            break
                                                                                                        while True:  # $label94
                                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> 1) & 16777215)
                                                                                                            v40 = i32(arg2)
                                                                                                            if (u32((((arg1 & 0xFFFFFFFF) >> 1) & 16777215)) < u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                                v19 = 1
                                                                                                                store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                                break
                                                                                                            v19 = 3
                                                                                                            break
                                                                                                        arg1 = (arg0 + 1)
                                                                                                        arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                        arg2 = ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                        break
                                                                                                    while True:  # $label96
                                                                                                        if (arg2 >= 0):
                                                                                                            break
                                                                                                        arg0 = load32(v6 + 16)
                                                                                                        if not load32(v6 + 16):
                                                                                                            break
                                                                                                        if (u32(load32(v6 + 24)) > u32(arg0)):
                                                                                                            v40 = load64(arg0)
                                                                                                            store32(v6 + 16, (arg0 + 7))
                                                                                                            v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                            store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                            arg2 = (arg2 + 56)
                                                                                                            break
                                                                                                        func36(v6)
                                                                                                        v41 = load64(v6)
                                                                                                        arg2 = load32(v6 + 12)
                                                                                                        break
                                                                                                    while True:  # $label97
                                                                                                        arg0 = (((arg1 * 163) & 0xFFFFFFFF) >> 8)
                                                                                                        v40 = i32(arg2)
                                                                                                        if (u32((((arg1 * 163) & 0xFFFFFFFF) >> 8)) < u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                            store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                            v19 = 2
                                                                                                            break
                                                                                                        v19 = 0
                                                                                                        break
                                                                                                    arg1 = (arg0 + 1)
                                                                                                    arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                    arg2 = ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                    break
                                                                                                arg0 = (arg1 << arg0)
                                                                                                store32(v6 + 12, arg2)
                                                                                                store32(v6 + 8, (arg0 - 1))
                                                                                                store8(v9 + 769, v19)
                                                                                                arg0 = (v19 * 16843009)
                                                                                                store32(v8, (v19 * 16843009))
                                                                                                store32(v16, arg0)
                                                                                                break
                                                                                            v20 = (v9 + 769)
                                                                                            v25 = 0
                                                                                            while True:  # $label120
                                                                                                v13 = (v16 + v25)
                                                                                                arg2 = load8u((v16 + v25))
                                                                                                v19 = 0
                                                                                                while True:  # $label119
                                                                                                    v7 = (v8 + v19)
                                                                                                    v27 = (((load8u((v8 + v19)) * 90) + (arg2 * 9)) + 12864)
                                                                                                    arg0 = load8u((((load8u((v8 + v19)) * 90) + (arg2 * 9)) + 12864))
                                                                                                    arg1 = load32(v6 + 8)
                                                                                                    while True:  # $label99
                                                                                                        arg2 = load32(v6 + 12)
                                                                                                        if (load32(v6 + 12) >= 0):
                                                                                                            break
                                                                                                        arg4 = load32(v6 + 16)
                                                                                                        if not load32(v6 + 16):
                                                                                                            break
                                                                                                        if (u32(load32(v6 + 24)) > u32(arg4)):
                                                                                                            v40 = load64(arg4)
                                                                                                            store32(v6 + 16, (arg4 + 7))
                                                                                                            store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                            arg2 = (arg2 + 56)
                                                                                                            break
                                                                                                        func36(v6)
                                                                                                        arg2 = load32(v6 + 12)
                                                                                                        break
                                                                                                    while True:  # $label100
                                                                                                        arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                        v41 = load64(v6)
                                                                                                        v40 = i32(arg2)
                                                                                                        arg4 = (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2)))))
                                                                                                        if not (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                            v41 = (v41 - (i32((arg0 + 1)) << v40))
                                                                                                            store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                            break
                                                                                                        break
                                                                                                    arg1 = (arg0 + 1)
                                                                                                    arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                    v12 = ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                    store32(arg2 + 12, ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                                    arg1 = ((arg1 << arg0) - 1)
                                                                                                    store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                    arg2 = 0
                                                                                                    while True:  # $label101
                                                                                                        if arg4:
                                                                                                            break
                                                                                                        arg0 = load8u(v27 + 1)
                                                                                                        while True:  # $label102
                                                                                                            if (v12 >= 0):
                                                                                                                break
                                                                                                            arg2 = load32(v6 + 16)
                                                                                                            if not load32(v6 + 16):
                                                                                                                break
                                                                                                            if (u32(load32(v6 + 24)) > u32(arg2)):
                                                                                                                v40 = load64(arg2)
                                                                                                                store32(v6 + 16, (arg2 + 7))
                                                                                                                v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                v12 = (v12 + 56)
                                                                                                                break
                                                                                                            func36(v6)
                                                                                                            v41 = load64(v6)
                                                                                                            v12 = load32(v6 + 12)
                                                                                                            break
                                                                                                        while True:  # $label103
                                                                                                            arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                            v40 = i32(v12)
                                                                                                            arg4 = (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(v12)))))
                                                                                                            if not (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(v12))))):
                                                                                                                v41 = (v41 - (i32((arg0 + 1)) << v40))
                                                                                                                store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                                break
                                                                                                            break
                                                                                                        arg1 = (arg0 + 1)
                                                                                                        arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                        v10 = ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                        store32(v12 + 12, ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                                        arg1 = ((arg1 << arg0) - 1)
                                                                                                        store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                        arg2 = 1
                                                                                                        if arg4:
                                                                                                            break
                                                                                                        arg0 = load8u(v27 + 2)
                                                                                                        while True:  # $label104
                                                                                                            if (v10 >= 0):
                                                                                                                break
                                                                                                            arg2 = load32(v6 + 16)
                                                                                                            if not load32(v6 + 16):
                                                                                                                break
                                                                                                            if (u32(load32(v6 + 24)) > u32(arg2)):
                                                                                                                v40 = load64(arg2)
                                                                                                                store32(v6 + 16, (arg2 + 7))
                                                                                                                v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                v10 = (v10 + 56)
                                                                                                                break
                                                                                                            func36(v6)
                                                                                                            v41 = load64(v6)
                                                                                                            v10 = load32(v6 + 12)
                                                                                                            break
                                                                                                        while True:  # $label105
                                                                                                            arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                            v40 = i32(v10)
                                                                                                            arg4 = (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(v10)))))
                                                                                                            if not (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(v10))))):
                                                                                                                v41 = (v41 - (i32((arg0 + 1)) << v40))
                                                                                                                store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                                break
                                                                                                            break
                                                                                                        arg1 = (arg0 + 1)
                                                                                                        arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                        v10 = ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                        store32(v10 + 12, ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                                        arg1 = ((arg1 << arg0) - 1)
                                                                                                        store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                        arg2 = 2
                                                                                                        if arg4:
                                                                                                            break
                                                                                                        arg0 = load8u(v27 + 3)
                                                                                                        while True:  # $label106
                                                                                                            if (v10 >= 0):
                                                                                                                break
                                                                                                            arg2 = load32(v6 + 16)
                                                                                                            if not load32(v6 + 16):
                                                                                                                break
                                                                                                            if (u32(load32(v6 + 24)) > u32(arg2)):
                                                                                                                v40 = load64(arg2)
                                                                                                                store32(v6 + 16, (arg2 + 7))
                                                                                                                v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                v10 = (v10 + 56)
                                                                                                                break
                                                                                                            func36(v6)
                                                                                                            v41 = load64(v6)
                                                                                                            v10 = load32(v6 + 12)
                                                                                                            break
                                                                                                        while True:  # $label107
                                                                                                            v21 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                            v40 = i32(v10)
                                                                                                            arg4 = i32(((v41 & 0xFFFFFFFF) >> i32(v10)))
                                                                                                            if (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u32(i32(((v41 & 0xFFFFFFFF) >> i32(v10))))):
                                                                                                                v41 = (v41 - (i32((v21 + 1)) << v40))
                                                                                                                store64(v6, (v41 - (i32((v21 + 1)) << v40)))
                                                                                                                break
                                                                                                            break
                                                                                                        arg1 = (v21 + 1)
                                                                                                        arg0 = (clz((v21 + 1)) ^ 24)
                                                                                                        arg2 = ((arg1 - v21) - (clz((v21 + 1)) ^ 24))
                                                                                                        store32(v10 + 12, ((arg1 - v21) - (clz((v21 + 1)) ^ 24)))
                                                                                                        v11 = ((arg1 << arg0) - 1)
                                                                                                        store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                        while True:  # $label112
                                                                                                            if (u32(arg4) <= u32(v21)):
                                                                                                                arg0 = load8u(v27 + 4)
                                                                                                                while True:  # $label108
                                                                                                                    if (arg2 >= 0):
                                                                                                                        break
                                                                                                                    arg1 = load32(v6 + 16)
                                                                                                                    if not load32(v6 + 16):
                                                                                                                        break
                                                                                                                    if (u32(load32(v6 + 24)) > u32(arg1)):
                                                                                                                        v40 = load64(arg1)
                                                                                                                        store32(v6 + 16, (arg1 + 7))
                                                                                                                        v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                        store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                        arg2 = (arg2 + 56)
                                                                                                                        break
                                                                                                                    func36(v6)
                                                                                                                    v41 = load64(v6)
                                                                                                                    arg2 = load32(v6 + 12)
                                                                                                                    break
                                                                                                                while True:  # $label109
                                                                                                                    arg0 = (((arg0 * v11) & 0xFFFFFFFF) >> 8)
                                                                                                                    v40 = i32(arg2)
                                                                                                                    arg4 = (u32((((arg0 * v11) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2)))))
                                                                                                                    if not (u32((((arg0 * v11) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                                        v41 = (v41 - (i32((arg0 + 1)) << v40))
                                                                                                                        store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                                        break
                                                                                                                    break
                                                                                                                arg1 = (arg0 + 1)
                                                                                                                arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                                v12 = ((v11 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                                store32(arg2 + 12, ((v11 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                                                arg1 = ((arg1 << arg0) - 1)
                                                                                                                store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                                arg2 = 3
                                                                                                                if arg4:
                                                                                                                    break
                                                                                                                arg0 = load8u(v27 + 5)
                                                                                                                while True:  # $label110
                                                                                                                    if (v12 >= 0):
                                                                                                                        break
                                                                                                                    arg2 = load32(v6 + 16)
                                                                                                                    if not load32(v6 + 16):
                                                                                                                        break
                                                                                                                    if (u32(load32(v6 + 24)) > u32(arg2)):
                                                                                                                        v40 = load64(arg2)
                                                                                                                        store32(v6 + 16, (arg2 + 7))
                                                                                                                        v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                        store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                        v12 = (v12 + 56)
                                                                                                                        break
                                                                                                                    func36(v6)
                                                                                                                    v41 = load64(v6)
                                                                                                                    v12 = load32(v6 + 12)
                                                                                                                    break
                                                                                                                while True:  # $label111
                                                                                                                    arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                                    v40 = i32(v12)
                                                                                                                    if (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u32(i32(((v41 & 0xFFFFFFFF) >> i32(v12))))):
                                                                                                                        store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                                        v10 = (arg1 - arg0)
                                                                                                                        break
                                                                                                                    v10 = (arg0 + 1)
                                                                                                                    break
                                                                                                                arg2 = 4
                                                                                                                arg0 = (clz(v10) ^ 24)
                                                                                                                v12 = (v12 - (clz(v10) ^ 24))
                                                                                                                break
                                                                                                            arg0 = load8u(v27 + 6)
                                                                                                            while True:  # $label113
                                                                                                                if (arg2 >= 0):
                                                                                                                    break
                                                                                                                arg1 = load32(v6 + 16)
                                                                                                                if not load32(v6 + 16):
                                                                                                                    break
                                                                                                                if (u32(load32(v6 + 24)) > u32(arg1)):
                                                                                                                    v40 = load64(arg1)
                                                                                                                    store32(v6 + 16, (arg1 + 7))
                                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                    arg2 = (arg2 + 56)
                                                                                                                    break
                                                                                                                func36(v6)
                                                                                                                v41 = load64(v6)
                                                                                                                arg2 = load32(v6 + 12)
                                                                                                                break
                                                                                                            while True:  # $label114
                                                                                                                arg0 = (((arg0 * v11) & 0xFFFFFFFF) >> 8)
                                                                                                                v40 = i32(arg2)
                                                                                                                arg4 = (u32((((arg0 * v11) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2)))))
                                                                                                                if not (u32((((arg0 * v11) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                                    v41 = (v41 - (i32((arg0 + 1)) << v40))
                                                                                                                    store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                                    break
                                                                                                                break
                                                                                                            arg1 = (arg0 + 1)
                                                                                                            arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                            v12 = ((v11 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                            store32(arg2 + 12, ((v11 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                                            arg1 = ((arg1 << arg0) - 1)
                                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                            arg2 = 6
                                                                                                            if arg4:
                                                                                                                break
                                                                                                            arg0 = load8u(v27 + 7)
                                                                                                            while True:  # $label115
                                                                                                                if (v12 >= 0):
                                                                                                                    break
                                                                                                                arg2 = load32(v6 + 16)
                                                                                                                if not load32(v6 + 16):
                                                                                                                    break
                                                                                                                if (u32(load32(v6 + 24)) > u32(arg2)):
                                                                                                                    v40 = load64(arg2)
                                                                                                                    store32(v6 + 16, (arg2 + 7))
                                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                    v12 = (v12 + 56)
                                                                                                                    break
                                                                                                                func36(v6)
                                                                                                                v41 = load64(v6)
                                                                                                                v12 = load32(v6 + 12)
                                                                                                                break
                                                                                                            while True:  # $label116
                                                                                                                arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                                v40 = i32(v12)
                                                                                                                arg4 = (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(v12)))))
                                                                                                                if not (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(v12))))):
                                                                                                                    v41 = (v41 - (i32((arg0 + 1)) << v40))
                                                                                                                    store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                                    break
                                                                                                                break
                                                                                                            arg1 = (arg0 + 1)
                                                                                                            arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                            v10 = ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                            store32(v12 + 12, ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                                            arg1 = ((arg1 << arg0) - 1)
                                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                            arg2 = 7
                                                                                                            if arg4:
                                                                                                                break
                                                                                                            arg0 = load8u(v27 + 8)
                                                                                                            while True:  # $label117
                                                                                                                if (v10 >= 0):
                                                                                                                    break
                                                                                                                arg2 = load32(v6 + 16)
                                                                                                                if not load32(v6 + 16):
                                                                                                                    break
                                                                                                                if (u32(load32(v6 + 24)) > u32(arg2)):
                                                                                                                    v40 = load64(arg2)
                                                                                                                    store32(v6 + 16, (arg2 + 7))
                                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                                    v10 = (v10 + 56)
                                                                                                                    break
                                                                                                                func36(v6)
                                                                                                                v41 = load64(v6)
                                                                                                                v10 = load32(v6 + 12)
                                                                                                                break
                                                                                                            while True:  # $label118
                                                                                                                arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                                v40 = i32(v10)
                                                                                                                if (u32((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u32(i32(((v41 & 0xFFFFFFFF) >> i32(v10))))):
                                                                                                                    store64(v6, (v41 - (i32((arg0 + 1)) << v40)))
                                                                                                                    arg0 = (arg1 - arg0)
                                                                                                                    break
                                                                                                                arg0 = (arg0 + 1)
                                                                                                                break
                                                                                                            arg2 = 8
                                                                                                            arg1 = (clz(arg0) ^ 24)
                                                                                                            v12 = (v10 - (clz(arg0) ^ 24))
                                                                                                            break
                                                                                                        arg0 = (arg0 << arg1)
                                                                                                        store32(v6 + 12, v12)
                                                                                                        store32(v6 + 8, (arg0 - 1))
                                                                                                        break
                                                                                                    store8(v7, arg2)
                                                                                                    v19 = (v19 + 1)
                                                                                                    if ((v19 + 1) != 4):
                                                                                                        continue
                                                                                                    break
                                                                                                store32(v20, load32(v8))
                                                                                                store8(v13, arg2)
                                                                                                v20 = (v20 + 4)
                                                                                                v25 = (v25 + 1)
                                                                                                if ((v25 + 1) != 4):
                                                                                                    continue
                                                                                                break
                                                                                            break
                                                                                        arg0 = load32(v6 + 8)
                                                                                        while True:  # $label121
                                                                                            arg2 = load32(v6 + 12)
                                                                                            if (load32(v6 + 12) >= 0):
                                                                                                break
                                                                                            arg1 = load32(v6 + 16)
                                                                                            if not load32(v6 + 16):
                                                                                                break
                                                                                            if (u32(load32(v6 + 24)) > u32(arg1)):
                                                                                                v40 = load64(arg1)
                                                                                                store32(v6 + 16, (arg1 + 7))
                                                                                                store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                arg2 = (arg2 + 56)
                                                                                                break
                                                                                            func36(v6)
                                                                                            arg2 = load32(v6 + 12)
                                                                                            break
                                                                                        while True:  # $label122
                                                                                            arg1 = (((arg0 * 142) & 0xFFFFFFFF) >> 8)
                                                                                            v41 = load64(v6)
                                                                                            v40 = i32(arg2)
                                                                                            arg4 = (u32((((arg0 * 142) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2)))))
                                                                                            if not (u32((((arg0 * 142) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(v6) & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                v41 = (v41 - (i32((arg1 + 1)) << v40))
                                                                                                store64(v6, (v41 - (i32((arg1 + 1)) << v40)))
                                                                                                break
                                                                                            break
                                                                                        arg1 = (arg1 + 1)
                                                                                        arg0 = (clz((arg1 + 1)) ^ 24)
                                                                                        arg2 = ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24))
                                                                                        store32(arg2 + 12, ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24)))
                                                                                        arg0 = ((arg1 << arg0) - 1)
                                                                                        store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                        v19 = 0
                                                                                        while True:  # $label123
                                                                                            if arg4:
                                                                                                break
                                                                                            while True:  # $label124
                                                                                                if (arg2 >= 0):
                                                                                                    break
                                                                                                arg1 = load32(v6 + 16)
                                                                                                if not load32(v6 + 16):
                                                                                                    break
                                                                                                if (u32(load32(v6 + 24)) > u32(arg1)):
                                                                                                    v40 = load64(arg1)
                                                                                                    store32(v6 + 16, (arg1 + 7))
                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                v41 = load64(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # $label125
                                                                                                arg1 = (((arg0 * 114) & 0xFFFFFFFF) >> 8)
                                                                                                v40 = i32(arg2)
                                                                                                arg4 = (u32((((arg0 * 114) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2)))))
                                                                                                if not (u32((((arg0 * 114) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                    v41 = (v41 - (i32((arg1 + 1)) << v40))
                                                                                                    store64(v6, (v41 - (i32((arg1 + 1)) << v40)))
                                                                                                    break
                                                                                                break
                                                                                            arg1 = (arg1 + 1)
                                                                                            arg0 = (clz((arg1 + 1)) ^ 24)
                                                                                            arg2 = ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24))
                                                                                            store32(arg2 + 12, ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24)))
                                                                                            arg0 = ((arg1 << arg0) - 1)
                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                            v19 = 2
                                                                                            if arg4:
                                                                                                break
                                                                                            while True:  # $label126
                                                                                                if (arg2 >= 0):
                                                                                                    break
                                                                                                arg1 = load32(v6 + 16)
                                                                                                if not load32(v6 + 16):
                                                                                                    break
                                                                                                if (u32(load32(v6 + 24)) > u32(arg1)):
                                                                                                    v40 = load64(arg1)
                                                                                                    store32(v6 + 16, (arg1 + 7))
                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                v41 = load64(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # $label127
                                                                                                arg1 = (((arg0 * 183) & 0xFFFFFFFF) >> 8)
                                                                                                v40 = i32(arg2)
                                                                                                if (u32((((arg0 * 183) & 0xFFFFFFFF) >> 8)) < u32(i32(((v41 & 0xFFFFFFFF) >> i32(arg2))))):
                                                                                                    v19 = 1
                                                                                                    store64(v6, (v41 - (i32((arg1 + 1)) << v40)))
                                                                                                    break
                                                                                                v19 = 3
                                                                                                break
                                                                                            arg1 = (arg1 + 1)
                                                                                            arg0 = (clz((arg1 + 1)) ^ 24)
                                                                                            store32(arg2 + 12, ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24)))
                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                            break
                                                                                        store8(v9 + 785, v19)
                                                                                        v17 = (v17 + 1)
                                                                                        if ((v17 + 1) < load32(v5 + 300)):
                                                                                            continue
                                                                                        break
                                                                                break
                                                                                break
                                                                            a_c()
                                                                            raise Unreachable()
                                                                            break
                                                                        if not 3339:
                                                                            break
                                                                        if (load32(v5 + 2340) < load32(v5 + 300)):
                                                                            v24 = ((v5 + ((v15 & v18) << 5)) + 328)
                                                                            while True:  # $label135
                                                                                v10 = 0
                                                                                v25 = 0
                                                                                v8 = 0
                                                                                v28 = (G.global0 - 32)
                                                                                G.global0 = (G.global0 - 32)
                                                                                arg2 = load32(v5 + 2300)
                                                                                v32 = (load32(v5 + 2300) - 2)
                                                                                v30 = load32(v5 + 2340)
                                                                                v33 = (arg2 + (load32(v5 + 2340) << 1))
                                                                                v34 = load32(v5 + 2348)
                                                                                while True:  # $label134
                                                                                    while True:  # $label131
                                                                                        if load32(v5 + 2280):
                                                                                            arg0 = (v34 + (v30 * 800))
                                                                                            if load8u((v34 + (v30 * 800)) + 797):
                                                                                                break
                                                                                        arg0 = (v34 + (v30 * 800))
                                                                                        v16 = load8u((v34 + (v30 * 800)) + 798)
                                                                                        # TODO: memory.fill
                                                                                        v7 = (v5 + (v16 << 5))
                                                                                        while True:  # $label132
                                                                                            if not load8u(arg0 + 768):
                                                                                                v18 = (v5 + 2008)
                                                                                                store64(v28 + 24, 0)
                                                                                                store64(v28 + 16, 0)
                                                                                                store64(v28 + 8, 0)
                                                                                                store64(v28, 0)
                                                                                                v10 = 1
                                                                                                arg1 = (arg2 - 1)
                                                                                                arg4 = (arg2 + (v30 << 1))
                                                                                                arg2 = call_table(load32(9687280))
                                                                                                arg1 = (call_table(load32(9687280)) > 0)
                                                                                                store8(v28, (call_table(load32(9687280)) > 0))
                                                                                                store8(arg4 + 1, arg1)
                                                                                                if (arg2 >= 2):
                                                                                                    break
                                                                                                arg1 = (((load16s(v28) + 3) & 0xFFFFFFFF) >> 3)
                                                                                                store16(arg0 + 480, (((load16s(v28) + 3) & 0xFFFFFFFF) >> 3))
                                                                                                store16(arg0 + 448, arg1)
                                                                                                store16(arg0 + 416, arg1)
                                                                                                store16(arg0 + 384, arg1)
                                                                                                store16(arg0 + 352, arg1)
                                                                                                store16(arg0 + 320, arg1)
                                                                                                store16(arg0 + 288, arg1)
                                                                                                store16(arg0 + 256, arg1)
                                                                                                store16(arg0 + 224, arg1)
                                                                                                store16(arg0 + 192, arg1)
                                                                                                store16(arg0 + 160, arg1)
                                                                                                store16(arg0 + 128, arg1)
                                                                                                store16(arg0 + 96, arg1)
                                                                                                store16(arg0 + 64, arg1)
                                                                                                store16(arg0 + 32, arg1)
                                                                                                store16(arg0, arg1)
                                                                                                break
                                                                                            v18 = (v5 + 2212)
                                                                                            break
                                                                                        v9 = (v7 + 820)
                                                                                        v29 = (load8u(v32) & 15)
                                                                                        v35 = (load8u(v33) & 15)
                                                                                        while True:  # $label133
                                                                                            arg1 = arg0
                                                                                            v17 = call_table(load32(9687280))
                                                                                            v15 = load16u(arg0)
                                                                                            arg2 = (v10 < v17)
                                                                                            arg0 = ((v35 & 0xFFFFFFFF) >> 1)
                                                                                            v21 = call_table(load32(9687280))
                                                                                            v13 = load16u(arg1 + 32)
                                                                                            v7 = (v10 < v21)
                                                                                            arg2 = ((((arg0 & 126) | (arg2 << 7)) & 0xFFFFFFFF) >> 1)
                                                                                            v11 = call_table(load32(9687280))
                                                                                            arg0 = load16u(arg1 + 64)
                                                                                            arg4 = (v10 < v11)
                                                                                            arg2 = ((((v7 << 7) | arg2) & 0xFFFFFFFF) >> 1)
                                                                                            v7 = call_table(load32(9687280))
                                                                                            v25 = ((((((3 if (v21 > 3) else (2 if (v21 >= 2) else (v13 != 0))) | (12 if (v17 > 3) else (8 if (v17 >= 2) else ((v15 != 0) << 2)))) << 4) | (12 if (v11 > 3) else (8 if (v11 >= 2) else ((arg0 != 0) << 2)))) | (3 if (v7 > 3) else (2 if (v7 >= 2) else (load16u(arg1 + 96) != 0)))) | (v25 << 8))
                                                                                            arg0 = (v7 > v10)
                                                                                            v35 = (((v7 > v10) << 3) | ((((arg4 << 7) | arg2) & 0xFFFFFFFF) >> 5))
                                                                                            v29 = ((arg0 << 7) | (((v29 & 254) & 0xFFFFFFFF) >> 1))
                                                                                            arg0 = (arg1 + 128)
                                                                                            v8 = (v8 + 1)
                                                                                            if ((v8 + 1) != 4):
                                                                                                continue
                                                                                            break
                                                                                        v31 = (v5 + 2144)
                                                                                        arg4 = load8u(v32)
                                                                                        arg2 = load8u(v33)
                                                                                        v27 = (v5 + (v16 << 5))
                                                                                        v20 = ((v5 + (v16 << 5)) + 836)
                                                                                        v36 = call_table(load32(9687280))
                                                                                        v9 = load16u(arg1 + 128)
                                                                                        arg0 = (v36 > 0)
                                                                                        v37 = call_table(load32(9687280))
                                                                                        v17 = load16u(arg1 + 160)
                                                                                        v38 = call_table(load32(9687280))
                                                                                        v21 = load16u(arg1 + 192)
                                                                                        v11 = (v38 > 0)
                                                                                        v8 = (v37 > 0)
                                                                                        v10 = call_table(load32(9687280))
                                                                                        v16 = load16u(arg1 + 224)
                                                                                        arg4 = load8u(v32)
                                                                                        arg2 = load8u(v33)
                                                                                        v12 = call_table(load32(9687280))
                                                                                        v15 = load16u(arg1 + 256)
                                                                                        arg0 = (v12 > 0)
                                                                                        v18 = call_table(load32(9687280))
                                                                                        v13 = load16u(arg1 + 288)
                                                                                        v19 = call_table(load32(9687280))
                                                                                        v7 = load16u(arg1 + 320)
                                                                                        arg0 = (v19 > 0)
                                                                                        arg4 = (v18 > 0)
                                                                                        v20 = call_table(load32(9687280))
                                                                                        arg2 = load16u(arg1 + 352)
                                                                                        arg1 = ((v20 > 0) << 7)
                                                                                        arg0 = ((v10 > 0) << 5)
                                                                                        store8(v33, (((((v20 > 0) << 7) | (arg0 << 6)) | (((v10 > 0) << 5) | (v11 << 4))) | v35))
                                                                                        store8(v32, (((((v8 << 4) | ((v29 & 0xFFFFFFFF) >> 4)) | arg0) | (arg4 << 6)) | arg1))
                                                                                        arg1 = (v34 + (v30 * 800))
                                                                                        arg0 = ((((((3 if (v37 > 3) else (2 if (v37 >= 2) else (v17 != 0))) | (12 if (v36 > 3) else (8 if (v36 >= 2) else ((v9 != 0) << 2)))) << 4) | (12 if (v38 > 3) else (8 if (v38 >= 2) else ((v21 != 0) << 2)))) | (3 if (v10 > 3) else (2 if (v10 >= 2) else (v16 != 0)))) | ((((((3 if (v18 > 3) else (2 if (v18 >= 2) else (v13 != 0))) | (12 if (v12 > 3) else (8 if (v12 >= 2) else ((v15 != 0) << 2)))) << 4) | (12 if (v19 > 3) else (8 if (v19 >= 2) else ((v7 != 0) << 2)))) | (3 if (v20 > 3) else (2 if (v20 >= 2) else (arg2 != 0)))) << 8))
                                                                                        store32((v34 + (v30 * 800)) + 792, ((((((3 if (v37 > 3) else (2 if (v37 >= 2) else (v17 != 0))) | (12 if (v36 > 3) else (8 if (v36 >= 2) else ((v9 != 0) << 2)))) << 4) | (12 if (v38 > 3) else (8 if (v38 >= 2) else ((v21 != 0) << 2)))) | (3 if (v10 > 3) else (2 if (v10 >= 2) else (v16 != 0)))) | ((((((3 if (v18 > 3) else (2 if (v18 >= 2) else (v13 != 0))) | (12 if (v12 > 3) else (8 if (v12 >= 2) else ((v15 != 0) << 2)))) << 4) | (12 if (v19 > 3) else (8 if (v19 >= 2) else ((v7 != 0) << 2)))) | (3 if (v20 > 3) else (2 if (v20 >= 2) else (arg2 != 0)))) << 8)))
                                                                                        store32(arg1 + 788, v25)
                                                                                        if (arg0 & 43690):
                                                                                        else:
                                                                                        store8(0 + 796, load32(v27 + 848))
                                                                                        v10 = ((arg0 | v25) != 0)
                                                                                        break
                                                                                        break
                                                                                    store8(v33, 0)
                                                                                    store8(v32, 0)
                                                                                    if not load8u(arg0 + 768):
                                                                                        store8((arg2 + (v30 << 1)) + 1, 0)
                                                                                        store8((arg2 - 1), 0)
                                                                                    arg0 = (v34 + (v30 * 800))
                                                                                    store64((v34 + (v30 * 800)) + 788, 0)
                                                                                    store8(arg0 + 796, 0)
                                                                                    break
                                                                                if (load32(v5 + 2352) > 0):
                                                                                    arg1 = (load32(v5 + 2304) + (load32(v5 + 2340) << 2))
                                                                                    arg0 = (v34 + (v30 * 800))
                                                                                    store32((load32(v5 + 2304) + (load32(v5 + 2340) << 2)), load32((((v5 + (load8u((v34 + (v30 * 800)) + 798) << 3)) + (load8u(arg0 + 768) << 2)) + 2356)))
                                                                                    store8(arg1 + 2, (load8u(arg1 + 2) | v10))
                                                                                arg0 = load32(v24 + 28)
                                                                                G.global0 = (v28 + 32)
                                                                                if arg0:
                                                                                    v20 = 0
                                                                                    if load32(v5):
                                                                                        break
                                                                                    store32(v5 + 8, 8324)
                                                                                    store64(v5, 7)
                                                                                    break
                                                                                arg0 = (load32(v5 + 2340) + 1)
                                                                                store32(v5 + 2340, (load32(v5 + 2340) + 1))
                                                                                if (arg0 < load32(v5 + 300)):
                                                                                    continue
                                                                                break
                                                                        store16((load32(v5 + 2300) - 2), 0)
                                                                        store32(v5 + 2340, 0)
                                                                        store32(v5 + 2292, 0)
                                                                        while True:  # $label137
                                                                            arg0 = 0
                                                                            while True:  # $label136
                                                                                if (load32(v5 + 2352) <= 0):
                                                                                    break
                                                                                arg1 = load32(v5 + 2344)
                                                                                if (load32(v5 + 2344) < load32(v5 + 312)):
                                                                                    break
                                                                                arg0 = (arg1 <= load32(v5 + 320))
                                                                                break
                                                                            arg4 = (v5 + 172)
                                                                            if not load32(v5 + 160):
                                                                                store32(v5 + 180, arg0)
                                                                                store32(v5 + 176, load32(v5 + 2344))
                                                                                func273(v20, 0, (arg1 + 352), arg1, v5, arg4)
                                                                                break
                                                                            arg2 = (v5 + 136)
                                                                            arg1 = call_table(load32(52348))
                                                                            if (load32(v5 + 140) == 1):
                                                                                if (arg1 & 1):
                                                                                    # TODO: memory.copy
                                                                                    store32(v5 + 180, arg0)
                                                                                    store32(v5 + 172, load32(v5 + 164))
                                                                                    store32(v5 + 176, load32(v5 + 2344))
                                                                                    while True:  # $label138
                                                                                        if (load32(v5 + 160) == 2):
                                                                                            arg1 = load32(v5 + 2348)
                                                                                            store32(v5 + 2348, load32(v5 + 188))
                                                                                            store32(v5 + 188, arg1)
                                                                                            break
                                                                                        func273((v5 + 136), (v5 + 192), v22, 108, v5, arg4)
                                                                                        break
                                                                                    if arg0:
                                                                                        arg0 = load32(v5 + 2304)
                                                                                        store32(v5 + 2304, load32(v5 + 184))
                                                                                        store32(v5 + 184, arg0)
                                                                                    arg0 = (load32(v5 + 164) + 1)
                                                                                    store32(v5 + 164, ((load32(v5 + 164) + 1) if (arg0 != load32(v5 + 168)) else 0))
                                                                                else:
                                                                                break
                                                                            a_c()
                                                                            raise Unreachable()
                                                                            break
                                                                        if not 2263:
                                                                            v20 = 0
                                                                            if load32(v5):
                                                                                break
                                                                            store32(v5 + 8, 8308)
                                                                            store64(v5, 6)
                                                                            break
                                                                        v18 = (load32(v5 + 2344) + 1)
                                                                        store32(v5 + 2344, (load32(v5 + 2344) + 1))
                                                                        if (v18 < load32(v5 + 320)):
                                                                            continue
                                                                        break
                                                                while True:  # $label140
                                                                    if (load32(v5 + 160) <= 0):
                                                                        break
                                                                    if call_table(load32(52348)):
                                                                        break
                                                                    v20 = 0
                                                                    break
                                                                    break
                                                                v20 = 1
                                                                break
                                                                break
                                                            a_c()
                                                            raise Unreachable()
                                                            break
                                                        v20 = 0
                                                        if load32(v5):
                                                            break
                                                        store32(v5 + 8, 8359)
                                                        store64(v5, 7)
                                                        break
                                                    arg0 = 1
                                                    if (load32(v5 + 160) > 0):
                                                        arg0 = call_table(load32(52348))
                                                    arg1 = load32(v22 + 52)
                                                    if load32(v22 + 52):
                                                    if (arg0 & v20):
                                                        break
                                                    break
                                                func450(v5)
                                                store64(v5 + 16, 0)
                                                store64(v5 + 2332, 0)
                                                store64(v5 + 24, 0)
                                                store64(v5 + 32, 0)
                                                store64(v5 + 40, 0)
                                                break
                                            break
                                        v18 = 0
                                        store32(v39, 0)
                                        break
                                    if v18:
                                        break
                                arg3 = load32(v5)
                                break
                            if v5:
                                func450(v5)
                                store64(v5 + 16, 0)
                                store64(v5 + 2332, 0)
                                store64(v5 + 24, 0)
                                store64(v5 + 32, 0)
                                store64(v5 + 40, 0)
                                store32(v5 + 4, 0)
                            break
                        v8 = func134(1, 288)
                        if func134(1, 288):
                            store64(v8, 8589934592)
                            func453()
                        if not v8:
                            break
                        arg3 = (v14 + 48)
                        while True:  # $label143
                            if not v8:
                                break
                            while True:  # $label144
                                if not arg3:
                                    # br_table load32(v8)
                                    break
                                store32(v8, 0)
                                store32(v8 + 8, arg3)
                                arg1 = (v8 + 24)
                                while True:  # $label148
                                    while True:  # $label146
                                        while True:  # $label145
                                            if (func39(arg1, 8) != 47):
                                                break
                                            arg2 = func39(arg1, 14)
                                            arg0 = func39(arg1, 14)
                                            if func39(arg1, 3):
                                                break
                                            if not load32(v8 + 48):
                                                break
                                            break
                                        while True:  # $label147
                                            # br_table load32(v8)
                                            break
                                            break
                                        store32(v8, 3)
                                        break
                                        break
                                    store32(v8 + 4, 2)
                                    arg1 = (arg0 + 1)
                                    store32(arg3 + 4, (arg0 + 1))
                                    arg0 = (arg2 + 1)
                                    store32(arg3, (arg2 + 1))
                                    v10 = 1
                                    if func153(arg0, arg1, 1, v8, 0):
                                        break
                                    break
                                func191(v8)
                                v10 = 0
                                if load32(v8):
                                    break
                                a_c()
                                raise Unreachable()
                                break
                            store32(v8, 2)
                            break
                        while True:  # $label149
                            if v10:
                                arg3 = func451(load32(v14 + 48), load32(v14 + 52), load32(v26 + 20), load32(v26))
                                if func451(load32(v14 + 48), load32(v14 + 52), load32(v26 + 20), load32(v26)):
                                    break
                                arg3 = 0
                                while True:  # $label150
                                    if not v8:
                                        break
                                    while True:  # $label164
                                        while True:  # $label159
                                            while True:  # $label158
                                                while True:  # $label155
                                                    while True:  # $label154
                                                        while True:  # $label153
                                                            while True:  # $label152
                                                                while True:  # $label151
                                                                    if load32(v8 + 172):
                                                                        if not load32(v8 + 168):
                                                                            break
                                                                        if (load32(v8 + 164) <= 0):
                                                                            break
                                                                        v16 = load32(v8 + 8)
                                                                        if not load32(v8 + 8):
                                                                            break
                                                                        v13 = load32(v16 + 40)
                                                                        if not load32(v16 + 40):
                                                                            break
                                                                        while True:  # $label157
                                                                            while True:  # $label156
                                                                                if load32(v8 + 4):
                                                                                    arg0 = load32(v13)
                                                                                    store32(v8 + 12, load32(v13))
                                                                                    if not arg0:
                                                                                        break
                                                                                    if not func447(load32(v13 + 20), v16, 3):
                                                                                        arg1 = 2
                                                                                        # br_table load32(v8)
                                                                                        break
                                                                                    arg0 = load32(v8 + 100)
                                                                                    arg1 = load32(v16)
                                                                                    if (load32(v8 + 100) > load32(v16)):
                                                                                        break
                                                                                    v40 = (load32(v8 + 104) * i32(arg0))
                                                                                    arg0 = (arg1 & 65535)
                                                                                    arg1 = func58(((load32(v8 + 104) * i32(arg0)) + (i32((arg1 & 65535)) + (i32(arg1) << 4))), 4)
                                                                                    store32(v8 + 16, func58(((load32(v8 + 104) * i32(arg0)) + (i32((arg1 & 65535)) + (i32(arg1) << 4))), 4))
                                                                                    if not arg1:
                                                                                        store32(v8 + 20, 0)
                                                                                        arg1 = 1
                                                                                        # br_table load32(v8)
                                                                                        break
                                                                                    store32(v8 + 20, ((arg1 + (i32(v40) << 2)) + (arg0 << 2)))
                                                                                    while True:  # $label161
                                                                                        while True:  # $label160
                                                                                            if load32(v16 + 92):
                                                                                                v7 = load32(v16 + 100)
                                                                                                arg4 = load32(v16 + 16)
                                                                                                arg0 = load32(v16 + 12)
                                                                                                arg1 = 1
                                                                                                arg2 = load32(v16 + 96)
                                                                                                v41 = i32(load32(v16 + 96))
                                                                                                v40 = (i32(load32(v16 + 96)) << 5)
                                                                                                v15 = func58((((i32(load32(v16 + 96)) << 5) + (v41 << 2)) + 84), 1)
                                                                                                if not func58((((i32(load32(v16 + 96)) << 5) + (v41 << 2)) + 84), 1):
                                                                                                    # br_table load32(v8)
                                                                                                    break
                                                                                                if load32(v8 + 280):
                                                                                                    break
                                                                                                store32(v8 + 284, v15)
                                                                                                store32(v8 + 280, v15)
                                                                                                arg0 = (v15 + 84)
                                                                                                if not func90(v15, arg0, arg4, ((v15 + 84) + i32(v40)), arg2, v7, 0, 4, arg0):
                                                                                                    break
                                                                                                if load32(v16 + 92):
                                                                                                    break
                                                                                            arg1 = load32(load32(v8 + 12))
                                                                                            if (u32((load32(load32(v8 + 12)) - 11)) < u32(-4)):
                                                                                                break
                                                                                            break
                                                                                        func188()
                                                                                        arg1 = load32(load32(v8 + 12))
                                                                                        break
                                                                                    while True:  # $label162
                                                                                        if (u32(arg1) < u32(11)):
                                                                                            break
                                                                                        arg0 = load32(52304)
                                                                                        if (load32(52304) != load32(52336)):
                                                                                            store32(9688020, 406)
                                                                                            store32(9688016, 407)
                                                                                            store32(9688004, 408)
                                                                                            store32(9688008, 409)
                                                                                            store32(9688012, 410)
                                                                                            store32(52336, arg0)
                                                                                        if not load32(load32(v8 + 12) + 28):
                                                                                            break
                                                                                        func188()
                                                                                        break
                                                                                    while True:  # $label163
                                                                                        if not load32(v8 + 56):
                                                                                            break
                                                                                        if (load32(v8 + 120) <= 0):
                                                                                            break
                                                                                        arg0 = (v8 + 136)
                                                                                        if load32((v8 + 136)):
                                                                                            break
                                                                                        if func455(arg0, load32(v8 + 132)):
                                                                                            break
                                                                                        arg1 = 1
                                                                                        # br_table load32(v8)
                                                                                        break
                                                                                        break
                                                                                    store32(v8 + 4, 0)
                                                                                if not func275(v8, load32(v8 + 16), load32(v8 + 100), load32(v8 + 104), load32(v16 + 88), 278):
                                                                                    break
                                                                                store32(v13 + 16, load32(v8 + 116))
                                                                                break
                                                                                break
                                                                            store32(v8, arg1)
                                                                            break
                                                                        func191(v8)
                                                                        if not load32(v8):
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
                                    break
                                if 4800:
                                    break
                            arg3 = load32(v8)
                            break
                        func190(v8)
                        break
                    if arg3:
                        arg0 = load32(v26)
                        if load32(v26):
                            if (load32(arg0 + 12) <= 0):
                            store32(arg0 + 80, 0)
                        break
                    arg0 = load32(v26 + 20)
                    if not load32(v26 + 20):
                        break
                    if not load32(arg0 + 48):
                        break
                    v7 = load32(v26)
                    if load32(v26):
                        arg4 = load32(v7 + 16)
                        arg2 = load32(v7 + 8)
                        while True:  # $label166
                            while True:  # $label165
                                if (u32(load32(v7)) <= u32(10)):
                                    arg0 = (v7 + 20)
                                    v10 = load32((v7 + 20))
                                    store32(v7 + 16, (arg4 + (load32((v7 + 20)) * (arg2 - 1))))
                                    break
                                arg0 = load32(v7 + 32)
                                store32(v7 + 32, (0 - load32(v7 + 32)))
                                arg3 = load32(v7 + 36)
                                store32(v7 + 36, (0 - load32(v7 + 36)))
                                arg1 = load32(v7 + 40)
                                store32(v7 + 40, (0 - load32(v7 + 40)))
                                v40 = (i32(arg2) - 1)
                                arg2 = i32((i32(arg2) - 1))
                                store32(v7 + 16, (arg4 + (arg0 * i32((i32(arg2) - 1)))))
                                arg0 = i32(((v40 & 0xFFFFFFFF) >> 1))
                                store32(v7 + 20, (load32(v7 + 20) + (arg3 * i32(((v40 & 0xFFFFFFFF) >> 1)))))
                                store32(v7 + 24, (load32(v7 + 24) + (arg0 * arg1)))
                                arg1 = load32(v7 + 28)
                                if not load32(v7 + 28):
                                    break
                                arg0 = (v7 + 44)
                                v10 = load32((v7 + 44))
                                store32(v7 + 28, (arg1 + (load32((v7 + 44)) * arg2)))
                                break
                            store32(arg0, (0 - v10))
                            break
                    break
                G.global0 = (v14 + 160)
                break
                break
            a_c()
            raise Unreachable()
            break
        break
    G.global0 = (v23 + 144)
    return 3738

# ----------------------------------------------------------
# $func450
# ----------------------------------------------------------
def func450(arg0):
    if arg0:
        store64(arg0 + 2404, 0)
        v1 = load32(arg0 + 2388)
        if load32(arg0 + 2388):
            func190(load32(v1 + 20))
            store32(v1 + 20, 0)
        store32(arg0 + 2388, 0)
        return
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func451
# ----------------------------------------------------------
def func451(arg0, arg1, arg2, arg3):
    v9 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = 2
    while True:  # $label0
        if (arg1 <= 0):
            break
        if (arg0 <= 0):
            break
        if not arg3:
            break
        while True:  # $label1
            if not arg2:
                break
            if load32(arg2 + 8):
                v5 = arg0
                v6 = arg1
                arg0 = load32(arg2 + 20)
                arg1 = load32(arg2 + 24)
                while True:  # $label2
                    v7 = (load32(arg2 + 12) & -2)
                    v8 = (load32(arg2 + 16) & -2)
                    if (((load32(arg2 + 12) & -2) | (load32(arg2 + 16) & -2)) < 0):
                        break
                    if (arg0 <= 0):
                        break
                    if (arg1 <= 0):
                        break
                    v10 = ((((((arg0 <= v5) & (v5 > v7)) & ((v5 - v7) >= arg0)) & (v6 > v8)) & (arg1 <= v6)) & ((v6 - v8) >= arg1))
                    break
                if not v10:
                    break
            if not load32(arg2 + 28):
                break
            store32(v9 + 12, load32(arg2 + 32))
            store32(v9 + 8, load32(arg2 + 36))
            if not func444(arg0, arg1, (v9 + 12), (v9 + 8)):
                break
            arg1 = load32(v9 + 8)
            arg0 = load32(v9 + 12)
            break
        store32(arg3 + 8, arg1)
        store32(arg3 + 4, arg0)
        if (arg0 <= 0):
            break
        if (arg1 <= 0):
            break
        v5 = load32(arg3)
        if (u32(load32(arg3)) > u32(12)):
            break
        while True:  # $label3
            if (load32(arg3 + 12) > 0):
                break
            if load32(arg3 + 80):
                break
            v12 = i32(arg0)
            v6 = load8u((v5 + 10296))
            if (u32((i32(arg0) * i32(load8u((v5 + 10296))))) > u32(2147483647)):
                break
            v13 = i32(arg1)
            v10 = (arg0 * v6)
            v14 = (i32(arg1) * i32((arg0 * v6)))
            v4 = 1
            while True:  # $label4
                if (u32(v5) < u32(11)):
                    v12 = 0
                    arg0 = 0
                    break
                v6 = (v5 == 12)
                v12 = ((v12 * v13) if (v5 == 12) else 0)
                v11 = (arg0 if v6 else 0)
                arg0 = (((arg0 + 1) & 0xFFFFFFFF) >> 1)
                break
            v13 = (i32((((arg0 + 1) & 0xFFFFFFFF) >> 1)) * i32((((arg1 + 1) & 0xFFFFFFFF) >> 1)))
            v15 = ((i32((((arg0 + 1) & 0xFFFFFFFF) >> 1)) * i32((((arg1 + 1) & 0xFFFFFFFF) >> 1))) << 1)
            arg1 = func58((((i32((((arg0 + 1) & 0xFFFFFFFF) >> 1)) * i32((((arg1 + 1) & 0xFFFFFFFF) >> 1))) << 1) + (v12 + v14)), 1)
            if not func58((((i32((((arg0 + 1) & 0xFFFFFFFF) >> 1)) * i32((((arg1 + 1) & 0xFFFFFFFF) >> 1))) << 1) + (v12 + v14)), 1):
                break
            store32(arg3 + 16, arg1)
            store32(arg3 + 80, arg1)
            v6 = i32(v14)
            if (u32(v5) >= u32(11)):
                store32(arg3 + 48, v6)
                store32(arg3 + 32, v10)
                v4 = i32(v13)
                store32(arg3 + 52, i32(v13))
                store32(arg3 + 36, arg0)
                arg1 = (arg1 + v6)
                store32(arg3 + 20, (arg1 + v6))
                store32(arg3 + 56, v4)
                store32(arg3 + 40, arg0)
                store32(arg3 + 24, (arg1 + v4))
                if (v5 == 12):
                    store32(arg3 + 28, (arg1 + i32(v15)))
                store32(arg3 + 44, v11)
                store32(arg3 + 60, v12)
                break
            store32(arg3 + 24, v6)
            store32(arg3 + 20, v10)
            break
        v6 = 2
        while True:  # $label5
            arg1 = load32(arg3)
            if (u32(load32(arg3)) > u32(12)):
                break
            v5 = load32(arg3 + 8)
            arg0 = load32(arg3 + 4)
            while True:  # $label7
                while True:  # $label6
                    if (u32(arg1) >= u32(11)):
                        v4 = load32(arg3 + 40)
                        v4 = (v4 >> 31)
                        v10 = ((load32(arg3 + 40) ^ (v4 >> 31)) - v4)
                        v4 = ((arg0 + 1) // 2)
                        v7 = load32(arg3 + 36)
                        v7 = (v7 >> 31)
                        v7 = ((load32(arg3 + 36) ^ (v7 >> 31)) - v7)
                        v8 = load32(arg3 + 32)
                        v8 = (v8 >> 31)
                        v8 = ((load32(arg3 + 32) ^ (v8 >> 31)) - v8)
                        v12 = i32(arg0)
                        v14 = i32((v5 - 1))
                        v13 = i32(v4)
                        v15 = i32((((v5 + 1) // 2) - 1))
                        v5 = (((((((load32(arg3 + 40) ^ (v4 >> 31)) - v4) >= ((arg0 + 1) // 2)) & ((((load32(arg3 + 36) ^ (v7 >> 31)) - v7) >= v4) & ((((load32(arg3 + 32) ^ (v8 >> 31)) - v8) >= arg0) & (((u32(load32(arg3 + 48)) >= u32((i32(arg0) + (i32((v5 - 1)) * i32(v8))))) & (u32(load32(arg3 + 52)) >= u32((i32(v4) + (i32((((v5 + 1) // 2) - 1)) * i32(v7)))))) & (u32(load32(arg3 + 56)) >= u32(((i32(v10) * v15) + v13))))))) & (load32(arg3 + 16) != 0)) & (load32(arg3 + 20) != 0)) & (load32(arg3 + 24) != 0))
                        if (arg1 != 12):
                            break
                        arg1 = load32(arg3 + 44)
                        arg1 = (arg1 >> 31)
                        arg1 = ((load32(arg3 + 44) ^ (arg1 >> 31)) - arg1)
                        if ((((arg0 <= ((load32(arg3 + 44) ^ (arg1 >> 31)) - arg1)) & (u32(load32(arg3 + 60)) >= u32(((i32(arg1) * v14) + v12)))) & (load32(arg3 + 28) != 0)) & v5):
                            break
                        break
                    v4 = load32(arg3 + 20)
                    v4 = (v4 >> 31)
                    v4 = ((load32(arg3 + 20) ^ (v4 >> 31)) - v4)
                    arg1 = load8u((arg1 + 10296))
                    if (((((load32(arg3 + 20) ^ (v4 >> 31)) - v4) >= (arg0 * load8u((arg1 + 10296)))) & (u32(load32(arg3 + 24)) >= u32(((i32((v5 - 1)) * i32(v4)) + (i32(arg0) * i32(arg1)))))) & (load32(arg3 + 16) != 0)):
                        break
                    break
                    break
                if not v5:
                    break
                break
            v6 = 0
            break
        v4 = v6
        if not arg2:
            break
        if v4:
            break
        if not load32(arg2 + 48):
            v4 = 0
            break
        arg2 = load32(arg3 + 16)
        v5 = load32(arg3 + 8)
        while True:  # $label8
            if (u32(load32(arg3)) <= u32(10)):
                arg0 = (arg3 + 20)
                arg1 = load32((arg3 + 20))
                store32(arg3 + 16, (arg2 + (load32((arg3 + 20)) * (v5 - 1))))
                break
            v4 = 0
            arg0 = load32(arg3 + 32)
            store32(arg3 + 32, (0 - load32(arg3 + 32)))
            arg1 = load32(arg3 + 36)
            store32(arg3 + 36, (0 - load32(arg3 + 36)))
            v6 = load32(arg3 + 40)
            store32(arg3 + 40, (0 - load32(arg3 + 40)))
            v12 = (i32(v5) - 1)
            v5 = i32((i32(v5) - 1))
            store32(arg3 + 16, (arg2 + (arg0 * i32((i32(v5) - 1)))))
            arg0 = i32(((v12 & 0xFFFFFFFF) >> 1))
            store32(arg3 + 20, (load32(arg3 + 20) + (arg1 * i32(((v12 & 0xFFFFFFFF) >> 1)))))
            store32(arg3 + 24, (load32(arg3 + 24) + (arg0 * v6)))
            arg2 = load32(arg3 + 28)
            if not load32(arg3 + 28):
                break
            arg0 = (arg3 + 44)
            arg1 = load32((arg3 + 44))
            store32(arg3 + 28, (arg2 + (load32((arg3 + 44)) * v5)))
            break
        v4 = 0
        store32(arg0, (0 - arg1))
        break
    G.global0 = (v9 + 16)
    return v4

# ----------------------------------------------------------
# $func452
# ----------------------------------------------------------
def func452(arg0, arg1):
    store32(arg1 + 8, 0)
    store32(arg1 + 16, arg1)
    v3 = func58(i32(arg0), 4)
    if func58(i32(arg0), 4):
        store32(arg1 + 4, v3)
        v2 = 1
    else:
    store32(arg0 + 12, 0)
    store32(arg1, v3)
    return v2

# ----------------------------------------------------------
# $func453
# ----------------------------------------------------------
def func453():
    v0 = load32(52304)
    if (load32(52304) != load32(52316)):
        store32(9687724, 344)
        store32(9687720, 344)
        store32(9687716, 345)
        store32(9687712, 346)
        store32(9687708, 347)
        store32(9687704, 348)
        store32(9687700, 349)
        store32(9687696, 350)
        store32(9687692, 351)
        store32(9687688, 352)
        store32(9687684, 353)
        store32(9687680, 354)
        store32(9687676, 355)
        store32(9687672, 356)
        store32(9687668, 357)
        store32(9687664, 344)
        store32(9687660, 358)
        store32(9687656, 358)
        store32(9687652, 359)
        store32(9687648, 360)
        store32(9687644, 361)
        store32(9687640, 362)
        store32(9687636, 363)
        store32(9687632, 364)
        store32(9687628, 365)
        store32(9687624, 366)
        store32(9687620, 367)
        store32(9687616, 368)
        store32(9687612, 369)
        store32(9687608, 370)
        store32(9687604, 371)
        store32(9687600, 358)
        store32(9687788, 358)
        store32(9687784, 358)
        store32(9687780, 359)
        store32(9687776, 360)
        store32(9687772, 361)
        store32(9687768, 362)
        store32(9687764, 363)
        store32(9687760, 364)
        store32(9687756, 365)
        store32(9687752, 366)
        store32(9687748, 367)
        store32(9687744, 368)
        store32(9687740, 369)
        store32(9687736, 370)
        store32(9687732, 371)
        store32(9687728, 358)
        store32(9687572, 372)
        store32(9687792, 373)
        store32(9687580, 374)
        store32(9687576, 375)
        store32(9687584, 376)
        store32(9687588, 377)
        store32(9687592, 378)
        store32(9687796, 379)
        store32(9687568, 380)
        store32(52316, v0)

# ----------------------------------------------------------
# $func454
# ----------------------------------------------------------
def func454(arg0, arg1, arg2, arg3):
    while True:  # $label12
        while True:  # $label13
            while True:  # $label0
                while True:  # $label11
                    while True:  # $label6
                        while True:  # $label10
                            while True:  # $label5
                                while True:  # $label9
                                    while True:  # $label4
                                        while True:  # $label8
                                            while True:  # $label3
                                                while True:  # $label2
                                                    while True:  # $label7
                                                        while True:  # $label1
                                                            # br_table arg2
                                                            break
                                                            break
                                                        return
                                                        break
                                                    break
                                                    break
                                                return
                                                break
                                            # TODO: memory.copy
                                            return
                                            break
                                        # TODO: memory.copy
                                        break
                                        break
                                    if (arg1 <= 0):
                                        break
                                    arg2 = (arg0 + (arg1 << 2))
                                    while True:  # $label14
                                        arg1 = load32(arg0)
                                        store32(arg3, (((load32(arg0) << 24) | ((arg1 & 65280) << 8)) | ((((arg1 & 0xFFFFFFFF) >> 8) & 65280) | ((arg1 & 0xFFFFFFFF) >> 24))))
                                        arg3 = (arg3 + 4)
                                        arg0 = (arg0 + 4)
                                        if (u32((arg0 + 4)) < u32(arg2)):
                                            continue
                                        break
                                    break
                                    break
                                if (arg1 > 0):
                                    v5 = (arg0 + (arg1 << 2))
                                    arg2 = arg3
                                    while True:  # $label15
                                        v4 = load32(arg0)
                                        store32(arg2, (((load32(arg0) << 24) | ((v4 & 65280) << 8)) | ((((v4 & 0xFFFFFFFF) >> 8) & 65280) | ((v4 & 0xFFFFFFFF) >> 24))))
                                        arg2 = (arg2 + 4)
                                        arg0 = (arg0 + 4)
                                        if (u32((arg0 + 4)) < u32(v5)):
                                            continue
                                        break
                                return
                                break
                            return
                            break
                        return
                        break
                    return
                    break
                a_c()
                raise Unreachable()
                break
            break
        return
        break

# ----------------------------------------------------------
# $func455
# ----------------------------------------------------------
def func455(arg0, arg1):
    v3 = func134(i32((1 << arg1)), 4)
    while True:  # $label0
        if arg0:
            if (arg1 <= 0):
                break
            if v3:
                store32(arg0 + 8, arg1)
                store32(arg0 + 4, (32 - arg1))
                v2 = 1
            store32(arg0, v3)
            return v2
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 2481

# ----------------------------------------------------------
# $func456
# ----------------------------------------------------------
def func456(arg0, arg1):
    while True:  # $label1
        while True:  # $label0
            if arg0:
                if not arg1:
                    break
                v2 = load32(arg0 + 8)
                if (load32(arg0 + 8) != load32(arg1 + 8)):
                    break
                # TODO: memory.copy
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
# $func457
# ----------------------------------------------------------
def func457(arg0, arg1, arg2, arg3):
    v9 = (G.global0 - 1024)
    G.global0 = (G.global0 - 1024)
    v6 = func276(0, arg1, arg2, arg3, 0)
    if (arg3 < 2329):
        while True:  # $label1
            while True:  # $label0
                if not arg0:
                    break
                if not v6:
                    break
                v4 = load32(arg0 + 16)
                v7 = load32(load32(arg0 + 16) + 4)
                v8 = load32(v4 + 12)
                if (u32((load32(load32(arg0 + 16) + 4) + (v6 << 2))) >= u32((load32(v4) + (load32(v4 + 12) << 2)))):
                    v4 = 0
                    v5 = func58(1, 16)
                    if not func58(1, 16):
                        break
                    v8 = (v6 if (v6 > v8) else v8)
                    v7 = func58(i32((v6 if (v6 > v8) else v8)), 4)
                    if not func58(i32((v6 if (v6 > v8) else v8)), 4):
                        break
                    store32(v5 + 8, 0)
                    store32(v5 + 4, v7)
                    store32(v5, v7)
                    store32(v5 + 12, v8)
                    store32(load32(arg0 + 16) + 8, v5)
                    store32(arg0 + 16, v5)
                if (arg3 <= 512):
                    break
                v4 = func58(i32(arg3), 2)
                if not func58(i32(arg3), 2):
                    v4 = 0
                    break
                break
            v4 = v6
            break
        G.global0 = (v9 + 1024)
        return v4
    a_c()
    raise Unreachable()
    return 4778

# ----------------------------------------------------------
# $func458
# ----------------------------------------------------------
def func458(arg0, arg1):
    while True:  # $label0
        if not arg0:
            break
        store32(arg0 + 8, 6932)
        store32(arg0, 0)
        if not arg1:
            store32(arg0 + 8, 8788)
            store64(arg0, 2)
            break
        while True:  # $label2
            while True:  # $label1
                v10 = load32(arg1 + 60)
                if (u32(load32(arg1 + 60)) <= u32(3)):
                    store32(arg0 + 8, 8211)
                    break
                v2 = load32(arg1 + 64)
                v3 = load8u(load32(arg1 + 64) + 1)
                v8 = load8u(v2 + 2)
                v4 = load8u(v2)
                v5 = (((load8u(v2) & 0xFFFFFFFF) >> 4) & 1)
                store8(arg0 + 54, (((load8u(v2) & 0xFFFFFFFF) >> 4) & 1))
                v11 = (((v4 & 0xFFFFFFFF) >> 1) & 7)
                store8(arg0 + 53, (((v4 & 0xFFFFFFFF) >> 1) & 7))
                v12 = (v4 & 1)
                store8(arg0 + 52, not (v4 & 1))
                v8 = (((v4 | ((v3 << 8) | (v8 << 16))) & 0xFFFFFFFF) >> 5)
                store32(arg0 + 56, (((v4 | ((v3 << 8) | (v8 << 16))) & 0xFFFFFFFF) >> 5))
                if (u32(v11) >= u32(4)):
                    store32(arg0 + 8, 8180)
                    break
                if not v5:
                    store32(arg0 + 8, 8285)
                    store64(arg0, 4)
                    break
                v4 = (v10 - 3)
                v3 = (v2 + 3)
                if not v12:
                    if (u32(v4) <= u32(6)):
                        store32(arg0 + 8, 3600)
                        break
                    while True:  # $label4
                        while True:  # $label3
                            if (load8u(v3) != 157):
                                break
                            if (load8u(v2 + 4) != 1):
                                break
                            if (load8u(v2 + 5) == 42):
                                break
                            break
                        store32(arg0 + 8, 4952)
                        break
                        break
                    v4 = (load8u(v2 + 6) | ((load8u(v2 + 7) << 8) & 16128))
                    store16(arg0 + 60, (load8u(v2 + 6) | ((load8u(v2 + 7) << 8) & 16128)))
                    store8((arg0 - -64), ((load8u(v2 + 7) & 0xFFFFFFFF) >> 6))
                    v3 = (load8u(v2 + 8) | ((load8u(v2 + 9) << 8) & 16128))
                    store16(arg0 + 62, (load8u(v2 + 8) | ((load8u(v2 + 9) << 8) & 16128)))
                    v8 = load8u(v2 + 9)
                    store32(arg0 + 304, (((v3 + 15) & 0xFFFFFFFF) >> 4))
                    store32(arg0 + 300, (((v4 + 15) & 0xFFFFFFFF) >> 4))
                    store8(arg0 + 65, ((v8 & 0xFFFFFFFF) >> 6))
                    store32(arg1 + 84, 0)
                    store32(arg1 + 4, v3)
                    store32(arg1, v4)
                    store32(arg1 + 100, v3)
                    store32(arg1 + 96, v4)
                    store32(arg1 + 92, 0)
                    store32(arg1 + 88, v3)
                    store32(arg1 + 80, v4)
                    store64(arg1 + 72, 0)
                    store32(arg1 + 16, v3)
                    store32(arg1 + 12, v4)
                    store16(arg0 + 948, 65535)
                    store8(arg0 + 950, 255)
                    store32(arg0 + 132, 0)
                    store64(arg0 + 124, 1)
                    store64(arg0 + 116, 0)
                    v3 = (v2 + 10)
                    v8 = load32(arg0 + 56)
                    v4 = (v10 - 10)
                while True:  # $label5
                    if (u32(v4) < u32(v8)):
                        if load32(arg0):
                            break
                        store32(arg0 + 8, 4209)
                        break
                    arg1 = (arg0 + 16)
                    func270((arg0 + 16), v3, v8)
                    v5 = load32(arg0 + 56)
                    if load8u(arg0 + 52):
                        store8(arg0 + 66, func33(arg1, 1))
                        store8(arg0 + 67, func33(arg1, 1))
                    v2 = func33(arg1, 1)
                    store32(arg0 + 116, func33(arg1, 1))
                    while True:  # $label6
                        if v2:
                            store32(arg0 + 120, func33(arg1, 1))
                            if func33(arg1, 1):
                                store32(arg0 + 124, func33(arg1, 1))
                                if func33(arg1, 1):
                                else:
                                store8(func51(arg1, 7) + 128, 0)
                                if func33(arg1, 1):
                                else:
                                store8(func51(arg1, 7) + 129, 0)
                                if func33(arg1, 1):
                                else:
                                store8(func51(arg1, 7) + 130, 0)
                                if func33(arg1, 1):
                                else:
                                store8(func51(arg1, 7) + 131, 0)
                                if func33(arg1, 1):
                                else:
                                store8(func51(arg1, 6) + 132, 0)
                                if func33(arg1, 1):
                                else:
                                store8(func51(arg1, 6) + 133, 0)
                                if func33(arg1, 1):
                                else:
                                store8(func51(arg1, 6) + 134, 0)
                                if func33(arg1, 1):
                                else:
                                store8(func51(arg1, 6) + 135, 0)
                            if not load32(arg0 + 120):
                                break
                            if func33(arg1, 1):
                            else:
                            store8(func33(arg1, 8) + 948, 255)
                            if func33(arg1, 1):
                            else:
                            store8(func33(arg1, 8) + 949, 255)
                            if func33(arg1, 1):
                            else:
                            store8(func33(arg1, 8) + 950, 255)
                            break
                        store32(arg0 + 120, 0)
                        break
                    if load32(arg0 + 44):
                        if load32(arg0):
                            break
                        store32(arg0 + 8, 3545)
                        break
                    store32(arg0 + 68, func33(arg1, 1))
                    store32(arg0 + 72, func33(arg1, 6))
                    store32(arg0 + 76, func33(arg1, 3))
                    v2 = func33(arg1, 1)
                    store32(arg0 + 80, func33(arg1, 1))
                    while True:  # $label7
                        if not v2:
                            break
                        if not func33(arg1, 1):
                            break
                        if func33(arg1, 1):
                            store32(arg0 + 84, func51(arg1, 6))
                        if func33(arg1, 1):
                            store32(arg0 + 88, func51(arg1, 6))
                        if func33(arg1, 1):
                            store32(arg0 + 92, func51(arg1, 6))
                        if func33(arg1, 1):
                            store32(arg0 + 96, func51(arg1, 6))
                        if func33(arg1, 1):
                            store32(arg0 + 100, func51(arg1, 6))
                        if func33(arg1, 1):
                            store32(arg0 + 104, func51(arg1, 6))
                        if func33(arg1, 1):
                            store32(arg0 + 108, func51(arg1, 6))
                        if not func33(arg1, 1):
                            break
                        store32(arg0 + 112, func51(arg1, 6))
                        break
                    if load32(arg0 + 72):
                    else:
                    store32((1 if load32(arg0 + 68) else 2) + 2352, 0)
                    if load32(arg1 + 28):
                        if load32(arg0):
                            break
                        store32(arg0 + 8, 3573)
                        break
                    v2 = (v3 + v5)
                    v10 = 0
                    v11 = func33((arg0 + 16), 2)
                    v8 = ((-1 << func33((arg0 + 16), 2)) ^ -1)
                    store32(arg0 + 324, ((-1 << func33((arg0 + 16), 2)) ^ -1))
                    while True:  # $label8
                        v4 = (v4 - v5)
                        v3 = (v8 * 3)
                        if (u32((v4 - v5)) < u32((v8 * 3))):
                            break
                        v12 = (v2 + v4)
                        v4 = (v4 - v3)
                        v3 = (v2 + v3)
                        if v11:
                            v11 = (1 if (u32(v8) <= u32(1)) else v8)
                            v9 = (arg0 + 328)
                            while True:  # $label9
                                v5 = (load16u(v2) | (load8u(v2 + 2) << 16))
                                v5 = ((load16u(v2) | (load8u(v2 + 2) << 16)) if (u32(v4) > u32(v5)) else v4)
                                func270((v9 + (v10 << 5)), v3, ((load16u(v2) | (load8u(v2 + 2) << 16)) if (u32(v4) > u32(v5)) else v4))
                                v4 = (v4 - v5)
                                v3 = (v3 + v5)
                                v2 = (v2 + 3)
                                v10 = (v10 + 1)
                                if ((v10 + 1) != v11):
                                    continue
                                break
                        func270(((arg0 + (v8 << 5)) + 328), v3, v4)
                        if (u32(v3) < u32(v12)):
                            break
                        break
                    v2 = (5 if load32(arg0 + 48) else 7)
                    if (5 if load32(arg0 + 48) else 7):
                        break
                    v8 = 0
                    v10 = 0
                    v5 = 0
                    v11 = 0
                    v2 = (arg0 + 16)
                    v4 = func33((arg0 + 16), 7)
                    if func33(v2, 1):
                        v10 = func51(v2, 4)
                    if func33(v2, 1):
                        v8 = func51(v2, 4)
                    if func33(v2, 1):
                        v11 = func51(v2, 4)
                    if func33(v2, 1):
                        v5 = func51(v2, 4)
                    if func33(v2, 1):
                    else:
                    v12 = 0
                    v2 = v4
                    v9 = load32(arg0 + 116)
                    if load32(arg0 + 116):
                        v2 = (load8s(arg0 + 128) + (0 if load32(arg0 + 124) else v4))
                    v3 = (v2 + v12)
                    store32(arg0 + 844, (v2 + v12))
                    v6 = (v2 + v5)
                    v6 = (117 if (v6 >= 117) else (v2 + v5))
                    store32(arg0 + 836, load8u((((117 if (v6 >= 117) else (v2 + v5)) if (v6 > 0) else 0) + 10368)))
                    v6 = (127 if (v2 >= 127) else v2)
                    store32(arg0 + 824, load16u(((((127 if (v2 >= 127) else v2) if (v6 > 0) else 0) << 1) + 10496)))
                    v6 = (v2 + v10)
                    v6 = (127 if (v6 >= 127) else (v2 + v10))
                    store32(arg0 + 820, load8u((((127 if (v6 >= 127) else (v2 + v10)) if (v6 > 0) else 0) + 10368)))
                    v3 = (127 if (v3 >= 127) else v3)
                    store32(arg0 + 840, load16u(((((127 if (v3 >= 127) else v3) if (v3 > 0) else 0) << 1) + 10496)))
                    v3 = (v2 + v8)
                    v3 = (127 if (v3 >= 127) else (v2 + v8))
                    store32(arg0 + 828, (load8u((((127 if (v3 >= 127) else (v2 + v8)) if (v3 > 0) else 0) + 10368)) << 1))
                    v2 = (v2 + v11)
                    v2 = (127 if (v2 >= 127) else (v2 + v11))
                    v2 = (load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581)
                    store32(arg0 + 832, (8 if (u32(v2) < u32(524288)) else (((load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
                    while True:  # $label10
                        if not v9:
                            store64(arg0 + 852, load64(arg0 + 820))
                            store64(arg0 + 876, load64(arg0 + 844))
                            store64(arg0 + 868, load64(arg0 + 836))
                            store64(arg0 + 860, load64(arg0 + 828))
                            store64(arg0 + 884, load64(arg0 + 820))
                            store64(arg0 + 892, load64(arg0 + 828))
                            store64(arg0 + 900, load64(arg0 + 836))
                            store64(arg0 + 908, load64(arg0 + 844))
                            store64(arg0 + 916, load64(arg0 + 820))
                            store64(arg0 + 924, load64(arg0 + 828))
                            store64(arg0 + 932, load64(arg0 + 836))
                            store64(arg0 + 940, load64(arg0 + 844))
                            break
                        v3 = (0 if load32(arg0 + 124) else v4)
                        v2 = ((0 if load32(arg0 + 124) else v4) + load8s(arg0 + 129))
                        v9 = (((0 if load32(arg0 + 124) else v4) + load8s(arg0 + 129)) + v12)
                        store32(arg0 + 876, (((0 if load32(arg0 + 124) else v4) + load8s(arg0 + 129)) + v12))
                        v3 = (v3 + load8s(arg0 + 130))
                        v6 = ((v3 + load8s(arg0 + 130)) + v12)
                        store32(arg0 + 908, ((v3 + load8s(arg0 + 130)) + v12))
                        v7 = (v2 + v5)
                        v7 = (117 if (v7 >= 117) else (v2 + v5))
                        store32(arg0 + 868, load8u((((117 if (v7 >= 117) else (v2 + v5)) if (v7 > 0) else 0) + 10368)))
                        v7 = (127 if (v2 >= 127) else v2)
                        store32(arg0 + 856, load16u(((((127 if (v2 >= 127) else v2) if (v7 > 0) else 0) << 1) + 10496)))
                        v7 = (v2 + v10)
                        v7 = (127 if (v7 >= 127) else (v2 + v10))
                        store32(arg0 + 852, load8u((((127 if (v7 >= 127) else (v2 + v10)) if (v7 > 0) else 0) + 10368)))
                        v7 = (v3 + v5)
                        v7 = (117 if (v7 >= 117) else (v3 + v5))
                        store32(arg0 + 900, load8u((((117 if (v7 >= 117) else (v3 + v5)) if (v7 > 0) else 0) + 10368)))
                        v7 = (127 if (v3 >= 127) else v3)
                        store32(arg0 + 888, load16u(((((127 if (v3 >= 127) else v3) if (v7 > 0) else 0) << 1) + 10496)))
                        v7 = (v3 + v10)
                        v7 = (127 if (v7 >= 127) else (v3 + v10))
                        store32(arg0 + 884, load8u((((127 if (v7 >= 127) else (v3 + v10)) if (v7 > 0) else 0) + 10368)))
                        v9 = (127 if (v9 >= 127) else v9)
                        store32(arg0 + 872, load16u(((((127 if (v9 >= 127) else v9) if (v9 > 0) else 0) << 1) + 10496)))
                        v9 = (v2 + v8)
                        v9 = (127 if (v9 >= 127) else (v2 + v8))
                        store32(arg0 + 860, (load8u((((127 if (v9 >= 127) else (v2 + v8)) if (v9 > 0) else 0) + 10368)) << 1))
                        v9 = (127 if (v6 >= 127) else v6)
                        store32(arg0 + 904, load16u(((((127 if (v6 >= 127) else v6) if (v9 > 0) else 0) << 1) + 10496)))
                        v9 = (v3 + v8)
                        v9 = (127 if (v9 >= 127) else (v3 + v8))
                        store32(arg0 + 892, (load8u((((127 if (v9 >= 127) else (v3 + v8)) if (v9 > 0) else 0) + 10368)) << 1))
                        v2 = (v2 + v11)
                        v2 = (127 if (v2 >= 127) else (v2 + v11))
                        v2 = (load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581)
                        store32(arg0 + 864, (8 if (u32(v2) < u32(524288)) else (((load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
                        v2 = (v3 + v11)
                        v2 = (127 if (v2 >= 127) else (v3 + v11))
                        v2 = (load16u(((((127 if (v2 >= 127) else (v3 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581)
                        store32(arg0 + 896, (8 if (u32(v2) < u32(524288)) else (((load16u(((((127 if (v2 >= 127) else (v3 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
                        v2 = (load8s(arg0 + 131) + (0 if load32(arg0 + 124) else v4))
                        v4 = ((load8s(arg0 + 131) + (0 if load32(arg0 + 124) else v4)) + v12)
                        store32(arg0 + 940, ((load8s(arg0 + 131) + (0 if load32(arg0 + 124) else v4)) + v12))
                        v3 = (v2 + v10)
                        v3 = (127 if (v3 >= 127) else (v2 + v10))
                        store32(arg0 + 916, load8u((((127 if (v3 >= 127) else (v2 + v10)) if (v3 > 0) else 0) + 10368)))
                        v3 = (127 if (v2 >= 127) else v2)
                        store32(arg0 + 920, load16u(((((127 if (v2 >= 127) else v2) if (v3 > 0) else 0) << 1) + 10496)))
                        v3 = (v2 + v5)
                        v3 = (117 if (v3 >= 117) else (v2 + v5))
                        store32(arg0 + 932, load8u((((117 if (v3 >= 117) else (v2 + v5)) if (v3 > 0) else 0) + 10368)))
                        v3 = (v2 + v8)
                        v3 = (127 if (v3 >= 127) else (v2 + v8))
                        store32(arg0 + 924, (load8u((((127 if (v3 >= 127) else (v2 + v8)) if (v3 > 0) else 0) + 10368)) << 1))
                        v4 = (127 if (v4 >= 127) else v4)
                        store32(arg0 + 936, load16u(((((127 if (v4 >= 127) else v4) if (v4 > 0) else 0) << 1) + 10496)))
                        v2 = (v2 + v11)
                        v2 = (127 if (v2 >= 127) else (v2 + v11))
                        v2 = (load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581)
                        store32(arg0 + 928, (8 if (u32(v2) < u32(524288)) else (((load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
                        break
                    if not load8u(arg0 + 52):
                        if load32(arg0):
                            break
                        store32(arg0 + 8, 8268)
                        store64(arg0, 4)
                        break
                    v8 = 0
                    v11 = (arg0 + 948)
                    while True:  # $label26
                        while True:  # $label12
                            while True:  # $label25
                                v3 = 0
                                while True:  # $label24
                                    v7 = (v3 * 33)
                                    v12 = (v8 * 264)
                                    v10 = (((v3 * 33) + (arg0 + (v8 * 264))) + 951)
                                    v4 = 0
                                    while True:  # $label15
                                        v9 = (v7 + v12)
                                        v13 = ((v7 + v12) + v4)
                                        v14 = load8u((((v7 + v12) + v4) + 10752))
                                        v6 = load32(arg1 + 8)
                                        while True:  # $label11
                                            v2 = load32(arg1 + 12)
                                            if (load32(arg1 + 12) >= 0):
                                                break
                                            v5 = load32(arg1 + 16)
                                            if not load32(arg1 + 16):
                                                break
                                            if (u32(load32(arg1 + 24)) > u32(v5)):
                                                v15 = load64(v5)
                                                store32(arg1 + 16, (v5 + 7))
                                                store64(arg1, ((load64(arg1) << 56) | ((((((v15 << 56) | ((v15 & 65280) << 40)) | (((v15 & 16711680) << 24) | ((v15 & 4278190080) << 8))) | ((((v15 & 0xFFFFFFFF) >> 40) & 65280) | ((((v15 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v15 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                                v2 = (v2 + 56)
                                                break
                                            func36(arg1)
                                            v2 = load32(arg1 + 12)
                                            break
                                        while True:  # $label13
                                            v5 = (((v6 * v14) & 0xFFFFFFFF) >> 8)
                                            v15 = load64(arg1)
                                            v16 = i32(v2)
                                            v2 = (u32((((v6 * v14) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(arg1) & 0xFFFFFFFF) >> i32(v2)))))
                                            if not (u32((((v6 * v14) & 0xFFFFFFFF) >> 8)) >= u32(i32(((load64(arg1) & 0xFFFFFFFF) >> i32(v2))))):
                                                store64(arg1, (v15 - (i32((v5 + 1)) << v16)))
                                                break
                                            break
                                        v5 = (v5 + 1)
                                        v6 = (clz((v5 + 1)) ^ 24)
                                        store32(v2 + 12, ((v6 - v5) - (clz((v5 + 1)) ^ 24)))
                                        store32(arg1 + 8, ((v5 << v6) - 1))
                                        while True:  # $label14
                                            if not v2:
                                                break
                                            break
                                        store8(func33(arg1, 8), load8u((v13 + 11808)))
                                        v4 = (v4 + 1)
                                        if ((v4 + 1) != 11):
                                            continue
                                        break
                                    v4 = 0
                                    while True:  # $label19
                                        v7 = (v4 + v9)
                                        v13 = load8u(((v4 + v9) + 10763))
                                        v6 = load32(arg1 + 8)
                                        while True:  # $label16
                                            v2 = load32(arg1 + 12)
                                            if (load32(arg1 + 12) >= 0):
                                                break
                                            v5 = load32(arg1 + 16)
                                            if not load32(arg1 + 16):
                                                break
                                            if (u32(load32(arg1 + 24)) <= u32(v5)):
                                                func36(arg1)
                                                v2 = load32(arg1 + 12)
                                                break
                                            v15 = load64(v5)
                                            store32(arg1 + 16, (v5 + 7))
                                            store64(arg1, ((load64(arg1) << 56) | ((((((v15 << 56) | ((v15 & 65280) << 40)) | (((v15 & 16711680) << 24) | ((v15 & 4278190080) << 8))) | ((((v15 & 0xFFFFFFFF) >> 40) & 65280) | ((((v15 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v15 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                            v2 = (v2 + 56)
                                            break
                                        while True:  # $label17
                                            v5 = (((v6 * v13) & 0xFFFFFFFF) >> 8)
                                            v15 = load64(arg1)
                                            v16 = i32(v2)
                                            v2 = (u32((((v6 * v13) & 0xFFFFFFFF) >> 8)) < u32(i32(((load64(arg1) & 0xFFFFFFFF) >> i32(v2)))))
                                            if not (u32((((v6 * v13) & 0xFFFFFFFF) >> 8)) < u32(i32(((load64(arg1) & 0xFFFFFFFF) >> i32(v2))))):
                                                break
                                            store64(arg1, (v15 - (i32((v5 + 1)) << v16)))
                                            break
                                        v5 = (v6 - v5)
                                        v6 = (clz((v6 - v5)) ^ 24)
                                        store32(v2 + 12, ((v5 + 1) - (clz((v6 - v5)) ^ 24)))
                                        store32(arg1 + 8, ((v5 << v6) - 1))
                                        while True:  # $label18
                                            if not v2:
                                                break
                                            break
                                        store8(load8u((v7 + 11819)) + 11, func33(arg1, 8))
                                        v4 = (v4 + 1)
                                        if ((v4 + 1) != 11):
                                            continue
                                        break
                                    v4 = 0
                                    while True:  # $label23
                                        v7 = (v4 + v9)
                                        v13 = load8u(((v4 + v9) + 10774))
                                        v6 = load32(arg1 + 8)
                                        while True:  # $label20
                                            v2 = load32(arg1 + 12)
                                            if (load32(arg1 + 12) >= 0):
                                                break
                                            v5 = load32(arg1 + 16)
                                            if not load32(arg1 + 16):
                                                break
                                            if (u32(load32(arg1 + 24)) <= u32(v5)):
                                                func36(arg1)
                                                v2 = load32(arg1 + 12)
                                                break
                                            v15 = load64(v5)
                                            store32(arg1 + 16, (v5 + 7))
                                            store64(arg1, ((load64(arg1) << 56) | ((((((v15 << 56) | ((v15 & 65280) << 40)) | (((v15 & 16711680) << 24) | ((v15 & 4278190080) << 8))) | ((((v15 & 0xFFFFFFFF) >> 40) & 65280) | ((((v15 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v15 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                            v2 = (v2 + 56)
                                            break
                                        while True:  # $label21
                                            v5 = (((v6 * v13) & 0xFFFFFFFF) >> 8)
                                            v15 = load64(arg1)
                                            v16 = i32(v2)
                                            v2 = (u32((((v6 * v13) & 0xFFFFFFFF) >> 8)) < u32(i32(((load64(arg1) & 0xFFFFFFFF) >> i32(v2)))))
                                            if not (u32((((v6 * v13) & 0xFFFFFFFF) >> 8)) < u32(i32(((load64(arg1) & 0xFFFFFFFF) >> i32(v2))))):
                                                break
                                            store64(arg1, (v15 - (i32((v5 + 1)) << v16)))
                                            break
                                        v5 = (v6 - v5)
                                        v6 = (clz((v6 - v5)) ^ 24)
                                        store32(v2 + 12, ((v5 + 1) - (clz((v6 - v5)) ^ 24)))
                                        store32(arg1 + 8, ((v5 << v6) - 1))
                                        while True:  # $label22
                                            if not v2:
                                                break
                                            break
                                        store8(load8u((v7 + 11830)) + 22, func33(arg1, 8))
                                        v4 = (v4 + 1)
                                        if ((v4 + 1) != 11):
                                            continue
                                        break
                                    v3 = (v3 + 1)
                                    if ((v3 + 1) != 8):
                                        continue
                                    break
                                v2 = (v11 + (v8 * 68))
                                v3 = (v11 + v12)
                                v10 = ((v11 + v12) + 3)
                                store32(((v11 + (v8 * 68)) + 1124), ((v11 + v12) + 3))
                                store32((v2 + 1120), (v3 + 234))
                                v4 = (v3 + 201)
                                store32((v2 + 1116), (v3 + 201))
                                store32((v2 + 1112), v4)
                                store32((v2 + 1108), v4)
                                store32((v2 + 1104), v4)
                                store32((v2 + 1100), v4)
                                store32((v2 + 1096), v4)
                                store32((v2 + 1092), v4)
                                store32((v2 + 1088), v4)
                                store32((v2 + 1084), (v3 + 168))
                                store32((v2 + 1080), (v3 + 135))
                                store32((v2 + 1076), v4)
                                store32((v2 + 1072), (v3 + 102))
                                store32((v2 + 1068), (v3 + 69))
                                store32((v2 + 1064), (v3 + 36))
                                store32((v2 + 1060), v10)
                                v8 = (v8 + 1)
                                if ((v8 + 1) != 4):
                                    continue
                                break
                            v2 = func33(arg1, 1)
                            store32(arg0 + 2280, func33(arg1, 1))
                            if v2:
                                store8(arg0 + 2284, func33(arg1, 8))
                            break
                            break
                        a_c()
                        raise Unreachable()
                        break
                    store32(arg0 + 4, 1)
                    break
                return 1
                break
            store64(arg0, 7)
            break
            break
        store64(arg0, 3)
        break
    return 0

# ----------------------------------------------------------
# $func459
# ----------------------------------------------------------
def func459(arg0, arg1):
    v3 = load16s(arg0 + 10)
    v5 = load16s(arg0 + 26)
    v17 = ((((load16s(arg0 + 10) * 20091) >> 16) + v3) + ((load16s(arg0 + 26) * 35468) >> 16))
    v8 = load16s(arg0 + 18)
    v14 = load16s(arg0 + 2)
    v18 = (load16s(arg0 + 18) + load16s(arg0 + 2))
    v2 = (((((load16s(arg0 + 10) * 20091) >> 16) + v3) + ((load16s(arg0 + 26) * 35468) >> 16)) + (load16s(arg0 + 18) + load16s(arg0 + 2)))
    v6 = load16s(arg0 + 14)
    v7 = load16s(arg0 + 30)
    v19 = ((((load16s(arg0 + 14) * 20091) >> 16) + v6) + ((load16s(arg0 + 30) * 35468) >> 16))
    v15 = load16s(arg0 + 22)
    v9 = load16s(arg0 + 6)
    v20 = (load16s(arg0 + 22) + load16s(arg0 + 6))
    v4 = (((((load16s(arg0 + 14) * 20091) >> 16) + v6) + ((load16s(arg0 + 30) * 35468) >> 16)) + (load16s(arg0 + 22) + load16s(arg0 + 6)))
    v21 = (((((((((load16s(arg0 + 10) * 20091) >> 16) + v3) + ((load16s(arg0 + 26) * 35468) >> 16)) + (load16s(arg0 + 18) + load16s(arg0 + 2))) * 20091) >> 16) + v2) + (((((((load16s(arg0 + 14) * 20091) >> 16) + v6) + ((load16s(arg0 + 30) * 35468) >> 16)) + (load16s(arg0 + 22) + load16s(arg0 + 6))) * 35468) >> 16))
    v10 = load16s(arg0 + 8)
    v11 = load16s(arg0 + 24)
    v22 = ((((load16s(arg0 + 8) * 20091) >> 16) + v10) + ((load16s(arg0 + 24) * 35468) >> 16))
    v23 = load16s(arg0 + 16)
    v24 = load16s(arg0)
    v25 = (load16s(arg0 + 16) + load16s(arg0))
    v26 = ((((((load16s(arg0 + 8) * 20091) >> 16) + v10) + ((load16s(arg0 + 24) * 35468) >> 16)) + (load16s(arg0 + 16) + load16s(arg0))) + 4)
    v12 = load16s(arg0 + 12)
    v13 = load16s(arg0 + 28)
    v27 = ((((load16s(arg0 + 12) * 20091) >> 16) + v12) + ((load16s(arg0 + 28) * 35468) >> 16))
    v28 = load16s(arg0 + 20)
    v29 = load16s(arg0 + 4)
    v30 = (load16s(arg0 + 20) + load16s(arg0 + 4))
    arg0 = (((((load16s(arg0 + 12) * 20091) >> 16) + v12) + ((load16s(arg0 + 28) * 35468) >> 16)) + (load16s(arg0 + 20) + load16s(arg0 + 4)))
    v31 = (((((((load16s(arg0 + 8) * 20091) >> 16) + v10) + ((load16s(arg0 + 24) * 35468) >> 16)) + (load16s(arg0 + 16) + load16s(arg0))) + 4) + (((((load16s(arg0 + 12) * 20091) >> 16) + v12) + ((load16s(arg0 + 28) * 35468) >> 16)) + (load16s(arg0 + 20) + load16s(arg0 + 4))))
    v16 = (load8u(arg1) + (((((((((((load16s(arg0 + 10) * 20091) >> 16) + v3) + ((load16s(arg0 + 26) * 35468) >> 16)) + (load16s(arg0 + 18) + load16s(arg0 + 2))) * 20091) >> 16) + v2) + (((((((load16s(arg0 + 14) * 20091) >> 16) + v6) + ((load16s(arg0 + 30) * 35468) >> 16)) + (load16s(arg0 + 22) + load16s(arg0 + 6))) * 35468) >> 16)) + (((((((load16s(arg0 + 8) * 20091) >> 16) + v10) + ((load16s(arg0 + 24) * 35468) >> 16)) + (load16s(arg0 + 16) + load16s(arg0))) + 4) + (((((load16s(arg0 + 12) * 20091) >> 16) + v12) + ((load16s(arg0 + 28) * 35468) >> 16)) + (load16s(arg0 + 20) + load16s(arg0 + 4))))) >> 3))
    v16 = ((load8u(arg1) + (((((((((((load16s(arg0 + 10) * 20091) >> 16) + v3) + ((load16s(arg0 + 26) * 35468) >> 16)) + (load16s(arg0 + 18) + load16s(arg0 + 2))) * 20091) >> 16) + v2) + (((((((load16s(arg0 + 14) * 20091) >> 16) + v6) + ((load16s(arg0 + 30) * 35468) >> 16)) + (load16s(arg0 + 22) + load16s(arg0 + 6))) * 35468) >> 16)) + (((((((load16s(arg0 + 8) * 20091) >> 16) + v10) + ((load16s(arg0 + 24) * 35468) >> 16)) + (load16s(arg0 + 16) + load16s(arg0))) + 4) + (((((load16s(arg0 + 12) * 20091) >> 16) + v12) + ((load16s(arg0 + 28) * 35468) >> 16)) + (load16s(arg0 + 20) + load16s(arg0 + 4))))) >> 3)) if (v16 > 0) else 0)
    store8(arg1, (255 if (v16 >= 255) else ((load8u(arg1) + (((((((((((load16s(arg0 + 10) * 20091) >> 16) + v3) + ((load16s(arg0 + 26) * 35468) >> 16)) + (load16s(arg0 + 18) + load16s(arg0 + 2))) * 20091) >> 16) + v2) + (((((((load16s(arg0 + 14) * 20091) >> 16) + v6) + ((load16s(arg0 + 30) * 35468) >> 16)) + (load16s(arg0 + 22) + load16s(arg0 + 6))) * 35468) >> 16)) + (((((((load16s(arg0 + 8) * 20091) >> 16) + v10) + ((load16s(arg0 + 24) * 35468) >> 16)) + (load16s(arg0 + 16) + load16s(arg0))) + 4) + (((((load16s(arg0 + 12) * 20091) >> 16) + v12) + ((load16s(arg0 + 28) * 35468) >> 16)) + (load16s(arg0 + 20) + load16s(arg0 + 4))))) >> 3)) if (v16 > 0) else 0)))
    v2 = (((v2 * 35468) >> 16) - (v4 + ((v4 * 20091) >> 16)))
    arg0 = (v26 - arg0)
    v4 = (load8u(arg1 + 1) + (((((v2 * 35468) >> 16) - (v4 + ((v4 * 20091) >> 16))) + (v26 - arg0)) >> 3))
    v4 = ((load8u(arg1 + 1) + (((((v2 * 35468) >> 16) - (v4 + ((v4 * 20091) >> 16))) + (v26 - arg0)) >> 3)) if (v4 > 0) else 0)
    store8(arg1 + 1, (255 if (v4 >= 255) else ((load8u(arg1 + 1) + (((((v2 * 35468) >> 16) - (v4 + ((v4 * 20091) >> 16))) + (v26 - arg0)) >> 3)) if (v4 > 0) else 0)))
    arg0 = (load8u(arg1 + 2) + ((arg0 - v2) >> 3))
    arg0 = ((load8u(arg1 + 2) + ((arg0 - v2) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 2, (255 if (arg0 >= 255) else ((load8u(arg1 + 2) + ((arg0 - v2) >> 3)) if (arg0 > 0) else 0)))
    arg0 = (load8u(arg1 + 3) + ((v31 - v21) >> 3))
    arg0 = ((load8u(arg1 + 3) + ((v31 - v21) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 3, (255 if (arg0 >= 255) else ((load8u(arg1 + 3) + ((v31 - v21) >> 3)) if (arg0 > 0) else 0)))
    v5 = (((v3 * 35468) >> 16) - (v5 + ((v5 * 20091) >> 16)))
    v2 = (v14 - v8)
    arg0 = ((((v3 * 35468) >> 16) - (v5 + ((v5 * 20091) >> 16))) + (v14 - v8))
    v6 = (((v6 * 35468) >> 16) - (v7 + ((v7 * 20091) >> 16)))
    v7 = (v9 - v15)
    v3 = ((((v6 * 35468) >> 16) - (v7 + ((v7 * 20091) >> 16))) + (v9 - v15))
    v4 = ((((((((v3 * 35468) >> 16) - (v5 + ((v5 * 20091) >> 16))) + (v14 - v8)) * 20091) >> 16) + arg0) + ((((((v6 * 35468) >> 16) - (v7 + ((v7 * 20091) >> 16))) + (v9 - v15)) * 35468) >> 16))
    v10 = (((v10 * 35468) >> 16) - (v11 + ((v11 * 20091) >> 16)))
    v11 = (v24 - v23)
    v8 = (((((v10 * 35468) >> 16) - (v11 + ((v11 * 20091) >> 16))) + (v24 - v23)) + 4)
    v12 = (((v12 * 35468) >> 16) - (v13 + ((v13 * 20091) >> 16)))
    v13 = (v29 - v28)
    v14 = ((((v12 * 35468) >> 16) - (v13 + ((v13 * 20091) >> 16))) + (v29 - v28))
    v15 = ((((((v10 * 35468) >> 16) - (v11 + ((v11 * 20091) >> 16))) + (v24 - v23)) + 4) + ((((v12 * 35468) >> 16) - (v13 + ((v13 * 20091) >> 16))) + (v29 - v28)))
    v9 = (load8u(arg1 + 32) + ((((((((((v3 * 35468) >> 16) - (v5 + ((v5 * 20091) >> 16))) + (v14 - v8)) * 20091) >> 16) + arg0) + ((((((v6 * 35468) >> 16) - (v7 + ((v7 * 20091) >> 16))) + (v9 - v15)) * 35468) >> 16)) + ((((((v10 * 35468) >> 16) - (v11 + ((v11 * 20091) >> 16))) + (v24 - v23)) + 4) + ((((v12 * 35468) >> 16) - (v13 + ((v13 * 20091) >> 16))) + (v29 - v28)))) >> 3))
    v9 = ((load8u(arg1 + 32) + ((((((((((v3 * 35468) >> 16) - (v5 + ((v5 * 20091) >> 16))) + (v14 - v8)) * 20091) >> 16) + arg0) + ((((((v6 * 35468) >> 16) - (v7 + ((v7 * 20091) >> 16))) + (v9 - v15)) * 35468) >> 16)) + ((((((v10 * 35468) >> 16) - (v11 + ((v11 * 20091) >> 16))) + (v24 - v23)) + 4) + ((((v12 * 35468) >> 16) - (v13 + ((v13 * 20091) >> 16))) + (v29 - v28)))) >> 3)) if (v9 > 0) else 0)
    store8(arg1 + 32, (255 if (v9 >= 255) else ((load8u(arg1 + 32) + ((((((((((v3 * 35468) >> 16) - (v5 + ((v5 * 20091) >> 16))) + (v14 - v8)) * 20091) >> 16) + arg0) + ((((((v6 * 35468) >> 16) - (v7 + ((v7 * 20091) >> 16))) + (v9 - v15)) * 35468) >> 16)) + ((((((v10 * 35468) >> 16) - (v11 + ((v11 * 20091) >> 16))) + (v24 - v23)) + 4) + ((((v12 * 35468) >> 16) - (v13 + ((v13 * 20091) >> 16))) + (v29 - v28)))) >> 3)) if (v9 > 0) else 0)))
    arg0 = (((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16)))
    v3 = (v8 - v14)
    v8 = (load8u(arg1 + 33) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v8 - v14)) >> 3))
    v8 = ((load8u(arg1 + 33) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v8 - v14)) >> 3)) if (v8 > 0) else 0)
    store8(arg1 + 33, (255 if (v8 >= 255) else ((load8u(arg1 + 33) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v8 - v14)) >> 3)) if (v8 > 0) else 0)))
    arg0 = (load8u(arg1 + 34) + ((v3 - arg0) >> 3))
    arg0 = ((load8u(arg1 + 34) + ((v3 - arg0) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 34, (255 if (arg0 >= 255) else ((load8u(arg1 + 34) + ((v3 - arg0) >> 3)) if (arg0 > 0) else 0)))
    arg0 = (load8u(arg1 + 35) + ((v15 - v4) >> 3))
    arg0 = ((load8u(arg1 + 35) + ((v15 - v4) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 35, (255 if (arg0 >= 255) else ((load8u(arg1 + 35) + ((v15 - v4) >> 3)) if (arg0 > 0) else 0)))
    arg0 = (v2 - v5)
    v3 = (v7 - v6)
    v5 = (((((v2 - v5) * 20091) >> 16) + arg0) + (((v7 - v6) * 35468) >> 16))
    v2 = ((v11 - v10) + 4)
    v6 = (v13 - v12)
    v7 = (((v11 - v10) + 4) + (v13 - v12))
    v4 = (load8u(arg1 + 64) + (((((((v2 - v5) * 20091) >> 16) + arg0) + (((v7 - v6) * 35468) >> 16)) + (((v11 - v10) + 4) + (v13 - v12))) >> 3))
    v4 = ((load8u(arg1 + 64) + (((((((v2 - v5) * 20091) >> 16) + arg0) + (((v7 - v6) * 35468) >> 16)) + (((v11 - v10) + 4) + (v13 - v12))) >> 3)) if (v4 > 0) else 0)
    store8(arg1 + 64, (255 if (v4 >= 255) else ((load8u(arg1 + 64) + (((((((v2 - v5) * 20091) >> 16) + arg0) + (((v7 - v6) * 35468) >> 16)) + (((v11 - v10) + 4) + (v13 - v12))) >> 3)) if (v4 > 0) else 0)))
    arg0 = (((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16)))
    v3 = (v2 - v6)
    v2 = (load8u(arg1 + 65) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v2 - v6)) >> 3))
    v2 = ((load8u(arg1 + 65) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v2 - v6)) >> 3)) if (v2 > 0) else 0)
    store8(arg1 + 65, (255 if (v2 >= 255) else ((load8u(arg1 + 65) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v2 - v6)) >> 3)) if (v2 > 0) else 0)))
    arg0 = (load8u(arg1 + 66) + ((v3 - arg0) >> 3))
    arg0 = ((load8u(arg1 + 66) + ((v3 - arg0) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 66, (255 if (arg0 >= 255) else ((load8u(arg1 + 66) + ((v3 - arg0) >> 3)) if (arg0 > 0) else 0)))
    arg0 = (load8u(arg1 + 67) + ((v7 - v5) >> 3))
    arg0 = ((load8u(arg1 + 67) + ((v7 - v5) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 67, (255 if (arg0 >= 255) else ((load8u(arg1 + 67) + ((v7 - v5) >> 3)) if (arg0 > 0) else 0)))
    arg0 = (v18 - v17)
    v3 = (v20 - v19)
    v5 = (((((v18 - v17) * 20091) >> 16) + arg0) + (((v20 - v19) * 35468) >> 16))
    v2 = ((v25 - v22) + 4)
    v6 = (v30 - v27)
    v7 = (((v25 - v22) + 4) + (v30 - v27))
    v4 = (load8u(arg1 + 96) + (((((((v18 - v17) * 20091) >> 16) + arg0) + (((v20 - v19) * 35468) >> 16)) + (((v25 - v22) + 4) + (v30 - v27))) >> 3))
    v4 = ((load8u(arg1 + 96) + (((((((v18 - v17) * 20091) >> 16) + arg0) + (((v20 - v19) * 35468) >> 16)) + (((v25 - v22) + 4) + (v30 - v27))) >> 3)) if (v4 > 0) else 0)
    store8(arg1 + 96, (255 if (v4 >= 255) else ((load8u(arg1 + 96) + (((((((v18 - v17) * 20091) >> 16) + arg0) + (((v20 - v19) * 35468) >> 16)) + (((v25 - v22) + 4) + (v30 - v27))) >> 3)) if (v4 > 0) else 0)))
    arg0 = (((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16)))
    v3 = (v2 - v6)
    v2 = (load8u(arg1 + 97) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v2 - v6)) >> 3))
    v2 = ((load8u(arg1 + 97) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v2 - v6)) >> 3)) if (v2 > 0) else 0)
    store8(arg1 + 97, (255 if (v2 >= 255) else ((load8u(arg1 + 97) + (((((arg0 * 35468) >> 16) - (v3 + ((v3 * 20091) >> 16))) + (v2 - v6)) >> 3)) if (v2 > 0) else 0)))
    arg0 = (load8u(arg1 + 98) + ((v3 - arg0) >> 3))
    arg0 = ((load8u(arg1 + 98) + ((v3 - arg0) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 98, (255 if (arg0 >= 255) else ((load8u(arg1 + 98) + ((v3 - arg0) >> 3)) if (arg0 > 0) else 0)))
    arg0 = (load8u(arg1 + 99) + ((v7 - v5) >> 3))
    arg0 = ((load8u(arg1 + 99) + ((v7 - v5) >> 3)) if (arg0 > 0) else 0)
    store8(arg1 + 99, (255 if (arg0 >= 255) else ((load8u(arg1 + 99) + ((v7 - v5) >> 3)) if (arg0 > 0) else 0)))

# ----------------------------------------------------------
# $func461
# ----------------------------------------------------------
def func461(arg0, arg1, arg2):
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = 1
    while True:  # $label2
        while True:  # $label4
            while True:  # $label3
                while True:  # $label1
                    while True:  # $label0
                        v6 = ((arg0 * 404) + ENTITY_TYPES)
                        # br_table load32(((arg0 * 404) + ENTITY_TYPES) + 264)
                        break
                        break
                    store64(v4 + 4, 1)
                    store32(v4, arg0)
                    store32(v4 + 44, arg1)
                    func417(v4, (v4 + 44), 1)
                    break
                    break
                v11 = load32(ENTITIES)
                v23 = load32(arg2 + 283876)
                v24 = load32(arg2 + 283872)
                if (load32(v6 + 188) != 2):
                    break
                v9 = load32(9142440)
                v12 = (load32(9142440) + 2)
                v14 = ((arg0 * 404) + ENTITY_TYPES)
                v16 = load32(9142840)
                v3 = 0
                while True:  # $label12
                    while True:  # $label5
                        v7 = v3
                        arg0 = (v3 << 2)
                        arg2 = (load32((((v3 << 2) | 4) + 8611904)) + v23)
                        if (u32(v9) <= u32((load32((((v3 << 2) | 4) + 8611904)) + v23))):
                            break
                        v6 = (load32((arg0 + 8611904)) + v24)
                        if (u32(v9) <= u32((load32((arg0 + 8611904)) + v24))):
                            break
                        if ((arg2 | v6) < 0):
                            break
                        while True:  # $label6
                            v13 = load32(v14 + 216)
                            if (load32(v14 + 216) <= 0):
                                break
                            v17 = (load32(v14 + 220) + arg2)
                            if ((load32(v14 + 220) + arg2) <= arg2):
                                break
                            v15 = (v6 + v13)
                            v8 = load32(v14 + 372)
                            arg0 = v6
                            while True:  # $label11
                                v5 = (arg0 + 1)
                                v10 = (arg0 - v6)
                                v3 = arg2
                                while True:  # $label9
                                    if (u32(arg0) < u32(v9)):
                                        while True:  # $label8
                                            while True:  # $label7
                                                if not load8u((v8 + (((v3 - arg2) * v13) + v10))):
                                                    v3 = (v3 + 1)
                                                    break
                                                if (u32(v3) >= u32(v9)):
                                                    break
                                                if ((arg0 | v3) < 0):
                                                    break
                                                v3 = (v3 + 1)
                                                if load32((v16 + ((((v3 + 1) * v12) + v5) << 2))):
                                                    break
                                                if (load32(((load8u((v11 + (load32((v16 + ((((v3 + v12) * v12) + v5) << 2))) * 132)) + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                                                    break
                                                break
                                            if (v3 != v17):
                                                continue
                                            break
                                            break
                                        raise Unreachable()
                                    while True:  # $label10
                                        if load8u((v8 + (((v3 - arg2) * v13) + v10))):
                                            break
                                        v3 = (v3 + 1)
                                        if ((v3 + 1) != v17):
                                            continue
                                        break
                                    break
                                arg0 = v5
                                if (v5 < v15):
                                    continue
                                break
                            break
                        arg0 = load32(38500)
                        store32(v4 + 8, arg2)
                        store32(v4 + 4, v6)
                        store32(v4, arg0)
                        arg0 = (arg1 * 132)
                        arg1 = (v11 + (arg1 * 132))
                        arg2 = load16u((v11 + (arg1 * 132)) + 110)
                        store32(v4 + 40, 0)
                        store64(v4 + 32, 4294967297)
                        store64(v4 + 24, 4294967297)
                        store64(v4 + 16, 4294967297)
                        store32(v4 + 12, arg2)
                        store32(v4 + 44, load32(arg1 + 28))
                        v3 = 1
                        store8((load32(ENTITIES) + arg0) + 129, 3)
                        break
                        break
                    v3 = (v7 + 2)
                    if (u32(v7) <= u32(3357)):
                        continue
                    break
                v3 = 0
                break
                break
            store32(v4, arg0)
            store32(v4 + 44, arg1)
            func364(v4, (v4 + 44), 1)
            break
            break
        if (arg0 == load32(38636)):
            v3 = 0
            v6 = (v11 + (arg1 * 132))
            v5 = load16u((v11 + (arg1 * 132)) + 112)
            arg2 = (load16u((v11 + (arg1 * 132)) + 112) - 2)
            v9 = ((load8u(v6 + 122) * 404) + ENTITY_TYPES)
            v14 = ((v5 + load32(((load8u(v6 + 122) * 404) + ENTITY_TYPES) + 216)) + 2)
            if ((load16u((v11 + (arg1 * 132)) + 112) - 2) >= ((v5 + load32(((load8u(v6 + 122) * 404) + ENTITY_TYPES) + 216)) + 2)):
                break
            v6 = load16u(v6 + 114)
            v7 = (load16u(v6 + 114) - 2)
            v13 = ((load32(v9 + 220) + v6) + 2)
            if ((load16u(v6 + 114) - 2) >= ((load32(v9 + 220) + v6) + 2)):
                break
            v9 = load32(9142440)
            v12 = (load32(9142440) + 2)
            v16 = load32(9142840)
            while True:  # $label16
                while True:  # $label14
                    v5 = (arg2 + 1)
                    v3 = v7
                    if (u32(arg2) < u32(v9)):
                        while True:  # $label15
                            v6 = v3
                            v3 = (v3 + 1)
                            while True:  # $label13
                                if (u32(v6) >= u32(v9)):
                                    break
                                if ((arg2 | v6) < 0):
                                    break
                                if not load32((v16 + ((v5 + ((v3 + v12) * v12)) << 2))):
                                    break
                                break
                            if (v3 != v13):
                                continue
                            break
                    v3 = 0
                    arg2 = v5
                    if (v5 != v14):
                        continue
                    break
                    break
                break
            store32(v4 + 8, v6)
            store32(v4 + 4, arg2)
            store32(v4, arg0)
            arg0 = (v11 + (arg1 * 132))
            arg1 = load16u((v11 + (arg1 * 132)) + 110)
            store32(v4 + 40, 0)
            store64(v4 + 32, 4294967297)
            store64(v4 + 24, 4294967297)
            store64(v4 + 16, 4294967297)
            store32(v4 + 12, arg1)
            store32(v4 + 44, load32(arg0 + 28))
            v3 = 1
            break
        arg1 = (v11 + (arg1 * 132))
        v32 = (v11 + (arg1 * 132))
        store8(arg1 + 129, 0)
        v12 = ((load32(38512) != arg0) & (load32(38792) != arg0))
        v13 = (1 if ((load32(38512) != arg0) & (load32(38792) != arg0)) else 2)
        v33 = (13 if v12 else 10)
        arg1 = ((arg0 * 404) + ENTITY_TYPES)
        v16 = load32(((arg0 * 404) + ENTITY_TYPES) + 220)
        v34 = (load32(((arg0 * 404) + ENTITY_TYPES) + 220) // 2)
        v17 = load32(arg1 + 216)
        v35 = (load32(arg1 + 216) // 2)
        v36 = load32(arg2 + 283908)
        v25 = load32(9142440)
        v3 = 0
        while True:  # $label32
            while True:  # $label17
                v14 = v3
                v3 = (v3 << 2)
                v26 = load32((((v3 << 2) | 4) + 8611904))
                arg1 = (load32((((v3 << 2) | 4) + 8611904)) + v23)
                if (u32(v25) <= u32((load32((((v3 << 2) | 4) + 8611904)) + v23))):
                    break
                v27 = load32((v3 + 8611904))
                v3 = (load32((v3 + 8611904)) + v24)
                if (u32(v25) <= u32((load32((v3 + 8611904)) + v24))):
                    break
                if ((arg1 | v3) < 0):
                    break
                while True:  # $label31
                    v18 = 0
                    while True:  # $label19
                        while True:  # $label18
                            v6 = (v13 << 1)
                            v5 = ((v13 << 1) + v17)
                            v11 = v3
                            v3 = (v3 - v13)
                            v7 = load32(arg2 + 283872)
                            v9 = ((((v13 << 1) + v17) + ((v3 - v13) << 1)) - (load32(arg2 + 283872) << 1))
                            v8 = (v6 + v16)
                            v9 = arg1
                            v6 = (arg1 - v13)
                            arg1 = load32(arg2 + 283876)
                            v10 = (((v6 + v16) + ((arg1 - v13) << 1)) - (load32(arg2 + 283876) << 1))
                            v10 = (v33 << 1)
                            if ((((((((v13 << 1) + v17) + ((v3 - v13) << 1)) - (load32(arg2 + 283872) << 1)) * v9) + ((((v6 + v16) + ((arg1 - v13) << 1)) - (load32(arg2 + 283876) << 1)) * v10)) - 1) <= ((v33 << 1) * v10)):
                                break
                            v18 = 1
                            if (v5 <= 0):
                                break
                            if (v8 <= 0):
                                break
                            v20 = (v6 + v8)
                            v28 = (v3 + v5)
                            v29 = (v9 + v16)
                            v30 = (v11 + v17)
                            v15 = load32(9142440)
                            v8 = (load32(9142440) + 2)
                            v21 = load32(ENTITIES)
                            v10 = load32(9142840)
                            if v12:
                                v19 = (arg1 - 3)
                                v31 = (arg1 + 3)
                                v37 = (v7 - 3)
                                v38 = (v7 + 3)
                                while True:  # $label27
                                    if (u32(v3) >= u32(v15)):
                                        break
                                    if ((v3 < v38) & (v3 > v37)):
                                        break
                                    v5 = (v3 + 1)
                                    arg1 = v6
                                    while True:  # $label23
                                        if ((v3 < v11) | (v3 >= v30)):
                                            while True:  # $label22
                                                if (u32(arg1) >= u32(v15)):
                                                    break
                                                if ((arg1 | v3) < 0):
                                                    break
                                                while True:  # $label20
                                                    v7 = (arg1 + 1)
                                                    v22 = load32((v10 + ((v5 + (((arg1 + 1) + v8) * v8)) << 2)))
                                                    if not load32((v10 + ((v5 + (((arg1 + 1) + v8) * v8)) << 2))):
                                                        break
                                                    if (load32(((load8u((v21 + (v22 * 132)) + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                                        break
                                                    break
                                                    break
                                                while True:  # $label21
                                                    if (arg1 >= v31):
                                                        break
                                                    if (arg1 <= v19):
                                                        break
                                                    break
                                                    break
                                                arg1 = v7
                                                if (v7 < v20):
                                                    continue
                                                break
                                                break
                                            raise Unreachable()
                                        while True:  # $label26
                                            if (u32(arg1) >= u32(v15)):
                                                break
                                            if ((arg1 | v3) < 0):
                                                break
                                            v7 = (arg1 + 1)
                                            while True:  # $label24
                                                if not ((arg1 < v29) & (arg1 >= v9)):
                                                    v22 = load32((v10 + ((v5 + ((v7 + v8) * v8)) << 2)))
                                                    if not load32((v10 + ((v5 + ((v7 + v8) * v8)) << 2))):
                                                        break
                                                    if (load32(((load8u((v21 + (v22 * 132)) + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                                        break
                                                    break
                                                if load32((v10 + ((((v7 + v8) * v8) + v5) << 2))):
                                                    break
                                                if not load32((v10 + (((v7 * v8) + v5) << 2))):
                                                    break
                                                break
                                                break
                                            while True:  # $label25
                                                if (arg1 >= v31):
                                                    break
                                                if (arg1 <= v19):
                                                    break
                                                break
                                                break
                                            arg1 = v7
                                            if (v7 < v20):
                                                continue
                                            break
                                        break
                                    v3 = v5
                                    if (v5 < v28):
                                        continue
                                    break
                                break
                            while True:  # $label30
                                v5 = v3
                                if (u32(v3) < u32(v15)):
                                    v3 = (v5 + 1)
                                    v19 = ((v5 < v30) & (v5 >= v11))
                                    arg1 = v6
                                    while True:  # $label29
                                        v18 = 0
                                        v7 = arg1
                                        if (u32(v15) <= u32(arg1)):
                                            break
                                        if ((v5 | v7) < 0):
                                            break
                                        arg1 = (v7 + 1)
                                        while True:  # $label28
                                            if not (((v7 >= v9) & v19) & (v7 < v29)):
                                                v7 = load32((v10 + ((v3 + ((arg1 + v8) * v8)) << 2)))
                                                if not load32((v10 + ((v3 + ((arg1 + v8) * v8)) << 2))):
                                                    break
                                                if (load32(((load8u((v21 + (v7 * 132)) + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                                    break
                                                break
                                            if load32((v10 + ((((arg1 + v8) * v8) + v3) << 2))):
                                                break
                                            if load32((v10 + (((arg1 * v8) + v3) << 2))):
                                                break
                                            break
                                        if (arg1 < v20):
                                            continue
                                        break
                                    if (v3 < v28):
                                        continue
                                break
                            v18 = (u32(v5) < u32(v15))
                            break
                        break
                        break
                    break
                if not 0:
                    break
                if not func108((v11 + v35), (v9 + v34), v36, 9):
                    break
                arg1 = ((v26 * v26) + (v27 * v27))
                if (((v26 * v26) + (v27 * v27)) > load32(arg2 + 283880)):
                    store32(arg2 + 283880, arg1)
                func261(arg0, v11, v9, v32)
                v3 = 1
                break
                break
            v3 = (v14 + 2)
            if (u32(v14) <= u32(116157)):
                continue
            break
        v3 = 0
        break
    G.global0 = (v4 + 48)
    return v3

# ----------------------------------------------------------
# $func462
# ----------------------------------------------------------
def func462(arg0, arg1, arg2):
    while True:  # $label4
        while True:  # $label8
            while True:  # $label7
                while True:  # $label5
                    while True:  # $label2
                        while True:  # $label1
                            while True:  # $label3
                                v5 = load32(arg1 + 8)
                                v6 = load32(arg1 + 12)
                                if (load32(arg1 + 8) >= load32(arg1 + 12)):
                                    while True:  # $label0
                                        v3 = load32(arg2 + 12)
                                        v8 = (v6 - load32(arg2 + 12))
                                        if ((v6 - load32(arg2 + 12)) <= 0):
                                            break
                                        v9 = (load32(arg1 + 4) + v3)
                                        v10 = load32(arg1)
                                        v3 = load32(arg0 + 24)
                                        v6 = load32(arg0 + 28)
                                        if (u32(load32(arg0 + 24)) < u32(load32(arg0 + 28))):
                                            store32(v3 + 12, v8)
                                            store32(v3 + 8, v5)
                                            store32(v3 + 4, v9)
                                            store32(v3, v10)
                                            store32(arg0 + 24, (v3 + 16))
                                            break
                                        v3 = load32((arg0 + 20))
                                        v11 = (v3 - load32((arg0 + 20)))
                                        v12 = ((v3 - load32((arg0 + 20))) >> 4)
                                        v4 = (((v3 - load32((arg0 + 20))) >> 4) + 1)
                                        if (u32((((v3 - load32((arg0 + 20))) >> 4) + 1)) >= u32(268435456)):
                                            break
                                        v6 = (v6 - v3)
                                        v7 = ((v6 - v3) >> 3)
                                        v6 = (268435455 if (u32(v6) >= u32(2147483632)) else (((v6 - v3) >> 3) if (u32(v4) < u32(v7)) else v4))
                                        if (268435455 if (u32(v6) >= u32(2147483632)) else (((v6 - v3) >> 3) if (u32(v4) < u32(v7)) else v4)):
                                            if (u32(v6) >= u32(268435456)):
                                                break
                                        else:
                                        v7 = 0
                                        v4 = (0 + (v12 << 4))
                                        store32((0 + (v12 << 4)) + 12, v8)
                                        store32(v4 + 8, v5)
                                        store32(v4 + 4, v9)
                                        store32(v4, v10)
                                        # TODO: memory.copy
                                        store32(arg0 + 28, (v7 + (v6 << 4)))
                                        store32(arg0 + 24, (v4 + 16))
                                        store32(arg0 + 20, v7)
                                        if not v3:
                                            break
                                        break
                                    v3 = load32(arg2 + 8)
                                    v5 = (load32(arg1 + 8) - load32(arg2 + 8))
                                    if ((load32(arg1 + 8) - load32(arg2 + 8)) <= 0):
                                        break
                                    v6 = (load32(arg1) + v3)
                                    v7 = load32(arg2 + 12)
                                    v8 = load32(arg1 + 4)
                                    arg1 = load32(arg0 + 24)
                                    v3 = load32(arg0 + 28)
                                    if (u32(load32(arg0 + 24)) < u32(load32(arg0 + 28))):
                                        store32(arg1 + 12, v7)
                                        store32(arg1 + 8, v5)
                                        store32(arg1 + 4, v8)
                                        store32(arg1, v6)
                                        break
                                    arg1 = load32((arg0 + 20))
                                    v9 = (arg1 - load32((arg0 + 20)))
                                    v10 = ((arg1 - load32((arg0 + 20))) >> 4)
                                    arg2 = (((arg1 - load32((arg0 + 20))) >> 4) + 1)
                                    if (u32((((arg1 - load32((arg0 + 20))) >> 4) + 1)) >= u32(268435456)):
                                        break
                                    v3 = (v3 - arg1)
                                    v4 = ((v3 - arg1) >> 3)
                                    v3 = (268435455 if (u32(v3) >= u32(2147483632)) else (((v3 - arg1) >> 3) if (u32(arg2) < u32(v4)) else arg2))
                                    if (268435455 if (u32(v3) >= u32(2147483632)) else (((v3 - arg1) >> 3) if (u32(arg2) < u32(v4)) else arg2)):
                                        if (u32(v3) >= u32(268435456)):
                                            break
                                    else:
                                    v4 = 0
                                    arg2 = (0 + (v10 << 4))
                                    store32((0 + (v10 << 4)) + 12, v7)
                                    store32(arg2 + 8, v5)
                                    store32(arg2 + 4, v8)
                                    store32(arg2, v6)
                                    # TODO: memory.copy
                                    store32(arg0 + 28, (v4 + (v3 << 4)))
                                    store32(arg0 + 24, (arg2 + 16))
                                    store32(arg0 + 20, v4)
                                    if not arg1:
                                        break
                                    return af(arg1)
                                while True:  # $label6
                                    v3 = load32(arg2 + 8)
                                    v8 = (v5 - load32(arg2 + 8))
                                    if ((v5 - load32(arg2 + 8)) <= 0):
                                        break
                                    v9 = (load32(arg1) + v3)
                                    v10 = load32(arg1 + 4)
                                    v3 = load32(arg0 + 24)
                                    v5 = load32(arg0 + 28)
                                    if (u32(load32(arg0 + 24)) < u32(load32(arg0 + 28))):
                                        store32(v3 + 12, v6)
                                        store32(v3 + 8, v8)
                                        store32(v3 + 4, v10)
                                        store32(v3, v9)
                                        store32(arg0 + 24, (v3 + 16))
                                        break
                                    v3 = load32((arg0 + 20))
                                    v11 = (v3 - load32((arg0 + 20)))
                                    v12 = ((v3 - load32((arg0 + 20))) >> 4)
                                    v4 = (((v3 - load32((arg0 + 20))) >> 4) + 1)
                                    if (u32((((v3 - load32((arg0 + 20))) >> 4) + 1)) >= u32(268435456)):
                                        break
                                    v5 = (v5 - v3)
                                    v7 = ((v5 - v3) >> 3)
                                    v5 = (268435455 if (u32(v5) >= u32(2147483632)) else (((v5 - v3) >> 3) if (u32(v4) < u32(v7)) else v4))
                                    if (268435455 if (u32(v5) >= u32(2147483632)) else (((v5 - v3) >> 3) if (u32(v4) < u32(v7)) else v4)):
                                        if (u32(v5) >= u32(268435456)):
                                            break
                                    else:
                                    v7 = 0
                                    v4 = (0 + (v12 << 4))
                                    store32((0 + (v12 << 4)) + 12, v6)
                                    store32(v4 + 8, v8)
                                    store32(v4 + 4, v10)
                                    store32(v4, v9)
                                    # TODO: memory.copy
                                    store32(arg0 + 28, (v7 + (v5 << 4)))
                                    store32(arg0 + 24, (v4 + 16))
                                    store32(arg0 + 20, v7)
                                    if not v3:
                                        break
                                    break
                                v3 = load32(arg2 + 12)
                                v5 = (load32(arg1 + 12) - load32(arg2 + 12))
                                if ((load32(arg1 + 12) - load32(arg2 + 12)) <= 0):
                                    break
                                v6 = (load32(arg1 + 4) + v3)
                                v7 = load32(arg2 + 8)
                                v8 = load32(arg1)
                                arg1 = load32(arg0 + 24)
                                v3 = load32(arg0 + 28)
                                if (u32(load32(arg0 + 24)) < u32(load32(arg0 + 28))):
                                    store32(arg1 + 12, v5)
                                    store32(arg1 + 8, v7)
                                    store32(arg1 + 4, v6)
                                    store32(arg1, v8)
                                    break
                                arg1 = load32((arg0 + 20))
                                v9 = (arg1 - load32((arg0 + 20)))
                                v10 = ((arg1 - load32((arg0 + 20))) >> 4)
                                arg2 = (((arg1 - load32((arg0 + 20))) >> 4) + 1)
                                if (u32((((arg1 - load32((arg0 + 20))) >> 4) + 1)) >= u32(268435456)):
                                    break
                                v3 = (v3 - arg1)
                                v4 = ((v3 - arg1) >> 3)
                                v3 = (268435455 if (u32(v3) >= u32(2147483632)) else (((v3 - arg1) >> 3) if (u32(arg2) < u32(v4)) else arg2))
                                if (268435455 if (u32(v3) >= u32(2147483632)) else (((v3 - arg1) >> 3) if (u32(arg2) < u32(v4)) else arg2)):
                                    if (u32(v3) >= u32(268435456)):
                                        break
                                else:
                                v4 = 0
                                arg2 = (0 + (v10 << 4))
                                store32((0 + (v10 << 4)) + 12, v5)
                                store32(arg2 + 8, v7)
                                store32(arg2 + 4, v6)
                                store32(arg2, v8)
                                # TODO: memory.copy
                                store32(arg0 + 28, (v4 + (v3 << 4)))
                                store32(arg0 + 24, (arg2 + 16))
                                store32(arg0 + 20, v4)
                                if not arg1:
                                    break
                                break
                            return af(arg1)
                            break
                        func42()
                        raise Unreachable()
                        break
                    func68()
                    raise Unreachable()
                    break
                func42()
                raise Unreachable()
                break
            func42()
            raise Unreachable()
            break
        func42()
        raise Unreachable()
        break
    store32(arg0 + 24, (arg1 + 16))
    return v9

# ----------------------------------------------------------
# $func463
# ----------------------------------------------------------
def func463(arg0, arg1):
    v7 = load32(arg0 + 8)
    v5 = load8u(arg1 + 3)
    while True:  # $label8
        while True:  # $label1
            while True:  # $label0
                v4 = load32(arg0 + 12)
                if (load32(arg0 + 12) >= 0):
                    break
                v6 = load32(arg0 + 16)
                if not load32(arg0 + 16):
                    break
                if (u32(load32(arg0 + 24)) > u32(v6)):
                    v3 = load64(v6)
                    store32(arg0 + 16, (v6 + 7))
                    store64(arg0, ((load64(arg0) << 56) | ((((((v3 << 56) | ((v3 & 65280) << 40)) | (((v3 & 16711680) << 24) | ((v3 & 4278190080) << 8))) | ((((v3 & 0xFFFFFFFF) >> 40) & 65280) | ((((v3 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v3 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                    v4 = (v4 + 56)
                    break
                func36(arg0)
                v4 = load32(arg0 + 12)
                break
            while True:  # $label2
                v5 = (((v5 * v7) & 0xFFFFFFFF) >> 8)
                v3 = load64(arg0)
                v2 = i32(v4)
                v8 = i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v4)))
                if (u32((((v5 * v7) & 0xFFFFFFFF) >> 8)) < u32(i32(((load64(arg0) & 0xFFFFFFFF) >> i32(v4))))):
                    v3 = (v3 - (i32((v5 + 1)) << v2))
                    store64(arg0, (v3 - (i32((v5 + 1)) << v2)))
                    break
                break
            v6 = (v5 + 1)
            v7 = (clz((v5 + 1)) ^ 24)
            v4 = ((v7 - v5) - (clz((v5 + 1)) ^ 24))
            store32(v4 + 12, ((v7 - v5) - (clz((v5 + 1)) ^ 24)))
            v6 = ((v6 << v7) - 1)
            store32(arg0 + 8, ((v6 << v7) - 1))
            while True:  # $label5
                if (u32(v5) >= u32(v8)):
                    v7 = load8u(arg1 + 4)
                    while True:  # $label3
                        if (v4 >= 0):
                            break
                        v5 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(v5)):
                            v2 = load64(v5)
                            store32(arg0 + 16, (v5 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # $label4
                        v5 = (((v6 * v7) & 0xFFFFFFFF) >> 8)
                        v2 = i32(v4)
                        v7 = (u32((((v6 * v7) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4)))))
                        if not (u32((((v6 * v7) & 0xFFFFFFFF) >> 8)) >= u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                            v3 = (v3 - (i32((v5 + 1)) << v2))
                            store64(arg0, (v3 - (i32((v5 + 1)) << v2)))
                            break
                        break
                    v5 = (v5 + 1)
                    v6 = (clz((v5 + 1)) ^ 24)
                    v4 = ((v6 - v5) - (clz((v5 + 1)) ^ 24))
                    store32(v4 + 12, ((v6 - v5) - (clz((v5 + 1)) ^ 24)))
                    v6 = ((v5 << v6) - 1)
                    store32(arg0 + 8, ((v5 << v6) - 1))
                    if v7:
                        break
                    v5 = load8u(arg1 + 5)
                    while True:  # $label6
                        if (v4 >= 0):
                            break
                        arg1 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(arg1)):
                            v2 = load64(arg1)
                            store32(arg0 + 16, (arg1 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # $label7
                        arg1 = (((v5 * v6) & 0xFFFFFFFF) >> 8)
                        v2 = i32(v4)
                        if (u32((((v5 * v6) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                            store64(arg0, (v3 - (i32((arg1 + 1)) << v2)))
                            v5 = 4
                            break
                        v5 = 3
                        break
                    arg1 = (arg1 + 1)
                    v4 = (clz((arg1 + 1)) ^ 24)
                    store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                    break
                v7 = load8u(arg1 + 6)
                while True:  # $label9
                    if (v4 >= 0):
                        break
                    v5 = load32(arg0 + 16)
                    if not load32(arg0 + 16):
                        break
                    if (u32(load32(arg0 + 24)) > u32(v5)):
                        v2 = load64(v5)
                        store32(arg0 + 16, (v5 + 7))
                        v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                        store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                        v4 = (v4 + 56)
                        break
                    func36(arg0)
                    v3 = load64(arg0)
                    v4 = load32(arg0 + 12)
                    break
                while True:  # $label10
                    v5 = (((v6 * v7) & 0xFFFFFFFF) >> 8)
                    v2 = i32(v4)
                    v7 = i32(((v3 & 0xFFFFFFFF) >> i32(v4)))
                    if (u32((((v6 * v7) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                        v3 = (v3 - (i32((v5 + 1)) << v2))
                        store64(arg0, (v3 - (i32((v5 + 1)) << v2)))
                        break
                    break
                v6 = (v5 + 1)
                v8 = (clz((v5 + 1)) ^ 24)
                v4 = ((v6 - v5) - (clz((v5 + 1)) ^ 24))
                store32(v4 + 12, ((v6 - v5) - (clz((v5 + 1)) ^ 24)))
                v6 = ((v6 << v8) - 1)
                store32(arg0 + 8, ((v6 << v8) - 1))
                if (u32(v5) >= u32(v7)):
                    v5 = load8u(arg1 + 7)
                    while True:  # $label11
                        if (v4 >= 0):
                            break
                        arg1 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(arg1)):
                            v2 = load64(arg1)
                            store32(arg0 + 16, (arg1 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # $label12
                        arg1 = (((v5 * v6) & 0xFFFFFFFF) >> 8)
                        v2 = i32(v4)
                        v7 = i32(((v3 & 0xFFFFFFFF) >> i32(v4)))
                        if (u32((((v5 * v6) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                            v3 = (v3 - (i32((arg1 + 1)) << v2))
                            store64(arg0, (v3 - (i32((arg1 + 1)) << v2)))
                            break
                        break
                    v5 = (arg1 + 1)
                    v6 = (clz((arg1 + 1)) ^ 24)
                    v4 = ((v6 - arg1) - (clz((arg1 + 1)) ^ 24))
                    store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                    v6 = ((v5 << v6) - 1)
                    store32(arg0 + 8, ((v5 << v6) - 1))
                    if (u32(arg1) >= u32(v7)):
                        while True:  # $label13
                            if (v4 >= 0):
                                break
                            arg1 = load32(arg0 + 16)
                            if not load32(arg0 + 16):
                                break
                            if (u32(load32(arg0 + 24)) > u32(arg1)):
                                v2 = load64(arg1)
                                store32(arg0 + 16, (arg1 + 7))
                                v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                v4 = (v4 + 56)
                                break
                            func36(arg0)
                            v3 = load64(arg0)
                            v4 = load32(arg0 + 12)
                            break
                        while True:  # $label14
                            arg1 = (((v6 * 159) & 0xFFFFFFFF) >> 8)
                            v2 = i32(v4)
                            if (u32((((v6 * 159) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                                store64(arg0, (v3 - (i32((arg1 + 1)) << v2)))
                                v5 = 6
                                break
                            v5 = 5
                            break
                        arg1 = (arg1 + 1)
                        v4 = (clz((arg1 + 1)) ^ 24)
                        store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                        break
                    while True:  # $label15
                        if (v4 >= 0):
                            break
                        arg1 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(arg1)):
                            v2 = load64(arg1)
                            store32(arg0 + 16, (arg1 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # $label16
                        arg1 = (((v6 * 165) & 0xFFFFFFFF) >> 8)
                        v2 = i32(v4)
                        if (u32((((v6 * 165) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                            v3 = (v3 - (i32((arg1 + 1)) << v2))
                            store64(arg0, (v3 - (i32((arg1 + 1)) << v2)))
                            arg1 = (v6 - arg1)
                            break
                        arg1 = (arg1 + 1)
                        break
                    v6 = 7
                    v5 = (clz(arg1) ^ 24)
                    v4 = (v4 - (clz(arg1) ^ 24))
                    store32(arg0 + 12, (v4 - (clz(arg1) ^ 24)))
                    v5 = ((arg1 << v5) - 1)
                    store32(arg0 + 8, ((arg1 << v5) - 1))
                    while True:  # $label17
                        if (v4 >= 0):
                            break
                        arg1 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if (u32(load32(arg0 + 24)) > u32(arg1)):
                            v2 = load64(arg1)
                            store32(arg0 + 16, (arg1 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # $label18
                        arg1 = (((v5 * 145) & 0xFFFFFFFF) >> 8)
                        v2 = i32(v4)
                        v7 = i32(((v3 & 0xFFFFFFFF) >> i32(v4)))
                        if (u32((((v5 * 145) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                            store64(arg0, (v3 - (i32((arg1 + 1)) << v2)))
                            break
                        break
                    v5 = (arg1 + 1)
                    v4 = (clz((arg1 + 1)) ^ 24)
                    store32(v4 + 12, ((v5 - arg1) - (clz((arg1 + 1)) ^ 24)))
                    store32(arg0 + 8, ((v5 << v4) - 1))
                    return (v6 + (u32(arg1) < u32(v7)))
                v7 = load8u(arg1 + 8)
                while True:  # $label19
                    if (v4 >= 0):
                        break
                    v5 = load32(arg0 + 16)
                    if not load32(arg0 + 16):
                        break
                    if (u32(load32(arg0 + 24)) > u32(v5)):
                        v2 = load64(v5)
                        store32(arg0 + 16, (v5 + 7))
                        v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                        store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                        v4 = (v4 + 56)
                        break
                    func36(arg0)
                    v3 = load64(arg0)
                    v4 = load32(arg0 + 12)
                    break
                while True:  # $label20
                    v5 = (((v6 * v7) & 0xFFFFFFFF) >> 8)
                    v2 = i32(v4)
                    v8 = i32(((v3 & 0xFFFFFFFF) >> i32(v4)))
                    if (u32((((v6 * v7) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                        v3 = (v3 - (i32((v5 + 1)) << v2))
                        store64(arg0, (v3 - (i32((v5 + 1)) << v2)))
                        v7 = 10
                        break
                    v7 = 9
                    break
                v6 = (v5 + 1)
                v9 = (clz((v5 + 1)) ^ 24)
                v4 = ((v6 - v5) - (clz((v5 + 1)) ^ 24))
                store32(v4 + 12, ((v6 - v5) - (clz((v5 + 1)) ^ 24)))
                v6 = ((v6 << v9) - 1)
                store32(arg0 + 8, ((v6 << v9) - 1))
                v7 = load8u((arg1 + v7))
                while True:  # $label21
                    if (v4 >= 0):
                        break
                    arg1 = load32(arg0 + 16)
                    if not load32(arg0 + 16):
                        break
                    if (u32(load32(arg0 + 24)) > u32(arg1)):
                        v2 = load64(arg1)
                        store32(arg0 + 16, (arg1 + 7))
                        v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                        store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                        v4 = (v4 + 56)
                        break
                    func36(arg0)
                    v3 = load64(arg0)
                    v4 = load32(arg0 + 12)
                    break
                while True:  # $label22
                    arg1 = (((v6 * v7) & 0xFFFFFFFF) >> 8)
                    v2 = i32(v4)
                    v7 = i32(((v3 & 0xFFFFFFFF) >> i32(v4)))
                    if (u32((((v6 * v7) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                        v3 = (v3 - (i32((arg1 + 1)) << v2))
                        store64(arg0, (v3 - (i32((arg1 + 1)) << v2)))
                        break
                    break
                v6 = (arg1 + 1)
                v9 = (clz((arg1 + 1)) ^ 24)
                v4 = ((v6 - arg1) - (clz((arg1 + 1)) ^ 24))
                store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                v6 = ((v6 << v9) - 1)
                store32(arg0 + 8, ((v6 << v9) - 1))
                while True:  # $label23
                    v9 = (((u32(v5) < u32(v8)) << 1) | (u32(arg1) < u32(v7)))
                    v5 = load32((((((u32(v5) < u32(v8)) << 1) | (u32(arg1) < u32(v7))) << 2) + 13984))
                    arg1 = load8u(load32((((((u32(v5) < u32(v8)) << 1) | (u32(arg1) < u32(v7))) << 2) + 13984)))
                    if not load8u(load32((((((u32(v5) < u32(v8)) << 1) | (u32(arg1) < u32(v7))) << 2) + 13984))):
                        v7 = 0
                        break
                    v7 = 0
                    while True:  # $label26
                        while True:  # $label24
                            if (v4 >= 0):
                                break
                            v8 = load32(arg0 + 16)
                            if not load32(arg0 + 16):
                                break
                            if (u32(load32(arg0 + 24)) > u32(v8)):
                                v2 = load64(v8)
                                store32(arg0 + 16, (v8 + 7))
                                v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                                store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8)))
                                v4 = (v4 + 56)
                                break
                            func36(arg0)
                            v3 = load64(arg0)
                            v4 = load32(arg0 + 12)
                            break
                        while True:  # $label25
                            arg1 = (((v6 * (arg1 & 255)) & 0xFFFFFFFF) >> 8)
                            v2 = i32(v4)
                            v8 = i32(((v3 & 0xFFFFFFFF) >> i32(v4)))
                            if (u32((((v6 * (arg1 & 255)) & 0xFFFFFFFF) >> 8)) < u32(i32(((v3 & 0xFFFFFFFF) >> i32(v4))))):
                                v3 = (v3 - (i32((arg1 + 1)) << v2))
                                store64(arg0, (v3 - (i32((arg1 + 1)) << v2)))
                                break
                            break
                        v6 = (arg1 + 1)
                        v10 = (clz((arg1 + 1)) ^ 24)
                        v4 = ((v6 - arg1) - (clz((arg1 + 1)) ^ 24))
                        store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                        v6 = ((v6 << v10) - 1)
                        store32(arg0 + 8, ((v6 << v10) - 1))
                        v7 = ((v7 << 1) | (u32(arg1) < u32(v8)))
                        arg1 = load8u(v5 + 1)
                        v5 = (v5 + 1)
                        if arg1:
                            continue
                        break
                    break
                break
            return ((v7 + (8 << v9)) + 3)
            break
        a_c()
        raise Unreachable()
        break
    store32(arg0 + 8, ((arg1 << v4) - 1))
    return v5
