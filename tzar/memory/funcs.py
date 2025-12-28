"""
Tzar Game Engine - Memory functions.
Auto-generated from WAT.
"""
from tzar.runtime import (
    G, M, load32, load64, load8u, load8s, load16u, load16s, load32u,
    loadf32, loadf64, store32, store64, store8, store16, storef32, storef64,
    atomic_load, atomic_store, i32, i64, u, u64,
    rotl, rotr, clz, ctz, popcnt, f32, sqrt, ceil, floor, trunc,
    mem_size, mem_grow, mem_copy, mem_fill, indirect_call,
)


# ------------------------------------------------------------
# $func26
# ------------------------------------------------------------
def func26(arg0):
    arg0 = (1 if (u(arg0) <= u(1)) else arg0)
    while True:  # block $label0
        while True:  # $label1
            v1 = e()
            if e():
                break
            v1 = atomic_load(9690984)
            if atomic_load(9690984):
                # call_indirect[v1]
                continue
            break
        a_g()
        raise RuntimeError('unreachable')
        break
    return v1

# ------------------------------------------------------------
# $af
# Export: af
# ------------------------------------------------------------
def af(arg0):
    """Exported as af."""
    while True:  # block $label0
        if (arg0 == 0):
            break
        if (load8u(9690908) & 2):
            if func55(9690912):
                break
        v2 = (arg0 - 8)
        v1 = load32((arg0 - 4))
        arg0 = (load32((arg0 - 4)) & -8)
        v5 = ((arg0 - 8) + (load32((arg0 - 4)) & -8))
        while True:  # block $label2
            while True:  # block $label1
                if (v1 & 1):
                    break
                if ((v1 & 3) == 0):
                    break
                v1 = load32(v2)
                v2 = (v2 - load32(v2))
                if (u((v2 - load32(v2))) < u(load32(9690480))):
                    break
                arg0 = (arg0 + v1)
                if (load32(9690484) != v2):
                    if (u(v1) <= u(255)):
                        v4 = ((v1 & 0xFFFFFFFF) >> 3)
                        v1 = load32(v2 + 12)
                        v3 = load32(v2 + 8)
                        if (load32(v2 + 12) == load32(v2 + 8)):
                            store32(9690464, (load32(9690464) & rotl(-2, v4, 32)))
                            break
                        store32(v3 + 12, v1)
                        store32(v1 + 8, v3)
                        break
                    v6 = load32(v2 + 24)
                    while True:  # block $label3
                        v1 = load32(v2 + 12)
                        if (v2 != load32(v2 + 12)):
                            v3 = load32(v2 + 8)
                            store32(load32(v2 + 8) + 12, v1)
                            store32(v1 + 8, v3)
                            break
                        while True:  # block $label4
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
                    if (v6 == 0):
                        break
                    while True:  # block $label6
                        v3 = load32(v2 + 28)
                        v4 = ((load32(v2 + 28) << 2) + 9690768)
                        if (load32(((load32(v2 + 28) << 2) + 9690768)) == v2):
                            store32(v4, v1)
                            if v1:
                                break
                            store32(9690468, (load32(9690468) & rotl(-2, v3, 32)))
                            break
                        store32((v6 + (16 if (load32(v6 + 16) == v2) else 20)), v1)
                        if (v1 == 0):
                            break
                        break
                    store32(v1 + 24, v6)
                    v3 = load32(v2 + 16)
                    if load32(v2 + 16):
                        store32(v1 + 16, v3)
                        store32(v3 + 24, v1)
                    v3 = load32(v2 + 20)
                    if (load32(v2 + 20) == 0):
                        break
                    store32(v1 + 20, v3)
                    store32(v3 + 24, v1)
                    break
                v1 = load32(v5 + 4)
                if ((load32(v5 + 4) & 3) != 3):
                    break
                store32(9690472, arg0)
                store32(v5 + 4, (v1 & -2))
                store32(v2 + 4, (arg0 | 1))
                store32((arg0 + v2), arg0)
                break
                break
            if (u(v2) >= u(v5)):
                break
            v1 = load32(v5 + 4)
            if ((load32(v5 + 4) & 1) == 0):
                break
            while True:  # block $label12
                if ((v1 & 2) == 0):
                    if (load32(9690488) == v5):
                        store32(9690488, v2)
                        arg0 = (load32(9690476) + arg0)
                        store32(9690476, (load32(9690476) + arg0))
                        store32(v2 + 4, (arg0 | 1))
                        if (v2 != load32(9690484)):
                            break
                        store32(9690472, 0)
                        store32(9690484, 0)
                        break
                    if (load32(9690484) == v5):
                        store32(9690484, v2)
                        arg0 = (load32(9690472) + arg0)
                        store32(9690472, (load32(9690472) + arg0))
                        store32(v2 + 4, (arg0 | 1))
                        store32((arg0 + v2), arg0)
                        break
                    arg0 = ((v1 & -8) + arg0)
                    while True:  # block $label7
                        if (u(v1) <= u(255)):
                            v4 = ((v1 & 0xFFFFFFFF) >> 3)
                            v1 = load32(v5 + 12)
                            v3 = load32(v5 + 8)
                            if (load32(v5 + 12) == load32(v5 + 8)):
                                store32(9690464, (load32(9690464) & rotl(-2, v4, 32)))
                                break
                            store32(v3 + 12, v1)
                            store32(v1 + 8, v3)
                            break
                        v6 = load32(v5 + 24)
                        while True:  # block $label8
                            v1 = load32(v5 + 12)
                            if (v5 != load32(v5 + 12)):
                                v3 = load32(v5 + 8)
                                store32(load32(v5 + 8) + 12, v1)
                                store32(v1 + 8, v3)
                                break
                            while True:  # block $label9
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
                        if (v6 == 0):
                            break
                        while True:  # block $label11
                            v3 = load32(v5 + 28)
                            v4 = ((load32(v5 + 28) << 2) + 9690768)
                            if (load32(((load32(v5 + 28) << 2) + 9690768)) == v5):
                                store32(v4, v1)
                                if v1:
                                    break
                                store32(9690468, (load32(9690468) & rotl(-2, v3, 32)))
                                break
                            store32((v6 + (16 if (load32(v6 + 16) == v5) else 20)), v1)
                            if (v1 == 0):
                                break
                            break
                        store32(v1 + 24, v6)
                        v3 = load32(v5 + 16)
                        if load32(v5 + 16):
                            store32(v1 + 16, v3)
                            store32(v3 + 24, v1)
                        v3 = load32(v5 + 20)
                        if (load32(v5 + 20) == 0):
                            break
                        store32(v1 + 20, v3)
                        store32(v3 + 24, v1)
                        break
                    store32(v2 + 4, (arg0 | 1))
                    store32((arg0 + v2), arg0)
                    if (v2 != load32(9690484)):
                        break
                    store32(9690472, arg0)
                    break
                store32(v5 + 4, (v1 & -2))
                store32(v2 + 4, (arg0 | 1))
                store32((arg0 + v2), arg0)
                break
            if (u(arg0) <= u(255)):
                v1 = ((arg0 & -8) + 9690504)
                while True:  # block $label13
                    v3 = load32(9690464)
                    arg0 = (1 << ((arg0 & 0xFFFFFFFF) >> 3))
                    if ((load32(9690464) & (1 << ((arg0 & 0xFFFFFFFF) >> 3))) == 0):
                        store32(9690464, (arg0 | v3))
                        break
                    break
                arg0 = load32(v1 + 8)
                store32(v1 + 8, v2)
                store32(arg0 + 12, v2)
                store32(v2 + 12, v1)
                store32(v2 + 8, arg0)
                break
            v3 = 31
            if (u(arg0) <= u(16777215)):
                v1 = clz(((arg0 & 0xFFFFFFFF) >> 8))
                v3 = (((((arg0 & 0xFFFFFFFF) >> (38 - clz(((arg0 & 0xFFFFFFFF) >> 8)))) & 1) - (v1 << 1)) + 62)
            store32(v2 + 28, v3)
            store64(v2 + 16, 0)
            v1 = ((v3 << 2) + 9690768)
            while True:  # block $label17
                while True:  # block $label15
                    while True:  # block $label14
                        v4 = load32(9690468)
                        v7 = (1 << v3)
                        if ((load32(9690468) & (1 << v3)) == 0):
                            store32(9690468, (v4 | v7))
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
            arg0 = (load32(9690496) - 1)
            store32(9690496, ((load32(9690496) - 1) if arg0 else -1))
            break
        if ((load8u(9690908) & 2) == 0):
            break
        func54(9690912)
        break
    return v1

# ------------------------------------------------------------
# $func28
# ------------------------------------------------------------
def func28(arg0, arg1):
    v9 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # block $label0
        if load8u(9147152):
            break
        if (load32(40600) == 0):
            break
        if (arg0 == 0):
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
            # TODO: memory.fill []
            store32(9215968, 0)
            arg0 = load32(9213808)
            store8(59186, (load32(9213808) != 0))
            while True:  # block $label2
                if (arg0 == 0):
                    store32(9263840, 0)
                    break
                v23 = load32(9671128)
                while True:  # $label39
                    v8 = (v23 + (load32(((v24 << 2) + 9173808)) * 132))
                    v6 = load16u((v23 + (load32(((v24 << 2) + 9173808)) * 132)) + 110)
                    while True:  # block $label5
                        while True:  # block $label3
                            if (v10 == 0):
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
                        while True:  # block $label6
                            if (load32(9215964) != v10):
                                arg0 = load32(9215960)
                                break
                            arg0 = (load32(9215972) + v10)
                            store32(9215964, (load32(9215972) + v10))
                            v3 = load32(9215960)
                            arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                            if v10:
                                # TODO: memory.copy []
                            if v3:
                                v23 = load32(9671128)
                                v10 = load32(9215968)
                            store32(9215960, arg0)
                            break
                        v3 = load16u(v8 + 110)
                        store32(9215968, (v10 + 1))
                        store32((arg0 + (v10 << 2)), v6)
                        v10 = load32(9215968)
                        break
                    while True:  # block $label7
                        v25 = load8u(v8 + 125)
                        if (u(((load8u(v8 + 125) - 9) & 255)) < u(3)):
                            break
                        v2 = load8u(v8 + 122)
                        v14 = ((load8u(v8 + 122) * 404) + 9568096)
                        if (load8u(((load8u(v8 + 122) * 404) + 9568096) + 353) == 0):
                            store8(59186, 0)
                        v15 = load32(9561692)
                        while True:  # block $label9
                            while True:  # block $label8
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
                            if (load32(v8 + 24) == 0):
                                break
                            v4 = load32(arg0)
                            if (load32(arg0) == 0):
                                break
                            arg0 = load32(v4)
                            if (load32(v4) == 0):
                                break
                            v13 = load32(v4 + 8)
                            v6 = arg0
                            break
                        while True:  # block $label10
                            v12 = load32(v8 + 20)
                            if (load32(v8 + 20) == 0):
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
                                    while True:  # block $label11
                                        if (v7 == 0):
                                            break
                                        if (load8u(v5 + 23) == 0):
                                            break
                                        v11 = load32(v7 + 8)
                                        if (load32(v7 + 8) == 0):
                                            break
                                        v16 = ((((v11 - 1) & 0xFFFFFFFF) >> 1) + 1)
                                        v19 = (((((v11 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                                        v18 = load32(v8 + 28)
                                        v4 = load32(v7)
                                        arg0 = 0
                                        if (u(v11) >= u(3)):
                                            v20 = (v16 & -2)
                                            v11 = 0
                                            while True:  # $label14
                                                while True:  # block $label12
                                                    v16 = (arg0 << 2)
                                                    if (load32((v4 + (arg0 << 2))) != v18):
                                                        break
                                                    if (load32((v4 + (v16 | 4))) != v17):
                                                        break
                                                    store32(v5 + 128, 2147483647)
                                                    break
                                                while True:  # block $label13
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
                                        if (v19 == 0):
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
                                    while True:  # block $label17
                                        while True:  # block $label16
                                            v5 = load32((v11 + (v7 << 2)))
                                            if (u(load32((v11 + (v7 << 2)))) >= u(2147483647)):
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
                                            while True:  # block $label18
                                                v2 = ((load32((v6 + (arg0 << 2))) * 132) + 9216080)
                                                if (load8u(((load32((v6 + (arg0 << 2))) * 132) + 9216080) + 23) == 0):
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
                                    if (u(v7) < u(load32(v12 + 8))):
                                        continue
                                    break
                            v2 = load32((v15 + (v3 * 286704)) + 281796)
                            if (load32((v15 + (v3 * 286704)) + 281796) == 0):
                                break
                            if (load8u(v8 + 125) == 14):
                                break
                            v4 = load32(v2 + 8)
                            if (load32(v2 + 8) == 0):
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
                                if (u((arg0 + 2)) < u(v4)):
                                    continue
                                break
                            break
                        if (v13 == 0):
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
                            while True:  # block $label22
                                while True:  # block $label23
                                    arg0 = load32((v6 + (v12 << 2)))
                                    if (load32((v6 + (v12 << 2))) <= 317):
                                        while True:  # block $label24
                                            # br_table[(arg0 - 186)]
                                            break
                                            break
                                        if (arg0 != 4):
                                            break
                                        break
                                    if (arg0 != 318):
                                        if (arg0 != 350):
                                            break
                                        arg0 = 350
                                        if (u(load32(v8 + 84)) >= u(3)):
                                            break
                                        break
                                    arg0 = (323 if load32(v20) else 318)
                                    break
                                while True:  # block $label25
                                    v3 = ((arg0 * 132) + 9216080)
                                    v26 = load32(((arg0 * 132) + 9216080) + 12)
                                    if (load32(((arg0 * 132) + 9216080) + 12) != 85):
                                        break
                                    if (load32(v17) != 1):
                                        break
                                    store32(v16, load32(v19))
                                    break
                                while True:  # block $label26
                                    v2 = load8u(v3 + 23)
                                    if load8u(v3 + 23):
                                        arg0 = load32(v3 + 4)
                                        if (load32(((load32(v3 + 4) * 404) + 9568096) + 264) != 3):
                                            break
                                        arg0 = (v4 + (arg0 << 2))
                                        if load32(((v4 + (arg0 << 2)) + 281808)):
                                            store32(v3 + 124, 1)
                                        if (load32((arg0 + 282828)) == 0):
                                            break
                                        store32(v3 + 124, 2)
                                        break
                                    while True:  # block $label27
                                        # br_table[(v25 - 4)]
                                        break
                                        break
                                    store8(v3 + 22, 1)
                                    store32(v3 + 124, 3)
                                    break
                                v27 = (load32(v3 + 16) + 1)
                                store32(v3 + 16, (load32(v3 + 16) + 1))
                                arg0 = 0
                                while True:  # block $label28
                                    v5 = load32(v8 + 24)
                                    if (load32(v8 + 24) == 0):
                                        break
                                    v5 = load32(v5)
                                    if (load32(v5) == 0):
                                        break
                                    if (load32(v5) == 0):
                                        break
                                    arg0 = (u(v12) >= u(load32(v14 + 236)))
                                    break
                                store8(v3 + 21, arg0)
                                while True:  # block $label29
                                    if (v7 != 1):
                                        break
                                    v11 = load32(v8 + 20)
                                    if (load32(v8 + 20) == 0):
                                        break
                                    if (v2 == 0):
                                        break
                                    if (load32(v14 + 264) != 1):
                                        break
                                    while True:  # block $label30
                                        # br_table[load32(((load32(v3 + 4) * 404) + 9568096) + 264)]
                                        break
                                        break
                                    store8(v3 + 21, 1)
                                    v28 = load32(v3 + 68)
                                    if (load32(v3 + 68) == 0):
                                        break
                                    v2 = 0
                                    while True:  # $label35
                                        while True:  # block $label32
                                            while True:  # block $label31
                                                v15 = load32((v3 + (v2 << 2)) + 28)
                                                if (load32(((load32((v3 + (v2 << 2)) + 28) * 404) + 9568096) + 264) != 3):
                                                    break
                                                v21 = load32(v11 + 8)
                                                if load32(v11 + 8):
                                                    v22 = load32(v11)
                                                    v5 = 0
                                                    while True:  # $label33
                                                        arg0 = load32((v22 + (v5 << 2)))
                                                        if (((load32((v22 + (v5 << 2))) - 2147483647) if (u(arg0) > u(2147483646)) else arg0) == v15):
                                                            break
                                                        v5 = (v5 + 1)
                                                        if ((v5 + 1) != v21):
                                                            continue
                                                        break
                                                arg0 = load32(v18)
                                                if (load32(v18) == 0):
                                                    break
                                                v21 = load32(arg0 + 8)
                                                if (load32(arg0 + 8) == 0):
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
                                                    if (u((arg0 + 2)) < u(v21)):
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
                                while True:  # block $label36
                                    v2 = load32(v14 + 164)
                                    if (u(load32(v14 + 164)) < u(2)):
                                        break
                                    v5 = load32(v14 + 160)
                                    arg0 = 1
                                    while True:  # $label37
                                        v11 = (v5 + (arg0 << 2))
                                        if (v26 != load32((v5 + (arg0 << 2)))):
                                            arg0 = (arg0 + 2)
                                            if (u((arg0 + 2)) < u(v2)):
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
                    if (u((v24 + 1)) < u(load32(9213808))):
                        continue
                    break
                arg0 = 0
                store32(9263840, 0)
                v8 = load32(9671120)
                if (load32(9671120) == 0):
                    break
                v6 = 0
                while True:  # $label41
                    while True:  # block $label40
                        v3 = load32(((arg0 << 2) + 9263072))
                        if (load32(((arg0 << 2) + 9263072)) == 0):
                            break
                        v10 = load32(v3 + 116)
                        if (u(load32(v3 + 116)) < u(2)):
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
            while True:  # block $label42
                if arg1:
                    break
                arg1 = ((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096)
                v6 = load32(((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096) + 48)
                if (load32(((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096) + 48) == 0):
                    break
                store32(v9 + 64, load32((load32(arg1 + 44) + ((load32(9142848) % v6) << 2))))
                a_b()
                arg0 = load32(9213820)
                break
            break
        if load8u(9147336):
            a_b()
        while True:  # block $label43
            while True:  # block $label45
                while True:  # block $label44
                    v3 = load32(9213808)
                    # br_table[load32(9213808)]
                    break
                    break
                while True:  # block $label46
                    if arg1:
                        break
                    arg0 = ((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096)
                    arg1 = load32(((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096) + 48)
                    if (load32(((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096) + 48) == 0):
                        break
                    store32(v9 + 48, load32((load32(arg0 + 44) + ((load32(9142848) % arg1) << 2))))
                    a_b()
                    break
                break
                break
            v8 = load32(38528)
            v13 = load32(9671128)
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
                v5 = ((0 if load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) else load32((v13 + (load32(((v4 << 2) + 9173808)) * 132)) + 84)) + v5)
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
            arg0 = (load32(9561692) + (arg1 * 286704))
            v3 = load32((load32(9561692) + (arg1 * 286704)) + 284628)
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

# ------------------------------------------------------------
# $func29
# ------------------------------------------------------------
def func29(arg0, arg1):
    while True:  # block $label0
        if (load8u(arg0 + 125) == 3):
            break
        if (load8u(arg0 + 129) == 5):
            if func200(arg0, 0, 0, 1):
                break
        while True:  # block $label1
            v3 = load32(arg0 + 20)
            if (load32(arg0 + 20) == 0):
                break
            if (u(load32(v3 + 8)) < u(3)):
                break
            v5 = load32(v3)
            v7 = load32(load32(v3))
            if (u((load32(load32(v3)) - 1)) > u(1)):
                break
            if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) == 1):
                break
            v2 = load32(v5 + 4)
            v6 = (v5 + (load32(v5 + 4) << 2))
            v4 = load32(arg0 + 32)
            while True:  # block $label3
                while True:  # block $label4
                    while True:  # block $label5
                        while True:  # block $label2
                            if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 0):
                                if v4:
                                    break
                                if (load32(v6) != load16u(arg0 + 116)):
                                    break
                                if (load32(v6 + 4) == load16u(arg0 + 118)):
                                    break
                                break
                            if (v4 == 0):
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
            while True:  # block $label6
                if (v7 != 2):
                    break
                if (u(v2) < u(load32(v3 + 8))):
                    break
                v2 = 2
                store32(v5 + 4, 2)
                break
            if (u(load32(v3 + 8)) <= u(v2)):
                store32(v3 + 8, 0)
                break
            store8(arg0 + 125, 0)
            v4 = load32(9671128)
            v2 = (v5 + (v2 << 2))
            v3 = load32((v5 + (v2 << 2)) + 8)
            if (load8u((load32(9671128) + (load32((v5 + (v2 << 2)) + 8) * 132)) + 125) == 3):
                if (load32(v2 + 12) != 69):
                    break
                v3 = func236((v4 + (load32(arg0 + 28) * 132)), (v4 + (v3 * 132)))
                if (func236((v4 + (load32(arg0 + 28) * 132)), (v4 + (v3 * 132))) == 0):
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
            while True:  # block $label7
                if (v8 == 0):
                    break
                if (load32(v6) != load16u(arg0 + 112)):
                    break
                v2 = (250 if (load32(v6 + 4) != load16u(arg0 + 114)) else 0)
                break
            if (func30(func86(arg0), arg0, v3, v10, v9, v7, v4, v5, v2, 0) == 0):
                break
            if (u(load32((load32(9215884) + (load32(arg0 + 44) << 4)))) > u(load32(9142848))):
                break
            break
        store8(arg0 + 125, 0)
        store8(arg0 + 123, 0)
        while True:  # block $label8
            if (arg1 == 0):
                break
            arg1 = load32(arg0 + 48)
            if (load32(arg0 + 48) == 0):
                break
            if (load32(((load8u(arg0 + 122) * 72) + 9263856)) == arg1):
                if load32(arg1 + 32):
                    break
            break
        if load8u(9147152):
            break
        func156(func86(arg0), arg0, 500)
        break

# ------------------------------------------------------------
# $Ua
# Export: Ua
# ------------------------------------------------------------
def Ua(arg0, arg1, arg2, arg3):
    """Exported as Ua."""
    v6 = load32(9142848)
    # TODO: i32.div_u []
    v8 = (arg0 + 25)
    v4 = load32(9215892)
    while True:  # block $label1
        while True:  # block $label0
            if (u(arg0) < u(25)):
                break
            if (u(v4) < u(5)):
                break
            v7 = load32(9215884)
            arg0 = 4
            while True:  # $label2
                v5 = (v7 + (arg0 << 2))
                if (u(load32((v7 + (arg0 << 2)))) < u(v6)):
                    break
                arg0 = (arg0 + 4)
                if (u((arg0 + 4)) < u(v4)):
                    continue
                break
            break
        while True:  # block $label3
            if (load32(9215888) != v4):
                v5 = load32(9215884)
                break
            arg0 = (load32(9215896) + v4)
            store32(9215888, (load32(9215896) + v4))
            v6 = load32(9215884)
            v5 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if v4:
                # TODO: memory.copy []
            if v6:
                v4 = load32(9215892)
            store32(9215884, v5)
            break
        store32(9215892, (v4 + 1))
        store32((v5 + (v4 << 2)), v8)
        while True:  # block $label4
            arg0 = load32(9215892)
            if (load32(9215892) != load32(9215888)):
                v4 = v5
                break
            v4 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v4 = func26((-1 if (u(v4) > u(1073741823)) else (v4 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(9215884, v4)
            arg0 = load32(9215892)
            break
        store32(9215892, (arg0 + 1))
        store32((v4 + (arg0 << 2)), arg1)
        while True:  # block $label5
            arg0 = load32(9215892)
            if (load32(9215892) != load32(9215888)):
                v5 = v4
                break
            arg1 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v5 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(9215884, v5)
            arg0 = load32(9215892)
            break
        store32(9215892, (arg0 + 1))
        store32((v5 + (arg0 << 2)), arg2)
        while True:  # block $label6
            arg0 = load32(9215892)
            if (load32(9215892) != load32(9215888)):
                v4 = v5
                break
            arg1 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v4 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
            if arg0:
                # TODO: memory.copy []
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