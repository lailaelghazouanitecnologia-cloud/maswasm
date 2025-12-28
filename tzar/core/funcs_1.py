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
# $func177
# ------------------------------------------------------------
def func177(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11):
    v36 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label67
        if (arg8 >= 2):
            while True:  # block $label21
                arg10 = arg0
                arg8 = arg1
                v15 = arg2
                arg11 = arg6
                v20 = arg7
                arg0 = 0
                arg1 = 0
                while True:  # block $label18
                    v19 = arg9
                    arg6 = load32(arg9)
                    if load32(arg9):
                        arg2 = ((arg6 & 0xFFFFFFFF) >> 16)
                        while True:  # block $label2
                            while True:  # block $label1
                                while True:  # block $label0
                                    arg6 = (arg6 & 65535)
                                    if (arg10 == (arg6 & 65535)):
                                        v14 = ((arg2 == arg8) | ((arg8 + 1) == arg2))
                                        if ((arg10 + 1) == arg6):
                                            break
                                        if (v14 == 0):
                                            break
                                        break
                                    if ((arg10 + 1) != arg6):
                                        break
                                    break
                                if (arg2 == arg8):
                                    break
                                if ((arg8 + 1) == arg2):
                                    break
                                if v14:
                                    break
                                break
                            arg7 = load32(9671128)
                            arg9 = load32(9142840)
                            v16 = (arg6 + 1)
                            v12 = (load32(9142440) + 2)
                            v14 = (arg2 + ((load32(9142440) + 2) * arg5))
                            v21 = (((arg2 + ((load32(9142440) + 2) * arg5)) + 1) * v12)
                            v13 = load32((load32(9142840) + (((arg6 + 1) + (((arg2 + ((load32(9142440) + 2) * arg5)) + 1) * v12)) << 2)))
                            if (arg4 != load32((load32(9142840) + (((arg6 + 1) + (((arg2 + ((load32(9142440) + 2) * arg5)) + 1) * v12)) << 2)))):
                                if (v13 == -1):
                                    break
                                if (load8u((arg7 + (v13 * 132)) + 125) != 1):
                                    break
                            v27 = (arg6 + 2)
                            v13 = load32((arg9 + ((v21 + (arg6 + 2)) << 2)))
                            if (arg4 != load32((arg9 + ((v21 + (arg6 + 2)) << 2)))):
                                if (v13 == -1):
                                    break
                                if (load8u((arg7 + (v13 * 132)) + 125) != 1):
                                    break
                            v13 = ((v14 + 2) * v12)
                            v12 = load32((arg9 + ((v16 + ((v14 + 2) * v12)) << 2)))
                            if (arg4 != load32((arg9 + ((v16 + ((v14 + 2) * v12)) << 2)))):
                                if (v12 == -1):
                                    break
                                if (load8u((arg7 + (v12 * 132)) + 125) != 1):
                                    break
                            arg9 = load32((arg9 + ((v13 + v27) << 2)))
                            if (arg4 != load32((arg9 + ((v13 + v27) << 2)))):
                                if (arg9 == -1):
                                    break
                                if (load8u((arg7 + (arg9 * 132)) + 125) != 1):
                                    break
                            v14 = 1
                            while True:  # block $label12
                                v27 = 0
                                arg7 = load16u(40596)
                                arg9 = (load16u(40596) + 2)
                                store16(40596, (load16u(40596) + 2))
                                v16 = load32(9142440)
                                while True:  # block $label3
                                    if (u((arg9 & 65535)) < u(65534)):
                                        break
                                    store16(40596, 1)
                                    arg9 = (v16 * v16)
                                    if ((v16 * v16) == 0):
                                        break
                                    # TODO: memory.fill []
                                    break
                                v17 = (arg7 + 1)
                                store32(59200, ((arg2 << 16) + arg6))
                                v23 = load32(9142436)
                                v21 = 1
                                while True:  # $label17
                                    v31 = (v17 & 65535)
                                    arg2 = load32(((v27 << 2) + 59200))
                                    arg7 = ((load32(((v27 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                                    arg9 = (arg2 & 65535)
                                    arg2 = (v23 + (((((load32(((v27 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * v16) + (arg2 & 65535)) << 1))
                                    if ((v17 & 65535) != load16u((v23 + (((((load32(((v27 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * v16) + (arg2 & 65535)) << 1)))):
                                        store16(arg2, v17)
                                        while True:  # $label13
                                            v22 = 0
                                            v33 = (load32(9142440) + 2)
                                            v32 = ((load32(9142440) + 2) * arg5)
                                            v26 = load32(9671128)
                                            v24 = load32(9142840)
                                            while True:  # $label9
                                                arg2 = (v22 << 3)
                                                v12 = (load32(((v22 << 3) + 8928)) + arg9)
                                                while True:  # block $label8
                                                    while True:  # block $label4
                                                        v13 = (load32((arg2 + 8932)) + arg7)
                                                        v25 = ((load32((arg2 + 8932)) + arg7) + 2)
                                                        if (((load32((arg2 + 8932)) + arg7) + 2) <= v13):
                                                            break
                                                        v28 = 0
                                                        arg6 = v13
                                                        v29 = (v12 + 2)
                                                        if ((v12 + 2) <= v12):
                                                            break
                                                        while True:  # $label7
                                                            arg6 = (arg6 + 1)
                                                            v34 = (((arg6 + 1) + v32) * v33)
                                                            arg2 = v12
                                                            while True:  # block $label5
                                                                while True:  # $label6
                                                                    arg2 = (arg2 + 1)
                                                                    v18 = load32((v24 + (((arg2 + 1) + v34) << 2)))
                                                                    if (arg4 != load32((v24 + (((arg2 + 1) + v34) << 2)))):
                                                                        if (v18 == -1):
                                                                            break
                                                                        if (load8u((v26 + (v18 * 132)) + 125) != 1):
                                                                            break
                                                                    if (arg2 != v29):
                                                                        continue
                                                                    break
                                                                v28 = (arg6 >= v25)
                                                                if (arg6 != v25):
                                                                    continue
                                                                break
                                                            break
                                                        if (v28 == 0):
                                                            break
                                                        break
                                                    if (load16u((v23 + (((v13 * v16) + v12) << 1))) == v31):
                                                        break
                                                    arg2 = (v12 - arg10)
                                                    arg2 = (v13 - arg8)
                                                    if (((((v12 - arg10) * arg2) + ((v13 - arg8) * arg2)) - 1) > 1156):
                                                        break
                                                    store32(((v21 << 2) + 59200), ((v13 << 16) + v12))
                                                    v21 = (v21 + 1)
                                                    break
                                                v22 = (v22 + 1)
                                                if ((v22 + 1) != 8):
                                                    continue
                                                break
                                            arg2 = (arg8 - arg7)
                                            while True:  # block $label10
                                                arg6 = (arg10 - arg9)
                                                if ((arg10 - arg9) == 0):
                                                    break
                                                if (arg7 == arg8):
                                                    break
                                                arg6 = (arg2 // arg6)
                                                arg6 = (arg6 >> 31)
                                                arg6 = (arg6 if (u((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u(1)) else 0)
                                                arg2 = ((arg6 if (u((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u(1)) else 0) // arg2)
                                                arg2 = (arg2 >> 31)
                                                arg2 = (arg2 if (u(((((arg6 if (u((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u(1)) else 0) // arg2) ^ (arg2 >> 31)) - arg2)) <= u(1)) else 0)
                                                break
                                            arg2 = (-1 if (arg2 < 0) else (arg2 != 0))
                                            arg7 = ((-1 if (arg2 < 0) else (arg2 != 0)) + arg7)
                                            while True:  # block $label11
                                                arg6 = (-1 if (arg6 < 0) else (arg6 != 0))
                                                arg9 = ((-1 if (arg6 < 0) else (arg6 != 0)) + arg9)
                                                if (((-1 if (arg6 < 0) else (arg6 != 0)) + arg9) != arg10):
                                                    break
                                                if (arg7 != arg8):
                                                    break
                                                store32(arg11, (0 - arg6))
                                                store32(v20, (0 - arg2))
                                                break
                                                break
                                            store16((v23 + (((arg7 * v16) + arg9) << 1)), v17)
                                            v13 = (arg7 + 2)
                                            if ((arg7 + 2) <= arg7):
                                                continue
                                            v25 = (arg9 + 2)
                                            if ((arg9 + 2) <= arg9):
                                                continue
                                            arg6 = 0
                                            v28 = (load32(9142440) + 2)
                                            v18 = ((load32(9142440) + 2) * arg5)
                                            v33 = load32(9671128)
                                            v32 = load32(9142840)
                                            v12 = arg7
                                            while True:  # $label16
                                                v12 = (v12 + 1)
                                                v26 = (((v12 + 1) + v18) * v28)
                                                arg2 = arg9
                                                while True:  # block $label14
                                                    while True:  # $label15
                                                        arg2 = (arg2 + 1)
                                                        v22 = load32((v32 + (((arg2 + 1) + v26) << 2)))
                                                        if (arg4 != load32((v32 + (((arg2 + 1) + v26) << 2)))):
                                                            if (v22 == -1):
                                                                break
                                                            if (load8u((v33 + (v22 * 132)) + 125) != 1):
                                                                break
                                                        if (arg2 != v25):
                                                            continue
                                                        break
                                                    arg6 = (v12 >= v13)
                                                    if (v12 != v13):
                                                        continue
                                                    break
                                                break
                                            if (arg6 & 1):
                                                continue
                                            break
                                    v27 = (v27 + 1)
                                    if (u((v27 + 1)) < u(v21)):
                                        continue
                                    break
                                break
                            if 0:
                                break
                            break
                        store32(v19, 0)
                    arg2 = (arg3 - arg8)
                    v23 = load32(9142440)
                    while True:  # block $label19
                        arg6 = (v15 - arg10)
                        if ((v15 - arg10) == 0):
                            break
                        if (arg3 == arg8):
                            break
                        arg6 = (arg2 // arg6)
                        arg6 = (arg6 >> 31)
                        arg6 = (arg6 if (u((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u(1)) else 0)
                        arg2 = ((arg6 if (u((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u(1)) else 0) // arg2)
                        arg2 = (arg2 >> 31)
                        arg2 = (arg2 if (u(((((arg6 if (u((((arg2 // arg6) ^ (arg6 >> 31)) - arg6)) <= u(1)) else 0) // arg2) ^ (arg2 >> 31)) - arg2)) <= u(1)) else 0)
                        break
                    arg6 = (-1 if (arg6 < 0) else (arg6 != 0))
                    store32(arg11, (-1 if (arg6 < 0) else (arg6 != 0)))
                    arg2 = (-1 if (arg2 < 0) else (arg2 != 0))
                    store32(v20, (-1 if (arg2 < 0) else (arg2 != 0)))
                    arg6 = (arg6 + arg10)
                    arg2 = (arg2 + arg8)
                    v16 = load32(9142440)
                    v21 = (load32(9142440) + 2)
                    v27 = ((load32(9142440) + 2) * arg5)
                    arg9 = load32(9671128)
                    v12 = load32(9142840)
                    v13 = 0
                    while True:  # $label26
                        while True:  # block $label20
                            if (arg6 != v15):
                                break
                            if (arg2 != arg3):
                                break
                            break
                            break
                        while True:  # block $label23
                            while True:  # block $label22
                                if (arg2 > 2147483645):
                                    break
                                if (arg6 > 2147483645):
                                    break
                                v14 = (arg6 + 1)
                                v17 = (arg2 + 1)
                                v22 = (((arg2 + 1) + v27) * v21)
                                arg7 = load32((v12 + (((arg6 + 1) + (((arg2 + 1) + v27) * v21)) << 2)))
                                if (arg4 != load32((v12 + (((arg6 + 1) + (((arg2 + 1) + v27) * v21)) << 2)))):
                                    if (arg7 == -1):
                                        break
                                    if (load8u((arg9 + (arg7 * 132)) + 125) != 1):
                                        break
                                v25 = (arg6 + 2)
                                arg7 = load32((v12 + ((v22 + (arg6 + 2)) << 2)))
                                if (arg4 != load32((v12 + ((v22 + (arg6 + 2)) << 2)))):
                                    if (arg7 == -1):
                                        break
                                    if (load8u((arg9 + (arg7 * 132)) + 125) != 1):
                                        break
                                while True:  # block $label24
                                    v22 = (arg2 + 2)
                                    v28 = (((arg2 + 2) + v27) * v21)
                                    arg7 = load32((v12 + ((v14 + (((arg2 + 2) + v27) * v21)) << 2)))
                                    if (arg4 != load32((v12 + ((v14 + (((arg2 + 2) + v27) * v21)) << 2)))):
                                        if (arg7 == -1):
                                            break
                                        if (load8u((arg9 + (arg7 * 132)) + 125) != 1):
                                            break
                                    arg7 = load32((v12 + ((v25 + v28) << 2)))
                                    if (arg4 != load32((v12 + ((v25 + v28) << 2)))):
                                        if (arg7 == -1):
                                            break
                                        if (load8u((arg9 + (arg7 * 132)) + 125) != 1):
                                            break
                                    break
                                    break
                                if (v17 < v22):
                                    break
                                break
                            v14 = (arg3 - arg2)
                            while True:  # block $label25
                                arg7 = (v15 - arg6)
                                if ((v15 - arg6) == 0):
                                    break
                                if (arg2 == arg3):
                                    break
                                arg7 = (v14 // arg7)
                                arg7 = (arg7 >> 31)
                                arg7 = (arg7 if (u((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u(1)) else 0)
                                v14 = ((arg7 if (u((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u(1)) else 0) // v14)
                                v14 = (v14 >> 31)
                                v14 = (v14 if (u(((((arg7 if (u((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u(1)) else 0) // v14) ^ (v14 >> 31)) - v14)) <= u(1)) else 0)
                                break
                            arg6 = ((-1 if (arg7 < 0) else (arg7 != 0)) + arg6)
                            arg2 = ((-1 if (v14 < 0) else (v14 != 0)) + arg2)
                            v14 = 1
                            v13 = (v13 + 1)
                            if ((v13 + 1) != 32):
                                continue
                            break
                            break
                        break
                    v21 = load16u(40596)
                    arg7 = (load16u(40596) + 2)
                    store16(40596, (load16u(40596) + 2))
                    v26 = (arg6 + (arg2 << 16))
                    while True:  # block $label27
                        if (u((arg7 & 65535)) < u(65534)):
                            break
                        store16(40596, 1)
                        arg7 = (v16 * v16)
                        if ((v16 * v16) == 0):
                            break
                        # TODO: memory.fill []
                        break
                    v33 = (v21 + 1)
                    store32(59200, v26)
                    v17 = load32(9142436)
                    store16((load32(9142436) + ((arg6 + (arg2 * v23)) << 1)), v21)
                    v27 = 2147483647
                    v18 = 1
                    arg2 = 0
                    v25 = 0
                    while True:  # $label44
                        v35 = (3000 if (u(v25) <= u(3000)) else v25)
                        v12 = (arg2 + 1)
                        arg2 = load32(((arg2 << 2) + 59200))
                        arg9 = ((load32(((arg2 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                        v16 = (arg2 & 65535)
                        while True:  # block $label28
                            while True:  # $label43
                                if (v25 == v35):
                                    break
                                v25 = (v25 + 1)
                                v14 = 0
                                v31 = 0
                                while True:  # $label42
                                    while True:  # block $label29
                                        arg2 = (v14 << 4)
                                        arg6 = (load32(((v14 << 4) + 8932)) + arg9)
                                        if ((load32(((v14 << 4) + 8932)) + arg9) > 2147483645):
                                            break
                                        arg7 = (load32((arg2 + 8928)) + v16)
                                        if ((load32((arg2 + 8928)) + v16) > 2147483645):
                                            break
                                        v13 = load32(9671128)
                                        while True:  # block $label31
                                            while True:  # block $label30
                                                v22 = load32(9142840)
                                                v29 = (arg7 + 1)
                                                v34 = (arg6 + 1)
                                                v28 = (load32(9142440) + 2)
                                                v32 = ((load32(9142440) + 2) * arg5)
                                                v24 = (((arg6 + 1) + ((load32(9142440) + 2) * arg5)) * v28)
                                                arg2 = load32((load32(9142840) + (((arg7 + 1) + (((arg6 + 1) + ((load32(9142440) + 2) * arg5)) * v28)) << 2)))
                                                if (load32((load32(9142840) + (((arg7 + 1) + (((arg6 + 1) + ((load32(9142440) + 2) * arg5)) * v28)) << 2))) == arg4):
                                                    break
                                                if (arg2 == -1):
                                                    break
                                                if (load8u((v13 + (arg2 * 132)) + 125) != 1):
                                                    break
                                                break
                                            while True:  # block $label33
                                                while True:  # block $label32
                                                    v38 = (arg7 + 2)
                                                    v24 = load32((v22 + (((arg7 + 2) + v24) << 2)))
                                                    if (load32((v22 + (((arg7 + 2) + v24) << 2))) == arg4):
                                                        break
                                                    if (v24 == -1):
                                                        break
                                                    if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                        break
                                                    break
                                                while True:  # block $label35
                                                    while True:  # block $label34
                                                        v37 = (arg6 + 2)
                                                        v39 = (((arg6 + 2) + v32) * v28)
                                                        v24 = load32((v22 + ((v29 + (((arg6 + 2) + v32) * v28)) << 2)))
                                                        if (load32((v22 + ((v29 + (((arg6 + 2) + v32) * v28)) << 2))) == arg4):
                                                            break
                                                        if (v24 == -1):
                                                            break
                                                        if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                            break
                                                        break
                                                    while True:  # block $label36
                                                        v24 = load32((v22 + ((v38 + v39) << 2)))
                                                        if (load32((v22 + ((v38 + v39) << 2))) == arg4):
                                                            break
                                                        if (v24 == -1):
                                                            break
                                                        if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                            break
                                                        break
                                                    break
                                                    break
                                                if (v34 >= v37):
                                                    break
                                                if (arg2 != -1):
                                                    break
                                                break
                                                break
                                            if (arg2 == -1):
                                                break
                                            break
                                        arg2 = 0
                                        v38 = (v17 + (((arg6 * v23) + arg7) << 1))
                                        if (load16u((v17 + (((arg6 * v23) + arg7) << 1))) == v21):
                                            break
                                        while True:  # $label40
                                            while True:  # block $label37
                                                v29 = (arg2 << 3)
                                                v24 = (load32(((arg2 << 3) + 8932)) + arg6)
                                                if ((load32(((arg2 << 3) + 8932)) + arg6) > 2147483645):
                                                    break
                                                v29 = (load32((v29 + 8928)) + arg7)
                                                if ((load32((v29 + 8928)) + arg7) > 2147483645):
                                                    break
                                                while True:  # block $label38
                                                    v37 = (v29 + 1)
                                                    v39 = (v24 + 1)
                                                    v40 = (((v24 + 1) + v32) * v28)
                                                    v34 = load32((v22 + (((v29 + 1) + (((v24 + 1) + v32) * v28)) << 2)))
                                                    if (arg4 != load32((v22 + (((v29 + 1) + (((v24 + 1) + v32) * v28)) << 2)))):
                                                        if (v34 == -1):
                                                            break
                                                        if (load8u((v13 + (v34 * 132)) + 125) != 1):
                                                            break
                                                    v34 = (v29 + 2)
                                                    v29 = load32((v22 + (((v29 + 2) + v40) << 2)))
                                                    if (arg4 != load32((v22 + (((v29 + 2) + v40) << 2)))):
                                                        if (v29 == -1):
                                                            break
                                                        if (load8u((v13 + (v29 * 132)) + 125) != 1):
                                                            break
                                                    while True:  # block $label39
                                                        v29 = (v24 + 2)
                                                        v40 = (((v24 + 2) + v32) * v28)
                                                        v24 = load32((v22 + ((v37 + (((v24 + 2) + v32) * v28)) << 2)))
                                                        if (arg4 != load32((v22 + ((v37 + (((v24 + 2) + v32) * v28)) << 2)))):
                                                            if (v24 == -1):
                                                                break
                                                            if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                                break
                                                        v24 = load32((v22 + ((v34 + v40) << 2)))
                                                        if (arg4 != load32((v22 + ((v34 + v40) << 2)))):
                                                            if (v24 == -1):
                                                                break
                                                            if (load8u((v13 + (v24 * 132)) + 125) != 1):
                                                                break
                                                        break
                                                        break
                                                    if (v29 <= v39):
                                                        break
                                                    break
                                                arg2 = (arg2 + 1)
                                                if ((arg2 + 1) != 8):
                                                    continue
                                                break
                                                break
                                            break
                                        arg2 = ((arg6 << 16) + arg7)
                                        while True:  # block $label41
                                            if (v31 == 0):
                                                arg0 = arg7
                                                arg1 = arg6
                                                break
                                            store32(((v18 << 2) + 59200), arg2)
                                            v18 = (v18 + 1)
                                            break
                                        store16(v38, v21)
                                        arg6 = (arg6 - arg3)
                                        arg6 = (arg7 - v15)
                                        arg6 = (((arg6 - arg3) * arg6) + ((arg7 - v15) * arg6))
                                        arg6 = (arg6 < v27)
                                        v27 = ((((arg6 - arg3) * arg6) + ((arg7 - v15) * arg6)) if (arg6 < v27) else v27)
                                        v30 = (arg2 if arg6 else v30)
                                        v31 = (v31 + 1)
                                        break
                                    v14 = (v14 + 1)
                                    if ((v14 + 1) != 4):
                                        continue
                                    break
                                v16 = arg0
                                arg9 = arg1
                                if v31:
                                    continue
                                break
                            if (u(v12) >= u(v18)):
                                break
                            arg2 = v12
                            if (u(v25) < u(3001)):
                                continue
                            break
                        break
                    arg6 = 0
                    v12 = (load32(9142440) + 2)
                    v16 = ((load32(9142440) + 2) * arg5)
                    arg7 = 2147483647
                    arg0 = (v26 if (v27 == 2147483647) else v30)
                    v27 = (((v26 if (v27 == 2147483647) else v30) & 0xFFFFFFFF) >> 16)
                    v22 = (arg0 & 65535)
                    arg1 = load32(9671128)
                    arg2 = load32(9142840)
                    v13 = 55
                    while True:  # $label48
                        arg9 = (arg6 << 3)
                        arg0 = (load32(((arg6 << 3) + 8928)) + v22)
                        while True:  # block $label46
                            while True:  # block $label45
                                arg9 = (load32((arg9 + 8932)) + v27)
                                if ((load32((arg9 + 8932)) + v27) > 2147483645):
                                    break
                                if (arg0 > 2147483645):
                                    break
                                v25 = (arg0 + 1)
                                v28 = (arg9 + 1)
                                v18 = (((arg9 + 1) + v16) * v12)
                                v14 = load32((arg2 + (((arg0 + 1) + (((arg9 + 1) + v16) * v12)) << 2)))
                                if (arg4 != load32((arg2 + (((arg0 + 1) + (((arg9 + 1) + v16) * v12)) << 2)))):
                                    if (v14 == -1):
                                        break
                                    if (load8u((arg1 + (v14 * 132)) + 125) != 1):
                                        break
                                v30 = (arg0 + 2)
                                v14 = load32((arg2 + ((v18 + (arg0 + 2)) << 2)))
                                if (arg4 != load32((arg2 + ((v18 + (arg0 + 2)) << 2)))):
                                    if (v14 == -1):
                                        break
                                    if (load8u((arg1 + (v14 * 132)) + 125) != 1):
                                        break
                                while True:  # block $label47
                                    v18 = (arg9 + 2)
                                    v31 = (((arg9 + 2) + v16) * v12)
                                    v14 = load32((arg2 + ((v25 + (((arg9 + 2) + v16) * v12)) << 2)))
                                    if (arg4 != load32((arg2 + ((v25 + (((arg9 + 2) + v16) * v12)) << 2)))):
                                        if (v14 == -1):
                                            break
                                        if (load8u((arg1 + (v14 * 132)) + 125) != 1):
                                            break
                                    v14 = load32((arg2 + ((v30 + v31) << 2)))
                                    if (arg4 != load32((arg2 + ((v30 + v31) << 2)))):
                                        if (v14 == -1):
                                            break
                                        if (load8u((arg1 + (v14 * 132)) + 125) != 1):
                                            break
                                    break
                                    break
                                if (v18 > v28):
                                    break
                                break
                            v14 = (arg9 - arg3)
                            v14 = (arg0 - v15)
                            v14 = (((arg9 - arg3) * v14) + ((arg0 - v15) * v14))
                            v14 = (arg7 > v14)
                            arg7 = ((((arg9 - arg3) * v14) + ((arg0 - v15) * v14)) if (arg7 > v14) else arg7)
                            v13 = (((arg9 << 16) + arg0) if v14 else v13)
                            break
                        arg6 = (arg6 + 1)
                        if ((arg6 + 1) != 8):
                            continue
                        break
                    store32(59200, v13)
                    store16((v17 + (((((v13 & 0xFFFFFFFF) >> 16) * v23) + (v13 & 65535)) << 1)), v33)
                    v27 = 1
                    arg0 = 0
                    while True:  # $label66
                        arg1 = arg0
                        arg0 = (arg0 + 1)
                        v15 = load32(((arg1 << 2) + 59200))
                        v25 = ((load32(((arg1 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                        v28 = (v15 & 65535)
                        arg9 = 0
                        while True:  # $label65
                            arg1 = (arg9 << 3)
                            v14 = load32(((arg9 << 3) + 8928))
                            arg6 = (load32(((arg9 << 3) + 8928)) + v28)
                            while True:  # block $label50
                                while True:  # block $label49
                                    v16 = load32((arg1 + 8932))
                                    arg2 = (load32((arg1 + 8932)) + v25)
                                    if ((load32((arg1 + 8932)) + v25) > 2147483645):
                                        break
                                    if (arg6 > 2147483645):
                                        break
                                    arg1 = load32(9671128)
                                    arg3 = load32(9142840)
                                    v13 = (arg6 + 1)
                                    v22 = (arg2 + 1)
                                    arg7 = (load32(9142440) + 2)
                                    v18 = ((load32(9142440) + 2) * arg5)
                                    v30 = (((arg2 + 1) + ((load32(9142440) + 2) * arg5)) * arg7)
                                    v12 = load32((load32(9142840) + (((arg6 + 1) + (((arg2 + 1) + ((load32(9142440) + 2) * arg5)) * arg7)) << 2)))
                                    if (arg4 != load32((load32(9142840) + (((arg6 + 1) + (((arg2 + 1) + ((load32(9142440) + 2) * arg5)) * arg7)) << 2)))):
                                        if (v12 == -1):
                                            break
                                        if (load8u((arg1 + (v12 * 132)) + 125) != 1):
                                            break
                                    v31 = (arg6 + 2)
                                    v12 = load32((arg3 + ((v30 + (arg6 + 2)) << 2)))
                                    if (arg4 != load32((arg3 + ((v30 + (arg6 + 2)) << 2)))):
                                        if (v12 == -1):
                                            break
                                        if (load8u((arg1 + (v12 * 132)) + 125) != 1):
                                            break
                                    while True:  # block $label51
                                        v12 = (arg2 + 2)
                                        v18 = (((arg2 + 2) + v18) * arg7)
                                        arg7 = load32((arg3 + ((v13 + (((arg2 + 2) + v18) * arg7)) << 2)))
                                        if (arg4 != load32((arg3 + ((v13 + (((arg2 + 2) + v18) * arg7)) << 2)))):
                                            if (arg7 == -1):
                                                break
                                            if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                break
                                        arg3 = load32((arg3 + ((v18 + v31) << 2)))
                                        if (arg4 != load32((arg3 + ((v18 + v31) << 2)))):
                                            if (arg3 == -1):
                                                break
                                            if (load8u((arg1 + (arg3 * 132)) + 125) != 1):
                                                break
                                        break
                                        break
                                    if (v12 > v22):
                                        break
                                    break
                                v13 = (arg2 * v23)
                                v18 = (v17 + (((arg2 * v23) + arg6) << 1))
                                if (load16u((v17 + (((arg2 * v23) + arg6) << 1))) == (v33 & 65535)):
                                    break
                                arg3 = (arg6 + 1)
                                while True:  # block $label53
                                    while True:  # block $label52
                                        arg1 = load32(9142440)
                                        v30 = (u(load32(9142440)) <= u(arg2))
                                        if (u(load32(9142440)) <= u(arg2)):
                                            break
                                        if (u(arg1) <= u(arg3)):
                                            break
                                        if ((arg2 | arg3) < 0):
                                            break
                                        if (load16u((v17 + ((arg3 + v13) << 1))) == v21):
                                            break
                                        break
                                    while True:  # block $label54
                                        v12 = (arg2 - 1)
                                        v22 = (u(arg1) <= u((arg2 - 1)))
                                        if (u(arg1) <= u((arg2 - 1))):
                                            break
                                        if (u(arg1) <= u(arg3)):
                                            break
                                        if ((arg3 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg3) << 1))) == v21):
                                            break
                                        break
                                    while True:  # block $label55
                                        if v22:
                                            break
                                        if (u(arg1) <= u(arg6)):
                                            break
                                        if ((arg6 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg6) << 1))) == v21):
                                            break
                                        break
                                    arg7 = (arg6 - 1)
                                    while True:  # block $label56
                                        if v22:
                                            break
                                        if (u(arg1) <= u(arg7)):
                                            break
                                        if ((arg7 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg7) << 1))) == v21):
                                            break
                                        break
                                    while True:  # block $label57
                                        if v30:
                                            break
                                        if (u(arg1) <= u(arg7)):
                                            break
                                        if ((arg2 | arg7) < 0):
                                            break
                                        if (load16u((v17 + ((arg7 + v13) << 1))) == v21):
                                            break
                                        break
                                    while True:  # block $label58
                                        v12 = (arg2 + 1)
                                        v13 = (u(arg1) <= u((arg2 + 1)))
                                        if (u(arg1) <= u((arg2 + 1))):
                                            break
                                        if (u(arg1) <= u(arg7)):
                                            break
                                        if ((arg7 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg7) << 1))) == v21):
                                            break
                                        break
                                    while True:  # block $label59
                                        if v13:
                                            break
                                        if (u(arg1) <= u(arg6)):
                                            break
                                        if ((arg6 | v12) < 0):
                                            break
                                        if (load16u((v17 + (((v12 * v23) + arg6) << 1))) == v21):
                                            break
                                        break
                                    if v13:
                                        break
                                    if (u(arg1) <= u(arg3)):
                                        break
                                    if ((arg3 | v12) < 0):
                                        break
                                    if (load16u((v17 + (((v12 * v23) + arg3) << 1))) != v21):
                                        break
                                    break
                                store32(((v27 << 2) + 59200), ((arg2 << 16) + arg6))
                                while True:  # block $label60
                                    arg3 = (arg6 - arg10)
                                    arg3 = (arg2 - arg8)
                                    if (((((arg6 - arg10) * arg3) + ((arg2 - arg8) * arg3)) - 1) > 1089):
                                        break
                                    if (((arg6 == arg10) & (arg2 == arg8)) == 0):
                                        v13 = (arg2 == arg8)
                                        v12 = (arg1 + 2)
                                        v22 = ((arg1 + 2) * arg5)
                                        arg1 = load32(9671128)
                                        arg3 = load32(9142840)
                                        while True:  # $label64
                                            v14 = (arg8 - arg2)
                                            while True:  # block $label61
                                                arg7 = (arg10 - arg6)
                                                if ((arg10 - arg6) == 0):
                                                    break
                                                if (v13 & 1):
                                                    break
                                                arg7 = (v14 // arg7)
                                                arg7 = (arg7 >> 31)
                                                arg7 = (arg7 if (u((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u(1)) else 0)
                                                v13 = ((arg7 if (u((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u(1)) else 0) // v14)
                                                v13 = (v13 >> 31)
                                                v14 = (v14 if (u(((((arg7 if (u((((v14 // arg7) ^ (arg7 >> 31)) - arg7)) <= u(1)) else 0) // v14) ^ (v13 >> 31)) - v13)) <= u(1)) else 0)
                                                break
                                            while True:  # block $label62
                                                v16 = (-1 if (v14 < 0) else (v14 != 0))
                                                arg2 = ((-1 if (v14 < 0) else (v14 != 0)) + arg2)
                                                v14 = (-1 if (arg7 < 0) else (arg7 != 0))
                                                arg6 = ((-1 if (arg7 < 0) else (arg7 != 0)) + arg6)
                                                if (load16u((v17 + (((((-1 if (v14 < 0) else (v14 != 0)) + arg2) * v23) + ((-1 if (arg7 < 0) else (arg7 != 0)) + arg6)) << 1))) != v21):
                                                    break
                                                if (arg2 > 2147483645):
                                                    break
                                                if (arg6 > 2147483645):
                                                    break
                                                v13 = (arg6 + 1)
                                                v30 = (arg2 + 1)
                                                v31 = (((arg2 + 1) + v22) * v12)
                                                arg7 = load32((arg3 + (((arg6 + 1) + (((arg2 + 1) + v22) * v12)) << 2)))
                                                if (arg4 != load32((arg3 + (((arg6 + 1) + (((arg2 + 1) + v22) * v12)) << 2)))):
                                                    if (arg7 == -1):
                                                        break
                                                    if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                        break
                                                v32 = (arg6 + 2)
                                                arg7 = load32((arg3 + ((v31 + (arg6 + 2)) << 2)))
                                                if (arg4 != load32((arg3 + ((v31 + (arg6 + 2)) << 2)))):
                                                    if (arg7 == -1):
                                                        break
                                                    if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                        break
                                                while True:  # block $label63
                                                    v31 = (arg2 + 2)
                                                    v26 = (((arg2 + 2) + v22) * v12)
                                                    arg7 = load32((arg3 + ((v13 + (((arg2 + 2) + v22) * v12)) << 2)))
                                                    if (arg4 != load32((arg3 + ((v13 + (((arg2 + 2) + v22) * v12)) << 2)))):
                                                        if (arg7 == -1):
                                                            break
                                                        if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                            break
                                                    arg7 = load32((arg3 + ((v26 + v32) << 2)))
                                                    if (arg4 != load32((arg3 + ((v26 + v32) << 2)))):
                                                        if (arg7 == -1):
                                                            break
                                                        if (load8u((arg1 + (arg7 * 132)) + 125) != 1):
                                                            break
                                                    break
                                                    break
                                                if (v30 < v31):
                                                    break
                                                break
                                            v13 = (arg2 == arg8)
                                            if (arg6 != arg10):
                                                continue
                                            if (arg2 != arg8):
                                                continue
                                            break
                                    store32(arg11, (0 - v14))
                                    store32(v20, (0 - v16))
                                    store32(v19, v15)
                                    break
                                    break
                                v27 = (v27 + 1)
                                store16(v18, v33)
                                break
                            arg9 = (arg9 + 1)
                            if ((arg9 + 1) != 8):
                                continue
                            break
                        v14 = 0
                        if (u(arg0) < u(v27)):
                            continue
                        break
                    break
                break
            v20 = v14
            break
        arg8 = load32(arg9)
        if load32(arg9):
            v20 = 1
            if func365(arg0, arg1, (arg8 & 65535), ((arg8 & 0xFFFFFFFF) >> 16), arg4, arg5, arg6, arg7, load8u(arg10)):
                break
            store32(arg9, 0)
        store32(arg6, (-1 if (arg0 > arg2) else (arg0 != arg2)))
        store32(arg7, (-1 if (arg1 > arg3) else (arg1 != arg3)))
        v24 = (load32(9142440) + 2)
        v14 = ((load32(9142440) + 2) * arg5)
        v32 = load32(9671128)
        v26 = load32(9142840)
        v20 = 1
        arg8 = arg0
        v12 = arg1
        while True:  # $label69
            v27 = ((-1 if (arg2 < arg8) else (arg2 != arg8)) + arg8)
            v21 = ((-1 if (arg3 < v12) else (arg3 != v12)) + v12)
            if ((arg2 == ((-1 if (arg2 < arg8) else (arg2 != arg8)) + arg8)) & (((-1 if (arg3 < v12) else (arg3 != v12)) + v12) == arg3)):
                break
            while True:  # block $label68
                v15 = load32((((v27 + (((v14 + v21) + 1) * v24)) << 2) + v26) + 4)
                if (arg4 != load32((((v27 + (((v14 + v21) + 1) * v24)) << 2) + v26) + 4)):
                    if (v15 == -1):
                        break
                    if (load8u((v32 + (v15 * 132)) + 125) != 1):
                        break
                arg8 = v27
                v12 = v21
                v16 = (v16 + 1)
                if ((v16 + 1) != 32):
                    continue
                break
                break
            break
        store32(v36 + 8, v12)
        store32(v36 + 12, arg8)
        while True:  # block $label81
            while True:  # block $label80
                while True:  # block $label78
                    while True:  # block $label77
                        v28 = arg4
                        v20 = (load32(9142440) + 2)
                        v12 = ((load32(9142440) + 2) * arg5)
                        v15 = load32(9671128)
                        v13 = load32(9142840)
                        while True:  # block $label73
                            while True:  # block $label71
                                while True:  # block $label70
                                    v19 = load32(v36 + 8)
                                    arg4 = (v21 - load32(v36 + 8))
                                    v22 = ((v21 - load32(v36 + 8)) * arg4)
                                    arg4 = v27
                                    v16 = (v27 + 1)
                                    v17 = load32(v36 + 12)
                                    arg8 = ((v27 + 1) - load32(v36 + 12))
                                    if (u((((v21 - load32(v36 + 8)) * arg4) + (((v27 + 1) - load32(v36 + 12)) * arg8))) > u(2)):
                                        break
                                    arg8 = load32((((arg4 + (((v12 + v21) + 1) * v20)) << 2) + v13) + 8)
                                    if (v28 != load32((((arg4 + (((v12 + v21) + 1) * v20)) << 2) + v13) + 8)):
                                        if (arg8 == -1):
                                            break
                                        if (load8u((v15 + (arg8 * 132)) + 125) != 1):
                                            break
                                    break
                                    break
                                while True:  # block $label72
                                    arg8 = (arg4 - v17)
                                    v25 = ((arg4 - v17) * arg8)
                                    arg8 = (v21 - 1)
                                    v23 = ((v21 - 1) - v19)
                                    if (u((((arg4 - v17) * arg8) + (((v21 - 1) - v19) * v23))) > u(2)):
                                        break
                                    v23 = load32((v13 + ((v16 + ((v12 + v21) * v20)) << 2)))
                                    if (load32((v13 + ((v16 + ((v12 + v21) * v20)) << 2))) == v28):
                                        break
                                    if (v23 == -1):
                                        break
                                    if (load8u((v15 + (v23 * 132)) + 125) == 1):
                                        break
                                    break
                                arg8 = (v21 + 1)
                                while True:  # block $label75
                                    while True:  # block $label74
                                        v23 = (arg4 - 1)
                                        v17 = ((arg4 - 1) - v17)
                                        if (u((v22 + (((arg4 - 1) - v17) * v17))) > u(2)):
                                            break
                                        v17 = load32((v13 + ((((arg8 + v12) * v20) + arg4) << 2)))
                                        if (load32((v13 + ((((arg8 + v12) * v20) + arg4) << 2))) == v28):
                                            break
                                        if (v17 == -1):
                                            break
                                        if (load8u((v15 + (v17 * 132)) + 125) == 1):
                                            break
                                        break
                                    while True:  # block $label76
                                        v19 = (arg8 - v19)
                                        if (u((((arg8 - v19) * v19) + v25)) > u(2)):
                                            break
                                        v20 = load32((v13 + ((v16 + (((v12 + v21) + 2) * v20)) << 2)))
                                        if (load32((v13 + ((v16 + (((v12 + v21) + 2) * v20)) << 2))) == v28):
                                            break
                                        if (v20 == -1):
                                            break
                                        if (load8u((v15 + (v20 * 132)) + 125) == 1):
                                            break
                                        break
                                    break
                                    break
                                break
                            arg4 = v23
                            arg8 = v21
                            break
                        store32(v36 + 12, arg4)
                        store32(v36 + 8, arg8)
                        break
                    if 1:
                        arg4 = load32(v36 + 12)
                        v13 = load32(v36 + 8)
                        break
                    arg4 = load32(v36 + 12)
                    v12 = (load32(v36 + 12) + 1)
                    while True:  # block $label79
                        v13 = load32(v36 + 8)
                        arg8 = (load32(v36 + 8) + 1)
                        v19 = (((v14 + (load32(v36 + 8) + 1)) * v24) + arg4)
                        v20 = load32((((((v14 + (load32(v36 + 8) + 1)) * v24) + arg4) << 2) + v26) + 8)
                        if (load32((((((v14 + (load32(v36 + 8) + 1)) * v24) + arg4) << 2) + v26) + 8) == v28):
                            break
                        if (v20 != -1):
                            if (load8u((v32 + (v20 * 132)) + 125) == 1):
                                break
                        v15 = v12
                        break
                        break
                    v17 = (v13 + v14)
                    v16 = load32((v26 + ((((v13 + v14) * v24) + v12) << 2)))
                    if (v28 != load32((v26 + ((((v13 + v14) * v24) + v12) << 2)))):
                        v20 = (v13 - 1)
                        if (v16 == -1):
                            v15 = arg4
                            break
                        v15 = arg4
                        if (load8u((v32 + (v16 * 132)) + 125) != 1):
                            break
                    v16 = load32((v26 + (v19 << 2)))
                    if (v28 != load32((v26 + (v19 << 2)))):
                        v15 = (arg4 - 1)
                        if (v16 == -1):
                            break
                        v20 = v13
                        if (load8u((v32 + (v16 * 132)) + 125) != 1):
                            break
                    v12 = load32((v26 + ((((v17 + 2) * v24) + v12) << 2)))
                    if (load32((v26 + ((((v17 + 2) * v24) + v12) << 2))) == v28):
                        break
                    if (v12 == -1):
                        v15 = arg4
                        v20 = arg8
                        break
                    v15 = arg4
                    v20 = arg8
                    if (load8u((v32 + (v12 * 132)) + 125) != 1):
                        break
                    break
                v20 = v21
                v15 = v27
                break
                break
            v20 = v13
            break
        v19 = (v13 - v20)
        v30 = (arg4 - v15)
        v29 = (v14 + 1)
        v14 = v13
        v16 = arg4
        v12 = v20
        arg8 = v15
        while True:  # $label95
            while True:  # block $label94
                v17 = (v14 + v30)
                v23 = (v16 + v19)
                while True:  # block $label82
                    v22 = (arg8 + v19)
                    v25 = (v12 + v30)
                    v35 = load32(((((arg8 + v19) + (v24 * (v29 + (v12 + v30)))) << 2) + v26) + 4)
                    if (load32(((((arg8 + v19) + (v24 * (v29 + (v12 + v30)))) << 2) + v26) + 4) == v28):
                        break
                    if (v35 != -1):
                        if (load8u((v32 + (v35 * 132)) + 125) == 1):
                            break
                    break
                v35 = 0
                while True:  # block $label87
                    while True:  # block $label86
                        while True:  # block $label83
                            while True:  # block $label85
                                while True:  # block $label84
                                    v38 = load32((((v23 + ((v17 + v29) * v24)) << 2) + v26) + 4)
                                    if (v28 != load32((((v23 + ((v17 + v29) * v24)) << 2) + v26) + 4)):
                                        if (v38 == -1):
                                            break
                                        if v35:
                                            break
                                        if (load8u((v32 + (v38 * 132)) + 125) != 1):
                                            break
                                        break
                                    if (v35 == 0):
                                        break
                                    break
                                v19 = ((v18 << 2) + 59200)
                                store32(((v18 << 2) + 59200), v23)
                                store32(v19 + 8, v33)
                                store32(v19 + 4, v17)
                                store32(v19 + 12, (((arg8 - v23) + ((v12 - v17) * 3)) + 4))
                                v30 = (v12 - v14)
                                v19 = (arg8 - v16)
                                v18 = (v18 + 4)
                                v14 = v25
                                v16 = v22
                                break
                                break
                            v19 = ((v18 << 2) + 59200)
                            store32(((v18 << 2) + 59200), v16)
                            store32(v19 + 8, v33)
                            store32(v19 + 4, v14)
                            store32(v19 + 12, (((v22 - v16) + ((v25 - v14) * 3)) + 13))
                            v30 = (v14 - v12)
                            v19 = (v16 - arg8)
                            v18 = (v18 + 4)
                            v12 = v17
                            arg8 = v23
                            break
                            break
                        v33 = 0
                        store32(59208, 0)
                        store32(59204, v14)
                        store32(59200, v16)
                        store32(59212, (((arg8 - v16) + ((v12 - v14) * 3)) + 13))
                        v25 = (0 - v30)
                        v30 = (0 - v19)
                        v13 = v14
                        arg4 = v16
                        v18 = 4
                        v19 = v12
                        v20 = arg8
                        while True:  # $label93
                            v15 = (v13 + v25)
                            v17 = (arg4 + v30)
                            while True:  # block $label88
                                v23 = (v20 + v30)
                                v22 = (v19 + v25)
                                v34 = load32(((((v20 + v30) + (v24 * (v29 + (v19 + v25)))) << 2) + v26) + 4)
                                if (load32(((((v20 + v30) + (v24 * (v29 + (v19 + v25)))) << 2) + v26) + 4) == v28):
                                    break
                                if (v34 != -1):
                                    if (load8u((v32 + (v34 * 132)) + 125) == 1):
                                        break
                                break
                            v34 = 0
                            while True:  # block $label89
                                while True:  # block $label92
                                    while True:  # block $label91
                                        while True:  # block $label90
                                            v35 = load32((((v17 + ((v15 + v29) * v24)) << 2) + v26) + 4)
                                            if (v28 != load32((((v17 + ((v15 + v29) * v24)) << 2) + v26) + 4)):
                                                if (v35 == -1):
                                                    break
                                                if v34:
                                                    break
                                                if (load8u((v32 + (v35 * 132)) + 125) == 1):
                                                    break
                                                v25 = ((v18 << 2) + 59200)
                                                store32(((v18 << 2) + 59200), arg4)
                                                store32(v25 + 8, v33)
                                                store32(v25 + 4, v13)
                                                store32(v25 + 12, (((v23 - arg4) + ((v22 - v13) * 3)) + 13))
                                                v25 = (v13 - v19)
                                                v30 = (arg4 - v20)
                                                v18 = (v18 + 4)
                                                v19 = v15
                                                v20 = v17
                                                break
                                            if (v34 == 0):
                                                break
                                            break
                                        v25 = ((v18 << 2) + 59200)
                                        store32(((v18 << 2) + 59200), v17)
                                        store32(v25 + 8, v33)
                                        store32(v25 + 4, v15)
                                        store32(v25 + 12, (((v20 - v17) + ((v19 - v15) * 3)) + 4))
                                        v25 = (v19 - v13)
                                        v30 = (v20 - arg4)
                                        v18 = (v18 + 4)
                                        v13 = v22
                                        arg4 = v23
                                        break
                                        break
                                    v13 = v15
                                    arg4 = v17
                                    v19 = v22
                                    v20 = v23
                                    break
                                v34 = 1
                                v33 = (v33 + 1)
                                if (arg8 != v20):
                                    continue
                                if (v12 != v19):
                                    continue
                                if (arg4 != v16):
                                    continue
                                if (v13 != v14):
                                    continue
                                break
                                break
                            break
                        arg8 = ((v18 << 2) + 59200)
                        store32(((v18 << 2) + 59200), arg4)
                        store32(arg8 + 8, v33)
                        store32(arg8 + 4, v13)
                        store32(arg8 + 12, (((v20 - arg4) + ((v19 - v13) * 3)) + 13))
                        v18 = (v18 + 4)
                        v34 = 1
                        break
                        break
                    v14 = v17
                    v16 = v23
                    v12 = v25
                    arg8 = v22
                    break
                v33 = (v33 + 1)
                if (arg8 != v15):
                    continue
                if (v12 != v20):
                    continue
                if (arg4 != v16):
                    continue
                if (v13 != v14):
                    continue
                break
            break
        v20 = 0
        if (v18 == 0):
            break
        v39 = (v18 - 4)
        v40 = ((v18 - 4) if v34 else v18)
        if (((v18 - 4) if v34 else v18) == 0):
            break
        v14 = ((arg2 << 1) | 1)
        v43 = ((v27 << 1) | 1)
        v23 = (((arg2 << 1) | 1) - ((v27 << 1) | 1))
        v17 = ((arg3 << 1) | 1)
        v44 = ((v21 << 1) | 1)
        v22 = (((arg3 << 1) | 1) - ((v21 << 1) | 1))
        v45 = ((arg0 << 1) | 1)
        v25 = (v14 - ((arg0 << 1) | 1))
        v46 = ((arg1 << 1) | 1)
        v32 = (v17 - ((arg1 << 1) | 1))
        v30 = 2147483647
        v27 = 2147483647
        while True:  # $label102
            arg4 = v20
            v20 = (v20 + 4)
            v12 = ((((v20 + 4) % v18) << 2) + 59200)
            v15 = load32(((((v20 + 4) % v18) << 2) + 59200) + 12)
            v21 = (v15 << 2)
            v13 = load32(v12 + 4)
            arg8 = ((((((3591 & 0xFFFFFFFF) >> load32(((((v20 + 4) % v18) << 2) + 59200) + 12)) & 1) + load32(((v15 << 2) + 9344))) + load32(v12 + 4)) << 1)
            v16 = load32(v12)
            v21 = ((load32(v12) + (load32((v21 + 9264)) + (((37449 & 0xFFFFFFFF) >> v15) & 1))) << 1)
            v12 = (arg4 << 2)
            v26 = load32((((arg4 << 2) | 12) + 59200))
            v29 = (v26 << 2)
            v15 = load32((v12 + 59200))
            v41 = ((((((37449 & 0xFFFFFFFF) >> load32((((arg4 << 2) | 12) + 59200))) & 1) + load32(((v26 << 2) + 9264))) + load32((v12 + 59200))) << 1)
            v24 = (((load32(v12) + (load32((v21 + 9264)) + (((37449 & 0xFFFFFFFF) >> v15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> load32((((arg4 << 2) | 12) + 59200))) & 1) + load32(((v26 << 2) + 9264))) + load32((v12 + 59200))) << 1))
            v12 = load32(((v12 | 4) + 59200))
            v42 = ((load32(((v12 | 4) + 59200)) + (load32((v29 + 9344)) + (((3591 & 0xFFFFFFFF) >> v26) & 1))) << 1)
            v26 = (arg8 - ((load32(((v12 | 4) + 59200)) + (load32((v29 + 9344)) + (((3591 & 0xFFFFFFFF) >> v26) & 1))) << 1))
            v29 = (((((((((3591 & 0xFFFFFFFF) >> load32(((((v20 + 4) % v18) << 2) + 59200) + 12)) & 1) + load32(((v15 << 2) + 9344))) + load32(v12 + 4)) << 1) - v17) * (((load32(v12) + (load32((v21 + 9264)) + (((37449 & 0xFFFFFFFF) >> v15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> load32((((arg4 << 2) | 12) + 59200))) & 1) + load32(((v26 << 2) + 9264))) + load32((v12 + 59200))) << 1))) + ((arg8 - ((load32(((v12 | 4) + 59200)) + (load32((v29 + 9344)) + (((3591 & 0xFFFFFFFF) >> v26) & 1))) << 1)) * (v14 - v21)))
            v35 = ((((((((((3591 & 0xFFFFFFFF) >> load32(((((v20 + 4) % v18) << 2) + 59200) + 12)) & 1) + load32(((v15 << 2) + 9344))) + load32(v12 + 4)) << 1) - v17) * (((load32(v12) + (load32((v21 + 9264)) + (((37449 & 0xFFFFFFFF) >> v15) & 1))) << 1) - ((((((37449 & 0xFFFFFFFF) >> load32((((arg4 << 2) | 12) + 59200))) & 1) + load32(((v26 << 2) + 9264))) + load32((v12 + 59200))) << 1))) + ((arg8 - ((load32(((v12 | 4) + 59200)) + (load32((v29 + 9344)) + (((3591 & 0xFFFFFFFF) >> v26) & 1))) << 1)) * (v14 - v21))) > 0)
            v38 = (v29 != 0)
            v29 = (v29 == 0)
            while True:  # block $label97
                while True:  # block $label96
                    v47 = (v17 - arg8)
                    v48 = (v21 - v14)
                    v37 = (((v17 - arg8) * v25) + ((v21 - v14) * v32))
                    v42 = (v17 - v42)
                    v41 = (v41 - v14)
                    v49 = (((v17 - v42) * v25) + ((v41 - v14) * v32))
                    if (((((((v17 - arg8) * v25) + ((v21 - v14) * v32)) != 0) & (((((v17 - v42) * v25) + ((v41 - v14) * v32)) <= 0) ^ (v37 > 0))) if v49 else (v37 == 0)) == 0):
                        v37 = (((arg8 - v46) * v24) + (v26 * (v45 - v21)))
                        if (((v38 & (((((arg8 - v46) * v24) + (v26 * (v45 - v21))) <= 0) ^ v35)) if v37 else v29) == 0):
                            break
                    v37 = ((v23 * v47) + (v22 * v48))
                    v41 = ((v23 * v42) + (v22 * v41))
                    if (((((v23 * v47) + (v22 * v48)) != 0) & ((((v23 * v42) + (v22 * v41)) <= 0) ^ (v37 > 0))) if v41 else (v37 == 0)):
                        break
                    arg8 = (((arg8 - v44) * v24) + (v26 * (v43 - v21)))
                    if ((v38 & (((((arg8 - v44) * v24) + (v26 * (v43 - v21))) <= 0) ^ v35)) if arg8 else v29):
                        break
                    break
                while True:  # block $label100
                    while True:  # block $label99
                        while True:  # block $label98
                            if (v12 == v13):
                                arg8 = (v15 > v16)
                                v13 = (v15 if (v15 > v16) else v16)
                                v21 = (v16 if arg8 else v15)
                                if ((v16 if arg8 else v15) > arg0):
                                    break
                                if (arg0 > v13):
                                    break
                                arg8 = (arg1 - v12)
                                break
                            arg8 = 0
                            if (v15 != v16):
                                break
                            arg8 = (arg0 - v15)
                            arg8 = ((arg0 - v15) * arg8)
                            v16 = (v12 > v13)
                            v21 = (v12 if (v12 > v13) else v13)
                            v16 = (v13 if v16 else v12)
                            if ((((v12 if (v12 > v13) else v13) >= arg1) & (arg1 >= (v13 if v16 else v12))) == 0):
                                v26 = (arg1 - v13)
                                v26 = (((arg1 - v13) * v26) + arg8)
                                v24 = (arg1 - v12)
                                arg8 = (arg8 + ((arg1 - v12) * v24))
                                arg8 = ((((arg1 - v13) * v26) + arg8) if (u(arg8) > u(v26)) else (arg8 + ((arg1 - v12) * v24)))
                            v15 = (arg2 - v15)
                            v15 = ((arg2 - v15) * v15)
                            if ((arg3 <= v21) & (arg3 >= v16)):
                                break
                            v13 = (arg3 - v13)
                            v13 = (((arg3 - v13) * v13) + v15)
                            v12 = (arg3 - v12)
                            v12 = (v15 + ((arg3 - v12) * v12))
                            break
                            break
                        arg8 = (arg1 - v12)
                        arg8 = ((arg1 - v12) * arg8)
                        v26 = (arg0 - v16)
                        v26 = (((arg1 - v12) * arg8) + ((arg0 - v16) * v26))
                        v24 = (arg0 - v15)
                        arg8 = (arg8 + ((arg0 - v15) * v24))
                        break
                    arg8 = ((((arg1 - v12) * arg8) + ((arg0 - v16) * v26)) if (u(arg8) > u(v26)) else (arg8 + ((arg0 - v15) * v24)))
                    while True:  # block $label101
                        if (arg2 < v21):
                            break
                        if (arg2 > v13):
                            break
                        v12 = (arg3 - v12)
                        break
                        break
                    v12 = (arg3 - v12)
                    v12 = ((arg3 - v12) * v12)
                    v13 = (arg2 - v16)
                    v13 = (((arg3 - v12) * v12) + ((arg2 - v16) * v13))
                    v15 = (arg2 - v15)
                    v12 = (v12 + ((arg2 - v15) * v15))
                    break
                v12 = ((((arg3 - v12) * v12) + ((arg2 - v16) * v13)) if (u(v12) > u(v13)) else (v12 + ((arg2 - v15) * v15)))
                v12 = (v12 < v30)
                v30 = (((((arg3 - v12) * v12) + ((arg2 - v16) * v13)) if (u(v12) > u(v13)) else (v12 + ((arg2 - v15) * v15))) if (v12 < v30) else v30)
                v19 = (arg4 if v12 else v19)
                arg8 = (arg8 < v27)
                v27 = (arg8 if (arg8 < v27) else v27)
                v31 = (arg4 if arg8 else v31)
                break
            if (u(v20) < u(v40)):
                continue
            break
        v20 = 0
        if (v30 == 2147483647):
            break
        v20 = (v19 != v31)
        if (v19 == v31):
            break
        if arg11:
            break
        v15 = ((v19 << 2) + 59200)
        v12 = load32(((v19 << 2) + 59200))
        v16 = load32(v15 + 8)
        arg4 = load32(((((v19 + 4) % v18) << 2) + 59200))
        v22 = ((v31 + 4) % v18)
        arg8 = load32(((((v31 + 4) % v18) << 2) + 59200))
        v14 = ((v31 << 2) + 59200)
        arg11 = load32(((v31 << 2) + 59200))
        v20 = 0
        while True:  # block $label104
            v13 = load32(v15 + 4)
            v15 = load32(((((v19 + 5) % v18) << 2) + 59200))
            if (load32(v15 + 4) == load32(((((v19 + 5) % v18) << 2) + 59200))):
                while True:  # block $label103
                    if ((arg4 if (arg4 < v12) else v12) > arg2):
                        break
                    if ((v12 if (arg4 < v12) else arg4) < arg2):
                        break
                    arg2 = (arg2 - v12)
                    arg2 = (arg2 >> 31)
                    break
                    break
                while True:  # block $label105
                    if (arg4 >= v12):
                        break
                    if (arg2 >= arg4):
                        break
                    break
                    break
                break
            if (arg4 != v12):
                break
            while True:  # block $label106
                if ((v15 if (v13 > v15) else v13) > arg3):
                    break
                if ((v13 if (v13 > v15) else v15) < arg3):
                    break
                arg2 = (arg3 - v13)
                arg2 = (arg2 >> 31)
                break
                break
            while True:  # block $label107
                if (v13 <= v15):
                    break
                if (arg3 >= v15):
                    break
                break
                break
            break
        arg4 = ((((v15 - v13) if (arg3 > v15) else 0) if (v13 < v15) else 0) + v16)
        while True:  # block $label109
            arg3 = load32(v14 + 4)
            arg2 = load32(((((v31 + 5) % v18) << 2) + 59200))
            if (load32(v14 + 4) == load32(((((v31 + 5) % v18) << 2) + 59200))):
                while True:  # block $label108
                    if ((arg8 if (arg8 < arg11) else arg11) > arg0):
                        break
                    if ((arg11 if (arg8 < arg11) else arg8) < arg0):
                        break
                    arg2 = (arg0 - arg11)
                    arg2 = (arg2 >> 31)
                    break
                    break
                while True:  # block $label110
                    if (arg8 >= arg11):
                        break
                    if (arg0 >= arg8):
                        break
                    break
                    break
                break
            if (arg8 != arg11):
                break
            while True:  # block $label111
                if ((arg2 if (arg2 < arg3) else arg3) > arg1):
                    break
                if ((arg3 if (arg2 < arg3) else arg2) < arg1):
                    break
                arg2 = (arg1 - arg3)
                arg2 = (arg2 >> 31)
                break
                break
            while True:  # block $label112
                if (arg2 >= arg3):
                    break
                if (arg1 >= arg2):
                    break
                break
                break
            break
        arg2 = ((((arg2 - arg3) if (arg1 > arg2) else 0) if (arg2 > arg3) else 0) + load32(((v31 << 2) + 59208)))
        arg2 = (arg2 - arg4)
        arg3 = ((((arg1 - arg3) ^ (arg2 >> 31)) - arg2) if ((arg2 - arg4) < 0) else (((arg3 - arg2) != ((((arg2 - arg3) if (arg1 > arg2) else 0) if (arg2 > arg3) else 0) + load32(((v31 << 2) + 59208)))) << 2))
        arg3 = (arg2 >> 31)
        arg2 = ((arg2 ^ (arg2 >> 31)) - arg3)
        arg2 = (v33 - arg2)
        arg2 = (arg2 >> 31)
        v15 = (((((arg1 - arg3) ^ (arg2 >> 31)) - arg2) if ((arg2 - arg4) < 0) else (((arg3 - arg2) != ((((arg2 - arg3) if (arg1 > arg2) else 0) if (arg2 > arg3) else 0) + load32(((v31 << 2) + 59208)))) << 2)) if v34 else (arg3 if (u(((arg2 ^ (arg2 >> 31)) - arg3)) < u((((v33 - arg2) ^ (arg2 >> 31)) - arg2))) else (0 - arg3)))
        if ((((((arg1 - arg3) ^ (arg2 >> 31)) - arg2) if ((arg2 - arg4) < 0) else (((arg3 - arg2) != ((((arg2 - arg3) if (arg1 > arg2) else 0) if (arg2 > arg3) else 0) + load32(((v31 << 2) + 59208)))) << 2)) if v34 else (arg3 if (u(((arg2 ^ (arg2 >> 31)) - arg3)) < u((((v33 - arg2) ^ (arg2 >> 31)) - arg2))) else (0 - arg3))) == 0):
            break
        while True:  # block $label118
            while True:  # $label119
                while True:  # block $label117
                    while True:  # block $label113
                        arg2 = ((v19 << 2) + 59200)
                        arg3 = load32(((v19 << 2) + 59200) + 12)
                        if (load32(((v19 << 2) + 59200) + 12) > 8):
                            break
                        while True:  # block $label114
                            arg4 = (v12 - arg0)
                            arg4 = (arg4 >> 31)
                            arg4 = (((v12 - arg0) ^ (arg4 >> 31)) - arg4)
                            arg2 = load32(arg2 + 4)
                            arg8 = (load32(arg2 + 4) - arg1)
                            arg8 = (arg8 >> 31)
                            arg8 = (((load32(arg2 + 4) - arg1) ^ (arg8 >> 31)) - arg8)
                            if (u(((((v12 - arg0) ^ (arg4 >> 31)) - arg4) if (u(arg4) > u(arg8)) else (((load32(arg2 + 4) - arg1) ^ (arg8 >> 31)) - arg8))) < u(56)):
                                break
                            if (v19 == v31):
                                break
                            if (v19 == v22):
                                break
                            arg4 = (v19 - v31)
                            arg4 = (arg4 >> 31)
                            arg4 = (((v19 - v31) ^ (arg4 >> 31)) - arg4)
                            if ((((v19 - v31) ^ (arg4 >> 31)) - arg4) == 4):
                                break
                            if (arg4 != v39):
                                break
                            break
                        v20 = ((arg0 << 8) | 128)
                        arg4 = (arg3 << 2)
                        v25 = load32(((arg3 << 2) + 9264))
                        v30 = (load32(((arg3 << 2) + 9264)) + (((((37449 & 0xFFFFFFFF) >> arg3) & 1) + v12) << 8))
                        v21 = (((arg0 << 8) | 128) - (load32(((arg3 << 2) + 9264)) + (((((37449 & 0xFFFFFFFF) >> arg3) & 1) + v12) << 8)))
                        v13 = ((arg1 << 8) | 128)
                        v33 = load32((arg4 + 9344))
                        v32 = (load32((arg4 + 9344)) + (((((3591 & 0xFFFFFFFF) >> arg3) & 1) + arg2) << 8))
                        v27 = (((arg1 << 8) | 128) - (load32((arg4 + 9344)) + (((((3591 & 0xFFFFFFFF) >> arg3) & 1) + arg2) << 8)))
                        arg3 = (v19 - v15)
                        v26 = ((v18 if (arg3 < 0) else (0 - (v18 if ((v19 - v15) >= v18) else 0))) + arg3)
                        arg4 = ((v18 if (arg3 < 0) else (0 - (v18 if ((v19 - v15) >= v18) else 0))) + arg3)
                        arg8 = load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((v19 - v15) >= v18) else 0))) + arg3) << 2) + 59200))
                        while True:  # $label115
                            arg3 = (arg4 + v15)
                            arg3 = ((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3)
                            arg11 = ((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200)
                            v14 = load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)
                            v17 = (v14 << 2)
                            v16 = ((((((3591 & 0xFFFFFFFF) >> load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)) & 1) + load32(((v14 << 2) + 9344))) + load32(arg11 + 4)) << 8)
                            arg11 = load32(arg11)
                            v14 = ((load32(arg11) + (load32((v17 + 9264)) + (((37449 & 0xFFFFFFFF) >> v14) & 1))) << 8)
                            v17 = (((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)) & 1) + load32(((v14 << 2) + 9344))) + load32(arg11 + 4)) << 8)) * v21) + ((((load32(arg11) + (load32((v17 + 9264)) + (((37449 & 0xFFFFFFFF) >> v14) & 1))) << 8) - v20) * v27))
                            v24 = ((arg4 << 2) + 59200)
                            v23 = load32(((arg4 << 2) + 59200) + 12)
                            v29 = (v23 << 2)
                            v24 = ((((((3591 & 0xFFFFFFFF) >> load32(((arg4 << 2) + 59200) + 12)) & 1) + load32(((v23 << 2) + 9344))) + load32(v24 + 4)) << 8)
                            arg8 = (((load32((v29 + 9264)) + (((37449 & 0xFFFFFFFF) >> v23) & 1)) + arg8) << 8)
                            v23 = (((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((arg4 << 2) + 59200) + 12)) & 1) + load32(((v23 << 2) + 9344))) + load32(v24 + 4)) << 8)) * v21) + (((((load32((v29 + 9264)) + (((37449 & 0xFFFFFFFF) >> v23) & 1)) + arg8) << 8) - v20) * v27))
                            v17 = (v14 - arg8)
                            v23 = (v16 - v24)
                            arg8 = (((v14 - arg8) * (v16 - v13)) + ((v16 - v24) * (v20 - v14)))
                            v16 = (((v16 - v32) * v17) + (v23 * (v30 - v14)))
                            v16 = (((((((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)) & 1) + load32(((v14 << 2) + 9344))) + load32(arg11 + 4)) << 8)) * v21) + ((((load32(arg11) + (load32((v17 + 9264)) + (((37449 & 0xFFFFFFFF) >> v14) & 1))) << 8) - v20) * v27)) != 0) & (((((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((arg4 << 2) + 59200) + 12)) & 1) + load32(((v23 << 2) + 9344))) + load32(v24 + 4)) << 8)) * v21) + (((((load32((v29 + 9264)) + (((37449 & 0xFFFFFFFF) >> v23) & 1)) + arg8) << 8) - v20) * v27)) <= 0) ^ (v17 > 0))) if v23 else (v17 == 0)) | ((((((v14 - arg8) * (v16 - v13)) + ((v16 - v24) * (v20 - v14))) != 0) & (((((v16 - v32) * v17) + (v23 * (v30 - v14))) <= 0) ^ (arg8 > 0))) if v16 else (arg8 == 0)))
                            if ((((((((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((((v18 if (arg3 < 0) else (0 - (v18 if ((arg4 + v15) >= v18) else 0))) + arg3) << 2) + 59200) + 12)) & 1) + load32(((v14 << 2) + 9344))) + load32(arg11 + 4)) << 8)) * v21) + ((((load32(arg11) + (load32((v17 + 9264)) + (((37449 & 0xFFFFFFFF) >> v14) & 1))) << 8) - v20) * v27)) != 0) & (((((v13 - ((((((3591 & 0xFFFFFFFF) >> load32(((arg4 << 2) + 59200) + 12)) & 1) + load32(((v23 << 2) + 9344))) + load32(v24 + 4)) << 8)) * v21) + (((((load32((v29 + 9264)) + (((37449 & 0xFFFFFFFF) >> v23) & 1)) + arg8) << 8) - v20) * v27)) <= 0) ^ (v17 > 0))) if v23 else (v17 == 0)) | ((((((v14 - arg8) * (v16 - v13)) + ((v16 - v24) * (v20 - v14))) != 0) & (((((v16 - v32) * v17) + (v23 * (v30 - v14))) <= 0) ^ (arg8 > 0))) if v16 else (arg8 == 0))) == 1):
                                v14 = (arg4 != v31)
                                arg8 = arg11
                                arg4 = arg3
                                if v14:
                                    continue
                            break
                        if (v16 ^ 1):
                            break
                        while True:  # block $label116
                            if ((v19 == 0) & v34):
                                arg8 = v12
                                v12 = arg2
                                break
                            arg3 = ((v26 << 2) + 59200)
                            arg4 = load32(((v26 << 2) + 59200))
                            arg8 = ((-1 if (arg4 < v12) else (load32(((v26 << 2) + 59200)) != v12)) + v12)
                            arg3 = load32(arg3 + 4)
                            v12 = ((-1 if (arg2 > arg3) else (load32(arg3 + 4) != arg2)) + arg2)
                            store8(arg10, (((((-1 if (arg4 < v12) else (load32(((v26 << 2) + 59200)) != v12)) + v12) - (v12 + v25)) + ((((-1 if (arg2 > arg3) else (load32(arg3 + 4) != arg2)) + arg2) - (arg2 + v33)) * 3)) + 4))
                            break
                        store32(arg9, ((v12 << 16) + arg8))
                        if (arg0 != arg8):
                            break
                        if (arg1 != v12):
                            break
                        store32(arg9, 0)
                        break
                        break
                    if (v19 == v31):
                        v20 = 0
                        break
                    else:
                        arg2 = (((v19 if v19 else v18) if (v15 < 0) else v19) + v15)
                        v19 = ((((v19 if v19 else v18) if (v15 < 0) else v19) + v15) if (arg2 != v18) else 0)
                        v12 = load32(((((((v19 if v19 else v18) if (v15 < 0) else v19) + v15) if (arg2 != v18) else 0) << 2) + 59200))
                        continue
                    raise RuntimeError('unreachable')
                    break
                break
            break
        v20 = 1
        break
    G.global0 = (v36 + 16)
    return v20

# ------------------------------------------------------------
# $func178
# ------------------------------------------------------------
def func178(arg0):
    v8 = load32(arg0 + 44)
    v11 = (load32(arg0 + 44) - 262)
    v2 = load32(arg0 + 116)
    while True:  # $label10
        v7 = load32(arg0 + 108)
        v6 = (load32(arg0 + 60) - (v2 + load32(arg0 + 108)))
        if (u((v11 + load32(arg0 + 44))) <= u(v7)):
            v1 = load32(arg0 + 56)
            store32(arg0 + 112, (load32(arg0 + 112) - v8))
            v7 = (load32(arg0 + 108) - v8)
            store32(arg0 + 108, (load32(arg0 + 108) - v8))
            store32(arg0 + 92, (load32(arg0 + 92) - v8))
            if (u(v7) < u(load32(arg0 + 5812))):
                store32(arg0 + 5812, v7)
            v1 = load32(arg0 + 76)
            v5 = (load32(arg0 + 76) - 1)
            v4 = (load32(arg0 + 68) + (v1 << 1))
            v3 = load32(arg0 + 44)
            v2 = 0
            v9 = (v1 & 3)
            if (v1 & 3):
                while True:  # $label0
                    v4 = (v4 - 2)
                    v10 = load16u(v4)
                    v12 = (load16u(v4) - v3)
                    store16((v4 - 2), ((load16u(v4) - v3) if (u(v10) >= u(v12)) else 0))
                    v1 = (v1 - 1)
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v9):
                        continue
                    break
            if (u(v5) >= u(3)):
                while True:  # $label1
                    v2 = (v4 - 2)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 2), ((load16u(v2) - v3) if (u(v2) >= u(v5)) else 0))
                    v2 = (v4 - 4)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 4), ((load16u(v2) - v3) if (u(v2) >= u(v5)) else 0))
                    v2 = (v4 - 6)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 6), ((load16u(v2) - v3) if (u(v2) >= u(v5)) else 0))
                    v4 = (v4 - 8)
                    v2 = load16u(v4)
                    v5 = (load16u(v4) - v3)
                    store16((v4 - 8), ((load16u(v4) - v3) if (u(v2) >= u(v5)) else 0))
                    v1 = (v1 - 4)
                    if (v1 - 4):
                        continue
                    break
            v4 = (load32(arg0 + 64) + (v3 << 1))
            v2 = 0
            v1 = v3
            v5 = (v3 & 3)
            if (v3 & 3):
                while True:  # $label2
                    v4 = (v4 - 2)
                    v9 = load16u(v4)
                    v10 = (load16u(v4) - v3)
                    store16((v4 - 2), ((load16u(v4) - v3) if (u(v9) >= u(v10)) else 0))
                    v1 = (v1 - 1)
                    v2 = (v2 + 1)
                    if ((v2 + 1) != v5):
                        continue
                    break
            if (u((v3 - 1)) >= u(3)):
                while True:  # $label3
                    v2 = (v4 - 2)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 2), ((load16u(v2) - v3) if (u(v2) >= u(v5)) else 0))
                    v2 = (v4 - 4)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 4), ((load16u(v2) - v3) if (u(v2) >= u(v5)) else 0))
                    v2 = (v4 - 6)
                    v2 = load16u(v2)
                    v5 = (load16u(v2) - v3)
                    store16((v4 - 6), ((load16u(v2) - v3) if (u(v2) >= u(v5)) else 0))
                    v4 = (v4 - 8)
                    v2 = load16u(v4)
                    v5 = (load16u(v4) - v3)
                    store16((v4 - 8), ((load16u(v4) - v3) if (u(v2) >= u(v5)) else 0))
                    v1 = (v1 - 4)
                    if (v1 - 4):
                        continue
                    break
            v6 = (v6 + v8)
        while True:  # block $label4
            v1 = load32(arg0)
            v4 = load32(load32(arg0) + 4)
            if (load32(load32(arg0) + 4) == 0):
                break
            v2 = load32(arg0 + 116)
            v3 = (v4 if (u(v4) < u(v6)) else v6)
            if (v4 if (u(v4) < u(v6)) else v6):
                v6 = load32(arg0 + 56)
                store32(v1 + 4, (v4 - v3))
                v4 = func35(((v6 + v7) + v2), load32(v1), v3)
                while True:  # block $label7
                    while True:  # block $label6
                        while True:  # block $label5
                            # br_table[(load32(load32(v1 + 28) + 24) - 1)]
                            break
                            break
                        store32(v1 + 48, func89(load32(v1 + 48), v4, v3))
                        break
                        break
                    store32(v1 + 48, func43(load32(v1 + 48), v4, v3))
                    break
                store32(v1, (load32(v1) + v3))
                store32(v1 + 8, (load32(v1 + 8) + v3))
            else:
            v2 = (v2 + v3)
            store32(load32(arg0 + 116) + 116, (v2 + v3))
            while True:  # block $label8
                v4 = load32(arg0 + 5812)
                if (u((load32(arg0 + 5812) + v2)) < u(3)):
                    break
                v7 = load32(arg0 + 56)
                v3 = (load32(arg0 + 108) - v4)
                v1 = (load32(arg0 + 56) + (load32(arg0 + 108) - v4))
                v6 = load8u((load32(arg0 + 56) + (load32(arg0 + 108) - v4)))
                store32(arg0 + 72, load8u((load32(arg0 + 56) + (load32(arg0 + 108) - v4))))
                v5 = load32(arg0 + 84)
                v6 = load32(arg0 + 88)
                v1 = (load32(arg0 + 84) & (load8u(v1 + 1) ^ (v6 << load32(arg0 + 88))))
                store32(arg0 + 72, (load32(arg0 + 84) & (load8u(v1 + 1) ^ (v6 << load32(arg0 + 88)))))
                while True:  # $label9
                    if (v4 == 0):
                        break
                    v1 = ((load8u((v3 + v7) + 2) ^ (v1 << v6)) & v5)
                    store32(arg0 + 72, ((load8u((v3 + v7) + 2) ^ (v1 << v6)) & v5))
                    v9 = (load32(arg0 + 68) + (v1 << 1))
                    store16((load32(arg0 + 64) + ((load32(arg0 + 52) & v3) << 1)), load16u((load32(arg0 + 68) + (v1 << 1))))
                    store16(v9, v3)
                    v4 = (v4 - 1)
                    store32(arg0 + 5812, (v4 - 1))
                    v3 = (v3 + 1)
                    if (u((v2 + v4)) > u(2)):
                        continue
                    break
                break
            if (u(v2) > u(261)):
                break
            if load32(load32(arg0) + 4):
                continue
            break
        break
    while True:  # block $label11
        v4 = load32(arg0 + 60)
        v1 = load32(arg0 + 5824)
        if (u(load32(arg0 + 60)) <= u(load32(arg0 + 5824))):
            break
        while True:  # block $label12
            v3 = (load32(arg0 + 116) + load32(arg0 + 108))
            if (u((load32(arg0 + 116) + load32(arg0 + 108))) > u(v1)):
                v1 = (v4 - v3)
                v1 = (258 if (u(v1) >= u(258)) else (v4 - v3))
                func98((load32(arg0 + 56) + v3), 0, (258 if (u(v1) >= u(258)) else (v4 - v3)))
                break
            v3 = (v3 + 258)
            if (u((v3 + 258)) <= u(v1)):
                break
            v3 = (v3 - v1)
            v1 = (v4 - v1)
            v1 = ((v3 - v1) if (u(v1) > u(v3)) else (v4 - v1))
            func98((load32(arg0 + 56) + v1), 0, ((v3 - v1) if (u(v1) > u(v3)) else (v4 - v1)))
            break
        store32((v1 + v3) + 5824, (load32(arg0 + 5824) + v1))
        break
    return arg0

# ------------------------------------------------------------
# $func179
# ------------------------------------------------------------
def func179(arg0, arg1):
    while True:  # block $label6
        while True:  # block $label0
            if (arg0 == 0):
                break
            if (arg1 == 0):
                break
            if (G.global4 if (load32(arg0 + 52) & 64) else 0):
                break
            v2 = func252(1, 208)
            if (func252(1, 208) == 0):
                break
            v3 = load32(52364)
            store32(52364, (load32(52364) + 1))
            store32(v2, v3)
            store32(v2 + 4, load32(arg0 + 32))
            store32(v2 + 168, load32(arg0 + 56))
            store32(v2 + 164, load32(arg0 + 52))
            store32(v2 + 172, load32(arg0 + 60))
            store32(v2 + 196, load32(arg0 + 84))
            store32(v2 + 200, load32(arg0 + 88))
            while True:  # block $label2
                while True:  # block $label1
                    v5 = (v2 + 112)
                    v3 = arg0
                    if (((v2 + 112) ^ arg0) & 3):
                        v4 = load8u(v3)
                        break
                    if (v3 & 3):
                        while True:  # $label3
                            v4 = load8u(v3)
                            store8(v5, load8u(v3))
                            if (v4 == 0):
                                break
                            v5 = (v5 + 1)
                            v3 = (v3 + 1)
                            if ((v3 + 1) & 3):
                                continue
                            break
                    v4 = load32(v3)
                    if (((load32(v3) ^ -1) & (v4 - 16843009)) & -2139062144):
                        break
                    while True:  # $label4
                        store32(v5, v4)
                        v4 = load32(v3 + 4)
                        v5 = (v5 + 4)
                        v3 = (v3 + 4)
                        if ((((v4 - 16843009) & (v4 ^ -1)) & -2139062144) == 0):
                            continue
                        break
                    break
                store8(v5, v4)
                if ((v4 & 255) == 0):
                    break
                while True:  # $label5
                    v4 = load8u(v3 + 1)
                    store8(v5 + 1, load8u(v3 + 1))
                    v5 = (v5 + 1)
                    v3 = (v3 + 1)
                    if v4:
                        continue
                    break
                break
            store32(v2 + 152, load32(arg0 + 40))
            store32(v2 + 148, load32(arg0 + 36))
            store32(v2 + 156, load32(arg0 + 44))
            store32(v2 + 160, load32(arg0 + 48))
            arg1 = func121(arg1)
            store32(v2 + 8, func121(arg1))
            if (arg1 == 0):
                func246(v2)
                return
            arg1 = load32(arg0 + 64)
            if load32(arg0 + 64):
                arg1 = func121(arg1)
                store32(v2 + 176, func121(arg1))
                if (arg1 == 0):
                    break
            arg1 = load32(arg0 + 68)
            if load32(arg0 + 68):
                arg1 = func121(arg1)
                store32(v2 + 180, func121(arg1))
                if (arg1 == 0):
                    break
            arg1 = load32(arg0 + 72)
            if load32(arg0 + 72):
                arg1 = func121(arg1)
                store32(v2 + 184, func121(arg1))
                if (arg1 == 0):
                    break
            arg1 = load32(arg0 + 80)
            if load32(arg0 + 80):
                arg1 = func121(arg1)
                store32(v2 + 192, func121(arg1))
                if (arg1 == 0):
                    break
            v5 = load32(arg0 + 76)
            if load32(arg0 + 76):
                arg1 = 0
                while True:  # $label7
                    arg0 = arg1
                    arg1 = (arg1 + 1)
                    if load32((v5 + (arg0 << 2))):
                        continue
                    break
                v3 = func252(1, ((arg0 << 2) + 4))
                if (func252(1, ((arg0 << 2) + 4)) == 0):
                    break
                if arg0:
                    arg1 = 0
                    while True:  # $label9
                        v4 = (arg1 << 2)
                        v4 = func121(load32((v4 + v5)))
                        store32((v3 + (arg1 << 2)), func121(load32((v4 + v5))))
                        if (v4 == 0):
                            if arg1:
                                arg0 = 0
                                while True:  # $label8
                                    arg0 = (arg0 + 1)
                                    if ((arg0 + 1) != arg1):
                                        continue
                                    break
                            break
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != arg0):
                            continue
                        break
                store32((v3 + (arg0 << 2)), 0)
                store32(v2 + 188, v3)
            a_m(v2)
            break
        return
        break
    func246(v2)

# ------------------------------------------------------------
# $func180
# ------------------------------------------------------------
def func180(arg0, arg1):
    while True:  # block $label1
        while True:  # block $label0
            if (load32(38604) == arg1):
                break
            if (load32(38608) == arg1):
                break
            if (load32(38612) == arg1):
                break
            if (load32(38616) == arg1):
                break
            if (load32(38624) == arg1):
                break
            if (load32(38628) == arg1):
                break
            if (load32(38632) == arg1):
                break
            if (load32(39056) != arg1):
                break
            break
        arg1 = (arg0 + 281808)
        v2 = (load32(9561068) << 2)
        v3 = (load32(9561064) << 2)
        v4 = (load32(9561060) << 2)
        v5 = (load32(9561056) << 2)
        v6 = (load32(9561052) << 2)
        v7 = (load32(9561048) << 2)
        v8 = (load32(9561044) << 2)
        v9 = (load32(9561040) << 2)
        arg0 = (arg0 + 282828)
        return ((load32(((arg0 + 281808) + (load32(9561068) << 2))) + ((load32((arg1 + (load32(9561064) << 2))) + ((load32((arg1 + (load32(9561060) << 2))) + ((load32((arg1 + (load32(9561056) << 2))) + ((load32((arg1 + (load32(9561052) << 2))) + ((load32((arg1 + (load32(9561048) << 2))) + ((load32((arg1 + (load32(9561044) << 2))) + (load32((arg1 + (load32(9561040) << 2))) + load32(((arg0 + 282828) + v9)))) + load32((arg0 + v8)))) + load32((arg0 + v7)))) + load32((arg0 + v6)))) + load32((arg0 + v5)))) + load32((arg0 + v4)))) + load32((arg0 + v3)))) + load32((arg0 + v2)))
        break
    arg0 = (arg0 + (arg1 << 2))
    return (load32(((arg0 + (arg1 << 2)) + 282828)) + load32((arg0 + 281808)))

# ------------------------------------------------------------
# $func181
# ------------------------------------------------------------
def func181(arg0, arg1, arg2):
    while True:  # block $label0
        v4 = load32(arg0 + 281796)
        if (load32(arg0 + 281796) == 0):
            v3 = func26(16)
            store32(func26(16) + 4, 20)
            store32(v3, func26(80))
            store64(v3 + 8, 85899345920)
            store32(arg0 + 281796, v3)
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
            v3 = load32(arg0 + 281796)
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
# $func182
# ------------------------------------------------------------
def func182():
    v0 = 3
    if (u(load32(9671136)) > u(3)):
        while True:  # $label0
            v0 = (v0 + 1)
            if (u((v0 + 1)) < u(load32(9671136))):
                continue
            break
    while True:  # block $label1
        v6 = load32(9142892)
        if (load32(9142892) == 0):
            break
        v4 = load32(9561692)
        while True:  # $label2
            v0 = 0
            while True:  # $label3
                v2 = (v4 + (v5 * 286704))
                v3 = ((v4 + (v5 * 286704)) + (v0 << 2))
                v1 = load32((((v4 + (v5 * 286704)) + (v0 << 2)) + 285656))
                if load32((((v4 + (v5 * 286704)) + (v0 << 2)) + 285656)):
                    store32(v1 + 8, 0)
                v1 = load32((v3 + 284636))
                if load32((v3 + 284636)):
                    store32(v1 + 8, 0)
                v1 = (v0 | 1)
                if ((v0 | 1) == 255):
                    v5 = (v5 + 1)
                    if ((v5 + 1) != v6):
                        continue
                    break
                v3 = (v2 + (v1 << 2))
                v1 = load32(((v2 + (v1 << 2)) + 285656))
                if load32(((v2 + (v1 << 2)) + 285656)):
                    store32(v1 + 8, 0)
                v1 = load32((v3 + 284636))
                if load32((v3 + 284636)):
                    store32(v1 + 8, 0)
                v0 = (v0 + 2)
                continue
                break
            raise RuntimeError('unreachable')
            break
        raise RuntimeError('unreachable')
        break
    v4 = load32(9671128)
    if load32(9671128):
        v3 = (v4 - 4)
        v1 = load32((v4 - 4))
        if load32((v4 - 4)):
            v0 = (v4 + (v1 * 132))
            while True:  # $label4
                v1 = (v0 - 132)
                v2 = load32((v0 - 132))
                if load32((v0 - 132)):
                    store32((v0 - 128), v2)
                v0 = v1
                if (v1 != v4):
                    continue
                break
        store32(9671128, 0)
    store32(9671132, 10000)
    v1 = func26(1320004)
    store32(func26(1320004), 10000)
    v3 = (v1 + 1320004)
    v1 = (v1 + 4)
    v0 = (v1 + 4)
    while True:  # $label5
        # TODO: memory.fill []
        v2 = func26(4)
        store32(v0 + 4, func26(4))
        store32(v0, v2)
        store32(v0 + 8, (v2 + 4))
        v0 = (v0 + 132)
        if ((v0 + 132) != v3):
            continue
        break
    store32(9671128, v1)
    store64(9671136, 42949672960003)
    store32(9163776, 4)
    store32(9684796, 0)
    store32(load32(9681936) + 8, 0)
    store32(9299880, 0)

# ------------------------------------------------------------
# $func183
# ------------------------------------------------------------
def func183(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    v13 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v9 = 1
    while True:  # block $label0
        v20 = load8u(arg0 + 125)
        if (load8u(arg0 + 125) == 3):
            break
        v9 = load32(((arg1 + (arg2 * 36)) + 269376))
        v9 = (load32(((arg1 + (arg2 * 36)) + 269376)) if v9 else 100)
        v12 = ((arg2 * 404) + 9568096)
        store32(v13, (((load32(((arg1 + (arg2 * 36)) + 269376)) if v9 else 100) * load32(((arg2 * 404) + 9568096) + 68)) // 100))
        store32(v13 + 4, ((load32(v12 + 72) * v9) // 100))
        store32(v13 + 8, ((load32(v12 + 76) * v9) // 100))
        store32(v13 + 12, ((load32(v12 + 80) * v9) // 100))
        while True:  # block $label32
            while True:  # block $label2
                if (arg3 == 0):
                    while True:  # block $label1
                        if (load32(v12 + 264) != 3):
                            break
                        if arg5:
                            break
                        v9 = 0
                        arg3 = (arg1 + (arg2 << 2))
                        if load32(((arg1 + (arg2 << 2)) + 282828)):
                            break
                        if load32((arg3 + 281808)):
                            break
                        break
                    arg7 = load32(arg0 + 20)
                    if (load32(arg0 + 20) == 0):
                        arg7 = func26(16)
                        store32(func26(16) + 4, 16)
                        store32(arg7, func26(64))
                        store64(arg7 + 8, 68719476736)
                        store32(arg0 + 20, arg7)
                        break
                    if (arg4 == 0):
                        break
                    if (arg6 == 0):
                        break
                    arg3 = load32(arg7 + 8)
                    if (load32(arg7 + 8) == 0):
                        break
                    v11 = (arg2 + 2147483647)
                    v10 = load32(arg7)
                    v9 = 0
                    arg6 = 0
                    while True:  # $label3
                        if (load32((v10 + (arg6 << 2))) == v11):
                            break
                        arg6 = (arg6 + 1)
                        if (arg3 != (arg6 + 1)):
                            continue
                        break
                    break
                arg5 = load32(arg0 + 20)
                if (load32(arg0 + 20) == 0):
                    v9 = 0
                    break
                while True:  # block $label4
                    arg4 = load32(arg5 + 8)
                    if (load32(arg5 + 8) == 0):
                        arg8 = 0
                        v11 = -1
                        break
                    v14 = (arg4 & 1)
                    arg6 = load32(arg5)
                    while True:  # block $label5
                        if (arg4 == 1):
                            v11 = -1
                            v9 = 0
                            arg8 = 0
                            break
                        v16 = (arg4 & -2)
                        v11 = -1
                        v9 = 0
                        arg8 = 0
                        arg4 = 0
                        while True:  # $label6
                            v15 = (v9 | 1)
                            v10 = load32((arg6 + ((v9 | 1) << 2)))
                            v17 = (u(load32((arg6 + ((v9 | 1) << 2)))) > u(2147483646))
                            v12 = load32((arg6 + (v9 << 2)))
                            v20 = (u(load32((arg6 + (v9 << 2)))) > u(2147483646))
                            v12 = (((v12 - 2147483647) if v20 else v12) == arg2)
                            v10 = (((v10 - 2147483647) if v17 else v10) == arg2)
                            arg8 = ((u(load32((arg6 + ((v9 | 1) << 2)))) > u(2147483646)) if (((v10 - 2147483647) if v17 else v10) == arg2) else ((u(load32((arg6 + (v9 << 2)))) > u(2147483646)) if (((v12 - 2147483647) if v20 else v12) == arg2) else arg8))
                            v11 = (v15 if v10 else (v9 if v12 else v11))
                            v9 = (v9 + 2)
                            arg4 = (arg4 + 2)
                            if ((arg4 + 2) != v16):
                                continue
                            break
                        break
                    if (v14 == 0):
                        break
                    arg4 = load32((arg6 + (v9 << 2)))
                    arg6 = (u(load32((arg6 + (v9 << 2)))) > u(2147483646))
                    arg4 = (((arg4 - 2147483647) if arg6 else arg4) == arg2)
                    arg8 = ((u(load32((arg6 + (v9 << 2)))) > u(2147483646)) if (((arg4 - 2147483647) if arg6 else arg4) == arg2) else arg8)
                    v11 = (v9 if arg4 else v11)
                    break
                while True:  # block $label7
                    arg4 = load32(arg1 + 281796)
                    if (load32(arg1 + 281796) == 0):
                        break
                    arg6 = load32(arg4 + 8)
                    if (load32(arg4 + 8) == 0):
                        break
                    v10 = load32(arg0 + 28)
                    v12 = load32(arg4)
                    v9 = 0
                    while True:  # $label11
                        while True:  # block $label8
                            v14 = (v9 << 2)
                            if (load32((v12 + (v9 << 2))) != v10):
                                break
                            if (load32((v12 + (v14 | 4))) != arg2):
                                break
                            v10 = (arg6 - 1)
                            store32(arg4 + 8, (arg6 - 1))
                            if (u(v9) < u(v10)):
                                arg6 = v9
                                while True:  # $label9
                                    arg6 = (arg6 + 1)
                                    store32((v12 + (arg6 << 2)), load32((v12 + ((arg6 + 1) << 2))))
                                    v10 = load32(arg4 + 8)
                                    if (u(arg6) < u(load32(arg4 + 8))):
                                        continue
                                    break
                            arg6 = (v10 - 1)
                            store32(arg4 + 8, (v10 - 1))
                            if (u(arg6) > u(v9)):
                                while True:  # $label10
                                    v9 = (v9 + 1)
                                    store32((v12 + (v9 << 2)), load32((v12 + ((v9 + 1) << 2))))
                                    if (u(v9) < u(load32(arg4 + 8))):
                                        continue
                                    break
                            arg6 = ((arg1 + (arg2 << 2)) + 282828)
                            store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg6) - 1))
                            break
                            break
                        v9 = (v9 + 2)
                        if (u((v9 + 2)) < u(arg6)):
                            continue
                        break
                    break
                while True:  # block $label12
                    v14 = ((arg2 * 404) + 9568096)
                    if (load32(((arg2 * 404) + 9568096) + 264) != 3):
                        break
                    arg6 = load32(v14 + 244)
                    if (load32(v14 + 244) == 0):
                        break
                    v17 = load32(((arg2 * 404) + 9568096) + 240)
                    v16 = 0
                    while True:  # $label18
                        while True:  # block $label13
                            if (arg4 == 0):
                                break
                            v10 = load32(arg4 + 8)
                            if (load32(arg4 + 8) == 0):
                                break
                            v15 = load32(((load32((v17 + (v16 << 2))) * 132) + 9216080) + 4)
                            v20 = load32(arg0 + 28)
                            v12 = load32(arg4)
                            v9 = 0
                            while True:  # $label17
                                while True:  # block $label14
                                    v18 = (v9 << 2)
                                    if (load32((v12 + (v9 << 2))) != v20):
                                        break
                                    if (load32((v12 + (v18 | 4))) != v15):
                                        break
                                    v10 = (v10 - 1)
                                    store32(arg4 + 8, (v10 - 1))
                                    arg6 = v9
                                    if (u(v9) < u(v10)):
                                        while True:  # $label15
                                            arg6 = (arg6 + 1)
                                            store32((v12 + (arg6 << 2)), load32((v12 + ((arg6 + 1) << 2))))
                                            v10 = load32(arg4 + 8)
                                            if (u(arg6) < u(load32(arg4 + 8))):
                                                continue
                                            break
                                    arg6 = (v10 - 1)
                                    store32(arg4 + 8, (v10 - 1))
                                    if (u(arg6) > u(v9)):
                                        while True:  # $label16
                                            v9 = (v9 + 1)
                                            store32((v12 + (v9 << 2)), load32((v12 + ((v9 + 1) << 2))))
                                            if (u(v9) < u(load32(arg4 + 8))):
                                                continue
                                            break
                                    arg6 = ((arg1 + (v15 << 2)) + 282828)
                                    store32(((arg1 + (v15 << 2)) + 282828), (load32(arg6) - 1))
                                    arg6 = load32(v14 + 244)
                                    break
                                    break
                                v9 = (v9 + 2)
                                if (u((v9 + 2)) < u(v10)):
                                    continue
                                break
                            break
                        v16 = (v16 + 1)
                        if (u((v16 + 1)) < u(arg6)):
                            continue
                        break
                    break
                while True:  # block $label19
                    if (v11 == -1):
                        break
                    arg4 = ((arg1 + (arg2 << 2)) + 282828)
                    store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg4) - 1))
                    v9 = load32(arg5 + 8)
                    while True:  # block $label20
                        if (load32(v14 + 264) != 3):
                            break
                        v10 = 0
                        if (v9 == 0):
                            v9 = 0
                            break
                        while True:  # $label24
                            while True:  # block $label22
                                while True:  # block $label21
                                    arg4 = load32((load32(arg5) + (v10 << 2)))
                                    arg4 = ((load32((load32(arg5) + (v10 << 2))) - 2147483647) if (u(arg4) > u(2147483646)) else arg4)
                                    arg6 = ((((load32((load32(arg5) + (v10 << 2))) - 2147483647) if (u(arg4) > u(2147483646)) else arg4) * 404) + 9568096)
                                    # br_table[load32(((((load32((load32(arg5) + (v10 << 2))) - 2147483647) if (u(arg4) > u(2147483646)) else arg4) * 404) + 9568096) + 264)]
                                    break
                                    break
                                v9 = 0
                                arg6 = load32(arg6 + 180)
                                v12 = load32(load32(arg6 + 180) + 68)
                                if (load32(load32(arg6 + 180) + 68) == 0):
                                    break
                                while True:  # $label23
                                    if (arg2 != load32((arg6 + (v9 << 2)) + 28)):
                                        v9 = (v9 + 1)
                                        if (v12 != (v9 + 1)):
                                            continue
                                        break
                                    break
                                v10 = (v10 - 1)
                                arg5 = load32(arg0 + 20)
                                break
                            v10 = (v10 + 1)
                            v9 = load32(arg5 + 8)
                            if (u((v10 + 1)) < u(load32(arg5 + 8))):
                                continue
                            break
                        break
                    arg6 = (v9 - 1)
                    store32(arg5 + 8, (v9 - 1))
                    if (u(arg6) > u(v11)):
                        arg3 = load32(arg5)
                        v9 = v11
                        while True:  # $label25
                            v9 = (v9 + 1)
                            store32((arg3 + (v9 << 2)), load32((arg3 + ((v9 + 1) << 2))))
                            arg6 = load32(arg5 + 8)
                            if (u(v9) < u(load32(arg5 + 8))):
                                continue
                            break
                    while True:  # block $label30
                        while True:  # block $label28
                            while True:  # block $label29
                                while True:  # block $label26
                                    if (arg7 == 0):
                                        break
                                    while True:  # block $label27
                                        # br_table[(load8u(arg0 + 125) - 4)]
                                        break
                                        break
                                    if arg6:
                                        if v11:
                                            break
                                        func230(arg0)
                                        break
                                    arg3 = load32(arg0 + 44)
                                    if load32(arg0 + 44):
                                        store32((load32(9215884) + (arg3 << 4)), 0)
                                    store32(arg0 + 44, 0)
                                    func29(arg0, 1)
                                    break
                                if v11:
                                    break
                                break
                            if ((arg8 & 1) == 0):
                                break
                            # br_table[(load8u(arg0 + 125) - 4)]
                            break
                            break
                        if (arg8 & 1):
                            break
                        break
                    arg3 = load32(arg1 + 283848)
                    if (load32(arg1 + 283848) != 2147483647):
                        store32(arg1 + 283848, (load32(v13) + arg3))
                    arg3 = load32((arg1 + 283852))
                    if (load32((arg1 + 283852)) != 2147483647):
                        store32(arg1 + 283852, (load32(v13 + 4) + arg3))
                    arg3 = load32((arg1 + 283856))
                    if (load32((arg1 + 283856)) != 2147483647):
                        store32(arg1 + 283856, (load32(v13 + 8) + arg3))
                    arg3 = load32(v13 + 12)
                    arg4 = load32((arg1 + 283860))
                    if (load32((arg1 + 283860)) != 2147483647):
                        store32(arg1 + 283860, (arg3 + arg4))
                    arg4 = (arg1 + 281692)
                    store32((arg1 + 281692), (load32(arg4) - load32(v13)))
                    arg4 = (arg1 + 281696)
                    store32((arg1 + 281696), (load32(arg4) - load32(v13 + 4)))
                    arg4 = load32(v13 + 8)
                    arg5 = (arg1 + 281704)
                    store32((arg1 + 281704), (load32(arg5) - arg3))
                    v9 = 1
                    store8(arg1 + 286701, 1)
                    arg3 = (arg1 + 281700)
                    store32((arg1 + 281700), (load32(arg3) - arg4))
                    arg3 = load32(9142892)
                    if (u(load32(9142892)) < u(2)):
                        break
                    arg6 = (arg3 - 1)
                    arg7 = ((arg3 - 1) & 1)
                    arg1 = (load32(arg1 + 283908) * arg3)
                    arg4 = load32(9561692)
                    arg5 = load32(9143016)
                    if (arg3 != 2):
                        arg3 = (arg6 & -2)
                        v10 = 0
                        while True:  # $label31
                            if load8u((arg5 + (arg1 + v9))):
                                store8((arg4 + (v9 * 286704)) + 286701, 1)
                            arg6 = (v9 + 1)
                            if load8u((arg5 + ((v9 + 1) + arg1))):
                                store8((arg4 + (arg6 * 286704)) + 286701, 1)
                            v9 = (v9 + 2)
                            v10 = (v10 + 2)
                            if ((v10 + 2) != arg3):
                                continue
                            break
                    if (arg7 == 0):
                        break
                    if (load8u((arg5 + (arg1 + v9))) == 0):
                        break
                    store8((arg4 + (v9 * 286704)) + 286701, 1)
                    break
                arg1 = ((arg2 * 404) + 9568096)
                if (load32(arg1 + 244) == 0):
                    break
                v9 = 0
                while True:  # $label33
                    v9 = (v9 + 1)
                    if (u((v9 + 1)) < u(load32(arg1 + 244))):
                        continue
                    break
                break
                break
            while True:  # block $label34
                if arg4:
                    break
                arg3 = load32(arg7 + 8)
                if (load32(arg7 + 8) == 0):
                    break
                v11 = (arg2 + 2147483647)
                v10 = load32(arg7)
                v9 = 0
                arg6 = 0
                while True:  # $label35
                    if (load32((v10 + (arg6 << 2))) == v11):
                        break
                    arg6 = (arg6 + 1)
                    if ((arg6 + 1) != arg3):
                        continue
                    break
                break
            while True:  # block $label36
                arg3 = load32(arg1 + 281796)
                if (load32(arg1 + 281796) == 0):
                    break
                if arg5:
                    break
                arg6 = load32(arg3 + 8)
                if (load32(arg3 + 8) == 0):
                    break
                v11 = load32(arg0 + 28)
                arg3 = load32(arg3)
                v9 = 0
                while True:  # $label38
                    while True:  # block $label37
                        v10 = (v9 << 2)
                        if (load32((arg3 + (v9 << 2))) != v11):
                            break
                        if (load32((arg3 + (v10 | 4))) != arg2):
                            break
                        v9 = 0
                        break
                        break
                    v9 = (v9 + 2)
                    if (u((v9 + 2)) < u(arg6)):
                        continue
                    break
                break
            while True:  # block $label48
                while True:  # block $label39
                    if (arg4 == 0):
                        break
                    while True:  # block $label40
                        if (load32(arg7 + 8) == 0):
                            v10 = 0
                            break
                        arg6 = (arg7 + 8)
                        v14 = ((arg2 * 404) + 9568096)
                        v18 = ((arg1 + (arg2 << 2)) + 282828)
                        arg3 = 0
                        v11 = 0
                        while True:  # $label47
                            while True:  # block $label41
                                arg7 = load32(arg7)
                                v9 = load32((load32(arg7) + (arg3 << 2)))
                                if (((load32((load32(arg7) + (arg3 << 2))) - 2147483647) if (u(v9) > u(2147483646)) else v9) != arg2):
                                    break
                                if (arg3 == 0):
                                    store32(arg7, (load32(arg7) + 2147483647))
                                    while True:  # block $label42
                                        if (load32(arg0 + 92) == 0):
                                            break
                                        arg3 = load8u(9147141)
                                        if load32(9140316):
                                            if (load32(9140320) != load32(arg0 + 28)):
                                                break
                                        break
                                    arg3 = 0
                                    v9 = 0
                                    if (load32(v14 + 244) == 0):
                                        v11 = 1
                                        break
                                    while True:  # $label43
                                        v11 = 1
                                        v9 = (v9 + 1)
                                        if (u((v9 + 1)) < u(load32(v14 + 244))):
                                            continue
                                        break
                                    break
                                v9 = load32(arg1 + 283848)
                                if (load32(arg1 + 283848) != 2147483647):
                                    store32(arg1 + 283848, (load32(v13) + v9))
                                v9 = load32(arg1 + 283852)
                                if (load32(arg1 + 283852) != 2147483647):
                                    store32(arg1 + 283852, (load32(v13 + 4) + v9))
                                v9 = load32(arg1 + 283856)
                                if (load32(arg1 + 283856) != 2147483647):
                                    store32(arg1 + 283856, (load32(v13 + 8) + v9))
                                v9 = load32(v13 + 12)
                                v10 = load32(arg1 + 283860)
                                if (load32(arg1 + 283860) != 2147483647):
                                    store32(arg1 + 283860, (v9 + v10))
                                store32(arg1 + 281692, (load32(arg1 + 281692) - load32(v13)))
                                store32(arg1 + 281696, (load32(arg1 + 281696) - load32(v13 + 4)))
                                v10 = load32(v13 + 8)
                                store32(arg1 + 281704, (load32(arg1 + 281704) - v9))
                                store8(arg1 + 286701, 1)
                                store32(arg1 + 281700, (load32(arg1 + 281700) - v10))
                                while True:  # block $label44
                                    v10 = load32(9142892)
                                    if (u(load32(9142892)) < u(2)):
                                        break
                                    v9 = 1
                                    v19 = (v10 - 1)
                                    v21 = ((v10 - 1) & 1)
                                    v16 = (load32(arg1 + 283908) * v10)
                                    v15 = load32(9561692)
                                    v17 = load32(9143016)
                                    if (v10 != 2):
                                        v19 = (v19 & -2)
                                        v10 = 0
                                        while True:  # $label45
                                            if load8u((v17 + (v9 + v16))):
                                                store8((v15 + (v9 * 286704)) + 286701, 1)
                                            v22 = (v9 + 1)
                                            if load8u((v17 + ((v9 + 1) + v16))):
                                                store8((v15 + (v22 * 286704)) + 286701, 1)
                                            v9 = (v9 + 2)
                                            v10 = (v10 + 2)
                                            if ((v10 + 2) != v19):
                                                continue
                                            break
                                    if (v21 == 0):
                                        break
                                    if (load8u((v17 + (v9 + v16))) == 0):
                                        break
                                    store8((v15 + (v9 * 286704)) + 286701, 1)
                                    break
                                v10 = (load32(arg6) - 1)
                                store32(arg6, (load32(arg6) - 1))
                                v9 = arg3
                                if (u(v10) > u(arg3)):
                                    while True:  # $label46
                                        v9 = (v9 + 1)
                                        store32((arg7 + (v9 << 2)), load32((arg7 + ((v9 + 1) << 2))))
                                        if (u(v9) < u(load32(arg6))):
                                            continue
                                        break
                                store32(v18, (load32(v18) - 1))
                                arg3 = (arg3 - 1)
                                break
                            arg7 = load32(arg0 + 20)
                            arg6 = (load32(arg0 + 20) + 8)
                            arg3 = (arg3 + 1)
                            v10 = load32(arg7 + 8)
                            if (u((arg3 + 1)) < u(load32(arg7 + 8))):
                                continue
                            break
                        v9 = 1
                        if (v11 & 1):
                            break
                        break
                    if v10:
                        break
                    # br_table[(v20 - 4)]
                    break
                    break
                arg3 = (arg4 ^ 1)
                if (func66(arg1, v13, (arg4 ^ 1), 1) == 0):
                    break
                if ((arg3 | arg5) == 0):
                    func181(arg1, load32(arg0 + 28), arg2)
                    arg1 = ((arg1 + (arg2 << 2)) + 282828)
                    store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg1) + 1))
                v9 = 0
                func294(arg0)
                arg0 = ((arg2 * 404) + 9568096)
                if (load32(arg0 + 244) == 0):
                    break
                arg7 = 0
                while True:  # $label49
                    arg7 = (arg7 + 1)
                    if (u((arg7 + 1)) < u(load32(arg0 + 244))):
                        continue
                    break
                break
                break
            while True:  # block $label50
                if (arg8 == 0):
                    break
                v9 = 0
                while True:  # block $label66
                    while True:  # block $label57
                        arg6 = 0
                        v10 = 0
                        v14 = 0
                        v16 = load16u(arg0 + 110)
                        v15 = load32(9561692)
                        while True:  # block $label53
                            while True:  # block $label52
                                while True:  # block $label51
                                    arg8 = load32(((arg2 * 404) + 9568096) + 180)
                                    if (load8u(load32(((arg2 * 404) + 9568096) + 180) + 23) == 0):
                                        break
                                    arg3 = load32(arg8 + 4)
                                    if (load32(((load32(arg8 + 4) * 404) + 9568096) + 264) != 3):
                                        break
                                    if (load32((((v15 + (v16 * 286704)) + (arg3 << 2)) + 281808)) == 0):
                                        break
                                    v11 = load32(arg8 + 68)
                                    break
                                    break
                                arg7 = 1
                                v11 = load32(arg8 + 68)
                                if (load32(arg8 + 68) == 0):
                                    break
                                v18 = (v15 + (v16 * 286704))
                                arg3 = 1
                                while True:  # $label56
                                    v19 = load32((arg8 + (arg6 << 2)) + 28)
                                    arg7 = load32(((load32((arg8 + (arg6 << 2)) + 28) * 404) + 9568096) + 264)
                                    v17 = (load32(((load32((arg8 + (arg6 << 2)) + 28) * 404) + 9568096) + 264) == 1)
                                    while True:  # block $label55
                                        while True:  # block $label54
                                            v19 = load32(((v18 + (v19 << 2)) + 281808))
                                            if (load32(((v18 + (v19 << 2)) + 281808)) == 1):
                                                break
                                            arg3 = ((arg7 != 3) & arg3)
                                            if v19:
                                                break
                                            arg3 = ((arg7 != 0) & arg3)
                                            break
                                            break
                                        v10 = (v10 | v17)
                                        break
                                    v14 = (v14 | v17)
                                    arg6 = (arg6 + 1)
                                    if ((arg6 + 1) != v11):
                                        continue
                                    break
                                arg7 = 1
                                if (((arg3 & v10) if (v14 & 1) else arg3) & 1):
                                    break
                                break
                            if (v11 == 0):
                                break
                            v10 = (v15 + (v16 * 286704))
                            v14 = ((v15 + (v16 * 286704)) + 281796)
                            v16 = load32(arg0 + 28)
                            arg3 = 0
                            v15 = load32(arg0 + 20)
                            if (load32(arg0 + 20) == 0):
                                while True:  # $label60
                                    while True:  # block $label58
                                        v15 = load32((arg8 + (arg3 << 2)) + 28)
                                        if load32(((v10 + (load32((arg8 + (arg3 << 2)) + 28) << 2)) + 281808)):
                                            break
                                        arg7 = 0
                                        arg6 = load32(v14)
                                        if (load32(v14) == 0):
                                            break
                                        v17 = load32(arg6 + 8)
                                        if (load32(arg6 + 8) == 0):
                                            break
                                        arg7 = load32(arg6)
                                        arg6 = 0
                                        while True:  # $label59
                                            v18 = (arg6 << 2)
                                            if (v16 == load32((arg7 + (arg6 << 2)))):
                                                if (load32((arg7 + (v18 | 4))) == v15):
                                                    break
                                            arg6 = (arg6 + 2)
                                            if (u((arg6 + 2)) < u(v17)):
                                                continue
                                            break
                                        break
                                        break
                                    arg7 = 2
                                    arg3 = (arg3 + 1)
                                    if ((arg3 + 1) != v11):
                                        continue
                                    break
                                    break
                                raise RuntimeError('unreachable')
                            while True:  # $label65
                                while True:  # block $label61
                                    v17 = load32((arg8 + (arg3 << 2)) + 28)
                                    if load32(((v10 + (load32((arg8 + (arg3 << 2)) + 28) << 2)) + 281808)):
                                        break
                                    while True:  # block $label62
                                        v18 = load32(v15 + 8)
                                        if (load32(v15 + 8) == 0):
                                            break
                                        v19 = load32(v15)
                                        arg7 = 0
                                        while True:  # $label63
                                            arg6 = load32((v19 + (arg7 << 2)))
                                            if (v17 != ((load32((v19 + (arg7 << 2))) - 2147483647) if (u(arg6) > u(2147483646)) else arg6)):
                                                arg7 = (arg7 + 1)
                                                if (v18 != (arg7 + 1)):
                                                    continue
                                                break
                                            break
                                        break
                                        break
                                    arg7 = 0
                                    arg6 = load32(v14)
                                    if (load32(v14) == 0):
                                        break
                                    v18 = load32(arg6 + 8)
                                    if (load32(arg6 + 8) == 0):
                                        break
                                    arg7 = load32(arg6)
                                    arg6 = 0
                                    while True:  # $label64
                                        v19 = (arg6 << 2)
                                        if (v16 == load32((arg7 + (arg6 << 2)))):
                                            if (load32((arg7 + (v19 | 4))) == v17):
                                                break
                                        arg6 = (arg6 + 2)
                                        if (u((arg6 + 2)) < u(v18)):
                                            continue
                                        break
                                    break
                                    break
                                arg7 = 2
                                arg3 = (arg3 + 1)
                                if ((arg3 + 1) != v11):
                                    continue
                                break
                            break
                        break
                    # br_table[arg7]
                    break
                    break
                func181(arg1, load32(arg0 + 28), arg2)
                arg1 = ((arg1 + (arg2 << 2)) + 282828)
                store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg1) + 1))
                func294(arg0)
                arg0 = ((arg2 * 404) + 9568096)
                if (load32(arg0 + 244) == 0):
                    break
                arg7 = 0
                while True:  # $label67
                    arg7 = (arg7 + 1)
                    if (u((arg7 + 1)) < u(load32(arg0 + 244))):
                        continue
                    break
                break
                break
            arg8 = ((2147483647 if arg4 else 0) + arg2)
            while True:  # block $label68
                arg3 = load32(arg0 + 20)
                arg7 = load32(load32(arg0 + 20) + 8)
                if (load32(load32(arg0 + 20) + 8) != load32(arg3 + 4)):
                    arg6 = load32(arg3)
                    break
                arg6 = (load32(arg3 + 12) + arg7)
                store32(arg3 + 4, (load32(arg3 + 12) + arg7))
                arg4 = load32(arg3)
                arg6 = func26((-1 if (u(arg6) > u(1073741823)) else (arg6 << 2)))
                if arg7:
                    # TODO: memory.copy []
                if arg4:
                    arg7 = load32(arg3 + 8)
                store32(arg3, arg6)
                break
            store32(arg3 + 8, (arg7 + 1))
            store32((arg6 + (arg7 << 2)), arg8)
            if (arg5 == 0):
                arg1 = ((arg1 + (arg2 << 2)) + 282828)
                store32(((arg1 + (arg2 << 2)) + 282828), (load32(arg1) + 1))
            while True:  # block $label69
                if (load32(load32(arg0 + 20) + 8) != 1):
                    break
                while True:  # block $label70
                    # br_table[(v20 - 4)]
                    break
                    break
                store8(arg0 + 125, 6)
                # TODO: i32.div_u []
                func63(arg0, 2, 0, ((load32(((arg2 * 404) + 9568096) + 116) * load32((load32(9142424) + (132 if load32(v12 + 264) else 128)))) * 1000), 100)
                break
            arg1 = ((arg2 * 404) + 9568096)
            if (load32(arg1 + 244) == 0):
                break
            v9 = 0
            while True:  # $label71
                v9 = (v9 + 1)
                if (u((v9 + 1)) < u(load32(arg1 + 244))):
                    continue
                break
            break
        v9 = 1
        if (load32(arg0 + 92) == 0):
            break
        arg1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break
    G.global0 = (v13 + 16)
    return v9

# ------------------------------------------------------------
# $func184
# ------------------------------------------------------------
def func184(arg0, arg1, arg2, arg3):
    while True:  # block $label1
        while True:  # block $label0
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

# ------------------------------------------------------------
# $func185
# ------------------------------------------------------------
def func185(arg0):
    if ((load8u(arg0) & 15) == 0):
        # TODO: i32.atomic.rmw.cmpxchg []
        return (10 & 10)
    while True:  # block $label4
        v2 = load32(arg0)
        while True:  # block $label3
            while True:  # block $label2
                while True:  # block $label0
                    v1 = G.global3
                    v4 = load32(G.global3 + 24)
                    v3 = load32(arg0 + 4)
                    v6 = (load32(arg0 + 4) & 1073741823)
                    if (load32(G.global3 + 24) != (load32(arg0 + 4) & 1073741823)):
                        break
                    while True:  # block $label1
                        if ((v2 & 8) == 0):
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
                    if (u(load32(arg0 + 20)) > u(2147483646)):
                        break
                    store32(arg0 + 20, (v1 + 1))
                    break
                    break
                v5 = 56
                if (v6 == 1073741823):
                    break
                while True:  # block $label5
                    if v6:
                        break
                    if (0 if (v2 & 4) else v3):
                        break
                    if (v2 & 128):
                        if (load32(v1 + 80) == 0):
                            store32(v1 + 80, -12)
                        v6 = load32(arg0 + 8)
                        store32(v1 + 84, (arg0 + 16))
                    else:
                    # TODO: i32.atomic.rmw.cmpxchg []
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
            if (v3 == 0):
                break
            store32(arg0 + 20, 0)
            break
            break
        break
    return v5

# ------------------------------------------------------------
# $func186
# ------------------------------------------------------------
def func186(arg0, arg1, arg2, arg3):
    v5 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        if (arg0 == 0):
            break
        if (load32(9688320) == 0):
            store32(9688320, 43)
        if (load8u(9688037) == 0):
            while True:  # block $label1
                v7 = load8s(9688039)
                if (load8s(9688039) == 0):
                    break
                # TODO: i32.atomic.rmw.cmpxchg []
                v4 = -2147483647
                if (v7 < 0):
                    store8(9688039, 0)
                if (v4 == 0):
                    break
                while True:  # $label2
                    v7 = ((v4 + 2147483647) if (v4 < 0) else v4)
                    # TODO: i32.atomic.rmw.cmpxchg []
                    v4 = (v7 - 2147483647)
                    if ((v7 - 2147483647) == v7):
                        break
                    v6 = (v6 + 1)
                    if ((v6 + 1) != 10):
                        continue
                    break
                # TODO: i32.atomic.rmw.add []
                v4 = (1 + 1)
                while True:  # $label3
                    if (v4 < 0):
                        func439(9688228, v4)
                        v4 = (v4 + 2147483647)
                    # TODO: i32.atomic.rmw.cmpxchg []
                    v4 = (v4 | -2147483648)
                    if (v4 != (v4 | -2147483648)):
                        continue
                    break
                break
            v4 = load32(9688232)
            if load32(9688232):
                while True:  # $label5
                    while True:  # block $label4
                        if (v4 == 0):
                            break
                        if (load32(v4 + 76) >= 0):
                            break
                        store32(v4 + 76, 0)
                        break
                    v4 = load32(v4 + 56)
                    if load32(v4 + 56):
                        continue
                    break
            while True:  # block $label6
                if (load32(9688228) >= 0):
                    break
                # TODO: i32.atomic.rmw.add []
                if (2147483647 == -2147483647):
                    break
                func97(9688228)
                break
            while True:  # block $label7
                v4 = load32(9688032)
                if (load32(9688032) == 0):
                    break
                if (load32(v4 + 76) >= 0):
                    break
                store32(v4 + 76, 0)
                break
            while True:  # block $label8
                v4 = load32(52736)
                if (load32(52736) == 0):
                    break
                if (load32(v4 + 76) >= 0):
                    break
                store32(v4 + 76, 0)
                break
            while True:  # block $label9
                v4 = load32(52584)
                if (load32(52584) == 0):
                    break
                if (load32(v4 + 76) >= 0):
                    break
                store32(v4 + 76, 0)
                break
            store8(9688037, 1)
        # TODO: memory.fill []
        while True:  # block $label10
            if (u((arg1 + 1)) >= u(2)):
                # TODO: memory.copy []
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
        if (arg1 == 0):
            store8(9688039, 1)
        if a_y():
            arg0 = (load32(9688040) - 1)
            store32(9688040, (load32(9688040) - 1))
            if (arg0 == 0):
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

# ------------------------------------------------------------
# $func187
# ------------------------------------------------------------
def func187(arg0):
    while True:  # block $label0
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

# ------------------------------------------------------------
# $func188
# ------------------------------------------------------------
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

# ------------------------------------------------------------
# $func189
# ------------------------------------------------------------
def func189(arg0, arg1, arg2, arg3, arg4):
    v13 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label10
        while True:  # block $label0
            if (arg1 < arg2):
                if (load32(arg0 + 12) < arg2):
                    break
                v8 = load32(arg0 + 8)
                while True:  # block $label5
                    while True:  # block $label4
                        while True:  # block $label2
                            while True:  # block $label1
                                while True:  # block $label3
                                    # br_table[load32(arg0)]
                                    break
                                    break
                                # call_indirect[load32(9687572)]
                                break
                                break
                            while True:  # block $label9
                                while True:  # block $label6
                                    if arg1:
                                        v7 = arg4
                                        break
                                    v5 = (load32(arg3) - 16777216)
                                    store32(arg4, (load32(arg3) - 16777216))
                                    while True:  # block $label7
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
                                        if (v12 == 0):
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
                                        if (v7 == 0):
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
                                    raise RuntimeError('unreachable')
                                v5 = load32(arg0 + 4)
                                v15 = (1 << load32(arg0 + 4))
                                v16 = (0 - (1 << load32(arg0 + 4)))
                                v17 = (v15 - 1)
                                v18 = ((((v15 - 1) + v8) & 0xFFFFFFFF) >> v5)
                                v10 = (load32(arg0 + 16) + ((((((v15 - 1) + v8) & 0xFFFFFFFF) >> v5) * (v9 >> v5)) << 2))
                                while True:  # $label13
                                    if (v7 == 0):
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
                                        # call_indirect[load32(((((load32(v6) & 0xFFFFFFFF) >> 6) & 60) + 9687600))]
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
                            # TODO: memory.copy []
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
                            while True:  # block $label14
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
                                    # call_indirect[load32(9687792)]
                                    v5 = (v5 + 4)
                                    v10 = (v6 << 2)
                                    arg4 = (arg4 + (v6 << 2))
                                    arg3 = (arg3 + v10)
                                    if (u((arg3 + v10)) < u(v14)):
                                        continue
                                    break
                                break
                            if (u(arg3) < u(v15)):
                                v5 = load32(v5)
                                store8(v13 + 12, load32(v5))
                                store8(v13 + 14, ((v5 & 0xFFFFFFFF) >> 16))
                                store8(v13 + 13, ((v5 & 0xFFFFFFFF) >> 8))
                                # call_indirect[load32(9687792)]
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
                    while True:  # block $label17
                        if (arg3 != arg4):
                            break
                        if (v5 <= 0):
                            break
                        arg4 = (arg2 - arg1)
                        arg4 = ((((((v8 + (1 << v5)) - 1) & 0xFFFFFFFF) >> v5) * arg4) << 2)
                        v6 = ((arg3 + ((v8 * (arg2 - arg1)) << 2)) - ((((((v8 + (1 << v5)) - 1) & 0xFFFFFFFF) >> v5) * arg4) << 2))
                        # TODO: memory.copy []
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
                                        while True:  # block $label18
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
                                    if ((arg4 & v11) == 0):
                                        v5 = load8u(v6 + 1)
                                        v6 = (v6 + 4)
                                    store32(arg3, load32((v9 + ((v5 & v10) << 2))))
                                    arg3 = (arg3 + 4)
                                arg1 = (arg1 + 1)
                                if ((arg1 + 1) != arg2):
                                    continue
                                break
                            break
                        # call_indirect[load32(9687796)]
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
                                    while True:  # block $label21
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
                                if ((v5 & v10) == 0):
                                    v6 = load8u(arg3 + 1)
                                    arg3 = (arg3 + 4)
                                store32(arg4, load32((v7 + ((v6 & v9) << 2))))
                                arg4 = (arg4 + 4)
                            arg1 = (arg1 + 1)
                            if ((arg1 + 1) != arg2):
                                continue
                            break
                        break
                    # call_indirect[load32(9687796)]
                    break
                G.global0 = (v13 + 16)
                return indirect_call(load32(9687796))
            a_c()
            raise RuntimeError('unreachable')
            break
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')
    return 7559

# ------------------------------------------------------------
# $func191
# ------------------------------------------------------------
def func191(arg0):
    func116((arg0 + 172))
    func151(load32(arg0 + 168))
    func136((arg0 + 124))
    func136((arg0 + 136))
    # TODO: memory.fill []
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

# ------------------------------------------------------------
# $func192
# ------------------------------------------------------------
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
                while True:  # block $label0
                    while True:  # block $label23
                        while True:  # block $label26
                            while True:  # block $label3
                                while True:  # block $label5
                                    while True:  # block $label4
                                        while True:  # block $label2
                                            while True:  # block $label1
                                                v10 = (arg1 - v4)
                                                v9 = ((arg1 - v4) // 28)
                                                # br_table[((arg1 - v4) // 28)]
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
                                    while True:  # block $label6
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
                                                while True:  # block $label7
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
                                if (arg2 == 0):
                                    if (arg1 == v4):
                                        break
                                    v8 = (((v9 - 2) & 0xFFFFFFFF) >> 1)
                                    arg0 = (((v9 - 2) & 0xFFFFFFFF) >> 1)
                                    while True:  # $label13
                                        while True:  # block $label10
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
                                                while True:  # block $label11
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
                                    # TODO: i32.div_u []
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
                                            while True:  # block $label14
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
                                        while True:  # block $label16
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
                                            # TODO: i32.div_u []
                                            v10 = (((28 - 2) & 0xFFFFFFFF) >> 1)
                                            arg2 = (arg2 + ((((28 - 2) & 0xFFFFFFFF) >> 1) * 28))
                                            if (v4 >= (load32((arg2 + ((((28 - 2) & 0xFFFFFFFF) >> 1) * 28)) + 12) * load32(arg2 + 8))):
                                                break
                                            v14 = load64(arg0)
                                            store32(v3 + 8, load32(arg0 + 24))
                                            store64(v3, load64(arg0 + 16))
                                            while True:  # $label18
                                                while True:  # block $label17
                                                    v5 = arg2
                                                    store64(arg0, load64(arg2))
                                                    store32(arg0 + 24, load32(v5 + 24))
                                                    store64(arg0 + 16, load64(v5 + 16))
                                                    store64(arg0 + 8, load64(v5 + 8))
                                                    if (v10 == 0):
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
                                while True:  # block $label20
                                    if (u(v10) >= u(27973)):
                                        arg0 = (((v9 & 0xFFFFFFFF) >> 2) * 28)
                                        break
                                    arg0 = (load32(v11) * load32(v12))
                                    while True:  # block $label21
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
                                while True:  # block $label22
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
                                if (u((v9 + 28)) >= u(arg0)):
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
                                    if (u(arg0) < u(v4)):
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
                                    raise RuntimeError('unreachable')
                                    break
                                raise RuntimeError('unreachable')
                                break
                            break
                            break
                        while True:  # block $label30
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
                        if (v10 == 0):
                            v4 = func419(v9, v6)
                            arg0 = (v6 + 28)
                            if func419((v6 + 28), arg1):
                                arg0 = v9
                                arg1 = v6
                                if (v4 == 0):
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
                        if (u(arg0) <= u(v4)):
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
                    raise RuntimeError('unreachable')
                    break
                break
            break
        break
    G.global0 = (v3 + 48)
    return func192((v6 + 28), arg1, arg2)

# ------------------------------------------------------------
# $func193
# ------------------------------------------------------------
def func193(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    v10 = load32(arg2 + 216)
    v18 = load32(arg2 + 208)
    v19 = load32(arg2 + 372)
    while True:  # block $label2
        while True:  # block $label0
            if (arg6 == 0):
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
            v25 = load32(9671128)
            v15 = load32(arg2 + 212)
            v16 = load32(9142840)
            v9 = arg0
            while True:  # $label6
                v11 = (v9 + 1)
                v17 = (v9 - arg0)
                arg6 = arg1
                v8 = arg1
                while True:  # block $label4
                    if (u(v9) < u(v13)):
                        while True:  # $label3
                            while True:  # block $label1
                                if (load8u((v19 + (v17 + ((arg6 - arg1) * v10)))) == 0):
                                    arg6 = (arg6 + 1)
                                    break
                                v8 = 0
                                if (u(arg6) >= u(v13)):
                                    break
                                if ((arg6 | v9) < 0):
                                    break
                                arg6 = (arg6 + 1)
                                v23 = load32((v16 + ((((v21 + (arg6 + 1)) * v14) + v11) << 2)))
                                if (v15 != load32((v16 + ((((v21 + (arg6 + 1)) * v14) + v11) << 2)))):
                                    v23 = (v25 + (v23 * 132))
                                    v26 = load8u((v25 + (v23 * 132)) + 122)
                                    if (((v24 == load8u((v25 + (v23 * 132)) + 122)) | (v22 == v26)) == 0):
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
                        raise RuntimeError('unreachable')
                    while True:  # $label5
                        if (load8u((v19 + (v17 + ((v8 - arg1) * v10)))) == 0):
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
        if (arg4 == 0):
            break
        if (v10 <= 0):
            break
        v11 = load32(arg2 + 220)
        v13 = (load32(arg2 + 220) + arg1)
        if ((load32(arg2 + 220) + arg1) <= arg1):
            break
        arg2 = (u(v11) > u(1))
        v14 = (3 if (u(v11) > u(1)) else 4)
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
                while True:  # block $label7
                    if (load8u((v19 + (v20 + ((arg6 - arg1) * v10)))) == 0):
                        break
                    while True:  # block $label8
                        if v17:
                            break
                        if (u(v8) < u(v15)):
                            break
                        if (u(v8) <= u(v14)):
                            break
                        break
                    v21 = (arg6 + 1)
                    arg7 = (load32(9142440) + 2)
                    arg7 = ((((arg6 + 1) + ((load32(9142440) + 2) * v18)) * arg7) + arg4)
                    v9 = load32(9142840)
                    while True:  # block $label9
                        if (arg5 == 0):
                            break
                        v12 = (load32(9671128) + (load32((v9 + (arg7 << 2))) * 132))
                        v22 = load8u((load32(9671128) + (load32((v9 + (arg7 << 2))) * 132)) + 122)
                        if (((load8u((load32(9671128) + (load32((v9 + (arg7 << 2))) * 132)) + 122) == load32(38600)) | (load32(38472) == v22)) == 0):
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

# ------------------------------------------------------------
# $func194
# ------------------------------------------------------------
def func194(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    v7 = load32(arg2 + 208)
    while True:  # block $label0
        while True:  # block $label30
            if arg6:
                arg6 = 0
                v14 = load32(9142440)
                v18 = (u(load32(9142440)) <= u(arg1))
                if (u(load32(9142440)) <= u(arg1)):
                    break
                v17 = (arg0 | arg1)
                if ((arg0 | arg1) < 0):
                    break
                if (u(arg0) >= u(v14)):
                    break
                v10 = load32(9142840)
                v16 = (arg0 + 1)
                v11 = (v14 + 2)
                v7 = ((v14 + 2) * v7)
                v19 = (arg1 + ((v14 + 2) * v7))
                v20 = ((arg0 + 1) + (((arg1 + ((v14 + 2) * v7)) + 1) * v11))
                if (load32((load32(9142840) + (((arg0 + 1) + (((arg1 + ((v14 + 2) * v7)) + 1) * v11)) << 2))) != load32(arg2 + 212)):
                    break
                if load32((((load32(9561692) + (arg3 * 286704)) + (load32(38452) << 2)) + 281808)):
                    break
                v8 = (arg0 - 1)
                v15 = (v7 + 1)
                v12 = (arg1 - 2)
                v13 = load32(38464)
                v7 = load32(9671128)
                while True:  # block $label1
                    arg2 = (arg0 - 2)
                    if (u((arg0 - 2)) >= u(v14)):
                        break
                    while True:  # block $label2
                        if (u(v12) >= u(v14)):
                            break
                        if ((arg2 | v12) < 0):
                            break
                        v9 = load32((v10 + ((v8 + ((v12 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((v8 + ((v12 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v9 * 132))
                        if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v9 * 132)) + 125) - 4)]
                        break
                        break
                    while True:  # block $label3
                        arg6 = (arg1 - 1)
                        if (u(v14) <= u((arg1 - 1))):
                            break
                        if ((arg2 | arg6) < 0):
                            break
                        v9 = load32((v10 + ((v8 + (v11 * v19)) << 2)))
                        if (u(load32((v10 + ((v8 + (v11 * v19)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v9 * 132))
                        if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v9 * 132)) + 125) - 4)]
                        break
                        break
                    while True:  # block $label4
                        if v18:
                            break
                        if ((arg1 | arg2) < 0):
                            break
                        v9 = load32((v10 + ((v8 + ((arg1 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((v8 + ((arg1 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v9 * 132))
                        if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v9 * 132)) + 125) - 4)]
                        break
                        break
                    while True:  # block $label5
                        arg6 = (arg1 + 1)
                        if (u(v14) <= u((arg1 + 1))):
                            break
                        if ((arg2 | arg6) < 0):
                            break
                        v9 = load32((v10 + ((v8 + ((arg6 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((v8 + ((arg6 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v9 * 132))
                        if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v9 * 132)) + 125) - 4)]
                        break
                        break
                    v9 = (arg1 + 2)
                    if (u((arg1 + 2)) >= u(v14)):
                        arg6 = 0
                        break
                    arg6 = 0
                    if ((arg2 | v9) < 0):
                        break
                    arg2 = load32((v10 + ((v8 + ((v9 + v15) * v11)) << 2)))
                    if (u(load32((v10 + ((v8 + ((v9 + v15) * v11)) << 2)))) < u(3)):
                        break
                    v9 = (v7 + (arg2 * 132))
                    if (arg3 != load16u((v7 + (arg2 * 132)) + 110)):
                        break
                    if (v13 != load8u(v9 + 122)):
                        break
                    arg2 = load8u((v7 + (arg2 * 132)) + 125)
                    arg6 = (0 - ((load8u((v7 + (arg2 * 132)) + 125) != 14) & (arg2 != 4)))
                    break
                while True:  # block $label8
                    while True:  # block $label6
                        if (u(v8) >= u(v14)):
                            break
                        while True:  # block $label7
                            if (u(v12) >= u(v14)):
                                break
                            if ((v8 | v12) < 0):
                                break
                            v9 = load32((v10 + ((((v12 + v15) * v11) + arg0) << 2)))
                            if (u(load32((v10 + ((((v12 + v15) * v11) + arg0) << 2)))) < u(3)):
                                break
                            arg2 = (v7 + (v9 * 132))
                            if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table[(load8u((v7 + (v9 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label9
                            arg2 = (arg1 - 1)
                            if (u(v14) <= u((arg1 - 1))):
                                break
                            if ((arg2 | v8) < 0):
                                break
                            v9 = load32((v10 + (((v11 * v19) + arg0) << 2)))
                            if (u(load32((v10 + (((v11 * v19) + arg0) << 2)))) < u(3)):
                                break
                            arg2 = (v7 + (v9 * 132))
                            if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table[(load8u((v7 + (v9 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label10
                            if v18:
                                break
                            if ((arg1 | v8) < 0):
                                break
                            v9 = load32((v10 + ((((arg1 + v15) * v11) + arg0) << 2)))
                            if (u(load32((v10 + ((((arg1 + v15) * v11) + arg0) << 2)))) < u(3)):
                                break
                            arg2 = (v7 + (v9 * 132))
                            if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table[(load8u((v7 + (v9 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label11
                            arg2 = (arg1 + 1)
                            if (u(v14) <= u((arg1 + 1))):
                                break
                            if ((arg2 | v8) < 0):
                                break
                            v9 = load32((v10 + ((((arg2 + v15) * v11) + arg0) << 2)))
                            if (u(load32((v10 + ((((arg2 + v15) * v11) + arg0) << 2)))) < u(3)):
                                break
                            arg2 = (v7 + (v9 * 132))
                            if (load16u((v7 + (v9 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table[(load8u((v7 + (v9 * 132)) + 125) - 4)]
                            break
                            break
                        arg2 = (arg1 + 2)
                        if (u(v14) <= u((arg1 + 2))):
                            break
                        if ((arg2 | v8) < 0):
                            break
                        v8 = load32((v10 + ((((arg2 + v15) * v11) + arg0) << 2)))
                        if (u(load32((v10 + ((((arg2 + v15) * v11) + arg0) << 2)))) < u(3)):
                            break
                        arg2 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg2 + 122)):
                            break
                        arg2 = 1
                        # br_table[(load8u((v7 + (v8 * 132)) + 125) - 4)]
                        break
                        break
                    arg2 = arg6
                    break
                while True:  # block $label13
                    while True:  # block $label12
                        v9 = (u(v12) >= u(v14))
                        if (u(v12) >= u(v14)):
                            break
                        if ((arg0 | v12) < 0):
                            break
                        v8 = load32((v10 + ((v16 + ((v12 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((v16 + ((v12 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v8 * 132)) + 125) - 4)]
                        break
                        break
                    while True:  # block $label14
                        arg6 = (arg1 - 1)
                        if (u(v14) <= u((arg1 - 1))):
                            break
                        if ((arg0 | arg6) < 0):
                            break
                        v8 = load32((v10 + ((v16 + (v11 * v19)) << 2)))
                        if (u(load32((v10 + ((v16 + (v11 * v19)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v8 * 132)) + 125) - 4)]
                        break
                        break
                    while True:  # block $label15
                        if v18:
                            break
                        if (v17 < 0):
                            break
                        v8 = load32((v10 + ((v16 + ((arg1 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((v16 + ((arg1 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v8 * 132)) + 125) - 4)]
                        break
                        break
                    while True:  # block $label16
                        arg6 = (arg1 + 1)
                        if (u(v14) <= u((arg1 + 1))):
                            break
                        if ((arg0 | arg6) < 0):
                            break
                        v8 = load32((v10 + ((v16 + ((arg6 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((v16 + ((arg6 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v8 * 132)) + 125) - 4)]
                        break
                        break
                    while True:  # block $label17
                        arg6 = (arg1 + 2)
                        if (u(v14) <= u((arg1 + 2))):
                            break
                        if ((arg0 | arg6) < 0):
                            break
                        v8 = load32((v10 + ((v16 + ((arg6 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((v16 + ((arg6 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg6 = (v7 + (v8 * 132))
                        if (load16u((v7 + (v8 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg6 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (v8 * 132)) + 125) - 4)]
                        break
                        break
                    arg6 = arg2
                    break
                v8 = (arg0 + 2)
                while True:  # block $label20
                    while True:  # block $label18
                        if (u(v14) <= u(v16)):
                            break
                        while True:  # block $label19
                            if v9:
                                break
                            if ((v12 | v16) < 0):
                                break
                            v17 = load32((v10 + ((v8 + ((v12 + v15) * v11)) << 2)))
                            if (u(load32((v10 + ((v8 + ((v12 + v15) * v11)) << 2)))) < u(3)):
                                break
                            arg2 = (v7 + (v17 * 132))
                            if (load16u((v7 + (v17 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table[(load8u((v7 + (v17 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label21
                            arg2 = (arg1 - 1)
                            if (u(v14) <= u((arg1 - 1))):
                                break
                            if ((arg2 | v16) < 0):
                                break
                            v17 = load32((v10 + ((v8 + (v11 * v19)) << 2)))
                            if (u(load32((v10 + ((v8 + (v11 * v19)) << 2)))) < u(3)):
                                break
                            arg2 = (v7 + (v17 * 132))
                            if (load16u((v7 + (v17 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table[(load8u((v7 + (v17 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label22
                            if v18:
                                break
                            if ((arg1 | v16) < 0):
                                break
                            v17 = load32((v10 + ((v8 + ((arg1 + v15) * v11)) << 2)))
                            if (u(load32((v10 + ((v8 + ((arg1 + v15) * v11)) << 2)))) < u(3)):
                                break
                            arg2 = (v7 + (v17 * 132))
                            if (load16u((v7 + (v17 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table[(load8u((v7 + (v17 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label23
                            arg2 = (arg1 + 1)
                            if (u(v14) <= u((arg1 + 1))):
                                break
                            if ((arg2 | v16) < 0):
                                break
                            v17 = load32((v10 + ((v8 + ((arg2 + v15) * v11)) << 2)))
                            if (u(load32((v10 + ((v8 + ((arg2 + v15) * v11)) << 2)))) < u(3)):
                                break
                            arg2 = (v7 + (v17 * 132))
                            if (load16u((v7 + (v17 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg2 + 122)):
                                break
                            arg2 = 1
                            # br_table[(load8u((v7 + (v17 * 132)) + 125) - 4)]
                            break
                            break
                        arg2 = (arg1 + 2)
                        if (u(v14) <= u((arg1 + 2))):
                            break
                        if ((arg2 | v16) < 0):
                            break
                        v16 = load32((v10 + ((v8 + ((arg2 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((v8 + ((arg2 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg2 = (v7 + (v16 * 132))
                        if (load16u((v7 + (v16 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg2 + 122)):
                            break
                        arg2 = 1
                        # br_table[(load8u((v7 + (v16 * 132)) + 125) - 4)]
                        break
                        break
                    arg2 = arg6
                    break
                while True:  # block $label26
                    while True:  # block $label24
                        if (u(v8) >= u(v14)):
                            break
                        arg0 = (arg0 + 3)
                        while True:  # block $label25
                            if v9:
                                break
                            if ((v8 | v12) < 0):
                                break
                            v12 = load32((v10 + ((arg0 + ((v12 + v15) * v11)) << 2)))
                            if (u(load32((v10 + ((arg0 + ((v12 + v15) * v11)) << 2)))) < u(3)):
                                break
                            arg6 = (v7 + (v12 * 132))
                            if (load16u((v7 + (v12 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg6 + 122)):
                                break
                            arg6 = 1
                            # br_table[(load8u((v7 + (v12 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label27
                            arg6 = (arg1 - 1)
                            if (u(v14) <= u((arg1 - 1))):
                                break
                            if ((arg6 | v8) < 0):
                                break
                            v12 = load32((v10 + ((arg0 + (v11 * v19)) << 2)))
                            if (u(load32((v10 + ((arg0 + (v11 * v19)) << 2)))) < u(3)):
                                break
                            arg6 = (v7 + (v12 * 132))
                            if (load16u((v7 + (v12 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg6 + 122)):
                                break
                            arg6 = 1
                            # br_table[(load8u((v7 + (v12 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label28
                            if v18:
                                break
                            if ((arg1 | v8) < 0):
                                break
                            v12 = load32((v10 + ((arg0 + ((arg1 + v15) * v11)) << 2)))
                            if (u(load32((v10 + ((arg0 + ((arg1 + v15) * v11)) << 2)))) < u(3)):
                                break
                            arg6 = (v7 + (v12 * 132))
                            if (load16u((v7 + (v12 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg6 + 122)):
                                break
                            arg6 = 1
                            # br_table[(load8u((v7 + (v12 * 132)) + 125) - 4)]
                            break
                            break
                        while True:  # block $label29
                            arg6 = (arg1 + 1)
                            if (u(v14) <= u((arg1 + 1))):
                                break
                            if ((arg6 | v8) < 0):
                                break
                            v12 = load32((v10 + ((arg0 + ((arg6 + v15) * v11)) << 2)))
                            if (u(load32((v10 + ((arg0 + ((arg6 + v15) * v11)) << 2)))) < u(3)):
                                break
                            arg6 = (v7 + (v12 * 132))
                            if (load16u((v7 + (v12 * 132)) + 110) != arg3):
                                break
                            if (v13 != load8u(arg6 + 122)):
                                break
                            arg6 = 1
                            # br_table[(load8u((v7 + (v12 * 132)) + 125) - 4)]
                            break
                            break
                        arg1 = (arg1 + 2)
                        if (u(v14) <= u((arg1 + 2))):
                            break
                        if ((arg1 | v8) < 0):
                            break
                        arg0 = load32((v10 + ((arg0 + ((arg1 + v15) * v11)) << 2)))
                        if (u(load32((v10 + ((arg0 + ((arg1 + v15) * v11)) << 2)))) < u(3)):
                            break
                        arg1 = (v7 + (arg0 * 132))
                        if (load16u((v7 + (arg0 * 132)) + 110) != arg3):
                            break
                        if (v13 != load8u(arg1 + 122)):
                            break
                        arg6 = 1
                        # br_table[(load8u((v7 + (arg0 * 132)) + 125) - 4)]
                        break
                        break
                    arg6 = arg2
                    break
                if ((arg6 & 1) == 0):
                    break
                if arg4:
                    break
                break
            arg6 = 1
            if (arg4 == 0):
                break
            arg2 = (load32(9142440) + 2)
            v20 = ((arg0 + (((arg1 + ((load32(9142440) + 2) * v7)) + 1) * arg2)) + 1)
            v10 = load32(9142840)
            break
        store32((v10 + (v20 << 2)), arg5)
        arg6 = 1
        break
    return (arg6 & 1)

# ------------------------------------------------------------
# $func195
# ------------------------------------------------------------
def func195():
    v1 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v0 = load32(9681808)
    if load32(9681808):
        v6 = load32(((load8u((load32(9671128) + (v0 * 132)) + 122) * 404) + 9568096) + 144)
    while True:  # block $label0
        v2 = load32(9681812)
        if (load32(9681812) == 0):
            break
        v5 = load32(9671128)
        v3 = load8u((load32(9671128) + (v2 * 132)) + 122)
        v7 = load32(((load8u((load32(9671128) + (v2 * 132)) + 122) * 404) + 9568096) + 144)
        if (v0 == 0):
            break
        if (v0 == v2):
            break
        v0 = (v5 + (v0 * 132))
        v8 = ((load8u((v5 + (v0 * 132)) + 122) * 404) + 9568096)
        v9 = load16u(v0 + 112)
        v2 = (v5 + (v2 * 132))
        v5 = load16u((v5 + (v2 * 132)) + 112)
        v3 = ((v3 * 404) + 9568096)
        v10 = ((((load32(((load8u((v5 + (v0 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v0 + 112)) - (load16u((v5 + (v2 * 132)) + 112) + ((load32(((v3 * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1)))
        v0 = load16u(v0 + 114)
        v2 = load16u(v2 + 114)
        v3 = ((load16u(v0 + 114) + ((load32(v8 + 220) & 0xFFFFFFFF) >> 1)) - (load16u(v2 + 114) + ((load32(v3 + 220) & 0xFFFFFFFF) >> 1)))
        if ((((((((load32(((load8u((v5 + (v0 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v0 + 112)) - (load16u((v5 + (v2 * 132)) + 112) + ((load32(((v3 * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1))) * v10) + (((load16u(v0 + 114) + ((load32(v8 + 220) & 0xFFFFFFFF) >> 1)) - (load16u(v2 + 114) + ((load32(v3 + 220) & 0xFFFFFFFF) >> 1))) * v3)) - 1) < 82):
            break
        v4 = load32(9681804)
        v12 = 0.800000012
        v0 = (v0 - v2)
        v0 = (v9 - v5)
        v3 = (load32(9561692) + (load32(9142872) * 286704))
        if (load32((((load32(9561692) + (load32(9142872) * 286704)) + (load32(39108) << 2)) + 281808)) != 1):
        else:
        # TODO: f32.convert_i32_u []
        # TODO: f64.promote_f32 []
        v11 = ((((0.800000012 if (load32(((v3 + (load32(39168) << 2)) + 281808)) == 1) else 0.75) * (0.800000012 * v4)) / 500.0) + 0.5)
        if ((((((0.800000012 if (load32(((v3 + (load32(39168) << 2)) + 281808)) == 1) else 0.75) * (0.800000012 * v4)) / 500.0) + 0.5) < 4294967296.0) & (v11 >= 0.0)):
            # TODO: i32.trunc_f64_u []
            v4 = v11
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

# ------------------------------------------------------------
# $func196
# ------------------------------------------------------------
def func196(arg0, arg1, arg2, arg3, arg4):
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v6 = func197(arg0, arg1, arg2, arg3)
    while True:  # block $label0
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

# ------------------------------------------------------------
# $func197
# ------------------------------------------------------------
def func197(arg0, arg1, arg2, arg3):
    v4 = (G.global0 - 32)
    v5 = (load32(arg2 + 12) * load32(arg2 + 8))
    while True:  # block $label0
        while True:  # block $label1
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

# ------------------------------------------------------------
# $func198
# ------------------------------------------------------------
def func198(arg0):
    v1 = load32(9561692)
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
    v3 = (load32(((load8u(arg0 + 122) * 404) + 9568096) + 224) > 1)
    store32(arg0 + 52, (load32(arg0 + 52) + ((load32(arg0 + 84) & 1) if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 224) > 1) else 1)))
    store32(arg0 + 60, (load32(arg0 + 60) + (((v1 & 3) == 1) if v3 else v2)))
    while True:  # block $label0
        if (load32(arg0 + 92) == 0):
            break
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break

# ------------------------------------------------------------
# $func199
# ------------------------------------------------------------
def func199(arg0):
    v2 = (G.global0 - 112)
    G.global0 = (G.global0 - 112)
    while True:  # block $label0
        v1 = load32(arg0 + 12)
        if (load32(arg0 + 12) == 0):
            break
        v8 = load32(load32(v1))
        if (load32(load32(v1)) == 0):
            break
        if (load32(arg0 + 40) == 0):
            break
        v1 = load32(((load8u(arg0 + 122) * 404) + 9568096))
        if load8u(9142916):
            while True:  # block $label1
                if (v1 == 0):
                    break
                if (load32(v1 + 20) == 0):
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
            # TODO: f32.convert_i32_u []
            # TODO: f64.promote_f32 []
            store32(v2 + 88, (load32(9142848) * 25))
            a_b()
            break
        v6 = load32(v1 + 16)
        while True:  # block $label2
            v5 = load32(v1 + 20)
            if (load32(v1 + 20) == 0):
                v7 = load32(v1)
                break
            v7 = load8u(arg0 + 124)
            while True:  # block $label3
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
            # TODO: i32.div_u []
            break
        v4 = (v5 + v3)
        v3 = 0
        v5 = (v5 * v6)
        if (v5 * v6):
            v3 = (load32(v1 + 4) // v5)
        v5 = load16u(arg0 + 110)
        store32(v2 + 56, float((v6 << 16)))
        store32((v2 - -64), v8)
        store32(v2 + 48, (v5 + 16))
        # TODO: f32.convert_i32_u []
        # TODO: f64.promote_f32 []
        store32(v2 + 40, (load32(9142848) * 25))
        # TODO: f32.convert_i32_u []
        # TODO: f32.convert_i32_u []
        # TODO: f64.promote_f32 []
        store32(v2 + 32, ((((v3 * v7) * 6) + v4) / load32(59156)))
        a_b()
        # TODO: f32.convert_i32_u []
        v12 = (load16u(arg0 + 114) * 32.0)
        # TODO: f32.convert_i32_u []
        v13 = (load16u(arg0 + 112) * 32.0)
        while True:  # block $label4
            if (load8u(9142916) == 0):
                v11 = float(load32(v1 + 8))
                v15 = 32.0
                break
            # TODO: f32.convert_i32_u []
            # TODO: f64.promote_f32 []
            v15 = ((16.0 / (load32(9142440) * 96)) + 0.25)
            break
        v14 = 0.0
        store32(v2 + 24, v8)
        store32(v2 + 16, v15)
        # TODO: f64.promote_f32 []
        store32(v2 + 8, (v12 - v14))
        # TODO: f64.promote_f32 []
        store32(v2, (v13 - v11))
        a_b()
        break
    G.global0 = (v2 + 112)
    return v2

# ------------------------------------------------------------
# $func200
# ------------------------------------------------------------
def func200(arg0, arg1, arg2, arg3):
    while True:  # block $label0
        v7 = load32(9561692)
        v5 = load16u(arg0 + 110)
        v10 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
        if (load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 286684) == 0):
            break
        v12 = load8u(arg0 + 122)
        v31 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 264)
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) == 1):
            break
        if (load32(38456) == v12):
            break
        if (load32(38764) == v12):
            break
        while True:  # block $label1
            v4 = load32(v10 + 283904)
            if ((load32(v10 + 283904) | arg1) == 0):
                break
            if (arg1 == 0):
                v25 = (load32(9142892) * v5)
                v26 = ((v12 * 404) + 9568096)
                v27 = load32(9671128)
                v17 = (load32(9671128) + (load32(arg0 + 28) * 132))
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
                    while True:  # block $label2
                        v7 = load32(((v37 + (v19 << 2)) + 284636))
                        if (load32(((v37 + (v19 << 2)) + 284636)) == 0):
                            break
                        v38 = load32(v7 + 8)
                        if (load32(v7 + 8) == 0):
                            break
                        v39 = load32(v7)
                        v20 = 0
                        while True:  # $label19
                            while True:  # block $label3
                                v7 = load32((v39 + (v20 << 2)))
                                if (load32((v39 + (v20 << 2))) == 0):
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
                                if (func162(arg0, load8u(v5 + 122), 0, 0) == 0):
                                    break
                                if (v9 == v36):
                                    break
                                v4 = load16u(v5 + 110)
                                while True:  # block $label4
                                    v6 = load16u(v5 + 120)
                                    if load16u(v5 + 120):
                                    else:
                                    if (load8u(((v6 if load8u((v30 + (v4 + v25))) else v4) + (v4 + v25))) == 0):
                                        if (load8u(v5 + 127) != 6):
                                            break
                                        if (load8u(v5 + 128) == 0):
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
                                v13 = ((v9 * 404) + 9568096)
                                v4 = load32(((v9 * 404) + 9568096) + 264)
                                if (load32(((v9 * 404) + 9568096) + 264) == 2):
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
                                while True:  # block $label7
                                    while True:  # block $label5
                                        while True:  # block $label6
                                            # br_table[v4]
                                            break
                                            break
                                        v8 = 0
                                        v11 = load32(v13 + 216)
                                        if (load32(v13 + 216) == 0):
                                            break
                                        v14 = load32(v13 + 220)
                                        if (load32(v13 + 220) == 0):
                                            break
                                        if (v16 == 0):
                                            break
                                        if (v10 == 0):
                                            break
                                        v15 = load32(v16)
                                        v6 = 0
                                        while True:  # $label9
                                            v24 = (v6 + v22)
                                            v4 = 0
                                            while True:  # $label8
                                                v8 = load32((v10 + ((v24 + ((v4 + v21) * v18)) << 2)))
                                                if (load32((v15 + (load32((v10 + ((v24 + ((v4 + v21) * v18)) << 2))) << 2))) == 0):
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
                                    if (v10 == 0):
                                        v8 = 0
                                        break
                                    v8 = load32((v10 + (((v18 * v21) + v22) << 2)))
                                    break
                                while True:  # block $label12
                                    while True:  # block $label10
                                        while True:  # block $label11
                                            # br_table[v31]
                                            break
                                            break
                                        v6 = 0
                                        v14 = load32(v26 + 216)
                                        if (load32(v26 + 216) == 0):
                                            break
                                        v15 = load32(v26 + 220)
                                        if (load32(v26 + 220) == 0):
                                            break
                                        if (v16 == 0):
                                            break
                                        if (v10 == 0):
                                            break
                                        v24 = load32(v16)
                                        v11 = 0
                                        while True:  # $label14
                                            v40 = (v11 + v28)
                                            v4 = 0
                                            while True:  # $label13
                                                v6 = load32((v10 + ((v40 + ((v4 + v29) * v18)) << 2)))
                                                if (load32((v24 + (load32((v10 + ((v40 + ((v4 + v29) * v18)) << 2))) << 2))) == 0):
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
                                    if (v10 == 0):
                                        v6 = 0
                                        break
                                    v6 = load32(v32)
                                    break
                                if (v6 != v8):
                                    break
                                v4 = load32(v5 + 100)
                                if load32(v5 + 100):
                                    v4 = (v27 + (v4 * 132))
                                    # TODO: i32.div_u []
                                    if (u((load32((((load8u((v27 + (v4 * 132)) + 122) * 1020) + 9299904) + (v9 << 2))) * load32(v4 + 52))) < u(100)):
                                        break
                                while True:  # block $label15
                                    v4 = load32(((load8u(v17 + 122) * 404) + 9568096) + 228)
                                    if (load32(((load8u(v17 + 122) * 404) + 9568096) + 228) == 0):
                                        break
                                    v9 = load32(v13 + 216)
                                    if (load32(v13 + 216) == 0):
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
                                        while True:  # block $label17
                                            while True:  # $label16
                                                v15 = (v23 - (v8 + v22))
                                                if (u(v13) > u((((v23 - (v8 + v22)) * v15) + v14))):
                                                    v8 = (v8 + 1)
                                                    if (v9 != (v8 + 1)):
                                                        continue
                                                    break
                                                break
                                            if ((v6 & 1) == 0):
                                                break
                                            break
                                            break
                                        v4 = (v4 + 1)
                                        v6 = (u((v4 + 1)) < u(v9))
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
                if (arg1 == 0):
                    break
            if (arg2 == 0):
                if arg3:
                    store8(arg0 + 125, 0)
                return 1
            store32(arg0 + 32, arg1)
            return 1
            break
        store8(arg0 + 129, 0)
        break
    return 0

# ------------------------------------------------------------
# $func201
# ------------------------------------------------------------
def func201(arg0):
    v1 = load32(arg0 + 24)
    if (load32(arg0 + 24) == 0):
        v1 = func26(16)
        store64(func26(16), 0)
        store64(v1 + 8, 0)
        store32(arg0 + 24, v1)
    if (load32(v1 + 8) == 0):
        v2 = func26(16)
        store32(func26(16) + 4, 20)
        store32(v2, func26(80))
        store64(v2 + 8, 8589934592)
        store32(v1 + 8, v2)
        v1 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 196)
        v6 = ((load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 283936) * 20) % load16u(((load32(((load8u(arg0 + 122) * 404) + 9568096) + 196) << 1) + 9142944)))
        v7 = ((v1 << 2) + 9142928)
        while True:  # $label1
            v8 = load16u((load32(v7) + ((v5 + v6) << 1)))
            if load16u((load32(v7) + ((v5 + v6) << 1))):
                while True:  # block $label0
                    v1 = load32(load32(arg0 + 24) + 8)
                    v2 = load32(load32(load32(arg0 + 24) + 8) + 8)
                    if (load32(load32(load32(arg0 + 24) + 8) + 8) != load32(v1 + 4)):
                        v3 = load32(v1)
                        break
                    v3 = (load32(v1 + 12) + v2)
                    store32(v1 + 4, (load32(v1 + 12) + v2))
                    v4 = load32(v1)
                    v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                    if v2:
                        # TODO: memory.copy []
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

# ------------------------------------------------------------
# $func202
# ------------------------------------------------------------
def func202(arg0, arg1, arg2):
    v3 = load32(arg0 + 16)
    if load32(arg0 + 16):
        v4 = load32(v3 + 8)
        v5 = func26((-1 if (u(v4) > u(1073741823)) else (load32(v3 + 8) << 2)))
        while True:  # block $label0
            if (v4 == 0):
                break
            v7 = load32(v3)
            v3 = 0
            if (u(v4) >= u(4)):
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
            if (v4 == 0):
                break
            v3 = 0
            while True:  # $label3
                v3 = (v3 + 1)
                if ((v3 + 1) != v4):
                    continue
                break
            break
        while True:  # block $label4
            if (arg1 == 0):
                break
            if load8u(9147210):
                if (load32(59164) != load32(9142384)):
                    break
            if (v4 == 0):
                break
            arg1 = load32(9671128)
            v3 = 0
            while True:  # $label5
                arg2 = (arg1 + (load32((v5 + (v3 << 2))) * 132))
                if (load32((arg1 + (load32((v5 + (v3 << 2))) * 132)) + 36) == 0):
                    func44(arg2, 0)
                    arg1 = load32(9671128)
                v3 = (v3 + 1)
                if ((v3 + 1) != v4):
                    continue
                break
            break
    while True:  # block $label6
        if (load32(arg0 + 92) == 0):
            break
        arg1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break

# ------------------------------------------------------------
# $func203
# ------------------------------------------------------------
def func203(arg0):
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) != 1):
            break
        if load32(arg0 + 80):
            break
        v3 = load16u(arg0 + 116)
        if (load16u(arg0 + 116) == 0):
            break
        v4 = load16u(arg0 + 118)
        if (load16u(arg0 + 118) == 0):
            break
        if (load8u(9147152) == 0):
            if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(arg0 + 110))))) == 0):
                break
            if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                break
            if (load8u(arg0 + 127) == 6):
                break
        while True:  # block $label1
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
            if (u(v5) < u(load32(9163784))):
                break
            store32(v2, v6)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            v4 = load16u(arg0 + 118)
            v3 = load16u(arg0 + 116)
            break
        store32(arg0 + 80, v1)
        # TODO: f32.convert_i32_u []
        break
    G.global0 = (v2 + 16)

# ------------------------------------------------------------
# $func204
# ------------------------------------------------------------
def func204(arg0, arg1):
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # block $label0
        if (load8u(arg0 + 125) == 3):
            break
        if (load8u(arg0 + 128) == 0):
            break
        store8(arg0 + 127, 0)
        while True:  # block $label1
            v3 = load32(arg0 + 40)
            if (load32(arg0 + 40) == 0):
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
    while True:  # block $label2
        if (load8u(9142916) == 0):
            break
        v3 = load32(arg0 + 40)
        if (load32(arg0 + 40) == 0):
            break
        store32(v2 + 20, v3)
        store32(v2 + 16, -13487182)
        a_b()
        break
    func119((v2 + 16), arg0, 0, 1)
    func156(1061, arg0, 500)
    while True:  # block $label3
        arg1 = load16u(arg0 + 112)
        v3 = ((load16u(arg0 + 112) << 5) - load32(9142952))
        v3 = load16u(arg0 + 114)
        v4 = ((load16u(arg0 + 114) << 5) - load32(9142956))
        if ((((((load16u(arg0 + 112) << 5) - load32(9142952)) * v3) + (((load16u(arg0 + 114) << 5) - load32(9142956)) * v4)) - 1) > 9000000):
            break
        v5 = load32(39880)
        while True:  # block $label4
            v6 = load32(load32(9142424) + 48)
            if (load32(load32(9142424) + 48) == 0):
                break
            if load8u(9147152):
                break
            v4 = load16u((load32(9147376) + (((load32(9142440) * v3) + arg1) << 1)))
            if (v6 == 2):
                if (u(v4) > u(1)):
                    break
                break
            if (v4 == 0):
                break
            break
        store32(v2 + 8, v3)
        store32(v2 + 4, arg1)
        store32(v2, v5)
        a_b()
        break
    func77(arg0)
    G.global0 = (v2 - -64)

# ------------------------------------------------------------
# $func205
# ------------------------------------------------------------
def func205(arg0, arg1):
    while True:  # block $label0
        v3 = load8u(arg0 + 122)
        if (load8u(arg0 + 122) == load32(38500)):
            break
        v2 = load16u(arg0 + 110)
        arg1 = (load32(9142892) * arg1)
        v4 = load32(9143004)
        while True:  # block $label1
            v5 = load16u(arg0 + 120)
            if load16u(arg0 + 120):
            else:
            if (load8u(((v5 if load8u((v4 + (arg1 + v2))) else v2) + (v2 + arg1))) == 0):
                v2 = 0
                if (load8u(arg0 + 127) != 6):
                    break
                if (load8u(arg0 + 128) == 0):
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
        arg1 = ((v3 * 404) + 9568096)
        v4 = load32(((v3 * 404) + 9568096) + 264)
        if (load32(((v3 * 404) + 9568096) + 264) == 2):
            break
        v2 = ((((((load32(arg1 + 188) == 55) & (load32(38560) != v3)) & (load32(38620) != v3)) & (load32(38564) != v3)) & (v4 == 1)) & (u(arg0) > u(1)))
        break
    return v2

# ------------------------------------------------------------
# $func206
# ------------------------------------------------------------
def func206(arg0):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if (load8u(arg0 + 126) == 1):
            break
        v1 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 296)
        v2 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
        v3 = load32(((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 284144))
        store8(arg0 + 126, 1)
        # TODO: i32.div_u []
        store32(load32(arg0 + 52) + 52, ((v1 * v3) + 100))
        while True:  # block $label1
            if (load32(arg0 + 92) == 0):
                break
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
        v1 = load16u(arg0 + 114)
        v2 = load16u(arg0 + 112)
        while True:  # block $label4
            while True:  # block $label3
                while True:  # block $label2
                    v6 = load32(load32(9142424) + 48)
                    if load32(load32(9142424) + 48):
                        if (load8u(9147152) == 0):
                            break
                    v3 = load32(9142440)
                    break
                    break
                v3 = load32(9142440)
                v5 = load16u((load32(9147376) + (((load32(9142440) * v1) + v2) << 1)))
                if (v6 == 2):
                    if (u(v5) > u(1)):
                        break
                    break
                if (v5 == 0):
                    break
                break
            # TODO: f32.convert_i32_u []
            # TODO: f32.convert_i32_u []
            # TODO: f32.convert_i32_u []
            func80(v2, v1, load32(9142460), 32.0, (v3 * 96))
            v1 = load16u(arg0 + 114)
            v2 = load16u(arg0 + 112)
            break
        arg0 = ((v2 << 5) - load32(9142952))
        arg0 = ((v1 << 5) - load32(9142956))
        if ((((((v2 << 5) - load32(9142952)) * arg0) + (((v1 << 5) - load32(9142956)) * arg0)) - 1) > 9000000):
            break
        v3 = load32(39884)
        while True:  # block $label5
            v5 = load32(load32(9142424) + 48)
            if (load32(load32(9142424) + 48) == 0):
                break
            if load8u(9147152):
                break
            arg0 = load16u((load32(9147376) + (((load32(9142440) * v1) + v2) << 1)))
            if (v5 == 2):
                if (u(arg0) > u(1)):
                    break
                break
            if (arg0 == 0):
                break
            break
        store32(v4 + 8, v1)
        store32(v4 + 4, v2)
        store32(v4, v3)
        a_b()
        break
    G.global0 = (v4 + 16)

# ------------------------------------------------------------
# $func207
# ------------------------------------------------------------
def func207(arg0, arg1):
    while True:  # block $label2
        while True:  # block $label1
            while True:  # block $label0
                v3 = load32(arg0 + 20)
                if (load32(arg0 + 20) == 0):
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
                if (load32(v3 + 4) == 0):
                    break
                v2 = v3
                break
            v6 = load32(v2)
            break
            break
        v2 = load32(v3 + 12)
        store32(v3 + 4, load32(v3 + 12))
        v5 = load32(v3)
        v6 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
        v2 = v3
        if v5:
            v4 = load32(v3 + 8)
            v2 = load32(arg0 + 20)
        store32(v3, v6)
        break
    store32(v7, (v4 + 1))
    store32((v6 + (v4 << 2)), 2)
    while True:  # block $label3
        arg0 = load32(v2 + 8)
        if (load32(v2 + 8) != load32(v2 + 4)):
            v4 = load32(v2)
            break
        v3 = (load32(v2 + 12) + arg0)
        store32(v2 + 4, (load32(v2 + 12) + arg0))
        v5 = load32(v2)
        v4 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
        if arg0:
            # TODO: memory.copy []
        if v5:
            arg0 = load32(v2 + 8)
        store32(v2, v4)
        break
    store32(v2 + 8, (arg0 + 1))
    store32((v4 + (arg0 << 2)), arg1)

# ------------------------------------------------------------
# $func208
# ------------------------------------------------------------
def func208(arg0, arg1, arg2, arg3):
    v8 = (load32(9142892) * arg2)
    v19 = load32(9142440)
    v10 = (load32(9142440) + 2)
    v22 = ((load32(9142440) + 2) << 1)
    v12 = load32(38564)
    v13 = load32(38620)
    v14 = load32(38560)
    v9 = load32(9143004)
    v15 = load32(38500)
    v16 = load32(9671128)
    v17 = load32(9142840)
    arg2 = 0
    while True:  # block $label4
        while True:  # $label10
            while True:  # block $label0
                v20 = arg2
                v4 = (arg2 << 2)
                arg2 = (load32((((arg2 << 2) | 4) + 8611904)) + arg1)
                if (u(v19) <= u((load32((((arg2 << 2) | 4) + 8611904)) + arg1))):
                    break
                v4 = (load32((v4 + 8611904)) + arg0)
                if (u(v19) <= u((load32((v4 + 8611904)) + arg0))):
                    break
                if ((arg2 | v4) < 0):
                    break
                while True:  # block $label1
                    v11 = (v4 + 1)
                    v21 = (arg2 + 1)
                    arg2 = load32((v17 + (((v4 + 1) + ((arg2 + 1) * v10)) << 2)))
                    if (u(load32((v17 + (((v4 + 1) + ((arg2 + 1) * v10)) << 2)))) < u(3)):
                        break
                    v7 = 0
                    while True:  # block $label2
                        v4 = (v16 + (arg2 * 132))
                        v6 = load8u((v16 + (arg2 * 132)) + 122)
                        if (v15 == load8u((v16 + (arg2 * 132)) + 122)):
                            break
                        v5 = load16u(v4 + 110)
                        while True:  # block $label3
                            v18 = load16u(v4 + 120)
                            if load16u(v4 + 120):
                            else:
                            if (load8u(((v18 if load8u((v9 + (v5 + v8))) else v5) + (v5 + v8))) == 0):
                                if (load8u(v4 + 127) != 6):
                                    break
                                if (load8u(v4 + 128) == 0):
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
                        v5 = ((v6 * 404) + 9568096)
                        if (load32(((v6 * 404) + 9568096) + 264) == 2):
                            break
                        v7 = ((((load32(v5 + 188) == 55) & (v6 != v14)) & (v6 != v13)) & (v6 != v12))
                        break
                    if v7:
                        break
                    if (u(load32(v4 + 84)) >= u(arg3)):
                        break
                    if load32(((v6 * 404) + 9568096) + 304):
                        break
                    break
                while True:  # block $label5
                    arg2 = load32((v17 + ((v11 + ((v10 + v21) * v10)) << 2)))
                    if (u(load32((v17 + ((v11 + ((v10 + v21) * v10)) << 2)))) < u(3)):
                        break
                    v7 = 0
                    while True:  # block $label6
                        v4 = (v16 + (arg2 * 132))
                        v6 = load8u((v16 + (arg2 * 132)) + 122)
                        if (v15 == load8u((v16 + (arg2 * 132)) + 122)):
                            break
                        v5 = load16u(v4 + 110)
                        while True:  # block $label7
                            v18 = load16u(v4 + 120)
                            if load16u(v4 + 120):
                            else:
                            if load8u(((v18 if load8u((v9 + (v5 + v8))) else v5) + (v5 + v8))):
                                if (load8u(v4 + 128) == 0):
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
                        v5 = ((v6 * 404) + 9568096)
                        if (load32(((v6 * 404) + 9568096) + 264) == 2):
                            break
                        v7 = ((((load32(v5 + 188) == 55) & (v6 != v14)) & (v6 != v13)) & (v6 != v12))
                        break
                    if v7:
                        break
                    if (u(load32(v4 + 84)) >= u(arg3)):
                        break
                    if load32(((v6 * 404) + 9568096) + 304):
                        break
                    break
                arg2 = load32((v17 + ((v11 + ((v21 + v22) * v10)) << 2)))
                if (u(load32((v17 + ((v11 + ((v21 + v22) * v10)) << 2)))) < u(3)):
                    break
                v6 = 0
                while True:  # block $label8
                    v4 = (v16 + (arg2 * 132))
                    v5 = load8u((v16 + (arg2 * 132)) + 122)
                    if (v15 == load8u((v16 + (arg2 * 132)) + 122)):
                        break
                    v7 = load16u(v4 + 110)
                    while True:  # block $label9
                        v11 = load16u(v4 + 120)
                        if load16u(v4 + 120):
                        else:
                        if load8u(((v11 if load8u((v9 + (v7 + v8))) else v7) + (v7 + v8))):
                            if (load8u(v4 + 128) == 0):
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
                    v7 = ((v5 * 404) + 9568096)
                    if (load32(((v5 * 404) + 9568096) + 264) == 2):
                        break
                    v6 = ((((load32(v7 + 188) == 55) & (v5 != v14)) & (v5 != v13)) & (v5 != v12))
                    break
                if v6:
                    break
                if (u(load32(v4 + 84)) >= u(arg3)):
                    break
                if load32(((v5 * 404) + 9568096) + 304):
                    break
                break
            arg2 = (v20 + 2)
            if (u(v20) < u(1678)):
                continue
            break
        arg2 = 0
        break
    return arg2

# ------------------------------------------------------------
# $func209
# ------------------------------------------------------------
def func209(arg0):
    while True:  # block $label0
        v1 = arg0
        if (arg0 & 3):
            while True:  # $label1
                if (load8u(v1) == 0):
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) & 3):
                    continue
                break
        while True:  # $label2
            v2 = v1
            v1 = (v1 + 4)
            v3 = load32(v2)
            if ((((load32(v2) ^ -1) & (v3 - 16843009)) & -2139062144) == 0):
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

# ------------------------------------------------------------
# $func210
# ------------------------------------------------------------
def func210(arg0, arg1, arg2):
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label1
        if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
        else:
        v4 = 10
        while True:  # block $label0
            if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
                break
            break
        v3 = (load8u(arg0 + 11) & 127)
        if (u(10) <= u((load32(arg0 + 4) - (load8u(arg0 + 11) & 127)))):
            if (arg2 == 0):
                break
            while True:  # block $label2
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

# ------------------------------------------------------------
# $func216
# ------------------------------------------------------------
def func216(arg0, arg1, arg2, arg3, arg4):
    while True:  # block $label0
        v5 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            v6 = load32(arg0)
            break
        v6 = (load32(arg0 + 12) + v5)
        store32(arg0 + 4, (load32(arg0 + 12) + v5))
        v7 = load32(arg0)
        v6 = func26((-1 if (u(v6) > u(1073741823)) else (v6 << 2)))
        if v5:
            # TODO: memory.copy []
        if v7:
            v5 = load32(arg0 + 8)
        store32(arg0, v6)
        break
    store32(arg0 + 8, (v5 + 1))
    store32((v6 + (v5 << 2)), arg1)
    while True:  # block $label1
        v5 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            arg1 = v6
            break
        arg1 = (load32(arg0 + 12) + v5)
        store32(arg0 + 4, (load32(arg0 + 12) + v5))
        arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
        if v5:
            # TODO: memory.copy []
        store32(arg0, arg1)
        v5 = load32(arg0 + 8)
        break
    store32(arg0 + 8, (v5 + 1))
    store32((arg1 + (v5 << 2)), arg2)
    while True:  # block $label2
        v5 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            v6 = arg1
            break
        arg2 = (load32(arg0 + 12) + v5)
        store32(arg0 + 4, (load32(arg0 + 12) + v5))
        v6 = func26((-1 if (u(arg2) > u(1073741823)) else (arg2 << 2)))
        if v5:
            # TODO: memory.copy []
        store32(arg0, v6)
        v5 = load32(arg0 + 8)
        break
    store32(arg0 + 8, (v5 + 1))
    store32((v6 + (v5 << 2)), arg3)
    while True:  # block $label3
        v5 = load32(arg0 + 8)
        if (load32(arg0 + 8) != load32(arg0 + 4)):
            arg1 = v6
            break
        arg1 = (load32(arg0 + 12) + v5)
        store32(arg0 + 4, (load32(arg0 + 12) + v5))
        arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
        if v5:
            # TODO: memory.copy []
        store32(arg0, arg1)
        v5 = load32(arg0 + 8)
        break
    store32(arg0 + 8, (v5 + 1))
    store32((arg1 + (v5 << 2)), arg4)

# ------------------------------------------------------------
# $xa
# Export: xa
# ------------------------------------------------------------
def xa():
    """Exported as xa."""
    if (load8u(9147126) == 0):
        v0 = load32(9142892)
        v1 = load32(41092)
        v2 = load8u(9147212)
        v5 = (load32(9142892) if load8u(9147212) else load32(41092))
        v6 = (((load32(9142892) if load8u(9147212) else load32(41092)) * 45) - 41)
        v3 = func26((-1 if (u(v6) > u(1073741823)) else ((((load32(9142892) if load8u(9147212) else load32(41092)) * 45) - 41) << 2)))
        store32(func26((-1 if (u(v6) > u(1073741823)) else ((((load32(9142892) if load8u(9147212) else load32(41092)) * 45) - 41) << 2))) + 8, v2)
        store32(v3 + 4, v1)
        store32(v3, v0)
        store32(v3 + 12, load8u(9561848))
        if (u(v5) >= u(2)):
            v7 = load32(9561692)
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

# ------------------------------------------------------------
# $func218
# ------------------------------------------------------------
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

# ------------------------------------------------------------
# $func219
# ------------------------------------------------------------
def func219():
    while True:  # block $label0
        v5 = load32(9142432)
        if (load32(9142432) == 0):
            break
        while True:  # block $label1
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
        while True:  # block $label13
            while True:  # block $label2
                v4 = load32(9142440)
                if (load32(9142440) <= 0):
                    v0 = v4
                    break
                v0 = v4
                while True:  # $label12
                    v3 = 0
                    while True:  # $label11
                        v1 = ((v0 * v3) + v8)
                        if (load32((v5 + (((v0 * v3) + v8) << 2))) == 0):
                            v5 = 0
                            v0 = load8s((load32(9147288) + v1))
                            if (load8s((load32(9147288) + v1)) >= 0):
                                v5 = (load32(load32((load32(9140332) + ((v0 & 255) << 2))) + 32) == 23)
                            while True:  # block $label3
                                v2 = load32(9215880)
                                v0 = load32(load32(9215880) + 8)
                                if (load32(load32(9215880) + 8) != load32(v2 + 4)):
                                    v1 = load32(v2)
                                    break
                                v1 = (load32(v2 + 12) + v0)
                                store32(v2 + 4, (load32(v2 + 12) + v0))
                                v6 = load32(v2)
                                v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
                                if v0:
                                    # TODO: memory.copy []
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
                                # TODO: i32.div_u []
                                v17 = load32(9142440)
                                v18 = (v0 - (load32(9142440) * v0))
                                v12 = 0
                                while True:  # $label9
                                    while True:  # block $label4
                                        v2 = load32(9142440)
                                        v1 = (v12 << 3)
                                        v0 = (load32(((v12 << 3) + 8932)) + v17)
                                        if (u(load32(9142440)) <= u((load32(((v12 << 3) + 8932)) + v17))):
                                            break
                                        v1 = (load32((v1 + 8928)) + v18)
                                        if (u(v2) <= u((load32((v1 + 8928)) + v18))):
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
                                                    if (u((v0 + 2)) < u(v6)):
                                                        continue
                                                    break
                                            while True:  # block $label6
                                                if (load32(v1 + 4) != v6):
                                                    v0 = load32(v1)
                                                    break
                                                v0 = (load32(v1 + 12) + v6)
                                                store32(v1 + 4, (load32(v1 + 12) + v6))
                                                v2 = load32(v1)
                                                v0 = func26((-1 if (u(v0) > u(1073741823)) else (v0 << 2)))
                                                if v6:
                                                    # TODO: memory.copy []
                                                if v2:
                                                    v6 = load32(v1 + 8)
                                                store32(v1, v0)
                                                v10 = load32(9142432)
                                                break
                                            v2 = load32(9215876)
                                            store32(v1 + 8, (v6 + 1))
                                            store32((v0 + (v6 << 2)), v7)
                                            v10 = load32((v10 + v19))
                                            while True:  # block $label7
                                                v0 = load32(v2 + 8)
                                                if (load32(v2 + 8) != load32(v2 + 4)):
                                                    v1 = load32(v2)
                                                    break
                                                v1 = (load32(v2 + 12) + v0)
                                                store32(v2 + 4, (load32(v2 + 12) + v0))
                                                v6 = load32(v2)
                                                v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
                                                if v0:
                                                    # TODO: memory.copy []
                                                if v6:
                                                    v0 = load32(v2 + 8)
                                                store32(v2, v1)
                                                break
                                            store32(v2 + 8, (v0 + 1))
                                            store32((v1 + (v0 << 2)), v10)
                                            break
                                        v1 = load8u((load32(9147288) + v0))
                                        # TODO: i32.extend8_s []
                                        v2 = load8u((load32(9147288) + v0))
                                        while True:  # block $label8
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
                                if (u((v11 + 1)) < u(v9)):
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
        while True:  # block $label14
            v0 = (v0 * v0)
            if ((v0 * v0) == 0):
                break
            v8 = 0
            v3 = 0
            if (u(v0) >= u(4)):
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
            if ((v0 & 3) == 0):
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
        while True:  # block $label17
            if v2:
                break
            v3 = 0
            v5 = load32(9684492)
            v8 = load32(load32(9215880))
            if (v7 != 1):
                v1 = (v7 & -2)
                v0 = 0
                while True:  # $label20
                    while True:  # block $label18
                        v4 = (v3 << 2)
                        if load32((v8 + (v3 << 2))):
                            break
                        if (u(load32((v4 + 59200))) <= u(load32(((v5 << 2) + 59200)))):
                            break
                        store32(9684492, v3)
                        v5 = v3
                        break
                    while True:  # block $label19
                        v4 = (v3 | 1)
                        v2 = ((v3 | 1) << 2)
                        if load32((v8 + ((v3 | 1) << 2))):
                            break
                        if (u(load32((v2 + 59200))) <= u(load32(((v5 << 2) + 59200)))):
                            break
                        store32(9684492, v4)
                        v5 = v4
                        break
                    v3 = (v3 + 2)
                    v0 = (v0 + 2)
                    if ((v0 + 2) != v1):
                        continue
                    break
            if ((v7 & 1) == 0):
                break
            v0 = (v3 << 2)
            if load32((v8 + (v3 << 2))):
                break
            if (u(load32((v0 + 59200))) <= u(load32(((v5 << 2) + 59200)))):
                break
            store32(9684492, v3)
            break
        v8 = 0
        v0 = (v7 * v7)
        v5 = func26((v7 * v7))
        # TODO: memory.fill []
        store32(9684440, v7)
        store32(9684436, v5)
        v0 = load32(9215876)
        v4 = load32(load32(9215876) + 8)
        if (load32(load32(9215876) + 8) == 0):
            break
        v3 = ((((v4 - 1) & 0xFFFFFFFF) >> 1) + 1)
        v2 = (((((v4 - 1) & 0xFFFFFFFF) >> 1) + 1) & 1)
        v0 = load32(v0)
        if (u(v4) >= u(3)):
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
        if (v2 == 0):
            break
        v4 = (v8 << 2)
        v3 = load32((v0 + ((v8 << 2) | 4)))
        v0 = load32((v0 + v4))
        store8((v5 + ((load32((v0 + ((v8 << 2) | 4))) * v7) + load32((v0 + v4)))), 1)
        store8((v5 + (v3 + (v0 * v7))), 1)
        break
    return v0

# ------------------------------------------------------------
# $func220
# ------------------------------------------------------------
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
                if (((v1 | 3) == 71) == 0):
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

# ------------------------------------------------------------
# $func221
# ------------------------------------------------------------
def func221(arg0):
    arg0 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v1 = load16u((load32(9671128) + (load32(9173808) * 132)) + 110)
    store32(9671124, 240)
    store32(9671120, 0)
    v2 = load32(9561692)
    a_b()
    while True:  # block $label0
        v2 = (v2 + (v1 * 286704))
        v1 = load32((v2 + (v1 * 286704)) + 281792)
        if (load32((v2 + (v1 * 286704)) + 281792) == 0):
            break
        if (load32(v1 + 8) == 0):
            break
        v2 = (v2 + 281792)
        while True:  # $label1
            v4 = (v3 << 2)
            if load32(((v3 << 2) + load32(v1))):
                v1 = load32(9671120)
                store32(9671120, (load32(9671120) + 1))
                store32(((v1 << 2) + 9263072), 9256340)
                v1 = load32(((load16u((load32(load32(v2)) + v4)) * 404) + 9568096) + 144)
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
            if (u((v3 + 1)) < u(load32(v1 + 8))):
                continue
            break
        break
    G.global0 = (arg0 + 48)

# ------------------------------------------------------------
# $func222
# ------------------------------------------------------------
def func222(arg0):
    arg0 = 0
    store32(9671124, 95)
    store32(9671120, 0)
    while True:  # block $label0
        v3 = (load32(9671128) + (load32(9173808) * 132))
        v1 = load32((load32(9671128) + (load32(9173808) * 132)) + 20)
        if (load32((load32(9671128) + (load32(9173808) * 132)) + 20) == 0):
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
        if (load32(v1 + 28) == 0):
            break
        store32(((arg0 << 2) + 9263072), load32(((v1 * 404) + 9567872)))
        store32(9671120, (arg0 + 1))
        break
    return func46(0, 1)

# ------------------------------------------------------------
# $func223
# ------------------------------------------------------------
def func223(arg0):
    arg0 = 0
    store32(9671124, 96)
    store32(9671120, 0)
    while True:  # block $label0
        v3 = (load32(9671128) + (load32(9173808) * 132))
        v1 = load32((load32(9671128) + (load32(9173808) * 132)) + 20)
        if (load32((load32(9671128) + (load32(9173808) * 132)) + 20) == 0):
            break
        v1 = load32(v1)
        v2 = load32(load32(v1) + 32)
        if load32(load32(v1) + 32):
            store32(9263072, load32(((v2 * 404) + 9567872)))
            store32(9671120, 1)
            v1 = load32(load32(v3 + 20))
            arg0 = 1
        v2 = load32(v1 + 36)
        if load32(v1 + 36):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 40)
        if load32(v1 + 40):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 44)
        if load32(v1 + 44):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 48)
        if load32(v1 + 48):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 52)
        if load32(v1 + 52):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
            v1 = load32(load32(v3 + 20))
        v2 = load32(v1 + 56)
        if load32(v1 + 56):
            store32(((arg0 << 2) + 9263072), load32(((v2 * 404) + 9567872)))
            arg0 = (arg0 + 1)
            store32(9671120, (arg0 + 1))
        else:
        v1 = load32(v1 + 60)
        if (load32(v1 + 60) == 0):
            break
        store32(((arg0 << 2) + 9263072), load32(((v1 * 404) + 9567872)))
        store32(9671120, (arg0 + 1))
        break
    return func46(0, 1)

# ------------------------------------------------------------
# $func224
# ------------------------------------------------------------
def func224(arg0, arg1, arg2):
    v4 = load32(9142440)
    v6 = (load32(9142440) + 2)
    v7 = ((load32(9142440) + 2) if (arg1 != 2) else 0)
    v5 = ((load8u(arg0 + 122) * 404) + 9568096)
    v8 = (load16u(arg0 + 114) + ((load32(((load8u(arg0 + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1))
    v9 = (load16u(arg0 + 112) + ((load32(v5 + 216) & 0xFFFFFFFF) >> 1))
    v5 = load32(9671128)
    v10 = load32(9142840)
    while True:  # block $label1
        while True:  # block $label3
            if arg2:
                while True:  # $label2
                    while True:  # block $label0
                        arg0 = v3
                        v3 = (v3 << 2)
                        arg1 = (v8 + load32((((v3 << 2) | 4) + 8611904)))
                        if (u(v4) <= u((v8 + load32((((v3 << 2) | 4) + 8611904))))):
                            break
                        v3 = (v9 + load32((v3 + 8611904)))
                        if (u(v4) <= u((v9 + load32((v3 + 8611904))))):
                            break
                        if ((arg1 | v3) < 0):
                            break
                        v3 = load32((((v3 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4)
                        if (load8u((v5 + (load32((((v3 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4) * 132)) + 122) == arg2):
                            break
                        break
                    v3 = (arg0 + 2)
                    if (u(arg0) <= u(717)):
                        continue
                    break
                    break
                raise RuntimeError('unreachable')
            if (arg1 == 2):
                v11 = load32(9142848)
                v12 = load32(38500)
                while True:  # $label5
                    while True:  # block $label4
                        arg0 = v3
                        arg2 = (v3 << 2)
                        arg1 = (v8 + load32((((v3 << 2) | 4) + 8611904)))
                        if (u(v4) <= u((v8 + load32((((v3 << 2) | 4) + 8611904))))):
                            break
                        arg2 = (v9 + load32((arg2 + 8611904)))
                        if (u(v4) <= u((v9 + load32((arg2 + 8611904))))):
                            break
                        if ((arg1 | arg2) < 0):
                            break
                        v3 = load32((((arg2 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4)
                        arg1 = (v5 + (load32((((arg2 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4) * 132))
                        if (v12 != load8u((v5 + (load32((((arg2 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4) * 132)) + 122)):
                            break
                        arg1 = load32(arg1 + 88)
                        if (load32(arg1 + 88) == 0):
                            break
                        if (u(((v11 - arg1) * 25)) > u(25000)):
                            break
                        break
                    v3 = (arg0 + 2)
                    if (u(arg0) <= u(717)):
                        continue
                    break
                break
            v11 = load32(38448)
            arg0 = 0
            if (arg1 == 1):
                while True:  # $label7
                    while True:  # block $label6
                        arg1 = arg0
                        arg2 = (arg0 << 2)
                        arg0 = (v8 + load32((((arg0 << 2) | 4) + 8611904)))
                        if (u(v4) <= u((v8 + load32((((arg0 << 2) | 4) + 8611904))))):
                            break
                        arg2 = (v9 + load32((arg2 + 8611904)))
                        if (u(v4) <= u((v9 + load32((arg2 + 8611904))))):
                            break
                        if ((arg0 | arg2) < 0):
                            break
                        v3 = load32((((arg2 + (((arg0 + v7) + 1) * v6)) << 2) + v10) + 4)
                        if (v11 == load8u((v5 + (load32((((arg2 + (((arg0 + v7) + 1) * v6)) << 2) + v10) + 4) * 132)) + 122)):
                            break
                        break
                    arg0 = (arg1 + 2)
                    if (u(arg1) <= u(717)):
                        continue
                    break
                    break
                raise RuntimeError('unreachable')
            v12 = load32(38504)
            v13 = load32(38508)
            while True:  # $label11
                while True:  # block $label8
                    arg2 = arg0
                    v3 = (arg0 << 2)
                    arg0 = (v8 + load32((((arg0 << 2) | 4) + 8611904)))
                    if (u(v4) <= u((v8 + load32((((arg0 << 2) | 4) + 8611904))))):
                        break
                    v3 = (v9 + load32((v3 + 8611904)))
                    if (u(v4) <= u((v9 + load32((v3 + 8611904))))):
                        break
                    if ((arg0 | v3) < 0):
                        break
                    v3 = load32((((v3 + (((arg0 + v7) + 1) * v6)) << 2) + v10) + 4)
                    while True:  # block $label10
                        while True:  # block $label9
                            # br_table[arg1]
                            break
                            break
                        arg0 = load8u((v5 + (v3 * 132)) + 122)
                        if (v13 == load8u((v5 + (v3 * 132)) + 122)):
                            break
                        if (arg0 != v12):
                            break
                        break
                        break
                    if (v11 == load8u((v5 + (v3 * 132)) + 122)):
                        break
                    break
                arg0 = (arg2 + 2)
                if (u(arg2) <= u(717)):
                    continue
                break
            break
        return 0
        break
    return load32((v5 + (v3 * 132)) + 28)

# ------------------------------------------------------------
# $func225
# ------------------------------------------------------------
def func225(arg0, arg1, arg2, arg3):
    v6 = load32(9142440)
    v12 = load16u(arg2 + 114)
    v13 = load16u(arg2 + 112)
    while True:  # $label9
        while True:  # block $label0
            v11 = v4
            v4 = (v4 << 2)
            v7 = (load32((((v4 << 2) | 4) + 8611904)) + v12)
            if (u(v6) <= u((load32((((v4 << 2) | 4) + 8611904)) + v12))):
                break
            v8 = (load32((v4 + 8611904)) + v13)
            if (u(v6) <= u((load32((v4 + 8611904)) + v13))):
                break
            if ((v7 | v8) < 0):
                break
            while True:  # block $label1
                v4 = (v6 + 2)
                v4 = load32((load32(9142840) + ((v8 + (((v7 + (v6 + 2)) + 1) * v4)) << 2)) + 4)
                if (load32((load32(9142840) + ((v8 + (((v7 + (v6 + 2)) + 1) * v4)) << 2)) + 4) == 0):
                    break
                v4 = (load32(9671128) + (v4 * 132))
                if (load8u((load32(9671128) + (v4 * 132)) + 129) == 10):
                    break
                if (load32(38528) != load8u(v4 + 122)):
                    break
                break
            v4 = func56(v8, v7, arg3, load16u(arg2 + 110), 0, 0, 1, 1, 0)
            v6 = load32(9142440)
            if (v4 == 0):
                break
            while True:  # block $label8
                while True:  # block $label5
                    while True:  # block $label4
                        while True:  # block $label2
                            while True:  # block $label3
                                v5 = ((load8u(arg2 + 122) * 404) + 9568096)
                                # br_table[load32(((load8u(arg2 + 122) * 404) + 9568096) + 264)]
                                break
                                break
                            v14 = load32(v5 + 216)
                            if (load32(v5 + 216) == 0):
                                v4 = load32(9142432)
                                break
                            v4 = load32(9142432)
                            v15 = load32(v5 + 220)
                            if (load32(v5 + 220) == 0):
                                break
                            v5 = load32(9215880)
                            if (load32(9215880) == 0):
                                break
                            if (v4 == 0):
                                break
                            v16 = load16u(arg2 + 114)
                            v17 = load16u(arg2 + 112)
                            v18 = load32(v5)
                            v5 = 0
                            while True:  # $label7
                                v19 = (v5 + v17)
                                v9 = 0
                                while True:  # $label6
                                    v10 = load32((v4 + ((v19 + ((v9 + v16) * v6)) << 2)))
                                    if (load32((v18 + (load32((v4 + ((v19 + ((v9 + v16) * v6)) << 2))) << 2))) == 0):
                                        break
                                    v9 = (v9 + 1)
                                    if ((v9 + 1) != v15):
                                        continue
                                    break
                                v5 = (v5 + 1)
                                if (v14 != (v5 + 1)):
                                    continue
                                break
                            break
                            break
                        v4 = load32(9142432)
                        if (load32(9142432) == 0):
                            break
                        v10 = load32((v4 + ((load16u(arg2 + 112) + (v6 * load16u(arg2 + 114))) << 2)))
                        break
                        break
                    v10 = 0
                    if (v4 == 0):
                        break
                    break
                if (v10 != load32((v4 + (((v6 * v7) + v8) << 2)))):
                    break
                break
            store32(arg0, v8)
            store32(arg1, v7)
            return 1
            break
        v4 = (v11 + 2)
        if (u(v11) < u(5198)):
            continue
        break
    return 0

# ------------------------------------------------------------
# $func226
# ------------------------------------------------------------
def func226(arg0, arg1):
    store32(arg0 + 8, 0)
    store64(arg0, 0)
    v2 = load32(arg1 + 4)
    v4 = load32(arg1)
    v5 = (load32(arg1 + 4) - load32(arg1))
    v3 = ((load32(arg1 + 4) - load32(arg1)) // 196)
    while True:  # block $label2
        while True:  # block $label0
            if (v2 != v4):
                if (u(v3) >= u(21913099)):
                    break
                v2 = func26(v5)
                store32(arg0 + 4, func26(v5))
                store32(arg0, v2)
                store32(arg0 + 8, (v2 + (v3 * 196)))
                v3 = load32(arg1)
                v4 = load32(arg1 + 4)
                if (load32(arg1) != load32(arg1 + 4)):
                    while True:  # $label1
                        # TODO: memory.copy []
                        v2 = (v2 + 196)
                        v3 = (v3 + 196)
                        if ((v3 + 196) != v4):
                            continue
                        break
                store32(arg0 + 4, v2)
            store64(arg0 + 12, 0)
            store32(arg0 + 20, 0)
            v2 = load32(arg1 + 16)
            v4 = load32(arg1 + 12)
            v5 = (load32(arg1 + 16) - load32(arg1 + 12))
            v3 = ((load32(arg1 + 16) - load32(arg1 + 12)) // 196)
            if (v2 != v4):
                if (u(v3) >= u(21913099)):
                    break
                v2 = func26(v5)
                store32(arg0 + 16, func26(v5))
                store32(arg0 + 12, v2)
                store32(arg0 + 20, (v2 + (v3 * 196)))
                v3 = load32(arg1 + 12)
                v4 = load32(arg1 + 16)
                if (load32(arg1 + 12) != load32(arg1 + 16)):
                    while True:  # $label3
                        # TODO: memory.copy []
                        v2 = (v2 + 196)
                        v3 = (v3 + 196)
                        if ((v3 + 196) != v4):
                            continue
                        break
                store32(arg0 + 16, v2)
            # TODO: memory.copy []
            return arg0
            break
        func42()
        raise RuntimeError('unreachable')
        break
    func42()
    raise RuntimeError('unreachable')
    return 104

# ------------------------------------------------------------
# $func227
# ------------------------------------------------------------
def func227():
    while True:  # block $label0
        if load8u(9142411):
            break
        if (load32(load32(9142424) + 48) == 0):
            break
        while True:  # block $label1
            v5 = load32(9142440)
            if (load32(9142440) <= 0):
                v1 = v5
                break
            v2 = load32(9142840)
            v1 = v5
            while True:  # $label6
                v6 = (v7 + 1)
                v3 = 0
                while True:  # $label5
                    v0 = (load32(9147376) + (((v1 * v3) + v7) << 1))
                    store16((load32(9147376) + (((v1 * v3) + v7) << 1)), (load16u(v0) + 2))
                    while True:  # block $label2
                        v4 = (v1 + 2)
                        v3 = (v3 + 1)
                        v0 = load32((v2 + ((((v1 + 2) * (v3 + 1)) + v6) << 2)))
                        if (u(load32((v2 + ((((v1 + 2) * (v3 + 1)) + v6) << 2)))) < u(3)):
                            break
                        v0 = (load32(9671128) + (v0 * 132))
                        if load32((load32(9671128) + (v0 * 132)) + 40):
                            break
                        v1 = load32(9142440)
                        v4 = (load32(9142440) + 2)
                        v2 = load32(9142840)
                        break
                    while True:  # block $label3
                        v0 = load32((v2 + ((((v3 + v4) * v4) + v6) << 2)))
                        if (u(load32((v2 + ((((v3 + v4) * v4) + v6) << 2)))) < u(3)):
                            break
                        v0 = (load32(9671128) + (v0 * 132))
                        if load32((load32(9671128) + (v0 * 132)) + 40):
                            break
                        v1 = load32(9142440)
                        v4 = (load32(9142440) + 2)
                        v2 = load32(9142840)
                        break
                    while True:  # block $label4
                        v0 = load32((v2 + (((((v4 << 1) + v3) * v4) + v6) << 2)))
                        if (u(load32((v2 + (((((v4 << 1) + v3) * v4) + v6) << 2)))) < u(3)):
                            break
                        v0 = (load32(9671128) + (v0 * 132))
                        if load32((load32(9671128) + (v0 * 132)) + 40):
                            break
                        v2 = load32(9142840)
                        v1 = load32(9142440)
                        break
                    if (v3 != v5):
                        continue
                    break
                v7 = v6
                if (v6 != v5):
                    continue
                break
            break
        store8(9142904, 1)
        store8(9142411, 1)
        store32(40612, (v1 - 1))
        store32(40608, 0)
        a_b()
        break

# ------------------------------------------------------------
# $func228
# ------------------------------------------------------------
def func228(arg0, arg1, arg2):
    v9 = (i64(arg1) * 132)
    v5 = i32((i64(arg1) * 132))
    v3 = (i32((i64(arg1) * 132)) + 4)
    v3 = func26((-1 if i32(((v9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else (-1 if (u(v3) < u(v5)) else (i32((i64(arg1) * 132)) + 4))))
    store32(func26((-1 if i32(((v9 & 0xFFFFFFFFFFFFFFFF) >> 32)) else (-1 if (u(v3) < u(v5)) else (i32((i64(arg1) * 132)) + 4)))), arg1)
    v5 = (v3 + 4)
    if arg1:
        v7 = (v5 + (arg1 * 132))
        arg1 = v5
        while True:  # $label0
            # TODO: memory.fill []
            v4 = func26(4)
            store32(arg1 + 4, func26(4))
            store32(arg1, v4)
            store32(arg1 + 8, (v4 + 4))
            arg1 = (arg1 + 132)
            if ((arg1 + 132) != v7):
                continue
            break
    while True:  # block $label5
        while True:  # block $label2
            if arg2:
                if (arg0 != v5):
                    arg1 = 0
                    while True:  # $label1
                        v3 = (arg1 * 132)
                        v4 = (v5 + (arg1 * 132))
                        v3 = (arg0 + v3)
                        # TODO: memory.copy []
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != arg2):
                            continue
                        break
                    break
                v4 = (arg2 & 3)
                v3 = (v3 + 16)
                v7 = 0
                arg1 = 0
                if (u(arg2) >= u(4)):
                    v8 = (arg2 & -4)
                    arg2 = 0
                    while True:  # $label3
                        v6 = (arg1 * 132)
                        # TODO: memory.copy []
                        v6 = ((arg1 | 1) * 132)
                        # TODO: memory.copy []
                        v6 = ((arg1 | 2) * 132)
                        # TODO: memory.copy []
                        v6 = ((arg1 | 3) * 132)
                        # TODO: memory.copy []
                        arg1 = (arg1 + 4)
                        arg2 = (arg2 + 4)
                        if ((arg2 + 4) != v8):
                            continue
                        break
                if (v4 == 0):
                    break
                while True:  # $label4
                    arg2 = (arg1 * 132)
                    # TODO: memory.copy []
                    arg1 = (arg1 + 1)
                    v7 = (v7 + 1)
                    if ((v7 + 1) != v4):
                        continue
                    break
                break
            if (arg0 == 0):
                break
            break
        v4 = (arg0 - 4)
        arg1 = load32((arg0 - 4))
        if load32((arg0 - 4)):
            arg1 = (arg0 + (arg1 * 132))
            while True:  # $label6
                arg2 = (arg1 - 132)
                v3 = load32((arg1 - 132))
                if load32((arg1 - 132)):
                    store32((arg1 - 128), v3)
                arg1 = arg2
                if (arg2 != arg0):
                    continue
                break
        break
    return v5

# ------------------------------------------------------------
# $hd
# Export: hd
# ------------------------------------------------------------
def hd():
    """Exported as hd."""
    v2 = 3
    if (u(load32(9671136)) > u(3)):
        while True:  # $label1
            while True:  # block $label0
                v0 = (load32(9671128) + (v2 * 132))
                if (load32((load32(9671128) + (v2 * 132)) + 28) == 0):
                    break
                if (load32(v0 + 40) == 0):
                    break
                if (load32(v0 + 64) == 0):
                    if (load32(38448) != load8u(v0 + 122)):
                        break
                    break
                v3 = load32(v0 + 48)
                v1 = load32(load32(v0 + 48) + 20)
                v4 = load8u(v0 + 124)
                if (load32(load32(v0 + 48) + 20) <= load8u(v0 + 124)):
                    v1 = (v4 % v1)
                    store8(v0 + 124, ((3 if (u(v1) < u(3)) else (v4 % v1)) if (load32(38448) == load8u(v0 + 122)) else v1))
                v0 = load8u(v0 + 125)
                break
            v2 = (v2 + 1)
            if (u((v2 + 1)) < u(load32(9671136))):
                continue
            break
    func320(1)

# ------------------------------------------------------------
# $func230
# ------------------------------------------------------------
def func230(arg0):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v6 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
    v1 = load32(arg0 + 20)
    while True:  # block $label10
        while True:  # block $label0
            while True:  # block $label9
                while True:  # $label8
                    v2 = load32(load32(v1))
                    if (u(load32(load32(v1))) < u(2147483647)):
                        break
                    v2 = ((v2 - 2147483647) if (u(v2) > u(2147483646)) else v2)
                    v1 = load32(((v6 + (((v2 - 2147483647) if (u(v2) > u(2147483646)) else v2) * 36)) + 269376))
                    v3 = (load32(((v6 + (((v2 - 2147483647) if (u(v2) > u(2147483646)) else v2) * 36)) + 269376)) if v1 else 100)
                    v1 = ((v2 * 404) + 9568096)
                    store32(v4, (((load32(((v6 + (((v2 - 2147483647) if (u(v2) > u(2147483646)) else v2) * 36)) + 269376)) if v1 else 100) * load32(((v2 * 404) + 9568096) + 68)) // 100))
                    store32(v4 + 4, ((load32(v1 + 72) * v3) // 100))
                    store32(v4 + 8, ((load32(v1 + 76) * v3) // 100))
                    store32(v4 + 12, ((load32(v1 + 80) * v3) // 100))
                    while True:  # block $label6
                        while True:  # block $label2
                            while True:  # block $label1
                                v7 = load32(v1 + 180)
                                if (load8u(load32(v1 + 180) + 23) == 0):
                                    break
                                v1 = load32(v7 + 4)
                                if (load32(((load32(v7 + 4) * 404) + 9568096) + 264) != 3):
                                    break
                                if load32(((v6 + (v1 << 2)) + 281808)):
                                    break
                                break
                            v12 = load32(v7 + 68)
                            if load32(v7 + 68):
                                v3 = 0
                                v5 = 1
                                v1 = 0
                                v8 = 0
                                while True:  # $label5
                                    v9 = load32((v7 + (v3 << 2)) + 28)
                                    v10 = load32(((load32((v7 + (v3 << 2)) + 28) * 404) + 9568096) + 264)
                                    v11 = (load32(((load32((v7 + (v3 << 2)) + 28) * 404) + 9568096) + 264) == 1)
                                    while True:  # block $label4
                                        while True:  # block $label3
                                            v9 = load32(((v6 + (v9 << 2)) + 281808))
                                            if (load32(((v6 + (v9 << 2)) + 281808)) == 1):
                                                break
                                            v5 = ((v10 != 3) & v5)
                                            if v9:
                                                break
                                            v5 = ((v10 != 0) & v5)
                                            break
                                            break
                                        v8 = (v8 | v11)
                                        break
                                    v1 = (v1 | v11)
                                    v3 = (v3 + 1)
                                    if ((v3 + 1) != v12):
                                        continue
                                    break
                                if ((((v5 & v8) if (v1 & 1) else v5) & 1) == 0):
                                    break
                            if (func66(v6, v4, 0, 1) == 0):
                                break
                            break
                        func181(v6, load32(arg0 + 28), v2)
                        v1 = load32(arg0 + 20)
                        v2 = (load32(v1 + 8) - 1)
                        store32(load32(arg0 + 20) + 8, (load32(v1 + 8) - 1))
                        if v2:
                            v2 = load32(v1)
                            v3 = 0
                            while True:  # $label7
                                v3 = (v3 + 1)
                                store32((v2 + (v3 << 2)), load32((v2 + ((v3 + 1) << 2))))
                                if (u(v3) < u(load32(v1 + 8))):
                                    continue
                                break
                        if load32(v1 + 8):
                            continue
                        break
                        break
                    break
                if (v2 != -1):
                    break
                break
            v1 = load32(arg0 + 44)
            if load32(arg0 + 44):
                store32((load32(9215884) + (v1 << 4)), 0)
            store32(arg0 + 44, 0)
            func29(arg0, 1)
            if (load32(arg0 + 92) == 0):
                break
            v1 = load8u(9147141)
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
            break
        v1 = ((v2 * 404) + 9568096)
        v1 = ((load32(((v2 * 404) + 9568096) + 116) * load32((load32(9142424) + (132 if load32(v1 + 264) else 128)))) * 1000)
        v2 = (u(((load32(((v2 * 404) + 9568096) + 116) * load32((load32(9142424) + (132 if load32(v1 + 264) else 128)))) * 1000)) < u(100))
        # TODO: i32.div_u []
        v1 = 100
        while True:  # block $label11
            if (load32(9142872) != load16u(arg0 + 110)):
                break
            v3 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 180)
            if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 180) == 0):
                break
            break
        v1 = (25 if v2 else v1)
        v2 = load32(arg0 + 44)
        if load32(arg0 + 44):
            # TODO: i32.div_u []
            store32(load32(9142848), (v1 + 25))
            break
        func63((load32(9215884) + (v2 << 4)), arg0, 2, 0, v1)
        break
    G.global0 = (v4 + 16)

# ------------------------------------------------------------
# $func231
# ------------------------------------------------------------
def func231(arg0):
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v2 = (v1 + 4)
    # TODO: memory.fill []
    # TODO: memory.copy []
    func436(9688272)
    store32(arg0, load32(52428))
    store32(arg0 + 4, load32(52432))
    func266(9688272)
    G.global0 = (v1 + 48)

# ------------------------------------------------------------
# $func232
# ------------------------------------------------------------
def func232(arg0):
    while True:  # block $label0
        if (arg0 == 0):
            break
        v8 = load32(9142836)
        v2 = (load32(9142836) + (arg0 * 80))
        if load32((load32(9142836) + (arg0 * 80))):
            break
        v2 = (arg0 + 1)
        v6 = ((arg0 + 1) * v2)
        v9 = func26((-1 if (v6 & 402653184) else (((arg0 + 1) * v2) << 5)))
        store32(v2, func26((-1 if (v6 & 402653184) else (((arg0 + 1) * v2) << 5))))
        v10 = (arg0 << 1)
        v2 = (0 - arg0)
        if ((arg0 << 1) > (0 - arg0)):
            v4 = (v8 + (arg0 * 80))
            v12 = (arg0 * arg0)
            v3 = v2
            while True:  # $label2
                v13 = ((v3 * v3) - 1)
                v1 = v2
                while True:  # $label1
                    if (v12 >= (v13 + (v1 * v1))):
                        v7 = load32(v4 + 4)
                        store32(v4 + 4, (load32(v4 + 4) + 1))
                        store32((v9 + (v7 << 2)), v3)
                        v7 = load32(v4 + 4)
                        store32(v4 + 4, (load32(v4 + 4) + 1))
                        store32((v9 + (v7 << 2)), v1)
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v10):
                        continue
                    break
                v3 = (v3 + 1)
                if ((v3 + 1) != v10):
                    continue
                break
        v6 = (-1 if (v6 & 805306368) else (v6 << 4))
        v14 = (arg0 * arg0)
        v8 = (v8 + (arg0 * 80))
        while True:  # $label7
            v2 = (v15 << 2)
            v11 = (v8 + (v15 << 2))
            v16 = func26(v6)
            store32((v8 + (v15 << 2)) + 8, func26(v6))
            while True:  # block $label3
                v17 = load32((v2 + 9264))
                v5 = (load32((v2 + 9264)) - arg0)
                v9 = (v10 + v17)
                if ((load32((v2 + 9264)) - arg0) >= (v10 + v17)):
                    break
                v4 = load32((v2 + 9344))
                v2 = (load32((v2 + 9344)) - arg0)
                v12 = (v4 + v10)
                if ((load32((v2 + 9344)) - arg0) >= (v4 + v10)):
                    break
                while True:  # $label6
                    v13 = ((v5 * v5) - 1)
                    v1 = (v5 - v17)
                    v7 = (((v5 - v17) * v1) - 1)
                    v1 = v2
                    while True:  # $label5
                        while True:  # block $label4
                            v3 = (v1 - v4)
                            if ((v7 + ((v1 - v4) * v3)) > v14):
                                break
                            if ((v13 + (v1 * v1)) <= v14):
                                break
                            v3 = load32(v11 + 44)
                            store32(v11 + 44, (load32(v11 + 44) + 1))
                            store32((v16 + (v3 << 2)), v5)
                            v3 = load32(v11 + 44)
                            store32(v11 + 44, (load32(v11 + 44) + 1))
                            store32((v16 + (v3 << 2)), v1)
                            break
                        v1 = (v1 + 1)
                        if ((v1 + 1) != v12):
                            continue
                        break
                    v5 = (v5 + 1)
                    if ((v5 + 1) != v9):
                        continue
                    break
                break
            v15 = (v15 + 1)
            if ((v15 + 1) != 9):
                continue
            break
        break

# ------------------------------------------------------------
# $func233
# ------------------------------------------------------------
def func233(arg0, arg1):
    v2 = load32(9671128)
    v5 = (load32(9671128) + (arg0 * 132))
    if (load8u((load32(9671128) + (arg0 * 132)) + 125) != 3):
        return 0
    v4 = load16u(v5 + 116)
    if (load16u(v5 + 116) == 0):
        return 0
    while True:  # block $label0
        arg0 = (load16u((v2 + (arg0 * 132)) + 110) << 2)
        if (load32(((load16u((v2 + (arg0 * 132)) + 110) << 2) + load32(arg1 + 48))) == 0):
            if (load32((load32(9142420) + arg0)) == 0):
                break
        v6 = load16u((v2 + (v4 * 132)) + 110)
        if (load32((load32(arg1 + 64) + (load16u((v2 + (v4 * 132)) + 110) << 2))) == 0):
            if (load32((load32(9142420) + (v6 << 2))) == 0):
                break
        while True:  # block $label11
            while True:  # block $label10
                while True:  # block $label5
                    while True:  # block $label4
                        while True:  # block $label1
                            while True:  # block $label3
                                while True:  # block $label2
                                    # br_table[load32(arg1 + 8)]
                                    break
                                    break
                                v7 = load32(arg1 + 104)
                                if (load32(arg1 + 104) == 0):
                                    break
                                v2 = load32((v2 + (v4 * 132)) + 28)
                                arg1 = load32(arg1 + 96)
                                arg0 = 0
                                break
                                break
                            arg1 = load32(9140300)
                            if (load32(9140300) == 0):
                                break
                            v2 = load32((v2 + (v4 * 132)) + 28)
                            arg0 = 0
                            break
                            break
                        arg1 = load32(arg1 + 36)
                        if (u(load32(arg1 + 36)) <= u(3)):
                            v2 = (v2 + (v4 * 132))
                            arg0 = load8u((v2 + (v4 * 132)) + 122)
                            while True:  # block $label9
                                while True:  # block $label7
                                    while True:  # block $label8
                                        while True:  # block $label6
                                            # br_table[(arg1 - 1)]
                                            break
                                            break
                                        arg1 = ((arg0 * 404) + 9568096)
                                        if load32(((arg0 * 404) + 9568096) + 264):
                                            return 0
                                        if (load32(arg1 + 268) == 1):
                                            break
                                        if (load32(((arg0 * 404) + 9568096) + 92) == 0):
                                            break
                                        if (load32(38456) == arg0):
                                            break
                                        if (load32(38764) != arg0):
                                            break
                                        break
                                        break
                                    if (load32(((arg0 * 404) + 9568096) + 264) == 1):
                                        break
                                    break
                                    break
                                if load32(((arg0 * 404) + 9568096) + 264):
                                    break
                                break
                            arg0 = 0
                            v2 = load32(v2 + 28)
                            arg1 = load32(9140300)
                            if (u(load32(9684388)) >= u(2)):
                                if (arg1 == 0):
                                    arg1 = 0
                                    break
                                while True:  # $label12
                                    if (load32(((arg0 << 2) + 8451904)) == v2):
                                        break
                                    arg0 = (arg0 + 1)
                                    if ((arg0 + 1) != arg1):
                                        continue
                                    break
                            if (u(arg1) < u(40000)):
                                break
                            break
                        v2 = (v2 + (v4 * 132))
                        if (load8u((v2 + (v4 * 132)) + 122) != (arg1 - 4)):
                            break
                        arg0 = 0
                        v2 = load32(v2 + 28)
                        arg1 = load32(9140300)
                        if (u(load32(9684388)) >= u(2)):
                            if (arg1 == 0):
                                arg1 = 0
                                break
                            while True:  # $label13
                                if (load32(((arg0 << 2) + 8451904)) == v2):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != arg1):
                                    continue
                                break
                        if (u(arg1) < u(40000)):
                            break
                        break
                        break
                    while True:  # $label14
                        if (load32((arg1 + (arg0 << 2))) != v2):
                            arg0 = (arg0 + 1)
                            if (v7 != (arg0 + 1)):
                                continue
                            break
                        break
                    arg0 = 0
                    arg1 = load32(9140300)
                    if (u(load32(9684388)) >= u(2)):
                        if (arg1 == 0):
                            arg1 = 0
                            break
                        while True:  # $label15
                            if (load32(((arg0 << 2) + 8451904)) == v2):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != arg1):
                                continue
                            break
                    if (u(arg1) < u(40000)):
                        break
                    break
                    break
                while True:  # $label16
                    if (load32(((arg0 << 2) + 8451904)) != v2):
                        arg0 = (arg0 + 1)
                        if (arg1 != (arg0 + 1)):
                            continue
                        break
                    break
                arg0 = 0
                if (u(load32(9684388)) > u(1)):
                    while True:  # $label17
                        if (load32(((arg0 << 2) + 8451904)) == v2):
                            break
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != arg1):
                            continue
                        break
                if (u(arg1) > u(39999)):
                    break
                break
            store32(9140300, (arg1 + 1))
            store32(((arg1 << 2) + 8451904), v2)
            break
        store16(v5 + 116, 0)
        store32((load32(9142420) + (v6 << 2)), 2)
        v3 = 1
        break
    return v3

# ------------------------------------------------------------
# $func234
# ------------------------------------------------------------
def func234(arg0, arg1):
    v7 = (arg0 - 16)
    if load32((arg0 - 16)):
        while True:  # $label28
            v2 = (arg0 + (v5 * 60))
            store32(9681920, (load32(9681920) + ((load32((arg0 + (v5 * 60))) * load32(v2 + 4)) << 2)))
            v3 = load32(v2 + 28)
            while True:  # block $label1
                while True:  # block $label3
                    while True:  # block $label2
                        while True:  # block $label0
                            v6 = load32(v2 + 32)
                            # br_table[(load32(v2 + 32) - 23)]
                            break
                            break
                        v4 = load32(9140324)
                        store32(9140324, (load32(9140324) + 1))
                        break
                        break
                    v4 = load32(9140328)
                    store32(9140328, (load32(9140328) + 1))
                    break
                store32(((v4 << 2) + 9140336), v2)
                break
            while True:  # block $label27
                if (u(v3) <= u(9999)):
                    while True:  # block $label26
                        while True:  # block $label25
                            while True:  # block $label24
                                while True:  # block $label23
                                    while True:  # block $label22
                                        while True:  # block $label21
                                            while True:  # block $label20
                                                while True:  # block $label19
                                                    while True:  # block $label18
                                                        while True:  # block $label17
                                                            while True:  # block $label16
                                                                while True:  # block $label15
                                                                    while True:  # block $label14
                                                                        while True:  # block $label13
                                                                            while True:  # block $label12
                                                                                while True:  # block $label11
                                                                                    while True:  # block $label10
                                                                                        while True:  # block $label9
                                                                                            while True:  # block $label8
                                                                                                while True:  # block $label7
                                                                                                    while True:  # block $label6
                                                                                                        while True:  # block $label5
                                                                                                            while True:  # block $label4
                                                                                                                # br_table[v6]
                                                                                                                break
                                                                                                                break
                                                                                                            store32(((v3 * 72) + 9263856) + 4, v2)
                                                                                                            break
                                                                                                            break
                                                                                                        store32(((v3 * 72) + 9263856) + 8, v2)
                                                                                                        break
                                                                                                        break
                                                                                                    store32(((v3 * 72) + 9263856) + 28, v2)
                                                                                                    break
                                                                                                    break
                                                                                                store32(((v3 * 72) + 9263856), v2)
                                                                                                break
                                                                                                break
                                                                                            store32(((v3 * 72) + 9263856) + 4, v2)
                                                                                            break
                                                                                            break
                                                                                        v4 = ((v3 * 404) + 9568096)
                                                                                        v6 = load32(v4 + 20)
                                                                                        store32(((v3 * 404) + 9568096) + 20, (load32(v4 + 20) + 1))
                                                                                        store32((v4 + (v6 << 2)), v2)
                                                                                        break
                                                                                        break
                                                                                    v4 = ((v3 * 404) + 9568096)
                                                                                    v6 = load32(v4 + 20)
                                                                                    store32(((v3 * 404) + 9568096) + 20, (load32(v4 + 20) + 1))
                                                                                    store32((v4 + (v6 << 2)), v2)
                                                                                    break
                                                                                    break
                                                                                store32(((v3 * 72) + 9263856) + 40, v2)
                                                                                break
                                                                                break
                                                                            store32(((v3 * 72) + 9263856) + 44, v2)
                                                                            break
                                                                            break
                                                                        store32(((v3 * 72) + 9263856) + 32, v2)
                                                                        break
                                                                        break
                                                                    store32(((v3 * 72) + 9263856) + 36, v2)
                                                                    break
                                                                    break
                                                                store32(((v3 * 72) + 9263856) + 52, v2)
                                                                break
                                                                break
                                                            store32(((v3 * 72) + 9263856) + 20, v2)
                                                            break
                                                            break
                                                        store32(((v3 * 72) + 9263856) + 60, v2)
                                                        break
                                                        break
                                                    store32(((v3 * 72) + 9263856) + 48, v2)
                                                    break
                                                    break
                                                store32(((v3 * 72) + 9263856) + 68, v2)
                                                break
                                                break
                                            store32(((v3 * 72) + 9263856) + 12, v2)
                                            break
                                            break
                                        store32(((v3 * 72) + 9263856) + 56, v2)
                                        break
                                        break
                                    store32(((v3 * 72) + 9263856) + 64, v2)
                                    break
                                    break
                                store32(((v3 * 72) + 9263856) + 68, v2)
                                break
                                break
                            store32(((v3 * 72) + 9263856) + 16, v2)
                            break
                            break
                        store32(((v3 * 72) + 9263856) + 24, v2)
                        break
                        break
                    v4 = ((v3 * 404) + 9568096)
                    v6 = load32(v4 + 20)
                    store32(((v3 * 404) + 9568096) + 20, (load32(v4 + 20) + 1))
                    store32((v4 + (v6 << 2)), v2)
                    break
                if (u(v3) > u(19999)):
                    break
                v3 = (v3 - 10000)
                if (u((v3 - 10000)) > u(95)):
                    break
                store32(((v3 << 2) + 9142448), v2)
                break
            store32(v2 + 28, 2147483647)
            v5 = (v5 + 1)
            if (u((v5 + 1)) < u(load32(v7))):
                continue
            break
    while True:  # block $label31
        if arg1:
            arg0 = 0
            while True:  # $label30
                arg1 = ((arg0 * 72) + 9263856)
                if (load32(((arg0 * 72) + 9263856)) == 0):
                    store32(arg1, load32(arg1 + 4))
                while True:  # block $label29
                    v4 = load32(arg1 + 8)
                    if (load32(arg1 + 8) == 0):
                        if load32(((arg0 * 404) + 9568096) + 264):
                            break
                        v4 = load32(arg1 + 12)
                        store32(arg1 + 8, load32(arg1 + 12))
                        if (v4 == 0):
                            break
                    arg1 = load32(((arg0 * 404) + 9568096) + 276)
                    if (load32(((arg0 * 404) + 9568096) + 276) == 0):
                        break
                    if (load32(v4 + 24) > 99):
                        break
                    # TODO: i32.div_u []
                    store32((load32(v4 + 16) * 1000) + 24, arg1)
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != 255):
                    continue
                break
            break
        v2 = ((v3 * 404) + 9568096)
        arg1 = ((v3 * 72) + 9263856)
        arg0 = 0
        while True:  # $label33
            while True:  # block $label32
                if (arg0 != v3):
                    break
                if (load32(arg1) == 0):
                    store32(arg1, load32(arg1 + 4))
                v5 = load32(arg1 + 8)
                if (load32(arg1 + 8) == 0):
                    if load32(v2 + 264):
                        break
                    v5 = load32(arg1 + 12)
                    store32(arg1 + 8, load32(arg1 + 12))
                    if (v5 == 0):
                        break
                v4 = load32(v2 + 276)
                if (load32(v2 + 276) == 0):
                    break
                if (load32(v5 + 24) > 99):
                    break
                # TODO: i32.div_u []
                store32((load32(v5 + 16) * 1000) + 24, v4)
                break
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != 255):
                continue
            break
        break
    return v3

# ------------------------------------------------------------
# $func235
# ------------------------------------------------------------
def func235(arg0, arg1, arg2, arg3, arg4):
    v17 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v12 = load16u(arg3 + 112)
    while True:  # block $label0
        v25 = load8u(arg3 + 122)
        if (load8u(arg3 + 122) == 20):
            arg2 = 0
            arg3 = load16u(arg3 + 114)
            arg4 = (load32(9142440) + 2)
            if load32((load32(9142840) + ((v12 + (((load16u(arg3 + 114) + (load32(9142440) + 2)) + 2) * arg4)) << 2)) + 8):
                break
            arg2 = 1
            store32(arg0, (v12 + 1))
            store32(arg1, (arg3 + 1))
            break
        v26 = load8u(arg2 + 122)
        v6 = ((load8u(arg2 + 122) * 404) + 9568096)
        v20 = load32(((load8u(arg2 + 122) * 404) + 9568096) + 212)
        v21 = load32(v6 + 208)
        v23 = load16u(arg2 + 114)
        v27 = load16u(arg2 + 112)
        v24 = (v12 - 1)
        v14 = load16u(arg3 + 114)
        v22 = (load16u(arg3 + 114) - 1)
        if (load32(((v25 * 404) + 9568096) + 264) == 2):
            arg2 = 1
            v8 = load32(9142840)
            v6 = (v12 + 1)
            arg4 = (v14 + 1)
            v5 = load32(9142440)
            arg3 = (load32(9142440) + 2)
            if (load32((load32(9142840) + (((v12 + 1) + (((v14 + 1) + (load32(9142440) + 2)) * arg3)) << 2))) == 0):
                store32(arg0, v12)
                store32(arg1, v14)
                break
            arg2 = (v24 - v27)
            v7 = ((v24 - v27) * arg2)
            arg2 = 2147483647
            while True:  # block $label1
                if (u(v5) <= u(v22)):
                    break
                if ((v22 | v24) < 0):
                    break
                if (u(v5) <= u(v24)):
                    break
                if (load32((v8 + (((((arg3 * v21) + v14) * arg3) + v12) << 2))) != v20):
                    break
                arg3 = (v22 - v23)
                arg3 = (((v22 - v23) * arg3) + v7)
                if ((((v22 - v23) * arg3) + v7) == 2147483647):
                    break
                store32(arg0, v24)
                store32(arg1, v22)
                v5 = load32(9142440)
                arg2 = arg3
                break
            while True:  # block $label2
                if (u(v5) <= u(v14)):
                    break
                if (v12 == 0):
                    break
                if (u(v5) <= u(v24)):
                    break
                arg3 = (v5 + 2)
                if (load32((v8 + ((((arg4 + ((v5 + 2) * v21)) * arg3) + v12) << 2))) != v20):
                    break
                arg3 = (v14 - v23)
                arg3 = (((v14 - v23) * arg3) + v7)
                if ((((v14 - v23) * arg3) + v7) >= arg2):
                    break
                store32(arg0, v24)
                store32(arg1, v14)
                v5 = load32(9142440)
                arg2 = arg3
                break
            while True:  # block $label3
                if (u(arg4) >= u(v5)):
                    break
                if ((arg4 | v24) < 0):
                    break
                if (u(v5) <= u(v24)):
                    break
                arg3 = (v5 + 2)
                if (load32((v8 + (((((v14 + ((v5 + 2) * v21)) + 2) * arg3) + v12) << 2))) != v20):
                    break
                arg3 = (arg4 - v23)
                arg3 = (((arg4 - v23) * arg3) + v7)
                if ((((arg4 - v23) * arg3) + v7) >= arg2):
                    break
                store32(arg0, v24)
                store32(arg1, arg4)
                v5 = load32(9142440)
                arg2 = arg3
                break
            arg3 = (v12 - v27)
            v7 = ((v12 - v27) * arg3)
            while True:  # block $label4
                if (u(v5) <= u(v22)):
                    break
                if (v14 == 0):
                    break
                if (u(v5) <= u(v12)):
                    break
                arg3 = (v5 + 2)
                if (load32((v8 + ((v6 + ((((v5 + 2) * v21) + v14) * arg3)) << 2))) != v20):
                    break
                arg3 = (v22 - v23)
                arg3 = (((v22 - v23) * arg3) + v7)
                if ((((v22 - v23) * arg3) + v7) >= arg2):
                    break
                store32(arg0, v12)
                store32(arg1, v22)
                v5 = load32(9142440)
                arg2 = arg3
                break
            while True:  # block $label5
                if (u(v5) <= u(v14)):
                    break
                if (u(v5) <= u(v12)):
                    break
                arg3 = (v5 + 2)
                if (load32((v8 + ((v6 + ((arg4 + ((v5 + 2) * v21)) * arg3)) << 2))) != v20):
                    break
                arg3 = (v14 - v23)
                arg3 = (((v14 - v23) * arg3) + v7)
                if ((((v14 - v23) * arg3) + v7) >= arg2):
                    break
                store32(arg0, v12)
                store32(arg1, v14)
                v5 = load32(9142440)
                arg2 = arg3
                break
            while True:  # block $label6
                if (u(arg4) >= u(v5)):
                    break
                if (u(v5) <= u(v12)):
                    break
                arg3 = (v5 + 2)
                if (load32((v8 + ((v6 + (((v14 + ((v5 + 2) * v21)) + 2) * arg3)) << 2))) != v20):
                    break
                arg3 = (arg4 - v23)
                arg3 = (((arg4 - v23) * arg3) + v7)
                if ((((arg4 - v23) * arg3) + v7) >= arg2):
                    break
                store32(arg0, v12)
                store32(arg1, arg4)
                v5 = load32(9142440)
                arg2 = arg3
                break
            v12 = (v12 + 2)
            arg3 = (v6 - v27)
            v7 = ((v6 - v27) * arg3)
            while True:  # block $label7
                if (u(v5) <= u(v22)):
                    break
                if ((v6 | v22) < 0):
                    break
                if (u(v5) <= u(v6)):
                    break
                arg3 = (v5 + 2)
                if (load32((v8 + ((v12 + ((((v5 + 2) * v21) + v14) * arg3)) << 2))) != v20):
                    break
                arg3 = (v22 - v23)
                arg3 = (((v22 - v23) * arg3) + v7)
                if ((((v22 - v23) * arg3) + v7) >= arg2):
                    break
                store32(arg0, v6)
                store32(arg1, v22)
                v5 = load32(9142440)
                arg2 = arg3
                break
            while True:  # block $label8
                if (u(v5) <= u(v14)):
                    break
                if (u(v5) <= u(v6)):
                    break
                arg3 = (v5 + 2)
                if (load32((v8 + ((v12 + ((arg4 + ((v5 + 2) * v21)) * arg3)) << 2))) != v20):
                    break
                arg3 = (v14 - v23)
                arg3 = (((v14 - v23) * arg3) + v7)
                if ((((v14 - v23) * arg3) + v7) >= arg2):
                    break
                store32(arg0, v6)
                store32(arg1, v14)
                v5 = load32(9142440)
                arg2 = arg3
                break
            while True:  # block $label9
                if (u(arg4) >= u(v5)):
                    break
                if (u(v5) <= u(v6)):
                    break
                arg3 = (v5 + 2)
                if (load32((v8 + ((v12 + (((v14 + ((v5 + 2) * v21)) + 2) * arg3)) << 2))) != v20):
                    break
                arg3 = (arg4 - v23)
                arg3 = (((arg4 - v23) * arg3) + v7)
                if ((((arg4 - v23) * arg3) + v7) >= arg2):
                    break
                store32(arg0, v6)
                store32(arg1, arg4)
                arg2 = arg3
                break
            arg2 = (arg2 != 2147483647)
            break
        while True:  # block $label10
            if (v25 != load32(38508)):
                if (load32(38504) != v25):
                    break
            while True:  # block $label11
                # br_table[(load8u(arg2 + 129) - 1)]
                break
                break
            v29 = ((v26 * 404) + 9568312)
            v5 = load32(9142440)
            v6 = 0
            while True:  # $label29
                while True:  # block $label12
                    v8 = v6
                    v6 = (v6 << 2)
                    v9 = (load32((((v6 << 2) | 4) + 9488)) + load16u(arg3 + 114))
                    v10 = ((load32((((v6 << 2) | 4) + 9488)) + load16u(arg3 + 114)) - 1)
                    if (u(v5) <= u(((load32((((v6 << 2) | 4) + 9488)) + load16u(arg3 + 114)) - 1))):
                        break
                    v7 = (load32((v6 + 9488)) + load16u(arg3 + 112))
                    v13 = ((load32((v6 + 9488)) + load16u(arg3 + 112)) - 1)
                    if (u(v5) <= u(((load32((v6 + 9488)) + load16u(arg3 + 112)) - 1))):
                        break
                    if ((v10 | v13) < 0):
                        break
                    v15 = load32(9142840)
                    v6 = (v5 + 2)
                    if load32((load32(9142840) + (((((v5 + 2) + v9) * v6) + v7) << 2))):
                        break
                    if arg4:
                        store32(v17 + 4, 0)
                        store8(v17 + 3, 0)
                        v6 = func177(load16u(arg2 + 112), load16u(arg2 + 114), v13, v10, v20, v21, (v17 + 12), (v17 + 8), load32(v29), (v17 + 4), (v17 + 3), 0)
                        v5 = load32(9142440)
                        if (v6 == 0):
                            break
                        v15 = load32(9142840)
                    v6 = (v5 + 2)
                    v18 = load16u(arg2 + 110)
                    v19 = load32(9671128)
                    while True:  # block $label15
                        while True:  # block $label13
                            v30 = (u(v5) <= u(v10))
                            if (u(v5) <= u(v10)):
                                break
                            if (u(v5) <= u(v7)):
                                break
                            if ((v7 | v10) < 0):
                                break
                            v11 = (v19 + (load32((((v7 + ((v6 + v9) * v6)) << 2) + v15) + 4) * 132))
                            if (load16u((v19 + (load32((((v7 + ((v6 + v9) * v6)) << 2) + v15) + 4) * 132)) + 110) != v18):
                                break
                            while True:  # block $label14
                                # br_table[load32(((load8u(v11 + 122) * 404) + 9568096) + 192)]
                                break
                                break
                            if (load8u(v11 + 125) == 0):
                                break
                            break
                        while True:  # block $label16
                            v16 = (v9 - 2)
                            v28 = (u(v5) <= u((v9 - 2)))
                            if (u(v5) <= u((v9 - 2))):
                                break
                            if (u(v5) <= u(v7)):
                                break
                            if ((v7 | v16) < 0):
                                break
                            v11 = (v19 + (load32((((v7 + ((v6 + v10) * v6)) << 2) + v15) + 4) * 132))
                            if (load16u((v19 + (load32((((v7 + ((v6 + v10) * v6)) << 2) + v15) + 4) * 132)) + 110) != v18):
                                break
                            while True:  # block $label17
                                # br_table[load32(((load8u(v11 + 122) * 404) + 9568096) + 192)]
                                break
                                break
                            if (load8u(v11 + 125) == 0):
                                break
                            break
                        while True:  # block $label18
                            if v28:
                                break
                            if (u(v5) <= u(v13)):
                                break
                            if ((v13 | v16) < 0):
                                break
                            v11 = (v19 + (load32((v15 + ((v7 + ((v6 + v10) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v7 + ((v6 + v10) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # block $label19
                                # br_table[load32(((load8u(v11 + 122) * 404) + 9568096) + 192)]
                                break
                                break
                            if (load8u(v11 + 125) == 0):
                                break
                            break
                        v11 = (v7 - 2)
                        while True:  # block $label20
                            if v28:
                                break
                            if (u(v5) <= u(v11)):
                                break
                            if ((v11 | v16) < 0):
                                break
                            v16 = (v19 + (load32((v15 + ((v13 + ((v6 + v10) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v13 + ((v6 + v10) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # block $label21
                                # br_table[load32(((load8u(v16 + 122) * 404) + 9568096) + 192)]
                                break
                                break
                            if (load8u(v16 + 125) == 0):
                                break
                            break
                        while True:  # block $label22
                            if v30:
                                break
                            if (u(v5) <= u(v11)):
                                break
                            if ((v10 | v11) < 0):
                                break
                            v16 = (v19 + (load32((v15 + ((v13 + ((v6 + v9) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v13 + ((v6 + v9) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # block $label23
                                # br_table[load32(((load8u(v16 + 122) * 404) + 9568096) + 192)]
                                break
                                break
                            if (load8u(v16 + 125) == 0):
                                break
                            break
                        while True:  # block $label24
                            v16 = (u(v5) <= u(v9))
                            if (u(v5) <= u(v9)):
                                break
                            if (u(v5) <= u(v11)):
                                break
                            if ((v9 | v11) < 0):
                                break
                            v11 = (v19 + (load32((v15 + ((v13 + (((v6 + v9) + 1) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v13 + (((v6 + v9) + 1) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # block $label25
                                # br_table[load32(((load8u(v11 + 122) * 404) + 9568096) + 192)]
                                break
                                break
                            if (load8u(v11 + 125) == 0):
                                break
                            break
                        while True:  # block $label26
                            if v16:
                                break
                            if (u(v5) <= u(v13)):
                                break
                            if ((v9 | v13) < 0):
                                break
                            v11 = (v19 + (load32((v15 + ((v7 + (((v6 + v9) + 1) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v7 + (((v6 + v9) + 1) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # block $label27
                                # br_table[load32(((load8u(v11 + 122) * 404) + 9568096) + 192)]
                                break
                                break
                            if (load8u(v11 + 125) == 0):
                                break
                            break
                        if v16:
                            break
                        if (u(v5) <= u(v7)):
                            break
                        if ((v7 | v9) < 0):
                            break
                        v6 = (v19 + (load32((((v7 + (((v6 + v9) + 1) * v6)) << 2) + v15) + 4) * 132))
                        if (load16u((v19 + (load32((((v7 + (((v6 + v9) + 1) * v6)) << 2) + v15) + 4) * 132)) + 110) != v18):
                            break
                        while True:  # block $label28
                            # br_table[load32(((load8u(v6 + 122) * 404) + 9568096) + 192)]
                            break
                            break
                        if load8u(v6 + 125):
                            break
                        break
                    store32(arg0, v13)
                    store32(arg1, v10)
                    arg2 = 1
                    break
                    break
                v6 = (v8 + 2)
                if (u(v8) < u(38)):
                    continue
                break
            break
        v6 = ((v25 * 404) + 9568096)
        v13 = (load32(((v25 * 404) + 9568096) + 220) + 2)
        v7 = (load32(v6 + 216) + 2)
        while True:  # block $label30
            if (arg4 == 0):
                break
            arg3 = (v7 * v13)
            if ((v7 * v13) == 0):
                break
            # TODO: memory.fill []
            break
        arg3 = 2147483647
        v28 = load32(v6 + 60)
        if load32(v6 + 60):
            v29 = ((v26 * 404) + 9568312)
            v30 = ((v25 * 404) + 9568152)
            v5 = 0
            while True:  # $label41
                while True:  # block $label31
                    v6 = load32(v30)
                    v9 = (v5 << 2)
                    v8 = load32((load32(v30) + ((v5 << 2) | 4)))
                    v18 = (load32((load32(v30) + ((v5 << 2) | 4))) + v22)
                    v10 = ((load32((load32(v30) + ((v5 << 2) | 4))) + v22) - v23)
                    v9 = load32((v6 + v9))
                    v19 = (load32((v6 + v9)) + v24)
                    v6 = ((load32((v6 + v9)) + v24) - v27)
                    v6 = ((((load32((load32(v30) + ((v5 << 2) | 4))) + v22) - v23) * v10) + (((load32((v6 + v9)) + v24) - v27) * v6))
                    if (((((load32((load32(v30) + ((v5 << 2) | 4))) + v22) - v23) * v10) + (((load32((v6 + v9)) + v24) - v27) * v6)) >= arg3):
                        break
                    v10 = load32(9142440)
                    if (u(load32(9142440)) <= u(v18)):
                        break
                    if ((v18 | v19) < 0):
                        break
                    if (u(v10) <= u(v19)):
                        break
                    v10 = (v10 + 2)
                    v10 = load32((load32(9142840) + (((v9 + v12) + (((v8 + v14) + ((v10 + 2) * v21)) * v10)) << 2)))
                    if (v20 != load32((load32(9142840) + (((v9 + v12) + (((v8 + v14) + ((v10 + 2) * v21)) * v10)) << 2)))):
                        if (v10 == -1):
                            break
                        if (load8u((load32(9671128) + (v10 * 132)) + 125) != 1):
                            break
                    while True:  # block $label32
                        if (arg4 == 0):
                            break
                        while True:  # block $label33
                            if (v5 == 0):
                                break
                            v10 = (v9 + 1)
                            while True:  # block $label34
                                v16 = (v9 < -1)
                                if (v9 < -1):
                                    break
                                if (v8 < 0):
                                    break
                                if (v7 <= v10):
                                    break
                                if (v8 >= v13):
                                    break
                                # br_table[(load32(((((v7 * v8) + v10) << 2) + 8451904)) - 1)]
                                break
                                break
                            v11 = (v8 - 1)
                            while True:  # block $label35
                                v31 = (v9 < 0)
                                if (v9 < 0):
                                    break
                                if (v8 <= 0):
                                    break
                                if (v7 <= v9):
                                    break
                                if (v8 > v13):
                                    break
                                # br_table[(load32(((((v7 * v11) + v9) << 2) + 8451904)) - 1)]
                                break
                                break
                            v25 = (v9 - 1)
                            while True:  # block $label36
                                v26 = (v9 <= 0)
                                if (v9 <= 0):
                                    break
                                if (v8 < 0):
                                    break
                                if (v7 < v9):
                                    break
                                if (v8 >= v13):
                                    break
                                # br_table[(load32(((((v7 * v8) + v25) << 2) + 8451904)) - 1)]
                                break
                                break
                            v15 = (v8 + 1)
                            while True:  # block $label37
                                if v31:
                                    break
                                if (v8 < -1):
                                    break
                                if (v7 <= v9):
                                    break
                                if (v13 <= v15):
                                    break
                                # br_table[(load32(((((v7 * v15) + v9) << 2) + 8451904)) - 1)]
                                break
                                break
                            while True:  # block $label38
                                if v16:
                                    break
                                if (v8 <= 0):
                                    break
                                if (v7 <= v10):
                                    break
                                if (v8 > v13):
                                    break
                                # br_table[(load32(((((v7 * v11) + v10) << 2) + 8451904)) - 1)]
                                break
                                break
                            while True:  # block $label39
                                if v26:
                                    break
                                if (v8 <= 0):
                                    break
                                if (v7 < v9):
                                    break
                                if (v8 > v13):
                                    break
                                # br_table[(load32(((((v7 * v11) + v25) << 2) + 8451904)) - 1)]
                                break
                                break
                            while True:  # block $label40
                                if v26:
                                    break
                                if (v8 < -1):
                                    break
                                if (v7 < v9):
                                    break
                                if (v13 <= v15):
                                    break
                                # br_table[(load32(((((v7 * v15) + v25) << 2) + 8451904)) - 1)]
                                break
                                break
                            if v16:
                                break
                            if (v8 < -1):
                                break
                            if (v7 <= v10):
                                break
                            if (v13 <= v15):
                                break
                            # br_table[(load32(((((v7 * v15) + v10) << 2) + 8451904)) - 1)]
                            break
                            break
                        store32(v17 + 4, 0)
                        store8(v17 + 3, 0)
                        v8 = func177(load16u(arg2 + 112), load16u(arg2 + 114), v19, v18, v20, v21, (v17 + 12), (v17 + 8), load32(v29), (v17 + 4), (v17 + 3), 1)
                        store32(((((v7 * v8) + v9) << 2) + 8451904), (2 if func177(load16u(arg2 + 112), load16u(arg2 + 114), v19, v18, v20, v21, (v17 + 12), (v17 + 8), load32(v29), (v17 + 4), (v17 + 3), 1) else 1))
                        if (v8 == 0):
                            break
                        break
                    store32(arg0, v19)
                    store32(arg1, v18)
                    arg3 = v6
                    break
                v5 = (v5 + 2)
                if (u((v5 + 2)) < u(v28)):
                    continue
                break
        arg2 = (arg3 != 2147483647)
        break
    G.global0 = (v17 + 16)
    return arg2

# ------------------------------------------------------------
# $func236
# ------------------------------------------------------------
def func236(arg0, arg1):
    v3 = load32(9142440)
    v4 = (load32(9142440) + 2)
    v5 = load32(arg0 + 28)
    v6 = load32(9671128)
    v7 = load32(9142840)
    v8 = load16u(arg1 + 114)
    v9 = load16u(arg1 + 112)
    v10 = load16u(arg1 + 110)
    v11 = load8u(arg1 + 122)
    arg0 = 0
    while True:  # block $label1
        while True:  # $label2
            while True:  # block $label0
                arg1 = arg0
                v2 = (arg0 << 2)
                arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v8)
                if (u(v3) <= u((load32((((arg0 << 2) | 4) + 8611904)) + v8))):
                    break
                v2 = (load32((v2 + 8611904)) + v9)
                if (u(v3) <= u((load32((v2 + 8611904)) + v9))):
                    break
                if ((arg0 | v2) < 0):
                    break
                arg0 = load32((((v2 + (((arg0 + v4) + 1) * v4)) << 2) + v7) + 4)
                if (load32((((v2 + (((arg0 + v4) + 1) * v4)) << 2) + v7) + 4) == 0):
                    break
                if (arg0 == v5):
                    break
                v2 = (v6 + (arg0 * 132))
                if (load16u((v6 + (arg0 * 132)) + 110) != v10):
                    break
                if (load8u(v2 + 122) == v11):
                    break
                break
            arg0 = (arg1 + 2)
            if (u(arg1) < u(878)):
                continue
            break
        arg0 = 0
        while True:  # $label4
            while True:  # block $label3
                arg1 = arg0
                v2 = (arg0 << 2)
                arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v8)
                if (u(v3) <= u((load32((((arg0 << 2) | 4) + 8611904)) + v8))):
                    break
                v2 = (load32((v2 + 8611904)) + v9)
                if (u(v3) <= u((load32((v2 + 8611904)) + v9))):
                    break
                if ((arg0 | v2) < 0):
                    break
                arg0 = load32((((v2 + (((arg0 + v4) + 1) * v4)) << 2) + v7) + 4)
                if (load32((((v2 + (((arg0 + v4) + 1) * v4)) << 2) + v7) + 4) == 0):
                    break
                if (arg0 == v5):
                    break
                v2 = (v6 + (arg0 * 132))
                if (load16u((v6 + (arg0 * 132)) + 110) != v10):
                    break
                if (load32(((load8u(v2 + 122) * 404) + 9568096) + 264) == 0):
                    break
                break
            arg0 = (arg1 + 2)
            if (u(arg1) < u(878)):
                continue
            break
        arg0 = 0
        break
    return arg0

# ------------------------------------------------------------
# $func238
# ------------------------------------------------------------
def func238(arg0, arg1, arg2):
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label0
        v6 = load32(9561692)
        v3 = (load32(9561692) + (arg1 * 286704))
        v7 = (((load32(9561692) + (arg1 * 286704)) + (arg0 << 2)) + 281808)
        if load32((((load32(9561692) + (arg1 * 286704)) + (arg0 << 2)) + 281808)):
            break
        if (load32(v3 + 283908) == load32(9142872)):
            store32(v5 + 16, load32(39232))
            a_b()
        v4 = load32(((arg0 * 404) + 9568096) + 368)
        if ((arg2 == 0) & (load32(((arg0 * 404) + 9568096) + 368) == 55)):
            break
        v3 = (v3 + 283908)
        while True:  # block $label1
            if v4:
                # call_indirect[v4]
                if (v4 == 55):
                    break
            store32(v7, 1)
            if (load32(v3) == load32(9142872)):
                store32(v5, (load32(load32(((arg0 * 404) + 9568096) + 180) + 8) * 48))
                a_b()
            if load8u(9142905):
                break
            # TODO: i32.div_u []
            store32((load32(9142848) * 25), (((load32(((arg0 * 404) + 9568096) + 116) * load32(load32(9142424) + 132)) * 1000) - 100))
            break
        store32((((v6 + (arg1 * 286704)) + (arg0 << 2)) + 282828), 0)
        if (load32(v3) != load32(9142872)):
            break
        arg2 = ((arg0 * 404) + 9568096)
        if (load32(((arg0 * 404) + 9568096) + 244) == 0):
            break
        arg1 = 0
        while True:  # $label5
            v6 = load32((load32(arg2 + 240) + (arg1 << 2)))
            while True:  # block $label2
                if load8u(9147141):
                    break
                arg0 = 0
                v3 = load32(9671120)
                if (load32(9671120) == 0):
                    break
                while True:  # $label4
                    while True:  # block $label3
                        v4 = load32(((arg0 << 2) + 9263072))
                        if (load32(((arg0 << 2) + 9263072)) == 0):
                            break
                        if (load32(v4 + 12) != v6):
                            break
                        if load8u(v4 + 24):
                            break
                        break
                        break
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v3):
                        continue
                    break
                break
            arg1 = (arg1 + 1)
            if (u((arg1 + 1)) < u(load32(arg2 + 244))):
                continue
            break
        break
    G.global0 = (v5 + 32)

# ------------------------------------------------------------
# $func239
# ------------------------------------------------------------
def func239(arg0):
    v2 = (arg0 * 286704)
    v1 = ((arg0 * 286704) + load32(9561692))
    store32((((arg0 * 286704) + load32(9561692)) + 281784), arg0)
    if (load32(9147132) == 0):
        arg0 = load32(9142892)
        arg0 = (-1 if (u((arg0 * 255)) > u(1073741823)) else (load32(9142892) * 1020))
        v3 = func26((-1 if (u((arg0 * 255)) > u(1073741823)) else (load32(9142892) * 1020)))
        # TODO: memory.fill []
        store32(v1 + 278556, v3)
        v1 = func26(arg0)
        # TODO: memory.fill []
        store32(((load32(9561692) + v2) + 278560), v1)
        v1 = func26(arg0)
        # TODO: memory.fill []
        store32(((load32(9561692) + v2) + 278564), v1)
        v1 = func26(arg0)
        # TODO: memory.fill []
        store32(((load32(9561692) + v2) + 278568), v1)
        arg0 = func26(16)
        store32(func26(16) + 4, 21000)
        store32(arg0, func26(84000))
        store64(arg0 + 8, 90194313216000)
        store32(((load32(9561692) + v2) + 278572), arg0)

# ------------------------------------------------------------
# $func240
# ------------------------------------------------------------
def func240(arg0, arg1, arg2):
    v3 = load8u(arg0 + 122)
    v4 = load32(9561692)
    v5 = load16u(arg0 + 110)
    func156(0, arg0, arg1)
    arg1 = ((v3 * 404) + 9568096)
    if (load32(((v3 * 404) + 9568096) + 264) == 4):
        store8(9671157, 1)
    if (load32(arg1 + 208) == 2):
        store8(9671158, 1)
    func144(((v5 * 286704) + v4), load32(arg0 + 28), arg2)
    while True:  # block $label0
        if (load32(arg0 + 76) == 0):
            break
        if (load32(38528) == load8u(arg0 + 122)):
            break
        break
    while True:  # block $label1
        if (load8u(arg0 + 126) != 2):
            break
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) == 2):
            break
        break
    arg1 = load8u(arg0 + 122)
    if (load8u(arg0 + 122) == load32(38996)):
        arg1 = load8u(arg0 + 122)
    while True:  # block $label3
        while True:  # block $label2
            if (load32(38540) == arg1):
                break
            if (load32(38812) == arg1):
                break
            if (load32(38888) != arg1):
                break
            break
        while True:  # block $label4
            # br_table[(load8u(arg0 + 125) - 4)]
            break
            break
        break

# ------------------------------------------------------------
# $func241
# ------------------------------------------------------------
def func241(arg0, arg1, arg2, arg3, arg4, arg5):
    v6 = (G.global0 + -64)
    store64((G.global0 + -64) + 48, 0)
    store64(v6 + 56, 0)
    store64(v6 + 32, 0)
    store64(v6 + 40, 0)
    while True:  # block $label7
        while True:  # block $label4
            while True:  # block $label5
                while True:  # block $label2
                    while True:  # block $label3
                        if arg2:
                            if (u(arg2) >= u(4)):
                                v11 = (arg2 & -4)
                                while True:  # $label0
                                    v13 = (v6 + 32)
                                    v14 = (v9 << 1)
                                    v10 = ((v6 + 32) + (load16u((arg1 + (v9 << 1))) << 1))
                                    store16(((v6 + 32) + (load16u((arg1 + (v9 << 1))) << 1)), (load16u(v10) + 1))
                                    v10 = ((load16u((arg1 + (v14 | 2))) << 1) + v13)
                                    store16(((load16u((arg1 + (v14 | 2))) << 1) + v13), (load16u(v10) + 1))
                                    v10 = ((load16u((arg1 + (v14 | 4))) << 1) + v13)
                                    store16(((load16u((arg1 + (v14 | 4))) << 1) + v13), (load16u(v10) + 1))
                                    v14 = ((load16u((arg1 + (v14 | 6))) << 1) + v13)
                                    store16(((load16u((arg1 + (v14 | 6))) << 1) + v13), (load16u(v14) + 1))
                                    v9 = (v9 + 4)
                                    v7 = (v7 + 4)
                                    if ((v7 + 4) != v11):
                                        continue
                                    break
                            v7 = (arg2 & 3)
                            if (arg2 & 3):
                                while True:  # $label1
                                    v14 = ((v6 + 32) + (load16u((arg1 + (v9 << 1))) << 1))
                                    store16(((v6 + 32) + (load16u((arg1 + (v9 << 1))) << 1)), (load16u(v14) + 1))
                                    v9 = (v9 + 1)
                                    v8 = (v8 + 1)
                                    if ((v8 + 1) != v7):
                                        continue
                                    break
                            v9 = load32(arg4)
                            v11 = 15
                            v7 = load16u(v6 + 62)
                            if load16u(v6 + 62):
                                break
                            break
                        v9 = load32(arg4)
                        break
                    v11 = 14
                    v7 = 0
                    if load16u(v6 + 60):
                        break
                    v11 = 13
                    if load16u(v6 + 58):
                        break
                    v11 = 12
                    if load16u(v6 + 56):
                        break
                    v11 = 11
                    if load16u(v6 + 54):
                        break
                    v11 = 10
                    if load16u(v6 + 52):
                        break
                    v11 = 9
                    if load16u(v6 + 50):
                        break
                    v11 = 8
                    if load16u(v6 + 48):
                        break
                    v11 = 7
                    if load16u(v6 + 46):
                        break
                    v11 = 6
                    if load16u(v6 + 44):
                        break
                    v11 = 5
                    if load16u(v6 + 42):
                        break
                    v11 = 4
                    if load16u(v6 + 40):
                        break
                    v11 = 3
                    if load16u(v6 + 38):
                        break
                    v11 = 2
                    if load16u(v6 + 36):
                        break
                    if (load16u(v6 + 34) == 0):
                        arg0 = load32(arg3)
                        store32(arg3, (load32(arg3) + 4))
                        store32(arg0, 320)
                        arg0 = load32(arg3)
                        store32(arg3, (load32(arg3) + 4))
                        store32(arg0, 320)
                        v10 = 1
                        break
                    v13 = (v9 != 0)
                    v11 = 1
                    v9 = 1
                    break
                    break
                v13 = (v9 if (u(v9) < u(v11)) else v11)
                v15 = 1
                v9 = 1
                while True:  # $label6
                    if load16u(((v6 + 32) + (v9 << 1))):
                        break
                    v9 = (v9 + 1)
                    if ((v9 + 1) != v11):
                        continue
                    break
                v9 = v11
                break
            v8 = -1
            v14 = load16u(v6 + 34)
            if (u(load16u(v6 + 34)) > u(2)):
                break
            v10 = load16u(v6 + 36)
            v12 = (load16u(v6 + 36) + (v14 << 1))
            if (u((load16u(v6 + 36) + (v14 << 1))) > u(4)):
                break
            v27 = load16u(v6 + 38)
            v12 = (load16u(v6 + 38) + (v12 << 1))
            if (u((load16u(v6 + 38) + (v12 << 1))) > u(8)):
                break
            v16 = load16u(v6 + 40)
            v12 = (load16u(v6 + 40) + (v12 << 1))
            if ((load16u(v6 + 40) + (v12 << 1)) > 16):
                break
            v21 = load16u(v6 + 42)
            v12 = (32 - (load16u(v6 + 42) + (v12 << 1)))
            if ((32 - (load16u(v6 + 42) + (v12 << 1))) < 0):
                break
            v12 = load16u(v6 + 44)
            v17 = ((v12 << 1) - load16u(v6 + 44))
            if (((v12 << 1) - load16u(v6 + 44)) < 0):
                break
            v17 = load16u(v6 + 46)
            v18 = ((v17 << 1) - load16u(v6 + 46))
            if (((v17 << 1) - load16u(v6 + 46)) < 0):
                break
            v18 = load16u(v6 + 48)
            v19 = ((v18 << 1) - load16u(v6 + 48))
            if (((v18 << 1) - load16u(v6 + 48)) < 0):
                break
            v19 = load16u(v6 + 50)
            v20 = ((v19 << 1) - load16u(v6 + 50))
            if (((v19 << 1) - load16u(v6 + 50)) < 0):
                break
            v20 = load16u(v6 + 52)
            v22 = ((v20 << 1) - load16u(v6 + 52))
            if (((v20 << 1) - load16u(v6 + 52)) < 0):
                break
            v22 = load16u(v6 + 54)
            v23 = ((v22 << 1) - load16u(v6 + 54))
            if (((v22 << 1) - load16u(v6 + 54)) < 0):
                break
            v23 = load16u(v6 + 56)
            v24 = ((v23 << 1) - load16u(v6 + 56))
            if (((v23 << 1) - load16u(v6 + 56)) < 0):
                break
            v24 = load16u(v6 + 58)
            v25 = ((v24 << 1) - load16u(v6 + 58))
            if (((v24 << 1) - load16u(v6 + 58)) < 0):
                break
            v25 = load16u(v6 + 60)
            v26 = ((v25 << 1) - load16u(v6 + 60))
            if (((v25 << 1) - load16u(v6 + 60)) < 0):
                break
            v26 = (v26 << 1)
            if (u((v26 << 1)) < u(v7)):
                break
            if ((v7 != v26) if ((arg0 == 0) | v15) else 0):
                break
            v15 = (u(v9) < u(v13))
            v8 = 0
            store16(v6 + 2, 0)
            store16(v6 + 4, v14)
            v7 = (v10 + v14)
            store16(v6 + 6, (v10 + v14))
            v7 = (v7 + v27)
            store16(v6 + 8, (v7 + v27))
            v7 = (v7 + v16)
            store16(v6 + 10, (v7 + v16))
            v7 = (v7 + v21)
            store16(v6 + 12, (v7 + v21))
            v7 = (v7 + v12)
            store16(v6 + 14, (v7 + v12))
            v7 = (v7 + v17)
            store16(v6 + 16, (v7 + v17))
            v7 = (v7 + v18)
            store16(v6 + 18, (v7 + v18))
            v7 = (v7 + v19)
            store16(v6 + 20, (v7 + v19))
            v7 = (v7 + v20)
            store16(v6 + 22, (v7 + v20))
            v7 = (v7 + v22)
            store16(v6 + 24, (v7 + v22))
            v7 = (v7 + v23)
            store16(v6 + 26, (v7 + v23))
            v7 = (v7 + v24)
            store16(v6 + 28, (v7 + v24))
            store16(v6 + 30, (v7 + v25))
            while True:  # block $label8
                if (arg2 == 0):
                    break
                if (arg2 != 1):
                    v14 = (arg2 & -2)
                    v7 = 0
                    while True:  # $label9
                        v10 = load16u((arg1 + (v8 << 1)))
                        if load16u((arg1 + (v8 << 1))):
                            v10 = (v6 + (v10 << 1))
                            v10 = load16u(v10)
                            store16((v6 + (v10 << 1)), (load16u(v10) + 1))
                            store16((arg5 + (v10 << 1)), v8)
                        v10 = (v8 | 1)
                        v12 = load16u((arg1 + ((v8 | 1) << 1)))
                        if load16u((arg1 + ((v8 | 1) << 1))):
                            v12 = (v6 + (v12 << 1))
                            v12 = load16u(v12)
                            store16((v6 + (v12 << 1)), (load16u(v12) + 1))
                            store16((arg5 + (v12 << 1)), v10)
                        v8 = (v8 + 2)
                        v7 = (v7 + 2)
                        if ((v7 + 2) != v14):
                            continue
                        break
                if ((arg2 & 1) == 0):
                    break
                arg2 = load16u((arg1 + (v8 << 1)))
                if (load16u((arg1 + (v8 << 1))) == 0):
                    break
                arg2 = (v6 + (arg2 << 1))
                arg2 = load16u(arg2)
                store16((v6 + (arg2 << 1)), (load16u(arg2) + 1))
                store16((arg5 + (arg2 << 1)), v8)
                break
            v10 = (v13 if v15 else v9)
            v21 = 20
            v22 = 0
            v14 = arg5
            v12 = arg5
            v17 = 0
            while True:  # block $label10
                while True:  # block $label12
                    while True:  # block $label11
                        # br_table[arg0]
                        break
                        break
                    v8 = 1
                    if (u(v10) > u(9)):
                        break
                    v21 = 257
                    v12 = 26272
                    v14 = 26208
                    v17 = 1
                    break
                    break
                v22 = (arg0 == 2)
                v21 = 0
                v12 = 26400
                v14 = 26336
                if (arg0 != 2):
                    break
                v8 = 1
                if (u(v10) > u(9)):
                    break
                break
            v18 = (1 << v10)
            v24 = ((1 << v10) - 1)
            v19 = load32(arg3)
            v20 = 0
            v7 = v10
            v16 = 0
            v15 = 0
            arg0 = -1
            while True:  # $label20
                v27 = (1 << v7)
                while True:  # block $label16
                    while True:  # $label17
                        v13 = (v9 - v16)
                        while True:  # block $label13
                            v7 = load16u((arg5 + (v20 << 1)))
                            if (u((load16u((arg5 + (v20 << 1))) + 1)) < u(v21)):
                                break
                            if (u(v7) < u(v21)):
                                v7 = 0
                                break
                            arg2 = ((v7 - v21) << 1)
                            v7 = load16u((v14 + ((v7 - v21) << 1)))
                            break
                        arg2 = load8u((arg2 + v12))
                        v25 = ((v15 & 0xFFFFFFFF) >> v16)
                        v26 = (-1 << v13)
                        v8 = v27
                        while True:  # $label14
                            v8 = (v8 + v26)
                            v23 = (v19 + (((v8 + v26) + v25) << 2))
                            store16((v19 + (((v8 + v26) + v25) << 2)) + 2, v7)
                            store8(v23 + 1, v13)
                            store8(v23, arg2)
                            if v8:
                                continue
                            break
                        v7 = (1 << (v9 - 1))
                        while True:  # $label15
                            arg2 = v7
                            v7 = ((v7 & 0xFFFFFFFF) >> 1)
                            if (arg2 & v15):
                                continue
                            break
                        v8 = ((v6 + 32) + (v9 << 1))
                        v8 = (load16u(v8) - 1)
                        store16(((v6 + 32) + (v9 << 1)), (load16u(v8) - 1))
                        v15 = ((((arg2 - 1) & v15) + arg2) if arg2 else 0)
                        v20 = (v20 + 1)
                        if ((v8 & 65535) == 0):
                            if (v9 == v11):
                                break
                            v9 = load16u((arg1 + (load16u((arg5 + (v20 << 1))) << 1)))
                        if (u(v9) <= u(v10)):
                            continue
                        arg2 = (v15 & v24)
                        if ((v15 & v24) == arg0):
                            continue
                        break
                    v16 = (v16 if v16 else v10)
                    v7 = (v9 - (v16 if v16 else v10))
                    v13 = (1 << (v9 - (v16 if v16 else v10)))
                    if (u(v9) < u(v11)):
                        arg0 = (v11 - v16)
                        v8 = v9
                        while True:  # block $label18
                            while True:  # $label19
                                v8 = (v13 - load16u(((v6 + 32) + (v8 << 1))))
                                if ((v13 - load16u(((v6 + 32) + (v8 << 1)))) <= 0):
                                    break
                                v13 = (v8 << 1)
                                v7 = (v7 + 1)
                                v8 = ((v7 + 1) + v16)
                                if (u(((v7 + 1) + v16)) < u(v11)):
                                    continue
                                break
                            v7 = arg0
                            break
                        v13 = (1 << v7)
                    v8 = 1
                    v18 = (v13 + v18)
                    if (v17 & (u((v13 + v18)) > u(852))):
                        break
                    if (v22 & (u(v18) > u(592))):
                        break
                    v8 = load32(arg3)
                    arg0 = (load32(arg3) + (arg2 << 2))
                    store8((load32(arg3) + (arg2 << 2)) + 1, v10)
                    store8(arg0, v7)
                    v19 = (v19 + (v27 << 2))
                    store16(arg0 + 2, ((((v19 + (v27 << 2)) - v8) & 0xFFFFFFFF) >> 2))
                    arg0 = arg2
                    continue
                    break
                break
            if v15:
                arg0 = (v19 + (v15 << 2))
                store16((v19 + (v15 << 2)) + 2, 0)
                store8(arg0 + 1, v13)
                store8(arg0, 64)
            store32(arg3, (load32(arg3) + (v18 << 2)))
            break
        store32(arg4, v10)
        v8 = 0
        break
    return v8

# ------------------------------------------------------------
# $func242
# ------------------------------------------------------------
def func242(arg0):
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label2
        while True:  # block $label1
            while True:  # block $label0
                v1 = load8u((load32(9671128) + (load32(9173808) * 132)) + 122)
                if (load8u((load32(9671128) + (load32(9173808) * 132)) + 122) == load32(38540)):
                    break
                if (load32(38812) == v1):
                    break
                if (load32(38888) != v1):
                    break
                break
            store32(v2 + 4, load32(9213816))
            v1 = load8u(9147210)
            arg0 = load32(9213808)
            if (load32(9671124) == 95):
                if v1:
                    func41(7, 9173808, arg0, (v2 + 4), 1)
                    break
                v3 = (arg0 << 2)
                v1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                if arg0:
                    # TODO: memory.copy []
                # call_indirect[load32(9213880)]
                break
            if v1:
                func41(8, 9173808, arg0, (v2 + 4), 1)
                break
            v3 = (arg0 << 2)
            v1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg0:
                # TODO: memory.copy []
            # call_indirect[load32(9213888)]
            break
            break
        v4 = load8u(9163793)
        v1 = load8u(9163792)
        v3 = load8u(9163794)
        v5 = load32(9213812)
        v6 = load8u(9685856)
        store32(v2 + 4, arg0)
        arg0 = (0 if v6 else v5)
        arg0 = (arg0 == 1)
        store32(v2 + 12, (0 if (arg0 == 1) else (0 if v6 else v5)))
        v4 = (-1 if v4 else (5 if v1 else (100 if v3 else 1)))
        store32(v2 + 8, (-1 if arg0 else ((-1 if v3 else (-1 if v4 else (5 if v1 else (100 if v3 else 1)))) if v1 else v4)))
        arg0 = load32(9213808)
        if load8u(9147210):
            func41(0, 9173808, arg0, (v2 + 4), 3)
            break
        v3 = (arg0 << 2)
        v1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy []
        # call_indirect[load32(9213824)]
        break
    G.global0 = (v2 + 16)

# ------------------------------------------------------------
# $func243
# ------------------------------------------------------------
def func243(arg0, arg1, arg2):
    v6 = (load32(9142892) * arg2)
    v19 = load32(9142440)
    v10 = (load32(9142440) + 2)
    v21 = ((load32(9142440) + 2) << 1)
    v12 = load32(38564)
    v13 = load32(38620)
    v14 = load32(38560)
    v7 = load32(9143004)
    v15 = load32(38500)
    v16 = load32(9671128)
    v17 = load32(9142840)
    arg2 = 0
    while True:  # block $label2
        while True:  # $label7
            while True:  # block $label0
                v20 = arg2
                v3 = (arg2 << 2)
                arg2 = (load32((((arg2 << 2) | 4) + 8611904)) + arg1)
                if (u(v19) <= u((load32((((arg2 << 2) | 4) + 8611904)) + arg1))):
                    break
                v3 = (load32((v3 + 8611904)) + arg0)
                if (u(v19) <= u((load32((v3 + 8611904)) + arg0))):
                    break
                if ((arg2 | v3) < 0):
                    break
                while True:  # block $label1
                    v8 = (v3 + 1)
                    v11 = (arg2 + 1)
                    arg2 = load32((v17 + (((v3 + 1) + ((arg2 + 1) * v10)) << 2)))
                    if (u(load32((v17 + (((v3 + 1) + ((arg2 + 1) * v10)) << 2)))) < u(3)):
                        break
                    v3 = (v16 + (arg2 * 132))
                    if (u(load32((v16 + (arg2 * 132)) + 64)) >= u(load32(v3 + 68))):
                        break
                    v4 = load8u(v3 + 122)
                    v9 = ((load8u(v3 + 122) * 404) + 9568096)
                    if (load32(((load8u(v3 + 122) * 404) + 9568096) + 300) == 0):
                        break
                    if (v4 == v15):
                        break
                    v5 = load16u(v3 + 110)
                    while True:  # block $label3
                        v18 = load16u(v3 + 120)
                        if load16u(v3 + 120):
                        else:
                        if (load8u(((v18 if load8u((v7 + (v5 + v6))) else v5) + (v5 + v6))) == 0):
                            if (load8u(v3 + 127) != 6):
                                break
                            if (load8u(v3 + 128) == 0):
                                break
                            break
                        if load8u(v3 + 128):
                            break
                        break
                    if (load8u(v3 + 125) == 10):
                        break
                    if (load8u(v3 + 126) == 2):
                        break
                    if (load32(v9 + 264) == 2):
                        break
                    if (load32(v9 + 188) != 55):
                        break
                    if (v4 == v14):
                        break
                    if (v4 == v13):
                        break
                    if (v4 == v12):
                        break
                    break
                while True:  # block $label4
                    arg2 = load32((v17 + ((v8 + ((v10 + v11) * v10)) << 2)))
                    if (u(load32((v17 + ((v8 + ((v10 + v11) * v10)) << 2)))) < u(3)):
                        break
                    v3 = (v16 + (arg2 * 132))
                    if (u(load32((v16 + (arg2 * 132)) + 64)) >= u(load32(v3 + 68))):
                        break
                    v4 = load8u(v3 + 122)
                    v9 = ((load8u(v3 + 122) * 404) + 9568096)
                    if (load32(((load8u(v3 + 122) * 404) + 9568096) + 300) == 0):
                        break
                    if (v4 == v15):
                        break
                    v5 = load16u(v3 + 110)
                    while True:  # block $label5
                        v18 = load16u(v3 + 120)
                        if load16u(v3 + 120):
                        else:
                        if load8u(((v18 if load8u((v7 + (v5 + v6))) else v5) + (v5 + v6))):
                            if (load8u(v3 + 128) == 0):
                                break
                            break
                        if (load8u(v3 + 127) != 6):
                            break
                        if load8u(v3 + 128):
                            break
                        break
                    if (load8u(v3 + 125) == 10):
                        break
                    if (load8u(v3 + 126) == 2):
                        break
                    if (load32(v9 + 264) == 2):
                        break
                    if (load32(v9 + 188) != 55):
                        break
                    if (v4 == v14):
                        break
                    if (v4 == v13):
                        break
                    if (v4 == v12):
                        break
                    break
                arg2 = load32((v17 + ((v8 + ((v11 + v21) * v10)) << 2)))
                if (u(load32((v17 + ((v8 + ((v11 + v21) * v10)) << 2)))) < u(3)):
                    break
                v3 = (v16 + (arg2 * 132))
                if (u(load32((v16 + (arg2 * 132)) + 64)) >= u(load32(v3 + 68))):
                    break
                v5 = load8u(v3 + 122)
                v8 = ((load8u(v3 + 122) * 404) + 9568096)
                if (load32(((load8u(v3 + 122) * 404) + 9568096) + 300) == 0):
                    break
                if (v5 == v15):
                    break
                v4 = load16u(v3 + 110)
                while True:  # block $label6
                    v11 = load16u(v3 + 120)
                    if load16u(v3 + 120):
                    else:
                    if load8u(((v11 if load8u((v7 + (v4 + v6))) else v4) + (v4 + v6))):
                        if (load8u(v3 + 128) == 0):
                            break
                        break
                    if (load8u(v3 + 127) != 6):
                        break
                    if load8u(v3 + 128):
                        break
                    break
                if (load8u(v3 + 125) == 10):
                    break
                if (load8u(v3 + 126) == 2):
                    break
                if (load32(v8 + 264) == 2):
                    break
                if (load32(v8 + 188) != 55):
                    break
                if (v5 == v14):
                    break
                if (v5 == v13):
                    break
                if (v5 == v12):
                    break
                break
            arg2 = (v20 + 2)
            if (u(v20) < u(1678)):
                continue
            break
        arg2 = 0
        break
    return arg2

# ------------------------------------------------------------
# $func244
# ------------------------------------------------------------
def func244(arg0):
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label2
        while True:  # block $label0
            if (load8u(9142916) == 0):
                break
            arg0 = load32(arg0 + 32)
            if ((load32(arg0 + 32) != 27) & (arg0 != 6)):
                break
            while True:  # block $label1
                arg0 = load32(9299896)
                if load32(9299896):
                    arg0 = (arg0 - 1)
                    store32(9299896, (arg0 - 1))
                    v1 = load32((load32(9299888) + (arg0 << 2)))
                    break
                v1 = load32(9163780)
                arg0 = (load32(9163780) + 1)
                store32(9163780, (load32(9163780) + 1))
                v3 = load32(9163788)
                if (u(arg0) < u(load32(9163788))):
                    break
                store32(v2 + 16, v3)
                a_b()
                store32(9163788, (load32(9163788) + 40000))
                break
            v1 = (v1 + 1073741823)
            break
            break
        if load8u(9142917):
            break
        arg0 = load32(9299880)
        if load32(9299880):
            arg0 = (arg0 - 1)
            store32(9299880, (arg0 - 1))
            v1 = load32((load32(9299872) + (arg0 << 2)))
            break
        v1 = load32(9163776)
        arg0 = (load32(9163776) + 1)
        store32(9163776, (load32(9163776) + 1))
        v3 = load32(9163784)
        if (u(arg0) < u(load32(9163784))):
            break
        store32(v2, v3)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    G.global0 = (v2 + 32)
    return v1

# ------------------------------------------------------------
# $func245
# ------------------------------------------------------------
def func245():
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if load8u(9142917):
            break
        v0 = load32(9299880)
        if load32(9299880):
            v0 = (v0 - 1)
            store32(9299880, (v0 - 1))
            v0 = load32((load32(9299872) + (v0 << 2)))
            break
        v0 = load32(9163776)
        v2 = (load32(9163776) + 1)
        store32(9163776, (load32(9163776) + 1))
        v3 = load32(9163784)
        if (u(v2) < u(load32(9163784))):
            break
        store32(v1, v3)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    G.global0 = (v1 + 16)
    return v0

# ------------------------------------------------------------
# $func246
# ------------------------------------------------------------
def func246(arg0):
    a_v(load32(arg0))
    store32(arg0, 0)
    v1 = load32(arg0 + 188)
    if load32(arg0 + 188):
        v3 = load32(v1)
        if load32(v1):
            while True:  # $label0
                v1 = load32(arg0 + 188)
                v2 = (v2 + 1)
                v3 = load32((load32(arg0 + 188) + ((v2 + 1) << 2)))
                if load32((load32(arg0 + 188) + ((v2 + 1) << 2))):
                    continue
                break

# ------------------------------------------------------------
# $func247
# ------------------------------------------------------------
def func247(arg0, arg1):
    v6 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # block $label0
        if (load8u(arg1 + 125) == 3):
            break
        v9 = load32(arg0 + 16)
        while True:  # block $label5
            while True:  # block $label6
                while True:  # block $label4
                    while True:  # block $label3
                        while True:  # block $label2
                            while True:  # block $label1
                                # br_table[load32(arg0 + 8)]
                                break
                                break
                            v4 = (5 if (v9 == 1) else 0)
                            v3 = (load32(arg0 + 24) + ((load32(arg0 + 40) & 0xFFFFFFFF) >> 1))
                            v2 = (load32(arg0 + 20) + ((load32(arg0 + 28) & 0xFFFFFFFF) >> 1))
                            break
                            break
                        v2 = load32(arg0 + 36)
                        store64(v6 + 16, load64(arg0 + 72))
                        store64(v6 + 8, load64(arg0 + 64))
                        v7 = func300(v2, (v6 + 8), arg1)
                        break
                        break
                    v4 = load32(arg0 + 104)
                    if (load32(arg0 + 104) == 0):
                        break
                    v11 = load32(arg0 + 96)
                    v12 = load16u(arg1 + 114)
                    v13 = load16u(arg1 + 112)
                    v14 = load32(9671128)
                    v8 = load32(arg1 + 28)
                    v2 = 2147483647
                    arg0 = 0
                    while True:  # $label7
                        v3 = load32((v11 + (arg0 << 2)))
                        if (v8 != load32((v11 + (arg0 << 2)))):
                            v3 = (v14 + (v3 * 132))
                            v10 = ((load16u((v14 + (v3 * 132)) + 114) - v12) << 1)
                            v10 = ((load16u(v3 + 112) - v13) << 1)
                            v10 = ((((load16u((v14 + (v3 * 132)) + 114) - v12) << 1) * v10) + (((load16u(v3 + 112) - v13) << 1) * v10))
                            v10 = (v2 > v10)
                            v2 = (((((load16u((v14 + (v3 * 132)) + 114) - v12) << 1) * v10) + (((load16u(v3 + 112) - v13) << 1) * v10)) if (v2 > v10) else v2)
                            v7 = (load32(v3 + 28) if v10 else v7)
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != v4):
                            continue
                        break
                    break
                    break
                v4 = load32(9140300)
                if (load32(9140300) == 0):
                    break
                v11 = load16u(arg1 + 114)
                v12 = load16u(arg1 + 112)
                v13 = load32(9671128)
                v14 = load32(arg1 + 28)
                v2 = 2147483647
                arg0 = 0
                while True:  # $label8
                    v3 = load32(((arg0 << 2) + 8451904))
                    if (v14 != load32(((arg0 << 2) + 8451904))):
                        v3 = (v13 + (v3 * 132))
                        v8 = ((load16u((v13 + (v3 * 132)) + 114) - v11) << 1)
                        v8 = ((load16u(v3 + 112) - v12) << 1)
                        v8 = ((((load16u((v13 + (v3 * 132)) + 114) - v11) << 1) * v8) + (((load16u(v3 + 112) - v12) << 1) * v8))
                        v8 = (v2 > v8)
                        v2 = (((((load16u((v13 + (v3 * 132)) + 114) - v11) << 1) * v8) + (((load16u(v3 + 112) - v12) << 1) * v8)) if (v2 > v8) else v2)
                        v7 = (load32(v3 + 28) if v8 else v7)
                    arg0 = (arg0 + 1)
                    if ((arg0 + 1) != v4):
                        continue
                    break
                break
            v4 = 0
            v2 = 0
            v3 = 0
            if (v7 == 0):
                break
            break
        while True:  # block $label18
            while True:  # block $label10
                while True:  # block $label17
                    while True:  # block $label16
                        while True:  # block $label15
                            while True:  # block $label14
                                while True:  # block $label13
                                    while True:  # block $label12
                                        while True:  # block $label11
                                            while True:  # block $label9
                                                # br_table[v9]
                                                break
                                                break
                                            if (v7 == 0):
                                                v7 = 0
                                                break
                                            store32(v6 + 32, load32(arg1 + 28))
                                            v5 = func161((load32(9671128) + (v7 * 132)), (v6 + 32), 1)
                                            break
                                            break
                                        v5 = 6
                                        break
                                        break
                                    v5 = 1
                                    break
                                    break
                                v5 = 4
                                break
                                break
                            v5 = 25
                            break
                            break
                        store64(v6 + 48, 4294967296)
                        store32(v6 + 36, v3)
                        store32(v6 + 32, v2)
                        store32(v6 + 40, v7)
                        store32(v6 + 56, 0)
                        store32(v6 + 44, (6 if v7 else 0))
                        store32(v6 + 28, load32(arg1 + 28))
                        break
                        break
                    if v7:
                        arg0 = (load32(9671128) + (v7 * 132))
                        v2 = ((load8u((load32(9671128) + (v7 * 132)) + 122) * 404) + 9568096)
                        v3 = (((load32(((load8u((load32(9671128) + (v7 * 132)) + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1) + load16u(arg0 + 114))
                        v2 = (load16u(arg0 + 112) + ((load32(v2 + 216) & 0xFFFFFFFF) >> 1))
                    store64(v6 + 52, 0)
                    store64(v6 + 44, 0)
                    store32(v6 + 40, -1)
                    store32(v6 + 36, v3)
                    store32(v6 + 32, v2)
                    store32(v6 + 28, load32(arg1 + 28))
                    break
                    break
                while True:  # block $label19
                    if (v9 != 8):
                        break
                    if (v7 == 0):
                        break
                    while True:  # block $label22
                        while True:  # block $label21
                            while True:  # block $label20
                                v2 = load32(arg1 + 20)
                                if (load32(arg1 + 20) == 0):
                                    arg0 = func26(16)
                                    store32(func26(16) + 4, 7)
                                    store32(arg0, func26(28))
                                    store64(arg0 + 8, 4294967296)
                                    store32(arg1 + 20, arg0)
                                    v5 = (arg0 + 8)
                                    break
                                v3 = 0
                                store32(v2 + 8, 0)
                                v5 = (v2 + 8)
                                if (load32(v2 + 4) == 0):
                                    break
                                arg0 = v2
                                break
                            v4 = load32(arg0)
                            v3 = 0
                            break
                            break
                        arg0 = load32(v2 + 12)
                        store32(v2 + 4, load32(v2 + 12))
                        v9 = load32(v2)
                        v4 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                        arg0 = v2
                        if v9:
                            v3 = load32(v2 + 8)
                            arg0 = load32(arg1 + 20)
                        store32(v2, v4)
                        break
                    store32(v5, (v3 + 1))
                    store32((v4 + (v3 << 2)), 1)
                    while True:  # block $label23
                        v3 = load32(arg0 + 8)
                        if (load32(arg0 + 8) != load32(arg0 + 4)):
                            v4 = load32(arg0)
                            v2 = arg0
                            break
                        v2 = (load32(arg0 + 12) + v3)
                        store32(arg0 + 4, (load32(arg0 + 12) + v3))
                        v5 = load32(arg0)
                        v4 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                        if v3:
                            # TODO: memory.copy []
                        v2 = arg0
                        if v5:
                            v3 = load32(arg0 + 8)
                            v2 = load32(arg1 + 20)
                        store32(arg0, v4)
                        break
                    store32(arg0 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 2)
                    while True:  # block $label24
                        v3 = load32(v2 + 8)
                        if (load32(v2 + 8) != load32(v2 + 4)):
                            v4 = load32(v2)
                            arg0 = v2
                            break
                        arg0 = (load32(v2 + 12) + v3)
                        store32(v2 + 4, (load32(v2 + 12) + v3))
                        v5 = load32(v2)
                        v4 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                        if v3:
                            # TODO: memory.copy []
                        arg0 = v2
                        if v5:
                            v3 = load32(v2 + 8)
                            arg0 = load32(arg1 + 20)
                        store32(v2, v4)
                        break
                    store32(v2 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 0)
                    while True:  # block $label25
                        v3 = load32(arg0 + 8)
                        if (load32(arg0 + 8) != load32(arg0 + 4)):
                            v4 = load32(arg0)
                            v2 = arg0
                            break
                        v2 = (load32(arg0 + 12) + v3)
                        store32(arg0 + 4, (load32(arg0 + 12) + v3))
                        v5 = load32(arg0)
                        v4 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                        if v3:
                            # TODO: memory.copy []
                        v2 = arg0
                        if v5:
                            v3 = load32(arg0 + 8)
                            v2 = load32(arg1 + 20)
                        store32(arg0, v4)
                        break
                    store32(arg0 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 0)
                    while True:  # block $label26
                        v3 = load32(v2 + 8)
                        if (load32(v2 + 8) != load32(v2 + 4)):
                            v4 = load32(v2)
                            arg0 = v2
                            break
                        arg0 = (load32(v2 + 12) + v3)
                        store32(v2 + 4, (load32(v2 + 12) + v3))
                        v5 = load32(v2)
                        v4 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                        if v3:
                            # TODO: memory.copy []
                        arg0 = v2
                        if v5:
                            v3 = load32(v2 + 8)
                            arg0 = load32(arg1 + 20)
                        store32(v2, v4)
                        break
                    store32(v2 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), v7)
                    while True:  # block $label27
                        v3 = load32(arg0 + 8)
                        if (load32(arg0 + 8) != load32(arg0 + 4)):
                            v4 = load32(arg0)
                            v2 = arg0
                            break
                        v2 = (load32(arg0 + 12) + v3)
                        store32(arg0 + 4, (load32(arg0 + 12) + v3))
                        v5 = load32(arg0)
                        v4 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                        if v3:
                            # TODO: memory.copy []
                        v2 = arg0
                        if v5:
                            v3 = load32(arg0 + 8)
                            v2 = load32(arg1 + 20)
                        store32(arg0, v4)
                        break
                    store32(arg0 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 0)
                    while True:  # block $label28
                        v3 = load32(v2 + 8)
                        if (load32(v2 + 8) != load32(v2 + 4)):
                            v4 = load32(v2)
                            arg0 = v2
                            break
                        arg0 = (load32(v2 + 12) + v3)
                        store32(v2 + 4, (load32(v2 + 12) + v3))
                        v5 = load32(v2)
                        v4 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                        if v3:
                            # TODO: memory.copy []
                        arg0 = v2
                        if v5:
                            v3 = load32(v2 + 8)
                            arg0 = load32(arg1 + 20)
                        store32(v2, v4)
                        break
                    store32(v2 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 0)
                    while True:  # block $label29
                        v3 = load32(arg0 + 8)
                        if (load32(arg0 + 8) != load32(arg0 + 4)):
                            v4 = load32(arg0)
                            v2 = arg0
                            break
                        v2 = (load32(arg0 + 12) + v3)
                        store32(arg0 + 4, (load32(arg0 + 12) + v3))
                        v5 = load32(arg0)
                        v4 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                        if v3:
                            # TODO: memory.copy []
                        v2 = arg0
                        if v5:
                            v3 = load32(arg0 + 8)
                            v2 = load32(arg1 + 20)
                        store32(arg0, v4)
                        break
                    store32(arg0 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 5)
                    while True:  # block $label30
                        arg0 = load32(v2 + 8)
                        if (load32(v2 + 8) != load32(v2 + 4)):
                            v3 = load32(v2)
                            break
                        v3 = (load32(v2 + 12) + arg0)
                        store32(v2 + 4, (load32(v2 + 12) + arg0))
                        v4 = load32(v2)
                        v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                        if arg0:
                            # TODO: memory.copy []
                        if v4:
                            arg0 = load32(v2 + 8)
                        store32(v2, v3)
                        break
                    store32(v2 + 8, (arg0 + 1))
                    store32((v3 + (arg0 << 2)), 0)
                    break
                    break
                arg0 = (v9 - 9)
                if (u((v9 - 9)) > u(21)):
                    break
                v5 = load32(((arg0 << 2) + 10196))
                break
            if (v7 == 0):
                break
            if (load8u(((v5 * 40) + 9671200) + 16) == 0):
                break
            arg0 = (v7 * 132)
            v7 = 0
            arg0 = (arg0 + load32(9671128))
            v2 = ((load8u((arg0 + load32(9671128)) + 122) * 404) + 9568096)
            v3 = (((load32(((load8u((arg0 + load32(9671128)) + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1) + load16u(arg0 + 114))
            v2 = (load16u(arg0 + 112) + ((load32(v2 + 216) & 0xFFFFFFFF) >> 1))
            break
        break
    G.global0 = (v6 - -64)

# ------------------------------------------------------------
# $func248
# ------------------------------------------------------------
def func248(arg0, param1):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(arg0 + 32, 1)
    v2 = (arg0 + 4)
    if (load32(arg0 + 44) != load32(arg0 + 48)):
        while True:  # $label0
            func392((v1 + 4), arg0)
            func54(v2)
            # call_indirect[load32(v1 + 4)]
            if (load32(arg0 + 44) != load32(arg0 + 48)):
                continue
            break
    func54(v2)
    store32(arg0 + 32, 0)
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $func249
# ------------------------------------------------------------
def func249(arg0):
    v1 = (G.global0 - 144)
    G.global0 = (G.global0 - 144)
    # TODO: memory.fill []
    store32(v1 + 52, 5522759)
    store32(v1 + 92, 56)
    store32(v1 + 88, 57)
    store32(v1 + 104, (1 if load8u(59184) else (5 if load8u(59185) else 1)))
    v2 = (v1 + 12)
    while True:  # block $label3
        arg0 = load8u(9681935)
        # TODO: i32.extend8_s []
        v3 = (load8u(9681935) < 0)
        v5 = (load32(9681924) if (load8u(9681935) < 0) else 9681924)
        arg0 = (load32(9681928) if v3 else arg0)
        v6 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        while True:  # block $label0
            if ((load8u(v2 + 11) & 0xFFFFFFFF) >> 7):
                break
            break
        v3 = (load8u(v2 + 11) & 127)
        if (u((load8u(v2 + 11) & 127)) >= u(0)):
            while True:  # block $label1
                if ((load8u(v2 + 11) & 0xFFFFFFFF) >> 7):
                else:
                v4 = 10
                if (u(((load32(v2 + 8) & 2147483647) - 1)) <= u((10 - v3))):
                    if (arg0 == 0):
                        break
                    while True:  # block $label2
                        if ((load8u(v2 + 11) & 0xFFFFFFFF) >> 7):
                            break
                        break
                    v4 = v2
                    if v3:
                        # TODO: memory.copy []
                    else:
                    # TODO: memory.copy []
                    arg0 = (arg0 + v3)
                    func312(v2, (arg0 + v3))
                    store8(v6 + 15, 0)
                    store8((arg0 + v4), load8u(v6 + 15))
                    break
                break
            G.global0 = (v6 + 16)
            break
        a_g()
        raise RuntimeError('unreachable')
        break
    arg0 = v2
    store32(func163(v2, v4, ((arg0 + v3) - v4), v3, 0, 0, arg0, v5) + 32, load32(v2 + 8))
    store64(v1 + 24, load64(arg0))
    store64(arg0, 0)
    store32(arg0 + 8, 0)
    arg0 = func211((v1 + 24), 7778)
    store32(v1 + 48, load32(func211((v1 + 24), 7778) + 8))
    store64(v1 + 40, load64(arg0))
    store64(arg0, 0)
    store32(arg0 + 8, 0)
    if (load8s(v1 + 35) < 0):
    if (load8s(v1 + 23) < 0):
    arg0 = (load32(v1 + 40) if (load8s(v1 + 51) < 0) else (v1 + 40))
    store32(v1, (load32(v1 + 40) if (load8s(v1 + 51) < 0) else (v1 + 40)))
    func179((v1 + 52), arg0)
    if (load8s(v1 + 51) < 0):
    G.global0 = (v1 + 144)
    return af(load32(v1 + 40))

# ------------------------------------------------------------
# $func250
# ------------------------------------------------------------
def func250(arg0, arg1, arg2):
    v13 = load32(9142440)
    v5 = (load32(9142440) + 2)
    v20 = load32(38564)
    v14 = load32(9671128)
    v9 = load32(9142840)
    while True:  # $label10
        while True:  # block $label0
            v15 = v3
            v3 = (v3 << 2)
            v7 = (load32((((v3 << 2) | 4) + 8611904)) + arg1)
            if (u(v13) <= u((load32((((v3 << 2) | 4) + 8611904)) + arg1))):
                break
            v8 = (load32((v3 + 8611904)) + arg0)
            if (u(v13) <= u((load32((v3 + 8611904)) + arg0))):
                break
            if ((v7 | v8) < 0):
                break
            v16 = (v7 + 1)
            v21 = load32((((v8 + (((v7 + 1) + v5) * v5)) << 2) + v9) + 4)
            v3 = (v14 + (load32((((v8 + (((v7 + 1) + v5) * v5)) << 2) + v9) + 4) * 132))
            if (v20 != load8u((v14 + (load32((((v8 + (((v7 + 1) + v5) * v5)) << 2) + v9) + 4) * 132)) + 122)):
                break
            while True:  # block $label1
                # br_table[(load8u(v3 + 125) - 4)]
                break
                break
            v10 = (v8 + 2)
            v17 = (v8 if (v8 > v10) else (v8 + 2))
            v11 = 1
            v18 = (v7 - 1)
            v4 = (v8 - 1)
            v19 = ((v5 + v7) * v5)
            while True:  # block $label2
                v3 = (v7 + 2)
                v12 = (v7 if (v3 < v7) else (v7 + 2))
                if ((v16 == (v7 if (v3 < v7) else (v7 + 2))) | (v7 > 2147483645)):
                    while True:  # $label5
                        v6 = (v4 + 1)
                        v3 = v18
                        while True:  # block $label4
                            if (v4 != v8):
                                while True:  # $label3
                                    v3 = (v3 + 1)
                                    v4 = load32((v9 + (((((v3 + 1) + v5) * v5) + v6) << 2)))
                                    if (load32((v9 + (((((v3 + 1) + v5) * v5) + v6) << 2))) == 0):
                                        break
                                    if (arg2 == v4):
                                        break
                                    if (v3 != v12):
                                        continue
                                    break
                                    break
                                raise RuntimeError('unreachable')
                            v3 = load32((v9 + ((v6 + v19) << 2)))
                            if (load32((v9 + ((v6 + v19) << 2))) == 0):
                                break
                            if (arg2 == v3):
                                break
                            break
                        v11 = (v6 < v10)
                        v4 = v6
                        if (v6 != v17):
                            continue
                        break
                        break
                    raise RuntimeError('unreachable')
                while True:  # $label9
                    v6 = (v4 + 1)
                    v3 = v18
                    while True:  # block $label7
                        if (v4 == v8):
                            v4 = load32((v9 + ((v6 + v19) << 2)))
                            if (load32((v9 + ((v6 + v19) << 2))) == 0):
                                break
                            v3 = v16
                            if (arg2 == v4):
                                break
                            while True:  # $label6
                                v4 = (v3 + 1)
                                if (v3 != v7):
                                    v3 = load32((v9 + ((((v4 + v5) * v5) + v6) << 2)))
                                    if (load32((v9 + ((((v4 + v5) * v5) + v6) << 2))) == 0):
                                        break
                                    if (arg2 == v3):
                                        break
                                v3 = v4
                                if (v4 != v12):
                                    continue
                                break
                            break
                        while True:  # $label8
                            v3 = (v3 + 1)
                            v4 = load32((v9 + (((((v3 + 1) + v5) * v5) + v6) << 2)))
                            if (load32((v9 + (((((v3 + 1) + v5) * v5) + v6) << 2))) == 0):
                                break
                            if (arg2 == v4):
                                break
                            if (v3 != v12):
                                continue
                            break
                        break
                    v11 = (v6 < v10)
                    v4 = v6
                    if (v6 != v17):
                        continue
                    break
                break
            if (v11 == 0):
                break
            return load32((v14 + (v21 * 132)) + 28)
            break
        v3 = (v15 + 2)
        if (u(v15) < u(878)):
            continue
        break
    return 0

# ------------------------------------------------------------
# $func252
# ------------------------------------------------------------
def func252(arg0, arg1):
    while True:  # block $label1
        while True:  # block $label0
            if (arg0 == 0):
                break
            v3 = (i64(arg0) * i64(arg1))
            v2 = i32((i64(arg0) * i64(arg1)))
            if (u((arg0 | arg1)) < u(65536)):
                break
            break
        v2 = (-1 if i32(((v3 & 0xFFFFFFFFFFFFFFFF) >> 32)) else v2)
        arg0 = e()
        if (e() == 0):
            break
        if ((load8u((arg0 - 4)) & 3) == 0):
            break
        func98(arg0, 0, v2)
        break
    return arg0

# ------------------------------------------------------------
# $func254
# ------------------------------------------------------------
def func254(arg0, arg1):
    while True:  # block $label0
        if (arg0 == 0):
            break
        v3 = load32(arg0 + 16)
        arg0 = load32(arg0 + 24)
        if (load32(arg0 + 24) >= 100):
            v4 = load32((((arg0 + v3) << 2) + 32700))
            if (((load32((((arg0 + v3) << 2) + 32700)) < 4294967300.0) & (v4 >= 0.0)) == 0):
                break
            # TODO: i32.trunc_f32_u []
            v2 = v4
            break
        v2 = ((v3 * 1000) // arg0)
        break

# ------------------------------------------------------------
# $func255
# ------------------------------------------------------------
def func255(arg0, arg1):
    store32(arg0, load32(arg1))
    store32(arg0 + 4, load32(arg1 + 4))
    store32(arg0 + 8, load32(arg1 + 8))
    store32(arg0 + 12, load32(arg1 + 12))
    store32(arg0 + 16, load32(arg1 + 16))
    store32(arg0 + 20, load32(arg1 + 20))
    store32(arg0 + 24, load32(arg1 + 24))
    store32(arg0 + 28, load32(arg1 + 28))
    store32(arg0 + 40, load32(arg1 + 40))
    store32(arg0 + 32, load32(arg1 + 32))
    store32(arg0 + 36, load32(arg1 + 36))
    store32(arg0, load32(arg1))
    if load32(arg1 + 56):
        while True:  # $label1
            v6 = load32((load32(arg1 + 48) + (v4 << 2)))
            while True:  # block $label0
                v2 = load32(arg0 + 56)
                if (load32(arg0 + 56) != load32(arg0 + 52)):
                    v3 = load32(arg0 + 48)
                    break
                v3 = (load32(arg0 + 60) + v2)
                store32(arg0 + 52, (load32(arg0 + 60) + v2))
                v5 = load32(arg0 + 48)
                v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                if v2:
                    # TODO: memory.copy []
                if v5:
                    v2 = load32(arg0 + 56)
                store32(arg0 + 48, v3)
                break
            store32(arg0 + 56, (v2 + 1))
            store32((v3 + (v2 << 2)), v6)
            v4 = (v4 + 1)
            if (u((v4 + 1)) < u(load32(arg1 + 56))):
                continue
            break
    if load32(arg1 + 72):
        v4 = 0
        while True:  # $label3
            v6 = load32((load32(arg1 + 64) + (v4 << 2)))
            while True:  # block $label2
                v2 = load32(arg0 + 72)
                if (load32(arg0 + 72) != load32(arg0 + 68)):
                    v3 = load32(arg0 + 64)
                    break
                v3 = (load32(arg0 + 76) + v2)
                store32(arg0 + 68, (load32(arg0 + 76) + v2))
                v5 = load32(arg0 + 64)
                v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                if v2:
                    # TODO: memory.copy []
                if v5:
                    v2 = load32(arg0 + 72)
                store32(arg0 + 64, v3)
                break
            store32(arg0 + 72, (v2 + 1))
            store32((v3 + (v2 << 2)), v6)
            v4 = (v4 + 1)
            if (u((v4 + 1)) < u(load32(arg1 + 72))):
                continue
            break
    if load32(arg1 + 88):
        v4 = 0
        while True:  # $label5
            v6 = load32((load32(arg1 + 80) + (v4 << 2)))
            while True:  # block $label4
                v2 = load32(arg0 + 88)
                if (load32(arg0 + 88) != load32(arg0 + 84)):
                    v3 = load32(arg0 + 80)
                    break
                v3 = (load32(arg0 + 92) + v2)
                store32(arg0 + 84, (load32(arg0 + 92) + v2))
                v5 = load32(arg0 + 80)
                v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                if v2:
                    # TODO: memory.copy []
                if v5:
                    v2 = load32(arg0 + 88)
                store32(arg0 + 80, v3)
                break
            store32(arg0 + 88, (v2 + 1))
            store32((v3 + (v2 << 2)), v6)
            v4 = (v4 + 1)
            if (u((v4 + 1)) < u(load32(arg1 + 88))):
                continue
            break
    if load32(arg1 + 104):
        v4 = 0
        while True:  # $label7
            v6 = load32((load32(arg1 + 96) + (v4 << 2)))
            while True:  # block $label6
                v2 = load32(arg0 + 104)
                if (load32(arg0 + 104) != load32(arg0 + 100)):
                    v3 = load32(arg0 + 96)
                    break
                v3 = (load32(arg0 + 108) + v2)
                store32(arg0 + 100, (load32(arg0 + 108) + v2))
                v5 = load32(arg0 + 96)
                v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                if v2:
                    # TODO: memory.copy []
                if v5:
                    v2 = load32(arg0 + 104)
                store32(arg0 + 96, v3)
                break
            store32(arg0 + 104, (v2 + 1))
            store32((v3 + (v2 << 2)), v6)
            v4 = (v4 + 1)
            if (u((v4 + 1)) < u(load32(arg1 + 104))):
                continue
            break
    while True:  # block $label8
        v3 = load32(arg1 + 192)
        if (load32(arg1 + 192) == 0):
            break
        v2 = 0
        if (u(v3) >= u(4)):
            v8 = (v3 & -4)
            while True:  # $label9
                v5 = (arg0 + 112)
                v4 = (v2 << 1)
                v6 = (arg1 + 112)
                store16(((arg0 + 112) + (v2 << 1)), load16u(((arg1 + 112) + v4)))
                v7 = (v4 | 2)
                store16((v5 + (v4 | 2)), load16u((v6 + v7)))
                v7 = (v4 | 4)
                store16((v5 + (v4 | 4)), load16u((v6 + v7)))
                v4 = (v4 | 6)
                store16((v5 + (v4 | 6)), load16u((v4 + v6)))
                v2 = (v2 + 4)
                v9 = (v9 + 4)
                if ((v9 + 4) != v8):
                    continue
                break
        v4 = (v3 & 3)
        if ((v3 & 3) == 0):
            break
        while True:  # $label10
            v5 = (v2 << 1)
            store16((arg0 + (v2 << 1)) + 112, load16u((arg1 + v5) + 112))
            v2 = (v2 + 1)
            v10 = (v10 + 1)
            if ((v10 + 1) != v4):
                continue
            break
        break
    store32(arg0 + 192, v3)

# ------------------------------------------------------------
# $func256
# ------------------------------------------------------------
def func256(arg0, arg1):
    v2 = load32(arg0 + 24)
    if (load32(arg0 + 24) == 0):
        v2 = func26(16)
        store64(func26(16), 0)
        store64(v2 + 8, 0)
        store32(arg0 + 24, v2)
    while True:  # block $label1
        while True:  # block $label0
            arg0 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                arg0 = func26(16)
                store32(func26(16) + 4, arg1)
                v3 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
                store32(arg0 + 12, 2)
                store32(arg0, v3)
                store32(v2 + 8, arg0)
                store32(arg0 + 8, 0)
                v2 = (arg0 + 8)
                v3 = arg1
                break
            store32(arg0 + 8, 0)
            v2 = (arg0 + 8)
            v3 = load32(arg0 + 4)
            if (u(load32(arg0 + 4)) > u(arg1)):
                break
            break
        v3 = (load32(arg0 + 12) + (arg1 + v3))
        store32(arg0 + 4, (load32(arg0 + 12) + (arg1 + v3)))
        v4 = load32(arg0)
        v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
        if v4:
        store32(arg0, v3)
        break
    while True:  # block $label2
        if (arg1 == 0):
            break
        v4 = (arg1 & 1)
        v3 = load32(arg0)
        arg0 = 0
        if (arg1 != 1):
            v7 = (arg1 & -2)
            arg1 = 0
            while True:  # $label3
                v5 = (arg0 << 2)
                v6 = load32(((arg0 << 2) + 9147392))
                v8 = load32(v2)
                store32(v2, (load32(v2) + 1))
                store32((v3 + (v8 << 2)), v6)
                v5 = load32(((v5 | 4) + 9147392))
                v6 = load32(v2)
                store32(v2, (load32(v2) + 1))
                store32((v3 + (v6 << 2)), v5)
                arg0 = (arg0 + 2)
                arg1 = (arg1 + 2)
                if ((arg1 + 2) != v7):
                    continue
                break
        if (v4 == 0):
            break
        arg0 = load32(((arg0 << 2) + 9147392))
        arg1 = load32(v2)
        store32(v2, (load32(v2) + 1))
        store32((v3 + (arg1 << 2)), arg0)
        break

# ------------------------------------------------------------
# $func257
# ------------------------------------------------------------
def func257(arg0, arg1):
    while True:  # block $label0
        v3 = load32(9142840)
        arg0 = (arg0 + 1)
        v4 = (arg1 + 1)
        arg1 = (load32(9142440) + 2)
        v2 = load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))
        if (u(load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))) < u(3)):
            break
        v2 = (load32(9671128) + (v2 * 132))
        if load32((load32(9671128) + (v2 * 132)) + 40):
            break
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # block $label1
        v2 = load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))
        if (u(load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))) < u(3)):
            break
        v2 = (load32(9671128) + (v2 * 132))
        if load32((load32(9671128) + (v2 * 132)) + 40):
            break
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # block $label2
        arg0 = load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))
        if (u(load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))) < u(3)):
            break
        arg0 = (load32(9671128) + (arg0 * 132))
        if load32((load32(9671128) + (arg0 * 132)) + 40):
            break
        break

# ------------------------------------------------------------
# $func258
# ------------------------------------------------------------
def func258(arg0, arg1):
    while True:  # block $label0
        v3 = load32(9142840)
        arg0 = (arg0 + 1)
        v4 = (arg1 + 1)
        arg1 = (load32(9142440) + 2)
        v2 = load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))
        if (u(load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))) < u(3)):
            break
        v2 = (load32(9671128) + (v2 * 132))
        if load32((load32(9671128) + (v2 * 132)) + 40):
            break
        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 264) == 0):
            break
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # block $label1
        v2 = load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))
        if (u(load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))) < u(3)):
            break
        v2 = (load32(9671128) + (v2 * 132))
        if load32((load32(9671128) + (v2 * 132)) + 40):
            break
        if (load32(((load8u(v2 + 122) * 404) + 9568096) + 264) == 0):
            break
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # block $label2
        arg0 = load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))
        if (u(load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))) < u(3)):
            break
        arg0 = (load32(9671128) + (arg0 * 132))
        if load32((load32(9671128) + (arg0 * 132)) + 40):
            break
        if (load32(((load8u(arg0 + 122) * 404) + 9568096) + 264) == 0):
            break
        break

# ------------------------------------------------------------
# $func259
# ------------------------------------------------------------
def func259(arg0, arg1):
    v2 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    while True:  # $label1
        v4 = ((load32((arg0 + (v7 << 2))) * 404) + 9568096)
        v3 = load32(((load32((arg0 + (v7 << 2))) * 404) + 9568096) + 84)
        v5 = load32(v4 + 100)
        v6 = load32(v4 + 92)
        v8 = load32(v4 + 104)
        v13 = load64(v4 + 76)
        v9 = load32(v4 + 88)
        v14 = load64(v4 + 68)
        v10 = load32(v4 + 264)
        store32(v2 + 80, load32(load32(v4 + 180) + 8))
        store32(v2 + 84, v10)
        store64(v2 + 88, v14)
        store32(v2 + 112, v9)
        store32(v2 + 108, v7)
        store32(v2 + 104, arg1)
        store64(v2 + 96, v13)
        store32(v2 + 68, v8)
        store32(v2 + 72, v6)
        store32(v2 + 76, v5)
        store32(v2 + 64, v3)
        v3 = load32(v4 + 236)
        if load32(v4 + 236):
            v5 = 0
            while True:  # $label0
                v6 = ((load32((load32(v4 + 232) + (v5 << 2))) * 132) + 9216080)
                if load8u(((load32((load32(v4 + 232) + (v5 << 2))) * 132) + 9216080) + 23):
                    v3 = ((load32(v6 + 4) * 404) + 9568096)
                    v8 = load32(((load32(v6 + 4) * 404) + 9568096) + 84)
                    v9 = load32(v3 + 100)
                    v10 = load32(v3 + 92)
                    v11 = load32(v3 + 104)
                    v13 = load64(v3 + 76)
                    v12 = load32(v3 + 88)
                    v14 = load64(v3 + 68)
                    v3 = load32(v3 + 264)
                    store32(v2 + 16, load32(v6 + 8))
                    store32(v2 + 20, v3)
                    store64(v2 + 24, v14)
                    store32(v2 + 48, v12)
                    store64(v2 + 40, 0)
                    store64(v2 + 32, v13)
                    store32(v2 + 4, v11)
                    store32(v2 + 8, v10)
                    store32(v2 + 12, v9)
                    store32(v2, v8)
                    v3 = load32(v4 + 236)
                v5 = (v5 + 1)
                if (u((v5 + 1)) < u(v3)):
                    continue
                break
        v7 = (v7 + 1)
        if ((v7 + 1) != 15):
            continue
        break
    G.global0 = (v2 + 128)

# ------------------------------------------------------------
# $func260
# ------------------------------------------------------------
def func260(arg0, arg1):
    v10 = (G.global0 - 32)
    v9 = load32(arg1)
    v2 = load32(arg1 + 8)
    v4 = load32(load32(arg1 + 8))
    v8 = load32(v2 + 12)
    store64(arg0 + 5200, 2461016260608)
    v14 = -1
    v2 = 0
    while True:  # block $label2
        if (v8 > 0):
            while True:  # $label1
                while True:  # block $label0
                    v3 = (v9 + (v2 << 2))
                    if load16u((v9 + (v2 << 2))):
                        v3 = (load32(arg0 + 5200) + 1)
                        store32(arg0 + 5200, (load32(arg0 + 5200) + 1))
                        store32(((arg0 + (v3 << 2)) + 2908), v2)
                        store8(((arg0 + v2) + 5208), 0)
                        v14 = v2
                        break
                    store16(v3 + 2, 0)
                    break
                v2 = (v2 + 1)
                if ((v2 + 1) != v8):
                    continue
                break
            v2 = load32(arg0 + 5200)
            if (load32(arg0 + 5200) > 1):
                break
        while True:  # $label3
            v2 = (v2 + 1)
            store32(arg0 + 5200, (v2 + 1))
            v3 = (v14 + 1)
            v7 = (v14 < 2)
            v2 = ((v14 + 1) if (v14 < 2) else 0)
            store32(((arg0 + (v2 << 2)) + 2908), ((v14 + 1) if (v14 < 2) else 0))
            v5 = (v2 << 2)
            store16((v9 + (v2 << 2)), 1)
            store8(((arg0 + v2) + 5208), 0)
            store32(arg0 + 5800, (load32(arg0 + 5800) - 1))
            if v4:
                store32(arg0 + 5804, (load32(arg0 + 5804) - load16u((v4 + v5) + 2)))
            v14 = (v3 if v7 else v14)
            v2 = load32(arg0 + 5200)
            if (load32(arg0 + 5200) < 2):
                continue
            break
        break
    store32(arg1 + 4, v14)
    v2 = ((v2 & 0xFFFFFFFF) >> 1)
    while True:  # $label8
        v7 = v2
        v6 = load32(((arg0 + (v2 << 2)) + 2908))
        while True:  # block $label4
            v3 = (v2 << 1)
            v5 = load32(arg0 + 5200)
            if ((v2 << 1) > load32(arg0 + 5200)):
                break
            v11 = ((arg0 + v6) + 5208)
            v12 = (v9 + (v6 << 2))
            v4 = v7
            while True:  # $label7
                while True:  # block $label5
                    if (v3 >= v5):
                        v2 = v3
                        break
                    v2 = (arg0 + 2908)
                    v5 = (v3 | 1)
                    v13 = load32(((arg0 + 2908) + ((v3 | 1) << 2)))
                    v15 = load16u((v9 + (load32(((arg0 + 2908) + ((v3 | 1) << 2))) << 2)))
                    v16 = load32((v2 + (v3 << 2)))
                    v2 = load16u((v9 + (load32((v2 + (v3 << 2))) << 2)))
                    if (u(load16u((v9 + (load32(((arg0 + 2908) + ((v3 | 1) << 2))) << 2)))) >= u(load16u((v9 + (load32((v2 + (v3 << 2))) << 2))))):
                        if (v2 != v15):
                            v2 = v3
                            break
                        v2 = v3
                        v3 = (arg0 + 5208)
                        if (u(load8u(((arg0 + 5208) + v13))) > u(load8u((v3 + v16)))):
                            break
                    v2 = v5
                    break
                v5 = load16u(v12)
                v3 = load32(((arg0 + (v2 << 2)) + 2908))
                v13 = load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2)))
                if (u(load16u(v12)) < u(load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2))))):
                    v2 = v4
                    break
                while True:  # block $label6
                    if (v5 != v13):
                        break
                    if (u(load8u(v11)) > u(load8u(((arg0 + v3) + 5208)))):
                        break
                    v2 = v4
                    break
                    break
                store32(((arg0 + (v4 << 2)) + 2908), v3)
                v4 = v2
                v3 = (v2 << 1)
                v5 = load32(arg0 + 5200)
                if ((v2 << 1) <= load32(arg0 + 5200)):
                    continue
                break
            break
        store32(((arg0 + (v2 << 2)) + 2908), v6)
        v2 = (v7 - 1)
        if (v7 > 1):
            continue
        break
    v3 = load32(arg0 + 5200)
    while True:  # $label17
        v7 = v8
        v5 = (v3 - 1)
        store32(arg0 + 5200, (v3 - 1))
        v12 = load32(arg0 + 2912)
        v11 = load32(((arg0 + (v3 << 2)) + 2908))
        store32(arg0 + 2912, load32(((arg0 + (v3 << 2)) + 2908)))
        v2 = 1
        while True:  # block $label9
            if (v3 < 3):
                break
            v6 = ((arg0 + v11) + 5208)
            v3 = 2
            v13 = (v9 + (v11 << 2))
            v4 = 1
            while True:  # $label12
                while True:  # block $label10
                    if (v3 >= v5):
                        v2 = v3
                        break
                    v2 = (arg0 + 2908)
                    v8 = (v3 | 1)
                    v5 = load32(((arg0 + 2908) + ((v3 | 1) << 2)))
                    v15 = load16u((v9 + (load32(((arg0 + 2908) + ((v3 | 1) << 2))) << 2)))
                    v16 = load32((v2 + (v3 << 2)))
                    v2 = load16u((v9 + (load32((v2 + (v3 << 2))) << 2)))
                    if (u(load16u((v9 + (load32(((arg0 + 2908) + ((v3 | 1) << 2))) << 2)))) >= u(load16u((v9 + (load32((v2 + (v3 << 2))) << 2))))):
                        if (v2 != v15):
                            v2 = v3
                            break
                        v2 = v3
                        v3 = (arg0 + 5208)
                        if (u(load8u(((arg0 + 5208) + v5))) > u(load8u((v3 + v16)))):
                            break
                    v2 = v8
                    break
                v8 = load16u(v13)
                v3 = load32(((arg0 + (v2 << 2)) + 2908))
                v5 = load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2)))
                if (u(load16u(v13)) < u(load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2))))):
                    v2 = v4
                    break
                while True:  # block $label11
                    if (v5 != v8):
                        break
                    if (u(load8u(v6)) > u(load8u(((arg0 + v3) + 5208)))):
                        break
                    v2 = v4
                    break
                    break
                store32(((arg0 + (v4 << 2)) + 2908), v3)
                v4 = v2
                v3 = (v2 << 1)
                v5 = load32(arg0 + 5200)
                if ((v2 << 1) <= load32(arg0 + 5200)):
                    continue
                break
            break
        v3 = 2
        v6 = (arg0 + 2908)
        store32(((arg0 + 2908) + (v2 << 2)), v11)
        v4 = (load32(arg0 + 5204) - 1)
        store32(arg0 + 5204, (load32(arg0 + 5204) - 1))
        v2 = load32(arg0 + 2912)
        store32((v6 + (v4 << 2)), v12)
        v4 = (load32(arg0 + 5204) - 1)
        store32(arg0 + 5204, (load32(arg0 + 5204) - 1))
        store32((v6 + (v4 << 2)), v2)
        v13 = (v9 + (v7 << 2))
        v4 = (v9 + (v2 << 2))
        v8 = (v9 + (v12 << 2))
        store16((v9 + (v7 << 2)), (load16u((v9 + (v2 << 2))) + load16u((v9 + (v12 << 2)))))
        v11 = (arg0 + 5208)
        v15 = ((arg0 + 5208) + v7)
        v5 = load8u((v11 + v12))
        v2 = load8u((v2 + v11))
        store8(((arg0 + 5208) + v7), ((load8u((v11 + v12)) if (u(v2) < u(v5)) else load8u((v2 + v11))) + 1))
        store16(v4 + 2, v7)
        store16(v8 + 2, v7)
        store32(arg0 + 2912, v7)
        v4 = 1
        v2 = 1
        while True:  # block $label13
            v5 = load32(arg0 + 5200)
            if (load32(arg0 + 5200) < 2):
                break
            while True:  # $label16
                while True:  # block $label14
                    if (v3 >= v5):
                        break
                    v8 = (v3 | 1)
                    v5 = load32((v6 + ((v3 | 1) << 2)))
                    v2 = load16u((v9 + (load32((v6 + ((v3 | 1) << 2))) << 2)))
                    v12 = load32((v6 + (v3 << 2)))
                    v16 = load16u((v9 + (load32((v6 + (v3 << 2))) << 2)))
                    if (u(load16u((v9 + (load32((v6 + ((v3 | 1) << 2))) << 2)))) >= u(load16u((v9 + (load32((v6 + (v3 << 2))) << 2))))):
                        if (v2 != v16):
                            break
                        if (u(load8u((v5 + v11))) > u(load8u((v11 + v12)))):
                            break
                    break
                v2 = v8
                v8 = load16u(v13)
                v3 = load32(((arg0 + (v2 << 2)) + 2908))
                v5 = load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2)))
                if (u(load16u(v13)) < u(load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2))))):
                    v2 = v4
                    break
                while True:  # block $label15
                    if (v5 != v8):
                        break
                    if (u(load8u(v15)) > u(load8u(((arg0 + v3) + 5208)))):
                        break
                    v2 = v4
                    break
                    break
                store32(((arg0 + (v4 << 2)) + 2908), v3)
                v4 = v2
                v3 = (v2 << 1)
                v5 = load32(arg0 + 5200)
                if ((v2 << 1) <= load32(arg0 + 5200)):
                    continue
                break
            break
        v8 = (v7 + 1)
        store32(((arg0 + (v2 << 2)) + 2908), v7)
        v3 = load32(arg0 + 5200)
        if (load32(arg0 + 5200) > 1):
            continue
        break
    v2 = (load32(arg0 + 5204) - 1)
    store32(arg0 + 5204, (load32(arg0 + 5204) - 1))
    v4 = (arg0 + 2908)
    store32(((arg0 + 2908) + (v2 << 2)), load32(arg0 + 2912))
    v5 = load32(arg1 + 4)
    v2 = load32(arg1 + 8)
    v3 = load32(load32(arg1 + 8) + 16)
    v11 = load32(v2 + 8)
    v16 = load32(v2 + 4)
    v12 = load32(v2)
    v7 = load32(arg1)
    v17 = (arg0 + 2900)
    store64((arg0 + 2900), 0)
    v18 = (arg0 + 2892)
    store64((arg0 + 2892), 0)
    v19 = (arg0 + 2884)
    store64((arg0 + 2884), 0)
    v20 = (arg0 + 2876)
    store64((arg0 + 2876), 0)
    v8 = 0
    store16((v7 + (load32((v4 + (load32(arg0 + 5204) << 2))) << 2)) + 2, 0)
    while True:  # block $label18
        arg1 = load32(arg0 + 5204)
        if (load32(arg0 + 5204) > 571):
            break
        v2 = (arg1 + 1)
        v4 = 0
        while True:  # $label20
            arg1 = load32(((arg0 + (v2 << 2)) + 2908))
            v21 = (load32(((arg0 + (v2 << 2)) + 2908)) << 2)
            v13 = (v7 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2))
            v6 = load16u((v7 + (load16u(v13 + 2) << 2)) + 2)
            v22 = (v3 <= v6)
            v15 = (v3 if (v3 <= v6) else (load16u((v7 + (load16u(v13 + 2) << 2)) + 2) + 1))
            store16((v7 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2)) + 2, (v3 if (v3 <= v6) else (load16u((v7 + (load16u(v13 + 2) << 2)) + 2) + 1)))
            while True:  # block $label19
                if (arg1 > v5):
                    break
                v6 = ((arg0 + (v15 << 1)) + 2876)
                store16(((arg0 + (v15 << 1)) + 2876), (load16u(v6) + 1))
                v6 = 0
                if (arg1 >= v11):
                    v6 = load32((v16 + ((arg1 - v11) << 2)))
                arg1 = load16u(v13)
                store32(arg0 + 5800, (load32(arg0 + 5800) + (load16u(v13) * (v6 + v15))))
                if (v12 == 0):
                    break
                store32(arg0 + 5804, (load32(arg0 + 5804) + ((v6 + load16u((v12 + v21) + 2)) * arg1)))
                break
            v4 = (v4 + v22)
            v2 = (v2 + 1)
            if ((v2 + 1) != 573):
                continue
            break
        if (v4 == 0):
            break
        v6 = ((arg0 + (v3 << 1)) + 2876)
        while True:  # $label22
            v2 = v3
            while True:  # $label21
                arg1 = v2
                v2 = (v2 - 1)
                v11 = ((arg0 + ((v2 - 1) << 1)) + 2876)
                v12 = load16u(((arg0 + ((v2 - 1) << 1)) + 2876))
                if (load16u(((arg0 + ((v2 - 1) << 1)) + 2876)) == 0):
                    continue
                break
            store16(v11, (v12 - 1))
            arg1 = ((arg0 + (arg1 << 1)) + 2876)
            store16(((arg0 + (arg1 << 1)) + 2876), (load16u(arg1) + 2))
            store16(v6, (load16u(v6) - 1))
            arg1 = (v4 > 2)
            v4 = (v4 - 2)
            if arg1:
                continue
            break
        if (v3 == 0):
            break
        v2 = 573
        while True:  # $label24
            v4 = load16u(((arg0 + (v3 << 1)) + 2876))
            if load16u(((arg0 + (v3 << 1)) + 2876)):
                while True:  # $label23
                    v2 = (v2 - 1)
                    arg1 = load32(((arg0 + ((v2 - 1) << 2)) + 2908))
                    if (load32(((arg0 + ((v2 - 1) << 2)) + 2908)) > v5):
                        continue
                    arg1 = (v7 + (arg1 << 2))
                    v6 = load16u((v7 + (arg1 << 2)) + 2)
                    if (load16u((v7 + (arg1 << 2)) + 2) != v3):
                        store32(arg0 + 5800, (load32(arg0 + 5800) + (load16u(arg1) * (v3 - v6))))
                        store16(arg1 + 2, v3)
                    v4 = (v4 - 1)
                    if (v4 - 1):
                        continue
                    break
            v3 = (v3 - 1)
            if (v3 - 1):
                continue
            break
        break
    arg1 = (load16u(v20) << 1)
    store16(v10 + 2, (load16u(v20) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2878))) << 1)
    store16(v10 + 4, ((arg1 + load16u((arg0 + 2878))) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2880))) << 1)
    store16(v10 + 6, ((arg1 + load16u((arg0 + 2880))) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2882))) << 1)
    store16(v10 + 8, ((arg1 + load16u((arg0 + 2882))) << 1))
    arg1 = ((arg1 + load16u(v19)) << 1)
    store16(v10 + 10, ((arg1 + load16u(v19)) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2886))) << 1)
    store16(v10 + 12, ((arg1 + load16u((arg0 + 2886))) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2888))) << 1)
    store16(v10 + 14, ((arg1 + load16u((arg0 + 2888))) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2890))) << 1)
    store16(v10 + 16, ((arg1 + load16u((arg0 + 2890))) << 1))
    arg1 = ((arg1 + load16u(v18)) << 1)
    store16(v10 + 18, ((arg1 + load16u(v18)) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2894))) << 1)
    store16(v10 + 20, ((arg1 + load16u((arg0 + 2894))) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2896))) << 1)
    store16(v10 + 22, ((arg1 + load16u((arg0 + 2896))) << 1))
    arg1 = ((arg1 + load16u((arg0 + 2898))) << 1)
    store16(v10 + 24, ((arg1 + load16u((arg0 + 2898))) << 1))
    arg1 = ((load16u(v17) + arg1) << 1)
    store16(v10 + 26, ((load16u(v17) + arg1) << 1))
    arg1 = ((load16u((arg0 + 2902)) + arg1) << 1)
    store16(v10 + 28, ((load16u((arg0 + 2902)) + arg1) << 1))
    store16(v10 + 30, ((arg1 + load16u((arg0 + 2904))) << 1))
    if (v14 >= 0):
        while True:  # $label28
            v7 = (v9 + (v8 << 2))
            arg0 = load16u((v9 + (v8 << 2)) + 2)
            if load16u((v9 + (v8 << 2)) + 2):
                arg1 = (v10 + (arg0 << 1))
                v2 = load16u(arg1)
                store16((v10 + (arg0 << 1)), (load16u(arg1) + 1))
                arg1 = (arg0 & 3)
                v3 = 0
                while True:  # block $label25
                    if (u(arg0) < u(4)):
                        arg0 = 0
                        break
                    v6 = (arg0 & 65532)
                    arg0 = 0
                    v4 = 0
                    while True:  # $label26
                        v5 = ((((v2 & 0xFFFFFFFF) >> 3) & 1) | (((((v2 & 0xFFFFFFFF) >> 2) & 1) | ((v2 & 2) | ((arg0 | (v2 & 1)) << 2))) << 1))
                        arg0 = (((((v2 & 0xFFFFFFFF) >> 3) & 1) | (((((v2 & 0xFFFFFFFF) >> 2) & 1) | ((v2 & 2) | ((arg0 | (v2 & 1)) << 2))) << 1)) << 1)
                        v2 = ((v2 & 0xFFFFFFFF) >> 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v6):
                            continue
                        break
                    break
                if arg1:
                    while True:  # $label27
                        v5 = (arg0 | (v2 & 1))
                        arg0 = ((arg0 | (v2 & 1)) << 1)
                        v2 = ((v2 & 0xFFFFFFFF) >> 1)
                        v3 = (v3 + 1)
                        if ((v3 + 1) != arg1):
                            continue
                        break
                store16(v7, v5)
            arg0 = (v8 != v14)
            v8 = (v8 + 1)
            if arg0:
                continue
            break

# ------------------------------------------------------------
# $func261
# ------------------------------------------------------------
def func261(arg0, arg1, arg2, arg3):
    v4 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    store32(v4 + 24, arg2)
    store32(v4 + 20, arg1)
    store32(v4 + 16, arg0)
    arg0 = load16u(arg3 + 110)
    store32(v4 + 56, 0)
    store64(v4 + 48, 4294967297)
    store64(v4 + 40, 4294967297)
    store64(v4 + 32, 4294967297)
    store32(v4 + 28, arg0)
    store32(v4 + 12, load32(arg3 + 28))
    G.global0 = (v4 - -64)

# ------------------------------------------------------------
# $func262
# ------------------------------------------------------------
def func262(arg0, arg1):
    # TODO: i64.reinterpret_f64 []
    # TODO: i64.reinterpret_f64 []
    if (((u((arg0 & 9223372036854775807)) < u(9218868437227405313)) & (u((arg1 & 9223372036854775807)) <= u(9218868437227405312))) == 0):
        return (arg0 + arg1)
    # TODO: i64.reinterpret_f64 []
    v7 = arg1
    v2 = i32(((arg1 & 0xFFFFFFFFFFFFFFFF) >> 32))
    v5 = i32(v7)
    if (((i32(((arg1 & 0xFFFFFFFFFFFFFFFF) >> 32)) - 1072693248) | i32(v7)) == 0):
        return func424(arg0)
    v6 = (((v2 & 0xFFFFFFFF) >> 30) & 2)
    # TODO: i64.reinterpret_f64 []
    v7 = arg0
    v3 = ((((v2 & 0xFFFFFFFF) >> 30) & 2) | i32(((arg0 & 0xFFFFFFFFFFFFFFFF) >> 63)))
    while True:  # block $label2
        v4 = (i32(((v7 & 0xFFFFFFFFFFFFFFFF) >> 32)) & 2147483647)
        if (((i32(((v7 & 0xFFFFFFFFFFFFFFFF) >> 32)) & 2147483647) | i32(v7)) == 0):
            while True:  # block $label1
                while True:  # block $label0
                    # br_table[(v3 - 2)]
                    break
                    break
                return 3.141592653589793
                break
            return -3.141592653589793
        v2 = (v2 & 2147483647)
        if (((v2 & 2147483647) | v5) == 0):
            # TODO: f64.copysign []
            return arg0
        while True:  # block $label3
            if (v2 == 2146435072):
                if (v4 != 2146435072):
                    break
                return load32(((v3 << 3) + 28800))
            if (((v4 != 2146435072) & (u((v2 + 67108864)) >= u(v4))) == 0):
                # TODO: f64.copysign []
                return arg0
            while True:  # block $label4
                if v6:
                    if (u((v4 + 67108864)) < u(v2)):
                        break
                break
            arg0 = func424(abs((arg0 / arg1)))
            while True:  # block $label7
                while True:  # block $label6
                    while True:  # block $label5
                        # br_table[v3]
                        break
                        break
                    return (-arg0)
                    break
                return (3.141592653589793 - (arg0 + -1.2246467991473532e-16))
                break
            return ((arg0 + -1.2246467991473532e-16) + -3.141592653589793)
            break
        arg0 = load32(((v3 << 3) + 28832))
        break
    return arg0

# ------------------------------------------------------------
# $func263
# ------------------------------------------------------------
def func263():
    v0 = load32(9688312)
    if load32(9688312):
        store32(9688312, (v0 - 1))
        return
    atomic_store(9688308, 0)
    if load32(9688316):
        func97(9688308)

# ------------------------------------------------------------
# $func264
# ------------------------------------------------------------
def func264():
    v0 = load32(G.global3 + 24)
    if (load32(G.global3 + 24) != load32(9688308)):
        # TODO: i32.atomic.rmw.cmpxchg []
        v1 = v0
        if v0:
            while True:  # $label0
                # TODO: i32.atomic.rmw.cmpxchg []
                v1 = v0
                if v0:
                    continue
                break
        return
    store32(9688312, (load32(9688312) + 1))

# ------------------------------------------------------------
# $func265
# ------------------------------------------------------------
def func265(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label2
        while True:  # block $label3
            while True:  # block $label1
                while True:  # block $label0
                    v3 = G.global5
                    if G.global5:
                        break
                    v4 = G.global3
                    if (load8u(G.global3 + 40) != 1):
                        break
                    if (load8u(v4 + 41) != 1):
                        break
                    break
                v5 = float((1 if v3 else 100))
                v7 = (a_f() + inf)
                v3 = G.global3
                while True:  # $label4
                    if load32(v3 + 36):
                        arg0 = 11
                        break
                    v6 = (v7 - a_f())
                    if ((v7 - a_f()) <= 0.0):
                        break
                    v4 = func131(arg0, arg1, (v5 if (v5 < v6) else v6))
                    if (func131(arg0, arg1, (v5 if (v5 < v6) else v6)) == -73):
                        continue
                    break
                break
                break
            break
        arg0 = (0 - func131(arg0, arg1, inf))
        arg0 = (((0 - func131(arg0, arg1, inf)) if ((arg0 & -17) == 11) else 0) if (arg0 != 73) else arg0)
        if ((((0 - func131(arg0, arg1, inf)) if ((arg0 & -17) == 11) else 0) if (arg0 != 73) else arg0) != 27):
            break
        arg0 = (27 if load32(9688304) else 0)
        break
    G.global0 = (arg2 + 16)
    return arg0

# ------------------------------------------------------------
# $func266
# ------------------------------------------------------------
def func266(arg0):
    if (load32(arg0 + 12) == load32(G.global3 + 24)):
        store32(arg0 + 12, 0)
    while True:  # $label0
        v3 = load32(arg0 + 4)
        v1 = load32(arg0)
        v2 = (v1 & 2147483647)
        v4 = (((v1 - 1) if ((v1 & 2147483647) != 1) else 0) if (v2 != 2147483647) else 0)
        # TODO: i32.atomic.rmw.cmpxchg []
        if ((((v1 - 1) if ((v1 & 2147483647) != 1) else 0) if (v2 != 2147483647) else 0) != v1):
            continue
        break
    while True:  # block $label1
        if v4:
            break
        if ((v3 == 0) & (v1 >= 0)):
            break
        func111(arg0, v2)
        break

# ------------------------------------------------------------
# $func267
# ------------------------------------------------------------
def func267(arg0):
    while True:  # block $label0
        while True:  # block $label1
            while True:  # $label3
                v2 = 6
                v3 = 10
                while True:  # block $label2
                    v1 = load32(arg0)
                    # br_table[((load32(arg0) & 2147483647) - 2147483646)]
                    break
                    break
                # TODO: i32.atomic.rmw.cmpxchg []
                if (v1 != (v1 + 1)):
                    continue
                break
            v3 = 0
            break
        v2 = v3
        break
    return v2

# ------------------------------------------------------------
# $func268
# ------------------------------------------------------------
def func268(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # block $label1
        while True:  # block $label0
            if (arg0 == 0):
                break
            if (arg2 == 0):
                break
            v6 = (arg1 >> 31)
            if (((arg1 ^ (arg1 >> 31)) - v6) < arg4):
                break
            v6 = (arg3 >> 31)
            if (((arg3 ^ (arg3 >> 31)) - v6) < arg4):
                break
            while True:  # block $label2
                if (arg5 <= 0):
                    break
                while True:  # block $label3
                    v8 = (arg5 & 3)
                    if ((arg5 & 3) == 0):
                        v6 = arg5
                        break
                    v6 = arg5
                    while True:  # $label4
                        # TODO: memory.copy []
                        arg2 = (arg2 + arg3)
                        arg0 = (arg0 + arg1)
                        v6 = (v6 - 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v8):
                            continue
                        break
                    break
                if (u(arg5) < u(4)):
                    break
                while True:  # $label5
                    # TODO: memory.copy []
                    arg2 = (arg2 + arg3)
                    arg0 = (arg0 + arg1)
                    # TODO: memory.copy []
                    arg2 = (arg2 + arg3)
                    arg0 = (arg0 + arg1)
                    # TODO: memory.copy []
                    arg2 = (arg2 + arg3)
                    arg0 = (arg0 + arg1)
                    # TODO: memory.copy []
                    arg2 = (arg2 + arg3)
                    arg0 = (arg0 + arg1)
                    arg5 = (v6 - 5)
                    v6 = (v6 - 4)
                    if (u(arg5) < u(-2)):
                        continue
                    break
                break
            return
            break
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func269
# ------------------------------------------------------------
def func269(arg0, arg1, arg2):
    while True:  # block $label1
        while True:  # block $label0
            if arg0:
                if (arg1 == 0):
                    break
                if (u(arg2) >= u(-8)):
                    break
                store64(arg0 + 20, 0)
                store32(arg0 + 12, arg2)
                store32(arg0 + 8, arg1)
                while True:  # block $label2
                    arg2 = (8 if (u(arg2) >= u(8)) else arg2)
                    if ((8 if (u(arg2) >= u(8)) else arg2) == 0):
                        break
                    v3 = load64(arg1)
                    if (arg2 == 1):
                        break
                    v3 = ((load64(arg1 + 1) << 8) | v3)
                    if (arg2 == 2):
                        break
                    v3 = ((load64(arg1 + 2) << 16) | v3)
                    if (arg2 == 3):
                        break
                    v3 = ((load64(arg1 + 3) << 24) | v3)
                    if (arg2 == 4):
                        break
                    v3 = ((load64(arg1 + 4) << 32) | v3)
                    if (arg2 == 5):
                        break
                    v3 = ((load64(arg1 + 5) << 40) | v3)
                    if (arg2 == 6):
                        break
                    v3 = ((load64(arg1 + 6) << 48) | v3)
                    if (arg2 == 7):
                        break
                    break
                v3 = ((load64(arg1 + 7) << 56) | v3)
                store32(arg0 + 16, arg2)
                store64(arg0, v3)
                return
            a_c()
            raise RuntimeError('unreachable')
            break
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')
    return 3628

# ------------------------------------------------------------
# $func270
# ------------------------------------------------------------
def func270(arg0, arg1, arg2):
    while True:  # block $label1
        while True:  # block $label0
            if arg0:
                if (arg1 == 0):
                    break
                if (arg2 < 0):
                    break
                store32(arg0 + 28, 0)
                store64(arg0, 0)
                store64(arg0 + 8, -34359738114)
                store32(arg0 + 16, arg1)
                v4 = (arg1 + arg2)
                store32(arg0 + 20, (arg1 + arg2))
                v4 = ((v4 - 7) if (u(arg2) > u(7)) else arg1)
                store32(arg0 + 24, ((v4 - 7) if (u(arg2) > u(7)) else arg1))
                if (u(arg1) < u(v4)):
                    v3 = load64(arg1)
                    store32(arg0 + 12, 48)
                    store32(arg0 + 16, (arg1 + 7))
                    store64(arg0, ((((((v3 << 56) | ((v3 & 65280) << 40)) | (((v3 & 16711680) << 24) | ((v3 & 4278190080) << 8))) | ((((v3 & 0xFFFFFFFFFFFFFFFF) >> 40) & 65280) | ((((v3 & 0xFFFFFFFFFFFFFFFF) >> 8) & 4278190080) | (((v3 & 0xFFFFFFFFFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFFFFFFFFFF) >> 8))
                    return
                store32(arg0 + 12, 0)
                if arg2:
                    store32(arg0 + 16, (arg1 + 1))
                    store64(arg0, load64(arg1))
                    return
                store32(arg0 + 28, 1)
                return
            a_c()
            raise RuntimeError('unreachable')
            break
        a_c()
        raise RuntimeError('unreachable')
        break
    a_c()
    raise RuntimeError('unreachable')