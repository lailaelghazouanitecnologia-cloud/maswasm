"""
Tzar Game Engine - Exports functions.
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
# $Te
# Export: Te
# ------------------------------------------------------------
def Te(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    """Exported as Te."""
    v11 = (G.global0 - 400)
    G.global0 = (G.global0 - 400)
    store8(9687269, arg5)
    store32(9687272, arg0)
    store32(v11 + 396, arg0)
    arg0 = (-1 if (u(arg0) > u(-5)) else ((arg0 & -4) + 4))
    v10 = func26((-1 if (u(arg0) > u(-5)) else ((arg0 & -4) + 4)))
    # TODO: memory.fill []
    v15 = load32(v10)
    store32(9684508, load32(v10))
    while True:  # block $label2
        while True:  # block $label3
            while True:  # block $label1
                if load8u(9147152):
                    while True:  # block $label0
                        if (u(v15) >= u(467)):
                            arg0 = load32(v10 + 72)
                            store32(9561760, load32(v10 + 72))
                            break
                        arg0 = load32(9561760)
                        break
                    if (arg0 == 0):
                        break
                    if (arg3 == 0):
                        if (arg0 == load32(9561756)):
                            break
                    store32(9561764, 0)
                    break
                store32(9561760, 0)
                break
                break
            store32(9561760, 0)
            func182()
            store8(59182, 1)
            store8(9681940, 1)
            store32(v11 + 64, load32(v10 + 48))
            break
        arg0 = load32(v10 + 36)
        if ((u(load32(v10 + 36)) <= u(arg2)) & (u(arg2) >= u(2))):
            break
        arg1 = load32(9687204)
        if load32(9687204):
            store32(9687204, 0)
        store32(9142892, arg0)
        arg1 = load32(v10 + 68)
        store32(9142872, ((1 if (u(arg0) <= u(arg1)) else load32(v10 + 68)) if arg1 else 1))
        v56 = (i64(arg0) * 286704)
        arg1 = (-1 if i32(((v56 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(arg0) * 286704)))
        arg3 = func26((-1 if i32(((v56 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(arg0) * 286704))))
        # TODO: memory.fill []
        store32(9561692, arg3)
        arg1 = load32(v10 + 48)
        store32(9142440, load32(v10 + 48))
        v21 = (v10 + 4)
        while True:  # block $label6
            while True:  # block $label7
                while True:  # block $label5
                    while True:  # block $label4
                        if (u(v15) >= u(491)):
                            v13 = load32(v10 + 76)
                            v20 = load32(v10 + 60)
                            v35 = load32(v10 + 56)
                            arg6 = load32(v10 + 24)
                            if (u(v15) <= u(551)):
                                arg3 = (arg0 - 1)
                                v8 = ((((arg1 * arg1) & 0xFFFFFFFF) >> 2) + 1)
                                v12 = (arg0 * arg0)
                                v23 = arg6
                                break
                            v23 = 1
                            v8 = ((((arg1 * arg1) & 0xFFFFFFFF) >> 2) + 1)
                            v12 = (arg0 * arg0)
                            v29 = load32(v10 + 144)
                            if (u(v15) < u(565)):
                                break
                            v33 = load32(v10 + 152)
                            break
                        arg3 = (arg0 - 1)
                        v8 = ((((arg1 * arg1) & 0xFFFFFFFF) >> 2) + 1)
                        v12 = (arg0 * arg0)
                        v13 = load32(v10 + 76)
                        v20 = load32(v10 + 60)
                        v35 = load32(v10 + 56)
                        arg6 = 0
                        if (u(v15) < u(473)):
                            break
                        break
                    arg6 = v23
                    v23 = 0
                    break
                    break
                arg3 = arg0
                break
            v33 = ((3019 if (u(v15) > u(555)) else 3011) * arg3)
            break
        v36 = 0
        v9 = load32(v10 + 12)
        v24 = load32(v10 + 16)
        v19 = load32(v10 + 20)
        v14 = load32(v21)
        v22 = load32(v10 + 40)
        v18 = load32(v10 + 84)
        store8(9147212, 1)
        while True:  # block $label8
            if (u(v15) < u(460)):
                break
            store8(9147208, (load32(v10 + 8) != 0))
            store8(9147209, (load32(v10 + 124) != 0))
            if (u(v15) < u(467)):
                break
            break
        store32(9561752, load32(v10 + 72))
        v30 = load32(v10 + 148)
        store32(9561764, 0)
        store32(9142952, load32(v10 + 28))
        store32(9142956, load32(v10 + 32))
        store32(9147220, load32(v10 + 44))
        arg0 = 0
        if (arg5 == 0):
            arg0 = load32(v10 + 52)
        store32(59148, arg0)
        store32(9142848, arg0)
        store32(59176, arg0)
        arg0 = load32(v10 + 64)
        store32(9671136, load32(v10 + 64))
        if (u(load32(9671132)) < u(arg0)):
            arg0 = (arg0 + 10000)
            store32(9671132, (arg0 + 10000))
            arg4 = load32(9671128)
            v56 = (i64(arg0) * 132)
            arg1 = i32((i64(arg0) * 132))
            arg3 = (i32((i64(arg0) * 132)) + 4)
            arg1 = func26((-1 if i32(((v56 & 0xFFFFFFFFFFFFFFFF) >> 32)) else (-1 if (u(arg1) > u(arg3)) else (i32((i64(arg0) * 132)) + 4))))
            store32(func26((-1 if i32(((v56 & 0xFFFFFFFFFFFFFFFF) >> 32)) else (-1 if (u(arg1) > u(arg3)) else (i32((i64(arg0) * 132)) + 4)))), arg0)
            arg3 = (arg1 + 4)
            if arg0:
                v7 = (arg3 + (arg0 * 132))
                arg0 = arg3
                while True:  # $label9
                    # TODO: memory.fill []
                    arg1 = func26(4)
                    store32(arg0 + 4, func26(4))
                    store32(arg0, arg1)
                    store32(arg0 + 8, (arg1 + 4))
                    arg0 = (arg0 + 132)
                    if ((arg0 + 132) != v7):
                        continue
                    break
            if arg4:
                v16 = (arg4 - 4)
                arg0 = load32((arg4 - 4))
                if load32((arg4 - 4)):
                    arg1 = (arg4 + (arg0 * 132))
                    while True:  # $label10
                        arg0 = (arg1 - 132)
                        v7 = load32((arg1 - 132))
                        if load32((arg1 - 132)):
                            store32((arg1 - 128), v7)
                        arg1 = arg0
                        if (arg0 != arg4):
                            continue
                        break
            store32(9671128, arg3)
        store32(9684364, load32(v10 + 88))
        store32(9684368, load32(v10 + 92))
        store32(9684372, load32(v10 + 96))
        store32(9684340, load32(v10 + 100))
        store32(9684344, load32(v10 + 104))
        store32(9684348, load32(v10 + 108))
        store32(9684352, load32(v10 + 112))
        store32(9684356, load32(v10 + 116))
        store32(9684360, load32(v10 + 120))
        if v23:
            store32(9147312, load32(v10 + 128))
            store32(9147316, load32(v10 + 132))
            store32(9147320, load32(v10 + 136))
            store32(9147324, load32(v10 + 140))
        v16 = ((v9 + v24) + v19)
        v17 = (32 if (u(v15) < u(552)) else 64)
        v19 = ((32 if (u(v15) < u(552)) else 64) + v14)
        v27 = (((v9 + v24) + v19) + ((32 if (u(v15) < u(552)) else 64) + v14))
        arg3 = ((((v9 + v24) + v19) + ((32 if (u(v15) < u(552)) else 64) + v14)) + v13)
        while True:  # block $label11
            arg0 = load32(v10 + 84)
            if load32(v10 + 84):
                arg1 = load32(9142424)
                if load32(9142424):
                    store32(9142424, 0)
                arg4 = (arg0 << 2)
                arg1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                store32(9142428, arg0)
                store32(9142424, arg1)
                # TODO: memory.copy []
                store32(v11 + 52, arg0)
                store32(v11 + 48, arg1)
                break
            arg0 = load32(9142424)
            if load32(9142424):
                store32(9142424, 0)
            arg0 = func26(188)
            store32(9142428, 47)
            store32(9142424, arg0)
            # TODO: memory.copy []
            break
        arg0 = load32(9142424)
        if load8u(9142917):
            store32(9142832, load32(arg0 + 48))
            store32(arg0 + 48, 0)
        arg4 = load32(arg0 + 16)
        store8(9216060, (load32(arg0 + 16) == 991915600))
        arg1 = load32(9142440)
        v7 = load32(9147132)
        store32(9147136, ((load32(9142440) == 4096) & (load32(9147132) != 0)))
        if (arg1 == 4096):
            store32(51784, 4)
            store32(51780, 3)
        if (arg4 == 991915600):
            store32(((load32(38460) * 404) + 9568096) + 244, 0)
            store32(((load32(38672) * 404) + 9568096) + 244, 0)
            store32(((load32(38732) * 404) + 9568096) + 244, 0)
        if v7:
            store32(9142872, 0)
        v18 = (arg3 + v18)
        while True:  # block $label12
            if (load32(arg0 + 32) == 0):
                break
            if load32(9684368):
                break
            store32(9684368, (load32(arg0 + 56) * 1000))
            break
        while True:  # block $label13
            if (u(v15) >= u(556)):
                v24 = 0
                if v30:
                    break
                if (load32(9142848) == 0):
                    break
            v24 = 0
            if (u((load32(arg0 + 48) - 1)) > u(1)):
                break
            v24 = ((((arg1 * arg1) & 0xFFFFFFFF) >> 5) + 1)
            break
        arg0 = 0
        arg1 = (arg1 * arg1)
        store32(9147288, func26((arg1 * arg1)))
        if arg1:
            arg1 = (v10 + (v18 << 2))
            while True:  # $label14
                store8((load32(9147288) + arg0), load8u((arg0 + arg1)))
                arg0 = (arg0 + 1)
                arg3 = load32(9142440)
                if (u((arg0 + 1)) < u((load32(9142440) * arg3))):
                    continue
                break
        if v14:
            arg0 = load32(9681936)
            if (load32(9681936) == 0):
                arg0 = func26(16)
                arg1 = (v14 << 2)
                # TODO: i32.div_u []
                arg3 = 3
                store32((v14 << 2) + 4, 3)
                store32(arg0, func26((-1 if (u(arg1) > u(-1073741825)) else (arg3 << 2))))
                store64(arg0 + 8, 206158430208)
                store32(9681936, arg0)
            arg4 = 0
            while True:  # $label19
                v9 = (v10 + ((arg4 + v17) << 2))
                v25 = load32((v10 + ((arg4 + v17) << 2)))
                while True:  # block $label15
                    arg3 = load32(arg0 + 8)
                    if (load32(arg0 + 8) != load32(arg0 + 4)):
                        v7 = load32(arg0)
                        break
                    v7 = (load32(arg0 + 12) + arg3)
                    store32(arg0 + 4, (load32(arg0 + 12) + arg3))
                    arg1 = load32(arg0)
                    v7 = func26((-1 if (u(v7) > u(1073741823)) else (v7 << 2)))
                    if arg3:
                        # TODO: memory.copy []
                    if arg1:
                        arg3 = load32(arg0 + 8)
                    store32(arg0, v7)
                    break
                arg1 = load32(9681936)
                store32(arg0 + 8, (arg3 + 1))
                store32((v7 + (arg3 << 2)), v25)
                v25 = load32(v9 + 4)
                while True:  # block $label16
                    arg3 = load32(arg1 + 8)
                    if (load32(arg1 + 8) != load32(arg1 + 4)):
                        v7 = load32(arg1)
                        break
                    v7 = (load32(arg1 + 12) + arg3)
                    store32(arg1 + 4, (load32(arg1 + 12) + arg3))
                    arg0 = load32(arg1)
                    v7 = func26((-1 if (u(v7) > u(1073741823)) else (v7 << 2)))
                    if arg3:
                        # TODO: memory.copy []
                    if arg0:
                        arg3 = load32(arg1 + 8)
                    store32(arg1, v7)
                    break
                arg0 = load32(9681936)
                store32(arg1 + 8, (arg3 + 1))
                store32((v7 + (arg3 << 2)), v25)
                v7 = load32(v9 + 8)
                while True:  # block $label17
                    arg3 = load32(arg0 + 8)
                    if (load32(arg0 + 8) != load32(arg0 + 4)):
                        v9 = load32(arg0)
                        break
                    v9 = (load32(arg0 + 12) + arg3)
                    store32(arg0 + 4, (load32(arg0 + 12) + arg3))
                    arg1 = load32(arg0)
                    v9 = func26((-1 if (u(v9) > u(1073741823)) else (v9 << 2)))
                    if arg3:
                        # TODO: memory.copy []
                    if arg1:
                        arg3 = load32(arg0 + 8)
                    store32(arg0, v9)
                    break
                arg1 = load32(9681936)
                store32(arg0 + 8, (arg3 + 1))
                store32((v9 + (arg3 << 2)), v7)
                while True:  # block $label18
                    arg3 = load32(arg1 + 8)
                    if (load32(arg1 + 8) != load32(arg1 + 4)):
                        v9 = load32(arg1)
                        break
                    v9 = (load32(arg1 + 12) + arg3)
                    store32(arg1 + 4, (load32(arg1 + 12) + arg3))
                    arg0 = load32(arg1)
                    v9 = func26((-1 if (u(v9) > u(1073741823)) else (v9 << 2)))
                    if arg3:
                        # TODO: memory.copy []
                    if arg0:
                        arg3 = load32(arg1 + 8)
                    store32(arg1, v9)
                    break
                arg0 = load32(9681936)
                store32(arg1 + 8, (arg3 + 1))
                store32((v9 + (arg3 << 2)), 0)
                arg4 = (arg4 + 3)
                if (u((arg4 + 3)) < u(v14)):
                    continue
                break
        v25 = (v8 + v18)
        v31 = ((v8 + v18) + v12)
        v32 = (((v8 + v18) + v12) + (v12 if (u(v15) > u(466)) else 0))
        v34 = ((((v8 + v18) + v12) + (v12 if (u(v15) > u(466)) else 0)) + v12)
        v9 = (((((v8 + v18) + v12) + (v12 if (u(v15) > u(466)) else 0)) + v12) + v12)
        v14 = ((((((v8 + v18) + v12) + (v12 if (u(v15) > u(466)) else 0)) + v12) + v12) + v22)
        store32(9142912, arg6)
        while True:  # block $label20
            if arg6:
                arg0 = load32(9142908)
                if load32(9142908):
                    store32(9142908, 0)
                arg0 = (arg6 << 2)
                arg1 = func26((-1 if (u(arg6) > u(1073741823)) else (arg6 << 2)))
                store32(9142908, func26((-1 if (u(arg6) > u(1073741823)) else (arg6 << 2))))
                # TODO: memory.copy []
                if (load8u(9687268) == 0):
                    break
                break
            if (load8u(9687268) == 0):
                break
            arg0 = load32(9142908)
            if load32(9142908):
                store32(9142908, 0)
            store32(9142912, 0)
            func272()
            func271()
            func220()
            func218()
            break
        while True:  # block $label21
            if (u(v15) < u(460)):
                break
            if (v16 == 0):
                break
            v18 = load32(v10 + 16)
            arg0 = load32(9684448)
            arg3 = load32(9684452)
            arg1 = load32(v10 + 12)
            if (u(load32(9684448)) <= u((load32(9684452) + load32(v10 + 12)))):
                arg4 = (load32(9684456) + (arg0 + arg1))
                store32(9684448, (load32(9684456) + (arg0 + arg1)))
                arg0 = load32(9684444)
                arg4 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                if arg3:
                    # TODO: memory.copy []
                if arg0:
                store32(9684444, arg4)
            while True:  # block $label22
                if (arg1 == 0):
                    break
                arg3 = (v10 + (v19 << 2))
                arg0 = 0
                v8 = load32(9684444)
                if (arg1 != 1):
                    v16 = (arg1 & -2)
                    arg4 = 0
                    while True:  # $label23
                        v7 = (arg0 << 2)
                        v17 = load32((arg3 + (arg0 << 2)))
                        v26 = load32(9684452)
                        store32(9684452, (load32(9684452) + 1))
                        store32((v8 + (v26 << 2)), v17)
                        v17 = load32((arg3 + (v7 | 4)))
                        v7 = load32(9684452)
                        store32(9684452, (load32(9684452) + 1))
                        store32((v8 + (v7 << 2)), v17)
                        arg0 = (arg0 + 2)
                        arg4 = (arg4 + 2)
                        if ((arg4 + 2) != v16):
                            continue
                        break
                if ((arg1 & 1) == 0):
                    break
                arg0 = load32((arg3 + (arg0 << 2)))
                arg3 = load32(9684452)
                store32(9684452, (load32(9684452) + 1))
                store32((v8 + (arg3 << 2)), arg0)
                break
            arg0 = load32(9684464)
            arg4 = load32(9684468)
            arg3 = load32(v10 + 16)
            if (u(load32(9684464)) <= u((load32(9684468) + load32(v10 + 16)))):
                v8 = (load32(9684472) + (arg0 + arg3))
                store32(9684464, (load32(9684472) + (arg0 + arg3)))
                arg0 = load32(9684460)
                v8 = func26((-1 if (u(v8) > u(1073741823)) else (v8 << 2)))
                if arg4:
                    # TODO: memory.copy []
                if arg0:
                store32(9684460, v8)
            v19 = (arg1 + v19)
            while True:  # block $label24
                if (arg3 == 0):
                    break
                arg1 = (v10 + (v19 << 2))
                arg0 = 0
                v8 = load32(9684460)
                if (arg3 != 1):
                    v16 = (arg3 & -2)
                    arg4 = 0
                    while True:  # $label25
                        v7 = (arg0 << 2)
                        v17 = load32((arg1 + (arg0 << 2)))
                        v26 = load32(9684468)
                        store32(9684468, (load32(9684468) + 1))
                        store32((v8 + (v26 << 2)), v17)
                        v17 = load32((arg1 + (v7 | 4)))
                        v7 = load32(9684468)
                        store32(9684468, (load32(9684468) + 1))
                        store32((v8 + (v7 << 2)), v17)
                        arg0 = (arg0 + 2)
                        arg4 = (arg4 + 2)
                        if ((arg4 + 2) != v16):
                            continue
                        break
                if ((arg3 & 1) == 0):
                    break
                arg0 = load32((arg1 + (arg0 << 2)))
                arg1 = load32(9684468)
                store32(9684468, (load32(9684468) + 1))
                store32((v8 + (arg1 << 2)), arg0)
                break
            arg0 = load32(9684480)
            arg3 = load32(9684484)
            arg1 = load32(v10 + 20)
            if (u(load32(9684480)) <= u((load32(9684484) + load32(v10 + 20)))):
                arg4 = (load32(9684488) + (arg0 + arg1))
                store32(9684480, (load32(9684488) + (arg0 + arg1)))
                arg0 = load32(9684476)
                arg4 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                if arg3:
                    # TODO: memory.copy []
                if arg0:
                store32(9684476, arg4)
            if (arg1 == 0):
                break
            arg3 = (v10 + ((v18 + v19) << 2))
            arg0 = 0
            v8 = load32(9684476)
            if (arg1 != 1):
                v19 = (arg1 & -2)
                arg4 = 0
                while True:  # $label26
                    v7 = (arg0 << 2)
                    v18 = load32((arg3 + (arg0 << 2)))
                    v16 = load32(9684484)
                    store32(9684484, (load32(9684484) + 1))
                    store32((v8 + (v16 << 2)), v18)
                    v18 = load32((arg3 + (v7 | 4)))
                    v7 = load32(9684484)
                    store32(9684484, (load32(9684484) + 1))
                    store32((v8 + (v7 << 2)), v18)
                    arg0 = (arg0 + 2)
                    arg4 = (arg4 + 2)
                    if ((arg4 + 2) != v19):
                        continue
                    break
            if ((arg1 & 1) == 0):
                break
            arg0 = load32((arg3 + (arg0 << 2)))
            arg1 = load32(9684484)
            store32(9684484, (load32(9684484) + 1))
            store32((v8 + (arg1 << 2)), arg0)
            break
        v19 = (arg6 + v14)
        while True:  # block $label27
            if (v24 == 0):
                break
            arg0 = 0
            store8(9142904, 1)
            arg1 = load32(9142440)
            arg1 = (load32(9142440) * arg1)
            arg3 = ((load32(9142440) * arg1) + 2)
            arg4 = func26((-1 if (arg3 < 0) else (((load32(9142440) * arg1) + 2) << 1)))
            store32(9147376, func26((-1 if (arg3 < 0) else (((load32(9142440) * arg1) + 2) << 1))))
            if (arg1 == 0):
                break
            v7 = (v10 + (v19 << 2))
            if (arg1 != 1):
                arg6 = (arg1 & -2)
                arg3 = 0
                while True:  # $label28
                    v8 = (v7 + (((arg0 & 0xFFFFFFFF) >> 3) & 536870908))
                    store16((arg4 + (arg0 << 1)), (((load32((v7 + (((arg0 & 0xFFFFFFFF) >> 3) & 536870908))) & 0xFFFFFFFF) >> (arg0 & 30)) & 1))
                    v14 = (arg0 | 1)
                    store16((arg4 + ((arg0 | 1) << 1)), (((load32(v8) & 0xFFFFFFFF) >> v14) & 1))
                    arg0 = (arg0 + 2)
                    arg3 = (arg3 + 2)
                    if ((arg3 + 2) != arg6):
                        continue
                    break
            if ((arg1 & 1) == 0):
                break
            store16((arg4 + (arg0 << 1)), (((load32((v7 + (((arg0 & 0xFFFFFFFF) >> 3) & 536870908))) & 0xFFFFFFFF) >> arg0) & 1))
            break
        while True:  # block $label71
            while True:  # block $label90
                while True:  # block $label44
                    while True:  # block $label42
                        if v13:
                            arg3 = (v10 + (v27 << 2))
                            arg6 = (v11 + 288)
                            v27 = (u(v15) > u(563))
                            arg0 = 0
                            while True:  # $label47
                                store64(v11 + 280, 0)
                                store64(v11 + 272, 0)
                                store64(v11 + 264, 0)
                                store32(v11 + 388, 0)
                                arg1 = (arg3 + (arg0 << 2))
                                v18 = load32((arg3 + (arg0 << 2)))
                                v16 = load32(arg1 + 4)
                                arg1 = load32(arg1 + 8)
                                store32(v11 + 368, load32(arg1 + 8))
                                arg0 = (arg0 + 3)
                                while True:  # block $label29
                                    if (arg1 == 0):
                                        break
                                    v17 = (arg1 & 3)
                                    v8 = 0
                                    while True:  # block $label30
                                        if (u(arg1) < u(4)):
                                            arg1 = 0
                                            break
                                        v26 = (arg1 & -4)
                                        arg1 = 0
                                        v14 = 0
                                        while True:  # $label31
                                            arg4 = (arg1 << 1)
                                            v7 = (arg3 + (arg0 << 2))
                                            store16((arg6 + (arg1 << 1)), load32((arg3 + (arg0 << 2))))
                                            store16((arg6 + (arg4 | 2)), load32(v7 + 4))
                                            store16((arg6 + (arg4 | 4)), load32(v7 + 8))
                                            store16((arg6 + (arg4 | 6)), load32(v7 + 12))
                                            arg1 = (arg1 + 4)
                                            arg0 = (arg0 + 4)
                                            v14 = (v14 + 4)
                                            if ((v14 + 4) != v26):
                                                continue
                                            break
                                        break
                                    if (v17 == 0):
                                        break
                                    while True:  # $label32
                                        store16(((arg1 << 1) + v11) + 288, load32((arg3 + (arg0 << 2))))
                                        arg1 = (arg1 + 1)
                                        arg0 = (arg0 + 1)
                                        v8 = (v8 + 1)
                                        if ((v8 + 1) != v17):
                                            continue
                                        break
                                    break
                                arg1 = (arg3 + (arg0 << 2))
                                store32(v11 + 372, load32((arg3 + (arg0 << 2))))
                                store32(v11 + 376, load32(arg1 + 4))
                                arg4 = load32(arg1 + 8)
                                v7 = (arg0 + 4)
                                store32(v11 + 392, (arg0 + 4))
                                store32(v11 + 380, arg4)
                                store32(v11 + 384, load32(arg1 + 12))
                                if v27:
                                    store32(v11 + 392, (arg0 + 5))
                                    store32(v11 + 388, load32((arg3 + (v7 << 2))))
                                arg4 = 0
                                while True:  # block $label38
                                    while True:  # block $label40
                                        while True:  # block $label36
                                            while True:  # block $label33
                                                if (v18 == 0):
                                                    break
                                                while True:  # $label37
                                                    while True:  # block $label35
                                                        func381((v11 + 68), arg3, (v11 + 392), 1, v15)
                                                        while True:  # block $label34
                                                            arg0 = load32(v11 + 268)
                                                            v8 = load32(v11 + 272)
                                                            if (u(load32(v11 + 268)) < u(load32(v11 + 272))):
                                                                # TODO: memory.copy []
                                                                store32(v11 + 268, (arg0 + 196))
                                                                break
                                                            arg0 = load32(v11 + 264)
                                                            v7 = (arg0 - load32(v11 + 264))
                                                            v14 = ((arg0 - load32(v11 + 264)) // 196)
                                                            arg1 = (((arg0 - load32(v11 + 264)) // 196) + 1)
                                                            if (u((((arg0 - load32(v11 + 264)) // 196) + 1)) >= u(21913099)):
                                                                break
                                                            v8 = ((v8 - arg0) // 196)
                                                            v17 = (((v8 - arg0) // 196) << 1)
                                                            arg1 = (21913098 if (u(v8) >= u(10956549)) else ((((v8 - arg0) // 196) << 1) if (u(arg1) < u(v17)) else arg1))
                                                            if (21913098 if (u(v8) >= u(10956549)) else ((((v8 - arg0) // 196) << 1) if (u(arg1) < u(v17)) else arg1)):
                                                                if (u(arg1) >= u(21913099)):
                                                                    break
                                                            else:
                                                            v17 = 0
                                                            v8 = (0 + (v14 * 196))
                                                            # TODO: memory.copy []
                                                            v14 = (v8 + ((v7 // -196) * 196))
                                                            # TODO: memory.copy []
                                                            store32(v11 + 272, (v17 + (arg1 * 196)))
                                                            store32(v11 + 268, (v8 + 196))
                                                            store32(v11 + 264, v14)
                                                            if (arg0 == 0):
                                                                break
                                                            break
                                                        arg4 = (arg4 + 1)
                                                        if (v18 != (arg4 + 1)):
                                                            continue
                                                        break
                                                        break
                                                    break
                                                func42()
                                                raise RuntimeError('unreachable')
                                                break
                                            arg4 = 0
                                            if (v16 == 0):
                                                break
                                            while True:  # $label41
                                                func381((v11 + 68), arg3, (v11 + 392), 0, v15)
                                                while True:  # block $label39
                                                    arg0 = load32(v11 + 280)
                                                    v8 = load32(v11 + 284)
                                                    if (u(load32(v11 + 280)) < u(load32(v11 + 284))):
                                                        # TODO: memory.copy []
                                                        store32(v11 + 280, (arg0 + 196))
                                                        break
                                                    arg0 = load32(v11 + 276)
                                                    v7 = (arg0 - load32(v11 + 276))
                                                    v14 = ((arg0 - load32(v11 + 276)) // 196)
                                                    arg1 = (((arg0 - load32(v11 + 276)) // 196) + 1)
                                                    if (u((((arg0 - load32(v11 + 276)) // 196) + 1)) >= u(21913099)):
                                                        break
                                                    v8 = ((v8 - arg0) // 196)
                                                    v18 = (((v8 - arg0) // 196) << 1)
                                                    arg1 = (21913098 if (u(v8) >= u(10956549)) else ((((v8 - arg0) // 196) << 1) if (u(arg1) < u(v18)) else arg1))
                                                    if (21913098 if (u(v8) >= u(10956549)) else ((((v8 - arg0) // 196) << 1) if (u(arg1) < u(v18)) else arg1)):
                                                        if (u(arg1) >= u(21913099)):
                                                            break
                                                    else:
                                                    v18 = 0
                                                    v8 = (0 + (v14 * 196))
                                                    # TODO: memory.copy []
                                                    v14 = (v8 + ((v7 // -196) * 196))
                                                    # TODO: memory.copy []
                                                    store32(v11 + 284, (v18 + (arg1 * 196)))
                                                    store32(v11 + 280, (v8 + 196))
                                                    store32(v11 + 276, v14)
                                                    if (arg0 == 0):
                                                        break
                                                    break
                                                arg4 = (arg4 + 1)
                                                if (v16 != (arg4 + 1)):
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
                                while True:  # block $label46
                                    v7 = load32(9568068)
                                    if (load32(9568068) != load32(9568072)):
                                        store32(v7 + 8, 0)
                                        store64(v7, 0)
                                        arg0 = load32(v11 + 268)
                                        arg4 = load32(v11 + 264)
                                        v8 = (load32(v11 + 268) - load32(v11 + 264))
                                        arg1 = ((load32(v11 + 268) - load32(v11 + 264)) // 196)
                                        if (arg0 != arg4):
                                            if (u(arg1) >= u(21913099)):
                                                break
                                            arg0 = func26(v8)
                                            store32(v7 + 4, func26(v8))
                                            store32(v7, arg0)
                                            store32(v7 + 8, (arg0 + (arg1 * 196)))
                                            arg1 = load32(v11 + 264)
                                            arg4 = load32(v11 + 268)
                                            if (load32(v11 + 264) != load32(v11 + 268)):
                                                while True:  # $label43
                                                    # TODO: memory.copy []
                                                    arg0 = (arg0 + 196)
                                                    arg1 = (arg1 + 196)
                                                    if ((arg1 + 196) != arg4):
                                                        continue
                                                    break
                                            store32(v7 + 4, arg0)
                                        store64(v7 + 12, 0)
                                        store32(v7 + 20, 0)
                                        v8 = load32(v11 + 280)
                                        arg0 = load32(v11 + 276)
                                        arg4 = (load32(v11 + 280) - load32(v11 + 276))
                                        arg1 = ((load32(v11 + 280) - load32(v11 + 276)) // 196)
                                        if (arg0 != v8):
                                            if (u(arg1) >= u(21913099)):
                                                break
                                            arg0 = func26(arg4)
                                            store32(v7 + 16, func26(arg4))
                                            store32(v7 + 12, arg0)
                                            store32(v7 + 20, (arg0 + (arg1 * 196)))
                                            v8 = load32(v11 + 276)
                                            arg1 = load32(v11 + 276)
                                            arg4 = load32(v11 + 280)
                                            if (load32(v11 + 280) != v8):
                                                while True:  # $label45
                                                    # TODO: memory.copy []
                                                    arg0 = (arg0 + 196)
                                                    arg1 = (arg1 + 196)
                                                    if ((arg1 + 196) != arg4):
                                                        continue
                                                    break
                                            store32(v7 + 16, arg0)
                                        # TODO: memory.copy []
                                        store32(9568068, (v7 + 128))
                                        break
                                    v8 = load32(v11 + 276)
                                    break
                                if v8:
                                    store32(v11 + 280, v8)
                                arg0 = load32(v11 + 264)
                                if load32(v11 + 264):
                                    store32(v11 + 268, arg0)
                                arg0 = load32(v11 + 392)
                                if (u(load32(v11 + 392)) < u(v13)):
                                    continue
                                break
                        arg0 = 0
                        arg1 = func26(v12)
                        # TODO: memory.fill []
                        store32(9143004, arg1)
                        arg1 = func26(v12)
                        # TODO: memory.fill []
                        store32(9143012, arg1)
                        arg1 = func26(v12)
                        # TODO: memory.fill []
                        store32(9143008, arg1)
                        arg1 = func26(v12)
                        # TODO: memory.fill []
                        store32(9143016, arg1)
                        if v12:
                            arg1 = (u(v15) < u(467))
                            while True:  # $label48
                                store8((load32(9143004) + arg0), (load32((v10 + ((arg0 + v25) << 2))) != 0))
                                if (arg1 == 0):
                                    store8((load32(9143012) + arg0), (load32((v10 + ((arg0 + v32) << 2))) != 0))
                                store8((load32(9143016) + arg0), load32((v10 + ((arg0 + v34) << 2))))
                                store8((load32(9143008) + arg0), (load32((v10 + ((arg0 + v31) << 2))) != 0))
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v12):
                                    continue
                                break
                        arg4 = load32(9142892)
                        if (u(load32(9142892)) >= u(2)):
                            v12 = (arg4 + 1)
                            arg0 = (arg4 - 1)
                            v7 = ((arg4 - 1) & -4)
                            arg6 = (arg0 & 3)
                            v13 = (u((arg4 - 2)) < u(3))
                            arg1 = 1
                            while True:  # $label53
                                arg3 = 0
                                v8 = (load32(9143012) + (arg1 * v12))
                                arg0 = 1
                                if (v13 == 0):
                                    while True:  # $label51
                                        while True:  # block $label50
                                            while True:  # block $label49
                                                if (arg0 == arg1):
                                                    break
                                                if (arg1 == (arg0 + 1)):
                                                    break
                                                if (arg1 == (arg0 + 2)):
                                                    break
                                                if (arg1 != (arg0 + 3)):
                                                    break
                                                break
                                            store8(v8, 1)
                                            break
                                        arg0 = (arg0 + 4)
                                        arg3 = (arg3 + 4)
                                        if ((arg3 + 4) != v7):
                                            continue
                                        break
                                arg3 = 0
                                if arg6:
                                    while True:  # $label52
                                        if (arg0 == arg1):
                                            store8(v8, 1)
                                        arg0 = (arg0 + 1)
                                        arg3 = (arg3 + 1)
                                        if ((arg3 + 1) != arg6):
                                            continue
                                        break
                                arg1 = (arg1 + 1)
                                if ((arg1 + 1) != arg4):
                                    continue
                                break
                        while True:  # block $label54
                            if (u(v15) > u(466)):
                                break
                            arg0 = 0
                            arg3 = (arg4 * arg4)
                            arg1 = func26((arg4 * arg4))
                            # TODO: memory.fill []
                            store32(9143012, arg1)
                            if (arg3 == 0):
                                break
                            v7 = (arg3 & 3)
                            arg6 = load32(9143004)
                            if (u(arg3) >= u(4)):
                                arg3 = (arg3 & -4)
                                arg4 = 0
                                while True:  # $label55
                                    store8((arg0 + arg1), (load8u((arg0 + arg6)) ^ 1))
                                    v8 = (arg0 | 1)
                                    store8((arg1 + (arg0 | 1)), (load8u((arg6 + v8)) ^ 1))
                                    v8 = (arg0 | 2)
                                    store8((arg1 + (arg0 | 2)), (load8u((arg6 + v8)) ^ 1))
                                    v8 = (arg0 | 3)
                                    store8((arg1 + (arg0 | 3)), (load8u((arg6 + v8)) ^ 1))
                                    arg0 = (arg0 + 4)
                                    arg4 = (arg4 + 4)
                                    if ((arg4 + 4) != arg3):
                                        continue
                                    break
                            if (v7 == 0):
                                break
                            arg4 = 0
                            while True:  # $label56
                                store8((arg0 + arg1), (load8u((arg0 + arg6)) ^ 1))
                                arg0 = (arg0 + 1)
                                arg4 = (arg4 + 1)
                                if ((arg4 + 1) != v7):
                                    continue
                                break
                            break
                        arg1 = (4 if arg5 else v22)
                        store32(9215892, (4 if arg5 else v22))
                        if (u(load32(9215888)) <= u(arg1)):
                            arg0 = (arg1 + 1024)
                            store32(9215888, (arg1 + 1024))
                            arg3 = load32(9215884)
                            arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                            if arg3:
                            store32(9215884, arg0)
                        v14 = (v19 + v24)
                        v33 = ((v19 + v24) + v33)
                        arg6 = 0
                        while True:  # block $label57
                            if (load32(9142848) == 0):
                                store32(9215892, 4)
                                v24 = 1
                                break
                            if (arg1 == 0):
                                v24 = 1
                                break
                            v7 = (arg1 & 3)
                            arg3 = 0
                            arg6 = load32(9215884)
                            arg0 = 0
                            if (u(arg1) >= u(4)):
                                v8 = (arg1 & -4)
                                arg4 = 0
                                while True:  # $label58
                                    store32((arg6 + (arg0 << 2)), load32((v10 + ((arg0 + v9) << 2))))
                                    v12 = (arg0 | 1)
                                    store32((arg6 + ((arg0 | 1) << 2)), load32((v10 + ((v9 + v12) << 2))))
                                    v12 = (arg0 | 2)
                                    store32((arg6 + ((arg0 | 2) << 2)), load32((v10 + ((v9 + v12) << 2))))
                                    v12 = (arg0 | 3)
                                    store32((arg6 + ((arg0 | 3) << 2)), load32((v10 + ((v9 + v12) << 2))))
                                    arg0 = (arg0 + 4)
                                    arg4 = (arg4 + 4)
                                    if ((arg4 + 4) != v8):
                                        continue
                                    break
                            v24 = (arg1 == 0)
                            if v7:
                                while True:  # $label59
                                    store32((arg6 + (arg0 << 2)), load32((v10 + ((arg0 + v9) << 2))))
                                    arg0 = (arg0 + 1)
                                    arg3 = (arg3 + 1)
                                    if ((arg3 + 1) != v7):
                                        continue
                                    break
                            arg6 = arg1
                            break
                        v22 = (v33 + v35)
                        v13 = (253 if (u(v15) < u(552)) else 255)
                        v8 = 0
                        arg1 = load32(9142892)
                        while True:  # block $label60
                            if v29:
                                if (arg1 == 0):
                                    break
                                arg0 = (v20 + v22)
                                while True:  # $label68
                                    v7 = load32(9561692)
                                    if (v30 == 0):
                                        arg3 = (v7 + (v8 * 286704))
                                        arg1 = (arg1 * v13)
                                        arg1 = (-1 if (u(arg1) > u(1073741823)) else ((arg1 * v13) << 2))
                                        store32((v7 + (v8 * 286704)) + 278556, func26((-1 if (u(arg1) > u(1073741823)) else ((arg1 * v13) << 2))))
                                        arg4 = (arg3 + 278560)
                                        store32((arg3 + 278560), func26(arg1))
                                        v9 = (arg3 + 278564)
                                        store32((arg3 + 278564), func26(arg1))
                                        v12 = func26(arg1)
                                        store32((arg3 + 278568), func26(arg1))
                                        v19 = load32(arg3 + 278556)
                                        arg1 = 0
                                        while True:  # $label61
                                            store32((v19 + (arg1 << 2)), load32((v10 + (arg0 << 2))))
                                            arg0 = (arg0 + 1)
                                            arg1 = (arg1 + 1)
                                            v18 = load32(9142892)
                                            if (u((arg1 + 1)) < u((load32(9142892) * 255))):
                                                continue
                                            break
                                        while True:  # block $label62
                                            if (v18 == 0):
                                                break
                                            arg4 = load32(arg4)
                                            arg1 = 0
                                            while True:  # $label63
                                                store32((arg4 + (arg1 << 2)), load32((v10 + (arg0 << 2))))
                                                arg0 = (arg0 + 1)
                                                arg1 = (arg1 + 1)
                                                v19 = load32(9142892)
                                                if (u((arg1 + 1)) < u((load32(9142892) * 255))):
                                                    continue
                                                break
                                            if (v19 == 0):
                                                break
                                            v9 = load32(v9)
                                            arg1 = 0
                                            while True:  # $label64
                                                store32((v9 + (arg1 << 2)), load32((v10 + (arg0 << 2))))
                                                arg0 = (arg0 + 1)
                                                arg1 = (arg1 + 1)
                                                v19 = load32(9142892)
                                                arg4 = (load32(9142892) * 255)
                                                if (u((arg1 + 1)) < u((load32(9142892) * 255))):
                                                    continue
                                                break
                                            if (v19 == 0):
                                                break
                                            arg1 = (1 if (u(arg4) <= u(1)) else arg4)
                                            # TODO: memory.copy []
                                            arg0 = (arg0 + arg1)
                                            break
                                        v12 = (arg0 << 2)
                                        arg1 = load32((v10 + (arg0 << 2)))
                                        arg4 = func26(16)
                                        v9 = (arg1 + 21000)
                                        store32(func26(16) + 4, (arg1 + 21000))
                                        v9 = func26((-1 if (u(v9) > u(1073741823)) else (v9 << 2)))
                                        store32(arg4 + 12, 21000)
                                        store32(arg4, v9)
                                        store32((arg3 + 278572), arg4)
                                        arg0 = (arg0 + 1)
                                        if arg1:
                                            # TODO: memory.copy []
                                            arg0 = (arg0 + arg1)
                                        store32(arg4 + 8, arg1)
                                    arg3 = 0
                                    arg4 = 0
                                    while True:  # $label65
                                        arg1 = (v7 + (v8 * 286704))
                                        v9 = ((v7 + (v8 * 286704)) + (arg4 << 2))
                                        v12 = (v10 + (arg0 << 2))
                                        store32((((v7 + (v8 * 286704)) + (arg4 << 2)) + 278576), load32((v10 + (arg0 << 2))))
                                        store32((v9 + 278580), load32(v12 + 4))
                                        store32((v9 + 278584), load32(v12 + 8))
                                        arg0 = (arg0 + 3)
                                        arg4 = (arg4 + 3)
                                        if ((arg4 + 3) != 255):
                                            continue
                                        break
                                    while True:  # $label66
                                        arg4 = (arg1 + (arg3 << 2))
                                        v7 = (v10 + (arg0 << 2))
                                        store32(((arg1 + (arg3 << 2)) + 279596), load32((v10 + (arg0 << 2))))
                                        store32((arg4 + 279600), load32(v7 + 4))
                                        store32((arg4 + 279604), load32(v7 + 8))
                                        arg0 = (arg0 + 3)
                                        arg3 = (arg3 + 3)
                                        if ((arg3 + 3) != 255):
                                            continue
                                        break
                                    arg4 = 0
                                    while True:  # $label67
                                        v9 = (arg1 + (arg4 << 2))
                                        v7 = arg0
                                        arg3 = (v10 + (arg0 << 2))
                                        store32(((arg1 + (arg4 << 2)) + 280616), load32((v10 + (arg0 << 2))))
                                        store32((v9 + 280620), load32(arg3 + 4))
                                        store32((v9 + 280624), load32(arg3 + 8))
                                        arg0 = (arg0 + 3)
                                        arg4 = (arg4 + 3)
                                        if ((arg4 + 3) != 255):
                                            continue
                                        break
                                    store32((arg1 + 281636), load32((v10 + (arg0 << 2))))
                                    store32((arg1 + 281640), load32(arg3 + 16))
                                    store32((arg1 + 281644), load32(arg3 + 20))
                                    store32((arg1 + 281648), load32(arg3 + 24))
                                    store32((arg1 + 281652), load32(arg3 + 28))
                                    store32((arg1 + 281656), load32(arg3 + 32))
                                    store32((arg1 + 281660), load32(arg3 + 36))
                                    store32((arg1 + 281664), load32(arg3 + 40))
                                    store32((arg1 + 281668), load32(arg3 + 44))
                                    store32((arg1 + 281672), load32(arg3 + 48))
                                    store32((arg1 + 281676), load32(arg3 + 52))
                                    store32((arg1 + 281680), load32(arg3 + 56))
                                    store32((arg1 + 281684), load32(arg3 + 60))
                                    store32((arg1 + 281688), load32((arg3 - -64)))
                                    store32((arg1 + 281692), load32(arg3 + 68))
                                    store32((arg1 + 281696), load32(arg3 + 72))
                                    store32((arg1 + 281700), load32(arg3 + 76))
                                    store32((arg1 + 281704), load32(arg3 + 80))
                                    store32((arg1 + 281708), load32(arg3 + 84))
                                    store32((arg1 + 281712), load32(arg3 + 88))
                                    store32((arg1 + 281716), load32(arg3 + 92))
                                    store32((arg1 + 281720), load32(arg3 + 96))
                                    if (arg5 == 0):
                                        store32((arg1 + 281724), load32(arg3 + 100))
                                        store32((arg1 + 281728), load32(arg3 + 104))
                                        store32((arg1 + 281732), load32(arg3 + 108))
                                        store32((arg1 + 281736), load32(arg3 + 112))
                                    store32((arg1 + 281740), load32(arg3 + 116))
                                    store32((arg1 + 281744), load32(arg3 + 120))
                                    store32((arg1 + 281748), load32(arg3 + 124))
                                    store32((arg1 + 281752), load32(arg3 + 128))
                                    store32((arg1 + 281756), load32(arg3 + 132))
                                    store32((arg1 + 281760), load32(arg3 + 136))
                                    store32((arg1 + 281764), load32(arg3 + 140))
                                    store32((arg1 + 281768), load32(arg3 + 144))
                                    store32((arg1 + 281772), load32(arg3 + 148))
                                    store32((arg1 + 281776), load32(arg3 + 152))
                                    arg0 = load32(arg3 + 156)
                                    store32((arg1 + 281784), v8)
                                    store32((arg1 + 281780), arg0)
                                    arg0 = (v7 + 40)
                                    v8 = (v8 + 1)
                                    arg1 = load32(9142892)
                                    if (u((v8 + 1)) < u(load32(9142892))):
                                        continue
                                    break
                                break
                            if (arg1 == 0):
                                break
                            arg0 = 0
                            while True:  # $label69
                                func239(arg0)
                                arg0 = (arg0 + 1)
                                if (u((arg0 + 1)) < u(load32(9142892))):
                                    continue
                                break
                            break
                        arg1 = load32(9561692)
                        arg0 = 39
                        while True:  # $label70
                            arg3 = (arg0 << 2)
                            arg4 = ((arg1 + (arg0 << 2)) + 283984)
                            if (load32(((arg1 + (arg0 << 2)) + 283984)) == 0):
                                store32(arg4, load32((arg3 + 9561072)))
                            arg3 = ((arg0 + 1) << 2)
                            arg4 = ((arg1 + ((arg0 + 1) << 2)) + 283984)
                            if (load32(((arg1 + ((arg0 + 1) << 2)) + 283984)) == 0):
                                store32(arg4, load32((arg3 + 9561072)))
                            arg0 = (arg0 + 2)
                            if ((arg0 + 2) != 155):
                                continue
                            break
                        v12 = (u(v15) < u(552))
                        if (u((u(v15) < u(552))) >= u(load32(9142892))):
                            break
                        arg0 = (v10 + (v14 << 2))
                        v21 = (v13 & 3)
                        v14 = (155 if (u(v15) > u(481)) else 40)
                        v34 = ((155 if (u(v15) > u(481)) else 40) & 184)
                        v19 = (v14 & 3)
                        v18 = (u(v15) < u(473))
                        v26 = (u(v15) < u(482))
                        v37 = (u(v15) < u(491))
                        v38 = (u(v15) < u(556))
                        arg3 = 0
                        while True:  # $label89
                            v7 = (load32(9561692) + (v12 * 286704))
                            store32((load32(9561692) + (v12 * 286704)) + 283908, v12)
                            arg1 = ((arg3 << 2) + arg0)
                            while True:  # block $label72
                                if load32(v7 + 284616):
                                    store32(v7 + 40, load32(arg1))
                                    store32(v7 + 44, load32(arg1 + 4))
                                    store32(v7 + 48, load32(arg1 + 8))
                                    store32(v7 + 52, load32(arg1 + 12))
                                    store32(v7 + 56, load32(arg1 + 16))
                                    store32(v7 + 60, load32(arg1 + 20))
                                    store32((v7 - -64), load32(arg1 + 24))
                                    store32(v7 + 68, load32(arg1 + 28))
                                    store32(v7 + 72, load32(arg1 + 32))
                                    store32(v7 + 76, load32(arg1 + 36))
                                    break
                                arg4 = load32(arg1)
                                store32(v7, load32(arg1))
                                v8 = load32(arg1 + 4)
                                store32(v7 + 4, load32(arg1 + 4))
                                v9 = load32(arg1 + 8)
                                store32(v7 + 8, load32(arg1 + 8))
                                v16 = load32(arg1 + 12)
                                store32(v7 + 12, load32(arg1 + 12))
                                v17 = load32(arg1 + 16)
                                store32(v7 + 16, load32(arg1 + 16))
                                v29 = load32(arg1 + 20)
                                store32(v7 + 20, load32(arg1 + 20))
                                v27 = load32(arg1 + 24)
                                store32(v7 + 24, load32(arg1 + 24))
                                v25 = load32(arg1 + 28)
                                store32(v7 + 28, load32(arg1 + 28))
                                v31 = load32(arg1 + 32)
                                store32(v7 + 32, load32(arg1 + 32))
                                v32 = load32(arg1 + 36)
                                store16(v7 + 76, load32(arg1 + 36))
                                store16(v7 + 74, ((v31 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 72, v31)
                                store16(v7 + 70, ((v25 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 68, v25)
                                store16(v7 + 66, ((v27 & 0xFFFFFFFF) >> 16))
                                store16((v7 - -64), v27)
                                store16(v7 + 62, ((v29 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 60, v29)
                                store16(v7 + 58, ((v17 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 56, v17)
                                store16(v7 + 54, ((v16 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 52, v16)
                                store16(v7 + 50, ((v9 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 48, v9)
                                store16(v7 + 46, ((v8 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 44, v8)
                                store16(v7 + 42, ((arg4 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 40, arg4)
                                store16(v7 + 36, v32)
                                arg4 = ((v32 & 0xFFFFFFFF) >> 16)
                                store16(v7 + 78, ((v32 & 0xFFFFFFFF) >> 16))
                                store16(v7 + 38, arg4)
                                break
                            while True:  # block $label73
                                arg4 = load32(arg1 + 40)
                                if (load32(arg1 + 40) == 0):
                                    break
                                if arg5:
                                    break
                                v16 = (v10 + (arg4 << 2))
                                arg4 = load32((v10 + (arg4 << 2)))
                                v8 = func26(16)
                                store32(func26(16) + 4, arg4)
                                v17 = (arg4 << 2)
                                v9 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                                store32(v8 + 12, 20)
                                store32(v8, v9)
                                store32(v8 + 8, arg4)
                                if arg4:
                                    # TODO: memory.copy []
                                store32(v7 + 281788, v8)
                                break
                            while True:  # block $label74
                                arg4 = load32(arg1 + 44)
                                if (load32(arg1 + 44) == 0):
                                    break
                                if arg5:
                                    break
                                v16 = (v10 + (arg4 << 2))
                                arg4 = load32((v10 + (arg4 << 2)))
                                v8 = func26(16)
                                v9 = (arg4 + 8)
                                store32(func26(16) + 4, (arg4 + 8))
                                v9 = func26((-1 if (u(v9) > u(1073741823)) else (v9 << 2)))
                                store32(v8 + 12, 20)
                                store32(v8, v9)
                                store32(v8 + 8, arg4)
                                if arg4:
                                    # TODO: memory.copy []
                                store32(v7 + 281792, v8)
                                break
                            v9 = (arg3 + 12)
                            if (v18 == 0):
                                while True:  # block $label75
                                    arg4 = load32((arg0 + (v9 << 2)))
                                    if (load32((arg0 + (v9 << 2))) == 0):
                                        break
                                    if arg5:
                                        break
                                    v16 = (v10 + (arg4 << 2))
                                    arg4 = load32((v10 + (arg4 << 2)))
                                    v8 = func26(16)
                                    store32(func26(16) + 4, arg4)
                                    v17 = (arg4 << 2)
                                    v9 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                                    store32(v8 + 12, 20)
                                    store32(v8, v9)
                                    store32(v8 + 8, arg4)
                                    if arg4:
                                        # TODO: memory.copy []
                                    store32(v7 + 281796, v8)
                                    break
                                arg1 = load32(arg1 + 52)
                                if load32(arg1 + 52):
                                    v9 = (v10 + (arg1 << 2))
                                    arg1 = load32((v10 + (arg1 << 2)))
                                    arg4 = func26(16)
                                    store32(func26(16) + 4, arg1)
                                    v16 = (arg1 << 2)
                                    v8 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
                                    store32(arg4 + 12, 20)
                                    store32(arg4, v8)
                                    store32(arg4 + 8, arg1)
                                    if arg1:
                                        # TODO: memory.copy []
                                    store32(v7 + 286680, arg4)
                                v9 = (arg3 + 14)
                            arg1 = 0
                            v8 = 0
                            while True:  # $label76
                                arg3 = (v7 + (v8 * 36))
                                arg4 = (arg0 + (v9 << 2))
                                store32(((v7 + (v8 * 36)) + 269376), load32((arg0 + (v9 << 2))))
                                store32((arg3 + 269380), load32(arg4 + 4))
                                store32((arg3 + 269384), load32(arg4 + 8))
                                store32((arg3 + 269388), load32(arg4 + 12))
                                store32((arg3 + 269392), load32(arg4 + 16))
                                store32((arg3 + 269396), load32(arg4 + 20))
                                store32((arg3 + 269400), load32(arg4 + 24))
                                store32((arg3 + 269404), load32(arg4 + 28))
                                store32((arg3 + 269408), load32(arg4 + 32))
                                v9 = (v9 + 9)
                                v8 = (v8 + 1)
                                if ((v8 + 1) != v13):
                                    continue
                                break
                            arg4 = 0
                            while True:  # $label77
                                arg3 = (v7 + 281808)
                                store32(((v7 + 281808) + (arg1 << 2)), load32((arg0 + ((arg1 + v9) << 2))))
                                v8 = (arg1 | 1)
                                store32((arg3 + ((arg1 | 1) << 2)), load32((arg0 + ((v8 + v9) << 2))))
                                v8 = (arg1 | 2)
                                store32((arg3 + ((arg1 | 2) << 2)), load32((arg0 + ((v8 + v9) << 2))))
                                v8 = (arg1 | 3)
                                store32((arg3 + ((arg1 | 3) << 2)), load32((arg0 + ((v8 + v9) << 2))))
                                arg1 = (arg1 + 4)
                                arg4 = (arg4 + 4)
                                if ((arg4 + 4) != 252):
                                    continue
                                break
                            arg3 = 0
                            while True:  # $label78
                                store32(((v7 + (arg1 << 2)) + 281808), load32((arg0 + ((arg1 + v9) << 2))))
                                arg1 = (arg1 + 1)
                                arg3 = (arg3 + 1)
                                if ((arg3 + 1) != v21):
                                    continue
                                break
                            arg3 = (v9 + v13)
                            v9 = 0
                            arg1 = 0
                            v8 = 0
                            if (arg5 == 0):
                                while True:  # $label79
                                    arg4 = (v7 + 282828)
                                    store32(((v7 + 282828) + (arg1 << 2)), load32((arg0 + ((arg1 + arg3) << 2))))
                                    v16 = (arg1 | 1)
                                    store32((arg4 + ((arg1 | 1) << 2)), load32((arg0 + ((arg3 + v16) << 2))))
                                    v16 = (arg1 | 2)
                                    store32((arg4 + ((arg1 | 2) << 2)), load32((arg0 + ((arg3 + v16) << 2))))
                                    v16 = (arg1 | 3)
                                    store32((arg4 + ((arg1 | 3) << 2)), load32((arg0 + ((arg3 + v16) << 2))))
                                    arg1 = (arg1 + 4)
                                    v8 = (v8 + 4)
                                    if ((v8 + 4) != 252):
                                        continue
                                    break
                                while True:  # $label80
                                    store32(((v7 + (arg1 << 2)) + 282828), load32((arg0 + ((arg1 + arg3) << 2))))
                                    arg1 = (arg1 + 1)
                                    v9 = (v9 + 1)
                                    if ((v9 + 1) != v21):
                                        continue
                                    break
                            arg3 = (arg3 + v13)
                            arg1 = (arg0 + ((arg3 + v13) << 2))
                            store32(v7 + 283848, load32((arg0 + ((arg3 + v13) << 2))))
                            store32((v7 + 283852), load32(arg1 + 4))
                            store32((v7 + 283856), load32(arg1 + 8))
                            store32((v7 + 283860), load32(arg1 + 12))
                            store32(v7 + 283864, load32(arg1 + 16))
                            store32(v7 + 283872, load32(arg1 + 20))
                            store32(v7 + 283876, load32(arg1 + 24))
                            store32(v7 + 283960, load32(arg1 + 28))
                            store32(v7 + 283968, load32(arg1 + 32))
                            store8(v7 + 283972, load32(arg1 + 36))
                            store8((v7 + 283973), ((load32(arg1 + 36) & 0xFFFFFFFF) >> 8))
                            store8((v7 + 283974), load16u(arg1 + 38))
                            arg3 = (arg3 + 10)
                            arg1 = 0
                            v9 = 0
                            while True:  # $label81
                                arg4 = (v7 + 283984)
                                store32(((v7 + 283984) + (arg1 << 2)), load32((arg0 + ((arg1 + arg3) << 2))))
                                v8 = (arg1 | 1)
                                store32((arg4 + ((arg1 | 1) << 2)), load32((arg0 + ((arg3 + v8) << 2))))
                                v8 = (arg1 | 2)
                                store32((arg4 + ((arg1 | 2) << 2)), load32((arg0 + ((arg3 + v8) << 2))))
                                v8 = (arg1 | 3)
                                store32((arg4 + ((arg1 | 3) << 2)), load32((arg0 + ((arg3 + v8) << 2))))
                                arg1 = (arg1 + 4)
                                v9 = (v9 + 4)
                                if ((v9 + 4) != v34):
                                    continue
                                break
                            v9 = 0
                            if v19:
                                while True:  # $label82
                                    store32(((v7 + (arg1 << 2)) + 283984), load32((arg0 + ((arg1 + arg3) << 2))))
                                    arg1 = (arg1 + 1)
                                    v9 = (v9 + 1)
                                    if ((v9 + 1) != v19):
                                        continue
                                    break
                            v9 = 39
                            if v26:
                                while True:  # $label83
                                    arg1 = (v9 << 2)
                                    store32((arg4 + (v9 << 2)), load32((arg1 + 9561072)))
                                    v8 = (arg1 + 4)
                                    store32((arg4 + (arg1 + 4)), load32((v8 + 9561072)))
                                    v8 = (arg1 + 8)
                                    store32((arg4 + (arg1 + 8)), load32((v8 + 9561072)))
                                    arg1 = (arg1 + 12)
                                    store32((arg4 + (arg1 + 12)), load32((arg1 + 9561072)))
                                    v9 = (v9 + 4)
                                    if ((v9 + 4) != 155):
                                        continue
                                    break
                            arg4 = (v7 + 283864)
                            while True:  # block $label86
                                while True:  # block $label85
                                    while True:  # block $label84
                                        if (v37 == 0):
                                            arg1 = (arg3 + v14)
                                            break
                                        store32((v7 + 284380), 4)
                                        store64((v7 + 284364), 19327352832002)
                                        store64((v7 + 284356), 85899345960)
                                        store64((v7 + 284384), 51539617552)
                                        store64((v7 + 284372), 137438953488)
                                        arg1 = (arg3 + v14)
                                        if v18:
                                            break
                                        break
                                    arg3 = (arg0 + (arg1 << 2))
                                    store32(v7 + 283868, load32((arg0 + (arg1 << 2))))
                                    store32(v7 + 283912, load32(arg3 + 4))
                                    store32(v7 + 283916, load32(arg3 + 8))
                                    store32(v7 + 283920, load32(arg3 + 12))
                                    store32(v7 + 283964, load32(arg3 + 16))
                                    store32(v7 + 283904, load32(arg3 + 20))
                                    store32(v7 + 283880, load32(arg3 + 24))
                                    arg1 = (arg1 + 7)
                                    store32(v7 + 283940, load32((arg0 + ((arg1 + 7) << 2))))
                                    break
                                    break
                                store32(arg4, load32((arg0 + (arg1 << 2))))
                                break
                            arg3 = (arg1 + 1)
                            if v23:
                                arg4 = (v7 + 284616)
                                store32(v7 + 281804, load32((arg0 + (arg3 << 2))))
                                arg3 = ((arg1 << 2) + arg0)
                                store32(v7 + 283924, load32(((arg1 << 2) + arg0) + 8))
                                store32(v7 + 283936, load32(arg3 + 12))
                                store32(v7 + 283948, load32(arg3 + 16))
                                store32(v7 + 283956, load32(arg3 + 20))
                                while True:  # block $label87
                                    if (v30 == 0):
                                        if (load8u(9561832) == 0):
                                            break
                                    store32(arg4, load32(arg3 + 24))
                                    break
                                store8(v7 + 286700, (load32(arg3 + 28) != 0))
                                store8(v7 + 286701, (load32(arg3 + 32) != 0))
                                arg3 = (arg1 + 9)
                            if (v38 == 0):
                                arg1 = (arg0 + (arg3 << 2))
                                store8(v7 + 286699, (load32((arg0 + (arg3 << 2))) != 0))
                                store8(v7 + 92, load32(arg1 + 4))
                                store8(v7 + 93, load32(arg1 + 8))
                                store32(v7 + 283964, load32(arg1 + 12))
                                store32(v7 + 283952, load32(arg1 + 16))
                                store32(v7 + 80, load32(arg1 + 20))
                                store32(v7 + 84, load32(arg1 + 24))
                                store32(v7 + 88, load32(arg1 + 28))
                                arg3 = (arg3 + 8)
                            while True:  # block $label88
                                if (v36 == 0):
                                    arg4 = arg3
                                    break
                                arg4 = (arg3 + 1)
                                arg3 = load32((arg0 + (arg3 << 2)))
                                if (load32((arg0 + (arg3 << 2))) == 0):
                                    break
                                if arg5:
                                    break
                                arg1 = load32(9142892)
                                v8 = (load32(9142892) << 2)
                                v9 = func26((-1 if (u(arg1) > u(1073741823)) else (load32(9142892) << 2)))
                                store32(v7 + 281800, func26((-1 if (u(arg1) > u(1073741823)) else (load32(9142892) << 2))))
                                if (arg1 == 0):
                                    break
                                # TODO: memory.copy []
                                break
                            arg1 = (arg0 + (arg4 << 2))
                            store32(v7 + 284608, load32((arg0 + (arg4 << 2))))
                            store32(v7 + 286684, load32(arg1 + 4))
                            store8(v7 + 286696, (load32(arg1 + 8) != 0))
                            if (arg5 == 0):
                                store32(v7 + 283976, load32(arg1 + 12))
                            store32(v7 + 283980, load32(arg1 + 16))
                            store32(v7 + 286688, load32(arg1 + 20))
                            store32(v7 + 283896, load32(arg1 + 24))
                            store32(v7 + 283900, load32(arg1 + 28))
                            if arg5:
                                store8(v7 + 286699, 1)
                            arg3 = (arg4 + 8)
                            v12 = (v12 + 1)
                            if (u((v12 + 1)) < u(load32(9142892))):
                                continue
                            break
                        break
                        break
                    func42()
                    raise RuntimeError('unreachable')
                    break
                func42()
                raise RuntimeError('unreachable')
                break
            arg1 = load32(9561692)
            break
        store16(arg1 + 283972, 65535)
        store8((arg1 + 283974), 255)
        arg0 = ((25 if (u(v15) < u(473)) else 30) if (u(v15) < u(552)) else (33 if (u(v15) > u(581)) else 32))
        # TODO: i32.div_u []
        v8 = ((25 if (u(v15) < u(473)) else 30) if (u(v15) < u(552)) else (33 if (u(v15) > u(581)) else 32))
        if arg5:
            arg1 = load32(9671136)
            v7 = func26((-1 if (u(arg1) > u(1073741823)) else (load32(9671136) << 2)))
        arg4 = 3
        if (u(arg0) <= u(v20)):
            v9 = (v10 + (v22 << 2))
            v19 = (1 if (u(v8) <= u(1)) else v8)
            v18 = (v8 << 5)
            v16 = (v8 * 31)
            v17 = (v8 * 30)
            v29 = (v8 * 29)
            v27 = (v8 * 28)
            v25 = (v8 * 27)
            v31 = (v8 * 26)
            v32 = (v8 * 25)
            v36 = (v8 * 24)
            v34 = (v8 * 22)
            v26 = (v8 * 21)
            v37 = (v8 * 20)
            v38 = (v8 * 19)
            v39 = (v8 * 17)
            v40 = (v8 * 15)
            v41 = (v8 * 14)
            v42 = (v8 * 13)
            v43 = (v8 * 12)
            v44 = (v8 * 10)
            v45 = (v8 * 9)
            v46 = (v8 << 3)
            v47 = (v8 * 7)
            v48 = (v8 * 5)
            v49 = (v8 << 2)
            v50 = (v8 << 1)
            v30 = (v8 << 4)
            v51 = (v8 * 11)
            v52 = (v8 * 3)
            v53 = (v8 * 23)
            v12 = load32(9671136)
            v54 = (u(v15) < u(473))
            v55 = (u(v15) < u(582))
            arg0 = 0
            while True:  # $label99
                while True:  # block $label91
                    arg3 = load32((v9 + ((arg0 + v52) << 2)))
                    if (load32((v9 + ((arg0 + v52) << 2))) == 0):
                        break
                    if (u(arg3) >= u(v12)):
                        break
                    v20 = (v9 + ((arg0 + v53) << 2))
                    arg1 = load32((v9 + ((arg0 + v53) << 2)))
                    v14 = ((load32((v9 + ((arg0 + v53) << 2))) & 0xFFFFFFFF) >> 24)
                    if (arg5 & (((load32((v9 + ((arg0 + v53) << 2))) & 0xFFFFFFFF) >> 24) == 3)):
                        break
                    v21 = load32((v9 + ((arg0 + v51) << 2)))
                    if (arg5 & (load32((v9 + ((arg0 + v51) << 2))) == 0)):
                        break
                    while True:  # block $label92
                        if (arg5 == 0):
                            break
                        if (load32(9147132) == 0):
                            break
                        if (load32(38788) != (arg1 & 255)):
                            break
                        if (u(load32((v9 + ((arg0 + v30) << 2)))) > u(2002)):
                            break
                        break
                    while True:  # block $label93
                        if (arg5 == 0):
                            arg1 = arg4
                            arg4 = arg3
                            break
                        store32((v7 + (arg3 << 2)), arg4)
                        arg1 = (arg4 + 1)
                        break
                    arg3 = (load32(9671128) + (arg4 * 132))
                    store32((load32(9671128) + (arg4 * 132)) + 28, arg4)
                    arg4 = load32((v9 + (arg0 << 2)))
                    if load32((v9 + (arg0 << 2))):
                        v22 = (v10 + (arg4 << 2))
                        arg4 = load32((v10 + (arg4 << 2)))
                        v12 = func26(16)
                        store32(func26(16) + 4, arg4)
                        v28 = (arg4 << 2)
                        v13 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                        store32(v12 + 12, 20)
                        store32(v12, v13)
                        store32(v12 + 8, arg4)
                        if arg4:
                            # TODO: memory.copy []
                        store32(arg3 + 16, v12)
                    arg4 = load32((v9 + ((arg0 + v8) << 2)))
                    if load32((v9 + ((arg0 + v8) << 2))):
                        v22 = (v10 + (arg4 << 2))
                        arg4 = load32((v10 + (arg4 << 2)))
                        v12 = func26(16)
                        store32(func26(16) + 4, arg4)
                        v28 = (arg4 << 2)
                        v13 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                        store32(v12 + 12, 20)
                        store32(v12, v13)
                        store32(v12 + 8, arg4)
                        if arg4:
                            # TODO: memory.copy []
                        store32(arg3 + 20, v12)
                    arg4 = load32((v9 + ((arg0 + v50) << 2)))
                    if load32((v9 + ((arg0 + v50) << 2))):
                        v22 = (v10 + (arg4 << 2))
                        arg4 = load32((v10 + (arg4 << 2)))
                        if (load32(arg3 + 24) == 0):
                            v12 = func26(16)
                            store64(func26(16), 0)
                            store64(v12 + 8, 0)
                            store32(arg3 + 24, v12)
                        v12 = func26(16)
                        store32(func26(16) + 4, arg4)
                        v28 = (arg4 << 2)
                        v13 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                        store32(v12 + 12, 20)
                        store32(v12, v13)
                        store32(v12 + 8, arg4)
                        if arg4:
                            # TODO: memory.copy []
                        store32(load32(arg3 + 24), v12)
                    store32(arg3 + 32, load32((v9 + ((arg0 + v49) << 2))))
                    store32(arg3 + 36, load32((v9 + ((arg0 + v48) << 2))))
                    store32(arg3 + 44, load32((v9 + ((arg0 + v47) << 2))))
                    store32(arg3 + 92, load32((v9 + ((arg0 + v46) << 2))))
                    store32(arg3 + 52, load32((v9 + ((arg0 + v45) << 2))))
                    arg4 = load32((v9 + ((arg0 + v44) << 2)))
                    store32(arg3 + 64, v21)
                    store32(arg3 + 60, arg4)
                    store32(arg3 + 68, load32((v9 + ((arg0 + v43) << 2))))
                    store32(arg3 + 72, load32((v9 + ((arg0 + v42) << 2))))
                    store32(arg3 + 76, load32((v9 + ((arg0 + v41) << 2))))
                    store32(arg3 + 80, load32((v9 + ((arg0 + v40) << 2))))
                    store32(arg3 + 84, load32((v9 + ((arg0 + v30) << 2))))
                    store32(arg3 + 88, load32((v9 + ((arg0 + v39) << 2))))
                    store32(arg3 + 108, load32((v9 + ((arg0 + v38) << 2))))
                    store32(arg3 + 112, load32((v9 + ((arg0 + v37) << 2))))
                    store32(arg3 + 116, load32((v9 + ((arg0 + v26) << 2))))
                    store16(arg3 + 120, load32((v9 + ((arg0 + v34) << 2))))
                    arg4 = load32(v20)
                    store8(arg3 + 125, v14)
                    store8(arg3 + 122, arg4)
                    store8(arg3 + 124, ((arg4 & 0xFFFFFFFF) >> 16))
                    store8(arg3 + 123, ((arg4 & 0xFFFFFFFF) >> 8))
                    arg4 = load32((v9 + ((arg0 + v36) << 2)))
                    store16(arg3 + 126, load32((v9 + ((arg0 + v36) << 2))))
                    v12 = load32(9671136)
                    while True:  # block $label94
                        if (load8u(9142916) == 0):
                            break
                        v13 = (((arg4 & 0xFFFFFFFF) >> 8) & 255)
                        if (u((((arg4 & 0xFFFFFFFF) >> 8) & 255)) > u(12)):
                            break
                        if (((1 << v13) & 7184) == 0):
                            break
                        store8(arg3 + 127, 0)
                        break
                    store8(arg3 + 129, ((arg4 & 0xFFFFFFFF) >> 24))
                    store8(arg3 + 128, ((arg4 & 0xFFFFFFFF) >> 16))
                    while True:  # block $label95
                        if v54:
                            break
                        store32(arg3 + 96, load32((v9 + ((arg0 + v32) << 2))))
                        store32(arg3 + 56, load32((v9 + ((arg0 + v31) << 2))))
                        arg4 = load32((v9 + ((arg0 + v25) << 2)))
                        if load32((v9 + ((arg0 + v25) << 2))):
                            v14 = (v10 + (arg4 << 2))
                            arg4 = load32((v10 + (arg4 << 2)))
                            if (load32(arg3 + 24) == 0):
                                v13 = func26(16)
                                store64(func26(16), 0)
                                store64(v13 + 8, 0)
                                store32(arg3 + 24, v13)
                            v13 = func26(16)
                            store32(func26(16) + 4, arg4)
                            v21 = (arg4 << 2)
                            v20 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                            store32(v13 + 12, 20)
                            store32(v13, v20)
                            store32(v13 + 8, arg4)
                            if arg4:
                                # TODO: memory.copy []
                            store32(load32(arg3 + 24) + 12, v13)
                        arg4 = load32((v9 + ((arg0 + v27) << 2)))
                        if load32((v9 + ((arg0 + v27) << 2))):
                            v14 = (v10 + (arg4 << 2))
                            arg4 = load32((v10 + (arg4 << 2)))
                            if (load32(arg3 + 24) == 0):
                                v13 = func26(16)
                                store64(func26(16), 0)
                                store64(v13 + 8, 0)
                                store32(arg3 + 24, v13)
                            v13 = func26(16)
                            store32(func26(16) + 4, arg4)
                            v21 = (arg4 << 2)
                            v20 = func26((-1 if (u(arg4) > u(1073741823)) else (arg4 << 2)))
                            store32(v13 + 12, 20)
                            store32(v13, v20)
                            store32(v13 + 8, arg4)
                            if arg4:
                                # TODO: memory.copy []
                            store32(load32(arg3 + 24) + 8, v13)
                        while True:  # block $label96
                            arg4 = load32((v9 + ((arg0 + v29) << 2)))
                            if (load32((v9 + ((arg0 + v29) << 2))) == 0):
                                break
                            v14 = (v10 + (arg4 << 2))
                            v13 = load32((v10 + (arg4 << 2)))
                            if (load32(arg3 + 24) == 0):
                                arg4 = func26(16)
                                store64(func26(16), 0)
                                store64(arg4 + 8, 0)
                                store32(arg3 + 24, arg4)
                            arg4 = func26(16)
                            store32(func26(16) + 4, v13)
                            v21 = (v13 << 2)
                            v20 = func26((-1 if (u(v13) > u(1073741823)) else (v13 << 2)))
                            store32(arg4 + 12, 20)
                            store32(arg4, v20)
                            store32(arg4 + 8, v13)
                            if (v13 == 0):
                                store32(load32(arg3 + 24) + 4, arg4)
                                break
                            # TODO: memory.copy []
                            store32(load32(arg3 + 24) + 4, arg4)
                            v22 = ((((v13 - 1) & 0xFFFFFFFF) >> 1) + 1)
                            v21 = (((((v13 - 1) & 0xFFFFFFFF) >> 1) + 1) & 3)
                            v14 = 0
                            arg4 = 0
                            if (u(v13) >= u(7)):
                                v28 = (v22 & -4)
                                v22 = 0
                                while True:  # $label97
                                    v13 = (arg4 << 2)
                                    store32((v20 + ((arg4 << 2) | 4)), 0)
                                    store32((v20 + (v13 | 12)), 0)
                                    store32((v20 + (v13 | 20)), 0)
                                    store32((v20 + (v13 | 28)), 0)
                                    arg4 = (arg4 + 8)
                                    v22 = (v22 + 4)
                                    if ((v22 + 4) != v28):
                                        continue
                                    break
                            if (v21 == 0):
                                break
                            while True:  # $label98
                                store32((v20 + ((arg4 << 2) | 4)), 0)
                                arg4 = (arg4 + 2)
                                v14 = (v14 + 1)
                                if ((v14 + 1) != v21):
                                    continue
                                break
                            break
                        if v23:
                            store32(arg3 + 100, load32((v9 + ((arg0 + v17) << 2))))
                            store32(arg3 + 104, load32((v9 + ((arg0 + v16) << 2))))
                        if v55:
                            break
                        store8(arg3 + 130, load32((v9 + ((arg0 + v18) << 2))))
                        break
                    arg4 = arg1
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v19):
                    continue
                break
        while True:  # block $label100
            if load32(9142848):
                break
            if (u(v15) > u(518)):
                break
            if (v24 == 0):
                arg1 = load32(9215884)
                arg0 = 0
                while True:  # $label101
                    arg3 = (arg0 << 2)
                    if (load32((arg1 + ((arg0 << 2) | 4))) == 22):
                        store32((arg1 + arg3), 0)
                    arg0 = (arg0 + 4)
                    if (u((arg0 + 4)) < u(arg6)):
                        continue
                    break
            arg0 = load32(9671136)
            if (u(load32(9671136)) < u(4)):
                break
            v23 = (arg0 - 3)
            arg3 = ((arg0 - 3) & 7)
            arg6 = load32(9671128)
            arg1 = 3
            if (u((arg0 - 4)) >= u(7)):
                v23 = (v23 & -8)
                v9 = 0
                while True:  # $label102
                    arg0 = (arg6 + (arg1 * 132))
                    store32((arg6 + (arg1 * 132)) + 44, 0)
                    store32(arg0 + 176, 0)
                    store32(arg0 + 308, 0)
                    store32(arg0 + 440, 0)
                    store32(arg0 + 572, 0)
                    store32(arg0 + 704, 0)
                    store32(arg0 + 836, 0)
                    store32(arg0 + 968, 0)
                    arg1 = (arg1 + 8)
                    v9 = (v9 + 8)
                    if ((v9 + 8) != v23):
                        continue
                    break
            if (arg3 == 0):
                break
            arg0 = 0
            while True:  # $label103
                store32((arg6 + (arg1 * 132)) + 44, 0)
                arg1 = (arg1 + 1)
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != arg3):
                    continue
                break
            break
        if v35:
            arg3 = (v10 + (v33 << 2))
            v23 = load32(9671128)
            arg1 = 0
            while True:  # $label104
                arg6 = (arg1 << 2)
                v8 = load32((arg3 + (arg1 << 2)))
                if load32((arg3 + (arg1 << 2))):
                    if arg5:
                        store32((v7 + (v8 << 2)), arg4)
                        v8 = arg4
                        arg4 = (arg4 + 1)
                    arg0 = (v23 + (v8 * 132))
                    store32((v23 + (v8 * 132)) + 28, v8)
                    store32(arg0 + 64, load32((arg3 + (arg6 | 4))))
                    store32(arg0 + 68, load32(((load32(38448) * 404) + 9568096) + 104))
                    store8(arg0 + 124, load32((arg3 + (arg6 | 8))))
                    store32(arg0 + 112, load32((arg3 + (arg6 | 12))))
                    store8(arg0 + 122, load32(38448))
                arg1 = (arg1 + 4)
                if (u((arg1 + 4)) < u(v35)):
                    continue
                break
        while True:  # block $label105
            if (arg5 == 0):
                break
            store32(9671136, arg4)
            if (u(arg4) >= u(4)):
                arg3 = load32(9671128)
                v9 = 3
                while True:  # $label108
                    arg0 = (arg3 + (v9 * 132))
                    arg1 = load32((arg3 + (v9 * 132)) + 36)
                    if load32((arg3 + (v9 * 132)) + 36):
                        store32(arg0 + 36, load32((v7 + (arg1 << 2))))
                    while True:  # block $label106
                        arg1 = load32(arg0 + 16)
                        if (load32(arg0 + 16) == 0):
                            break
                        if (load32(arg1 + 8) == 0):
                            break
                        arg4 = load32(arg1)
                        arg0 = 0
                        while True:  # $label107
                            arg5 = (arg4 + (arg0 << 2))
                            store32((arg4 + (arg0 << 2)), load32((v7 + (load32(arg5) << 2))))
                            arg0 = (arg0 + 1)
                            if (u((arg0 + 1)) < u(load32(arg1 + 8))):
                                continue
                            break
                        arg4 = load32(9671136)
                        break
                    v9 = (v9 + 1)
                    if (u((v9 + 1)) < u(arg4)):
                        continue
                    break
            if (v7 == 0):
                break
            break
        v7 = 1
        if (arg2 == 0):
            break
        store32(v11 + 32, (load32(9142892) - 1))
        while True:  # block $label109
            arg3 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            arg0 = load32(9561692)
            if (load32((load32(9561692) + 570612)) == 0):
                break
            arg1 = 1
            while True:  # $label110
                arg0 = (arg0 + (arg1 * 286704))
                arg2 = load8u((arg0 + (arg1 * 286704)) + 283972)
                arg3 = load8u((arg0 + 283974))
                arg4 = load8u((arg0 + 283973))
                store32(v11 + 20, load32(arg0 + 284608))
                store32(v11 + 16, arg0)
                store32(v11 + 24, ((arg3 | (arg4 << 8)) | (arg2 << 16)))
                arg1 = (arg1 + 1)
                arg3 = load32(9142892)
                if (u((arg1 + 1)) >= u(load32(9142892))):
                    break
                arg0 = load32(9561692)
                if load32((load32(9561692) + (arg1 * 286704)) + 283908):
                    continue
                break
            break
        store32(v11, (arg3 - 1))
        break
    G.global0 = (v11 + 400)
    return v7

# ------------------------------------------------------------
# $Fb
# Export: Fb
# ------------------------------------------------------------
def Fb():
    """Exported as Fb."""
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store64(v5 + 20, 0)
    store32(v5 + 28, 0)
    v8 = load32(9687244)
    v0 = (load32(9687244) + load32(9687248))
    if (load32(9687244) + load32(9687248)):
        while True:  # block $label0
            v3 = load32(v5 + 28)
            v8 = load32(v5 + 24)
            if (u(v0) <= u(((load32(v5 + 28) - load32(v5 + 24)) // 20))):
                if v0:
                    v0 = ((v0 * 20) - 20)
                    v0 = ((((v0 * 20) - 20) - (v0 % 20)) + 20)
                    # TODO: memory.fill []
                else:
                store32((v0 + v8) + 24, v8)
                break
            while True:  # block $label1
                v8 = load32(v5 + 20)
                v4 = (v8 - load32(v5 + 20))
                v6 = ((v8 - load32(v5 + 20)) // 20)
                v2 = (((v8 - load32(v5 + 20)) // 20) + v0)
                if (u((((v8 - load32(v5 + 20)) // 20) + v0)) < u(214748365)):
                    v3 = ((v3 - v8) // 20)
                    v7 = (((v3 - v8) // 20) << 1)
                    v2 = (214748364 if (u(v3) >= u(107374182)) else ((((v3 - v8) // 20) << 1) if (u(v2) < u(v7)) else v2))
                    if (214748364 if (u(v3) >= u(107374182)) else ((((v3 - v8) // 20) << 1) if (u(v2) < u(v7)) else v2)):
                        if (u(v2) >= u(214748365)):
                            break
                        v9 = func26((v2 * 20))
                    v3 = ((v6 * 20) + v9)
                    v0 = ((v0 * 20) - 20)
                    v0 = ((((v0 * 20) - 20) - (v0 % 20)) + 20)
                    # TODO: memory.fill []
                    v6 = (v3 + ((v4 // -20) * 20))
                    # TODO: memory.copy []
                    store32(v5 + 28, (v9 + (v2 * 20)))
                    store32(v5 + 24, (v0 + v3))
                    store32(v5 + 20, v6)
                    if v8:
                    break
                func42()
                raise RuntimeError('unreachable')
                break
            func68()
            raise RuntimeError('unreachable')
            break
    else:
    if v8:
        while True:  # $label2
            v0 = (load32(9684500) + (v1 * 60))
            v23 = load64((load32(9684500) + (v1 * 60)))
            v24 = load64(v0 + 16)
            v8 = (load32(v5 + 20) + (v1 * 20))
            store32((load32(v5 + 20) + (v1 * 20)) + 16, (v0 + 48))
            store64(v8 + 8, v24)
            store64(v8, v23)
            v1 = (v1 + 1)
            if (u((v1 + 1)) < u(load32(9687244))):
                continue
            break
    v8 = 0
    if load32(9687248):
        while True:  # $label3
            v0 = (load32(9684496) + (v8 * 60))
            v23 = load64((load32(9684496) + (v8 * 60)))
            v24 = load64(v0 + 16)
            v9 = (load32(v5 + 20) + (v1 * 20))
            store32((load32(v5 + 20) + (v1 * 20)) + 16, (v0 + 48))
            store64(v9 + 8, v24)
            store64(v9, v23)
            v1 = (v1 + 1)
            v8 = (v8 + 1)
            if (u((v8 + 1)) < u(load32(9687248))):
                continue
            break
    store32(v5 + 16, 0)
    store64(v5 + 8, 0)
    while True:  # block $label4
        v4 = load32(v5 + 24)
        v3 = load32(v5 + 20)
        if (load32(v5 + 24) == load32(v5 + 20)):
            v8 = 0
            break
        v1 = 0
        v8 = 0
        v9 = 0
        while True:  # $label10
            v2 = (v3 + (v9 * 20))
            v0 = load32((v3 + (v9 * 20)) + 4)
            v6 = load32(v2 + 12)
            v7 = load32(v2 + 8)
            store32(load32(v2 + 16), v8)
            v0 = (v6 * v7)
            # TODO: i32.div_u []
            v6 = (v6 * v7)
            if v0:
                v0 = (v0 + v8)
                while True:  # block $label9
                    while True:  # block $label7
                        while True:  # $label8
                            while True:  # block $label6
                                v7 = (v8 * 3)
                                v10 = load32(v2)
                                while True:  # block $label5
                                    v3 = load32(v5 + 16)
                                    if (u(load32(v5 + 16)) > u(v1)):
                                        store32(v1 + 24, -1)
                                        store64(v1 + 16, -1)
                                        store32(v1 + 12, v6)
                                        store32(v1 + 8, v10)
                                        store32(v1 + 4, v7)
                                        store32(v1, v9)
                                        v1 = (v1 + 28)
                                        store32(v5 + 12, (v1 + 28))
                                        break
                                    v4 = load32(v5 + 8)
                                    v11 = (v1 - load32(v5 + 8))
                                    v12 = ((v1 - load32(v5 + 8)) // 28)
                                    v1 = (((v1 - load32(v5 + 8)) // 28) + 1)
                                    if (u((((v1 - load32(v5 + 8)) // 28) + 1)) >= u(153391690)):
                                        break
                                    v3 = ((v3 - v4) // 28)
                                    v14 = (((v3 - v4) // 28) << 1)
                                    v3 = (153391689 if (u(v3) >= u(76695844)) else ((((v3 - v4) // 28) << 1) if (u(v1) < u(v14)) else v1))
                                    if (153391689 if (u(v3) >= u(76695844)) else ((((v3 - v4) // 28) << 1) if (u(v1) < u(v14)) else v1)):
                                        if (u(v3) >= u(153391690)):
                                            break
                                    else:
                                    v14 = 0
                                    v1 = (0 + (v12 * 28))
                                    store32((0 + (v12 * 28)) + 24, -1)
                                    store64(v1 + 16, -1)
                                    store32(v1 + 12, v6)
                                    store32(v1 + 8, v10)
                                    store32(v1 + 4, v7)
                                    store32(v1, v9)
                                    v7 = (v1 + ((v11 // -28) * 28))
                                    # TODO: memory.copy []
                                    store32(v5 + 16, (v14 + (v3 * 28)))
                                    v1 = (v1 + 28)
                                    store32(v5 + 12, (v1 + 28))
                                    store32(v5 + 8, v7)
                                    if (v4 == 0):
                                        break
                                    break
                                v8 = (v8 + 1)
                                if (v0 != (v8 + 1)):
                                    continue
                                break
                                break
                            break
                        func42()
                        raise RuntimeError('unreachable')
                        break
                    func68()
                    raise RuntimeError('unreachable')
                    break
                v3 = load32(v5 + 20)
                v4 = load32(v5 + 24)
                v8 = v0
            v9 = (v9 + 1)
            if (u((v9 + 1)) < u(((v4 - v3) // 20))):
                continue
            break
        break
    v14 = load32(v5 + 8)
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    store32(v2 + 24, 8192)
    store32(v2 + 28, 8192)
    v1 = load32(v5 + 8)
    v0 = load32(v5 + 12)
    v1 = ((load32(v5 + 12) - load32(v5 + 8)) // 28)
    v19 = func26((-1 if (u((v1 * 3)) > u(1073741823)) else (((load32(v5 + 12) - load32(v5 + 8)) // 28) * 12)))
    store32(9687240, func26((-1 if (u((v1 * 3)) > u(1073741823)) else (((load32(v5 + 12) - load32(v5 + 8)) // 28) * 12))))
    store32(v2 + 20, 0)
    store64(v2 + 12, 0)
    v9 = load32(v5 + 8)
    v20 = load32(v5 + 12)
    if (load32(v5 + 8) != load32(v5 + 12)):
        while True:  # $label28
            while True:  # block $label27
                while True:  # block $label11
                    v7 = (load32(v9 + 8) + 8)
                    v15 = load32(v2 + 28)
                    if ((load32(v9 + 8) + 8) > load32(v2 + 28)):
                        break
                    v10 = (load32(v9 + 12) + 8)
                    v17 = load32(v2 + 24)
                    if ((load32(v9 + 12) + 8) > load32(v2 + 24)):
                        break
                    while True:  # block $label17
                        while True:  # block $label16
                            while True:  # block $label18
                                v3 = load32(v2 + 16)
                                v18 = load32(v2 + 12)
                                if (load32(v2 + 16) != load32(v2 + 12)):
                                    v1 = ((v3 - v18) >> 5)
                                    v21 = (1 if (u(v1) <= u(1)) else ((v3 - v18) >> 5))
                                    v11 = 0
                                    while True:  # $label19
                                        while True:  # block $label12
                                            v1 = (v18 + (v11 << 5))
                                            v0 = load32((v18 + (v11 << 5)) + 24)
                                            v12 = load32(v1 + 20)
                                            if (load32((v18 + (v11 << 5)) + 24) == load32(v1 + 20)):
                                                break
                                            v0 = ((v0 - v12) >> 4)
                                            v22 = (1 if (u(v0) <= u(1)) else ((v0 - v12) >> 4))
                                            v6 = 2147483647
                                            v0 = 0
                                            v4 = -1
                                            while True:  # $label14
                                                while True:  # block $label13
                                                    v13 = (v12 + (v0 << 4))
                                                    v16 = load32((v12 + (v0 << 4)) + 8)
                                                    if (load32((v12 + (v0 << 4)) + 8) < v7):
                                                        break
                                                    v13 = load32(v13 + 12)
                                                    if (load32(v13 + 12) < v10):
                                                        break
                                                    v13 = (v13 - v10)
                                                    v16 = (v16 - v7)
                                                    v13 = ((v13 - v10) if (v13 < v16) else (v16 - v7))
                                                    v13 = (v6 > v13)
                                                    v6 = (((v13 - v10) if (v13 < v16) else (v16 - v7)) if (v6 > v13) else v6)
                                                    v4 = (v0 if v13 else v4)
                                                    break
                                                v0 = (v0 + 1)
                                                if ((v0 + 1) != v22):
                                                    continue
                                                break
                                            if (v4 == -1):
                                                break
                                            v0 = (v12 + (v4 << 4))
                                            store32(v2 + 32, load32((v12 + (v4 << 4))))
                                            v3 = load32(v0 + 4)
                                            store32(v2 + 44, v10)
                                            store32(v2 + 40, v7)
                                            store32(v2 + 36, v3)
                                            store64(v2 + 56, load64(v0 + 8))
                                            store64(v2 + 48, load64(v0))
                                            v3 = load32(v1 + 24)
                                            if (v4 != (((load32(v1 + 24) - v12) >> 4) - 1)):
                                                v4 = (v3 - 16)
                                                store64(v0, load64((v3 - 16)))
                                                store64(v0 + 8, load64(v4 + 8))
                                            else:
                                            store32(load32(v1 + 24) + 24, (v3 - 16))
                                            while True:  # block $label15
                                                v0 = load32(v1 + 12)
                                                if (load32(v1 + 12) != load32(v1 + 16)):
                                                    store64(v0, load64(v2 + 32))
                                                    store64(v0 + 8, load64(v2 + 40))
                                                    store32(v1 + 12, (v0 + 16))
                                                    break
                                                v0 = load32(v1 + 8)
                                                v4 = (v0 - load32(v1 + 8))
                                                v7 = ((v0 - load32(v1 + 8)) >> 4)
                                                v3 = (((v0 - load32(v1 + 8)) >> 4) + 1)
                                                if (u((((v0 - load32(v1 + 8)) >> 4) + 1)) >= u(268435456)):
                                                    break
                                                v6 = (v4 >> 3)
                                                v3 = (268435455 if (u(v4) >= u(2147483632)) else ((v4 >> 3) if (u(v3) < u(v6)) else v3))
                                                if (268435455 if (u(v4) >= u(2147483632)) else ((v4 >> 3) if (u(v3) < u(v6)) else v3)):
                                                    if (u(v3) >= u(268435456)):
                                                        break
                                                else:
                                                v6 = 0
                                                v7 = (0 + (v7 << 4))
                                                store64((0 + (v7 << 4)), load64(v2 + 32))
                                                store64(v7 + 8, load64(v2 + 40))
                                                # TODO: memory.copy []
                                                store32(v1 + 8, v6)
                                                store32(v1 + 12, (v7 + 16))
                                                store32(v1 + 16, (v6 + (v3 << 4)))
                                                if (v0 == 0):
                                                    break
                                                break
                                            v1 = load32(v2 + 32)
                                            v0 = (load32(v2 + 36) + 4)
                                            store32(v9 + 20, (load32(v2 + 36) + 4))
                                            v1 = (v1 + 4)
                                            store32(v9 + 16, (v1 + 4))
                                            break
                                            break
                                        v11 = (v11 + 1)
                                        if ((v11 + 1) != v21):
                                            continue
                                        break
                                while True:  # block $label20
                                    if (u(load32(v2 + 20)) > u(v3)):
                                        store64(v3 + 8, 0)
                                        store32(v3 + 4, v17)
                                        store32(v3, v15)
                                        store64(v3 + 16, 0)
                                        store64(v3 + 24, 0)
                                        v1 = func26(16)
                                        store32(func26(16) + 12, v17)
                                        store32(v1 + 8, v15)
                                        store64(v1, 0)
                                        v0 = (v1 + 16)
                                        store32(v3 + 28, (v1 + 16))
                                        store32(v3 + 24, v0)
                                        store32(v3 + 20, v1)
                                        v0 = (v3 + 32)
                                        store32(v2 + 16, (v3 + 32))
                                        break
                                    v0 = load32(v2 + 16)
                                    break
                                v1 = (v0 - 32)
                                v0 = load32((v0 - 32) + 24)
                                v3 = load32(v1 + 20)
                                if (load32((v0 - 32) + 24) == load32(v1 + 20)):
                                    break
                                v0 = ((v0 - v3) >> 4)
                                v11 = (1 if (u(v0) <= u(1)) else ((v0 - v3) >> 4))
                                v6 = 2147483647
                                v0 = 0
                                v4 = -1
                                while True:  # $label22
                                    while True:  # block $label21
                                        v12 = (v3 + (v0 << 4))
                                        v15 = load32((v3 + (v0 << 4)) + 8)
                                        if (load32((v3 + (v0 << 4)) + 8) < v7):
                                            break
                                        v12 = load32(v12 + 12)
                                        if (load32(v12 + 12) < v10):
                                            break
                                        v12 = (v12 - v10)
                                        v15 = (v15 - v7)
                                        v12 = ((v12 - v10) if (v12 < v15) else (v15 - v7))
                                        v12 = (v6 > v12)
                                        v6 = (((v12 - v10) if (v12 < v15) else (v15 - v7)) if (v6 > v12) else v6)
                                        v4 = (v0 if v12 else v4)
                                        break
                                    v0 = (v0 + 1)
                                    if ((v0 + 1) != v11):
                                        continue
                                    break
                                if (v4 == -1):
                                    break
                                v6 = (v4 << 4)
                                v0 = (v3 + (v4 << 4))
                                store32(v2 + 48, load32((v3 + (v4 << 4))))
                                v0 = load32(v0 + 4)
                                store32(v2 + 60, v10)
                                store32(v2 + 56, v7)
                                store32(v2 + 52, v0)
                                v0 = (v2 + 48)
                                v3 = (G.global0 - 16)
                                G.global0 = (G.global0 - 16)
                                v10 = load32(v1 + 20)
                                v6 = (v6 + load32(v1 + 20))
                                store64(v3 + 8, load64((v6 + load32(v1 + 20)) + 8))
                                store64(v3, load64(v6))
                                v7 = load32(v1 + 24)
                                if (v4 != (((load32(v1 + 24) - v10) >> 4) - 1)):
                                    v4 = (v7 - 16)
                                    store64(v6, load64((v7 - 16)))
                                    store64(v6 + 8, load64(v4 + 8))
                                else:
                                store32(load32(v1 + 24) + 24, (v7 - 16))
                                while True:  # block $label26
                                    while True:  # block $label25
                                        while True:  # block $label24
                                            while True:  # block $label23
                                                v4 = load32(v1 + 12)
                                                if (load32(v1 + 12) != load32(v1 + 16)):
                                                    store64(v4, load64(v0))
                                                    store64(v4 + 8, load64(v0 + 8))
                                                    store32(v1 + 12, (v4 + 16))
                                                    break
                                                v4 = load32(v1 + 8)
                                                v6 = (v4 - load32(v1 + 8))
                                                v11 = ((v4 - load32(v1 + 8)) >> 4)
                                                v7 = (((v4 - load32(v1 + 8)) >> 4) + 1)
                                                if (u((((v4 - load32(v1 + 8)) >> 4) + 1)) >= u(268435456)):
                                                    break
                                                v10 = (v6 >> 3)
                                                v7 = (268435455 if (u(v6) >= u(2147483632)) else ((v6 >> 3) if (u(v7) < u(v10)) else v7))
                                                if (268435455 if (u(v6) >= u(2147483632)) else ((v6 >> 3) if (u(v7) < u(v10)) else v7)):
                                                    if (u(v7) >= u(268435456)):
                                                        break
                                                else:
                                                v10 = 0
                                                v11 = (0 + (v11 << 4))
                                                store64((0 + (v11 << 4)), load64(v0))
                                                store64(v11 + 8, load64(v0 + 8))
                                                # TODO: memory.copy []
                                                store32(v1 + 16, (v10 + (v7 << 4)))
                                                store32(v1 + 12, (v11 + 16))
                                                store32(v1 + 8, v10)
                                                if (v4 == 0):
                                                    break
                                                break
                                            G.global0 = (v3 + 16)
                                            break
                                            break
                                        func42()
                                        raise RuntimeError('unreachable')
                                        break
                                    func68()
                                    raise RuntimeError('unreachable')
                                    break
                                v1 = load32(v2 + 48)
                                v0 = (load32(v2 + 52) + 4)
                                store32(v9 + 20, (load32(v2 + 52) + 4))
                                v1 = (v1 + 4)
                                store32(v9 + 16, (v1 + 4))
                                v11 = (((load32(v2 + 16) - load32(v2 + 12)) >> 5) - 1)
                                break
                            store32(v9 + 24, v11)
                            v4 = (load32(v9 + 4) << 2)
                            v3 = (v19 + (load32(v9 + 4) << 2))
                            store32((v19 + (load32(v9 + 4) << 2)), float(v1))
                            store32(v3 + 4, float(v0))
                            store32((v4 + load32(9687240)) + 8, v11)
                            break
                            break
                        func42()
                        raise RuntimeError('unreachable')
                        break
                    func68()
                    raise RuntimeError('unreachable')
                    break
                store64(v9 + 16, -1)
                store32(v9 + 24, -1)
                break
            v9 = (v9 + 28)
            if ((v9 + 28) != v20):
                continue
            break
    v9 = load32(v2 + 12)
    if load32(v2 + 12):
        v0 = load32(v2 + 16)
        v1 = v9
        if (load32(v2 + 16) != v9):
            while True:  # $label29
                v1 = (v0 - 32)
                v4 = load32((v0 - 32) + 20)
                if load32((v0 - 32) + 20):
                    store32((v0 - 8), v4)
                v4 = load32((v0 - 24))
                if load32((v0 - 24)):
                    store32((v0 - 20), v4)
                v0 = v1
                if (v1 != v9):
                    continue
                break
            v1 = load32(v2 + 12)
        store32(v2 + 16, v9)
    G.global0 = (v2 - -64)
    store32(v5 + 4, (v8 * 3))
    store32(v5, load32(9687240))
    if v14:
    v1 = load32(v5 + 20)
    if load32(v5 + 20):
        store32(v5 + 24, v1)
    G.global0 = (v5 + 32)
    return af(v1)

# ------------------------------------------------------------
# $O
# Export: O
# ------------------------------------------------------------
def O(arg0):
    """Exported as O."""
    return (load32(9561692) + (arg0 * 286704))

# ------------------------------------------------------------
# $Nb
# Export: Nb
# ------------------------------------------------------------
def Nb():
    """Exported as Nb."""
    while True:  # block $label0
        v1 = load8u(9147210)
        if (load8u(9147210) == 0):
            store32(9142872, 1)
            break
        while True:  # block $label1
            v2 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            v4 = load32(9142384)
            v5 = load32(9561692)
            v0 = 1
            while True:  # $label2
                if (load32((v5 + (v0 * 286704)) + 284616) == v4):
                    break
                v0 = (v0 + 1)
                if ((v0 + 1) != v2):
                    continue
                break
            v0 = 0
            break
        store32(9142872, v0)
        store32(9142892, load32(41092))
        break
    v10 = load32(9561692)
    store16(load32(9561692) + 283972, 65535)
    store8((v10 + 283974), 255)
    v3 = load32(9142424)
    v4 = load32(load32(9142424) + 16)
    v0 = (load32(load32(9142424) + 16) == 991915600)
    store8(9216060, (load32(load32(9142424) + 16) == 991915600))
    v6 = load32(v3 + 4)
    v11 = load32(v3 + 4)
    v7 = load32(v3 + 8)
    v12 = load32(v3 + 8)
    v8 = load32(v3 + 12)
    v9 = load32(v3 + 12)
    v5 = v4
    v2 = load32(v3 + 44)
    if (u(load32(v3 + 44)) >= u(101)):
        v2 = ((v2 * 15) - 1500)
        # TODO: i32.div_u []
        v5 = (100 + v4)
        # TODO: i32.div_u []
        v12 = (100 + v7)
        # TODO: i32.div_u []
        v11 = (100 + v6)
        # TODO: i32.div_u []
        v9 = (100 + v8)
    while True:  # block $label3
        if (u(load32(9142892)) < u(2)):
            break
        v4 = (0 if v0 else v4)
        v2 = 1
        if (v1 == 0):
            while True:  # $label6
                while True:  # block $label4
                    v0 = (v10 + (v2 * 286704))
                    if (u(load32((v10 + (v2 * 286704)) + 283960)) <= u(2)):
                        v1 = load32(v0 + 284616)
                        break
                    v1 = load32(v0 + 284616)
                    store32((v0 + 283960), ((load32(v0 + 284616) + load32(v3 + 184)) % 3))
                    break
                while True:  # block $label5
                    if (((v1 == 0) & (u(v2) > u(1))) == 0):
                        v1 = load32(v0 + 286684)
                        break
                    v1 = load32(v3 + 44)
                    store32(v0 + 286684, load32(v3 + 44))
                    store32(v0 + 286688, load32(v3 + 52))
                    break
                store32(v0 + 283848, (v11 if v1 else v6))
                store32((v0 + 283860), (v5 if v1 else v4))
                store32((v0 + 283856), (v9 if v1 else v8))
                store32((v0 + 283852), (v12 if v1 else v7))
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(load32(9142892))):
                    continue
                break
                break
            raise RuntimeError('unreachable')
        while True:  # $label9
            while True:  # block $label7
                v0 = (v10 + (v2 * 286704))
                if (u(load32((v10 + (v2 * 286704)) + 283960)) <= u(2)):
                    v1 = load32(v0 + 284616)
                    break
                v1 = load32(v0 + 284616)
                store32((v0 + 283960), ((load32(v0 + 284616) + load32(v3 + 184)) % 3))
                break
            while True:  # block $label8
                if v1:
                    v1 = load32(v0 + 286684)
                    break
                v1 = load32(v3 + 44)
                store32(v0 + 286684, load32(v3 + 44))
                store32(v0 + 286688, load32(v3 + 52))
                break
            store32(v0 + 283848, (v11 if v1 else v6))
            store32((v0 + 283860), (v5 if v1 else v4))
            store32((v0 + 283856), (v9 if v1 else v8))
            store32((v0 + 283852), (v12 if v1 else v7))
            v2 = (v2 + 1)
            if (u((v2 + 1)) < u(load32(9142892))):
                continue
            break
        break

# ------------------------------------------------------------
# $Gb
# Export: Gb
# ------------------------------------------------------------
def Gb(arg0):
    """Exported as Gb."""
    v3 = load32(9142440)
    if (load32(9142440) > 0):
        while True:  # $label3
            v4 = (v1 + 1)
            arg0 = 0
            while True:  # $label2
                v2 = load32(9142440)
                v5 = ((load32(9142440) * arg0) + v1)
                v6 = load32(9147288)
                while True:  # block $label1
                    while True:  # block $label0
                        arg0 = (arg0 + 1)
                        if (load32((load32(9142840) + ((v4 + ((arg0 + 1) * (v2 + 2))) << 2))) == 1):
                            break
                        v2 = (v5 + v6)
                        v7 = load8s((v5 + v6))
                        if (load8s((v5 + v6)) >= 0):
                            if (load32(load32((load32(9140332) + ((v7 & 255) << 2))) + 32) == 23):
                                break
                        store8(v2, 0)
                        break
                        break
                    store8((v5 + v6), 1)
                    break
                if (arg0 != v3):
                    continue
                break
            v1 = v4
            if (v4 != v3):
                continue
            break
    arg0 = 0
    v1 = load32(9681936)
    if load32(9681936):
        if load32(v1 + 8):
            while True:  # $label4
                func38(load32((load32(v1) + ((arg0 << 2) | 12))))
                arg0 = (arg0 + 4)
                v1 = load32(9681936)
                if (u((arg0 + 4)) < u(load32(load32(9681936) + 8))):
                    continue
                break
        store32(v1 + 8, 0)
        store32(9140328, 0)
    store8(9681940, 1)

# ------------------------------------------------------------
# $Xc
# Export: Xc
# ------------------------------------------------------------
def Xc(arg0):
    """Exported as Xc."""
    v1 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    while True:  # block $label0
        v2 = load32(9568088)
        v3 = load32(load32(9568088) + 28)
        if (load32(load32(9568088) + 28) == 0):
            break
        # TODO: f32.convert_i32_u []
        v5 = (v3 << 5)
        # TODO: f32.convert_i32_u []
        v6 = (load32(v2 + 40) << 5)
        # TODO: f32.convert_i32_u []
        v7 = (load32(v2 + 24) << 5)
        # TODO: f32.convert_i32_u []
        v8 = (load32(v2 + 20) << 5)
        if (load8u(9142917) == 0):
            while True:  # block $label1
                v4 = ((v6 * 0.5) + v7)
                if ((((v6 * 0.5) + v7) < 4294967300.0) & (v4 >= 0.0)):
                    # TODO: i32.trunc_f32_u []
                    break
                break
            store32(v4 + 84, 0)
            while True:  # block $label2
                v4 = ((v5 * 0.5) + v8)
                if ((((v5 * 0.5) + v8) < 4294967300.0) & (v4 >= 0.0)):
                    # TODO: i32.trunc_f32_u []
                    break
                break
            store32(v4 + 80, 0)
        if (arg0 == 0):
            store8(9684432, 1)
        arg0 = load32(9142876)
        if load8u(9142916):
            # TODO: f32.convert_i32_u []
            # TODO: f64.promote_f32 []
        else:
        v9 = 0.0
        store32(v1 + 72, arg0)
        store32((v1 - -64), v9)
        # TODO: f64.promote_f32 []
        store32(v1 + 56, v7)
        # TODO: f64.promote_f32 []
        store32(v1 + 48, v8)
        a_b()
        if load8u(9142916):
            break
        store64(v1 + 16, 0)
        store64(v1 + 24, 0)
        store32(v1 + 32, load32(9142876))
        # TODO: f64.promote_f32 []
        store32(v1 + 8, v6)
        # TODO: f64.promote_f32 []
        store32(v1, (-v5))
        a_b()
        break
    G.global0 = (v1 + 96)
    return v1

# ------------------------------------------------------------
# $Xb
# Export: Xb
# ------------------------------------------------------------
def Xb(arg0):
    """Exported as Xb."""
    v6 = load32(9142892)
    v3 = (load32(9142892) + 1)
    store32(9142892, (load32(9142892) + 1))
    v12 = (i64(v3) * 286704)
    v3 = (-1 if i32(((v12 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(v3) * 286704)))
    v4 = func26((-1 if i32(((v12 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(v3) * 286704))))
    # TODO: memory.fill []
    v1 = load32(9561692)
    while True:  # block $label4
        while True:  # block $label3
            while True:  # block $label1
                if v6:
                    if (u(v6) >= u(4)):
                        v5 = (v6 & -4)
                        v3 = 0
                        while True:  # $label0
                            v7 = (v2 * 286704)
                            # TODO: memory.copy []
                            v7 = ((v2 | 1) * 286704)
                            # TODO: memory.copy []
                            v7 = ((v2 | 2) * 286704)
                            # TODO: memory.copy []
                            v7 = ((v2 | 3) * 286704)
                            # TODO: memory.copy []
                            v2 = (v2 + 4)
                            v3 = (v3 + 4)
                            if ((v3 + 4) != v5):
                                continue
                            break
                    v6 = (v6 & 3)
                    if ((v6 & 3) == 0):
                        break
                    v3 = 0
                    while True:  # $label2
                        v5 = (v2 * 286704)
                        # TODO: memory.copy []
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        if ((v3 + 1) != v6):
                            continue
                        break
                    break
                if v1:
                    break
                v3 = 0
                store32(9561692, v4)
                v2 = (v4 + (v6 * 286704))
                v6 = 1
                break
                break
            store32(9561692, v4)
            v6 = load32(9142892)
            v3 = (load32(9142892) - 1)
            v2 = (v4 + ((load32(9142892) - 1) * 286704))
            if (u(v3) <= u(8)):
                break
            v12 = load64(9147316)
            v1 = load32(9147312)
            store32(9147316, load32(9147312))
            v5 = load32(9147324)
            store64(9147320, v12)
            v5 = (v5 ^ (v5 << 11))
            v1 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v5 ^ (v5 << 11)) & 0xFFFFFFFF) >> 8))) ^ v5)
            store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v5 ^ (v5 << 11)) & 0xFFFFFFFF) >> 8))) ^ v5))
            break
            break
        break
    v5 = load32(((v6 << 2) + 42120))
    v1 = (v4 + (v3 * 286704))
    v7 = (100 if (v3 != 1) else 0)
    store32((v4 + (v3 * 286704)) + 286688, (100 if (v3 != 1) else 0))
    store32(v1 + 286684, v7)
    store8(v1 + 283972, ((v5 & 0xFFFFFFFF) >> 16))
    store32(v1 + 283960, 3)
    store8((v1 + 283974), v5)
    store8((v1 + 283973), ((v5 & 0xFFFFFFFF) >> 8))
    while True:  # block $label5
        v1 = (v6 * 20)
        v5 = ((v6 * 20) - 60)
        if (u(((v6 * 20) - 60)) < u(load16u(9142944))):
            v7 = load32(9142928)
            store16(v2, load16u((load32(9142928) + (v5 << 1))))
            v1 = (v7 + (v1 << 1))
            store16(v2 + 2, load16u(((v7 + (v1 << 1)) - 118)))
            store16(v2 + 4, load16u((v1 - 116)))
            store16(v2 + 6, load16u((v1 - 114)))
            store16(v2 + 8, load16u((v1 - 112)))
            store16(v2 + 10, load16u((v1 - 110)))
            store16(v2 + 12, load16u((v1 - 108)))
            store16(v2 + 14, load16u((v1 - 106)))
            store16(v2 + 16, load16u((v1 - 104)))
            store16(v2 + 18, load16u((v1 - 102)))
            store16(v2 + 20, load16u((v1 - 100)))
            store16(v2 + 22, load16u((v1 - 98)))
            store16(v2 + 24, load16u((v1 - 96)))
            store16(v2 + 26, load16u((v1 - 94)))
            store16(v2 + 28, load16u((v1 - 92)))
            store16(v2 + 30, load16u((v1 - 90)))
            store16(v2 + 32, load16u((v1 - 88)))
            store16(v2 + 34, load16u((v1 - 86)))
            store16(v2 + 36, load16u((v1 - 84)))
            store16(v2 + 38, load16u((v1 - 82)))
            break
        break
    v1 = (v4 + (v3 * 286704))
    store32((v4 + (v3 * 286704)) + 284608, v3)
    store32(v1 + 283908, v3)
    store32(v1 + 283868, load32(9561460))
    # TODO: memory.copy []
    v2 = load32(9142424)
    store32((v1 + 284000), load32(load32(9142424) + 40))
    store32((v1 + 284136), load32(v2 + 36))
    if (u(v6) >= u(3)):
        store32(v1 + 283848, load32((v4 + 570552)))
        store32((v1 + 283852), load32((v4 + 570556)))
        store32((v1 + 283856), load32((v4 + 570560)))
        store32((v1 + 283860), load32((v4 + 570564)))
    v3 = load32(9142892)
    if load32(9142892):
        v2 = load32(9561692)
        v5 = 0
        while True:  # $label10
            v1 = (v2 + (v5 * 286704))
            if load32((v2 + (v5 * 286704)) + 281800):
                v2 = (-1 if (u(v3) > u(1073741823)) else (v3 << 2))
                v4 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                # TODO: memory.fill []
                v10 = (v1 + 281800)
                v1 = load32((v1 + 281800))
                while True:  # block $label9
                    while True:  # block $label7
                        v7 = (v3 - 1)
                        if (v3 - 1):
                            v9 = 0
                            v2 = 0
                            if (u((v3 - 2)) >= u(3)):
                                v11 = (v7 & -4)
                                v6 = 0
                                while True:  # $label6
                                    v3 = (v2 << 2)
                                    store32((v4 + (v2 << 2)), load32((v1 + v3)))
                                    v8 = (v3 | 4)
                                    store32((v4 + (v3 | 4)), load32((v1 + v8)))
                                    v8 = (v3 | 8)
                                    store32((v4 + (v3 | 8)), load32((v1 + v8)))
                                    v3 = (v3 | 12)
                                    store32((v4 + (v3 | 12)), load32((v1 + v3)))
                                    v2 = (v2 + 4)
                                    v6 = (v6 + 4)
                                    if ((v6 + 4) != v11):
                                        continue
                                    break
                            v3 = (v7 & 3)
                            if ((v7 & 3) == 0):
                                break
                            while True:  # $label8
                                v6 = (v2 << 2)
                                store32((v4 + (v2 << 2)), load32((v1 + v6)))
                                v2 = (v2 + 1)
                                v9 = (v9 + 1)
                                if ((v9 + 1) != v3):
                                    continue
                                break
                            break
                        if (v1 == 0):
                            break
                        break
                    v3 = load32(9142892)
                    break
                store32(v10, v4)
                v2 = load32(9561692)
            v5 = (v5 + 1)
            if (u((v5 + 1)) < u(v3)):
                continue
            break
    if (arg0 != 5):
    func284(0)
    return 0

# ------------------------------------------------------------
# $Rc
# Export: Rc
# ------------------------------------------------------------
def Rc(arg0):
    """Exported as Rc."""
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = load32(9671128)
    if (load8u(9142917) == 0):
        v2 = (v3 + (arg0 * 132))
        v4 = load32((v3 + (arg0 * 132)) + 36)
        v2 = (v3 + ((load32((v3 + (arg0 * 132)) + 36) if v4 else load32(v2 + 28)) * 132))
        v4 = ((load8u((v3 + ((load32((v3 + (arg0 * 132)) + 36) if v4 else load32(v2 + 28)) * 132)) + 122) * 404) + 9568096)
        v5 = load32(((load8u((v3 + ((load32((v3 + (arg0 * 132)) + 36) if v4 else load32(v2 + 28)) * 132)) + 122) * 404) + 9568096) + 216)
        v6 = load16u(v2 + 112)
        store32(v1 + 36, (((load32(v4 + 220) << 4) & 2147483632) + (load16u(v2 + 114) << 5)))
        store32(v1 + 32, (((v5 << 4) & 2147483632) + (v6 << 5)))
    while True:  # block $label0
        arg0 = load32((v3 + (arg0 * 132)) + 40)
        if (load32((v3 + (arg0 * 132)) + 40) == 0):
            break
        if load8u(9142916):
            store32(v1 + 20, arg0)
            store32(v1 + 16, -65281)
            a_b()
            break
        store32(v1 + 4, arg0)
        store32(v1, 13)
        a_b()
        break
    G.global0 = (v1 + 48)

# ------------------------------------------------------------
# $Ca
# Export: Ca
# ------------------------------------------------------------
def Ca(arg0):
    """Exported as Ca."""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v1 + 12, arg0)
    func71(21, 0, 0, (v1 + 12), 1, 0)
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $Db
# Export: Db
# ------------------------------------------------------------
def Db(arg0):
    """Exported as Db."""
    store32(9563944, arg0)
    return 9563904

# ------------------------------------------------------------
# $Aa
# Export: Aa
# ------------------------------------------------------------
def Aa(arg0, arg1):
    """Exported as Aa."""
    while True:  # block $label0
        v3 = (arg0 + arg1)
        if ((arg0 + arg1) == 0):
            break
        v4 = load8u(9147212)
        if (u(v3) >= u(load32((9142892 if load8u(9147212) else 41092)))):
            break
        v2 = load32(9561692)
        arg1 = (load32(9561692) + (arg0 * 286704))
        v5 = load32((load32(9561692) + (arg0 * 286704)) + 284616)
        v6 = load16u(arg1 + 38)
        v7 = load16u(arg1 + 36)
        v8 = load16u(arg1 + 34)
        v9 = load16u(arg1 + 32)
        v10 = load16u(arg1 + 30)
        v11 = load16u(arg1 + 28)
        v12 = load16u(arg1 + 26)
        v13 = load16u(arg1 + 24)
        v14 = load16u(arg1 + 22)
        v15 = load16u(arg1 + 20)
        v16 = load16u(arg1 + 18)
        v17 = load16u(arg1 + 16)
        v18 = load16u(arg1 + 14)
        v19 = load16u(arg1 + 12)
        v20 = load16u(arg1 + 10)
        v21 = load16u(arg1 + 8)
        v22 = load16u(arg1 + 6)
        v23 = load16u(arg1 + 4)
        v24 = load16u(arg1 + 2)
        v25 = load16u(arg1)
        while True:  # block $label1
            if (v4 == 0):
                v4 = load32(arg1 + 286684)
                v26 = load32(arg1 + 284608)
                v27 = load32(arg1 + 283960)
                v28 = load16u(arg1 + 283972)
                v29 = load8u((arg1 + 283974))
                v31 = load64(arg1 + 40)
                v32 = load64(arg1 + 48)
                v33 = load64(arg1 + 56)
                v34 = load64((arg1 - -64))
                v35 = load64(arg1 + 72)
                v30 = (v3 * 286704)
                v2 = (v2 + (v3 * 286704))
                # TODO: memory.copy []
                store32(arg1 + 283908, arg0)
                store32(v2 + 284616, v5)
                store64(v2 + 72, v35)
                store64((v2 - -64), v34)
                store64(v2 + 56, v33)
                store64(v2 + 48, v32)
                store64(v2 + 40, v31)
                store16(v2 + 38, v6)
                store16(v2 + 36, v7)
                store16(v2 + 34, v8)
                store16(v2 + 32, v9)
                store16(v2 + 30, v10)
                store16(v2 + 28, v11)
                store16(v2 + 26, v12)
                store16(v2 + 24, v13)
                store16(v2 + 22, v14)
                store16(v2 + 20, v15)
                store16(v2 + 18, v16)
                store16(v2 + 16, v17)
                store16(v2 + 14, v18)
                store16(v2 + 12, v19)
                store16(v2 + 10, v20)
                store16(v2 + 8, v21)
                store16(v2 + 6, v22)
                store16(v2 + 4, v23)
                store16(v2 + 2, v24)
                store16(v2, v25)
                store8((v2 + 283974), v29)
                store16(v2 + 283972, v28)
                store32(v2 + 283960, v27)
                store32(v2 + 284608, v26)
                store32(v2 + 286684, v4)
                store32((load32(9561692) + v30) + 283908, v3)
                break
            v4 = (arg1 + 284616)
            arg0 = (v2 + (v3 * 286704))
            v2 = ((v2 + (v3 * 286704)) + 284616)
            while True:  # block $label2
                v3 = load32(arg0 + 284616)
                if load32(arg0 + 284616):
                    store16(arg1, load16u(arg0))
                    store16(arg1 + 2, load16u(arg0 + 2))
                    store16(arg1 + 4, load16u(arg0 + 4))
                    store16(arg1 + 6, load16u(arg0 + 6))
                    store16(arg1 + 8, load16u(arg0 + 8))
                    store16(arg1 + 10, load16u(arg0 + 10))
                    store16(arg1 + 12, load16u(arg0 + 12))
                    store16(arg1 + 14, load16u(arg0 + 14))
                    store16(arg1 + 16, load16u(arg0 + 16))
                    store16(arg1 + 18, load16u(arg0 + 18))
                    store16(arg1 + 20, load16u(arg0 + 20))
                    store16(arg1 + 22, load16u(arg0 + 22))
                    store16(arg1 + 24, load16u(arg0 + 24))
                    store16(arg1 + 26, load16u(arg0 + 26))
                    store16(arg1 + 28, load16u(arg0 + 28))
                    store16(arg1 + 30, load16u(arg0 + 30))
                    store16(arg1 + 32, load16u(arg0 + 32))
                    store16(arg1 + 34, load16u(arg0 + 34))
                    store16(arg1 + 36, load16u(arg0 + 36))
                    store16(arg1 + 38, load16u(arg0 + 38))
                    break
                store64(arg1 + 32, load64(arg1 + 72))
                store64(arg1 + 24, load64((arg1 - -64)))
                store64(arg1 + 16, load64(arg1 + 56))
                store64(arg1 + 8, load64(arg1 + 48))
                store64(arg1, load64(arg1 + 40))
                break
            store32(v4, v3)
            store32(v2, v5)
            store16(arg0 + 38, v6)
            store16(arg0 + 36, v7)
            store16(arg0 + 34, v8)
            store16(arg0 + 32, v9)
            store16(arg0 + 30, v10)
            store16(arg0 + 28, v11)
            store16(arg0 + 26, v12)
            store16(arg0 + 24, v13)
            store16(arg0 + 22, v14)
            store16(arg0 + 20, v15)
            store16(arg0 + 18, v16)
            store16(arg0 + 16, v17)
            store16(arg0 + 14, v18)
            store16(arg0 + 12, v19)
            store16(arg0 + 10, v20)
            store16(arg0 + 8, v21)
            store16(arg0 + 6, v22)
            store16(arg0 + 4, v23)
            store16(arg0 + 2, v24)
            store16(arg0, v25)
            break
        xa()
        break

# ------------------------------------------------------------
# $Nd
# Export: Nd
# ------------------------------------------------------------
def Nd(arg0):
    """Exported as Nd."""
    store8(9216068, arg0)
    if arg0:
        while True:  # $label0
            v1 = (v1 + 1)
            if ((v1 + 1) != 356):
                continue
            break

# ------------------------------------------------------------
# $Td
# Export: Td
# ------------------------------------------------------------
def Td():
    """Exported as Td."""
    while True:  # $label2
        while True:  # block $label1
            while True:  # block $label0
                v0 = ((v3 * 404) + 9568096)
                # br_table[load32(((v3 * 404) + 9568096) + 264)]
                break
                break
            if load8u(v0 + 354):
                break
            v6 = load32(v0 + 116)
            v7 = load32(v0 + 68)
            v8 = load32(v0 + 120)
            v9 = load32(v0 + 100)
            v4 = load32(v0 + 92)
            v10 = load32(v0 + 104)
            v11 = load32(v0 + 72)
            v12 = load32(v0 + 76)
            v5 = load32(v0 + 276)
            if load32(v0 + 276):
                # TODO: i32.div_u []
            else:
            v13 = 0
            v14 = load32(v0 + 224)
            v1 = ((v2 * 52) + 9147392)
            store32(((v2 * 52) + 9147392) + 48, load32(v0 + 260))
            store32(v1 + 44, v14)
            store32(v1 + 40, v13)
            store32(v1 + 36, v5)
            store32(v1 + 32, v6)
            store32(v1 + 28, v11)
            store32(v1 + 24, v12)
            store32(v1 + 20, v7)
            store32(v1 + 16, v8)
            store32(v1 + 12, v9)
            store32(v1 + 8, v4)
            store32(v1 + 4, v10)
            store32(v1, v3)
            v2 = (v2 + 1)
            break
        v3 = (v3 + 1)
        if ((v3 + 1) != 255):
            continue
        break
    return (v2 * 13)

# ------------------------------------------------------------
# $Ib
# Export: Ib
# ------------------------------------------------------------
def Ib(arg0, arg1, arg2):
    """Exported as Ib."""
    while True:  # block $label0
        arg0 = ((arg2 * 404) + 9568096)
        if (arg0 != load32(((arg2 * 404) + 9568096) + 196)):
            break
        if (load32(arg0 + 264) != arg1):
            break
        while True:  # block $label1
            arg0 = ((arg2 * 404) + 9568096)
            if (load32(((arg2 * 404) + 9568096) + 188) == 55):
                break
            if (load32(38528) == arg2):
                break
            if (load32(38768) != arg2):
                break
            break
        if load8u(arg0 + 378):
            break
        v3 = load32(((arg2 * 404) + 9568096) + 84)
        break
    return v3

# ------------------------------------------------------------
# $Jd
# Export: Jd
# ------------------------------------------------------------
def Jd(arg0, arg1):
    """Exported as Jd."""
    store32(9684808, arg1)
    store32(9684804, arg0)

# ------------------------------------------------------------
# $Yd
# Export: Yd
# ------------------------------------------------------------
def Yd():
    """Exported as Yd."""
    while True:  # $label1
        while True:  # block $label0
            v1 = ((v2 * 404) + 9568096)
            if (load32(((v2 * 404) + 9568096) + 264) != 3):
                break
            if (load32(v1 + 180) == 0):
                break
            v0 = ((load32(v1 + 236) + (v0 + load32(v1 + 244))) + 23)
            v6 = (v6 + 1)
            break
        v2 = (v2 + 1)
        if ((v2 + 1) != 255):
            continue
        break
    v1 = load32(9685864)
    if load32(9685864):
        store32(9685864, 0)
    v2 = (v6 * 23)
    v6 = func26((-1 if (u(v0) > u(1073741823)) else (v0 << 2)))
    store32(9685864, func26((-1 if (u(v0) > u(1073741823)) else (v0 << 2))))
    while True:  # $label12
        while True:  # block $label2
            v1 = ((v11 * 404) + 9568096)
            if (load32(((v11 * 404) + 9568096) + 264) != 3):
                break
            if (load32(v1 + 180) == 0):
                break
            v19 = load64(v1 + 72)
            v8 = load32(v1 + 112)
            v7 = load32(v1 + 120)
            v9 = load32(v1 + 100)
            v10 = load32(v1 + 92)
            v12 = load32(v1 + 104)
            v14 = load32(v1 + 212)
            v15 = load8u(v1 + 354)
            v5 = load32(v1 + 236)
            v16 = load32(v1 + 80)
            v4 = load32(v1 + 244)
            v17 = load32(v1 + 116)
            v18 = load32(v1 + 68)
            v0 = (v6 + (v13 * 92))
            while True:  # block $label3
                v3 = load32(v1 + 368)
                if (load32(v1 + 368) == 60):
                    break
                if (v3 == 61):
                    break
                if (v3 == 63):
                    break
                if (v3 == 62):
                    break
                if (v3 == 55):
                    break
                break
            store32((v6 + (v13 * 92)) + 4, (6 if v3 else 5))
            store32(v0 + 8, v18)
            store32(v0 + 12, v17)
            store32(v0 + 16, v4)
            store32(v0 + 28, v16)
            store32(v0 + 32, v5)
            store32(v0 + 36, v15)
            store32(v0 + 40, v14)
            store32(v0 + 44, v12)
            store32(v0 + 48, v10)
            store32(v0 + 52, v9)
            store32(v0 + 56, v7)
            store64(v0 + 64, 0)
            store32(v0 + 60, v8)
            store64(v0 + 20, v19)
            store64(v0 + 72, 0)
            store64(v0 + 80, 0)
            store32(v0 + 88, 0)
            store32(v0, v11)
            while True:  # block $label4
                if (v4 == 0):
                    break
                v10 = (v4 & 3)
                v3 = load32(v1 + 240)
                v8 = 0
                while True:  # block $label5
                    if (u(v4) < u(4)):
                        v0 = 0
                        break
                    v12 = (v4 & -4)
                    v0 = 0
                    v4 = 0
                    while True:  # $label6
                        v7 = (v6 + (v2 << 2))
                        v9 = (v0 << 2)
                        store32((v6 + (v2 << 2)), load32((v3 + (v0 << 2))))
                        store32(v7 + 4, load32((v3 + (v9 | 4))))
                        store32(v7 + 8, load32((v3 + (v9 | 8))))
                        store32(v7 + 12, load32((v3 + (v9 | 12))))
                        v0 = (v0 + 4)
                        v2 = (v2 + 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v12):
                            continue
                        break
                    break
                if (v10 == 0):
                    break
                while True:  # $label7
                    store32((v6 + (v2 << 2)), load32((v3 + (v0 << 2))))
                    v0 = (v0 + 1)
                    v2 = (v2 + 1)
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v10):
                        continue
                    break
                break
            while True:  # block $label8
                if (v5 == 0):
                    break
                v7 = (v5 & 3)
                v1 = load32(v1 + 232)
                v8 = 0
                while True:  # block $label9
                    if (u(v5) < u(4)):
                        v0 = 0
                        break
                    v9 = (v5 & -4)
                    v0 = 0
                    v4 = 0
                    while True:  # $label10
                        v5 = (v6 + (v2 << 2))
                        v3 = (v0 << 2)
                        store32((v6 + (v2 << 2)), load32((v1 + (v0 << 2))))
                        store32(v5 + 4, load32((v1 + (v3 | 4))))
                        store32(v5 + 8, load32((v1 + (v3 | 8))))
                        store32(v5 + 12, load32((v1 + (v3 | 12))))
                        v0 = (v0 + 4)
                        v2 = (v2 + 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v9):
                            continue
                        break
                    break
                if (v7 == 0):
                    break
                while True:  # $label11
                    store32((v6 + (v2 << 2)), load32((v1 + (v0 << 2))))
                    v0 = (v0 + 1)
                    v2 = (v2 + 1)
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v7):
                        continue
                    break
                break
            v13 = (v13 + 1)
            break
        v11 = (v11 + 1)
        if ((v11 + 1) != 255):
            continue
        break
    return (v13 * 23)

# ------------------------------------------------------------
# $Gc
# Export: Gc
# ------------------------------------------------------------
def Gc(arg0, arg1):
    """Exported as Gc."""
    return load32(9215892)

# ------------------------------------------------------------
# $Gd
# Export: Gd
# ------------------------------------------------------------
def Gd(arg0):
    """Exported as Gd."""
    if (arg0 == 2147483647):
        arg0 = load32(load32(9568088) + 96)
        store32(load32(load32(9568088) + 96), load32(9147392))
        store32(arg0 + 4, load32(9147396))
        store32(arg0 + 8, load32(9147400))
        store32(arg0 + 12, load32(9147404))
        store32(arg0 + 16, load32(9147408))
        store32(arg0 + 20, load32(9147412))
        store32(arg0 + 24, load32(9147416))
        store32(arg0 + 28, load32(9147420))
        return
    func368(arg0)

# ------------------------------------------------------------
# $Le
# Export: Le
# ------------------------------------------------------------
def Le():
    """Exported as Le."""
    return load32(9687224)

# ------------------------------------------------------------
# $Va
# Export: Va
# ------------------------------------------------------------
def Va(arg0, arg1):
    """Exported as Va."""
    v4 = (arg0 * 20)
    v3 = func26((-1 if ((arg0 * 20) < 0) else (arg0 * 40)))
    store32(((arg1 << 2) + 9142928), func26((-1 if ((arg0 * 20) < 0) else (arg0 * 40))))
    if v4:
        arg0 = 0
        while True:  # $label0
            store16((v3 + (arg0 << 1)), load32(((arg0 << 2) + 9147392)))
            v2 = (arg0 | 1)
            store16((v3 + ((arg0 | 1) << 1)), load32(((v2 << 2) + 9147392)))
            v2 = (arg0 | 2)
            store16((v3 + ((arg0 | 2) << 1)), load32(((v2 << 2) + 9147392)))
            v2 = (arg0 | 3)
            store16((v3 + ((arg0 | 3) << 1)), load32(((v2 << 2) + 9147392)))
            arg0 = (arg0 + 4)
            if ((arg0 + 4) != v4):
                continue
            break
    store16(((arg1 << 1) + 9142944), v4)

# ------------------------------------------------------------
# $E
# Export: E
# ------------------------------------------------------------
def E(arg0):
    """Exported as E."""
    store8(9147336, arg0)

# ------------------------------------------------------------
# $Wa
# Export: Wa
# ------------------------------------------------------------
def Wa(arg0, arg1, arg2):
    """Exported as Wa."""
    store8(9143020, arg1)
    store32(9671160, arg0)
    store32(42160, arg2)

# ------------------------------------------------------------
# $Rb
# Export: Rb
# ------------------------------------------------------------
def Rb():
    """Exported as Rb."""
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # block $label0
        if (u(load32(9142892)) < u(2)):
            break
        v3 = load32(9561692)
        v1 = 1
        while True:  # $label1
            v0 = (v3 + (v1 * 286704))
            v4 = func88(v0)
            store32((v3 + (v1 * 286704)) + 283884, func88(v0))
            store32(v0 + 283892, v4)
            v1 = (v1 + 1)
            v0 = load32(9142892)
            if (u((v1 + 1)) < u(load32(9142892))):
                continue
            break
        if (u(v0) < u(2)):
            break
        v4 = 1
        while True:  # $label4
            v0 = (v3 + (v4 * 286704))
            store32((v3 + (v4 * 286704)) + 283944, 1)
            v1 = load32(9142892)
            if (u(load32(9142892)) >= u(2)):
                v5 = (v0 + 283944)
                v7 = (v0 + 283884)
                v6 = 1
                v0 = 1
                while True:  # $label3
                    while True:  # block $label2
                        if (v0 == v4):
                            break
                        v9 = load32((v3 + (v0 * 286704)) + 283884)
                        v8 = load32(v7)
                        if (u(load32((v3 + (v0 * 286704)) + 283884)) <= u(load32(v7))):
                            if (v8 != v9):
                                break
                            if (u(v0) <= u(v4)):
                                break
                        v6 = (v6 + 1)
                        store32(v5, (v6 + 1))
                        v1 = load32(9142892)
                        break
                    v0 = (v0 + 1)
                    if (u((v0 + 1)) < u(v1)):
                        continue
                    break
            v4 = (v4 + 1)
            if (u((v4 + 1)) < u(v1)):
                continue
            break
        if (u(v1) < u(2)):
            break
        v4 = 1
        while True:  # $label10
            v5 = load32(9561692)
            v0 = 1
            while True:  # block $label5
                if (u(v1) <= u(1)):
                    break
                while True:  # $label6
                    if (v4 == load32((v5 + (v0 * 286704)) + 283944)):
                        break
                    v0 = (v0 + 1)
                    if ((v0 + 1) != v1):
                        continue
                    break
                v0 = v1
                break
            v3 = (v5 + (v0 * 286704))
            while True:  # block $label7
                if load32(9147132):
                    if (load32(v3 + 284616) == 0):
                        break
                v6 = 0
                while True:  # block $label8
                    v7 = load32(9142872)
                    v9 = ((load32(9142872) * v1) + v0)
                    if (load8u((((load32(9142872) * v1) + v0) + load32(9143004))) == 0):
                        break
                    v6 = 1
                    v8 = load32(v3 + 281800)
                    if (load32(v3 + 281800) == 0):
                        break
                    v8 = load32((v8 + (v7 << 2)))
                    if (load32((v8 + (v7 << 2))) == 0):
                        break
                    v6 = (3 if (u(((load32(9142848) - v8) * 25)) < u(60000)) else 2)
                    break
                v5 = load32((v5 + (v7 * 286704)) + 281800)
                if load32((v5 + (v7 * 286704)) + 281800):
                    v6 = (4 if load32((v5 + (v0 << 2))) else v6)
                v8 = func88(v3)
                v12 = ((load8u((v3 + 283974)) | (load8u((v3 + 283973)) << 8)) | (load8u(v3 + 283972) << 16))
                v10 = load32(9143012)
                v1 = (v7 + (v0 * v1))
                v13 = load8u((load32(9143012) + (v7 + (v0 * v1))))
                v10 = load8u((v9 + v10))
                while True:  # block $label9
                    if load8u(9216060):
                        break
                    if load8u(v3 + 286696):
                        break
                    break
                v5 = (load8u(v3 + 286699) != 0)
                v14 = load32(v3 + 284628)
                v7 = load32(v3 + 284616)
                v15 = load32(v3 + 284608)
                v11 = load32(9143016)
                v16 = load8u((load32(9143016) + v1))
                v1 = load32(9143008)
                v17 = load8u((v1 + load32(9143008)))
                v11 = load8u((v9 + v11))
                v1 = load8u((v1 + v9))
                store32(v2 + 16, v10)
                store32(v2 + 20, v13)
                store32(v2 + 24, v5)
                store32(v2 + 28, v1)
                store32(v2 + 32, v6)
                store32(v2 + 40, v11)
                store32(v2 + 44, v0)
                store32(v2 + 48, v17)
                store32(v2 + 52, v16)
                store32(v2 + 56, v15)
                store32(v2 + 36, (v7 if v7 else v14))
                store32(v2, v4)
                store32(v2 + 4, v3)
                store32(v2 + 8, v8)
                store32(v2 + 12, v12)
                a_b()
                v1 = load32(9142892)
                break
            v4 = (v4 + 1)
            if (u((v4 + 1)) < u(v1)):
                continue
            break
        break
    G.global0 = (v2 - -64)
    return v2

# ------------------------------------------------------------
# $N
# Export: N
# ------------------------------------------------------------
def N(arg0, arg1):
    """Exported as N."""
    if (arg0 == 0):
        return (load8u(9147209) != 0)
    store8(9147209, arg1)
    arg0 = 0
    v2 = load32(9142892)
    v3 = (load32(9142892) * v2)
    v2 = func26((load32(9142892) * v2))
    # TODO: memory.fill []
    store32(9143012, v2)
    while True:  # block $label0
        if (v3 == 0):
            break
        v4 = load32(9143004)
        if (u(v3) >= u(4)):
            v7 = (v3 & -4)
            while True:  # $label1
                store8((arg0 + v2), (load8u((arg0 + v4)) ^ 1))
                v5 = (arg0 | 1)
                store8((v2 + (arg0 | 1)), (load8u((v4 + v5)) ^ 1))
                v5 = (arg0 | 2)
                store8((v2 + (arg0 | 2)), (load8u((v4 + v5)) ^ 1))
                v5 = (arg0 | 3)
                store8((v2 + (arg0 | 3)), (load8u((v4 + v5)) ^ 1))
                arg0 = (arg0 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v7):
                    continue
                break
        v3 = (v3 & 3)
        if ((v3 & 3) == 0):
            break
        v6 = 0
        while True:  # $label2
            store8((arg0 + v2), (load8u((arg0 + v4)) ^ 1))
            arg0 = (arg0 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v3):
                continue
            break
        break
    return arg1

# ------------------------------------------------------------
# $Tb
# Export: Tb
# ------------------------------------------------------------
def Tb(arg0, arg1, arg2, arg3, arg4):
    """Exported as Tb."""
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v5 + 16, arg4)
    store32(v5 + 12, arg3)
    store32(v5 + 8, arg2)
    store32(v5 + 4, arg1)
    store32(v5, arg0)
    while True:  # block $label0
        if load8u(9147210):
            func41(41, 0, 0, v5, 5)
            break
        # call_indirect[load32(9214152)]
        break
    G.global0 = (v5 + 32)

# ------------------------------------------------------------
# $Zc
# Export: Zc
# ------------------------------------------------------------
def Zc(arg0, arg1, arg2):
    """Exported as Zc."""
    v3 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    store32(9684428, arg1)
    v4 = load32((load32(9568076) + (12 if (arg1 != 1) else 0)))
    store32(9568084, arg0)
    arg0 = (v4 + (arg0 * 196))
    store32(9568088, (v4 + (arg0 * 196)))
    if (arg2 == 0):
        v11 = load64(arg0 + 4)
        v12 = load64(arg0 + 12)
        arg2 = load32(arg0 + 96)
        v4 = load8u(arg0 + 44)
        v5 = load8u(arg0 + 45)
        v6 = load32(arg0 + 104)
        v7 = load32(arg0 + 80)
        v8 = load32(arg0 + 88)
        v13 = load64(arg0 + 32)
        v9 = load32(arg0 + 40)
        v10 = load32(arg0)
        store32(v3 + 20, load32(arg0 + 28))
        store32(v3 + 24, v9)
        store64(v3 + 28, v13)
        store32(v3 + 36, v8)
        store32(v3 + 40, v7)
        store32(v3 + 44, v6)
        store32(v3 + 60, v5)
        store32(v3 + 56, v4)
        store32(v3 + 52, arg1)
        store32(v3 + 48, arg2)
        store64(v3 + 12, v12)
        store64(v3 + 4, v11)
        store32(v3, v10)
        a_b()
    G.global0 = (v3 - -64)

# ------------------------------------------------------------
# $Nc
# Export: Nc
# ------------------------------------------------------------
def Nc():
    """Exported as Nc."""
    v0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(9568064)
    if (load32(9568064) != load32(9568068)):
        while True:  # $label0
            v2 = (v2 + (v1 << 7))
            v3 = load32((v2 + (v1 << 7)) + 104)
            store32(v0 + 8, v1)
            store32(v0 + 4, v3)
            store32(v0, (v2 + 24))
            a_b()
            v1 = (v1 + 1)
            v2 = load32(9568064)
            if (u((v1 + 1)) < u(((load32(9568068) - load32(9568064)) >> 7))):
                continue
            break
    G.global0 = (v0 + 16)

# ------------------------------------------------------------
# $F
# Export: F
# ------------------------------------------------------------
def F(arg0):
    """Exported as F."""
    store32(40616, arg0)

# ------------------------------------------------------------
# $Xa
# Export: Xa
# ------------------------------------------------------------
def Xa(arg0, arg1):
    """Exported as Xa."""
    store32(9142956, arg1)
    store32(9142952, arg0)

# ------------------------------------------------------------
# $C
# Export: C
# ------------------------------------------------------------
def C(arg0):
    """Exported as C."""
    store32(9147312, arg0)
    store32(9147324, (arg0 ^ -1))
    store32(9147320, (arg0 ^ -1515870811))
    store32(9147316, (arg0 ^ 1515870810))

# ------------------------------------------------------------
# $Ic
# Export: Ic
# ------------------------------------------------------------
def Ic(arg0):
    """Exported as Ic."""
    while True:  # block $label0
        if (load32(9142892) == 0):
            break
        v1 = load32(9561692)
        if (load32(9561692) == 0):
            break
        break
    arg0 = (arg0 + 1)
    store32(9142892, (arg0 + 1))
    v2 = (i64(arg0) * 286704)
    arg0 = (-1 if i32(((v2 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(arg0) * 286704)))
    v1 = func26((-1 if i32(((v2 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(arg0) * 286704))))
    # TODO: memory.fill []
    store32(9561692, v1)

# ------------------------------------------------------------
# $Cb
# Export: Cb
# ------------------------------------------------------------
def Cb():
    """Exported as Cb."""
    v0 = (G.global0 - 192)
    G.global0 = (G.global0 - 192)
    store32(v0 + 128, load32(38468))
    store32(v0 + 132, load32(38476))
    store32(v0 + 136, load32(38524))
    store32(v0 + 140, load32(38488))
    store32(v0 + 144, load32(38484))
    store32(v0 + 148, load32(38464))
    store32(v0 + 152, load32(38520))
    store32(v0 + 156, load32(38516))
    store32(v0 + 160, load32(38512))
    store32(v0 + 164, load32(38552))
    store32(v0 + 168, load32(38480))
    store32(v0 + 172, load32(38536))
    store32(v0 + 176, load32(38540))
    store32(v0 + 180, load32(38544))
    store32(v0 + 184, load32(38532))
    store32(v0 + 64, load32(38668))
    store32(v0 + 68, load32(38820))
    store32(v0 + 72, load32(38800))
    store32(v0 + 76, load32(38848))
    store32(v0 + 80, load32(38840))
    store32(v0 + 84, load32(38836))
    store32(v0 + 88, load32(38808))
    store32(v0 + 92, load32(38844))
    store32(v0 + 96, load32(38792))
    store32(v0 + 100, load32(38816))
    store32(v0 + 104, load32(38784))
    store32(v0 + 108, load32(38804))
    store32(v0 + 112, load32(38812))
    store32(v0 + 116, load32(38780))
    store32(v0 + 120, load32(38824))
    store32(v0, load32(38664))
    store32(v0 + 4, load32(38700))
    store32(v0 + 8, load32(38876))
    store32(v0 + 12, load32(38916))
    store32(v0 + 16, load32(38908))
    store32(v0 + 20, load32(38904))
    store32(v0 + 24, load32(38884))
    store32(v0 + 28, load32(38912))
    store32(v0 + 32, load32(38868))
    store32(v0 + 36, load32(38892))
    store32(v0 + 40, load32(38860))
    store32(v0 + 44, load32(38880))
    store32(v0 + 48, load32(38888))
    store32(v0 + 52, load32(38856))
    store32(v0 + 56, load32(38896))
    func259((v0 + 128), 0)
    func259((v0 - -64), 1)
    func259(v0, 2)
    G.global0 = (v0 + 192)

# ------------------------------------------------------------
# $Lc
# Export: Lc
# ------------------------------------------------------------
def Lc(arg0):
    """Exported as Lc."""
    v1 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    store64(v1 + 8, 0)
    store64(v1 + 16, 0)
    store64(v1, 0)
    store64(v1 + 104, 4294967296)
    store64(v1 + 120, 0)
    store64(v1 + 112, 2147483648000)
    while True:  # block $label2
        while True:  # block $label0
            while True:  # block $label4
                v3 = load32(9568068)
                if (load32(9568068) != load32(9568072)):
                    store32(v3 + 8, 0)
                    store64(v3, 0)
                    v4 = load32(v1 + 4)
                    v2 = load32(v1)
                    v5 = (load32(v1 + 4) - load32(v1))
                    arg0 = ((load32(v1 + 4) - load32(v1)) // 196)
                    if (v2 != v4):
                        if (u(arg0) >= u(21913099)):
                            break
                        v2 = func26(v5)
                        store32(v3 + 4, func26(v5))
                        store32(v3, v2)
                        store32(v3 + 8, (v2 + (arg0 * 196)))
                        arg0 = load32(v1)
                        v4 = load32(v1 + 4)
                        if (load32(v1) != load32(v1 + 4)):
                            while True:  # $label1
                                # TODO: memory.copy []
                                v2 = (v2 + 196)
                                arg0 = (arg0 + 196)
                                if ((arg0 + 196) != v4):
                                    continue
                                break
                        store32(v3 + 4, v2)
                    store64(v3 + 12, 0)
                    store32(v3 + 20, 0)
                    v4 = load32(v1 + 16)
                    v2 = load32(v1 + 12)
                    v5 = (load32(v1 + 16) - load32(v1 + 12))
                    arg0 = ((load32(v1 + 16) - load32(v1 + 12)) // 196)
                    if (v2 != v4):
                        if (u(arg0) >= u(21913099)):
                            break
                        v2 = func26(v5)
                        store32(v3 + 16, func26(v5))
                        store32(v3 + 12, v2)
                        store32(v3 + 20, (v2 + (arg0 * 196)))
                        v4 = load32(v1 + 12)
                        v5 = load32(v1 + 16)
                        if (load32(v1 + 12) != load32(v1 + 16)):
                            arg0 = v4
                            while True:  # $label3
                                # TODO: memory.copy []
                                v2 = (v2 + 196)
                                arg0 = (arg0 + 196)
                                if ((arg0 + 196) != v5):
                                    continue
                                break
                        store32(v3 + 16, v2)
                    # TODO: memory.copy []
                    arg0 = (v3 + 128)
                    store32(9568068, (v3 + 128))
                    break
                arg0 = load32(9568068)
                v4 = load32(v1 + 12)
                break
            v3 = load32(9568064)
            if v4:
                store32(v1 + 16, v4)
            v4 = load32(v1)
            if load32(v1):
                store32(v1 + 4, v4)
            G.global0 = (v1 + 128)
            return (((arg0 - v3) >> 7) - 1)
            break
        func42()
        raise RuntimeError('unreachable')
        break
    func42()
    raise RuntimeError('unreachable')
    return af(v4)

# ------------------------------------------------------------
# $Ha
# Export: Ha
# ------------------------------------------------------------
def Ha():
    """Exported as Ha."""
    v0 = load32(9561692)
    if load32(9561692):
        store32(9561692, 0)
    store8(9147212, 0)
    store32(9142912, 0)
    store32(9142892, 0)

# ------------------------------------------------------------
# $Ad
# Export: Ad
# ------------------------------------------------------------
def Ad(arg0):
    """Exported as Ad."""
    v1 = load32(9568088)
    if (load32(load32(9568088) + 88) if arg0 else 1):
        return load32(v1 + 80)
    while True:  # $label1
        while True:  # block $label0
            v3 = load32(v1 + 88)
            if (load32(v1 + 88) != load32(v1 + 84)):
                v2 = load32(v1 + 80)
                break
            v2 = (load32(v1 + 92) + v3)
            store32(v1 + 84, (load32(v1 + 92) + v3))
            v4 = load32(v1 + 80)
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if v3:
                # TODO: memory.copy []
            if v4:
                v3 = load32(v1 + 88)
            store32(v1 + 80, v2)
            break
        store32(v1 + 88, (v3 + 1))
        store32((v2 + (v3 << 2)), 0)
        v5 = (v5 + 1)
        if ((v5 + 1) != arg0):
            continue
        break
    return v2

# ------------------------------------------------------------
# $Cd
# Export: Cd
# ------------------------------------------------------------
def Cd(arg0):
    """Exported as Cd."""
    v1 = load32(9568088)
    if (load32(load32(9568088) + 104) if arg0 else 1):
        return load32(v1 + 96)
    while True:  # $label1
        while True:  # block $label0
            v3 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v2 = load32(v1 + 96)
                break
            v2 = (load32(v1 + 108) + v3)
            store32(v1 + 100, (load32(v1 + 108) + v3))
            v4 = load32(v1 + 96)
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if v3:
                # TODO: memory.copy []
            if v4:
                v3 = load32(v1 + 104)
            store32(v1 + 96, v2)
            break
        store32(v1 + 104, (v3 + 1))
        store32((v2 + (v3 << 2)), 0)
        v5 = (v5 + 1)
        if ((v5 + 1) != arg0):
            continue
        break
    return v2

# ------------------------------------------------------------
# $Re
# Export: Re
# ------------------------------------------------------------
def Re(arg0):
    """Exported as Re."""
    v1 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    v1 = func26((arg0 + 4))
    store32(9687208, arg0)
    store32(9687204, v1)
    return v1

# ------------------------------------------------------------
# $Sa
# Export: Sa
# ------------------------------------------------------------
def Sa(arg0, arg1):
    """Exported as Sa."""
    v7 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label1
        while True:  # block $label0
            if (load8u(9147212) | load8u(9147210)):
                if (load32(9142892) == 0):
                    break
                store32(9142892, 0)
                v2 = load32(9561692)
                if load32(9561692):
                    store32(9561692, 0)
            v4 = load32(9142892)
            if load32(9142892):
                break
            break
        v4 = 6
        break
    v2 = 0
    arg0 = (arg0 + v4)
    v5 = (2 if (arg0 <= 2) else (arg0 + v4))
    store32(9142892, (2 if (arg0 <= 2) else (arg0 + v4)))
    arg0 = load32(9561692)
    v11 = (i64(v5) * 286704)
    v6 = (-1 if i32(((v11 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(v5) * 286704)))
    v3 = func26((-1 if i32(((v11 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(v5) * 286704))))
    # TODO: memory.fill []
    if arg0:
        v5 = (v5 if (u(v4) > u(v5)) else v4)
        v4 = ((v5 if (u(v4) > u(v5)) else v4) & 3)
        if (u((v5 - 1)) >= u(3)):
            v6 = (v5 & 2147483644)
            v5 = 0
            while True:  # $label2
                v8 = (v2 * 286704)
                # TODO: memory.copy []
                v8 = ((v2 | 1) * 286704)
                # TODO: memory.copy []
                v8 = ((v2 | 2) * 286704)
                # TODO: memory.copy []
                v8 = ((v2 | 3) * 286704)
                # TODO: memory.copy []
                v2 = (v2 + 4)
                v5 = (v5 + 4)
                if ((v5 + 4) != v6):
                    continue
                break
        if v4:
            v5 = 0
            while True:  # $label3
                v6 = (v2 * 286704)
                # TODO: memory.copy []
                v2 = (v2 + 1)
                v5 = (v5 + 1)
                if ((v5 + 1) != v4):
                    continue
                break
        v5 = load32(9142892)
    store32(9561692, v3)
    store32(v7 + 32, (v5 - 1))
    if (u(load32(9142892)) >= u(2)):
        arg0 = 1
        while True:  # $label10
            v2 = (load32(9561692) + (arg0 * 286704))
            v8 = ((load32(9561692) + (arg0 * 286704)) + 283908)
            while True:  # block $label4
                if load32(v2 + 283908):
                    v5 = (arg0 - 1)
                    v4 = load8u(v2 + 283972)
                    v6 = load8u((v2 + 283973))
                    v3 = load8u((v2 + 283974))
                    break
                store64(v2 + 283848, 1717986918800)
                v5 = (arg0 - 1)
                # TODO: i32.div_u []
                store32((arg0 - 1) + 284608, (3 + 1))
                store64((v2 + 283856), 1717986918800)
                while True:  # block $label5
                    if (u(arg0) <= u(1)):
                        store16(v2, load16u(9563904))
                        store16(v2 + 2, load16u(9563906))
                        store16(v2 + 4, load16u(9563908))
                        store16(v2 + 6, load16u(9563910))
                        store16(v2 + 8, load16u(9563912))
                        store16(v2 + 10, load16u(9563914))
                        store16(v2 + 12, load16u(9563916))
                        store16(v2 + 14, load16u(9563918))
                        store16(v2 + 16, load16u(9563920))
                        store16(v2 + 18, load16u(9563922))
                        store16(v2 + 20, load16u(9563924))
                        store16(v2 + 22, load16u(9563926))
                        store16(v2 + 24, load16u(9563928))
                        store16(v2 + 26, load16u(9563930))
                        store16(v2 + 28, load16u(9563932))
                        store16(v2 + 30, load16u(9563934))
                        store16(v2 + 32, load16u(9563936))
                        store16(v2 + 34, load16u(9563938))
                        store16(v2 + 36, load16u(9563940))
                        store16(v2 + 38, load16u(9563942))
                        v3 = load32(9563944)
                        if (u(arg1) >= u(3)):
                            break
                        store32(v2 + 283960, arg1)
                        break
                    v11 = load64(9147316)
                    v3 = load32(9147312)
                    store32(9147316, load32(9147312))
                    v4 = load32(9147324)
                    store64(9147320, v11)
                    v4 = (v4 ^ (v4 << 11))
                    v3 = ((v3 ^ (((v3 & 0xFFFFFFFF) >> 19) ^ (((v4 ^ (v4 << 11)) & 0xFFFFFFFF) >> 8))) ^ v4)
                    store32(9147312, ((v3 ^ (((v3 & 0xFFFFFFFF) >> 19) ^ (((v4 ^ (v4 << 11)) & 0xFFFFFFFF) >> 8))) ^ v4))
                    store32(v2 + 283960, (v3 % 3))
                    v6 = (v2 + 283960)
                    while True:  # block $label6
                        if (u(arg0) <= u(8)):
                            break
                        v11 = load64(9147316)
                        v3 = load32(9147312)
                        store32(9147316, load32(9147312))
                        v4 = load32(9147324)
                        store64(9147320, v11)
                        v4 = (v4 ^ (v4 << 11))
                        v3 = ((v3 ^ (((v3 & 0xFFFFFFFF) >> 19) ^ (((v4 ^ (v4 << 11)) & 0xFFFFFFFF) >> 8))) ^ v4)
                        store32(9147312, ((v3 ^ (((v3 & 0xFFFFFFFF) >> 19) ^ (((v4 ^ (v4 << 11)) & 0xFFFFFFFF) >> 8))) ^ v4))
                        break
                    v3 = (v3 % 16777215)
                    while True:  # block $label9
                        while True:  # block $label8
                            while True:  # block $label7
                                # br_table[load32(v6)]
                                break
                                break
                            store32(v2 + 283964, load32(((((load32(9561840) + v3) & 31) << 2) + 1472)))
                            break
                            break
                        store32(v2 + 283964, load32(((((load32(9561840) + v3) % 15) << 2) + 1600)))
                        break
                        break
                    store32(v2 + 283964, load32(((((load32(9561840) + v3) % 17) << 2) + 1664)))
                    break
                v4 = ((v3 & 0xFFFFFFFF) >> 16)
                store8(v2 + 283972, ((v3 & 0xFFFFFFFF) >> 16))
                store8((v2 + 283974), v3)
                v6 = ((v3 & 0xFFFFFFFF) >> 8)
                store8((v2 + 283973), ((v3 & 0xFFFFFFFF) >> 8))
                break
            v9 = load32(v2 + 284608)
            v10 = load32(v2 + 283960)
            store32(v7 + 16, v5)
            store32(v7 + 8, v10)
            store32(v7 + 4, v9)
            store32(v7, v2)
            store32(v7 + 12, (((v3 & 255) | ((v6 & 255) << 8)) | ((v4 & 255) << 16)))
            store32(v8, arg0)
            arg0 = (arg0 + 1)
            if (u((arg0 + 1)) < u(load32(9142892))):
                continue
            break
    G.global0 = (v7 + 48)
    return v7

# ------------------------------------------------------------
# $Eb
# Export: Eb
# ------------------------------------------------------------
def Eb():
    """Exported as Eb."""
    return load8u(9147212)

# ------------------------------------------------------------
# $Ae
# Export: Ae
# ------------------------------------------------------------
def Ae(arg0):
    """Exported as Ae."""
    if load8u(9142916):
        store32(9603804, 0)
        store32(9577140, 0)
        store32(9576736, 0)
        store32(9571080, 0)
    v1 = load8u(9147152)
    while True:  # block $label3
        while True:  # block $label1
            while True:  # block $label0
                if (load8u(9147212) == 0):
                    if v1:
                        break
                    break
                while True:  # block $label2
                    if load8u(9147210):
                        break
                    if load32(9142848):
                        break
                    store32(9147312, arg0)
                    store32(9147324, (arg0 ^ -1))
                    store32(9147320, (arg0 ^ -1515870811))
                    store32(9147316, (arg0 ^ 1515870810))
                    break
                if v1:
                    break
                break
                break
            v1 = 0
            store32(9142872, 1)
            v3 = load32(9142440)
            if (load32(9142440) * v3):
                while True:  # $label4
                    store8((load32(9147288) + v1), load32(9147292))
                    v1 = (v1 + 1)
                    v3 = load32(9142440)
                    if (u((v1 + 1)) < u((load32(9142440) * v3))):
                        continue
                    break
            store32(9147312, arg0)
            store32(9142892, 2)
            store32(9147324, (arg0 ^ -1))
            store32(9147320, (arg0 ^ -1515870811))
            store32(9147316, (arg0 ^ 1515870810))
            arg0 = load32(9561692)
            if load32(9561692):
            else:
            v5 = (i64(2) * 286704)
            v1 = (load32(9142892) if i32(((v5 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(2) * 286704)))
            arg0 = func26((load32(9142892) if i32(((v5 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64(2) * 286704))))
            # TODO: memory.fill []
            store32(9561692, arg0)
            store32((arg0 + 571312), 1)
            store32((arg0 + 286712), 6553701)
            store64((arg0 + 286704), 32088563964837972)
            store32((arg0 + 570612), 1)
            store32((arg0 + 570572), load32(9561460))
            # TODO: memory.copy []
            v1 = load32(9142424)
            store32((arg0 + 570704), load32(load32(9142424) + 40))
            store32((arg0 + 570840), load32(v1 + 36))
            v1 = load32(42128)
            store8((arg0 + 570678), load32(42128))
            store64((arg0 + 570560), 21474836485000)
            store64((arg0 + 570552), 21474836485000)
            store8((arg0 + 283974), 255)
            store16(arg0 + 283972, 65535)
            store8((arg0 + 570677), ((v1 & 0xFFFFFFFF) >> 8))
            store8((arg0 + 570676), ((v1 & 0xFFFFFFFF) >> 16))
            break
        v4 = (load8u(9147212) != 0)
        v1 = 0
        v3 = load32(9142892)
        store32(9142420, func26((-1 if (u(v3) > u(1073741823)) else (load32(9142892) << 2))))
        arg0 = load32(9142424)
        v2 = load32(load32(9142424) + 136)
        # TODO: i32.div_u []
        store32(1, (1 if (u(v2) <= u(99)) else (load32(load32(9142424) + 136) if load8u(9147210) else 100)))
        v2 = load32(arg0 + 140)
        store32(51760, (load32(arg0 + 140) * 1000))
        # TODO: f32.convert_i32_u []
        store32(9682176, v2)
        v2 = load32(arg0 + 144)
        store32(51764, (load32(arg0 + 144) * 1000))
        # TODO: f32.convert_i32_u []
        store32(9682180, v2)
        v2 = load32(arg0 + 148)
        store32(51768, (load32(arg0 + 148) * 1000))
        # TODO: f32.convert_i32_u []
        store32(9682184, v2)
        arg0 = load32(arg0 + 152)
        store32(51772, (load32(arg0 + 152) * 1000))
        # TODO: f32.convert_i32_u []
        store32(9682188, arg0)
        if v4:
            break
        if (v3 == 0):
            break
        while True:  # $label5
            func239(v1)
            v1 = (v1 + 1)
            if (u((v1 + 1)) < u(load32(9142892))):
                continue
            break
        break
    return 40592

# ------------------------------------------------------------
# $He
# Export: He
# ------------------------------------------------------------
def He():
    """Exported as He."""
    return load32(9147220)

# ------------------------------------------------------------
# $We
# Export: We
# ------------------------------------------------------------
def We():
    """Exported as We."""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v3 + 12, 0)
    func71(30, (v3 + 12), 1, 0, 0, 1)
    while True:  # block $label0
        v4 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v5 = load32(9561692)
        v1 = 1
        while True:  # $label2
            while True:  # block $label1
                v2 = (v5 + (v1 * 286704))
                v6 = load32((v5 + (v1 * 286704)) + 284616)
                if (load32((v5 + (v1 * 286704)) + 284616) == 0):
                    break
                if (load32(v2 + 284604) == 0):
                    break
                v7 = ((v0 << 2) + 8447808)
                store32(((v0 << 2) + 8447808), v6)
                store32(v7 + 4, load32((v2 + 284604)))
                v0 = (v0 + 2)
                break
            v1 = (v1 + 1)
            if ((v1 + 1) != v4):
                continue
            break
        if (v0 == 0):
            break
        func71(32, 8447808, v0, 0, 0, 1)
        v2 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v0 = load32(9561692)
        v1 = 1
        while True:  # $label4
            v4 = (v0 + (v1 * 286704))
            if (load8u((v0 + (v1 * 286704)) + 286699) == 0):
                v2 = load32(v4 + 284604)
                while True:  # block $label3
                    if (load8u(9147210) == 0):
                        break
                    if (load32(v4 + 284616) != load32(9561844)):
                        if (load32(9142872) != v1):
                            break
                        if (load8u(9142388) == 0):
                            break
                    v2 = 2147483647
                    break
                store32(v3 + 4, v2)
                store32(v3, v1)
                a_b()
                v2 = load32(9142892)
                v0 = load32(9561692)
            v1 = (v1 + 1)
            if (u((v1 + 1)) < u(v2)):
                continue
            break
        break
    G.global0 = (v3 + 16)

# ------------------------------------------------------------
# $Ve
# Export: Ve
# ------------------------------------------------------------
def Ve(arg0):
    """Exported as Ve."""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v4 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v5 = load32(9561692)
        v3 = 1
        v1 = 1
        while True:  # $label1
            v6 = (v5 + (v1 * 286704))
            v7 = load32((v5 + (v1 * 286704)) + 284616)
            if (arg0 == load32(v6 + 284628)):
                if v7:
                    break
                store32((v6 + 284616), arg0)
                arg0 = (v5 + (v1 * 286704))
                store8((v5 + (v1 * 286704)) + 286699, 0)
                v1 = load32(arg0 + 283908)
                arg0 = load8u(arg0 + 286696)
                store32(v2 + 8, 0)
                store32(v2 + 4, arg0)
                store32(v2, v1)
                a_b()
                break
            if (arg0 == v7):
                break
            v1 = (v1 + 1)
            v3 = (u((v1 + 1)) < u(v4))
            if (v1 != v4):
                continue
            break
        break
    G.global0 = (v2 + 16)
    return v3

# ------------------------------------------------------------
# $Rd
# Export: Rd
# ------------------------------------------------------------
def Rd(arg0, arg1):
    """Exported as Rd."""
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    if (load8u(9216068) == 0):
        arg1 = load32(((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096) + 196)
    while True:  # block $label0
        v2 = ((arg0 * 132) + 9216080)
        if (load8u(((arg0 * 132) + 9216080) + 23) == 0):
            v5 = 1
            v7 = 2147483647
            break
        v5 = 1
        while True:  # block $label1
            v7 = load32(v2 + 4)
            v4 = ((load32(v2 + 4) * 404) + 9568096)
            if (load32(((load32(v2 + 4) * 404) + 9568096) + 264) == 3):
                break
            arg0 = load32(v4 + 196)
            if (load32(v4 + 196) == arg1):
                break
            if (u(arg0) > u(2)):
                break
            v5 = (load32(9147132) != 0)
            break
        v6 = load32(v4 + 144)
        v8 = load32(v4 + 88)
        v5 = ((load8u(v4 + 354) == 0) & v5)
        break
    arg1 = load32(v4 + 84)
    arg0 = load32(v2 + 8)
    while True:  # block $label2
        v2 = load32(v2)
        if (load32(v2) == 5):
            break
        if (v2 == 12):
            break
        if (v2 == 7):
            break
        break
    v4 = (3 if (v2 == 15) else (3 if (v2 == 1) else (3 if (v2 == 16) else -1)))
    store32(v3 + 28, v5)
    store32(v3 + 24, v7)
    store32(v3 + 20, v4)
    store32(v3 + 16, (0 - v6))
    store32(v3 + 8, v8)
    store32(v3 + 4, arg1)
    store32(v3, arg0)
    store32(v3 + 12, (v2 == 2))
    G.global0 = (v3 + 32)
    return v3

# ------------------------------------------------------------
# $Ja
# Export: Ja
# ------------------------------------------------------------
def Ja():
    """Exported as Ja."""
    return (load32(41092) - 1)

# ------------------------------------------------------------
# $Ea
# Export: Ea
# ------------------------------------------------------------
def Ea(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
    """Exported as Ea."""
    if arg6:
        while True:  # block $label0
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg4 = load32(9561784)
                break
            arg1 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg0 = load32(9561784)
            arg4 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
            if arg6:
                # TODO: memory.copy []
            if arg0:
                arg6 = load32(9561792)
            store32(9561784, arg4)
            break
        store32(9561792, (arg6 + 1))
        store32((arg4 + (arg6 << 2)), arg3)
        arg1 = (load32(59176) + 10)
        while True:  # block $label1
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg3 = arg4
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg3 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy []
            store32(9561784, arg3)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg3 + (arg6 << 2)), arg1)
        while True:  # block $label2
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg4 = arg3
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg4 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy []
            store32(9561784, arg4)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg4 + (arg6 << 2)), arg5)
        while True:  # block $label3
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg3 = arg4
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg3 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy []
            store32(9561784, arg3)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg3 + (arg6 << 2)), arg2)
        while True:  # block $label4
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg4 = arg3
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg4 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy []
            store32(9561784, arg4)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg4 + (arg6 << 2)), arg8)
        while True:  # block $label5
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg3 = arg4
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg3 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy []
            store32(9561784, arg3)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg3 + (arg6 << 2)), arg7)
        while True:  # block $label6
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg4 = arg3
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg4 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy []
            store32(9561784, arg4)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg4 + (arg6 << 2)), arg9)
        while True:  # block $label7
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg3 = arg4
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg3 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy []
            store32(9561784, arg3)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg3 + (arg6 << 2)), arg10)
        return 0
    arg6 = 0
    if (load8u(9561832) == 0):
        v13 = load32(9561692)
        v14 = (arg11 + 1)
        arg11 = ((arg11 + 1) * 286704)
        arg6 = (load32(9561692) + ((arg11 + 1) * 286704))
        store32((load32(9561692) + ((arg11 + 1) * 286704)) + 283908, v14)
        v15 = load8u(9147212)
        store32(arg6 + 286684, ((load8u(9147212) == 0) & arg4))
        if (arg4 == 0):
            store32((arg11 + v13) + 284616, arg3)
        arg11 = (arg11 + v13)
        store32((arg11 + v13) + 283952, arg8)
        store32(arg11 + 283948, arg5)
        store32(arg11 + 284620, (arg12 + 1))
        store32(arg11 + 283964, arg9)
        store8(arg11 + 93, arg10)
        store8(arg11 + 92, arg7)
        while True:  # block $label8
            if (arg3 != load32(9142384)):
                if load8u(9147210):
                    break
                if arg4:
                    break
            store32(9142872, v14)
            break
        if (v15 == 0):
            arg3 = (v13 + (v14 * 286704))
            store32((v13 + (v14 * 286704)) + 284608, arg0)
            store32(arg3 + 283960, (arg1 if (u(arg1) <= u(4)) else 0))
            store8(arg3 + 283972, ((arg2 & 0xFFFFFFFF) >> 16))
            store8((arg3 + 283974), arg2)
            store8((arg3 + 283973), ((arg2 & 0xFFFFFFFF) >> 8))
        store32(41092, (load32(41092) + 1))
    return arg6

# ------------------------------------------------------------
# $G
# Export: G
# ------------------------------------------------------------
def G(arg0, arg1):
    """Exported as G."""
    v2 = load32(9142440)
    return ((u(load32(9142440)) > u(arg1)) & ((u(arg0) < u(v2)) & ((arg0 | arg1) >= 0)))

# ------------------------------------------------------------
# $Jc
# Export: Jc
# ------------------------------------------------------------
def Jc():
    """Exported as Jc."""
    return load32(9142892)

# ------------------------------------------------------------
# $Me
# Export: Me
# ------------------------------------------------------------
def Me():
    """Exported as Me."""
    return load32(9687216)

# ------------------------------------------------------------
# $Ia
# Export: Ia
# ------------------------------------------------------------
def Ia():
    """Exported as Ia."""
    while True:  # block $label0
        if load8u(9147212):
            break
        v1 = load32(41092)
        if (u(load32(41092)) < u(2)):
            break
        v0 = (v1 - 1)
        v3 = ((v1 - 1) & 3)
        v5 = load32(9561692)
        while True:  # block $label1
            if (u((v1 - 2)) < u(3)):
                v1 = 1
                v0 = 0
                break
            v7 = (v0 & -4)
            v0 = 0
            v1 = 1
            while True:  # $label2
                v2 = (v5 + (v1 * 286704))
                v0 = ((((v0 + (load32((v5 + (v1 * 286704)) + 284616) == 0)) + (load32((v2 + 571320)) == 0)) + (load32((v2 + 858024)) == 0)) + (load32((v2 + 1144728)) == 0))
                v1 = (v1 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v7):
                    continue
                break
            break
        if (v3 == 0):
            break
        while True:  # $label3
            v0 = (v0 + (load32((v5 + (v1 * 286704)) + 284616) == 0))
            v1 = (v1 + 1)
            v4 = (v4 + 1)
            if ((v4 + 1) != v3):
                continue
            break
        break
    return v0

# ------------------------------------------------------------
# $Pb
# Export: Pb
# ------------------------------------------------------------
def Pb():
    """Exported as Pb."""
    return load32(9142872)

# ------------------------------------------------------------
# $Od
# Export: Od
# ------------------------------------------------------------
def Od(arg0):
    """Exported as Od."""
    if load8u(9147141):

# ------------------------------------------------------------
# $Qd
# Export: Qd
# ------------------------------------------------------------
def Qd(arg0):
    """Exported as Qd."""
    arg0 = ((load32(9143000) * load32(9147120)) + arg0)
    while True:  # block $label0
        if load8u(9147141):
            v1 = load32((load32(9671128) + (load32(9173808) * 132)) + 16)
            if (load32((load32(9671128) + (load32(9173808) * 132)) + 16) == 0):
                break
            if (u(arg0) >= u(load32(v1 + 8))):
                break
            return
        if (u(arg0) >= u(load32(9671120))):
            break
        if load32(9681836):
            return
        v1 = (load32(9671128) + (load32(9173808) * 132))
        v3 = load16u((load32(9671128) + (load32(9173808) * 132)) + 110)
        v4 = load32(load32(((arg0 << 2) + 9263072)) + 12)
        v1 = load8u(v1 + 122)
        v5 = load32(((load8u(v1 + 122) * 404) + 9568096) + 196)
        v2 = 1
        while True:  # block $label1
            if (load32(38540) == v1):
                break
            if (load32(38812) == v1):
                break
            v2 = (load32(38888) == v1)
            break
        break

# ------------------------------------------------------------
# $Id
# Export: Id
# ------------------------------------------------------------
def Id(arg0, arg1, arg2):
    """Exported as Id."""
    v3 = (G.global0 - 144)
    G.global0 = (G.global0 - 144)
    while True:  # block $label0
        if load8u(9684432):
            break
        store32(9142900, arg2)
        store8(9142409, 1)
        while True:  # block $label1
            v14 = load32(40616)
            # TODO: f32.convert_i32_u []
            v15 = load32(9142856)
            v15 = load32(9671164)
            v16 = (((load32(40616) * float(arg0)) + float(load32(9142952))) + ((load32(9142856) - ((v14 * v15) / load32(9671164))) * 0.5))
            if (abs((((load32(40616) * float(arg0)) + float(load32(9142952))) + ((load32(9142856) - ((v14 * v15) / load32(9671164))) * 0.5))) < 2147483650.0):
                break
            break
        arg0 = -2147483648
        store32(int(v16), -2147483648)
        while True:  # block $label2
            # TODO: f32.convert_i32_u []
            v16 = load32(9142860)
            v14 = (((load32(9142860) - ((v14 * v16) / v15)) * 0.5) + ((v14 * float(arg1)) + float(load32(9142956))))
            if (abs((((load32(9142860) - ((v14 * v16) / v15)) * 0.5) + ((v14 * float(arg1)) + float(load32(9142956))))) < 2147483650.0):
                break
            break
        arg1 = -2147483648
        store32(int(v14), -2147483648)
        v4 = load32(9684792)
        if (load32(9684792) == 0):
            break
        if (arg2 == 2):
            store32(9684792, 0)
            arg0 = load32(9684796)
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
        arg2 = load32(v4)
        v6 = (arg0 - load32(v4))
        v9 = load32(v4 + 8)
        arg0 = 0
        v5 = (load32(v4 + 20) * load32(v4 + 16))
        if (load32(v4 + 20) * load32(v4 + 16)):
        else:
        v10 = ((load32(v4 + 4) // v5) - 0)
        arg1 = (((load32(v4 + 4) // v5) - 0) // 32)
        v11 = load32(v4 + 12)
        while True:  # block $label6
            arg0 = (v6 // 32)
            v7 = ((arg0 + (arg2 // 32)) + ((arg2 & 31) != 0))
            if ((v6 // 32) < ((arg0 + (arg2 // 32)) + ((arg2 & 31) != 0))):
                arg2 = (load32(v4 + 4) // v5)
                arg2 = ((((load32(v4 + 4) // v5) // 32) + arg1) + ((arg2 & 31) != 0))
                v12 = (arg1 if (arg1 > arg2) else ((((load32(v4 + 4) // v5) // 32) + arg1) + ((arg2 & 31) != 0)))
                v5 = (load32(9142440) + 2)
                v13 = load32(9142840)
                while True:  # $label5
                    arg0 = (arg0 + 1)
                    arg2 = arg1
                    while True:  # block $label4
                        while True:  # $label3
                            if (arg2 != v12):
                                arg2 = (arg2 + 1)
                                if (load32((v13 + (((((arg2 + 1) + v5) * v5) + arg0) << 2))) != 1):
                                    continue
                                break
                            break
                        v8 = (arg0 >= v7)
                        if (arg0 != v7):
                            continue
                        break
                    break
                if (v8 == 0):
                    break
            arg0 = (v6 + v9)
            arg1 = (v10 + v11)
            func216(load32(9681936), load32(v4 + 52), (v6 + v9), (v10 + v11), func370(v4, arg0, arg1))
            arg0 = load32(9684796)
            if load8u(9142916):
                store32(v3 + 128, arg0)
                a_b()
                break
            store32(v3 + 120, arg0)
            store64(v3 + 112, -4602115869219225600)
            store64(v3 + 104, 0)
            store64(v3 + 96, 0)
            a_b()
            break
        if load8u(9163792):
            break
        store32(9684792, 0)
        arg0 = load32(9684796)
        if load8u(9142916):
            store32(v3 + 80, arg0)
            a_b()
            break
        store32(v3 + 72, arg0)
        store64((v3 - -64), -4602115869219225600)
        store64(v3 + 56, 0)
        store64(v3 + 48, 0)
        a_b()
        break
    G.global0 = (v3 + 144)
    return (v3 + 48)

# ------------------------------------------------------------
# $Ee
# Export: Ee
# ------------------------------------------------------------
def Ee(arg0):
    """Exported as Ee."""
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v1 = 9143012
    if (u(arg0) <= u(2)):
        v1 = load32(((arg0 << 2) + 10284))
    v3 = 1
    v2 = load32(9142892)
    if (u(load32(9142892)) > u(1)):
        v6 = load32(v1)
        while True:  # $label3
            v8 = (load32(9561692) + (v3 * 286704))
            while True:  # block $label0
                if (u(v2) < u(2)):
                    break
                v4 = (v2 - 1)
                v9 = ((v2 - 1) & 3)
                v1 = 1
                if (u((v2 - 2)) >= u(3)):
                    v10 = (v4 & -4)
                    v4 = 0
                    while True:  # $label1
                        store32(((v1 << 2) + 9147392), load8u((v6 + ((v1 * v2) + v3))))
                        v7 = (v1 + 1)
                        store32((((v1 + 1) << 2) + 9147392), load8u((v6 + ((v2 * v7) + v3))))
                        v7 = (v1 + 2)
                        store32((((v1 + 2) << 2) + 9147392), load8u((v6 + ((v2 * v7) + v3))))
                        v7 = (v1 + 3)
                        store32((((v1 + 3) << 2) + 9147392), load8u((v6 + ((v2 * v7) + v3))))
                        v1 = (v1 + 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v10):
                            continue
                        break
                v4 = 0
                if (v9 == 0):
                    break
                while True:  # $label2
                    store32(((v1 << 2) + 9147392), load8u((v6 + ((v1 * v2) + v3))))
                    v1 = (v1 + 1)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v9):
                        continue
                    break
                break
            v1 = load8u(v8 + 283972)
            v2 = load8u((v8 + 283974))
            v4 = load8u((v8 + 283973))
            store32(v5 + 12, arg0)
            store32(v5 + 4, v8)
            store32(v5, v3)
            store32(v5 + 8, ((v2 | (v4 << 8)) | (v1 << 16)))
            v3 = (v3 + 1)
            v2 = load32(9142892)
            if (u((v3 + 1)) < u(load32(9142892))):
                continue
            break
    G.global0 = (v5 + 16)

# ------------------------------------------------------------
# $Fd
# Export: Fd
# ------------------------------------------------------------
def Fd(arg0):
    """Exported as Fd."""
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    store32(40600, arg0)
    while True:  # block $label0
        if (arg0 == 0):
            arg0 = load32(9142884)
            if load8u(9142916):
                store32(v1 + 32, arg0)
                a_b()
                break
            store32(v1 + 24, arg0)
            store64(v1 + 16, -4602115869219225600)
            store64(v1 + 8, 0)
            store64(v1, 0)
            a_b()
            break
        break
    G.global0 = (v1 + 48)

# ------------------------------------------------------------
# $Wd
# Export: Wd
# ------------------------------------------------------------
def Wd():
    """Exported as Wd."""
    while True:  # $label3
        while True:  # block $label1
            while True:  # block $label0
                v3 = ((v1 * 404) + 9568096)
                # br_table[load32(((v1 * 404) + 9568096) + 264)]
                break
                break
            v2 = ((load32(v3 + 364) + (v2 + load32(v3 + 236))) + 60)
            v3 = 0
            while True:  # $label2
                v2 = (((v1 * 1020) + 9299904) + (v3 << 2))
                v5 = (v2 if (load32((((v1 * 1020) + 9299904) + (v3 << 2))) == 100) else (v2 + 2))
                v5 = ((v2 if (load32((((v1 * 1020) + 9299904) + (v3 << 2))) == 100) else (v2 + 2)) if (load32(v2 + 4) == 100) else (v5 + 2))
                v2 = (((v2 if (load32((((v1 * 1020) + 9299904) + (v3 << 2))) == 100) else (v2 + 2)) if (load32(v2 + 4) == 100) else (v5 + 2)) if (load32(v2 + 8) == 100) else (v5 + 2))
                v3 = (v3 + 3)
                if ((v3 + 3) != 255):
                    continue
                break
            v0 = (v0 + 1)
            break
        v1 = (v1 + 1)
        if ((v1 + 1) != 255):
            continue
        break
    v1 = load32(9685864)
    if load32(9685864):
        store32(9685864, 0)
    v3 = (v0 * 60)
    v5 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
    store32(9685864, func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2))))
    while True:  # $label16
        while True:  # block $label5
            while True:  # block $label4
                v1 = ((v10 * 404) + 9568096)
                # br_table[load32(((v10 * 404) + 9568096) + 264)]
                break
                break
            v0 = 0
            v2 = 0
            while True:  # $label6
                v13 = ((v10 * 1020) + 9299904)
                v2 = (((v10 * 1020) + 9299904) + (v0 << 2))
                v4 = (v2 if (load32((((v10 * 1020) + 9299904) + (v0 << 2))) == 100) else (v2 + 2))
                v4 = ((v2 if (load32((((v10 * 1020) + 9299904) + (v0 << 2))) == 100) else (v2 + 2)) if (load32(v2 + 4) == 100) else (v4 + 2))
                v2 = (((v2 if (load32((((v10 * 1020) + 9299904) + (v0 << 2))) == 100) else (v2 + 2)) if (load32(v2 + 4) == 100) else (v4 + 2)) if (load32(v2 + 8) == 100) else (v4 + 2))
                v0 = (v0 + 3)
                if ((v0 + 3) != 255):
                    continue
                break
            v4 = load32(v1 + 104)
            v6 = load32(v1 + 92)
            v7 = load32(v1 + 100)
            v8 = load32(v1 + 68)
            v9 = load32(v1 + 72)
            v11 = load32(v1 + 76)
            v14 = load32(v1 + 80)
            v15 = load32(v1 + 120)
            v16 = load32(v1 + 116)
            v17 = load32(v1 + 276)
            v18 = load32(v1 + 96)
            v19 = load32(v1 + 224)
            v20 = load32(v1 + 260)
            v21 = load32(v1 + 204)
            v22 = load32(v1 + 200)
            v23 = load32(v1 + 236)
            v24 = load32(v1 + 228)
            v25 = load32(v1 + 208)
            v26 = load32(v1 + 216)
            v27 = load32(v1 + 192)
            v28 = load32(v1 + 188)
            v29 = load32(v1 + 84)
            v30 = load32(v1 + 136)
            v31 = load32(v1 + 140)
            v32 = load32(v1 + 176)
            v33 = load32(v1 + 364)
            v34 = load32(v1 + 272)
            v35 = load32(v1 + 212)
            v36 = load32(v1 + 124)
            v37 = load32(v1 + 280)
            v38 = load32(v1 + 328)
            v39 = load8u(v1 + 353)
            v40 = load8u(v1 + 335)
            v41 = load8u(v1 + 333)
            v42 = load8u(v1 + 334)
            v43 = load8u(v1 + 336)
            v55 = load64(v1 + 284)
            v56 = load64(v1 + 292)
            v44 = load32(v1 + 300)
            v45 = load32(v1 + 308)
            v46 = load32(v1 + 312)
            v47 = load32(v1 + 324)
            v48 = load32(v1 + 320)
            v49 = load32(v1 + 340)
            v50 = load32(v1 + 344)
            v51 = load32(v1 + 348)
            v52 = load32(v1 + 304)
            v53 = load32(v1 + 316)
            v54 = load8u(v1 + 352)
            v0 = (v5 + (v12 * 240))
            store32((v5 + (v12 * 240)) + 212, load8u(v1 + 354))
            store32(v0 + 208, v54)
            store32(v0 + 204, v53)
            store32(v0 + 200, v52)
            store32(v0 + 196, v51)
            store32(v0 + 192, v50)
            store32(v0 + 188, v49)
            store32(v0 + 184, v48)
            store32(v0 + 180, v47)
            store32(v0 + 176, v46)
            store32(v0 + 172, v45)
            store32(v0 + 168, v44)
            store64(v0 + 160, v56)
            store64(v0 + 152, v55)
            store32(v0 + 148, v43)
            store32(v0 + 144, v42)
            store32(v0 + 140, v41)
            store32(v0 + 136, v40)
            store32(v0 + 132, v39)
            store32(v0 + 128, v38)
            store32(v0 + 124, v37)
            store32(v0 + 120, v2)
            store32(v0 + 116, v36)
            store32(v0 + 112, v35)
            store32(v0 + 108, v34)
            store32(v0 + 104, v33)
            store32(v0 + 100, v32)
            store32(v0 + 96, v31)
            store32(v0 + 92, v30)
            store32(v0 + 88, v29)
            store32(v0 + 84, v28)
            store32(v0 + 80, v27)
            store32(v0 + 76, v26)
            store32(v0 + 72, v25)
            store32(v0 + 68, v24)
            store32(v0 + 64, v23)
            store32(v0 + 60, v22)
            store32(v0 + 56, v21)
            store32(v0 + 52, v20)
            store32(v0 + 48, v19)
            store32(v0 + 44, v18)
            store32(v0 + 40, v17)
            store32(v0 + 36, v16)
            store32(v0 + 32, v15)
            store32(v0 + 28, v14)
            store32(v0 + 24, v11)
            store32(v0 + 20, v9)
            store32(v0 + 16, v8)
            store32(v0 + 12, v7)
            store32(v0 + 8, v6)
            store32(v0 + 4, v4)
            store32(v0, v10)
            store64(v0 + 232, 0)
            store64(v0 + 224, 0)
            store64(v0 + 216, 0)
            while True:  # block $label7
                v2 = load32(v1 + 236)
                if (load32(v1 + 236) == 0):
                    break
                v8 = (v2 & 3)
                v0 = load32(v1 + 232)
                v4 = 0
                while True:  # block $label8
                    if (u(v2) < u(4)):
                        v2 = 0
                        break
                    v11 = (v2 & -4)
                    v2 = 0
                    v9 = 0
                    while True:  # $label9
                        v6 = (v5 + (v3 << 2))
                        v7 = (v2 << 2)
                        store32((v5 + (v3 << 2)), load32((v0 + (v2 << 2))))
                        store32(v6 + 4, load32((v0 + (v7 | 4))))
                        store32(v6 + 8, load32((v0 + (v7 | 8))))
                        store32(v6 + 12, load32((v0 + (v7 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v9 = (v9 + 4)
                        if ((v9 + 4) != v11):
                            continue
                        break
                    break
                if (v8 == 0):
                    break
                while True:  # $label10
                    store32((v5 + (v3 << 2)), load32((v0 + (v2 << 2))))
                    v2 = (v2 + 1)
                    v3 = (v3 + 1)
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v8):
                        continue
                    break
                break
            while True:  # block $label11
                v0 = load32(v1 + 364)
                if (load32(v1 + 364) == 0):
                    break
                v7 = (v0 & 3)
                v1 = load32(v1 + 24)
                v8 = 0
                while True:  # block $label12
                    if (u(v0) < u(4)):
                        v2 = 0
                        break
                    v9 = (v0 & -4)
                    v2 = 0
                    v4 = 0
                    while True:  # $label13
                        v0 = (v5 + (v3 << 2))
                        v6 = (v2 << 2)
                        store32((v5 + (v3 << 2)), load32((v1 + (v2 << 2))))
                        store32(v0 + 4, load32((v1 + (v6 | 4))))
                        store32(v0 + 8, load32((v1 + (v6 | 8))))
                        store32(v0 + 12, load32((v1 + (v6 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v4 = (v4 + 4)
                        if ((v4 + 4) != v9):
                            continue
                        break
                    break
                if (v7 == 0):
                    break
                while True:  # $label14
                    store32((v5 + (v3 << 2)), load32((v1 + (v2 << 2))))
                    v2 = (v2 + 1)
                    v3 = (v3 + 1)
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v7):
                        continue
                    break
                break
            v2 = 0
            while True:  # $label15
                v1 = load32((v13 + (v2 << 2)))
                if (load32((v13 + (v2 << 2))) != 100):
                    v0 = (v5 + (v3 << 2))
                    store32((v5 + (v3 << 2)), v2)
                    store32(v0 + 4, v1)
                    v3 = (v3 + 2)
                v1 = (v2 | 1)
                if ((v2 | 1) != 255):
                    v0 = load32((v13 + (v1 << 2)))
                    if (load32((v13 + (v1 << 2))) != 100):
                        v4 = (v5 + (v3 << 2))
                        store32((v5 + (v3 << 2)), v1)
                        store32(v4 + 4, v0)
                        v3 = (v3 + 2)
                    v2 = (v2 + 2)
                    continue
                break
            v12 = (v12 + 1)
            break
        v10 = (v10 + 1)
        if ((v10 + 1) != 255):
            continue
        break
    return (v12 * 60)

# ------------------------------------------------------------
# $Ud
# Export: Ud
# ------------------------------------------------------------
def Ud(arg0):
    """Exported as Ud."""
    while True:  # block $label0
        if (arg0 != 2147483647):
            if arg0:
                break
            return load32(9142908)
        return 0
        break
    v1 = load32(9142908)
    if load32(9142908):
        store32(9142908, 0)
    store32(9142912, arg0)
    arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
    store32(9142908, func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2))))
    return arg0

# ------------------------------------------------------------
# $Vd
# Export: Vd
# ------------------------------------------------------------
def Vd():
    """Exported as Vd."""
    return load32(9685864)

# ------------------------------------------------------------
# $Lb
# Export: Lb
# ------------------------------------------------------------
def Lb():
    """Exported as Lb."""
    return load32(9142912)

# ------------------------------------------------------------
# $Oe
# Export: Oe
# ------------------------------------------------------------
def Oe():
    """Exported as Oe."""
    return load32(9142440)

# ------------------------------------------------------------
# $Ze
# Export: Ze
# ------------------------------------------------------------
def Ze(arg0, arg1):
    """Exported as Ze."""
    store64(9147320, -104595085891)
    store64(9147312, 6510615450831814680)
    store32(9671228, 0)
    store32(9671220, 105)
    store32(9671240, 1)
    store32(9671224, 106)
    store64(9671204, 0)
    store32(9671280, 2)
    store32(9671268, 107)
    store32(9671260, 108)
    store32(9671276, 109)
    store32(9671272, 110)
    store8(9671257, 1)
    store64(9671244, 0)
    store32(9671308, 0)
    store32(9671300, 111)
    store32(9671264, 112)
    store32(9671200, 0)
    store32(9671348, 0)
    store32(9671340, 113)
    store32(9671320, 3)
    store64(9671284, 0)
    store32(9671360, 4)
    store32(9671380, 114)
    store32(9671388, 115)
    store64(9671324, 0)
    store32(9671384, 116)
    store32(9671400, 5)
    store32(9671420, 117)
    store32(9671428, 0)
    store64(9671364, 0)
    store8(9671377, 1)
    store32(9671440, 6)
    store32(9671460, 118)
    store32(9671468, 119)
    store64(9671404, 0)
    store32(9671508, 0)
    store32(9671500, 120)
    store32(9671480, 7)
    store32(9671472, 121)
    store32(9671464, 122)
    store8(9671457, 1)
    store64(9671444, 4294967294)
    store64(9671484, 0)
    store32(9671548, 0)
    store32(9671540, 123)
    store32(9671520, 8)
    store64(9671524, 0)
    store32(9671588, 0)
    store32(9671580, 124)
    store32(9671560, 9)
    store8(9671576, 1)
    store64(9671564, 176093659147)
    store32(9671628, 0)
    store32(9671620, 125)
    store32(9671600, 10)
    store32(9671668, 0)
    store32(9671660, 126)
    store32(9671640, 11)
    store64(9671604, 0)
    store32(9671708, 0)
    store32(9671700, 127)
    store32(9671680, 12)
    store64(9671644, 0)
    store32(9671748, 128)
    store32(9671740, 129)
    store32(9671720, 13)
    store64(9671684, 0)
    store32(9671788, 0)
    store32(9671780, 130)
    store32(9671760, 14)
    store32(9671744, 131)
    store8(9671737, 1)
    store64(9671724, 193273528330)
    store32(9671948, 0)
    store32(9671940, 132)
    store32(9671920, 18)
    store8(9671776, 1)
    store64(9671764, 197568495629)
    store32(9671944, 133)
    store8(9671937, 1)
    store64(9671924, 206158430222)
    store32(9671908, 0)
    store32(9671900, 134)
    store32(9671880, 17)
    store32(9671988, 0)
    store32(9671980, 135)
    store32(9671960, 19)
    store32(9671904, 136)
    store8(9671897, 1)
    store64(9671884, 201863462928)
    store32(9672028, 0)
    store32(9672020, 137)
    store32(9672000, 20)
    store64(9671964, 0)
    store64(9672004, 0)
    store32(9671828, 0)
    store32(9671820, 138)
    store32(9671800, 15)
    store8(9671816, 1)
    store64(9671804, 261993005068)
    arg0 = load32(38724)
    store32(9671868, 0)
    store32(9671860, 139)
    store32(9671840, 16)
    store8(9671818, 1)
    store8(9671856, 1)
    store64(9671844, 266287972367)
    store32(9671812, ((arg0 * 404) + 9568164))
    arg0 = load32(38728)
    store32(9672068, 0)
    store32(9672060, 140)
    store32(9672040, 21)
    store8(9671858, 1)
    store32(9672080, 22)
    store32(9672100, 141)
    store32(9672108, 0)
    store64(9672044, 0)
    store64(9672084, 0)
    store32(9672148, 0)
    store32(9672140, 142)
    store32(9672120, 23)
    store8(9672137, 1)
    store64(9672124, 395136991232)
    store32(9672268, 0)
    store32(9672260, 143)
    store32(9672240, 26)
    store32(9672144, 144)
    store32(9671852, ((arg0 * 404) + 9568164))
    store32(9672308, 0)
    store32(9672300, 145)
    store32(9672280, 27)
    store8(9672256, 1)
    store64(9672244, 287762808857)
    store8(9672296, 1)
    store64(9672284, 292057776159)
    arg0 = load32(38940)
    store32(9672348, 0)
    store32(9672340, 146)
    store32(9672320, 28)
    store8(9672298, 1)
    store8(9672336, 1)
    store64(9672324, 296352743457)
    store32(9672292, ((arg0 * 404) + 9568164))
    arg0 = load32(38936)
    store32(9672388, 0)
    store32(9672380, 147)
    store32(9672360, 29)
    store8(9672338, 1)
    store8(9672376, 1)
    store32(9672400, 30)
    store32(9672420, 148)
    store32(9672428, 0)
    store64(9672364, 300647710754)
    store8(9672416, 1)
    store64(9672404, 304942678048)
    store32(9672188, 0)
    store32(9672180, 149)
    store32(9672160, 24)
    store32(9673320, 53)
    store32(9673340, 150)
    store32(9673348, 0)
    store64(9672164, 0)
    store32(9672332, ((arg0 * 404) + 9568164))
    store64(9673324, 0)
    store32(9672228, 151)
    store32(9672220, 152)
    store32(9672200, 25)
    store32(9672468, 0)
    store32(9672460, 153)
    store32(9672440, 31)
    store32(9672224, 154)
    store64(9672204, 0)
    store32(9672508, 0)
    store32(9672500, 155)
    store32(9672480, 32)
    store64(9672444, 0)
    store32(9673548, 0)
    store32(9673540, 156)
    store32(9673520, 58)
    store64(9672484, 0)
    store64(9673524, 0)
    store32(9672548, 0)
    store32(9672540, 157)
    store32(9672520, 33)
    store32(9672588, 0)
    store32(9672580, 158)
    store32(9672560, 34)
    store64(9672524, 0)
    store32(9672628, 159)
    store32(9672620, 160)
    store32(9672600, 35)
    store64(9672564, 0)
    store32(9673428, 0)
    store32(9673420, 161)
    store32(9673400, 55)
    store32(9672624, 162)
    store64(9672604, 0)
    store64(9673404, 0)
    store32(9672668, 0)
    store32(9672660, 163)
    store32(9672640, 36)
    store32(9672708, 0)
    store32(9672700, 164)
    store32(9672680, 37)
    store64(9672644, 0)
    store32(9672748, 0)
    store32(9672740, 165)
    store32(9672720, 38)
    store32(9672704, 166)
    store64(9672684, 0)
    store32(9672788, 0)
    store32(9672780, 167)
    store32(9672760, 39)
    store32(9672744, 168)
    store64(9672724, 0)
    store32(9672820, 169)
    store32(9672800, 40)
    store8(9672776, 1)
    store64(9672764, 317827579939)
    store32(9672868, 0)
    store32(9672860, 170)
    store32(9672840, 41)
    store32(9672828, 171)
    store32(9672824, 172)
    store8(9672817, 1)
    store64(9672804, 322122547220)
    store32(9672908, 0)
    store32(9672900, 173)
    store32(9672880, 42)
    store8(9672856, 1)
    store64(9672844, 326417514515)
    store32(9672948, 0)
    store32(9672940, 174)
    store32(9672920, 43)
    store8(9672896, 1)
    store64(9672884, 330712481810)
    store8(9672936, 1)
    store64(9672924, 335007449105)
    arg0 = load32(38932)
    store32(9672988, 0)
    store32(9672980, 175)
    store32(9672960, 44)
    store8(9672938, 1)
    store32(9673000, 45)
    store32(9673020, 176)
    store32(9673028, 0)
    store64(9672964, 0)
    store64(9673004, 0)
    store32(9673068, 177)
    store32(9673060, 178)
    store32(9673040, 46)
    store8(9673057, 1)
    store64(9673044, 343597383708)
    store32(9673108, 0)
    store32(9673100, 179)
    store32(9673080, 47)
    store32(9673064, 180)
    store32(9672932, ((arg0 * 404) + 9568164))
    store32(9673188, 0)
    store32(9673180, 181)
    store32(9673160, 49)
    store32(9673104, 182)
    store8(9673097, 1)
    store64(9673084, 339302416420)
    store32(9673228, 0)
    store32(9673220, 183)
    store32(9673200, 50)
    store64(9673164, 0)
    store32(9673268, 0)
    store32(9673260, 184)
    store32(9673240, 51)
    store64(9673204, 0)
    store32(9673308, 0)
    store32(9673300, 185)
    store32(9673280, 52)
    store64(9673244, 0)
    store32(9673388, 186)
    store32(9673380, 187)
    store32(9673360, 54)
    store64(9673284, 0)
    store32(9673468, 0)
    store32(9673460, 188)
    store32(9673440, 56)
    store32(9673384, 189)
    store8(9673377, 1)
    store64(9673364, 0)
    store32(9673508, 0)
    store32(9673500, 190)
    store32(9673480, 57)
    store64(9673444, 0)
    store32(9673588, 0)
    store32(9673580, 191)
    store32(9673560, 59)
    store64(9673484, 0)
    store32(9673628, 192)
    store32(9673620, 193)
    store32(9673600, 60)
    store64(9673564, 0)
    store32(9673668, 0)
    store32(9673660, 194)
    store32(9673640, 61)
    store64(9673604, 0)
    store32(9673708, 195)
    store32(9673700, 196)
    store32(9673680, 62)
    store8(9673657, 1)
    store64(9673644, 0)
    store32(9673748, 197)
    store32(9673740, 198)
    store32(9673720, 63)
    store32(9673704, 199)
    store8(9673697, 1)
    store64(9673684, 0)
    store32(9673788, 0)
    store32(9673780, 200)
    store32(9673760, 64)
    store32(9673744, 201)
    store8(9673736, 1)
    store64(9673724, 0)
    store32(9673868, 0)
    store32(9673860, 202)
    store32(9673840, 66)
    store64(9673764, 0)
    store32(9673948, 0)
    store32(9673940, 203)
    store32(9673920, 68)
    store64(9673844, 0)
    store32(9673988, 204)
    store32(9673980, 205)
    store32(9673960, 69)
    store64(9673924, 0)
    store32(9674028, 0)
    store32(9674020, 206)
    store32(9674000, 70)
    store8(9673977, 1)
    store64(9673964, 0)
    store32(9674068, 0)
    store32(9674060, 207)
    store32(9674040, 71)
    store64(9674004, 0)
    store64(9674044, 0)
    store64(9685188, 523986010233)
    store64(9685180, 515396075639)
    store64(9685172, 506806141045)
    store64(9685164, 498216206451)
    store64(9685156, 489626271857)
    store64(9685148, 481036337263)
    store64(9685140, 472446402669)
    store64(9685132, 463856468075)
    store64(9685124, 455266533481)
    store64(9685116, 446676598887)
    store64(9685108, 438086664293)
    store64(9685100, 429496729699)
    store64(9685092, 420906795105)
    store32(9686320, 79)
    store32(9686324, 80)
    store32(9686328, 81)
    store32(9686336, 82)
    store32(9686340, 83)
    store32(9686344, 84)
    store32(9686348, 85)
    store32(9686356, 86)
    store32(9686360, 87)
    store32(9686364, 88)
    store32(9686368, 89)
    store32(9686372, 90)
    store32(9686000, 91)
    store32(9685944, 92)
    store32(9685940, 93)
    store32(9685936, 94)
    store32(9685924, 95)
    store32(9685904, 96)
    store32(9685908, 97)
    store32(9686064, 98)
    store32(9686068, 98)
    store32(9686072, 98)
    store32(9686076, 98)
    store32(9686080, 98)
    store32(9686084, 98)
    store32(9686088, 98)
    store32(9686092, 98)
    store32(9686096, 98)
    store32(9686100, 98)
    store32(9686752, 99)
    store32(9686232, 100)
    store32(9686228, 100)
    store32(9686224, 100)
    store32(9686220, 100)
    store32(9686216, 100)
    store32(9686212, 100)
    store32(9686208, 100)
    store32(9686204, 100)
    store32(9686200, 100)
    store32(9686196, 101)
    store32(9686192, 100)
    store32(9686188, 100)
    store32(9686184, 100)
    store32(9686180, 100)
    store32(9686176, 100)
    store32(9686172, 100)
    store32(9686168, 100)
    store32(9686164, 100)
    store32(9686160, 100)
    store32(9686156, 100)
    store32(9686152, 100)
    store32(9686148, 100)
    store32(9686144, 100)
    store32(9686140, 100)
    store32(9686136, 100)
    store32(9686132, 100)
    while True:  # block $label0
        arg1 = load32(9215892)
        if (load32(9215892) != load32(9215888)):
            arg0 = load32(9215884)
            break
        arg0 = (load32(9215896) + arg1)
        store32(9215888, (load32(9215896) + arg1))
        v2 = load32(9215884)
        arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg1:
            # TODO: memory.copy []
        if v2:
            arg1 = load32(9215892)
        store32(9215884, arg0)
        break
    store32(9215892, (arg1 + 1))
    store32((arg0 + (arg1 << 2)), 0)
    while True:  # block $label1
        arg1 = load32(9215892)
        if (load32(9215892) != load32(9215888)):
            v2 = arg0
            break
        v2 = (load32(9215896) + arg1)
        store32(9215888, (load32(9215896) + arg1))
        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
        if arg1:
            # TODO: memory.copy []
        store32(9215884, v2)
        arg1 = load32(9215892)
        break
    store32(9215892, (arg1 + 1))
    store32((v2 + (arg1 << 2)), 0)
    while True:  # block $label2
        arg1 = load32(9215892)
        if (load32(9215892) != load32(9215888)):
            arg0 = v2
            break
        arg0 = (load32(9215896) + arg1)
        store32(9215888, (load32(9215896) + arg1))
        arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if arg1:
            # TODO: memory.copy []
        store32(9215884, arg0)
        arg1 = load32(9215892)
        break
    store32(9215892, (arg1 + 1))
    store32((arg0 + (arg1 << 2)), 0)
    while True:  # block $label3
        arg1 = load32(9215892)
        if (load32(9215892) != load32(9215888)):
            v2 = arg0
            break
        v2 = (load32(9215896) + arg1)
        store32(9215888, (load32(9215896) + arg1))
        v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
        if arg1:
            # TODO: memory.copy []
        store32(9215884, v2)
        arg1 = load32(9215892)
        break
    store32(9215892, (arg1 + 1))
    store32((v2 + (arg1 << 2)), 0)
    store32(9214036, 208)
    store32(9214032, 209)
    store32(9214020, 208)
    store32(9214016, 210)
    store32(9214004, 0)
    store32(9214000, 211)
    store32(9213996, 212)
    store32(9213992, 213)
    store32(9213988, 0)
    store32(9213984, 214)
    store32(9213980, 215)
    store32(9213976, 216)
    store32(9213972, 215)
    store32(9213968, 217)
    store32(9213964, 212)
    store32(9213960, 218)
    store32(9213956, 0)
    store32(9213952, 219)
    store32(9213948, 0)
    store32(9213944, 220)
    store32(9213940, 212)
    store32(9213936, 221)
    store32(9213932, 208)
    store32(9213928, 222)
    store32(9213924, 208)
    store32(9213920, 223)
    store32(9213916, 208)
    store32(9213912, 224)
    store32(9213908, 208)
    store32(9213904, 225)
    store32(9213892, 208)
    store32(9213888, 226)
    store32(9213884, 208)
    store32(9213880, 227)
    store32(9213876, 208)
    store32(9213872, 228)
    store32(9213868, 208)
    store32(9213864, 229)
    store32(9213860, 208)
    store32(9213856, 230)
    store32(9213852, 208)
    store32(9213848, 231)
    store32(9213844, 208)
    store32(9213840, 232)
    store32(9213836, 233)
    store32(9213832, 234)
    store32(9213828, 208)
    store32(9213824, 235)
    store32(9214188, 0)
    store32(9214184, 236)
    store32(9214180, 0)
    store32(9214176, 237)
    store32(9214172, 212)
    store32(9214168, 238)
    store32(9214164, 208)
    store32(9214160, 239)
    store32(9214156, 0)
    store32(9214152, 240)
    store32(9214148, 0)
    store32(9214144, 241)
    store32(9214140, 242)
    store32(9214136, 243)
    store32(9214132, 208)
    store32(9214128, 244)
    store32(9214124, 0)
    store32(9214120, 245)
    store32(9214116, 0)
    store32(9214112, 246)
    store32(9214108, 0)
    store32(9214104, 247)
    store32(9214100, 0)
    store32(9214096, 248)
    store32(9214092, 208)
    store32(9214088, 249)
    store32(9214084, 0)
    store32(9214080, 250)
    store32(9214076, 0)
    store32(9214072, 251)
    store32(9214068, 212)
    store32(9214064, 252)
    store32(9214060, 212)
    store32(9214056, 253)
    store32(9214052, 208)
    store32(9214048, 254)
    store32(9214044, 215)
    store32(9214040, 255)
    store32(9214028, 0)
    store32(9214024, 256)
    store32(9214012, 208)
    store32(9214008, 257)
    arg0 = load32(9142908)
    if load32(9142908):
        store32(9142908, 0)
    store32(9142912, 0)
    func272()
    func271()
    func220()
    func218()
    arg0 = func26(188)
    store32(9142424, func26(188))
    # TODO: memory.copy []
    store32(9142428, 47)
    v3 = load32(38868)
    while True:  # block $label4
        arg1 = load32(9681452)
        arg0 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg1 = load32(9681448)
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        v2 = load32(9681448)
        arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
        if arg0:
            # TODO: memory.copy []
        if v2:
            arg0 = load32(9681456)
        store32(9681448, arg1)
        break
    store32(9681456, (arg0 + 1))
    store32((arg1 + (arg0 << 2)), v3)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 3)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 3)
    v3 = load32(38500)
    while True:  # block $label5
        arg0 = load32(9681452)
        v2 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg0 = arg1
            break
        arg0 = ((arg0 + load32(9681460)) + 3)
        store32(9681452, ((arg0 + load32(9681460)) + 3))
        arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if v2:
            # TODO: memory.copy []
        store32(9681448, arg0)
        v2 = load32(9681456)
        break
    store32(9681456, (v2 + 1))
    store32((arg0 + (v2 << 2)), v3)
    arg1 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg0 + (arg1 << 2)), 1)
    arg1 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg0 + (arg1 << 2)), 0)
    v3 = load32(38500)
    while True:  # block $label6
        arg1 = load32(9681452)
        v2 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg1 = arg0
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy []
        store32(9681448, arg1)
        v2 = load32(9681456)
        break
    store32(9681456, (v2 + 1))
    store32((arg1 + (v2 << 2)), v3)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 4)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 0)
    v3 = load32(38500)
    while True:  # block $label7
        arg0 = load32(9681452)
        v2 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg0 = arg1
            break
        arg0 = ((arg0 + load32(9681460)) + 3)
        store32(9681452, ((arg0 + load32(9681460)) + 3))
        arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if v2:
            # TODO: memory.copy []
        store32(9681448, arg0)
        v2 = load32(9681456)
        break
    store32(9681456, (v2 + 1))
    store32((arg0 + (v2 << 2)), v3)
    arg1 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg0 + (arg1 << 2)), 7)
    arg1 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg0 + (arg1 << 2)), 1)
    v3 = load32(38500)
    while True:  # block $label8
        arg1 = load32(9681452)
        v2 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg1 = arg0
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy []
        store32(9681448, arg1)
        v2 = load32(9681456)
        break
    store32(9681456, (v2 + 1))
    store32((arg1 + (v2 << 2)), v3)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 0)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 3)
    v3 = load32(38500)
    while True:  # block $label9
        arg0 = load32(9681452)
        v2 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg0 = arg1
            break
        arg0 = ((arg0 + load32(9681460)) + 3)
        store32(9681452, ((arg0 + load32(9681460)) + 3))
        arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if v2:
            # TODO: memory.copy []
        store32(9681448, arg0)
        v2 = load32(9681456)
        break
    store32(9681456, (v2 + 1))
    store32((arg0 + (v2 << 2)), v3)
    arg1 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg0 + (arg1 << 2)), 1)
    arg1 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg0 + (arg1 << 2)), 6)
    v3 = load32(38500)
    while True:  # block $label10
        arg1 = load32(9681452)
        v2 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg1 = arg0
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy []
        store32(9681448, arg1)
        v2 = load32(9681456)
        break
    store32(9681456, (v2 + 1))
    store32((arg1 + (v2 << 2)), v3)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 4)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 7)
    v3 = load32(38500)
    while True:  # block $label11
        arg0 = load32(9681452)
        v2 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg0 = arg1
            break
        arg0 = ((arg0 + load32(9681460)) + 3)
        store32(9681452, ((arg0 + load32(9681460)) + 3))
        arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
        if v2:
            # TODO: memory.copy []
        store32(9681448, arg0)
        v2 = load32(9681456)
        break
    store32(9681456, (v2 + 1))
    store32((arg0 + (v2 << 2)), v3)
    arg1 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg0 + (arg1 << 2)), 7)
    arg1 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg0 + (arg1 << 2)), 7)
    v3 = load32(38500)
    while True:  # block $label12
        arg1 = load32(9681452)
        v2 = load32(9681456)
        if (u(load32(9681452)) > u((load32(9681456) + 3))):
            arg1 = arg0
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy []
        store32(9681448, arg1)
        v2 = load32(9681456)
        break
    store32(9681456, (v2 + 1))
    store32((arg1 + (v2 << 2)), v3)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 7)
    arg0 = load32(9681456)
    store32(9681456, (load32(9681456) + 1))
    store32((arg1 + (arg0 << 2)), 4)
    return 0

# ------------------------------------------------------------
# $Je
# Export: Je
# ------------------------------------------------------------
def Je(arg0):
    """Exported as Je."""
    arg0 = (load32(9561692) + (arg0 * 286704))
    return (((load8u(((load32(9561692) + (arg0 * 286704)) + 283973)) << 8) | load8u((arg0 + 283974))) | (load8u(arg0 + 283972) << 16))

# ------------------------------------------------------------
# $Q
# Export: Q
# ------------------------------------------------------------
def Q(arg0, arg1, arg2):
    """Exported as Q."""
    v3 = load32(9561692)
    if arg2:
        store32((((v3 + (arg0 * 286704)) + (arg1 << 2)) + 283984), (arg2 - 1))
    if (arg1 == 97):
        arg2 = (v3 + (arg0 * 286704))
        store32((v3 + (arg0 * 286704)) + 283868, load32((arg2 + 284372)))
    return load32((((v3 + (arg0 * 286704)) + (arg1 << 2)) + 283984))

# ------------------------------------------------------------
# $R
# Export: R
# ------------------------------------------------------------
def R(arg0, arg1, arg2, arg3):
    """Exported as R."""
    v4 = load32(9561692)
    while True:  # block $label0
        if (arg1 == 0):
            break
        v5 = (v4 + (arg0 * 286704))
        arg1 = (arg1 - 1)
        store32(((v4 + (arg0 * 286704)) + (286688 if arg2 else 286684)), (100 if (u(arg1) >= u(100)) else (arg1 - 1)))
        if (arg3 == 0):
            break
        if load32(v5 + 286688):
            break
        store32((v5 + 286688), 100)
        break
    return load32(((v4 + (arg0 * 286704)) + (286688 if arg2 else 286684)))

# ------------------------------------------------------------
# $De
# Export: De
# ------------------------------------------------------------
def De(arg0, arg1, arg2):
    """Exported as De."""
    func182()
    v6 = load32(9142440)
    if (load32(9142440) > 0):
        v3 = v6
        while True:  # $label2
            v5 = (v4 + 1)
            v8 = load32(9142840)
            arg0 = 0
            while True:  # $label1
                v7 = arg0
                arg0 = (arg0 + 1)
                while True:  # block $label0
                    if (u(v3) <= u(v7)):
                        break
                    if (u(v3) <= u(v4)):
                        break
                    store32((v8 + ((v5 + (arg0 * (v3 + 2))) << 2)), 0)
                    v3 = (load32(9142440) + 2)
                    store32((v8 + ((v5 + ((arg0 + (load32(9142440) + 2)) * v3)) << 2)), 0)
                    v3 = (load32(9142440) + 2)
                    store32((v8 + ((v5 + ((arg0 + ((load32(9142440) + 2) << 1)) * v3)) << 2)), 0)
                    v3 = load32(9142440)
                    break
                if (arg0 != v6):
                    continue
                break
            v4 = v5
            if (v5 != v6):
                continue
            break
        if (v3 > 0):
            v4 = 0
            v5 = v3
            while True:  # $label5
                v6 = (v4 + 1)
                v8 = load32(9142840)
                arg0 = 0
                while True:  # $label4
                    v7 = arg0
                    arg0 = (arg0 + 1)
                    while True:  # block $label3
                        if (u(v5) <= u(v7)):
                            break
                        if (u(v4) >= u(v5)):
                            break
                        store32((v8 + ((v6 + (arg0 * (v5 + 2))) << 2)), 0)
                        v5 = (load32(9142440) + 2)
                        store32((v8 + ((v6 + ((arg0 + (load32(9142440) + 2)) * v5)) << 2)), 0)
                        v5 = (load32(9142440) + 2)
                        store32((v8 + ((v6 + ((arg0 + ((load32(9142440) + 2) << 1)) * v5)) << 2)), 0)
                        v5 = load32(9142440)
                        break
                    if (arg0 != v3):
                        continue
                    break
                v4 = v6
                if (v6 != v3):
                    continue
                break
    else:
    v7 = ((v6 & 0xFFFFFFFF) >> 1)
    v16 = v7
    v14 = arg2
    v15 = v7
    v13 = arg1
    v4 = load32(9142440)
    if (load32(9142440) > 0):
        arg0 = ((v4 & 0xFFFFFFFF) >> 1)
        v8 = (((v4 & 0xFFFFFFFF) >> 1) + 15)
        arg1 = (arg0 - 15)
        v9 = (v4 & -4)
        arg2 = (v4 & 3)
        v10 = (v4 & -2)
        v11 = (v4 & 1)
        v12 = (u(v4) < u(4))
        v3 = 0
        while True:  # $label12
            while True:  # block $label9
                if (((arg1 < v3) & (v3 < v8)) == 0):
                    arg0 = 0
                    v5 = 0
                    if (v4 != 1):
                        while True:  # $label8
                            while True:  # block $label6
                                if (arg0 <= arg1):
                                    break
                                if (arg0 >= v8):
                                    break
                                store8((load32(9147288) + ((load32(9142440) * arg0) + v3)), 3)
                                break
                            while True:  # block $label7
                                if (arg0 < arg1):
                                    break
                                v6 = (arg0 | 1)
                                if ((arg0 | 1) >= v8):
                                    break
                                store8((load32(9147288) + ((load32(9142440) * v6) + v3)), 3)
                                break
                            arg0 = (arg0 + 2)
                            v5 = (v5 + 2)
                            if ((v5 + 2) != v10):
                                continue
                            break
                    if (v11 == 0):
                        break
                    if (arg0 <= arg1):
                        break
                    if (arg0 >= v8):
                        break
                    store8((load32(9147288) + ((load32(9142440) * arg0) + v3)), 3)
                    break
                v5 = 0
                arg0 = 0
                v6 = 0
                if (v12 == 0):
                    while True:  # $label10
                        store8((load32(9147288) + ((load32(9142440) * arg0) + v3)), 3)
                        store8((load32(9147288) + ((load32(9142440) * (arg0 | 1)) + v3)), 3)
                        store8((load32(9147288) + ((load32(9142440) * (arg0 | 2)) + v3)), 3)
                        store8((load32(9147288) + ((load32(9142440) * (arg0 | 3)) + v3)), 3)
                        arg0 = (arg0 + 4)
                        v6 = (v6 + 4)
                        if ((v6 + 4) != v9):
                            continue
                        break
                if (arg2 == 0):
                    break
                while True:  # $label11
                    store8((load32(9147288) + ((load32(9142440) * arg0) + v3)), 3)
                    arg0 = (arg0 + 1)
                    v5 = (v5 + 1)
                    if ((v5 + 1) != arg2):
                        continue
                    break
                break
            v3 = (v3 + 1)
            if ((v3 + 1) != v4):
                continue
            break
        v4 = load32(9142440)
    # TODO: i32.div_u []
    arg0 = 100
    v3 = ((v13 * v4) - 100)
    v6 = ((arg0 << 1) + v7)
    if (((v13 * v4) - 100) < ((arg0 << 1) + v7)):
        v5 = (arg0 * arg0)
        arg1 = v3
        while True:  # $label15
            arg0 = (arg1 - v7)
            v8 = (((arg1 - v7) * arg0) - 1)
            arg0 = v3
            while True:  # $label14
                while True:  # block $label13
                    v4 = (arg0 - v7)
                    if ((v8 + ((arg0 - v7) * v4)) > v5):
                        break
                    v4 = load32(9142440)
                    if (u(load32(9142440)) <= u(arg0)):
                        break
                    if ((arg0 | arg1) < 0):
                        break
                    if (u(arg1) >= u(v4)):
                        break
                    store8((load32(9147288) + ((arg0 * v4) + arg1)), 3)
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v6):
                    continue
                break
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != v6):
                continue
            break
        v4 = load32(9142440)
    # TODO: i32.div_u []
    arg0 = 100
    arg2 = ((v14 * v4) - 100)
    v3 = ((arg0 << 1) + v7)
    if (((v14 * v4) - 100) < ((arg0 << 1) + v7)):
        v4 = (arg0 * arg0)
        arg1 = arg2
        while True:  # $label18
            arg0 = (arg1 - v7)
            v5 = (((arg1 - v7) * arg0) - 1)
            arg0 = arg2
            while True:  # $label17
                while True:  # block $label16
                    v6 = (arg0 - v7)
                    if ((v5 + ((arg0 - v7) * v6)) > v4):
                        break
                    v6 = load32(9142440)
                    if (u(load32(9142440)) <= u(arg0)):
                        break
                    if ((arg0 | arg1) < 0):
                        break
                    if (u(arg1) >= u(v6)):
                        break
                    store8((load32(9147288) + ((arg0 * v6) + arg1)), 1)
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != v3):
                    continue
                break
            arg1 = (arg1 + 1)
            if ((arg1 + 1) != v3):
                continue
            break
        v4 = load32(9142440)
    v3 = 0
    if v4:
        v6 = load32(9147288)
        v3 = v4
        v5 = 0
        while True:  # $label21
            arg1 = (v5 + 1)
            arg2 = load32(9142840)
            v4 = load32(9140332)
            arg0 = 0
            while True:  # $label20
                while True:  # block $label19
                    v7 = load8s((v6 + ((arg0 * v3) + v5)))
                    if (load8s((v6 + ((arg0 * v3) + v5))) < 0):
                        break
                    if (load32(load32((v4 + ((v7 & 255) << 2))) + 32) != 23):
                        break
                    v7 = (arg0 + 1)
                    store32((arg2 + ((((arg0 + 1) * (v3 + 2)) + arg1) << 2)), 1)
                    v3 = (load32(9142440) + 2)
                    store32((arg2 + (((((load32(9142440) + 2) + v7) * v3) + arg1) << 2)), 1)
                    v3 = load32(9142440)
                    break
                arg0 = (arg0 + 1)
                if (u((arg0 + 1)) < u(v3)):
                    continue
                break
            v5 = arg1
            if (u(arg1) < u(v3)):
                continue
            break
    func169()
    return func343()

# ------------------------------------------------------------
# $Zd
# Export: Zd
# ------------------------------------------------------------
def Zd():
    """Exported as Zd."""
    while True:  # $label1
        v3 = ((v1 * 404) + 9568096)
        if (load32(((v1 * 404) + 9568096) + 264) == 1):
            v0 = (((load32(v3 + 364) + (v0 + load32(v3 + 236))) + (load32(v3 + 220) * load32(v3 + 216))) + 56)
            v3 = 0
            while True:  # $label0
                v0 = (((v1 * 1020) + 9299904) + (v3 << 2))
                v6 = (v0 if (load32((((v1 * 1020) + 9299904) + (v3 << 2))) == 100) else (v0 + 2))
                v6 = ((v0 if (load32((((v1 * 1020) + 9299904) + (v3 << 2))) == 100) else (v0 + 2)) if (load32(v0 + 4) == 100) else (v6 + 2))
                v0 = (((v0 if (load32((((v1 * 1020) + 9299904) + (v3 << 2))) == 100) else (v0 + 2)) if (load32(v0 + 4) == 100) else (v6 + 2)) if (load32(v0 + 8) == 100) else (v6 + 2))
                v3 = (v3 + 3)
                if ((v3 + 3) != 255):
                    continue
                break
            v2 = (v2 + 1)
        v1 = (v1 + 1)
        if ((v1 + 1) != 255):
            continue
        break
    v3 = load32(9685864)
    if load32(9685864):
        store32(9685864, 0)
    v3 = (v2 * 56)
    v6 = func26((-1 if (u(v0) > u(1073741823)) else (v0 << 2)))
    store32(9685864, func26((-1 if (u(v0) > u(1073741823)) else (v0 << 2))))
    while True:  # $label16
        v1 = 0
        v0 = 0
        v2 = ((v11 * 404) + 9568096)
        if (load32(((v11 * 404) + 9568096) + 264) == 1):
            while True:  # $label2
                v15 = ((v11 * 1020) + 9299904)
                v0 = (((v11 * 1020) + 9299904) + (v1 << 2))
                v4 = (v0 if (load32((((v11 * 1020) + 9299904) + (v1 << 2))) == 100) else (v0 + 2))
                v4 = ((v0 if (load32((((v11 * 1020) + 9299904) + (v1 << 2))) == 100) else (v0 + 2)) if (load32(v0 + 4) == 100) else (v4 + 2))
                v0 = (((v0 if (load32((((v11 * 1020) + 9299904) + (v1 << 2))) == 100) else (v0 + 2)) if (load32(v0 + 4) == 100) else (v4 + 2)) if (load32(v0 + 8) == 100) else (v4 + 2))
                v1 = (v1 + 3)
                if ((v1 + 3) != 255):
                    continue
                break
            v10 = load32(v2 + 104)
            v12 = load32(v2 + 68)
            v14 = load32(v2 + 72)
            v16 = load32(v2 + 76)
            v17 = load32(v2 + 80)
            v18 = load32(v2 + 116)
            v4 = load32(v2 + 236)
            v19 = load32(v2 + 92)
            v20 = load32(v2 + 276)
            v21 = load32(v2 + 224)
            v22 = load32(v2 + 204)
            v23 = load32(v2 + 200)
            v24 = load32(v2 + 228)
            v25 = load32(v2 + 208)
            v5 = load32(v2 + 220)
            v7 = load32(v2 + 216)
            v8 = load32(v2 + 192)
            v26 = load32(v2 + 188)
            v27 = load32(v2 + 84)
            v28 = load32(v2 + 136)
            v29 = load32(v2 + 140)
            v30 = load32(v2 + 176)
            v9 = load32(v2 + 364)
            v31 = load32(v2 + 272)
            v32 = load32(v2 + 212)
            v1 = (v6 + (v13 * 224))
            store32((v6 + (v13 * 224)) + 108, v0)
            store32(v1 + 104, v32)
            store32(v1 + 100, v31)
            store32(v1 + 96, v9)
            store32(v1 + 92, v30)
            store32(v1 + 88, v29)
            store32(v1 + 84, v28)
            store32(v1 + 80, v27)
            store32(v1 + 76, v26)
            store32(v1 + 72, v8)
            v8 = (v5 * v7)
            store32(v1 + 68, (v5 * v7))
            store32(v1 + 64, v5)
            store32(v1 + 60, v7)
            store32(v1 + 56, v25)
            store32(v1 + 52, v24)
            store32(v1 + 48, v23)
            store32(v1 + 44, v22)
            store32(v1 + 40, v21)
            store32(v1 + 36, v20)
            store32(v1 + 32, v19)
            store32(v1 + 28, v4)
            store32(v1 + 24, v18)
            store32(v1 + 20, v17)
            store32(v1 + 16, v16)
            store32(v1 + 12, v14)
            store32(v1 + 8, v12)
            store32(v1 + 4, v10)
            store32(v1, v11)
            # TODO: memory.fill []
            while True:  # block $label3
                if (v4 == 0):
                    break
                v10 = (v4 & 3)
                v5 = load32(v2 + 232)
                v1 = 0
                while True:  # block $label4
                    if (u(v4) < u(4)):
                        v0 = 0
                        break
                    v14 = (v4 & -4)
                    v0 = 0
                    v12 = 0
                    while True:  # $label5
                        v4 = (v6 + (v3 << 2))
                        v7 = (v0 << 2)
                        store32((v6 + (v3 << 2)), load32((v5 + (v0 << 2))))
                        store32(v4 + 4, load32((v5 + (v7 | 4))))
                        store32(v4 + 8, load32((v5 + (v7 | 8))))
                        store32(v4 + 12, load32((v5 + (v7 | 12))))
                        v0 = (v0 + 4)
                        v3 = (v3 + 4)
                        v12 = (v12 + 4)
                        if ((v12 + 4) != v14):
                            continue
                        break
                    break
                if (v10 == 0):
                    break
                while True:  # $label6
                    store32((v6 + (v3 << 2)), load32((v5 + (v0 << 2))))
                    v0 = (v0 + 1)
                    v3 = (v3 + 1)
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v10):
                        continue
                    break
                break
            while True:  # block $label7
                if (v8 == 0):
                    break
                v7 = (v8 & 3)
                v4 = load32(v2 + 372)
                v10 = 0
                while True:  # block $label8
                    if (u(v8) < u(4)):
                        v0 = 0
                        break
                    v8 = (v8 & -4)
                    v0 = 0
                    v1 = 0
                    while True:  # $label9
                        v5 = (v6 + (v3 << 2))
                        store32((v6 + (v3 << 2)), load8u((v0 + v4)))
                        store32(v5 + 4, load8u((v4 + (v0 | 1))))
                        store32(v5 + 8, load8u((v4 + (v0 | 2))))
                        store32(v5 + 12, load8u((v4 + (v0 | 3))))
                        v0 = (v0 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v8):
                            continue
                        break
                    break
                if (v7 == 0):
                    break
                while True:  # $label10
                    store32((v6 + (v3 << 2)), load8u((v0 + v4)))
                    v0 = (v0 + 1)
                    v3 = (v3 + 1)
                    v10 = (v10 + 1)
                    if ((v10 + 1) != v7):
                        continue
                    break
                break
            while True:  # block $label11
                if (v9 == 0):
                    break
                v5 = (v9 & 3)
                v2 = load32(v2 + 24)
                v8 = 0
                while True:  # block $label12
                    if (u(v9) < u(4)):
                        v0 = 0
                        break
                    v7 = (v9 & -4)
                    v0 = 0
                    v1 = 0
                    while True:  # $label13
                        v4 = (v6 + (v3 << 2))
                        v9 = (v0 << 2)
                        store32((v6 + (v3 << 2)), load32((v2 + (v0 << 2))))
                        store32(v4 + 4, load32((v2 + (v9 | 4))))
                        store32(v4 + 8, load32((v2 + (v9 | 8))))
                        store32(v4 + 12, load32((v2 + (v9 | 12))))
                        v0 = (v0 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v7):
                            continue
                        break
                    break
                if (v5 == 0):
                    break
                while True:  # $label14
                    store32((v6 + (v3 << 2)), load32((v2 + (v0 << 2))))
                    v0 = (v0 + 1)
                    v3 = (v3 + 1)
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v5):
                        continue
                    break
                break
            v0 = 0
            while True:  # $label15
                v2 = load32((v15 + (v0 << 2)))
                if (load32((v15 + (v0 << 2))) != 100):
                    v1 = (v6 + (v3 << 2))
                    store32((v6 + (v3 << 2)), v0)
                    store32(v1 + 4, v2)
                    v3 = (v3 + 2)
                v2 = (v0 | 1)
                if ((v0 | 1) != 255):
                    v1 = load32((v15 + (v2 << 2)))
                    if (load32((v15 + (v2 << 2))) != 100):
                        v4 = (v6 + (v3 << 2))
                        store32((v6 + (v3 << 2)), v2)
                        store32(v4 + 4, v1)
                        v3 = (v3 + 2)
                    v0 = (v0 + 2)
                    continue
                break
            v13 = (v13 + 1)
        v11 = (v11 + 1)
        if ((v11 + 1) != 255):
            continue
        break
    return (v13 * 56)

# ------------------------------------------------------------
# $Ec
# Export: Ec
# ------------------------------------------------------------
def Ec():
    """Exported as Ec."""
    return load32(9671136)

# ------------------------------------------------------------
# $X
# Export: X
# ------------------------------------------------------------
def X(arg0):
    """Exported as X."""
    if (arg0 == 0):
        return 0
    return (load32((load32(9561692) + (load32(9142872) * 286704)) + 284608) == arg0)

# ------------------------------------------------------------
# $Sd
# Export: Sd
# ------------------------------------------------------------
def Sd(arg0, arg1, arg2):
    """Exported as Sd."""
    while True:  # block $label0
        v3 = ((arg0 * 404) + 9568096)
        if load8u(((arg0 * 404) + 9568096) + 378):
            break
        v3 = load32(v3 + 264)
        while True:  # block $label1
            if arg2:
                if (v3 == 0):
                    break
                break
            if (v3 != 1):
                break
            break
        arg2 = 0
        while True:  # $label3
            while True:  # block $label2
                if load8u(((arg2 * 404) + 9568096) + 378):
                    break
                v3 = load32(((((arg2 * 1020) + 9299904) + (arg0 << 2)) if arg1 else (((arg0 * 1020) + 9299904) + (arg2 << 2))))
                if (load32(((((arg2 * 1020) + 9299904) + (arg0 << 2)) if arg1 else (((arg0 * 1020) + 9299904) + (arg2 << 2)))) == 100):
                    break
                v5 = ((v4 << 2) + 9147392)
                store32(((v4 << 2) + 9147392), arg2)
                store32(v5 + 4, v3)
                v4 = (v4 + 2)
                break
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != 255):
                continue
            break
        break
    return v4

# ------------------------------------------------------------
# $Cc
# Export: Cc
# ------------------------------------------------------------
def Cc():
    """Exported as Cc."""
    return load32(9163780)

# ------------------------------------------------------------
# $Pa
# Export: Pa
# ------------------------------------------------------------
def Pa():
    """Exported as Pa."""
    return load8u(9147213)

# ------------------------------------------------------------
# $Bb
# Export: Bb
# ------------------------------------------------------------
def Bb(arg0):
    """Exported as Bb."""
    while True:  # block $label0
        v1 = ((arg0 * 404) + 9568096)
        arg0 = load32(((arg0 * 404) + 9568096) + 236)
        if (load32(((arg0 * 404) + 9568096) + 236) == 0):
            arg0 = 0
            break
        v5 = (arg0 & 1)
        v2 = load32(v1 + 232)
        while True:  # block $label1
            if (arg0 == 1):
                arg0 = 0
                v1 = 0
                break
            v6 = (arg0 & -2)
            arg0 = 0
            v1 = 0
            while True:  # $label2
                v3 = (v1 << 2)
                v7 = load32((v2 + (v1 << 2)))
                if load8u(((load32((v2 + (v1 << 2))) * 132) + 9216080) + 23):
                    store32(((arg0 << 2) + 9147392), v7)
                    arg0 = (arg0 + 1)
                v3 = load32((v2 + (v3 | 4)))
                if load8u(((load32((v2 + (v3 | 4))) * 132) + 9216080) + 23):
                    store32(((arg0 << 2) + 9147392), v3)
                    arg0 = (arg0 + 1)
                v1 = (v1 + 2)
                v4 = (v4 + 2)
                if ((v4 + 2) != v6):
                    continue
                break
            break
        if (v5 == 0):
            break
        v1 = load32((v2 + (v1 << 2)))
        if (load8u(((load32((v2 + (v1 << 2))) * 132) + 9216080) + 23) == 0):
            break
        store32(((arg0 << 2) + 9147392), v1)
        arg0 = (arg0 + 1)
        break
    store32(((arg0 << 2) + 9147392), -1)

# ------------------------------------------------------------
# $Hb
# Export: Hb
# ------------------------------------------------------------
def Hb():
    """Exported as Hb."""
    return load32(load32(9142424) + 24)

# ------------------------------------------------------------
# $Dc
# Export: Dc
# ------------------------------------------------------------
def Dc():
    """Exported as Dc."""
    return load32(9163776)

# ------------------------------------------------------------
# $H
# Export: H
# ------------------------------------------------------------
def H():
    """Exported as H."""
    return load32(9142848)

# ------------------------------------------------------------
# $Ce
# Export: Ce
# ------------------------------------------------------------
def Ce(arg0):
    """Exported as Ce."""
    func182()
    if (arg0 == 0):
        v5 = load32(9142440)
        if (load32(9142440) > 0):
            v2 = v5
            while True:  # $label2
                v3 = (v4 + 1)
                v6 = load32(9142840)
                arg0 = 0
                while True:  # $label1
                    v1 = arg0
                    arg0 = (arg0 + 1)
                    while True:  # block $label0
                        if (u(v1) >= u(v2)):
                            break
                        if (u(v2) <= u(v4)):
                            break
                        store32((v6 + ((v3 + (arg0 * (v2 + 2))) << 2)), 0)
                        v1 = (load32(9142440) + 2)
                        store32((v6 + ((v3 + ((arg0 + (load32(9142440) + 2)) * v1)) << 2)), 0)
                        v1 = (load32(9142440) + 2)
                        store32((v6 + ((v3 + ((arg0 + ((load32(9142440) + 2) << 1)) * v1)) << 2)), 0)
                        v2 = load32(9142440)
                        break
                    if (arg0 != v5):
                        continue
                    break
                v4 = v3
                if (v3 != v5):
                    continue
                break
        func169()

# ------------------------------------------------------------
# $Zb
# Export: Zb
# ------------------------------------------------------------
def Zb(arg0):
    """Exported as Zb."""
    while True:  # $label2
        while True:  # block $label0
            v1 = load32(((arg0 + (v2 << 2)) + 284636))
            if (load32(((arg0 + (v2 << 2)) + 284636)) == 0):
                break
            v3 = load32(v1 + 8)
            if (load32(v1 + 8) == 0):
                break
            v4 = load32(v1)
            v1 = 0
            while True:  # $label1
                v5 = load32((v4 + (v1 << 2)))
                if (load32((v4 + (v1 << 2))) == 0):
                    v1 = (v1 + 1)
                    if (v3 != (v1 + 1)):
                        continue
                    break
                break
            v2 = (load32(9671128) + (v5 * 132))
            v1 = ((load8u((load32(9671128) + (v5 * 132)) + 122) * 404) + 9568096)
            store32(arg0 + 283896, (((load32(((load8u((load32(9671128) + (v5 * 132)) + 122) * 404) + 9568096) + 216) & 0xFFFFFFFF) >> 1) + load16u(v2 + 112)))
            store32(arg0 + 283900, (load16u(v2 + 114) + ((load32(v1 + 220) & 0xFFFFFFFF) >> 1)))
            return
            break
        v2 = (v2 + 1)
        if ((v2 + 1) != 255):
            continue
        break

# ------------------------------------------------------------
# $Ne
# Export: Ne
# ------------------------------------------------------------
def Ne():
    """Exported as Ne."""
    v0 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)

# ------------------------------------------------------------
# $Mc
# Export: Mc
# ------------------------------------------------------------
def Mc(arg0):
    """Exported as Mc."""
    v10 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    v3 = func26(4)
    v7 = func26(4)
    v8 = func26(4)
    v9 = func26(4)
    v1 = load32(9568076)
    while True:  # block $label5
        while True:  # block $label2
            while True:  # block $label1
                while True:  # block $label3
                    if (arg0 == 1):
                        while True:  # block $label0
                            arg0 = load32(v1 + 16)
                            if (load32(v1 + 16) != load32(v1 + 20)):
                                store64(arg0, 0)
                                store32(arg0 + 108, 1)
                                store64(arg0 + 100, 1)
                                store32(arg0 + 96, v9)
                                store32(arg0 + 92, 1)
                                store64(arg0 + 84, 1)
                                store32(arg0 + 80, v8)
                                store32(arg0 + 76, 1)
                                store64(arg0 + 68, 1)
                                store32(arg0 + 64, v7)
                                store32(arg0 + 60, 1)
                                store64(arg0 + 52, 1)
                                store32(arg0 + 48, v3)
                                store64(arg0 + 39, 0)
                                store64(arg0 + 32, 0)
                                store64(arg0 + 24, 0)
                                store64(arg0 + 16, 0)
                                store64(arg0 + 8, 0)
                                # TODO: memory.copy []
                                store32(arg0 + 192, 0)
                                arg0 = (arg0 + 196)
                                store32(v1 + 16, (arg0 + 196))
                                break
                            v4 = load32((v1 + 12))
                            v6 = (arg0 - load32((v1 + 12)))
                            arg0 = ((arg0 - load32((v1 + 12))) // 196)
                            v2 = (((arg0 - load32((v1 + 12))) // 196) + 1)
                            if (u((((arg0 - load32((v1 + 12))) // 196) + 1)) >= u(21913099)):
                                break
                            v11 = (arg0 << 1)
                            v2 = (21913098 if (u(arg0) >= u(10956549)) else ((arg0 << 1) if (u(v2) < u(v11)) else v2))
                            if (21913098 if (u(arg0) >= u(10956549)) else ((arg0 << 1) if (u(v2) < u(v11)) else v2)):
                                if (u(v2) >= u(21913099)):
                                    break
                                v5 = func26((v2 * 196))
                            arg0 = (v5 + (arg0 * 196))
                            store64((v5 + (arg0 * 196)), 0)
                            store32(arg0 + 192, 0)
                            store32(arg0 + 108, 1)
                            store64(arg0 + 100, 1)
                            store32(arg0 + 96, v9)
                            store32(arg0 + 92, 1)
                            store64(arg0 + 84, 1)
                            store32(arg0 + 80, v8)
                            store32(arg0 + 76, 1)
                            store64(arg0 + 68, 1)
                            store32(arg0 + 64, v7)
                            store32(arg0 + 60, 1)
                            store64(arg0 + 52, 1)
                            store32(arg0 + 48, v3)
                            store64(arg0 + 39, 0)
                            store64(arg0 + 32, 0)
                            store64(arg0 + 24, 0)
                            store64(arg0 + 16, 0)
                            store64(arg0 + 8, 0)
                            v3 = (arg0 + ((v6 // -196) * 196))
                            # TODO: memory.copy []
                            store32(v1 + 20, (v5 + (v2 * 196)))
                            arg0 = (arg0 + 196)
                            store32(v1 + 16, (arg0 + 196))
                            store32(v1 + 12, v3)
                            if (v4 == 0):
                                break
                            v1 = load32(9568076)
                            arg0 = load32(load32(9568076) + 16)
                            break
                        v1 = (v1 + 12)
                        break
                    while True:  # block $label4
                        arg0 = load32(v1 + 4)
                        if (load32(v1 + 4) != load32(v1 + 8)):
                            store64(arg0, 0)
                            store32(arg0 + 108, 1)
                            store64(arg0 + 100, 1)
                            store32(arg0 + 96, v9)
                            store32(arg0 + 92, 1)
                            store64(arg0 + 84, 1)
                            store32(arg0 + 80, v8)
                            store32(arg0 + 76, 1)
                            store64(arg0 + 68, 1)
                            store32(arg0 + 64, v7)
                            store32(arg0 + 60, 1)
                            store64(arg0 + 52, 1)
                            store32(arg0 + 48, v3)
                            store64(arg0 + 39, 0)
                            store64(arg0 + 32, 0)
                            store64(arg0 + 24, 0)
                            store64(arg0 + 16, 0)
                            store64(arg0 + 8, 0)
                            # TODO: memory.copy []
                            store32(arg0 + 192, 0)
                            store32(v1 + 4, (arg0 + 196))
                            break
                        v4 = load32(v1)
                        v6 = (arg0 - load32(v1))
                        arg0 = ((arg0 - load32(v1)) // 196)
                        v2 = (((arg0 - load32(v1)) // 196) + 1)
                        if (u((((arg0 - load32(v1)) // 196) + 1)) >= u(21913099)):
                            break
                        v11 = (arg0 << 1)
                        v2 = (21913098 if (u(arg0) >= u(10956549)) else ((arg0 << 1) if (u(v2) < u(v11)) else v2))
                        if (21913098 if (u(arg0) >= u(10956549)) else ((arg0 << 1) if (u(v2) < u(v11)) else v2)):
                            if (u(v2) >= u(21913099)):
                                break
                            v5 = func26((v2 * 196))
                        arg0 = (v5 + (arg0 * 196))
                        store64((v5 + (arg0 * 196)), 0)
                        store32(arg0 + 192, 0)
                        store32(arg0 + 108, 1)
                        store64(arg0 + 100, 1)
                        store32(arg0 + 96, v9)
                        store32(arg0 + 92, 1)
                        store64(arg0 + 84, 1)
                        store32(arg0 + 80, v8)
                        store32(arg0 + 76, 1)
                        store64(arg0 + 68, 1)
                        store32(arg0 + 64, v7)
                        store32(arg0 + 60, 1)
                        store64(arg0 + 52, 1)
                        store32(arg0 + 48, v3)
                        store64(arg0 + 39, 0)
                        store64(arg0 + 32, 0)
                        store64(arg0 + 24, 0)
                        store64(arg0 + 16, 0)
                        store64(arg0 + 8, 0)
                        v3 = (arg0 + ((v6 // -196) * 196))
                        # TODO: memory.copy []
                        store32(v1 + 8, (v5 + (v2 * 196)))
                        store32(v1 + 4, (arg0 + 196))
                        store32(v1, v3)
                        if (v4 == 0):
                            break
                        break
                    v1 = load32(9568076)
                    arg0 = load32(load32(9568076) + 4)
                    break
                v1 = load32(v1)
                G.global0 = (v10 + 80)
                return (((arg0 - v1) // 196) - 1)
                break
            func42()
            raise RuntimeError('unreachable')
            break
        func68()
        raise RuntimeError('unreachable')
        break
    func42()
    raise RuntimeError('unreachable')
    return af(v4)

# ------------------------------------------------------------
# $S
# Export: S
# ------------------------------------------------------------
def S(arg0, arg1):
    """Exported as S."""
    v6 = load32(9561692)
    if (arg1 == 0):
        arg1 = ((v6 + (arg0 * 286704)) + 283984)
        while True:  # $label0
            v2 = (v4 << 2)
            store32(((v4 << 2) + 9561072), load32((arg1 + v2)))
            v3 = (v2 + 4)
            store32(((v2 + 4) + 9561072), load32((arg1 + v3)))
            v3 = (v2 + 8)
            store32(((v2 + 8) + 9561072), load32((arg1 + v3)))
            v3 = (v2 + 12)
            store32(((v2 + 12) + 9561072), load32((arg1 + v3)))
            v2 = (v2 + 16)
            store32(((v2 + 16) + 9561072), load32((arg1 + v2)))
            v4 = (v4 + 5)
            if ((v4 + 5) != 155):
                continue
            break
        arg1 = load32(9142892)
        if load32(9142892):
            v9 = (v6 + (arg0 * 286704))
            v10 = ((v6 + (arg0 * 286704)) + 286688)
            v11 = (v9 + 286684)
            v4 = 0
            while True:  # $label3
                v2 = (v6 + (v4 * 286704))
                if (arg0 != load32((v6 + (v4 * 286704)) + 283908)):
                    while True:  # block $label1
                        arg1 = load32(v11)
                        if (load32(v11) == 0):
                            break
                        if (v4 == 0):
                            break
                        store32(v2 + 286684, arg1)
                        store32(v2 + 286688, load32(v10))
                        break
                    v8 = 0
                    while True:  # $label2
                        v3 = (v2 + 283984)
                        arg1 = (v8 << 2)
                        v7 = (v9 + 283984)
                        store32(((v2 + 283984) + (v8 << 2)), load32(((v9 + 283984) + arg1)))
                        v5 = (arg1 + 4)
                        store32((v3 + (arg1 + 4)), load32((v5 + v7)))
                        v5 = (arg1 + 8)
                        store32((v3 + (arg1 + 8)), load32((v5 + v7)))
                        v5 = (arg1 + 12)
                        store32((v3 + (arg1 + 12)), load32((v5 + v7)))
                        arg1 = (arg1 + 16)
                        store32((v3 + (arg1 + 16)), load32((arg1 + v7)))
                        v8 = (v8 + 5)
                        if ((v8 + 5) != 155):
                            continue
                        break
                    store32(v2 + 283868, load32((v2 + 284372)))
                    arg1 = load32(9142892)
                v4 = (v4 + 1)
                if (u((v4 + 1)) < u(arg1)):
                    continue
                break
        return
    arg0 = (v6 + (arg0 * 286704))
    store32((v6 + (arg0 * 286704)) + 283868, load32(9561460))
    # TODO: memory.copy []
    arg1 = load32(9142424)
    store32((arg0 + 284000), load32(load32(9142424) + 40))
    store32((arg0 + 284136), load32(arg1 + 36))

# ------------------------------------------------------------
# $Ra
# Export: Ra
# ------------------------------------------------------------
def Ra(arg0):
    """Exported as Ra."""
    return load32((load32(9561692) + (arg0 * 286704)) + 283964)

# ------------------------------------------------------------
# $P
# Export: P
# ------------------------------------------------------------
def P():
    """Exported as P."""
    v0 = (load32(9561692) + (load32(9142872) * 286704))
    return ((load32(9142440) * load32((load32(9561692) + (load32(9142872) * 286704)) + 283876)) + load32(v0 + 283872))

# ------------------------------------------------------------
# $Hd
# Export: Hd
# ------------------------------------------------------------
def Hd(arg0):
    """Exported as Hd."""
    v1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    store32(9684792, load32(((arg0 << 2) + 9140336)))
    store8(9681884, 0)
    arg0 = load32(9142880)
    while True:  # block $label0
        if load8u(9142916):
            store32(v1 + 48, arg0)
            a_b()
            break
        store32(v1 + 40, arg0)
        store64(v1 + 32, -4602115869219225600)
        store64(v1 + 24, 0)
        store64(v1 + 16, 0)
        a_b()
        break
    arg0 = 0
    if (load32(9684796) == 0):
        while True:  # block $label1
            if load8u(9142917):
                break
            arg0 = load32(9299880)
            if load32(9299880):
                arg0 = (arg0 - 1)
                store32(9299880, (arg0 - 1))
                arg0 = load32((load32(9299872) + (arg0 << 2)))
                break
            arg0 = load32(9163776)
            v2 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v3 = load32(9163784)
            if (u(v2) < u(load32(9163784))):
                break
            store32(v1, v3)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        store32(9684796, arg0)
    G.global0 = (v1 - -64)

# ------------------------------------------------------------
# $Oc
# Export: Oc
# ------------------------------------------------------------
def Oc(arg0, arg1):
    """Exported as Oc."""
    if arg1:
        v5 = load32(9568088)
        while True:  # block $label0
            if (arg0 == 0):
                break
            arg1 = 0
            if (u(arg0) >= u(4)):
                v7 = (arg0 & -4)
                v3 = (v5 + 112)
                while True:  # $label1
                    store16((v3 + (arg1 << 1)), load32(((arg1 << 2) + 9147392)))
                    v2 = (arg1 | 1)
                    store16((v3 + ((arg1 | 1) << 1)), load32(((v2 << 2) + 9147392)))
                    v2 = (arg1 | 2)
                    store16((v3 + ((arg1 | 2) << 1)), load32(((v2 << 2) + 9147392)))
                    v2 = (arg1 | 3)
                    store16((v3 + ((arg1 | 3) << 1)), load32(((v2 << 2) + 9147392)))
                    arg1 = (arg1 + 4)
                    v4 = (v4 + 4)
                    if ((v4 + 4) != v7):
                        continue
                    break
            v4 = (arg0 & 3)
            if ((arg0 & 3) == 0):
                break
            while True:  # $label2
                store16((v5 + (arg1 << 1)) + 112, load32(((arg1 << 2) + 9147392)))
                arg1 = (arg1 + 1)
                v6 = (v6 + 1)
                if ((v6 + 1) != v4):
                    continue
                break
            break
        store32(v5 + 192, arg0)
        return
    v5 = load32(9568076)
    while True:  # block $label3
        if (arg0 == 0):
            break
        arg1 = 0
        if (u(arg0) >= u(4)):
            v7 = (arg0 & -4)
            v3 = (v5 + 24)
            while True:  # $label4
                store16((v3 + (arg1 << 1)), load32(((arg1 << 2) + 9147392)))
                v2 = (arg1 | 1)
                store16((v3 + ((arg1 | 1) << 1)), load32(((v2 << 2) + 9147392)))
                v2 = (arg1 | 2)
                store16((v3 + ((arg1 | 2) << 1)), load32(((v2 << 2) + 9147392)))
                v2 = (arg1 | 3)
                store16((v3 + ((arg1 | 3) << 1)), load32(((v2 << 2) + 9147392)))
                arg1 = (arg1 + 4)
                v4 = (v4 + 4)
                if ((v4 + 4) != v7):
                    continue
                break
        v4 = (arg0 & 3)
        if ((arg0 & 3) == 0):
            break
        while True:  # $label5
            store16((v5 + (arg1 << 1)) + 24, load32(((arg1 << 2) + 9147392)))
            arg1 = (arg1 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v4):
                continue
            break
        break
    store32(v5 + 104, arg0)

# ------------------------------------------------------------
# $Fe
# Export: Fe
# ------------------------------------------------------------
def Fe(arg0):
    """Exported as Fe."""
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # block $label0
        v4 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v3 = 1
        v1 = 1
        while True:  # block $label1
            while True:  # block $label3
                while True:  # block $label2
                    # br_table[arg0]
                    break
                    break
                v10 = (arg0 - 2)
                v11 = (arg0 - 1)
                while True:  # $label7
                    store8(9147208, 1)
                    v8 = (load32(9561692) + (arg0 * 286704))
                    while True:  # block $label4
                        if (u(arg0) <= u(1)):
                            break
                        v3 = (v6 + v11)
                        v9 = ((v6 + v11) & 3)
                        v5 = load32(9143004)
                        v1 = 1
                        if (u((v6 + v10)) >= u(3)):
                            v12 = (v3 & -4)
                            v3 = 0
                            while True:  # $label5
                                store32(((v1 << 2) + 9147392), load8u((v5 + ((v1 * v4) + arg0))))
                                v7 = (v1 + 1)
                                store32((((v1 + 1) << 2) + 9147392), load8u((v5 + ((v4 * v7) + arg0))))
                                v7 = (v1 + 2)
                                store32((((v1 + 2) << 2) + 9147392), load8u((v5 + ((v4 * v7) + arg0))))
                                v7 = (v1 + 3)
                                store32((((v1 + 3) << 2) + 9147392), load8u((v5 + ((v4 * v7) + arg0))))
                                v1 = (v1 + 4)
                                v3 = (v3 + 4)
                                if ((v3 + 4) != v12):
                                    continue
                                break
                        v3 = 0
                        if (v9 == 0):
                            break
                        while True:  # $label6
                            store32(((v1 << 2) + 9147392), load8u((v5 + ((v1 * v4) + arg0))))
                            v1 = (v1 + 1)
                            v3 = (v3 + 1)
                            if ((v3 + 1) != v9):
                                continue
                            break
                        break
                    v1 = load8u(v8 + 283972)
                    v3 = load8u((v8 + 283974))
                    v4 = load8u((v8 + 283973))
                    store32(v2 + 52, v8)
                    store32(v2 + 48, arg0)
                    store32(v2 + 56, ((v3 | (v4 << 8)) | (v1 << 16)))
                    store32(v2 + 60, 0)
                    v6 = (v6 + 1)
                    arg0 = (arg0 + 1)
                    v4 = load32(9142892)
                    if (u((arg0 + 1)) < u(load32(9142892))):
                        continue
                    break
                break
                break
            while True:  # $label8
                arg0 = (load32(9561692) + (v3 * 286704))
                if load8u(9147208):
                    store8(9147208, 0)
                v1 = load8u(arg0 + 283972)
                v4 = load8u((arg0 + 283974))
                v5 = load8u((arg0 + 283973))
                store32(v2 + 12, load32(arg0 + 284608))
                store32(v2 + 4, arg0)
                store32(v2, v3)
                store32(v2 + 8, ((v4 | (v5 << 8)) | (v1 << 16)))
                v3 = (v3 + 1)
                if (u((v3 + 1)) < u(load32(9142892))):
                    continue
                break
            break
            break
        while True:  # $label9
            arg0 = (load32(9561692) + (v1 * 286704))
            v3 = load8u((load32(9561692) + (v1 * 286704)) + 283972)
            v4 = load8u((arg0 + 283974))
            v5 = load8u((arg0 + 283973))
            v6 = load32(arg0 + 286684)
            v13 = load64((arg0 + 283856))
            store64(v2 + 32, load64(arg0 + 283848))
            store64(v2 + 40, v13)
            store32(v2 + 16, v1)
            store32(v2 + 24, arg0)
            store32(v2 + 28, v6)
            store32(v2 + 20, ((v4 | (v5 << 8)) | (v3 << 16)))
            v1 = (v1 + 1)
            if (u((v1 + 1)) < u(load32(9142892))):
                continue
            break
        break
    G.global0 = (v2 - -64)

# ------------------------------------------------------------
# $Ye
# Export: Ye
# ------------------------------------------------------------
def Ye():
    """Exported as Ye."""
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v3 = load32(9684496)
        v1 = load32((load32(9684496) - 16))
        if (load32((load32(9684496) - 16)) == 0):
            break
        if (u(v1) >= u(4)):
            v4 = (v1 & -4)
            while True:  # $label1
                v2 = ((v0 * 60) + v3)
                store32(((v0 * 60) + v3) + 208, 2147483647)
                store32(v2 + 148, 2147483647)
                store32(v2 + 88, 2147483647)
                store32(v2 + 28, 2147483647)
                v0 = (v0 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v4):
                    continue
                break
        v2 = (v1 & 3)
        if ((v1 & 3) == 0):
            break
        v1 = 0
        while True:  # $label2
            store32(((v0 * 60) + v3) + 28, 2147483647)
            v0 = (v0 + 1)
            v1 = (v1 + 1)
            if ((v1 + 1) != v2):
                continue
            break
        break
    store32(9140308, 0)
    hd()
    func319()
    v0 = load32(9142440)
    v0 = (load32(9142440) * v0)
    store32(9142400, func26((-1 if (v0 & 805306368) else ((load32(9142440) * v0) << 4))))
    v1 = 0
    while True:  # block $label3
        v3 = load32(9140328)
        if (load32(9140328) == 0):
            break
        v6 = 0
        v0 = load32(9142440)
        v2 = (load32(9142440) * v0)
        v0 = 0
        if (u(v3) >= u(4)):
            v7 = (v3 & -4)
            while True:  # $label4
                v4 = (v0 << 2)
                v1 = ((((v2 * load32(load32((((v0 << 2) | 12) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + ((((((v2 * load32(load32((v4 + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + v1) + (((v2 * load32(load32(((v4 | 4) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)) + (((v2 * load32(load32(((v4 | 8) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16)))
                v0 = (v0 + 4)
                v8 = (v8 + 4)
                if ((v8 + 4) != v7):
                    continue
                break
        v3 = (v3 & 3)
        if ((v3 & 3) == 0):
            break
        while True:  # $label5
            v1 = ((((v2 * load32(load32(((v0 << 2) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + v1)
            v0 = (v0 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v3):
                continue
            break
        break
    if (load32(9681936) == 0):
        v0 = func26(16)
        v2 = (v1 << 2)
        store32(func26(16) + 4, (v1 << 2))
        store32(v0, func26((-1 if (u(v2) > u(1073741823)) else (v1 << 4))))
        store64(v0 + 8, 206158430208)
        store32(9681936, v0)
    store8(59182, 0)
    if (load8u(9142917) == 0):
        v0 = (load32(9142440) << 4)
        store32(v5, (load32(9142440) << 4))
        store32(v5 + 4, v0)
    G.global0 = (v5 + 16)

# ------------------------------------------------------------
# $Vb
# Export: Vb
# ------------------------------------------------------------
def Vb(arg0, arg1, arg2):
    """Exported as Vb."""
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if (load8u(9147210) == 0):
            func176(arg2, load32(9142872), (arg1 == 0))
            break
        while True:  # block $label1
            if (arg1 == 0):
                break
            if (load32(9147132) == 0):
                break
            if (load32(9142440) != 4096):
                break
            v5 = load32(9142892)
            if (u(load32(9142892)) < u(2)):
                break
            arg2 = 1
            v6 = (v5 - 1)
            v10 = ((v5 - 1) & 1)
            v7 = load32((load32(9561692) + (load32(9142872) * 286704)) + 283908)
            v8 = (load32((load32(9561692) + (load32(9142872) * 286704)) + 283908) * v5)
            v9 = load32(9143004)
            if (v5 != 2):
                v6 = (v6 & -2)
                v5 = 0
                while True:  # $label2
                    v3 = (arg2 + 1)
                    v3 = ((v3 + ((load8u((v9 + (arg2 + v8))) == 0) & (arg2 != v7))) + ((load8u((v9 + ((arg2 + 1) + v8))) == 0) & (v3 != v7)))
                    arg2 = (arg2 + 2)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v6):
                        continue
                    break
            if v10:
            else:
            if (u(v3) < u(3)):
                break
            a_b()
            store64(v4, 12884902817)
            a_b()
            break
            break
        store32(v4 + 12, arg1)
        store32(v4 + 8, arg0)
        func41(45, 0, 0, (v4 + 8), 2)
        break
    G.global0 = (v4 + 16)
    return v4

# ------------------------------------------------------------
# $Ub
# Export: Ub
# ------------------------------------------------------------
def Ub(arg0, arg1, arg2):
    """Exported as Ub."""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v3 + 12, arg2)
    store32(v3 + 8, arg1)
    store32(v3 + 4, arg0)
    while True:  # block $label0
        if load8u(9147210):
            func41(40, 0, 0, (v3 + 4), 3)
            break
        # call_indirect[load32(9214144)]
        break
    G.global0 = (v3 + 16)

# ------------------------------------------------------------
# $W
# Export: W
# ------------------------------------------------------------
def W(arg0, arg1):
    """Exported as W."""
    arg0 = (load32(9561692) + (arg0 * 286704))
    if load8u((load32(9561692) + (arg0 * 286704)) + 286699):

# ------------------------------------------------------------
# $Ge
# Export: Ge
# ------------------------------------------------------------
def Ge():
    """Exported as Ge."""
    return load8u(9147208)

# ------------------------------------------------------------
# $Ue
# Export: Ue
# ------------------------------------------------------------
def Ue(arg0, arg1):
    """Exported as Ue."""
    if (load32(9142912) if arg0 else 1):
        arg0 = load32(9142908)
        if load32(9142908):
            store32(9142908, 0)
        store32(9142912, 0)
        func272()
        func271()
        func220()
        func218()

# ------------------------------------------------------------
# $Ma
# Export: Ma
# ------------------------------------------------------------
def Ma():
    """Exported as Ma."""
    v1 = load32(9142892)
    if (u(load32(9142892)) >= u(2)):
        v2 = load32(9561692)
        v0 = 1
        while True:  # $label1
            while True:  # block $label0
                v3 = (v2 + (v0 * 286704))
                v4 = load32((v2 + (v0 * 286704)) + 284616)
                if (load32((v2 + (v0 * 286704)) + 284616) == 0):
                    break
                if load32(v3 + 284632):
                    break
                if (load32(v3 + 283908) == load32(9142872)):
                    break
                La(v4, 0)
                v1 = load32(9142892)
                v2 = load32(9561692)
                break
            v0 = (v0 + 1)
            if (u((v0 + 1)) < u(v1)):
                continue
            break

# ------------------------------------------------------------
# $Qc
# Export: Qc
# ------------------------------------------------------------
def Qc(arg0):
    """Exported as Qc."""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(9684424)
    while True:  # block $label0
        if arg0:
            v5 = load32(v2 + 8)
            if (load32(v2 + 8) == 0):
                break
            v4 = load32(v2)
            while True:  # $label1
                if (arg0 != load32((v4 + (v1 << 2)))):
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v5):
                        continue
                    break
                break
            if (v1 < 0):
                break
            arg0 = (v5 - 1)
            store32(v2 + 8, (v5 - 1))
            if (u(arg0) <= u(v1)):
                break
            while True:  # $label2
                v1 = (v1 + 1)
                store32((v4 + (v1 << 2)), load32((v4 + ((v1 + 1) << 2))))
                if (u(v1) < u(load32(v2 + 8))):
                    continue
                break
            break
        store32(v2 + 8, 0)
        break
    arg0 = load32(9568088)
    v1 = load32(load32(9568088) + 104)
    v2 = load32(arg0 + 88)
    v4 = load32(arg0 + 96)
    store32(v3, load32(arg0 + 80))
    store32(v3 + 4, v2)
    store32(v3 + 8, v4)
    store32(v3 + 12, v1)
    G.global0 = (v3 + 16)

# ------------------------------------------------------------
# $Yb
# Export: Yb
# ------------------------------------------------------------
def Yb(arg0):
    """Exported as Yb."""
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v2 = 3
    v1 = load32(9142892)
    if (u(load32(9142892)) >= u(3)):
        if (u(load32(9671136)) > u(3)):
            while True:  # $label2
                while True:  # block $label0
                    v1 = (load32(9671128) + (v2 * 132))
                    if (load8u((load32(9671128) + (v2 * 132)) + 125) == 3):
                        break
                    v3 = load16u(v1 + 110)
                    if (arg0 == load16u(v1 + 110)):
                        break
                    if (u(arg0) >= u(v3)):
                        break
                    v4 = (v3 - 1)
                    store16(v1 + 110, (v3 - 1))
                    store8(v1 + 127, 0)
                    while True:  # block $label1
                        v3 = load32(v1 + 40)
                        if (load32(v1 + 40) == 0):
                            break
                        if load8u(9142916):
                            store32(v5 + 20, v3)
                            store32(v5 + 16, 0)
                            a_b()
                            break
                        store32(v5 + 4, v3)
                        store32(v5, ((v4 & 65535) + 16))
                        a_b()
                        break
                    if (load32(((load8u(v1 + 122) * 404) + 9568096) + 20) == 0):
                        break
                    break
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(load32(9671136))):
                    continue
                break
            v1 = load32(9142892)
        v9 = (v1 - 1)
        if (u((v1 - 1)) >= u(2)):
            v4 = load32(9143004)
            v10 = (v1 & 1)
            v12 = (v1 - 3)
            v11 = (v1 - 2)
            v13 = ((v1 - 2) & -2)
            v3 = 1
            while True:  # $label4
                v6 = (v3 + (u(arg0) <= u(v3)))
                v8 = 0
                v2 = 1
                if v12:
                    while True:  # $label3
                        v7 = (v2 + 1)
                        store8((v4 + ((v1 * v2) + v3)), load8u((v4 + (v6 + ((v2 if (u(arg0) > u(v2)) else (v2 + 1)) * v1)))))
                        v2 = (v2 + 2)
                        store8((v4 + ((v1 * v7) + v3)), load8u((v4 + (v6 + ((v7 if (u(arg0) > u(v7)) else (v2 + 2)) * v1)))))
                        v8 = (v8 + 2)
                        if ((v8 + 2) != v13):
                            continue
                        break
                if v10:
                    store8((v4 + ((v1 * v2) + v3)), load8u((v4 + (v6 + ((v2 + (u(arg0) <= u(v2))) * v1)))))
                v3 = (v3 + 1)
                if ((v3 + 1) != v9):
                    continue
                break
            v10 = (v11 & -2)
            v11 = (v1 & 1)
            v4 = load32(9143012)
            v3 = 1
            while True:  # $label6
                v6 = (v3 + (u(arg0) <= u(v3)))
                v2 = 1
                v8 = 0
                if v12:
                    while True:  # $label5
                        v7 = (v2 + 1)
                        store8((v4 + ((v1 * v2) + v3)), load8u((v4 + (v6 + ((v2 if (u(arg0) > u(v2)) else (v2 + 1)) * v1)))))
                        v2 = (v2 + 2)
                        store8((v4 + ((v1 * v7) + v3)), load8u((v4 + (v6 + ((v7 if (u(arg0) > u(v7)) else (v2 + 2)) * v1)))))
                        v8 = (v8 + 2)
                        if ((v8 + 2) != v10):
                            continue
                        break
                if v11:
                    store8((v4 + ((v1 * v2) + v3)), load8u((v4 + (v6 + ((v2 + (u(arg0) <= u(v2))) * v1)))))
                v3 = (v3 + 1)
                if ((v3 + 1) != v9):
                    continue
                break
        store32(9142892, v9)
        if (u(arg0) < u(v9)):
            v3 = load32(9561692)
            v1 = arg0
            while True:  # $label7
                v2 = (v3 + (v1 * 286704))
                # TODO: memory.copy []
                store32(v2 + 283908, v1)
                v1 = (v1 + 1)
                v2 = load32(9142892)
                if (u((v1 + 1)) < u(load32(9142892))):
                    continue
                break
        else:
        func284(arg0)
    G.global0 = (v5 + 32)
    return 0

# ------------------------------------------------------------
# $Kc
# Export: Kc
# ------------------------------------------------------------
def Kc():
    """Exported as Kc."""
    v0 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v2 = 1
    if (u(load32(9142892)) > u(1)):
        while True:  # $label0
            v1 = (load32(9561692) + (v2 * 286704))
            v3 = load32((load32(9561692) + (v2 * 286704)) + 283908)
            v4 = load32(v1 + 284608)
            v5 = load8u((v1 + 283974))
            v6 = load8u((v1 + 283973))
            store32(v0 + 16, load8u(v1 + 283972))
            store32(v0 + 20, v6)
            store32(v0 + 24, v5)
            store32(v0, v2)
            store32(v0 + 4, v1)
            store32(v0 + 8, v4)
            store32(v0 + 12, (v3 == load32(9142872)))
            v2 = (v2 + 1)
            if (u((v2 + 1)) < u(load32(9142892))):
                continue
            break
    G.global0 = (v0 + 32)

# ------------------------------------------------------------
# $Ke
# Export: Ke
# ------------------------------------------------------------
def Ke():
    """Exported as Ke."""
    return load32(9681976)

# ------------------------------------------------------------
# $Sc
# Export: Sc
# ------------------------------------------------------------
def Sc(arg0):
    """Exported as Sc."""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = load32(9568088)
    v6 = ((load32(9568088) + 96) if arg0 else (v4 + 80))
    store32(9684424, ((load32(9568088) + 96) if arg0 else (v4 + 80)))
    v5 = load32(v6 + 8)
    if load32(v6 + 8):
        v7 = load32((v4 + (96 if arg0 else 80)))
        v8 = load32(9671128)
        v2 = v5
        while True:  # $label1
            if (load8u((v8 + (load32((v7 + (v1 << 2))) * 132)) + 125) == 3):
                v2 = (v2 - 1)
                store32(v6 + 8, (v2 - 1))
                arg0 = v1
                if (u(v1) < u(v2)):
                    while True:  # $label0
                        arg0 = (arg0 + 1)
                        store32((v7 + (arg0 << 2)), load32((v7 + ((arg0 + 1) << 2))))
                        v2 = load32(v6 + 8)
                        if (u(arg0) < u(load32(v6 + 8))):
                            continue
                        break
                v1 = (v1 - 1)
            v1 = (v1 + 1)
            if (u((v1 + 1)) < u(v2)):
                continue
            break
    if (v2 != v5):
        v1 = load32(v4 + 88)
        v5 = load32(v4 + 80)
        arg0 = load32(v4 + 96)
        store32(v3 + 12, load32(v4 + 104))
        store32(v3 + 8, arg0)
        store32(v3 + 4, v1)
        store32(v3, v5)
    G.global0 = (v3 + 16)

# ------------------------------------------------------------
# $Pc
# Export: Pc
# ------------------------------------------------------------
def Pc(arg0):
    """Exported as Pc."""
    v3 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # block $label2
        if (arg0 == 2):
            arg0 = load32(9568088)
            v2 = load32(load32(9568088) + 104)
            v1 = load32(arg0 + 88)
            v6 = load32(arg0 + 96)
            store32(v3, load32(arg0 + 80))
            store32(v3 + 4, v1)
            store32(v3 + 8, v6)
            store32(v3 + 12, v2)
            v2 = 0
            arg0 = (G.global0 - 32)
            G.global0 = (G.global0 - 32)
            v6 = load32(9684424)
            if load32(load32(9684424) + 8):
                while True:  # $label1
                    v1 = (load32(9671128) + (load32((load32(v6) + (v2 << 2))) * 132))
                    v4 = load32(((load8u(v1 + 122) * 404) + 9568096) + 156)
                    store8((load32(9671128) + (load32((load32(v6) + (v2 << 2))) * 132)) + 127, load32(((load8u(v1 + 122) * 404) + 9568096) + 156))
                    while True:  # block $label0
                        v5 = load32(v1 + 40)
                        if (load32(v1 + 40) == 0):
                            break
                        v1 = (v4 if v4 else (load16u(v1 + 110) + 16))
                        if load8u(9142916):
                            v4 = 0
                            if (u(v1) <= u(15)):
                                v1 = (v1 << 4)
                                v4 = ((((load32(((v1 << 4) + 1748)) << 8) + load32((v1 + 1744))) + (load32((v1 + 1752)) << 16)) + (load32((v1 + 1756)) << 24))
                            store32(arg0 + 20, v5)
                            store32(arg0 + 16, v4)
                            a_b()
                            break
                        store32(arg0 + 4, v5)
                        store32(arg0, v1)
                        a_b()
                        break
                    v2 = (v2 + 1)
                    if (u((v2 + 1)) < u(load32(v6 + 8))):
                        continue
                    break
            G.global0 = (arg0 + 32)
            break
        if (load32(9213808) == 0):
            break
        v2 = load32(9684424)
        if (arg0 == 0):
            while True:  # $label7
                v4 = load32(((v6 << 2) + 9173808))
                v7 = load32(9671128)
                while True:  # block $label3
                    v5 = load32(v2 + 8)
                    if (load32(v2 + 8) == 0):
                        break
                    v1 = load32(v2)
                    arg0 = 0
                    while True:  # $label4
                        if (v4 != load32((v1 + (arg0 << 2)))):
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != v5):
                                continue
                            break
                        break
                    if (arg0 < 0):
                        break
                    v5 = (v5 - 1)
                    store32(v2 + 8, (v5 - 1))
                    if (u(arg0) >= u(v5)):
                        break
                    while True:  # $label5
                        arg0 = (arg0 + 1)
                        store32((v1 + (arg0 << 2)), load32((v1 + ((arg0 + 1) << 2))))
                        if (u(arg0) < u(load32(v2 + 8))):
                            continue
                        break
                    break
                arg0 = (v7 + (v4 * 132))
                v1 = load32(((load8u(arg0 + 122) * 404) + 9568096) + 156)
                store8((v7 + (v4 * 132)) + 127, load32(((load8u(arg0 + 122) * 404) + 9568096) + 156))
                while True:  # block $label6
                    v4 = load32(arg0 + 40)
                    if (load32(arg0 + 40) == 0):
                        break
                    arg0 = (v1 if v1 else (load16u(arg0 + 110) + 16))
                    if load8u(9142916):
                        v1 = 0
                        if (u(arg0) <= u(15)):
                            arg0 = (arg0 << 4)
                            v1 = ((((load32(((arg0 << 4) + 1748)) << 8) + load32((arg0 + 1744))) + (load32((arg0 + 1752)) << 16)) + (load32((arg0 + 1756)) << 24))
                        store32(v3 + 36, v4)
                        store32(v3 + 32, v1)
                        a_b()
                        break
                    store32(v3 + 20, v4)
                    store32(v3 + 16, arg0)
                    a_b()
                    break
                v6 = (v6 + 1)
                if (u((v6 + 1)) < u(load32(9213808))):
                    continue
                break
                break
            raise RuntimeError('unreachable')
        while True:  # $label12
            v4 = load32(((v6 << 2) + 9173808))
            v7 = load32(9671128)
            while True:  # block $label8
                v1 = load32(v2 + 8)
                if load32(v2 + 8):
                    v5 = load32(v2)
                    arg0 = 0
                    while True:  # $label9
                        if (load32((v5 + (arg0 << 2))) == v4):
                            break
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != v1):
                            continue
                        break
                while True:  # block $label10
                    if (load32(v2 + 4) != v1):
                        arg0 = load32(v2)
                        break
                    arg0 = (load32(v2 + 12) + v1)
                    store32(v2 + 4, (load32(v2 + 12) + v1))
                    v5 = load32(v2)
                    arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                    if v1:
                        # TODO: memory.copy []
                    if v5:
                        v1 = load32(v2 + 8)
                    store32(v2, arg0)
                    break
                store32(v2 + 8, (v1 + 1))
                store32((arg0 + (v1 << 2)), v4)
                break
            while True:  # block $label11
                arg0 = load32((v7 + (v4 * 132)) + 40)
                if (load32((v7 + (v4 * 132)) + 40) == 0):
                    break
                if load8u(9142916):
                    store32(v3 + 68, arg0)
                    store32(v3 + 64, -16711936)
                    a_b()
                    break
                store32(v3 + 52, arg0)
                store32(v3 + 48, 0)
                a_b()
                break
            v6 = (v6 + 1)
            if (u((v6 + 1)) < u(load32(9213808))):
                continue
            break
        break
    G.global0 = (v3 + 80)

# ------------------------------------------------------------
# $Tc
# Export: Tc
# ------------------------------------------------------------
def Tc(arg0):
    """Exported as Tc."""
    arg0 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v1 = load32(9684424)
    if load32(load32(9684424) + 8):
        while True:  # $label1
            while True:  # block $label0
                v1 = load32((load32(9671128) + (load32((load32(v1) + (v2 << 2))) * 132)) + 40)
                if (load32((load32(9671128) + (load32((load32(v1) + (v2 << 2))) * 132)) + 40) == 0):
                    break
                if load8u(9142916):
                    store32(arg0 + 20, v1)
                    store32(arg0 + 16, -16711936)
                    a_b()
                    break
                store32(arg0 + 4, v1)
                store32(arg0, 0)
                a_b()
                break
            v2 = (v2 + 1)
            v1 = load32(9684424)
            if (u((v2 + 1)) < u(load32(load32(9684424) + 8))):
                continue
            break
    G.global0 = (arg0 + 32)

# ------------------------------------------------------------
# $Qb
# Export: Qb
# ------------------------------------------------------------
def Qb(arg0):
    """Exported as Qb."""
    store32(9142872, arg0)

# ------------------------------------------------------------
# $Ka
# Export: Ka
# ------------------------------------------------------------
def Ka(arg0):
    """Exported as Ka."""
    while True:  # block $label1
        while True:  # block $label0
            if arg0:
                if (load8u(9147212) == 0):
                    break
            v1 = load32(9142892)
            break
            break
        v1 = load32(41092)
        store32(9142892, load32(41092))
        break
    store32(41092, 1)
    store8(9147210, 0)
    store8(9142388, 0)
    store32(9142384, 0)
    while True:  # block $label2
        if arg0:
            break
        if (v1 == 0):
            break
        store32(9142892, 0)
        arg0 = load32(9561692)
        if load32(9561692):
            store32(9561692, 0)
        break

# ------------------------------------------------------------
# $Qe
# Export: Qe
# ------------------------------------------------------------
def Qe(arg0):
    """Exported as Qe."""
    store32(load32(9142424) + 48, (arg0 & 3))

# ------------------------------------------------------------
# $Xe
# Export: Xe
# ------------------------------------------------------------
def Xe(arg0):
    """Exported as Xe."""
    store32(9687276, arg0)
    if (arg0 == 0):
        la()

# ------------------------------------------------------------
# $Qa
# Export: Qa
# ------------------------------------------------------------
def Qa(arg0):
    """Exported as Qa."""
    v2 = 1
    while True:  # block $label0
        v3 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v4 = load32(9561692)
        v1 = 1
        while True:  # $label1
            if (arg0 != load32((v4 + (v1 * 286704)) + 284616)):
                v1 = (v1 + 1)
                if ((v1 + 1) != v3):
                    continue
                break
            break
        v2 = (load8u((load32(9143004) + (load32((v4 + (v1 * 286704)) + 283908) + (load32(9142872) * v3)))) != 0)
        break
    return v2

# ------------------------------------------------------------
# $Vc
# Export: Vc
# ------------------------------------------------------------
def Vc(arg0, arg1):
    """Exported as Vc."""
    v3 = (64 if arg1 else 48)
    while True:  # block $label0
        v2 = load32(9568088)
        v4 = ((load32(9568088) - -64) if arg1 else (v2 + 48))
        arg1 = load32(((load32(9568088) - -64) if arg1 else (v2 + 48)) + 8)
        if (u(arg0) < u(load32(((load32(9568088) - -64) if arg1 else (v2 + 48)) + 8))):
            v2 = load32((v2 + v3))
            break
        while True:  # block $label1
            v6 = load32(9142892)
            v7 = (load32(9142892) + 1)
            if (u((load32(9142892) + 1)) <= u(arg1)):
                v2 = load32((v2 + v3))
                break
            v3 = (v2 + v3)
            while True:  # $label3
                while True:  # block $label2
                    if (load32(v4 + 4) != arg1):
                        v2 = load32(v3)
                        break
                    v2 = (load32(v4 + 12) + arg1)
                    store32(v4 + 4, (load32(v4 + 12) + arg1))
                    v5 = load32(v3)
                    v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
                    if arg1:
                        # TODO: memory.copy []
                    if v5:
                        arg1 = load32(v4 + 8)
                    store32(v3, v2)
                    break
                store32(v4 + 8, (arg1 + 1))
                store32((v2 + (arg1 << 2)), 1)
                arg1 = load32(v4 + 8)
                if (u(load32(v4 + 8)) < u(v7)):
                    continue
                break
            break
        store32((v2 + (v6 << 2)), 0)
        break
    return load32((v2 + (arg0 << 2)))

# ------------------------------------------------------------
# $Uc
# Export: Uc
# ------------------------------------------------------------
def Uc(arg0, arg1, arg2):
    """Exported as Uc."""
    v9 = (64 if arg2 else 48)
    v5 = load32(9568088)
    v3 = ((load32(9568088) - -64) if arg2 else (v5 + 48))
    arg2 = load32(((load32(9568088) - -64) if arg2 else (v5 + 48)) + 8)
    v6 = (load32(9142892) + 1)
    if (u(load32(((load32(9568088) - -64) if arg2 else (v5 + 48)) + 8)) < u((load32(9142892) + 1))):
        v7 = (v5 + v9)
        while True:  # $label1
            while True:  # block $label0
                if (load32(v3 + 4) != arg2):
                    v4 = load32(v7)
                    break
                v4 = (load32(v3 + 12) + arg2)
                store32(v3 + 4, (load32(v3 + 12) + arg2))
                v8 = load32(v7)
                v4 = func26((-1 if (u(v4) > u(1073741823)) else (v4 << 2)))
                if arg2:
                    # TODO: memory.copy []
                if v8:
                    arg2 = load32(v3 + 8)
                store32(v7, v4)
                break
            store32(v3 + 8, (arg2 + 1))
            store32((v4 + (arg2 << 2)), 1)
            arg2 = load32(v3 + 8)
            if (u(load32(v3 + 8)) < u(v6)):
                continue
            break
    if (u(arg2) > u(v6)):
        store32(v3 + 8, v6)
    store32((load32((v5 + v9)) + (arg0 << 2)), arg1)

# ------------------------------------------------------------
# $Bd
# Export: Bd
# ------------------------------------------------------------
def Bd(arg0, arg1):
    """Exported as Bd."""
    store32((load32(load32(9568088) + 80) + (arg0 << 2)), arg1)

# ------------------------------------------------------------
# $Dd
# Export: Dd
# ------------------------------------------------------------
def Dd(arg0, arg1):
    """Exported as Dd."""
    store32((load32(load32(9568088) + 96) + (arg0 << 2)), arg1)

# ------------------------------------------------------------
# $Wc
# Export: Wc
# ------------------------------------------------------------
def Wc(arg0):
    """Exported as Wc."""
    v1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v2 = load32(9568088)
    store64(load32(9568088) + 4, 0)
    store32(v2, arg0)
    store64(v2 + 36, 0)
    store64(v2 + 28, 0)
    store64(v2 + 20, 0)
    store64(v2 + 12, 0)
    store32(v2 + 104, 0)
    store32(v2 + 88, 0)
    store32(v2 + 72, 0)
    store32(v2 + 56, 0)
    v3 = load8u(v2 + 45)
    v4 = load8u(v2 + 44)
    v5 = load32(v2 + 96)
    store32(v1 + 40, load32(v2 + 80))
    store64(v1 + 16, 0)
    store64(v1 + 24, 0)
    store64(v1 + 32, 0)
    store32(v1 + 44, 0)
    store32(v1 + 48, v5)
    store32(v1 + 56, v4)
    store32(v1 + 60, v3)
    store32(v1 + 52, load32(9684428))
    store32(v1, arg0)
    store32(v1 + 4, 0)
    store64(v1 + 8, 0)
    a_b()
    G.global0 = (v1 - -64)

# ------------------------------------------------------------
# $Ie
# Export: Ie
# ------------------------------------------------------------
def Ie(arg0, arg1, arg2, arg3):
    """Exported as Ie."""
    while True:  # block $label1
        while True:  # block $label2
            while True:  # block $label0
                # br_table[arg3]
                break
                break
            arg3 = load32(9143004)
            v4 = load32(9142892)
            arg0 = (arg0 != 0)
            store8((load32(9143004) + ((load32(9142892) * arg1) + arg2)), (arg0 != 0))
            store8((arg3 + ((arg2 * v4) + arg1)), arg0)
            return
            break
        store8((load32(9143012) + ((load32(9142892) * arg1) + arg2)), (arg0 != 0))
        break

# ------------------------------------------------------------
# $Z
# Export: Z
# ------------------------------------------------------------
def Z(arg0, arg1):
    """Exported as Z."""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg0 = (load32(9561692) + (arg0 * 286704))
    arg1 = ((load32(arg0 + 283960) + arg1) & 3)
    store32((load32(9561692) + (arg0 * 286704)) + 283960, ((load32(arg0 + 283960) + arg1) & 3))
    if load8u(9147210):
        store32(v2, load32(arg0 + 283908))
        store32(v2 + 4, ((load8u((arg0 + 283974)) | (load8u((arg0 + 283973)) << 8)) | (load8u(arg0 + 283972) << 16)))
        store32(v2 + 8, load32(arg0 + 284608))
        arg0 = (arg0 + 283960)
        store32(v2 + 12, load32((arg0 + 283960)))
        func71(16, 0, 0, v2, 4, 1)
        arg1 = load32(arg0)
    G.global0 = (v2 + 16)
    return arg1

# ------------------------------------------------------------
# $Y
# Export: Y
# ------------------------------------------------------------
def Y(arg0, arg1):
    """Exported as Y."""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        v5 = load32(9561692)
        v3 = (load32(9561692) + (arg0 * 286704))
        v6 = load32((load32(9561692) + (arg0 * 286704)) + 284608)
        if ((load32((load32(9561692) + (arg0 * 286704)) + 284608) == 0) & (arg1 < 0)):
            break
        v3 = (v3 + 284608)
        v4 = ((arg1 + v6) % 17)
        store32((v3 + 284608), ((arg1 + v6) % 17))
        if (load8u(9147210) == 0):
            break
        arg0 = (v5 + (arg0 * 286704))
        store32(v2, load32((v5 + (arg0 * 286704)) + 283908))
        store32(v2 + 4, ((load8u((arg0 + 283974)) | (load8u((arg0 + 283973)) << 8)) | (load8u(arg0 + 283972) << 16)))
        store32(v2 + 8, load32(v3))
        store32(v2 + 12, load32(arg0 + 283960))
        func71(16, 0, 0, v2, 4, 1)
        v4 = load32(v3)
        break
    G.global0 = (v2 + 16)
    return v4

# ------------------------------------------------------------
# $Md
# Export: Md
# ------------------------------------------------------------
def Md(arg0, arg1):
    """Exported as Md."""
    while True:  # block $label0
        if arg0:
            break
        if load8u(9147210):
            break
        arg1 = load32(9561692)
        v3 = load32(9142872)
        arg0 = (load32(9561692) + (load32(9142872) * 286704))
        v2 = load32((load32(9561692) + (load32(9142872) * 286704)) + 283848)
        if (load32((load32(9561692) + (load32(9142872) * 286704)) + 283848) != 2147483647):
            store32((arg0 + 283848), (v2 + 50000))
        arg0 = (arg0 + 283852)
        v2 = load32((arg0 + 283852))
        if (load32((arg0 + 283852)) != 2147483647):
            store32(arg0, (v2 + 50000))
        arg0 = (arg1 + (v3 * 286704))
        v2 = ((arg1 + (v3 * 286704)) + 283856)
        v4 = load32(((arg1 + (v3 * 286704)) + 283856))
        if (load32(((arg1 + (v3 * 286704)) + 283856)) != 2147483647):
            store32(v2, (v4 + 50000))
        arg0 = (arg0 + 283860)
        v2 = load32((arg0 + 283860))
        if (load32((arg0 + 283860)) != 2147483647):
            store32(arg0, (v2 + 50000))
        arg0 = 1
        v3 = (arg1 + (v3 * 286704))
        store8((arg1 + (v3 * 286704)) + 286701, 1)
        arg1 = load32(9142892)
        if (u(load32(9142892)) < u(2)):
            break
        v5 = (arg1 - 1)
        v6 = ((arg1 - 1) & 1)
        v3 = (load32(v3 + 283908) * arg1)
        v2 = load32(9561692)
        v4 = load32(9143016)
        if (arg1 != 2):
            v5 = (v5 & -2)
            arg1 = 0
            while True:  # $label1
                if load8u((v4 + (arg0 + v3))):
                    store8((v2 + (arg0 * 286704)) + 286701, 1)
                v7 = (arg0 + 1)
                if load8u((v4 + ((arg0 + 1) + v3))):
                    store8((v2 + (v7 * 286704)) + 286701, 1)
                arg0 = (arg0 + 2)
                arg1 = (arg1 + 2)
                if ((arg1 + 2) != v5):
                    continue
                break
        if (v6 == 0):
            break
        if (load8u((v4 + (arg0 + v3))) == 0):
            break
        store8((v2 + (arg0 * 286704)) + 286701, 1)
        break

# ------------------------------------------------------------
# $Bc
# Export: Bc
# ------------------------------------------------------------
def Bc(arg0, arg1, arg2, arg3, arg4):
    """Exported as Bc."""
    v5 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    if (load8u(9142916) == 0):
        store32(v5 + 32, arg3)
        # TODO: f64.promote_f32 []
        store32(v5 + 24, arg4)
        # TODO: f64.promote_f32 []
        store32(v5 + 16, arg2)
        # TODO: f64.promote_f32 []
        store32(v5 + 8, arg1)
        # TODO: f64.promote_f32 []
        store32(v5, arg0)
        a_b()
    G.global0 = (v5 + 48)

# ------------------------------------------------------------
# $M
# Export: M
# ------------------------------------------------------------
def M(arg0):
    """Exported as M."""
    v2 = func26(arg0)
    while True:  # block $label0
        if (arg0 == 0):
            break
        v4 = (arg0 & 3)
        if (u(arg0) >= u(4)):
            v5 = (arg0 & 65532)
            arg0 = 0
            while True:  # $label1
                store8((v1 + v2), (load32(((v1 << 2) + 9147392)) != 0))
                v3 = (v1 | 1)
                store8((v2 + (v1 | 1)), (load32(((v3 << 2) + 9147392)) != 0))
                v3 = (v1 | 2)
                store8((v2 + (v1 | 2)), (load32(((v3 << 2) + 9147392)) != 0))
                v3 = (v1 | 3)
                store8((v2 + (v1 | 3)), (load32(((v3 << 2) + 9147392)) != 0))
                v1 = (v1 + 4)
                arg0 = (arg0 + 4)
                if ((arg0 + 4) != v5):
                    continue
                break
        if (v4 == 0):
            break
        while True:  # $label2
            store8((v1 + v2), (load32(((v1 << 2) + 9147392)) != 0))
            v1 = (v1 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v4):
                continue
            break
        break
    return v2

# ------------------------------------------------------------
# $Xd
# Export: Xd
# ------------------------------------------------------------
def Xd():
    """Exported as Xd."""
    while True:  # $label1
        v2 = ((v0 * 404) + 9568096)
        if (load32(((v0 * 404) + 9568096) + 264) == 1):
            v1 = ((load32(v2 + 244) + ((load32(v2 + 364) + (v1 + load32(v2 + 236))) + (load32(v2 + 220) * load32(v2 + 216)))) + 55)
            v3 = 0
            while True:  # $label0
                v2 = (((v0 * 1020) + 9299904) + (v3 << 2))
                v1 = (v1 if (load32((((v0 * 1020) + 9299904) + (v3 << 2))) == 100) else (v1 + 2))
                v1 = ((v1 if (load32((((v0 * 1020) + 9299904) + (v3 << 2))) == 100) else (v1 + 2)) if (load32(v2 + 4) == 100) else (v1 + 2))
                v1 = (((v1 if (load32((((v0 * 1020) + 9299904) + (v3 << 2))) == 100) else (v1 + 2)) if (load32(v2 + 4) == 100) else (v1 + 2)) if (load32(v2 + 8) == 100) else (v1 + 2))
                v3 = (v3 + 3)
                if ((v3 + 3) != 255):
                    continue
                break
            v7 = (v7 + 1)
        v0 = (v0 + 1)
        if ((v0 + 1) != 255):
            continue
        break
    v2 = load32(9685864)
    if load32(9685864):
        store32(9685864, 0)
    v3 = (v7 * 55)
    v7 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
    store32(9685864, func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2))))
    while True:  # $label20
        v0 = 0
        v1 = 0
        v2 = ((v11 * 404) + 9568096)
        if (load32(((v11 * 404) + 9568096) + 264) == 1):
            while True:  # $label2
                v12 = ((v11 * 1020) + 9299904)
                v1 = (((v11 * 1020) + 9299904) + (v0 << 2))
                v5 = (v1 if (load32((((v11 * 1020) + 9299904) + (v0 << 2))) == 100) else (v1 + 2))
                v5 = ((v1 if (load32((((v11 * 1020) + 9299904) + (v0 << 2))) == 100) else (v1 + 2)) if (load32(v1 + 4) == 100) else (v5 + 2))
                v1 = (((v1 if (load32((((v11 * 1020) + 9299904) + (v0 << 2))) == 100) else (v1 + 2)) if (load32(v1 + 4) == 100) else (v5 + 2)) if (load32(v1 + 8) == 100) else (v5 + 2))
                v0 = (v0 + 3)
                if ((v0 + 3) != 255):
                    continue
                break
            v6 = load32(v2 + 104)
            v8 = load32(v2 + 68)
            v9 = load32(v2 + 72)
            v10 = load32(v2 + 76)
            v14 = load32(v2 + 80)
            v15 = load32(v2 + 116)
            v16 = load32(v2 + 236)
            v17 = load32(v2 + 92)
            v18 = load32(v2 + 276)
            v19 = load32(v2 + 96)
            v20 = load32(v2 + 224)
            v21 = load32(v2 + 204)
            v22 = load32(v2 + 200)
            v23 = load32(v2 + 228)
            v24 = load32(v2 + 208)
            v5 = load32(v2 + 220)
            v4 = load32(v2 + 216)
            v25 = load32(v2 + 192)
            v26 = load32(v2 + 188)
            v27 = load32(v2 + 84)
            v28 = load32(v2 + 136)
            v29 = load32(v2 + 140)
            v30 = load32(v2 + 176)
            v31 = load32(v2 + 112)
            v32 = load32(v2 + 364)
            v33 = load32(v2 + 272)
            v34 = load32(v2 + 212)
            v35 = load32(v2 + 280)
            v36 = load32(v2 + 328)
            v37 = load8u(v2 + 332)
            v38 = load8u(v2 + 353)
            v39 = load8u(v2 + 335)
            v40 = load8u(v2 + 336)
            v49 = load64(v2 + 284)
            v50 = load64(v2 + 292)
            v41 = load32(v2 + 300)
            v42 = load32(v2 + 308)
            v43 = load32(v2 + 312)
            v44 = load32(v2 + 324)
            v45 = load32(v2 + 320)
            v46 = load32(v2 + 340)
            v47 = load32(v2 + 344)
            v48 = load8u(v2 + 354)
            v0 = (v7 + (v13 * 220))
            store32((v7 + (v13 * 220)) + 192, load32(v2 + 244))
            store32(v0 + 188, v48)
            store32(v0 + 184, v47)
            store32(v0 + 180, v46)
            store32(v0 + 176, v45)
            store32(v0 + 172, v44)
            store32(v0 + 168, v43)
            store32(v0 + 164, v42)
            store32(v0 + 160, v41)
            store64(v0 + 152, v50)
            store64(v0 + 144, v49)
            store32(v0 + 140, v40)
            store32(v0 + 136, v39)
            store32(v0 + 132, v38)
            store32(v0 + 128, v37)
            store32(v0 + 124, v36)
            store32(v0 + 120, v35)
            store32(v0 + 116, v1)
            store32(v0 + 112, v34)
            store32(v0 + 108, v33)
            store32(v0 + 104, v32)
            store32(v0 + 100, v31)
            store32(v0 + 96, v30)
            store32(v0 + 92, v29)
            store32(v0 + 88, v28)
            store32(v0 + 84, v27)
            store32(v0 + 80, v26)
            store32(v0 + 76, v25)
            store32(v0 + 72, (v4 * v5))
            store32(v0 + 68, v5)
            store32(v0 + 64, v4)
            store32(v0 + 60, v24)
            store32(v0 + 56, v23)
            store32(v0 + 52, v22)
            store32(v0 + 48, v21)
            store32(v0 + 44, v20)
            store32(v0 + 40, v19)
            store32(v0 + 36, v18)
            store32(v0 + 32, v17)
            store32(v0 + 28, v16)
            store32(v0 + 24, v15)
            store32(v0 + 20, v14)
            store32(v0 + 16, v10)
            store32(v0 + 12, v9)
            store32(v0 + 8, v8)
            store32(v0 + 4, v6)
            store32(v0, v11)
            store64(v0 + 212, 0)
            store64(v0 + 204, 0)
            store64(v0 + 196, 0)
            while True:  # block $label3
                v1 = load32(v2 + 236)
                if (load32(v2 + 236) == 0):
                    break
                v9 = (v1 & 3)
                v4 = load32(v2 + 232)
                v0 = 0
                while True:  # block $label4
                    if (u(v1) < u(4)):
                        v1 = 0
                        break
                    v10 = (v1 & -4)
                    v1 = 0
                    v5 = 0
                    while True:  # $label5
                        v6 = (v7 + (v3 << 2))
                        v8 = (v1 << 2)
                        store32((v7 + (v3 << 2)), load32((v4 + (v1 << 2))))
                        store32(v6 + 4, load32((v4 + (v8 | 4))))
                        store32(v6 + 8, load32((v4 + (v8 | 8))))
                        store32(v6 + 12, load32((v4 + (v8 | 12))))
                        v1 = (v1 + 4)
                        v3 = (v3 + 4)
                        v5 = (v5 + 4)
                        if ((v5 + 4) != v10):
                            continue
                        break
                    break
                if (v9 == 0):
                    break
                while True:  # $label6
                    store32((v7 + (v3 << 2)), load32((v4 + (v1 << 2))))
                    v1 = (v1 + 1)
                    v3 = (v3 + 1)
                    v0 = (v0 + 1)
                    if ((v0 + 1) != v9):
                        continue
                    break
                break
            while True:  # block $label7
                v1 = (load32(v2 + 220) * load32(v2 + 216))
                if ((load32(v2 + 220) * load32(v2 + 216)) == 0):
                    break
                v8 = (v1 & 3)
                v4 = load32(v2 + 372)
                v5 = 0
                while True:  # block $label8
                    if (u(v1) < u(4)):
                        v1 = 0
                        break
                    v9 = (v1 & -4)
                    v1 = 0
                    v0 = 0
                    while True:  # $label9
                        v6 = (v7 + (v3 << 2))
                        store32((v7 + (v3 << 2)), load8u((v1 + v4)))
                        store32(v6 + 4, load8u((v4 + (v1 | 1))))
                        store32(v6 + 8, load8u((v4 + (v1 | 2))))
                        store32(v6 + 12, load8u((v4 + (v1 | 3))))
                        v1 = (v1 + 4)
                        v3 = (v3 + 4)
                        v0 = (v0 + 4)
                        if ((v0 + 4) != v9):
                            continue
                        break
                    break
                if (v8 == 0):
                    break
                while True:  # $label10
                    store32((v7 + (v3 << 2)), load8u((v1 + v4)))
                    v1 = (v1 + 1)
                    v3 = (v3 + 1)
                    v5 = (v5 + 1)
                    if ((v5 + 1) != v8):
                        continue
                    break
                break
            while True:  # block $label11
                v1 = load32(v2 + 364)
                if (load32(v2 + 364) == 0):
                    break
                v9 = (v1 & 3)
                v4 = load32(v2 + 24)
                v0 = 0
                while True:  # block $label12
                    if (u(v1) < u(4)):
                        v1 = 0
                        break
                    v10 = (v1 & -4)
                    v1 = 0
                    v5 = 0
                    while True:  # $label13
                        v6 = (v7 + (v3 << 2))
                        v8 = (v1 << 2)
                        store32((v7 + (v3 << 2)), load32((v4 + (v1 << 2))))
                        store32(v6 + 4, load32((v4 + (v8 | 4))))
                        store32(v6 + 8, load32((v4 + (v8 | 8))))
                        store32(v6 + 12, load32((v4 + (v8 | 12))))
                        v1 = (v1 + 4)
                        v3 = (v3 + 4)
                        v5 = (v5 + 4)
                        if ((v5 + 4) != v10):
                            continue
                        break
                    break
                if (v9 == 0):
                    break
                while True:  # $label14
                    store32((v7 + (v3 << 2)), load32((v4 + (v1 << 2))))
                    v1 = (v1 + 1)
                    v3 = (v3 + 1)
                    v0 = (v0 + 1)
                    if ((v0 + 1) != v9):
                        continue
                    break
                break
            v1 = 0
            while True:  # $label15
                v0 = load32((v12 + (v1 << 2)))
                if (load32((v12 + (v1 << 2))) != 100):
                    v5 = (v7 + (v3 << 2))
                    store32((v7 + (v3 << 2)), v1)
                    store32(v5 + 4, v0)
                    v3 = (v3 + 2)
                v0 = (v1 | 1)
                if ((v1 | 1) != 255):
                    v5 = load32((v12 + (v0 << 2)))
                    if (load32((v12 + (v0 << 2))) != 100):
                        v4 = (v7 + (v3 << 2))
                        store32((v7 + (v3 << 2)), v0)
                        store32(v4 + 4, v5)
                        v3 = (v3 + 2)
                    v1 = (v1 + 2)
                    continue
                break
            while True:  # block $label16
                v1 = load32(v2 + 244)
                if (load32(v2 + 244) == 0):
                    break
                v6 = (v1 & 3)
                v2 = load32(v2 + 240)
                v8 = 0
                while True:  # block $label17
                    if (u(v1) < u(4)):
                        v1 = 0
                        break
                    v12 = (v1 & -4)
                    v1 = 0
                    v5 = 0
                    while True:  # $label18
                        v0 = (v7 + (v3 << 2))
                        v4 = (v1 << 2)
                        store32((v7 + (v3 << 2)), load32((v2 + (v1 << 2))))
                        store32(v0 + 4, load32((v2 + (v4 | 4))))
                        store32(v0 + 8, load32((v2 + (v4 | 8))))
                        store32(v0 + 12, load32((v2 + (v4 | 12))))
                        v1 = (v1 + 4)
                        v3 = (v3 + 4)
                        v5 = (v5 + 4)
                        if ((v5 + 4) != v12):
                            continue
                        break
                    break
                if (v6 == 0):
                    break
                while True:  # $label19
                    store32((v7 + (v3 << 2)), load32((v2 + (v1 << 2))))
                    v1 = (v1 + 1)
                    v3 = (v3 + 1)
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v6):
                        continue
                    break
                break
            v13 = (v13 + 1)
        v11 = (v11 + 1)
        if ((v11 + 1) != 255):
            continue
        break
    return (v13 * 55)

# ------------------------------------------------------------
# $Yc
# Export: Yc
# ------------------------------------------------------------
def Yc(arg0):
    """Exported as Yc."""
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    store8(59183, arg0)
    while True:  # block $label1
        if (arg0 == 0):
            arg0 = load32(9142876)
            while True:  # block $label0
                if load8u(9142916):
                    store32(v1 + 32, arg0)
                    a_b()
                    break
                store32(v1 + 24, arg0)
                store64(v1 + 16, -4602115869219225600)
                store64(v1 + 8, 0)
                store64(v1, 0)
                a_b()
                break
            store8(9684432, 0)
            break
        break
    arg0 = load32(load32(9568088) + 28)
    G.global0 = (v1 + 48)
    return arg0

# ------------------------------------------------------------
# $Ed
# Export: Ed
# ------------------------------------------------------------
def Ed(arg0, arg1):
    """Exported as Ed."""
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(9568088)
    while True:  # block $label0
        if arg1:
            arg0 = load32(v2 + 80)
            store32(v4 + 4, load32(v2 + 88))
            store32(v4, arg0)
            break
        store32(v2 + 88, 0)
        arg1 = load32(v2 + 84)
        if (u(arg0) >= u(load32(v2 + 84))):
            arg1 = (load32(v2 + 92) + (arg0 + arg1))
            store32(v2 + 84, (load32(v2 + 92) + (arg0 + arg1)))
            v3 = load32(v2 + 80)
            arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
            if v3:
            store32(v2 + 80, arg1)
        if (arg0 == 0):
            break
        v7 = (arg0 & 1)
        v3 = load32(v2 + 80)
        arg1 = 0
        if (arg0 != 1):
            v8 = (arg0 & -2)
            arg0 = 0
            while True:  # $label1
                v5 = (arg1 << 2)
                v6 = load32(((arg1 << 2) + 9147392))
                v9 = load32(v2 + 88)
                store32(v2 + 88, (load32(v2 + 88) + 1))
                store32((v3 + (v9 << 2)), v6)
                v5 = load32(((v5 | 4) + 9147392))
                v6 = load32(v2 + 88)
                store32(v2 + 88, (load32(v2 + 88) + 1))
                store32((v3 + (v6 << 2)), v5)
                arg1 = (arg1 + 2)
                arg0 = (arg0 + 2)
                if ((arg0 + 2) != v8):
                    continue
                break
        if (v7 == 0):
            break
        arg0 = load32(((arg1 << 2) + 9147392))
        arg1 = load32(v2 + 88)
        store32(v2 + 88, (load32(v2 + 88) + 1))
        store32((v3 + (arg1 << 2)), arg0)
        break
    G.global0 = (v4 + 16)