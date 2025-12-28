"""
Tzar Engine - Core module (part 5).
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
# $func184
# ----------------------------------------------------------
def func184(arg0, arg1, arg2, arg3):
    while True:  # $label1
        while True:  # $label0
            v4 = load32(arg0 + 5820)
            if (load32(arg0 + 5820) >= 14):
                v4 = (load16u(arg0 + 5816) | (arg3 << v4))
                store16(arg0 + 5816, (load16u(arg0 + 5816) | (arg3 << v4)))
                v5 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v5 + load32(arg0 + 8)), v4)
                v4 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v4 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                arg3 = load32(arg0 + 5820)
                v5 = (((arg3 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820)))
                store16(arg0 + 5816, (((arg3 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                break
            v5 = (load16u(arg0 + 5816) | (arg3 << v4))
            store16(arg0 + 5816, (load16u(arg0 + 5816) | (arg3 << v4)))
            break
        arg3 = (v4 + 3)
        if ((v4 + 3) >= 9):
            arg3 = load32(arg0 + 20)
            store32(arg0 + 20, (load32(arg0 + 20) + 1))
            store8((arg3 + load32(arg0 + 8)), v5)
            arg3 = load32(arg0 + 20)
            store32(arg0 + 20, (load32(arg0 + 20) + 1))
            store8((arg3 + load32(arg0 + 8)), load8u((arg0 + 5817)))
            break
        if (arg3 <= 0):
            break
        arg3 = load32(arg0 + 20)
        store32(arg0 + 20, (load32(arg0 + 20) + 1))
        store8((arg3 + load32(arg0 + 8)), v5)
        break
    store32(arg0 + 5820, 0)
    store16(arg0 + 5816, 0)
    arg3 = load32(arg0 + 20)
    store32(arg0 + 20, (load32(arg0 + 20) + 1))
    store8((arg3 + load32(arg0 + 8)), arg2)
    arg3 = load32(arg0 + 20)
    store32(arg0 + 20, (load32(arg0 + 20) + 1))
    store8((arg3 + load32(arg0 + 8)), ((arg2 & 0xFFFFFFFF) >> 8))
    arg3 = load32(arg0 + 20)
    store32(arg0 + 20, (load32(arg0 + 20) + 1))
    arg3 = (arg2 ^ -1)
    store8((arg3 + load32(arg0 + 8)), (arg2 ^ -1))
    v4 = load32(arg0 + 20)
    store32(arg0 + 20, (load32(arg0 + 20) + 1))
    store8((v4 + load32(arg0 + 8)), ((arg3 & 0xFFFFFFFF) >> 8))
    if arg2:
    store32(arg0 + 20, (load32(arg0 + 20) + arg2))
    return (arg3 - 13)

# ----------------------------------------------------------
# $func185
# ----------------------------------------------------------
def func185(arg0):
    if not (load8u(arg0) & 15):
        # TODO: i32.atomic.rmw.cmpxchg
        return (10 & 10)
    while True:  # $label4
        v2 = load32(arg0)
        while True:  # $label3
            while True:  # $label2
                while True:  # $label0
                    v1 = G.global3
                    v4 = load32(G.global3 + 24)
                    v3 = load32(arg0 + 4)
                    v6 = (load32(arg0 + 4) & 1073741823)
                    if (load32(G.global3 + 24) != (load32(arg0 + 4) & 1073741823)):
                        break
                    while True:  # $label1
                        if not (v2 & 8):
                            break
                        if (load32(arg0 + 20) >= 0):
                            break
                        store32(arg0 + 20, 0)
                        v3 = (v3 & 1073741824)
                        break
                        break
                    if ((v2 & 3) != 1):
                        break
                    v5 = 6
                    v1 = load32(arg0 + 20)
                    if (u32(load32(arg0 + 20)) > u32(2147483646)):
                        break
                    store32(arg0 + 20, (v1 + 1))
                    break
                    break
                v5 = 56
                if (v6 == 1073741823):
                    break
                while True:  # $label5
                    if v6:
                        break
                    if (0 if (v2 & 4) else v3):
                        break
                    if (v2 & 128):
                        if not load32(v1 + 80):
                            store32(v1 + 80, -12)
                        v6 = load32(arg0 + 8)
                        store32(v1 + 84, (arg0 + 16))
                    else:
                    # TODO: i32.atomic.rmw.cmpxchg
                    if (((v4 | -2147483648) if v6 else v4) == (v4 | (v3 & 1073741824))):
                        break
                    store32(v1 + 84, 0)
                    if ((v2 & 12) != 12):
                        break
                    if load32(arg0 + 8):
                        break
                    break
                break
                break
            v2 = load32(v1 + 76)
            v5 = (v1 + 76)
            store32(arg0 + 12, (v1 + 76))
            store32(arg0 + 16, v2)
            v4 = (arg0 + 16)
            if (v2 != v5):
                store32((v2 - 4), v4)
            store32(v1 + 76, v4)
            v5 = 0
            store32(v1 + 84, 0)
            if not v3:
                break
            store32(arg0 + 20, 0)
            break
            break
        break
    return v5

# ----------------------------------------------------------
# $func186
# ----------------------------------------------------------
def func186(arg0, arg1, arg2, arg3):
    v5 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label0
        if not arg0:
            break
        if not load32(9688320):
            store32(9688320, 43)
        if not load8u(9688037):
            while True:  # $label1
                v7 = load8s(9688039)
                if not load8s(9688039):
                    break
                # TODO: i32.atomic.rmw.cmpxchg
                v4 = -2147483647
                if (v7 < 0):
                    store8(9688039, 0)
                if not v4:
                    break
                while True:  # $label2
                    v7 = ((v4 + 2147483647) if (v4 < 0) else v4)
                    # TODO: i32.atomic.rmw.cmpxchg
                    v4 = (v7 - 2147483647)
                    if ((v7 - 2147483647) == v7):
                        break
                    v6 = (v6 + 1)
                    if ((v6 + 1) != 10):
                        continue
                    break
                # TODO: i32.atomic.rmw.add
                v4 = 2
                while True:  # $label3
                    if (v4 < 0):
                        func439(9688228, v4)
                        v4 = (v4 + 2147483647)
                    # TODO: i32.atomic.rmw.cmpxchg
                    v4 = (v4 | -2147483648)
                    if (v4 != (v4 | -2147483648)):
                        continue
                    break
                break
            v4 = load32(9688232)
            if load32(9688232):
                while True:  # $label5
                    while True:  # $label4
                        if not v4:
                            break
                        if (load32(v4 + 76) >= 0):
                            break
                        store32(v4 + 76, 0)
                        break
                    v4 = load32(v4 + 56)
                    if load32(v4 + 56):
                        continue
                    break
            while True:  # $label6
                if (load32(9688228) >= 0):
                    break
                # TODO: i32.atomic.rmw.add
                if (2147483647 == -2147483647):
                    break
                func97(9688228)
                break
            while True:  # $label7
                v4 = load32(9688032)
                if not load32(9688032):
                    break
                if (load32(v4 + 76) >= 0):
                    break
                store32(v4 + 76, 0)
                break
            while True:  # $label8
                v4 = load32(52736)
                if not load32(52736):
                    break
                if (load32(v4 + 76) >= 0):
                    break
                store32(v4 + 76, 0)
                break
            while True:  # $label9
                v4 = load32(52584)
                if not load32(52584):
                    break
                if (load32(v4 + 76) >= 0):
                    break
                store32(v4 + 76, 0)
                break
            store8(9688037, 1)
        # TODO: memory.fill
        while True:  # $label10
            if (u32((arg1 + 1)) >= u32(2)):
                # TODO: memory.copy
                v4 = load32(v5 + 4)
                if load32(v5 + 4):
                    break
            v4 = a_w()
            store32(v5 + 4, a_w())
            break
        arg1 = (load32(52436) + 148)
        v6 = ((load32(52436) + 148) + (0 if load32(v5 + 12) else (v4 + 15)))
        v4 = e()
        func98(e(), 0, arg1)
        store32(v4 + 48, v6)
        store32(v4 + 44, v4)
        store32(v4, v4)
        arg1 = load32(9688320)
        store32(9688320, (load32(9688320) + 1))
        store32(v4 + 76, (v4 + 76))
        store32(v4 + 24, arg1)
        store32(v4 + 96, 9688068)
        store32(v4 + 32, (3 if load32(v5 + 16) else 2))
        v6 = load32(v5 + 4)
        store32(v4 + 56, load32(v5 + 4))
        arg1 = ((v4 + 139) & -4)
        store32(v4 + 116, ((v4 + 139) & -4))
        arg1 = (arg1 + 6)
        if load32(52436):
            arg1 = ((arg1 + 3) & -4)
            store32(v4 + 72, ((arg1 + 3) & -4))
            arg1 = (load32(52436) + arg1)
        v7 = load32(v5 + 12)
        store32(v4 + 52, (load32(v5 + 12) if v7 else (((arg1 + v6) + 15) & -16)))
        func430(v4)
        arg1 = G.global3
        func264()
        v6 = load32(arg1 + 12)
        store32(v4 + 8, arg1)
        store32(v4 + 12, v6)
        store32(v6 + 8, v4)
        store32(load32(v4 + 8) + 12, v4)
        func263()
        arg1 = load32(9688040)
        store32(9688040, (load32(9688040) + 1))
        if not arg1:
            store8(9688039, 1)
        if a_y():
            arg0 = (load32(9688040) - 1)
            store32(9688040, (load32(9688040) - 1))
            if not arg0:
                store8(9688039, 0)
            func264()
            arg0 = load32(v4 + 12)
            store32(load32(v4 + 12) + 8, load32(v4 + 8))
            store32(load32(v4 + 8) + 12, arg0)
            store32(v4 + 12, v4)
            store32(v4 + 8, v4)
            func263()
            break
        store32(arg0, v4)
        break
    G.global0 = (v5 + 48)

# ----------------------------------------------------------
# $func187
# ----------------------------------------------------------
def func187(arg0):
    while True:  # $label0
        v2 = (arg0 - -64)
        if (load32((arg0 - -64)) >= load32(arg0 + 56)):
            break
        while True:  # $label1
            if (load32(arg0 + 24) > 0):
                break
            func91(0, arg0)
            v1 = (v1 + 1)
            if (load32(v2) < load32(arg0 + 56)):
                continue
            break
        break
    return v1

# ----------------------------------------------------------
# $func188
# ----------------------------------------------------------
def func188():
    v0 = load32(52304)
    if (load32(52304) != load32(52300)):
        store32(9687288, 281)
        store32(9687284, 282)
        store32(9687296, 283)
        store32(9687316, 284)
        store32(9687292, 285)
        store32(9687300, 286)
        store32(9687304, 287)
        store32(9687308, 288)
        store32(9687312, 289)
        store32(9687320, 290)
        store32(9687324, 291)
        store32(9687328, 292)
        store32(52300, v0)

# ----------------------------------------------------------
# $func189
# ----------------------------------------------------------
def func189(arg0, arg1, arg2, arg3, arg4):
    v13 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label10
        while True:  # $label0
            if (arg1 < arg2):
                if (load32(arg0 + 12) < arg2):
                    break
                v8 = load32(arg0 + 8)
                while True:  # $label5
                    while True:  # $label4
                        while True:  # $label2
                            while True:  # $label1
                                while True:  # $label3
                                    # br_table load32(arg0)
                                    break
                                    break
                                break
                                break
                            while True:  # $label9
                                while True:  # $label6
                                    if arg1:
                                        v7 = arg4
                                        break
                                    v5 = (load32(arg3) - 16777216)
                                    store32(arg4, (load32(arg3) - 16777216))
                                    while True:  # $label7
                                        if (v8 < 2):
                                            break
                                        v9 = (arg4 + 4)
                                        v10 = (arg3 + 4)
                                        v7 = (v8 - 1)
                                        v12 = ((v8 - 1) & 1)
                                        if (v8 != 2):
                                            v15 = (v7 & -2)
                                            v7 = 0
                                            while True:  # $label8
                                                v11 = (v6 << 2)
                                                v14 = load32((v10 + v11))
                                                v16 = (((load32((v10 + v11)) & -16711936) + (v5 & -16711936)) & -16711936)
                                                v5 = (((v14 & 16711935) + (v5 & 16711935)) & 16711935)
                                                store32((v9 + (v6 << 2)), ((((load32((v10 + v11)) & -16711936) + (v5 & -16711936)) & -16711936) | (((v14 & 16711935) + (v5 & 16711935)) & 16711935)))
                                                v11 = (v11 | 4)
                                                v11 = load32((v10 + v11))
                                                v5 = ((((load32((v10 + v11)) & -16711936) + v16) & -16711936) | (((v11 & 16711935) + v5) & 16711935))
                                                store32((v9 + (v11 | 4)), ((((load32((v10 + v11)) & -16711936) + v16) & -16711936) | (((v11 & 16711935) + v5) & 16711935)))
                                                v6 = (v6 + 2)
                                                v7 = (v7 + 2)
                                                if ((v7 + 2) != v15):
                                                    continue
                                                break
                                        if not v12:
                                            break
                                        v6 = (v6 << 2)
                                        v6 = load32((v6 + v10))
                                        store32((v9 + (v6 << 2)), ((((load32((v6 + v10)) & -16711936) + (v5 & -16711936)) & -16711936) | (((v6 & 16711935) + (v5 & 16711935)) & 16711935)))
                                        break
                                    v5 = (v8 << 2)
                                    v7 = (arg4 + (v8 << 2))
                                    arg3 = (arg3 + v5)
                                    break
                                v9 = 1
                                if (1 >= arg2):
                                    break
                                v12 = (0 - v8)
                                if (v8 < 2):
                                    while True:  # $label11
                                        if not v7:
                                            break
                                        v5 = load32(arg3)
                                        v6 = load32((v7 + (v12 << 2)))
                                        store32(v7, ((((load32(arg3) & -16711936) + (load32((v7 + (v12 << 2))) & -16711936)) & -16711936) | (((v5 & 16711935) + (v6 & 16711935)) & 16711935)))
                                        v5 = (v8 << 2)
                                        v7 = (v7 + (v8 << 2))
                                        arg3 = (arg3 + v5)
                                        v9 = (v9 + 1)
                                        if ((v9 + 1) != arg2):
                                            continue
                                        break
                                        break
                                    raise Unreachable()
                                v5 = load32(arg0 + 4)
                                v15 = (1 << load32(arg0 + 4))
                                v16 = (0 - (1 << load32(arg0 + 4)))
                                v17 = (v15 - 1)
                                v18 = ((((v15 - 1) + v8) & 0xFFFFFFFF) >> v5)
                                v10 = (load32(arg0 + 16) + ((((((v15 - 1) + v8) & 0xFFFFFFFF) >> v5) * (v9 >> v5)) << 2))
                                while True:  # $label13
                                    if not v7:
                                        break
                                    v5 = load32(arg3)
                                    v19 = (v12 << 2)
                                    v6 = load32((v7 + (v12 << 2)))
                                    store32(v7, ((((load32(arg3) & -16711936) + (load32((v7 + (v12 << 2))) & -16711936)) & -16711936) | (((v5 & 16711935) + (v6 & 16711935)) & 16711935)))
                                    v5 = 1
                                    v6 = v10
                                    while True:  # $label12
                                        v11 = (v5 << 2)
                                        v20 = (v7 + v11)
                                        v14 = ((v5 & v16) + v15)
                                        v14 = (v8 > v14)
                                        v11 = (((v5 & v16) + v15) if (v8 > v14) else v8)
                                        v6 = (v6 + 4)
                                        v5 = v11
                                        if v14:
                                            continue
                                        break
                                    v5 = (v8 << 2)
                                    v7 = (v7 + (v8 << 2))
                                    arg3 = (arg3 + v5)
                                    v9 = (v9 + 1)
                                    v10 = (v10 + ((0 if ((v9 + 1) & v17) else v18) << 2))
                                    if (arg2 != v9):
                                        continue
                                    break
                                break
                            if (load32(arg0 + 12) == arg2):
                                break
                            arg0 = (v8 << 2)
                            # TODO: memory.copy
                            break
                            break
                        arg0 = load32(arg0 + 4)
                        v6 = (1 << load32(arg0 + 4))
                        v11 = ((1 << load32(arg0 + 4)) - 1)
                        v12 = (((((1 << load32(arg0 + 4)) - 1) + v8) & 0xFFFFFFFF) >> arg0)
                        arg0 = (load32(arg0 + 16) + (((((((1 << load32(arg0 + 4)) - 1) + v8) & 0xFFFFFFFF) >> arg0) * (arg1 >> arg0)) << 2))
                        v7 = (v8 & (0 - v6))
                        v9 = (v8 - (v8 & (0 - v6)))
                        while True:  # $label16
                            store8(v13 + 14, 0)
                            store16(v13 + 12, 0)
                            v15 = (arg3 + (v8 << 2))
                            while True:  # $label14
                                if (v7 <= 0):
                                    v5 = arg0
                                    break
                                v14 = (arg3 + (v7 << 2))
                                v5 = arg0
                                while True:  # $label15
                                    v10 = load32(v5)
                                    store8(v13 + 12, load32(v5))
                                    store8(v13 + 14, ((v10 & 0xFFFFFFFF) >> 16))
                                    store8(v13 + 13, ((v10 & 0xFFFFFFFF) >> 8))
                                    v5 = (v5 + 4)
                                    v10 = (v6 << 2)
                                    arg4 = (arg4 + (v6 << 2))
                                    arg3 = (arg3 + v10)
                                    if (u32((arg3 + v10)) < u32(v14)):
                                        continue
                                    break
                                break
                            if (u32(arg3) < u32(v15)):
                                v5 = load32(v5)
                                store8(v13 + 12, load32(v5))
                                store8(v13 + 14, ((v5 & 0xFFFFFFFF) >> 16))
                                store8(v13 + 13, ((v5 & 0xFFFFFFFF) >> 8))
                                v5 = (v9 << 2)
                                arg4 = (arg4 + (v9 << 2))
                                arg3 = (arg3 + v5)
                            arg1 = (arg1 + 1)
                            arg0 = (arg0 + ((0 if ((arg1 + 1) & v11) else v12) << 2))
                            if (arg1 != arg2):
                                continue
                            break
                        break
                        break
                    v5 = load32(arg0 + 4)
                    while True:  # $label17
                        if (arg3 != arg4):
                            break
                        if (v5 <= 0):
                            break
                        arg4 = (arg2 - arg1)
                        arg4 = ((((((v8 + (1 << v5)) - 1) & 0xFFFFFFFF) >> v5) * arg4) << 2)
                        v6 = ((arg3 + ((v8 * (arg2 - arg1)) << 2)) - ((((((v8 + (1 << v5)) - 1) & 0xFFFFFFFF) >> v5) * arg4) << 2))
                        # TODO: memory.copy
                        v9 = load32(arg0 + 16)
                        v7 = load32(arg0 + 8)
                        arg0 = load32(arg0 + 4)
                        if load32(arg0 + 4):
                            if (v7 <= 0):
                                break
                            v8 = ((8 & 0xFFFFFFFF) >> arg0)
                            v10 = ((-1 << ((8 & 0xFFFFFFFF) >> arg0)) ^ -1)
                            v11 = ((-1 << arg0) ^ -1)
                            v15 = (v7 & -2)
                            v14 = (v7 & 1)
                            while True:  # $label20
                                arg4 = 0
                                v5 = 0
                                v12 = 0
                                if (v7 != 1):
                                    while True:  # $label19
                                        if (arg4 & v11):
                                        else:
                                            v5 = load8u(v6 + 1)
                                        arg0 = (v6 + 4)
                                        store32(arg3, load32((v9 + ((v5 & v10) << 2))))
                                        while True:  # $label18
                                            if ((arg4 | 1) & v11):
                                                v6 = arg0
                                                break
                                            v6 = (arg0 + 4)
                                            break
                                        v5 = load8u(arg0 + 1)
                                        store32(v9 + 4, load32((v10 + ((((v5 & 0xFFFFFFFF) >> v8) & load8u(arg0 + 1)) << 2))))
                                        arg4 = (arg4 + 2)
                                        v5 = ((v5 & 0xFFFFFFFF) >> v8)
                                        arg3 = (arg3 + 8)
                                        v12 = (v12 + 2)
                                        if ((v12 + 2) != v15):
                                            continue
                                        break
                                if v14:
                                    if not (arg4 & v11):
                                        v5 = load8u(v6 + 1)
                                        v6 = (v6 + 4)
                                    store32(arg3, load32((v9 + ((v5 & v10) << 2))))
                                    arg3 = (arg3 + 4)
                                arg1 = (arg1 + 1)
                                if ((arg1 + 1) != arg2):
                                    continue
                                break
                            break
                        break
                        break
                    v7 = load32(arg0 + 16)
                    if v5:
                        if (v8 <= 0):
                            break
                        v11 = ((8 & 0xFFFFFFFF) >> v5)
                        v9 = ((-1 << ((8 & 0xFFFFFFFF) >> v5)) ^ -1)
                        v10 = ((-1 << v5) ^ -1)
                        v15 = (v8 & -2)
                        v14 = (v8 & 1)
                        while True:  # $label23
                            v5 = 0
                            v6 = 0
                            v12 = 0
                            if (v8 != 1):
                                while True:  # $label22
                                    if (v5 & v10):
                                    else:
                                        v6 = load8u(arg3 + 1)
                                    arg0 = (arg3 + 4)
                                    store32(arg4, load32((v7 + ((v6 & v9) << 2))))
                                    while True:  # $label21
                                        if ((v5 | 1) & v10):
                                            v6 = ((v6 & 0xFFFFFFFF) >> v11)
                                            break
                                        v6 = load8u(arg0 + 1)
                                        break
                                    arg3 = (arg0 + 4)
                                    store32(arg4 + 4, load32((v7 + ((v6 & v9) << 2))))
                                    v5 = (v5 + 2)
                                    v6 = ((v6 & 0xFFFFFFFF) >> v11)
                                    arg4 = (arg4 + 8)
                                    v12 = (v12 + 2)
                                    if ((v12 + 2) != v15):
                                        continue
                                    break
                            if v14:
                                if not (v5 & v10):
                                    v6 = load8u(arg3 + 1)
                                    arg3 = (arg3 + 4)
                                store32(arg4, load32((v7 + ((v6 & v9) << 2))))
                                arg4 = (arg4 + 4)
                            arg1 = (arg1 + 1)
                            if ((arg1 + 1) != arg2):
                                continue
                            break
                        break
                    break
                G.global0 = (v13 + 16)
                return call_table(load32(9687796))
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 7559

# ----------------------------------------------------------
# $func190
# ----------------------------------------------------------
def func190(arg0):
    if arg0:
        func191(arg0)

# ----------------------------------------------------------
# $func191
# ----------------------------------------------------------
def func191(arg0):
    func116((arg0 + 172))
    func151(load32(arg0 + 168))
    func136((arg0 + 124))
    func136((arg0 + 136))
    # TODO: memory.fill
    store32(arg0 + 16, 0)
    if (load32(arg0 + 192) > 0):
        while True:  # $label0
            v2 = (arg0 + (v1 * 20))
            store32(v2 + 212, 0)
            v1 = (v1 + 1)
            if ((v1 + 1) < load32(arg0 + 192)):
                continue
            break
    store32(arg0 + 276, 0)
    store32(arg0 + 192, 0)
    store32(arg0 + 12, 0)
    store32(arg0 + 280, 0)

# ----------------------------------------------------------
# $func192
# ----------------------------------------------------------
def func192(arg0, arg1, arg2):
    v3 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label31
        v11 = (arg1 - 16)
        v12 = (arg1 - 20)
        v8 = (arg1 - 28)
        while True:  # $label32
            v4 = arg0
            while True:  # $label35
                while True:  # $label0
                    while True:  # $label23
                        while True:  # $label26
                            while True:  # $label3
                                while True:  # $label5
                                    while True:  # $label4
                                        while True:  # $label2
                                            while True:  # $label1
                                                v10 = (arg1 - v4)
                                                v9 = ((arg1 - v4) // 28)
                                                # br_table ((arg1 - v4) // 28)
                                                break
                                                break
                                            arg0 = (arg1 - 28)
                                            if ((load32((arg1 - 28) + 12) * load32(arg0 + 8)) <= (load32(v4 + 12) * load32((v4 + 8)))):
                                                break
                                            store32(v3 + 40, load32((v4 + 24)))
                                            store64(v3 + 32, load64((v4 + 16)))
                                            store64(v3 + 24, load64(v4 + 8))
                                            store64(v3 + 16, load64(v4))
                                            store32(v4 + 24, load32(arg0 + 24))
                                            store64(v4 + 16, load64(arg0 + 16))
                                            store64(v4 + 8, load64(arg0 + 8))
                                            store64(v4, load64(arg0))
                                            store32(arg0 + 24, load32(v3 + 40))
                                            store64(arg0 + 16, load64(v3 + 32))
                                            store64(arg0 + 8, load64(v3 + 24))
                                            store64(arg0, load64(v3 + 16))
                                            break
                                            break
                                        arg1 = (arg1 - 28)
                                        arg2 = (load32(((arg1 - 28) + 12)) * load32(arg1 + 8))
                                        arg0 = (v4 + 28)
                                        v5 = (load32(v4 + 40) * load32(v4 + 36))
                                        if ((load32(v4 + 40) * load32(v4 + 36)) <= (load32(v4 + 12) * load32(v4 + 8))):
                                            if (arg2 <= v5):
                                                break
                                            store32(v3 + 40, load32(arg0 + 24))
                                            store64(v3 + 32, load64(arg0 + 16))
                                            store64(v3 + 24, load64(arg0 + 8))
                                            store64(v3 + 16, load64(arg0))
                                            store32(arg0 + 24, load32(arg1 + 24))
                                            store64(arg0 + 16, load64(arg1 + 16))
                                            store64(arg0 + 8, load64(arg1 + 8))
                                            store64(arg0, load64(arg1))
                                            store32(arg1 + 24, load32(v3 + 40))
                                            store64(arg1 + 16, load64(v3 + 32))
                                            store64(arg1 + 8, load64(v3 + 24))
                                            store64(arg1, load64(v3 + 16))
                                            if ((load32(v4 + 40) * load32(v4 + 36)) <= (load32(v4 + 12) * load32((v4 + 8)))):
                                                break
                                            store32(v3 + 40, load32((v4 + 24)))
                                            store64(v3 + 32, load64((v4 + 16)))
                                            store64(v3 + 24, load64(v4 + 8))
                                            store64(v3 + 16, load64(v4))
                                            store32(v4 + 24, load32(arg0 + 24))
                                            store64(v4 + 16, load64(arg0 + 16))
                                            store64(v4 + 8, load64(arg0 + 8))
                                            store64(v4, load64(arg0))
                                            store32(arg0 + 24, load32(v3 + 40))
                                            store64(arg0 + 16, load64(v3 + 32))
                                            store64(arg0 + 8, load64(v3 + 24))
                                            store64(arg0, load64(v3 + 16))
                                            break
                                        if (arg2 > v5):
                                            store32(v3 + 40, load32((v4 + 24)))
                                            store64(v3 + 32, load64((v4 + 16)))
                                            store64(v3 + 24, load64((v4 + 8)))
                                            store64(v3 + 16, load64(v4))
                                            store32(v4 + 24, load32(arg1 + 24))
                                            store64(v4 + 16, load64(arg1 + 16))
                                            store64(v4 + 8, load64(arg1 + 8))
                                            store64(v4, load64(arg1))
                                            store32(arg1 + 24, load32(v3 + 40))
                                            store64(arg1 + 16, load64(v3 + 32))
                                            store64(arg1 + 8, load64(v3 + 24))
                                            store64(arg1, load64(v3 + 16))
                                            break
                                        store32(v3 + 40, load32((v4 + 24)))
                                        store64(v3 + 32, load64((v4 + 16)))
                                        store64(v3 + 24, load64((v4 + 8)))
                                        store64(v3 + 16, load64(v4))
                                        store32(v4 + 24, load32(arg0 + 24))
                                        store64(v4 + 16, load64(arg0 + 16))
                                        store64(v4 + 8, load64(arg0 + 8))
                                        store64(v4, load64(arg0))
                                        store32(arg0 + 24, load32(v3 + 40))
                                        store64(arg0 + 16, load64(v3 + 32))
                                        store64(arg0 + 8, load64(v3 + 24))
                                        store64(arg0, load64(v3 + 16))
                                        if ((load32(arg1 + 12) * load32(arg1 + 8)) <= (load32(v4 + 40) * load32(v4 + 36))):
                                            break
                                        store32(v3 + 40, load32(arg0 + 24))
                                        store64(v3 + 32, load64(arg0 + 16))
                                        store64(v3 + 24, load64(arg0 + 8))
                                        store64(v3 + 16, load64(arg0))
                                        store32(arg0 + 24, load32(arg1 + 24))
                                        store64(arg0 + 16, load64(arg1 + 16))
                                        store64(arg0 + 8, load64(arg1 + 8))
                                        store64(arg0, load64(arg1))
                                        store32(arg1 + 24, load32(v3 + 40))
                                        store64(arg1 + 16, load64(v3 + 32))
                                        store64(arg1 + 8, load64(v3 + 24))
                                        store64(arg1, load64(v3 + 16))
                                        break
                                        break
                                    break
                                    break
                                if (v10 <= 867):
                                    v5 = (load32(v4 + 68) * load32((v4 - -64)))
                                    arg0 = (v4 + 28)
                                    arg2 = (v4 + 56)
                                    while True:  # $label6
                                        v6 = (load32(v4 + 40) * load32(v4 + 36))
                                        v7 = (load32(v4 + 12) * load32(v4 + 8))
                                        if ((load32(v4 + 40) * load32(v4 + 36)) <= (load32(v4 + 12) * load32(v4 + 8))):
                                            if (v5 <= v6):
                                                break
                                            store32(v3 + 40, load32(arg0 + 24))
                                            store64(v3 + 32, load64(arg0 + 16))
                                            store64(v3 + 24, load64(arg0 + 8))
                                            store64(v3 + 16, load64(arg0))
                                            store32(arg0 + 24, load32((arg2 + 24)))
                                            store64(arg0 + 16, load64((arg2 + 16)))
                                            store64(arg0 + 8, load64((arg2 + 8)))
                                            store64(arg0, load64(arg2))
                                            store32(arg2 + 24, load32(v3 + 40))
                                            store64(arg2 + 16, load64(v3 + 32))
                                            store64(arg2 + 8, load64(v3 + 24))
                                            store64(arg2, load64(v3 + 16))
                                            if ((load32(v4 + 40) * load32(v4 + 36)) <= v7):
                                                break
                                            store32(v3 + 40, load32((v4 + 24)))
                                            store64(v3 + 32, load64((v4 + 16)))
                                            store64(v3 + 24, load64((v4 + 8)))
                                            store64(v3 + 16, load64(v4))
                                            store32(v4 + 24, load32(arg0 + 24))
                                            store64(v4 + 16, load64(arg0 + 16))
                                            store64(v4 + 8, load64(arg0 + 8))
                                            store64(v4, load64(arg0))
                                            store32(arg0 + 24, load32(v3 + 40))
                                            store64(arg0 + 16, load64(v3 + 32))
                                            store64(arg0 + 8, load64(v3 + 24))
                                            store64(arg0, load64(v3 + 16))
                                            break
                                        if (v5 > v6):
                                            store32(v3 + 40, load32((v4 + 24)))
                                            store64(v3 + 32, load64((v4 + 16)))
                                            store64(v3 + 24, load64((v4 + 8)))
                                            store64(v3 + 16, load64(v4))
                                            store32(v4 + 24, load32((arg2 + 24)))
                                            store64(v4 + 16, load64((arg2 + 16)))
                                            store64(v4 + 8, load64((arg2 + 8)))
                                            store64(v4, load64(arg2))
                                            store32(arg2 + 24, load32(v3 + 40))
                                            store64(arg2 + 16, load64(v3 + 32))
                                            store64(arg2 + 8, load64(v3 + 24))
                                            store64(arg2, load64(v3 + 16))
                                            break
                                        store32(v3 + 40, load32((v4 + 24)))
                                        store64(v3 + 32, load64((v4 + 16)))
                                        store64(v3 + 24, load64((v4 + 8)))
                                        store64(v3 + 16, load64(v4))
                                        store32(v4 + 24, load32(arg0 + 24))
                                        store64(v4 + 16, load64(arg0 + 16))
                                        store64(v4 + 8, load64(arg0 + 8))
                                        store64(v4, load64(arg0))
                                        store32(arg0 + 24, load32(v3 + 40))
                                        store64(arg0 + 16, load64(v3 + 32))
                                        store64(arg0 + 8, load64(v3 + 24))
                                        store64(arg0, load64(v3 + 16))
                                        if (v5 <= (load32(v4 + 40) * load32(v4 + 36))):
                                            break
                                        store32(v3 + 40, load32(arg0 + 24))
                                        store64(v3 + 32, load64(arg0 + 16))
                                        store64(v3 + 24, load64(arg0 + 8))
                                        store64(v3 + 16, load64(arg0))
                                        store32(arg0 + 24, load32((arg2 + 24)))
                                        store64(arg0 + 16, load64((arg2 + 16)))
                                        store64(arg0 + 8, load64((arg2 + 8)))
                                        store64(arg0, load64(arg2))
                                        store32(arg2 + 24, load32(v3 + 40))
                                        store64(arg2 + 16, load64(v3 + 32))
                                        store64(arg2 + 8, load64(v3 + 24))
                                        store64(arg2, load64(v3 + 16))
                                        break
                                    v6 = (v4 + 84)
                                    if ((v4 + 84) == arg1):
                                        break
                                    while True:  # $label9
                                        v7 = load32(v6 + 12)
                                        v9 = load32(v6 + 8)
                                        v8 = (load32(v6 + 12) * load32(v6 + 8))
                                        if ((load32(v6 + 12) * load32(v6 + 8)) > (load32(arg2 + 12) * load32(arg2 + 8))):
                                            v14 = load64(v6)
                                            store32(v3 + 24, load32(v6 + 24))
                                            store64(v3 + 16, load64(v6 + 16))
                                            v5 = v6
                                            while True:  # $label8
                                                while True:  # $label7
                                                    arg0 = arg2
                                                    store64(v5, load64(arg2))
                                                    store32(v5 + 24, load32(arg0 + 24))
                                                    store64(v5 + 16, load64(arg0 + 16))
                                                    store64(v5 + 8, load64(arg0 + 8))
                                                    if (arg0 == v4):
                                                        arg0 = v4
                                                        break
                                                    v5 = arg0
                                                    arg2 = (arg0 - 28)
                                                    if (v8 > (load32((arg0 - 28) + 12) * load32(arg2 + 8))):
                                                        continue
                                                    break
                                                break
                                            store32(arg0 + 12, v7)
                                            store32(arg0 + 8, v9)
                                            store64(arg0, v14)
                                            store64(arg0 + 16, load64(v3 + 16))
                                            store32(arg0 + 24, load32(v3 + 24))
                                        arg2 = v6
                                        arg0 = (v6 + 28)
                                        v6 = (v6 + 28)
                                        if (arg0 != arg1):
                                            continue
                                        break
                                    break
                                if not arg2:
                                    if (arg1 == v4):
                                        break
                                    v8 = (((v9 - 2) & 0xFFFFFFFF) >> 1)
                                    arg0 = (((v9 - 2) & 0xFFFFFFFF) >> 1)
                                    while True:  # $label13
                                        while True:  # $label10
                                            v7 = arg0
                                            if (v8 < arg0):
                                                break
                                            arg2 = (v7 << 1)
                                            v6 = ((v7 << 1) | 1)
                                            arg0 = (v4 + (((v7 << 1) | 1) * 28))
                                            arg2 = (arg2 + 2)
                                            if (v9 > (arg2 + 2)):
                                                arg2 = ((load32(arg0 + 12) * load32(arg0 + 8)) > (load32(arg0 + 40) * load32(arg0 + 36)))
                                                v6 = (arg2 if ((load32(arg0 + 12) * load32(arg0 + 8)) > (load32(arg0 + 40) * load32(arg0 + 36))) else v6)
                                                arg0 = ((arg0 + 28) if arg2 else arg0)
                                            v5 = (v4 + (v7 * 28))
                                            v11 = load32((v4 + (v7 * 28)) + 12)
                                            v12 = load32(v5 + 8)
                                            v13 = (load32((v4 + (v7 * 28)) + 12) * load32(v5 + 8))
                                            if ((load32((v4 + (v7 * 28)) + 12) * load32(v5 + 8)) < (load32(arg0 + 12) * load32(arg0 + 8))):
                                                break
                                            v14 = load64(v5)
                                            store32(v3 + 24, load32(v5 + 24))
                                            store64(v3 + 16, load64(v5 + 16))
                                            while True:  # $label12
                                                while True:  # $label11
                                                    arg2 = arg0
                                                    store64(v5, load64(arg0))
                                                    store32(v5 + 24, load32(arg0 + 24))
                                                    store64(v5 + 16, load64(arg0 + 16))
                                                    store64(v5 + 8, load64(arg0 + 8))
                                                    if (v6 > v8):
                                                        break
                                                    v5 = (v6 << 1)
                                                    v6 = ((v6 << 1) | 1)
                                                    arg0 = (v4 + (((v6 << 1) | 1) * 28))
                                                    v5 = (v5 + 2)
                                                    if (v9 > (v5 + 2)):
                                                        v5 = ((load32(arg0 + 12) * load32(arg0 + 8)) > (load32(arg0 + 40) * load32(arg0 + 36)))
                                                        v6 = (v5 if ((load32(arg0 + 12) * load32(arg0 + 8)) > (load32(arg0 + 40) * load32(arg0 + 36))) else v6)
                                                        arg0 = ((arg0 + 28) if v5 else arg0)
                                                    v5 = arg2
                                                    if ((load32(arg0 + 12) * load32(arg0 + 8)) <= v13):
                                                        continue
                                                    break
                                                break
                                            store32(arg2 + 12, v11)
                                            store32(arg2 + 8, v12)
                                            store64(arg2, v14)
                                            store64(arg2 + 16, load64(v3 + 16))
                                            store32(arg2 + 24, load32(v3 + 24))
                                            break
                                        arg0 = (v7 - 1)
                                        if v7:
                                            continue
                                        break
                                    # TODO: i32.div_u
                                    arg0 = 28
                                    while True:  # $label19
                                        store32(v3 + 40, load32(v4 + 24))
                                        store64(v3 + 32, load64(v4 + 16))
                                        store64(v3 + 24, load64(v4 + 8))
                                        store64(v3 + 16, load64(v4))
                                        v6 = arg0
                                        v9 = (((arg0 - 2) & 0xFFFFFFFF) >> 1)
                                        arg2 = 0
                                        v5 = v4
                                        while True:  # $label15
                                            v8 = (arg2 << 1)
                                            v7 = ((arg2 << 1) | 1)
                                            arg0 = (((arg2 * 28) + v5) + 28)
                                            while True:  # $label14
                                                arg2 = (v8 + 2)
                                                if (v6 <= (v8 + 2)):
                                                    arg2 = v7
                                                    break
                                                v7 = ((load32(arg0 + 12) * load32(arg0 + 8)) > (load32(arg0 + 40) * load32(arg0 + 36)))
                                                arg2 = (arg2 if ((load32(arg0 + 12) * load32(arg0 + 8)) > (load32(arg0 + 40) * load32(arg0 + 36))) else v7)
                                                arg0 = ((arg0 + 28) if v7 else arg0)
                                                break
                                            store64(v5, load64(arg0))
                                            store32(v5 + 24, load32((arg0 + 24)))
                                            store64(v5 + 16, load64((arg0 + 16)))
                                            store64(v5 + 8, load64((arg0 + 8)))
                                            v5 = arg0
                                            if (arg2 <= v9):
                                                continue
                                            break
                                        while True:  # $label16
                                            arg1 = (arg1 - 28)
                                            if ((arg1 - 28) == arg0):
                                                store64(arg0, load64(v3 + 16))
                                                store32(arg0 + 24, load32(v3 + 40))
                                                store64(arg0 + 16, load64(v3 + 32))
                                                store64(arg0 + 8, load64(v3 + 24))
                                                break
                                            store64(arg0, load64(arg1))
                                            store32(arg0 + 24, load32((arg1 + 24)))
                                            store64(arg0 + 16, load64((arg1 + 16)))
                                            store64(arg0 + 8, load64((arg1 + 8)))
                                            store64(arg1, load64(v3 + 16))
                                            store64(arg1 + 8, load64(v3 + 24))
                                            store64(arg1 + 16, load64(v3 + 32))
                                            store32(arg1 + 24, load32(v3 + 40))
                                            arg2 = ((arg0 - v4) + 28)
                                            if (((arg0 - v4) + 28) < 29):
                                                break
                                            v7 = load32(arg0 + 12)
                                            v9 = load32(arg0 + 8)
                                            v8 = (load32(arg0 + 12) * load32(arg0 + 8))
                                            # TODO: i32.div_u
                                            v10 = (((28 - 2) & 0xFFFFFFFF) >> 1)
                                            arg2 = (arg2 + ((((28 - 2) & 0xFFFFFFFF) >> 1) * 28))
                                            if (v4 >= (load32((arg2 + ((((28 - 2) & 0xFFFFFFFF) >> 1) * 28)) + 12) * load32(arg2 + 8))):
                                                break
                                            v14 = load64(arg0)
                                            store32(v3 + 8, load32(arg0 + 24))
                                            store64(v3, load64(arg0 + 16))
                                            while True:  # $label18
                                                while True:  # $label17
                                                    v5 = arg2
                                                    store64(arg0, load64(arg2))
                                                    store32(arg0 + 24, load32(v5 + 24))
                                                    store64(arg0 + 16, load64(v5 + 16))
                                                    store64(arg0 + 8, load64(v5 + 8))
                                                    if not v10:
                                                        break
                                                    arg0 = v5
                                                    v10 = (((v10 - 1) & 0xFFFFFFFF) >> 1)
                                                    arg2 = (v4 + ((((v10 - 1) & 0xFFFFFFFF) >> 1) * 28))
                                                    if ((load32((v4 + ((((v10 - 1) & 0xFFFFFFFF) >> 1) * 28)) + 12) * load32(arg2 + 8)) > v8):
                                                        continue
                                                    break
                                                break
                                            store32(v5 + 12, v7)
                                            store32(v5 + 8, v9)
                                            store64(v5, v14)
                                            store64(v5 + 16, load64(v3))
                                            store32(v5 + 24, load32(v3 + 8))
                                            break
                                        arg0 = (v6 - 1)
                                        if (v6 > 2):
                                            continue
                                        break
                                    break
                                v7 = (v4 + (((v9 & 0xFFFFFFFF) >> 1) * 28))
                                while True:  # $label20
                                    if (u32(v10) >= u32(27973)):
                                        arg0 = (((v9 & 0xFFFFFFFF) >> 2) * 28)
                                        break
                                    arg0 = (load32(v11) * load32(v12))
                                    while True:  # $label21
                                        v5 = (load32((v7 + 12)) * load32((v7 + 8)))
                                        if ((load32((v7 + 12)) * load32((v7 + 8))) <= (load32((v4 + 12)) * load32((v4 + 8)))):
                                            if (arg0 <= v5):
                                                break
                                            arg0 = v7
                                            store32(v3 + 40, load32((v7 + 24)))
                                            store64(v3 + 32, load64((arg0 + 16)))
                                            store64(v3 + 24, load64(arg0 + 8))
                                            store64(v3 + 16, load64(arg0))
                                            store32(arg0 + 24, load32(v8 + 24))
                                            store64(arg0 + 16, load64(v8 + 16))
                                            store64(arg0 + 8, load64(v8 + 8))
                                            store64(arg0, load64(v8))
                                            store32(v8 + 24, load32(v3 + 40))
                                            store64(v8 + 16, load64(v3 + 32))
                                            store64(v8 + 8, load64(v3 + 24))
                                            store64(v8, load64(v3 + 16))
                                            if ((load32(arg0 + 12) * load32(arg0 + 8)) <= (load32(v4 + 12) * load32(v4 + 8))):
                                                break
                                            store32(v3 + 40, load32((v4 + 24)))
                                            store64(v3 + 32, load64((v4 + 16)))
                                            store64(v3 + 24, load64(v4 + 8))
                                            store64(v3 + 16, load64(v4))
                                            store32(v4 + 24, load32(arg0 + 24))
                                            store64(v4 + 16, load64(v7 + 16))
                                            store64(v4 + 8, load64(v7 + 8))
                                            store64(v4, load64(v7))
                                            store32(arg0 + 24, load32(v3 + 40))
                                            store64(v7 + 16, load64(v3 + 32))
                                            store64(v7 + 8, load64(v3 + 24))
                                            store64(v7, load64(v3 + 16))
                                            break
                                        if (arg0 > v5):
                                            store32(v3 + 40, load32((v4 + 24)))
                                            store64(v3 + 32, load64((v4 + 16)))
                                            store64(v3 + 24, load64(v4 + 8))
                                            store64(v3 + 16, load64(v4))
                                            store32(v4 + 24, load32(v8 + 24))
                                            store64(v4 + 16, load64(v8 + 16))
                                            store64(v4 + 8, load64(v8 + 8))
                                            store64(v4, load64(v8))
                                            store32(v8 + 24, load32(v3 + 40))
                                            store64(v8 + 16, load64(v3 + 32))
                                            store64(v8 + 8, load64(v3 + 24))
                                            store64(v8, load64(v3 + 16))
                                            break
                                        store32(v3 + 40, load32((v4 + 24)))
                                        store64(v3 + 32, load64((v4 + 16)))
                                        store64(v3 + 24, load64(v4 + 8))
                                        store64(v3 + 16, load64(v4))
                                        arg0 = v7
                                        store32(v4 + 24, load32((v7 + 24)))
                                        store64(v4 + 16, load64((arg0 + 16)))
                                        store64(v4 + 8, load64(arg0 + 8))
                                        store64(v4, load64(arg0))
                                        store32(arg0 + 24, load32(v3 + 40))
                                        store64(arg0 + 16, load64(v3 + 32))
                                        store64(arg0 + 8, load64(v3 + 24))
                                        store64(arg0, load64(v3 + 16))
                                        if ((load32(v11) * load32(v12)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
                                            break
                                        store32(v3 + 40, load32(arg0 + 24))
                                        store64(v3 + 32, load64(v7 + 16))
                                        store64(v3 + 24, load64(v7 + 8))
                                        store64(v3 + 16, load64(v7))
                                        store32(arg0 + 24, load32(v8 + 24))
                                        store64(v7 + 16, load64(v8 + 16))
                                        store64(v7 + 8, load64(v8 + 8))
                                        store64(v7, load64(v8))
                                        store32(v8 + 24, load32(v3 + 40))
                                        store64(v8 + 16, load64(v3 + 32))
                                        store64(v8 + 8, load64(v3 + 24))
                                        store64(v8, load64(v3 + 16))
                                        break
                                    break
                                v10 = 2
                                arg2 = (arg2 - 1)
                                v5 = v8
                                while True:  # $label22
                                    v9 = v4
                                    v4 = (load32((v4 + 12)) * load32((v4 + 8)))
                                    v13 = (load32(v7 + 12) * load32(v7 + 8))
                                    if ((load32((v4 + 12)) * load32((v4 + 8))) > (load32(v7 + 12) * load32(v7 + 8))):
                                        arg0 = v8
                                        break
                                    while True:  # $label25
                                        arg0 = (v5 - 28)
                                        if ((v5 - 28) == v9):
                                            v5 = (v9 + 28)
                                            if (v4 > (load32(v11) * load32(v12))):
                                                break
                                            if (v5 == v8):
                                                break
                                            while True:  # $label24
                                                if ((load32(v5 + 12) * load32((v5 + 8))) < v4):
                                                    store32(v3 + 40, load32((v5 + 24)))
                                                    store64(v3 + 32, load64((v5 + 16)))
                                                    store64(v3 + 24, load64(v5 + 8))
                                                    store64(v3 + 16, load64(v5))
                                                    store32(v5 + 24, load32(v8 + 24))
                                                    store64(v5 + 16, load64(v8 + 16))
                                                    store64(v5 + 8, load64(v8 + 8))
                                                    store64(v5, load64(v8))
                                                    store32(v8 + 24, load32(v3 + 40))
                                                    store64(v8 + 16, load64(v3 + 32))
                                                    store64(v8 + 8, load64(v3 + 24))
                                                    store64(v8, load64(v3 + 16))
                                                    v5 = (v5 + 28)
                                                    break
                                                v5 = (v5 + 28)
                                                if ((v5 + 28) != v8):
                                                    continue
                                                break
                                            break
                                        v6 = (v5 - 28)
                                        v5 = arg0
                                        if ((load32(v6 + 12) * load32(v6 + 8)) <= v13):
                                            continue
                                        break
                                    store32(v3 + 40, load32((v9 + 24)))
                                    store64(v3 + 32, load64((v9 + 16)))
                                    store64(v3 + 24, load64(v9 + 8))
                                    store64(v3 + 16, load64(v9))
                                    store32(v9 + 24, load32((arg0 + 24)))
                                    store64(v9 + 16, load64((arg0 + 16)))
                                    store64(v9 + 8, load64((arg0 + 8)))
                                    store64(v9, load64(arg0))
                                    store32(arg0 + 24, load32(v3 + 40))
                                    store64(arg0 + 16, load64(v3 + 32))
                                    store64(arg0 + 8, load64(v3 + 24))
                                    store64(arg0, load64(v3 + 16))
                                    v10 = (v10 + 1)
                                    break
                                v6 = (v9 + 28)
                                if (u32((v9 + 28)) >= u32(arg0)):
                                    break
                                while True:  # $label29
                                    v5 = (load32(v7 + 12) * load32(v7 + 8))
                                    while True:  # $label27
                                        v4 = v6
                                        v6 = (v6 + 28)
                                        if ((load32(v4 + 12) * load32(v4 + 8)) > v5):
                                            continue
                                        break
                                    while True:  # $label28
                                        arg0 = (arg0 - 28)
                                        if ((load32((arg0 - 28) + 12) * load32((arg0 + 8))) <= v5):
                                            continue
                                        break
                                    if (u32(arg0) < u32(v4)):
                                        v6 = v4
                                        break
                                    else:
                                        store32(v3 + 40, load32(v4 + 24))
                                        store64(v3 + 32, load64(v4 + 16))
                                        store64(v3 + 24, load64(v4 + 8))
                                        store64(v3 + 16, load64(v4))
                                        store32(v4 + 24, load32((arg0 + 24)))
                                        store64(v4 + 16, load64((arg0 + 16)))
                                        store64(v4 + 8, load64(arg0 + 8))
                                        store64(v4, load64(arg0))
                                        store32(arg0 + 24, load32(v3 + 40))
                                        store64(arg0 + 16, load64(v3 + 32))
                                        store64(arg0 + 8, load64(v3 + 24))
                                        store64(arg0, load64(v3 + 16))
                                        v7 = (arg0 if (v4 == v7) else v7)
                                        v10 = (v10 + 1)
                                        continue
                                    raise Unreachable()
                                    break
                                raise Unreachable()
                                break
                            break
                            break
                        while True:  # $label30
                            if (v6 == v7):
                                break
                            if ((load32(v7 + 12) * load32((v7 + 8))) <= (load32(v6 + 12) * load32((v6 + 8)))):
                                break
                            store32(v3 + 40, load32((v6 + 24)))
                            store64(v3 + 32, load64((v6 + 16)))
                            store64(v3 + 24, load64(v6 + 8))
                            store64(v3 + 16, load64(v6))
                            store32(v6 + 24, load32((v7 + 24)))
                            store64(v6 + 16, load64((v7 + 16)))
                            store64(v6 + 8, load64(v7 + 8))
                            store64(v6, load64(v7))
                            store32(v7 + 24, load32(v3 + 40))
                            store64(v7 + 16, load64(v3 + 32))
                            store64(v7 + 8, load64(v3 + 24))
                            store64(v7, load64(v3 + 16))
                            v10 = (v10 + 1)
                            break
                        if not v10:
                            v4 = func419(v9, v6)
                            arg0 = (v6 + 28)
                            if func419((v6 + 28), arg1):
                                arg0 = v9
                                arg1 = v6
                                if not v4:
                                    continue
                                break
                            if v4:
                                continue
                        if (((v6 - v9) // 28) < ((arg1 - v6) // 28)):
                            arg0 = (v6 + 28)
                            continue
                        arg0 = v9
                        arg1 = v6
                        continue
                        break
                    arg0 = v8
                    if (v8 == v5):
                        break
                    while True:  # $label36
                        v6 = (load32(v9 + 12) * load32(v9 + 8))
                        while True:  # $label33
                            v4 = v5
                            v5 = (v5 + 28)
                            if (v6 <= (load32(v4 + 12) * load32((v4 + 8)))):
                                continue
                            break
                        while True:  # $label34
                            arg0 = (arg0 - 28)
                            if (v6 > (load32((arg0 - 28) + 12) * load32((arg0 + 8)))):
                                continue
                            break
                        if (u32(arg0) <= u32(v4)):
                            continue
                        store32(v3 + 40, load32((v4 + 24)))
                        store64(v3 + 32, load64((v4 + 16)))
                        store64(v3 + 24, load64(v4 + 8))
                        store64(v3 + 16, load64(v4))
                        store32(v4 + 24, load32((arg0 + 24)))
                        store64(v4 + 16, load64((arg0 + 16)))
                        store64(v4 + 8, load64(arg0 + 8))
                        store64(v4, load64(arg0))
                        store32(arg0 + 24, load32(v3 + 40))
                        store64(arg0 + 16, load64(v3 + 32))
                        store64(arg0 + 8, load64(v3 + 24))
                        store64(arg0, load64(v3 + 16))
                        continue
                        break
                    raise Unreachable()
                    break
                break
            break
        break
    G.global0 = (v3 + 48)
    return func192((v6 + 28), arg1, arg2)

# ----------------------------------------------------------
# $func193
# ----------------------------------------------------------
def func193(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    v10 = load32(arg2 + 216)
    v18 = load32(arg2 + 208)
    v19 = load32(arg2 + 372)
    while True:  # $label2
        while True:  # $label0
            if not arg6:
                break
            if (v10 <= 0):
                break
            v12 = (load32(arg2 + 220) + arg1)
            if ((load32(arg2 + 220) + arg1) <= arg1):
                break
            v20 = (arg0 + v10)
            v13 = load32(9142440)
            v14 = (load32(9142440) + 2)
            v21 = ((load32(9142440) + 2) * v18)
            v22 = load32(38472)
            v24 = load32(38600)
            v25 = load32(ENTITIES)
            v15 = load32(arg2 + 212)
            v16 = load32(9142840)
            v9 = arg0
            while True:  # $label6
                v11 = (v9 + 1)
                v17 = (v9 - arg0)
                arg6 = arg1
                v8 = arg1
                while True:  # $label4
                    if (u32(v9) < u32(v13)):
                        while True:  # $label3
                            while True:  # $label1
                                if not load8u((v19 + (v17 + ((arg6 - arg1) * v10)))):
                                    arg6 = (arg6 + 1)
                                    break
                                v8 = 0
                                if (u32(arg6) >= u32(v13)):
                                    break
                                if ((arg6 | v9) < 0):
                                    break
                                arg6 = (arg6 + 1)
                                v23 = load32((v16 + ((((v21 + (arg6 + 1)) * v14) + v11) << 2)))
                                if (v15 != load32((v16 + ((((v21 + (arg6 + 1)) * v14) + v11) << 2)))):
                                    v23 = (v25 + (v23 * 132))
                                    v26 = load8u((v25 + (v23 * 132)) + 122)
                                    if not ((v24 == load8u((v25 + (v23 * 132)) + 122)) | (v22 == v26)):
                                        break
                                    if (load16u(v23 + 110) != arg3):
                                        break
                                if (load32((v16 + (((arg6 * v14) + v11) << 2))) != v15):
                                    break
                                break
                            if (arg6 != v12):
                                continue
                            break
                            break
                        raise Unreachable()
                    while True:  # $label5
                        if not load8u((v19 + (v17 + ((v8 - arg1) * v10)))):
                            v8 = (v8 + 1)
                            if (v12 != (v8 + 1)):
                                continue
                            break
                        break
                    v8 = 0
                    break
                    break
                v9 = v11
                if (v11 < v20):
                    continue
                break
            break
        v8 = 1
        if not arg4:
            break
        if (v10 <= 0):
            break
        v11 = load32(arg2 + 220)
        v13 = (load32(arg2 + 220) + arg1)
        if ((load32(arg2 + 220) + arg1) <= arg1):
            break
        arg2 = (u32(v11) > u32(1))
        v14 = (3 if (u32(v11) > u32(1)) else 4)
        v15 = (1 if arg2 else 2)
        v16 = (arg0 + v10)
        arg2 = 0
        v17 = (arg7 != 8)
        arg6 = arg0
        while True:  # $label11
            arg4 = (arg6 + 1)
            v20 = (arg6 - arg0)
            arg6 = arg1
            v8 = arg2
            while True:  # $label10
                while True:  # $label7
                    if not load8u((v19 + (v20 + ((arg6 - arg1) * v10)))):
                        break
                    while True:  # $label8
                        if v17:
                            break
                        if (u32(v8) < u32(v15)):
                            break
                        if (u32(v8) <= u32(v14)):
                            break
                        break
                    v21 = (arg6 + 1)
                    arg7 = (load32(9142440) + 2)
                    arg7 = ((((arg6 + 1) + ((load32(9142440) + 2) * v18)) * arg7) + arg4)
                    v9 = load32(9142840)
                    while True:  # $label9
                        if not arg5:
                            break
                        v12 = entities[load32((v9 + (arg7 << 2)))]
                        v22 = load8u(entities[load32((v9 + (arg7 << 2)))].sub_state)
                        if not ((load8u(entities[load32((v9 + (arg7 << 2)))].sub_state) == load32(38600)) | (load32(38472) == v22)):
                            break
                        if (load16u(v12 + 110) != arg3):
                            break
                        arg7 = (load32(9142440) + 2)
                        arg7 = (((((load32(9142440) + 2) * v18) + v21) * arg7) + arg4)
                        v9 = load32(9142840)
                        break
                    store32((v9 + (arg7 << 2)), arg5)
                    break
                v8 = (v8 + 1)
                arg6 = (arg6 + 1)
                if ((arg6 + 1) != v13):
                    continue
                break
            arg2 = (arg2 + v11)
            arg6 = arg4
            if (arg4 < v16):
                continue
            break
        return 1
        break
    return v8

# ----------------------------------------------------------
# $func194
# ----------------------------------------------------------
def func194(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    v7 = load32(arg2 + 208)
    while True:  # $label0
        while True:  # $label30
            if arg6:
                arg6 = 0
                v14 = load32(9142440)
                v18 = (u32(load32(9142440)) <= u32(arg1))
                if (u32(load32(9142440)) <= u32(arg1)):
                    break
                v17 = (arg0 | arg1)
                if ((arg0 | arg1) < 0):
                    break
                if (u32(arg0) >= u32(v14)):
                    break
                v10 = load32(9142840)
                v16 = (arg0 + 1)
                v11 = (v14 + 2)
                v7 = ((v14 + 2) * v7)
                v19 = (arg1 + ((v14 + 2) * v7))
                v20 = ((arg0 + 1) + (((arg1 + ((v14 + 2) * v7)) + 1) * v11))
                if (load32((load32(9142840) + (((arg0 + 1) + (((arg1 + ((v14 + 2) * v7)) + 1) * v11)) << 2))) != load32(arg2 + 212)):
                    break
                if load32(((players[arg3] + (load32(38452) << 2)) + 281808)):
                    break
                v8 = (arg0 - 1)
                v15 = (v7 + 1)
                v12 = (arg1 - 2)
                v13 = load32(38464)
                v7 = load32(ENTITIES)
                while True:  # $label1
                    arg2 = (arg0 - 2)
                    if (u32((arg0 - 2)) >= u32(v14)):
                        break
                    while True:  # $label2
                        if (u32(v12) >= u32(v14)):
                            break
                        if ((arg2 | v12) < 0):
                            break
                        v9 = load32((v10 + ((v8 + ((v12 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((v8 + ((v12 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v9 * 132))
                        if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v9 * 132)) + 125) - 4)
                        break
                        break
                    while True:  # $label3
                        arg6 = (arg1 - 1)
                        if (u32(v14) <= u32((arg1 - 1))):
                            break
                        if ((arg2 | arg6) < 0):
                            break
                        v9 = load32((v10 + ((v8 + (v11 * v19)) << 2)))
                        if (u32(load32((v10 + ((v8 + (v11 * v19)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v9 * 132))
                        if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v9 * 132)) + 125) - 4)
                        break
                        break
                    while True:  # $label4
                        if v18:
                            break
                        if ((arg1 | arg2) < 0):
                            break
                        v9 = load32((v10 + ((v8 + ((arg1 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((v8 + ((arg1 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v9 * 132))
                        if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v9 * 132)) + 125) - 4)
                        break
                        break
                    while True:  # $label5
                        arg6 = (arg1 + 1)
                        if (u32(v14) <= u32((arg1 + 1))):
                            break
                        if ((arg2 | arg6) < 0):
                            break
                        v9 = load32((v10 + ((v8 + ((arg6 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((v8 + ((arg6 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v9 * 132))
                        if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v9 * 132)) + 125) - 4)
                        break
                        break
                    v9 = (arg1 + 2)
                    if (u32((arg1 + 2)) >= u32(v14)):
                        arg6 = 0
                        break
                    arg6 = 0
                    if ((arg2 | v9) < 0):
                        break
                    arg2 = load32((v10 + ((v8 + ((v9 + v15) * v11)) << 2)))
                    if (u32(load32((v10 + ((v8 + ((v9 + v15) * v11)) << 2)))) < u32(3)):
                        break
                    v9 = (v7 + (arg2 * 132))
                    if (arg3 != load16u((v7 + (arg2 * 132)) + 110)):
                        break
                    if (v13 != load8u(v9 + 122)):
                        break
                    arg2 = load8u((v7 + (arg2 * 132)) + 125)
                    arg6 = (0 - ((load8u((v7 + (arg2 * 132)) + 125) != 14) & (arg2 != 4)))
                    break
                while True:  # $label8
                    while True:  # $label6
                        if (u32(v8) >= u32(v14)):
                            break
                        while True:  # $label7
                            if (u32(v12) >= u32(v14)):
                                break
                            if ((v8 | v12) < 0):
                                break
                            v9 = load32((v10 + ((((v12 + v15) * v11) + arg0) << 2)))
                            if (u32(load32((v10 + ((((v12 + v15) * v11) + arg0) << 2)))) < u32(3)):
                                break
                            arg2 = (v7 + (v9 * 132))
                            if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table (load8u((v7 + (v9 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label9
                            arg2 = (arg1 - 1)
                            if (u32(v14) <= u32((arg1 - 1))):
                                break
                            if ((arg2 | v8) < 0):
                                break
                            v9 = load32((v10 + (((v11 * v19) + arg0) << 2)))
                            if (u32(load32((v10 + (((v11 * v19) + arg0) << 2)))) < u32(3)):
                                break
                            arg2 = (v7 + (v9 * 132))
                            if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table (load8u((v7 + (v9 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label10
                            if v18:
                                break
                            if ((arg1 | v8) < 0):
                                break
                            v9 = load32((v10 + ((((arg1 + v15) * v11) + arg0) << 2)))
                            if (u32(load32((v10 + ((((arg1 + v15) * v11) + arg0) << 2)))) < u32(3)):
                                break
                            arg2 = (v7 + (v9 * 132))
                            if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table (load8u((v7 + (v9 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label11
                            arg2 = (arg1 + 1)
                            if (u32(v14) <= u32((arg1 + 1))):
                                break
                            if ((arg2 | v8) < 0):
                                break
                            v9 = load32((v10 + ((((arg2 + v15) * v11) + arg0) << 2)))
                            if (u32(load32((v10 + ((((arg2 + v15) * v11) + arg0) << 2)))) < u32(3)):
                                break
                            arg2 = (v7 + (v9 * 132))
                            if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table (load8u((v7 + (v9 * 132)) + 125) - 4)
                            break
                            break
                        arg2 = (arg1 + 2)
                        if (u32(v14) <= u32((arg1 + 2))):
                            break
                        if ((arg2 | v8) < 0):
                            break
                        v8 = load32((v10 + ((((arg2 + v15) * v11) + arg0) << 2)))
                        if (u32(load32((v10 + ((((arg2 + v15) * v11) + arg0) << 2)))) < u32(3)):
                            break
                        arg2 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg2 + 122)):
                            break
                        arg2 = 1
                        # br_table (load8u((v7 + (v8 * 132)) + 125) - 4)
                        break
                        break
                    arg2 = arg6
                    break
                while True:  # $label13
                    while True:  # $label12
                        v9 = (u32(v12) >= u32(v14))
                        if (u32(v12) >= u32(v14)):
                            break
                        if ((arg0 | v12) < 0):
                            break
                        v8 = load32((v10 + ((v16 + ((v12 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((v16 + ((v12 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v8 * 132)) + 125) - 4)
                        break
                        break
                    while True:  # $label14
                        arg6 = (arg1 - 1)
                        if (u32(v14) <= u32((arg1 - 1))):
                            break
                        if ((arg0 | arg6) < 0):
                            break
                        v8 = load32((v10 + ((v16 + (v11 * v19)) << 2)))
                        if (u32(load32((v10 + ((v16 + (v11 * v19)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v8 * 132)) + 125) - 4)
                        break
                        break
                    while True:  # $label15
                        if v18:
                            break
                        if (v17 < 0):
                            break
                        v8 = load32((v10 + ((v16 + ((arg1 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((v16 + ((arg1 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v8 * 132)) + 125) - 4)
                        break
                        break
                    while True:  # $label16
                        arg6 = (arg1 + 1)
                        if (u32(v14) <= u32((arg1 + 1))):
                            break
                        if ((arg0 | arg6) < 0):
                            break
                        v8 = load32((v10 + ((v16 + ((arg6 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((v16 + ((arg6 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v8 * 132)) + 125) - 4)
                        break
                        break
                    while True:  # $label17
                        arg6 = (arg1 + 2)
                        if (u32(v14) <= u32((arg1 + 2))):
                            break
                        if ((arg0 | arg6) < 0):
                            break
                        v8 = load32((v10 + ((v16 + ((arg6 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((v16 + ((arg6 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (v8 * 132)) + 125) - 4)
                        break
                        break
                    arg6 = arg2
                    break
                v8 = (arg0 + 2)
                while True:  # $label20
                    while True:  # $label18
                        if (u32(v14) <= u32(v16)):
                            break
                        while True:  # $label19
                            if v9:
                                break
                            if ((v12 | v16) < 0):
                                break
                            v17 = load32((v10 + ((v8 + ((v12 + v15) * v11)) << 2)))
                            if (u32(load32((v10 + ((v8 + ((v12 + v15) * v11)) << 2)))) < u32(3)):
                                break
                            arg2 = (v7 + (v17 * 132))
                            if (load16u((v7 + (v17 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table (load8u((v7 + (v17 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label21
                            arg2 = (arg1 - 1)
                            if (u32(v14) <= u32((arg1 - 1))):
                                break
                            if ((arg2 | v16) < 0):
                                break
                            v17 = load32((v10 + ((v8 + (v11 * v19)) << 2)))
                            if (u32(load32((v10 + ((v8 + (v11 * v19)) << 2)))) < u32(3)):
                                break
                            arg2 = (v7 + (v17 * 132))
                            if (load16u((v7 + (v17 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table (load8u((v7 + (v17 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label22
                            if v18:
                                break
                            if ((arg1 | v16) < 0):
                                break
                            v17 = load32((v10 + ((v8 + ((arg1 + v15) * v11)) << 2)))
                            if (u32(load32((v10 + ((v8 + ((arg1 + v15) * v11)) << 2)))) < u32(3)):
                                break
                            arg2 = (v7 + (v17 * 132))
                            if (load16u((v7 + (v17 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table (load8u((v7 + (v17 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label23
                            arg2 = (arg1 + 1)
                            if (u32(v14) <= u32((arg1 + 1))):
                                break
                            if ((arg2 | v16) < 0):
                                break
                            v17 = load32((v10 + ((v8 + ((arg2 + v15) * v11)) << 2)))
                            if (u32(load32((v10 + ((v8 + ((arg2 + v15) * v11)) << 2)))) < u32(3)):
                                break
                            arg2 = (v7 + (v17 * 132))
                            if (load16u((v7 + (v17 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table (load8u((v7 + (v17 * 132)) + 125) - 4)
                            break
                            break
                        arg2 = (arg1 + 2)
                        if (u32(v14) <= u32((arg1 + 2))):
                            break
                        if ((arg2 | v16) < 0):
                            break
                        v16 = load32((v10 + ((v8 + ((arg2 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((v8 + ((arg2 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg2 = (v7 + (v16 * 132))
                        if (load16u((v7 + (v16 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg2 + 122)):
                            break
                        arg2 = 1
                        # br_table (load8u((v7 + (v16 * 132)) + 125) - 4)
                        break
                        break
                    arg2 = arg6
                    break
                while True:  # $label26
                    while True:  # $label24
                        if (u32(v8) >= u32(v14)):
                            break
                        arg0 = (arg0 + 3)
                        while True:  # $label25
                            if v9:
                                break
                            if ((v8 | v12) < 0):
                                break
                            v12 = load32((v10 + ((arg0 + ((v12 + v15) * v11)) << 2)))
                            if (u32(load32((v10 + ((arg0 + ((v12 + v15) * v11)) << 2)))) < u32(3)):
                                break
                            arg6 = (v7 + (v12 * 132))
                            if (load16u((v7 + (v12 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg6 + 122)):
                                break
                            arg6 = 1
                            # br_table (load8u((v7 + (v12 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label27
                            arg6 = (arg1 - 1)
                            if (u32(v14) <= u32((arg1 - 1))):
                                break
                            if ((arg6 | v8) < 0):
                                break
                            v12 = load32((v10 + ((arg0 + (v11 * v19)) << 2)))
                            if (u32(load32((v10 + ((arg0 + (v11 * v19)) << 2)))) < u32(3)):
                                break
                            arg6 = (v7 + (v12 * 132))
                            if (load16u((v7 + (v12 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg6 + 122)):
                                break
                            arg6 = 1
                            # br_table (load8u((v7 + (v12 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label28
                            if v18:
                                break
                            if ((arg1 | v8) < 0):
                                break
                            v12 = load32((v10 + ((arg0 + ((arg1 + v15) * v11)) << 2)))
                            if (u32(load32((v10 + ((arg0 + ((arg1 + v15) * v11)) << 2)))) < u32(3)):
                                break
                            arg6 = (v7 + (v12 * 132))
                            if (load16u((v7 + (v12 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg6 + 122)):
                                break
                            arg6 = 1
                            # br_table (load8u((v7 + (v12 * 132)) + 125) - 4)
                            break
                            break
                        while True:  # $label29
                            arg6 = (arg1 + 1)
                            if (u32(v14) <= u32((arg1 + 1))):
                                break
                            if ((arg6 | v8) < 0):
                                break
                            v12 = load32((v10 + ((arg0 + ((arg6 + v15) * v11)) << 2)))
                            if (u32(load32((v10 + ((arg0 + ((arg6 + v15) * v11)) << 2)))) < u32(3)):
                                break
                            arg6 = (v7 + (v12 * 132))
                            if (load16u((v7 + (v12 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg6 + 122)):
                                break
                            arg6 = 1
                            # br_table (load8u((v7 + (v12 * 132)) + 125) - 4)
                            break
                            break
                        arg1 = (arg1 + 2)
                        if (u32(v14) <= u32((arg1 + 2))):
                            break
                        if ((arg1 | v8) < 0):
                            break
                        arg0 = load32((v10 + ((arg0 + ((arg1 + v15) * v11)) << 2)))
                        if (u32(load32((v10 + ((arg0 + ((arg1 + v15) * v11)) << 2)))) < u32(3)):
                            break
                        arg1 = (v7 + (arg0 * 132))
                        if (load16u((v7 + (arg0 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg1 + 122)):
                            break
                        arg6 = 1
                        # br_table (load8u((v7 + (arg0 * 132)) + 125) - 4)
                        break
                        break
                    arg6 = arg2
                    break
                if not (arg6 & 1):
                    break
                if arg4:
                    break
                break
            arg6 = 1
            if not arg4:
                break
            arg2 = (load32(9142440) + 2)
            v20 = ((arg0 + (((arg1 + ((load32(9142440) + 2) * v7)) + 1) * arg2)) + 1)
            v10 = load32(9142840)
            break
        store32((v10 + (v20 << 2)), arg5)
        arg6 = 1
        break
    return (arg6 & 1)

# ----------------------------------------------------------
# $func195
# ----------------------------------------------------------
def func195():
    v1 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v0 = load32(9681808)
    if load32(9681808):
        v6 = load32(((load8u(entities[v0].sub_state) * 404) + ENTITY_TYPES) + 144)
    while True:  # $label0
        v2 = load32(9681812)
        if not load32(9681812):
            break
        v5 = load32(ENTITIES)
        v3 = load8u(entities[v2].sub_state)
        v7 = load32(((load8u(entities[v2].sub_state) * 404) + ENTITY_TYPES) + 144)
        if not v0:
            break
        if (v0 == v2):
            break
        v0 = (v5 + (v0 * 132))
        v8 = ((load8u((v5 + (v0 * 132)) + 122) * 404) + ENTITY_TYPES)
        v9 = load16u(v0 + 112)
        v2 = (v5 + (v2 * 132))
        v5 = load16u((v5 + (v2 * 132)) + 112)
        v3 = ((v3 * 404) + ENTITY_TYPES)
        v10 = ((((load32(((load8u((v5 + (v0 * 132)) + 122) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v0 + 112)) - (load16u((v5 + (v2 * 132)) + 112) + ((load32(((v3 * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1)))
        v0 = load16u(v0 + 114)
        v2 = load16u(v2 + 114)
        v3 = ((load16u(v0 + 114) + ((load32(v8 + 220) & 0xFFFFFFFF) >> 1)) - (load16u(v2 + 114) + ((load32(v3 + 220) & 0xFFFFFFFF) >> 1)))
        if ((((((((load32(((load8u((v5 + (v0 * 132)) + 122) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v0 + 112)) - (load16u((v5 + (v2 * 132)) + 112) + ((load32(((v3 * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1))) * v10) + (((load16u(v0 + 114) + ((load32(v8 + 220) & 0xFFFFFFFF) >> 1)) - (load16u(v2 + 114) + ((load32(v3 + 220) & 0xFFFFFFFF) >> 1))) * v3)) - 1) < 82):
            break
        v4 = load32(9681804)
        v12 = 0.800000012
        v0 = (v0 - v2)
        v0 = (v9 - v5)
        v3 = players[load32(CURRENT_PLAYER)]
        if (load32(((players[load32(CURRENT_PLAYER)] + (load32(39108) << 2)) + 281808)) != 1):
        else:
        # TODO: f64.promote_f32
        v11 = ((((0.800000012 if (load32(((v3 + (load32(39168) << 2)) + 281808)) == 1) else 0.75) * (0.800000012 * i32(v4))) / 500.0) + 0.5)
        if ((((((0.800000012 if (load32(((v3 + (load32(39168) << 2)) + 281808)) == 1) else 0.75) * (0.800000012 * i32(v4))) / 500.0) + 0.5) < 4294967296.0) & (v11 >= 0.0)):
            v4 = i32(v11)
            break
        v4 = 0
        break
    store32(v1 + 16, load32(9681820))
    store32(v1 + 20, v4)
    store32(v1 + 4, v6)
    store32(v1 + 8, v7)
    store32(v1, load32(9681804))
    store32(v1 + 12, load32(9681816))
    G.global0 = (v1 + 32)
    return v1

# ----------------------------------------------------------
# $func196
# ----------------------------------------------------------
def func196(arg0, arg1, arg2, arg3, arg4):
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v6 = func197(arg0, arg1, arg2, arg3)
    while True:  # $label0
        if ((load32(arg4 + 12) * load32(arg4 + 8)) <= (load32(arg3 + 12) * load32(arg3 + 8))):
            break
        store32(v5 + 24, load32(arg3 + 24))
        store64(v5 + 16, load64(arg3 + 16))
        store64(v5 + 8, load64(arg3 + 8))
        store64(v5, load64(arg3))
        store32(arg3 + 24, load32(arg4 + 24))
        store64(arg3 + 16, load64(arg4 + 16))
        store64(arg3 + 8, load64(arg4 + 8))
        store64(arg3, load64(arg4))
        store32(arg4 + 24, load32(v5 + 24))
        store64(arg4 + 16, load64(v5 + 16))
        store64(arg4 + 8, load64(v5 + 8))
        store64(arg4, load64(v5))
        if ((load32(arg3 + 12) * load32(arg3 + 8)) <= (load32(arg2 + 12) * load32(arg2 + 8))):
            v6 = (v6 + 1)
            break
        store32(v5 + 24, load32(arg2 + 24))
        store64(v5 + 16, load64(arg2 + 16))
        store64(v5 + 8, load64(arg2 + 8))
        store64(v5, load64(arg2))
        store32(arg2 + 24, load32(arg3 + 24))
        store64(arg2 + 16, load64(arg3 + 16))
        store64(arg2 + 8, load64(arg3 + 8))
        store64(arg2, load64(arg3))
        store32(arg3 + 24, load32(v5 + 24))
        store64(arg3 + 16, load64(v5 + 16))
        store64(arg3 + 8, load64(v5 + 8))
        store64(arg3, load64(v5))
        if ((load32(arg2 + 12) * load32(arg2 + 8)) <= (load32(arg1 + 12) * load32(arg1 + 8))):
            v6 = (v6 + 2)
            break
        store32(v5 + 24, load32(arg1 + 24))
        store64(v5 + 16, load64(arg1 + 16))
        store64(v5 + 8, load64(arg1 + 8))
        store64(v5, load64(arg1))
        store32(arg1 + 24, load32(arg2 + 24))
        store64(arg1 + 16, load64(arg2 + 16))
        store64(arg1 + 8, load64(arg2 + 8))
        store64(arg1, load64(arg2))
        store32(arg2 + 24, load32(v5 + 24))
        store64(arg2 + 16, load64(v5 + 16))
        store64(arg2 + 8, load64(v5 + 8))
        store64(arg2, load64(v5))
        if ((load32(arg1 + 12) * load32(arg1 + 8)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
            v6 = (v6 + 3)
            break
        store32(v5 + 24, load32(arg0 + 24))
        store64(v5 + 16, load64(arg0 + 16))
        store64(v5 + 8, load64(arg0 + 8))
        store64(v5, load64(arg0))
        store32(arg0 + 24, load32(arg1 + 24))
        store64(arg0 + 16, load64(arg1 + 16))
        store64(arg0 + 8, load64(arg1 + 8))
        store64(arg0, load64(arg1))
        store32(arg1 + 24, load32(v5 + 24))
        store64(arg1 + 16, load64(v5 + 16))
        store64(arg1 + 8, load64(v5 + 8))
        store64(arg1, load64(v5))
        v6 = (v6 + 4)
        break
    G.global0 = (v5 + 32)
    return v6

# ----------------------------------------------------------
# $func197
# ----------------------------------------------------------
def func197(arg0, arg1, arg2, arg3):
    v4 = (G.global0 - 32)
    v5 = (load32(arg2 + 12) * load32(arg2 + 8))
    while True:  # $label0
        while True:  # $label1
            v6 = (load32(arg1 + 12) * load32(arg1 + 8))
            if ((load32(arg1 + 12) * load32(arg1 + 8)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
                if (v5 <= v6):
                    break
                store32(v4 + 24, load32(arg1 + 24))
                store64(v4 + 16, load64(arg1 + 16))
                store64(v4 + 8, load64(arg1 + 8))
                store64(v4, load64(arg1))
                store32(arg1 + 24, load32(arg2 + 24))
                store64(arg1 + 16, load64(arg2 + 16))
                store64(arg1 + 8, load64(arg2 + 8))
                store64(arg1, load64(arg2))
                store32(arg2 + 24, load32(v4 + 24))
                store64(arg2 + 16, load64(v4 + 16))
                store64(arg2 + 8, load64(v4 + 8))
                store64(arg2, load64(v4))
                if ((load32(arg1 + 12) * load32(arg1 + 8)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
                    break
                store32(v4 + 24, load32(arg0 + 24))
                store64(v4 + 16, load64(arg0 + 16))
                store64(v4 + 8, load64(arg0 + 8))
                store64(v4, load64(arg0))
                store32(arg0 + 24, load32(arg1 + 24))
                store64(arg0 + 16, load64(arg1 + 16))
                store64(arg0 + 8, load64(arg1 + 8))
                store64(arg0, load64(arg1))
                store32(arg1 + 24, load32(v4 + 24))
                store64(arg1 + 16, load64(v4 + 16))
                store64(arg1 + 8, load64(v4 + 8))
                store64(arg1, load64(v4))
                break
            if (v5 > v6):
                store32(v4 + 24, load32(arg0 + 24))
                store64(v4 + 16, load64(arg0 + 16))
                store64(v4 + 8, load64(arg0 + 8))
                store64(v4, load64(arg0))
                store32(arg0 + 24, load32(arg2 + 24))
                store64(arg0 + 16, load64(arg2 + 16))
                store64(arg0 + 8, load64(arg2 + 8))
                store64(arg0, load64(arg2))
                store32(arg2 + 24, load32(v4 + 24))
                store64(arg2 + 16, load64(v4 + 16))
                store64(arg2 + 8, load64(v4 + 8))
                store64(arg2, load64(v4))
                break
            store32(v4 + 24, load32(arg0 + 24))
            store64(v4 + 16, load64(arg0 + 16))
            store64(v4 + 8, load64(arg0 + 8))
            store64(v4, load64(arg0))
            store32(arg0 + 24, load32(arg1 + 24))
            store64(arg0 + 16, load64(arg1 + 16))
            store64(arg0 + 8, load64(arg1 + 8))
            store64(arg0, load64(arg1))
            store32(arg1 + 24, load32(v4 + 24))
            store64(arg1 + 16, load64(v4 + 16))
            store64(arg1 + 8, load64(v4 + 8))
            store64(arg1, load64(v4))
            if ((load32(arg2 + 12) * load32(arg2 + 8)) <= (load32(arg1 + 12) * load32(arg1 + 8))):
                break
            store32(v4 + 24, load32(arg1 + 24))
            store64(v4 + 16, load64(arg1 + 16))
            store64(v4 + 8, load64(arg1 + 8))
            store64(v4, load64(arg1))
            store32(arg1 + 24, load32(arg2 + 24))
            store64(arg1 + 16, load64(arg2 + 16))
            store64(arg1 + 8, load64(arg2 + 8))
            store64(arg1, load64(arg2))
            store32(arg2 + 24, load32(v4 + 24))
            store64(arg2 + 16, load64(v4 + 16))
            store64(arg2 + 8, load64(v4 + 8))
            store64(arg2, load64(v4))
            break
        break
    v5 = 2
    if ((load32(arg3 + 12) * load32(arg3 + 8)) > (load32(arg2 + 12) * load32(arg2 + 8))):
        store32(v4 + 24, load32(arg2 + 24))
        store64(v4 + 16, load64(arg2 + 16))
        store64(v4 + 8, load64(arg2 + 8))
        store64(v4, load64(arg2))
        store32(arg2 + 24, load32(arg3 + 24))
        store64(arg2 + 16, load64(arg3 + 16))
        store64(arg2 + 8, load64(arg3 + 8))
        store64(arg2, load64(arg3))
        store32(arg3 + 24, load32(v4 + 24))
        store64(arg3 + 16, load64(v4 + 16))
        store64(arg3 + 8, load64(v4 + 8))
        store64(arg3, load64(v4))
        if ((load32(arg2 + 12) * load32(arg2 + 8)) <= (load32(arg1 + 12) * load32(arg1 + 8))):
            return (v5 + 1)
        store32(v4 + 24, load32(arg1 + 24))
        store64(v4 + 16, load64(arg1 + 16))
        store64(v4 + 8, load64(arg1 + 8))
        store64(v4, load64(arg1))
        store32(arg1 + 24, load32(arg2 + 24))
        store64(arg1 + 16, load64(arg2 + 16))
        store64(arg1 + 8, load64(arg2 + 8))
        store64(arg1, load64(arg2))
        store32(arg2 + 24, load32(v4 + 24))
        store64(arg2 + 16, load64(v4 + 16))
        store64(arg2 + 8, load64(v4 + 8))
        store64(arg2, load64(v4))
        if ((load32(arg1 + 12) * load32(arg1 + 8)) <= (load32(arg0 + 12) * load32(arg0 + 8))):
            return (v5 + 2)
        store32(v4 + 24, load32(arg0 + 24))
        store64(v4 + 16, load64(arg0 + 16))
        store64(v4 + 8, load64(arg0 + 8))
        store64(v4, load64(arg0))
        store32(arg0 + 24, load32(arg1 + 24))
        store64(arg0 + 16, load64(arg1 + 16))
        store64(arg0 + 8, load64(arg1 + 8))
        store64(arg0, load64(arg1))
        store32(arg1 + 24, load32(v4 + 24))
        store64(arg1 + 16, load64(v4 + 16))
        store64(arg1 + 8, load64(v4 + 8))
        store64(arg1, load64(v4))
    else:
    return v5

# ----------------------------------------------------------
# $func198
# ----------------------------------------------------------
def func198(arg0):
    v1 = load32(PLAYERS)
    store32(arg0 + 80, 0)
    v2 = (load32(arg0 + 84) + 1)
    store32(arg0 + 84, (load32(arg0 + 84) + 1))
    v1 = (v1 + (load16u(arg0 + 110) * 286704))
    v3 = ((v1 + (load16u(arg0 + 110) * 286704)) + 281672)
    store32(((v1 + (load16u(arg0 + 110) * 286704)) + 281672), (load32(v3) + 1))
    if (load32((v1 + 284388)) == v2):
        func201(arg0)
        store32(v1 + 283936, (load32(v1 + 283936) + 1))
        v2 = (v1 + 281636)
        store32((v1 + 281636), (load32(v2) + 1))
    v1 = (v1 + 284020)
    store32(arg0 + 64, (load32(arg0 + 64) + load32((v1 + 284020))))
    store32(arg0 + 68, (load32(arg0 + 68) + load32(v1)))
    v1 = load32(arg0 + 84)
    v2 = (load32(arg0 + 84) & 1)
    v3 = (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 224) > 1)
    store32(arg0 + 52, (load32(arg0 + 52) + ((load32(arg0 + 84) & 1) if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 224) > 1) else 1)))
    store32(arg0 + 60, (load32(arg0 + 60) + (((v1 & 3) == 1) if v3 else v2)))
    while True:  # $label0
        if not load32(arg0 + 92):
            break
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break

# ----------------------------------------------------------
# $func199
# ----------------------------------------------------------
def func199(arg0):
    v2 = (G.global0 - 112)
    G.global0 = (G.global0 - 112)
    while True:  # $label0
        v1 = load32(arg0 + 12)
        if not load32(arg0 + 12):
            break
        v8 = load32(load32(v1))
        if not load32(load32(v1)):
            break
        if not load32(arg0 + 40):
            break
        v1 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES))
        if load8u(9142916):
            while True:  # $label1
                if not v1:
                    break
                if not load32(v1 + 20):
                    break
                v4 = load32(v1 + 28)
                if (load32(v1 + 28) != 2147483647):
                    break
                v4 = load32(59152)
                store32(59152, (load32(59152) + 1))
                v3 = load32(9568052)
                store32(v1 + 28, v4)
                v6 = load32(v1)
                arg0 = load32(v1 + 4)
                v5 = load32(9568048)
                store32(9568048, (load32(9568048) + 1))
                store32(((v5 << 2) + 9563952), v1)
                store32(9568052, (v3 + ((v6 * (arg0 + 2)) << 2)))
                v3 = load32(9568056)
                store32(v1 + 56, load32(9568056))
                store32(9568056, (v3 + ((arg0 * load32(v1)) << 2)))
                break
            store32(v2 + 96, v8)
            store32(v2 + 80, v4)
            # TODO: f64.promote_f32
            storef64(v2 + 88, i32((load32(9142848) * 25)))
            a_b()
            break
        v6 = load32(v1 + 16)
        while True:  # $label2
            v5 = load32(v1 + 20)
            if not load32(v1 + 20):
                v7 = load32(v1)
                break
            v7 = load8u(arg0 + 124)
            while True:  # $label3
                v3 = load32(v1 + 28)
                if (load32(v1 + 28) != 2147483647):
                    v4 = load32(v1 + 4)
                    break
                v9 = load32(v1)
                v10 = load32(9568052)
                v3 = ((load32(v1) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                store32(v1 + 28, ((load32(v1) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2)))
                v4 = load32(v1 + 4)
                store32(9568052, (v10 + ((v9 * (load32(v1 + 4) + 2)) << 2)))
                v9 = load32(9568048)
                store32(9568048, (load32(9568048) + 1))
                store32(((v9 << 2) + 9563952), v1)
                break
            v7 = load32(v1)
            # TODO: i32.div_u
            break
        v4 = (v5 + v3)
        v3 = 0
        v5 = (v5 * v6)
        if (v5 * v6):
            v3 = (load32(v1 + 4) // v5)
        v5 = load16u(arg0 + 110)
        storef64(v2 + 56, i32((v6 << 16)))
        store32((v2 - -64), v8)
        store32(v2 + 48, (v5 + 16))
        # TODO: f64.promote_f32
        storef64(v2 + 40, i32((load32(9142848) * 25)))
        # TODO: f64.promote_f32
        storef64(v2 + 32, (i32((((v3 * v7) * 6) + v4)) / i32(load32(59156))))
        a_b()
        v12 = (i32(load16u(arg0 + 114)) * 32.0)
        v13 = (i32(load16u(arg0 + 112)) * 32.0)
        while True:  # $label4
            if not load8u(9142916):
                v11 = i32(load32(v1 + 8))
                v15 = 32.0
                break
            # TODO: f64.promote_f32
            v15 = ((16.0 / i32((load32(9142440) * 96))) + 0.25)
            break
        v14 = 0.0
        store32(v2 + 24, v8)
        storef64(v2 + 16, v15)
        # TODO: f64.promote_f32
        storef64(v2 + 8, (v12 - v14))
        # TODO: f64.promote_f32
        storef64(v2, (v13 - v11))
        a_b()
        break
    G.global0 = (v2 + 112)
    return v2

# ----------------------------------------------------------
# $func200
# ----------------------------------------------------------
def func200(arg0, arg1, arg2, arg3):
    while True:  # $label0
        v7 = load32(PLAYERS)
        v5 = load16u(arg0 + 110)
        v10 = players[load16u(arg0 + 110)]
        if not load32(players[load16u(arg0 + 110)] + 286684):
            break
        v12 = load8u(arg0 + 122)
        v31 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264)
        if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) == 1):
            break
        if (load32(38456) == v12):
            break
        if (load32(38764) == v12):
            break
        while True:  # $label1
            v4 = load32(v10 + 283904)
            if not (load32(v10 + 283904) | arg1):
                break
            if not arg1:
                v25 = (load32(PLAYER_COUNT) * v5)
                v26 = ((v12 * 404) + ENTITY_TYPES)
                v27 = load32(ENTITIES)
                v17 = entities[load32(arg0 + 28)]
                v10 = load32(9142432)
                v28 = load16u(arg0 + 112)
                v18 = load32(9142440)
                v29 = load16u(arg0 + 114)
                v32 = (load32(9142432) + ((load16u(arg0 + 112) + (load32(9142440) * load16u(arg0 + 114))) << 2))
                v16 = load32(9215880)
                v33 = load32(38564)
                v34 = load32(38620)
                v35 = load32(38560)
                v30 = load32(9143004)
                v36 = load32(38500)
                v12 = 2147483647
                v37 = (v7 + (v4 * 286704))
                arg1 = 0
                while True:  # $label20
                    while True:  # $label2
                        v7 = load32(((v37 + (v19 << 2)) + 284636))
                        if not load32(((v37 + (v19 << 2)) + 284636)):
                            break
                        v38 = load32(v7 + 8)
                        if not load32(v7 + 8):
                            break
                        v39 = load32(v7)
                        v20 = 0
                        while True:  # $label19
                            while True:  # $label3
                                v7 = load32((v39 + (v20 << 2)))
                                if not load32((v39 + (v20 << 2))):
                                    break
                                v5 = (v27 + (v7 * 132))
                                v21 = load16u((v27 + (v7 * 132)) + 114)
                                v7 = (load16u((v27 + (v7 * 132)) + 114) - v29)
                                v22 = load16u(v5 + 112)
                                v7 = (load16u(v5 + 112) - v28)
                                v7 = (((load16u((v27 + (v7 * 132)) + 114) - v29) * v7) + ((load16u(v5 + 112) - v28) * v7))
                                if ((((load16u((v27 + (v7 * 132)) + 114) - v29) * v7) + ((load16u(v5 + 112) - v28) * v7)) >= v12):
                                    break
                                v9 = load8u(v5 + 122)
                                if not func162(arg0, load8u(v5 + 122), 0, 0):
                                    break
                                if (v9 == v36):
                                    break
                                v4 = load16u(v5 + 110)
                                while True:  # $label4
                                    v6 = load16u(v5 + 120)
                                    if load16u(v5 + 120):
                                    else:
                                    if not load8u(((v6 if load8u((v30 + (v4 + v25))) else v4) + (v4 + v25))):
                                        if (load8u(v5 + 127) != 6):
                                            break
                                        if not load8u(v5 + 128):
                                            break
                                        break
                                    if load8u(v5 + 128):
                                        break
                                    break
                                if (load8u(v5 + 125) == 10):
                                    break
                                if (load8u(v5 + 126) == 2):
                                    break
                                v23 = load32(v5 + 64)
                                if (load32(v5 + 64) == -1):
                                    break
                                v13 = ((v9 * 404) + ENTITY_TYPES)
                                v4 = load32(((v9 * 404) + ENTITY_TYPES) + 264)
                                if (load32(((v9 * 404) + ENTITY_TYPES) + 264) == 2):
                                    break
                                if (load32(v13 + 188) != 55):
                                    break
                                if (v9 == v35):
                                    break
                                if (v9 == v34):
                                    break
                                if (v9 == v33):
                                    break
                                if load32(v5 + 36):
                                    break
                                while True:  # $label7
                                    while True:  # $label5
                                        while True:  # $label6
                                            # br_table v4
                                            break
                                            break
                                        v8 = 0
                                        v11 = load32(v13 + 216)
                                        if not load32(v13 + 216):
                                            break
                                        v14 = load32(v13 + 220)
                                        if not load32(v13 + 220):
                                            break
                                        if not v16:
                                            break
                                        if not v10:
                                            break
                                        v15 = load32(v16)
                                        v6 = 0
                                        while True:  # $label9
                                            v24 = (v6 + v22)
                                            v4 = 0
                                            while True:  # $label8
                                                v8 = load32((v10 + ((v24 + ((v4 + v21) * v18)) << 2)))
                                                if not load32((v15 + (load32((v10 + ((v24 + ((v4 + v21) * v18)) << 2))) << 2))):
                                                    break
                                                v4 = (v4 + 1)
                                                if ((v4 + 1) != v14):
                                                    continue
                                                break
                                            v8 = 0
                                            v6 = (v6 + 1)
                                            if ((v6 + 1) != v11):
                                                continue
                                            break
                                        break
                                        break
                                    if not v10:
                                        v8 = 0
                                        break
                                    v8 = load32((v10 + (((v18 * v21) + v22) << 2)))
                                    break
                                while True:  # $label12
                                    while True:  # $label10
                                        while True:  # $label11
                                            # br_table v31
                                            break
                                            break
                                        v6 = 0
                                        v14 = load32(v26 + 216)
                                        if not load32(v26 + 216):
                                            break
                                        v15 = load32(v26 + 220)
                                        if not load32(v26 + 220):
                                            break
                                        if not v16:
                                            break
                                        if not v10:
                                            break
                                        v24 = load32(v16)
                                        v11 = 0
                                        while True:  # $label14
                                            v40 = (v11 + v28)
                                            v4 = 0
                                            while True:  # $label13
                                                v6 = load32((v10 + ((v40 + ((v4 + v29) * v18)) << 2)))
                                                if not load32((v24 + (load32((v10 + ((v40 + ((v4 + v29) * v18)) << 2))) << 2))):
                                                    break
                                                v4 = (v4 + 1)
                                                if ((v4 + 1) != v15):
                                                    continue
                                                break
                                            v6 = 0
                                            v11 = (v11 + 1)
                                            if ((v11 + 1) != v14):
                                                continue
                                            break
                                        break
                                        break
                                    if not v10:
                                        v6 = 0
                                        break
                                    v6 = load32(v32)
                                    break
                                if (v6 != v8):
                                    break
                                v4 = load32(v5 + 100)
                                if load32(v5 + 100):
                                    v4 = (v27 + (v4 * 132))
                                    # TODO: i32.div_u
                                    if (u32((load32((((load8u((v27 + (v4 * 132)) + 122) * 1020) + 9299904) + (v9 << 2))) * load32(v4 + 52))) < u32(100)):
                                        break
                                while True:  # $label15
                                    v4 = load32(((load8u(v17 + 122) * 404) + ENTITY_TYPES) + 228)
                                    if not load32(((load8u(v17 + 122) * 404) + ENTITY_TYPES) + 228):
                                        break
                                    v9 = load32(v13 + 216)
                                    if not load32(v13 + 216):
                                        break
                                    v13 = (v4 * v4)
                                    v11 = load16u(v17 + 114)
                                    v23 = load16u(v17 + 112)
                                    v4 = 0
                                    v6 = 1
                                    while True:  # $label18
                                        v8 = (v11 - (v4 + v21))
                                        v14 = ((v11 - (v4 + v21)) * v8)
                                        v8 = 0
                                        while True:  # $label17
                                            while True:  # $label16
                                                v15 = (v23 - (v8 + v22))
                                                if (u32(v13) > u32((((v23 - (v8 + v22)) * v15) + v14))):
                                                    v8 = (v8 + 1)
                                                    if (v9 != (v8 + 1)):
                                                        continue
                                                    break
                                                break
                                            if not (v6 & 1):
                                                break
                                            break
                                            break
                                        v4 = (v4 + 1)
                                        v6 = (u32((v4 + 1)) < u32(v9))
                                        if (v4 != v9):
                                            continue
                                        break
                                    break
                                    break
                                arg1 = load32(v5 + 28)
                                v12 = v7
                                break
                            v20 = (v20 + 1)
                            if ((v20 + 1) != v38):
                                continue
                            break
                        break
                    v19 = (v19 + 1)
                    if ((v19 + 1) != 255):
                        continue
                    break
                if not arg1:
                    break
            if not arg2:
                if arg3:
                    store8(arg0 + 125, 0)
                return 1
            store32(arg0 + 32, arg1)
            return 1
            break
        store8(arg0 + 129, 0)
        break
    return 0

# ----------------------------------------------------------
# $func201
# ----------------------------------------------------------
def func201(arg0):
    v1 = load32(arg0 + 24)
    if not load32(arg0 + 24):
        v1 = func26(16)
        store64(func26(16), 0)
        store64(v1 + 8, 0)
        store32(arg0 + 24, v1)
    if not load32(v1 + 8):
        v2 = func26(16)
        store32(func26(16) + 4, 20)
        store32(v2, func26(80))
        store64(v2 + 8, 8589934592)
        store32(v1 + 8, v2)
        v1 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 196)
        v6 = ((load32(players[load16u(arg0 + 110)] + 283936) * 20) % load16u(((load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 196) << 1) + 9142944)))
        v7 = ((v1 << 2) + 9142928)
        while True:  # $label1
            v8 = load16u((load32(v7) + ((v5 + v6) << 1)))
            if load16u((load32(v7) + ((v5 + v6) << 1))):
                while True:  # $label0
                    v1 = load32(load32(arg0 + 24) + 8)
                    v2 = load32(load32(load32(arg0 + 24) + 8) + 8)
                    if (load32(load32(load32(arg0 + 24) + 8) + 8) != load32(v1 + 4)):
                        v3 = load32(v1)
                        break
                    v3 = (load32(v1 + 12) + v2)
                    store32(v1 + 4, (load32(v1 + 12) + v2))
                    v4 = load32(v1)
                    v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                    if v2:
                        # TODO: memory.copy
                    if v4:
                        v2 = load32(v1 + 8)
                    store32(v1, v3)
                    break
                store32(v1 + 8, (v2 + 1))
                store32((v3 + (v2 << 2)), v8)
            v5 = (v5 + 1)
            if ((v5 + 1) != 20):
                continue
            break

# ----------------------------------------------------------
# $func202
# ----------------------------------------------------------
def func202(arg0, arg1, arg2):
    v3 = load32(arg0 + 16)
    if load32(arg0 + 16):
        v4 = load32(v3 + 8)
        v5 = func26((-1 if (u32(v4) > u32(1073741823)) else (load32(v3 + 8) << 2)))
        while True:  # $label0
            if not v4:
                break
            v7 = load32(v3)
            v3 = 0
            if (u32(v4) >= u32(4)):
                v8 = (v4 & -4)
                while True:  # $label1
                    v6 = (v3 << 2)
                    store32((v5 + (v3 << 2)), load32((v6 + v7)))
                    v9 = (v6 | 4)
                    store32((v5 + (v6 | 4)), load32((v7 + v9)))
                    v9 = (v6 | 8)
                    store32((v5 + (v6 | 8)), load32((v7 + v9)))
                    v6 = (v6 | 12)
                    store32((v5 + (v6 | 12)), load32((v6 + v7)))
                    v3 = (v3 + 4)
                    v10 = (v10 + 4)
                    if ((v10 + 4) != v8):
                        continue
                    break
            v6 = (v4 & 3)
            if (v4 & 3):
                while True:  # $label2
                    v8 = (v3 << 2)
                    store32((v5 + (v3 << 2)), load32((v7 + v8)))
                    v3 = (v3 + 1)
                    v11 = (v11 + 1)
                    if ((v11 + 1) != v6):
                        continue
                    break
            if not v4:
                break
            v3 = 0
            while True:  # $label3
                v3 = (v3 + 1)
                if ((v3 + 1) != v4):
                    continue
                break
            break
        while True:  # $label4
            if not arg1:
                break
            if load8u(9147210):
                if (load32(59164) != load32(9142384)):
                    break
            if not v4:
                break
            arg1 = load32(ENTITIES)
            v3 = 0
            while True:  # $label5
                arg2 = (arg1 + (load32((v5 + (v3 << 2))) * 132))
                if not load32((arg1 + (load32((v5 + (v3 << 2))) * 132)) + 36):
                    func44(arg2, 0)
                    arg1 = load32(ENTITIES)
                v3 = (v3 + 1)
                if ((v3 + 1) != v4):
                    continue
                break
            break
    while True:  # $label6
        if not load32(arg0 + 92):
            break
        arg1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break

# ----------------------------------------------------------
# $func203
# ----------------------------------------------------------
def func203(arg0):
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
            break
        if load32(arg0 + 80):
            break
        v3 = load16u(arg0 + 116)
        if not load16u(arg0 + 116):
            break
        v4 = load16u(arg0 + 118)
        if not load16u(arg0 + 118):
            break
        if not load8u(9147152):
            if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u(arg0 + 110))))):
                break
            if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                break
            if (load8u(arg0 + 127) == 6):
                break
        while True:  # $label1
            if load8u(9142917):
                break
            v1 = load32(9299880)
            if load32(9299880):
                v1 = (v1 - 1)
                store32(9299880, (v1 - 1))
                v1 = load32((load32(9299872) + (v1 << 2)))
                break
            v1 = load32(9163776)
            v5 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v6 = load32(9163784)
            if (u32(v5) < u32(load32(9163784))):
                break
            store32(v2, v6)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            v4 = load16u(arg0 + 118)
            v3 = load16u(arg0 + 116)
            break
        store32(arg0 + 80, v1)
        break
    G.global0 = (v2 + 16)

# ----------------------------------------------------------
# $func204
# ----------------------------------------------------------
def func204(arg0, arg1):
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        if (load8u(arg0 + 125) == 3):
            break
        if not load8u(arg0 + 128):
            break
        store8(arg0 + 127, 0)
        while True:  # $label1
            v3 = load32(arg0 + 40)
            if not load32(arg0 + 40):
                break
            if load8u(9142916):
                store32(v2 + 52, v3)
                store32(v2 + 48, 0)
                a_b()
                break
            v4 = load16u(arg0 + 110)
            store32(v2 + 36, v3)
            store32(v2 + 32, (v4 + 16))
            a_b()
            break
        store8(arg0 + 128, 0)
        break
    store8(arg0 + 127, 6)
    while True:  # $label2
        if not load8u(9142916):
            break
        v3 = load32(arg0 + 40)
        if not load32(arg0 + 40):
            break
        store32(v2 + 20, v3)
        store32(v2 + 16, -13487182)
        a_b()
        break
    func119((v2 + 16), arg0, 0, 1)
    func156(1061, arg0, 500)
    while True:  # $label3
        arg1 = load16u(arg0 + 112)
        v3 = ((load16u(arg0 + 112) << 5) - load32(9142952))
        v3 = load16u(arg0 + 114)
        v4 = ((load16u(arg0 + 114) << 5) - load32(9142956))
        if ((((((load16u(arg0 + 112) << 5) - load32(9142952)) * v3) + (((load16u(arg0 + 114) << 5) - load32(9142956)) * v4)) - 1) > 9000000):
            break
        v5 = load32(39880)
        while True:  # $label4
            v6 = load32(load32(GAME_STATE) + 48)
            if not load32(load32(GAME_STATE) + 48):
                break
            if load8u(9147152):
                break
            v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + arg1) << 1)))
            if (v6 == 2):
                if (u32(v4) > u32(1)):
                    break
                break
            if not v4:
                break
            break
        store32(v2 + 8, v3)
        store32(v2 + 4, arg1)
        store32(v2, v5)
        a_b()
        break
    func77(arg0)
    G.global0 = (v2 - -64)

# ----------------------------------------------------------
# $func205
# ----------------------------------------------------------
def func205(arg0, arg1):
    while True:  # $label0
        v3 = load8u(arg0 + 122)
        if (load8u(arg0 + 122) == load32(38500)):
            break
        v2 = load16u(arg0 + 110)
        arg1 = (load32(PLAYER_COUNT) * arg1)
        v4 = load32(9143004)
        while True:  # $label1
            v5 = load16u(arg0 + 120)
            if load16u(arg0 + 120):
            else:
            if not load8u(((v5 if load8u((v4 + (arg1 + v2))) else v2) + (v2 + arg1))):
                v2 = 0
                if (load8u(arg0 + 127) != 6):
                    break
                if not load8u(arg0 + 128):
                    break
                break
            v2 = 0
            if load8u(arg0 + 128):
                break
            break
        if (load8u(arg0 + 125) == 10):
            break
        if (load8u(arg0 + 126) == 2):
            break
        arg0 = load32(arg0 + 64)
        if (load32(arg0 + 64) == -1):
            break
        arg1 = ((v3 * 404) + ENTITY_TYPES)
        v4 = load32(((v3 * 404) + ENTITY_TYPES) + 264)
        if (load32(((v3 * 404) + ENTITY_TYPES) + 264) == 2):
            break
        v2 = ((((((load32(arg1 + 188) == 55) & (load32(38560) != v3)) & (load32(38620) != v3)) & (load32(38564) != v3)) & (v4 == 1)) & (u32(arg0) > u32(1)))
        break
    return v2

# ----------------------------------------------------------
# $func206
# ----------------------------------------------------------
def func206(arg0):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if (load8u(arg0 + 126) == 1):
            break
        v1 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 296)
        v2 = players[load16u(arg0 + 110)]
        v3 = load32((players[load16u(arg0 + 110)] + 284144))
        store8(arg0 + 126, 1)
        # TODO: i32.div_u
        store32(load32(arg0 + 52) + 52, ((v1 * v3) + 100))
        while True:  # $label1
            if not load32(arg0 + 92):
                break
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
        v1 = load16u(arg0 + 114)
        v2 = load16u(arg0 + 112)
        while True:  # $label4
            while True:  # $label3
                while True:  # $label2
                    v6 = load32(load32(GAME_STATE) + 48)
                    if load32(load32(GAME_STATE) + 48):
                        if not load8u(9147152):
                            break
                    v3 = load32(9142440)
                    break
                    break
                v3 = load32(9142440)
                v5 = load16u((load32(9147376) + (((load32(9142440) * v1) + v2) << 1)))
                if (v6 == 2):
                    if (u32(v5) > u32(1)):
                        break
                    break
                if not v5:
                    break
                break
            func80(i32(v2), i32(v1), load32(9142460), 32.0, i32((v3 * 96)))
            v1 = load16u(arg0 + 114)
            v2 = load16u(arg0 + 112)
            break
        arg0 = ((v2 << 5) - load32(9142952))
        arg0 = ((v1 << 5) - load32(9142956))
        if ((((((v2 << 5) - load32(9142952)) * arg0) + (((v1 << 5) - load32(9142956)) * arg0)) - 1) > 9000000):
            break
        v3 = load32(39884)
        while True:  # $label5
            v5 = load32(load32(GAME_STATE) + 48)
            if not load32(load32(GAME_STATE) + 48):
                break
            if load8u(9147152):
                break
            arg0 = load16u((load32(9147376) + (((load32(9142440) * v1) + v2) << 1)))
            if (v5 == 2):
                if (u32(arg0) > u32(1)):
                    break
                break
            if not arg0:
                break
            break
        store32(v4 + 8, v1)
        store32(v4 + 4, v2)
        store32(v4, v3)
        a_b()
        break
    G.global0 = (v4 + 16)

# ----------------------------------------------------------
# $func207
# ----------------------------------------------------------
def func207(arg0, arg1):
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                v3 = load32(arg0 + 20)
                if not load32(arg0 + 20):
                    v2 = func26(16)
                    store32(func26(16) + 4, 2)
                    v3 = func26(8)
                    store32(v2 + 12, 16)
                    store32(v2, v3)
                    store32(arg0 + 20, v2)
                    store32(v2 + 8, 0)
                    v7 = (v2 + 8)
                    break
                store32(v3 + 8, 0)
                v7 = (v3 + 8)
                if not load32(v3 + 4):
                    break
                v2 = v3
                break
            v6 = load32(v2)
            break
            break
        v2 = load32(v3 + 12)
        store32(v3 + 4, load32(v3 + 12))
        v5 = load32(v3)
        v6 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
        v2 = v3
        if v5:
            v4 = load32(v3 + 8)
            v2 = load32(arg0 + 20)
        store32(v3, v6)
        break
    store32(v7, (v4 + 1))
    store32((v6 + (v4 << 2)), 2)
    while True:  # $label3
        arg0 = load32(v2 + 8)
        if (load32(v2 + 8) != load32(v2 + 4)):
            v4 = load32(v2)
            break
        v3 = (load32(v2 + 12) + arg0)
        store32(v2 + 4, (load32(v2 + 12) + arg0))
        v5 = load32(v2)
        v4 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
        if arg0:
            # TODO: memory.copy
        if v5:
            arg0 = load32(v2 + 8)
        store32(v2, v4)
        break
    store32(v2 + 8, (arg0 + 1))
    store32((v4 + (arg0 << 2)), arg1)

# ----------------------------------------------------------
# $func208
# ----------------------------------------------------------
def func208(arg0, arg1, arg2, arg3):
    v8 = (load32(PLAYER_COUNT) * arg2)
    v19 = load32(9142440)
    v10 = (load32(9142440) + 2)
    v22 = ((load32(9142440) + 2) << 1)
    v12 = load32(38564)
    v13 = load32(38620)
    v14 = load32(38560)
    v9 = load32(9143004)
    v15 = load32(38500)
    v16 = load32(ENTITIES)
    v17 = load32(9142840)
    arg2 = 0
    while True:  # $label4
        while True:  # $label10
            while True:  # $label0
                v20 = arg2
                v4 = (arg2 << 2)
                arg2 = (load32((((arg2 << 2) | 4) + 8611904)) + arg1)
                if (u32(v19) <= u32((load32((((arg2 << 2) | 4) + 8611904)) + arg1))):
                    break
                v4 = (load32((v4 + 8611904)) + arg0)
                if (u32(v19) <= u32((load32((v4 + 8611904)) + arg0))):
                    break
                if ((arg2 | v4) < 0):
                    break
                while True:  # $label1
                    v11 = (v4 + 1)
                    v21 = (arg2 + 1)
                    arg2 = load32((v17 + (((v4 + 1) + ((arg2 + 1) * v10)) << 2)))
                    if (u32(load32((v17 + (((v4 + 1) + ((arg2 + 1) * v10)) << 2)))) < u32(3)):
                        break
                    v7 = 0
                    while True:  # $label2
                        v4 = (v16 + (arg2 * 132))
                        v6 = load8u((v16 + (arg2 * 132)) + 122)
                        if (v15 == load8u((v16 + (arg2 * 132)) + 122)):
                            break
                        v5 = load16u(v4 + 110)
                        while True:  # $label3
                            v18 = load16u(v4 + 120)
                            if load16u(v4 + 120):
                            else:
                            if not load8u(((v18 if load8u((v9 + (v5 + v8))) else v5) + (v5 + v8))):
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
                        v5 = ((v6 * 404) + ENTITY_TYPES)
                        if (load32(((v6 * 404) + ENTITY_TYPES) + 264) == 2):
                            break
                        v7 = ((((load32(v5 + 188) == 55) & (v6 != v14)) & (v6 != v13)) & (v6 != v12))
                        break
                    if v7:
                        break
                    if (u32(load32(v4 + 84)) >= u32(arg3)):
                        break
                    if load32(((v6 * 404) + ENTITY_TYPES) + 304):
                        break
                    break
                while True:  # $label5
                    arg2 = load32((v17 + ((v11 + ((v10 + v21) * v10)) << 2)))
                    if (u32(load32((v17 + ((v11 + ((v10 + v21) * v10)) << 2)))) < u32(3)):
                        break
                    v7 = 0
                    while True:  # $label6
                        v4 = (v16 + (arg2 * 132))
                        v6 = load8u((v16 + (arg2 * 132)) + 122)
                        if (v15 == load8u((v16 + (arg2 * 132)) + 122)):
                            break
                        v5 = load16u(v4 + 110)
                        while True:  # $label7
                            v18 = load16u(v4 + 120)
                            if load16u(v4 + 120):
                            else:
                            if load8u(((v18 if load8u((v9 + (v5 + v8))) else v5) + (v5 + v8))):
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
                        v5 = ((v6 * 404) + ENTITY_TYPES)
                        if (load32(((v6 * 404) + ENTITY_TYPES) + 264) == 2):
                            break
                        v7 = ((((load32(v5 + 188) == 55) & (v6 != v14)) & (v6 != v13)) & (v6 != v12))
                        break
                    if v7:
                        break
                    if (u32(load32(v4 + 84)) >= u32(arg3)):
                        break
                    if load32(((v6 * 404) + ENTITY_TYPES) + 304):
                        break
                    break
                arg2 = load32((v17 + ((v11 + ((v21 + v22) * v10)) << 2)))
                if (u32(load32((v17 + ((v11 + ((v21 + v22) * v10)) << 2)))) < u32(3)):
                    break
                v6 = 0
                while True:  # $label8
                    v4 = (v16 + (arg2 * 132))
                    v5 = load8u((v16 + (arg2 * 132)) + 122)
                    if (v15 == load8u((v16 + (arg2 * 132)) + 122)):
                        break
                    v7 = load16u(v4 + 110)
                    while True:  # $label9
                        v11 = load16u(v4 + 120)
                        if load16u(v4 + 120):
                        else:
                        if load8u(((v11 if load8u((v9 + (v7 + v8))) else v7) + (v7 + v8))):
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
                    v7 = ((v5 * 404) + ENTITY_TYPES)
                    if (load32(((v5 * 404) + ENTITY_TYPES) + 264) == 2):
                        break
                    v6 = ((((load32(v7 + 188) == 55) & (v5 != v14)) & (v5 != v13)) & (v5 != v12))
                    break
                if v6:
                    break
                if (u32(load32(v4 + 84)) >= u32(arg3)):
                    break
                if load32(((v5 * 404) + ENTITY_TYPES) + 304):
                    break
                break
            arg2 = (v20 + 2)
            if (u32(v20) < u32(1678)):
                continue
            break
        arg2 = 0
        break
    return arg2

# ----------------------------------------------------------
# $func209
# ----------------------------------------------------------
def func209(arg0):
    while True:  # $label0
        v1 = arg0
        if (arg0 & 3):
            while True:  # $label1
                if not load8u(v1):
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) & 3):
                    continue
                break
        while True:  # $label2
            v2 = v1
            v1 = (v1 + 4)
            v3 = load32(v2)
            if not (((load32(v2) ^ -1) & (v3 - 16843009)) & -2139062144):
                continue
            break
        while True:  # $label3
            v1 = v2
            v2 = (v2 + 1)
            if load8u(v1):
                continue
            break
        break
    return (v1 - arg0)

# ----------------------------------------------------------
# $func210
# ----------------------------------------------------------
def func210(arg0, arg1, arg2):
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label1
        if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
        else:
        v4 = 10
        while True:  # $label0
            if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
                break
            break
        v3 = (load8u(arg0 + 11) & 127)
        if (u32(10) <= u32((load32(arg0 + 4) - (load8u(arg0 + 11) & 127)))):
            if not arg2:
                break
            while True:  # $label2
                if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
                    break
                break
            v4 = arg0
            func122((arg0 + v3), arg1, arg2)
            arg1 = (arg2 + v3)
            func312(arg0, (arg2 + v3))
            store8(v5 + 15, 0)
            store8((arg1 + v4), load8u(v5 + 15))
            break
        break
    G.global0 = (v5 + 16)
    return arg0

# ----------------------------------------------------------
# $func211
# ----------------------------------------------------------
def func211(arg0, arg1):
    return func210(arg0, arg1, func209(arg1))

# ----------------------------------------------------------
# $func212
# ----------------------------------------------------------
def func212():
    func313(4477)
    raise Unreachable()

# ----------------------------------------------------------
# $func213
# ----------------------------------------------------------
def func213(arg0, arg1):
    # TODO: i32.div_u
    arg0 = 1000000
    return func214(func104(arg1, 1000000), (arg1 - (arg0 * 1000000)))

# ----------------------------------------------------------
# $func214
# ----------------------------------------------------------
def func214(arg0, arg1):
    # TODO: i32.div_u
    arg0 = 10000
    return func215(func104(arg1, 10000), (arg1 - (arg0 * 10000)))

# ----------------------------------------------------------
# $func215
# ----------------------------------------------------------
def func215(arg0, arg1):
    # TODO: i32.div_u
    arg0 = 100
    return func104(func104(arg1, 100), (arg1 - (arg0 * 100)))

# ----------------------------------------------------------
# $func216
# ----------------------------------------------------------
def func216(arg0, arg1, arg2, arg3, arg4):
    while True:  # $label0
        v5 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            v6 = load32(arg0)
            break
        v6 = (load32(arg0 + 12) + v5)
        store32(arg0 + 4, (load32(arg0 + 12) + v5))
        v7 = load32(arg0)
        v6 = func26((-1 if (u32(v6) > u32(1073741823)) else (v6 << 2)))
        if v5:
            # TODO: memory.copy
        if v7:
            v5 = load32(arg0 + 8)
        store32(arg0, v6)
        break
    store32(arg0 + 8, (v5 + 1))
    store32((v6 + (v5 << 2)), arg1)
    while True:  # $label1
        v5 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            arg1 = v6
            break
        arg1 = (load32(arg0 + 12) + v5)
        store32(arg0 + 4, (load32(arg0 + 12) + v5))
        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if v5:
            # TODO: memory.copy
        store32(arg0, arg1)
        v5 = load32(arg0 + 8)
        break
    store32(arg0 + 8, (v5 + 1))
    store32((arg1 + (v5 << 2)), arg2)
    while True:  # $label2
        v5 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            v6 = arg1
            break
        arg2 = (load32(arg0 + 12) + v5)
        store32(arg0 + 4, (load32(arg0 + 12) + v5))
        v6 = func26((-1 if (u32(arg2) > u32(1073741823)) else (arg2 << 2)))
        if v5:
            # TODO: memory.copy
        store32(arg0, v6)
        v5 = load32(arg0 + 8)
        break
    store32(arg0 + 8, (v5 + 1))
    store32((v6 + (v5 << 2)), arg3)
    while True:  # $label3
        v5 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            arg1 = v6
            break
        arg1 = (load32(arg0 + 12) + v5)
        store32(arg0 + 4, (load32(arg0 + 12) + v5))
        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if v5:
            # TODO: memory.copy
        store32(arg0, arg1)
        v5 = load32(arg0 + 8)
        break
    store32(arg0 + 8, (v5 + 1))
    store32((arg1 + (v5 << 2)), arg4)

# ----------------------------------------------------------
# $xa
# Export: xa
# ----------------------------------------------------------
def xa():
    """Export: xa"""
    if not load8u(9147126):
        v0 = load32(PLAYER_COUNT)
        v1 = load32(41092)
        v2 = load8u(9147212)
        v5 = (load32(PLAYER_COUNT) if load8u(9147212) else load32(41092))
        v6 = (((load32(PLAYER_COUNT) if load8u(9147212) else load32(41092)) * 45) - 41)
        v3 = func26((-1 if (u32(v6) > u32(1073741823)) else ((((load32(PLAYER_COUNT) if load8u(9147212) else load32(41092)) * 45) - 41) << 2)))
        store32(func26((-1 if (u32(v6) > u32(1073741823)) else ((((load32(PLAYER_COUNT) if load8u(9147212) else load32(41092)) * 45) - 41) << 2))) + 8, v2)
        store32(v3 + 4, v1)
        store32(v3, v0)
        store32(v3 + 12, load8u(9561848))
        if (u32(v5) >= u32(2)):
            v7 = load32(PLAYERS)
            v2 = 4
            v4 = 1
            while True:  # $label0
                v1 = (v3 + (v2 << 2))
                v0 = (v7 + (v4 * 286704))
                store32((v3 + (v2 << 2)), load16u((v7 + (v4 * 286704))))
                store32(v1 + 4, load16u(v0 + 2))
                store32(v1 + 8, load16u(v0 + 4))
                store32(v1 + 12, load16u(v0 + 6))
                store32(v1 + 16, load16u(v0 + 8))
                store32(v1 + 20, load16u(v0 + 10))
                store32(v1 + 24, load16u(v0 + 12))
                store32(v1 + 28, load16u(v0 + 14))
                store32(v1 + 32, load16u(v0 + 16))
                store32(v1 + 36, load16u(v0 + 18))
                store32(v1 + 40, load16u(v0 + 20))
                store32(v1 + 44, load16u(v0 + 22))
                store32(v1 + 48, load16u(v0 + 24))
                store32(v1 + 52, load16u(v0 + 26))
                store32(v1 + 56, load16u(v0 + 28))
                store32(v1 + 60, load16u(v0 + 30))
                store32((v1 - -64), load16u(v0 + 32))
                store32(v1 + 68, load16u(v0 + 34))
                store32(v1 + 72, load16u(v0 + 36))
                store32(v1 + 76, load16u(v0 + 38))
                store32(v1 + 80, load16u(v0 + 40))
                store32(v1 + 84, load16u(v0 + 42))
                store32(v1 + 88, load16u(v0 + 44))
                store32(v1 + 92, load16u(v0 + 46))
                store32(v1 + 96, load16u(v0 + 48))
                store32(v1 + 100, load16u(v0 + 50))
                store32(v1 + 104, load16u(v0 + 52))
                store32(v1 + 108, load16u(v0 + 54))
                store32(v1 + 112, load16u(v0 + 56))
                store32(v1 + 116, load16u(v0 + 58))
                store32(v1 + 120, load16u(v0 + 60))
                store32(v1 + 124, load16u(v0 + 62))
                store32(v1 + 128, load16u((v0 - -64)))
                store32(v1 + 132, load16u(v0 + 66))
                store32(v1 + 136, load16u(v0 + 68))
                store32(v1 + 140, load16u(v0 + 70))
                store32(v1 + 144, load16u(v0 + 72))
                store32(v1 + 148, load16u(v0 + 74))
                store32(v1 + 152, load16u(v0 + 76))
                store32(v1 + 156, load16u(v0 + 78))
                store32(v1 + 160, load32(v0 + 284608))
                store32(v1 + 164, load32(v0 + 283960))
                store32(v1 + 168, load32(v0 + 284616))
                store32(v1 + 172, ((load8u((v0 + 283974)) | (load8u((v0 + 283973)) << 8)) | (load8u(v0 + 283972) << 16)))
                store32(v1 + 176, load32(v0 + 286684))
                v2 = (v2 + 45)
                v4 = (v4 + 1)
                if ((v4 + 1) != v5):
                    continue
                break
        func71(14, v3, v6, 0, 0, 0)

# ----------------------------------------------------------
# $func218
# ----------------------------------------------------------
def func218():
    store32(9561212, 13)
    store64(9561204, 25769803779)
    store64(9561196, 35184372088835)
    store64(9561188, 64424509441)
    store64(9561180, 8589934595)
    store64(9561172, 12884901903)
    store64(9561164, 2)
    store64(9561156, 8589934594)
    store64(9561132, 51539607568)
    store64(9561124, 51539607565)
    store64(9561116, 21474836489)
    store64(9561108, 4294967296)
    store64(9561100, 4)
    store64(9561092, 100)
    store64(9561080, 42949672970)
    store64(9561072, 42949672970)
    store32(9561152, 21)
    store64(9561452, 19327352832002)
    store32(9561148, 17)
    store64(9561444, 85899345960)
    store64(9561336, 429496729616)
    store64(9561324, 257698037810000)
    store64(9561316, 107374183000)
    store64(9561308, 644245334400)
    store64(9561284, 85899345950000)
    store64(9561276, 1073741824020)
    store64(9561268, 171798691847)
    store64(9561260, 214748364850)
    store64(9561252, 257698037764)
    store64(9561244, 25769804776)
    store64(9561236, 128849018880050)
    store64(9561228, 21474836484)
    store32(9561292, 50000)
    store32(9561216, 1)
    store64(9561140, 81604378628)
    store64(9561468, 42949672960004)
    store32(9561440, 100)
    store64(9561432, 34359738468)
    store64(9561424, 214748364814)
    store64(9561416, 214748364804)
    store64(9561408, 429496730200)
    store64(9561400, 34359738388)
    store64(9561392, 773094113290)
    store64(9561384, 257698038360)
    store64(9561376, 214748364850)
    store64(9561368, 214748364870)
    store64(9561360, 85899345920005)
    store64(9561352, 128849018950)
    store64(9561344, 2147483648300)
    store32(9561476, 12)
    store64(9561460, 137438953488)

# ----------------------------------------------------------
# $func219
# ----------------------------------------------------------
def func219():
    while True:  # $label0
        v5 = load32(9142432)
        if not load32(9142432):
            break
        while True:  # $label1
            v3 = load32(9215876)
            if load32(9215876):
                v0 = load32(9215880)
                break
            v3 = func26(16)
            store32(func26(16) + 4, 1024)
            store32(v3, func26(4096))
            store64(v3 + 8, 4398046511104)
            store32(9215876, v3)
            v0 = func26(16)
            store32(func26(16) + 4, 256)
            store32(v0, func26(1024))
            store64(v0 + 8, 4398046511104)
            store32(9215880, v0)
            break
        v7 = 1
        store32(v0 + 8, 1)
        store32(v3 + 8, 0)
        while True:  # $label13
            while True:  # $label2
                v4 = load32(9142440)
                if (load32(9142440) <= 0):
                    v0 = v4
                    break
                v0 = v4
                while True:  # $label12
                    v3 = 0
                    while True:  # $label11
                        v1 = ((v0 * v3) + v8)
                        if not load32((v5 + (((v0 * v3) + v8) << 2))):
                            v5 = 0
                            v0 = load8s((load32(9147288) + v1))
                            if (load8s((load32(9147288) + v1)) >= 0):
                                v5 = (load32(load32((load32(9140332) + ((v0 & 255) << 2))) + 32) == 23)
                            while True:  # $label3
                                v2 = load32(9215880)
                                v0 = load32(load32(9215880) + 8)
                                if (load32(load32(9215880) + 8) != load32(v2 + 4)):
                                    v1 = load32(v2)
                                    break
                                v1 = (load32(v2 + 12) + v0)
                                store32(v2 + 4, (load32(v2 + 12) + v0))
                                v6 = load32(v2)
                                v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                                if v0:
                                    # TODO: memory.copy
                                if v6:
                                    v0 = load32(v2 + 8)
                                store32(v2, v1)
                                break
                            store32(v2 + 8, (v0 + 1))
                            store32((v1 + (v0 << 2)), v5)
                            v11 = 0
                            v16 = load32(9142440)
                            v0 = ((load32(9142440) * v3) + v8)
                            store32(59200, ((load32(9142440) * v3) + v8))
                            store32((load32(9142432) + (v0 << 2)), v7)
                            v9 = 1
                            while True:  # $label10
                                v0 = load32((((v11 & 2097151) << 2) + 59200))
                                v0 = load32(9142440)
                                # TODO: i32.div_u
                                v17 = load32(9142440)
                                v18 = (v0 - (load32(9142440) * v0))
                                v12 = 0
                                while True:  # $label9
                                    while True:  # $label4
                                        v2 = load32(9142440)
                                        v1 = (v12 << 3)
                                        v0 = (load32(((v12 << 3) + 8932)) + v17)
                                        if (u32(load32(9142440)) <= u32((load32(((v12 << 3) + 8932)) + v17))):
                                            break
                                        v1 = (load32((v1 + 8928)) + v18)
                                        if (u32(v2) <= u32((load32((v1 + 8928)) + v18))):
                                            break
                                        if ((v0 | v1) < 0):
                                            break
                                        v10 = load32(9142432)
                                        v0 = ((v0 * v16) + v1)
                                        v19 = (((v0 * v16) + v1) << 2)
                                        v6 = (load32(9142432) + (((v0 * v16) + v1) << 2))
                                        v2 = load32((load32(9142432) + (((v0 * v16) + v1) << 2)))
                                        if load32((load32(9142432) + (((v0 * v16) + v1) << 2))):
                                            if (v2 == v7):
                                                break
                                            v1 = load32(9215876)
                                            v6 = load32(load32(9215876) + 8)
                                            if load32(load32(9215876) + 8):
                                                v14 = load32(v1)
                                                v0 = 0
                                                while True:  # $label5
                                                    v13 = (v0 << 2)
                                                    v15 = load32((v14 + ((v0 << 2) | 4)))
                                                    v13 = load32((v13 + v14))
                                                    if ((v7 == load32((v13 + v14))) & (v2 == v15)):
                                                        break
                                                    if ((v2 == v13) & (v7 == v15)):
                                                        break
                                                    v0 = (v0 + 2)
                                                    if (u32((v0 + 2)) < u32(v6)):
                                                        continue
                                                    break
                                            while True:  # $label6
                                                if (load32(v1 + 4) != v6):
                                                    v0 = load32(v1)
                                                    break
                                                v0 = (load32(v1 + 12) + v6)
                                                store32(v1 + 4, (load32(v1 + 12) + v6))
                                                v2 = load32(v1)
                                                v0 = func26((-1 if (u32(v0) > u32(1073741823)) else (v0 << 2)))
                                                if v6:
                                                    # TODO: memory.copy
                                                if v2:
                                                    v6 = load32(v1 + 8)
                                                store32(v1, v0)
                                                v10 = load32(9142432)
                                                break
                                            v2 = load32(9215876)
                                            store32(v1 + 8, (v6 + 1))
                                            store32((v0 + (v6 << 2)), v7)
                                            v10 = load32((v10 + v19))
                                            while True:  # $label7
                                                v0 = load32(v2 + 8)
                                                if (load32(v2 + 8) != load32(v2 + 4)):
                                                    v1 = load32(v2)
                                                    break
                                                v1 = (load32(v2 + 12) + v0)
                                                store32(v2 + 4, (load32(v2 + 12) + v0))
                                                v6 = load32(v2)
                                                v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                                                if v0:
                                                    # TODO: memory.copy
                                                if v6:
                                                    v0 = load32(v2 + 8)
                                                store32(v2, v1)
                                                break
                                            store32(v2 + 8, (v0 + 1))
                                            store32((v1 + (v0 << 2)), v10)
                                            break
                                        v1 = load8u((load32(9147288) + v0))
                                        v2 = i32(load8u((load32(9147288) + v0)))
                                        while True:  # $label8
                                            if v5:
                                                if (v2 < 0):
                                                    break
                                                if (load32(load32((load32(9140332) + (v1 << 2))) + 32) == 23):
                                                    break
                                                break
                                            if (v2 < 0):
                                                break
                                            if (load32(load32((load32(9140332) + (v1 << 2))) + 32) == 23):
                                                break
                                            break
                                        store32((((v9 & 2097151) << 2) + 59200), v0)
                                        store32(v6, v7)
                                        v9 = (v9 + 1)
                                        break
                                    v12 = (v12 + 1)
                                    if ((v12 + 1) != 8):
                                        continue
                                    break
                                v11 = (v11 + 1)
                                if (u32((v11 + 1)) < u32(v9)):
                                    continue
                                break
                            v7 = (v7 + 1)
                            v0 = load32(9142440)
                            v5 = load32(9142432)
                        v3 = (v3 + 1)
                        if ((v3 + 1) != v4):
                            continue
                        break
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v4):
                        continue
                    break
                if v7:
                    break
                v7 = 0
                break
                break
            store32(((v7 << 2) + 59200), 0)
            break
        v2 = 0
        while True:  # $label14
            v0 = (v0 * v0)
            if not (v0 * v0):
                break
            v8 = 0
            v3 = 0
            if (u32(v0) >= u32(4)):
                v6 = (v0 & -4)
                v1 = 0
                while True:  # $label15
                    v4 = (v3 << 2)
                    v9 = ((load32((v5 + (v3 << 2))) << 2) + 59200)
                    store32(((load32((v5 + (v3 << 2))) << 2) + 59200), (load32(v9) + 1))
                    v9 = ((load32((v5 + (v4 | 4))) << 2) + 59200)
                    store32(((load32((v5 + (v4 | 4))) << 2) + 59200), (load32(v9) + 1))
                    v9 = ((load32((v5 + (v4 | 8))) << 2) + 59200)
                    store32(((load32((v5 + (v4 | 8))) << 2) + 59200), (load32(v9) + 1))
                    v4 = ((load32((v5 + (v4 | 12))) << 2) + 59200)
                    store32(((load32((v5 + (v4 | 12))) << 2) + 59200), (load32(v4) + 1))
                    v3 = (v3 + 4)
                    v1 = (v1 + 4)
                    if ((v1 + 4) != v6):
                        continue
                    break
            v0 = (v0 & 3)
            if not (v0 & 3):
                break
            while True:  # $label16
                v4 = ((load32((v5 + (v3 << 2))) << 2) + 59200)
                store32(((load32((v5 + (v3 << 2))) << 2) + 59200), (load32(v4) + 1))
                v3 = (v3 + 1)
                v8 = (v8 + 1)
                if ((v8 + 1) != v0):
                    continue
                break
            break
        while True:  # $label17
            if v2:
                break
            v3 = 0
            v5 = load32(9684492)
            v8 = load32(load32(9215880))
            if (v7 != 1):
                v1 = (v7 & -2)
                v0 = 0
                while True:  # $label20
                    while True:  # $label18
                        v4 = (v3 << 2)
                        if load32((v8 + (v3 << 2))):
                            break
                        if (u32(load32((v4 + 59200))) <= u32(load32(((v5 << 2) + 59200)))):
                            break
                        store32(9684492, v3)
                        v5 = v3
                        break
                    while True:  # $label19
                        v4 = (v3 | 1)
                        v2 = ((v3 | 1) << 2)
                        if load32((v8 + ((v3 | 1) << 2))):
                            break
                        if (u32(load32((v2 + 59200))) <= u32(load32(((v5 << 2) + 59200)))):
                            break
                        store32(9684492, v4)
                        v5 = v4
                        break
                    v3 = (v3 + 2)
                    v0 = (v0 + 2)
                    if ((v0 + 2) != v1):
                        continue
                    break
            if not (v7 & 1):
                break
            v0 = (v3 << 2)
            if load32((v8 + (v3 << 2))):
                break
            if (u32(load32((v0 + 59200))) <= u32(load32(((v5 << 2) + 59200)))):
                break
            store32(9684492, v3)
            break
        v8 = 0
        v0 = (v7 * v7)
        v5 = func26((v7 * v7))
        # TODO: memory.fill
        store32(9684440, v7)
        store32(9684436, v5)
        v0 = load32(9215876)
        v4 = load32(load32(9215876) + 8)
        if not load32(load32(9215876) + 8):
            break
        v3 = ((((v4 - 1) & 0xFFFFFFFF) >> 1) + 1)
        v2 = (((((v4 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
        v0 = load32(v0)
        if (u32(v4) >= u32(3)):
            v3 = (v3 & -2)
            v1 = 0
            while True:  # $label21
                v4 = (v8 << 2)
                v6 = load32((v0 + ((v8 << 2) | 4)))
                v9 = load32((v0 + v4))
                store8((v5 + ((load32((v0 + ((v8 << 2) | 4))) * v7) + load32((v0 + v4)))), 1)
                store8((v5 + (v6 + (v7 * v9))), 1)
                v6 = load32((v0 + (v4 | 8)))
                v4 = load32((v0 + (v4 | 12)))
                store8((v5 + (load32((v0 + (v4 | 8))) + (load32((v0 + (v4 | 12))) * v7))), 1)
                store8((v5 + (v4 + (v6 * v7))), 1)
                v8 = (v8 + 4)
                v1 = (v1 + 2)
                if ((v1 + 2) != v3):
                    continue
                break
        if not v2:
            break
        v4 = (v8 << 2)
        v3 = load32((v0 + ((v8 << 2) | 4)))
        v0 = load32((v0 + v4))
        store8((v5 + ((load32((v0 + ((v8 << 2) | 4))) * v7) + load32((v0 + v4)))), 1)
        store8((v5 + (v3 + (v0 * v7))), 1)
        break
    return v0

# ----------------------------------------------------------
# $func220
# ----------------------------------------------------------
def func220():
    v3 = (G.global0 - 560)
    G.global0 = (G.global0 - 560)
    v70 = load32(38676)
    v71 = load32(38924)
    v72 = load32(38428)
    v73 = load32(38760)
    v74 = load32(38744)
    v75 = load32(38424)
    v76 = load32(38680)
    v77 = load32(38736)
    v78 = load32(57152)
    v79 = load32(38732)
    v80 = load32(38672)
    v81 = load32(38460)
    v63 = load32(38928)
    v64 = load32(38772)
    v65 = load32(38440)
    v66 = load32(38728)
    v42 = load32(38940)
    v67 = load32(38932)
    v43 = load32(38580)
    v44 = load32(38660)
    v45 = load32(38656)
    v46 = load32(38652)
    v47 = load32(38724)
    v9 = load32(38432)
    v12 = load32(38748)
    v82 = load32(38712)
    v14 = load32(38720)
    v4 = load32(38716)
    v10 = load32(38708)
    v18 = load32(38576)
    v11 = load32(38572)
    v20 = load32(38568)
    v21 = load32(38436)
    v22 = load32(38684)
    v23 = load32(38740)
    v24 = load32(38444)
    v25 = load32(38756)
    v26 = load32(38692)
    v27 = load32(38704)
    v33 = load32(38452)
    v28 = load32(38776)
    v34 = load32(38752)
    v68 = load32(38696)
    v69 = load32(38496)
    v15 = load32(38596)
    v16 = load32(38640)
    v6 = load32(38644)
    v8 = load32(38648)
    v13 = load32(38548)
    v5 = load32(38608)
    store32(v3 + 272, load32(38608))
    v7 = load32(38612)
    store32(v3 + 276, load32(38612))
    v17 = load32(38616)
    store32(v3 + 280, load32(38616))
    v32 = load32(38604)
    store32(v3 + 284, load32(38604))
    v35 = load32(38624)
    store32(v3 + 288, load32(38624))
    v36 = load32(38628)
    store32(v3 + 292, load32(38628))
    v37 = load32(38632)
    store32(v3 + 296, load32(38632))
    v38 = load32(39056)
    store32(v3 + 300, load32(39056))
    v39 = load32(38464)
    store32(v3 + 304, load32(38464))
    v29 = load32(38468)
    store32(v3 + 308, load32(38468))
    v30 = load32(38472)
    store32(v3 + 312, load32(38472))
    store32(v3 + 316, load32(38600))
    v40 = load32(38476)
    store32(v3 + 320, load32(38476))
    v41 = load32(38480)
    store32(v3 + 324, load32(38480))
    v31 = load32(38484)
    store32(v3 + 328, load32(38484))
    v19 = load32(38488)
    store32(v3 + 332, load32(38488))
    v48 = load32(38492)
    store32(v3 + 336, load32(38492))
    v49 = load32(38512)
    store32(v3 + 340, load32(38512))
    v50 = load32(38516)
    store32(v3 + 344, load32(38516))
    v51 = load32(38520)
    store32(v3 + 348, load32(38520))
    v52 = load32(38524)
    store32(v3 + 352, load32(38524))
    v53 = load32(38532)
    store32(v3 + 356, load32(38532))
    v54 = load32(38536)
    store32(v3 + 360, load32(38536))
    v55 = load32(38540)
    store32(v3 + 364, load32(38540))
    v2 = load32(38544)
    store32(v3 + 372, v13)
    store32(v3 + 368, v2)
    v56 = load32(38552)
    store32(v3 + 376, load32(38552))
    v57 = load32(38556)
    store32(v3 + 380, load32(38556))
    v58 = load32(38560)
    store32(v3 + 384, load32(38560))
    v0 = load32(38584)
    store32(v3 + 404, v8)
    store32(v3 + 400, v6)
    store32(v3 + 396, v16)
    store32(v3 + 392, v15)
    store32(v3 + 388, v0)
    v59 = load32(38664)
    store32(v3 + 408, load32(38664))
    v60 = load32(38668)
    store32(v3 + 412, load32(38668))
    v61 = load32(38700)
    store32(v3 + 416, load32(38700))
    v62 = load32(38780)
    store32(v3 + 420, load32(38780))
    v83 = load32(38784)
    store32(v3 + 424, load32(38784))
    v84 = load32(38788)
    store32(v3 + 428, load32(38788))
    v85 = load32(38792)
    store32(v3 + 432, load32(38792))
    v86 = load32(38796)
    store32(v3 + 436, load32(38796))
    v87 = load32(38800)
    store32(v3 + 440, load32(38800))
    v88 = load32(38804)
    store32(v3 + 444, load32(38804))
    v89 = load32(38808)
    store32(v3 + 448, load32(38808))
    v90 = load32(38812)
    store32(v3 + 452, load32(38812))
    v91 = load32(38816)
    store32(v3 + 456, load32(38816))
    v92 = load32(38820)
    store32(v3 + 460, load32(38820))
    v93 = load32(38824)
    store32(v3 + 464, load32(38824))
    v94 = load32(38828)
    store32(v3 + 468, load32(38828))
    v95 = load32(38836)
    store32(v3 + 472, load32(38836))
    v96 = load32(38840)
    store32(v3 + 476, load32(38840))
    v97 = load32(38844)
    store32(v3 + 480, load32(38844))
    v98 = load32(38848)
    store32(v3 + 484, load32(38848))
    v99 = load32(38852)
    store32(v3 + 488, load32(38852))
    v100 = load32(38856)
    store32(v3 + 492, load32(38856))
    v101 = load32(38860)
    store32(v3 + 496, load32(38860))
    v102 = load32(38864)
    store32(v3 + 500, load32(38864))
    v103 = load32(38868)
    store32(v3 + 504, load32(38868))
    v104 = load32(38872)
    store32(v3 + 508, load32(38872))
    v105 = load32(38876)
    store32(v3 + 512, load32(38876))
    v106 = load32(38880)
    store32(v3 + 516, load32(38880))
    v107 = load32(38884)
    store32(v3 + 520, load32(38884))
    v108 = load32(38888)
    store32(v3 + 524, load32(38888))
    v109 = load32(38892)
    store32(v3 + 528, load32(38892))
    v110 = load32(38896)
    store32(v3 + 532, load32(38896))
    v111 = load32(38900)
    store32(v3 + 536, load32(38900))
    v112 = load32(38904)
    store32(v3 + 540, load32(38904))
    v113 = load32(38908)
    store32(v3 + 544, load32(38908))
    v114 = load32(38912)
    store32(v3 + 548, load32(38912))
    v115 = load32(38916)
    store32(v3 + 552, load32(38916))
    store32(v3 + 92, v2)
    store32(v3 + 88, v55)
    store32(v3 + 84, v54)
    store32(v3 + 80, v53)
    store32(v3 + 76, v52)
    store32(v3 + 72, v51)
    store32(v3 + 68, v50)
    store32(v3 + 64, v49)
    store32(v3 + 60, v48)
    store32(v3 + 56, v19)
    store32(v3 + 52, v31)
    store32(v3 + 48, v41)
    store32(v3 + 44, v40)
    store32(v3 + 40, v30)
    store32(v3 + 36, v29)
    store32(v3 + 32, v39)
    store32(v3 + 28, v38)
    store32(v3 + 24, v37)
    store32(v3 + 20, v36)
    store32(v3 + 16, v35)
    store32(v3 + 12, v32)
    store32(v3 + 8, v17)
    store32(v3 + 4, v7)
    store32(v3, v5)
    v2 = load32(38548)
    store32(v3 + 260, v115)
    store32(v3 + 256, v114)
    store32(v3 + 252, v113)
    store32(v3 + 248, v112)
    store32(v3 + 244, v111)
    store32(v3 + 240, v110)
    store32(v3 + 236, v109)
    store32(v3 + 232, v108)
    store32(v3 + 228, v107)
    store32(v3 + 224, v106)
    store32(v3 + 220, v105)
    store32(v3 + 216, v104)
    store32(v3 + 212, v103)
    store32(v3 + 208, v102)
    store32(v3 + 204, v101)
    store32(v3 + 200, v100)
    store32(v3 + 196, v99)
    store32(v3 + 192, v98)
    store32(v3 + 188, v97)
    store32(v3 + 184, v96)
    store32(v3 + 180, v95)
    store32(v3 + 176, v94)
    store32(v3 + 172, v93)
    store32(v3 + 168, v92)
    store32(v3 + 164, v91)
    store32(v3 + 160, v90)
    store32(v3 + 156, v89)
    store32(v3 + 152, v88)
    store32(v3 + 148, v87)
    store32(v3 + 144, v86)
    store32(v3 + 140, v85)
    store32(v3 + 136, v84)
    store32(v3 + 132, v83)
    store32(v3 + 128, v62)
    store32(v3 + 124, v61)
    store32(v3 + 120, v60)
    store32(v3 + 116, v59)
    store32(v3 + 112, v0)
    store32(v3 + 108, v58)
    store32(v3 + 104, v57)
    store32(v3 + 100, v56)
    store32(v3 + 96, v2)
    v48 = load32(38656)
    v49 = load32(38724)
    v50 = load32(38704)
    v51 = load32(38728)
    v52 = load32(38932)
    v53 = load32(38760)
    v54 = load32(38748)
    v55 = load32(38688)
    v35 = load32(38764)
    v36 = load32(38456)
    v56 = load32(38680)
    v57 = load32(38736)
    v58 = load32(57152)
    v37 = load32(38928)
    v38 = load32(38772)
    v39 = load32(38440)
    v59 = load32(38732)
    v60 = load32(38672)
    v61 = load32(38460)
    v29 = load32(38600)
    v30 = load32(38472)
    v32 = load32(38920)
    v62 = load32(38924)
    v40 = load32(38744)
    v41 = load32(38424)
    v31 = load32(38576)
    v19 = load32(38568)
    while True:  # $label1
        v2 = 0
        while True:  # $label0
            v0 = (((v1 * 1020) + 9299904) + (v2 << 2))
            store64((((v1 * 1020) + 9299904) + (v2 << 2)), 429496729700)
            store32(v0 + 16, 100)
            store64(v0 + 8, 429496729700)
            v2 = (v2 + 5)
            if ((v2 + 5) != 255):
                continue
            break
        v1 = (v1 + 1)
        if ((v1 + 1) != 255):
            continue
        break
    v5 = ((v6 * 1020) + 9299904)
    v2 = (v10 << 2)
    v1 = (((v6 * 1020) + 9299904) + (v10 << 2))
    store32((((v6 * 1020) + 9299904) + (v10 << 2)), (load32(v1) + 400))
    v7 = ((v8 * 1020) + 9299904)
    v1 = (((v8 * 1020) + 9299904) + v2)
    store32((((v8 * 1020) + 9299904) + v2), (load32(v1) + 400))
    v1 = (v4 << 2)
    v0 = (v5 + (v4 << 2))
    store32((v5 + (v4 << 2)), (load32(v0) + 400))
    v0 = (v1 + v7)
    store32((v1 + v7), (load32(v0) + 400))
    v0 = (v14 << 2)
    v5 = (v5 + (v14 << 2))
    store32((v5 + (v14 << 2)), (load32(v5) + 400))
    v5 = (v0 + v7)
    store32((v0 + v7), (load32(v5) + 400))
    v5 = ((v10 * 1020) + 9299904)
    v7 = (((v10 * 1020) + 9299904) + v2)
    store32((((v10 * 1020) + 9299904) + v2), (load32(v7) + 300))
    v7 = ((v4 * 1020) + 9299904)
    v17 = (((v4 * 1020) + 9299904) + v2)
    store32((((v4 * 1020) + 9299904) + v2), (load32(v17) + 300))
    v17 = ((v14 * 1020) + 9299904)
    v2 = (((v14 * 1020) + 9299904) + v2)
    store32((((v14 * 1020) + 9299904) + v2), (load32(v2) + 300))
    v2 = (v1 + v5)
    store32((v1 + v5), (load32(v2) + 300))
    v2 = (v1 + v7)
    store32((v1 + v7), (load32(v2) + 300))
    v2 = (v1 + v17)
    store32((v1 + v17), (load32(v2) + 300))
    v2 = (v0 + v5)
    store32((v0 + v5), (load32(v2) + 300))
    v2 = (v0 + v7)
    store32((v0 + v7), (load32(v2) + 300))
    v2 = (v0 + v17)
    store32((v0 + v17), (load32(v2) + 300))
    v2 = 0
    while True:  # $label2
        v1 = (load32((v3 + (v2 << 2))) << 2)
        v0 = (v5 + (load32((v3 + (v2 << 2))) << 2))
        store32((v5 + (load32((v3 + (v2 << 2))) << 2)), (load32(v0) + 300))
        v0 = (v1 + v7)
        store32((v1 + v7), (load32(v0) + 300))
        v1 = (v1 + v17)
        store32((v1 + v17), (load32(v1) + 300))
        v2 = (v2 + 1)
        if ((v2 + 1) != 66):
            continue
        break
    v2 = ((v10 * 1020) + 9299904)
    v0 = (v13 << 2)
    v1 = (((v10 * 1020) + 9299904) + (v13 << 2))
    store32((((v10 * 1020) + 9299904) + (v13 << 2)), (load32(v1) + 300))
    v1 = ((v4 * 1020) + 9299904)
    v5 = (((v4 * 1020) + 9299904) + v0)
    store32((((v4 * 1020) + 9299904) + v0), (load32(v5) + 300))
    v0 = ((v14 * 1020) + 9299904)
    v5 = (v0 + ((v14 * 1020) + 9299904))
    store32((v0 + ((v14 * 1020) + 9299904)), (load32(v5) + 300))
    v5 = (v16 << 2)
    v7 = (v2 + (v16 << 2))
    store32((v2 + (v16 << 2)), (load32(v7) + 300))
    v7 = (v1 + v5)
    store32((v1 + v5), (load32(v7) + 300))
    v5 = (v0 + v5)
    store32((v0 + v5), (load32(v5) + 300))
    v5 = (v15 << 2)
    v7 = (v2 + (v15 << 2))
    store32((v2 + (v15 << 2)), (load32(v7) + 300))
    v7 = (v1 + v5)
    store32((v1 + v5), (load32(v7) + 300))
    v5 = (v0 + v5)
    store32((v0 + v5), (load32(v5) + 300))
    v5 = (v6 << 2)
    v7 = (v2 + (v6 << 2))
    store32((v2 + (v6 << 2)), (load32(v7) + 300))
    v7 = (v1 + v5)
    store32((v1 + v5), (load32(v7) + 300))
    v5 = (v0 + v5)
    store32((v0 + v5), (load32(v5) + 300))
    v5 = (v8 << 2)
    v7 = (v2 + (v8 << 2))
    store32((v2 + (v8 << 2)), (load32(v7) + 300))
    v7 = (v1 + v5)
    store32((v1 + v5), (load32(v7) + 300))
    v5 = (v0 + v5)
    store32((v0 + v5), (load32(v5) + 300))
    v5 = (v30 << 2)
    v7 = (v2 + (v30 << 2))
    store32((v2 + (v30 << 2)), (load32(v7) + 500))
    v7 = (v1 + v5)
    store32((v1 + v5), (load32(v7) + 500))
    v5 = (v0 + v5)
    store32((v0 + v5), (load32(v5) + 500))
    v5 = (v29 << 2)
    v7 = (v2 + (v29 << 2))
    store32((v2 + (v29 << 2)), (load32(v7) + 500))
    v7 = (v1 + v5)
    store32((v1 + v5), (load32(v7) + 500))
    v5 = (v0 + v5)
    store32((v0 + v5), (load32(v5) + 500))
    v5 = (v20 << 2)
    v7 = (v2 + (v20 << 2))
    store32((v2 + (v20 << 2)), (load32(v7) + 200))
    v7 = (v1 + v5)
    store32((v1 + v5), (load32(v7) + 200))
    v5 = (v0 + v5)
    store32((v0 + v5), (load32(v5) + 200))
    v5 = (v11 << 2)
    v7 = (v2 + (v11 << 2))
    store32((v2 + (v11 << 2)), (load32(v7) + 200))
    v7 = (v1 + v5)
    store32((v1 + v5), (load32(v7) + 200))
    v5 = (v0 + v5)
    store32((v0 + v5), (load32(v5) + 200))
    v5 = (v18 << 2)
    v2 = (v2 + (v18 << 2))
    store32((v2 + (v18 << 2)), (load32(v2) + 200))
    v2 = (v1 + v5)
    store32((v1 + v5), (load32(v2) + 200))
    v2 = (v0 + v5)
    store32((v0 + v5), (load32(v2) + 200))
    v2 = 0
    while True:  # $label3
        v1 = ((v19 * 1020) + 9299904)
        v0 = (v2 << 2)
        v5 = (load32((v3 + (v2 << 2))) << 2)
        v7 = (((v19 * 1020) + 9299904) + (load32((v3 + (v2 << 2))) << 2))
        store32((((v19 * 1020) + 9299904) + (load32((v3 + (v2 << 2))) << 2)), (load32(v7) + 400))
        v5 = ((v31 * 1020) + 9299904)
        v7 = (v5 + ((v31 * 1020) + 9299904))
        store32((v5 + ((v31 * 1020) + 9299904)), (load32(v7) + 400))
        v0 = (load32((v3 + (v0 | 4))) << 2)
        v1 = (v1 + (load32((v3 + (v0 | 4))) << 2))
        store32((v1 + (load32((v3 + (v0 | 4))) << 2)), (load32(v1) + 400))
        v1 = (v0 + v5)
        store32((v0 + v5), (load32(v1) + 400))
        v2 = (v2 + 2)
        if ((v2 + 2) != 66):
            continue
        break
    v2 = ((v19 * 1020) + 9299904)
    v1 = (v10 << 2)
    v0 = (((v19 * 1020) + 9299904) + (v10 << 2))
    store32((((v19 * 1020) + 9299904) + (v10 << 2)), (load32(v0) + 400))
    v1 = ((v31 * 1020) + 9299904)
    v0 = (v1 + ((v31 * 1020) + 9299904))
    store32((v1 + ((v31 * 1020) + 9299904)), (load32(v0) + 400))
    v0 = (v4 << 2)
    v4 = (v2 + (v4 << 2))
    store32((v2 + (v4 << 2)), (load32(v4) + 400))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 400))
    v0 = (v14 << 2)
    v4 = (v2 + (v14 << 2))
    store32((v2 + (v14 << 2)), (load32(v4) + 400))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 400))
    v0 = (v82 << 2)
    v4 = (v2 + (v82 << 2))
    store32((v2 + (v82 << 2)), (load32(v4) + 400))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 400))
    v0 = (v13 << 2)
    v4 = (v2 + (v13 << 2))
    store32((v2 + (v13 << 2)), (load32(v4) + 600))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 600))
    v0 = (v16 << 2)
    v4 = (v2 + (v16 << 2))
    store32((v2 + (v16 << 2)), (load32(v4) + 600))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 600))
    v0 = (v15 << 2)
    v4 = (v2 + (v15 << 2))
    store32((v2 + (v15 << 2)), (load32(v4) + 600))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 600))
    v0 = (v6 << 2)
    v4 = (v2 + (v6 << 2))
    store32((v2 + (v6 << 2)), (load32(v4) + 600))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 600))
    v0 = (v8 << 2)
    v4 = (v2 + (v8 << 2))
    store32((v2 + (v8 << 2)), (load32(v4) + 600))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 600))
    v10 = (v20 << 2)
    v0 = (v2 + (v20 << 2))
    store32((v2 + (v20 << 2)), (load32(v0) + 400))
    v0 = (v1 + v10)
    store32((v1 + v10), (load32(v0) + 400))
    v6 = (v11 << 2)
    v0 = (v2 + (v11 << 2))
    store32((v2 + (v11 << 2)), (load32(v0) + 400))
    v0 = (v1 + v6)
    store32((v1 + v6), (load32(v0) + 400))
    v8 = (v18 << 2)
    v0 = (v2 + (v18 << 2))
    store32((v2 + (v18 << 2)), (load32(v0) + 400))
    v0 = (v1 + v8)
    store32((v1 + v8), (load32(v0) + 400))
    v0 = (v30 << 2)
    v4 = (v2 + (v30 << 2))
    store32((v2 + (v30 << 2)), (load32(v4) + 900))
    v0 = (v0 + v1)
    store32((v0 + v1), (load32(v0) + 900))
    v0 = (v29 << 2)
    v2 = (v2 + (v29 << 2))
    store32((v2 + (v29 << 2)), (load32(v2) + 900))
    v2 = (v0 + v1)
    store32((v0 + v1), (load32(v2) + 900))
    v2 = ((v55 * 1020) + 9299904)
    v4 = (v68 << 2)
    v1 = (((v55 * 1020) + 9299904) + (v68 << 2))
    store32((((v55 * 1020) + 9299904) + (v68 << 2)), (load32(v1) + 50))
    v5 = (v33 << 2)
    v1 = (v2 + (v33 << 2))
    store32((v2 + (v33 << 2)), (load32(v1) + 50))
    v7 = (v28 << 2)
    v1 = (v2 + (v28 << 2))
    store32((v2 + (v28 << 2)), (load32(v1) + 50))
    v0 = (v69 << 2)
    v1 = (v2 + (v69 << 2))
    store32((v2 + (v69 << 2)), (load32(v1) + 30))
    v17 = (v34 << 2)
    v1 = (v2 + (v34 << 2))
    store32((v2 + (v34 << 2)), (load32(v1) + 30))
    v18 = (v27 << 2)
    v1 = (v2 + (v27 << 2))
    store32((v2 + (v27 << 2)), (load32(v1) + 30))
    v11 = (v26 << 2)
    v1 = (v2 + (v26 << 2))
    store32((v2 + (v26 << 2)), (load32(v1) + 30))
    v20 = (v25 << 2)
    v2 = (v2 + (v25 << 2))
    store32((v2 + (v25 << 2)), (load32(v2) + 30))
    v2 = ((v56 * 1020) + 9299904)
    v29 = (v61 << 2)
    v1 = (((v56 * 1020) + 9299904) + (v61 << 2))
    store32((((v56 * 1020) + 9299904) + (v61 << 2)), (load32(v1) + 100))
    v30 = (v60 << 2)
    v1 = (v2 + (v60 << 2))
    store32((v2 + (v60 << 2)), (load32(v1) + 100))
    v31 = (v59 << 2)
    v1 = (v2 + (v59 << 2))
    store32((v2 + (v59 << 2)), (load32(v1) + 100))
    v1 = ((v41 * 1020) + 9299904)
    v19 = (((v41 * 1020) + 9299904) + v0)
    store32((((v41 * 1020) + 9299904) + v0), (load32(v19) + 600))
    v0 = ((v40 * 1020) + 9299904)
    v19 = (v0 + ((v40 * 1020) + 9299904))
    store32((v0 + ((v40 * 1020) + 9299904)), (load32(v19) + 600))
    v19 = (v1 + v4)
    store32((v1 + v4), (load32(v19) + 600))
    v4 = (v0 + v4)
    store32((v0 + v4), (load32(v4) + 600))
    v4 = (v1 + v17)
    store32((v1 + v17), (load32(v4) + 600))
    v4 = (v0 + v17)
    store32((v0 + v17), (load32(v4) + 600))
    v4 = (v1 + v7)
    store32((v1 + v7), (load32(v4) + 600))
    v4 = (v0 + v7)
    store32((v0 + v7), (load32(v4) + 600))
    v4 = (v1 + v5)
    store32((v1 + v5), (load32(v4) + 600))
    v4 = (v0 + v5)
    store32((v0 + v5), (load32(v4) + 600))
    v4 = (v1 + v18)
    store32((v1 + v18), (load32(v4) + 600))
    v4 = (v0 + v18)
    store32((v0 + v18), (load32(v4) + 600))
    v4 = (v1 + v11)
    store32((v1 + v11), (load32(v4) + 600))
    v4 = (v0 + v11)
    store32((v0 + v11), (load32(v4) + 600))
    v1 = (v1 + v20)
    store32((v1 + v20), (load32(v1) + 600))
    v1 = (v0 + v20)
    store32((v0 + v20), (load32(v1) + 600))
    v1 = ((v58 * 1020) + 9299904)
    v0 = (v41 << 2)
    v4 = (((v58 * 1020) + 9299904) + (v41 << 2))
    store32((((v58 * 1020) + 9299904) + (v41 << 2)), (load32(v4) + 150))
    v4 = ((v57 * 1020) + 9299904)
    v5 = (((v57 * 1020) + 9299904) + v0)
    store32((((v57 * 1020) + 9299904) + v0), (load32(v5) + 150))
    v5 = (v0 + v2)
    store32((v0 + v2), (load32(v5) + 150))
    v5 = (v40 << 2)
    v7 = (v1 + (v40 << 2))
    store32((v1 + (v40 << 2)), (load32(v7) + 150))
    v7 = (v4 + v5)
    store32((v4 + v5), (load32(v7) + 150))
    v5 = (v2 + v5)
    store32((v2 + v5), (load32(v5) + 150))
    v5 = (v24 << 2)
    v7 = (v1 + (v24 << 2))
    store32((v1 + (v24 << 2)), (load32(v7) + 150))
    v7 = (v4 + v5)
    store32((v4 + v5), (load32(v7) + 150))
    v5 = (v2 + v5)
    store32((v2 + v5), (load32(v5) + 150))
    v5 = (v23 << 2)
    v7 = (v1 + (v23 << 2))
    store32((v1 + (v23 << 2)), (load32(v7) + 150))
    v7 = (v4 + v5)
    store32((v4 + v5), (load32(v7) + 150))
    v5 = (v2 + v5)
    store32((v2 + v5), (load32(v5) + 150))
    v5 = (v22 << 2)
    v7 = (v1 + (v22 << 2))
    store32((v1 + (v22 << 2)), (load32(v7) + 150))
    v7 = (v4 + v5)
    store32((v4 + v5), (load32(v7) + 150))
    v5 = (v2 + v5)
    store32((v2 + v5), (load32(v5) + 150))
    v5 = (v21 << 2)
    v7 = (v1 + (v21 << 2))
    store32((v1 + (v21 << 2)), (load32(v7) + 150))
    v7 = (v4 + v5)
    store32((v4 + v5), (load32(v7) + 150))
    v5 = (v2 + v5)
    store32((v2 + v5), (load32(v5) + 150))
    v5 = (v53 << 2)
    v1 = (v1 + (v53 << 2))
    store32((v1 + (v53 << 2)), (load32(v1) + 100))
    v1 = (v4 + v5)
    store32((v4 + v5), (load32(v1) + 100))
    v2 = (v2 + v5)
    store32((v2 + v5), (load32(v2) + 100))
    v2 = ((v54 * 1020) + 9299904)
    v1 = (((v54 * 1020) + 9299904) + v29)
    store32((((v54 * 1020) + 9299904) + v29), (load32(v1) + 200))
    v1 = (v2 + v30)
    store32((v2 + v30), (load32(v1) + 200))
    v2 = (v2 + v31)
    store32((v2 + v31), (load32(v2) + 200))
    v17 = ((v12 * 1020) + 9299904)
    v2 = (((v12 * 1020) + 9299904) + v10)
    store32((((v12 * 1020) + 9299904) + v10), (load32(v2) + 150))
    v18 = ((v9 * 1020) + 9299904)
    v2 = (((v9 * 1020) + 9299904) + v10)
    store32((((v9 * 1020) + 9299904) + v10), (load32(v2) + 150))
    v2 = (v6 + v17)
    store32((v6 + v17), (load32(v2) + 150))
    v2 = (v6 + v18)
    store32((v6 + v18), (load32(v2) + 150))
    v2 = (v8 + v17)
    store32((v8 + v17), (load32(v2) + 150))
    v2 = (v8 + v18)
    store32((v8 + v18), (load32(v2) + 150))
    v4 = ((v24 * 1020) + 9299904)
    v2 = (v52 << 2)
    v1 = (((v24 * 1020) + 9299904) + (v52 << 2))
    store32((((v24 * 1020) + 9299904) + (v52 << 2)), (load32(v1) + 75))
    v10 = ((v23 * 1020) + 9299904)
    v1 = (((v23 * 1020) + 9299904) + v2)
    store32((((v23 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v6 = ((v22 * 1020) + 9299904)
    v1 = (((v22 * 1020) + 9299904) + v2)
    store32((((v22 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v8 = ((v21 * 1020) + 9299904)
    v1 = (((v21 * 1020) + 9299904) + v2)
    store32((((v21 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v5 = ((v26 * 1020) + 9299904)
    v1 = (((v26 * 1020) + 9299904) + v2)
    store32((((v26 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v7 = ((v25 * 1020) + 9299904)
    v1 = (((v25 * 1020) + 9299904) + v2)
    store32((((v25 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v14 = ((v14 * 1020) + 9299904)
    v1 = (((v14 * 1020) + 9299904) + v2)
    store32((((v14 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v13 = ((v13 * 1020) + 9299904)
    v1 = (((v13 * 1020) + 9299904) + v2)
    store32((((v13 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v16 = ((v16 * 1020) + 9299904)
    v1 = (((v16 * 1020) + 9299904) + v2)
    store32((((v16 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v15 = ((v15 * 1020) + 9299904)
    v1 = (((v15 * 1020) + 9299904) + v2)
    store32((((v15 * 1020) + 9299904) + v2), (load32(v1) + 75))
    v1 = (v51 << 2)
    v11 = (v4 + (v51 << 2))
    store32((v4 + (v51 << 2)), (load32(v11) + 100))
    v11 = (v1 + v10)
    store32((v1 + v10), (load32(v11) + 100))
    v11 = (v1 + v6)
    store32((v1 + v6), (load32(v11) + 100))
    v11 = (v1 + v8)
    store32((v1 + v8), (load32(v11) + 100))
    v11 = (v1 + v5)
    store32((v1 + v5), (load32(v11) + 100))
    v11 = (v1 + v7)
    store32((v1 + v7), (load32(v11) + 100))
    v11 = (v1 + v14)
    store32((v1 + v14), (load32(v11) + 100))
    v11 = (v1 + v13)
    store32((v1 + v13), (load32(v11) + 100))
    v11 = (v1 + v16)
    store32((v1 + v16), (load32(v11) + 100))
    v11 = (v1 + v15)
    store32((v1 + v15), (load32(v11) + 100))
    v11 = (v0 + v4)
    store32((v0 + v4), (load32(v11) - 75))
    v11 = (v0 + v10)
    store32((v0 + v10), (load32(v11) - 75))
    v11 = (v0 + v6)
    store32((v0 + v6), (load32(v11) - 75))
    v11 = (v0 + v8)
    store32((v0 + v8), (load32(v11) - 75))
    v11 = (v0 + v5)
    store32((v0 + v5), (load32(v11) - 75))
    v11 = (v0 + v7)
    store32((v0 + v7), (load32(v11) - 75))
    v11 = (v0 + v14)
    store32((v0 + v14), (load32(v11) - 75))
    v11 = (v0 + v13)
    store32((v0 + v13), (load32(v11) - 75))
    v11 = (v0 + v16)
    store32((v0 + v16), (load32(v11) - 75))
    v0 = (v0 + v15)
    store32((v0 + v15), (load32(v0) - 75))
    v0 = (v12 << 2)
    v12 = (v4 + (v12 << 2))
    store32((v4 + (v12 << 2)), (load32(v12) + 100))
    v12 = (v0 + v10)
    store32((v0 + v10), (load32(v12) + 100))
    v12 = (v0 + v6)
    store32((v0 + v6), (load32(v12) + 100))
    v12 = (v0 + v8)
    store32((v0 + v8), (load32(v12) + 100))
    v12 = (v0 + v5)
    store32((v0 + v5), (load32(v12) + 100))
    v12 = (v0 + v7)
    store32((v0 + v7), (load32(v12) + 100))
    v12 = (v0 + v14)
    store32((v0 + v14), (load32(v12) + 100))
    v12 = (v0 + v13)
    store32((v0 + v13), (load32(v12) + 100))
    v12 = (v0 + v16)
    store32((v0 + v16), (load32(v12) + 100))
    v0 = (v0 + v15)
    store32((v0 + v15), (load32(v0) + 100))
    v0 = (v9 << 2)
    v9 = (v4 + (v9 << 2))
    store32((v4 + (v9 << 2)), (load32(v9) + 100))
    v9 = (v0 + v10)
    store32((v0 + v10), (load32(v9) + 100))
    v9 = (v0 + v6)
    store32((v0 + v6), (load32(v9) + 100))
    v9 = (v0 + v8)
    store32((v0 + v8), (load32(v9) + 100))
    v9 = (v0 + v5)
    store32((v0 + v5), (load32(v9) + 100))
    v9 = (v0 + v7)
    store32((v0 + v7), (load32(v9) + 100))
    v9 = (v0 + v14)
    store32((v0 + v14), (load32(v9) + 100))
    v9 = (v0 + v13)
    store32((v0 + v13), (load32(v9) + 100))
    v9 = (v0 + v16)
    store32((v0 + v16), (load32(v9) + 100))
    v0 = (v0 + v15)
    store32((v0 + v15), (load32(v0) + 100))
    v0 = (v50 << 2)
    v9 = (v4 + (v50 << 2))
    store32((v4 + (v50 << 2)), (load32(v9) - 30))
    v9 = (v0 + v10)
    store32((v0 + v10), (load32(v9) - 30))
    v9 = (v0 + v6)
    store32((v0 + v6), (load32(v9) - 30))
    v9 = (v0 + v8)
    store32((v0 + v8), (load32(v9) - 30))
    v9 = (v0 + v5)
    store32((v0 + v5), (load32(v9) - 30))
    v9 = (v0 + v7)
    store32((v0 + v7), (load32(v9) - 30))
    v9 = (v0 + v14)
    store32((v0 + v14), (load32(v9) - 30))
    v9 = (v0 + v13)
    store32((v0 + v13), (load32(v9) - 30))
    v9 = (v0 + v16)
    store32((v0 + v16), (load32(v9) - 30))
    v0 = (v0 + v15)
    store32((v0 + v15), (load32(v0) - 30))
    v0 = (v62 << 2)
    v9 = (v4 + (v62 << 2))
    store32((v4 + (v62 << 2)), (load32(v9) + 50))
    v9 = (v0 + v10)
    store32((v0 + v10), (load32(v9) + 50))
    v9 = (v0 + v6)
    store32((v0 + v6), (load32(v9) + 50))
    v9 = (v0 + v8)
    store32((v0 + v8), (load32(v9) + 50))
    v9 = (v0 + v5)
    store32((v0 + v5), (load32(v9) + 50))
    v9 = (v0 + v7)
    store32((v0 + v7), (load32(v9) + 50))
    v9 = (v0 + v14)
    store32((v0 + v14), (load32(v9) + 50))
    v9 = (v0 + v13)
    store32((v0 + v13), (load32(v9) + 50))
    v9 = (v0 + v16)
    store32((v0 + v16), (load32(v9) + 50))
    v0 = (v0 + v15)
    store32((v0 + v15), (load32(v0) + 50))
    v0 = (v32 << 2)
    v4 = (v4 + (v32 << 2))
    store32((v4 + (v32 << 2)), (load32(v4) + 50))
    v4 = (v0 + v10)
    store32((v0 + v10), (load32(v4) + 50))
    v4 = (v0 + v6)
    store32((v0 + v6), (load32(v4) + 50))
    v4 = (v0 + v8)
    store32((v0 + v8), (load32(v4) + 50))
    v4 = (v0 + v5)
    store32((v0 + v5), (load32(v4) + 50))
    v4 = (v0 + v7)
    store32((v0 + v7), (load32(v4) + 50))
    v4 = (v0 + v14)
    store32((v0 + v14), (load32(v4) + 50))
    v4 = (v0 + v13)
    store32((v0 + v13), (load32(v4) + 50))
    v4 = (v0 + v16)
    store32((v0 + v16), (load32(v4) + 50))
    v4 = (v0 + v15)
    store32((v0 + v15), (load32(v4) + 50))
    v4 = ((v39 * 1020) + 9299904)
    v10 = (v36 << 2)
    v6 = (((v39 * 1020) + 9299904) + (v36 << 2))
    store32((((v39 * 1020) + 9299904) + (v36 << 2)), (load32(v6) + 400))
    v6 = ((v38 * 1020) + 9299904)
    v8 = (((v38 * 1020) + 9299904) + v10)
    store32((((v38 * 1020) + 9299904) + v10), (load32(v8) + 400))
    v10 = ((v37 * 1020) + 9299904)
    v8 = (v10 + ((v37 * 1020) + 9299904))
    store32((v10 + ((v37 * 1020) + 9299904)), (load32(v8) + 400))
    v8 = (v35 << 2)
    v5 = (v4 + (v35 << 2))
    store32((v4 + (v35 << 2)), (load32(v5) + 400))
    v5 = (v6 + v8)
    store32((v6 + v8), (load32(v5) + 400))
    v8 = (v8 + v10)
    store32((v8 + v10), (load32(v8) + 400))
    v4 = (v0 + v4)
    store32((v0 + v4), (load32(v4) + 400))
    v4 = (v0 + v6)
    store32((v0 + v6), (load32(v4) + 400))
    v0 = (v0 + v10)
    store32((v0 + v10), (load32(v0) + 400))
    v0 = ((v36 * 1020) + 9299904)
    v10 = (v39 << 2)
    v4 = (((v36 * 1020) + 9299904) + (v39 << 2))
    store32((((v36 * 1020) + 9299904) + (v39 << 2)), (load32(v4) + 300))
    v4 = ((v35 * 1020) + 9299904)
    v6 = (((v35 * 1020) + 9299904) + v10)
    store32((((v35 * 1020) + 9299904) + v10), (load32(v6) + 300))
    v10 = ((v32 * 1020) + 9299904)
    v6 = (v10 + ((v32 * 1020) + 9299904))
    store32((v10 + ((v32 * 1020) + 9299904)), (load32(v6) + 300))
    v6 = (v38 << 2)
    v8 = (v0 + (v38 << 2))
    store32((v0 + (v38 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v37 << 2)
    v8 = (v0 + (v37 << 2))
    store32((v0 + (v37 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v47 << 2)
    v8 = (v0 + (v47 << 2))
    store32((v0 + (v47 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v46 << 2)
    v8 = (v0 + (v46 << 2))
    store32((v0 + (v46 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v45 << 2)
    v8 = (v0 + (v45 << 2))
    store32((v0 + (v45 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v44 << 2)
    v8 = (v0 + (v44 << 2))
    store32((v0 + (v44 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v43 << 2)
    v8 = (v0 + (v43 << 2))
    store32((v0 + (v43 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v67 << 2)
    v8 = (v0 + (v67 << 2))
    store32((v0 + (v67 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v42 << 2)
    v8 = (v0 + (v42 << 2))
    store32((v0 + (v42 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v66 << 2)
    v8 = (v0 + (v66 << 2))
    store32((v0 + (v66 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v65 << 2)
    v8 = (v0 + (v65 << 2))
    store32((v0 + (v65 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v64 << 2)
    v8 = (v0 + (v64 << 2))
    store32((v0 + (v64 << 2)), (load32(v8) + 300))
    v8 = (v4 + v6)
    store32((v4 + v6), (load32(v8) + 300))
    v6 = (v6 + v10)
    store32((v6 + v10), (load32(v6) + 300))
    v6 = (v63 << 2)
    v0 = (v0 + (v63 << 2))
    store32((v0 + (v63 << 2)), (load32(v0) + 300))
    v0 = (v4 + v6)
    store32((v4 + v6), (load32(v0) + 300))
    v0 = (v6 + v10)
    store32((v6 + v10), (load32(v0) + 300))
    v0 = ((v81 * 1020) + 9299904)
    v4 = (((v81 * 1020) + 9299904) + v1)
    store32((((v81 * 1020) + 9299904) + v1), (load32(v4) - 20))
    v4 = ((v80 * 1020) + 9299904)
    v10 = (((v80 * 1020) + 9299904) + v1)
    store32((((v80 * 1020) + 9299904) + v1), (load32(v10) - 20))
    v10 = ((v79 * 1020) + 9299904)
    v6 = (((v79 * 1020) + 9299904) + v1)
    store32((((v79 * 1020) + 9299904) + v1), (load32(v6) - 20))
    v6 = ((v78 * 1020) + 9299904)
    v8 = (((v78 * 1020) + 9299904) + v1)
    store32((((v78 * 1020) + 9299904) + v1), (load32(v8) - 20))
    v8 = ((v77 * 1020) + 9299904)
    v5 = (((v77 * 1020) + 9299904) + v1)
    store32((((v77 * 1020) + 9299904) + v1), (load32(v5) - 20))
    v5 = ((v76 * 1020) + 9299904)
    v7 = (((v76 * 1020) + 9299904) + v1)
    store32((((v76 * 1020) + 9299904) + v1), (load32(v7) - 20))
    v7 = ((v75 * 1020) + 9299904)
    v14 = (((v75 * 1020) + 9299904) + v1)
    store32((((v75 * 1020) + 9299904) + v1), (load32(v14) - 20))
    v14 = ((v74 * 1020) + 9299904)
    v13 = (((v74 * 1020) + 9299904) + v1)
    store32((((v74 * 1020) + 9299904) + v1), (load32(v13) - 20))
    v13 = (v1 + v17)
    store32((v1 + v17), (load32(v13) - 20))
    v13 = (v1 + v18)
    store32((v1 + v18), (load32(v13) - 20))
    v13 = ((v34 * 1020) + 9299904)
    v16 = (((v34 * 1020) + 9299904) + v1)
    store32((((v34 * 1020) + 9299904) + v1), (load32(v16) - 20))
    v16 = ((v73 * 1020) + 9299904)
    v15 = (((v73 * 1020) + 9299904) + v1)
    store32((((v73 * 1020) + 9299904) + v1), (load32(v15) - 20))
    v15 = ((v72 * 1020) + 9299904)
    v9 = (((v72 * 1020) + 9299904) + v1)
    store32((((v72 * 1020) + 9299904) + v1), (load32(v9) - 20))
    v9 = ((v28 * 1020) + 9299904)
    v12 = (((v28 * 1020) + 9299904) + v1)
    store32((((v28 * 1020) + 9299904) + v1), (load32(v12) - 20))
    v12 = ((v68 * 1020) + 9299904)
    v11 = (((v68 * 1020) + 9299904) + v1)
    store32((((v68 * 1020) + 9299904) + v1), (load32(v11) - 20))
    v11 = ((v71 * 1020) + 9299904)
    v20 = (((v71 * 1020) + 9299904) + v1)
    store32((((v71 * 1020) + 9299904) + v1), (load32(v20) - 20))
    v20 = ((v27 * 1020) + 9299904)
    v21 = (((v27 * 1020) + 9299904) + v1)
    store32((((v27 * 1020) + 9299904) + v1), (load32(v21) - 20))
    v21 = ((v70 * 1020) + 9299904)
    v22 = (((v70 * 1020) + 9299904) + v1)
    store32((((v70 * 1020) + 9299904) + v1), (load32(v22) - 20))
    v22 = ((v47 * 1020) + 9299904)
    v23 = (((v47 * 1020) + 9299904) + v1)
    store32((((v47 * 1020) + 9299904) + v1), (load32(v23) - 20))
    v23 = ((v46 * 1020) + 9299904)
    v24 = (((v46 * 1020) + 9299904) + v1)
    store32((((v46 * 1020) + 9299904) + v1), (load32(v24) - 20))
    v24 = ((v45 * 1020) + 9299904)
    v25 = (((v45 * 1020) + 9299904) + v1)
    store32((((v45 * 1020) + 9299904) + v1), (load32(v25) - 20))
    v25 = ((v42 * 1020) + 9299904)
    v26 = (((v42 * 1020) + 9299904) + v1)
    store32((((v42 * 1020) + 9299904) + v1), (load32(v26) - 20))
    v26 = ((v44 * 1020) + 9299904)
    v27 = (((v44 * 1020) + 9299904) + v1)
    store32((((v44 * 1020) + 9299904) + v1), (load32(v27) - 20))
    v27 = ((v43 * 1020) + 9299904)
    v28 = (((v43 * 1020) + 9299904) + v1)
    store32((((v43 * 1020) + 9299904) + v1), (load32(v28) - 20))
    v28 = ((v69 * 1020) + 9299904)
    v34 = (((v69 * 1020) + 9299904) + v1)
    store32((((v69 * 1020) + 9299904) + v1), (load32(v34) - 20))
    v1 = ((v33 * 1020) + 9299904)
    v33 = (v1 + ((v33 * 1020) + 9299904))
    store32((v1 + ((v33 * 1020) + 9299904)), (load32(v33) - 20))
    v0 = (v0 + v2)
    store32((v0 + v2), (load32(v0) - 50))
    v0 = (v2 + v4)
    store32((v2 + v4), (load32(v0) - 50))
    v0 = (v2 + v10)
    store32((v2 + v10), (load32(v0) - 50))
    v0 = (v2 + v6)
    store32((v2 + v6), (load32(v0) - 50))
    v0 = (v2 + v8)
    store32((v2 + v8), (load32(v0) - 50))
    v0 = (v2 + v5)
    store32((v2 + v5), (load32(v0) - 50))
    v0 = (v2 + v7)
    store32((v2 + v7), (load32(v0) - 50))
    v0 = (v2 + v14)
    store32((v2 + v14), (load32(v0) - 50))
    v0 = (v2 + v17)
    store32((v2 + v17), (load32(v0) - 50))
    v0 = (v2 + v18)
    store32((v2 + v18), (load32(v0) - 50))
    v0 = (v2 + v13)
    store32((v2 + v13), (load32(v0) - 50))
    v0 = (v2 + v16)
    store32((v2 + v16), (load32(v0) - 50))
    v0 = (v2 + v15)
    store32((v2 + v15), (load32(v0) - 50))
    v0 = (v2 + v9)
    store32((v2 + v9), (load32(v0) - 50))
    v0 = (v2 + v12)
    store32((v2 + v12), (load32(v0) - 50))
    v0 = (v2 + v11)
    store32((v2 + v11), (load32(v0) - 50))
    v0 = (v2 + v20)
    store32((v2 + v20), (load32(v0) - 50))
    v0 = (v2 + v21)
    store32((v2 + v21), (load32(v0) - 50))
    v0 = (v2 + v22)
    store32((v2 + v22), (load32(v0) - 50))
    v0 = (v2 + v23)
    store32((v2 + v23), (load32(v0) - 50))
    v0 = (v2 + v24)
    store32((v2 + v24), (load32(v0) - 50))
    v0 = (v2 + v25)
    store32((v2 + v25), (load32(v0) - 50))
    v0 = (v2 + v26)
    store32((v2 + v26), (load32(v0) - 50))
    v0 = (v2 + v27)
    store32((v2 + v27), (load32(v0) - 50))
    v0 = (v2 + v28)
    store32((v2 + v28), (load32(v0) - 50))
    v2 = (v1 + v2)
    store32((v1 + v2), (load32(v2) - 50))
    v1 = 0
    v2 = 0
    while True:  # $label5
        v0 = ((v49 * 1020) + 9299904)
        v4 = (v2 << 2)
        v5 = (v3 + 272)
        v10 = (((v49 * 1020) + 9299904) + (load32(((v2 << 2) + (v3 + 272))) << 2))
        store32((((v49 * 1020) + 9299904) + (load32(((v2 << 2) + (v3 + 272))) << 2)), (load32(v10) + 100))
        v10 = (v0 + (load32(((v4 | 4) + v5)) << 2))
        store32((v0 + (load32(((v4 | 4) + v5)) << 2)), (load32(v10) + 100))
        v4 = (v0 + (load32(((v4 | 8) + v5)) << 2))
        store32((v0 + (load32(((v4 | 8) + v5)) << 2)), (load32(v4) + 100))
        v4 = (v2 | 3)
        if ((v2 | 3) == 71):
            v2 = ((v48 * 1020) + 9299904)
            while True:  # $label4
                v0 = (v1 << 2)
                v5 = (v3 + 272)
                v4 = (v2 + (load32(((v1 << 2) + (v3 + 272))) << 2))
                store32((v2 + (load32(((v1 << 2) + (v3 + 272))) << 2)), (load32(v4) + 400))
                v4 = (v2 + (load32(((v0 | 4) + v5)) << 2))
                store32((v2 + (load32(((v0 | 4) + v5)) << 2)), (load32(v4) + 400))
                v0 = (v2 + (load32(((v0 | 8) + v5)) << 2))
                store32((v2 + (load32(((v0 | 8) + v5)) << 2)), (load32(v0) + 400))
                v0 = (v1 | 3)
                if not ((v1 | 3) == 71):
                    v0 = (v2 + (load32(((v3 + 272) + (v0 << 2))) << 2))
                    store32((v2 + (load32(((v3 + 272) + (v0 << 2))) << 2)), (load32(v0) + 400))
                    v1 = (v1 + 4)
                    continue
                break
            v2 = (v32 << 2)
            v1 = ((v32 << 2) + ((v47 * 1020) + 9299904))
            store32(((v32 << 2) + ((v47 * 1020) + 9299904)), (load32(v1) - 50))
            v1 = (((v46 * 1020) + 9299904) + v2)
            store32((((v46 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v1 = (((v45 * 1020) + 9299904) + v2)
            store32((((v45 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v1 = (((v44 * 1020) + 9299904) + v2)
            store32((((v44 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v1 = (((v43 * 1020) + 9299904) + v2)
            store32((((v43 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v1 = (((v67 * 1020) + 9299904) + v2)
            store32((((v67 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v1 = (((v42 * 1020) + 9299904) + v2)
            store32((((v42 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v1 = (((v66 * 1020) + 9299904) + v2)
            store32((((v66 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v1 = (((v65 * 1020) + 9299904) + v2)
            store32((((v65 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v1 = (((v64 * 1020) + 9299904) + v2)
            store32((((v64 * 1020) + 9299904) + v2), (load32(v1) - 50))
            v2 = (((v63 * 1020) + 9299904) + v2)
            store32((((v63 * 1020) + 9299904) + v2), (load32(v2) - 50))
            G.global0 = (v3 + 560)
        else:
            v0 = (v0 + (load32(((v3 + 272) + (v4 << 2))) << 2))
            store32((v0 + (load32(((v3 + 272) + (v4 << 2))) << 2)), (load32(v0) + 100))
            v2 = (v2 + 4)
            continue
        break

# ----------------------------------------------------------
# $func221
# ----------------------------------------------------------
def func221(arg0):
    arg0 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v1 = load16u(entities[load32(9173808)] + 110)
    store32(9671124, 240)
    store32(9671120, 0)
    v2 = load32(PLAYERS)
    a_b()
    while True:  # $label0
        v2 = (v2 + (v1 * 286704))
        v1 = load32((v2 + (v1 * 286704)) + 281792)
        if not load32((v2 + (v1 * 286704)) + 281792):
            break
        if not load32(v1 + 8):
            break
        v2 = (v2 + 281792)
        while True:  # $label1
            v4 = (v3 << 2)
            if load32(((v3 << 2) + load32(v1))):
                v1 = load32(9671120)
                store32(9671120, (load32(9671120) + 1))
                store32(((v1 << 2) + 9263072), 9256340)
                v1 = load32(((load16u((load32(load32(v2)) + v4)) * 404) + ENTITY_TYPES) + 144)
                store64(arg0 + 40, 4294967295)
                store64(arg0 + 32, 0)
                store64(arg0 + 24, 0)
                store64(arg0 + 16, 1)
                store64(arg0 + 8, 1)
                store32(arg0, v3)
                store32(arg0 + 4, (0 - v1))
                a_b()
                v1 = load32(v2)
            v3 = (v3 + 1)
            if (u32((v3 + 1)) < u32(load32(v1 + 8))):
                continue
            break
        break
    G.global0 = (arg0 + 48)

# ----------------------------------------------------------
# $func222
# ----------------------------------------------------------
def func222(arg0):
    arg0 = 0
    store32(9671124, 95)
    store32(9671120, 0)
    while True:  # $label0
        v3 = entities[load32(9173808)]
        v1 = load32(entities[load32(9173808)].z)
        if not load32(entities[load32(9173808)].z):
            break
        v1 = load32(v1)
        v2 = load32(load32(v1))
        if load32(load32(v1)):
            store32(9263072, load32(((v2 * 404) + 9567872)))
            store32(9671120, 1)
            v1 = load32(load32(v3 + 20))
            arg0 = 1
        v2 = load32(v1 + 4)
        if load32(v1 + 4):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 8)
        if load32(v1 + 8):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 12)
        if load32(v1 + 12):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 16)
        if load32(v1 + 16):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 20)
        if load32(v1 + 20):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 24)
        if load32(v1 + 24):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
        else:
        v1 = load32(v1 + 28)
        if not load32(v1 + 28):
            break
        store32(((arg0 << 2) + 9263072), load32(((v1 * 404) + 9567872)))
        store32(9671120, (arg0 + 1))
        break
    return func46(0, 1)
