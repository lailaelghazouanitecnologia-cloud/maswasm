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
# $func298
# ------------------------------------------------------------
def func298(arg0, arg1, arg2, arg3):
    v24 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v24 + 12, arg3)
    v29 = arg0
    v16 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v26 = load32(v24 + 12)
    while True:  # block $label0
        v33 = arg1
        v22 = load32(arg1)
        if (load32(arg1) == 0):
            v22 = 1
            v29 = (v16 + 7)
            break
        store32(v33, 0)
        break
    store32(v16 + 48, 0)
    store64(v16 + 40, 0)
    store32(v16 + 12, 0)
    store32(v16 + 8, arg2)
    while True:  # block $label6
        while True:  # block $label2
            arg1 = (v16 + 8)
            while True:  # block $label1
                if (load8u(7784) != 49):
                    break
                if (arg1 == 0):
                    break
                store32(arg1 + 24, 0)
                arg0 = load32(arg1 + 32)
                if (load32(arg1 + 32) == 0):
                    store32(arg1 + 40, 0)
                    store32(arg1 + 32, 417)
                    arg0 = 417
                if (load32(arg1 + 36) == 0):
                    store32(arg1 + 36, 418)
                # call_indirect[arg0]
                arg3 = indirect_call(arg0)
                if (indirect_call(arg0) == 0):
                    break
                store32(arg1 + 28, arg3)
                store32(arg3 + 56, 0)
                store32(arg3, arg1)
                store32(arg3 + 4, 16180)
                arg0 = -2
                while True:  # block $label3
                    if (arg1 == 0):
                        break
                    if (load32(arg1 + 32) == 0):
                        break
                    v12 = load32(arg1 + 36)
                    if (load32(arg1 + 36) == 0):
                        break
                    arg2 = load32(arg1 + 28)
                    if (load32(arg1 + 28) == 0):
                        break
                    if (load32(arg2) != arg1):
                        break
                    if (u((load32(arg2 + 4) - 16180)) > u(31)):
                        break
                    while True:  # block $label5
                        while True:  # block $label4
                            v5 = load32(arg2 + 56)
                            if load32(arg2 + 56):
                                if (load32(arg2 + 40) != 15):
                                    break
                            store32(arg2 + 40, 15)
                            store32(arg2 + 12, 5)
                            break
                            break
                        # call_indirect[v12]
                        store32(arg2 + 56, 0)
                        v12 = load32(arg1 + 32)
                        store32(arg2 + 40, 15)
                        store32(arg2 + 12, 5)
                        if (v12 == 0):
                            break
                        break
                    if (load32(arg1 + 36) == 0):
                        break
                    arg2 = load32(arg1 + 28)
                    if (load32(arg1 + 28) == 0):
                        break
                    if (load32(arg2) != arg1):
                        break
                    if (u((load32(arg2 + 4) - 16180)) > u(31)):
                        break
                    arg0 = 0
                    store32(arg2 + 52, 0)
                    store64(arg2 + 44, 0)
                    store32(arg2 + 32, 0)
                    store32(arg1 + 8, 0)
                    store64(arg1 + 20, 0)
                    v12 = load32(arg2 + 12)
                    if load32(arg2 + 12):
                        store32(arg1 + 48, (v12 & 1))
                    store64(arg2 + 60, 0)
                    store32(arg2 + 36, 0)
                    store32(arg2 + 24, 32768)
                    store64(arg2 + 16, -4294967296)
                    store64(arg2 + 4, 16180)
                    store64(arg2 + 7108, -4294967295)
                    v12 = (arg2 + 1332)
                    store32(arg2 + 112, (arg2 + 1332))
                    store32(arg2 + 84, v12)
                    store32(arg2 + 80, v12)
                    break
                if (arg0 == 0):
                    break
                # call_indirect[load32(arg1 + 36)]
                store32(arg1 + 28, 0)
                break
            break
        if arg0:
            break
        store32(v16 + 24, 0)
        store32(v16 + 20, v29)
        arg0 = 0
        while True:  # $label185
            if (arg0 == 0):
                store32(v16 + 24, v22)
                v22 = 0
            if (load32(v16 + 12) == 0):
                store32(v16 + 12, v26)
                v26 = 0
            v12 = 0
            v20 = (G.global0 - 16)
            G.global0 = (G.global0 - 16)
            v23 = -2
            while True:  # block $label7
                v10 = (v16 + 8)
                if ((v16 + 8) == 0):
                    break
                if (load32(v10 + 32) == 0):
                    break
                if (load32(v10 + 36) == 0):
                    break
                v4 = load32(v10 + 28)
                if (load32(v10 + 28) == 0):
                    break
                if (load32(v4) != v10):
                    break
                v5 = load32(v4 + 4)
                if (u((load32(v4 + 4) - 16180)) > u(31)):
                    break
                v14 = load32(v10 + 12)
                if (load32(v10 + 12) == 0):
                    break
                arg0 = load32(v10)
                if (load32(v10) == 0):
                    if load32(v10 + 4):
                        break
                if (v5 == 16191):
                    store32(v4 + 4, 16192)
                    v5 = 16192
                v39 = (v4 + 92)
                v30 = (v4 + 756)
                v31 = (v4 + 116)
                v34 = (v4 + 88)
                v32 = (v4 + 112)
                v27 = (v4 + 1332)
                arg2 = load32(v4 + 64)
                v35 = load32(v10 + 4)
                arg3 = load32(v10 + 4)
                v6 = load32(v4 + 60)
                v13 = load32(v10 + 16)
                v18 = load32(v10 + 16)
                while True:  # block $label37
                    while True:  # block $label36
                        while True:  # block $label177
                            while True:  # block $label174
                                while True:  # block $label43
                                    while True:  # $label52
                                        arg1 = -3
                                        v8 = 1
                                        while True:  # block $label41
                                            while True:  # block $label35
                                                while True:  # block $label74
                                                    while True:  # block $label163
                                                        while True:  # block $label16
                                                            while True:  # block $label15
                                                                while True:  # block $label14
                                                                    while True:  # block $label13
                                                                        while True:  # block $label65
                                                                            while True:  # block $label62
                                                                                while True:  # block $label94
                                                                                    while True:  # block $label83
                                                                                        while True:  # block $label159
                                                                                            while True:  # block $label157
                                                                                                while True:  # block $label100
                                                                                                    while True:  # block $label133
                                                                                                        while True:  # block $label137
                                                                                                            while True:  # block $label140
                                                                                                                while True:  # block $label143
                                                                                                                    while True:  # block $label147
                                                                                                                        while True:  # block $label151
                                                                                                                            while True:  # block $label88
                                                                                                                                while True:  # block $label153
                                                                                                                                    while True:  # block $label77
                                                                                                                                        while True:  # block $label31
                                                                                                                                            while True:  # block $label38
                                                                                                                                                while True:  # block $label29
                                                                                                                                                    while True:  # block $label39
                                                                                                                                                        while True:  # block $label27
                                                                                                                                                            while True:  # block $label26
                                                                                                                                                                while True:  # block $label40
                                                                                                                                                                    while True:  # block $label76
                                                                                                                                                                        while True:  # block $label75
                                                                                                                                                                            while True:  # block $label78
                                                                                                                                                                                while True:  # block $label82
                                                                                                                                                                                    while True:  # block $label49
                                                                                                                                                                                        while True:  # block $label33
                                                                                                                                                                                            while True:  # block $label32
                                                                                                                                                                                                while True:  # block $label24
                                                                                                                                                                                                    while True:  # block $label42
                                                                                                                                                                                                        while True:  # block $label44
                                                                                                                                                                                                            while True:  # block $label22
                                                                                                                                                                                                                while True:  # block $label21
                                                                                                                                                                                                                    while True:  # block $label20
                                                                                                                                                                                                                        while True:  # block $label19
                                                                                                                                                                                                                            while True:  # block $label18
                                                                                                                                                                                                                                while True:  # block $label45
                                                                                                                                                                                                                                    while True:  # block $label46
                                                                                                                                                                                                                                        while True:  # block $label63
                                                                                                                                                                                                                                            while True:  # block $label61
                                                                                                                                                                                                                                                while True:  # block $label12
                                                                                                                                                                                                                                                    while True:  # block $label59
                                                                                                                                                                                                                                                        while True:  # block $label58
                                                                                                                                                                                                                                                            while True:  # block $label11
                                                                                                                                                                                                                                                                while True:  # block $label56
                                                                                                                                                                                                                                                                    while True:  # block $label55
                                                                                                                                                                                                                                                                        while True:  # block $label10
                                                                                                                                                                                                                                                                            while True:  # block $label47
                                                                                                                                                                                                                                                                                while True:  # block $label48
                                                                                                                                                                                                                                                                                    while True:  # block $label8
                                                                                                                                                                                                                                                                                        while True:  # block $label9
                                                                                                                                                                                                                                                                                            while True:  # block $label17
                                                                                                                                                                                                                                                                                                while True:  # block $label23
                                                                                                                                                                                                                                                                                                    while True:  # block $label34
                                                                                                                                                                                                                                                                                                        while True:  # block $label25
                                                                                                                                                                                                                                                                                                            while True:  # block $label28
                                                                                                                                                                                                                                                                                                                while True:  # block $label30
                                                                                                                                                                                                                                                                                                                    # br_table[(v5 - 16180)]
                                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                                v9 = load32(v4 + 76)
                                                                                                                                                                                                                                                                                                                arg1 = arg0
                                                                                                                                                                                                                                                                                                                v5 = arg3
                                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                                            v8 = load32(v4 + 76)
                                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                                        v5 = load32(v4 + 108)
                                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                                    v5 = load32(v4 + 12)
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                if (u(arg2) >= u(14)):
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                if (arg3 == 0):
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                arg1 = (arg2 + 8)
                                                                                                                                                                                                                                                                                                v5 = (arg0 + 1)
                                                                                                                                                                                                                                                                                                v8 = (arg3 - 1)
                                                                                                                                                                                                                                                                                                v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                                                if (u(arg2) <= u(5)):
                                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                                arg0 = v5
                                                                                                                                                                                                                                                                                                arg3 = v8
                                                                                                                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            if (u(arg2) >= u(32)):
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            if (arg3 == 0):
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            arg1 = (arg0 + 1)
                                                                                                                                                                                                                                                                                            v5 = (arg3 - 1)
                                                                                                                                                                                                                                                                                            v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                                            if (u(arg2) <= u(23)):
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                            arg0 = arg1
                                                                                                                                                                                                                                                                                            arg3 = v5
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if (u(arg2) >= u(16)):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if (arg3 == 0):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        arg1 = (arg2 + 8)
                                                                                                                                                                                                                                                                                        v5 = (arg0 + 1)
                                                                                                                                                                                                                                                                                        v8 = (arg3 - 1)
                                                                                                                                                                                                                                                                                        v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                                        if (u(arg2) <= u(7)):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        arg0 = v5
                                                                                                                                                                                                                                                                                        arg3 = v8
                                                                                                                                                                                                                                                                                        arg2 = arg1
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                    v7 = load32(v4 + 12)
                                                                                                                                                                                                                                                                                    if (load32(v4 + 12) == 0):
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                    while True:  # block $label50
                                                                                                                                                                                                                                                                                        if (u(arg2) >= u(16)):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if (arg3 == 0):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        arg1 = (arg2 + 8)
                                                                                                                                                                                                                                                                                        v5 = (arg0 + 1)
                                                                                                                                                                                                                                                                                        v8 = (arg3 - 1)
                                                                                                                                                                                                                                                                                        v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                                        if (u(arg2) > u(7)):
                                                                                                                                                                                                                                                                                            arg0 = v5
                                                                                                                                                                                                                                                                                            arg3 = v8
                                                                                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if (v8 == 0):
                                                                                                                                                                                                                                                                                            arg0 = v5
                                                                                                                                                                                                                                                                                            arg3 = 0
                                                                                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                                                                                            arg1 = v12
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        arg2 = (arg2 + 16)
                                                                                                                                                                                                                                                                                        arg3 = (arg3 - 2)
                                                                                                                                                                                                                                                                                        v6 = ((load8u(arg0 + 1) << arg1) + v6)
                                                                                                                                                                                                                                                                                        arg0 = (arg0 + 2)
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                    while True:  # block $label51
                                                                                                                                                                                                                                                                                        if ((v7 & 2) == 0):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if (v6 != 35615):
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                        if (load32(v4 + 40) == 0):
                                                                                                                                                                                                                                                                                            store32(v4 + 40, 15)
                                                                                                                                                                                                                                                                                        v6 = 0
                                                                                                                                                                                                                                                                                        arg1 = func43(0, 0, 0)
                                                                                                                                                                                                                                                                                        store32(v4 + 28, func43(0, 0, 0))
                                                                                                                                                                                                                                                                                        store16(v20 + 12, 35615)
                                                                                                                                                                                                                                                                                        arg1 = func43(arg1, (v20 + 12), 2)
                                                                                                                                                                                                                                                                                        store32(v4 + 4, 16181)
                                                                                                                                                                                                                                                                                        store32(v4 + 28, arg1)
                                                                                                                                                                                                                                                                                        arg2 = 0
                                                                                                                                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                                                                                                                                        continue
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                    arg1 = load32(v4 + 36)
                                                                                                                                                                                                                                                                                    if load32(v4 + 36):
                                                                                                                                                                                                                                                                                        store32(arg1 + 48, -1)
                                                                                                                                                                                                                                                                                    while True:  # block $label53
                                                                                                                                                                                                                                                                                        if (v7 & 1):
                                                                                                                                                                                                                                                                                            if (((((v6 << 8) & 65280) + ((v6 & 0xFFFFFFFF) >> 8)) % 31) == 0):
                                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                                        store32(v10 + 24, 4091)
                                                                                                                                                                                                                                                                                        store32(v4 + 4, 16209)
                                                                                                                                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                                                                                                                                        continue
                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                    if ((v6 & 15) != 8):
                                                                                                                                                                                                                                                                                        store32(v10 + 24, 4966)
                                                                                                                                                                                                                                                                                        store32(v4 + 4, 16209)
                                                                                                                                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                                                                                                                                        continue
                                                                                                                                                                                                                                                                                    arg1 = ((v6 & 0xFFFFFFFF) >> 4)
                                                                                                                                                                                                                                                                                    v8 = (((v6 & 0xFFFFFFFF) >> 4) & 15)
                                                                                                                                                                                                                                                                                    v5 = ((((v6 & 0xFFFFFFFF) >> 4) & 15) + 8)
                                                                                                                                                                                                                                                                                    v7 = load32(v4 + 40)
                                                                                                                                                                                                                                                                                    if load32(v4 + 40):
                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                        store32(v4 + 40, v5)
                                                                                                                                                                                                                                                                                    if ((v7 & (u(v5) >= u(v5))) == 0):
                                                                                                                                                                                                                                                                                        arg2 = (arg2 - 4)
                                                                                                                                                                                                                                                                                        store32(v10 + 24, 4674)
                                                                                                                                                                                                                                                                                        store32(v4 + 4, 16209)
                                                                                                                                                                                                                                                                                        v6 = arg1
                                                                                                                                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                                                                                                                                        continue
                                                                                                                                                                                                                                                                                    arg2 = 0
                                                                                                                                                                                                                                                                                    store32(v4 + 20, 0)
                                                                                                                                                                                                                                                                                    store32(v4 + 24, (256 << v8))
                                                                                                                                                                                                                                                                                    arg1 = func89(0, 0, 0)
                                                                                                                                                                                                                                                                                    store32(v4 + 28, func89(0, 0, 0))
                                                                                                                                                                                                                                                                                    store32(v10 + 48, arg1)
                                                                                                                                                                                                                                                                                    store32(v4 + 4, (16189 if (v6 & 8192) else 16191))
                                                                                                                                                                                                                                                                                    v6 = 0
                                                                                                                                                                                                                                                                                    v5 = load32(v4 + 4)
                                                                                                                                                                                                                                                                                    continue
                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                if (v8 == 0):
                                                                                                                                                                                                                                                                                    arg0 = v5
                                                                                                                                                                                                                                                                                    arg3 = 0
                                                                                                                                                                                                                                                                                    arg2 = arg1
                                                                                                                                                                                                                                                                                    arg1 = v12
                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                arg2 = (arg2 + 16)
                                                                                                                                                                                                                                                                                arg3 = (arg3 - 2)
                                                                                                                                                                                                                                                                                v6 = ((load8u(arg0 + 1) << arg1) + v6)
                                                                                                                                                                                                                                                                                arg0 = (arg0 + 2)
                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                            store32(v4 + 20, v6)
                                                                                                                                                                                                                                                                            if ((v6 & 255) != 8):
                                                                                                                                                                                                                                                                                store32(v10 + 24, 4966)
                                                                                                                                                                                                                                                                                store32(v4 + 4, 16209)
                                                                                                                                                                                                                                                                                v5 = load32(v4 + 4)
                                                                                                                                                                                                                                                                                continue
                                                                                                                                                                                                                                                                            if (v6 & 57344):
                                                                                                                                                                                                                                                                                store32(v10 + 24, 2847)
                                                                                                                                                                                                                                                                                store32(v4 + 4, 16209)
                                                                                                                                                                                                                                                                                v5 = load32(v4 + 4)
                                                                                                                                                                                                                                                                                continue
                                                                                                                                                                                                                                                                            arg1 = load32(v4 + 36)
                                                                                                                                                                                                                                                                            if load32(v4 + 36):
                                                                                                                                                                                                                                                                                store32(arg1, (((v6 & 0xFFFFFFFF) >> 8) & 1))
                                                                                                                                                                                                                                                                            while True:  # block $label54
                                                                                                                                                                                                                                                                                if ((v6 & 512) == 0):
                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                if ((load8u(v4 + 12) & 4) == 0):
                                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                                store16(v20 + 12, v6)
                                                                                                                                                                                                                                                                                store32(v4 + 28, func43(load32(v4 + 28), (v20 + 12), 2))
                                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                            store32(v4 + 4, 16182)
                                                                                                                                                                                                                                                                            arg2 = 0
                                                                                                                                                                                                                                                                            v6 = 0
                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                        if (u(arg2) > u(31)):
                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    if (arg3 == 0):
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg1 = (arg0 + 1)
                                                                                                                                                                                                                                                                    v5 = (arg3 - 1)
                                                                                                                                                                                                                                                                    v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                                    if (u(arg2) > u(23)):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    v8 = (arg2 + 8)
                                                                                                                                                                                                                                                                    if (v5 == 0):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                                                        arg2 = v8
                                                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg1 = (arg0 + 2)
                                                                                                                                                                                                                                                                    v5 = (arg3 - 2)
                                                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 1) << v8) + v6)
                                                                                                                                                                                                                                                                    if (u(arg2) > u(15)):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    v8 = (arg2 + 16)
                                                                                                                                                                                                                                                                    if (v5 == 0):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                                                        arg2 = v8
                                                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg1 = (arg0 + 3)
                                                                                                                                                                                                                                                                    v5 = (arg3 - 3)
                                                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 2) << v8) + v6)
                                                                                                                                                                                                                                                                    if (u(arg2) > u(7)):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg2 = (arg2 + 24)
                                                                                                                                                                                                                                                                    if (v5 == 0):
                                                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    arg3 = (arg3 - 4)
                                                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 3) << arg2) + v6)
                                                                                                                                                                                                                                                                    arg0 = (arg0 + 4)
                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                arg1 = load32(v4 + 36)
                                                                                                                                                                                                                                                                if load32(v4 + 36):
                                                                                                                                                                                                                                                                    store32(arg1 + 4, v6)
                                                                                                                                                                                                                                                                while True:  # block $label57
                                                                                                                                                                                                                                                                    if ((load8u(v4 + 21) & 2) == 0):
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    if ((load8u(v4 + 12) & 4) == 0):
                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                    store32(v20 + 12, v6)
                                                                                                                                                                                                                                                                    store32(v4 + 28, func43(load32(v4 + 28), (v20 + 12), 4))
                                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                                store32(v4 + 4, 16183)
                                                                                                                                                                                                                                                                arg2 = 0
                                                                                                                                                                                                                                                                v6 = 0
                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                            if (u(arg2) > u(15)):
                                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        if (arg3 == 0):
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        arg1 = (arg0 + 1)
                                                                                                                                                                                                                                                        v5 = (arg3 - 1)
                                                                                                                                                                                                                                                        v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                                                        if (u(arg2) > u(7)):
                                                                                                                                                                                                                                                            arg0 = arg1
                                                                                                                                                                                                                                                            arg3 = v5
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        arg2 = (arg2 + 8)
                                                                                                                                                                                                                                                        if (v5 == 0):
                                                                                                                                                                                                                                                            arg0 = arg1
                                                                                                                                                                                                                                                            arg3 = 0
                                                                                                                                                                                                                                                            arg1 = v12
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        arg3 = (arg3 - 2)
                                                                                                                                                                                                                                                        v6 = ((load8u(arg0 + 1) << arg2) + v6)
                                                                                                                                                                                                                                                        arg0 = (arg0 + 2)
                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                    arg1 = load32(v4 + 36)
                                                                                                                                                                                                                                                    if load32(v4 + 36):
                                                                                                                                                                                                                                                        store32(arg1 + 12, ((v6 & 0xFFFFFFFF) >> 8))
                                                                                                                                                                                                                                                        store32(arg1 + 8, (v6 & 255))
                                                                                                                                                                                                                                                    while True:  # block $label60
                                                                                                                                                                                                                                                        if ((load8u(v4 + 21) & 2) == 0):
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        if ((load8u(v4 + 12) & 4) == 0):
                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                        store16(v20 + 12, v6)
                                                                                                                                                                                                                                                        store32(v4 + 28, func43(load32(v4 + 28), (v20 + 12), 2))
                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                    store32(v4 + 4, 16184)
                                                                                                                                                                                                                                                    v5 = 0
                                                                                                                                                                                                                                                    arg2 = 0
                                                                                                                                                                                                                                                    v6 = 0
                                                                                                                                                                                                                                                    arg1 = load32(v4 + 20)
                                                                                                                                                                                                                                                    if (load32(v4 + 20) & 1024):
                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                arg1 = load32(v4 + 20)
                                                                                                                                                                                                                                                if ((load32(v4 + 20) & 1024) == 0):
                                                                                                                                                                                                                                                    v5 = arg2
                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                v5 = v6
                                                                                                                                                                                                                                                if (u(arg2) > u(15)):
                                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            if (arg3 == 0):
                                                                                                                                                                                                                                                arg3 = 0
                                                                                                                                                                                                                                                v6 = v5
                                                                                                                                                                                                                                                arg1 = v12
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            v8 = (arg0 + 1)
                                                                                                                                                                                                                                            v7 = (arg3 - 1)
                                                                                                                                                                                                                                            v6 = ((load8u(arg0) << arg2) + v5)
                                                                                                                                                                                                                                            if (u(arg2) > u(7)):
                                                                                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                                                                                arg3 = v7
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            arg2 = (arg2 + 8)
                                                                                                                                                                                                                                            if (v7 == 0):
                                                                                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                                                                                arg3 = 0
                                                                                                                                                                                                                                                arg1 = v12
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            arg3 = (arg3 - 2)
                                                                                                                                                                                                                                            v6 = ((load8u(arg0 + 1) << arg2) + v6)
                                                                                                                                                                                                                                            arg0 = (arg0 + 2)
                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                        store32(v4 + 68, v6)
                                                                                                                                                                                                                                        arg2 = load32(v4 + 36)
                                                                                                                                                                                                                                        if load32(v4 + 36):
                                                                                                                                                                                                                                            store32(arg2 + 20, v6)
                                                                                                                                                                                                                                        arg2 = 0
                                                                                                                                                                                                                                        while True:  # block $label64
                                                                                                                                                                                                                                            if ((arg1 & 512) == 0):
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            if ((load8u(v4 + 12) & 4) == 0):
                                                                                                                                                                                                                                                break
                                                                                                                                                                                                                                            store16(v20 + 12, v6)
                                                                                                                                                                                                                                            store32(v4 + 28, func43(load32(v4 + 28), (v20 + 12), 2))
                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                        v6 = 0
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    v8 = (arg2 + 8)
                                                                                                                                                                                                                                    if (v5 == 0):
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                        arg2 = v8
                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    arg1 = (arg0 + 2)
                                                                                                                                                                                                                                    v5 = (arg3 - 2)
                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 1) << v8) + v6)
                                                                                                                                                                                                                                    if (u(arg2) > u(15)):
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    v8 = (arg2 + 16)
                                                                                                                                                                                                                                    if (v5 == 0):
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                        arg2 = v8
                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    arg1 = (arg0 + 3)
                                                                                                                                                                                                                                    v5 = (arg3 - 3)
                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 2) << v8) + v6)
                                                                                                                                                                                                                                    if (u(arg2) > u(7)):
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = v5
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    arg2 = (arg2 + 24)
                                                                                                                                                                                                                                    if (v5 == 0):
                                                                                                                                                                                                                                        arg0 = arg1
                                                                                                                                                                                                                                        arg3 = 0
                                                                                                                                                                                                                                        arg1 = v12
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    arg3 = (arg3 - 4)
                                                                                                                                                                                                                                    v6 = ((load8u(arg0 + 3) << arg2) + v6)
                                                                                                                                                                                                                                    arg0 = (arg0 + 4)
                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                arg1 = (((v6 << 24) | ((v6 & 65280) << 8)) | ((((v6 & 0xFFFFFFFF) >> 8) & 65280) | ((v6 & 0xFFFFFFFF) >> 24)))
                                                                                                                                                                                                                                store32(v4 + 28, (((v6 << 24) | ((v6 & 65280) << 8)) | ((((v6 & 0xFFFFFFFF) >> 8) & 65280) | ((v6 & 0xFFFFFFFF) >> 24))))
                                                                                                                                                                                                                                store32(v10 + 48, arg1)
                                                                                                                                                                                                                                store32(v4 + 4, 16190)
                                                                                                                                                                                                                                v6 = 0
                                                                                                                                                                                                                                arg2 = 0
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                            if (load32(v4 + 16) == 0):
                                                                                                                                                                                                                                store32(v10 + 16, v13)
                                                                                                                                                                                                                                store32(v10 + 12, v14)
                                                                                                                                                                                                                                store32(v10 + 4, arg3)
                                                                                                                                                                                                                                store32(v10, arg0)
                                                                                                                                                                                                                                store32(v4 + 64, arg2)
                                                                                                                                                                                                                                store32(v4 + 60, v6)
                                                                                                                                                                                                                                v23 = 2
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                            arg1 = func89(0, 0, 0)
                                                                                                                                                                                                                            store32(v4 + 28, func89(0, 0, 0))
                                                                                                                                                                                                                            store32(v10 + 48, arg1)
                                                                                                                                                                                                                            store32(v4 + 4, 16191)
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        while True:  # block $label67
                                                                                                                                                                                                                            while True:  # block $label66
                                                                                                                                                                                                                                if (load32(v4 + 8) == 0):
                                                                                                                                                                                                                                    if (u(arg2) < u(3)):
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                store32(v4 + 4, 16206)
                                                                                                                                                                                                                                v6 = ((v6 & 0xFFFFFFFF) >> (arg2 & 7))
                                                                                                                                                                                                                                arg2 = (arg2 & -8)
                                                                                                                                                                                                                                v5 = load32(v4 + 4)
                                                                                                                                                                                                                                continue
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                            if (arg3 == 0):
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                            arg3 = (arg3 - 1)
                                                                                                                                                                                                                            v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                            arg0 = (arg0 + 1)
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        arg1 = (arg2 + 8)
                                                                                                                                                                                                                        store32(v4 + 8, (v6 & 1))
                                                                                                                                                                                                                        v5 = 16193
                                                                                                                                                                                                                        while True:  # block $label72
                                                                                                                                                                                                                            while True:  # block $label71
                                                                                                                                                                                                                                while True:  # block $label70
                                                                                                                                                                                                                                    while True:  # block $label69
                                                                                                                                                                                                                                        while True:  # block $label68
                                                                                                                                                                                                                                            # br_table[((((v6 & 0xFFFFFFFF) >> 1) & 3) - 1)]
                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                        store32(v4 + 80, 26512)
                                                                                                                                                                                                                                        store64(v4 + 88, 21474836489)
                                                                                                                                                                                                                                        store32(v4 + 84, 28560)
                                                                                                                                                                                                                                        store32(v4 + 4, 16199)
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                    v5 = 16196
                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                    break
                                                                                                                                                                                                                                store32(v10 + 24, 4719)
                                                                                                                                                                                                                                v5 = 16209
                                                                                                                                                                                                                                break
                                                                                                                                                                                                                            store32(v4 + 4, v5)
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        arg2 = (arg1 - 3)
                                                                                                                                                                                                                        v6 = ((v6 & 0xFFFFFFFF) >> 3)
                                                                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                                                                        continue
                                                                                                                                                                                                                        break
                                                                                                                                                                                                                    v6 = ((v6 & 0xFFFFFFFF) >> (arg2 & 7))
                                                                                                                                                                                                                    while True:  # block $label73
                                                                                                                                                                                                                        arg2 = (arg2 & -8)
                                                                                                                                                                                                                        if (u((arg2 & -8)) > u(31)):
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        if (arg3 == 0):
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        arg1 = (arg2 + 8)
                                                                                                                                                                                                                        v5 = (arg0 + 1)
                                                                                                                                                                                                                        v8 = (arg3 - 1)
                                                                                                                                                                                                                        v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                                                        if (u(arg2) > u(23)):
                                                                                                                                                                                                                            arg0 = v5
                                                                                                                                                                                                                            arg3 = v8
                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        if (v8 == 0):
                                                                                                                                                                                                                            arg0 = v5
                                                                                                                                                                                                                            arg3 = 0
                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                            arg1 = v12
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        v5 = (arg2 + 16)
                                                                                                                                                                                                                        v8 = (arg0 + 2)
                                                                                                                                                                                                                        v7 = (arg3 - 2)
                                                                                                                                                                                                                        v6 = ((load8u(arg0 + 1) << arg1) + v6)
                                                                                                                                                                                                                        if (u(arg2) > u(15)):
                                                                                                                                                                                                                            arg0 = v8
                                                                                                                                                                                                                            arg3 = v7
                                                                                                                                                                                                                            arg2 = v5
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        if (v7 == 0):
                                                                                                                                                                                                                            arg0 = v8
                                                                                                                                                                                                                            arg3 = 0
                                                                                                                                                                                                                            arg2 = v5
                                                                                                                                                                                                                            arg1 = v12
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        arg1 = (arg2 + 24)
                                                                                                                                                                                                                        v8 = (arg0 + 3)
                                                                                                                                                                                                                        v7 = (arg3 - 3)
                                                                                                                                                                                                                        v6 = ((load8u(arg0 + 2) << v5) + v6)
                                                                                                                                                                                                                        if arg2:
                                                                                                                                                                                                                            arg0 = v8
                                                                                                                                                                                                                            arg3 = v7
                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        if (v7 == 0):
                                                                                                                                                                                                                            arg0 = v8
                                                                                                                                                                                                                            arg3 = 0
                                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                                            arg1 = v12
                                                                                                                                                                                                                            break
                                                                                                                                                                                                                        arg2 = (arg2 + 32)
                                                                                                                                                                                                                        arg3 = (arg3 - 4)
                                                                                                                                                                                                                        v6 = ((load8u(arg0 + 3) << arg1) + v6)
                                                                                                                                                                                                                        arg0 = (arg0 + 4)
                                                                                                                                                                                                                        break
                                                                                                                                                                                                                    arg1 = (v6 & 65535)
                                                                                                                                                                                                                    if ((v6 & 65535) != (((v6 ^ -1) & 0xFFFFFFFF) >> 16)):
                                                                                                                                                                                                                        store32(v10 + 24, 3310)
                                                                                                                                                                                                                        store32(v4 + 4, 16209)
                                                                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                                                                        continue
                                                                                                                                                                                                                    store32(v4 + 4, 16194)
                                                                                                                                                                                                                    store32(v4 + 68, arg1)
                                                                                                                                                                                                                    v6 = 0
                                                                                                                                                                                                                    arg2 = 0
                                                                                                                                                                                                                    break
                                                                                                                                                                                                                store32(v4 + 4, 16195)
                                                                                                                                                                                                                break
                                                                                                                                                                                                            arg1 = load32(v4 + 68)
                                                                                                                                                                                                            if load32(v4 + 68):
                                                                                                                                                                                                                arg1 = (arg1 if (u(arg1) < u(arg3)) else arg3)
                                                                                                                                                                                                                arg1 = ((arg1 if (u(arg1) < u(arg3)) else arg3) if (u(arg1) < u(v13)) else v13)
                                                                                                                                                                                                                if (((arg1 if (u(arg1) < u(arg3)) else arg3) if (u(arg1) < u(v13)) else v13) == 0):
                                                                                                                                                                                                                    break
                                                                                                                                                                                                                v5 = func35(v14, arg0, arg1)
                                                                                                                                                                                                                store32(v4 + 68, (load32(v4 + 68) - arg1))
                                                                                                                                                                                                                v14 = (arg1 + v5)
                                                                                                                                                                                                                v13 = (v13 - arg1)
                                                                                                                                                                                                                arg0 = (arg0 + arg1)
                                                                                                                                                                                                                arg3 = (arg3 - arg1)
                                                                                                                                                                                                                v5 = load32(v4 + 4)
                                                                                                                                                                                                                continue
                                                                                                                                                                                                            store32(v4 + 4, 16191)
                                                                                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                                                                                            continue
                                                                                                                                                                                                            break
                                                                                                                                                                                                        if (v8 == 0):
                                                                                                                                                                                                            arg0 = v5
                                                                                                                                                                                                            arg3 = 0
                                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                                            arg1 = v12
                                                                                                                                                                                                            break
                                                                                                                                                                                                        arg2 = (arg2 + 16)
                                                                                                                                                                                                        arg3 = (arg3 - 2)
                                                                                                                                                                                                        v6 = ((load8u(arg0 + 1) << arg1) + v6)
                                                                                                                                                                                                        arg0 = (arg0 + 2)
                                                                                                                                                                                                        break
                                                                                                                                                                                                    arg1 = (v6 & 31)
                                                                                                                                                                                                    store32(v4 + 100, ((v6 & 31) + 257))
                                                                                                                                                                                                    v5 = (((v6 & 0xFFFFFFFF) >> 5) & 31)
                                                                                                                                                                                                    store32(v4 + 104, ((((v6 & 0xFFFFFFFF) >> 5) & 31) + 1))
                                                                                                                                                                                                    v7 = ((((v6 & 0xFFFFFFFF) >> 10) & 15) + 4)
                                                                                                                                                                                                    store32(v4 + 96, ((((v6 & 0xFFFFFFFF) >> 10) & 15) + 4))
                                                                                                                                                                                                    arg2 = (arg2 - 14)
                                                                                                                                                                                                    v6 = ((v6 & 0xFFFFFFFF) >> 14)
                                                                                                                                                                                                    if (((u(v5) < u(30)) & (u(arg1) <= u(29))) == 0):
                                                                                                                                                                                                        store32(v10 + 24, 3236)
                                                                                                                                                                                                        store32(v4 + 4, 16209)
                                                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                                                        continue
                                                                                                                                                                                                    store32(v4 + 4, 16197)
                                                                                                                                                                                                    v5 = 0
                                                                                                                                                                                                    store32(v4 + 108, 0)
                                                                                                                                                                                                    break
                                                                                                                                                                                                    break
                                                                                                                                                                                                v5 = load32(v4 + 108)
                                                                                                                                                                                                v7 = load32(v4 + 96)
                                                                                                                                                                                                if (u(load32(v4 + 108)) < u(load32(v4 + 96))):
                                                                                                                                                                                                    break
                                                                                                                                                                                                break
                                                                                                                                                                                                break
                                                                                                                                                                                            if (v13 == 0):
                                                                                                                                                                                                break
                                                                                                                                                                                            store8(v14, load32(v4 + 68))
                                                                                                                                                                                            store32(v4 + 4, 16200)
                                                                                                                                                                                            v13 = (v13 - 1)
                                                                                                                                                                                            v14 = (v14 + 1)
                                                                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                                                                            continue
                                                                                                                                                                                            break
                                                                                                                                                                                        v5 = load32(v4 + 12)
                                                                                                                                                                                        if (load32(v4 + 12) == 0):
                                                                                                                                                                                            v5 = 0
                                                                                                                                                                                            break
                                                                                                                                                                                        while True:  # block $label79
                                                                                                                                                                                            if (u(arg2) > u(31)):
                                                                                                                                                                                                v8 = arg0
                                                                                                                                                                                                break
                                                                                                                                                                                            if (arg3 == 0):
                                                                                                                                                                                                break
                                                                                                                                                                                            arg1 = (arg2 + 8)
                                                                                                                                                                                            v8 = (arg0 + 1)
                                                                                                                                                                                            v7 = (arg3 - 1)
                                                                                                                                                                                            v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                            if (u(arg2) > u(23)):
                                                                                                                                                                                                arg3 = v7
                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                break
                                                                                                                                                                                            if (v7 == 0):
                                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                                arg3 = 0
                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                arg1 = v12
                                                                                                                                                                                                break
                                                                                                                                                                                            v7 = (arg2 + 16)
                                                                                                                                                                                            v8 = (arg0 + 2)
                                                                                                                                                                                            v9 = (arg3 - 2)
                                                                                                                                                                                            v6 = ((load8u(arg0 + 1) << arg1) + v6)
                                                                                                                                                                                            if (u(arg2) > u(15)):
                                                                                                                                                                                                arg3 = v9
                                                                                                                                                                                                arg2 = v7
                                                                                                                                                                                                break
                                                                                                                                                                                            if (v9 == 0):
                                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                                arg3 = 0
                                                                                                                                                                                                arg2 = v7
                                                                                                                                                                                                arg1 = v12
                                                                                                                                                                                                break
                                                                                                                                                                                            arg1 = (arg2 + 24)
                                                                                                                                                                                            v8 = (arg0 + 3)
                                                                                                                                                                                            v9 = (arg3 - 3)
                                                                                                                                                                                            v6 = ((load8u(arg0 + 2) << v7) + v6)
                                                                                                                                                                                            if (u(arg2) > u(7)):
                                                                                                                                                                                                arg3 = v9
                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                break
                                                                                                                                                                                            if (v9 == 0):
                                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                                arg3 = 0
                                                                                                                                                                                                arg2 = arg1
                                                                                                                                                                                                arg1 = v12
                                                                                                                                                                                                break
                                                                                                                                                                                            arg2 = (arg2 + 32)
                                                                                                                                                                                            v8 = (arg0 + 4)
                                                                                                                                                                                            arg3 = (arg3 - 4)
                                                                                                                                                                                            v6 = ((load8u(arg0 + 3) << arg1) + v6)
                                                                                                                                                                                            break
                                                                                                                                                                                        arg0 = (v18 - v13)
                                                                                                                                                                                        store32(v10 + 20, ((v18 - v13) + load32(v10 + 20)))
                                                                                                                                                                                        store32(v4 + 32, (load32(v4 + 32) + arg0))
                                                                                                                                                                                        while True:  # block $label80
                                                                                                                                                                                            arg1 = (v5 & 4)
                                                                                                                                                                                            if ((v5 & 4) == 0):
                                                                                                                                                                                                break
                                                                                                                                                                                            if (v13 == v18):
                                                                                                                                                                                                break
                                                                                                                                                                                            arg1 = (v14 - arg0)
                                                                                                                                                                                            v5 = load32(v4 + 28)
                                                                                                                                                                                            while True:  # block $label81
                                                                                                                                                                                                if load32(v4 + 20):
                                                                                                                                                                                                    break
                                                                                                                                                                                                break
                                                                                                                                                                                            arg0 = func89(v5, arg1, arg0)
                                                                                                                                                                                            store32(func43(v5, arg1, arg0) + 28, func89(v5, arg1, arg0))
                                                                                                                                                                                            store32(v10 + 48, arg0)
                                                                                                                                                                                            v5 = load32(v4 + 12)
                                                                                                                                                                                            arg1 = (load32(v4 + 12) & 4)
                                                                                                                                                                                            break
                                                                                                                                                                                        if (arg1 == 0):
                                                                                                                                                                                            break
                                                                                                                                                                                        if (load32(v4 + 28) == (v6 if load32(v4 + 20) else (((v6 << 24) | ((v6 & 65280) << 8)) | ((((v6 & 0xFFFFFFFF) >> 8) & 65280) | ((v6 & 0xFFFFFFFF) >> 24))))):
                                                                                                                                                                                            break
                                                                                                                                                                                        store32(v10 + 24, 4137)
                                                                                                                                                                                        store32(v4 + 4, 16209)
                                                                                                                                                                                        arg0 = v8
                                                                                                                                                                                        v18 = v13
                                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                                        continue
                                                                                                                                                                                        break
                                                                                                                                                                                    store32(v4 + 4, 16192)
                                                                                                                                                                                    break
                                                                                                                                                                                    break
                                                                                                                                                                                arg0 = v8
                                                                                                                                                                                v6 = 0
                                                                                                                                                                                arg2 = 0
                                                                                                                                                                                v18 = v13
                                                                                                                                                                                break
                                                                                                                                                                            store32(v4 + 4, 16207)
                                                                                                                                                                            break
                                                                                                                                                                            break
                                                                                                                                                                        while True:  # $label84
                                                                                                                                                                            if (u(arg2) <= u(2)):
                                                                                                                                                                                if (arg3 == 0):
                                                                                                                                                                                    break
                                                                                                                                                                                arg3 = (arg3 - 1)
                                                                                                                                                                                v6 = ((load8u(arg0) << arg2) + v6)
                                                                                                                                                                                arg2 = (arg2 + 8)
                                                                                                                                                                                arg0 = (arg0 + 1)
                                                                                                                                                                            arg1 = (v5 + 1)
                                                                                                                                                                            store32(v4 + 108, (v5 + 1))
                                                                                                                                                                            store16((v4 + (load16u(((v5 << 1) + 26464)) << 1)) + 116, (v6 & 7))
                                                                                                                                                                            arg2 = (arg2 - 3)
                                                                                                                                                                            v6 = ((v6 & 0xFFFFFFFF) >> 3)
                                                                                                                                                                            v5 = arg1
                                                                                                                                                                            if (arg1 != v7):
                                                                                                                                                                                continue
                                                                                                                                                                            break
                                                                                                                                                                        v5 = v7
                                                                                                                                                                        break
                                                                                                                                                                    if (u(v5) <= u(18)):
                                                                                                                                                                        v8 = 0
                                                                                                                                                                        arg1 = v5
                                                                                                                                                                        v12 = ((3 - v5) & 3)
                                                                                                                                                                        if ((3 - v5) & 3):
                                                                                                                                                                            while True:  # $label85
                                                                                                                                                                                store16((v4 + (load16u(((arg1 << 1) + 26464)) << 1)) + 116, 0)
                                                                                                                                                                                arg1 = (arg1 + 1)
                                                                                                                                                                                v8 = (v8 + 1)
                                                                                                                                                                                if ((v8 + 1) != v12):
                                                                                                                                                                                    continue
                                                                                                                                                                                break
                                                                                                                                                                        if (u((v5 - 16)) >= u(3)):
                                                                                                                                                                            while True:  # $label86
                                                                                                                                                                                v12 = (v4 + 116)
                                                                                                                                                                                v5 = (arg1 << 1)
                                                                                                                                                                                store16(((v4 + 116) + (load16u(((arg1 << 1) + 26464)) << 1)), 0)
                                                                                                                                                                                store16((v12 + (load16u((v5 + 26466)) << 1)), 0)
                                                                                                                                                                                store16((v12 + (load16u((v5 + 26468)) << 1)), 0)
                                                                                                                                                                                store16((v12 + (load16u((v5 + 26470)) << 1)), 0)
                                                                                                                                                                                arg1 = (arg1 + 4)
                                                                                                                                                                                if ((arg1 + 4) != 19):
                                                                                                                                                                                    continue
                                                                                                                                                                                break
                                                                                                                                                                        store32(v4 + 108, 19)
                                                                                                                                                                    store32(v4 + 88, 7)
                                                                                                                                                                    store32(v4 + 80, v27)
                                                                                                                                                                    store32(v4 + 112, v27)
                                                                                                                                                                    v5 = 0
                                                                                                                                                                    v12 = func241(0, v31, 19, v32, v34, v30)
                                                                                                                                                                    if func241(0, v31, 19, v32, v34, v30):
                                                                                                                                                                        store32(v10 + 24, 2822)
                                                                                                                                                                        store32(v4 + 4, 16209)
                                                                                                                                                                        v5 = load32(v4 + 4)
                                                                                                                                                                        continue
                                                                                                                                                                    store32(v4 + 4, 16198)
                                                                                                                                                                    store32(v4 + 108, 0)
                                                                                                                                                                    v12 = 0
                                                                                                                                                                    break
                                                                                                                                                                v28 = load32(v4 + 100)
                                                                                                                                                                v19 = (load32(v4 + 100) + load32(v4 + 104))
                                                                                                                                                                if (u((load32(v4 + 100) + load32(v4 + 104))) > u(v5)):
                                                                                                                                                                    v21 = ((-1 << load32(v4 + 88)) ^ -1)
                                                                                                                                                                    v17 = load32(v4 + 80)
                                                                                                                                                                    while True:  # $label103
                                                                                                                                                                        v9 = arg2
                                                                                                                                                                        v8 = arg3
                                                                                                                                                                        v7 = arg0
                                                                                                                                                                        while True:  # block $label87
                                                                                                                                                                            v15 = (v6 & v21)
                                                                                                                                                                            v11 = load8u((v17 + ((v6 & v21) << 2)) + 1)
                                                                                                                                                                            if (u(load8u((v17 + ((v6 & v21) << 2)) + 1)) <= u(arg2)):
                                                                                                                                                                                arg1 = arg2
                                                                                                                                                                                break
                                                                                                                                                                            while True:  # $label89
                                                                                                                                                                                if (v8 == 0):
                                                                                                                                                                                    break
                                                                                                                                                                                v11 = (load8u(v7) << v9)
                                                                                                                                                                                v7 = (v7 + 1)
                                                                                                                                                                                v8 = (v8 - 1)
                                                                                                                                                                                arg1 = (v9 + 8)
                                                                                                                                                                                v9 = (v9 + 8)
                                                                                                                                                                                v6 = (v6 + v11)
                                                                                                                                                                                v15 = ((v6 + v11) & v21)
                                                                                                                                                                                v11 = load8u((v17 + (((v6 + v11) & v21) << 2)) + 1)
                                                                                                                                                                                if (u(arg1) < u(load8u((v17 + (((v6 + v11) & v21) << 2)) + 1))):
                                                                                                                                                                                    continue
                                                                                                                                                                                break
                                                                                                                                                                            arg0 = v7
                                                                                                                                                                            arg3 = v8
                                                                                                                                                                            break
                                                                                                                                                                        while True:  # block $label90
                                                                                                                                                                            arg2 = load16u((v17 + (v15 << 2)) + 2)
                                                                                                                                                                            if (u(load16u((v17 + (v15 << 2)) + 2)) <= u(15)):
                                                                                                                                                                                v8 = (v5 + 1)
                                                                                                                                                                                store32(v4 + 108, (v5 + 1))
                                                                                                                                                                                store16((v4 + (v5 << 1)) + 116, arg2)
                                                                                                                                                                                arg2 = (arg1 - v11)
                                                                                                                                                                                v6 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                                                v5 = v8
                                                                                                                                                                                break
                                                                                                                                                                            while True:  # block $label96
                                                                                                                                                                                while True:  # block $label98
                                                                                                                                                                                    while True:  # block $label93
                                                                                                                                                                                        while True:  # block $label92
                                                                                                                                                                                            while True:  # block $label91
                                                                                                                                                                                                # br_table[(arg2 - 16)]
                                                                                                                                                                                                break
                                                                                                                                                                                                break
                                                                                                                                                                                            arg2 = (v11 + 2)
                                                                                                                                                                                            if (u((v11 + 2)) > u(arg1)):
                                                                                                                                                                                                while True:  # $label95
                                                                                                                                                                                                    if (arg3 == 0):
                                                                                                                                                                                                        break
                                                                                                                                                                                                    arg3 = (arg3 - 1)
                                                                                                                                                                                                    v6 = ((load8u(arg0) << arg1) + v6)
                                                                                                                                                                                                    arg0 = (arg0 + 1)
                                                                                                                                                                                                    arg1 = (arg1 + 8)
                                                                                                                                                                                                    if (u((arg1 + 8)) < u(arg2)):
                                                                                                                                                                                                        continue
                                                                                                                                                                                                    break
                                                                                                                                                                                            arg2 = (arg1 - v11)
                                                                                                                                                                                            arg1 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                                                            if (v5 == 0):
                                                                                                                                                                                                store32(v10 + 24, 2894)
                                                                                                                                                                                                store32(v4 + 4, 16209)
                                                                                                                                                                                                v6 = arg1
                                                                                                                                                                                                v5 = load32(v4 + 4)
                                                                                                                                                                                                continue
                                                                                                                                                                                            arg2 = (arg2 - 2)
                                                                                                                                                                                            v6 = ((arg1 & 0xFFFFFFFF) >> 2)
                                                                                                                                                                                            v8 = ((arg1 & 3) + 3)
                                                                                                                                                                                            break
                                                                                                                                                                                            break
                                                                                                                                                                                        arg2 = (v11 + 3)
                                                                                                                                                                                        if (u((v11 + 3)) > u(arg1)):
                                                                                                                                                                                            while True:  # $label97
                                                                                                                                                                                                if (arg3 == 0):
                                                                                                                                                                                                    break
                                                                                                                                                                                                arg3 = (arg3 - 1)
                                                                                                                                                                                                v6 = ((load8u(arg0) << arg1) + v6)
                                                                                                                                                                                                arg0 = (arg0 + 1)
                                                                                                                                                                                                arg1 = (arg1 + 8)
                                                                                                                                                                                                if (u((arg1 + 8)) < u(arg2)):
                                                                                                                                                                                                    continue
                                                                                                                                                                                                break
                                                                                                                                                                                        arg2 = ((arg1 - v11) - 3)
                                                                                                                                                                                        arg1 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                                                        v6 = ((((v6 & 0xFFFFFFFF) >> v11) & 0xFFFFFFFF) >> 3)
                                                                                                                                                                                        break
                                                                                                                                                                                        break
                                                                                                                                                                                    arg2 = (v11 + 7)
                                                                                                                                                                                    if (u((v11 + 7)) > u(arg1)):
                                                                                                                                                                                        while True:  # $label99
                                                                                                                                                                                            if (arg3 == 0):
                                                                                                                                                                                                break
                                                                                                                                                                                            arg3 = (arg3 - 1)
                                                                                                                                                                                            v6 = ((load8u(arg0) << arg1) + v6)
                                                                                                                                                                                            arg0 = (arg0 + 1)
                                                                                                                                                                                            arg1 = (arg1 + 8)
                                                                                                                                                                                            if (u((arg1 + 8)) < u(arg2)):
                                                                                                                                                                                                continue
                                                                                                                                                                                            break
                                                                                                                                                                                    arg2 = ((arg1 - v11) - 7)
                                                                                                                                                                                    arg1 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                                                    v6 = ((((v6 & 0xFFFFFFFF) >> v11) & 0xFFFFFFFF) >> 7)
                                                                                                                                                                                    break
                                                                                                                                                                                v8 = ((arg1 & 127) + 11)
                                                                                                                                                                                break
                                                                                                                                                                            arg1 = 0
                                                                                                                                                                            if (u((v5 + v8)) > u(v19)):
                                                                                                                                                                                break
                                                                                                                                                                            v9 = (v8 - 1)
                                                                                                                                                                            v7 = 0
                                                                                                                                                                            v11 = (v8 & 3)
                                                                                                                                                                            if (v8 & 3):
                                                                                                                                                                                while True:  # $label101
                                                                                                                                                                                    store16((v4 + (v5 << 1)) + 116, arg1)
                                                                                                                                                                                    v5 = (v5 + 1)
                                                                                                                                                                                    v8 = (v8 - 1)
                                                                                                                                                                                    v7 = (v7 + 1)
                                                                                                                                                                                    if ((v7 + 1) != v11):
                                                                                                                                                                                        continue
                                                                                                                                                                                    break
                                                                                                                                                                            if (u(v9) >= u(3)):
                                                                                                                                                                                while True:  # $label102
                                                                                                                                                                                    v7 = (v4 + (v5 << 1))
                                                                                                                                                                                    store16((v4 + (v5 << 1)) + 118, arg1)
                                                                                                                                                                                    store16(v7 + 116, arg1)
                                                                                                                                                                                    store16(v7 + 120, arg1)
                                                                                                                                                                                    store16(v7 + 122, arg1)
                                                                                                                                                                                    v5 = (v5 + 4)
                                                                                                                                                                                    v8 = (v8 - 4)
                                                                                                                                                                                    if (v8 - 4):
                                                                                                                                                                                        continue
                                                                                                                                                                                    break
                                                                                                                                                                            store32(v4 + 108, v5)
                                                                                                                                                                            break
                                                                                                                                                                        if (u(v5) < u(v19)):
                                                                                                                                                                            continue
                                                                                                                                                                        break
                                                                                                                                                                if (load16u(v4 + 628) == 0):
                                                                                                                                                                    store32(v10 + 24, 4054)
                                                                                                                                                                    store32(v4 + 4, 16209)
                                                                                                                                                                    v5 = load32(v4 + 4)
                                                                                                                                                                    continue
                                                                                                                                                                store32(v4 + 88, 9)
                                                                                                                                                                store32(v4 + 80, v27)
                                                                                                                                                                store32(v4 + 112, v27)
                                                                                                                                                                v12 = func241(1, v31, v28, v32, v34, v30)
                                                                                                                                                                if func241(1, v31, v28, v32, v34, v30):
                                                                                                                                                                    store32(v10 + 24, 2794)
                                                                                                                                                                    store32(v4 + 4, 16209)
                                                                                                                                                                    v5 = load32(v4 + 4)
                                                                                                                                                                    continue
                                                                                                                                                                store32(v4 + 92, 6)
                                                                                                                                                                store32(v4 + 84, load32(v4 + 112))
                                                                                                                                                                v12 = func241(2, (v31 + (load32(v4 + 100) << 1)), load32(v4 + 104), v32, v39, v30)
                                                                                                                                                                if func241(2, (v31 + (load32(v4 + 100) << 1)), load32(v4 + 104), v32, v39, v30):
                                                                                                                                                                    store32(v10 + 24, 2872)
                                                                                                                                                                    store32(v4 + 4, 16209)
                                                                                                                                                                    v5 = load32(v4 + 4)
                                                                                                                                                                    continue
                                                                                                                                                                store32(v4 + 4, 16199)
                                                                                                                                                                v12 = 0
                                                                                                                                                                break
                                                                                                                                                            store32(v4 + 4, 16200)
                                                                                                                                                            break
                                                                                                                                                        while True:  # block $label104
                                                                                                                                                            if (u(arg3) < u(6)):
                                                                                                                                                                break
                                                                                                                                                            if (u(v13) < u(258)):
                                                                                                                                                                break
                                                                                                                                                            store32(v10 + 16, v13)
                                                                                                                                                            store32(v10 + 12, v14)
                                                                                                                                                            store32(v10 + 4, arg3)
                                                                                                                                                            store32(v10, arg0)
                                                                                                                                                            store32(v4 + 64, arg2)
                                                                                                                                                            store32(v4 + 60, v6)
                                                                                                                                                            arg1 = load32(v10 + 16)
                                                                                                                                                            v7 = load32(v10 + 12)
                                                                                                                                                            arg0 = (load32(v10 + 16) + load32(v10 + 12))
                                                                                                                                                            v19 = ((load32(v10 + 16) + load32(v10 + 12)) + (v18 ^ -1))
                                                                                                                                                            v14 = load32(v10 + 28)
                                                                                                                                                            v9 = load32(load32(v10 + 28) + 52)
                                                                                                                                                            v40 = ((arg0 + (load32(load32(v10 + 28) + 52) ^ -1)) - v18)
                                                                                                                                                            v21 = (v9 & 7)
                                                                                                                                                            v41 = load32(v14 + 44)
                                                                                                                                                            v42 = (v9 + load32(v14 + 44))
                                                                                                                                                            v28 = (arg0 - 257)
                                                                                                                                                            v43 = (v7 + (arg1 - v18))
                                                                                                                                                            arg2 = load32(v10)
                                                                                                                                                            v36 = ((load32(v10) + load32(v10 + 4)) - 5)
                                                                                                                                                            v44 = ((-1 << load32(v14 + 92)) ^ -1)
                                                                                                                                                            v45 = ((-1 << load32(v14 + 88)) ^ -1)
                                                                                                                                                            v37 = load32(v14 + 84)
                                                                                                                                                            v38 = load32(v14 + 80)
                                                                                                                                                            v6 = load32(v14 + 64)
                                                                                                                                                            v11 = load32(v14 + 60)
                                                                                                                                                            v8 = load32(v14 + 56)
                                                                                                                                                            v46 = load32(v14 + 48)
                                                                                                                                                            while True:  # block $label130
                                                                                                                                                                while True:  # block $label112
                                                                                                                                                                    while True:  # $label131
                                                                                                                                                                        if (u(v6) <= u(14)):
                                                                                                                                                                            v11 = (((load8u(arg2) << v6) + v11) + (load8u(arg2 + 1) << (v6 + 8)))
                                                                                                                                                                            v6 = (v6 + 16)
                                                                                                                                                                            arg2 = (arg2 + 2)
                                                                                                                                                                        arg3 = (v38 + ((v11 & v45) << 2))
                                                                                                                                                                        arg0 = load8u((v38 + ((v11 & v45) << 2)) + 1)
                                                                                                                                                                        v6 = (v6 - load8u((v38 + ((v11 & v45) << 2)) + 1))
                                                                                                                                                                        v11 = ((v11 & 0xFFFFFFFF) >> arg0)
                                                                                                                                                                        while True:  # block $label110
                                                                                                                                                                            while True:  # block $label105
                                                                                                                                                                                while True:  # block $label108
                                                                                                                                                                                    while True:  # $label111
                                                                                                                                                                                        arg0 = load8u(arg3)
                                                                                                                                                                                        if (load8u(arg3) == 0):
                                                                                                                                                                                            store8(v7, load8u(arg3 + 2))
                                                                                                                                                                                            v7 = (v7 + 1)
                                                                                                                                                                                            break
                                                                                                                                                                                        if (arg0 & 16):
                                                                                                                                                                                            v13 = load16u(arg3 + 2)
                                                                                                                                                                                            while True:  # block $label106
                                                                                                                                                                                                arg0 = (arg0 & 15)
                                                                                                                                                                                                if ((arg0 & 15) == 0):
                                                                                                                                                                                                    arg1 = arg2
                                                                                                                                                                                                    break
                                                                                                                                                                                                while True:  # block $label107
                                                                                                                                                                                                    if (u(arg0) <= u(v6)):
                                                                                                                                                                                                        arg1 = arg2
                                                                                                                                                                                                        break
                                                                                                                                                                                                    arg1 = (arg2 + 1)
                                                                                                                                                                                                    v11 = ((load8u(arg2) << v6) + v11)
                                                                                                                                                                                                    break
                                                                                                                                                                                                v6 = ((v6 + 8) - arg0)
                                                                                                                                                                                                v13 = ((v11 & ((-1 << arg0) ^ -1)) + v13)
                                                                                                                                                                                                break
                                                                                                                                                                                            arg0 = ((v11 & 0xFFFFFFFF) >> arg0)
                                                                                                                                                                                            if (u(v6) <= u(14)):
                                                                                                                                                                                                arg0 = (((load8u(arg1) << v6) + arg0) + (load8u(arg1 + 1) << (v6 + 8)))
                                                                                                                                                                                                v6 = (v6 + 16)
                                                                                                                                                                                                arg1 = (arg1 + 2)
                                                                                                                                                                                            arg3 = (v37 + ((arg0 & v44) << 2))
                                                                                                                                                                                            arg2 = load8u((v37 + ((arg0 & v44) << 2)) + 1)
                                                                                                                                                                                            v6 = (v6 - load8u((v37 + ((arg0 & v44) << 2)) + 1))
                                                                                                                                                                                            v11 = ((arg0 & 0xFFFFFFFF) >> arg2)
                                                                                                                                                                                            arg0 = load8u(arg3)
                                                                                                                                                                                            if (load8u(arg3) & 16):
                                                                                                                                                                                                break
                                                                                                                                                                                            while True:  # $label109
                                                                                                                                                                                                if ((arg0 & 64) == 0):
                                                                                                                                                                                                    arg3 = ((v37 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2))
                                                                                                                                                                                                    arg0 = load8u(((v37 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2)) + 1)
                                                                                                                                                                                                    v6 = (v6 - load8u(((v37 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2)) + 1))
                                                                                                                                                                                                    v11 = ((v11 & 0xFFFFFFFF) >> arg0)
                                                                                                                                                                                                    arg0 = load8u(arg3)
                                                                                                                                                                                                    if ((load8u(arg3) & 16) == 0):
                                                                                                                                                                                                        continue
                                                                                                                                                                                                    break
                                                                                                                                                                                                break
                                                                                                                                                                                            v13 = 4865
                                                                                                                                                                                            arg2 = arg1
                                                                                                                                                                                            break
                                                                                                                                                                                        if ((arg0 & 64) == 0):
                                                                                                                                                                                            arg3 = ((v38 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2))
                                                                                                                                                                                            arg0 = load8u(((v38 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2)) + 1)
                                                                                                                                                                                            v6 = (v6 - load8u(((v38 + (load16u(arg3 + 2) << 2)) + ((v11 & ((-1 << arg0) ^ -1)) << 2)) + 1))
                                                                                                                                                                                            v11 = ((v11 & 0xFFFFFFFF) >> arg0)
                                                                                                                                                                                            continue
                                                                                                                                                                                        break
                                                                                                                                                                                    v13 = 4837
                                                                                                                                                                                    if (arg0 & 32):
                                                                                                                                                                                        break
                                                                                                                                                                                    break
                                                                                                                                                                                    break
                                                                                                                                                                                v15 = load16u(arg3 + 2)
                                                                                                                                                                                while True:  # block $label113
                                                                                                                                                                                    arg3 = (arg0 & 15)
                                                                                                                                                                                    if (u((arg0 & 15)) <= u(v6)):
                                                                                                                                                                                        arg0 = v6
                                                                                                                                                                                        break
                                                                                                                                                                                    v11 = ((load8u(arg1) << v6) + v11)
                                                                                                                                                                                    arg0 = (v6 + 8)
                                                                                                                                                                                    if (u(arg3) <= u((v6 + 8))):
                                                                                                                                                                                        break
                                                                                                                                                                                    v11 = ((load8u(arg1 + 1) << arg0) + v11)
                                                                                                                                                                                    arg0 = (v6 + 16)
                                                                                                                                                                                    break
                                                                                                                                                                                arg2 = (arg1 + 2)
                                                                                                                                                                                arg1 = (v11 & ((-1 << arg3) ^ -1))
                                                                                                                                                                                v6 = (arg0 - arg3)
                                                                                                                                                                                v11 = ((v11 & 0xFFFFFFFF) >> arg3)
                                                                                                                                                                                while True:  # block $label128
                                                                                                                                                                                    v17 = (arg1 + v15)
                                                                                                                                                                                    arg0 = (v7 - v43)
                                                                                                                                                                                    if (u((arg1 + v15)) > u((v7 - v43))):
                                                                                                                                                                                        while True:  # block $label114
                                                                                                                                                                                            v5 = (v17 - arg0)
                                                                                                                                                                                            if (u((v17 - arg0)) <= u(v46)):
                                                                                                                                                                                                break
                                                                                                                                                                                            if (load32(v14 + 7108) == 0):
                                                                                                                                                                                                break
                                                                                                                                                                                            v13 = 4158
                                                                                                                                                                                            break
                                                                                                                                                                                            break
                                                                                                                                                                                        while True:  # block $label115
                                                                                                                                                                                            while True:  # block $label117
                                                                                                                                                                                                if (v9 == 0):
                                                                                                                                                                                                    arg3 = (v8 + (v41 - v5))
                                                                                                                                                                                                    if (u(v5) >= u(v13)):
                                                                                                                                                                                                        break
                                                                                                                                                                                                    v15 = (((arg1 + v19) + v15) - v7)
                                                                                                                                                                                                    arg1 = 0
                                                                                                                                                                                                    arg0 = v5
                                                                                                                                                                                                    v25 = (v5 & 7)
                                                                                                                                                                                                    if (v5 & 7):
                                                                                                                                                                                                        while True:  # $label116
                                                                                                                                                                                                            store8(v7, load8u(arg3))
                                                                                                                                                                                                            arg0 = (arg0 - 1)
                                                                                                                                                                                                            v7 = (v7 + 1)
                                                                                                                                                                                                            arg3 = (arg3 + 1)
                                                                                                                                                                                                            arg1 = (arg1 + 1)
                                                                                                                                                                                                            if ((arg1 + 1) != v25):
                                                                                                                                                                                                                continue
                                                                                                                                                                                                            break
                                                                                                                                                                                                    if (u(v15) < u(7)):
                                                                                                                                                                                                        break
                                                                                                                                                                                                    while True:  # $label118
                                                                                                                                                                                                        store8(v7, load8u(arg3))
                                                                                                                                                                                                        store8(v7 + 1, load8u(arg3 + 1))
                                                                                                                                                                                                        store8(v7 + 2, load8u(arg3 + 2))
                                                                                                                                                                                                        store8(v7 + 3, load8u(arg3 + 3))
                                                                                                                                                                                                        store8(v7 + 4, load8u(arg3 + 4))
                                                                                                                                                                                                        store8(v7 + 5, load8u(arg3 + 5))
                                                                                                                                                                                                        store8(v7 + 6, load8u(arg3 + 6))
                                                                                                                                                                                                        store8(v7 + 7, load8u(arg3 + 7))
                                                                                                                                                                                                        v7 = (v7 + 8)
                                                                                                                                                                                                        arg3 = (arg3 + 8)
                                                                                                                                                                                                        arg0 = (arg0 - 8)
                                                                                                                                                                                                        if (arg0 - 8):
                                                                                                                                                                                                            continue
                                                                                                                                                                                                        break
                                                                                                                                                                                                    break
                                                                                                                                                                                                if (u(v5) > u(v9)):
                                                                                                                                                                                                    arg3 = (v8 + (v42 - v5))
                                                                                                                                                                                                    v5 = (v5 - v9)
                                                                                                                                                                                                    if (u(v13) <= u((v5 - v9))):
                                                                                                                                                                                                        break
                                                                                                                                                                                                    v15 = (((arg1 + v40) + v15) - v7)
                                                                                                                                                                                                    arg1 = 0
                                                                                                                                                                                                    arg0 = v5
                                                                                                                                                                                                    v25 = (v5 & 7)
                                                                                                                                                                                                    if (v5 & 7):
                                                                                                                                                                                                        while True:  # $label119
                                                                                                                                                                                                            store8(v7, load8u(arg3))
                                                                                                                                                                                                            arg0 = (arg0 - 1)
                                                                                                                                                                                                            v7 = (v7 + 1)
                                                                                                                                                                                                            arg3 = (arg3 + 1)
                                                                                                                                                                                                            arg1 = (arg1 + 1)
                                                                                                                                                                                                            if ((arg1 + 1) != v25):
                                                                                                                                                                                                                continue
                                                                                                                                                                                                            break
                                                                                                                                                                                                    if (u(v15) >= u(7)):
                                                                                                                                                                                                        while True:  # $label120
                                                                                                                                                                                                            store8(v7, load8u(arg3))
                                                                                                                                                                                                            store8(v7 + 1, load8u(arg3 + 1))
                                                                                                                                                                                                            store8(v7 + 2, load8u(arg3 + 2))
                                                                                                                                                                                                            store8(v7 + 3, load8u(arg3 + 3))
                                                                                                                                                                                                            store8(v7 + 4, load8u(arg3 + 4))
                                                                                                                                                                                                            store8(v7 + 5, load8u(arg3 + 5))
                                                                                                                                                                                                            store8(v7 + 6, load8u(arg3 + 6))
                                                                                                                                                                                                            store8(v7 + 7, load8u(arg3 + 7))
                                                                                                                                                                                                            v7 = (v7 + 8)
                                                                                                                                                                                                            arg3 = (arg3 + 8)
                                                                                                                                                                                                            arg0 = (arg0 - 8)
                                                                                                                                                                                                            if (arg0 - 8):
                                                                                                                                                                                                                continue
                                                                                                                                                                                                            break
                                                                                                                                                                                                    v13 = (v13 - v5)
                                                                                                                                                                                                    if (u(v9) >= u((v13 - v5))):
                                                                                                                                                                                                        arg3 = v8
                                                                                                                                                                                                        break
                                                                                                                                                                                                    arg1 = 0
                                                                                                                                                                                                    arg0 = v9
                                                                                                                                                                                                    arg3 = v8
                                                                                                                                                                                                    if v21:
                                                                                                                                                                                                        while True:  # $label121
                                                                                                                                                                                                            store8(v7, load8u(arg3))
                                                                                                                                                                                                            arg0 = (arg0 - 1)
                                                                                                                                                                                                            v7 = (v7 + 1)
                                                                                                                                                                                                            arg3 = (arg3 + 1)
                                                                                                                                                                                                            arg1 = (arg1 + 1)
                                                                                                                                                                                                            if ((arg1 + 1) != v21):
                                                                                                                                                                                                                continue
                                                                                                                                                                                                            break
                                                                                                                                                                                                    if (u(v9) >= u(8)):
                                                                                                                                                                                                        while True:  # $label122
                                                                                                                                                                                                            store8(v7, load8u(arg3))
                                                                                                                                                                                                            store8(v7 + 1, load8u(arg3 + 1))
                                                                                                                                                                                                            store8(v7 + 2, load8u(arg3 + 2))
                                                                                                                                                                                                            store8(v7 + 3, load8u(arg3 + 3))
                                                                                                                                                                                                            store8(v7 + 4, load8u(arg3 + 4))
                                                                                                                                                                                                            store8(v7 + 5, load8u(arg3 + 5))
                                                                                                                                                                                                            store8(v7 + 6, load8u(arg3 + 6))
                                                                                                                                                                                                            store8(v7 + 7, load8u(arg3 + 7))
                                                                                                                                                                                                            v7 = (v7 + 8)
                                                                                                                                                                                                            arg3 = (arg3 + 8)
                                                                                                                                                                                                            arg0 = (arg0 - 8)
                                                                                                                                                                                                            if (arg0 - 8):
                                                                                                                                                                                                                continue
                                                                                                                                                                                                            break
                                                                                                                                                                                                    arg3 = (v7 - v17)
                                                                                                                                                                                                    v13 = (v13 - v9)
                                                                                                                                                                                                    break
                                                                                                                                                                                                arg3 = (v8 + (v9 - v5))
                                                                                                                                                                                                if (u(v5) >= u(v13)):
                                                                                                                                                                                                    break
                                                                                                                                                                                                v15 = (((arg1 + v19) + v15) - v7)
                                                                                                                                                                                                arg1 = 0
                                                                                                                                                                                                arg0 = v5
                                                                                                                                                                                                v25 = (v5 & 7)
                                                                                                                                                                                                if (v5 & 7):
                                                                                                                                                                                                    while True:  # $label123
                                                                                                                                                                                                        store8(v7, load8u(arg3))
                                                                                                                                                                                                        arg0 = (arg0 - 1)
                                                                                                                                                                                                        v7 = (v7 + 1)
                                                                                                                                                                                                        arg3 = (arg3 + 1)
                                                                                                                                                                                                        arg1 = (arg1 + 1)
                                                                                                                                                                                                        if ((arg1 + 1) != v25):
                                                                                                                                                                                                            continue
                                                                                                                                                                                                        break
                                                                                                                                                                                                if (u(v15) < u(7)):
                                                                                                                                                                                                    break
                                                                                                                                                                                                while True:  # $label124
                                                                                                                                                                                                    store8(v7, load8u(arg3))
                                                                                                                                                                                                    store8(v7 + 1, load8u(arg3 + 1))
                                                                                                                                                                                                    store8(v7 + 2, load8u(arg3 + 2))
                                                                                                                                                                                                    store8(v7 + 3, load8u(arg3 + 3))
                                                                                                                                                                                                    store8(v7 + 4, load8u(arg3 + 4))
                                                                                                                                                                                                    store8(v7 + 5, load8u(arg3 + 5))
                                                                                                                                                                                                    store8(v7 + 6, load8u(arg3 + 6))
                                                                                                                                                                                                    store8(v7 + 7, load8u(arg3 + 7))
                                                                                                                                                                                                    v7 = (v7 + 8)
                                                                                                                                                                                                    arg3 = (arg3 + 8)
                                                                                                                                                                                                    arg0 = (arg0 - 8)
                                                                                                                                                                                                    if (arg0 - 8):
                                                                                                                                                                                                        continue
                                                                                                                                                                                                    break
                                                                                                                                                                                                break
                                                                                                                                                                                            arg3 = (v7 - v17)
                                                                                                                                                                                            v13 = (v13 - v5)
                                                                                                                                                                                            break
                                                                                                                                                                                        while True:  # block $label125
                                                                                                                                                                                            if (u(v13) < u(3)):
                                                                                                                                                                                                break
                                                                                                                                                                                            arg0 = 0
                                                                                                                                                                                            arg1 = (v13 - 3)
                                                                                                                                                                                            # TODO: i32.div_u []
                                                                                                                                                                                            v5 = ((3 + 1) & 3)
                                                                                                                                                                                            if ((3 + 1) & 3):
                                                                                                                                                                                                while True:  # $label126
                                                                                                                                                                                                    store8(v7, load8u(arg3))
                                                                                                                                                                                                    store8(v7 + 1, load8u(arg3 + 1))
                                                                                                                                                                                                    store8(v7 + 2, load8u(arg3 + 2))
                                                                                                                                                                                                    v13 = (v13 - 3)
                                                                                                                                                                                                    v7 = (v7 + 3)
                                                                                                                                                                                                    arg3 = (arg3 + 3)
                                                                                                                                                                                                    arg0 = (arg0 + 1)
                                                                                                                                                                                                    if ((arg0 + 1) != v5):
                                                                                                                                                                                                        continue
                                                                                                                                                                                                    break
                                                                                                                                                                                            if (u(arg1) < u(9)):
                                                                                                                                                                                                break
                                                                                                                                                                                            while True:  # $label127
                                                                                                                                                                                                store8(v7, load8u(arg3))
                                                                                                                                                                                                store8(v7 + 1, load8u(arg3 + 1))
                                                                                                                                                                                                store8(v7 + 2, load8u(arg3 + 2))
                                                                                                                                                                                                store8(v7 + 3, load8u(arg3 + 3))
                                                                                                                                                                                                store8(v7 + 4, load8u(arg3 + 4))
                                                                                                                                                                                                store8(v7 + 5, load8u(arg3 + 5))
                                                                                                                                                                                                store8(v7 + 6, load8u(arg3 + 6))
                                                                                                                                                                                                store8(v7 + 7, load8u(arg3 + 7))
                                                                                                                                                                                                store8(v7 + 8, load8u(arg3 + 8))
                                                                                                                                                                                                store8(v7 + 9, load8u(arg3 + 9))
                                                                                                                                                                                                store8(v7 + 10, load8u(arg3 + 10))
                                                                                                                                                                                                store8(v7 + 11, load8u(arg3 + 11))
                                                                                                                                                                                                v7 = (v7 + 12)
                                                                                                                                                                                                arg3 = (arg3 + 12)
                                                                                                                                                                                                v13 = (v13 - 12)
                                                                                                                                                                                                if (u((v13 - 12)) > u(2)):
                                                                                                                                                                                                    continue
                                                                                                                                                                                                break
                                                                                                                                                                                            break
                                                                                                                                                                                        if (v13 == 0):
                                                                                                                                                                                            break
                                                                                                                                                                                        store8(v7, load8u(arg3))
                                                                                                                                                                                        if (v13 != 1):
                                                                                                                                                                                            break
                                                                                                                                                                                        v7 = (v7 + 1)
                                                                                                                                                                                        break
                                                                                                                                                                                    arg1 = (v7 - v17)
                                                                                                                                                                                    while True:  # $label129
                                                                                                                                                                                        arg0 = v7
                                                                                                                                                                                        arg3 = arg1
                                                                                                                                                                                        store8(v7, load8u(arg1))
                                                                                                                                                                                        store8(arg0 + 1, load8u(arg1 + 1))
                                                                                                                                                                                        store8(arg0 + 2, load8u(arg1 + 2))
                                                                                                                                                                                        v7 = (arg0 + 3)
                                                                                                                                                                                        arg1 = (arg1 + 3)
                                                                                                                                                                                        v13 = (v13 - 3)
                                                                                                                                                                                        if (u((v13 - 3)) > u(2)):
                                                                                                                                                                                            continue
                                                                                                                                                                                        break
                                                                                                                                                                                    if (v13 == 0):
                                                                                                                                                                                        break
                                                                                                                                                                                    store8(arg0 + 3, load8u(arg1))
                                                                                                                                                                                    if (v13 == 1):
                                                                                                                                                                                        v7 = (arg0 + 4)
                                                                                                                                                                                        break
                                                                                                                                                                                    store8(arg0 + 4, load8u(arg3 + 4))
                                                                                                                                                                                    v7 = (arg0 + 5)
                                                                                                                                                                                    break
                                                                                                                                                                                    break
                                                                                                                                                                                store8(v7 + 1, load8u(arg3 + 1))
                                                                                                                                                                                v7 = (v7 + 2)
                                                                                                                                                                                break
                                                                                                                                                                            if (u(arg2) >= u(v36)):
                                                                                                                                                                                break
                                                                                                                                                                            if (u(v7) < u(v28)):
                                                                                                                                                                                continue
                                                                                                                                                                            break
                                                                                                                                                                            break
                                                                                                                                                                        break
                                                                                                                                                                    store32(v10 + 24, v13)
                                                                                                                                                                    break
                                                                                                                                                                store32((v13 - 3) + 4, 16209)
                                                                                                                                                                break
                                                                                                                                                            store32(v10 + 12, v7)
                                                                                                                                                            arg0 = (arg2 - ((v6 & 0xFFFFFFFF) >> 3))
                                                                                                                                                            store32(v10, (arg2 - ((v6 & 0xFFFFFFFF) >> 3)))
                                                                                                                                                            store32(v10 + 16, ((v28 - v7) + 257))
                                                                                                                                                            store32(v10 + 4, ((v36 - arg0) + 5))
                                                                                                                                                            arg0 = (v6 & 7)
                                                                                                                                                            store32(v14 + 64, (v6 & 7))
                                                                                                                                                            store32(v14 + 60, (v11 & ((-1 << arg0) ^ -1)))
                                                                                                                                                            arg2 = load32(v4 + 64)
                                                                                                                                                            v6 = load32(v4 + 60)
                                                                                                                                                            arg3 = load32(v10 + 4)
                                                                                                                                                            arg0 = load32(v10)
                                                                                                                                                            v13 = load32(v10 + 16)
                                                                                                                                                            v14 = load32(v10 + 12)
                                                                                                                                                            if (load32(v4 + 4) != 16191):
                                                                                                                                                                break
                                                                                                                                                            store32(v4 + 7112, -1)
                                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                                            continue
                                                                                                                                                            break
                                                                                                                                                        store32(v4 + 7112, 0)
                                                                                                                                                        v8 = arg2
                                                                                                                                                        v5 = arg3
                                                                                                                                                        arg1 = arg0
                                                                                                                                                        while True:  # block $label132
                                                                                                                                                            v19 = load32(v4 + 80)
                                                                                                                                                            v15 = ((-1 << load32(v4 + 88)) ^ -1)
                                                                                                                                                            v11 = (load32(v4 + 80) + ((v6 & ((-1 << load32(v4 + 88)) ^ -1)) << 2))
                                                                                                                                                            v9 = load8u((load32(v4 + 80) + ((v6 & ((-1 << load32(v4 + 88)) ^ -1)) << 2)) + 1)
                                                                                                                                                            if (u(load8u((load32(v4 + 80) + ((v6 & ((-1 << load32(v4 + 88)) ^ -1)) << 2)) + 1)) <= u(arg2)):
                                                                                                                                                                v7 = arg2
                                                                                                                                                                break
                                                                                                                                                            while True:  # $label134
                                                                                                                                                                if (v5 == 0):
                                                                                                                                                                    break
                                                                                                                                                                v9 = (load8u(arg1) << v8)
                                                                                                                                                                arg1 = (arg1 + 1)
                                                                                                                                                                v5 = (v5 - 1)
                                                                                                                                                                v7 = (v8 + 8)
                                                                                                                                                                v8 = (v8 + 8)
                                                                                                                                                                v6 = (v6 + v9)
                                                                                                                                                                v11 = (v19 + (((v6 + v9) & v15) << 2))
                                                                                                                                                                v9 = load8u((v19 + (((v6 + v9) & v15) << 2)) + 1)
                                                                                                                                                                if (u(v7) < u(load8u((v19 + (((v6 + v9) & v15) << 2)) + 1))):
                                                                                                                                                                    continue
                                                                                                                                                                break
                                                                                                                                                            break
                                                                                                                                                        v15 = load16u(v11 + 2)
                                                                                                                                                        while True:  # block $label135
                                                                                                                                                            v8 = load8u(v11)
                                                                                                                                                            if (u(((load8u(v11) - 1) & 255)) > u(14)):
                                                                                                                                                                v11 = v9
                                                                                                                                                                v9 = 0
                                                                                                                                                                arg0 = arg1
                                                                                                                                                                arg3 = v5
                                                                                                                                                                break
                                                                                                                                                            arg3 = v5
                                                                                                                                                            arg0 = arg1
                                                                                                                                                            while True:  # block $label136
                                                                                                                                                                arg2 = v7
                                                                                                                                                                v21 = ((-1 << (v8 + v9)) ^ -1)
                                                                                                                                                                v17 = (v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2))
                                                                                                                                                                v11 = load8u((v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)
                                                                                                                                                                if (u(v7) >= u((v9 + load8u((v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)))):
                                                                                                                                                                    v8 = v7
                                                                                                                                                                    break
                                                                                                                                                                while True:  # $label138
                                                                                                                                                                    if (arg3 == 0):
                                                                                                                                                                        break
                                                                                                                                                                    v11 = (load8u(arg0) << arg2)
                                                                                                                                                                    arg0 = (arg0 + 1)
                                                                                                                                                                    arg3 = (arg3 - 1)
                                                                                                                                                                    v8 = (arg2 + 8)
                                                                                                                                                                    arg2 = (arg2 + 8)
                                                                                                                                                                    v6 = (v6 + v11)
                                                                                                                                                                    v17 = (v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2))
                                                                                                                                                                    v11 = load8u((v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)
                                                                                                                                                                    if (u((v9 + load8u((v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1))) > u(v8)):
                                                                                                                                                                        continue
                                                                                                                                                                    break
                                                                                                                                                                break
                                                                                                                                                            v7 = (v8 - v9)
                                                                                                                                                            v6 = ((v6 & 0xFFFFFFFF) >> v9)
                                                                                                                                                            v8 = load8u(v17)
                                                                                                                                                            v15 = load16u(v17 + 2)
                                                                                                                                                            break
                                                                                                                                                        store32(v4 + 68, (v15 & 65535))
                                                                                                                                                        store32(v4 + 7112, (v9 + v11))
                                                                                                                                                        arg2 = (v7 - v11)
                                                                                                                                                        v6 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                        arg1 = (v8 & 255)
                                                                                                                                                        if ((v8 & 255) == 0):
                                                                                                                                                            store32(v4 + 4, 16205)
                                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                                            continue
                                                                                                                                                        if (arg1 & 32):
                                                                                                                                                            store32(v4 + 4, 16191)
                                                                                                                                                            store32(v4 + 7112, -1)
                                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                                            continue
                                                                                                                                                        if (arg1 & 64):
                                                                                                                                                            store32(v10 + 24, 4837)
                                                                                                                                                            store32(v4 + 4, 16209)
                                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                                            continue
                                                                                                                                                        store32(v4 + 4, 16201)
                                                                                                                                                        v8 = (arg1 & 15)
                                                                                                                                                        store32(v4 + 76, (arg1 & 15))
                                                                                                                                                        break
                                                                                                                                                    v9 = arg0
                                                                                                                                                    v7 = arg3
                                                                                                                                                    while True:  # block $label139
                                                                                                                                                        if (v8 == 0):
                                                                                                                                                            arg1 = load32(v4 + 68)
                                                                                                                                                            break
                                                                                                                                                        v5 = arg2
                                                                                                                                                        arg1 = arg0
                                                                                                                                                        if (u(arg2) < u(v8)):
                                                                                                                                                            while True:  # $label141
                                                                                                                                                                if (arg3 == 0):
                                                                                                                                                                    break
                                                                                                                                                                arg3 = (arg3 - 1)
                                                                                                                                                                v6 = ((load8u(arg1) << v5) + v6)
                                                                                                                                                                arg0 = (arg1 + 1)
                                                                                                                                                                arg1 = (arg1 + 1)
                                                                                                                                                                v5 = (v5 + 8)
                                                                                                                                                                if (u((v5 + 8)) < u(v8)):
                                                                                                                                                                    continue
                                                                                                                                                                break
                                                                                                                                                        store32(v4 + 7112, (load32(v4 + 7112) + v8))
                                                                                                                                                        arg1 = (load32(v4 + 68) + (v6 & ((-1 << v8) ^ -1)))
                                                                                                                                                        store32(v4 + 68, (load32(v4 + 68) + (v6 & ((-1 << v8) ^ -1))))
                                                                                                                                                        arg2 = (v5 - v8)
                                                                                                                                                        v6 = ((v6 & 0xFFFFFFFF) >> v8)
                                                                                                                                                        break
                                                                                                                                                    store32(v4 + 4, 16202)
                                                                                                                                                    store32(v4 + 7116, arg1)
                                                                                                                                                    break
                                                                                                                                                v8 = arg2
                                                                                                                                                v5 = arg3
                                                                                                                                                arg1 = arg0
                                                                                                                                                while True:  # block $label142
                                                                                                                                                    v19 = load32(v4 + 84)
                                                                                                                                                    v15 = ((-1 << load32(v4 + 92)) ^ -1)
                                                                                                                                                    v11 = (load32(v4 + 84) + ((v6 & ((-1 << load32(v4 + 92)) ^ -1)) << 2))
                                                                                                                                                    v9 = load8u((load32(v4 + 84) + ((v6 & ((-1 << load32(v4 + 92)) ^ -1)) << 2)) + 1)
                                                                                                                                                    if (u(load8u((load32(v4 + 84) + ((v6 & ((-1 << load32(v4 + 92)) ^ -1)) << 2)) + 1)) <= u(arg2)):
                                                                                                                                                        v7 = arg2
                                                                                                                                                        break
                                                                                                                                                    while True:  # $label144
                                                                                                                                                        if (v5 == 0):
                                                                                                                                                            break
                                                                                                                                                        v9 = (load8u(arg1) << v8)
                                                                                                                                                        arg1 = (arg1 + 1)
                                                                                                                                                        v5 = (v5 - 1)
                                                                                                                                                        v7 = (v8 + 8)
                                                                                                                                                        v8 = (v8 + 8)
                                                                                                                                                        v6 = (v6 + v9)
                                                                                                                                                        v11 = (v19 + (((v6 + v9) & v15) << 2))
                                                                                                                                                        v9 = load8u((v19 + (((v6 + v9) & v15) << 2)) + 1)
                                                                                                                                                        if (u(v7) < u(load8u((v19 + (((v6 + v9) & v15) << 2)) + 1))):
                                                                                                                                                            continue
                                                                                                                                                        break
                                                                                                                                                    break
                                                                                                                                                v15 = load16u(v11 + 2)
                                                                                                                                                while True:  # block $label145
                                                                                                                                                    v8 = load8u(v11)
                                                                                                                                                    if (u(load8u(v11)) >= u(16)):
                                                                                                                                                        v11 = v9
                                                                                                                                                        break
                                                                                                                                                    arg3 = v5
                                                                                                                                                    arg0 = arg1
                                                                                                                                                    while True:  # block $label146
                                                                                                                                                        arg2 = v7
                                                                                                                                                        v21 = ((-1 << (v8 + v9)) ^ -1)
                                                                                                                                                        v17 = (v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2))
                                                                                                                                                        v11 = load8u((v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)
                                                                                                                                                        if (u(v7) >= u((v9 + load8u((v19 + (((((v6 & ((-1 << (v8 + v9)) ^ -1)) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)))):
                                                                                                                                                            v8 = v7
                                                                                                                                                            break
                                                                                                                                                        while True:  # $label148
                                                                                                                                                            if (arg3 == 0):
                                                                                                                                                                break
                                                                                                                                                            v11 = (load8u(arg0) << arg2)
                                                                                                                                                            arg0 = (arg0 + 1)
                                                                                                                                                            arg3 = (arg3 - 1)
                                                                                                                                                            v8 = (arg2 + 8)
                                                                                                                                                            arg2 = (arg2 + 8)
                                                                                                                                                            v6 = (v6 + v11)
                                                                                                                                                            v17 = (v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2))
                                                                                                                                                            v11 = load8u((v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1)
                                                                                                                                                            if (u((v9 + load8u((v19 + ((((((v6 + v11) & v21) & 0xFFFFFFFF) >> v9) + v15) << 2)) + 1))) > u(v8)):
                                                                                                                                                                continue
                                                                                                                                                            break
                                                                                                                                                        arg1 = arg0
                                                                                                                                                        v5 = arg3
                                                                                                                                                        break
                                                                                                                                                    v7 = (v8 - v9)
                                                                                                                                                    v6 = ((v6 & 0xFFFFFFFF) >> v9)
                                                                                                                                                    v8 = load8u(v17)
                                                                                                                                                    v15 = load16u(v17 + 2)
                                                                                                                                                    break
                                                                                                                                                store32(load32(v4 + 7112) + 7112, ((load32(v4 + 7112) + v9) + v11))
                                                                                                                                                arg2 = (v7 - v11)
                                                                                                                                                v6 = ((v6 & 0xFFFFFFFF) >> v11)
                                                                                                                                                if (v8 & 64):
                                                                                                                                                    store32(v10 + 24, 4865)
                                                                                                                                                    store32(v4 + 4, 16209)
                                                                                                                                                    arg0 = arg1
                                                                                                                                                    arg3 = v5
                                                                                                                                                    v5 = load32(v4 + 4)
                                                                                                                                                    continue
                                                                                                                                                store32(v4 + 4, 16203)
                                                                                                                                                v9 = (v8 & 15)
                                                                                                                                                store32(v4 + 76, (v8 & 15))
                                                                                                                                                store32(v4 + 72, (v15 & 65535))
                                                                                                                                                break
                                                                                                                                            while True:  # block $label149
                                                                                                                                                if (v9 == 0):
                                                                                                                                                    arg0 = arg1
                                                                                                                                                    arg3 = v5
                                                                                                                                                    break
                                                                                                                                                v8 = arg2
                                                                                                                                                arg3 = v5
                                                                                                                                                v7 = arg1
                                                                                                                                                while True:  # block $label150
                                                                                                                                                    if (u(arg2) >= u(v9)):
                                                                                                                                                        arg0 = arg1
                                                                                                                                                        break
                                                                                                                                                    while True:  # $label152
                                                                                                                                                        if (arg3 == 0):
                                                                                                                                                            break
                                                                                                                                                        arg3 = (arg3 - 1)
                                                                                                                                                        v6 = ((load8u(v7) << v8) + v6)
                                                                                                                                                        arg0 = (v7 + 1)
                                                                                                                                                        v7 = (v7 + 1)
                                                                                                                                                        v8 = (v8 + 8)
                                                                                                                                                        if (u((v8 + 8)) < u(v9)):
                                                                                                                                                            continue
                                                                                                                                                        break
                                                                                                                                                    break
                                                                                                                                                store32(v4 + 7112, (load32(v4 + 7112) + v9))
                                                                                                                                                store32(v4 + 72, (load32(v4 + 72) + (v6 & ((-1 << v9) ^ -1))))
                                                                                                                                                arg2 = (v8 - v9)
                                                                                                                                                v6 = ((v6 & 0xFFFFFFFF) >> v9)
                                                                                                                                                break
                                                                                                                                            store32(v4 + 4, 16204)
                                                                                                                                            break
                                                                                                                                        if v13:
                                                                                                                                            break
                                                                                                                                        break
                                                                                                                                    v13 = 0
                                                                                                                                    break
                                                                                                                                    break
                                                                                                                                while True:  # block $label156
                                                                                                                                    arg1 = load32(v4 + 72)
                                                                                                                                    v5 = (v18 - v13)
                                                                                                                                    if (u(load32(v4 + 72)) > u((v18 - v13))):
                                                                                                                                        while True:  # block $label154
                                                                                                                                            arg1 = (arg1 - v5)
                                                                                                                                            if (u((arg1 - v5)) <= u(load32(v4 + 48))):
                                                                                                                                                break
                                                                                                                                            if (load32(v4 + 7108) == 0):
                                                                                                                                                break
                                                                                                                                            store32(v10 + 24, 4158)
                                                                                                                                            store32(v4 + 4, 16209)
                                                                                                                                            v5 = load32(v4 + 4)
                                                                                                                                            continue
                                                                                                                                            break
                                                                                                                                        while True:  # block $label155
                                                                                                                                            v5 = load32(v4 + 52)
                                                                                                                                            if (u(load32(v4 + 52)) < u(arg1)):
                                                                                                                                                arg1 = (arg1 - v5)
                                                                                                                                                break
                                                                                                                                            break
                                                                                                                                        v5 = (load32(v4 + 56) + (v5 - arg1))
                                                                                                                                        v8 = load32(v4 + 68)
                                                                                                                                        break
                                                                                                                                    v5 = (v14 - arg1)
                                                                                                                                    v8 = load32(v4 + 68)
                                                                                                                                    break
                                                                                                                                arg1 = load32(v4 + 68)
                                                                                                                                v7 = (arg1 if (u(arg1) < u(v13)) else v13)
                                                                                                                                store32(v4 + 68, (v8 - (arg1 if (u(arg1) < u(v13)) else v13)))
                                                                                                                                v9 = (v7 - 1)
                                                                                                                                v8 = 0
                                                                                                                                v11 = (v7 & 7)
                                                                                                                                if ((v7 & 7) == 0):
                                                                                                                                    break
                                                                                                                                arg1 = v7
                                                                                                                                while True:  # $label158
                                                                                                                                    store8(v14, load8u(v5))
                                                                                                                                    arg1 = (arg1 - 1)
                                                                                                                                    v14 = (v14 + 1)
                                                                                                                                    v5 = (v5 + 1)
                                                                                                                                    v8 = (v8 + 1)
                                                                                                                                    if ((v8 + 1) != v11):
                                                                                                                                        continue
                                                                                                                                    break
                                                                                                                                break
                                                                                                                                break
                                                                                                                            arg0 = (arg0 + arg3)
                                                                                                                            arg2 = (arg2 + (arg3 << 3))
                                                                                                                            break
                                                                                                                            break
                                                                                                                        arg0 = (arg1 + v5)
                                                                                                                        arg2 = (arg2 + (v5 << 3))
                                                                                                                        break
                                                                                                                        break
                                                                                                                    arg0 = (arg1 + v5)
                                                                                                                    arg2 = (v7 + (v5 << 3))
                                                                                                                    break
                                                                                                                    break
                                                                                                                arg0 = (arg0 + arg3)
                                                                                                                arg2 = (arg2 + (arg3 << 3))
                                                                                                                break
                                                                                                                break
                                                                                                            arg0 = (v7 + v9)
                                                                                                            arg2 = (arg2 + (v7 << 3))
                                                                                                            break
                                                                                                            break
                                                                                                        arg0 = (arg1 + v5)
                                                                                                        arg2 = (v7 + (v5 << 3))
                                                                                                        break
                                                                                                        break
                                                                                                    arg0 = (arg0 + arg3)
                                                                                                    arg2 = (arg2 + (arg3 << 3))
                                                                                                    break
                                                                                                    break
                                                                                                store32(v10 + 24, 2894)
                                                                                                store32(v4 + 4, 16209)
                                                                                                v5 = load32(v4 + 4)
                                                                                                continue
                                                                                                break
                                                                                            arg1 = v7
                                                                                            break
                                                                                        if (u(v9) >= u(7)):
                                                                                            while True:  # $label160
                                                                                                store8(v14, load8u(v5))
                                                                                                store8(v14 + 1, load8u(v5 + 1))
                                                                                                store8(v14 + 2, load8u(v5 + 2))
                                                                                                store8(v14 + 3, load8u(v5 + 3))
                                                                                                store8(v14 + 4, load8u(v5 + 4))
                                                                                                store8(v14 + 5, load8u(v5 + 5))
                                                                                                store8(v14 + 6, load8u(v5 + 6))
                                                                                                store8(v14 + 7, load8u(v5 + 7))
                                                                                                v14 = (v14 + 8)
                                                                                                v5 = (v5 + 8)
                                                                                                arg1 = (arg1 - 8)
                                                                                                if (arg1 - 8):
                                                                                                    continue
                                                                                                break
                                                                                        v13 = (v13 - v7)
                                                                                        if load32(v4 + 68):
                                                                                            break
                                                                                        store32(v4 + 4, 16200)
                                                                                        v5 = load32(v4 + 4)
                                                                                        continue
                                                                                        break
                                                                                    v5 = load32(v4 + 4)
                                                                                    continue
                                                                                    break
                                                                                arg3 = 0
                                                                                arg2 = arg1
                                                                                arg1 = v12
                                                                                break
                                                                                break
                                                                            arg1 = load32(v4 + 36)
                                                                            if load32(v4 + 36):
                                                                                store32(arg1 + 16, 0)
                                                                            arg2 = v5
                                                                            break
                                                                        store32(v4 + 4, 16185)
                                                                        break
                                                                    v8 = load32(v4 + 20)
                                                                    if (load32(v4 + 20) & 1024):
                                                                        v5 = load32(v4 + 68)
                                                                        arg1 = (load32(v4 + 68) if (u(arg3) > u(v5)) else arg3)
                                                                        if (load32(v4 + 68) if (u(arg3) > u(v5)) else arg3):
                                                                            while True:  # block $label161
                                                                                v7 = load32(v4 + 36)
                                                                                if (load32(v4 + 36) == 0):
                                                                                    break
                                                                                v11 = load32(v7 + 16)
                                                                                if (load32(v7 + 16) == 0):
                                                                                    break
                                                                                v9 = load32(v7 + 24)
                                                                                v5 = (load32(v7 + 20) - v5)
                                                                                if (u(load32(v7 + 24)) <= u((load32(v7 + 20) - v5))):
                                                                                    break
                                                                                v8 = load32(v4 + 20)
                                                                                break
                                                                            while True:  # block $label162
                                                                                if ((v8 & 512) == 0):
                                                                                    break
                                                                                if ((load8u(v4 + 12) & 4) == 0):
                                                                                    break
                                                                                store32(v4 + 28, func43(load32(v4 + 28), arg0, arg1))
                                                                                break
                                                                            v5 = (load32(v4 + 68) - arg1)
                                                                            store32(v4 + 68, (load32(v4 + 68) - arg1))
                                                                            arg3 = (arg3 - arg1)
                                                                            arg0 = (arg0 + arg1)
                                                                        if v5:
                                                                            break
                                                                    store32(v4 + 4, 16186)
                                                                    store32(v4 + 68, 0)
                                                                    break
                                                                while True:  # block $label167
                                                                    if (load8u(v4 + 21) & 8):
                                                                        v5 = 0
                                                                        if (arg3 == 0):
                                                                            break
                                                                        while True:  # $label165
                                                                            arg1 = load8u((arg0 + v5))
                                                                            while True:  # block $label164
                                                                                v8 = load32(v4 + 36)
                                                                                if (load32(v4 + 36) == 0):
                                                                                    break
                                                                                v9 = load32(v8 + 28)
                                                                                if (load32(v8 + 28) == 0):
                                                                                    break
                                                                                v7 = load32(v4 + 68)
                                                                                if (u(load32(v4 + 68)) >= u(load32(v8 + 32))):
                                                                                    break
                                                                                store32(v4 + 68, (v7 + 1))
                                                                                store8((v7 + v9), arg1)
                                                                                break
                                                                            v5 = (v5 + 1)
                                                                            if (arg1 if (u(arg3) > u((v5 + 1))) else 0):
                                                                                continue
                                                                            break
                                                                        while True:  # block $label166
                                                                            if ((load8u(v4 + 21) & 2) == 0):
                                                                                break
                                                                            if ((load8u(v4 + 12) & 4) == 0):
                                                                                break
                                                                            store32(v4 + 28, func43(load32(v4 + 28), arg0, v5))
                                                                            break
                                                                        arg0 = (arg0 + v5)
                                                                        arg3 = (arg3 - v5)
                                                                        if (arg1 == 0):
                                                                            break
                                                                        break
                                                                    arg1 = load32(v4 + 36)
                                                                    if (load32(v4 + 36) == 0):
                                                                        break
                                                                    store32(arg1 + 28, 0)
                                                                    break
                                                                store32(v4 + 4, 16187)
                                                                store32(v4 + 68, 0)
                                                                break
                                                            while True:  # block $label171
                                                                if (load8u(v4 + 21) & 16):
                                                                    v5 = 0
                                                                    if (arg3 == 0):
                                                                        break
                                                                    while True:  # $label169
                                                                        arg1 = load8u((arg0 + v5))
                                                                        while True:  # block $label168
                                                                            v8 = load32(v4 + 36)
                                                                            if (load32(v4 + 36) == 0):
                                                                                break
                                                                            v9 = load32(v8 + 36)
                                                                            if (load32(v8 + 36) == 0):
                                                                                break
                                                                            v7 = load32(v4 + 68)
                                                                            if (u(load32(v4 + 68)) >= u(load32(v8 + 40))):
                                                                                break
                                                                            store32(v4 + 68, (v7 + 1))
                                                                            store8((v7 + v9), arg1)
                                                                            break
                                                                        v5 = (v5 + 1)
                                                                        if (arg1 if (u(arg3) > u((v5 + 1))) else 0):
                                                                            continue
                                                                        break
                                                                    while True:  # block $label170
                                                                        if ((load8u(v4 + 21) & 2) == 0):
                                                                            break
                                                                        if ((load8u(v4 + 12) & 4) == 0):
                                                                            break
                                                                        store32(v4 + 28, func43(load32(v4 + 28), arg0, v5))
                                                                        break
                                                                    arg0 = (arg0 + v5)
                                                                    arg3 = (arg3 - v5)
                                                                    if (arg1 == 0):
                                                                        break
                                                                    break
                                                                arg1 = load32(v4 + 36)
                                                                if (load32(v4 + 36) == 0):
                                                                    break
                                                                store32(arg1 + 36, 0)
                                                                break
                                                            store32(v4 + 4, 16188)
                                                            break
                                                        v7 = load32(v4 + 20)
                                                        if (load32(v4 + 20) & 512):
                                                            while True:  # block $label172
                                                                if (u(arg2) > u(15)):
                                                                    v5 = arg0
                                                                    break
                                                                if (arg3 == 0):
                                                                    break
                                                                arg1 = (arg2 + 8)
                                                                v5 = (arg0 + 1)
                                                                v8 = (arg3 - 1)
                                                                v6 = ((load8u(arg0) << arg2) + v6)
                                                                if (u(arg2) > u(7)):
                                                                    arg3 = v8
                                                                    arg2 = arg1
                                                                    break
                                                                if (v8 == 0):
                                                                    arg0 = v5
                                                                    arg3 = 0
                                                                    arg2 = arg1
                                                                    arg1 = v12
                                                                    break
                                                                arg2 = (arg2 + 16)
                                                                v5 = (arg0 + 2)
                                                                arg3 = (arg3 - 2)
                                                                v6 = ((load8u(arg0 + 1) << arg1) + v6)
                                                                break
                                                            while True:  # block $label173
                                                                if ((load8u(v4 + 12) & 4) == 0):
                                                                    break
                                                                if (v6 == load16u(v4 + 28)):
                                                                    break
                                                                store32(v10 + 24, 4325)
                                                                store32(v4 + 4, 16209)
                                                                arg0 = v5
                                                                v5 = load32(v4 + 4)
                                                                continue
                                                                break
                                                            v6 = 0
                                                            arg2 = 0
                                                            arg0 = v5
                                                        arg1 = load32(v4 + 36)
                                                        if load32(v4 + 36):
                                                            store32(arg1 + 48, 1)
                                                            store32(arg1 + 44, (((v7 & 0xFFFFFFFF) >> 9) & 1))
                                                        arg1 = func43(0, 0, 0)
                                                        store32(v4 + 28, func43(0, 0, 0))
                                                        store32(v10 + 48, arg1)
                                                        store32(v4 + 4, 16191)
                                                        v5 = load32(v4 + 4)
                                                        continue
                                                        break
                                                    arg3 = 0
                                                    break
                                                v8 = v12
                                                break
                                            arg1 = v8
                                            break
                                            break
                                        if (v5 == 0):
                                            break
                                        if (load32(v4 + 20) == 0):
                                            break
                                        while True:  # block $label175
                                            if (u(arg2) > u(31)):
                                                arg1 = arg0
                                                break
                                            if (arg3 == 0):
                                                break
                                            v8 = (arg2 + 8)
                                            arg1 = (arg0 + 1)
                                            v7 = (arg3 - 1)
                                            v6 = ((load8u(arg0) << arg2) + v6)
                                            if (u(arg2) > u(23)):
                                                arg3 = v7
                                                arg2 = v8
                                                break
                                            if (v7 == 0):
                                                arg0 = arg1
                                                arg3 = 0
                                                arg2 = v8
                                                arg1 = v12
                                                break
                                            v7 = (arg2 + 16)
                                            arg1 = (arg0 + 2)
                                            v9 = (arg3 - 2)
                                            v6 = ((load8u(arg0 + 1) << v8) + v6)
                                            if (u(arg2) > u(15)):
                                                arg3 = v9
                                                arg2 = v7
                                                break
                                            if (v9 == 0):
                                                arg0 = arg1
                                                arg3 = 0
                                                arg2 = v7
                                                arg1 = v12
                                                break
                                            v8 = (arg2 + 24)
                                            arg1 = (arg0 + 3)
                                            v9 = (arg3 - 3)
                                            v6 = ((load8u(arg0 + 2) << v7) + v6)
                                            if (u(arg2) > u(7)):
                                                arg3 = v9
                                                arg2 = v8
                                                break
                                            if (v9 == 0):
                                                arg0 = arg1
                                                arg3 = 0
                                                arg2 = v8
                                                arg1 = v12
                                                break
                                            arg2 = (arg2 + 32)
                                            arg1 = (arg0 + 4)
                                            arg3 = (arg3 - 4)
                                            v6 = ((load8u(arg0 + 3) << v8) + v6)
                                            break
                                        v8 = 0
                                        while True:  # block $label176
                                            if ((v5 & 4) == 0):
                                                break
                                            if (v6 == load32(v4 + 32)):
                                                break
                                            store32(v10 + 24, 4114)
                                            store32(v4 + 4, 16209)
                                            arg0 = arg1
                                            v5 = load32(v4 + 4)
                                            continue
                                            break
                                        break
                                    arg0 = arg1
                                    arg2 = 0
                                    break
                                    break
                                arg3 = 0
                                arg1 = v12
                                break
                                break
                            v8 = v6
                            break
                        store32(v4 + 4, 16208)
                        arg1 = 1
                        v6 = v8
                        break
                    store32(v10 + 16, v13)
                    store32(v10 + 12, v14)
                    store32(v10 + 4, arg3)
                    store32(v10, arg0)
                    store32(v4 + 64, arg2)
                    store32(v4 + 60, v6)
                    while True:  # block $label182
                        while True:  # block $label178
                            if (load32(v4 + 44) == 0):
                                if (v13 == v18):
                                    break
                                if (u(load32(v4 + 4)) > u(16208)):
                                    break
                            while True:  # block $label181
                                arg2 = (v18 - v13)
                                while True:  # block $label180
                                    while True:  # block $label179
                                        arg0 = load32(v10 + 28)
                                        v12 = load32(load32(v10 + 28) + 56)
                                        if (load32(load32(v10 + 28) + 56) == 0):
                                            v5 = 1
                                            # call_indirect[load32(v10 + 32)]
                                            v12 = indirect_call(load32(v10 + 32))
                                            store32(1 + 56, indirect_call(load32(v10 + 32)))
                                            if (v12 == 0):
                                                break
                                        arg3 = load32(arg0 + 44)
                                        if (load32(arg0 + 44) == 0):
                                            store64(arg0 + 48, 0)
                                            arg3 = (1 << load32(arg0 + 40))
                                            store32(arg0 + 44, (1 << load32(arg0 + 40)))
                                        if (u(arg2) >= u(arg3)):
                                            store32(arg0 + 52, 0)
                                            break
                                        v5 = load32(arg0 + 52)
                                        arg3 = (arg3 - v5)
                                        v12 = (u(arg2) > u(arg3))
                                        arg3 = ((arg3 - v5) if (u(arg2) > u(arg3)) else arg2)
                                        if v12:
                                            arg2 = (arg2 - arg3)
                                            store32(arg0 + 52, arg2)
                                            break
                                        v5 = 0
                                        arg2 = (load32(arg0 + 52) + arg3)
                                        v12 = load32(arg0 + 44)
                                        store32(arg0 + 52, ((load32(arg0 + 52) + arg3) if (arg2 != load32(arg0 + 44)) else 0))
                                        arg2 = load32(arg0 + 48)
                                        if (u(load32(arg0 + 48)) >= u(v12)):
                                            break
                                        store32(arg0 + 48, (arg2 + arg3))
                                        break
                                    break
                                    break
                                store32(arg0 + 48, load32(arg0 + 44))
                                break
                            if 0:
                                break
                            v13 = load32(v10 + 16)
                            break
                        arg2 = load32(v10 + 4)
                        store32(v10 + 8, (load32(v10 + 8) + (v35 - arg2)))
                        arg0 = (v18 - v13)
                        store32(v10 + 20, ((v18 - v13) + load32(v10 + 20)))
                        store32(v4 + 32, (load32(v4 + 32) + arg0))
                        while True:  # block $label183
                            if ((load8u(v4 + 12) & 4) == 0):
                                break
                            if (v13 == v18):
                                break
                            arg3 = (load32(v10 + 12) - arg0)
                            v12 = load32(v4 + 28)
                            while True:  # block $label184
                                if load32(v4 + 20):
                                    break
                                break
                            arg0 = func89(v12, arg3, arg0)
                            store32(func43(v12, arg3, arg0) + 28, func89(v12, arg3, arg0))
                            store32(v10 + 48, arg0)
                            break
                        arg0 = load32(v4 + 4)
                        store32(v10 + 44, (((load32(v4 + 64) + ((load32(v4 + 8) != 0) << 6)) + ((load32(v4 + 4) == 16191) << 7)) + (256 if (arg0 == 16199) else ((arg0 == 16194) << 8))))
                        v23 = (((arg1 if arg1 else -5) if (v13 == v18) else arg1) if (arg2 == v35) else arg1)
                        break
                        break
                    store32(v4 + 4, 16210)
                    break
                v23 = -4
                break
            G.global0 = (v20 + 16)
            if (v23 == 0):
                arg0 = load32(v16 + 24)
                continue
            break
        store32(v24 + 12, (load32(v24 + 12) - (load32(v16 + 12) + v26)))
        arg0 = load32(v16 + 28)
        while True:  # block $label186
            if ((v16 + 7) != v29):
                store32(v33, arg0)
                break
            v22 = ((1 if (v23 == -5) else v22) if arg0 else v22)
            break
        while True:  # block $label187
            arg1 = (v16 + 8)
            if ((v16 + 8) == 0):
                break
            if (load32(arg1 + 32) == 0):
                break
            arg0 = load32(arg1 + 36)
            if (load32(arg1 + 36) == 0):
                break
            arg2 = load32(arg1 + 28)
            if (load32(arg1 + 28) == 0):
                break
            if (load32(arg2) != arg1):
                break
            if (u((load32(arg2 + 4) - 16180)) > u(31)):
                break
            arg3 = load32(arg2 + 56)
            if load32(arg2 + 56):
                # call_indirect[arg0]
                arg2 = load32(arg1 + 28)
                arg0 = load32(arg1 + 36)
            # call_indirect[arg0]
            store32(arg1 + 28, 0)
            break
        while True:  # block $label189
            while True:  # block $label188
                # br_table[(v23 + 5)]
                break
                break
            if (v22 != (0 - load32(v16 + 24))):
                break
            break
        break
    G.global0 = (v16 - -64)
    G.global0 = (v24 + 16)
    return indirect_call(arg0)

# ------------------------------------------------------------
# $func299
# ------------------------------------------------------------
def func299(arg0, arg1):
    v3 = load32(9142892)
    if load32(9142892):
        while True:  # $label9
            while True:  # block $label0
                v2 = load32(arg0 + 48)
                v4 = (v5 << 2)
                if (load32((load32(arg0 + 48) + (v5 << 2))) == 0):
                    if (load32((v2 + (v3 << 2))) == 0):
                        break
                    if (load32((load32(9142420) + v4)) == 0):
                        break
                v2 = 0
                v7 = load32(9561692)
                v8 = load32(arg0 + 32)
                if (u(load32(arg0 + 32)) <= u(3)):
                    while True:  # $label7
                        while True:  # block $label5
                            while True:  # block $label4
                                while True:  # block $label2
                                    while True:  # block $label3
                                        while True:  # block $label1
                                            # br_table[(v8 - 1)]
                                            break
                                            break
                                        v3 = ((v2 * 404) + 9568096)
                                        if load32(((v2 * 404) + 9568096) + 264):
                                            break
                                        if (load32(v3 + 268) == 1):
                                            break
                                        if (load32(v3 + 92) == 0):
                                            break
                                        if (load32(38456) == v2):
                                            break
                                        if (load32(38764) != v2):
                                            break
                                        break
                                        break
                                    if (load32(((v2 * 404) + 9568096) + 264) == 1):
                                        break
                                    break
                                    break
                                if load32(((v2 * 404) + 9568096) + 264):
                                    break
                                break
                            v6 = load32((((v7 + (v5 * 286704)) + (v2 << 2)) + 284636))
                            if (load32((((v7 + (v5 * 286704)) + (v2 << 2)) + 284636)) == 0):
                                break
                            v3 = 0
                            v4 = load32(v6 + 8)
                            if (load32(v6 + 8) == 0):
                                break
                            while True:  # $label6
                                v9 = load32((load32(v6) + (v3 << 2)))
                                if load32((load32(v6) + (v3 << 2))):
                                    # call_indirect[arg1]
                                    v4 = load32(v6 + 8)
                                v3 = (v3 + 1)
                                if (u((v3 + 1)) < u(v4)):
                                    continue
                                break
                            break
                        v2 = (v2 + 1)
                        if ((v2 + 1) != 255):
                            continue
                        break
                        break
                    raise RuntimeError('unreachable')
                v2 = load32((((v7 + (v5 * 286704)) + (v8 << 2)) + 284620))
                if (load32((((v7 + (v5 * 286704)) + (v8 << 2)) + 284620)) == 0):
                    break
                v3 = 0
                v4 = load32(v2 + 8)
                if (load32(v2 + 8) == 0):
                    break
                while True:  # $label8
                    v6 = load32((load32(v2) + (v3 << 2)))
                    if load32((load32(v2) + (v3 << 2))):
                        # call_indirect[arg1]
                        v4 = load32(v2 + 8)
                    v3 = (v3 + 1)
                    if (u((v3 + 1)) < u(v4)):
                        continue
                    break
                break
            v5 = (v5 + 1)
            v3 = load32(9142892)
            if (u((v5 + 1)) < u(load32(9142892))):
                continue
            break

# ------------------------------------------------------------
# $func300
# ------------------------------------------------------------
def func300(arg0, arg1, arg2):
    while True:  # block $label0
        v6 = load32(9142892)
        if (load32(9142892) == 0):
            break
        v11 = load32(arg1)
        v12 = (load32(arg1) + (v6 << 2))
        v13 = load16u(arg2 + 114)
        v14 = load16u(arg2 + 112)
        v15 = load32(arg2 + 28)
        v16 = load32(9671128)
        v17 = load32(9561692)
        v18 = load32(9142420)
        arg1 = 2147483647
        if (u(arg0) <= u(3)):
            v7 = load32(38764)
            v8 = load32(38456)
            v9 = (arg0 - 1)
            while True:  # $label10
                while True:  # block $label1
                    arg0 = (v3 << 2)
                    if (load32((v11 + (v3 << 2))) == 0):
                        if (load32(v12) == 0):
                            break
                        if (load32((arg0 + v18)) == 0):
                            break
                    arg0 = 0
                    while True:  # $label9
                        while True:  # block $label6
                            while True:  # block $label5
                                while True:  # block $label2
                                    while True:  # block $label3
                                        while True:  # block $label4
                                            # br_table[v9]
                                            break
                                            break
                                        if (load32(((arg0 * 404) + 9568096) + 264) == 1):
                                            break
                                        break
                                        break
                                    if (load32(((arg0 * 404) + 9568096) + 264) == 0):
                                        break
                                    break
                                    break
                                arg2 = ((arg0 * 404) + 9568096)
                                if load32(((arg0 * 404) + 9568096) + 264):
                                    break
                                if (load32(arg2 + 268) == 1):
                                    break
                                if (load32(arg2 + 92) == 0):
                                    break
                                if (arg0 == v8):
                                    break
                                if (arg0 == v7):
                                    break
                                break
                            arg2 = load32((((v17 + (v3 * 286704)) + (arg0 << 2)) + 284636))
                            if (load32((((v17 + (v3 * 286704)) + (arg0 << 2)) + 284636)) == 0):
                                break
                            v10 = load32(arg2 + 8)
                            if (load32(arg2 + 8) == 0):
                                break
                            v19 = load32(arg2)
                            arg2 = 0
                            while True:  # $label8
                                while True:  # block $label7
                                    v4 = load32((v19 + (arg2 << 2)))
                                    if (load32((v19 + (arg2 << 2))) == 0):
                                        break
                                    v4 = (v16 + (v4 * 132))
                                    v20 = load32((v16 + (v4 * 132)) + 28)
                                    if (load32((v16 + (v4 * 132)) + 28) == v15):
                                        break
                                    v21 = ((load16u(v4 + 114) - v13) << 1)
                                    v4 = ((load16u(v4 + 112) - v14) << 1)
                                    v4 = ((((load16u(v4 + 114) - v13) << 1) * v21) + (((load16u(v4 + 112) - v14) << 1) * v4))
                                    v4 = (arg1 > v4)
                                    arg1 = (((((load16u(v4 + 114) - v13) << 1) * v21) + (((load16u(v4 + 112) - v14) << 1) * v4)) if (arg1 > v4) else arg1)
                                    v5 = (v20 if v4 else v5)
                                    break
                                arg2 = (arg2 + 1)
                                if ((arg2 + 1) != v10):
                                    continue
                                break
                            break
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != 255):
                            continue
                        break
                    break
                v3 = (v3 + 1)
                if ((v3 + 1) != v6):
                    continue
                break
            break
        v4 = ((arg0 - 4) << 2)
        arg0 = 0
        while True:  # $label14
            while True:  # block $label11
                arg2 = (arg0 << 2)
                if (load32((v11 + (arg0 << 2))) == 0):
                    if (load32(v12) == 0):
                        break
                    if (load32((arg2 + v18)) == 0):
                        break
                arg2 = load32((((v17 + (arg0 * 286704)) + v4) + 284636))
                if (load32((((v17 + (arg0 * 286704)) + v4) + 284636)) == 0):
                    break
                v7 = load32(arg2 + 8)
                if (load32(arg2 + 8) == 0):
                    break
                v8 = load32(arg2)
                arg2 = 0
                while True:  # $label13
                    while True:  # block $label12
                        v3 = load32((v8 + (arg2 << 2)))
                        if (load32((v8 + (arg2 << 2))) == 0):
                            break
                        v3 = (v16 + (v3 * 132))
                        v9 = load32((v16 + (v3 * 132)) + 28)
                        if (load32((v16 + (v3 * 132)) + 28) == v15):
                            break
                        v10 = ((load16u(v3 + 114) - v13) << 1)
                        v3 = ((load16u(v3 + 112) - v14) << 1)
                        v3 = ((((load16u(v3 + 114) - v13) << 1) * v10) + (((load16u(v3 + 112) - v14) << 1) * v3))
                        v3 = (arg1 > v3)
                        arg1 = (((((load16u(v3 + 114) - v13) << 1) * v10) + (((load16u(v3 + 112) - v14) << 1) * v3)) if (arg1 > v3) else arg1)
                        v5 = (v9 if v3 else v5)
                        break
                    arg2 = (arg2 + 1)
                    if ((arg2 + 1) != v7):
                        continue
                    break
                break
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != v6):
                continue
            break
        break
    return v5

# ------------------------------------------------------------
# $func301
# ------------------------------------------------------------
def func301(arg0, arg1, arg2, arg3):
    v7 = (load32(9142892) * arg2)
    v21 = load32(9142440)
    v13 = (load32(9142440) + 2)
    v23 = ((load32(9142440) + 2) << 1)
    v8 = load32(9215884)
    v15 = load32(38564)
    v16 = load32(38620)
    v17 = load32(38560)
    v9 = load32(9143004)
    v18 = load32(38500)
    v10 = load32(9671128)
    v19 = load32(9142840)
    arg2 = 0
    while True:  # block $label3
        while True:  # $label7
            while True:  # block $label0
                v22 = arg2
                v4 = (arg2 << 2)
                arg2 = (load32((((arg2 << 2) | 4) + 8611904)) + arg1)
                if (u(v21) <= u((load32((((arg2 << 2) | 4) + 8611904)) + arg1))):
                    break
                v4 = (load32((v4 + 8611904)) + arg0)
                if (u(v21) <= u((load32((v4 + 8611904)) + arg0))):
                    break
                if ((arg2 | v4) < 0):
                    break
                while True:  # block $label1
                    v11 = (v4 + 1)
                    v14 = (arg2 + 1)
                    arg2 = load32((v19 + (((v4 + 1) + ((arg2 + 1) * v13)) << 2)))
                    if (u(load32((v19 + (((v4 + 1) + ((arg2 + 1) * v13)) << 2)))) < u(3)):
                        break
                    v4 = (v10 + (arg2 * 132))
                    v6 = load8u((v10 + (arg2 * 132)) + 122)
                    v12 = ((load8u((v10 + (arg2 * 132)) + 122) * 404) + 9568096)
                    if (load32(((load8u((v10 + (arg2 * 132)) + 122) * 404) + 9568096) + 340) == 0):
                        break
                    if (v6 == v18):
                        break
                    v5 = load16u(v4 + 110)
                    while True:  # block $label2
                        v20 = load16u(v4 + 120)
                        if load16u(v4 + 120):
                        else:
                        if (load8u(((v20 if load8u((v9 + (v5 + v7))) else v5) + (v5 + v7))) == 0):
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
                    if (load32(v12 + 264) == 2):
                        break
                    if (load32(v12 + 188) != 55):
                        break
                    if (v6 == v17):
                        break
                    if (v6 == v16):
                        break
                    if (v6 == v15):
                        break
                    if (((arg3 == -1) | (arg3 == v6)) == 0):
                        break
                    v5 = load32(v4 + 104)
                    if (load32(v4 + 104) == 0):
                        break
                    v5 = load32((v10 + (v5 * 132)) + 44)
                    if (load32((v8 + (load32((v10 + (v5 * 132)) + 44) << 4)) + 4) != 40):
                        break
                    if (load32((v8 + ((v5 << 4) | 12))) != load32(v4 + 28)):
                        break
                    break
                while True:  # block $label4
                    arg2 = load32((v19 + ((v11 + ((v13 + v14) * v13)) << 2)))
                    if (u(load32((v19 + ((v11 + ((v13 + v14) * v13)) << 2)))) < u(3)):
                        break
                    v4 = (v10 + (arg2 * 132))
                    v6 = load8u((v10 + (arg2 * 132)) + 122)
                    v12 = ((load8u((v10 + (arg2 * 132)) + 122) * 404) + 9568096)
                    if (load32(((load8u((v10 + (arg2 * 132)) + 122) * 404) + 9568096) + 340) == 0):
                        break
                    if (v6 == v18):
                        break
                    v5 = load16u(v4 + 110)
                    while True:  # block $label5
                        v20 = load16u(v4 + 120)
                        if load16u(v4 + 120):
                        else:
                        if load8u(((v20 if load8u((v9 + (v5 + v7))) else v5) + (v5 + v7))):
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
                    if (load32(v12 + 264) == 2):
                        break
                    if (load32(v12 + 188) != 55):
                        break
                    if (v6 == v17):
                        break
                    if (v6 == v16):
                        break
                    if (v6 == v15):
                        break
                    if (((arg3 == -1) | (arg3 == v6)) == 0):
                        break
                    v5 = load32(v4 + 104)
                    if (load32(v4 + 104) == 0):
                        break
                    v5 = load32((v10 + (v5 * 132)) + 44)
                    if (load32((v8 + (load32((v10 + (v5 * 132)) + 44) << 4)) + 4) != 40):
                        break
                    if (load32((v8 + ((v5 << 4) | 12))) != load32(v4 + 28)):
                        break
                    break
                arg2 = load32((v19 + ((v11 + ((v14 + v23) * v13)) << 2)))
                if (u(load32((v19 + ((v11 + ((v14 + v23) * v13)) << 2)))) < u(3)):
                    break
                v4 = (v10 + (arg2 * 132))
                v5 = load8u((v10 + (arg2 * 132)) + 122)
                v11 = ((load8u((v10 + (arg2 * 132)) + 122) * 404) + 9568096)
                if (load32(((load8u((v10 + (arg2 * 132)) + 122) * 404) + 9568096) + 340) == 0):
                    break
                if (v5 == v18):
                    break
                v6 = load16u(v4 + 110)
                while True:  # block $label6
                    v14 = load16u(v4 + 120)
                    if load16u(v4 + 120):
                    else:
                    if load8u(((v14 if load8u((v9 + (v6 + v7))) else v6) + (v6 + v7))):
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
                if (load32(v11 + 264) == 2):
                    break
                if (load32(v11 + 188) != 55):
                    break
                if (v5 == v17):
                    break
                if (v5 == v16):
                    break
                if (v5 == v15):
                    break
                if (((arg3 == -1) | (arg3 == v5)) == 0):
                    break
                v5 = load32(v4 + 104)
                if (load32(v4 + 104) == 0):
                    break
                v5 = load32((v10 + (v5 * 132)) + 44)
                if (load32((v8 + (load32((v10 + (v5 * 132)) + 44) << 4)) + 4) != 40):
                    break
                if (load32((v8 + ((v5 << 4) | 12))) != load32(v4 + 28)):
                    break
                break
            arg2 = (v22 + 2)
            if (u(v22) < u(5198)):
                continue
            break
        arg2 = 0
        break
    return arg2

# ------------------------------------------------------------
# $cc
# Export: cc
# ------------------------------------------------------------
def cc():
    """Exported as cc."""
    while True:  # block $label0
        v3 = load32(9671136)
        v12 = load8u(9671158)
        v14 = (3 if load8u(9671158) else 2)
        v10 = load8u(9671157)
        v11 = (load8u(9671157) == 0)
        v2 = load32(9142440)
        if (u(load32(9671136)) <= u((((3 if load8u(9671158) else 2) - (load8u(9671157) == 0)) * (load32(9142440) * v2)))):
            if (u(v3) < u(4)):
                break
            v6 = load32(38448)
            v7 = load32(9671128)
            v1 = 3
            while True:  # $label2
                while True:  # block $label1
                    v4 = (v7 + (v1 * 132))
                    if (load8u((v7 + (v1 * 132)) + 125) == 3):
                        break
                    if (v6 == load8u(v4 + 122)):
                        break
                    v4 = load16u(v4 + 112)
                    v0 = (((((load16u(v4 + 114) + (v2 * load16u(v4 + 112))) * v2) + v4) * v1) + v0)
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v3):
                    continue
                break
            break
        if (v2 == 0):
            break
        v7 = load32(9142840)
        v6 = (v2 + 2)
        v8 = (0 if v10 else (v2 + 2))
        v15 = (v2 & -2)
        v13 = (v2 & 1)
        v16 = (v2 - 1)
        while True:  # $label5
            v4 = v1
            v9 = (v1 * v2)
            v1 = (v1 + 1)
            v3 = 0
            v5 = 0
            if v16:
                while True:  # $label3
                    v18 = (v3 | 1)
                    v17 = load32((v7 + ((v1 + (((v3 | 1) + v8) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 | 1) + v8) * v6)) << 2))):
                        v0 = ((v17 * (((v3 + v9) * v2) + v4)) + v0)
                    v3 = (v3 + 2)
                    v17 = load32((v7 + ((v1 + (((v3 + 2) + v8) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 + 2) + v8) * v6)) << 2))):
                        v0 = ((v17 * (((v9 + v18) * v2) + v4)) + v0)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v15):
                        continue
                    break
            while True:  # block $label4
                if (v13 == 0):
                    break
                v5 = load32((v7 + ((v1 + (((v3 + v8) + 1) * v6)) << 2)))
                if (load32((v7 + ((v1 + (((v3 + v8) + 1) * v6)) << 2))) == 0):
                    break
                v0 = ((v5 * (((v3 + v9) * v2) + v4)) + v0)
                break
            if (v1 != v2):
                continue
            break
        if ((v10 | v12) == 0):
            break
        v12 = (v2 & -2)
        v15 = (v2 & 1)
        v8 = (v6 << v11)
        v1 = 0
        while True:  # $label8
            v4 = v1
            v9 = (v1 * v2)
            v1 = (v1 + 1)
            v3 = 0
            v5 = 0
            if v16:
                while True:  # $label6
                    v11 = (v3 | 1)
                    v13 = load32((v7 + ((v1 + (((v3 | 1) + v8) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 | 1) + v8) * v6)) << 2))):
                        v0 = ((v13 * (((v3 + v9) * v2) + v4)) + v0)
                    v3 = (v3 + 2)
                    v13 = load32((v7 + ((v1 + (((v3 + 2) + v8) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 + 2) + v8) * v6)) << 2))):
                        v0 = ((v13 * (((v9 + v11) * v2) + v4)) + v0)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v12):
                        continue
                    break
            while True:  # block $label7
                if (v15 == 0):
                    break
                v5 = load32((v7 + ((v1 + (((v3 + v8) + 1) * v6)) << 2)))
                if (load32((v7 + ((v1 + (((v3 + v8) + 1) * v6)) << 2))) == 0):
                    break
                v0 = ((v5 * (((v3 + v9) * v2) + v4)) + v0)
                break
            if (v1 != v2):
                continue
            break
        v1 = (2 if v10 else 3)
        if ((2 if v10 else 3) == v14):
            break
        v9 = (v2 & -2)
        v12 = (v2 & 1)
        v10 = (v1 * v6)
        v1 = 0
        while True:  # $label11
            v4 = v1
            v8 = (v1 * v2)
            v1 = (v1 + 1)
            v3 = 0
            v5 = 0
            if v16:
                while True:  # $label9
                    v14 = (v3 | 1)
                    v11 = load32((v7 + ((v1 + (((v3 | 1) + v10) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 | 1) + v10) * v6)) << 2))):
                        v0 = ((v11 * (((v3 + v8) * v2) + v4)) + v0)
                    v3 = (v3 + 2)
                    v11 = load32((v7 + ((v1 + (((v3 + 2) + v10) * v6)) << 2)))
                    if load32((v7 + ((v1 + (((v3 + 2) + v10) * v6)) << 2))):
                        v0 = ((v11 * (((v8 + v14) * v2) + v4)) + v0)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v9):
                        continue
                    break
            while True:  # block $label10
                if (v12 == 0):
                    break
                v5 = load32((v7 + ((v1 + (((v3 + v10) + 1) * v6)) << 2)))
                if (load32((v7 + ((v1 + (((v3 + v10) + 1) * v6)) << 2))) == 0):
                    break
                v0 = ((v5 * (((v3 + v8) * v2) + v4)) + v0)
                break
            if (v1 != v2):
                continue
            break
        break
    return v0

# ------------------------------------------------------------
# $func304
# ------------------------------------------------------------
def func304(arg0):
    while True:  # block $label2
        while True:  # block $label1
            while True:  # block $label0
                # br_table[(load8u(arg0 + 125) - 4)]
                break
                break
            return
            break
        store8(arg0 + 125, 0)
        v3 = load32(9561692)
        v5 = load16u(arg0 + 110)
        v2 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
        v7 = load32(9215884)
        v1 = load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12)
        store32((((load32(9561692) + (load16u(arg0 + 110) * 286704)) + (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 12) << 2)) + 282828), 0)
        v1 = ((v1 * 404) + 9568164)
        v4 = load32(v2 + 283848)
        if (load32(v2 + 283848) != 2147483647):
            store32((v2 + 283848), (load32(v1) + v4))
        v2 = (v2 + 283852)
        v4 = load32((v2 + 283852))
        if (load32((v2 + 283852)) != 2147483647):
            store32(v2, (load32(v1 + 4) + v4))
        v2 = (v3 + (v5 * 286704))
        v4 = ((v3 + (v5 * 286704)) + 283856)
        v6 = load32(((v3 + (v5 * 286704)) + 283856))
        if (load32(((v3 + (v5 * 286704)) + 283856)) != 2147483647):
            store32(v4, (load32(v1 + 8) + v6))
        v2 = (v2 + 283860)
        v4 = load32((v2 + 283860))
        if (load32((v2 + 283860)) != 2147483647):
            store32(v2, (load32(v1 + 12) + v4))
        v2 = (v3 + (v5 * 286704))
        v3 = ((v3 + (v5 * 286704)) + 281692)
        store32(((v3 + (v5 * 286704)) + 281692), (load32(v3) - load32(v1)))
        v3 = (v2 + 281696)
        store32((v2 + 281696), (load32(v3) - load32(v1 + 4)))
        v3 = (v2 + 281700)
        store32((v2 + 281700), (load32(v3) - load32(v1 + 8)))
        v3 = load32(v1 + 12)
        v1 = 1
        store8(v2 + 286701, 1)
        v5 = (v2 + 281704)
        store32((v2 + 281704), (load32(v5) - v3))
        while True:  # block $label3
            v3 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v6 = (v3 - 1)
            v8 = ((v3 - 1) & 1)
            v2 = (load32(v2 + 283908) * v3)
            v5 = load32(9561692)
            v4 = load32(9143016)
            if (v3 != 2):
                v6 = (v6 & -2)
                v3 = 0
                while True:  # $label4
                    if load8u((v4 + (v1 + v2))):
                        store8((v5 + (v1 * 286704)) + 286701, 1)
                    v9 = (v1 + 1)
                    if load8u((v4 + ((v1 + 1) + v2))):
                        store8((v5 + (v9 * 286704)) + 286701, 1)
                    v1 = (v1 + 2)
                    v3 = (v3 + 2)
                    if ((v3 + 2) != v6):
                        continue
                    break
            if (v8 == 0):
                break
            if (load8u((v4 + (v1 + v2))) == 0):
                break
            store8((v5 + (v1 * 286704)) + 286701, 1)
            break
        v1 = load32(arg0 + 44)
        if load32(arg0 + 44):
            store32((v7 + (v1 << 4)), 0)
        store32(arg0 + 44, 0)
        while True:  # block $label5
            if (load32(arg0 + 92) == 0):
                break
            v1 = load8u(9147141)
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
        return
        break
    while True:  # block $label7
        while True:  # block $label9
            while True:  # block $label8
                while True:  # block $label6
                    v6 = load32(9215884)
                    v1 = load32(arg0 + 44)
                    v2 = load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4)
                    # br_table[load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4)]
                    break
                    break
                store8(arg0 + 123, 0)
                store32(arg0 + 32, 0)
                store32(arg0 + 116, load32(arg0 + 112))
                arg0 = load32(arg0 + 20)
                if (load32(arg0 + 20) == 0):
                    break
                if (u(load32(arg0 + 8)) < u(3)):
                    break
                if (u((load32(load32(arg0)) - 1)) > u(1)):
                    break
                store32(arg0 + 8, 0)
                return
                break
            store8(arg0 + 129, 11)
            return
            break
        if (v2 != 34):
            break
        while True:  # block $label10
            v5 = load32(9561692)
            v4 = load16u(arg0 + 110)
            v2 = (load32(9561692) + (load16u(arg0 + 110) * 286704))
            v3 = load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 283848)
            if (load32((load32(9561692) + (load16u(arg0 + 110) * 286704)) + 283848) == 2147483647):
                break
            store32((v2 + 283848), (load16u((v6 + ((v1 << 4) | 12)) + 2) + v3))
            v1 = 1
            store8(v2 + 286701, 1)
            v3 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v8 = (v3 - 1)
            v9 = ((v3 - 1) & 1)
            v5 = (load32((v5 + (v4 * 286704)) + 283908) * v3)
            v4 = load32(9561692)
            v7 = load32(9143016)
            if (v3 != 2):
                v3 = (v8 & -2)
                while True:  # $label11
                    if load8u((v7 + (v1 + v5))):
                        store8((v4 + (v1 * 286704)) + 286701, 1)
                    v8 = (v1 + 1)
                    if load8u((v7 + ((v1 + 1) + v5))):
                        store8((v4 + (v8 * 286704)) + 286701, 1)
                    v1 = (v1 + 2)
                    v10 = (v10 + 2)
                    if ((v10 + 2) != v3):
                        continue
                    break
            if (v9 == 0):
                break
            if (load8u((v7 + (v1 + v5))) == 0):
                break
            store8((v4 + (v1 * 286704)) + 286701, 1)
            break
        store32(v2 + 283912, (load32(v2 + 283912) - 1))
        v1 = load32(arg0 + 44)
        if load32(arg0 + 44):
            store32((v6 + (v1 << 4)), 0)
        store32(arg0 + 44, 0)
        if (load32(arg0 + 92) == 0):
            break
        v1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32(arg0 + 28)):
                break
        break

# ------------------------------------------------------------
# $func307
# ------------------------------------------------------------
def func307(arg0):
    store32(arg0, 32988)
    v1 = (load32(arg0 + 4) - 12)
    # TODO: i32.atomic.rmw.add []
    if ((-1 - 1) < 0):
    return arg0

# ------------------------------------------------------------
# $func308
# ------------------------------------------------------------
def func308(arg0, arg1):
    v4 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # block $label0
        v7 = (v4 + 32)
        v3 = (v4 + 32)
        v2 = (v4 + 21)
        v5 = ((v4 + 32) - (v4 + 21))
        if (((v4 + 32) - (v4 + 21)) <= 9):
            v6 = (((32 - clz((arg1 | 1))) * 1233) >> 12)
            if (v5 < ((((32 - clz((arg1 | 1))) * 1233) >> 12) + (u(load32(((v6 << 2) + 32256))) <= u(arg1)))):
                break
        while True:  # block $label1
            if (u(arg1) <= u(999999)):
                if (u(arg1) <= u(9999)):
                    if (u(arg1) <= u(99)):
                        if (u(arg1) <= u(9)):
                            store8(v2, (arg1 + 48))
                            break
                        break
                    if (u(arg1) <= u(999)):
                        # TODO: i32.div_u []
                        v3 = 100
                        store8(arg1, (100 + 48))
                        break
                    break
                if (u(arg1) <= u(99999)):
                    # TODO: i32.div_u []
                    v3 = 10000
                    store8(arg1, (10000 + 48))
                    break
                break
            if (u(arg1) <= u(99999999)):
                if (u(arg1) <= u(9999999)):
                    # TODO: i32.div_u []
                    v3 = 1000000
                    store8(arg1, (1000000 + 48))
                    break
                break
            if (u(arg1) <= u(999999999)):
                # TODO: i32.div_u []
                v3 = 100000000
                store8(arg1, (100000000 + 48))
                break
            # TODO: i32.div_u []
            v3 = 100000000
            break
        v3 = func213(func104(arg1, 100000000), (arg1 - (v3 * 100000000)))
        break
    store32(v2 + 16, 0)
    store32(v4 + 12, v3)
    v5 = load32(v4 + 12)
    v6 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label4
        v3 = (v5 - v2)
        if (u((v5 - v2)) <= u(2147483631)):
            while True:  # block $label2
                if (u(v3) < u(11)):
                    store8(arg0 + 11, ((load8u(arg0 + 11) & 128) | v3))
                    store8(arg0 + 11, (load8u(arg0 + 11) & 127))
                    arg1 = arg0
                    break
                if (u(v3) >= u(11)):
                    arg1 = ((v3 + 16) & -16)
                    arg1 = (arg1 - 1)
                else:
                func314(arg0, (((v3 + 16) & -16) if (arg1 == 11) else (arg1 - 1)), (10 + 1))
                arg1 = load32(v4 + 8)
                store32(arg0, load32(v4 + 8))
                store32(arg0 + 8, ((load32(arg0 + 8) & -2147483648) | (load32(v4 + 12) & 2147483647)))
                store32(arg0 + 8, (load32(arg0 + 8) | -2147483648))
                store32(arg0 + 4, v3)
                break
            while True:  # $label3
                if (v2 != v5):
                    store8(arg1, load8u(v2))
                    arg1 = (arg1 + 1)
                    v2 = (v2 + 1)
                    continue
                break
            store8(v4 + 7, 0)
            store8(arg1, load8u(v4 + 7))
            G.global0 = (v4 + 16)
            break
        func212()
        raise RuntimeError('unreachable')
        break
    G.global0 = (v6 + 16)
    G.global0 = v7
    return (v4 + 8)

# ------------------------------------------------------------
# $func309
# ------------------------------------------------------------
def func309(arg0, arg1, arg2):
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v4 + 12, arg0)
    store32(v4 + 8, (arg0 + arg1))
    store32(v3 + 24, load32(v4 + 12))
    store32(v3 + 28, load32(v4 + 8))
    G.global0 = (v4 + 16)
    v4 = load32(v3 + 24)
    v7 = load32(v3 + 28)
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v6 = (v7 - v4)
    if (v4 != v7):
        # TODO: memory.copy []
    store32(arg1 + 12, (v4 + v6))
    store32(arg1 + 8, (arg2 + v6))
    store32(v3 + 16, load32(arg1 + 12))
    store32(v3 + 20, load32(arg1 + 8))
    G.global0 = (arg1 + 16)
    store32(v3 + 12, (arg0 + (load32(v3 + 16) - arg0)))
    store32(v3 + 8, (arg2 + (load32(v3 + 20) - arg2)))
    store32(v5 + 8, load32(v3 + 12))
    store32(v5 + 12, load32(v3 + 8))
    G.global0 = (v3 + 32)
    arg0 = load32(v5 + 12)
    G.global0 = (v5 + 16)
    return arg0

# ------------------------------------------------------------
# $func310
# ------------------------------------------------------------
def func310(arg0, arg1, arg2):
    v5 = (arg2 - arg1)
    v6 = ((arg2 - arg1) >> 2)
    v3 = load32(arg0 + 8)
    v4 = load32(arg0)
    if (u(((arg2 - arg1) >> 2)) <= u(((load32(arg0 + 8) - load32(arg0)) >> 2))):
        v5 = (load32(arg0 + 4) - v4)
        v3 = (arg1 + (load32(arg0 + 4) - v4))
        v8 = (v5 >> 2)
        v5 = ((arg1 + (load32(arg0 + 4) - v4)) if (u(v6) > u((v5 >> 2))) else arg2)
        v7 = (((arg1 + (load32(arg0 + 4) - v4)) if (u(v6) > u((v5 >> 2))) else arg2) - arg1)
        if (arg1 != v5):
            # TODO: memory.copy []
        if (u(v6) > u(v8)):
            arg1 = load32(arg0 + 4)
            if (arg2 != v5):
                while True:  # $label0
                    store32(arg1, load32(v3))
                    arg1 = (arg1 + 4)
                    v3 = (v3 + 4)
                    if ((v3 + 4) != arg2):
                        continue
                    break
            store32(arg0 + 4, arg1)
            return v7
        store32(arg0 + 4, (v4 + v7))
        return arg1
    if v4:
        store32(arg0 + 4, v4)
        store32(arg0 + 8, 0)
        store64(arg0, 0)
        v3 = 0
    while True:  # block $label1
        if (v5 < 0):
            break
        v4 = (v3 >> 1)
        v3 = (1073741823 if (u(v3) >= u(2147483644)) else ((v3 >> 1) if (u(v4) > u(v6)) else v6))
        if (u((1073741823 if (u(v3) >= u(2147483644)) else ((v3 >> 1) if (u(v4) > u(v6)) else v6))) >= u(1073741824)):
            break
        v4 = (v3 << 2)
        v3 = func26((v3 << 2))
        store32(arg0 + 4, func26((v3 << 2)))
        store32(arg0, v3)
        store32(arg0 + 8, (v3 + v4))
        if (arg1 != arg2):
            arg0 = (((v5 - 4) & -4) + 4)
            # TODO: memory.copy []
        else:
        store32((arg0 + v3) + 4, v3)
        return (((v5 - 4) & -4) + 4)
        break
    func42()
    raise RuntimeError('unreachable')
    return arg1

# ------------------------------------------------------------
# $func311
# ------------------------------------------------------------
def func311(arg0, arg1, arg2):
    v6 = (arg2 - arg1)
    v5 = ((arg2 - arg1) // 196)
    v3 = load32(arg0 + 8)
    v4 = load32(arg0)
    if (u(((arg2 - arg1) // 196)) <= u(((load32(arg0 + 8) - load32(arg0)) // 196))):
        v6 = ((load32(arg0 + 4) - v4) // 196)
        v3 = (arg1 + (((load32(arg0 + 4) - v4) // 196) * 196))
        v7 = ((arg1 + (((load32(arg0 + 4) - v4) // 196) * 196)) if (u(v5) > u(v6)) else arg2)
        v8 = (((arg1 + (((load32(arg0 + 4) - v4) // 196) * 196)) if (u(v5) > u(v6)) else arg2) - arg1)
        if (arg1 != v7):
            # TODO: memory.copy []
        if (u(v5) > u(v6)):
            arg1 = load32(arg0 + 4)
            if (arg2 != v7):
                while True:  # $label0
                    # TODO: memory.copy []
                    arg1 = (arg1 + 196)
                    v3 = (v3 + 196)
                    if ((v3 + 196) != arg2):
                        continue
                    break
            store32(arg0 + 4, arg1)
            return 196
        store32(arg0 + 4, (v4 + ((v8 // 196) * 196)))
        return v3
    if v4:
        store32(arg0 + 4, v4)
        store32(arg0 + 8, 0)
        store64(arg0, 0)
        v3 = 0
    while True:  # block $label1
        if (u(v5) >= u(21913099)):
            break
        v3 = (v3 // 196)
        v4 = ((v3 // 196) << 1)
        v3 = (21913098 if (u(v3) >= u(10956549)) else (((v3 // 196) << 1) if (u(v4) > u(v5)) else v5))
        if (u((21913098 if (u(v3) >= u(10956549)) else (((v3 // 196) << 1) if (u(v4) > u(v5)) else v5))) >= u(21913099)):
            break
        v4 = (v3 * 196)
        v3 = func26((v3 * 196))
        store32(arg0 + 4, func26((v3 * 196)))
        store32(arg0, v3)
        store32(arg0 + 8, (v3 + v4))
        if (arg1 != arg2):
            arg0 = (v6 - 196)
            arg0 = (((v6 - 196) - (arg0 % 196)) + 196)
            # TODO: memory.copy []
        else:
        store32((arg0 + v3) + 4, v3)
        return (((v6 - 196) - (arg0 % 196)) + 196)
        break
    func42()
    raise RuntimeError('unreachable')
    return arg1

# ------------------------------------------------------------
# $func312
# ------------------------------------------------------------
def func312(arg0, arg1):
    if ((load8u(arg0 + 11) & 0xFFFFFFFF) >> 7):
        store32(arg0 + 4, arg1)
        return
    store8(arg0 + 11, ((load8u(arg0 + 11) & 128) | arg1))
    store8(arg0 + 11, (load8u(arg0 + 11) & 127))

# ------------------------------------------------------------
# $func313
# ------------------------------------------------------------
def func313(arg0):
    v2 = func443(8)
    store32(func443(8), 32876)
    store32(v2, 32988)
    v3 = func209(arg0)
    v1 = func26((func209(arg0) + 13))
    store32(func26((func209(arg0) + 13)) + 8, 0)
    store32(v1 + 4, v3)
    store32(v1, v3)
    v1 = (v1 + 12)
    # TODO: memory.copy []
    store32(v2 + 4, v1)
    store32(v2, 33036)
    a_i()
    raise RuntimeError('unreachable')

# ------------------------------------------------------------
# $func314
# ------------------------------------------------------------
def func314(arg0, arg1, arg2):
    arg1 = func26(arg2)
    store32(arg0 + 4, arg2)
    store32(arg0, arg1)

# ------------------------------------------------------------
# $func315
# ------------------------------------------------------------
def func315(arg0, arg1, arg2):
    v9 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v3 = load32(9142892)
        if ((arg1 != 2147483647) & (u(load32(9142892)) <= u(arg1))):
            break
        v11 = load32(arg0 + 16)
        while True:  # block $label1
            while True:  # block $label4
                while True:  # block $label2
                    while True:  # block $label3
                        # br_table[load32(arg0 + 4)]
                        break
                        break
                    v8 = load32(arg0 + 88)
                    if (load32(arg0 + 88) == 0):
                        break
                    v6 = load32(arg0 + 12)
                    if (load32(arg0 + 12) == 0):
                        break
                    v5 = ((v11 * 404) + 9568096)
                    arg2 = 0
                    v4 = v6
                    while True:  # $label8
                        while True:  # block $label5
                            if (v4 == 0):
                                v4 = 0
                                break
                            v3 = 0
                            v7 = (arg2 << 2)
                            if (load8u((load32(9671128) + (load32(((arg2 << 2) + load32(arg0 + 80))) * 132)) + 125) == 3):
                                break
                            while True:  # $label7
                                v4 = (load32(9671128) + (load32((load32(arg0 + 80) + v7)) * 132))
                                if (load8u((load32(9671128) + (load32((load32(arg0 + 80) + v7)) * 132)) + 125) != 3):
                                    while True:  # block $label6
                                        if (func59((v9 + 12), (v9 + 8), v4, v5) == 0):
                                            break
                                        v4 = func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1)
                                        if (func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1) == 0):
                                            break
                                        if (u(load32(arg0 + 104)) < u(7)):
                                            break
                                        func148(v4, load32(arg0 + 96), 0)
                                        break
                                    v6 = load32(arg0 + 12)
                                v3 = (v3 + 1)
                                if (u((v3 + 1)) < u(v6)):
                                    continue
                                break
                            v8 = load32(arg0 + 88)
                            v4 = v6
                            break
                        arg2 = (arg2 + 1)
                        if (u((arg2 + 1)) < u(v8)):
                            continue
                        break
                    break
                    break
                if (v3 == 0):
                    break
                v17 = ((v11 * 404) + 9568096)
                arg2 = load32(arg0 + 36)
                if (u(load32(arg0 + 36)) <= u(3)):
                    v14 = (arg2 - 1)
                    while True:  # $label23
                        while True:  # block $label9
                            arg2 = load32(arg0 + 64)
                            v4 = (v8 << 2)
                            if (load32((load32(arg0 + 64) + (v8 << 2))) == 0):
                                if (load32((arg2 + (v3 << 2))) == 0):
                                    break
                                if (load32((load32(9142420) + v4)) == 0):
                                    break
                            v5 = 0
                            v15 = load32(9561692)
                            while True:  # $label22
                                while True:  # block $label14
                                    while True:  # block $label13
                                        while True:  # block $label10
                                            while True:  # block $label11
                                                while True:  # block $label12
                                                    # br_table[v14]
                                                    break
                                                    break
                                                if (load32(((v5 * 404) + 9568096) + 264) == 1):
                                                    break
                                                break
                                                break
                                            if (load32(((v5 * 404) + 9568096) + 264) == 0):
                                                break
                                            break
                                            break
                                        arg2 = ((v5 * 404) + 9568096)
                                        if load32(((v5 * 404) + 9568096) + 264):
                                            break
                                        if (load32(arg2 + 268) == 1):
                                            break
                                        if (load32(arg2 + 92) == 0):
                                            break
                                        if (load32(38456) == v5):
                                            break
                                        if (load32(38764) == v5):
                                            break
                                        break
                                    v13 = load32((((v15 + (v8 * 286704)) + (v5 << 2)) + 284636))
                                    if (load32((((v15 + (v8 * 286704)) + (v5 << 2)) + 284636)) == 0):
                                        break
                                    v10 = 0
                                    v12 = load32(v13 + 8)
                                    if (load32(v13 + 8) == 0):
                                        break
                                    while True:  # $label21
                                        while True:  # block $label15
                                            arg2 = load32((load32(v13) + (v10 << 2)))
                                            if (load32((load32(v13) + (v10 << 2))) == 0):
                                                break
                                            if (load32(arg0 + 12) == 0):
                                                break
                                            v6 = 0
                                            v18 = (load32(9671128) + (arg2 * 132))
                                            while True:  # $label20
                                                while True:  # block $label16
                                                    if (func59((v9 + 12), (v9 + 8), v18, v17) == 0):
                                                        break
                                                    arg2 = func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1)
                                                    if (func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1) == 0):
                                                        break
                                                    if (u(load32(arg0 + 104)) < u(7)):
                                                        break
                                                    v3 = (load32(9671128) + (arg2 * 132))
                                                    v7 = load32(arg0 + 96)
                                                    arg2 = load32(load32(arg0 + 96))
                                                    if (u(load32(load32(arg0 + 96))) <= u(2147483646)):
                                                        store32(v3 + 52, arg2)
                                                    arg2 = load32(v7 + 4)
                                                    if (u(load32(v7 + 4)) <= u(2147483646)):
                                                        store32(v3 + 60, arg2)
                                                    while True:  # block $label17
                                                        arg2 = load32(v7 + 8)
                                                        if (u(load32(v7 + 8)) > u(2147483646)):
                                                            break
                                                        store32(v3 + 64, arg2)
                                                        if (u(load32(v7 + 8)) > u(2147483646)):
                                                            break
                                                        store32(v3 + 68, load32(v7 + 12))
                                                        break
                                                    v4 = load32(v3 + 76)
                                                    arg2 = load32(v3 + 76)
                                                    while True:  # block $label18
                                                        v16 = load32(v7 + 16)
                                                        if (u(load32(v7 + 16)) > u(2147483646)):
                                                            break
                                                        store32(v3 + 72, v16)
                                                        if (u(load32(v7 + 16)) > u(2147483646)):
                                                            break
                                                        arg2 = load32(v7 + 20)
                                                        store32(v3 + 76, load32(v7 + 20))
                                                        break
                                                    v7 = load32(v7 + 24)
                                                    if (u(load32(v7 + 24)) <= u(2147483646)):
                                                        store32(v3 + 84, v7)
                                                    v16 = ((load8u(v3 + 122) * 404) + 9568096)
                                                    v7 = load32(((load8u(v3 + 122) * 404) + 9568096) + 264)
                                                    while True:  # block $label19
                                                        if (load32(v16 + 92) == 0):
                                                            if (v7 == 2):
                                                                break
                                                            store32(v3 + 52, 0)
                                                        if (v7 != 1):
                                                            break
                                                        arg2 = 0
                                                        store32(v3 + 72, 0)
                                                        store32(v3 + 60, 0)
                                                        store32(v3 + 76, 0)
                                                        store32(v3 + 84, 0)
                                                        break
                                                    if (load32(v3 + 64) == 0):
                                                        store32((v3 - -64), -1)
                                                    if (arg2 == 0):
                                                        break
                                                    if v4:
                                                        break
                                                    break
                                                v6 = (v6 + 1)
                                                if (u((v6 + 1)) < u(load32(arg0 + 12))):
                                                    continue
                                                break
                                            break
                                        v10 = (v10 + 1)
                                        if ((v10 + 1) != v12):
                                            continue
                                        break
                                    break
                                v5 = (v5 + 1)
                                if ((v5 + 1) != 255):
                                    continue
                                break
                            v3 = load32(9142892)
                            break
                        v8 = (v8 + 1)
                        if (u((v8 + 1)) < u(v3)):
                            continue
                        break
                    break
                v13 = ((arg2 - 4) << 2)
                while True:  # $label32
                    while True:  # block $label24
                        arg2 = load32(arg0 + 64)
                        v4 = (v8 << 2)
                        if (load32((load32(arg0 + 64) + (v8 << 2))) == 0):
                            if (load32((arg2 + (v3 << 2))) == 0):
                                break
                            if (load32((load32(9142420) + v4)) == 0):
                                break
                        v7 = load32((((load32(9561692) + (v8 * 286704)) + v13) + 284636))
                        if (load32((((load32(9561692) + (v8 * 286704)) + v13) + 284636)) == 0):
                            break
                        v10 = 0
                        v14 = load32(v7 + 8)
                        if (load32(v7 + 8) == 0):
                            break
                        while True:  # $label31
                            while True:  # block $label25
                                arg2 = load32((load32(v7) + (v10 << 2)))
                                if (load32((load32(v7) + (v10 << 2))) == 0):
                                    break
                                if (load32(arg0 + 12) == 0):
                                    break
                                v6 = 0
                                v15 = (load32(9671128) + (arg2 * 132))
                                while True:  # $label30
                                    while True:  # block $label26
                                        if (func59((v9 + 12), (v9 + 8), v15, v17) == 0):
                                            break
                                        arg2 = func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1)
                                        if (func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1) == 0):
                                            break
                                        if (u(load32(arg0 + 104)) < u(7)):
                                            break
                                        v3 = (load32(9671128) + (arg2 * 132))
                                        v5 = load32(arg0 + 96)
                                        arg2 = load32(load32(arg0 + 96))
                                        if (u(load32(load32(arg0 + 96))) <= u(2147483646)):
                                            store32(v3 + 52, arg2)
                                        arg2 = load32(v5 + 4)
                                        if (u(load32(v5 + 4)) <= u(2147483646)):
                                            store32(v3 + 60, arg2)
                                        while True:  # block $label27
                                            arg2 = load32(v5 + 8)
                                            if (u(load32(v5 + 8)) > u(2147483646)):
                                                break
                                            store32(v3 + 64, arg2)
                                            if (u(load32(v5 + 8)) > u(2147483646)):
                                                break
                                            store32(v3 + 68, load32(v5 + 12))
                                            break
                                        v4 = load32(v3 + 76)
                                        arg2 = load32(v3 + 76)
                                        while True:  # block $label28
                                            v12 = load32(v5 + 16)
                                            if (u(load32(v5 + 16)) > u(2147483646)):
                                                break
                                            store32(v3 + 72, v12)
                                            if (u(load32(v5 + 16)) > u(2147483646)):
                                                break
                                            arg2 = load32(v5 + 20)
                                            store32(v3 + 76, load32(v5 + 20))
                                            break
                                        v5 = load32(v5 + 24)
                                        if (u(load32(v5 + 24)) <= u(2147483646)):
                                            store32(v3 + 84, v5)
                                        v12 = ((load8u(v3 + 122) * 404) + 9568096)
                                        v5 = load32(((load8u(v3 + 122) * 404) + 9568096) + 264)
                                        while True:  # block $label29
                                            if (load32(v12 + 92) == 0):
                                                if (v5 == 2):
                                                    break
                                                store32(v3 + 52, 0)
                                            if (v5 != 1):
                                                break
                                            arg2 = 0
                                            store32(v3 + 72, 0)
                                            store32(v3 + 60, 0)
                                            store32(v3 + 76, 0)
                                            store32(v3 + 84, 0)
                                            break
                                        if (load32(v3 + 64) == 0):
                                            store32((v3 - -64), -1)
                                        if (arg2 == 0):
                                            break
                                        if v4:
                                            break
                                        break
                                    v6 = (v6 + 1)
                                    if (u((v6 + 1)) < u(load32(arg0 + 12))):
                                        continue
                                    break
                                break
                            v10 = (v10 + 1)
                            if ((v10 + 1) != v14):
                                continue
                            break
                        v3 = load32(9142892)
                        break
                    v8 = (v8 + 1)
                    if (u((v8 + 1)) < u(v3)):
                        continue
                    break
                break
                break
            v8 = load32(9140300)
            if (load32(9140300) == 0):
                break
            v5 = ((v11 * 404) + 9568096)
            v4 = load32(arg0 + 12)
            while True:  # $label36
                v3 = 0
                while True:  # block $label33
                    v7 = (load32(9671128) + (load32(((v6 << 2) + 8451904)) * 132))
                    v10 = load16u((load32(9671128) + (load32(((v6 << 2) + 8451904)) * 132)) + 110)
                    if ((((load32((load32(9142420) + (load16u((load32(9671128) + (load32(((v6 << 2) + 8451904)) * 132)) + 110) << 2))) != 0) & (arg1 == v10)) | arg2) != 1):
                        break
                    if (v4 == 0):
                        break
                    while True:  # $label35
                        while True:  # block $label34
                            if (func59((v9 + 12), (v9 + 8), v7, v5) == 0):
                                break
                            v4 = func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1)
                            if (func34(v11, arg1, load32(v9 + 12), load32(v9 + 8), 0, 1) == 0):
                                break
                            if (u(load32(arg0 + 104)) < u(7)):
                                break
                            func148(v4, load32(arg0 + 96), 0)
                            break
                        v3 = (v3 + 1)
                        v4 = load32(arg0 + 12)
                        if (u((v3 + 1)) < u(load32(arg0 + 12))):
                            continue
                        break
                    v8 = load32(9140300)
                    break
                v6 = (v6 + 1)
                if (u((v6 + 1)) < u(v8)):
                    continue
                break
            break
            break
        if (load32(arg0 + 12) == 0):
            break
        v10 = ((v11 * 404) + 9568096)
        arg2 = 0
        while True:  # $label41
            v8 = load32(arg0 + 20)
            v3 = 0
            v5 = load32(arg0 + 28)
            if load32(arg0 + 28):
                v19 = load64(9147316)
                v4 = load32(9147312)
                store32(9147316, load32(9147312))
                v6 = load32(9147324)
                store64(9147320, v19)
                v6 = (v6 ^ (v6 << 11))
                v4 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6)
                store32(9147312, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6))
            else:
            v8 = (0 + v8)
            v3 = load32(arg0 + 24)
            while True:  # block $label40
                while True:  # block $label37
                    v5 = load32(arg0 + 40)
                    if load32(arg0 + 40):
                        v19 = load64(9147316)
                        v4 = load32(9147312)
                        store32(9147316, load32(9147312))
                        v6 = load32(9147324)
                        store64(9147320, v19)
                        v6 = (v6 ^ (v6 << 11))
                        v4 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6)
                        store32(9147312, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6))
                    else:
                    v5 = (0 + v3)
                    if func56((v4 % v5), (0 + v3), v10, arg1, 0, 0, 1, 1, 0):
                        v3 = v8
                        v4 = v5
                        break
                    v4 = 0
                    v6 = load32(9142440)
                    while True:  # $label39
                        while True:  # block $label38
                            v7 = v4
                            v3 = (v4 << 2)
                            v4 = (load32((((v4 << 2) | 4) + 8611904)) + v5)
                            if (u(v6) <= u((load32((((v4 << 2) | 4) + 8611904)) + v5))):
                                break
                            v3 = (load32((v3 + 8611904)) + v8)
                            if (u(v6) <= u((load32((v3 + 8611904)) + v8))):
                                break
                            if ((v3 | v4) < 0):
                                break
                            if func56(v3, v4, v10, arg1, 0, 0, 1, 1, 0):
                                break
                            v6 = load32(9142440)
                            break
                        v4 = (v7 + 2)
                        if (u(v7) < u(5198)):
                            continue
                        break
                    break
                    break
                v4 = func34(v11, arg1, v3, v4, 0, 1)
                if (func34(v11, arg1, v3, v4, 0, 1) == 0):
                    break
                if (u(load32(arg0 + 104)) < u(7)):
                    break
                func148(v4, load32(arg0 + 96), 0)
                break
            arg2 = (arg2 + 1)
            if (u((arg2 + 1)) < u(load32(arg0 + 12))):
                continue
            break
        break
    G.global0 = (v9 + 16)
    return v8

# ------------------------------------------------------------
# $func317
# ------------------------------------------------------------
def func317(arg0):
    v1 = load32(arg0 + 283960)
    v25 = (load32(arg0 + 283960) if (u(v1) <= u(2)) else 0)
    while True:  # block $label43
        v2 = load32(9142428)
        if (u(load32(9142428)) >= u(48)):
            v4 = 47
            v26 = 1
            v1 = -1
            while True:  # $label42
                v6 = (load32(9142424) + (v4 << 2))
                v29 = load32((load32(9142424) + (v4 << 2)) + 16)
                v30 = ((v4 + 7) if load32((load32(9142424) + (v4 << 2)) + 16) else v4)
                while True:  # block $label0
                    if (load32(v6 + 4) != 1):
                        break
                    v17 = load32(v6 + 8)
                    if (load32(v6 + 8) < 0):
                        v17 = load32((((v25 + (v17 ^ -1)) << 2) + 9681488))
                    v12 = load32(v6)
                    v13 = load32(v6 + 12)
                    v40 = 0.0
                    while True:  # block $label1
                        if (v3 == 0):
                            break
                        if (v3 != v12):
                            break
                        if (v1 != v13):
                            break
                        v40 = (3.14159274 / float(v3))
                        break
                    if (v12 == 0):
                        v3 = 0
                        v1 = v13
                        break
                    v41 = (6.28318548 / float(v12))
                    v9 = ((v17 * 404) + 9568096)
                    v35 = float(v13)
                    v23 = 0
                    while True:  # $label41
                        # TODO: f32.convert_i32_u []
                        v33 = ((v41 * v23) + v40)
                        v24 = load32(arg0 + 283908)
                        v1 = load32(arg0 + 283876)
                        v2 = load32(arg0 + 283872)
                        v20 = 0
                        v27 = load32(v9 + 264)
                        if (load32(v9 + 264) == 0):
                            while True:  # block $label2
                                # TODO: f64.promote_f32 []
                                v44 = (((v33 * -8.0) / 6.2831854820251465) + 10.5)
                                if (((((v33 * -8.0) / 6.2831854820251465) + 10.5) < 4294967296.0) & (v44 >= 0.0)):
                                    # TODO: i32.trunc_f64_u []
                                    break
                                break
                            v20 = (0 & 7)
                        v28 = load32(v9 + 220)
                        # TODO: f32.convert_i32_u []
                        v42 = (load32(v9 + 220) * -0.5)
                        v34 = (((v35 * func48(v33)) + (load32(v9 + 220) * -0.5)) + 0.5)
                        v7 = load32(v9 + 216)
                        # TODO: f32.convert_i32_u []
                        v43 = (load32(v9 + 216) * -0.5)
                        v36 = (((v35 * func49(v33)) + (load32(v9 + 216) * -0.5)) + 0.5)
                        v38 = float(v1)
                        v39 = float(v2)
                        while True:  # block $label6
                            while True:  # block $label9
                                while True:  # block $label5
                                    while True:  # block $label3
                                        v37 = (v33 + 0.196349546)
                                        v33 = (v33 + 6.28318548)
                                        if ((v33 + 0.196349546) >= (v33 + 6.28318548)):
                                            v8 = load32(9142440)
                                            v14 = (load32(9142440) + 2)
                                            v18 = load32(9142840)
                                            break
                                        if (v7 <= 0):
                                            while True:  # block $label4
                                                v33 = (v34 + v38)
                                                if (abs((v34 + v38)) < 2147483650.0):
                                                    break
                                                break
                                            v3 = -2147483648
                                            v33 = (v36 + v39)
                                            if ((abs((v36 + v39)) < 2147483650.0) == 0):
                                                break
                                            break
                                        v18 = load32(9142840)
                                        v10 = load32(v9 + 372)
                                        v8 = load32(9142440)
                                        v14 = (load32(9142440) + 2)
                                        v19 = ((load32(9142440) + 2) * load32(v9 + 208))
                                        v15 = load32(v9 + 212)
                                        while True:  # $label21
                                            while True:  # block $label7
                                                v34 = (v34 + v38)
                                                if (abs((v34 + v38)) < 2147483650.0):
                                                    break
                                                break
                                            v3 = -2147483648
                                            v11 = (v3 + v28)
                                            v1 = (-2147483648 >= (v3 + v28))
                                            while True:  # block $label8
                                                v34 = (v36 + v39)
                                                if (abs((v36 + v39)) < 2147483650.0):
                                                    break
                                                break
                                            v4 = -2147483648
                                            if v1:
                                                break
                                            v21 = (v4 + v7)
                                            v2 = v4
                                            while True:  # block $label10
                                                if (v27 == 1):
                                                    while True:  # $label15
                                                        v5 = (v2 + 1)
                                                        v16 = (v2 - v4)
                                                        v1 = v3
                                                        while True:  # block $label12
                                                            if (u(v2) >= u(v8)):
                                                                while True:  # $label11
                                                                    if load8u((v10 + (((v1 - v3) * v7) + v16))):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if ((v1 + 1) != v11):
                                                                        continue
                                                                    break
                                                                    break
                                                                raise RuntimeError('unreachable')
                                                            while True:  # $label14
                                                                while True:  # block $label13
                                                                    if (load8u((v10 + (((v1 - v3) * v7) + v16))) == 0):
                                                                        v1 = (v1 + 1)
                                                                        break
                                                                    if (u(v1) >= u(v8)):
                                                                        break
                                                                    if ((v1 | v2) < 0):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (load32((v18 + (((((v1 + 1) + v19) * v14) + v5) << 2))) != v15):
                                                                        break
                                                                    if (load32((v18 + (((v1 * v14) + v5) << 2))) != v15):
                                                                        break
                                                                    break
                                                                if (v1 != v11):
                                                                    continue
                                                                break
                                                            break
                                                        v2 = v5
                                                        if (v5 < v21):
                                                            continue
                                                        break
                                                        break
                                                    raise RuntimeError('unreachable')
                                                while True:  # $label20
                                                    v5 = (v2 + 1)
                                                    v16 = (v2 - v4)
                                                    v1 = v3
                                                    while True:  # block $label18
                                                        if (u(v2) < u(v8)):
                                                            while True:  # $label17
                                                                while True:  # block $label16
                                                                    if (load8u((v10 + (((v1 - v3) * v7) + v16))) == 0):
                                                                        v1 = (v1 + 1)
                                                                        break
                                                                    if (u(v1) >= u(v8)):
                                                                        break
                                                                    if ((v1 | v2) < 0):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (load32((v18 + (((((v1 + 1) + v19) * v14) + v5) << 2))) != v15):
                                                                        break
                                                                    break
                                                                if (v1 != v11):
                                                                    continue
                                                                break
                                                                break
                                                            raise RuntimeError('unreachable')
                                                        while True:  # $label19
                                                            if load8u((v10 + (((v1 - v3) * v7) + v16))):
                                                                break
                                                            v1 = (v1 + 1)
                                                            if ((v1 + 1) != v11):
                                                                continue
                                                            break
                                                        break
                                                    v2 = v5
                                                    if (v5 < v21):
                                                        continue
                                                    break
                                                break
                                                break
                                            v34 = (((v35 * func48(v37)) + v42) + 0.5)
                                            v36 = (((v35 * func49(v37)) + v43) + 0.5)
                                            v37 = (v37 + 0.196349546)
                                            if (((v37 + 0.196349546) >= v33) == 0):
                                                continue
                                            break
                                        break
                                    while True:  # block $label22
                                        v33 = (v34 + v38)
                                        if (abs((v34 + v38)) < 2147483650.0):
                                            break
                                        break
                                    v31 = -2147483648
                                    while True:  # block $label23
                                        v33 = (v36 + v39)
                                        if (abs((v36 + v39)) < 2147483650.0):
                                            break
                                        break
                                    v32 = -2147483648
                                    v1 = 0
                                    while True:  # $label36
                                        while True:  # block $label24
                                            v10 = v1
                                            v1 = (v1 << 2)
                                            v3 = (load32((((v1 << 2) | 4) + 8611904)) + v31)
                                            if (u(v8) <= u((load32((((v1 << 2) | 4) + 8611904)) + v31))):
                                                break
                                            v5 = (load32((v1 + 8611904)) + v32)
                                            if (u(v8) <= u((load32((v1 + 8611904)) + v32))):
                                                break
                                            if ((v3 | v5) < 0):
                                                break
                                            while True:  # block $label25
                                                if (v7 <= 0):
                                                    break
                                                v11 = (v3 + v28)
                                                if ((v3 + v28) <= v3):
                                                    break
                                                v21 = (v5 + v7)
                                                v15 = load32(v9 + 372)
                                                v16 = (load32(v9 + 208) * v14)
                                                v19 = load32(v9 + 212)
                                                v4 = v5
                                                v2 = v5
                                                if (v27 == 1):
                                                    while True:  # $label30
                                                        v2 = (v4 + 1)
                                                        v22 = (v4 - v5)
                                                        v1 = v3
                                                        while True:  # block $label27
                                                            if (u(v4) >= u(v8)):
                                                                while True:  # $label26
                                                                    if load8u((v15 + (((v1 - v3) * v7) + v22))):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if ((v1 + 1) != v11):
                                                                        continue
                                                                    break
                                                                    break
                                                                raise RuntimeError('unreachable')
                                                            while True:  # $label29
                                                                while True:  # block $label28
                                                                    if (load8u((v15 + (((v1 - v3) * v7) + v22))) == 0):
                                                                        v1 = (v1 + 1)
                                                                        break
                                                                    if (u(v1) >= u(v8)):
                                                                        break
                                                                    if ((v1 | v4) < 0):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (load32((v18 + (((((v1 + 1) + v16) * v14) + v2) << 2))) != v19):
                                                                        break
                                                                    if (load32((v18 + (((v1 * v14) + v2) << 2))) != v19):
                                                                        break
                                                                    break
                                                                if (v1 != v11):
                                                                    continue
                                                                break
                                                            break
                                                        v4 = v2
                                                        if (v2 < v21):
                                                            continue
                                                        break
                                                        break
                                                    raise RuntimeError('unreachable')
                                                while True:  # $label35
                                                    v4 = (v2 + 1)
                                                    v22 = (v2 - v5)
                                                    v1 = v3
                                                    while True:  # block $label33
                                                        if (u(v2) < u(v8)):
                                                            while True:  # $label32
                                                                while True:  # block $label31
                                                                    if (load8u((v15 + (((v1 - v3) * v7) + v22))) == 0):
                                                                        v1 = (v1 + 1)
                                                                        break
                                                                    if (u(v1) >= u(v8)):
                                                                        break
                                                                    if ((v1 | v2) < 0):
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (load32((v18 + (((((v1 + 1) + v16) * v14) + v4) << 2))) != v19):
                                                                        break
                                                                    break
                                                                if (v1 != v11):
                                                                    continue
                                                                break
                                                                break
                                                            raise RuntimeError('unreachable')
                                                        while True:  # $label34
                                                            if load8u((v15 + (((v1 - v3) * v7) + v22))):
                                                                break
                                                            v1 = (v1 + 1)
                                                            if ((v1 + 1) != v11):
                                                                continue
                                                            break
                                                        break
                                                    v2 = v4
                                                    if (v4 < v21):
                                                        continue
                                                    break
                                                break
                                            break
                                            break
                                        v1 = (v10 + 2)
                                        if (u(v10) < u(13118)):
                                            continue
                                        break
                                    break
                                    break
                                v4 = -2147483648
                                break
                            break
                        v1 = func34(v17, v24, v4, v3, v20, 1)
                        if v26:
                            store32(arg0 + 284624, v1)
                        if (load32(v9 + 268) == 1):
                            store32((load32(9671128) + (v1 * 132)) + 56, 1)
                        while True:  # block $label37
                            if (v29 == 0):
                                break
                            if (v1 == 0):
                                break
                            v1 = (load32(9671128) + (v1 * 132))
                            v2 = load32(v6 + 20)
                            if (u(load32(v6 + 20)) <= u(2147483646)):
                                store32(v1 + 52, v2)
                            v2 = load32(v6 + 24)
                            if (u(load32(v6 + 24)) <= u(2147483646)):
                                store32(v1 + 60, v2)
                            while True:  # block $label38
                                v2 = load32(v6 + 28)
                                if (u(load32(v6 + 28)) > u(2147483646)):
                                    break
                                store32(v1 + 64, v2)
                                if (u(load32(v6 + 28)) > u(2147483646)):
                                    break
                                store32(v1 + 68, load32(v6 + 32))
                                break
                            v4 = load32(v1 + 76)
                            while True:  # block $label39
                                v2 = load32(v6 + 36)
                                if (u(load32(v6 + 36)) > u(2147483646)):
                                    break
                                store32(v1 + 72, v2)
                                if (u(load32(v6 + 36)) > u(2147483646)):
                                    break
                                store32(v1 + 76, load32(v6 + 40))
                                break
                            v2 = load32(v6 + 44)
                            if (u(load32(v6 + 44)) <= u(2147483646)):
                                store32(v1 + 84, v2)
                            v3 = ((load8u(v1 + 122) * 404) + 9568096)
                            v2 = load32(((load8u(v1 + 122) * 404) + 9568096) + 264)
                            while True:  # block $label40
                                if (load32(v3 + 92) == 0):
                                    if (v2 == 2):
                                        break
                                    store32(v1 + 52, 0)
                                if (v2 != 1):
                                    break
                                store32(v1 + 84, 0)
                                store32(v1 + 72, 0)
                                store32(v1 + 60, 0)
                                break
                            v2 = load32(v1 + 64)
                            if load32(v1 + 64):
                            else:
                                store32((v1 - -64), -1)
                            store32(v2 + 68, -1)
                            v2 = load32(v1 + 72)
                            store32(v1 + 76, load32(v1 + 72))
                            if (v2 == 0):
                                break
                            if v4:
                                break
                            break
                        v26 = 0
                        v23 = (v23 + 1)
                        if ((v23 + 1) != v12):
                            continue
                        break
                    v2 = load32(9142428)
                    v1 = v13
                    v3 = v12
                    break
                v4 = (v30 + 5)
                if (u((v30 + 5)) < u(v2)):
                    continue
                break
            if (v1 != -1):
                break
        while True:  # block $label48
            v12 = load32(arg0 + 283908)
            v33 = 0.0
            v10 = load32(((v25 << 2) + 9681488))
            v2 = ((load32(((v25 << 2) + 9681488)) * 404) + 9568096)
            v6 = (0 if load32(((load32(((v25 << 2) + 9681488)) * 404) + 9568096) + 264) else 2)
            # TODO: f32.convert_i32_u []
            v34 = (load32(v2 + 220) * -0.5)
            # TODO: f32.convert_i32_u []
            v36 = (load32(v2 + 216) * -0.5)
            v37 = float(load32(arg0 + 283876))
            v38 = float(load32(arg0 + 283872))
            while True:  # block $label46
                while True:  # $label47
                    v35 = (v33 + 0.196349546)
                    while True:  # block $label44
                        v39 = ((((func48(v33) * 0.0) + v34) + 0.5) + v37)
                        if (abs(((((func48(v33) * 0.0) + v34) + 0.5) + v37)) < 2147483650.0):
                            break
                        break
                    v4 = -2147483648
                    arg0 = (v35 >= 6.28318548)
                    while True:  # block $label45
                        v33 = ((((func49(v33) * 0.0) + v36) + 0.5) + v38)
                        if (abs(((((func49(v33) * 0.0) + v36) + 0.5) + v38)) < 2147483650.0):
                            break
                        break
                    v3 = -2147483648
                    if arg0:
                        break
                    v33 = v35
                    if (func73(v3, v4, v2, 0, 0, 1) == 0):
                        continue
                    break
                break
                break
            v13 = load32(9142440)
            arg0 = 0
            while True:  # block $label50
                while True:  # $label51
                    while True:  # block $label49
                        v1 = arg0
                        v5 = (arg0 << 2)
                        arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v4)
                        if (u(v13) <= u((load32((((arg0 << 2) | 4) + 8611904)) + v4))):
                            break
                        v5 = (load32((v5 + 8611904)) + v3)
                        if (u(v13) <= u((load32((v5 + 8611904)) + v3))):
                            break
                        if ((arg0 | v5) < 0):
                            break
                        if func73(v5, arg0, v2, 0, 0, 1):
                            break
                        v13 = load32(9142440)
                        break
                    arg0 = (v1 + 2)
                    if (u(v1) < u(13118)):
                        continue
                    break
                break
                break
            break
        store32(0 + 284624, func34(v10, v12, v5, arg0, v6, 1))
        break
    return func34(v10, v12, v3, v4, v6, 1)

# ------------------------------------------------------------
# $func318
# ------------------------------------------------------------
def func318(arg0, arg1, arg2):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label1
        while True:  # block $label0
            v3 = load8u(9147152)
            if (load8u(9147152) == 0):
                v4 = load32(arg1)
                break
            v4 = load32(9142440)
            v5 = load32(arg1)
            if (load32(9142440) == load32(arg1)):
                break
            store32(arg0, v5)
            v3 = load8u(9147152)
            break
            break
        store32(9142440, v4)
        break
    while True:  # block $label2
        if (v3 == 0):
            break
        v3 = load32(arg1 + 24)
        v4 = load32(9142424)
        if (load32(arg1 + 24) == load32(load32(9142424) + 24)):
            break
        store32(v4 + 24, v3)
        Gb(arg2)
        break
    store32(9142424, 0)
    v4 = (arg2 << 2)
    v3 = func26((-1 if (u(arg2) > u(1073741823)) else (arg2 << 2)))
    store32(9142428, arg2)
    store32(9142424, v3)
    if arg2:
        # TODO: memory.copy []
    G.global0 = (arg0 + 16)

# ------------------------------------------------------------
# $func319
# ------------------------------------------------------------
def func319():
    v4 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    func402(load32(9142440))
    v1 = load32(9142440)
    if load32(9142440):
        v5 = load32(9147288)
        while True:  # $label2
            v3 = (v0 + 1)
            v2 = 0
            v6 = load32(9142840)
            v7 = load32(9140332)
            while True:  # $label1
                while True:  # block $label0
                    v8 = load8s((v5 + ((v1 * v2) + v0)))
                    if (load8s((v5 + ((v1 * v2) + v0))) < 0):
                        break
                    if (load32(load32((v7 + ((v8 & 255) << 2))) + 32) != 23):
                        break
                    v8 = (v2 + 1)
                    store32((v6 + ((((v2 + 1) * (v1 + 2)) + v3) << 2)), 1)
                    v1 = (load32(9142440) + 2)
                    store32((v6 + (((((load32(9142440) + 2) + v8) * v1) + v3) << 2)), 1)
                    v1 = load32(9142440)
                    break
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(v1)):
                    continue
                break
            v0 = v3
            if (u(v3) < u(v1)):
                continue
            break
    v1 = 3
    if (u(load32(9671136)) > u(3)):
        v6 = 0
        while True:  # $label9
            while True:  # block $label3
                v0 = (load32(9671128) + (v1 * 132))
                v3 = load32((load32(9671128) + (v1 * 132)) + 28)
                if (load32((load32(9671128) + (v1 * 132)) + 28) == 0):
                    break
                v2 = load16u(v0 + 110)
                if (u(load16u(v0 + 110)) >= u(load32(9142892))):
                    break
                v5 = load8u(v0 + 122)
                v7 = (load8u(v0 + 122) != load32(38448))
                if ((load8u(v0 + 122) != load32(38448)) == 0):
                    store32(v0 + 48, load32(((v5 * 72) + 9263856)))
                v2 = (load32(9561692) + (v2 * 286704))
                while True:  # block $label5
                    while True:  # block $label4
                        if (load8u(9216060) == 0):
                            if (load32(v0 + 64) == 0):
                                break
                        if (load8u(v0 + 125) != 3):
                            break
                        break
                    store8(v0 + 125, 3)
                    if (v7 == 0):
                        v3 = load32(v0 + 28)
                    store32(v0 + 92, 0)
                    func388(v2, v3)
                    break
                    break
                if func292(v0):
                    store32(v0 + 92, 0)
                v3 = ((v5 * 404) + 9568096)
                store32(v0 + 92, 0)
                while True:  # block $label6
                    if load32(v0 + 36):
                        func138(v0)
                        break
                    v5 = load8u(v0 + 125)
                    break
                while True:  # block $label7
                    if (u(load32(9684508)) > u(551)):
                        break
                    if (u(load32(v0 + 84)) < u(12)):
                        break
                    if load32(((load8u(v0 + 122) * 404) + 9568096) + 264):
                        break
                    store32(v2 + 283936, (load32(v2 + 283936) + 1))
                    break
                while True:  # block $label8
                    if (load32(v0 + 32) != -1):
                        break
                    if load8u(9147152):
                        break
                    store32(v0 + 32, 0)
                    v6 = (v6 + 25)
                    func240(v0, (((v6 + 25) % 1000) + 25), 0)
                    break
                    break
                if (load32(v3 + 264) == 4):
                    store8(9671157, 1)
                if (load32(v3 + 208) == 2):
                    store8(9671158, 1)
                func144(v2, load32(v0 + 28), 0)
                break
            v1 = (v1 + 1)
            if (u((v1 + 1)) < u(load32(9671136))):
                continue
            break
    if load8u(9561801):
        store32(v4 + 16, load32(9142840))
        v0 = (load32(9142440) + 2)
        store32(v4 + 20, (((load32(9142440) + 2) * v0) * 3))
    while True:  # block $label10
        if load32(9147132):
            break
        if (load32(load32(9142424) + 48) == 0):
            break
        if load8u(9147152):
            break
        v3 = load32(9671136)
        if (u(load32(9671136)) < u(4)):
            break
        v0 = load32(9671128)
        v1 = 3
        while True:  # $label12
            while True:  # block $label11
                v2 = (v0 + (v1 * 132))
                if (load8u((v0 + (v1 * 132)) + 125) == 3):
                    break
                if (load32(v2 + 28) == 0):
                    break
                if load32(v2 + 36):
                    break
                v3 = load32(9671136)
                v0 = load32(9671128)
                break
            v1 = (v1 + 1)
            if (u((v1 + 1)) < u(v3)):
                continue
            break
        break
    while True:  # block $label13
        if (load8u(9147152) == 0):
            break
        if (load32(load32(9142424) + 48) == 0):
            break
        store32(v4, 0)
        store32(v4 + 4, load32(9142440))
        a_b()
        break
    G.global0 = (v4 + 32)

# ------------------------------------------------------------
# $func320
# ------------------------------------------------------------
def func320(arg0):
    v3 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    if (load8u(9142917) == 0):
        if (arg0 == 0):
            while True:  # block $label9
                while True:  # block $label5
                    while True:  # block $label4
                        while True:  # block $label2
                            if (load8u(9142916) == 0):
                                while True:  # block $label1
                                    while True:  # block $label0
                                        arg0 = load32(9299880)
                                        if load32(9299880):
                                            arg0 = (arg0 - 1)
                                            store32(9299880, (arg0 - 1))
                                            arg0 = load32((load32(9299872) + (arg0 << 2)))
                                            break
                                        arg0 = load32(9163776)
                                        v1 = (load32(9163776) + 1)
                                        store32(9163776, (load32(9163776) + 1))
                                        v2 = load32(9163784)
                                        if (u(v1) >= u(load32(9163784))):
                                            break
                                        break
                                    store32(9142888, arg0)
                                    break
                                    break
                                store32(v3 + 64, v2)
                                a_b()
                                store32(9142888, arg0)
                                store32(9163784, (load32(9163784) + 40000))
                                if (load8u(9142916) == 0):
                                    break
                            while True:  # block $label3
                                arg0 = load32(9299896)
                                if load32(9299896):
                                    arg0 = (arg0 - 1)
                                    store32(9299896, (arg0 - 1))
                                    arg0 = load32((load32(9299888) + (arg0 << 2)))
                                    break
                                arg0 = load32(9163780)
                                v1 = (load32(9163780) + 1)
                                store32(9163780, (load32(9163780) + 1))
                                v2 = load32(9163788)
                                if (u(v1) < u(load32(9163788))):
                                    break
                                store32(v3 + 48, v2)
                                a_b()
                                store32(9163788, (load32(9163788) + 40000))
                                break
                            arg0 = (arg0 + 1073741823)
                            break
                            break
                        if load8u(9142917):
                            store32(9142884, 0)
                            break
                        arg0 = load32(9299880)
                        if load32(9299880):
                            arg0 = (arg0 - 1)
                            store32(9299880, (arg0 - 1))
                            arg0 = load32((load32(9299872) + (arg0 << 2)))
                            break
                        arg0 = load32(9163776)
                        v1 = (load32(9163776) + 1)
                        store32(9163776, (load32(9163776) + 1))
                        v2 = load32(9163784)
                        if (u(v1) < u(load32(9163784))):
                            break
                        store32(v3 + 32, v2)
                        a_b()
                        store32(9163784, (load32(9163784) + 40000))
                        break
                    store32(9142884, arg0)
                    if load8u(9142917):
                        break
                    while True:  # block $label8
                        while True:  # block $label7
                            while True:  # block $label6
                                arg0 = load32(9299880)
                                if load32(9299880):
                                    arg0 = (arg0 - 1)
                                    store32(9299880, (arg0 - 1))
                                    v1 = load32((load32(9299872) + (arg0 << 2)))
                                    break
                                arg0 = 0
                                v1 = load32(9163776)
                                v2 = (load32(9163776) + 1)
                                store32(9163776, (load32(9163776) + 1))
                                v4 = load32(9163784)
                                if (u(v2) >= u(load32(9163784))):
                                    break
                                break
                            store32(9142876, v1)
                            break
                            break
                        store32(v3 + 16, v4)
                        a_b()
                        store32(9142876, v1)
                        store32(9163784, (load32(9163784) + 40000))
                        if load8u(9142917):
                            break
                        break
                    arg0 = load32(9299880)
                    if load32(9299880):
                        arg0 = (arg0 - 1)
                        store32(9299880, (arg0 - 1))
                        arg0 = load32((load32(9299872) + (arg0 << 2)))
                        break
                    arg0 = load32(9163776)
                    v1 = (load32(9163776) + 1)
                    store32(9163776, (load32(9163776) + 1))
                    v2 = load32(9163784)
                    if (u(v1) < u(load32(9163784))):
                        break
                    store32(v3, v2)
                    a_b()
                    store32(9163784, (load32(9163784) + 40000))
                    break
                    break
                arg0 = 0
                store32(9142876, 0)
                break
            store32(9142880, arg0)
        while True:  # block $label13
            while True:  # block $label14
                while True:  # block $label11
                    while True:  # block $label10
                        arg0 = load32(9142640)
                        if (load32(9142640) == 0):
                            break
                        if (load32(arg0 + 20) == 0):
                            break
                        v1 = load8u(9142916)
                        if (load32(arg0 + 28) != 2147483647):
                            break
                        while True:  # block $label12
                            if v1:
                                v2 = load32(59152)
                                store32(59152, (load32(59152) + 1))
                                v4 = load32(9568052)
                                v5 = load32(arg0)
                                break
                            v5 = load32(arg0)
                            v4 = load32(9568052)
                            v2 = ((load32(arg0) + load32(9140308)) + ((load32(9568052) & 0xFFFFFFFF) >> 2))
                            break
                        store32(arg0 + 28, v2)
                        v2 = load32(arg0 + 4)
                        v6 = load32(9568048)
                        store32(9568048, (load32(9568048) + 1))
                        store32(((v6 << 2) + 9563952), arg0)
                        store32(9568052, (((v5 * (v2 + 2)) << 2) + v4))
                        if (v1 == 0):
                            break
                        v1 = load32(9568056)
                        store32(arg0 + 56, load32(9568056))
                        store32(9568056, (v1 + ((v2 * load32(arg0)) << 2)))
                        break
                    if load8u(9142916):
                        break
                    break
                    break
                if v1:
                    break
                break
            break
    G.global0 = (v3 + 80)

# ------------------------------------------------------------
# $func321
# ------------------------------------------------------------
def func321(arg0, arg1, arg2):
    if (arg2 >= 0):
        v11 = load16u(arg1 + 2)
        v8 = (4 if load16u(arg1 + 2) else 3)
        v5 = (7 if v11 else 138)
        v9 = (arg0 + 5817)
        v6 = -1
        while True:  # $label12
            v10 = v11
            v14 = v13
            v13 = (v13 + 1)
            v11 = load16u((arg1 + ((v13 + 1) << 2)) + 2)
            while True:  # block $label1
                while True:  # block $label0
                    v3 = (v4 + 1)
                    if ((v4 + 1) >= v5):
                        break
                    if (v10 != v11):
                        break
                    v4 = v3
                    break
                    break
                while True:  # block $label4
                    if (v3 < v8):
                        v4 = (arg0 + (v10 << 2))
                        v5 = ((arg0 + (v10 << 2)) + 2686)
                        v7 = (v4 + 2684)
                        v4 = load32(arg0 + 5820)
                        while True:  # $label3
                            v12 = load16u(v5)
                            v8 = load16u(v7)
                            v6 = (load16u(arg0 + 5816) | (load16u(v7) << v4))
                            store16(arg0 + 5816, (load16u(arg0 + 5816) | (load16u(v7) << v4)))
                            while True:  # block $label2
                                if ((16 - v12) < v4):
                                    v4 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v4 + load32(arg0 + 8)), v6)
                                    v4 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v4 + load32(arg0 + 8)), load8u(v9))
                                    v4 = load32(arg0 + 5820)
                                    store16(arg0 + 5816, ((v8 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                    break
                                break
                            v4 = (v4 + v12)
                            store32(((v4 + v12) - 16) + 5820, (v4 + v12))
                            v3 = (v3 - 1)
                            if (v3 - 1):
                                continue
                            break
                        break
                    while True:  # block $label8
                        if v10:
                            while True:  # block $label5
                                if (v6 == v10):
                                    v5 = load32(arg0 + 5820)
                                    v4 = v3
                                    break
                                v3 = (arg0 + (v10 << 2))
                                v7 = load16u(((arg0 + (v10 << 2)) + 2686))
                                v8 = load16u((v3 + 2684))
                                v3 = load32(arg0 + 5820)
                                v6 = (load16u(arg0 + 5816) | (load16u((v3 + 2684)) << load32(arg0 + 5820)))
                                store16(arg0 + 5816, (load16u(arg0 + 5816) | (load16u((v3 + 2684)) << load32(arg0 + 5820))))
                                while True:  # block $label6
                                    if ((16 - v7) < v3):
                                        v3 = load32(arg0 + 20)
                                        store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                        store8((v3 + load32(arg0 + 8)), v6)
                                        v3 = load32(arg0 + 20)
                                        store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                        store8((v3 + load32(arg0 + 8)), load8u(v9))
                                        v3 = load32(arg0 + 5820)
                                        store16(arg0 + 5816, ((v8 & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                        break
                                    break
                                v5 = (v3 + v7)
                                store32(((v3 + v7) - 16) + 5820, (v3 + v7))
                                break
                            v8 = load16u(arg0 + 2748)
                            v3 = (load16u(arg0 + 5816) | (load16u(arg0 + 2748) << v5))
                            while True:  # block $label7
                                v7 = load16u(arg0 + 2750)
                                if ((16 - load16u(arg0 + 2750)) < v5):
                                    store16(arg0 + 5816, v3)
                                    v6 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v6 + load32(arg0 + 8)), v3)
                                    v3 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v3 + load32(arg0 + 8)), load8u(v9))
                                    v3 = load32(arg0 + 5820)
                                    v5 = ((v7 + load32(arg0 + 5820)) - 16)
                                    v3 = ((v8 & 0xFFFFFFFF) >> (16 - v3))
                                    break
                                v5 = (v5 + v7)
                                break
                            store32(arg0 + 5820, v5)
                            v6 = (v4 + 65533)
                            if (v5 >= 15):
                                v3 = (v3 | (v6 << v5))
                                store16(arg0 + 5816, (v3 | (v6 << v5)))
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), v3)
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), load8u(v9))
                                v4 = load32(arg0 + 5820)
                                store16(arg0 + 5816, (((v6 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                break
                            store16(arg0 + 5816, (v3 | (v6 << v5)))
                            break
                        v3 = load16u(arg0 + 5816)
                        v6 = load32(arg0 + 5820)
                        if (v4 <= 9):
                            v8 = load16u(arg0 + 2752)
                            v3 = (v3 | (load16u(arg0 + 2752) << v6))
                            while True:  # block $label9
                                v7 = load16u(arg0 + 2754)
                                if ((16 - load16u(arg0 + 2754)) < v6):
                                    store16(arg0 + 5816, v3)
                                    v6 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v6 + load32(arg0 + 8)), v3)
                                    v3 = load32(arg0 + 20)
                                    store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                    store8((v3 + load32(arg0 + 8)), load8u(v9))
                                    v3 = load32(arg0 + 5820)
                                    v5 = ((v7 + load32(arg0 + 5820)) - 16)
                                    v3 = ((v8 & 0xFFFFFFFF) >> (16 - v3))
                                    break
                                v5 = (v6 + v7)
                                break
                            store32(arg0 + 5820, v5)
                            v6 = (v4 + 65534)
                            if (v5 >= 14):
                                v3 = (v3 | (v6 << v5))
                                store16(arg0 + 5816, (v3 | (v6 << v5)))
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), v3)
                                v4 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v4 + load32(arg0 + 8)), load8u(v9))
                                v4 = load32(arg0 + 5820)
                                store16(arg0 + 5816, (((v6 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                                break
                            store16(arg0 + 5816, (v3 | (v6 << v5)))
                            break
                        v8 = load16u(arg0 + 2756)
                        v3 = (v3 | (load16u(arg0 + 2756) << v6))
                        while True:  # block $label10
                            v7 = load16u(arg0 + 2758)
                            if ((16 - load16u(arg0 + 2758)) < v6):
                                store16(arg0 + 5816, v3)
                                v6 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v6 + load32(arg0 + 8)), v3)
                                v3 = load32(arg0 + 20)
                                store32(arg0 + 20, (load32(arg0 + 20) + 1))
                                store8((v3 + load32(arg0 + 8)), load8u(v9))
                                v3 = load32(arg0 + 5820)
                                v5 = ((v7 + load32(arg0 + 5820)) - 16)
                                v3 = ((v8 & 0xFFFFFFFF) >> (16 - v3))
                                break
                            v5 = (v6 + v7)
                            break
                        store32(arg0 + 5820, v5)
                        v6 = (v4 + 65526)
                        if (v5 >= 10):
                            v3 = (v3 | (v6 << v5))
                            store16(arg0 + 5816, (v3 | (v6 << v5)))
                            v4 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v4 + load32(arg0 + 8)), v3)
                            v4 = load32(arg0 + 20)
                            store32(arg0 + 20, (load32(arg0 + 20) + 1))
                            store8((v4 + load32(arg0 + 8)), load8u(v9))
                            v4 = load32(arg0 + 5820)
                            store16(arg0 + 5816, (((v6 & 65535) & 0xFFFFFFFF) >> (16 - load32(arg0 + 5820))))
                            break
                        store16(arg0 + 5816, (v3 | (v6 << v5)))
                        break
                    store32((v4 - 9) + 5820, (v5 + 7))
                    break
                v4 = 0
                while True:  # block $label11
                    if (v11 == 0):
                        v5 = 138
                        break
                    v3 = (v10 == v11)
                    v5 = (6 if (v10 == v11) else 7)
                    break
                v8 = (3 if v3 else 4)
                v6 = v10
                break
            if (arg2 != v14):
                continue
            break
    return 3

# ------------------------------------------------------------
# $func322
# ------------------------------------------------------------
def func322(arg0, arg1, arg2):
    v6 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v7 = load32(9561692)
    while True:  # block $label2
        while True:  # block $label1
            while True:  # block $label0
                if load32(9147132):
                    if (load32(9142440) == 4096):
                        break
                v3 = load32(arg2)
                break
                break
            v3 = load32(arg2)
            if (u((load32(arg2) + load32(((v7 + (arg1 * 286704)) + 281724)))) < u(1000001)):
                break
            if (load32(9142872) != arg1):
                break
            store64(v6, 4294967296000930)
            a_b()
            break
            break
        if (v3 < 0):
            break
        v4 = load32(arg2 + 4)
        if (load32(arg2 + 4) < 0):
            break
        v5 = load32(arg2 + 8)
        if (load32(arg2 + 8) < 0):
            break
        v8 = load32(arg2 + 12)
        if (load32(arg2 + 12) < 0):
            break
        while True:  # block $label3
            if v3:
                break
            if v4:
                break
            if v5:
                break
            if (v8 == 0):
                break
            break
        if load8u((load32(9143004) + ((load32(9142892) * arg1) + arg0))):
            break
        v11 = (v7 + (arg1 * 286704))
        if func66((v7 + (arg1 * 286704)), arg2, 1, 0):
            break
        v4 = (v7 + (arg1 * 286704))
        v3 = ((v7 + (arg1 * 286704)) + 281724)
        store32(((v7 + (arg1 * 286704)) + 281724), (load32(v3) + load32(arg2)))
        v3 = (v7 + (arg0 * 286704))
        v5 = ((v7 + (arg0 * 286704)) + 281708)
        store32(((v7 + (arg0 * 286704)) + 281708), (load32(v5) + load32(arg2)))
        v5 = (v4 + 281728)
        store32((v4 + 281728), (load32(v5) + load32(arg2 + 4)))
        v5 = (v3 + 281712)
        store32((v3 + 281712), (load32(v5) + load32(arg2 + 4)))
        v5 = (v4 + 281732)
        store32((v4 + 281732), (load32(v5) + load32(arg2 + 8)))
        v5 = (v3 + 281716)
        store32((v3 + 281716), (load32(v5) + load32(arg2 + 8)))
        v4 = (v4 + 281736)
        store32((v4 + 281736), (load32(v4) + load32(arg2 + 12)))
        v4 = (v3 + 281720)
        store32((v3 + 281720), (load32(v4) + load32(arg2 + 12)))
        v4 = load32(v3 + 283848)
        if (load32(v3 + 283848) != 2147483647):
            store32((v3 + 283848), (load32(arg2) + v4))
        v3 = (v3 + 283852)
        v4 = load32((v3 + 283852))
        if (load32((v3 + 283852)) != 2147483647):
            store32(v3, (load32(arg2 + 4) + v4))
        v3 = (v7 + (arg0 * 286704))
        v4 = ((v7 + (arg0 * 286704)) + 283856)
        v5 = load32(((v7 + (arg0 * 286704)) + 283856))
        if (load32(((v7 + (arg0 * 286704)) + 283856)) != 2147483647):
            store32(v4, (load32(arg2 + 8) + v5))
        v3 = (v3 + 283860)
        v4 = load32((v3 + 283860))
        if (load32((v3 + 283860)) != 2147483647):
            store32(v3, (load32(arg2 + 12) + v4))
        v3 = 1
        v5 = (v7 + (arg0 * 286704))
        store8((v7 + (arg0 * 286704)) + 286701, 1)
        while True:  # block $label4
            v4 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v9 = (v4 - 1)
            v12 = ((v4 - 1) & 1)
            v5 = (load32(v5 + 283908) * v4)
            v8 = load32(9561692)
            v10 = load32(9143016)
            if (v4 != 2):
                v9 = (v9 & -2)
                v4 = 0
                while True:  # $label5
                    if load8u((v10 + (v3 + v5))):
                        store8((v8 + (v3 * 286704)) + 286701, 1)
                    v13 = (v3 + 1)
                    if load8u((v10 + ((v3 + 1) + v5))):
                        store8((v8 + (v13 * 286704)) + 286701, 1)
                    v3 = (v3 + 2)
                    v4 = (v4 + 2)
                    if ((v4 + 2) != v9):
                        continue
                    break
            if (v12 == 0):
                break
            if (load8u((v10 + (v3 + v5))) == 0):
                break
            store8((v8 + (v3 * 286704)) + 286701, 1)
            break
        if (load32(9142872) != arg0):
            break
        v14 = load64(arg2)
        v15 = load64(arg2 + 8)
        store32(v6 + 36, load32((v7 + (arg1 * 286704)) + 284616))
        store32(v6 + 32, v11)
        store64(v6 + 24, v15)
        store64(v6 + 16, v14)
        a_b()
        break
    G.global0 = (v6 + 48)

# ------------------------------------------------------------
# $func323
# ------------------------------------------------------------
def func323(arg0, arg1):
    while True:  # block $label0
        v2 = load32(arg0 + 20)
        if (load32(arg0 + 20) == 0):
            break
        if (u(load32(v2 + 8)) < u(2)):
            break
        v2 = load32(v2)
        if (load32(load32(v2)) != 2):
            break
        break
    v10 = load32(v2 + 4)
    v2 = load16u(arg0 + 110)
    v4 = load32(9561692)
    v3 = load32(arg0 + 88)
    v11 = ((load32(arg0 + 88) & 0xFFFFFFFF) >> 16)
    v5 = load16u(arg0 + 108)
    v14 = load32(arg0 + 28)
    v7 = load32(9671128)
    while True:  # block $label5
        while True:  # block $label3
            while True:  # block $label4
                while True:  # block $label2
                    while True:  # block $label1
                        v6 = (v3 & 65535)
                        # br_table[(v3 & 65535)]
                        break
                        break
                    break
                    break
                break
                break
            break
            break
        if (load32(38528) == v11):
            break
        if (load32(((v11 * 404) + 9568096) + 268) == 3):
            break
        if (load32(38712) == load8u(arg0 + 122)):
            break
        break
    v3 = ((v4 + (v2 * 286704)) + 281648)
    store32(((v4 + (v2 * 286704)) + 281648), (load32(v3) + v5))
    while True:  # block $label6
        v8 = (v4 + (v2 * 286704))
        v3 = (((v4 + (v2 * 286704)) + (v6 << 2)) + 283848)
        v6 = load32((((v4 + (v2 * 286704)) + (v6 << 2)) + 283848))
        if (load32((((v4 + (v2 * 286704)) + (v6 << 2)) + 283848)) == 2147483647):
            break
        store32(v3, (v5 + v6))
        v3 = 1
        store8(v8 + 286701, 1)
        v5 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v9 = (v5 - 1)
        v12 = ((v5 - 1) & 1)
        v4 = (load32((v4 + (v2 * 286704)) + 283908) * v5)
        v6 = load32(9561692)
        v8 = load32(9143016)
        if (v5 != 2):
            v5 = (v9 & -2)
            v2 = 0
            while True:  # $label7
                if load8u((v8 + (v3 + v4))):
                    store8((v6 + (v3 * 286704)) + 286701, 1)
                v9 = (v3 + 1)
                if load8u((v8 + ((v3 + 1) + v4))):
                    store8((v6 + (v9 * 286704)) + 286701, 1)
                v3 = (v3 + 2)
                v2 = (v2 + 2)
                if ((v2 + 2) != v5):
                    continue
                break
        if (v12 == 0):
            break
        if (load8u((v8 + (v3 + v4))) == 0):
            break
        store8((v6 + (v3 * 286704)) + 286701, 1)
        break
    store16(arg0 + 108, 0)
    if (arg1 == 0):
        store8(arg0 + 125, 0)
        while True:  # block $label8
            if (load32(arg0 + 92) == 0):
                break
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
        arg1 = ((v11 * 404) + 9568096)
        if (load32(((v11 * 404) + 9568096) + 268) == 3):
            v6 = load32(9142440)
            v12 = (load32(9142440) + 2)
            v15 = ((load32(9142440) + 2) * load32(arg1 + 208))
            v8 = load16u(arg0 + 112)
            v16 = (load16u(arg0 + 112) + 29)
            v9 = load16u(arg0 + 114)
            v17 = (load16u(arg0 + 114) + 29)
            v10 = (v9 - 30)
            v2 = (v8 - 30)
            v18 = load32(9671128)
            v19 = load32(9142840)
            v5 = 2147483647
            v7 = 0
            while True:  # $label11
                v4 = (v2 + 1)
                if (u(v2) < u(v6)):
                    arg1 = (v8 - v2)
                    v20 = ((v8 - v2) * arg1)
                    arg1 = v10
                    while True:  # $label10
                        while True:  # block $label9
                            v3 = arg1
                            if (u(v6) <= u(arg1)):
                                break
                            if ((v2 | v3) < 0):
                                break
                            arg1 = (v9 - v3)
                            v13 = (((v9 - v3) * arg1) + v20)
                            if ((((v9 - v3) * arg1) + v20) >= v5):
                                break
                            arg1 = load32((v19 + (((((v3 + v15) + 1) * v12) + v4) << 2)))
                            if (load32((v19 + (((((v3 + v15) + 1) * v12) + v4) << 2))) == 0):
                                break
                            v13 = (v11 == load8u((v18 + (arg1 * 132)) + 122))
                            v5 = (v13 if (v11 == load8u((v18 + (arg1 * 132)) + 122)) else v5)
                            v7 = (arg1 if v13 else v7)
                            break
                        arg1 = (v3 + 1)
                        if (v3 != v17):
                            continue
                        break
                arg1 = (v2 != v16)
                v2 = v4
                if arg1:
                    continue
                break
            if v7:
                return func28(1, 1)
            func404(v14)
            return ((v4 + (v2 * 286704)) + 281664)
        while True:  # block $label12
            if (v11 == load32(38528)):
                break
            v2 = (v7 + (v10 * 132))
            arg1 = load32((v7 + (v10 * 132)) + 28)
            if (load32((v7 + (v10 * 132)) + 28) == 0):
                break
            while True:  # block $label13
                if (load8u(v2 + 125) == 10):
                    break
                if (u(load32(((load8u((v7 + (v10 * 132)) + 122) * 404) + 9568096) + 188)) < u(4)):
                    break
                func29(arg0, 1)
                return ((v4 + (v2 * 286704)) + 281644)
                break
            if load8u(9142916):
            else:
            return arg0
            break
        func404(v14)
    return ((v4 + (v2 * 286704)) + 281640)

# ------------------------------------------------------------
# $func324
# ------------------------------------------------------------
def func324():
    v9 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    store32(9143000, 0)
    v1 = load32(59144)
    v2 = load32(59136)
    v0 = load32(59140)
    v4 = load32(59132)
    v6 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (v6 * 132)))
        store32(9213820, 0)
    if (load8u(9163792) == 0):
        func45()
    if (load8u(9147152) == 0):
        func52((207 if load8u(9143020) else 0), 0)
        a_b()
    while True:  # block $label21
        while True:  # block $label24
            while True:  # block $label1
                while True:  # block $label0
                    if (u(((v4 - v2) if (u(v2) < u(v4)) else (v2 - v4))) > u(12)):
                        break
                    if (u(((v0 - v1) if (u(v0) > u(v1)) else (v1 - v0))) > u(12)):
                        break
                    v2 = func141(v4, v0)
                    if (((a_f() - load32(9681904)) < 500.0) == 0):
                        break
                    if (u(v2) < u(3)):
                        break
                    v1 = (load32(9681912) - v4)
                    v1 = (load32(9681916) - v0)
                    if (((((load32(9681912) - v4) * v1) + ((load32(9681916) - v0) * v1)) - 1) > 100):
                        break
                    v6 = load32(9671128)
                    v1 = (load32(9671128) + (v2 * 132))
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v1 + 110))))) == 0):
                            break
                        v5 = (v6 + (v2 * 132))
                        if (load32((load32(9215884) + (load32((v6 + (v2 * 132)) + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v5 + 127) == 6):
                            break
                        if load8u(9163793):
                        else:
                        v15 = -1
                        v2 = (v6 + (v2 * 132))
                        v1 = load8u((v6 + (v2 * 132)) + 125)
                        v10 = load8u(v2 + 122)
                        if (load8u(9163792) == 0):
                            func45()
                        while True:  # block $label2
                            v20 = load32(40616)
                            # TODO: f32.convert_i32_u []
                            v21 = load32(9142860)
                            v22 = load32(9671164)
                            v23 = ((load32(40616) * load32(9142860)) / load32(9671164))
                            v24 = ceil(((((load32(40616) * load32(9142860)) / load32(9671164)) + 32.0) * 0.03125))
                            if (abs(ceil(((((load32(40616) * load32(9142860)) / load32(9671164)) + 32.0) * 0.03125))) < 2147483650.0):
                                break
                            break
                        v0 = -2147483648
                        while True:  # block $label3
                            v21 = ((((v21 - v23) * 0.5) + float(load32(9142956))) * 0.03125)
                            if (abs(((((v21 - v23) * 0.5) + float(load32(9142956))) * 0.03125)) < 2147483650.0):
                                break
                            break
                        v2 = -2147483648
                        while True:  # block $label4
                            # TODO: f32.convert_i32_u []
                            v20 = load32(9142856)
                            v21 = ((v20 * load32(9142856)) / v22)
                            v22 = ceil(((((v20 * load32(9142856)) / v22) + 32.0) * 0.03125))
                            if (abs(ceil(((((v20 * load32(9142856)) / v22) + 32.0) * 0.03125))) < 2147483650.0):
                                break
                            break
                        v6 = -2147483648
                        while True:  # block $label5
                            v20 = ((((v20 - v21) * 0.5) + float(load32(9142952))) * 0.03125)
                            if (abs(((((v20 - v21) * 0.5) + float(load32(9142952))) * 0.03125)) < 2147483650.0):
                                break
                            break
                        v4 = -2147483648
                        while True:  # block $label6
                            if (v6 <= 0):
                                break
                            if (v0 <= 0):
                                break
                            v13 = ((v1 == 4) | (v1 == 14))
                            v16 = (v0 + v2)
                            v17 = (v4 + v6)
                            v18 = ((v10 * 404) + 9568360)
                            v3 = load32(9142440)
                            while True:  # $label20
                                v6 = (v4 + 1)
                                v0 = v2
                                while True:  # $label19
                                    while True:  # block $label9
                                        while True:  # block $label8
                                            while True:  # block $label7
                                                if ((v0 | v4) < 0):
                                                    break
                                                if (u(v3) <= u(v4)):
                                                    break
                                                if (u(v0) < u(v3)):
                                                    break
                                                break
                                            break
                                            break
                                        v1 = 0
                                        v14 = (v0 + 1)
                                        v19 = (v4 if (u(v0) < u(v4)) else v0)
                                        if (u((v4 if (u(v0) < u(v4)) else v0)) >= u(v3)):
                                            break
                                        while True:  # $label18
                                            while True:  # block $label10
                                                if (u(v3) <= u(v19)):
                                                    break
                                                v5 = (v3 + 2)
                                                v5 = load32((load32(9142840) + ((v6 + ((v14 + ((v3 + 2) * v1)) * v5)) << 2)))
                                                if (u(load32((load32(9142840) + ((v6 + ((v14 + ((v3 + 2) * v1)) * v5)) << 2)))) < u(3)):
                                                    break
                                                while True:  # block $label12
                                                    while True:  # block $label11
                                                        v7 = load32(load32(9142424) + 48)
                                                        v8 = load8u(9147152)
                                                        if ((0 if load8u(9147152) else load32(load32(9142424) + 48)) == 0):
                                                            v5 = (load32(9671128) + (v5 * 132))
                                                            if (v8 == 0):
                                                                break
                                                            break
                                                        v8 = load16u((load32(9147376) + (((v0 * v3) + v4) << 1)))
                                                        while True:  # block $label13
                                                            if (v7 != 2):
                                                                if v8:
                                                                    break
                                                                break
                                                            if (u(v8) < u(2)):
                                                                break
                                                            break
                                                        break
                                                    v5 = (load32(9671128) + (v5 * 132))
                                                    if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v5 + 110))))) == 0):
                                                        break
                                                    if (load32((load32(9215884) + (load32(v5 + 44) << 4)) + 4) == 20):
                                                        break
                                                    if (load8u(v5 + 127) == 6):
                                                        break
                                                    break
                                                while True:  # block $label14
                                                    v7 = load8u(v5 + 125)
                                                    v8 = ((load8u(v5 + 125) == 4) | (v7 == 14))
                                                    if ((v13 & ((load8u(v5 + 125) == 4) | (v7 == 14))) == 0):
                                                        if (v8 | v13):
                                                            break
                                                        if (v7 != 5):
                                                            break
                                                        break
                                                    if (v7 == 5):
                                                        break
                                                    break
                                                v8 = load8u(v5 + 122)
                                                v11 = load8u(9163793)
                                                while True:  # block $label16
                                                    while True:  # block $label15
                                                        v12 = load8u(9163794)
                                                        if load8u(9163794):
                                                            break
                                                        if v11:
                                                            break
                                                        if (v8 == v10):
                                                            break
                                                        break
                                                    while True:  # block $label17
                                                        if (v12 == 0):
                                                            break
                                                        v12 = ((v8 * 404) + 9568096)
                                                        if load32(((v8 * 404) + 9568096) + 264):
                                                            break
                                                        if (load32(v12 + 268) == 1):
                                                            break
                                                        if (load32(v12 + 92) == 0):
                                                            break
                                                        if (load32(38456) == v8):
                                                            break
                                                        if (load32(38764) == v8):
                                                            break
                                                        if (v7 != 8):
                                                            break
                                                        break
                                                    if (v11 == 0):
                                                        break
                                                    if (func287(v5) != v15):
                                                        break
                                                    if (v8 != v10):
                                                        break
                                                    if (load32(v18) == 1):
                                                        break
                                                    break
                                                func44(v5, 0)
                                                v3 = load32(9142440)
                                                break
                                            v1 = (v1 + 1)
                                            if ((v1 + 1) != 3):
                                                continue
                                            break
                                        break
                                    v0 = v14
                                    if ((v0 + 1) > v14):
                                        continue
                                    break
                                v4 = v6
                                if (v6 < v17):
                                    continue
                                break
                            break
                        break
                    v4 = load16u(v1 + 110)
                    v6 = load8u(v1 + 126)
                    v2 = (G.global0 - 16)
                    G.global0 = (G.global0 - 16)
                    while True:  # block $label23
                        while True:  # block $label22
                            v0 = load32(v1 + 24)
                            if (load32(v1 + 24) == 0):
                                break
                            v0 = load32(v0 + 8)
                            if (load32(v0 + 8) == 0):
                                break
                            v5 = load32(v0 + 8)
                            if (load32(v0 + 8) == 0):
                                break
                            store32(v2 + 4, load32(v0))
                            store32(v2, v5)
                            a_b()
                            break
                            break
                        a_b()
                        break
                    G.global0 = (v2 + 16)
                    v2 = load32(v1 + 52)
                    v25 = load64(v1 + 64)
                    v0 = load32(v1 + 60)
                    v26 = load64(v1 + 72)
                    v5 = load32(v1 + 84)
                    v8 = load8u(v1 + 122)
                    v3 = load32(v1 + 28)
                    store32(v9 + 36, (2147483647 if (v6 == 2) else v4))
                    store32(v9 + 32, v3)
                    store32(v9 + 28, v8)
                    store32(v9 + 24, v5)
                    store64(v9 + 16, v26)
                    store32(v9 + 4, v0)
                    store64(v9 + 8, v25)
                    store32(v9, v2)
                    func44(v1, 0)
                    break
                    break
                v2 = (v2 // 32)
                v4 = (v4 // 32)
                v6 = ((v2 // 32) if (v2 < v4) else (v4 // 32))
                v5 = (((v2 // 32) if (v2 < v4) else (v4 // 32)) if (v6 > 0) else 0)
                v2 = (v2 if (v2 > v4) else v4)
                v4 = load32(9142440)
                v6 = (load32(9142440) - 1)
                v13 = ((v2 if (v2 > v4) else v4) if (u(v2) < u(v4)) else (load32(9142440) - 1))
                if ((((v2 // 32) if (v2 < v4) else (v4 // 32)) if (v6 > 0) else 0) > ((v2 if (v2 > v4) else v4) if (u(v2) < u(v4)) else (load32(9142440) - 1))):
                    break
                v1 = (v1 // 32)
                v2 = (v0 // 32)
                v0 = ((v1 // 32) if (v1 < v2) else (v0 // 32))
                v8 = (((v1 // 32) if (v1 < v2) else (v0 // 32)) if (v0 > 0) else 0)
                v1 = (v1 if (v1 > v2) else v2)
                v1 = ((v1 if (v1 > v2) else v2) if (u(v1) < u(v4)) else v6)
                if ((((v1 // 32) if (v1 < v2) else (v0 // 32)) if (v0 > 0) else 0) > ((v1 if (v1 > v2) else v2) if (u(v1) < u(v4)) else v6)):
                    break
                v14 = (v1 + 1)
                v4 = 0
                while True:  # $label34
                    v2 = v5
                    while True:  # $label33
                        v6 = (v2 + 1)
                        v1 = v8
                        while True:  # $label32
                            while True:  # block $label25
                                v3 = load32(9142440)
                                v0 = v1
                                if (((u(load32(9142440)) > u(v1)) & (u(v2) < u(v3))) == 0):
                                    v1 = (v0 + 1)
                                    break
                                v1 = (v0 + 1)
                                v7 = (v3 + 2)
                                v7 = load32((load32(9142840) + ((v6 + (((v0 + 1) + ((v3 + 2) * v4)) * v7)) << 2)))
                                if (u(load32((load32(9142840) + ((v6 + (((v0 + 1) + ((v3 + 2) * v4)) * v7)) << 2)))) < u(3)):
                                    break
                                v10 = load8u(9147152)
                                while True:  # block $label29
                                    while True:  # block $label28
                                        while True:  # block $label26
                                            v11 = load32(load32(9142424) + 48)
                                            if (load32(load32(9142424) + 48) == 0):
                                                break
                                            if v10:
                                                break
                                            v0 = load16u((load32(9147376) + (((v0 * v3) + v2) << 1)))
                                            while True:  # block $label27
                                                if (v11 == 2):
                                                    if (u(v0) > u(1)):
                                                        break
                                                    break
                                                if (v0 == 0):
                                                    break
                                                break
                                            v3 = (load32(9671128) + (v7 * 132))
                                            break
                                            break
                                        v3 = (load32(9671128) + (v7 * 132))
                                        if v10:
                                            break
                                        break
                                    if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v3 + 110))))) == 0):
                                        break
                                    if (load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) == 20):
                                        break
                                    if (load8u(v3 + 127) == 6):
                                        break
                                    if (load32(((load8u(v3 + 122) * 404) + 9568096) + 264) == 1):
                                        break
                                    break
                                if load32(v3 + 92):
                                    break
                                v7 = load32(9213808)
                                if (u(load32(9213808)) > u(9999)):
                                    break
                                if (load8u(v3 + 125) == 3):
                                    break
                                v0 = 1
                                v10 = load32(v3 + 28)
                                store32(9213808, (v7 + 1))
                                store32(((v7 << 2) + 9173808), v10)
                                while True:  # block $label30
                                    if (load8u(9142906) | load8u(9142916)):
                                        break
                                    v0 = 0
                                    if load8u(9142917):
                                        break
                                    v0 = load32(9299880)
                                    if load32(9299880):
                                        v0 = (v0 - 1)
                                        store32(9299880, (v0 - 1))
                                        v0 = load32((load32(9299872) + (v0 << 2)))
                                        break
                                    v0 = load32(9163776)
                                    v7 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v10 = load32(9163784)
                                    if (u(v7) < u(load32(9163784))):
                                        break
                                    store32(v9 + 64, v10)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    break
                                store32(v3 + 92, v0)
                                if (load32(v3 + 36) == 0):
                                if (load32(((load8u(v3 + 122) * 404) + 9568096) + 264) != 1):
                                    break
                                if load32(v3 + 80):
                                    break
                                v7 = load16u(v3 + 116)
                                if (load16u(v3 + 116) == 0):
                                    break
                                v10 = load16u(v3 + 118)
                                if (load16u(v3 + 118) == 0):
                                    break
                                if (load8u(9147152) == 0):
                                    if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v3 + 110))))) == 0):
                                        break
                                    if (load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) == 20):
                                        break
                                    if (load8u(v3 + 127) == 6):
                                        break
                                v0 = 0
                                while True:  # block $label31
                                    if load8u(9142917):
                                        break
                                    v0 = load32(9299880)
                                    if load32(9299880):
                                        v0 = (v0 - 1)
                                        store32(9299880, (v0 - 1))
                                        v0 = load32((load32(9299872) + (v0 << 2)))
                                        break
                                    v0 = load32(9163776)
                                    v11 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v12 = load32(9163784)
                                    if (u(v11) < u(load32(9163784))):
                                        break
                                    store32(v9 + 48, v12)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    v10 = load16u(v3 + 118)
                                    v7 = load16u(v3 + 116)
                                    break
                                store32(v3 + 80, v0)
                                # TODO: f32.convert_i32_u []
                                break
                            if (v1 != v14):
                                continue
                            break
                        v1 = (v2 != v13)
                        v2 = v6
                        if v1:
                            continue
                        break
                    v4 = (v4 + 1)
                    if ((v4 + 1) != 3):
                        continue
                    break
                break
                break
            v27 = a_f()
            store32(9681912, v4)
            store32(9681904, v27)
            store32(9681916, v0)
            if (u(v2) < u(3)):
                break
            v0 = load32(9671128)
            v1 = (load32(9671128) + (v2 * 132))
            while True:  # block $label35
                if (load8u(9147152) == 0):
                    if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v1 + 110))))) == 0):
                        break
                    v4 = (v0 + (v2 * 132))
                    if (load32((load32(9215884) + (load32((v0 + (v2 * 132)) + 44) << 4)) + 4) == 20):
                        break
                    if (load8u(v4 + 127) == 6):
                        break
                while True:  # block $label36
                    if (load32(v1 + 92) == 0):
                        break
                    if (load8u(9163792) == 0):
                        break
                    func77(v1)
                    break
                    break
                func44(v1, 0)
                break
                break
            v2 = (v0 + (v2 * 132))
            if (load8u(9163792) | load8u((v0 + (v2 * 132)) + 128)):
                break
            store32(9213820, load32(v2 + 28))
            func44(v1, 1)
            break
        break
    G.global0 = (v9 + 80)
    return func28(0, 0)

# ------------------------------------------------------------
# $func325
# ------------------------------------------------------------
def func325(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (arg0 * 132)))
        store32(9213820, 0)
    func45()
    v10 = (load32(9561692) + (load32(9142872) * 286704))
    while True:  # $label12
        while True:  # block $label1
            while True:  # block $label0
                if (v4 == load32(38440)):
                    break
                if (v4 == load32(38772)):
                    break
                if (v4 != load32(38928)):
                    break
                break
            v7 = load32(((v10 + (v4 << 2)) + 284636))
            if (load32(((v10 + (v4 << 2)) + 284636)) == 0):
                break
            v8 = 0
            v9 = load32(v7 + 8)
            if (load32(v7 + 8) == 0):
                break
            while True:  # $label11
                while True:  # block $label2
                    arg0 = load32((load32(v7) + (v8 << 2)))
                    if (load32((load32(v7) + (v8 << 2))) == 0):
                        break
                    v5 = load32(9671128)
                    v1 = (load32(9671128) + (arg0 * 132))
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v1 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v1 + 127) == 6):
                            break
                    v6 = load32(v1 + 28)
                    while True:  # block $label3
                        arg0 = load32(9215928)
                        if (load32(9215928) == 0):
                            break
                        v2 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        v3 = load32(arg0)
                        arg0 = 0
                        while True:  # $label4
                            if (load32((v5 + (load32((v3 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v2):
                                continue
                            break
                        break
                    while True:  # block $label5
                        arg0 = load32(9215932)
                        if (load32(9215932) == 0):
                            break
                        v2 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        v3 = load32(arg0)
                        arg0 = 0
                        while True:  # $label6
                            if (load32((v5 + (load32((v3 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v2):
                                continue
                            break
                        break
                    while True:  # block $label7
                        arg0 = load32(9215936)
                        if (load32(9215936) == 0):
                            break
                        v2 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        v3 = load32(arg0)
                        arg0 = 0
                        while True:  # $label8
                            if (load32((v5 + (load32((v3 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v2):
                                continue
                            break
                        break
                    while True:  # block $label9
                        arg0 = load32(9215940)
                        if (load32(9215940) == 0):
                            break
                        v2 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        v3 = load32(arg0)
                        arg0 = 0
                        while True:  # $label10
                            if (load32((v5 + (load32((v3 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v2):
                                continue
                            break
                        break
                    if load32(v1 + 36):
                        break
                    if (load8u(v1 + 125) == 8):
                        break
                    func44(v1, 0)
                    v9 = load32(v7 + 8)
                    break
                v8 = (v8 + 1)
                if (u((v8 + 1)) < u(v9)):
                    continue
                break
            break
        v4 = (v4 + 1)
        if ((v4 + 1) != 255):
            continue
        break

# ------------------------------------------------------------
# $func326
# ------------------------------------------------------------
def func326(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (arg0 * 132)))
        store32(9213820, 0)
    func45()
    v5 = (load32(9561692) + (load32(9142872) * 286704))
    while True:  # $label3
        while True:  # block $label0
            arg0 = ((v1 * 404) + 9568096)
            if load32(((v1 * 404) + 9568096) + 264):
                break
            if (load32(arg0 + 268) == 1):
                break
            if (load32(arg0 + 92) == 0):
                break
            if (load32(arg0 + 224) > 1):
                break
            v2 = load32(((v5 + (v1 << 2)) + 284636))
            if (load32(((v5 + (v1 << 2)) + 284636)) == 0):
                break
            v3 = 0
            v4 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                break
            while True:  # $label2
                while True:  # block $label1
                    arg0 = load32((load32(v2) + (v3 << 2)))
                    if (load32((load32(v2) + (v3 << 2))) == 0):
                        break
                    arg0 = (load32(9671128) + (arg0 * 132))
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(arg0 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(arg0 + 127) == 6):
                            break
                    if (func159(arg0) == 0):
                        break
                    if load32(arg0 + 36):
                        break
                    if (load8u(arg0 + 125) == 8):
                        break
                    if (load8u(arg0 + 123) == 63):
                        break
                    func44(arg0, 0)
                    v4 = load32(v2 + 8)
                    break
                v3 = (v3 + 1)
                if (u((v3 + 1)) < u(v4)):
                    continue
                break
            break
        v1 = (v1 + 1)
        if ((v1 + 1) != 255):
            continue
        break

# ------------------------------------------------------------
# $func327
# ------------------------------------------------------------
def func327(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (arg0 * 132)))
        store32(9213820, 0)
    func45()
    v10 = (load32(9561692) + (load32(9142872) * 286704))
    while True:  # $label11
        while True:  # block $label0
            if (load32(38456) != v4):
                if (v4 != load32(38764)):
                    break
            v7 = load32(((v10 + (v4 << 2)) + 284636))
            if (load32(((v10 + (v4 << 2)) + 284636)) == 0):
                break
            v8 = 0
            v9 = load32(v7 + 8)
            if (load32(v7 + 8) == 0):
                break
            while True:  # $label10
                while True:  # block $label1
                    arg0 = load32((load32(v7) + (v8 << 2)))
                    if (load32((load32(v7) + (v8 << 2))) == 0):
                        break
                    v5 = load32(9671128)
                    v3 = (load32(9671128) + (arg0 * 132))
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v3 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(v3 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v3 + 127) == 6):
                            break
                    v6 = load32(v3 + 28)
                    while True:  # block $label2
                        arg0 = load32(9215928)
                        if (load32(9215928) == 0):
                            break
                        v1 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        v2 = load32(arg0)
                        arg0 = 0
                        while True:  # $label3
                            if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v1):
                                continue
                            break
                        break
                    while True:  # block $label4
                        arg0 = load32(9215932)
                        if (load32(9215932) == 0):
                            break
                        v1 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        v2 = load32(arg0)
                        arg0 = 0
                        while True:  # $label5
                            if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v1):
                                continue
                            break
                        break
                    while True:  # block $label6
                        arg0 = load32(9215936)
                        if (load32(9215936) == 0):
                            break
                        v1 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        v2 = load32(arg0)
                        arg0 = 0
                        while True:  # $label7
                            if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v1):
                                continue
                            break
                        break
                    while True:  # block $label8
                        arg0 = load32(9215940)
                        if (load32(9215940) == 0):
                            break
                        v1 = load32(arg0 + 8)
                        if (load32(arg0 + 8) == 0):
                            break
                        v2 = load32(arg0)
                        arg0 = 0
                        while True:  # $label9
                            if (load32((v5 + (load32((v2 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v1):
                                continue
                            break
                        break
                    if load32(v3 + 36):
                        break
                    func44(v3, 0)
                    v9 = load32(v7 + 8)
                    break
                v8 = (v8 + 1)
                if (u((v8 + 1)) < u(v9)):
                    continue
                break
            break
        v4 = (v4 + 1)
        if ((v4 + 1) != 255):
            continue
        break

# ------------------------------------------------------------
# $func328
# ------------------------------------------------------------
def func328(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (arg0 * 132)))
        store32(9213820, 0)
    func45()
    v5 = (load32(9561692) + (load32(9142872) * 286704))
    arg0 = 0
    while True:  # $label4
        while True:  # block $label0
            v1 = ((arg0 * 404) + 9568096)
            if load32(((arg0 * 404) + 9568096) + 264):
                break
            if (load32(v1 + 268) == 1):
                break
            if (load32(v1 + 92) == 0):
                break
            while True:  # block $label1
                if (load32(38452) == arg0):
                    break
                if (load32(38496) == arg0):
                    break
                if (load32(38756) == arg0):
                    break
                if (load32(38692) == arg0):
                    break
                if (load32(38696) == arg0):
                    break
                if (load32(38776) == arg0):
                    break
                if (load32(38752) == arg0):
                    break
                if (load32(38704) != arg0):
                    break
                break
            v2 = load32(((v5 + (arg0 << 2)) + 284636))
            if (load32(((v5 + (arg0 << 2)) + 284636)) == 0):
                break
            v3 = 0
            v4 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                break
            while True:  # $label3
                while True:  # block $label2
                    v1 = load32((load32(v2) + (v3 << 2)))
                    if (load32((load32(v2) + (v3 << 2))) == 0):
                        break
                    v1 = (load32(9671128) + (v1 * 132))
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v1 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v1 + 127) == 6):
                            break
                    if (func159(v1) == 0):
                        break
                    if load32(v1 + 36):
                        break
                    if (load8u(v1 + 125) == 8):
                        break
                    if (load8u(v1 + 123) == 63):
                        break
                    func44(v1, 0)
                    v4 = load32(v2 + 8)
                    break
                v3 = (v3 + 1)
                if (u((v3 + 1)) < u(v4)):
                    continue
                break
            break
        arg0 = (arg0 + 1)
        if ((arg0 + 1) != 255):
            continue
        break

# ------------------------------------------------------------
# $func329
# ------------------------------------------------------------
def func329(arg0):
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
            v1 = ((v3 * 404) + 9568096)
            if load32(((v3 * 404) + 9568096) + 264):
                break
            if (load32(v1 + 268) == 1):
                break
            arg0 = (load32(v1 + 92) != 0)
            break
        while True:  # block $label1
            if (arg0 == 0):
                break
            if (v3 == load32(38456)):
                break
            if (v3 == load32(38764)):
                break
            if (v3 == load32(38428)):
                break
            v7 = load32(((v10 + (v3 << 2)) + 284636))
            if (load32(((v10 + (v3 << 2)) + 284636)) == 0):
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
                    v1 = (load32(9671128) + (arg0 * 132))
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v1 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v1 + 127) == 6):
                            break
                    v6 = load32(v1 + 28)
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
                            if (load32((v2 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
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
                            if (load32((v2 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
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
                            if (load32((v2 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
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
                            if (load32((v2 + (load32((v5 + (arg0 << 2))) * 132)) + 28) == v6):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v4):
                                continue
                            break
                        break
                    if load32(v1 + 36):
                        break
                    while True:  # block $label11
                        if (load8u(v1 + 125) == 8):
                            v2 = load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4)
                            if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 43):
                                break
                            arg0 = load8u(v1 + 123)
                            if (load8u(v1 + 123) == 43):
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
                        if (load8u(v1 + 123) == 63):
                            break
                        break
                    func44(v1, 0)
                    v9 = load32(v7 + 8)
                    break
                v8 = (v8 + 1)
                if (u((v8 + 1)) < u(v9)):
                    continue
                break
            break
        v3 = (v3 + 1)
        if ((v3 + 1) != 255):
            continue
        break

# ------------------------------------------------------------
# $func330
# ------------------------------------------------------------
def func330(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (arg0 * 132)))
        store32(9213820, 0)
    func45()
    while True:  # block $label0
        v1 = load32((((load32(9561692) + (load32(9142872) * 286704)) + (load32(38528) << 2)) + 284636))
        if (load32((((load32(9561692) + (load32(9142872) * 286704)) + (load32(38528) << 2)) + 284636)) == 0):
            break
        v3 = load32(v1 + 8)
        if (load32(v1 + 8) == 0):
            break
        while True:  # $label2
            while True:  # block $label1
                arg0 = load32((load32(v1) + (v2 << 2)))
                if (load32((load32(v1) + (v2 << 2))) == 0):
                    break
                arg0 = (load32(9671128) + (arg0 * 132))
                v4 = 1
                if load8u(9147152):
                else:
                    if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(arg0 + 110))))) == 0):
                        break
                    if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                        break
                if ((load8u(arg0 + 127) != 6) == 0):
                    break
                if (u(load32(arg0 + 80)) < u(450)):
                    break
                if (func159(arg0) == 0):
                    break
                if load32(arg0 + 36):
                    break
                func44(arg0, 0)
                v3 = load32(v1 + 8)
                break
            v2 = (v2 + 1)
            if (u((v2 + 1)) < u(v3)):
                continue
            break
        break
    return func28(0, 0)

# ------------------------------------------------------------
# $func331
# ------------------------------------------------------------
def func331(arg0):
    store32(9143000, 0)
    arg0 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (arg0 * 132)))
        store32(9213820, 0)
    func45()
    v5 = (load32(9561692) + (load32(9142872) * 286704))
    while True:  # $label3
        while True:  # block $label0
            arg0 = ((v1 * 404) + 9568096)
            if load32(((v1 * 404) + 9568096) + 264):
                break
            v2 = load32(arg0 + 268)
            if (load32(arg0 + 268) == 1):
                break
            if (load32(arg0 + 92) == 0):
                break
            if (load32(arg0 + 224) < 2):
                break
            if (v1 == load32(38456)):
                break
            if (v1 == load32(38764)):
                break
            if (v1 == load32(38932)):
                break
            if (v2 == 2):
                break
            v2 = load32(((v5 + (v1 << 2)) + 284636))
            if (load32(((v5 + (v1 << 2)) + 284636)) == 0):
                break
            v3 = 0
            v4 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                break
            while True:  # $label2
                while True:  # block $label1
                    arg0 = load32((load32(v2) + (v3 << 2)))
                    if (load32((load32(v2) + (v3 << 2))) == 0):
                        break
                    arg0 = (load32(9671128) + (arg0 * 132))
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(arg0 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(arg0 + 127) == 6):
                            break
                    if (func159(arg0) == 0):
                        break
                    if load32(arg0 + 36):
                        break
                    if (load8u(arg0 + 125) == 8):
                        break
                    if (load8u(arg0 + 123) == 63):
                        break
                    func44(arg0, 0)
                    v4 = load32(v2 + 8)
                    break
                v3 = (v3 + 1)
                if (u((v3 + 1)) < u(v4)):
                    continue
                break
            break
        v1 = (v1 + 1)
        if ((v1 + 1) != 255):
            continue
        break

# ------------------------------------------------------------
# $func332
# ------------------------------------------------------------
def func332(arg0):
    v1 = load32(9142872)
    v3 = load32(9561692)
    while True:  # block $label0
        if (arg0 != -1):
            if (load8u(9163792) == 0):
                break
        store32(9143000, 0)
        v2 = load32(9213820)
        if load32(9213820):
            func47((load32(9671128) + (v2 * 132)))
            store32(9213820, 0)
        func45()
        break
    while True:  # block $label1
        v4 = load32((((v3 + (v1 * 286704)) + (load32(38428) << 2)) + 284636))
        if (load32((((v3 + (v1 * 286704)) + (load32(38428) << 2)) + 284636)) == 0):
            break
        v1 = load32(v4 + 8)
        if (load32(v4 + 8) == 0):
            break
        v3 = 0
        if (arg0 == -1):
            while True:  # $label3
                while True:  # block $label2
                    v2 = load32((load32(v4) + (v3 << 2)))
                    if (load32((load32(v4) + (v3 << 2))) == 0):
                        break
                    v2 = (load32(9671128) + (v2 * 132))
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v2 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(v2 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v2 + 127) == 6):
                            break
                    func44(v2, 0)
                    v1 = load32(v4 + 8)
                    break
                v3 = (v3 + 1)
                if (u((v3 + 1)) < u(v1)):
                    continue
                break
                break
            raise RuntimeError('unreachable')
        while True:  # $label6
            while True:  # block $label4
                v1 = load32((load32(v4) + (v3 << 2)))
                if (load32((load32(v4) + (v3 << 2))) == 0):
                    break
                v1 = (load32(9671128) + (v1 * 132))
                if load8u(9163792):
                    if (load8u(9147152) == 0):
                        if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v1 + 110))))) == 0):
                            break
                        if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                            break
                        if (load8u(v1 + 127) == 6):
                            break
                    func44(v1, 0)
                    break
                v6 = load32(v1 + 28)
                while True:  # block $label5
                    v2 = load32(9681836)
                    if (load32(9681836) != load32(9681832)):
                        v1 = load32(9681828)
                        break
                    v1 = (load32(9681840) + v2)
                    store32(9681832, (load32(9681840) + v2))
                    v5 = load32(9681828)
                    v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
                    if v2:
                        # TODO: memory.copy []
                    if v5:
                        v2 = load32(9681836)
                    store32(9681828, v1)
                    break
                store32(9681836, (v2 + 1))
                store32((v1 + (v2 << 2)), v6)
                break
            v3 = (v3 + 1)
            if (u((v3 + 1)) < u(load32(v4 + 8))):
                continue
            break
        break
    while True:  # block $label7
        if (arg0 != -1):
            if (load8u(9163792) == 0):
                break
        return
        break
    func172(1)

# ------------------------------------------------------------
# $func333
# ------------------------------------------------------------
def func333(arg0):
    v1 = load32(9142872)
    v2 = load32(9561692)
    while True:  # block $label0
        if (arg0 != -1):
            if (load8u(9163792) == 0):
                break
        store32(9143000, 0)
        v3 = load32(9213820)
        if load32(9213820):
            func47((load32(9671128) + (v3 * 132)))
            store32(9213820, 0)
        func45()
        break
    v7 = (v2 + (v1 * 286704))
    v8 = (arg0 == -1)
    v3 = 0
    while True:  # $label7
        while True:  # block $label1
            v4 = load32(((v7 + (v3 << 2)) + 284636))
            if (load32(((v7 + (v3 << 2)) + 284636)) == 0):
                break
            v5 = 0
            if (load32(v4 + 8) == 0):
                break
            while True:  # $label6
                while True:  # block $label2
                    v1 = load32((load32(v4) + (v5 << 2)))
                    if (load32((load32(v4) + (v5 << 2))) == 0):
                        break
                    while True:  # block $label3
                        v1 = (load32(9671128) + (v1 * 132))
                        if (u(load32((load32(9671128) + (v1 * 132)) + 84)) >= u(12)):
                            if (load32(((load8u(v1 + 122) * 404) + 9568096) + 264) == 0):
                                break
                        v2 = load32(v1 + 24)
                        if (load32(v1 + 24) == 0):
                            break
                        if (load32(v2 + 8) == 0):
                            break
                        break
                    while True:  # block $label4
                        if (v8 == 0):
                            if (load8u(9163792) == 0):
                                break
                        if (load8u(9147152) == 0):
                            if (load8u((load32(9143008) + (load32(9142872) + (load32(9142892) * load16u(v1 + 110))))) == 0):
                                break
                            if (load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 20):
                                break
                            if (load8u(v1 + 127) == 6):
                                break
                        func44(v1, 0)
                        break
                        break
                    v9 = load32(v1 + 28)
                    while True:  # block $label5
                        v1 = load32(9681836)
                        if (load32(9681836) != load32(9681832)):
                            v2 = load32(9681828)
                            break
                        v2 = (load32(9681840) + v1)
                        store32(9681832, (load32(9681840) + v1))
                        v6 = load32(9681828)
                        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                        if v1:
                            # TODO: memory.copy []
                        if v6:
                            v1 = load32(9681836)
                        store32(9681828, v2)
                        break
                    store32(9681836, (v1 + 1))
                    store32((v2 + (v1 << 2)), v9)
                    break
                v5 = (v5 + 1)
                if (u((v5 + 1)) < u(load32(v4 + 8))):
                    continue
                break
            break
        v3 = (v3 + 1)
        if ((v3 + 1) != 255):
            continue
        break
    while True:  # block $label8
        if (arg0 != -1):
            if (load8u(9163792) == 0):
                break
        return
        break
    func172(1)

# ------------------------------------------------------------
# $func334
# ------------------------------------------------------------
def func334(arg0):
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(9143000, 0)
    arg0 = load32(9142872)
    v2 = load32(9561692)
    v3 = load32(9213820)
    if load32(9213820):
        func47((load32(9671128) + (v3 * 132)))
        store32(9213820, 0)
    func45()
    v11 = (v2 + (arg0 * 286704))
    while True:  # block $label15
        while True:  # block $label12
            while True:  # $label14
                while True:  # block $label0
                    v12 = load32(((v7 << 2) + 9940))
                    v8 = load32(((v11 + (load32(((v7 << 2) + 9940)) << 2)) + 284636))
                    if (load32(((v11 + (load32(((v7 << 2) + 9940)) << 2)) + 284636)) == 0):
                        break
                    v9 = 0
                    v10 = load32(v8 + 8)
                    if (load32(v8 + 8) == 0):
                        break
                    while True:  # $label13
                        while True:  # block $label1
                            arg0 = load32((load32(v8) + (v9 << 2)))
                            if (load32((load32(v8) + (v9 << 2))) == 0):
                                break
                            v6 = load32(9671128)
                            v2 = (load32(9671128) + (arg0 * 132))
                            arg0 = load32((load32(9671128) + (arg0 * 132)) + 44)
                            if (((load32((load32(9215884) + (load32((load32(9671128) + (arg0 * 132)) + 44) << 4)) + 4) == 22) | (arg0 == 0)) == 0):
                                break
                            if load8u(v2 + 125):
                                break
                            if load32(v2 + 36):
                                break
                            v3 = load32(v2 + 28)
                            while True:  # block $label4
                                while True:  # block $label2
                                    arg0 = load32(9215928)
                                    if (load32(9215928) == 0):
                                        break
                                    v1 = load32(arg0 + 8)
                                    if (load32(arg0 + 8) == 0):
                                        break
                                    v4 = load32(arg0)
                                    arg0 = 0
                                    while True:  # $label3
                                        if (v3 != load32((v6 + (load32((v4 + (arg0 << 2))) * 132)) + 28)):
                                            arg0 = (arg0 + 1)
                                            if (v1 != (arg0 + 1)):
                                                continue
                                            break
                                        break
                                    v1 = 1
                                    break
                                    break
                                while True:  # block $label5
                                    arg0 = load32(9215932)
                                    if (load32(9215932) == 0):
                                        break
                                    v1 = load32(arg0 + 8)
                                    if (load32(arg0 + 8) == 0):
                                        break
                                    v4 = load32(arg0)
                                    arg0 = 0
                                    while True:  # $label6
                                        if (v3 == load32((v6 + (load32((v4 + (arg0 << 2))) * 132)) + 28)):
                                            v1 = 1
                                            break
                                        arg0 = (arg0 + 1)
                                        if ((arg0 + 1) != v1):
                                            continue
                                        break
                                    break
                                while True:  # block $label7
                                    arg0 = load32(9215936)
                                    if (load32(9215936) == 0):
                                        break
                                    v1 = load32(arg0 + 8)
                                    if (load32(arg0 + 8) == 0):
                                        break
                                    v4 = load32(arg0)
                                    arg0 = 0
                                    while True:  # $label8
                                        if (v3 == load32((v6 + (load32((v4 + (arg0 << 2))) * 132)) + 28)):
                                            v1 = 1
                                            break
                                        arg0 = (arg0 + 1)
                                        if ((arg0 + 1) != v1):
                                            continue
                                        break
                                    break
                                v1 = 0
                                arg0 = load32(9215940)
                                if (load32(9215940) == 0):
                                    break
                                v4 = load32(arg0 + 8)
                                if (load32(arg0 + 8) == 0):
                                    break
                                v13 = load32(arg0)
                                arg0 = 0
                                while True:  # $label9
                                    v1 = (load32((v6 + (load32((v13 + (arg0 << 2))) * 132)) + 28) == v3)
                                    if (load32((v6 + (load32((v13 + (arg0 << 2))) * 132)) + 28) == v3):
                                        break
                                    arg0 = (arg0 + 1)
                                    if ((arg0 + 1) != v4):
                                        continue
                                    break
                                break
                            if v1:
                                break
                            if (v12 != load8u(v2 + 122)):
                                break
                            if (load8u(v2 + 129) == 10):
                                break
                            while True:  # block $label10
                                if load32(v2 + 92):
                                    break
                                v1 = load32(9213808)
                                if (u(load32(9213808)) > u(9999)):
                                    break
                                arg0 = 1
                                store32(9213808, (v1 + 1))
                                store32(((v1 << 2) + 9173808), v3)
                                while True:  # block $label11
                                    if (load8u(9142906) | load8u(9142916)):
                                        break
                                    arg0 = 0
                                    if load8u(9142917):
                                        break
                                    arg0 = load32(9299880)
                                    if load32(9299880):
                                        arg0 = (arg0 - 1)
                                        store32(9299880, (arg0 - 1))
                                        arg0 = load32((load32(9299872) + (arg0 << 2)))
                                        break
                                    arg0 = load32(9163776)
                                    v3 = (load32(9163776) + 1)
                                    store32(9163776, (load32(9163776) + 1))
                                    v1 = load32(9163784)
                                    if (u(v3) < u(load32(9163784))):
                                        break
                                    store32(v5 + 16, v1)
                                    a_b()
                                    store32(9163784, (load32(9163784) + 40000))
                                    break
                                store32(v2 + 92, arg0)
                                if (load32(v2 + 36) == 0):
                                func203(v2)
                                break
                            if load8u(9163792):
                                break
                            v10 = load32(v8 + 8)
                            break
                        v9 = (v9 + 1)
                        if (u((v9 + 1)) < u(v10)):
                            continue
                        break
                    break
                v7 = (v7 + 1)
                if ((v7 + 1) != 3):
                    continue
                break
            if (load32(9213808) == 0):
                break
            break
            break
        if load8u(9142917):
            break
        arg0 = load32(v2 + 36)
        arg0 = (load32(9671128) + ((load32(v2 + 36) if arg0 else load32(v2 + 28)) * 132))
        v2 = ((load8u((load32(9671128) + ((load32(v2 + 36) if arg0 else load32(v2 + 28)) * 132)) + 122) * 404) + 9568096)
        v3 = load32(((load8u((load32(9671128) + ((load32(v2 + 36) if arg0 else load32(v2 + 28)) * 132)) + 122) * 404) + 9568096) + 220)
        v1 = load16u(arg0 + 114)
        store32(v5, (((load32(v2 + 216) << 4) & 2147483632) + (load16u(arg0 + 112) << 5)))
        store32(v5 + 4, (((v3 << 4) & 2147483632) + (v1 << 5)))
        break
    G.global0 = (v5 + 32)

# ------------------------------------------------------------
# $func335
# ------------------------------------------------------------
def func335(arg0, arg1, arg2, arg3):
    v18 = (arg1 - 30)
    v19 = ((arg1 - 30) + 60)
    v6 = (arg0 - 30)
    v20 = ((arg0 - 30) + 60)
    v8 = load32(9142440)
    v10 = (load32(9142440) + 2)
    v21 = ((load32(9142440) + 2) * load32(((arg2 * 404) + 9568096) + 208))
    v22 = (v8 + 4)
    v23 = load32(9671128)
    v11 = load32(9142840)
    v9 = 2147483647
    v24 = (load32(38500) != arg2)
    while True:  # $label3
        v12 = (v6 + 1)
        if (u(v6) < u(v8)):
            v4 = (arg0 - v6)
            v25 = ((arg0 - v6) * v4)
            v5 = v18
            while True:  # $label2
                while True:  # block $label0
                    if (u(v5) >= u(v8)):
                        break
                    if ((v5 | v6) < 0):
                        break
                    v4 = (arg1 - v5)
                    v13 = (((arg1 - v5) * v4) + v25)
                    if ((((arg1 - v5) * v4) + v25) >= v9):
                        break
                    v7 = load32((v11 + ((v12 + (((v5 + v21) + 1) * v10)) << 2)))
                    if (load32((v11 + ((v12 + (((v5 + v21) + 1) * v10)) << 2))) == 0):
                        break
                    if (arg3 == v7):
                        break
                    v14 = (v23 + (v7 * 132))
                    v15 = (load8u((v23 + (v7 * 132)) + 122) != arg2)
                    v4 = (v9 if (load8u((v23 + (v7 * 132)) + 122) != arg2) else v13)
                    v17 = (v16 if v15 else v7)
                    while True:  # block $label1
                        if v15:
                            break
                        if v24:
                            break
                        v17 = v7
                        v4 = v13
                        if load32((((load16u(v14 + 112) + ((v22 + load16u(v14 + 114)) * v10)) << 2) + v11) + 8):
                            break
                        break
                    v16 = v17
                    v9 = v4
                    break
                v5 = (v5 + 1)
                if ((v5 + 1) < v19):
                    continue
                break
        v6 = v12
        if (v12 < v20):
            continue
        break
    return v16

# ------------------------------------------------------------
# $func336
# ------------------------------------------------------------
def func336(arg0, arg1, arg2):
    v12 = (arg0 + 29)
    v13 = (arg1 + 29)
    v14 = (arg1 - 30)
    v4 = (arg0 - 30)
    v7 = load32(9142440)
    v8 = (load32(9142440) + 2)
    v15 = load32(38564)
    v16 = load32(9671128)
    v17 = load32(9142840)
    v9 = 2147483647
    while True:  # $label3
        v11 = (v4 + 1)
        if (u(v4) < u(v7)):
            v3 = (v4 - arg0)
            v18 = ((v4 - arg0) * v3)
            v3 = v14
            while True:  # $label2
                while True:  # block $label0
                    v5 = v3
                    if (u(v7) <= u(v3)):
                        break
                    if ((v4 | v5) < 0):
                        break
                    v3 = (v5 - arg1)
                    v3 = (((v5 - arg1) * v3) + v18)
                    if ((((v5 - arg1) * v3) + v18) >= v9):
                        break
                    v6 = (v16 + (load32((v17 + ((v11 + (((v5 + v8) + 1) * v8)) << 2))) * 132))
                    if (u(load32((v16 + (load32((v17 + ((v11 + (((v5 + v8) + 1) * v8)) << 2))) * 132)) + 64)) >= u(load32(v6 + 68))):
                        break
                    if (load16u(v6 + 110) != arg2):
                        break
                    v19 = load8u(v6 + 122)
                    v20 = ((load8u(v6 + 122) * 404) + 9568096)
                    if (load32(((load8u(v6 + 122) * 404) + 9568096) + 264) != 1):
                        break
                    if (load32(v20 + 188) != 55):
                        break
                    while True:  # block $label1
                        if (v15 != v19):
                            break
                        # br_table[(load8u(v6 + 125) - 4)]
                        break
                        break
                    v10 = load32(v6 + 28)
                    v9 = v3
                    break
                v3 = (v5 + 1)
                if (v5 < v13):
                    continue
                break
        v3 = (v4 < v12)
        v4 = v11
        if v3:
            continue
        break
    return v10

# ------------------------------------------------------------
# $func337
# ------------------------------------------------------------
def func337(arg0, arg1, arg2, arg3, arg4, arg5):
    v17 = load16u(arg2 + 114)
    v15 = (load16u(arg2 + 114) - 1)
    v18 = load16u(arg2 + 112)
    v16 = (load16u(arg2 + 112) - 1)
    v19 = load8u(arg2 + 122)
    v7 = ((load8u(arg2 + 122) * 404) + 9568096)
    v14 = load32(((load8u(arg2 + 122) * 404) + 9568096) + 60)
    if load32(((load8u(arg2 + 122) * 404) + 9568096) + 60):
        v8 = load32(v7 + 56)
        v10 = load32(9142440)
        v6 = 2147483647
        v7 = 0
        while True:  # $label0
            v9 = (v7 << 2)
            v11 = (load32((v8 + ((v7 << 2) | 4))) + v15)
            v13 = ((load32((v8 + ((v7 << 2) | 4))) + v15) - arg5)
            v9 = (load32((v8 + v9)) + v16)
            v13 = ((load32((v8 + v9)) + v16) - arg4)
            v13 = ((((load32((v8 + ((v7 << 2) | 4))) + v15) - arg5) * v13) + (((load32((v8 + v9)) + v16) - arg4) * v13))
            if (v6 > ((((load32((v8 + ((v7 << 2) | 4))) + v15) - arg5) * v13) + (((load32((v8 + v9)) + v16) - arg4) * v13))):
                v11 = (((u(v9) < u(v10)) & ((v9 | v11) >= 0)) & (u(v10) > u(v11)))
                v6 = (v13 if (((u(v9) < u(v10)) & ((v9 | v11) >= 0)) & (u(v10) > u(v11))) else v6)
                v12 = (((v7 & 0xFFFFFFFF) >> 1) if v11 else v12)
            v7 = (v7 + 2)
            if (u((v7 + 2)) < u(v14)):
                continue
            break
    arg4 = load16u(40596)
    arg5 = (load16u(40596) + 2)
    store16(40596, (load16u(40596) + 2))
    while True:  # block $label1
        if (u((arg5 & 65535)) < u(65534)):
            break
        store16(40596, 1)
        arg5 = load32(9142440)
        arg5 = (load32(9142440) * arg5)
        if ((load32(9142440) * arg5) == 0):
            break
        # TODO: memory.fill []
        break
    while True:  # block $label5
        if v14:
            v10 = ((v14 & 0xFFFFFFFF) >> 1)
            v11 = ((v19 * 404) + 9568152)
            v7 = 0
            while True:  # $label6
                while True:  # block $label3
                    while True:  # block $label2
                        if (v7 == 0):
                            break
                        if (v7 & 2):
                            break
                        break
                    arg5 = (load32(v11) + (((((((v7 & 0xFFFFFFFF) >> 2) + v12) % v10) + v10) % v10) << 3))
                    v8 = load32((load32(v11) + (((((((v7 & 0xFFFFFFFF) >> 2) + v12) % v10) + v10) % v10) << 3)))
                    v9 = load32(arg5 + 4)
                    arg5 = load32(9142440)
                    v6 = (load32(9142440) + 2)
                    v6 = load32((load32(9142840) + (((load32((load32(v11) + (((((((v7 & 0xFFFFFFFF) >> 2) + v12) % v10) + v10) % v10) << 3))) + v18) + (((load32(arg5 + 4) + v17) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v6)) << 2)))
                    if (u(load32((load32(9142840) + (((load32((load32(v11) + (((((((v7 & 0xFFFFFFFF) >> 2) + v12) % v10) + v10) % v10) << 3))) + v18) + (((load32(arg5 + 4) + v17) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v6)) << 2)))) <= u(2)):
                        if (load32(arg3 + 212) != v6):
                            break
                    if (u(v6) >= u(3)):
                        if func205((load32(9671128) + (v6 * 132)), load16u(arg2 + 110)):
                            break
                        arg5 = load32(9142440)
                    while True:  # block $label4
                        v6 = (v9 + v15)
                        v8 = (v8 + v16)
                        v9 = (((v9 + v15) | (v8 + v16)) < 0)
                        if (((v9 + v15) | (v8 + v16)) < 0):
                            break
                        if (u(arg5) <= u(v8)):
                            break
                        if (u(arg5) <= u(v6)):
                            break
                        if func56(v8, v6, arg3, load16u(arg2 + 110), 0, 0, 1, 1, 0):
                            break
                        arg5 = load32(9142440)
                        break
                    if v9:
                        break
                    if (u(arg5) <= u(v8)):
                        break
                    if (u(arg5) <= u(v6)):
                        break
                    if (func347(arg0, arg1, v8, v6, v8, v6, arg2, arg3, arg4) == 0):
                        break
                    return 1
                    break
                v7 = (v7 + 2)
                if (u((v7 + 2)) < u(v14)):
                    continue
                break
        return 0
        break
    store32(arg0, v8)
    store32(arg1, v6)
    return 1

# ------------------------------------------------------------
# $func338
# ------------------------------------------------------------
def func338(arg0, arg1, arg2, arg3):
    v8 = load8u(arg2 + 122)
    v10 = ((load8u(arg2 + 122) * 404) + 9568096)
    v9 = load32(((load8u(arg2 + 122) * 404) + 9568096) + 60)
    v11 = load16u(arg2 + 112)
    v12 = load16u(arg2 + 114)
    v6 = load32(9147324)
    store32(9147324, load32(9147320))
    v7 = load32(9147316)
    v4 = load32(9147312)
    store32(9147316, load32(9147312))
    store32(9147320, v7)
    v6 = (v6 ^ (v6 << 11))
    v6 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6)
    store32(9147312, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v6 ^ (v6 << 11)) & 0xFFFFFFFF) >> 8))) ^ v6))
    v13 = ((v6 % ((v9 & 0xFFFFFFFF) >> 1)) << 1)
    v14 = (v12 - 1)
    v15 = (v11 - 1)
    while True:  # block $label1
        if v9:
            v6 = load32(9142440)
            v4 = 0
            while True:  # $label2
                while True:  # block $label0
                    v5 = (load32(v10 + 56) + (((v4 + v13) % v9) << 2))
                    v7 = (load32((load32(v10 + 56) + (((v4 + v13) % v9) << 2)) + 4) + v14)
                    if (u(v6) <= u((load32((load32(v10 + 56) + (((v4 + v13) % v9) << 2)) + 4) + v14))):
                        break
                    v5 = (load32(v5) + v15)
                    if (u(v6) <= u((load32(v5) + v15))):
                        break
                    if ((v5 | v7) < 0):
                        break
                    if func56(v5, v7, arg3, load16u(arg2 + 110), 0, 0, 1, 1, 0):
                        break
                    v6 = load32(9142440)
                    break
                v4 = (v4 + 2)
                if (u((v4 + 2)) < u(v9)):
                    continue
                break
        v6 = load16u(40596)
        v4 = (load16u(40596) + 2)
        store16(40596, (load16u(40596) + 2))
        while True:  # block $label3
            if (u((v4 & 65535)) < u(65534)):
                break
            store16(40596, 1)
            v4 = load32(9142440)
            v4 = (load32(9142440) * v4)
            if ((load32(9142440) * v4) == 0):
                break
            # TODO: memory.fill []
            break
        if v9:
            v10 = ((v8 * 404) + 9568152)
            v4 = 0
            while True:  # $label5
                while True:  # block $label4
                    v7 = (load32(v10) + (((v4 + v13) % v9) << 2))
                    v8 = load32((load32(v10) + (((v4 + v13) % v9) << 2)))
                    v16 = load32(v7 + 4)
                    v7 = load32(9142440)
                    v5 = (load32(9142440) + 2)
                    v5 = load32((load32(9142840) + (((load32((load32(v10) + (((v4 + v13) % v9) << 2))) + v11) + (((load32(v7 + 4) + v12) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v5)) << 2)))
                    if (u(load32((load32(9142840) + (((load32((load32(v10) + (((v4 + v13) % v9) << 2))) + v11) + (((load32(v7 + 4) + v12) + ((load32(9142440) + 2) * load32(arg3 + 208))) * v5)) << 2)))) <= u(2)):
                        if (load32(arg3 + 212) != v5):
                            break
                    if (u(v5) >= u(3)):
                        if func205((load32(9671128) + (v5 * 132)), load16u(arg2 + 110)):
                            break
                        v7 = load32(9142440)
                    v5 = (v14 + v16)
                    if (u(v7) <= u((v14 + v16))):
                        break
                    v8 = (v8 + v15)
                    if ((v5 | (v8 + v15)) < 0):
                        break
                    if (u(v7) <= u(v8)):
                        break
                    if (func347(arg0, arg1, v8, v5, v8, v5, arg2, arg3, v6) == 0):
                        break
                    return 1
                    break
                v4 = (v4 + 2)
                if (u((v4 + 2)) < u(v9)):
                    continue
                break
        return 0
        break
    store32(arg0, v5)
    store32(arg1, v7)
    return 1