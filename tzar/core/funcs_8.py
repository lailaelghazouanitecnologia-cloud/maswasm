"""
Tzar Game Engine - Core functions.
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
# $func449
# ------------------------------------------------------------
def func449(arg0, arg1, arg2, arg3, arg4, param5, param6, param7, param8, param9, param10, param11, param12, param13, param14, param15):
    v23 = (G.global0 - 144)
    G.global0 = (G.global0 - 144)
    while True:  # block $label0
        if (arg2 == 0):
            break
        v7 = (v23 + 4)
        if (v23 + 4):
            # TODO: memory.fill []
        else:
        if (0 == 0):
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
        while True:  # block $label25
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
            while True:  # block $label24
                while True:  # block $label1
                    if (arg2 == 0):
                        arg3 = 7
                        break
                    if (u(arg1) < u(12)):
                        arg3 = 7
                        break
                    store32(v9 + 44, 0)
                    store64(v9 + 36, 0)
                    store64(v9 + 28, 0)
                    store64(v9 + 20, 0)
                    store32(v9 + 16, arg1)
                    store32(v9 + 12, arg2)
                    while True:  # block $label2
                        v13 = func358(arg2, 6935)
                        if func358(arg2, 6935):
                            break
                        arg3 = 3
                        if (load32(arg2 + 8) != 1346520407):
                            break
                        v12 = load32(arg2 + 4)
                        if (u((load32(arg2 + 4) + 9)) < u(21)):
                            break
                        while True:  # block $label3
                            if (arg4 == 0):
                                break
                            if (u(v12) <= u((arg1 - 8))):
                                break
                            arg3 = 7
                            break
                            break
                        store32(v9 + 40, v12)
                        arg2 = (arg2 + 12)
                        store32(v9 + 60, (arg2 + 12))
                        arg1 = (arg1 - 12)
                        store32(v9 + 56, (arg1 - 12))
                        if (u(arg1) >= u(8)):
                            break
                        arg3 = 7
                        break
                        break
                    v8 = func358(arg2, 5741)
                    if (func358(arg2, 5741) == 0):
                        if (load32(arg2 + 4) != 10):
                            arg3 = 3
                            break
                        arg3 = 7
                        if (u(arg1) < u(18)):
                            break
                        v16 = ((load16u(arg2 + 12) | (load8u(arg2 + 14) << 16)) + 1)
                        v15 = ((load16u(arg2 + 15) | (load8u(arg2 + 17) << 16)) + 1)
                        if ((((i64(((load16u(arg2 + 12) | (load8u(arg2 + 14) << 16)) + 1)) * i64(((load16u(arg2 + 15) | (load8u(arg2 + 17) << 16)) + 1))) & 0xFFFFFFFFFFFFFFFF) >> 32) != 0):
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
                    while True:  # block $label4
                        if ((v17 == 0) & v18):
                            break
                        arg0 = 7
                        while True:  # block $label5
                            if (u(arg1) < u(4)):
                                break
                            while True:  # block $label20
                                v21 = (v9 + 56)
                                while True:  # block $label6
                                    if (v8 | v13):
                                        if (v13 == 0):
                                            break
                                        if (v8 == 0):
                                            break
                                        if (load32(arg2) != 1213221953):
                                            break
                                    while True:  # block $label10
                                        v11 = (v9 + 56)
                                        v13 = (v9 + 28)
                                        v7 = (v9 + 32)
                                        while True:  # block $label9
                                            while True:  # block $label8
                                                while True:  # block $label7
                                                    if (v9 + 60):
                                                        if (v11 == 0):
                                                            break
                                                        if (v13 == 0):
                                                            break
                                                        if (v7 == 0):
                                                            break
                                                        arg1 = load32(v11)
                                                        arg2 = load32(v9 + 60)
                                                        store32(v13, 0)
                                                        store32(v7, 0)
                                                        store32(v9 + 60, arg2)
                                                        store32(v11, arg1)
                                                        if (u(arg1) < u(8)):
                                                            break
                                                        while True:  # block $label11
                                                            if (v12 == 0):
                                                                while True:  # $label12
                                                                    arg3 = load32(arg2 + 4)
                                                                    if (u(load32(arg2 + 4)) > u(-10)):
                                                                        break
                                                                    v18 = 0
                                                                    if (load32(arg2) == 540561494):
                                                                        break
                                                                    if (load32(arg2) == 1278758998):
                                                                        break
                                                                    arg0 = ((arg3 + 9) & -2)
                                                                    if (u(((arg3 + 9) & -2)) > u(arg1)):
                                                                        break
                                                                    if (load32(arg2) == 1213221953):
                                                                        store32(v13, (arg2 + 8))
                                                                        store32(v7, arg3)
                                                                    arg2 = (arg0 + arg2)
                                                                    store32(v9 + 60, (arg0 + arg2))
                                                                    arg1 = (arg1 - arg0)
                                                                    store32(v11, (arg1 - arg0))
                                                                    if (u(arg1) >= u(8)):
                                                                        continue
                                                                    break
                                                                break
                                                            v29 = 22
                                                            while True:  # $label13
                                                                v18 = 3
                                                                arg0 = load32(arg2 + 4)
                                                                if (u(load32(arg2 + 4)) > u(-10)):
                                                                    break
                                                                arg3 = ((arg0 + 9) & -2)
                                                                v29 = (((arg0 + 9) & -2) + v29)
                                                                if (u((((arg0 + 9) & -2) + v29)) > u(v12)):
                                                                    break
                                                                v18 = 0
                                                                if (load32(arg2) == 540561494):
                                                                    break
                                                                if (load32(arg2) == 1278758998):
                                                                    break
                                                                if (u(arg1) < u(arg3)):
                                                                    break
                                                                if (load32(arg2) == 1213221953):
                                                                    store32(v13, (arg2 + 8))
                                                                    store32(v7, arg0)
                                                                arg2 = (arg2 + arg3)
                                                                store32(v9 + 60, (arg2 + arg3))
                                                                arg1 = (arg1 - arg3)
                                                                store32(v11, (arg1 - arg3))
                                                                v18 = 7
                                                                if (u(arg1) > u(7)):
                                                                    continue
                                                                break
                                                            break
                                                        break
                                                    a_c()
                                                    raise RuntimeError('unreachable')
                                                    break
                                                a_c()
                                                raise RuntimeError('unreachable')
                                                break
                                            a_c()
                                            raise RuntimeError('unreachable')
                                            break
                                        a_c()
                                        raise RuntimeError('unreachable')
                                        break
                                    arg0 = 3290
                                    if 3290:
                                        break
                                    break
                                arg2 = load32(v9 + 40)
                                v13 = (v9 + 36)
                                v7 = (v9 + 44)
                                while True:  # block $label16
                                    while True:  # block $label15
                                        while True:  # block $label14
                                            v11 = load32(v9 + 60)
                                            if load32(v9 + 60):
                                                if (v21 == 0):
                                                    break
                                                if (v13 == 0):
                                                    break
                                                if (v7 == 0):
                                                    break
                                                while True:  # block $label17
                                                    arg1 = load32(v21)
                                                    if (u(load32(v21)) < u(8)):
                                                        break
                                                    while True:  # block $label18
                                                        arg0 = load32(v11)
                                                        if (((load32(v11) != 540561494) & (arg0 != 1278758998)) == 0):
                                                            arg3 = load32(v11 + 4)
                                                            if (u(arg2) >= u(12)):
                                                                if (u(arg3) > u((arg2 - 12))):
                                                                    break
                                                            if arg4:
                                                                if (u(arg3) > u((arg1 - 8))):
                                                                    break
                                                            store32(v13, arg3)
                                                            store32(v9 + 60, (v11 + 8))
                                                            store32(v21, (load32(v21) - 8))
                                                            store32(v7, (arg0 == 1278758998))
                                                            break
                                                        arg0 = 0
                                                        while True:  # block $label19
                                                            if (u(arg1) < u(5)):
                                                                break
                                                            if (load8u(v11) != 47):
                                                                break
                                                            arg0 = (u(load8u(v11 + 4)) < u(32))
                                                            break
                                                        store32(v7, arg0)
                                                        store32(v13, load32(v21))
                                                        break
                                                    break
                                                break
                                            a_c()
                                            raise RuntimeError('unreachable')
                                            break
                                        a_c()
                                        raise RuntimeError('unreachable')
                                        break
                                    a_c()
                                    raise RuntimeError('unreachable')
                                    break
                                a_c()
                                raise RuntimeError('unreachable')
                                break
                            arg0 = 3702
                            if 3702:
                                break
                            arg3 = 3
                            arg2 = load32(v9 + 36)
                            if (u(load32(v9 + 36)) > u(-10)):
                                break
                            v13 = load32(v9 + 56)
                            while True:  # block $label22
                                if (load32(v9 + 44) == 0):
                                    arg0 = 7
                                    if (u(v13) < u(10)):
                                        break
                                    v7 = (v9 + 52)
                                    arg4 = (v9 + 48)
                                    arg0 = 0
                                    while True:  # block $label21
                                        v11 = load32(v9 + 60)
                                        if (load32(v9 + 60) == 0):
                                            break
                                        if (u(v13) < u(10)):
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
                                        if (u((((((load8u(v11 + 1) << 8) | (load8u(v11 + 2) << 16)) | arg1) & 0xFFFFFFFF) >> 5)) >= u(arg2)):
                                            break
                                        arg2 = (load8u(v11 + 6) | ((load8u(v11 + 7) << 8) & 16128))
                                        if ((load8u(v11 + 6) | ((load8u(v11 + 7) << 8) & 16128)) == 0):
                                            break
                                        arg1 = (load8u(v11 + 8) | ((load8u(v11 + 9) << 8) & 16128))
                                        if ((load8u(v11 + 8) | ((load8u(v11 + 9) << 8) & 16128)) == 0):
                                            break
                                        if v7:
                                            store32(v7, arg2)
                                        arg0 = 1
                                        if (arg4 == 0):
                                            break
                                        store32(arg4, arg1)
                                        break
                                    if arg0:
                                        break
                                    break
                                arg0 = 7
                                if (u(v13) < u(5)):
                                    break
                                arg1 = load32(v9 + 60)
                                v7 = (v9 + 52)
                                arg4 = (v9 + 48)
                                arg0 = 0
                                v11 = (G.global0 - 32)
                                G.global0 = (G.global0 - 32)
                                while True:  # block $label23
                                    if (arg1 == 0):
                                        break
                                    if (u(v13) < u(5)):
                                        break
                                    if (load8u(arg1) != 47):
                                        break
                                    if (u(load8u(arg1 + 4)) > u(31)):
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
                                if (arg0 == 0):
                                    break
                                break
                            if (v8 == 0):
                                if (v16 != load32(v9 + 52)):
                                    break
                                if (v15 != load32(v9 + 48)):
                                    break
                            if (v17 == 0):
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
                            raise RuntimeError('unreachable')
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
            raise RuntimeError('unreachable')
            break
        store32(399 + 48, 4033)
        while True:  # block $label26
            while True:  # block $label27
                if load32(v14 + 48):
                    if (load32(v14 + 48) != 7):
                        break
                    if load32(v14 + 156):
                        break
                    break
                if (load32(v14 + 156) == 0):
                    break
                break
            store32(v14 + 48, 4)
            break
        while True:  # block $label167
            while True:  # block $label29
                while True:  # block $label28
                    if load32(v14 + 48):
                        break
                    if (v26 == 0):
                        break
                    arg0 = (v14 + 48)
                    if (v14 + 48):
                        # TODO: memory.fill []
                    arg0 = load32(v14 + 24)
                    store32(v14 + 112, (load32(v14 + 24) + load32(v14 + 12)))
                    store32(v14 + 108, (load32(v14 + 16) - arg0))
                    store32(v14 + 100, 262)
                    store32(v14 + 96, 263)
                    store32(v14 + 92, 264)
                    store32(v14 + 88, v26)
                    while True:  # block $label142
                        if (load32(v14 + 44) == 0):
                            while True:  # block $label30
                                v5 = func134(1, 2424)
                                if (func134(1, 2424) == 0):
                                    break
                                store32(v5 + 8, 6932)
                                store32(v5, 0)
                                # call_indirect[load32(52340)]
                                store32(v5 + 324, 0)
                                store32(v5 + 4, 0)
                                arg0 = load32(52304)
                                if (load32(52304) == load32(52296)):
                                    break
                                while True:  # block $label31
                                    if arg0:
                                        # call_indirect[arg0]
                                        if indirect_call(arg0):
                                            break
                                    break
                                store32(279, 280)
                                store32(52296, load32(52304))
                                break
                            if (v5 == 0):
                                break
                            store32(v5 + 2392, load32(v14 + 28))
                            store32(v5 + 2396, load32(v14 + 32))
                            while True:  # block $label32
                                if func458(v5, (v14 + 48)):
                                    arg3 = func451(load32(v14 + 48), load32(v14 + 52), load32(v26 + 20), load32(v26))
                                    if func451(load32(v14 + 48), load32(v14 + 52), load32(v26 + 20), load32(v26)):
                                        break
                                    arg1 = (v14 + 12)
                                    while True:  # block $label33
                                        arg0 = load32(v26 + 20)
                                        if (load32(v26 + 20) == 0):
                                            break
                                        if (arg1 == 0):
                                            break
                                        if (load32(arg0 + 40) == 0):
                                            break
                                        if (load32(arg1 + 32) == 0):
                                            break
                                        a_c()
                                        raise RuntimeError('unreachable')
                                        break
                                    store32(v5 + 160, 0)
                                    arg2 = load32(v26 + 20)
                                    while True:  # block $label34
                                        if v5:
                                            if (arg2 == 0):
                                                break
                                            while True:  # block $label35
                                                arg0 = load32(arg2 + 44)
                                                if (load32(arg2 + 44) < 0):
                                                    break
                                                arg3 = 255
                                                if (u(arg0) <= u(100)):
                                                    # TODO: i32.div_u []
                                                    arg3 = 100
                                                    if ((arg0 & 65535) == 0):
                                                        break
                                                while True:  # block $label36
                                                    arg0 = load32(v5 + 844)
                                                    if (load32(v5 + 844) >= 12):
                                                        arg1 = load32(v5 + 848)
                                                        break
                                                    arg1 = (((arg3 * load8u(((arg0 if (arg0 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                                                    store32(v5 + 848, (((arg3 * load8u(((arg0 if (arg0 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                                                    break
                                                while True:  # block $label37
                                                    arg0 = load32(v5 + 876)
                                                    if (load32(v5 + 876) >= 12):
                                                        v10 = load32(v5 + 880)
                                                        break
                                                    v10 = (((arg3 * load8u(((arg0 if (arg0 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                                                    store32(v5 + 880, (((arg3 * load8u(((arg0 if (arg0 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                                                    break
                                                arg0 = (arg1 | v10)
                                                while True:  # block $label38
                                                    arg1 = load32(v5 + 908)
                                                    if (load32(v5 + 908) >= 12):
                                                        v10 = load32(v5 + 912)
                                                        break
                                                    v10 = (((arg3 * load8u(((arg1 if (arg1 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                                                    store32(v5 + 912, (((arg3 * load8u(((arg1 if (arg1 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                                                    break
                                                arg0 = (arg0 | v10)
                                                while True:  # block $label39
                                                    arg1 = load32(v5 + 940)
                                                    if (load32(v5 + 940) >= 12):
                                                        arg3 = load32(v5 + 944)
                                                        break
                                                    arg3 = (((arg3 * load8u(((arg1 if (arg1 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3)
                                                    store32(v5 + 944, (((arg3 * load8u(((arg1 if (arg1 > 0) else 0) + 10309))) & 0xFFFFFFFF) >> 3))
                                                    break
                                                if ((arg0 | arg3) == 0):
                                                    break
                                                # TODO: memory.copy []
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
                                        raise RuntimeError('unreachable')
                                        break
                                    arg3 = 0
                                    v22 = (v14 + 48)
                                    v12 = 0
                                    v18 = 0
                                    while True:  # block $label40
                                        if (v5 == 0):
                                            break
                                        while True:  # block $label141
                                            while True:  # block $label41
                                                if (v22 == 0):
                                                    if load32(v5):
                                                        break
                                                    store32(v5 + 8, 8496)
                                                    store32(v5, 2)
                                                    v39 = (v5 + 4)
                                                    break
                                                v39 = (v5 + 4)
                                                while True:  # block $label68
                                                    while True:  # block $label77
                                                        while True:  # block $label130
                                                            while True:  # block $label42
                                                                if (load32(v5 + 4) == 0):
                                                                    if (func458(v5, v22) == 0):
                                                                        break
                                                                    if (load32(v5 + 4) == 0):
                                                                        break
                                                                while True:  # block $label44
                                                                    while True:  # block $label43
                                                                        arg0 = load32(v22 + 48)
                                                                        if (load32(v22 + 48) == 0):
                                                                            break
                                                                        # call_indirect[arg0]
                                                                        if indirect_call(arg0):
                                                                            break
                                                                        break
                                                                        break
                                                                    while True:  # block $label47
                                                                        while True:  # block $label48
                                                                            while True:  # block $label46
                                                                                while True:  # block $label45
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
                                                                    while True:  # block $label50
                                                                        if (arg0 > 0):
                                                                            v13 = load32(v5 + 116)
                                                                            if (load32(v5 + 80) == 0):
                                                                                while True:  # block $label49
                                                                                    if v13:
                                                                                        arg0 = load8s(v5 + 132)
                                                                                        if load32(v5 + 124):
                                                                                            break
                                                                                        break
                                                                                    break
                                                                                arg0 = load32(v5 + 72)
                                                                                v7 = ((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72))
                                                                                arg0 = (((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72)) > 0)
                                                                                if ((((load32(v5 + 72) + arg0) if (arg0 >= 63) else load32(v5 + 72)) > 0) == 0):
                                                                                    store8(v5 + 2356, 0)
                                                                                    store8((v5 + 2360), 0)
                                                                                    store8((v5 + 2358), 0)
                                                                                    break
                                                                                arg1 = (v7 if arg0 else 0)
                                                                                arg4 = (2 if (u(arg1) > u(39)) else (u((v7 if arg0 else 0)) > u(14)))
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
                                                                                arg1 = ((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1))
                                                                                arg0 = (9 - arg0)
                                                                                arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0))
                                                                                arg0 = (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0)))
                                                                                store8((v5 + 2357), (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0))))
                                                                                store8((v5 + 2361), arg0)
                                                                                arg0 = (arg0 + arg2)
                                                                                store8(v5 + 2356, (arg0 + arg2))
                                                                                store8((v5 + 2360), arg0)
                                                                                break
                                                                            v16 = load32(v5 + 84)
                                                                            if (v13 == 0):
                                                                                v7 = (load32(v5 + 72) + v16)
                                                                                v15 = (63 if (v7 >= 63) else (load32(v5 + 72) + v16))
                                                                                arg0 = (v15 > 0)
                                                                                arg2 = ((63 if (v7 >= 63) else (load32(v5 + 72) + v16)) if (v15 > 0) else 0)
                                                                                while True:  # block $label51
                                                                                    if arg0:
                                                                                        arg0 = arg2
                                                                                        arg4 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg1 = ((arg2 & 0xFFFFFFFF) >> (2 if (u(arg4) > u(4)) else 1))
                                                                                            arg0 = (9 - arg4)
                                                                                            arg0 = (((arg2 & 0xFFFFFFFF) >> (2 if (u(arg4) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg4))
                                                                                        store8((v5 + 2359), (2 if (u(arg2) > u(39)) else (u(arg2) > u(14))))
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
                                                                                while True:  # block $label52
                                                                                    if arg0:
                                                                                        arg0 = arg1
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg1 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2363), (2 if (u(arg1) > u(39)) else (u(arg1) > u(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2361), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2360, (arg0 + (arg1 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2360, 0)
                                                                                    break
                                                                                store8((v5 + 2362), 1)
                                                                                while True:  # block $label53
                                                                                    if (v15 > 0):
                                                                                        arg0 = arg2
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg2 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg2 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2367), (2 if (u(arg2) > u(39)) else (u(arg2) > u(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2365), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2364, (arg0 + (arg2 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2364, 0)
                                                                                    break
                                                                                store8((v5 + 2366), 0)
                                                                                while True:  # block $label54
                                                                                    if (v13 > 0):
                                                                                        arg0 = arg1
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg1 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2371), (2 if (u(arg1) > u(39)) else (u(arg1) > u(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2369), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2368, (arg0 + (arg1 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2368, 0)
                                                                                    break
                                                                                store8((v5 + 2370), 1)
                                                                                while True:  # block $label55
                                                                                    if (v15 > 0):
                                                                                        arg0 = arg2
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg2 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg2 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2375), (2 if (u(arg2) > u(39)) else (u(arg2) > u(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2373), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2372, (arg0 + (arg2 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2372, 0)
                                                                                    break
                                                                                store8((v5 + 2374), 0)
                                                                                while True:  # block $label56
                                                                                    if (v13 > 0):
                                                                                        arg0 = arg1
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg1 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2379), (2 if (u(arg1) > u(39)) else (u(arg1) > u(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2377), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2376, (arg0 + (arg1 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2376, 0)
                                                                                    break
                                                                                store8((v5 + 2378), 1)
                                                                                while True:  # block $label57
                                                                                    if (v15 > 0):
                                                                                        arg0 = arg2
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg4 = ((arg2 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((arg2 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1)) if (arg0 > arg4) else (9 - v7))
                                                                                        store8((v5 + 2383), (2 if (u(arg2) > u(39)) else (u(arg2) > u(14))))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v5 + 2381), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v5 + 2380, (arg0 + (arg2 << 1)))
                                                                                        break
                                                                                    store8(v5 + 2380, 0)
                                                                                    break
                                                                                store8((v5 + 2382), 0)
                                                                                while True:  # block $label58
                                                                                    if (v13 > 0):
                                                                                        arg0 = arg1
                                                                                        arg4 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg2 = ((arg1 & 0xFFFFFFFF) >> (2 if (u(arg4) > u(4)) else 1))
                                                                                            arg0 = (9 - arg4)
                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg4) > u(4)) else 1)) if (arg0 > arg2) else (9 - arg4))
                                                                                        store8((v5 + 2387), (2 if (u(arg1) > u(39)) else (u(arg1) > u(14))))
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
                                                                                while True:  # block $label59
                                                                                    if arg2:
                                                                                    else:
                                                                                    v15 = ((load32(v5 + 72) + arg0) + v16)
                                                                                    arg0 = (arg0 if (v15 >= 63) else ((load32(v5 + 72) + arg0) + v16))
                                                                                    if ((arg0 if (v15 >= 63) else ((load32(v5 + 72) + arg0) + v16)) > 0):
                                                                                        v8 = (arg0 if (arg0 > 0) else 0)
                                                                                        arg0 = (arg0 if (arg0 > 0) else 0)
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg1 = ((v8 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((v8 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1)) if (arg0 > arg1) else (9 - v7))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v11 + 2357), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v13, (arg0 + (v8 << 1)))
                                                                                        store8((v11 + 2359), (2 if (u(v8) > u(39)) else (u(v8) > u(14))))
                                                                                        break
                                                                                    store8(v13, 0)
                                                                                    break
                                                                                store8((v11 + 2358), 0)
                                                                                v13 = (v11 + 2360)
                                                                                while True:  # block $label60
                                                                                    arg0 = (arg4 + v15)
                                                                                    arg0 = (63 if (arg0 >= 63) else (arg4 + v15))
                                                                                    if ((63 if (arg0 >= 63) else (arg4 + v15)) > 0):
                                                                                        v15 = (arg0 if (arg0 > 0) else 0)
                                                                                        arg0 = (arg0 if (arg0 > 0) else 0)
                                                                                        v7 = load32(v5 + 76)
                                                                                        if (load32(v5 + 76) > 0):
                                                                                            arg1 = ((v15 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1))
                                                                                            arg0 = (9 - v7)
                                                                                            arg0 = (((v15 & 0xFFFFFFFF) >> (2 if (u(v7) > u(4)) else 1)) if (arg0 > arg1) else (9 - v7))
                                                                                        arg0 = (1 if (arg0 <= 1) else arg0)
                                                                                        store8((v11 + 2361), (1 if (arg0 <= 1) else arg0))
                                                                                        store8(v13, (arg0 + (v15 << 1)))
                                                                                        store8((v11 + 2363), (2 if (u(v15) > u(39)) else (u(v15) > u(14))))
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
                                                                    while True:  # block $label63
                                                                        while True:  # block $label62
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
                                                                            arg4 = (2 if (u(arg1) > u(39)) else (u((v7 if (v7 > 0) else 0)) > u(14)))
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
                                                                            arg1 = ((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1))
                                                                            arg0 = (9 - arg0)
                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0))
                                                                            arg0 = (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0)))
                                                                            store8((v5 + 2365), (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0))))
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
                                                                    while True:  # block $label65
                                                                        while True:  # block $label64
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
                                                                            arg4 = (2 if (u(arg1) > u(39)) else (u((v7 if (v7 > 0) else 0)) > u(14)))
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
                                                                            arg1 = ((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1))
                                                                            arg0 = (9 - arg0)
                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0))
                                                                            arg0 = (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0)))
                                                                            store8((v5 + 2373), (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0))))
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
                                                                    while True:  # block $label67
                                                                        while True:  # block $label66
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
                                                                            arg4 = (2 if (u(arg1) > u(39)) else (u((v7 if (v7 > 0) else 0)) > u(14)))
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
                                                                            arg1 = ((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1))
                                                                            arg0 = (9 - arg0)
                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0))
                                                                            arg0 = (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0)))
                                                                            store8((v5 + 2381), (1 if (arg0 <= 1) else (((arg1 & 0xFFFFFFFF) >> (2 if (u(arg0) > u(4)) else 1)) if (arg0 > arg1) else (9 - arg0))))
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
                                                                while True:  # block $label71
                                                                    arg1 = 0
                                                                    store32(v5 + 164, 0)
                                                                    v12 = 1
                                                                    while True:  # block $label70
                                                                        while True:  # block $label69
                                                                            if (load32(v5 + 160) > 0):
                                                                                # call_indirect[load32(52344)]
                                                                                if (indirect_call(load32(52344)) == 0):
                                                                                    break
                                                                                store32(v5 + 152, (v5 + 192))
                                                                                store32(v5 + 148, v5)
                                                                                store32(v5 + 144, 261)
                                                                                v12 = (3 if (load32(v5 + 2352) > 0) else 2)
                                                                            store32(v5 + 168, v12)
                                                                            break
                                                                            break
                                                                        if (func99(v5, 1, 8437) == 0):
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
                                                                    while True:  # block $label75
                                                                        while True:  # block $label72
                                                                            if load32(v5 + 2392):
                                                                            else:
                                                                            v41 = 0
                                                                            v40 = (0 + (i64(v11) + (i64(v15) + (i64(v8) + (i64(v21) + (i64(arg4) + i64(v17)))))))
                                                                            if (u((0 + (i64(v11) + (i64(v15) + (i64(v8) + (i64(v21) + (i64(arg4) + i64(v17)))))))) > u(4294966432)):
                                                                                break
                                                                            v10 = load32(v5 + 2332)
                                                                            while True:  # block $label76
                                                                                while True:  # block $label73
                                                                                    v40 = (v40 + 863)
                                                                                    arg1 = load32(v5 + 2336)
                                                                                    if (u((v40 + 863)) > u(i64(load32(v5 + 2336)))):
                                                                                        arg1 = 0
                                                                                        store32(v5 + 2336, 0)
                                                                                        v10 = func58(v40, 1)
                                                                                        store32(v5 + 2332, func58(v40, 1))
                                                                                        if (v10 == 0):
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
                                                                                    while True:  # block $label74
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
                                                                                    store32(v5 + 2408, (0 if (v41 == 0) else (arg4 + v11)))
                                                                                    arg2 = (((arg2 & 0xFFFFFFFF) >> 1) * v16)
                                                                                    arg0 = ((((arg2 & 0xFFFFFFFF) >> 1) * v16) + (arg0 + (v13 * v15)))
                                                                                    store32(v5 + 2316, ((((arg2 & 0xFFFFFFFF) >> 1) * v16) + (arg0 + (v13 * v15))))
                                                                                    store32(v5 + 2320, ((arg0 + ((v12 * v16) << 3)) + arg2))
                                                                                    if (u((arg4 + i32(v41))) > u((arg1 + v10))):
                                                                                        break
                                                                                    # TODO: memory.fill []
                                                                                    store16((load32(v5 + 2300) - 2), 0)
                                                                                    store32(v5 + 2340, 0)
                                                                                    store32(v5 + 2292, 0)
                                                                                    # TODO: memory.fill []
                                                                                    break
                                                                                    break
                                                                                if (func99(v5, 1, 8229) == 0):
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
                                                                    raise RuntimeError('unreachable')
                                                                    break
                                                                if (2020 == 0):
                                                                    break
                                                                store32(v5 + 2344, 0)
                                                                if (load32(v5 + 320) > 0):
                                                                    v6 = (v5 + 16)
                                                                    while True:  # $label139
                                                                        v15 = load32(v5 + 324)
                                                                        while True:  # block $label129
                                                                            v17 = 0
                                                                            while True:  # block $label80
                                                                                if (load32(v5 + 300) > 0):
                                                                                    v16 = (v5 + 2292)
                                                                                    while True:  # $label128
                                                                                        v13 = load32(v5 + 2288)
                                                                                        v7 = load32(v5 + 2348)
                                                                                        while True:  # block $label78
                                                                                            if (load32(v5 + 120) == 0):
                                                                                                break
                                                                                            arg1 = load32(v6 + 8)
                                                                                            arg0 = load8u(v5 + 948)
                                                                                            while True:  # block $label79
                                                                                                arg2 = load32(v6 + 12)
                                                                                                if (load32(v6 + 12) >= 0):
                                                                                                    break
                                                                                                arg4 = load32(v6 + 16)
                                                                                                if (load32(v6 + 16) == 0):
                                                                                                    break
                                                                                                if (u(load32(v6 + 24)) > u(arg4)):
                                                                                                    v40 = load64(arg4)
                                                                                                    store32(v6 + 16, (arg4 + 7))
                                                                                                    store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # block $label81
                                                                                                v11 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                v41 = load64(v6)
                                                                                                v40 = i64(arg2)
                                                                                                arg4 = i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))
                                                                                                if (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))):
                                                                                                    v41 = (v41 - (i64((v11 + 1)) << v40))
                                                                                                    store64(v6, (v41 - (i64((v11 + 1)) << v40)))
                                                                                                    break
                                                                                                break
                                                                                            arg1 = (v11 + 1)
                                                                                            arg0 = (clz((v11 + 1)) ^ 24)
                                                                                            arg2 = ((arg1 - v11) - (clz((v11 + 1)) ^ 24))
                                                                                            store32(arg2 + 12, ((arg1 - v11) - (clz((v11 + 1)) ^ 24)))
                                                                                            v8 = ((arg1 << arg0) - 1)
                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                            if (u(arg4) <= u(v11)):
                                                                                                arg0 = load8u(v5 + 949)
                                                                                                while True:  # block $label82
                                                                                                    if (arg2 >= 0):
                                                                                                        break
                                                                                                    arg1 = load32(v6 + 16)
                                                                                                    if (load32(v6 + 16) == 0):
                                                                                                        break
                                                                                                    if (u(load32(v6 + 24)) > u(arg1)):
                                                                                                        v40 = load64(arg1)
                                                                                                        store32(v6 + 16, (arg1 + 7))
                                                                                                        v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                        store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                        arg2 = (arg2 + 56)
                                                                                                        break
                                                                                                    func36(v6)
                                                                                                    v41 = load64(v6)
                                                                                                    arg2 = load32(v6 + 12)
                                                                                                    break
                                                                                                while True:  # block $label83
                                                                                                    arg4 = (((arg0 * v8) & 0xFFFFFFFF) >> 8)
                                                                                                    v40 = i64(arg2)
                                                                                                    arg2 = i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))
                                                                                                    if (u((((arg0 * v8) & 0xFFFFFFFF) >> 8)) < u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))):
                                                                                                        store64(v6, (v41 - (i64((arg4 + 1)) << v40)))
                                                                                                        break
                                                                                                    break
                                                                                                arg1 = (arg4 + 1)
                                                                                                arg0 = (clz((arg4 + 1)) ^ 24)
                                                                                                store32(arg2 + 12, ((v8 - arg4) - (clz((arg4 + 1)) ^ 24)))
                                                                                                store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                break
                                                                                            arg0 = load8u(v5 + 950)
                                                                                            while True:  # block $label84
                                                                                                if (arg2 >= 0):
                                                                                                    break
                                                                                                arg1 = load32(v6 + 16)
                                                                                                if (load32(v6 + 16) == 0):
                                                                                                    break
                                                                                                if (u(load32(v6 + 24)) > u(arg1)):
                                                                                                    v40 = load64(arg1)
                                                                                                    store32(v6 + 16, (arg1 + 7))
                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                v41 = load64(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # block $label85
                                                                                                arg4 = (((arg0 * v8) & 0xFFFFFFFF) >> 8)
                                                                                                v40 = i64(arg2)
                                                                                                arg2 = i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))
                                                                                                if (u((((arg0 * v8) & 0xFFFFFFFF) >> 8)) < u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))):
                                                                                                    store64(v6, (v41 - (i64((arg4 + 1)) << v40)))
                                                                                                    break
                                                                                                break
                                                                                            arg1 = (arg4 + 1)
                                                                                            arg0 = (clz((arg4 + 1)) ^ 24)
                                                                                            store32(arg2 + 12, ((v8 - arg4) - (clz((arg4 + 1)) ^ 24)))
                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                            break
                                                                                        arg0 = ((u(arg2) > u(arg4)) | 2)
                                                                                        v9 = (v7 + (v17 * 800))
                                                                                        store8((v7 + (v17 * 800)) + 798, arg0)
                                                                                        while True:  # block $label86
                                                                                            if (load32(v5 + 2280) == 0):
                                                                                                arg2 = load32(v6 + 12)
                                                                                                v10 = load32(v6 + 8)
                                                                                                break
                                                                                            arg1 = load32(v6 + 8)
                                                                                            arg0 = load8u(v5 + 2284)
                                                                                            while True:  # block $label87
                                                                                                arg2 = load32(v6 + 12)
                                                                                                if (load32(v6 + 12) >= 0):
                                                                                                    break
                                                                                                arg4 = load32(v6 + 16)
                                                                                                if (load32(v6 + 16) == 0):
                                                                                                    break
                                                                                                if (u(load32(v6 + 24)) > u(arg4)):
                                                                                                    v40 = load64(arg4)
                                                                                                    store32(v6 + 16, (arg4 + 7))
                                                                                                    store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # block $label88
                                                                                                v7 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                v41 = load64(v6)
                                                                                                v40 = i64(arg2)
                                                                                                arg4 = i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))
                                                                                                if (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))):
                                                                                                    store64(v6, (v41 - (i64((v7 + 1)) << v40)))
                                                                                                    break
                                                                                                break
                                                                                            arg1 = (v7 + 1)
                                                                                            arg0 = (clz((v7 + 1)) ^ 24)
                                                                                            arg2 = ((arg1 - v7) - (clz((v7 + 1)) ^ 24))
                                                                                            store32(arg2 + 12, ((arg1 - v7) - (clz((v7 + 1)) ^ 24)))
                                                                                            v10 = ((arg1 << arg0) - 1)
                                                                                            store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                            store8(v9 + 797, (u(arg4) > u(v7)))
                                                                                            break
                                                                                        while True:  # block $label89
                                                                                            if (arg2 >= 0):
                                                                                                break
                                                                                            arg0 = load32(v6 + 16)
                                                                                            if (load32(v6 + 16) == 0):
                                                                                                break
                                                                                            if (u(load32(v6 + 24)) > u(arg0)):
                                                                                                v40 = load64(arg0)
                                                                                                store32(v6 + 16, (arg0 + 7))
                                                                                                store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                arg2 = (arg2 + 56)
                                                                                                break
                                                                                            func36(v6)
                                                                                            arg2 = load32(v6 + 12)
                                                                                            break
                                                                                        v8 = ((v17 << 2) + v13)
                                                                                        while True:  # block $label90
                                                                                            arg0 = (((v10 * 145) & 0xFFFFFFFF) >> 8)
                                                                                            v41 = load64(v6)
                                                                                            v40 = i64(arg2)
                                                                                            arg4 = (u((((v10 * 145) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))))
                                                                                            if ((u((((v10 * 145) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))) == 0):
                                                                                                store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
                                                                                                break
                                                                                            break
                                                                                        arg1 = (arg0 + 1)
                                                                                        arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                        arg2 = ((v10 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                        store32(arg2 + 12, ((v10 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                        arg0 = ((arg1 << arg0) - 1)
                                                                                        store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                        store8(v9 + 768, arg4)
                                                                                        while True:  # block $label98
                                                                                            if (arg4 == 0):
                                                                                                while True:  # block $label91
                                                                                                    if (arg2 >= 0):
                                                                                                        break
                                                                                                    arg1 = load32(v6 + 16)
                                                                                                    if (load32(v6 + 16) == 0):
                                                                                                        break
                                                                                                    if (u(load32(v6 + 24)) > u(arg1)):
                                                                                                        v40 = load64(arg1)
                                                                                                        store32(v6 + 16, (arg1 + 7))
                                                                                                        store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                        arg2 = (arg2 + 56)
                                                                                                        break
                                                                                                    func36(v6)
                                                                                                    arg2 = load32(v6 + 12)
                                                                                                    break
                                                                                                while True:  # block $label92
                                                                                                    arg1 = (((arg0 * 156) & 0xFFFFFFFF) >> 8)
                                                                                                    v41 = load64(v6)
                                                                                                    v40 = i64(arg2)
                                                                                                    arg4 = (u((((arg0 * 156) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))))
                                                                                                    if ((u((((arg0 * 156) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))) == 0):
                                                                                                        v41 = (v41 - (i64((arg1 + 1)) << v40))
                                                                                                        store64(v6, (v41 - (i64((arg1 + 1)) << v40)))
                                                                                                        break
                                                                                                    break
                                                                                                arg1 = (arg1 + 1)
                                                                                                arg0 = (clz((arg1 + 1)) ^ 24)
                                                                                                arg2 = ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24))
                                                                                                store32(arg2 + 12, ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24)))
                                                                                                arg1 = ((arg1 << arg0) - 1)
                                                                                                store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                while True:  # block $label95
                                                                                                    if (arg4 == 0):
                                                                                                        while True:  # block $label93
                                                                                                            if (arg2 >= 0):
                                                                                                                break
                                                                                                            arg0 = load32(v6 + 16)
                                                                                                            if (load32(v6 + 16) == 0):
                                                                                                                break
                                                                                                            if (u(load32(v6 + 24)) > u(arg0)):
                                                                                                                v40 = load64(arg0)
                                                                                                                store32(v6 + 16, (arg0 + 7))
                                                                                                                v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                arg2 = (arg2 + 56)
                                                                                                                break
                                                                                                            func36(v6)
                                                                                                            v41 = load64(v6)
                                                                                                            arg2 = load32(v6 + 12)
                                                                                                            break
                                                                                                        while True:  # block $label94
                                                                                                            arg0 = (((arg1 & 0xFFFFFFFF) >> 1) & 16777215)
                                                                                                            v40 = i64(arg2)
                                                                                                            if (u((((arg1 & 0xFFFFFFFF) >> 1) & 16777215)) < u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))):
                                                                                                                v19 = 1
                                                                                                                store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
                                                                                                                break
                                                                                                            v19 = 3
                                                                                                            break
                                                                                                        arg1 = (arg0 + 1)
                                                                                                        arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                        arg2 = ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                        break
                                                                                                    while True:  # block $label96
                                                                                                        if (arg2 >= 0):
                                                                                                            break
                                                                                                        arg0 = load32(v6 + 16)
                                                                                                        if (load32(v6 + 16) == 0):
                                                                                                            break
                                                                                                        if (u(load32(v6 + 24)) > u(arg0)):
                                                                                                            v40 = load64(arg0)
                                                                                                            store32(v6 + 16, (arg0 + 7))
                                                                                                            v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                            store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                            arg2 = (arg2 + 56)
                                                                                                            break
                                                                                                        func36(v6)
                                                                                                        v41 = load64(v6)
                                                                                                        arg2 = load32(v6 + 12)
                                                                                                        break
                                                                                                    while True:  # block $label97
                                                                                                        arg0 = (((arg1 * 163) & 0xFFFFFFFF) >> 8)
                                                                                                        v40 = i64(arg2)
                                                                                                        if (u((((arg1 * 163) & 0xFFFFFFFF) >> 8)) < u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))):
                                                                                                            store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
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
                                                                                                    while True:  # block $label99
                                                                                                        arg2 = load32(v6 + 12)
                                                                                                        if (load32(v6 + 12) >= 0):
                                                                                                            break
                                                                                                        arg4 = load32(v6 + 16)
                                                                                                        if (load32(v6 + 16) == 0):
                                                                                                            break
                                                                                                        if (u(load32(v6 + 24)) > u(arg4)):
                                                                                                            v40 = load64(arg4)
                                                                                                            store32(v6 + 16, (arg4 + 7))
                                                                                                            store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                            arg2 = (arg2 + 56)
                                                                                                            break
                                                                                                        func36(v6)
                                                                                                        arg2 = load32(v6 + 12)
                                                                                                        break
                                                                                                    while True:  # block $label100
                                                                                                        arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                        v41 = load64(v6)
                                                                                                        v40 = i64(arg2)
                                                                                                        arg4 = (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))))
                                                                                                        if ((u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))) == 0):
                                                                                                            v41 = (v41 - (i64((arg0 + 1)) << v40))
                                                                                                            store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
                                                                                                            break
                                                                                                        break
                                                                                                    arg1 = (arg0 + 1)
                                                                                                    arg0 = (clz((arg0 + 1)) ^ 24)
                                                                                                    v12 = ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24))
                                                                                                    store32(arg2 + 12, ((arg1 - arg0) - (clz((arg0 + 1)) ^ 24)))
                                                                                                    arg1 = ((arg1 << arg0) - 1)
                                                                                                    store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                    arg2 = 0
                                                                                                    while True:  # block $label101
                                                                                                        if arg4:
                                                                                                            break
                                                                                                        arg0 = load8u(v27 + 1)
                                                                                                        while True:  # block $label102
                                                                                                            if (v12 >= 0):
                                                                                                                break
                                                                                                            arg2 = load32(v6 + 16)
                                                                                                            if (load32(v6 + 16) == 0):
                                                                                                                break
                                                                                                            if (u(load32(v6 + 24)) > u(arg2)):
                                                                                                                v40 = load64(arg2)
                                                                                                                store32(v6 + 16, (arg2 + 7))
                                                                                                                v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                v12 = (v12 + 56)
                                                                                                                break
                                                                                                            func36(v6)
                                                                                                            v41 = load64(v6)
                                                                                                            v12 = load32(v6 + 12)
                                                                                                            break
                                                                                                        while True:  # block $label103
                                                                                                            arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                            v40 = i64(v12)
                                                                                                            arg4 = (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v12)))))
                                                                                                            if ((u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v12))))) == 0):
                                                                                                                v41 = (v41 - (i64((arg0 + 1)) << v40))
                                                                                                                store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
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
                                                                                                        while True:  # block $label104
                                                                                                            if (v10 >= 0):
                                                                                                                break
                                                                                                            arg2 = load32(v6 + 16)
                                                                                                            if (load32(v6 + 16) == 0):
                                                                                                                break
                                                                                                            if (u(load32(v6 + 24)) > u(arg2)):
                                                                                                                v40 = load64(arg2)
                                                                                                                store32(v6 + 16, (arg2 + 7))
                                                                                                                v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                v10 = (v10 + 56)
                                                                                                                break
                                                                                                            func36(v6)
                                                                                                            v41 = load64(v6)
                                                                                                            v10 = load32(v6 + 12)
                                                                                                            break
                                                                                                        while True:  # block $label105
                                                                                                            arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                            v40 = i64(v10)
                                                                                                            arg4 = (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v10)))))
                                                                                                            if ((u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v10))))) == 0):
                                                                                                                v41 = (v41 - (i64((arg0 + 1)) << v40))
                                                                                                                store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
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
                                                                                                        while True:  # block $label106
                                                                                                            if (v10 >= 0):
                                                                                                                break
                                                                                                            arg2 = load32(v6 + 16)
                                                                                                            if (load32(v6 + 16) == 0):
                                                                                                                break
                                                                                                            if (u(load32(v6 + 24)) > u(arg2)):
                                                                                                                v40 = load64(arg2)
                                                                                                                store32(v6 + 16, (arg2 + 7))
                                                                                                                v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                v10 = (v10 + 56)
                                                                                                                break
                                                                                                            func36(v6)
                                                                                                            v41 = load64(v6)
                                                                                                            v10 = load32(v6 + 12)
                                                                                                            break
                                                                                                        while True:  # block $label107
                                                                                                            v21 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                            v40 = i64(v10)
                                                                                                            arg4 = i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v10)))
                                                                                                            if (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v10))))):
                                                                                                                v41 = (v41 - (i64((v21 + 1)) << v40))
                                                                                                                store64(v6, (v41 - (i64((v21 + 1)) << v40)))
                                                                                                                break
                                                                                                            break
                                                                                                        arg1 = (v21 + 1)
                                                                                                        arg0 = (clz((v21 + 1)) ^ 24)
                                                                                                        arg2 = ((arg1 - v21) - (clz((v21 + 1)) ^ 24))
                                                                                                        store32(v10 + 12, ((arg1 - v21) - (clz((v21 + 1)) ^ 24)))
                                                                                                        v11 = ((arg1 << arg0) - 1)
                                                                                                        store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                                        while True:  # block $label112
                                                                                                            if (u(arg4) <= u(v21)):
                                                                                                                arg0 = load8u(v27 + 4)
                                                                                                                while True:  # block $label108
                                                                                                                    if (arg2 >= 0):
                                                                                                                        break
                                                                                                                    arg1 = load32(v6 + 16)
                                                                                                                    if (load32(v6 + 16) == 0):
                                                                                                                        break
                                                                                                                    if (u(load32(v6 + 24)) > u(arg1)):
                                                                                                                        v40 = load64(arg1)
                                                                                                                        store32(v6 + 16, (arg1 + 7))
                                                                                                                        v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                        store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                        arg2 = (arg2 + 56)
                                                                                                                        break
                                                                                                                    func36(v6)
                                                                                                                    v41 = load64(v6)
                                                                                                                    arg2 = load32(v6 + 12)
                                                                                                                    break
                                                                                                                while True:  # block $label109
                                                                                                                    arg0 = (((arg0 * v11) & 0xFFFFFFFF) >> 8)
                                                                                                                    v40 = i64(arg2)
                                                                                                                    arg4 = (u((((arg0 * v11) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))))
                                                                                                                    if ((u((((arg0 * v11) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))) == 0):
                                                                                                                        v41 = (v41 - (i64((arg0 + 1)) << v40))
                                                                                                                        store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
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
                                                                                                                while True:  # block $label110
                                                                                                                    if (v12 >= 0):
                                                                                                                        break
                                                                                                                    arg2 = load32(v6 + 16)
                                                                                                                    if (load32(v6 + 16) == 0):
                                                                                                                        break
                                                                                                                    if (u(load32(v6 + 24)) > u(arg2)):
                                                                                                                        v40 = load64(arg2)
                                                                                                                        store32(v6 + 16, (arg2 + 7))
                                                                                                                        v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                        store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                        v12 = (v12 + 56)
                                                                                                                        break
                                                                                                                    func36(v6)
                                                                                                                    v41 = load64(v6)
                                                                                                                    v12 = load32(v6 + 12)
                                                                                                                    break
                                                                                                                while True:  # block $label111
                                                                                                                    arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                                    v40 = i64(v12)
                                                                                                                    if (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v12))))):
                                                                                                                        store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
                                                                                                                        v10 = (arg1 - arg0)
                                                                                                                        break
                                                                                                                    v10 = (arg0 + 1)
                                                                                                                    break
                                                                                                                arg2 = 4
                                                                                                                arg0 = (clz(v10) ^ 24)
                                                                                                                v12 = (v12 - (clz(v10) ^ 24))
                                                                                                                break
                                                                                                            arg0 = load8u(v27 + 6)
                                                                                                            while True:  # block $label113
                                                                                                                if (arg2 >= 0):
                                                                                                                    break
                                                                                                                arg1 = load32(v6 + 16)
                                                                                                                if (load32(v6 + 16) == 0):
                                                                                                                    break
                                                                                                                if (u(load32(v6 + 24)) > u(arg1)):
                                                                                                                    v40 = load64(arg1)
                                                                                                                    store32(v6 + 16, (arg1 + 7))
                                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                    arg2 = (arg2 + 56)
                                                                                                                    break
                                                                                                                func36(v6)
                                                                                                                v41 = load64(v6)
                                                                                                                arg2 = load32(v6 + 12)
                                                                                                                break
                                                                                                            while True:  # block $label114
                                                                                                                arg0 = (((arg0 * v11) & 0xFFFFFFFF) >> 8)
                                                                                                                v40 = i64(arg2)
                                                                                                                arg4 = (u((((arg0 * v11) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))))
                                                                                                                if ((u((((arg0 * v11) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))) == 0):
                                                                                                                    v41 = (v41 - (i64((arg0 + 1)) << v40))
                                                                                                                    store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
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
                                                                                                            while True:  # block $label115
                                                                                                                if (v12 >= 0):
                                                                                                                    break
                                                                                                                arg2 = load32(v6 + 16)
                                                                                                                if (load32(v6 + 16) == 0):
                                                                                                                    break
                                                                                                                if (u(load32(v6 + 24)) > u(arg2)):
                                                                                                                    v40 = load64(arg2)
                                                                                                                    store32(v6 + 16, (arg2 + 7))
                                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                    v12 = (v12 + 56)
                                                                                                                    break
                                                                                                                func36(v6)
                                                                                                                v41 = load64(v6)
                                                                                                                v12 = load32(v6 + 12)
                                                                                                                break
                                                                                                            while True:  # block $label116
                                                                                                                arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                                v40 = i64(v12)
                                                                                                                arg4 = (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v12)))))
                                                                                                                if ((u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v12))))) == 0):
                                                                                                                    v41 = (v41 - (i64((arg0 + 1)) << v40))
                                                                                                                    store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
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
                                                                                                            while True:  # block $label117
                                                                                                                if (v10 >= 0):
                                                                                                                    break
                                                                                                                arg2 = load32(v6 + 16)
                                                                                                                if (load32(v6 + 16) == 0):
                                                                                                                    break
                                                                                                                if (u(load32(v6 + 24)) > u(arg2)):
                                                                                                                    v40 = load64(arg2)
                                                                                                                    store32(v6 + 16, (arg2 + 7))
                                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                                    v10 = (v10 + 56)
                                                                                                                    break
                                                                                                                func36(v6)
                                                                                                                v41 = load64(v6)
                                                                                                                v10 = load32(v6 + 12)
                                                                                                                break
                                                                                                            while True:  # block $label118
                                                                                                                arg0 = (((arg0 * arg1) & 0xFFFFFFFF) >> 8)
                                                                                                                v40 = i64(v10)
                                                                                                                if (u((((arg0 * arg1) & 0xFFFFFFFF) >> 8)) < u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(v10))))):
                                                                                                                    store64(v6, (v41 - (i64((arg0 + 1)) << v40)))
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
                                                                                        while True:  # block $label121
                                                                                            arg2 = load32(v6 + 12)
                                                                                            if (load32(v6 + 12) >= 0):
                                                                                                break
                                                                                            arg1 = load32(v6 + 16)
                                                                                            if (load32(v6 + 16) == 0):
                                                                                                break
                                                                                            if (u(load32(v6 + 24)) > u(arg1)):
                                                                                                v40 = load64(arg1)
                                                                                                store32(v6 + 16, (arg1 + 7))
                                                                                                store64(v6, ((load64(v6) << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                arg2 = (arg2 + 56)
                                                                                                break
                                                                                            func36(v6)
                                                                                            arg2 = load32(v6 + 12)
                                                                                            break
                                                                                        while True:  # block $label122
                                                                                            arg1 = (((arg0 * 142) & 0xFFFFFFFF) >> 8)
                                                                                            v41 = load64(v6)
                                                                                            v40 = i64(arg2)
                                                                                            arg4 = (u((((arg0 * 142) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))))
                                                                                            if ((u((((arg0 * 142) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(v6) & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))) == 0):
                                                                                                v41 = (v41 - (i64((arg1 + 1)) << v40))
                                                                                                store64(v6, (v41 - (i64((arg1 + 1)) << v40)))
                                                                                                break
                                                                                            break
                                                                                        arg1 = (arg1 + 1)
                                                                                        arg0 = (clz((arg1 + 1)) ^ 24)
                                                                                        arg2 = ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24))
                                                                                        store32(arg2 + 12, ((arg0 - arg1) - (clz((arg1 + 1)) ^ 24)))
                                                                                        arg0 = ((arg1 << arg0) - 1)
                                                                                        store32(v6 + 8, ((arg1 << arg0) - 1))
                                                                                        v19 = 0
                                                                                        while True:  # block $label123
                                                                                            if arg4:
                                                                                                break
                                                                                            while True:  # block $label124
                                                                                                if (arg2 >= 0):
                                                                                                    break
                                                                                                arg1 = load32(v6 + 16)
                                                                                                if (load32(v6 + 16) == 0):
                                                                                                    break
                                                                                                if (u(load32(v6 + 24)) > u(arg1)):
                                                                                                    v40 = load64(arg1)
                                                                                                    store32(v6 + 16, (arg1 + 7))
                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                v41 = load64(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # block $label125
                                                                                                arg1 = (((arg0 * 114) & 0xFFFFFFFF) >> 8)
                                                                                                v40 = i64(arg2)
                                                                                                arg4 = (u((((arg0 * 114) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2)))))
                                                                                                if ((u((((arg0 * 114) & 0xFFFFFFFF) >> 8)) >= u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))) == 0):
                                                                                                    v41 = (v41 - (i64((arg1 + 1)) << v40))
                                                                                                    store64(v6, (v41 - (i64((arg1 + 1)) << v40)))
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
                                                                                            while True:  # block $label126
                                                                                                if (arg2 >= 0):
                                                                                                    break
                                                                                                arg1 = load32(v6 + 16)
                                                                                                if (load32(v6 + 16) == 0):
                                                                                                    break
                                                                                                if (u(load32(v6 + 24)) > u(arg1)):
                                                                                                    v40 = load64(arg1)
                                                                                                    store32(v6 + 16, (arg1 + 7))
                                                                                                    v41 = ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                                                                                    store64(v6, ((v41 << 56) | ((((((v40 << 56) | ((v40 & 65280) << 40)) | (((v40 & 16711680) << 24) | ((v40 & 4278190080) << 8))) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v40 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v40 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                                                                    arg2 = (arg2 + 56)
                                                                                                    break
                                                                                                func36(v6)
                                                                                                v41 = load64(v6)
                                                                                                arg2 = load32(v6 + 12)
                                                                                                break
                                                                                            while True:  # block $label127
                                                                                                arg1 = (((arg0 * 183) & 0xFFFFFFFF) >> 8)
                                                                                                v40 = i64(arg2)
                                                                                                if (u((((arg0 * 183) & 0xFFFFFFFF) >> 8)) < u(i32(((v41 & 0xFFFFFFFFFFFFFFFF) >> i64(arg2))))):
                                                                                                    v19 = 1
                                                                                                    store64(v6, (v41 - (i64((arg1 + 1)) << v40)))
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
                                                                            raise RuntimeError('unreachable')
                                                                            break
                                                                        if (3339 == 0):
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
                                                                                while True:  # block $label134
                                                                                    while True:  # block $label131
                                                                                        if load32(v5 + 2280):
                                                                                            arg0 = (v34 + (v30 * 800))
                                                                                            if load8u((v34 + (v30 * 800)) + 797):
                                                                                                break
                                                                                        arg0 = (v34 + (v30 * 800))
                                                                                        v16 = load8u((v34 + (v30 * 800)) + 798)
                                                                                        # TODO: memory.fill []
                                                                                        v7 = (v5 + (v16 << 5))
                                                                                        while True:  # block $label132
                                                                                            if (load8u(arg0 + 768) == 0):
                                                                                                v18 = (v5 + 2008)
                                                                                                store64(v28 + 24, 0)
                                                                                                store64(v28 + 16, 0)
                                                                                                store64(v28 + 8, 0)
                                                                                                store64(v28, 0)
                                                                                                v10 = 1
                                                                                                arg1 = (arg2 - 1)
                                                                                                arg4 = (arg2 + (v30 << 1))
                                                                                                # call_indirect[load32(9687280)]
                                                                                                arg2 = indirect_call(load32(9687280))
                                                                                                arg1 = (indirect_call(load32(9687280)) > 0)
                                                                                                store8(v28, (indirect_call(load32(9687280)) > 0))
                                                                                                store8(arg4 + 1, arg1)
                                                                                                if (arg2 >= 2):
                                                                                                    # call_indirect[load32(9687332)]
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
                                                                                            # call_indirect[load32(9687280)]
                                                                                            v17 = indirect_call(load32(9687280))
                                                                                            v15 = load16u(arg0)
                                                                                            arg2 = (v10 < v17)
                                                                                            arg0 = ((v35 & 0xFFFFFFFF) >> 1)
                                                                                            # call_indirect[load32(9687280)]
                                                                                            v21 = indirect_call(load32(9687280))
                                                                                            v13 = load16u(arg1 + 32)
                                                                                            v7 = (v10 < v21)
                                                                                            arg2 = ((((arg0 & 126) | (arg2 << 7)) & 0xFFFFFFFF) >> 1)
                                                                                            # call_indirect[load32(9687280)]
                                                                                            v11 = indirect_call(load32(9687280))
                                                                                            arg0 = load16u(arg1 + 64)
                                                                                            arg4 = (v10 < v11)
                                                                                            arg2 = ((((v7 << 7) | arg2) & 0xFFFFFFFF) >> 1)
                                                                                            # call_indirect[load32(9687280)]
                                                                                            v7 = indirect_call(load32(9687280))
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
                                                                                        # call_indirect[load32(9687280)]
                                                                                        v36 = indirect_call(load32(9687280))
                                                                                        v9 = load16u(arg1 + 128)
                                                                                        arg0 = (v36 > 0)
                                                                                        # call_indirect[load32(9687280)]
                                                                                        v37 = indirect_call(load32(9687280))
                                                                                        v17 = load16u(arg1 + 160)
                                                                                        # call_indirect[load32(9687280)]
                                                                                        v38 = indirect_call(load32(9687280))
                                                                                        v21 = load16u(arg1 + 192)
                                                                                        v11 = (v38 > 0)
                                                                                        v8 = (v37 > 0)
                                                                                        # call_indirect[load32(9687280)]
                                                                                        v10 = indirect_call(load32(9687280))
                                                                                        v16 = load16u(arg1 + 224)
                                                                                        arg4 = load8u(v32)
                                                                                        arg2 = load8u(v33)
                                                                                        # call_indirect[load32(9687280)]
                                                                                        v12 = indirect_call(load32(9687280))
                                                                                        v15 = load16u(arg1 + 256)
                                                                                        arg0 = (v12 > 0)
                                                                                        # call_indirect[load32(9687280)]
                                                                                        v18 = indirect_call(load32(9687280))
                                                                                        v13 = load16u(arg1 + 288)
                                                                                        # call_indirect[load32(9687280)]
                                                                                        v19 = indirect_call(load32(9687280))
                                                                                        v7 = load16u(arg1 + 320)
                                                                                        arg0 = (v19 > 0)
                                                                                        arg4 = (v18 > 0)
                                                                                        # call_indirect[load32(9687280)]
                                                                                        v20 = indirect_call(load32(9687280))
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
                                                                                    if (load8u(arg0 + 768) == 0):
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
                                                                        while True:  # block $label137
                                                                            arg0 = 0
                                                                            while True:  # block $label136
                                                                                if (load32(v5 + 2352) <= 0):
                                                                                    break
                                                                                arg1 = load32(v5 + 2344)
                                                                                if (load32(v5 + 2344) < load32(v5 + 312)):
                                                                                    break
                                                                                arg0 = (arg1 <= load32(v5 + 320))
                                                                                break
                                                                            arg4 = (v5 + 172)
                                                                            if (load32(v5 + 160) == 0):
                                                                                store32(v5 + 180, arg0)
                                                                                store32(v5 + 176, load32(v5 + 2344))
                                                                                func273(v20, 0, (arg1 + 352), arg1, v5, arg4)
                                                                                break
                                                                            arg2 = (v5 + 136)
                                                                            # call_indirect[load32(52348)]
                                                                            arg1 = indirect_call(load32(52348))
                                                                            if (load32(v5 + 140) == 1):
                                                                                if (arg1 & 1):
                                                                                    # TODO: memory.copy []
                                                                                    store32(v5 + 180, arg0)
                                                                                    store32(v5 + 172, load32(v5 + 164))
                                                                                    store32(v5 + 176, load32(v5 + 2344))
                                                                                    while True:  # block $label138
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
                                                                                    # call_indirect[load32(52352)]
                                                                                    arg0 = (load32(v5 + 164) + 1)
                                                                                    store32(v5 + 164, ((load32(v5 + 164) + 1) if (arg0 != load32(v5 + 168)) else 0))
                                                                                else:
                                                                                break
                                                                            a_c()
                                                                            raise RuntimeError('unreachable')
                                                                            break
                                                                        if (2263 == 0):
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
                                                                while True:  # block $label140
                                                                    if (load32(v5 + 160) <= 0):
                                                                        break
                                                                    # call_indirect[load32(52348)]
                                                                    if indirect_call(load32(52348)):
                                                                        break
                                                                    v20 = 0
                                                                    break
                                                                    break
                                                                v20 = 1
                                                                break
                                                                break
                                                            a_c()
                                                            raise RuntimeError('unreachable')
                                                            break
                                                        v20 = 0
                                                        if load32(v5):
                                                            break
                                                        store32(v5 + 8, 8359)
                                                        store64(v5, 7)
                                                        break
                                                    arg0 = 1
                                                    if (load32(v5 + 160) > 0):
                                                        # call_indirect[load32(52348)]
                                                        arg0 = indirect_call(load32(52348))
                                                    arg1 = load32(v22 + 52)
                                                    if load32(v22 + 52):
                                                        # call_indirect[arg1]
                                                    if (arg0 & v20):
                                                        break
                                                    break
                                                # call_indirect[load32(52360)]
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
                                # call_indirect[load32(52360)]
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
                        if (v8 == 0):
                            break
                        arg3 = (v14 + 48)
                        while True:  # block $label143
                            if (v8 == 0):
                                break
                            while True:  # block $label144
                                if (arg3 == 0):
                                    # br_table[load32(v8)]
                                    break
                                store32(v8, 0)
                                store32(v8 + 8, arg3)
                                arg1 = (v8 + 24)
                                while True:  # block $label148
                                    while True:  # block $label146
                                        while True:  # block $label145
                                            if (func39(arg1, 8) != 47):
                                                break
                                            arg2 = func39(arg1, 14)
                                            arg0 = func39(arg1, 14)
                                            if func39(arg1, 3):
                                                break
                                            if (load32(v8 + 48) == 0):
                                                break
                                            break
                                        while True:  # block $label147
                                            # br_table[load32(v8)]
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
                                raise RuntimeError('unreachable')
                                break
                            store32(v8, 2)
                            break
                        while True:  # block $label149
                            if v10:
                                arg3 = func451(load32(v14 + 48), load32(v14 + 52), load32(v26 + 20), load32(v26))
                                if func451(load32(v14 + 48), load32(v14 + 52), load32(v26 + 20), load32(v26)):
                                    break
                                arg3 = 0
                                while True:  # block $label150
                                    if (v8 == 0):
                                        break
                                    while True:  # block $label164
                                        while True:  # block $label159
                                            while True:  # block $label158
                                                while True:  # block $label155
                                                    while True:  # block $label154
                                                        while True:  # block $label153
                                                            while True:  # block $label152
                                                                while True:  # block $label151
                                                                    if load32(v8 + 172):
                                                                        if (load32(v8 + 168) == 0):
                                                                            break
                                                                        if (load32(v8 + 164) <= 0):
                                                                            break
                                                                        v16 = load32(v8 + 8)
                                                                        if (load32(v8 + 8) == 0):
                                                                            break
                                                                        v13 = load32(v16 + 40)
                                                                        if (load32(v16 + 40) == 0):
                                                                            break
                                                                        while True:  # block $label157
                                                                            while True:  # block $label156
                                                                                if load32(v8 + 4):
                                                                                    arg0 = load32(v13)
                                                                                    store32(v8 + 12, load32(v13))
                                                                                    if (arg0 == 0):
                                                                                        break
                                                                                    if (func447(load32(v13 + 20), v16, 3) == 0):
                                                                                        arg1 = 2
                                                                                        # br_table[load32(v8)]
                                                                                        break
                                                                                    arg0 = load32(v8 + 100)
                                                                                    arg1 = load32(v16)
                                                                                    if (load32(v8 + 100) > load32(v16)):
                                                                                        break
                                                                                    v40 = (load32s(v8 + 104) * i64(arg0))
                                                                                    arg0 = (arg1 & 65535)
                                                                                    arg1 = func58(((load32s(v8 + 104) * i64(arg0)) + (i64((arg1 & 65535)) + (i64(arg1) << 4))), 4)
                                                                                    store32(v8 + 16, func58(((load32s(v8 + 104) * i64(arg0)) + (i64((arg1 & 65535)) + (i64(arg1) << 4))), 4))
                                                                                    if (arg1 == 0):
                                                                                        store32(v8 + 20, 0)
                                                                                        arg1 = 1
                                                                                        # br_table[load32(v8)]
                                                                                        break
                                                                                    store32(v8 + 20, ((arg1 + (i32(v40) << 2)) + (arg0 << 2)))
                                                                                    while True:  # block $label161
                                                                                        while True:  # block $label160
                                                                                            if load32(v16 + 92):
                                                                                                v7 = load32(v16 + 100)
                                                                                                arg4 = load32(v16 + 16)
                                                                                                arg0 = load32(v16 + 12)
                                                                                                arg1 = 1
                                                                                                arg2 = load32(v16 + 96)
                                                                                                v41 = i64(load32(v16 + 96))
                                                                                                v40 = (i64(load32(v16 + 96)) << 5)
                                                                                                v15 = func58((((i64(load32(v16 + 96)) << 5) + (v41 << 2)) + 84), 1)
                                                                                                if (func58((((i64(load32(v16 + 96)) << 5) + (v41 << 2)) + 84), 1) == 0):
                                                                                                    # br_table[load32(v8)]
                                                                                                    break
                                                                                                if load32(v8 + 280):
                                                                                                    break
                                                                                                store32(v8 + 284, v15)
                                                                                                store32(v8 + 280, v15)
                                                                                                arg0 = (v15 + 84)
                                                                                                if (func90(v15, arg0, arg4, ((v15 + 84) + i32(v40)), arg2, v7, 0, 4, arg0) == 0):
                                                                                                    break
                                                                                                if load32(v16 + 92):
                                                                                                    break
                                                                                            arg1 = load32(load32(v8 + 12))
                                                                                            if (u((load32(load32(v8 + 12)) - 11)) < u(-4)):
                                                                                                break
                                                                                            break
                                                                                        func188()
                                                                                        arg1 = load32(load32(v8 + 12))
                                                                                        break
                                                                                    while True:  # block $label162
                                                                                        if (u(arg1) < u(11)):
                                                                                            break
                                                                                        arg0 = load32(52304)
                                                                                        if (load32(52304) != load32(52336)):
                                                                                            store32(9688020, 406)
                                                                                            store32(9688016, 407)
                                                                                            store32(9688004, 408)
                                                                                            store32(9688008, 409)
                                                                                            store32(9688012, 410)
                                                                                            store32(52336, arg0)
                                                                                        if (load32(load32(v8 + 12) + 28) == 0):
                                                                                            break
                                                                                        func188()
                                                                                        break
                                                                                    while True:  # block $label163
                                                                                        if (load32(v8 + 56) == 0):
                                                                                            break
                                                                                        if (load32(v8 + 120) <= 0):
                                                                                            break
                                                                                        arg0 = (v8 + 136)
                                                                                        if load32((v8 + 136)):
                                                                                            break
                                                                                        if func455(arg0, load32(v8 + 132)):
                                                                                            break
                                                                                        arg1 = 1
                                                                                        # br_table[load32(v8)]
                                                                                        break
                                                                                        break
                                                                                    store32(v8 + 4, 0)
                                                                                if (func275(v8, load32(v8 + 16), load32(v8 + 100), load32(v8 + 104), load32(v16 + 88), 278) == 0):
                                                                                    break
                                                                                store32(v13 + 16, load32(v8 + 116))
                                                                                break
                                                                                break
                                                                            store32(v8, arg1)
                                                                            break
                                                                        func191(v8)
                                                                        if (load32(v8) == 0):
                                                                            break
                                                                        break
                                                                    a_c()
                                                                    raise RuntimeError('unreachable')
                                                                    break
                                                                a_c()
                                                                raise RuntimeError('unreachable')
                                                                break
                                                            a_c()
                                                            raise RuntimeError('unreachable')
                                                            break
                                                        a_c()
                                                        raise RuntimeError('unreachable')
                                                        break
                                                    a_c()
                                                    raise RuntimeError('unreachable')
                                                    break
                                                a_c()
                                                raise RuntimeError('unreachable')
                                                break
                                            a_c()
                                            raise RuntimeError('unreachable')
                                            break
                                        a_c()
                                        raise RuntimeError('unreachable')
                                        break
                                    a_c()
                                    raise RuntimeError('unreachable')
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
                    if (load32(v26 + 20) == 0):
                        break
                    if (load32(arg0 + 48) == 0):
                        break
                    v7 = load32(v26)
                    if load32(v26):
                        arg4 = load32(v7 + 16)
                        arg2 = load32(v7 + 8)
                        while True:  # block $label166
                            while True:  # block $label165
                                if (u(load32(v7)) <= u(10)):
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
                                v40 = (i64(arg2) - 1)
                                arg2 = i32((i64(arg2) - 1))
                                store32(v7 + 16, (arg4 + (arg0 * i32((i64(arg2) - 1)))))
                                arg0 = i32(((v40 & 0xFFFFFFFFFFFFFFFF) >> 1))
                                store32(v7 + 20, (load32(v7 + 20) + (arg3 * i32(((v40 & 0xFFFFFFFFFFFFFFFF) >> 1)))))
                                store32(v7 + 24, (load32(v7 + 24) + (arg0 * arg1)))
                                arg1 = load32(v7 + 28)
                                if (load32(v7 + 28) == 0):
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
            raise RuntimeError('unreachable')
            break
        break
    G.global0 = (v23 + 144)
    return 3738

# ------------------------------------------------------------
# $func450
# ------------------------------------------------------------
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
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func451
# ------------------------------------------------------------
def func451(arg0, arg1, arg2, arg3):
    v9 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = 2
    while True:  # block $label0
        if (arg1 <= 0):
            break
        if (arg0 <= 0):
            break
        if (arg3 == 0):
            break
        while True:  # block $label1
            if (arg2 == 0):
                break
            if load32(arg2 + 8):
                v5 = arg0
                v6 = arg1
                arg0 = load32(arg2 + 20)
                arg1 = load32(arg2 + 24)
                while True:  # block $label2
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
                if (v10 == 0):
                    break
            if (load32(arg2 + 28) == 0):
                break
            store32(v9 + 12, load32(arg2 + 32))
            store32(v9 + 8, load32(arg2 + 36))
            if (func444(arg0, arg1, (v9 + 12), (v9 + 8)) == 0):
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
        if (u(load32(arg3)) > u(12)):
            break
        while True:  # block $label3
            if (load32(arg3 + 12) > 0):
                break
            if load32(arg3 + 80):
                break
            v12 = i64(arg0)
            v6 = load8u((v5 + 10296))
            if (u((i64(arg0) * i64(load8u((v5 + 10296))))) > u(2147483647)):
                break
            v13 = i64(arg1)
            v10 = (arg0 * v6)
            v14 = (i64(arg1) * i64((arg0 * v6)))
            v4 = 1
            while True:  # block $label4
                if (u(v5) < u(11)):
                    v12 = 0
                    arg0 = 0
                    break
                v6 = (v5 == 12)
                v12 = ((v12 * v13) if (v5 == 12) else 0)
                v11 = (arg0 if v6 else 0)
                arg0 = (((arg0 + 1) & 0xFFFFFFFF) >> 1)
                break
            v13 = (i64((((arg0 + 1) & 0xFFFFFFFF) >> 1)) * i64((((arg1 + 1) & 0xFFFFFFFF) >> 1)))
            v15 = ((i64((((arg0 + 1) & 0xFFFFFFFF) >> 1)) * i64((((arg1 + 1) & 0xFFFFFFFF) >> 1))) << 1)
            arg1 = func58((((i64((((arg0 + 1) & 0xFFFFFFFF) >> 1)) * i64((((arg1 + 1) & 0xFFFFFFFF) >> 1))) << 1) + (v12 + v14)), 1)
            if (func58((((i64((((arg0 + 1) & 0xFFFFFFFF) >> 1)) * i64((((arg1 + 1) & 0xFFFFFFFF) >> 1))) << 1) + (v12 + v14)), 1) == 0):
                break
            store32(arg3 + 16, arg1)
            store32(arg3 + 80, arg1)
            v6 = i32(v14)
            if (u(v5) >= u(11)):
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
        while True:  # block $label5
            arg1 = load32(arg3)
            if (u(load32(arg3)) > u(12)):
                break
            v5 = load32(arg3 + 8)
            arg0 = load32(arg3 + 4)
            while True:  # block $label7
                while True:  # block $label6
                    if (u(arg1) >= u(11)):
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
                        v12 = i64(arg0)
                        v14 = i64((v5 - 1))
                        v13 = i64(v4)
                        v15 = i64((((v5 + 1) // 2) - 1))
                        v5 = (((((((load32(arg3 + 40) ^ (v4 >> 31)) - v4) >= ((arg0 + 1) // 2)) & ((((load32(arg3 + 36) ^ (v7 >> 31)) - v7) >= v4) & ((((load32(arg3 + 32) ^ (v8 >> 31)) - v8) >= arg0) & (((u(load32u(arg3 + 48)) >= u((i64(arg0) + (i64((v5 - 1)) * i64(v8))))) & (u(load32u(arg3 + 52)) >= u((i64(v4) + (i64((((v5 + 1) // 2) - 1)) * i64(v7)))))) & (u(load32u(arg3 + 56)) >= u(((i64(v10) * v15) + v13))))))) & (load32(arg3 + 16) != 0)) & (load32(arg3 + 20) != 0)) & (load32(arg3 + 24) != 0))
                        if (arg1 != 12):
                            break
                        arg1 = load32(arg3 + 44)
                        arg1 = (arg1 >> 31)
                        arg1 = ((load32(arg3 + 44) ^ (arg1 >> 31)) - arg1)
                        if ((((arg0 <= ((load32(arg3 + 44) ^ (arg1 >> 31)) - arg1)) & (u(load32u(arg3 + 60)) >= u(((i64(arg1) * v14) + v12)))) & (load32(arg3 + 28) != 0)) & v5):
                            break
                        break
                    v4 = load32(arg3 + 20)
                    v4 = (v4 >> 31)
                    v4 = ((load32(arg3 + 20) ^ (v4 >> 31)) - v4)
                    arg1 = load8u((arg1 + 10296))
                    if (((((load32(arg3 + 20) ^ (v4 >> 31)) - v4) >= (arg0 * load8u((arg1 + 10296)))) & (u(load32u(arg3 + 24)) >= u(((i64((v5 - 1)) * i64(v4)) + (i64(arg0) * i64(arg1)))))) & (load32(arg3 + 16) != 0)):
                        break
                    break
                    break
                if (v5 == 0):
                    break
                break
            v6 = 0
            break
        v4 = v6
        if (arg2 == 0):
            break
        if v4:
            break
        if (load32(arg2 + 48) == 0):
            v4 = 0
            break
        arg2 = load32(arg3 + 16)
        v5 = load32(arg3 + 8)
        while True:  # block $label8
            if (u(load32(arg3)) <= u(10)):
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
            v12 = (i64(v5) - 1)
            v5 = i32((i64(v5) - 1))
            store32(arg3 + 16, (arg2 + (arg0 * i32((i64(v5) - 1)))))
            arg0 = i32(((v12 & 0xFFFFFFFFFFFFFFFF) >> 1))
            store32(arg3 + 20, (load32(arg3 + 20) + (arg1 * i32(((v12 & 0xFFFFFFFFFFFFFFFF) >> 1)))))
            store32(arg3 + 24, (load32(arg3 + 24) + (arg0 * v6)))
            arg2 = load32(arg3 + 28)
            if (load32(arg3 + 28) == 0):
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

# ------------------------------------------------------------
# $func452
# ------------------------------------------------------------
def func452(arg0, arg1):
    store32(arg1 + 8, 0)
    store32(arg1 + 16, arg1)
    v3 = func58(i64(arg0), 4)
    if func58(i64(arg0), 4):
        store32(arg1 + 4, v3)
        v2 = 1
    else:
    store32(arg0 + 12, 0)
    store32(arg1, v3)
    return v2

# ------------------------------------------------------------
# $func453
# ------------------------------------------------------------
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

# ------------------------------------------------------------
# $func454
# ------------------------------------------------------------
def func454(arg0, arg1, arg2, arg3):
    while True:  # block $label12
        while True:  # block $label13
            while True:  # block $label0
                while True:  # block $label11
                    while True:  # block $label6
                        while True:  # block $label10
                            while True:  # block $label5
                                while True:  # block $label9
                                    while True:  # block $label4
                                        while True:  # block $label8
                                            while True:  # block $label3
                                                while True:  # block $label2
                                                    while True:  # block $label7
                                                        while True:  # block $label1
                                                            # br_table[arg2]
                                                            break
                                                            break
                                                        # call_indirect[load32(9687580)]
                                                        return
                                                        break
                                                    # call_indirect[load32(9687580)]
                                                    break
                                                    break
                                                # call_indirect[load32(9687584)]
                                                return
                                                break
                                            # TODO: memory.copy []
                                            return
                                            break
                                        # TODO: memory.copy []
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
                                        if (u((arg0 + 4)) < u(arg2)):
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
                                        if (u((arg0 + 4)) < u(v5)):
                                            continue
                                        break
                                # call_indirect[load32(9687292)]
                                return
                                break
                            # call_indirect[load32(9687588)]
                            return
                            break
                        # call_indirect[load32(9687588)]
                        # call_indirect[load32(9687296)]
                        return
                        break
                    # call_indirect[load32(9687592)]
                    return
                    break
                a_c()
                raise RuntimeError('unreachable')
                break
            # call_indirect[load32(9687576)]
            break
        return
        break
    # call_indirect[load32(9687292)]

# ------------------------------------------------------------
# $func455
# ------------------------------------------------------------
def func455(arg0, arg1):
    v3 = func134(i64((1 << arg1)), 4)
    while True:  # block $label0
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
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')
    return 2481

# ------------------------------------------------------------
# $func456
# ------------------------------------------------------------
def func456(arg0, arg1):
    while True:  # block $label1
        while True:  # block $label0
            if arg0:
                if (arg1 == 0):
                    break
                v2 = load32(arg0 + 8)
                if (load32(arg0 + 8) != load32(arg1 + 8)):
                    break
                # TODO: memory.copy []
                return
            a_c()
            raise RuntimeError('unreachable')
            break
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func457
# ------------------------------------------------------------
def func457(arg0, arg1, arg2, arg3):
    v9 = (G.global0 - 1024)
    G.global0 = (G.global0 - 1024)
    v6 = func276(0, arg1, arg2, arg3, 0)
    if (arg3 < 2329):
        while True:  # block $label1
            while True:  # block $label0
                if (arg0 == 0):
                    break
                if (v6 == 0):
                    break
                v4 = load32(arg0 + 16)
                v7 = load32(load32(arg0 + 16) + 4)
                v8 = load32(v4 + 12)
                if (u((load32(load32(arg0 + 16) + 4) + (v6 << 2))) >= u((load32(v4) + (load32(v4 + 12) << 2)))):
                    v4 = 0
                    v5 = func58(1, 16)
                    if (func58(1, 16) == 0):
                        break
                    v8 = (v6 if (v6 > v8) else v8)
                    v7 = func58(i64((v6 if (v6 > v8) else v8)), 4)
                    if (func58(i64((v6 if (v6 > v8) else v8)), 4) == 0):
                        break
                    store32(v5 + 8, 0)
                    store32(v5 + 4, v7)
                    store32(v5, v7)
                    store32(v5 + 12, v8)
                    store32(load32(arg0 + 16) + 8, v5)
                    store32(arg0 + 16, v5)
                if (arg3 <= 512):
                    break
                v4 = func58(i64(arg3), 2)
                if (func58(i64(arg3), 2) == 0):
                    v4 = 0
                    break
                break
            v4 = v6
            break
        G.global0 = (v9 + 1024)
        return v4
    a_c()
    raise RuntimeError('unreachable')
    return 4778

# ------------------------------------------------------------
# $func458
# ------------------------------------------------------------
def func458(arg0, arg1):
    while True:  # block $label0
        if (arg0 == 0):
            break
        store32(arg0 + 8, 6932)
        store32(arg0, 0)
        if (arg1 == 0):
            store32(arg0 + 8, 8788)
            store64(arg0, 2)
            break
        while True:  # block $label2
            while True:  # block $label1
                v10 = load32(arg1 + 60)
                if (u(load32(arg1 + 60)) <= u(3)):
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
                store8(arg0 + 52, ((v4 & 1) == 0))
                v8 = (((v4 | ((v3 << 8) | (v8 << 16))) & 0xFFFFFFFF) >> 5)
                store32(arg0 + 56, (((v4 | ((v3 << 8) | (v8 << 16))) & 0xFFFFFFFF) >> 5))
                if (u(v11) >= u(4)):
                    store32(arg0 + 8, 8180)
                    break
                if (v5 == 0):
                    store32(arg0 + 8, 8285)
                    store64(arg0, 4)
                    break
                v4 = (v10 - 3)
                v3 = (v2 + 3)
                if (v12 == 0):
                    if (u(v4) <= u(6)):
                        store32(arg0 + 8, 3600)
                        break
                    while True:  # block $label4
                        while True:  # block $label3
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
                while True:  # block $label5
                    if (u(v4) < u(v8)):
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
                    while True:  # block $label6
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
                            if (load32(arg0 + 120) == 0):
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
                    while True:  # block $label7
                        if (v2 == 0):
                            break
                        if (func33(arg1, 1) == 0):
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
                        if (func33(arg1, 1) == 0):
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
                    while True:  # block $label8
                        v4 = (v4 - v5)
                        v3 = (v8 * 3)
                        if (u((v4 - v5)) < u((v8 * 3))):
                            break
                        v12 = (v2 + v4)
                        v4 = (v4 - v3)
                        v3 = (v2 + v3)
                        if v11:
                            v11 = (1 if (u(v8) <= u(1)) else v8)
                            v9 = (arg0 + 328)
                            while True:  # $label9
                                v5 = (load16u(v2) | (load8u(v2 + 2) << 16))
                                v5 = ((load16u(v2) | (load8u(v2 + 2) << 16)) if (u(v4) > u(v5)) else v4)
                                func270((v9 + (v10 << 5)), v3, ((load16u(v2) | (load8u(v2 + 2) << 16)) if (u(v4) > u(v5)) else v4))
                                v4 = (v4 - v5)
                                v3 = (v3 + v5)
                                v2 = (v2 + 3)
                                v10 = (v10 + 1)
                                if ((v10 + 1) != v11):
                                    continue
                                break
                        func270(((arg0 + (v8 << 5)) + 328), v3, v4)
                        if (u(v3) < u(v12)):
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
                    store32(arg0 + 832, (8 if (u(v2) < u(524288)) else (((load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
                    while True:  # block $label10
                        if (v9 == 0):
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
                        store32(arg0 + 864, (8 if (u(v2) < u(524288)) else (((load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
                        v2 = (v3 + v11)
                        v2 = (127 if (v2 >= 127) else (v3 + v11))
                        v2 = (load16u(((((127 if (v2 >= 127) else (v3 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581)
                        store32(arg0 + 896, (8 if (u(v2) < u(524288)) else (((load16u(((((127 if (v2 >= 127) else (v3 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
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
                        store32(arg0 + 928, (8 if (u(v2) < u(524288)) else (((load16u(((((127 if (v2 >= 127) else (v2 + v11)) if (v2 > 0) else 0) << 1) + 10496)) * 101581) & 0xFFFFFFFF) >> 16)))
                        break
                    if (load8u(arg0 + 52) == 0):
                        if load32(arg0):
                            break
                        store32(arg0 + 8, 8268)
                        store64(arg0, 4)
                        break
                    v8 = 0
                    v11 = (arg0 + 948)
                    while True:  # block $label26
                        while True:  # block $label12
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
                                        while True:  # block $label11
                                            v2 = load32(arg1 + 12)
                                            if (load32(arg1 + 12) >= 0):
                                                break
                                            v5 = load32(arg1 + 16)
                                            if (load32(arg1 + 16) == 0):
                                                break
                                            if (u(load32(arg1 + 24)) > u(v5)):
                                                v15 = load64(v5)
                                                store32(arg1 + 16, (v5 + 7))
                                                store64(arg1, ((load64(arg1) << 56) | ((((((v15 << 56) | ((v15 & 65280) << 40)) | (((v15 & 16711680) << 24) | ((v15 & 4278190080) << 8))) | ((((v15 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v15 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v15 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                                v2 = (v2 + 56)
                                                break
                                            func36(arg1)
                                            v2 = load32(arg1 + 12)
                                            break
                                        while True:  # block $label13
                                            v5 = (((v6 * v14) & 0xFFFFFFFF) >> 8)
                                            v15 = load64(arg1)
                                            v16 = i64(v2)
                                            v2 = (u((((v6 * v14) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(arg1) & 0xFFFFFFFFFFFFFFFF) >> i64(v2)))))
                                            if ((u((((v6 * v14) & 0xFFFFFFFF) >> 8)) >= u(i32(((load64(arg1) & 0xFFFFFFFFFFFFFFFF) >> i64(v2))))) == 0):
                                                store64(arg1, (v15 - (i64((v5 + 1)) << v16)))
                                                break
                                            break
                                        v5 = (v5 + 1)
                                        v6 = (clz((v5 + 1)) ^ 24)
                                        store32(v2 + 12, ((v6 - v5) - (clz((v5 + 1)) ^ 24)))
                                        store32(arg1 + 8, ((v5 << v6) - 1))
                                        while True:  # block $label14
                                            if (v2 == 0):
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
                                        while True:  # block $label16
                                            v2 = load32(arg1 + 12)
                                            if (load32(arg1 + 12) >= 0):
                                                break
                                            v5 = load32(arg1 + 16)
                                            if (load32(arg1 + 16) == 0):
                                                break
                                            if (u(load32(arg1 + 24)) <= u(v5)):
                                                func36(arg1)
                                                v2 = load32(arg1 + 12)
                                                break
                                            v15 = load64(v5)
                                            store32(arg1 + 16, (v5 + 7))
                                            store64(arg1, ((load64(arg1) << 56) | ((((((v15 << 56) | ((v15 & 65280) << 40)) | (((v15 & 16711680) << 24) | ((v15 & 4278190080) << 8))) | ((((v15 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v15 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v15 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                            v2 = (v2 + 56)
                                            break
                                        while True:  # block $label17
                                            v5 = (((v6 * v13) & 0xFFFFFFFF) >> 8)
                                            v15 = load64(arg1)
                                            v16 = i64(v2)
                                            v2 = (u((((v6 * v13) & 0xFFFFFFFF) >> 8)) < u(i32(((load64(arg1) & 0xFFFFFFFFFFFFFFFF) >> i64(v2)))))
                                            if ((u((((v6 * v13) & 0xFFFFFFFF) >> 8)) < u(i32(((load64(arg1) & 0xFFFFFFFFFFFFFFFF) >> i64(v2))))) == 0):
                                                break
                                            store64(arg1, (v15 - (i64((v5 + 1)) << v16)))
                                            break
                                        v5 = (v6 - v5)
                                        v6 = (clz((v6 - v5)) ^ 24)
                                        store32(v2 + 12, ((v5 + 1) - (clz((v6 - v5)) ^ 24)))
                                        store32(arg1 + 8, ((v5 << v6) - 1))
                                        while True:  # block $label18
                                            if (v2 == 0):
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
                                        while True:  # block $label20
                                            v2 = load32(arg1 + 12)
                                            if (load32(arg1 + 12) >= 0):
                                                break
                                            v5 = load32(arg1 + 16)
                                            if (load32(arg1 + 16) == 0):
                                                break
                                            if (u(load32(arg1 + 24)) <= u(v5)):
                                                func36(arg1)
                                                v2 = load32(arg1 + 12)
                                                break
                                            v15 = load64(v5)
                                            store32(arg1 + 16, (v5 + 7))
                                            store64(arg1, ((load64(arg1) << 56) | ((((((v15 << 56) | ((v15 & 65280) << 40)) | (((v15 & 16711680) << 24) | ((v15 & 4278190080) << 8))) | ((((v15 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v15 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v15 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                            v2 = (v2 + 56)
                                            break
                                        while True:  # block $label21
                                            v5 = (((v6 * v13) & 0xFFFFFFFF) >> 8)
                                            v15 = load64(arg1)
                                            v16 = i64(v2)
                                            v2 = (u((((v6 * v13) & 0xFFFFFFFF) >> 8)) < u(i32(((load64(arg1) & 0xFFFFFFFFFFFFFFFF) >> i64(v2)))))
                                            if ((u((((v6 * v13) & 0xFFFFFFFF) >> 8)) < u(i32(((load64(arg1) & 0xFFFFFFFFFFFFFFFF) >> i64(v2))))) == 0):
                                                break
                                            store64(arg1, (v15 - (i64((v5 + 1)) << v16)))
                                            break
                                        v5 = (v6 - v5)
                                        v6 = (clz((v6 - v5)) ^ 24)
                                        store32(v2 + 12, ((v5 + 1) - (clz((v6 - v5)) ^ 24)))
                                        store32(arg1 + 8, ((v5 << v6) - 1))
                                        while True:  # block $label22
                                            if (v2 == 0):
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
                        raise RuntimeError('unreachable')
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

# ------------------------------------------------------------
# $func459
# ------------------------------------------------------------
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

# ------------------------------------------------------------
# $func460
# ------------------------------------------------------------
def func460(arg0):
    v1 = load32(arg0 + 8)
    if load32(arg0 + 8):
        # call_indirect[v1]
        v1 = indirect_call(v1)
        store32(arg0 + 20, (load32(arg0 + 20) | (v1 == 0)))
    return load32(arg0 + 16)

# ------------------------------------------------------------
# $func461
# ------------------------------------------------------------
def func461(arg0, arg1, arg2):
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = 1
    while True:  # block $label2
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label1
                    while True:  # block $label0
                        v6 = ((arg0 * 404) + 9568096)
                        # br_table[load32(((arg0 * 404) + 9568096) + 264)]
                        break
                        break
                    store64(v4 + 4, 1)
                    store32(v4, arg0)
                    store32(v4 + 44, arg1)
                    func417(v4, (v4 + 44), 1)
                    break
                    break
                v11 = load32(9671128)
                v23 = load32(arg2 + 283876)
                v24 = load32(arg2 + 283872)
                if (load32(v6 + 188) != 2):
                    break
                v9 = load32(9142440)
                v12 = (load32(9142440) + 2)
                v14 = ((arg0 * 404) + 9568096)
                v16 = load32(9142840)
                v3 = 0
                while True:  # $label12
                    while True:  # block $label5
                        v7 = v3
                        arg0 = (v3 << 2)
                        arg2 = (load32((((v3 << 2) | 4) + 8611904)) + v23)
                        if (u(v9) <= u((load32((((v3 << 2) | 4) + 8611904)) + v23))):
                            break
                        v6 = (load32((arg0 + 8611904)) + v24)
                        if (u(v9) <= u((load32((arg0 + 8611904)) + v24))):
                            break
                        if ((arg2 | v6) < 0):
                            break
                        while True:  # block $label6
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
                                while True:  # block $label9
                                    if (u(arg0) < u(v9)):
                                        while True:  # $label8
                                            while True:  # block $label7
                                                if (load8u((v8 + (((v3 - arg2) * v13) + v10))) == 0):
                                                    v3 = (v3 + 1)
                                                    break
                                                if (u(v3) >= u(v9)):
                                                    break
                                                if ((arg0 | v3) < 0):
                                                    break
                                                v3 = (v3 + 1)
                                                if load32((v16 + ((((v3 + 1) * v12) + v5) << 2))):
                                                    break
                                                if (load32(((load8u((v11 + (load32((v16 + ((((v3 + v12) * v12) + v5) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1):
                                                    break
                                                break
                                            if (v3 != v17):
                                                continue
                                            break
                                            break
                                        raise RuntimeError('unreachable')
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
                        store8((load32(9671128) + arg0) + 129, 3)
                        break
                        break
                    v3 = (v7 + 2)
                    if (u(v7) <= u(3357)):
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
            v9 = ((load8u(v6 + 122) * 404) + 9568096)
            v14 = ((v5 + load32(((load8u(v6 + 122) * 404) + 9568096) + 216)) + 2)
            if ((load16u((v11 + (arg1 * 132)) + 112) - 2) >= ((v5 + load32(((load8u(v6 + 122) * 404) + 9568096) + 216)) + 2)):
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
                while True:  # block $label14
                    v5 = (arg2 + 1)
                    v3 = v7
                    if (u(arg2) < u(v9)):
                        while True:  # $label15
                            v6 = v3
                            v3 = (v3 + 1)
                            while True:  # block $label13
                                if (u(v6) >= u(v9)):
                                    break
                                if ((arg2 | v6) < 0):
                                    break
                                if (load32((v16 + ((v5 + ((v3 + v12) * v12)) << 2))) == 0):
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
        arg1 = ((arg0 * 404) + 9568096)
        v16 = load32(((arg0 * 404) + 9568096) + 220)
        v34 = (load32(((arg0 * 404) + 9568096) + 220) // 2)
        v17 = load32(arg1 + 216)
        v35 = (load32(arg1 + 216) // 2)
        v36 = load32(arg2 + 283908)
        v25 = load32(9142440)
        v3 = 0
        while True:  # $label32
            while True:  # block $label17
                v14 = v3
                v3 = (v3 << 2)
                v26 = load32((((v3 << 2) | 4) + 8611904))
                arg1 = (load32((((v3 << 2) | 4) + 8611904)) + v23)
                if (u(v25) <= u((load32((((v3 << 2) | 4) + 8611904)) + v23))):
                    break
                v27 = load32((v3 + 8611904))
                v3 = (load32((v3 + 8611904)) + v24)
                if (u(v25) <= u((load32((v3 + 8611904)) + v24))):
                    break
                if ((arg1 | v3) < 0):
                    break
                while True:  # block $label31
                    v18 = 0
                    while True:  # block $label19
                        while True:  # block $label18
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
                            v21 = load32(9671128)
                            v10 = load32(9142840)
                            if v12:
                                v19 = (arg1 - 3)
                                v31 = (arg1 + 3)
                                v37 = (v7 - 3)
                                v38 = (v7 + 3)
                                while True:  # $label27
                                    if (u(v3) >= u(v15)):
                                        break
                                    if ((v3 < v38) & (v3 > v37)):
                                        break
                                    v5 = (v3 + 1)
                                    arg1 = v6
                                    while True:  # block $label23
                                        if ((v3 < v11) | (v3 >= v30)):
                                            while True:  # $label22
                                                if (u(arg1) >= u(v15)):
                                                    break
                                                if ((arg1 | v3) < 0):
                                                    break
                                                while True:  # block $label20
                                                    v7 = (arg1 + 1)
                                                    v22 = load32((v10 + ((v5 + (((arg1 + 1) + v8) * v8)) << 2)))
                                                    if (load32((v10 + ((v5 + (((arg1 + 1) + v8) * v8)) << 2))) == 0):
                                                        break
                                                    if (load32(((load8u((v21 + (v22 * 132)) + 122) * 404) + 9568096) + 264) != 1):
                                                        break
                                                    break
                                                    break
                                                while True:  # block $label21
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
                                            raise RuntimeError('unreachable')
                                        while True:  # $label26
                                            if (u(arg1) >= u(v15)):
                                                break
                                            if ((arg1 | v3) < 0):
                                                break
                                            v7 = (arg1 + 1)
                                            while True:  # block $label24
                                                if (((arg1 < v29) & (arg1 >= v9)) == 0):
                                                    v22 = load32((v10 + ((v5 + ((v7 + v8) * v8)) << 2)))
                                                    if (load32((v10 + ((v5 + ((v7 + v8) * v8)) << 2))) == 0):
                                                        break
                                                    if (load32(((load8u((v21 + (v22 * 132)) + 122) * 404) + 9568096) + 264) != 1):
                                                        break
                                                    break
                                                if load32((v10 + ((((v7 + v8) * v8) + v5) << 2))):
                                                    break
                                                if (load32((v10 + (((v7 * v8) + v5) << 2))) == 0):
                                                    break
                                                break
                                                break
                                            while True:  # block $label25
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
                                if (u(v3) < u(v15)):
                                    v3 = (v5 + 1)
                                    v19 = ((v5 < v30) & (v5 >= v11))
                                    arg1 = v6
                                    while True:  # $label29
                                        v18 = 0
                                        v7 = arg1
                                        if (u(v15) <= u(arg1)):
                                            break
                                        if ((v5 | v7) < 0):
                                            break
                                        arg1 = (v7 + 1)
                                        while True:  # block $label28
                                            if ((((v7 >= v9) & v19) & (v7 < v29)) == 0):
                                                v7 = load32((v10 + ((v3 + ((arg1 + v8) * v8)) << 2)))
                                                if (load32((v10 + ((v3 + ((arg1 + v8) * v8)) << 2))) == 0):
                                                    break
                                                if (load32(((load8u((v21 + (v7 * 132)) + 122) * 404) + 9568096) + 264) != 1):
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
                            v18 = (u(v5) < u(v15))
                            break
                        break
                        break
                    break
                if (0 == 0):
                    break
                if (func108((v11 + v35), (v9 + v34), v36, 9) == 0):
                    break
                arg1 = ((v26 * v26) + (v27 * v27))
                if (((v26 * v26) + (v27 * v27)) > load32(arg2 + 283880)):
                    store32(arg2 + 283880, arg1)
                func261(arg0, v11, v9, v32)
                v3 = 1
                break
                break
            v3 = (v14 + 2)
            if (u(v14) <= u(116157)):
                continue
            break
        v3 = 0
        break
    G.global0 = (v4 + 48)
    return v3

# ------------------------------------------------------------
# $func462
# ------------------------------------------------------------
def func462(arg0, arg1, arg2):
    while True:  # block $label4
        while True:  # block $label8
            while True:  # block $label7
                while True:  # block $label5
                    while True:  # block $label2
                        while True:  # block $label1
                            while True:  # block $label3
                                v5 = load32(arg1 + 8)
                                v6 = load32(arg1 + 12)
                                if (load32(arg1 + 8) >= load32(arg1 + 12)):
                                    while True:  # block $label0
                                        v3 = load32(arg2 + 12)
                                        v8 = (v6 - load32(arg2 + 12))
                                        if ((v6 - load32(arg2 + 12)) <= 0):
                                            break
                                        v9 = (load32(arg1 + 4) + v3)
                                        v10 = load32(arg1)
                                        v3 = load32(arg0 + 24)
                                        v6 = load32(arg0 + 28)
                                        if (u(load32(arg0 + 24)) < u(load32(arg0 + 28))):
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
                                        if (u((((v3 - load32((arg0 + 20))) >> 4) + 1)) >= u(268435456)):
                                            break
                                        v6 = (v6 - v3)
                                        v7 = ((v6 - v3) >> 3)
                                        v6 = (268435455 if (u(v6) >= u(2147483632)) else (((v6 - v3) >> 3) if (u(v4) < u(v7)) else v4))
                                        if (268435455 if (u(v6) >= u(2147483632)) else (((v6 - v3) >> 3) if (u(v4) < u(v7)) else v4)):
                                            if (u(v6) >= u(268435456)):
                                                break
                                        else:
                                        v7 = 0
                                        v4 = (0 + (v12 << 4))
                                        store32((0 + (v12 << 4)) + 12, v8)
                                        store32(v4 + 8, v5)
                                        store32(v4 + 4, v9)
                                        store32(v4, v10)
                                        # TODO: memory.copy []
                                        store32(arg0 + 28, (v7 + (v6 << 4)))
                                        store32(arg0 + 24, (v4 + 16))
                                        store32(arg0 + 20, v7)
                                        if (v3 == 0):
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
                                    if (u(load32(arg0 + 24)) < u(load32(arg0 + 28))):
                                        store32(arg1 + 12, v7)
                                        store32(arg1 + 8, v5)
                                        store32(arg1 + 4, v8)
                                        store32(arg1, v6)
                                        break
                                    arg1 = load32((arg0 + 20))
                                    v9 = (arg1 - load32((arg0 + 20)))
                                    v10 = ((arg1 - load32((arg0 + 20))) >> 4)
                                    arg2 = (((arg1 - load32((arg0 + 20))) >> 4) + 1)
                                    if (u((((arg1 - load32((arg0 + 20))) >> 4) + 1)) >= u(268435456)):
                                        break
                                    v3 = (v3 - arg1)
                                    v4 = ((v3 - arg1) >> 3)
                                    v3 = (268435455 if (u(v3) >= u(2147483632)) else (((v3 - arg1) >> 3) if (u(arg2) < u(v4)) else arg2))
                                    if (268435455 if (u(v3) >= u(2147483632)) else (((v3 - arg1) >> 3) if (u(arg2) < u(v4)) else arg2)):
                                        if (u(v3) >= u(268435456)):
                                            break
                                    else:
                                    v4 = 0
                                    arg2 = (0 + (v10 << 4))
                                    store32((0 + (v10 << 4)) + 12, v7)
                                    store32(arg2 + 8, v5)
                                    store32(arg2 + 4, v8)
                                    store32(arg2, v6)
                                    # TODO: memory.copy []
                                    store32(arg0 + 28, (v4 + (v3 << 4)))
                                    store32(arg0 + 24, (arg2 + 16))
                                    store32(arg0 + 20, v4)
                                    if (arg1 == 0):
                                        break
                                    return af(arg1)
                                while True:  # block $label6
                                    v3 = load32(arg2 + 8)
                                    v8 = (v5 - load32(arg2 + 8))
                                    if ((v5 - load32(arg2 + 8)) <= 0):
                                        break
                                    v9 = (load32(arg1) + v3)
                                    v10 = load32(arg1 + 4)
                                    v3 = load32(arg0 + 24)
                                    v5 = load32(arg0 + 28)
                                    if (u(load32(arg0 + 24)) < u(load32(arg0 + 28))):
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
                                    if (u((((v3 - load32((arg0 + 20))) >> 4) + 1)) >= u(268435456)):
                                        break
                                    v5 = (v5 - v3)
                                    v7 = ((v5 - v3) >> 3)
                                    v5 = (268435455 if (u(v5) >= u(2147483632)) else (((v5 - v3) >> 3) if (u(v4) < u(v7)) else v4))
                                    if (268435455 if (u(v5) >= u(2147483632)) else (((v5 - v3) >> 3) if (u(v4) < u(v7)) else v4)):
                                        if (u(v5) >= u(268435456)):
                                            break
                                    else:
                                    v7 = 0
                                    v4 = (0 + (v12 << 4))
                                    store32((0 + (v12 << 4)) + 12, v6)
                                    store32(v4 + 8, v8)
                                    store32(v4 + 4, v10)
                                    store32(v4, v9)
                                    # TODO: memory.copy []
                                    store32(arg0 + 28, (v7 + (v5 << 4)))
                                    store32(arg0 + 24, (v4 + 16))
                                    store32(arg0 + 20, v7)
                                    if (v3 == 0):
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
                                if (u(load32(arg0 + 24)) < u(load32(arg0 + 28))):
                                    store32(arg1 + 12, v5)
                                    store32(arg1 + 8, v7)
                                    store32(arg1 + 4, v6)
                                    store32(arg1, v8)
                                    break
                                arg1 = load32((arg0 + 20))
                                v9 = (arg1 - load32((arg0 + 20)))
                                v10 = ((arg1 - load32((arg0 + 20))) >> 4)
                                arg2 = (((arg1 - load32((arg0 + 20))) >> 4) + 1)
                                if (u((((arg1 - load32((arg0 + 20))) >> 4) + 1)) >= u(268435456)):
                                    break
                                v3 = (v3 - arg1)
                                v4 = ((v3 - arg1) >> 3)
                                v3 = (268435455 if (u(v3) >= u(2147483632)) else (((v3 - arg1) >> 3) if (u(arg2) < u(v4)) else arg2))
                                if (268435455 if (u(v3) >= u(2147483632)) else (((v3 - arg1) >> 3) if (u(arg2) < u(v4)) else arg2)):
                                    if (u(v3) >= u(268435456)):
                                        break
                                else:
                                v4 = 0
                                arg2 = (0 + (v10 << 4))
                                store32((0 + (v10 << 4)) + 12, v5)
                                store32(arg2 + 8, v7)
                                store32(arg2 + 4, v6)
                                store32(arg2, v8)
                                # TODO: memory.copy []
                                store32(arg0 + 28, (v4 + (v3 << 4)))
                                store32(arg0 + 24, (arg2 + 16))
                                store32(arg0 + 20, v4)
                                if (arg1 == 0):
                                    break
                                break
                            return af(arg1)
                            break
                        func42()
                        raise RuntimeError('unreachable')
                        break
                    func68()
                    raise RuntimeError('unreachable')
                    break
                func42()
                raise RuntimeError('unreachable')
                break
            func42()
            raise RuntimeError('unreachable')
            break
        func42()
        raise RuntimeError('unreachable')
        break
    store32(arg0 + 24, (arg1 + 16))
    return v9

# ------------------------------------------------------------
# $func463
# ------------------------------------------------------------
def func463(arg0, arg1):
    v7 = load32(arg0 + 8)
    v5 = load8u(arg1 + 3)
    while True:  # block $label8
        while True:  # block $label1
            while True:  # block $label0
                v4 = load32(arg0 + 12)
                if (load32(arg0 + 12) >= 0):
                    break
                v6 = load32(arg0 + 16)
                if (load32(arg0 + 16) == 0):
                    break
                if (u(load32(arg0 + 24)) > u(v6)):
                    v3 = load64(v6)
                    store32(arg0 + 16, (v6 + 7))
                    store64(arg0, ((load64(arg0) << 56) | ((((((v3 << 56) | ((v3 & 65280) << 40)) | (((v3 & 16711680) << 24) | ((v3 & 4278190080) << 8))) | ((((v3 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v3 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v3 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                    v4 = (v4 + 56)
                    break
                func36(arg0)
                v4 = load32(arg0 + 12)
                break
            while True:  # block $label2
                v5 = (((v5 * v7) & 0xFFFFFFFF) >> 8)
                v3 = load64(arg0)
                v2 = i64(v4)
                v8 = i32(((load64(arg0) & 0xFFFFFFFFFFFFFFFF) >> i64(v4)))
                if (u((((v5 * v7) & 0xFFFFFFFF) >> 8)) < u(i32(((load64(arg0) & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                    v3 = (v3 - (i64((v5 + 1)) << v2))
                    store64(arg0, (v3 - (i64((v5 + 1)) << v2)))
                    break
                break
            v6 = (v5 + 1)
            v7 = (clz((v5 + 1)) ^ 24)
            v4 = ((v7 - v5) - (clz((v5 + 1)) ^ 24))
            store32(v4 + 12, ((v7 - v5) - (clz((v5 + 1)) ^ 24)))
            v6 = ((v6 << v7) - 1)
            store32(arg0 + 8, ((v6 << v7) - 1))
            while True:  # block $label5
                if (u(v5) >= u(v8)):
                    v7 = load8u(arg1 + 4)
                    while True:  # block $label3
                        if (v4 >= 0):
                            break
                        v5 = load32(arg0 + 16)
                        if (load32(arg0 + 16) == 0):
                            break
                        if (u(load32(arg0 + 24)) > u(v5)):
                            v2 = load64(v5)
                            store32(arg0 + 16, (v5 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # block $label4
                        v5 = (((v6 * v7) & 0xFFFFFFFF) >> 8)
                        v2 = i64(v4)
                        v7 = (u((((v6 * v7) & 0xFFFFFFFF) >> 8)) >= u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4)))))
                        if ((u((((v6 * v7) & 0xFFFFFFFF) >> 8)) >= u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))) == 0):
                            v3 = (v3 - (i64((v5 + 1)) << v2))
                            store64(arg0, (v3 - (i64((v5 + 1)) << v2)))
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
                    while True:  # block $label6
                        if (v4 >= 0):
                            break
                        arg1 = load32(arg0 + 16)
                        if (load32(arg0 + 16) == 0):
                            break
                        if (u(load32(arg0 + 24)) > u(arg1)):
                            v2 = load64(arg1)
                            store32(arg0 + 16, (arg1 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # block $label7
                        arg1 = (((v5 * v6) & 0xFFFFFFFF) >> 8)
                        v2 = i64(v4)
                        if (u((((v5 * v6) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                            store64(arg0, (v3 - (i64((arg1 + 1)) << v2)))
                            v5 = 4
                            break
                        v5 = 3
                        break
                    arg1 = (arg1 + 1)
                    v4 = (clz((arg1 + 1)) ^ 24)
                    store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                    break
                v7 = load8u(arg1 + 6)
                while True:  # block $label9
                    if (v4 >= 0):
                        break
                    v5 = load32(arg0 + 16)
                    if (load32(arg0 + 16) == 0):
                        break
                    if (u(load32(arg0 + 24)) > u(v5)):
                        v2 = load64(v5)
                        store32(arg0 + 16, (v5 + 7))
                        v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                        store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                        v4 = (v4 + 56)
                        break
                    func36(arg0)
                    v3 = load64(arg0)
                    v4 = load32(arg0 + 12)
                    break
                while True:  # block $label10
                    v5 = (((v6 * v7) & 0xFFFFFFFF) >> 8)
                    v2 = i64(v4)
                    v7 = i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4)))
                    if (u((((v6 * v7) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                        v3 = (v3 - (i64((v5 + 1)) << v2))
                        store64(arg0, (v3 - (i64((v5 + 1)) << v2)))
                        break
                    break
                v6 = (v5 + 1)
                v8 = (clz((v5 + 1)) ^ 24)
                v4 = ((v6 - v5) - (clz((v5 + 1)) ^ 24))
                store32(v4 + 12, ((v6 - v5) - (clz((v5 + 1)) ^ 24)))
                v6 = ((v6 << v8) - 1)
                store32(arg0 + 8, ((v6 << v8) - 1))
                if (u(v5) >= u(v7)):
                    v5 = load8u(arg1 + 7)
                    while True:  # block $label11
                        if (v4 >= 0):
                            break
                        arg1 = load32(arg0 + 16)
                        if (load32(arg0 + 16) == 0):
                            break
                        if (u(load32(arg0 + 24)) > u(arg1)):
                            v2 = load64(arg1)
                            store32(arg0 + 16, (arg1 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # block $label12
                        arg1 = (((v5 * v6) & 0xFFFFFFFF) >> 8)
                        v2 = i64(v4)
                        v7 = i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4)))
                        if (u((((v5 * v6) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                            v3 = (v3 - (i64((arg1 + 1)) << v2))
                            store64(arg0, (v3 - (i64((arg1 + 1)) << v2)))
                            break
                        break
                    v5 = (arg1 + 1)
                    v6 = (clz((arg1 + 1)) ^ 24)
                    v4 = ((v6 - arg1) - (clz((arg1 + 1)) ^ 24))
                    store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                    v6 = ((v5 << v6) - 1)
                    store32(arg0 + 8, ((v5 << v6) - 1))
                    if (u(arg1) >= u(v7)):
                        while True:  # block $label13
                            if (v4 >= 0):
                                break
                            arg1 = load32(arg0 + 16)
                            if (load32(arg0 + 16) == 0):
                                break
                            if (u(load32(arg0 + 24)) > u(arg1)):
                                v2 = load64(arg1)
                                store32(arg0 + 16, (arg1 + 7))
                                v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                v4 = (v4 + 56)
                                break
                            func36(arg0)
                            v3 = load64(arg0)
                            v4 = load32(arg0 + 12)
                            break
                        while True:  # block $label14
                            arg1 = (((v6 * 159) & 0xFFFFFFFF) >> 8)
                            v2 = i64(v4)
                            if (u((((v6 * 159) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                                store64(arg0, (v3 - (i64((arg1 + 1)) << v2)))
                                v5 = 6
                                break
                            v5 = 5
                            break
                        arg1 = (arg1 + 1)
                        v4 = (clz((arg1 + 1)) ^ 24)
                        store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                        break
                    while True:  # block $label15
                        if (v4 >= 0):
                            break
                        arg1 = load32(arg0 + 16)
                        if (load32(arg0 + 16) == 0):
                            break
                        if (u(load32(arg0 + 24)) > u(arg1)):
                            v2 = load64(arg1)
                            store32(arg0 + 16, (arg1 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # block $label16
                        arg1 = (((v6 * 165) & 0xFFFFFFFF) >> 8)
                        v2 = i64(v4)
                        if (u((((v6 * 165) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                            v3 = (v3 - (i64((arg1 + 1)) << v2))
                            store64(arg0, (v3 - (i64((arg1 + 1)) << v2)))
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
                    while True:  # block $label17
                        if (v4 >= 0):
                            break
                        arg1 = load32(arg0 + 16)
                        if (load32(arg0 + 16) == 0):
                            break
                        if (u(load32(arg0 + 24)) > u(arg1)):
                            v2 = load64(arg1)
                            store32(arg0 + 16, (arg1 + 7))
                            v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                            store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                            v4 = (v4 + 56)
                            break
                        func36(arg0)
                        v3 = load64(arg0)
                        v4 = load32(arg0 + 12)
                        break
                    while True:  # block $label18
                        arg1 = (((v5 * 145) & 0xFFFFFFFF) >> 8)
                        v2 = i64(v4)
                        v7 = i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4)))
                        if (u((((v5 * 145) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                            store64(arg0, (v3 - (i64((arg1 + 1)) << v2)))
                            break
                        break
                    v5 = (arg1 + 1)
                    v4 = (clz((arg1 + 1)) ^ 24)
                    store32(v4 + 12, ((v5 - arg1) - (clz((arg1 + 1)) ^ 24)))
                    store32(arg0 + 8, ((v5 << v4) - 1))
                    return (v6 + (u(arg1) < u(v7)))
                v7 = load8u(arg1 + 8)
                while True:  # block $label19
                    if (v4 >= 0):
                        break
                    v5 = load32(arg0 + 16)
                    if (load32(arg0 + 16) == 0):
                        break
                    if (u(load32(arg0 + 24)) > u(v5)):
                        v2 = load64(v5)
                        store32(arg0 + 16, (v5 + 7))
                        v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                        store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                        v4 = (v4 + 56)
                        break
                    func36(arg0)
                    v3 = load64(arg0)
                    v4 = load32(arg0 + 12)
                    break
                while True:  # block $label20
                    v5 = (((v6 * v7) & 0xFFFFFFFF) >> 8)
                    v2 = i64(v4)
                    v8 = i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4)))
                    if (u((((v6 * v7) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                        v3 = (v3 - (i64((v5 + 1)) << v2))
                        store64(arg0, (v3 - (i64((v5 + 1)) << v2)))
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
                while True:  # block $label21
                    if (v4 >= 0):
                        break
                    arg1 = load32(arg0 + 16)
                    if (load32(arg0 + 16) == 0):
                        break
                    if (u(load32(arg0 + 24)) > u(arg1)):
                        v2 = load64(arg1)
                        store32(arg0 + 16, (arg1 + 7))
                        v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                        store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                        v4 = (v4 + 56)
                        break
                    func36(arg0)
                    v3 = load64(arg0)
                    v4 = load32(arg0 + 12)
                    break
                while True:  # block $label22
                    arg1 = (((v6 * v7) & 0xFFFFFFFF) >> 8)
                    v2 = i64(v4)
                    v7 = i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4)))
                    if (u((((v6 * v7) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                        v3 = (v3 - (i64((arg1 + 1)) << v2))
                        store64(arg0, (v3 - (i64((arg1 + 1)) << v2)))
                        break
                    break
                v6 = (arg1 + 1)
                v9 = (clz((arg1 + 1)) ^ 24)
                v4 = ((v6 - arg1) - (clz((arg1 + 1)) ^ 24))
                store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                v6 = ((v6 << v9) - 1)
                store32(arg0 + 8, ((v6 << v9) - 1))
                while True:  # block $label23
                    v9 = (((u(v5) < u(v8)) << 1) | (u(arg1) < u(v7)))
                    v5 = load32((((((u(v5) < u(v8)) << 1) | (u(arg1) < u(v7))) << 2) + 13984))
                    arg1 = load8u(load32((((((u(v5) < u(v8)) << 1) | (u(arg1) < u(v7))) << 2) + 13984)))
                    if (load8u(load32((((((u(v5) < u(v8)) << 1) | (u(arg1) < u(v7))) << 2) + 13984))) == 0):
                        v7 = 0
                        break
                    v7 = 0
                    while True:  # $label26
                        while True:  # block $label24
                            if (v4 >= 0):
                                break
                            v8 = load32(arg0 + 16)
                            if (load32(arg0 + 16) == 0):
                                break
                            if (u(load32(arg0 + 24)) > u(v8)):
                                v2 = load64(v8)
                                store32(arg0 + 16, (v8 + 7))
                                v3 = ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                                store64(arg0, ((v3 << 56) | ((((((v2 << 56) | ((v2 & 65280) << 40)) | (((v2 & 16711680) << 24) | ((v2 & 4278190080) << 8))) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v2 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v2 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                                v4 = (v4 + 56)
                                break
                            func36(arg0)
                            v3 = load64(arg0)
                            v4 = load32(arg0 + 12)
                            break
                        while True:  # block $label25
                            arg1 = (((v6 * (arg1 & 255)) & 0xFFFFFFFF) >> 8)
                            v2 = i64(v4)
                            v8 = i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4)))
                            if (u((((v6 * (arg1 & 255)) & 0xFFFFFFFF) >> 8)) < u(i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> i64(v4))))):
                                v3 = (v3 - (i64((arg1 + 1)) << v2))
                                store64(arg0, (v3 - (i64((arg1 + 1)) << v2)))
                                break
                            break
                        v6 = (arg1 + 1)
                        v10 = (clz((arg1 + 1)) ^ 24)
                        v4 = ((v6 - arg1) - (clz((arg1 + 1)) ^ 24))
                        store32(v4 + 12, ((v6 - arg1) - (clz((arg1 + 1)) ^ 24)))
                        v6 = ((v6 << v10) - 1)
                        store32(arg0 + 8, ((v6 << v10) - 1))
                        v7 = ((v7 << 1) | (u(arg1) < u(v8)))
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
        raise RuntimeError('unreachable')
        break
    store32(arg0 + 8, ((arg1 << v4) - 1))
    return v5

# ------------------------------------------------------------
# $func464
# ------------------------------------------------------------
def func464(arg0):
    v11 = load32(arg0)
    v16 = load32(arg0 + 12)
    v12 = load32(arg0 + 4)
    v8 = load32(arg0 + 8)
    v6 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # block $label6
        while True:  # block $label7
            if (load8u(9142916) == 0):
                if v11:
                    while True:  # $label0
                        v3 = load32((v16 + (v2 << 2)))
                        v5 = ((load32(load32((v16 + (v2 << 2)))) * (load32(v3 + 4) + 2)) << 2)
                        v4 = (((load32(load32((v16 + (v2 << 2)))) * (load32(v3 + 4) + 2)) << 2) + v4)
                        if load32(v3 + 56):
                            v3 = (v4 + v5)
                            v1 = (((v4 + v5) - v8) if (u(v3) > u((v1 + v8))) else v1)
                        v2 = (v2 + 1)
                        if ((v2 + 1) != v11):
                            continue
                        break
                v13 = (load32(9684256) & 511)
                store32(9684256, ((load32(9684256) & 511) + 1))
                v7 = func26((v1 + v8))
                store32(((v13 << 2) + 9682208), func26((v1 + v8)))
                if v11:
                    while True:  # $label5
                        v3 = load32((v16 + (v14 << 2)))
                        v15 = load32(load32((v16 + (v14 << 2))) + 4)
                        v4 = load32(v3)
                        v9 = (load32(load32((v16 + (v14 << 2))) + 4) * load32(v3))
                        v17 = load32(v3 + 36)
                        v5 = (v4 << 2)
                        v18 = load32(v3 + 40)
                        v1 = 1
                        while True:  # block $label1
                            if ((u(v15) < u(16384)) & (u(v4) <= u(16383))):
                                break
                            while True:  # $label3
                                while True:  # block $label2
                                    # TODO: i32.div_u []
                                    v4 = v1
                                    if (v9 - (v1 * v1)):
                                        break
                                    if (u(v4) >= u(16384)):
                                        break
                                    v4 = v1
                                    break
                                    break
                                v4 = 16384
                                v2 = (v1 + 1)
                                if ((v1 + 1) == 16384):
                                    break
                                # TODO: i32.div_u []
                                v19 = v2
                                if (v9 == (v2 * v2)):
                                    v4 = v2
                                    if (u(v19) < u(16384)):
                                        break
                                v1 = (v1 + 2)
                                continue
                                break
                            raise RuntimeError('unreachable')
                            break
                        if v5:
                            # TODO: memory.fill []
                        v2 = (v5 + v10)
                        v9 = ((v15 + 2) * v5)
                        v1 = 0
                        if v5:
                            while True:  # $label4
                                store8((v7 + ((v1 + v2) + ((load32(v3) * load32(v3 + 4)) << 2))), 0)
                                store8((v7 + ((v2 + (v1 | 1)) + ((load32(v3) * load32(v3 + 4)) << 2))), 0)
                                v1 = (v1 + 2)
                                if ((v1 + 2) != v5):
                                    continue
                                break
                        v10 = (v9 + v10)
                        v14 = (v14 + 1)
                        if ((v14 + 1) != v11):
                            continue
                        break
                store32(v6 + 12, v13)
                store32(v6 + 8, v7)
                store32(v6 + 4, v12)
                store32(v6, v8)
                if v12:
                    break
                break
            while True:  # block $label8
                v15 = load32(9684260)
                if load32(9684260):
                    break
                if (load8u(9142918) == 0):
                    break
                break
            if v11:
                while True:  # $label18
                    v3 = load32((v16 + (v14 << 2)))
                    v4 = load32(load32((v16 + (v14 << 2))) + 4)
                    v1 = load32(v3)
                    v7 = (load32(load32((v16 + (v14 << 2))) + 4) * load32(v3))
                    v10 = (v3 + load32(v3 + 36))
                    v2 = 1
                    while True:  # block $label9
                        if ((u(v4) < u(16384)) & (u(v1) <= u(16383))):
                            break
                        while True:  # $label11
                            while True:  # block $label10
                                # TODO: i32.div_u []
                                v1 = v2
                                if (v7 - (v2 * v2)):
                                    break
                                if (u(v1) >= u(16384)):
                                    break
                                v1 = v2
                                break
                                break
                            v1 = 16384
                            v4 = (v2 + 1)
                            if ((v2 + 1) == 16384):
                                break
                            # TODO: i32.div_u []
                            v5 = v4
                            if (v7 == (v4 * v4)):
                                v1 = v4
                                if (u(v5) < u(16384)):
                                    break
                            v2 = (v2 + 2)
                            continue
                            break
                        raise RuntimeError('unreachable')
                        break
                    v13 = (load32(9684256) & 511)
                    store32(9684256, ((load32(9684256) & 511) + 1))
                    v9 = (v7 << 2)
                    v5 = func26((v7 << 2))
                    store32(((v13 << 2) + 9682208), func26((v7 << 2)))
                    while True:  # block $label16
                        while True:  # block $label14
                            while True:  # block $label13
                                while True:  # block $label12
                                    v10 = load32(v3 + 32)
                                    # br_table[(load32(v3 + 32) - 23)]
                                    break
                                    break
                                v8 = 0
                                v4 = 0
                                v12 = 0
                                v1 = 0
                                v2 = 0
                                if (v7 == 0):
                                    break
                                while True:  # $label15
                                    if load8u((v5 + (v2 | 3))):
                                        v8 = (v8 + load8u((v2 + v5)))
                                        v12 = (v12 + load8u((v5 + (v2 | 2))))
                                        v4 = (v4 + load8u((v5 + (v2 | 1))))
                                        v1 = (v1 + 1)
                                    v2 = (v2 + 4)
                                    if (u(v9) > u((v2 + 4))):
                                        continue
                                    break
                                break
                                break
                            v8 = 0
                            if (v10 != 27):
                                break
                            if (load8u(9142916) == 0):
                                break
                            v2 = 0
                            if (v7 == 0):
                                break
                            while True:  # $label17
                                # TODO: i32.div_u []
                                store8((load8u((v5 + (v2 | 2))) + (load8u((v5 + (v2 | 1))) + load8u((v2 + v5)))), 3)
                                v2 = (v2 + 4)
                                if (u((v2 + 4)) < u(v9)):
                                    continue
                                break
                            v10 = load32(v3 + 32)
                            break
                            break
                        # TODO: i32.div_u []
                        # TODO: i32.div_u []
                        # TODO: i32.div_u []
                        v8 = (v12 + (v1 << 16))
                        break
                    v1 = load32((v3 + (48 if load8u(9142918) else 56)))
                    v4 = load32(v3 + 16)
                    v20 = load64(v3)
                    v2 = load32(v3 + 28)
                    v21 = load64(v3 + 8)
                    store64(v6 + 32, load64(v3 + 20))
                    store64(v6 + 40, v21)
                    store32(v6 + 48, v10)
                    store32(v6 + 52, v8)
                    store32(v6 + 56, v1)
                    store32(v6 + 60, v2)
                    store32((v6 - -64), v13)
                    store32(v6 + 16, v5)
                    store64(v6 + 20, v20)
                    store32(v6 + 28, v4)
                    a_b()
                    store32(9684260, (load32(9684260) + v9))
                    v14 = (v14 + 1)
                    if ((v14 + 1) != v11):
                        continue
                    break
            if v15:
                break
            break
        a_b()
        break
    G.global0 = (v6 + 80)
    v1 = load32(arg0 + 12)
    if load32(arg0 + 12):
    hf(af(v1), af(arg0), 0)
    a_l()
    raise RuntimeError('unreachable')
    return 0

# ------------------------------------------------------------
# $func465
# ------------------------------------------------------------
def func465(arg0, arg1, param2):
    v29 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v22 = load32(arg0 + 2324)
    v37 = load32(arg0 + 172)
    v5 = load8u((load32(arg0 + 2352) + 10321))
    v10 = load32(arg0 + 2312)
    v26 = load32(arg0 + 2328)
    v12 = load32(arg0 + 2320)
    v13 = load32(arg0 + 2316)
    v16 = load32(arg0 + 320)
    v33 = load32(arg0 + 176)
    if (load32(arg0 + 160) == 2):
        func273(0, 0, 0, 0, arg0, (arg0 + 172))
    while True:  # block $label98
        while True:  # block $label95
            while True:  # block $label96
                while True:  # block $label2
                    while True:  # block $label0
                        if (load32(arg0 + 180) == 0):
                            break
                        v15 = load32(arg0 + 308)
                        if (load32(arg0 + 308) >= load32(arg0 + 316)):
                            break
                        v27 = load32(arg0 + 176)
                        while True:  # $label3
                            while True:  # block $label1
                                v8 = (load32(arg0 + 184) + (v15 << 2))
                                v4 = load8u((load32(arg0 + 184) + (v15 << 2)))
                                if (load8u((load32(arg0 + 184) + (v15 << 2))) == 0):
                                    break
                                if (u(v4) <= u(2)):
                                    break
                                v6 = load32(arg0 + 172)
                                v2 = load32(arg0 + 2324)
                                v3 = ((load32(arg0 + 2312) + ((load32(arg0 + 172) * load32(arg0 + 2324)) << 4)) + (v15 << 4))
                                if (load32(arg0 + 2352) == 1):
                                    if (v15 > 0):
                                        # call_indirect[load32(9687508)]
                                    if load8u(v8 + 2):
                                        # call_indirect[load32(9687516)]
                                    if (v27 > 0):
                                        # call_indirect[load32(9687504)]
                                    if (load8u(v8 + 2) == 0):
                                        break
                                    # call_indirect[load32(9687512)]
                                    break
                                v7 = load8u(v8 + 1)
                                v11 = (v15 << 3)
                                v14 = load32(arg0 + 2328)
                                v6 = ((v6 * load32(arg0 + 2328)) << 3)
                                v9 = ((v15 << 3) + (((v6 * load32(arg0 + 2328)) << 3) + load32(arg0 + 2320)))
                                v11 = ((load32(arg0 + 2316) + v6) + v11)
                                v6 = load8u(v8 + 3)
                                if (v15 > 0):
                                    v17 = (v4 + 4)
                                    # call_indirect[load32(9687476)]
                                    # call_indirect[load32(9687484)]
                                if load8u(v8 + 2):
                                    # call_indirect[load32(9687492)]
                                    # call_indirect[load32(9687500)]
                                if (v27 > 0):
                                    v17 = (v4 + 4)
                                    # call_indirect[load32(9687472)]
                                    # call_indirect[load32(9687480)]
                                if (load8u(v8 + 2) == 0):
                                    break
                                # call_indirect[load32(9687488)]
                                # call_indirect[load32(9687496)]
                                break
                            v15 = (v15 + 1)
                            if ((v15 + 1) < load32(arg0 + 316)):
                                continue
                            break
                        break
                    v8 = ((v22 * v37) << 4)
                    v38 = (v5 * v22)
                    v11 = (v10 - (v5 * v22))
                    v3 = ((v26 * v37) << 3)
                    v34 = (((v5 & 0xFFFFFFFF) >> 1) * v26)
                    v26 = (v12 - (((v5 & 0xFFFFFFFF) >> 1) * v26))
                    v27 = (v13 - v34)
                    while True:  # block $label4
                        if (load32(arg0 + 584) == 0):
                            break
                        v7 = load32(arg0 + 308)
                        v2 = load32(arg0 + 316)
                        if (load32(arg0 + 308) >= load32(arg0 + 316)):
                            break
                        v6 = (arg0 + 596)
                        while True:  # $label7
                            v22 = (load32(arg0 + 188) + (v7 * 800))
                            v10 = load8u((load32(arg0 + 188) + (v7 * 800)) + 796)
                            if (u(load8u((load32(arg0 + 188) + (v7 * 800)) + 796)) >= u(4)):
                                v14 = load32(arg0 + 2328)
                                v9 = ((load32(arg0 + 2328) * load32(arg0 + 172)) << 3)
                                v12 = load32(arg0 + 2320)
                                v13 = load32(arg0 + 2316)
                                v4 = load32(arg0 + 592)
                                v15 = load32(arg0 + 588)
                                v2 = 0
                                while True:  # $label5
                                    v15 = (v6 + (v15 << 2))
                                    v17 = (load32(v15) - load32((v6 + (v4 << 2))))
                                    store32((v6 + (v15 << 2)), ((load32(v15) - load32((v6 + (v4 << 2)))) & 2147483647))
                                    v4 = (load32(arg0 + 588) + 1)
                                    v15 = ((load32(arg0 + 588) + 1) if (v4 != 55) else 0)
                                    store32(arg0 + 588, ((load32(arg0 + 588) + 1) if (v4 != 55) else 0))
                                    v4 = (load32(arg0 + 592) + 1)
                                    v4 = ((load32(arg0 + 592) + 1) if (v4 != 55) else 0)
                                    store32(arg0 + 592, ((load32(arg0 + 592) + 1) if (v4 != 55) else 0))
                                    store8((v2 + v29), ((((((v17 << 1) >> 24) * v10) & 0xFFFFFFFF) >> 8) ^ 128))
                                    v2 = (v2 + 1)
                                    if ((v2 + 1) != 64):
                                        continue
                                    break
                                v2 = 0
                                v10 = (v7 << 3)
                                # call_indirect[load32(9687520)]
                                v22 = load8u(v22 + 796)
                                v4 = load32(arg0 + 592)
                                v15 = load32(arg0 + 588)
                                while True:  # $label6
                                    v15 = (v6 + (v15 << 2))
                                    v13 = (load32(v15) - load32((v6 + (v4 << 2))))
                                    store32((v6 + (v15 << 2)), ((load32(v15) - load32((v6 + (v4 << 2)))) & 2147483647))
                                    v4 = (load32(arg0 + 588) + 1)
                                    v15 = ((load32(arg0 + 588) + 1) if (v4 != 55) else 0)
                                    store32(arg0 + 588, ((load32(arg0 + 588) + 1) if (v4 != 55) else 0))
                                    v4 = (load32(arg0 + 592) + 1)
                                    v4 = ((load32(arg0 + 592) + 1) if (v4 != 55) else 0)
                                    store32(arg0 + 592, ((load32(arg0 + 592) + 1) if (v4 != 55) else 0))
                                    store8((v2 + v29), ((((((v13 << 1) >> 24) * v22) & 0xFFFFFFFF) >> 8) ^ 128))
                                    v2 = (v2 + 1)
                                    if ((v2 + 1) != 64):
                                        continue
                                    break
                                # call_indirect[load32(9687520)]
                                v2 = load32(arg0 + 316)
                            v7 = (v7 + 1)
                            if ((v7 + 1) < v2):
                                continue
                            break
                        break
                    v22 = (v8 + v11)
                    v26 = (v3 + v26)
                    v27 = (v3 + v27)
                    v39 = (v16 - 1)
                    while True:  # block $label8
                        if (load32(arg1 + 44) == 0):
                            break
                        v7 = (v33 << 4)
                        v6 = ((v33 << 4) + 16)
                        while True:  # block $label9
                            if v33:
                                v4 = v22
                                v3 = v27
                                v2 = v26
                                break
                            v2 = (load32(arg0 + 2320) + v3)
                            v3 = (load32(arg0 + 2316) + v3)
                            v4 = (load32(arg0 + 2312) + v8)
                            break
                        v15 = 0
                        store32(arg1 + 28, v2)
                        store32(arg1 + 24, v3)
                        store32(arg1 + 20, v4)
                        v4 = 0
                        store32(arg1 + 104, 0)
                        v2 = (v6 - (v5 if (v33 < v39) else 0))
                        v3 = load32(arg1 + 88)
                        v35 = ((v6 - (v5 if (v33 < v39) else 0)) if (v2 < v3) else load32(arg1 + 88))
                        while True:  # block $label10
                            if (load32(arg0 + 2392) == 0):
                                break
                            if (v15 >= v35):
                                break
                            while True:  # block $label13
                                v4 = (v35 - v15)
                                v2 = 0
                                v17 = 0
                                while True:  # block $label16
                                    while True:  # block $label41
                                        while True:  # block $label37
                                            while True:  # block $label36
                                                while True:  # block $label35
                                                    while True:  # block $label18
                                                        while True:  # block $label17
                                                            while True:  # block $label14
                                                                if arg0:
                                                                    while True:  # block $label11
                                                                        if (v15 < 0):
                                                                            break
                                                                        if (v4 <= 0):
                                                                            break
                                                                        v14 = (v4 + v15)
                                                                        v6 = load32(arg1 + 88)
                                                                        if ((v4 + v15) > load32(arg1 + 88)):
                                                                            break
                                                                        v30 = load32(arg1)
                                                                        while True:  # block $label12
                                                                            if load32(arg0 + 2400):
                                                                                break
                                                                            v3 = load32(arg0 + 2388)
                                                                            if (load32(arg0 + 2388) == 0):
                                                                                v2 = func134(1, 144)
                                                                                store32(arg0 + 2388, func134(1, 144))
                                                                                if (v2 == 0):
                                                                                    break
                                                                                if load32(arg0 + 2404):
                                                                                    break
                                                                                v3 = func58((load32s(arg1 + 88) * load32s(arg1)), 1)
                                                                                store32(arg0 + 2404, func58((load32s(arg1 + 88) * load32s(arg1)), 1))
                                                                                while True:  # block $label15
                                                                                    if v3:
                                                                                        store32(arg0 + 2412, 0)
                                                                                        store32(arg0 + 2408, v3)
                                                                                        break
                                                                                    if (func99(arg0, 1, 8400) == 0):
                                                                                        break
                                                                                    v3 = load32(arg0 + 2408)
                                                                                    break
                                                                                v7 = load32(arg0 + 2392)
                                                                                if (load32(arg0 + 2392) == 0):
                                                                                    break
                                                                                if (v3 == 0):
                                                                                    break
                                                                                v2 = load32(arg0 + 2388)
                                                                                v8 = load32(arg0 + 2396)
                                                                                v5 = load32(52304)
                                                                                if (load32(52304) != load32(52312)):
                                                                                    store32(9687564, 337)
                                                                                    store32(9687560, 338)
                                                                                    store32(9687556, 339)
                                                                                    store32(9687552, 340)
                                                                                    store32(9687548, 341)
                                                                                    store32(9687544, 342)
                                                                                    store32(9687540, 343)
                                                                                    store32(52312, v5)
                                                                                    store32(9687536, 0)
                                                                                store32(v2 + 136, v3)
                                                                                v3 = load32(arg1)
                                                                                store32(v2, load32(arg1))
                                                                                v5 = load32(arg1 + 4)
                                                                                store32(v2 + 4, load32(arg1 + 4))
                                                                                if (v3 <= 0):
                                                                                    break
                                                                                if (v5 <= 0):
                                                                                    break
                                                                                while True:  # block $label33
                                                                                    while True:  # block $label19
                                                                                        if (u(v8) < u(2)):
                                                                                            break
                                                                                        v3 = (load8u(v7) & 3)
                                                                                        store32(v2 + 8, (load8u(v7) & 3))
                                                                                        store32(v2 + 12, (((load8u(v7) & 0xFFFFFFFF) >> 2) & 3))
                                                                                        v5 = (((load8u(v7) & 0xFFFFFFFF) >> 4) & 3)
                                                                                        store32(v2 + 16, (((load8u(v7) & 0xFFFFFFFF) >> 4) & 3))
                                                                                        if (u(v3) > u(1)):
                                                                                            break
                                                                                        if (u(v5) > u(1)):
                                                                                            break
                                                                                        if (u(load8u(v7)) > u(63)):
                                                                                            break
                                                                                        v3 = (v2 + 24)
                                                                                        if (v2 + 24):
                                                                                            # TODO: memory.fill []
                                                                                        v8 = (v8 - 1)
                                                                                        store32(v3 + 52, 262)
                                                                                        store32(v3 + 48, 263)
                                                                                        store32(v3 + 44, 264)
                                                                                        store32(v3 + 40, 0)
                                                                                        store32((v2 - -64), v2)
                                                                                        store32(v2 + 24, load32(arg1))
                                                                                        store32(v2 + 28, load32(arg1 + 4))
                                                                                        store32(v2 + 96, load32(arg1 + 72))
                                                                                        store32(v2 + 100, load32(arg1 + 76))
                                                                                        store32(v2 + 104, load32(arg1 + 80))
                                                                                        store32(v2 + 108, load32(arg1 + 84))
                                                                                        store32(v2 + 112, load32(arg1 + 88))
                                                                                        while True:  # block $label23
                                                                                            while True:  # block $label21
                                                                                                while True:  # block $label22
                                                                                                    while True:  # block $label20
                                                                                                        # br_table[load32(v2 + 8)]
                                                                                                        break
                                                                                                        break
                                                                                                    break
                                                                                                    break
                                                                                                a_c()
                                                                                                raise RuntimeError('unreachable')
                                                                                                break
                                                                                            while True:  # block $label24
                                                                                                v3 = func134(1, 288)
                                                                                                if (func134(1, 288) == 0):
                                                                                                    break
                                                                                                v5 = (v7 + 1)
                                                                                                store64(v3, 8589934592)
                                                                                                func453()
                                                                                                while True:  # block $label29
                                                                                                    if v2:
                                                                                                        v14 = load32(v2)
                                                                                                        store32(v3 + 100, load32(v2))
                                                                                                        v7 = load32(v2 + 4)
                                                                                                        store32(v3 + 8, (v2 + 24))
                                                                                                        store32(v3 + 104, v7)
                                                                                                        store32(v2 + 28, v7)
                                                                                                        store32(v2 + 24, v14)
                                                                                                        store32((v2 - -64), v2)
                                                                                                        store32(v3, 0)
                                                                                                        while True:  # block $label25
                                                                                                            if (func153(load32(v2), load32(v2 + 4), 1, v3, 0) == 0):
                                                                                                                break
                                                                                                            while True:  # block $label31
                                                                                                                while True:  # block $label32
                                                                                                                    while True:  # block $label30
                                                                                                                        while True:  # block $label27
                                                                                                                            while True:  # block $label26
                                                                                                                                if (load32(v3 + 192) != 1):
                                                                                                                                    break
                                                                                                                                if (load32(v3 + 196) != 3):
                                                                                                                                    break
                                                                                                                                if (load32(v3 + 120) > 0):
                                                                                                                                    break
                                                                                                                                v5 = load32(v3 + 164)
                                                                                                                                if (load32(v3 + 164) <= 0):
                                                                                                                                    break
                                                                                                                                v14 = load32(v3 + 168)
                                                                                                                                v7 = 0
                                                                                                                                while True:  # $label28
                                                                                                                                    v8 = (v14 + (v7 * 548))
                                                                                                                                    if load8u(load32((v14 + (v7 * 548)) + 4)):
                                                                                                                                        break
                                                                                                                                    if load8u(load32(v8 + 8)):
                                                                                                                                        break
                                                                                                                                    if load8u(load32(v8 + 12)):
                                                                                                                                        break
                                                                                                                                    v7 = (v7 + 1)
                                                                                                                                    if (v5 != (v7 + 1)):
                                                                                                                                        continue
                                                                                                                                    break
                                                                                                                                break
                                                                                                                                break
                                                                                                                            store32(v2 + 132, 0)
                                                                                                                            v8 = load32(v3 + 100)
                                                                                                                            v7 = load32(v2)
                                                                                                                            if (load32(v3 + 100) > load32(v2)):
                                                                                                                                break
                                                                                                                            v51 = (load32s(v3 + 104) * i64(v8))
                                                                                                                            v8 = (v7 & 65535)
                                                                                                                            v7 = func58(((load32s(v3 + 104) * i64(v8)) + (i64((v7 & 65535)) + (i64(v7) << 4))), 4)
                                                                                                                            store32(v3 + 16, func58(((load32s(v3 + 104) * i64(v8)) + (i64((v7 & 65535)) + (i64(v7) << 4))), 4))
                                                                                                                            if v7:
                                                                                                                                break
                                                                                                                            store32(v3 + 20, 0)
                                                                                                                            # br_table[load32(v3)]
                                                                                                                            break
                                                                                                                            break
                                                                                                                        store32(v2 + 132, 1)
                                                                                                                        store32(v3 + 20, 0)
                                                                                                                        v7 = func58((load32s(v3 + 104) * load32s(v3 + 100)), 1)
                                                                                                                        store32(v3 + 16, func58((load32s(v3 + 104) * load32s(v3 + 100)), 1))
                                                                                                                        if v7:
                                                                                                                            break
                                                                                                                        # br_table[load32(v3)]
                                                                                                                        break
                                                                                                                        break
                                                                                                                    store32(v3 + 20, ((v7 + (i32(v51) << 2)) + (v8 << 2)))
                                                                                                                    break
                                                                                                                store32(v2 + 20, v3)
                                                                                                                break
                                                                                                                break
                                                                                                            store32(v3, 1)
                                                                                                            break
                                                                                                        func191(v3)
                                                                                                        break
                                                                                                    a_c()
                                                                                                    raise RuntimeError('unreachable')
                                                                                                    break
                                                                                                a_c()
                                                                                                raise RuntimeError('unreachable')
                                                                                                break
                                                                                            break
                                                                                        if 5601:
                                                                                            break
                                                                                        break
                                                                                    v4 = load32(load32(arg0 + 2388) + 20)
                                                                                    if load32(load32(arg0 + 2388) + 20):
                                                                                    else:
                                                                                    break
                                                                                    break
                                                                                while True:  # block $label34
                                                                                    v3 = load32(arg0 + 2388)
                                                                                    if (load32(load32(arg0 + 2388) + 16) != 1):
                                                                                        store32(arg0 + 2416, 0)
                                                                                        break
                                                                                    v4 = (v6 - v15)
                                                                                    break
                                                                                v14 = (v4 + v15)
                                                                            if (v6 < v14):
                                                                                break
                                                                            v31 = load32(v3 + 112)
                                                                            while True:  # block $label40
                                                                                if (load32(v3 + 8) == 0):
                                                                                    v2 = load32(arg0 + 2392)
                                                                                    v6 = load32(v3)
                                                                                    v7 = (load32(v3) * v15)
                                                                                    v8 = ((load32(arg0 + 2392) + (load32(v3) * v15)) + 1)
                                                                                    if (u(((load32(arg0 + 2392) + (load32(v3) * v15)) + 1)) > u((v2 + load32(arg0 + 2396)))):
                                                                                        break
                                                                                    if (load32(((load32(v3 + 12) << 2) + 9687552)) == 0):
                                                                                        break
                                                                                    v2 = load32(arg0 + 2412)
                                                                                    while True:  # block $label38
                                                                                        if (v4 <= 0):
                                                                                            break
                                                                                        v5 = (v4 & 1)
                                                                                        v7 = (load32(arg0 + 2408) + v7)
                                                                                        if (v4 != 1):
                                                                                            v9 = (v4 & -2)
                                                                                            v4 = 0
                                                                                            while True:  # $label39
                                                                                                # call_indirect[load32(((load32(v3 + 12) << 2) + 9687552))]
                                                                                                v8 = (v6 + v8)
                                                                                                v2 = (v6 + v7)
                                                                                                # call_indirect[load32(((load32(v3 + 12) << 2) + 9687552))]
                                                                                                v8 = (v6 + v8)
                                                                                                v7 = (v2 + v6)
                                                                                                v4 = (v4 + 2)
                                                                                                if ((v4 + 2) != v9):
                                                                                                    continue
                                                                                                break
                                                                                        if (v5 == 0):
                                                                                            break
                                                                                        # call_indirect[load32(((load32(v3 + 12) << 2) + 9687552))]
                                                                                        v2 = v7
                                                                                        break
                                                                                    store32(arg0 + 2412, v2)
                                                                                    break
                                                                                if (load32(v3 + 20) == 0):
                                                                                    break
                                                                                while True:  # block $label77
                                                                                    while True:  # block $label72
                                                                                        while True:  # block $label49
                                                                                            while True:  # block $label42
                                                                                                while True:  # block $label43
                                                                                                    v9 = load32(v3 + 20)
                                                                                                    if load32(v3 + 20):
                                                                                                        v10 = load32(v9 + 104)
                                                                                                        if (v14 <= load32(v9 + 104)):
                                                                                                            v12 = 1
                                                                                                            if (load32(v9 + 108) >= v14):
                                                                                                                break
                                                                                                            if (load32(v3 + 132) == 0):
                                                                                                                func188()
                                                                                                                if (load32(v3 + 132) == 0):
                                                                                                                    break
                                                                                                                v10 = load32(v9 + 104)
                                                                                                            v13 = load32(v9 + 112)
                                                                                                            v16 = load32(v9 + 100)
                                                                                                            v4 = (v13 // load32(v9 + 100))
                                                                                                            v12 = (load32(v9 + 112) - ((v13 // load32(v9 + 100)) * v16))
                                                                                                            v23 = load32(v9 + 148)
                                                                                                            v24 = load32(v9 + 16)
                                                                                                            while True:  # block $label44
                                                                                                                v25 = (v14 * v16)
                                                                                                                v3 = (v13 >= (v14 * v16))
                                                                                                                if ((v13 >= (v14 * v16)) == 0):
                                                                                                                    v2 = load32(v9 + 152)
                                                                                                                    if load32(v9 + 152):
                                                                                                                    else:
                                                                                                                    v2 = 0
                                                                                                                    if (0 >= load32(v9 + 164)):
                                                                                                                        break
                                                                                                                    v17 = (load32(v9 + 168) + (v2 * 548))
                                                                                                                v20 = (v10 * v16)
                                                                                                                if ((v10 * v16) >= v13):
                                                                                                                    if (v10 >= v14):
                                                                                                                        while True:  # block $label46
                                                                                                                            while True:  # block $label45
                                                                                                                                if (load32(v9 + 120) > 0):
                                                                                                                                    break
                                                                                                                                v7 = load32(v9 + 164)
                                                                                                                                if (load32(v9 + 164) <= 0):
                                                                                                                                    break
                                                                                                                                v6 = load32(v9 + 168)
                                                                                                                                v5 = 0
                                                                                                                                while True:  # $label47
                                                                                                                                    v2 = (v6 + (v5 * 548))
                                                                                                                                    if load8u(load32((v6 + (v5 * 548)) + 4)):
                                                                                                                                        break
                                                                                                                                    if load8u(load32(v2 + 8)):
                                                                                                                                        break
                                                                                                                                    if load8u(load32(v2 + 12)):
                                                                                                                                        break
                                                                                                                                    v5 = (v5 + 1)
                                                                                                                                    if (v7 != (v5 + 1)):
                                                                                                                                        continue
                                                                                                                                    break
                                                                                                                                break
                                                                                                                                break
                                                                                                                            a_c()
                                                                                                                            raise RuntimeError('unreachable')
                                                                                                                            break
                                                                                                                        while True:  # block $label51
                                                                                                                            while True:  # block $label48
                                                                                                                                if v3:
                                                                                                                                    break
                                                                                                                                if load32(v9 + 48):
                                                                                                                                    break
                                                                                                                                v18 = (v9 + 24)
                                                                                                                                while True:  # $label73
                                                                                                                                    while True:  # block $label50
                                                                                                                                        while True:  # block $label62
                                                                                                                                            while True:  # block $label65
                                                                                                                                                if ((v12 & v23) == 0):
                                                                                                                                                    v2 = load32(v9 + 152)
                                                                                                                                                    if load32(v9 + 152):
                                                                                                                                                    else:
                                                                                                                                                    v2 = 0
                                                                                                                                                    if (0 >= load32(v9 + 164)):
                                                                                                                                                        break
                                                                                                                                                    v17 = (load32(v9 + 168) + (v2 * 548))
                                                                                                                                                while True:  # block $label58
                                                                                                                                                    while True:  # block $label59
                                                                                                                                                        while True:  # block $label60
                                                                                                                                                            while True:  # block $label61
                                                                                                                                                                if v17:
                                                                                                                                                                    v5 = load32(v9 + 44)
                                                                                                                                                                    if (load32(v9 + 44) >= 32):
                                                                                                                                                                        func135(v18)
                                                                                                                                                                        v5 = load32(v9 + 44)
                                                                                                                                                                    v51 = load64(v9 + 24)
                                                                                                                                                                    v10 = (load32(v17) + ((i32(((load64(v9 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64((v5 & 63)))) & 255) << 2))
                                                                                                                                                                    v2 = load8u((load32(v17) + ((i32(((load64(v9 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64((v5 & 63)))) & 255) << 2)))
                                                                                                                                                                    if (u(load8u((load32(v17) + ((i32(((load64(v9 + 24) & 0xFFFFFFFFFFFFFFFF) >> i64((v5 & 63)))) & 255) << 2)))) >= u(9)):
                                                                                                                                                                        v5 = (v5 + 8)
                                                                                                                                                                        v10 = ((v10 + (load16u(v10 + 2) << 2)) + ((i32(((v51 & 0xFFFFFFFFFFFFFFFF) >> i64(((v5 + 8) & 63)))) & ((-1 << (v2 - 8)) ^ -1)) << 2))
                                                                                                                                                                    else:
                                                                                                                                                                    v3 = ((v2 & 255) + v5)
                                                                                                                                                                    store32(load8u(((v10 + (load16u(v10 + 2) << 2)) + ((i32(((v51 & 0xFFFFFFFFFFFFFFFF) >> i64(((v5 + 8) & 63)))) & ((-1 << (v2 - 8)) ^ -1)) << 2))) + 44, ((v2 & 255) + v5))
                                                                                                                                                                    v2 = load16u(v10 + 2)
                                                                                                                                                                    if (u(load16u(v10 + 2)) <= u(255)):
                                                                                                                                                                        store8((v13 + v24), v2)
                                                                                                                                                                        v13 = (v13 + 1)
                                                                                                                                                                        v12 = (v12 + 1)
                                                                                                                                                                        if ((v12 + 1) < v16):
                                                                                                                                                                            break
                                                                                                                                                                        v2 = (v4 + 1)
                                                                                                                                                                        v12 = 0
                                                                                                                                                                        if (v4 >= v14):
                                                                                                                                                                            v4 = v2
                                                                                                                                                                            break
                                                                                                                                                                        if (v2 & 15):
                                                                                                                                                                            v4 = v2
                                                                                                                                                                            break
                                                                                                                                                                        v4 = v2
                                                                                                                                                                        break
                                                                                                                                                                    v11 = 1
                                                                                                                                                                    if (u(v2) > u(279)):
                                                                                                                                                                        break
                                                                                                                                                                    v7 = (v2 - 256)
                                                                                                                                                                    if (u((v2 - 256)) >= u(4)):
                                                                                                                                                                        v3 = (((v2 - 258) & 0xFFFFFFFF) >> 1)
                                                                                                                                                                        v7 = (func39(v18, (((v2 - 258) & 0xFFFFFFFF) >> 1)) + (((v2 & 1) | 2) << v3))
                                                                                                                                                                        v51 = load64(v9 + 24)
                                                                                                                                                                        v3 = load32(v9 + 44)
                                                                                                                                                                    v5 = (load32(v17 + 16) + ((i32(((v51 & 0xFFFFFFFFFFFFFFFF) >> i64((v3 & 63)))) & 255) << 2))
                                                                                                                                                                    v2 = load8u((load32(v17 + 16) + ((i32(((v51 & 0xFFFFFFFFFFFFFFFF) >> i64((v3 & 63)))) & 255) << 2)))
                                                                                                                                                                    if (u(load8u((load32(v17 + 16) + ((i32(((v51 & 0xFFFFFFFFFFFFFFFF) >> i64((v3 & 63)))) & 255) << 2)))) >= u(9)):
                                                                                                                                                                        v3 = (v3 + 8)
                                                                                                                                                                        v5 = ((v5 + (load16u(v5 + 2) << 2)) + ((i32(((v51 & 0xFFFFFFFFFFFFFFFF) >> i64(((v3 + 8) & 63)))) & ((-1 << (v2 - 8)) ^ -1)) << 2))
                                                                                                                                                                    else:
                                                                                                                                                                    v2 = ((v2 & 255) + v3)
                                                                                                                                                                    store32(load8u(((v5 + (load16u(v5 + 2) << 2)) + ((i32(((v51 & 0xFFFFFFFFFFFFFFFF) >> i64(((v3 + 8) & 63)))) & ((-1 << (v2 - 8)) ^ -1)) << 2))) + 44, ((v2 & 255) + v3))
                                                                                                                                                                    v5 = load16u(v5 + 2)
                                                                                                                                                                    if (v2 >= 32):
                                                                                                                                                                        func135(v18)
                                                                                                                                                                    while True:  # block $label52
                                                                                                                                                                        if (u(v5) >= u(4)):
                                                                                                                                                                            v2 = (((v5 - 2) & 0xFFFFFFFF) >> 1)
                                                                                                                                                                            v5 = (func39(v18, (((v5 - 2) & 0xFFFFFFFF) >> 1)) + (((v5 & 1) | 2) << v2))
                                                                                                                                                                        if ((v5 + 1) >= 121):
                                                                                                                                                                            break
                                                                                                                                                                        v2 = load8u((v5 + 13840))
                                                                                                                                                                        v2 = (((((load8u((v5 + 13840)) & 0xFFFFFFFF) >> 4) * v16) - (v2 & 15)) + 8)
                                                                                                                                                                        break
                                                                                                                                                                    v2 = (1 if (v2 <= 1) else (((((load8u((v5 + 13840)) & 0xFFFFFFFF) >> 4) * v16) - (v2 & 15)) + 8))
                                                                                                                                                                    if (v13 < (1 if (v2 <= 1) else (((((load8u((v5 + 13840)) & 0xFFFFFFFF) >> 4) * v16) - (v2 & 15)) + 8))):
                                                                                                                                                                        break
                                                                                                                                                                    v6 = (v7 + 1)
                                                                                                                                                                    if ((v7 + 1) > (v20 - v13)):
                                                                                                                                                                        break
                                                                                                                                                                    v5 = (v13 + v24)
                                                                                                                                                                    v11 = ((v13 + v24) - v2)
                                                                                                                                                                    while True:  # block $label53
                                                                                                                                                                        if (v6 < 8):
                                                                                                                                                                            break
                                                                                                                                                                        while True:  # block $label57
                                                                                                                                                                            while True:  # block $label56
                                                                                                                                                                                while True:  # block $label55
                                                                                                                                                                                    while True:  # block $label54
                                                                                                                                                                                        # br_table[(v2 - 1)]
                                                                                                                                                                                        break
                                                                                                                                                                                        break
                                                                                                                                                                                    break
                                                                                                                                                                                    break
                                                                                                                                                                                break
                                                                                                                                                                                break
                                                                                                                                                                            break
                                                                                                                                                                        v10 = load32(v11)
                                                                                                                                                                        if ((v5 & 3) == 0):
                                                                                                                                                                            v2 = v6
                                                                                                                                                                            break
                                                                                                                                                                        store8(v5, load8u(v11))
                                                                                                                                                                        v10 = rotl(v10, 24, 32)
                                                                                                                                                                        v11 = (v11 + 1)
                                                                                                                                                                        v5 = (v5 + 1)
                                                                                                                                                                        if (((v5 + 1) & 3) == 0):
                                                                                                                                                                            v3 = v6
                                                                                                                                                                            v2 = v7
                                                                                                                                                                            break
                                                                                                                                                                        store8(v5, load8u(v11))
                                                                                                                                                                        v2 = (v7 - 1)
                                                                                                                                                                        v10 = rotl(v10, 24, 32)
                                                                                                                                                                        v11 = (v11 + 1)
                                                                                                                                                                        v5 = (v5 + 1)
                                                                                                                                                                        if (((v5 + 1) & 3) == 0):
                                                                                                                                                                            v3 = v7
                                                                                                                                                                            break
                                                                                                                                                                        store8(v5, load8u(v11))
                                                                                                                                                                        v8 = (v7 - 2)
                                                                                                                                                                        v10 = rotl(v10, 24, 32)
                                                                                                                                                                        v11 = (v11 + 1)
                                                                                                                                                                        v5 = (v5 + 1)
                                                                                                                                                                        if ((v5 + 1) & 3):
                                                                                                                                                                            break
                                                                                                                                                                        v3 = v2
                                                                                                                                                                        v2 = v8
                                                                                                                                                                        break
                                                                                                                                                                        break
                                                                                                                                                                    if (v2 >= v6):
                                                                                                                                                                        break
                                                                                                                                                                    if (u(v7) > u(2147483646)):
                                                                                                                                                                        break
                                                                                                                                                                    v3 = 0
                                                                                                                                                                    v10 = 0
                                                                                                                                                                    if (u(v7) >= u(3)):
                                                                                                                                                                        v2 = (v6 & -4)
                                                                                                                                                                        v7 = 0
                                                                                                                                                                        while True:  # $label63
                                                                                                                                                                            store8((v5 + v10), load8u((v10 + v11)))
                                                                                                                                                                            v8 = (v10 | 1)
                                                                                                                                                                            store8((v5 + (v10 | 1)), load8u((v8 + v11)))
                                                                                                                                                                            v8 = (v10 | 2)
                                                                                                                                                                            store8((v5 + (v10 | 2)), load8u((v8 + v11)))
                                                                                                                                                                            v8 = (v10 | 3)
                                                                                                                                                                            store8((v5 + (v10 | 3)), load8u((v8 + v11)))
                                                                                                                                                                            v10 = (v10 + 4)
                                                                                                                                                                            v7 = (v7 + 4)
                                                                                                                                                                            if ((v7 + 4) != v2):
                                                                                                                                                                                continue
                                                                                                                                                                            break
                                                                                                                                                                    v2 = (v6 & 3)
                                                                                                                                                                    if ((v6 & 3) == 0):
                                                                                                                                                                        break
                                                                                                                                                                    while True:  # $label64
                                                                                                                                                                        store8((v5 + v10), load8u((v10 + v11)))
                                                                                                                                                                        v10 = (v10 + 1)
                                                                                                                                                                        v3 = (v3 + 1)
                                                                                                                                                                        if ((v3 + 1) != v2):
                                                                                                                                                                            continue
                                                                                                                                                                        break
                                                                                                                                                                    break
                                                                                                                                                                a_c()
                                                                                                                                                                raise RuntimeError('unreachable')
                                                                                                                                                                break
                                                                                                                                                            # TODO: memory.copy []
                                                                                                                                                            break
                                                                                                                                                            break
                                                                                                                                                        store8(v5, load8u(v11))
                                                                                                                                                        v2 = (v7 - 3)
                                                                                                                                                        v10 = rotl(v10, 24, 32)
                                                                                                                                                        v5 = (v5 + 1)
                                                                                                                                                        v11 = (v11 + 1)
                                                                                                                                                        v3 = v8
                                                                                                                                                        break
                                                                                                                                                    if (v3 < 5):
                                                                                                                                                        break
                                                                                                                                                    break
                                                                                                                                                v8 = ((v2 & 0xFFFFFFFF) >> 2)
                                                                                                                                                v21 = (((v2 & 0xFFFFFFFF) >> 2) & 7)
                                                                                                                                                v3 = 0
                                                                                                                                                v7 = 0
                                                                                                                                                if (u((v8 - 1)) >= u(7)):
                                                                                                                                                    v36 = (v8 & 1073741816)
                                                                                                                                                    v28 = 0
                                                                                                                                                    while True:  # $label66
                                                                                                                                                        v8 = (v7 << 2)
                                                                                                                                                        store32((v5 + (v7 << 2)), v10)
                                                                                                                                                        store32((v5 + (v8 | 4)), v10)
                                                                                                                                                        store32((v5 + (v8 | 8)), v10)
                                                                                                                                                        store32((v5 + (v8 | 12)), v10)
                                                                                                                                                        store32((v5 + (v8 | 16)), v10)
                                                                                                                                                        store32((v5 + (v8 | 20)), v10)
                                                                                                                                                        store32((v5 + (v8 | 24)), v10)
                                                                                                                                                        store32((v5 + (v8 | 28)), v10)
                                                                                                                                                        v7 = (v7 + 8)
                                                                                                                                                        v28 = (v28 + 8)
                                                                                                                                                        if ((v28 + 8) != v36):
                                                                                                                                                            continue
                                                                                                                                                        break
                                                                                                                                                if v21:
                                                                                                                                                    while True:  # $label67
                                                                                                                                                        store32((v5 + (v7 << 2)), v10)
                                                                                                                                                        v7 = (v7 + 1)
                                                                                                                                                        v3 = (v3 + 1)
                                                                                                                                                        if ((v3 + 1) != v21):
                                                                                                                                                            continue
                                                                                                                                                        break
                                                                                                                                                break
                                                                                                                                            v3 = (v2 & -4)
                                                                                                                                            if ((v2 & -4) >= v2):
                                                                                                                                                break
                                                                                                                                            v7 = (v2 + (v3 ^ -1))
                                                                                                                                            v10 = 0
                                                                                                                                            v8 = (v2 & 3)
                                                                                                                                            if (v2 & 3):
                                                                                                                                                while True:  # $label68
                                                                                                                                                    store8((v3 + v5), load8u((v3 + v11)))
                                                                                                                                                    v3 = (v3 + 1)
                                                                                                                                                    v10 = (v10 + 1)
                                                                                                                                                    if ((v10 + 1) != v8):
                                                                                                                                                        continue
                                                                                                                                                    break
                                                                                                                                            if (u(v7) < u(3)):
                                                                                                                                                break
                                                                                                                                            while True:  # $label69
                                                                                                                                                store8((v3 + v5), load8u((v3 + v11)))
                                                                                                                                                v7 = (v3 + 1)
                                                                                                                                                store8((v5 + (v3 + 1)), load8u((v7 + v11)))
                                                                                                                                                v7 = (v3 + 2)
                                                                                                                                                store8((v5 + (v3 + 2)), load8u((v7 + v11)))
                                                                                                                                                v7 = (v3 + 3)
                                                                                                                                                store8((v5 + (v3 + 3)), load8u((v7 + v11)))
                                                                                                                                                v3 = (v3 + 4)
                                                                                                                                                if ((v3 + 4) != v2):
                                                                                                                                                    continue
                                                                                                                                                break
                                                                                                                                            break
                                                                                                                                        v13 = (v6 + v13)
                                                                                                                                        v12 = (v6 + v12)
                                                                                                                                        if (v16 <= (v6 + v12)):
                                                                                                                                            while True:  # $label71
                                                                                                                                                v12 = (v12 - v16)
                                                                                                                                                v2 = v4
                                                                                                                                                v4 = (v4 + 1)
                                                                                                                                                while True:  # block $label70
                                                                                                                                                    if (v2 >= v14):
                                                                                                                                                        break
                                                                                                                                                    if (v4 & 15):
                                                                                                                                                        break
                                                                                                                                                    break
                                                                                                                                                if (v12 >= v16):
                                                                                                                                                    continue
                                                                                                                                                break
                                                                                                                                        if (v13 >= v25):
                                                                                                                                            break
                                                                                                                                        if ((v12 & v23) == 0):
                                                                                                                                            break
                                                                                                                                        v2 = load32(v9 + 152)
                                                                                                                                        if load32(v9 + 152):
                                                                                                                                        else:
                                                                                                                                        v2 = 0
                                                                                                                                        if (0 >= load32(v9 + 164)):
                                                                                                                                            break
                                                                                                                                        v17 = (load32(v9 + 168) + (v2 * 548))
                                                                                                                                        break
                                                                                                                                    v2 = load32(v9 + 40)
                                                                                                                                    v3 = load32(v9 + 36)
                                                                                                                                    if (u(load32(v9 + 40)) > u(load32(v9 + 36))):
                                                                                                                                        break
                                                                                                                                    if load32(v9 + 48):
                                                                                                                                        store32(v9 + 48, 1)
                                                                                                                                        break
                                                                                                                                    v5 = 0
                                                                                                                                    if (v2 == v3):
                                                                                                                                        v5 = (load32(v9 + 44) > 64)
                                                                                                                                    store32(v9 + 48, v5)
                                                                                                                                    if v5:
                                                                                                                                        break
                                                                                                                                    if (v13 < v25):
                                                                                                                                        continue
                                                                                                                                    break
                                                                                                                                break
                                                                                                                            v11 = 0
                                                                                                                            break
                                                                                                                        v4 = load32(v9 + 40)
                                                                                                                        v2 = load32(v9 + 36)
                                                                                                                        if (u(load32(v9 + 40)) <= u(load32(v9 + 36))):
                                                                                                                            while True:  # block $label74
                                                                                                                                if load32(v9 + 48):
                                                                                                                                    break
                                                                                                                                if (v2 != v4):
                                                                                                                                    break
                                                                                                                                break
                                                                                                                            v4 = (load32(v9 + 44) > 64)
                                                                                                                            store32(v9 + 48, (load32(v9 + 44) > 64))
                                                                                                                            while True:  # block $label75
                                                                                                                                if (v11 == 0):
                                                                                                                                    if (v4 == 0):
                                                                                                                                        break
                                                                                                                                    if (v13 >= v20):
                                                                                                                                        break
                                                                                                                                v12 = 0
                                                                                                                                while True:  # block $label76
                                                                                                                                    # br_table[load32(v9)]
                                                                                                                                    break
                                                                                                                                    break
                                                                                                                                store32(v9, (5 if v4 else 3))
                                                                                                                                break
                                                                                                                                break
                                                                                                                            store32(v9 + 112, v13)
                                                                                                                            break
                                                                                                                        break
                                                                                                                    a_c()
                                                                                                                    raise RuntimeError('unreachable')
                                                                                                                a_c()
                                                                                                                raise RuntimeError('unreachable')
                                                                                                                break
                                                                                                            break
                                                                                                        a_c()
                                                                                                        raise RuntimeError('unreachable')
                                                                                                    a_c()
                                                                                                    raise RuntimeError('unreachable')
                                                                                                    break
                                                                                                v12 = func275(v9, load32(v9 + 16), load32(v9 + 100), load32(v9 + 104), v14, 277)
                                                                                                break
                                                                                            break
                                                                                            break
                                                                                        a_c()
                                                                                        raise RuntimeError('unreachable')
                                                                                        break
                                                                                    a_c()
                                                                                    raise RuntimeError('unreachable')
                                                                                    break
                                                                                if (3953 == 0):
                                                                                    break
                                                                                break
                                                                            while True:  # block $label78
                                                                                if (v14 >= v31):
                                                                                    store32(arg0 + 2400, 1)
                                                                                    break
                                                                                if (load32(arg0 + 2400) == 0):
                                                                                    break
                                                                                break
                                                                            v4 = load32(arg0 + 2388)
                                                                            if load32(arg0 + 2388):
                                                                                func190(load32(v4 + 20))
                                                                                store32(v4 + 20, 0)
                                                                            store32(arg0 + 2388, 0)
                                                                            v4 = load32(arg0 + 2416)
                                                                            if (load32(arg0 + 2416) <= 0):
                                                                                break
                                                                            v2 = load32(arg1 + 76)
                                                                            v3 = load32(arg1 + 84)
                                                                            v7 = (load32(arg1 + 76) + (load32(arg0 + 2408) + (load32(arg1 + 84) * v30)))
                                                                            v16 = (load32(arg1 + 80) - v2)
                                                                            v23 = (load32(arg1 + 88) - v3)
                                                                            v6 = 0
                                                                            v10 = 0
                                                                            v31 = 0
                                                                            v25 = (G.global0 - 256)
                                                                            G.global0 = (G.global0 - 256)
                                                                            v2 = (v4 // 25)
                                                                            while True:  # block $label79
                                                                                if (u(v4) > u(100)):
                                                                                    break
                                                                                if (v7 == 0):
                                                                                    break
                                                                                if (v16 <= 0):
                                                                                    break
                                                                                if (v23 <= 0):
                                                                                    break
                                                                                v6 = 1
                                                                                v42 = (v23 - 1)
                                                                                v36 = (v16 - 1)
                                                                                v4 = ((((v16 - 1) & 0xFFFFFFFF) >> 1) if (((v2 << 1) | 1) > v16) else v2)
                                                                                v13 = ((((v23 - 1) & 0xFFFFFFFF) >> 1) if (((v4 << 1) | 1) > v23) else ((((v16 - 1) & 0xFFFFFFFF) >> 1) if (((v2 << 1) | 1) > v16) else v2))
                                                                                if (((((v23 - 1) & 0xFFFFFFFF) >> 1) if (((v4 << 1) | 1) > v23) else ((((v16 - 1) & 0xFFFFFFFF) >> 1) if (((v2 << 1) | 1) > v16) else v2)) <= 0):
                                                                                    break
                                                                                v6 = 0
                                                                                v20 = (v16 << 1)
                                                                                v19 = (v13 << 1)
                                                                                v2 = (v20 * ((v13 << 1) + 2))
                                                                                v9 = func58(1, (((v16 << 1) + (v20 * ((v13 << 1) + 2))) + 4094))
                                                                                if (func58(1, (((v16 << 1) + (v20 * ((v13 << 1) + 2))) + 4094)) == 0):
                                                                                    break
                                                                                v24 = (0 - v13)
                                                                                v4 = (v19 | 1)
                                                                                v12 = (v9 + (((v19 | 1) * v16) << 1))
                                                                                v11 = ((v9 + (((v19 | 1) * v16) << 1)) - v20)
                                                                                # TODO: memory.fill []
                                                                                # TODO: memory.fill []
                                                                                v17 = (v2 + v9)
                                                                                v18 = (v4 * v4)
                                                                                v28 = 255
                                                                                v3 = 0
                                                                                v14 = 255
                                                                                v4 = v7
                                                                                while True:  # $label81
                                                                                    v6 = v3
                                                                                    v8 = v14
                                                                                    v2 = 0
                                                                                    while True:  # $label80
                                                                                        v5 = load8u((v2 + v4))
                                                                                        store8((v25 + load8u((v2 + v4))), 1)
                                                                                        v21 = (v5 > v6)
                                                                                        v3 = (v5 if (v5 > v6) else v3)
                                                                                        v31 = (v5 if v21 else v31)
                                                                                        v21 = (v5 < v8)
                                                                                        v14 = (v5 if (v5 < v8) else v14)
                                                                                        v28 = (v5 if v21 else v28)
                                                                                        v6 = (v6 if (v5 < v6) else v5)
                                                                                        v8 = (v8 if (v5 > v8) else v5)
                                                                                        v2 = (v2 + 1)
                                                                                        if ((v2 + 1) != v16):
                                                                                            continue
                                                                                        break
                                                                                    v4 = (v4 + v30)
                                                                                    v10 = (v10 + 1)
                                                                                    if ((v10 + 1) != v23):
                                                                                        continue
                                                                                    break
                                                                                v8 = (v3 - v14)
                                                                                v5 = (v17 + v20)
                                                                                v6 = -1
                                                                                v2 = 0
                                                                                v4 = 0
                                                                                while True:  # $label83
                                                                                    if load8u((v4 + v25)):
                                                                                        v2 = (v2 + 1)
                                                                                        if (v6 >= 0):
                                                                                            v3 = (v4 - v6)
                                                                                            v8 = ((v4 - v6) if (v3 < v8) else v8)
                                                                                    else:
                                                                                    v3 = v6
                                                                                    while True:  # block $label82
                                                                                        v6 = (v4 | 1)
                                                                                        if (load8u((v25 + (v4 | 1))) == 0):
                                                                                            v6 = v3
                                                                                            break
                                                                                        v2 = (v2 + 1)
                                                                                        if (v3 < 0):
                                                                                            break
                                                                                        v3 = (v6 - v3)
                                                                                        v8 = ((v6 - v3) if (v3 < v8) else v8)
                                                                                        break
                                                                                    v4 = (v4 + 2)
                                                                                    if ((v4 + 2) != 256):
                                                                                        continue
                                                                                    break
                                                                                v3 = (v8 << 2)
                                                                                v6 = ((v8 * 12) >> 2)
                                                                                v8 = ((v8 << 2) - ((v8 * 12) >> 2))
                                                                                v21 = (v5 + 2046)
                                                                                v4 = 1
                                                                                while True:  # $label85
                                                                                    v5 = (v4 << 1)
                                                                                    while True:  # block $label84
                                                                                        if (v4 <= v6):
                                                                                            break
                                                                                        if (v3 <= v4):
                                                                                            break
                                                                                        break
                                                                                    v14 = (((((v3 - v4) * v6) // v8) & 0xFFFFFFFF) >> 2)
                                                                                    store16((v21 + (v4 << 1)), (((((v3 - v4) * v6) // v8) & 0xFFFFFFFF) >> 2))
                                                                                    store16((v21 - v5), (0 - v14))
                                                                                    v4 = (v4 + 1)
                                                                                    if ((v4 + 1) != 1024):
                                                                                        continue
                                                                                    break
                                                                                store16(v21, 0)
                                                                                # TODO: i32.div_u []
                                                                                v18 = v18
                                                                                while True:  # block $label86
                                                                                    if (v2 < 3):
                                                                                        break
                                                                                    if (v23 <= v24):
                                                                                        break
                                                                                    v10 = (v13 + 2)
                                                                                    v40 = (v16 & 1)
                                                                                    v43 = (v16 & -2)
                                                                                    v44 = (v20 - 2)
                                                                                    v20 = (v13 ^ -1)
                                                                                    v5 = (v16 - v13)
                                                                                    v41 = (v13 - 1)
                                                                                    v8 = (v13 + 1)
                                                                                    v45 = ((v13 + 1) & -2)
                                                                                    v46 = (v8 & 1)
                                                                                    v47 = (v12 + (v36 << 1))
                                                                                    v48 = (v17 + (v8 << 1))
                                                                                    v49 = (v12 + ((v8 + v13) << 1))
                                                                                    v50 = ((v16 - 2) == v19)
                                                                                    v2 = v9
                                                                                    v3 = v7
                                                                                    while True:  # $label94
                                                                                        v14 = 0
                                                                                        v4 = 0
                                                                                        v6 = 0
                                                                                        if v36:
                                                                                            while True:  # $label87
                                                                                                v19 = (v4 << 1)
                                                                                                v14 = (load8u((v3 + v4)) + (v14 & 65535))
                                                                                                v32 = ((load8u((v3 + v4)) + (v14 & 65535)) + load16u((v11 + v19)))
                                                                                                v19 = (v2 + v19)
                                                                                                store16((v12 + (v4 << 1)), (((load8u((v3 + v4)) + (v14 & 65535)) + load16u((v11 + v19))) - load16u((v2 + v19))))
                                                                                                store16(v19, v32)
                                                                                                v32 = (v4 | 1)
                                                                                                v19 = ((v4 | 1) << 1)
                                                                                                v14 = (load8u((v3 + v32)) + (v14 & 65535))
                                                                                                v32 = ((load8u((v3 + v32)) + (v14 & 65535)) + load16u((v11 + v19)))
                                                                                                v19 = (v2 + v19)
                                                                                                store16((v12 + ((v4 | 1) << 1)), (((load8u((v3 + v32)) + (v14 & 65535)) + load16u((v11 + v19))) - load16u((v2 + v19))))
                                                                                                store16(v19, v32)
                                                                                                v4 = (v4 + 2)
                                                                                                v6 = (v6 + 2)
                                                                                                if ((v6 + 2) != v43):
                                                                                                    continue
                                                                                                break
                                                                                        if v40:
                                                                                            v6 = (v4 << 1)
                                                                                            v4 = (load16u((v6 + v11)) + (v14 + load8u((v3 + v4))))
                                                                                            v6 = (v2 + v6)
                                                                                            store16((v12 + (v4 << 1)), ((load16u((v6 + v11)) + (v14 + load8u((v3 + v4)))) - load16u((v2 + v6))))
                                                                                            store16(v6, v4)
                                                                                        v14 = (v2 + (v16 << 1))
                                                                                        v19 = ((v2 + (v16 << 1)) == v12)
                                                                                        v4 = 0
                                                                                        v6 = 0
                                                                                        if (v13 <= v24):
                                                                                            while True:  # $label88
                                                                                                store16((v17 + (v4 << 1)), (((v18 * ((load16u((v12 + ((v13 - v4) << 1))) + load16u((v12 + ((v4 + v41) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                v11 = (v4 | 1)
                                                                                                store16((v17 + ((v4 | 1) << 1)), (((v18 * ((load16u((v12 + ((v13 - v11) << 1))) + load16u((v12 + ((v4 + v13) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                v4 = (v4 + 2)
                                                                                                v6 = (v6 + 2)
                                                                                                if ((v6 + 2) != v45):
                                                                                                    continue
                                                                                                break
                                                                                            if v46:
                                                                                                store16((v17 + (v4 << 1)), (((v18 * ((load16u((v12 + ((v13 - v4) << 1))) + load16u((v12 + ((v4 + v41) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                            while True:  # block $label89
                                                                                                v4 = v8
                                                                                                if (v8 >= v5):
                                                                                                    break
                                                                                                v6 = v8
                                                                                                if (v40 == 0):
                                                                                                    store16(v48, (((v18 * ((load16u(v49) - load16u(v12)) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                    v6 = v10
                                                                                                v4 = v5
                                                                                                if v50:
                                                                                                    break
                                                                                                while True:  # $label90
                                                                                                    store16((v17 + (v6 << 1)), (((v18 * ((load16u((v12 + ((v6 + v13) << 1))) - load16u((v12 + ((v6 + v20) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                    v4 = (v6 + 1)
                                                                                                    store16((v17 + ((v6 + 1) << 1)), (((v18 * ((load16u((v12 + ((v4 + v13) << 1))) - load16u((v12 + ((v6 - v13) << 1)))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                    v6 = (v6 + 2)
                                                                                                    if ((v6 + 2) != v5):
                                                                                                        continue
                                                                                                    break
                                                                                                v4 = v5
                                                                                                break
                                                                                            if (v4 < v16):
                                                                                                while True:  # $label91
                                                                                                    store16((v17 + (v4 << 1)), (((v18 * (((load16u(v47) << 1) - (load16u((v12 + ((v44 - (v4 + v13)) << 1))) + load16u((v12 + ((v4 + v20) << 1))))) & 65535)) & 0xFFFFFFFF) >> 16))
                                                                                                    v4 = (v4 + 1)
                                                                                                    if ((v4 + 1) != v16):
                                                                                                        continue
                                                                                                    break
                                                                                            v4 = 0
                                                                                            while True:  # $label93
                                                                                                while True:  # block $label92
                                                                                                    v11 = (v4 + v7)
                                                                                                    v6 = load8u((v4 + v7))
                                                                                                    if (v31 <= load8u((v4 + v7))):
                                                                                                        break
                                                                                                    if (v6 <= v28):
                                                                                                        break
                                                                                                    v6 = (load16s((v21 + ((load16u((v17 + (v4 << 1))) - (v6 << 2)) << 1))) + v6)
                                                                                                    v6 = ((load16s((v21 + ((load16u((v17 + (v4 << 1))) - (v6 << 2)) << 1))) + v6) if (v6 > 0) else 0)
                                                                                                    store8(v11, (255 if (v6 >= 255) else ((load16s((v21 + ((load16u((v17 + (v4 << 1))) - (v6 << 2)) << 1))) + v6) if (v6 > 0) else 0)))
                                                                                                    break
                                                                                                v4 = (v4 + 1)
                                                                                                if ((v4 + 1) != v16):
                                                                                                    continue
                                                                                                break
                                                                                            v7 = (v7 + v30)
                                                                                        v3 = (((v30 if (v24 < v42) else 0) if (v24 >= 0) else 0) + v3)
                                                                                        v11 = v2
                                                                                        v2 = (v9 if v19 else v14)
                                                                                        v24 = (v24 + 1)
                                                                                        if ((v24 + 1) != v23):
                                                                                            continue
                                                                                        break
                                                                                    break
                                                                                v6 = 1
                                                                                break
                                                                            G.global0 = (v25 + 256)
                                                                            if (v6 == 0):
                                                                                break
                                                                            break
                                                                        v2 = (load32(arg0 + 2408) + (v15 * v30))
                                                                        break
                                                                    break
                                                                a_c()
                                                                raise RuntimeError('unreachable')
                                                                break
                                                            a_c()
                                                            raise RuntimeError('unreachable')
                                                            break
                                                        a_c()
                                                        raise RuntimeError('unreachable')
                                                        break
                                                    a_c()
                                                    raise RuntimeError('unreachable')
                                                    break
                                                a_c()
                                                raise RuntimeError('unreachable')
                                                break
                                            a_c()
                                            raise RuntimeError('unreachable')
                                            break
                                        a_c()
                                        raise RuntimeError('unreachable')
                                        break
                                    a_c()
                                    raise RuntimeError('unreachable')
                                    break
                                store64(arg0 + 2404, 0)
                                v4 = load32(arg0 + 2388)
                                if load32(arg0 + 2388):
                                    func190(load32(v4 + 20))
                                    store32(v4 + 20, 0)
                                store32(arg0 + 2388, 0)
                                break
                            v4 = 0
                            store32(af(v4) + 104, 0)
                            if (v4 == 0):
                                break
                            break
                        v2 = load32(arg1 + 84)
                        if (v15 < load32(arg1 + 84)):
                            v3 = (v2 - v15)
                            if ((v2 - v15) & 1):
                                break
                            store32(arg1 + 20, (load32(arg1 + 20) + (load32(arg0 + 2324) * v3)))
                            v7 = (load32(arg0 + 2328) * (v3 >> 1))
                            store32(arg1 + 24, ((load32(arg0 + 2328) * (v3 >> 1)) + load32(arg1 + 24)))
                            store32(arg1 + 28, (load32(arg1 + 28) + v7))
                            while True:  # block $label97
                                if (v4 == 0):
                                    v4 = 0
                                    break
                                v4 = (v4 + (load32(arg1) * v3))
                                store32(arg1 + 104, (v4 + (load32(arg1) * v3)))
                                break
                            v15 = v2
                        if (v15 >= v35):
                            break
                        v3 = load32(arg1 + 76)
                        store32(arg1 + 20, (load32(arg1 + 76) + load32(arg1 + 20)))
                        v7 = (v3 >> 1)
                        store32(arg1 + 24, ((v3 >> 1) + load32(arg1 + 24)))
                        store32(arg1 + 28, (load32(arg1 + 28) + v7))
                        if v4:
                            store32(arg1 + 104, (v3 + v4))
                        store32(arg1 + 8, (v15 - v2))
                        store32(arg1 + 16, (v35 - v15))
                        store32(arg1 + 12, (load32(arg1 + 80) - v3))
                        # call_indirect[load32(arg1 + 44)]
                        break
                    v2 = indirect_call(load32(arg1 + 44))
                    if (load32(arg0 + 168) != (v37 + 1)):
                        break
                    if (v33 >= v39):
                        break
                    # TODO: memory.copy []
                    arg1 = (0 - v34)
                    # TODO: memory.copy []
                    # TODO: memory.copy []
                    break
                    break
                a_c()
                raise RuntimeError('unreachable')
                break
            a_c()
            raise RuntimeError('unreachable')
            break
        v2 = func99(arg0, 3, 8467)
        break
    G.global0 = (v29 - -64)
    return v2

# ------------------------------------------------------------
# $ze
# Export: ze
# ------------------------------------------------------------
def ze(arg0):
    """Exported as ze."""
    while True:  # block $label0
        if (arg0 == 0):
            break
        v21 = load32(9142440)
        if (load32(9142440) > 0):
            while True:  # $label12
                v3 = 0
                while True:  # $label11
                    v2 = 0
                    v25 = 0.0
                    v26 = 0.0
                    while True:  # block $label1
                        v17 = ((load32(9142440) * v3) + v5)
                        v22 = (((load32(9142440) * v3) + v5) + load32(9147288))
                        v1 = load8u((((load32(9142440) * v3) + v5) + load32(9147288)))
                        # TODO: i32.extend8_s []
                        v7 = load8u((((load32(9142440) * v3) + v5) + load32(9147288)))
                        v12 = ((load8u((((load32(9142440) * v3) + v5) + load32(9147288))) + 128) if (v7 < 0) else v7)
                        if (u(((load8u((((load32(9142440) * v3) + v5) + load32(9147288))) + 128) if (v7 < 0) else v7)) <= u(15)):
                            v7 = load32(load32(9142424) + 24)
                            break
                        break
                    v16 = (((v12 & 0xFFFFFFFF) >> 4) - 1)
                    v4 = ((v1 & 0xFFFFFFFF) >> 7)
                    while True:  # block $label2
                        v10 = load32((load32(9561728) + (v17 << 2)))
                        if (load32((load32(9561728) + (v17 << 2))) < 4):
                            v1 = (((v1 << 4) | ((((v1 << 24) + 1879048192) & 0xFFFFFFFF) >> 28)) & 255)
                            v9 = ((u((((v1 << 4) | ((((v1 << 24) + 1879048192) & 0xFFFFFFFF) >> 28)) & 255)) < u(14)) & ((10965 & 0xFFFFFFFF) >> v1))
                            break
                        v9 = 1
                        v1 = (((v10 << 1) & 6) | v4)
                        if ((((v10 << 1) & 6) | v4) == 0):
                            v1 = load32(load32(9142424) + 24)
                            v16 = (5 if (v1 == 2) else (4 if (load32(load32(9142424) + 24) == 3) else 7))
                            break
                        v16 = (v1 - 1)
                        break
                    v13 = load32(9140332)
                    v1 = load32((load32(9140332) + (v16 << 2)))
                    v7 = load32(load32((load32(9140332) + (v16 << 2))))
                    while True:  # block $label3
                        if (load32(v1 + 20) == 0):
                            break
                        v2 = load32(v1 + 28)
                        if (load32(v1 + 28) != 2147483647):
                            break
                        while True:  # block $label4
                            v14 = load8u(9142916)
                            if load8u(9142916):
                                v2 = load32(59152)
                                store32(59152, (load32(59152) + 1))
                                v8 = load32(9568052)
                                break
                            v8 = load32(9568052)
                            v2 = ((load32(9140308) + v7) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                            break
                        v15 = v7
                        store32(v1 + 28, v2)
                        v11 = load32(v1 + 4)
                        v18 = load32(9568048)
                        store32(9568048, (load32(9568048) + 1))
                        store32(((v18 << 2) + 9563952), v1)
                        store32(9568052, (((v15 * (v11 + 2)) << 2) + v8))
                        if (v14 == 0):
                            break
                        v8 = load32(9568056)
                        store32(v1 + 56, load32(9568056))
                        store32(9568056, (v8 + ((v11 * load32(v1)) << 2)))
                        break
                    v14 = (v5 << 5)
                    v15 = (v3 << 5)
                    v2 = ((((v5 << 5) % v7) + v2) + (((v3 << 5) % v7) * v7))
                    v18 = load32(v1 + 32)
                    while True:  # block $label5
                        if v9:
                            v4 = 0
                            break
                        while True:  # block $label6
                            v1 = (((v10 % 4) << 1) | v4)
                            if ((((v10 % 4) << 1) | v4) == 0):
                                v1 = load32(load32(9142424) + 24)
                                break
                            break
                        v1 = load32(((5 if (v1 == 2) else (4 if (load32(load32(9142424) + 24) == 3) else 7)) + ((v1 - 1) << 2)))
                        v4 = load32(load32(((5 if (v1 == 2) else (4 if (load32(load32(9142424) + 24) == 3) else 7)) + ((v1 - 1) << 2))))
                        v10 = 0
                        v9 = 0
                        while True:  # block $label7
                            if (load32(v1 + 20) == 0):
                                break
                            v9 = load32(v1 + 28)
                            if (load32(v1 + 28) != 2147483647):
                                break
                            while True:  # block $label8
                                v13 = load8u(9142916)
                                if load8u(9142916):
                                    v9 = load32(59152)
                                    store32(59152, (load32(59152) + 1))
                                    v8 = load32(9568052)
                                    break
                                v8 = load32(9568052)
                                v9 = ((load32(9140308) + v4) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                break
                            v19 = v4
                            store32(v1 + 28, v9)
                            v11 = load32(v1 + 4)
                            v20 = load32(9568048)
                            store32(9568048, (load32(9568048) + 1))
                            store32(((v20 << 2) + 9563952), v1)
                            store32(9568052, (((v19 * (v11 + 2)) << 2) + v8))
                            if (v13 == 0):
                                break
                            v8 = load32(9568056)
                            store32(v1 + 56, load32(9568056))
                            store32(9568056, (v8 + ((v11 * load32(v1)) << 2)))
                            break
                        v8 = (v12 & 15)
                        v12 = (load32(v1 + 32) == 23)
                        v11 = ((13 - (v12 & 15)) if (load32(v1 + 32) == 23) else v8)
                        v13 = (((v14 % v4) + v9) + ((v15 % v4) * v4))
                        v14 = (v2 if v12 else (((v14 % v4) + v9) + ((v15 % v4) * v4)))
                        v15 = (v4 // 32)
                        v1 = (v1 + (load32(v1 + 44) << 2))
                        v8 = load32((v1 + (load32(v1 + 44) << 2)))
                        while True:  # block $label9
                            if (load32(v1 + 20) == 0):
                                break
                            v10 = load32(v1 + 28)
                            if (load32(v1 + 28) != 2147483647):
                                break
                            while True:  # block $label10
                                v19 = load8u(9142916)
                                if load8u(9142916):
                                    v10 = load32(59152)
                                    store32(59152, (load32(59152) + 1))
                                    v4 = load32(9568052)
                                    break
                                v4 = load32(9568052)
                                v10 = ((load32(9140308) + v8) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                break
                            v20 = v8
                            store32(v1 + 28, v10)
                            v9 = load32(v1 + 4)
                            v23 = load32(9568048)
                            store32(9568048, (load32(9568048) + 1))
                            store32(((v23 << 2) + 9563952), v1)
                            store32(9568052, (((v20 * (v9 + 2)) << 2) + v4))
                            if (v19 == 0):
                                break
                            v4 = load32(9568056)
                            store32(v1 + 56, load32(9568056))
                            store32(9568056, (v4 + ((v9 * load32(v1)) << 2)))
                            break
                        v2 = (v13 if v12 else v2)
                        v26 = float(((v10 + ((v8 * v11) << 5)) + ((load32((((v17 % 24) << 2) + 9824)) << 5) & 32)))
                        v4 = ((v8 // 32) << 16)
                        v25 = float(v14)
                        break
                    v8 = (0 if v12 else (v15 << 8))
                    v1 = (load32(9142400) + (v17 << 4))
                    store32((load32(9142400) + (v17 << 4)), float(v2))
                    store32(v1 + 4, v25)
                    store32(v1 + 8, v26)
                    store32(v1 + 12, float(((v8 + ((v7 // 32) if (v18 != 23) else 0)) + v4)))
                    store8(v22, v16)
                    v3 = (v3 + 1)
                    if ((v3 + 1) != v21):
                        continue
                    break
                v5 = (v5 + 1)
                if ((v5 + 1) != v21):
                    continue
                break
        while True:  # block $label13
            v2 = load32(9140328)
            if (load32(9140328) == 0):
                break
            v1 = 0
            v3 = load32(9142440)
            v5 = (load32(9142440) * v3)
            v3 = 0
            if (u(v2) >= u(4)):
                v4 = (v2 & -4)
                while True:  # $label14
                    v7 = (v3 << 2)
                    v6 = ((((v5 * load32(load32((((v3 << 2) | 12) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + ((((((v5 * load32(load32((v7 + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + v6) + (((v5 * load32(load32(((v7 | 4) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)) + (((v5 * load32(load32(((v7 | 8) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)))
                    v3 = (v3 + 4)
                    v24 = (v24 + 4)
                    if ((v24 + 4) != v4):
                        continue
                    break
            v2 = (v2 & 3)
            if ((v2 & 3) == 0):
                break
            while True:  # $label15
                v6 = ((((v5 * load32(load32(((v3 << 2) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + v6)
                v3 = (v3 + 1)
                v1 = (v1 + 1)
                if ((v1 + 1) != v2):
                    continue
                break
            break
        if load32(9681936):
            break
        v3 = func26(16)
        v5 = (v6 << 2)
        store32(func26(16) + 4, (v6 << 2))
        store32(v3, func26((-1 if (u(v5) > u(1073741823)) else (v6 << 4))))
        store64(v3 + 8, 206158430208)
        store32(9681936, v3)
        break
    v1 = 0
    v7 = load32(9142440)
    if (load32(9142440) > 0):
        while True:  # $label19
            v5 = (v1 + 1)
            v3 = 0
            while True:  # $label18
                while True:  # block $label17
                    while True:  # block $label16
                        v2 = load32(9142440)
                        v6 = load8s((load32(9147288) + ((load32(9142440) * v3) + v1)))
                        if (load8s((load32(9147288) + ((load32(9142440) * v3) + v1))) >= 0):
                            if (load32(load32((load32(9140332) + ((v6 & 255) << 2))) + 32) == 23):
                                break
                        v6 = load32(9142840)
                        v3 = (v3 + 1)
                        v2 = (((v3 + 1) * (v2 + 2)) + v5)
                        v4 = (load32(9671128) + (load32((load32(9142840) + ((((v3 + 1) * (v2 + 2)) + v5) << 2))) * 132))
                        if (load32(((load8u((load32(9671128) + (load32((load32(9142840) + ((((v3 + 1) * (v2 + 2)) + v5) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 4):
                            v2 = (((load32(9142440) + 2) * v3) + v5)
                            v6 = load32(9142840)
                        v2 = (v6 + (v2 << 2))
                        if (load32((v6 + (v2 << 2))) != 1):
                            break
                        store32(v2, 0)
                        v2 = (load32(9142440) + 2)
                        store32((v6 + (((((load32(9142440) + 2) + v3) * v2) + v5) << 2)), 0)
                        break
                        break
                    v6 = load32(9142840)
                    v2 = (v2 + 2)
                    v3 = (v3 + 1)
                    v4 = (load32(9142840) + ((((v2 + 2) * (v3 + 1)) + v5) << 2))
                    if (load32((load32(9142840) + ((((v2 + 2) * (v3 + 1)) + v5) << 2))) == 0):
                        store32(v4, 1)
                        v2 = (load32(9142440) + 2)
                    v2 = (((v2 + v3) * v2) + v5)
                    v4 = load32((v6 + ((((v2 + v3) * v2) + v5) << 2)))
                    if (u(load32((v6 + ((((v2 + v3) * v2) + v5) << 2)))) >= u(3)):
                        v6 = (load32(9142440) + 2)
                        v2 = ((((load32(9142440) + 2) + v3) * v6) + v5)
                        v6 = load32(9142840)
                    store32((v6 + (v2 << 2)), 1)
                    break
                if (v3 != v7):
                    continue
                break
            v1 = v5
            if (v5 != v7):
                continue
            break
    if (arg0 == 0):
    return func115(0, 0, load32(9142440), 0, 0)

# ------------------------------------------------------------
# $kc
# Export: kc
# ------------------------------------------------------------
def kc():
    """Exported as kc."""
    return load32(51776)

# ------------------------------------------------------------
# $func470
# ------------------------------------------------------------
def func470(arg0, arg1):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(9671128)
    arg1 = (load32(9671128) + (arg0 * 132))
    v5 = load16u(arg1 + 116)
    v6 = load16u(arg1 + 118)
    while True:  # block $label0
        v3 = load32(9142840)
        arg1 = (load32(9142440) + 2)
        v4 = (v6 + (load32(9142440) + 2))
        if (load32((load32(9142840) + ((v5 + (((v6 + (load32(9142440) + 2)) + 1) * arg1)) << 2)) + 4) != 1):
            break
        if (load32((((v5 + ((v4 + 3) * arg1)) << 2) + v3) + 12) != 1):
            break
        arg1 = 0
        v3 = (load32(9561692) + (load16u((v2 + (arg0 * 132)) + 110) * 286704))
        v2 = (load32(((load32(9561692) + (load16u((v2 + (arg0 * 132)) + 110) * 286704)) + 284192)) << 2)
        v3 = load32((v3 + 284196))
        if (u((load32(((load32(9561692) + (load16u((v2 + (arg0 * 132)) + 110) * 286704)) + 284192)) << 2)) <= u(load32((v3 + 284196)))):
            # TODO: i32.div_u []
            v4 = v2
            v4 = (v3 if (u(v4) <= u(1)) else v2)
            v8 = ((v6 << 16) | v5)
            while True:  # $label1
                arg1 = (arg1 + 1)
                if (arg1 != v4):
                    continue
                break
        arg1 = 0
        while True:  # block $label2
            if load8u(9142917):
                break
            arg0 = load32(9299880)
            if load32(9299880):
                arg0 = (arg0 - 1)
                store32(9299880, (arg0 - 1))
                arg1 = load32((load32(9299872) + (arg0 << 2)))
                break
            arg1 = load32(9163776)
            arg0 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v2 = load32(9163784)
            if (u(arg0) < u(load32(9163784))):
                break
            store32(v7, v2)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        # TODO: f64.convert_i32_u []
        # TODO: f32.demote_f64 []
        break
    G.global0 = (v7 + 16)

# ------------------------------------------------------------
# $func471
# ------------------------------------------------------------
def func471(arg0, arg1):
    v6 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v11 = ((arg1 & 0xFFFFFFFF) >> 16)
    v14 = (((arg1 & 0xFFFFFFFF) >> 16) + 3)
    v12 = (v11 + 2)
    v13 = (v11 + 1)
    v8 = (arg1 & 65535)
    v15 = ((arg1 & 65535) + 2)
    v7 = (load32(9671128) + (arg0 * 132))
    arg1 = load32(9142440)
    while True:  # $label6
        arg0 = v8
        v8 = (v8 + 1)
        while True:  # block $label0
            if (u(arg1) <= u(v11)):
                break
            if (u(arg0) >= u(arg1)):
                break
            while True:  # block $label1
                arg1 = load32((load32(9142840) + ((v8 + (v13 * (arg1 + 2))) << 2)))
                if (u(load32((load32(9142840) + ((v8 + (v13 * (arg1 + 2))) << 2)))) < u(3)):
                    break
                arg1 = (load32(9671128) + (arg1 * 132))
                v5 = load8u((load32(9671128) + (arg1 * 132)) + 122)
                v2 = ((load8u((load32(9671128) + (arg1 * 132)) + 122) * 404) + 9568096)
                if (load32(((load8u((load32(9671128) + (arg1 * 132)) + 122) * 404) + 9568096) + 264) != 4):
                    break
                v9 = load32(9561692)
                v10 = load16u(v7 + 110)
                v4 = (load32(9561692) + (load16u(v7 + 110) * 286704))
                v2 = (load32(v2 + 312) * load32(((load32(9561692) + (load16u(v7 + 110) * 286704)) + 284188)))
                # TODO: i32.div_u []
                v2 = ((load32(v2 + 312) * load32(((load32(9561692) + (load16u(v7 + 110) * 286704)) + 284188))) if (u(v2) < u(100)) else 100)
                v3 = load16u(arg1 + 110)
                v4 = load32(v4 + 278556)
                if load32(v4 + 278556):
                    v4 = (v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2))
                    store32((v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
                v3 = load32(((v9 + (v3 * 286704)) + 278564))
                if load32(((v9 + (v3 * 286704)) + 278564)):
                    v3 = (v3 + (((v10 * 255) + v5) << 2))
                    store32((v3 + (((v10 * 255) + v5) << 2)), (load32(v3) + v2))
                if (load8u(arg1 + 125) == 3):
                    break
                v3 = (arg1 - -64)
                v5 = load32(arg1 + 64)
                if (u(v2) >= u(load32(arg1 + 64))):
                    store32(v3, 0)
                    break
                store32(v3, (v5 - v2))
                if (load32(arg1 + 92) == 0):
                    break
                if load8u(9147141):
                    break
                store32(v6 + 32, v2)
                a_b()
                break
            arg1 = load32(9142440)
            break
        while True:  # block $label2
            if (u(arg1) <= u(v13)):
                break
            if (u(arg0) >= u(arg1)):
                break
            while True:  # block $label3
                arg1 = load32((load32(9142840) + ((v8 + (v12 * (arg1 + 2))) << 2)))
                if (u(load32((load32(9142840) + ((v8 + (v12 * (arg1 + 2))) << 2)))) < u(3)):
                    break
                arg1 = (load32(9671128) + (arg1 * 132))
                v5 = load8u((load32(9671128) + (arg1 * 132)) + 122)
                v2 = ((load8u((load32(9671128) + (arg1 * 132)) + 122) * 404) + 9568096)
                if (load32(((load8u((load32(9671128) + (arg1 * 132)) + 122) * 404) + 9568096) + 264) != 4):
                    break
                v9 = load32(9561692)
                v10 = load16u(v7 + 110)
                v4 = (load32(9561692) + (load16u(v7 + 110) * 286704))
                v2 = (load32(v2 + 312) * load32(((load32(9561692) + (load16u(v7 + 110) * 286704)) + 284188)))
                # TODO: i32.div_u []
                v2 = ((load32(v2 + 312) * load32(((load32(9561692) + (load16u(v7 + 110) * 286704)) + 284188))) if (u(v2) < u(100)) else 100)
                v3 = load16u(arg1 + 110)
                v4 = load32(v4 + 278556)
                if load32(v4 + 278556):
                    v4 = (v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2))
                    store32((v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
                v3 = load32(((v9 + (v3 * 286704)) + 278564))
                if load32(((v9 + (v3 * 286704)) + 278564)):
                    v3 = (v3 + (((v10 * 255) + v5) << 2))
                    store32((v3 + (((v10 * 255) + v5) << 2)), (load32(v3) + v2))
                if (load8u(arg1 + 125) == 3):
                    break
                v3 = (arg1 - -64)
                v5 = load32(arg1 + 64)
                if (u(v2) >= u(load32(arg1 + 64))):
                    store32(v3, 0)
                    break
                store32(v3, (v5 - v2))
                if (load32(arg1 + 92) == 0):
                    break
                if load8u(9147141):
                    break
                store32(v6 + 16, v2)
                a_b()
                break
            arg1 = load32(9142440)
            break
        while True:  # block $label4
            if (u(arg1) <= u(v12)):
                break
            if (u(arg0) >= u(arg1)):
                break
            while True:  # block $label5
                arg1 = load32((load32(9142840) + ((v8 + (v14 * (arg1 + 2))) << 2)))
                if (u(load32((load32(9142840) + ((v8 + (v14 * (arg1 + 2))) << 2)))) < u(3)):
                    break
                arg1 = (load32(9671128) + (arg1 * 132))
                v5 = load8u((load32(9671128) + (arg1 * 132)) + 122)
                v2 = ((load8u((load32(9671128) + (arg1 * 132)) + 122) * 404) + 9568096)
                if (load32(((load8u((load32(9671128) + (arg1 * 132)) + 122) * 404) + 9568096) + 264) != 4):
                    break
                v9 = load32(9561692)
                v10 = load16u(v7 + 110)
                v4 = (load32(9561692) + (load16u(v7 + 110) * 286704))
                v2 = (load32(v2 + 312) * load32(((load32(9561692) + (load16u(v7 + 110) * 286704)) + 284188)))
                # TODO: i32.div_u []
                v2 = ((load32(v2 + 312) * load32(((load32(9561692) + (load16u(v7 + 110) * 286704)) + 284188))) if (u(v2) < u(100)) else 100)
                v3 = load16u(arg1 + 110)
                v4 = load32(v4 + 278556)
                if load32(v4 + 278556):
                    v4 = (v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2))
                    store32((v4 + ((load8u(v7 + 122) + (v3 * 255)) << 2)), (load32(v4) + v2))
                v3 = load32(((v9 + (v3 * 286704)) + 278564))
                if load32(((v9 + (v3 * 286704)) + 278564)):
                    v3 = (v3 + (((v10 * 255) + v5) << 2))
                    store32((v3 + (((v10 * 255) + v5) << 2)), (load32(v3) + v2))
                if (load8u(arg1 + 125) == 3):
                    break
                v3 = (arg1 - -64)
                v5 = load32(arg1 + 64)
                if (u(v2) >= u(load32(arg1 + 64))):
                    store32(v3, 0)
                    break
                store32(v3, (v5 - v2))
                if (load32(arg1 + 92) == 0):
                    break
                if load8u(9147141):
                    break
                store32(v6, v2)
                a_b()
                break
            arg1 = load32(9142440)
            break
        if (arg0 != v15):
            continue
        break
    G.global0 = (v6 + 48)

# ------------------------------------------------------------
# $fe
# Export: fe
# ------------------------------------------------------------
def fe(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
    """Exported as fe."""
    while True:  # block $label0
        if (u(load32(9142892)) <= u(arg1)):
            break
        if (arg0 == load32(38624)):
            arg0 = (load32(39056) if (arg11 == 3) else (load32(38632) if (arg11 == 2) else (load32(38628) if (arg11 == 1) else arg0)))
        if (load32(38604) == arg0):
            arg0 = (load32(38616) if (arg11 == 3) else (load32(38612) if (arg11 == 2) else (load32(38608) if (arg11 == 1) else arg0)))
        arg0 = ((load32(38620) if (arg0 == load32(38560)) else arg0) if arg11 else arg0)
        arg0 = func34(((load32(38620) if (arg0 == load32(38560)) else arg0) if arg11 else arg0), arg1, arg2, arg3, ((arg4 if (arg0 == 7) else 0) if (load32(((arg0 * 404) + 9568096) + 264) == 1) else arg4), 1)
        if (func34(((load32(38620) if (arg0 == load32(38560)) else arg0) if arg11 else arg0), arg1, arg2, arg3, ((arg4 if (arg0 == 7) else 0) if (load32(((arg0 * 404) + 9568096) + 264) == 1) else arg4), 1) == 0):
            break
        arg1 = load32(9671128)
        arg2 = (load32(9671128) + (arg0 * 132))
        store32((load32(9671128) + (arg0 * 132)) + 60, arg6)
        store32(arg2 + 52, arg5)
        if arg7:
            store32(arg2 + 64, arg7)
        if arg8:
            store32((arg1 + (arg0 * 132)) + 68, arg8)
        arg0 = (arg1 + (arg0 * 132))
        store32((arg1 + (arg0 * 132)) + 72, arg10)
        store32(arg0 + 84, arg9)
        break

# ------------------------------------------------------------
# $ee
# Export: ee
# ------------------------------------------------------------
def ee(arg0, arg1, arg2):
    """Exported as ee."""
    v8 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    func182()
    arg0 = (arg0 + 1)
    store32(9142892, (arg0 + 1))
    store16(9147208, 1)
    v3 = load32(9561692)
    if load32(9561692):
    else:
    v14 = (i64(arg0) * 286704)
    v3 = (load32(9142892) if i32(((v14 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(arg0) * 286704)))
    arg0 = func26((load32(9142892) if i32(((v14 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(arg0) * 286704))))
    # TODO: memory.fill []
    store32(9561692, arg0)
    store8((arg0 + 283974), 255)
    store16(arg0 + 283972, 65535)
    store32(v8 + 16, arg2)
    v10 = load32(9142424)
    store32(load32(9142424) + 24, arg1)
    store32(v10, arg2)
    store8(9681940, 1)
    v6 = load32(9142892)
    v3 = (load32(9142892) * v6)
    v5 = func26((load32(9142892) * v6))
    # TODO: memory.fill []
    store32(9143004, v5)
    arg0 = func26(v3)
    # TODO: memory.fill []
    store32(9143012, arg0)
    while True:  # block $label0
        if (v3 == 0):
            break
        arg2 = 0
        arg0 = 0
        if (u(v3) >= u(4)):
            v7 = (v3 & -4)
            arg1 = 0
            while True:  # $label1
                store8((arg0 + v5), (load32(((arg0 << 2) + 9147392)) != 0))
                v4 = (arg0 | 1)
                store8((v5 + (arg0 | 1)), (load32(((v4 << 2) + 9147392)) != 0))
                v4 = (arg0 | 2)
                store8((v5 + (arg0 | 2)), (load32(((v4 << 2) + 9147392)) != 0))
                v4 = (arg0 | 3)
                store8((v5 + (arg0 | 3)), (load32(((v4 << 2) + 9147392)) != 0))
                arg0 = (arg0 + 4)
                arg1 = (arg1 + 4)
                if ((arg1 + 4) != v7):
                    continue
                break
        arg1 = (v3 & 3)
        if ((v3 & 3) == 0):
            break
        while True:  # $label2
            store8((arg0 + v5), (load32(((arg0 << 2) + 9147392)) != 0))
            arg0 = (arg0 + 1)
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != arg1):
                continue
            break
        break
    arg1 = func26(v3)
    # TODO: memory.fill []
    store32(9143008, arg1)
    if (u(v6) >= u(2)):
        arg0 = (v6 - 1)
        v12 = ((v6 - 1) & -4)
        v11 = (arg0 & 3)
        v13 = (u((v6 - 2)) < u(3))
        arg2 = 1
        while True:  # $label5
            v7 = (arg2 * v6)
            v4 = 0
            arg0 = 1
            if (v13 == 0):
                while True:  # $label3
                    store8((arg1 + (arg0 + v7)), (arg0 == arg2))
                    v9 = (arg0 + 1)
                    store8((arg1 + ((arg0 + 1) + v7)), (arg2 == v9))
                    v9 = (arg0 + 2)
                    store8((arg1 + ((arg0 + 2) + v7)), (arg2 == v9))
                    v9 = (arg0 + 3)
                    store8((arg1 + ((arg0 + 3) + v7)), (arg2 == v9))
                    arg0 = (arg0 + 4)
                    v4 = (v4 + 4)
                    if ((v4 + 4) != v12):
                        continue
                    break
            v4 = 0
            if v11:
                while True:  # $label4
                    store8((arg1 + (arg0 + v7)), (arg0 == arg2))
                    arg0 = (arg0 + 1)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v11):
                        continue
                    break
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != v6):
                continue
            break
    arg0 = func26(v3)
    # TODO: memory.fill []
    store32(9143016, arg0)
    arg2 = func26(v3)
    # TODO: memory.fill []
    store32(9143012, arg2)
    while True:  # block $label6
        if (v3 == 0):
            break
        arg1 = 0
        arg0 = 0
        if (u(v3) >= u(4)):
            v7 = (v3 & -4)
            v6 = 0
            while True:  # $label7
                store8((arg0 + arg2), (load8u((arg0 + v5)) ^ 1))
                v4 = (arg0 | 1)
                store8((arg2 + (arg0 | 1)), (load8u((v4 + v5)) ^ 1))
                v4 = (arg0 | 2)
                store8((arg2 + (arg0 | 2)), (load8u((v4 + v5)) ^ 1))
                v4 = (arg0 | 3)
                store8((arg2 + (arg0 | 3)), (load8u((v4 + v5)) ^ 1))
                arg0 = (arg0 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v7):
                    continue
                break
        v3 = (v3 & 3)
        if ((v3 & 3) == 0):
            break
        while True:  # $label8
            store8((arg0 + arg2), (load8u((arg0 + v5)) ^ 1))
            arg0 = (arg0 + 1)
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != v3):
                continue
            break
        break
    store32(v8, v10)
    store32(v8 + 4, load32(9142428))
    G.global0 = (v8 + 32)
    return v8

# ------------------------------------------------------------
# $ge
# Export: ge
# ------------------------------------------------------------
def ge(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
    """Exported as ge."""
    arg5 = (load32(9561692) + (arg0 * 286704))
    arg4 = (100 if arg4 else 0)
    store32((load32(9561692) + (arg0 * 286704)) + 286688, (100 if arg4 else 0))
    store32(arg5 + 286684, arg4)
    store32(arg5 + 283908, arg0)
    store32(arg5 + 283868, load32(9561460))
    # TODO: memory.copy []
    arg0 = load32(9142424)
    store32((arg5 + 284000), load32(load32(9142424) + 40))
    arg0 = load32(arg0 + 36)
    store32(arg5 + 283960, 3)
    store32((arg5 + 284136), arg0)
    store8((arg5 + 283974), arg3)
    store8((arg5 + 283973), arg2)
    store8(arg5 + 283972, arg1)
    store32((arg5 + 283860), arg9)
    store32((arg5 + 283856), arg8)
    store32((arg5 + 283852), arg7)
    store32(arg5 + 283848, arg6)
    while True:  # block $label0
        if (arg10 == 0):
            break
        arg0 = (arg10 & 3)
        if (u(arg10) >= u(4)):
            arg1 = (arg10 & -4)
            arg10 = 0
            while True:  # $label1
                store16((arg5 + (v11 << 1)), load32(((v11 << 2) + 9147392)))
                arg2 = (v11 | 1)
                store16((arg5 + ((v11 | 1) << 1)), load32(((arg2 << 2) + 9147392)))
                arg2 = (v11 | 2)
                store16((arg5 + ((v11 | 2) << 1)), load32(((arg2 << 2) + 9147392)))
                arg2 = (v11 | 3)
                store16((arg5 + ((v11 | 3) << 1)), load32(((arg2 << 2) + 9147392)))
                v11 = (v11 + 4)
                arg10 = (arg10 + 4)
                if ((arg10 + 4) != arg1):
                    continue
                break
        if (arg0 == 0):
            break
        arg10 = 0
        while True:  # $label2
            store16((arg5 + (v11 << 1)), load32(((v11 << 2) + 9147392)))
            v11 = (v11 + 1)
            arg10 = (arg10 + 1)
            if ((arg10 + 1) != arg0):
                continue
            break
        break

# ------------------------------------------------------------
# $vc
# Export: vc
# ------------------------------------------------------------
def vc():
    """Exported as vc."""
    v0 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    func231(v0)
    store32(v0 + 12, 1)
    func186((v0 + 44), v0, 78, 0)
    G.global0 = (v0 + 48)

# ------------------------------------------------------------
# $func476
# ------------------------------------------------------------
def func476(arg0, arg1):
    while True:  # block $label0
        v2 = load32(9671128)
        arg1 = (load32(9671128) + (arg0 * 132))
        if (load8u((load32(9671128) + (arg0 * 132)) + 125) == 3):
            break
        if (load8u(arg1 + 129) != 7):
            break
        arg0 = (v2 + (arg0 * 132))
        v2 = load32((v2 + (arg0 * 132)) + 88)
        if (load32((v2 + (arg0 * 132)) + 88) == 0):
            break
        v3 = load32(9142440)
        store32(arg0 + 80, 0)
        store32(arg0 + 88, 0)
        store8(arg1 + 129, 0)
        # TODO: i32.div_u []
        arg0 = v3
        break

# ------------------------------------------------------------
# $wa
# Export: wa
# ------------------------------------------------------------
def wa(arg0, arg1):
    """Exported as wa."""
    v4 = load32(9561692)
    while True:  # block $label0
        v5 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v2 = 1
        while True:  # $label1
            if (arg0 == load32((v4 + (v2 * 286704)) + 284616)):
                v3 = v2
                break
            v2 = (v2 + 1)
            if ((v2 + 1) != v5):
                continue
            break
        break
    store32((v4 + (v3 * 286704)) + 284604, arg1)

# ------------------------------------------------------------
# $fd
# Export: fd
# ------------------------------------------------------------
def fd():
    """Exported as fd."""
    v0 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v1 = (load32(9561692) + (load32(9142872) * 286704))
    store64(v0 + 16, load64(v0 + 32))
    store64(v0 + 24, load64(v0 + 40))
    v2 = load32((v1 + 284000))
    v3 = load32((v1 + 284136))
    v4 = load32(v1 + 283980)
    store32(v0, load32(v1 + 283976))
    v1 = (v3 + v4)
    store32(v0 + 4, (v2 if (u(v1) > u(v2)) else (v3 + v4)))
    G.global0 = (v0 + 48)

# ------------------------------------------------------------
# $cd
# Export: cd
# ------------------------------------------------------------
def cd(arg0, arg1):
    """Exported as cd."""
    arg1 = ((9684460 if (arg1 == 1) else 9684476) if arg1 else 9684444)
    store32(((9684460 if (arg1 == 1) else 9684476) if arg1 else 9684444) + 8, 0)
    v2 = load32(arg1 + 4)
    if (u(arg0) >= u(load32(arg1 + 4))):
        v2 = (load32(arg1 + 12) + (arg0 + v2))
        store32(arg1 + 4, (load32(arg1 + 12) + (arg0 + v2)))
        v3 = load32(arg1)
        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
        if v3:
        store32(arg1, v2)
    while True:  # block $label0
        if (arg0 == 0):
            break
        v6 = (arg0 & 1)
        v3 = load32(arg1)
        v2 = 0
        if (arg0 != 1):
            v7 = (arg0 & -2)
            arg0 = 0
            while True:  # $label1
                v4 = (v2 << 2)
                v5 = load32(((v2 << 2) + 9147392))
                v8 = load32(arg1 + 8)
                store32(arg1 + 8, (load32(arg1 + 8) + 1))
                store32((v3 + (v8 << 2)), v5)
                v4 = load32(((v4 | 4) + 9147392))
                v5 = load32(arg1 + 8)
                store32(arg1 + 8, (load32(arg1 + 8) + 1))
                store32((v3 + (v5 << 2)), v4)
                v2 = (v2 + 2)
                arg0 = (arg0 + 2)
                if ((arg0 + 2) != v7):
                    continue
                break
        if (v6 == 0):
            break
        arg0 = load32(((v2 << 2) + 9147392))
        arg1 = load32(arg1 + 8)
        store32(arg1 + 8, (load32(arg1 + 8) + 1))
        store32((v3 + (arg1 << 2)), arg0)
        break

# ------------------------------------------------------------
# $_c
# Export: _c
# ------------------------------------------------------------
def _c(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    """Exported as _c."""
    v10 = load32(9568088)
    store32(load32(9568088) + 36, arg6)
    store32(v10 + 32, arg5)
    store32(v10 + 16, arg4)
    store32(v10 + 12, arg3)
    store32(v10 + 8, arg2)
    store32(v10 + 4, arg1)
    store32(v10, arg0)
    store8(v10 + 45, arg8)
    store32(v10 + 28, arg7)
    store8(v10 + 44, arg9)

# ------------------------------------------------------------
# $za
# Export: za
# ------------------------------------------------------------
def za(arg0):
    """Exported as za."""
    v2 = load32(9142892)
    store32(9142892, arg0)
    v7 = (i64(arg0) * 286704)
    v1 = (-1 if i32(((v7 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(arg0) * 286704)))
    v5 = func26((-1 if i32(((v7 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(arg0) * 286704))))
    # TODO: memory.fill []
    v1 = load32(9561692)
    while True:  # block $label3
        while True:  # block $label1
            v2 = (v2 if (u(arg0) > u(v2)) else arg0)
            if (v2 if (u(arg0) > u(v2)) else arg0):
                if (u(v2) >= u(4)):
                    v6 = (v2 & -4)
                    arg0 = 0
                    while True:  # $label0
                        v4 = (v3 * 286704)
                        # TODO: memory.copy []
                        v4 = ((v3 | 1) * 286704)
                        # TODO: memory.copy []
                        v4 = ((v3 | 2) * 286704)
                        # TODO: memory.copy []
                        v4 = ((v3 | 3) * 286704)
                        # TODO: memory.copy []
                        v3 = (v3 + 4)
                        arg0 = (arg0 + 4)
                        if ((arg0 + 4) != v6):
                            continue
                        break
                v2 = (v2 & 3)
                if ((v2 & 3) == 0):
                    break
                arg0 = 0
                while True:  # $label2
                    v6 = (v3 * 286704)
                    # TODO: memory.copy []
                    v3 = (v3 + 1)
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v2):
                        continue
                    break
                break
            if (v1 == 0):
                break
            break
        break
    store32(9561692, v5)

# ------------------------------------------------------------
# $qd
# Export: qd
# ------------------------------------------------------------
def qd(arg0):
    """Exported as qd."""
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if load8u(9142916):
        v1 = load32(9142892)
        v12 = (v1 * 3)
        v2 = func26((-1 if (u((v1 * 3)) > u(1073741823)) else (load32(9142892) * 12)))
        while True:  # block $label0
            if (v1 == 0):
                break
            v6 = load32(9142872)
            v10 = (load32(9142872) * v1)
            v11 = load32(9143012)
            v8 = load32(9143004)
            v3 = load32(9561692)
            if (arg0 == 0):
                arg0 = 0
                while True:  # $label1
                    v9 = (v2 + (v4 << 2))
                    v5 = (v3 + (arg0 * 286704))
                    store32((v2 + (v4 << 2)), ((load16u((v3 + (arg0 * 286704)) + 283972) | (load8u((v5 + 283974)) << 16)) | -16777216))
                    store32(v9 + 4, load8u((v8 + ((load32(v5 + 283908) * v1) + v6))))
                    store32(v9 + 8, load8u((v11 + (load32(v5 + 283908) + v10))))
                    v4 = (v4 + 3)
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v1):
                        continue
                    break
                break
            store32(v2, ((load16u(v3 + 283972) | (load8u((v3 + 283974)) << 16)) | -16777216))
            store32(v2 + 4, load8u((v8 + ((load32(v3 + 283908) * v1) + v6))))
            store32(v2 + 8, load8u((v11 + (load32(v3 + 283908) + v10))))
            arg0 = 1
            if (v1 == 1):
                break
            v4 = 3
            while True:  # $label2
                v5 = (v2 + (v4 << 2))
                if (arg0 != v6):
                else:
                store32((-16776961 if load8u((v8 + (v6 + (arg0 * v1)))) else -16711936), -65536)
                v9 = (v3 + (arg0 * 286704))
                store32(v5 + 4, load8u((v8 + ((load32((v3 + (arg0 * 286704)) + 283908) * v1) + v6))))
                store32(v5 + 8, load8u((v11 + (load32(v9 + 283908) + v10))))
                v4 = (v4 + 3)
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v1):
                    continue
                break
            break
        store32(v7 + 4, v12)
        store32(v7, v2)
    G.global0 = (v7 + 16)
    return af(v2)

# ------------------------------------------------------------
# $func488
# ------------------------------------------------------------
def func488(arg0, arg1):
    arg0 = (load32(9671128) + (arg0 * 132))
    if (load8u((load32(9671128) + (arg0 * 132)) + 129) == 7):
        store8(arg0 + 129, 0)
    func202(arg0, 0, 0)
    func29(arg0, 1)

# ------------------------------------------------------------
# $func489
# ------------------------------------------------------------
def func489(arg0, arg1, arg2, arg3, arg4):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg4 = 0
    while True:  # block $label0
        arg0 = load8u((load32(9671128) + (arg0 * 132)) + 122)
        if (load32(((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096) + 212) != 1):
            break
        v5 = load32(arg2)
        v6 = load32(arg3)
        v7 = (load32(9142440) + 2)
        if (u((load32((load32(9142840) + ((load32(arg2) + (((load32(arg3) + (load32(9142440) + 2)) + 1) * v7)) << 2)) + 4) - 3)) > u(-3)):
            break
        store32(arg1 + 12, v5)
        store32(arg1 + 8, v6)
        if func167((arg1 + 12), (arg1 + 8), 1, 1, load32(((arg0 * 404) + 9568096) + 216)):
            store32(arg2, load32(arg1 + 12))
            store32(arg3, load32(arg1 + 8))
            break
        arg4 = 1
        break
    G.global0 = (arg1 + 16)
    return arg4

# ------------------------------------------------------------
# $func492
# ------------------------------------------------------------
def func492(arg0, arg1):
    v2 = load32(arg1 + 24)
    if (load32(arg1 + 24) == 0):
        v2 = func26(16)
        store64(func26(16), 0)
        store64(v2 + 8, 0)
        store32(arg1 + 24, v2)
    if (load32(v2 + 12) == 0):
        v3 = func26(16)
        store32(func26(16) + 4, 16)
        store32(v3, func26(64))
        store64(v3 + 8, 4294967296)
        store32(v2 + 12, v3)
        while True:  # $label1
            while True:  # block $label0
                v2 = load32(load32(arg1 + 24) + 12)
                v3 = load32(load32(load32(arg1 + 24) + 12) + 8)
                if (load32(load32(load32(arg1 + 24) + 12) + 8) != load32(v2 + 4)):
                    v4 = load32(v2)
                    break
                v4 = (load32(v2 + 12) + v3)
                store32(v2 + 4, (load32(v2 + 12) + v3))
                v5 = load32(v2)
                v4 = func26((-1 if (u(v4) > u(1073741823)) else (v4 << 2)))
                if v3:
                    # TODO: memory.copy []
                if v5:
                    v3 = load32(v2 + 8)
                store32(v2, v4)
                break
            store32(v2 + 8, (v3 + 1))
            store32((v4 + (v3 << 2)), 0)
            v6 = (v6 + 1)
            if ((v6 + 1) != 16):
                continue
            break
    arg1 = load32(load32(arg1 + 24) + 12)
    v2 = load32(arg0 + 8)
    if (u(load32(arg0 + 8)) >= u(16777216)):
        v2 = load32(((load32(arg1) + (v2 << 2)) - 67108864))
    v3 = load32(arg0 + 36)
    while True:  # block $label7
        while True:  # block $label6
            while True:  # block $label5
                while True:  # block $label4
                    while True:  # block $label3
                        while True:  # block $label2
                            # br_table[load32(arg0 + 28)]
                            break
                            break
                        store32((load32(arg1) + (v3 << 2)), v2)
                        return
                        break
                    arg0 = (load32(arg1) + (v3 << 2))
                    store32((load32(arg1) + (v3 << 2)), (load32(arg0) + v2))
                    return
                    break
                arg0 = (load32(arg1) + (v3 << 2))
                store32((load32(arg1) + (v3 << 2)), (load32(arg0) - v2))
                return
                break
            arg0 = (load32(arg1) + (v3 << 2))
            store32((load32(arg1) + (v3 << 2)), (load32(arg0) * v2))
            return
            break
        arg0 = (load32(arg1) + (v3 << 2))
        # TODO: i32.div_u []
        store32(load32(arg0), v2)
        break

# ------------------------------------------------------------
# $func493
# ------------------------------------------------------------
def func493(arg0, arg1):
    v2 = load32(9671128)
    arg1 = (load32(9671128) + (arg0 * 132))
    store8((load32(9671128) + (arg0 * 132)) + 126, 0)
    # TODO: i32.div_u []
    store32(load32(arg1 + 52) + 52, ((load32(((load8u(arg1 + 122) * 404) + 9568096) + 296) * load32(((load32(9561692) + (load16u(arg1 + 110) * 286704)) + 284144))) - 100))
    while True:  # block $label0
        if (load32(arg1 + 92) == 0):
            break
        if load32(9140316):
            if (load32(9140320) != load32((v2 + (arg0 * 132)) + 28)):
                break
        break

# ------------------------------------------------------------
# $xe
# Export: xe
# ------------------------------------------------------------
def xe():
    """Exported as xe."""
    return load32(9687252)

# ------------------------------------------------------------
# $func495
# ------------------------------------------------------------
def func495(arg0, arg1, param2):
    v9 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v4 = load32(9671128)
    while True:  # block $label0
        if (u(load32(9142848)) < u((load32(load32(9142424) + 72) * 2400))):
            func29((v4 + (arg0 * 132)), 1)
            break
        while True:  # block $label1
            v3 = (arg0 * 132)
            v2 = (v4 + (arg0 * 132))
            if (load8u((v4 + (arg0 * 132)) + 125) == 3):
                break
            if (load8u(v2 + 128) == 0):
                break
            v4 = (v4 + (arg0 * 132))
            store8((v4 + (arg0 * 132)) + 127, 0)
            while True:  # block $label2
                v5 = load32(v4 + 40)
                if (load32(v4 + 40) == 0):
                    break
                if load8u(9142916):
                    store32(v9 + 20, v5)
                    store32(v9 + 16, 0)
                    a_b()
                    break
                v4 = load16u(v4 + 110)
                store32(v9 + 4, v5)
                store32(v9, (v4 + 16))
                a_b()
                break
            store8(v2 + 128, 0)
            v4 = load32(9671128)
            break
        v10 = (v3 + v4)
        v2 = (v4 + (arg1 * 132))
        if (load8u((v4 + (arg1 * 132)) + 125) == 3):
            func29(v10, 1)
            break
        v8 = (v4 + (arg1 * 132))
        v5 = load16u((v4 + (arg1 * 132)) + 112)
        v6 = (v4 + (arg0 * 132))
        if (load8u((v4 + (arg0 * 132)) + 125) == 1):
            v3 = load16u(v6 + 114)
            v2 = load16u(v8 + 114)
            while True:  # block $label4
                while True:  # block $label3
                    v8 = load16u(v6 + 112)
                    if (v5 != load16u(v6 + 112)):
                        break
                    if (u(v2) > u(v3)):
                        break
                    if (u(v2) < u(v3)):
                        break
                    v8 = 0
                    break
                    break
                v8 = (1 if (u(v5) > u(v8)) else (-1 if (u(v5) < u(v8)) else 0))
                break
            v3 = (1 if (u(v2) > u(v3)) else (-1 if (u(v2) < u(v3)) else 0))
            v7 = 6
            v3 = (((v3 * 3) + v8) + 4)
            if (u((((v3 * 3) + v8) + 4)) <= u(8)):
                v7 = load8u((v3 + 10184))
            v3 = (v4 + (arg0 * 132))
            store8((v4 + (arg0 * 132)) + 124, v7)
            if (arg0 != arg1):
            v2 = load32(((load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) * 40) + 9671200) + 32):
                # call_indirect[v2]
            while True:  # block $label5
                if (load8u(v6 + 125) == 3):
                    break
                v5 = load32(v3 + 44)
                if load32(v3 + 44):
                    v10 = load32(9142848)
                    v2 = load32(9215884)
                    store32((load32(9215884) + (v5 << 4)) + 4, 40)
                    store32((v2 + (load32(v3 + 44) << 4)) + 8, load32((v4 + (arg0 * 132)) + 28))
                    store32((v2 + (load32(v3 + 44) << 4)) + 12, arg1)
                    store32((v2 + (load32(v3 + 44) << 4)), (v10 + 28))
                    break
                store32(v3 + 44, ((Ua(700, 40, load32((v4 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
                break
            store32((v4 + (arg1 * 132)) + 104, arg0)
            break
        v3 = load16u(v8 + 114)
        while True:  # block $label8
            while True:  # block $label7
                while True:  # block $label6
                    v11 = load32(load32(9142424) + 48)
                    if load32(load32(9142424) + 48):
                        if (load8u(9147152) == 0):
                            break
                    v6 = load32(9142440)
                    break
                    break
                v6 = load32(9142440)
                v7 = load16u((load32(9147376) + (((load32(9142440) * v3) + v5) << 1)))
                if (v11 == 2):
                    if (u(v7) > u(1)):
                        break
                    break
                if (v7 == 0):
                    break
                break
            # TODO: f32.convert_i32_u []
            # TODO: f32.convert_i32_u []
            # TODO: f32.convert_i32_u []
            func80(v5, v3, load32(9142580), 32.0, (v6 * 96))
            break
        v5 = (G.global0 - 32)
        G.global0 = (G.global0 - 32)
        store8(v2 + 127, 5)
        while True:  # block $label9
            if (load8u(9142916) == 0):
                break
            v3 = load32(v2 + 40)
            if (load32(v2 + 40) == 0):
                break
            store32(v5 + 20, v3)
            store32(v5 + 16, -11842741)
            a_b()
            break
        while True:  # block $label10
            v3 = load16u(v2 + 112)
            v6 = ((load16u(v2 + 112) << 5) - load32(9142952))
            v6 = load16u(v2 + 114)
            v7 = ((load16u(v2 + 114) << 5) - load32(9142956))
            if ((((((load16u(v2 + 112) << 5) - load32(9142952)) * v6) + (((load16u(v2 + 114) << 5) - load32(9142956)) * v7)) - 1) > 9000000):
                break
            v11 = load32(39888)
            while True:  # block $label11
                v12 = load32(load32(9142424) + 48)
                if (load32(load32(9142424) + 48) == 0):
                    break
                if load8u(9147152):
                    break
                v7 = load16u((load32(9147376) + (((load32(9142440) * v6) + v3) << 1)))
                if (v12 == 2):
                    if (u(v7) > u(1)):
                        break
                    break
                if (v7 == 0):
                    break
                break
            store32(v5 + 8, v6)
            store32(v5 + 4, v3)
            store32(v5, v11)
            a_b()
            break
        func119(v5, v2, 0, 1)
        store8(v2 + 125, 10)
        func63(1738, v2, 20, 0, load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284220)))
        func77(v2)
        G.global0 = (v5 + 32)
        store32((v4 + (arg1 * 132)) + 104, 0)
        if (arg0 == arg1):
            break
        v2 = load8u((v4 + (arg0 * 132)) + 129)
        if ((load8u((v4 + (arg0 * 132)) + 129) & 254) == 14):
            arg0 = func301(load16u(v8 + 112), load16u(v8 + 114), load16u((v4 + (arg0 * 132)) + 110), (-1 if (v2 != 15) else load8u((v4 + (arg1 * 132)) + 122)))
            if func301(load16u(v8 + 112), load16u(v8 + 114), load16u((v4 + (arg0 * 132)) + 110), (-1 if (v2 != 15) else load8u((v4 + (arg1 * 132)) + 122))):
                break
            func29(v10, 1)
            break
        func29(v10, 1)
        break
    G.global0 = (v9 + 32)
    return (v5 + 16)

# ------------------------------------------------------------
# $func496
# ------------------------------------------------------------
def func496(arg0, arg1, arg2, arg3, arg4):
    return (load32(((load8u((load32(9671128) + (load32(arg1) * 132)) + 122) * 404) + 9568096) + 340) == 0)

# ------------------------------------------------------------
# $func497
# ------------------------------------------------------------
def func497(arg0):
    while True:  # block $label0
        v1 = load8u(arg0 + 129)
        if ((load8u(arg0 + 129) & 254) != 14):
            break
        v1 = func301(load16u(arg0 + 112), load16u(arg0 + 114), load16u(arg0 + 110), (-1 if (v1 != 15) else load8u((load32(9671128) + (load32(arg0 + 32) * 132)) + 122)))
        if (func301(load16u(arg0 + 112), load16u(arg0 + 114), load16u(arg0 + 110), (-1 if (v1 != 15) else load8u((load32(9671128) + (load32(arg0 + 32) * 132)) + 122))) == 0):
            break
        store32(arg0 + 32, v1)
        break
    return 0

# ------------------------------------------------------------
# $ue
# Export: ue
# ------------------------------------------------------------
def ue():
    """Exported as ue."""
    return load32(9147296)

# ------------------------------------------------------------
# $te
# Export: te
# ------------------------------------------------------------
def te():
    """Exported as te."""
    return load32(9147292)

# ------------------------------------------------------------
# $nd
# Export: nd
# ------------------------------------------------------------
def nd(arg0):
    """Exported as nd."""
    while True:  # block $label0
        if (arg0 == 0):
            break
        v1 = load32(9681936)
        if (load32(9681936) == 0):
            break
        if load32(v1 + 8):
            arg0 = 0
            while True:  # $label1
                func38(load32((load32(v1) + ((arg0 << 2) | 12))))
                arg0 = (arg0 + 4)
                v1 = load32(9681936)
                if (u((arg0 + 4)) < u(load32(load32(9681936) + 8))):
                    continue
                break
        store32(v1 + 8, 0)
        break
    return load32(9147288)

# ------------------------------------------------------------
# $func501
# ------------------------------------------------------------
def func501(arg0):
    while True:  # block $label0
        if (arg0 == 0):
            break
        v1 = load32(9671128)
        v2 = (load32(9671128) + (arg0 * 132))
        if load8u((load32(9143004) + (load32(9142872) + (load32(9142892) * load16u((load32(9671128) + (arg0 * 132)) + 110))))):
            break
        while True:  # block $label1
            # br_table[(load8u(v2 + 125) - 4)]
            break
            break
        while True:  # block $label2
            v1 = load8u((v1 + (arg0 * 132)) + 122)
            if (load8u((v1 + (arg0 * 132)) + 122) == load32(38552)):
                break
            if (load32(38892) == v1):
                break
            if (load32(38816) == v1):
                break
            if (load32(38872) == v1):
                break
            if (load32(38584) == v1):
                break
            if (load32(38796) != v1):
                break
            break
        store32((9681808 if load8u(9681824) else 9681812), arg0)
        break

# ------------------------------------------------------------
# $nb
# Export: nb
# ------------------------------------------------------------
def nb(arg0):
    """Exported as nb."""
    v1 = (load32(9671128) + (load32(9173808) * 132))
    arg0 = load32(((load32(9561692) + (load16u((load32(9671128) + (load32(9173808) * 132)) + 110) * 286704)) + 284340))
    v2 = (load32(9681804) + ((arg0 * load32(((load32(9561692) + (load16u((load32(9671128) + (load32(9173808) * 132)) + 110) * 286704)) + 284340))) * ((load8u(9163792) + 1) & 255)))
    store32(9681804, (load32(9681804) + ((arg0 * load32(((load32(9561692) + (load16u((load32(9671128) + (load32(9173808) * 132)) + 110) * 286704)) + 284340))) * ((load8u(9163792) + 1) & 255))))
    while True:  # block $label0
        v1 = load32(((load8u(v1 + 122) * 404) + 9568096) + 124)
        if (u(load32(((load8u(v1 + 122) * 404) + 9568096) + 124)) >= u(v2)):
            v1 = arg0
            if (u(v2) >= u(arg0)):
                break
        store32(9681804, v1)
        break

# ------------------------------------------------------------
# $ob
# Export: ob
# ------------------------------------------------------------
def ob(arg0, arg1):
    """Exported as ob."""
    if arg1:
        arg0 = ((load32(9681816) + arg0) & 3)
        store32(9681816, ((load32(9681816) + arg0) & 3))
        return arg0
    arg0 = ((load32(9681820) + arg0) & 3)
    store32(9681820, ((load32(9681820) + arg0) & 3))
    return arg0

# ------------------------------------------------------------
# $func504
# ------------------------------------------------------------
def func504(arg0):
    while True:  # block $label1
        while True:  # block $label0
            arg0 = load32((load32(9671128) + (load32(9173808) * 132)) + 20)
            if (load32((load32(9671128) + (load32(9173808) * 132)) + 20) == 0):
                break
            if (u(load32(arg0 + 8)) < u(3)):
                break
            arg0 = load32(arg0)
            if load32(load32(arg0)):
                break
            store32(9681804, load32(arg0 + 4))
            store32(9681808, load32(arg0 + 8))
            store32(9681812, load32(arg0 + 12))
            store32(9681816, load32(arg0 + 16))
            v1 = load32(arg0 + 20)
            break
            break
        store32(9681804, 50)
        store32(9681808, 0)
        store32(9681812, 0)
        store32(9681816, 0)
        break
    store32(9681820, v1)

# ------------------------------------------------------------
# $func505
# ------------------------------------------------------------
def func505(arg0, arg1, param2):
    v6 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label0
        v4 = load32(9671128)
        v8 = (load32(9671128) + (arg0 * 132))
        v3 = load32((load32(9671128) + (arg0 * 132)) + 20)
        if (load32((load32(9671128) + (arg0 * 132)) + 20) == 0):
            break
        v2 = load32(v3 + 8)
        if (u(load32(v3 + 8)) < u(3)):
            break
        v7 = load32(v3)
        if load32(load32(v3)):
            break
        v10 = (v4 + (arg0 * 132))
        v5 = load16u((v4 + (arg0 * 132)) + 88)
        v9 = load32(v7 + 8)
        v15 = (load32(v7 + 8) == arg1)
        v11 = load32((v7 + (16 if (load32(v7 + 8) == arg1) else 20)))
        v12 = load32(9561692)
        v13 = load16u((v4 + (arg1 * 132)) + 110)
        v16 = (load32(9561692) + (load16u((v4 + (arg1 * 132)) + 110) * 286704))
        if (load8u(v10 + 125) == 1):
            while True:  # block $label1
                while True:  # block $label2
                    if (v2 == 7):
                        store32(v3 + 8, 6)
                        v2 = (v5 << 2)
                        if (load32(((v5 << 2) + (v6 + 16))) == 2147483647):
                            break
                        v3 = (((v12 + (v13 * 286704)) + v2) + 283848)
                        v2 = load16u((v4 + (arg0 * 132)) + 108)
                        break
                    v2 = (v4 + (arg0 * 132))
                    v3 = load16u((v4 + (arg0 * 132)) + 108)
                    if (load16u((v4 + (arg0 * 132)) + 108) == 0):
                        break
                    v17 = 0.800000012
                    v2 = (v12 + (load16u(v2 + 110) * 286704))
                    if (load32((((v12 + (load16u(v2 + 110) * 286704)) + (load32(39108) << 2)) + 281808)) != 1):
                        v17 = (0.800000012 if (load32(((v2 + (load32(39168) << 2)) + 281808)) == 1) else 0.75)
                    if (load32(((v6 + 16) + (v5 << 2))) == 2147483647):
                        break
                    while True:  # block $label3
                        v2 = (v4 + (v9 * 132))
                        v9 = (v4 + (load32(v7 + 12) * 132))
                        v14 = (load16u((v4 + (v9 * 132)) + 112) - load16u((v4 + (load32(v7 + 12) * 132)) + 112))
                        v2 = (load16u(v2 + 114) - load16u(v9 + 114))
                        # TODO: f32.convert_i32_u []
                        # TODO: f64.promote_f32 []
                        v18 = (((sqrt(float((((load16u((v4 + (v9 * 132)) + 112) - load16u((v4 + (load32(v7 + 12) * 132)) + 112)) * v14) + ((load16u(v2 + 114) - load16u(v9 + 114)) * v2)))) * (v17 * load32(v7 + 4))) / 500.0) + 0.5)
                        if (((((sqrt(float((((load16u((v4 + (v9 * 132)) + 112) - load16u((v4 + (load32(v7 + 12) * 132)) + 112)) * v14) + ((load16u(v2 + 114) - load16u(v9 + 114)) * v2)))) * (v17 * load32(v7 + 4))) / 500.0) + 0.5) < 4294967296.0) & (v18 >= 0.0)):
                            # TODO: i32.trunc_f64_u []
                            break
                        break
                    v2 = 0
                    v7 = ((v12 + (v13 * 286704)) + (v5 << 2))
                    v5 = (((v12 + (v13 * 286704)) + (v5 << 2)) + 283848)
                    store32((((v12 + (v13 * 286704)) + (v5 << 2)) + 283848), ((load32(v5) + v3) + v2))
                    v3 = (v7 + 281676)
                    break
                store32(v3, (load32(v3) + v2))
                break
            v2 = (v4 + (arg0 * 132))
            store16((v4 + (arg0 * 132)) + 108, 0)
            store32(v10 + 88, ((load8u((v4 + (arg1 * 132)) + 122) << 16) + v11))
            while True:  # block $label4
                if (load32(v2 + 92) == 0):
                    break
                if load32(9140316):
                    if (load32(9140320) != load32((v4 + (arg0 * 132)) + 28)):
                        break
                break
            v3 = load32(v8 + 20)
        else:
        if (v2 == 7):
            store32(v3 + 8, 6)
        v2 = (v4 + (arg1 * 132))
        v7 = (v4 + (arg1 * 132))
        while True:  # block $label6
            while True:  # block $label5
                v2 = load32(v2 + 56)
                if (load32(v2 + 56) == 0):
                    break
                v5 = load32(9215884)
                v9 = load32((load32(9671128) + (v2 * 132)) + 44)
                if (load32((load32(9215884) + (load32((load32(9671128) + (v2 * 132)) + 44) << 4)) + 12) != arg1):
                    break
                if (load32((v5 + ((v9 << 4) | 4))) == 60):
                    break
                break
            store32(v7 + 56, arg0)
            v2 = arg0
            break
        while True:  # block $label7
            v14 = load32(((v6 + 16) + (v11 << 2)))
            v5 = load32(((load32(9561692) + (load16u((v4 + (arg0 * 132)) + 110) * 286704)) + 284344))
            if (u(load32(((v6 + 16) + (v11 << 2)))) < u(load32(((load32(9561692) + (load16u((v4 + (arg0 * 132)) + 110) * 286704)) + 284344)))):
                break
            if (arg0 != v2):
                break
            v2 = (v4 + (arg0 * 132))
            v9 = (load16u(v2 + 108) + v5)
            store16((v4 + (arg0 * 132)) + 108, (load16u(v2 + 108) + v5))
            if (v14 != 2147483647):
                store64(v6 + 8, 0)
                store64(v6, 0)
                v3 = (v11 << 2)
                store32((v6 + (v11 << 2)), v5)
                v5 = load32(load32(load32(v8 + 20)) + 4)
                v11 = load16u(v2 + 108)
                if (u(load32(load32(load32(v8 + 20)) + 4)) <= u(load16u(v2 + 108))):
                    v3 = (((v12 + (v13 * 286704)) + v3) + 283848)
                    store32((((v12 + (v13 * 286704)) + v3) + 283848), (load32(v3) + (v11 - v5)))
                v9 = load16u(v2 + 108)
            else:
            v3 = load32(load32(v3) + 4)
            if (u(load32(load32(v3) + 4)) <= u((v9 & 65535))):
                store16(v2 + 108, v3)
                while True:  # block $label8
                    if (load32((v4 + (arg0 * 132)) + 92) == 0):
                        break
                    if load32(9140316):
                        if (load32(9140320) != load32((v4 + (arg0 * 132)) + 28)):
                            break
                    break
                store32(v7 + 56, 0)
                store8(v10 + 125, 0)
                break
            if (load32((v4 + (arg0 * 132)) + 92) == 0):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v4 + (arg0 * 132)) + 28)):
                    break
            break
        if (load8u(v10 + 125) == 1):
            v2 = (v4 + (arg0 * 132))
            v3 = load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
                # call_indirect[v3]
                if (load8u(v10 + 125) == 3):
                    break
            v8 = load32(v2 + 44)
            if load32(v2 + 44):
                v10 = load32(9142848)
                v3 = load32(9215884)
                store32((load32(9215884) + (v8 << 4)) + 4, 60)
                store32((v3 + (load32(v2 + 44) << 4)) + 8, load32((v4 + (arg0 * 132)) + 28))
                store32((v3 + (load32(v2 + 44) << 4)) + 12, arg1)
                store32((v3 + (load32(v2 + 44) << 4)), (v10 + 40))
                break
            store32(v2 + 44, ((Ua(1000, 60, load32((v4 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        store32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
        break
    G.global0 = (v6 + 32)
    return indirect_call(v3)

# ------------------------------------------------------------
# $func506
# ------------------------------------------------------------
def func506(arg0):
    v1 = 1
    while True:  # block $label0
        v2 = load32(9671128)
        v3 = load32(arg0 + 32)
        v4 = (load32(9671128) + (load32(arg0 + 32) * 132))
        v5 = load8u((load32(9671128) + (load32(arg0 + 32) * 132)) + 125)
        if (load8u((load32(9671128) + (load32(arg0 + 32) * 132)) + 125) == 3):
            break
        if load8u((load32(9143004) + (load16u(arg0 + 110) + (load32(9142892) * load16u(v4 + 110))))):
            break
        while True:  # block $label1
            # br_table[(v5 - 4)]
            break
            break
        while True:  # block $label2
            arg0 = load8u((v2 + (v3 * 132)) + 122)
            if (load8u((v2 + (v3 * 132)) + 122) == load32(38552)):
                break
            if (load32(38892) == arg0):
                break
            if (load32(38816) == arg0):
                break
            if (load32(38872) == arg0):
                break
            if (load32(38584) == arg0):
                break
            if (load32(38796) != arg0):
                break
            break
        v1 = 0
        break
    return v1

# ------------------------------------------------------------
# $func508
# ------------------------------------------------------------
def func508(arg0, arg1, arg2):
    if arg2:
        while True:  # $label4
            while True:  # block $label0
                arg0 = (load32(9671128) + (load32((arg1 + (v5 << 2))) * 132))
                v6 = load8u((load32(9671128) + (load32((arg1 + (v5 << 2))) * 132)) + 122)
                v3 = ((load8u((load32(9671128) + (load32((arg1 + (v5 << 2))) * 132)) + 122) * 404) + 9568096)
                v4 = load8u(9147152)
                if (0 if load8u(9147152) else load8u(((load8u((load32(9671128) + (load32((arg1 + (v5 << 2))) * 132)) + 122) * 404) + 9568096) + 332)):
                    break
                while True:  # block $label1
                    if v4:
                        break
                    if (load32(v3 + 264) == 1):
                        if (u(load32(arg0 + 84)) < u(load32(v3 + 112))):
                            break
                    v4 = load16u(arg0 + 110)
                    v3 = load32(9561692)
                    while True:  # block $label2
                        if (load32(9147132) == 0):
                            break
                        if (load32(9142440) != 4096):
                            break
                        if (load32(9671152) != v6):
                            break
                        if (u(load32((v3 + (v4 * 286704)) + 283976)) > u(1)):
                            break
                        break
                    v3 = load32(((v3 + (v4 * 286704)) + 278568))
                    if (load32(((v3 + (v4 * 286704)) + 278568)) == 0):
                        break
                    while True:  # block $label3
                        # br_table[(load8u(arg0 + 125) - 4)]
                        break
                        break
                    v4 = (v3 + (((v4 * 255) + v6) << 2))
                    store32((v3 + (((v4 * 255) + v6) << 2)), (load32(v4) + 1))
                    break
                break
            v5 = (v5 + 1)
            if ((v5 + 1) != arg2):
                continue
            break

# ------------------------------------------------------------
# $ya
# Export: ya
# ------------------------------------------------------------
def ya(arg0):
    """Exported as ya."""
    if load8u(9142388):
        store8(9561848, arg0)
        xa()

# ------------------------------------------------------------
# $od
# Export: od
# ------------------------------------------------------------
def od(arg0, arg1):
    """Exported as od."""
    store8(9671156, 1)

# ------------------------------------------------------------
# $ie
# Export: ie
# ------------------------------------------------------------
def ie(arg0, arg1, arg2):
    """Exported as ie."""
    store8(59180, (arg1 != 0))
    return load32(9215884)

# ------------------------------------------------------------
# $ca
# Export: ca
# ------------------------------------------------------------
def ca(arg0):
    """Exported as ca."""
    v1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
    store32(9561732, arg0)
    store32(9561728, v1)
    return v1

# ------------------------------------------------------------
# $func516
# ------------------------------------------------------------
def func516(arg0, arg1):
    v12 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if (load8u(arg1 + 125) == 3):
            break
        while True:  # block $label9
            while True:  # block $label5
                while True:  # block $label6
                    while True:  # block $label4
                        while True:  # block $label3
                            while True:  # block $label2
                                while True:  # block $label1
                                    # br_table[load32(arg0 + 8)]
                                    break
                                    break
                                v5 = load32(arg0 + 20)
                                v6 = load32(arg0 + 28)
                                v4 = load32(arg0 + 24)
                                v8 = load32(arg0 + 40)
                                arg0 = load32(9147324)
                                store32(9147324, load32(9147316))
                                v3 = load32(9147320)
                                v2 = load32(9147312)
                                store32(9147320, load32(9147312))
                                arg0 = (arg0 ^ (arg0 << 11))
                                v2 = ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((arg0 ^ (arg0 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg0)
                                store32(9147316, ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((arg0 ^ (arg0 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg0))
                                arg0 = (v3 ^ (v3 << 11))
                                arg0 = ((((((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ v2)
                                store32(9147312, ((((((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ arg0) ^ v2))
                                arg0 = (v4 + (arg0 % v8))
                                break
                                break
                            v2 = load32(arg0 + 36)
                            store64(v12 + 8, load64(arg0 + 72))
                            store64(v12, load64(arg0 + 64))
                            v4 = func300(v2, v12, arg1)
                            break
                            break
                        v5 = load32(arg0 + 104)
                        if (load32(arg0 + 104) == 0):
                            break
                        v6 = load32(arg0 + 96)
                        v8 = load16u(arg1 + 114)
                        v9 = load16u(arg1 + 112)
                        v11 = load32(9671128)
                        v7 = load32(arg1 + 28)
                        v2 = 2147483647
                        arg0 = 0
                        while True:  # $label7
                            v3 = load32((v6 + (arg0 << 2)))
                            if (v7 != load32((v6 + (arg0 << 2)))):
                                v3 = (v11 + (v3 * 132))
                                v10 = ((load16u((v11 + (v3 * 132)) + 114) - v8) << 1)
                                v10 = ((load16u(v3 + 112) - v9) << 1)
                                v10 = ((((load16u((v11 + (v3 * 132)) + 114) - v8) << 1) * v10) + (((load16u(v3 + 112) - v9) << 1) * v10))
                                v10 = (v2 > v10)
                                v2 = (((((load16u((v11 + (v3 * 132)) + 114) - v8) << 1) * v10) + (((load16u(v3 + 112) - v9) << 1) * v10)) if (v2 > v10) else v2)
                                v4 = (load32(v3 + 28) if v10 else v4)
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v5):
                                continue
                            break
                        break
                        break
                    v5 = load32(9140300)
                    if (load32(9140300) == 0):
                        break
                    v6 = load16u(arg1 + 114)
                    v8 = load16u(arg1 + 112)
                    v9 = load32(9671128)
                    v11 = load32(arg1 + 28)
                    v2 = 2147483647
                    arg0 = 0
                    while True:  # $label8
                        v3 = load32(((arg0 << 2) + 8451904))
                        if (v11 != load32(((arg0 << 2) + 8451904))):
                            v3 = (v9 + (v3 * 132))
                            v7 = ((load16u((v9 + (v3 * 132)) + 114) - v6) << 1)
                            v7 = ((load16u(v3 + 112) - v8) << 1)
                            v7 = ((((load16u((v9 + (v3 * 132)) + 114) - v6) << 1) * v7) + (((load16u(v3 + 112) - v8) << 1) * v7))
                            v7 = (v2 > v7)
                            v2 = (((((load16u((v9 + (v3 * 132)) + 114) - v6) << 1) * v7) + (((load16u(v3 + 112) - v8) << 1) * v7)) if (v2 > v7) else v2)
                            v4 = (load32(v3 + 28) if v7 else v4)
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != v5):
                            continue
                        break
                    break
                if (v4 == 0):
                    break
                v2 = (load32(9671128) + (v4 * 132))
                arg0 = load16u((load32(9671128) + (v4 * 132)) + 114)
                break
            v5 = load16u(v2 + 112)
            v8 = ((load8u(arg1 + 122) * 404) + 9568096)
            v9 = load16u(arg1 + 110)
            if func56(load16u(v2 + 112), arg0, ((load8u(arg1 + 122) * 404) + 9568096), load16u(arg1 + 110), 0, 0, 1, 1, 0):
                v2 = v5
                v3 = arg0
                break
            v4 = load32(9142440)
            v2 = 0
            while True:  # $label11
                while True:  # block $label10
                    v6 = v2
                    v2 = (v2 << 2)
                    v3 = (load32((((v2 << 2) | 4) + 8611904)) + arg0)
                    if (u(v4) <= u((load32((((v2 << 2) | 4) + 8611904)) + arg0))):
                        break
                    v2 = (load32((v2 + 8611904)) + v5)
                    if (u(v4) <= u((load32((v2 + 8611904)) + v5))):
                        break
                    if ((v2 | v3) < 0):
                        break
                    if func56(v2, v3, v8, v9, 0, 0, 1, 1, 0):
                        break
                    v4 = load32(9142440)
                    break
                v2 = (v6 + 2)
                if (u(v6) < u(5198)):
                    continue
                break
            break
            break
        arg0 = load32(arg1 + 20)
        if load32(arg1 + 20):
            store32(arg0 + 8, 0)
        store32(arg1 + 32, 0)
        store8(arg1 + 129, 0)
        if load32(arg1 + 36):
        while True:  # block $label12
            v5 = load8u(arg1 + 125)
            if (load8u(arg1 + 125) == 13):
                break
            if (load8u(59181) == 0):
                break
            arg0 = load32(arg1 + 44)
            if (load32(arg1 + 44) == 0):
                break
            v6 = load32(9215884)
            if (load32((load32(9215884) + (arg0 << 4)) + 12) == 1):
                break
            if (v5 == 7):
                break
            if load32((v6 + ((arg0 << 4) | 4))):
                break
            arg0 = (load8u(arg1 + 124) << 3)
            break
        arg0 = load32(arg1 + 44)
        if load32(arg1 + 44):
            store32((load32(9215884) + (arg0 << 4)), 0)
        store32(arg1 + 44, 0)
        if (load8u(arg1 + 125) == 13):
            store16(arg1 + 114, v3)
            store16(arg1 + 112, v2)
            break
        v5 = ((load8u(arg1 + 122) * 404) + 9568096)
        if load32(((load8u(arg1 + 122) * 404) + 9568096) + 216):
            v4 = load32(9142840)
            v8 = load16u(arg1 + 114)
            v9 = load16u(arg1 + 112)
            v6 = 0
            while True:  # $label14
                v6 = (v6 + 1)
                v11 = ((v6 + 1) + v9)
                arg0 = 0
                while True:  # $label13
                    arg0 = (arg0 + 1)
                    v7 = (load32(9142440) + 2)
                    store32((v4 + ((v11 + ((((arg0 + 1) + v8) + ((load32(9142440) + 2) * load32(v5 + 208))) * v7)) << 2)), load32(v5 + 212))
                    v7 = load32(v5 + 216)
                    if (u(arg0) < u(load32(v5 + 216))):
                        continue
                    break
                if (u(v6) < u(v7)):
                    continue
                break
        store16(arg1 + 114, v3)
        store16(arg1 + 112, v2)
        if (load8u(arg1 + 125) == 13):
            break
        v5 = ((load8u(arg1 + 122) * 404) + 9568096)
        if load32(((load8u(arg1 + 122) * 404) + 9568096) + 216):
            v3 = (v3 & 65535)
            v6 = (v2 & 65535)
            v4 = load32(9142840)
            v2 = 0
            while True:  # $label16
                v2 = (v2 + 1)
                v8 = ((v2 + 1) + v6)
                arg0 = 0
                while True:  # $label15
                    arg0 = (arg0 + 1)
                    v9 = (load32(9142440) + 2)
                    store32((v4 + ((v8 + ((((arg0 + 1) + v3) + ((load32(9142440) + 2) * load32(v5 + 208))) * v9)) << 2)), load32(arg1 + 28))
                    v9 = load32(v5 + 216)
                    if (u(arg0) < u(load32(v5 + 216))):
                        continue
                    break
                if (u(v2) < u(v9)):
                    continue
                break
        func118(arg1)
        func92(arg1, 0.0, 0.0)
        func29(arg1, 1)
        break
    G.global0 = (v12 + 16)
    return func60(arg1, 1.0)

# ------------------------------------------------------------
# $func517
# ------------------------------------------------------------
def func517(arg0, arg1, param2):
    v13 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = load32(9671128)
    v14 = (load32(9671128) + (arg1 * 132))
    while True:  # block $label3
        v5 = (v4 + (arg0 * 132))
        v3 = load8u((v4 + (arg0 * 132)) + 125)
        if (load8u((v4 + (arg0 * 132)) + 125) == 1):
            v2 = ((load8u(v14 + 122) * 404) + 9568096)
            v8 = load32(((load8u(v14 + 122) * 404) + 9568096) + 220)
            v10 = load16u(v14 + 114)
            v15 = (load32(((load8u(v14 + 122) * 404) + 9568096) + 220) + load16u(v14 + 114))
            v3 = load32(v2 + 216)
            v12 = load16u(v14 + 112)
            v6 = (load32(v2 + 216) + load16u(v14 + 112))
            v9 = load16u(v5 + 114)
            while True:  # block $label1
                while True:  # block $label0
                    v7 = load16u(v5 + 112)
                    v2 = (u(load16u(v5 + 112)) < u(v12))
                    if (u(load16u(v5 + 112)) < u(v12)):
                        break
                    if (v6 <= v7):
                        break
                    if (u(v9) < u(v10)):
                        break
                    if (v9 >= v15):
                        break
                    v2 = ((v8 // 2) + v10)
                    v8 = (-1 if (v2 < v9) else (((v8 // 2) + v10) != v9))
                    v2 = ((v3 // 2) + v12)
                    break
                    break
                v8 = (1 if (u(v9) < u(v10)) else (-1 if (v9 >= v15) else 0))
                break
            v7 = (1 if v2 else (-1 if (v6 <= v7) else 0))
            v3 = 6
            v2 = (((v8 * 3) + v7) + 4)
            if (u((((v8 * 3) + v7) + 4)) <= u(8)):
                v3 = load8u((v2 + 10184))
            v2 = (v4 + (arg0 * 132))
            store8((v4 + (arg0 * 132)) + 124, v3)
            while True:  # block $label2
                v2 = ((load8u(v2 + 122) * 72) + 9263856)
                if load32(((load8u(v2 + 122) * 72) + 9263856) + 12):
                    break
                break
            v6 = (v4 + (arg0 * 132))
            v2 = load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
                # call_indirect[v2]
            if (load8u(v5 + 125) == 3):
                break
            v3 = load32(v6 + 44)
            if load32(v6 + 44):
                v2 = load32(9142848)
                v8 = load32(9215884)
                store32((load32(9215884) + (v3 << 4)) + 4, 46)
                store32((v8 + (load32(v6 + 44) << 4)) + 8, load32((v4 + (arg0 * 132)) + 28))
                store32((v8 + (load32(v6 + 44) << 4)) + 12, arg1)
                store32((v8 + (load32(v6 + 44) << 4)), (v2 + 1))
                break
            store32(v6 + 44, ((Ua(25, 46, load32((v4 + (arg0 * 132)) + 28), arg1) & 0xFFFFFFFF) >> 2))
            break
        while True:  # block $label4
            if (load8u(v14 + 125) != 3):
                v15 = (v4 + (arg1 * 132))
                v11 = (v4 + (arg0 * 132))
                if (u(load32((v4 + (arg1 * 132)) + 84)) < u(load32((v4 + (arg0 * 132)) + 84))):
                    break
            v2 = (v4 + (arg0 * 132))
            if load32((v4 + (arg0 * 132)) + 96):
                break
            arg0 = (v4 + (arg1 * 132))
            arg0 = func208(load16u((v4 + (arg1 * 132)) + 112), load16u(arg0 + 114), load16u(v2 + 110), load32(v2 + 84))
            if func208(load16u((v4 + (arg1 * 132)) + 112), load16u(arg0 + 114), load16u(v2 + 110), load32(v2 + 84)):
                break
            func29(v5, 1)
            break
            break
        v6 = load32(v11 + 96)
        if (load32(v11 + 96) == 0):
            v10 = load32(9561692)
            v7 = load16u(v11 + 110)
            v12 = load32(((load32(9561692) + (load16u(v11 + 110) * 286704)) + 284304))
            if (v3 == 8):
                store8(v5 + 125, 1)
                v3 = 1
            v9 = (v4 + (arg0 * 132))
            v8 = load32((v4 + (arg0 * 132)) + 72)
            if (u(v12) > u(load32((v4 + (arg0 * 132)) + 72))):
                v2 = load32(((load8u(v9 + 122) * 72) + 9263856))
                if (load32(((load8u(v9 + 122) * 72) + 9263856)) != load32(v9 + 48)):
                    v7 = load16u(v11 + 110)
                    v10 = load32(9561692)
                    v3 = load8u(v5 + 125)
                v2 = load32(((v10 + (v7 * 286704)) + 284156))
                if (v3 == 1):
                    func63(func37(v5, v2, 0.0, 0), v5, 46, arg1, v2)
                    break
                # TODO: i32.div_u []
                store32(load32(9142848), (v2 + 25))
                break
            v3 = (v4 + (arg1 * 132))
            v2 = (load16u(v9 + 112) - load16u((v4 + (arg1 * 132)) + 112))
            v2 = (load16u(v9 + 114) - load16u(v3 + 114))
            v3 = (v10 + (v7 * 286704))
            v2 = load32(((v10 + (v7 * 286704)) + 284096))
            if (((((load16u(v9 + 112) - load16u((v4 + (arg1 * 132)) + 112)) * v2) + ((load16u(v9 + 114) - load16u(v3 + 114)) * v2)) - 1) > (load32(((v10 + (v7 * 286704)) + 284096)) * v2)):
                func117(v5, arg1, 46)
                break
            store32(v9 + 72, (v8 - v12))
            v2 = (v3 + 281668)
            store32((v3 + 281668), (load32(v2) + v12))
        while True:  # block $label5
            arg0 = ((load8u((v4 + (arg0 * 132)) + 122) * 72) + 9263856)
            if load32(((load8u((v4 + (arg0 * 132)) + 122) * 72) + 9263856) + 12):
                arg0 = (v4 + (arg1 * 132))
                break
            break
        while True:  # block $label13
            while True:  # block $label11
                while True:  # block $label12
                    v2 = load32(v11 + 84)
                    if (u(load32(v11 + 84)) > u(load32(v15 + 84))):
                        v8 = (v4 + (arg1 * 132))
                        v7 = load16u((v4 + (arg1 * 132)) + 114)
                        v6 = load16u(v8 + 112)
                        while True:  # block $label8
                            while True:  # block $label7
                                while True:  # block $label6
                                    arg0 = load32(load32(9142424) + 48)
                                    if load32(load32(9142424) + 48):
                                        if (load8u(9147152) == 0):
                                            break
                                    v3 = load32(9142440)
                                    break
                                    break
                                v3 = load32(9142440)
                                v2 = load16u((load32(9147376) + (((load32(9142440) * v7) + v6) << 1)))
                                if (arg0 == 2):
                                    if (u(v2) > u(1)):
                                        break
                                    break
                                if (v2 == 0):
                                    break
                                break
                            # TODO: f32.convert_i32_u []
                            # TODO: f32.convert_i32_u []
                            func80(v6, float((v7 - 1)), load32(9142584), 32.0, (v3 * 96))
                            v7 = load16u(v8 + 114)
                            v6 = load16u(v8 + 112)
                            break
                        while True:  # block $label9
                            arg0 = ((v6 << 5) - load32(9142952))
                            arg0 = ((v7 << 5) - load32(9142956))
                            if ((((((v6 << 5) - load32(9142952)) * arg0) + (((v7 << 5) - load32(9142956)) * arg0)) - 1) > 9000000):
                                break
                            v2 = load32(39892)
                            while True:  # block $label10
                                arg0 = load32(load32(9142424) + 48)
                                if (load32(load32(9142424) + 48) == 0):
                                    break
                                if load8u(9147152):
                                    break
                                v3 = load16u((load32(9147376) + (((load32(9142440) * v7) + v6) << 1)))
                                if (arg0 == 2):
                                    if (u(v3) > u(1)):
                                        break
                                    break
                                if (v3 == 0):
                                    break
                                break
                            store32(v13 + 8, v7)
                            store32(v13 + 4, v6)
                            store32(v13, v2)
                            a_b()
                            break
                        v2 = (v4 + (arg1 * 132))
                        arg0 = (load32(v2 + 80) + 100)
                        store32((v4 + (arg1 * 132)) + 80, (load32(v2 + 80) + 100))
                        arg0 = load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284008))
                        # TODO: i32.div_u []
                        if (u((load32(v15 + 84) * 100)) >= u((1 if (u(arg0) <= u(1)) else load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284008))))):
                            func198(v14)
                        if load32(v11 + 96):
                            break
                        func291(v5, 46, arg1, 1400)
                        break
                    if v6:
                        store8(v5 + 125, 0)
                    if load32(v11 + 96):
                        break
                    arg0 = (v4 + (arg1 * 132))
                    func117(v5, func208(load16u((v4 + (arg1 * 132)) + 112), load16u(arg0 + 114), load16u(v11 + 110), v2), 46)
                    break
                if (load32(v11 + 96) == 0):
                    break
                break
            func29(v5, 1)
            break
        if (load32((v4 + (arg1 * 132)) + 92) == 0):
            break
        if load32(9140316):
            if (load32(9140320) != load32((v4 + (arg1 * 132)) + 28)):
                break
        break
    G.global0 = (v13 + 16)
    return func28(1, 1)

# ------------------------------------------------------------
# $func518
# ------------------------------------------------------------
def func518(arg0, arg1, arg2, arg3, arg4):
    while True:  # block $label0
        arg2 = load32(9671128)
        arg1 = load32(arg1)
        arg3 = ((load32(((load8u((load32(9671128) + (load32(arg1) * 132)) + 122) * 404) + 9568096) + 304) == 0) & arg4)
        if (((load32(((load8u((load32(9671128) + (load32(arg1) * 132)) + 122) * 404) + 9568096) + 304) == 0) & arg4) == 0):
            break
        arg0 = load32((arg2 + (arg0 * 132)) + 44)
        if (load32((arg2 + (arg0 * 132)) + 44) == 0):
            break
        arg2 = load32(9215884)
        if (load32((load32(9215884) + (arg0 << 4)) + 4) != 46):
            break
        store32((arg2 + ((arg0 << 4) | 12)), arg1)
        break
    return arg3

# ------------------------------------------------------------
# $func519
# ------------------------------------------------------------
def func519(arg0):
    while True:  # block $label1
        while True:  # block $label0
            v2 = load32(9671128)
            v3 = load32(arg0 + 32)
            v4 = (load32(9671128) + (load32(arg0 + 32) * 132))
            if (load8u((load32(9671128) + (load32(arg0 + 32) * 132)) + 125) == 3):
                v1 = load32(arg0 + 84)
                break
            v1 = load32(arg0 + 84)
            if (u(load32(arg0 + 84)) > u(load32(v4 + 84))):
                break
            break
        v2 = (v2 + (v3 * 132))
        v1 = func208(load16u((v2 + (v3 * 132)) + 112), load16u(v2 + 114), load16u(arg0 + 110), v1)
        if (func208(load16u((v2 + (v3 * 132)) + 112), load16u(v2 + 114), load16u(arg0 + 110), v1) == 0):
            return 1
        store32(arg0 + 32, v1)
        break
    return 0

# ------------------------------------------------------------
# $gb
# Export: gb
# ------------------------------------------------------------
def gb(arg0):
    """Exported as gb."""
    arg0 = ((arg0 * 404) + 9568096)
    if (load32(((arg0 * 404) + 9568096) + 264) == 3):
    else:
    return 0

# ------------------------------------------------------------
# $func521
# ------------------------------------------------------------
def func521(arg0, arg1):
    v6 = load32(9671128)
    v4 = (load32(9671128) + (arg0 * 132))
    if (load8u((load32(9671128) + (arg0 * 132)) + 125) != 3):
        v7 = load16u(v4 + 110)
        v8 = load32(9561692)
        while True:  # block $label0
            arg1 = load32(v4 + 20)
            if (load32(v4 + 20) == 0):
                arg1 = func26(16)
                store32(func26(16) + 4, 17)
                v2 = func26(68)
                store32(arg1 + 12, 1)
                store32(arg1, v2)
                store32(v4 + 20, arg1)
                # TODO: memory.fill []
                store32(arg1 + 8, 17)
                break
            v2 = load32(arg1 + 4)
            if (u(load32(arg1 + 4)) > u(16)):
                break
            v3 = load32(arg1 + 8)
            if (u(v2) <= u((load32(arg1 + 8) + 17))):
                v5 = ((v2 + load32(arg1 + 12)) + 17)
                store32(arg1 + 4, ((v2 + load32(arg1 + 12)) + 17))
                v2 = load32(arg1)
                v5 = func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2)))
                if v3:
                    # TODO: memory.copy []
                if v2:
                store32(arg1, v5)
                arg1 = load32(v4 + 20)
            # TODO: memory.fill []
            break
        while True:  # block $label1
            v5 = (v8 + (v7 * 286704))
            if (load32((((v8 + (v7 * 286704)) + (load32(39128) << 2)) + 281808)) != 1):
                break
            arg1 = load32(arg1)
            v9 = load64(load32(arg1) + 16)
            store64(arg1 + 12, load64(arg1 + 8))
            v2 = load32(arg1 + 24)
            store64(arg1 + 20, v9)
            store64(arg1 + 4, load64(arg1))
            store32(arg1 + 28, v2)
            v9 = load64(9147316)
            v2 = load32(9147312)
            store32(9147316, load32(9147312))
            v3 = load32(9147324)
            store64(9147320, v9)
            v3 = (v3 ^ (v3 << 11))
            v2 = ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8))) ^ v3)
            store32(9147312, ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8))) ^ v3))
            store32(arg1, (load32((((v2 % 19) << 2) + 9682096)) + 1))
            if (load32(9671124) != 95):
                break
            if (load32(9173808) != load32((v6 + (arg0 * 132)) + 28)):
                break
            break
        while True:  # block $label2
            if (load32(((v5 + (load32(39132) << 2)) + 281808)) != 1):
                break
            arg1 = load32(load32(v4 + 20))
            v9 = load64(load32(load32(v4 + 20)) + 40)
            store64(arg1 + 36, load64(arg1 + 32))
            v10 = load64(arg1 + 48)
            store64(arg1 + 44, v9)
            v2 = load32(arg1 + 56)
            store64(arg1 + 52, v10)
            store32(arg1 + 60, v2)
            v9 = load64(9147316)
            v2 = load32(9147312)
            store32(9147316, load32(9147312))
            v3 = load32(9147324)
            store64(9147320, v9)
            v3 = (v3 ^ (v3 << 11))
            v2 = ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8))) ^ v3)
            store32(9147312, ((v2 ^ (((v2 & 0xFFFFFFFF) >> 19) ^ (((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8))) ^ v3))
            store32(arg1 + 32, (load32((((v2 % 19) << 2) + 9682096)) + 1))
            if (load32(9671124) != 96):
                break
            if (load32(9173808) != load32((v6 + (arg0 * 132)) + 28)):
                break
            break
        arg1 = load32(((load32(9561692) + (load16u(v4 + 110) * 286704)) + 284236))

# ------------------------------------------------------------
# $func522
# ------------------------------------------------------------
def func522(arg0, arg1):
    while True:  # block $label0
        if (arg0 == 0):
            break
        arg0 = load32(9213808)
        if (load32(9213808) == 0):
            break
        if (load8u(9163792) == 0):
            break
        arg1 = load32(9140316)
        store32(9140316, (load32(9140316) + 1))
        arg0 = (load32(9671128) + (load32((((arg1 % arg0) << 2) + 9173808)) * 132))
        while True:  # block $label1
            arg1 = load32(9140320)
            if (load32(9140320) == 0):
                break
            v2 = load32(9671128)
            v3 = load32((load32(9671128) + (arg1 * 132)) + 92)
            if (load32((load32(9671128) + (arg1 * 132)) + 92) == 0):
                break
            break
        arg0 = load32(arg0 + 28)
        store32(9140320, load32(arg0 + 28))
        break

# ------------------------------------------------------------
# $mc
# Export: mc
# ------------------------------------------------------------
def mc():
    """Exported as mc."""
    while True:  # block $label0
        if load8u(9147210):
            if load32(load32(9142424) + 48):
                break
        store8(9684336, 1)
        store8(9215872, 1)
        break

# ------------------------------------------------------------
# $tb
# Export: tb
# ------------------------------------------------------------
def tb(arg0):
    """Exported as tb."""
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label10
        arg0 = load32(9681844)
        if (load32(9681844) == 0):
            arg0 = 0
            while True:  # $label0
                v3 = ((arg0 * 404) + 9568096)
                v1 = (load32(((arg0 * 404) + 9568096) + 236) + 10)
                v3 = load32(v3 + 180)
                if load32(v3 + 180):
                    v1 = (load32(v3 + 68) + v1)
                else:
                v7 = (0 + (v1 + v2))
                v2 = (arg0 | 1)
                if ((arg0 | 1) != 255):
                    v2 = ((v2 * 404) + 9568096)
                    v1 = (load32(((v2 * 404) + 9568096) + 236) + 10)
                    arg0 = (arg0 + 2)
                    v2 = load32(v2 + 180)
                    if load32(v2 + 180):
                        v1 = (load32(v2 + 68) + v1)
                    else:
                    v2 = (0 + (v1 + v7))
                    continue
                break
            arg0 = 0
            store32(9681848, v7)
            v4 = func26((-1 if (u(v7) > u(1073741823)) else (v7 << 2)))
            store32(9681844, func26((-1 if (u(v7) > u(1073741823)) else (v7 << 2))))
            while True:  # $label9
                v2 = ((v8 * 404) + 9568096)
                v3 = load32(((v8 * 404) + 9568096) + 180)
                v1 = (v4 + (arg0 << 2))
                store32((v4 + (arg0 << 2)), v8)
                store32(v1 + 4, (load32(v2 + 144) * -48))
                store32(v1 + 8, load32(v2 + 84))
                store32(v1 + 12, load32(v2 + 196))
                store32(v1 + 16, load32(v2 + 264))
                v6 = (arg0 + 5)
                while True:  # block $label1
                    if (v3 == 0):
                        store32((v4 + (v6 << 2)), 0)
                        break
                    store32((v4 + (v6 << 2)), load32(v3 + 8))
                    break
                store32(0 + 24, load32(v3 + 12))
                v1 = load32(v2 + 236)
                store32(v1 + 28, load32(v2 + 236))
                arg0 = (arg0 + 8)
                while True:  # block $label2
                    if (v1 == 0):
                        break
                    v10 = (v1 & 3)
                    v2 = load32(v2 + 232)
                    v11 = 0
                    while True:  # block $label3
                        if (u(v1) < u(4)):
                            v1 = 0
                            break
                        v13 = (v1 & -4)
                        v1 = 0
                        v12 = 0
                        while True:  # $label4
                            v6 = (v4 + (arg0 << 2))
                            v9 = (v1 << 2)
                            store32((v4 + (arg0 << 2)), load32((v2 + (v1 << 2))))
                            store32(v6 + 4, load32((v2 + (v9 | 4))))
                            store32(v6 + 8, load32((v2 + (v9 | 8))))
                            store32(v6 + 12, load32((v2 + (v9 | 12))))
                            v1 = (v1 + 4)
                            arg0 = (arg0 + 4)
                            v12 = (v12 + 4)
                            if ((v12 + 4) != v13):
                                continue
                            break
                        break
                    if (v10 == 0):
                        break
                    while True:  # $label5
                        store32((v4 + (arg0 << 2)), load32((v2 + (v1 << 2))))
                        v1 = (v1 + 1)
                        arg0 = (arg0 + 1)
                        v11 = (v11 + 1)
                        if ((v11 + 1) != v10):
                            continue
                        break
                    break
                while True:  # block $label6
                    if (v3 == 0):
                        store64((v4 + (arg0 << 2)), 0)
                        arg0 = (arg0 + 2)
                        break
                    store32((v4 + (arg0 << 2)), load32(v3 + 68))
                    v2 = (arg0 + 1)
                    v1 = 0
                    if load32(v3 + 68):
                        while True:  # $label7
                            arg0 = v2
                            store32((v4 + (v2 << 2)), load32((v3 + (v1 << 2)) + 28))
                            v2 = (arg0 + 1)
                            v1 = (v1 + 1)
                            if (u((v1 + 1)) < u(load32(v3 + 68))):
                                continue
                            break
                    store32((v4 + (v2 << 2)), load32(v3 + 112))
                    arg0 = (arg0 + 2)
                    v1 = 0
                    if (load32(v3 + 112) == 0):
                        break
                    while True:  # $label8
                        store32((v4 + (arg0 << 2)), load32((v3 + (v1 << 2)) + 72))
                        arg0 = (arg0 + 1)
                        v1 = (v1 + 1)
                        if (u((v1 + 1)) < u(load32(v3 + 112))):
                            continue
                        break
                    break
                v8 = (v8 + 1)
                if ((v8 + 1) != 255):
                    continue
                break
            arg0 = load32((load32(9561692) + (load32(9142872) * 286704)) + 283960)
            store32(v5, v4)
            store32(v5 + 4, v7)
            store32(v5 + 8, arg0)
            a_b()
            break
        v2 = load32((load32(9561692) + (load32(9142872) * 286704)) + 283960)
        store32(v5 + 16, arg0)
        store32(v5 + 20, load32(9681848))
        store32(v5 + 24, v2)
        a_b()
        break
    G.global0 = (v5 + 32)
    return (v5 + 16)

# ------------------------------------------------------------
# $func526
# ------------------------------------------------------------
def func526(arg0, arg1):
    if (arg0 == 0):
        arg0 = load32(9213808)
        if load8u(9147210):
            func41(10, 9173808, arg0, 0, 0)
            return
        v2 = (arg0 << 2)
        arg1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy []
        # call_indirect[load32(9213904)]

# ------------------------------------------------------------
# $lb
# Export: lb
# ------------------------------------------------------------
def lb():
    """Exported as lb."""
    v0 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v0, load32(9681804))
    store32(v0 + 4, load32(9681808))
    store32(v0 + 8, load32(9681812))
    store32(v0 + 12, load32(9681816))
    store32(v0 + 16, load32(9681820))
    v1 = load32(9213808)
    while True:  # block $label0
        if load8u(9147210):
            func41(33, 9173808, v1, v0, 5)
            break
        v3 = (v1 << 2)
        v2 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
        if v1:
            # TODO: memory.copy []
        # call_indirect[load32(9214088)]
        break
    G.global0 = (v0 + 32)

# ------------------------------------------------------------
# $func531
# ------------------------------------------------------------
def func531(arg0, arg1, arg2):
    if arg2:
        v3 = load32(9671128)
        arg0 = 0
        while True:  # $label0
            v4 = (v3 + (load32((arg1 + (arg0 << 2))) * 132))
            if (load8u((v3 + (load32((arg1 + (arg0 << 2))) * 132)) + 125) != 3):
                func304(v4)
                v3 = load32(9671128)
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != arg2):
                continue
            break

# ------------------------------------------------------------
# $func533
# ------------------------------------------------------------
def func533(arg0, arg1):
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v3 = load32(9671128)
    v4 = (load32(9671128) + (arg1 * 132))
    while True:  # block $label0
        v6 = (v3 + (arg0 * 132))
        if (load8u((v3 + (arg0 * 132)) + 125) == 3):
            break
        if (load8u(v6 + 128) == 0):
            break
        v5 = (v3 + (arg0 * 132))
        store8((v3 + (arg0 * 132)) + 127, 0)
        while True:  # block $label1
            v7 = load32(v5 + 40)
            if (load32(v5 + 40) == 0):
                break
            if load8u(9142916):
                store32(v2 + 20, v7)
                store32(v2 + 16, 0)
                a_b()
                break
            v5 = load16u(v5 + 110)
            store32(v2 + 4, v7)
            store32(v2, (v5 + 16))
            a_b()
            break
        store8(v6 + 128, 0)
        break
    while True:  # block $label2
        if (load32(38528) != load8u(v4 + 122)):
            break
        if (u(load32(9142848)) < u((load32(load32(9142424) + 72) * 2400))):
            break
        func78(v4, load16u((v3 + (arg0 * 132)) + 110), 0, 0)
        if (load32((v3 + (arg1 * 132)) + 92) == 0):
            break
        v4 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v3 + (arg1 * 132)) + 28)):
                break
        break
    func29((v3 + (arg0 * 132)), 1)
    G.global0 = (v2 + 32)

# ------------------------------------------------------------
# $func535
# ------------------------------------------------------------
def func535(arg0):
    return load32(arg0 + 4)

# ------------------------------------------------------------
# $_b
# Export: _b
# ------------------------------------------------------------
def _b():
    """Exported as _b."""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store16(9147213, 1)
    store8(9147124, 1)
    v0 = load32(9142848)
    store32(59160, load32(9142848))
    while True:  # block $label0
        if load8u(9147152):
            break
        while True:  # block $label1
            if (load8u(9147212) == 0):
                break
            if load32(9147132):
                break
            # TODO: i32.div_u []
            store32(v0, 10)
            break
        func52((207 if load8u(9143020) else 0), 0)
        a_b()
        while True:  # block $label2
            if (load8u(9147210) == 0):
                break
            if (load8u(9142388) == 0):
                break
            if (load8u(9147125) == 0):
                break
            func344()
            break
        if (load32(9147132) == 0):
            while True:  # block $label3
                v3 = load32(9561692)
                v5 = load32(9142872)
                v1 = (load32(9561692) + (load32(9142872) * 286704))
                v0 = load32((load32(9561692) + (load32(9142872) * 286704)) + 283896)
                if load32((load32(9561692) + (load32(9142872) * 286704)) + 283896):
                    break
                v0 = 0
                if load32(v1 + 283900):
                    break
                v4 = (v1 + 283896)
                v6 = (v1 + 283900)
                v7 = (v3 + (v5 * 286704))
                v1 = 0
                while True:  # $label6
                    while True:  # block $label4
                        v0 = load32(((v7 + (v1 << 2)) + 284636))
                        if (load32(((v7 + (v1 << 2)) + 284636)) == 0):
                            break
                        v8 = load32(v0 + 8)
                        if (load32(v0 + 8) == 0):
                            break
                        v9 = load32(v0)
                        v0 = 0
                        while True:  # $label5
                            v10 = load32((v9 + (v0 << 2)))
                            if (load32((v9 + (v0 << 2))) == 0):
                                v0 = (v0 + 1)
                                if (v8 != (v0 + 1)):
                                    continue
                                break
                            break
                        v1 = (load32(9671128) + (v10 * 132))
                        v4 = ((load8u((load32(9671128) + (v10 * 132)) + 122) * 404) + 9568096)
                        v0 = (((load32(((load8u((load32(9671128) + (v10 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v1 + 112))
                        store32(v4, (((load32(((load8u((load32(9671128) + (v10 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v1 + 112)))
                        store32(v6, (load16u(v1 + 114) + ((load32(v4 + 220) & 0xFFFFFFFF) >> 1)))
                        break
                        break
                    v1 = (v1 + 1)
                    if ((v1 + 1) != 255):
                        continue
                    break
                v0 = 0
                break
            while True:  # block $label7
                if load8u(9142917):
                    break
                v1 = (v3 + (v5 * 286704))
                v3 = load32((v3 + (v5 * 286704)) + 283900)
                store32(v2, (v0 << 5))
                store32(v2 + 4, (v3 << 5))
                v0 = load32(v1 + 284624)
                if (load32(v1 + 284624) == 0):
                    break
                if load8u(9142917):
                    break
                func44((load32(9671128) + (v0 * 132)), 0)
                break
            la()
            break
        store32(9142872, 0)
        break
    G.global0 = (v2 + 16)

# ------------------------------------------------------------
# $func540
# ------------------------------------------------------------
def func540(arg0, arg1, arg2):
    if arg2:
        v6 = load32(9215884)
        v7 = load32(9671128)
        while True:  # $label3
            v4 = 12
            while True:  # block $label2
                while True:  # block $label1
                    while True:  # block $label0
                        arg0 = (v7 + (load32((arg1 + (v3 << 2))) * 132))
                        # br_table[load32((v6 + (load32((v7 + (load32((arg1 + (v3 << 2))) * 132)) + 44) << 4)) + 4)]
                        break
                        break
                    store8(arg0 + 123, 0)
                    store32(arg0 + 32, 0)
                    store32(arg0 + 116, load32(arg0 + 112))
                    v4 = 6
                    v5 = load32(arg0 + 20)
                    if (load32(arg0 + 20) == 0):
                        break
                    if (u(load32(v5 + 8)) < u(3)):
                        break
                    if (u((load32(load32(v5)) - 1)) > u(1)):
                        break
                    store32(v5 + 8, 0)
                    break
                    break
                func29(arg0, 1)
                v6 = load32(9215884)
                v7 = load32(9671128)
                v4 = 6
                break
            store8(arg0 + 129, v4)
            v3 = (v3 + 1)
            if ((v3 + 1) != arg2):
                continue
            break

# ------------------------------------------------------------
# $lf
# Export: lf
# ------------------------------------------------------------
def lf():
    """Exported as lf."""
    return G.global0

# ------------------------------------------------------------
# $mf
# Export: mf
# ------------------------------------------------------------
def mf(arg0):
    """Exported as mf."""
    G.global0 = arg0

# ------------------------------------------------------------
# $nf
# Export: nf
# ------------------------------------------------------------
def nf(arg0):
    """Exported as nf."""
    arg0 = ((G.global0 - arg0) & -16)
    G.global0 = ((G.global0 - arg0) & -16)
    return arg0

# ------------------------------------------------------------
# $ma
# Export: ma
# ------------------------------------------------------------
def ma(arg0, arg1, arg2, arg3, arg4):
    """Exported as ma."""
    store8(9561804, (arg3 != 0))
    store8(9561803, (arg2 != 0))
    store8(9561802, (arg1 != 0))
    store8(9561800, (arg0 != 0))
    store8(9561801, (arg4 != 0))

# ------------------------------------------------------------
# $ne
# Export: ne
# ------------------------------------------------------------
def ne(arg0):
    """Exported as ne."""
    v1 = load32(9681976)
    if load32(9681976):
        store32(9681976, 0)
    v1 = func26(524288000)
    # TODO: memory.fill []
    store32(9687220, v1)
    store32(9681976, v1)
    store32(9687228, 4)
    store32(9687224, ((arg0 * 60) + 16))
    store32(v1, arg0)

# ------------------------------------------------------------
# $qe
# Export: qe
# ------------------------------------------------------------
def qe(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
    """Exported as qe."""
    if (u(arg9) <= u(254)):
        v20 = ((load32(((arg9 * 404) + 9568096) + 264) == 0) & (u(arg11) > u(1)))
    v22 = (arg6 * arg7)
    # TODO: i32.div_u []
    v19 = (arg6 * arg7)
    v17 = load32(9687232)
    while True:  # block $label4
        if (arg11 == 1):
            while True:  # block $label3
                while True:  # block $label2
                    while True:  # block $label0
                        while True:  # block $label1
                            # br_table[(arg10 - 6)]
                            break
                            break
                        v16 = (arg1 * arg2)
                        break
                        break
                    v16 = (arg1 * arg2)
                    if ((arg1 * arg2) == 0):
                        break
                    arg2 = 0
                    if (u(v16) >= u(4)):
                        v18 = (v16 & -4)
                        arg12 = 0
                        while True:  # $label5
                            v13 = (arg2 << 2)
                            v14 = (v17 + (arg2 << 2))
                            if (load32((v17 + (arg2 << 2))) == -16712192):
                                store32(v14, 0)
                            v14 = (v17 + (v13 | 4))
                            if (load32((v17 + (v13 | 4))) == -16712192):
                                store32(v14, 0)
                            v14 = (v17 + (v13 | 8))
                            if (load32((v17 + (v13 | 8))) == -16712192):
                                store32(v14, 0)
                            v13 = (v17 + (v13 | 12))
                            if (load32((v17 + (v13 | 12))) == -16712192):
                                store32(v13, 0)
                            arg2 = (arg2 + 4)
                            arg12 = (arg12 + 4)
                            if ((arg12 + 4) != v18):
                                continue
                            break
                    arg12 = (v16 & 3)
                    if ((v16 & 3) == 0):
                        break
                    while True:  # $label6
                        v13 = (v17 + (arg2 << 2))
                        if (load32((v17 + (arg2 << 2))) == -16712192):
                            store32(v13, 0)
                        arg2 = (arg2 + 1)
                        v15 = (v15 + 1)
                        if ((v15 + 1) != arg12):
                            continue
                        break
                    break
                    break
                v16 = (arg1 * arg2)
                if ((arg1 * arg2) == 0):
                    break
                arg2 = 0
                while True:  # $label8
                    while True:  # block $label7
                        v15 = (arg2 << 2)
                        arg12 = (v17 + (arg2 << 2))
                        v13 = load8u((v17 + (arg2 << 2)))
                        if (load8u((v17 + (arg2 << 2))) == load8u(arg12 + 1)):
                            if (v13 == load8u((v17 + (v15 | 2)))):
                                break
                        store32(arg12, 0)
                        break
                    arg2 = (arg2 + 1)
                    if ((arg2 + 1) != v16):
                        continue
                    break
                break
            if (v16 == 0):
                break
            v15 = 0
            arg2 = 0
            if (u(v16) >= u(4)):
                v18 = (v16 & -4)
                arg12 = 0
                while True:  # $label9
                    v13 = (arg2 << 2)
                    v14 = (v17 + (arg2 << 2))
                    if (load32((v17 + (arg2 << 2))) == -16711936):
                        store32(v14, 0)
                    v14 = (v17 + (v13 | 4))
                    if (load32((v17 + (v13 | 4))) == -16711936):
                        store32(v14, 0)
                    v14 = (v17 + (v13 | 8))
                    if (load32((v17 + (v13 | 8))) == -16711936):
                        store32(v14, 0)
                    v13 = (v17 + (v13 | 12))
                    if (load32((v17 + (v13 | 12))) == -16711936):
                        store32(v13, 0)
                    arg2 = (arg2 + 4)
                    arg12 = (arg12 + 4)
                    if ((arg12 + 4) != v18):
                        continue
                    break
            arg12 = (v16 & 3)
            if ((v16 & 3) == 0):
                break
            while True:  # $label10
                v13 = (v17 + (arg2 << 2))
                if (load32((v17 + (arg2 << 2))) == -16711936):
                    store32(v13, 0)
                arg2 = (arg2 + 1)
                v15 = (v15 + 1)
                if ((v15 + 1) != arg12):
                    continue
                break
            break
        if (arg10 != 22):
            break
        v13 = (arg1 * arg2)
        if ((arg1 * arg2) == 0):
            break
        arg2 = 0
        while True:  # $label11
            arg12 = load32(9687232)
            v15 = (arg2 << 2)
            v18 = (load32(9687232) + (arg2 << 2))
            v16 = (v15 | 2)
            v15 = (v15 | 1)
            # TODO: i32.div_u []
            arg12 = 3
            store8((load8u((arg12 + (v15 | 2))) + (load8u((arg12 + (v15 | 1))) + load8u(v18))), 3)
            store8((load32(9687232) + v15), arg12)
            store8((load32(9687232) + v16), arg12)
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != v13):
                continue
            break
        break
    arg12 = -1
    while True:  # block $label16
        while True:  # block $label12
            if (v22 == 0):
                break
            if (arg1 <= 0):
                break
            v15 = v19
            v14 = 0
            v16 = -1
            while True:  # $label15
                v13 = 0
                v18 = (v19 * v24)
                if ((v19 * v24) < (v18 + v19)):
                    while True:  # $label14
                        arg2 = v18
                        while True:  # $label13
                            if load32((v17 + (((arg1 * arg2) + v13) << 2))):
                                v23 = (arg2 % v19)
                                v21 = ((arg2 % v19) if (u(v21) < u(v23)) else v21)
                                v16 = (v23 if (u(v16) > u(v23)) else v16)
                                v14 = (v13 if (u(v13) > u(v14)) else v14)
                                arg12 = (v13 if (u(arg12) > u(v13)) else arg12)
                            arg2 = (arg2 + 1)
                            if ((arg2 + 1) != v15):
                                continue
                            break
                        v13 = (v13 + 1)
                        if ((v13 + 1) != arg1):
                            continue
                        break
                v15 = (v15 + v19)
                v24 = (v24 + 1)
                if ((v24 + 1) != v22):
                    continue
                break
            break
            break
        v16 = -1
        v14 = 0
        break
    v23 = ((v21 - v16) + 1)
    v24 = ((v14 - arg12) + 1)
    if v20:
        arg2 = (((v22 * v23) * v24) << 2)
        v25 = func26((((v22 * v23) * v24) << 2))
        # TODO: memory.fill []
    while True:  # block $label17
        if (v22 == 0):
            arg2 = load32(9687232)
            break
        v17 = 0
        arg2 = load32(9687232)
        v26 = (v14 + 1)
        if (((arg12 < (v14 + 1)) & v20) == 0):
            break
        v27 = load32(9687236)
        v28 = (v21 + 1)
        v14 = (v21 + 1)
        v15 = 0
        while True:  # $label20
            v13 = (v17 * v19)
            v20 = ((v17 * v19) + v16)
            if (((v17 * v19) + v16) < (v13 + v28)):
                while True:  # $label19
                    v29 = (arg1 * v20)
                    v13 = arg12
                    while True:  # $label18
                        v18 = ((v13 + v29) << 2)
                        if load8u((v27 + ((v13 + v29) << 2))):
                            v21 = (v15 + v25)
                            # TODO: i32.div_u []
                            v30 = 3
                            store8((load8u((arg2 + (v18 | 2))) + (load8u((arg2 + (v18 | 1))) + load8u((arg2 + v18)))) + 2, 3)
                            store16(v21, ((v30 & 255) * 257))
                            store8(v21 + 3, load8u((arg2 + (v18 | 3))))
                        v15 = (v15 + 4)
                        v13 = (v13 + 1)
                        if ((v13 + 1) < v26):
                            continue
                        break
                    v20 = (v20 + 1)
                    if ((v20 + 1) != v14):
                        continue
                    break
            v14 = (v14 + v19)
            v17 = (v17 + 1)
            if ((v17 + 1) != v22):
                continue
            break
        break
    if arg2:
        store32(9687232, 0)
    arg1 = load32(9687236)
    if load32(9687236):
        store32(9687236, 0)
    arg2 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    v15 = load32(9687224)
    arg1 = load32(9687220)
    v13 = (arg2 << 2)
    store32((load32(9687220) + (arg2 << 2)), v24)
    v19 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (v19 << 2)), (v22 * v23))
    v19 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    # TODO: i32.div_u []
    store32(arg4, (arg12 - arg11))
    arg4 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    # TODO: i32.div_u []
    store32(arg5, (v16 - arg11))
    arg4 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg4 << 2)), arg6)
    arg4 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg4 << 2)), arg7)
    arg4 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg4 << 2)), arg3)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg9)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg10)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), (v15 - v13))
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), 0)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg8)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg11)
    arg3 = load32(9687228)
    store32(9687228, (load32(9687228) + 1))
    store32((arg1 + (arg3 << 2)), arg0)
    arg0 = load32(9687228)
    store32(9687228, (load32(9687228) + 2))
    store32((arg1 + (arg0 << 2)) + 4, 0)
    if v25:
    return arg2

# ------------------------------------------------------------
# $func547
# ------------------------------------------------------------
def func547(arg0):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v1 = load32(9173808)
    store32(arg0 + 12, load32(9173808))
    while True:  # block $label0
        if load8u(9147210):
            func41(3, (arg0 + 12), 1, 0, 0)
            break
        v2 = func26(4)
        store32(func26(4), v1)
        # call_indirect[load32(9213848)]
        break
    G.global0 = (arg0 + 16)

# ------------------------------------------------------------
# $func548
# ------------------------------------------------------------
def func548(arg0, arg1, arg2, arg3, arg4):
    arg1 = load32(arg1)
    arg2 = (load32(9671128) + (load32(arg1) * 132))
    return (((load8u(((load8u((load32(9671128) + (load32(arg1) * 132)) + 122) * 404) + 9568096) + 352) == 0) | (arg0 == arg1)) | (load16u(arg2 + 110) == 0))

# ------------------------------------------------------------
# $yc
# Export: yc
# ------------------------------------------------------------
def yc(arg0):
    """Exported as yc."""
    store8(9147211, arg0)

# ------------------------------------------------------------
# $re
# Export: re
# ------------------------------------------------------------
def re():
    """Exported as re."""
    return ((load32(9213820) | load32(9213808)) != 0)

# ------------------------------------------------------------
# $hb
# Export: hb
# ------------------------------------------------------------
def hb(arg0):
    """Exported as hb."""
    while True:  # block $label0
        if (load8u(9142905) == 0):
            break
        if (load8u(9147127) == 0):
            func361()
        v9 = load32(9681680)
        if load32(9681680):
            store32(9681680, 0)
        v9 = load32(9142892)
        arg0 = (load32(9142892) * arg0)
        v13 = func26((-1 if (u(arg0) > u(1073741823)) else ((load32(9142892) * arg0) << 2)))
        store32(9681680, func26((-1 if (u(arg0) > u(1073741823)) else ((load32(9142892) * arg0) << 2))))
        if (u(v9) < u(2)):
            break
        v17 = load32(38528)
        v20 = load32(9561720)
        v15 = load32(9143004)
        v16 = load32(9561692)
        v21 = load8u(9147127)
        v18 = 1
        while True:  # $label33
            v10 = 1
            while True:  # block $label1
                while True:  # $label2
                    if (load32((v16 + (v10 * 286704)) + 283944) == v18):
                        break
                    v10 = (v10 + 1)
                    if ((v10 + 1) != v9):
                        continue
                    break
                v10 = v9
                break
            v3 = (v16 + (v10 * 286704))
            v19 = ((v16 + (v10 * 286704)) + 278556)
            if v21:
                arg0 = (v13 + (v11 << 2))
                store32((v13 + (v11 << 2)), load32(v3 + 283884))
                store32(arg0 + 4, load32(v3 + 283888))
                v11 = (v11 + 2)
            v4 = (v13 + (v11 << 2))
            store32((v13 + (v11 << 2)), load32(v3 + 283892))
            store32(v4 + 4, load32(v3 + 284608))
            v8 = (v11 + 2)
            v22 = (v3 + 284608)
            v12 = (v3 + 281784)
            arg0 = load32((v3 + 281784))
            v5 = (load32((v3 + 281784)) * 255)
            v14 = (arg0 * v9)
            v1 = 0
            v2 = 0
            while True:  # $label5
                while True:  # block $label3
                    if (load8u((v15 + (v1 + v14))) == 0):
                        break
                    v7 = ((v16 + (v1 * 286704)) + 278568)
                    arg0 = 0
                    while True:  # $label4
                        if (load32(((arg0 * 404) + 9568096) + 264) != 1):
                            v2 = (load32((load32(v7) + ((arg0 + v5) << 2))) + v2)
                        v6 = (arg0 | 1)
                        if ((arg0 | 1) == 255):
                            break
                        if (load32(((v6 * 404) + 9568096) + 264) != 1):
                            v2 = (load32((load32(v7) + ((v5 + v6) << 2))) + v2)
                        arg0 = (arg0 + 2)
                        continue
                        break
                    raise RuntimeError('unreachable')
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v8 << 2)), v2)
            v8 = (v11 + 3)
            v23 = (v3 + 278568)
            v7 = load32((v3 + 278568))
            v1 = 0
            v2 = 0
            while True:  # $label9
                v6 = (v1 * 255)
                arg0 = 0
                while True:  # $label8
                    while True:  # block $label6
                        if (load32(((arg0 * 404) + 9568096) + 264) == 1):
                            break
                        if (arg0 == v17):
                            break
                        v2 = (load32((v7 + ((arg0 + v6) << 2))) + v2)
                        break
                    v5 = (arg0 | 1)
                    if ((arg0 | 1) != 255):
                        while True:  # block $label7
                            if (load32(((v5 * 404) + 9568096) + 264) == 1):
                                break
                            if (v5 == v17):
                                break
                            v2 = (load32((v7 + ((v5 + v6) << 2))) + v2)
                            break
                        arg0 = (arg0 + 2)
                        continue
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v8 << 2)), v2)
            v6 = load32(v12)
            v7 = (load32(v12) * v9)
            v8 = load32(v19)
            v1 = 0
            v2 = 0
            while True:  # $label11
                if load8u((v15 + (v1 + v7))):
                    v14 = (v1 * 255)
                    arg0 = 0
                    while True:  # $label10
                        v5 = (v8 + ((arg0 + v14) << 2))
                        v2 = (load32((v8 + ((arg0 + v14) << 2)) + 16) + (load32(v5 + 12) + (load32(v5 + 8) + (load32(v5 + 4) + (load32(v5) + v2)))))
                        arg0 = (arg0 + 5)
                        if ((arg0 + 5) != 255):
                            continue
                        break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            v6 = (v6 * 255)
            v1 = 0
            v5 = 0
            while True:  # $label14
                while True:  # block $label12
                    if (load8u((v15 + (v1 + v7))) == 0):
                        break
                    v8 = ((v16 + (v1 * 286704)) + 278564)
                    arg0 = 0
                    while True:  # $label13
                        if (load32(((arg0 * 404) + 9568096) + 264) == 1):
                            v5 = (load32((load32(v8) + ((arg0 + v6) << 2))) + v5)
                        v14 = (arg0 | 1)
                        if ((arg0 | 1) == 255):
                            break
                        if (load32(((v14 * 404) + 9568096) + 264) == 1):
                            v5 = (load32((load32(v8) + ((v6 + v14) << 2))) + v5)
                        arg0 = (arg0 + 2)
                        continue
                        break
                    raise RuntimeError('unreachable')
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32(v4 + 24, v5)
            store32(v4 + 20, (v2 - v5))
            store32(v4 + 16, v2)
            v24 = (v11 + 7)
            v6 = (load32(v12) * v9)
            v25 = (v3 + 278564)
            v7 = load32((v3 + 278564))
            v1 = 0
            v2 = 0
            while True:  # $label16
                if load8u((v15 + (v1 + v6))):
                    v8 = (v1 * 255)
                    arg0 = 0
                    while True:  # $label15
                        v5 = (v7 + ((arg0 + v8) << 2))
                        v2 = (load32((v7 + ((arg0 + v8) << 2)) + 16) + (load32(v5 + 12) + (load32(v5 + 8) + (load32(v5 + 4) + (load32(v5) + v2)))))
                        arg0 = (arg0 + 5)
                        if ((arg0 + 5) != 255):
                            continue
                        break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            v1 = 0
            v5 = 0
            while True:  # $label19
                while True:  # block $label17
                    if (load8u((v15 + (v1 + v6))) == 0):
                        break
                    v8 = (v1 * 255)
                    arg0 = 0
                    while True:  # $label18
                        if (load32(((arg0 * 404) + 9568096) + 264) == 1):
                            v5 = (load32((v7 + ((arg0 + v8) << 2))) + v5)
                        v14 = (arg0 | 1)
                        if ((arg0 | 1) == 255):
                            break
                        if (load32(((v14 * 404) + 9568096) + 264) == 1):
                            v5 = (load32((v7 + ((v8 + v14) << 2))) + v5)
                        arg0 = (arg0 + 2)
                        continue
                        break
                    raise RuntimeError('unreachable')
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v24 << 2)), v2)
            store32(v4 + 36, v5)
            store32(v4 + 32, (v2 - v5))
            store32(v4 + 40, load32(v3 + 283956))
            arg0 = (v3 + 281676)
            v1 = (v3 + 281640)
            store32(v4 + 44, (load32((v3 + 281676)) + load32((v3 + 281640))))
            store32(v4 + 48, load32(v1))
            store32(v4 + 52, load32(arg0))
            arg0 = (v3 + 281680)
            v1 = (v3 + 281644)
            store32(v4 + 56, (load32((v3 + 281680)) + load32((v3 + 281644))))
            store32(v4 + 60, load32(v1))
            store32((v4 - -64), load32(arg0))
            arg0 = (v3 + 281684)
            v1 = (v3 + 281656)
            v2 = (v3 + 281648)
            v5 = (v3 + 281660)
            v7 = (v3 + 281652)
            store32(v4 + 68, (load32((v3 + 281684)) + (load32((v3 + 281656)) + (load32((v3 + 281648)) + (load32((v3 + 281660)) + load32((v3 + 281652)))))))
            store32(v4 + 72, load32(v7))
            store32(v4 + 76, load32(v5))
            store32(v4 + 80, load32(v2))
            store32(v4 + 84, load32(v1))
            store32(v4 + 88, load32(arg0))
            arg0 = (v3 + 281688)
            v1 = (v3 + 281664)
            store32(v4 + 92, (load32((v3 + 281688)) + load32((v3 + 281664))))
            store32(v4 + 96, load32(v1))
            store32(v4 + 100, load32(arg0))
            store32(v4 + 104, load32((v3 + 281636)))
            store32(v4 + 108, load32((v3 + 281744)))
            store32(v4 + 112, load32((v3 + 281672)))
            store32(v4 + 116, load32((v3 + 281668)))
            store32(v4 + 120, load32((v3 + 281748)))
            arg0 = 0
            v2 = 0
            while True:  # $label22
                while True:  # block $label20
                    if (load32(((arg0 * 404) + 9568096) + 264) & -5):
                        break
                    if (arg0 == v17):
                        break
                    v2 = (load32(((v3 + (arg0 << 2)) + 278576)) + v2)
                    break
                v1 = (arg0 | 1)
                if ((arg0 | 1) != 255):
                    while True:  # block $label21
                        if (load32(((v1 * 404) + 9568096) + 264) & -5):
                            break
                        if (v1 == v17):
                            break
                        v2 = (load32(((v3 + (v1 << 2)) + 278576)) + v2)
                        break
                    arg0 = (arg0 + 2)
                    continue
                break
            store32(v4 + 124, v2)
            v6 = (v11 + 32)
            arg0 = load32(v12)
            v5 = (load32(v12) * 255)
            v8 = (arg0 * v9)
            v1 = 0
            v2 = 0
            while True:  # $label25
                while True:  # block $label23
                    if (load8u((v15 + (v1 + v8))) == 0):
                        break
                    v12 = ((v16 + (v1 * 286704)) + 278568)
                    arg0 = 0
                    while True:  # $label24
                        if (load32(((arg0 * 404) + 9568096) + 264) == 1):
                            v2 = (load32((load32(v12) + ((arg0 + v5) << 2))) + v2)
                        v7 = (arg0 | 1)
                        if ((arg0 | 1) == 255):
                            break
                        if (load32(((v7 * 404) + 9568096) + 264) == 1):
                            v2 = (load32((load32(v12) + ((v5 + v7) << 2))) + v2)
                        arg0 = (arg0 + 2)
                        continue
                        break
                    raise RuntimeError('unreachable')
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v6 << 2)), v2)
            v5 = load32(v23)
            v1 = 0
            v2 = 0
            while True:  # $label27
                v12 = (v1 * 255)
                arg0 = 0
                while True:  # $label26
                    if (load32(((arg0 * 404) + 9568096) + 264) == 1):
                        v2 = (load32((v5 + ((arg0 + v12) << 2))) + v2)
                    v7 = (arg0 | 1)
                    if ((arg0 | 1) != 255):
                        if (load32(((v7 * 404) + 9568096) + 264) == 1):
                            v2 = (load32((v5 + ((v7 + v12) << 2))) + v2)
                        arg0 = (arg0 + 2)
                        continue
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32(v4 + 132, v2)
            store32(v4 + 136, load32((v3 + 281740)))
            store32(v4 + 140, load32((v3 + 281724)))
            store32(v4 + 144, load32((v3 + 281728)))
            store32(v4 + 148, load32((v3 + 281732)))
            store32(v4 + 152, load32((v3 + 281736)))
            store32(v4 + 156, load32((v3 + 281692)))
            store32(v4 + 160, load32((v3 + 281696)))
            store32(v4 + 164, load32((v3 + 281700)))
            store32(v4 + 168, load32((v3 + 281704)))
            store32(v4 + 172, load32((v3 + 281708)))
            store32(v4 + 176, load32((v3 + 281712)))
            store32(v4 + 180, load32((v3 + 281716)))
            store32(v4 + 184, load32((v3 + 281720)))
            while True:  # block $label28
                arg0 = load32(v22)
                if load32(v22):
                    if (arg0 == v20):
                        break
                break
            store32((v13 + ((v11 + 47) << 2)), (load8u(v3 + 286697) != 0))
            arg0 = load32((v3 + 278572))
            store32(v4 + 192, load32(load32((v3 + 278572)) + 8))
            store32(v4 + 196, load32(v3 + 283944))
            store32(v4 + 200, load32(arg0))
            v1 = 0
            v2 = func26(1020)
            # TODO: memory.fill []
            v12 = (v9 * v10)
            v7 = (v11 + 51)
            while True:  # $label30
                if load8u((v15 + (v1 + v12))):
                    v10 = (v1 * 255)
                    v5 = load32(v25)
                    arg0 = 0
                    while True:  # $label29
                        v6 = (v2 + (arg0 << 2))
                        store32((v2 + (arg0 << 2)), (load32(v6) + load32((v5 + ((arg0 + v10) << 2)))))
                        v6 = (arg0 + 1)
                        v8 = (v2 + ((arg0 + 1) << 2))
                        store32((v2 + ((arg0 + 1) << 2)), (load32(v8) + load32((v5 + ((v6 + v10) << 2)))))
                        v6 = (arg0 + 2)
                        v8 = (v2 + ((arg0 + 2) << 2))
                        store32((v2 + ((arg0 + 2) << 2)), (load32(v8) + load32((v5 + ((v6 + v10) << 2)))))
                        arg0 = (arg0 + 3)
                        if ((arg0 + 3) != 255):
                            continue
                        break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v7 << 2)), v2)
            store32(v4 + 216, (v3 + 280616))
            store32(v4 + 212, (v3 + 279596))
            store32(v4 + 208, (v3 + 278576))
            v1 = 0
            v10 = func26(1020)
            # TODO: memory.fill []
            v7 = (v11 + 55)
            while True:  # $label32
                if load8u((v15 + (v1 + v12))):
                    v2 = (v1 * 255)
                    v5 = load32(v19)
                    arg0 = 0
                    while True:  # $label31
                        v6 = (v10 + (arg0 << 2))
                        store32((v10 + (arg0 << 2)), (load32(v6) + load32((v5 + ((arg0 + v2) << 2)))))
                        v6 = (arg0 + 1)
                        v8 = (v10 + ((arg0 + 1) << 2))
                        store32((v10 + ((arg0 + 1) << 2)), (load32(v8) + load32((v5 + ((v2 + v6) << 2)))))
                        v6 = (arg0 + 2)
                        v8 = (v10 + ((arg0 + 2) << 2))
                        store32((v10 + ((arg0 + 2) << 2)), (load32(v8) + load32((v5 + ((v2 + v6) << 2)))))
                        arg0 = (arg0 + 3)
                        if ((arg0 + 3) != 255):
                            continue
                        break
                v1 = (v1 + 1)
                if ((v1 + 1) != v9):
                    continue
                break
            store32((v13 + (v7 << 2)), v10)
            store32(v4 + 224, load32(v3 + 283908))
            store32(v4 + 228, load32(v3 + 283960))
            arg0 = load32(v3 + 284616)
            if load32(v3 + 284616):
            else:
            store32(arg0, load32(v3 + 284628))
            store32(v4 + 236, v3)
            store32(v4 + 240, ((load8u((v3 + 283974)) | (load8u((v3 + 283973)) << 8)) | (load8u(v3 + 283972) << 16)))
            v11 = (v11 + 61)
            v18 = (v18 + 1)
            if ((v18 + 1) != v9):
                continue
            break
        break
    return v13

# ------------------------------------------------------------
# $ka
# Export: ka
# ------------------------------------------------------------
def ka(arg0, arg1):
    """Exported as ka."""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = load32(9561696)
    while True:  # block $label2
        v6 = load32(9561704)
        if load32(9561704):
            while True:  # block $label0
                while True:  # $label1
                    v5 = ((v2 << 2) + v4)
                    if (u(load32(((v2 << 2) + v4) + 4)) >= u(arg0)):
                        break
                    v2 = (load32(v5 + 8) + v2)
                    if (u((load32(v5 + 8) + v2)) < u(v6)):
                        continue
                    break
                v2 = 0
                break
            arg0 = 0
            while True:  # $label3
                v5 = ((arg0 << 2) + v4)
                if (u(load32(((arg0 << 2) + v4) + 4)) >= u(arg1)):
                    break
                arg0 = (load32(v5 + 8) + arg0)
                if (u((load32(v5 + 8) + arg0)) < u(v6)):
                    continue
                break
        arg0 = 0
        break
    store32(v3 + 4, (arg0 - v2))
    store32(v3, (v4 + (v2 << 2)))
    G.global0 = (v3 + 16)

# ------------------------------------------------------------
# $func557
# ------------------------------------------------------------
def func557(arg0, arg1, arg2):
    func290((load32(9671128) + (load32(arg1) * 132)))

# ------------------------------------------------------------
# $func558
# ------------------------------------------------------------
def func558(arg0):
    store32(9143000, 0)
    arg0 = load32(9142872)
    v1 = load32(9561692)
    v2 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (v2 * 132)))
        store32(9213820, 0)
    func45()
    while True:  # block $label0
        arg0 = load32((((v1 + (arg0 * 286704)) + (load32(38452) << 2)) + 284636))
        if (load32((((v1 + (arg0 * 286704)) + (load32(38452) << 2)) + 284636)) == 0):
            break
        v2 = load32(arg0 + 8)
        if (load32(arg0 + 8) == 0):
            break
        v1 = 0
        while True:  # $label1
            v3 = load32((load32(arg0) + (v1 << 2)))
            if load32((load32(arg0) + (v1 << 2))):
                func44((load32(9671128) + (v3 * 132)), 0)
                v2 = load32(arg0 + 8)
            v1 = (v1 + 1)
            if (u((v1 + 1)) < u(v2)):
                continue
            break
        break

# ------------------------------------------------------------
# $func559
# ------------------------------------------------------------
def func559(arg0, arg1):
    arg1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    store8(9163792, arg0)
    while True:  # block $label0
        if arg0:
            break
        if load32(9684820):
            v6 = 2
            arg0 = load32(9684820)
            # TODO: i32.div_u []
            v7 = (6 + 2)
            v4 = func26(((6 + 2) << 2))
            # TODO: i32.div_u []
            store32(arg0 + 4, 6)
            store32(v4, -1)
            if arg0:
                while True:  # $label1
                    arg0 = (v4 + (v6 << 2))
                    v5 = load32(9684812)
                    v8 = (v3 << 2)
                    v2 = (load32(9684812) + (v3 << 2))
                    store32((v4 + (v6 << 2)), load32((load32(9684812) + (v3 << 2))))
                    store32(arg0 + 4, load32((v5 + (v8 | 4))))
                    store32(arg0 + 8, load32(v2 + 8))
                    v5 = load32(v2 + 12)
                    store32(arg0 + 16, 0)
                    store32(arg0 + 12, v5)
                    v5 = load32(v2 + 16)
                    store32(arg0 + 24, 0)
                    store32(arg0 + 20, v5)
                    func38(load32(v2 + 20))
                    v6 = (v6 + 7)
                    v3 = (v3 + 6)
                    if (u((v3 + 6)) < u(load32(9684820))):
                        continue
                    break
            arg0 = load32(9213808)
            while True:  # block $label2
                if load8u(9147210):
                    func41(5, 9173808, arg0, v4, v7)
                    break
                v3 = (arg0 << 2)
                v2 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                if arg0:
                    # TODO: memory.copy []
                # call_indirect[load32(9213864)]
                break
            store32(9684820, 0)
        while True:  # block $label3
            if (load32(9671176) == 0):
                break
            if load32(9671192):
                arg0 = 0
                while True:  # $label4
                    func38(load32((load32(9671184) + (arg0 << 2))))
                    arg0 = (arg0 + 1)
                    if (u((arg0 + 1)) < u(load32(9671192))):
                        continue
                    break
            store32(9671192, 0)
            store32(9671176, 0)
            store8(9142412, 0)
            if (load8u(9684396) == 0):
                break
            store8(9684396, 0)
            a_b()
            break
        store32(40604, -1)
        if (load32(9684792) == 0):
            break
        store32(9684792, 0)
        arg0 = load32(9684796)
        if load8u(9142916):
            store32(arg1 + 32, arg0)
            a_b()
            break
        store32(arg1 + 24, arg0)
        store64(arg1 + 16, -4602115869219225600)
        store64(arg1 + 8, 0)
        store64(arg1, 0)
        a_b()
        break
    G.global0 = (arg1 + 48)

# ------------------------------------------------------------
# $td
# Export: td
# ------------------------------------------------------------
def td():
    """Exported as td."""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label3
        if (load8u(9147141) == 0):
            while True:  # block $label0
                v3 = load32(9671120)
                if (load32(9671120) == 0):
                    break
                if (u(v3) >= u(4)):
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
                if ((v3 & 3) == 0):
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

# ------------------------------------------------------------
# $func563
# ------------------------------------------------------------
def func563(arg0, arg1, arg2):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if arg2:
        v3 = load32(9142892)
        v6 = load32(9561692)
        while True:  # $label3
            v7 = (v5 << 2)
            arg0 = 0
            while True:  # block $label0
                if (u(v3) < u(2)):
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
            while True:  # block $label2
                if (u(arg0) >= u(v3)):
                    break
                arg0 = (v6 + (arg0 * 286704))
                if (load32((v6 + (arg0 * 286704)) + 283908) == 0):
                    break
                store32(arg0 + 284604, load32((arg1 + (v7 | 4))))
                v3 = load32(9142892)
                break
            v5 = (v5 + 2)
            if (u((v5 + 2)) < u(arg2)):
                continue
            break
    while True:  # block $label4
        if load8u(9147213):
            if (load32(9687276) == 0):
                break
            arg1 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            arg2 = load32(9561692)
            arg0 = 1
            while True:  # $label6
                v3 = (arg2 + (arg0 * 286704))
                if (load8u((arg2 + (arg0 * 286704)) + 286699) == 0):
                    arg1 = load32(v3 + 284604)
                    while True:  # block $label5
                        if (load8u(9147210) == 0):
                            break
                        if (load32(v3 + 284616) != load32(9561844)):
                            if (load32(9142872) != arg0):
                                break
                            if (load8u(9142388) == 0):
                                break
                        arg1 = 2147483647
                        break
                    store32(v4 + 4, arg1)
                    store32(v4, arg0)
                    a_b()
                    arg2 = load32(9561692)
                    arg1 = load32(9142892)
                arg0 = (arg0 + 1)
                if (u((arg0 + 1)) < u(arg1)):
                    continue
                break
            break
        break
    G.global0 = (v4 + 16)

# ------------------------------------------------------------
# $va
# Export: va
# ------------------------------------------------------------
def va(arg0, arg1):
    """Exported as va."""
    store32(9561844, arg0)

# ------------------------------------------------------------
# $eb
# Export: eb
# ------------------------------------------------------------
def eb(arg0):
    """Exported as eb."""
    return load32(((arg0 * 404) + 9568096) + 196)

# ------------------------------------------------------------
# $db
# Export: db
# ------------------------------------------------------------
def db(arg0, arg1, arg2, arg3):
    """Exported as db."""
    while True:  # block $label0
        if (arg0 == 54):
            break
        if load8u(((arg0 * 404) + 9568096) + 378):
            break
        while True:  # block $label1
            if arg1:
                if ((load32(((arg0 * 404) + 9568096) + 264) & -5) == 0):
                    break
                break
            if arg2:
                if (load32(((arg0 * 404) + 9568096) + 264) != 1):
                    break
            if (arg3 == 0):
                break
            if (load32(((arg0 * 404) + 9568096) + 264) != 2):
                break
            break
        v4 = (load32(((arg0 * 404) + 9568096) + 144) * -48)
        break
    return v4

# ------------------------------------------------------------
# $cb
# Export: cb
# ------------------------------------------------------------
def cb(arg0, arg1, arg2, arg3):
    """Exported as cb."""
    while True:  # block $label0
        while True:  # block $label1
            if arg1:
                arg0 = ((arg0 * 404) + 9568096)
                if (load32(((arg0 * 404) + 9568096) + 264) & -5):
                    arg1 = 0
                    if (arg2 == 0):
                        break
                arg1 = -48
                break
            if arg2:
                arg1 = 0
                if (load32(((arg0 * 404) + 9568096) + 264) != 1):
                    break
            if arg3:
                arg1 = 0
                arg2 = ((arg0 * 404) + 9568096)
                if (load32(((arg0 * 404) + 9568096) + 264) != 3):
                    break
                if (load32(arg2 + 368) == 55):
                    break
            arg0 = load32(((arg0 * 404) + 9568096) + 180)
            if (load32(((arg0 * 404) + 9568096) + 180) == 0):
                return 0
            arg1 = 48
            break
        arg0 = (arg0 + 8)
        arg1 = (load32(arg0) * arg1)
        break
    return arg1

# ------------------------------------------------------------
# $sa
# Export: sa
# ------------------------------------------------------------
def sa(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    """Exported as sa."""
    store8(59184, arg1)
    store32(59168, arg0)
    store8(59185, arg2)
    store32(9561840, arg3)
    store8(9142916, arg4)
    store8(9142917, arg5)
    store8(9142918, arg6)

# ------------------------------------------------------------
# $func573
# ------------------------------------------------------------
def func573(arg0, arg1, arg2):
    while True:  # block $label0
        v3 = load32(arg0 + 4)
        v11 = load32(arg0 + 8)
        if (load32(arg0 + 4) == load32(arg0 + 8)):
            break
        v4 = load32(9671128)
        v3 = (load32(9671128) + (v3 * 132))
        v7 = ((load8u((load32(9671128) + (v3 * 132)) + 122) * 404) + 9568096)
        v5 = (v4 + (v11 * 132))
        v6 = ((load8u((v4 + (v11 * 132)) + 122) * 404) + 9568096)
        v9 = ((((load32(((load8u((load32(9671128) + (v3 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v3 + 112)) - (((load32(((load8u((v4 + (v11 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v5 + 112)))
        v3 = ((load16u(v3 + 114) + ((load32(v7 + 220) & 0xFFFFFFFF) >> 1)) - (load16u(v5 + 114) + ((load32(v6 + 220) & 0xFFFFFFFF) >> 1)))
        if ((((((((load32(((load8u((load32(9671128) + (v3 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v3 + 112)) - (((load32(((load8u((v4 + (v11 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v5 + 112))) * v9) + (((load16u(v3 + 114) + ((load32(v7 + 220) & 0xFFFFFFFF) >> 1)) - (load16u(v5 + 114) + ((load32(v6 + 220) & 0xFFFFFFFF) >> 1))) * v3)) - 1) < 82):
            break
        if (arg2 == 0):
            break
        v9 = load32(arg0)
        v3 = load32(9561692)
        while True:  # $label11
            while True:  # block $label1
                v7 = (v4 + (load32((arg1 + (v12 << 2))) * 132))
                v6 = load32(((load8u((v4 + (load32((arg1 + (v12 << 2))) * 132)) + 122) * 404) + 9568096) + 124)
                if (load32(((load8u((v4 + (load32((arg1 + (v12 << 2))) * 132)) + 122) * 404) + 9568096) + 124) == 0):
                    break
                v5 = (v3 + (load16u(v7 + 110) * 286704))
                if (load32((((v3 + (load16u(v7 + 110) * 286704)) + (load32(39104) << 2)) + 281808)) == 0):
                    break
                v3 = load32((v5 + 284340))
                v13 = (v9 if (u(v3) < u(v9)) else load32((v5 + 284340)))
                v14 = (u(v6) < u(v9))
                while True:  # block $label4
                    while True:  # block $label3
                        while True:  # block $label2
                            v4 = load32(v7 + 20)
                            if (load32(v7 + 20) == 0):
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
                            if (load32(v4 + 4) == 0):
                                break
                            break
                        v5 = load32(v4)
                        v3 = 0
                        break
                        break
                    v3 = load32(v4 + 12)
                    store32(v4 + 4, load32(v4 + 12))
                    v10 = load32(v4)
                    v5 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                    if v10:
                    else:
                    v3 = 0
                    store32(v4, v5)
                    v4 = load32(v7 + 20)
                    break
                v10 = (v6 if v14 else v13)
                store32(v8, (v3 + 1))
                store32((v5 + (v3 << 2)), 0)
                while True:  # block $label5
                    v3 = load32(v4 + 8)
                    if (load32(v4 + 8) != load32(v4 + 4)):
                        v5 = load32(v4)
                        break
                    v5 = (load32(v4 + 12) + v3)
                    store32(v4 + 4, (load32(v4 + 12) + v3))
                    v6 = load32(v4)
                    v5 = func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy []
                    if v6:
                        v3 = load32(v4 + 8)
                    store32(v4, v5)
                    break
                v6 = load32(v7 + 20)
                store32(v4 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v10)
                v8 = load32(arg0 + 4)
                while True:  # block $label6
                    v3 = load32(v6 + 8)
                    if (load32(v6 + 8) != load32(v6 + 4)):
                        v5 = load32(v6)
                        break
                    v5 = (load32(v6 + 12) + v3)
                    store32(v6 + 4, (load32(v6 + 12) + v3))
                    v4 = load32(v6)
                    v5 = func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy []
                    if v4:
                        v3 = load32(v6 + 8)
                    store32(v6, v5)
                    break
                v4 = load32(v7 + 20)
                store32(v6 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v8)
                v8 = load32(arg0 + 8)
                while True:  # block $label7
                    v3 = load32(v4 + 8)
                    if (load32(v4 + 8) != load32(v4 + 4)):
                        v5 = load32(v4)
                        break
                    v5 = (load32(v4 + 12) + v3)
                    store32(v4 + 4, (load32(v4 + 12) + v3))
                    v6 = load32(v4)
                    v5 = func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy []
                    if v6:
                        v3 = load32(v4 + 8)
                    store32(v4, v5)
                    break
                v6 = load32(v7 + 20)
                store32(v4 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v8)
                v8 = load32(arg0 + 12)
                while True:  # block $label8
                    v3 = load32(v6 + 8)
                    if (load32(v6 + 8) != load32(v6 + 4)):
                        v5 = load32(v6)
                        break
                    v5 = (load32(v6 + 12) + v3)
                    store32(v6 + 4, (load32(v6 + 12) + v3))
                    v4 = load32(v6)
                    v5 = func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy []
                    if v4:
                        v3 = load32(v6 + 8)
                    store32(v6, v5)
                    break
                v4 = load32(v7 + 20)
                store32(v6 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v8)
                v8 = load32(arg0 + 16)
                while True:  # block $label9
                    v3 = load32(v4 + 8)
                    if (load32(v4 + 8) != load32(v4 + 4)):
                        v5 = load32(v4)
                        break
                    v5 = (load32(v4 + 12) + v3)
                    store32(v4 + 4, (load32(v4 + 12) + v3))
                    v6 = load32(v4)
                    v5 = func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2)))
                    if v3:
                        # TODO: memory.copy []
                    if v6:
                        v3 = load32(v4 + 8)
                    store32(v4, v5)
                    break
                v6 = load32(v7 + 20)
                store32(v4 + 8, (v3 + 1))
                store32((v5 + (v3 << 2)), v8)
                while True:  # block $label10
                    v4 = load32(v6 + 8)
                    if (load32(v6 + 8) != load32(v6 + 4)):
                        v3 = load32(v6)
                        break
                    v3 = (load32(v6 + 12) + v4)
                    store32(v6 + 4, (load32(v6 + 12) + v4))
                    v5 = load32(v6)
                    v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                    if v4:
                        # TODO: memory.copy []
                    if v5:
                        v4 = load32(v6 + 8)
                    store32(v6, v3)
                    break
                store32(v6 + 8, (v4 + 1))
                store32((v3 + (v4 << 2)), 1)
                v3 = load32(9561692)
                v4 = load32(9671128)
                break
            v12 = (v12 + 1)
            if ((v12 + 1) != arg2):
                continue
            break
        break
    return (v4 << 2)

# ------------------------------------------------------------
# $wc
# Export: wc
# ------------------------------------------------------------
def wc(arg0, arg1, arg2, arg3, arg4):
    """Exported as wc."""
    arg4 = (load32(9561692) + (arg4 * 286704))
    store32((load32(9561692) + (arg4 * 286704)) + 283848, (load32(arg4 + 283848) + arg0))
    arg0 = (arg4 + 283852)
    store32((arg4 + 283852), (load32(arg0) + arg1))
    arg0 = (arg4 + 283856)
    store32((arg4 + 283856), (load32(arg0) + arg2))
    arg0 = (arg4 + 283860)
    store32((arg4 + 283860), (load32(arg0) + arg3))

# ------------------------------------------------------------
# $da
# Export: da
# ------------------------------------------------------------
def da(arg0, arg1, arg2):
    """Exported as da."""
    while True:  # block $label0
        if (load32(9142384) == 0):
            break
        if (arg1 == 0):
            break
        store8(9140304, 1)
        break
    store8(9142388, arg1)
    store32(9142384, arg0)

# ------------------------------------------------------------
# $func579
# ------------------------------------------------------------
def func579(arg0):
    store32(40604, arg0)

# ------------------------------------------------------------
# $func580
# ------------------------------------------------------------
def func580(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if load8u(9163793):
            store32(v1 + 8, arg0)
            store32(v1 + 12, load8u(9163792))
            arg0 = load32(9213808)
            if load8u(9147210):
                func41(42, 9173808, arg0, (v1 + 8), 2)
                break
            v3 = (arg0 << 2)
            v2 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg0:
                # TODO: memory.copy []
            # call_indirect[load32(9214160)]
            break
        store32(40604, arg0)
        break
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $func581
# ------------------------------------------------------------
def func581(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if (arg0 != 18):
            store32(40604, arg0)
            break
        if (load8u(9163793) == 0):
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
        v2 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy []
        # call_indirect[load32(9213928)]
        break
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $rd
# Export: rd
# ------------------------------------------------------------
def rd(arg0, arg1, arg2, arg3, arg4):
    """Exported as rd."""
    v7 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    store32(9163784, arg1)
    store32(9163788, arg1)
    store8(9142906, arg4)
    store8(59181, (arg2 == 3))
    store8(9568060, (arg3 != 0))
    arg1 = load8u(9142916)
    store32(9671164, (1.0 if load8u(9142916) else arg0))
    if (u(arg2) <= u(2)):
        store32(51788, load32(((arg2 << 2) + 10152)))
    if arg1:
        arg4 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        arg1 = func26(8160)
        while True:  # $label0
            arg2 = (v5 << 2)
            arg3 = ((v6 * 404) + 9568096)
            store32((arg1 + (v5 << 2)), load32(((v6 * 404) + 9568096) + 200))
            store32((arg1 + (arg2 | 4)), load32(arg3 + 216))
            store32((arg1 + (arg2 | 8)), load32(arg3 + 220))
            store32((arg1 + (arg2 | 12)), ((load32(arg3 + 264) & -5) == 0))
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
    while True:  # block $label2
        while True:  # block $label3
            if load8u(9147212):
                while True:  # block $label1
                    if (load8u(9147152) == 0):
                        break
                    arg1 = load32(9561752)
                    if (load32(9561752) == 0):
                        break
                    if (arg1 == load32(9561756)):
                        break
                    store32(9147288, 0)
                    store32(9142892, 0)
                    break
                    break
                func319()
                break
            while True:  # block $label4
                arg1 = load32(9671136)
                if (u(load32(9671136)) < u(4)):
                    break
                arg4 = load32(9671128)
                arg2 = 3
                while True:  # $label6
                    while True:  # block $label5
                        arg3 = (arg4 + (arg2 * 132))
                        if (load8u((arg4 + (arg2 * 132)) + 125) == 3):
                            break
                        if (load32(arg3 + 28) == 0):
                            break
                        if (load32(load32(9142424) + 48) == 0):
                            break
                        arg1 = load32(9671136)
                        arg4 = load32(9671128)
                        break
                    arg2 = (arg2 + 1)
                    if (u((arg2 + 1)) < u(arg1)):
                        continue
                    break
                arg2 = 3
                if (u(arg1) <= u(3)):
                    break
                while True:  # $label14
                    while True:  # block $label7
                        arg3 = (arg4 + (arg2 * 132))
                        if (load8u((arg4 + (arg2 * 132)) + 125) == 3):
                            break
                        if (load32(arg3 + 28) == 0):
                            break
                        v5 = 0
                        v6 = load8u(arg3 + 122)
                        while True:  # block $label9
                            while True:  # block $label8
                                arg1 = load32(load32(9142424) + 48)
                                if (load32(load32(9142424) + 48) == 0):
                                    break
                                arg4 = load32(((v6 * 404) + 9568096) + 216)
                                if (load32(((v6 * 404) + 9568096) + 216) == 0):
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
                                            if (u(load16u((v12 + ((v14 + (v9 * (arg1 + v8))) << 1)))) > u(1)):
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
                                    raise RuntimeError('unreachable')
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
                        arg4 = load32(9671128)
                        break
                    arg2 = (arg2 + 1)
                    if (u((arg2 + 1)) < u(arg1)):
                        continue
                    break
                break
            if (load32(9142892) == 0):
                break
            arg3 = load32(9142424)
            arg4 = load32(9561692)
            arg1 = 0
            while True:  # $label15
                arg2 = (arg4 + (arg1 * 286704))
                store32((arg4 + (arg1 * 286704)) + 283868, load32(9561460))
                # TODO: memory.copy []
                store32((arg2 + 284000), load32(arg3 + 40))
                store32((arg2 + 284136), load32(arg3 + 36))
                arg1 = (arg1 + 1)
                if (u((arg1 + 1)) < u(load32(9142892))):
                    continue
                break
            break
        arg4 = 0
        while True:  # block $label16
            arg3 = load32(9140328)
            if (load32(9140328) == 0):
                break
            arg1 = load32(9142440)
            arg1 = (load32(9142440) * arg1)
            arg2 = 0
            if (u(arg3) >= u(4)):
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
            if ((arg3 & 3) == 0):
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
        if (load32(9681936) == 0):
            arg1 = func26(16)
            arg2 = (arg4 << 2)
            store32(func26(16) + 4, (arg4 << 2))
            store32(arg1, func26((-1 if (u(arg2) > u(1073741823)) else (arg4 << 4))))
            store64(arg1 + 8, 206158430208)
            store32(9681936, arg1)
        while True:  # block $label19
            if ((load8u(9147212) | load8u(9147152)) == 0):
                func169()
                break
            if (load32(arg1 + 8) == 0):
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
                while True:  # block $label22
                    while True:  # block $label20
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
                        if (load32((v10 - 16)) == 0):
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
                if (u((v11 + 4)) < u(load32(arg1 + 8))):
                    continue
                break
            break
        while True:  # block $label25
            if (load8u(9147212) == 0):
                break
            if (load32(load32(9142424) + 32) == 0):
                break
            arg1 = load32(9684368)
            store32(v7 + 24, load32(9684368))
            store32(v7 + 60, load32(9684364))
            arg0 = load32(9684356)
            # TODO: f64.promote_f32 []
            store32(v7 + 16, load32(9684356))
            store32(v7 + 56, (load32(9684372) - arg1))
            v15 = load32(9684340)
            # TODO: f64.promote_f32 []
            store32(v7 + 32, (load32(9684348) - load32(9684340)))
            v16 = load32(9684344)
            # TODO: f64.promote_f32 []
            store32(v7 + 40, (load32(9684352) - load32(9684344)))
            # TODO: f64.promote_f32 []
            store32(v7 + 48, (load32(9684360) - arg0))
            # TODO: f64.promote_f32 []
            store32(v7, v15)
            # TODO: f64.promote_f32 []
            store32(v7 + 8, v16)
            a_b()
            break
        func152()
        break
    G.global0 = (v7 - -64)

# ------------------------------------------------------------
# $ye
# Export: ye
# ------------------------------------------------------------
def ye(arg0):
    """Exported as ye."""
    store8(9147152, 1)
    if (load8u(9147212) == 0):
        store32(9142892, 3)
        v1 = load32(9142424)
        if load32(9142424):
            store32(9142424, 0)
        v2 = (arg0 << 2)
        v1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        store32(9142428, arg0)
        store32(9142424, v1)
        if arg0:
            # TODO: memory.copy []
        else:
        store32(load32(v1), arg0)
    return v2

# ------------------------------------------------------------
# $func586
# ------------------------------------------------------------
def func586(arg0, arg1, arg2):
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    arg2 = 0
    while True:  # block $label0
        if (load8u(9142917) | load8u(9147152)):
            break
        v4 = load32(59164)
        v5 = load32(9561692)
        while True:  # block $label1
            v6 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
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
        if (load32(arg0 + 8) == 0):
            if load8u((load32(9143004) + (load32((v5 + (arg2 * 286704)) + 283908) + (load32(9142872) * v6)))):
                break
        arg2 = load32(arg0 + 4)
        v8 = load32(arg0)
        arg0 = 0
        while True:  # block $label3
            if (u(v6) < u(2)):
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
        store32(v3 + 12, (v7 == 0))
        store32(v3 + 8, (v5 + (arg0 * 286704)))
        break
    G.global0 = (v3 + 32)

# ------------------------------------------------------------
# $func587
# ------------------------------------------------------------
def func587(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg1 = 0
    v3 = load32(9142892)
    v4 = load32(arg0)
    while True:  # block $label0
        if load8u(9147210):
            if (u(v3) < u(2)):
                break
            v5 = load32(59164)
            v6 = load32(9561692)
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
        arg1 = load32(9142872)
        break
    while True:  # block $label2
        if (v4 == 0):
            break
        if (arg1 == v4):
            break
        if (u(v3) <= u(v4)):
            break
        v3 = load32(9142424)
        if load32(load32(9142424) + 180):
            if (u(load32(9142848)) < u((load32(v3 + 72) * 2400))):
                break
        store32(arg2, load32(arg0 + 4))
        store32(arg2 + 4, load32(arg0 + 8))
        store32(arg2 + 8, load32(arg0 + 12))
        store32(arg2 + 12, load32(arg0 + 16))
        func322(v4, arg1, arg2)
        break
    G.global0 = (arg2 + 16)

# ------------------------------------------------------------
# $func588
# ------------------------------------------------------------
def func588(arg0, arg1):

# ------------------------------------------------------------
# $pb
# Export: pb
# ------------------------------------------------------------
def pb(arg0):
    """Exported as pb."""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg0 = (load32(9671128) + (arg0 * 132))
    v2 = load16u((load32(9671128) + (arg0 * 132)) + 114)
    v3 = load16u(arg0 + 112)
    store32(v1, load32(((load8u(arg0 + 122) * 404) + 9568096) + 84))
    store32(v1 + 4, v3)
    store32(v1 + 8, v2)
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $mb
# Export: mb
# ------------------------------------------------------------
def mb(arg0):
    """Exported as mb."""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store8(9681824, arg0)
    if (load32(9216064) == 0):
        store32(41088, 7)
        store64(v1, 7)
    store32(9216064, 58)
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $func591
# ------------------------------------------------------------
def func591(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func326(arg0)

# ------------------------------------------------------------
# $func592
# ------------------------------------------------------------
def func592(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func332(-1)

# ------------------------------------------------------------
# $func593
# ------------------------------------------------------------
def func593(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func327(arg0)

# ------------------------------------------------------------
# $func594
# ------------------------------------------------------------
def func594(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func328(arg0)

# ------------------------------------------------------------
# $func595
# ------------------------------------------------------------
def func595(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func329(arg0)

# ------------------------------------------------------------
# $func596
# ------------------------------------------------------------
def func596(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        store32(9143000, 0)
        arg0 = load32(9213820)
        if load32(9213820):
            func47((load32(9671128) + (arg0 * 132)))
            store32(9213820, 0)
        func45()
        v10 = (load32(9561692) + (load32(9142872) * 286704))
        while True:  # $label13
            arg0 = 0
            while True:  # block $label0
                arg1 = ((v5 * 404) + 9568096)
                if load32(((v5 * 404) + 9568096) + 264):
                    break
                if (load32(arg1 + 268) == 1):
                    break
                arg0 = (load32(arg1 + 92) != 0)
                break
            while True:  # block $label1
                if (arg0 == 0):
                    break
                if (v5 == load32(38456)):
                    break
                if (v5 == load32(38764)):
                    break
                v7 = load32(((v10 + (v5 << 2)) + 284636))
                if (load32(((v10 + (v5 << 2)) + 284636)) == 0):
                    break
                v8 = 0
                v9 = load32(v7 + 8)
                if (load32(v7 + 8) == 0):
                    break
                while True:  # $label12
                    while True:  # block $label2
                        arg0 = load32((load32(v7) + (v8 << 2)))
                        if (load32((load32(v7) + (v8 << 2))) == 0):
                            break
                        v2 = load32(9671128)
                        arg1 = (load32(9671128) + (arg0 * 132))
                        if (load8u(9147152) == 0):
                            if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(arg1 + 110))))) == 0):
                                break
                            if (load32((load32(9215884) + (load32(arg1 + 44) << 4)) + 4) == 20):
                                break
                            if (load8u(arg1 + 127) == 6):
                                break
                        v6 = load32(arg1 + 28)
                        while True:  # block $label3
                            arg0 = load32(9215928)
                            if (load32(9215928) == 0):
                                break
                            v3 = load32(arg0 + 8)
                            if (load32(arg0 + 8) == 0):
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
                        while True:  # block $label5
                            arg0 = load32(9215932)
                            if (load32(9215932) == 0):
                                break
                            v3 = load32(arg0 + 8)
                            if (load32(arg0 + 8) == 0):
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
                        while True:  # block $label7
                            arg0 = load32(9215936)
                            if (load32(9215936) == 0):
                                break
                            v3 = load32(arg0 + 8)
                            if (load32(arg0 + 8) == 0):
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
                        while True:  # block $label9
                            arg0 = load32(9215940)
                            if (load32(9215940) == 0):
                                break
                            v3 = load32(arg0 + 8)
                            if (load32(arg0 + 8) == 0):
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
                        while True:  # block $label11
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
                    if (u((v8 + 1)) < u(v9)):
                        continue
                    break
                break
            v5 = (v5 + 1)
            if ((v5 + 1) != 255):
                continue
            break

# ------------------------------------------------------------
# $func597
# ------------------------------------------------------------
def func597(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        arg1 = 0
        store32(9143000, 0)
        arg0 = load32(9213820)
        if load32(9213820):
            func47((load32(9671128) + (arg0 * 132)))
            store32(9213820, 0)
        func45()
        v10 = (load32(9561692) + (load32(9142872) * 286704))
        while True:  # $label13
            arg0 = 0
            while True:  # block $label0
                v2 = ((arg1 * 404) + 9568096)
                if load32(((arg1 * 404) + 9568096) + 264):
                    break
                if (load32(v2 + 268) == 1):
                    break
                arg0 = (load32(v2 + 92) != 0)
                break
            while True:  # block $label1
                if (arg0 == 0):
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
                if (load32(((v10 + (arg1 << 2)) + 284636)) == 0):
                    break
                v8 = 0
                v9 = load32(v7 + 8)
                if (load32(v7 + 8) == 0):
                    break
                while True:  # $label12
                    while True:  # block $label2
                        arg0 = load32((load32(v7) + (v8 << 2)))
                        if (load32((load32(v7) + (v8 << 2))) == 0):
                            break
                        v3 = load32(9671128)
                        v2 = (load32(9671128) + (arg0 * 132))
                        if (load8u(9147152) == 0):
                            if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v2 + 110))))) == 0):
                                break
                            if (load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) == 20):
                                break
                            if (load8u(v2 + 127) == 6):
                                break
                        v6 = load32(v2 + 28)
                        while True:  # block $label3
                            arg0 = load32(9215928)
                            if (load32(9215928) == 0):
                                break
                            v4 = load32(arg0 + 8)
                            if (load32(arg0 + 8) == 0):
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
                        while True:  # block $label5
                            arg0 = load32(9215932)
                            if (load32(9215932) == 0):
                                break
                            v4 = load32(arg0 + 8)
                            if (load32(arg0 + 8) == 0):
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
                        while True:  # block $label7
                            arg0 = load32(9215936)
                            if (load32(9215936) == 0):
                                break
                            v4 = load32(arg0 + 8)
                            if (load32(arg0 + 8) == 0):
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
                        while True:  # block $label9
                            arg0 = load32(9215940)
                            if (load32(9215940) == 0):
                                break
                            v4 = load32(arg0 + 8)
                            if (load32(arg0 + 8) == 0):
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
                        while True:  # block $label11
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
                    if (u((v8 + 1)) < u(v9)):
                        continue
                    break
                break
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != 255):
                continue
            break

# ------------------------------------------------------------
# $func598
# ------------------------------------------------------------
def func598(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func325(arg0)

# ------------------------------------------------------------
# $func599
# ------------------------------------------------------------
def func599(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func333(-1)

# ------------------------------------------------------------
# $func600
# ------------------------------------------------------------
def func600(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func334(arg0)

# ------------------------------------------------------------
# $func601
# ------------------------------------------------------------
def func601(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()

# ------------------------------------------------------------
# $func602
# ------------------------------------------------------------
def func602(arg0, arg1):
    if arg0:
        if (load8u(9147152) == 0):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func331(arg0)

# ------------------------------------------------------------
# $func603
# ------------------------------------------------------------
def func603(arg0):
    if (load8u(9163793) == 0):
        store8(9216068, 1)
        a_b()

# ------------------------------------------------------------
# $func604
# ------------------------------------------------------------
def func604(arg0):
    v7 = load32(9561692)
    while True:  # $label4
        while True:  # block $label0
            arg0 = ((v3 * 404) + 9568096)
            if (load32(((v3 * 404) + 9568096) + 264) != 2):
                break
            if (u(load32(arg0 + 268)) > u(2)):
                break
            v4 = load32(((v7 + (v3 << 2)) + 284636))
            if (load32(((v7 + (v3 << 2)) + 284636)) == 0):
                break
            v5 = 0
            arg0 = load32(v4 + 8)
            if (load32(v4 + 8) == 0):
                break
            while True:  # $label3
                while True:  # block $label1
                    v1 = load32((load32(v4) + (v5 << 2)))
                    if (load32((load32(v4) + (v5 << 2))) == 0):
                        break
                    v2 = load32(9671128)
                    v1 = (load32(9671128) + (v1 * 132))
                    v6 = load32((load32(9671128) + (v1 * 132)) + 36)
                    if (load32((load32(9671128) + (v1 * 132)) + 36) == 0):
                        break
                    if (load32(9142872) != load16u((v2 + (v6 * 132)) + 110)):
                        break
                    v6 = load32(v1 + 28)
                    while True:  # block $label2
                        v1 = load32(9681836)
                        if (load32(9681836) != load32(9681832)):
                            arg0 = load32(9681828)
                            break
                        arg0 = (load32(9681840) + v1)
                        store32(9681832, (load32(9681840) + v1))
                        v2 = load32(9681828)
                        arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                        if v1:
                            # TODO: memory.copy []
                        if v2:
                            v1 = load32(9681836)
                        store32(9681828, arg0)
                        break
                    store32(9681836, (v1 + 1))
                    store32((arg0 + (v1 << 2)), v6)
                    arg0 = load32(v4 + 8)
                    break
                v5 = (v5 + 1)
                if (u((v5 + 1)) < u(arg0)):
                    continue
                break
            break
        v3 = (v3 + 1)
        if ((v3 + 1) != 255):
            continue
        break
    func172(1)

# ------------------------------------------------------------
# $xc
# Export: xc
# ------------------------------------------------------------
def xc(arg0, arg1):
    """Exported as xc."""
    while True:  # block $label0
        v3 = load32(9142844)
        if (u(load32(9142844)) < u(4)):
            break
        v4 = load32(9671128)
        v2 = 3
        while True:  # $label1
            v5 = (v4 + (v2 * 132))
            if (arg0 == load16u((v4 + (v2 * 132)) + 110)):
                if (load8u(v5 + 122) == arg1):
                    break
            v2 = (v2 + 1)
            if ((v2 + 1) != v3):
                continue
            break
        return 0
        break
    return v2

# ------------------------------------------------------------
# $pd
# Export: pd
# ------------------------------------------------------------
def pd(arg0):
    """Exported as pd."""
    store32(9143000, 0)
    v1 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (v1 * 132)))
        store32(9213820, 0)
    func45()
    store8(9142906, arg0)

# ------------------------------------------------------------
# $ic
# Export: ic
# ------------------------------------------------------------
def ic():
    """Exported as ic."""
    store8(9140304, 0)

# ------------------------------------------------------------
# $ad
# Export: ad
# ------------------------------------------------------------
def ad(arg0, arg1, arg2):
    """Exported as ad."""
    if (arg0 >= 0):
        store32(load32(9568076) + 108, arg0)
    if (arg1 >= 0):
        store32(load32(9568076) + 112, arg1)
    if (arg2 >= 0):
        store32(load32(9568076) + 116, arg2)

# ------------------------------------------------------------
# $zd
# Export: zd
# ------------------------------------------------------------
def zd(arg0):
    """Exported as zd."""
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        v1 = load32(9568088)
        if load32(load32(9568088) + 104):
            arg0 = load32(v1 + 96)
            break
        v3 = load32(v1 + 100)
        while True:  # block $label2
            while True:  # block $label1
                if (arg0 == 0):
                    if (v3 == 0):
                        break
                    v3 = load32(v1 + 96)
                    arg0 = 0
                    break
                while True:  # block $label3
                    if v3:
                        v3 = load32(v1 + 96)
                        arg0 = 0
                        break
                    arg0 = load32(v1 + 108)
                    store32(v1 + 100, load32(v1 + 108))
                    v2 = load32(v1 + 96)
                    v3 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                    if v2:
                    else:
                    arg0 = 0
                    store32(v1 + 96, v3)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v3 + (arg0 << 2)), 2147483647)
                while True:  # block $label4
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v2 = v3
                        break
                    v2 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy []
                    store32(v1 + 96, v2)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v2 + (arg0 << 2)), 2147483647)
                while True:  # block $label5
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v3 = v2
                        break
                    v3 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                    if arg0:
                        # TODO: memory.copy []
                    store32(v1 + 96, v3)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v3 + (arg0 << 2)), 2147483647)
                while True:  # block $label6
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v2 = v3
                        break
                    v2 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy []
                    store32(v1 + 96, v2)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v2 + (arg0 << 2)), 2147483647)
                while True:  # block $label7
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v3 = v2
                        break
                    v3 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                    if arg0:
                        # TODO: memory.copy []
                    store32(v1 + 96, v3)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v3 + (arg0 << 2)), 2147483647)
                while True:  # block $label8
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v2 = v3
                        break
                    v2 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy []
                    store32(v1 + 96, v2)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v2 + (arg0 << 2)), 2147483647)
                while True:  # block $label9
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v3 = v2
                        break
                    v3 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                    if arg0:
                        # TODO: memory.copy []
                    store32(v1 + 96, v3)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v3 + (arg0 << 2)), 2147483647)
                while True:  # block $label10
                    v2 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        arg0 = v3
                        break
                    arg0 = (load32(v1 + 108) + v2)
                    store32(v1 + 100, (load32(v1 + 108) + v2))
                    arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                    if v2:
                        # TODO: memory.copy []
                    store32(v1 + 96, arg0)
                    v2 = load32(v1 + 104)
                    break
                store32(v1 + 104, (v2 + 1))
                store32((arg0 + (v2 << 2)), 2147483647)
                store32(arg0 + 20, 0)
                store32(arg0 + 12, 50)
                break
                break
            arg0 = load32(v1 + 108)
            store32(v1 + 100, load32(v1 + 108))
            v2 = load32(v1 + 96)
            v3 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if v2:
            else:
            arg0 = 0
            store32(v1 + 96, v3)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v3 + (arg0 << 2)), 0)
        while True:  # block $label11
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v2 = v3
                break
            v2 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(v1 + 96, v2)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v2 + (arg0 << 2)), 0)
        while True:  # block $label12
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v3 = v2
                break
            v3 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(v1 + 96, v3)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v3 + (arg0 << 2)), 0)
        while True:  # block $label13
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v2 = v3
                break
            v2 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(v1 + 96, v2)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v2 + (arg0 << 2)), 0)
        while True:  # block $label14
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v3 = v2
                break
            v3 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(v1 + 96, v3)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v3 + (arg0 << 2)), 0)
        while True:  # block $label15
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v2 = v3
                break
            v2 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(v1 + 96, v2)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v2 + (arg0 << 2)), 0)
        while True:  # block $label16
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v3 = v2
                break
            v3 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(v1 + 96, v3)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v3 + (arg0 << 2)), 0)
        while True:  # block $label17
            v2 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                arg0 = v3
                break
            arg0 = (load32(v1 + 108) + v2)
            store32(v1 + 100, (load32(v1 + 108) + v2))
            arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if v2:
                # TODO: memory.copy []
            store32(v1 + 96, arg0)
            v2 = load32(v1 + 104)
            break
        store32(v1 + 104, (v2 + 1))
        store32((arg0 + (v2 << 2)), 0)
        store64(arg0 + 8, 214748364850)
        store32(arg0, 5)
        break
    v3 = 50
    v2 = load32(arg0 + 8)
    v5 = load64(arg0)
    v6 = load64(arg0 + 16)
    v7 = load64(arg0 + 24)
    store32(v4 + 32, 0)
    store64(v4 + 24, v7)
    store64(v4 + 16, v6)
    store32(v4 + 12, v3)
    store64(v4, v5)
    store32(v4 + 8, v2)
    G.global0 = (v4 + 48)
    return v4

# ------------------------------------------------------------
# $dd
# Export: dd
# ------------------------------------------------------------
def dd(arg0):
    """Exported as dd."""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg0 = ((9684460 if (arg0 == 1) else 9684476) if arg0 else 9684444)
    v2 = load32(((9684460 if (arg0 == 1) else 9684476) if arg0 else 9684444))
    store32(v1 + 4, load32(arg0 + 8))
    store32(v1, v2)
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $be
# Export: be
# ------------------------------------------------------------
def be():
    """Exported as be."""
    while True:  # block $label0
        v0 = load32(9142440)
        if (load32(9142440) <= 0):
            v1 = v0
            break
        v4 = load32(9671128)
        v5 = load32(9142840)
        v1 = v0
        while True:  # $label2
            v6 = (v6 + 1)
            v3 = 0
            while True:  # $label1
                v2 = (v1 + 2)
                v3 = (v3 + 1)
                v2 = (v4 + (load32((v5 + ((v6 + (((v1 + 2) + (v3 + 1)) * v2)) << 2))) * 132))
                if (load8u((v4 + (load32((v5 + ((v6 + (((v1 + 2) + (v3 + 1)) * v2)) << 2))) * 132)) + 122) == 7):
                    store8(v2 + 122, 0)
                    v4 = load32(9671128)
                    v5 = load32(9142840)
                    v1 = load32(9142440)
                if (v0 != v3):
                    continue
                break
            if (v0 != v6):
                continue
            break
        break
    if (u(((v1 * v1) * 80)) > u(65535)):
        while True:  # $label3
            v3 = load32(9147312)
            v0 = load32(9147324)
            v0 = ((load32(9147324) << 11) ^ v0)
            v4 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v0)
            store32(9147324, (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v0))
            v0 = load32(9147320)
            v0 = ((load32(9147320) << 11) ^ v0)
            v5 = (((((((load32(9147320) << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v4)
            store32(9147320, (((((((load32(9147320) << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v4))
            v0 = load32(9147316)
            v0 = ((load32(9147316) << 11) ^ v0)
            v2 = (((((((load32(9147316) << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v5 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v5)
            store32(9147316, (((((((load32(9147316) << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v5 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v5))
            v0 = (v3 ^ (v3 << 11))
            v0 = ((((((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v2)
            store32(9147312, ((((((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v2))
            v7 = (v7 + 1)
            v1 = load32(9142440)
            if (u((v7 + 1)) < u(((((load32(9142440) * v1) * 80) & 0xFFFFFFFF) >> 16))):
                continue
            break

# ------------------------------------------------------------
# $ae
# Export: ae
# ------------------------------------------------------------
def ae():
    """Exported as ae."""
    v1 = load32(9142440)
    if (load32(9142440) > 0):
        v5 = load32(9671128)
        v6 = load32(9142840)
        v0 = v1
        while True:  # $label1
            v4 = (v4 + 1)
            v3 = 0
            while True:  # $label0
                v2 = (v0 + 2)
                v3 = (v3 + 1)
                v2 = (v5 + (load32((v6 + ((v4 + (((v0 + 2) + (v3 + 1)) * v2)) << 2))) * 132))
                if (u(((load8u((v5 + (load32((v6 + ((v4 + (((v0 + 2) + (v3 + 1)) * v2)) << 2))) * 132)) + 122) - 21) & 255)) <= u(1)):
                    store8(v2 + 122, 0)
                    v5 = load32(9671128)
                    v6 = load32(9142840)
                    v0 = load32(9142440)
                if (v1 != v3):
                    continue
                break
            if (v1 != v4):
                continue
            break
    v3 = 0
    v5 = 0
    v0 = load32(9142440)
    v0 = ((load32(9142440) << 3) * v0)
    if (u(((load32(9142440) << 3) * v0)) >= u(65536)):
        v6 = ((v0 & 0xFFFFFFFF) >> 16)
        while True:  # $label2
            v0 = load32(9147324)
            v1 = load32(9147312)
            store32(9147324, load32(9147312))
            v2 = load32(9147320)
            v0 = (v0 ^ (v0 << 11))
            v4 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0)
            store32(9147320, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0))
            v1 = load32(9147316)
            v0 = (v2 ^ (v2 << 11))
            v2 = ((((((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v4)
            store32(9147316, ((((((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v4))
            v0 = (v1 ^ (v1 << 11))
            v1 = ((((((v1 ^ (v1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v2)
            store32(9147312, ((((((v1 ^ (v1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v2))
            v0 = load32(9142440)
            v3 = (v3 + 1)
            if ((v3 + 1) != v6):
                continue
            break
        while True:  # $label3
            v0 = load32(9147324)
            v1 = load32(9147312)
            store32(9147324, load32(9147312))
            v2 = load32(9147320)
            v0 = (v0 ^ (v0 << 11))
            v3 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0)
            store32(9147320, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0))
            v1 = load32(9147316)
            v0 = (v2 ^ (v2 << 11))
            v2 = ((((((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v3)
            store32(9147316, ((((((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v3))
            v0 = (v1 ^ (v1 << 11))
            v1 = ((((((v1 ^ (v1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v2)
            store32(9147312, ((((((v1 ^ (v1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v2))
            v0 = load32(9142440)
            v5 = (v5 + 1)
            if ((v5 + 1) != v6):
                continue
            break

# ------------------------------------------------------------
# $bd
# Export: bd
# ------------------------------------------------------------
def bd(arg0, arg1, arg2):
    """Exported as bd."""
    v3 = (G.global0 - 336)
    G.global0 = (G.global0 - 336)
    while True:  # block $label5
        if (arg1 == 0):
            while True:  # block $label2
                while True:  # block $label1
                    while True:  # block $label0
                        # br_table[arg0]
                        break
                        break
                    arg2 = (load32(9568064) + (arg2 << 7))
                    arg0 = ((load32(9568064) + (arg2 << 7)) + 128)
                    arg1 = load32(9568068)
                    if (((load32(9568064) + (arg2 << 7)) + 128) != load32(9568068)):
                        while True:  # $label3
                            v6 = load32(arg2)
                            if load32(arg2):
                                store32(arg2 + 4, v6)
                                store32(arg2 + 8, 0)
                            store32(arg2, load32(arg0))
                            store32(arg2 + 4, load32(arg0 + 4))
                            store32(arg2 + 8, load32(arg0 + 8))
                            store32(arg0 + 8, 0)
                            store64(arg0, 0)
                            v6 = load32(arg2 + 12)
                            if load32(arg2 + 12):
                                store32(arg2 + 16, v6)
                                store32(arg2 + 20, 0)
                            store32(arg2 + 12, load32(arg0 + 12))
                            store32(arg2 + 16, load32(arg0 + 16))
                            store32(arg2 + 20, load32(arg0 + 20))
                            store32(arg0 + 20, 0)
                            store64(arg0 + 12, 0)
                            # TODO: memory.copy []
                            arg2 = (arg2 + 128)
                            arg0 = (arg0 + 128)
                            if ((arg0 + 128) != arg1):
                                continue
                            break
                        arg0 = load32(9568068)
                    if (arg0 != arg2):
                        while True:  # $label4
                            arg1 = (arg0 - 128)
                            v6 = load32((arg0 - 128) + 12)
                            if load32((arg0 - 128) + 12):
                                store32((arg0 - 112), v6)
                            v6 = load32(arg1)
                            if load32(arg1):
                                store32((arg0 - 124), v6)
                            arg0 = arg1
                            if (arg1 != arg2):
                                continue
                            break
                    store32(9568068, arg2)
                    break
                    break
                v6 = load32(9568076)
                arg1 = (load32(load32(9568076)) + (arg2 * 196))
                arg0 = (arg1 + 196)
                arg0 = (load32(v6 + 4) - arg0)
                # TODO: memory.copy []
                store32(v6 + 4, (arg1 + ((arg0 // 196) * 196)))
                break
                break
            v6 = load32(9568076)
            arg1 = (load32(load32(9568076) + 12) + (arg2 * 196))
            arg0 = (arg1 + 196)
            arg0 = (load32(v6 + 16) - arg0)
            # TODO: memory.copy []
            store32(v6 + 16, (arg1 + ((arg0 // 196) * 196)))
            break
        v7 = load32(9568076)
        if (load32(9568076) == 0):
            break
        while True:  # block $label18
            while True:  # block $label20
                while True:  # block $label12
                    while True:  # block $label9
                        while True:  # block $label11
                            if (arg0 == 0):
                                store64(v3 + 224, 0)
                                store64(v3 + 216, 0)
                                store64(v3 + 208, 0)
                                arg0 = 0
                                store32(v3 + 332, 0)
                                store32(v3 + 316, load32(v7 + 108))
                                store32(v3 + 320, load32(v7 + 112))
                                store32(v3 + 324, load32(v7 + 116))
                                store32(v3 + 328, load32(v7 + 120))
                                store32(v3 + 312, load32(v7 + 104))
                                while True:  # block $label6
                                    v8 = load32(v7 + 104)
                                    if (load32(v7 + 104) == 0):
                                        break
                                    if (u(v8) >= u(4)):
                                        arg2 = (v8 & -4)
                                        while True:  # $label7
                                            v4 = (v3 + 232)
                                            v9 = (arg0 << 1)
                                            v5 = (v7 + 24)
                                            store16(((v3 + 232) + (arg0 << 1)), load16u(((v7 + 24) + v9)))
                                            arg1 = (v9 | 2)
                                            store16((v4 + (v9 | 2)), load16u((arg1 + v5)))
                                            arg1 = (v9 | 4)
                                            store16((v4 + (v9 | 4)), load16u((arg1 + v5)))
                                            arg1 = (v9 | 6)
                                            store16((v4 + (v9 | 6)), load16u((arg1 + v5)))
                                            arg0 = (arg0 + 4)
                                            v6 = (v6 + 4)
                                            if ((v6 + 4) != arg2):
                                                continue
                                            break
                                    v6 = (v8 & 3)
                                    if ((v8 & 3) == 0):
                                        break
                                    arg2 = 0
                                    while True:  # $label8
                                        arg1 = (arg0 << 1)
                                        store16((v3 + (arg0 << 1)) + 232, load16u((arg1 + v7) + 24))
                                        arg0 = (arg0 + 1)
                                        arg2 = (arg2 + 1)
                                        if ((arg2 + 1) != v6):
                                            continue
                                        break
                                    break
                                if (load32(v7 + 4) == load32(v7)):
                                    break
                                arg1 = 0
                                v4 = 0
                                arg0 = 0
                                arg2 = 0
                                while True:  # $label13
                                    store64(v3 + 47, 0)
                                    store64(v3 + 40, 0)
                                    store64(v3 + 32, 0)
                                    store64(v3 + 24, 0)
                                    store64(v3 + 16, 0)
                                    store64(v3 + 8, 0)
                                    store32(v3 + 60, 1)
                                    store32(v3 + 56, func26(4))
                                    store32(v3 + 76, 1)
                                    store64(v3 + 64, 4294967296)
                                    store32(v3 + 72, func26(4))
                                    store32(v3 + 92, 1)
                                    store64(v3 + 80, 4294967296)
                                    store32(v3 + 88, func26(4))
                                    store32(v3 + 108, 1)
                                    store64(v3 + 96, 4294967296)
                                    store32(v3 + 104, func26(4))
                                    store32(v3 + 200, 0)
                                    store64(v3 + 112, 4294967296)
                                    func255((v3 + 8), (load32(v7) + (arg2 * 196)))
                                    while True:  # block $label10
                                        if (arg0 != v4):
                                            # TODO: memory.copy []
                                            arg0 = (arg0 + 196)
                                            store32(v3 + 212, (arg0 + 196))
                                            break
                                        v4 = (v4 - arg1)
                                        v5 = ((v4 - arg1) // 196)
                                        v6 = (((v4 - arg1) // 196) + 1)
                                        if (u((((v4 - arg1) // 196) + 1)) >= u(21913099)):
                                            break
                                        arg0 = (v5 << 1)
                                        v8 = (21913098 if (u(v5) >= u(10956549)) else ((v5 << 1) if (u(arg0) > u(v6)) else v6))
                                        if (21913098 if (u(v5) >= u(10956549)) else ((v5 << 1) if (u(arg0) > u(v6)) else v6)):
                                            if (u(v8) >= u(21913099)):
                                                break
                                        else:
                                        arg0 = 0
                                        v5 = (0 + (v5 * 196))
                                        # TODO: memory.copy []
                                        v6 = (v5 + ((v4 // -196) * 196))
                                        # TODO: memory.copy []
                                        v4 = (arg0 + (v8 * 196))
                                        store32(v3 + 216, (arg0 + (v8 * 196)))
                                        arg0 = (v5 + 196)
                                        store32(v3 + 212, (v5 + 196))
                                        store32(v3 + 208, v6)
                                        if arg1:
                                        arg1 = v6
                                        break
                                    arg2 = (arg2 + 1)
                                    if (u((arg2 + 1)) < u(((load32(v7 + 4) - load32(v7)) // 196))):
                                        continue
                                    break
                                break
                            arg2 = load32(9568088)
                            if (load32(9568088) == 0):
                                break
                            store64(v3 + 47, 0)
                            store64(v3 + 40, 0)
                            store64(v3 + 32, 0)
                            store64(v3 + 24, 0)
                            store64(v3 + 16, 0)
                            store32(v3 + 60, 1)
                            store64(v3 + 8, 0)
                            arg1 = func26(4)
                            store32(v3 + 76, 1)
                            store64((v3 - -64), 4294967296)
                            store32(v3 + 56, arg1)
                            arg1 = func26(4)
                            store32(v3 + 92, 1)
                            store64(v3 + 80, 4294967296)
                            store32(v3 + 72, arg1)
                            arg1 = func26(4)
                            store32(v3 + 108, 1)
                            store64(v3 + 96, 4294967296)
                            store32(v3 + 88, arg1)
                            arg1 = func26(4)
                            store64(v3 + 112, 4294967296)
                            store32(v3 + 104, arg1)
                            store32(v3 + 200, 0)
                            v9 = (v3 + 8)
                            func255((v3 + 8), arg2)
                            arg2 = load32(9568076)
                            arg1 = (arg0 == 1)
                            v11 = (load32(9568076) if (arg0 == 1) else (arg2 + 12))
                            arg0 = load32((load32(9568076) if (arg0 == 1) else (arg2 + 12)))
                            v5 = ((load32((arg2 + (0 if arg1 else 12))) + (load32(9568084) * 196)) - arg0)
                            v4 = (((load32((arg2 + (0 if arg1 else 12))) + (load32(9568084) * 196)) - arg0) // 196)
                            v7 = (load32((load32(9568076) if (arg0 == 1) else (arg2 + 12))) + ((((load32((arg2 + (0 if arg1 else 12))) + (load32(9568084) * 196)) - arg0) // 196) * 196))
                            while True:  # block $label14
                                arg2 = load32(v11 + 4)
                                arg1 = load32(v11 + 8)
                                if (u(load32(v11 + 4)) < u(load32(v11 + 8))):
                                    if (arg2 == v7):
                                        # TODO: memory.copy []
                                        store32(v11 + 4, (v7 + 196))
                                        break
                                    arg0 = arg2
                                    v6 = (v7 + 196)
                                    v5 = (arg2 - (v7 + 196))
                                    arg1 = (v7 + (((arg2 - (v7 + 196)) // 196) * 196))
                                    if (u(arg2) > u((v7 + (((arg2 - (v7 + 196)) // 196) * 196)))):
                                        while True:  # $label15
                                            # TODO: memory.copy []
                                            arg0 = (arg0 + 196)
                                            arg1 = (arg1 + 196)
                                            if (u((arg1 + 196)) < u(arg2)):
                                                continue
                                            break
                                    store32(v11 + 4, arg0)
                                    if (arg2 != v6):
                                        # TODO: memory.copy []
                                    else:
                                    # TODO: memory.copy []
                                    break
                                while True:  # block $label16
                                    v6 = (((arg2 - arg0) // 196) + 1)
                                    if (u((((arg2 - arg0) // 196) + 1)) < u(21913099)):
                                        arg2 = ((arg1 - arg0) // 196)
                                        arg1 = (((arg1 - arg0) // 196) << 1)
                                        arg2 = (21913098 if (u(arg2) >= u(10956549)) else ((((arg1 - arg0) // 196) << 1) if (u(arg1) > u(v6)) else v6))
                                        if (21913098 if (u(arg2) >= u(10956549)) else ((((arg1 - arg0) // 196) << 1) if (u(arg1) > u(v6)) else v6)):
                                            if (u(arg2) >= u(21913099)):
                                                break
                                        else:
                                        v8 = 0
                                        v6 = (v4 * 196)
                                        arg1 = (v8 + (v4 * 196))
                                        while True:  # block $label17
                                            arg2 = (arg2 * 196)
                                            if (v6 != (arg2 * 196)):
                                                arg2 = (arg2 + v8)
                                                break
                                            if (u(arg1) > u(v8)):
                                                arg2 = arg1
                                                arg1 = (arg1 + (((v4 + 1) // -2) * 196))
                                                break
                                            v6 = (1 if (u((v5 + 195)) < u(391)) else (v4 << 1))
                                            if (u((1 if (u((v5 + 195)) < u(391)) else (v4 << 1))) >= u(21913099)):
                                                break
                                            arg2 = (v6 * 196)
                                            arg1 = func26((v6 * 196))
                                            arg2 = (func26((v6 * 196)) + arg2)
                                            arg1 = (arg1 + (((v6 & 0xFFFFFFFF) >> 2) * 196))
                                            if (v8 == 0):
                                                break
                                            arg0 = load32(v11)
                                            break
                                        # TODO: memory.copy []
                                        v5 = (v7 - arg0)
                                        v6 = (arg1 + (((v7 - arg0) // -196) * 196))
                                        # TODO: memory.copy []
                                        arg1 = (arg1 + 196)
                                        arg0 = (load32(v11 + 4) - v7)
                                        # TODO: memory.copy []
                                        store32(v11 + 8, arg2)
                                        arg2 = load32(v11)
                                        store32(v11, v6)
                                        store32(v11 + 4, (arg1 + ((arg0 // 196) * 196)))
                                        if arg2:
                                        break
                                    func42()
                                    raise RuntimeError('unreachable')
                                    break
                                func68()
                                raise RuntimeError('unreachable')
                                break
                            break
                            break
                        func42()
                        raise RuntimeError('unreachable')
                        break
                    if (load32(v7 + 16) == load32(v7 + 12)):
                        break
                    arg1 = 0
                    v4 = 0
                    arg0 = 0
                    arg2 = 0
                    while True:  # $label21
                        store64(v3 + 47, 0)
                        store64(v3 + 40, 0)
                        store64(v3 + 32, 0)
                        store64(v3 + 24, 0)
                        store64(v3 + 16, 0)
                        store64(v3 + 8, 0)
                        store32(v3 + 60, 1)
                        store32(v3 + 56, func26(4))
                        store32(v3 + 76, 1)
                        store64(v3 + 64, 4294967296)
                        store32(v3 + 72, func26(4))
                        store32(v3 + 92, 1)
                        store64(v3 + 80, 4294967296)
                        store32(v3 + 88, func26(4))
                        store32(v3 + 108, 1)
                        store64(v3 + 96, 4294967296)
                        store32(v3 + 104, func26(4))
                        store32(v3 + 200, 0)
                        store64(v3 + 112, 4294967296)
                        func255((v3 + 8), (load32(v7 + 12) + (arg2 * 196)))
                        while True:  # block $label19
                            if (arg0 != v4):
                                # TODO: memory.copy []
                                arg0 = (arg0 + 196)
                                store32(v3 + 224, (arg0 + 196))
                                break
                            v4 = (v4 - arg1)
                            v5 = ((v4 - arg1) // 196)
                            v6 = (((v4 - arg1) // 196) + 1)
                            if (u((((v4 - arg1) // 196) + 1)) >= u(21913099)):
                                break
                            arg0 = (v5 << 1)
                            v8 = (21913098 if (u(v5) >= u(10956549)) else ((v5 << 1) if (u(arg0) > u(v6)) else v6))
                            if (21913098 if (u(v5) >= u(10956549)) else ((v5 << 1) if (u(arg0) > u(v6)) else v6)):
                                if (u(v8) >= u(21913099)):
                                    break
                            else:
                            arg0 = 0
                            v5 = (0 + (v5 * 196))
                            # TODO: memory.copy []
                            v6 = (v5 + ((v4 // -196) * 196))
                            # TODO: memory.copy []
                            v4 = (arg0 + (v8 * 196))
                            store32(v3 + 228, (arg0 + (v8 * 196)))
                            arg0 = (v5 + 196)
                            store32(v3 + 224, (v5 + 196))
                            store32(v3 + 220, v6)
                            if arg1:
                            arg1 = v6
                            break
                        arg2 = (arg2 + 1)
                        if (u((arg2 + 1)) < u(((load32(v7 + 16) - load32(v7 + 12)) // 196))):
                            continue
                        break
                    break
                    break
                func68()
                raise RuntimeError('unreachable')
                break
            func42()
            raise RuntimeError('unreachable')
            break
        v11 = load32(9568064)
        arg0 = (load32(9568064) + (load32(9568080) << 7))
        v6 = (v3 + 208)
        v12 = (G.global0 - 32)
        G.global0 = (G.global0 - 32)
        v7 = ((arg0 - v11) >> 7)
        while True:  # block $label36
            while True:  # block $label26
                while True:  # block $label25
                    while True:  # block $label22
                        arg1 = load32(9568068)
                        arg2 = load32(9568072)
                        if (u(load32(9568068)) < u(load32(9568072))):
                            if (arg0 == arg1):
                                store32(9568068, (func226(arg0, v6) + 128))
                                break
                            v5 = load32(9568068)
                            v9 = load32(9568068)
                            arg2 = arg0
                            v8 = (arg0 + 128)
                            arg0 = (arg0 + (v5 - (arg0 + 128)))
                            if (u(arg1) > u((arg0 + (v5 - (arg0 + 128))))):
                                v4 = arg0
                                while True:  # $label23
                                    store32(v9 + 8, 0)
                                    store64(v9, 0)
                                    store32(v9, load32(v4))
                                    store32(v9 + 4, load32(v4 + 4))
                                    store32(v9 + 8, load32(v4 + 8))
                                    store32(v4 + 8, 0)
                                    store64(v4, 0)
                                    store32(v9 + 20, 0)
                                    store64(v9 + 12, 0)
                                    store32(v9 + 12, load32(v4 + 12))
                                    store32(v9 + 16, load32(v4 + 16))
                                    store32(v9 + 20, load32(v4 + 20))
                                    store32(v4 + 20, 0)
                                    store64(v4 + 12, 0)
                                    # TODO: memory.copy []
                                    v9 = (v9 + 128)
                                    v4 = (v4 + 128)
                                    if (u((v4 + 128)) < u(arg1)):
                                        continue
                                    break
                            store32(9568068, v9)
                            if (v5 != v8):
                                while True:  # $label24
                                    arg1 = (v5 - 128)
                                    v8 = load32((v5 - 128))
                                    if load32((v5 - 128)):
                                        v4 = (v5 - 124)
                                        store32((v5 - 124), v8)
                                        store64(v4, 0)
                                        store32(arg1, 0)
                                    v4 = (arg0 - 128)
                                    store32(arg1, load32((arg0 - 128)))
                                    store32(arg1 + 4, load32(v4 + 4))
                                    store32(arg1 + 8, load32(v4 + 8))
                                    store64(v4 + 4, 0)
                                    store32(v4, 0)
                                    v9 = load32(arg1 + 12)
                                    if load32(arg1 + 12):
                                        v8 = (v5 - 112)
                                        store32((v5 - 112), v9)
                                        store64(v8, 0)
                                        store32(arg1 + 12, 0)
                                    store32(arg1 + 12, load32(v4 + 12))
                                    v8 = (v5 - 128)
                                    store32((v5 - 128) + 16, load32(v4 + 16))
                                    store32(v8 + 20, load32(v4 + 20))
                                    store32(v4 + 20, 0)
                                    store64(v4 + 12, 0)
                                    # TODO: memory.copy []
                                    v5 = arg1
                                    arg0 = v4
                                    if (v4 != arg2):
                                        continue
                                    break
                            arg0 = (v6 + (((u(arg2) <= u(v6)) & (u(load32(9568068)) > u(v6))) << 7))
                            if ((v6 + (((u(arg2) <= u(v6)) & (u(load32(9568068)) > u(v6))) << 7)) != arg2):
                            # TODO: memory.copy []
                            break
                        v5 = (((arg1 - v11) >> 7) + 1)
                        if (u((((arg1 - v11) >> 7) + 1)) >= u(33554432)):
                            break
                        store32(v12 + 28, 9568072)
                        arg2 = (arg2 - v11)
                        arg1 = ((arg2 - v11) >> 6)
                        v5 = (33554431 if (u(arg2) >= u(2147483520)) else (((arg2 - v11) >> 6) if (u(arg1) > u(v5)) else v5))
                        if (33554431 if (u(arg2) >= u(2147483520)) else (((arg2 - v11) >> 6) if (u(arg1) > u(v5)) else v5)):
                            if (u(v5) >= u(33554432)):
                                break
                        else:
                        arg2 = 0
                        store32(func26((v5 << 7)) + 12, 0)
                        arg1 = (arg2 + (v7 << 7))
                        store32(v12 + 20, (arg2 + (v7 << 7)))
                        store32(v12 + 24, (arg2 + (v5 << 7)))
                        store32(v12 + 16, arg1)
                        while True:  # block $label27
                            arg2 = (v12 + 12)
                            v11 = load32((v12 + 12) + 8)
                            if (load32((v12 + 12) + 8) != load32(arg2 + 12)):
                                break
                            v10 = load32(arg2 + 4)
                            v7 = load32(arg2)
                            if (u(load32(arg2 + 4)) > u(load32(arg2))):
                                v5 = (((((v10 - v7) >> 7) + 1) // -2) << 7)
                                arg1 = (v10 + (((((v10 - v7) >> 7) + 1) // -2) << 7))
                                if (v10 != v11):
                                    while True:  # $label28
                                        v4 = load32(arg1)
                                        if load32(arg1):
                                            store32(arg1 + 4, v4)
                                            store32(arg1 + 8, 0)
                                            store64(arg1, 0)
                                        store32(arg1, load32(v10))
                                        store32(arg1 + 4, load32(v10 + 4))
                                        store32(arg1 + 8, load32(v10 + 8))
                                        store32(v10 + 8, 0)
                                        store64(v10, 0)
                                        v4 = load32(arg1 + 12)
                                        if load32(arg1 + 12):
                                            store32(arg1 + 16, v4)
                                            store32(arg1 + 20, 0)
                                            store64(arg1 + 12, 0)
                                        store32(arg1 + 12, load32(v10 + 12))
                                        store32(arg1 + 16, load32(v10 + 16))
                                        store32(arg1 + 20, load32(v10 + 20))
                                        store32(v10 + 20, 0)
                                        store64(v10 + 12, 0)
                                        # TODO: memory.copy []
                                        arg1 = (arg1 + 128)
                                        v10 = (v10 + 128)
                                        if ((v10 + 128) != v11):
                                            continue
                                        break
                                    v11 = load32(arg2 + 4)
                                store32(arg2 + 8, arg1)
                                store32(arg2 + 4, (v5 + v11))
                                break
                            while True:  # block $label31
                                while True:  # block $label29
                                    v5 = (1 if (v7 == v11) else ((v11 - v7) >> 6))
                                    if (u((1 if (v7 == v11) else ((v11 - v7) >> 6))) < u(33554432)):
                                        arg1 = (v5 << 7)
                                        v9 = func26((v5 << 7))
                                        v8 = (func26((v5 << 7)) + arg1)
                                        v5 = (v9 + ((v5 << 5) & -128))
                                        if (v10 == v11):
                                            break
                                        v4 = (v5 + (v11 - v10))
                                        arg1 = v5
                                        while True:  # $label30
                                            store32(arg1, load32(v10))
                                            store32(arg1 + 4, load32(v10 + 4))
                                            store32(arg1 + 8, load32(v10 + 8))
                                            store32(v10 + 8, 0)
                                            store64(v10, 0)
                                            store32(arg1 + 12, load32(v10 + 12))
                                            store32(arg1 + 16, load32(v10 + 16))
                                            store32(arg1 + 20, load32(v10 + 20))
                                            store32(v10 + 20, 0)
                                            store64(v10 + 12, 0)
                                            # TODO: memory.copy []
                                            v10 = (v10 + 128)
                                            arg1 = (arg1 + 128)
                                            if ((arg1 + 128) != v4):
                                                continue
                                            break
                                        store32(arg2 + 12, v8)
                                        arg1 = load32(arg2 + 8)
                                        store32(arg2 + 8, v4)
                                        v8 = load32(arg2 + 4)
                                        store32(arg2 + 4, v5)
                                        v7 = load32(arg2)
                                        store32(arg2, v9)
                                        if (arg1 == v8):
                                            break
                                        while True:  # $label32
                                            v5 = (arg1 - 128)
                                            v4 = load32((arg1 - 128) + 12)
                                            if load32((arg1 - 128) + 12):
                                                store32((arg1 - 112), v4)
                                            v4 = load32(v5)
                                            if load32(v5):
                                                store32((arg1 - 124), v4)
                                            arg1 = v5
                                            if (v5 != v8):
                                                continue
                                            break
                                        break
                                    func68()
                                    raise RuntimeError('unreachable')
                                    break
                                store32(arg2 + 12, v8)
                                store32(arg2 + 8, v5)
                                store32(arg2 + 4, v5)
                                store32(arg2, v9)
                                break
                            if (v7 == 0):
                                break
                            break
                        store32(arg2 + 8, (load32(arg2 + 8) + 128))
                        v6 = arg2
                        v4 = load32(arg2 + 4)
                        v5 = load32(arg2 + 4)
                        v8 = load32(9568064)
                        arg1 = arg0
                        if (load32(9568064) != arg0):
                            while True:  # $label33
                                v5 = (v4 - 128)
                                store64((v4 - 128), 0)
                                store32(v5 + 8, 0)
                                arg2 = (arg0 - 128)
                                store32(v5, load32((arg0 - 128)))
                                store32(v5 + 4, load32(arg2 + 4))
                                store32(v5 + 8, load32(arg2 + 8))
                                store32(arg2 + 8, 0)
                                store64(arg2, 0)
                                store32(v5 + 20, 0)
                                store64(v5 + 12, 0)
                                store32(v5 + 12, load32(arg2 + 12))
                                store32(v5 + 16, load32(arg2 + 16))
                                store32(v5 + 20, load32(arg2 + 20))
                                store32(arg2 + 20, 0)
                                store64(arg2 + 12, 0)
                                # TODO: memory.copy []
                                v4 = v5
                                arg0 = arg2
                                if (arg2 != v8):
                                    continue
                                break
                        store32(v6 + 4, v5)
                        v4 = load32(v6 + 8)
                        arg0 = load32(9568068)
                        if (arg1 != load32(9568068)):
                            while True:  # $label34
                                store32(v4 + 8, 0)
                                store64(v4, 0)
                                store32(v4, load32(arg1))
                                store32(v4 + 4, load32(arg1 + 4))
                                store32(v4 + 8, load32(arg1 + 8))
                                store32(arg1 + 8, 0)
                                store64(arg1, 0)
                                store32(v4 + 20, 0)
                                store64(v4 + 12, 0)
                                store32(v4 + 12, load32(arg1 + 12))
                                store32(v4 + 16, load32(arg1 + 16))
                                store32(v4 + 20, load32(arg1 + 20))
                                store32(arg1 + 20, 0)
                                store64(arg1 + 12, 0)
                                # TODO: memory.copy []
                                v4 = (v4 + 128)
                                arg1 = (arg1 + 128)
                                if ((arg1 + 128) != arg0):
                                    continue
                                break
                            v5 = load32(v6 + 4)
                        store32(v6 + 8, v4)
                        arg0 = load32(9568064)
                        store32(9568064, v5)
                        store32(v6 + 4, arg0)
                        arg0 = load32(9568068)
                        store32(9568068, load32(v6 + 8))
                        store32(v6 + 8, arg0)
                        arg0 = load32(9568072)
                        store32(9568072, load32(v6 + 12))
                        store32(v6 + 12, arg0)
                        store32(v6, load32(v6 + 4))
                        arg1 = load32(v12 + 20)
                        arg0 = load32(v12 + 16)
                        if (load32(v12 + 20) != load32(v12 + 16)):
                            while True:  # $label35
                                v6 = (arg1 - 128)
                                store32(v12 + 20, (arg1 - 128))
                                arg2 = load32(v6 + 12)
                                if load32(v6 + 12):
                                    store32((arg1 - 112), arg2)
                                arg2 = load32(v6)
                                if load32(v6):
                                    store32((arg1 - 124), arg2)
                                arg1 = load32(v12 + 20)
                                if (load32(v12 + 20) != arg0):
                                    continue
                                break
                        arg0 = load32(v12 + 12)
                        if (load32(v12 + 12) == 0):
                            break
                        break
                    G.global0 = (v12 + 32)
                    break
                    break
                func42()
                raise RuntimeError('unreachable')
                break
            func68()
            raise RuntimeError('unreachable')
            break
        arg0 = load32(v3 + 220)
        if load32(v3 + 220):
            store32(v3 + 224, arg0)
        arg0 = load32(v3 + 208)
        if (load32(v3 + 208) == 0):
            break
        store32(v3 + 212, arg0)
        break
    G.global0 = (v3 + 336)
    return af(arg0)

# ------------------------------------------------------------
# $func620
# ------------------------------------------------------------
def func620(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store64(v1 + 8, 0)
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
# $ec
# Export: ec
# ------------------------------------------------------------
def ec():
    """Exported as ec."""
    if ((load8u(9147210) | load8u(9147152)) == 0):
        store8(9140312, 0)

# ------------------------------------------------------------
# $func622
# ------------------------------------------------------------
def func622(arg0, arg1):
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v3 = load32(9671128)
        v4 = (load32(9671128) + (arg0 * 132))
        if (load8u((load32(9671128) + (arg0 * 132)) + 125) == 3):
            break
        if arg1:
            if (load8u((v3 + (arg0 * 132)) + 127) != 6):
                break
        arg1 = (v3 + (arg0 * 132))
        store8((v3 + (arg0 * 132)) + 127, 0)
        while True:  # block $label1
            if (load8u(9142916) == 0):
                break
            v5 = load32(arg1 + 40)
            if (load32(arg1 + 40) == 0):
                break
            store32(v2 + 4, v5)
            store32(v2, 0)
            a_b()
            break
        func29(v4, 1)
        if (load32(arg1 + 92) == 0):
            break
        arg1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v3 + (arg0 * 132)) + 28)):
                break
        break
    G.global0 = (v2 + 16)

# ------------------------------------------------------------
# $func623
# ------------------------------------------------------------
def func623(arg0, arg1):
    arg0 = (load32(9671128) + (arg0 * 132))
    if (load8u((load32(9671128) + (arg0 * 132)) + 127) == 2):
        store8(arg0 + 127, arg1)

# ------------------------------------------------------------
# $func624
# ------------------------------------------------------------
def func624(arg0, arg1):
    while True:  # block $label0
        v3 = load32(9561692)
        arg1 = (load32(9561692) + (arg0 * 286704))
        if load32((((load32(9561692) + (arg0 * 286704)) + (load32(38452) << 2)) + 281808)):
            break
        v2 = (load32(arg1 + 283868) + 1)
        store32(arg1 + 283868, (load32(arg1 + 283868) + 1))
        while True:  # block $label1
            if (u(v2) >= u((load32((arg1 + 284372)) + (load32((arg1 + 284380)) * load32(arg1 + 283864))))):
                break
            arg1 = (v3 + (arg0 * 286704))
            if (u(v2) >= u(load32(((v3 + (arg0 * 286704)) + 284376)))):
                break
            break
        arg0 = 0
        arg1 = load32(9213808)
        if (load32(9213808) == 0):
            break
        v2 = load32(38464)
        v3 = load32(9671128)
        while True:  # $label2
            if (load8u((v3 + (load32(((arg0 << 2) + 9173808)) * 132)) + 122) != v2):
                arg0 = (arg0 + 1)
                if (arg1 != (arg0 + 1)):
                    continue
                break
            break
        break

# ------------------------------------------------------------
# $func625
# ------------------------------------------------------------
def func625(arg0, arg1):
    while True:  # block $label0
        if (arg0 == arg1):
            break
        v2 = load32(9671128)
        v3 = (load32(9671128) + (arg0 * 132))
        v7 = (v2 + (arg1 * 132))
        v8 = load8u((v2 + (arg1 * 132)) + 122)
        if func297(v7, arg0):
            store8(v3 + 129, 0)
            store32(v3 + 36, arg1)
            v4 = load32(v3 + 44)
            if load32(v3 + 44):
                store32((load32(9215884) + (v4 << 4)), 0)
            store32(v3 + 44, 0)
            v4 = (v2 + (arg0 * 132))
            v5 = load32((v2 + (arg0 * 132)) + 20)
            if load32((v2 + (arg0 * 132)) + 20):
                store32(v5 + 8, 0)
            v4 = ((load8u(v4 + 122) * 404) + 9568096)
            if load32(((load8u(v4 + 122) * 404) + 9568096) + 216):
                arg0 = (v2 + (arg0 * 132))
                v9 = load16u((v2 + (arg0 * 132)) + 114)
                v10 = load16u(arg0 + 112)
                v11 = load32(9142840)
                v5 = 0
                while True:  # $label2
                    v5 = (v5 + 1)
                    v12 = ((v5 + 1) + v10)
                    arg0 = 0
                    while True:  # $label1
                        arg0 = (arg0 + 1)
                        v6 = (load32(9142440) + 2)
                        store32((v11 + ((v12 + ((((arg0 + 1) + v9) + ((load32(9142440) + 2) * load32(v4 + 208))) * v6)) << 2)), load32(v4 + 212))
                        v6 = load32(v4 + 216)
                        if (u(arg0) < u(load32(v4 + 216))):
                            continue
                        break
                    if (u(v5) < u(v6)):
                        continue
                    break
            func138(v3)
            while True:  # block $label3
                arg0 = (v2 + (arg1 * 132))
                if (load32((v2 + (arg1 * 132)) + 92) == 0):
                    break
                if load32(9140316):
                    if (load32(9140320) != load32((v2 + (arg1 * 132)) + 28)):
                        break
                break
            while True:  # block $label4
                if (load8u(9147141) == 0):
                    break
                if (load32(arg0 + 92) == 0):
                    break
                if (load8u(9147152) == 0):
                    arg0 = (v2 + (arg1 * 132))
                    if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u((v2 + (arg1 * 132)) + 110))))) == 0):
                        break
                    if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                        break
                    if (load8u((v2 + (arg1 * 132)) + 127) == 6):
                        break
                arg0 = load32((v2 + (arg1 * 132)) + 16)
                if (load32((v2 + (arg1 * 132)) + 16) == 0):
                    break
                if (load32(arg0 + 8) == 0):
                    break
                Ya(1)
                break
            v3 = (v2 + (arg1 * 132))
            if (load32((v2 + (arg1 * 132)) + 88) == 0):
                break
            if (load32(((v8 * 404) + 9568096) + 264) != 4):
                break
            arg0 = (v2 + (arg1 * 132))
            if (load8u((v2 + (arg1 * 132)) + 129) != 7):
                store8(arg0 + 129, 7)
            v4 = load32(arg0 + 16)
            if load32(arg0 + 16):
            else:
            v5 = (v2 + (arg1 * 132))
            if (u(0) < u(load32((v2 + (arg1 * 132)) + 80))):
                break
            arg1 = load32(v3 + 88)
            if (load32(v3 + 88) == 0):
                break
            v2 = load32(9142440)
            store32(v5 + 80, 0)
            store32(v3 + 88, 0)
            store8(arg0 + 129, 0)
            # TODO: i32.div_u []
            arg0 = v2
            return load32(v4 + 8)
        func29(v3, 1)
        break
    return func28(1, 1)

# ------------------------------------------------------------
# $func626
# ------------------------------------------------------------
def func626(arg0, arg1, arg2, arg3, arg4):
    arg2 = 1
    while True:  # block $label0
        arg3 = load32(9671128)
        v5 = load8u((load32(9671128) + (arg0 * 132)) + 122)
        arg1 = load32(arg1)
        v6 = (arg3 + (load32(arg1) * 132))
        arg4 = load8u((arg3 + (load32(arg1) * 132)) + 122)
        if (load8u((load32(9671128) + (arg0 * 132)) + 122) == load8u((arg3 + (load32(arg1) * 132)) + 122)):
            break
        if (load32(((arg4 * 404) + 9568096) + 140) == 2):
            if (u(load32(((v5 * 404) + 9568096) + 216)) > u(1)):
                break
        if (load32((arg3 + (arg0 * 132)) + 36) == arg1):
            break
        arg2 = 0
        if (load32((load32(9561692) + (load16u((arg3 + (arg1 * 132)) + 110) * 286704)) + 286684) == 0):
            break
        if (load32(((arg4 * 404) + 9568096) + 264) != 4):
            break
        arg1 = (arg3 + (arg1 * 132))
        if load8u((arg3 + (arg1 * 132)) + 125):
            break
        if (load8u(arg1 + 129) == 7):
            break
        break
    return arg2

# ------------------------------------------------------------
# $func627
# ------------------------------------------------------------
def func627(arg0):
    v2 = load32(9671128)
    v3 = load32(arg0 + 32)
    v1 = (load32(9671128) + (load32(arg0 + 32) * 132))
    while True:  # block $label0
        v5 = load32(9561692)
        if (load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 286684) == 0):
            v6 = load32(v1 + 16)
            if (load32(v1 + 16) == 0):
                break
            v2 = (v2 + (v3 * 132))
            v3 = load32(((load8u((v2 + (v3 * 132)) + 122) * 404) + 9568096) + 136)
            # TODO: i32.div_u []
            if (u((load32(((load8u((v2 + (v3 * 132)) + 122) * 404) + 9568096) + 136) * 150)) < u((100 if (load32((((v5 + (load16u(v2 + 110) * 286704)) + (load32(39216) << 2)) + 281808)) == 1) else v3))):
                break
            while True:  # block $label3
                v9 = load16u(v1 + 110)
                v10 = (((load32(9561692) + (load16u(v1 + 110) * 286704)) + (load32(39216) << 2)) + 281808)
                v3 = load32(9142440)
                v5 = (load32(9142440) + 2)
                v11 = load8u(v1 + 122)
                v6 = ((load8u(v1 + 122) * 404) + 9568096)
                v7 = load32(9671128)
                v12 = load32(9142840)
                v13 = load16u(v1 + 114)
                v14 = load16u(v1 + 112)
                v1 = 0
                while True:  # $label4
                    while True:  # block $label1
                        v2 = v1
                        v4 = (v1 << 2)
                        v1 = (load32((((v1 << 2) | 4) + 8611904)) + v13)
                        if (u(v3) <= u((load32((((v1 << 2) | 4) + 8611904)) + v13))):
                            break
                        v4 = (load32((v4 + 8611904)) + v14)
                        if (u(v3) <= u((load32((v4 + 8611904)) + v14))):
                            break
                        if ((v1 | v4) < 0):
                            break
                        v4 = load32((((v4 + (((v1 + (load32(v6 + 208) * v5)) + 1) * v5)) << 2) + v12) + 4)
                        v1 = (v7 + (load32((((v4 + (((v1 + (load32(v6 + 208) * v5)) + 1) * v5)) << 2) + v12) + 4) * 132))
                        if (load8u((v7 + (load32((((v4 + (((v1 + (load32(v6 + 208) * v5)) + 1) * v5)) << 2) + v12) + 4) * 132)) + 122) != v11):
                            break
                        if (load16u(v1 + 110) != v9):
                            break
                        while True:  # block $label2
                            # br_table[(load8u(v1 + 125) - 4)]
                            break
                            break
                        v1 = load32(v1 + 16)
                        if load32(v1 + 16):
                            v15 = load32(v6 + 136)
                            # TODO: i32.div_u []
                            if (u((load32(v6 + 136) * 150)) >= u((100 if (load32(v10) == 1) else v15))):
                                break
                        break
                        break
                    v1 = (v2 + 2)
                    if (u(v2) < u(1918)):
                        continue
                    break
                break
            v1 = 0
            if (0 == 0):
                break
            store32(arg0 + 32, v1)
            return 0
        if (load32(((load8u(v1 + 122) * 404) + 9568096) + 264) != 4):
            return 0
        v8 = 1
        v2 = (v2 + (v3 * 132))
        if (load8u((v2 + (v3 * 132)) + 123) == 38):
            break
        if load8u(v2 + 125):
            return 0
        v8 = 0
        if (load8u(v2 + 129) == 7):
            break
        break
    return v8

# ------------------------------------------------------------
# $func628
# ------------------------------------------------------------
def func628(arg0):
    atomic_store(arg0, 1)
    func248(0, arg0)
    # TODO: i32.atomic.rmw.cmpxchg []

# ------------------------------------------------------------
# $func629
# ------------------------------------------------------------
def func629(arg0, arg1, arg2):
    v3 = load32(arg0)
    v4 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    v4 = func26((v3 + 4))
    store32(9687208, v3)
    store32(9687204, v4)
    if arg2:
        # TODO: memory.copy []
    arg1 = 0
    arg2 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    arg0 = load32(arg0 + 8)
    store32(9147312, load32(arg0 + 8))
    store32(9147324, (arg0 ^ -1))
    store32(9147320, (arg0 ^ -1515870811))
    store32(9147316, (arg0 ^ 1515870810))
    while True:  # block $label0
        arg0 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        arg2 = load32(9142384)
        v3 = load32(9561692)
        arg1 = 1
        while True:  # $label1
            if (load32((v3 + (arg1 * 286704)) + 284616) == arg2):
                break
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != arg0):
                continue
            break
        arg1 = 0
        break
    store8(9147210, 1)
    store32(9142872, arg1)
    if (load8u(9147208) == 0):
        arg0 = load32(9142892)
    if (u(arg0) >= u(2)):
        v3 = load32(9561692)
        arg1 = 1
        while True:  # $label3
            while True:  # block $label2
                arg2 = (v3 + (arg1 * 286704))
                if (load32((v3 + (arg1 * 286704)) + 284616) == 0):
                    break
                if (load32(arg2 + 286684) == 0):
                    break
                store32((arg2 + 286684), 0)
                arg0 = load32(9142892)
                break
            arg1 = (arg1 + 1)
            if (u((arg1 + 1)) < u(arg0)):
                continue
            break

# ------------------------------------------------------------
# $func632
# ------------------------------------------------------------
def func632(arg0, arg1):
    while True:  # block $label0
        arg1 = load32(9671128)
        v2 = (load32(9671128) + (arg0 * 132))
        v3 = load8u((load32(9671128) + (arg0 * 132)) + 125)
        if (load8u((load32(9671128) + (arg0 * 132)) + 125) == 3):
            break
        if load16u(v2 + 110):
            break
        v4 = (arg1 + (arg0 * 132))
        while True:  # block $label1
            if (u(v3) > u(1)):
                break
            if load8u(v4 + 123):
                break
            arg0 = (arg1 + (arg0 * 132))
            v5 = load16u((arg1 + (arg0 * 132)) + 112)
            v6 = load16u(arg0 + 114)
            arg0 = load32(9147324)
            store32(9147324, load32(9147316))
            arg1 = load32(9147320)
            v3 = load32(9147312)
            store32(9147320, load32(9147312))
            arg0 = (arg0 ^ (arg0 << 11))
            arg0 = ((v3 ^ (((v3 & 0xFFFFFFFF) >> 19) ^ (((arg0 ^ (arg0 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg0)
            store32(9147316, ((v3 ^ (((v3 & 0xFFFFFFFF) >> 19) ^ (((arg0 ^ (arg0 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg0))
            arg1 = (arg1 ^ (arg1 << 11))
            arg1 = ((((((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg0 & 0xFFFFFFFF) >> 19)) ^ arg1) ^ arg0)
            store32(9147312, ((((((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg0 & 0xFFFFFFFF) >> 19)) ^ arg1) ^ arg0))
            v2 = ((v5 + (arg0 % 21)) - 10)
            arg0 = load32(9142440)
            v3 = (load32(9142440) - 1)
            v2 = (((v5 + (arg0 % 21)) - 10) if (u(arg0) > u(v2)) else (load32(9142440) - 1))
            arg1 = ((v6 + (arg1 % 21)) - 10)
            arg0 = (((v6 + (arg1 % 21)) - 10) if (u(arg0) > u(arg1)) else v3)
            break
        v7 = load64(9147316)
        arg0 = load32(9147312)
        store32(9147316, load32(9147312))
        arg1 = load32(9147324)
        store64(9147320, v7)
        arg1 = (arg1 ^ (arg1 << 11))
        arg0 = ((arg0 ^ (((arg0 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1)
        store32(9147312, ((arg0 ^ (((arg0 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1))
        break

# ------------------------------------------------------------
# $func634
# ------------------------------------------------------------
def func634(arg0, arg1):
    arg1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v2 = (load32(9671128) + (arg0 * 132))
    v5 = load16u(v2 + 116)
    v6 = load16u(v2 + 118)
    while True:  # block $label0
        v2 = load32(9142440)
        if (u(load32(9142440)) <= u(v6)):
            break
        if (u(v2) <= u(v5)):
            break
        while True:  # block $label1
            v4 = ((v5 << 5) - load32(9142952))
            v4 = ((v6 << 5) - load32(9142956))
            if ((((((v5 << 5) - load32(9142952)) * v4) + (((v6 << 5) - load32(9142956)) * v4)) - 1) > 9000000):
                break
            v4 = load32(39940)
            while True:  # block $label2
                v3 = load32(load32(9142424) + 48)
                if (load32(load32(9142424) + 48) == 0):
                    break
                if load8u(9147152):
                    break
                v2 = load16u((load32(9147376) + (((v2 * v6) + v5) << 1)))
                if (v3 == 2):
                    if (u(v2) > u(1)):
                        break
                    break
                if (v2 == 0):
                    break
                break
            store32(arg1 + 56, v6)
            store32(arg1 + 52, v5)
            store32(arg1 + 48, v4)
            a_b()
            break
        v9 = load32(9671136)
        if (u(load32(9671136)) < u(4)):
            break
        v4 = 3
        while True:  # $label7
            while True:  # block $label3
                v7 = (v4 * 132)
                v2 = ((v4 * 132) + load32(9671128))
                if (load8u(((v4 * 132) + load32(9671128)) + 125) != 3):
                    break
                if (u(((load32(9142848) - load32(v2 + 68)) * 25)) > u(6999)):
                    break
                v3 = (load16u(v2 + 112) - v5)
                v3 = (load16u(v2 + 114) - v6)
                v3 = load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284348))
                if (((((load16u(v2 + 112) - v5) * v3) + ((load16u(v2 + 114) - v6) * v3)) - 1) > (load32(((load32(9561692) + (load16u(v2 + 110) * 286704)) + 284348)) * v3)):
                    break
                if (load32(((load8u(v2 + 122) * 404) + 9568096) + 348) == 0):
                    break
                while True:  # block $label4
                    v3 = load32(v2 + 40)
                    if (load32(v2 + 40) == 0):
                        break
                    if load8u(9142916):
                        store32(arg1 + 32, v3)
                        a_b()
                        break
                    store32(arg1 + 24, v3)
                    store64(arg1 + 16, -4602115869219225600)
                    store64(arg1 + 8, 0)
                    store64(arg1, 0)
                    a_b()
                    break
                if (func34(load32(38660), load16u((load32(9671128) + (arg0 * 132)) + 110), load16u(v2 + 112), load16u(v2 + 114), 0, 1) == 0):
                    break
                v3 = (load32(9671128) + v7)
                v2 = load16u((load32(9671128) + v7) + 114)
                v3 = load16u(v3 + 112)
                while True:  # block $label6
                    while True:  # block $label5
                        v10 = load32(load32(9142424) + 48)
                        if load32(load32(9142424) + 48):
                            if (load8u(9147152) == 0):
                                break
                        v7 = load32(9142440)
                        break
                        break
                    v7 = load32(9142440)
                    v8 = load16u((load32(9147376) + (((load32(9142440) * v2) + v3) << 1)))
                    if (v10 == 2):
                        if (u(v8) > u(1)):
                            break
                        break
                    if (v8 == 0):
                        break
                    break
                # TODO: f32.convert_i32_u []
                # TODO: f32.convert_i32_u []
                # TODO: f32.convert_i32_u []
                func80(v3, v2, load32(9142536), 32.0, (v7 * 96))
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != v9):
                continue
            break
        break
    G.global0 = (arg1 - -64)

# ------------------------------------------------------------
# $func635
# ------------------------------------------------------------
def func635(arg0, arg1):
    while True:  # block $label0
        v5 = load32(9671128)
        v7 = (load32(9671128) + (arg0 * 132))
        if load8u((load32(9671128) + (arg0 * 132)) + 128):
            break
        arg1 = load8u(v7 + 125)
        if ((u(load8u(v7 + 125)) <= u(14)) if ((1 << arg1) & 16408) else 0):
            break
        arg1 = -1
        v10 = func106(v7, -1, -1, -1)
        if (func106(v7, -1, -1, -1) == 0):
            break
        while True:  # block $label1
            v14 = (v5 + (arg0 * 132))
            if (load8u((v5 + (arg0 * 132)) + 129) == 6):
                break
            arg1 = 5
            if (load32(((load8u(v14 + 122) * 404) + 9568096) + 264) == 1):
                break
            v2 = (load32(9671128) + (v10 * 132))
            v19 = ((load32(9671128) + (v10 * 132)) - -64)
            v11 = (v5 + (arg0 * 132))
            v5 = load16u((v5 + (arg0 * 132)) + 114)
            v20 = (load16u((v5 + (arg0 * 132)) + 114) + 9)
            arg1 = load16u(v11 + 112)
            v21 = (load16u(v11 + 112) + 9)
            v5 = (v5 - 5)
            v6 = (arg1 - 5)
            while True:  # $label7
                v15 = (v6 + 1)
                arg1 = v5
                while True:  # $label6
                    while True:  # block $label2
                        v4 = (v6 - load16u(v11 + 112))
                        v4 = arg1
                        arg1 = (arg1 - load16u(v11 + 114))
                        if (((((v6 - load16u(v11 + 112)) * v4) + ((arg1 - load16u(v11 + 114)) * arg1)) - 1) > 25):
                            break
                        v12 = load32(9142440)
                        if (u(load32(9142440)) <= u(v4)):
                            break
                        if ((v4 | v6) < 0):
                            break
                        if (u(v6) >= u(v12)):
                            break
                        v22 = (v4 + 1)
                        arg1 = 0
                        v16 = load32(9142840)
                        while True:  # $label5
                            while True:  # block $label3
                                v3 = (v12 + 2)
                                v3 = load32((v16 + ((v15 + ((v22 + ((v12 + 2) * arg1)) * v3)) << 2)))
                                if (u(load32((v16 + ((v15 + ((v22 + ((v12 + 2) * arg1)) * v3)) << 2)))) < u(3)):
                                    break
                                if (arg0 == v3):
                                    break
                                v8 = load8u(v2 + 122)
                                if (load8u(v2 + 122) == load32(38500)):
                                    break
                                v13 = load16u(v2 + 110)
                                v9 = (load32(9671128) + (v3 * 132))
                                v17 = (load32(9142892) * load16u((load32(9671128) + (v3 * 132)) + 110))
                                v18 = load32(9143004)
                                while True:  # block $label4
                                    v3 = load16u(v2 + 120)
                                    if load16u(v2 + 120):
                                    else:
                                    if (load8u(((v3 if load8u((v18 + (v13 + v17))) else v13) + (v13 + v17))) == 0):
                                        if (load8u(v2 + 127) != 6):
                                            break
                                        if (load8u(v2 + 128) == 0):
                                            break
                                        break
                                    if load8u(v2 + 128):
                                        break
                                    break
                                if (load8u(v2 + 125) == 10):
                                    break
                                if (load8u(v2 + 126) == 2):
                                    break
                                if (load32(v19) == -1):
                                    break
                                v3 = ((v8 * 404) + 9568096)
                                if (load32(((v8 * 404) + 9568096) + 264) == 2):
                                    break
                                if (load32(v3 + 188) != 55):
                                    break
                                if (load32(38560) == v8):
                                    break
                                if (load32(38620) == v8):
                                    break
                                if (load32(38564) == v8):
                                    break
                                if (load32((load32(9215884) + (load32(v9 + 44) << 4)) + 4) != 22):
                                    break
                                if (load8u(v9 + 129) == 6):
                                    break
                                if load8u(v9 + 128):
                                    break
                                v16 = load32(9142840)
                                v12 = load32(9142440)
                                break
                            arg1 = (arg1 + 1)
                            if ((arg1 + 1) != 3):
                                continue
                            break
                        break
                    arg1 = (v4 + 1)
                    if (v4 != v20):
                        continue
                    break
                arg1 = (v6 == v21)
                v6 = v15
                if (arg1 == 0):
                    continue
                break
            arg1 = (-1 if (load8u(v14 + 129) == 6) else 5)
            break
        return
        break
    store32((load32(9215884) + (load32(v7 + 44) << 4)), (load32(9142848) + (80 if load8u(9216060) else 40)))

# ------------------------------------------------------------
# $ba
# Export: ba
# ------------------------------------------------------------
def ba():
    """Exported as ba."""
    return load32((9142892 if load8u(9147212) else 41092))

# ------------------------------------------------------------
# $ub
# Export: ub
# ------------------------------------------------------------
def ub():
    """Exported as ub."""
    return load32(9671176)

# ------------------------------------------------------------
# $func638
# ------------------------------------------------------------
def func638(arg0, arg1, param2):
    while True:  # block $label0
        v4 = load32(9671128)
        arg1 = (load32(9671128) + (arg0 * 132))
        v3 = load32((load32(9671128) + (arg0 * 132)) + 20)
        if (load32((load32(9671128) + (arg0 * 132)) + 20) == 0):
            break
        if (u(load32(v3 + 8)) < u(5)):
            break
        v2 = load32(load32(v3) + 16)
        break
    while True:  # block $label1
        if (load8u(arg1 + 125) == 1):
            v2 = (v4 + (arg0 * 132))
            v3 = load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
                # call_indirect[v3]
            if (load8u(arg1 + 125) == 3):
                break
            v3 = load32(v2 + 44)
            if load32(v2 + 44):
                v5 = load32(9142848)
                arg1 = load32(9215884)
                store32((load32(9215884) + (v3 << 4)) + 4, 69)
                store32((arg1 + (load32(v2 + 44) << 4)) + 8, load32((v4 + (arg0 * 132)) + 28))
                store32((arg1 + (load32(v2 + 44) << 4)) + 12, arg0)
                store32((arg1 + (load32(v2 + 44) << 4)), (v5 + 40))
                return
            store32(v2 + 44, ((Ua(1000, 69, load32((v4 + (arg0 * 132)) + 28), arg0) & 0xFFFFFFFF) >> 2))
            return
        v3 = (v4 + (v2 * 132))
        v5 = func106(arg1, -1, load16u((v4 + (v2 * 132)) + 112), load16u(v3 + 114))
        if func106(arg1, -1, load16u((v4 + (v2 * 132)) + 112), load16u(v3 + 114)):
        v5 = (v4 + (arg0 * 132))
        v6 = (load16u((v4 + (arg0 * 132)) + 112) - load16u(v3 + 112))
        v3 = (load16u(v5 + 114) - load16u(v3 + 114))
        if (((((load16u((v4 + (arg0 * 132)) + 112) - load16u(v3 + 112)) * v6) + ((load16u(v5 + 114) - load16u(v3 + 114)) * v3)) - 1) >= 26):
            return
        if (load8u((v4 + (v2 * 132)) + 125) == 3):
            arg0 = load32(arg1 + 20)
            v4 = func236(arg1, (v4 + (v2 * 132)))
            if func236(arg1, (v4 + (v2 * 132))):
                while True:  # block $label2
                    if (arg0 == 0):
                        break
                    if (u(load32(arg0 + 8)) < u(5)):
                        break
                    store32(load32(arg0) + 16, v4)
                    break
                return
            store32(arg0 + 8, 0)
            func29(arg1, 1)
            return
        store32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
        break

# ------------------------------------------------------------
# $func639
# ------------------------------------------------------------
def func639(arg0):
    while True:  # block $label0
        v1 = (load32(9671128) + (load32(arg0 + 32) * 132))
        if (load8u((load32(9671128) + (load32(arg0 + 32) * 132)) + 125) != 3):
            break
        v1 = func236(arg0, v1)
        if func236(arg0, v1):
            store32(arg0 + 32, v1)
            arg0 = load32(arg0 + 20)
            if (load32(arg0 + 20) == 0):
                break
            if (u(load32(arg0 + 8)) < u(5)):
                break
            store32(load32(arg0) + 16, v1)
            return 0
        v2 = 1
        arg0 = load32(arg0 + 20)
        if (load32(arg0 + 20) == 0):
            break
        store32(arg0 + 8, 0)
        break
    return v2

# ------------------------------------------------------------
# $func641
# ------------------------------------------------------------
def func641(arg0):
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        if load8u(9163793):
            break
        v4 = (load32(9671128) + (load32(9173808) * 132))
        arg0 = load16u((load32(9671128) + (load32(9173808) * 132)) + 112)
        v3 = (load16u((load32(9671128) + (load32(9173808) * 132)) + 112) - 2)
        v5 = ((load8u(v4 + 122) * 404) + 9568096)
        v7 = ((arg0 + load32(((load8u(v4 + 122) * 404) + 9568096) + 216)) + 2)
        if ((load16u((load32(9671128) + (load32(9173808) * 132)) + 112) - 2) >= ((arg0 + load32(((load8u(v4 + 122) * 404) + 9568096) + 216)) + 2)):
            break
        v6 = ((load32(v5 + 220) + load16u(v4 + 114)) + 2)
        while True:  # $label6
            v5 = (v3 + 1)
            arg0 = (load16u(v4 + 114) - 2)
            if (v6 > (load16u(v4 + 114) - 2)):
                while True:  # $label5
                    while True:  # block $label3
                        while True:  # block $label2
                            while True:  # block $label1
                                v2 = load32(9142440)
                                if (u(load32(9142440)) <= u(arg0)):
                                    break
                                if ((arg0 | v3) < 0):
                                    break
                                if (u(v2) > u(v3)):
                                    break
                                break
                            break
                            break
                        while True:  # block $label4
                            v8 = (arg0 + 1)
                            v2 = (v2 + 2)
                            if load32((load32(9142840) + ((v5 + (((arg0 + 1) + (v2 + 2)) * v2)) << 2))):
                                break
                            store32(v1 + 8, arg0)
                            store32(v1 + 4, v3)
                            store32(v1, load32(38636))
                            store32(v1 + 12, load16u(v4 + 110))
                            store64(v1 + 32, 4294967297)
                            store64(v1 + 24, 4294967297)
                            store64(v1 + 16, 4294967297)
                            store32(v1 + 40, 0)
                            arg0 = load32(9213808)
                            if load8u(9147210):
                                func41(4, 9173808, arg0, v1, 11)
                                break
                            v9 = (arg0 << 2)
                            v2 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                            if arg0:
                                # TODO: memory.copy []
                            # call_indirect[load32(9213856)]
                            break
                        break
                    arg0 = v8
                    if (indirect_call(load32(9213856)) != v8):
                        continue
                    break
            v3 = v5
            if (v5 != v7):
                continue
            break
        break
    G.global0 = (v1 + 48)
    return arg0

# ------------------------------------------------------------
# $func645
# ------------------------------------------------------------
def func645(arg0, arg1, arg2):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if load8u(9142388):
        store32(arg0, load32(59164))
    G.global0 = (arg0 + 16)

# ------------------------------------------------------------
# $ce
# Export: ce
# ------------------------------------------------------------
def ce():
    """Exported as ce."""
    store8(9147213, 1)
    store8(9147152, 0)
    store8(9681884, 0)
    v0 = load32(9142440)
    v0 = (load32(9142440) * v0)
    v0 = (-1 if (v0 < 0) else ((load32(9142440) * v0) << 1))
    v1 = func26((-1 if (v0 < 0) else ((load32(9142440) * v0) << 1)))
    # TODO: memory.fill []
    store32(9142436, v1)
    v0 = load32(9142872)
    if (((load32(9142872) != 2147483647) if v0 else 0) == 0):
        store32(9142872, 1)
    la()
    if (load8u(9147152) == 0):
        func52((207 if load8u(9143020) else 0), 0)
        a_b()
    v1 = load32(9671136)
    if (u(load32(9671136)) >= u(4)):
        v2 = load32(9671128)
        v0 = 3
        while True:  # $label1
            while True:  # block $label0
                v3 = (v2 + (v0 * 132))
                if (load8u((v2 + (v0 * 132)) + 125) == 3):
                    break
                if (load32(v3 + 28) == 0):
                    break
                if (load32(v3 + 32) != -1):
                    break
                store32(v3 + 32, 0)
                func240(v3, 500, 0)
                v1 = load32(9671136)
                v2 = load32(9671128)
                break
            v0 = (v0 + 1)
            if (u((v0 + 1)) < u(v1)):
                continue
            break
    while True:  # block $label2
        v0 = load32(9142424)
        if (load32(load32(9142424) + 48) == 0):
            break
        while True:  # block $label3
            if load32(9147376):
            else:
                v2 = load32(9142440)
                v2 = ((load32(9142440) * v2) + 2)
                v2 = (-1 if (v2 < 0) else (((load32(9142440) * v2) + 2) << 1))
                v3 = func26((-1 if (v2 < 0) else (((load32(9142440) * v2) + 2) << 1)))
                # TODO: memory.fill []
                store32(9147376, v3)
            if ((load32(v0 + 48) != 0) == 0):
                break
            if load8u(9147152):
                break
            if (u(v1) < u(4)):
                break
            v2 = load32(9671128)
            v0 = 3
            while True:  # $label5
                while True:  # block $label4
                    v3 = (v2 + (v0 * 132))
                    if (load8u((v2 + (v0 * 132)) + 125) == 3):
                        break
                    if (load32(v3 + 28) == 0):
                        break
                    if load32(v3 + 36):
                        break
                    v1 = load32(9671136)
                    v2 = load32(9671128)
                    break
                v0 = (v0 + 1)
                if (u((v0 + 1)) < u(v1)):
                    continue
                break
            break
        if (u(v1) < u(4)):
            break
        v0 = 3
        while True:  # $label7
            while True:  # block $label6
                v1 = (load32(9671128) + (v0 * 132))
                if (load8u((load32(9671128) + (v0 * 132)) + 125) == 3):
                    break
                if (load32(v1 + 28) == 0):
                    break
                if func292(v1):
                    break
                func158(v1)
                break
            v0 = (v0 + 1)
            if (u((v0 + 1)) < u(load32(9671136))):
                continue
            break
        break
    return 0

# ------------------------------------------------------------
# $func648
# ------------------------------------------------------------
def func648(arg0, arg1, arg2):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        arg0 = (load32(9561692) + (load32(arg0) * 286704))
        arg2 = load32((load32(9561692) + (load32(arg0) * 286704)) + 284616)
        if (load32((load32(9561692) + (load32(arg0) * 286704)) + 284616) == 0):
            La(load32(arg0 + 283908), 1)
            break
        store32(arg1, arg2)
        break
    G.global0 = (arg1 + 16)

# ------------------------------------------------------------
# $func649
# ------------------------------------------------------------
def func649(arg0, arg1, arg2):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(arg0 + 12, 0)
    func71(31, (arg0 + 12), 1, 0, 0, 1)
    G.global0 = (arg0 + 16)

# ------------------------------------------------------------
# $func650
# ------------------------------------------------------------
def func650(arg0, arg1, arg2):
    arg2 = 0
    v3 = load32(9561692)
    while True:  # block $label0
        v4 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v5 = load32(59164)
        arg1 = 1
        while True:  # $label1
            if (v5 == load32((v3 + (arg1 * 286704)) + 284616)):
                arg2 = arg1
                break
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != v4):
                continue
            break
        break
    store32((v3 + (arg2 * 286704)) + 286692, load32(arg0))

# ------------------------------------------------------------
# $ea
# Export: ea
# ------------------------------------------------------------
def ea(arg0):
    """Exported as ea."""
    while True:  # block $label0
        v2 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v3 = load32(9561692)
        v1 = 1
        while True:  # $label1
            if (load32((v3 + (v1 * 286704)) + 284616) == arg0):
                break
            v1 = (v1 + 1)
            if ((v1 + 1) != v2):
                continue
            break
        v1 = 0
        break
    return v1

# ------------------------------------------------------------
# $ja
# Export: ja
# ------------------------------------------------------------
def ja(arg0, arg1, arg2, arg3):
    """Exported as ja."""
    v6 = load32(9142892)
    if (u(load32(9142892)) >= u(2)):
        v5 = load32(9561692)
        v4 = 1
        while True:  # block $label0
            while True:  # $label1
                if (load32((v5 + (v4 * 286704)) + 284616) == arg0):
                    break
                v4 = (v4 + 1)
                if ((v4 + 1) != v6):
                    continue
                break
            return 0
            break
        arg0 = (v5 + (v4 * 286704))
        store8((v5 + (v4 * 286704)) + 283972, arg1)
        store8((arg0 + 283974), arg3)
        store8((arg0 + 283973), arg2)
    return v4

# ------------------------------------------------------------
# $ia
# Export: ia
# ------------------------------------------------------------
def ia(arg0, arg1):
    """Exported as ia."""
    v4 = load32(9142892)
    if (u(load32(9142892)) >= u(2)):
        v3 = load32(9561692)
        v2 = 1
        while True:  # block $label0
            while True:  # $label1
                if (load32((v3 + (v2 * 286704)) + 284616) == arg0):
                    break
                v2 = (v2 + 1)
                if ((v2 + 1) != v4):
                    continue
                break
            return 0
            break
        store32((v3 + (v2 * 286704)) + 283960, arg1)
    return v2

# ------------------------------------------------------------
# $func654
# ------------------------------------------------------------
def func654(arg0, arg1):
    v5 = load32(9671128)
    v8 = (load32(9671128) + (arg0 * 132))
    v9 = (v5 + (arg1 * 132))
    v2 = load8u((v5 + (arg1 * 132)) + 122)
    while True:  # block $label0
        if (load8u(9216060) == 0):
            break
        if (load32(39064) != v2):
            break
        v12 = (v5 + (arg1 * 132))
        while True:  # block $label1
            v2 = load32(9561692)
            v13 = (v5 + (arg0 * 132))
            v6 = load16u((v5 + (arg0 * 132)) + 110)
            arg1 = (load32(9561692) + (load16u((v5 + (arg0 * 132)) + 110) * 286704))
            v3 = load32((load32(9561692) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + 283848)
            if (load32((load32(9561692) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + 283848) == 2147483647):
                break
            store32((arg1 + 283848), (load32(v12 + 52) + v3))
            v3 = 1
            store8(arg1 + 286701, 1)
            v4 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v10 = (v4 - 1)
            v14 = ((v4 - 1) & 1)
            v6 = (load32((v2 + (v6 * 286704)) + 283908) * v4)
            v2 = 0
            v7 = load32(9561692)
            v11 = load32(9143016)
            if (v4 != 2):
                v4 = (v10 & -2)
                while True:  # $label2
                    if load8u((v11 + (v3 + v6))):
                        store8((v7 + (v3 * 286704)) + 286701, 1)
                    v10 = (v3 + 1)
                    if load8u((v11 + ((v3 + 1) + v6))):
                        store8((v7 + (v10 * 286704)) + 286701, 1)
                    v3 = (v3 + 2)
                    v2 = (v2 + 2)
                    if ((v2 + 2) != v4):
                        continue
                    break
            if (v14 == 0):
                break
            if (load8u((v11 + (v3 + v6))) == 0):
                break
            store8((v7 + (v3 * 286704)) + 286701, 1)
            break
        arg1 = (arg1 + 281640)
        store32((arg1 + 281640), (load32(arg1) + load32(v12 + 52)))
        while True:  # block $label3
            if load8u(9142917):
                break
            if (load32(9142872) != load16u(v13 + 110)):
                break
            a_b()
            break
        arg0 = (v5 + (arg0 * 132))
        store8((v5 + (arg0 * 132)) + 125, 0)
        v6 = load32(9142440)
        v12 = (load32(9142440) + 2)
        v13 = load8u(v9 + 122)
        v10 = ((load32(9142440) + 2) * load32(((load8u(v9 + 122) * 404) + 9568096) + 208))
        v7 = load16u(arg0 + 112)
        v14 = (load16u(arg0 + 112) + 12)
        v11 = load16u(arg0 + 114)
        v16 = (load16u(arg0 + 114) + 12)
        v9 = (v11 - 12)
        v2 = (v7 - 12)
        v17 = load32(9671128)
        v18 = load32(9142840)
        v4 = 2147483647
        arg0 = 0
        while True:  # $label6
            v5 = (v2 + 1)
            if (u(v2) < u(v6)):
                arg1 = (v7 - v2)
                v19 = ((v7 - v2) * arg1)
                arg1 = v9
                while True:  # $label5
                    while True:  # block $label4
                        v3 = arg1
                        if (u(v6) <= u(arg1)):
                            break
                        if ((v2 | v3) < 0):
                            break
                        arg1 = (v11 - v3)
                        v15 = (((v11 - v3) * arg1) + v19)
                        if ((((v11 - v3) * arg1) + v19) >= v4):
                            break
                        arg1 = load32((v18 + (((((v3 + v10) + 1) * v12) + v5) << 2)))
                        if (load32((v18 + (((((v3 + v10) + 1) * v12) + v5) << 2))) == 0):
                            break
                        v15 = (load8u((v17 + (arg1 * 132)) + 122) == v13)
                        v4 = (v15 if (load8u((v17 + (arg1 * 132)) + 122) == v13) else v4)
                        arg0 = (arg1 if v15 else arg0)
                        break
                    arg1 = (v3 + 1)
                    if (v3 != v16):
                        continue
                    break
            arg1 = (v2 != v14)
            v2 = v5
            if arg1:
                continue
            break
        if arg0:
            return 1064
        func29(v8, 1)
        return 54546
        break
    while True:  # block $label7
        v6 = ((v2 * 404) + 9568096)
        if (load32(((v2 * 404) + 9568096) + 268) != 3):
            break
        while True:  # block $label8
            while True:  # block $label9
                v3 = (v5 + (arg0 * 132))
                v4 = load8u((v5 + (arg0 * 132)) + 122)
                # br_table[(load8u((v5 + (arg0 * 132)) + 122) + -64)]
                break
                break
            if (v4 != 10):
                break
            break
        v6 = (v5 + (arg1 * 132))
        store16(v3 + 108, load32((v5 + (arg1 * 132)) + 52))
        v4 = (v5 + (arg0 * 132))
        if (load8u(v6 + 125) != 10):
        else:
        store32(load32(((v2 * 404) + 9568096) + 188) + 88, (3 + (v2 << 16)))
        arg1 = (v5 + (arg1 * 132))
        func207(v8, load32((v5 + (arg1 * 132)) + 28))
        store8(v4 + 125, 0)
        v5 = ((load8u(v9 + 122) * 404) + 9568096)
        if load32(((load8u(v9 + 122) * 404) + 9568096) + 216):
            v7 = load16u(arg1 + 114)
            v11 = load16u(arg1 + 112)
            v12 = load32(9142840)
            v2 = 0
            while True:  # $label11
                v2 = (v2 + 1)
                v13 = ((v2 + 1) + v11)
                v3 = 0
                while True:  # $label10
                    v3 = (v3 + 1)
                    v10 = (load32(9142440) + 2)
                    store32((v12 + ((v13 + ((((v3 + 1) + v7) + ((load32(9142440) + 2) * load32(v5 + 208))) * v10)) << 2)), load32(v5 + 212))
                    v10 = load32(v5 + 216)
                    if (u(v3) < u(load32(v5 + 216))):
                        continue
                    break
                if (u(v2) < u(v10)):
                    continue
                break
        func138(v9)
        store32(arg1 + 36, arg0)
        if (load8u(v6 + 125) != 10):
        else:
        arg0 = func166(load16u(v4 + 114), load16u(v4 + 110), load32(((load8u(v9 + 122) * 404) + 9568096) + 188), 3)
        if func166(load16u(v4 + 114), load16u(v4 + 110), load32(((load8u(v9 + 122) * 404) + 9568096) + 188), 3):
            return (v5 + (arg0 * 132))
        func29(v8, 1)
        return func32(0, v9, 1)
        break
    while True:  # block $label12
        if (func297(v8, arg1) == 0):
            break
        v4 = ((load8u(v9 + 122) * 404) + 9568096)
        if load32(((load8u(v9 + 122) * 404) + 9568096) + 216):
            v2 = (v5 + (arg1 * 132))
            v7 = load16u((v5 + (arg1 * 132)) + 114)
            v11 = load16u(v2 + 112)
            v12 = load32(9142840)
            v2 = 0
            while True:  # $label14
                v2 = (v2 + 1)
                v13 = ((v2 + 1) + v11)
                v3 = 0
                while True:  # $label13
                    v3 = (v3 + 1)
                    v10 = (load32(9142440) + 2)
                    store32((v12 + ((v13 + ((((v3 + 1) + v7) + ((load32(9142440) + 2) * load32(v4 + 208))) * v10)) << 2)), load32(v4 + 212))
                    v10 = load32(v4 + 216)
                    if (u(v3) < u(load32(v4 + 216))):
                        continue
                    break
                if (u(v2) < u(v10)):
                    continue
                break
        func138(v9)
        v2 = (v5 + (arg1 * 132))
        store32((v5 + (arg1 * 132)) + 36, arg0)
        if (load32(v6 + 268) == 2):
            arg1 = (v5 + (arg0 * 132))
            store32((v5 + (arg0 * 132)) + 52, (load32(arg1 + 52) + load32(v2 + 52)))
            store32(arg1 + 60, (load32(arg1 + 60) + load32(v2 + 60)))
        v2 = 0
        v9 = 0
        v6 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        v3 = load32(v8 + 24)
        if (load32(v8 + 24) == 0):
            v3 = func26(16)
            store64(func26(16), 0)
            store64(v3 + 8, 0)
            store32(v8 + 24, v3)
        while True:  # block $label16
            while True:  # block $label15
                arg1 = load32(v3 + 4)
                if (load32(v3 + 4) == 0):
                    arg1 = func26(16)
                    store32(func26(16) + 4, 2)
                    store32(arg1, func26(8))
                    store64(arg1 + 8, 8589934592)
                    store32(v3 + 4, arg1)
                    break
                v4 = load32(arg1 + 8)
                if (load32(arg1 + 8) == 0):
                    break
                v7 = load32(arg1)
                while True:  # $label17
                    if (load32((v7 + (v2 << 2))) == 0):
                        break
                    v2 = (v2 + 2)
                    if (u((v2 + 2)) < u(v4)):
                        continue
                    break
                break
            while True:  # block $label18
                if (load32(v8 + 40) == 0):
                    break
                if load8u(9142917):
                    break
                v2 = load32(9299880)
                if load32(9299880):
                    v2 = (v2 - 1)
                    store32(9299880, (v2 - 1))
                    v9 = load32((load32(9299872) + (v2 << 2)))
                    break
                v9 = load32(9163776)
                v2 = (load32(9163776) + 1)
                store32(9163776, (load32(9163776) + 1))
                v4 = load32(9163784)
                if (u(v2) < u(load32(9163784))):
                    break
                store32(v6, v4)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                v3 = load32(v8 + 24)
                arg1 = load32(load32(v8 + 24) + 4)
                break
            while True:  # block $label19
                v2 = load32(arg1 + 8)
                if (load32(arg1 + 8) != load32(arg1 + 4)):
                    v4 = load32(arg1)
                    break
                v4 = (load32(arg1 + 12) + v2)
                store32(arg1 + 4, (load32(arg1 + 12) + v2))
                v7 = load32(arg1)
                v4 = func26((-1 if (u(v4) > u(1073741823)) else (v4 << 2)))
                if v2:
                    # TODO: memory.copy []
                if v7:
                    v3 = load32(v8 + 24)
                    v2 = load32(arg1 + 8)
                store32(arg1, v4)
                break
            v3 = load32(v3 + 4)
            store32(arg1 + 8, (v2 + 1))
            store32((v4 + (v2 << 2)), 0)
            while True:  # block $label20
                arg1 = load32(v3 + 8)
                if (load32(v3 + 8) != load32(v3 + 4)):
                    v2 = load32(v3)
                    break
                v2 = (load32(v3 + 12) + arg1)
                store32(v3 + 4, (load32(v3 + 12) + arg1))
                v4 = load32(v3)
                v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                if arg1:
                    # TODO: memory.copy []
                if v4:
                    arg1 = load32(v3 + 8)
                store32(v3, v2)
                break
            store32(v3 + 8, (arg1 + 1))
            store32((v2 + (arg1 << 2)), v9)
            if (load32(v8 + 40) == 0):
                break
            arg1 = (load16u(v8 + 114) << 5)
            # TODO: f32.convert_i32_u []
            break
        G.global0 = (v6 + 16)
        while True:  # block $label21
            if (load32((v5 + (arg0 * 132)) + 92) == 0):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v5 + (arg0 * 132)) + 28)):
                    break
            break
        if (load8u(9147141) == 0):
            break
        if (load32(9173808) != load32((v5 + (arg0 * 132)) + 28)):
            break
        Ya(1)
        break
    func29(v8, 1)
    return func28(1, 1)

# ------------------------------------------------------------
# $func655
# ------------------------------------------------------------
def func655(arg0, arg1, arg2, arg3, arg4):
    arg3 = 1
    while True:  # block $label0
        arg2 = load32(9671128)
        arg4 = load8u((load32(9671128) + (arg0 * 132)) + 122)
        if (load32(((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096) + 136) == 0):
            break
        arg1 = load32(arg1)
        v5 = load8u((arg2 + (load32(arg1) * 132)) + 122)
        if (load32(((load8u((arg2 + (load32(arg1) * 132)) + 122) * 404) + 9568096) + 208) == 0):
            if (load32(((arg4 * 404) + 9568096) + 208) == 2):
                break
        while True:  # block $label1
            if (u(load32(9142848)) >= u((load32(load32(9142424) + 72) * 2400))):
                break
            arg1 = load32((arg2 + (arg1 * 132)) + 56)
            if (load32((arg2 + (arg1 * 132)) + 56) == 0):
                break
            if (arg1 == load16u((arg2 + (arg0 * 132)) + 110)):
                break
            if (load32(38984) != v5):
                break
            break
        arg3 = 0
        break
    return arg3

# ------------------------------------------------------------
# $func656
# ------------------------------------------------------------
def func656(arg0):
    while True:  # block $label0
        v8 = load32(9671128)
        v13 = load32(arg0 + 32)
        v1 = (load32(9671128) + (load32(arg0 + 32) * 132))
        if (load32((load32(9671128) + (load32(arg0 + 32) * 132)) + 36) == 0):
            if (load8u(v1 + 125) != 3):
                break
        while True:  # block $label1
            v5 = load8u(v1 + 122)
            if (load32(((load8u(v1 + 122) * 404) + 9568096) + 268) != 3):
                break
            while True:  # block $label2
                while True:  # block $label3
                    while True:  # block $label4
                        v1 = load8u(arg0 + 122)
                        # br_table[(load8u(arg0 + 122) + -64)]
                        break
                        break
                    if (v1 == 10):
                        break
                    break
                if (load8u(9216060) == 0):
                    break
                break
            v9 = load32(9142440)
            v14 = (load32(9142440) + 2)
            v15 = ((load32(9142440) + 2) * load32(((v5 * 404) + 9568096) + 208))
            v10 = load16u(arg0 + 112)
            v16 = (load16u(arg0 + 112) + 9)
            v11 = load16u(arg0 + 114)
            v17 = (load16u(arg0 + 114) + 9)
            v18 = (v11 - 10)
            v2 = (v10 - 10)
            v19 = load32(9142840)
            v6 = 2147483647
            while True:  # $label7
                v12 = (v2 + 1)
                if (u(v2) < u(v9)):
                    v1 = (v10 - v2)
                    v20 = ((v10 - v2) * v1)
                    v1 = v18
                    while True:  # $label6
                        while True:  # block $label5
                            v3 = v1
                            if (u(v9) <= u(v1)):
                                break
                            if ((v2 | v3) < 0):
                                break
                            v1 = (v11 - v3)
                            v7 = (((v11 - v3) * v1) + v20)
                            if ((((v11 - v3) * v1) + v20) >= v6):
                                break
                            v1 = load32((v19 + (((((v3 + v15) + 1) * v14) + v12) << 2)))
                            if (load32((v19 + (((((v3 + v15) + 1) * v14) + v12) << 2))) == 0):
                                break
                            v7 = (load8u((v8 + (v1 * 132)) + 122) == v5)
                            v6 = (v7 if (load8u((v8 + (v1 * 132)) + 122) == v5) else v6)
                            v4 = (v1 if v7 else v4)
                            break
                        v1 = (v3 + 1)
                        if (v3 != v17):
                            continue
                        break
                v1 = (v2 != v16)
                v2 = v12
                if v1:
                    continue
                break
            if v4:
                store32(arg0 + 32, v4)
                return 0
            if (load32(38984) != v5):
                break
            store8(arg0 + 129, 10)
            return 1
            break
        store8(arg0 + 123, 0)
        store32(arg0 + 32, 0)
        v1 = (v8 + (v13 * 132))
        store16(arg0 + 116, load16u((v8 + (v13 * 132)) + 112))
        store16(arg0 + 118, load16u(v1 + 114))
        break
    return 0

# ------------------------------------------------------------
# $dc
# Export: dc
# ------------------------------------------------------------
def dc():
    """Exported as dc."""
    if ((load8u(9147210) | load8u(9147152)) == 0):
        store8(9140312, 1)

# ------------------------------------------------------------
# $na
# Export: na
# ------------------------------------------------------------
def na(arg0):
    """Exported as na."""
    if (arg0 == 1):
    store32(9561704, 0)
    func344()

# ------------------------------------------------------------
# $qa
# Export: qa
# ------------------------------------------------------------
def qa():
    """Exported as qa."""
    v3 = load32(9561728)
    while True:  # block $label0
        v1 = load32(9561704)
        if (load32(9561704) == 0):
            break
        v4 = load32(v3 + 4)
        v5 = load32(9561696)
        while True:  # $label1
            v6 = ((v0 << 2) + v5)
            if (u(load32(((v0 << 2) + v5) + 4)) >= u(v4)):
                break
            v0 = (load32(v6 + 8) + v0)
            if (u((load32(v6 + 8) + v0)) < u(v1)):
                continue
            break
        v0 = 0
        break
    store32(9561704, v0)
    if load32(9561732):
        while True:  # $label3
            v5 = load32((v3 + (v2 << 2)))
            while True:  # block $label2
                if (load32(9561700) != v0):
                    v1 = load32(9561696)
                    break
                v1 = (load32(9561708) + v0)
                store32(9561700, (load32(9561708) + v0))
                v4 = load32(9561696)
                v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
                if v0:
                    # TODO: memory.copy []
                if v4:
                    v3 = load32(9561728)
                    v0 = load32(9561704)
                store32(9561696, v1)
                break
            store32(9561704, (v0 + 1))
            store32((v1 + (v0 << 2)), v5)
            v0 = load32(9561704)
            v2 = (v2 + 1)
            if (u((v2 + 1)) < u(load32(9561732))):
                continue
            break
    store32(9561828, v0)
    while True:  # block $label4
        if (load32(9561700) != v0):
            v2 = load32(9561696)
            break
        v2 = (load32(9561708) + v0)
        store32(9561700, (load32(9561708) + v0))
        v1 = load32(9561696)
        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
        if v0:
            # TODO: memory.copy []
        if v1:
            v3 = load32(9561728)
            v0 = load32(9561704)
        store32(9561696, v2)
        break
    store32(9561704, (v0 + 1))
    store32((v2 + (v0 << 2)), 0)
    v3 = (load32((((load32(9561732) << 2) + v3) - 8)) + 10)
    while True:  # block $label5
        v0 = load32(9561704)
        if (load32(9561704) != load32(9561700)):
            v1 = v2
            break
        v1 = (load32(9561708) + v0)
        store32(9561700, (load32(9561708) + v0))
        v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
        if v0:
            # TODO: memory.copy []
        store32(9561696, v1)
        v0 = load32(9561704)
        break
    store32(9561704, (v0 + 1))
    store32((v1 + (v0 << 2)), v3)
    while True:  # block $label6
        v0 = load32(9561704)
        if (load32(9561704) != load32(9561700)):
            v2 = v1
            break
        v2 = (load32(9561708) + v0)
        store32(9561700, (load32(9561708) + v0))
        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
        if v0:
            # TODO: memory.copy []
        store32(9561696, v2)
        v0 = load32(9561704)
        break
    store32(9561704, (v0 + 1))
    store32((v2 + (v0 << 2)), 3)
    v2 = load32(9561728)
    if load32(9561728):
        store32(9561728, 0)

# ------------------------------------------------------------
# $pa
# Export: pa
# ------------------------------------------------------------
def pa(arg0):
    """Exported as pa."""
    arg0 = (load32(9561836) + arg0)
    store32(9561824, (load32(9561836) + arg0))
    # TODO: i32.div_u []
    v3 = 25
    store32((arg0 * 250), 25)
    while True:  # block $label1
        while True:  # block $label0
            arg0 = load32(59160)
            if (u(load32(59160)) < u(v3)):
                if (u(((v3 - arg0) * 25)) > u(249)):
                    break
                break
            if (u(arg0) <= u(v3)):
                break
            break
        store32(59160, v3)
        break
    arg0 = 0
    v1 = load32(9561704)
    if load32(9561704):
        arg0 = load32(9561828)
        store32((load32(9561696) + (load32(9561828) << 2)) + 8, (v1 - arg0))
        arg0 = load32(9561704)
    store32(9561828, arg0)
    while True:  # block $label2
        if (load32(9561700) != arg0):
            v2 = load32(9561696)
            break
        v1 = (load32(9561708) + arg0)
        store32(9561700, (load32(9561708) + arg0))
        v4 = load32(9561696)
        v2 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
        if arg0:
            # TODO: memory.copy []
        if v4:
            arg0 = load32(9561704)
        store32(9561696, v2)
        break
    store32(9561704, (arg0 + 1))
    store32((v2 + (arg0 << 2)), 0)
    v4 = (v3 + 10)
    while True:  # block $label3
        arg0 = load32(9561704)
        if (load32(9561704) != load32(9561700)):
            v1 = v2
            break
        v1 = (load32(9561708) + arg0)
        store32(9561700, (load32(9561708) + arg0))
        v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
        if arg0:
            # TODO: memory.copy []
        store32(9561696, v1)
        arg0 = load32(9561704)
        break
    store32(9561704, (arg0 + 1))
    store32((v1 + (arg0 << 2)), v4)
    while True:  # block $label4
        arg0 = load32(9561704)
        if (load32(9561704) != load32(9561700)):
            v2 = v1
            break
        v2 = (load32(9561708) + arg0)
        store32(9561700, (load32(9561708) + arg0))
        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
        if arg0:
            # TODO: memory.copy []
        store32(9561696, v2)
        arg0 = load32(9561704)
        break
    store32(9561704, (arg0 + 1))
    store32((v2 + (arg0 << 2)), 3)

# ------------------------------------------------------------
# $func664
# ------------------------------------------------------------
def func664(arg0, arg1, arg2):
    v5 = load32(arg1)
    store32(41092, load32(arg1 + 4))
    store8(9147212, (load32(arg1 + 8) != 0))
    store8(9561848, (load32(arg1 + 12) != 0))
    v3 = load32(9142892)
    while True:  # block $label1
        while True:  # block $label0
            if (load8u(9147210) == 0):
                if v3:
                    store32(9142892, 0)
                    arg0 = load32(9561692)
                    if load32(9561692):
                        store32(9561692, 0)
                store32(9142892, v5)
                store8(9147210, 1)
                v9 = (i64(v5) * 286704)
                arg0 = (-1 if i32(((v9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(v5) * 286704)))
                arg2 = func26((-1 if i32(((v9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(v5) * 286704))))
                # TODO: memory.fill []
                break
            if (v3 == v5):
                break
            arg0 = 0
            store32(9142892, v5)
            v9 = (i64(v5) * 286704)
            v7 = (-1 if i32(((v9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(v5) * 286704)))
            arg2 = func26((-1 if i32(((v9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(v5) * 286704))))
            # TODO: memory.fill []
            v7 = load32(9561692)
            while True:  # block $label3
                v3 = (v3 if (u(v3) < u(v5)) else v5)
                if (v3 if (u(v3) < u(v5)) else v5):
                    if (u(v3) >= u(4)):
                        v8 = (v3 & -4)
                        v5 = 0
                        while True:  # $label2
                            v4 = (arg0 * 286704)
                            # TODO: memory.copy []
                            v4 = ((arg0 | 1) * 286704)
                            # TODO: memory.copy []
                            v4 = ((arg0 | 2) * 286704)
                            # TODO: memory.copy []
                            v4 = ((arg0 | 3) * 286704)
                            # TODO: memory.copy []
                            arg0 = (arg0 + 4)
                            v5 = (v5 + 4)
                            if ((v5 + 4) != v8):
                                continue
                            break
                    v3 = (v3 & 3)
                    if ((v3 & 3) == 0):
                        break
                    v5 = 0
                    while True:  # $label4
                        v8 = (arg0 * 286704)
                        # TODO: memory.copy []
                        arg0 = (arg0 + 1)
                        v5 = (v5 + 1)
                        if ((v5 + 1) != v3):
                            continue
                        break
                    break
                if (v7 == 0):
                    break
                break
            v5 = load32(9142892)
            break
        store32(9561692, arg2)
        break
    v7 = 1
    arg0 = load8u(9147212)
    v8 = (v5 if load8u(9147212) else load32(41092))
    if (u((v5 if load8u(9147212) else load32(41092))) > u(1)):
        v5 = 4
        while True:  # $label5
            arg2 = (arg1 + (v5 << 2))
            v3 = load32((arg1 + (v5 << 2)) + 12)
            v4 = load32(arg2)
            v6 = load32(arg2 + 4)
            arg0 = (load32(9561692) + (v7 * 286704))
            store16((load32(9561692) + (v7 * 286704)) + 4, load32(arg2 + 8))
            store16(arg0 + 2, v6)
            store16(arg0, v4)
            store16(arg0 + 6, v3)
            v3 = load32(arg2 + 28)
            v4 = load32(arg2 + 16)
            v6 = load32(arg2 + 20)
            store16(arg0 + 12, load32(arg2 + 24))
            store16(arg0 + 10, v6)
            store16(arg0 + 8, v4)
            store16(arg0 + 14, v3)
            v3 = load32(arg2 + 44)
            v4 = load32(arg2 + 32)
            v6 = load32(arg2 + 36)
            store16(arg0 + 20, load32(arg2 + 40))
            store16(arg0 + 18, v6)
            store16(arg0 + 16, v4)
            store16(arg0 + 22, v3)
            v3 = load32(arg2 + 60)
            v4 = load32(arg2 + 48)
            v6 = load32(arg2 + 52)
            store16(arg0 + 28, load32(arg2 + 56))
            store16(arg0 + 26, v6)
            store16(arg0 + 24, v4)
            store16(arg0 + 30, v3)
            v3 = load32(arg2 + 76)
            v4 = load32((arg2 - -64))
            v6 = load32(arg2 + 68)
            store16(arg0 + 36, load32(arg2 + 72))
            store16(arg0 + 34, v6)
            store16(arg0 + 32, v4)
            store16(arg0 + 38, v3)
            v3 = load32(arg2 + 92)
            v4 = load32(arg2 + 80)
            v6 = load32(arg2 + 84)
            store16(arg0 + 44, load32(arg2 + 88))
            store16(arg0 + 42, v6)
            store16(arg0 + 40, v4)
            store16(arg0 + 46, v3)
            v3 = load32(arg2 + 108)
            v4 = load32(arg2 + 96)
            v6 = load32(arg2 + 100)
            store16(arg0 + 52, load32(arg2 + 104))
            store16(arg0 + 50, v6)
            store16(arg0 + 48, v4)
            store16(arg0 + 54, v3)
            v3 = load32(arg2 + 124)
            v4 = load32(arg2 + 112)
            v6 = load32(arg2 + 116)
            store16(arg0 + 60, load32(arg2 + 120))
            store16(arg0 + 58, v6)
            store16(arg0 + 56, v4)
            store16(arg0 + 62, v3)
            v3 = load32(arg2 + 140)
            v4 = load32(arg2 + 128)
            v6 = load32(arg2 + 132)
            store16(arg0 + 68, load32(arg2 + 136))
            store16(arg0 + 66, v6)
            store16((arg0 - -64), v4)
            store16(arg0 + 70, v3)
            v3 = load32(arg2 + 144)
            v4 = load32(arg2 + 148)
            v6 = load32(arg2 + 152)
            store16(arg0 + 78, load32(arg2 + 156))
            store16(arg0 + 76, v6)
            store16(arg0 + 74, v4)
            store16(arg0 + 72, v3)
            store32(arg0 + 284608, load32(arg2 + 160))
            store32(arg0 + 283960, load32(arg2 + 164))
            store32(arg0 + 284616, load32(arg2 + 168))
            v3 = load32(arg2 + 172)
            store8((arg0 + 283974), load32(arg2 + 172))
            store8((arg0 + 283973), ((v3 & 0xFFFFFFFF) >> 8))
            store8(arg0 + 283972, ((v3 & 0xFFFFFFFF) >> 16))
            arg2 = load32(arg2 + 176)
            store32(arg0 + 283908, v7)
            store32(arg0 + 286684, arg2)
            v5 = (v5 + 45)
            v7 = (v7 + 1)
            if ((v7 + 1) != v8):
                continue
            break
    else:
    if (arg0 & 255):
    return 0

# ------------------------------------------------------------
# $ra
# Export: ra
# ------------------------------------------------------------
def ra(arg0):
    """Exported as ra."""
    while True:  # block $label4
        while True:  # block $label0
            while True:  # block $label1
                v1 = load32(9561728)
                if (load32(load32(9561728) + 4) == -1):
                    arg0 = load32(v1 + 8)
                    store32(59164, load32(v1 + 8))
                    if (arg0 == load32(9142384)):
                        break
                    arg0 = 3
                    v4 = load32(9561732)
                    if (u(load32(9561732)) <= u(3)):
                        break
                    while True:  # $label3
                        v2 = (v1 + (arg0 << 2))
                        v3 = load32((v1 + (arg0 << 2)) + 4)
                        v5 = (arg0 + 3)
                        v6 = (load32((v1 + (arg0 << 2)) + 4) + (arg0 + 3))
                        v7 = load32(v2 + 8)
                        arg0 = ((load32((v1 + (arg0 << 2)) + 4) + (arg0 + 3)) + load32(v2 + 8))
                        while True:  # block $label2
                            v2 = load32(v2)
                            if (u(load32(v2)) > u(255)):
                                break
                            v2 = ((v2 << 3) + 9213824)
                            v8 = load32(((v2 << 3) + 9213824))
                            if (load32(((v2 << 3) + 9213824)) == 0):
                                break
                            v6 = ((v1 + (v6 << 2)) if v7 else 0)
                            v5 = ((v1 + (v5 << 2)) if v3 else 0)
                            v7 = load32(v2 + 4)
                            if load32(v2 + 4):
                                # call_indirect[v7]
                                if (indirect_call(v7) == 0):
                                    break
                            else:
                            # call_indirect[v8]
                            break
                        if (u(arg0) < u(v4)):
                            continue
                        break
                    store32(59164, 0)
                    v1 = load32(9561728)
                    if load32(9561728):
                        break
                    break
                if load8u(9140304):
                    break
                while True:  # block $label5
                    v1 = load32(9561704)
                    if (load32(9561704) != load32(9561700)):
                        v3 = load32(9561696)
                        break
                    v3 = (load32(9561708) + v1)
                    store32(9561700, (load32(9561708) + v1))
                    v2 = load32(9561696)
                    v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                    if v1:
                        # TODO: memory.copy []
                    if v2:
                        v1 = load32(9561704)
                    store32(9561696, v3)
                    break
                store32(9561704, (v1 + 1))
                v4 = 2
                store32((v3 + (v1 << 2)), arg0)
                v1 = load32(9561728)
                if (u(load32(9561732)) > u(2)):
                    while True:  # $label6
                        v5 = load32((v1 + (v4 << 2)))
                        arg0 = load32(9561704)
                        if (load32(9561704) == load32(9561700)):
                            v2 = (load32(9561708) + arg0)
                            store32(9561700, (load32(9561708) + arg0))
                            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                            if arg0:
                                # TODO: memory.copy []
                            store32(9561696, v2)
                            v1 = load32(9561728)
                            v3 = v2
                            arg0 = load32(9561704)
                        store32(9561704, (arg0 + 1))
                        store32((v3 + (arg0 << 2)), v5)
                        v4 = (v4 + 1)
                        if (u((v4 + 1)) < u(load32(9561732))):
                            continue
                        break
                if v1:
                    break
                break
                break
            store32(59164, 0)
            break
        break
    return af(v1)

# ------------------------------------------------------------
# $func669
# ------------------------------------------------------------
def func669(arg0, arg1, arg2):
    while True:  # block $label0
        v6 = load32(9671128)
        v3 = (load32(9671128) + (arg0 * 132))
        if ((arg2 == 0) & (load8u((load32(9671128) + (arg0 * 132)) + 125) == 3)):
            break
        arg2 = load32(v3 + 44)
        v4 = (load32(v3 + 44) << 2)
        v5 = load32(9215884)
        arg2 = load32((load32(9215884) + (arg2 << 4)) + 12)
        while True:  # block $label6
            while True:  # block $label5
                while True:  # block $label4
                    while True:  # block $label3
                        while True:  # block $label2
                            while True:  # block $label1
                                # br_table[load32(arg1 + 28)]
                                break
                                break
                            if (load32((v5 + ((v4 << 2) | 4))) == 6):
                                break
                            break
                            break
                        if (load32((v5 + ((v4 << 2) | 4))) == 4):
                            break
                        break
                        break
                    if (load32((v5 + ((v4 << 2) | 4))) == 13):
                        break
                    break
                    break
                if (load32((v5 + ((v4 << 2) | 4))) == 46):
                    break
                break
                break
            arg2 = load32((v6 + (arg0 * 132)) + 36)
            if (load32((v6 + (arg0 * 132)) + 36) == 0):
                break
            break
        while True:  # block $label15
            arg0 = 0
            while True:  # block $label7
                if (arg2 == 0):
                    break
                if (load32(v3 + 28) == arg2):
                    break
                v3 = load32(9671128)
                while True:  # block $label8
                    if load32(arg1 + 8):
                        arg0 = load32(arg1 + 104)
                        if (load32(arg1 + 104) == 0):
                            break
                        arg2 = load32((v3 + (arg2 * 132)) + 28)
                        v3 = load32(arg1 + 96)
                        arg1 = 0
                        while True:  # $label9
                            if (arg2 != load32((v3 + (arg1 << 2)))):
                                arg1 = (arg1 + 1)
                                if ((arg1 + 1) != arg0):
                                    continue
                                break
                            break
                        arg0 = 1
                        if (arg1 < 0):
                            break
                        break
                    arg2 = load8u((v3 + (arg2 * 132)) + 122)
                    arg1 = load32(arg1 + 36)
                    if (u(load32(arg1 + 36)) <= u(3)):
                        while True:  # block $label13
                            while True:  # block $label12
                                while True:  # block $label11
                                    while True:  # block $label10
                                        # br_table[(arg1 - 1)]
                                        break
                                        break
                                    arg0 = 1
                                    while True:  # block $label14
                                        arg1 = ((arg2 * 404) + 9568096)
                                        if load32(((arg2 * 404) + 9568096) + 264):
                                            break
                                        if (load32(arg1 + 268) == 1):
                                            break
                                        arg0 = (load32(((arg2 * 404) + 9568096) + 92) == 0)
                                        break
                                    arg0 = ((arg0 | (load32(38456) == arg2)) | (load32(38764) == arg2))
                                    break
                                    break
                                arg0 = (load32(((arg2 * 404) + 9568096) + 264) != 0)
                                break
                                break
                            arg0 = (load32(((arg2 * 404) + 9568096) + 264) != 1)
                            break
                        break
                    arg0 = 1
                    if ((arg1 - 4) == arg2):
                        break
                    break
                arg0 = 0
                break
            break
        v7 = arg0
        break
    return v7

# ------------------------------------------------------------
# $func670
# ------------------------------------------------------------
def func670(arg0, arg1, arg2):
    while True:  # block $label0
        v4 = load32(9671128)
        if ((arg2 == 0) & (load8u((load32(9671128) + (arg0 * 132)) + 125) == 3)):
            break
        arg2 = load32(arg1 + 96)
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label2
                    while True:  # block $label1
                        # br_table[load32(arg1 + 36)]
                        break
                        break
                    arg1 = (v4 + (arg0 * 132))
                    v3 = load32(arg2)
                    if (load32(arg2) != 2147483647):
                        if (u(load32(arg1 + 52)) < u(v3)):
                            break
                    v3 = load32(arg2 + 4)
                    if (load32(arg2 + 4) != 2147483647):
                        if (u(load32(arg1 + 60)) < u(v3)):
                            break
                    arg1 = load32(arg2 + 8)
                    v3 = (load32(arg2 + 8) == 2147483647)
                    if ((load32(arg2 + 8) == 2147483647) == 0):
                        if (u(load32((v4 + (arg0 * 132)) + 64)) < u(arg1)):
                            break
                    if (v3 == 0):
                        if (u(load32((v4 + (arg0 * 132)) + 68)) < u(load32(arg2 + 12))):
                            break
                    arg1 = load32(arg2 + 16)
                    v3 = (load32(arg2 + 16) == 2147483647)
                    if ((load32(arg2 + 16) == 2147483647) == 0):
                        if (u(load32((v4 + (arg0 * 132)) + 72)) < u(arg1)):
                            break
                    if (v3 == 0):
                        if (u(load32((v4 + (arg0 * 132)) + 76)) < u(load32(arg2 + 20))):
                            break
                    arg1 = load32(arg2 + 24)
                    if (load32(arg2 + 24) == 2147483647):
                        break
                    if (u(load32((v4 + (arg0 * 132)) + 84)) >= u(arg1)):
                        break
                    break
                    break
                arg1 = (v4 + (arg0 * 132))
                v3 = load32(arg2)
                if (load32(arg2) != 2147483647):
                    if (u(load32(arg1 + 52)) > u(v3)):
                        break
                v3 = load32(arg2 + 4)
                if (load32(arg2 + 4) != 2147483647):
                    if (u(load32(arg1 + 60)) > u(v3)):
                        break
                arg1 = load32(arg2 + 8)
                v3 = (load32(arg2 + 8) == 2147483647)
                if ((load32(arg2 + 8) == 2147483647) == 0):
                    if (u(load32((v4 + (arg0 * 132)) + 64)) > u(arg1)):
                        break
                if (v3 == 0):
                    if (u(load32((v4 + (arg0 * 132)) + 68)) > u(load32(arg2 + 12))):
                        break
                arg1 = load32(arg2 + 16)
                v3 = (load32(arg2 + 16) == 2147483647)
                if ((load32(arg2 + 16) == 2147483647) == 0):
                    if (u(load32((v4 + (arg0 * 132)) + 72)) > u(arg1)):
                        break
                if (v3 == 0):
                    if (u(load32((v4 + (arg0 * 132)) + 76)) > u(load32(arg2 + 20))):
                        break
                arg1 = load32(arg2 + 24)
                if (load32(arg2 + 24) == 2147483647):
                    break
                if (u(load32((v4 + (arg0 * 132)) + 84)) <= u(arg1)):
                    break
                break
                break
            arg1 = (v4 + (arg0 * 132))
            v3 = load32(arg2)
            if (load32(arg2) != 2147483647):
                if (load32(arg1 + 52) != v3):
                    break
            v3 = load32(arg2 + 4)
            if (load32(arg2 + 4) != 2147483647):
                if (load32(arg1 + 60) != v3):
                    break
            arg1 = load32(arg2 + 8)
            v3 = (load32(arg2 + 8) == 2147483647)
            if ((load32(arg2 + 8) == 2147483647) == 0):
                if (load32((v4 + (arg0 * 132)) + 64) != arg1):
                    break
            if (v3 == 0):
                if (load32((v4 + (arg0 * 132)) + 68) != load32(arg2 + 12)):
                    break
            arg1 = load32(arg2 + 16)
            v3 = (load32(arg2 + 16) == 2147483647)
            if ((load32(arg2 + 16) == 2147483647) == 0):
                if (load32((v4 + (arg0 * 132)) + 72) != arg1):
                    break
            if (v3 == 0):
                if (load32((v4 + (arg0 * 132)) + 76) != load32(arg2 + 20)):
                    break
            arg1 = load32(arg2 + 24)
            if (load32(arg2 + 24) == 2147483647):
                break
            if (load32((v4 + (arg0 * 132)) + 84) != arg1):
                break
            break
        v5 = 1
        break
    return v5

# ------------------------------------------------------------
# $func671
# ------------------------------------------------------------
def func671(arg0, arg1, arg2):
    while True:  # block $label0
        v6 = load32(9671128)
        if ((arg2 == 0) & (load8u((load32(9671128) + (arg0 * 132)) + 125) == 3)):
            break
        while True:  # block $label1
            if (load32(arg1 + 8) == 0):
                v5 = load32(arg1 + 104)
                if (load32(arg1 + 104) == 0):
                    break
                v4 = (v6 + (arg0 * 132))
                arg2 = (load32(arg1 + 28) << 1)
                v9 = ((load32(arg1 + 28) << 1) * arg2)
                v10 = load32(arg1 + 96)
                arg2 = 0
                if load32(arg1 + 36):
                    break
                while True:  # $label3
                    while True:  # block $label2
                        arg1 = (v6 + (load32((v10 + (arg2 << 2))) * 132))
                        if (load8u((v6 + (load32((v10 + (arg2 << 2))) * 132)) + 125) == 3):
                            break
                        v3 = ((load16u(v4 + 112) - load16u(arg1 + 112)) << 1)
                        v3 = ((load16u(v4 + 114) - load16u(arg1 + 114)) << 1)
                        if ((((((load16u(v4 + 112) - load16u(arg1 + 112)) << 1) * v3) + (((load16u(v4 + 114) - load16u(arg1 + 114)) << 1) * v3)) - 1) > v9):
                            break
                        if (load32(arg1 + 28) == arg0):
                            break
                        v3 = 1
                        break
                        break
                    arg2 = (arg2 + 1)
                    if ((arg2 + 1) != v5):
                        continue
                    break
                v3 = 0
                break
            v5 = load32(9142892)
            if (load32(9142892) == 0):
                break
            v9 = load32(arg1 + 64)
            v10 = (load32(arg1 + 64) + (v5 << 2))
            v4 = (v6 + (arg0 * 132))
            v3 = 1
            arg0 = (load32(arg1 + 28) << 1)
            v7 = ((load32(arg1 + 28) << 1) * arg0)
            arg0 = 0
            v15 = load32(9561692)
            v16 = load32(9142420)
            arg1 = load32(arg1 + 36)
            if (u(load32(arg1 + 36)) <= u(3)):
                v12 = load32(38764)
                v13 = load32(38456)
                v11 = (arg1 - 1)
                while True:  # $label13
                    while True:  # block $label4
                        arg1 = (arg0 << 2)
                        if (load32((v9 + (arg0 << 2))) == 0):
                            if (load32(v10) == 0):
                                break
                            if (load32((arg1 + v16)) == 0):
                                break
                        arg1 = 0
                        while True:  # $label12
                            while True:  # block $label9
                                while True:  # block $label8
                                    while True:  # block $label5
                                        while True:  # block $label6
                                            while True:  # block $label7
                                                # br_table[v11]
                                                break
                                                break
                                            if (load32(((arg1 * 404) + 9568096) + 264) == 1):
                                                break
                                            break
                                            break
                                        if (load32(((arg1 * 404) + 9568096) + 264) == 0):
                                            break
                                        break
                                        break
                                    arg2 = ((arg1 * 404) + 9568096)
                                    if load32(((arg1 * 404) + 9568096) + 264):
                                        break
                                    if (load32(arg2 + 268) == 1):
                                        break
                                    if (load32(arg2 + 92) == 0):
                                        break
                                    if (arg1 == v13):
                                        break
                                    if (arg1 == v12):
                                        break
                                    break
                                arg2 = load32((((v15 + (arg0 * 286704)) + (arg1 << 2)) + 284636))
                                if (load32((((v15 + (arg0 * 286704)) + (arg1 << 2)) + 284636)) == 0):
                                    break
                                v17 = load32(arg2 + 8)
                                if (load32(arg2 + 8) == 0):
                                    break
                                v18 = load32(arg2)
                                arg2 = 0
                                while True:  # $label11
                                    while True:  # block $label10
                                        v8 = load32((v18 + (arg2 << 2)))
                                        if (load32((v18 + (arg2 << 2))) == 0):
                                            break
                                        v8 = (v6 + (v8 * 132))
                                        v14 = ((load16u(v4 + 112) - load16u((v6 + (v8 * 132)) + 112)) << 1)
                                        v14 = ((load16u(v4 + 114) - load16u(v8 + 114)) << 1)
                                        if ((((((load16u(v4 + 112) - load16u((v6 + (v8 * 132)) + 112)) << 1) * v14) + (((load16u(v4 + 114) - load16u(v8 + 114)) << 1) * v14)) - 1) > v7):
                                            break
                                        if (load32(v8 + 28) != load32(v4 + 28)):
                                            break
                                        break
                                    arg2 = (arg2 + 1)
                                    if ((arg2 + 1) != v17):
                                        continue
                                    break
                                break
                            arg1 = (arg1 + 1)
                            if ((arg1 + 1) != 255):
                                continue
                            break
                        break
                    arg0 = (arg0 + 1)
                    v3 = (u((arg0 + 1)) < u(v5))
                    if (arg0 != v5):
                        continue
                    break
                break
            v8 = ((arg1 - 4) << 2)
            while True:  # $label17
                while True:  # block $label14
                    arg1 = (arg0 << 2)
                    if (load32((v9 + (arg0 << 2))) == 0):
                        if (load32(v10) == 0):
                            break
                        if (load32((arg1 + v16)) == 0):
                            break
                    arg1 = load32((((v15 + (arg0 * 286704)) + v8) + 284636))
                    if (load32((((v15 + (arg0 * 286704)) + v8) + 284636)) == 0):
                        break
                    v12 = load32(arg1 + 8)
                    if (load32(arg1 + 8) == 0):
                        break
                    v13 = load32(arg1)
                    arg2 = 0
                    while True:  # $label16
                        while True:  # block $label15
                            arg1 = load32((v13 + (arg2 << 2)))
                            if (load32((v13 + (arg2 << 2))) == 0):
                                break
                            arg1 = (v6 + (arg1 * 132))
                            v11 = ((load16u(v4 + 112) - load16u((v6 + (arg1 * 132)) + 112)) << 1)
                            v11 = ((load16u(v4 + 114) - load16u(arg1 + 114)) << 1)
                            if ((((((load16u(v4 + 112) - load16u((v6 + (arg1 * 132)) + 112)) << 1) * v11) + (((load16u(v4 + 114) - load16u(arg1 + 114)) << 1) * v11)) - 1) > v7):
                                break
                            if (load32(arg1 + 28) != load32(v4 + 28)):
                                break
                            break
                        arg2 = (arg2 + 1)
                        if ((arg2 + 1) != v12):
                            continue
                        break
                    break
                arg0 = (arg0 + 1)
                v3 = (u((arg0 + 1)) < u(v5))
                if (arg0 != v5):
                    continue
                break
            break
            break
        while True:  # $label18
            v3 = 0
            arg1 = (v6 + (load32((v10 + (arg2 << 2))) * 132))
            if (load8u((v6 + (load32((v10 + (arg2 << 2))) * 132)) + 125) == 3):
                break
            v7 = ((load16u(v4 + 112) - load16u(arg1 + 112)) << 1)
            v7 = ((load16u(v4 + 114) - load16u(arg1 + 114)) << 1)
            if ((((((load16u(v4 + 112) - load16u(arg1 + 112)) << 1) * v7) + (((load16u(v4 + 114) - load16u(arg1 + 114)) << 1) * v7)) - 1) > v9):
                break
            if (load32(arg1 + 28) == arg0):
                break
            v3 = 1
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != v5):
                continue
            break
        break
    return v3

# ------------------------------------------------------------
# $func672
# ------------------------------------------------------------
def func672(arg0, arg1, arg2):
    while True:  # block $label0
        v3 = (load32(9671128) + (arg0 * 132))
        if (load8u((load32(9671128) + (arg0 * 132)) + 125) != 3):
            break
        if arg2:
            break
        return 0
        break
    arg0 = load16u(v3 + 114)
    v5 = load16u(v3 + 112)
    arg2 = load32(arg1 + 20)
    while True:  # block $label2
        while True:  # block $label4
            while True:  # block $label3
                v3 = ((load8u(v3 + 122) * 404) + 9568096)
                v6 = (load32(((load8u(v3 + 122) * 404) + 9568096) + 216) - 1)
                if (load32(((load8u(v3 + 122) * 404) + 9568096) + 216) - 1):
                    v3 = load32(v3 + 220)
                    while True:  # block $label1
                        v7 = (u(arg2) > u(v5))
                        if (u(arg2) > u(v5)):
                            break
                        if (u((load32(arg1 + 28) + arg2)) <= u(v5)):
                            break
                        v8 = load32(arg1 + 24)
                        if (u(load32(arg1 + 24)) > u(arg0)):
                            break
                        v4 = 1
                        if (u((load32(arg1 + 40) + v8)) > u(arg0)):
                            break
                        break
                    v3 = (v3 - 1)
                    v4 = (v5 + v6)
                    if (u(arg2) > u((v5 + v6))):
                        break
                    if (u((load32(arg1 + 28) + arg2)) <= u(v4)):
                        break
                    v6 = load32(arg1 + 24)
                    if (u(arg0) >= u(load32(arg1 + 24))):
                        v4 = 1
                        if (u((load32(arg1 + 40) + v6)) > u(arg0)):
                            break
                    v6 = load32(arg1 + 24)
                    arg0 = (arg0 + v3)
                    if (u(load32(arg1 + 24)) > u((arg0 + v3))):
                        break
                    v4 = 1
                    if (u((load32(arg1 + 40) + v6)) > u(arg0)):
                        break
                    break
                if (u(arg2) > u(v5)):
                    break
                if (u((load32(arg1 + 28) + arg2)) <= u(v5)):
                    break
                arg2 = load32(arg1 + 24)
                if (u(load32(arg1 + 24)) > u(arg0)):
                    break
                v4 = (u((load32(arg1 + 40) + arg2)) > u(arg0))
                break
                break
            arg0 = (arg0 + v3)
            break
        if v7:
            return 0
        if (u(v5) >= u((load32(arg1 + 28) + arg2))):
            return 0
        v4 = 0
        arg2 = load32(arg1 + 24)
        if (u(load32(arg1 + 24)) > u(arg0)):
            break
        return (u((load32(arg1 + 40) + arg2)) > u(arg0))
        break
    return v4

# ------------------------------------------------------------
# $le
# Export: le
# ------------------------------------------------------------
def le(arg0):
    """Exported as le."""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(9142912, arg0)
    v2 = (arg0 << 2)
    v3 = (-1 if (u(arg0) > u(1073741823)) else (arg0 << 2))
    arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
    # TODO: memory.fill []
    store32(9142908, arg0)
    store32(v1 + 12, v2)
    arg0 = load32(9142908)
    G.global0 = (v1 + 16)
    return arg0

# ------------------------------------------------------------
# $ke
# Export: ke
# ------------------------------------------------------------
def ke():
    """Exported as ke."""
    v0 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    v0 = load32(9687216)
    v1 = func26(load32(9687216))
    store32(9687204, func26(load32(9687216)))
    store32(9147392, load32(9687216))
    return load32(9687204)

# ------------------------------------------------------------
# $je
# Export: je
# ------------------------------------------------------------
def je(arg0):
    """Exported as je."""
    store32(9687216, arg0)
    arg0 = func26(arg0)
    store32(9687212, func26(arg0))
    return arg0

# ------------------------------------------------------------
# $oe
# Export: oe
# ------------------------------------------------------------
def oe(arg0):
    """Exported as oe."""
    arg0 = func26(arg0)
    store32(9687232, func26(arg0))
    return arg0

# ------------------------------------------------------------
# $pe
# Export: pe
# ------------------------------------------------------------
def pe(arg0):
    """Exported as pe."""
    arg0 = func26(arg0)
    store32(9687236, func26(arg0))
    return arg0

# ------------------------------------------------------------
# $ab
# Export: ab
# ------------------------------------------------------------
def ab():
    """Exported as ab."""
    return load32(((load32((load32(9681476) + (load32(9681468) << 2))) * 404) + 9568096) + 152)

# ------------------------------------------------------------
# $ib
# Export: ib
# ------------------------------------------------------------
def ib(arg0):
    """Exported as ib."""
    store32(9681464, arg0)
    v1 = 9681776
    while True:  # block $label3
        while True:  # block $label0
            while True:  # block $label1
                while True:  # block $label2
                    # br_table[arg0]
                    break
                    break
                v1 = 9681792
                break
            store32(9681476, v1)
            store32(9681468, 0)
            break
            break
        store32(9681476, 9681696)
        store32(9681468, 0)
        break
    store32(100, load32(((load32(9681696) * 404) + 9568096) + 68))
    return 9681472

# ------------------------------------------------------------
# $jb
# Export: jb
# ------------------------------------------------------------
def jb(arg0):
    """Exported as jb."""
    v1 = load32(9681468)
    v3 = (load32(9681468) + arg0)
    v2 = load32(9681464)
    v4 = ((4 if (load32(9681464) == 1) else 3) if v2 else 18)
    arg0 = (((load32(9681468) + arg0) if v1 else (((4 if (load32(9681464) == 1) else 3) if v2 else 18) - 1)) if (arg0 == -1) else v3)
    v1 = ((((load32(9681468) + arg0) if v1 else (((4 if (load32(9681464) == 1) else 3) if v2 else 18) - 1)) if (arg0 == -1) else v3) if (arg0 < v4) else 0)
    store32(9681468, ((((load32(9681468) + arg0) if v1 else (((4 if (load32(9681464) == 1) else 3) if v2 else 18) - 1)) if (arg0 == -1) else v3) if (arg0 < v4) else 0))
    arg0 = 100
    if v2:
    else:
    store32(100, load32(((load32((load32(9681476) + (v1 << 2))) * 404) + 9568096) + 68))
    return 9681472

# ------------------------------------------------------------
# $nc
# Export: nc
# ------------------------------------------------------------
def nc():
    """Exported as nc."""
    v9 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    if load8u(9684336):
        a_b()
        store8(9684336, 0)
    while True:  # block $label0
        if load8u(9147152):
            func152()
            break
        if (load8u(9140304) | load8u(9140312)):
            break
        v1 = (load32(59160) + load32(40592))
        store32(59160, (load32(59160) + load32(40592)))
        v0 = load32(9682196)
        if load32(9682196):
            store32(59160, (v0 + v1))
            store32(9682196, 0)
        if (load32(51776) == 0):
            break
        if load8u(9215872):
            if load32(9215984):
                v1 = 0
                while True:  # $label1
                    v0 = load32(9215976)
                    v2 = (v1 << 2)
                    v1 = (v1 + 8)
                    if (u((v1 + 8)) < u(load32(9215984))):
                        continue
                    break
            v1 = 0
            store32(9215984, 0)
            if load32(9216000):
                while True:  # $label2
                    v0 = (load32(9215992) + (v1 << 2))
                    v1 = (v1 + 3)
                    if (u((v1 + 3)) < u(load32(9216000))):
                        continue
                    break
            v1 = 0
            store32(9216000, 0)
            if load32(9216016):
                while True:  # $label3
                    v0 = load32(9216008)
                    v2 = (v1 << 2)
                    qc(load32((load32(9216008) + (v1 << 2))), (load32((v0 + (v2 | 4))) != 0))
                    v1 = (v1 + 2)
                    if (u((v1 + 2)) < u(load32(9216016))):
                        continue
                    break
            v1 = 0
            store32(9216016, 0)
            if load32(9216032):
                while True:  # $label4
                    v0 = load32(9216024)
                    v2 = (v1 << 2)
                    v1 = (v1 + 4)
                    if (u((v1 + 4)) < u(load32(9216032))):
                        continue
                    break
            store32(9216032, 0)
            store8(9215872, 0)
        v1 = load32(9142848)
        while True:  # block $label5
            if (load8u(9147210) == 0):
                break
            if (v1 == 0):
                break
            if ((v1 * 25) % 250):
                break
            if (u(v1) <= u(load32(59148))):
                break
            if ((load8u(9142388) == 0) | (load8u(9147125) == 0)):
                if (u(load32(59176)) < u(v1)):
                    break
            v1 = (G.global0 - 80)
            G.global0 = (G.global0 - 80)
            while True:  # block $label6
                if (load32(9561792) == 0):
                    break
                while True:  # $label25
                    while True:  # block $label7
                        v0 = load32(9561784)
                        v2 = (v10 << 2)
                        v3 = (load32(9561784) + (v10 << 2))
                        v5 = load32((load32(9561784) + (v10 << 2)))
                        if (load32((load32(9561784) + (v10 << 2))) == 0):
                            break
                        if (load32(9142848) != load32((v0 + (v2 | 4)))):
                            break
                        v14 = load32((v0 + (v2 | 28)))
                        v15 = load32((v0 + (v2 | 24)))
                        v16 = load32((v0 + (v2 | 20)))
                        v6 = load32((v0 + (v2 | 16)))
                        v11 = load32((v0 + (v2 | 12)))
                        v12 = load32((v0 + (v2 | 8)))
                        store32(v3, 0)
                        while True:  # block $label17
                            while True:  # block $label12
                                while True:  # block $label19
                                    while True:  # block $label16
                                        while True:  # block $label8
                                            v2 = load32(9142892)
                                            v4 = (u(load32(9142892)) < u(2))
                                            if (u(load32(9142892)) < u(2)):
                                                break
                                            v3 = load32(9561692)
                                            v0 = 1
                                            while True:  # block $label11
                                                while True:  # $label10
                                                    while True:  # block $label9
                                                        if v12:
                                                            if (load32((v3 + (v0 * 286704)) + 283948) == v12):
                                                                break
                                                        if v6:
                                                            if (load32((v3 + (v0 * 286704)) + 283952) == v6):
                                                                break
                                                        v0 = (v0 + 1)
                                                        if ((v0 + 1) != v2):
                                                            continue
                                                        break
                                                        break
                                                    break
                                                v3 = load32((v3 + (v0 * 286704)) + 283908)
                                                if load32((v3 + (v0 * 286704)) + 283908):
                                                    break
                                                break
                                            if v4:
                                                break
                                            v3 = load32(9561692)
                                            v0 = 1
                                            while True:  # $label18
                                                while True:  # block $label14
                                                    while True:  # block $label13
                                                        v4 = (v3 + (v0 * 286704))
                                                        if (load32((v3 + (v0 * 286704)) + 283976) == 0):
                                                            if load8u(v4 + 286699):
                                                                break
                                                        if load32(v4 + 284616):
                                                            break
                                                        break
                                                    v3 = load32(v4 + 283908)
                                                    v0 = load32(v4 + 281800)
                                                    if load32(v4 + 281800):
                                                        store32((v4 + 281800), 0)
                                                        v2 = load32(9142892)
                                                    v0 = 1
                                                    if (u(v2) >= u(2)):
                                                        while True:  # $label15
                                                            if (v0 != v3):
                                                                func176(v3, v0, 1)
                                                                v2 = load32(9142892)
                                                            v0 = (v0 + 1)
                                                            if (u((v0 + 1)) < u(v2)):
                                                                continue
                                                            break
                                                    v0 = load32(9142384)
                                                    if (v3 == 0):
                                                        break
                                                    break
                                                    break
                                                v0 = (v0 + 1)
                                                if ((v0 + 1) != v2):
                                                    continue
                                                break
                                            break
                                        if (v5 == load32(9142384)):
                                            break
                                        break
                                        break
                                    if (v0 != v5):
                                        break
                                    break
                                break
                                break
                            break
                        v2 = (v5 == load32(9142384))
                        store32(v1 + 68, v5)
                        v0 = (load32(9561692) + (v3 * 286704))
                        store32(v1 + 64, (load32(9561692) + (v3 * 286704)))
                        store32(v1 + 52, v5)
                        store32(v1 + 48, (v0 + 80))
                        store32(v0 + 283952, v6)
                        store32(v0 + 283948, v12)
                        store32(v0 + 284616, v5)
                        store32(v0 + 283964, v15)
                        store8(v0 + 92, v16)
                        store8(v0 + 286699, 0)
                        store8(v0 + 93, v14)
                        store8((v0 + 283974), v11)
                        store8((v0 + 283973), ((v11 & 0xFFFFFFFF) >> 8))
                        store8(v0 + 283972, ((v11 & 0xFFFFFFFF) >> 16))
                        if v2:
                            store32(9142872, load32(v0 + 283908))
                            v4 = load32(9142892)
                            if (u(load32(9142892)) >= u(2)):
                                v6 = load32(9561692)
                                v2 = 1
                                while True:  # $label20
                                    v3 = (v6 + (v2 * 286704))
                                    v11 = load32((v6 + (v2 * 286704)) + 284616)
                                    if load32((v6 + (v2 * 286704)) + 284616):
                                        v4 = load8u(v3 + 92)
                                        v6 = load32(v3 + 283948)
                                        v12 = load8u(v3 + 283972)
                                        v14 = load8u((v3 + 283974))
                                        v15 = load8u((v3 + 283973))
                                        v16 = load32(v3 + 283964)
                                        v17 = load8u(v3 + 93)
                                        store32(v1 + 40, (v3 + 80))
                                        store32(v1 + 36, v17)
                                        store32(v1 + 32, v16)
                                        store32(v1 + 44, ((v14 | (v15 << 8)) | (v12 << 16)))
                                        store32(v1 + 28, v6)
                                        store32(v1 + 24, v4)
                                        store32(v1 + 20, v3)
                                        store32(v1 + 16, v11)
                                        v6 = load32(9561692)
                                        v4 = load32(9142892)
                                    v2 = (v2 + 1)
                                    if (u((v2 + 1)) < u(v4)):
                                        continue
                                    break
                            func346()
                            if (load32(v0 + 283976) == 0):
                                break
                            while True:  # block $label21
                                v0 = load32(((v0 + (load32(9671152) << 2)) + 284636))
                                if (load32(((v0 + (load32(9671152) << 2)) + 284636)) == 0):
                                    break
                                v2 = load32(v0 + 8)
                                if (load32(v0 + 8) == 0):
                                    break
                                v3 = load32(v0)
                                v0 = 0
                                while True:  # $label22
                                    v4 = load32((v3 + (v0 << 2)))
                                    if (load32((v3 + (v0 << 2))) == 0):
                                        v0 = (v0 + 1)
                                        if (v2 != (v0 + 1)):
                                            continue
                                        break
                                    break
                                if load8u(9142917):
                                    break
                                v0 = load32(9671128)
                                v0 = (v0 + (v4 * 132))
                                v2 = load32((v0 + (v4 * 132)) + 36)
                                v0 = (load32(9671128) + ((load32((v0 + (v4 * 132)) + 36) if v2 else load32(v0 + 28)) * 132))
                                v2 = ((load8u((load32(9671128) + ((load32((v0 + (v4 * 132)) + 36) if v2 else load32(v0 + 28)) * 132)) + 122) * 404) + 9568096)
                                v3 = load32(((load8u((load32(9671128) + ((load32((v0 + (v4 * 132)) + 36) if v2 else load32(v0 + 28)) * 132)) + 122) * 404) + 9568096) + 220)
                                v4 = load16u(v0 + 114)
                                store32(v1, (((load32(v2 + 216) << 4) & 2147483632) + (load16u(v0 + 112) << 5)))
                                store32(v1 + 4, (((v3 << 4) & 2147483632) + (v4 << 5)))
                                break
                            if (load32(load32(9142424) + 48) == 0):
                                break
                            if load8u(9147152):
                                break
                            v4 = load32(9671136)
                            if (u(load32(9671136)) < u(4)):
                                break
                            v6 = load32(9671128)
                            v2 = 3
                            while True:  # $label24
                                while True:  # block $label23
                                    v0 = (v6 + (v2 * 132))
                                    if (load8u((v6 + (v2 * 132)) + 125) == 3):
                                        break
                                    if (load32(v0 + 28) == 0):
                                        break
                                    if load32(v0 + 36):
                                        break
                                    v4 = load32(9671136)
                                    v6 = load32(9671128)
                                    break
                                v2 = (v2 + 1)
                                if (u((v2 + 1)) < u(v4)):
                                    continue
                                break
                            break
                        break
                    v13 = (v13 + (v5 != 0))
                    v10 = (v10 + 8)
                    if (u((v10 + 8)) < u(load32(9561792))):
                        continue
                    break
                if v13:
                    break
                store32(9561792, 0)
                break
            G.global0 = (v1 + 80)
            while True:  # block $label26
                if load8u(9147125):
                    break
                if (load32(9561776) == 0):
                    break
                v1 = load32(9561768)
                while True:  # $label29
                    v3 = (v8 << 2)
                    v5 = load32((v1 + (v8 << 2)))
                    v4 = (load32((v1 + (v8 << 2))) != 0)
                    while True:  # block $label27
                        if (v5 == 0):
                            break
                        if (load32((v1 + (v3 | 4))) != load32(9142848)):
                            break
                        v6 = load32(9142892)
                        if (u(load32(9142892)) < u(2)):
                            break
                        v10 = load32(9561692)
                        v2 = 1
                        while True:  # $label28
                            v0 = (v10 + (v2 * 286704))
                            if (v5 == load32((v10 + (v2 * 286704)) + 284616)):
                                store32((v1 + v3), 0)
                                if load32(9147132):
                                    store8(v0 + 286699, 1)
                                    break
                                v1 = (v0 + 284616)
                                store32(v0 + 284628, load32((v0 + 284616)))
                                store32(v1, 0)
                                v1 = load32(9561768)
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v6):
                                continue
                            break
                        break
                    v7 = (v4 + v7)
                    v8 = (v8 + 2)
                    if (u((v8 + 2)) < u(load32(9561776))):
                        continue
                    break
                if v7:
                    break
                store32(9561776, 0)
                break
            v1 = load32(59172)
            v0 = (load32(9561696) + (load32(59172) << 2))
            v3 = load32((load32(9561696) + (load32(59172) << 2)) + 8)
            if (u(load32((load32(9561696) + (load32(59172) << 2)) + 8)) >= u(4)):
                v1 = 3
                while True:  # $label31
                    v2 = (v0 + (v1 << 2))
                    store32(59164, load32((v0 + (v1 << 2))))
                    v7 = load32(v2 + 8)
                    v5 = (v1 + 4)
                    v8 = (load32(v2 + 8) + (v1 + 4))
                    v4 = load32(v2 + 12)
                    v1 = ((load32(v2 + 8) + (v1 + 4)) + load32(v2 + 12))
                    while True:  # block $label30
                        v2 = load32(v2 + 4)
                        if (u(load32(v2 + 4)) > u(255)):
                            break
                        v2 = ((v2 << 3) + 9213824)
                        v6 = load32(((v2 << 3) + 9213824))
                        if (load32(((v2 << 3) + 9213824)) == 0):
                            break
                        v8 = ((v0 + (v8 << 2)) if v4 else 0)
                        v5 = ((v0 + (v5 << 2)) if v7 else 0)
                        v4 = load32(v2 + 4)
                        if load32(v2 + 4):
                            # call_indirect[v4]
                            if (indirect_call(v4) == 0):
                                break
                        else:
                        # call_indirect[v6]
                        break
                    store32(59164, 0)
                    if (u(v1) < u(v3)):
                        continue
                    break
            else:
            store32(load32(59172), (v1 + v3))
            v1 = load32(9142848)
            break
        while True:  # block $label32
            if (load32(9147132) == 0):
                break
            if load8u(9684337):
                break
            if (u(v1) < u(11)):
                break
            if (u(load32(59160)) > u((v1 + 1))):
                break
            a_b()
            store8(9684337, 1)
            if load32((load32(9561692) + (load32(9142872) * 286704)) + 283976):
                break
            Za()
            break
        if (load32(51776) == 2):
            store32(51776, 0)
            func231(v9)
            store32(v9 + 12, 1)
            func186((v9 + 44), v9, 66, 0)
            break
        store32(51776, 0)
        while True:  # block $label38
            if (load32(9684288) == 0):
                v8 = 0
                v7 = -1
                v0 = (G.global0 - 16)
                G.global0 = (G.global0 - 16)
                store32(v0 + 12, 0)
                func175(9684320)
                v1 = load32(9684308)
                v2 = (load32(9684308) != 0)
                while True:  # block $label33
                    if (v1 == 0):
                        break
                    while True:  # $label35
                        while True:  # block $label34
                            # TODO: i32.atomic.rmw.cmpxchg []
                            if 1:
                                store32(v0 + 12, (load32(v0 + 12) + 1))
                                store32(v1 + 16, (v0 + 12))
                                break
                            v8 = (v8 if v8 else v1)
                            v7 = (v7 - 1)
                            break
                        v1 = load32(v1)
                        v2 = (load32(v1) != 0)
                        if (v7 == 0):
                            break
                        if v1:
                            continue
                        break
                    break
                while True:  # block $label36
                    if v2:
                        v7 = (v1 + 4)
                        v2 = load32(v1 + 4)
                        if (load32(v1 + 4) == 0):
                            break
                        store32(v2, 0)
                        break
                    v7 = 9684292
                    break
                store32(v7, 0)
                store32(9684308, v1)
                func154(9684320)
                v1 = load32(v0 + 12)
                if load32(v0 + 12):
                    while True:  # $label37
                        v1 = load32(v0 + 12)
                        if load32(v0 + 12):
                            continue
                        break
                if v8:
                    func154((v8 + 12))
                G.global0 = (v0 + 16)
                break
            if load32(9684300):
                # TODO: i32.atomic.rmw.add []
                func111(9684296, 2147483647)
            break
        func54(9684264)
        break
    G.global0 = (v9 + 48)
    return 9684296