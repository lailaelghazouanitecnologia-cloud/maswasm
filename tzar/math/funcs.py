"""
Tzar Game Engine - Math functions.
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
# $func42
# ------------------------------------------------------------
def func42():
    func313(3421)
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func51
# ------------------------------------------------------------
def func51(arg0, arg1):
    arg1 = func33(arg0, arg1)
    return ((0 - func33(arg0, arg1)) if func33(arg0, 1) else arg1)

# ------------------------------------------------------------
# $func75
# ------------------------------------------------------------
def func75(arg0):
    v1 = (arg0 * arg0)
    v2 = ((arg0 * arg0) * arg0)
    # TODO: f32.demote_f64 []
    return (((((arg0 * arg0) * arg0) * (v1 * v1)) * ((v1 * 2.718311493989822e-06) + -0.00019839334836096632)) + ((v2 * ((v1 * 0.008333329385889463) + -0.16666666641626524)) + arg0))

# ------------------------------------------------------------
# $func76
# ------------------------------------------------------------
def func76(arg0):
    arg0 = (arg0 * arg0)
    v1 = (arg0 * arg0)
    # TODO: f32.demote_f64 []
    return ((((arg0 * arg0) * (arg0 * arg0)) * ((arg0 * 2.439044879627741e-05) + -0.001388676377460993)) + ((v1 * 0.04166662332373906) + ((arg0 * -0.499999997251031) + 1.0)))

# ------------------------------------------------------------
# $func77
# ------------------------------------------------------------
def func77(arg0):
    while True:  # block $label0
        if (load32(arg0 + 92) == 0):
            break
        while True:  # block $label1
            v3 = load32(arg0 + 28)
            if (load32(arg0 + 28) != load32(9213820)):
                v2 = load32(9213808)
                if (load32(9213808) == 0):
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
            if (load8u(9147152) == 0):
                func52((207 if load8u(9143020) else 0), 0)
                a_b()
            func47(arg0)
            return
            break
        store32(v4, 0)
        v3 = (v2 - 1)
        store32(9213808, (v2 - 1))
        while True:  # block $label3
            if (u(v1) >= u(v3)):
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
            if (u(v4) <= u(2)):
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

# ------------------------------------------------------------
# $func78
# ------------------------------------------------------------
def func78(arg0, arg1, arg2, arg3):
    v15 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v11 = load16u(arg0 + 110)
        if (load16u(arg0 + 110) == arg1):
            break
        v12 = load8u(arg0 + 122)
        v5 = ((load8u(arg0 + 122) * 404) + 9568096)
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) == 2):
            break
        if (load32(v5 + 188) != 55):
            if (load32(38528) != v12):
                break
        v10 = load8u(arg0 + 125)
        if (load8u(arg0 + 125) == 3):
            break
        v4 = ((v12 * 404) + 9568096)
        v16 = load32(((v12 * 404) + 9568096) + 176)
        v13 = load32(9561692)
        v14 = (load32(9561692) + (v11 * 286704))
        v9 = load32(v4 + 280)
        v6 = (load32(v14 + 283976) - load32(v4 + 280))
        store32((load32(9561692) + (v11 * 286704)) + 283976, (load32(v14 + 283976) - load32(v4 + 280)))
        store32(v14 + 283980, (load32(v14 + 283980) - v16))
        if ((((v9 - 1) < 0) & (u(v16) < u(-2147483647))) == 0):
            store8(v14 + 286700, 1)
        v4 = ((v13 + (v11 * 286704)) + 281748)
        if (u(v6) > u(load32(((v13 + (v11 * 286704)) + 281748)))):
            store32(v4, v6)
        while True:  # block $label3
            while True:  # block $label2
                while True:  # block $label1
                    # br_table[(v10 - 4)]
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
            while True:  # block $label4
                if (load32(v14 + 283908) != load32(9142872)):
                    break
                if (load32(v5 + 244) == 0):
                    break
                while True:  # $label8
                    v10 = load32((load32(v5 + 240) + (v7 << 2)))
                    while True:  # block $label5
                        if load8u(9147141):
                            break
                        v8 = 0
                        v4 = load32(9671120)
                        if (load32(9671120) == 0):
                            break
                        while True:  # $label7
                            while True:  # block $label6
                                v6 = load32(((v8 << 2) + 9263072))
                                if (load32(((v8 << 2) + 9263072)) == 0):
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
                    if (u((v7 + 1)) < u(load32(v5 + 244))):
                        continue
                    break
                break
            break
        while True:  # block $label9
            v5 = load32(arg0 + 20)
            if (load32(arg0 + 20) == 0):
                break
            if (load32(v5 + 8) == 0):
                break
            func157(arg0)
            while True:  # block $label10
                v5 = load32(9215884)
                v4 = load32(arg0 + 44)
                # br_table[(load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) - 2)]
                break
                break
            if v4:
                store32((v5 + (v4 << 4)), 0)
            store32(arg0 + 44, 0)
            break
        while True:  # block $label11
            v8 = load32((v13 + (v11 * 286704)) + 281796)
            if (load32((v13 + (v11 * 286704)) + 281796) == 0):
                break
            v7 = load32(v8 + 8)
            if (load32(v8 + 8) == 0):
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
                    if (u(v5) < u(v7)):
                        while True:  # $label12
                            v4 = (v4 + 1)
                            store32((v6 + (v4 << 2)), load32((v6 + ((v4 + 1) << 2))))
                            v7 = load32(v8 + 8)
                            if (u(v4) < u(load32(v8 + 8))):
                                continue
                            break
                    v7 = (v7 - 1)
                    store32(v8 + 8, (v7 - 1))
                    v4 = v5
                    if (u(v5) < u(v7)):
                        while True:  # $label13
                            v4 = (v4 + 1)
                            store32((v6 + (v4 << 2)), load32((v6 + ((v4 + 1) << 2))))
                            v7 = load32(v8 + 8)
                            if (u(v4) < u(load32(v8 + 8))):
                                continue
                            break
                    v5 = (v5 - 2)
                v5 = (v5 + 2)
                if (u((v5 + 2)) < u(v7)):
                    continue
                break
            break
        store16(arg0 + 110, arg1)
        v7 = load32(9561692)
        v8 = load16u(arg0 + 110)
        v6 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
        v5 = (load32(v6 + 283976) + v9)
        store32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 283976, (load32(v6 + 283976) + v9))
        store32(v6 + 283980, (load32(v6 + 283980) + v16))
        if (((v16 <= 0) & (v9 >= 0)) == 0):
            store8((v7 + (v8 * 286704)) + 286700, 1)
        arg1 = ((v7 + (v8 * 286704)) + 281748)
        if (u(v5) > u(load32(((v7 + (v8 * 286704)) + 281748)))):
            store32(arg1, v5)
        v4 = load32(arg0 + 28)
        while True:  # block $label15
            arg1 = load32((((v13 + (v11 * 286704)) + (load8u(arg0 + 122) << 2)) + 284636))
            if (load32((((v13 + (v11 * 286704)) + (load8u(arg0 + 122) << 2)) + 284636)) == 0):
                break
            v10 = load32(arg1 + 8)
            if (load32(arg1 + 8) == 0):
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
                store32(arg1 + 283956, (load32(arg1 + 283956) + load32(((v12 * 404) + 9568096) + 68)))
            arg1 = (v7 + (v8 * 286704))
            store32((v7 + (v8 * 286704)) + 283956, (load32(arg1 + 283956) - load32(((v12 * 404) + 9568096) + 68)))
        while True:  # block $label17
            if (load8u(9142916) == 0):
                break
            v4 = load32(arg0 + 40)
            if (load32(arg0 + 40) == 0):
                break
            v5 = load8u(arg0 + 122)
            arg1 = load16u(arg0 + 110)
            store32(v15 + 4, v4)
            store32(v15, (v5 | (arg1 << 16)))
            a_b()
            break
        while True:  # block $label20
            while True:  # block $label19
                while True:  # block $label18
                    # br_table[(load8u(arg0 + 125) - 4)]
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
            if (load32(v5 + 283908) != load32(9142872)):
                break
            v6 = ((v12 * 404) + 9568096)
            if (load32(((v12 * 404) + 9568096) + 244) == 0):
                break
            v5 = 0
            while True:  # $label24
                v4 = load32((load32(v6 + 240) + (v5 << 2)))
                while True:  # block $label21
                    if load8u(9147141):
                        break
                    v9 = 0
                    arg1 = load32(9671120)
                    if (load32(9671120) == 0):
                        break
                    while True:  # $label23
                        while True:  # block $label22
                            v10 = load32(((v9 << 2) + 9263072))
                            if (load32(((v9 << 2) + 9263072)) == 0):
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
                if (u((v5 + 1)) < u(load32(v6 + 244))):
                    continue
                break
            break
        if arg3:
        func77(arg0)
        if load32(((load8u(arg0 + 122) * 404) + 9568096) + 20):
        func387(v14)
        if (arg2 == 0):
            break
        while True:  # block $label25
            arg1 = load32(arg0 + 44)
            if (load32(arg0 + 44) == 0):
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

# ------------------------------------------------------------
# $func79
# ------------------------------------------------------------
def func79(arg0, arg1, arg2):
    if (arg2 == 0):
        return (load32(arg0 + 4) == load32(arg1 + 4))
    if (arg0 == arg1):
        return 1
    arg2 = load32(arg1 + 4)
    arg1 = load8u(load32(arg1 + 4))
    while True:  # block $label0
        v3 = load32(arg0 + 4)
        arg0 = load8u(load32(arg0 + 4))
        if (load8u(load32(arg0 + 4)) == 0):
            break
        if (arg0 != arg1):
            break
        while True:  # $label1
            arg1 = load8u(arg2 + 1)
            arg0 = load8u(v3 + 1)
            if (load8u(v3 + 1) == 0):
                break
            arg2 = (arg2 + 1)
            v3 = (v3 + 1)
            if (arg0 == arg1):
                continue
            break
        break
    return (arg0 == arg1)

# ------------------------------------------------------------
# $func80
# ------------------------------------------------------------
def func80(arg0, arg1, arg2, arg3, arg4):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
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
        if (u(v6) < u(load32(9163784))):
            break
        store32(v7, v9)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    while True:  # block $label1
        if (arg2 == 0):
            break
        v6 = load32(arg2 + 16)
        arg2 = load32(arg2 + 24)
        if (load32(arg2 + 24) >= 100):
            arg0 = load32((((arg2 + v6) << 2) + 32700))
            if (((load32((((arg2 + v6) << 2) + 32700)) < 4294967300.0) & (arg0 >= 0.0)) == 0):
                break
            # TODO: i32.trunc_f32_u []
            v8 = arg0
            break
        v8 = ((v6 * 1000) // arg2)
        break
    G.global0 = (v7 + 16)

# ------------------------------------------------------------
# $func81
# ------------------------------------------------------------
def func81(arg0, arg1, arg2, arg3):
    v16 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v5 = load8u(arg0 + 122)
        v6 = ((load8u(arg0 + 122) * 404) + 9568096)
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 188) != 55):
            if (load32(v6 + 264) == 1):
                break
        v8 = load8u(arg1 + 122)
        arg2 = (load32((((load8u(arg1 + 122) * 1020) + 9299904) + (v5 << 2))) * arg2)
        # TODO: i32.div_u []
        v6 = 100
        if (u(arg2) < u(100)):
            break
        while True:  # block $label1
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
        # TODO: i32.div_u []
        v7 = load32(arg0 + 64)
        arg2 = (((v6 * v6) if (u(arg2) > u(v7)) else (arg2 + v6)) if (load32(arg0 + 64) != -1) else 0)
        v10 = load32(9561692)
        v11 = load16u(arg1 + 110)
        v6 = (load32(9561692) + (load16u(arg1 + 110) * 286704))
        while True:  # block $label2
            if (load32(38564) == v5):
                break
            v7 = (arg2 if (u(arg2) < u(v7)) else v7)
            v9 = load16u(arg0 + 110)
            v12 = load32(v6 + 278556)
            if load32(v6 + 278556):
                v8 = (v12 + (((v9 * 255) + v8) << 2))
                store32((v12 + (((v9 * 255) + v8) << 2)), (load32(v8) + v7))
            v9 = load32(((v10 + (v9 * 286704)) + 278564))
            if (load32(((v10 + (v9 * 286704)) + 278564)) == 0):
                break
            v5 = (v9 + (((v11 * 255) + v5) << 2))
            store32((v9 + (((v11 * 255) + v5) << 2)), (load32(v5) + v7))
            break
        while True:  # block $label3
            if (v4 == 3):
                break
            v5 = load32(arg0 + 64)
            if (u(arg2) < u(load32(arg0 + 64))):
                store32(arg0 + 64, (v5 - arg2))
                if (load32(arg0 + 92) == 0):
                    break
                if load8u(9147141):
                    break
                store32(v16, arg2)
                a_b()
                break
            v5 = ((v4 == 4) | (v4 == 14))
            store32(arg0 + 64, 0)
            while True:  # block $label4
                if (load32(load32(9142424) + 120) != 3):
                    break
                if (load8u((load32(9143004) + (load16u(arg1 + 110) + (load32(9142892) * load16u(arg0 + 110))))) == 0):
                    break
                if load32(((load8u(arg0 + 122) * 404) + 9568096) + 264):
                    break
                arg2 = 1
                store8(v6 + 286701, 1)
                while True:  # block $label5
                    v4 = load32(9142892)
                    if (u(load32(9142892)) < u(2)):
                        break
                    v12 = (v4 - 1)
                    v14 = ((v4 - 1) & 1)
                    v7 = (load32(v6 + 283908) * v4)
                    v9 = load32(9561692)
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
                    if (v14 == 0):
                        break
                    if (load8u((v8 + (arg2 + v7))) == 0):
                        break
                    store8((v9 + (arg2 * 286704)) + 286701, 1)
                    break
                arg2 = (v10 + (v11 * 286704))
                v6 = load32(9142424)
                store32((v10 + (v11 * 286704)) + 283848, (load32(arg2 + 283848) + load32(load32(9142424) + 100)))
                v4 = (arg2 + 283852)
                store32((arg2 + 283852), (load32(v4) + load32(v6 + 104)))
                v4 = (arg2 + 283856)
                store32((arg2 + 283856), (load32(v4) + load32(v6 + 108)))
                arg2 = (arg2 + 283860)
                store32((arg2 + 283860), (load32(arg2) + load32(v6 + 112)))
                break
            func155(arg1, arg0, v5)
            while True:  # block $label7
                v6 = load8u(arg0 + 122)
                if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) == 0):
                    arg2 = load32(38472)
                    break
                arg2 = load32(38472)
                if ((load32(38600) != v6) & (load32(38472) != v6)):
                    break
                if (v5 == 0):
                    break
                break
            while True:  # block $label8
                if ((v5 & (arg2 == v6)) == 0):
                    v9 = load16u(arg0 + 110)
                    break
                store32(59200, load32(arg0 + 28))
                v6 = load32(9671128)
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
                    v6 = load32(9671128)
                    v12 = load32(9142840)
                    while True:  # block $label9
                        v10 = load16u(v10 + 114)
                        v17 = (u(v7) <= u(load16u(v10 + 114)))
                        if (u(v7) <= u(load16u(v10 + 114))):
                            break
                        if (u(v7) <= u(v14)):
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
                    while True:  # block $label10
                        if (v10 == 0):
                            break
                        if (u(v7) <= u((v10 - 1))):
                            break
                        if (u(v7) <= u(v8)):
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
                    while True:  # block $label11
                        if v17:
                            break
                        if (u(v7) <= u((v8 - 1))):
                            break
                        if (v8 == 0):
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
                    while True:  # block $label12
                        if (u(v7) <= u(v15)):
                            break
                        if (u(v7) <= u(v8)):
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
                    if (u(v4) > u(34)):
                        break
                    v4 = (v4 + 1)
                    if (u((v4 + 1)) < u(arg2)):
                        continue
                    break
                break
            if (load8u((load32(9143004) + (load16u(arg1 + 110) + (load32(9142892) * v9)))) == 0):
                break
            if (arg3 == 0):
                break
            while True:  # block $label14
                arg0 = load32(9561692)
                v6 = load16u(arg1 + 110)
                if (load32(((load32(9561692) + (load16u(arg1 + 110) * 286704)) + 284008)) == 0):
                    break
                if (load8u(((load8u(arg1 + 122) * 404) + 9568096) + 334) == 0):
                    break
                arg2 = (load32(arg1 + 80) + 100)
                store32(arg1 + 80, (load32(arg1 + 80) + 100))
                while True:  # block $label15
                    arg3 = load32(arg1 + 84)
                    v5 = (arg0 + (v6 * 286704))
                    if (u(load32(arg1 + 84)) < u(load32(((arg0 + (v6 * 286704)) + 284388)))):
                        break
                    if (load32(((v5 + (load32(39180) << 2)) + 281808)) != 1):
                        break
                    v12 = load16u(arg1 + 114)
                    v17 = load32(arg1 + 28)
                    while True:  # block $label16
                        v15 = load16u(arg1 + 112)
                        arg0 = load32(((load32(9561692) + (v6 * 286704)) + 284336))
                        arg2 = (load16u(arg1 + 112) - load32(((load32(9561692) + (v6 * 286704)) + 284336)))
                        arg3 = (arg0 << 1)
                        v18 = ((arg0 << 1) + v15)
                        if ((load16u(arg1 + 112) - load32(((load32(9561692) + (v6 * 286704)) + 284336))) >= ((arg0 << 1) + v15)):
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
                                while True:  # block $label17
                                    v4 = (arg0 - v12)
                                    if ((v22 + ((arg0 - v12) * v4)) > v20):
                                        break
                                    v4 = load32(9142440)
                                    if (u(load32(9142440)) <= u(arg0)):
                                        break
                                    if ((arg0 | arg2) < 0):
                                        break
                                    if (u(arg2) >= u(v4)):
                                        break
                                    v23 = (arg0 + 1)
                                    v14 = 0
                                    while True:  # $label22
                                        while True:  # block $label18
                                            v4 = (load32(9142440) + 2)
                                            v4 = load32((load32(9142840) + ((arg3 + ((v23 + ((load32(9142440) + 2) * v14)) * v4)) << 2)))
                                            if (u(load32((load32(9142840) + ((arg3 + ((v23 + ((load32(9142440) + 2) * v14)) * v4)) << 2)))) < u(3)):
                                                break
                                            if (v4 == v17):
                                                break
                                            v4 = (load32(9671128) + (v4 * 132))
                                            if (load16u((load32(9671128) + (v4 * 132)) + 110) != v6):
                                                break
                                            v10 = load8u(v4 + 122)
                                            if (load8u(((load8u(v4 + 122) * 404) + 9568096) + 334) == 0):
                                                break
                                            v8 = load32(v4 + 84)
                                            if (u(load32(v4 + 84)) > u(10)):
                                                break
                                            v7 = (load32(v4 + 80) + 100)
                                            store32(v4 + 80, (load32(v4 + 80) + 100))
                                            v9 = (load32(9561692) + v21)
                                            # TODO: i32.div_u []
                                            if (u((v8 * 100)) < u(load32(((load32(9561692) + v21) + 284008)))):
                                                break
                                            v11 = load32((v9 + 284012))
                                            v7 = 10
                                            while True:  # block $label19
                                                if load32(((v9 + (load32(38488) << 2)) + 281808)):
                                                    break
                                                if load32(((v9 + (load32(38848) << 2)) + 281808)):
                                                    break
                                                v7 = (10 if load32(((v9 + (load32(38916) << 2)) + 281808)) else 0)
                                                break
                                            if (u(v8) >= u((v7 + v11))):
                                                break
                                            store32(v4 + 80, 0)
                                            v7 = (v8 + 1)
                                            store32(v4 + 84, (v8 + 1))
                                            v8 = (v9 + 281672)
                                            store32((v9 + 281672), (load32(v8) + 1))
                                            if (load32((v9 + 284388)) == v7):
                                                v7 = load32(v4 + 24)
                                                if (load32(v4 + 24) == 0):
                                                    v7 = func26(16)
                                                    store64(func26(16), 0)
                                                    store64(v7 + 8, 0)
                                                    store32(v4 + 24, v7)
                                                if (load32(v7 + 8) == 0):
                                                    v8 = func26(16)
                                                    store32(func26(16) + 4, 20)
                                                    store32(v8, func26(80))
                                                    store64(v8 + 8, 8589934592)
                                                    store32(v7 + 8, v8)
                                                    v10 = 0
                                                    v7 = load32(((load8u(v4 + 122) * 404) + 9568096) + 196)
                                                    v24 = ((load32((load32(9561692) + (load16u(v4 + 110) * 286704)) + 283936) * 20) % load16u(((load32(((load8u(v4 + 122) * 404) + 9568096) + 196) << 1) + 9142944)))
                                                    v25 = ((v7 << 2) + 9142928)
                                                    while True:  # $label21
                                                        v26 = load16u((load32(v25) + ((v10 + v24) << 1)))
                                                        if load16u((load32(v25) + ((v10 + v24) << 1))):
                                                            while True:  # block $label20
                                                                v8 = load32(load32(v4 + 24) + 8)
                                                                v7 = load32(load32(load32(v4 + 24) + 8) + 8)
                                                                if (load32(load32(load32(v4 + 24) + 8) + 8) != load32(v8 + 4)):
                                                                    v11 = load32(v8)
                                                                    break
                                                                v11 = (load32(v8 + 12) + v7)
                                                                store32(v8 + 4, (load32(v8 + 12) + v7))
                                                                v13 = load32(v8)
                                                                v11 = func26((-1 if (u(v11) > u(1073741823)) else (v11 << 2)))
                                                                if v7:
                                                                    # TODO: memory.copy []
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
                                            v8 = (load32(((v10 * 404) + 9568096) + 224) > 1)
                                            store32(v4 + 52, (load32(v4 + 52) + ((load32(v4 + 84) & 1) if (load32(((v10 * 404) + 9568096) + 224) > 1) else 1)))
                                            store32(v4 + 60, (load32(v4 + 60) + (((v7 & 3) == 1) if v8 else v9)))
                                            if (load32(v4 + 92) == 0):
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
                    arg0 = load32(9561692)
                    break
                # TODO: i32.div_u []
                if (u((arg3 * 100)) < u(load32(((arg0 + (v6 * 286704)) + 284008)))):
                    break
                v5 = (arg0 + (v6 * 286704))
                v4 = load32(((arg0 + (v6 * 286704)) + 284012))
                arg2 = 10
                while True:  # block $label25
                    if load32(((v5 + (load32(38488) << 2)) + 281808)):
                        break
                    if load32(((v5 + (load32(38848) << 2)) + 281808)):
                        break
                    arg2 = (10 if load32((((arg0 + (v6 * 286704)) + (load32(38916) << 2)) + 281808)) else 0)
                    break
                if (u(arg3) >= u((arg2 + v4))):
                    break
                func198(arg1)
                break
            break
            break
        while True:  # block $label26
            arg2 = load32(9671128)
            arg3 = load32(arg1 + 28)
            if (load8u((load32(9143004) + (load16u(arg0 + 110) + (load32(9142892) * load16u((load32(9671128) + (load32(arg1 + 28) * 132)) + 110))))) == 0):
                break
            if (load8u(arg0 + 126) == 2):
                break
            while True:  # block $label28
                while True:  # block $label27
                    v4 = load32(9215884)
                    v5 = load32(arg0 + 44)
                    v6 = load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4)
                    if (((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 22) | (v5 == 0)) == 0):
                        break
                    if load8u(arg0 + 125):
                        break
                    if load32(arg0 + 36):
                        break
                    arg1 = load8u(arg0 + 122)
                    if load32(((load8u(arg0 + 122) * 404) + 9568096) + 260):
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
                v6 = ((load8u(v6 + 122) * 404) + 9568096)
                if (load32(((load8u(v6 + 122) * 404) + 9568096) + 264) == 1):
                    arg1 = (arg1 if (load32(v6 + 268) == 1) else (arg1 + 100))
                v6 = (arg2 + (load32((v4 + ((v5 << 4) | 12))) * 132))
                v5 = (v7 - load16u((arg2 + (load32((v4 + ((v5 << 4) | 12))) * 132)) + 114))
                v5 = (v9 - load16u(v6 + 112))
                v5 = (((v7 - load16u((arg2 + (load32((v4 + ((v5 << 4) | 12))) * 132)) + 114)) * v5) + ((v9 - load16u(v6 + 112)) * v5))
                v6 = load8u(v6 + 122)
                if (load32(((load8u(v6 + 122) * 404) + 9568096) + 264) == 1):
                else:
                if (v5 <= arg1):
                    break
                arg1 = load8u(arg0 + 122)
                break
            while True:  # block $label29
                arg1 = ((arg1 * 404) + 9568096)
                if (load32(((arg1 * 404) + 9568096) + 228) == 0):
                    if load32(arg1 + 260):
                        break
                v6 = load32(arg0 + 28)
                v5 = load32(((load8u((arg2 + (load32(arg0 + 28) * 132)) + 122) * 404) + 9568096) + 228)
                if (load32(((load8u((arg2 + (load32(arg0 + 28) * 132)) + 122) * 404) + 9568096) + 228) == 0):
                    break
                arg1 = load32(((load8u((arg2 + (arg3 * 132)) + 122) * 404) + 9568096) + 216)
                if (load32(((load8u((arg2 + (arg3 * 132)) + 122) * 404) + 9568096) + 216) == 0):
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
                    while True:  # block $label31
                        while True:  # $label30
                            v12 = (v10 - (arg2 + v8))
                            if (u(v5) > u((((v10 - (arg2 + v8)) * v12) + v11))):
                                arg2 = (arg2 + 1)
                                if (arg1 != (arg2 + 1)):
                                    continue
                                break
                            break
                        if (v4 == 0):
                            break
                        break
                        break
                    v6 = (v6 + 1)
                    v4 = (u((v6 + 1)) < u(arg1))
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

# ------------------------------------------------------------
# $func82
# ------------------------------------------------------------
def func82(arg0, arg1, arg2, arg3):
    while True:  # block $label0
        if (arg1 <= 0):
            break
        v6 = (arg0 - -64)
        while True:  # $label3
            if (load32(v6) < load32(arg0 + 56)):
                if (load32(arg0 + 24) <= 0):
                    break
            if load32(arg0 + 4):
                store64(arg0 + 76, rotl(load64(arg0 + 76), 32, 64))
            if (load32(arg0 + 60) >= load32(arg0 + 48)):
                a_c()
                raise RuntimeError('unreachable')
            # call_indirect[load32((9687804 if load32(arg0) else 9687800))]
            while True:  # block $label1
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

# ------------------------------------------------------------
# $func83
# ------------------------------------------------------------
def func83(arg0, arg1, arg2, arg3):
    v8 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    v6 = (arg1 + 24)
    v7 = func39((arg1 + 24), 1)
    # TODO: memory.fill []
    while True:  # block $label10
        while True:  # block $label9
            while True:  # block $label0
                if v7:
                    v7 = func39(v6, 1)
                    store32((arg2 + (func39(v6, (8 if func39(v6, 1) else 1)) << 2)), 1)
                    if (v7 != 1):
                        break
                    store32((arg2 + (func39(v6, 8) << 2)), 1)
                    break
                # TODO: memory.fill []
                v7 = (func39(v6, 4) + 4)
                if ((func39(v6, 4) + 4) <= 19):
                    if (v7 > 0):
                        while True:  # $label1
                            store32((v8 + (load8u((v4 + 13808)) << 2)), func39(v6, 3))
                            v4 = (v4 + 1)
                            if ((v4 + 1) != v7):
                                continue
                            break
                    while True:  # block $label2
                        if (func452(128, (v8 + 76)) == 0):
                            break
                        if (func457((v8 + 76), 7, v8, 19) == 0):
                            break
                        v10 = arg0
                        if func39(v6, 1):
                            v10 = (func39(v6, ((func39(v6, 3) << 1) + 2)) + 2)
                            if ((func39(v6, ((func39(v6, 3) << 1) + 2)) + 2) > arg0):
                                break
                        while True:  # block $label3
                            if (arg0 <= 0):
                                break
                            v11 = 8
                            while True:  # $label7
                                if (v10 == 0):
                                    break
                                v4 = load32(arg1 + 44)
                                if (load32(arg1 + 44) >= 32):
                                    func135(v6)
                                    v4 = load32(arg1 + 44)
                                v7 = (load32(load32(v8 + 92)) + ((i32(((load64(arg1 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64((v4 & 63)))) & 127) << 2))
                                store32(arg1 + 44, (v4 + load8u((load32(load32(v8 + 92)) + ((i32(((load64(arg1 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64((v4 & 63)))) & 127) << 2)))))
                                while True:  # block $label4
                                    v4 = load16u(v7 + 2)
                                    if (u(load16u(v7 + 2)) <= u(15)):
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
                                    if (u((v12 - 1)) >= u(7)):
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
                    while True:  # block $label8
                        # br_table[load32(arg1)]
                        break
                        break
                    store32(arg1, 3)
                    break
                a_c()
                raise RuntimeError('unreachable')
                break
            if load32(arg1 + 48):
                break
            v4 = func457(arg3, 8, arg2, arg0)
            if func457(arg3, 8, arg2, arg0):
                break
            break
        v4 = 0
        while True:  # block $label11
            # br_table[load32(arg1)]
            break
            break
        store32(arg1, 3)
        break
    G.global0 = (v8 + 96)
    return v4

# ------------------------------------------------------------
# $func84
# ------------------------------------------------------------
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
            while True:  # block $label0
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
                while True:  # block $label1
                    if (((arg6 >= v26) & (arg6 >= v27)) == 0):
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
            if (u(arg4) > u(1)):
                continue
            break
    return (v13 - v9)

# ------------------------------------------------------------
# $func85
# ------------------------------------------------------------
def func85(arg0, arg1, param2):
    store8(arg0 + 125, 1)
    while True:  # block $label0
        v4 = load32(9142840)
        v6 = load16u(arg0 + 112)
        v8 = load16u(arg0 + 114)
        v2 = (load32(9142440) + 2)
        v3 = ((load8u(arg0 + 122) * 404) + 9568096)
        if (load32((load32(9142840) + ((load16u(arg0 + 112) + (((load16u(arg0 + 114) + ((load32(9142440) + 2) * load32(((load8u(arg0 + 122) * 404) + 9568096) + 208))) + 1) * v2)) << 2)) + 4) != load32(v3 + 212)):
            break
        if (load32(v3 + 216) == 0):
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
                if (u(v2) < u(load32(v3 + 216))):
                    continue
                break
            if (u(v5) < u(v7)):
                continue
            break
        break
    func92(arg0, 0.0, 0.0)
    if load8u(9142916):
    while True:  # block $label8
        while True:  # block $label11
            while True:  # block $label3
                v2 = load8u(arg0 + 123)
                if (load8u(arg0 + 123) == 0):
                    break
                if (arg1 == 0):
                    break
                while True:  # block $label5
                    arg1 = load32(arg0 + 96)
                    if load32(arg0 + 96):
                        while True:  # block $label4
                            v3 = load32(9671128)
                            v2 = (load32(9671128) + (arg1 * 132))
                            if (load32((load32(9671128) + (arg1 * 132)) + 36) != load32(arg0 + 28)):
                                break
                            if (load8u(v2 + 125) == 3):
                                break
                            arg1 = (v3 + (arg1 * 132))
                            if load32(((load8u((v3 + (arg1 * 132)) + 122) * 404) + 9568096) + 268):
                                arg1 = load32(arg1 + 52)
                                store32(arg1 + 52, (load32(arg1 + 52) - 1))
                                if (u(arg1) >= u(2)):
                                    break
                            break
                            break
                        func29(arg0, 0)
                        return func32(func60(arg0, 1.0), v2, 0)
                    v3 = load32(9561692)
                    v5 = load16u(arg0 + 110)
                    arg1 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
                    while True:  # block $label6
                        v4 = ((v2 * 40) + 9671200)
                        if (load8u(((v2 * 40) + 9671200) + 18) == 0):
                            break
                        while True:  # block $label7
                            v6 = (load32(arg1 + 283976) + 1)
                            if (u((load32(arg1 + 283976) + 1)) > u((load32((arg1 + 284136)) + load32(arg1 + 283980)))):
                                v2 = 57101
                                if (load32((v3 + (v5 * 286704)) + 283908) == load32(9142872)):
                                    break
                                break
                            v3 = (v3 + (v5 * 286704))
                            if (u(v6) <= u(load32(((v3 + (v5 * 286704)) + 284000)))):
                                break
                            v2 = 57113
                            if (load32(v3 + 283908) != load32(9142872)):
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
                    while True:  # block $label9
                        if (v2 == 0):
                            break
                        v5 = load32(arg0 + 72)
                        v4 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
                        v2 = load32((((load32(9561692) + (load16u(arg0 + 110) * 286704)) + (v2 << 2)) + 283984))
                        if (u(load32(arg0 + 72)) < u(load32((((load32(9561692) + (load16u(arg0 + 110) * 286704)) + (v2 << 2)) + 283984)))):
                            while True:  # block $label10
                                if (u(v2) <= u(load32(arg0 + 76))):
                                    break
                                store8(arg0 + 127, 1)
                                v2 = load32(arg0 + 40)
                                if (load32(arg0 + 40) == 0):
                                    break
                                if (load8u(9142916) == 0):
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
                        if (load32(arg0 + 92) == 0):
                            break
                        if load32(9140316):
                            if (load32(9140320) != load32(arg0 + 28)):
                                break
                        break
                    G.global0 = (arg1 + 16)
                    if (v3 == 0):
                        break
                    break
                # call_indirect[load32(((load8u(arg0 + 123) * 40) + 9671200) + 20)]
                if (load8u(arg0 + 125) == 10):
                    break
                if (load8u(arg0 + 123) == 63):
                    break
                store8(arg0 + 125, 0)
                return indirect_call(load32(((load8u(arg0 + 123) * 40) + 9671200) + 20))
                break
            arg1 = load32(((v2 * 40) + 9671200) + 36)
            if load32(((v2 * 40) + 9671200) + 36):
                # call_indirect[arg1]
                if indirect_call(arg1):
                    break
            func29(arg0, 1)
            break
        return load32(arg0 + 28)
        break
    func29(arg0, 1)
    return load32(arg0 + 32)

# ------------------------------------------------------------
# $func86
# ------------------------------------------------------------
def func86(arg0):
    v1 = load8u(arg0 + 122)
    while True:  # block $label3
        while True:  # block $label1
            while True:  # block $label0
                if (load16u(arg0 + 108) == 0):
                    break
                while True:  # block $label2
                    # br_table[(v1 + -64)]
                    break
                    break
                if (v1 == 10):
                    break
                break
            v2 = ((v1 * 72) + 9263856)
            break
            break
        while True:  # block $label5
            while True:  # block $label4
                v2 = load32(arg0 + 20)
                if (load32(arg0 + 20) == 0):
                    break
                if (u(load32(v2 + 8)) < u(3)):
                    break
                if load32(load32(v2)):
                    break
                v2 = ((v1 * 72) + 9263856)
                if (load32(((v1 * 72) + 9263856) + 68) == 0):
                    break
                break
                break
            while True:  # block $label9
                while True:  # block $label6
                    while True:  # block $label8
                        while True:  # block $label7
                            v2 = load32(arg0 + 88)
                            # br_table[(load32(arg0 + 88) & 65535)]
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
    while True:  # block $label10
        if (load32(38472) == v1):
            break
        if (load32(38600) == v1):
            break
        break
    return func37(arg0, load32(v2), v3, 0)

# ------------------------------------------------------------
# $func87
# ------------------------------------------------------------
def func87(arg0, arg1):
    v4 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v19 = load32(9561692)
    v17 = (1 if (load32(38504) == arg1) else 4)
    store8(arg0 + 129, (1 if (load32(38504) == arg1) else 4))
    while True:  # block $label0
        arg1 = load32(((v19 + (arg1 << 2)) + 284636))
        if (load32(((v19 + (arg1 << 2)) + 284636)) == 0):
            break
        v20 = load32(arg1 + 8)
        if (load32(arg1 + 8) == 0):
            break
        v21 = load16u(arg0 + 110)
        v22 = (v19 + (load16u(arg0 + 110) * 286704))
        v9 = ((v19 + (load16u(arg0 + 110) * 286704)) + 283872)
        v10 = (v22 + 283876)
        v11 = load32(v22 + 283960)
        v14 = (((v19 + (v21 * 286704)) + (load32(((load32(v22 + 283960) << 2) + 9940)) << 2)) + 284636)
        v13 = load32(9215884)
        v15 = load32(9671128)
        v8 = load32(arg1)
        v24 = -1.0
        while True:  # $label5
            while True:  # block $label1
                arg1 = load32((v8 + (v16 << 2)))
                if (load32((v8 + (v16 << 2))) == 0):
                    break
                v18 = (v15 + (arg1 * 132))
                if (load8u((v15 + (arg1 * 132)) + 125) == 3):
                    break
                arg1 = (load32(v10) - load16u(v18 + 114))
                arg1 = (load32(v9) - load16u(v18 + 112))
                # TODO: i32.div_u []
                # TODO: f32.convert_i32_u []
                # TODO: f64.promote_f32 []
                # TODO: f32.demote_f64 []
                v25 = ((load32(v18 + 68) - load32(v18 + 64)) + 100)
                if ((sqrt(float((((load32(v10) - load16u(v18 + 114)) * arg1) + ((load32(v9) - load16u(v18 + 112)) * arg1)))) | (((load32(v18 + 68) - load32(v18 + 64)) + 100) < v24)) == 0):
                    break
                v7 = 0
                while True:  # block $label2
                    arg1 = load32(v14)
                    if (load32(v14) == 0):
                        break
                    v2 = load32(arg1 + 8)
                    if (load32(arg1 + 8) == 0):
                        break
                    v6 = load32(arg1)
                    arg1 = 0
                    while True:  # $label4
                        while True:  # block $label3
                            v5 = load32((v6 + (arg1 << 2)))
                            if (load32((v6 + (arg1 << 2))) == 0):
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
                arg1 = (u(v7) < u(20))
                v12 = (load32(v18 + 28) if (u(v7) < u(20)) else v12)
                v24 = (v25 if arg1 else v24)
                v23 = (v7 if arg1 else v23)
                break
            v16 = (v16 + 1)
            if ((v16 + 1) != v20):
                continue
            break
        if (v12 == 0):
            v2 = 0
            break
        v7 = 0
        v17 = load32(9671128)
        v2 = load8u((load32(9671128) + (v12 * 132)) + 122)
        while True:  # block $label15
            while True:  # block $label8
                while True:  # block $label6
                    v20 = load32(((v11 << 2) + 9687164))
                    v9 = load32((((v19 + (v21 * 286704)) + (load32(((v11 << 2) + 9687164)) << 2)) + 284636))
                    if (load32((((v19 + (v21 * 286704)) + (load32(((v11 << 2) + 9687164)) << 2)) + 284636)) == 0):
                        break
                    v10 = load32(v9 + 8)
                    if (load32(v9 + 8) == 0):
                        break
                    v6 = (v17 + (v12 * 132))
                    arg1 = 0
                    while True:  # $label9
                        while True:  # block $label7
                            v11 = load32((load32(v9) + (arg1 << 2)))
                            if (load32((load32(v9) + (arg1 << 2))) == 0):
                                break
                            v14 = load32(9671128)
                            v8 = (load32(9671128) + (v11 * 132))
                            v3 = load8u((load32(9671128) + (v11 * 132)) + 125)
                            if (load8u((load32(9671128) + (v11 * 132)) + 125) == 3):
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
                        if (u((arg1 + 1)) < u(v10)):
                            continue
                        break
                    break
                # TODO: i32.div_u []
                if ((v7 & (u(v23) <= u(6))) == 0):
                    v2 = 1
                    break
                v2 = load32(((v2 * 404) + 9568096) + 216)
                v13 = ((v20 * 404) + 9568096)
                arg1 = load32(((v20 * 404) + 9568096) + 216)
                v15 = ((v19 + (v21 * 286704)) + 283908)
                while True:  # block $label11
                    while True:  # block $label10
                        v8 = (v17 + (v12 * 132))
                        v6 = load16u((v17 + (v12 * 132)) + 112)
                        v3 = load16u(v8 + 114)
                        v5 = (load16u(v8 + 114) + (load32(v13 + 220) ^ -1))
                        if (func73(load16u((v17 + (v12 * 132)) + 112), (load16u(v8 + 114) + (load32(v13 + 220) ^ -1)), v13, 0, 0, 1) == 0):
                            break
                        if (func108(v6, v5, load32(v15), 7) == 0):
                            break
                        arg1 = v6
                        break
                        break
                    while True:  # block $label12
                        v2 = (v2 + 1)
                        v5 = ((v2 + 1) + v3)
                        if (func73(v6, ((v2 + 1) + v3), v13, 0, 0, 1) == 0):
                            break
                        if (func108(v6, v5, load32(v15), 7) == 0):
                            break
                        arg1 = v6
                        break
                        break
                    while True:  # block $label13
                        arg1 = ((arg1 ^ -1) + v6)
                        if (func73(((arg1 ^ -1) + v6), v3, v13, 0, 0, 1) == 0):
                            break
                        if (func108(arg1, v3, load32(v15), 7) == 0):
                            break
                        v5 = v3
                        break
                        break
                    while True:  # block $label14
                        arg1 = (v2 + v6)
                        if (func73((v2 + v6), v3, v13, 0, 0, 1) == 0):
                            break
                        if (func108(arg1, v3, load32(v15), 7) == 0):
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
                        while True:  # block $label16
                            v8 = v2
                            v2 = (v2 << 2)
                            v9 = load32((((v2 << 2) | 4) + 8611904))
                            v10 = (load32((((v2 << 2) | 4) + 8611904)) + v3)
                            if (u(v16) <= u((load32((((v2 << 2) | 4) + 8611904)) + v3))):
                                break
                            v2 = load32((v2 + 8611904))
                            v11 = (load32((v2 + 8611904)) + v6)
                            if (u(v16) <= u((load32((v2 + 8611904)) + v6))):
                                break
                            if ((v10 | v11) < 0):
                                break
                            v2 = ((v9 * v9) + (v2 * v2))
                            if (((v9 * v9) + (v2 * v2)) >= v14):
                                break
                            v9 = func73(v11, v10, v13, 0, 0, 1)
                            v16 = load32(9142440)
                            if (v9 == 0):
                                break
                            if (func108(v11, v10, load32(v15), 7) == 0):
                                break
                            arg1 = v11
                            v5 = v10
                            v14 = v2
                            break
                        v2 = (v8 + 2)
                        if (u(v8) < u(1918)):
                            continue
                        break
                    v2 = 0
                    if (v14 == 2147483647):
                        break
                    break
                while True:  # block $label19
                    while True:  # block $label18
                        v6 = ((v20 * 404) + 9568096)
                        v3 = load32(((v20 * 404) + 9568096) + 68)
                        if load32(((v20 * 404) + 9568096) + 68):
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
                        if (load32(v6 + 80) == 0):
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
                if load32(load32(9142424) + 156):
                    func29((load32(9671128) + (v3 * 132)), 1)
                arg0 = (load32(9142440) + 2)
                arg0 = load32((load32(9142840) + ((arg1 + (((v5 + (load32(9142440) + 2)) + 1) * arg0)) << 2)) + 4)
                if (u(load32((load32(9142840) + ((arg1 + (((v5 + (load32(9142440) + 2)) + 1) * arg0)) << 2)) + 4)) < u(3)):
                    break
                store32((load32(9671128) + (arg0 * 132)) + 96, v12)
                break
                break
            v2 = 1
            break
            break
        v2 = 1
        break
    G.global0 = (v4 - -64)
    return v2

# ------------------------------------------------------------
# $func88
# ------------------------------------------------------------
def func88(arg0):
    while True:  # block $label0
        if load8u(9216060):
            if load8u(arg0 + 286696):
                break
            if (load32(arg0 + 284616) == 0):
                break
            if (load32(arg0 + 283976) == 0):
                break
            arg0 = (((load32(arg0 + 283848) + load32((arg0 + 281692))) - load32(arg0 + 283956)) + 100000)
            return ((((load32(arg0 + 283848) + load32((arg0 + 281692))) - load32(arg0 + 283956)) + 100000) if (arg0 > 0) else 0)
        # TODO: i32.div_u []
        v5 = load32(9142892)
        if load32(9142892):
            v10 = load32((arg0 + 281784))
            v6 = (load32((arg0 + 281784)) * 255)
            v7 = (v5 * v10)
            arg0 = 0
            v8 = load32(9561692)
            v9 = load32(9143004)
            while True:  # $label3
                if load8u((v9 + (arg0 + v7))):
                    v2 = ((v8 + (arg0 * 286704)) + 278564)
                    v1 = 0
                    while True:  # $label2
                        while True:  # block $label1
                            v3 = ((v1 * 404) + 9568096)
                            if (load32(((v1 * 404) + 9568096) + 264) != 1):
                                break
                            if (load32(v3 + 268) == 1):
                                break
                            # TODO: i32.div_u []
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
                        while True:  # block $label4
                            v2 = ((v1 * 404) + 9568096)
                            if (load32(((v1 * 404) + 9568096) + 264) == 1):
                                if (load32(v2 + 268) != 1):
                                    break
                            # TODO: i32.div_u []
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
                while True:  # block $label7
                    if load8u((v9 + (v2 + v7))):
                        break
                    if (v2 == v10):
                        break
                    v12 = ((v8 + (v2 * 286704)) + 278564)
                    v1 = 0
                    while True:  # $label9
                        while True:  # block $label8
                            v4 = ((v1 * 404) + 9568096)
                            if (load32(((v1 * 404) + 9568096) + 264) == 1):
                                if (load32(v4 + 268) != 1):
                                    break
                            # TODO: i32.div_u []
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
                while True:  # block $label11
                    if load8u((v9 + (arg0 + v7))):
                        break
                    if (arg0 == v10):
                        break
                    v12 = ((v8 + (arg0 * 286704)) + 278564)
                    v1 = 0
                    while True:  # $label13
                        while True:  # block $label12
                            v2 = ((v1 * 404) + 9568096)
                            if (load32(((v1 * 404) + 9568096) + 264) != 1):
                                break
                            if (load32(v2 + 268) == 1):
                                break
                            # TODO: i32.div_u []
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

# ------------------------------------------------------------
# $func97
# ------------------------------------------------------------
def func97(arg0):
    func111(arg0, 1)

# ------------------------------------------------------------
# $func104
# ------------------------------------------------------------
def func104(arg0, arg1):
    return func309(((arg1 << 1) + 32304), 2, arg0)

# ------------------------------------------------------------
# $func117
# ------------------------------------------------------------
def func117(arg0, arg1, arg2):
    if arg1:
        return
    func29(arg0, 1)

# ------------------------------------------------------------
# $func121
# ------------------------------------------------------------
def func121(arg0):
    v1 = (func209(arg0) + 1)
    v2 = e()
    if (e() == 0):
        return 0
    return func35(v2, arg0, v1)

# ------------------------------------------------------------
# $func122
# ------------------------------------------------------------
def func122(arg0, arg1, arg2):

# ------------------------------------------------------------
# $func150
# ------------------------------------------------------------
def func150(arg0):

# ------------------------------------------------------------
# $func151
# ------------------------------------------------------------
def func151(arg0):
    if arg0:

# ------------------------------------------------------------
# $func154
# ------------------------------------------------------------
def func154(arg0):
    # TODO: i32.atomic.rmw.xchg []
    if (0 == 2):
        func97(arg0)

# ------------------------------------------------------------
# $func175
# ------------------------------------------------------------
def func175(arg0):
    # TODO: i32.atomic.rmw.cmpxchg []
    if 1:
        # TODO: i32.atomic.rmw.cmpxchg []
        while True:  # $label0
            # TODO: i32.atomic.rmw.cmpxchg []
            if 2:
                continue
            break

# ------------------------------------------------------------
# $func190
# ------------------------------------------------------------
def func190(arg0):
    if arg0:
        func191(arg0)

# ------------------------------------------------------------
# $func211
# ------------------------------------------------------------
def func211(arg0, arg1):
    return func210(arg0, arg1, func209(arg1))

# ------------------------------------------------------------
# $func212
# ------------------------------------------------------------
def func212():
    func313(4477)
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func213
# ------------------------------------------------------------
def func213(arg0, arg1):
    # TODO: i32.div_u []
    arg0 = 1000000
    return func214(func104(arg1, 1000000), (arg1 - (arg0 * 1000000)))

# ------------------------------------------------------------
# $func214
# ------------------------------------------------------------
def func214(arg0, arg1):
    # TODO: i32.div_u []
    arg0 = 10000
    return func215(func104(arg1, 10000), (arg1 - (arg0 * 10000)))

# ------------------------------------------------------------
# $func215
# ------------------------------------------------------------
def func215(arg0, arg1):
    # TODO: i32.div_u []
    arg0 = 100
    return func104(func104(arg1, 100), (arg1 - (arg0 * 100)))

# ------------------------------------------------------------
# $func306
# ------------------------------------------------------------
def func306(arg0):

# ------------------------------------------------------------
# $ac
# Export: ac
# ------------------------------------------------------------
def ac(arg0, arg1):
    """Exported as ac."""
    func38(arg0)

# ------------------------------------------------------------
# $func384
# ------------------------------------------------------------
def func384(arg0):

# ------------------------------------------------------------
# $func437
# ------------------------------------------------------------
def func437(arg0):
    func436(arg0)

# ------------------------------------------------------------
# $func439
# ------------------------------------------------------------
def func439(arg0, arg1):

# ------------------------------------------------------------
# $func443
# ------------------------------------------------------------
def func443(arg0):
    return (e() + 80)

# ------------------------------------------------------------
# $func466
# ------------------------------------------------------------
def func466(arg0, arg1):

# ------------------------------------------------------------
# $func467
# ------------------------------------------------------------
def func467(arg0, arg1, arg2):
    return e()

# ------------------------------------------------------------
# $Mb
# Export: Mb
# ------------------------------------------------------------
def Mb(arg0):
    """Exported as Mb."""
    v2 = (arg0 << 2)
    v1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
    if arg0:
        # TODO: memory.copy []
    func318(arg0, v1, arg0)

# ------------------------------------------------------------
# $Be
# Export: Be
# ------------------------------------------------------------
def Be():
    """Exported as Be."""
    func169()

# ------------------------------------------------------------
# $func749
# ------------------------------------------------------------
def func749(arg0):

# ------------------------------------------------------------
# $func762
# ------------------------------------------------------------
def func762(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = load32(9561692)
    v8 = load32(9671128)
    v9 = load32(arg1)
    arg1 = load16u((load32(9671128) + (load32(arg1) * 132)) + 110)
    v3 = (load32(9561692) + (load16u((load32(9671128) + (load32(arg1) * 132)) + 110) * 286704))
    v6 = ((load32(9561692) + (load16u((load32(9671128) + (load32(arg1) * 132)) + 110) * 286704)) + 283916)
    v5 = load32(v3 + 283916)
    while True:  # block $label0
        if load32(arg0 + 4):
            if v5:
                break
            while True:  # block $label1
                v10 = (v4 + (arg1 * 286704))
                arg0 = load32(arg0)
                v11 = (3 if (u(arg0) >= u(3)) else load32(arg0))
                arg0 = (((v4 + (arg1 * 286704)) + ((3 if (u(arg0) >= u(3)) else load32(arg0)) << 2)) + 283848)
                v3 = load32((((v4 + (arg1 * 286704)) + ((3 if (u(arg0) >= u(3)) else load32(arg0)) << 2)) + 283848))
                if (load32((((v4 + (arg1 * 286704)) + ((3 if (u(arg0) >= u(3)) else load32(arg0)) << 2)) + 283848)) == 2147483647):
                    break
                store32(arg0, (v3 + 1000))
                arg0 = 1
                store8(v10 + 286701, 1)
                v3 = load32(9142892)
                if (u(load32(9142892)) < u(2)):
                    break
                v7 = (v3 - 1)
                v12 = ((v3 - 1) & 1)
                arg1 = (load32((v4 + (arg1 * 286704)) + 283908) * v3)
                v4 = load32(9561692)
                v5 = load32(9143016)
                if (v3 != 2):
                    v7 = (v7 & -2)
                    v3 = 0
                    while True:  # $label2
                        if load8u((v5 + (arg0 + arg1))):
                            store8((v4 + (arg0 * 286704)) + 286701, 1)
                        v13 = (arg0 + 1)
                        if load8u((v5 + ((arg0 + 1) + arg1))):
                            store8((v4 + (v13 * 286704)) + 286701, 1)
                        arg0 = (arg0 + 2)
                        v3 = (v3 + 2)
                        if ((v3 + 2) != v7):
                            continue
                        break
                if (v12 == 0):
                    break
                if (load8u((v5 + (arg0 + arg1))) == 0):
                    break
                store8((v4 + (arg0 * 286704)) + 286701, 1)
                break
            store32(v6, 1200)
            store32(v10 + 283920, v11)
            break
        if (v5 == 0):
            break
        store64(arg2 + 8, 0)
        store64(arg2, 0)
        store32((arg2 + (load32((v4 + (arg1 * 286704)) + 283920) << 2)), load32(v6))
        if func66(v3, arg2, 1, 1):
            break
        store32(v6, 0)
        break
    while True:  # block $label3
        if (load32((v8 + (v9 * 132)) + 92) == 0):
            break
        arg0 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v8 + (v9 * 132)) + 28)):
                break
        break
    G.global0 = (arg2 + 16)

# ------------------------------------------------------------
# $func763
# ------------------------------------------------------------
def func763(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v1 + 12, 1)
    store32(v1 + 8, arg0)
    arg0 = load32(9213808)
    while True:  # block $label0
        if load8u(9147210):
            func41(38, 9173808, arg0, (v1 + 8), 2)
            break
        v3 = (arg0 << 2)
        v2 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy []
        # call_indirect[load32(9214128)]
        break
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $func770
# ------------------------------------------------------------
def func770(arg0, arg1, arg2):
    while True:  # block $label0
        if (arg2 == 0):
            break
        if (load32(arg0) == 0):
            break
        arg0 = 0
        while True:  # $label29
            while True:  # block $label12
                v12 = (load32(9671128) + (load32((arg1 + (arg0 << 2))) * 132))
                if (load8u((load32(9671128) + (load32((arg1 + (arg0 << 2))) * 132)) + 129) != 8):
                    v3 = 0
                    v4 = 0
                    v14 = 0
                    while True:  # block $label1
                        if (load8u(v12 + 129) == 8):
                            break
                        if (load8u(v12 + 125) == 3):
                            break
                        v6 = 5
                        while True:  # block $label8
                            while True:  # block $label4
                                while True:  # block $label2
                                    v7 = load8u(v12 + 122)
                                    if (load8u(v12 + 122) == load32(38604)):
                                        break
                                    if (load32(38624) == v7):
                                        break
                                    v15 = -1
                                    while True:  # block $label3
                                        if (v7 == load32(38608)):
                                            v4 = 1
                                            break
                                        if (v7 == load32(38628)):
                                            break
                                        v6 = 4
                                        v14 = -1
                                        v3 = 1
                                        while True:  # block $label7
                                            while True:  # block $label5
                                                if (load32(38612) == v7):
                                                    break
                                                if (load32(38632) == v7):
                                                    break
                                                while True:  # block $label6
                                                    if (load32(38616) == v7):
                                                        break
                                                    if (load32(39056) == v7):
                                                        break
                                                    v3 = 0
                                                    v15 = 0
                                                    break
                                                    break
                                                v14 = 1
                                                break
                                                break
                                            break
                                        v15 = 0
                                        break
                                        break
                                    v14 = 0
                                    v6 = 5
                                    break
                                    break
                                v15 = 1
                                break
                            v4 = 1
                            break
                        v9 = 2
                        v13 = load32(9142840)
                        v8 = load16u(v12 + 112)
                        v18 = (v14 + 1)
                        v17 = (v4 * v9)
                        v5 = (load32(9142440) + 2)
                        v16 = ((v7 * 404) + 9568096)
                        v10 = ((load32(9142440) + 2) * load32(((v7 * 404) + 9568096) + 208))
                        v11 = load16u(v12 + 114)
                        v19 = (v15 + 1)
                        v20 = (v3 * v9)
                        v16 = load32(v16 + 212)
                        if (load32((load32(9142840) + (((load16u(v12 + 112) + ((v14 + 1) + (v4 * v9))) + ((((load32(9142440) + 2) * load32(((v7 * 404) + 9568096) + 208)) + (load16u(v12 + 114) + ((v15 + 1) + (v3 * v9)))) * v5)) << 2))) != load32(v16 + 212)):
                            break
                        while True:  # block $label9
                            v21 = (v9 + 1)
                            if ((v9 + 1) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v21)) + v8) + ((((v19 + (v3 * v21)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            v21 = (v9 + 2)
                            if ((v9 + 2) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v21)) + v8) + ((((v19 + (v3 * v21)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            v21 = (v9 + 3)
                            if ((v9 + 3) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v21)) + v8) + ((((v19 + (v3 * v21)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            break
                        v18 = ((v14 << 1) | 1)
                        v15 = ((v15 << 1) | 1)
                        if (load32((v13 + ((((((v14 << 1) | 1) + v17) + v8) + ((((((v15 << 1) | 1) + v20) + v11) + v10) * v5)) << 2))) != v16):
                            break
                        while True:  # block $label10
                            v14 = (v9 + 1)
                            if ((v9 + 1) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v14)) + v8) + ((((v15 + (v3 * v14)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            v19 = (v9 + 2)
                            if ((v9 + 2) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v19)) + v8) + ((((v15 + (v3 * v19)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            v19 = (v9 + 3)
                            if ((v9 + 3) == v6):
                                break
                            if (load32((v13 + ((((v18 + (v4 * v19)) + v8) + ((((v15 + (v3 * v19)) + v11) + v10) * v5)) << 2))) != v16):
                                break
                            break
                        v5 = (load32(9142440) + 2)
                        v7 = ((v7 * 404) + 9568096)
                        store32(((((v8 + v17) + ((((v11 + v20) + ((load32(9142440) + 2) * load32(((v7 * 404) + 9568096) + 208))) + 1) * v5)) << 2) + v13) + 4, load32(v7 + 212))
                        while True:  # block $label11
                            if (v6 == v14):
                                break
                            v5 = (load32(9142440) + 2)
                            store32((((((v4 * v14) + v8) + (((((v3 * v14) + v11) + ((load32(9142440) + 2) * load32(v7 + 208))) + 1) * v5)) << 2) + v13) + 4, load32(v7 + 212))
                            v5 = (v9 + 2)
                            if ((v9 + 2) == v6):
                                break
                            v5 = (load32(9142440) + 2)
                            store32((((((v4 * v5) + v8) + (((((v3 * v5) + v11) + ((load32(9142440) + 2) * load32(v7 + 208))) + 1) * v5)) << 2) + v13) + 4, load32(v7 + 212))
                            v6 = (v9 + 3)
                            if (v6 == (v9 + 3)):
                                break
                            v3 = (load32(9142440) + 2)
                            store32((((((v4 * v6) + v8) + (((((v3 * v6) + v11) + ((load32(9142440) + 2) * load32(v7 + 208))) + 1) * v3)) << 2) + v13) + 4, load32(v7 + 212))
                            break
                        store8(v12 + 129, 8)
                        if (load32(v12 + 92) == 0):
                            break
                        v3 = load8u(9147141)
                        if load32(9140316):
                            if (load32(9140320) != load32(v12 + 28)):
                                break
                        break
                    break
                v3 = 0
                v6 = 0
                v15 = 0
                v13 = (G.global0 - 112)
                G.global0 = (G.global0 - 112)
                while True:  # block $label13
                    if (load8u(v12 + 129) != 8):
                        break
                    if (load8u(v12 + 125) == 3):
                        break
                    v14 = load8u(v12 + 122)
                    v19 = ((load8u(v12 + 122) * 404) + 9568096)
                    v8 = 5
                    while True:  # block $label20
                        while True:  # block $label16
                            while True:  # block $label14
                                if (load32(38604) == v14):
                                    break
                                if (load32(38624) == v14):
                                    break
                                v18 = -1
                                while True:  # block $label15
                                    if (v14 == load32(38608)):
                                        v6 = 1
                                        break
                                    if (v14 == load32(38628)):
                                        break
                                    v8 = 4
                                    v15 = -1
                                    v3 = 1
                                    while True:  # block $label19
                                        while True:  # block $label17
                                            if (load32(38612) == v14):
                                                break
                                            if (load32(38632) == v14):
                                                break
                                            while True:  # block $label18
                                                if (load32(38616) == v14):
                                                    break
                                                if (load32(39056) == v14):
                                                    break
                                                v3 = 0
                                                v18 = 0
                                                break
                                                break
                                            v15 = 1
                                            break
                                            break
                                        break
                                    v18 = 0
                                    break
                                    break
                                v15 = 0
                                v8 = 5
                                break
                                break
                            v18 = 1
                            break
                        v6 = 1
                        break
                    v7 = 2
                    v10 = load32(v19 + 212)
                    v4 = load32(9142840)
                    v21 = (v6 * v7)
                    v11 = load16u(v12 + 112)
                    v24 = ((v6 * v7) + load16u(v12 + 112))
                    v23 = (v3 * v7)
                    v9 = load16u(v12 + 114)
                    v25 = ((v3 * v7) + load16u(v12 + 114))
                    v5 = (load32(9142440) + 2)
                    v16 = ((load32(9142440) + 2) * load32(v19 + 208))
                    if (load32(v19 + 212) != load32((load32(9142840) + ((((v6 * v7) + load16u(v12 + 112)) + (((((v3 * v7) + load16u(v12 + 114)) + ((load32(9142440) + 2) * load32(v19 + 208))) + 1) * v5)) << 2)) + 4)):
                        break
                    while True:  # block $label21
                        v17 = (v7 + 1)
                        if ((v7 + 1) == v8):
                            break
                        if (load32((((((v6 * v17) + v11) + (((((v3 * v17) + v9) + v16) + 1) * v5)) << 2) + v4) + 4) != v10):
                            break
                        v17 = (v7 + 2)
                        if ((v7 + 2) == v8):
                            break
                        if (load32((((((v6 * v17) + v11) + (((((v3 * v17) + v9) + v16) + 1) * v5)) << 2) + v4) + 4) != v10):
                            break
                        v17 = (v7 + 3)
                        if ((v7 + 3) == v8):
                            break
                        if (load32((((((v6 * v17) + v11) + (((((v3 * v17) + v9) + v16) + 1) * v5)) << 2) + v4) + 4) != v10):
                            break
                        break
                    v17 = (v15 + 1)
                    v20 = (v18 + 1)
                    if (load32((v4 + (((((v15 + 1) + v21) + v11) + (((((v18 + 1) + v23) + v9) + v16) * v5)) << 2))) != v10):
                        break
                    while True:  # block $label22
                        v22 = (v7 + 1)
                        if ((v7 + 1) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v22)) + v11) + ((((v20 + (v3 * v22)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        v22 = (v7 + 2)
                        if ((v7 + 2) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v22)) + v11) + ((((v20 + (v3 * v22)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        v22 = (v7 + 3)
                        if ((v7 + 3) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v22)) + v11) + ((((v20 + (v3 * v22)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        break
                    v17 = ((v15 << 1) | 1)
                    v18 = ((v18 << 1) | 1)
                    if (load32((v4 + ((((((v15 << 1) | 1) + v21) + v11) + ((((((v18 << 1) | 1) + v23) + v9) + v16) * v5)) << 2))) != v10):
                        break
                    while True:  # block $label23
                        v15 = (v7 + 1)
                        if ((v7 + 1) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v15)) + v11) + ((((v18 + (v3 * v15)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        v20 = (v7 + 2)
                        if ((v7 + 2) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v20)) + v11) + ((((v18 + (v3 * v20)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        v20 = (v7 + 3)
                        if ((v7 + 3) == v8):
                            break
                        if (load32((v4 + ((((v17 + (v6 * v20)) + v11) + ((((v18 + (v3 * v20)) + v9) + v16) * v5)) << 2))) != v10):
                            break
                        break
                    v10 = (load32(9142440) + 2)
                    v5 = ((v14 * 404) + 9568096)
                    store32((((v24 + (((v25 + ((load32(9142440) + 2) * load32(((v14 * 404) + 9568096) + 208))) + 1) * v10)) << 2) + v4) + 4, load32(v12 + 28))
                    while True:  # block $label24
                        if (v8 == v15):
                            break
                        v10 = (load32(9142440) + 2)
                        store32((((((v6 * v15) + v11) + (((((v3 * v15) + v9) + ((load32(9142440) + 2) * load32(v5 + 208))) + 1) * v10)) << 2) + v4) + 4, load32(v12 + 28))
                        v10 = (v7 + 2)
                        if ((v7 + 2) == v8):
                            break
                        v10 = (load32(9142440) + 2)
                        store32((((((v6 * v10) + v11) + (((((v3 * v10) + v9) + ((load32(9142440) + 2) * load32(v5 + 208))) + 1) * v10)) << 2) + v4) + 4, load32(v12 + 28))
                        v8 = (v7 + 3)
                        if (v8 == (v7 + 3)):
                            break
                        v3 = (load32(9142440) + 2)
                        store32((((((v6 * v8) + v11) + (((((v3 * v8) + v9) + ((load32(9142440) + 2) * load32(v5 + 208))) + 1) * v3)) << 2) + v4) + 4, load32(v12 + 28))
                        break
                    while True:  # block $label25
                        v3 = load32(v12 + 12)
                        if (load32(v12 + 12) == 0):
                            break
                        v8 = load32(load32(v3))
                        if (load32(load32(v3)) == 0):
                            break
                        if (load32(v12 + 40) == 0):
                            break
                        v4 = load32(v19)
                        v3 = 0
                        if load8u(9142916):
                            while True:  # block $label26
                                if (v4 == 0):
                                    break
                                if (load32(v4 + 20) == 0):
                                    break
                                v11 = load8u(v12 + 124)
                                v3 = load32(v4 + 28)
                                if (load32(v4 + 28) == 2147483647):
                                    v3 = load32(59152)
                                    store32(59152, (load32(59152) + 1))
                                    v9 = load32(9568052)
                                    store32(v4 + 28, v3)
                                    v7 = load32(v4)
                                    v6 = load32(v4 + 4)
                                    v5 = load32(9568048)
                                    store32(9568048, (load32(9568048) + 1))
                                    store32(((v5 << 2) + 9563952), v4)
                                    store32(9568052, (v9 + ((v7 * (v6 + 2)) << 2)))
                                    v9 = load32(9568056)
                                    store32(v4 + 56, load32(9568056))
                                    store32(9568056, (v9 + ((v6 * load32(v4)) << 2)))
                                v3 = (v3 + (v11 << 16))
                                break
                            store32(v13 + 96, v8)
                            store64(v13 + 88, -4616189618054758400)
                            store32(v13 + 80, v3)
                            a_b()
                            break
                        v11 = (load32(v4 + 16) << 16)
                        v9 = load32(v4 + 20)
                        if load32(v4 + 20):
                            v7 = load8u(v12 + 124)
                            while True:  # block $label27
                                v3 = load32(v4 + 28)
                                if (load32(v4 + 28) != 2147483647):
                                    v6 = load32(v4 + 4)
                                    break
                                v5 = load32(v4)
                                v10 = load32(9568052)
                                v3 = ((load32(v4) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                store32(v4 + 28, ((load32(v4) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2)))
                                v6 = load32(v4 + 4)
                                store32(9568052, (v10 + ((v5 * (load32(v4 + 4) + 2)) << 2)))
                                v5 = load32(9568048)
                                store32(9568048, (load32(9568048) + 1))
                                store32(((v5 << 2) + 9563952), v4)
                                break
                            # TODO: i32.div_u []
                            # TODO: f32.convert_i32_u []
                        else:
                        v26 = 0.0
                        v3 = load16u(v12 + 110)
                        store32(v13 + 56, float(v11))
                        store32((v13 - -64), v8)
                        store32(v13 + 48, (v3 + 16))
                        # TODO: f32.convert_i32_u []
                        # TODO: f64.promote_f32 []
                        store32(v13 + 32, (v26 / load32(59156)))
                        # TODO: f32.convert_i32_u []
                        # TODO: f64.promote_f32 []
                        store32(v13 + 40, (load32(9142848) * 25))
                        a_b()
                        # TODO: f32.convert_i32_u []
                        v27 = (load16u(v12 + 112) * 32.0)
                        v3 = load8u(9142916)
                        v28 = float(load32(v4 + 12))
                        v29 = float(load32(v4 + 8))
                        while True:  # block $label28
                            # TODO: f32.convert_i32_u []
                            v30 = (load16u(v12 + 114) * 32.0)
                            v4 = load32(9142440)
                            # TODO: f32.convert_i32_u []
                            v26 = ((load16u(v12 + 114) * 32.0) + (load32(9142440) * 32.0))
                            if (((load16u(v12 + 114) * 32.0) + (load32(9142440) * 32.0)) == -55.0):
                                break
                            if (v3 == 0):
                                break
                            # TODO: f32.convert_i32_u []
                            v26 = (((v26 * 0.5) / (v4 * 96)) + 0.25)
                            break
                        store32(v13 + 24, v8)
                        # TODO: f64.promote_f32 []
                        store32(v13 + 16, v26)
                        # TODO: f64.promote_f32 []
                        store32(v13 + 8, (v30 - (0.0 if v3 else v28)))
                        # TODO: f64.promote_f32 []
                        store32(v13, (v27 - (0.0 if v3 else v29)))
                        a_b()
                        break
                    store8(v12 + 129, 0)
                    if (load32(v12 + 92) == 0):
                        break
                    v3 = load8u(9147141)
                    if load32(9140316):
                        if (load32(9140320) != load32(v12 + 28)):
                            break
                    break
                G.global0 = (v13 + 112)
                break
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break
        break
    return func28((v3 != 0), 1)

# ------------------------------------------------------------
# $func771
# ------------------------------------------------------------
def func771(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store64(v1 + 8, 1)
    while True:  # block $label0
        if arg0:
            break
        arg0 = load32(9213808)
        if load8u(9147210):
            func41(28, 9173808, arg0, (v1 + 8), 2)
            break
        v3 = (arg0 << 2)
        v2 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy []
        # call_indirect[load32(9214048)]
        break
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $func772
# ------------------------------------------------------------
def func772(arg0, arg1, arg2):
    while True:  # block $label0
        arg2 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v10 = load32(59164)
        arg1 = load32(9561692)
        arg0 = 1
        while True:  # $label1
            if (v10 != load32((arg1 + (arg0 * 286704)) + 284616)):
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != arg2):
                    continue
                break
            break
        if (load8u(9216060) == 0):
            break
        if load32((((arg1 + (arg0 * 286704)) + (load32(9671152) << 2)) + 281808)):
            break
        v17 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        arg1 = load32(9561692)
        v16 = arg0
        v13 = (load32(9561692) + (arg0 * 286704))
        # TODO: memory.fill []
        func239(load32(v13 + 283908))
        store32(v13 + 283976, 0)
        store32(v13 + 283956, 0)
        arg0 = load32(v13 + 281788)
        if load32(v13 + 281788):
            store32(arg0 + 8, 0)
        arg0 = load32(v13 + 281792)
        if load32(v13 + 281792):
            store32(arg0 + 8, 0)
        arg2 = (arg1 + (v16 * 286704))
        arg0 = load32((arg1 + (v16 * 286704)) + 281796)
        if load32((arg1 + (v16 * 286704)) + 281796):
            store32(arg0 + 8, 0)
        v23 = load32(9561692)
        while True:  # $label3
            arg0 = (arg2 + (v4 * 36))
            store32(((arg2 + (v4 * 36)) + 269408), 0)
            store64((arg0 + 269400), 0)
            store64((arg0 + 269392), 0)
            store64((arg0 + 269384), 0)
            store64((arg0 + 269376), 0)
            arg0 = (arg2 + (v4 << 2))
            store32(((arg2 + (v4 << 2)) + 282828), 0)
            store32((arg0 + 281808), 0)
            v3 = 0
            while True:  # $label2
                v6 = (arg2 + 283984)
                v7 = (v3 << 2)
                v10 = (v23 + 283984)
                store32(((arg2 + 283984) + (v3 << 2)), load32(((v23 + 283984) + v7)))
                arg0 = (v7 + 4)
                store32((v6 + (v7 + 4)), load32((arg0 + v10)))
                arg0 = (v7 + 8)
                store32((v6 + (v7 + 8)), load32((arg0 + v10)))
                arg0 = (v7 + 12)
                store32((v6 + (v7 + 12)), load32((arg0 + v10)))
                arg0 = (v7 + 16)
                store32((v6 + (v7 + 16)), load32((arg0 + v10)))
                v3 = (v3 + 5)
                if ((v3 + 5) != 155):
                    continue
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != 255):
                continue
            break
        store32((arg1 + (v16 * 286704)) + 283848, load32(load32(9142424) + 4))
        store8(9682192, 1)
        while True:  # block $label4
            v3 = load32(9142440)
            # TODO: i32.div_u []
            # TODO: f32.convert_i32_u []
            # TODO: i32.div_u []
            # TODO: f32.convert_i32_u []
            v45 = (100 + 20)
            v44 = ((load32(51780) * v3) - (100 + 20))
            if ((((load32(51780) * v3) - (100 + 20)) < 4294967300.0) & (v44 >= 0.0)):
                # TODO: i32.trunc_f32_u []
                break
            break
        v5 = 0
        v18 = ((v3 & 0xFFFFFFFF) >> 1)
        v27 = load32(9684492)
        v19 = load32(9142432)
        arg2 = load32(9147316)
        arg1 = load32(9147320)
        v7 = load32(9147312)
        arg0 = load32(9147324)
        while True:  # block $label22
            while True:  # block $label20
                while True:  # block $label5
                    if (load32(9147132) == 0):
                        break
                    if (v3 != 4096):
                        break
                    v20 = (v3 + 2)
                    v36 = (v3 - 30)
                    v37 = load32(38448)
                    v38 = load32(9671128)
                    v28 = load32(9142840)
                    while True:  # $label21
                        v6 = arg1
                        arg1 = v7
                        store32(9147320, v7)
                        v10 = arg2
                        store32(9147324, arg2)
                        arg0 = ((arg0 << 11) ^ arg0)
                        arg2 = (((((v7 & 0xFFFFFFFF) >> 19) ^ ((((arg0 << 11) ^ arg0) & 0xFFFFFFFF) >> 8)) ^ v7) ^ arg0)
                        store32(9147316, (((((v7 & 0xFFFFFFFF) >> 19) ^ ((((arg0 << 11) ^ arg0) & 0xFFFFFFFF) >> 8)) ^ v7) ^ arg0))
                        arg0 = (v6 ^ (v6 << 11))
                        v7 = ((((((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg2 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ arg2)
                        store32(9147312, ((((((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg2 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ arg2))
                        while True:  # block $label6
                            v29 = (arg2 % 4066)
                            v8 = ((arg2 % 4066) + 15)
                            arg0 = (((arg2 % 4066) + 15) - v18)
                            v30 = (v7 % v36)
                            v9 = ((v7 % v36) + 15)
                            arg0 = (((v7 % v36) + 15) - v18)
                            if (((((((arg2 % 4066) + 15) - v18) * arg0) + ((((v7 % v36) + 15) - v18) * arg0)) - 1) < 65537):
                                break
                            v24 = 1
                            while True:  # block $label7
                                v5 = (30 if (u(v15) > u(500)) else 60)
                                v3 = (v8 - (30 if (u(v15) > u(500)) else 60))
                                arg0 = (v5 << 1)
                                v31 = ((v5 << 1) + v8)
                                if ((v8 - (30 if (u(v15) > u(500)) else 60)) >= ((v5 << 1) + v8)):
                                    break
                                v6 = (v9 - v5)
                                v39 = (arg0 + v9)
                                if ((v9 - v5) >= (arg0 + v9)):
                                    break
                                v24 = 0
                                v32 = (load32(9142892) * v16)
                                v33 = load32(9142440)
                                v34 = (load32(9142440) + 2)
                                v40 = load32(38564)
                                v41 = load32(38620)
                                v42 = load32(38560)
                                v35 = load32(9143004)
                                v43 = load32(38500)
                                v12 = load32(9671128)
                                v14 = load32(9142840)
                                v21 = (v5 * v5)
                                while True:  # $label11
                                    v5 = (v3 + 1)
                                    if (u(v3) < u(v33)):
                                        arg0 = (v3 - v8)
                                        v25 = (((v3 - v8) * arg0) - 1)
                                        arg0 = v6
                                        while True:  # $label10
                                            while True:  # block $label8
                                                v4 = (arg0 - v9)
                                                if ((v25 + ((arg0 - v9) * v4)) > v21):
                                                    break
                                                if (u(arg0) >= u(v33)):
                                                    break
                                                if ((arg0 | v3) < 0):
                                                    break
                                                v4 = load32((v14 + ((v5 + (((arg0 + v34) + 1) * v34)) << 2)))
                                                if (u(load32((v14 + ((v5 + (((arg0 + v34) + 1) * v34)) << 2)))) < u(3)):
                                                    break
                                                v11 = (v12 + (v4 * 132))
                                                v22 = load8u((v12 + (v4 * 132)) + 122)
                                                if (v43 == load8u((v12 + (v4 * 132)) + 122)):
                                                    break
                                                v26 = load16u(v11 + 110)
                                                while True:  # block $label9
                                                    v4 = load16u(v11 + 120)
                                                    if load16u(v11 + 120):
                                                    else:
                                                    if load8u(((v4 if load8u((v35 + (v26 + v32))) else v26) + (v26 + v32))):
                                                        if (load8u(v11 + 128) == 0):
                                                            break
                                                        break
                                                    if (load8u(v11 + 127) != 6):
                                                        break
                                                    if load8u(v11 + 128):
                                                        break
                                                    break
                                                if (load8u(v11 + 125) == 10):
                                                    break
                                                if (load8u(v11 + 126) == 2):
                                                    break
                                                if (load32(v11 + 64) == -1):
                                                    break
                                                v4 = ((v22 * 404) + 9568096)
                                                if (load32(((v22 * 404) + 9568096) + 264) == 2):
                                                    break
                                                if (load32(v4 + 188) != 55):
                                                    break
                                                if (v22 == v42):
                                                    break
                                                if (v22 == v41):
                                                    break
                                                if (v22 != v40):
                                                    break
                                                break
                                            arg0 = (arg0 + 1)
                                            if ((arg0 + 1) != v39):
                                                continue
                                            break
                                    v24 = (v5 >= v31)
                                    v3 = v5
                                    if (v5 != v31):
                                        continue
                                    break
                                break
                            if (v24 == 0):
                                break
                            v14 = (v29 + 33)
                            v12 = 0
                            v4 = (v29 + 6)
                            arg0 = (v29 + 6)
                            v6 = (v30 + 6)
                            v21 = (v30 + 33)
                            if (u((v30 + 6)) < u((v30 + 33))):
                                while True:  # $label15
                                    while True:  # block $label13
                                        v5 = (arg0 + 1)
                                        if (u(arg0) <= u(4095)):
                                            arg0 = (arg0 - v8)
                                            v25 = (((arg0 - v8) * arg0) - 1)
                                            arg0 = v6
                                            while True:  # $label14
                                                while True:  # block $label12
                                                    v3 = (arg0 - v9)
                                                    if ((v25 + ((arg0 - v9) * v3)) > 81):
                                                        break
                                                    if (u(arg0) > u(4095)):
                                                        break
                                                    if (load32((v28 + (((((arg0 + v20) + 1) * v20) + v5) << 2))) == 1):
                                                        break
                                                    break
                                                arg0 = (arg0 + 1)
                                                if ((arg0 + 1) != v21):
                                                    continue
                                                break
                                        v12 = (u(v5) >= u(v14))
                                        arg0 = v5
                                        if (v5 != v14):
                                            continue
                                        break
                                    break
                                if (v12 == 0):
                                    break
                            v12 = 0
                            while True:  # $label19
                                while True:  # block $label17
                                    v5 = (v4 + 1)
                                    if (u(v4) <= u(4095)):
                                        arg0 = (v4 - v8)
                                        v4 = (((v4 - v8) * arg0) - 1)
                                        arg0 = v6
                                        while True:  # $label18
                                            while True:  # block $label16
                                                v3 = (arg0 - v9)
                                                if ((v4 + ((arg0 - v9) * v3)) > 81):
                                                    break
                                                if (u(arg0) > u(4095)):
                                                    break
                                                v3 = load32((v28 + (((((arg0 + v20) + 1) * v20) + v5) << 2)))
                                                if (u(load32((v28 + (((((arg0 + v20) + 1) * v20) + v5) << 2)))) < u(3)):
                                                    break
                                                if (v37 == load8u((v38 + (v3 * 132)) + 122)):
                                                    break
                                                break
                                            arg0 = (arg0 + 1)
                                            if ((arg0 + 1) != v21):
                                                continue
                                            break
                                    v12 = (u(v5) >= u(v14))
                                    v4 = v5
                                    if (v5 != v14):
                                        continue
                                    break
                                break
                            if (v12 == 0):
                                break
                            if v19:
                            else:
                            if (0 == v27):
                                break
                            break
                        arg0 = v10
                        v15 = (v15 + 1)
                        if ((v15 + 1) != 2000):
                            continue
                        break
                    break
                    break
                while True:  # $label25
                    v10 = v7
                    store32(9147320, v7)
                    store32(9147324, arg2)
                    arg0 = ((arg0 << 11) ^ arg0)
                    v6 = (((((v7 & 0xFFFFFFFF) >> 19) ^ ((((arg0 << 11) ^ arg0) & 0xFFFFFFFF) >> 8)) ^ v7) ^ arg0)
                    store32(9147316, (((((v7 & 0xFFFFFFFF) >> 19) ^ ((((arg0 << 11) ^ arg0) & 0xFFFFFFFF) >> 8)) ^ v7) ^ arg0))
                    arg0 = ((arg1 << 11) ^ arg1)
                    v7 = (((((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ ((v6 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ v6)
                    store32(9147312, (((((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ ((v6 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ v6))
                    while True:  # block $label23
                        v46 = ((float((v6 % 10000)) * 6.28318548) / 10000.0)
                        v44 = (v45 + float((v7 % v5)))
                        # TODO: f64.promote_f32 []
                        v47 = ((func48(((float((v6 % 10000)) * 6.28318548) / 10000.0)) * (v45 + float((v7 % v5)))) + 0.5)
                        if (abs(((func48(((float((v6 % 10000)) * 6.28318548) / 10000.0)) * (v45 + float((v7 % v5)))) + 0.5)) < 2147483648.0):
                            break
                        break
                    v9 = (-2147483648 + v18)
                    while True:  # block $label24
                        # TODO: f64.promote_f32 []
                        v47 = ((func49(v46) * v44) + 0.5)
                        if (abs(((func49(v46) * v44) + 0.5)) < 2147483648.0):
                            break
                        break
                    v8 = (-2147483648 + v18)
                    if v19:
                    else:
                    if (0 == v27):
                        break
                    arg0 = arg2
                    arg1 = v10
                    arg2 = v6
                    v15 = (v15 + 1)
                    if ((v15 + 1) != 2000):
                        continue
                    break
                break
                break
            while True:  # block $label26
                if (load32(9142872) != v16):
                    break
                if load8u(9142917):
                    break
                store32(v17 + 4, (v9 << 5))
                store32(v17, (v8 << 5))
                v23 = load32(9561692)
                break
            arg0 = (v23 + (v16 * 286704))
            store32((v23 + (v16 * 286704)) + 283900, v9)
            store32(arg0 + 283896, v8)
            store32(arg0 + 283876, v9)
            store32(arg0 + 283872, v8)
            break
        store8(9682192, 0)
        G.global0 = (v17 + 16)
        break
    return func317(v13)

# ------------------------------------------------------------
# $func774
# ------------------------------------------------------------
def func774(arg0, arg1):
    arg1 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v2 = load32(9671128)
    while True:  # block $label0
        if (u(load32(9142848)) < u((load32(load32(9142424) + 72) * 2400))):
            func29((v2 + (arg0 * 132)), 1)
            break
        while True:  # block $label1
            v5 = (arg0 * 132)
            v3 = (v2 + (arg0 * 132))
            if (load8u((v2 + (arg0 * 132)) + 125) == 3):
                break
            if (load8u(v3 + 128) == 0):
                break
            v2 = (v2 + (arg0 * 132))
            store8((v2 + (arg0 * 132)) + 127, 0)
            while True:  # block $label2
                v4 = load32(v2 + 40)
                if (load32(v2 + 40) == 0):
                    break
                if load8u(9142916):
                    store32(arg1 + 20, v4)
                    store32(arg1 + 16, 0)
                    a_b()
                    break
                v2 = load16u(v2 + 110)
                store32(arg1 + 4, v4)
                store32(arg1, (v2 + 16))
                a_b()
                break
            store8(v3 + 128, 0)
            v2 = load32(9671128)
            break
        v2 = (v2 + v5)
        v3 = load16u(v2 + 116)
        v2 = load16u(v2 + 118)
        break
    G.global0 = (arg1 + 32)

# ------------------------------------------------------------
# $func775
# ------------------------------------------------------------
def func775(arg0, arg1):
    v8 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v2 = ((arg1 & 0xFFFFFFFF) >> 16)
    arg1 = (arg1 & 65535)
    v12 = load32(9671128)
    v13 = (load32(9671128) + (arg0 * 132))
    v4 = load16u((load32(9671128) + (arg0 * 132)) + 110)
    v11 = load32(9561692)
    while True:  # block $label0
        if load8u(9142917):
            break
        v6 = load32(9299880)
        if load32(9299880):
            v6 = (v6 - 1)
            store32(9299880, (v6 - 1))
            v6 = load32((load32(9299872) + (v6 << 2)))
            break
        v6 = load32(9163776)
        v5 = (load32(9163776) + 1)
        store32(9163776, (load32(9163776) + 1))
        v9 = load32(9163784)
        if (u(v5) < u(load32(9163784))):
            break
        store32(v8 + 48, v9)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    v14 = (arg1 << 5)
    v15 = (v2 << 5)
    # TODO: f32.convert_i32_u []
    while True:  # block $label1
        v5 = load32(9142572)
        if (load32(9142572) == 0):
            break
        v9 = load32(v5 + 16)
        v5 = load32(v5 + 24)
        if (load32(v5 + 24) >= 100):
            v21 = load32((((v5 + v9) << 2) + 32700))
            if (((load32((((v5 + v9) << 2) + 32700)) < 4294967300.0) & (v21 >= 0.0)) == 0):
                break
            # TODO: i32.trunc_f32_u []
            v3 = v21
            break
        v3 = ((v9 * 1000) // v5)
        break
    while True:  # block $label2
        v6 = (v14 - load32(9142952))
        v6 = (v15 - load32(9142956))
        if (((((v14 - load32(9142952)) * v6) + ((v15 - load32(9142956)) * v6)) - 1) > 9000000):
            break
        v5 = load32(39868)
        while True:  # block $label3
            v9 = load32(load32(9142424) + 48)
            if (load32(load32(9142424) + 48) == 0):
                break
            if load8u(9147152):
                break
            v6 = load16u((load32(9147376) + (((load32(9142440) * v2) + arg1) << 1)))
            if (v9 == 2):
                if (u(v6) > u(1)):
                    break
                break
            if (v6 == 0):
                break
            break
        store32(v8 + 40, v2)
        store32(v8 + 36, arg1)
        store32(v8 + 32, v5)
        a_b()
        break
    while True:  # block $label4
        v6 = (arg1 - 3)
        arg1 = (load32(9561692) + (load16u(v13 + 110) * 286704))
        v5 = load32(((load32(9561692) + (load16u(v13 + 110) * 286704)) + 284180))
        v17 = (v6 + load32(((load32(9561692) + (load16u(v13 + 110) * 286704)) + 284180)))
        if ((arg1 - 3) >= (v6 + load32(((load32(9561692) + (load16u(v13 + 110) * 286704)) + 284180)))):
            break
        v14 = (v2 - 3)
        v18 = (v5 + v14)
        if ((v2 - 3) >= (v5 + v14)):
            break
        v19 = load32((arg1 + 284184))
        arg1 = (v11 + (v4 * 286704))
        v15 = ((v11 + (v4 * 286704)) + 281752)
        v16 = (arg1 + 281780)
        v11 = (v12 + (arg0 * 132))
        v4 = load32(9142440)
        while True:  # $label17
            v12 = (v6 + 1)
            arg0 = v14
            while True:  # $label16
                arg1 = arg0
                arg0 = (arg0 + 1)
                while True:  # block $label5
                    if (u(arg1) >= u(v4)):
                        break
                    if ((arg1 | v6) < 0):
                        break
                    if (u(v4) <= u(v6)):
                        break
                    arg1 = 0
                    v3 = load32(9142840)
                    while True:  # $label15
                        while True:  # block $label6
                            v2 = (v4 + 2)
                            v2 = load32((v3 + ((v12 + ((arg0 + ((v4 + 2) * arg1)) * v2)) << 2)))
                            if (u(load32((v3 + ((v12 + ((arg0 + ((v4 + 2) * arg1)) * v2)) << 2)))) < u(3)):
                                break
                            v2 = (load32(9671128) + (v2 * 132))
                            v7 = load8u((load32(9671128) + (v2 * 132)) + 122)
                            v5 = load32(((load8u((load32(9671128) + (v2 * 132)) + 122) * 404) + 9568096) + 288)
                            if (load32(((load8u((load32(9671128) + (v2 * 132)) + 122) * 404) + 9568096) + 288) == 0):
                                break
                            if (load8u(v2 + 125) == 10):
                                break
                            v3 = load32(9561692)
                            while True:  # block $label7
                                v4 = load32(v2 + 64)
                                v9 = load32((((load8u(v11 + 122) * 1020) + 9299904) + (v7 << 2)))
                                # TODO: i32.div_u []
                                # TODO: i32.div_u []
                                v5 = 100
                                v5 = ((100 * v5) if (u(v4) < u(v5)) else 100)
                                if (((((100 * v5) if (u(v4) < u(v5)) else 100) == v4) & (u(v9) > u(100))) == 0):
                                    v4 = load16u(v2 + 110)
                                    break
                                v10 = load16u(v13 + 110)
                                v4 = (v3 + (load16u(v13 + 110) * 286704))
                                while True:  # block $label8
                                    if (load32(9147132) == 0):
                                        break
                                    if (load32(9671152) != v7):
                                        break
                                    v7 = load16u(v2 + 110)
                                    if (v10 == load16u(v2 + 110)):
                                        break
                                    if (v10 == 0):
                                        break
                                    v3 = (v3 + (v7 * 286704))
                                    v10 = load32((v3 + (v7 * 286704)) + 284628)
                                    v7 = load32(v3 + 284616)
                                    v20 = load32(v4 + 284616)
                                    store32(v8 + 16, (load32(v4 + 284616) if v20 else load32(v4 + 284628)))
                                    store32(v8 + 12, v4)
                                    store32(v8 + 4, v3)
                                    store32(v8, 927)
                                    store32(v8 + 8, (v7 if v7 else v10))
                                    a_b()
                                    break
                                while True:  # block $label9
                                    v3 = load32((v4 + 278560))
                                    if load32((v4 + 278560)):
                                        v4 = load16u(v2 + 110)
                                        v3 = (v3 + ((load8u(v11 + 122) + (load16u(v2 + 110) * 255)) << 2))
                                        store32((v3 + ((load8u(v11 + 122) + (load16u(v2 + 110) * 255)) << 2)), (load32(v3) + 1))
                                        break
                                    v4 = load16u(v2 + 110)
                                    break
                                v3 = load32(9561692)
                                v7 = load32(((load32(9561692) + (v4 * 286704)) + 278568))
                                if load32(((load32(9561692) + (v4 * 286704)) + 278568)):
                                    v7 = (v7 + ((load8u(v2 + 122) + (load16u(v13 + 110) * 255)) << 2))
                                    store32((v7 + ((load8u(v2 + 122) + (load16u(v13 + 110) * 255)) << 2)), (load32(v7) + 1))
                                store16(v2 + 116, load32(v11 + 28))
                                break
                            store32(v16, (load32(v16) + v5))
                            store32(v15, (load32(v15) + 1))
                            v7 = load16u(v13 + 110)
                            v10 = load32((v3 + (load16u(v13 + 110) * 286704)) + 278556)
                            if load32((v3 + (load16u(v13 + 110) * 286704)) + 278556):
                                v10 = (v10 + ((load8u(v11 + 122) + (v4 * 255)) << 2))
                                store32((v10 + ((load8u(v11 + 122) + (v4 * 255)) << 2)), (load32(v10) + v5))
                            v3 = load32(((v3 + (v4 * 286704)) + 278564))
                            if load32(((v3 + (v4 * 286704)) + 278564)):
                                v3 = (v3 + ((load8u(v2 + 122) + (v7 * 255)) << 2))
                                store32((v3 + ((load8u(v2 + 122) + (v7 * 255)) << 2)), (load32(v3) + v5))
                            v3 = (G.global0 - 48)
                            G.global0 = (G.global0 - 48)
                            while True:  # block $label10
                                if (load32(((load8u(v2 + 122) * 404) + 9568096) + 288) == 0):
                                    break
                                v4 = load8u(v2 + 125)
                                if (load8u(v2 + 125) == 10):
                                    break
                                while True:  # block $label11
                                    if (v4 == 3):
                                        break
                                    if (load8u(v2 + 128) == 0):
                                        break
                                    store8(v2 + 127, 0)
                                    while True:  # block $label12
                                        v4 = load32(v2 + 40)
                                        if (load32(v2 + 40) == 0):
                                            break
                                        if load8u(9142916):
                                            store32(v3 + 36, v4)
                                            store32(v3 + 32, 0)
                                            a_b()
                                            break
                                        v7 = load16u(v2 + 110)
                                        store32(v3 + 20, v4)
                                        store32(v3 + 16, (v7 + 16))
                                        a_b()
                                        break
                                    store8(v2 + 128, 0)
                                    break
                                store8(v2 + 127, 2)
                                while True:  # block $label13
                                    if (load8u(9142916) == 0):
                                        break
                                    v4 = load32(v2 + 40)
                                    if (load32(v2 + 40) == 0):
                                        break
                                    store32(v3 + 4, v4)
                                    store32(v3, -419430656)
                                    a_b()
                                    break
                                func119(func60(v2, 1.0), v2, 0, 0)
                                store8(v2 + 125, 9)
                                while True:  # block $label14
                                    v4 = load32(v2 + 64)
                                    if (u(v5) >= u(load32(v2 + 64))):
                                        if (u(v9) < u(101)):
                                            break
                                        store32(v2 + 64, 0)
                                        break
                                    break
                                store32(func32(v2, v2, 0) + 64, (v4 - v5))
                                func63(v3, v2, 20, 0, load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284200)))
                                func77(v2)
                                break
                            G.global0 = (v3 + 48)
                            func103(v2)
                            v3 = load32(9142840)
                            v4 = load32(9142440)
                            break
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != 3):
                            continue
                        break
                    break
                if (arg0 != v18):
                    continue
                break
            v6 = v12
            if (v12 != v17):
                continue
            break
        break
    G.global0 = (v8 - -64)
    return 1061

# ------------------------------------------------------------
# $func776
# ------------------------------------------------------------
def func776(arg0, arg1):
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = load32(9671128)
    v2 = (load32(9671128) + (arg0 * 132))
    while True:  # block $label0
        if (u(load32(9142848)) < u((load32(load32(9142424) + 72) * 2400))):
            func29(v2, 1)
            break
        while True:  # block $label1
            if (load8u(v2 + 125) == 3):
                break
            arg1 = (v3 + (arg0 * 132))
            if (load8u((v3 + (arg0 * 132)) + 128) == 0):
                break
            store8(arg1 + 127, 0)
            while True:  # block $label2
                v5 = load32(arg1 + 40)
                if (load32(arg1 + 40) == 0):
                    break
                if load8u(9142916):
                    store32(v4 + 36, v5)
                    store32(v4 + 32, 0)
                    a_b()
                    break
                v6 = load16u(arg1 + 110)
                store32(v4 + 20, v5)
                store32(v4 + 16, (v6 + 16))
                a_b()
                break
            store8(arg1 + 128, 0)
            break
        v3 = (v3 + (arg0 * 132))
        while True:  # block $label3
            arg1 = load16u(v3 + 112)
            v2 = ((load16u(v3 + 112) << 5) - load32(9142952))
            v2 = load16u(v3 + 114)
            v5 = ((load16u(v3 + 114) << 5) - load32(9142956))
            if ((((((load16u(v3 + 112) << 5) - load32(9142952)) * v2) + (((load16u(v3 + 114) << 5) - load32(9142956)) * v5)) - 1) > 9000000):
                break
            v6 = load32(39872)
            while True:  # block $label4
                v7 = load32(load32(9142424) + 48)
                if (load32(load32(9142424) + 48) == 0):
                    break
                if load8u(9147152):
                    break
                v5 = load16u((load32(9147376) + (((load32(9142440) * v2) + arg1) << 1)))
                if (v7 == 2):
                    if (u(v5) > u(1)):
                        break
                    break
                if (v5 == 0):
                    break
                break
            store32(v4 + 8, v2)
            store32(v4 + 4, arg1)
            store32(v4, v6)
            a_b()
            v2 = load16u(v3 + 114)
            arg1 = load16u(v3 + 112)
            break
        v8 = 3.0
        # TODO: f32.convert_i32_u []
        # TODO: f32.convert_i32_u []
        v15 = (arg1 & 65535)
        v10 = (load16u(v3 + 116) - (arg1 & 65535))
        # TODO: f32.convert_i32_u []
        # TODO: f32.convert_i32_u []
        v16 = (v2 & 65535)
        v9 = (load16u(v3 + 118) - (v2 & 65535))
        v12 = sqrt((((load16u(v3 + 116) - (arg1 & 65535)) * v10) + ((load16u(v3 + 118) - (v2 & 65535)) * v9)))
        if ((sqrt((((load16u(v3 + 116) - (arg1 & 65535)) * v10) + ((load16u(v3 + 118) - (v2 & 65535)) * v9))) > 3.0) == 0):
            break
        v9 = (v9 / v12)
        v14 = (v10 / v12)
        v3 = load32(9142440)
        while True:  # $label19
            while True:  # block $label5
                v10 = ((v14 * v8) + v15)
                # TODO: f64.promote_f32 []
                v17 = (((v14 * v8) + v15) + 0.5)
                if (abs((((v14 * v8) + v15) + 0.5)) < 2147483648.0):
                    break
                break
            v2 = -2147483648
            while True:  # block $label7
                while True:  # block $label6
                    v13 = ((v9 * v8) + v16)
                    # TODO: f64.promote_f32 []
                    v17 = (((v9 * v8) + v16) + 0.5)
                    if (abs((((v9 * v8) + v16) + 0.5)) < 2147483648.0):
                        break
                    break
                arg1 = -2147483648
                if (u(-2147483648) >= u(v3)):
                    break
                if ((arg1 | v2) < 0):
                    break
                if (u(v2) >= u(v3)):
                    break
                v2 = ((arg1 << 16) + v2)
                while True:  # block $label8
                    if ((v8 < 4294967300.0) & (v8 >= 0.0)):
                        # TODO: i32.trunc_f32_u []
                        break
                    break
                arg1 = (0 * 50)
                while True:  # block $label9
                    v11 = (v13 * 32.0)
                    if (((v13 * 32.0) < 4294967300.0) & (v11 >= 0.0)):
                        # TODO: i32.trunc_f32_u []
                        break
                    break
                v3 = 0
                while True:  # block $label10
                    v11 = (v10 * 32.0)
                    if (((v10 * 32.0) < 4294967300.0) & (v11 >= 0.0)):
                        # TODO: i32.trunc_f32_u []
                        break
                    break
                v3 = load32(9142440)
                break
            while True:  # block $label11
                # TODO: f64.promote_f32 []
                v17 = ((v9 + v10) + 0.5)
                if (abs(((v9 + v10) + 0.5)) < 2147483648.0):
                    break
                break
            v2 = -2147483648
            while True:  # block $label13
                while True:  # block $label12
                    # TODO: f64.promote_f32 []
                    v17 = ((v14 + v13) + 0.5)
                    if (abs(((v14 + v13) + 0.5)) < 2147483648.0):
                        break
                    break
                arg1 = -2147483648
                if (u(-2147483648) >= u(v3)):
                    break
                if ((arg1 | v2) < 0):
                    break
                if (u(v2) >= u(v3)):
                    break
                v2 = ((arg1 << 16) + v2)
                while True:  # block $label14
                    if ((v8 < 4294967300.0) & (v8 >= 0.0)):
                        # TODO: i32.trunc_f32_u []
                        break
                    break
                v3 = load32(9142440)
                break
            while True:  # block $label15
                # TODO: f64.promote_f32 []
                v17 = ((v10 - v9) + 0.5)
                if (abs(((v10 - v9) + 0.5)) < 2147483648.0):
                    break
                break
            v2 = -2147483648
            while True:  # block $label17
                while True:  # block $label16
                    # TODO: f64.promote_f32 []
                    v17 = ((v13 - v9) + 0.5)
                    if (abs(((v13 - v9) + 0.5)) < 2147483648.0):
                        break
                    break
                arg1 = -2147483648
                if (u(-2147483648) >= u(v3)):
                    break
                if ((arg1 | v2) < 0):
                    break
                if (u(v2) >= u(v3)):
                    break
                v2 = ((arg1 << 16) + v2)
                while True:  # block $label18
                    if ((v8 < 4294967300.0) & (v8 >= 0.0)):
                        # TODO: i32.trunc_f32_u []
                        break
                    break
                v3 = load32(9142440)
                break
            v8 = (v8 + 1.0)
            if ((v8 + 1.0) < v12):
                continue
            break
        break
    G.global0 = (v4 + 48)
    return v8

# ------------------------------------------------------------
# $func777
# ------------------------------------------------------------
def func777(arg0, arg1):
    v9 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = load32(9671128)
    arg0 = (load32(9671128) + (arg0 * 132))
    v7 = ((load32(9561692) + (load16u((load32(9671128) + (arg0 * 132)) + 110) * 286704)) + 281776)
    while True:  # block $label0
        v10 = ((arg1 & 65535) + 1)
        v11 = (((arg1 & 0xFFFFFFFF) >> 16) + 1)
        v5 = load32((load32(9142840) + ((((arg1 & 65535) + 1) + ((((arg1 & 0xFFFFFFFF) >> 16) + 1) * (load32(9142440) + 2))) << 2)))
        if (u(load32((load32(9142840) + ((((arg1 & 65535) + 1) + ((((arg1 & 0xFFFFFFFF) >> 16) + 1) * (load32(9142440) + 2))) << 2)))) < u(3)):
            break
        arg1 = (v3 + (v5 * 132))
        v2 = load32(((load8u((v3 + (v5 * 132)) + 122) * 404) + 9568096) + 292)
        if (load32(((load8u((v3 + (v5 * 132)) + 122) * 404) + 9568096) + 292) == 0):
            break
        v8 = load8u(arg1 + 125)
        if (load8u(arg1 + 125) == 10):
            break
        v2 = (v2 * 96)
        # TODO: i32.div_u []
        v4 = ((v2 * 96) if (u(v2) < u(100)) else 100)
        v12 = (v3 + (v5 * 132))
        v6 = load32((v3 + (v5 * 132)) + 64)
        v2 = (((v2 * 96) if (u(v2) < u(100)) else 100) if (u(v4) < u(v6)) else load32((v3 + (v5 * 132)) + 64))
        while True:  # block $label1
            if (v8 == 3):
                break
            v8 = (v12 - -64)
            if (u(v4) < u(v6)):
                store32(v8, (v6 - v2))
                if (load32((v3 + (v5 * 132)) + 92) == 0):
                    break
                if load8u(9147141):
                    break
                store32(v9 + 32, v2)
                a_b()
                break
            store32(v8, 0)
            func155(arg0, arg1, 0)
            break
        func103(arg1)
        store32(v7, (load32(v7) + v2))
        v3 = load16u(v12 + 110)
        v5 = load32(9561692)
        v6 = load16u(arg0 + 110)
        v4 = load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 278556)
        if load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 278556):
            v4 = (v4 + ((load8u(arg0 + 122) + (v3 * 255)) << 2))
            store32((v4 + ((load8u(arg0 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
        v3 = load32(((v5 + (v3 * 286704)) + 278564))
        if (load32(((v5 + (v3 * 286704)) + 278564)) == 0):
            break
        arg1 = (v3 + ((load8u(arg1 + 122) + (v6 * 255)) << 2))
        store32((v3 + ((load8u(arg1 + 122) + (v6 * 255)) << 2)), (load32(arg1) + v2))
        break
    while True:  # block $label2
        arg1 = (load32(9142440) + 2)
        v3 = load32((load32(9142840) + ((v10 + ((v11 + (load32(9142440) + 2)) * arg1)) << 2)))
        if (u(load32((load32(9142840) + ((v10 + ((v11 + (load32(9142440) + 2)) * arg1)) << 2)))) < u(3)):
            break
        v6 = load32(9671128)
        arg1 = (load32(9671128) + (v3 * 132))
        v2 = load32(((load8u((load32(9671128) + (v3 * 132)) + 122) * 404) + 9568096) + 292)
        if (load32(((load8u((load32(9671128) + (v3 * 132)) + 122) * 404) + 9568096) + 292) == 0):
            break
        v8 = load8u(arg1 + 125)
        if (load8u(arg1 + 125) == 10):
            break
        v2 = (v2 * 96)
        # TODO: i32.div_u []
        v4 = ((v2 * 96) if (u(v2) < u(100)) else 100)
        v12 = (v6 + (v3 * 132))
        v5 = load32((v6 + (v3 * 132)) + 64)
        v2 = (((v2 * 96) if (u(v2) < u(100)) else 100) if (u(v4) < u(v5)) else load32((v6 + (v3 * 132)) + 64))
        while True:  # block $label3
            if (v8 == 3):
                break
            v8 = (v12 - -64)
            if (u(v4) >= u(v5)):
                store32(v8, 0)
                func155(arg0, arg1, 0)
                break
            store32(v8, (v5 - v2))
            if (load32((v6 + (v3 * 132)) + 92) == 0):
                break
            if load8u(9147141):
                break
            store32(v9 + 16, v2)
            a_b()
            break
        func103(arg1)
        store32(v7, (load32(v7) + v2))
        v3 = load16u(v12 + 110)
        v5 = load32(9561692)
        v6 = load16u(arg0 + 110)
        v4 = load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 278556)
        if load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 278556):
            v4 = (v4 + ((load8u(arg0 + 122) + (v3 * 255)) << 2))
            store32((v4 + ((load8u(arg0 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
        v3 = load32(((v5 + (v3 * 286704)) + 278564))
        if (load32(((v5 + (v3 * 286704)) + 278564)) == 0):
            break
        arg1 = (v3 + ((load8u(arg1 + 122) + (v6 * 255)) << 2))
        store32((v3 + ((load8u(arg1 + 122) + (v6 * 255)) << 2)), (load32(arg1) + v2))
        break
    while True:  # block $label4
        arg1 = (load32(9142440) + 2)
        v3 = load32((load32(9142840) + ((v10 + ((v11 + ((load32(9142440) + 2) << 1)) * arg1)) << 2)))
        if (u(load32((load32(9142840) + ((v10 + ((v11 + ((load32(9142440) + 2) << 1)) * arg1)) << 2)))) < u(3)):
            break
        v6 = load32(9671128)
        arg1 = (load32(9671128) + (v3 * 132))
        v2 = load32(((load8u((load32(9671128) + (v3 * 132)) + 122) * 404) + 9568096) + 292)
        if (load32(((load8u((load32(9671128) + (v3 * 132)) + 122) * 404) + 9568096) + 292) == 0):
            break
        v4 = load8u(arg1 + 125)
        if (load8u(arg1 + 125) == 10):
            break
        v2 = (v2 * 96)
        # TODO: i32.div_u []
        v10 = ((v2 * 96) if (u(v2) < u(100)) else 100)
        v11 = (v6 + (v3 * 132))
        v5 = load32((v6 + (v3 * 132)) + 64)
        v2 = (((v2 * 96) if (u(v2) < u(100)) else 100) if (u(v5) > u(v10)) else load32((v6 + (v3 * 132)) + 64))
        while True:  # block $label5
            if (v4 == 3):
                break
            v4 = (v11 - -64)
            if (u(v5) <= u(v10)):
                store32(v4, 0)
                func155(arg0, arg1, 0)
                break
            store32(v4, (v5 - v2))
            if (load32((v6 + (v3 * 132)) + 92) == 0):
                break
            if load8u(9147141):
                break
            store32(v9, v2)
            a_b()
            break
        func103(arg1)
        store32(v7, (load32(v7) + v2))
        v7 = load16u(v11 + 110)
        v3 = load32(9561692)
        v5 = load16u(arg0 + 110)
        v6 = load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 278556)
        if load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 278556):
            arg0 = (v6 + ((load8u(arg0 + 122) + (v7 * 255)) << 2))
            store32((v6 + ((load8u(arg0 + 122) + (v7 * 255)) << 2)), (load32(arg0) + v2))
        arg0 = load32(((v3 + (v7 * 286704)) + 278564))
        if (load32(((v3 + (v7 * 286704)) + 278564)) == 0):
            break
        arg0 = (arg0 + ((load8u(arg1 + 122) + (v5 * 255)) << 2))
        store32((arg0 + ((load8u(arg1 + 122) + (v5 * 255)) << 2)), (load32(arg0) + v2))
        break
    G.global0 = (v9 + 48)

# ------------------------------------------------------------
# $func778
# ------------------------------------------------------------
def func778(arg0, arg1, param2):
    while True:  # block $label0
        v5 = load32(9671128)
        v3 = (load32(9671128) + (arg0 * 132))
        if (load8u((load32(9671128) + (arg0 * 132)) + 125) == 1):
            store16(v3 + 108, 0)
            store32(v3 + 88, 0)
            v2 = load32(((load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) * 40) + 9671200) + 32):
                # call_indirect[v2]
            if (load8u(v3 + 125) == 3):
                break
            v4 = load32(v3 + 44)
            if load32(v3 + 44):
                v6 = load32(9142848)
                v2 = load32(9215884)
                store32((load32(9215884) + (v4 << 4)) + 4, 55)
                store32((v2 + (load32(v3 + 44) << 4)) + 8, load32((v5 + (arg0 * 132)) + 28))
                store32((v2 + (load32(v3 + 44) << 4)) + 12, arg1)
                store32((v2 + (load32(v3 + 44) << 4)), (v6 + 80))
                return
            store32(v3 + 44, ((Ua(2000, 55, load32((v5 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            return
        if (load8u((v5 + (arg1 * 132)) + 125) == 3):
            func29(v3, 1)
            return
        v2 = (v5 + (arg0 * 132))
        v4 = (load32(9561692) + (load16u(v2 + 110) * 286704))
        v6 = (load16u(v2 + 108) + load16u(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284328)))
        store16((v5 + (arg0 * 132)) + 108, (load16u(v2 + 108) + load16u(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284328))))
        v4 = load32((v4 + 284332))
        if (u(load32((v4 + 284332))) <= u((v6 & 65535))):
            store16(v2 + 108, v4)
            store32(v2 + 88, 2)
            func207(v3, load32((v5 + (arg1 * 132)) + 28))
            v15 = load16u(v2 + 110)
            v9 = load16u(v2 + 112)
            v16 = (load16u(v2 + 112) + 149)
            v10 = load16u(v2 + 114)
            v17 = (load16u(v2 + 114) + 149)
            v18 = (v10 - 75)
            v2 = (v9 - 75)
            v11 = load32(9142440)
            v12 = (load32(9142440) + 2)
            v19 = load32(38872)
            v20 = load32(38796)
            v21 = load32(38584)
            v22 = load32(9671128)
            v23 = load32(9142840)
            v6 = 2147483647
            while True:  # $label5
                v13 = (v2 + 1)
                if (u(v2) < u(v11)):
                    arg1 = (v2 - v9)
                    v24 = ((v2 - v9) * arg1)
                    arg1 = v18
                    while True:  # $label4
                        while True:  # block $label1
                            v4 = arg1
                            arg1 = (arg1 - v10)
                            arg1 = (((arg1 - v10) * arg1) + v24)
                            if (((((arg1 - v10) * arg1) + v24) - 1) > 5625):
                                break
                            if (u(v4) >= u(v11)):
                                break
                            if ((v2 | v4) < 0):
                                break
                            if (arg1 >= v6):
                                break
                            v7 = (v22 + (load32((v23 + ((v13 + (((v4 + v12) + 1) * v12)) << 2))) * 132))
                            if (load16u((v22 + (load32((v23 + ((v13 + (((v4 + v12) + 1) * v12)) << 2))) * 132)) + 110) != v15):
                                break
                            while True:  # block $label2
                                # br_table[(load8u(v7 + 125) - 4)]
                                break
                                break
                            while True:  # block $label3
                                v14 = load8u(v7 + 122)
                                if (v21 == load8u(v7 + 122)):
                                    break
                                if (v14 == v20):
                                    break
                                if (v14 != v19):
                                    break
                                break
                            v8 = load32(v7 + 28)
                            v6 = arg1
                            break
                        arg1 = (v4 + 1)
                        if (v4 < v17):
                            continue
                        break
                arg1 = (v2 < v16)
                v2 = v13
                if arg1:
                    continue
                break
            while True:  # block $label6
                arg1 = v8
                if v8:
                    break
                func29(v3, 1)
                break
            if (load32((v5 + (arg0 * 132)) + 92) == 0):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v5 + (arg0 * 132)) + 28)):
                    break
            return
        while True:  # block $label7
            if (load32(v2 + 92) == 0):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v5 + (arg0 * 132)) + 28)):
                    break
            break
        store32((load32(9215884) + (load32((v5 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 80))
        break

# ------------------------------------------------------------
# $func780
# ------------------------------------------------------------
def func780(arg0, arg1):
    arg1 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v2 = load32(9671128)
    while True:  # block $label0
        if (u(load32(9142848)) < u((load32(load32(9142424) + 72) * 2400))):
            func29((v2 + (arg0 * 132)), 1)
            break
        while True:  # block $label1
            v5 = (arg0 * 132)
            v3 = (v2 + (arg0 * 132))
            if (load8u((v2 + (arg0 * 132)) + 125) == 3):
                break
            if (load8u(v3 + 128) == 0):
                break
            v2 = (v2 + (arg0 * 132))
            store8((v2 + (arg0 * 132)) + 127, 0)
            while True:  # block $label2
                v4 = load32(v2 + 40)
                if (load32(v2 + 40) == 0):
                    break
                if load8u(9142916):
                    store32(arg1 + 20, v4)
                    store32(arg1 + 16, 0)
                    a_b()
                    break
                v2 = load16u(v2 + 110)
                store32(arg1 + 4, v4)
                store32(arg1, (v2 + 16))
                a_b()
                break
            store8(v3 + 128, 0)
            v2 = load32(9671128)
            break
        v2 = (v2 + v5)
        v3 = load16u(v2 + 116)
        v4 = load16u(v2 + 118)
        v3 = (load32(9561692) + (load16u(v2 + 110) * 286704))
        v6 = load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284364))
        v11 = (v3 - load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284364)))
        v2 = (v6 << 1)
        v13 = (v6 << 1)
        v14 = load32((v3 + 284368))
        v12 = load32((v3 + 284360))
        if load32((v3 + 284360)):
            v15 = v2
            v16 = arg0
            v17 = (v4 - v6)
            v18 = (v6 + (v4 - v6))
            v19 = (v6 + v11)
            v8 = load32(9142440)
            v5 = load32(9147316)
            v3 = load32(9147320)
            arg0 = load32(9147312)
            v4 = load32(9147324)
            v20 = (v6 * v6)
            while True:  # $label5
                store32(9147320, arg0)
                v2 = v5
                store32(9147324, v5)
                v4 = ((v4 << 11) ^ v4)
                v5 = (((((arg0 & 0xFFFFFFFF) >> 19) ^ ((((v4 << 11) ^ v4) & 0xFFFFFFFF) >> 8)) ^ arg0) ^ v4)
                store32(9147316, (((((arg0 & 0xFFFFFFFF) >> 19) ^ ((((v4 << 11) ^ v4) & 0xFFFFFFFF) >> 8)) ^ arg0) ^ v4))
                v3 = ((v3 << 11) ^ v3)
                v4 = (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v5 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v5)
                store32(9147312, (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v5 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v5))
                v3 = (v5 % v13)
                while True:  # block $label4
                    while True:  # block $label3
                        v9 = ((v4 % v15) + v17)
                        if (u(v8) <= u(((v4 % v15) + v17))):
                            break
                        v10 = (v3 + v11)
                        if (u(v8) <= u((v3 + v11))):
                            break
                        if ((v9 | v10) < 0):
                            break
                        if v6:
                            v3 = arg0
                            arg0 = v4
                            v4 = v2
                            v2 = (v10 - v19)
                            v2 = (v9 - v18)
                            if (((((v10 - v19) * v2) + ((v9 - v18) * v2)) - 1) > v20):
                                break
                        # TODO: i32.div_u []
                        v8 = load32(9142440)
                        v5 = load32(9147316)
                        v3 = load32(9147320)
                        arg0 = load32(9147312)
                        v4 = load32(9147324)
                        break
                        break
                    v3 = arg0
                    arg0 = v4
                    v4 = v2
                    break
                v7 = (v7 + 1)
                if ((v7 + 1) != v12):
                    continue
                break
        break
    G.global0 = (arg1 + 32)

# ------------------------------------------------------------
# $func781
# ------------------------------------------------------------
def func781(arg0, arg1):
    v2 = load32(9671128)
    arg0 = (load32(9671128) + (arg0 * 132))
    func29((load32(9671128) + (arg0 * 132)), 1)
    arg1 = (v2 + (arg1 * 132))
    if (load8u((v2 + (arg1 * 132)) + 125) != 10):
        # TODO: i32.div_u []

# ------------------------------------------------------------
# $func783
# ------------------------------------------------------------
def func783(arg0):
    while True:  # block $label0
        arg0 = (load32(9671128) + (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12) * 132))
        if (load32(38528) != load8u((load32(9671128) + (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12) * 132)) + 122)):
            break
        if (load8u(arg0 + 125) == 3):
            break
        store8(arg0 + 125, 0)
        break

# ------------------------------------------------------------
# $func784
# ------------------------------------------------------------
def func784(arg0):
    v1 = (load32(9671128) + (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12) * 132))
    if (load32((load32(9671128) + (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12) * 132)) + 100) == load32(arg0 + 28)):
        store32(v1 + 100, 0)

# ------------------------------------------------------------
# $func785
# ------------------------------------------------------------
def func785(arg0, arg1, arg2):
    if arg2:
        arg0 = 0
        while True:  # $label0
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break

# ------------------------------------------------------------
# $func786
# ------------------------------------------------------------
def func786(arg0, arg1, arg2, arg3, arg4):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label5
        while True:  # block $label0
            arg4 = load32(9142832)
            if (load32(9142832) == 0):
                if (load32(load32(9142424) + 48) == 0):
                    break
            while True:  # block $label3
                while True:  # block $label4
                    while True:  # block $label2
                        while True:  # block $label1
                            v7 = load8u((load32(9671128) + (arg0 * 132)) + 122)
                            v8 = load32(((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096) + 212)
                            # br_table[load32(((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096) + 212)]
                            break
                            break
                        arg0 = load32(arg2)
                        v6 = load32(arg3)
                        v5 = (load32(9142440) + 2)
                        if (load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + (load32(9142440) + 2)) + 1) * v5)) << 2)) + 4) != 1):
                            break
                        break
                        break
                    arg0 = load32(arg2)
                    v6 = load32(arg3)
                    v5 = (load32(9142440) + 2)
                    if (u((load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + (load32(9142440) + 2)) + 1) * v5)) << 2)) + 4) - 3)) >= u(-2)):
                        break
                    break
                store32(arg1 + 12, arg0)
                store32(arg1 + 8, v6)
                if (func167((arg1 + 12), (arg1 + 8), 1, v8, load32(((v7 * 404) + 9568096) + 216)) == 0):
                    break
                store32(arg2, load32(arg1 + 12))
                store32(arg3, load32(arg1 + 8))
                arg4 = load32(9142832)
                break
            if arg4:
                break
            break
        break
    arg0 = (load32(load32(9142424) + 48) == 0)
    G.global0 = (arg1 + 16)
    return arg0

# ------------------------------------------------------------
# $func787
# ------------------------------------------------------------
def func787(arg0):
    v12 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        if (load32(9142872) != load16u(arg0 + 110)):
            break
        v22 = load16u(arg0 + 114)
        v33 = load16u(arg0 + 118)
        v1 = (load16u(arg0 + 114) - load16u(arg0 + 118))
        v23 = load16u(arg0 + 112)
        v34 = load16u(arg0 + 116)
        v1 = (load16u(arg0 + 112) - load16u(arg0 + 116))
        if (u((((load16u(arg0 + 114) - load16u(arg0 + 118)) * v1) + ((load16u(arg0 + 112) - load16u(arg0 + 116)) * v1))) > u(4)):
            break
        v26 = ((load8u(arg0 + 124) & 0xFFFFFFFF) >> 1)
        v13 = load32(9142440)
        v24 = (load32(9142440) + 2)
        v25 = load8u(arg0 + 122)
        v1 = ((load8u(arg0 + 122) * 404) + 9568096)
        v18 = ((load8u(arg0 + 122) * 404) + 9568096)
        v10 = load32(v1 + 200)
        v15 = (load32(v1 + 200) << 1)
        v17 = load32(v1 + 216)
        v30 = load32(v1 + 212)
        v27 = (v10 * v10)
        v31 = load32(9147376)
        v32 = load32(9142840)
        v8 = v22
        v9 = v23
        while True:  # block $label25
            while True:  # $label26
                v14 = 0
                v5 = 0
                v6 = 0
                while True:  # $label10
                    v1 = (v6 << 3)
                    v7 = (load32(((v6 << 3) + 8992)) + v9)
                    while True:  # block $label4
                        v11 = (load32((v1 + 8996)) + v8)
                        v4 = (v17 + (load32((v1 + 8996)) + v8))
                        if ((v17 + (load32((v1 + 8996)) + v8)) > v11):
                            v1 = (v7 + v17)
                            v19 = (v7 if (v1 < v7) else (v7 + v17))
                            v20 = (v24 * load32(v18 + 208))
                            v3 = 0
                            v1 = v11
                            while True:  # $label3
                                v1 = (v1 + 1)
                                v21 = (((v1 + 1) + v20) * v24)
                                v2 = v7
                                while True:  # block $label2
                                    while True:  # $label1
                                        if (v2 != v19):
                                            v2 = (v2 + 1)
                                            if (load32((v32 + (((v2 + 1) + v21) << 2))) == v30):
                                                continue
                                            break
                                        break
                                    v3 = (v1 >= v4)
                                    if (v1 != v4):
                                        continue
                                    break
                                break
                            if ((v3 & 1) == 0):
                                break
                        v3 = 0
                        while True:  # block $label9
                            while True:  # block $label5
                                v4 = (v7 - v10)
                                v19 = (v7 + v15)
                                if ((v7 - v10) >= (v7 + v15)):
                                    break
                                v1 = (v11 - v10)
                                v20 = (v11 + v15)
                                if ((v11 - v10) >= (v11 + v15)):
                                    break
                                while True:  # $label8
                                    if (u(v4) < u(v13)):
                                        v2 = (v4 - v7)
                                        v21 = (((v4 - v7) * v2) - 1)
                                        v2 = v1
                                        while True:  # $label7
                                            while True:  # block $label6
                                                v28 = (v2 - v11)
                                                if ((v21 + ((v2 - v11) * v28)) > v27):
                                                    break
                                                if (u(v2) >= u(v13)):
                                                    break
                                                if ((v2 | v4) < 0):
                                                    break
                                                v3 = (v3 + (load16u((v31 + (((v2 * v13) + v4) << 1))) == 0))
                                                break
                                            v2 = (v2 + 1)
                                            if ((v2 + 1) != v20):
                                                continue
                                            break
                                    v4 = (v4 + 1)
                                    if ((v4 + 1) != v19):
                                        continue
                                    break
                                if (u(v3) > u(v5)):
                                    break
                                break
                            if (v3 != v5):
                                break
                            if (((v14 & 0xFFFFFFFF) >> 1) != v26):
                                break
                            break
                        v5 = v3
                        v14 = v6
                        break
                    v6 = (v6 + 1)
                    if ((v6 + 1) != 8):
                        continue
                    break
                while True:  # block $label18
                    if (v5 == 0):
                        v4 = (v8 + 2)
                        v14 = (v9 + 2)
                        v7 = (v8 - 1)
                        v11 = (v9 - 1)
                        v26 = load32(v18 + 208)
                        v27 = (v24 * load32(v18 + 208))
                        v25 = ((v25 * 404) + 9568096)
                        v10 = load32(9142432)
                        v19 = (load32(9142432) + (((v13 * v22) + v23) << 2))
                        v18 = load32(9215880)
                        v16 = 1
                        while True:  # $label24
                            while True:  # block $label11
                                if (v11 >= v14):
                                    break
                                if (v4 <= v7):
                                    break
                                v20 = (v14 - 1)
                                v21 = (v4 - 1)
                                v1 = v11
                                while True:  # $label23
                                    if (u(v1) < u(v13)):
                                        v28 = (v1 == v20)
                                        v35 = (v1 == v11)
                                        v2 = (v1 + v17)
                                        v36 = (v1 if (v1 > v2) else (v1 + v17))
                                        v3 = v7
                                        while True:  # $label22
                                            while True:  # block $label12
                                                if ((v28 | ((v35 | (v3 == v7)) | (v3 == v21))) == 0):
                                                    break
                                                if (u(v3) >= u(v13)):
                                                    break
                                                if ((v1 | v3) < 0):
                                                    break
                                                v2 = 1
                                                if (u(v26) <= u(1)):
                                                    if v10:
                                                    else:
                                                    v15 = 0
                                                    while True:  # block $label15
                                                        while True:  # block $label14
                                                            while True:  # block $label13
                                                                # br_table[load32(v25 + 264)]
                                                                break
                                                                break
                                                            if (v10 == 0):
                                                                v5 = 0
                                                                break
                                                            v5 = load32(v19)
                                                            break
                                                            break
                                                        v5 = 0
                                                        if (v17 == 0):
                                                            break
                                                        if (v10 == 0):
                                                            break
                                                        v29 = load32(v25 + 220)
                                                        if (load32(v25 + 220) == 0):
                                                            break
                                                        if (v18 == 0):
                                                            break
                                                        v37 = load32(v18)
                                                        v6 = 0
                                                        while True:  # $label17
                                                            v38 = (v6 + v23)
                                                            v2 = 0
                                                            while True:  # $label16
                                                                v5 = load32((v10 + ((v38 + ((v2 + v22) * v13)) << 2)))
                                                                if (load32((v37 + (load32((v10 + ((v38 + ((v2 + v22) * v13)) << 2))) << 2))) == 0):
                                                                    break
                                                                v2 = (v2 + 1)
                                                                if ((v2 + 1) != v29):
                                                                    continue
                                                                break
                                                            v5 = 0
                                                            v6 = (v6 + 1)
                                                            if ((v6 + 1) != v17):
                                                                continue
                                                            break
                                                        break
                                                else:
                                                if (1 == 0):
                                                    break
                                                if load16u((v31 + (((v3 * v13) + v1) << 1))):
                                                    break
                                                v5 = 0
                                                v6 = v3
                                                v15 = (v3 + v17)
                                                if ((v3 + v17) <= v3):
                                                    break
                                                while True:  # $label21
                                                    v6 = (v6 + 1)
                                                    v29 = (((v6 + 1) + v27) * v24)
                                                    v2 = v1
                                                    while True:  # block $label20
                                                        while True:  # $label19
                                                            if (v2 != v36):
                                                                v2 = (v2 + 1)
                                                                if (load32((v32 + (((v2 + 1) + v29) << 2))) == v30):
                                                                    continue
                                                                break
                                                            break
                                                        v5 = (v6 >= v15)
                                                        if (v6 != v15):
                                                            continue
                                                        break
                                                    break
                                                if (v5 & 1):
                                                    break
                                                break
                                            v3 = (v3 + 1)
                                            if ((v3 + 1) != v4):
                                                continue
                                            break
                                    v1 = (v1 + 1)
                                    if ((v1 + 1) != v14):
                                        continue
                                    break
                                break
                            v4 = (v4 + 1)
                            v14 = (v14 + 1)
                            v16 = (v16 + 1)
                            v7 = (v8 - (v16 + 1))
                            v11 = (v9 - v16)
                            if (v16 != 250):
                                continue
                            break
                        break
                    v1 = (v14 << 3)
                    v8 = (load32(((v14 << 3) + 8996)) + v8)
                    v9 = (load32((v1 + 8992)) + v9)
                    v16 = (v16 + 1)
                    if ((v16 + 1) != 8):
                        continue
                    break
                    break
                break
            v9 = v1
            v8 = v3
            break
        if ((v9 == v34) & (v8 == v33)):
            break
        if ((v9 == v23) & (v8 == v22)):
            break
        if load8u(9147210):
            store32(v12 + 40, 0)
            store64(v12 + 32, 0)
            store64(v12 + 24, 270582939648)
            store32(v12 + 20, v8)
            store32(v12 + 16, v9)
            store32(v12 + 12, load32(arg0 + 28))
            func41(5, (v12 + 12), 1, (v12 + 16), 7)
            break
        store16(arg0 + 118, v8)
        store16(arg0 + 116, v9)
        break
    G.global0 = (v12 + 48)
    return 0

# ------------------------------------------------------------
# $func788
# ------------------------------------------------------------
def func788(arg0, arg1):
    while True:  # block $label0
        if (load8u(arg1 + 125) == 3):
            break
        while True:  # block $label18
            if (load32(arg0 + 8) == 0):
                if (u(load32(arg0 + 104)) < u(7)):
                    break
                v2 = load32(arg0 + 96)
                v4 = load32(arg1 + 76)
                v3 = load32(arg1 + 76)
                while True:  # block $label6
                    while True:  # block $label5
                        while True:  # block $label4
                            while True:  # block $label3
                                while True:  # block $label2
                                    while True:  # block $label1
                                        v5 = load32(arg0 + 16)
                                        # br_table[load32(arg0 + 16)]
                                        break
                                        break
                                    arg0 = load32(v2)
                                    if (load32(v2) != 2147483647):
                                        store32(arg1 + 52, arg0)
                                    arg0 = load32(v2 + 4)
                                    if (load32(v2 + 4) != 2147483647):
                                        store32(arg1 + 60, arg0)
                                    while True:  # block $label7
                                        arg0 = load32(v2 + 8)
                                        if (load32(v2 + 8) == 2147483647):
                                            break
                                        store32(arg1 + 64, arg0)
                                        if (load32(v2 + 8) == 2147483647):
                                            break
                                        store32(arg1 + 68, load32(v2 + 12))
                                        break
                                    while True:  # block $label8
                                        arg0 = load32(v2 + 16)
                                        if (load32(v2 + 16) == 2147483647):
                                            break
                                        store32(arg1 + 72, arg0)
                                        if (load32(v2 + 16) == 2147483647):
                                            break
                                        v3 = load32(v2 + 20)
                                        store32(arg1 + 76, load32(v2 + 20))
                                        break
                                    arg0 = load32(v2 + 24)
                                    if (load32(v2 + 24) == 2147483647):
                                        break
                                    store32(arg1 + 84, arg0)
                                    break
                                    break
                                arg0 = load32(v2)
                                if (load32(v2) != 2147483647):
                                    store32(arg1 + 52, (load32(arg1 + 52) + arg0))
                                arg0 = load32(v2 + 4)
                                if (load32(v2 + 4) != 2147483647):
                                    store32(arg1 + 60, (load32(arg1 + 60) + arg0))
                                while True:  # block $label9
                                    arg0 = load32(v2 + 8)
                                    if (load32(v2 + 8) == 2147483647):
                                        break
                                    store32(arg1 + 64, (load32(arg1 + 64) + arg0))
                                    if (load32(v2 + 8) == 2147483647):
                                        break
                                    store32(arg1 + 68, (load32(arg1 + 68) + load32(v2 + 12)))
                                    break
                                while True:  # block $label10
                                    arg0 = load32(v2 + 16)
                                    if (load32(v2 + 16) == 2147483647):
                                        break
                                    store32(arg1 + 72, (load32(arg1 + 72) + arg0))
                                    if (load32(v2 + 16) == 2147483647):
                                        break
                                    v3 = (load32(v2 + 20) + v4)
                                    store32(arg1 + 76, (load32(v2 + 20) + v4))
                                    break
                                arg0 = load32(v2 + 24)
                                if (load32(v2 + 24) == 2147483647):
                                    break
                                store32(arg1 + 84, (load32(arg1 + 84) + arg0))
                                break
                                break
                            arg0 = load32(v2)
                            if (load32(v2) != 2147483647):
                                store32(arg1 + 52, (load32(arg1 + 52) - arg0))
                            arg0 = load32(v2 + 4)
                            if (load32(v2 + 4) != 2147483647):
                                store32(arg1 + 60, (load32(arg1 + 60) - arg0))
                            while True:  # block $label11
                                arg0 = load32(v2 + 8)
                                if (load32(v2 + 8) == 2147483647):
                                    break
                                store32(arg1 + 64, (load32(arg1 + 64) - arg0))
                                if (load32(v2 + 8) == 2147483647):
                                    break
                                store32(arg1 + 68, (load32(arg1 + 68) - load32(v2 + 12)))
                                break
                            while True:  # block $label12
                                arg0 = load32(v2 + 16)
                                if (load32(v2 + 16) == 2147483647):
                                    break
                                store32(arg1 + 72, (load32(arg1 + 72) - arg0))
                                if (load32(v2 + 16) == 2147483647):
                                    break
                                v3 = (v4 - load32(v2 + 20))
                                store32(arg1 + 76, (v4 - load32(v2 + 20)))
                                break
                            arg0 = load32(v2 + 24)
                            if (load32(v2 + 24) == 2147483647):
                                break
                            store32(arg1 + 84, (load32(arg1 + 84) - arg0))
                            break
                            break
                        arg0 = load32(v2)
                        if (load32(v2) != 2147483647):
                            store32(arg1 + 52, (load32(arg1 + 52) * arg0))
                        arg0 = load32(v2 + 4)
                        if (load32(v2 + 4) != 2147483647):
                            store32(arg1 + 60, (load32(arg1 + 60) * arg0))
                        while True:  # block $label13
                            arg0 = load32(v2 + 8)
                            if (load32(v2 + 8) == 2147483647):
                                break
                            store32(arg1 + 64, (load32(arg1 + 64) * arg0))
                            if (load32(v2 + 8) == 2147483647):
                                break
                            store32(arg1 + 68, (load32(arg1 + 68) * load32(v2 + 12)))
                            break
                        while True:  # block $label14
                            arg0 = load32(v2 + 16)
                            if (load32(v2 + 16) == 2147483647):
                                break
                            store32(arg1 + 72, (load32(arg1 + 72) * arg0))
                            if (load32(v2 + 16) == 2147483647):
                                break
                            v3 = (load32(v2 + 20) * v4)
                            store32(arg1 + 76, (load32(v2 + 20) * v4))
                            break
                        arg0 = load32(v2 + 24)
                        if (load32(v2 + 24) == 2147483647):
                            break
                        store32(arg1 + 84, (load32(arg1 + 84) * arg0))
                        break
                        break
                    arg0 = load32(v2)
                    if (load32(v2) != 2147483647):
                        # TODO: i32.div_u []
                        store32(load32(arg1 + 52) + 52, arg0)
                    arg0 = load32(v2 + 4)
                    if (load32(v2 + 4) != 2147483647):
                        # TODO: i32.div_u []
                        store32(load32(arg1 + 60) + 60, arg0)
                    while True:  # block $label15
                        arg0 = load32(v2 + 8)
                        if (load32(v2 + 8) == 2147483647):
                            break
                        # TODO: i32.div_u []
                        store32(load32(arg1 + 64) + 64, arg0)
                        if (load32(v2 + 8) == 2147483647):
                            break
                        # TODO: i32.div_u []
                        store32(load32(arg1 + 68) + 68, load32(v2 + 12))
                        break
                    while True:  # block $label16
                        arg0 = load32(v2 + 16)
                        if (load32(v2 + 16) == 2147483647):
                            break
                        # TODO: i32.div_u []
                        store32(load32(arg1 + 72) + 72, arg0)
                        if (load32(v2 + 16) == 2147483647):
                            break
                        # TODO: i32.div_u []
                        v3 = load32(v2 + 20)
                        store32(v4 + 76, load32(v2 + 20))
                        break
                    arg0 = load32(v2 + 24)
                    if (load32(v2 + 24) == 2147483647):
                        break
                    # TODO: i32.div_u []
                    store32(load32(arg1 + 84) + 84, arg0)
                    break
                v2 = ((load8u(arg1 + 122) * 404) + 9568096)
                arg0 = load32(((load8u(arg1 + 122) * 404) + 9568096) + 264)
                while True:  # block $label17
                    if (load32(v2 + 92) == 0):
                        if (arg0 == 2):
                            break
                        store32(arg1 + 52, 0)
                    if (arg0 != 1):
                        break
                    store64(arg1 + 72, 0)
                    v3 = 0
                    store32(arg1 + 60, 0)
                    break
                v2 = load32(arg1 + 64)
                if load32(arg1 + 64):
                    arg0 = (2147483646 if (v5 != 2) else 0)
                    if (u(load32(arg1 + 52)) >= u(2147483647)):
                        store32(arg1 + 52, arg0)
                    if (u(load32(arg1 + 60)) >= u(2147483647)):
                        store32(arg1 + 60, arg0)
                    if (u(v2) >= u(2147483647)):
                        store32(arg1 + 64, arg0)
                        v2 = arg0
                    v5 = load32(arg1 + 68)
                    if (u(load32(arg1 + 68)) >= u(2147483647)):
                        store32(arg1 + 68, arg0)
                        v5 = arg0
                    if (u(load32(arg1 + 72)) >= u(2147483647)):
                        store32(arg1 + 72, arg0)
                    if (u(v3) >= u(2147483647)):
                        store32(arg1 + 76, arg0)
                        v3 = arg0
                    if (u(load32(arg1 + 84)) >= u(2147483647)):
                        store32(arg1 + 84, arg0)
                    if (u(v2) > u(v5)):
                        store32(arg1 + 64, v5)
                    if (v3 == 0):
                        break
                    if v4:
                        break
                    break
                return
            if (load32(arg0 + 36) == 0):
                store32(arg1 + 64, load32(arg1 + 68))
                break
            store32(arg1 + 72, load32(arg1 + 76))
            break
        if (load32(arg1 + 92) == 0):
            break
        if load32(9140316):
            if (load32(9140320) != load32(arg1 + 28)):
                break
        break

# ------------------------------------------------------------
# $func790
# ------------------------------------------------------------
def func790(arg0, arg1):
    while True:  # block $label0
        while True:  # block $label1
            # br_table[(load8u(arg1 + 125) - 3)]
            break
            break
        func119(0, arg1, 13, 1)
        arg0 = ((load8u(arg1 + 122) * 404) + 9568096)
        arg0 = load8u(arg1 + 125)
        arg0 = ((load8u(arg1 + 122) * 404) + 9568096)
        if load32(((load8u(arg1 + 122) * 404) + 9568096) + 216):
            v5 = load32(9142840)
            v6 = load16u(arg1 + 114)
            v7 = load16u(arg1 + 112)
            while True:  # $label3
                v2 = (v2 + 1)
                v8 = ((v2 + 1) + v7)
                v3 = 0
                while True:  # $label2
                    v3 = (v3 + 1)
                    v4 = (load32(9142440) + 2)
                    store32((v5 + ((v8 + ((((v3 + 1) + v6) + ((load32(9142440) + 2) * load32(arg0 + 208))) * v4)) << 2)), load32(arg0 + 212))
                    v4 = load32(arg0 + 216)
                    if (u(v3) < u(load32(arg0 + 216))):
                        continue
                    break
                if (u(v2) < u(v4)):
                    continue
                break
        func138(arg1)
        break

# ------------------------------------------------------------
# $func792
# ------------------------------------------------------------
def func792(arg0, arg1):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if (arg0 == 0):
            break
        if (load8u(9163793) == 0):
            break
        if (u(load32(9684392)) > u(2)):
            break
        v5 = load32(9142856)
        v6 = load32(9142952)
        v7 = load32(9142864)
        v4 = load32(9671164)
        arg0 = load32(9142860)
        v8 = load32(9142956)
        v2 = load32(40616)
        v9 = load32(9142868)
        store32(arg1 + 12, load8u(9163792))
        while True:  # block $label1
            # TODO: f32.convert_i32_u []
            v3 = arg0
            v3 = (((arg0 - ((v2 * v3) / v4)) * 0.5) + ((v2 * float(((v9 & 0xFFFFFFFF) >> 1))) + float(v8)))
            if (abs((((arg0 - ((v2 * v3) / v4)) * 0.5) + ((v2 * float(((v9 & 0xFFFFFFFF) >> 1))) + float(v8)))) < 2147483650.0):
                break
            break
        store32(int(v3) + 8, (-2147483648 // 32))
        while True:  # block $label2
            # TODO: f32.convert_i32_u []
            v3 = v5
            v2 = (((v2 * float(((v7 & 0xFFFFFFFF) >> 1))) + float(v6)) + ((v5 - ((v2 * v3) / v4)) * 0.5))
            if (abs((((v2 * float(((v7 & 0xFFFFFFFF) >> 1))) + float(v6)) + ((v5 - ((v2 * v3) / v4)) * 0.5))) < 2147483650.0):
                break
            break
        store32(int(v2) + 4, (-2147483648 // 32))
        func71(37, 0, 0, (arg1 + 4), 3, 0)
        store32(9684392, (load32(9684392) + 1))
        break
    G.global0 = (arg1 + 16)
    return arg1

# ------------------------------------------------------------
# $func794
# ------------------------------------------------------------
def func794():
    v0 = G.global1
    if (load32(G.global1) == 0):
        store32(v0, 1)
        v0 = func372(9688236, G.global3)
        func54(9688236)
        while True:  # block $label0
            if (v0 == 0):
                break
            if load32(v0 + 32):
                break
            func248(0, v0)
            break
        store32(G.global1, 0)

# ------------------------------------------------------------
# $func797
# ------------------------------------------------------------
def func797(arg0, arg1, arg2):
    arg0 = 0
    if (load32(59164) == load32(9142384)):
        store32(9143000, 0)
        v3 = load32(9213820)
        if load32(9213820):
            func47((load32(9671128) + (v3 * 132)))
            store32(9213820, 0)
        func45()
    if arg2:
        while True:  # $label0
            func202((load32(9671128) + (load32((arg1 + (arg0 << 2))) * 132)), 1, 0)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break
    if (load32(59164) == load32(9142384)):

# ------------------------------------------------------------
# $func798
# ------------------------------------------------------------
def func798(arg0):
    v2 = (G.global0 - 40032)
    G.global0 = (G.global0 - 40032)
    while True:  # block $label6
        if load8u(9163792):
            v4 = load32(9213808)
            if load32(9213808):
                # TODO: memory.copy []
            store32(9143000, 0)
            arg0 = load32(9213820)
            if load32(9213820):
                func47((load32(9671128) + (arg0 * 132)))
                store32(9213820, 0)
            func45()
            if v4:
                while True:  # $label5
                    while True:  # block $label0
                        v8 = (load32(9671128) + (load32(((v2 + 32) + (v7 << 2))) * 132))
                        arg0 = load32((load32(9671128) + (load32(((v2 + 32) + (v7 << 2))) * 132)) + 16)
                        if (load32((load32(9671128) + (load32(((v2 + 32) + (v7 << 2))) * 132)) + 16) == 0):
                            break
                        if (load32(arg0 + 8) == 0):
                            break
                        v6 = 0
                        while True:  # $label4
                            while True:  # block $label1
                                arg0 = (load32(9671128) + (load32((load32(arg0) + (v6 << 2))) * 132))
                                if load32((load32(9671128) + (load32((load32(arg0) + (v6 << 2))) * 132)) + 92):
                                    break
                                v3 = load32(9213808)
                                if (u(load32(9213808)) > u(9999)):
                                    break
                                if (load8u(arg0 + 125) == 3):
                                    break
                                store32(((v3 << 2) + 9173808), load32(arg0 + 28))
                                v1 = 1
                                store32(9213808, (v3 + 1))
                                while True:  # block $label2
                                    if (load8u(9142906) | load8u(9142916)):
                                        break
                                    v1 = 0
                                    if load8u(9142917):
                                        break
                                    v1 = load32(9299880)
                                    if load32(9299880):
                                        v1 = (v1 - 1)
                                        store32(9299880, (v1 - 1))
                                        v1 = load32((load32(9299872) + (v1 << 2)))
                                        break
                                    v1 = load32(9163776)
                                    v3 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v5 = load32(9163784)
                                    if (u(v3) < u(load32(9163784))):
                                        break
                                    store32(v2 + 16, v5)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    break
                                store32(arg0 + 92, v1)
                                if (load32(arg0 + 36) == 0):
                                if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) != 1):
                                    break
                                if load32(arg0 + 80):
                                    break
                                v3 = load16u(arg0 + 116)
                                if (load16u(arg0 + 116) == 0):
                                    break
                                v5 = load16u(arg0 + 118)
                                if (load16u(arg0 + 118) == 0):
                                    break
                                if (load8u(9147152) == 0):
                                    if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(arg0 + 110))))) == 0):
                                        break
                                    if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                                        break
                                    if (load8u(arg0 + 127) == 6):
                                        break
                                v1 = 0
                                while True:  # block $label3
                                    if load8u(9142917):
                                        break
                                    v1 = load32(9299880)
                                    if load32(9299880):
                                        v1 = (v1 - 1)
                                        store32(9299880, (v1 - 1))
                                        v1 = load32((load32(9299872) + (v1 << 2)))
                                        break
                                    v1 = load32(9163776)
                                    v9 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v10 = load32(9163784)
                                    if (u(v9) < u(load32(9163784))):
                                        break
                                    store32(v2, v10)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    v5 = load16u(arg0 + 118)
                                    v3 = load16u(arg0 + 116)
                                    break
                                store32(arg0 + 80, v1)
                                # TODO: f32.convert_i32_u []
                                break
                            v6 = (v6 + 1)
                            arg0 = load32(v8 + 16)
                            if (u((v6 + 1)) < u(load32(load32(v8 + 16) + 8))):
                                continue
                            break
                        break
                    v7 = (v7 + 1)
                    if ((v7 + 1) != v4):
                        continue
                    break
            break
        store32(v2 + 32, 0)
        arg0 = load32(9213808)
        if load8u(9147210):
            func41(6, 9173808, arg0, (v2 + 32), 1)
            break
        v4 = (arg0 << 2)
        v1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy []
        # call_indirect[load32(9213872)]
        break
    G.global0 = (v2 + 40032)

# ------------------------------------------------------------
# $func799
# ------------------------------------------------------------
def func799():
    v0 = e()
    if e():
        atomic_store(v0 + 8, 0)
        store32(v0 + 184, 0)
        store32(v0 + 4, 0)
    return v0

# ------------------------------------------------------------
# $func805
# ------------------------------------------------------------
def func805(arg0):
    v8 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = load32(arg0 + 12)
    v5 = (load32(arg0 + 12) + 16)
    v9 = func234((load32(arg0 + 12) + 16), 0)
    while True:  # block $label0
        v1 = load32(v3)
        if (load32(v3) == 0):
            break
        if (load8u(9142916) == 0):
            while True:  # $label1
                v2 = (v5 + (v4 * 60))
                if (load32((v5 + (v4 * 60)) + 32) == 3):
                    store32(v2 + 28, (load32(9140308) + ((load32(9568052) & 0xFFFFFFFF) >> 2)))
                    store32(9568052, (load32(9568052) + ((load32(v2) * (load32(v2 + 4) + 2)) << 2)))
                    v1 = load32(9568048)
                    store32(9568048, (load32(9568048) + 1))
                    store32(((v1 << 2) + 9563952), v2)
                    v1 = load32(v3)
                v4 = (v4 + 1)
                if (u((v4 + 1)) < u(v1)):
                    continue
                break
                break
            raise RuntimeError('unreachable')
        while True:  # $label2
            v2 = (v5 + (v4 * 60))
            if (load32((v5 + (v4 * 60)) + 32) == 3):
                v1 = load32(59152)
                store32(59152, (load32(59152) + 1))
                store32(v2 + 28, v1)
                v1 = load32(v2)
                v7 = load32(v2 + 4)
                v6 = load32(9568048)
                store32(9568048, (load32(9568048) + 1))
                store32(((v6 << 2) + 9563952), v2)
                store32(9568052, (load32(9568052) + ((v1 * (v7 + 2)) << 2)))
                v1 = load32(v3)
            v4 = (v4 + 1)
            if (u((v4 + 1)) < u(v1)):
                continue
            break
        break
    v2 = load32(9140308)
    v4 = load32(9568052)
    v1 = (load32(59156) << 2)
    v3 = (load32(9568052) % (load32(59156) << 2))
    if (load32(9568052) % (load32(59156) << 2)):
        v4 = ((v4 - v3) + v1)
        store32(9568052, ((v4 - v3) + v1))
    store32(9140308, (((v4 & 0xFFFFFFFF) >> 2) + v2))
    v1 = func26(20)
    v3 = load32(9568048)
    store32(v1 + 8, v4)
    store32(v1 + 4, v2)
    store32(v1, v3)
    v4 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
    store32(v1 + 16, arg0)
    store32(v1 + 12, v4)
    while True:  # block $label3
        if (v3 == 0):
            break
        arg0 = 0
        v4 = 0
        if (u(v3) >= u(4)):
            v7 = (v3 & -4)
            v2 = 0
            while True:  # $label4
                v5 = (v4 << 2)
                store32(((v4 << 2) + load32(v1 + 12)), load32((v5 + 9563952)))
                v6 = (v5 | 4)
                store32(((v5 | 4) + load32(v1 + 12)), load32((v6 + 9563952)))
                v6 = (v5 | 8)
                store32(((v5 | 8) + load32(v1 + 12)), load32((v6 + 9563952)))
                v5 = (v5 | 12)
                store32(((v5 | 12) + load32(v1 + 12)), load32((v5 + 9563952)))
                v4 = (v4 + 4)
                v2 = (v2 + 4)
                if ((v2 + 4) != v7):
                    continue
                break
        v2 = (v3 & 3)
        if ((v3 & 3) == 0):
            break
        while True:  # $label5
            v3 = (v4 << 2)
            store32(((v4 << 2) + load32(v1 + 12)), load32((v3 + 9563952)))
            v4 = (v4 + 1)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != v2):
                continue
            break
        break
    func186((v8 + 12), 0, 59, v1)
    store32(9568052, 0)
    store32(9568048, 0)
    arg0 = load32(9671136)
    if (u(load32(9671136)) >= u(4)):
        v2 = load32(9671128)
        v4 = 3
        while True:  # $label11
            while True:  # block $label6
                v3 = (v2 + (v4 * 132))
                v1 = load8u((v2 + (v4 * 132)) + 125)
                if (load8u((v2 + (v4 * 132)) + 125) == 3):
                    break
                if (v9 != load8u(v3 + 122)):
                    break
                v5 = load32(v3 + 40)
                while True:  # block $label7
                    arg0 = load32(9299880)
                    if (load32(9299880) != load32(9299876)):
                        v2 = load32(9299872)
                        break
                    v2 = (load32(9299884) + arg0)
                    store32(9299876, (load32(9299884) + arg0))
                    v1 = load32(9299872)
                    v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy []
                    if v1:
                        arg0 = load32(9299880)
                    store32(9299872, v2)
                    v1 = load8u(v3 + 125)
                    break
                store32(9299880, (arg0 + 1))
                store32((v2 + (arg0 << 2)), v5)
                store32(v3 + 40, 0)
                arg0 = (v1 & 255)
                v2 = (((v1 & 255) != 4) & (arg0 != 14))
                while True:  # block $label10
                    while True:  # block $label9
                        while True:  # block $label8
                            # br_table[(arg0 - 4)]
                            break
                            break
                        arg0 = ((load8u(v3 + 122) * 404) + 9568096)
                        v1 = load32(((load8u(v3 + 122) * 404) + 9568096) + 356)
                        if load32(((load8u(v3 + 122) * 404) + 9568096) + 356):
                            break
                        v1 = 9142636
                        v5 = load32(arg0 + 216)
                        arg0 = load32(arg0 + 220)
                        arg0 = (load32(arg0 + 216) if (u(arg0) < u(v5)) else load32(arg0 + 220))
                        arg0 = ((6 if (u(arg0) >= u(6)) else (load32(arg0 + 216) if (u(arg0) < u(v5)) else load32(arg0 + 220))) - 1)
                        if (u(((6 if (u(arg0) >= u(6)) else (load32(arg0 + 216) if (u(arg0) < u(v5)) else load32(arg0 + 220))) - 1)) >= u(5)):
                            break
                        v1 = load32(((arg0 << 2) + 10132))
                        break
                        break
                    v1 = ((load8u(v3 + 122) * 72) + 9263856)
                    break
                arg0 = load32(9671136)
                v2 = load32(9671128)
                break
            v4 = (v4 + 1)
            if (u((v4 + 1)) < u(arg0)):
                continue
            break
    while True:  # block $label12
        if (load32(9671176) == 0):
            break
        if (load32(load32(9671168)) != v9):
            break
        break
    G.global0 = (v8 + 16)

# ------------------------------------------------------------
# $func808
# ------------------------------------------------------------
def func808(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = load64(arg0 + 32)
    if (load64(arg0 + 32) != 0):
        while True:  # block $label0
            # TODO: f64.convert_i64_u []
            # TODO: f64.convert_i64_u []
            v2 = ((load64(arg0 + 24) * 100.0) / v3)
            if ((((load64(arg0 + 24) * 100.0) / v3) < 4294967296.0) & (v2 >= 0.0)):
                # TODO: i32.trunc_f64_u []
                break
            break
        store32(v2, 0)
    G.global0 = (v1 + 16)
    return v1

# ------------------------------------------------------------
# $func810
# ------------------------------------------------------------
def func810(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(arg0 + 8)
    store32(v1 + 4, load16u(arg0 + 42))
    store32(v1, v2)
    func383(func363(8863, v1), arg0)
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $func811
# ------------------------------------------------------------
def func811(arg0, arg1):
    while True:  # block $label3
        while True:  # block $label2
            while True:  # block $label1
                while True:  # block $label0
                    # br_table[(arg0 - 1)]
                    break
                    break
                break
                break
            arg0 = G.global3
            break
        break
    v15 = arg0
    if (arg0 == G.global3):
    else:
    if 0:
    else:
        v6 = (G.global0 - 32)
        G.global0 = (G.global0 - 32)
        store32(v6 + 28, arg1)
        store32(v6 + 16, arg1)
        store32(v6 + 24, 0)
        store32(v6 + 20, 422)
        store64(v6 + 8, load64(v6 + 20))
        v9 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        while True:  # block $label16
            while True:  # block $label15
                arg0 = func372(9688236, v15)
                if (func372(9688236, v15) == 0):
                    arg0 = load32(9688264)
                    if (load32(9688264) == load32(9688268)):
                        while True:  # block $label4
                            v16 = ((arg0 << 1) if arg0 else 1)
                            v7 = (((arg0 << 1) if arg0 else 1) << 2)
                            arg0 = 0
                            v10 = load32(9688260)
                            if (load32(9688260) == 0):
                                break
                            if (u(v7) >= u(-64)):
                                store32(G.global3 + 28, 48)
                                break
                            while True:  # block $label5
                                if (load8u(9690908) & 2):
                                    if func55(9690912):
                                        break
                                while True:  # block $label6
                                    v4 = (16 if (u(v7) < u(11)) else ((v7 + 11) & -8))
                                    arg1 = (v10 - 8)
                                    v8 = load32((v10 - 8) + 4)
                                    v2 = (load32((v10 - 8) + 4) & -8)
                                    while True:  # block $label7
                                        if ((v8 & 3) == 0):
                                            if (u(v4) < u(256)):
                                                break
                                            if (u((v4 + 4)) <= u(v2)):
                                                arg0 = arg1
                                                if (u((v2 - v4)) <= u((load32(9690448) << 1))):
                                                    break
                                            break
                                        v5 = (arg1 + v2)
                                        while True:  # block $label8
                                            if (u(v2) >= u(v4)):
                                                arg0 = (v2 - v4)
                                                if (u((v2 - v4)) < u(16)):
                                                    break
                                                store32(arg1 + 4, (((v8 & 1) | v4) | 2))
                                                v2 = (arg1 + v4)
                                                store32((arg1 + v4) + 4, (arg0 | 3))
                                                store32(v5 + 4, (load32(v5 + 4) | 1))
                                                break
                                            if (load32(9690488) == v5):
                                                v2 = (load32(9690476) + v2)
                                                if (u((load32(9690476) + v2)) <= u(v4)):
                                                    break
                                                store32(arg1 + 4, (((v8 & 1) | v4) | 2))
                                                arg0 = (arg1 + v4)
                                                v2 = (v2 - v4)
                                                store32((arg1 + v4) + 4, ((v2 - v4) | 1))
                                                store32(9690476, v2)
                                                store32(9690488, arg0)
                                                break
                                            if (load32(9690484) == v5):
                                                v2 = (load32(9690472) + v2)
                                                if (u((load32(9690472) + v2)) < u(v4)):
                                                    break
                                                while True:  # block $label9
                                                    arg0 = (v2 - v4)
                                                    if (u((v2 - v4)) >= u(16)):
                                                        store32(arg1 + 4, (((v8 & 1) | v4) | 2))
                                                        v3 = (arg1 + v4)
                                                        store32((arg1 + v4) + 4, (arg0 | 1))
                                                        v2 = (arg1 + v2)
                                                        store32((arg1 + v2), arg0)
                                                        store32(v2 + 4, (load32(v2 + 4) & -2))
                                                        break
                                                    store32(arg1 + 4, (((v8 & 1) | v2) | 2))
                                                    arg0 = (arg1 + v2)
                                                    store32((arg1 + v2) + 4, (load32(arg0 + 4) | 1))
                                                    arg0 = 0
                                                    break
                                                store32(9690484, v3)
                                                store32(9690472, arg0)
                                                break
                                            v3 = load32(v5 + 4)
                                            if (load32(v5 + 4) & 2):
                                                break
                                            v11 = ((v3 & -8) + v2)
                                            if (u(((v3 & -8) + v2)) < u(v4)):
                                                break
                                            v13 = (v11 - v4)
                                            while True:  # block $label10
                                                if (u(v3) <= u(255)):
                                                    arg0 = load32(v5 + 12)
                                                    v2 = load32(v5 + 8)
                                                    if (load32(v5 + 12) == load32(v5 + 8)):
                                                        store32(9690464, (load32(9690464) & rotl(-2, ((v3 & 0xFFFFFFFF) >> 3), 32)))
                                                        break
                                                    store32(v2 + 12, arg0)
                                                    store32(arg0 + 8, v2)
                                                    break
                                                v12 = load32(v5 + 24)
                                                while True:  # block $label11
                                                    v2 = load32(v5 + 12)
                                                    if (v5 != load32(v5 + 12)):
                                                        arg0 = load32(v5 + 8)
                                                        store32(load32(v5 + 8) + 12, v2)
                                                        store32(v2 + 8, arg0)
                                                        break
                                                    while True:  # block $label12
                                                        v3 = (v5 + 20)
                                                        arg0 = load32((v5 + 20))
                                                        if load32((v5 + 20)):
                                                            break
                                                        v3 = (v5 + 16)
                                                        arg0 = load32((v5 + 16))
                                                        if load32((v5 + 16)):
                                                            break
                                                        v2 = 0
                                                        break
                                                        break
                                                    while True:  # $label13
                                                        v14 = v3
                                                        v2 = arg0
                                                        v3 = (arg0 + 20)
                                                        arg0 = load32((arg0 + 20))
                                                        if load32((arg0 + 20)):
                                                            continue
                                                        v3 = (v2 + 16)
                                                        arg0 = load32(v2 + 16)
                                                        if load32(v2 + 16):
                                                            continue
                                                        break
                                                    store32(v14, 0)
                                                    break
                                                if (v12 == 0):
                                                    break
                                                while True:  # block $label14
                                                    arg0 = load32(v5 + 28)
                                                    v3 = ((load32(v5 + 28) << 2) + 9690768)
                                                    if (load32(((load32(v5 + 28) << 2) + 9690768)) == v5):
                                                        store32(v3, v2)
                                                        if v2:
                                                            break
                                                        store32(9690468, (load32(9690468) & rotl(-2, arg0, 32)))
                                                        break
                                                    store32((v12 + (16 if (load32(v12 + 16) == v5) else 20)), v2)
                                                    if (v2 == 0):
                                                        break
                                                    break
                                                store32(v2 + 24, v12)
                                                arg0 = load32(v5 + 16)
                                                if load32(v5 + 16):
                                                    store32(v2 + 16, arg0)
                                                    store32(arg0 + 24, v2)
                                                arg0 = load32(v5 + 20)
                                                if (load32(v5 + 20) == 0):
                                                    break
                                                store32(v2 + 20, arg0)
                                                store32(arg0 + 24, v2)
                                                break
                                            if (u(v13) <= u(15)):
                                                store32(arg1 + 4, (((v8 & 1) | v11) | 2))
                                                arg0 = (arg1 + v11)
                                                store32((arg1 + v11) + 4, (load32(arg0 + 4) | 1))
                                                break
                                            store32(arg1 + 4, (((v8 & 1) | v4) | 2))
                                            arg0 = (arg1 + v4)
                                            store32((arg1 + v4) + 4, (v13 | 3))
                                            v2 = (arg1 + v11)
                                            store32((arg1 + v11) + 4, (load32(v2 + 4) | 1))
                                            break
                                        arg0 = arg1
                                        break
                                    break
                                arg0 = arg0
                                if (load8u(9690908) & 2):
                                    func54(9690912)
                                if arg0:
                                    break
                                arg0 = e()
                                if (e() == 0):
                                    break
                                arg1 = load32((v10 - 4))
                                arg1 = ((-4 if (load32((v10 - 4)) & 3) else -8) + (arg1 & -8))
                                break
                            break
                        arg0 = arg0
                        if (arg0 == 0):
                            break
                        store32(9688268, v16)
                        store32(9688260, arg0)
                    arg0 = func393(v15)
                    if (func393(v15) == 0):
                        break
                    arg1 = load32(9688264)
                    store32(9688264, (load32(9688264) + 1))
                    store32((load32(9688260) + (arg1 << 2)), arg0)
                break
                break
            break
        arg1 = 0
        func54(9688236)
        if arg1:
            store32(v9 + 8, load32(v6 + 16))
            store64(v9, load64(v6 + 8))
            arg0 = (G.global0 - 48)
            G.global0 = (G.global0 - 48)
            while True:  # block $label17
                v3 = load32(arg1 + 28)
                v2 = atomic_load(load32(arg1 + 28) + 124)
                while True:  # $label18
                    if (v2 == 0):
                        break
                    # TODO: i32.atomic.rmw.cmpxchg [('offset', 124)]
                    v2 = (v2 + 1)
                    if (v2 != (v2 + 1)):
                        continue
                    break
                break
            if 1:
                v2 = (arg1 + 4)
                store32(arg0 + 32, load32(v9 + 8))
                store64(arg0 + 24, load64(v9))
                v3 = func391(arg1, (arg0 + 24))
                func54(v2)
                while True:  # block $label19
                    if v3:
                        # TODO: i32.atomic.rmw.xchg []
                        v3 = 2
                        v2 = load32(arg1 + 28)
                        if (v3 == 2):
                            break
                        store32(arg0 + 44, arg1)
                        store32(arg0 + 16, arg1)
                        store32(arg0 + 40, 423)
                        store32(arg0 + 36, 424)
                        store64(arg0 + 8, load64(arg0 + 36))
                        v3 = (G.global0 - 16)
                        G.global0 = (G.global0 - 16)
                        v14 = load32(v2 + 120)
                        store32(v3 + 8, load32(arg0 + 16))
                        store64(v3, load64(arg0 + 8))
                        func54((load32(v2 + 120) + 4))
                        while True:  # block $label20
                            # TODO: i32.atomic.rmw.xchg []
                            if (2 == 2):
                                break
                            if atomic_load(v2 + 128):
                                # TODO: memory.atomic.notify []
                                break
                            a_u()
                            break
                        G.global0 = (v3 + 16)
                    break
                arg1 = load32(arg1 + 28)
                # TODO: i32.atomic.rmw.sub [('offset', 124)]
                if (1 == 1):
                    func111((arg1 + 124), 2147483647)
            G.global0 = (arg0 + 48)
        G.global0 = (v9 + 16)
        G.global0 = (v6 + 32)
    return 0

# ------------------------------------------------------------
# $func814
# ------------------------------------------------------------
def func814(arg0, arg1, arg2):
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = load32(9142892)
    while True:  # block $label0
        while True:  # block $label1
            if load8u(9147210):
                if (u(v3) < u(2)):
                    break
                arg2 = load32(59164)
                v6 = load32(9561692)
                arg1 = 1
                while True:  # $label2
                    v5 = (v6 + (arg1 * 286704))
                    if (load32((v6 + (arg1 * 286704)) + 284616) == arg2):
                        break
                    if (load32(v5 + 284628) == arg2):
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v3):
                        continue
                    break
                arg1 = 0
                break
            arg1 = load32(9142872)
            break
        if (u(v3) < u(2)):
            break
        v5 = load32(arg0)
        v6 = load32(9561692)
        arg2 = 1
        while True:  # $label4
            while True:  # block $label3
                v7 = (v6 + (arg2 * 286704))
                if (load32((v6 + (arg2 * 286704)) + 284616) == v5):
                    break
                if (load32(v7 + 284628) == v5):
                    break
                arg2 = (arg2 + 1)
                if ((arg2 + 1) != v3):
                    continue
                break
                break
            break
        if (u(arg2) >= u(v3)):
            break
        if (arg1 == arg2):
            break
        if (load32(9147136) == 0):
            break
        v11 = load32(arg0 + 4)
        v9 = (v6 + (arg2 * 286704))
        v8 = ((v6 + (arg2 * 286704)) + 281800)
        arg0 = load32(v9 + 281800)
        if (load32(v9 + 281800) == 0):
            v5 = (-1 if (u(v3) > u(1073741823)) else (v3 << 2))
            arg0 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
            # TODO: memory.fill []
            store32(v8, arg0)
        v5 = (v6 + (arg1 * 286704))
        v10 = ((v6 + (arg1 * 286704)) + 281800)
        v7 = load32(v5 + 281800)
        if load32(v5 + 281800):
        else:
            arg0 = (-1 if (u(v3) > u(1073741823)) else (v3 << 2))
            v7 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
            # TODO: memory.fill []
            store32(v10, v7)
        arg0 = load32((load32(v8) + (arg1 << 2)))
        if load32((load32(v8) + (arg1 << 2))):
            if (u(((load32(9142848) - arg0) * 25)) < u(60000)):
                break
        arg0 = load8u((load32(9143004) + (arg2 + (arg1 * v3))))
        if (v11 == 0):
            while True:  # block $label5
                if arg0:
                    break
                if (load32(9142872) != arg2):
                    break
                arg0 = (v6 + (arg1 * 286704))
                v3 = load32((v6 + (arg1 * 286704)) + 284628)
                arg0 = load32(arg0 + 284616)
                store32(v4 + 4, v5)
                store32(v4, 914)
                store32(v4 + 8, (arg0 if arg0 else v3))
                a_b()
                break
            func176(arg2, arg1, 1)
            break
        if (arg0 == 0):
            break
        while True:  # block $label6
            if (load32(9147132) == 0):
                break
            if (load32(9142440) != 4096):
                break
            if (u(func385(v5)) > u(2)):
                break
            v7 = load32(v10)
            break
        if load32((v7 + (arg2 << 2))):
            while True:  # block $label7
                if (load32(9147132) == 0):
                    break
                if (load32(9142440) != 4096):
                    break
                if (u(func385(v9)) < u(3)):
                    break
                a_b()
                break
                break
            func176(arg2, arg1, 0)
            if (load32(9142872) != arg2):
                break
            arg0 = (v6 + (arg1 * 286704))
            arg1 = load32((v6 + (arg1 * 286704)) + 284628)
            arg0 = load32(arg0 + 284616)
            store32(v4 + 36, v5)
            store32(v4 + 32, 916)
            store32(v4 + 40, (arg0 if arg0 else arg1))
            a_b()
            break
        store32((load32(v8) + (arg1 << 2)), load32(9142848))
        if (load32(9142872) != arg2):
            break
        store32(v4 + 16, load32((v6 + (arg1 * 286704)) + 284616))
        a_b()
        break
    G.global0 = (v4 + 48)
    return (v4 + 16)

# ------------------------------------------------------------
# $func819
# ------------------------------------------------------------
def func819(arg0, arg1):
    while True:  # block $label0
        if (arg1 == -1):
            break
        if arg1:
            func38(arg1)
        if (u(load32(load32(9142424) + 48)) < u(2)):
            break
        v6 = load32(9142836)
        v7 = load32(load32(9142836) + 964)
        if (load32(load32(9142836) + 964) == 0):
            break
        v8 = ((arg0 & 0xFFFFFFFF) >> 16)
        v9 = (arg0 & 65535)
        arg0 = load32(9142440)
        arg1 = 0
        while True:  # $label2
            while True:  # block $label1
                v2 = load32(v6 + 960)
                v3 = (arg1 << 2)
                v4 = load32((load32(v6 + 960) + ((arg1 << 2) | 4)))
                v5 = (load32((load32(v6 + 960) + ((arg1 << 2) | 4))) + v8)
                if (u(arg0) <= u((load32((load32(v6 + 960) + ((arg1 << 2) | 4))) + v8))):
                    break
                v2 = load32((v2 + v3))
                v3 = (load32((v2 + v3)) + v9)
                if (u(arg0) <= u((load32((v2 + v3)) + v9))):
                    break
                if ((v3 | v5) < 0):
                    break
                if ((((v2 * v2) + (v4 * v4)) - 1) > 64):
                    break
                arg0 = load32(9142440)
                break
            arg1 = (arg1 + 2)
            if (u((arg1 + 2)) < u(v7)):
                continue
            break
        break

# ------------------------------------------------------------
# $func822
# ------------------------------------------------------------
def func822(arg0, arg1):
    while True:  # $label7
        while True:  # block $label2
            while True:  # block $label3
                while True:  # block $label0
                    if (u(load32(arg0 + 116)) > u(261)):
                        break
                    v2 = load32(arg0 + 116)
                    while True:  # block $label1
                        if arg1:
                            break
                        if (u(v2) >= u(262)):
                            break
                        return 0
                        break
                    if (v2 == 0):
                        break
                    if (u(v2) > u(2)):
                        break
                    v2 = load32(arg0 + 96)
                    store32(arg0 + 120, load32(arg0 + 96))
                    store32(arg0 + 100, load32(arg0 + 112))
                    v4 = 2
                    store32(arg0 + 96, 2)
                    break
                    break
                v4 = 2
                v3 = load32(arg0 + 108)
                v2 = (load32(arg0 + 84) & (load8u((load32(arg0 + 108) + load32(arg0 + 56)) + 2) ^ (load32(arg0 + 72) << load32(arg0 + 88))))
                store32(arg0 + 72, (load32(arg0 + 84) & (load8u((load32(arg0 + 108) + load32(arg0 + 56)) + 2) ^ (load32(arg0 + 72) << load32(arg0 + 88)))))
                v2 = (load32(arg0 + 68) + (v2 << 1))
                v5 = load16u((load32(arg0 + 68) + (v2 << 1)))
                store16((load32(arg0 + 64) + ((v3 & load32(arg0 + 52)) << 1)), load16u((load32(arg0 + 68) + (v2 << 1))))
                store16(v2, v3)
                v2 = load32(arg0 + 96)
                store32(arg0 + 120, load32(arg0 + 96))
                store32(arg0 + 100, load32(arg0 + 112))
                store32(arg0 + 96, 2)
                if (v5 == 0):
                    break
                while True:  # block $label4
                    if (u(v2) >= u(load32(arg0 + 128))):
                        break
                    if (u((load32(arg0 + 44) - 262)) < u((v3 - v5))):
                        break
                    v4 = func359(arg0, v5)
                    store32(arg0 + 96, func359(arg0, v5))
                    if (u(v4) > u(5)):
                        break
                    if (load32(arg0 + 136) != 1):
                        if (v4 != 3):
                            break
                        v4 = 3
                        if (u((load32(arg0 + 108) - load32(arg0 + 112))) < u(4097)):
                            break
                    v4 = 2
                    store32(arg0 + 96, 2)
                    break
                v2 = load32(arg0 + 120)
                break
            while True:  # block $label5
                if (u(v2) < u(3)):
                    break
                if (u(v2) < u(v4)):
                    break
                v3 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                v5 = load32(arg0 + 116)
                v6 = load32(arg0 + 108)
                v3 = (load32(arg0 + 108) + (load32(arg0 + 100) ^ -1))
                store8((v3 + load32(arg0 + 5784)), (load32(arg0 + 108) + (load32(arg0 + 100) ^ -1)))
                v4 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v4 + load32(arg0 + 5784)), ((v3 & 0xFFFFFFFF) >> 8))
                v4 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                v2 = (v2 - 3)
                store8((v4 + load32(arg0 + 5784)), (v2 - 3))
                v2 = (((load8u(((v2 & 255) + 23984)) << 2) + arg0) + 1176)
                store16((((load8u(((v2 & 255) + 23984)) << 2) + arg0) + 1176), (load16u(v2) + 1))
                v2 = ((v3 - 1) & 65535)
                v2 = ((arg0 + (load8u(((((v3 - 1) & 65535) if (u(v2) < u(256)) else (((v2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440)
                store16(((arg0 + (load8u(((((v3 - 1) & 65535) if (u(v2) < u(256)) else (((v2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440), (load16u(v2) + 1))
                v2 = load32(arg0 + 120)
                v4 = (load32(arg0 + 120) - 2)
                store32(arg0 + 120, (load32(arg0 + 120) - 2))
                store32(arg0 + 116, ((load32(arg0 + 116) - v2) + 1))
                v5 = ((v5 + v6) - 3)
                v2 = load32(arg0 + 108)
                v6 = load32(arg0 + 5796)
                v8 = load32(arg0 + 5792)
                while True:  # $label6
                    v3 = v2
                    v2 = (v2 + 1)
                    store32(arg0 + 108, (v2 + 1))
                    if (u(v2) <= u(v5)):
                        v7 = (load32(arg0 + 84) & (load8u((v3 + load32(arg0 + 56)) + 3) ^ (load32(arg0 + 72) << load32(arg0 + 88))))
                        store32(arg0 + 72, (load32(arg0 + 84) & (load8u((v3 + load32(arg0 + 56)) + 3) ^ (load32(arg0 + 72) << load32(arg0 + 88)))))
                        v7 = (load32(arg0 + 68) + (v7 << 1))
                        store16((load32(arg0 + 64) + ((load32(arg0 + 52) & v2) << 1)), load16u((load32(arg0 + 68) + (v7 << 1))))
                        store16(v7, v2)
                    v4 = (v4 - 1)
                    store32(arg0 + 120, (v4 - 1))
                    if v4:
                        continue
                    break
                store32(arg0 + 96, 2)
                store32(arg0 + 104, 0)
                v3 = (v3 + 2)
                store32(arg0 + 108, (v3 + 2))
                if (v6 != v8):
                    continue
                v4 = 0
                v2 = load32(arg0 + 92)
                if (load32(arg0 + 92) >= 0):
                else:
                store32(arg0 + 92, load32(arg0 + 108))
                v2 = load32(arg0)
                v3 = load32(load32(arg0) + 28)
                while True:  # block $label8
                    v4 = load32(v3 + 20)
                    v5 = load32(v2 + 16)
                    v4 = (load32(v3 + 20) if (u(v4) < u(v5)) else load32(v2 + 16))
                    if ((load32(v3 + 20) if (u(v4) < u(v5)) else load32(v2 + 16)) == 0):
                        break
                    store32(v2 + 12, (load32(v2 + 12) + v4))
                    store32(v3 + 16, (load32(v3 + 16) + v4))
                    store32(v2 + 20, (load32(v2 + 20) + v4))
                    store32(v2 + 16, (load32(v2 + 16) - v4))
                    v2 = load32(v3 + 20)
                    store32(v3 + 20, (load32(v3 + 20) - v4))
                    if (v2 != v4):
                        break
                    store32(v3 + 16, load32(v3 + 8))
                    break
                if load32(load32(arg0) + 16):
                    continue
                return 0
                break
            if load32(arg0 + 104):
                v2 = load8u(((load32(arg0 + 108) + load32(arg0 + 56)) - 1))
                v3 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v3 + load32(arg0 + 5784)), 0)
                v3 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v3 + load32(arg0 + 5784)), 0)
                v3 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v3 + load32(arg0 + 5784)), v2)
                v2 = (arg0 + (v2 << 2))
                store16(((arg0 + (v2 << 2)) + 148), (load16u(v2 + 148) + 1))
                while True:  # block $label9
                    if (load32(arg0 + 5792) != load32(arg0 + 5796)):
                        break
                    v4 = 0
                    v2 = load32(arg0 + 92)
                    if (load32(arg0 + 92) >= 0):
                    else:
                    store32(arg0 + 92, load32(arg0 + 108))
                    v2 = load32(arg0)
                    v3 = load32(load32(arg0) + 28)
                    v4 = load32(v3 + 20)
                    v5 = load32(v2 + 16)
                    v4 = (load32(v3 + 20) if (u(v4) < u(v5)) else load32(v2 + 16))
                    if ((load32(v3 + 20) if (u(v4) < u(v5)) else load32(v2 + 16)) == 0):
                        break
                    store32(v2 + 12, (load32(v2 + 12) + v4))
                    store32(v3 + 16, (load32(v3 + 16) + v4))
                    store32(v2 + 20, (load32(v2 + 20) + v4))
                    store32(v2 + 16, (load32(v2 + 16) - v4))
                    v2 = load32(v3 + 20)
                    store32(v3 + 20, (load32(v3 + 20) - v4))
                    if (v2 != v4):
                        break
                    store32(v3 + 16, load32(v3 + 8))
                    break
                store32(arg0 + 108, (load32(arg0 + 108) + 1))
                store32(arg0 + 116, (load32(arg0 + 116) - 1))
                if load32(load32(arg0) + 16):
                    continue
                return 0
            else:
                store32(arg0 + 104, 1)
                store32(arg0 + 108, (load32(arg0 + 108) + 1))
                store32(arg0 + 116, (load32(arg0 + 116) - 1))
                continue
            raise RuntimeError('unreachable')
            break
        break
    if load32(arg0 + 104):
        v2 = load8u(((load32(arg0 + 108) + load32(arg0 + 56)) - 1))
        v3 = load32(arg0 + 5792)
        store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
        store8((v3 + load32(arg0 + 5784)), 0)
        v3 = load32(arg0 + 5792)
        store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
        store8((v3 + load32(arg0 + 5784)), 0)
        v3 = load32(arg0 + 5792)
        store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
        store8((v3 + load32(arg0 + 5784)), v2)
        v2 = (arg0 + (v2 << 2))
        store16(((arg0 + (v2 << 2)) + 148), (load16u(v2 + 148) + 1))
        store32(arg0 + 104, 0)
    v2 = load32(arg0 + 108)
    store32(arg0 + 5812, (2 if (u(v2) >= u(2)) else load32(arg0 + 108)))
    if (arg1 == 4):
        v4 = 0
        arg1 = load32(arg0 + 92)
        if (load32(arg0 + 92) >= 0):
        else:
        store32(arg0 + 92, load32(arg0 + 108))
        arg1 = load32(arg0)
        v2 = load32(load32(arg0) + 28)
        while True:  # block $label10
            v3 = load32(v2 + 20)
            v4 = load32(arg1 + 16)
            v3 = (load32(v2 + 20) if (u(v3) < u(v4)) else load32(arg1 + 16))
            if ((load32(v2 + 20) if (u(v3) < u(v4)) else load32(arg1 + 16)) == 0):
                break
            store32(arg1 + 12, (load32(arg1 + 12) + v3))
            store32(v2 + 16, (load32(v2 + 16) + v3))
            store32(arg1 + 20, (load32(arg1 + 20) + v3))
            store32(arg1 + 16, (load32(arg1 + 16) - v3))
            arg1 = load32(v2 + 20)
            store32(v2 + 20, (load32(v2 + 20) - v3))
            if (arg1 != v3):
                break
            store32(v2 + 16, load32(v2 + 8))
            break
        return (3 if load32(load32(arg0) + 16) else 2)
    while True:  # block $label11
        if (load32(arg0 + 5792) == 0):
            break
        v4 = 0
        arg1 = load32(arg0 + 92)
        if (load32(arg0 + 92) >= 0):
        else:
        store32(arg0 + 92, load32(arg0 + 108))
        arg1 = load32(arg0)
        v2 = load32(load32(arg0) + 28)
        while True:  # block $label12
            v3 = load32(v2 + 20)
            v4 = load32(arg1 + 16)
            v3 = (load32(v2 + 20) if (u(v3) < u(v4)) else load32(arg1 + 16))
            if ((load32(v2 + 20) if (u(v3) < u(v4)) else load32(arg1 + 16)) == 0):
                break
            store32(arg1 + 12, (load32(arg1 + 12) + v3))
            store32(v2 + 16, (load32(v2 + 16) + v3))
            store32(arg1 + 20, (load32(arg1 + 20) + v3))
            store32(arg1 + 16, (load32(arg1 + 16) - v3))
            arg1 = load32(v2 + 20)
            store32(v2 + 20, (load32(v2 + 20) - v3))
            if (arg1 != v3):
                break
            store32(v2 + 16, load32(v2 + 8))
            break
        if load32(load32(arg0) + 16):
            break
        return 0
        break
    return 1

# ------------------------------------------------------------
# $func823
# ------------------------------------------------------------
def func823(arg0, arg1):
    while True:  # block $label1
        while True:  # $label6
            while True:  # block $label3
                while True:  # block $label2
                    if (u(load32(arg0 + 116)) <= u(261)):
                        v2 = load32(arg0 + 116)
                        while True:  # block $label0
                            if arg1:
                                break
                            if (u(v2) >= u(262)):
                                break
                            return 0
                            break
                        if (v2 == 0):
                            break
                        if (u(v2) < u(3)):
                            break
                    v4 = load32(arg0 + 108)
                    v2 = (load32(arg0 + 84) & (load8u((load32(arg0 + 108) + load32(arg0 + 56)) + 2) ^ (load32(arg0 + 72) << load32(arg0 + 88))))
                    store32(arg0 + 72, (load32(arg0 + 84) & (load8u((load32(arg0 + 108) + load32(arg0 + 56)) + 2) ^ (load32(arg0 + 72) << load32(arg0 + 88)))))
                    v2 = (load32(arg0 + 68) + (v2 << 1))
                    v3 = load16u((load32(arg0 + 68) + (v2 << 1)))
                    store16((load32(arg0 + 64) + ((v4 & load32(arg0 + 52)) << 1)), load16u((load32(arg0 + 68) + (v2 << 1))))
                    store16(v2, v4)
                    if (v3 == 0):
                        break
                    if (u((load32(arg0 + 44) - 262)) < u((v4 - v3))):
                        break
                    v3 = func359(arg0, v3)
                    store32(arg0 + 96, func359(arg0, v3))
                    break
                    break
                v3 = load32(arg0 + 96)
                break
            while True:  # block $label7
                if (u(v3) >= u(3)):
                    v2 = load32(arg0 + 5792)
                    store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                    v4 = (load32(arg0 + 108) - load32(arg0 + 112))
                    store8((v2 + load32(arg0 + 5784)), (load32(arg0 + 108) - load32(arg0 + 112)))
                    v2 = load32(arg0 + 5792)
                    store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                    store8((v2 + load32(arg0 + 5784)), ((v4 & 0xFFFFFFFF) >> 8))
                    v2 = load32(arg0 + 5792)
                    store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                    v2 = (v3 - 3)
                    store8((v2 + load32(arg0 + 5784)), (v3 - 3))
                    v2 = (((load8u(((v2 & 255) + 23984)) << 2) + arg0) + 1176)
                    store16((((load8u(((v2 & 255) + 23984)) << 2) + arg0) + 1176), (load16u(v2) + 1))
                    v2 = ((v4 - 1) & 65535)
                    v2 = ((arg0 + (load8u(((((v4 - 1) & 65535) if (u(v2) < u(256)) else (((v2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440)
                    store16(((arg0 + (load8u(((((v4 - 1) & 65535) if (u(v2) < u(256)) else (((v2 & 0xFFFFFFFF) >> 7) + 256)) + 23472)) << 2)) + 2440), (load16u(v2) + 1))
                    v3 = load32(arg0 + 96)
                    v2 = (load32(arg0 + 116) - load32(arg0 + 96))
                    store32(arg0 + 116, (load32(arg0 + 116) - load32(arg0 + 96)))
                    v8 = load32(arg0 + 5796)
                    v9 = load32(arg0 + 5792)
                    while True:  # block $label4
                        if (u(v3) > u(load32(arg0 + 128))):
                            break
                        if (u(v2) < u(3)):
                            break
                        v6 = (v3 - 1)
                        store32(arg0 + 96, (v3 - 1))
                        v7 = load32(arg0 + 72)
                        v3 = load32(arg0 + 108)
                        v10 = load32(arg0 + 52)
                        v11 = load32(arg0 + 64)
                        v12 = load32(arg0 + 68)
                        v13 = load32(arg0 + 84)
                        v14 = load32(arg0 + 56)
                        v5 = load32(arg0 + 88)
                        while True:  # $label5
                            v2 = v3
                            v3 = (v3 + 1)
                            store32(arg0 + 108, (v3 + 1))
                            v7 = ((load8u((v2 + v14) + 3) ^ (v7 << v5)) & v13)
                            store32(arg0 + 72, ((load8u((v2 + v14) + 3) ^ (v7 << v5)) & v13))
                            v4 = (v12 + (v7 << 1))
                            store16((v11 + ((v3 & v10) << 1)), load16u((v12 + (v7 << 1))))
                            store16(v4, v3)
                            v6 = (v6 - 1)
                            store32(arg0 + 96, (v6 - 1))
                            if v6:
                                continue
                            break
                        v3 = (v2 + 2)
                        store32(arg0 + 108, (v2 + 2))
                        if (v8 != v9):
                            continue
                        break
                        break
                    store32(arg0 + 96, 0)
                    v3 = (load32(arg0 + 108) + v3)
                    store32(arg0 + 108, (load32(arg0 + 108) + v3))
                    v4 = (load32(arg0 + 56) + v3)
                    v2 = load8u((load32(arg0 + 56) + v3))
                    store32(arg0 + 72, load8u((load32(arg0 + 56) + v3)))
                    store32(arg0 + 72, (load32(arg0 + 84) & (load8u(v4 + 1) ^ (v2 << load32(arg0 + 88)))))
                    if (v8 != v9):
                        continue
                    break
                v3 = load8u((load32(arg0 + 56) + load32(arg0 + 108)))
                v2 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v2 + load32(arg0 + 5784)), 0)
                v2 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v2 + load32(arg0 + 5784)), 0)
                v2 = load32(arg0 + 5792)
                store32(arg0 + 5792, (load32(arg0 + 5792) + 1))
                store8((v2 + load32(arg0 + 5784)), v3)
                v2 = (arg0 + (v3 << 2))
                store16(((arg0 + (v3 << 2)) + 148), (load16u(v2 + 148) + 1))
                store32(arg0 + 116, (load32(arg0 + 116) - 1))
                v3 = (load32(arg0 + 108) + 1)
                store32(arg0 + 108, (load32(arg0 + 108) + 1))
                if (load32(arg0 + 5792) != load32(arg0 + 5796)):
                    continue
                break
            v6 = 0
            v2 = load32(arg0 + 92)
            if (load32(arg0 + 92) >= 0):
            else:
            store32(arg0 + 92, load32(arg0 + 108))
            v5 = load32(arg0)
            v4 = load32(load32(arg0) + 28)
            while True:  # block $label8
                v3 = load32(v4 + 20)
                v2 = load32(v5 + 16)
                v3 = (load32(v4 + 20) if (u(v2) > u(v3)) else load32(v5 + 16))
                if ((load32(v4 + 20) if (u(v2) > u(v3)) else load32(v5 + 16)) == 0):
                    break
                store32(v5 + 12, (load32(v5 + 12) + v3))
                store32(v4 + 16, (load32(v4 + 16) + v3))
                store32(v5 + 20, (load32(v5 + 20) + v3))
                store32(v5 + 16, (load32(v5 + 16) - v3))
                v2 = load32(v4 + 20)
                store32(v4 + 20, (load32(v4 + 20) - v3))
                if (v2 != v3):
                    break
                store32(v4 + 16, load32(v4 + 8))
                break
            if load32(load32(arg0) + 16):
                continue
            break
        return 0
        break
    v2 = load32(arg0 + 108)
    store32(arg0 + 5812, (2 if (u(v2) >= u(2)) else load32(arg0 + 108)))
    if (arg1 == 4):
        v6 = 0
        arg1 = load32(arg0 + 92)
        if (load32(arg0 + 92) >= 0):
        else:
        store32(arg0 + 92, load32(arg0 + 108))
        v4 = load32(arg0)
        v3 = load32(load32(arg0) + 28)
        while True:  # block $label9
            v2 = load32(v3 + 20)
            arg1 = load32(v4 + 16)
            v2 = (load32(v3 + 20) if (u(arg1) > u(v2)) else load32(v4 + 16))
            if ((load32(v3 + 20) if (u(arg1) > u(v2)) else load32(v4 + 16)) == 0):
                break
            store32(v4 + 12, (load32(v4 + 12) + v2))
            store32(v3 + 16, (load32(v3 + 16) + v2))
            store32(v4 + 20, (load32(v4 + 20) + v2))
            store32(v4 + 16, (load32(v4 + 16) - v2))
            arg1 = load32(v3 + 20)
            store32(v3 + 20, (load32(v3 + 20) - v2))
            if (arg1 != v2):
                break
            store32(v3 + 16, load32(v3 + 8))
            break
        return (3 if load32(load32(arg0) + 16) else 2)
    while True:  # block $label10
        if (load32(arg0 + 5792) == 0):
            break
        v6 = 0
        arg1 = load32(arg0 + 92)
        if (load32(arg0 + 92) >= 0):
        else:
        store32(arg0 + 92, load32(arg0 + 108))
        v4 = load32(arg0)
        v3 = load32(load32(arg0) + 28)
        while True:  # block $label11
            v2 = load32(v3 + 20)
            arg1 = load32(v4 + 16)
            v2 = (load32(v3 + 20) if (u(arg1) > u(v2)) else load32(v4 + 16))
            if ((load32(v3 + 20) if (u(arg1) > u(v2)) else load32(v4 + 16)) == 0):
                break
            store32(v4 + 12, (load32(v4 + 12) + v2))
            store32(v3 + 16, (load32(v3 + 16) + v2))
            store32(v4 + 20, (load32(v4 + 20) + v2))
            store32(v4 + 16, (load32(v4 + 16) - v2))
            arg1 = load32(v3 + 20)
            store32(v3 + 20, (load32(v3 + 20) - v2))
            if (arg1 != v2):
                break
            store32(v3 + 16, load32(v3 + 8))
            break
        if load32(load32(arg0) + 16):
            break
        return 0
        break
    return 1

# ------------------------------------------------------------
# $func824
# ------------------------------------------------------------
def func824(arg0, arg1, param2):
    v19 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label1
        while True:  # block $label0
            while True:  # block $label2
                v5 = load32(9671128)
                v6 = (load32(9671128) + (arg0 * 132))
                v2 = load8u((load32(9671128) + (arg0 * 132)) + 122)
                # br_table[(load8u((load32(9671128) + (arg0 * 132)) + 122) + -64)]
                break
                break
            if (v2 != 10):
                break
            break
        while True:  # block $label3
            v2 = load32(v6 + 20)
            if (load32(v6 + 20) == 0):
                break
            if (u(load32(v2 + 8)) < u(3)):
                break
            if (u((load32(load32(v2)) - 1)) > u(1)):
                break
            store32(v2 + 8, 0)
            break
        v11 = (v5 + (arg1 * 132))
        v14 = load8u((v5 + (arg1 * 132)) + 122)
        while True:  # block $label5
            while True:  # block $label4
                if (load8u(v11 + 125) == 10):
                    v7 = 3
                    v8 = 1
                    break
                v7 = load32(((v14 * 404) + 9568096) + 188)
                if (u(load32(((v14 * 404) + 9568096) + 188)) >= u(4)):
                    func29(v6, 1)
                    break
                v8 = (v7 == 3)
                # br_table[v7]
                break
                break
            v4 = (v5 + (arg0 * 132))
            v9 = load16u((v5 + (arg0 * 132)) + 112)
            v2 = ((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952))
            v3 = load16u(v4 + 114)
            v2 = ((load16u(v4 + 114) << 5) - load32(9142956))
            if ((((((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952)) * v2) + (((load16u(v4 + 114) << 5) - load32(9142956)) * v2)) - 1) > 9000000):
                break
            while True:  # block $label6
                v2 = load32(load32(9142424) + 48)
                if (load32(load32(9142424) + 48) == 0):
                    break
                if load8u(9147152):
                    break
                v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + v9) << 1)))
                if (v2 == 2):
                    if (u(v4) > u(1)):
                        break
                    break
                if (v4 == 0):
                    break
                break
            store32(v19 + 40, v3)
            store32(v19 + 36, v9)
            store32(v19 + 32, load32(((((load32(9142848) + v9) % 3) << 2) + 57224)))
            a_b()
            break
        while True:  # block $label7
            if (v7 == 1):
                v4 = (v5 + (arg0 * 132))
                v9 = load16u((v5 + (arg0 * 132)) + 112)
                v2 = ((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952))
                v3 = load16u(v4 + 114)
                v2 = ((load16u(v4 + 114) << 5) - load32(9142956))
                if ((((((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952)) * v2) + (((load16u(v4 + 114) << 5) - load32(9142956)) * v2)) - 1) > 9000000):
                    break
                while True:  # block $label8
                    v2 = load32(load32(9142424) + 48)
                    if (load32(load32(9142424) + 48) == 0):
                        break
                    if load8u(9147152):
                        break
                    v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + v9) << 1)))
                    if (v2 == 2):
                        if (u(v4) > u(1)):
                            break
                        break
                    if (v4 == 0):
                        break
                    break
                store32(v19 + 8, v3)
                store32(v19 + 4, v9)
                store32(v19, load32(((((load32(9142848) + v9) % 11) << 2) + 57168)))
                a_b()
                break
            if (v7 != 2):
                break
            v20 = 1
            if (load32(38500) != load8u(v11 + 122)):
                break
            v4 = (v5 + (arg0 * 132))
            v9 = load16u((v5 + (arg0 * 132)) + 112)
            v2 = ((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952))
            v3 = load16u(v4 + 114)
            v2 = ((load16u(v4 + 114) << 5) - load32(9142956))
            if ((((((load16u((v5 + (arg0 * 132)) + 112) << 5) - load32(9142952)) * v2) + (((load16u(v4 + 114) << 5) - load32(9142956)) * v2)) - 1) > 9000000):
                break
            while True:  # block $label9
                v2 = load32(load32(9142424) + 48)
                if (load32(load32(9142424) + 48) == 0):
                    break
                if load8u(9147152):
                    break
                v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + v9) << 1)))
                if (v2 == 2):
                    if (u(v4) > u(1)):
                        break
                    break
                if (v4 == 0):
                    break
                break
            store32(v19 + 24, v3)
            store32(v19 + 20, v9)
            store32(v19 + 16, load32(((((load32(9142848) + v9) % 3) << 2) + 57212)))
            a_b()
            break
        v17 = load32(38528)
        v12 = load8u(v11 + 122)
        v9 = (v5 + (arg0 * 132))
        if (load8u((v5 + (arg0 * 132)) + 125) == 1):
            v8 = (v12 != v17)
            if ((v20 & (v12 != v17)) == 0):
                v4 = ((v14 * 404) + 9568096)
                v3 = load32(((v14 * 404) + 9568096) + 220)
                v2 = (v5 + (arg1 * 132))
                v18 = load16u((v5 + (arg1 * 132)) + 114)
                v21 = (load32(((v14 * 404) + 9568096) + 220) + load16u((v5 + (arg1 * 132)) + 114))
                v4 = load32(v4 + 216)
                v17 = load16u(v2 + 112)
                v14 = (load32(v4 + 216) + load16u(v2 + 112))
                v2 = (v5 + (arg0 * 132))
                v13 = load16u((v5 + (arg0 * 132)) + 114)
                while True:  # block $label11
                    while True:  # block $label10
                        v15 = load16u(v2 + 112)
                        v2 = (u(load16u(v2 + 112)) < u(v17))
                        if (u(load16u(v2 + 112)) < u(v17)):
                            break
                        if (v14 <= v15):
                            break
                        if (u(v13) < u(v18)):
                            break
                        if (v13 >= v21):
                            break
                        v2 = ((v3 // 2) + v18)
                        v10 = (-1 if (v2 < v13) else (((v3 // 2) + v18) != v13))
                        v2 = ((v4 // 2) + v17)
                        break
                        break
                    v10 = (1 if (u(v13) < u(v18)) else (-1 if (v13 >= v21) else 0))
                    break
                v2 = (((1 if v2 else (-1 if (v14 <= v15) else 0)) + (v10 * 3)) + 4)
                if (u((((1 if v2 else (-1 if (v14 <= v15) else 0)) + (v10 * 3)) + 4)) <= u(8)):
                else:
                store8(load8u((v2 + 10184)) + 124, 6)
            v2 = load8u(v6 + 122)
            while True:  # block $label12
                if (v7 == 1):
                    break
                if v20:
                    if (v8 == 0):
                        func119(func37(v6, load32(((v2 * 72) + 9263856) + 56), 0.0, 0), v11, 12, 1)
                        store32((v5 + (arg1 * 132)) + 96, 0)
                        break
                    break
                break
            v8 = (v5 + (arg0 * 132))
            store16((v5 + (arg0 * 132)) + 108, 0)
            store32(v8 + 88, 0)
            v2 = load32(((load32((load32(9215884) + (load32(v8 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v8 + 44) << 4)) + 4) * 40) + 9671200) + 32):
                # call_indirect[v2]
            if (load8u(v9 + 125) == 3):
                break
            v4 = load32(v8 + 44)
            if load32(v8 + 44):
                v2 = load32(9142848)
                v3 = load32(9215884)
                store32((load32(9215884) + (v4 << 4)) + 4, 1)
                store32((v3 + (load32(v8 + 44) << 4)) + 8, load32((v5 + (arg0 * 132)) + 28))
                store32((v3 + (load32(v8 + 44) << 4)) + 12, arg1)
                store32((v3 + (load32(v8 + 44) << 4)), (v2 + 40))
                break
            store32(v8 + 44, ((Ua(1000, 1, load32((v5 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        while True:  # block $label21
            while True:  # block $label18
                while True:  # block $label20
                    while True:  # block $label19
                        while True:  # block $label17
                            if (load8u(v11 + 125) == 3):
                                if (v7 == 1):
                                    v7 = load32(9671128)
                                    arg0 = (v5 + (arg0 * 132))
                                    v15 = load16u(arg0 + 110)
                                    arg0 = (load32(9671128) + (func166(load16u((v5 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), 1) * 132))
                                    v16 = load16u((load32(9671128) + (func166(load16u((v5 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), 1) * 132)) + 112)
                                    v18 = (load16u((load32(9671128) + (func166(load16u((v5 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), 1) * 132)) + 112) + 29)
                                    v5 = load16u(arg0 + 114)
                                    v21 = (load16u(arg0 + 114) + 29)
                                    v2 = (v5 - 30)
                                    arg1 = (v16 - 30)
                                    v11 = load32(9142440)
                                    v17 = (load32(9142440) + 2)
                                    v14 = ((load32(9142440) + 2) * load32(((v12 * 404) + 9568096) + 208))
                                    v9 = load32(9142840)
                                    v20 = 2147483647
                                    while True:  # $label15
                                        v4 = (arg1 + 1)
                                        if (u(arg1) < u(v11)):
                                            arg0 = (v16 - arg1)
                                            v8 = ((v16 - arg1) * arg0)
                                            arg0 = v2
                                            while True:  # $label14
                                                while True:  # block $label13
                                                    v3 = arg0
                                                    if (u(v11) <= u(arg0)):
                                                        break
                                                    if ((arg1 | v3) < 0):
                                                        break
                                                    arg0 = (v5 - v3)
                                                    arg0 = (((v5 - v3) * arg0) + v8)
                                                    if ((((v5 - v3) * arg0) + v8) >= v20):
                                                        break
                                                    v13 = load32((v9 + (((((v3 + v14) + 1) * v17) + v4) << 2)))
                                                    if (load32((v9 + (((((v3 + v14) + 1) * v17) + v4) << 2))) == 0):
                                                        break
                                                    arg0 = (load8u((v7 + (v13 * 132)) + 122) == v12)
                                                    v20 = (arg0 if (load8u((v7 + (v13 * 132)) + 122) == v12) else v20)
                                                    v10 = (v13 if arg0 else v10)
                                                    break
                                                arg0 = (v3 + 1)
                                                if (v3 != v21):
                                                    continue
                                                break
                                        arg0 = (arg1 != v18)
                                        arg1 = v4
                                        if arg0:
                                            continue
                                        break
                                    if v10:
                                        while True:  # block $label16
                                            if (load32((load32(9561692) + (v15 * 286704)) + 286684) == 0):
                                                break
                                            arg1 = (v7 + (v10 * 132))
                                            arg0 = (v16 - load16u((v7 + (v10 * 132)) + 112))
                                            arg0 = (v5 - load16u(arg1 + 114))
                                            if (((((v16 - load16u((v7 + (v10 * 132)) + 112)) * arg0) + ((v5 - load16u(arg1 + 114)) * arg0)) - 1) < 50):
                                                break
                                            break
                                            break
                                        break
                                    func29(v6, 1)
                                    break
                                if (v12 == v17):
                                    v2 = load32((v5 + (arg0 * 132)) + 88)
                                    store32((v5 + (arg1 * 132)) + 72, 0)
                                    # TODO: i32.div_u []
                                    break
                                func29(v6, 1)
                                break
                            if (v12 != v17):
                                break
                            v3 = (v5 + (arg1 * 132))
                            v4 = load32((v5 + (arg1 * 132)) + 72)
                            if (u(load32((v5 + (arg1 * 132)) + 72)) > u(3)):
                                break
                            v2 = load32((v5 + (arg0 * 132)) + 88)
                            store32(v3 + 72, 0)
                            store8(v11 + 125, 0)
                            # TODO: i32.div_u []
                            break
                        v3 = (1000 + v4)
                        if load32(load32(9142424) + 176):
                            break
                        v2 = (v5 + (arg1 * 132))
                        if (u(load32((v5 + (arg1 * 132)) + 80)) < u(load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284320)))):
                            break
                        break
                        break
                    store32(v3 + 72, (v4 - 3))
                    v3 = 0
                    break
                v4 = load32(9671128)
                if (load32((load32(9671128) + (arg1 * 132)) + 92) == 0):
                    break
                v2 = load8u(9147141)
                if load32(9140316):
                    if (load32(9140320) != load32((v4 + (arg1 * 132)) + 28)):
                        break
                break
                break
            v3 = 0
            store32((v5 + (arg1 * 132)) + 88, load32(9142848))
            break
        v5 = load32(9671128)
        v11 = (load32(9671128) + (arg0 * 132))
        v2 = (load32((load32(9671128) + (arg0 * 132)) + 88) + 1000)
        if ((((load32((load32(9671128) + (arg0 * 132)) + 88) + 1000) == load32(((v7 << 2) + 51760))) & (v12 != v17)) | v3):
            v4 = (v5 + (arg0 * 132))
            if (v12 != v17):
            else:
            store16(load32((((load32(9561692) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + (v7 << 2)) + 283984)) + 108, v3)
            v2 = (v5 + (arg1 * 132))
            store32(v11 + 88, ((load8u((v5 + (arg1 * 132)) + 122) << 16) + v7))
            func207(v11, load32(v2 + 28))
            while True:  # block $label22
                if v20:
                    break
                v20 = load16u(v4 + 108)
                while True:  # block $label24
                    while True:  # block $label23
                        # br_table[v7]
                        break
                        break
                    # TODO: i32.div_u []
                    v20 = load32(((load32(9561692) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + 284100))
                    break
                if (load8u((v5 + (arg1 * 132)) + 125) == 10):
                    break
                v9 = (10 if (v7 == 1) else v20)
                v3 = (G.global0 - 16)
                G.global0 = (G.global0 - 16)
                while True:  # block $label25
                    v14 = (v5 + (arg1 * 132))
                    if (load8u((v5 + (arg1 * 132)) + 125) == 3):
                        break
                    arg1 = load32(v14 + 64)
                    if (u(v9) >= u(load32(v14 + 64))):
                        store32(v14 + 64, 0)
                        break
                    store32(v14 + 64, (arg1 - v9))
                    if (load32(v14 + 92) == 0):
                        break
                    if load8u(9147141):
                        break
                    store32(v3, v9)
                    a_b()
                    break
                G.global0 = (v3 + 16)
                break
            while True:  # block $label26
                if (load32(v4 + 92) == 0):
                    break
                if load32(9140316):
                    if (load32(9140320) != load32((v5 + (arg0 * 132)) + 28)):
                        break
                break
            arg1 = (0 if v8 else v7)
            while True:  # block $label27
                v9 = load8u(v2 + 122)
                if (load8u(v2 + 122) != load32(38508)):
                    if (load32(38504) != v9):
                        break
                v17 = (v5 + (arg0 * 132))
                v10 = load16u((v5 + (arg0 * 132)) + 112)
                v3 = load16u(v17 + 110)
                v13 = (v10 + 1)
                v12 = load32(9142440)
                v6 = (load32(9142440) + 2)
                v15 = load32(9671128)
                v18 = load32(9142840)
                while True:  # block $label30
                    while True:  # block $label28
                        v16 = load16u(v17 + 114)
                        v4 = (u(v12) <= u(load16u(v17 + 114)))
                        if (u(v12) <= u(load16u(v17 + 114))):
                            break
                        if (u(v12) <= u(v13)):
                            break
                        if ((v13 | v16) < 0):
                            break
                        v2 = load32((((v10 + (((v6 + v16) + 1) * v6)) << 2) + v18) + 8)
                        if (u(load32((((v10 + (((v6 + v16) + 1) * v6)) << 2) + v18) + 8)) < u(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # block $label29
                            # br_table[(load8u(v2 + 125) - 4)]
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + 9568096) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # block $label31
                        v14 = (v16 - 1)
                        v8 = (u(v12) <= u((v16 - 1)))
                        if (u(v12) <= u((v16 - 1))):
                            break
                        if (u(v12) <= u(v13)):
                            break
                        if ((v13 | v14) < 0):
                            break
                        v2 = load32((((v10 + ((v6 + v16) * v6)) << 2) + v18) + 8)
                        if (u(load32((((v10 + ((v6 + v16) * v6)) << 2) + v18) + 8)) < u(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # block $label32
                            # br_table[(load8u(v2 + 125) - 4)]
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + 9568096) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # block $label33
                        if v8:
                            break
                        if (u(v10) >= u(v12)):
                            break
                        if ((v10 | v14) < 0):
                            break
                        v2 = load32((v18 + ((v13 + ((v6 + v16) * v6)) << 2)))
                        if (u(load32((v18 + ((v13 + ((v6 + v16) * v6)) << 2)))) < u(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # block $label34
                            # br_table[(load8u(v2 + 125) - 4)]
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + 9568096) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    v21 = (v10 - 1)
                    while True:  # block $label35
                        if v8:
                            break
                        if (u(v12) <= u(v21)):
                            break
                        if ((v14 | v21) < 0):
                            break
                        v2 = load32((v18 + ((((v6 + v16) * v6) + v10) << 2)))
                        if (u(load32((v18 + ((((v6 + v16) * v6) + v10) << 2)))) < u(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # block $label36
                            # br_table[(load8u(v2 + 125) - 4)]
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + 9568096) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    v8 = (v16 + 1)
                    while True:  # block $label37
                        if v4:
                            break
                        if (u(v12) <= u(v21)):
                            break
                        if ((v16 | v21) < 0):
                            break
                        v2 = load32((v18 + ((((v6 + v8) * v6) + v10) << 2)))
                        if (u(load32((v18 + ((((v6 + v8) * v6) + v10) << 2)))) < u(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # block $label38
                            # br_table[(load8u(v2 + 125) - 4)]
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + 9568096) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # block $label39
                        v4 = (u(v8) >= u(v12))
                        if (u(v8) >= u(v12)):
                            break
                        if (u(v12) <= u(v21)):
                            break
                        if ((v8 | v21) < 0):
                            break
                        v2 = load32((v18 + (((((v6 + v16) + 2) * v6) + v10) << 2)))
                        if (u(load32((v18 + (((((v6 + v16) + 2) * v6) + v10) << 2)))) < u(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # block $label40
                            # br_table[(load8u(v2 + 125) - 4)]
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + 9568096) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # block $label41
                        if v4:
                            break
                        if (u(v10) >= u(v12)):
                            break
                        if ((v8 | v10) < 0):
                            break
                        v2 = load32((v18 + ((v13 + (((v6 + v16) + 2) * v6)) << 2)))
                        if (u(load32((v18 + ((v13 + (((v6 + v16) + 2) * v6)) << 2)))) < u(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # block $label42
                            # br_table[(load8u(v2 + 125) - 4)]
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + 9568096) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    while True:  # block $label43
                        if v4:
                            break
                        if (u(v12) <= u(v13)):
                            break
                        if ((v8 | v13) < 0):
                            break
                        v2 = load32((((v10 + (((v6 + v16) + 2) * v6)) << 2) + v18) + 8)
                        if (u(load32((((v10 + (((v6 + v16) + 2) * v6)) << 2) + v18) + 8)) < u(3)):
                            break
                        v2 = (v15 + (v2 * 132))
                        if (load16u((v15 + (v2 * 132)) + 110) != v3):
                            break
                        while True:  # block $label44
                            # br_table[(load8u(v2 + 125) - 4)]
                            break
                            break
                        v7 = 1
                        v2 = load32(((load8u(v2 + 122) * 404) + 9568096) + 192)
                        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 192) == arg1):
                            break
                        if (v2 == 4):
                            break
                        break
                    v7 = 0
                    break
                if v7:
                    store32(v11 + 88, 0)
                    store32((load32(9215884) + (load32(v17 + 44) << 4)), (load32(9142848) + 40))
                    break
                if (load32((load32(9561692) + (v3 * 286704)) + 286684) == 0):
                    break
                if func87(v11, v9):
                    break
                break
            arg0 = (v5 + (arg0 * 132))
            arg0 = func166(load16u((v5 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), arg1)
            if func166(load16u((v5 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), arg1):
                break
            func29(v11, 1)
            break
        store32(v11 + 88, v2)
        store32((load32(9215884) + (load32((v5 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
        break
    G.global0 = (v19 + 48)
    return func28(1, 1)

# ------------------------------------------------------------
# $func825
# ------------------------------------------------------------
def func825(arg0):
    v1 = 3
    while True:  # block $label3
        while True:  # block $label0
            while True:  # block $label1
                v7 = load32(9671128)
                v5 = load32(arg0 + 32)
                v2 = (load32(9671128) + (load32(arg0 + 32) * 132))
                v6 = load8u((load32(9671128) + (load32(arg0 + 32) * 132)) + 125)
                if (load8u((load32(9671128) + (load32(arg0 + 32) * 132)) + 125) != 10):
                    v3 = 1
                    v4 = load8u(v2 + 122)
                    v1 = load32(((load8u(v2 + 122) * 404) + 9568096) + 188)
                    if (u(load32(((load8u(v2 + 122) * 404) + 9568096) + 188)) > u(3)):
                        break
                    if v6:
                        break
                v4 = load8u(v2 + 122)
                while True:  # block $label2
                    if (load8u(arg0 + 125) != 7):
                        break
                    if (load32(38504) == v4):
                        break
                    if (load32(38508) != v4):
                        break
                    break
                v3 = 0
                if (load32(38500) != v4):
                    break
                v2 = (v7 + (v5 * 132))
                v6 = (load32(9142440) + 2)
                v2 = load32((load32(9142840) + ((load16u((v7 + (v5 * 132)) + 112) + ((((load32(9142440) + 2) + load16u(v2 + 114)) + 2) * v6)) << 2)) + 8)
                if (load32((load32(9142840) + ((load16u((v7 + (v5 * 132)) + 112) + ((((load32(9142440) + 2) + load16u(v2 + 114)) + 2) * v6)) << 2)) + 8) == 0):
                    break
                if (v2 == load32(arg0 + 28)):
                    break
                break
            v3 = 0
            if (v4 != load32(38528)):
                if (load32(38504) == v4):
                    break
                if (load32(38508) == v4):
                    break
                v1 = func335(load16u(arg0 + 112), load16u(arg0 + 114), load32(((v1 << 2) + 9680)), v5)
                if (func335(load16u(arg0 + 112), load16u(arg0 + 114), load32(((v1 << 2) + 9680)), v5) == 0):
                    break
                break
            v5 = load32(9142440)
            v6 = (load32(9142440) + 3)
            v8 = (v5 + 2)
            v9 = load32(9142840)
            v10 = load16u(arg0 + 114)
            v11 = load16u(arg0 + 112)
            v12 = load16u(arg0 + 110)
            v1 = 0
            while True:  # block $label7
                while True:  # $label6
                    while True:  # block $label5
                        while True:  # block $label4
                            v3 = v1
                            v2 = (v1 << 2)
                            v1 = (load32((((v1 << 2) | 4) + 8611904)) + v10)
                            if (u(v5) <= u((load32((((v1 << 2) | 4) + 8611904)) + v10))):
                                break
                            v2 = (load32((v2 + 8611904)) + v11)
                            if (u(v5) <= u((load32((v2 + 8611904)) + v11))):
                                break
                            if ((v1 | v2) < 0):
                                break
                            v2 = load32((((v2 + ((v1 + v6) * v8)) << 2) + v9) + 4)
                            v1 = (v7 + (load32((((v2 + ((v1 + v6) * v8)) << 2) + v9) + 4) * 132))
                            if (v4 != load8u((v7 + (load32((((v2 + ((v1 + v6) * v8)) << 2) + v9) + 4) * 132)) + 122)):
                                break
                            if (u(load32(v1 + 72)) < u(50)):
                                break
                            if (load8u(v1 + 125) == 12):
                                break
                            if (load16u(v1 + 110) != v12):
                                break
                            if (load32(v1 + 96) == 0):
                                break
                            break
                        v1 = (v3 + 2)
                        if (u(v3) <= u(16557)):
                            continue
                        break
                        break
                    break
                v1 = load32((v7 + (v2 * 132)) + 28)
                if load32((v7 + (v2 * 132)) + 28):
                    break
                break
            store8(arg0 + 129, 10)
            store32(arg0 + 32, 0)
            v3 = 1
            break
        return v3
        break
    store32(arg0 + 32, v1)
    return 0

# ------------------------------------------------------------
# $func826
# ------------------------------------------------------------
def func826(arg0, arg1, arg2, arg3, arg4):
    while True:  # block $label0
        arg3 = load32(9671128)
        arg2 = (load32(9671128) + (load32(arg1) * 132))
        if (load8u((load32(9671128) + (load32(arg1) * 132)) + 125) != 10):
            if (u(load32(((load8u(arg2 + 122) * 404) + 9568096) + 188)) > u(3)):
                break
        arg2 = (arg3 + (arg0 * 132))
        arg4 = load32((arg3 + (arg0 * 132)) + 88)
        if (load32((arg3 + (arg0 * 132)) + 88) == 0):
            return 0
        if (load16u(arg2 + 108) == 0):
            break
        arg1 = ((arg4 & 0xFFFFFFFF) >> 16)
        arg4 = (arg4 & 65535)
        if (((arg4 & 0xFFFFFFFF) >> 16) != ((arg4 & 65535) if (arg4 != 3) else 0)):
            break
        arg0 = (arg3 + (arg0 * 132))
        arg0 = func166(load16u((arg3 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), arg1)
        if func166(load16u((arg3 + (arg0 * 132)) + 112), load16u(arg0 + 114), load16u(arg0 + 110), arg1):
            return 1
        func29(arg2, 1)
        break
    return 1

# ------------------------------------------------------------
# $func827
# ------------------------------------------------------------
def func827(arg0):
    while True:  # block $label0
        v1 = load32(9671128)
        arg0 = (v1 + (arg0 * 132))
        v1 = load32((v1 + (arg0 * 132)) + 32)
        v3 = load8u((load32(9671128) + (load32((v1 + (arg0 * 132)) + 32) * 132)) + 122)
        if (load8u((load32(9671128) + (load32((v1 + (arg0 * 132)) + 32) * 132)) + 122) != load32(38448)):
            break
        v1 = func335(load16u(arg0 + 112), load16u(arg0 + 114), v3, v1)
        if (func335(load16u(arg0 + 112), load16u(arg0 + 114), v3, v1) == 0):
            break
        store32(arg0 + 32, v1)
        func140(arg0)
        v2 = 1
        break
    return v2

# ------------------------------------------------------------
# $func830
# ------------------------------------------------------------
def func830(arg0, arg1, arg2):
    func397(load32(arg0), arg1, arg2)

# ------------------------------------------------------------
# $func831
# ------------------------------------------------------------
def func831(arg0, arg1, arg2):
    if load8u(9142388):
        v5 = load32(9561692)
        v3 = load32(arg0)
        while True:  # block $label0
            v7 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v6 = load32(59164)
            arg0 = 1
            while True:  # $label1
                v8 = (v5 + (arg0 * 286704))
                if (v6 == load32((v5 + (arg0 * 286704)) + 284616)):
                    v4 = arg0
                    break
                if (v6 == load32(v8 + 284628)):
                    v4 = arg0
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v7):
                    continue
                break
            break
        store32((v5 + (v4 * 286704)) + 284632, v3)
        while True:  # block $label2
            if (u(load32(9561744)) >= u(v3)):
                break
            store32(9561744, v3)
            if (arg2 == 0):
                break
            arg0 = load32(9561736)
            if load32(9561736):
                store32(9561736, 0)
            v4 = (arg2 << 2)
            arg0 = func26((-1 if (u(arg2) > u(1073741823)) else (arg2 << 2)))
            store32(9561740, arg2)
            store32(9561736, arg0)
            # TODO: memory.copy []
            break
        if (u(v3) < u(load32(9561748))):
            store32(9561748, v3)

# ------------------------------------------------------------
# $func832
# ------------------------------------------------------------
def func832(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label2
        v6 = load32(arg0)
        if (u(load32(arg0)) < u(load32(59176))):
            while True:  # block $label0
                v4 = load32(9561704)
                if load32(9561704):
                    arg0 = 0
                    v5 = load32(9561696)
                    while True:  # $label1
                        v3 = ((arg0 << 2) + v5)
                        if (u(v6) <= u(load32(((arg0 << 2) + v5) + 4))):
                            v3 = (v4 - arg0)
                            break
                        arg0 = (load32(v3 + 8) + arg0)
                        if (u(v4) > u((load32(v3 + 8) + arg0))):
                            continue
                        break
                    v3 = 0
                break
            func71((v5 + (arg0 << 2)), 0, v3, 59176, 1, 1)
            break
        func71(35, 0, 0, 59176, 1, 1)
        break
    v4 = load32(9142892)
    if (u(load32(9142892)) >= u(2)):
        v5 = load32(9561692)
        arg0 = 1
        while True:  # $label4
            while True:  # block $label3
                if (load32((arg1 + (arg0 << 2))) == 0):
                    break
                v3 = (v5 + (arg0 * 286704))
                if load32((v5 + (arg0 * 286704)) + 284616):
                    break
                store32((v3 + 284616), load32(v3 + 284628))
                store8(v3 + 286699, 0)
                v4 = load32(v3 + 283908)
                v3 = load8u(v3 + 286696)
                store32(arg2 + 8, 0)
                store32(arg2 + 4, v3)
                store32(arg2, v4)
                a_b()
                v4 = load32(9142892)
                v5 = load32(9561692)
                break
            arg0 = (arg0 + 1)
            if (u((arg0 + 1)) < u(v4)):
                continue
            break
    G.global0 = (arg2 + 16)
    return arg2

# ------------------------------------------------------------
# $func834
# ------------------------------------------------------------
def func834(arg0, arg1):
    store8(9163793, arg0)
    while True:  # block $label0
        if (arg0 == 0):
            break
        if (load32(9671176) == 0):
            break
        arg1 = load32(38620)
        v2 = load32(38560)
        arg0 = load32(load32(9671168))
        v2 = (load32(38620) if (arg0 == v2) else (load32(38560) if (arg0 == arg1) else load32(load32(9671168))))
        arg1 = ((load32(38620) if (arg0 == v2) else (load32(38560) if (arg0 == arg1) else load32(load32(9671168)))) + 1)
        arg1 = load32(38604)
        arg1 = (((load32(38620) if (arg0 == v2) else (load32(38560) if (arg0 == arg1) else load32(load32(9671168)))) + 1) if (arg0 == arg1) else (arg1 if (arg0 == load32(38608)) else (arg1 if (arg0 == load32(38612)) else (load32(38604) if (arg0 == load32(38616)) else v2))))
        while True:  # block $label2
            while True:  # block $label1
                v2 = load32(38624)
                if (load32(38624) != arg0):
                    if (arg0 != load32(38628)):
                        break
                break
                break
            v3 = load32(39056)
            if (arg0 == load32(38632)):
                break
            break
        v3 = (v2 if (arg0 == v3) else arg1)
        if ((arg1 + 1) == (v2 if (arg0 == v3) else arg1)):
            break
        if load32(9671192):
            arg0 = 0
            while True:  # $label3
                func38(load32((load32(9671184) + (arg0 << 2))))
                arg0 = (arg0 + 1)
                if (u((arg0 + 1)) < u(load32(9671192))):
                    continue
                break
        arg0 = 0
        store32(9671192, 0)
        store32(9671176, 0)
        store8(9142412, 0)
        if load8u(9684396):
            store8(9684396, 0)
            a_b()
            arg0 = load32(9671176)
        while True:  # block $label4
            arg1 = load32(9671172)
            if (u(load32(9671172)) > u((arg0 + 3))):
                arg1 = load32(9671168)
                break
            arg1 = ((arg1 + load32(9671180)) + 3)
            store32(9671172, ((arg1 + load32(9671180)) + 3))
            v2 = load32(9671168)
            arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
            if arg0:
                # TODO: memory.copy []
            if v2:
                arg0 = load32(9671176)
            store32(9671168, arg1)
            break
        store32(9671176, (arg0 + 1))
        store32((arg1 + (arg0 << 2)), v3)
        arg0 = load32(9671176)
        store32(9671176, (load32(9671176) + 1))
        store32((arg1 + (arg0 << 2)), 0)
        arg0 = load32(9671176)
        store32(9671176, (load32(9671176) + 1))
        store32((arg1 + (arg0 << 2)), 0)
        if (load8u(9147152) == 0):
            break
        store8(9142412, 1)
        break
    return func132(2147483647, 2147483647)

# ------------------------------------------------------------
# $func837
# ------------------------------------------------------------
def func837(arg0, arg1):
    func146(arg0, load32(38940))

# ------------------------------------------------------------
# $func838
# ------------------------------------------------------------
def func838(arg0, arg1):
    func146(arg0, load32(38932))

# ------------------------------------------------------------
# $func839
# ------------------------------------------------------------
def func839(arg0, arg1):
    func146(arg0, load32(38936))

# ------------------------------------------------------------
# $func840
# ------------------------------------------------------------
def func840(arg0, arg1):
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v2 + 28, (arg0 & 65535))
    store32(v2 + 24, ((arg0 & 0xFFFFFFFF) >> 16))
    v3 = (arg1 & 65535)
    arg0 = (((arg1 & 65535) * 404) + 9568096)
    arg0 = load32(v2 + 28)
    arg1 = load32(v2 + 24)
    while True:  # block $label2
        while True:  # block $label1
            while True:  # block $label0
                v5 = load32(load32(9142424) + 48)
                if load32(load32(9142424) + 48):
                    if (load8u(9147152) == 0):
                        break
                v3 = load32(9142440)
                break
                break
            v3 = load32(9142440)
            v4 = load16u((load32(9147376) + (((load32(9142440) * arg1) + arg0) << 1)))
            if (v5 == 2):
                if (u(v4) > u(1)):
                    break
                break
            if (v4 == 0):
                break
            break
        # TODO: f32.convert_i32_u []
        func80(float(arg0), float(arg1), load32(9142536), 32.0, (v3 * 96))
        break
    while True:  # block $label3
        v3 = ((arg0 << 5) - load32(9142952))
        v3 = ((arg1 << 5) - load32(9142956))
        if ((((((arg0 << 5) - load32(9142952)) * v3) + (((arg1 << 5) - load32(9142956)) * v3)) - 1) > 9000000):
            break
        while True:  # block $label4
            v4 = load32(load32(9142424) + 48)
            if (load32(load32(9142424) + 48) == 0):
                break
            if load8u(9147152):
                break
            v3 = load16u((load32(9147376) + (((load32(9142440) * arg1) + arg0) << 1)))
            if (v4 == 2):
                if (u(v3) > u(1)):
                    break
                break
            if (v3 == 0):
                break
            break
        store32(v2 + 8, arg1)
        store32(v2 + 4, arg0)
        store32(v2, load32(((((load32(9142848) + arg0) % 10) << 2) + 57744)))
        a_b()
        break
    G.global0 = (v2 + 32)

# ------------------------------------------------------------
# $func841
# ------------------------------------------------------------
def func841(arg0, arg1, arg2):
    arg2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label0
        v7 = load32(9671128)
        v4 = load32(arg1)
        v5 = (load32(9671128) + (load32(arg1) * 132))
        if (load8u((load32(9671128) + (load32(arg1) * 132)) + 125) == 3):
            break
        arg1 = load32(v5 + 20)
        if (load32(v5 + 20) == 0):
            break
        arg1 = load32(arg0)
        arg0 = load32((load32(arg1) + (load32(arg0) << 2)))
        if (load32((load32(arg1) + (load32(arg0) << 2))) == 0):
            break
        v6 = (arg0 - 1)
        v3 = (((arg0 - 1) * 404) + 9568096)
        v8 = load32(9561692)
        v7 = load16u((v7 + (v4 * 132)) + 110)
        arg0 = (load32(9561692) + (load16u((v7 + (v4 * 132)) + 110) * 286704))
        v9 = load32((((load32(9561692) + (load16u((v7 + (v4 * 132)) + 110) * 286704)) + (load32(39136) << 2)) + 281808))
        store32(arg2, (((load32((((arg0 - 1) * 404) + 9568096) + 68) * 144) // 10) + (120 if (load32((((load32(9561692) + (load16u((v7 + (v4 * 132)) + 110) * 286704)) + (load32(39136) << 2)) + 281808)) == 1) else 0)))
        store32(arg2 + 4, ((load32(v3 + 72) * 144) // 10))
        store32(arg2 + 8, ((load32(v3 + 76) * 144) // 10))
        store32(arg2 + 12, ((load32(v3 + 80) * 144) // 10))
        while True:  # block $label2
            while True:  # block $label1
                v3 = (load32(arg0 + 283976) + 1)
                if (u((load32(arg0 + 283976) + 1)) > u((load32((arg0 + 284136)) + load32(arg0 + 283980)))):
                    arg1 = 57101
                    if (load32(arg0 + 283908) == load32(9142872)):
                        break
                    break
                if (u(v3) <= u(load32((arg0 + 284000)))):
                    break
                arg1 = 57113
                if (load32((v8 + (v7 * 286704)) + 283908) != load32(9142872)):
                    break
                break
            a_b()
            break
            break
        if func66(arg0, arg2, 1, 1):
            break
        arg0 = load32(load32(v5 + 20))
        while True:  # block $label3
            if (u(arg1) >= u(7)):
                break
            v3 = (arg1 + 1)
            v5 = (arg0 + ((arg1 + 1) << 2))
            store32((arg0 + (arg1 << 2)), load32((arg0 + ((arg1 + 1) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 2)
            store32(v5, load32((arg0 + ((arg1 + 2) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 3)
            v5 = (arg0 + ((arg1 + 3) << 2))
            store32((arg0 + (v3 << 2)), load32((arg0 + ((arg1 + 3) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 4)
            store32(v5, load32((arg0 + ((arg1 + 4) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 5)
            v5 = (arg0 + ((arg1 + 5) << 2))
            store32((arg0 + (v3 << 2)), load32((arg0 + ((arg1 + 5) << 2))))
            if (v3 == 7):
                break
            v3 = (arg1 + 6)
            store32(v5, load32((arg0 + ((arg1 + 6) << 2))))
            if (v3 == 7):
                break
            store32((arg0 + (v3 << 2)), load32(((arg1 << 2) + arg0) + 28))
            break
        arg1 = 0
        store32(arg0 + 28, 0)
        arg0 = ((v8 + (v7 * 286704)) + 281744)
        store32(((v8 + (v7 * 286704)) + 281744), (load32(arg0) + 9))
        arg0 = ((v6 * 404) + 9568096)
        while True:  # block $label6
            if (v9 == 1):
                v5 = (v4 * 132)
                while True:  # $label5
                    while True:  # block $label4
                        v3 = (load32(9671128) + v5)
                        if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + v5), arg0) == 0):
                            break
                        v8 = func34(v6, load16u(v3 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                        if (func34(v6, load16u(v3 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                            break
                        v7 = load32(9671128)
                        v3 = (load32(9671128) + (v8 * 132))
                        if load32((load32(9671128) + (v8 * 132)) + 28):
                            store32(v3 + 84, 4)
                            store32(v3 + 52, (load32(v3 + 52) + 4))
                            store32(v3 + 60, (load32(v3 + 60) + 2))
                        func69((v5 + v7), v8)
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != 9):
                        continue
                    break
                break
            while True:  # block $label7
                arg1 = (load32(9671128) + (v4 * 132))
                if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                    break
                func69((load32(9671128) + (v4 * 132)), arg1)
                break
            while True:  # block $label8
                arg1 = (load32(9671128) + (v4 * 132))
                if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                    break
                func69((load32(9671128) + (v4 * 132)), arg1)
                break
            while True:  # block $label9
                arg1 = (load32(9671128) + (v4 * 132))
                if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                    break
                func69((load32(9671128) + (v4 * 132)), arg1)
                break
            while True:  # block $label10
                arg1 = (load32(9671128) + (v4 * 132))
                if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                    break
                func69((load32(9671128) + (v4 * 132)), arg1)
                break
            while True:  # block $label11
                arg1 = (load32(9671128) + (v4 * 132))
                if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                    break
                func69((load32(9671128) + (v4 * 132)), arg1)
                break
            while True:  # block $label12
                arg1 = (load32(9671128) + (v4 * 132))
                if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                    break
                func69((load32(9671128) + (v4 * 132)), arg1)
                break
            while True:  # block $label13
                arg1 = (load32(9671128) + (v4 * 132))
                if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                    break
                func69((load32(9671128) + (v4 * 132)), arg1)
                break
            while True:  # block $label14
                arg1 = (load32(9671128) + (v4 * 132))
                if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                    break
                arg1 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
                if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                    break
                func69((load32(9671128) + (v4 * 132)), arg1)
                break
            arg1 = (load32(9671128) + (v4 * 132))
            if (func59((arg2 + 28), (arg2 + 24), (load32(9671128) + (v4 * 132)), arg0) == 0):
                break
            arg0 = func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
            if (func34(v6, load16u(arg1 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1) == 0):
                break
            func69((load32(9671128) + (v4 * 132)), arg0)
            break
        if (load32(9671124) != 95):
            break
        if (load32(9173808) != v4):
            break
        break
    G.global0 = (arg2 + 32)

# ------------------------------------------------------------
# $func842
# ------------------------------------------------------------
def func842(arg0, arg1):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if load8u(9147152):
            break
        v5 = load32(9671128)
        v2 = (load32(9671128) + (arg0 * 132))
        v10 = load16u((load32(9671128) + (arg0 * 132)) + 110)
        v8 = load32(((load32(9561692) + (load16u((load32(9671128) + (arg0 * 132)) + 110) * 286704)) + 284324))
        if (load32(((load32(9561692) + (load16u((load32(9671128) + (arg0 * 132)) + 110) * 286704)) + 284324)) == 0):
            break
        v4 = load32(v2 + 80)
        # TODO: i32.div_u []
        v11 = v8
        if (u(v4) >= u(v8)):
            while True:  # block $label1
                v2 = (arg0 * 132)
                if (func225((arg1 + 12), (arg1 + 8), (v5 + (arg0 * 132)), ((load32(38984) * 404) + 9568096)) == 0):
                    break
                v2 = func34(load32(38984), load16u((load32(9671128) + v2) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1)
                if (func34(load32(38984), load16u((load32(9671128) + v2) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1) == 0):
                    break
                v5 = load32(9671128)
                v2 = (load32(9671128) + (v2 * 132))
                store64((load32(9671128) + (v2 * 132)) + 64, 1073741824250)
                store32(v2 + 56, v10)
                store32(v2 + 52, v8)
                v16 = load16u((v5 + (arg0 * 132)) + 110)
                v9 = load32(9142440)
                v14 = load16u(v2 + 114)
                v15 = load16u(v2 + 112)
                while True:  # $label8
                    while True:  # block $label7
                        while True:  # block $label2
                            v5 = v3
                            v3 = (v3 << 2)
                            v7 = (load32((((v3 << 2) | 4) + 8611904)) + v14)
                            if (u(v9) <= u((load32((((v3 << 2) | 4) + 8611904)) + v14))):
                                break
                            v4 = (load32((v3 + 8611904)) + v15)
                            if (u(v9) <= u((load32((v3 + 8611904)) + v15))):
                                break
                            if ((v4 | v7) < 0):
                                break
                            while True:  # block $label3
                                while True:  # block $label4
                                    v12 = load32(9671128)
                                    v3 = (v9 + 2)
                                    v6 = (load32(9671128) + (load32((load32(9142840) + ((v4 + (((v7 + (v9 + 2)) + 1) * v3)) << 2)) + 4) * 132))
                                    v3 = load8u((load32(9671128) + (load32((load32(9142840) + ((v4 + (((v7 + (v9 + 2)) + 1) * v3)) << 2)) + 4) * 132)) + 122)
                                    # br_table[(load8u((load32(9671128) + (load32((load32(9142840) + ((v4 + (((v7 + (v9 + 2)) + 1) * v3)) << 2)) + 4) * 132)) + 122) + -64)]
                                    break
                                    break
                                if (v3 != 10):
                                    break
                                break
                            if (load8u(v6 + 129) != 10):
                                break
                            if (load16u(v6 + 110) != v16):
                                break
                            v4 = load8u(v6 + 125)
                            while True:  # block $label6
                                while True:  # block $label5
                                    v3 = load32(v6 + 44)
                                    if (((load32((load32(9215884) + (load32(v6 + 44) << 4)) + 4) == 22) | (v3 == 0)) == 0):
                                        break
                                    if v4:
                                        break
                                    if (load32(v6 + 36) == 0):
                                        break
                                    break
                                    break
                                if (v4 != 1):
                                    break
                                v4 = load32(v6 + 32)
                                v7 = (v12 + (load32(v6 + 32) * 132))
                                v3 = load8u((v12 + (load32(v6 + 32) * 132)) + 122)
                                if (load8u((v12 + (load32(v6 + 32) * 132)) + 122) == load32(38528)):
                                    break
                                if (load8u(v7 + 125) == 3):
                                    break
                                if (v4 == 0):
                                    break
                                if (load32(38984) != v3):
                                    break
                                v12 = load16u(v6 + 114)
                                v3 = (load16u(v7 + 114) - load16u(v6 + 114))
                                v4 = load16u(v6 + 112)
                                v3 = (load16u(v7 + 112) - load16u(v6 + 112))
                                v3 = (v14 - v12)
                                v3 = (v15 - v4)
                                if (u((((load16u(v7 + 114) - load16u(v6 + 114)) * v3) + ((load16u(v7 + 112) - load16u(v6 + 112)) * v3))) <= u((((v14 - v12) * v3) + ((v15 - v4) * v3)))):
                                    break
                                break
                            if v13:
                                break
                            v9 = load32(9142440)
                            v13 = 1
                            break
                        v3 = (v5 + 2)
                        if (u(v5) < u(16558)):
                            continue
                        break
                    break
                break
            v4 = 1
            v2 = (u(v11) > u(1))
            if (u(v11) > u(1)):
                v5 = (v11 if v2 else 1)
                v3 = (arg0 * 132)
                while True:  # $label10
                    while True:  # block $label9
                        if (func225((arg1 + 12), (arg1 + 8), (load32(9671128) + v3), ((load32(38984) * 404) + 9568096)) == 0):
                            break
                        v2 = func34(load32(38984), load16u((load32(9671128) + v3) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1)
                        if (func34(load32(38984), load16u((load32(9671128) + v3) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1) == 0):
                            break
                        v2 = (load32(9671128) + (v2 * 132))
                        store64((load32(9671128) + (v2 * 132)) + 64, 1073741824250)
                        store32(v2 + 56, v10)
                        store32(v2 + 52, v8)
                        break
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v5):
                        continue
                    break
            v5 = load32(9671128)
            v4 = load32((load32(9671128) + (arg0 * 132)) + 80)
        v3 = (v8 * v11)
        if (u(v4) <= u((v8 * v11))):
            break
        v2 = (arg0 * 132)
        if (func225((arg1 + 12), (arg1 + 8), (v5 + (arg0 * 132)), ((load32(38984) * 404) + 9568096)) == 0):
            break
        v5 = func34(load32(38984), load16u((load32(9671128) + v2) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1)
        if (func34(load32(38984), load16u((load32(9671128) + v2) + 110), load32(arg1 + 12), load32(arg1 + 8), 0, 1) == 0):
            break
        v2 = load32(9671128)
        arg0 = load32((load32(9671128) + (arg0 * 132)) + 80)
        v2 = (v2 + (v5 * 132))
        store64((v2 + (v5 * 132)) + 64, 1073741824250)
        store32(v2 + 56, v10)
        store32(v2 + 52, (arg0 - v3))
        break
    G.global0 = (arg1 + 16)

# ------------------------------------------------------------
# $func844
# ------------------------------------------------------------
def func844(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v5 = load32(9671128)
        v6 = load32(arg1)
        arg1 = (load32(9671128) + (load32(arg1) * 132))
        v3 = load8u((load32(9671128) + (load32(arg1) * 132)) + 125)
        if (load8u((load32(9671128) + (load32(arg1) * 132)) + 125) == 3):
            break
        v4 = load32(9561692)
        v8 = load16u(arg1 + 110)
        if load32((load32(9561692) + (load16u(arg1 + 110) * 286704)) + 283912):
            break
        v7 = load32(arg0)
        arg0 = load32(arg0 + 4)
        store32(arg2 + 12, 0)
        store64(arg2 + 4, 0)
        store32(arg2, arg0)
        if v3:
            break
        if func66((v4 + (v8 * 286704)), arg2, 1, 1):
            break
        v3 = load32(((v7 * 404) + 9568096) + 268)
        v4 = (load32(9561692) + (load16u(arg1 + 110) * 286704))
        store32((load32(9561692) + (load16u(arg1 + 110) * 286704)) + 283912, (load32(v4 + 283912) + 1))
        # TODO: i32.div_u []
        func63(arg1, 34, ((arg0 << 16) + v7), (load32(load32(9142424) + 132) * ((500 if (v3 == 1) else 250) * arg0)), 100)
        if (load32((v5 + (v6 * 132)) + 92) == 0):
            break
        arg0 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v5 + (v6 * 132)) + 28)):
                break
        break
    G.global0 = (arg2 + 16)

# ------------------------------------------------------------
# $func845
# ------------------------------------------------------------
def func845(arg0, arg1):
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = (load32(9671128) + (arg0 * 132))
    v2 = (load32(9561692) + (load16u((load32(9671128) + (arg0 * 132)) + 110) * 286704))
    store32((load32(9561692) + (load16u((load32(9671128) + (arg0 * 132)) + 110) * 286704)) + 283912, (load32(v2 + 283912) - 1))
    while True:  # block $label0
        v2 = (arg1 & 65535)
        if (func59((v5 + 12), (v5 + 8), v3, (((arg1 & 65535) * 404) + 9568096)) == 0):
            break
        v4 = func34(v2, load16u(v3 + 110), load32(v5 + 12), load32(v5 + 8), 0, 1)
        if (func34(v2, load16u(v3 + 110), load32(v5 + 12), load32(v5 + 8), 0, 1) == 0):
            break
        v6 = ((arg1 & 0xFFFFFFFF) >> 16)
        v8 = load32(9671128)
        v2 = (load32(9671128) + (v4 * 132))
        store16((load32(9671128) + (v4 * 132)) + 110, 0)
        store32(v2 + 56, load16u(v3 + 110))
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label2
                    while True:  # block $label1
                        v3 = load8u(v2 + 122)
                        v7 = ((load8u(v2 + 122) * 404) + 9568096)
                        # br_table[load32(((load8u(v2 + 122) * 404) + 9568096) + 268)]
                        break
                        break
                    if load32(v2 + 52):
                        store32(v2 + 52, ((arg1 & 0xFFFFFFFF) >> 17))
                    v2 = (v8 + (v4 * 132))
                    if load32((v8 + (v4 * 132)) + 60):
                        store32(v2 + 60, ((arg1 & 0xFFFFFFFF) >> 17))
                    if load32(v2 + 72):
                        store32(v2 + 72, v6)
                    v7 = (v8 + (v4 * 132))
                    if load32((v8 + (v4 * 132)) + 76):
                        store32(v7 + 76, v6)
                    v4 = 480
                    if (load32(v7 + 84) == 0):
                        break
                    v2 = 1
                    while True:  # block $label5
                        if (u(arg1) < u(327680)):
                            break
                        # TODO: i32.div_u []
                        v6 = 327680
                        v10 = (327680 & 1)
                        v3 = 1
                        if (u((arg1 - 327680)) >= u(327680)):
                            v6 = (v6 & 16382)
                            arg1 = 0
                            v3 = 0
                            while True:  # $label6
                                arg1 = ((arg1 + 1) % v2)
                                v9 = ((arg1 + 2) if ((arg1 + 1) % v2) else 1)
                                v2 = (v2 + (arg1 == 0))
                                v9 = (v9 % (v2 + (arg1 == 0)))
                                arg1 = (((arg1 + 2) if ((arg1 + 1) % v2) else 1) if (v9 % (v2 + (arg1 == 0))) else 0)
                                v2 = (v2 + (v9 == 0))
                                v3 = (v3 + 2)
                                if ((v3 + 2) != v6):
                                    continue
                                break
                            v3 = (arg1 + 1)
                        if (v10 == 0):
                            break
                        v2 = (v2 + ((v3 % v2) == 0))
                        break
                    store32(v7 + 84, v2)
                    break
                    break
                # TODO: i32.div_u []
                store32(v6 + 52, load32(v7 + 68))
                v4 = 624
                break
                break
            if load32(v2 + 52):
                store32(v2 + 52, ((arg1 & 0xFFFFFFFF) >> 18))
            v2 = (v8 + (v4 * 132))
            if load32((v8 + (v4 * 132)) + 60):
                store32(v2 + 60, ((arg1 & 0xFFFFFFFF) >> 18))
            v4 = 528
            if (load32(38952) == v3):
                break
            v4 = 576
            if (load32(38956) == v3):
                break
            v4 = (672 if (load32(38960) == v3) else 0)
            break
        if (load32(9142872) != load16u((v8 + (arg0 * 132)) + 110)):
            break
        store32(v5, v4)
        a_b()
        break
    arg1 = (arg0 * 132)
    func29(((arg0 * 132) + load32(9671128)), 0)
    while True:  # block $label7
        arg1 = load32(9671128)
        if (load32((arg1 + load32(9671128)) + 92) == 0):
            break
        v2 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((arg1 + (arg0 * 132)) + 28)):
                break
        break
    G.global0 = (v5 + 16)

# ------------------------------------------------------------
# $func846
# ------------------------------------------------------------
def func846(arg0, arg1, arg2):
    arg2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label0
        v4 = load32(9671128)
        v6 = load32(arg1)
        v7 = (load32(9671128) + (load32(arg1) * 132))
        if (load8u((load32(9671128) + (load32(arg1) * 132)) + 125) == 3):
            break
        arg1 = load32(v7 + 20)
        if (load32(v7 + 20) == 0):
            break
        v3 = load32(arg0)
        arg1 = (load32(arg0) + 8)
        arg0 = load32((load32(arg1) + ((load32(arg0) + 8) << 2)))
        if (load32((load32(arg1) + ((load32(arg0) + 8) << 2))) == 0):
            break
        v9 = (arg0 - 1)
        arg0 = (((arg0 - 1) * 404) + 9568096)
        store32(arg2, (((load32((((arg0 - 1) * 404) + 9568096) + 68) * 36) // 10) + 620))
        store32(arg2 + 4, ((load32(arg0 + 72) * 36) // 10))
        store32(arg2 + 8, ((load32(arg0 + 76) * 36) // 10))
        store32(arg2 + 12, ((load32(arg0 + 80) * 36) // 10))
        while True:  # block $label2
            while True:  # block $label1
                v8 = load32(9561692)
                v10 = (v4 + (v6 * 132))
                v4 = load16u((v4 + (v6 * 132)) + 110)
                arg0 = (load32(9561692) + (load16u((v4 + (v6 * 132)) + 110) * 286704))
                v5 = (load32((load32(9561692) + (load16u((v4 + (v6 * 132)) + 110) * 286704)) + 283976) + 1)
                if (u((load32((load32(9561692) + (load16u((v4 + (v6 * 132)) + 110) * 286704)) + 283976) + 1)) > u((load32((arg0 + 284136)) + load32(arg0 + 283980)))):
                    arg1 = 57101
                    if (load32(arg0 + 283908) == load32(9142872)):
                        break
                    break
                if (u(v5) <= u(load32((arg0 + 284000)))):
                    break
                arg1 = 57113
                if (load32((v8 + (v4 * 286704)) + 283908) != load32(9142872)):
                    break
                break
            a_b()
            break
            break
        if func66((v8 + (v4 * 286704)), arg2, 1, 1):
            break
        arg0 = load32(load32(v7 + 20))
        while True:  # block $label3
            if (u(arg1) > u(14)):
                break
            v11 = ((3 - v3) & 3)
            if ((3 - v3) & 3):
                v5 = 0
                while True:  # $label4
                    arg1 = (arg1 + 1)
                    store32((arg0 + (arg1 << 2)), load32((arg0 + ((arg1 + 1) << 2))))
                    v5 = (v5 + 1)
                    if ((v5 + 1) != v11):
                        continue
                    break
            if (u((v3 - 4)) <= u(2)):
                break
            while True:  # $label5
                v3 = (arg0 + (arg1 << 2))
                v12 = load64((arg0 + (arg1 << 2)) + 4)
                store32(v3 + 8, load32(v3 + 12))
                store64(v3, v12)
                arg1 = (arg1 + 4)
                store32(v3 + 12, load32((arg0 + ((arg1 + 4) << 2))))
                if (arg1 != 15):
                    continue
                break
            break
        store32(arg0 + 60, 0)
        arg1 = 0
        if func59((arg2 + 28), (arg2 + 24), v7, ((v9 * 404) + 9568096)):
            arg1 = func34(v9, load16u(v10 + 110), load32(arg2 + 28), load32(arg2 + 24), 0, 1)
        arg0 = (load32(9671128) + (arg1 * 132))
        if load32((load32(9671128) + (arg1 * 132)) + 28):
            arg1 = load32(((load32(9561692) + (load16u(v10 + 110) * 286704)) + 284248))
            store32(arg0 + 84, load32(((load32(9561692) + (load16u(v10 + 110) * 286704)) + 284248)))
            func201(arg0)
            v3 = (v8 + (v4 * 286704))
            store32((v8 + (v4 * 286704)) + 283936, (load32(v3 + 283936) + 1))
            v3 = (v3 + 281636)
            store32((v3 + 281636), (load32(v3) + 1))
            store32(arg0 + 52, (arg1 + load32(arg0 + 52)))
            store32(arg0 + 60, (load32(arg0 + 60) + ((arg1 & 0xFFFFFFFF) >> 1)))
            func69((load32(9671128) + (v6 * 132)), load32(arg0 + 28))
        if (load32(9671124) != 96):
            break
        if (load32(9173808) != v6):
            break
        break
    G.global0 = (arg2 + 32)

# ------------------------------------------------------------
# $func847
# ------------------------------------------------------------
def func847(arg0, arg1):
    while True:  # block $label0
        if (arg0 == 0):
            break
        v3 = ((arg1 << 2) + 9215712)
        arg0 = load32(((arg1 << 2) + 9215712))
        if load8u(9163793):
            if (arg0 == 0):
                arg0 = func26(16)
                store32(func26(16) + 4, 10000)
                store32(arg0, func26(40000))
                store64(arg0 + 8, 4294967296)
                store32(v3, arg0)
            arg1 = load32(9213808)
            store32(arg0 + 8, load32(9213808))
            if (arg1 == 0):
                break
            arg1 = load32(arg0)
            arg0 = 0
            while True:  # $label1
                v2 = (arg0 << 2)
                store32((arg1 + (arg0 << 2)), load32((v2 + 9173808)))
                arg0 = (arg0 + 1)
                if (u((arg0 + 1)) < u(load32(9213808))):
                    continue
                break
            break
        if (arg0 == 0):
            break
        store32(9143000, 0)
        arg0 = load32(9213820)
        if load32(9213820):
            func47((load32(9671128) + (arg0 * 132)))
            store32(9213820, 0)
        func45()
        arg1 = load32(v3)
        if load32(load32(v3) + 8):
            v4 = load32(9671128)
            arg0 = 0
            while True:  # $label3
                while True:  # block $label2
                    v2 = (v4 + (load32((load32(arg1) + (arg0 << 2))) * 132))
                    if (load8u((v4 + (load32((load32(arg1) + (arg0 << 2))) * 132)) + 125) == 3):
                        break
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v2 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v2 + 127) == 6):
                            break
                    if load8u(9163792):
                        if load32(((load8u(v2 + 122) * 404) + 9568096) + 264):
                            break
                    func44(v2, 0)
                    arg1 = load32(v3)
                    v4 = load32(9671128)
                    break
                arg0 = (arg0 + 1)
                if (u((arg0 + 1)) < u(load32(arg1 + 8))):
                    continue
                break
        break

# ------------------------------------------------------------
# $func848
# ------------------------------------------------------------
def func848(arg0, arg1):
    func146(arg0, load32(38724))

# ------------------------------------------------------------
# $func849
# ------------------------------------------------------------
def func849(arg0, arg1):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if load8u(9147152):
            break
        v17 = load32(9561692)
        v2 = load32(9671128)
        v4 = (arg0 * 132)
        arg0 = (load32(9671128) + (arg0 * 132))
        v10 = load16u((load32(9671128) + (arg0 * 132)) + 110)
        v11 = (load32(9561692) + (load16u((load32(9671128) + (arg0 * 132)) + 110) * 286704))
        v18 = load8u(arg0 + 122)
        v19 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 68)
        arg0 = ((load32(((load8u(arg0 + 122) * 404) + 9568096) + 68) & 0xFFFFFFFF) >> 1)
        while True:  # block $label1
            if (load32(9671152) != v18):
                break
            arg0 = ((load32(v11 + 283848) // 2) + arg0)
            v7 = load32(9671136)
            # TODO: i32.div_u []
            v8 = 200
            v3 = load32(9671132)
            if (u((func88(v11) + 200)) < u(load32(9671132))):
                break
            v8 = (load32(9671140) + (v3 + v8))
            store32(9671132, (load32(9671140) + (v3 + v8)))
            v2 = func228(v2, v8, v7)
            store32(9671128, func228(v2, v8, v7))
            break
        v2 = (v2 + v4)
        v20 = load16u((v2 + v4) + 112)
        v8 = load16u(v2 + 114)
        # TODO: i32.div_u []
        v9 = 100
        v2 = (100 * -100)
        v4 = load32(9671132)
        v7 = load32(9671136)
        if (u(load32(9671132)) <= u((load32(9671136) + v9))):
            v4 = (load32(9671140) + (v4 + v9))
            store32(9671132, (load32(9671140) + (v4 + v9)))
            store32(9671128, func228(load32(9671128), v4, v7))
        v13 = (100 if (u(arg0) >= u(100)) else 0)
        arg0 = (arg0 + v2)
        v7 = v8
        while True:  # $label9
            v6 = (v8 - v12)
            v2 = ((v12 << 1) | 1)
            v14 = (((v8 - v12) + ((v12 << 1) | 1)) - 1)
            v4 = (v20 - v12)
            v21 = (v2 + (v20 - v12))
            v15 = ((v2 + (v20 - v12)) - 1)
            v2 = v4
            while True:  # block $label3
                while True:  # $label5
                    while True:  # block $label2
                        v3 = load32(9142440)
                        if (u(v6) >= u(load32(9142440))):
                            break
                        if ((v2 | v6) < 0):
                            break
                        if (u(v2) >= u(v3)):
                            break
                        v3 = func34(load32(39064), 0, v2, v6, 0, 1)
                        if func34(load32(39064), 0, v2, v6, 0, 1):
                            v16 = (load32(9671128) + (v3 * 132))
                            store64((load32(9671128) + (v3 * 132)) + 64, 2147483648500)
                            store32(v16 + 52, (arg0 + v13))
                            arg0 = 0
                        v5 = (v5 + (v3 != 0))
                        if (u((v5 + (v3 != 0))) >= u(v9)):
                            break
                        v3 = load32(9142440)
                        break
                    while True:  # block $label4
                        if (u(v3) <= u(v14)):
                            break
                        if ((v2 | v14) < 0):
                            break
                        if (u(v2) >= u(v3)):
                            break
                        v3 = func34(load32(39064), 0, v2, v14, 0, 1)
                        if func34(load32(39064), 0, v2, v14, 0, 1):
                            v16 = (load32(9671128) + (v3 * 132))
                            store64((load32(9671128) + (v3 * 132)) + 64, 2147483648500)
                            store32(v16 + 52, (arg0 + v13))
                            arg0 = 0
                        v5 = (v5 + (v3 != 0))
                        if (u((v5 + (v3 != 0))) >= u(v9)):
                            break
                        break
                    v2 = (v2 + 1)
                    if ((v2 + 1) < v21):
                        continue
                    break
                v2 = (v6 + 1)
                if (v14 > (v6 + 1)):
                    while True:  # $label8
                        while True:  # block $label6
                            v3 = load32(9142440)
                            if (u(v2) >= u(load32(9142440))):
                                break
                            if ((v2 | v4) < 0):
                                break
                            if (u(v3) <= u(v4)):
                                break
                            v3 = func34(load32(39064), 0, v4, v2, 0, 1)
                            if func34(load32(39064), 0, v4, v2, 0, 1):
                                v6 = (load32(9671128) + (v3 * 132))
                                store64((load32(9671128) + (v3 * 132)) + 64, 2147483648500)
                                store32(v6 + 52, (arg0 + v13))
                                arg0 = 0
                            v5 = (v5 + (v3 != 0))
                            if (u((v5 + (v3 != 0))) >= u(v9)):
                                break
                            v3 = load32(9142440)
                            break
                        while True:  # block $label7
                            if (u(v2) >= u(v3)):
                                break
                            if ((v2 | v15) < 0):
                                break
                            if (u(v3) <= u(v15)):
                                break
                            v3 = func34(load32(39064), 0, v15, v2, 0, 1)
                            if func34(load32(39064), 0, v15, v2, 0, 1):
                                v6 = (load32(9671128) + (v3 * 132))
                                store64((load32(9671128) + (v3 * 132)) + 64, 2147483648500)
                                store32(v6 + 52, (arg0 + v13))
                                arg0 = 0
                            v5 = (v5 + (v3 != 0))
                            if (u((v5 + (v3 != 0))) >= u(v9)):
                                break
                            break
                        v2 = (v2 + 1)
                        if ((v2 + 1) != v7):
                            continue
                        break
                v7 = (v7 + 1)
                v12 = (v12 + 1)
                if ((v12 + 1) != 512):
                    continue
                break
            break
        store32(v11 + 283956, (load32(v11 + 283956) + v19))
        if (v10 == 0):
            break
        if (load32(9671152) != v18):
            break
        if (u(load32(9671136)) >= u(4)):
            arg0 = 3
            while True:  # $label11
                while True:  # block $label10
                    v2 = (load32(9671128) + (arg0 * 132))
                    if (load16u((load32(9671128) + (arg0 * 132)) + 110) != v10):
                        break
                    if load8u(((load8u(v2 + 122) * 404) + 9568096) + 332):
                        func78(v2, 0, 0, 1)
                        break
                    break
                arg0 = (arg0 + 1)
                if (u((arg0 + 1)) < u(load32(9671136))):
                    continue
                break
        arg0 = (v17 + (v10 * 286704))
        store32((v17 + (v10 * 286704)) + 283976, 0)
        store32(arg0 + 283848, 0)
        v2 = load32(arg0 + 281788)
        if load32(arg0 + 281788):
            store32(v2 + 8, 0)
        arg0 = load32(arg0 + 281792)
        if load32(arg0 + 281792):
            store32(arg0 + 8, 0)
        arg0 = (v17 + (v10 * 286704))
        v2 = load32((v17 + (v10 * 286704)) + 281796)
        if load32((v17 + (v10 * 286704)) + 281796):
            store32(v2 + 8, 0)
        v2 = load32(arg0 + 284628)
        arg0 = load32(arg0 + 284616)
        store32(arg1 + 4, v11)
        store32(arg1, 118)
        store32(arg1 + 8, (arg0 if arg0 else v2))
        a_b()
        if (load32(9142872) != v10):
            break
        a_b()
        break
    G.global0 = (arg1 + 16)

# ------------------------------------------------------------
# $func850
# ------------------------------------------------------------
def func850(arg0, arg1):
    func146(arg0, load32(38728))

# ------------------------------------------------------------
# $func851
# ------------------------------------------------------------
def func851(arg0, arg1):
    v5 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v10 = ((arg0 & 0xFFFFFFFF) >> 16)
    v15 = (((arg0 & 0xFFFFFFFF) >> 16) + 3)
    v11 = (arg0 & 65535)
    v16 = ((arg0 & 65535) + 3)
    v17 = (v10 - 2)
    v7 = (v11 - 2)
    v8 = (load32(9671128) + (arg1 * 132))
    v18 = load32(((load32(9561692) + (load16u((load32(9671128) + (arg1 * 132)) + 110) * 286704)) + 284356))
    while True:  # $label6
        v14 = (v7 + 1)
        arg0 = (v7 - v11)
        v19 = (((v7 - v11) * arg0) - 1)
        arg0 = v17
        while True:  # $label5
            while True:  # block $label0
                arg1 = arg0
                arg0 = (arg0 - v10)
                if ((v19 + ((arg0 - v10) * arg0)) > 4):
                    break
                arg0 = load32(9142440)
                if (u(load32(9142440)) <= u(arg1)):
                    break
                if ((arg1 | v7) < 0):
                    break
                if (u(arg0) <= u(v7)):
                    break
                v20 = ((v18 & 0xFFFFFFFF) >> ((v7 != v11) | (arg1 != v10)))
                v21 = (arg1 + 1)
                arg0 = 0
                while True:  # $label4
                    while True:  # block $label1
                        v4 = (load32(9142440) + 2)
                        v4 = load32((load32(9142840) + ((v14 + ((v21 + ((load32(9142440) + 2) * arg0)) * v4)) << 2)))
                        if (u(load32((load32(9142840) + ((v14 + ((v21 + ((load32(9142440) + 2) * arg0)) * v4)) << 2)))) < u(3)):
                            break
                        v4 = (load32(9671128) + (v4 * 132))
                        v6 = load8u((load32(9671128) + (v4 * 132)) + 122)
                        v2 = load32(((load8u((load32(9671128) + (v4 * 132)) + 122) * 404) + 9568096) + 284)
                        if (load32(((load8u((load32(9671128) + (v4 * 132)) + 122) * 404) + 9568096) + 284) == 0):
                            break
                        v9 = load8u(v4 + 125)
                        if (load8u(v4 + 125) == 10):
                            break
                        v2 = (v2 * v20)
                        # TODO: i32.div_u []
                        v2 = ((v2 * v20) if (u(v2) < u(100)) else 100)
                        v3 = load32(v4 + 64)
                        v2 = (((v2 * v20) if (u(v2) < u(100)) else 100) if (u(v2) < u(v3)) else load32(v4 + 64))
                        v3 = load16u(v4 + 110)
                        v12 = load32(9561692)
                        v22 = load16u(v8 + 110)
                        v13 = load32((load32(9561692) + (load16u(v8 + 110) * 286704)) + 278556)
                        if load32((load32(9561692) + (load16u(v8 + 110) * 286704)) + 278556):
                            v13 = (v13 + ((load8u(v8 + 122) + (v3 * 255)) << 2))
                            store32((v13 + ((load8u(v8 + 122) + (v3 * 255)) << 2)), (load32(v13) + v2))
                        v3 = load32(((v12 + (v3 * 286704)) + 278564))
                        if load32(((v12 + (v3 * 286704)) + 278564)):
                            v3 = (v3 + (((v22 * 255) + v6) << 2))
                            store32((v3 + (((v22 * 255) + v6) << 2)), (load32(v3) + v2))
                        if (v9 == 3):
                            break
                        v3 = (v4 - -64)
                        v6 = load32((v4 - -64))
                        if (u(v2) < u(load32((v4 - -64)))):
                            store32(v3, (v6 - v2))
                            if (load32(v4 + 92) == 0):
                                break
                            if load8u(9147141):
                                break
                            store32(v5, v2)
                            a_b()
                            break
                        store32(v3, 0)
                        v6 = load32(9561692)
                        v3 = load16u(v8 + 110)
                        v2 = (load32(9561692) + (load16u(v8 + 110) * 286704))
                        while True:  # block $label2
                            if (load32(9147132) == 0):
                                break
                            if (load32(9671152) != load8u(v4 + 122)):
                                break
                            v9 = load16u(v4 + 110)
                            if (v3 == load16u(v4 + 110)):
                                break
                            if (v3 == 0):
                                break
                            v3 = (v6 + (v9 * 286704))
                            v9 = load32((v6 + (v9 * 286704)) + 284628)
                            v6 = load32(v3 + 284616)
                            v12 = load32(v2 + 284616)
                            store32(v5 + 32, (load32(v2 + 284616) if v12 else load32(v2 + 284628)))
                            store32(v5 + 28, v2)
                            store32(v5 + 20, v3)
                            store32(v5 + 16, 927)
                            store32(v5 + 24, (v6 if v6 else v9))
                            a_b()
                            break
                        while True:  # block $label3
                            v3 = load32((v2 + 278560))
                            if (load32((v2 + 278560)) == 0):
                                v2 = load16u(v4 + 110)
                                break
                            v2 = load16u(v4 + 110)
                            v3 = (v3 + ((load8u(v8 + 122) + (load16u(v4 + 110) * 255)) << 2))
                            store32((v3 + ((load8u(v8 + 122) + (load16u(v4 + 110) * 255)) << 2)), (load32(v3) + 1))
                            break
                        v2 = load32(((load32(9561692) + (v2 * 286704)) + 278568))
                        if load32(((load32(9561692) + (v2 * 286704)) + 278568)):
                            v2 = (v2 + ((load8u(v4 + 122) + (load16u(v8 + 110) * 255)) << 2))
                            store32((v2 + ((load8u(v4 + 122) + (load16u(v8 + 110) * 255)) << 2)), (load32(v2) + 1))
                        store16(v4 + 116, load32(v8 + 28))
                        break
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != 3):
                        continue
                    break
                break
            arg0 = (arg1 + 1)
            if (arg1 != v15):
                continue
            break
        arg0 = (v7 == v16)
        v7 = v14
        if (arg0 == 0):
            continue
        break
    G.global0 = (v5 + 48)

# ------------------------------------------------------------
# $func852
# ------------------------------------------------------------
def func852(arg0, arg1):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = ((arg0 & -32) - load32(9142952))
    v2 = ((arg1 & -32) - load32(9142956))
    v2 = (((((arg0 & -32) - load32(9142952)) * v2) + (((arg1 & -32) - load32(9142956)) * v2)) - 1)
    while True:  # block $label0
        while True:  # block $label1
            v4 = ((arg0 & 0xFFFFFFFF) >> 5)
            v5 = ((arg1 & 0xFFFFFFFF) >> 5)
            v3 = load32(9142440)
            v6 = (load32(9142440) + 2)
            if (load32((load32(9142840) + ((((arg0 & 0xFFFFFFFF) >> 5) + (((((arg1 & 0xFFFFFFFF) >> 5) + (load32(9142440) + 2)) + 1) * v6)) << 2)) + 4) == 1):
                if (v2 > 9000000):
                    v2 = 9142540
                    break
                v6 = load32(39836)
                v2 = 9142540
                v8 = load32(load32(9142424) + 48)
                if (load32(load32(9142424) + 48) == 0):
                    break
                if load8u(9147152):
                    break
                v3 = load16u((load32(9147376) + (((v3 * v5) + v4) << 1)))
                if (v8 == 2):
                    if (u(v3) > u(1)):
                        break
                    break
                if v3:
                    break
                break
            if (v2 > 9000000):
                v2 = 9142544
                break
            v6 = load32(39832)
            v2 = 9142544
            v8 = load32(load32(9142424) + 48)
            if (load32(load32(9142424) + 48) == 0):
                break
            if load8u(9147152):
                break
            v3 = load16u((load32(9147376) + (((v3 * v5) + v4) << 1)))
            if (v8 == 2):
                if (u(v3) > u(1)):
                    break
                break
            if (v3 == 0):
                break
            break
        store32(v7 + 8, v5)
        store32(v7 + 4, v4)
        store32(v7, v6)
        a_b()
        break
    v3 = load32(v2)
    while True:  # block $label3
        while True:  # block $label2
            v6 = load32(load32(9142424) + 48)
            if (load32(load32(9142424) + 48) == 0):
                break
            if load8u(9147152):
                break
            v2 = load16u((load32(9147376) + (((load32(9142440) * v5) + v4) << 1)))
            if (v6 == 2):
                if (u(v2) > u(1)):
                    break
                break
            if (v2 == 0):
                break
            break
        v2 = (v4 * v5)
        # TODO: f32.convert_i32_u []
        # TODO: f32.convert_i32_u []
        # TODO: f64.convert_i32_u []
        # TODO: f32.demote_f64 []
        func80(((arg0 + (((v4 * v5) * v4) & 31)) - 16), ((arg1 + ((v2 * v5) & 31)) - 16), v3, 1.0, (arg1 * 0.7))
        break
    G.global0 = (v7 + 16)

# ------------------------------------------------------------
# $func853
# ------------------------------------------------------------
def func853(arg0, arg1):
    while True:  # block $label0
        if (arg1 == 0):
            break
        v3 = load32(9671128)
        v6 = (load32(9671128) + (arg0 * 132))
        v7 = load8u((load32(9671128) + (arg0 * 132)) + 125)
        arg1 = load8u((load32(9671128) + (arg0 * 132)) + 125)
        if (load8u((load32(9671128) + (arg0 * 132)) + 125) == 3):
            break
        while True:  # block $label1
            if (arg1 == 12):
                break
            arg1 = (v3 + (arg0 * 132))
            v2 = load32((v3 + (arg0 * 132)) + 72)
            v5 = load32(arg1 + 76)
            if (u(load32((v3 + (arg0 * 132)) + 72)) < u(load32(arg1 + 76))):
                v2 = (load32(((load32(9561692) + (load16u(arg1 + 110) * 286704)) + 284072)) + v2)
                v2 = ((load32(((load32(9561692) + (load16u(arg1 + 110) * 286704)) + 284072)) + v2) if (u(v2) < u(v5)) else v5)
                store32(arg1 + 72, ((load32(((load32(9561692) + (load16u(arg1 + 110) * 286704)) + 284072)) + v2) if (u(v2) < u(v5)) else v5))
            while True:  # block $label2
                v4 = load32(arg1 + 96)
                if load32(arg1 + 96):
                    v4 = (load32(9671128) + (v4 * 132))
                    if ((load8u((load32(9671128) + (v4 * 132)) + 125) & 251) != 3):
                        if (load32(v4 + 32) == arg0):
                            break
                    store32(arg1 + 96, 0)
                break
            v4 = 0
            if (v2 != v5):
                break
            if v4:
                break
            if load32((v3 + (arg0 * 132)) + 36):
                break
            if (v7 == 1):
                break
            func403(v6)
            break
        arg0 = (v3 + (arg0 * 132))
        v3 = load32((v3 + (arg0 * 132)) + 80)
        v2 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
        arg1 = load32(((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 284320))
        if (u(load32((v3 + (arg0 * 132)) + 80)) >= u(load32(((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 284320)))):
            break
        arg0 = (load32((v2 + 284076)) + v3)
        store32(arg0 + 80, ((load32((v2 + 284076)) + v3) if (u(arg0) < u(arg1)) else arg1))
        break

# ------------------------------------------------------------
# $func854
# ------------------------------------------------------------
def func854(arg0, arg1):
    while True:  # block $label0
        v2 = ((arg1 * 404) + 9568096)
        v4 = load32(((arg1 * 404) + 9568096) + 236)
        if (load32(((arg1 * 404) + 9568096) + 236) == 0):
            break
        arg1 = 0
        v7 = load32(9561692)
        v5 = load32(v2 + 92)
        v2 = load32(v2 + 232)
        if (u(v4) >= u(4)):
            v9 = (v4 & -4)
            v3 = ((v7 + (arg0 * 286704)) + 269376)
            while True:  # $label1
                v6 = (arg1 << 2)
                store32((v3 + (load32((v2 + (arg1 << 2))) * 36)), v5)
                store32((v3 + (load32((v2 + (v6 | 4))) * 36)), v5)
                store32((v3 + (load32((v2 + (v6 | 8))) * 36)), v5)
                store32((v3 + (load32((v2 + (v6 | 12))) * 36)), v5)
                arg1 = (arg1 + 4)
                v8 = (v8 + 4)
                if ((v8 + 4) != v9):
                    continue
                break
        v4 = (v4 & 3)
        if ((v4 & 3) == 0):
            break
        v3 = 0
        arg0 = (v7 + (arg0 * 286704))
        while True:  # $label2
            store32(((arg0 + (load32((v2 + (arg1 << 2))) * 36)) + 269376), v5)
            arg1 = (arg1 + 1)
            v3 = (v3 + 1)
            if ((v3 + 1) != v4):
                continue
            break
        break

# ------------------------------------------------------------
# $func855
# ------------------------------------------------------------
def func855(arg0, arg1, arg2):
    if arg2:
        v4 = load32(arg0)
        v3 = load32(9671128)
        arg0 = 0
        while True:  # $label0
            v5 = (v3 + (load32((arg1 + (arg0 << 2))) * 132))
            if (load8u((v3 + (load32((arg1 + (arg0 << 2))) * 132)) + 125) != 3):
                v3 = load32(9671128)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break

# ------------------------------------------------------------
# $func856
# ------------------------------------------------------------
def func856(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v1 + 12, arg0)
    arg0 = load32(9213808)
    while True:  # block $label0
        if load8u(9147210):
            func41(11, 9173808, arg0, (v1 + 12), 1)
            break
        v3 = (arg0 << 2)
        v2 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy []
        # call_indirect[load32(9213912)]
        break
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $func857
# ------------------------------------------------------------
def func857(arg0, arg1):

# ------------------------------------------------------------
# $func858
# ------------------------------------------------------------
def func858(arg0, arg1):
    v4 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    arg1 = load32(9671128)
    while True:  # block $label0
        if (u(load32(9142848)) < u((load32(load32(9142424) + 72) * 2400))):
            func29((arg1 + (arg0 * 132)), 1)
            break
        while True:  # block $label1
            v2 = (arg0 * 132)
            v3 = (arg1 + (arg0 * 132))
            if (load8u((arg1 + (arg0 * 132)) + 125) == 3):
                break
            if (load8u(v3 + 128) == 0):
                break
            arg1 = (arg1 + (arg0 * 132))
            store8((arg1 + (arg0 * 132)) + 127, 0)
            while True:  # block $label2
                v5 = load32(arg1 + 40)
                if (load32(arg1 + 40) == 0):
                    break
                if load8u(9142916):
                    store32(v4 + 20, v5)
                    store32(v4 + 16, 0)
                    a_b()
                    break
                arg1 = load16u(arg1 + 110)
                store32(v4 + 4, v5)
                store32(v4, (arg1 + 16))
                a_b()
                break
            store8(v3 + 128, 0)
            arg1 = load32(9671128)
            break
        v2 = (arg1 + v2)
        v9 = load16u((arg1 + v2) + 110)
        v3 = load32(9561692)
        arg1 = load16u(v2 + 116)
        v5 = load16u(v2 + 118)
        v10 = (arg1 - 2)
        v2 = (load32(9561692) + (load16u(v2 + 110) * 286704))
        arg1 = load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284272))
        v14 = (v10 + load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284272)))
        if ((arg1 - 2) >= (v10 + load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284272)))):
            break
        v5 = (v5 - 2)
        v15 = (arg1 + v5)
        if ((v5 - 2) >= (arg1 + v5)):
            break
        v12 = load32((v2 + 284276))
        arg1 = (v3 + (v9 * 286704))
        v7 = ((v3 + (v9 * 286704)) + 281768)
        v13 = (arg1 + 283908)
        v8 = (arg1 + 281764)
        v6 = load32(9142440)
        while True:  # $label7
            v3 = (v10 + 1)
            arg1 = v5
            while True:  # $label6
                v2 = arg1
                arg1 = (arg1 + 1)
                while True:  # block $label3
                    if (u(v2) >= u(v6)):
                        break
                    if ((v2 | v10) < 0):
                        break
                    if (u(v6) <= u(v10)):
                        break
                    while True:  # block $label4
                        v11 = load32(9142840)
                        v9 = (v6 + 2)
                        v2 = load32((load32(9142840) + ((v3 + (arg1 * (v6 + 2))) << 2)))
                        if (u(load32((load32(9142840) + ((v3 + (arg1 * (v6 + 2))) << 2)))) <= u(2)):
                            break
                        if (arg0 == v2):
                            break
                        v2 = (load32(9671128) + (v2 * 132))
                        if (load32(((load8u((load32(9671128) + (v2 * 132)) + 122) * 404) + 9568096) + 344) == 0):
                            break
                        if (u(((load8u(v2 + 125) - 9) & 255)) < u(2)):
                            break
                        store32(v8, (load32(v8) + 1))
                        if load8u((load32(9143004) + (load32(v13) + (load32(9142892) * load16u(v2 + 110))))):
                            store32(v7, (load32(v7) + load32(v2 + 64)))
                        func204(v2, v12)
                        v6 = load32(9142440)
                        v9 = (load32(9142440) + 2)
                        v11 = load32(9142840)
                        break
                    while True:  # block $label5
                        v2 = load32((v11 + ((v3 + ((arg1 + v9) * v9)) << 2)))
                        if (u(load32((v11 + ((v3 + ((arg1 + v9) * v9)) << 2)))) < u(3)):
                            break
                        if (arg0 == v2):
                            break
                        v2 = (load32(9671128) + (v2 * 132))
                        if (load32(((load8u((load32(9671128) + (v2 * 132)) + 122) * 404) + 9568096) + 344) == 0):
                            break
                        if (u(((load8u(v2 + 125) - 9) & 255)) < u(2)):
                            break
                        store32(v8, (load32(v8) + 1))
                        if load8u((load32(9143004) + (load32(v13) + (load32(9142892) * load16u(v2 + 110))))):
                            store32(v7, (load32(v7) + load32(v2 + 64)))
                        func204(v2, v12)
                        v11 = load32(9142840)
                        v6 = load32(9142440)
                        break
                    v2 = (v6 + 2)
                    v2 = load32((v11 + ((v3 + ((arg1 + ((v6 + 2) << 1)) * v2)) << 2)))
                    if (u(load32((v11 + ((v3 + ((arg1 + ((v6 + 2) << 1)) * v2)) << 2)))) < u(3)):
                        break
                    if (arg0 == v2):
                        break
                    v2 = (load32(9671128) + (v2 * 132))
                    if (load32(((load8u((load32(9671128) + (v2 * 132)) + 122) * 404) + 9568096) + 344) == 0):
                        break
                    if (u(((load8u(v2 + 125) - 9) & 255)) < u(2)):
                        break
                    store32(v8, (load32(v8) + 1))
                    if load8u((load32(9143004) + (load32(v13) + (load32(9142892) * load16u(v2 + 110))))):
                        store32(v7, (load32(v7) + load32(v2 + 64)))
                    func204(v2, v12)
                    v6 = load32(9142440)
                    break
                if (arg1 != v15):
                    continue
                break
            v10 = v3
            if (v3 != v14):
                continue
            break
        break
    G.global0 = (v4 + 32)

# ------------------------------------------------------------
# $func880
# ------------------------------------------------------------
def func880(arg0, arg1, arg2):
    while True:  # block $label0
        v7 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v3 = load32(59164)
        v4 = load32(9561692)
        arg0 = 1
        while True:  # block $label1
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
        if (arg2 == 0):
            v3 = 1
            break
        v4 = load32(arg1)
        v8 = load32(9671136)
        v6 = ((u(load32(arg1)) < u(3)) | (u(v4) >= u(load32(9671136))))
        v3 = 0
        if (load8u(9147152) == 0):
            v5 = 0
            if v6:
                break
            v6 = load32(9215884)
            v9 = load32(9143008)
            v10 = load32(9671128)
            while True:  # $label3
                v4 = (v10 + (v4 * 132))
                if (load8u((v9 + ((v7 * load16u((v10 + (v4 * 132)) + 110)) + arg0))) == 0):
                    break
                if (load32((v6 + (load32(v4 + 44) << 4)) + 4) == 20):
                    break
                if (load8u(v4 + 127) == 6):
                    break
                v5 = (v5 + 1)
                v3 = (u((v5 + 1)) >= u(arg2))
                if (arg2 == v5):
                    break
                v4 = load32((arg1 + (v5 << 2)))
                if (u(load32((arg1 + (v5 << 2)))) < u(3)):
                    break
                if (u(v4) < u(v8)):
                    continue
                break
            break
        if v6:
            break
        v4 = (arg2 - 1)
        arg0 = 0
        while True:  # $label5
            while True:  # block $label4
                v3 = (arg0 + 1)
                if (arg0 == v4):
                    break
                v5 = load32((arg1 + (v3 << 2)))
                if (u(load32((arg1 + (v3 << 2)))) < u(3)):
                    break
                arg0 = v3
                if (u(v5) < u(v8)):
                    continue
                break
            break
        v3 = (u(arg2) <= u(v3))
        break
    return v3

# ------------------------------------------------------------
# $func881
# ------------------------------------------------------------
def func881(arg0, arg1, arg2):
    while True:  # block $label0
        v7 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v3 = load32(59164)
        v4 = load32(9561692)
        arg0 = 1
        while True:  # block $label1
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
        if (arg2 == 0):
            v3 = 1
            break
        v4 = load32(arg1)
        v8 = load32(9671136)
        v6 = ((u(load32(arg1)) < u(3)) | (u(v4) >= u(load32(9671136))))
        v3 = 0
        if (load8u(9147152) == 0):
            v5 = 0
            if v6:
                break
            v9 = load32(9215884)
            v10 = load32(9143008)
            v6 = load32(9671128)
            while True:  # $label3
                v4 = (v6 + (load32((v6 + (v4 * 132)) + 36) * 132))
                if (load8u((v10 + ((v7 * load16u((v6 + (load32((v6 + (v4 * 132)) + 36) * 132)) + 110)) + arg0))) == 0):
                    break
                if (load32((v9 + (load32(v4 + 44) << 4)) + 4) == 20):
                    break
                if (load8u(v4 + 127) == 6):
                    break
                v5 = (v5 + 1)
                v3 = (u((v5 + 1)) >= u(arg2))
                if (arg2 == v5):
                    break
                v4 = load32((arg1 + (v5 << 2)))
                if (u(load32((arg1 + (v5 << 2)))) < u(3)):
                    break
                if (u(v4) < u(v8)):
                    continue
                break
            break
        if v6:
            break
        v4 = (arg2 - 1)
        arg0 = 0
        while True:  # $label5
            while True:  # block $label4
                v3 = (arg0 + 1)
                if (arg0 == v4):
                    break
                v5 = load32((arg1 + (v3 << 2)))
                if (u(load32((arg1 + (v3 << 2)))) < u(3)):
                    break
                arg0 = v3
                if (u(v5) < u(v8)):
                    continue
                break
            break
        v3 = (u(arg2) <= u(v3))
        break
    return v3

# ------------------------------------------------------------
# $func882
# ------------------------------------------------------------
def func882(arg0, arg1, arg2):
    return (load8u(9147213) == 0)

# ------------------------------------------------------------
# $func883
# ------------------------------------------------------------
def func883(arg0, arg1, arg2):
    while True:  # block $label0
        v3 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        arg0 = load32(59164)
        v4 = load32(9561692)
        arg2 = 1
        while True:  # block $label1
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
        arg2 = load32(9671128)
        arg1 = load32((arg2 + (load32(arg1) * 132)) + 36)
        if (load8u((load32(9143008) + (arg2 + (v3 * load16u((load32(9671128) + (load32((arg2 + (load32(arg1) * 132)) + 36) * 132)) + 110))))) == 0):
            break
        arg1 = (arg2 + (arg1 * 132))
        if (load32((load32(9215884) + (load32((arg2 + (arg1 * 132)) + 44) << 4)) + 4) == 20):
            break
        break
    return (load8u(arg1 + 127) != 6)

# ------------------------------------------------------------
# $func884
# ------------------------------------------------------------
def func884(arg0, arg1, arg2):
    return (load32(59164) == load32(9561844))

# ------------------------------------------------------------
# $func886
# ------------------------------------------------------------
def func886(arg0, arg1, arg2):
    arg2 = load32(arg0 + 8)
    v3 = load32(arg0 + 4)
    v4 = load32(arg0)
    while True:  # block $label0
        if load8u(9147210):
            arg0 = 0
            v5 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            arg1 = load32(59164)
            v6 = load32(9561692)
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
        arg0 = load32(9142872)
        break
    func414(v4, v3, arg2, arg0, 0)

# ------------------------------------------------------------
# $func889
# ------------------------------------------------------------
def func889(arg0, arg1):
    while True:  # block $label0
        if (load8u(arg1 + 125) == 3):
            break
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label1
                    arg0 = load32(arg0 + 36)
                    if (load32(arg0 + 36) != 2147483646):
                        break
                    arg0 = 0
                    v2 = load32(9142892)
                    if (load32(9142892) == 0):
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
                    if (u(v2) >= u(2147483647)):
                        break
                    break
                    break
                if (arg0 == 2147483647):
                    store8(arg1 + 126, 2)
                    arg0 = 0
                    if (load32(9142892) == 0):
                        break
                    v2 = 0
                    if load16u(arg1 + 110):
                        break
                    break
                if (u(arg0) >= u(load32(9142892))):
                    break
                if (arg0 == load16u(arg1 + 110)):
                    break
                break
            v2 = 0
            if (load8u(arg1 + 126) != 2):
                break
            if load8u(((load8u(arg1 + 122) * 404) + 9568096) + 332):
                break
            store8(arg1 + 126, 0)
            v2 = 1
            break
        func78(arg1, arg0, 0, 1)
        if (load8u(arg1 + 126) == 2):
            if (load32(((load8u(arg1 + 122) * 404) + 9568096) + 264) != 2):
            func29(arg1, 1)
        if (v2 == 0):
            break
        func156(0, arg1, 500)
        break

# ------------------------------------------------------------
# $func900
# ------------------------------------------------------------
def func900(arg0):
    func394(0, arg0)

# ------------------------------------------------------------
# $of
# Export: of
# ------------------------------------------------------------
def of(arg0):
    """Exported as of."""
    if (arg0 == 0):
        return 0
    return (func440(arg0, 32684) != 0)

# ------------------------------------------------------------
# $func1003
# ------------------------------------------------------------
def func1003(arg0, arg1, arg2, arg3, arg4, arg5):
    v6 = (arg2 << 2)

# ------------------------------------------------------------
# $func1004
# ------------------------------------------------------------
def func1004(arg0, arg1, arg2, arg3, arg4, arg5):
    func137(arg0, arg2, 1, 8, arg3, arg4, arg5)
    func137(arg1, arg2, 1, 8, arg3, arg4, arg5)

# ------------------------------------------------------------
# $func1006
# ------------------------------------------------------------
def func1006(arg0, arg1, arg2, arg3, arg4):
    func137(arg0, arg1, 1, 16, arg2, arg3, arg4)

# ------------------------------------------------------------
# $func1022
# ------------------------------------------------------------
def func1022(arg0, arg1, arg2):
    func459(arg0, arg1)
    if arg2:
        func459((arg0 + 32), (arg1 + 4))

# ------------------------------------------------------------
# $func1062
# ------------------------------------------------------------
def func1062(arg0, arg1, arg2, arg3, arg4, arg5):

# ------------------------------------------------------------
# $func1063
# ------------------------------------------------------------
def func1063(arg0, arg1, arg2, arg3, arg4, arg5):
    func137(arg0, 1, arg2, 8, arg3, arg4, arg5)
    func137(arg1, 1, arg2, 8, arg3, arg4, arg5)

# ------------------------------------------------------------
# $func1065
# ------------------------------------------------------------
def func1065(arg0, arg1, arg2, arg3, arg4):
    func137(arg0, 1, arg1, 16, arg2, arg3, arg4)

# ------------------------------------------------------------
# $func1123
# ------------------------------------------------------------
def func1123(arg0):