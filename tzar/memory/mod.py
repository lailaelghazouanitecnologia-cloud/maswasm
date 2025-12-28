"""
Tzar Engine - Memory module.
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

# Known addresses
GAME_STATE = 9142424
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892
PLAYERS = 9561692
ENTITY_TYPES = 9568096
ENTITIES = 9671128
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
# $func26
# ----------------------------------------------------------
def func26(arg0):
    arg0 = (1 if (u32(arg0) <= u32(1)) else arg0)
    while True:  # $label0
        while True:  # $label1
            v1 = e()
            if e():
                break
            v1 = atomic_load(ALLOC_HANDLER)
            if atomic_load(ALLOC_HANDLER):
                continue
            break
        a_g()
        raise Unreachable()
        break
    return v1

# ----------------------------------------------------------
# $af
# Export: af
# ----------------------------------------------------------
def af(arg0):
    """Export: af"""
    while True:  # $label0
        if not arg0:
            break
        if (load8u(MEM_FLAGS) & 2):
            if func55(MEM_MUTEX):
                break
        v2 = (arg0 - 8)
        v1 = load32((arg0 - 4))
        arg0 = (load32((arg0 - 4)) & -8)
        v5 = ((arg0 - 8) + (load32((arg0 - 4)) & -8))
        while True:  # $label2
            while True:  # $label1
                if (v1 & 1):
                    break
                if not (v1 & 3):
                    break
                v1 = load32(v2)
                v2 = (v2 - load32(v2))
                if (u32((v2 - load32(v2))) < u32(load32(HEAP_BASE))):
                    break
                arg0 = (arg0 + v1)
                if (load32(HEAP_TOP) != v2):
                    if (u32(v1) <= u32(255)):
                        v4 = ((v1 & 0xFFFFFFFF) >> 3)
                        v1 = load32(v2 + 12)
                        v3 = load32(v2 + 8)
                        if (load32(v2 + 12) == load32(v2 + 8)):
                            store32(HEAP_FREELIST, (load32(HEAP_FREELIST) & rotl(-2, v4)))
                            break
                        store32(v3 + 12, v1)
                        store32(v1 + 8, v3)
                        break
                    v6 = load32(v2 + 24)
                    while True:  # $label3
                        v1 = load32(v2 + 12)
                        if (v2 != load32(v2 + 12)):
                            v3 = load32(v2 + 8)
                            store32(load32(v2 + 8) + 12, v1)
                            store32(v1 + 8, v3)
                            break
                        while True:  # $label4
                            v3 = (v2 + 20)
                            v4 = load32((v2 + 20))
                            if load32((v2 + 20)):
                                break
                            v3 = (v2 + 16)
                            v4 = load32((v2 + 16))
                            if load32((v2 + 16)):
                                break
                            v1 = 0
                            break
                            break
                        while True:  # $label5
                            v7 = v3
                            v1 = v4
                            v3 = (v4 + 20)
                            v4 = load32((v4 + 20))
                            if load32((v4 + 20)):
                                continue
                            v3 = (v1 + 16)
                            v4 = load32(v1 + 16)
                            if load32(v1 + 16):
                                continue
                            break
                        store32(v7, 0)
                        break
                    if not v6:
                        break
                    while True:  # $label6
                        v3 = load32(v2 + 28)
                        v4 = ((load32(v2 + 28) << 2) + 9690768)
                        if (load32(((load32(v2 + 28) << 2) + 9690768)) == v2):
                            store32(v4, v1)
                            if v1:
                                break
                            store32(HEAP_TREE, (load32(HEAP_TREE) & rotl(-2, v3)))
                            break
                        store32((v6 + (16 if (load32(v6 + 16) == v2) else 20)), v1)
                        if not v1:
                            break
                        break
                    store32(v1 + 24, v6)
                    v3 = load32(v2 + 16)
                    if load32(v2 + 16):
                        store32(v1 + 16, v3)
                        store32(v3 + 24, v1)
                    v3 = load32(v2 + 20)
                    if not load32(v2 + 20):
                        break
                    store32(v1 + 20, v3)
                    store32(v3 + 24, v1)
                    break
                v1 = load32(v5 + 4)
                if ((load32(v5 + 4) & 3) != 3):
                    break
                store32(FREE_SIZE, arg0)
                store32(v5 + 4, (v1 & -2))
                store32(v2 + 4, (arg0 | 1))
                store32((arg0 + v2), arg0)
                break
                break
            if (u32(v2) >= u32(v5)):
                break
            v1 = load32(v5 + 4)
            if not (load32(v5 + 4) & 1):
                break
            while True:  # $label12
                if not (v1 & 2):
                    if (load32(HEAP_END) == v5):
                        store32(HEAP_END, v2)
                        arg0 = (load32(HEAP_TOTAL) + arg0)
                        store32(HEAP_TOTAL, (load32(HEAP_TOTAL) + arg0))
                        store32(v2 + 4, (arg0 | 1))
                        if (v2 != load32(HEAP_TOP)):
                            break
                        store32(FREE_SIZE, 0)
                        store32(HEAP_TOP, 0)
                        break
                    if (load32(HEAP_TOP) == v5):
                        store32(HEAP_TOP, v2)
                        arg0 = (load32(FREE_SIZE) + arg0)
                        store32(FREE_SIZE, (load32(FREE_SIZE) + arg0))
                        store32(v2 + 4, (arg0 | 1))
                        store32((arg0 + v2), arg0)
                        break
                    arg0 = ((v1 & -8) + arg0)
                    while True:  # $label7
                        if (u32(v1) <= u32(255)):
                            v4 = ((v1 & 0xFFFFFFFF) >> 3)
                            v1 = load32(v5 + 12)
                            v3 = load32(v5 + 8)
                            if (load32(v5 + 12) == load32(v5 + 8)):
                                store32(HEAP_FREELIST, (load32(HEAP_FREELIST) & rotl(-2, v4)))
                                break
                            store32(v3 + 12, v1)
                            store32(v1 + 8, v3)
                            break
                        v6 = load32(v5 + 24)
                        while True:  # $label8
                            v1 = load32(v5 + 12)
                            if (v5 != load32(v5 + 12)):
                                v3 = load32(v5 + 8)
                                store32(load32(v5 + 8) + 12, v1)
                                store32(v1 + 8, v3)
                                break
                            while True:  # $label9
                                v4 = (v5 + 20)
                                v3 = load32((v5 + 20))
                                if load32((v5 + 20)):
                                    break
                                v4 = (v5 + 16)
                                v3 = load32((v5 + 16))
                                if load32((v5 + 16)):
                                    break
                                v1 = 0
                                break
                                break
                            while True:  # $label10
                                v7 = v4
                                v1 = v3
                                v4 = (v3 + 20)
                                v3 = load32((v3 + 20))
                                if load32((v3 + 20)):
                                    continue
                                v4 = (v1 + 16)
                                v3 = load32(v1 + 16)
                                if load32(v1 + 16):
                                    continue
                                break
                            store32(v7, 0)
                            break
                        if not v6:
                            break
                        while True:  # $label11
                            v3 = load32(v5 + 28)
                            v4 = ((load32(v5 + 28) << 2) + 9690768)
                            if (load32(((load32(v5 + 28) << 2) + 9690768)) == v5):
                                store32(v4, v1)
                                if v1:
                                    break
                                store32(HEAP_TREE, (load32(HEAP_TREE) & rotl(-2, v3)))
                                break
                            store32((v6 + (16 if (load32(v6 + 16) == v5) else 20)), v1)
                            if not v1:
                                break
                            break
                        store32(v1 + 24, v6)
                        v3 = load32(v5 + 16)
                        if load32(v5 + 16):
                            store32(v1 + 16, v3)
                            store32(v3 + 24, v1)
                        v3 = load32(v5 + 20)
                        if not load32(v5 + 20):
                            break
                        store32(v1 + 20, v3)
                        store32(v3 + 24, v1)
                        break
                    store32(v2 + 4, (arg0 | 1))
                    store32((arg0 + v2), arg0)
                    if (v2 != load32(HEAP_TOP)):
                        break
                    store32(FREE_SIZE, arg0)
                    break
                store32(v5 + 4, (v1 & -2))
                store32(v2 + 4, (arg0 | 1))
                store32((arg0 + v2), arg0)
                break
            if (u32(arg0) <= u32(255)):
                v1 = ((arg0 & -8) + 9690504)
                while True:  # $label13
                    v3 = load32(HEAP_FREELIST)
                    arg0 = (1 << ((arg0 & 0xFFFFFFFF) >> 3))
                    if not (load32(HEAP_FREELIST) & (1 << ((arg0 & 0xFFFFFFFF) >> 3))):
                        store32(HEAP_FREELIST, (arg0 | v3))
                        break
                    break
                arg0 = load32(v1 + 8)
                store32(v1 + 8, v2)
                store32(arg0 + 12, v2)
                store32(v2 + 12, v1)
                store32(v2 + 8, arg0)
                break
            v3 = 31
            if (u32(arg0) <= u32(16777215)):
                v1 = clz(((arg0 & 0xFFFFFFFF) >> 8))
                v3 = (((((arg0 & 0xFFFFFFFF) >> (38 - clz(((arg0 & 0xFFFFFFFF) >> 8)))) & 1) - (v1 << 1)) + 62)
            store32(v2 + 28, v3)
            store64(v2 + 16, 0)
            v1 = ((v3 << 2) + 9690768)
            while True:  # $label17
                while True:  # $label15
                    while True:  # $label14
                        v4 = load32(HEAP_TREE)
                        v7 = (1 << v3)
                        if not (load32(HEAP_TREE) & (1 << v3)):
                            store32(HEAP_TREE, (v4 | v7))
                            store32(v1, v2)
                            store32(v2 + 24, v1)
                            break
                        v3 = (arg0 << ((25 - ((v3 & 0xFFFFFFFF) >> 1)) if (v3 != 31) else 0))
                        v1 = load32(v1)
                        while True:  # $label16
                            v4 = v1
                            if ((load32(v1 + 4) & -8) == arg0):
                                break
                            v1 = ((v3 & 0xFFFFFFFF) >> 29)
                            v3 = (v3 << 1)
                            v7 = (v4 + (v1 & 4))
                            v1 = load32(((v4 + (v1 & 4)) + 16))
                            if load32(((v4 + (v1 & 4)) + 16)):
                                continue
                            break
                        store32(v7 + 16, v2)
                        store32(v2 + 24, v4)
                        break
                    store32(v2 + 12, v2)
                    store32(v2 + 8, v2)
                    break
                    break
                arg0 = load32(v4 + 8)
                store32(load32(v4 + 8) + 12, v2)
                store32(v4 + 8, v2)
                store32(v2 + 24, 0)
                store32(v2 + 12, v4)
                store32(v2 + 8, arg0)
                break
            arg0 = (load32(ALLOC_COUNT) - 1)
            store32(ALLOC_COUNT, ((load32(ALLOC_COUNT) - 1) if arg0 else -1))
            break
        if not (load8u(MEM_FLAGS) & 2):
            break
        func54(MEM_MUTEX)
        break
    return v1

# ----------------------------------------------------------
# $func28
# ----------------------------------------------------------
def func28(arg0, arg1):
    v9 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # $label0
        if load8u(9147152):
            break
        if not load32(40600):
            break
        if not arg0:
            store32(9671120, 0)
            store32(9263840, 0)
            store32(9671124, 0)
            while True:  # $label1
                arg0 = ((v4 * 132) + 9216080)
                store32(((v4 * 132) + 9216080) + 116, 0)
                store32(arg0 + 16, 0)
                store16(arg0 + 21, 0)
                store64(arg0 + 124, 0)
                store8(arg0 + 24, 0)
                v4 = (v4 + 1)
                if ((v4 + 1) != 356):
                    continue
                break
            # TODO: memory.fill
            store32(9215968, 0)
            arg0 = load32(9213808)
            store8(59186, (load32(9213808) != 0))
            while True:  # $label2
                if not arg0:
                    store32(9263840, 0)
                    break
                v23 = load32(ENTITIES)
                while True:  # $label39
                    v8 = (v23 + (load32(((v24 << 2) + 9173808)) * 132))
                    v6 = load16u((v23 + (load32(((v24 << 2) + 9173808)) * 132)) + 110)
                    while True:  # $label5
                        while True:  # $label3
                            if not v10:
                                break
                            arg0 = 0
                            v3 = load32(9215960)
                            while True:  # $label4
                                if (v6 != load32((v3 + (arg0 << 2)))):
                                    arg0 = (arg0 + 1)
                                    if (v10 != (arg0 + 1)):
                                        continue
                                    break
                                break
                            v3 = v6
                            break
                            break
                        while True:  # $label6
                            if (load32(9215964) != v10):
                                arg0 = load32(9215960)
                                break
                            arg0 = (load32(9215972) + v10)
                            store32(9215964, (load32(9215972) + v10))
                            v3 = load32(9215960)
                            arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                            if v10:
                                # TODO: memory.copy
                            if v3:
                                v23 = load32(ENTITIES)
                                v10 = load32(9215968)
                            store32(9215960, arg0)
                            break
                        v3 = load16u(v8 + 110)
                        store32(9215968, (v10 + 1))
                        store32((arg0 + (v10 << 2)), v6)
                        v10 = load32(9215968)
                        break
                    while True:  # $label7
                        v25 = load8u(v8 + 125)
                        if (u32(((load8u(v8 + 125) - 9) & 255)) < u32(3)):
                            break
                        v2 = load8u(v8 + 122)
                        v14 = ((load8u(v8 + 122) * 404) + ENTITY_TYPES)
                        if not load8u(((load8u(v8 + 122) * 404) + ENTITY_TYPES) + 353):
                            store8(59186, 0)
                        v15 = load32(PLAYERS)
                        while True:  # $label9
                            while True:  # $label8
                                if (v25 != 5):
                                    if (load32((load32(9215884) + (load32(v8 + 44) << 4)) + 4) != 34):
                                        break
                                v6 = func26(4)
                                store32(func26(4), 6)
                                v13 = 1
                                break
                                break
                            if (v2 == load32(38852)):
                                if load32((v15 + (v3 * 286704)) + 283912):
                                    break
                            v6 = load32(v14 + 232)
                            v13 = load32(v14 + 236)
                            arg0 = load32(v8 + 24)
                            if not load32(v8 + 24):
                                break
                            v4 = load32(arg0)
                            if not load32(arg0):
                                break
                            arg0 = load32(v4)
                            if not load32(v4):
                                break
                            v13 = load32(v4 + 8)
                            v6 = arg0
                            break
                        while True:  # $label10
                            v12 = load32(v8 + 20)
                            if not load32(v8 + 20):
                                break
                            if (load32(v14 + 264) != 1):
                                break
                            if (load32(38540) == v2):
                                break
                            if (load32(38812) == v2):
                                break
                            if (load32(38888) == v2):
                                break
                            if v13:
                                v7 = load32((v15 + (v3 * 286704)) + 281796)
                                v2 = 0
                                while True:  # $label15
                                    v5 = ((load32((v6 + (v2 << 2))) * 132) + 9216080)
                                    v17 = load32(((load32((v6 + (v2 << 2))) * 132) + 9216080) + 4)
                                    store32(((load32(((load32((v6 + (v2 << 2))) * 132) + 9216080) + 4) << 2) + 9143024), v2)
                                    store8(v5 + 21, 1)
                                    v2 = (v2 + 1)
                                    while True:  # $label11
                                        if not v7:
                                            break
                                        if not load8u(v5 + 23):
                                            break
                                        v11 = load32(v7 + 8)
                                        if not load32(v7 + 8):
                                            break
                                        v16 = ((((v11 - 1) & 0xFFFFFFFF) >> 1) + 1)
                                        v19 = (((((v11 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                                        v18 = load32(v8 + 28)
                                        v4 = load32(v7)
                                        arg0 = 0
                                        if (u32(v11) >= u32(3)):
                                            v20 = (v16 & -2)
                                            v11 = 0
                                            while True:  # $label14
                                                while True:  # $label12
                                                    v16 = (arg0 << 2)
                                                    if (load32((v4 + (arg0 << 2))) != v18):
                                                        break
                                                    if (load32((v4 + (v16 | 4))) != v17):
                                                        break
                                                    store32(v5 + 128, 2147483647)
                                                    break
                                                while True:  # $label13
                                                    if (load32((v4 + (v16 | 8))) != v18):
                                                        break
                                                    if (load32((v4 + (v16 | 12))) != v17):
                                                        break
                                                    store32(v5 + 128, 2147483647)
                                                    break
                                                arg0 = (arg0 + 4)
                                                v11 = (v11 + 2)
                                                if ((v11 + 2) != v20):
                                                    continue
                                                break
                                        if not v19:
                                            break
                                        arg0 = (arg0 << 2)
                                        if (load32((v4 + (arg0 << 2))) != v18):
                                            break
                                        if (load32((v4 + (arg0 | 4))) != v17):
                                            break
                                        store32(v5 + 128, 2147483647)
                                        break
                                    if (v2 != v13):
                                        continue
                                    break
                            if load32(v12 + 8):
                                v11 = load32(v12)
                                v7 = 0
                                while True:  # $label20
                                    while True:  # $label17
                                        while True:  # $label16
                                            v5 = load32((v11 + (v7 << 2)))
                                            if (u32(load32((v11 + (v7 << 2)))) >= u32(2147483647)):
                                                v5 = (v5 - 2147483647)
                                                arg0 = ((load32((((v5 - 2147483647) << 2) + 9143024)) << 2) + 9147392)
                                                v2 = load32(((load32((((v5 - 2147483647) << 2) + 9143024)) << 2) + 9147392))
                                                v4 = (1073741824 if (v2 <= 1073741824) else load32(((load32((((v5 - 2147483647) << 2) + 9143024)) << 2) + 9147392)))
                                                break
                                            arg0 = ((load32(((v5 << 2) + 9143024)) << 2) + 9147392)
                                            v4 = load32(((load32(((v5 << 2) + 9143024)) << 2) + 9147392))
                                            if (load32(((load32(((v5 << 2) + 9143024)) << 2) + 9147392)) > 1073741823):
                                                break
                                            break
                                        store32(arg0, (v4 + 1))
                                        break
                                    v7 = (v7 + 1)
                                    arg0 = 0
                                    if v13:
                                        while True:  # $label19
                                            while True:  # $label18
                                                v2 = ((load32((v6 + (arg0 << 2))) * 132) + 9216080)
                                                if not load8u(((load32((v6 + (arg0 << 2))) * 132) + 9216080) + 23):
                                                    break
                                                if (load32(v2 + 4) != v5):
                                                    break
                                                if load32(v2 + 128):
                                                    break
                                                store32(v2 + 128, v7)
                                                break
                                            arg0 = (arg0 + 1)
                                            if ((arg0 + 1) != v13):
                                                continue
                                            break
                                    if (u32(v7) < u32(load32(v12 + 8))):
                                        continue
                                    break
                            v2 = load32((v15 + (v3 * 286704)) + 281796)
                            if not load32((v15 + (v3 * 286704)) + 281796):
                                break
                            if (load8u(v8 + 125) == 14):
                                break
                            v4 = load32(v2 + 8)
                            if not load32(v2 + 8):
                                break
                            v5 = load32(v2)
                            arg0 = 0
                            while True:  # $label21
                                v7 = (arg0 << 2)
                                if (load32((v5 + (arg0 << 2))) == load32(v8 + 28)):
                                    v4 = ((load32(((load32((v5 + (v7 | 4))) << 2) + 9143024)) << 2) + 9147392)
                                    v4 = load32(v4)
                                    store32(((load32(((load32((v5 + (v7 | 4))) << 2) + 9143024)) << 2) + 9147392), ((1073741824 if (v4 <= 1073741824) else load32(v4)) + 1))
                                    v4 = load32(v2 + 8)
                                arg0 = (arg0 + 2)
                                if (u32((arg0 + 2)) < u32(v4)):
                                    continue
                                break
                            break
                        if not v13:
                            break
                        v12 = 0
                        v4 = (v15 + (v3 * 286704))
                        v17 = (((v15 + (v3 * 286704)) + (load32(39144) << 2)) + 281808)
                        v18 = (v4 + 281796)
                        v16 = ((load32(9143364) << 2) + 9147392)
                        v19 = (v4 + 283868)
                        v20 = (v4 + 283916)
                        v7 = load32(9213808)
                        while True:  # $label38
                            while True:  # $label22
                                while True:  # $label23
                                    arg0 = load32((v6 + (v12 << 2)))
                                    if (load32((v6 + (v12 << 2))) <= 317):
                                        while True:  # $label24
                                            # br_table (arg0 - 186)
                                            break
                                            break
                                        if (arg0 != 4):
                                            break
                                        break
                                    if (arg0 != 318):
                                        if (arg0 != 350):
                                            break
                                        arg0 = 350
                                        if (u32(load32(v8 + 84)) >= u32(3)):
                                            break
                                        break
                                    arg0 = (323 if load32(v20) else 318)
                                    break
                                while True:  # $label25
                                    v3 = ((arg0 * 132) + 9216080)
                                    v26 = load32(((arg0 * 132) + 9216080) + 12)
                                    if (load32(((arg0 * 132) + 9216080) + 12) != 85):
                                        break
                                    if (load32(v17) != 1):
                                        break
                                    store32(v16, load32(v19))
                                    break
                                while True:  # $label26
                                    v2 = load8u(v3 + 23)
                                    if load8u(v3 + 23):
                                        arg0 = load32(v3 + 4)
                                        if (load32(((load32(v3 + 4) * 404) + ENTITY_TYPES) + 264) != 3):
                                            break
                                        arg0 = (v4 + (arg0 << 2))
                                        if load32(((v4 + (arg0 << 2)) + 281808)):
                                            store32(v3 + 124, 1)
                                        if not load32((arg0 + 282828)):
                                            break
                                        store32(v3 + 124, 2)
                                        break
                                    while True:  # $label27
                                        # br_table (v25 - 4)
                                        break
                                        break
                                    store8(v3 + 22, 1)
                                    store32(v3 + 124, 3)
                                    break
                                v27 = (load32(v3 + 16) + 1)
                                store32(v3 + 16, (load32(v3 + 16) + 1))
                                arg0 = 0
                                while True:  # $label28
                                    v5 = load32(v8 + 24)
                                    if not load32(v8 + 24):
                                        break
                                    v5 = load32(v5)
                                    if not load32(v5):
                                        break
                                    if not load32(v5):
                                        break
                                    arg0 = (u32(v12) >= u32(load32(v14 + 236)))
                                    break
                                store8(v3 + 21, arg0)
                                while True:  # $label29
                                    if (v7 != 1):
                                        break
                                    v11 = load32(v8 + 20)
                                    if not load32(v8 + 20):
                                        break
                                    if not v2:
                                        break
                                    if (load32(v14 + 264) != 1):
                                        break
                                    while True:  # $label30
                                        # br_table load32(((load32(v3 + 4) * 404) + ENTITY_TYPES) + 264)
                                        break
                                        break
                                    store8(v3 + 21, 1)
                                    v28 = load32(v3 + 68)
                                    if not load32(v3 + 68):
                                        break
                                    v2 = 0
                                    while True:  # $label35
                                        while True:  # $label32
                                            while True:  # $label31
                                                v15 = load32((v3 + (v2 << 2)) + 28)
                                                if (load32(((load32((v3 + (v2 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) != 3):
                                                    break
                                                v21 = load32(v11 + 8)
                                                if load32(v11 + 8):
                                                    v22 = load32(v11)
                                                    v5 = 0
                                                    while True:  # $label33
                                                        arg0 = load32((v22 + (v5 << 2)))
                                                        if (((load32((v22 + (v5 << 2))) - 2147483647) if (u32(arg0) > u32(2147483646)) else arg0) == v15):
                                                            break
                                                        v5 = (v5 + 1)
                                                        if ((v5 + 1) != v21):
                                                            continue
                                                        break
                                                arg0 = load32(v18)
                                                if not load32(v18):
                                                    break
                                                v21 = load32(arg0 + 8)
                                                if not load32(arg0 + 8):
                                                    break
                                                v22 = load32(v8 + 28)
                                                v5 = load32(arg0)
                                                arg0 = 0
                                                while True:  # $label34
                                                    v29 = (arg0 << 2)
                                                    if (v22 == load32((v5 + (arg0 << 2)))):
                                                        if (load32((v5 + (v29 | 4))) == v15):
                                                            break
                                                    arg0 = (arg0 + 2)
                                                    if (u32((arg0 + 2)) < u32(v21)):
                                                        continue
                                                    break
                                                break
                                            store8(v3 + 21, 0)
                                            break
                                            break
                                        v2 = (v2 + 1)
                                        if ((v2 + 1) != v28):
                                            continue
                                        break
                                    break
                                while True:  # $label36
                                    v2 = load32(v14 + 164)
                                    if (u32(load32(v14 + 164)) < u32(2)):
                                        break
                                    v5 = load32(v14 + 160)
                                    arg0 = 1
                                    while True:  # $label37
                                        v11 = (v5 + (arg0 << 2))
                                        if (v26 != load32((v5 + (arg0 << 2)))):
                                            arg0 = (arg0 + 2)
                                            if (u32((arg0 + 2)) < u32(v2)):
                                                continue
                                            break
                                        break
                                    if (arg0 < 0):
                                        break
                                    arg0 = load32((v11 - 4))
                                    v2 = load32(v3 + 116)
                                    if load32(v3 + 116):
                                        v2 = (arg0 == v2)
                                        arg0 = 1
                                        if v2:
                                            break
                                    store32(v3 + 116, arg0)
                                    break
                                if (v7 != v27):
                                    break
                                arg0 = load32(9671120)
                                store32(9671120, (load32(9671120) + 1))
                                store32(((arg0 << 2) + 9263072), v3)
                                break
                            v12 = (v12 + 1)
                            if ((v12 + 1) != v13):
                                continue
                            break
                        break
                    v24 = (v24 + 1)
                    if (u32((v24 + 1)) < u32(load32(9213808))):
                        continue
                    break
                arg0 = 0
                store32(9263840, 0)
                v8 = load32(9671120)
                if not load32(9671120):
                    break
                v6 = 0
                while True:  # $label41
                    while True:  # $label40
                        v3 = load32(((arg0 << 2) + 9263072))
                        if not load32(((arg0 << 2) + 9263072)):
                            break
                        v10 = load32(v3 + 116)
                        if (u32(load32(v3 + 116)) < u32(2)):
                            break
                        v2 = ((v6 << 2) + 9263328)
                        store32(((v6 << 2) + 9263328), v10)
                        store32(v2 + 4, load32(v3 + 12))
                        v6 = (v6 + 2)
                        store32(9263840, (v6 + 2))
                        break
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v8):
                        continue
                    break
                break
        arg0 = load32(9213820)
        if load32(9213820):
            while True:  # $label42
                if arg1:
                    break
                arg1 = ((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES)
                v6 = load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 48)
                if not load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 48):
                    break
                store32(v9 + 64, load32((load32(arg1 + 44) + ((load32(9142848) % v6) << 2))))
                a_b()
                arg0 = load32(9213820)
                break
            break
        if load8u(9147336):
            a_b()
        while True:  # $label43
            while True:  # $label45
                while True:  # $label44
                    v3 = load32(9213808)
                    # br_table load32(9213808)
                    break
                    break
                while True:  # $label46
                    if arg1:
                        break
                    arg0 = ((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES)
                    arg1 = load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 48)
                    if not load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 48):
                        break
                    store32(v9 + 48, load32((load32(arg0 + 44) + ((load32(9142848) % arg1) << 2))))
                    a_b()
                    break
                break
                break
            v8 = load32(38528)
            v13 = load32(ENTITIES)
            arg1 = load32(load32(9215960))
            v4 = 0
            v6 = 0
            v5 = 0
            v7 = 0
            v11 = 0
            v2 = 0
            v12 = 0
            v10 = 0
            while True:  # $label47
                arg0 = (v13 + (load32(((v4 << 2) + 9173808)) * 132))
                v14 = load8u(arg0 + 122)
                v5 = ((0 if load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) else load32((v13 + (load32(((v4 << 2) + 9173808)) * 132)) + 84)) + v5)
                v11 = (load32(arg0 + 60) + v11)
                v2 = (load32(arg0 + 52) + v2)
                v12 = (load32(arg0 + 68) + v12)
                v10 = (load32(arg0 + 64) + v10)
                v7 = ((load32(arg0 + 80) if (v8 == v14) else 0) + v7)
                arg0 = load32(arg0 + 16)
                if load32(arg0 + 16):
                else:
                v6 = (0 + v6)
                v4 = (v4 + 1)
                if ((v4 + 1) != v3):
                    continue
                break
            func52(189, 0)
            arg0 = players[arg1]
            v3 = load32(players[arg1] + 284628)
            arg0 = load32(arg0 + 284616)
            store32(v9 + 20, v2)
            store32(v9 + 24, v11)
            store32(v9 + 28, v7)
            store32(v9 + 32, v5)
            store32(v9 + 36, v6)
            store32(v9 + 16, (arg0 if arg0 else v3))
            store32(v9, load32(9213808))
            store32(v9 + 4, v10)
            store32(v9 + 8, v12)
            store32(v9 + 12, arg1)
            a_b()
            break
            break
        if load8u(9147152):
            break
        func52((207 if load8u(9143020) else 0), 0)
        a_b()
        break
    G.global0 = (v9 + 80)
    return func57(0)

# ----------------------------------------------------------
# $func29
# ----------------------------------------------------------
def func29(arg0, arg1):
    while True:  # $label0
        if (load8u(arg0 + 125) == 3):
            break
        if (load8u(arg0 + 129) == 5):
            if func200(arg0, 0, 0, 1):
                break
        while True:  # $label1
            v3 = load32(arg0 + 20)
            if not load32(arg0 + 20):
                break
            if (u32(load32(v3 + 8)) < u32(3)):
                break
            v5 = load32(v3)
            v7 = load32(load32(v3))
            if (u32((load32(load32(v3)) - 1)) > u32(1)):
                break
            if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                break
            v2 = load32(v5 + 4)
            v6 = (v5 + (load32(v5 + 4) << 2))
            v4 = load32(arg0 + 32)
            while True:  # $label3
                while True:  # $label4
                    while True:  # $label5
                        while True:  # $label2
                            if not load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4):
                                if v4:
                                    break
                                if (load32(v6) != load16u(arg0 + 116)):
                                    break
                                if (load32(v6 + 4) == load16u(arg0 + 118)):
                                    break
                                break
                            if not v4:
                                break
                            break
                            break
                        if (v4 == load32(v6 + 8)):
                            break
                        break
                    if (v4 != load32(v6 + 8)):
                        break
                    break
                v2 = (v2 + 7)
                store32(v5 + 4, (v2 + 7))
                v8 = 1
                break
            while True:  # $label6
                if (v7 != 2):
                    break
                if (u32(v2) < u32(load32(v3 + 8))):
                    break
                v2 = 2
                store32(v5 + 4, 2)
                break
            if (u32(load32(v3 + 8)) <= u32(v2)):
                store32(v3 + 8, 0)
                break
            store8(arg0 + 125, 0)
            v4 = load32(ENTITIES)
            v2 = (v5 + (v2 << 2))
            v3 = load32((v5 + (v2 << 2)) + 8)
            if (load8u(entities[load32((v5 + (v2 << 2)) + 8)].unit_class) == 3):
                if (load32(v2 + 12) != 69):
                    break
                v3 = func236((v4 + (load32(arg0 + 28) * 132)), (v4 + (v3 * 132)))
                if not func236((v4 + (load32(arg0 + 28) * 132)), (v4 + (v3 * 132))):
                    break
                store32(v2 + 8, v3)
                if (load8u((v4 + (v3 * 132)) + 125) == 3):
                    break
            v5 = (5 if load32(v2 + 20) else 0)
            v4 = load32(v2 + 16)
            v7 = load32(v2 + 4)
            v9 = load32(v2)
            v10 = load32(v2 + 12)
            v2 = 250
            while True:  # $label7
                if not v8:
                    break
                if (load32(v6) != load16u(arg0 + 112)):
                    break
                v2 = (250 if (load32(v6 + 4) != load16u(arg0 + 114)) else 0)
                break
            if not func30(func86(arg0), arg0, v3, v10, v9, v7, v4, v5, v2, 0):
                break
            if (u32(load32((load32(9215884) + (load32(arg0 + 44) << 4)))) > u32(load32(9142848))):
                break
            break
        store8(arg0 + 125, 0)
        store8(arg0 + 123, 0)
        while True:  # $label8
            if not arg1:
                break
            arg1 = load32(arg0 + 48)
            if not load32(arg0 + 48):
                break
            if (load32(((load8u(arg0 + 122) * 72) + 9263856)) == arg1):
                if load32(arg1 + 32):
                    break
            break
        if load8u(9147152):
            break
        func156(func86(arg0), arg0, 500)
        break

# ----------------------------------------------------------
# $func30
# ----------------------------------------------------------
def func30(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, param9):
    v22 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v22 + 24, arg3)
    store32(v22 + 28, arg1)
    store32(v22 + 20, arg4)
    arg3 = 0
    while True:  # $label0
        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
            break
        arg1 = load8u(arg0 + 125)
        if ((load8u(arg0 + 125) & -2) == 12):
            break
        if (arg1 == 3):
            break
        arg1 = load32(((arg2 * 40) + 9671200) + 24)
        if load32(((arg2 * 40) + 9671200) + 24):
            if call_table(arg1):
                break
        if load32(arg0 + 36):
            if load32(arg0 + 36):
                break
        v14 = arg0
        arg0 = load32(v22 + 28)
        arg1 = 0
        v12 = (G.global0 - 32)
        G.global0 = (G.global0 - 32)
        while True:  # $label1
            if not arg0:
                break
            v30 = load32(PLAYERS)
            v27 = load16u(v14 + 110)
            v11 = players[load16u(v14 + 110)]
            if not load32(players[load16u(v14 + 110)] + 286684):
                break
            arg4 = load32(ENTITIES)
            v28 = entities[arg0]
            v9 = load8u(entities[arg0].sub_state)
            v13 = load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 264)
            if (load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 264) == 4):
                break
            v20 = load8u(v14 + 122)
            v10 = load32(((load8u(v14 + 122) * 404) + ENTITY_TYPES) + 264)
            if (load32(((load8u(v14 + 122) * 404) + ENTITY_TYPES) + 264) == 4):
                break
            v18 = load16u(v14 + 112)
            store32(v12 + 12, load16u(v14 + 112))
            v21 = load16u(v14 + 114)
            store32(v12 + 8, load16u(v14 + 114))
            while True:  # $label2
                if v10:
                    arg1 = ((v20 * 404) + ENTITY_TYPES)
                    v15 = load32(((v20 * 404) + ENTITY_TYPES) + 216)
                    if not load32(((v20 * 404) + ENTITY_TYPES) + 216):
                        v10 = 0
                        break
                    v10 = 0
                    v16 = load32(arg1 + 220)
                    if not load32(arg1 + 220):
                        break
                    arg1 = load32(9215880)
                    if not load32(9215880):
                        break
                    v19 = load32(9142432)
                    if not load32(9142432):
                        break
                    v24 = load32(9142440)
                    v17 = load32(arg1)
                    v20 = 0
                    while True:  # $label4
                        v23 = (v18 + v20)
                        arg1 = 0
                        while True:  # $label3
                            v10 = load32((v19 + ((v23 + ((arg1 + v21) * v24)) << 2)))
                            if not load32((v17 + (load32((v19 + ((v23 + ((arg1 + v21) * v24)) << 2))) << 2))):
                                break
                            arg1 = (arg1 + 1)
                            if ((arg1 + 1) != v16):
                                continue
                            break
                        v10 = 0
                        v20 = (v20 + 1)
                        if ((v20 + 1) != v15):
                            continue
                        break
                    break
                v10 = 0
                arg1 = load32(9142432)
                if not load32(9142432):
                    break
                v10 = load32((arg1 + (((load32(9142440) * v21) + v18) << 2)))
                break
            while True:  # $label7
                while True:  # $label5
                    while True:  # $label6
                        # br_table v13
                        break
                        break
                    arg1 = ((v9 * 404) + ENTITY_TYPES)
                    v13 = load32(((v9 * 404) + ENTITY_TYPES) + 216)
                    if not load32(((v9 * 404) + ENTITY_TYPES) + 216):
                        v20 = 0
                        break
                    v20 = 0
                    v15 = load32(arg1 + 220)
                    if not load32(arg1 + 220):
                        break
                    arg1 = load32(9215880)
                    if not load32(9215880):
                        break
                    v16 = load32(9142432)
                    if not load32(9142432):
                        break
                    arg0 = (arg4 + (arg0 * 132))
                    arg4 = load16u((arg4 + (arg0 * 132)) + 114)
                    arg0 = load16u(arg0 + 112)
                    v19 = load32(9142440)
                    v24 = load32(arg1)
                    v9 = 0
                    while True:  # $label9
                        v17 = (arg0 + v9)
                        arg1 = 0
                        while True:  # $label8
                            v20 = load32((v16 + ((v17 + ((arg1 + arg4) * v19)) << 2)))
                            if not load32((v24 + (load32((v16 + ((v17 + ((arg1 + arg4) * v19)) << 2))) << 2))):
                                break
                            arg1 = (arg1 + 1)
                            if ((arg1 + 1) != v15):
                                continue
                            break
                        v20 = 0
                        v9 = (v9 + 1)
                        if ((v9 + 1) != v13):
                            continue
                        break
                    break
                    break
                v20 = 0
                arg1 = load32(9142432)
                if not load32(9142432):
                    break
                arg0 = (arg4 + (arg0 * 132))
                v20 = load32((arg1 + (((load32(9142440) * load16u((arg4 + (arg0 * 132)) + 114)) + load16u(arg0 + 112)) << 2)))
                break
            arg1 = 0
            if (v10 == v20):
                break
            arg4 = 0
            store8(v14 + 129, 0)
            arg1 = 1
            arg0 = load32(9684440)
            if not load32(9684440):
                break
            v32 = load32(((load32((v30 + (v27 * 286704)) + 283960) << 2) + 58928))
            v9 = load32(9684436)
            while True:  # $label12
                while True:  # $label11
                    arg1 = (arg0 * arg4)
                    while True:  # $label10
                        if (arg4 != v10):
                            if not load8u((v9 + (arg1 + v10))):
                                break
                        if (arg4 == v20):
                            break
                        if load8u((v9 + (arg1 + v20))):
                            break
                        break
                    arg1 = 1
                    arg4 = (arg4 + 1)
                    if ((arg4 + 1) != arg0):
                        continue
                    break
                    break
                break
            arg1 = 1
            if not arg4:
                break
            arg0 = (v30 + (v27 * 286704))
            store32((v30 + (v27 * 286704)) + 283940, (load32(arg0 + 283940) + 1))
            while True:  # $label50
                while True:  # $label13
                    v24 = ((v32 * 404) + ENTITY_TYPES)
                    arg0 = load32(((v32 * 404) + ENTITY_TYPES) + 68)
                    if load32(((v32 * 404) + ENTITY_TYPES) + 68):
                        if (load32(v12 + 16) < arg0):
                            break
                    arg0 = load32(v24 + 72)
                    if load32(v24 + 72):
                        if (load32(v12 + 20) < arg0):
                            break
                    arg0 = load32(v24 + 76)
                    if load32(v24 + 76):
                        if (load32(v12 + 24) < arg0):
                            break
                    arg0 = load32(v24 + 80)
                    if load32(v24 + 80):
                        if (load32(v12 + 28) < arg0):
                            break
                    v9 = 0
                    v13 = 0
                    v19 = load32(ENTITIES)
                    while True:  # $label16
                        v23 = load32(9142432)
                        if load32(9142432):
                            v25 = load32(9142440)
                            v13 = 1
                            while True:  # $label20
                                while True:  # $label14
                                    arg1 = load32(((v9 << 2) + 58928))
                                    arg0 = load32(((v11 + (load32(((v9 << 2) + 58928)) << 2)) + 284636))
                                    if not load32(((v11 + (load32(((v9 << 2) + 58928)) << 2)) + 284636)):
                                        break
                                    v26 = load32(arg0 + 8)
                                    if not load32(arg0 + 8):
                                        break
                                    v17 = ((arg1 * 404) + ENTITY_TYPES)
                                    v29 = load32(arg0)
                                    v16 = 0
                                    while True:  # $label19
                                        while True:  # $label15
                                            arg0 = load32((v29 + (v16 << 2)))
                                            if not load32((v29 + (v16 << 2))):
                                                break
                                            arg0 = (v19 + (arg0 * 132))
                                            v15 = load16u((v19 + (arg0 * 132)) + 112)
                                            v31 = (load16u((v19 + (arg0 * 132)) + 112) + load32(v17 + 216))
                                            if ((load16u((v19 + (arg0 * 132)) + 112) + load32(v17 + 216)) <= v15):
                                                break
                                            arg1 = load16u(arg0 + 114)
                                            v33 = (load16u(arg0 + 114) + load32(v17 + 220))
                                            if ((load16u(arg0 + 114) + load32(v17 + 220)) <= arg1):
                                                break
                                            while True:  # $label18
                                                arg0 = arg1
                                                while True:  # $label17
                                                    if (load32((v23 + (((arg0 * v25) + v15) << 2))) == arg4):
                                                        break
                                                    arg0 = (arg0 + 1)
                                                    if ((arg0 + 1) != v33):
                                                        continue
                                                    break
                                                v15 = (v15 + 1)
                                                if ((v15 + 1) != v31):
                                                    continue
                                                break
                                            break
                                        v16 = (v16 + 1)
                                        if ((v16 + 1) != v26):
                                            continue
                                        break
                                    break
                                v9 = (v9 + 1)
                                v13 = (u32((v9 + 1)) < u32(3))
                                if (v9 != 3):
                                    continue
                                break
                            break
                        if arg4:
                            break
                        v13 = 1
                        while True:  # $label24
                            while True:  # $label21
                                arg1 = load32(((v9 << 2) + 58928))
                                arg0 = load32(((v11 + (load32(((v9 << 2) + 58928)) << 2)) + 284636))
                                if not load32(((v11 + (load32(((v9 << 2) + 58928)) << 2)) + 284636)):
                                    break
                                v15 = load32(arg0 + 8)
                                if not load32(arg0 + 8):
                                    break
                                arg1 = ((arg1 * 404) + ENTITY_TYPES)
                                v16 = load32(arg0)
                                arg0 = 0
                                while True:  # $label23
                                    while True:  # $label22
                                        v17 = load32((v16 + (arg0 << 2)))
                                        if not load32((v16 + (arg0 << 2))):
                                            break
                                        v17 = (v19 + (v17 * 132))
                                        v23 = load16u((v19 + (v17 * 132)) + 112)
                                        if ((load16u((v19 + (v17 * 132)) + 112) + load32(arg1 + 216)) <= v23):
                                            break
                                        v17 = load16u(v17 + 114)
                                        if ((load16u(v17 + 114) + load32(arg1 + 220)) > v17):
                                            break
                                        break
                                    arg0 = (arg0 + 1)
                                    if ((arg0 + 1) != v15):
                                        continue
                                    break
                                break
                            v9 = (v9 + 1)
                            v13 = (u32((v9 + 1)) < u32(3))
                            if (v9 != 3):
                                continue
                            break
                        break
                    if v13:
                        break
                    store32(v12 + 16, v18)
                    store32(v12 + 4, v21)
                    while True:  # $label25
                        v18 = load32(9142440)
                        if (u32(load32(9142440)) < u32(2)):
                            break
                        v17 = load32(v12 + 16)
                        v13 = (load32(v12 + 16) - 1)
                        v15 = load32(v12 + 4)
                        arg1 = (load32(v12 + 4) - 1)
                        v21 = (v17 + 2)
                        v16 = (v15 + 2)
                        v19 = 1
                        while True:  # $label39
                            while True:  # $label26
                                if (v13 >= v21):
                                    break
                                if (arg1 >= v16):
                                    break
                                v25 = (v21 - 1)
                                v26 = (v16 - 1)
                                v23 = 1
                                v9 = v13
                                while True:  # $label30
                                    v29 = load32(9142432)
                                    if not load32(9142432):
                                        while True:  # $label34
                                            while True:  # $label27
                                                if (u32(v9) >= u32(v18)):
                                                    break
                                                while True:  # $label28
                                                    if (v9 == v25):
                                                        break
                                                    arg0 = arg1
                                                    if (v9 == v13):
                                                        break
                                                    while True:  # $label31
                                                        while True:  # $label29
                                                            if ((arg0 != arg1) & (arg0 != v26)):
                                                                break
                                                            if (u32(arg0) >= u32(v18)):
                                                                break
                                                            if ((arg0 | v9) < 0):
                                                                break
                                                            if arg4:
                                                                break
                                                            break
                                                            break
                                                        arg0 = (arg0 + 1)
                                                        if ((arg0 + 1) != v16):
                                                            continue
                                                        break
                                                    break
                                                    break
                                                arg0 = arg1
                                                if arg4:
                                                    break
                                                while True:  # $label33
                                                    while True:  # $label32
                                                        if (u32(arg0) >= u32(v18)):
                                                            break
                                                        if ((arg0 | v9) < 0):
                                                            break
                                                        break
                                                        break
                                                    arg0 = (arg0 + 1)
                                                    if ((arg0 + 1) != v16):
                                                        continue
                                                    break
                                                break
                                            v9 = (v9 + 1)
                                            v23 = ((v9 + 1) < v21)
                                            if (v9 != v21):
                                                continue
                                            break
                                            break
                                        raise Unreachable()
                                    while True:  # $label38
                                        arg0 = arg1
                                        if (u32(v9) < u32(v18)):
                                            while True:  # $label37
                                                while True:  # $label36
                                                    while True:  # $label35
                                                        if (v9 == v13):
                                                            break
                                                        if (arg0 == arg1):
                                                            break
                                                        if (arg0 == v26):
                                                            break
                                                        if (v9 != v25):
                                                            break
                                                        break
                                                    if (u32(arg0) >= u32(v18)):
                                                        break
                                                    if ((arg0 | v9) < 0):
                                                        break
                                                    if (load32((v29 + (((arg0 * v18) + v9) << 2))) != arg4):
                                                        break
                                                    break
                                                    break
                                                arg0 = (arg0 + 1)
                                                if ((arg0 + 1) != v16):
                                                    continue
                                                break
                                        v9 = (v9 + 1)
                                        v23 = ((v9 + 1) < v21)
                                        if (v9 != v21):
                                            continue
                                        break
                                    break
                                    break
                                store32(v12 + 16, v9)
                                v15 = arg0
                                store32(v12 + 4, arg0)
                                if v23:
                                    break
                                v18 = load32(9142440)
                                v17 = load32(v12 + 16)
                                break
                            v19 = (v19 + 1)
                            arg1 = (v15 - (v19 + 1))
                            arg0 = ((v19 << 1) | 1)
                            v16 = ((v15 - (v19 + 1)) + ((v19 << 1) | 1))
                            v13 = (v17 - v19)
                            v21 = ((v17 - v19) + arg0)
                            if (u32(v18) > u32(v19)):
                                continue
                            break
                        break
                    v18 = load32(v12 + 16)
                    v21 = load32(v12 + 4)
                    v13 = 0
                    v15 = 0
                    v16 = load32(ENTITIES)
                    while True:  # $label44
                        v17 = load32(9142432)
                        if load32(9142432):
                            v23 = load32(9142440)
                            arg0 = 2147483647
                            while True:  # $label43
                                while True:  # $label40
                                    arg1 = load32(((v11 + (load32(((v13 << 2) + 58896)) << 2)) + 284636))
                                    if not load32(((v11 + (load32(((v13 << 2) + 58896)) << 2)) + 284636)):
                                        break
                                    v25 = load32(arg1 + 8)
                                    if not load32(arg1 + 8):
                                        break
                                    v26 = load32(arg1)
                                    v9 = 0
                                    while True:  # $label42
                                        while True:  # $label41
                                            arg1 = load32((v26 + (v9 << 2)))
                                            if not load32((v26 + (v9 << 2))):
                                                break
                                            v19 = (v16 + (arg1 * 132))
                                            v29 = load16u((v16 + (arg1 * 132)) + 114)
                                            arg1 = (v21 - load16u((v16 + (arg1 * 132)) + 114))
                                            v31 = load16u(v19 + 112)
                                            arg1 = (v18 - load16u(v19 + 112))
                                            arg1 = (((v21 - load16u((v16 + (arg1 * 132)) + 114)) * arg1) + ((v18 - load16u(v19 + 112)) * arg1))
                                            if ((((v21 - load16u((v16 + (arg1 * 132)) + 114)) * arg1) + ((v18 - load16u(v19 + 112)) * arg1)) >= arg0):
                                                break
                                            if (load32((v17 + (((v23 * v29) + v31) << 2))) != v10):
                                                break
                                            v15 = load32(v19 + 28)
                                            arg0 = arg1
                                            break
                                        v9 = (v9 + 1)
                                        if ((v9 + 1) != v25):
                                            continue
                                        break
                                    break
                                v13 = (v13 + 1)
                                if ((v13 + 1) != 3):
                                    continue
                                break
                            break
                        if v10:
                            break
                        arg0 = 2147483647
                        while True:  # $label48
                            while True:  # $label45
                                arg1 = load32(((v11 + (load32(((v13 << 2) + 58896)) << 2)) + 284636))
                                if not load32(((v11 + (load32(((v13 << 2) + 58896)) << 2)) + 284636)):
                                    break
                                v19 = load32(arg1 + 8)
                                if not load32(arg1 + 8):
                                    break
                                v17 = load32(arg1)
                                v9 = 0
                                while True:  # $label47
                                    while True:  # $label46
                                        arg1 = load32((v17 + (v9 << 2)))
                                        if not load32((v17 + (v9 << 2))):
                                            break
                                        v10 = (v16 + (arg1 * 132))
                                        arg1 = (v21 - load16u((v16 + (arg1 * 132)) + 114))
                                        arg1 = (v18 - load16u(v10 + 112))
                                        arg1 = (((v21 - load16u((v16 + (arg1 * 132)) + 114)) * arg1) + ((v18 - load16u(v10 + 112)) * arg1))
                                        if ((((v21 - load16u((v16 + (arg1 * 132)) + 114)) * arg1) + ((v18 - load16u(v10 + 112)) * arg1)) >= arg0):
                                            break
                                        v15 = load32(v10 + 28)
                                        arg0 = arg1
                                        break
                                    v9 = (v9 + 1)
                                    if ((v9 + 1) != v19):
                                        continue
                                    break
                                break
                            v13 = (v13 + 1)
                            if ((v13 + 1) != 3):
                                continue
                            break
                        break
                    v9 = v15
                    if not v15:
                        break
                    v10 = load32(9142440)
                    arg0 = 0
                    while True:  # $label51
                        while True:  # $label49
                            arg1 = arg0
                            v11 = (arg0 << 2)
                            arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v21)
                            if (u32(v10) <= u32((load32((((arg0 << 2) | 4) + 8611904)) + v21))):
                                break
                            v11 = (load32((v11 + 8611904)) + v18)
                            if (u32(v10) <= u32((load32((v11 + 8611904)) + v18))):
                                break
                            if ((arg0 | v11) < 0):
                                break
                            if func56(v11, arg0, v24, load16u(v14 + 110), 0, 0, 1, 1, 0):
                                break
                            v10 = load32(9142440)
                            break
                        arg0 = (arg1 + 2)
                        if (u32(arg1) < u32(718)):
                            continue
                        break
                    break
                v30 = (v30 + (v27 * 286704))
                v18 = 0
                while True:  # $label76
                    while True:  # $label52
                        arg0 = load32(((v30 + (load32(((v18 << 2) + 58940)) << 2)) + 284636))
                        if not load32(((v30 + (load32(((v18 << 2) + 58940)) << 2)) + 284636)):
                            break
                        v16 = load32(arg0 + 8)
                        if not load32(arg0 + 8):
                            break
                        arg1 = 0
                        v27 = load32(39216)
                        v17 = load32(PLAYERS)
                        v19 = load32(9215880)
                        v21 = load32(9142440)
                        v11 = load32(9142432)
                        v23 = load32(ENTITIES)
                        v32 = load32(arg0)
                        v24 = 1
                        while True:  # $label61
                            while True:  # $label62
                                while True:  # $label60
                                    while True:  # $label53
                                        arg0 = load32((v32 + (arg1 << 2)))
                                        if not load32((v32 + (arg1 << 2))):
                                            break
                                        while True:  # $label56
                                            while True:  # $label54
                                                while True:  # $label55
                                                    v13 = (v23 + (arg0 * 132))
                                                    v10 = ((load8u((v23 + (arg0 * 132)) + 122) * 404) + ENTITY_TYPES)
                                                    # br_table load32(((load8u((v23 + (arg0 * 132)) + 122) * 404) + ENTITY_TYPES) + 264)
                                                    break
                                                    break
                                                arg0 = 0
                                                v25 = load32(v10 + 216)
                                                if not load32(v10 + 216):
                                                    break
                                                v26 = load32(v10 + 220)
                                                if not load32(v10 + 220):
                                                    break
                                                if not v19:
                                                    break
                                                if not v11:
                                                    break
                                                v29 = load16u(v13 + 114)
                                                v31 = load16u(v13 + 112)
                                                v33 = load32(v19)
                                                v15 = 0
                                                while True:  # $label58
                                                    v34 = (v15 + v31)
                                                    v9 = 0
                                                    while True:  # $label57
                                                        arg0 = load32((v11 + ((v34 + ((v9 + v29) * v21)) << 2)))
                                                        if not load32((v33 + (load32((v11 + ((v34 + ((v9 + v29) * v21)) << 2))) << 2))):
                                                            break
                                                        v9 = (v9 + 1)
                                                        if ((v9 + 1) != v26):
                                                            continue
                                                        break
                                                    arg0 = 0
                                                    v15 = (v15 + 1)
                                                    if ((v15 + 1) != v25):
                                                        continue
                                                    break
                                                break
                                                break
                                            if not v11:
                                                arg0 = 0
                                                break
                                            arg0 = load32((v11 + ((load16u(v13 + 112) + (v21 * load16u(v13 + 114))) << 2)))
                                            break
                                        if (arg0 != arg4):
                                            break
                                        if (load8u(v13 + 123) == 38):
                                            break
                                        v25 = load32(v13 + 80)
                                        arg0 = load32(v10 + 136)
                                        # TODO: i32.div_u
                                        if (u32((load32(v10 + 136) * 150)) >= u32((100 if (load32((((v17 + (load16u(v13 + 110) * 286704)) + (v27 << 2)) + 281808)) == 1) else arg0))):
                                            break
                                        while True:  # $label59
                                            # br_table load8u(v13 + 129)
                                            break
                                            break
                                        arg0 = load32(v13 + 88)
                                        if not load32(v13 + 88):
                                            break
                                        if v11:
                                        else:
                                        if (0 == v20):
                                            break
                                        break
                                    arg1 = (arg1 + 1)
                                    v24 = (u32((arg1 + 1)) < u32(v16))
                                    if (arg1 != v16):
                                        continue
                                    break
                                    break
                                break
                            arg0 = 0
                            arg1 = 0
                            v15 = 0
                            while True:  # $label72
                                while True:  # $label66
                                    while True:  # $label65
                                        while True:  # $label63
                                            while True:  # $label64
                                                v11 = load8u(v28 + 122)
                                                v9 = ((load8u(v28 + 122) * 404) + ENTITY_TYPES)
                                                # br_table load32(((load8u(v28 + 122) * 404) + ENTITY_TYPES) + 264)
                                                break
                                                break
                                            v19 = load32(v9 + 216)
                                            if not load32(v9 + 216):
                                                break
                                            v16 = load32(9142432)
                                            v27 = load32(((v11 * 404) + ENTITY_TYPES) + 220)
                                            if not load32(((v11 * 404) + ENTITY_TYPES) + 220):
                                                break
                                            arg0 = load16u(v28 + 114)
                                            arg1 = load16u(v28 + 112)
                                            if not v16:
                                                break
                                            v17 = load32(9142440)
                                            v23 = load32(load32(9215880))
                                            while True:  # $label69
                                                v11 = (arg1 + v15)
                                                v10 = 0
                                                while True:  # $label68
                                                    while True:  # $label67
                                                        v9 = (arg0 + v10)
                                                        if load32((v23 + (load32((v16 + ((((arg0 + v10) * v17) + v11) << 2))) << 2))):
                                                            v10 = (v10 + 1)
                                                            if (v27 != (v10 + 1)):
                                                                continue
                                                            break
                                                        break
                                                    arg1 = v11
                                                    arg0 = v9
                                                    break
                                                    break
                                                v15 = (v15 + 1)
                                                if ((v15 + 1) != v19):
                                                    continue
                                                break
                                            break
                                            break
                                        arg0 = load16u(v28 + 114)
                                        arg1 = load16u(v28 + 112)
                                        break
                                    break
                                v16 = load32(9142432)
                                if load32(9142432):
                                    v9 = load32(v12 + 8)
                                    v15 = load32(v12 + 12)
                                    while True:  # $label71
                                        v10 = (arg0 - v9)
                                        while True:  # $label70
                                            v11 = (arg1 - v15)
                                            if not (arg1 - v15):
                                                break
                                            if (arg0 == v9):
                                                break
                                            v11 = (v10 // v11)
                                            v11 = (v11 >> 31)
                                            v11 = (v11 if (u32((((v10 // v11) ^ (v11 >> 31)) - v11)) <= u32(1)) else 0)
                                            v9 = ((v11 if (u32((((v10 // v11) ^ (v11 >> 31)) - v11)) <= u32(1)) else 0) // v10)
                                            v9 = (v9 >> 31)
                                            v10 = (v10 if (u32(((((v11 if (u32((((v10 // v11) ^ (v11 >> 31)) - v11)) <= u32(1)) else 0) // v10) ^ (v9 >> 31)) - v9)) <= u32(1)) else 0)
                                            break
                                        store32(v12 + 12, ((-1 if (v11 < 0) else (v11 != 0)) + v15))
                                        v9 = (load32(v12 + 8) + (-1 if (v10 < 0) else (v10 != 0)))
                                        store32(v12 + 8, (load32(v12 + 8) + (-1 if (v10 < 0) else (v10 != 0))))
                                        v15 = load32(v12 + 12)
                                        if (load32((v16 + ((load32(v12 + 12) + (load32(9142440) * v9)) << 2))) != v20):
                                            continue
                                        break
                                    break
                                if v20:
                                    v9 = load32(v12 + 8)
                                    while True:  # $label74
                                        v10 = (arg0 - v9)
                                        while True:  # $label73
                                            arg2 = load32(v12 + 12)
                                            v11 = (arg1 - load32(v12 + 12))
                                            if not (arg1 - load32(v12 + 12)):
                                                break
                                            if (arg0 == v9):
                                                break
                                            arg3 = (v10 // v11)
                                            arg3 = (arg3 >> 31)
                                            v11 = (v11 if (u32((((v10 // v11) ^ (arg3 >> 31)) - arg3)) <= u32(1)) else 0)
                                            arg3 = ((v11 if (u32((((v10 // v11) ^ (arg3 >> 31)) - arg3)) <= u32(1)) else 0) // v10)
                                            arg3 = (arg3 >> 31)
                                            v10 = (v10 if (u32(((((v11 if (u32((((v10 // v11) ^ (arg3 >> 31)) - arg3)) <= u32(1)) else 0) // v10) ^ (arg3 >> 31)) - arg3)) <= u32(1)) else 0)
                                            break
                                        store32(v12 + 12, ((-1 if (v11 < 0) else (v11 != 0)) + arg2))
                                        v9 = (load32(v12 + 8) + (-1 if (v10 < 0) else (v10 != 0)))
                                        store32(v12 + 8, (load32(v12 + 8) + (-1 if (v10 < 0) else (v10 != 0))))
                                        continue
                                        break
                                    raise Unreachable()
                                v9 = load32(v12 + 8)
                                v10 = (arg0 - load32(v12 + 8))
                                while True:  # $label75
                                    arg1 = load32(v12 + 12)
                                    v11 = (arg1 - load32(v12 + 12))
                                    if not (arg1 - load32(v12 + 12)):
                                        break
                                    if (arg0 == v9):
                                        break
                                    arg0 = (v10 // v11)
                                    arg0 = (arg0 >> 31)
                                    v11 = (v11 if (u32((((v10 // v11) ^ (arg0 >> 31)) - arg0)) <= u32(1)) else 0)
                                    arg0 = ((v11 if (u32((((v10 // v11) ^ (arg0 >> 31)) - arg0)) <= u32(1)) else 0) // v10)
                                    arg0 = (arg0 >> 31)
                                    v10 = (v10 if (u32(((((v11 if (u32((((v10 // v11) ^ (arg0 >> 31)) - arg0)) <= u32(1)) else 0) // v10) ^ (arg0 >> 31)) - arg0)) <= u32(1)) else 0)
                                    break
                                store32(v12 + 12, ((-1 if (v11 < 0) else (v11 != 0)) + arg1))
                                store32(v12 + 8, (load32(v12 + 8) + (-1 if (v10 < 0) else (v10 != 0))))
                                break
                            store32(v13 + 88, (load32(v12 + 12) + (v21 * load32(v12 + 8))))
                            break
                        store32(v13 + 80, (v25 + 1))
                        if not v24:
                            break
                        arg1 = 2
                        break
                        break
                    arg1 = 1
                    v18 = (v18 + 1)
                    if ((v18 + 1) != 3):
                        continue
                    break
                break
                break
            arg0 = (v9 * 132)
            func261(v32, v11, arg0, ((v9 * 132) + load32(ENTITIES)))
            if load32(load32(GAME_STATE) + 156):
                func29((load32(ENTITIES) + arg0), 1)
            arg1 = 1
            break
        G.global0 = (v12 + 32)
        while True:  # $label77
            while True:  # $label78
                # br_table arg1
                break
                break
            if not load32(v14 + 44):
                break
            arg0 = load32(v14 + 20)
            if load32(v14 + 20):
                store32(arg0 + 8, 0)
            func92(v14, 0.0, 0.0)
            func29(v14, 1)
            break
            break
        arg0 = load32(((load32((load32(9215884) + (load32(v14 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if load32(((load32((load32(9215884) + (load32(v14 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        while True:  # $label79
            if (arg2 != 6):
                break
            if not arg8:
                break
            v11 = load32(9215884)
            v9 = load32(v14 + 44)
            if (load32((load32(9215884) + (load32(v14 + 44) << 4)) + 4) != 6):
                break
            arg4 = load32(v14 + 28)
            arg1 = 0
            while True:  # $label80
                v20 = load32(ENTITIES)
                v10 = load32(v22 + 28)
                arg0 = entities[load32(v22 + 28)]
                arg3 = load32(((load8u(entities[load32(v22 + 28)].sub_state) * 404) + ENTITY_TYPES) + 216)
                if not load32(((load8u(entities[load32(v22 + 28)].sub_state) * 404) + ENTITY_TYPES) + 216):
                    break
                v13 = load16u(arg0 + 114)
                arg1 = (v20 + (arg4 * 132))
                v20 = load16u((v20 + (arg4 * 132)) + 114)
                v15 = load16u(arg0 + 112)
                v28 = load16u(arg1 + 112)
                arg0 = load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 224)
                v12 = (load32(((load8u(arg1 + 122) * 404) + ENTITY_TYPES) + 224) * arg0)
                arg0 = 0
                arg1 = 1
                while True:  # $label82
                    arg4 = (v20 - (arg0 + v13))
                    v18 = (((v20 - (arg0 + v13)) * arg4) - 1)
                    arg4 = 0
                    while True:  # $label81
                        v21 = (v28 - (arg4 + v15))
                        if ((v18 + ((v28 - (arg4 + v15)) * v21)) <= v12):
                            break
                        arg4 = (arg4 + 1)
                        if ((arg4 + 1) != arg3):
                            continue
                        break
                    arg0 = (arg0 + 1)
                    arg1 = (u32((arg0 + 1)) < u32(arg3))
                    if (arg0 != arg3):
                        continue
                    break
                break
            if not arg1:
                break
            if (arg6 != -1):
                store8(v14 + 129, arg6)
            store32((v11 + ((v9 << 4) | 12)), v10)
            arg3 = 0
            break
            break
        while True:  # $label83
            if (load8u(v14 + 127) != 1):
                break
            store8(v14 + 127, 0)
            arg0 = load32(v14 + 40)
            if not load32(v14 + 40):
                break
            if not load8u(9142916):
                break
            store32(v22 + 4, arg0)
            store32(v22, 0)
            a_b()
            break
        while True:  # $label84
            if (arg6 == -1):
                break
            if (load8u(v14 + 129) == arg6):
                break
            store8(v14 + 129, arg6)
            break
        arg1 = 1
        store8(v14 + 123, arg2)
        store32(v14 + 56, 0)
        store32(v14 + 96, arg5)
        while True:  # $label85
            arg0 = load32(v22 + 28)
            if (u32(load32(v22 + 28)) >= u32(3)):
                arg2 = load32(v14 + 32)
                store32(v14 + 32, arg0)
                arg1 = (arg1 | ((arg6 == 9) & (arg0 != arg2)))
                break
            store16(v14 + 116, load32(v22 + 24))
            arg0 = load32(v22 + 20)
            store32(v14 + 32, 0)
            store16(v14 + 118, arg0)
            break
        arg3 = 1
        if (load8u(v14 + 125) == 1):
            break
        while True:  # $label86
            if not arg8:
                break
            if (load32((load32(9215884) + (load32(v14 + 44) << 4)) + 4) != 6):
                break
            arg0 = load8u(v14 + 129)
            if (load8u(v14 + 129) == 5):
                break
            if not (arg1 | (arg0 != 9)):
                break
            break
        store8(v14 + 125, 1)
        func63(v22, v14, 0, 1, arg7)
        break
    G.global0 = (v22 + 32)
    return arg3

# ----------------------------------------------------------
# $Ua
# Export: Ua
# ----------------------------------------------------------
def Ua(arg0, arg1, arg2, arg3):
    """Export: Ua"""
    v6 = load32(9142848)
    # TODO: i32.div_u
    v8 = (arg0 + 25)
    v4 = load32(9215892)
    while True:  # $label1
        while True:  # $label0
            if (u32(arg0) < u32(25)):
                break
            if (u32(v4) < u32(5)):
                break
            v7 = load32(9215884)
            arg0 = 4
            while True:  # $label2
                v5 = (v7 + (arg0 << 2))
                if (u32(load32((v7 + (arg0 << 2)))) < u32(v6)):
                    break
                arg0 = (arg0 + 4)
                if (u32((arg0 + 4)) < u32(v4)):
                    continue
                break
            break
        while True:  # $label3
            if (load32(9215888) != v4):
                v5 = load32(9215884)
                break
            arg0 = (load32(9215896) + v4)
            store32(9215888, (load32(9215896) + v4))
            v6 = load32(9215884)
            v5 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if v4:
                # TODO: memory.copy
            if v6:
                v4 = load32(9215892)
            store32(9215884, v5)
            break
        store32(9215892, (v4 + 1))
        store32((v5 + (v4 << 2)), v8)
        while True:  # $label4
            arg0 = load32(9215892)
            if (load32(9215892) != load32(9215888)):
                v4 = v5
                break
            v4 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v4 = func26((-1 if (u32(v4) > u32(1073741823)) else (v4 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(9215884, v4)
            arg0 = load32(9215892)
            break
        store32(9215892, (arg0 + 1))
        store32((v4 + (arg0 << 2)), arg1)
        while True:  # $label5
            arg0 = load32(9215892)
            if (load32(9215892) != load32(9215888)):
                v5 = v4
                break
            arg1 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v5 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(9215884, v5)
            arg0 = load32(9215892)
            break
        store32(9215892, (arg0 + 1))
        store32((v5 + (arg0 << 2)), arg2)
        while True:  # $label6
            arg0 = load32(9215892)
            if (load32(9215892) != load32(9215888)):
                v4 = v5
                break
            arg1 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v4 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(9215884, v4)
            arg0 = load32(9215892)
            break
        store32(9215892, (arg0 + 1))
        store32((v4 + (arg0 << 2)), arg3)
        return (load32(9215892) - 4)
        break
    store32(v5, v8)
    v5 = (arg0 << 2)
    store32((v7 + ((arg0 << 2) | 4)), arg1)
    store32((v7 + (v5 | 8)), arg2)
    store32((v7 + (v5 | 12)), arg3)
    return arg0