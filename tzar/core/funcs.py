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
# $func30
# ------------------------------------------------------------
def func30(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, param9):
    v22 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v22 + 24, arg3)
    store32(v22 + 28, arg1)
    store32(v22 + 20, arg4)
    arg3 = 0
    while True:  # block $label0
        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
            break
        arg1 = load8u(arg0 + 125)
        if ((load8u(arg0 + 125) & -2) == 12):
            break
        if (arg1 == 3):
            break
        arg1 = load32(((arg2 * 40) + 9671200) + 24)
        if load32(((arg2 * 40) + 9671200) + 24):
            # call_indirect[arg1]
            if indirect_call(arg1):
                break
        if load32(arg0 + 36):
            if load32(arg0 + 36):
                break
        v14 = arg0
        arg0 = load32(v22 + 28)
        arg1 = 0
        v12 = (G.global0 - 32)
        G.global0 = (G.global0 - 32)
        while True:  # block $label1
            if (arg0 == 0):
                break
            v30 = load32(9561692)
            v27 = load16u(v14 + 110)
            v11 = (load32(9561692) + (load16u(v14 + 110) * 286704))
            if (load32((load32(9561692) + (load16u(v14 + 110) * 286704)) + 286684) == 0):
                break
            arg4 = load32(9671128)
            v28 = (load32(9671128) + (arg0 * 132))
            v9 = load8u((load32(9671128) + (arg0 * 132)) + 122)
            v13 = load32(((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096) + 264)
            if (load32(((load8u((load32(9671128) + (arg0 * 132)) + 122) * 404) + 9568096) + 264) == 4):
                break
            v20 = load8u(v14 + 122)
            v10 = load32(((load8u(v14 + 122) * 404) + 9568096) + 264)
            if (load32(((load8u(v14 + 122) * 404) + 9568096) + 264) == 4):
                break
            v18 = load16u(v14 + 112)
            store32(v12 + 12, load16u(v14 + 112))
            v21 = load16u(v14 + 114)
            store32(v12 + 8, load16u(v14 + 114))
            while True:  # block $label2
                if v10:
                    arg1 = ((v20 * 404) + 9568096)
                    v15 = load32(((v20 * 404) + 9568096) + 216)
                    if (load32(((v20 * 404) + 9568096) + 216) == 0):
                        v10 = 0
                        break
                    v10 = 0
                    v16 = load32(arg1 + 220)
                    if (load32(arg1 + 220) == 0):
                        break
                    arg1 = load32(9215880)
                    if (load32(9215880) == 0):
                        break
                    v19 = load32(9142432)
                    if (load32(9142432) == 0):
                        break
                    v24 = load32(9142440)
                    v17 = load32(arg1)
                    v20 = 0
                    while True:  # $label4
                        v23 = (v18 + v20)
                        arg1 = 0
                        while True:  # $label3
                            v10 = load32((v19 + ((v23 + ((arg1 + v21) * v24)) << 2)))
                            if (load32((v17 + (load32((v19 + ((v23 + ((arg1 + v21) * v24)) << 2))) << 2))) == 0):
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
                if (load32(9142432) == 0):
                    break
                v10 = load32((arg1 + (((load32(9142440) * v21) + v18) << 2)))
                break
            while True:  # block $label7
                while True:  # block $label5
                    while True:  # block $label6
                        # br_table[v13]
                        break
                        break
                    arg1 = ((v9 * 404) + 9568096)
                    v13 = load32(((v9 * 404) + 9568096) + 216)
                    if (load32(((v9 * 404) + 9568096) + 216) == 0):
                        v20 = 0
                        break
                    v20 = 0
                    v15 = load32(arg1 + 220)
                    if (load32(arg1 + 220) == 0):
                        break
                    arg1 = load32(9215880)
                    if (load32(9215880) == 0):
                        break
                    v16 = load32(9142432)
                    if (load32(9142432) == 0):
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
                            if (load32((v24 + (load32((v16 + ((v17 + ((arg1 + arg4) * v19)) << 2))) << 2))) == 0):
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
                if (load32(9142432) == 0):
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
            if (load32(9684440) == 0):
                break
            v32 = load32(((load32((v30 + (v27 * 286704)) + 283960) << 2) + 58928))
            v9 = load32(9684436)
            while True:  # $label12
                while True:  # block $label11
                    arg1 = (arg0 * arg4)
                    while True:  # block $label10
                        if (arg4 != v10):
                            if (load8u((v9 + (arg1 + v10))) == 0):
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
            if (arg4 == 0):
                break
            arg0 = (v30 + (v27 * 286704))
            store32((v30 + (v27 * 286704)) + 283940, (load32(arg0 + 283940) + 1))
            while True:  # block $label50
                while True:  # block $label13
                    v24 = ((v32 * 404) + 9568096)
                    arg0 = load32(((v32 * 404) + 9568096) + 68)
                    if load32(((v32 * 404) + 9568096) + 68):
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
                    v19 = load32(9671128)
                    while True:  # block $label16
                        v23 = load32(9142432)
                        if load32(9142432):
                            v25 = load32(9142440)
                            v13 = 1
                            while True:  # $label20
                                while True:  # block $label14
                                    arg1 = load32(((v9 << 2) + 58928))
                                    arg0 = load32(((v11 + (load32(((v9 << 2) + 58928)) << 2)) + 284636))
                                    if (load32(((v11 + (load32(((v9 << 2) + 58928)) << 2)) + 284636)) == 0):
                                        break
                                    v26 = load32(arg0 + 8)
                                    if (load32(arg0 + 8) == 0):
                                        break
                                    v17 = ((arg1 * 404) + 9568096)
                                    v29 = load32(arg0)
                                    v16 = 0
                                    while True:  # $label19
                                        while True:  # block $label15
                                            arg0 = load32((v29 + (v16 << 2)))
                                            if (load32((v29 + (v16 << 2))) == 0):
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
                                v13 = (u((v9 + 1)) < u(3))
                                if (v9 != 3):
                                    continue
                                break
                            break
                        if arg4:
                            break
                        v13 = 1
                        while True:  # $label24
                            while True:  # block $label21
                                arg1 = load32(((v9 << 2) + 58928))
                                arg0 = load32(((v11 + (load32(((v9 << 2) + 58928)) << 2)) + 284636))
                                if (load32(((v11 + (load32(((v9 << 2) + 58928)) << 2)) + 284636)) == 0):
                                    break
                                v15 = load32(arg0 + 8)
                                if (load32(arg0 + 8) == 0):
                                    break
                                arg1 = ((arg1 * 404) + 9568096)
                                v16 = load32(arg0)
                                arg0 = 0
                                while True:  # $label23
                                    while True:  # block $label22
                                        v17 = load32((v16 + (arg0 << 2)))
                                        if (load32((v16 + (arg0 << 2))) == 0):
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
                            v13 = (u((v9 + 1)) < u(3))
                            if (v9 != 3):
                                continue
                            break
                        break
                    if v13:
                        break
                    store32(v12 + 16, v18)
                    store32(v12 + 4, v21)
                    while True:  # block $label25
                        v18 = load32(9142440)
                        if (u(load32(9142440)) < u(2)):
                            break
                        v17 = load32(v12 + 16)
                        v13 = (load32(v12 + 16) - 1)
                        v15 = load32(v12 + 4)
                        arg1 = (load32(v12 + 4) - 1)
                        v21 = (v17 + 2)
                        v16 = (v15 + 2)
                        v19 = 1
                        while True:  # $label39
                            while True:  # block $label26
                                if (v13 >= v21):
                                    break
                                if (arg1 >= v16):
                                    break
                                v25 = (v21 - 1)
                                v26 = (v16 - 1)
                                v23 = 1
                                v9 = v13
                                while True:  # block $label30
                                    v29 = load32(9142432)
                                    if (load32(9142432) == 0):
                                        while True:  # $label34
                                            while True:  # block $label27
                                                if (u(v9) >= u(v18)):
                                                    break
                                                while True:  # block $label28
                                                    if (v9 == v25):
                                                        break
                                                    arg0 = arg1
                                                    if (v9 == v13):
                                                        break
                                                    while True:  # $label31
                                                        while True:  # block $label29
                                                            if ((arg0 != arg1) & (arg0 != v26)):
                                                                break
                                                            if (u(arg0) >= u(v18)):
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
                                                    while True:  # block $label32
                                                        if (u(arg0) >= u(v18)):
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
                                        raise RuntimeError('unreachable')
                                    while True:  # $label38
                                        arg0 = arg1
                                        if (u(v9) < u(v18)):
                                            while True:  # $label37
                                                while True:  # block $label36
                                                    while True:  # block $label35
                                                        if (v9 == v13):
                                                            break
                                                        if (arg0 == arg1):
                                                            break
                                                        if (arg0 == v26):
                                                            break
                                                        if (v9 != v25):
                                                            break
                                                        break
                                                    if (u(arg0) >= u(v18)):
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
                            if (u(v18) > u(v19)):
                                continue
                            break
                        break
                    v18 = load32(v12 + 16)
                    v21 = load32(v12 + 4)
                    v13 = 0
                    v15 = 0
                    v16 = load32(9671128)
                    while True:  # block $label44
                        v17 = load32(9142432)
                        if load32(9142432):
                            v23 = load32(9142440)
                            arg0 = 2147483647
                            while True:  # $label43
                                while True:  # block $label40
                                    arg1 = load32(((v11 + (load32(((v13 << 2) + 58896)) << 2)) + 284636))
                                    if (load32(((v11 + (load32(((v13 << 2) + 58896)) << 2)) + 284636)) == 0):
                                        break
                                    v25 = load32(arg1 + 8)
                                    if (load32(arg1 + 8) == 0):
                                        break
                                    v26 = load32(arg1)
                                    v9 = 0
                                    while True:  # $label42
                                        while True:  # block $label41
                                            arg1 = load32((v26 + (v9 << 2)))
                                            if (load32((v26 + (v9 << 2))) == 0):
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
                            while True:  # block $label45
                                arg1 = load32(((v11 + (load32(((v13 << 2) + 58896)) << 2)) + 284636))
                                if (load32(((v11 + (load32(((v13 << 2) + 58896)) << 2)) + 284636)) == 0):
                                    break
                                v19 = load32(arg1 + 8)
                                if (load32(arg1 + 8) == 0):
                                    break
                                v17 = load32(arg1)
                                v9 = 0
                                while True:  # $label47
                                    while True:  # block $label46
                                        arg1 = load32((v17 + (v9 << 2)))
                                        if (load32((v17 + (v9 << 2))) == 0):
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
                    if (v15 == 0):
                        break
                    v10 = load32(9142440)
                    arg0 = 0
                    while True:  # $label51
                        while True:  # block $label49
                            arg1 = arg0
                            v11 = (arg0 << 2)
                            arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v21)
                            if (u(v10) <= u((load32((((arg0 << 2) | 4) + 8611904)) + v21))):
                                break
                            v11 = (load32((v11 + 8611904)) + v18)
                            if (u(v10) <= u((load32((v11 + 8611904)) + v18))):
                                break
                            if ((arg0 | v11) < 0):
                                break
                            if func56(v11, arg0, v24, load16u(v14 + 110), 0, 0, 1, 1, 0):
                                break
                            v10 = load32(9142440)
                            break
                        arg0 = (arg1 + 2)
                        if (u(arg1) < u(718)):
                            continue
                        break
                    break
                v30 = (v30 + (v27 * 286704))
                v18 = 0
                while True:  # $label76
                    while True:  # block $label52
                        arg0 = load32(((v30 + (load32(((v18 << 2) + 58940)) << 2)) + 284636))
                        if (load32(((v30 + (load32(((v18 << 2) + 58940)) << 2)) + 284636)) == 0):
                            break
                        v16 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        arg1 = 0
                        v27 = load32(39216)
                        v17 = load32(9561692)
                        v19 = load32(9215880)
                        v21 = load32(9142440)
                        v11 = load32(9142432)
                        v23 = load32(9671128)
                        v32 = load32(arg0)
                        v24 = 1
                        while True:  # block $label61
                            while True:  # $label62
                                while True:  # block $label60
                                    while True:  # block $label53
                                        arg0 = load32((v32 + (arg1 << 2)))
                                        if (load32((v32 + (arg1 << 2))) == 0):
                                            break
                                        while True:  # block $label56
                                            while True:  # block $label54
                                                while True:  # block $label55
                                                    v13 = (v23 + (arg0 * 132))
                                                    v10 = ((load8u((v23 + (arg0 * 132)) + 122) * 404) + 9568096)
                                                    # br_table[load32(((load8u((v23 + (arg0 * 132)) + 122) * 404) + 9568096) + 264)]
                                                    break
                                                    break
                                                arg0 = 0
                                                v25 = load32(v10 + 216)
                                                if (load32(v10 + 216) == 0):
                                                    break
                                                v26 = load32(v10 + 220)
                                                if (load32(v10 + 220) == 0):
                                                    break
                                                if (v19 == 0):
                                                    break
                                                if (v11 == 0):
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
                                                        if (load32((v33 + (load32((v11 + ((v34 + ((v9 + v29) * v21)) << 2))) << 2))) == 0):
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
                                            if (v11 == 0):
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
                                        # TODO: i32.div_u []
                                        if (u((load32(v10 + 136) * 150)) >= u((100 if (load32((((v17 + (load16u(v13 + 110) * 286704)) + (v27 << 2)) + 281808)) == 1) else arg0))):
                                            break
                                        while True:  # block $label59
                                            # br_table[load8u(v13 + 129)]
                                            break
                                            break
                                        arg0 = load32(v13 + 88)
                                        if (load32(v13 + 88) == 0):
                                            break
                                        if v11:
                                        else:
                                        if (0 == v20):
                                            break
                                        break
                                    arg1 = (arg1 + 1)
                                    v24 = (u((arg1 + 1)) < u(v16))
                                    if (arg1 != v16):
                                        continue
                                    break
                                    break
                                break
                            arg0 = 0
                            arg1 = 0
                            v15 = 0
                            while True:  # block $label72
                                while True:  # block $label66
                                    while True:  # block $label65
                                        while True:  # block $label63
                                            while True:  # block $label64
                                                v11 = load8u(v28 + 122)
                                                v9 = ((load8u(v28 + 122) * 404) + 9568096)
                                                # br_table[load32(((load8u(v28 + 122) * 404) + 9568096) + 264)]
                                                break
                                                break
                                            v19 = load32(v9 + 216)
                                            if (load32(v9 + 216) == 0):
                                                break
                                            v16 = load32(9142432)
                                            v27 = load32(((v11 * 404) + 9568096) + 220)
                                            if (load32(((v11 * 404) + 9568096) + 220) == 0):
                                                break
                                            arg0 = load16u(v28 + 114)
                                            arg1 = load16u(v28 + 112)
                                            if (v16 == 0):
                                                break
                                            v17 = load32(9142440)
                                            v23 = load32(load32(9215880))
                                            while True:  # $label69
                                                v11 = (arg1 + v15)
                                                v10 = 0
                                                while True:  # block $label68
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
                                        while True:  # block $label70
                                            v11 = (arg1 - v15)
                                            if ((arg1 - v15) == 0):
                                                break
                                            if (arg0 == v9):
                                                break
                                            v11 = (v10 // v11)
                                            v11 = (v11 >> 31)
                                            v11 = (v11 if (u((((v10 // v11) ^ (v11 >> 31)) - v11)) <= u(1)) else 0)
                                            v9 = ((v11 if (u((((v10 // v11) ^ (v11 >> 31)) - v11)) <= u(1)) else 0) // v10)
                                            v9 = (v9 >> 31)
                                            v10 = (v10 if (u(((((v11 if (u((((v10 // v11) ^ (v11 >> 31)) - v11)) <= u(1)) else 0) // v10) ^ (v9 >> 31)) - v9)) <= u(1)) else 0)
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
                                        while True:  # block $label73
                                            arg2 = load32(v12 + 12)
                                            v11 = (arg1 - load32(v12 + 12))
                                            if ((arg1 - load32(v12 + 12)) == 0):
                                                break
                                            if (arg0 == v9):
                                                break
                                            arg3 = (v10 // v11)
                                            arg3 = (arg3 >> 31)
                                            v11 = (v11 if (u((((v10 // v11) ^ (arg3 >> 31)) - arg3)) <= u(1)) else 0)
                                            arg3 = ((v11 if (u((((v10 // v11) ^ (arg3 >> 31)) - arg3)) <= u(1)) else 0) // v10)
                                            arg3 = (arg3 >> 31)
                                            v10 = (v10 if (u(((((v11 if (u((((v10 // v11) ^ (arg3 >> 31)) - arg3)) <= u(1)) else 0) // v10) ^ (arg3 >> 31)) - arg3)) <= u(1)) else 0)
                                            break
                                        store32(v12 + 12, ((-1 if (v11 < 0) else (v11 != 0)) + arg2))
                                        v9 = (load32(v12 + 8) + (-1 if (v10 < 0) else (v10 != 0)))
                                        store32(v12 + 8, (load32(v12 + 8) + (-1 if (v10 < 0) else (v10 != 0))))
                                        continue
                                        break
                                    raise RuntimeError('unreachable')
                                v9 = load32(v12 + 8)
                                v10 = (arg0 - load32(v12 + 8))
                                while True:  # block $label75
                                    arg1 = load32(v12 + 12)
                                    v11 = (arg1 - load32(v12 + 12))
                                    if ((arg1 - load32(v12 + 12)) == 0):
                                        break
                                    if (arg0 == v9):
                                        break
                                    arg0 = (v10 // v11)
                                    arg0 = (arg0 >> 31)
                                    v11 = (v11 if (u((((v10 // v11) ^ (arg0 >> 31)) - arg0)) <= u(1)) else 0)
                                    arg0 = ((v11 if (u((((v10 // v11) ^ (arg0 >> 31)) - arg0)) <= u(1)) else 0) // v10)
                                    arg0 = (arg0 >> 31)
                                    v10 = (v10 if (u(((((v11 if (u((((v10 // v11) ^ (arg0 >> 31)) - arg0)) <= u(1)) else 0) // v10) ^ (arg0 >> 31)) - arg0)) <= u(1)) else 0)
                                    break
                                store32(v12 + 12, ((-1 if (v11 < 0) else (v11 != 0)) + arg1))
                                store32(v12 + 8, (load32(v12 + 8) + (-1 if (v10 < 0) else (v10 != 0))))
                                break
                            store32(v13 + 88, (load32(v12 + 12) + (v21 * load32(v12 + 8))))
                            break
                        store32(v13 + 80, (v25 + 1))
                        if (v24 == 0):
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
            func261(v32, v11, arg0, ((v9 * 132) + load32(9671128)))
            if load32(load32(9142424) + 156):
                func29((load32(9671128) + arg0), 1)
            arg1 = 1
            break
        G.global0 = (v12 + 32)
        while True:  # block $label77
            while True:  # block $label78
                # br_table[arg1]
                break
                break
            if (load32(v14 + 44) == 0):
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
            # call_indirect[arg0]
        while True:  # block $label79
            if (arg2 != 6):
                break
            if (arg8 == 0):
                break
            v11 = load32(9215884)
            v9 = load32(v14 + 44)
            if (load32((load32(9215884) + (load32(v14 + 44) << 4)) + 4) != 6):
                break
            arg4 = load32(v14 + 28)
            arg1 = 0
            while True:  # block $label80
                v20 = load32(9671128)
                v10 = load32(v22 + 28)
                arg0 = (load32(9671128) + (load32(v22 + 28) * 132))
                arg3 = load32(((load8u((load32(9671128) + (load32(v22 + 28) * 132)) + 122) * 404) + 9568096) + 216)
                if (load32(((load8u((load32(9671128) + (load32(v22 + 28) * 132)) + 122) * 404) + 9568096) + 216) == 0):
                    break
                v13 = load16u(arg0 + 114)
                arg1 = (v20 + (arg4 * 132))
                v20 = load16u((v20 + (arg4 * 132)) + 114)
                v15 = load16u(arg0 + 112)
                v28 = load16u(arg1 + 112)
                arg0 = load32(((load8u(arg1 + 122) * 404) + 9568096) + 224)
                v12 = (load32(((load8u(arg1 + 122) * 404) + 9568096) + 224) * arg0)
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
                    arg1 = (u((arg0 + 1)) < u(arg3))
                    if (arg0 != arg3):
                        continue
                    break
                break
            if (arg1 == 0):
                break
            if (arg6 != -1):
                store8(v14 + 129, arg6)
            store32((v11 + ((v9 << 4) | 12)), v10)
            arg3 = 0
            break
            break
        while True:  # block $label83
            if (load8u(v14 + 127) != 1):
                break
            store8(v14 + 127, 0)
            arg0 = load32(v14 + 40)
            if (load32(v14 + 40) == 0):
                break
            if (load8u(9142916) == 0):
                break
            store32(v22 + 4, arg0)
            store32(v22, 0)
            a_b()
            break
        while True:  # block $label84
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
        while True:  # block $label85
            arg0 = load32(v22 + 28)
            if (u(load32(v22 + 28)) >= u(3)):
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
        while True:  # block $label86
            if (arg8 == 0):
                break
            if (load32((load32(9215884) + (load32(v14 + 44) << 4)) + 4) != 6):
                break
            arg0 = load8u(v14 + 129)
            if (load8u(v14 + 129) == 5):
                break
            if ((arg1 | (arg0 != 9)) == 0):
                break
            break
        store8(v14 + 125, 1)
        func63(v22, v14, 0, 1, arg7)
        break
    G.global0 = (v22 + 32)
    return arg3

# ------------------------------------------------------------
# $func32
# ------------------------------------------------------------
def func32(arg0, arg1, param2):
    v13 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if (load8u(arg0 + 125) == 3):
            break
        v10 = load8u(arg0 + 122)
        v14 = ((load8u(arg0 + 122) * 404) + 9568096)
        v8 = load16u(arg0 + 110)
        v9 = load32(9561692)
        v4 = load32(((v10 * 72) + 9263856) + 28)
        while True:  # block $label1
            if arg1:
                break
            v5 = load8u(9147152)
            if load8u(9147152):
                break
            if (load8u(9147211) == 0):
                break
            v6 = ((v10 * 404) + 9568096)
            v7 = load32(((v10 * 404) + 9568096) + 40)
            if (load32(((v10 * 404) + 9568096) + 40) == 0):
                break
            v2 = load16u(arg0 + 112)
            v3 = ((load16u(arg0 + 112) << 5) - load32(9142952))
            v3 = load16u(arg0 + 114)
            v11 = ((load16u(arg0 + 114) << 5) - load32(9142956))
            if ((((((load16u(arg0 + 112) << 5) - load32(9142952)) * v3) + (((load16u(arg0 + 114) << 5) - load32(9142956)) * v11)) - 1) > 9000000):
                break
            v6 = load32(v6 + 36)
            while True:  # block $label2
                v11 = load32(load32(9142424) + 48)
                if (load32(load32(9142424) + 48) == 0):
                    break
                if v5:
                    break
                v5 = load16u((load32(9147376) + (((load32(9142440) * v3) + v2) << 1)))
                if (v11 == 2):
                    if (u(v5) > u(1)):
                        break
                    break
                if (v5 == 0):
                    break
                break
            store32(v13, load32((v6 + (((load32(9142848) + v2) % v7) << 2))))
            store32(v13 + 4, v2)
            store32(v13 + 8, v3)
            a_b()
            break
        v15 = load8u(arg0 + 124)
        while True:  # block $label3
            if (load32(v14 + 264) != 1):
                break
            v2 = ((v10 * 404) + 9568096)
            v3 = load32(((v10 * 404) + 9568096) + 360)
            if load32(((v10 * 404) + 9568096) + 360):
                v4 = load32(v3)
                break
            while True:  # block $label10
                while True:  # block $label9
                    while True:  # block $label8
                        while True:  # block $label7
                            while True:  # block $label6
                                while True:  # block $label5
                                    while True:  # block $label4
                                        v3 = load32(v2 + 216)
                                        v2 = load32(v2 + 220)
                                        v2 = (load32(v2 + 216) if (u(v2) < u(v3)) else load32(v2 + 220))
                                        # br_table[((6 if (u(v2) >= u(6)) else (load32(v2 + 216) if (u(v2) < u(v3)) else load32(v2 + 220))) - 1)]
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
            v4 = (load32(9142632) if (u(v2) > u(5)) else v4)
            store8(arg0 + 124, 0)
            break
        if load8u(9147152):
            func77(arg0)
            store32(arg0 + 28, 0)
        while True:  # block $label11
            if (load8u(9147213) == 0):
                break
            while True:  # block $label12
                if (arg1 == 0):
                    if (load8u(9147152) == 0):
                        break
                v2 = load32(arg0 + 40)
                if (load32(arg0 + 40) == 0):
                    break
                func38(v2)
                break
                break
            if (load32(38448) == load8u(arg0 + 122)):
                store8(arg0 + 124, (load32(arg0 + 28) % 3))
                break
            if v4:
                store8(arg0 + 124, 0)
                func92(arg0, 0.0, 0.0)
                if (load32(v4 + 24) == 0):
                    break
                v2 = load32(arg0 + 40)
                if (load32(arg0 + 40) == 0):
                    break
                func254(v4, v2)
                break
            v2 = load32(arg0 + 40)
            if (load32(arg0 + 40) == 0):
                break
            func38(v2)
            break
        v11 = load32(arg0 + 36)
        if load32(arg0 + 36):
        v2 = load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
        if load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
            # call_indirect[v2]
        if load32(9147132):
            v6 = load32(arg0 + 28)
            v7 = load32(9671128)
            while True:  # block $label32
                while True:  # block $label14
                    while True:  # block $label13
                        v3 = load32(9215904)
                        if (load32(9215904) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label15
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # block $label16
                        v3 = load32(9215908)
                        if (load32(9215908) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label17
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # block $label18
                        v3 = load32(9215912)
                        if (load32(9215912) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label19
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # block $label20
                        v3 = load32(9215916)
                        if (load32(9215916) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label21
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # block $label22
                        v3 = load32(9215920)
                        if (load32(9215920) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label23
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # block $label24
                        v3 = load32(9215924)
                        if (load32(9215924) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label25
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # block $label26
                        v3 = load32(9215928)
                        if (load32(9215928) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label27
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # block $label28
                        v3 = load32(9215932)
                        if (load32(9215932) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label29
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    while True:  # block $label30
                        v3 = load32(9215936)
                        if (load32(9215936) == 0):
                            break
                        v5 = load32(v3 + 8)
                        if (load32(v3 + 8) == 0):
                            break
                        v4 = load32(v3)
                        v2 = 0
                        while True:  # $label31
                            if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) != v5):
                                continue
                            break
                        break
                    v3 = load32(9215940)
                    if (load32(9215940) == 0):
                        break
                    v5 = load32(v3 + 8)
                    if (load32(v3 + 8) == 0):
                        break
                    v4 = load32(v3)
                    v2 = 0
                    while True:  # $label33
                        if (load32((v7 + (load32((v4 + (v2 << 2))) * 132)) + 28) == v6):
                            break
                        v2 = (v2 + 1)
                        if ((v2 + 1) != v5):
                            continue
                        break
                    break
                    break
                v5 = (v5 - 1)
                store32(v3 + 8, (v5 - 1))
                if (u(v2) >= u(v5)):
                    break
                while True:  # $label34
                    v2 = (v2 + 1)
                    store32((v4 + (v2 << 2)), load32((v4 + ((v2 + 1) << 2))))
                    if (u(v2) < u(load32(v3 + 8))):
                        continue
                    break
                break
        while True:  # block $label35
            if (load8u(9147213) == 0):
                break
            if (load32(arg0 + 40) == 0):
                break
            v3 = load32(arg0 + 12)
            if (load32(arg0 + 12) == 0):
                break
            if load32(v3 + 8):
                v4 = 0
                while True:  # $label36
                    func38(load32((load32(v3) + (v4 << 2))))
                    v4 = (v4 + 2)
                    v3 = load32(arg0 + 12)
                    if (u((v4 + 2)) < u(load32(load32(arg0 + 12) + 8))):
                        continue
                    break
            store32(v3 + 8, 0)
            break
        while True:  # block $label37
            v12 = load8u(arg0 + 125)
            if (load8u(arg0 + 125) != 4):
                break
            v2 = load8u(arg0 + 122)
            if (load8u(arg0 + 122) == load32(38600)):
                break
            if (load32(38472) == v2):
                break
            if load8u(9216060):
                break
            v2 = ((v10 * 404) + 9568164)
            v3 = (v9 + (v8 * 286704))
            v4 = load32((v9 + (v8 * 286704)) + 283848)
            if (load32((v9 + (v8 * 286704)) + 283848) != 2147483647):
                store32((v3 + 283848), (load32(v2) + v4))
            v3 = (v3 + 283852)
            v4 = load32((v3 + 283852))
            if (load32((v3 + 283852)) != 2147483647):
                store32(v3, (load32(v2 + 4) + v4))
            v3 = (v9 + (v8 * 286704))
            v4 = ((v9 + (v8 * 286704)) + 283856)
            v5 = load32(((v9 + (v8 * 286704)) + 283856))
            if (load32(((v9 + (v8 * 286704)) + 283856)) != 2147483647):
                store32(v4, (load32(v2 + 8) + v5))
            v3 = (v3 + 283860)
            v4 = load32((v3 + 283860))
            if (load32((v3 + 283860)) != 2147483647):
                store32(v3, (load32(v2 + 12) + v4))
            v3 = (v9 + (v8 * 286704))
            v4 = ((v9 + (v8 * 286704)) + 281692)
            store32(((v9 + (v8 * 286704)) + 281692), (load32(v4) - load32(v2)))
            v4 = (v3 + 281696)
            store32((v3 + 281696), (load32(v4) - load32(v2 + 4)))
            v4 = (v3 + 281700)
            store32((v3 + 281700), (load32(v4) - load32(v2 + 8)))
            v2 = load32(v2 + 12)
            v4 = 1
            store8(v3 + 286701, 1)
            v5 = (v3 + 281704)
            store32((v3 + 281704), (load32(v5) - v2))
            v2 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v5 = (v2 - 1)
            v16 = ((v2 - 1) & 1)
            v3 = (load32(v3 + 283908) * v2)
            v6 = load32(9561692)
            v7 = load32(9143016)
            if (v2 != 2):
                v2 = (v5 & -2)
                v5 = 0
                while True:  # $label38
                    if load8u((v7 + (v3 + v4))):
                        store8((v6 + (v4 * 286704)) + 286701, 1)
                    v17 = (v4 + 1)
                    if load8u((v7 + ((v4 + 1) + v3))):
                        store8((v6 + (v17 * 286704)) + 286701, 1)
                    v4 = (v4 + 2)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v2):
                        continue
                    break
            if (v16 == 0):
                break
            if (load8u((v7 + (v3 + v4))) == 0):
                break
            store8((v6 + (v4 * 286704)) + 286701, 1)
            break
        if (v11 == 0):
        func202(arg0, 0, 1)
        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 34):
            v2 = (v9 + (v8 * 286704))
            store32((v9 + (v8 * 286704)) + 283912, (load32(v2 + 283912) - 1))
        func157(arg0)
        while True:  # block $label39
            v7 = (v9 + (v8 * 286704))
            v4 = load32((v9 + (v8 * 286704)) + 281796)
            if (load32((v9 + (v8 * 286704)) + 281796) == 0):
                break
            v5 = load32(v4 + 8)
            if (load32(v4 + 8) == 0):
                break
            v6 = load32(v4)
            v2 = 0
            v12 = (v9 + (v8 * 286704))
            while True:  # $label42
                v3 = (v6 + (v2 << 2))
                if (load32((v6 + (v2 << 2))) == load32(arg0 + 28)):
                    v3 = ((v12 + (load32(v3 + 4) << 2)) + 282828)
                    store32(((v12 + (load32(v3 + 4) << 2)) + 282828), (load32(v3) - 1))
                    v5 = (load32(v4 + 8) - 1)
                    store32(v4 + 8, (load32(v4 + 8) - 1))
                    v3 = v2
                    if (u(v5) > u(v2)):
                        while True:  # $label40
                            v3 = (v3 + 1)
                            store32((v6 + (v3 << 2)), load32((v6 + ((v3 + 1) << 2))))
                            v5 = load32(v4 + 8)
                            if (u(v3) < u(load32(v4 + 8))):
                                continue
                            break
                    v5 = (v5 - 1)
                    store32(v4 + 8, (v5 - 1))
                    v3 = v2
                    if (u(v5) > u(v2)):
                        while True:  # $label41
                            v3 = (v3 + 1)
                            store32((v6 + (v3 << 2)), load32((v6 + ((v3 + 1) << 2))))
                            v5 = load32(v4 + 8)
                            if (u(v3) < u(load32(v4 + 8))):
                                continue
                            break
                    v2 = (v2 - 2)
                v2 = (v2 + 2)
                if (u((v2 + 2)) < u(v5)):
                    continue
                break
            break
        while True:  # block $label43
            v5 = load32(v7 + 281788)
            if (load32(v7 + 281788) == 0):
                break
            v3 = load32(v5 + 8)
            if (load32(v5 + 8) == 0):
                break
            v6 = load32(v5)
            v2 = 0
            while True:  # $label45
                if (load32((v6 + (v2 << 2))) == load32(arg0 + 28)):
                    v3 = (v3 - 1)
                    store32(v5 + 8, (v3 - 1))
                    v4 = v2
                    if (u(v2) < u(v3)):
                        while True:  # $label44
                            v4 = (v4 + 1)
                            store32((v6 + (v4 << 2)), load32((v6 + ((v4 + 1) << 2))))
                            v3 = load32(v5 + 8)
                            if (u(v4) < u(load32(v5 + 8))):
                                continue
                            break
                    v2 = (v2 - 1)
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(v3)):
                    continue
                break
            break
        if (v11 == 0):
        v6 = ((v8 * 286704) + v9)
        v5 = (load32(38428) if load16u(arg0 + 120) else load8u(arg0 + 122))
        while True:  # block $label48
            while True:  # block $label46
                while True:  # block $label47
                    # br_table[(load8u(arg0 + 125) - 4)]
                    break
                    break
                v2 = (((v9 + (v8 * 286704)) + (v5 << 2)) + 281808)
                store32((((v9 + (v8 * 286704)) + (v5 << 2)) + 281808), (load32(v2) - 1))
                store8(arg0 + 125, 3)
                if load16u(arg0 + 110):
                    func387(v6)
                v3 = load32(((v10 * 404) + 9568096) + 176)
                if (load32(((v10 * 404) + 9568096) + 176) == 0):
                    break
                v2 = (v9 + (v8 * 286704))
                store32((v9 + (v8 * 286704)) + 283980, (load32(v2 + 283980) - v3))
                v4 = load32(v2 + 283976)
                if (u(v3) >= u(-2147483647)):
                    store8(v2 + 286700, 1)
                v2 = (v2 + 281748)
                if (u(load32((v2 + 281748))) >= u(v4)):
                    break
                store32(v2, v4)
                break
                break
            v2 = (((v9 + (v8 * 286704)) + (v5 << 2)) + 282828)
            store32((((v9 + (v8 * 286704)) + (v5 << 2)) + 282828), (load32(v2) - 1))
            break
        store8(arg0 + 125, 3)
        if (load8u(9147152) == 0):
            func77(arg0)
        while True:  # block $label49
            if (load32(9142872) != load16u(arg0 + 110)):
                break
            v2 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 180)
            if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 180) == 0):
                break
            break
        while True:  # block $label50
            if (u(load32(arg0 + 84)) < u(12)):
                break
            if load32(((load8u(arg0 + 122) * 404) + 9568096) + 264):
                break
            v2 = (v9 + (v8 * 286704))
            store32((v9 + (v8 * 286704)) + 283936, (load32(v2 + 283936) - 1))
            break
        v2 = (v9 + (v8 * 286704))
        v4 = load32(((v10 * 404) + 9568096) + 280)
        v3 = (load32(v2 + 283976) - load32(((v10 * 404) + 9568096) + 280))
        store32((v9 + (v8 * 286704)) + 283976, (load32(v2 + 283976) - load32(((v10 * 404) + 9568096) + 280)))
        if ((v4 - 1) >= 0):
            store8(v2 + 286700, 1)
        v2 = (v2 + 281748)
        if (u(v3) > u(load32((v2 + 281748)))):
            store32(v2, v3)
        while True:  # block $label51
            if (v5 != load32(38452)):
                break
            v2 = (v9 + (v8 * 286704))
            if load32((((v9 + (v8 * 286704)) + (v5 << 2)) + 281808)):
                break
            v4 = 0
            store32(((v2 + (load32(39144) << 2)) + 281808), 1)
            store32(v2 + 283868, load32((v2 + 284380)))
            v2 = load32(((v2 + (load32(38636) << 2)) + 284636))
            if (load32(((v2 + (load32(38636) << 2)) + 284636)) == 0):
                break
            v3 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                break
            while True:  # $label52
                v7 = load32((load32(v2) + (v4 << 2)))
                if load32((load32(v2) + (v4 << 2))):
                v4 = (v4 + 1)
                if ((v4 + 1) != v3):
                    continue
                break
            break
        while True:  # block $label53
            v2 = (v9 + (v8 * 286704))
            if load32((((v9 + (v8 * 286704)) + (v5 << 2)) + 281808)):
                break
            if (load32(v2 + 283908) != load32(9142872)):
                break
            v3 = ((v10 * 404) + 9568096)
            if (load32(((v10 * 404) + 9568096) + 244) == 0):
                break
            v2 = 0
            while True:  # $label57
                v11 = load32((load32(v3 + 240) + (v2 << 2)))
                while True:  # block $label54
                    if load8u(9147141):
                        break
                    v4 = 0
                    v12 = load32(9671120)
                    if (load32(9671120) == 0):
                        break
                    while True:  # $label56
                        while True:  # block $label55
                            v7 = load32(((v4 << 2) + 9263072))
                            if (load32(((v4 << 2) + 9263072)) == 0):
                                break
                            if (load32(v7 + 12) != v11):
                                break
                            if load8u(v7 + 24):
                                break
                            break
                            break
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v12):
                            continue
                        break
                    break
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(load32(v3 + 244))):
                    continue
                break
            break
        v2 = load32(arg0 + 44)
        if load32(arg0 + 44):
            store32((load32(9215884) + (v2 << 4)), 0)
        store32(arg0 + 64, 0)
        store32(arg0 + 44, 0)
        v2 = load32(9142848)
        store8(arg0 + 122, v5)
        store16(arg0 + 116, 0)
        store32(arg0 + 68, v2)
        while True:  # block $label58
            if load8u(9147152):
                break
            v3 = load32(arg0 + 28)
            while True:  # block $label59
                v2 = load32((((v9 + (v8 * 286704)) + (v5 << 2)) + 284636))
                if (load32((((v9 + (v8 * 286704)) + (v5 << 2)) + 284636)) == 0):
                    break
                v5 = load32(v2 + 8)
                if (load32(v2 + 8) == 0):
                    break
                v2 = load32(v2)
                v4 = 0
                while True:  # $label60
                    v8 = (v2 + (v4 << 2))
                    if (v3 != load32((v2 + (v4 << 2)))):
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v5):
                            continue
                        break
                    break
                if (v4 < 0):
                    break
                store32(v8, 0)
                v3 = load32(arg0 + 28)
                break
            func388(v6, v3)
            if (load32(38528) != load8u(arg0 + 122)):
                break
            if load8u(9147152):
                break
            break
        if (load8u(9216060) == 0):
            break
        if (load32(v14 + 264) == 2):
            break
        if arg1:
            break
        if load8u(9147152):
            break
        if (load32(((v10 * 404) + 9568096) + 68) == 0):
            break
        break
    G.global0 = (v13 + 16)
    return func46(0, 0)

# ------------------------------------------------------------
# $func33
# ------------------------------------------------------------
def func33(arg0, arg1):
    if (arg1 <= 0):
        return 0
    v3 = load32(arg0 + 12)
    v4 = load32(arg0 + 8)
    while True:  # block $label1
        while True:  # $label4
            while True:  # block $label0
                if (v3 >= 0):
                    break
                v2 = load32(arg0 + 16)
                if (load32(arg0 + 16) == 0):
                    break
                if (u(load32(arg0 + 24)) > u(v2)):
                    v9 = load64(v2)
                    store32(arg0 + 16, (v2 + 7))
                    store64(arg0, ((load64(arg0) << 56) | ((((((v9 << 56) | ((v9 & 65280) << 40)) | (((v9 & 16711680) << 24) | ((v9 & 4278190080) << 8))) | ((((v9 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v9 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v9 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8)))
                    break
                while True:  # block $label2
                    if (u(load32(arg0 + 20)) > u(v2)):
                        store32(arg0 + 16, (v2 + 1))
                        store64(arg0, (load64(v2) | (load64(arg0) << 8)))
                        break
                    if load32(arg0 + 28):
                        break
                    store32(arg0 + 28, 1)
                    store64(arg0, (load64(arg0) << 8))
                    break
                break
            v2 = (v3 + 8)
            v7 = (arg1 - 1)
            while True:  # block $label3
                v5 = (((v4 & 0xFFFFFFFF) >> 1) & 16777215)
                v9 = load64(arg0)
                v10 = i64(v2)
                v8 = i32(((load64(arg0) & 0xFFFFFFFFFFFFFFFF) >> i64(v2)))
                if (u((((v4 & 0xFFFFFFFF) >> 1) & 16777215)) < u(i32(((load64(arg0) & 0xFFFFFFFFFFFFFFFF) >> i64(v2))))):
                    store64(arg0, (v9 - (i64((v5 + 1)) << v10)))
                    break
                break
            v4 = (v5 + 1)
            v2 = (clz((v5 + 1)) ^ 24)
            v3 = ((v4 - v5) - (clz((v5 + 1)) ^ 24))
            store32(v2 + 12, ((v4 - v5) - (clz((v5 + 1)) ^ 24)))
            v4 = ((v4 << v2) - 1)
            store32(arg0 + 8, ((v4 << v2) - 1))
            v6 = (((u(v5) < u(v8)) << v7) | v6)
            v2 = (u(arg1) > u(1))
            arg1 = v7
            if v2:
                continue
            break
        return v6
        break
    a_c()
    raise RuntimeError('unreachable')
    return 3339

# ------------------------------------------------------------
# $func34
# ------------------------------------------------------------
def func34(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # block $label0
        if (load32(9147132) == 0):
            v7 = load32(9671136)
            break
        while True:  # block $label2
            while True:  # block $label1
                v18 = load32(9142848)
                if (load32(9142848) == load32(9671144)):
                    break
                store32(9671148, 3)
                store32(9671144, v18)
                break
            v6 = 3
            v7 = load32(9671136)
            if (u(3) < u(load32(9671136))):
                v9 = load32(9671128)
                while True:  # $label3
                    v8 = (v9 + (v6 * 132))
                    if (load8u((v9 + (v6 * 132)) + 125) == 3):
                        if (u(((v18 - load32(v8 + 68)) * 25)) > u(70000)):
                            break
                    v6 = (v6 + 1)
                    if ((v6 + 1) != v7):
                        continue
                    break
            store32(9671148, v7)
            break
            break
        store32(9671148, (v6 + 1))
        v7 = v6
        break
    while True:  # block $label4
        v19 = ((arg0 * 404) + 9568096)
        if (load32(((arg0 * 404) + 9568096) + 264) == 3):
            break
        v20 = load32(9561692)
        v16 = (arg1 if (arg1 != 2147483647) else 0)
        if (func56(arg2, arg3, v19, (arg1 if (arg1 != 2147483647) else 0), 1, v7, 1, arg5, 0) == 0):
            break
        while True:  # block $label5
            v18 = (v7 != load32(9671136))
            if ((v7 != load32(9671136)) == 0):
                v8 = (v7 + 1)
                store32(9671136, (v7 + 1))
                v6 = load32(9671132)
                if (u(v8) < u(load32(9671132))):
                    break
                v6 = (load32(9671140) + v6)
                store32(9671132, (load32(9671140) + v6))
                store32(9671128, func228(load32(9671128), v6, v8))
                break
            v9 = func26(4)
            v6 = (func26(4) + 4)
            v10 = (load32(9671128) + (v7 * 132))
            v8 = load32((load32(9671128) + (v7 * 132)))
            if load32((load32(9671128) + (v7 * 132))):
                store32(v10 + 4, v8)
            store32(v10 + 8, v6)
            store32(v10 + 4, v9)
            store32(v10, v9)
            # TODO: memory.fill []
            break
        v11 = load32(9671128)
        v21 = (load32(9671128) + (v7 * 132))
        store32((load32(9671128) + (v7 * 132)) + 28, v7)
        while True:  # block $label8
            while True:  # block $label6
                while True:  # block $label7
                    if (load32(v19 + 264) != 2):
                        if (load32(((arg0 * 404) + 9568096) + 188) == 55):
                            break
                        if (load32(38500) != arg0):
                            break
                        break
                    if (load32(38500) == arg0):
                        break
                    break
                if (load32(38528) != arg0):
                    break
                break
            store16((v11 + (v7 * 132)) + 110, v16)
            break
        while True:  # block $label9
            if (arg1 != 2147483647):
                break
            if (load32(((arg0 * 404) + 9568096) + 188) != 55):
                break
            store8((v11 + (v7 * 132)) + 126, 2)
            break
        v8 = (v11 + (v7 * 132))
        store16((v11 + (v7 * 132)) + 114, arg3)
        store16(v8 + 112, arg2)
        store8(v8 + 122, arg0)
        v6 = ((arg0 * 404) + 9568096)
        arg1 = load32(((arg0 * 404) + 9568096) + 168)
        store8(v8 + 124, (load32(((arg0 * 404) + 9568096) + 168) if arg1 else arg4))
        while True:  # block $label10
            if arg5:
                func420(v21)
                v10 = load32(((load8u(v8 + 122) * 72) + 9263856))
                store32(v8 + 64, (load32((((v20 + (v16 * 286704)) + (arg0 * 36)) + 269388)) + load32(v6 + 104)))
                break
            while True:  # block $label11
                v6 = load32(v6 + 356)
                if load32(v6 + 356):
                    break
                arg1 = ((arg0 * 404) + 9568096)
                arg4 = load32(((arg0 * 404) + 9568096) + 216)
                arg1 = load32(arg1 + 220)
                arg1 = (load32(((arg0 * 404) + 9568096) + 216) if (u(arg1) < u(arg4)) else load32(arg1 + 220))
                arg1 = ((6 if (u(arg1) >= u(6)) else (load32(((arg0 * 404) + 9568096) + 216) if (u(arg1) < u(arg4)) else load32(arg1 + 220))) - 1)
                if (u(((6 if (u(arg1) >= u(6)) else (load32(((arg0 * 404) + 9568096) + 216) if (u(arg1) < u(arg4)) else load32(arg1 + 220))) - 1)) > u(4)):
                    v6 = 9142636
                    break
                v6 = load32(((arg1 << 2) + 10132))
                break
            v10 = load32(v6)
            arg1 = (v11 + (v7 * 132))
            store8((v11 + (v7 * 132)) + 125, 4)
            store32(arg1 + 64, 1)
            arg1 = (((v20 + (v16 * 286704)) + (arg0 << 2)) + 282828)
            store32((((v20 + (v16 * 286704)) + (arg0 << 2)) + 282828), (load32(arg1) + 1))
            break
        v6 = (v11 + (v7 * 132))
        arg4 = ((arg0 * 404) + 9568096)
        arg1 = ((v20 + (v16 * 286704)) + (arg0 * 36))
        store32((v11 + (v7 * 132)) + 68, (load32(((arg0 * 404) + 9568096) + 108) + load32((((v20 + (v16 * 286704)) + (arg0 * 36)) + 269392))))
        store32(v6 + 52, (load32(arg4 + 92) + load32((arg1 + 269380))))
        store32(v6 + 60, (load32(arg4 + 100) + load32((arg1 + 269384))))
        store32(v6 + 84, (load32(arg4 + 112) + load32((arg1 + 269396))))
        arg1 = (load32(arg4 + 120) + load32((arg1 + 269404)))
        store32(v6 + 72, (load32(arg4 + 120) + load32((arg1 + 269404))))
        store32(v6 + 76, arg1)
        if (arg0 == load32(38528)):
            store32(v6 + 80, 300)
        if (arg0 == load32(38500)):
            v22 = load64(9147316)
            arg4 = load32(9147312)
            store32(9147316, load32(9147312))
            arg1 = load32(9147324)
            store64(9147320, v22)
            arg1 = (arg1 ^ (arg1 << 11))
            arg1 = ((arg4 ^ (((arg4 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1)
            store32(9147312, ((arg4 ^ (((arg4 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1))
            store8(v8 + 124, (arg1 % 9))
        while True:  # block $label19
            if load8u(9147213):
                while True:  # block $label13
                    while True:  # block $label12
                        arg1 = load32(load32(9142424) + 48)
                        if (load32(load32(9142424) + 48) == 0):
                            break
                        v12 = load32(((arg0 * 404) + 9568096) + 216)
                        if (load32(((arg0 * 404) + 9568096) + 216) == 0):
                            break
                        if load8u(9147152):
                            break
                        v14 = load32(9142440)
                        v15 = load32(9147376)
                        while True:  # block $label16
                            if (arg1 != 2):
                                v9 = (v12 & -2)
                                v8 = (v12 & 1)
                                v6 = 0
                                while True:  # $label15
                                    v13 = (arg2 + v17)
                                    arg1 = 0
                                    arg4 = 0
                                    if (v12 != 1):
                                        while True:  # $label14
                                            v6 = (((load16u((v15 + ((v13 + (v14 * ((arg1 | 1) + arg3))) << 1))) | load16u((v15 + ((v13 + (v14 * (arg1 + arg3))) << 1)))) != 0) | v6)
                                            arg1 = (arg1 + 2)
                                            arg4 = (arg4 + 2)
                                            if ((arg4 + 2) != v9):
                                                continue
                                            break
                                    if v8:
                                        v6 = ((load16u((v15 + ((v13 + (v14 * (arg1 + arg3))) << 1))) != 0) | v6)
                                    v17 = (v17 + 1)
                                    if ((v17 + 1) != v12):
                                        continue
                                    break
                                break
                            v9 = (v12 & -2)
                            v8 = (v12 & 1)
                            v6 = 0
                            while True:  # $label18
                                v13 = (arg2 + v17)
                                arg1 = 0
                                arg4 = 0
                                if (v12 != 1):
                                    while True:  # $label17
                                        v6 = (((u(load16u((v15 + ((v13 + (v14 * ((arg1 | 1) + arg3))) << 1)))) > u(1)) | (u(load16u((v15 + ((v13 + (v14 * (arg1 + arg3))) << 1)))) > u(1))) | v6)
                                        arg1 = (arg1 + 2)
                                        arg4 = (arg4 + 2)
                                        if ((arg4 + 2) != v9):
                                            continue
                                        break
                                if v8:
                                    v6 = ((u(load16u((v15 + ((v13 + (v14 * (arg1 + arg3))) << 1)))) > u(1)) | v6)
                                v17 = (v17 + 1)
                                if ((v17 + 1) != v12):
                                    continue
                                break
                            break
                        if ((v6 & 1) == 0):
                            break
                        break
                    break
                break
            if (load32(v19 + 264) != 2):
                break
            if (load32(((arg0 * 404) + 9568096) + 268) == 1):
                store32(v6 + 52, 1)
                break
            if (load32(38964) != arg0):
                break
            store32((v11 + (v7 * 132)) + 80, ((D(12) * 10) + 10))
            break
        while True:  # block $label20
            if (load8u(9147152) == 0):
                func240(v21, 500, v18)
                break
            store32((v11 + (v7 * 132)) + 32, -1)
            break
        while True:  # block $label21
            arg0 = load32(((arg0 * 404) + 9568096) + 280)
            if load32(((arg0 * 404) + 9568096) + 280):
                arg2 = (v20 + (v16 * 286704))
                arg1 = (load32(arg2 + 283976) + arg0)
                store32((v20 + (v16 * 286704)) + 283976, (load32(arg2 + 283976) + arg0))
                if (arg0 < 0):
                    store8(arg2 + 286700, 1)
                arg0 = (arg2 + 281748)
                if (u(load32((arg2 + 281748))) >= u(arg1)):
                    break
                store32(arg0, arg1)
                break
            if (load32(v19 + 264) != 1):
                break
            if arg5:
                break
            store32((v11 + (v7 * 132)) + 88, load32(9142848))
            break
        break
    return v7

# ------------------------------------------------------------
# $func35
# ------------------------------------------------------------
def func35(arg0, arg1, arg2):
    if (u(arg2) >= u(512)):
        # TODO: memory.copy []
        return arg0
    v4 = (arg0 + arg2)
    while True:  # block $label3
        if (((arg0 ^ arg1) & 3) == 0):
            while True:  # block $label0
                if ((arg0 & 3) == 0):
                    break
                if (arg2 == 0):
                    break
                arg2 = (arg0 ^ -1)
                v3 = (arg0 + 1)
                v3 = ((arg0 ^ -1) + (v4 if (u(v3) < u(v4)) else (arg0 + 1)))
                arg2 = (arg2 & 3)
                arg2 = ((((arg0 ^ -1) + (v4 if (u(v3) < u(v4)) else (arg0 + 1))) if (u(arg2) > u(v3)) else (arg2 & 3)) + 1)
                # TODO: memory.copy []
                arg1 = (arg1 + arg2)
                break
            arg2 = (arg0 + arg2)
            while True:  # block $label1
                v3 = (v4 & -4)
                if (u((v4 & -4)) < u(64)):
                    break
                v5 = (v3 + -64)
                if (u(arg2) > u((v3 + -64))):
                    break
                while True:  # $label2
                    store32(arg2, load32(arg1))
                    store32(arg2 + 4, load32(arg1 + 4))
                    store32(arg2 + 8, load32(arg1 + 8))
                    store32(arg2 + 12, load32(arg1 + 12))
                    store32(arg2 + 16, load32(arg1 + 16))
                    store32(arg2 + 20, load32(arg1 + 20))
                    store32(arg2 + 24, load32(arg1 + 24))
                    store32(arg2 + 28, load32(arg1 + 28))
                    store32(arg2 + 32, load32(arg1 + 32))
                    store32(arg2 + 36, load32(arg1 + 36))
                    store32(arg2 + 40, load32(arg1 + 40))
                    store32(arg2 + 44, load32(arg1 + 44))
                    store32(arg2 + 48, load32(arg1 + 48))
                    store32(arg2 + 52, load32(arg1 + 52))
                    store32(arg2 + 56, load32(arg1 + 56))
                    store32(arg2 + 60, load32(arg1 + 60))
                    arg1 = (arg1 - -64)
                    arg2 = (arg2 - -64)
                    if (u((arg2 - -64)) <= u(v5)):
                        continue
                    break
                break
            if (u(arg2) >= u(v3)):
                break
            v5 = (arg2 + 4)
            v3 = ((((arg2 ^ -1) + (v3 if (u(v3) > u(v5)) else (arg2 + 4))) & -4) + 4)
            # TODO: memory.copy []
            arg1 = (arg1 + v3)
            arg2 = (arg2 + v3)
            break
        if (u(v4) < u(4)):
            arg2 = arg0
            break
        v3 = (v4 - 4)
        if (u(arg0) > u((v4 - 4))):
            arg2 = arg0
            break
        arg2 = arg0
        while True:  # $label4
            store8(arg2, load8u(arg1))
            store8(arg2 + 1, load8u(arg1 + 1))
            store8(arg2 + 2, load8u(arg1 + 2))
            store8(arg2 + 3, load8u(arg1 + 3))
            arg1 = (arg1 + 4)
            arg2 = (arg2 + 4)
            if (u((arg2 + 4)) <= u(v3)):
                continue
            break
        break
    if (u(arg2) < u(v4)):
        # TODO: memory.copy []
    return arg0

# ------------------------------------------------------------
# $func36
# ------------------------------------------------------------
def func36(arg0):
    while True:  # block $label0
        if (arg0 == 0):
            break
        v1 = load32(arg0 + 16)
        if (load32(arg0 + 16) == 0):
            break
        if (u(load32(arg0 + 20)) > u(v1)):
            store32(arg0 + 16, (v1 + 1))
            store32(arg0 + 12, (load32(arg0 + 12) + 8))
            store64(arg0, (load64(v1) | (load64(arg0) << 8)))
            return
        if (load32(arg0 + 28) == 0):
            store32(arg0 + 28, 1)
            store64(arg0, (load64(arg0) << 8))
            store32(arg0 + 12, (load32(arg0 + 12) + 8))
            return
        store32(arg0 + 12, 0)
        return
        break
    a_c()
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func37
# ------------------------------------------------------------
def func37(arg0, arg1, arg2, arg3):
    v5 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    while True:  # block $label0
        if (arg1 == 0):
            break
        v11 = load32(arg0 + 40)
        if (load32(arg0 + 40) == 0):
            break
        v12 = load32(9142848)
        store32(arg0 + 48, arg1)
        v10 = load16u(arg0 + 110)
        v4 = load16u(arg0 + 120)
        v7 = load8u(arg0 + 122)
        while True:  # block $label1
            if load32(arg0 + 92):
                v8 = 13
                if load8u(9142906):
                    break
            v8 = (((v4 if v4 else v10) & 65535) + 16)
            if (load8u(9142916) == 0):
                v4 = load8u(arg0 + 127)
                v10 = ((v7 * 404) + 9568096)
                if ((load8u(arg0 + 127) | load32(((v7 * 404) + 9568096) + 156)) == 0):
                    break
                v8 = load32(v10 + 156)
                v8 = (load32(v10 + 156) if v8 else v4)
                break
            v4 = load8u(arg0 + 127)
            v8 = (load8u(arg0 + 127) if v4 else v8)
            break
        v10 = load32(((v7 * 404) + 9568096) + 264)
        v14 = load32(arg1 + 32)
        v15 = load32(arg1 + 24)
        v7 = load32(arg1)
        v16 = load32(arg1 + 16)
        v4 = (load32(arg1 + 16) * load32(arg1 + 20))
        if (load32(arg1 + 16) * load32(arg1 + 20)):
            # TODO: f64.promote_f32 []
            v20 = float((load32(arg1 + 4) // v4))
        if (arg3 == 0):
            while True:  # block $label7
                while True:  # block $label3
                    while True:  # block $label2
                        if load8u(9147152):
                            v4 = load8u(arg0 + 125)
                            break
                        v4 = load32(9142872)
                        if (load32(9142872) == 0):
                            break
                        if (load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(9142892) * v4)))) == 0):
                            break
                        v4 = load8u(arg0 + 125)
                        if (load8u(arg0 + 125) == 3):
                            break
                        break
                    while True:  # block $label6
                        while True:  # block $label5
                            while True:  # block $label4
                                # br_table[(v4 - 4)]
                                break
                                break
                            v4 = load8u(arg0 + 122)
                            v6 = ((load8u(arg0 + 122) * 404) + 9568096)
                            v9 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 216)
                            v6 = load32(v6 + 220)
                            break
                            break
                        v4 = load8u(arg0 + 122)
                        break
                    v6 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 200)
                    if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 200) == 0):
                        break
                    while True:  # block $label8
                        v9 = load16u(arg0 + 114)
                        v4 = ((v4 * 404) + 9568096)
                        # TODO: f32.convert_i32_u []
                        # TODO: f32.convert_i32_u []
                        v9 = load32(arg0 + 48)
                        v18 = ceil(((((load16u(arg0 + 114) + ((load32(((v4 * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1)) << 5) - ((v9 * 32.0) - float(load32(load32(arg0 + 48) + 12)))) * 0.03125))
                        if (abs(ceil(((((load16u(arg0 + 114) + ((load32(((v4 * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1)) << 5) - ((v9 * 32.0) - float(load32(load32(arg0 + 48) + 12)))) * 0.03125))) < 2147483650.0):
                            break
                        break
                    v13 = (-2147483648 * 10)
                    while True:  # block $label9
                        v6 = load16u(arg0 + 112)
                        # TODO: f32.convert_i32_u []
                        # TODO: f32.convert_i32_u []
                        v18 = ceil(((((load16u(arg0 + 112) + ((load32(v4 + 216) & 0xFFFFFFFF) >> 1)) << 5) - ((v6 * 32.0) - float(load32(v9 + 8)))) * 0.03125))
                        if (abs(ceil(((((load16u(arg0 + 112) + ((load32(v4 + 216) & 0xFFFFFFFF) >> 1)) << 5) - ((v6 * 32.0) - float(load32(v9 + 8)))) * 0.03125))) < 2147483650.0):
                            break
                        break
                    # TODO: f32.convert_i32_u []
                    v18 = (int(v18) + ((-2147483648 + v13) << 8))
                    break
                break
            # TODO: f64.promote_f32 []
            v21 = v18
        if (load8u(9142916) == 0):
            store32(v5 + 112, v11)
            store32(v5 + 104, v21)
            store64(v5 + 96, -4616189618054758400)
            store32(v5 + 88, v20)
            # TODO: f64.promote_f32 []
            store32(v5 + 80, float(v7))
            a_b()
        # TODO: f32.convert_i32_u []
        arg2 = ((v12 * 25) if (arg2 == 0.0) else arg2)
        while True:  # block $label15
            while True:  # block $label14
                while True:  # block $label12
                    while True:  # block $label13
                        v13 = load32(arg1 + 20)
                        if load32(arg1 + 20):
                            v12 = load8u(arg0 + 124)
                            v11 = load8u(9142916)
                            while True:  # block $label11
                                v4 = load32(arg1 + 28)
                                if (load32(arg1 + 28) == 2147483647):
                                    while True:  # block $label10
                                        if v11:
                                            v4 = load32(59152)
                                            store32(59152, (load32(59152) + 1))
                                            v6 = load32(9568052)
                                            v9 = load32(arg1)
                                            break
                                        v9 = load32(arg1)
                                        v6 = load32(9568052)
                                        v4 = ((load32(arg1) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                        break
                                    store32(arg1 + 28, v4)
                                    v7 = load32(arg1 + 4)
                                    v17 = load32(9568048)
                                    store32(9568048, (load32(9568048) + 1))
                                    store32(((v17 << 2) + 9563952), arg1)
                                    store32(9568052, (((v9 * (v7 + 2)) << 2) + v6))
                                    if (v11 == 0):
                                        break
                                    arg3 = load32(9568056)
                                    store32(arg1 + 56, load32(9568056))
                                    store32(9568056, (arg3 + ((v7 * load32(arg1)) << 2)))
                                    break
                                if v11:
                                    break
                                v7 = load32(arg1 + 4)
                                break
                            arg2 = (arg2 + -0.0)
                            # TODO: i32.div_u []
                            # TODO: f32.convert_i32_u []
                            v19 = (v13 + v4)
                            arg1 = load32(arg0 + 40)
                            break
                        arg2 = (arg2 + -0.0)
                        v4 = 0
                        arg1 = load32(arg0 + 40)
                        if load8u(9142916):
                            break
                        break
                    store32(v5 + 16, ((15 if (v10 == 1) else v8) if arg3 else v8))
                    # TODO: f32.convert_i32_u []
                    # TODO: f64.promote_f32 []
                    store32(v5 + 24, ((((200 if (v14 == 27) else (0 if (v10 & -5) else 100)) + v16) << 16) + v15))
                    store32(v5 + 32, arg1)
                    # TODO: f64.promote_f32 []
                    store32(v5 + 8, arg2)
                    # TODO: f32.convert_i32_u []
                    # TODO: f64.promote_f32 []
                    store32(v5, (v19 / load32(59156)))
                    a_b()
                    break
                    break
                arg2 = (arg2 + -0.0)
                v4 = (v4 + (v12 << 16))
                break
            store32(v5, load32(arg0 + 40))
            store32(v5 + 48, v4)
            # TODO: f64.promote_f32 []
            store32(v5 + 56, arg2)
            a_b()
            break
        if load8u(9142916):
            break
        break
    G.global0 = (v5 + 128)
    return func60(arg0, 1.0)

# ------------------------------------------------------------
# $func38
# ------------------------------------------------------------
def func38(arg0):
    v3 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label1
        if (u(arg0) >= u(1073741823)):
            v5 = (arg0 - 1073741823)
            while True:  # block $label0
                v1 = load32(9299896)
                if (load32(9299896) != load32(9299892)):
                    v2 = load32(9299888)
                    break
                v2 = (load32(9299900) + v1)
                store32(9299892, (load32(9299900) + v1))
                v4 = load32(9299888)
                v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                if v1:
                    # TODO: memory.copy []
                if v4:
                    v1 = load32(9299896)
                store32(9299888, v2)
                break
            store32(9299896, (v1 + 1))
            store32((v2 + (v1 << 2)), v5)
            break
        while True:  # block $label2
            v1 = load32(9299880)
            if (load32(9299880) != load32(9299876)):
                v2 = load32(9299872)
                break
            v2 = (load32(9299884) + v1)
            store32(9299876, (load32(9299884) + v1))
            v4 = load32(9299872)
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if v1:
                # TODO: memory.copy []
            if v4:
                v1 = load32(9299880)
            store32(9299872, v2)
            break
        store32(9299880, (v1 + 1))
        store32((v2 + (v1 << 2)), arg0)
        break
    while True:  # block $label3
        if load8u(9142916):
            store32(v3 + 32, arg0)
            a_b()
            break
        store32(v3 + 24, arg0)
        store64(v3 + 16, -4602115869219225600)
        store64(v3 + 8, 0)
        store64(v3, 0)
        a_b()
        break
    G.global0 = (v3 + 48)

# ------------------------------------------------------------
# $func39
# ------------------------------------------------------------
def func39(arg0, arg1):
    while True:  # block $label3
        if (arg1 >= 0):
            while True:  # block $label4
                while True:  # block $label5
                    while True:  # block $label0
                        if (u(arg1) > u(24)):
                            break
                        if load32(arg0 + 24):
                            break
                        v5 = (arg0 + 20)
                        v6 = load32(arg0 + 20)
                        v2 = (load32(arg0 + 20) + arg1)
                        store32((arg0 + 20), (load32(arg0 + 20) + arg1))
                        v7 = load32(((arg1 << 2) + 17888))
                        v11 = load64(arg0)
                        while True:  # block $label1
                            if (v2 <= 7):
                                v4 = load32(arg0 + 12)
                                v3 = load32(arg0 + 16)
                                break
                            arg1 = load32(arg0 + 16)
                            v4 = load32(arg0 + 12)
                            v3 = (load32(arg0 + 16) if (u(arg1) > u(v4)) else load32(arg0 + 12))
                            v10 = v11
                            while True:  # $label2
                                if (arg1 == v3):
                                    break
                                v10 = ((v10 & 0xFFFFFFFFFFFFFFFF) >> 8)
                                store64(arg0, ((v10 & 0xFFFFFFFFFFFFFFFF) >> 8))
                                v12 = load64((load32(arg0 + 8) + arg1))
                                v8 = (v2 - 8)
                                store32(arg0 + 20, (v2 - 8))
                                arg1 = (arg1 + 1)
                                store32(arg0 + 16, (arg1 + 1))
                                v10 = ((v12 << 56) | v10)
                                store64(arg0, ((v12 << 56) | v10))
                                v9 = (v2 > 15)
                                v2 = v8
                                if v9:
                                    continue
                                break
                            v3 = arg1
                            break
                        if (u(v3) > u(v4)):
                            break
                        arg1 = (v7 & i32(((v11 & 0xFFFFFFFFFFFFFFFF) >> i64((v6 & 63)))))
                        if (v3 != v4):
                            break
                        if (v2 < 65):
                            break
                        store32(arg0 + 24, 1)
                        break
                        break
                    store32(arg0 + 24, 1)
                    v5 = (arg0 + 20)
                    arg1 = 0
                    break
                store32(v5, 0)
                break
            return arg1
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')
    return 3953

# ------------------------------------------------------------
# $func40
# ------------------------------------------------------------
def func40(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15):
    v16 = (G.global0 - 320)
    G.global0 = (G.global0 - 320)
    while True:  # block $label0
        if load8u(9142917):
            break
        if load8u(9142916):
            arg12 = 0
            arg14 = 0
            if (u(arg10) <= u(14)):
                arg10 = (arg10 << 4)
                arg14 = ((((load32(((arg10 << 4) + 1748)) << 8) + load32((arg10 + 1744))) + (load32((arg10 + 1752)) << 16)) + (load32((arg10 + 1756)) << 24))
            while True:  # block $label1
                if (arg9 == 0):
                    break
                if (load32(arg9 + 20) == 0):
                    break
                arg10 = load32(arg9 + 28)
                if (load32(arg9 + 28) == 2147483647):
                    arg10 = load32(59152)
                    store32(59152, (load32(59152) + 1))
                    v17 = load32(9568052)
                    store32(arg9 + 28, arg10)
                    v18 = load32(arg9)
                    arg12 = load32(arg9 + 4)
                    v19 = load32(9568048)
                    store32(9568048, (load32(9568048) + 1))
                    store32(((v19 << 2) + 9563952), arg9)
                    store32(9568052, (v17 + ((v18 * (arg12 + 2)) << 2)))
                    v17 = load32(9568056)
                    store32(arg9 + 56, load32(9568056))
                    store32(9568056, (v17 + ((arg12 * load32(arg9)) << 2)))
                arg12 = (arg10 + (arg13 << 16))
                break
            arg9 = (load32(9142848) * 25)
            if (arg2 > 0.0):
                # TODO: f32.convert_i32_u []
                arg2 = (((arg2 * 0.5) / (load32(9142440) * 96)) + 0.25)
            store32(v16 + 316, arg11)
            store64(v16 + 308, 65535)
            store32(v16 + 304, arg14)
            # TODO: f64.promote_f32 []
            store32(v16 + 296, arg8)
            store32(v16 + 292, arg9)
            store32(v16 + 288, arg12)
            # TODO: f64.promote_f32 []
            store32(v16 + 280, arg5)
            # TODO: f64.promote_f32 []
            store32(v16 + 272, arg4)
            # TODO: f64.promote_f32 []
            store32(v16 + 264, arg3)
            # TODO: f64.promote_f32 []
            store32(v16 + 256, arg2)
            # TODO: f64.promote_f32 []
            store32(v16 + 248, arg1)
            # TODO: f64.promote_f32 []
            store32(v16 + 240, arg0)
            a_b()
            break
        arg8 = (arg8 if (arg8 != 0.0) else -1.0)
        while True:  # block $label2
            if (((arg6 == 0.0) & (arg7 == 0.0)) == 0):
                arg6 = (-arg6)
                # TODO: f64.promote_f32 []
                break
            arg6 = float(load32(arg9))
            v17 = (load32(arg9 + 20) * load32(arg9 + 16))
            if ((load32(arg9 + 20) * load32(arg9 + 16)) == 0):
                break
            # TODO: f64.promote_f32 []
            break
        v26 = float((load32(arg9 + 4) // v17))
        store32(v16 + 224, arg11)
        # TODO: f64.promote_f32 []
        store32(v16 + 216, arg15)
        # TODO: f64.promote_f32 []
        store32(v16 + 208, arg8)
        store32(v16 + 200, v26)
        # TODO: f64.promote_f32 []
        store32(v16 + 192, arg6)
        a_b()
        v17 = load8u(9142916)
        arg6 = float(load32(arg9 + 12))
        arg7 = float(load32(arg9 + 8))
        while True:  # block $label3
            if (arg2 == -55.0):
                break
            if (v17 == 0):
                break
            # TODO: f32.convert_i32_u []
            arg2 = (((arg2 * 0.5) / (load32(9142440) * 96)) + 0.25)
            break
        store32(v16 + 184, arg11)
        # TODO: f64.promote_f32 []
        store32(v16 + 176, arg2)
        # TODO: f64.promote_f32 []
        store32(v16 + 168, (arg1 - (0.0 if v17 else arg6)))
        # TODO: f64.promote_f32 []
        store32(v16 + 160, (arg0 - (0.0 if v17 else arg7)))
        a_b()
        # TODO: f64.promote_f32 []
        v26 = arg5
        # TODO: f64.promote_f32 []
        v27 = arg4
        # TODO: f64.promote_f32 []
        v28 = arg3
        while True:  # block $label4
            if load8u(9142916):
                store32(v16 + 152, arg11)
                store32(v16 + 144, v26)
                store32(v16 + 136, v27)
                store32(v16 + 128, v28)
                a_b()
                break
            store32(v16 + 96, v26)
            store32(v16 + 112, arg11)
            # TODO: f32.convert_i32_u []
            # TODO: f64.promote_f32 []
            store32(v16 + 104, (load32(9142848) * 25))
            store32(v16 + 80, v28)
            store32(v16 + 88, v27)
            a_b()
            break
        if (arg14 == 0):
            v19 = load32(arg9 + 24)
        v22 = load32(arg9 + 16)
        v23 = load32(arg9 + 32)
        while True:  # block $label9
            while True:  # block $label7
                while True:  # block $label8
                    v24 = load32(arg9 + 20)
                    if load32(arg9 + 20):
                        v18 = load8u(9142916)
                        while True:  # block $label6
                            arg14 = load32(arg9 + 28)
                            if (load32(arg9 + 28) == 2147483647):
                                while True:  # block $label5
                                    if v18:
                                        arg14 = load32(59152)
                                        store32(59152, (load32(59152) + 1))
                                        v20 = load32(9568052)
                                        v21 = load32(arg9)
                                        break
                                    v21 = load32(arg9)
                                    v20 = load32(9568052)
                                    arg14 = ((load32(arg9) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                    break
                                store32(arg9 + 28, arg14)
                                v17 = load32(arg9 + 4)
                                v25 = load32(9568048)
                                store32(9568048, (load32(9568048) + 1))
                                store32(((v25 << 2) + 9563952), arg9)
                                store32(9568052, (((v21 * (v17 + 2)) << 2) + v20))
                                if (v18 == 0):
                                    break
                                arg10 = load32(9568056)
                                store32(arg9 + 56, load32(9568056))
                                store32(9568056, (arg10 + ((v17 * load32(arg9)) << 2)))
                                break
                            if v18:
                                break
                            v17 = load32(arg9 + 4)
                            break
                        # TODO: f32.convert_i32_u []
                        arg2 = (load32(9142848) * 25)
                        # TODO: i32.div_u []
                        # TODO: f32.convert_i32_u []
                        break
                    arg9 = 0
                    # TODO: f32.convert_i32_u []
                    arg2 = (load32(9142848) * 25)
                    if load8u(9142916):
                        break
                    break
                arg8 = 0.0
                store32(v16 + 16, arg10)
                # TODO: f32.convert_i32_u []
                # TODO: f64.promote_f32 []
                store32(v16 + 24, ((((200 if (v23 == 27) else (arg12 * 100)) + v22) << 16) + v19))
                store32(v16 + 32, arg11)
                # TODO: f64.promote_f32 []
                store32(v16 + 8, arg2)
                # TODO: f32.convert_i32_u []
                # TODO: f64.promote_f32 []
                store32(v16, (arg8 / load32(59156)))
                a_b()
                break
                break
            arg9 = (arg14 + (arg13 << 16))
            # TODO: f32.convert_i32_u []
            break
        arg2 = (load32(9142848) * 25)
        store32((v16 - -64), arg11)
        store32(v16 + 48, arg9)
        # TODO: f64.promote_f32 []
        store32(v16 + 56, arg2)
        a_b()
        break
    G.global0 = (v16 + 320)
    return (v16 + 48)

# ------------------------------------------------------------
# $func41
# ------------------------------------------------------------
def func41(arg0, arg1, arg2, arg3, arg4):
    v8 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label0
        v5 = load8u(9147125)
        if ((load8u(9142388) if load8u(9147125) else 0) == 0):
            v7 = ((arg2 + arg4) + 5)
            v6 = func26((-1 if (u(v7) > u(1073741823)) else (((arg2 + arg4) + 5) << 2)))
            store32(func26((-1 if (u(v7) > u(1073741823)) else (((arg2 + arg4) + 5) << 2))) + 16, arg4)
            store32(v6 + 12, arg2)
            store32(v6 + 8, arg0)
            store64(v6, 0)
            if arg2:
                # TODO: memory.copy []
            if arg4:
                # TODO: memory.copy []
            if (v5 == 0):
                store32(v8 + 4, v7)
                store32(v8, v6)
                break
            arg1 = load32((9142892 if load8u(9147212) else 41092))
            if (u(load32((9142892 if load8u(9147212) else 41092))) >= u(2)):
                arg0 = load32(9561692)
                v5 = 1
                while True:  # $label1
                    arg2 = load32((arg0 + (v5 * 286704)) + 284616)
                    if load32((arg0 + (v5 * 286704)) + 284616):
                        store32(v8 + 24, arg2)
                        store32(v8 + 20, v7)
                        store32(v8 + 16, v6)
                        arg0 = load32(9561692)
                    v5 = (v5 + 1)
                    if ((v5 + 1) != arg1):
                        continue
                    break
            break
        if load8u(9140304):
            break
        v9 = load32(9142384)
        while True:  # block $label2
            v5 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                v6 = load32(9561696)
                break
            v6 = (load32(9561708) + v5)
            store32(9561700, (load32(9561708) + v5))
            v7 = load32(9561696)
            v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
            if v5:
                # TODO: memory.copy []
            if v7:
                v5 = load32(9561704)
            store32(9561696, v6)
            break
        store32(9561704, (v5 + 1))
        store32((v6 + (v5 << 2)), v9)
        while True:  # block $label3
            v5 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                v7 = v6
                break
            v7 = (load32(9561708) + v5)
            store32(9561700, (load32(9561708) + v5))
            v7 = func26((-1 if (u(v7) > u(1073741823)) else (v7 << 2)))
            if v5:
                # TODO: memory.copy []
            store32(9561696, v7)
            v5 = load32(9561704)
            break
        store32(9561704, (v5 + 1))
        store32((v7 + (v5 << 2)), arg0)
        while True:  # block $label4
            v5 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                v6 = v7
                break
            arg0 = (load32(9561708) + v5)
            store32(9561700, (load32(9561708) + v5))
            v6 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if v5:
                # TODO: memory.copy []
            store32(9561696, v6)
            v5 = load32(9561704)
            break
        store32(9561704, (v5 + 1))
        store32((v6 + (v5 << 2)), arg2)
        while True:  # block $label5
            v5 = load32(9561704)
            if (load32(9561704) != load32(9561700)):
                arg0 = v6
                break
            arg0 = (load32(9561708) + v5)
            store32(9561700, (load32(9561708) + v5))
            arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if v5:
                # TODO: memory.copy []
            store32(9561696, arg0)
            v5 = load32(9561704)
            break
        store32(9561704, (v5 + 1))
        store32((arg0 + (v5 << 2)), arg4)
        if arg2:
            v6 = 0
            while True:  # $label6
                v9 = load32((arg1 + (v6 << 2)))
                v5 = load32(9561704)
                if (load32(9561704) == load32(9561700)):
                    v7 = (load32(9561708) + v5)
                    store32(9561700, (load32(9561708) + v5))
                    v7 = func26((-1 if (u(v7) > u(1073741823)) else (v7 << 2)))
                    if v5:
                        # TODO: memory.copy []
                    store32(9561696, v7)
                    v5 = load32(9561704)
                    arg0 = v7
                store32(9561704, (v5 + 1))
                store32((arg0 + (v5 << 2)), v9)
                v6 = (v6 + 1)
                if ((v6 + 1) != arg2):
                    continue
                break
        if (arg4 == 0):
            break
        v6 = 0
        while True:  # $label7
            arg2 = load32((arg3 + (v6 << 2)))
            v5 = load32(9561704)
            if (load32(9561704) == load32(9561700)):
                arg1 = (load32(9561708) + v5)
                store32(9561700, (load32(9561708) + v5))
                arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
                if v5:
                    # TODO: memory.copy []
                store32(9561696, arg1)
                v5 = load32(9561704)
                arg0 = arg1
            store32(9561704, (v5 + 1))
            store32((arg0 + (v5 << 2)), arg2)
            v6 = (v6 + 1)
            if ((v6 + 1) != arg4):
                continue
            break
        break
    G.global0 = (v8 + 32)

# ------------------------------------------------------------
# $func43
# ------------------------------------------------------------
def func43(arg0, arg1, arg2):
    while True:  # block $label0
        if (arg1 == 0):
            break
        v3 = (arg0 ^ -1)
        if (u(arg2) >= u(23)):
            while True:  # block $label1
                if ((arg1 & 3) == 0):
                    break
                v3 = (load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                v5 = (arg1 + 1)
                while True:  # block $label2
                    arg0 = (arg2 - 1)
                    if ((arg2 - 1) == 0):
                        break
                    if ((v5 & 3) == 0):
                        break
                    v3 = (load32(((((load8u(arg1 + 1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                    v5 = (arg1 + 2)
                    while True:  # block $label3
                        arg0 = (arg2 - 2)
                        if ((arg2 - 2) == 0):
                            break
                        if ((v5 & 3) == 0):
                            break
                        v3 = (load32(((((load8u(arg1 + 2) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                        v5 = (arg1 + 3)
                        while True:  # block $label4
                            arg0 = (arg2 - 3)
                            if ((arg2 - 3) == 0):
                                break
                            if ((v5 & 3) == 0):
                                break
                            v3 = (load32(((((load8u(arg1 + 3) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                            arg1 = (arg1 + 4)
                            arg2 = (arg2 - 4)
                            break
                            break
                        arg2 = arg0
                        arg1 = v5
                        break
                        break
                    arg2 = arg0
                    arg1 = v5
                    break
                    break
                arg2 = arg0
                arg1 = v5
                break
            # TODO: i32.div_u []
            arg0 = 20
            v11 = (20 * -20)
            while True:  # block $label5
                v10 = (arg0 - 1)
                if ((arg0 - 1) == 0):
                    break
                v5 = ((arg0 * 20) - 20)
                arg0 = arg1
                while True:  # $label6
                    v4 = (load32(arg0 + 16) ^ v9)
                    v9 = (load32((((((load32(arg0 + 16) ^ v9) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    v4 = (load32(arg0 + 12) ^ v8)
                    v8 = (load32((((((load32(arg0 + 12) ^ v8) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    v4 = (load32(arg0 + 8) ^ v6)
                    v6 = (load32((((((load32(arg0 + 8) ^ v6) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    v4 = (load32(arg0 + 4) ^ v7)
                    v7 = (load32((((((load32(arg0 + 4) ^ v7) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    v4 = (load32(arg0) ^ v3)
                    v3 = (load32((((((load32(arg0) ^ v3) & 0xFFFFFFFF) >> 22) & 1020) + 22320)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 14) & 1020) + 21296)) ^ (load32(((((v4 & 0xFFFFFFFF) >> 6) & 1020) + 20272)) ^ load32((((v4 & 255) << 2) + 19248)))))
                    arg0 = (arg0 + 20)
                    v10 = (v10 - 1)
                    if (v10 - 1):
                        continue
                    break
                arg1 = (arg1 + v5)
                break
            arg2 = (arg2 + v11)
            arg0 = (load32(arg1) ^ v3)
            arg0 = ((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8))
            arg0 = (((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8))
            arg0 = (((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8))
            arg0 = (((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8))
            arg0 = (((((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = ((((((((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg0 = (((((((((((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            v3 = ((((((((((((((load32(arg1 + 16) ^ (load32(((((((((((((((load32(arg1 + 12) ^ (load32(((((((((((((((load32(arg1 + 8) ^ (load32(((((((((((((((load32(arg1 + 4) ^ (load32((((((((((((((load32(arg1) ^ v3) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v7)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v6)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v8)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 255) << 2) + 18224)) ^ v9)) ^ ((arg0 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32((((arg0 & 255) << 2) + 18224)))
            arg1 = (arg1 + 20)
        if (u(arg2) > u(7)):
            while True:  # $label7
                arg0 = (load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                arg0 = ((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224)))
                arg0 = (((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224)))
                arg0 = ((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224)))
                arg0 = (((((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 4) ^ arg0) & 255) << 2) + 18224)))
                arg0 = ((((((((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 4) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 5) ^ arg0) & 255) << 2) + 18224)))
                arg0 = (((((((((((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 4) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 5) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 6) ^ arg0) & 255) << 2) + 18224)))
                v3 = ((((((((((((((((((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 1) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 2) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 3) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 4) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 5) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 6) ^ arg0) & 255) << 2) + 18224))) & 0xFFFFFFFF) >> 8) ^ load32(((((load8u(arg1 + 7) ^ arg0) & 255) << 2) + 18224)))
                arg1 = (arg1 + 8)
                arg2 = (arg2 - 8)
                if (u((arg2 - 8)) > u(7)):
                    continue
                break
        while True:  # block $label8
            if (arg2 == 0):
                break
            if (arg2 & 1):
                v3 = (load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                arg1 = (arg1 + 1)
            else:
            arg0 = arg2
            if (arg2 == 1):
                break
            while True:  # $label9
                arg2 = (load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8))
                v3 = (load32((((((load32(((((load8u(arg1) ^ v3) & 255) << 2) + 18224)) ^ ((v3 & 0xFFFFFFFF) >> 8)) ^ load8u(arg1 + 1)) & 255) << 2) + 18224)) ^ ((arg2 & 0xFFFFFFFF) >> 8))
                arg1 = (arg1 + 2)
                arg0 = (arg0 - 2)
                if (arg0 - 2):
                    continue
                break
            break
        break
    return (v3 ^ -1)

# ------------------------------------------------------------
# $func44
# ------------------------------------------------------------
def func44(arg0, arg1):
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if load32(arg0 + 92):
            break
        v2 = load32(9213808)
        if (u(load32(9213808)) > u(9999)):
            break
        if (load8u(arg0 + 125) == 3):
            break
        if (arg1 == 0):
            arg1 = load32(arg0 + 28)
            store32(9213808, (v2 + 1))
            store32(((v2 << 2) + 9173808), arg1)
        arg1 = 1
        while True:  # block $label1
            if (load8u(9142906) | load8u(9142916)):
                break
            arg1 = 0
            if load8u(9142917):
                break
            arg1 = load32(9299880)
            if load32(9299880):
                arg1 = (arg1 - 1)
                store32(9299880, (arg1 - 1))
                arg1 = load32((load32(9299872) + (arg1 << 2)))
                break
            arg1 = load32(9163776)
            v2 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v4 = load32(9163784)
            if (u(v2) < u(load32(9163784))):
                break
            store32(v3, v4)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        store32(arg0 + 92, arg1)
        if (load32(arg0 + 36) == 0):
        func203(arg0)
        break
    G.global0 = (v3 + 16)

# ------------------------------------------------------------
# $func45
# ------------------------------------------------------------
def func45():
    if load32(9213808):
        while True:  # $label0
            v1 = ((v0 << 2) + 9173808)
            func47((load32(9671128) + (load32(((v0 << 2) + 9173808)) * 132)))
            store32(v1, 0)
            v0 = (v0 + 1)
            if (u((v0 + 1)) < u(load32(9213808))):
                continue
            break
    v0 = 0
    store32(40604, -1)
    store32(9140316, 0)
    store32(9213808, 0)
    store32(9140320, 0)
    while True:  # block $label1
        if (load32(9142396) == 0):
            break
        while True:  # $label2
            func38(load32((load32(9142392) + (v0 << 2))))
            v0 = (v0 + 1)
            if (u((v0 + 1)) < u(load32(9142396))):
                continue
            break
        store32(9142396, 0)
        v0 = load32(9142392)
        if (load32(9142392) == 0):
            break
        break
    while True:  # block $label3
        if (load32(9671176) == 0):
            break
        if load32(9671192):
            v0 = 0
            while True:  # $label4
                func38(load32((load32(9671184) + (v0 << 2))))
                v0 = (v0 + 1)
                if (u((v0 + 1)) < u(load32(9671192))):
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

# ------------------------------------------------------------
# $func46
# ------------------------------------------------------------
def func46(arg0, arg1):
    v4 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    a_b()
    store32(9681836, 0)
    store8(9147141, 0)
    while True:  # block $label0
        v3 = load32(9671120)
        if (load32(9671120) == 0):
            break
        if (load8u(59186) == 0):
            while True:  # $label10
                v2 = load32(((v5 << 2) + 9263072))
                store8(load32(((v5 << 2) + 9263072)) + 20, 1)
                v9 = ((load32(v2 + 128) != 0) + v9)
                if (v6 == 0):
                    v7 = 0
                    while True:  # block $label9
                        while True:  # block $label1
                            v15 = load32(9215968)
                            if load32(9215968):
                                v16 = load32(9561692)
                                v17 = load32(9215960)
                                while True:  # $label8
                                    if load8u(v2 + 22):
                                        break
                                    v8 = (v16 + (load32((v17 + (v7 << 2))) * 286704))
                                    v6 = load32(v2 + 4)
                                    v18 = load8u(v2 + 23)
                                    while True:  # block $label2
                                        if load8u(v2 + 21):
                                            break
                                        while True:  # block $label4
                                            while True:  # block $label3
                                                if (v18 == 0):
                                                    break
                                                if (load32(((v6 * 404) + 9568096) + 264) != 3):
                                                    break
                                                if load32(((v8 + (v6 << 2)) + 281808)):
                                                    break
                                                break
                                            v21 = load32(v2 + 68)
                                            if (load32(v2 + 68) == 0):
                                                break
                                            v10 = 0
                                            v3 = 1
                                            v11 = 0
                                            v13 = 0
                                            while True:  # $label7
                                                v14 = load32((v2 + (v10 << 2)) + 28)
                                                v19 = load32(((load32((v2 + (v10 << 2)) + 28) * 404) + 9568096) + 264)
                                                v20 = (load32(((load32((v2 + (v10 << 2)) + 28) * 404) + 9568096) + 264) == 1)
                                                while True:  # block $label6
                                                    while True:  # block $label5
                                                        v14 = load32(((v8 + (v14 << 2)) + 281808))
                                                        if (load32(((v8 + (v14 << 2)) + 281808)) == 1):
                                                            break
                                                        v3 = ((v19 != 3) & v3)
                                                        if v14:
                                                            break
                                                        v3 = ((v19 != 0) & v3)
                                                        break
                                                        break
                                                    v13 = (v13 | v20)
                                                    break
                                                v11 = (v11 | v20)
                                                v10 = (v10 + 1)
                                                if ((v10 + 1) != v21):
                                                    continue
                                                break
                                            break
                                        if (((v3 & v13) if (v11 & 1) else v3) & 1):
                                            break
                                        if (u((load32(9671124) - 95)) > u(1)):
                                            break
                                        break
                                    if v18:
                                        if load8u(((v6 * 404) + 9568096) + 354):
                                            break
                                    v3 = ((v6 * 404) + 9568096)
                                    if (load32(((v6 * 404) + 9568096) + 264) == 1):
                                        if (u(func180(v8, v6)) >= u(load32(v3 + 204))):
                                            break
                                        v17 = load32(9215960)
                                        v16 = load32(9561692)
                                        v15 = load32(9215968)
                                    v7 = (v7 + 1)
                                    if (u((v7 + 1)) < u(v15)):
                                        continue
                                    break
                            break
                            break
                        store8(v2 + 20, 0)
                        break
                    v6 = load8u(59186)
                    v3 = load32(9671120)
                v5 = (v5 + 1)
                if (u((v5 + 1)) < u(v3)):
                    continue
                break
            break
        v2 = (v3 & 1)
        if (v3 != 1):
            v6 = (v3 & -2)
            v3 = 0
            while True:  # $label11
                v7 = (v5 << 2)
                v8 = load32(((v5 << 2) + 9263072))
                store8(load32(((v5 << 2) + 9263072)) + 20, 1)
                v8 = load32(v8 + 128)
                v7 = load32(((v7 | 4) + 9263072))
                store8(load32(((v7 | 4) + 9263072)) + 20, 1)
                v9 = ((v9 + (v8 != 0)) + (load32(v7 + 128) != 0))
                v5 = (v5 + 2)
                v3 = (v3 + 2)
                if ((v3 + 2) != v6):
                    continue
                break
        if (v2 == 0):
            break
        v2 = load32(((v5 << 2) + 9263072))
        store8(load32(((v5 << 2) + 9263072)) + 20, 1)
        v9 = (v9 + (load32(v2 + 128) != 0))
        break
    while True:  # block $label12
        v5 = load32(9147120)
        if (load32(9147120) == 0):
            break
        while True:  # $label14
            v2 = ((load32(9143000) * v5) + v12)
            if (u(((load32(9143000) * v5) + v12)) >= u(load32(9671120))):
                break
            while True:  # block $label13
                v2 = load32(((v2 << 2) + 9263072))
                if (load8u(load32(((v2 << 2) + 9263072)) + 23) == 0):
                    v6 = 0
                    break
                v5 = ((load32(v2 + 4) * 404) + 9568096)
                v6 = (load32(((load32(v2 + 4) * 404) + 9568096) + 264) == 3)
                break
            v5 = load8u(v5 + 354)
            v3 = load8u(v2 + 20)
            v7 = load32(v2 + 8)
            v8 = load8u(v2 + 24)
            v10 = load32(v2 + 12)
            v11 = load32(v2 + 124)
            v2 = load32(v2 + 128)
            store32(v4 + 32, 0)
            store32(v4 + 36, v5)
            store32(v4 + 40, v2)
            store32(v4 + 44, v6)
            store32(v4 + 48, v11)
            store32(v4 + 52, v9)
            store32(v4 + 56, v10)
            store32(v4 + 60, v8)
            store32(v4 + 20, v7)
            store32(v4 + 24, v3)
            store32(v4 + 16, v12)
            store32(v4 + 28, load32(((v12 << 2) + 9147392)))
            a_b()
            v12 = (v12 + 1)
            v5 = load32(9147120)
            if (u((v12 + 1)) < u(load32(9147120))):
                continue
            break
        break
    if arg1:
        store32(v4, load32(9143000))
        store32(v4 + 4, (arg0 if arg0 else load32(9671120)))
        a_b()
    store8(9684768, 0)
    G.global0 = (v4 - -64)
    return v4

# ------------------------------------------------------------
# $func47
# ------------------------------------------------------------
def func47(arg0):
    v2 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        if load8u(9142906):
            v3 = load32(arg0 + 40)
            if (load32(arg0 + 40) == 0):
                break
            v1 = load8u(arg0 + 127)
            v1 = (load8u(arg0 + 127) if v1 else 16)
            if load8u(9142916):
                if (u(v1) <= u(15)):
                    v1 = (v1 << 4)
                    v4 = ((((load32(((v1 << 4) + 1748)) << 8) + load32((v1 + 1744))) + (load32((v1 + 1752)) << 16)) + (load32((v1 + 1756)) << 24))
                store32(v2 + 36, v3)
                store32(v2 + 32, v4)
                a_b()
                break
            store32(v2 + 20, v3)
            store32(v2 + 16, v1)
            a_b()
            break
        if load8u(9142916):
            v1 = load32(arg0 + 40)
            if (load32(arg0 + 40) == 0):
                break
            v3 = load8u(arg0 + 125)
            store32(v2 + 4, v1)
            store32(v2, (v3 << 8))
            a_b()
            break
        while True:  # block $label1
            v1 = ((load8u(arg0 + 122) * 404) + 9568096)
            if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) != 1):
                break
            if (u(load32(v1 + 216)) < u(2)):
                break
            v4 = load32(arg0 + 12)
            if (load32(arg0 + 12) == 0):
                break
            v5 = load32(v4 + 8)
            if (load32(v4 + 8) == 0):
                break
            v1 = 0
            while True:  # $label3
                v3 = (load32(v4) + (v1 << 2))
                if (load32((load32(v4) + (v1 << 2)) + 4) == 1):
                    func38(load32(v3))
                    v4 = load32(arg0 + 12)
                    v5 = (load32(v4 + 8) - 2)
                    store32(load32(arg0 + 12) + 8, (load32(v4 + 8) - 2))
                    if (u(v1) < u(v5)):
                        v6 = load32(v4)
                        v3 = v1
                        while True:  # $label2
                            v5 = (v6 + (v3 << 2))
                            store32((v6 + (v3 << 2)), load32(v5 + 8))
                            v3 = (v3 + 1)
                            v5 = load32(v4 + 8)
                            if (u((v3 + 1)) < u(load32(v4 + 8))):
                                continue
                            break
                    v1 = (v1 - 2)
                v1 = (v1 + 2)
                if (u((v1 + 2)) < u(v5)):
                    continue
                break
            break
            break
        func38(load32(arg0 + 92))
        break
    store32(arg0 + 92, 0)
    while True:  # block $label4
        v1 = load32(arg0 + 80)
        if (load32(arg0 + 80) == 0):
            break
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) != 1):
            break
        func38(v1)
        store32(arg0 + 80, 0)
        break
    G.global0 = (v2 + 48)

# ------------------------------------------------------------
# $func48
# ------------------------------------------------------------
def func48(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        # TODO: i32.reinterpret_f32 []
        v3 = arg0
        v2 = (arg0 & 2147483647)
        if (u((arg0 & 2147483647)) <= u(1061752794)):
            if (u(v2) < u(964689920)):
                break
            # TODO: f64.promote_f32 []
            arg0 = func75(arg0)
            break
        if (u(v2) <= u(1081824209)):
            # TODO: f64.promote_f32 []
            v4 = arg0
            if (u(v2) <= u(1075235811)):
                if (v3 < 0):
                    arg0 = (-func76((v4 + 1.5707963267948966)))
                    break
                arg0 = func76((v4 + -1.5707963267948966))
                break
            arg0 = func75((-((-3.141592653589793 if (v3 >= 0) else 3.141592653589793) + v4)))
            break
        if (u(v2) <= u(1088565717)):
            if (u(v2) <= u(1085271519)):
                # TODO: f64.promote_f32 []
                v4 = arg0
                if (v3 < 0):
                    arg0 = func76((v4 + 4.71238898038469))
                    break
                arg0 = (-func76((v4 + -4.71238898038469)))
                break
            # TODO: f64.promote_f32 []
            arg0 = func75(((6.283185307179586 if (v3 < 0) else -6.283185307179586) + arg0))
            break
        if (u(v2) >= u(2139095040)):
            arg0 = (arg0 - arg0)
            break
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label2
                    while True:  # block $label1
                        # br_table[(func435(arg0, (v1 + 8)) & 3)]
                        break
                        break
                    arg0 = func75(load32(v1 + 8))
                    break
                    break
                arg0 = func76(load32(v1 + 8))
                break
                break
            arg0 = func75((-load32(v1 + 8)))
            break
            break
        arg0 = (-func76(load32(v1 + 8)))
        break
    G.global0 = (v1 + 16)
    return arg0

# ------------------------------------------------------------
# $func49
# ------------------------------------------------------------
def func49(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        # TODO: i32.reinterpret_f32 []
        v3 = arg0
        v2 = (arg0 & 2147483647)
        if (u((arg0 & 2147483647)) <= u(1061752794)):
            if (u(v2) < u(964689920)):
                break
            # TODO: f64.promote_f32 []
            break
        if (u(v2) <= u(1081824209)):
            if (u(v2) >= u(1075235812)):
                # TODO: f64.promote_f32 []
                break
            # TODO: f64.promote_f32 []
            v4 = arg0
            if (v3 < 0):
                break
            break
        if (u(v2) <= u(1088565717)):
            if (u(v2) >= u(1085271520)):
                # TODO: f64.promote_f32 []
                break
            if (v3 < 0):
                # TODO: f64.promote_f32 []
                break
            # TODO: f64.promote_f32 []
            break
        if (u(v2) >= u(2139095040)):
            break
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label2
                    while True:  # block $label1
                        # br_table[(func435(arg0, (v1 + 8)) & 3)]
                        break
                        break
                    break
                    break
                break
                break
            break
            break
        break
    arg0 = func75(load32(v1 + 8))
    G.global0 = (v1 + 16)
    return arg0

# ------------------------------------------------------------
# $func50
# ------------------------------------------------------------
def func50(arg0):
    while True:  # block $label1
        while True:  # block $label0
            v1 = load32(arg0 + 5820)
            if (load32(arg0 + 5820) == 16):
                v1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v1 + load32(arg0 + 8)), load8u(arg0 + 5816))
                v1 = load32(arg0 + 20)
                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                store8((v1 + load32(arg0 + 8)), load8u((arg0 + 5817)))
                store16(arg0 + 5816, 0)
                break
            if (v1 < 8):
                break
            v1 = load32(arg0 + 20)
            store32(arg0 + 20, (load32(arg0 + 20) + 1))
            store8((v1 + load32(arg0 + 8)), load8u(arg0 + 5816))
            store16(arg0 + 5816, load8u((arg0 + 5817)))
            break
        store32(0 + 5820, (load32(arg0 + 5820) - 8))
        break
    return arg0

# ------------------------------------------------------------
# $func52
# ------------------------------------------------------------
def func52(arg0, arg1):
    v2 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # block $label0
        if (load32(40600) == 0):
            break
        if (u(load32(9142868)) < u(490)):
            break
        v10 = load32(42160)
        v3 = load8u(9143020)
        v11 = (float(load32(9147148)) if load8u(9143020) else (load32(42160) * 12.0))
        v10 = (float(load32(9147144)) if v3 else (v10 * 174.0))
        if load8u(9142916):
            v10 = load32(9671164)
            v12 = (v10 * load32(9671164))
            v11 = (v11 * v10)
            v7 = load32(9142884)
            while True:  # block $label1
                v3 = load32(9142640)
                if (load32(9142640) == 0):
                    break
                if (load32(v3 + 20) == 0):
                    break
                v4 = load32(v3 + 28)
                if (load32(v3 + 28) == 2147483647):
                    v4 = load32(59152)
                    store32(59152, (load32(59152) + 1))
                    v5 = load32(9568052)
                    store32(v3 + 28, v4)
                    v8 = load32(v3)
                    v6 = load32(v3 + 4)
                    v9 = load32(9568048)
                    store32(9568048, (load32(9568048) + 1))
                    store32(((v9 << 2) + 9563952), v3)
                    store32(9568052, (v5 + ((v8 * (v6 + 2)) << 2)))
                    v5 = load32(9568056)
                    store32(v3 + 56, load32(9568056))
                    store32(9568056, (v5 + ((v6 * load32(v3)) << 2)))
                v4 = (v4 + (arg0 << 16))
                break
            store32(v2 + 76, v7)
            store32(v2 + 72, 0)
            store32(v2 + 68, (arg1 << 16))
            store32((v2 - -64), 0)
            store64(v2 + 56, 0)
            store32(v2 + 52, 0)
            store32(v2 + 48, v4)
            store64(v2 + 40, 0)
            store64(v2 + 32, 0)
            store64(v2 + 24, 0)
            store64(v2 + 16, -4590434657685733376)
            # TODO: f64.promote_f32 []
            store32(v2 + 8, v12)
            # TODO: f64.promote_f32 []
            store32(v2, v11)
            a_b()
            break
        v11 = load32(9671164)
        break
    G.global0 = (v2 + 80)

# ------------------------------------------------------------
# $func53
# ------------------------------------------------------------
def func53(arg0):
    v9 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    if load8u(9216068):
        v11 = load32(9561692)
        v10 = load32(9142872)
        v12 = (load32(9561692) + (load32(9142872) * 286704))
        v2 = 1
        while True:  # block $label3
            while True:  # block $label0
                v7 = ((arg0 * 132) + 9216080)
                if (load8u(((arg0 * 132) + 9216080) + 23) == 0):
                    break
                v2 = 0
                while True:  # block $label2
                    while True:  # block $label1
                        v1 = load32(v7 + 4)
                        # br_table[load32(((load32(v7 + 4) * 404) + 9568096) + 264)]
                        break
                        break
                    v2 = 1
                    break
                    break
                if load32(((v12 + (v1 << 2)) + 281808)):
                    break
                break
            v14 = load32(v7 + 68)
            if (load32(v7 + 68) == 0):
                break
            v1 = 1
            while True:  # block $label7
                if (v2 == 1):
                    v2 = 0
                    while True:  # $label6
                        v5 = load32((v7 + (v3 << 2)) + 28)
                        v8 = load32(((load32((v7 + (v3 << 2)) + 28) * 404) + 9568096) + 264)
                        v4 = (load32(((load32((v7 + (v3 << 2)) + 28) * 404) + 9568096) + 264) == 1)
                        while True:  # block $label5
                            while True:  # block $label4
                                v5 = load32(((v12 + (v5 << 2)) + 281808))
                                if (load32(((v12 + (v5 << 2)) + 281808)) == 1):
                                    break
                                v1 = ((v8 != 3) & v1)
                                if v5:
                                    break
                                v1 = ((v8 != 0) & v1)
                                break
                                break
                            v6 = (v4 | v6)
                            break
                        v2 = (v2 | v4)
                        v3 = (v3 + 1)
                        if ((v3 + 1) != v14):
                            continue
                        break
                    break
                v2 = 0
                while True:  # $label10
                    v5 = load32((v7 + (v3 << 2)) + 28)
                    v8 = load32(((load32((v7 + (v3 << 2)) + 28) * 404) + 9568096) + 264)
                    v4 = (load32(((load32((v7 + (v3 << 2)) + 28) * 404) + 9568096) + 264) == 1)
                    while True:  # block $label9
                        while True:  # block $label8
                            v5 = (v12 + (v5 << 2))
                            v5 = (load32(((v12 + (v5 << 2)) + 282828)) + load32((v5 + 281808)))
                            if ((load32(((v12 + (v5 << 2)) + 282828)) + load32((v5 + 281808))) == 1):
                                break
                            v1 = ((v8 != 3) & v1)
                            if v5:
                                break
                            v1 = ((v8 != 0) & v1)
                            break
                            break
                        v6 = (v4 | v6)
                        break
                    v2 = (v2 | v4)
                    v3 = (v3 + 1)
                    if ((v3 + 1) != v14):
                        continue
                    break
                break
            break
        v14 = (((v1 & v6) if (v2 & 1) else v1) & 1)
        while True:  # block $label11
            if (load8u(v7 + 23) == 0):
                v3 = -1
                v12 = 0
                v2 = 0
                break
            while True:  # block $label14
                while True:  # block $label13
                    while True:  # block $label12
                        v2 = load32(v7 + 4)
                        if (load32(v7 + 4) == load32(38604)):
                            break
                        if (load32(38608) == v2):
                            break
                        if (load32(38612) == v2):
                            break
                        if (load32(38616) == v2):
                            break
                        if (load32(38624) == v2):
                            break
                        if (load32(38628) == v2):
                            break
                        if (load32(38632) == v2):
                            break
                        if (load32(39056) != v2):
                            break
                        break
                    v13 = (v11 + (v10 * 286704))
                    v1 = ((v11 + (v10 * 286704)) + 282828)
                    v6 = (load32(9561044) << 2)
                    v7 = (load32(9561040) << 2)
                    v8 = (load32(9561048) << 2)
                    v4 = (load32(9561052) << 2)
                    v5 = (load32(9561056) << 2)
                    v16 = (load32(9561060) << 2)
                    v17 = (load32(9561064) << 2)
                    v15 = (load32(9561068) << 2)
                    v3 = (((((((load32((((v11 + (v10 * 286704)) + 282828) + (load32(9561044) << 2))) + load32((v1 + (load32(9561040) << 2)))) + load32((v1 + (load32(9561048) << 2)))) + load32((v1 + (load32(9561052) << 2)))) + load32((v1 + (load32(9561056) << 2)))) + load32((v1 + (load32(9561060) << 2)))) + load32((v1 + (load32(9561064) << 2)))) + load32((v1 + (load32(9561068) << 2))))
                    v1 = (v13 + 281808)
                    break
                    break
                v1 = ((v11 + (v10 * 286704)) + (v2 << 2))
                v3 = load32((((v11 + (v10 * 286704)) + (v2 << 2)) + 282828))
                break
            v16 = load32((v1 + 281808))
            v1 = ((v2 * 404) + 9568096)
            v17 = load8u(((v2 * 404) + 9568096) + 354)
            v13 = 0
            v7 = load32(v1 + 264)
            if (load32(v1 + 264) == 1):
                v14 = (v14 & (u(func180(v12, v2)) < u(load32(v1 + 204))))
                v7 = load32(v1 + 264)
            v12 = (v3 if (v7 == 1) else 0)
            while True:  # block $label15
                v5 = ((arg0 * 132) + 9216080)
                v15 = load32(((arg0 * 132) + 9216080) + 112)
                if (load32(((arg0 * 132) + 9216080) + 112) == 0):
                    v3 = -1
                    break
                v8 = 0
                v18 = load32(9671128)
                v3 = -1
                v19 = (v11 + (v10 * 286704))
                while True:  # $label20
                    while True:  # block $label16
                        v1 = load32(((v19 + (load32((v5 + (v8 << 2)) + 72) << 2)) + 284636))
                        if (load32(((v19 + (load32((v5 + (v8 << 2)) + 72) << 2)) + 284636)) == 0):
                            break
                        v20 = load32(v1 + 8)
                        if (load32(v1 + 8) == 0):
                            break
                        v21 = load32(v1)
                        v6 = 0
                        while True:  # $label19
                            while True:  # block $label17
                                v1 = load32((v21 + (v6 << 2)))
                                if (load32((v21 + (v6 << 2))) == 0):
                                    break
                                v1 = load32((v18 + (v1 * 132)) + 20)
                                if (load32((v18 + (v1 * 132)) + 20) == 0):
                                    break
                                v22 = load32(v1 + 8)
                                if (load32(v1 + 8) == 0):
                                    break
                                v23 = load32(v1)
                                v1 = 0
                                while True:  # $label18
                                    v4 = load32((v23 + (v1 << 2)))
                                    v24 = (u(v4) > u(2147483646))
                                    if (v2 == ((load32((v23 + (v1 << 2))) - 2147483647) if (u(v4) > u(2147483646)) else v4)):
                                        v12 = (v12 + (u(v4) < u(2147483647)))
                                        v13 = (v13 + v24)
                                        v3 = (v1 if (u(v1) < u(v3)) else v3)
                                    v1 = (v1 + 1)
                                    if ((v1 + 1) != v22):
                                        continue
                                    break
                                break
                            v6 = (v6 + 1)
                            if ((v6 + 1) != v20):
                                continue
                            break
                        break
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v15):
                        continue
                    break
                break
            while True:  # block $label21
                v1 = load32((v11 + (v10 * 286704)) + 281796)
                if (load32((v11 + (v10 * 286704)) + 281796) == 0):
                    break
                v10 = load32(v1 + 8)
                if (load32(v1 + 8) == 0):
                    break
                v4 = ((((v10 - 1) & 0xFFFFFFFF) >> 1) + 1)
                v8 = (((((v10 - 1) & 0xFFFFFFFF) >> 1) + 1) & 3)
                v11 = load32(v1)
                v6 = 0
                while True:  # block $label22
                    if (u(v10) < u(7)):
                        v1 = 0
                        break
                    v5 = (v4 & -4)
                    v1 = 0
                    v4 = 0
                    while True:  # $label23
                        v10 = (v1 << 2)
                        v13 = ((((v13 + (load32((v11 + ((v1 << 2) | 4))) == v2)) + (load32((v11 + (v10 | 12))) == v2)) + (load32((v11 + (v10 | 20))) == v2)) + (load32((v11 + (v10 | 28))) == v2))
                        v1 = (v1 + 8)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v5):
                            continue
                        break
                    break
                if (v8 == 0):
                    break
                while True:  # $label24
                    v13 = (v13 + (load32((v11 + ((v1 << 2) | 4))) == v2))
                    v1 = (v1 + 2)
                    v6 = (v6 + 1)
                    if ((v6 + 1) != v8):
                        continue
                    break
                break
            v2 = (v7 == 3)
            v15 = (v7 == 0)
            break
        v1 = (v7 == 1)
        store32(v9 + 36, v17)
        store32(v9 + 32, v1)
        store32(v9 + 28, v15)
        store32(v9 + 24, v2)
        store32(v9 + 20, v3)
        store32(v9 + 16, v13)
        store32(v9 + 12, v12)
        store32(v9 + 8, arg0)
        store32(v9 + 4, v16)
        store32(v9, v14)
        a_b()
    G.global0 = (v9 + 48)
    return v9

# ------------------------------------------------------------
# $func54
# ------------------------------------------------------------
def func54(arg0):
    v4 = load32(arg0 + 8)
    while True:  # block $label1
        while True:  # block $label0
            v2 = load32(arg0)
            if ((load32(arg0) & 15) == 0):
                v1 = (arg0 + 4)
                # TODO: i32.atomic.rmw.xchg []
                arg0 = 0
                break
            v3 = G.global3
            v5 = load32(arg0 + 4)
            if (load32(G.global3 + 24) != (load32(arg0 + 4) & 1073741823)):
                break
            while True:  # block $label2
                if ((v2 & 3) != 1):
                    break
                v1 = load32(arg0 + 20)
                if (load32(arg0 + 20) == 0):
                    break
                store32(arg0 + 20, (v1 - 1))
                return
                break
            v6 = (v2 & 128)
            if (v2 & 128):
                store32(v3 + 84, (arg0 + 16))
                # TODO: i32.atomic.rmw.add [('offset', 9689392)]
            v1 = (arg0 + 4)
            v7 = load32(arg0 + 12)
            arg0 = load32(arg0 + 16)
            store32(load32(arg0 + 12), load32(arg0 + 16))
            if ((v3 + 76) != arg0):
                store32((arg0 - 4), v7)
            # TODO: i32.atomic.rmw.xchg []
            arg0 = ((((v5 << 1) & (v2 << 29)) >> 31) & 2147483647)
            if (v6 == 0):
                break
            store32(v3 + 84, 0)
            while True:  # block $label3
                # TODO: i32.atomic.rmw.add [('offset', 9689392)]
                if (-1 != 1):
                    break
                if (load32(9689396) == 0):
                    break
                func111(9689392, 2147483647)
                break
            break
        if ((v4 == 0) & (arg0 >= 0)):
            break
        func97(v1)
        break

# ------------------------------------------------------------
# $func55
# ------------------------------------------------------------
def func55(arg0):
    while True:  # block $label0
        if (load8u(arg0) & 15):
            break
        # TODO: i32.atomic.rmw.cmpxchg []
        if 10:
            break
        return 0
        break
    while True:  # block $label6
        while True:  # block $label1
            v2 = load32(arg0)
            if ((load32(arg0) & 15) == 0):
                # TODO: i32.atomic.rmw.cmpxchg []
                if (10 == 0):
                    break
                v2 = load32(arg0)
            v1 = func185(arg0)
            if (func185(arg0) != 10):
                break
            v3 = (arg0 + 8)
            v4 = (arg0 + 4)
            v1 = 100
            while True:  # $label3
                while True:  # block $label2
                    if (v1 == 0):
                        break
                    if (load32(v4) == 0):
                        break
                    v1 = (v1 - 1)
                    if (load32(v3) == 0):
                        continue
                    break
                break
            v1 = func185(arg0)
            if (func185(arg0) != 10):
                break
            v5 = ((v2 ^ -1) & 128)
            v6 = ((v2 & 4) == 0)
            v2 = ((v2 & 3) != 2)
            while True:  # $label7
                while True:  # block $label4
                    v1 = load32(arg0 + 4)
                    v7 = (load32(arg0 + 4) & 1073741823)
                    if (((load32(arg0 + 4) & 1073741823) | ((v1 != 0) & v6)) == 0):
                        break
                    while True:  # block $label5
                        if v2:
                            break
                        if (v7 != load32(G.global3 + 24)):
                            break
                        break
                        break
                    # TODO: i32.atomic.rmw.add []
                    v1 = (v1 | -2147483648)
                    # TODO: i32.atomic.rmw.cmpxchg []
                    v1 = func434(v4, v1, v5)
                    # TODO: i32.atomic.rmw.sub []
                    if (v1 == 27):
                        break
                    if v1:
                        break
                    break
                v1 = func185(arg0)
                if (func185(arg0) == 10):
                    continue
                break
            break
        break
    return v1

# ------------------------------------------------------------
# $func56
# ------------------------------------------------------------
def func56(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    while True:  # block $label3
        while True:  # block $label2
            while True:  # block $label1
                while True:  # block $label0
                    v11 = load32(arg2 + 248)
                    # br_table[(load32(arg2 + 248) - 1)]
                    break
                    break
                return func282(arg0, arg1, arg2, arg4, arg5, arg6)
                break
            return func283(arg0, arg1, arg2, arg4, arg5, arg6, arg7)
            break
        while True:  # block $label10
            arg3 = arg0
            arg7 = arg2
            v12 = load32(arg2 + 216)
            v10 = load32(arg2 + 208)
            v9 = load32(arg2 + 372)
            while True:  # block $label6
                while True:  # block $label4
                    if (arg6 == 0):
                        break
                    if (v12 <= 0):
                        break
                    v14 = (load32(arg7 + 220) + arg1)
                    if ((load32(arg7 + 220) + arg1) <= arg1):
                        break
                    v17 = (arg3 + v12)
                    v15 = load32(9142440)
                    v18 = (load32(9142440) + 2)
                    v19 = ((load32(9142440) + 2) * v10)
                    v11 = load32(arg7 + 212)
                    arg8 = load32(9142840)
                    arg2 = arg3
                    while True:  # $label11
                        arg6 = (arg2 + 1)
                        v16 = (arg2 - arg3)
                        arg0 = arg1
                        v13 = arg1
                        while True:  # block $label8
                            if (u(arg2) < u(v15)):
                                while True:  # $label7
                                    while True:  # block $label5
                                        if (load8u((v9 + (v16 + ((arg0 - arg1) * v12)))) == 0):
                                            arg0 = (arg0 + 1)
                                            break
                                        v13 = 0
                                        if (u(arg0) >= u(v15)):
                                            break
                                        if ((arg0 | arg2) < 0):
                                            break
                                        arg0 = (arg0 + 1)
                                        if (load32((arg8 + ((arg6 + (((arg0 + 1) + v19) * v18)) << 2))) != v11):
                                            break
                                        break
                                    if (arg0 != v14):
                                        continue
                                    break
                                    break
                                raise RuntimeError('unreachable')
                            while True:  # $label9
                                if (load8u((v9 + (v16 + ((v13 - arg1) * v12)))) == 0):
                                    v13 = (v13 + 1)
                                    if (v14 != (v13 + 1)):
                                        continue
                                    break
                                break
                            break
                            break
                        arg2 = arg6
                        if (arg6 < v17):
                            continue
                        break
                    break
                v13 = 1
                if (arg4 == 0):
                    break
                if (v12 <= 0):
                    break
                v11 = (load32(arg7 + 220) + arg1)
                if ((load32(arg7 + 220) + arg1) <= arg1):
                    break
                arg8 = (arg3 + v12)
                arg0 = arg3
                while True:  # $label14
                    arg2 = (arg0 + 1)
                    arg7 = (arg0 - arg3)
                    arg6 = load32(9142840)
                    arg0 = arg1
                    while True:  # $label13
                        while True:  # block $label12
                            if (load8u((v9 + (arg7 + ((arg0 - arg1) * v12)))) == 0):
                                arg0 = (arg0 + 1)
                                break
                            arg0 = (arg0 + 1)
                            arg4 = (load32(9142440) + 2)
                            store32((arg6 + ((arg2 + (((arg0 + 1) + ((load32(9142440) + 2) * v10)) * arg4)) << 2)), arg5)
                            break
                        if (arg0 != v11):
                            continue
                        break
                    arg0 = arg2
                    if (arg2 < arg8):
                        continue
                    break
                break
            break
        return v13
        break
    arg7 = load32(arg2 + 208)
    if (load32(arg2 + 208) == 0):
        while True:  # block $label21
            arg3 = arg0
            arg7 = arg2
            v9 = load32(arg2 + 216)
            v14 = load32(arg2 + 372)
            while True:  # block $label17
                while True:  # block $label15
                    if (arg6 == 0):
                        break
                    if (v9 <= 0):
                        break
                    v16 = (load32(arg7 + 220) + arg1)
                    if ((load32(arg7 + 220) + arg1) <= arg1):
                        break
                    v11 = (arg3 + v9)
                    v17 = load32(9142440)
                    v15 = (load32(9142440) + 2)
                    arg8 = load32(9671128)
                    v18 = load32(9142840)
                    arg2 = arg3
                    while True:  # $label22
                        arg6 = (arg2 + 1)
                        v19 = (arg2 - arg3)
                        arg0 = arg1
                        v10 = arg1
                        while True:  # block $label19
                            if (u(arg2) < u(v17)):
                                while True:  # $label18
                                    while True:  # block $label16
                                        if (load8u((v14 + (v19 + ((arg0 - arg1) * v9)))) == 0):
                                            arg0 = (arg0 + 1)
                                            break
                                        v10 = 0
                                        if (u(arg0) >= u(v17)):
                                            break
                                        if ((arg0 | arg2) < 0):
                                            break
                                        arg0 = (arg0 + 1)
                                        if load32((v18 + (((v15 * (arg0 + 1)) + arg6) << 2))):
                                            break
                                        if (load32(((load8u((arg8 + (load32((v18 + ((((arg0 + v15) * v15) + arg6) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1):
                                            break
                                        break
                                    if (arg0 != v16):
                                        continue
                                    break
                                    break
                                raise RuntimeError('unreachable')
                            while True:  # $label20
                                if (load8u((v14 + (v19 + ((v10 - arg1) * v9)))) == 0):
                                    v10 = (v10 + 1)
                                    if (v16 != (v10 + 1)):
                                        continue
                                    break
                                break
                            break
                            break
                        arg2 = arg6
                        if (arg6 < v11):
                            continue
                        break
                    break
                v10 = 1
                if (arg4 == 0):
                    break
                if (v9 <= 0):
                    break
                arg8 = (load32(arg7 + 220) + arg1)
                if ((load32(arg7 + 220) + arg1) <= arg1):
                    break
                arg7 = (arg3 + v9)
                arg0 = arg3
                while True:  # $label25
                    arg2 = (arg0 + 1)
                    arg6 = (arg0 - arg3)
                    arg4 = load32(9142840)
                    arg0 = arg1
                    while True:  # $label24
                        while True:  # block $label23
                            if (load8u((v14 + (arg6 + ((arg0 - arg1) * v9)))) == 0):
                                arg0 = (arg0 + 1)
                                break
                            arg0 = (arg0 + 1)
                            store32((arg4 + ((arg2 + ((arg0 + 1) * (load32(9142440) + 2))) << 2)), arg5)
                            break
                        if (arg0 != arg8):
                            continue
                        break
                    arg0 = arg2
                    if (arg2 < arg7):
                        continue
                    break
                break
            break
        return v10
    while True:  # block $label28
        while True:  # block $label27
            while True:  # block $label26
                # br_table[(v11 - 4)]
                break
                break
            return func193(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg8)
            break
        return func194(arg0, arg1, arg2, arg3, arg4, arg5, arg6)
        break
    if (u(arg7) <= u(2)):
    else:
    return 0

# ------------------------------------------------------------
# $func57
# ------------------------------------------------------------
def func57(arg0):
    v10 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    if (load8u(9142917) == 0):
        store32(9143000, arg0)
        store32(9671120, 0)
        store32(9263840, 0)
        v11 = load32(9671128)
        v7 = load32(9561692)
        v12 = load32(9142872)
        v5 = (load32(9561692) + (load32(9142872) * 286704))
        while True:  # $label4
            while True:  # block $label0
                v1 = load32(((v5 + (v3 << 2)) + 284636))
                if (load32(((v5 + (v3 << 2)) + 284636)) == 0):
                    break
                v6 = load32(v1 + 8)
                if (load32(v1 + 8) == 0):
                    break
                v8 = load32(v1)
                v1 = 0
                if (v6 != 1):
                    v13 = (v6 & -2)
                    v4 = 0
                    while True:  # $label3
                        while True:  # block $label1
                            v9 = (v1 << 2)
                            v14 = load32((v8 + (v1 << 2)))
                            if (load32((v8 + (v1 << 2))) == 0):
                                break
                            v14 = load32((v11 + (v14 * 132)) + 24)
                            if (load32((v11 + (v14 * 132)) + 24) == 0):
                                break
                            v2 = ((load32(v14 + 8) != 0) | v2)
                            break
                        while True:  # block $label2
                            v9 = load32((v8 + (v9 | 4)))
                            if (load32((v8 + (v9 | 4))) == 0):
                                break
                            v9 = load32((v11 + (v9 * 132)) + 24)
                            if (load32((v11 + (v9 * 132)) + 24) == 0):
                                break
                            v2 = ((load32(v9 + 8) != 0) | v2)
                            break
                        v1 = (v1 + 2)
                        v4 = (v4 + 2)
                        if ((v4 + 2) != v13):
                            continue
                        break
                if ((v6 & 1) == 0):
                    break
                v1 = load32((v8 + (v1 << 2)))
                if (load32((v8 + (v1 << 2))) == 0):
                    break
                v1 = load32((v11 + (v1 * 132)) + 24)
                if (load32((v11 + (v1 * 132)) + 24) == 0):
                    break
                v2 = ((load32(v1 + 8) != 0) | v2)
                break
            v3 = (v3 + 1)
            if ((v3 + 1) != 255):
                continue
            break
        v1 = 1
        store32(9671120, 1)
        store8(9262828, 1)
        store32(9263072, 9262808)
        v3 = (((load32((v7 + (v12 * 286704)) + 283936) != 0) | v2) & 1)
        store8(9256756, (((load32((v7 + (v12 * 286704)) + 283936) != 0) | v2) & 1))
        v6 = load8u(9143020)
        if (v3 if load8u(9143020) else 1):
            store32(9671120, 2)
            store32(9263076, 9256736)
            v1 = 2
        v3 = load32((((v7 + (v12 * 286704)) + (load32(38428) << 2)) + 281808))
        store8(9256888, (load32((((v7 + (v12 * 286704)) + (load32(38428) << 2)) + 281808)) != 0))
        while True:  # block $label6
            while True:  # block $label5
                if v3:
                    break
                if (v6 == 0):
                    break
                v2 = v1
                break
                break
            v2 = (v1 + 1)
            store32(9671120, (v1 + 1))
            store32(((v1 << 2) + 9263072), 9256868)
            break
        v4 = 0
        while True:  # block $label15
            while True:  # block $label14
                while True:  # block $label13
                    while True:  # block $label12
                        while True:  # block $label9
                            while True:  # $label11
                                while True:  # block $label7
                                    v3 = ((v4 * 404) + 9568096)
                                    if (load32(((v4 * 404) + 9568096) + 264) != 2):
                                        break
                                    if (u(load32(v3 + 268)) > u(2)):
                                        break
                                    v3 = load32(((v7 + (v4 << 2)) + 284636))
                                    if (load32(((v7 + (v4 << 2)) + 284636)) == 0):
                                        break
                                    v8 = load32(v3 + 8)
                                    if (load32(v3 + 8) == 0):
                                        break
                                    v3 = load32(v3)
                                    v1 = 0
                                    while True:  # $label10
                                        while True:  # block $label8
                                            v5 = load32((v3 + (v1 << 2)))
                                            if (load32((v3 + (v1 << 2))) == 0):
                                                break
                                            v5 = load32((v11 + (v5 * 132)) + 36)
                                            if (load32((v11 + (v5 * 132)) + 36) == 0):
                                                break
                                            if (v12 == load16u((v11 + (v5 * 132)) + 110)):
                                                break
                                            break
                                        v1 = (v1 + 1)
                                        if ((v1 + 1) != v8):
                                            continue
                                        break
                                    break
                                v4 = (v4 + 1)
                                if ((v4 + 1) != 255):
                                    continue
                                break
                            store8(9257020, 0)
                            if v6:
                                store8(9257152, 0)
                                v1 = v2
                                break
                            store8(9257152, 0)
                            store32(((v2 << 2) + 9263072), 9257000)
                            v1 = (v2 + 1)
                            break
                            break
                        v1 = (v2 + 1)
                        store32(9671120, (v2 + 1))
                        store8(9257020, 1)
                        store8(9257152, 0)
                        store32(((v2 << 2) + 9263072), 9257000)
                        if (v6 == 0):
                            break
                        break
                    v3 = load32(9142912)
                    store8(9257284, (load32(9142912) != 0))
                    if v3:
                        break
                    v3 = v1
                    if v6:
                        break
                    break
                    break
                store32(((v1 << 2) + 9263072), 9257132)
                store8(9257284, (load32(9142912) != 0))
                v1 = (v1 + 1)
                break
            v3 = (v1 + 1)
            store32(9671120, (v1 + 1))
            store32(((v1 << 2) + 9263072), 9257264)
            break
        v2 = 0
        v8 = load32(9215884)
        while True:  # block $label16
            v4 = (v7 + (v12 * 286704))
            v1 = load32(((v7 + (v12 * 286704)) + 284676))
            if (load32(((v7 + (v12 * 286704)) + 284676)) == 0):
                break
            v5 = load32(v1 + 8)
            if (load32(v1 + 8) == 0):
                break
            v13 = load32(v1)
            v1 = 0
            while True:  # $label18
                while True:  # block $label17
                    v2 = load32((v13 + (v1 << 2)))
                    if (load32((v13 + (v1 << 2))) == 0):
                        break
                    v2 = (v11 + (v2 * 132))
                    if (load8u((v11 + (v2 * 132)) + 122) != 10):
                        break
                    v9 = load32(v2 + 44)
                    if (((load32((v8 + (load32(v2 + 44) << 4)) + 4) == 22) | (v9 == 0)) == 0):
                        break
                    if load8u(v2 + 125):
                        break
                    if load32(v2 + 36):
                        break
                    if (load8u(v2 + 129) == 10):
                        break
                    v2 = 1
                    break
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v5):
                    continue
                break
            v2 = 0
            break
        while True:  # block $label19
            v1 = load32((v4 + 284952))
            if (load32((v4 + 284952)) == 0):
                break
            v5 = load32(v1 + 8)
            if (load32(v1 + 8) == 0):
                break
            v13 = load32(v1)
            v1 = 0
            while True:  # $label21
                while True:  # block $label20
                    v4 = load32((v13 + (v1 << 2)))
                    if (load32((v13 + (v1 << 2))) == 0):
                        break
                    v4 = (v11 + (v4 * 132))
                    if (load8u((v11 + (v4 * 132)) + 122) != 79):
                        break
                    v9 = load32(v4 + 44)
                    if (((load32((v8 + (load32(v4 + 44) << 4)) + 4) == 22) | (v9 == 0)) == 0):
                        break
                    if load8u(v4 + 125):
                        break
                    if load32(v4 + 36):
                        break
                    if (load8u(v4 + 129) == 10):
                        break
                    v2 = 1
                    break
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v5):
                    continue
                break
            break
        while True:  # block $label26
            while True:  # block $label24
                while True:  # block $label22
                    v1 = load32(((v7 + (v12 * 286704)) + 284892))
                    if (load32(((v7 + (v12 * 286704)) + 284892)) == 0):
                        break
                    v5 = load32(v1 + 8)
                    if (load32(v1 + 8) == 0):
                        break
                    v13 = load32(v1)
                    v1 = 0
                    while True:  # $label25
                        while True:  # block $label23
                            v4 = load32((v13 + (v1 << 2)))
                            if (load32((v13 + (v1 << 2))) == 0):
                                break
                            v4 = (v11 + (v4 * 132))
                            if (load8u((v11 + (v4 * 132)) + 122) != 64):
                                break
                            v9 = load32(v4 + 44)
                            if (((load32((v8 + (load32(v4 + 44) << 4)) + 4) == 22) | (v9 == 0)) == 0):
                                break
                            if load8u(v4 + 125):
                                break
                            if load32(v4 + 36):
                                break
                            if (load8u(v4 + 129) == 10):
                                break
                            store8(9257416, 1)
                            break
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != v5):
                            continue
                        break
                    break
                store8(9257416, v2)
                if ((v2 | (v6 == 0)) != 1):
                    break
                break
            v1 = (v3 + 1)
            store32(9671120, (v3 + 1))
            store32(((v3 << 2) + 9263072), 9257396)
            if v6:
                v3 = v1
                break
            v3 = (v3 + 2)
            store32(9671120, (v3 + 2))
            store8(9257548, 1)
            store32(((v1 << 2) + 9263072), 9257528)
            break
        v1 = 0
        v4 = load32(38764)
        v8 = load32(38456)
        v5 = (v7 + (v12 * 286704))
        while True:  # block $label31
            while True:  # block $label30
                while True:  # block $label28
                    while True:  # $label29
                        while True:  # block $label27
                            v2 = ((v1 * 404) + 9568096)
                            if load32(((v1 * 404) + 9568096) + 264):
                                break
                            if (load32(v2 + 268) == 1):
                                break
                            if (load32(v2 + 92) == 0):
                                break
                            if (v1 == v8):
                                break
                            if (v1 == v4):
                                break
                            if load32(((v5 + (v1 << 2)) + 281808)):
                                break
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                    store8(9261640, 0)
                    if (v6 == 0):
                        break
                    v2 = v3
                    break
                    break
                store8(9261640, 1)
                break
            v2 = (v3 + 1)
            store32(9671120, (v3 + 1))
            store32(((v3 << 2) + 9263072), 9261620)
            break
        while True:  # block $label33
            while True:  # block $label32
                v3 = (v7 + (v12 * 286704))
                if (load32((((v7 + (v12 * 286704)) + (v8 << 2)) + 281808)) == 0):
                    v3 = load32(((v3 + (v4 << 2)) + 281808))
                    store8(9261772, (load32(((v3 + (v4 << 2)) + 281808)) != 0))
                    if v3:
                        break
                    if (v6 == 0):
                        break
                    v1 = v2
                    break
                store8(9261772, 1)
                break
            v1 = (v2 + 1)
            store32(9671120, (v2 + 1))
            store32(((v2 << 2) + 9263072), 9261752)
            break
        while True:  # block $label36
            while True:  # block $label35
                while True:  # block $label34
                    v3 = (v7 + (v12 * 286704))
                    if load32((((v7 + (v12 * 286704)) + (load32(38440) << 2)) + 281808)):
                        break
                    if load32(((v3 + (load32(38772) << 2)) + 281808)):
                        break
                    v3 = load32((((v7 + (v12 * 286704)) + (load32(38928) << 2)) + 281808))
                    store8(9262432, (load32((((v7 + (v12 * 286704)) + (load32(38928) << 2)) + 281808)) != 0))
                    if v3:
                        break
                    if (v6 == 0):
                        break
                    v2 = v1
                    break
                    break
                store8(9262432, 1)
                break
            v2 = (v1 + 1)
            store32(9671120, (v1 + 1))
            store32(((v1 << 2) + 9263072), 9262412)
            break
        v3 = 0
        while True:  # block $label40
            while True:  # block $label39
                while True:  # block $label37
                    v1 = load32((((v7 + (v12 * 286704)) + (load32(38528) << 2)) + 284636))
                    if load32((((v7 + (v12 * 286704)) + (load32(38528) << 2)) + 284636)):
                        v5 = load32(v1 + 8)
                        if load32(v1 + 8):
                            v13 = load32(v1)
                            v1 = 0
                            v3 = 1
                            while True:  # $label38
                                v9 = load32((v13 + (v1 << 2)))
                                if load32((v13 + (v1 << 2))):
                                    if (u(load32((v11 + (v9 * 132)) + 80)) > u(449)):
                                        break
                                v1 = (v1 + 1)
                                v3 = (u((v1 + 1)) < u(v5))
                                if (v1 != v5):
                                    continue
                                break
                        store8(9262564, v3)
                        if (v6 == 0):
                            break
                        v3 = v2
                        break
                    store8(9262564, 0)
                    if (v6 == 0):
                        break
                    v3 = v2
                    break
                    break
                store8(9262564, (v3 & 1))
                break
            v3 = (v2 + 1)
            store32(9671120, (v2 + 1))
            store32(((v2 << 2) + 9263072), 9262544)
            break
        v1 = 0
        v11 = load32(38932)
        v5 = (v7 + (v12 * 286704))
        while True:  # block $label45
            while True:  # block $label44
                while True:  # block $label42
                    while True:  # $label43
                        while True:  # block $label41
                            if (load32(((v5 + (v1 << 2)) + 281808)) == 0):
                                break
                            v2 = ((v1 * 404) + 9568096)
                            if load32(((v1 * 404) + 9568096) + 264):
                                break
                            v13 = load32(v2 + 268)
                            if (load32(v2 + 268) == 1):
                                break
                            if (load32(v2 + 92) == 0):
                                break
                            if (v13 == 2):
                                break
                            if (v1 == v11):
                                break
                            if (v1 == v8):
                                break
                            if (v1 == v4):
                                break
                            if (load32(v2 + 224) > 1):
                                break
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                    store8(9262036, 0)
                    if (v6 == 0):
                        break
                    v2 = v3
                    break
                    break
                store8(9262036, 1)
                break
            v2 = (v3 + 1)
            store32(9671120, (v3 + 1))
            store32(((v3 << 2) + 9263072), 9262016)
            break
        v1 = 0
        v4 = load32(38704)
        v11 = load32(38752)
        v8 = load32(38776)
        v5 = load32(38696)
        v13 = load32(38692)
        v9 = load32(38756)
        v14 = load32(38496)
        v15 = load32(38452)
        v16 = (v7 + (v12 * 286704))
        while True:  # block $label50
            while True:  # block $label49
                while True:  # block $label47
                    while True:  # $label48
                        while True:  # block $label46
                            if (load32(((v16 + (v1 << 2)) + 281808)) == 0):
                                break
                            v3 = ((v1 * 404) + 9568096)
                            if load32(((v1 * 404) + 9568096) + 264):
                                break
                            if (load32(v3 + 268) == 1):
                                break
                            if (load32(v3 + 92) == 0):
                                break
                            if (v1 == v15):
                                break
                            if (v1 == v14):
                                break
                            if (v1 == v9):
                                break
                            if (v1 == v13):
                                break
                            if (v1 == v5):
                                break
                            if (v1 == v8):
                                break
                            if (v1 == v11):
                                break
                            if (v1 == v4):
                                break
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != 255):
                            continue
                        break
                    store8(9261904, 0)
                    if (v6 == 0):
                        break
                    v3 = v2
                    break
                    break
                store8(9261904, 1)
                break
            v3 = (v2 + 1)
            store32(9671120, (v2 + 1))
            store32(((v2 << 2) + 9263072), 9261884)
            break
        v1 = 0
        v7 = (v7 + (v12 * 286704))
        while True:  # block $label56
            while True:  # block $label55
                while True:  # block $label54
                    while True:  # block $label52
                        while True:  # $label53
                            while True:  # block $label51
                                if (load32(((v7 + (v1 << 2)) + 281808)) == 0):
                                    break
                                v2 = ((v1 * 404) + 9568096)
                                if load32(((v1 * 404) + 9568096) + 264):
                                    break
                                if (load32(v2 + 268) == 1):
                                    break
                                if (load32(v2 + 92) == 0):
                                    break
                                if (load32(v2 + 224) == 1):
                                    break
                                break
                            v1 = (v1 + 1)
                            if ((v1 + 1) != 255):
                                continue
                            break
                        store8(9262168, 0)
                        if v6:
                            v2 = v3
                            break
                        v2 = v3
                        break
                        break
                    v2 = (v3 + 1)
                    store32(9671120, (v3 + 1))
                    store8(9262168, 1)
                    store32(((v3 << 2) + 9263072), 9262148)
                    if (v6 == 0):
                        break
                    break
                store8(9257548, 1)
                break
            v1 = 9257528
            v3 = (v2 + 1)
            store32(9671120, (v2 + 1))
            store32(((v2 << 2) + 9263072), v1)
            v2 = v3
            break
        v1 = 0
        while True:  # block $label57
            v4 = load32(9147120)
            if (load32(9147120) == 0):
                break
            while True:  # $label58
                arg0 = load32(9143000)
                v2 = ((load32(9143000) * v4) + v1)
                if (((load32(9143000) * v4) + v1) == load32(9671120)):
                    break
                arg0 = load32(((v2 << 2) + 9263072))
                v3 = load8u(load32(((v2 << 2) + 9263072)) + 20)
                arg0 = load32(arg0 + 8)
                store64(v10 + 32, 0)
                store64(v10 + 40, 0)
                store64(v10 + 48, 0)
                store64(v10 + 56, 4294967295)
                store32(v10 + 20, arg0)
                store32(v10 + 24, v3)
                store32(v10 + 28, 0)
                store32(v10 + 16, v1)
                a_b()
                v1 = (v1 + 1)
                v4 = load32(9147120)
                if (u((v1 + 1)) < u(load32(9147120))):
                    continue
                break
            v2 = load32(9671120)
            arg0 = load32(9143000)
            break
        store32(v10 + 4, v2)
        store32(v10, arg0)
        a_b()
        store8(9684768, 1)
    G.global0 = (v10 - -64)
    return v10

# ------------------------------------------------------------
# $func58
# ------------------------------------------------------------
def func58(arg0, arg1):
    while True:  # block $label0
        if (arg0 == 0):
            break
        # TODO: i64.div_u []
        v3 = arg0
        while True:  # block $label1
            v4 = i64(arg1)
            arg0 = (i64(arg1) * arg0)
            if (u((i64(arg1) * arg0)) > u(4294967295)):
                break
            if (u(v3) < u(v4)):
                break
            if (arg0 == 0):
                break
            v2 = e()
            break
        return v2
        break
    a_c()
    raise RuntimeError('unreachable')
    return 5173

# ------------------------------------------------------------
# $func59
# ------------------------------------------------------------
def func59(arg0, arg1, arg2, arg3):
    v23 = ((load8u(arg2 + 122) * 404) + 9568096)
    v24 = 1
    while True:  # $label41
        while True:  # block $label38
            while True:  # block $label0
                v6 = load16u(arg2 + 112)
                v21 = (load16u(arg2 + 112) - v19)
                v5 = load32(v23 + 216)
                v8 = (v19 << 1)
                v25 = (v21 + (load32(v23 + 216) + (v19 << 1)))
                if ((load16u(arg2 + 112) - v19) >= (v21 + (load32(v23 + 216) + (v19 << 1)))):
                    break
                v7 = load16u(arg2 + 114)
                v22 = (load16u(arg2 + 114) - v19)
                v4 = load32(v23 + 220)
                v8 = (v22 + (v8 + load32(v23 + 220)))
                if ((load16u(arg2 + 114) - v19) >= (v22 + (v8 + load32(v23 + 220)))):
                    break
                v27 = (v25 - 1)
                v28 = (v8 - 1)
                v29 = ((v6 + v19) + v5)
                v30 = ((v7 + v19) + v4)
                v26 = 1
                v8 = v21
                while True:  # $label40
                    v5 = v22
                    while True:  # $label39
                        while True:  # block $label2
                            while True:  # block $label1
                                if (v8 == v21):
                                    break
                                if (v5 == v22):
                                    break
                                if (v5 == v28):
                                    break
                                if (v8 != v27):
                                    break
                                break
                            v11 = load32(9142440)
                            if (u(load32(9142440)) <= u(v5)):
                                break
                            if ((v5 | v8) < 0):
                                break
                            if (u(v8) >= u(v11)):
                                break
                            while True:  # block $label7
                                while True:  # block $label6
                                    while True:  # block $label3
                                        while True:  # block $label4
                                            while True:  # block $label5
                                                v4 = load32(arg3 + 248)
                                                # br_table[(load32(arg3 + 248) - 1)]
                                                break
                                                break
                                            v9 = load32(arg3 + 216)
                                            if (load32(arg3 + 216) <= 0):
                                                break
                                            v12 = (load32(arg3 + 220) + v5)
                                            if ((load32(arg3 + 220) + v5) <= v5):
                                                break
                                            v16 = (v8 + v9)
                                            v13 = load32(arg3 + 372)
                                            v17 = (v11 + 2)
                                            v18 = ((v11 + 2) * load32(arg3 + 208))
                                            v15 = load32(arg3 + 212)
                                            v20 = load32(9142840)
                                            v7 = v8
                                            while True:  # $label12
                                                v10 = (v7 + 1)
                                                v14 = (v7 - v8)
                                                v6 = v5
                                                v4 = v5
                                                while True:  # block $label9
                                                    if (u(v7) >= u(v11)):
                                                        while True:  # $label8
                                                            if load8u((v13 + (((v6 - v5) * v9) + v14))):
                                                                break
                                                            v6 = (v6 + 1)
                                                            if ((v6 + 1) != v12):
                                                                continue
                                                            break
                                                            break
                                                        raise RuntimeError('unreachable')
                                                    while True:  # $label11
                                                        while True:  # block $label10
                                                            if load8u((v13 + (((v4 - v5) * v9) + v14))):
                                                                if (u(v4) >= u(v11)):
                                                                    break
                                                                if ((v4 | v7) < 0):
                                                                    break
                                                                v4 = (v4 + 1)
                                                                if (load32((v20 + (((((v4 + 1) + v18) * v17) + v10) << 2))) == v15):
                                                                    break
                                                                break
                                                            v4 = (v4 + 1)
                                                            break
                                                        if (v4 != v12):
                                                            continue
                                                        break
                                                    break
                                                v7 = v10
                                                if (v10 < v16):
                                                    continue
                                                break
                                            break
                                            break
                                        v6 = load32(arg3 + 216)
                                        if (load32(arg3 + 216) <= 0):
                                            break
                                        v10 = (load32(arg3 + 220) + v5)
                                        if ((load32(arg3 + 220) + v5) <= v5):
                                            break
                                        v9 = (v6 + v8)
                                        v12 = (v11 + 2)
                                        v13 = ((v11 + 2) * load32(arg3 + 208))
                                        v14 = load32(9142840)
                                        v6 = v8
                                        while True:  # $label13
                                            if (u(v6) >= u(v11)):
                                                break
                                            v7 = (v6 + 1)
                                            v4 = v5
                                            while True:  # $label14
                                                if (v4 == v10):
                                                    v6 = v7
                                                    if (v7 < v9):
                                                        continue
                                                    break
                                                if (u(v4) >= u(v11)):
                                                    break
                                                if ((v4 | v6) < 0):
                                                    break
                                                v4 = (v4 + 1)
                                                if (u(load32((v14 + (((((v4 + 1) + v13) * v12) + v7) << 2)))) <= u(2)):
                                                    continue
                                                break
                                            break
                                        break
                                        break
                                    v9 = load32(arg3 + 216)
                                    if (load32(arg3 + 216) <= 0):
                                        break
                                    v16 = load32(arg3 + 220)
                                    if (load32(arg3 + 220) <= 0):
                                        break
                                    v17 = (v5 + v16)
                                    v31 = (v8 + v9)
                                    v18 = load32(arg3 + 372)
                                    v12 = (v11 + 2)
                                    v32 = ((v11 + 2) * load32(arg3 + 208))
                                    v13 = 0
                                    v14 = load32(9142840)
                                    v7 = 0
                                    v6 = v8
                                    while True:  # $label19
                                        v10 = (v6 + 1)
                                        v15 = (v6 - v8)
                                        v4 = v5
                                        while True:  # block $label17
                                            if (u(v6) < u(v11)):
                                                while True:  # $label16
                                                    while True:  # block $label15
                                                        if load8u((v18 + (((v4 - v5) * v9) + v15))):
                                                            if (u(v4) >= u(v11)):
                                                                break
                                                            if ((v4 | v6) < 0):
                                                                break
                                                            v4 = (v4 + 1)
                                                            v20 = load32((v14 + (((((v4 + 1) + v32) * v12) + v10) << 2)))
                                                            if (u(load32((v14 + (((((v4 + 1) + v32) * v12) + v10) << 2)))) > u(2)):
                                                                break
                                                            if (u(load32((v14 + (((v4 * v12) + v10) << 2)))) > u(2)):
                                                                break
                                                            if (u(load32((v14 + ((((v4 + v12) * v12) + v10) << 2)))) > u(2)):
                                                                break
                                                            v7 = ((v20 == 0) | v7)
                                                            v13 = (v13 + (v20 == 1))
                                                            break
                                                        v4 = (v4 + 1)
                                                        break
                                                    if (v4 < v17):
                                                        continue
                                                    break
                                                break
                                            while True:  # $label18
                                                if load8u((v18 + (((v4 - v5) * v9) + v15))):
                                                    break
                                                v4 = (v4 + 1)
                                                if ((v4 + 1) < v17):
                                                    continue
                                                break
                                            break
                                        v6 = v10
                                        if (v10 < v31):
                                            continue
                                        break
                                    if (((u(v13) >= u((((v9 * v16) // 2) - 1))) & v7) == 0):
                                        break
                                    break
                                    break
                                while True:  # block $label21
                                    v6 = load32(arg3 + 208)
                                    if load32(arg3 + 208):
                                        v7 = load16u(arg2 + 110)
                                        while True:  # block $label22
                                            while True:  # block $label20
                                                # br_table[(v4 - 4)]
                                                break
                                                break
                                            if (func193(v8, v5, arg3, v7, 0, 0, 1, 0) == 0):
                                                break
                                            break
                                            break
                                        if (u(v6) > u(2)):
                                            break
                                        v10 = load32(arg3 + 216)
                                        if (load32(arg3 + 216) <= 0):
                                            break
                                        v9 = (load32(arg3 + 220) + v5)
                                        if ((load32(arg3 + 220) + v5) <= v5):
                                            break
                                        v17 = (v8 + v10)
                                        v12 = load32(arg3 + 372)
                                        v13 = (v11 + 2)
                                        v18 = (v6 * (v11 + 2))
                                        v14 = load32(arg3 + 212)
                                        v16 = load32(9142840)
                                        v6 = v8
                                        v7 = v8
                                        if (load32(arg3 + 264) != 1):
                                            while True:  # $label27
                                                v7 = (v6 + 1)
                                                v15 = (v6 - v8)
                                                v4 = v5
                                                while True:  # block $label24
                                                    if (u(v6) >= u(v11)):
                                                        while True:  # $label23
                                                            if load8u((v12 + (((v4 - v5) * v10) + v15))):
                                                                break
                                                            v4 = (v4 + 1)
                                                            if ((v4 + 1) != v9):
                                                                continue
                                                            break
                                                            break
                                                        raise RuntimeError('unreachable')
                                                    while True:  # $label26
                                                        while True:  # block $label25
                                                            if load8u((v12 + (((v4 - v5) * v10) + v15))):
                                                                if (u(v4) >= u(v11)):
                                                                    break
                                                                if ((v4 | v6) < 0):
                                                                    break
                                                                v4 = (v4 + 1)
                                                                if (load32((v16 + (((((v4 + 1) + v18) * v13) + v7) << 2))) == v14):
                                                                    break
                                                                break
                                                            v4 = (v4 + 1)
                                                            break
                                                        if (v4 != v9):
                                                            continue
                                                        break
                                                    break
                                                v6 = v7
                                                if (v7 < v17):
                                                    continue
                                                break
                                                break
                                            raise RuntimeError('unreachable')
                                        while True:  # $label32
                                            v6 = (v7 + 1)
                                            v15 = (v7 - v8)
                                            v4 = v5
                                            while True:  # block $label29
                                                if (u(v7) >= u(v11)):
                                                    while True:  # $label28
                                                        if load8u((v12 + (((v4 - v5) * v10) + v15))):
                                                            break
                                                        v4 = (v4 + 1)
                                                        if ((v4 + 1) != v9):
                                                            continue
                                                        break
                                                        break
                                                    raise RuntimeError('unreachable')
                                                while True:  # $label31
                                                    while True:  # block $label30
                                                        if load8u((v12 + (((v4 - v5) * v10) + v15))):
                                                            if (u(v4) >= u(v11)):
                                                                break
                                                            if ((v4 | v7) < 0):
                                                                break
                                                            v4 = (v4 + 1)
                                                            if (load32((v16 + (((((v4 + 1) + v18) * v13) + v6) << 2))) != v14):
                                                                break
                                                            if (load32((v16 + (((v4 * v13) + v6) << 2))) == v14):
                                                                break
                                                            break
                                                        v4 = (v4 + 1)
                                                        break
                                                    if (v4 != v9):
                                                        continue
                                                    break
                                                break
                                            v7 = v6
                                            if (v6 < v17):
                                                continue
                                            break
                                        break
                                    v9 = load32(arg3 + 216)
                                    if (load32(arg3 + 216) <= 0):
                                        break
                                    v13 = (load32(arg3 + 220) + v5)
                                    if ((load32(arg3 + 220) + v5) <= v5):
                                        break
                                    v18 = (v8 + v9)
                                    v14 = load32(arg3 + 372)
                                    v12 = (v11 + 2)
                                    v15 = load32(9671128)
                                    v16 = load32(9142840)
                                    v7 = v8
                                    while True:  # $label37
                                        v10 = (v7 + 1)
                                        v17 = (v7 - v8)
                                        v6 = v5
                                        v4 = v5
                                        while True:  # block $label34
                                            if (u(v7) >= u(v11)):
                                                while True:  # $label33
                                                    if load8u((v14 + (((v6 - v5) * v9) + v17))):
                                                        break
                                                    v6 = (v6 + 1)
                                                    if ((v6 + 1) != v13):
                                                        continue
                                                    break
                                                    break
                                                raise RuntimeError('unreachable')
                                            while True:  # $label36
                                                while True:  # block $label35
                                                    if load8u((v14 + (((v4 - v5) * v9) + v17))):
                                                        if (u(v4) >= u(v11)):
                                                            break
                                                        if ((v4 | v7) < 0):
                                                            break
                                                        v4 = (v4 + 1)
                                                        if load32((v16 + ((((v4 + 1) * v12) + v10) << 2))):
                                                            break
                                                        if (load32(((load8u((v15 + (load32((v16 + ((((v4 + v12) * v12) + v10) << 2))) * 132)) + 122) * 404) + 9568096) + 264) != 1):
                                                            break
                                                        break
                                                    v4 = (v4 + 1)
                                                    break
                                                if (v4 != v13):
                                                    continue
                                                break
                                            break
                                        v7 = v10
                                        if (v10 < v18):
                                            continue
                                        break
                                    break
                                    break
                                if (func194(v8, v5, arg3, v7, 0, 0, 1) == 0):
                                    break
                                break
                            store32(arg0, v8)
                            store32(arg1, v5)
                            if v26:
                                break
                            break
                            break
                        v5 = (v5 + 1)
                        if ((v5 + 1) != v30):
                            continue
                        break
                    v8 = (v8 + 1)
                    v26 = ((v8 + 1) < v25)
                    if (v8 != v29):
                        continue
                    break
                break
            v19 = (v19 + 1)
            v24 = (u((v19 + 1)) < u(20))
            if (v19 != 20):
                continue
            break
        break
    return v24

# ------------------------------------------------------------
# $func60
# ------------------------------------------------------------
def func60(arg0, arg1):
    v4 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # block $label0
        v3 = load32(arg0 + 48)
        if (load32(arg0 + 48) == 0):
            break
        v2 = load32(arg0 + 40)
        if (load32(arg0 + 40) == 0):
            break
        # TODO: f32.convert_i32_u []
        v11 = (load16u(arg0 + 112) * 32.0)
        v13 = float(load32(v3 + 12))
        v14 = float(load32(v3 + 8))
        # TODO: f32.convert_i32_u []
        v12 = (load16u(arg0 + 114) * 32.0)
        v3 = ((load8u(arg0 + 122) * 404) + 9568096)
        v5 = load32(9142440)
        # TODO: f32.convert_i32_u []
        v10 = (((load16u(arg0 + 114) * 32.0) + ((1.0 if (load32(v3 + 264) == 4) else float(load32(((load8u(arg0 + 122) * 404) + 9568096) + 208))) * (load32(9142440) * 32.0))) * arg1)
        arg1 = (((load16u(arg0 + 114) * 32.0) + ((1.0 if (load32(v3 + 264) == 4) else float(load32(((load8u(arg0 + 122) * 404) + 9568096) + 208))) * (load32(9142440) * 32.0))) * arg1)
        while True:  # block $label1
            v3 = load8u(9142916)
            if (load8u(9142916) == 0):
                break
            if (v10 == -55.0):
                break
            # TODO: f32.convert_i32_u []
            arg1 = (((v10 * 0.5) / (v5 * 96)) + 0.25)
            break
        store32(v4 + 56, v2)
        # TODO: f64.promote_f32 []
        store32(v4 + 48, arg1)
        # TODO: f64.promote_f32 []
        store32(v4 + 40, (v12 - (0.0 if v3 else v13)))
        # TODO: f64.promote_f32 []
        store32(v4 + 32, (v11 - (0.0 if v3 else v14)))
        a_b()
        while True:  # block $label2
            if load8u(9142916):
                break
            v3 = load32(arg0 + 92)
            if (load32(arg0 + 92) == 0):
                break
            if load8u(9142906):
                break
            v2 = ((load8u(arg0 + 122) * 404) + 9568096)
            if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) == 1):
                if (u(load32(v2 + 216)) > u(1)):
                    break
            v2 = load32(9142448)
            v5 = load32(load32(9142448) + 12)
            v2 = load32(v2 + 8)
            # TODO: f64.promote_f32 []
            store32(v4 + 16, (v10 + -1.0))
            store32(v4 + 24, v3)
            # TODO: f64.promote_f32 []
            store32(v4, (v11 - float(v2)))
            # TODO: f64.promote_f32 []
            store32(v4 + 8, (v12 - float(v5)))
            a_b()
            break
        v3 = (G.global0 - 48)
        G.global0 = (G.global0 - 48)
        while True:  # block $label3
            v2 = load32(arg0 + 24)
            if (load32(arg0 + 24) == 0):
                break
            v5 = load32(v2 + 4)
            if (load32(v2 + 4) == 0):
                break
            if (load32(v5 + 8) == 0):
                break
            # TODO: f32.convert_i32_u []
            v10 = (load16u(arg0 + 112) * 32.0)
            # TODO: f32.convert_i32_u []
            arg1 = (load16u(arg0 + 114) * 32.0)
            v11 = ((load16u(arg0 + 114) * 32.0) + -44.0)
            # TODO: f32.convert_i32_u []
            arg1 = (load32(9142440) * 32.0)
            arg1 = (arg1 + ((load32(9142440) * 32.0) + arg1))
            v12 = ((arg1 + ((load32(9142440) * 32.0) + arg1)) * 0.5)
            while True:  # $label6
                v6 = ((v8 | 1) << 2)
                v2 = load32((((v8 | 1) << 2) + load32(v5)))
                if (load32((((v8 | 1) << 2) + load32(v5))) == 0):
                    v2 = 0
                    while True:  # block $label4
                        if load8u(9142917):
                            break
                        v2 = load32(9299880)
                        if load32(9299880):
                            v2 = (v2 - 1)
                            store32(9299880, (v2 - 1))
                            v2 = load32((load32(9299872) + (v2 << 2)))
                            break
                        v2 = load32(9163776)
                        v7 = (load32(9163776) + 1)
                        store32(9163776, (load32(9163776) + 1))
                        v9 = load32(9163784)
                        if (u(v7) < u(load32(9163784))):
                            break
                        store32(v3 + 32, v9)
                        a_b()
                        store32(9163784, (load32(9163784) + 40000))
                        break
                    v7 = (load16u(arg0 + 114) << 5)
                    # TODO: f32.convert_i32_u []
                    store32((load32(v5) + v6), v2)
                v6 = load8u(9142916)
                v7 = load32(9142584)
                v13 = float(load32(load32(9142584) + 12))
                v14 = float(load32(v7 + 8))
                while True:  # block $label5
                    if (arg1 == -55.0):
                        break
                    if (v6 == 0):
                        break
                    # TODO: f32.convert_i32_u []
                    break
                v15 = ((v12 / (load32(9142440) * 96)) + 0.25)
                store32(v3 + 24, v2)
                # TODO: f64.promote_f32 []
                store32(v3 + 16, v15)
                # TODO: f64.promote_f32 []
                store32(v3 + 8, (v11 - (0.0 if v6 else v13)))
                # TODO: f64.promote_f32 []
                store32(v3, (v10 - (0.0 if v6 else v14)))
                a_b()
                v8 = (v8 + 2)
                if (u((v8 + 2)) < u(load32(v5 + 8))):
                    continue
                break
            break
        G.global0 = (v3 + 48)
        break
    G.global0 = (v4 - -64)
    return v3

# ------------------------------------------------------------
# $func61
# ------------------------------------------------------------
def func61(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
    v23 = load32(load32(9142424) + 64)
    while True:  # block $label0
        if (arg0 == 3):
            if load8u(9216060):
                break
        v10 = load32(9142440)
        v18 = ((((load32(9142440) & 0xFFFFFFFF) >> 1) - 20) if v23 else v10)
        v26 = (((((((load32(9142440) & 0xFFFFFFFF) >> 1) - 20) if v23 else v10) * (arg1 * v18)) // 65536) if (arg2 == 1) else arg1)
        if ((((((((load32(9142440) & 0xFFFFFFFF) >> 1) - 20) if v23 else v10) * (arg1 * v18)) // 65536) if (arg2 == 1) else arg1) == 0):
            break
        v38 = float(v18)
        v27 = (arg7 != 2147483647)
        while True:  # $label18
            arg1 = load32(9147320)
            arg2 = load32(9147312)
            store32(9147320, load32(9147312))
            v11 = load32(9147316)
            store32(9147316, arg2)
            v10 = (arg1 ^ (arg1 << 11))
            arg1 = load32(9147324)
            arg1 = ((load32(9147324) << 11) ^ arg1)
            arg1 = ((arg2 ^ (((arg2 & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ arg1) & 0xFFFFFFFF) >> 8))) ^ arg1)
            v10 = ((((((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((((arg2 ^ (((arg2 & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ arg1) & 0xFFFFFFFF) >> 8))) ^ arg1) & 0xFFFFFFFF) >> 19)) ^ v10) ^ arg1)
            while True:  # block $label1
                if (arg8 == 0):
                    v14 = ((arg2 << 11) ^ arg2)
                    arg2 = ((v11 << 11) ^ v11)
                    arg2 = (((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v10)
                    v11 = (((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v10) & 0xFFFFFFFF) >> 19)) ^ v14) ^ arg2)
                    v13 = ((((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v10) & 0xFFFFFFFF) >> 19)) ^ v14) ^ arg2) % v18)
                    v12 = (arg2 % v18)
                    v19 = ((v10 % 7) - 3)
                    break
                store32(9147324, arg2)
                arg1 = ((arg1 << 11) ^ arg1)
                arg2 = ((arg2 << 11) ^ arg2)
                v11 = ((v11 << 11) ^ v11)
                v14 = (((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ v11) ^ v10)
                arg2 = (((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ v11) ^ v10) & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v14)
                v11 = (((((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ (((((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ v11) ^ v10) & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v14) & 0xFFFFFFFF) >> 19)) ^ arg1) ^ arg2)
                v19 = ((((((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ (((((((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8) ^ (((((((((v11 << 11) ^ v11) & 0xFFFFFFFF) >> 8) ^ ((v10 & 0xFFFFFFFF) >> 19)) ^ v11) ^ v10) & 0xFFFFFFFF) >> 19)) ^ arg2) ^ v14) & 0xFFFFFFFF) >> 19)) ^ arg1) ^ arg2) & 3)
                arg1 = (v14 % v18)
                v12 = (arg1 & 1)
                v13 = (0 if (arg1 & 1) else (v14 % v18))
                v12 = ((0 - v12) & arg1)
                arg1 = v10
                v10 = v14
                break
            v20 = (arg2 & 3)
            arg1 = ((arg1 << 11) ^ arg1)
            arg1 = (((((v11 & 0xFFFFFFFF) >> 19) ^ ((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8)) ^ v11) ^ arg1)
            v15 = ((((((v11 & 0xFFFFFFFF) >> 19) ^ ((((arg1 << 11) ^ arg1) & 0xFFFFFFFF) >> 8)) ^ v11) ^ arg1) % arg3)
            while True:  # block $label2
                if v27:
                    v14 = v11
                    v11 = arg2
                    arg2 = v10
                    break
                v14 = arg1
                arg1 = ((v10 << 11) ^ v10)
                arg1 = (arg1 ^ ((((((v10 << 11) ^ v10) & 0xFFFFFFFF) >> 8) ^ ((v14 & 0xFFFFFFFF) >> 19)) ^ arg1))
                break
            v24 = (((arg1 ^ ((((((v10 << 11) ^ v10) & 0xFFFFFFFF) >> 8) ^ ((v14 & 0xFFFFFFFF) >> 19)) ^ arg1)) % 3) + 1)
            store32(9147320, v14)
            store32(9147324, v11)
            store32(9147316, arg1)
            arg2 = ((arg2 << 11) ^ arg2)
            arg1 = ((arg1 ^ (((arg1 & 0xFFFFFFFF) >> 19) ^ ((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8))) ^ arg2)
            store32(9147312, ((arg1 ^ (((arg1 & 0xFFFFFFFF) >> 19) ^ ((((arg2 << 11) ^ arg2) & 0xFFFFFFFF) >> 8))) ^ arg2))
            v28 = ((arg1 % arg4) + arg6)
            if ((arg1 % arg4) + arg6):
                v14 = (arg5 + v15)
                v21 = ((arg5 + v15) << 1)
                v25 = (v14 * v14)
                v22 = 0
                while True:  # $label17
                    v13 = (v13 + v19)
                    v12 = (v12 + v20)
                    arg1 = load32(9142440)
                    while True:  # block $label3
                        while True:  # block $label4
                            if (arg9 == 0):
                                if (u(arg1) <= u(v13)):
                                    break
                                if ((v12 | v13) < 0):
                                    break
                                if (u(arg1) <= u(v12)):
                                    break
                                if (v22 % v24):
                                    break
                                arg1 = load32(9147324)
                                store32(9147324, load32(9147316))
                                arg2 = load32(9147320)
                                v10 = load32(9147312)
                                store32(9147320, load32(9147312))
                                arg1 = (arg1 ^ (arg1 << 11))
                                arg1 = ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1)
                                store32(9147316, ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1))
                                arg2 = (arg2 ^ (arg2 << 11))
                                arg2 = ((((((arg2 ^ (arg2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ arg1)
                                store32(9147312, ((((((arg2 ^ (arg2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ arg1))
                                v19 = ((arg2 % 7) - 3)
                                v20 = ((arg1 % 7) - 3)
                                break
                            while True:  # block $label5
                                if (u(arg1) <= u(v12)):
                                    v12 = (v12 % arg1)
                                    break
                                if (v12 >= 0):
                                    break
                                v12 = (arg1 - (v12 % arg1))
                                break
                            while True:  # block $label6
                                if (u(arg1) <= u(v13)):
                                    v13 = (v13 % arg1)
                                    break
                                if (v13 >= 0):
                                    break
                                v13 = (arg1 - (v13 % arg1))
                                break
                            if (v22 % v24):
                                break
                            arg1 = load32(9147324)
                            store32(9147324, load32(9147316))
                            arg2 = load32(9147320)
                            v10 = load32(9147312)
                            store32(9147320, load32(9147312))
                            arg1 = (arg1 ^ (arg1 << 11))
                            arg1 = ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1)
                            store32(9147316, ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1))
                            arg2 = (arg2 ^ (arg2 << 11))
                            arg2 = ((((((arg2 ^ (arg2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ arg1)
                            store32(9147312, ((((((arg2 ^ (arg2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ arg2) ^ arg1))
                            arg2 = ((v19 + (arg2 % 3)) - 1)
                            arg2 = (-3 if (arg2 <= -3) else ((v19 + (arg2 % 3)) - 1))
                            v19 = (3 if (arg2 >= 3) else (-3 if (arg2 <= -3) else ((v19 + (arg2 % 3)) - 1)))
                            arg1 = ((v20 + (arg1 % 3)) - 1)
                            arg1 = (-3 if (arg1 <= -3) else ((v20 + (arg1 % 3)) - 1))
                            v20 = (3 if (arg1 >= 3) else (-3 if (arg1 <= -3) else ((v20 + (arg1 % 3)) - 1)))
                            break
                        if v23:
                            arg1 = load32(9142416)
                            arg2 = load32(9142416)
                            if (arg1 == 0):
                                arg2 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                            v33 = func262(float(v13), float(v12))
                            # TODO: f32.demote_f64 []
                            v36 = sqrt(float(((v13 * v13) + (v12 * v12))))
                            if (sqrt(float(((v13 * v13) + (v12 * v12)))) >= v38):
                                break
                            # TODO: f32.demote_f64 []
                            v35 = v33
                            if (v33 < 0.0):
                                break
                            # TODO: f32.convert_i32_u []
                            v37 = (6.28318548 / (4 if (u(arg2) < u(3)) else (arg2 << (arg2 & 1))))
                            if ((6.28318548 / (4 if (u(arg2) < u(3)) else (arg2 << (arg2 & 1)))) < v35):
                                break
                            v39 = (v37 - v35)
                            v15 = 0
                            while True:  # $label13
                                arg2 = arg1
                                if (arg1 == 0):
                                    arg2 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                                if (u(v15) >= u((4 if (u(arg2) < u(3)) else (arg2 << (arg2 & 1))))):
                                    break
                                while True:  # block $label7
                                    # TODO: f32.convert_i32_u []
                                    v40 = ((v37 * v15) + (v39 if (v15 & 1) else v35))
                                    # TODO: f64.promote_f32 []
                                    arg2 = load32(9142440)
                                    # TODO: f64.convert_i32_u []
                                    v33 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                                    v34 = (((func49(((v37 * v15) + (v39 if (v15 & 1) else v35))) * v36) + 0.5) + ((load32(9142440) & 0xFFFFFFFF) >> 1))
                                    if (abs((((func49(((v37 * v15) + (v39 if (v15 & 1) else v35))) * v36) + 0.5) + ((load32(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0):
                                        break
                                    break
                                v16 = -2147483648
                                while True:  # block $label9
                                    while True:  # block $label8
                                        # TODO: f64.promote_f32 []
                                        v33 = (((func48(v40) * v36) + 0.5) + v33)
                                        if (abs((((func48(v40) * v36) + 0.5) + v33)) < 2147483648.0):
                                            break
                                        break
                                    v17 = -2147483648
                                    if (u(int(v33)) <= u(-2147483648)):
                                        break
                                    if (u(arg2) <= u(v16)):
                                        break
                                    if ((v16 | v17) < 0):
                                        break
                                    v11 = (v16 - v14)
                                    v29 = (v16 + v21)
                                    if ((v16 - v14) >= (v16 + v21)):
                                        break
                                    v10 = (v17 - v14)
                                    v30 = (v17 + v21)
                                    if ((v17 - v14) >= (v17 + v21)):
                                        break
                                    while True:  # $label12
                                        arg1 = (v11 - v16)
                                        v31 = (((v11 - v16) * arg1) - 1)
                                        arg2 = v10
                                        while True:  # $label11
                                            while True:  # block $label10
                                                arg1 = (arg2 - v17)
                                                if ((v31 + ((arg2 - v17) * arg1)) > v25):
                                                    break
                                                arg1 = load32(9142440)
                                                if (u(load32(9142440)) <= u(arg2)):
                                                    break
                                                if ((arg2 | v11) < 0):
                                                    break
                                                if (u(arg1) <= u(v11)):
                                                    break
                                                store8((load32(9147288) + ((arg1 * arg2) + v11)), arg0)
                                                break
                                            arg2 = (arg2 + 1)
                                            if ((arg2 + 1) != v30):
                                                continue
                                            break
                                        v11 = (v11 + 1)
                                        if ((v11 + 1) != v29):
                                            continue
                                        break
                                    arg1 = load32(9142416)
                                    break
                                v15 = (v15 + 1)
                                continue
                                break
                            raise RuntimeError('unreachable')
                        v11 = (v12 - v14)
                        v15 = (v12 + v21)
                        if ((v12 - v14) >= (v12 + v21)):
                            break
                        arg1 = (v13 - v14)
                        v16 = (v13 + v21)
                        if ((v13 - v14) >= (v13 + v21)):
                            break
                        while True:  # $label16
                            arg2 = (v11 - v12)
                            v17 = (((v11 - v12) * arg2) - 1)
                            arg2 = arg1
                            while True:  # $label15
                                while True:  # block $label14
                                    v10 = (arg2 - v13)
                                    if ((v17 + ((arg2 - v13) * v10)) > v25):
                                        break
                                    v10 = load32(9142440)
                                    if (u(load32(9142440)) <= u(arg2)):
                                        break
                                    if ((arg2 | v11) < 0):
                                        break
                                    if (u(v10) <= u(v11)):
                                        break
                                    store8((load32(9147288) + ((arg2 * v10) + v11)), arg0)
                                    break
                                arg2 = (arg2 + 1)
                                if ((arg2 + 1) != v16):
                                    continue
                                break
                            v11 = (v11 + 1)
                            if ((v11 + 1) != v15):
                                continue
                            break
                        break
                    v22 = (v22 + 1)
                    if (u((v22 + 1)) < u(v28)):
                        continue
                    break
            v32 = (v32 + 1)
            if ((v32 + 1) != v26):
                continue
            break
        break
    return arg2

# ------------------------------------------------------------
# $func62
# ------------------------------------------------------------
def func62(arg0, arg1, arg2, arg3):
    v4 = load16u(arg0 + 114)
    while True:  # block $label1
        while True:  # block $label0
            v5 = load16u(arg0 + 112)
            if (load16u(arg0 + 112) != arg1):
                break
            if (arg2 > v4):
                break
            if (arg2 < v4):
                break
            v4 = (arg2 != v4)
            break
            break
        v4 = (1 if (arg2 > v4) else (-1 if (arg2 < v4) else 0))
        break
    arg1 = (1 if (arg1 > v5) else (-1 if (arg1 < v5) else 0))
    arg2 = 6
    arg1 = (((v4 * 3) + arg1) + 4)
    if (u((((v4 * 3) + arg1) + 4)) <= u(8)):
    else:
    store8(load8u((arg1 + 10184)) + 124, 6)
    while True:  # block $label3
        while True:  # block $label2
            arg1 = load8u(arg0 + 122)
            arg2 = load32(((load8u(arg0 + 122) * 72) + 9263856) + 12)
            if (load32(((load8u(arg0 + 122) * 72) + 9263856) + 12) == 0):
                if (load32(38588) != arg1):
                    break
                arg2 = load32(((arg1 * 72) + 9263856) + 8)
                if (load32(((arg1 * 72) + 9263856) + 8) == 0):
                    break
            if arg3:
                break
            arg0 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 276)
            func63(func37(arg0, arg2, 0.0, 0), arg0, 10, 0, (load32(((load8u(arg0 + 122) * 404) + 9568096) + 276) if arg0 else 25))
            return arg0
            break
        func29(arg0, 1)
        break
    return 0

# ------------------------------------------------------------
# $func63
# ------------------------------------------------------------
def func63(arg0, arg1, arg2, arg3, param4):
    v4 = load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        # call_indirect[v4]
    while True:  # block $label0
        if (load8u(arg0 + 125) == 3):
            break
        v5 = load32(arg0 + 44)
        if load32(arg0 + 44):
            v6 = load32(9142848)
            v4 = load32(9215884)
            store32((load32(9215884) + (v5 << 4)) + 4, arg1)
            store32((v4 + (load32(arg0 + 44) << 4)) + 8, load32(arg0 + 28))
            store32((v4 + (load32(arg0 + 44) << 4)) + 12, arg2)
            if arg3:
                # TODO: i32.div_u []
                store32(v6, (arg3 + 25))
                return
            store32((v4 + (load32(arg0 + 44) << 4)), load32(9142848))
            # call_indirect[load32(((arg1 * 40) + 9671200) + 20)]
            arg0 = (load32(9215884) + (load32(arg0 + 44) << 4))
            if (load32((load32(9215884) + (load32(arg0 + 44) << 4))) != load32(9142848)):
                break
            store32(arg0, 0)
            return
        store32(arg0 + 44, ((Ua(arg3, arg1, load32(arg0 + 28), arg2) & 0xFFFFFFFF) >> 2))
        break

# ------------------------------------------------------------
# $func65
# ------------------------------------------------------------
def func65(arg0, arg1):
    while True:  # block $label0
        if load8u(9147152):
            break
        v3 = load16u(arg0 + 114)
        v4 = load16u(arg0 + 112)
        while True:  # block $label1
            if (load8u(59181) == 0):
                break
            if (arg1 == 0):
                break
            arg1 = load32(arg0 + 44)
            if (load32(arg0 + 44) == 0):
                break
            v2 = load32(9215884)
            if (load32((load32(9215884) + (arg1 << 4)) + 12) == 1):
                break
            if (load8u(arg0 + 125) == 7):
                break
            if load32((v2 + ((arg1 << 4) | 4))):
                break
            arg1 = (load8u(arg0 + 124) << 3)
            v3 = (v3 - load32(((load8u(arg0 + 124) << 3) + 8996)))
            v4 = (v4 - load32((arg1 + 8992)))
            break
        arg1 = load32(9142872)
        if (load32(9142872) == 0):
            break
        if (load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(9142892) * arg1)))) == 0):
            break
        v5 = load8u(arg0 + 125)
        if (load8u(arg0 + 125) == 3):
            break
        arg0 = ((load8u(arg0 + 122) * 404) + 9568096)
        arg1 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 220)
        v2 = load32(arg0 + 216)
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label2
                    # br_table[(v5 - 4)]
                    break
                    break
                break
                break
            break
        arg0 = load32(arg0 + 200)
        if (load32(arg0 + 200) == 0):
            break
        if (load32(load32(9142424) + 48) == 0):
            break
        v5 = (load32(9142836) + (arg0 * 80))
        v6 = load32((load32(9142836) + (arg0 * 80)) + 324)
        if (load32((load32(9142836) + (arg0 * 80)) + 324) == 0):
            break
        v7 = (((arg1 & 0xFFFFFFFF) >> 1) + v3)
        v8 = (((v2 & 0xFFFFFFFF) >> 1) + v4)
        v9 = (arg0 * arg0)
        arg0 = 0
        while True:  # $label6
            while True:  # block $label5
                v10 = load32(9142440)
                v3 = load32(v5 + 320)
                v2 = (arg0 << 2)
                v4 = load32((load32(v5 + 320) + ((arg0 << 2) | 4)))
                arg1 = (v7 + load32((load32(v5 + 320) + ((arg0 << 2) | 4))))
                if (u(load32(9142440)) <= u((v7 + load32((load32(v5 + 320) + ((arg0 << 2) | 4)))))):
                    break
                v2 = load32((v2 + v3))
                v3 = (v8 + load32((v2 + v3)))
                if (u(v10) <= u((v8 + load32((v2 + v3))))):
                    break
                if ((arg1 | v3) < 0):
                    break
                if (v9 >= (((v2 * v2) + (v4 * v4)) - 1)):
                    break
                func258(v3, arg1)
                break
            arg0 = (arg0 + 2)
            if (u((arg0 + 2)) < u(v6)):
                continue
            break
        break
    return func129(v3, arg1, 1)

# ------------------------------------------------------------
# $func66
# ------------------------------------------------------------
def func66(arg0, arg1, arg2, arg3):
    v6 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # block $label0
        if (arg2 == 0):
            break
        if (load32(arg0 + 283908) != load32(9142872)):
            break
        while True:  # block $label1
            arg2 = load32(arg1)
            if (load32(arg1) == 0):
                break
            if (load32(v6 + 64) >= arg2):
                break
            store32(v6 + 48, 0)
            a_b()
            break
        while True:  # block $label2
            arg2 = load32(arg1 + 4)
            if (load32(arg1 + 4) == 0):
                break
            if (load32(v6 + 68) >= arg2):
                break
            store32(v6 + 32, 1)
            a_b()
            break
        while True:  # block $label3
            arg2 = load32(arg1 + 8)
            if (load32(arg1 + 8) == 0):
                break
            if (load32(v6 + 72) >= arg2):
                break
            store32(v6 + 16, 2)
            a_b()
            break
        arg2 = load32(arg1 + 12)
        if (load32(arg1 + 12) == 0):
            break
        if (load32(v6 + 76) >= arg2):
            break
        store32(v6, 3)
        a_b()
        break
    arg2 = 1
    while True:  # block $label4
        v4 = load32(arg1)
        if load32(arg1):
            if (load32(v6 + 64) < v4):
                break
        v5 = load32(arg1 + 4)
        if load32(arg1 + 4):
            if (load32(v6 + 68) < v5):
                break
        v5 = load32(arg1 + 8)
        if load32(arg1 + 8):
            if (load32(v6 + 72) < v5):
                break
        v5 = load32(arg1 + 12)
        if load32(arg1 + 12):
            if (load32(v6 + 76) < v5):
                break
        v10 = load32(9143016)
        while True:  # block $label5
            if (load32(v6 + 64) == 2147483647):
                break
            if (v4 == 0):
                break
            if arg3:
                arg2 = (arg0 + 281692)
                store32((arg0 + 281692), (load32(arg2) + v4))
                v4 = load32(arg1)
            arg2 = load32(arg0 + 283848)
            v5 = (v4 - load32(arg0 + 283848))
            if ((v4 - load32(arg0 + 283848)) <= 0):
                store32(arg0 + 283848, (arg2 - v4))
                break
            store32(arg0 + 283848, 0)
            arg2 = (arg0 + 281708)
            store32((arg0 + 281708), (load32(arg2) + v5))
            v4 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v7 = load32(9561692)
            arg2 = 1
            while True:  # $label7
                while True:  # block $label6
                    if (load8u((v10 + (load32(arg0 + 283908) + (arg2 * v4)))) & 1):
                        v8 = (v7 + (arg2 * 286704))
                        v9 = ((v7 + (arg2 * 286704)) + 283848)
                        v4 = load32(v8 + 283848)
                        if (v5 <= load32(v8 + 283848)):
                            break
                        v8 = (v8 + 281724)
                        store32((v8 + 281724), (load32(v8) + v4))
                        store32(v9, 0)
                        v5 = (v5 - v4)
                        v4 = load32(9142892)
                    arg2 = (arg2 + 1)
                    if (u((arg2 + 1)) < u(v4)):
                        continue
                    break
                    break
                break
            store32(v9, (v4 - v5))
            arg2 = ((v7 + (arg2 * 286704)) + 281724)
            store32(((v7 + (arg2 * 286704)) + 281724), (load32(arg2) + v5))
            break
        while True:  # block $label8
            if (load32(v6 + 68) == 2147483647):
                break
            arg2 = load32(arg1 + 4)
            if (load32(arg1 + 4) == 0):
                break
            if arg3:
                v4 = (arg0 + 281696)
                store32((arg0 + 281696), (load32(v4) + arg2))
                arg2 = load32(arg1 + 4)
            v4 = load32((arg0 + 283852))
            v5 = (arg2 - load32((arg0 + 283852)))
            if ((arg2 - load32((arg0 + 283852))) > 0):
                store32(arg0 + 283852, 0)
                arg2 = (arg0 + 281712)
                store32((arg0 + 281712), (load32(arg2) + v5))
                v4 = load32(9142892)
                if (u(load32(9142892)) < u(2)):
                    break
                v7 = load32(9561692)
                arg2 = 1
                while True:  # $label9
                    if (load8u((v10 + (load32(arg0 + 283908) + (arg2 * v4)))) & 2):
                        v9 = (v7 + (arg2 * 286704))
                        v8 = ((v7 + (arg2 * 286704)) + 283852)
                        v4 = load32(((v7 + (arg2 * 286704)) + 283852))
                        if (load32(((v7 + (arg2 * 286704)) + 283852)) >= v5):
                            store32(v8, (v4 - v5))
                            arg2 = ((v7 + (arg2 * 286704)) + 281728)
                            store32(((v7 + (arg2 * 286704)) + 281728), (load32(arg2) + v5))
                            break
                        v9 = (v9 + 281728)
                        store32((v9 + 281728), (load32(v9) + v4))
                        store32(v8, 0)
                        v5 = (v5 - v4)
                        v4 = load32(9142892)
                    arg2 = (arg2 + 1)
                    if (u((arg2 + 1)) < u(v4)):
                        continue
                    break
                break
            store32(arg0 + 283852, (v4 - arg2))
            break
        while True:  # block $label10
            if (load32(v6 + 72) == 2147483647):
                break
            arg2 = load32(arg1 + 8)
            if (load32(arg1 + 8) == 0):
                break
            if arg3:
                v4 = (arg0 + 281700)
                store32((arg0 + 281700), (load32(v4) + arg2))
                arg2 = load32(arg1 + 8)
            v4 = load32((arg0 + 283856))
            v5 = (arg2 - load32((arg0 + 283856)))
            if ((arg2 - load32((arg0 + 283856))) > 0):
                store32(arg0 + 283856, 0)
                arg2 = (arg0 + 281716)
                store32((arg0 + 281716), (load32(arg2) + v5))
                v4 = load32(9142892)
                if (u(load32(9142892)) < u(2)):
                    break
                v7 = load32(9561692)
                arg2 = 1
                while True:  # $label11
                    if (load8u((v10 + (load32(arg0 + 283908) + (arg2 * v4)))) & 4):
                        v9 = (v7 + (arg2 * 286704))
                        v8 = ((v7 + (arg2 * 286704)) + 283856)
                        v4 = load32(((v7 + (arg2 * 286704)) + 283856))
                        if (load32(((v7 + (arg2 * 286704)) + 283856)) >= v5):
                            store32(v8, (v4 - v5))
                            arg2 = ((v7 + (arg2 * 286704)) + 281732)
                            store32(((v7 + (arg2 * 286704)) + 281732), (load32(arg2) + v5))
                            break
                        v9 = (v9 + 281732)
                        store32((v9 + 281732), (load32(v9) + v4))
                        store32(v8, 0)
                        v5 = (v5 - v4)
                        v4 = load32(9142892)
                    arg2 = (arg2 + 1)
                    if (u((arg2 + 1)) < u(v4)):
                        continue
                    break
                break
            store32(arg0 + 283856, (v4 - arg2))
            break
        arg2 = 0
        if (load32(v6 + 76) == 2147483647):
            break
        v4 = load32(arg1 + 12)
        if (load32(arg1 + 12) == 0):
            break
        if arg3:
            arg3 = (arg0 + 281704)
            store32((arg0 + 281704), (load32(arg3) + v4))
            v4 = load32(arg1 + 12)
        arg1 = load32((arg0 + 283860))
        arg3 = (v4 - load32((arg0 + 283860)))
        if ((v4 - load32((arg0 + 283860))) > 0):
            store32(arg0 + 283860, 0)
            arg1 = (arg0 + 281720)
            store32((arg0 + 281720), (load32(arg1) + arg3))
            v4 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v5 = load32(9561692)
            arg1 = 1
            while True:  # $label12
                if (load8u((v10 + (load32(arg0 + 283908) + (arg1 * v4)))) & 8):
                    v7 = (v5 + (arg1 * 286704))
                    v4 = ((v5 + (arg1 * 286704)) + 283860)
                    arg2 = load32(((v5 + (arg1 * 286704)) + 283860))
                    if (load32(((v5 + (arg1 * 286704)) + 283860)) >= arg3):
                        store32(v4, (arg2 - arg3))
                        arg0 = ((v5 + (arg1 * 286704)) + 281736)
                        store32(((v5 + (arg1 * 286704)) + 281736), (load32(arg0) + arg3))
                        arg2 = 0
                        break
                    v7 = (v7 + 281736)
                    store32((v7 + 281736), (load32(v7) + arg2))
                    store32(v4, 0)
                    v4 = load32(9142892)
                    arg3 = (arg3 - arg2)
                arg2 = 0
                arg1 = (arg1 + 1)
                if (u((arg1 + 1)) < u(v4)):
                    continue
                break
            break
        store32(arg0 + 283860, (arg1 - v4))
        break
    G.global0 = (v6 + 80)
    return arg2

# ------------------------------------------------------------
# $func67
# ------------------------------------------------------------
def func67(arg0):
    v3 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # block $label0
        if load8u(9142917):
            break
        while True:  # block $label2
            while True:  # block $label1
                v4 = load8u(arg0 + 125)
                # br_table[(load8u(arg0 + 125) - 4)]
                break
                break
            while True:  # block $label3
                v2 = ((load8u(arg0 + 122) * 404) + 9568096)
                v1 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 356)
                if load32(((load8u(arg0 + 122) * 404) + 9568096) + 356):
                    break
                v1 = load32(v2 + 216)
                v2 = load32(v2 + 220)
                v1 = (load32(v2 + 216) if (u(v1) > u(v2)) else load32(v2 + 220))
                v1 = ((6 if (u(v1) >= u(6)) else (load32(v2 + 216) if (u(v1) > u(v2)) else load32(v2 + 220))) - 1)
                if (u(((6 if (u(v1) >= u(6)) else (load32(v2 + 216) if (u(v1) > u(v2)) else load32(v2 + 220))) - 1)) > u(4)):
                    v1 = 9142636
                    break
                v1 = load32(((v1 << 2) + 10132))
                break
            v1 = load32(v1)
            break
        v2 = load8u(arg0 + 122)
        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 6):
            v5 = load32(((v2 * 72) + 9263856) + 8)
            v1 = (load32(((v2 * 72) + 9263856) + 8) if v5 else v1)
        v4 = ((v4 != 4) & (v4 != 14))
        while True:  # block $label4
            if (((load32(38600) == v2) | (load32(38472) == v2)) == 0):
                break
            if v1:
                break
            v1 = load32(((v2 * 72) + 9263856))
            store8(arg0 + 124, 0)
            break
        if (load8u(arg0 + 129) == 8):
        if v1:
            break
        v1 = load8u(arg0 + 122)
        if (load8u(arg0 + 125) == 1):
            v1 = load32(((v1 * 404) + 9568096) + 260)
            if load32(((v1 * 404) + 9568096) + 260):
                v2 = (32000 // v1)
                # TODO: i32.extend16_s []
            else:
            v9 = (float(((32000 // v1) - (v2 % 25))) / 1.0)
            v2 = (load8u(arg0 + 124) << 3)
            v6 = float(load32(((load8u(arg0 + 124) << 3) + 8996)))
            v7 = ((float(((32000 // v1) - (v2 % 25))) / 1.0) * float(load32(((load8u(arg0 + 124) << 3) + 8996))))
            v9 = float(load32((v2 + 8992)))
            v10 = (v9 * float(load32((v2 + 8992))))
            v2 = (load32((load32(9215884) + (load32(arg0 + 44) << 4))) * 25)
            if v1:
                v1 = (32000 // v1)
                # TODO: i32.extend16_s []
            else:
            # TODO: f32.convert_i32_u []
            v11 = (-1 + v2)
            # TODO: f64.promote_f32 []
            v12 = v7
            # TODO: f64.promote_f32 []
            v13 = v10
            v1 = load32(arg0 + 40)
            while True:  # block $label5
                if load8u(9142916):
                    store32(v3 + 72, v1)
                    store64((v3 - -64), 0)
                    store32(v3 + 56, v12)
                    store32(v3 + 48, v13)
                    a_b()
                    break
                store32(v3 + 32, v1)
                # TODO: f64.promote_f32 []
                store32(v3 + 24, v11)
                store64(v3 + 16, 0)
                store32(v3 + 8, v12)
                store32(v3, v13)
                a_b()
                break
            while True:  # block $label6
                # TODO: f32.convert_i32_u []
                v8 = (load16u(arg0 + 112) - v9)
                if (((load16u(arg0 + 112) - v9) < 4294967300.0) & (v8 >= 0.0)):
                    # TODO: i32.trunc_f32_u []
                    break
                break
            store16(v8 + 112, 0)
            while True:  # block $label7
                # TODO: f32.convert_i32_u []
                v8 = (load16u(arg0 + 114) - v6)
                if (((load16u(arg0 + 114) - v6) < 4294967300.0) & (v8 >= 0.0)):
                    # TODO: i32.trunc_f32_u []
                    break
                break
            store16(v8 + 114, 0)
            if load8u(9142916):
            func288(arg0, v10, v7)
            while True:  # block $label8
                # TODO: f32.convert_i32_u []
                v7 = (v9 + load16u(arg0 + 112))
                if (((v9 + load16u(arg0 + 112)) < 4294967300.0) & (v7 >= 0.0)):
                    # TODO: i32.trunc_f32_u []
                    break
                break
            store16(v7 + 112, 0)
            # TODO: f32.convert_i32_u []
            v6 = (v6 + load16u(arg0 + 114))
            if (((v6 + load16u(arg0 + 114)) < 4294967300.0) & (v6 >= 0.0)):
                # TODO: i32.trunc_f32_u []
                store16(arg0 + 114, v6)
                break
            store16(arg0 + 114, 0)
            break
        while True:  # block $label10
            while True:  # block $label9
                while True:  # block $label11
                    # br_table[(v1 + -64)]
                    break
                    break
                if (v1 != 10):
                    break
                break
            while True:  # block $label12
                while True:  # block $label13
                    v2 = load32(9215884)
                    v4 = load32(arg0 + 44)
                    # br_table[(load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) - 1)]
                    break
                    break
                break
                break
            while True:  # block $label14
                v2 = (load32(9671128) + (load32((v2 + ((v4 << 4) | 12))) * 132))
                if (load8u((load32(9671128) + (load32((v2 + ((v4 << 4) | 12))) * 132)) + 125) == 10):
                    break
                while True:  # block $label16
                    while True:  # block $label15
                        v2 = load8u(v2 + 122)
                        # br_table[(load32(((load8u(v2 + 122) * 404) + 9568096) + 188) - 1)]
                        break
                        break
                    break
                    break
                if (v2 == load32(38500)):
                    break
                break
                break
            break
            break
        break
    G.global0 = (v3 + 80)
    return func86(arg0)

# ------------------------------------------------------------
# $func68
# ------------------------------------------------------------
def func68():
    v0 = func443(4)
    store32(func443(4), 32876)
    store32(v0, 32836)
    store32(v0, 32856)
    a_i()
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func69
# ------------------------------------------------------------
def func69(arg0, arg1):
    v7 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v8 = load16u(arg0 + 116)
        if (load16u(arg0 + 116) == 0):
            break
        v9 = load16u(arg0 + 118)
        if (load16u(arg0 + 118) == 0):
            break
        v5 = load32(9671128)
        v10 = (load32(9671128) + (arg1 * 132))
        while True:  # block $label7
            while True:  # block $label2
                while True:  # block $label1
                    v3 = load32(9142840)
                    v2 = (v8 + 1)
                    v4 = (load32(9142440) + 2)
                    v6 = (v9 + 1)
                    arg0 = load32((load32(9142840) + (((v8 + 1) + ((load32(9142440) + 2) * (v9 + 1))) << 2)))
                    if (u(load32((load32(9142840) + (((v8 + 1) + ((load32(9142440) + 2) * (v9 + 1))) << 2)))) > u(2)):
                        break
                    arg0 = load32((v3 + ((((v4 + v6) * v4) + v2) << 2)))
                    if (u(load32((v3 + ((((v4 + v6) * v4) + v2) << 2)))) > u(2)):
                        break
                    v6 = load8u((v5 + (arg0 * 132)) + 122)
                    v3 = 0
                    break
                    break
                v4 = (v5 + (arg0 * 132))
                v6 = load8u((v5 + (arg0 * 132)) + 122)
                v2 = load32(((load8u((v5 + (arg0 * 132)) + 122) * 404) + 9568096) + 192)
                while True:  # block $label4
                    while True:  # block $label3
                        while True:  # block $label5
                            v11 = load8u(v10 + 122)
                            # br_table[(load8u(v10 + 122) + -64)]
                            break
                            break
                        if (v11 != 10):
                            break
                        break
                    if (u(v2) > u(1)):
                        break
                    while True:  # block $label6
                        # br_table[(load8u((v5 + (arg0 * 132)) + 125) - 4)]
                        break
                        break
                    v3 = 0
                    v4 = func224(v4, v2, 0)
                    if (func224(v4, v2, 0) == 0):
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
                # br_table[func161(v4, (v7 + 12), 1)]
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

# ------------------------------------------------------------
# $func70
# ------------------------------------------------------------
def func70(arg0, arg1, arg2, arg3):
    while True:  # block $label18
        while True:  # block $label17
            if (load32(arg0 + 132) > 0):
                v7 = load32(arg0)
                if (load32(load32(arg0) + 44) == 2):
                    v4 = -201342849
                    while True:  # block $label1
                        while True:  # $label3
                            while True:  # block $label0
                                if ((v4 & 1) == 0):
                                    break
                                if (load16u((arg0 + (v5 << 2)) + 148) == 0):
                                    break
                                v4 = 0
                                break
                                break
                            while True:  # block $label2
                                if ((v4 & 2) == 0):
                                    break
                                if (load16u((arg0 + ((v5 << 2) | 4)) + 148) == 0):
                                    break
                                v4 = 0
                                break
                                break
                            v4 = ((v4 & 0xFFFFFFFF) >> 2)
                            v5 = (v5 + 2)
                            if ((v5 + 2) != 32):
                                continue
                            break
                        while True:  # block $label4
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
                        while True:  # block $label7
                            while True:  # block $label6
                                v9 = (v6 + 1)
                                if ((v6 + 1) >= v12):
                                    break
                                if (v4 != v5):
                                    break
                                v6 = v9
                                break
                                break
                            while True:  # block $label8
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
                            while True:  # block $label9
                                if (v4 == 0):
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
                        while True:  # block $label12
                            while True:  # block $label11
                                v9 = (v6 + 1)
                                if ((v6 + 1) >= v12):
                                    break
                                if (v4 != v5):
                                    break
                                v6 = v9
                                break
                                break
                            while True:  # block $label13
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
                            while True:  # block $label14
                                if (v4 == 0):
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
                while True:  # block $label16
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
                if (u((((load32(arg0 + 5804) + 10) & 0xFFFFFFFF) >> 3)) <= u((((v4 + 27) & 0xFFFFFFFF) >> 3))):
                    break
                if (load32(arg0 + 136) == 4):
                    break
                break
            v5 = (arg2 + 5)
            break
        v4 = v5
        break
    while True:  # block $label20
        while True:  # block $label19
            if (arg1 == 0):
                break
            if (u((arg2 + 4)) > u(v4)):
                break
            break
            break
        arg1 = load32(arg0 + 5820)
        if (v4 == v5):
            arg2 = (arg3 + 2)
            while True:  # block $label21
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
        while True:  # block $label22
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
        while True:  # block $label23
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
        while True:  # block $label24
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
        while True:  # block $label25
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
            while True:  # block $label26
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
        while True:  # block $label28
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

# ------------------------------------------------------------
# $func71
# ------------------------------------------------------------
def func71(arg0, arg1, arg2, arg3, arg4, arg5):
    v6 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v9 = ((arg2 + arg4) + 6)
    v7 = func26((-1 if (u(v9) > u(1073741823)) else (((arg2 + arg4) + 6) << 2)))
    store64(func26((-1 if (u(v9) > u(1073741823)) else (((arg2 + arg4) + 6) << 2))), -4294967296)
    v8 = load32(9142384)
    store32(v7 + 20, arg4)
    store32(v7 + 16, arg2)
    store32(v7 + 12, arg0)
    store32(v7 + 8, v8)
    if arg2:
        # TODO: memory.copy []
    if arg4:
        # TODO: memory.copy []
    while True:  # block $label0
        if (load8u(9147125) == 0):
            store32(v6 + 4, v9)
            store32(v6, v7)
            break
        v10 = load32((9142892 if load8u(9147212) else 41092))
        if (u(load32((9142892 if load8u(9147212) else 41092))) >= u(2)):
            v8 = load32(9561692)
            arg4 = 1
            while True:  # $label1
                v11 = load32((v8 + (arg4 * 286704)) + 284616)
                if load32((v8 + (arg4 * 286704)) + 284616):
                    store32(v6 + 24, v11)
                    store32(v6 + 20, v9)
                    store32(v6 + 16, v7)
                    v8 = load32(9561692)
                arg4 = (arg4 + 1)
                if ((arg4 + 1) != v10):
                    continue
                break
        break
    if (arg5 == 0):
        store32(59164, load32(9142384))
        # call_indirect[load32(((arg0 << 3) + 9213824))]
        store32(59164, 0)
    G.global0 = (v6 + 48)

# ------------------------------------------------------------
# $func72
# ------------------------------------------------------------
def func72(arg0, arg1):
    v8 = load32(arg0 + 283848)
    store32(arg1, load32(arg0 + 283848))
    v9 = load32((arg0 + 283852))
    store32(arg1 + 4, load32((arg0 + 283852)))
    v10 = load32((arg0 + 283856))
    store32(arg1 + 8, load32((arg0 + 283856)))
    v2 = load32((arg0 + 283860))
    store32(arg1 + 12, load32((arg0 + 283860)))
    v12 = load32(9142892)
    if (u(load32(9142892)) >= u(2)):
        v3 = load32(9561692)
        v11 = load32(9143016)
        v4 = 1
        while True:  # $label4
            v5 = v3
            v3 = v8
            v6 = v9
            v7 = v10
            v13 = v2
            while True:  # block $label0
                v14 = (v4 * v12)
                v2 = ((v4 * v12) + load32(arg0 + 283908))
                if ((load8u((v11 + ((v4 * v12) + load32(arg0 + 283908)))) & 1) == 0):
                    break
                v8 = 2147483647
                if (v3 == 2147483647):
                    break
                v3 = load32((v5 + (v4 * 286704)) + 283848)
                v8 = (2147483647 if (v3 == 2147483647) else (v3 + load32((v5 + (v4 * 286704)) + 283848)))
                store32(arg1, (2147483647 if (v3 == 2147483647) else (v3 + load32((v5 + (v4 * 286704)) + 283848))))
                v12 = load32(9142892)
                v14 = (load32(9142892) * v4)
                v2 = ((load32(9142892) * v4) + load32(arg0 + 283908))
                break
            v3 = load32(9561692)
            while True:  # block $label1
                v2 = load8u((v2 + v11))
                if ((load8u((v2 + v11)) & 2) == 0):
                    break
                v9 = 2147483647
                if (v6 == 2147483647):
                    break
                v6 = load32(((v5 + (v4 * 286704)) + 283852))
                v9 = (2147483647 if (v6 == 2147483647) else (v6 + load32(((v5 + (v4 * 286704)) + 283852))))
                store32(arg1 + 4, (2147483647 if (v6 == 2147483647) else (v6 + load32(((v5 + (v4 * 286704)) + 283852)))))
                v2 = load8u((v11 + (v14 + load32(arg0 + 283908))))
                break
            while True:  # block $label2
                if ((v2 & 4) == 0):
                    break
                v10 = 2147483647
                if (v7 == 2147483647):
                    break
                v7 = load32(((v5 + (v4 * 286704)) + 283856))
                v10 = (2147483647 if (v7 == 2147483647) else (v7 + load32(((v5 + (v4 * 286704)) + 283856))))
                store32(arg1 + 8, (2147483647 if (v7 == 2147483647) else (v7 + load32(((v5 + (v4 * 286704)) + 283856)))))
                v2 = load8u((v11 + (v14 + load32(arg0 + 283908))))
                break
            while True:  # block $label3
                if ((v2 & 8) == 0):
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
            if (u((v4 + 1)) < u(v12)):
                continue
            break
    return v5

# ------------------------------------------------------------
# $func73
# ------------------------------------------------------------
def func73(arg0, arg1, arg2, arg3, arg4, arg5):
    v7 = load32(arg2 + 216)
    v16 = load32(arg2 + 208)
    v11 = load32(arg2 + 372)
    while True:  # block $label4
        while True:  # block $label0
            if (arg5 == 0):
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
                    while True:  # block $label2
                        if (u(v6) >= u(v10)):
                            while True:  # $label1
                                if load8u((v11 + (v12 + ((arg5 - arg1) * v7)))):
                                    return 0
                                arg5 = (arg5 + 1)
                                if ((arg5 + 1) != v9):
                                    continue
                                break
                                break
                            raise RuntimeError('unreachable')
                        while True:  # $label5
                            while True:  # block $label3
                                if (load8u((v11 + (v12 + ((arg5 - arg1) * v7)))) == 0):
                                    arg5 = (arg5 + 1)
                                    break
                                if (u(arg5) >= u(v10)):
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
                while True:  # block $label9
                    if (u(v6) < u(v10)):
                        while True:  # $label8
                            while True:  # block $label7
                                if (load8u((v11 + (v12 + ((arg5 - arg1) * v7)))) == 0):
                                    arg5 = (arg5 + 1)
                                    break
                                if (u(arg5) >= u(v10)):
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
                        raise RuntimeError('unreachable')
                    while True:  # $label10
                        if (load8u((v11 + (v12 + ((arg5 - arg1) * v7)))) == 0):
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
        if (arg3 == 0):
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
                while True:  # block $label12
                    if (load8u((v11 + (v8 + ((arg5 - arg1) * v7)))) == 0):
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

# ------------------------------------------------------------
# $func74
# ------------------------------------------------------------
def func74(arg0, arg1, arg2):
    while True:  # block $label0
        if load8u(9147152):
            break
        v5 = load16u(arg0 + 114)
        v4 = load16u(arg0 + 112)
        while True:  # block $label1
            if (arg1 == -1):
                break
            if (load8u(59181) == 0):
                break
            v3 = load32(arg0 + 44)
            if (load32(arg0 + 44) == 0):
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
        while True:  # block $label2
            v3 = load32(9142872)
            if (load32(9142872) == 0):
                break
            if (load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(9142892) * v3)))) == 0):
                break
            break
        if (((load8u(arg0 + 125) != 3) | arg2) == 0):
            break
        v3 = ((load8u(arg0 + 122) * 404) + 9568096)
        arg1 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 220)
        arg2 = load32(v3 + 216)
        while True:  # block $label5
            while True:  # block $label4
                while True:  # block $label3
                    # br_table[(load8u(arg0 + 125) - 4)]
                    break
                    break
                break
                break
            break
        arg0 = load32(v3 + 200)
        if (load32(v3 + 200) == 0):
            break
        if (u(load32(load32(9142424) + 48)) < u(2)):
            break
        v6 = (load32(9142836) + (arg0 * 80))
        v7 = load32((load32(9142836) + (arg0 * 80)) + 324)
        if (load32((load32(9142836) + (arg0 * 80)) + 324) == 0):
            break
        v8 = (((arg1 & 0xFFFFFFFF) >> 1) + v5)
        v9 = (((arg2 & 0xFFFFFFFF) >> 1) + v4)
        arg1 = load32(9142440)
        v10 = (arg0 * arg0)
        arg0 = 0
        while True:  # $label7
            while True:  # block $label6
                v4 = load32(v6 + 320)
                v3 = (arg0 << 2)
                arg2 = load32((load32(v6 + 320) + ((arg0 << 2) | 4)))
                v5 = (v8 + load32((load32(v6 + 320) + ((arg0 << 2) | 4))))
                if (u(arg1) <= u((v8 + load32((load32(v6 + 320) + ((arg0 << 2) | 4)))))):
                    break
                v4 = load32((v3 + v4))
                v3 = (v9 + load32((v3 + v4)))
                if (u(arg1) <= u((v9 + load32((v3 + v4))))):
                    break
                if ((v3 | v5) < 0):
                    break
                if ((((v4 * v4) + (arg2 * arg2)) - 1) > v10):
                    break
                arg1 = load32(9142440)
                break
            arg0 = (arg0 + 2)
            if (u((arg0 + 2)) < u(v7)):
                continue
            break
        break
    return func129(v3, v5, 0)

# ------------------------------------------------------------
# $func89
# ------------------------------------------------------------
def func89(arg0, arg1, arg2):
    while True:  # block $label0
        v3 = (arg0 & 65535)
        v4 = ((arg0 & 0xFFFFFFFF) >> 16)
        if (arg2 == 1):
            arg0 = (v3 + load8u(arg1))
            arg0 = (((v3 + load8u(arg1)) - 65521) if (u(arg0) > u(65520)) else arg0)
            arg1 = ((((v3 + load8u(arg1)) - 65521) if (u(arg0) > u(65520)) else arg0) + v4)
            arg2 = (((((v3 + load8u(arg1)) - 65521) if (u(arg0) > u(65520)) else arg0) + v4) << 16)
            break
        if arg1:
            if (u(arg2) >= u(16)):
                while True:  # block $label3
                    while True:  # block $label6
                        while True:  # block $label4
                            if (u(arg2) > u(5551)):
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
                                    if (u(arg2) > u(5551)):
                                        continue
                                    break
                                if (arg2 == 0):
                                    break
                                if (u(arg2) < u(16)):
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
                                if (u((arg2 - 16)) > u(15)):
                                    continue
                                break
                            if (arg2 == 0):
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
                        if (u(v6) < u(3)):
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
            while True:  # block $label9
                if (arg2 == 0):
                    break
                while True:  # block $label10
                    v7 = (arg2 & 3)
                    if ((arg2 & 3) == 0):
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
                if (u(arg2) < u(4)):
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

# ------------------------------------------------------------
# $func90
# ------------------------------------------------------------
def func90(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    v9 = ((i64(arg4) * i64(arg7)) << 3)
    if (u(((i64(arg4) * i64(arg7)) << 3)) <= u(4294967295)):
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
        # TODO: memory.fill []
        arg3 = load32(arg0)
        arg6 = ((arg1 - 1) if load32(arg0) else arg4)
        store32(arg0 + 40, ((arg1 - 1) if load32(arg0) else arg4))
        arg1 = ((arg4 - 1) if arg3 else arg1)
        store32(arg0 + 36, ((arg4 - 1) if arg3 else arg1))
        if (arg3 == 0):
            # TODO: i64.div_u []
            store32(4294967296 + 12, i64(arg6))
        arg3 = load32(arg0 + 4)
        arg6 = (load32(arg0 + 4) != 0)
        arg4 = (arg5 - (load32(arg0 + 4) != 0))
        store32(arg0 + 32, (arg5 - (load32(arg0 + 4) != 0)))
        arg2 = (arg2 - arg6)
        store32(arg0 + 28, (arg2 - arg6))
        while True:  # block $label0
            if (arg3 == 0):
                store32(arg0 + 24, arg2)
                # TODO: i64.div_u []
                v9 = (i64(arg2) * i64(arg1))
                store32(4294967296 + 20, ((i64(arg5) << 32) if (u(v9) >= u(4294967296)) else (i64(arg2) * i64(arg1))))
                break
            store32(arg0 + 24, arg4)
            arg4 = arg1
            break
        # TODO: i64.div_u []
        store32(4294967296 + 16, i64(arg4))
        arg0 = load32(52304)
        if (load32(52304) != load32(52320)):
            store32(9687812, 381)
            store32(9687808, 382)
            store32(9687804, 383)
            store32(9687800, 384)
            store32(52320, arg0)
    else:
    return 0

# ------------------------------------------------------------
# $func91
# ------------------------------------------------------------
def func91(arg0, param1):
    while True:  # block $label3
        while True:  # block $label2
            while True:  # block $label0
                if (load32(arg0 + 24) <= 0):
                    v2 = load32(arg0 + 56)
                    if (load32(arg0 + 56) <= load32((arg0 - -64))):
                        break
                    v1 = 9687808
                    while True:  # block $label4
                        while True:  # block $label1
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
                        # call_indirect[load32(v1)]
                        break
                    store32(arg0 + 24, (load32(arg0 + 24) + load32(arg0 + 28)))
                    store32(arg0 + 68, (load32(arg0 + 68) + load32(arg0 + 72)))
                    arg0 = (arg0 - -64)
                    store32((arg0 - -64), (load32(arg0) + 1))
                return
                break
            a_c()
            raise RuntimeError('unreachable')
            break
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func92
# ------------------------------------------------------------
def func92(arg0, arg1, arg2):
    v3 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    v4 = load32(arg0 + 40)
    if load32(arg0 + 40):
        # TODO: f64.promote_f32 []
        v5 = arg2
        # TODO: f64.promote_f32 []
        v6 = arg1
        while True:  # block $label0
            if load8u(9142916):
                store32(v3 + 120, v4)
                store64(v3 + 112, 0)
                store32(v3 + 104, v5)
                store32(v3 + 96, v6)
                a_b()
                break
            store64((v3 - -64), 0)
            store32(v3 + 80, v4)
            # TODO: f32.convert_i32_u []
            # TODO: f64.promote_f32 []
            store32(v3 + 72, (load32(9142848) * 25))
            store32(v3 + 48, v6)
            store32(v3 + 56, v5)
            a_b()
            break
        while True:  # block $label1
            if load8u(9142916):
                break
            v4 = load32(arg0 + 92)
            if (load32(arg0 + 92) == 0):
                break
            if load8u(9142906):
                break
            store64(v3 + 16, 0)
            store32(v3 + 32, v4)
            # TODO: f32.convert_i32_u []
            # TODO: f64.promote_f32 []
            store32(v3 + 24, (load32(9142848) * 25))
            store32(v3, v6)
            store32(v3 + 8, v5)
            a_b()
            break
        func288(arg0, arg1, arg2)
    G.global0 = (v3 + 128)

# ------------------------------------------------------------
# $func93
# ------------------------------------------------------------
def func93(arg0, arg1, arg2):
    v6 = (arg1 - 1)
    v7 = (arg0 - 1)
    v3 = load32(arg2 + 216)
    while True:  # block $label1
        while True:  # block $label0
            if (((arg0 > 0) & (arg1 > 0)) == 0):
                v5 = load32(arg2 + 220)
                break
            v5 = load32(arg2 + 220)
            if (u(v3) <= u(v7)):
                break
            if (u(v5) <= u(v6)):
                break
            if load8u(arg2 + 377):
                break
            if load8u((load32(arg2 + 372) + ((v3 * v6) + v7))):
                break
            break
        v4 = ((arg1 > 0) & (arg0 >= 0))
        while True:  # block $label9
            if load8u(arg2 + 377):
                while True:  # block $label2
                    if (v4 == 0):
                        break
                    if (u(arg0) >= u(v3)):
                        break
                    v4 = 1
                    if (u(v5) > u(v6)):
                        break
                    break
                while True:  # block $label3
                    if (arg0 <= 0):
                        break
                    if (arg1 < 2):
                        break
                    if (u(v3) <= u(v7)):
                        break
                    v4 = 1
                    if (u((arg1 - 2)) < u(v5)):
                        break
                    break
                while True:  # block $label4
                    if (arg0 < 2):
                        break
                    v4 = 1
                    if (arg1 <= 0):
                        break
                    if (u((arg0 - 2)) >= u(v3)):
                        break
                    if (u(v5) > u(v6)):
                        break
                    break
                while True:  # block $label5
                    if (arg0 <= 0):
                        break
                    if (arg1 < 0):
                        break
                    if (u(v3) <= u(v7)):
                        break
                    v4 = 1
                    if (u(arg1) < u(v5)):
                        break
                    break
                while True:  # block $label6
                    if (arg0 < 0):
                        break
                    if (arg1 < 2):
                        break
                    if (u(arg0) >= u(v3)):
                        break
                    v4 = 1
                    if (u((arg1 - 2)) < u(v5)):
                        break
                    break
                while True:  # block $label7
                    arg2 = (arg0 < 2)
                    if (arg0 < 2):
                        break
                    if (arg1 < 2):
                        break
                    if (u((arg0 - 2)) >= u(v3)):
                        break
                    v4 = 1
                    if (u((arg1 - 2)) < u(v5)):
                        break
                    break
                while True:  # block $label8
                    if arg2:
                        break
                    if (arg1 < 0):
                        break
                    if (u((arg0 - 2)) >= u(v3)):
                        break
                    v4 = 1
                    if (u(arg1) < u(v5)):
                        break
                    break
                if ((arg0 | arg1) < 0):
                    break
                if (u(arg0) >= u(v3)):
                    break
                v4 = 1
                if (u(arg1) >= u(v5)):
                    break
                break
            arg2 = load32(arg2 + 372)
            while True:  # block $label10
                if (v4 == 0):
                    break
                if (u(arg0) >= u(v3)):
                    break
                if (u(v5) <= u(v6)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v6) + arg0))):
                    break
                break
            v8 = (arg1 - 2)
            while True:  # block $label11
                if (arg0 <= 0):
                    break
                if (arg1 < 2):
                    break
                if (u(v3) <= u(v7)):
                    break
                if (u(v5) <= u(v8)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v8) + v7))):
                    break
                break
            v9 = (arg0 - 2)
            while True:  # block $label12
                if (arg0 < 2):
                    break
                if (arg1 <= 0):
                    break
                if (u(v3) <= u(v9)):
                    break
                if (u(v5) <= u(v6)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v6) + v9))):
                    break
                break
            while True:  # block $label13
                if (arg0 <= 0):
                    break
                if (arg1 < 0):
                    break
                if (u(v3) <= u(v7)):
                    break
                if (u(arg1) >= u(v5)):
                    break
                v4 = 1
                if load8u((arg2 + ((arg1 * v3) + v7))):
                    break
                break
            while True:  # block $label14
                if (arg0 < 0):
                    break
                if (arg1 < 2):
                    break
                if (u(arg0) >= u(v3)):
                    break
                if (u(v5) <= u(v8)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v8) + arg0))):
                    break
                break
            while True:  # block $label15
                v6 = (arg0 < 2)
                if (arg0 < 2):
                    break
                if (arg1 < 2):
                    break
                if (u(v3) <= u(v9)):
                    break
                if (u(v5) <= u(v8)):
                    break
                v4 = 1
                if load8u((arg2 + ((v3 * v8) + v9))):
                    break
                break
            while True:  # block $label16
                if v6:
                    break
                if (arg1 < 0):
                    break
                if (u(v3) <= u(v9)):
                    break
                if (u(arg1) >= u(v5)):
                    break
                v4 = 1
                if load8u((arg2 + ((arg1 * v3) + v9))):
                    break
                break
            if ((arg0 | arg1) < 0):
                break
            if (u(arg0) >= u(v3)):
                break
            if (u(arg1) >= u(v5)):
                break
            v4 = 1
            if load8u((arg2 + ((arg1 * v3) + arg0))):
                break
            break
        v4 = 0
        break
    return v4

# ------------------------------------------------------------
# $func94
# ------------------------------------------------------------
def func94(arg0, arg1, arg2):
    v12 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # block $label0
        if (load32(arg0 + 283908) == 0):
            break
        while True:  # block $label1
            if (arg1 == 0):
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
        while True:  # block $label2
            v3 = load8u(arg0 + 286696)
            if load8u(arg0 + 286696):
                break
            if load8u(9147152):
                break
            if load8u(9142905):
                break
            while True:  # block $label3
                if (arg2 != load32(9142872)):
                    break
                a_b()
                if (load32(load32(9142424) + 160) == 0):
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
            if (load32(arg0 + 283956) == 0):
                # TODO: i32.div_u []
                store32((load32(9142848) * 25) + 283956, 1000)
            if (arg1 == 0):
                store8(arg0 + 286696, 1)
            if load8u(9147127):
                arg1 = 0
                v3 = (G.global0 - 16)
                G.global0 = (G.global0 - 16)
                while True:  # block $label4
                    v4 = load32(9142892)
                    if (u(load32(9142892)) < u(2)):
                        break
                    v6 = load32(9143004)
                    v5 = load32(arg0 + 283908)
                    v14 = load32(9561692)
                    arg2 = 1
                    while True:  # $label6
                        while True:  # block $label5
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
                    if (arg1 == 0):
                        break
                    store32(v3, (load32(arg0 + 283848) // arg1))
                    store32(v3 + 4, (load32((arg0 + 283852)) // arg1))
                    store32(v3 + 8, (load32((arg0 + 283856)) // arg1))
                    store32(v3 + 12, (load32((arg0 + 283860)) // arg1))
                    if (u(v4) < u(2)):
                        break
                    arg1 = load32(9143004)
                    v5 = load32(9561692)
                    arg2 = 1
                    while True:  # $label8
                        while True:  # block $label7
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
                            v4 = load32(9142892)
                            arg1 = load32(9143004)
                            v5 = load32(9561692)
                            break
                        arg2 = (arg2 + 1)
                        if (u((arg2 + 1)) < u(v4)):
                            continue
                        break
                    break
                G.global0 = (v3 + 16)
            v16 = 0
            v14 = (G.global0 - 32)
            G.global0 = (G.global0 - 32)
            while True:  # block $label9
                arg2 = load32(9142892)
                if (u(load32(9142892)) < u(2)):
                    break
                v6 = load32(9561692)
                v4 = 1
                while True:  # $label14
                    while True:  # block $label10
                        if (u(arg2) < u(2)):
                            arg2 = 1
                            break
                        v3 = (v6 + (v4 * 286704))
                        v9 = (arg2 * v4)
                        v5 = 0
                        v7 = load32(9143004)
                        arg1 = 1
                        while True:  # block $label13
                            while True:  # $label12
                                while True:  # block $label11
                                    if (arg1 == v4):
                                        break
                                    v10 = load8u((v7 + (arg1 + v9)))
                                    v15 = (v6 + (arg1 * 286704))
                                    v18 = load8u((v6 + (arg1 * 286704)) + 286699)
                                    v5 = (((load8u((v7 + (arg1 + v9))) != 0) | v5) if load8u((v6 + (arg1 * 286704)) + 286699) else v5)
                                    if (v10 == 0):
                                        break
                                    if v18:
                                        break
                                    if (load8u(v15 + 286696) == 0):
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
                            if ((v5 & 1) == 0):
                                break
                            break
                        store32(9561720, load32(v3 + 284608))
                        v16 = 1
                        if load8u(v3 + 286696):
                            break
                        if load8u(v3 + 286697):
                            break
                        store8((v3 + 286697), 1)
                        if (load32(v3 + 283908) == load32(9142872)):
                            a_b()
                        arg2 = load32(v3 + 284628)
                        arg1 = load32(v3 + 284616)
                        store32(v14 + 20, v3)
                        store32(v14 + 16, 119)
                        store32(v14 + 24, (arg1 if arg1 else arg2))
                        a_b()
                        func227()
                        arg2 = load32(9142892)
                        v6 = load32(9561692)
                        break
                    v4 = (v4 + 1)
                    if (u((v4 + 1)) < u(arg2)):
                        continue
                    break
                if ((v16 & (load8u(9142905) == 0)) == 0):
                    break
                store8(9142905, 1)
                arg1 = (load32(9142848) * 25)
                # TODO: i32.div_u []
                store32(1, ((load32(9142848) * 25) if (u(arg1) < u(1000)) else 1000))
                if (u(arg2) >= u(2)):
                    v3 = load32(9561692)
                    arg1 = 1
                    while True:  # $label15
                        v4 = (v3 + (arg1 * 286704))
                        if (load32((v3 + (arg1 * 286704)) + 283956) == 0):
                            store32((v4 + 283956), load32(9561724))
                            arg2 = load32(9142892)
                        arg1 = (arg1 + 1)
                        if (u((arg1 + 1)) < u(arg2)):
                            continue
                        break
                if load8u(9147127):
                    func361()
                    arg2 = load32(9142892)
                    v18 = ((load32(9142892) * 54) - 54)
                    v19 = func26((-1 if (u(v18) > u(1073741823)) else (((load32(9142892) * 54) - 54) << 2)))
                    while True:  # block $label19
                        while True:  # block $label18
                            if (u(arg2) >= u(2)):
                                v3 = load32(9561692)
                                arg1 = 1
                                while True:  # $label17
                                    while True:  # block $label16
                                        if (load32((v3 + (arg1 * 286704)) + 283944) == 1):
                                            v20 = load32((v3 + (arg1 * 286704)) + 283884)
                                            break
                                        arg1 = (arg1 + 1)
                                        if ((arg1 + 1) != arg2):
                                            continue
                                        break
                                    break
                                if (u(arg2) > u(1)):
                                    break
                            v7 = load32(9561720)
                            break
                            break
                        v16 = 1
                        while True:  # $label59
                            v5 = 0
                            arg1 = load32(9561692)
                            v4 = (load32(9561692) + (v16 * 286704))
                            if v20:
                                # TODO: i32.div_u []
                            else:
                            store32(v20 + 283884, 0)
                            v3 = ((v16 * 216) + v19)
                            store32((((v16 * 216) + v19) - 216), load32(v4 + 283944))
                            store32((v3 - 212), load32(v4 + 283960))
                            store32((v3 - 208), load32(v4 + 284608))
                            store32((v3 - 204), load32(v4 + 283892))
                            v17 = (v4 + 283884)
                            while True:  # block $label33
                                v6 = load32(9142892)
                                if load32(9142892):
                                    v10 = (v4 + 281784)
                                    arg1 = load32((v4 + 281784))
                                    v7 = (load32((v4 + 281784)) * 255)
                                    v13 = (arg1 * v6)
                                    v15 = load32(9561692)
                                    v9 = load32(9143004)
                                    arg2 = 0
                                    while True:  # $label22
                                        while True:  # block $label20
                                            if (load8u((v9 + (v5 + v13))) == 0):
                                                break
                                            v8 = ((v15 + (v5 * 286704)) + 278568)
                                            arg1 = 0
                                            while True:  # $label21
                                                if (load32(((arg1 * 404) + 9568096) + 264) != 1):
                                                    arg2 = (load32((load32(v8) + ((arg1 + v7) << 2))) + arg2)
                                                v11 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v11 * 404) + 9568096) + 264) != 1):
                                                    arg2 = (load32((load32(v8) + ((v7 + v11) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise RuntimeError('unreachable')
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
                                            while True:  # block $label23
                                                if (load32(((arg1 * 404) + 9568096) + 264) == 1):
                                                    break
                                                if (arg1 == v11):
                                                    break
                                                arg2 = (load32((v8 + ((arg1 + v13) << 2))) + arg2)
                                                break
                                            v7 = (arg1 | 1)
                                            if ((arg1 | 1) != 255):
                                                while True:  # block $label24
                                                    if (load32(((v7 * 404) + 9568096) + 264) == 1):
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
                                        while True:  # block $label27
                                            if (load8u((v9 + (v5 + v13))) == 0):
                                                break
                                            v8 = ((v15 + (v5 * 286704)) + 278564)
                                            arg1 = 0
                                            while True:  # $label28
                                                if (load32(((arg1 * 404) + 9568096) + 264) != 1):
                                                    arg2 = (load32((load32(v8) + ((arg1 + v7) << 2))) + arg2)
                                                v11 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v11 * 404) + 9568096) + 264) != 1):
                                                    arg2 = (load32((load32(v8) + ((v7 + v11) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise RuntimeError('unreachable')
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
                                        while True:  # block $label30
                                            if (load8u((v9 + (v5 + v8))) == 0):
                                                break
                                            v10 = (v5 * 255)
                                            arg1 = 0
                                            while True:  # $label31
                                                if (load32(((arg1 * 404) + 9568096) + 264) != 1):
                                                    arg2 = (load32((v7 + ((arg1 + v10) << 2))) + arg2)
                                                v15 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v15 * 404) + 9568096) + 264) != 1):
                                                    arg2 = (load32((v7 + ((v10 + v15) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise RuntimeError('unreachable')
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
                            while True:  # block $label34
                                if (v6 == 0):
                                    arg2 = 0
                                    store32((v3 - 148), 0)
                                    break
                                arg1 = load32((v4 + 281784))
                                v9 = (load32((v4 + 281784)) * 255)
                                v17 = (arg1 * v6)
                                v5 = 0
                                v26 = load32(9561692)
                                v27 = load32(9143004)
                                arg2 = 0
                                while True:  # $label37
                                    while True:  # block $label35
                                        if (load8u((v27 + (v5 + v17))) == 0):
                                            break
                                        v7 = ((v26 + (v5 * 286704)) + 278568)
                                        arg1 = 0
                                        while True:  # $label36
                                            if (load32(((arg1 * 404) + 9568096) + 264) == 1):
                                                arg2 = (load32((load32(v7) + ((arg1 + v9) << 2))) + arg2)
                                            v10 = (arg1 | 1)
                                            if ((arg1 | 1) == 255):
                                                break
                                            if (load32(((v10 * 404) + 9568096) + 264) == 1):
                                                arg2 = (load32((load32(v7) + ((v9 + v10) << 2))) + arg2)
                                            arg1 = (arg1 + 2)
                                            continue
                                            break
                                        raise RuntimeError('unreachable')
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
                                        if (load32(((arg1 * 404) + 9568096) + 264) == 1):
                                            arg2 = (load32((v9 + ((arg1 + v7) << 2))) + arg2)
                                        v10 = (arg1 | 1)
                                        if ((arg1 | 1) != 255):
                                            if (load32(((v10 * 404) + 9568096) + 264) == 1):
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
                            while True:  # block $label40
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
                                while True:  # block $label41
                                    if (load32(((arg1 * 404) + 9568096) + 264) & -5):
                                        break
                                    if (arg1 == v9):
                                        break
                                    arg2 = (load32(((v4 + (arg1 << 2)) + 278576)) + arg2)
                                    break
                                v5 = (arg1 | 1)
                                if ((arg1 | 1) != 255):
                                    while True:  # block $label42
                                        if (load32(((v5 * 404) + 9568096) + 264) & -5):
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
                            while True:  # block $label58
                                if v6:
                                    v10 = (v4 + 281784)
                                    arg1 = load32((v4 + 281784))
                                    v8 = (load32((v4 + 281784)) * 255)
                                    v17 = (arg1 * v6)
                                    v5 = 0
                                    v15 = load32(9561692)
                                    v9 = load32(9143004)
                                    arg2 = 0
                                    while True:  # $label46
                                        while True:  # block $label44
                                            if (load8u((v9 + (v5 + v17))) == 0):
                                                break
                                            v11 = ((v15 + (v5 * 286704)) + 278564)
                                            arg1 = 0
                                            while True:  # $label45
                                                if (load32(((arg1 * 404) + 9568096) + 264) == 1):
                                                    arg2 = (load32((load32(v11) + ((arg1 + v8) << 2))) + arg2)
                                                v13 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v13 * 404) + 9568096) + 264) == 1):
                                                    arg2 = (load32((load32(v11) + ((v8 + v13) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise RuntimeError('unreachable')
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
                                        while True:  # block $label47
                                            if (load8u((v9 + (v5 + v13))) == 0):
                                                break
                                            v8 = (v5 * 255)
                                            arg1 = 0
                                            while True:  # $label48
                                                if (load32(((arg1 * 404) + 9568096) + 264) == 1):
                                                    arg2 = (load32((v4 + ((arg1 + v8) << 2))) + arg2)
                                                v11 = (arg1 | 1)
                                                if ((arg1 | 1) == 255):
                                                    break
                                                if (load32(((v11 * 404) + 9568096) + 264) == 1):
                                                    arg2 = (load32((v4 + ((v8 + v11) << 2))) + arg2)
                                                arg1 = (arg1 + 2)
                                                continue
                                                break
                                            raise RuntimeError('unreachable')
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
                                        while True:  # block $label50
                                            if load8u((v9 + (v5 + v13))):
                                                break
                                            if (v4 == v5):
                                                break
                                            v17 = ((v15 + (v5 * 286704)) + 278564)
                                            arg1 = 0
                                            while True:  # $label52
                                                while True:  # block $label51
                                                    v8 = ((arg1 * 404) + 9568096)
                                                    if (load32(((arg1 * 404) + 9568096) + 264) == 1):
                                                        if (load32(v8 + 268) != 1):
                                                            break
                                                    # TODO: i32.div_u []
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
                                        while True:  # block $label54
                                            if load8u((v9 + (v4 + v11))):
                                                break
                                            if (v4 == v5):
                                                break
                                            v13 = ((v15 + (v4 * 286704)) + 278564)
                                            arg1 = 0
                                            while True:  # $label56
                                                while True:  # block $label55
                                                    v10 = ((arg1 * 404) + 9568096)
                                                    if (load32(((arg1 * 404) + 9568096) + 264) != 1):
                                                        break
                                                    if (load32(v10 + 268) == 1):
                                                        break
                                                    # TODO: i32.div_u []
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
                            if (u((v16 + 1)) < u(v6)):
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

# ------------------------------------------------------------
# $func95
# ------------------------------------------------------------
def func95(arg0, arg1, arg2):
    while True:  # $label9
        while True:  # block $label0
            v3 = load32(9142440)
            v4 = ((load32(9142440) * arg1) + arg0)
            v6 = (((load32(9142440) * arg1) + arg0) + load32(9147288))
            v7 = load8u((((load32(9142440) * arg1) + arg0) + load32(9147288)))
            # TODO: i32.extend8_s []
            v8 = load8u((((load32(9142440) * arg1) + arg0) + load32(9147288)))
            if (load8u((((load32(9142440) * arg1) + arg0) + load32(9147288))) != arg2):
                break
            v5 = func373(arg0, arg1, arg2)
            if (func373(arg0, arg1, arg2) < 0):
                break
            if (arg2 <= v5):
                break
            if (func410(v4, v5) != 55):
                break
            while True:  # block $label1
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
            while True:  # block $label2
                v3 = load32(9142440)
                if (u(load32(9142440)) <= u(arg1)):
                    break
                if (u(v3) <= u(v5)):
                    break
                if ((arg1 | v5) < 0):
                    break
                func95(v5, arg1, arg2)
                v3 = load32(9142440)
                break
            while True:  # block $label3
                v6 = (arg1 - 1)
                if (u(v3) <= u((arg1 - 1))):
                    break
                if (u(v3) <= u(v5)):
                    break
                if ((v5 | v6) < 0):
                    break
                func95(v5, v6, arg2)
                v3 = load32(9142440)
                break
            while True:  # block $label4
                if (u(v3) <= u(v6)):
                    break
                if (u(arg0) >= u(v3)):
                    break
                if ((arg0 | v6) < 0):
                    break
                func95(arg0, v6, arg2)
                v3 = load32(9142440)
                break
            v4 = (arg0 - 1)
            while True:  # block $label5
                if (u(v3) <= u(v6)):
                    break
                if (u(v3) <= u(v4)):
                    break
                if ((v4 | v6) < 0):
                    break
                func95(v4, v6, arg2)
                v3 = load32(9142440)
                break
            while True:  # block $label6
                if (u(arg1) >= u(v3)):
                    break
                if (u(v3) <= u(v4)):
                    break
                if ((arg1 | v4) < 0):
                    break
                func95(v4, arg1, arg2)
                v3 = load32(9142440)
                break
            while True:  # block $label7
                arg1 = (arg1 + 1)
                if (u(v3) <= u((arg1 + 1))):
                    break
                if (u(v3) <= u(v4)):
                    break
                if ((arg1 | v4) < 0):
                    break
                func95(v4, arg1, arg2)
                v3 = load32(9142440)
                break
            while True:  # block $label8
                if (u(arg1) >= u(v3)):
                    break
                if (u(arg0) >= u(v3)):
                    break
                if ((arg0 | arg1) < 0):
                    break
                func95(arg0, arg1, arg2)
                v3 = load32(9142440)
                break
            if (u(arg1) >= u(v3)):
                break
            if (u(v3) <= u(v5)):
                break
            arg0 = v5
            if ((v5 | arg1) >= 0):
                continue
            break
        break

# ------------------------------------------------------------
# $func96
# ------------------------------------------------------------
def func96(arg0, arg1, arg2, arg3):
    while True:  # $label17
        while True:  # block $label0
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
            while True:  # block $label1
                v8 = (u(arg1) >= u(v6))
                if (u(arg1) >= u(v6)):
                    break
                if (u(v6) <= u(v7)):
                    break
                if (v16 < 0):
                    break
                v4 = load8s((v12 + (v7 + v13)))
                v4 = (-1 if (v4 < 0) else (-1 if (arg2 == v4) else load8s((v12 + (v7 + v13)))))
                break
            v10 = (arg1 - 1)
            v17 = ((arg1 - 1) | v7)
            v11 = 0
            while True:  # block $label2
                v14 = (u(v6) <= u(v10))
                if (u(v6) <= u(v10)):
                    break
                if (u(v6) <= u(v7)):
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
            while True:  # block $label3
                if v14:
                    break
                if (u(arg0) >= u(v6)):
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
            while True:  # block $label4
                if v14:
                    break
                if (u(v6) <= u(v9)):
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
            while True:  # block $label5
                if v8:
                    break
                if (u(v6) <= u(v9)):
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
            while True:  # block $label6
                v22 = (u(v6) <= u(v8))
                if (u(v6) <= u(v8)):
                    break
                if (u(v6) <= u(v9)):
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
            while True:  # block $label7
                if v22:
                    break
                if (u(arg0) >= u(v6)):
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
            while True:  # block $label8
                if v22:
                    break
                if (u(v6) <= u(v7)):
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
            if (v11 == 0):
                break
            if (load32(9147292) >= arg2):
                break
            store16(v15, arg3)
            while True:  # block $label9
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
            while True:  # block $label10
                v4 = load32(9142440)
                if (u(load32(9142440)) <= u(v7)):
                    break
                if (u(arg1) >= u(v4)):
                    break
                if (v16 < 0):
                    break
                if (load8s((load32(9147288) + ((arg1 * v4) + v7))) != arg2):
                    break
                func96(v7, arg1, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # block $label11
                if (u(v4) <= u(v7)):
                    break
                if (u(v4) <= u(v10)):
                    break
                if (v17 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v10) + v7))) != arg2):
                    break
                func96(v7, v10, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # block $label12
                if (u(arg0) >= u(v4)):
                    break
                if (u(v4) <= u(v10)):
                    break
                if (v18 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v10) + arg0))) != arg2):
                    break
                func96(arg0, v10, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # block $label13
                if (u(v4) <= u(v9)):
                    break
                if (u(v4) <= u(v10)):
                    break
                if (v19 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v10) + v9))) != arg2):
                    break
                func96(v9, v10, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # block $label14
                if (u(v4) <= u(v9)):
                    break
                if (u(arg1) >= u(v4)):
                    break
                if (v20 < 0):
                    break
                if (load8s((load32(9147288) + ((arg1 * v4) + v9))) != arg2):
                    break
                func96(v9, arg1, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # block $label15
                if (u(v4) <= u(v9)):
                    break
                if (u(v4) <= u(v8)):
                    break
                if (v21 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v8) + v9))) != arg2):
                    break
                func96(v9, v8, arg2, arg3)
                v4 = load32(9142440)
                break
            while True:  # block $label16
                if (u(arg0) >= u(v4)):
                    break
                if (u(v4) <= u(v8)):
                    break
                if (v13 < 0):
                    break
                if (load8s((load32(9147288) + ((v4 * v8) + arg0))) != arg2):
                    break
                func96(arg0, v8, arg2, arg3)
                v4 = load32(9142440)
                break
            if (u(v4) <= u(v7)):
                break
            if (u(v4) <= u(v8)):
                break
            if (v14 < 0):
                break
            arg0 = v7
            arg1 = v8
            if (load8s((load32(9147288) + (v7 + (v8 * v4)))) == arg2):
                continue
            break
        break

# ------------------------------------------------------------
# $func98
# ------------------------------------------------------------
def func98(arg0, arg1, arg2):
    if (u(arg2) >= u(512)):
        # TODO: i32.extend8_s []
        # TODO: memory.fill []
        return
    while True:  # block $label0
        if (arg2 == 0):
            break
        store8(arg0, arg1)
        v3 = (arg0 + arg2)
        store8(((arg0 + arg2) - 1), arg1)
        if (u(arg2) < u(3)):
            break
        store8(arg0 + 2, arg1)
        store8(arg0 + 1, arg1)
        store8((v3 - 3), arg1)
        store8((v3 - 2), arg1)
        if (u(arg2) < u(7)):
            break
        store8(arg0 + 3, arg1)
        store8((v3 - 4), arg1)
        if (u(arg2) < u(9)):
            break
        v4 = ((0 - arg0) & 3)
        v3 = (arg0 + ((0 - arg0) & 3))
        arg0 = ((arg1 & 255) * 16843009)
        store32((arg0 + ((0 - arg0) & 3)), ((arg1 & 255) * 16843009))
        arg2 = ((arg2 - v4) & -4)
        arg1 = (v3 + ((arg2 - v4) & -4))
        store32(((v3 + ((arg2 - v4) & -4)) - 4), arg0)
        if (u(arg2) < u(9)):
            break
        store32(v3 + 8, arg0)
        store32(v3 + 4, arg0)
        store32((arg1 - 8), arg0)
        store32((arg1 - 12), arg0)
        if (u(arg2) < u(25)):
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
        if (u((arg2 - ((v3 & 4) | 24))) < u(32)):
            break
        v5 = (i64(arg0) * 4294967297)
        arg0 = (arg2 + v3)
        while True:  # $label1
            store64(arg0 + 24, v5)
            store64(arg0 + 16, v5)
            store64(arg0 + 8, v5)
            store64(arg0, v5)
            arg0 = (arg0 + 32)
            arg1 = (arg1 - 32)
            if (u((arg1 - 32)) > u(31)):
                continue
            break
        break

# ------------------------------------------------------------
# $func99
# ------------------------------------------------------------
def func99(arg0, arg1, arg2):
    while True:  # block $label0
        if (arg1 == 5):
            if (load32(arg0 + 48) == 0):
                break
        if (load32(arg0) == 0):
            store32(arg0 + 8, arg2)
            store32(arg0, arg1)
            store32(arg0 + 4, 0)
        return 0
        break
    a_c()
    raise RuntimeError('unreachable')
    return 3476

# ------------------------------------------------------------
# $func100
# ------------------------------------------------------------
def func100(arg0, arg1, arg2):
    v6 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    while True:  # block $label0
        if load8u(9142906):
            arg0 = load32(arg0 + 40)
            if (load32(arg0 + 40) == 0):
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
            if (load32(arg0 + 40) == 0):
                break
            arg0 = load8u(arg0 + 125)
            store32(v6 + 52, arg1)
            store32(v6 + 48, ((arg0 << 8) | 1))
            a_b()
            break
        v4 = load16u(arg0 + 114)
        v9 = load16u(arg0 + 112)
        v10 = load8u(arg0 + 122)
        while True:  # block $label2
            while True:  # block $label1
                v3 = load32(arg0 + 44)
                if (load32(arg0 + 44) == 0):
                    break
                v5 = load32(9215884)
                if (load32((load32(9215884) + (v3 << 4)) + 12) == 1):
                    break
                if (load8u(arg0 + 125) == 7):
                    break
                v3 = (v3 << 4)
                if load32((v5 + ((v3 << 4) | 4))):
                    break
                v7 = load32(((v10 * 404) + 9568096) + 260)
                v3 = (1 if (u(v7) <= u(1)) else load32(((v10 * 404) + 9568096) + 260))
                v5 = (((load32((v3 + v5)) - load32(9142848)) * -25) + (32000 // (1 if (u(v7) <= u(1)) else load32(((v10 * 404) + 9568096) + 260))))
                v8 = (load8u(arg0 + 124) << 3)
                v11 = load32(((load8u(arg0 + 124) << 3) + 8996))
                v12 = (load32(((load8u(arg0 + 124) << 3) + 8996)) * v3)
                v7 = (((((load32((v3 + v5)) - load32(9142848)) * -25) + (32000 // (1 if (u(v7) <= u(1)) else load32(((v10 * 404) + 9568096) + 260)))) * (load32(((load8u(arg0 + 124) << 3) + 8996)) * v3)) // 1000)
                v8 = load32((v8 + 8992))
                v13 = (load32((v8 + 8992)) * v3)
                v3 = ((v5 * (load32((v8 + 8992)) * v3)) // 1000)
                v14 = float(v12)
                v4 = (v4 - v11)
                v9 = (v9 - v8)
                break
                break
            v3 = 0
            break
        v15 = 0.0
        v5 = ((v10 * 404) + 9568096)
        v8 = load32(((v10 * 404) + 9568096) + 216)
        while True:  # block $label3
            if (load32(v5 + 264) != 1):
                break
            if (u(v8) < u(2)):
                break
            while True:  # block $label4
                v5 = ((v10 * 404) + 9568096)
                v11 = load32(((v10 * 404) + 9568096) + 392)
                if load32(((v10 * 404) + 9568096) + 392):
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
            v16 = float((v3 + (v9 << 5)))
            v17 = float((v7 + (v4 << 5)))
            v19 = float(v4)
            v20 = (float(v4) * 32.0)
            # TODO: f32.convert_i32_u []
            v7 = ((v10 * 404) + 9568096)
            # TODO: f32.convert_i32_u []
            v18 = v11
            v4 = 0
            while True:  # block $label5
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
                if (u(arg1) < u(load32(9163784))):
                    break
                store32(v6 + 32, v3)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            # TODO: f32.convert_i32_u []
            v21 = v8
            func120(arg0, v4, 1)
            v18 = (v18 + v16)
            # TODO: f32.convert_i32_u []
            while True:  # block $label6
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
                if (u(arg1) < u(load32(9163784))):
                    break
                store32(v6 + 16, v4)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            func120(arg0, v5, 1)
            v16 = (v21 + v17)
            v17 = (v19 * 32.0)
            # TODO: f32.convert_i32_u []
            v4 = 0
            while True:  # block $label7
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
                if (u(arg1) < u(load32(9163784))):
                    break
                store32(v6, v3)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            func120(arg0, v4, 1)
            # TODO: f32.convert_i32_u []
            break
            break
        # TODO: f32.convert_i32_u []
        break
    G.global0 = (v6 + 96)
    return func40(float((v3 + (v9 << 5))), float((v7 + (v4 << 5))), (((float(v4) * 32.0) + ((load32(9142440) * 32.0) * float(load32(v5 + 208)))) + -1.0), v15, v14, 0.0, 0.0, 0.0, -1.0, load32((9142744 if (u(v8) > u(1)) else 9142448)), arg2, arg1, 0, 0, 0, 0.0)

# ------------------------------------------------------------
# $func101
# ------------------------------------------------------------
def func101(arg0):
    v3 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # block $label0
        if (load32(arg0 + 40) == 0):
            break
        v10 = load32(38560)
        v11 = load16u(arg0 + 114)
        v6 = load16u(arg0 + 112)
        v9 = load8u(arg0 + 122)
        v12 = ((load8u(arg0 + 122) * 404) + 9568096)
        while True:  # block $label1
            v1 = load32(arg0 + 12)
            if (load32(arg0 + 12) == 0):
                break
            v7 = load32(v1 + 8)
            if (load32(v1 + 8) == 0):
                break
            while True:  # $label3
                v4 = (load32(v1) + (v2 << 2))
                if (load32((load32(v1) + (v2 << 2)) + 4) == 0):
                    func38(load32(v4))
                    v1 = load32(arg0 + 12)
                    v7 = (load32(v1 + 8) - 2)
                    store32(load32(arg0 + 12) + 8, (load32(v1 + 8) - 2))
                    if (u(v2) < u(v7)):
                        v8 = load32(v1)
                        v4 = v2
                        while True:  # $label2
                            v5 = (v8 + (v4 << 2))
                            store32((v8 + (v4 << 2)), load32(v5 + 8))
                            v4 = (v4 + 1)
                            v7 = load32(v1 + 8)
                            if (u((v4 + 1)) < u(load32(v1 + 8))):
                                continue
                            break
                    v2 = (v2 - 2)
                v2 = (v2 + 2)
                if (u((v2 + 2)) < u(v7)):
                    continue
                break
            break
        if (load32(v12 + 20) == 0):
            break
        # TODO: f32.convert_i32_u []
        v16 = (v11 * 32.0)
        v17 = (((v11 * 32.0) + 192.0) if (v9 == v10) else v16)
        v18 = ((((v11 * 32.0) + 192.0) if (v9 == v10) else v16) + -1.0)
        v14 = ((v9 * 404) + 9568304)
        # TODO: f64.promote_f32 []
        v20 = v16
        # TODO: f32.convert_i32_u []
        v19 = (v6 * 32.0)
        # TODO: f64.promote_f32 []
        v21 = (v6 * 32.0)
        v11 = (v3 - -64)
        v7 = 0
        while True:  # $label8
            while True:  # block $label5
                while True:  # block $label4
                    v1 = load32((v12 + (v7 << 2)))
                    if (load32(load32((v12 + (v7 << 2))) + 32) == 6):
                        v2 = 7
                        if load8u(40588):
                            break
                        break
                    v4 = load8u(arg0 + 127)
                    v2 = (load8u(arg0 + 127) if v4 else (load16u(arg0 + 110) + 16))
                    # TODO: f32.convert_i32_u []
                    break
                v15 = ((((load32(9142440) * 32.0) * float(load32(v14))) + v17) + 1.0)
                v9 = func244(v1)
                func120(arg0, func244(v1), 0)
                v13 = load32(v1 + 32)
                if load8u(9142916):
                    if (v13 == 6):
                        # TODO: f32.convert_i32_u []
                        v15 = (((load32(9142440) * 32.0) * float(load32(v14))) + v17)
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
                    while True:  # block $label6
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
                        # TODO: f32.convert_i32_u []
                        v15 = (((v15 * 0.5) / (load32(9142440) * 96)) + 0.25)
                    store32(v3 + 76, v9)
                    store32(v3 + 72, 0)
                    store32(v11, (2130706431 if (v13 == 6) else 0))
                    store64(v3 + 56, 0)
                    store32(v3 + 52, (0 - v1))
                    store32(v3 + 48, v2)
                    store64(v3 + 40, 0)
                    store64(v3 + 32, 0)
                    store64(v3 + 24, 0)
                    # TODO: f64.promote_f32 []
                    store32(v3 + 16, v15)
                    store32(v3 + 68, ((v4 << 16) | 65535))
                    store32(v3 + 8, v20)
                    store32(v3, v21)
                    a_b()
                    break
                v5 = (v13 == 22)
                v4 = load8u(arg0 + 124)
                v8 = 1
                while True:  # block $label7
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
            if (u((v7 + 1)) < u(load32(v12 + 20))):
                continue
            break
        break
    G.global0 = (v3 + 80)
    return func40(v19, v16, v15, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, v1, v2, v9, v5, v4, v8, 0.0)

# ------------------------------------------------------------
# $func102
# ------------------------------------------------------------
def func102(arg0, arg1, arg2):
    v3 = (G.global0 - 192)
    G.global0 = (G.global0 - 192)
    while True:  # block $label0
        if load8u(9142917):
            break
        v7 = load8u(arg0 + 122)
        v5 = load8u(arg0 + 122)
        v6 = load32(arg0 + 40)
        if (load32(arg0 + 40) == 0):
            while True:  # block $label1
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
                if (u(v4) < u(load32(9163784))):
                    break
                store32(v3 + 176, v5)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                break
            v5 = load8u(arg0 + 122)
            store32(arg0 + 40, v6)
        if ((arg1 | load32(((v5 * 72) + 9263856))) == 0):
            arg0 = ((v5 << 2) + 9560016)
            if load32(((v5 << 2) + 9560016)):
                break
            store32(arg0, load32(9671136))
            break
        while True:  # block $label3
            if load8u(9142916):
                store32(arg0 + 48, arg1)
                v4 = load8u(arg0 + 127)
                if (u(((load8u(arg0 + 127) - 1) & 255)) <= u(13)):
                    v4 = (v4 << 4)
                    v8 = ((((load32(((v4 << 4) + 1748)) << 8) + load32((v4 + 1744))) + (load32((v4 + 1752)) << 16)) + (load32((v4 + 1756)) << 24))
                v4 = load16u(arg0 + 114)
                v10 = (load16u(arg0 + 114) << 5)
                v11 = (load16u(arg0 + 112) << 5)
                v14 = load32(9142440)
                # TODO: f32.convert_i32_u []
                v17 = ((((load32(9142440) * load32(((v5 * 404) + 9568096) + 208)) + v4) << 5) | 1)
                while True:  # block $label2
                    if (arg1 == 0):
                        break
                    if (load32(arg1 + 20) == 0):
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
                # TODO: f32.convert_i32_u []
                # TODO: f64.promote_f32 []
                store32(v3 + 112, (((v17 * 0.5) / (v14 * 96)) + 0.25))
                store32(v3 + 104, float(v10))
                store32(v3 + 96, float(v11))
                a_b()
                break
            if arg1:
            func92(arg0, 0.0, 0.0)
            break
        if arg2:
            break
        if (load32(((v7 * 404) + 9568096) + 20) == 0):
            break
        while True:  # block $label4
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
        while True:  # block $label5
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
            if (u(v6) < u(load32(9163784))):
                break
            store32(v3 + 80, v5)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        func120(arg0, arg1, 0)
        v9 = load32(9142440)
        # TODO: f32.convert_i32_u []
        v6 = (load16u(arg0 + 114) << 5)
        v17 = (((load32(9142440) * 32.0) * float(load32(((load8u(arg0 + 122) * 404) + 9568096) + 208))) + float((load16u(arg0 + 114) << 5)))
        v4 = (v4 + v6)
        v5 = ((load16u(arg0 + 112) << 5) + arg2)
        if load8u(9142916):
            v17 = (v17 + 30.0)
            v6 = 0
            while True:  # block $label6
                arg2 = load32(9142740)
                if (load32(9142740) == 0):
                    break
                if (load32(arg2 + 20) == 0):
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
                # TODO: f32.convert_i32_u []
            else:
            # TODO: f64.promote_f32 []
            store32((((v17 * 0.5) / (v9 * 96)) + 0.25) + 16, v17)
            store32(v3 + 68, ((arg0 << 16) | 65535))
            store32(v3 + 8, float(v4))
            store32(v3, float(v5))
            a_b()
            break
        break
    G.global0 = (v3 + 192)
    return func40(float(v5), float(v4), v17, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, load32(9142740), (load16u(arg0 + 110) + 16), arg1, 1, 0, 0, 0.0)

# ------------------------------------------------------------
# $func103
# ------------------------------------------------------------
def func103(arg0):
    v4 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label0
        v1 = load32(9142872)
        if (load32(9142872) == 0):
            break
        if (v1 != load16u(arg0 + 110)):
            break
        v10 = load8u(arg0 + 122)
        if (load8u(arg0 + 122) == load32(38564)):
            break
        if load8u(9142917):
            break
        v11 = load16u(arg0 + 112)
        v1 = ((v10 * 404) + 9568096)
        v12 = load16u(arg0 + 114)
        v7 = ((load16u(arg0 + 112) + ((load32(((v10 * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1)) + ((load16u(arg0 + 114) + ((load32(v1 + 220) & 0xFFFFFFFF) >> 1)) << 16))
        v2 = load32(9216048)
        if load32(9216048):
            v5 = load32(9142848)
            v6 = load32(9216040)
            while True:  # $label2
                v1 = (v3 << 2)
                v8 = load32((v6 + (v3 << 2)))
                while True:  # block $label1
                    v1 = ((v5 - load32((v6 + (v1 | 4)))) * 25)
                    if (u(((v5 - load32((v6 + (v1 | 4)))) * 25)) <= u(19999)):
                        v1 = ((v8 & 65535) - v11)
                        v1 = (((v8 & 0xFFFFFFFF) >> 16) - v12)
                        if ((((((v8 & 65535) - v11) * v1) + ((((v8 & 0xFFFFFFFF) >> 16) - v12) * v1)) - 1) >= 3601):
                            break
                        break
                    v9 = (((v7 == v8) & (u(v1) < u(35000))) | v9)
                    break
                v3 = (v3 + 2)
                if (u((v3 + 2)) < u(v2)):
                    continue
                break
            v3 = 0
            v6 = load32(9216040)
            v5 = load32(9142848)
            while True:  # $label3
                v1 = (v6 + ((v3 << 2) | 4))
                if (u(((v5 - load32((v6 + ((v3 << 2) | 4)))) * 25)) >= u(35001)):
                    store32((v6 + (v3 << 2)), v7)
                    store32(v1, load32(9142848))
                    arg0 = load32(((v10 * 404) + 9568096) + 264)
                    store32(v4 + 28, (v9 & 1))
                    store32(v4 + 20, v12)
                    store32(v4 + 16, v11)
                    store32(v4 + 24, (arg0 == 1))
                    break
                v3 = (v3 + 2)
                if (u((v3 + 2)) < u(v2)):
                    continue
                break
        while True:  # block $label4
            if (load32(9216044) != v2):
                v1 = load32(9216040)
                break
            v1 = (load32(9216052) + v2)
            store32(9216044, (load32(9216052) + v2))
            v5 = load32(9216040)
            v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
            if v2:
                # TODO: memory.copy []
            if v5:
                v2 = load32(9216048)
            store32(9216040, v1)
            break
        store32(9216048, (v2 + 1))
        store32((v1 + (v2 << 2)), v7)
        v5 = load32(9142848)
        while True:  # block $label5
            v3 = load32(9216048)
            if (load32(9216048) != load32(9216044)):
                v2 = v1
                break
            v2 = (load32(9216052) + v3)
            store32(9216044, (load32(9216052) + v3))
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if v3:
                # TODO: memory.copy []
            store32(9216040, v2)
            v3 = load32(9216048)
            break
        store32(9216048, (v3 + 1))
        store32((v2 + (v3 << 2)), v5)
        v2 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 264)
        v1 = load16u(arg0 + 112)
        arg0 = load16u(arg0 + 114)
        store32(v4 + 12, (v9 & 1))
        store32(v4 + 4, arg0)
        store32(v4, v1)
        store32(v4 + 8, (v2 == 1))
        break
    G.global0 = (v4 + 32)

# ------------------------------------------------------------
# $func105
# ------------------------------------------------------------
def func105(arg0, arg1):
    while True:  # block $label0
        v2 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            v3 = load32(arg0)
            break
        v3 = (load32(arg0 + 12) + v2)
        store32(arg0 + 4, (load32(arg0 + 12) + v2))
        v4 = load32(arg0)
        v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
        if v2:
            # TODO: memory.copy []
        if v4:
            v2 = load32(arg0 + 8)
        store32(arg0, v3)
        break
    store32(arg0 + 8, (v2 + 1))
    store32((v3 + (v2 << 2)), arg1)

# ------------------------------------------------------------
# $func106
# ------------------------------------------------------------
def func106(arg0, arg1, arg2, arg3):
    v10 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label1
        while True:  # block $label2
            while True:  # block $label0
                if (u(load32(9142848)) >= u((load32(load32(9142424) + 72) * 2400))):
                    break
                v5 = load8u(arg0 + 122)
                if (load32(arg0 + 56) == 1):
                    if (load32(((v5 * 404) + 9568096) + 268) == 1):
                        break
                if (load8u(((v5 * 404) + 9568096) + 336) == 0):
                    break
                if (load16u(arg0 + 120) == 0):
                    break
                break
                break
            if load16u(arg0 + 120):
                break
            v5 = load8u(arg0 + 122)
            break
        store32(v10 + 12, 0)
        v4 = ((v5 * 404) + 9568096)
        v14 = load32(((v5 * 404) + 9568096) + 200)
        v7 = load32(((v5 * 404) + 9568096) + 200)
        if (load32(v4 + 268) == 1):
            v7 = load32(v4 + 224)
        v8 = load16u(arg0 + 114)
        v11 = load16u(arg0 + 112)
        v15 = load16u(arg0 + 110)
        v16 = (load16u(arg0 + 110) * 286704)
        v6 = load32(9561692)
        while True:  # block $label5
            while True:  # block $label3
                while True:  # block $label4
                    # br_table[load32(v4 + 264)]
                    break
                    break
                v4 = ((v5 * 404) + 9568096)
                v9 = load32(((v5 * 404) + 9568096) + 216)
                if (load32(((v5 * 404) + 9568096) + 216) == 0):
                    break
                v13 = load32(v4 + 220)
                if (load32(v4 + 220) == 0):
                    break
                v4 = load32(9215880)
                if (load32(9215880) == 0):
                    break
                v17 = load32(9142432)
                if (load32(9142432) == 0):
                    break
                v18 = load32(9142440)
                v19 = load32(v4)
                v5 = 0
                while True:  # $label7
                    v20 = (v5 + v11)
                    v4 = 0
                    while True:  # $label6
                        v12 = load32((v17 + ((v20 + ((v4 + v8) * v18)) << 2)))
                        if (load32((v19 + (load32((v17 + ((v20 + ((v4 + v8) * v18)) << 2))) << 2))) == 0):
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
            if (load32(9142432) == 0):
                break
            v12 = load32((v4 + (((load32(9142440) * v8) + v11) << 2)))
            break
        v16 = (v6 + v16)
        v4 = load8u(arg0 + 127)
        store32(v10 + 8, 2147483647)
        while True:  # block $label9
            while True:  # block $label8
                if load8u(9216060):
                    v5 = load8u(9671158)
                    v6 = load8u(9671157)
                    break
                v6 = load8u(9671157)
                v5 = load8u(9671158)
                if (u(load32((v6 + (v15 * 286704)) + 283924)) > u((((v7 * v7) * (((load8u(9671157) + load8u(9671158)) + 1) & 255)) * 3))):
                    break
                if (v4 == 6):
                    break
                v6 = 0
                v4 = load32(9142892)
                if (load32(9142892) == 0):
                    break
                while True:  # $label14
                    if load8u((load32(9143004) + ((v4 * v15) + v6))):
                        v7 = load32(9561692)
                        arg2 = 0
                        while True:  # $label13
                            while True:  # block $label10
                                arg3 = ((arg2 * 404) + 9568096)
                                if (load32(((arg2 * 404) + 9568096) + 264) == 2):
                                    break
                                if (load32(arg3 + 188) != 55):
                                    break
                                v5 = load32((((v7 + (v6 * 286704)) + (arg2 << 2)) + 284636))
                                if (load32((((v7 + (v6 * 286704)) + (arg2 << 2)) + 284636)) == 0):
                                    break
                                v4 = 0
                                v8 = load32(v5 + 8)
                                if (load32(v5 + 8) == 0):
                                    break
                                while True:  # $label12
                                    while True:  # block $label11
                                        arg3 = load32((load32(v5) + (v4 << 2)))
                                        if (load32((load32(v5) + (v4 << 2))) == 0):
                                            break
                                        arg3 = (load32(9671128) + (arg3 * 132))
                                        if load32((load32(9671128) + (arg3 * 132)) + 36):
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
                        v4 = load32(9142892)
                    v6 = (v6 + 1)
                    if (u((v6 + 1)) < u(v4)):
                        continue
                    break
                break
                break
            v14 = (load32(9142836) + (v7 * 80))
            v9 = load32((load32(9142836) + (v7 * 80)) + 4)
            if (load32((load32(9142836) + (v7 * 80)) + 4) == 0):
                break
            v13 = (v8 if (arg3 == -1) else arg3)
            v11 = (v11 if (arg2 == -1) else arg2)
            v17 = (v5 | 2)
            arg2 = ((v6 & 255) == 0)
            v18 = (v4 == 6)
            v5 = load32(9142440)
            v6 = 0
            while True:  # $label17
                while True:  # block $label15
                    arg3 = load32(v14)
                    v4 = (v6 << 2)
                    v7 = (load32((load32(v14) + ((v6 << 2) | 4))) + v13)
                    if (u(v5) <= u((load32((load32(v14) + ((v6 << 2) | 4))) + v13))):
                        break
                    v8 = (load32((arg3 + v4)) + v11)
                    if (u(v5) <= u((load32((arg3 + v4)) + v11))):
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
                        if (u(load32((arg3 + ((v19 + ((v20 + ((v5 + 2) * v4)) * v21)) << 2)))) >= u(3)):
                            v5 = load32(9142440)
                            arg3 = load32(9142840)
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v17):
                            continue
                        break
                    break
                v6 = (v6 + 2)
                if (u((v6 + 2)) < u(v9)):
                    continue
                break
            break
        v4 = load32(v10 + 12)
        break
    G.global0 = (v10 + 16)
    return v4

# ------------------------------------------------------------
# $func107
# ------------------------------------------------------------
def func107(arg0, arg1, arg2, arg3, arg4):
    v5 = (G.global0 - 256)
    G.global0 = (G.global0 - 256)
    while True:  # block $label0
        if (arg2 <= arg3):
            break
        if (arg4 & 73728):
            break
        arg3 = (arg2 - arg3)
        arg1 = (u(arg3) < u(256))
        func98(v5, (arg1 & 255), ((arg2 - arg3) if (u(arg3) < u(256)) else 256))
        if (arg1 == 0):
            while True:  # $label1
                arg3 = (arg3 - 256)
                if (u((arg3 - 256)) > u(255)):
                    continue
                break
        break
    G.global0 = (v5 + 256)

# ------------------------------------------------------------
# $func108
# ------------------------------------------------------------
def func108(arg0, arg1, arg2, arg3):
    arg3 = ((arg3 << 1) | 1)
    v12 = (((((arg3 << 1) | 1) * arg3) << 1) - 2)
    if (((((arg3 << 1) | 1) * arg3) << 1) - 2):
        v6 = (load32(9142892) * arg2)
        v11 = load32(9142440)
        arg3 = (load32(9142440) + 2)
        v13 = ((load32(9142440) + 2) << 1)
        v7 = load32(9143004)
        v8 = load32(9671128)
        v9 = load32(9142840)
        arg2 = 0
        while True:  # $label3
            while True:  # block $label0
                v4 = (arg2 << 2)
                v5 = (load32((((arg2 << 2) | 4) + 8611904)) + arg1)
                if (u(v11) <= u((load32((((arg2 << 2) | 4) + 8611904)) + arg1))):
                    break
                v4 = (load32((v4 + 8611904)) + arg0)
                if (u(v11) <= u((load32((v4 + 8611904)) + arg0))):
                    break
                if ((v4 | v5) < 0):
                    break
                while True:  # block $label1
                    v4 = (v4 + 1)
                    v5 = (v5 + 1)
                    v10 = load16u((v8 + (load32((v9 + (((v4 + 1) + ((v5 + 1) * arg3)) << 2))) * 132)) + 110)
                    if (load16u((v8 + (load32((v9 + (((v4 + 1) + ((v5 + 1) * arg3)) << 2))) * 132)) + 110) == 0):
                        break
                    if (load8u((v7 + (v6 + v10))) == 0):
                        break
                    return 0
                    break
                while True:  # block $label2
                    v10 = load16u((v8 + (load32((v9 + ((v4 + ((arg3 + v5) * arg3)) << 2))) * 132)) + 110)
                    if (load16u((v8 + (load32((v9 + ((v4 + ((arg3 + v5) * arg3)) << 2))) * 132)) + 110) == 0):
                        break
                    if (load8u((v7 + (v6 + v10))) == 0):
                        break
                    return 0
                    break
                v5 = load16u((v8 + (load32((v9 + ((v4 + ((v5 + v13) * arg3)) << 2))) * 132)) + 110)
                if (load16u((v8 + (load32((v9 + ((v4 + ((v5 + v13) * arg3)) << 2))) * 132)) + 110) == 0):
                    break
                if (load8u((v7 + (v5 + v6))) == 0):
                    break
                return 0
                break
            arg2 = (arg2 + 2)
            if (u((arg2 + 2)) < u(v12)):
                continue
            break
    return 1

# ------------------------------------------------------------
# $func111
# ------------------------------------------------------------
def func111(arg0, arg1):
    while True:  # block $label0
        if (arg0 == 0):
            break
        if (arg1 < 0):
            break
        if (arg0 & 3):
            break
        if (arg1 == 0):
            return
        # TODO: i32.atomic.rmw.cmpxchg [('offset', 9688024)]
        v2 = 0
        v2 = (arg0 if (arg0 == v2) else 0)
        while True:  # block $label1
            if (arg1 == 2147483647):
                break
            if (arg0 != v2):
                break
            if (u(arg1) < u(2)):
                break
            arg1 = (arg1 - 1)
            break
        # TODO: memory.atomic.notify []
        break

# ------------------------------------------------------------
# $func112
# ------------------------------------------------------------
def func112(arg0, arg1):
    v5 = load32(9142892)
    v9 = (load32(9142892) * v5)
    v7 = func26((load32(9142892) * v5))
    # TODO: memory.fill []
    v8 = func26(v9)
    # TODO: memory.fill []
    v11 = (v5 if (u(arg0) > u(v5)) else arg0)
    while True:  # block $label0
        if (arg0 == 0):
            break
        if (load8u(9147208) == 0):
            break
        if (u(v5) >= u(2)):
            v2 = (v5 - 1)
            v12 = ((v5 - 1) & -4)
            v10 = (v2 & 3)
            v13 = (u((v5 - 2)) < u(3))
            v3 = 1
            while True:  # $label3
                v6 = (v3 * v5)
                v4 = 0
                v2 = 1
                if (v13 == 0):
                    while True:  # $label1
                        store8((v7 + (v2 + v6)), (v2 != v3))
                        v14 = (v2 + 1)
                        store8((v7 + ((v2 + 1) + v6)), (v3 != v14))
                        v14 = (v2 + 2)
                        store8((v7 + ((v2 + 2) + v6)), (v3 != v14))
                        v14 = (v2 + 3)
                        store8((v7 + ((v2 + 3) + v6)), (v3 != v14))
                        v2 = (v2 + 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v12):
                            continue
                        break
                v4 = 0
                if v10:
                    while True:  # $label2
                        store8((v7 + (v2 + v6)), (v2 != v3))
                        v2 = (v2 + 1)
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v10):
                            continue
                        break
                v3 = (v3 + 1)
                if ((v3 + 1) != v5):
                    continue
                break
        if (u(v11) < u(2)):
            break
        v2 = (v11 - 1)
        v14 = ((v11 - 1) & -4)
        v13 = (v2 & 3)
        v6 = load32(9143004)
        v15 = (u((v11 - 2)) < u(3))
        v3 = 1
        while True:  # $label6
            v10 = (v3 * v5)
            v12 = (arg0 * v3)
            v2 = 1
            v4 = 0
            if (v15 == 0):
                while True:  # $label4
                    store8((v7 + (v2 + v10)), load8u((v6 + (v2 + v12))))
                    v16 = (v2 + 1)
                    store8((v7 + ((v2 + 1) + v10)), load8u((v6 + (v12 + v16))))
                    v16 = (v2 + 2)
                    store8((v7 + ((v2 + 2) + v10)), load8u((v6 + (v12 + v16))))
                    v16 = (v2 + 3)
                    store8((v7 + ((v2 + 3) + v10)), load8u((v6 + (v12 + v16))))
                    v2 = (v2 + 4)
                    v4 = (v4 + 4)
                    if ((v4 + 4) != v14):
                        continue
                    break
            v4 = 0
            if v13:
                while True:  # $label5
                    store8((v7 + (v2 + v10)), load8u((v6 + (v2 + v12))))
                    v2 = (v2 + 1)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v13):
                        continue
                    break
            v3 = (v3 + 1)
            if ((v3 + 1) != v11):
                continue
            break
        break
    while True:  # block $label7
        if ((arg0 == 0) & (arg1 ^ 1)):
            break
        if (load8u(9147209) == 0):
            break
        if (u(v5) >= u(2)):
            arg1 = (v5 - 1)
            v10 = ((v5 - 1) & -4)
            v6 = (arg1 & 3)
            v12 = (u((v5 - 2)) < u(3))
            v3 = 1
            while True:  # $label10
                arg1 = (v3 * v5)
                v4 = 0
                v2 = 1
                if (v12 == 0):
                    while True:  # $label8
                        store8((v8 + (arg1 + v2)), (v2 == v3))
                        v13 = (v2 + 1)
                        store8((v8 + ((v2 + 1) + arg1)), (v3 == v13))
                        v13 = (v2 + 2)
                        store8((v8 + ((v2 + 2) + arg1)), (v3 == v13))
                        v13 = (v2 + 3)
                        store8((v8 + ((v2 + 3) + arg1)), (v3 == v13))
                        v2 = (v2 + 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v10):
                            continue
                        break
                v4 = 0
                if v6:
                    while True:  # $label9
                        store8((v8 + (arg1 + v2)), (v2 == v3))
                        v2 = (v2 + 1)
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v6):
                            continue
                        break
                v3 = (v3 + 1)
                if ((v3 + 1) != v5):
                    continue
                break
        if (u(v11) < u(2)):
            break
        arg1 = (v11 - 1)
        v13 = ((v11 - 1) & -4)
        v12 = (arg1 & 3)
        arg1 = load32(9143012)
        v14 = (u((v11 - 2)) < u(3))
        v3 = 1
        while True:  # $label13
            v6 = (v3 * v5)
            v10 = (arg0 * v3)
            v2 = 1
            v4 = 0
            if (v14 == 0):
                while True:  # $label11
                    store8((v8 + (v2 + v6)), load8u((arg1 + (v2 + v10))))
                    v15 = (v2 + 1)
                    store8((v8 + ((v2 + 1) + v6)), load8u((arg1 + (v10 + v15))))
                    v15 = (v2 + 2)
                    store8((v8 + ((v2 + 2) + v6)), load8u((arg1 + (v10 + v15))))
                    v15 = (v2 + 3)
                    store8((v8 + ((v2 + 3) + v6)), load8u((arg1 + (v10 + v15))))
                    v2 = (v2 + 4)
                    v4 = (v4 + 4)
                    if ((v4 + 4) != v13):
                        continue
                    break
            v4 = 0
            if v12:
                while True:  # $label12
                    store8((v8 + (v2 + v6)), load8u((arg1 + (v2 + v10))))
                    v2 = (v2 + 1)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v12):
                        continue
                    break
            v3 = (v3 + 1)
            if ((v3 + 1) != v11):
                continue
            break
        break
    while True:  # block $label14
        arg0 = load32(9143004)
        if (load32(9143004) == 0):
            break
        store32(9143004, 0)
        arg0 = load32(9143008)
        if load32(9143008):
            store32(9143008, 0)
        arg0 = load32(9143016)
        if load32(9143016):
            store32(9143016, 0)
        if load8u(9147209):
            break
        arg0 = load32(9143012)
        if (load32(9143012) == 0):
            break
        break
    store32(9143012, v8)
    store32(9143004, v7)
    arg1 = func26(v9)
    # TODO: memory.fill []
    store32(9143008, arg1)
    arg0 = func26(v9)
    # TODO: memory.fill []
    store32(9143016, arg0)
    while True:  # block $label15
        arg0 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v4 = (arg0 - 1)
        v5 = ((arg0 - 1) & 3)
        v2 = 1
        v11 = (arg0 - 2)
        if (u((arg0 - 2)) >= u(3)):
            v8 = (v4 & -4)
            v3 = 0
            while True:  # $label16
                store8((v7 + (arg0 * v2)), 1)
                store8((v2 + v7), 1)
                v9 = (v2 + 1)
                store8((v7 + (arg0 * (v2 + 1))), 1)
                store8((v7 + v9), 1)
                v9 = (v2 + 2)
                store8((v7 + (arg0 * (v2 + 2))), 1)
                store8((v7 + v9), 1)
                v9 = (v2 + 3)
                store8((v7 + (arg0 * (v2 + 3))), 1)
                store8((v7 + v9), 1)
                v2 = (v2 + 4)
                v3 = (v3 + 4)
                if ((v3 + 4) != v8):
                    continue
                break
        if v5:
            v3 = 0
            while True:  # $label17
                store8((v7 + (arg0 * v2)), 1)
                store8((v2 + v7), 1)
                v2 = (v2 + 1)
                v3 = (v3 + 1)
                if ((v3 + 1) != v5):
                    continue
                break
        if (u(arg0) < u(2)):
            break
        if (load8u(9147208) == 0):
            v3 = load32(9561692)
            v4 = 1
            while True:  # $label20
                v5 = (arg0 * v4)
                v8 = ((v3 + (v4 * 286704)) + 284608)
                v2 = 1
                while True:  # $label19
                    v11 = (v2 + v5)
                    while True:  # block $label18
                        v9 = (v2 == v4)
                        if (v2 == v4):
                            break
                        v6 = load32(v8)
                        if (load32(v8) == 0):
                            break
                        break
                    store8((v7 + (v2 + v5)), ((v6 == load32((v3 + (v2 * 286704)) + 284608)) ^ 1))
                    store8((arg1 + v11), v9)
                    v2 = (v2 + 1)
                    if ((v2 + 1) != arg0):
                        continue
                    break
                v4 = (v4 + 1)
                if ((v4 + 1) != arg0):
                    continue
                break
            break
        v9 = (v4 & -4)
        v8 = (v4 & 3)
        v3 = 1
        while True:  # $label23
            v5 = (arg0 * v3)
            v4 = 0
            v2 = 1
            if (u(v11) >= u(3)):
                while True:  # $label21
                    store8((arg1 + (v2 + v5)), (v2 == v3))
                    v6 = (v2 + 1)
                    store8((arg1 + ((v2 + 1) + v5)), (v3 == v6))
                    v6 = (v2 + 2)
                    store8((arg1 + ((v2 + 2) + v5)), (v3 == v6))
                    v6 = (v2 + 3)
                    store8((arg1 + ((v2 + 3) + v5)), (v3 == v6))
                    v2 = (v2 + 4)
                    v4 = (v4 + 4)
                    if ((v4 + 4) != v9):
                        continue
                    break
            v4 = 0
            if v8:
                while True:  # $label22
                    store8((arg1 + (v2 + v5)), (v2 == v3))
                    v2 = (v2 + 1)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v8):
                        continue
                    break
            v3 = (v3 + 1)
            if ((v3 + 1) != arg0):
                continue
            break
        break
    while True:  # block $label24
        if load8u(9147209):
            break
        v2 = 0
        arg1 = (arg0 * arg0)
        arg0 = func26((arg0 * arg0))
        # TODO: memory.fill []
        store32(9143012, arg0)
        if (arg1 == 0):
            break
        if (u(arg1) >= u(4)):
            v4 = (arg1 & -4)
            v3 = 0
            while True:  # $label25
                store8((arg0 + v2), (load8u((v2 + v7)) ^ 1))
                v5 = (v2 | 1)
                store8((arg0 + (v2 | 1)), (load8u((v5 + v7)) ^ 1))
                v5 = (v2 | 2)
                store8((arg0 + (v2 | 2)), (load8u((v5 + v7)) ^ 1))
                v5 = (v2 | 3)
                store8((arg0 + (v2 | 3)), (load8u((v5 + v7)) ^ 1))
                v2 = (v2 + 4)
                v3 = (v3 + 4)
                if ((v3 + 4) != v4):
                    continue
                break
        arg1 = (arg1 & 3)
        if ((arg1 & 3) == 0):
            break
        v3 = 0
        while True:  # $label26
            store8((arg0 + v2), (load8u((v2 + v7)) ^ 1))
            v2 = (v2 + 1)
            v3 = (v3 + 1)
            if ((v3 + 1) != arg1):
                continue
            break
        break
    return arg1

# ------------------------------------------------------------
# $func113
# ------------------------------------------------------------
def func113(arg0, arg1):
    if (load8u(9142917) == 0):
        v5 = ((load32(9142848) * 25) + arg0)
        while True:  # block $label4
            while True:  # block $label0
                v2 = load32(9299864)
                if load32(9299864):
                    arg0 = 0
                    v4 = load32(9299856)
                    while True:  # $label1
                        v3 = (v4 + (arg0 << 2))
                        if (load32((v4 + (arg0 << 2))) == 0):
                            break
                        arg0 = (arg0 + 2)
                        if (u((arg0 + 2)) < u(v2)):
                            continue
                        break
                while True:  # block $label2
                    if (load32(9299860) != v2):
                        v3 = load32(9299856)
                        break
                    arg0 = (load32(9299868) + v2)
                    store32(9299860, (load32(9299868) + v2))
                    v4 = load32(9299856)
                    v3 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                    if v2:
                        # TODO: memory.copy []
                    if v4:
                        v2 = load32(9299864)
                    store32(9299856, v3)
                    break
                store32(9299864, (v2 + 1))
                store32((v3 + (v2 << 2)), v5)
                while True:  # block $label3
                    arg0 = load32(9299864)
                    if (load32(9299864) != load32(9299860)):
                        v2 = v3
                        break
                    v2 = (load32(9299868) + arg0)
                    store32(9299860, (load32(9299868) + arg0))
                    v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy []
                    store32(9299856, v2)
                    arg0 = load32(9299864)
                    break
                store32(9299864, (arg0 + 1))
                break
                break
            store32(v3, v5)
            break
        store32((v4 + ((arg0 << 2) | 4)), arg1)
    return (v2 + (arg0 << 2))

# ------------------------------------------------------------
# $func114
# ------------------------------------------------------------
def func114(arg0):
    if arg0:
        # TODO: memory.fill []
    store32(9142848, 0)
    store32(9142440, 0)
    store32(59176, 0)
    store32(9140328, 0)
    store32(9142872, 0)
    store32(9561752, 0)
    store32(9561756, 0)
    v1 = load32(9568068)
    v2 = load32(9568064)
    if (load32(9568068) != load32(9568064)):
        while True:  # $label0
            arg0 = (v1 - 128)
            v3 = load32((v1 - 128) + 12)
            if load32((v1 - 128) + 12):
                store32((v1 - 112), v3)
            v3 = load32(arg0)
            if load32(arg0):
                store32((v1 - 124), v3)
            v1 = arg0
            if (arg0 != v2):
                continue
            break
        store32(9568068, v2)
    store32(9684468, 0)
    store32(9684452, 0)
    store32(9684484, 0)
    arg0 = load32(9143004)
    if load32(9143004):
        store32(9143004, 0)
    arg0 = load32(9143008)
    if load32(9143008):
        store32(9143008, 0)
    arg0 = load32(9147288)
    if load32(9147288):
        store32(9147288, 0)
    arg0 = load32(9147376)
    if load32(9147376):
        store32(9147376, 0)
    arg0 = load32(9142400)
    if load32(9142400):
        store32(9142400, 0)
    arg0 = load32(9142840)
    if load32(9142840):
        store32(9142840, 0)
    arg0 = load32(9142432)
    if load32(9142432):
        store32(9142432, 0)
    arg0 = load32(9142436)
    if load32(9142436):
        store32(9142436, 0)
    if load32(9671136):
        v2 = load32(9671128)
        if load32(9671128):
            v4 = (v2 - 4)
            arg0 = load32((v2 - 4))
            if load32((v2 - 4)):
                v1 = (v2 + (arg0 * 132))
                while True:  # $label1
                    arg0 = (v1 - 132)
                    v3 = load32((v1 - 132))
                    if load32((v1 - 132)):
                        store32((v1 - 128), v3)
                    v1 = arg0
                    if (arg0 != v2):
                        continue
                    break
            store32(9671128, 0)
        store32(9671132, 10000)
        arg0 = func26(1320004)
        store32(func26(1320004), 10000)
        v2 = (arg0 + 1320004)
        v3 = (arg0 + 4)
        arg0 = (arg0 + 4)
        while True:  # $label2
            # TODO: memory.fill []
            v1 = func26(4)
            store32(arg0 + 4, func26(4))
            store32(arg0, v1)
            store32(arg0 + 8, (v1 + 4))
            arg0 = (arg0 + 132)
            if ((arg0 + 132) != v2):
                continue
            break
        store32(9671128, v3)
        store64(9671136, 42949672960003)
    arg0 = load32(9681936)
    if load32(9681936):
        store32(arg0 + 8, 0)
    if load32(9215892):
        store64(9215888, 1024)
        v3 = 0
        while True:  # block $label4
            while True:  # block $label3
                arg0 = load32(9215884)
                if (load32(9215884) == 0):
                    v2 = func26(4096)
                    break
                v3 = load32(9215892)
                arg0 = load32(9215888)
                v1 = func26((-1 if (u(arg0) > u(1073741823)) else (load32(9215888) << 2)))
                store32(9215884, func26((-1 if (u(arg0) > u(1073741823)) else (load32(9215888) << 2))))
                if (arg0 != v3):
                    v2 = v1
                    break
                v2 = (load32(9215896) + arg0)
                store32(9215888, (load32(9215896) + arg0))
                v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                if arg0:
                    # TODO: memory.copy []
                v3 = load32(9215892)
                break
            arg0 = load32(9215888)
            store32(9215884, v2)
            break
        v1 = (v3 + 1)
        store32(9215892, (v3 + 1))
        store32((v2 + (v3 << 2)), 0)
        while True:  # block $label5
            if (arg0 != v1):
                v3 = v2
                break
            v1 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v3 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(9215884, v3)
            v1 = load32(9215892)
            break
        store32(9215892, (v1 + 1))
        store32((v3 + (v1 << 2)), 0)
        while True:  # block $label6
            arg0 = load32(9215892)
            if (load32(9215892) != load32(9215888)):
                v1 = v3
                break
            v1 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(9215884, v1)
            arg0 = load32(9215892)
            break
        store32(9215892, (arg0 + 1))
        store32((v1 + (arg0 << 2)), 0)
        while True:  # block $label7
            arg0 = load32(9215892)
            if (load32(9215892) != load32(9215888)):
                v2 = v1
                break
            v2 = (load32(9215896) + arg0)
            store32(9215888, (load32(9215896) + arg0))
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(9215884, v2)
            arg0 = load32(9215892)
            break
        store32(9215892, (arg0 + 1))
        store32((v2 + (arg0 << 2)), 0)
    return af(v1)

# ------------------------------------------------------------
# $func115
# ------------------------------------------------------------
def func115(arg0, arg1, arg2, arg3, arg4):
    while True:  # block $label0
        if load8u(9142917):
            break
        if load8u(9142916):
            if load32(9142404):
                break
            v5 = load32(9142440)
            v5 = (load32(9142440) * v5)
            v6 = (-1 if (u((v5 * 3)) > u(1073741823)) else ((load32(9142440) * v5) * 12))
            v5 = func26((-1 if (u((v5 * 3)) > u(1073741823)) else ((load32(9142440) * v5) * 12)))
            # TODO: memory.fill []
            store32(9142404, v5)
            break
        if load32(9142400):
            break
        v5 = load32(9142440)
        v5 = (load32(9142440) * v5)
        v6 = (-1 if (v5 & 805306368) else ((load32(9142440) * v5) << 4))
        v5 = func26((-1 if (v5 & 805306368) else ((load32(9142440) * v5) << 4)))
        # TODO: memory.fill []
        store32(9142400, v5)
        break
    while True:  # block $label1
        if ((((load8u(9147212) == 0) & (arg3 ^ -1)) | arg4) == 0):
            break
        v9 = load32(9140324)
        if (load32(9140324) == 0):
            break
        v6 = (v9 - 1)
        if (arg2 > 0):
            v18 = (arg1 + arg2)
            v10 = (arg0 + arg2)
            while True:  # $label6
                v9 = v6
                v15 = load16u(40596)
                v5 = (load16u(40596) + 2)
                store16(40596, (load16u(40596) + 2))
                store32(9140296, 0)
                while True:  # block $label2
                    if (u((v5 & 65535)) <= u(65533)):
                        v7 = load32(9142440)
                        break
                    store16(40596, 1)
                    v7 = load32(9142440)
                    v5 = (load32(9142440) * v7)
                    if ((load32(9142440) * v7) == 0):
                        break
                    # TODO: memory.fill []
                    break
                v5 = arg0
                while True:  # $label5
                    v6 = arg1
                    while True:  # $label4
                        while True:  # block $label3
                            if (u(v6) >= u(v7)):
                                break
                            if ((v5 | v6) < 0):
                                break
                            if (u(v5) >= u(v7)):
                                break
                            if (v9 != load8s((load32(9147288) + ((v6 * v7) + v5)))):
                                break
                            func96(v5, v6, v9, v15)
                            v7 = load32(9142440)
                            break
                        v6 = (v6 + 1)
                        if ((v6 + 1) < v18):
                            continue
                        break
                    v5 = (v5 + 1)
                    if ((v5 + 1) < v10):
                        continue
                    break
                v6 = (v9 - 1)
                if v9:
                    continue
                break
            break
        v5 = load32(9142440)
        v18 = (load32(9142440) * v5)
        v10 = ((load32(9142440) * v5) << 1)
        v15 = load32(9142436)
        v7 = load16u(40596)
        if (v9 & 1):
            v7 = (v7 + 2)
            store16(40596, (v7 + 2))
            while True:  # block $label7
                if (u((v7 & 65535)) < u(65534)):
                    break
                v7 = 1
                store16(40596, 1)
                if (v18 == 0):
                    break
                # TODO: memory.fill []
                v7 = load16u(40596)
                break
        else:
        v5 = v6
        if v6:
            while True:  # $label10
                v9 = v5
                v6 = (v7 + 2)
                store16(40596, (v7 + 2))
                while True:  # block $label8
                    if (u((v6 & 65535)) < u(65534)):
                        break
                    v6 = 1
                    store16(40596, 1)
                    if (v18 == 0):
                        break
                    # TODO: memory.fill []
                    v6 = load16u(40596)
                    break
                v7 = (v6 + 2)
                store16(40596, (v6 + 2))
                while True:  # block $label9
                    if (u((v7 & 65535)) < u(65534)):
                        break
                    v7 = 1
                    store16(40596, 1)
                    if (v18 == 0):
                        break
                    # TODO: memory.fill []
                    v7 = load16u(40596)
                    break
                v5 = (v9 - 2)
                if (v9 != 1):
                    continue
                break
        store32(9140296, 0)
        break
    while True:  # block $label13
        while True:  # block $label12
            while True:  # block $label11
                if (load8u(9147212) == 0):
                    break
                if arg3:
                    break
                if (arg4 == 0):
                    break
                break
            arg3 = load32(9140324)
            if (load32(9140324) == 0):
                break
            if (arg2 <= 0):
                break
            v9 = (arg1 + arg2)
            arg4 = (arg0 + arg2)
            v7 = load32(9142440)
            while True:  # $label17
                arg3 = (arg3 - 1)
                v5 = arg0
                while True:  # $label16
                    v6 = arg1
                    while True:  # $label15
                        while True:  # block $label14
                            if (u(v6) >= u(v7)):
                                break
                            if ((v5 | v6) < 0):
                                break
                            if (u(v5) >= u(v7)):
                                break
                            func95(v5, v6, arg3)
                            v7 = load32(9142440)
                            break
                        v6 = (v6 + 1)
                        if ((v6 + 1) < v9):
                            continue
                        break
                    v5 = (v5 + 1)
                    if ((v5 + 1) < arg4):
                        continue
                    break
                if arg3:
                    continue
                break
            break
        arg3 = load32(9140324)
        if (load32(9140324) == 0):
            break
        v23 = (arg1 + arg2)
        v24 = (arg0 + arg2)
        v18 = (arg2 <= 0)
        while True:  # $label35
            store32(9140296, 0)
            arg3 = (arg3 - 1)
            while True:  # block $label18
                if v18:
                    break
                v7 = load32(9142440)
                v5 = arg0
                while True:  # $label33
                    v6 = arg1
                    while True:  # $label32
                        while True:  # block $label19
                            if (u(v6) >= u(v7)):
                                break
                            if ((v5 | v6) < 0):
                                break
                            if (u(v5) >= u(v7)):
                                break
                            if (arg3 != load8s((load32(9147288) + ((v6 * v7) + v5)))):
                                break
                            v17 = 0
                            v22 = 0
                            v7 = 0
                            v19 = 0
                            v9 = (load32(9142440) * v6)
                            v10 = load32(9140332)
                            v8 = load32((load32(9140332) + (arg3 << 2)))
                            v11 = load32(load32((load32(9140332) + (arg3 << 2))))
                            while True:  # block $label22
                                while True:  # block $label21
                                    if load32(v8 + 20):
                                        v14 = load8u(9142916)
                                        v19 = load32(v8 + 28)
                                        if (load32(v8 + 28) == 2147483647):
                                            while True:  # block $label20
                                                if v14:
                                                    v19 = load32(59152)
                                                    store32(59152, (load32(59152) + 1))
                                                    v13 = load32(9568052)
                                                    break
                                                v13 = load32(9568052)
                                                v19 = ((load32(9140308) + v11) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                                break
                                            arg4 = v11
                                            store32(v8 + 28, v19)
                                            v15 = load32(v8 + 4)
                                            arg2 = load32(9568048)
                                            store32(9568048, (load32(9568048) + 1))
                                            store32(((arg2 << 2) + 9563952), v8)
                                            store32(9568052, (((arg4 * (v15 + 2)) << 2) + v13))
                                            if (v14 == 0):
                                                break
                                            arg2 = load32(9568056)
                                            store32(v8 + 56, load32(9568056))
                                            store32(9568056, (arg2 + ((v15 * load32(v8)) << 2)))
                                            break
                                        if (v14 == 0):
                                            break
                                        break
                                    if load8u(9142916):
                                        break
                                    break
                                v22 = ((((v6 << 5) % v11) * v11) + ((v5 << 5) % v11))
                                v17 = 1
                                break
                            v20 = (v5 + v9)
                            v15 = load32(v8 + 32)
                            v9 = (v11 // 32)
                            v21 = 55
                            while True:  # block $label23
                                v11 = func373(v5, v6, arg3)
                                if (func373(v5, v6, arg3) < 0):
                                    v16 = 0
                                    v13 = 0
                                    break
                                v16 = 0
                                v13 = 0
                                if (arg3 <= v11):
                                    break
                                v12 = load32((v10 + (v11 << 2)))
                                v7 = load32(load32((v10 + (v11 << 2))))
                                while True:  # block $label26
                                    while True:  # block $label25
                                        if load32(v12 + 20):
                                            v13 = load32(v12 + 28)
                                            if (load32(v12 + 28) == 2147483647):
                                                while True:  # block $label24
                                                    if (v17 == 0):
                                                        v13 = load32(59152)
                                                        store32(59152, (load32(59152) + 1))
                                                        v16 = load32(9568052)
                                                        break
                                                    v16 = load32(9568052)
                                                    v13 = ((load32(9140308) + v7) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                                    break
                                                arg4 = v7
                                                store32(v12 + 28, v13)
                                                v14 = 0
                                                v10 = load32(v12 + 4)
                                                arg2 = load32(9568048)
                                                store32(9568048, (load32(9568048) + 1))
                                                store32(((arg2 << 2) + 9563952), v12)
                                                store32(9568052, (((arg4 * (v10 + 2)) << 2) + v16))
                                                if v17:
                                                    break
                                                arg2 = load32(9568056)
                                                store32(v12 + 56, load32(9568056))
                                                store32(9568056, (arg2 + ((v10 * load32(v12)) << 2)))
                                                break
                                        v14 = 0
                                        if (v17 == 0):
                                            break
                                        break
                                    v14 = ((((v6 << 5) % v7) * v7) + ((v5 << 5) % v7))
                                    break
                                v16 = 0
                                v7 = (v7 if (load32(v12 + 32) != 23) else 0)
                                v13 = (v13 + v14)
                                v21 = func410(v20, v11)
                                if (func410(v20, v11) == 55):
                                    v21 = 55
                                    break
                                v8 = (v8 + (load32(v8 + 44) << 2))
                                v11 = load32((v8 + (load32(v8 + 44) << 2)))
                                while True:  # block $label30
                                    while True:  # block $label29
                                        while True:  # block $label27
                                            if load32(v8 + 20):
                                                v12 = load32(v8 + 28)
                                                if (load32(v8 + 28) != 2147483647):
                                                    break
                                                while True:  # block $label28
                                                    if (v17 == 0):
                                                        v12 = load32(59152)
                                                        store32(59152, (load32(59152) + 1))
                                                        v16 = load32(9568052)
                                                        break
                                                    v16 = load32(9568052)
                                                    v12 = ((load32(9140308) + v11) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                                                    break
                                                arg4 = v11
                                                store32(v8 + 28, v12)
                                                v14 = 0
                                                v10 = load32(v8 + 4)
                                                arg2 = load32(9568048)
                                                store32(9568048, (load32(9568048) + 1))
                                                store32(((arg2 << 2) + 9563952), v8)
                                                store32(9568052, (((arg4 * (v10 + 2)) << 2) + v16))
                                                if v17:
                                                    break
                                                arg2 = load32(9568056)
                                                store32(v8 + 56, load32(9568056))
                                                store32(9568056, (arg2 + ((v10 * load32(v8)) << 2)))
                                                break
                                            v12 = 0
                                            break
                                        v14 = 0
                                        if (v17 == 0):
                                            break
                                        break
                                    v14 = (((load32((((v20 % 24) << 2) + 9824)) << 5) & 32) + ((v11 * v21) << 5))
                                    break
                                v16 = ((v11 // 32) << 16)
                                break
                            v10 = (v12 + v14)
                            while True:  # block $label31
                                if load8u(9142917):
                                    break
                                arg4 = (v19 + v22)
                                if (v17 == 0):
                                    arg2 = (load32(9142404) + (v20 * 12))
                                    store32((load32(9142404) + (v20 * 12)), arg4)
                                    store32(arg2 + 8, ((v10 << 16) + v21))
                                    store32(arg2 + 4, v13)
                                    break
                                arg2 = (load32(9142400) + (v20 << 4))
                                store32((load32(9142400) + (v20 << 4)), float(arg4))
                                store32(arg2 + 4, float(v13))
                                store32(arg2 + 8, float(v10))
                                store32(arg2 + 12, float(((v16 + (v9 if (v15 != 23) else 0)) + ((v7 // 32) << 8))))
                                break
                            if (v21 != 55):
                                arg2 = load32(9140296)
                                store32(9140296, (load32(9140296) + 1))
                                store32(((arg2 << 2) + 59200), v20)
                            v7 = load32(9142440)
                            break
                        v6 = (v6 + 1)
                        if ((v6 + 1) < v23):
                            continue
                        break
                    v5 = (v5 + 1)
                    if ((v5 + 1) < v24):
                        continue
                    break
                v6 = 0
                if (load32(9140296) == 0):
                    break
                while True:  # $label34
                    arg2 = (load32(9147288) + load32(((v6 << 2) + 59200)))
                    store8((load32(9147288) + load32(((v6 << 2) + 59200))), (load8u(arg2) ^ -1))
                    v6 = (v6 + 1)
                    if (u((v6 + 1)) < u(load32(9140296))):
                        continue
                    break
                break
            if arg3:
                continue
            break
        break
    return load32(v8)

# ------------------------------------------------------------
# $func116
# ------------------------------------------------------------
def func116(arg0):
    while True:  # block $label0
        if (arg0 == 0):
            break
        v1 = load32(arg0 + 8)
        store32(arg0, 0)
        store64(arg0 + 8, 0)
        if (v1 == 0):
            break
        while True:  # $label1
            arg0 = load32(v1 + 8)
            v1 = arg0
            if arg0:
                continue
            break
        break

# ------------------------------------------------------------
# $func118
# ------------------------------------------------------------
def func118(arg0):
    v3 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    while True:  # block $label0
        if (load32(load32(9142424) + 48) == 0):
            break
        if load8u(9147152):
            break
        while True:  # block $label1
            v1 = load32(9142872)
            if (load32(9142872) == 0):
                break
            if (load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(9142892) * v1)))) == 0):
                break
            if (load8u(arg0 + 125) != 3):
                break
            break
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 216) == 0):
            break
        while True:  # $label17
            v8 = 0
            while True:  # $label16
                v1 = load32(load32(9142424) + 48)
                v2 = ((load8u(9147152) == 0) & (load32(load32(9142424) + 48) != 0))
                while True:  # block $label3
                    if (load32(arg0 + 40) == 0):
                        while True:  # block $label2
                            if (v2 == 0):
                                break
                            v2 = load16u((load32(9147376) + (((v9 + load16u(arg0 + 112)) + (load32(9142440) * (v8 + load16u(arg0 + 114)))) << 1)))
                            if (v1 == 2):
                                if (u(v2) > u(1)):
                                    break
                                break
                            if (v2 == 0):
                                break
                            break
                        break
                    if (v2 == 0):
                        break
                    v2 = load16u((load32(9147376) + (((v9 + load16u(arg0 + 112)) + (load32(9142440) * (v8 + load16u(arg0 + 114)))) << 1)))
                    while True:  # block $label4
                        if (v1 == 2):
                            if (u(v2) <= u(1)):
                                break
                            break
                        if v2:
                            break
                        break
                    func77(arg0)
                    if (load32(arg0 + 40) == 0):
                        break
                    v1 = load32(arg0 + 12)
                    if load32(arg0 + 12):
                        v7 = 0
                        if load32(v1 + 8):
                            while True:  # $label9
                                while True:  # block $label6
                                    v5 = load32((load32(v1) + (v7 << 2)))
                                    if (u(load32((load32(v1) + (v7 << 2)))) >= u(1073741823)):
                                        v6 = (v5 - 1073741823)
                                        while True:  # block $label5
                                            v1 = load32(9299896)
                                            if (load32(9299896) != load32(9299892)):
                                                v2 = load32(9299888)
                                                break
                                            v2 = (load32(9299900) + v1)
                                            store32(9299892, (load32(9299900) + v1))
                                            v4 = load32(9299888)
                                            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                                            if v1:
                                                # TODO: memory.copy []
                                            if v4:
                                                v1 = load32(9299896)
                                            store32(9299888, v2)
                                            break
                                        store32(9299896, (v1 + 1))
                                        store32((v2 + (v1 << 2)), v6)
                                        break
                                    while True:  # block $label7
                                        v1 = load32(9299880)
                                        if (load32(9299880) != load32(9299876)):
                                            v2 = load32(9299872)
                                            break
                                        v2 = (load32(9299884) + v1)
                                        store32(9299876, (load32(9299884) + v1))
                                        v4 = load32(9299872)
                                        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                                        if v1:
                                            # TODO: memory.copy []
                                        if v4:
                                            v1 = load32(9299880)
                                        store32(9299872, v2)
                                        break
                                    store32(9299880, (v1 + 1))
                                    store32((v2 + (v1 << 2)), v5)
                                    break
                                while True:  # block $label8
                                    if load8u(9142916):
                                        store32(v3 + 80, v5)
                                        a_b()
                                        break
                                    store32(v3 + 72, v5)
                                    store64((v3 - -64), -4602115869219225600)
                                    store64(v3 + 56, 0)
                                    store64(v3 + 48, 0)
                                    a_b()
                                    break
                                v7 = (v7 + 2)
                                v1 = load32(arg0 + 12)
                                if (u((v7 + 2)) < u(load32(load32(arg0 + 12) + 8))):
                                    continue
                                break
                        store32(v1 + 8, 0)
                    while True:  # block $label10
                        v1 = load32(arg0 + 24)
                        if (load32(arg0 + 24) == 0):
                            break
                        v4 = load32(v1 + 4)
                        if (load32(v1 + 4) == 0):
                            break
                        v1 = load32(v4 + 8)
                        if (load32(v4 + 8) == 0):
                            break
                        v2 = load32(v4)
                        v7 = 0
                        while True:  # $label15
                            v10 = ((v7 | 1) << 2)
                            v5 = load32((v2 + ((v7 | 1) << 2)))
                            if load32((v2 + ((v7 | 1) << 2))):
                                while True:  # block $label12
                                    if (u(v5) >= u(1073741823)):
                                        v11 = (v5 - 1073741823)
                                        while True:  # block $label11
                                            v1 = load32(9299896)
                                            if (load32(9299896) != load32(9299892)):
                                                v2 = load32(9299888)
                                                break
                                            v2 = (load32(9299900) + v1)
                                            store32(9299892, (load32(9299900) + v1))
                                            v6 = load32(9299888)
                                            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                                            if v1:
                                                # TODO: memory.copy []
                                            if v6:
                                                v1 = load32(9299896)
                                            store32(9299888, v2)
                                            break
                                        store32(9299896, (v1 + 1))
                                        store32((v2 + (v1 << 2)), v11)
                                        break
                                    while True:  # block $label13
                                        v1 = load32(9299880)
                                        if (load32(9299880) != load32(9299876)):
                                            v2 = load32(9299872)
                                            break
                                        v2 = (load32(9299884) + v1)
                                        store32(9299876, (load32(9299884) + v1))
                                        v6 = load32(9299872)
                                        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                                        if v1:
                                            # TODO: memory.copy []
                                        if v6:
                                            v1 = load32(9299880)
                                        store32(9299872, v2)
                                        break
                                    store32(9299880, (v1 + 1))
                                    store32((v2 + (v1 << 2)), v5)
                                    break
                                while True:  # block $label14
                                    if load8u(9142916):
                                        store32(v3 + 32, v5)
                                        a_b()
                                        break
                                    store32(v3 + 24, v5)
                                    store64(v3 + 16, -4602115869219225600)
                                    store64(v3 + 8, 0)
                                    store64(v3, 0)
                                    a_b()
                                    break
                                v2 = load32(v4)
                                store32((load32(v4) + v10), 0)
                                v1 = load32(v4 + 8)
                            v7 = (v7 + 2)
                            if (u((v7 + 2)) < u(v1)):
                                continue
                            break
                        break
                    func38(load32(arg0 + 40))
                    store32(arg0 + 40, 0)
                    break
                v8 = (v8 + 1)
                v1 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 216)
                if (u((v8 + 1)) < u(load32(((load8u(arg0 + 122) * 404) + 9568096) + 216))):
                    continue
                break
            v9 = (v9 + 1)
            if (u((v9 + 1)) < u(v1)):
                continue
            break
        break
    G.global0 = (v3 + 96)

# ------------------------------------------------------------
# $func119
# ------------------------------------------------------------
def func119(arg0, arg1, arg2, param3):
    v3 = load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32)
    if load32(((load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) * 40) + 9671200) + 32):
        # call_indirect[v3]
    while True:  # block $label0
        v3 = load32(arg0 + 20)
        if (load32(arg0 + 20) == 0):
            break
        if (u(load32(v3 + 8)) < u(3)):
            break
        if (u((load32(load32(v3)) - 1)) > u(1)):
            break
        store32(v3 + 8, 0)
        break
    store8(arg0 + 129, 0)
    store32(arg0 + 32, 0)
    store8(arg0 + 123, 0)
    while True:  # block $label1
        if (load8u(59181) == 0):
            break
        v3 = load32(arg0 + 44)
        if (load32(arg0 + 44) == 0):
            break
        v4 = load32(9215884)
        if (load32((load32(9215884) + (v3 << 4)) + 12) == 1):
            break
        if (load8u(arg0 + 125) == 7):
            break
        if load32((v4 + ((v3 << 4) | 4))):
            break
        v3 = (load8u(arg0 + 124) << 3)
        break
    store8(arg0 + 125, arg1)
    if arg2:
        arg1 = load32(arg0 + 44)
        if load32(arg0 + 44):
            store32((load32(9215884) + (arg1 << 4)), 0)
        store32(arg0 + 44, 0)
    func92(arg0, 0.0, 0.0)

# ------------------------------------------------------------
# $func120
# ------------------------------------------------------------
def func120(arg0, arg1, arg2):
    while True:  # block $label0
        v4 = load32(arg0 + 12)
        if (load32(arg0 + 12) == 0):
            v3 = func26(16)
            store32(func26(16) + 4, 3)
            store32(v3, func26(12))
            store64(v3 + 8, 4294967296)
            store32(arg0 + 12, v3)
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
        v6 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
        if v5:
            # TODO: memory.copy []
        v3 = v4
        if v7:
            v5 = load32(v4 + 8)
            v3 = load32(arg0 + 12)
        store32(v4, v6)
        break
    store32(v8, (v5 + 1))
    store32((v6 + (v5 << 2)), arg1)
    while True:  # block $label1
        arg0 = load32(v3 + 8)
        if (load32(v3 + 8) != load32(v3 + 4)):
            v5 = load32(v3)
            break
        arg1 = (load32(v3 + 12) + arg0)
        store32(v3 + 4, (load32(v3 + 12) + arg0))
        v4 = load32(v3)
        v5 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
        if arg0:
            # TODO: memory.copy []
        if v4:
            arg0 = load32(v3 + 8)
        store32(v3, v5)
        break
    store32(v3 + 8, (arg0 + 1))
    store32((v5 + (arg0 << 2)), arg2)

# ------------------------------------------------------------
# $func123
# ------------------------------------------------------------
def func123(arg0, arg1):
    while True:  # block $label3
        while True:  # block $label2
            while True:  # block $label0
                while True:  # block $label1
                    # br_table[load32(arg0 + 4)]
                    break
                    break
                func299(arg0, arg1)
                return
                break
            v3 = load32(arg0 + 88)
            if (load32(arg0 + 88) == 0):
                break
            v4 = load32(9671128)
            while True:  # $label4
                v5 = (v4 + (load32((load32(arg0 + 80) + (v2 << 2))) * 132))
                if (load8u((v4 + (load32((load32(arg0 + 80) + (v2 << 2))) * 132)) + 125) != 3):
                    # call_indirect[arg1]
                    v4 = load32(9671128)
                    v3 = load32(arg0 + 88)
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(v3)):
                    continue
                break
            break
            break
        v3 = load32(9140300)
        if (load32(9140300) == 0):
            break
        v4 = load32(9142420)
        v5 = load32(9671128)
        while True:  # $label5
            v6 = (v5 + (load32(((v2 << 2) + 8451904)) * 132))
            if load32((v4 + (load16u((v5 + (load32(((v2 << 2) + 8451904)) * 132)) + 110) << 2))):
                # call_indirect[arg1]
                v4 = load32(9142420)
                v5 = load32(9671128)
                v3 = load32(9140300)
            v2 = (v2 + 1)
            if (u((v2 + 1)) < u(v3)):
                continue
            break
        break

# ------------------------------------------------------------
# $func124
# ------------------------------------------------------------
def func124(arg0):
    v1 = (G.global0 - 112)
    G.global0 = (G.global0 - 112)
    store32(9684420, arg0)
    v4 = load32(9671128)
    v3 = (load32(9671128) + (arg0 * 132))
    v7 = load16u((load32(9671128) + (arg0 * 132)) + 88)
    v6 = load16u(v3 + 108)
    v8 = load8u(v3 + 122)
    func52(load32(((load8u(v3 + 122) * 404) + 9568096) + 144), load16u(v3 + 110))
    while True:  # block $label1
        while True:  # block $label0
            v2 = load32(v3 + 24)
            if (load32(v3 + 24) == 0):
                break
            v2 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                break
            v5 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                break
            store32(v1 + 100, load32(v2))
            store32(v1 + 96, v5)
            a_b()
            break
            break
        a_b()
        break
    v2 = load32((v4 + (arg0 * 132)) + 16)
    if load32((v4 + (arg0 * 132)) + 16):
        v11 = load32(v2 + 8)
    while True:  # block $label2
        if load8u(9147152):
            break
        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v3 + 110))))) == 0):
            break
        v2 = (v4 + (arg0 * 132))
        if (load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) == 20):
            break
        break
    v12 = (load8u(v2 + 127) != 6)
    while True:  # block $label4
        while True:  # block $label3
            while True:  # block $label5
                v2 = load32(9215884)
                v5 = (v4 + (arg0 * 132))
                v9 = load32((v4 + (arg0 * 132)) + 44)
                v10 = load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4)
                # br_table[(load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) - 2)]
                break
                break
            if (v10 != 34):
                break
            break
        v13 = load32((v2 + (v9 << 4)))
        break
    v9 = (v7 if v6 else 0)
    v10 = load32(v5 + 52)
    v2 = ((v8 * 404) + 9568096)
    v8 = load32(((v8 * 404) + 9568096) + 264)
    v14 = load32(v2 + 84)
    v2 = load8u(v3 + 122)
    while True:  # block $label6
        if (load8u(v5 + 125) == 9):
            v5 = 0
            if (load32(38452) == v2):
                break
            if (load32(38496) == v2):
                break
            if (load32(38756) == v2):
                break
            if (load32(38692) == v2):
                break
            if (load32(38696) == v2):
                break
            if (load32(38776) == v2):
                break
            if (load32(38752) == v2):
                break
            if (load32(38704) == v2):
                break
        v5 = load32((v4 + (arg0 * 132)) + 60)
        break
    v7 = 0
    v15 = load16u(v3 + 110)
    v6 = (load32(9561692) + (load16u(v3 + 110) * 286704))
    v16 = load32((load32(9561692) + (load16u(v3 + 110) * 286704)) + 284628)
    v6 = load32(v6 + 284616)
    arg0 = (v4 + (arg0 * 132))
    v17 = load64((v4 + (arg0 * 132)) + 80)
    v18 = load64(arg0 + 72)
    v4 = load16u(v3 + 108)
    store32(v1 + 48, v8)
    store32(v1 + 52, v10)
    store32(v1 + 56, v5)
    store64(v1 + 60, v18)
    store32(v1 + 68, v2)
    store64(v1 + 72, v17)
    store32(v1 + 80, v15)
    store32(v1 + 84, v9)
    store32(v1 + 88, v4)
    store32(v1 + 92, (v6 if v6 else v16))
    store32(v1 + 32, v11)
    store32(v1 + 36, v12)
    store32(v1 + 40, v13)
    store32(v1 + 44, v14)
    a_b()
    store64(v1 + 16, load64(arg0 + 64))
    a_b()
    if load32(9147136):
        v2 = load32(9561692)
        arg0 = load16u(v3 + 110)
        if load16u(v3 + 110):
            v7 = load8u((load32(9143004) + ((load32(9142892) * load32(9142872)) + arg0)))
        arg0 = load32((v2 + (arg0 * 286704)) + 281800)
        if load32((v2 + (arg0 * 286704)) + 281800):
        else:
        store32((load32((arg0 + (load32(9142872) << 2))) != 0) + 4, 0)
        store32(v1, v7)
        a_b()
    G.global0 = (v1 + 112)
    return v1

# ------------------------------------------------------------
# $func125
# ------------------------------------------------------------
def func125(arg0):
    v2 = ((arg0 + 7) & -8)
    while True:  # block $label0
        while True:  # $label1
            arg0 = atomic_load(52740)
            v1 = (atomic_load(52740) + v2)
            if (v2 if (u((atomic_load(52740) + v2)) <= u(arg0)) else 0):
                break
            if (u(v1) > u((mem_size() << 16))):
                if (a_n(v1) == 0):
                    break
            # TODO: i32.atomic.rmw.cmpxchg [('offset', 52740)]
            if (v1 != arg0):
                continue
            break
        return arg0
        break
    store32((G.global3 + 28), 48)
    return -1

# ------------------------------------------------------------
# $func126
# ------------------------------------------------------------
def func126(arg0, arg1, arg2, arg3, arg4):
    v10 = ((arg1 - 4) + (arg3 // -2))
    v11 = (((arg2 // -2) + arg0) - 4)
    while True:  # $label5
        arg0 = load32(38448)
        v8 = load32(load32(((load32(38448) * 72) + 9263856)) + 20)
        arg1 = load32(9147320)
        v6 = ((load32(9147320) << 11) ^ arg1)
        arg1 = load32(9147312)
        v7 = load32(9147324)
        v7 = ((load32(9147324) << 11) ^ v7)
        v7 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v7) & 0xFFFFFFFF) >> 8)) ^ arg1) ^ v7)
        v6 = (((((((load32(9147320) << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ (((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v7) & 0xFFFFFFFF) >> 8)) ^ arg1) ^ v7) & 0xFFFFFFFF) >> 19)) ^ v6) ^ v7)
        store32(9147324, (((((((load32(9147320) << 11) ^ arg1) & 0xFFFFFFFF) >> 8) ^ (((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v7) & 0xFFFFFFFF) >> 8)) ^ arg1) ^ v7) & 0xFFFFFFFF) >> 19)) ^ v6) ^ v7))
        v5 = load32(9147316)
        v5 = ((load32(9147316) << 11) ^ v5)
        v5 = (((((((load32(9147316) << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v6 & 0xFFFFFFFF) >> 19)) ^ v5) ^ v6)
        store32(9147320, (((((((load32(9147316) << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v6 & 0xFFFFFFFF) >> 19)) ^ v5) ^ v6))
        arg1 = (arg1 ^ (arg1 << 11))
        arg1 = ((((((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v5 & 0xFFFFFFFF) >> 19)) ^ arg1) ^ v5)
        store32(9147316, ((((((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v5 & 0xFFFFFFFF) >> 19)) ^ arg1) ^ v5))
        v9 = ((v7 << 11) ^ v7)
        v9 = (((((((v7 << 11) ^ v7) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ v9) ^ arg1)
        store32(9147312, (((((((v7 << 11) ^ v7) & 0xFFFFFFFF) >> 8) ^ ((arg1 & 0xFFFFFFFF) >> 19)) ^ v9) ^ arg1))
        arg1 = ((v10 + (arg1 % arg3)) + (v9 & 7))
        v6 = ((v11 + (v6 % arg2)) + (v5 & 7))
        v7 = ((v7 % (v8 - 3)) + 3)
        while True:  # block $label0
            if (arg4 == 0):
                break
            v8 = load32(9142416)
            v5 = load32(9142416)
            if (v8 == 0):
                v5 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
            while True:  # block $label1
                # TODO: f32.convert_i32_u []
                v15 = (6.28318548 / (4 if (u(v5) < u(3)) else (v5 << (v5 & 1))))
                arg1 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                v5 = (arg1 - ((load32(9142440) & 0xFFFFFFFF) >> 1))
                v6 = (v6 - arg1)
                # TODO: f32.demote_f64 []
                v13 = func262(float((arg1 - ((load32(9142440) & 0xFFFFFFFF) >> 1))), float((v6 - arg1)))
                if ((6.28318548 / (4 if (u(v5) < u(3)) else (v5 << (v5 & 1)))) < func262(float((arg1 - ((load32(9142440) & 0xFFFFFFFF) >> 1))), float((v6 - arg1)))):
                    break
                if (v13 < 0.0):
                    break
                # TODO: f32.demote_f64 []
                v16 = sqrt(float(((v6 * v6) + (v5 * v5))))
                # TODO: f32.convert_i32_u []
                if (sqrt(float(((v6 * v6) + (v5 * v5)))) >= arg1):
                    break
                v17 = (v15 - v13)
                arg1 = ((arg0 * 404) + 9568096)
                v6 = (v7 & 255)
                v5 = 0
                while True:  # $label4
                    if (v8 == 0):
                        v8 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                    if (u(v5) >= u((4 if (u(v8) < u(3)) else (v8 << (v8 & 1))))):
                        break
                    # TODO: f32.convert_i32_u []
                    v14 = ((v15 * v5) + (v17 if (v5 & 1) else v13))
                    v18 = func48(((v15 * v5) + (v17 if (v5 & 1) else v13)))
                    while True:  # block $label2
                        # TODO: f64.convert_i32_u []
                        # TODO: f64.promote_f32 []
                        # TODO: f64.convert_i32_u []
                        v19 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                        v20 = (((0.5 - (load32(arg1 + 220) * 0.5)) + (v18 * v16)) + ((load32(9142440) & 0xFFFFFFFF) >> 1))
                        if (abs((((0.5 - (load32(arg1 + 220) * 0.5)) + (v18 * v16)) + ((load32(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0):
                            break
                        break
                    v7 = -2147483648
                    v14 = func49(v14)
                    while True:  # block $label3
                        # TODO: f64.convert_i32_u []
                        # TODO: f64.promote_f32 []
                        v19 = (((0.5 - (load32(arg1 + 216) * 0.5)) + (v14 * v16)) + v19)
                        if (abs((((0.5 - (load32(arg1 + 216) * 0.5)) + (v14 * v16)) + v19)) < 2147483648.0):
                            break
                        break
                    v5 = (v5 + 1)
                    v8 = load32(9142416)
                    continue
                    break
                raise RuntimeError('unreachable')
                break
            break
        v12 = (v12 + 1)
        if ((v12 + 1) != 55):
            continue
        break
    return arg0

# ------------------------------------------------------------
# $la
# Export: la
# ------------------------------------------------------------
def la():
    """Exported as la."""
    v0 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        if (load8u(9216060) | load8u(9142917)):
            break
        a_b()
        v2 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v3 = 1
        while True:  # $label1
            v1 = (load32(9561692) + (v3 * 286704))
            v5 = load8u(((load32(9561692) + (v3 * 286704)) + 283973))
            v6 = load8u(v1 + 283972)
            v7 = load32(v1 + 284608)
            v8 = load8u(v1 + 286699)
            v9 = load32(v1 + 284628)
            v4 = load32(v1 + 284616)
            v2 = load8u((load32(9143004) + (load32(9142872) + (load32(v1 + 283908) * v2))))
            v10 = load32(v1 + 284604)
            v11 = load8u(v1 + 286696)
            store32(v0 + 16, load8u((v1 + 283974)))
            store32(v0 + 20, v11)
            store32(v0 + 24, v10)
            store32(v0 + 28, v2)
            store32(v0 + 32, (v4 if v4 else v9))
            store32(v0 + 36, v8)
            store32(v0 + 40, v7)
            store32(v0, v3)
            store32(v0 + 4, v1)
            store32(v0 + 8, v6)
            store32(v0 + 12, v5)
            a_b()
            v3 = (v3 + 1)
            v2 = load32(9142892)
            if (u((v3 + 1)) < u(load32(9142892))):
                continue
            break
        break
    G.global0 = (v0 + 48)

# ------------------------------------------------------------
# $func128
# ------------------------------------------------------------
def func128(arg0, arg1, arg2):
    if ((load8u(arg0) & 32) == 0):
        while True:  # block $label1
            v3 = arg1
            while True:  # block $label0
                arg1 = arg0
                arg0 = load32(arg0 + 16)
                if load32(arg0 + 16):
                else:
                    if func433(arg1):
                        break
                v5 = load32(arg1 + 20)
                if (u(arg0) > u((load32(arg1 + 16) - load32(arg1 + 20)))):
                    # call_indirect[load32(arg1 + 36)]
                    break
                while True:  # block $label2
                    if (load32(arg1 + 80) < 0):
                        break
                    arg0 = arg2
                    while True:  # $label3
                        v4 = arg0
                        if (arg0 == 0):
                            break
                        arg0 = (v4 - 1)
                        if (load8u((v3 + (v4 - 1))) != 10):
                            continue
                        break
                    # call_indirect[load32(arg1 + 36)]
                    if (u(indirect_call(load32(arg1 + 36))) < u(v4)):
                        break
                    v3 = (v3 + v4)
                    arg2 = (arg2 - v4)
                    v5 = load32(arg1 + 20)
                    break
                store32(arg1 + 20, (load32(arg1 + 20) + arg2))
                break
            break
    return v4

# ------------------------------------------------------------
# $func129
# ------------------------------------------------------------
def func129(arg0, arg1, arg2):
    if (arg1 < load32(40608)):
        store32(40608, arg1)
    if (arg1 > load32(40612)):
        store32(40612, arg1)
    v5 = (1 if arg2 else -1)
    v3 = (load32(9147376) + (((load32(9142440) * arg1) + arg0) << 1))
    while True:  # block $label5
        while True:  # block $label1
            while True:  # block $label0
                while True:  # block $label2
                    # br_table[(load32(load32(9142424) + 48) - 1)]
                    break
                    break
                v4 = load16u(v3)
                while True:  # block $label3
                    while True:  # block $label4
                        if arg2:
                            if v4:
                                break
                            func257(arg0, arg1)
                            break
                        if (v4 != 1):
                            break
                        func411(arg0, arg1)
                        break
                    store8(9142904, 1)
                    break
                store16(v3, (load16u(v3) + v5))
                return
                break
            if (arg2 == 0):
                break
            if load16u(v3):
                break
            func257(arg0, arg1)
            store8(9142904, 1)
            store16(v3, 1)
            return
            break
        v4 = load16u(v3)
        while True:  # block $label6
            if arg2:
                if (u(v4) <= u(1)):
                    store16(v3, 1)
                    func257(arg0, arg1)
                else:
                store16(load16u(v3), (v4 + v5))
                break
            arg2 = (v4 + v5)
            store16(v3, (v4 + v5))
            if ((arg2 & 65535) != 1):
                break
            func411(arg0, arg1)
            break
        if load8u(9142904):
            break
        if (u(((load16u(v3) - 1) & 65535)) > u(1)):
            break
        store8(9142904, 1)
        break
    return v3

# ------------------------------------------------------------
# $func130
# ------------------------------------------------------------
def func130(arg0):
    v2 = load32(arg0 + 28)
    while True:  # block $label0
        v1 = load32(v2 + 20)
        v3 = load32(arg0 + 16)
        v1 = (load32(v2 + 20) if (u(v1) < u(v3)) else load32(arg0 + 16))
        if ((load32(v2 + 20) if (u(v1) < u(v3)) else load32(arg0 + 16)) == 0):
            break
        store32(arg0 + 12, (load32(arg0 + 12) + v1))
        store32(v2 + 16, (load32(v2 + 16) + v1))
        store32(arg0 + 20, (load32(arg0 + 20) + v1))
        store32(arg0 + 16, (load32(arg0 + 16) - v1))
        arg0 = load32(v2 + 20)
        store32(v2 + 20, (load32(v2 + 20) - v1))
        if (arg0 != v1):
            break
        store32(v2 + 16, load32(v2 + 8))
        break

# ------------------------------------------------------------
# $func131
# ------------------------------------------------------------
def func131(arg0, arg1, arg2):
    if (arg0 & 3):
    else:
        func429()
        if (G.global6 == 0):
            while True:  # block $label3
                v4 = a_f()
                # TODO: i32.atomic.rmw.cmpxchg [('offset', 9688024)]
                while True:  # block $label0
                    arg2 = (v4 + arg2)
                    if (a_f() > (v4 + arg2)):
                        break
                    while True:  # block $label1
                        while True:  # $label2
                            # TODO: i32.atomic.rmw.cmpxchg [('offset', 9688024)]
                            v3 = 0
                            if ((arg0 if (arg0 == v3) else 0) == 0):
                                break
                            func429()
                            if (arg1 == atomic_load(arg0)):
                                # TODO: i32.atomic.rmw.cmpxchg [('offset', 9688024)]
                                if (a_f() > arg2):
                                    break
                                continue
                            break
                        break
                    break
                    break
                # TODO: i32.atomic.rmw.cmpxchg [('offset', 9688024)]
                break
            return -73
        v3 = (arg2 != inf)
        while True:  # block $label4
            arg2 = ((arg2 * 1000.0) * 1000.0)
            if (abs(((arg2 * 1000.0) * 1000.0)) < 9.223372036854776e+18):
                # TODO: i64.trunc_f64_s []
                break
            break
        # TODO: memory.atomic.wait32 []
        arg0 = (-9223372036854775808 if v3 else -1)
    return (arg0 if (arg0 == 1) else (arg1 if ((-9223372036854775808 if v3 else -1) == 2) else arg2))

# ------------------------------------------------------------
# $func132
# ------------------------------------------------------------
def func132(arg0, arg1):
    v10 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    v15 = load32(9671176)
    if (u(load32(9671176)) >= u(4)):
        # TODO: i32.div_u []
        v14 = 3
        v9 = load32(9671168)
        while True:  # $label0
            v8 = (v9 + (v2 * 12))
            v6 = ((load32((v9 + (v2 * 12))) * 404) + 9568096)
            v19 = (load32(((load32((v9 + (v2 * 12))) * 404) + 9568096) + 220) + load32(v8 + 8))
            v3 = ((load32(((load32((v9 + (v2 * 12))) * 404) + 9568096) + 220) + load32(v8 + 8)) if (v3 < v19) else v3)
            v19 = (load32(v6 + 216) + load32(v8 + 4))
            v5 = ((load32(v6 + 216) + load32(v8 + 4)) if (v5 < v19) else v5)
            v2 = (v2 + 1)
            if ((v2 + 1) != v14):
                continue
            break
        v5 = (v5 << 4)
        v3 = (v3 << 4)
    if (u(v15) >= u(3)):
        v26 = load32(9671192)
        v19 = ((arg1 - v3) // 32)
        v31 = ((arg0 - v5) // 32)
        v27 = (arg0 == 2147483647)
        while True:  # $label32
            v6 = (load32(9671168) + (v21 * 12))
            v3 = load32((load32(9671168) + (v21 * 12)))
            v7 = ((load32((load32(9671168) + (v21 * 12))) * 404) + 9568096)
            while True:  # block $label3
                while True:  # block $label2
                    while True:  # block $label1
                        if load8u(9142409):
                            break
                        v11 = ((v3 * 72) + 9263856)
                        if load32(((v3 * 72) + 9263856)):
                            break
                        v2 = ((v3 << 2) + 9560016)
                        if load32(((v3 << 2) + 9560016)):
                            break
                        store32(v2, load32(9671136))
                        break
                    v23 = (v3 == load32(38472))
                    if ((v3 == load32(38472)) == 0):
                        if (v3 != load32(38600)):
                            break
                    store8(9142410, 1)
                    v6 = (load32(v7 + 216) << 4)
                    v13 = ((load32(59140) - (load32(v7 + 216) << 4)) // 32)
                    v11 = ((load32(59132) - v6) // 32)
                    v2 = load32(9142440)
                    v4 = ((arg1 - (load32(v7 + 220) << 4)) // 32)
                    if (u(load32(9142440)) <= u(((arg1 - (load32(v7 + 220) << 4)) // 32))):
                        break
                    v7 = ((arg0 - v6) // 32)
                    if (u(v2) <= u(((arg0 - v6) // 32))):
                        break
                    if ((v4 | v7) < 0):
                        break
                    v2 = (v13 - v4)
                    v2 = (v2 >> 31)
                    v17 = (((v13 - v4) ^ (v2 >> 31)) - v2)
                    v14 = ((((v13 - v4) ^ (v2 >> 31)) - v2) + 1)
                    v2 = (v11 - v7)
                    v2 = (v2 >> 31)
                    v18 = (((v11 - v7) ^ (v2 >> 31)) - v2)
                    v9 = ((((v11 - v7) ^ (v2 >> 31)) - v2) + 1)
                    v22 = 1
                    v15 = 1
                    v24 = 1
                    v16 = 1
                    if (load8u(9163792) == 0):
                        v5 = (v7 >= v11)
                        v3 = (v7 < v11)
                        v8 = (u(v17) < u(v18))
                        v16 = ((v7 >= v11) if (u(v17) < u(v18)) else (v7 < v11))
                        v6 = (v4 < v13)
                        v2 = (v4 >= v13)
                        v24 = ((v4 < v13) if v8 else (v4 >= v13))
                        v15 = (v3 if v8 else v5)
                        v22 = (v2 if v8 else v6)
                    store8(9684791, v15)
                    store8(9684790, v22)
                    store8(9684789, v16)
                    v5 = 0
                    store8(9684788, v24)
                    v7 = (v11 if (v7 > v11) else v7)
                    store32(9684772, (v11 if (v7 > v11) else v7))
                    v13 = (v13 if (v4 > v13) else v4)
                    store32(9684776, (v13 if (v4 > v13) else v4))
                    store32(9684780, v9)
                    store32(9684784, v14)
                    v2 = (v18 - 1)
                    v3 = (((1 - v17) * ((v18 - 1) if (u(v2) <= u(v18)) else 0)) if (u(v17) > u(1)) else 0)
                    while True:  # block $label4
                        if (load32(9142396) == 0):
                            break
                        while True:  # $label9
                            while True:  # block $label6
                                v11 = load32((load32(9142392) + (v5 << 2)))
                                if (u(load32((load32(9142392) + (v5 << 2)))) >= u(1073741823)):
                                    v6 = (v11 - 1073741823)
                                    while True:  # block $label5
                                        v4 = load32(9299896)
                                        if (load32(9299896) != load32(9299892)):
                                            v2 = load32(9299888)
                                            break
                                        v2 = (load32(9299900) + v4)
                                        store32(9299892, (load32(9299900) + v4))
                                        v8 = load32(9299888)
                                        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                                        if v4:
                                            # TODO: memory.copy []
                                        if v8:
                                            v4 = load32(9299896)
                                        store32(9299888, v2)
                                        break
                                    store32(9299896, (v4 + 1))
                                    store32((v2 + (v4 << 2)), v6)
                                    break
                                while True:  # block $label7
                                    v4 = load32(9299880)
                                    if (load32(9299880) != load32(9299876)):
                                        v2 = load32(9299872)
                                        break
                                    v2 = (load32(9299884) + v4)
                                    store32(9299876, (load32(9299884) + v4))
                                    v6 = load32(9299872)
                                    v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                                    if v4:
                                        # TODO: memory.copy []
                                    if v6:
                                        v4 = load32(9299880)
                                    store32(9299872, v2)
                                    break
                                store32(9299880, (v4 + 1))
                                store32((v2 + (v4 << 2)), v11)
                                break
                            while True:  # block $label8
                                if load8u(9142916):
                                    store32(v10 + 48, v11)
                                    a_b()
                                    break
                                store32(v10 + 40, v11)
                                store64(v10 + 32, -4602115869219225600)
                                store64(v10 + 24, 0)
                                store64(v10 + 16, 0)
                                a_b()
                                break
                            v5 = (v5 + 1)
                            if (u((v5 + 1)) < u(load32(9142396))):
                                continue
                            break
                        store32(9142396, 0)
                        v2 = load32(9142392)
                        if (load32(9142392) == 0):
                            break
                        break
                    v12 = 0
                    v2 = (v3 + (v9 * v14))
                    store32(9142392, func26((-1 if (u(v2) > u(1073741823)) else ((v3 + (v9 * v14)) << 2))))
                    while True:  # $label17
                        v32 = (float(v12) / 100.0)
                        v28 = (v7 + v12)
                        v29 = ((v7 + v12) + 1)
                        v2 = (v12 == 0)
                        v11 = ((v12 == 0) | (u(v12) >= u(v18)))
                        v8 = (v22 & (v12 == v18))
                        v14 = (v2 & v24)
                        v33 = float((v28 << 5))
                        v3 = 0
                        while True:  # $label16
                            while True:  # block $label10
                                v6 = v3
                                if (((v15 & (v3 == v17)) | ((v14 | (v16 & (v3 == 0))) | v8)) == 0):
                                    break
                                v2 = load32(9142440)
                                if (u(load32(9142440)) <= u(v6)):
                                    break
                                if (u(v2) <= u(v12)):
                                    break
                                while True:  # block $label11
                                    if (v11 == 0):
                                        break
                                    while True:  # block $label12
                                        if (v6 == 0):
                                            break
                                        if (u(v6) >= u(v17)):
                                            break
                                        break
                                        break
                                    break
                                v9 = load32(((load32((38472 if v23 else 38600)) * 72) + 9263856))
                                if (load32(((load32((38472 if v23 else 38600)) * 72) + 9263856)) == 0):
                                    break
                                v2 = 0
                                while True:  # block $label13
                                    if load8u(9142917):
                                        break
                                    v2 = load32(9299880)
                                    if load32(9299880):
                                        v2 = (v2 - 1)
                                        store32(9299880, (v2 - 1))
                                        v2 = load32((load32(9299872) + (v2 << 2)))
                                        break
                                    v2 = load32(9163776)
                                    v5 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v3 = load32(9163784)
                                    if (u(v5) < u(load32(9163784))):
                                        break
                                    store32(v10, v3)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    break
                                v3 = load32(9142396)
                                store32(9142396, (load32(9142396) + 1))
                                store32((load32(9142392) + (v3 << 2)), v2)
                                while True:  # block $label15
                                    while True:  # block $label14
                                        v5 = load32(9142840)
                                        v30 = load32(9142440)
                                        v4 = (load32(9142440) + 2)
                                        v25 = (v6 + v13)
                                        v3 = ((v6 + v13) + 1)
                                        if load32((load32(9142840) + (((((load32(9142440) + 2) + ((v6 + v13) + 1)) * v4) + v29) << 2))):
                                            break
                                        if load32((v5 + (((v3 * v4) + v29) << 2))):
                                            break
                                        v3 = 0
                                        if (load32(load32(9142424) + 48) == 0):
                                            break
                                        if load8u(9147152):
                                            break
                                        if load16u((load32(9147376) + (((v25 * v30) + v28) << 1))):
                                            break
                                        break
                                    v3 = 1
                                    break
                                # TODO: f32.convert_i32_u []
                                break
                            v3 = (v6 + 1)
                            if (v6 != v17):
                                continue
                            break
                        v2 = (v12 != v18)
                        v12 = (v12 + 1)
                        if v2:
                            continue
                        break
                    break
                    break
                while True:  # block $label18
                    if (v27 == 0):
                        v2 = v19
                        if (u(v15) > u(3)):
                            break
                        v2 = (((arg1 - (load32(v7 + 220) << 4)) & 0xFFFFFFFF) >> 5)
                        break
                    v2 = load32(9684776)
                    break
                v3 = load32(9684772)
                while True:  # block $label19
                    if v27:
                        break
                    if v21:
                        break
                    if (load32(9684772) != v3):
                        break
                    if (load32(9684776) == v2):
                        break
                    break
                if (v21 == 0):
                    store32(9684776, v2)
                    store32(9684772, v3)
                v3 = (load32(v6 + 4) + v3)
                v16 = 0
                while True:  # block $label20
                    v13 = load32(9142440)
                    v6 = (load32(v6 + 8) + v2)
                    if (u(load32(9142440)) <= u((load32(v6 + 8) + v2))):
                        break
                    if (u(v3) >= u(v13)):
                        break
                    if ((v3 | v6) < 0):
                        break
                    while True:  # block $label21
                        if (load32(load32(9142424) + 48) == 0):
                            break
                        if load8u(9147152):
                            break
                        v5 = load32(v7 + 216)
                        if (load32(v7 + 216) <= 0):
                            break
                        v2 = load32(v7 + 220)
                        if (load32(v7 + 220) <= 0):
                            break
                        v8 = (v2 + v6)
                        v14 = (v3 + v5)
                        v9 = load32(9147376)
                        v2 = v3
                        while True:  # $label24
                            v5 = v6
                            if (u(v2) < u(v13)):
                                while True:  # $label23
                                    while True:  # block $label22
                                        if (u(v5) >= u(v13)):
                                            break
                                        if ((v2 | v5) < 0):
                                            break
                                        if load16u((v9 + (((v5 * v13) + v2) << 1))):
                                            break
                                        break
                                    v5 = (v5 + 1)
                                    if ((v5 + 1) < v8):
                                        continue
                                    break
                            v2 = (v2 + 1)
                            if ((v2 + 1) < v14):
                                continue
                            break
                        break
                        break
                    v16 = func56(v3, v6, v7, load32(9142872), 0, 0, 1, 1, 0)
                    break
                store32(9684800, v16)
                v14 = (v16 ^ 1)
                while True:  # block $label27
                    if (v26 == 0):
                        v2 = 0
                        while True:  # block $label25
                            if load8u(9142917):
                                break
                            v2 = load32(9299880)
                            if load32(9299880):
                                v2 = (v2 - 1)
                                store32(9299880, (v2 - 1))
                                v2 = load32((load32(9299872) + (v2 << 2)))
                                break
                            v2 = load32(9163776)
                            v9 = (load32(9163776) + 1)
                            store32(9163776, (load32(9163776) + 1))
                            v5 = load32(9163784)
                            if (u(v9) < u(load32(9163784))):
                                break
                            store32(v10 + 80, v5)
                            a_b()
                            store32(9163784, (load32(9163784) + 40000))
                            break
                        while True:  # block $label26
                            v5 = load32(9671192)
                            if (load32(9671192) != load32(9671188)):
                                v4 = load32(9671184)
                                break
                            v9 = (load32(9671196) + v5)
                            store32(9671188, (load32(9671196) + v5))
                            v8 = load32(9671184)
                            v4 = func26((-1 if (u(v9) > u(1073741823)) else (v9 << 2)))
                            if v5:
                                # TODO: memory.copy []
                            if v8:
                                v5 = load32(9671192)
                            store32(9671184, v4)
                            break
                        store32(9671192, (v5 + 1))
                        store32((v4 + (v5 << 2)), v2)
                        break
                    v2 = load32((load32(9671184) + (v20 << 2)))
                    v20 = (v20 + 1)
                    break
                v5 = 0
                v32 = float((v3 << 5))
                v33 = float((v6 << 5))
                # TODO: f32.convert_i32_u []
                v4 = load32(v7 + 20)
                if (load32(v7 + 20) == 0):
                    break
                while True:  # $label31
                    v3 = (v7 + (v5 << 2))
                    v2 = load32((v7 + (v5 << 2)))
                    if (load32(load32((v7 + (v5 << 2))) + 32) != 6):
                        while True:  # block $label30
                            if (v26 == 0):
                                v4 = 0
                                while True:  # block $label28
                                    if load8u(9142917):
                                        break
                                    v2 = load32(9299880)
                                    if load32(9299880):
                                        v2 = (v2 - 1)
                                        store32(9299880, (v2 - 1))
                                        v4 = load32((load32(9299872) + (v2 << 2)))
                                        break
                                    v4 = load32(9163776)
                                    v6 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v2 = load32(9163784)
                                    if (u(v6) < u(load32(9163784))):
                                        break
                                    store32(v10 + 64, v2)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    break
                                while True:  # block $label29
                                    v2 = load32(9671192)
                                    if (load32(9671192) != load32(9671188)):
                                        v12 = load32(9671184)
                                        break
                                    v6 = (load32(9671196) + v2)
                                    store32(9671188, (load32(9671196) + v2))
                                    v9 = load32(9671184)
                                    v12 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
                                    if v2:
                                        # TODO: memory.copy []
                                    if v9:
                                        v2 = load32(9671192)
                                    store32(9671184, v12)
                                    break
                                store32(9671192, (v2 + 1))
                                store32((v12 + (v2 << 2)), v4)
                                v2 = load32(v3)
                                break
                            v4 = load32((load32(9671184) + (v20 << 2)))
                            v20 = (v20 + 1)
                            break
                        # TODO: f32.convert_i32_u []
                        v4 = load32(v7 + 20)
                    v5 = (v5 + 1)
                    if (u((v5 + 1)) < u(v4)):
                        continue
                    break
                break
            v21 = (v21 + 1)
            v15 = load32(9671176)
            # TODO: i32.div_u []
            if (u(load32(9671176)) < u(3)):
                continue
            break
    G.global0 = (v10 + 96)
    return (v21 + 1)

# ------------------------------------------------------------
# $func133
# ------------------------------------------------------------
def func133(arg0, arg1, arg2):
    v11 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v16 = load8u(9216060)
    v17 = load32(arg0 + 40)
    v22 = load32(arg0 + 36)
    v25 = load32(arg0 + 32)
    v12 = load32(arg0 + 28)
    v13 = load32(arg0 + 24)
    v20 = load32(arg0 + 20)
    v21 = load32(arg0 + 16)
    v9 = load32(arg0 + 12)
    v23 = load32(arg0 + 8)
    v24 = load32(arg0 + 4)
    v5 = load32(arg0)
    while True:  # block $label2
        if (load8u(9142412) == 0):
            v8 = load32(9561692)
            while True:  # block $label0
                v7 = load32(((v5 * 404) + 9568096) + 180)
                if (load32(((v5 * 404) + 9568096) + 180) == 0):
                    break
                while True:  # block $label1
                    if (load8u(v7 + 23) == 0):
                        break
                    arg0 = load32(v7 + 4)
                    if (load32(((load32(v7 + 4) * 404) + 9568096) + 264) != 3):
                        break
                    if load32((((v8 + (v9 * 286704)) + (arg0 << 2)) + 281808)):
                        break
                    break
                v19 = load32(v7 + 68)
                if (load32(v7 + 68) == 0):
                    break
                arg0 = 0
                v4 = 1
                v14 = (v8 + (v9 * 286704))
                while True:  # $label5
                    v18 = load32((v7 + (arg0 << 2)) + 28)
                    v10 = load32(((load32((v7 + (arg0 << 2)) + 28) * 404) + 9568096) + 264)
                    v15 = (load32(((load32((v7 + (arg0 << 2)) + 28) * 404) + 9568096) + 264) == 1)
                    while True:  # block $label4
                        while True:  # block $label3
                            v18 = load32(((v14 + (v18 << 2)) + 281808))
                            if (load32(((v14 + (v18 << 2)) + 281808)) == 1):
                                break
                            v4 = ((v10 != 3) & v4)
                            if v18:
                                break
                            v4 = ((v10 != 0) & v4)
                            break
                            break
                        v3 = (v3 | v15)
                        break
                    v6 = (v6 | v15)
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v19):
                        continue
                    break
                if ((((v3 & v4) if (v6 & 1) else v4) & 1) == 0):
                    break
                break
            if load8u((v8 + (v9 * 286704)) + 286696):
                break
        if (v21 == 0):
            break
        if (v20 == 0):
            break
        v18 = (v23 + 1)
        v26 = (v24 + 1)
        v27 = (v20 - 1)
        v28 = (v21 - 1)
        v19 = ((v5 << 2) + 9560016)
        v29 = ((v5 * 72) + 9263856)
        v7 = ((v5 * 404) + 9568096)
        v16 = (((((((((((((((0 if v16 else v17) if (v5 != load32(38500)) else 0) if (v5 != load32(38636)) else 0) if (v5 != load32(39056)) else 0) if (v5 != load32(38632)) else 0) if (v5 != load32(38628)) else 0) if (v5 != load32(38624)) else 0) if (v5 != load32(38616)) else 0) if (v5 != load32(38612)) else 0) if (v5 != load32(38608)) else 0) if (v5 != load32(38604)) else 0) if (v5 != load32(38472)) else 0) if (v5 != load32(38600)) else 0) if (v5 != load32(38620)) else 0) if (v5 != load32(38560)) else 0)
        v30 = (v13 == 0)
        v31 = (v12 == 0)
        v32 = (u(v5) > u(254))
        v33 = (v5 * 36)
        v15 = 0
        while True:  # $label33
            v34 = ((v15 == v28) & (v25 != 0))
            v17 = (v15 + v24)
            v35 = (v30 | (v15 != 0))
            arg0 = 0
            while True:  # $label32
                while True:  # block $label6
                    if ((((arg0 == v27) & (v22 != 0)) | (((v35 & (v31 | (arg0 != 0))) == 0) | v34)) == 0):
                        break
                    v3 = load32(9142440)
                    v4 = (arg0 + v23)
                    if (u(load32(9142440)) <= u((arg0 + v23))):
                        break
                    if ((v4 | v17) < 0):
                        break
                    if (u(v3) <= u(v17)):
                        break
                    v10 = load8u(9142412)
                    if (load8u(9142412) == 0):
                        if v32:
                            break
                        if (load32(v7 + 264) != 1):
                            break
                    v12 = load32(38500)
                    v13 = (v5 == load32(38500))
                    v6 = (v5 == load32(38500))
                    while True:  # block $label22
                        while True:  # block $label15
                            while True:  # block $label24
                                while True:  # block $label8
                                    while True:  # block $label7
                                        if (load32(38636) == v5):
                                            v8 = load32(9561692)
                                            v3 = (load32(9561692) + (v9 * 286704))
                                            v14 = (load32((load32(9561692) + (v9 * 286704)) + 283976) + 1)
                                            if (u((load32((load32(9561692) + (v9 * 286704)) + 283976) + 1)) > u((load32((v3 + 284136)) + load32(v3 + 283980)))):
                                                break
                                            v6 = 1
                                            if (u(v14) > u(load32((v3 + 284000)))):
                                                break
                                        v16 = (0 if load32(load32(9142424) + 156) else v16)
                                        while True:  # block $label10
                                            while True:  # block $label9
                                                if arg2:
                                                    break
                                                if load8u(9147210):
                                                    break
                                                if (v10 == 0):
                                                    break
                                                v9 = load32(9142872)
                                                v6 = 1
                                                break
                                                break
                                            v8 = (load32(9561692) + (v9 * 286704))
                                            v3 = load32((((load32(9561692) + (v9 * 286704)) + v33) + 269376))
                                            v3 = (load32((((load32(9561692) + (v9 * 286704)) + v33) + 269376)) if v3 else 100)
                                            store32(v11 + 32, (((load32((((load32(9561692) + (v9 * 286704)) + v33) + 269376)) if v3 else 100) * load32(v7 + 68)) // 100))
                                            store32(v11 + 36, ((load32(v7 + 72) * v3) // 100))
                                            store32(v11 + 40, ((load32(v7 + 76) * v3) // 100))
                                            store32(v11 + 44, ((load32(v7 + 80) * v3) // 100))
                                            v10 = (v16 == 0)
                                            v3 = func66(v8, (v11 + 32), (v16 == 0), 1)
                                            if (v10 if v3 else 0):
                                                break
                                            if (u(func180(v8, v5)) >= u(load32(v7 + 204))):
                                                break
                                            break
                                        v3 = (v3 ^ 1)
                                        v9 = (v9 if (v5 != load32(38620)) else 0)
                                        v8 = (v5 == load32(38560))
                                        while True:  # block $label11
                                            if load32(v29):
                                                break
                                            if load32(v19):
                                                break
                                            store32(v19, load32(9671136))
                                            break
                                        v9 = (0 if v8 else v9)
                                        if v6:
                                        else:
                                        v8 = func34((0 if v8 else v9), v17, v4, 0, 1, (load32(load32(9142424) + 156) != 0))
                                        while True:  # block $label12
                                            if arg2:
                                                break
                                            if (load8u(9142412) == 0):
                                                break
                                            while True:  # block $label13
                                                v3 = (load32(9671128) + (v8 * 132))
                                                v4 = load8u((load32(9671128) + (v8 * 132)) + 122)
                                                v6 = ((load8u((load32(9671128) + (v8 * 132)) + 122) * 404) + 9568096)
                                                if (load32(((load8u((load32(9671128) + (v8 * 132)) + 122) * 404) + 9568096) + 264) == 2):
                                                    if (load32(v6 + 268) == 1):
                                                        break
                                                if (load32(38964) != v4):
                                                    break
                                                store32(v3 + 80, 100)
                                                break
                                                break
                                            store32(v3 + 52, 1)
                                            break
                                            break
                                        if v8:
                                            while True:  # block $label14
                                                if (v3 | (v16 == 0)):
                                                    break
                                                v3 = (v8 * 132)
                                                if (load8u(((v8 * 132) + load32(9671128)) + 125) != 4):
                                                    break
                                                func181((load32(9561692) + (v9 * 286704)), v8, -1)
                                                v3 = (load32(9671128) + v3)
                                                store8((load32(9671128) + v3) + 127, 14)
                                                store8(v3 + 125, 14)
                                                v3 = load32(v3 + 40)
                                                if (load32(v3 + 40) == 0):
                                                    break
                                                if load8u(9142916):
                                                    store32(v11 + 20, v3)
                                                    store32(v11 + 16, -65536)
                                                    a_b()
                                                    break
                                                store32(v11 + 4, v3)
                                                store32(v11, 14)
                                                a_b()
                                                break
                                            if (v5 == load32(38636)):
                                                break
                                            if (v22 == 2):
                                                break
                                            v13 = (1 if v13 else 4)
                                            while True:  # block $label16
                                                v36 = (v5 == v12)
                                                if (v5 == v12):
                                                    break
                                                v3 = load32(9142424)
                                                if (load32(load32(9142424) + 124) == 0):
                                                    break
                                                if load32(v3 + 156):
                                                    break
                                                if (arg2 == 0):
                                                    break
                                                v4 = 0
                                                v3 = load32(9671128)
                                                while True:  # $label18
                                                    while True:  # block $label17
                                                        v6 = (v3 + (load32((arg1 + (v4 << 2))) * 132))
                                                        if (load8u((v3 + (load32((arg1 + (v4 << 2))) * 132)) + 125) == 3):
                                                            break
                                                        if (load32((load32(9215884) + (load32(v6 + 44) << 4)) + 4) == 4):
                                                            break
                                                        if (load8u(v6 + 123) == 4):
                                                            break
                                                        v3 = load32(9671128)
                                                        break
                                                    v4 = (v4 + 1)
                                                    if ((v4 + 1) != arg2):
                                                        continue
                                                    break
                                                break
                                                break
                                            if (arg2 == 0):
                                                break
                                            v6 = 0
                                            v37 = load32(9215884)
                                            v14 = load32(9671128)
                                            v3 = -1
                                            v12 = 0
                                            while True:  # $label21
                                                while True:  # block $label19
                                                    v10 = (v14 + (load32((arg1 + (v6 << 2))) * 132))
                                                    v4 = (v18 - load16u((v14 + (load32((arg1 + (v6 << 2))) * 132)) + 114))
                                                    v4 = (v26 - load16u(v10 + 112))
                                                    v4 = (((v18 - load16u((v14 + (load32((arg1 + (v6 << 2))) * 132)) + 114)) * v4) + ((v26 - load16u(v10 + 112)) * v4))
                                                    if (u((((v18 - load16u((v14 + (load32((arg1 + (v6 << 2))) * 132)) + 114)) * v4) + ((v26 - load16u(v10 + 112)) * v4))) >= u(v3)):
                                                        break
                                                    while True:  # block $label20
                                                        if (v36 == 0):
                                                            if (load32((v37 + (load32(v10 + 44) << 4)) + 4) == 4):
                                                                break
                                                            if (load8u(v10 + 123) != 4):
                                                                break
                                                            break
                                                        if (load8u(v10 + 123) != 1):
                                                            break
                                                        v38 = (v14 + (load32(v10 + 32) * 132))
                                                        if (load8u((v14 + (load32(v10 + 32) * 132)) + 125) == 10):
                                                            break
                                                        if (load32(((load8u(v38 + 122) * 404) + 9568096) + 188) == 2):
                                                            break
                                                        break
                                                    v12 = load32(v10 + 28)
                                                    v3 = v4
                                                    break
                                                v6 = (v6 + 1)
                                                if (arg2 != (v6 + 1)):
                                                    continue
                                                break
                                            break
                                        if (v3 == 0):
                                            break
                                        v3 = (load32(9561692) + (v9 * 286704))
                                        v4 = load32((load32(9561692) + (v9 * 286704)) + 283848)
                                        if (load32((load32(9561692) + (v9 * 286704)) + 283848) != 2147483647):
                                            store32((v3 + 283848), (load32(v7 + 68) + v4))
                                        v4 = (v3 + 283852)
                                        v6 = load32((v3 + 283852))
                                        if (load32((v3 + 283852)) != 2147483647):
                                            store32(v4, (load32(v7 + 72) + v6))
                                        v4 = (v3 + 283856)
                                        v6 = load32((v3 + 283856))
                                        if (load32((v3 + 283856)) != 2147483647):
                                            store32(v4, (load32(v7 + 76) + v6))
                                        v4 = (v3 + 283860)
                                        v6 = load32((v3 + 283860))
                                        if (load32((v3 + 283860)) != 2147483647):
                                            store32(v4, (load32(v7 + 80) + v6))
                                        v4 = (v3 + 281692)
                                        store32((v3 + 281692), (load32(v4) - load32(v7 + 68)))
                                        v4 = (v3 + 281696)
                                        store32((v3 + 281696), (load32(v4) - load32(v7 + 72)))
                                        v4 = (v3 + 281700)
                                        store32((v3 + 281700), (load32(v4) - load32(v7 + 76)))
                                        v4 = load32(v7 + 80)
                                        store8(v3 + 286701, 1)
                                        v6 = (v3 + 281704)
                                        store32((v3 + 281704), (load32(v6) - v4))
                                        v6 = load32(9142892)
                                        if (u(load32(9142892)) < u(2)):
                                            break
                                        v4 = 1
                                        v13 = (v6 - 1)
                                        v14 = ((v6 - 1) & 1)
                                        v8 = (load32(v3 + 283908) * v6)
                                        v10 = load32(9561692)
                                        v12 = load32(9143016)
                                        if (v6 != 2):
                                            v6 = (v13 & -2)
                                            v3 = 0
                                            while True:  # $label23
                                                if load8u((v12 + (v4 + v8))):
                                                    store8((v10 + (v4 * 286704)) + 286701, 1)
                                                v13 = (v4 + 1)
                                                if load8u((v12 + ((v4 + 1) + v8))):
                                                    store8((v10 + (v13 * 286704)) + 286701, 1)
                                                v4 = (v4 + 2)
                                                v3 = (v3 + 2)
                                                if ((v3 + 2) != v6):
                                                    continue
                                                break
                                        if (v14 == 0):
                                            break
                                        if (load8u((v12 + (v4 + v8))) == 0):
                                            break
                                        store8((v10 + (v4 * 286704)) + 286701, 1)
                                        break
                                        break
                                    arg0 = 57101
                                    if (load32((v8 + (v9 * 286704)) + 283908) == load32(9142872)):
                                        break
                                    break
                                    break
                                arg0 = 57113
                                if (load32((v8 + (v9 * 286704)) + 283908) != load32(9142872)):
                                    break
                                break
                            a_b()
                            break
                            break
                        arg1 = (load32(9671128) + (v8 * 132))
                        arg0 = (G.global0 - 32)
                        G.global0 = (G.global0 - 32)
                        while True:  # block $label25
                            if (load8u(arg1 + 125) == 3):
                                break
                            v3 = load32(9561692)
                            v4 = load16u(arg1 + 110)
                            v5 = (load32(9561692) + (load16u(arg1 + 110) * 286704))
                            if load32((((load32(9561692) + (load16u(arg1 + 110) * 286704)) + (load32(38452) << 2)) + 281808)):
                                break
                            while True:  # block $label28
                                while True:  # block $label29
                                    while True:  # block $label30
                                        while True:  # block $label26
                                            arg2 = (v3 + (v4 * 286704))
                                            v7 = (load32((v3 + (v4 * 286704)) + 283976) + 1)
                                            if (u((load32((v3 + (v4 * 286704)) + 283976) + 1)) > u((load32((arg2 + 284136)) + load32(arg2 + 283980)))):
                                                arg1 = 57101
                                                if (load32(arg2 + 283908) == load32(9142872)):
                                                    break
                                                break
                                            if (u(load32((arg2 + 284000))) >= u(v7)):
                                                arg1 = load32(arg1 + 28)
                                                v7 = load32(v5 + 283868)
                                                if load32(v5 + 283868):
                                                    arg2 = 0
                                                    v5 = (arg1 * 132)
                                                    while True:  # $label27
                                                        v9 = (load32(9671128) + v5)
                                                        v6 = load32(38452)
                                                        if (func59((arg0 + 28), (arg0 + 24), (load32(9671128) + v5), ((load32(38452) * 404) + 9568096)) == 0):
                                                            break
                                                        v9 = func34(v6, load16u(v9 + 110), load32(arg0 + 28), load32(arg0 + 24), 0, 1)
                                                        if (func34(v6, load16u(v9 + 110), load32(arg0 + 28), load32(arg0 + 24), 0, 1) == 0):
                                                            break
                                                        func69((load32(9671128) + v5), v9)
                                                        arg2 = (arg2 + 1)
                                                        if ((arg2 + 1) != v7):
                                                            continue
                                                        break
                                                arg2 = (load32(9671128) + (arg1 * 132))
                                                arg1 = load16u((load32(9671128) + (arg1 * 132)) + 112)
                                                v5 = ((load16u((load32(9671128) + (arg1 * 132)) + 112) << 5) - load32(9142952))
                                                arg2 = load16u(arg2 + 114)
                                                v5 = ((load16u(arg2 + 114) << 5) - load32(9142956))
                                                if ((((((load16u((load32(9671128) + (arg1 * 132)) + 112) << 5) - load32(9142952)) * v5) + (((load16u(arg2 + 114) << 5) - load32(9142956)) * v5)) - 1) > 9000000):
                                                    break
                                                v7 = load32(39876)
                                                v9 = load32(load32(9142424) + 48)
                                                if (load32(load32(9142424) + 48) == 0):
                                                    break
                                                if load8u(9147152):
                                                    break
                                                v5 = load16u((load32(9147376) + (((load32(9142440) * arg2) + arg1) << 1)))
                                                if (v9 != 2):
                                                    break
                                                if (u(v5) > u(1)):
                                                    break
                                                break
                                            arg1 = 57113
                                            if (load32((v3 + (v4 * 286704)) + 283908) != load32(9142872)):
                                                break
                                            break
                                        a_b()
                                        break
                                        break
                                    if (v5 == 0):
                                        break
                                    break
                                store32(arg0 + 8, arg2)
                                store32(arg0 + 4, arg1)
                                store32(arg0, v7)
                                a_b()
                                break
                            arg1 = (v3 + (v4 * 286704))
                            store32((((v3 + (v4 * 286704)) + (load32(39144) << 2)) + 281808), 55)
                            store32(arg1 + 283864, (load32(arg1 + 283864) + 1))
                            arg2 = load32(9213808)
                            if (load32(9213808) == 0):
                                break
                            v3 = load32(38464)
                            arg1 = 0
                            v4 = load32(9671128)
                            while True:  # $label31
                                if (load8u((v4 + (load32(((arg1 << 2) + 9173808)) * 132)) + 122) != v3):
                                    arg1 = (arg1 + 1)
                                    if (arg2 != (arg1 + 1)):
                                        continue
                                    break
                                break
                            break
                        G.global0 = (arg0 + 32)
                        break
                        break
                    if (v12 == 0):
                        break
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v20):
                    continue
                break
            v15 = (v15 + 1)
            if ((v15 + 1) != v21):
                continue
            break
        break
    G.global0 = (v11 + 48)
    return arg0

# ------------------------------------------------------------
# $func134
# ------------------------------------------------------------
def func134(arg0, arg1):
    while True:  # block $label0
        if (arg0 == 0):
            break
        # TODO: i64.div_u []
        v3 = arg0
        while True:  # block $label1
            v4 = i64(arg1)
            v5 = (i64(arg1) * arg0)
            if (u((i64(arg1) * arg0)) > u(4294967295)):
                break
            if (u(v3) < u(v4)):
                break
            if (v5 == 0):
                break
            v2 = func252(i32(arg0), arg1)
            break
        return v2
        break
    a_c()
    raise RuntimeError('unreachable')
    return 5188

# ------------------------------------------------------------
# $func135
# ------------------------------------------------------------
def func135(arg0):
    while True:  # block $label2
        v2 = load32(arg0 + 20)
        if (load32(arg0 + 20) > 31):
            v3 = load32(arg0 + 12)
            v1 = load32(arg0 + 16)
            if (u(load32(arg0 + 12)) > u((load32(arg0 + 16) + 8))):
                store32(arg0 + 20, (v2 - 32))
                v7 = ((load64(arg0) & 0xFFFFFFFFFFFFFFFF) >> 32)
                store64(arg0, ((load64(arg0) & 0xFFFFFFFFFFFFFFFF) >> 32))
                v8 = load32u((load32(arg0 + 8) + v1))
                store32(arg0 + 16, (v1 + 4))
                store64(arg0, ((v8 << 32) | v7))
                return
            v5 = (v1 if (u(v1) > u(v3)) else v3)
            while True:  # $label1
                while True:  # block $label0
                    if (v1 == v5):
                        v1 = v5
                        v4 = v2
                        break
                    v7 = ((load64(arg0) & 0xFFFFFFFFFFFFFFFF) >> 8)
                    store64(arg0, ((load64(arg0) & 0xFFFFFFFFFFFFFFFF) >> 8))
                    v8 = load64((load32(arg0 + 8) + v1))
                    v4 = (v2 - 8)
                    store32(arg0 + 20, (v2 - 8))
                    v1 = (v1 + 1)
                    store32(arg0 + 16, (v1 + 1))
                    store64(arg0, ((v8 << 56) | v7))
                    v6 = (v2 > 15)
                    v2 = v4
                    if v6:
                        continue
                    break
                break
            if (u(v1) > u(v3)):
                break
            while True:  # block $label3
                if (load32(arg0 + 24) == 0):
                    if (v1 != v3):
                        break
                    if (v4 < 65):
                        break
                store64(arg0 + 20, 4294967296)
                break
            return
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func136
# ------------------------------------------------------------
def func136(arg0):
    if arg0:
        store32(arg0, 0)

# ------------------------------------------------------------
# $func137
# ------------------------------------------------------------
def func137(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    if (arg3 > 0):
        v19 = ((arg4 << 1) | 1)
        v20 = (arg1 * 3)
        v21 = (0 - arg1)
        v22 = (arg1 * -3)
        v23 = (0 - (arg1 << 2))
        v24 = (arg1 << 1)
        v25 = (0 - (arg1 << 1))
        v15 = load32(16308)
        v9 = load32(17088)
        v16 = load32(16076)
        v7 = load32(17616)
        while True:  # $label2
            arg4 = arg3
            while True:  # block $label0
                v26 = (arg0 + v25)
                v10 = load8u((arg0 + v25))
                v27 = (arg0 + arg1)
                v14 = load8u((arg0 + arg1))
                v8 = (load8u((arg0 + v25)) - load8u((arg0 + arg1)))
                v17 = (arg0 + v21)
                arg3 = load8u((arg0 + v21))
                v11 = load8u(arg0)
                if ((load8u((v7 + (load8u((arg0 + v25)) - load8u((arg0 + arg1))))) + (load8u((v7 + (load8u((arg0 + v21)) - load8u(arg0)))) << 2)) > v19):
                    break
                v28 = (arg0 + v22)
                v12 = load8u((arg0 + v22))
                if (load8u((v7 + (load8u((arg0 + v23)) - load8u((arg0 + v22))))) > arg5):
                    break
                if (load8u((v7 + (v12 - v10))) > arg5):
                    break
                v29 = load8u((v7 + (v10 - arg3)))
                if (load8u((v7 + (v10 - arg3))) > arg5):
                    break
                v13 = (arg0 + v24)
                v18 = load8u((arg0 + v24))
                if (load8u((v7 + (load8u((arg0 + v20)) - load8u((arg0 + v24))))) > arg5):
                    break
                if (load8u((v7 + (v18 - v14))) > arg5):
                    break
                v30 = load8u((v7 + (v14 - v11)))
                if (load8u((v7 + (v14 - v11))) > arg5):
                    break
                v8 = (load8s((v8 + v16)) + ((v11 - arg3) * 3))
                while True:  # block $label1
                    if (((arg6 >= v29) & (arg6 >= v30)) == 0):
                        v13 = load8s((v15 + ((v8 + 4) >> 3)))
                        store8(v17, load8u((v9 + (load8s((v15 + ((v8 + 3) >> 3))) + arg3))))
                        arg3 = (v11 - v13)
                        v13 = arg0
                        break
                    v8 = load8s((v8 + v16))
                    v12 = (((load8s((v8 + v16)) * 9) + 63) >> 7)
                    store8(v28, load8u((v9 + (v12 + (((load8s((v8 + v16)) * 9) + 63) >> 7)))))
                    v10 = (((v8 * 18) + 63) >> 7)
                    store8(v26, load8u((v9 + (v10 + (((v8 * 18) + 63) >> 7)))))
                    arg3 = (((v8 * 27) + 63) >> 7)
                    store8(v17, load8u((v9 + (arg3 + (((v8 * 27) + 63) >> 7)))))
                    store8(arg0, load8u((v9 + (v11 - arg3))))
                    store8(v27, load8u((v9 + (v14 - v10))))
                    arg3 = (v18 - v12)
                    break
                store8(v13, load8u((arg3 + v9)))
                break
            arg3 = (arg4 - 1)
            arg0 = (arg0 + arg2)
            if (u(arg4) > u(1)):
                continue
            break

# ------------------------------------------------------------
# $func138
# ------------------------------------------------------------
def func138(arg0):
    v1 = (G.global0 - 144)
    G.global0 = (G.global0 - 144)
    while True:  # block $label0
        if (load32(arg0 + 40) == 0):
            break
        func77(arg0)
        v2 = load32(arg0 + 40)
        while True:  # block $label1
            if load8u(9142916):
                store32(v1 + 128, v2)
                a_b()
                break
            store32(v1 + 120, v2)
            store64(v1 + 112, -4602115869219225600)
            store64(v1 + 104, 0)
            store64(v1 + 96, 0)
            a_b()
            break
        while True:  # block $label2
            v2 = load32(arg0 + 24)
            if (load32(arg0 + 24) == 0):
                break
            v3 = load32(v2 + 4)
            if (load32(v2 + 4) == 0):
                break
            if (load32(v3 + 8) == 0):
                break
            v2 = 0
            v5 = (v1 - -64)
            while True:  # $label4
                while True:  # block $label3
                    v4 = load32((load32(v3) + ((v2 << 2) | 4)))
                    if (load32((load32(v3) + ((v2 << 2) | 4))) == 0):
                        break
                    if load8u(9142916):
                        store32(v1 + 80, v4)
                        a_b()
                        break
                    store32(v1 + 72, v4)
                    store64(v5, -4602115869219225600)
                    store64(v1 + 56, 0)
                    store64(v1 + 48, 0)
                    a_b()
                    break
                v2 = (v2 + 2)
                if (u((v2 + 2)) < u(load32(v3 + 8))):
                    continue
                break
            break
        v3 = load32(arg0 + 12)
        if (load32(arg0 + 12) == 0):
            break
        if (load32(v3 + 8) == 0):
            break
        v2 = 0
        while True:  # $label6
            v3 = load32((load32(v3) + (v2 << 2)))
            while True:  # block $label5
                if load8u(9142916):
                    store32(v1 + 32, v3)
                    a_b()
                    break
                store32(v1 + 24, v3)
                store64(v1 + 16, -4602115869219225600)
                store64(v1 + 8, 0)
                store64(v1, 0)
                a_b()
                break
            v2 = (v2 + 2)
            v3 = load32(arg0 + 12)
            if (u((v2 + 2)) < u(load32(load32(arg0 + 12) + 8))):
                continue
            break
        break
    G.global0 = (v1 + 144)

# ------------------------------------------------------------
# $func139
# ------------------------------------------------------------
def func139(arg0, arg1, arg2, arg3):
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v4 = load32(arg0 + 36)
        if (load32(arg0 + 36) == 0):
            break
        v6 = load32(9671128)
        v8 = (load32(9671128) + (v4 * 132))
        v9 = ((load8u(v8 + 122) * 404) + 9568096)
        v7 = (arg0 if (load32(((load8u(v8 + 122) * 404) + 9568096) + 264) == 1) else (load32(9671128) + (v4 * 132)))
        store32(v5 + 12, load16u((arg0 if (load32(((load8u(v8 + 122) * 404) + 9568096) + 264) == 1) else (load32(9671128) + (v4 * 132))) + 112))
        store32(v5 + 8, load16u(v7 + 114))
        while True:  # block $label9
            while True:  # block $label2
                while True:  # block $label1
                    if arg2:
                        break
                    if arg3:
                        break
                    arg3 = ((load8u(arg0 + 122) * 404) + 9568096)
                    v7 = (v6 + (v4 * 132))
                    v10 = load16u((v6 + (v4 * 132)) + 118)
                    v7 = load16u(v7 + 116)
                    v10 = (load16u(v7 + 116) | v10)
                    v11 = ((load16u((v6 + (v4 * 132)) + 118) if (load16u(v7 + 116) | v10) else load16u(arg0 + 114)) & 65535)
                    v7 = ((v7 if v10 else load16u(arg0 + 112)) & 65535)
                    if (((load16u((v6 + (v4 * 132)) + 118) if (load16u(v7 + 116) | v10) else load16u(arg0 + 114)) & 65535) | ((v7 if v10 else load16u(arg0 + 112)) & 65535)):
                        if func337((v5 + 12), (v5 + 8), v8, arg3, v7, v11):
                            break
                        break
                    if (func338((v5 + 12), (v5 + 8), v8, arg3) == 0):
                        break
                    break
                while True:  # block $label3
                    if (load32(v9 + 264) != 4):
                        break
                    arg1 = (v6 + (v4 * 132))
                    if (load8u((v6 + (v4 * 132)) + 125) != 3):
                        break
                    arg3 = (load16u(arg1 + 112) - load32(v5 + 12))
                    arg1 = (load16u(arg1 + 114) - load32(v5 + 8))
                    if (((((load16u(arg1 + 112) - load32(v5 + 12)) * arg3) + ((load16u(arg1 + 114) - load32(v5 + 8)) * arg1)) - 1) < 17):
                        break
                    break
                    break
                store32(arg0 + 36, 0)
                while True:  # block $label4
                    if arg2:
                        break
                    store16(arg0 + 112, load32(v5 + 12))
                    store16(arg0 + 114, load32(v5 + 8))
                    while True:  # block $label5
                        if (load32(arg0 + 40) == 0):
                            break
                        break
                    arg3 = ((load8u(arg0 + 122) * 404) + 9568096)
                    if load32(((load8u(arg0 + 122) * 404) + 9568096) + 216):
                        v9 = load32(9142840)
                        v7 = load16u(arg0 + 114)
                        v10 = load16u(arg0 + 112)
                        arg1 = 0
                        while True:  # $label7
                            arg1 = (arg1 + 1)
                            v11 = ((arg1 + 1) + v10)
                            arg2 = 0
                            while True:  # $label6
                                arg2 = (arg2 + 1)
                                v12 = (load32(9142440) + 2)
                                store32((v9 + ((v11 + ((((arg2 + 1) + v7) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v12)) << 2)), load32(arg0 + 28))
                                v12 = load32(arg3 + 216)
                                if (u(arg2) < u(load32(arg3 + 216))):
                                    continue
                                break
                            if (u(arg1) < u(v12)):
                                continue
                            break
                    func29(arg0, 1)
                    func118(arg0)
                    arg1 = load32(arg0 + 92)
                    if (load32(arg0 + 92) == 0):
                        break
                    break
                while True:  # block $label8
                    arg1 = ((load8u(arg0 + 122) * 404) + 9568096)
                    if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) != 2):
                        break
                    if (load32(arg1 + 268) != 2):
                        break
                    arg1 = (v6 + (v4 * 132))
                    store32((v6 + (v4 * 132)) + 52, (load32(arg1 + 52) - load32(arg0 + 52)))
                    store32(arg1 + 60, (load32(arg1 + 60) - load32(arg0 + 60)))
                    break
                arg1 = load32((v6 + (v4 * 132)) + 16)
                if (load32((v6 + (v4 * 132)) + 16) == 0):
                    break
                while True:  # block $label10
                    v9 = load32(arg1 + 8)
                    if (load32(arg1 + 8) == 0):
                        break
                    arg0 = load32(arg0 + 28)
                    arg3 = load32(arg1)
                    arg2 = 0
                    while True:  # $label12
                        if (arg0 == load32((arg3 + (arg2 << 2)))):
                            arg0 = (v9 - 1)
                            store32(arg1 + 8, (v9 - 1))
                            if (u(arg0) > u(arg2)):
                                while True:  # $label11
                                    arg2 = (arg2 + 1)
                                    store32((arg3 + (arg2 << 2)), load32((arg3 + ((arg2 + 1) << 2))))
                                    arg0 = load32(arg1 + 8)
                                    if (u(arg2) < u(load32(arg1 + 8))):
                                        continue
                                    break
                            if arg0:
                                break
                            break
                        arg2 = (arg2 + 1)
                        if ((arg2 + 1) != v9):
                            continue
                        break
                    break
                    break
                if (load32(((load8u(v8 + 122) * 404) + 9568096) + 264) != 1):
                    break
                arg1 = load32(9215892)
                if (u(load32(9215892)) < u(5)):
                    break
                arg3 = load32((v6 + (v4 * 132)) + 28)
                arg0 = load32(9215884)
                arg2 = 4
                while True:  # $label14
                    while True:  # block $label13
                        v8 = (arg2 << 2)
                        if (load32((arg0 + ((arg2 << 2) | 4))) != 57):
                            break
                        if (load32((arg0 + (v8 | 8))) != arg3):
                            break
                        store32((arg0 + (arg2 << 2)), 0)
                        break
                        break
                    arg2 = (arg2 + 4)
                    if (u((arg2 + 4)) < u(arg1)):
                        continue
                    break
                break
                break
            if (arg1 == 0):
                break
            break
        while True:  # block $label15
            arg0 = (v6 + (v4 * 132))
            if (load32((v6 + (v4 * 132)) + 92) == 0):
                break
            if (load8u(9147152) == 0):
                arg1 = (v6 + (v4 * 132))
                if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u((v6 + (v4 * 132)) + 110))))) == 0):
                    break
                if (load32((load32(9215884) + (load32(arg1 + 44) << 4)) + 4) == 20):
                    break
                if (load8u((v6 + (v4 * 132)) + 127) == 6):
                    break
            while True:  # block $label16
                if (load8u(9147141) == 0):
                    break
                arg1 = load32((v6 + (v4 * 132)) + 16)
                if (load32((v6 + (v4 * 132)) + 16) == 0):
                    break
                if (load32(arg1 + 8) == 0):
                    break
                Ya(1)
                break
                break
            store8(9147141, 0)
            if load32(9140316):
                if (load32(9140320) != load32((v6 + (v4 * 132)) + 28)):
                    break
            break
        arg0 = load32(arg0 + 24)
        if (load32(arg0 + 24) == 0):
            break
        arg1 = load32(arg0 + 4)
        if (load32(arg0 + 4) == 0):
            break
        arg3 = load32((v6 + (v4 * 132)) + 16)
        arg2 = 0
        v4 = load32(9671128)
        while True:  # $label17
            arg0 = 0
            if arg3:
            else:
            if (u(0) > u(arg2)):
                arg0 = (arg2 << 2)
                arg2 = (arg2 + 1)
                if (load32(((load8u((v4 + (load32((arg0 + load32(arg3))) * 132)) + 122) * 404) + 9568096) + 264) != 2):
                    continue
                break
            break
        arg3 = load32(arg1 + 8)
        if (load32(arg1 + 8) == 0):
            break
        arg0 = load32(arg1)
        arg2 = 0
        while True:  # $label21
            while True:  # block $label18
                v4 = (arg2 << 2)
                if load32((arg0 + (arg2 << 2))):
                    break
                v4 = load32((arg0 + (v4 | 4)))
                if (load32((arg0 + (v4 | 4))) == 0):
                    break
                func38(v4)
                arg0 = (load32(arg1 + 8) - 1)
                store32(arg1 + 8, (load32(arg1 + 8) - 1))
                if (u(arg0) > u(arg2)):
                    v4 = load32(arg1)
                    arg3 = arg2
                    while True:  # $label19
                        arg3 = (arg3 + 1)
                        store32((v4 + (arg3 << 2)), load32((v4 + ((arg3 + 1) << 2))))
                        arg0 = load32(arg1 + 8)
                        if (u(arg3) < u(load32(arg1 + 8))):
                            continue
                        break
                arg0 = (arg0 - 1)
                store32(arg1 + 8, (arg0 - 1))
                if (u(arg0) <= u(arg2)):
                    break
                arg0 = load32(arg1)
                while True:  # $label20
                    arg2 = (arg2 + 1)
                    store32((arg0 + (arg2 << 2)), load32((arg0 + ((arg2 + 1) << 2))))
                    if (u(arg2) < u(load32(arg1 + 8))):
                        continue
                    break
                break
                break
            arg2 = (arg2 + 2)
            if (u((arg2 + 2)) < u(arg3)):
                continue
            break
        break
    G.global0 = (v5 + 16)
    return load32(arg3 + 8)

# ------------------------------------------------------------
# $func140
# ------------------------------------------------------------
def func140(arg0):
    store8(arg0 + 125, 7)
    func92(arg0, 0.0, 0.0)
    if load8u(9142916):
    v1 = ((load8u(arg0 + 122) * 404) + 9568096)
    if load32(((load8u(arg0 + 122) * 404) + 9568096) + 216):
        v5 = load32(9142840)
        v6 = load16u(arg0 + 114)
        v7 = load16u(arg0 + 112)
        while True:  # $label1
            v2 = (v2 + 1)
            v8 = ((v2 + 1) + v7)
            v3 = 0
            while True:  # $label0
                v3 = (v3 + 1)
                v4 = (load32(9142440) + 2)
                store32((v5 + ((v8 + ((((v3 + 1) + v6) + ((load32(9142440) + 2) * load32(v1 + 208))) * v4)) << 2)), load32(arg0 + 28))
                v4 = load32(v1 + 216)
                if (u(v3) < u(load32(v1 + 216))):
                    continue
                break
            if (u(v2) < u(v4)):
                continue
            break
    v1 = load32(v1 + 260)
    if load32(v1 + 260):
        # TODO: i32.div_u []
        store32(load32(9142848), ((32000 // v1) + 25))

# ------------------------------------------------------------
# $func141
# ------------------------------------------------------------
def func141(arg0, arg1):
    v9 = (arg0 // 32)
    v19 = ((arg0 // 32) + 3)
    v10 = load32(9142440)
    v15 = (load32(9142440) + 2)
    v11 = (arg1 // 32)
    v20 = ((arg1 // 32) + 4)
    v11 = (v11 - 3)
    v8 = (v9 - 3)
    v21 = load32(9142848)
    v22 = load32(9215884)
    v23 = load32(38448)
    v24 = load32(9671128)
    v25 = load32(9142840)
    v26 = load32(9147376)
    v27 = load32(9142424)
    v12 = 2147483647
    v28 = (load8u(9147152) == 0)
    v29 = load8u(9142408)
    while True:  # $label4
        v9 = (v8 + 1)
        v2 = v11
        if (u(v8) < u(v10)):
            while True:  # $label3
                if ((u(v2) < u(v10)) & ((v2 | v8) >= 0)):
                    v13 = 0
                    v30 = ((load32(v27 + 48) != 0) & v28)
                    v16 = (v2 + 1)
                    v31 = (v26 + (((v2 * v10) + v8) << 1))
                    while True:  # $label2
                        while True:  # block $label0
                            if v30:
                                if (load16u(v31) == 0):
                                    break
                            v17 = load32((v25 + ((v9 + ((v16 + (v13 * v15)) * v15)) << 2)))
                            if (u(load32((v25 + ((v9 + ((v16 + (v13 * v15)) * v15)) << 2)))) < u(3)):
                                break
                            v3 = (v24 + (v17 * 132))
                            if (load32((v24 + (v17 * 132)) + 40) == 0):
                                break
                            if v29:
                                if (v23 == load8u(v3 + 122)):
                                    break
                            v7 = (load16u(v3 + 112) << 5)
                            v4 = load32(v3 + 48)
                            if load32(v3 + 48):
                                v7 = (v7 - load32(v4 + 8))
                            else:
                            v5 = (load32(v4 + 12) - 0)
                            if (load8u(v3 + 125) == 1):
                                v6 = (load8u(v3 + 124) << 3)
                                v2 = load32(((load8u(v3 + 124) << 3) + 8996))
                                v5 = (v5 - (load32(((load8u(v3 + 124) << 3) + 8996)) << 5))
                                v14 = load32((v6 + 8992))
                                v6 = (v7 - (load32((v6 + 8992)) << 5))
                                v2 = load32(((load8u(v3 + 122) * 404) + 9568096) + 260)
                                if load32(((load8u(v3 + 122) * 404) + 9568096) + 260):
                                else:
                                v2 = (0 * v2)
                                v5 = (v2 + (((((load32((v22 + (load32(v3 + 44) << 4))) - v21) * -25) + (32000 // v2)) * (0 * v2)) // 1000))
                                v7 = (v6 + ((v2 * v14) // 1000))
                            while True:  # block $label1
                                if v4:
                                    v2 = (load32(v4 + 4) // (load32(v4 + 20) * load32(v4 + 16)))
                                    break
                                v6 = ((load8u(v3 + 122) * 404) + 9568096)
                                v2 = (load32(((load8u(v3 + 122) * 404) + 9568096) + 220) << 5)
                                break
                            v3 = (load32(v6 + 216) << 5)
                            v6 = (v2 < 32)
                            v4 = ((v5 - 16) if (v2 < 32) else v5)
                            v14 = (48 if v6 else v2)
                            v2 = (arg1 - (((v5 - 16) if (v2 < 32) else v5) + (((48 if v6 else v2) & 0xFFFFFFFF) >> 1)))
                            v2 = (v3 < 32)
                            v5 = ((v7 - 16) if (v3 < 32) else v7)
                            v6 = (48 if v2 else v3)
                            v2 = (arg0 - (((v7 - 16) if (v3 < 32) else v7) + (((48 if v2 else v3) & 0xFFFFFFFF) >> 1)))
                            v2 = (((arg1 - (((v5 - 16) if (v2 < 32) else v5) + (((48 if v6 else v2) & 0xFFFFFFFF) >> 1))) * v2) + ((arg0 - (((v7 - 16) if (v3 < 32) else v7) + (((48 if v2 else v3) & 0xFFFFFFFF) >> 1))) * v2))
                            v2 = (((((v2 < v12) & (arg0 > v5)) & ((v5 + v6) > arg0)) & (arg1 > v4)) & ((v4 + v14) > arg1))
                            v12 = ((((arg1 - (((v5 - 16) if (v2 < 32) else v5) + (((48 if v6 else v2) & 0xFFFFFFFF) >> 1))) * v2) + ((arg0 - (((v7 - 16) if (v3 < 32) else v7) + (((48 if v2 else v3) & 0xFFFFFFFF) >> 1))) * v2)) if (((((v2 < v12) & (arg0 > v5)) & ((v5 + v6) > arg0)) & (arg1 > v4)) & ((v4 + v14) > arg1)) else v12)
                            v18 = (v17 if v2 else v18)
                            break
                        v13 = (v13 + 1)
                        if ((v13 + 1) != 3):
                            continue
                        break
                else:
                v2 = (v2 + 1)
                if (v16 != (v2 + 1)):
                    continue
                break
        v2 = (v8 == v19)
        v8 = v9
        if (v2 == 0):
            continue
        break
    return v18

# ------------------------------------------------------------
# $func142
# ------------------------------------------------------------
def func142(arg0, arg1):
    v12 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # block $label1
        while True:  # block $label0
            v14 = load32(9561692)
            v16 = load16u(arg0 + 110)
            v18 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
            v2 = load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 281804)
            if (load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 281804) == 0):
                break
            if (u(((load32(9142848) - v2) * 25)) > u(29999)):
                break
            if (arg1 == 0):
                break
            func29(arg0, 1)
            break
            break
        v23 = load32(v18 + 283876)
        v24 = load32(v18 + 283872)
        store8(arg0 + 129, 2)
        while True:  # block $label2
            v19 = load32(((load32(v18 + 283960) << 2) + 9687152))
            v30 = ((v18 + (load32(((load32(v18 + 283960) << 2) + 9687152)) << 2)) + 284636)
            v2 = load32(((v18 + (load32(((load32(v18 + 283960) << 2) + 9687152)) << 2)) + 284636))
            if (load32(((v18 + (load32(((load32(v18 + 283960) << 2) + 9687152)) << 2)) + 284636)) == 0):
                break
            v20 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                break
            v6 = load32(9142440)
            v9 = (load32(9142440) + 2)
            v21 = load32(38448)
            v27 = load32(9142840)
            v10 = load32(9671128)
            v17 = load32(v2)
            v28 = 1
            while True:  # $label14
                while True:  # block $label3
                    v2 = load32((v17 + (v7 << 2)))
                    if (load32((v17 + (v7 << 2))) == 0):
                        break
                    while True:  # block $label4
                        while True:  # block $label5
                            v3 = (v10 + (v2 * 132))
                            # br_table[load8u((v10 + (v2 * 132)) + 125)]
                            break
                            break
                        break
                        break
                    v15 = load16u(v3 + 114)
                    v25 = (load16u(v3 + 114) + 11)
                    v13 = load16u(v3 + 112)
                    v26 = (load16u(v3 + 112) + 11)
                    v3 = (v13 - 6)
                    v8 = (v15 - 6)
                    v11 = 0
                    while True:  # $label8
                        v5 = (v3 + 1)
                        if (u(v3) < u(v6)):
                            v2 = (v3 - v13)
                            v22 = (((v3 - v13) * v2) - 1)
                            v2 = v8
                            while True:  # $label7
                                while True:  # block $label6
                                    v4 = v2
                                    v2 = (v2 - v15)
                                    if ((v22 + ((v2 - v15) * v2)) > 36):
                                        break
                                    if (u(v4) >= u(v6)):
                                        break
                                    if ((v3 | v4) < 0):
                                        break
                                    v2 = load32((v27 + (((((v4 + v9) + 1) * v9) + v5) << 2)))
                                    if (u(load32((v27 + (((((v4 + v9) + 1) * v9) + v5) << 2)))) < u(3)):
                                        break
                                    v11 = (v11 + (v21 == load8u((v10 + (v2 * 132)) + 122)))
                                    break
                                v2 = (v4 + 1)
                                if (v4 != v25):
                                    continue
                                break
                        v2 = (v3 != v26)
                        v3 = v5
                        if v2:
                            continue
                        break
                    if (u(v11) < u(4)):
                        break
                    v20 = (v13 + 9)
                    v17 = (v15 + 9)
                    v11 = (v15 - 10)
                    v4 = (v13 - 10)
                    v25 = (v9 * load32(((v21 * 404) + 9568096) + 208))
                    v3 = 2147483647
                    v8 = 0
                    while True:  # $label11
                        v7 = (v4 + 1)
                        if (u(v4) < u(v6)):
                            v2 = (v13 - v4)
                            v26 = ((v13 - v4) * v2)
                            v2 = v11
                            while True:  # $label10
                                while True:  # block $label9
                                    v5 = v2
                                    if (u(v6) <= u(v2)):
                                        break
                                    if ((v4 | v5) < 0):
                                        break
                                    v2 = (v15 - v5)
                                    v22 = (((v15 - v5) * v2) + v26)
                                    if ((((v15 - v5) * v2) + v26) >= v3):
                                        break
                                    v2 = load32((v27 + (((((v5 + v25) + 1) * v9) + v7) << 2)))
                                    if (load32((v27 + (((((v5 + v25) + 1) * v9) + v7) << 2))) == 0):
                                        break
                                    v22 = (v21 == load8u((v10 + (v2 * 132)) + 122))
                                    v3 = (v22 if (v21 == load8u((v10 + (v2 * 132)) + 122)) else v3)
                                    v8 = (v2 if v22 else v8)
                                    break
                                v2 = (v5 + 1)
                                if (v5 != v17):
                                    continue
                                break
                        v2 = (v4 != v20)
                        v4 = v7
                        if v2:
                            continue
                        break
                    while True:  # block $label12
                        if v8:
                            break
                        while True:  # block $label13
                            v2 = load32(arg0 + 44)
                            if (load32(arg0 + 44) == 0):
                                break
                            v3 = load32(9215884)
                            if (load32((load32(9215884) + (v2 << 4)) + 12) == 1):
                                break
                            if (load8u(arg0 + 125) == 7):
                                break
                            if (load32((v3 + ((v2 << 4) | 4))) == 0):
                                break
                            break
                        func29(arg0, 1)
                        break
                    if (v28 == 0):
                        break
                    break
                    break
                v7 = (v7 + 1)
                v28 = (u((v7 + 1)) < u(v20))
                if (v7 != v20):
                    continue
                break
            break
        while True:  # block $label16
            while True:  # block $label15
                v21 = ((v19 * 404) + 9568096)
                v2 = (v14 + (v16 * 286704))
                if (load32(((v19 * 404) + 9568096) + 68) > load32((v14 + (v16 * 286704)) + 283848)):
                    break
                if (load32(v21 + 72) > load32((v2 + 283852))):
                    break
                v2 = ((v19 * 404) + 9568096)
                v3 = (v14 + (v16 * 286704))
                if (load32(((v19 * 404) + 9568096) + 76) > load32(((v14 + (v16 * 286704)) + 283856))):
                    break
                if (load32(v2 + 80) <= load32((v3 + 283860))):
                    break
                break
            v7 = load32(9142440)
            v11 = (load32(9142440) + 2)
            v15 = load32(38448)
            v13 = ((load32(9142440) + 2) * load32(((load32(38448) * 404) + 9568096) + 208))
            v9 = (v23 + 24)
            v10 = (v24 + 24)
            v8 = (v23 - 25)
            arg1 = (v24 - 25)
            v18 = load32(9671128)
            v14 = load32(9142840)
            v3 = 2147483647
            v6 = 0
            while True:  # $label19
                v5 = (arg1 + 1)
                if (u(arg1) < u(v7)):
                    v2 = (v24 - arg1)
                    v16 = ((v24 - arg1) * v2)
                    v2 = v8
                    while True:  # $label18
                        while True:  # block $label17
                            v4 = v2
                            if (u(v7) <= u(v2)):
                                break
                            if ((arg1 | v4) < 0):
                                break
                            v2 = (v23 - v4)
                            v19 = (((v23 - v4) * v2) + v16)
                            if ((((v23 - v4) * v2) + v16) >= v3):
                                break
                            v2 = load32((v14 + (((((v4 + v13) + 1) * v11) + v5) << 2)))
                            if (load32((v14 + (((((v4 + v13) + 1) * v11) + v5) << 2))) == 0):
                                break
                            v19 = (v15 == load8u((v18 + (v2 * 132)) + 122))
                            v3 = (v19 if (v15 == load8u((v18 + (v2 * 132)) + 122)) else v3)
                            v6 = (v2 if v19 else v6)
                            break
                        v2 = (v4 + 1)
                        if (v4 < v9):
                            continue
                        break
                v2 = (arg1 < v10)
                arg1 = v5
                if v2:
                    continue
                break
            if v6:
                break
            while True:  # block $label20
                arg1 = load32(arg0 + 44)
                if (load32(arg0 + 44) == 0):
                    break
                v2 = load32(9215884)
                if (load32((load32(9215884) + (arg1 << 4)) + 12) == 1):
                    break
                if (load8u(arg0 + 125) == 7):
                    break
                if load32((v2 + ((arg1 << 4) | 4))):
                    break
                break
                break
            func29(arg0, 1)
            break
            break
        if (u(load32(9142440)) >= u(2)):
            v7 = (v24 - 1)
            v8 = (v23 - 1)
            v10 = (v24 + 2)
            v9 = (v23 + 2)
            v22 = ((v14 + (v16 * 286704)) + 283908)
            v14 = 1
            while True:  # $label37
                while True:  # block $label21
                    if (v7 >= v10):
                        break
                    if (v8 >= v9):
                        break
                    v16 = (v10 - 1)
                    v20 = (v9 - 1)
                    v27 = 1
                    v5 = v7
                    while True:  # $label36
                        while True:  # block $label35
                            v28 = 1
                            v2 = v8
                            v4 = v8
                            while True:  # block $label25
                                v15 = (v5 - 6)
                                v31 = (v5 + 12)
                                if ((v5 - 6) >= (v5 + 12)):
                                    while True:  # $label24
                                        while True:  # block $label23
                                            while True:  # block $label22
                                                if (v5 == v7):
                                                    break
                                                if (v2 == v8):
                                                    break
                                                if (v2 == v20):
                                                    break
                                                if (v5 != v16):
                                                    break
                                                break
                                            v3 = load32(9142440)
                                            if (u(load32(9142440)) <= u(v2)):
                                                break
                                            if ((v2 | v5) < 0):
                                                break
                                            if (u(v3) <= u(v5)):
                                                break
                                            break
                                        v2 = (v2 + 1)
                                        if ((v2 + 1) != v9):
                                            continue
                                        break
                                        break
                                    raise RuntimeError('unreachable')
                                while True:  # $label34
                                    while True:  # block $label31
                                        while True:  # block $label27
                                            while True:  # block $label26
                                                if (v5 == v7):
                                                    break
                                                if (v4 == v8):
                                                    break
                                                if (v4 == v20):
                                                    break
                                                if (v5 != v16):
                                                    break
                                                break
                                            v2 = load32(9142440)
                                            if (u(load32(9142440)) <= u(v4)):
                                                break
                                            if ((v4 | v5) < 0):
                                                break
                                            if (u(v2) <= u(v5)):
                                                break
                                            if (func73(v5, v4, v21, 0, 0, 1) == 0):
                                                break
                                            v13 = (v4 - 6)
                                            v32 = (v4 + 12)
                                            if ((v4 - 6) >= (v4 + 12)):
                                                break
                                            v6 = 0
                                            v17 = load32(9142440)
                                            v25 = (load32(9142440) + 2)
                                            v33 = load32(38448)
                                            v26 = load32(9671128)
                                            v34 = load32(9142840)
                                            v3 = v15
                                            while True:  # $label30
                                                v11 = (v3 + 1)
                                                if (u(v3) < u(v17)):
                                                    v2 = (v3 - v5)
                                                    v35 = (((v3 - v5) * v2) - 1)
                                                    v2 = v13
                                                    while True:  # $label29
                                                        while True:  # block $label28
                                                            v29 = (v2 - v4)
                                                            if ((v35 + ((v2 - v4) * v29)) > 36):
                                                                break
                                                            if (u(v2) >= u(v17)):
                                                                break
                                                            if ((v2 | v3) < 0):
                                                                break
                                                            v29 = load32((v34 + (((((v2 + v25) + 1) * v25) + v11) << 2)))
                                                            if (u(load32((v34 + (((((v2 + v25) + 1) * v25) + v11) << 2)))) < u(3)):
                                                                break
                                                            v6 = (v6 + (v33 == load8u((v26 + (v29 * 132)) + 122)))
                                                            break
                                                        v2 = (v2 + 1)
                                                        if ((v2 + 1) != v32):
                                                            continue
                                                        break
                                                v3 = v11
                                                if (v11 != v31):
                                                    continue
                                                break
                                            if (u(v6) < u(11)):
                                                break
                                            if (func108(v5, v4, load32(v22), 7) == 0):
                                                break
                                            v2 = load32(v30)
                                            if (load32(v30) == 0):
                                                break
                                            v3 = load32(v2 + 8)
                                            if (load32(v2 + 8) == 0):
                                                break
                                            v13 = load32(v2)
                                            v2 = 0
                                            v11 = 1
                                            while True:  # $label33
                                                while True:  # block $label32
                                                    v6 = load32((v13 + (v2 << 2)))
                                                    if load32((v13 + (v2 << 2))):
                                                        v6 = (v26 + (v6 * 132))
                                                        v17 = (v5 - load16u((v26 + (v6 * 132)) + 112))
                                                        v6 = (v4 - load16u(v6 + 114))
                                                        if (((((v5 - load16u((v26 + (v6 * 132)) + 112)) * v17) + ((v4 - load16u(v6 + 114)) * v6)) - 1) <= 81):
                                                            break
                                                    v2 = (v2 + 1)
                                                    v11 = (u((v2 + 1)) < u(v3))
                                                    if (v2 != v3):
                                                        continue
                                                    break
                                                    break
                                                break
                                            if (v11 == 0):
                                                break
                                            break
                                        v4 = (v4 + 1)
                                        v28 = ((v4 + 1) < v9)
                                        if (v4 != v9):
                                            continue
                                        break
                                        break
                                    break
                                v2 = load32(arg0 + 28)
                                store32(v12 + 24, v4)
                                store32(v12 + 20, v5)
                                store32(v12 + 16, v19)
                                v3 = load16u(arg0 + 110)
                                store64(v12 + 48, 4294967297)
                                store64(v12 + 40, 4294967297)
                                store64(v12 + 32, 4294967297)
                                store32(v12 + 28, v3)
                                store32(v12 + 56, 0)
                                store32(v12 + 12, v2)
                                if load32(load32(9142424) + 156):
                                    func29((load32(9671128) + (v2 * 132)), 1)
                                if v28:
                                    break
                                break
                            v5 = (v5 + 1)
                            v27 = ((v5 + 1) < v10)
                            if (v5 != v10):
                                continue
                            break
                            break
                        break
                    if v27:
                        break
                    break
                v9 = (v9 + 1)
                v10 = (v10 + 1)
                v14 = (v14 + 1)
                v8 = (v23 - (v14 + 1))
                v7 = (v24 - v14)
                if (u(v14) < u(load32(9142440))):
                    continue
                break
        store32((v18 + 281804), load32(9142848))
        if (arg1 == 0):
            break
        func29(arg0, 1)
        break
    v2 = 0
    G.global0 = (v12 - -64)
    return v2

# ------------------------------------------------------------
# $func143
# ------------------------------------------------------------
def func143(arg0, arg1):
    v2 = load16u(arg0 + 110)
    v3 = load32(9561692)
    while True:  # block $label2
        if arg1:
            while True:  # block $label0
                v2 = (v3 + (v2 * 286704))
                arg1 = load32((((v3 + (v2 * 286704)) + (load32(38528) << 2)) + 284636))
                if (load32((((v3 + (v2 * 286704)) + (load32(38528) << 2)) + 284636)) == 0):
                    break
                v3 = load32(arg1 + 8)
                if (load32(arg1 + 8) == 0):
                    break
                v4 = load32(arg1)
                arg1 = 0
                while True:  # $label1
                    v5 = load32((v4 + (arg1 << 2)))
                    if (load32((v4 + (arg1 << 2))) == 0):
                        arg1 = (arg1 + 1)
                        if (v3 != (arg1 + 1)):
                            continue
                        break
                    break
                arg1 = load32(9671128)
                store8(arg0 + 129, 10)
                return 1
                break
            arg1 = load32(((v2 + (load32(((load32(v2 + 283960) << 2) + 9687176)) << 2)) + 284636))
            if (load32(((v2 + (load32(((load32(v2 + 283960) << 2) + 9687176)) << 2)) + 284636)) == 0):
                break
            v2 = load32(arg1 + 8)
            if (load32(arg1 + 8) == 0):
                break
            v3 = load32(arg1)
            arg1 = 0
            while True:  # block $label3
                while True:  # $label4
                    v4 = load32((v3 + (arg1 << 2)))
                    if load32((v3 + (arg1 << 2))):
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v2):
                        continue
                    break
                return 0
                break
            arg1 = load32(9671128)
            store8(arg0 + 129, 10)
            return 1
        v7 = load32(38500)
        v4 = ((load32(38500) * 404) + 9568096)
        arg1 = (v3 + (v2 * 286704))
        if (load32(((load32(38500) * 404) + 9568096) + 68) > load32((v3 + (v2 * 286704)) + 283848)):
            break
        if (load32(v4 + 72) > load32((arg1 + 283852))):
            break
        v4 = ((v7 * 404) + 9568096)
        v2 = (v3 + (v2 * 286704))
        if (load32(((v7 * 404) + 9568096) + 76) > load32(((v3 + (v2 * 286704)) + 283856))):
            break
        if (load32(v4 + 80) > load32((v2 + 283860))):
            break
        v16 = load32(arg1 + 283876)
        v17 = load32(arg1 + 283872)
        store8(arg0 + 129, 3)
        v6 = load32(9142440)
        v8 = (load32(9142440) + 2)
        v9 = ((v7 * 404) + 9568096)
        v18 = load32(9671128)
        v11 = load32(9142840)
        arg1 = 0
        while True:  # $label12
            while True:  # block $label5
                v12 = arg1
                arg1 = (arg1 << 2)
                v3 = (load32((((arg1 << 2) | 4) + 8611904)) + v16)
                if (u(v6) <= u((load32((((arg1 << 2) | 4) + 8611904)) + v16))):
                    break
                v4 = (load32((arg1 + 8611904)) + v17)
                if (u(v6) <= u((load32((arg1 + 8611904)) + v17))):
                    break
                if ((v3 | v4) < 0):
                    break
                while True:  # block $label6
                    v10 = load32(v9 + 216)
                    if (load32(v9 + 216) <= 0):
                        break
                    v13 = (load32(v9 + 220) + v3)
                    if ((load32(v9 + 220) + v3) <= v3):
                        break
                    v19 = (v4 + v10)
                    v14 = load32(v9 + 372)
                    v2 = v4
                    while True:  # $label11
                        v5 = (v2 + 1)
                        v15 = (v2 - v4)
                        arg1 = v3
                        while True:  # block $label9
                            if (u(v2) < u(v6)):
                                while True:  # $label8
                                    while True:  # block $label7
                                        if (load8u((v14 + (((arg1 - v3) * v10) + v15))) == 0):
                                            arg1 = (arg1 + 1)
                                            break
                                        if (u(arg1) >= u(v6)):
                                            break
                                        if ((arg1 | v2) < 0):
                                            break
                                        arg1 = (arg1 + 1)
                                        if load32((v11 + ((((arg1 + 1) * v8) + v5) << 2))):
                                            break
                                        if (load32(((load8u((v18 + (load32((v11 + ((((arg1 + v8) * v8) + v5) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1):
                                            break
                                        break
                                    if (arg1 != v13):
                                        continue
                                    break
                                    break
                                raise RuntimeError('unreachable')
                            while True:  # $label10
                                if load8u((v14 + (((arg1 - v3) * v10) + v15))):
                                    break
                                arg1 = (arg1 + 1)
                                if ((arg1 + 1) != v13):
                                    continue
                                break
                            break
                        v2 = v5
                        if (v5 < v19):
                            continue
                        break
                    break
                func261(v7, v4, v3, arg0)
                return 1
                break
            arg1 = (v12 + 2)
            if (u(v12) < u(3358)):
                continue
            break
        break
    return 0

# ------------------------------------------------------------
# $func144
# ------------------------------------------------------------
def func144(arg0, arg1, arg2):
    while True:  # block $label0
        v5 = (load32(9671128) + (arg1 * 132))
        arg0 = ((arg0 + ((load32(38428) if load16u(v5 + 120) else load8u((load32(9671128) + (arg1 * 132)) + 122)) << 2)) + 284636)
        v4 = load32(((arg0 + ((load32(38428) if load16u(v5 + 120) else load8u((load32(9671128) + (arg1 * 132)) + 122)) << 2)) + 284636))
        if (load32(((arg0 + ((load32(38428) if load16u(v5 + 120) else load8u((load32(9671128) + (arg1 * 132)) + 122)) << 2)) + 284636)) == 0):
            v4 = func26(16)
            store32(func26(16) + 4, 55)
            store32(v4, func26(220))
            store64(v4 + 8, 665719930880)
            store32(arg0, v4)
            v7 = (v4 + 8)
            break
        v7 = (v4 + 8)
        v3 = load32(v4 + 8)
        v6 = load32(v4 + 4)
        if (load32(v4 + 8) != load32(v4 + 4)):
            break
        while True:  # block $label1
            if (v6 == 0):
                v3 = 0
                break
            v5 = load32(v4)
            arg0 = 0
            v3 = 0
            while True:  # $label2
                v8 = load32((v5 + (arg0 << 2)))
                if load32((v5 + (arg0 << 2))):
                    store32((v5 + (v3 << 2)), v8)
                    v6 = load32(v4 + 8)
                    v3 = (v3 + 1)
                arg0 = (arg0 + 1)
                if (u((arg0 + 1)) < u(v6)):
                    continue
                break
            break
        store32(v4 + 8, v3)
        break
    arg0 = load32(v4 + 4)
    while True:  # block $label4
        while True:  # block $label5
            if arg2:
                while True:  # block $label3
                    if (arg0 != v3):
                        v6 = load32(v4)
                        break
                    arg2 = (load32(v4 + 12) + v3)
                    store32(v4 + 4, (load32(v4 + 12) + v3))
                    arg0 = load32(v4)
                    v6 = func26((-1 if (u(arg2) > u(1073741823)) else (arg2 << 2)))
                    if v3:
                        # TODO: memory.copy []
                    if arg0:
                        v3 = load32(v7)
                    store32(v4, v6)
                    break
                store32(v7, (v3 + 1))
                store32((v6 + (v3 << 2)), -1)
                v5 = load32(v7)
                if (load32(v7) == 0):
                    break
                arg0 = 0
                while True:  # $label9
                    v4 = (v6 + (arg0 << 2))
                    if (u(arg1) < u(load32((v6 + (arg0 << 2))))):
                        v3 = (v5 - 1)
                        if (u((v5 - 1)) <= u(arg0)):
                            break
                        v8 = ((v5 - arg0) - 2)
                        while True:  # block $label6
                            v9 = ((v3 - arg0) & 3)
                            if (((v3 - arg0) & 3) == 0):
                                arg2 = v5
                                break
                            v7 = 0
                            while True:  # $label7
                                arg2 = v3
                                store32((v6 + (v3 << 2)), load32((((v5 << 2) + v6) - 8)))
                                v3 = (v3 - 1)
                                v5 = arg2
                                v7 = (v7 + 1)
                                if ((v7 + 1) != v9):
                                    continue
                                break
                            break
                        if (u(v8) < u(3)):
                            break
                        while True:  # $label8
                            v5 = (v6 + (v3 << 2))
                            store32((v6 + (v3 << 2)), load32((((arg2 << 2) + v6) - 8)))
                            arg2 = (v5 - 8)
                            store32((v5 - 4), load32((v5 - 8)))
                            arg2 = (v3 - 3)
                            v5 = (v6 + ((v3 - 3) << 2))
                            store32(arg2, load32((v6 + ((v3 - 3) << 2))))
                            v3 = (v3 - 4)
                            store32(v5, load32((v6 + ((v3 - 4) << 2))))
                            if (u(arg0) < u(v3)):
                                continue
                            break
                        break
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v5):
                        continue
                    break
                break
            while True:  # block $label10
                if (arg0 != v3):
                    arg0 = load32(v4)
                    break
                arg0 = (load32(v4 + 12) + v3)
                store32(v4 + 4, (load32(v4 + 12) + v3))
                arg2 = load32(v4)
                arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                if v3:
                    # TODO: memory.copy []
                if arg2:
                    v3 = load32(v7)
                store32(v4, arg0)
                break
            store32(v7, (v3 + 1))
            v4 = (arg0 + (v3 << 2))
            break
        store32(v4, arg1)
        break

# ------------------------------------------------------------
# $func145
# ------------------------------------------------------------
def func145(arg0, arg1):
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label11
        while True:  # block $label12
            while True:  # block $label2
                while True:  # block $label10
                    while True:  # block $label9
                        while True:  # block $label8
                            while True:  # block $label7
                                while True:  # block $label3
                                    while True:  # block $label1
                                        while True:  # block $label6
                                            while True:  # block $label5
                                                while True:  # block $label0
                                                    while True:  # block $label4
                                                        # br_table[arg0]
                                                        break
                                                        break
                                                    if load32(9216064):
                                                        break
                                                    break
                                                    break
                                                if load32(9216064):
                                                    break
                                                break
                                                break
                                            if load32(9216064):
                                                break
                                            break
                                            break
                                        if (load32(9216064) == 0):
                                            break
                                        break
                                        break
                                    if load32(9216064):
                                        break
                                    break
                                    break
                                if load32(9216064):
                                    break
                                break
                                break
                            if load32(9216064):
                                break
                            break
                            break
                        if load32(9216064):
                            break
                        break
                        break
                    if load32(9216064):
                        break
                    break
                    break
                if load32(9216064):
                    break
                break
                break
            if load32(9216064):
                break
            break
        arg0 = 2
        store32(4, 2)
        store32(v2, arg0)
        store32(v2 + 4, arg1)
        break
    G.global0 = (v2 + 16)
    return v2

# ------------------------------------------------------------
# $func146
# ------------------------------------------------------------
def func146(arg0, arg1):
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label0
        v2 = load32(9671128)
        v4 = (arg0 * 132)
        v5 = (load32(9671128) + (arg0 * 132))
        if (load8u((load32(9671128) + (arg0 * 132)) + 125) == 3):
            break
        if (load8u(v5 + 128) == 0):
            break
        arg0 = (v2 + (arg0 * 132))
        store8((v2 + (arg0 * 132)) + 127, 0)
        while True:  # block $label1
            v2 = load32(arg0 + 40)
            if (load32(arg0 + 40) == 0):
                break
            if load8u(9142916):
                store32(v3 + 20, v2)
                store32(v3 + 16, 0)
                a_b()
                break
            arg0 = load16u(arg0 + 110)
            store32(v3 + 4, v2)
            store32(v3, (arg0 + 16))
            a_b()
            break
        store8(v5 + 128, 0)
        v2 = load32(9671128)
        break
    arg0 = (v2 + v4)
    v2 = load16u(arg0 + 116)
    v5 = load16u(arg0 + 118)
    v4 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 96)
    v4 = (load32(((load8u(arg0 + 122) * 404) + 9568096) + 96) - (v4 % 25))
    G.global0 = (v3 + 32)

# ------------------------------------------------------------
# $func148
# ------------------------------------------------------------
def func148(arg0, arg1, arg2):
    v4 = load32(9671128)
    v5 = (load32(9671128) + (arg0 * 132))
    v3 = load32(arg1)
    if (u(load32(arg1)) <= u(2147483646)):
        store32(v5 + 52, v3)
    v3 = load32(arg1 + 4)
    if (u(load32(arg1 + 4)) <= u(2147483646)):
        store32((v4 + (arg0 * 132)) + 60, v3)
    while True:  # block $label0
        v3 = load32(arg1 + 8)
        if (u(load32(arg1 + 8)) > u(2147483646)):
            break
        v7 = (v4 + (arg0 * 132))
        store32((v4 + (arg0 * 132)) + 64, v3)
        if (u(load32(arg1 + 8)) > u(2147483646)):
            break
        store32(v7 + 68, load32(arg1 + 12))
        break
    v7 = load32(v5 + 76)
    v3 = load32(v5 + 76)
    while True:  # block $label1
        v6 = load32(arg1 + 16)
        if (u(load32(arg1 + 16)) > u(2147483646)):
            break
        store32((v4 + (arg0 * 132)) + 72, v6)
        if (u(load32(arg1 + 16)) > u(2147483646)):
            break
        v3 = load32(arg1 + 20)
        store32(v5 + 76, load32(arg1 + 20))
        break
    arg1 = load32(arg1 + 24)
    if (u(load32(arg1 + 24)) <= u(2147483646)):
        store32((v4 + (arg0 * 132)) + 84, arg1)
    v6 = ((load8u((v4 + (arg0 * 132)) + 122) * 404) + 9568096)
    arg1 = load32(((load8u((v4 + (arg0 * 132)) + 122) * 404) + 9568096) + 264)
    while True:  # block $label2
        if (load32(v6 + 92) == 0):
            if (arg1 == 2):
                break
            store32((v4 + (arg0 * 132)) + 52, 0)
        if (arg1 != 1):
            break
        v3 = 0
        arg1 = (v4 + (arg0 * 132))
        store32((v4 + (arg0 * 132)) + 72, 0)
        store32(arg1 + 60, 0)
        store32(v5 + 76, 0)
        store32(arg1 + 84, 0)
        break
    v6 = (v4 + (arg0 * 132))
    arg1 = load32((v4 + (arg0 * 132)) + 64)
    if (load32((v4 + (arg0 * 132)) + 64) == 0):
        store32((v6 - -64), -1)
        arg1 = -1
    if arg2:
        arg2 = (v4 + (arg0 * 132))
        store32((v4 + (arg0 * 132)) + 68, arg1)
        v3 = load32(arg2 + 72)
        store32(v5 + 76, load32(arg2 + 72))
    while True:  # block $label3
        if (v3 == 0):
            break
        if v7:
            break
        break

# ------------------------------------------------------------
# $func149
# ------------------------------------------------------------
def func149(arg0, arg1, arg2):
    v3 = 100
    while True:  # block $label2
        while True:  # block $label3
            while True:  # block $label0
                while True:  # $label1
                    if v3:
                        if arg1:
                            if load32(arg1):
                                break
                        v3 = (v3 - 1)
                        if (load32(arg0) == arg2):
                            continue
                        break
                    break
                if arg1:
                    break
                break
                break
            # TODO: i32.atomic.rmw.add []
            break
        v5 = 0
        v3 = G.global5
        while True:  # block $label4
            if (load32(arg0) != arg2):
                break
            v6 = float((1 if v3 else 100))
            v4 = G.global3
            while True:  # $label8
                while True:  # block $label7
                    while True:  # block $label5
                        if (v3 == 0):
                            if (load8u(v4 + 41) != 1):
                                break
                        while True:  # $label6
                            if load32(v4 + 36):
                                break
                            if (func131(arg0, arg2, v6) == -73):
                                continue
                            break
                        break
                        break
                    break
                if (load32(arg0) == arg2):
                    continue
                break
            break
        if v5:
            break
        # TODO: i32.atomic.rmw.sub []
        break
    return arg1

# ------------------------------------------------------------
# $func152
# ------------------------------------------------------------
def func152():
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        if load8u(9142917):
            break
        if (load32(9568048) == 0):
            break
        v1 = load32(9140308)
        v3 = load32(9568052)
        v0 = (load32(59156) << 2)
        v2 = (load32(9568052) % (load32(59156) << 2))
        if (load32(9568052) % (load32(59156) << 2)):
            v3 = ((v3 - v2) + v0)
            store32(9568052, ((v3 - v2) + v0))
        store32(9140308, (((v3 & 0xFFFFFFFF) >> 2) + v1))
        func231(v4)
        store32(v4 + 12, 1)
        v0 = func26(16)
        v2 = load32(9568048)
        store32(v0 + 4, v1)
        store32(v0, v2)
        store32(v0 + 8, load32(9568052))
        store32(v0 + 12, func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2))))
        while True:  # block $label1
            if (v2 == 0):
                break
            v3 = 0
            if (u(v2) >= u(4)):
                v6 = (v2 & -4)
                while True:  # $label2
                    v1 = (v3 << 2)
                    store32(((v3 << 2) + load32(v0 + 12)), load32((v1 + 9563952)))
                    v5 = (v1 | 4)
                    store32(((v1 | 4) + load32(v0 + 12)), load32((v5 + 9563952)))
                    v5 = (v1 | 8)
                    store32(((v1 | 8) + load32(v0 + 12)), load32((v5 + 9563952)))
                    v1 = (v1 | 12)
                    store32(((v1 | 12) + load32(v0 + 12)), load32((v1 + 9563952)))
                    v3 = (v3 + 4)
                    v7 = (v7 + 4)
                    if ((v7 + 4) != v6):
                        continue
                    break
            v2 = (v2 & 3)
            if ((v2 & 3) == 0):
                break
            while True:  # $label3
                v1 = (v3 << 2)
                store32(((v3 << 2) + load32(v0 + 12)), load32((v1 + 9563952)))
                v3 = (v3 + 1)
                v8 = (v8 + 1)
                if ((v8 + 1) != v2):
                    continue
                break
            break
        func186((v4 + 44), v4, 65, v0)
        store32(9568052, 0)
        store32(9568048, 0)
        break
    G.global0 = (v4 + 48)

# ------------------------------------------------------------
# $func153
# ------------------------------------------------------------
def func153(arg0, arg1, arg2, arg3, arg4):
    v17 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v25 = (arg3 + 120)
    v12 = (arg3 + 24)
    while True:  # block $label16
        while True:  # block $label15
            while True:  # block $label2
                while True:  # block $label48
                    while True:  # block $label50
                        while True:  # block $label49
                            while True:  # block $label47
                                while True:  # block $label46
                                    while True:  # block $label14
                                        while True:  # block $label11
                                            while True:  # block $label44
                                                while True:  # block $label12
                                                    while True:  # block $label1
                                                        while True:  # block $label0
                                                            if (arg2 == 0):
                                                                break
                                                            while True:  # $label10
                                                                if (func39(v12, 1) == 0):
                                                                    break
                                                                v5 = load32(arg3 + 192)
                                                                v10 = func39(v12, 2)
                                                                v7 = load32(arg3 + 276)
                                                                v13 = (1 << v10)
                                                                if (load32(arg3 + 276) & (1 << v10)):
                                                                    break
                                                                store32(arg3 + 276, (v7 | v13))
                                                                v5 = (arg3 + (v5 * 20))
                                                                v18 = ((arg3 + (v5 * 20)) + 212)
                                                                store32(((arg3 + (v5 * 20)) + 212), 0)
                                                                store32(v5 + 208, arg1)
                                                                store32(v5 + 204, arg0)
                                                                store32(v5 + 196, v10)
                                                                v7 = load32(arg3 + 192)
                                                                store32(arg3 + 192, (load32(arg3 + 192) + 1))
                                                                if (v7 >= 4):
                                                                    break
                                                                v7 = 1
                                                                while True:  # block $label4
                                                                    while True:  # block $label3
                                                                        while True:  # block $label6
                                                                            while True:  # block $label5
                                                                                # br_table[v10]
                                                                                break
                                                                                break
                                                                            while True:  # block $label7
                                                                                arg0 = (func39(v12, 8) + 1)
                                                                                if ((func39(v12, 8) + 1) > 16):
                                                                                    break
                                                                                if (arg0 > 4):
                                                                                    break
                                                                                break
                                                                            v7 = (2 if (arg0 > 2) else 3)
                                                                            v11 = load32(v5 + 204)
                                                                            store32(v5 + 200, v7)
                                                                            if (func153(arg0, 1, 0, arg3, v18) == 0):
                                                                                break
                                                                            v6 = ((8 & 0xFFFFFFFF) >> load32(v5 + 200))
                                                                            v5 = func58(i64((1 << ((8 & 0xFFFFFFFF) >> load32(v5 + 200)))), 4)
                                                                            if func58(i64((1 << ((8 & 0xFFFFFFFF) >> load32(v5 + 200)))), 4):
                                                                                v15 = load32(v18)
                                                                                store32(v5, load32(load32(v18)))
                                                                                v9 = 4
                                                                                while True:  # block $label8
                                                                                    if (arg0 < 2):
                                                                                        break
                                                                                    arg0 = (arg0 << 2)
                                                                                    v9 = (5 if (arg0 <= 5) else (arg0 << 2))
                                                                                    v8 = ((5 if (arg0 <= 5) else (arg0 << 2)) & 1)
                                                                                    v10 = 4
                                                                                    if (arg0 >= 6):
                                                                                        v14 = ((v9 & 2147483644) - 6)
                                                                                        v13 = 0
                                                                                        while True:  # $label9
                                                                                            arg0 = (v5 + v10)
                                                                                            store8((v5 + v10), (load8u((arg0 - 4)) + load8u((v10 + v15))))
                                                                                            v21 = (v10 | 1)
                                                                                            store8((v5 + (v10 | 1)), (load8u((arg0 - 3)) + load8u((v15 + v21))))
                                                                                            v10 = (v10 + 2)
                                                                                            arg0 = (v13 == v14)
                                                                                            v13 = (v13 + 2)
                                                                                            if (arg0 == 0):
                                                                                                continue
                                                                                            break
                                                                                    if (v8 == 0):
                                                                                        break
                                                                                    arg0 = (v5 + v10)
                                                                                    store8((v5 + v10), (load8u((arg0 - 4)) + load8u((v10 + v15))))
                                                                                    break
                                                                                arg0 = (4 << v6)
                                                                                if (u(v9) < u((4 << v6))):
                                                                                    # TODO: memory.fill []
                                                                                arg0 = ((((v11 + (1 << v7)) - 1) & 0xFFFFFFFF) >> v7)
                                                                                store32(v18, v5)
                                                                                continue
                                                                            v13 = 1
                                                                            v7 = load32(arg3)
                                                                            # br_table[load32(arg3)]
                                                                            break
                                                                            break
                                                                        a_c()
                                                                        raise RuntimeError('unreachable')
                                                                        break
                                                                    v7 = (func39(v12, 3) + 2)
                                                                    store32(v5 + 200, (func39(v12, 3) + 2))
                                                                    v10 = ((-1 << v7) ^ -1)
                                                                    v7 = func153((((((-1 << v7) ^ -1) + load32(v5 + 204)) & 0xFFFFFFFF) >> v7), (((load32(v5 + 208) + v10) & 0xFFFFFFFF) >> v7), 0, arg3, v18)
                                                                    break
                                                                if v7:
                                                                    continue
                                                                break
                                                            break
                                                            break
                                                        v18 = 0
                                                        while True:  # block $label13
                                                            if (func39(v12, 1) == 0):
                                                                break
                                                            v18 = func39(v12, 4)
                                                            if (u((func39(v12, 4) - 1)) < u(11)):
                                                                break
                                                            v13 = 3
                                                            v10 = 0
                                                            # br_table[load32(arg3)]
                                                            break
                                                            break
                                                        store32(v17 + 12, 0)
                                                        store32(v17 + 8, 0)
                                                        v15 = (arg3 + 172)
                                                        if load32((arg3 + 172)):
                                                            break
                                                        if load32(arg3 + 188):
                                                            break
                                                        v10 = 1
                                                        while True:  # block $label18
                                                            while True:  # block $label17
                                                                if (arg2 == 0):
                                                                    v13 = 0
                                                                    v7 = 1
                                                                    break
                                                                v13 = 0
                                                                v7 = 1
                                                                if (func39(v12, 1) == 0):
                                                                    break
                                                                v7 = 0
                                                                v5 = (func39(v12, 3) + 2)
                                                                v12 = (1 << (func39(v12, 3) + 2))
                                                                v9 = ((((arg0 + (1 << (func39(v12, 3) + 2))) - 1) & 0xFFFFFFFF) >> v5)
                                                                v12 = ((((arg1 + v12) - 1) & 0xFFFFFFFF) >> v5)
                                                                if (func153(((((arg0 + (1 << (func39(v12, 3) + 2))) - 1) & 0xFFFFFFFF) >> v5), ((((arg1 + v12) - 1) & 0xFFFFFFFF) >> v5), 0, arg3, (v17 + 12)) == 0):
                                                                    break
                                                                store32(arg3 + 152, v5)
                                                                while True:  # block $label19
                                                                    v5 = (v9 * v12)
                                                                    if ((v9 * v12) <= 0):
                                                                        break
                                                                    v7 = load32(v17 + 12)
                                                                    if (v5 != 1):
                                                                        v6 = (v5 & -2)
                                                                        v12 = 0
                                                                        while True:  # $label20
                                                                            v11 = (v13 << 2)
                                                                            v9 = (v7 + (v13 << 2))
                                                                            v9 = load16u(v9 + 1)
                                                                            store32((v7 + (v13 << 2)), load16u(v9 + 1))
                                                                            v11 = (v7 + (v11 | 4))
                                                                            v11 = load16u(v11 + 1)
                                                                            store32((v7 + (v11 | 4)), load16u(v11 + 1))
                                                                            v10 = (v10 if (v9 < v10) else (v9 + 1))
                                                                            v10 = ((v10 if (v9 < v10) else (v9 + 1)) if (v10 > v11) else (v11 + 1))
                                                                            v13 = (v13 + 2)
                                                                            v12 = (v12 + 2)
                                                                            if ((v12 + 2) != v6):
                                                                                continue
                                                                            break
                                                                    if ((v5 & 1) == 0):
                                                                        break
                                                                    v7 = (v7 + (v13 << 2))
                                                                    v7 = load16u(v7 + 1)
                                                                    store32((v7 + (v13 << 2)), load16u(v7 + 1))
                                                                    v10 = (v10 if (v7 < v10) else (v7 + 1))
                                                                    break
                                                                while True:  # block $label21
                                                                    if (v10 > 1000):
                                                                        break
                                                                    v13 = 0
                                                                    if (v10 > (arg0 * arg1)):
                                                                        break
                                                                    v7 = v10
                                                                    break
                                                                    break
                                                                v13 = func58(i64(v10), 4)
                                                                if (func58(i64(v10), 4) == 0):
                                                                    v7 = 0
                                                                    v13 = 0
                                                                    while True:  # block $label22
                                                                        # br_table[load32(arg3)]
                                                                        break
                                                                        break
                                                                    store32(arg3, 1)
                                                                    break
                                                                # TODO: memory.fill []
                                                                if (v5 <= 0):
                                                                    v7 = 0
                                                                    break
                                                                v6 = (v5 & 1)
                                                                v11 = load32(v17 + 12)
                                                                while True:  # block $label23
                                                                    if (v5 == 1):
                                                                        v7 = 0
                                                                        v5 = 0
                                                                        break
                                                                    v8 = (v5 & -2)
                                                                    v7 = 0
                                                                    v5 = 0
                                                                    v9 = 0
                                                                    while True:  # $label24
                                                                        v14 = (v7 << 2)
                                                                        v21 = (v11 + (v7 << 2))
                                                                        v24 = (v13 + (load32((v11 + (v7 << 2))) << 2))
                                                                        v12 = load32((v13 + (load32((v11 + (v7 << 2))) << 2)))
                                                                        if (load32((v13 + (load32((v11 + (v7 << 2))) << 2))) == -1):
                                                                            store32(v24, v5)
                                                                            v12 = v5
                                                                            v5 = (v5 + 1)
                                                                        store32(v21, v12)
                                                                        v14 = (v11 + (v14 | 4))
                                                                        v21 = (v13 + (load32((v11 + (v14 | 4))) << 2))
                                                                        v12 = load32((v13 + (load32((v11 + (v14 | 4))) << 2)))
                                                                        if (load32((v13 + (load32((v11 + (v14 | 4))) << 2))) == -1):
                                                                            store32(v21, v5)
                                                                            v12 = v5
                                                                            v5 = (v5 + 1)
                                                                        store32(v14, v12)
                                                                        v7 = (v7 + 2)
                                                                        v9 = (v9 + 2)
                                                                        if ((v9 + 2) != v8):
                                                                            continue
                                                                        break
                                                                    break
                                                                if (v6 == 0):
                                                                    v7 = v5
                                                                    break
                                                                v9 = (v11 + (v7 << 2))
                                                                v7 = (v13 + (load32((v11 + (v7 << 2))) << 2))
                                                                v12 = load32((v13 + (load32((v11 + (v7 << 2))) << 2)))
                                                                if (load32((v13 + (load32((v11 + (v7 << 2))) << 2))) != -1):
                                                                else:
                                                                    store32(v7, v5)
                                                                    v12 = v5
                                                                v7 = (v5 + 1)
                                                                store32(v9, v12)
                                                                break
                                                            if load32(arg3 + 48):
                                                                v7 = 0
                                                                break
                                                            while True:  # block $label42
                                                                v9 = 0
                                                                while True:  # block $label38
                                                                    while True:  # block $label25
                                                                        if (v7 > v10):
                                                                            break
                                                                        if ((v13 == 0) & (v7 != v10)):
                                                                            break
                                                                        v12 = load16u(((v18 << 1) + 13776))
                                                                        v11 = (1 << v18)
                                                                        v9 = func134(i64((280 if (v18 <= 0) else ((1 << v18) + 280))), 4)
                                                                        v5 = func58(i64(v7), 548)
                                                                        while True:  # block $label26
                                                                            if (v7 < 65537):
                                                                                break
                                                                            if (v5 == 0):
                                                                                break
                                                                            a_c()
                                                                            raise RuntimeError('unreachable')
                                                                            break
                                                                        store32(v17 + 8, v5)
                                                                        while True:  # block $label27
                                                                            if (v5 == 0):
                                                                                break
                                                                            if (v9 == 0):
                                                                                break
                                                                            if (func452((v7 * v12), v15) == 0):
                                                                                break
                                                                            while True:  # block $label39
                                                                                if (v10 > 0):
                                                                                    v21 = (280 if (v18 <= 0) else (v11 + 280))
                                                                                    v5 = ((280 if (v18 <= 0) else (v11 + 280)) - 1)
                                                                                    v29 = (((280 if (v18 <= 0) else (v11 + 280)) - 1) & -4)
                                                                                    v24 = (v5 & 3)
                                                                                    v30 = (u((v21 - 2)) < u(3))
                                                                                    v12 = 0
                                                                                    while True:  # $label41
                                                                                        v5 = v12
                                                                                        while True:  # block $label29
                                                                                            while True:  # block $label28
                                                                                                if (v13 == 0):
                                                                                                    break
                                                                                                v5 = load32((v13 + (v12 << 2)))
                                                                                                if (load32((v13 + (v12 << 2))) != -1):
                                                                                                    break
                                                                                                if (func83(v21, arg3, v9, 0) == 0):
                                                                                                    break
                                                                                                if (func83(256, arg3, v9, 0) == 0):
                                                                                                    break
                                                                                                if (func83(256, arg3, v9, 0) == 0):
                                                                                                    break
                                                                                                if (func83(256, arg3, v9, 0) == 0):
                                                                                                    break
                                                                                                if func83(40, arg3, v9, 0):
                                                                                                    break
                                                                                                break
                                                                                                break
                                                                                            v11 = load32(v17 + 8)
                                                                                            v6 = func83(v21, arg3, v9, v15)
                                                                                            v11 = (v11 + (v5 * 548))
                                                                                            v5 = load32(load32(v15 + 16) + 4)
                                                                                            store32((v11 + (v5 * 548)), load32(load32(v15 + 16) + 4))
                                                                                            if (v6 == 0):
                                                                                                break
                                                                                            v19 = load8u(v5)
                                                                                            v5 = load32(v15 + 16)
                                                                                            store32(load32(v15 + 16) + 4, (load32(v5 + 4) + (v6 << 2)))
                                                                                            v14 = load32(v9)
                                                                                            while True:  # block $label30
                                                                                                if (v21 < 2):
                                                                                                    break
                                                                                                v8 = 0
                                                                                                v5 = 1
                                                                                                if (v30 == 0):
                                                                                                    while True:  # $label31
                                                                                                        v6 = (v9 + (v5 << 2))
                                                                                                        v22 = load32((v9 + (v5 << 2)) + 12)
                                                                                                        v16 = load32(v6 + 8)
                                                                                                        v20 = load32(v6 + 4)
                                                                                                        v6 = load32(v6)
                                                                                                        v6 = (load32(v6) if (v6 > v14) else v14)
                                                                                                        v6 = (load32(v6 + 4) if (v6 < v20) else (load32(v6) if (v6 > v14) else v14))
                                                                                                        v6 = (load32(v6 + 8) if (v6 < v16) else (load32(v6 + 4) if (v6 < v20) else (load32(v6) if (v6 > v14) else v14)))
                                                                                                        v14 = (load32((v9 + (v5 << 2)) + 12) if (v6 < v22) else (load32(v6 + 8) if (v6 < v16) else (load32(v6 + 4) if (v6 < v20) else (load32(v6) if (v6 > v14) else v14))))
                                                                                                        v5 = (v5 + 4)
                                                                                                        v8 = (v8 + 4)
                                                                                                        if ((v8 + 4) != v29):
                                                                                                            continue
                                                                                                        break
                                                                                                v6 = 0
                                                                                                if (v24 == 0):
                                                                                                    break
                                                                                                while True:  # $label32
                                                                                                    v8 = load32((v9 + (v5 << 2)))
                                                                                                    v14 = (load32((v9 + (v5 << 2))) if (v8 > v14) else v14)
                                                                                                    v5 = (v5 + 1)
                                                                                                    v6 = (v6 + 1)
                                                                                                    if ((v6 + 1) != v24):
                                                                                                        continue
                                                                                                    break
                                                                                                break
                                                                                            v5 = func83(256, arg3, v9, v15)
                                                                                            v6 = load32(load32(v15 + 16) + 4)
                                                                                            store32(v11 + 4, load32(load32(v15 + 16) + 4))
                                                                                            if (v5 == 0):
                                                                                                break
                                                                                            v22 = load8u(v6)
                                                                                            v6 = load32(v15 + 16)
                                                                                            store32(load32(v15 + 16) + 4, (load32(v6 + 4) + (v5 << 2)))
                                                                                            v6 = load32(v9)
                                                                                            v8 = 1
                                                                                            while True:  # $label33
                                                                                                v5 = (v9 + (v8 << 2))
                                                                                                v16 = load32((v9 + (v8 << 2)) + 16)
                                                                                                v20 = load32(v5 + 12)
                                                                                                v26 = load32(v5 + 8)
                                                                                                v23 = load32(v5 + 4)
                                                                                                v5 = load32(v5)
                                                                                                v5 = (load32(v5) if (v5 > v6) else v6)
                                                                                                v5 = (load32(v5 + 4) if (v5 < v23) else (load32(v5) if (v5 > v6) else v6))
                                                                                                v5 = (load32(v5 + 8) if (v5 < v26) else (load32(v5 + 4) if (v5 < v23) else (load32(v5) if (v5 > v6) else v6)))
                                                                                                v5 = (load32(v5 + 12) if (v5 < v20) else (load32(v5 + 8) if (v5 < v26) else (load32(v5 + 4) if (v5 < v23) else (load32(v5) if (v5 > v6) else v6))))
                                                                                                v6 = (load32((v9 + (v8 << 2)) + 16) if (v5 < v16) else (load32(v5 + 12) if (v5 < v20) else (load32(v5 + 8) if (v5 < v26) else (load32(v5 + 4) if (v5 < v23) else (load32(v5) if (v5 > v6) else v6)))))
                                                                                                v8 = (v8 + 5)
                                                                                                if ((v8 + 5) != 256):
                                                                                                    continue
                                                                                                break
                                                                                            v5 = func83(256, arg3, v9, v15)
                                                                                            v8 = load32(load32(v15 + 16) + 4)
                                                                                            store32(v11 + 8, load32(load32(v15 + 16) + 4))
                                                                                            if (v5 == 0):
                                                                                                break
                                                                                            v16 = 0
                                                                                            if (v22 == 0):
                                                                                                v16 = (load8u(v8) == 0)
                                                                                            v20 = (v6 + v14)
                                                                                            v26 = load8u(v8)
                                                                                            v6 = load32(v15 + 16)
                                                                                            store32(load32(v15 + 16) + 4, (load32(v6 + 4) + (v5 << 2)))
                                                                                            v6 = load32(v9)
                                                                                            v8 = 1
                                                                                            while True:  # $label34
                                                                                                v5 = (v9 + (v8 << 2))
                                                                                                v14 = load32((v9 + (v8 << 2)) + 16)
                                                                                                v23 = load32(v5 + 12)
                                                                                                v27 = load32(v5 + 8)
                                                                                                v28 = load32(v5 + 4)
                                                                                                v5 = load32(v5)
                                                                                                v5 = (load32(v5) if (v5 > v6) else v6)
                                                                                                v5 = (load32(v5 + 4) if (v5 < v28) else (load32(v5) if (v5 > v6) else v6))
                                                                                                v5 = (load32(v5 + 8) if (v5 < v27) else (load32(v5 + 4) if (v5 < v28) else (load32(v5) if (v5 > v6) else v6)))
                                                                                                v5 = (load32(v5 + 12) if (v5 < v23) else (load32(v5 + 8) if (v5 < v27) else (load32(v5 + 4) if (v5 < v28) else (load32(v5) if (v5 > v6) else v6))))
                                                                                                v6 = (load32((v9 + (v8 << 2)) + 16) if (v5 < v14) else (load32(v5 + 12) if (v5 < v23) else (load32(v5 + 8) if (v5 < v27) else (load32(v5 + 4) if (v5 < v28) else (load32(v5) if (v5 > v6) else v6)))))
                                                                                                v8 = (v8 + 5)
                                                                                                if ((v8 + 5) != 256):
                                                                                                    continue
                                                                                                break
                                                                                            v5 = func83(256, arg3, v9, v15)
                                                                                            v8 = load32(load32(v15 + 16) + 4)
                                                                                            store32(v11 + 12, load32(load32(v15 + 16) + 4))
                                                                                            if (v5 == 0):
                                                                                                break
                                                                                            if v16:
                                                                                            else:
                                                                                            v14 = (1 == 0)
                                                                                            v16 = (v6 + v20)
                                                                                            v20 = load8u(v8)
                                                                                            v6 = load32(v15 + 16)
                                                                                            store32(load32(v15 + 16) + 4, (load32(v6 + 4) + (v5 << 2)))
                                                                                            v6 = load32(v9)
                                                                                            v8 = 1
                                                                                            while True:  # $label35
                                                                                                v5 = (v9 + (v8 << 2))
                                                                                                v23 = load32((v9 + (v8 << 2)) + 16)
                                                                                                v27 = load32(v5 + 12)
                                                                                                v28 = load32(v5 + 8)
                                                                                                v31 = load32(v5 + 4)
                                                                                                v5 = load32(v5)
                                                                                                v5 = (load32(v5) if (v5 > v6) else v6)
                                                                                                v5 = (load32(v5 + 4) if (v5 < v31) else (load32(v5) if (v5 > v6) else v6))
                                                                                                v5 = (load32(v5 + 8) if (v5 < v28) else (load32(v5 + 4) if (v5 < v31) else (load32(v5) if (v5 > v6) else v6)))
                                                                                                v5 = (load32(v5 + 12) if (v5 < v27) else (load32(v5 + 8) if (v5 < v28) else (load32(v5 + 4) if (v5 < v31) else (load32(v5) if (v5 > v6) else v6))))
                                                                                                v6 = (load32((v9 + (v8 << 2)) + 16) if (v5 < v23) else (load32(v5 + 12) if (v5 < v27) else (load32(v5 + 8) if (v5 < v28) else (load32(v5 + 4) if (v5 < v31) else (load32(v5) if (v5 > v6) else v6)))))
                                                                                                v8 = (v8 + 5)
                                                                                                if ((v8 + 5) != 256):
                                                                                                    continue
                                                                                                break
                                                                                            v5 = func83(40, arg3, v9, v15)
                                                                                            v8 = load32(load32(v15 + 16) + 4)
                                                                                            store32(v11 + 16, load32(load32(v15 + 16) + 4))
                                                                                            if (v5 == 0):
                                                                                                break
                                                                                            v22 = (v20 + (v26 + (v19 + v22)))
                                                                                            v8 = load8u(v8)
                                                                                            v19 = load32(v15 + 16)
                                                                                            store32(load32(v15 + 16) + 4, (load32(v19 + 4) + (v5 << 2)))
                                                                                            store32(v11 + 28, 0)
                                                                                            store32(v11 + 20, v14)
                                                                                            while True:  # block $label36
                                                                                                if (v14 == 0):
                                                                                                    break
                                                                                                v5 = ((load16u(load32(v11 + 8) + 2) | (load16u(load32(v11 + 4) + 2) << 16)) | (load16u(load32(v11 + 12) + 2) << 24))
                                                                                                store32(v11 + 24, ((load16u(load32(v11 + 8) + 2) | (load16u(load32(v11 + 4) + 2) << 16)) | (load16u(load32(v11 + 12) + 2) << 24)))
                                                                                                if (v22 != (0 - v8)):
                                                                                                    break
                                                                                                v8 = load16u(load32(v11) + 2)
                                                                                                if (u(load16u(load32(v11) + 2)) > u(255)):
                                                                                                    break
                                                                                                store32(v11 + 28, 1)
                                                                                                store32(v11 + 24, ((v8 << 8) | v5))
                                                                                                store32(v11 + 32, 0)
                                                                                                break
                                                                                                break
                                                                                            v5 = (v6 + v16)
                                                                                            store32(v11 + 32, ((v6 + v16) < 6))
                                                                                            if (v5 > 5):
                                                                                                break
                                                                                            v22 = load32(v11)
                                                                                            v5 = 0
                                                                                            while True:  # $label40
                                                                                                v6 = (v11 + (v5 << 3))
                                                                                                v8 = load32((v22 + (v5 << 2)))
                                                                                                v14 = ((load32((v22 + (v5 << 2))) & 0xFFFFFFFF) >> 16)
                                                                                                while True:  # block $label37
                                                                                                    if (u(v8) >= u(16777216)):
                                                                                                        store32(v6 + 36, ((v8 & 255) | 256))
                                                                                                        store32(v6 + 40, v14)
                                                                                                        break
                                                                                                    v8 = (v8 & 255)
                                                                                                    store32(v6 + 36, (v8 & 255))
                                                                                                    v14 = (v14 << 8)
                                                                                                    store32(v6 + 40, (v14 << 8))
                                                                                                    if (u(v8) >= u(9)):
                                                                                                        break
                                                                                                    v16 = ((v5 & 0xFFFFFFFF) >> v8)
                                                                                                    v19 = (load32(v11 + 4) + (((v5 & 0xFFFFFFFF) >> v8) << 2))
                                                                                                    v20 = load16u((load32(v11 + 4) + (((v5 & 0xFFFFFFFF) >> v8) << 2)) + 2)
                                                                                                    v19 = load8u(v19)
                                                                                                    v8 = (v8 + load8u(v19))
                                                                                                    store32(v6 + 36, (v8 + load8u(v19)))
                                                                                                    v14 = ((v20 << 16) | v14)
                                                                                                    store32(v6 + 40, ((v20 << 16) | v14))
                                                                                                    if (u(v8) >= u(9)):
                                                                                                        break
                                                                                                    v16 = ((v16 & 0xFFFFFFFF) >> v19)
                                                                                                    v19 = (load32(v11 + 8) + (((v16 & 0xFFFFFFFF) >> v19) << 2))
                                                                                                    v20 = load16u((load32(v11 + 8) + (((v16 & 0xFFFFFFFF) >> v19) << 2)) + 2)
                                                                                                    v19 = load8u(v19)
                                                                                                    v8 = (v8 + load8u(v19))
                                                                                                    store32(v6 + 36, (v8 + load8u(v19)))
                                                                                                    v14 = (v14 | v20)
                                                                                                    store32(v6 + 40, (v14 | v20))
                                                                                                    if (u(v8) >= u(9)):
                                                                                                        break
                                                                                                    v16 = (load32(v11 + 12) + (((v16 & 0xFFFFFFFF) >> v19) << 2))
                                                                                                    v19 = load16u((load32(v11 + 12) + (((v16 & 0xFFFFFFFF) >> v19) << 2)) + 2)
                                                                                                    v8 = (v8 + load8u(v16))
                                                                                                    store32(v6 + 36, (v8 + load8u(v16)))
                                                                                                    store32(v6 + 40, ((v19 << 24) | v14))
                                                                                                    if (u(v8) >= u(9)):
                                                                                                        break
                                                                                                    break
                                                                                                v5 = (v5 + 1)
                                                                                                if ((v5 + 1) != 64):
                                                                                                    continue
                                                                                                break
                                                                                            break
                                                                                        v12 = (v12 + 1)
                                                                                        if ((v12 + 1) != v10):
                                                                                            continue
                                                                                        break
                                                                                break
                                                                                break
                                                                            break
                                                                            break
                                                                        while True:  # block $label43
                                                                            # br_table[load32(arg3)]
                                                                            break
                                                                            break
                                                                        store32(arg3, 1)
                                                                        break
                                                                    func116(v15)
                                                                    func151(load32(v17 + 8))
                                                                    store32(v17 + 8, 0)
                                                                    break
                                                                    break
                                                                a_c()
                                                                raise RuntimeError('unreachable')
                                                                break
                                                            if 4903:
                                                                break
                                                            v7 = load32(v17 + 8)
                                                            break
                                                        func116(v15)
                                                        func151(v7)
                                                        break
                                                    v7 = load32(arg3)
                                                    break
                                                v13 = 3
                                                v10 = 0
                                                # br_table[v7]
                                                break
                                                break
                                            v5 = load32(v17 + 12)
                                            store32(arg3 + 164, v7)
                                            store32(arg3 + 160, v5)
                                            store32(arg3 + 168, load32(v17 + 8))
                                            while True:  # block $label45
                                                if (v18 > 0):
                                                    store32(arg3 + 120, (1 << v18))
                                                    if func455((arg3 + 124), v18):
                                                        break
                                                    v13 = 1
                                                    v10 = 0
                                                    # br_table[load32(arg3)]
                                                    break
                                                store32(v25, 0)
                                                break
                                            store32(arg3 + 104, arg1)
                                            store32(arg3 + 100, arg0)
                                            v5 = load32(arg3 + 152)
                                            store32(arg3 + 148, (((-1 << load32(arg3 + 152)) ^ -1) if v5 else -1))
                                            store32(arg3 + 156, ((((arg0 + (1 << v5)) - 1) & 0xFFFFFFFF) >> v5))
                                            if arg2:
                                                break
                                            v10 = func58((i64(arg0) * i64(arg1)), 4)
                                            if (func58((i64(arg0) * i64(arg1)), 4) == 0):
                                                v13 = 1
                                                v10 = 0
                                                # br_table[load32(arg3)]
                                                break
                                            if (func275(arg3, v10, arg0, arg1, arg1, 0) == 0):
                                                break
                                            if load32(arg3 + 48):
                                                break
                                            if arg4:
                                                break
                                            a_c()
                                            raise RuntimeError('unreachable')
                                            break
                                        store32(arg3, v13)
                                        v10 = 0
                                        break
                                    func116((arg3 + 172))
                                    func151(load32(arg3 + 168))
                                    func136((arg3 + 124))
                                    func136((arg3 + 136))
                                    # TODO: memory.fill []
                                    break
                                    break
                                store32(arg3 + 4, 1)
                                if (arg4 == 0):
                                    break
                                store32(arg4, 0)
                                store32(arg3 + 112, 0)
                                break
                                break
                            store32(arg4, v10)
                            store32(arg3 + 112, 0)
                            func116(v15)
                            func151(load32(arg3 + 168))
                            func136((arg3 + 124))
                            func136((arg3 + 136))
                            # TODO: memory.fill []
                            break
                            break
                        store32(arg3 + 112, 0)
                        break
                    break
                arg0 = 1
                G.global0 = (v17 + 16)
                return arg0
                break
            a_c()
            raise RuntimeError('unreachable')
            break
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')
    return 3404

# ------------------------------------------------------------
# $func155
# ------------------------------------------------------------
def func155(arg0, arg1, arg2):
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v4 = load32(9561692)
    v6 = load16u(arg0 + 110)
    while True:  # block $label0
        if (load32(9147132) == 0):
            break
        if (load32(9671152) != load8u(arg1 + 122)):
            break
        v5 = load16u(arg1 + 110)
        if (v6 == load16u(arg1 + 110)):
            break
        if (v6 == 0):
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
    while True:  # block $label1
        if arg2:
            break
        while True:  # block $label2
            v4 = load32(((v4 + (v6 * 286704)) + 278560))
            if (load32(((v4 + (v6 * 286704)) + 278560)) == 0):
                arg2 = load16u(arg1 + 110)
                break
            arg2 = load16u(arg1 + 110)
            v4 = (v4 + ((load8u(arg0 + 122) + (load16u(arg1 + 110) * 255)) << 2))
            store32((v4 + ((load8u(arg0 + 122) + (load16u(arg1 + 110) * 255)) << 2)), (load32(v4) + 1))
            break
        arg2 = load32(((load32(9561692) + (arg2 * 286704)) + 278568))
        if (load32(((load32(9561692) + (arg2 * 286704)) + 278568)) == 0):
            break
        arg2 = (arg2 + ((load8u(arg1 + 122) + (load16u(arg0 + 110) * 255)) << 2))
        store32((arg2 + ((load8u(arg1 + 122) + (load16u(arg0 + 110) * 255)) << 2)), (load32(arg2) + 1))
        break
    store16(arg1 + 116, load32(arg0 + 28))
    G.global0 = (v3 + 32)

# ------------------------------------------------------------
# $func156
# ------------------------------------------------------------
def func156(arg0, arg1, param2):
    v2 = load8u(arg0 + 125)
    while True:  # block $label3
        while True:  # block $label4
            while True:  # block $label0
                while True:  # block $label2
                    while True:  # block $label1
                        v3 = ((load8u(arg0 + 122) * 404) + 9568096)
                        v4 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 264)
                        # br_table[load32(((load8u(arg0 + 122) * 404) + 9568096) + 264)]
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
                if (load32(arg0 + 52) == 0):
                    break
                break
                break
            if (load32(arg0 + 52) == 0):
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
        # call_indirect[arg1]
    store32(arg0 + 44, 0)

# ------------------------------------------------------------
# $func157
# ------------------------------------------------------------
def func157(arg0):
    while True:  # block $label0
        v2 = load8u(arg0 + 122)
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) != 1):
            break
        v3 = load32(arg0 + 20)
        if (load32(arg0 + 20) == 0):
            break
        if (load32(38540) == v2):
            break
        if (load32(38812) == v2):
            break
        if (load32(38888) == v2):
            break
        if load32(v3 + 8):
            v2 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
            v18 = ((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 283908)
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
                v1 = (u(arg0) > u(2147483646))
                v17 = ((load32((v20 + (v4 << 2))) - 2147483647) if (u(arg0) > u(2147483646)) else arg0)
                while True:  # block $label2
                    while True:  # block $label1
                        if (v4 == 0):
                            if (u(arg0) < u(2147483647)):
                                break
                            # br_table[v21]
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
                    v1 = load32(9142892)
                    if (u(load32(9142892)) < u(2)):
                        break
                    arg0 = 1
                    v6 = (v1 - 1)
                    v22 = ((v1 - 1) & 1)
                    v7 = (load32(v18) * v1)
                    v8 = load32(9561692)
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
                    if (v22 == 0):
                        break
                    if (load8u((v5 + (arg0 + v7))) == 0):
                        break
                    store8((v8 + (arg0 * 286704)) + 286701, 1)
                    break
                arg0 = ((v2 + (v17 << 2)) + 282828)
                store32(((v2 + (v17 << 2)) + 282828), (load32(arg0) - 1))
                v4 = (v4 + 1)
                if (u((v4 + 1)) < u(load32(v3 + 8))):
                    continue
                break
        store32(v3 + 8, 0)
        break

# ------------------------------------------------------------
# $func158
# ------------------------------------------------------------
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
                    if (u((v2 + 2)) < u(load32(load32(arg0 + 12) + 8))):
                        continue
                    break
            store32(v1 + 8, 0)
        while True:  # block $label1
            v1 = load32(arg0 + 24)
            if (load32(arg0 + 24) == 0):
                break
            v3 = load32(v1 + 4)
            if (load32(v1 + 4) == 0):
                break
            v1 = load32(v3 + 8)
            if (load32(v3 + 8) == 0):
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
                if (u((v2 + 2)) < u(v1)):
                    continue
                break
            break
        func38(load32(arg0 + 40))
        store32(arg0 + 40, 0)

# ------------------------------------------------------------
# $func159
# ------------------------------------------------------------
def func159(arg0):
    v3 = load32(arg0 + 28)
    v5 = load32(9671128)
    while True:  # block $label1
        while True:  # block $label0
            arg0 = load32(9215928)
            if (load32(9215928) == 0):
                break
            v1 = load32(arg0 + 8)
            if (load32(arg0 + 8) == 0):
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
        while True:  # block $label3
            arg0 = load32(9215932)
            if (load32(9215932) == 0):
                break
            v1 = load32(arg0 + 8)
            if (load32(arg0 + 8) == 0):
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
        while True:  # block $label5
            arg0 = load32(9215936)
            if (load32(9215936) == 0):
                break
            v1 = load32(arg0 + 8)
            if (load32(arg0 + 8) == 0):
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
        if (load32(9215940) == 0):
            break
        v1 = load32(arg0 + 8)
        if (load32(arg0 + 8) == 0):
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

# ------------------------------------------------------------
# $func160
# ------------------------------------------------------------
def func160(arg0, arg1, arg2):
    v3 = load8u(59181)
    v8 = load16u(arg0 + 114)
    v9 = load16u(arg0 + 112)
    while True:  # block $label1
        while True:  # block $label0
            if load8u(9147152):
                v4 = load8u(arg0 + 125)
                break
            v4 = load32(9142872)
            if (load32(9142872) == 0):
                break
            if (load8u((load32(9143012) + (load16u(arg0 + 110) + (load32(9142892) * v4)))) == 0):
                break
            v4 = load8u(arg0 + 125)
            if (load8u(arg0 + 125) == 3):
                break
            break
        v7 = ((load8u(arg0 + 122) * 404) + 9568096)
        v5 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 220)
        arg0 = ((v8 - (arg2 if v3 else 0)) + ((load32(((load8u(arg0 + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1))
        v3 = load32(v7 + 216)
        v8 = ((v9 - (arg1 if v3 else 0)) + ((load32(v7 + 216) & 0xFFFFFFFF) >> 1))
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label2
                    # br_table[(v4 - 4)]
                    break
                    break
                break
                break
            break
        v7 = load32(v7 + 200)
        while True:  # block $label5
            if (load32(load32(9142424) + 48) == 0):
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
                    while True:  # block $label6
                        v6 = (v3 << 2)
                        v9 = (load32((v5 + ((v3 << 2) | 4))) + arg0)
                        if (u(v4) <= u((load32((v5 + ((v3 << 2) | 4))) + arg0))):
                            break
                        v6 = (load32((v5 + v6)) + v8)
                        if (u(v4) <= u((load32((v5 + v6)) + v8))):
                            break
                        if ((v6 | v9) < 0):
                            break
                        v4 = load32(9142440)
                        break
                    v3 = (v3 + 2)
                    if (u((v3 + 2)) < u(v11)):
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
                    while True:  # block $label8
                        v6 = (v3 << 2)
                        v9 = (load32((v5 + ((v3 << 2) | 4))) + arg0)
                        if (u(v4) <= u((load32((v5 + ((v3 << 2) | 4))) + arg0))):
                            break
                        v6 = (load32((v5 + v6)) + v8)
                        if (u(v4) <= u((load32((v5 + v6)) + v8))):
                            break
                        if ((v6 | v9) < 0):
                            break
                        func258(v6, v9)
                        v4 = load32(9142440)
                        break
                    v3 = (v3 + 2)
                    if (u((v3 + 2)) < u(v10)):
                        continue
                    break
            if (load32(load32(9142424) + 48) == 1):
                break
            v3 = ((load32(9142836) + (v7 * 80)) + ((((1 - arg2) * 3) - arg1) << 2))
            v7 = load32(((load32(9142836) + (v7 * 80)) + ((((1 - arg2) * 3) - arg1) << 2)) + 48)
            if (load32(((load32(9142836) + (v7 * 80)) + ((((1 - arg2) * 3) - arg1) << 2)) + 48) == 0):
                break
            v5 = (arg0 + arg2)
            v8 = (arg1 + v8)
            arg0 = load32(v3 + 12)
            v4 = load32(9142440)
            v3 = 0
            while True:  # $label11
                while True:  # block $label10
                    arg2 = (v3 << 2)
                    arg1 = (v5 + load32((arg0 + ((v3 << 2) | 4))))
                    if (u(v4) <= u((v5 + load32((arg0 + ((v3 << 2) | 4)))))):
                        break
                    arg2 = (v8 + load32((arg0 + arg2)))
                    if (u(v4) <= u((v8 + load32((arg0 + arg2))))):
                        break
                    if ((arg1 | arg2) < 0):
                        break
                    v4 = load32(9142440)
                    break
                v3 = (v3 + 2)
                if (u((v3 + 2)) < u(v7)):
                    continue
                break
            break
        break
    return func129(arg2, arg1, 0)

# ------------------------------------------------------------
# $func161
# ------------------------------------------------------------
def func161(arg0, arg1, arg2):
    v8 = load32(9671128)
    v11 = (load32(9671128) + (load32(arg1) * 132))
    v9 = load8u((load32(9671128) + (load32(arg1) * 132)) + 122)
    v3 = load8u(arg0 + 122)
    v13 = 1
    while True:  # block $label0
        if (arg2 == 0):
            v12 = 1
            break
        v12 = 1
        while True:  # $label4
            while True:  # block $label1
                while True:  # block $label2
                    while True:  # block $label3
                        v5 = (v8 + (load32((arg1 + (v4 << 2))) * 132))
                        v6 = load8u((v8 + (load32((arg1 + (v4 << 2))) * 132)) + 122)
                        # br_table[(load8u((v8 + (load32((arg1 + (v4 << 2))) * 132)) + 122) + -64)]
                        break
                        break
                    if (v6 == 10):
                        break
                    break
                v13 = 0
                break
            if load32(((v6 * 404) + 9568096) + 264):
                v12 = 0
                v7 = (v7 | (load32(v5 + 52) == 0))
            v9 = (-1 if (v6 != v9) else v9)
            v4 = (v4 + 1)
            if ((v4 + 1) != arg2):
                continue
            break
        break
    v4 = load16u(v11 + 110)
    v6 = load8u(arg0 + 128)
    while True:  # block $label5
        v11 = load32(38768)
        if (v3 == load32(38768)):
            arg2 = 55
            if (v9 == load32(38712)):
                break
        arg2 = 35
        v8 = load32(((v3 * 404) + 9568096) + 264)
        if ((load32(((v3 * 404) + 9568096) + 264) == 2) & v12):
            break
        while True:  # block $label6
            v15 = load8u(9216060)
            if (((load8u(9216060) == 0) & v13) == 0):
                break
            if (v8 != 1):
                break
            v14 = load32(((v3 * 404) + 9568096) + 112)
            if (load32(((v3 * 404) + 9568096) + 112) == 0):
                break
            arg1 = load16u(arg0 + 110)
            while True:  # block $label9
                while True:  # block $label7
                    if (load32(38500) == v3):
                        break
                    v5 = (load32(9142892) * v4)
                    v10 = load32(9143004)
                    while True:  # block $label8
                        arg2 = load16u(arg0 + 120)
                        if load16u(arg0 + 120):
                        else:
                        if (load8u(((arg2 if load8u((v10 + (arg1 + v5))) else arg1) + (arg1 + v5))) == 0):
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
                    if (load32(((v3 * 404) + 9568096) + 188) != 55):
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
                if (u(v14) <= u(load32(arg0 + 84))):
                    break
                v5 = load8u(arg0 + 125)
                break
            arg2 = 54
            # br_table[(v5 - 4)]
            break
            break
        arg1 = load16u(arg0 + 110)
        while True:  # block $label13
            while True:  # block $label12
                while True:  # block $label10
                    if (load32(38500) == v3):
                        break
                    v5 = (load32(9142892) * v4)
                    v10 = load32(9143004)
                    arg2 = arg1
                    while True:  # block $label11
                        v14 = load16u(arg0 + 120)
                        if load16u(arg0 + 120):
                        else:
                        if (load8u(((v14 if load8u((v10 + (arg1 + v5))) else arg1) + (arg2 + v5))) == 0):
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
                    if (load32(((v3 * 404) + 9568096) + 188) != 55):
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
                # br_table[(load8u(arg0 + 125) - 4)]
                break
                break
            arg2 = 6
            if ((v7 & 1) == 0):
                break
            break
        while True:  # block $label14
            if (v13 == 0):
                break
            while True:  # block $label15
                if (load32(38528) != v3):
                    break
                if (load8u((load32(9143004) + ((load32(9142892) * arg1) + v4))) == 0):
                    break
                arg2 = 61
                if (load32((((load32(9561692) + (v4 * 286704)) + (load32(39188) << 2)) + 281808)) == 1):
                    break
                break
            arg2 = load8u(arg0 + 125)
            while True:  # block $label17
                while True:  # block $label16
                    if (v15 == 0):
                        if (arg2 == 10):
                            break
                        if (load32(((v3 * 404) + 9568096) + 188) == 55):
                            break
                        arg2 = 1
                        if (v3 == v11):
                            break
                        break
                    if (arg2 == 10):
                        break
                    if load32(((v3 * 404) + 9568096) + 188):
                        break
                    return 1
                    break
                arg2 = 1
                if (v3 != v11):
                    break
                break
            if (u(load32(arg0 + 64)) >= u(load32(arg0 + 68))):
                break
            arg2 = 4
            while True:  # block $label18
                # br_table[v8]
                break
                break
            if (load32(((v3 * 404) + 9568096) + 268) == 2):
                break
            break
        arg2 = 0
        if load8u(9147152):
        else:
            if (load8u((load32(9143008) + ((load32(9142892) * arg1) + v4))) == 0):
                break
            if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                break
        if (load8u(arg0 + 127) == 6):
            return 0
        if (v3 == v9):
            return 0
        arg1 = ((v3 * 404) + 9568096)
        if (load32(((v3 * 404) + 9568096) + 136) == 0):
            break
        if (((load32(arg1 + 140) != 0) & v12) == 0):
            break
        arg0 = load8u(arg0 + 125)
        arg2 = ((25 if (load8u(arg0 + 125) != 4) else 0) if (arg0 != 14) else 0)
        break
    return arg2

# ------------------------------------------------------------
# $func162
# ------------------------------------------------------------
def func162(arg0, arg1, arg2, arg3):
    while True:  # block $label2
        while True:  # block $label0
            if (u(load32(9142848)) >= u((load32(load32(9142424) + 72) * 2400))):
                break
            if (load32(arg0 + 56) == 1):
            else:
            if 0:
                break
            if (load32(38564) == arg1):
                break
            while True:  # block $label1
                # br_table[(arg2 - 4)]
                break
                break
            if (arg3 == 0):
                break
            arg2 = load32(9561692)
            v5 = load32(9671128)
            v4 = (load32(9671128) + (arg3 * 132))
            v6 = load16u((load32(9671128) + (arg3 * 132)) + 110)
            v7 = load32((load32(9561692) + (load16u((load32(9671128) + (arg3 * 132)) + 110) * 286704)) + 283872)
            if (load32((load32(9561692) + (load16u((load32(9671128) + (arg3 * 132)) + 110) * 286704)) + 283872) == 0):
                break
            v4 = (load16u(v4 + 112) - v7)
            v4 = (v4 >> 31)
            if (u((((load16u(v4 + 112) - v7) ^ (v4 >> 31)) - v4)) > u(30)):
                break
            v4 = 0
            arg2 = (load16u((v5 + (arg3 * 132)) + 114) - load32((arg2 + (v6 * 286704)) + 283876))
            arg2 = (arg2 >> 31)
            if (u((((load16u((v5 + (arg3 * 132)) + 114) - load32((arg2 + (v6 * 286704)) + 283876)) ^ (arg2 >> 31)) - arg2)) < u(31)):
                break
            break
        arg3 = ((arg1 * 404) + 9568096)
        arg2 = load32(((arg1 * 404) + 9568096) + 264)
        arg0 = load8u(arg0 + 122)
        while True:  # block $label3
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
            if (load32(((arg0 * 404) + 9568096) + 224) == 1):
                break
        v4 = 0
        while True:  # block $label4
            if (load32(((arg0 * 404) + 9568096) + 272) == 0):
                if (load32(38648) != arg0):
                    break
            if (load32(((arg1 * 404) + 9568096) + 208) == 2):
                break
            break
        while True:  # block $label5
            if (load32(38564) != arg1):
                break
            arg3 = ((arg0 * 404) + 9568096)
            if load8u(((arg0 * 404) + 9568096) + 334):
                break
            if (load32(arg3 + 268) != 2):
                break
            break
        while True:  # block $label6
            if (arg0 != load32(38728)):
                if (load32(38996) != arg0):
                    break
            if arg2:
                break
            if (load32(((arg1 * 404) + 9568096) + 268) == 2):
                break
            break
        arg2 = ((arg0 * 404) + 9568096)
        if load8u(((arg0 * 404) + 9568096) + 379):
            break
        arg2 = load32(arg2 + 24)
        if (load32(arg2 + 24) == 0):
            return 1
        arg3 = load32(((arg0 * 404) + 9568096) + 364)
        if (load32(((arg0 * 404) + 9568096) + 364) == 0):
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

# ------------------------------------------------------------
# $func163
# ------------------------------------------------------------
def func163(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    v8 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if (u(arg2) <= u(((arg1 ^ -1) + 2147483631))):
        while True:  # block $label0
            if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
                break
            break
        v9 = arg0
        if (u(arg1) < u(1073741799)):
            store32(v8 + 12, (arg1 << 1))
            store32(v8 + 4, (arg1 + arg2))
            arg2 = (G.global0 - 16)
            G.global0 = (G.global0 - 16)
            v10 = (v8 + 4)
            v11 = (v8 + 12)
            v12 = (u(load32((v8 + 4))) < u(load32((v8 + 12))))
            G.global0 = (arg2 + 16)
            arg2 = load32((v11 if v12 else v10))
            if (u(load32((v11 if v12 else v10))) >= u(11)):
                arg2 = ((arg2 + 16) & -16)
                arg2 = (arg2 - 1)
            else:
        else:
        func314((((arg2 + 16) & -16) if (arg2 == 11) else (arg2 - 1)), (10 + 1), 2147483631)
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
    raise RuntimeError('unreachable')
    return arg0

# ------------------------------------------------------------
# $func164
# ------------------------------------------------------------
def func164():
    while True:  # $label0
        v2 = ((v0 * 132) + 9216080)
        if load8u(((v0 * 132) + 9216080) + 23):
            store32(((load32(v2 + 4) * 404) + 9568096) + 180, v2)
        store32(v2 + 68, 0)
        store32(v2 + 112, 0)
        v0 = (v0 + 1)
        if ((v0 + 1) != 356):
            continue
        break
    v8 = load8u(9216060)
    while True:  # $label7
        v2 = ((v4 * 404) + 9568096)
        if (load32(((v4 * 404) + 9568096) + 148) == 0):
            store32(v2 + 148, 9)
        while True:  # block $label1
            v0 = load32(v2 + 244)
            if (load32(v2 + 244) == 0):
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
            if ((v0 & 1) == 0):
                break
            v1 = ((load32((v3 + (v1 << 2))) * 132) + 9216080)
            v0 = load32(v1 + 68)
            store32(((load32((v3 + (v1 << 2))) * 132) + 9216080) + 68, (load32(v1 + 68) + 1))
            store32((v1 + (v0 << 2)) + 28, v4)
            break
        while True:  # block $label3
            v1 = load32(v2 + 180)
            if (load32(v2 + 180) == 0):
                break
            v0 = load32(v2 + 264)
            if (load32(v2 + 264) == 1):
                while True:  # block $label4
                    v0 = load32(v2 + 196)
                    if (((v8 == 0) & (load32(v2 + 196) != 3)) == 0):
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
            if (load32(v2 + 236) == 0):
                break
            v6 = load32(v2 + 232)
            v1 = 0
            while True:  # $label6
                while True:  # block $label5
                    v3 = ((load32((v6 + (v1 << 2))) * 132) + 9216080)
                    if (load8u(((load32((v6 + (v1 << 2))) * 132) + 9216080) + 23) == 0):
                        break
                    v3 = load32(((load32(v3 + 4) * 404) + 9568096) + 180)
                    if (load32(((load32(v3 + 4) * 404) + 9568096) + 180) == 0):
                        break
                    v0 = load32(v3 + 112)
                    store32(v3 + 112, (load32(v3 + 112) + 1))
                    store32((v3 + (v0 << 2)) + 72, v4)
                    v0 = load32(v2 + 236)
                    break
                v1 = (v1 + 1)
                if (u((v1 + 1)) < u(v0)):
                    continue
                break
            break
        v4 = (v4 + 1)
        if ((v4 + 1) != 255):
            continue
        break
    return load32(v2 + 264)

# ------------------------------------------------------------
# $func165
# ------------------------------------------------------------
def func165(arg0, arg1):
    while True:  # block $label9
        while True:  # block $label1
            while True:  # block $label3
                while True:  # block $label2
                    while True:  # block $label0
                        # br_table[load32(arg0 + 4)]
                        break
                        break
                    if (load32(arg0 + 88) == 0):
                        break
                    v7 = load32(arg0 + 32)
                    v8 = (load32(arg0 + 32) == 0)
                    while True:  # $label8
                        while True:  # block $label7
                            v4 = load32((load32(arg0 + 80) + (v6 << 2)))
                            # call_indirect[arg1]
                            if (indirect_call(arg1) != (load8u(arg0 + 45) != 0)):
                                v3 = load32(9140300)
                                while True:  # block $label5
                                    while True:  # block $label4
                                        if (u(load32(9684388)) >= u(2)):
                                            v2 = 0
                                            if (v3 == 0):
                                                break
                                            while True:  # $label6
                                                if (load32(((v2 << 2) + 8451904)) == v4):
                                                    break
                                                v2 = (v2 + 1)
                                                if ((v2 + 1) != v3):
                                                    continue
                                                break
                                        v2 = v3
                                        if (u(v3) > u(39999)):
                                            break
                                        break
                                    store32(9140300, (v2 + 1))
                                    store32(((v2 << 2) + 8451904), v4)
                                    break
                                store32((load32(9142420) + (load16u((load32(9671128) + (v4 * 132)) + 110) << 2)), 1)
                                v5 = (v5 | v8)
                                break
                            if v7:
                                break
                            break
                        v6 = (v6 + 1)
                        if (u((v6 + 1)) < u(load32(arg0 + 88))):
                            continue
                        break
                    v7 = ((v7 != 0) | v5)
                    break
                    break
                v8 = load32(9140300)
                v4 = load32(arg0 + 32)
                store32(9140300, 0)
                if load32(9142892):
                    v3 = load32(9142420)
                    while True:  # $label10
                        store32((v3 + (v2 << 2)), 0)
                        v2 = (v2 + 1)
                        if (u((v2 + 1)) < u(load32(9142892))):
                            continue
                        break
                if v8:
                    v9 = (v4 == 0)
                    while True:  # $label15
                        while True:  # block $label14
                            v7 = load32(((v6 << 2) + 8451904))
                            # call_indirect[arg1]
                            if (indirect_call(arg1) != (load8u(arg0 + 45) != 0)):
                                v3 = load32(9140300)
                                while True:  # block $label12
                                    while True:  # block $label11
                                        if (u(load32(9684388)) >= u(2)):
                                            v2 = 0
                                            if (v3 == 0):
                                                break
                                            while True:  # $label13
                                                if (load32(((v2 << 2) + 8451904)) == v7):
                                                    break
                                                v2 = (v2 + 1)
                                                if ((v2 + 1) != v3):
                                                    continue
                                                break
                                        v2 = v3
                                        if (u(v3) > u(39999)):
                                            break
                                        break
                                    store32(9140300, (v2 + 1))
                                    store32(((v2 << 2) + 8451904), v7)
                                    break
                                store32((load32(9142420) + (load16u((load32(9671128) + (v7 * 132)) + 110) << 2)), 1)
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
        v2 = load32(9142892)
        if (load32(9142892) == 0):
            break
        v3 = load32(arg0 + 32)
        v13 = (u(load32(arg0 + 32)) > u(3))
        v14 = (v3 - 1)
        v15 = ((v3 - 4) << 2)
        while True:  # $label38
            v3 = load32(arg0 + 48)
            v2 = load32((load32(arg0 + 48) + (v2 << 2)))
            while True:  # block $label16
                while True:  # block $label18
                    while True:  # block $label17
                        v9 = (v8 << 2)
                        if (load32((v3 + (v8 << 2))) == 0):
                            if (v2 == 0):
                                break
                            if load32((load32(9142420) + v9)):
                                break
                            break
                        if (v2 == 0):
                            break
                        break
                    store32((load32(9142420) + v9), 0)
                    break
                v6 = 0
                v16 = load32(9140300)
                v10 = load32(9561692)
                v4 = 0
                while True:  # block $label37
                    while True:  # block $label36
                        while True:  # block $label35
                            while True:  # block $label30
                                while True:  # block $label29
                                    if (v13 == 0):
                                        while True:  # $label28
                                            while True:  # block $label23
                                                while True:  # block $label22
                                                    while True:  # block $label20
                                                        while True:  # block $label21
                                                            while True:  # block $label19
                                                                # br_table[v14]
                                                                break
                                                                break
                                                            v2 = ((v4 * 404) + 9568096)
                                                            if load32(((v4 * 404) + 9568096) + 264):
                                                                break
                                                            if (load32(v2 + 268) == 1):
                                                                break
                                                            if (load32(v2 + 92) == 0):
                                                                break
                                                            if (load32(38456) == v4):
                                                                break
                                                            if (load32(38764) != v4):
                                                                break
                                                            break
                                                            break
                                                        if (load32(((v4 * 404) + 9568096) + 264) == 1):
                                                            break
                                                        break
                                                        break
                                                    if load32(((v4 * 404) + 9568096) + 264):
                                                        break
                                                    break
                                                v11 = load32((((v10 + (v8 * 286704)) + 284636) + (v4 << 2)))
                                                if (load32((((v10 + (v8 * 286704)) + 284636) + (v4 << 2))) == 0):
                                                    break
                                                v5 = 0
                                                v17 = load32(v11 + 8)
                                                if (load32(v11 + 8) == 0):
                                                    break
                                                while True:  # $label27
                                                    while True:  # block $label24
                                                        v2 = load32((load32(v11) + (v5 << 2)))
                                                        if (load32((load32(v11) + (v5 << 2))) == 0):
                                                            break
                                                        v2 = (load32(9671128) + (v2 * 132))
                                                        # call_indirect[arg1]
                                                        if (indirect_call(arg1) == (load8u(arg0 + 45) != 0)):
                                                            break
                                                        v6 = (v6 + 1)
                                                        v3 = load32(9140300)
                                                        v12 = load32(v2 + 28)
                                                        while True:  # block $label25
                                                            if (u(load32(9684388)) >= u(2)):
                                                                v2 = 0
                                                                if (v3 == 0):
                                                                    break
                                                                while True:  # $label26
                                                                    if (load32(((v2 << 2) + 8451904)) == v12):
                                                                        break
                                                                    v2 = (v2 + 1)
                                                                    if ((v2 + 1) != v3):
                                                                        continue
                                                                    break
                                                            v2 = v3
                                                            if (u(v3) > u(39999)):
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
                                        raise RuntimeError('unreachable')
                                    v4 = load32((((v10 + (v8 * 286704)) + 284636) + v15))
                                    if (load32((((v10 + (v8 * 286704)) + 284636) + v15)) == 0):
                                        break
                                    v5 = 0
                                    v11 = load32(v4 + 8)
                                    if (load32(v4 + 8) == 0):
                                        break
                                    while True:  # $label34
                                        while True:  # block $label31
                                            v2 = load32((load32(v4) + (v5 << 2)))
                                            if (load32((load32(v4) + (v5 << 2))) == 0):
                                                break
                                            v2 = (load32(9671128) + (v2 * 132))
                                            # call_indirect[arg1]
                                            if (indirect_call(arg1) == (load8u(arg0 + 45) != 0)):
                                                break
                                            v6 = (v6 + 1)
                                            v3 = load32(9140300)
                                            v10 = load32(v2 + 28)
                                            while True:  # block $label32
                                                if (u(load32(9684388)) >= u(2)):
                                                    v2 = 0
                                                    if (v3 == 0):
                                                        break
                                                    while True:  # $label33
                                                        if (load32(((v2 << 2) + 8451904)) == v10):
                                                            break
                                                        v2 = (v2 + 1)
                                                        if ((v2 + 1) != v3):
                                                            continue
                                                        break
                                                v2 = v3
                                                if (u(v3) > u(39999)):
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
                                if (u(v2) < u(v6)):
                                    break
                                break
                                break
                            v2 = load32(arg0 + 12)
                            v5 = load32(arg0 + 16)
                            break
                        if (v5 == 0):
                            break
                        if (u(v2) <= u(v6)):
                            break
                        break
                    v7 = 1
                    store32((load32(9142420) + v9), 1)
                    v2 = load32(arg0 + 12)
                    v5 = load32(arg0 + 16)
                    break
                if (v5 == 0):
                    break
                if (u(v2) > u(v6)):
                    break
                store32(9140300, v16)
                break
            v8 = (v8 + 1)
            v2 = load32(9142892)
            if (u((v8 + 1)) < u(load32(9142892))):
                continue
            break
        break
    return (v7 & 1)

# ------------------------------------------------------------
# $func166
# ------------------------------------------------------------
def func166(arg0, arg1, arg2, arg3):
    while True:  # block $label5
        v7 = load32(9142432)
        if load32(9142432):
            v10 = (arg1 << 1)
            v11 = (arg0 << 1)
            v12 = load32(9142440)
            v13 = load32((v7 + (((load32(9142440) * arg1) + arg0) << 2)))
            v14 = load32(9671128)
            arg0 = 2147483647
            v16 = (load32(9561692) + (arg2 * 286704))
            while True:  # $label4
                while True:  # block $label0
                    v9 = ((v6 * 404) + 9568096)
                    arg1 = load32(((v6 * 404) + 9568096) + 192)
                    if ((arg3 != load32(((v6 * 404) + 9568096) + 192)) & (arg1 != 4)):
                        break
                    arg1 = load32(((v16 + (v6 << 2)) + 284636))
                    if (load32(((v16 + (v6 << 2)) + 284636)) == 0):
                        break
                    v17 = load32(arg1 + 8)
                    if (load32(arg1 + 8) == 0):
                        break
                    v18 = load32(arg1)
                    arg1 = 0
                    while True:  # $label3
                        while True:  # block $label1
                            v4 = load32((v18 + (arg1 << 2)))
                            if (load32((v18 + (arg1 << 2))) == 0):
                                break
                            v5 = (v14 + (v4 * 132))
                            v19 = load16u((v14 + (v4 * 132)) + 114)
                            v4 = (v10 - (load32(v9 + 220) + (load16u((v14 + (v4 * 132)) + 114) << 1)))
                            v15 = load16u(v5 + 112)
                            v4 = (v11 - (load32(v9 + 216) + (load16u(v5 + 112) << 1)))
                            v4 = (((v10 - (load32(v9 + 220) + (load16u((v14 + (v4 * 132)) + 114) << 1))) * v4) + ((v11 - (load32(v9 + 216) + (load16u(v5 + 112) << 1))) * v4))
                            if ((((v10 - (load32(v9 + 220) + (load16u((v14 + (v4 * 132)) + 114) << 1))) * v4) + ((v11 - (load32(v9 + 216) + (load16u(v5 + 112) << 1))) * v4)) >= arg0):
                                break
                            v15 = ((load8u(v5 + 122) * 404) + 9568096)
                            if (load32((v7 + (((v15 + ((load32(((load8u(v5 + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1)) + (v12 * (((load32(v15 + 220) & 0xFFFFFFFF) >> 1) + v19))) << 2))) != v13):
                                break
                            if (load16u(v5 + 110) != arg2):
                                break
                            while True:  # block $label2
                                # br_table[(load8u(v5 + 125) - 4)]
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
        v11 = load32(9671128)
        arg0 = 2147483647
        v12 = (load32(9561692) + (arg2 * 286704))
        while True:  # $label10
            while True:  # block $label6
                v7 = ((v5 * 404) + 9568096)
                arg1 = load32(((v5 * 404) + 9568096) + 192)
                if ((arg3 != load32(((v5 * 404) + 9568096) + 192)) & (arg1 != 4)):
                    break
                arg1 = load32(((v12 + (v5 << 2)) + 284636))
                if (load32(((v12 + (v5 << 2)) + 284636)) == 0):
                    break
                v13 = load32(arg1 + 8)
                if (load32(arg1 + 8) == 0):
                    break
                v14 = load32(arg1)
                arg1 = 0
                while True:  # $label9
                    while True:  # block $label7
                        v4 = load32((v14 + (arg1 << 2)))
                        if (load32((v14 + (arg1 << 2))) == 0):
                            break
                        v6 = (v11 + (v4 * 132))
                        v4 = (v9 - (load32(v7 + 220) + (load16u((v11 + (v4 * 132)) + 114) << 1)))
                        v4 = (v10 - (load32(v7 + 216) + (load16u(v6 + 112) << 1)))
                        v4 = (((v9 - (load32(v7 + 220) + (load16u((v11 + (v4 * 132)) + 114) << 1))) * v4) + ((v10 - (load32(v7 + 216) + (load16u(v6 + 112) << 1))) * v4))
                        if ((((v9 - (load32(v7 + 220) + (load16u((v11 + (v4 * 132)) + 114) << 1))) * v4) + ((v10 - (load32(v7 + 216) + (load16u(v6 + 112) << 1))) * v4)) >= arg0):
                            break
                        if (load16u(v6 + 110) != arg2):
                            break
                        while True:  # block $label8
                            # br_table[(load8u(v6 + 125) - 4)]
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

# ------------------------------------------------------------
# $func167
# ------------------------------------------------------------
def func167(arg0, arg1, arg2, arg3, arg4):
    v8 = load32(9142440)
    v20 = load32(arg1)
    v21 = load32(arg0)
    while True:  # block $label8
        while True:  # block $label2
            if (arg4 == 0):
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
                        while True:  # block $label0
                            if (u(v6) >= u(v8)):
                                break
                            v5 = arg2
                            while True:  # block $label1
                                if (v6 != v13):
                                    if (arg3 != v6):
                                        break
                                while True:  # $label3
                                    if ((u(v5) < u(v8)) & ((v5 | v6) >= 0)):
                                        break
                                    v5 = (v5 + 1)
                                    if ((v5 + 1) < arg4):
                                        continue
                                    break
                                break
                                break
                            while True:  # $label5
                                while True:  # block $label4
                                    if ((arg2 != v5) & (v5 != v14)):
                                        break
                                    if (u(v5) >= u(v8)):
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
                    v11 = (u(v7) < u(39))
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
                    if (u(v6) < u(v8)):
                        v29 = (v6 == v26)
                        v30 = (v6 == v12)
                        v5 = v13
                        while True:  # $label12
                            while True:  # block $label9
                                if ((v29 | ((v30 | (v5 == v13)) | (v5 == v28))) == 0):
                                    break
                                if (u(v5) >= u(v8)):
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
                v11 = (u(v9) < u(39))
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

# ------------------------------------------------------------
# $func168
# ------------------------------------------------------------
def func168(arg0, arg1):
    while True:  # block $label0
        if (arg1 >= 1024):
            arg0 = (arg0 * 8.98846567431158e+307)
            if (u(arg1) < u(2047)):
                arg1 = (arg1 - 1023)
                break
            arg0 = (arg0 * 8.98846567431158e+307)
            arg1 = ((3069 if (arg1 >= 3069) else arg1) - 2046)
            break
        if (arg1 > -1023):
            break
        arg0 = (arg0 * 2.004168360008973e-292)
        if (u(arg1) > u(-1992)):
            arg1 = (arg1 + 969)
            break
        arg0 = (arg0 * 2.004168360008973e-292)
        arg1 = ((-2960 if (arg1 <= -2960) else arg1) + 1938)
        break
    # TODO: f64.reinterpret_i64 []
    return (arg0 * (i64((arg1 + 1023)) << 52))

# ------------------------------------------------------------
# $func169
# ------------------------------------------------------------
def func169():
    v14 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v0 = load32(9140328)
    if load32(9140328):
        v5 = load32(9142440)
        while True:  # $label7
            v1 = load32(((v15 << 2) + 9140336))
            v17 = load32(load32(((v15 << 2) + 9140336)) + 44)
            if (u(((v5 * load32(load32(((v15 << 2) + 9140336)) + 44)) * v5)) >= u(65536)):
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
                    while True:  # block $label3
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
                                while True:  # block $label1
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
                            if (v12 == 0):
                                break
                        v0 = 0
                        v3 = load32(v1 + 52)
                        v6 = load32(9681936)
                        while True:  # block $label4
                            if ((load8u(9568060) | load8u(9147152)) == 0):
                                break
                            if load8u(9142917):
                                break
                            while True:  # block $label5
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
                                if (u(v4) < u(load32(9163784))):
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
                    if (u((v18 + 1)) < u(((((v5 * v17) * v5) & 0xFFFFFFFF) >> 16))):
                        continue
                    break
                v0 = load32(9140328)
            v15 = (v15 + 1)
            if (u((v15 + 1)) < u(v0)):
                continue
            break
    G.global0 = (v14 + 16)

# ------------------------------------------------------------
# $func170
# ------------------------------------------------------------
def func170(arg0):
    if load32(9142912):
        v3 = load32(9142908)
        v9 = load32(load32(9142908) + 60)
        v6 = load32(v3)
        v7 = (v6 + (load32(v3 + 4) * 60))
        if (u(load32(v3)) < u((v6 + (load32(v3 + 4) * 60)))):
            v4 = v7
            while True:  # $label6
                v8 = load32(9142908)
                v1 = (load32(9142908) + (v6 << 2))
                v10 = load32((load32(9142908) + (v6 << 2)))
                v2 = ((load32((load32(9142908) + (v6 << 2))) * 404) + 9568096)
                v3 = load32(v1 + 4)
                store32(((load32((load32(9142908) + (v6 << 2))) * 404) + 9568096) + 108, load32(v1 + 4))
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
                while True:  # block $label0
                    if (v3 == load32(v2 + 220)):
                        break
                    store32(v2 + 220, v3)
                    v3 = (v3 * v3)
                    v12 = func26((v3 * v3))
                    store32(v2 + 372, func26((v3 * v3)))
                    if (v3 == 0):
                        break
                    # TODO: memory.fill []
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
                    store32(v2 + 232, func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2))))
                if v3:
                    store32(v2 + 24, func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2))))
                if load32(v2 + 236):
                    v3 = load32(v2 + 232)
                    v1 = 0
                    v5 = load32(9142908)
                    while True:  # $label1
                        store32((v3 + (v1 << 2)), load32((v5 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u((v1 + 1)) < u(load32(v2 + 236))):
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
                        if (u((v1 + 1)) < u(load32(v2 + 364))):
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
                while True:  # block $label4
                    if (v8 == 0):
                        break
                    v1 = ((((v8 - 1) & 0xFFFFFFFF) >> 1) + 1)
                    v10 = (((((v8 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                    v5 = load32(9142908)
                    if (u(v8) >= u(3)):
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
                    if (v10 == 0):
                        break
                    v1 = (v5 + (v4 << 2))
                    store32((v2 + (load32((v5 + (v4 << 2))) << 2)), load32(v1 + 4))
                    v4 = (v4 + 2)
                    break
                v6 = (v6 + 60)
                if (u((v6 + 60)) < u(v7)):
                    continue
                break
            v3 = load32(9142908)
        v6 = load32(v3 + 8)
        v7 = (v6 + (load32(v3 + 12) * 55))
        if (u(load32(v3 + 8)) < u((v6 + (load32(v3 + 12) * 55)))):
            v11 = (u(v9) < u(623))
            v12 = (u(v9) > u(622))
            v4 = v7
            while True:  # $label16
                v1 = (load32(9142908) + (v6 << 2))
                v13 = load32((load32(9142908) + (v6 << 2)))
                v2 = ((load32((load32(9142908) + (v6 << 2))) * 404) + 9568096)
                v3 = load32(v1 + 4)
                store32(((load32((load32(9142908) + (v6 << 2))) * 404) + 9568096) + 108, load32(v1 + 4))
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
                if (v11 == 0):
                    store32(v2 + 244, load32(v1 + 192))
                if v3:
                    store32(v2 + 232, func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2))))
                v3 = func26((v9 * v10))
                store32(v2 + 372, func26((v9 * v10)))
                if v5:
                    store32(v2 + 24, func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2))))
                if load32(v2 + 236):
                    v5 = load32(v2 + 232)
                    v1 = 0
                    v9 = load32(9142908)
                    while True:  # $label7
                        store32((v5 + (v1 << 2)), load32((v9 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u((v1 + 1)) < u(load32(v2 + 236))):
                            continue
                        break
                while True:  # block $label8
                    v5 = (load32(v2 + 220) * load32(v2 + 216))
                    if ((load32(v2 + 220) * load32(v2 + 216)) == 0):
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
                    if ((v5 & 1) == 0):
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
                        if (u((v1 + 1)) < u(load32(v2 + 364))):
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
                while True:  # block $label12
                    if (v8 == 0):
                        break
                    v1 = ((((v8 - 1) & 0xFFFFFFFF) >> 1) + 1)
                    v10 = (((((v8 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
                    v9 = load32(9142908)
                    if (u(v8) >= u(3)):
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
                    if (v10 == 0):
                        break
                    v1 = (v9 + (v4 << 2))
                    store32((v5 + (load32((v9 + (v4 << 2))) << 2)), load32(v1 + 4))
                    v4 = (v4 + 2)
                    break
                while True:  # block $label14
                    if (v12 == 0):
                        break
                    v1 = load32(v2 + 244)
                    if (load32(v2 + 244) == 0):
                        break
                    v3 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
                    store32(v2 + 240, func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2))))
                    v2 = load32(v2 + 244)
                    v1 = 0
                    v5 = load32(9142908)
                    while True:  # $label15
                        store32((v3 + (v1 << 2)), load32((v5 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u((v1 + 1)) < u(v2)):
                            continue
                        break
                    break
                v6 = (v6 + 55)
                if (u((v6 + 55)) < u(v7)):
                    continue
                break
            v3 = load32(9142908)
        v6 = load32(v3 + 16)
        v7 = (v6 + (load32(v3 + 20) * 23))
        if (u(load32(v3 + 16)) < u((v6 + (load32(v3 + 20) * 23)))):
            v4 = v7
            while True:  # $label19
                v1 = (v3 + (v6 << 2))
                v2 = ((load32((v3 + (v6 << 2))) * 404) + 9568096)
                v5 = load32(v1 + 4)
                if (u(load32(v1 + 4)) <= u(4)):
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
                    store32(v2 + 232, func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2))))
                if v8:
                    v5 = func26((-1 if (u(v8) > u(1073741823)) else (v8 << 2)))
                    store32(v2 + 240, func26((-1 if (u(v8) > u(1073741823)) else (v8 << 2))))
                    v8 = load32(v2 + 244)
                    v1 = 0
                    while True:  # $label17
                        store32((v5 + (v1 << 2)), load32((v3 + (v4 << 2))))
                        v4 = (v4 + 1)
                        v1 = (v1 + 1)
                        if (u((v1 + 1)) < u(v8)):
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
                        if (u((v1 + 1)) < u(load32(v2 + 236))):
                            continue
                        break
                v6 = (v6 + 23)
                if (u((v6 + 23)) < u(v7)):
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
        while True:  # block $label21
            if load8u(9147152):
                break
            if ((arg0 ^ 1) & (load8u(9147212) != 0)):
                break
            if (load32(9142892) == 0):
                break
            v2 = load32(9561692)
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
                if (u((v6 + 1)) < u(load32(9142892))):
                    continue
                break
            break
    return func164()

# ------------------------------------------------------------
# $md
# Export: md
# ------------------------------------------------------------
def md(arg0):
    """Exported as md."""
    v2 = load32(9142440)
    v1 = (load32(9142440) * v2)
    while True:  # block $label8
        while True:  # block $label0
            while True:  # block $label1
                while True:  # block $label2
                    while True:  # block $label3
                        while True:  # block $label4
                            while True:  # block $label5
                                while True:  # block $label6
                                    while True:  # block $label7
                                        # br_table[((arg0 - 1) if arg0 else load32(load32(9142424) + 28))]
                                        break
                                        break
                                    while True:  # block $label9
                                        if (v1 == 0):
                                            break
                                        v2 = 0
                                        arg0 = 0
                                        if (u((v1 - 1)) >= u(3)):
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
                                        if ((v1 & 3) == 0):
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
                                            if (u((v2 + 8)) < u(load32(9147300))):
                                                continue
                                            break
                                    break
                                    break
                                while True:  # block $label13
                                    if (v1 == 0):
                                        break
                                    v2 = 0
                                    arg0 = 0
                                    if (u((v1 - 1)) >= u(3)):
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
                                    if ((v1 & 3) == 0):
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
                                        if (u((v2 + 8)) < u(load32(9147300))):
                                            continue
                                        break
                                break
                                break
                            while True:  # block $label17
                                if (v1 == 0):
                                    break
                                v2 = 0
                                arg0 = 0
                                if (u((v1 - 1)) >= u(3)):
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
                                if ((v1 & 3) == 0):
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
                                    if (u((v2 + 8)) < u(load32(9147300))):
                                        continue
                                    break
                            break
                            break
                        while True:  # block $label21
                            if (v1 == 0):
                                break
                            v2 = 0
                            arg0 = 0
                            if (u((v1 - 1)) >= u(3)):
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
                            if ((v1 & 3) == 0):
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
                        if (load32(9147300) == 0):
                            break
                        while True:  # $label24
                            arg0 = load32(9684504)
                            v1 = (v2 << 2)
                            v2 = (v2 + 8)
                            if (u((v2 + 8)) < u(load32(9147300))):
                                continue
                            break
                        break
                        break
                    while True:  # block $label25
                        if (v1 == 0):
                            break
                        v2 = 0
                        arg0 = 0
                        if (u((v1 - 1)) >= u(3)):
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
                        if ((v1 & 3) == 0):
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
                            if (u((v2 + 8)) < u(load32(9147300))):
                                continue
                            break
                    break
                    break
                while True:  # block $label29
                    if (v1 == 0):
                        break
                    v2 = 0
                    arg0 = 0
                    if (u((v1 - 1)) >= u(3)):
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
                    if ((v1 & 3) == 0):
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
                        if (u((v2 + 8)) < u(load32(9147300))):
                            continue
                        break
                break
                break
            while True:  # block $label33
                if (v1 == 0):
                    break
                v2 = 0
                arg0 = 0
                if (u((v1 - 1)) >= u(3)):
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
                if ((v1 & 3) == 0):
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
                    if (u((v2 + 8)) < u(load32(9147300))):
                        continue
                    break
            break
            break
        while True:  # block $label37
            if (v1 == 0):
                break
            v2 = 0
            arg0 = 0
            if (u((v1 - 1)) >= u(3)):
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
            if ((v1 & 3) == 0):
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
        if (load32(9147300) == 0):
            break
        while True:  # $label40
            arg0 = load32(9684504)
            v1 = (v2 << 2)
            v2 = (v2 + 8)
            if (u((v2 + 8)) < u(load32(9147300))):
                continue
            break
        break
    while True:  # block $label41
        if (load32(load32(9142424) + 64) == 0):
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
            while True:  # block $label43
                if (v9 == 0):
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

# ------------------------------------------------------------
# $func172
# ------------------------------------------------------------
def func172(arg0):
    v1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    if arg0:
        store32(9143000, 0)
    arg0 = 0
    a_b()
    store32(9671120, 0)
    while True:  # block $label0
        v2 = load32(9147120)
        if (load32(9147120) == 0):
            break
        while True:  # $label1
            v2 = ((load32(9143000) * v2) + arg0)
            if (u(((load32(9143000) * v2) + arg0)) >= u(load32(9681836))):
                break
            store32(9671120, (load32(9671120) + 1))
            v2 = load32(((load8u((load32(9671128) + (load32((load32(9681828) + (v2 << 2))) * 132)) + 122) * 404) + 9568096) + 144)
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
            if (u((arg0 + 1)) < u(load32(9147120))):
                continue
            break
        break
    store32(v1, load32(9143000))
    store32(v1 + 4, load32(9681836))
    a_b()
    G.global0 = (v1 - -64)

# ------------------------------------------------------------
# $func174
# ------------------------------------------------------------
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
    v17 = (u(load32((arg0 + ((v12 << 2) | 4)))) < u(v4))
    v6 = (arg0 + v6)
    v18 = load32((arg0 + v6) + 8)
    v21 = load32(9671136)
    v11 = (u(load32((arg0 + v6) + 8)) > u(load32(9671136)))
    v7 = (v12 | 5)
    v10 = load32(v6 + 12)
    if (load32(v6 + 12) == 69):
        store32((arg0 + (v7 << 2)), 1)
    v16 = (v16 if v17 else v5)
    v17 = (v3 if (u(v3) < u(v4)) else v5)
    v19 = load32(v6 + 16)
    v20 = load32((arg0 + (v7 << 2)))
    v3 = ((v11 | (load32((arg0 + (v7 << 2))) != 0)) & (v10 != 40))
    v8 = (5 if ((v11 | (load32((arg0 + (v7 << 2))) != 0)) & (v10 != 40)) else 0)
    v9 = load32(v6 + 24)
    if arg2:
        v14 = (1 if v3 else (1 if v11 else v13))
        v22 = (-1 if (u(v14) > u(1073741823)) else ((1 if v3 else (1 if v11 else v13)) << 2))
        v6 = (v14 * 7)
        v23 = (1 if (u(v6) <= u(1)) else (v14 * 7))
        v24 = (2 if v11 else 1)
        v13 = 0
        while True:  # $label16
            while True:  # block $label0
                v7 = (load32(9671128) + (load32((arg1 + (v13 << 2))) * 132))
                if (load32(((load8u((load32(9671128) + (load32((arg1 + (v13 << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1):
                    break
                while True:  # block $label1
                    if (u(v18) <= u(v21)):
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
                while True:  # block $label15
                    if v14:
                        while True:  # block $label4
                            while True:  # block $label3
                                while True:  # block $label2
                                    if (v3 == 0):
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
                                    if (load32(v3 + 4) == 0):
                                        break
                                    break
                                v5 = load32(v3)
                                v4 = 0
                                break
                                break
                            v5 = load32(v3 + 12)
                            store32(v3 + 4, load32(v3 + 12))
                            v4 = load32(v3)
                            v5 = func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2)))
                            if v4:
                            else:
                            v4 = 0
                            store32(v3, v5)
                            v3 = load32(v7 + 20)
                            break
                        store32(v6, (v4 + 1))
                        store32((v5 + (v4 << 2)), v24)
                        while True:  # block $label5
                            v4 = load32(v3 + 8)
                            if (load32(v3 + 8) != load32(v3 + 4)):
                                v5 = load32(v3)
                                break
                            v5 = (load32(v3 + 12) + v4)
                            store32(v3 + 4, (load32(v3 + 12) + v4))
                            v6 = load32(v3)
                            v5 = func26((-1 if (u(v5) > u(1073741823)) else (v5 << 2)))
                            if v4:
                                # TODO: memory.copy []
                            if v6:
                                v4 = load32(v3 + 8)
                            store32(v3, v5)
                            break
                        store32(v3 + 8, (v4 + 1))
                        store32((v5 + (v4 << 2)), 2)
                        v5 = 0
                        while True:  # $label7
                            v25 = load32((arg0 + ((v5 + v12) << 2)))
                            while True:  # block $label6
                                v4 = load32(v7 + 20)
                                v3 = load32(load32(v7 + 20) + 8)
                                if (load32(load32(v7 + 20) + 8) != load32(v4 + 4)):
                                    v6 = load32(v4)
                                    break
                                v6 = (load32(v4 + 12) + v3)
                                store32(v4 + 4, (load32(v4 + 12) + v3))
                                v15 = load32(v4)
                                v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
                                if v3:
                                    # TODO: memory.copy []
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
                        if (v11 == 0):
                            break
                        store32(v3 + 16, 0)
                        v15 = load16u(v7 + 112)
                        while True:  # block $label8
                            v5 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v6 = v3
                                break
                            v6 = (load32(v4 + 12) + v5)
                            store32(v4 + 4, (load32(v4 + 12) + v5))
                            v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy []
                            store32(v4, v6)
                            v5 = load32(v4 + 8)
                            break
                        v3 = load32(v7 + 20)
                        store32(v4 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), v15)
                        v15 = load16u(v7 + 114)
                        while True:  # block $label9
                            v5 = load32(v3 + 8)
                            if (load32(v3 + 8) != load32(v3 + 4)):
                                v6 = load32(v3)
                                break
                            v6 = (load32(v3 + 12) + v5)
                            store32(v3 + 4, (load32(v3 + 12) + v5))
                            v4 = load32(v3)
                            v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy []
                            if v4:
                                v5 = load32(v3 + 8)
                            store32(v3, v6)
                            break
                        v4 = load32(v7 + 20)
                        store32(v3 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), v15)
                        while True:  # block $label10
                            v5 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v6 = load32(v4)
                                break
                            v6 = (load32(v4 + 12) + v5)
                            store32(v4 + 4, (load32(v4 + 12) + v5))
                            v3 = load32(v4)
                            v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy []
                            if v3:
                                v5 = load32(v4 + 8)
                            store32(v4, v6)
                            break
                        v3 = load32(v7 + 20)
                        store32(v4 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), 0)
                        while True:  # block $label11
                            v5 = load32(v3 + 8)
                            if (load32(v3 + 8) != load32(v3 + 4)):
                                v6 = load32(v3)
                                break
                            v6 = (load32(v3 + 12) + v5)
                            store32(v3 + 4, (load32(v3 + 12) + v5))
                            v4 = load32(v3)
                            v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy []
                            if v4:
                                v5 = load32(v3 + 8)
                            store32(v3, v6)
                            break
                        v4 = load32(v7 + 20)
                        store32(v3 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), 0)
                        while True:  # block $label12
                            v5 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v6 = load32(v4)
                                break
                            v6 = (load32(v4 + 12) + v5)
                            store32(v4 + 4, (load32(v4 + 12) + v5))
                            v3 = load32(v4)
                            v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy []
                            if v3:
                                v5 = load32(v4 + 8)
                            store32(v4, v6)
                            break
                        v3 = load32(v7 + 20)
                        store32(v4 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), 0)
                        while True:  # block $label13
                            v5 = load32(v3 + 8)
                            if (load32(v3 + 8) != load32(v3 + 4)):
                                v6 = load32(v3)
                                break
                            v6 = (load32(v3 + 12) + v5)
                            store32(v3 + 4, (load32(v3 + 12) + v5))
                            v4 = load32(v3)
                            v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
                            if v5:
                                # TODO: memory.copy []
                            if v4:
                                v5 = load32(v3 + 8)
                            store32(v3, v6)
                            break
                        v4 = load32(v7 + 20)
                        store32(v3 + 8, (v5 + 1))
                        store32((v6 + (v5 << 2)), 5)
                        while True:  # block $label14
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
                        store32(v4 + 8, (v3 + 1))
                        break
                    if (v3 == 0):
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
    while True:  # block $label17
        if (v20 == 0):
            break
        if (v7 == 0):
            break
        if ((v10 != 62) & (v10 != 40)):
            break
        v12 = 14
        break
    while True:  # block $label20
        while True:  # block $label19
            while True:  # block $label18
                if (v20 == 0):
                    break
                if (v9 == 0):
                    break
                if (v7 == 0):
                    break
                if ((v10 != 62) & (v10 != 40)):
                    break
                v12 = 15
                break
                break
            v6 = v16
            if (v7 == 0):
                break
            break
        arg0 = (load32(9671128) + (v7 * 132))
        v6 = load16u((load32(9671128) + (v7 * 132)) + 114)
        break
    v13 = load16u(arg0 + 112)
    while True:  # block $label23
        while True:  # block $label22
            while True:  # block $label21
                if (v9 == 0):
                    break
                if (v10 == 6):
                    break
                if (v12 != 15):
                    break
                break
            if (arg2 == 0):
                break
            # TODO: memory.fill []
            arg0 = 0
            while True:  # $label25
                v11 = load32(9671128)
                v3 = 2147483647
                v4 = 0
                while True:  # $label24
                    if (load8u((v4 + 9163808)) == 0):
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
        if (arg2 == 0):
            break
        v11 = ((v10 * 40) + 9671208)
        v4 = 0
        v8 = load32(9561692)
        v14 = load32(9671128)
        v5 = 2147483647
        v3 = 0
        while True:  # $label27
            while True:  # block $label26
                arg0 = (v14 + (load32((arg1 + (v4 << 2))) * 132))
                if (v10 == load8u((v14 + (load32((arg1 + (v4 << 2))) * 132)) + 123)):
                    break
                v9 = load32(v11)
                if load32(v11):
                    if (u(load32((((v8 + (load16u(arg0 + 110) * 286704)) + (v9 << 2)) + 283984))) > u(load32(arg0 + 72))):
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
        if (v3 == 0):
            break
        break
    return 9163808

# ------------------------------------------------------------
# $func176
# ------------------------------------------------------------
def func176(arg0, arg1, arg2):
    v7 = load32(9561692)
    v3 = load32(9143004)
    v4 = load32(9142892)
    v5 = ((load32(9142892) * arg1) + arg0)
    v6 = (arg2 != 0)
    store8((load32(9143004) + ((load32(9142892) * arg1) + arg0)), (arg2 != 0))
    store8((v3 + ((arg0 * v4) + arg1)), v6)
    v6 = load32(9142872)
    v8 = (load32(9142872) == arg0)
    v9 = ((load32(9142872) == arg0) | (arg1 == v6))
    if arg2:
        while True:  # block $label0
            if (v9 == 0):
                break
            v3 = 0
            arg2 = (arg1 if v8 else arg0)
            if (load8u((load32(9143012) + ((arg1 if v8 else arg0) + (v4 * v6)))) == 0):
                break
            v8 = (v7 + (arg2 * 286704))
            while True:  # $label4
                while True:  # block $label1
                    v4 = load32(((v8 + (v3 << 2)) + 284636))
                    if (load32(((v8 + (v3 << 2)) + 284636)) == 0):
                        break
                    arg2 = 0
                    v6 = load32(v4 + 8)
                    if (load32(v4 + 8) == 0):
                        break
                    while True:  # $label3
                        while True:  # block $label2
                            v5 = load32((load32(v4) + (arg2 << 2)))
                            if (load32((load32(v4) + (arg2 << 2))) == 0):
                                break
                            v5 = (load32(9671128) + (v5 * 132))
                            if load32((load32(9671128) + (v5 * 132)) + 36):
                                break
                            func118(v5)
                            v6 = load32(v4 + 8)
                            break
                        arg2 = (arg2 + 1)
                        if (u((arg2 + 1)) < u(v6)):
                            continue
                        break
                    break
                v3 = (v3 + 1)
                if ((v3 + 1) != 255):
                    continue
                break
            v5 = ((load32(9142892) * arg1) + arg0)
            break
        store8((load32(9143016) + v5), 0)
        store8((load32(9143016) + ((load32(9142892) * arg0) + arg1)), 0)
        arg2 = load32(9143012)
        v3 = load32(9142892)
        v4 = ((load32(9142892) * arg1) + arg0)
        store8((load32(9143012) + ((load32(9142892) * arg1) + arg0)), 0)
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