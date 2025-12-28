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
# $func350
# ------------------------------------------------------------
def func350():
    v0 = load32(9142440)
    if load32(9142440):
        v4 = load32(9147288)
        v16 = v0
        while True:  # $label2
            v2 = (v1 + 1)
            v3 = load32(9142840)
            v6 = load32(9140332)
            v0 = 0
            while True:  # $label1
                while True:  # block $label0
                    v5 = load8s((v4 + ((v0 * v16) + v1)))
                    if (load8s((v4 + ((v0 * v16) + v1))) < 0):
                        break
                    if (load32(load32((v6 + ((v5 & 255) << 2))) + 32) != 23):
                        break
                    v5 = (v0 + 1)
                    store32((v3 + ((((v0 + 1) * (v16 + 2)) + v2) << 2)), 1)
                    v16 = (load32(9142440) + 2)
                    store32((v3 + ((((v5 + (load32(9142440) + 2)) * v16) + v2) << 2)), 1)
                    v16 = load32(9142440)
                    break
                v0 = (v0 + 1)
                if (u((v0 + 1)) < u(v16)):
                    continue
                break
            v1 = v2
            if (u(v2) < u(v16)):
                continue
            break
    v11 = load32(9142424)
    v0 = load32(load32(9142424) + 164)
    if (load32(load32(9142424) + 164) == 0):
        store32(v11 + 164, 100)
        v0 = 100
    v1 = ((load32(38448) * 404) + 9568096)
    store32(((load32(38448) * 404) + 9568096) + 104, v0)
    store32(v1 + 108, load32(v11 + 164))
    v17 = (v16 * v16)
    v15 = load32(v11 + 116)
    while True:  # block $label25
        while True:  # block $label69
            while True:  # block $label68
                while True:  # block $label67
                    while True:  # block $label63
                        while True:  # block $label3
                            while True:  # block $label4
                                if load32(v11 + 68):
                                    v0 = load32(9142892)
                                    if (u(load32(9142892)) < u(2)):
                                        break
                                    v1 = (v0 - 1)
                                    v4 = ((v0 - 1) & 3)
                                    v3 = 0
                                    v6 = load32(9561692)
                                    if (u((v0 - 2)) < u(3)):
                                        v2 = 1
                                        break
                                    v5 = (v1 & -4)
                                    v2 = 1
                                    while True:  # $label5
                                        v1 = (v6 + (v2 * 286704))
                                        v7 = load32(((v6 + (v2 * 286704)) + 1144720))
                                        v8 = load32((v1 + 858016))
                                        v10 = load32((v1 + 571312))
                                        v1 = load32(v1 + 284608)
                                        v1 = (load32(v1 + 284608) if (u(v1) > u(v12)) else v12)
                                        v1 = (load32((v1 + 571312)) if (u(v1) < u(v10)) else (load32(v1 + 284608) if (u(v1) > u(v12)) else v12))
                                        v1 = (load32((v1 + 858016)) if (u(v1) < u(v8)) else (load32((v1 + 571312)) if (u(v1) < u(v10)) else (load32(v1 + 284608) if (u(v1) > u(v12)) else v12)))
                                        v12 = (load32(((v6 + (v2 * 286704)) + 1144720)) if (u(v1) < u(v7)) else (load32((v1 + 858016)) if (u(v1) < u(v8)) else (load32((v1 + 571312)) if (u(v1) < u(v10)) else (load32(v1 + 284608) if (u(v1) > u(v12)) else v12))))
                                        v2 = (v2 + 4)
                                        v9 = (v9 + 4)
                                        if ((v9 + 4) != v5):
                                            continue
                                        break
                                    break
                                while True:  # block $label6
                                    if load32(v11 + 64):
                                        v7 = 1
                                        # TODO: f32.convert_i32_u []
                                        v33 = (((v16 & 0xFFFFFFFF) >> 1) - 37)
                                        v34 = (((((v16 & 0xFFFFFFFF) >> 1) - 37) * 3.14159274) * v33)
                                        v1 = load32(9142416)
                                        v0 = load32(9142892)
                                        v2 = (load32(9142892) - 1)
                                        v1 = (load32(9142416) if v1 else (load32(41092) if load8u(9147210) else (load32(9142892) - 1)))
                                        # TODO: f32.convert_i32_u []
                                        v37 = (4 if (u(v1) < u(3)) else ((load32(9142416) if v1 else (load32(41092) if load8u(9147210) else (load32(9142892) - 1))) << (v1 & 1)))
                                        v33 = (v33 + -15.0)
                                        # TODO: f32.convert_i32_u []
                                        v36 = (6.28318548 / v2)
                                        v38 = ((6.28318548 / v2) * 0.5)
                                        v9 = load8u(9147127)
                                        if (u(v0) < u(2)):
                                            break
                                        v2 = load32(9561692)
                                        v6 = load32(9561692)
                                        v11 = 1
                                        while True:  # $label14
                                            while True:  # block $label7
                                                if v9:
                                                    if (load32((v6 + (v11 * 286704)) + 284608) != 1):
                                                        break
                                                while True:  # block $label8
                                                    # TODO: f32.convert_i32_u []
                                                    v35 = ((v36 * (v7 - 1)) + v38)
                                                    # TODO: f32.convert_i32_u []
                                                    v39 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                                                    v40 = ((v33 * func48(((v36 * (v7 - 1)) + v38))) + ((load32(9142440) & 0xFFFFFFFF) >> 1))
                                                    if (abs(((v33 * func48(((v36 * (v7 - 1)) + v38))) + ((load32(9142440) & 0xFFFFFFFF) >> 1))) < 2147483650.0):
                                                        break
                                                    break
                                                v4 = -2147483648
                                                while True:  # block $label10
                                                    while True:  # block $label9
                                                        v35 = ((v33 * func49(v35)) + v39)
                                                        if (abs(((v33 * func49(v35)) + v39)) < 2147483650.0):
                                                            break
                                                        break
                                                    v12 = -2147483648
                                                    v1 = (-2147483648 - 25)
                                                    v8 = (v12 + 50)
                                                    if ((-2147483648 - 25) >= (v12 + 50)):
                                                        break
                                                    v3 = (v4 - 25)
                                                    v10 = (v4 + 50)
                                                    if ((v4 - 25) >= (v4 + 50)):
                                                        break
                                                    while True:  # $label13
                                                        v2 = (v1 + 1)
                                                        v0 = (v1 - v12)
                                                        v13 = (((v1 - v12) * v0) - 1)
                                                        v0 = v3
                                                        while True:  # $label12
                                                            while True:  # block $label11
                                                                v5 = (v0 - v4)
                                                                if ((v13 + ((v0 - v4) * v5)) > 625):
                                                                    break
                                                                v5 = load32(9142440)
                                                                if (u(load32(9142440)) <= u(v0)):
                                                                    break
                                                                if ((v0 | v1) < 0):
                                                                    break
                                                                if (u(v1) >= u(v5)):
                                                                    break
                                                                v5 = (load32(9147288) + ((v0 * v5) + v1))
                                                                v17 = load8s((load32(9147288) + ((v0 * v5) + v1)))
                                                                if (load8s((load32(9147288) + ((v0 * v5) + v1))) < 0):
                                                                    break
                                                                if (load32(load32((load32(9140332) + ((v17 & 255) << 2))) + 32) != 23):
                                                                    break
                                                                store8(v5, load32(9147292))
                                                                v5 = load32(9142840)
                                                                v17 = (v0 + 1)
                                                                store32((load32(9142840) + ((((v0 + 1) * (load32(9142440) + 2)) + v2) << 2)), 0)
                                                                v15 = (load32(9142440) + 2)
                                                                store32((v5 + ((((v17 + (load32(9142440) + 2)) * v15) + v2) << 2)), 0)
                                                                break
                                                            v0 = (v0 + 1)
                                                            if ((v0 + 1) != v10):
                                                                continue
                                                            break
                                                        v1 = v2
                                                        if (v2 != v8):
                                                            continue
                                                        break
                                                    v2 = load32(9561692)
                                                    break
                                                v7 = (v7 + 1)
                                                v0 = (v6 + (v11 * 286704))
                                                store32((v6 + (v11 * 286704)) + 283900, v4)
                                                store32(v0 + 283896, v12)
                                                store32(v0 + 283876, v4)
                                                store32(v0 + 283872, v12)
                                                v0 = load32(9142892)
                                                v6 = v2
                                                break
                                            v11 = (v11 + 1)
                                            if (u((v11 + 1)) < u(v0)):
                                                continue
                                            break
                                        break
                                    while True:  # block $label24
                                        while True:  # block $label15
                                            v20 = load32(v11 + 168)
                                            if (load32(v11 + 168) == 0):
                                                break
                                            while True:  # block $label20
                                                while True:  # block $label16
                                                    v2 = load32(9142892)
                                                    if (u(load32(9142892)) < u(2)):
                                                        break
                                                    v0 = (v2 - 1)
                                                    v4 = ((v2 - 1) & 3)
                                                    v3 = 0
                                                    v6 = load32(9561692)
                                                    while True:  # block $label17
                                                        if (u((v2 - 2)) < u(3)):
                                                            v0 = 1
                                                            break
                                                        v12 = (v0 & -4)
                                                        v0 = 1
                                                        while True:  # $label18
                                                            v1 = (v6 + (v0 * 286704))
                                                            v9 = load32(((v6 + (v0 * 286704)) + 1144720))
                                                            v5 = load32((v1 + 858016))
                                                            v11 = load32((v1 + 571312))
                                                            v1 = load32(v1 + 284608)
                                                            v1 = (load32(v1 + 284608) if (u(v1) > u(v8)) else v8)
                                                            v1 = (load32((v1 + 571312)) if (u(v1) < u(v11)) else (load32(v1 + 284608) if (u(v1) > u(v8)) else v8))
                                                            v1 = (load32((v1 + 858016)) if (u(v1) < u(v5)) else (load32((v1 + 571312)) if (u(v1) < u(v11)) else (load32(v1 + 284608) if (u(v1) > u(v8)) else v8)))
                                                            v8 = (load32(((v6 + (v0 * 286704)) + 1144720)) if (u(v1) < u(v9)) else (load32((v1 + 858016)) if (u(v1) < u(v5)) else (load32((v1 + 571312)) if (u(v1) < u(v11)) else (load32(v1 + 284608) if (u(v1) > u(v8)) else v8))))
                                                            v0 = (v0 + 4)
                                                            v10 = (v10 + 4)
                                                            if ((v10 + 4) != v12):
                                                                continue
                                                            break
                                                        break
                                                    if v4:
                                                        while True:  # $label19
                                                            v1 = load32((v6 + (v0 * 286704)) + 284608)
                                                            v8 = (load32((v6 + (v0 * 286704)) + 284608) if (u(v1) > u(v8)) else v8)
                                                            v0 = (v0 + 1)
                                                            v3 = (v3 + 1)
                                                            if ((v3 + 1) != v4):
                                                                continue
                                                            break
                                                    if (v8 != -1):
                                                        break
                                                    store32(9142416, 0)
                                                    break
                                                    break
                                                # TODO: memory.fill []
                                                store32(9142416, 0)
                                                v3 = load32(9561692)
                                                v0 = 0
                                                v9 = 0
                                                while True:  # $label23
                                                    v1 = v0
                                                    v0 = 1
                                                    while True:  # block $label21
                                                        if (u(v2) <= u(1)):
                                                            break
                                                        while True:  # $label22
                                                            if (v1 != load32((v3 + (v0 * 286704)) + 284608)):
                                                                v0 = (v0 + 1)
                                                                if (v2 != (v0 + 1)):
                                                                    continue
                                                                break
                                                            break
                                                        v0 = (v9 + 1)
                                                        store32(9142416, (v9 + 1))
                                                        store32(((v1 << 2) + 59200), v9)
                                                        v9 = v0
                                                        break
                                                    v0 = (v1 + 1)
                                                    if (v1 != v8):
                                                        continue
                                                    break
                                                break
                                            if (v20 == 0):
                                                break
                                            if load8u(9147127):
                                                break
                                            break
                                        v7 = load32(9142892)
                                        if (u(load32(9142892)) < u(2)):
                                            break
                                        v14 = load32(9142416)
                                        v12 = load32(9147316)
                                        v0 = load32(9147320)
                                        v5 = load32(9147312)
                                        v2 = load32(9147324)
                                        v10 = load32(9561692)
                                        v6 = v16
                                        v3 = 1
                                        while True:  # $label38
                                            while True:  # block $label31
                                                while True:  # block $label28
                                                    if v20:
                                                        v1 = ((v6 & 0xFFFFFFFF) >> 1)
                                                        v13 = (((v6 & 0xFFFFFFFF) >> 1) - 35)
                                                        # TODO: f32.convert_i32_u []
                                                        v34 = (6.28318548 / v14)
                                                        v36 = ((6.28318548 / v14) + -0.122173049)
                                                        v19 = ((v10 + (v3 * 286704)) + 284608)
                                                        # TODO: f32.convert_i32_u []
                                                        v33 = v1
                                                        v4 = 0
                                                        while True:  # $label30
                                                            v9 = load32(v19)
                                                            v1 = v12
                                                            store32(9147324, v12)
                                                            v11 = v5
                                                            store32(9147320, v5)
                                                            v2 = ((v2 << 11) ^ v2)
                                                            v12 = (((((v5 & 0xFFFFFFFF) >> 19) ^ ((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v5) ^ v2)
                                                            store32(9147316, (((((v5 & 0xFFFFFFFF) >> 19) ^ ((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v5) ^ v2))
                                                            v0 = ((v0 << 11) ^ v0)
                                                            v5 = (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v12 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v12)
                                                            store32(9147312, (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v12 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v12))
                                                            while True:  # block $label26
                                                                v38 = float(((v5 % v13) + 22))
                                                                # TODO: f64.promote_f32 []
                                                                # TODO: f32.convert_i32_u []
                                                                # TODO: f64.promote_f32 []
                                                                # TODO: f32.demote_f64 []
                                                                v37 = (((v36 * float((v12 % 360))) / 360.0) + ((v34 * load32(((v9 << 2) + 59200))) + 0.122173049))
                                                                v35 = ((float(((v5 % v13) + 22)) * func48((((v36 * float((v12 % 360))) / 360.0) + ((v34 * load32(((v9 << 2) + 59200))) + 0.122173049)))) + v33)
                                                                if (abs(((float(((v5 % v13) + 22)) * func48((((v36 * float((v12 % 360))) / 360.0) + ((v34 * load32(((v9 << 2) + 59200))) + 0.122173049)))) + v33)) < 2147483650.0):
                                                                    break
                                                                break
                                                            v8 = -2147483648
                                                            while True:  # block $label27
                                                                v38 = ((v38 * func49(v37)) + v33)
                                                                if (abs(((v38 * func49(v37)) + v33)) < 2147483650.0):
                                                                    break
                                                                break
                                                            v9 = -2147483648
                                                            if (u(v3) < u(2)):
                                                                break
                                                            v0 = ((-15 if (u(v4) > u(55)) else 0) + v15)
                                                            v2 = (((-15 if (u(v4) > u(55)) else 0) + v15) * v0)
                                                            v0 = 1
                                                            while True:  # $label29
                                                                v21 = (v10 + (v0 * 286704))
                                                                v18 = (load32((v10 + (v0 * 286704)) + 283872) - v9)
                                                                v21 = (load32(v21 + 283876) - v8)
                                                                if (v2 < ((((load32((v10 + (v0 * 286704)) + 283872) - v9) * v18) + ((load32(v21 + 283876) - v8) * v21)) - 1)):
                                                                    v0 = (v0 + 1)
                                                                    if (v3 != (v0 + 1)):
                                                                        continue
                                                                    break
                                                                break
                                                            v2 = v1
                                                            v0 = v11
                                                            v4 = (v4 + 1)
                                                            if ((v4 + 1) != 85):
                                                                continue
                                                            break
                                                        break
                                                    v11 = (v6 - 30)
                                                    v13 = 0
                                                    if (u(v3) >= u(2)):
                                                        while True:  # $label33
                                                            v1 = v5
                                                            store32(9147320, v5)
                                                            v4 = v12
                                                            store32(9147324, v12)
                                                            v2 = ((v2 << 11) ^ v2)
                                                            v12 = (((((v1 & 0xFFFFFFFF) >> 19) ^ ((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v1) ^ v2)
                                                            store32(9147316, (((((v1 & 0xFFFFFFFF) >> 19) ^ ((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v1) ^ v2))
                                                            v0 = ((v0 << 11) ^ v0)
                                                            v5 = (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v12 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v12)
                                                            store32(9147312, (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v12 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v12))
                                                            v8 = ((v5 % v11) + 13)
                                                            v9 = ((v12 % v11) + 13)
                                                            v0 = ((-15 if (u(v13) > u(55)) else 0) + v15)
                                                            v2 = (((-15 if (u(v13) > u(55)) else 0) + v15) * v0)
                                                            v0 = 1
                                                            while True:  # $label32
                                                                v19 = (v10 + (v0 * 286704))
                                                                v21 = (load32((v10 + (v0 * 286704)) + 283872) - v9)
                                                                v19 = (load32(v19 + 283876) - v8)
                                                                if (v2 < ((((load32((v10 + (v0 * 286704)) + 283872) - v9) * v21) + ((load32(v19 + 283876) - v8) * v19)) - 1)):
                                                                    v0 = (v0 + 1)
                                                                    if (v3 != (v0 + 1)):
                                                                        continue
                                                                    break
                                                                break
                                                            v2 = v4
                                                            v0 = v1
                                                            v13 = (v13 + 1)
                                                            if ((v13 + 1) != 85):
                                                                continue
                                                            break
                                                        break
                                                    store32(9147320, v5)
                                                    store32(9147324, v12)
                                                    v1 = ((v2 << 11) ^ v2)
                                                    v1 = (((((v5 & 0xFFFFFFFF) >> 19) ^ ((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v5) ^ v1)
                                                    store32(9147316, (((((v5 & 0xFFFFFFFF) >> 19) ^ ((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v5) ^ v1))
                                                    v0 = ((v0 << 11) ^ v0)
                                                    v0 = (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1)
                                                    store32(9147312, (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1))
                                                    v8 = ((v0 % v11) + 13)
                                                    v9 = ((v1 % v11) + 13)
                                                    break
                                                v12 = load32(9561692)
                                                while True:  # block $label34
                                                    v1 = (v9 - 25)
                                                    v5 = (v9 + 50)
                                                    if ((v9 - 25) >= (v9 + 50)):
                                                        break
                                                    v4 = (v8 - 25)
                                                    v11 = (v8 + 50)
                                                    if ((v8 - 25) >= (v8 + 50)):
                                                        break
                                                    while True:  # $label37
                                                        v2 = (v1 + 1)
                                                        v0 = (v1 - v9)
                                                        v7 = (((v1 - v9) * v0) - 1)
                                                        v0 = v4
                                                        while True:  # $label36
                                                            while True:  # block $label35
                                                                v6 = (v0 - v8)
                                                                if ((v7 + ((v0 - v8) * v6)) > 625):
                                                                    break
                                                                v6 = load32(9142440)
                                                                if (u(load32(9142440)) <= u(v0)):
                                                                    break
                                                                if ((v0 | v1) < 0):
                                                                    break
                                                                if (u(v1) >= u(v6)):
                                                                    break
                                                                v6 = (load32(9147288) + ((v0 * v6) + v1))
                                                                v10 = load8s((load32(9147288) + ((v0 * v6) + v1)))
                                                                if (load8s((load32(9147288) + ((v0 * v6) + v1))) < 0):
                                                                    break
                                                                if (load32(load32((load32(9140332) + ((v10 & 255) << 2))) + 32) != 23):
                                                                    break
                                                                store8(v6, load32(9147292))
                                                                v6 = load32(9142840)
                                                                v10 = (v0 + 1)
                                                                store32((load32(9142840) + ((((v0 + 1) * (load32(9142440) + 2)) + v2) << 2)), 0)
                                                                v13 = (load32(9142440) + 2)
                                                                store32((v6 + ((((v10 + (load32(9142440) + 2)) * v13) + v2) << 2)), 0)
                                                                break
                                                            v0 = (v0 + 1)
                                                            if ((v0 + 1) != v11):
                                                                continue
                                                            break
                                                        v1 = v2
                                                        if (v2 != v5):
                                                            continue
                                                        break
                                                    break
                                                v0 = (v12 + (v3 * 286704))
                                                store32((v12 + (v3 * 286704)) + 283900, v8)
                                                store32(v0 + 283896, v9)
                                                store32(v0 + 283876, v8)
                                                store32(v0 + 283872, v9)
                                                v7 = load32(9142892)
                                                v6 = load32(9142440)
                                                v14 = load32(9142416)
                                                v12 = load32(9147316)
                                                v0 = load32(9147320)
                                                v5 = load32(9147312)
                                                v2 = load32(9147324)
                                                v10 = load32(9561692)
                                                break
                                            v3 = (v3 + 1)
                                            if (u((v3 + 1)) < u(v7)):
                                                continue
                                            break
                                        break
                                        break
                                    # TODO: i32.div_u []
                                    v10 = 90
                                    # TODO: i32.div_u []
                                    v19 = 90
                                    v12 = (((load32(9142892) - 1) & 0xFFFFFFFF) >> 1)
                                    # TODO: i32.div_u []
                                    v0 = v10
                                    v24 = (v10 + (v12 != (v0 * v10)))
                                    if ((v10 + (v12 != (v0 * v10))) == 0):
                                        break
                                    v25 = (((v16 & 0xFFFFFFFF) >> 1) - 82)
                                    v26 = (0 - v19)
                                    v27 = ((v19 & 0xFFFFFFFF) >> 1)
                                    v3 = v12
                                    v4 = 0
                                    v15 = 0
                                    while True:  # $label52
                                        v0 = (v12 - (v10 * v15))
                                        v0 = ((v12 - (v10 * v15)) if (u(v0) < u(v10)) else v10)
                                        if ((v12 - (v10 * v15)) if (u(v0) < u(v10)) else v10):
                                            v28 = (v3 if (u(v3) < u(v10)) else v10)
                                            v29 = (0 if (v0 & 1) else v27)
                                            v13 = (v25 + (v15 * -70))
                                            v21 = ((v25 + (v15 * -70)) + 50)
                                            v11 = (v13 - 25)
                                            v20 = 0
                                            while True:  # $label51
                                                v9 = v7
                                                v2 = v4
                                                v4 = -1
                                                v5 = 0
                                                while True:  # block $label39
                                                    v1 = load32(9142892)
                                                    if (u(load32(9142892)) < u(2)):
                                                        break
                                                    v0 = 1
                                                    v7 = (v1 - 1)
                                                    v8 = ((v1 - 1) & 1)
                                                    v6 = load32(9561692)
                                                    if (v1 != 2):
                                                        v14 = (v7 & -2)
                                                        v1 = 0
                                                        while True:  # $label40
                                                            v7 = (v6 + (v0 * 286704))
                                                            if (load32((v6 + (v0 * 286704)) + 284608) == 1):
                                                                v7 = load32(v7 + 284620)
                                                                v7 = ((u(v2) < u(v7)) & (u(v4) > u(v7)))
                                                                v4 = (load32(v7 + 284620) if ((u(v2) < u(v7)) & (u(v4) > u(v7))) else v4)
                                                                v5 = (v0 if v7 else v5)
                                                            v18 = (v0 + 1)
                                                            v7 = (v6 + ((v0 + 1) * 286704))
                                                            if (load32((v6 + ((v0 + 1) * 286704)) + 284608) == 1):
                                                                v7 = load32(v7 + 284620)
                                                                v7 = ((u(v2) < u(v7)) & (u(v4) > u(v7)))
                                                                v4 = (load32(v7 + 284620) if ((u(v2) < u(v7)) & (u(v4) > u(v7))) else v4)
                                                                v5 = (v18 if v7 else v5)
                                                            v0 = (v0 + 2)
                                                            v1 = (v1 + 2)
                                                            if ((v1 + 2) != v14):
                                                                continue
                                                            break
                                                    if (v8 == 0):
                                                        break
                                                    v1 = (v6 + (v0 * 286704))
                                                    if (load32((v6 + (v0 * 286704)) + 284608) != 1):
                                                        break
                                                    v1 = load32(v1 + 284620)
                                                    v1 = ((u(v1) < u(v4)) & (u(v1) > u(v2)))
                                                    v4 = (load32(v1 + 284620) if ((u(v1) < u(v4)) & (u(v1) > u(v2))) else v4)
                                                    v5 = (v0 if v1 else v5)
                                                    break
                                                v20 = (v20 + 1)
                                                v8 = ((((load32(9142440) & 0xFFFFFFFF) >> 1) - v29) + ((v19 if (v20 & 1) else v26) * (((v20 + 1) & 0xFFFFFFFF) >> 1)))
                                                v7 = load32(9561692)
                                                while True:  # block $label41
                                                    if (v11 >= v21):
                                                        break
                                                    v1 = (v8 - 25)
                                                    v14 = (v8 + 50)
                                                    if ((v8 - 25) >= (v8 + 50)):
                                                        break
                                                    while True:  # $label44
                                                        v2 = (v1 + 1)
                                                        v0 = (v1 - v8)
                                                        v18 = (((v1 - v8) * v0) - 1)
                                                        v0 = v11
                                                        while True:  # $label43
                                                            while True:  # block $label42
                                                                v6 = (v0 - v13)
                                                                if ((v18 + ((v0 - v13) * v6)) > 625):
                                                                    break
                                                                v6 = load32(9142440)
                                                                if (u(load32(9142440)) <= u(v0)):
                                                                    break
                                                                if ((v0 | v1) < 0):
                                                                    break
                                                                if (u(v1) >= u(v6)):
                                                                    break
                                                                v6 = (load32(9147288) + ((v0 * v6) + v1))
                                                                v22 = load8s((load32(9147288) + ((v0 * v6) + v1)))
                                                                if (load8s((load32(9147288) + ((v0 * v6) + v1))) < 0):
                                                                    break
                                                                if (load32(load32((load32(9140332) + ((v22 & 255) << 2))) + 32) != 23):
                                                                    break
                                                                store8(v6, load32(9147292))
                                                                v6 = load32(9142840)
                                                                v22 = (v0 + 1)
                                                                store32((load32(9142840) + ((((v0 + 1) * (load32(9142440) + 2)) + v2) << 2)), 0)
                                                                v23 = (load32(9142440) + 2)
                                                                store32((v6 + ((((v22 + (load32(9142440) + 2)) * v23) + v2) << 2)), 0)
                                                                break
                                                            v0 = (v0 + 1)
                                                            if ((v0 + 1) != v21):
                                                                continue
                                                            break
                                                        v1 = v2
                                                        if (v2 != v14):
                                                            continue
                                                        break
                                                    break
                                                v0 = (v7 + (v5 * 286704))
                                                store32((v7 + (v5 * 286704)) + 283900, v13)
                                                store32(v0 + 283896, v8)
                                                store32(v0 + 283876, v13)
                                                store32(v0 + 283872, v8)
                                                v6 = 0
                                                v14 = load32(9561692)
                                                v7 = -1
                                                while True:  # block $label45
                                                    v1 = load32(9142892)
                                                    if (u(load32(9142892)) < u(2)):
                                                        break
                                                    v0 = 1
                                                    v2 = (v1 - 1)
                                                    v5 = ((v1 - 1) & 1)
                                                    if (v1 != 2):
                                                        v18 = (v2 & -2)
                                                        v2 = 0
                                                        while True:  # $label46
                                                            v1 = (v14 + (v0 * 286704))
                                                            if (load32((v14 + (v0 * 286704)) + 284608) == 2):
                                                                v1 = load32(v1 + 284620)
                                                                v1 = ((u(v1) < u(v7)) & (u(v1) > u(v9)))
                                                                v7 = (load32(v1 + 284620) if ((u(v1) < u(v7)) & (u(v1) > u(v9))) else v7)
                                                                v6 = (v0 if v1 else v6)
                                                            v22 = (v0 + 1)
                                                            v1 = (v14 + ((v0 + 1) * 286704))
                                                            if (load32((v14 + ((v0 + 1) * 286704)) + 284608) == 2):
                                                                v1 = load32(v1 + 284620)
                                                                v1 = ((u(v1) < u(v7)) & (u(v1) > u(v9)))
                                                                v7 = (load32(v1 + 284620) if ((u(v1) < u(v7)) & (u(v1) > u(v9))) else v7)
                                                                v6 = (v22 if v1 else v6)
                                                            v0 = (v0 + 2)
                                                            v2 = (v2 + 2)
                                                            if ((v2 + 2) != v18):
                                                                continue
                                                            break
                                                    if (v5 == 0):
                                                        break
                                                    v1 = (v14 + (v0 * 286704))
                                                    if (load32((v14 + (v0 * 286704)) + 284608) != 2):
                                                        break
                                                    v1 = load32(v1 + 284620)
                                                    v1 = ((u(v1) < u(v7)) & (u(v1) > u(v9)))
                                                    v7 = (load32(v1 + 284620) if ((u(v1) < u(v7)) & (u(v1) > u(v9))) else v7)
                                                    v6 = (v0 if v1 else v6)
                                                    break
                                                v5 = (load32(9142440) - v13)
                                                while True:  # block $label47
                                                    v1 = (v8 - 25)
                                                    v22 = (v8 + 50)
                                                    if ((v8 - 25) >= (v8 + 50)):
                                                        break
                                                    v9 = (v5 - 25)
                                                    v23 = (v5 + 50)
                                                    if ((v5 - 25) >= (v5 + 50)):
                                                        break
                                                    while True:  # $label50
                                                        v2 = (v1 + 1)
                                                        v0 = (v1 - v8)
                                                        v30 = (((v1 - v8) * v0) - 1)
                                                        v0 = v9
                                                        while True:  # $label49
                                                            while True:  # block $label48
                                                                v18 = (v0 - v5)
                                                                if ((v30 + ((v0 - v5) * v18)) > 625):
                                                                    break
                                                                v18 = load32(9142440)
                                                                if (u(load32(9142440)) <= u(v0)):
                                                                    break
                                                                if ((v0 | v1) < 0):
                                                                    break
                                                                if (u(v1) >= u(v18)):
                                                                    break
                                                                v18 = (load32(9147288) + ((v0 * v18) + v1))
                                                                v31 = load8s((load32(9147288) + ((v0 * v18) + v1)))
                                                                if (load8s((load32(9147288) + ((v0 * v18) + v1))) < 0):
                                                                    break
                                                                if (load32(load32((load32(9140332) + ((v31 & 255) << 2))) + 32) != 23):
                                                                    break
                                                                store8(v18, load32(9147292))
                                                                v18 = load32(9142840)
                                                                v31 = (v0 + 1)
                                                                store32((load32(9142840) + ((((v0 + 1) * (load32(9142440) + 2)) + v2) << 2)), 0)
                                                                v32 = (load32(9142440) + 2)
                                                                store32((v18 + ((((v31 + (load32(9142440) + 2)) * v32) + v2) << 2)), 0)
                                                                break
                                                            v0 = (v0 + 1)
                                                            if ((v0 + 1) != v23):
                                                                continue
                                                            break
                                                        v1 = v2
                                                        if (v2 != v22):
                                                            continue
                                                        break
                                                    break
                                                v0 = (v14 + (v6 * 286704))
                                                store32((v14 + (v6 * 286704)) + 283900, v5)
                                                store32(v0 + 283896, v8)
                                                store32(v0 + 283876, v5)
                                                store32(v0 + 283872, v8)
                                                if (v20 != v28):
                                                    continue
                                                break
                                        v3 = (v3 - v10)
                                        v15 = (v15 + 1)
                                        if ((v15 + 1) != v24):
                                            continue
                                        break
                                    break
                                    break
                                v34 = (v34 / v37)
                                while True:  # block $label53
                                    if (v9 == 0):
                                        break
                                    if (u(v0) < u(2)):
                                        break
                                    v2 = load32(9561692)
                                    v6 = load32(9561692)
                                    v11 = 1
                                    while True:  # $label61
                                        while True:  # block $label54
                                            if v9:
                                                if (load32((v6 + (v11 * 286704)) + 284608) != 2):
                                                    break
                                            while True:  # block $label55
                                                # TODO: f32.convert_i32_u []
                                                v37 = ((v36 * (v7 - 1)) + v38)
                                                # TODO: f32.convert_i32_u []
                                                v35 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                                                v39 = ((v33 * func48(((v36 * (v7 - 1)) + v38))) + ((load32(9142440) & 0xFFFFFFFF) >> 1))
                                                if (abs(((v33 * func48(((v36 * (v7 - 1)) + v38))) + ((load32(9142440) & 0xFFFFFFFF) >> 1))) < 2147483650.0):
                                                    break
                                                break
                                            v4 = -2147483648
                                            while True:  # block $label57
                                                while True:  # block $label56
                                                    v37 = ((v33 * func49(v37)) + v35)
                                                    if (abs(((v33 * func49(v37)) + v35)) < 2147483650.0):
                                                        break
                                                    break
                                                v12 = -2147483648
                                                v1 = (-2147483648 - 25)
                                                v8 = (v12 + 50)
                                                if ((-2147483648 - 25) >= (v12 + 50)):
                                                    break
                                                v3 = (v4 - 25)
                                                v10 = (v4 + 50)
                                                if ((v4 - 25) >= (v4 + 50)):
                                                    break
                                                while True:  # $label60
                                                    v2 = (v1 + 1)
                                                    v0 = (v1 - v12)
                                                    v13 = (((v1 - v12) * v0) - 1)
                                                    v0 = v3
                                                    while True:  # $label59
                                                        while True:  # block $label58
                                                            v5 = (v0 - v4)
                                                            if ((v13 + ((v0 - v4) * v5)) > 625):
                                                                break
                                                            v5 = load32(9142440)
                                                            if (u(load32(9142440)) <= u(v0)):
                                                                break
                                                            if ((v0 | v1) < 0):
                                                                break
                                                            if (u(v1) >= u(v5)):
                                                                break
                                                            v5 = (load32(9147288) + ((v0 * v5) + v1))
                                                            v17 = load8s((load32(9147288) + ((v0 * v5) + v1)))
                                                            if (load8s((load32(9147288) + ((v0 * v5) + v1))) < 0):
                                                                break
                                                            if (load32(load32((load32(9140332) + ((v17 & 255) << 2))) + 32) != 23):
                                                                break
                                                            store8(v5, load32(9147292))
                                                            v5 = load32(9142840)
                                                            v17 = (v0 + 1)
                                                            store32((load32(9142840) + ((((v0 + 1) * (load32(9142440) + 2)) + v2) << 2)), 0)
                                                            v15 = (load32(9142440) + 2)
                                                            store32((v5 + ((((v17 + (load32(9142440) + 2)) * v15) + v2) << 2)), 0)
                                                            break
                                                        v0 = (v0 + 1)
                                                        if ((v0 + 1) != v10):
                                                            continue
                                                        break
                                                    v1 = v2
                                                    if (v2 != v8):
                                                        continue
                                                    break
                                                v2 = load32(9561692)
                                                break
                                            v7 = (v7 + 1)
                                            v0 = (v6 + (v11 * 286704))
                                            store32((v6 + (v11 * 286704)) + 283900, v4)
                                            store32(v0 + 283896, v12)
                                            store32(v0 + 283876, v4)
                                            store32(v0 + 283872, v12)
                                            v0 = load32(9142892)
                                            v6 = v2
                                            break
                                        v11 = (v11 + 1)
                                        if (u((v11 + 1)) < u(v0)):
                                            continue
                                        break
                                    break
                                if ((v34 < 4294967300.0) & (v34 >= 0.0)):
                                    # TODO: i32.trunc_f32_u []
                                    v17 = v34
                                    break
                                v17 = 0
                                break
                                break
                            if v4:
                                while True:  # $label62
                                    v1 = load32((v6 + (v2 * 286704)) + 284608)
                                    v12 = (load32((v6 + (v2 * 286704)) + 284608) if (u(v1) > u(v12)) else v12)
                                    v2 = (v2 + 1)
                                    v3 = (v3 + 1)
                                    if ((v3 + 1) != v4):
                                        continue
                                    break
                            v6 = -1
                            if (v12 == -1):
                                break
                            break
                        # TODO: memory.fill []
                        store32(9142416, 0)
                        v3 = load32(9561692)
                        v2 = 0
                        v4 = 0
                        while True:  # $label66
                            v1 = v2
                            v2 = 1
                            while True:  # block $label64
                                if (u(v0) <= u(1)):
                                    break
                                while True:  # $label65
                                    if (v1 != load32((v3 + (v2 * 286704)) + 284608)):
                                        v2 = (v2 + 1)
                                        if (v0 != (v2 + 1)):
                                            continue
                                        break
                                    break
                                v4 = (v4 + 1)
                                store32(9142416, (v4 + 1))
                                store32(((v1 << 2) + 59200), 1)
                                break
                            v2 = (v1 + 1)
                            if (v1 != v12):
                                continue
                            break
                        break
                        break
                    v4 = 0
                    store32(9142416, 0)
                    v1 = 1
                    v5 = 0
                    if (load32(v11 + 64) == 0):
                        break
                    break
                    break
                if (load32(v11 + 64) == 0):
                    break
                v1 = (v0 - 1)
                v10 = ((v0 - 1) & -4)
                v7 = (v1 & 3)
                v5 = 0
                v8 = load32(9561692)
                v13 = (u((v0 - 2)) > u(2))
                v1 = 0
                while True:  # $label73
                    if load32(((v1 << 2) + 59200)):
                        v3 = 0
                        while True:  # block $label70
                            if (u(v0) < u(2)):
                                break
                            v2 = 1
                            v9 = 0
                            v11 = 0
                            if v13:
                                while True:  # $label71
                                    v6 = (v8 + (v2 * 286704))
                                    v3 = ((((v3 + (load32((v8 + (v2 * 286704)) + 284608) == v1)) + (load32((v6 + 571312)) == v1)) + (load32((v6 + 858016)) == v1)) + (load32((v6 + 1144720)) == v1))
                                    v2 = (v2 + 4)
                                    v11 = (v11 + 4)
                                    if ((v11 + 4) != v10):
                                        continue
                                    break
                            if (v7 == 0):
                                break
                            while True:  # $label72
                                v3 = (v3 + (load32((v8 + (v2 * 286704)) + 284608) == v1))
                                v2 = (v2 + 1)
                                v9 = (v9 + 1)
                                if ((v9 + 1) != v7):
                                    continue
                                break
                            break
                        v5 = (v3 if (u(v3) > u(v5)) else v5)
                    v2 = (v1 == v12)
                    v1 = (v1 + 1)
                    if (v2 == 0):
                        continue
                    break
                v1 = 0
                v6 = v12
                break
            while True:  # block $label74
                v2 = v4
                if (v4 == 0):
                    v2 = (load32(41092) if load8u(9147210) else (v0 - 1))
                # TODO: f32.convert_i32_u []
                # TODO: f32.convert_i32_u []
                # TODO: f64.promote_f32 []
                # TODO: f32.demote_f64 []
                v33 = ((((v16 & 0xFFFFFFFF) >> 1) + (((20.0 if (u(v5) < u(5)) else 14.0) * v5) / -6.2831854820251465)) + -8.0)
                # TODO: f32.convert_i32_u []
                v34 = ((((((v16 & 0xFFFFFFFF) >> 1) + (((20.0 if (u(v5) < u(5)) else 14.0) * v5) / -6.2831854820251465)) + -8.0) * (v33 * 3.14159274)) / (4 if (u(v2) < u(3)) else (v2 << (v2 & 1))))
                if ((((((((v16 & 0xFFFFFFFF) >> 1) + (((20.0 if (u(v5) < u(5)) else 14.0) * v5) / -6.2831854820251465)) + -8.0) * (v33 * 3.14159274)) / (4 if (u(v2) < u(3)) else (v2 << (v2 & 1)))) < 4294967300.0) & (v34 >= 0.0)):
                    # TODO: i32.trunc_f32_u []
                    break
                break
            v17 = 0
            if v1:
                break
            # TODO: f32.convert_i32_u []
            v38 = (6.28318548 / v4)
            v37 = ((6.28318548 / v4) * 0.5)
            v12 = 0
            v7 = 0
            while True:  # $label88
                if load32(((v7 << 2) + 59200)):
                    while True:  # block $label78
                        while True:  # block $label75
                            if (u(v0) < u(2)):
                                v34 = 0.0
                                v41 = 0.0
                                break
                            v3 = (v0 - 1)
                            v4 = ((v0 - 1) & 3)
                            v8 = 0
                            v9 = load32(9561692)
                            v2 = 1
                            v1 = 0
                            if (u((v0 - 2)) >= u(3)):
                                v5 = (v3 & -4)
                                v10 = 0
                                while True:  # $label76
                                    v3 = (v9 + (v2 * 286704))
                                    v1 = ((((v1 + (v7 == load32((v9 + (v2 * 286704)) + 284608))) + (v7 == load32((v3 + 571312)))) + (v7 == load32((v3 + 858016)))) + (v7 == load32((v3 + 1144720))))
                                    v2 = (v2 + 4)
                                    v10 = (v10 + 4)
                                    if ((v10 + 4) != v5):
                                        continue
                                    break
                            if v4:
                                while True:  # $label77
                                    v1 = (v1 + (v7 == load32((v9 + (v2 * 286704)) + 284608)))
                                    v2 = (v2 + 1)
                                    v8 = (v8 + 1)
                                    if ((v8 + 1) != v4):
                                        continue
                                    break
                            # TODO: f32.convert_i32_u []
                            v34 = v1
                            # TODO: f64.promote_f32 []
                            v41 = v1
                            if (u(v1) > u(4)):
                                break
                            break
                        break
                    v42 = 20.0
                    if (u(v0) >= u(2)):
                        v13 = 0
                        v11 = 1
                        v34 = (6.28318548 / v34)
                        # TODO: f32.demote_f64 []
                        v36 = ((v42 * v41) / 6.2831854820251465)
                        while True:  # block $label79
                            # TODO: f32.convert_i32_u []
                            v35 = ((v38 * v12) + v37)
                            # TODO: f64.promote_f32 []
                            # TODO: f64.convert_i32_u []
                            v41 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                            v42 = (((v33 * func48(((v38 * v12) + v37))) + 0.5) + ((load32(9142440) & 0xFFFFFFFF) >> 1))
                            if (abs((((v33 * func48(((v38 * v12) + v37))) + 0.5) + ((load32(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0):
                                break
                            break
                        v42 = float(-2147483648)
                        while True:  # block $label80
                            # TODO: f64.promote_f32 []
                            v41 = (((v33 * func49(v35)) + 0.5) + v41)
                            if (abs((((v33 * func49(v35)) + 0.5) + v41)) < 2147483648.0):
                                break
                            break
                        v41 = float(-2147483648)
                        v35 = (v34 * 0.5)
                        v2 = load32(9561692)
                        while True:  # $label87
                            v9 = (v2 + (v11 * 286704))
                            if (v7 == load32((v2 + (v11 * 286704)) + 284608)):
                                while True:  # block $label81
                                    # TODO: f32.convert_i32_u []
                                    v39 = ((v34 * v13) + v35)
                                    # TODO: f64.promote_f32 []
                                    v43 = (((func48(((v34 * v13) + v35)) * v36) + 0.5) + v42)
                                    if (abs((((func48(((v34 * v13) + v35)) * v36) + 0.5) + v42)) < 2147483648.0):
                                        break
                                    break
                                v4 = -2147483648
                                while True:  # block $label83
                                    while True:  # block $label82
                                        # TODO: f64.promote_f32 []
                                        v43 = (((func49(v39) * v36) + 0.5) + v41)
                                        if (abs((((func49(v39) * v36) + 0.5) + v41)) < 2147483648.0):
                                            break
                                        break
                                    v5 = -2147483648
                                    v1 = (-2147483648 - 25)
                                    v10 = (v5 + 50)
                                    if ((-2147483648 - 25) >= (v5 + 50)):
                                        break
                                    v3 = (v4 - 25)
                                    v15 = (v4 + 50)
                                    if ((v4 - 25) >= (v4 + 50)):
                                        break
                                    while True:  # $label86
                                        v2 = (v1 + 1)
                                        v0 = (v1 - v5)
                                        v20 = (((v1 - v5) * v0) - 1)
                                        v0 = v3
                                        while True:  # $label85
                                            while True:  # block $label84
                                                v8 = (v0 - v4)
                                                if ((v20 + ((v0 - v4) * v8)) > 625):
                                                    break
                                                v8 = load32(9142440)
                                                if (u(load32(9142440)) <= u(v0)):
                                                    break
                                                if ((v0 | v1) < 0):
                                                    break
                                                if (u(v1) >= u(v8)):
                                                    break
                                                v8 = (load32(9147288) + ((v0 * v8) + v1))
                                                v14 = load8s((load32(9147288) + ((v0 * v8) + v1)))
                                                if (load8s((load32(9147288) + ((v0 * v8) + v1))) < 0):
                                                    break
                                                if (load32(load32((load32(9140332) + ((v14 & 255) << 2))) + 32) != 23):
                                                    break
                                                store8(v8, load32(9147292))
                                                v8 = load32(9142840)
                                                v14 = (v0 + 1)
                                                store32((load32(9142840) + ((((v0 + 1) * (load32(9142440) + 2)) + v2) << 2)), 0)
                                                v19 = (load32(9142440) + 2)
                                                store32((v8 + ((((v14 + (load32(9142440) + 2)) * v19) + v2) << 2)), 0)
                                                break
                                            v0 = (v0 + 1)
                                            if ((v0 + 1) != v15):
                                                continue
                                            break
                                        v1 = v2
                                        if (v2 != v10):
                                            continue
                                        break
                                    v2 = load32(9561692)
                                    break
                                store32(v9 + 283900, v4)
                                store32(v9 + 283896, v5)
                                store32(v9 + 283876, v4)
                                store32(v9 + 283872, v5)
                                v13 = (v13 + 1)
                                v0 = load32(9142892)
                            v11 = (v11 + 1)
                            if (u((v11 + 1)) < u(v0)):
                                continue
                            break
                    v12 = (v12 + 1)
                v1 = (v6 == v7)
                v7 = (v7 + 1)
                if (v1 == 0):
                    continue
                break
            break
            break
        v20 = (v15 * v15)
        v2 = 0
        while True:  # $label106
            while True:  # block $label89
                v7 = v2
                if (load32(((v2 << 2) + 59200)) == 0):
                    break
                v2 = load32(9561692)
                while True:  # block $label94
                    while True:  # block $label93
                        while True:  # block $label90
                            if (u(v0) < u(2)):
                                v33 = 0.0
                                v41 = 0.0
                                break
                            v4 = (v0 - 1)
                            v6 = ((v0 - 1) & 3)
                            v1 = 1
                            v9 = 0
                            v3 = 0
                            if (u((v0 - 2)) >= u(3)):
                                v5 = (v4 & -4)
                                v10 = 0
                                while True:  # $label91
                                    v4 = (v2 + (v1 * 286704))
                                    v3 = ((((v3 + (v7 == load32((v2 + (v1 * 286704)) + 284608))) + (v7 == load32((v4 + 571312)))) + (v7 == load32((v4 + 858016)))) + (v7 == load32((v4 + 1144720))))
                                    v1 = (v1 + 4)
                                    v10 = (v10 + 4)
                                    if ((v10 + 4) != v5):
                                        continue
                                    break
                            if v6:
                                while True:  # $label92
                                    v3 = (v3 + (v7 == load32((v2 + (v1 * 286704)) + 284608)))
                                    v1 = (v1 + 1)
                                    v9 = (v9 + 1)
                                    if ((v9 + 1) != v6):
                                        continue
                                    break
                            # TODO: f32.convert_i32_u []
                            v33 = v3
                            # TODO: f64.promote_f32 []
                            v41 = v3
                            if (u(v3) > u(4)):
                                break
                            break
                        break
                    # TODO: f32.demote_f64 []
                    v34 = ((20.0 * v41) / 6.2831854820251465)
                    v36 = (((20.0 * v41) / 6.2831854820251465) + 8.0)
                    if (abs((((20.0 * v41) / 6.2831854820251465) + 8.0)) < 2147483650.0):
                        break
                    break
                v1 = -2147483648
                v13 = (-2147483648 + 15)
                v6 = 0
                v15 = ((load32(9142440) - v1) - 30)
                v4 = load32(9147316)
                v1 = load32(9147320)
                v11 = load32(9147312)
                v3 = load32(9147324)
                while True:  # block $label98
                    if (u(v0) >= u(2)):
                        while True:  # $label96
                            v5 = v11
                            store32(9147320, v11)
                            store32(9147324, v4)
                            v3 = ((v3 << 11) ^ v3)
                            v8 = (((((v5 & 0xFFFFFFFF) >> 19) ^ ((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v5) ^ v3)
                            store32(9147316, (((((v5 & 0xFFFFFFFF) >> 19) ^ ((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v5) ^ v3))
                            v1 = ((v1 << 11) ^ v1)
                            v11 = (((((((v1 << 11) ^ v1) & 0xFFFFFFFF) >> 8) ^ ((v8 & 0xFFFFFFFF) >> 19)) ^ v1) ^ v8)
                            store32(9147312, (((((((v1 << 11) ^ v1) & 0xFFFFFFFF) >> 8) ^ ((v8 & 0xFFFFFFFF) >> 19)) ^ v1) ^ v8))
                            v9 = (v13 + (v11 % v15))
                            v10 = (v13 + (v8 % v15))
                            v1 = 1
                            while True:  # $label97
                                while True:  # block $label95
                                    v3 = (v2 + (v1 * 286704))
                                    v14 = load32((v2 + (v1 * 286704)) + 283872)
                                    if (load32((v2 + (v1 * 286704)) + 283872) == 0):
                                        break
                                    v14 = (v14 - v10)
                                    v3 = (load32(v3 + 283876) - v9)
                                    if (((((v14 - v10) * v14) + ((load32(v3 + 283876) - v9) * v3)) - 1) > v20):
                                        break
                                    v3 = v4
                                    v1 = v5
                                    v4 = v8
                                    v6 = (v6 + 1)
                                    if ((v6 + 1) != 55):
                                        continue
                                    break
                                    break
                                v1 = (v1 + 1)
                                if ((v1 + 1) != v0):
                                    continue
                                break
                            break
                            break
                        raise RuntimeError('unreachable')
                    store32(9147320, v11)
                    store32(9147324, v4)
                    v3 = ((v3 << 11) ^ v3)
                    v3 = (((((v11 & 0xFFFFFFFF) >> 19) ^ ((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v11) ^ v3)
                    store32(9147316, (((((v11 & 0xFFFFFFFF) >> 19) ^ ((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8)) ^ v11) ^ v3))
                    v1 = ((v1 << 11) ^ v1)
                    v1 = (((((((v1 << 11) ^ v1) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v1) ^ v3)
                    store32(9147312, (((((((v1 << 11) ^ v1) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v1) ^ v3))
                    v9 = (v13 + (v1 % v15))
                    v10 = (v13 + (v3 % v15))
                    break
                if (u(v0) < u(2)):
                    break
                v33 = (6.28318548 / v33)
                v36 = ((6.28318548 / v33) * 0.5)
                v41 = float(v9)
                v42 = float(v10)
                v11 = 1
                v13 = 0
                while True:  # $label105
                    v6 = (v2 + (v11 * 286704))
                    if (v7 == load32((v2 + (v11 * 286704)) + 284608)):
                        while True:  # block $label99
                            # TODO: f32.convert_i32_u []
                            v38 = ((v33 * v13) + v36)
                            # TODO: f64.promote_f32 []
                            v43 = (((func48(((v33 * v13) + v36)) * v34) + 0.5) + v41)
                            if (abs((((func48(((v33 * v13) + v36)) * v34) + 0.5) + v41)) < 2147483648.0):
                                break
                            break
                        v4 = -2147483648
                        while True:  # block $label101
                            while True:  # block $label100
                                # TODO: f64.promote_f32 []
                                v43 = (((func49(v38) * v34) + 0.5) + v42)
                                if (abs((((func49(v38) * v34) + 0.5) + v42)) < 2147483648.0):
                                    break
                                break
                            v9 = -2147483648
                            v1 = (-2147483648 - 25)
                            v8 = (v9 + 50)
                            if ((-2147483648 - 25) >= (v9 + 50)):
                                break
                            v3 = (v4 - 25)
                            v10 = (v4 + 50)
                            if ((v4 - 25) >= (v4 + 50)):
                                break
                            while True:  # $label104
                                v2 = (v1 + 1)
                                v0 = (v1 - v9)
                                v15 = (((v1 - v9) * v0) - 1)
                                v0 = v3
                                while True:  # $label103
                                    while True:  # block $label102
                                        v5 = (v0 - v4)
                                        if ((v15 + ((v0 - v4) * v5)) > 625):
                                            break
                                        v5 = load32(9142440)
                                        if (u(load32(9142440)) <= u(v0)):
                                            break
                                        if ((v0 | v1) < 0):
                                            break
                                        if (u(v1) >= u(v5)):
                                            break
                                        v5 = (load32(9147288) + ((v0 * v5) + v1))
                                        v14 = load8s((load32(9147288) + ((v0 * v5) + v1)))
                                        if (load8s((load32(9147288) + ((v0 * v5) + v1))) < 0):
                                            break
                                        if (load32(load32((load32(9140332) + ((v14 & 255) << 2))) + 32) != 23):
                                            break
                                        store8(v5, load32(9147292))
                                        v5 = load32(9142840)
                                        v14 = (v0 + 1)
                                        store32((load32(9142840) + ((((v0 + 1) * (load32(9142440) + 2)) + v2) << 2)), 0)
                                        v19 = (load32(9142440) + 2)
                                        store32((v5 + ((((v14 + (load32(9142440) + 2)) * v19) + v2) << 2)), 0)
                                        break
                                    v0 = (v0 + 1)
                                    if ((v0 + 1) != v10):
                                        continue
                                    break
                                v1 = v2
                                if (v2 != v8):
                                    continue
                                break
                            break
                        store32(v6 + 283900, v4)
                        store32(v6 + 283896, v9)
                        store32(v6 + 283876, v4)
                        store32(v6 + 283872, v9)
                        v13 = (v13 + 1)
                        v2 = load32(9561692)
                        v0 = load32(9142892)
                    v11 = (v11 + 1)
                    if (u((v11 + 1)) < u(v0)):
                        continue
                    break
                break
            v2 = (v7 + 1)
            if (v7 != v12):
                continue
            break
        break
    v2 = 0
    v0 = load32(9142440)
    if load32(9142440):
        v12 = load32(9147288)
        v2 = v0
        v3 = 0
        while True:  # $label109
            v4 = (v3 + 1)
            v1 = load32(9147292)
            v6 = load32(9142840)
            v0 = 0
            while True:  # $label108
                while True:  # block $label107
                    if (load8s((v12 + ((v0 * v2) + v3))) != v1):
                        v0 = (v0 + 1)
                        break
                    v0 = (v0 + 1)
                    v9 = (v6 + ((((v0 + 1) * (v2 + 2)) + v4) << 2))
                    if (load32((v6 + ((((v0 + 1) * (v2 + 2)) + v4) << 2))) != 1):
                        break
                    store32(v9, 0)
                    v1 = (load32(9142440) + 2)
                    store32((v6 + (((((load32(9142440) + 2) + v0) * v1) + v4) << 2)), 0)
                    v2 = load32(9142440)
                    v1 = load32(9147292)
                    break
                if (u(v0) < u(v2)):
                    continue
                break
            v3 = v4
            if (u(v4) < u(v2)):
                continue
            break
    v0 = 1
    if (u(load32(9142892)) > u(1)):
        while True:  # $label110
            v1 = (load32(9561692) + (v0 * 286704))
            if (load32(v1 + 284624) == 0):
            v0 = (v0 + 1)
            if (u((v0 + 1)) < u(load32(9142892))):
                continue
            break
    v0 = 47
    v8 = load32(9142428)
    if (u(load32(9142428)) > u(47)):
        # TODO: f32.convert_i32_u []
        v36 = (v17 * 1.52587891e-05)
        while True:  # $label145
            v13 = (load32(9142424) + (v0 << 2))
            v26 = load32((load32(9142424) + (v0 << 2)) + 16)
            v27 = ((v0 + 7) if load32((load32(9142424) + (v0 << 2)) + 16) else v0)
            while True:  # block $label111
                v0 = load32(v13 + 4)
                if (load32(v13 + 4) == 1):
                    break
                v6 = load32(v13 + 8)
                while True:  # block $label112
                    v1 = load32(v13)
                    # TODO: f32.convert_i32_u []
                    # TODO: f64.promote_f32 []
                    # TODO: f64.convert_i32_u []
                    v2 = load32(v13 + 12)
                    v41 = (((v36 * load32(v13)) + 0.5) if load32(v13 + 12) else v1)
                    if (((((v36 * load32(v13)) + 0.5) if load32(v13 + 12) else v1) < 4294967296.0) & (v41 >= 0.0)):
                        # TODO: i32.trunc_f64_u []
                        break
                    break
                v1 = 0
                v28 = ((0 if v1 else 1) if v2 else v1)
                if (((0 if v1 else 1) if v2 else v1) == 0):
                    break
                v11 = (2147483647 if (v0 == 2) else v0)
                v12 = 0
                while True:  # $label144
                    v0 = 0
                    while True:  # $label139
                        v1 = 0
                        while True:  # block $label113
                            if (load32(38504) != v6):
                                if (v6 != load32(38508)):
                                    break
                            v44 = load64(9147316)
                            v1 = load32(9147312)
                            store32(9147316, load32(9147312))
                            v2 = load32(9147324)
                            store64(9147320, v44)
                            v2 = (v2 ^ (v2 << 11))
                            v1 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2)
                            store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2))
                            v1 = (v1 % 3)
                            break
                        while True:  # block $label114
                            if (load32(load32(9142424) + 64) == 0):
                                v2 = load32(9147324)
                                store32(9147324, load32(9147316))
                                v3 = load32(9147320)
                                v4 = load32(9147312)
                                store32(9147320, load32(9147312))
                                v2 = (v2 ^ (v2 << 11))
                                v2 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2)
                                store32(9147316, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2))
                                v3 = (v3 ^ (v3 << 11))
                                v3 = ((((((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v2)
                                store32(9147312, ((((((v3 ^ (v3 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v3) ^ v2))
                                break
                            v3 = v1
                            v15 = 0
                            v20 = 0
                            v1 = load32(9142416)
                            v2 = load32(9142416)
                            if (v1 == 0):
                                v2 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                            # TODO: f32.convert_i32_u []
                            v33 = (6.28318548 / (4 if (u(v2) < u(3)) else (v2 << (v2 & 1))))
                            v9 = load32(9147312)
                            v2 = load32(9147324)
                            v2 = ((load32(9147324) << 11) ^ v2)
                            v4 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v9) ^ v2)
                            v7 = ((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v9) ^ v2) % ((load32(9142440) & 0xFFFFFFFF) >> 1))
                            v8 = load32(9147316)
                            v5 = load32(9147320)
                            v2 = v1
                            if (v1 == 0):
                                v2 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                            v34 = float(v7)
                            store32(9147320, v9)
                            store32(9147324, v8)
                            store32(9147316, v4)
                            v9 = ((v5 << 11) ^ v5)
                            v4 = (((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v9) ^ v4)
                            store32(9147312, (((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v9) ^ v4))
                            # TODO: f32.convert_i32_u []
                            v38 = (((6.28318548 / (4 if (u(v2) < u(3)) else (v2 << (v2 & 1)))) * float((v4 % 100000))) / 100000.0)
                            v37 = (v33 - (((6.28318548 / (4 if (u(v2) < u(3)) else (v2 << (v2 & 1)))) * float((v4 % 100000))) / 100000.0))
                            v10 = ((v6 * 404) + 9568096)
                            v29 = (v3 & 255)
                            while True:  # $label138
                                if (v1 == 0):
                                    v1 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                                if (u((4 if (u(v1) < u(3)) else (v1 << (v1 & 1)))) > u(v15)):
                                    # TODO: f32.convert_i32_u []
                                    v35 = ((v33 * v15) + (v37 if (v15 & 1) else v38))
                                    v39 = func48(((v33 * v15) + (v37 if (v15 & 1) else v38)))
                                    while True:  # block $label115
                                        # TODO: f64.convert_i32_u []
                                        # TODO: f64.promote_f32 []
                                        # TODO: f64.convert_i32_u []
                                        v41 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                                        v42 = (((0.5 - (load32(v10 + 220) * 0.5)) + (v39 * v34)) + ((load32(9142440) & 0xFFFFFFFF) >> 1))
                                        if (abs((((0.5 - (load32(v10 + 220) * 0.5)) + (v39 * v34)) + ((load32(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0):
                                            break
                                        break
                                    v9 = -2147483648
                                    v35 = func49(v35)
                                    while True:  # block $label123
                                        while True:  # block $label116
                                            # TODO: f64.convert_i32_u []
                                            # TODO: f64.promote_f32 []
                                            v41 = (((0.5 - (load32(v10 + 216) * 0.5)) + (v35 * v34)) + v41)
                                            if (abs((((0.5 - (load32(v10 + 216) * 0.5)) + (v35 * v34)) + v41)) < 2147483648.0):
                                                break
                                            break
                                        v7 = -2147483648
                                        if (func56(-2147483648, v9, v10, v11, 0, 0, 1, 1, 0) == 0):
                                            v1 = 0
                                            v17 = load32(9142440)
                                            while True:  # $label137
                                                while True:  # block $label117
                                                    v8 = v1
                                                    v1 = (v1 << 2)
                                                    v2 = (load32((((v1 << 2) | 4) + 8611904)) + v9)
                                                    if (u(v17) <= u((load32((((v1 << 2) | 4) + 8611904)) + v9))):
                                                        break
                                                    v4 = (load32((v1 + 8611904)) + v7)
                                                    if (u(v17) <= u((load32((v1 + 8611904)) + v7))):
                                                        break
                                                    if ((v2 | v4) < 0):
                                                        break
                                                    while True:  # block $label122
                                                        while True:  # block $label121
                                                            while True:  # block $label120
                                                                while True:  # block $label119
                                                                    while True:  # block $label118
                                                                        v1 = load32(v10 + 248)
                                                                        # br_table[(load32(v10 + 248) - 1)]
                                                                        break
                                                                        break
                                                                    if (func282(v4, v2, v10, 0, 0, 1) == 0):
                                                                        break
                                                                    break
                                                                    break
                                                                if (func283(v4, v2, v10, 0, 0, 1, 1) == 0):
                                                                    break
                                                                break
                                                                break
                                                            v14 = load32(v10 + 216)
                                                            if (load32(v10 + 216) <= 0):
                                                                break
                                                            v19 = (load32(v10 + 220) + v2)
                                                            if ((load32(v10 + 220) + v2) <= v2):
                                                                break
                                                            v24 = (v4 + v14)
                                                            v21 = load32(v10 + 372)
                                                            v25 = (v17 + 2)
                                                            v22 = ((v17 + 2) * load32(v10 + 208))
                                                            v23 = load32(v10 + 212)
                                                            v30 = load32(9142840)
                                                            v3 = v4
                                                            while True:  # $label128
                                                                v5 = (v3 + 1)
                                                                v18 = (v3 - v4)
                                                                v1 = v2
                                                                while True:  # block $label126
                                                                    if (u(v3) < u(v17)):
                                                                        while True:  # $label125
                                                                            while True:  # block $label124
                                                                                if (load8u((v21 + (((v1 - v2) * v14) + v18))) == 0):
                                                                                    v1 = (v1 + 1)
                                                                                    break
                                                                                if (u(v1) >= u(v17)):
                                                                                    break
                                                                                if ((v1 | v3) < 0):
                                                                                    break
                                                                                v1 = (v1 + 1)
                                                                                if (load32((v30 + (((((v1 + 1) + v22) * v25) + v5) << 2))) != v23):
                                                                                    break
                                                                                break
                                                                            if (v1 != v19):
                                                                                continue
                                                                            break
                                                                            break
                                                                        raise RuntimeError('unreachable')
                                                                    while True:  # $label127
                                                                        if load8u((v21 + (((v1 - v2) * v14) + v18))):
                                                                            break
                                                                        v1 = (v1 + 1)
                                                                        if ((v1 + 1) != v19):
                                                                            continue
                                                                        break
                                                                    break
                                                                v3 = v5
                                                                if (v5 < v24):
                                                                    continue
                                                                break
                                                            break
                                                            break
                                                        v3 = load32(v10 + 208)
                                                        if (load32(v10 + 208) == 0):
                                                            v14 = load32(v10 + 216)
                                                            if (load32(v10 + 216) <= 0):
                                                                break
                                                            v21 = (load32(v10 + 220) + v2)
                                                            if ((load32(v10 + 220) + v2) <= v2):
                                                                break
                                                            v22 = (v4 + v14)
                                                            v18 = load32(v10 + 372)
                                                            v19 = (v17 + 2)
                                                            v23 = load32(9671128)
                                                            v24 = load32(9142840)
                                                            v3 = v4
                                                            while True:  # $label133
                                                                v5 = (v3 + 1)
                                                                v25 = (v3 - v4)
                                                                v1 = v2
                                                                while True:  # block $label131
                                                                    if (u(v3) < u(v17)):
                                                                        while True:  # $label130
                                                                            while True:  # block $label129
                                                                                if (load8u((v18 + (((v1 - v2) * v14) + v25))) == 0):
                                                                                    v1 = (v1 + 1)
                                                                                    break
                                                                                if (u(v1) >= u(v17)):
                                                                                    break
                                                                                if ((v1 | v3) < 0):
                                                                                    break
                                                                                v1 = (v1 + 1)
                                                                                if load32((v24 + ((((v1 + 1) * v19) + v5) << 2))):
                                                                                    break
                                                                                if (load32(((load8u((v23 + (load32((v24 + ((((v1 + v19) * v19) + v5) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 1):
                                                                                    break
                                                                                break
                                                                            if (v1 != v21):
                                                                                continue
                                                                            break
                                                                            break
                                                                        raise RuntimeError('unreachable')
                                                                    while True:  # $label132
                                                                        if load8u((v18 + (((v1 - v2) * v14) + v25))):
                                                                            break
                                                                        v1 = (v1 + 1)
                                                                        if ((v1 + 1) != v21):
                                                                            continue
                                                                        break
                                                                    break
                                                                v3 = v5
                                                                if (v5 < v22):
                                                                    continue
                                                                break
                                                            break
                                                        while True:  # block $label136
                                                            while True:  # block $label135
                                                                while True:  # block $label134
                                                                    # br_table[(v1 - 4)]
                                                                    break
                                                                    break
                                                                if (func193(v4, v2, v10, v11, 0, 0, 1, 0) == 0):
                                                                    break
                                                                break
                                                                break
                                                            if (func194(v4, v2, v10, v11, 0, 0, 1) == 0):
                                                                break
                                                            break
                                                            break
                                                        if (u(v3) > u(2)):
                                                            break
                                                        if func73(v4, v2, v10, 0, 0, 1):
                                                            break
                                                        break
                                                    v17 = load32(9142440)
                                                    break
                                                v1 = (v8 + 2)
                                                if (u(v8) < u(5198)):
                                                    continue
                                                break
                                        v4 = v7
                                        v2 = v9
                                        break
                                    v20 = (1 if func34(v6, v11, v4, v2, v29, 1) else v20)
                                    v15 = (v15 + 1)
                                    v1 = load32(9142416)
                                    continue
                                break
                            break
                        v1 = v20
                        if (v20 == 0):
                            v2 = (u(v0) < u(24))
                            v0 = (v0 + 1)
                            if v2:
                                continue
                        break
                    while True:  # block $label140
                        if (v26 == 0):
                            break
                        if (v1 == 0):
                            break
                        v0 = (load32(9671128) + (v1 * 132))
                        v1 = load32(v13 + 20)
                        if (u(load32(v13 + 20)) <= u(2147483646)):
                            store32(v0 + 52, v1)
                        v1 = load32(v13 + 24)
                        if (u(load32(v13 + 24)) <= u(2147483646)):
                            store32(v0 + 60, v1)
                        while True:  # block $label141
                            v1 = load32(v13 + 28)
                            if (u(load32(v13 + 28)) > u(2147483646)):
                                break
                            store32(v0 + 64, v1)
                            if (u(load32(v13 + 28)) > u(2147483646)):
                                break
                            store32(v0 + 68, load32(v13 + 32))
                            break
                        v2 = load32(v0 + 76)
                        while True:  # block $label142
                            v1 = load32(v13 + 36)
                            if (u(load32(v13 + 36)) > u(2147483646)):
                                break
                            store32(v0 + 72, v1)
                            if (u(load32(v13 + 36)) > u(2147483646)):
                                break
                            store32(v0 + 76, load32(v13 + 40))
                            break
                        v1 = load32(v13 + 44)
                        if (u(load32(v13 + 44)) <= u(2147483646)):
                            store32(v0 + 84, v1)
                        v3 = ((load8u(v0 + 122) * 404) + 9568096)
                        v1 = load32(((load8u(v0 + 122) * 404) + 9568096) + 264)
                        while True:  # block $label143
                            if (load32(v3 + 92) == 0):
                                if (v1 == 2):
                                    break
                                store32(v0 + 52, 0)
                            if (v1 != 1):
                                break
                            store32(v0 + 84, 0)
                            store32(v0 + 72, 0)
                            store32(v0 + 60, 0)
                            break
                        v1 = load32(v0 + 64)
                        if load32(v0 + 64):
                        else:
                            store32((v0 - -64), -1)
                        store32(v1 + 68, -1)
                        v1 = load32(v0 + 72)
                        store32(v0 + 76, load32(v0 + 72))
                        if (v1 == 0):
                            break
                        if v2:
                            break
                        break
                    v12 = (v12 + 1)
                    if ((v12 + 1) != v28):
                        continue
                    break
                v8 = load32(9142428)
                break
            v0 = (v27 + 5)
            if (u((v27 + 5)) < u(v8)):
                continue
            break
    store32(9684376, load32(9671136))
    while True:  # block $label146
        if (u((load32(load32(9142424) + 60) << 1)) < u(200)):
            break
        v16 = 0
        v1 = load32(9142440)
        if (load32(9142440) <= 0):
            break
        while True:  # $label148
            v0 = 0
            while True:  # $label147
                v4 = load32(38448)
                v6 = load32(load32(((load32(38448) * 72) + 9263856)) + 20)
                v2 = load32(9147324)
                store32(9147324, load32(9147320))
                v12 = load32(9147316)
                v3 = load32(9147312)
                store32(9147316, load32(9147312))
                store32(9147320, v12)
                v2 = (v2 ^ (v2 << 11))
                v2 = ((v3 ^ (((v3 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2)
                store32(9147312, ((v3 ^ (((v3 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2))
                v0 = (v0 + 1)
                if ((v0 + 1) != v1):
                    continue
                break
            v16 = (v16 + 1)
            if ((v16 + 1) != v1):
                continue
            break
        break
    store32(9684380, (load32(9671136) - load32(9684376)))
    v11 = 1
    if (u(load32(9142892)) > u(1)):
        while True:  # $label163
            while True:  # block $label149
                v4 = (load32(9561692) + (v11 * 286704))
                if (load32((load32(9561692) + (v11 * 286704)) + 284624) == 0):
                    break
                while True:  # block $label150
                    v6 = load32(v4 + 283872)
                    v9 = (load32(v4 + 283872) - 25)
                    v7 = (v6 + 50)
                    if ((load32(v4 + 283872) - 25) >= (v6 + 50)):
                        break
                    v12 = load32(v4 + 283876)
                    v2 = (load32(v4 + 283876) - 25)
                    v8 = (v12 + 50)
                    if ((load32(v4 + 283876) - 25) >= (v12 + 50)):
                        break
                    while True:  # $label153
                        v1 = (v9 + 1)
                        v0 = (v9 - v6)
                        v10 = (((v9 - v6) * v0) - 1)
                        v0 = v2
                        while True:  # $label152
                            while True:  # block $label151
                                v3 = (v0 - v12)
                                if ((v10 + ((v0 - v12) * v3)) > 625):
                                    break
                                v3 = load32(9142440)
                                if (u(load32(9142440)) <= u(v0)):
                                    break
                                if ((v0 | v9) < 0):
                                    break
                                if (u(v3) <= u(v9)):
                                    break
                                v3 = (v3 + 2)
                                v3 = (load32(9671128) + (load32((load32(9142840) + ((v1 + (((v0 + (v3 + 2)) + 1) * v3)) << 2))) * 132))
                                if (load32(38448) != load8u((load32(9671128) + (load32((load32(9142840) + ((v1 + (((v0 + (v3 + 2)) + 1) * v3)) << 2))) * 132)) + 122)):
                                    break
                                v5 = func26(4)
                                v13 = (func26(4) + 4)
                                v16 = load32(v3)
                                if load32(v3):
                                    store32(v3 + 4, v16)
                                store32(v3 + 8, v13)
                                store32(v3 + 4, v5)
                                store32(v3, v5)
                                # TODO: memory.fill []
                                break
                            v0 = (v0 + 1)
                            if ((v0 + 1) != v8):
                                continue
                            break
                        v9 = v1
                        if (v1 != v7):
                            continue
                        break
                    break
                v0 = load32(9142424)
                if (u((load32(load32(9142424) + 60) << 1)) < u(5)):
                    break
                if load32(v0 + 64):
                    break
                v5 = 0
                if (load32(9147128) == 9):
                    break
                v12 = (v4 + 283876)
                v9 = (v4 + 283872)
                while True:  # $label162
                    v3 = load32(v12)
                    v4 = load32(v9)
                    v0 = load32(9147324)
                    store32(9147324, load32(9147320))
                    v2 = load32(9147316)
                    v1 = load32(9147312)
                    store32(9147316, load32(9147312))
                    store32(9147320, v2)
                    v0 = (v0 ^ (v0 << 11))
                    v0 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0)
                    store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0))
                    v33 = ((float((v0 % 100)) / 100.0) * 6.28318548)
                    v0 = load32(9142440)
                    while True:  # $label155
                        while True:  # block $label154
                            v34 = v33
                            v33 = (func49(v33) * 20.0)
                            if (abs((func49(v33) * 20.0)) < 2147483650.0):
                                break
                            break
                        v1 = -2147483648
                        v33 = (v34 + 1.57079637)
                        v1 = (v1 + v4)
                        if ((v1 + v4) <= 0):
                            continue
                        if (u(v0) <= u(v1)):
                            continue
                        while True:  # block $label156
                            v34 = (func48(v34) * 20.0)
                            if (abs((func48(v34) * 20.0)) < 2147483650.0):
                                break
                            break
                        v2 = (-2147483648 + v3)
                        if ((-2147483648 + v3) <= 0):
                            continue
                        if (u(v0) <= u(v2)):
                            continue
                        break
                    v16 = (v2 - 10)
                    v7 = (v1 - 10)
                    v10 = 0
                    v8 = load32(load32(9142424) + 64)
                    while True:  # $label161
                        v1 = load32(38448)
                        v13 = load32(load32(((load32(38448) * 72) + 9263856)) + 20)
                        v0 = load32(9147320)
                        v3 = ((load32(9147320) << 11) ^ v0)
                        v2 = load32(9147312)
                        v0 = load32(9147324)
                        v0 = ((load32(9147324) << 11) ^ v0)
                        v0 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v2) ^ v0)
                        v3 = (((((((load32(9147320) << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ (((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v2) ^ v0) & 0xFFFFFFFF) >> 19)) ^ v3) ^ v0)
                        store32(9147324, (((((((load32(9147320) << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ (((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v2) ^ v0) & 0xFFFFFFFF) >> 19)) ^ v3) ^ v0))
                        v4 = load32(9147316)
                        v4 = ((load32(9147316) << 11) ^ v4)
                        v4 = (((((((load32(9147316) << 11) ^ v4) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v4) ^ v3)
                        store32(9147320, (((((((load32(9147316) << 11) ^ v4) & 0xFFFFFFFF) >> 8) ^ ((v3 & 0xFFFFFFFF) >> 19)) ^ v4) ^ v3))
                        v2 = (v2 ^ (v2 << 11))
                        v2 = ((((((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v4)
                        store32(9147316, ((((((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v4))
                        v6 = ((v0 << 11) ^ v0)
                        v6 = (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v6) ^ v2)
                        store32(9147312, (((((((v0 << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v6) ^ v2))
                        v6 = ((v16 + (v2 % 13)) + (v6 & 7))
                        v3 = ((v7 + (v3 % 13)) + (v4 & 7))
                        v4 = ((v0 % (v13 - 3)) + 3)
                        while True:  # block $label157
                            if (v8 == 0):
                                break
                            v0 = load32(9142416)
                            v2 = load32(9142416)
                            if (v0 == 0):
                                v2 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                            # TODO: f32.convert_i32_u []
                            v34 = (6.28318548 / (4 if (u(v2) < u(3)) else (v2 << (v2 & 1))))
                            v2 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                            v6 = (v6 - ((load32(9142440) & 0xFFFFFFFF) >> 1))
                            v3 = (v3 - v2)
                            # TODO: f32.demote_f64 []
                            v33 = func262(float((v6 - ((load32(9142440) & 0xFFFFFFFF) >> 1))), float((v3 - v2)))
                            if ((6.28318548 / (4 if (u(v2) < u(3)) else (v2 << (v2 & 1)))) < func262(float((v6 - ((load32(9142440) & 0xFFFFFFFF) >> 1))), float((v3 - v2)))):
                                break
                            if (v33 < 0.0):
                                break
                            # TODO: f32.demote_f64 []
                            v36 = sqrt(float(((v3 * v3) + (v6 * v6))))
                            # TODO: f32.convert_i32_u []
                            if (sqrt(float(((v3 * v3) + (v6 * v6)))) >= v2):
                                break
                            v38 = (v34 - v33)
                            v3 = ((v1 * 404) + 9568096)
                            v2 = 0
                            while True:  # $label160
                                if (v0 == 0):
                                    v0 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                                if (u(v2) >= u((4 if (u(v0) < u(3)) else (v0 << (v0 & 1))))):
                                    break
                                # TODO: f32.convert_i32_u []
                                v37 = ((v34 * v2) + (v38 if (v2 & 1) else v33))
                                v35 = func48(((v34 * v2) + (v38 if (v2 & 1) else v33)))
                                while True:  # block $label158
                                    # TODO: f64.convert_i32_u []
                                    # TODO: f64.promote_f32 []
                                    # TODO: f64.convert_i32_u []
                                    v41 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                                    v42 = (((0.5 - (load32(v3 + 220) * 0.5)) + (v35 * v36)) + ((load32(9142440) & 0xFFFFFFFF) >> 1))
                                    if (abs((((0.5 - (load32(v3 + 220) * 0.5)) + (v35 * v36)) + ((load32(9142440) & 0xFFFFFFFF) >> 1))) < 2147483648.0):
                                        break
                                    break
                                v0 = -2147483648
                                v37 = func49(v37)
                                while True:  # block $label159
                                    # TODO: f64.convert_i32_u []
                                    # TODO: f64.promote_f32 []
                                    v41 = (((0.5 - (load32(v3 + 216) * 0.5)) + (v37 * v36)) + v41)
                                    if (abs((((0.5 - (load32(v3 + 216) * 0.5)) + (v37 * v36)) + v41)) < 2147483648.0):
                                        break
                                    break
                                v2 = (v2 + 1)
                                v0 = load32(9142416)
                                continue
                                break
                            raise RuntimeError('unreachable')
                            break
                        v10 = (v10 + 1)
                        if ((v10 + 1) != 55):
                            continue
                        break
                    v5 = (v5 + 1)
                    if ((v5 + 1) != 4):
                        continue
                    break
                break
            v11 = (v11 + 1)
            if (u((v11 + 1)) < u(load32(9142892))):
                continue
            break
    while True:  # block $label164
        v0 = load32(9142424)
        if (u((load32(load32(9142424) + 60) << 1)) <= u(4)):
            break
        if (load32(v0 + 64) == 0):
            break
        v0 = load32(9561692)
        v3 = load32((load32(9561692) + 570580))
        v4 = load32((v0 + 570576))
        v0 = load32(9147324)
        store32(9147324, load32(9147320))
        v2 = load32(9147316)
        v1 = load32(9147312)
        store32(9147316, load32(9147312))
        store32(9147320, v2)
        v0 = (v0 ^ (v0 << 11))
        v0 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0)
        store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0))
        v33 = ((float((v0 % 100)) / 100.0) * 6.28318548)
        v0 = load32(9142440)
        while True:  # $label166
            while True:  # block $label165
                v34 = v33
                v33 = (func49(v33) * 20.0)
                if (abs((func49(v33) * 20.0)) < 2147483650.0):
                    break
                break
            v1 = -2147483648
            v33 = (v34 + 1.57079637)
            v1 = (v1 + v4)
            if ((v1 + v4) <= 0):
                continue
            if (u(v0) <= u(v1)):
                continue
            while True:  # block $label167
                v34 = (func48(v34) * 20.0)
                if (abs((func48(v34) * 20.0)) < 2147483650.0):
                    break
                break
            v2 = (-2147483648 + v3)
            if ((-2147483648 + v3) <= 0):
                continue
            if (u(v0) <= u(v2)):
                continue
            break
        v0 = load32(9561692)
        v3 = load32((load32(9561692) + 570580))
        v4 = load32((v0 + 570576))
        v0 = load32(9147324)
        store32(9147324, load32(9147320))
        v2 = load32(9147316)
        v1 = load32(9147312)
        store32(9147316, load32(9147312))
        store32(9147320, v2)
        v0 = (v0 ^ (v0 << 11))
        v0 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0)
        store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0))
        v33 = ((float((v0 % 100)) / 100.0) * 6.28318548)
        v0 = load32(9142440)
        while True:  # $label169
            while True:  # block $label168
                v34 = v33
                v33 = (func49(v33) * 20.0)
                if (abs((func49(v33) * 20.0)) < 2147483650.0):
                    break
                break
            v1 = -2147483648
            v33 = (v34 + 1.57079637)
            v1 = (v1 + v4)
            if ((v1 + v4) <= 0):
                continue
            if (u(v0) <= u(v1)):
                continue
            while True:  # block $label170
                v34 = (func48(v34) * 20.0)
                if (abs((func48(v34) * 20.0)) < 2147483650.0):
                    break
                break
            v2 = (-2147483648 + v3)
            if ((-2147483648 + v3) <= 0):
                continue
            if (u(v0) <= u(v2)):
                continue
            break
        v0 = load32(9561692)
        v3 = load32((load32(9561692) + 570580))
        v4 = load32((v0 + 570576))
        v0 = load32(9147324)
        store32(9147324, load32(9147320))
        v2 = load32(9147316)
        v1 = load32(9147312)
        store32(9147316, load32(9147312))
        store32(9147320, v2)
        v0 = (v0 ^ (v0 << 11))
        v0 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0)
        store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0))
        v33 = ((float((v0 % 100)) / 100.0) * 6.28318548)
        v0 = load32(9142440)
        while True:  # $label172
            while True:  # block $label171
                v34 = v33
                v33 = (func49(v33) * 20.0)
                if (abs((func49(v33) * 20.0)) < 2147483650.0):
                    break
                break
            v1 = -2147483648
            v33 = (v34 + 1.57079637)
            v1 = (v1 + v4)
            if ((v1 + v4) <= 0):
                continue
            if (u(v0) <= u(v1)):
                continue
            while True:  # block $label173
                v34 = (func48(v34) * 20.0)
                if (abs((func48(v34) * 20.0)) < 2147483650.0):
                    break
                break
            v2 = (-2147483648 + v3)
            if ((-2147483648 + v3) <= 0):
                continue
            if (u(v0) <= u(v2)):
                continue
            break
        v0 = load32(9561692)
        v3 = load32((load32(9561692) + 570580))
        v4 = load32((v0 + 570576))
        v0 = load32(9147324)
        store32(9147324, load32(9147320))
        v2 = load32(9147316)
        v1 = load32(9147312)
        store32(9147316, load32(9147312))
        store32(9147320, v2)
        v0 = (v0 ^ (v0 << 11))
        v0 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0)
        store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v0 ^ (v0 << 11)) & 0xFFFFFFFF) >> 8))) ^ v0))
        v33 = ((float((v0 % 100)) / 100.0) * 6.28318548)
        v0 = load32(9142440)
        while True:  # $label175
            while True:  # block $label174
                v34 = v33
                v33 = (func49(v33) * 20.0)
                if (abs((func49(v33) * 20.0)) < 2147483650.0):
                    break
                break
            v1 = -2147483648
            v33 = (v34 + 1.57079637)
            v1 = (v1 + v4)
            if ((v1 + v4) <= 0):
                continue
            if (u(v0) <= u(v1)):
                continue
            while True:  # block $label176
                v34 = (func48(v34) * 20.0)
                if (abs((func48(v34) * 20.0)) < 2147483650.0):
                    break
                break
            v2 = (-2147483648 + v3)
            if ((-2147483648 + v3) <= 0):
                continue
            if (u(v0) <= u(v2)):
                continue
            break
        break
    v0 = 0
    while True:  # block $label177
        v2 = load32(9561692)
        v1 = load32(((load32(9561692) + (load32(38508) << 2)) + 284636))
        if (load32(((load32(9561692) + (load32(38508) << 2)) + 284636)) == 0):
            break
        v3 = load32(v1 + 8)
        if (load32(v1 + 8) == 0):
            break
        while True:  # $label178
            v2 = load32((load32(v1) + (v0 << 2)))
            if load32((load32(v1) + (v0 << 2))):
                func408(load32(38492), (load32(9671128) + (v2 * 132)))
            v0 = (v0 + 1)
            if ((v0 + 1) != v3):
                continue
            break
        v2 = load32(9561692)
        break
    v0 = 0
    while True:  # block $label179
        v1 = load32(((v2 + (load32(38504) << 2)) + 284636))
        if (load32(((v2 + (load32(38504) << 2)) + 284636)) == 0):
            break
        v2 = load32(v1 + 8)
        if (load32(v1 + 8) == 0):
            break
        while True:  # $label180
            v3 = load32((load32(v1) + (v0 << 2)))
            if load32((load32(v1) + (v0 << 2))):
                func408(load32(38492), (load32(9671128) + (v3 * 132)))
            v0 = (v0 + 1)
            if ((v0 + 1) != v2):
                continue
            break
        break
    return func126(v1, v2, 13, 13, (load32(load32(9142424) + 64) != 0))

# ------------------------------------------------------------
# $func351
# ------------------------------------------------------------
def func351(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
    v14 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v19 = load8u(arg0 + 122)
    while True:  # block $label0
        v11 = load32(9671128)
        v18 = (load32(9671128) + (arg3 * 132))
        v12 = load8u((load32(9671128) + (arg3 * 132)) + 122)
        if ((arg4 != -1) & (load8u((load32(9671128) + (arg3 * 132)) + 122) != arg4)):
            break
        v16 = load16u(v18 + 110)
        while True:  # block $label1
            if (load32(38500) == v12):
                break
            v13 = (load32(9142892) * arg6)
            v15 = load32(9143004)
            while True:  # block $label2
                v17 = load16u((v11 + (arg3 * 132)) + 120)
                if load16u((v11 + (arg3 * 132)) + 120):
                else:
                if (load8u(((v17 if load8u((v15 + (v13 + v16))) else v16) + (v16 + v13))) == 0):
                    arg5 = (v11 + (arg3 * 132))
                    if ((arg5 == 0) & (load8u((v11 + (arg3 * 132)) + 127) != 6)):
                        break
                    if (load8u(arg5 + 128) == 0):
                        break
                    break
                if load8u((v11 + (arg3 * 132)) + 128):
                    break
                break
            arg5 = (v11 + (arg3 * 132))
            v13 = load8u((v11 + (arg3 * 132)) + 125)
            if (load8u((v11 + (arg3 * 132)) + 125) == 10):
                break
            if (load8u(arg5 + 126) == 2):
                break
            v15 = load32(arg5 + 64)
            if (load32(arg5 + 64) == -1):
                break
            arg5 = ((v12 * 404) + 9568096)
            v17 = load32(((v12 * 404) + 9568096) + 264)
            if (load32(((v12 * 404) + 9568096) + 264) == 2):
                break
            if (load32(arg5 + 188) != 55):
                break
            if (load32(38560) == v12):
                break
            if (load32(38620) == v12):
                break
            if (load32(38564) == v12):
                break
            v20 = load32((v11 + (arg3 * 132)) + 28)
            if (func162(arg0, v12, v13, load32((v11 + (arg3 * 132)) + 28)) == 0):
                break
            v21 = load32(arg8 + 286684)
            if load32(arg8 + 286684):
                while True:  # block $label5
                    while True:  # block $label3
                        while True:  # block $label4
                            # br_table[v17]
                            break
                            break
                        arg8 = ((v12 * 404) + 9568096)
                        v22 = load32(((v12 * 404) + 9568096) + 216)
                        if (load32(((v12 * 404) + 9568096) + 216) == 0):
                            arg5 = 0
                            break
                        arg5 = 0
                        v23 = load32(arg8 + 220)
                        if (load32(arg8 + 220) == 0):
                            break
                        arg8 = load32(9215880)
                        if (load32(9215880) == 0):
                            break
                        v24 = load32(9142432)
                        if (load32(9142432) == 0):
                            break
                        arg5 = (v11 + (arg3 * 132))
                        v25 = load16u((v11 + (arg3 * 132)) + 114)
                        v26 = load16u(arg5 + 112)
                        v27 = load32(9142440)
                        v28 = load32(arg8)
                        v13 = 0
                        while True:  # $label7
                            v29 = (v13 + v26)
                            arg8 = 0
                            while True:  # $label6
                                arg5 = load32((v24 + ((v29 + ((arg8 + v25) * v27)) << 2)))
                                if (load32((v28 + (load32((v24 + ((v29 + ((arg8 + v25) * v27)) << 2))) << 2))) == 0):
                                    break
                                arg8 = (arg8 + 1)
                                if ((arg8 + 1) != v23):
                                    continue
                                break
                            arg5 = 0
                            v13 = (v13 + 1)
                            if ((v13 + 1) != v22):
                                continue
                            break
                        break
                        break
                    arg5 = 0
                    arg8 = load32(9142432)
                    if (load32(9142432) == 0):
                        break
                    arg5 = (v11 + (arg3 * 132))
                    arg5 = load32((arg8 + (((load32(9142440) * load16u((v11 + (arg3 * 132)) + 114)) + load16u(arg5 + 112)) << 2)))
                    break
                if (arg5 != arg7):
                    break
            while True:  # block $label8
                if (arg4 != -1):
                    break
                if v21:
                    break
                if (load8u(((v12 * 404) + 9568096) + 380) == 0):
                    break
                if (u(v15) > u(1)):
                    break
                break
            arg4 = load32(((v19 * 404) + 9568096) + 228)
            if load32(((v19 * 404) + 9568096) + 228):
                arg5 = (load16u(arg0 + 114) - arg10)
                arg5 = (load16u(arg0 + 112) - arg9)
                if (u((((load16u(arg0 + 114) - arg10) * arg5) + ((load16u(arg0 + 112) - arg9) * arg5))) < u((arg4 * arg4))):
                    break
            arg4 = load32((v11 + (arg3 * 132)) + 100)
            if load32((v11 + (arg3 * 132)) + 100):
                arg4 = (v11 + (arg4 * 132))
                # TODO: i32.div_u []
                if (u((load32((((load8u((v11 + (arg4 * 132)) + 122) * 1020) + 9299904) + (v12 << 2))) * load32(arg4 + 52))) < u(100)):
                    break
            if (v17 == 1):
                if (u(load32((v11 + (arg3 * 132)) + 84)) < u(load32(((v12 * 404) + 9568096) + 112))):
                    break
            arg5 = (load32(9671128) + (v20 * 132))
            arg4 = (load16u(arg0 + 114) - load16u((load32(9671128) + (v20 * 132)) + 114))
            arg4 = (load16u(arg0 + 112) - load16u(arg5 + 112))
            arg4 = (((load16u(arg0 + 114) - load16u((load32(9671128) + (v20 * 132)) + 114)) * arg4) + ((load16u(arg0 + 112) - load16u(arg5 + 112)) * arg4))
            arg5 = ((load8u(arg5 + 122) * 404) + 9568096)
            if (load32(((load8u(arg5 + 122) * 404) + 9568096) + 264) == 1):
                arg4 = (arg4 if (load32(arg5 + 268) == 1) else (arg4 + 100))
            if (load32(arg1) <= arg4):
                break
            if (load32(arg0 + 28) == arg3):
                break
            store32(arg2, arg3)
            store32(arg1, arg4)
            break
        if (load8u(((v19 * 404) + 9568096) + 336) == 0):
            break
        if (load8u((load32(9143004) + ((load32(9142892) * v16) + arg6))) == 0):
            break
        while True:  # block $label9
            arg0 = (v11 + (arg3 * 132))
            if (load8u((v11 + (arg3 * 132)) + 125) == 3):
                break
            if (load8u(arg0 + 128) == 0):
                break
            arg1 = (v11 + (arg3 * 132))
            store8((v11 + (arg3 * 132)) + 127, 0)
            while True:  # block $label10
                arg1 = load32(arg1 + 40)
                if (load32(arg1 + 40) == 0):
                    break
                if load8u(9142916):
                    store32(v14 + 20, arg1)
                    store32(v14 + 16, 0)
                    a_b()
                    break
                arg2 = load16u(v18 + 110)
                store32(v14 + 4, arg1)
                store32(v14, (arg2 + 16))
                a_b()
                break
            store8(arg0 + 128, 0)
            break
        func290(v18)
        break
    G.global0 = (v14 + 32)
    return v14

# ------------------------------------------------------------
# $func352
# ------------------------------------------------------------
def func352(arg0, arg1, arg2, arg3, arg4):
    v7 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    store32(v7 + 76, arg1)
    v21 = (v7 + 55)
    v17 = (v7 + 56)
    while True:  # block $label65
        while True:  # block $label62
            while True:  # block $label15
                while True:  # block $label0
                    while True:  # $label4
                        v9 = arg1
                        if (v5 > (v13 ^ 2147483647)):
                            break
                        v13 = (v5 + v13)
                        while True:  # block $label18
                            while True:  # block $label21
                                while True:  # block $label10
                                    v5 = v9
                                    v6 = load8u(v9)
                                    if load8u(v9):
                                        while True:  # $label64
                                            while True:  # block $label2
                                                while True:  # block $label1
                                                    arg1 = (v6 & 255)
                                                    if ((v6 & 255) == 0):
                                                        arg1 = v5
                                                        break
                                                    if (arg1 != 37):
                                                        break
                                                    v6 = v5
                                                    while True:  # $label3
                                                        if (load8u(v6 + 1) != 37):
                                                            arg1 = v6
                                                            break
                                                        v5 = (v5 + 1)
                                                        v10 = load8u(v6 + 2)
                                                        arg1 = (v6 + 2)
                                                        v6 = (v6 + 2)
                                                        if (v10 == 37):
                                                            continue
                                                        break
                                                    break
                                                v5 = (v5 - v9)
                                                v22 = (v13 ^ 2147483647)
                                                if ((v5 - v9) > (v13 ^ 2147483647)):
                                                    break
                                                if arg0:
                                                if v5:
                                                    continue
                                                store32(v7 + 76, arg1)
                                                v5 = (arg1 + 1)
                                                v15 = -1
                                                while True:  # block $label5
                                                    if (u((load8s(arg1 + 1) - 48)) >= u(10)):
                                                        break
                                                    if (load8u(arg1 + 2) != 36):
                                                        break
                                                    v5 = (arg1 + 3)
                                                    v15 = (load8s(arg1 + 1) - 48)
                                                    v18 = 1
                                                    break
                                                store32(v7 + 76, v5)
                                                v11 = 0
                                                while True:  # block $label6
                                                    v6 = load8s(v5)
                                                    arg1 = (load8s(v5) - 32)
                                                    if (u((load8s(v5) - 32)) > u(31)):
                                                        v10 = v5
                                                        break
                                                    v10 = v5
                                                    arg1 = (1 << arg1)
                                                    if (((1 << arg1) & 75913) == 0):
                                                        break
                                                    while True:  # $label7
                                                        v10 = (v5 + 1)
                                                        store32(v7 + 76, (v5 + 1))
                                                        v11 = (arg1 | v11)
                                                        v6 = load8s(v5 + 1)
                                                        arg1 = (load8s(v5 + 1) - 32)
                                                        if (u((load8s(v5 + 1) - 32)) >= u(32)):
                                                            break
                                                        v5 = v10
                                                        arg1 = (1 << arg1)
                                                        if ((1 << arg1) & 75913):
                                                            continue
                                                        break
                                                    break
                                                while True:  # block $label11
                                                    if (v6 == 42):
                                                        while True:  # block $label9
                                                            while True:  # block $label8
                                                                if (u((load8s(v10 + 1) - 48)) >= u(10)):
                                                                    break
                                                                if (load8u(v10 + 2) != 36):
                                                                    break
                                                                store32((((load8s(v10 + 1) << 2) + arg4) - 192), 10)
                                                                v6 = (v10 + 3)
                                                                v18 = 1
                                                                break
                                                                break
                                                            if v18:
                                                                break
                                                            v6 = (v10 + 1)
                                                            if (arg0 == 0):
                                                                store32(v7 + 76, v6)
                                                                v18 = 0
                                                                v16 = 0
                                                                break
                                                            arg1 = load32(arg2)
                                                            store32(arg2, (load32(arg2) + 4))
                                                            v18 = 0
                                                            break
                                                        v16 = load32(arg1)
                                                        store32(v7 + 76, v6)
                                                        if (v16 >= 0):
                                                            break
                                                        v16 = (0 - v16)
                                                        v11 = (v11 | 8192)
                                                        break
                                                    v16 = func371((v7 + 76))
                                                    if (func371((v7 + 76)) < 0):
                                                        break
                                                    v6 = load32(v7 + 76)
                                                    break
                                                v5 = 0
                                                v8 = -1
                                                while True:  # block $label12
                                                    if (load8u(v6) != 46):
                                                        arg1 = v6
                                                        break
                                                    if (load8u(v6 + 1) == 42):
                                                        while True:  # block $label14
                                                            while True:  # block $label13
                                                                if (u((load8s(v6 + 2) - 48)) >= u(10)):
                                                                    break
                                                                if (load8u(v6 + 3) != 36):
                                                                    break
                                                                store32((((load8s(v6 + 2) << 2) + arg4) - 192), 10)
                                                                arg1 = (v6 + 4)
                                                                break
                                                                break
                                                            if v18:
                                                                break
                                                            arg1 = (v6 + 2)
                                                            if (arg0 == 0):
                                                                break
                                                            v6 = load32(arg2)
                                                            store32(arg2, (load32(arg2) + 4))
                                                            break
                                                        v8 = load32(v6)
                                                        store32(v7 + 76, arg1)
                                                        break
                                                    store32(v7 + 76, (v6 + 1))
                                                    v8 = func371((v7 + 76))
                                                    arg1 = load32(v7 + 76)
                                                    break
                                                v19 = 1
                                                while True:  # $label16
                                                    v14 = v5
                                                    v10 = 28
                                                    v12 = arg1
                                                    v5 = load8s(arg1)
                                                    if (u((load8s(arg1) - 123)) < u(-58)):
                                                        break
                                                    arg1 = (v12 + 1)
                                                    v5 = load8u(((v5 + (v14 * 58)) + 31711))
                                                    if (u((load8u(((v5 + (v14 * 58)) + 31711)) - 1)) < u(8)):
                                                        continue
                                                    break
                                                store32(v7 + 76, arg1)
                                                while True:  # block $label19
                                                    while True:  # block $label17
                                                        if (v5 != 27):
                                                            if (v5 == 0):
                                                                break
                                                            if (v15 >= 0):
                                                                store32((arg4 + (v15 << 2)), v5)
                                                                store64(v7 + 64, load64((arg3 + (v15 << 3))))
                                                                break
                                                            if (arg0 == 0):
                                                                break
                                                            func353((v7 - -64), v5, arg2)
                                                            break
                                                        if (v15 >= 0):
                                                            break
                                                        break
                                                    v5 = 0
                                                    if (arg0 == 0):
                                                        continue
                                                    break
                                                v6 = (v11 & -65537)
                                                v11 = ((v11 & -65537) if (v11 & 8192) else v11)
                                                v15 = 0
                                                v20 = 2107
                                                v10 = v17
                                                while True:  # block $label23
                                                    while True:  # block $label22
                                                        while True:  # block $label58
                                                            while True:  # block $label57
                                                                while True:  # block $label31
                                                                    while True:  # block $label33
                                                                        while True:  # block $label28
                                                                            while True:  # block $label43
                                                                                while True:  # block $label34
                                                                                    while True:  # block $label24
                                                                                        while True:  # block $label26
                                                                                            while True:  # block $label20
                                                                                                while True:  # block $label27
                                                                                                    while True:  # block $label25
                                                                                                        while True:  # block $label29
                                                                                                            while True:  # block $label30
                                                                                                                v5 = load8s(v12)
                                                                                                                v5 = (((load8s(v12) & -33) if ((v5 & 15) == 3) else v5) if v14 else v5)
                                                                                                                # br_table[((((load8s(v12) & -33) if ((v5 & 15) == 3) else v5) if v14 else v5) - 88)]
                                                                                                                break
                                                                                                                break
                                                                                                            while True:  # block $label32
                                                                                                                # br_table[(v5 - 65)]
                                                                                                                break
                                                                                                                break
                                                                                                            if (v5 == 83):
                                                                                                                break
                                                                                                            break
                                                                                                            break
                                                                                                        v23 = load64(v7 + 64)
                                                                                                        break
                                                                                                        break
                                                                                                    v5 = 0
                                                                                                    while True:  # block $label41
                                                                                                        while True:  # block $label40
                                                                                                            while True:  # block $label39
                                                                                                                while True:  # block $label38
                                                                                                                    while True:  # block $label37
                                                                                                                        while True:  # block $label36
                                                                                                                            while True:  # block $label35
                                                                                                                                # br_table[(v14 & 255)]
                                                                                                                                break
                                                                                                                                break
                                                                                                                            store32(load32(v7 + 64), v13)
                                                                                                                            continue
                                                                                                                            break
                                                                                                                        store32(load32(v7 + 64), v13)
                                                                                                                        continue
                                                                                                                        break
                                                                                                                    store64(load32(v7 + 64), i64(v13))
                                                                                                                    continue
                                                                                                                    break
                                                                                                                store16(load32(v7 + 64), v13)
                                                                                                                continue
                                                                                                                break
                                                                                                            store8(load32(v7 + 64), v13)
                                                                                                            continue
                                                                                                            break
                                                                                                        store32(load32(v7 + 64), v13)
                                                                                                        continue
                                                                                                        break
                                                                                                    store64(load32(v7 + 64), i64(v13))
                                                                                                    continue
                                                                                                    break
                                                                                                v8 = (8 if (u(v8) <= u(8)) else v8)
                                                                                                v11 = (v11 | 8)
                                                                                                v5 = 120
                                                                                                break
                                                                                            v9 = v17
                                                                                            v23 = load64(v7 + 64)
                                                                                            if (load64(v7 + 64) != 0):
                                                                                                v12 = (v5 & 32)
                                                                                                while True:  # $label42
                                                                                                    v9 = (v9 - 1)
                                                                                                    store8((v9 - 1), (load8u(((i32(v23) & 15) + 32240)) | v12))
                                                                                                    v6 = (u(v23) > u(15))
                                                                                                    v23 = ((v23 & 0xFFFFFFFFFFFFFFFF) >> 4)
                                                                                                    if v6:
                                                                                                        continue
                                                                                                    break
                                                                                            if (load64(v7 + 64) == 0):
                                                                                                break
                                                                                            if ((v11 & 8) == 0):
                                                                                                break
                                                                                            v20 = (((v5 & 0xFFFFFFFF) >> 4) + 2107)
                                                                                            v15 = 2
                                                                                            break
                                                                                            break
                                                                                        v5 = v17
                                                                                        v23 = load64(v7 + 64)
                                                                                        if (load64(v7 + 64) != 0):
                                                                                            while True:  # $label44
                                                                                                v5 = (v5 - 1)
                                                                                                store8((v5 - 1), ((i32(v23) & 7) | 48))
                                                                                                v9 = (u(v23) > u(7))
                                                                                                v23 = ((v23 & 0xFFFFFFFFFFFFFFFF) >> 3)
                                                                                                if v9:
                                                                                                    continue
                                                                                                break
                                                                                        v9 = v5
                                                                                        if ((v11 & 8) == 0):
                                                                                            break
                                                                                        v5 = (v17 - v9)
                                                                                        v8 = (v8 if (v5 < v8) else ((v17 - v9) + 1))
                                                                                        break
                                                                                        break
                                                                                    v23 = load64(v7 + 64)
                                                                                    if (load64(v7 + 64) < 0):
                                                                                        v23 = (0 - v23)
                                                                                        store64(v7 + 64, (0 - v23))
                                                                                        v15 = 1
                                                                                        break
                                                                                    if (v11 & 2048):
                                                                                        v15 = 1
                                                                                        break
                                                                                    v15 = (v11 & 1)
                                                                                    break
                                                                                v20 = (2109 if (v11 & 1) else 2107)
                                                                                v6 = v17
                                                                                while True:  # block $label45
                                                                                    if (u(v23) < u(4294967296)):
                                                                                        v24 = v23
                                                                                        break
                                                                                    while True:  # $label46
                                                                                        v6 = (v6 - 1)
                                                                                        # TODO: i64.div_u []
                                                                                        v24 = 10
                                                                                        store8(v23, (i32((v23 - (10 * 10))) | 48))
                                                                                        v5 = (u(v23) > u(42949672959))
                                                                                        v23 = v24
                                                                                        if v5:
                                                                                            continue
                                                                                        break
                                                                                    break
                                                                                v9 = i32(v24)
                                                                                if i32(v24):
                                                                                    while True:  # $label47
                                                                                        v6 = (v6 - 1)
                                                                                        # TODO: i32.div_u []
                                                                                        v5 = 10
                                                                                        store8(v9, ((v9 - (10 * 10)) | 48))
                                                                                        v12 = (u(v9) > u(9))
                                                                                        v9 = v5
                                                                                        if v12:
                                                                                            continue
                                                                                        break
                                                                                v9 = v6
                                                                                break
                                                                            if (v19 if (v8 < 0) else 0):
                                                                                break
                                                                            v11 = ((v11 & -65537) if v19 else v11)
                                                                            while True:  # block $label48
                                                                                v24 = load64(v7 + 64)
                                                                                if (load64(v7 + 64) != 0):
                                                                                    break
                                                                                if v8:
                                                                                    break
                                                                                v9 = v17
                                                                                v8 = 0
                                                                                break
                                                                                break
                                                                            v5 = ((v24 == 0) + (v17 - v9))
                                                                            v8 = (v8 if (v5 < v8) else ((v24 == 0) + (v17 - v9)))
                                                                            break
                                                                            break
                                                                        while True:  # block $label55
                                                                            v10 = (2147483647 if (u(v8) >= u(2147483647)) else v8)
                                                                            v12 = (2147483647 if (u(v8) >= u(2147483647)) else v8)
                                                                            v11 = ((2147483647 if (u(v8) >= u(2147483647)) else v8) != 0)
                                                                            while True:  # block $label52
                                                                                while True:  # block $label50
                                                                                    while True:  # block $label49
                                                                                        v5 = load32(v7 + 64)
                                                                                        v9 = (load32(v7 + 64) if v5 else 8568)
                                                                                        v14 = (load32(v7 + 64) if v5 else 8568)
                                                                                        if (((load32(v7 + 64) if v5 else 8568) & 3) == 0):
                                                                                            break
                                                                                        if (v12 == 0):
                                                                                            break
                                                                                        while True:  # $label51
                                                                                            if (load8u(v14) == 0):
                                                                                                break
                                                                                            v12 = (v12 - 1)
                                                                                            v11 = ((v12 - 1) != 0)
                                                                                            v14 = (v14 + 1)
                                                                                            if (((v14 + 1) & 3) == 0):
                                                                                                break
                                                                                            if v12:
                                                                                                continue
                                                                                            break
                                                                                        break
                                                                                    if (v11 == 0):
                                                                                        break
                                                                                    while True:  # block $label53
                                                                                        if (load8u(v14) == 0):
                                                                                            break
                                                                                        if (u(v12) < u(4)):
                                                                                            break
                                                                                        while True:  # $label54
                                                                                            v5 = load32(v14)
                                                                                            if (((load32(v14) ^ -1) & (v5 - 16843009)) & -2139062144):
                                                                                                break
                                                                                            v14 = (v14 + 4)
                                                                                            v12 = (v12 - 4)
                                                                                            if (u((v12 - 4)) > u(3)):
                                                                                                continue
                                                                                            break
                                                                                        break
                                                                                    if (v12 == 0):
                                                                                        break
                                                                                    break
                                                                                while True:  # $label56
                                                                                    if (load8u(v14) == 0):
                                                                                        break
                                                                                    v14 = (v14 + 1)
                                                                                    v12 = (v12 - 1)
                                                                                    if (v12 - 1):
                                                                                        continue
                                                                                    break
                                                                                break
                                                                            break
                                                                        v5 = 0
                                                                        v5 = ((0 - v9) if v5 else v10)
                                                                        v10 = (((0 - v9) if v5 else v10) + v9)
                                                                        if (v8 >= 0):
                                                                            v11 = v6
                                                                            v8 = v5
                                                                            break
                                                                        v11 = v6
                                                                        v8 = v5
                                                                        if load8u(v10):
                                                                            break
                                                                        break
                                                                        break
                                                                    if v8:
                                                                        break
                                                                    v5 = 0
                                                                    func107(arg0, 32, v16, 0, v11)
                                                                    break
                                                                    break
                                                                store32(v7 + 12, 0)
                                                                store32(v7 + 8, load64(v7 + 64))
                                                                v5 = (v7 + 8)
                                                                store32(v7 + 64, (v7 + 8))
                                                                v8 = -1
                                                                break
                                                            v6 = v5
                                                            v5 = 0
                                                            while True:  # block $label59
                                                                while True:  # $label61
                                                                    v9 = load32(v6)
                                                                    if (load32(v6) == 0):
                                                                        break
                                                                    while True:  # block $label60
                                                                        v10 = func278((v7 + 4), v9)
                                                                        v9 = (func278((v7 + 4), v9) < 0)
                                                                        if (func278((v7 + 4), v9) < 0):
                                                                            break
                                                                        if (u(v10) > u((v8 - v5))):
                                                                            break
                                                                        v6 = (v6 + 4)
                                                                        v5 = (v5 + v10)
                                                                        if (u(v8) > u((v5 + v10))):
                                                                            continue
                                                                        break
                                                                        break
                                                                    break
                                                                if v9:
                                                                    break
                                                                break
                                                            v10 = 61
                                                            if (v5 < 0):
                                                                break
                                                            func107(arg0, 32, v16, v5, v11)
                                                            if (v5 == 0):
                                                                v5 = 0
                                                                break
                                                            v10 = 0
                                                            v6 = load32(v7 + 64)
                                                            while True:  # $label63
                                                                v9 = load32(v6)
                                                                if (load32(v6) == 0):
                                                                    break
                                                                v9 = func278((v7 + 4), v9)
                                                                v10 = (func278((v7 + 4), v9) + v10)
                                                                if (u((func278((v7 + 4), v9) + v10)) > u(v5)):
                                                                    break
                                                                v6 = (v6 + 4)
                                                                if (u(v5) > u(v10)):
                                                                    continue
                                                                break
                                                            break
                                                        func107(arg0, 32, v16, v5, (v11 ^ 8192))
                                                        v5 = (v16 if (v5 < v16) else v5)
                                                        continue
                                                        break
                                                    if (v19 if (v8 < 0) else 0):
                                                        break
                                                    v10 = 61
                                                    raise RuntimeError('unreachable')
                                                    break
                                                store8(v7 + 55, load64(v7 + 64))
                                                v8 = 1
                                                v9 = v21
                                                v11 = v6
                                                break
                                                break
                                            v6 = load8u(v5 + 1)
                                            v5 = (v5 + 1)
                                            continue
                                            break
                                        raise RuntimeError('unreachable')
                                    if arg0:
                                        break
                                    if (v18 == 0):
                                        break
                                    v5 = 1
                                    while True:  # $label66
                                        arg0 = load32((arg4 + (v5 << 2)))
                                        if load32((arg4 + (v5 << 2))):
                                            func353((arg3 + (v5 << 3)), arg0, arg2)
                                            v13 = 1
                                            v5 = (v5 + 1)
                                            if ((v5 + 1) != 10):
                                                continue
                                            break
                                        break
                                    v13 = 1
                                    if (u(v5) >= u(10)):
                                        break
                                    while True:  # $label67
                                        if load32((arg4 + (v5 << 2))):
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != 10):
                                            continue
                                        break
                                    break
                                    break
                                v10 = 28
                                break
                                break
                            v12 = (v10 - v9)
                            v6 = (v8 if (v8 > v12) else (v10 - v9))
                            if ((v8 if (v8 > v12) else (v10 - v9)) > (v15 ^ 2147483647)):
                                break
                            v10 = 61
                            v8 = (v6 + v15)
                            v5 = (v16 if (v8 < v16) else (v6 + v15))
                            if ((v16 if (v8 < v16) else (v6 + v15)) > v22):
                                break
                            func107(arg0, 32, v5, v8, v11)
                            func107(arg0, 48, v5, v8, (v11 ^ 65536))
                            func107(arg0, 48, v6, v12, 0)
                            func107(arg0, 32, v5, v8, (v11 ^ 8192))
                            continue
                            break
                        break
                    v13 = 0
                    break
                    break
                v10 = 61
                break
            store32((G.global3 + 28), v10)
            break
        v13 = -1
        break
    G.global0 = (v7 + 80)
    return v13

# ------------------------------------------------------------
# $func353
# ------------------------------------------------------------
def func353(arg0, arg1, arg2):
    while True:  # block $label3
        while True:  # block $label2
            while True:  # block $label1
                while True:  # block $label10
                    while True:  # block $label9
                        while True:  # block $label8
                            while True:  # block $label7
                                while True:  # block $label6
                                    while True:  # block $label5
                                        while True:  # block $label4
                                            while True:  # block $label0
                                                # br_table[(arg1 - 9)]
                                                break
                                                break
                                            arg1 = load32(arg2)
                                            store32(arg2, (load32(arg2) + 4))
                                            store32(arg0, load32(arg1))
                                            return
                                            break
                                        arg1 = load32(arg2)
                                        store32(arg2, (load32(arg2) + 4))
                                        store64(arg0, load64(arg1))
                                        return
                                        break
                                    arg1 = load32(arg2)
                                    store32(arg2, (load32(arg2) + 4))
                                    store64(arg0, load64(arg1))
                                    return
                                    break
                                arg1 = load32(arg2)
                                store32(arg2, (load32(arg2) + 4))
                                store64(arg0, load64(arg1))
                                return
                                break
                            arg1 = load32(arg2)
                            store32(arg2, (load32(arg2) + 4))
                            store64(arg0, load64(arg1))
                            return
                            break
                        arg1 = ((load32(arg2) + 7) & -8)
                        store32(arg2, (((load32(arg2) + 7) & -8) + 8))
                        store32(arg0, load32(arg1))
                        return
                        break
                    raise RuntimeError('unreachable')
                    break
                return
                break
            arg1 = load32(arg2)
            store32(arg2, (load32(arg2) + 4))
            store64(arg0, load32s(arg1))
            return
            break
        arg1 = load32(arg2)
        store32(arg2, (load32(arg2) + 4))
        store64(arg0, load32u(arg1))
        return
        break
    arg1 = ((load32(arg2) + 7) & -8)
    store32(arg2, (((load32(arg2) + 7) & -8) + 8))
    store64(arg0, load64(arg1))

# ------------------------------------------------------------
# $func355
# ------------------------------------------------------------
def func355(arg0, arg1, arg2):
    v9 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    v6 = (arg1 // 32)
    v3 = load32(9681892)
    v4 = load32(9142880)
    while True:  # block $label1
        while True:  # block $label0
            v7 = (arg0 // 32)
            if ((arg0 // 32) != load32(9687260)):
                break
            if (v6 != load32(9687264)):
                break
            if arg2:
                break
            if (v3 >= 0):
                break
            break
        store32(9687264, v6)
        store32(9687260, v7)
        while True:  # block $label2
            if (v3 < 0):
                v3 = (load32(9681888) << 4)
                v5 = (arg1 - (load32(9681888) << 4))
                v3 = (arg0 - v3)
                if (load8u(9142916) == 0):
                    break
                # TODO: f32.convert_i32_u []
                break
            v3 = (load32(9681888) << 4)
            v5 = ((v6 << 5) - (load32(9681888) << 4))
            v3 = ((v7 << 5) - v3)
            if (load8u(9142916) == 0):
                break
            # TODO: f32.convert_i32_u []
            break
        v13 = ((0.0 / (load32(9142440) * 96)) + 0.25)
        store32(v9 + 72, v4)
        # TODO: f64.promote_f32 []
        store32((v9 - -64), v13)
        # TODO: f64.promote_f32 []
        store32(v9 + 56, float(v5))
        # TODO: f64.promote_f32 []
        store32(v9 + 48, float(v3))
        a_b()
        if (load8u(9142916) == 0):
            store64(v9 + 16, 0)
            store64(v9 + 24, 0)
            store32(v9 + 32, v4)
            # TODO: f32.demote_f64 []
            v13 = (float((load32(9681888) << 5)) + 0.5)
            # TODO: f64.promote_f32 []
            store32(v9 + 8, (float((load32(9681888) << 5)) + 0.5))
            # TODO: f64.promote_f32 []
            store32(v9, (-v13))
            a_b()
        if ((((load32(9142900) == 0) & (load8u(9142409) != 0)) | arg2) == 0):
            break
        arg2 = load32(9681892)
        if (load32(9681892) < 0):
            arg0 = load32(9681888)
            arg2 = (load32(9681888) << 4)
            func401((arg0 - (load32(9681888) << 4)), (arg1 - arg2), (arg0 << 5))
            break
        arg0 = load32(9681888)
        arg1 = (load32(9681888) // 2)
        v6 = (v6 - (load32(9681888) // 2))
        v7 = (v7 - arg1)
        while True:  # block $label4
            while True:  # block $label10
                while True:  # block $label3
                    if load8u(9681885):
                        if (load32(load32((load32(9140332) + (arg2 << 2))) + 32) != 23):
                            break
                        func401((v7 << 5), (v6 << 5), (arg0 << 5))
                        arg2 = load32(9681888)
                        if (load32(9681888) <= 0):
                            break
                        v8 = (arg2 + v6)
                        v10 = (arg2 + v7)
                        arg1 = load32(9142440)
                        arg0 = v7
                        while True:  # $label9
                            v3 = (arg0 + 1)
                            arg2 = v6
                            while True:  # $label8
                                while True:  # block $label7
                                    while True:  # block $label6
                                        while True:  # block $label5
                                            if (u(arg1) <= u(arg2)):
                                                break
                                            if ((arg0 | arg2) < 0):
                                                break
                                            if (u(arg0) < u(arg1)):
                                                break
                                            break
                                        break
                                        break
                                    v5 = load32(9142840)
                                    arg1 = (arg1 + 2)
                                    v4 = (arg2 + 1)
                                    v11 = (load32(9142840) + ((((arg1 + 2) * (arg2 + 1)) + v3) << 2))
                                    if (load32((load32(9142840) + ((((arg1 + 2) * (arg2 + 1)) + v3) << 2))) == 0):
                                        store32(v11, 1)
                                        arg1 = (load32(9142440) + 2)
                                    arg1 = (((arg1 + v4) * arg1) + v3)
                                    v11 = load32((v5 + ((((arg1 + v4) * arg1) + v3) << 2)))
                                    if (u(load32((v5 + ((((arg1 + v4) * arg1) + v3) << 2)))) >= u(3)):
                                        v5 = load32(9142840)
                                        arg1 = (load32(9142440) + 2)
                                    else:
                                    store32(((arg1 << 2) + v5), 1)
                                    store8((load32(9147288) + ((load32(9142440) * arg2) + arg0)), load32(9681892))
                                    arg1 = load32(9142440)
                                    break
                                arg2 = v4
                                if (((((load32(9142440) + 2) + v4) * arg1) + v3) > v4):
                                    continue
                                break
                            arg0 = v3
                            if (v3 < v10):
                                continue
                            break
                        break
                    if (arg0 <= 0):
                        break
                    v4 = (arg0 + v6)
                    v5 = (arg0 + v7)
                    arg1 = load32(9142440)
                    arg0 = v7
                    while True:  # $label15
                        v3 = (arg0 + 1)
                        arg2 = v6
                        while True:  # $label14
                            while True:  # block $label13
                                while True:  # block $label12
                                    while True:  # block $label11
                                        if (u(arg1) <= u(arg2)):
                                            break
                                        if ((arg0 | arg2) < 0):
                                            break
                                        if (u(arg0) < u(arg1)):
                                            break
                                        break
                                    arg2 = (arg2 + 1)
                                    break
                                    break
                                arg2 = (arg2 + 1)
                                v8 = (arg1 + 2)
                                v8 = load32((load32(9142840) + ((v3 + (((arg2 + 1) + (arg1 + 2)) * v8)) << 2)))
                                if (u(load32((load32(9142840) + ((v3 + (((arg2 + 1) + (arg1 + 2)) * v8)) << 2)))) < u(3)):
                                    break
                                v10 = load32(38448)
                                v8 = (load32(9671128) + (v8 * 132))
                                if (load32(38448) != load8u((load32(9671128) + (v8 * 132)) + 122)):
                                    break
                                if (load32(9681892) != v10):
                                    break
                                arg1 = load32(9142440)
                                break
                            if (arg2 < v4):
                                continue
                            break
                        arg0 = v3
                        if (v3 < v5):
                            continue
                        break
                    arg0 = load32(9681888)
                    if (load32(9681888) <= 0):
                        break
                    v8 = (arg0 + v6)
                    v10 = (arg0 + v7)
                    arg1 = load32(9142440)
                    arg0 = v7
                    while True:  # $label18
                        v11 = (arg0 - v7)
                        arg2 = v6
                        while True:  # $label17
                            while True:  # block $label16
                                if (u(arg1) <= u(arg2)):
                                    break
                                if ((arg0 | arg2) < 0):
                                    break
                                if (u(arg0) >= u(arg1)):
                                    break
                                v3 = load32(9681892)
                                v12 = (load32(9681892) != load32(38448))
                                if ((load32(9681892) != load32(38448)) == 0):
                                    v14 = load64(9147316)
                                    v4 = load32(9147312)
                                    store32(9147316, load32(9147312))
                                    v5 = load32(9147324)
                                    store64(9147320, v14)
                                    v5 = (v5 ^ (v5 << 11))
                                    v4 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v5 ^ (v5 << 11)) & 0xFFFFFFFF) >> 8))) ^ v5)
                                    store32(9147312, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((v5 ^ (v5 << 11)) & 0xFFFFFFFF) >> 8))) ^ v5))
                                    if (load32(9681896) < (v4 % 100)):
                                        break
                                v4 = load32(9681900)
                                if load32(9681900):
                                    v5 = ((v3 * 404) + 9568096)
                                    if (v11 % (load32(((v3 * 404) + 9568096) + 216) + v4)):
                                        break
                                    if ((arg2 - v6) % (load32(v5 + 220) + v4)):
                                        break
                                arg1 = 0
                                if (v12 == 0):
                                    v5 = load32(load32(((v3 * 72) + 9263856)) + 20)
                                    arg1 = load32(9147324)
                                    store32(9147324, load32(9147320))
                                    v12 = load32(9147316)
                                    v4 = load32(9147312)
                                    store32(9147316, load32(9147312))
                                    store32(9147320, v12)
                                    arg1 = (arg1 ^ (arg1 << 11))
                                    arg1 = ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1)
                                    store32(9147312, ((v4 ^ (((v4 & 0xFFFFFFFF) >> 19) ^ (((arg1 ^ (arg1 << 11)) & 0xFFFFFFFF) >> 8))) ^ arg1))
                                    arg1 = ((arg1 % (v5 - 3)) + 3)
                                arg1 = load32(9142440)
                                break
                            arg2 = (arg2 + 1)
                            if ((arg2 + 1) < v8):
                                continue
                            break
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) < v10):
                            continue
                        break
                    break
                    break
                if (arg0 <= 0):
                    break
                v10 = (arg0 + v6)
                v11 = (arg0 + v7)
                arg1 = load32(9142440)
                arg0 = v7
                while True:  # $label23
                    v3 = (arg0 + 1)
                    arg2 = v6
                    while True:  # $label22
                        while True:  # block $label21
                            while True:  # block $label20
                                while True:  # block $label19
                                    if (u(arg1) <= u(arg2)):
                                        break
                                    if ((arg0 | arg2) < 0):
                                        break
                                    if (u(arg0) < u(arg1)):
                                        break
                                    break
                                break
                                break
                            v5 = load32(9142840)
                            v4 = (arg2 + 1)
                            v8 = (((arg2 + 1) * (arg1 + 2)) + v3)
                            v12 = (load32(9671128) + (load32((load32(9142840) + ((((arg2 + 1) * (arg1 + 2)) + v3) << 2))) * 132))
                            if (load32(((load8u((load32(9671128) + (load32((load32(9142840) + ((((arg2 + 1) * (arg1 + 2)) + v3) << 2))) * 132)) + 122) * 404) + 9568096) + 264) == 4):
                                arg1 = load32(9142440)
                                v8 = (((load32(9142440) + 2) * v4) + v3)
                                v5 = load32(9142840)
                            v8 = (v5 + (v8 << 2))
                            if (load32((v5 + (v8 << 2))) == 1):
                                store32(v8, 0)
                                arg1 = (load32(9142440) + 2)
                                store32((v5 + (((((load32(9142440) + 2) + v4) * arg1) + v3) << 2)), 0)
                                arg1 = load32(9142440)
                            store8((load32(9147288) + ((arg1 * arg2) + arg0)), load32(9681892))
                            arg1 = load32(9142440)
                            break
                        arg2 = v4
                        if (func32((arg2 + 1), v12, 0) > v4):
                            continue
                        break
                    arg0 = v3
                    if (v3 < v11):
                        continue
                    break
                break
            arg2 = load32(9681888)
            break
        v6 = (v6 - 4)
        v3 = (arg2 + 8)
        v7 = (v7 - 4)
        if (arg2 >= -7):
            v4 = (v3 + v6)
            v5 = (v3 + v7)
            arg1 = load32(9142440)
            arg0 = v7
            while True:  # $label26
                arg2 = v6
                while True:  # $label25
                    while True:  # block $label24
                        if (u(arg1) <= u(arg2)):
                            break
                        if ((arg0 | arg2) < 0):
                            break
                        if (u(arg0) >= u(arg1)):
                            break
                        v8 = (load32(9147288) + ((arg1 * arg2) + arg0))
                        v10 = load8s((load32(9147288) + ((arg1 * arg2) + arg0)))
                        if (load8s((load32(9147288) + ((arg1 * arg2) + arg0))) >= 0):
                            break
                        store8(v8, (v10 ^ -1))
                        arg1 = load32(9142440)
                        break
                    arg2 = (arg2 + 1)
                    if ((arg2 + 1) < v4):
                        continue
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) < v5):
                    continue
                break
        break
    G.global0 = (v9 + 80)
    return 0

# ------------------------------------------------------------
# $oc
# Export: oc
# ------------------------------------------------------------
def oc(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, param8):
    """Exported as oc."""
    v8 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    while True:  # block $label0
        if load8u(9684432):
            break
        if (load32(51776) == 0):
            store8(9215872, 1)
            while True:  # block $label1
                v9 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    v10 = load32(9215976)
                    break
                v10 = (load32(9215988) + v9)
                store32(9215980, (load32(9215988) + v9))
                v11 = load32(9215976)
                v10 = func26((-1 if (u(v10) > u(1073741823)) else (v10 << 2)))
                if v9:
                    # TODO: memory.copy []
                if v11:
                    v9 = load32(9215984)
                store32(9215976, v10)
                break
            store32(9215984, (v9 + 1))
            store32((v10 + (v9 << 2)), arg0)
            while True:  # block $label2
                arg0 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    v9 = v10
                    break
                v9 = (load32(9215988) + arg0)
                store32(9215980, (load32(9215988) + arg0))
                v9 = func26((-1 if (u(v9) > u(1073741823)) else (v9 << 2)))
                if arg0:
                    # TODO: memory.copy []
                store32(9215976, v9)
                arg0 = load32(9215984)
                break
            store32(9215984, (arg0 + 1))
            store32((v9 + (arg0 << 2)), arg1)
            while True:  # block $label3
                arg1 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg0 = v9
                    break
                arg0 = (load32(9215988) + arg1)
                store32(9215980, (load32(9215988) + arg1))
                arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                if arg1:
                    # TODO: memory.copy []
                store32(9215976, arg0)
                arg1 = load32(9215984)
                break
            store32(9215984, (arg1 + 1))
            store32((arg0 + (arg1 << 2)), arg2)
            while True:  # block $label4
                arg1 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg2 = arg0
                    break
                arg2 = (load32(9215988) + arg1)
                store32(9215980, (load32(9215988) + arg1))
                arg2 = func26((-1 if (u(arg2) > u(1073741823)) else (arg2 << 2)))
                if arg1:
                    # TODO: memory.copy []
                store32(9215976, arg2)
                arg1 = load32(9215984)
                break
            store32(9215984, (arg1 + 1))
            store32((arg2 + (arg1 << 2)), arg3)
            while True:  # block $label5
                arg1 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg0 = arg2
                    break
                arg0 = (load32(9215988) + arg1)
                store32(9215980, (load32(9215988) + arg1))
                arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                if arg1:
                    # TODO: memory.copy []
                store32(9215976, arg0)
                arg1 = load32(9215984)
                break
            store32(9215984, (arg1 + 1))
            store32((arg0 + (arg1 << 2)), arg4)
            while True:  # block $label6
                arg4 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg1 = arg0
                    break
                arg1 = (load32(9215988) + arg4)
                store32(9215980, (load32(9215988) + arg4))
                arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
                if arg4:
                    # TODO: memory.copy []
                store32(9215976, arg1)
                arg4 = load32(9215984)
                break
            store32(9215984, (arg4 + 1))
            store32((arg1 + (arg4 << 2)), arg5)
            while True:  # block $label7
                arg4 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg0 = arg1
                    break
                arg0 = (load32(9215988) + arg4)
                store32(9215980, (load32(9215988) + arg4))
                arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                if arg4:
                    # TODO: memory.copy []
                store32(9215976, arg0)
                arg4 = load32(9215984)
                break
            store32(9215984, (arg4 + 1))
            store32((arg0 + (arg4 << 2)), arg6)
            while True:  # block $label8
                arg4 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg1 = arg0
                    break
                arg1 = (load32(9215988) + arg4)
                store32(9215980, (load32(9215988) + arg4))
                arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
                if arg4:
                    # TODO: memory.copy []
                store32(9215976, arg1)
                arg4 = load32(9215984)
                break
            store32(9215984, (arg4 + 1))
            store32((arg1 + (arg4 << 2)), arg7)
            break
        store8(9163793, arg6)
        store8(9163792, arg5)
        store8(9163794, arg7)
        while True:  # block $label9
            if arg3:
                break
            if load8u(9142409):
                break
            if (arg4 == 0):
                break
            break
        store8(9142409, 0)
        while True:  # block $label10
            if (load8u(9142410) == 0):
                break
            if load8u(59183):
                break
            if load8u(9142916):
                break
            store64(v8 + 80, -4602115869219225600)
            store32(v8 + 88, load32(9142876))
            store64(v8 + 64, 0)
            store64(v8 + 72, 0)
            a_b()
            break
        while True:  # block $label11
            if arg4:
                break
            while True:  # block $label12
                # TODO: f32.convert_i32_u []
                v19 = load32(9142860)
                v19 = load32(40616)
                v21 = load32(9671164)
                v20 = (((load32(9142860) - ((v19 * load32(40616)) / load32(9671164))) * 0.5) + ((v19 * float(arg1)) + float(load32(9142956))))
                if (abs((((load32(9142860) - ((v19 * load32(40616)) / load32(9671164))) * 0.5) + ((v19 * float(arg1)) + float(load32(9142956))))) < 2147483650.0):
                    break
                break
            arg1 = -2147483648
            # TODO: f32.convert_i32_u []
            v20 = load32(9142856)
            v19 = (((v19 * float(arg0)) + float(load32(9142952))) + ((load32(9142856) - ((v19 * v20) / v21)) * 0.5))
            if (abs((((v19 * float(arg0)) + float(load32(9142952))) + ((load32(9142856) - ((v19 * v20) / v21)) * 0.5))) < 2147483650.0):
                arg0 = int(v19)
                break
            arg0 = -2147483648
            break
        store32(59144, arg1)
        store32(59136, arg0)
        if load32(9684792):
            break
        arg4 = load8u(9681884)
        while True:  # block $label13
            arg7 = load32(9671176)
            if load32(9671176):
                break
            if arg4:
                break
            if arg2:
                break
            if (load8u(59183) == 0):
                break
            arg0 = load32(59132)
            arg1 = load32(59136)
            arg2 = load32(9568088)
            arg3 = load32(59144)
            arg4 = load32(59140)
            arg5 = ((load32(59144) if (arg3 < arg4) else load32(59140)) // 32)
            store32(load32(9568088) + 24, ((load32(59144) if (arg3 < arg4) else load32(59140)) // 32))
            arg6 = ((arg1 if (arg0 > arg1) else arg0) // 32)
            store32(arg2 + 20, ((arg1 if (arg0 > arg1) else arg0) // 32))
            arg3 = ((arg3 if (arg3 > arg4) else arg4) - (arg5 << 5))
            arg3 = (arg3 >> 31)
            arg3 = ((((arg3 if (arg3 > arg4) else arg4) - (arg5 << 5)) ^ (arg3 >> 31)) - arg3)
            store32(arg2 + 40, (((((((arg3 if (arg3 > arg4) else arg4) - (arg5 << 5)) ^ (arg3 >> 31)) - arg3) & 0xFFFFFFFF) >> 5) + ((arg3 & 31) != 0)))
            arg0 = ((arg1 if (arg0 < arg1) else arg0) - (arg6 << 5))
            arg0 = (arg0 >> 31)
            arg0 = ((((arg1 if (arg0 < arg1) else arg0) - (arg6 << 5)) ^ (arg0 >> 31)) - arg0)
            store32(arg2 + 28, (((((((arg1 if (arg0 < arg1) else arg0) - (arg6 << 5)) ^ (arg0 >> 31)) - arg0) & 0xFFFFFFFF) >> 5) + ((arg0 & 31) != 0)))
            break
            break
        if (arg3 == 2):
            store32(59140, arg1)
            store32(59132, arg0)
        while True:  # block $label14
            if (arg2 != 2):
                break
            if (arg4 == 0):
                break
            arg1 = load32(9142880)
            arg0 = (G.global0 - 48)
            G.global0 = (G.global0 - 48)
            while True:  # block $label15
                if load8u(9142916):
                    store32(arg0 + 32, arg1)
                    a_b()
                    break
                store32(arg0 + 24, arg1)
                store64(arg0 + 16, -4602115869219225600)
                store64(arg0 + 8, 0)
                store64(arg0, 0)
                a_b()
                break
            G.global0 = (arg0 + 48)
            store8(9681884, 0)
            break
            break
        if arg4:
            break
        arg3 = load32(9142440)
        arg6 = ((arg1 & 0xFFFFFFFF) >> 5)
        arg5 = ((arg0 & 0xFFFFFFFF) >> 5)
        arg4 = ((u(load32(9142440)) > u(((arg1 & 0xFFFFFFFF) >> 5))) & (u(arg3) > u(((arg0 & 0xFFFFFFFF) >> 5))))
        while True:  # block $label18
            if (arg2 == 2):
                if (arg4 == 0):
                    break
                arg4 = load8u(9147152)
                while True:  # block $label17
                    while True:  # block $label16
                        if (load32(load32(9142424) + 48) == 0):
                            break
                        if arg4:
                            break
                        if (load16u((load32(9147376) + (((arg3 * arg6) + arg5) << 1))) == 0):
                            break
                        break
                    break
                arg2 = func141(arg0, arg1)
                if (load32(40604) != -1):
                    store32(40604, -1)
                    store32(9142896, 0)
                    if load32(9216064):
                        break
                    store32(41088, 2)
                    store64(v8 + 16, 2)
                    break
                if arg7:
                    arg0 = 0
                    while True:  # block $label19
                        if (load32(9142396) == 0):
                            break
                        while True:  # $label20
                            func38(load32((load32(9142392) + (arg0 << 2))))
                            arg0 = (arg0 + 1)
                            if (u((arg0 + 1)) < u(load32(9142396))):
                                continue
                            break
                        store32(9142396, 0)
                        arg0 = load32(9142392)
                        if (load32(9142392) == 0):
                            break
                        break
                    arg0 = 0
                    while True:  # block $label21
                        if (load32(9671176) == 0):
                            break
                        if load32(9671192):
                            while True:  # $label22
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
                    break
                arg7 = load32(9213808)
                if (load32(9213808) == 0):
                    break
                if arg4:
                    break
                arg4 = 0
                arg3 = 0
                v9 = load32(9671128)
                v10 = (arg2 if load32((load32(9671128) + (arg2 * 132)) + 40) else 0)
                if (arg2 if load32((load32(9671128) + (arg2 * 132)) + 40) else 0):
                    while True:  # block $label23
                        arg3 = (v9 + (v10 * 132))
                        arg4 = func161((v9 + (v10 * 132)), 9173808, arg7)
                        if (func161((v9 + (v10 * 132)), 9173808, arg7) == 0):
                            arg7 = 0
                            v11 = load8u(arg3 + 122)
                            if (load8u(arg3 + 122) == load32(38560)):
                                break
                            if (load32(38620) == v11):
                                break
                        if load32(arg3 + 40):
                            arg7 = (v9 + (v10 * 132))
                            func415((func295(arg3, load32(9142872)) | (load16u(arg7 + 110) == 0)), load32(arg3 + 40))
                        arg7 = arg2
                        break
                    arg2 = ((arg4 == 6) & (load8u(9163793) != 0))
                    arg3 = (0 if ((arg4 == 6) & (load8u(9163793) != 0)) else arg4)
                    arg4 = (0 if arg2 else arg7)
                if load8u(9163792):
                    arg0 = func245()
                    func105(9684812, arg5)
                    func105(9684812, arg6)
                    func105(9684812, arg4)
                    func105(9684812, arg3)
                    func105(9684812, load8u(9163793))
                    func105(9684812, arg0)
                    arg1 = load32(9671128)
                    if arg4:
                        arg2 = (arg1 + (arg4 * 132))
                        arg3 = ((load8u((arg1 + (arg4 * 132)) + 122) * 404) + 9568096)
                        arg6 = (((load32(((load8u((arg1 + (arg4 * 132)) + 122) * 404) + 9568096) + 220) & 0xFFFFFFFF) >> 1) + load16u(arg2 + 114))
                    else:
                    # TODO: f32.convert_i32_u []
                    # TODO: f32.convert_i32_u []
                    # TODO: f32.convert_i32_u []
                    break
                store32(v8 + 108, arg3)
                store32(v8 + 104, arg4)
                store32(v8 + 100, arg6)
                store32(v8 + 96, arg5)
                store32(v8 + 112, 0)
                store32(v8 + 116, load8u(9163793))
                store32(v8 + 120, load8u(9163794))
                func360((v8 + 96), load32(9213808))
                arg2 = ((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096)
                arg5 = load32(((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096) + 64)
                if load32(((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096) + 64):
                    store32(v8, load32((load32(arg2 + 52) + ((load32(9142848) % arg5) << 2))))
                    a_b()
                if (arg3 | arg4):
                    break
                arg2 = func245()
                # TODO: f32.convert_i32_u []
                # TODO: f32.convert_i32_u []
                # TODO: f32.convert_i32_u []
                func254(load32(9142576), arg2)
                break
            if (arg4 == 0):
                if (load8u(9142410) == 0):
                    break
                break
            arg2 = load8u(9147152)
            while True:  # block $label25
                while True:  # block $label24
                    if (load32(load32(9142424) + 48) == 0):
                        break
                    if arg2:
                        break
                    if (load16u((load32(9147376) + (((arg3 * arg6) + arg5) << 1))) == 0):
                        break
                    break
                break
            arg3 = func141(arg0, arg1)
            arg0 = load32(9216064)
            if load32(9216064):
                # call_indirect[arg0]
                store32(9216064, 0)
                break
            while True:  # block $label26
                while True:  # block $label27
                    while True:  # block $label28
                        # br_table[arg7]
                        break
                        break
                    if load8u(9142412):
                        break
                    arg0 = load32(load32(9671168))
                    if (load32(load32(9671168)) == load32(38600)):
                        break
                    if (arg0 == load32(38472)):
                        break
                    if (load32(9684800) == 0):
                        break
                    arg2 = (load32(9561692) + (load32((load32(9215960) if load32(9215968) else 9142872)) * 286704))
                    arg1 = load32((((load32(9561692) + (load32((load32(9215960) if load32(9215968) else 9142872)) * 286704)) + (arg0 * 36)) + 269376))
                    arg1 = (load32((((load32(9561692) + (load32((load32(9215960) if load32(9215968) else 9142872)) * 286704)) + (arg0 * 36)) + 269376)) if arg1 else 100)
                    arg0 = ((arg0 * 404) + 9568096)
                    store32(v8 + 96, (((load32((((load32(9561692) + (load32((load32(9215960) if load32(9215968) else 9142872)) * 286704)) + (arg0 * 36)) + 269376)) if arg1 else 100) * load32(((arg0 * 404) + 9568096) + 68)) // 100))
                    store32(v8 + 100, ((load32(arg0 + 72) * arg1) // 100))
                    store32(v8 + 104, ((load32(arg0 + 76) * arg1) // 100))
                    store32(v8 + 108, ((load32(arg0 + 80) * arg1) // 100))
                    if load8u(9163793):
                        break
                    arg0 = (G.global0 - 80)
                    G.global0 = (G.global0 - 80)
                    while True:  # block $label29
                        arg1 = load32(v8 + 96)
                        if (load32(v8 + 96) == 0):
                            break
                        if (load32(arg0 + 64) >= arg1):
                            break
                        store32(arg0 + 48, 0)
                        a_b()
                        break
                    while True:  # block $label30
                        arg1 = load32(v8 + 100)
                        if (load32(v8 + 100) == 0):
                            break
                        if (load32(arg0 + 68) >= arg1):
                            break
                        store32(arg0 + 32, 1)
                        a_b()
                        break
                    while True:  # block $label31
                        arg1 = load32(v8 + 104)
                        if (load32(v8 + 104) == 0):
                            break
                        if (load32(arg0 + 72) >= arg1):
                            break
                        store32(arg0 + 16, 2)
                        a_b()
                        break
                    while True:  # block $label32
                        arg1 = load32(v8 + 108)
                        if (load32(v8 + 108) == 0):
                            break
                        if (load32(arg0 + 76) >= arg1):
                            break
                        store32(arg0, 3)
                        a_b()
                        break
                    while True:  # block $label33
                        arg1 = load32(v8 + 96)
                        if load32(v8 + 96):
                            if (load32(arg0 + 64) < arg1):
                                break
                        arg1 = load32(v8 + 100)
                        if load32(v8 + 100):
                            if (load32(arg0 + 68) < arg1):
                                break
                        arg1 = load32(v8 + 104)
                        if load32(v8 + 104):
                            if (load32(arg0 + 72) < arg1):
                                break
                        arg1 = load32(v8 + 108)
                        if load32(v8 + 108):
                            if (load32(arg0 + 76) < arg1):
                                break
                        break
                    arg1 = 1
                    G.global0 = (arg0 + 80)
                    if (arg1 == 0):
                        break
                    break
                arg6 = 0
                arg4 = (G.global0 - 48)
                G.global0 = (G.global0 - 48)
                arg7 = load32(9671176)
                if (u(load32(9671176)) >= u(3)):
                    while True:  # $label41
                        arg0 = (load32(9671168) + (arg6 * 12))
                        arg2 = (load32(9684776) + load32((load32(9671168) + (arg6 * 12)) + 8))
                        arg3 = (load32(9684772) + load32(arg0 + 4))
                        while True:  # block $label36
                            while True:  # block $label35
                                while True:  # block $label34
                                    v9 = load32(arg0)
                                    if ((load32(arg0) != load32(38472)) & (v9 != load32(38600))):
                                        break
                                    if (load8u(9142410) == 0):
                                        break
                                    arg5 = load8u(9684791)
                                    v10 = load8u(9684790)
                                    v11 = load8u(9684789)
                                    v12 = load8u(9684788)
                                    v13 = load32(9684784)
                                    v15 = load32(9684780)
                                    break
                                    break
                                v15 = 1
                                if (load32(load32(9142424) + 48) == 0):
                                    v13 = 1
                                    v12 = 1
                                    v11 = 1
                                    v10 = 1
                                    arg5 = 1
                                    break
                                v13 = 1
                                v12 = 1
                                v11 = 1
                                v10 = 1
                                arg5 = 1
                                if load8u(9147152):
                                    break
                                arg0 = ((v9 * 404) + 9568096)
                                arg1 = load32(((v9 * 404) + 9568096) + 216)
                                if (load32(((v9 * 404) + 9568096) + 216) <= 0):
                                    break
                                arg0 = load32(arg0 + 220)
                                if (load32(arg0 + 220) <= 0):
                                    break
                                v16 = (arg0 + arg2)
                                v17 = (arg1 + arg3)
                                v18 = load32(9147376)
                                v14 = load32(9142440)
                                arg1 = arg3
                                while True:  # $label39
                                    arg0 = arg2
                                    if (u(arg1) < u(v14)):
                                        while True:  # $label38
                                            while True:  # block $label37
                                                if (u(arg0) >= u(v14)):
                                                    break
                                                if ((arg0 | arg1) < 0):
                                                    break
                                                if load16u((v18 + (((arg0 * v14) + arg1) << 1))):
                                                    break
                                                break
                                            arg0 = (arg0 + 1)
                                            if ((arg0 + 1) < v16):
                                                continue
                                            break
                                    arg1 = (arg1 + 1)
                                    if ((arg1 + 1) < v17):
                                        continue
                                    break
                                break
                                break
                            arg1 = load32(38500)
                            store32(arg4 + 8, arg2)
                            store32(arg4 + 4, arg3)
                            arg2 = load32(9215968)
                            arg3 = load32(9215960)
                            arg0 = load8u(9142412)
                            store32(arg4, v9)
                            arg2 = load32((9142872 if arg0 else (arg3 if arg2 else 9142872)))
                            store32(arg4 + 32, v10)
                            store32(arg4 + 28, v11)
                            store32(arg4 + 24, v12)
                            store32(arg4 + 20, v13)
                            store32(arg4 + 16, v15)
                            store32(arg4 + 12, arg2)
                            store32(arg4 + 40, load8u(9163793))
                            store32(arg4 + 36, (((2 if (arg1 == v9) else arg5) if (u(arg7) > u(3)) else arg5) if arg6 else arg5))
                            while True:  # block $label40
                                if arg0:
                                    if load8u(9147210):
                                        func41(4, 0, 0, arg4, 11)
                                        break
                                    # call_indirect[load32(9213856)]
                                    break
                                arg0 = load32(9213808)
                                if load8u(9147210):
                                    func41(4, 9173808, arg0, arg4, 11)
                                    break
                                arg2 = (arg0 << 2)
                                arg1 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                                if arg0:
                                    # TODO: memory.copy []
                                # call_indirect[load32(9213856)]
                                break
                            arg7 = load32(9671176)
                            break
                        arg6 = (arg6 + 1)
                        # TODO: i32.div_u []
                        if (u(arg7) < u(3)):
                            continue
                        break
                while True:  # block $label42
                    if load8u(9163792):
                        if (load32(load32(9671168)) != load32(38636)):
                            break
                    if (arg7 == 0):
                        break
                    if load32(9671192):
                        arg0 = 0
                        while True:  # $label43
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
                arg0 = 0
                while True:  # block $label44
                    if (load32(9142396) == 0):
                        break
                    while True:  # $label45
                        func38(load32((load32(9142392) + (arg0 << 2))))
                        arg0 = (arg0 + 1)
                        if (u((arg0 + 1)) < u(load32(9142396))):
                            continue
                        break
                    store32(9142396, 0)
                    arg0 = load32(9142392)
                    if (load32(9142392) == 0):
                        break
                    break
                store32(9684784, 1)
                store32(9684780, 1)
                G.global0 = (arg4 + 48)
                break
                break
            while True:  # block $label46
                arg0 = load32(40604)
                if (load32(40604) == -1):
                    break
                if arg2:
                    break
                arg1 = arg0
                if (arg0 == 65):
                    store32(40604, 0)
                    arg3 = 0
                    arg1 = 0
                arg3 = ((arg1 * 40) + 9671200)
                arg1 = (0 if load8u(((arg1 * 40) + 9671200) + 16) else arg3)
                arg4 = load32(9142896)
                if (0 if arg1 else load8u(arg3 + 17)):
                    break
                if (load8u(9163792) == 0):
                    store32(40604, -1)
                    store32(41088, 2)
                    store32(9142896, 0)
                    store64(v8 + 48, 2)
                while True:  # block $label47
                    if (arg1 == 0):
                        break
                    arg2 = (load32(9671128) + (arg1 * 132))
                    if (load32((load32(9671128) + (arg1 * 132)) + 40) == 0):
                        break
                    func415((func295(arg2, load32(9142872)) | (load16u(arg2 + 110) == 0)), load32(arg2 + 40))
                    break
                store32(v8 + 100, arg6)
                store32(v8 + 96, arg5)
                store32(v8 + 104, (-1 if (arg0 == 65) else arg1))
                arg0 = load32(arg3)
                store32(v8 + 112, arg4)
                store32(v8 + 108, arg0)
                store32(v8 + 116, load8u(9163793))
                store32(v8 + 120, load8u(9163794))
                func360((v8 + 96), load32(9213808))
                arg0 = ((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096)
                arg1 = load32(((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096) + 64)
                if (load32(((load8u((load32(9671128) + (load32(9173808) * 132)) + 122) * 404) + 9568096) + 64) == 0):
                    break
                store32(v8 + 32, load32((load32(arg0 + 52) + ((load32(9142848) % arg1) << 2))))
                a_b()
                break
                break
            break
        store8(9142410, 0)
        break
    G.global0 = (v8 + 128)
    return func324()

# ------------------------------------------------------------
# $pc
# Export: pc
# ------------------------------------------------------------
def pc(arg0, arg1, arg2):
    """Exported as pc."""
    v5 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    while True:  # block $label0
        if load8u(9684432):
            break
        if (load32(51776) == 0):
            store8(9215872, 1)
            while True:  # block $label1
                v3 = load32(9216000)
                if (load32(9216000) != load32(9215996)):
                    v4 = load32(9215992)
                    break
                v4 = (load32(9216004) + v3)
                store32(9215996, (load32(9216004) + v3))
                v6 = load32(9215992)
                v4 = func26((-1 if (u(v4) > u(1073741823)) else (v4 << 2)))
                if v3:
                    # TODO: memory.copy []
                if v6:
                    v3 = load32(9216000)
                store32(9215992, v4)
                break
            store32(9216000, (v3 + 1))
            store32((v4 + (v3 << 2)), arg0)
            while True:  # block $label2
                arg0 = load32(9216000)
                if (load32(9216000) != load32(9215996)):
                    v3 = v4
                    break
                v3 = (load32(9216004) + arg0)
                store32(9215996, (load32(9216004) + arg0))
                v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
                if arg0:
                    # TODO: memory.copy []
                store32(9215992, v3)
                arg0 = load32(9216000)
                break
            store32(9216000, (arg0 + 1))
            store32((v3 + (arg0 << 2)), arg1)
            while True:  # block $label3
                arg1 = load32(9216000)
                if (load32(9216000) != load32(9215996)):
                    arg0 = v3
                    break
                arg0 = (load32(9216004) + arg1)
                store32(9215996, (load32(9216004) + arg1))
                arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                if arg1:
                    # TODO: memory.copy []
                store32(9215992, arg0)
                arg1 = load32(9216000)
                break
            store32(9216000, (arg1 + 1))
            store32((arg0 + (arg1 << 2)), arg2)
            break
        while True:  # block $label4
            if arg2:
                store32(9681444, arg1)
                store32(9681440, arg0)
                break
            arg1 = load32(9681444)
            arg0 = load32(9681440)
            break
        while True:  # block $label5
            # TODO: f32.convert_i32_u []
            v15 = load32(9142860)
            v15 = load32(40616)
            v16 = load32(9671164)
            v17 = (((load32(9142860) - ((v15 * load32(40616)) / load32(9671164))) * 0.5) + ((v15 * float(arg1)) + float(load32(9142956))))
            if (abs((((load32(9142860) - ((v15 * load32(40616)) / load32(9671164))) * 0.5) + ((v15 * float(arg1)) + float(load32(9142956))))) < 2147483650.0):
                break
            break
        arg1 = -2147483648
        while True:  # block $label6
            # TODO: f32.convert_i32_u []
            v17 = load32(9142856)
            v15 = (((v15 * float(arg0)) + float(load32(9142952))) + ((load32(9142856) - ((v15 * v17) / v16)) * 0.5))
            if (abs((((v15 * float(arg0)) + float(load32(9142952))) + ((load32(9142856) - ((v15 * v17) / v16)) * 0.5))) < 2147483650.0):
                break
            break
        arg0 = -2147483648
        if load8u(9681884):
            break
        arg2 = load8u(9142409)
        if load8u(9142409):
            if load32(9142900):
                break
        if load32(9684792):
            arg2 = load32(9684792)
            v6 = load32(load32(9684792))
            v7 = (arg0 - load32(load32(9684792)))
            v10 = load32(arg2 + 8)
            arg1 = (load32(arg2 + 20) * load32(arg2 + 16))
            if (load32(arg2 + 20) * load32(arg2 + 16)):
            else:
            v11 = ((load32(arg2 + 4) // arg1) - 0)
            arg0 = (((load32(arg2 + 4) // arg1) - 0) // 32)
            v12 = load32(arg2 + 12)
            while True:  # block $label7
                v3 = (v7 // 32)
                v6 = ((v3 + (v6 // 32)) + ((v6 & 31) != 0))
                if ((v7 // 32) >= ((v3 + (v6 // 32)) + ((v6 & 31) != 0))):
                    v8 = load32(9142440)
                    v4 = 1
                    break
                arg1 = (load32(arg2 + 4) // arg1)
                arg1 = ((((load32(arg2 + 4) // arg1) // 32) + arg0) + ((arg1 & 31) != 0))
                v13 = (arg0 if (arg0 > arg1) else ((((load32(arg2 + 4) // arg1) // 32) + arg0) + ((arg1 & 31) != 0)))
                v8 = load32(9142440)
                v9 = (load32(9142440) + 2)
                v14 = load32(9142840)
                while True:  # $label9
                    v3 = (v3 + 1)
                    arg1 = arg0
                    while True:  # $label8
                        if (arg1 != v13):
                            arg1 = (arg1 + 1)
                            if (load32((v14 + (((((arg1 + 1) + v9) * v9) + v3) << 2))) != 1):
                                continue
                            break
                        break
                    v4 = (v3 >= v6)
                    if (v3 != v6):
                        continue
                    break
                break
            # TODO: f32.convert_i32_u []
            break
        while True:  # block $label10
            if load32(9671176):
                break
            if (arg2 == 0):
                break
            v15 = float(arg1)
            v16 = float(load32(59140))
            arg2 = (v15 < v16)
            v17 = (float(arg1) if (v15 < v16) else float(load32(59140)))
            v18 = float(arg0)
            v19 = float(load32(59132))
            v3 = (v18 < v19)
            v20 = (float(arg0) if (v18 < v19) else float(load32(59132)))
            while True:  # block $label11
                if (load8u(59183) == 0):
                    v15 = abs((v15 - v16))
                    break
                while True:  # block $label12
                    v15 = (v17 * 0.03125)
                    if (abs((v17 * 0.03125)) < 2147483650.0):
                        break
                    break
                v17 = float((-2147483648 << 5))
                v15 = (ceil((abs((int(v15) - float((-2147483648 << 5)))) * 0.03125)) * 32.0)
                while True:  # block $label13
                    v16 = (v20 * 0.03125)
                    if (abs((v20 * 0.03125)) < 2147483650.0):
                        break
                    break
                v20 = float((-2147483648 << 5))
                break
            v18 = (ceil((abs((int(v16) - float((-2147483648 << 5)))) * 0.03125)) * 32.0)
            if (load8u(9142410) == 0):
                store8(9142410, 1)
            if load8u(9142916):
                break
            v3 = load32(9142876)
            v16 = 0.0
            arg2 = (G.global0 - 32)
            G.global0 = (G.global0 - 32)
            if load8u(9142916):
                # TODO: f32.convert_i32_u []
                v16 = ((0.0 / (load32(9142440) * 96)) + 0.25)
            store32(arg2 + 24, v3)
            # TODO: f64.promote_f32 []
            store32(arg2 + 16, v16)
            # TODO: f64.promote_f32 []
            store32(arg2 + 8, (v17 + -0.0))
            # TODO: f64.promote_f32 []
            store32(arg2, (v20 + -0.0))
            a_b()
            G.global0 = (arg2 + 32)
            if load8u(9142916):
                break
            store64((v5 - -64), 0)
            store64(v5 + 72, 0)
            store32(v5 + 80, load32(9142876))
            # TODO: f64.promote_f32 []
            store32(v5 + 56, v15)
            # TODO: f64.promote_f32 []
            store32(v5 + 48, (-v18))
            a_b()
            break
        arg2 = (arg0 // 32)
        while True:  # block $label17
            while True:  # block $label15
                while True:  # block $label16
                    while True:  # block $label14
                        v4 = load32(9142440)
                        v6 = (arg1 // 32)
                        if (u(load32(9142440)) <= u((arg1 // 32))):
                            break
                        if ((arg2 | v6) < 0):
                            break
                        if (u(arg2) >= u(v4)):
                            break
                        v7 = load8u(9147152)
                        if ((0 if load8u(9147152) else load32(load32(9142424) + 48)) == 0):
                            v3 = load32(40604)
                            break
                        v3 = load32(40604)
                        if load16u((load32(9147376) + (((v4 * v6) + arg2) << 1))):
                            break
                        if (v3 != -1):
                            break
                        break
                        break
                    v3 = load32(40604)
                    if (load32(40604) != -1):
                        break
                    break
                if load32(9216064):
                    break
                store32(41088, 2)
                store64(v5 + 32, 2)
                break
                break
            if (v3 != -1):
                break
            if v7:
                break
            if load32(9216064):
                break
            while True:  # block $label18
                arg0 = func141(arg0, arg1)
                if func141(arg0, arg1):
                    arg1 = load32(9213808)
                    if load32(9213808):
                        break
                store32(41088, 2)
                store64(v5 + 16, 2)
                break
                break
            arg0 = func161((load32(9671128) + (arg0 * 132)), 9173808, arg1)
            if func161((load32(9671128) + (arg0 * 132)), 9173808, arg1):
                break
            store32(41088, 2)
            store64(v5, 2)
            break
            break
        if (load8u(((v3 * 40) + 9671200) + 17) == 0):
            break
        break
    G.global0 = (v5 + 96)
    return func145(v3, (func141(arg0, arg1) == 0))

# ------------------------------------------------------------
# $func358
# ------------------------------------------------------------
def func358(arg0, arg1):
    v2 = 4
    while True:  # block $label2
        while True:  # block $label0
            if ((arg0 | arg1) & 3):
                break
            while True:  # $label1
                if (load32(arg0) != load32(arg1)):
                    break
                arg1 = (arg1 + 4)
                arg0 = (arg0 + 4)
                v2 = (v2 - 4)
                if (u((v2 - 4)) > u(3)):
                    continue
                break
            if (v2 == 0):
                break
            break
        while True:  # $label3
            v3 = load8u(arg0)
            v4 = load8u(arg1)
            if (load8u(arg0) == load8u(arg1)):
                arg1 = (arg1 + 1)
                arg0 = (arg0 + 1)
                v2 = (v2 - 1)
                if (v2 - 1):
                    continue
                break
            break
        return (v3 - v4)
        break
    return 0

# ------------------------------------------------------------
# $func359
# ------------------------------------------------------------
def func359(arg0, arg1):
    v5 = load32(arg0 + 124)
    v5 = load32(arg0 + 120)
    v9 = (load32(arg0 + 124) if (u(load32(arg0 + 120)) < u(load32(arg0 + 140))) else ((v5 & 0xFFFFFFFF) >> 2))
    v3 = load32(arg0 + 108)
    v2 = ((load32(arg0 + 108) - load32(arg0 + 44)) + 262)
    v12 = (((load32(arg0 + 108) - load32(arg0 + 44)) + 262) if (u(v2) <= u(v3)) else 0)
    v2 = load32(arg0 + 144)
    v8 = load32(arg0 + 116)
    v13 = (load32(arg0 + 144) if (u(v2) < u(v8)) else load32(arg0 + 116))
    v14 = load32(arg0 + 56)
    v7 = (load32(arg0 + 56) + v3)
    v15 = ((load32(arg0 + 56) + v3) + 258)
    v3 = (v5 + v7)
    v10 = load8u((v5 + v7))
    v11 = load8u((v3 - 1))
    v16 = load32(arg0 + 52)
    v17 = load32(arg0 + 64)
    while True:  # $label10
        while True:  # block $label9
            while True:  # block $label0
                v4 = (arg1 + v14)
                v3 = ((arg1 + v14) + v5)
                if (load8u(((arg1 + v14) + v5)) != v10):
                    break
                if (load8u((v3 - 1)) != v11):
                    break
                if (load8u(v4) != load8u(v7)):
                    break
                v3 = 2
                if (load8u(v4 + 1) != load8u(v7 + 1)):
                    break
                while True:  # block $label7
                    while True:  # block $label6
                        while True:  # block $label5
                            while True:  # block $label4
                                while True:  # block $label3
                                    while True:  # block $label2
                                        while True:  # block $label1
                                            while True:  # $label8
                                                v2 = (v3 + v7)
                                                if (load8u((v3 + v7) + 1) == load8u(v4 + 3)):
                                                    if (load8u(v2 + 2) != load8u(v4 + 4)):
                                                        break
                                                    if (load8u(v2 + 3) != load8u(v4 + 5)):
                                                        break
                                                    if (load8u(v2 + 4) != load8u(v4 + 6)):
                                                        break
                                                    if (load8u(v2 + 5) != load8u(v4 + 7)):
                                                        break
                                                    if (load8u(v2 + 6) != load8u(v4 + 8)):
                                                        break
                                                    if (load8u(v2 + 7) != load8u(v4 + 9)):
                                                        break
                                                    v2 = (v3 + 8)
                                                    v6 = (v7 + (v3 + 8))
                                                    if (load8u((v7 + (v3 + 8))) != load8u(v4 + 10)):
                                                        break
                                                    v4 = (v4 + 8)
                                                    v18 = (u(v3) < u(250))
                                                    v3 = v2
                                                    if v18:
                                                        continue
                                                    break
                                                break
                                            v6 = (v2 + 1)
                                            break
                                            break
                                        v6 = (v2 + 2)
                                        break
                                        break
                                    v6 = (v2 + 3)
                                    break
                                    break
                                v6 = (v2 + 4)
                                break
                                break
                            v6 = (v2 + 5)
                            break
                            break
                        v6 = (v2 + 6)
                        break
                        break
                    v6 = (v2 + 7)
                    break
                v2 = (v6 - v15)
                v3 = ((v6 - v15) + 258)
                if (((v6 - v15) + 258) <= v5):
                    break
                store32(arg0 + 112, arg1)
                if (v3 >= v13):
                    v5 = v3
                    break
                v10 = load8u((v3 + v7))
                v11 = load8u((v2 + v7) + 257)
                v5 = v3
                break
            arg1 = load16u((v17 + ((arg1 & v16) << 1)))
            if (u(v12) >= u(load16u((v17 + ((arg1 & v16) << 1))))):
                break
            v9 = (v9 - 1)
            if (v9 - 1):
                continue
            break
        break
    return (v5 if (u(v5) < u(v8)) else v8)

# ------------------------------------------------------------
# $func360
# ------------------------------------------------------------
def func360(arg0, arg1):
    if load8u(9147210):
        func41(5, 9173808, arg1, arg0, (7 if arg0 else 0))
        return
    v3 = (arg1 << 2)
    v2 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
    if arg1:
        # TODO: memory.copy []
    # call_indirect[load32(9213864)]

# ------------------------------------------------------------
# $func361
# ------------------------------------------------------------
def func361():
    while True:  # block $label0
        if (u(load32(9142892)) < u(2)):
            break
        v5 = load32(9561692)
        v3 = 1
        v1 = 1
        while True:  # block $label5
            if load8u(9147127):
                while True:  # $label4
                    v2 = (v5 + (v3 * 286704))
                    store32((v5 + (v3 * 286704)) + 283892, func88(v2))
                    v0 = 0
                    v1 = load32((v2 + 278572))
                    v4 = load32(load32((v2 + 278572)) + 8)
                    if load32(load32((v2 + 278572)) + 8):
                        v6 = load32(v1)
                        v1 = 0
                        while True:  # $label1
                            v1 = (load32((v6 + (v0 << 2))) + v1)
                            v0 = (v0 + 15)
                            if (u((v0 + 15)) < u(v4)):
                                continue
                            break
                        # TODO: i32.div_u []
                        v0 = 6
                    store32(v2 + 283888, v0)
                    if (load32(9147128) == 9):
                        # TODO: i32.div_u []
                        v0 = load32(9561724)
                    store32(v2 + 283884, v0)
                    v4 = (v2 + 283884)
                    while True:  # block $label2
                        v2 = load32(v2 + 284608)
                        v1 = load32(9561720)
                        if (load32(v2 + 284608) != load32(9561720)):
                            break
                        if (v1 == 0):
                            break
                        # TODO: i32.div_u []
                        store32((v0 * 155), 100)
                        v1 = load32(9561720)
                        break
                    v0 = load32(9142892)
                    while True:  # block $label3
                        if (v1 == v2):
                            break
                        if (v1 == 0):
                            break
                        if (v0 != 3):
                            break
                        if (load32(9147128) != 1):
                            break
                        store32(v4, 0)
                        v0 = load32(9142892)
                        break
                    v3 = (v3 + 1)
                    if (u((v3 + 1)) < u(v0)):
                        continue
                    break
                break
            while True:  # $label6
                v0 = (v5 + (v1 * 286704))
                v2 = func88(v0)
                store32((v5 + (v1 * 286704)) + 283884, func88(v0))
                store32(v0 + 283892, v2)
                v1 = (v1 + 1)
                v0 = load32(9142892)
                if (u((v1 + 1)) < u(load32(9142892))):
                    continue
                break
            break
        if (u(v0) < u(2)):
            break
        v3 = load32(9561692)
        v2 = 1
        while True:  # $label9
            v0 = (v3 + (v2 * 286704))
            store32((v3 + (v2 * 286704)) + 283944, 1)
            v1 = load32(9142892)
            if (u(load32(9142892)) >= u(2)):
                v4 = (v0 + 283944)
                v6 = (v0 + 283884)
                v5 = 1
                v0 = 1
                while True:  # $label8
                    while True:  # block $label7
                        if (v0 == v2):
                            break
                        v7 = load32((v3 + (v0 * 286704)) + 283884)
                        v8 = load32(v6)
                        if (u(load32((v3 + (v0 * 286704)) + 283884)) <= u(load32(v6))):
                            if (v7 != v8):
                                break
                            if (u(v0) <= u(v2)):
                                break
                        v5 = (v5 + 1)
                        store32(v4, (v5 + 1))
                        v1 = load32(9142892)
                        break
                    v0 = (v0 + 1)
                    if (u((v0 + 1)) < u(v1)):
                        continue
                    break
            v2 = (v2 + 1)
            if (u((v2 + 1)) < u(v1)):
                continue
            break
        break

# ------------------------------------------------------------
# $func362
# ------------------------------------------------------------
def func362(arg0, arg1):
    v2 = 2
    while True:  # block $label3
        while True:  # block $label0
            if (u(arg1) <= u(2)):
                v3 = load32(arg0 + 283960)
                break
            v5 = (arg1 - 2)
            v7 = ((arg1 - 2) & 3)
            v3 = load32(arg0 + 283960)
            v6 = load32(9561692)
            if (u((arg1 - 3)) >= u(3)):
                v9 = (v5 & -4)
                arg1 = 0
                while True:  # $label1
                    v5 = (v6 + (v2 * 286704))
                    v4 = ((((v4 + (load32((v6 + (v2 * 286704)) + 283960) == v3)) + (load32((v6 + ((v2 | 1) * 286704)) + 283960) == v3)) + (load32((v5 + 857368)) == v3)) + (load32((v5 + 1144072)) == v3))
                    v2 = (v2 + 4)
                    arg1 = (arg1 + 4)
                    if ((arg1 + 4) != v9):
                        continue
                    break
            if v7:
                while True:  # $label2
                    v4 = (v4 + (load32((v6 + (v2 * 286704)) + 283960) == v3))
                    v2 = (v2 + 1)
                    v8 = (v8 + 1)
                    if ((v8 + 1) != v7):
                        continue
                    break
            break
        v2 = (v4 * 20)
        if (u((v4 * 20)) < u(load16u(((v3 << 1) + 9142944)))):
            v3 = load32(((v3 << 2) + 9142928))
            v2 = (v2 << 1)
            arg1 = (load32(((v3 << 2) + 9142928)) + (v2 << 1))
            store16(arg0, load16u((load32(((v3 << 2) + 9142928)) + (v2 << 1))))
            store16(arg0 + 2, load16u((v3 + (v2 | 2))))
            store16(arg0 + 4, load16u((v3 + (v2 | 4))))
            store16(arg0 + 6, load16u((v3 + (v2 | 6))))
            store16(arg0 + 8, load16u(arg1 + 8))
            store16(arg0 + 10, load16u(arg1 + 10))
            store16(arg0 + 12, load16u(arg1 + 12))
            store16(arg0 + 14, load16u(arg1 + 14))
            store16(arg0 + 16, load16u(arg1 + 16))
            store16(arg0 + 18, load16u(arg1 + 18))
            store16(arg0 + 20, load16u(arg1 + 20))
            store16(arg0 + 22, load16u(arg1 + 22))
            store16(arg0 + 24, load16u(arg1 + 24))
            store16(arg0 + 26, load16u(arg1 + 26))
            store16(arg0 + 28, load16u(arg1 + 28))
            store16(arg0 + 30, load16u(arg1 + 30))
            store16(arg0 + 32, load16u(arg1 + 32))
            store16(arg0 + 34, load16u(arg1 + 34))
            store16(arg0 + 36, load16u(arg1 + 36))
            v3 = 19
            break
        store16(arg0 + 8, 101)
        store64(arg0, 32088563964837972)
        v3 = 5
        break
    v2 = 100
    store16((arg0 + (v3 << 1)), v2)
    return load16u(arg1 + 38)

# ------------------------------------------------------------
# $func363
# ------------------------------------------------------------
def func363(arg0, arg1):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v4 + 12, arg1)
    v2 = (G.global0 - 208)
    G.global0 = (G.global0 - 208)
    store32(v2 + 204, arg1)
    arg1 = (v2 + 160)
    # TODO: memory.fill []
    store32(v2 + 200, load32(v2 + 204))
    while True:  # block $label0
        if (func352(0, arg0, (v2 + 200), (v2 + 80), arg1) < 0):
            break
        if (load32(52668) >= 0):
            while True:  # block $label1
                arg1 = load32(G.global3 + 24)
                if (load32(G.global3 + 24) == (load32(52668) & -1073741825)):
                    break
                v3 = 1
                # TODO: i32.atomic.rmw.cmpxchg []
                if (arg1 == 0):
                    break
                v7 = (arg1 | 1073741824)
                # TODO: i32.atomic.rmw.cmpxchg []
                arg1 = (arg1 | 1073741824)
                if ((arg1 | 1073741824) == 0):
                    break
                while True:  # $label3
                    v5 = (arg1 | 1073741824)
                    while True:  # block $label2
                        if ((arg1 & 1073741824) == 0):
                            # TODO: i32.atomic.rmw.cmpxchg []
                            if (arg1 != v5):
                                break
                        func439(52668, v5)
                        break
                    # TODO: i32.atomic.rmw.cmpxchg []
                    arg1 = v7
                    if v7:
                        continue
                    break
                break
        arg1 = load32(52592)
        if (load32(52664) <= 0):
            store32(52592, (arg1 & -33))
        while True:  # block $label6
            while True:  # block $label5
                while True:  # block $label4
                    if (load32(52640) == 0):
                        store32(52640, 80)
                        store32(52620, 0)
                        store64(52608, 0)
                        v6 = load32(52636)
                        store32(52636, v2)
                        break
                    if load32(52608):
                        break
                    break
                if func433(52592):
                    break
                break
            break
        arg0 = func352(52592, arg0, (v2 + 200), (v2 + 80), (v2 + 160))
        if v6:
            # call_indirect[load32(52628)]
            store32(52640, 0)
            store32(52636, v6)
            store32(52620, 0)
            store64(52608, 0)
        else:
        store32(52592, (load32(52592) | (arg1 & 32)))
        if (v3 == 0):
            break
        # TODO: i32.atomic.rmw.xchg []
        if (0 & 1073741824):
            func97(52668)
        break
    G.global0 = (v2 + 208)
    G.global0 = (v4 + 16)
    return 52668

# ------------------------------------------------------------
# $func364
# ------------------------------------------------------------
def func364(arg0, arg1, arg2):
    while True:  # block $label0
        v5 = load32(arg0)
        v3 = ((load32(arg0) * 404) + 9568096)
        v6 = (1 if (load32(((load32(arg0) * 404) + 9568096) + 368) != 55) else arg2)
        if ((1 if (load32(((load32(arg0) * 404) + 9568096) + 368) != 55) else arg2) == 0):
            break
        v7 = (v3 + 68)
        arg2 = 0
        while True:  # $label2
            arg0 = (load32(9671128) + (load32((arg1 + (arg2 << 2))) * 132))
            v4 = (load32(9561692) + (load16u((load32(9671128) + (load32((arg1 + (arg2 << 2))) * 132)) + 110) * 286704))
            v8 = ((load32(9561692) + (load16u((load32(9671128) + (load32((arg1 + (arg2 << 2))) * 132)) + 110) * 286704)) + (v5 << 2))
            if load32((((load32(9561692) + (load16u((load32(9671128) + (load32((arg1 + (arg2 << 2))) * 132)) + 110) * 286704)) + (v5 << 2)) + 281808)):
                break
            if load8u(arg0 + 125):
                break
            if func66(v4, v7, 1, 1):
                break
            if (load32(v3 + 368) != 55):
                store32((v8 + 282828), 1)
            store8(arg0 + 125, 5)
            # TODO: i32.div_u []
            func63(arg0, 5, v5, ((load32(v3 + 116) * load32(load32(9142424) + 132)) * 1000), 100)
            while True:  # block $label1
                if (load32(arg0 + 92) == 0):
                    break
                v4 = load8u(9147141)
                if load32(9140316):
                    if (load32(9140320) != load32(arg0 + 28)):
                        break
                break
            arg2 = (arg2 + 1)
            if ((arg2 + 1) != v6):
                continue
            break
        break

# ------------------------------------------------------------
# $func365
# ------------------------------------------------------------
def func365(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    v9 = (arg8 << 2)
    v10 = load32(((arg8 << 2) + 9344))
    v14 = load32((v9 + 9264))
    v11 = load32(9142440)
    while True:  # block $label3
        while True:  # block $label2
            while True:  # block $label1
                if (((28728 & 0xFFFFFFFF) >> arg8) & 1):
                    while True:  # block $label0
                        arg8 = ((v14 * 5) + arg2)
                        if ((((v14 * 5) + arg2) if (arg2 > arg8) else arg2) > arg0):
                            break
                        if ((arg2 if (arg2 > arg8) else arg8) < arg0):
                            break
                        arg8 = (arg1 - arg3)
                        break
                        break
                    v9 = (arg1 - arg3)
                    v9 = ((arg1 - arg3) * v9)
                    arg8 = (arg0 - arg8)
                    arg8 = (((arg1 - arg3) * v9) + ((arg0 - arg8) * arg8))
                    v12 = (arg0 - arg2)
                    v9 = (v9 + ((arg0 - arg2) * v12))
                    break
                if ((((74898 & 0xFFFFFFFF) >> arg8) & 1) == 0):
                    break
                arg8 = (arg0 - arg2)
                arg8 = ((arg0 - arg2) * arg8)
                v9 = ((v10 * 5) + arg3)
                v12 = (arg3 > v9)
                if ((arg1 >= (((v10 * 5) + arg3) if (arg3 > v9) else arg3)) & ((arg3 if v12 else v9) >= arg1)):
                    break
                v9 = (arg1 - v9)
                v9 = (((arg1 - v9) * v9) + arg8)
                arg8 = (arg1 - arg3)
                arg8 = (arg8 + ((arg1 - arg3) * arg8))
                break
            if (((((arg1 - v9) * v9) + arg8) if (u(arg8) > u(v9)) else (arg8 + ((arg1 - arg3) * arg8))) == 0):
                break
            v12 = (v11 + 2)
            v15 = (((v11 + 2) * arg5) + 1)
            v13 = load32(9142840)
            while True:  # block $label5
                while True:  # block $label4
                    if (u(arg3) >= u(v11)):
                        break
                    if (u(arg2) >= u(v11)):
                        break
                    if ((arg2 | arg3) < 0):
                        break
                    arg8 = arg2
                    v9 = arg3
                    if (load32((((arg2 + ((v15 + arg3) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                arg8 = (arg2 + v14)
                while True:  # block $label6
                    v9 = (arg3 + v10)
                    if (u(v11) <= u((arg3 + v10))):
                        break
                    if (u(arg8) >= u(v11)):
                        break
                    if ((arg8 | v9) < 0):
                        break
                    if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                arg8 = (arg8 + v14)
                while True:  # block $label7
                    v9 = (v9 + v10)
                    if (u(v11) <= u((v9 + v10))):
                        break
                    if (u(arg8) >= u(v11)):
                        break
                    if ((arg8 | v9) < 0):
                        break
                    if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                arg8 = (arg8 + v14)
                while True:  # block $label8
                    v9 = (v9 + v10)
                    if (u(v11) <= u((v9 + v10))):
                        break
                    if (u(arg8) >= u(v11)):
                        break
                    if ((arg8 | v9) < 0):
                        break
                    if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                arg8 = (arg8 + v14)
                while True:  # block $label9
                    v9 = (v9 + v10)
                    if (u(v11) <= u((v9 + v10))):
                        break
                    if (u(arg8) >= u(v11)):
                        break
                    if ((arg8 | v9) < 0):
                        break
                    if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) == arg4):
                        break
                    break
                v9 = (v9 + v10)
                if (u(v11) <= u((v9 + v10))):
                    break
                arg8 = (arg8 + v14)
                if (u(v11) <= u((arg8 + v14))):
                    break
                if ((arg8 | v9) < 0):
                    break
                if (load32((((arg8 + ((v9 + v15) * v12)) << 2) + v13) + 4) != arg4):
                    break
                break
            arg2 = (arg2 - arg0)
            arg2 = (arg2 >> 31)
            arg2 = (((arg2 - arg0) ^ (arg2 >> 31)) - arg2)
            arg3 = (arg3 - arg1)
            arg3 = (arg3 >> 31)
            arg3 = (((arg3 - arg1) ^ (arg3 >> 31)) - arg3)
            v15 = (((((arg2 - arg0) ^ (arg2 >> 31)) - arg2) if (u(arg2) > u(arg3)) else (((arg3 - arg1) ^ (arg3 >> 31)) - arg3)) << 5)
            store32(59200, (arg8 + (v9 << 16)))
            v24 = load32(9142436)
            v13 = 1
            v10 = 1
            while True:  # $label23
                arg2 = load32(((v25 << 2) + 59200))
                arg8 = ((load32(((v25 << 2) + 59200)) & 0xFFFFFFFF) >> 16)
                v9 = (arg2 & 65535)
                arg2 = ((((load32(((v25 << 2) + 59200)) & 0xFFFFFFFF) >> 16) * v11) + (arg2 & 65535))
                while True:  # block $label10
                    if (v13 == 0):
                        if (load16u((v24 + (arg2 << 1))) == (v14 & 65535)):
                            break
                    v20 = load32(9142436)
                    v21 = (load32(9142436) + (arg2 << 1))
                    v17 = load32(9142440)
                    v19 = (load32(9142440) + 2)
                    v22 = ((load32(9142440) + 2) * arg5)
                    v18 = (((load32(9142440) + 2) * arg5) + 1)
                    v23 = load32(9671128)
                    v12 = load32(9142840)
                    while True:  # $label22
                        arg2 = (arg1 - arg8)
                        while True:  # block $label11
                            arg3 = (arg0 - v9)
                            if ((arg0 - v9) == 0):
                                break
                            if (arg1 == arg8):
                                break
                            arg3 = (arg2 // arg3)
                            arg3 = (arg3 >> 31)
                            arg3 = (arg3 if (u((((arg2 // arg3) ^ (arg3 >> 31)) - arg3)) <= u(1)) else 0)
                            arg2 = ((arg3 if (u((((arg2 // arg3) ^ (arg3 >> 31)) - arg3)) <= u(1)) else 0) // arg2)
                            arg2 = (arg2 >> 31)
                            arg2 = (arg2 if (u(((((arg3 if (u((((arg2 // arg3) ^ (arg3 >> 31)) - arg3)) <= u(1)) else 0) // arg2) ^ (arg2 >> 31)) - arg2)) <= u(1)) else 0)
                            break
                        v16 = (-1 if (arg2 < 0) else (arg2 != 0))
                        arg2 = ((-1 if (arg2 < 0) else (arg2 != 0)) + arg8)
                        while True:  # block $label12
                            v26 = (-1 if (arg3 < 0) else (arg3 != 0))
                            arg3 = ((-1 if (arg3 < 0) else (arg3 != 0)) + v9)
                            if (((-1 if (arg3 < 0) else (arg3 != 0)) + v9) != arg0):
                                break
                            if (arg1 != arg2):
                                break
                            store32(arg6, (0 - v26))
                            store32(arg7, (0 - v16))
                            return 1
                            break
                        if (v13 == 0):
                            store16((v20 + (((arg2 * v11) + arg3) << 1)), v14)
                        while True:  # block $label13
                            v16 = load32((((arg3 + (v19 * (arg2 + v18))) << 2) + v12) + 4)
                            if (load32((((arg3 + (v19 * (arg2 + v18))) << 2) + v12) + 4) == arg4):
                                break
                            if (v16 != -1):
                                if (load8u((v23 + (v16 * 132)) + 125) == 1):
                                    break
                            while True:  # block $label14
                                if (v13 == 0):
                                    arg2 = (v9 + 1)
                                    arg3 = load32(9142436)
                                    v13 = load32(9671128)
                                    v20 = (v9 + 2)
                                    v23 = ((arg8 + v18) * v19)
                                    v17 = load32((v12 + (((v9 + 2) + ((arg8 + v18) * v19)) << 2)))
                                    if (arg4 != load32((v12 + (((v9 + 2) + ((arg8 + v18) * v19)) << 2)))):
                                        if (v17 == -1):
                                            break
                                        if (load8u((v13 + (v17 * 132)) + 125) != 1):
                                            break
                                    if (load16u((arg3 + (((arg8 * v11) + arg2) << 1))) == (v14 & 65535)):
                                        break
                                    store32(((v10 << 2) + 59200), ((arg8 << 16) + arg2))
                                    v10 = (v10 + 1)
                                    if (u((v10 + 1)) <= u(v15)):
                                        break
                                    break
                                arg2 = load16u(40596)
                                arg3 = (load16u(40596) + 2)
                                store16(40596, (load16u(40596) + 2))
                                while True:  # block $label15
                                    if (u((arg3 & 65535)) < u(65534)):
                                        break
                                    store16(40596, 1)
                                    arg3 = (v17 * v17)
                                    if ((v17 * v17) == 0):
                                        break
                                    # TODO: memory.fill []
                                    break
                                v14 = (arg2 + 1)
                                store32(((v10 << 2) + 59200), ((arg8 << 16) + v9))
                                v10 = (v10 + 1)
                                break
                                break
                            v17 = (arg8 - 1)
                            while True:  # block $label16
                                v21 = ((arg8 + v22) * v19)
                                v16 = load32((v12 + ((arg2 + ((arg8 + v22) * v19)) << 2)))
                                if (arg4 != load32((v12 + ((arg2 + ((arg8 + v22) * v19)) << 2)))):
                                    if (v16 == -1):
                                        break
                                    if (load8u((v13 + (v16 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((v11 * v17) + v9) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((v17 << 16) + v9))
                                v10 = (v10 + 1)
                                if (u((v10 + 1)) <= u(v15)):
                                    break
                                break
                                break
                            v16 = (v9 - 1)
                            while True:  # block $label17
                                v22 = load32((v12 + ((v9 + v23) << 2)))
                                if (arg4 != load32((v12 + ((v9 + v23) << 2)))):
                                    if (v22 == -1):
                                        break
                                    if (load8u((v13 + (v22 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((arg8 * v11) + v16) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((arg8 << 16) + v16))
                                v10 = (v10 + 1)
                                if (u((v10 + 1)) <= u(v15)):
                                    break
                                break
                                break
                            while True:  # block $label18
                                arg8 = (arg8 + 1)
                                v19 = ((v18 + (arg8 + 1)) * v19)
                                v18 = load32((v12 + ((arg2 + ((v18 + (arg8 + 1)) * v19)) << 2)))
                                if (arg4 != load32((v12 + ((arg2 + ((v18 + (arg8 + 1)) * v19)) << 2)))):
                                    if (v18 == -1):
                                        break
                                    if (load8u((v13 + (v18 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((arg8 * v11) + v9) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((arg8 << 16) + v9))
                                v10 = (v10 + 1)
                                if (u((v10 + 1)) <= u(v15)):
                                    break
                                break
                                break
                            while True:  # block $label19
                                v18 = load32((v12 + ((v20 + v21) << 2)))
                                if (arg4 != load32((v12 + ((v20 + v21) << 2)))):
                                    if (v18 == -1):
                                        break
                                    if (load8u((v13 + (v18 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((v11 * v17) + arg2) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((v17 << 16) + arg2))
                                v10 = (v10 + 1)
                                if (u((v10 + 1)) <= u(v15)):
                                    break
                                break
                                break
                            while True:  # block $label20
                                v18 = load32((v12 + ((v9 + v21) << 2)))
                                if (arg4 != load32((v12 + ((v9 + v21) << 2)))):
                                    if (v18 == -1):
                                        break
                                    if (load8u((v13 + (v18 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((v11 * v17) + v16) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((v17 << 16) + v16))
                                v10 = (v10 + 1)
                                if (u((v10 + 1)) <= u(v15)):
                                    break
                                break
                                break
                            while True:  # block $label21
                                v9 = load32((v12 + ((v9 + v19) << 2)))
                                if (arg4 != load32((v12 + ((v9 + v19) << 2)))):
                                    if (v9 == -1):
                                        break
                                    if (load8u((v13 + (v9 * 132)) + 125) != 1):
                                        break
                                if (load16u((arg3 + (((arg8 * v11) + v16) << 1))) == (v14 & 65535)):
                                    break
                                store32(((v10 << 2) + 59200), ((arg8 << 16) + v16))
                                v10 = (v10 + 1)
                                if (u((v10 + 1)) <= u(v15)):
                                    break
                                break
                                break
                            v9 = load32((v12 + ((v19 + v20) << 2)))
                            if (arg4 != load32((v12 + ((v19 + v20) << 2)))):
                                if (v9 == -1):
                                    break
                                if (load8u((v13 + (v9 * 132)) + 125) != 1):
                                    break
                            if (load16u((arg3 + (((arg8 * v11) + arg2) << 1))) == (v14 & 65535)):
                                break
                            store32(((v10 << 2) + 59200), ((arg8 << 16) + arg2))
                            v10 = (v10 + 1)
                            if (u((v10 + 1)) <= u(v15)):
                                break
                            break
                            break
                        store16(v21, v14)
                        v9 = arg3
                        arg8 = arg2
                        continue
                        break
                    raise RuntimeError('unreachable')
                    break
                v13 = 0
                v25 = (v25 + 1)
                if (u((v25 + 1)) < u(v10)):
                    continue
                break
            break
        return 0
        break
    return 0

# ------------------------------------------------------------
# $func366
# ------------------------------------------------------------
def func366():
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if (load32(9690440) == 0):
        store32(9690460, 2)
        store64(9690452, -1)
        store64(9690444, 17592186048512)
        store32(9690908, 2)
        store32(v1 + 12, 0)
        # $block0
        v0 = (G.global0 - 32)
        store64((G.global0 - 32) + 24, 0)
        store64(v0 + 16, 0)
        store64(v0 + 8, 0)
        store64(9690912, load64(v0 + 8))
        store64(9690928, load64(v0 + 24))
        store64(9690920, load64(v0 + 16))
        v0 = (v1 + 12)
        if (v1 + 12):
            store32(9690912, load32(v0))
        store32(9690440, (((v1 + 8) & -16) ^ 1431655768))
    func54(9690960)
    G.global0 = (v1 + 16)

# ------------------------------------------------------------
# $func367
# ------------------------------------------------------------
def func367(arg0):
    v2 = (arg0 + 148)
    while True:  # $label0
        v3 = (v1 << 2)
        store16((v2 + (v1 << 2)), 0)
        store16((v2 + (v3 | 4)), 0)
        v1 = (v1 + 2)
        if ((v1 + 2) != 286):
            continue
        break
    store16(arg0 + 2684, 0)
    store16(arg0 + 2440, 0)
    store16((arg0 + 2756), 0)
    store16((arg0 + 2752), 0)
    store16((arg0 + 2748), 0)
    store16((arg0 + 2744), 0)
    store16((arg0 + 2740), 0)
    store16((arg0 + 2736), 0)
    store16((arg0 + 2732), 0)
    store16((arg0 + 2728), 0)
    store16((arg0 + 2724), 0)
    store16((arg0 + 2720), 0)
    store16((arg0 + 2716), 0)
    store16((arg0 + 2712), 0)
    store16((arg0 + 2708), 0)
    store16((arg0 + 2704), 0)
    store16((arg0 + 2700), 0)
    store16((arg0 + 2696), 0)
    store16((arg0 + 2692), 0)
    store16((arg0 + 2688), 0)
    store16((arg0 + 2556), 0)
    store16((arg0 + 2552), 0)
    store16((arg0 + 2548), 0)
    store16((arg0 + 2544), 0)
    store16((arg0 + 2540), 0)
    store16((arg0 + 2536), 0)
    store16((arg0 + 2532), 0)
    store16((arg0 + 2528), 0)
    store16((arg0 + 2524), 0)
    store16((arg0 + 2520), 0)
    store16((arg0 + 2516), 0)
    store16((arg0 + 2512), 0)
    store16((arg0 + 2508), 0)
    store16((arg0 + 2504), 0)
    store16((arg0 + 2500), 0)
    store16((arg0 + 2496), 0)
    store16((arg0 + 2492), 0)
    store16((arg0 + 2488), 0)
    store16((arg0 + 2484), 0)
    store16((arg0 + 2480), 0)
    store16((arg0 + 2476), 0)
    store16((arg0 + 2472), 0)
    store16((arg0 + 2468), 0)
    store16((arg0 + 2464), 0)
    store16((arg0 + 2460), 0)
    store16((arg0 + 2456), 0)
    store16((arg0 + 2452), 0)
    store16((arg0 + 2448), 0)
    store16((arg0 + 2444), 0)
    store64(arg0 + 5804, 0)
    store16((arg0 + 1172), 1)
    store32(arg0 + 5800, 0)
    store32(arg0 + 5792, 0)

# ------------------------------------------------------------
# $func368
# ------------------------------------------------------------
def func368(arg0):
    v1 = load32(9671128)
    func148(arg0, 9147392, 0)
    v3 = (v1 + (arg0 * 132))
    while True:  # block $label0
        while True:  # block $label3
            while True:  # block $label2
                while True:  # block $label1
                    v5 = load32(9147420)
                    # br_table[(load32(9147420) - 2147483646)]
                    break
                    break
                v2 = 2
                store8(v3 + 126, 2)
                v5 = 0
                break
                break
            v2 = load8u(v3 + 126)
            if (load8u(v3 + 126) != 2):
                break
            v2 = 0
            store8(v3 + 126, 0)
            v6 = load32(9215884)
            v7 = (v1 + (arg0 * 132))
            v4 = load32((v1 + (arg0 * 132)) + 44)
            if (load32((load32(9215884) + (load32((v1 + (arg0 * 132)) + 44) << 4)) + 4) != 51):
                break
            if v4:
                store32((v6 + (v4 << 4)), 0)
            store32(v7 + 44, 0)
            break
        while True:  # block $label4
            v4 = (v1 + (arg0 * 132))
            if (v5 == load16u((v1 + (arg0 * 132)) + 110)):
                break
            if (load32(((load8u(v4 + 122) * 404) + 9568096) + 188) != 55):
                break
            func78(v3, v5, 1, 1)
            v2 = load8u((v1 + (arg0 * 132)) + 126)
            break
        if (v2 != 2):
            break
        arg0 = (v1 + (arg0 * 132))
        if (load32(((load8u((v1 + (arg0 * 132)) + 122) * 404) + 9568096) + 264) == 2):
            break
        break

# ------------------------------------------------------------
# $func369
# ------------------------------------------------------------
def func369(arg0):
    while True:  # block $label0
        if (load32(9671176) == 0):
            break
        if load32(9671192):
            while True:  # $label1
                func38(load32((load32(9671184) + (v2 << 2))))
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(load32(9671192))):
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
    v2 = load32(9671176)
    while True:  # block $label2
        v1 = load32(9671172)
        if (u(load32(9671172)) > u((v2 + 3))):
            v1 = load32(9671168)
            break
        v1 = ((v1 + load32(9671180)) + 3)
        store32(9671172, ((v1 + load32(9671180)) + 3))
        v3 = load32(9671168)
        v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
        if v2:
            # TODO: memory.copy []
        if v3:
            v2 = load32(9671176)
        store32(9671168, v1)
        break
    store32(9671176, (v2 + 1))
    store32((v1 + (v2 << 2)), arg0)
    arg0 = load32(9671176)
    store32(9671176, (load32(9671176) + 1))
    store32((v1 + (arg0 << 2)), 0)
    arg0 = load32(9671176)
    store32(9671176, (load32(9671176) + 1))
    store32((v1 + (arg0 << 2)), 0)
    if (load8u(9147336) == 0):
        while True:  # block $label3
            # TODO: f32.convert_i32_u []
            v4 = load32(9142860)
            v4 = load32(40616)
            v6 = load32(9671164)
            v5 = (((load32(9142860) - ((v4 * load32(40616)) / load32(9671164))) * 0.5) + ((v4 * float(load32(9681444))) + float(load32(9142956))))
            if (abs((((load32(9142860) - ((v4 * load32(40616)) / load32(9671164))) * 0.5) + ((v4 * float(load32(9681444))) + float(load32(9142956))))) < 2147483650.0):
                break
            break
        arg0 = -2147483648
        while True:  # block $label4
            # TODO: f32.convert_i32_u []
            v5 = load32(9142856)
            v4 = (((v4 * float(load32(9681440))) + float(load32(9142952))) + ((load32(9142856) - ((v4 * v5) / v6)) * 0.5))
            if (abs((((v4 * float(load32(9681440))) + float(load32(9142952))) + ((load32(9142856) - ((v4 * v5) / v6)) * 0.5))) < 2147483650.0):
                break
            break
    return func132(-2147483648, arg0)

# ------------------------------------------------------------
# $func370
# ------------------------------------------------------------
def func370(arg0, arg1, arg2):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # block $label0
        if ((load8u(9568060) | load8u(9147152)) == 0):
            break
        if load8u(9142917):
            break
        while True:  # block $label1
            v3 = load32(9299880)
            if load32(9299880):
                v3 = (v3 - 1)
                store32(9299880, (v3 - 1))
                v3 = load32((load32(9299872) + (v3 << 2)))
                break
            v3 = load32(9163776)
            v5 = (load32(9163776) + 1)
            store32(9163776, (load32(9163776) + 1))
            v6 = load32(9163784)
            if (u(v5) < u(load32(9163784))):
                break
            store32(v4, v6)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        break
    G.global0 = (v4 + 16)
    return v3

# ------------------------------------------------------------
# $func371
# ------------------------------------------------------------
def func371(arg0):
    if (u((load8s(load32(arg0)) - 48)) >= u(10)):
        return 0
    while True:  # $label0
        v3 = load32(arg0)
        v1 = -1
        if (u(v2) <= u(214748364)):
            v1 = (load8s(v3) - 48)
            v2 = (v2 * 10)
            v1 = (-1 if (v1 > (v2 ^ 2147483647)) else ((load8s(v3) - 48) + (v2 * 10)))
        store32(arg0, (v3 + 1))
        v2 = v1
        if (u((load8s(v3 + 1) - 48)) < u(10)):
            continue
        break
    return v2

# ------------------------------------------------------------
# $func372
# ------------------------------------------------------------
def func372(arg0, arg1):
    while True:  # block $label0
        v2 = load32(arg0 + 28)
        if (load32(arg0 + 28) <= 0):
            break
        v3 = load32(arg0 + 24)
        arg0 = 0
        while True:  # $label1
            v4 = load32((v3 + (arg0 << 2)))
            if (arg1 != load32(load32((v3 + (arg0 << 2))) + 28)):
                arg0 = (arg0 + 1)
                if (v2 != (arg0 + 1)):
                    continue
                break
            break
        return v4
        break
    return 0

# ------------------------------------------------------------
# $func373
# ------------------------------------------------------------
def func373(arg0, arg1, arg2):
    v6 = (arg0 + 1)
    v8 = load32(9147288)
    while True:  # block $label8
        while True:  # block $label1
            while True:  # block $label0
                v3 = load32(9142440)
                v10 = (u(load32(9142440)) <= u(arg1))
                if (u(load32(9142440)) <= u(arg1)):
                    break
                if (u(v3) <= u(v6)):
                    break
                if ((arg1 | v6) < 0):
                    break
                v4 = load8s((v8 + ((arg1 * v3) + v6)))
                if (load8s((v8 + ((arg1 * v3) + v6))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # block $label2
                v5 = (arg1 - 1)
                v9 = (u(v3) <= u((arg1 - 1)))
                if (u(v3) <= u((arg1 - 1))):
                    break
                if (u(v3) <= u(v6)):
                    break
                if ((v5 | v6) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + v6)))
                if (load8s((v8 + ((v3 * v5) + v6))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # block $label3
                if v9:
                    break
                if (u(arg0) >= u(v3)):
                    break
                if ((arg0 | v5) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + arg0)))
                if (load8s((v8 + ((v3 * v5) + arg0))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            v7 = (arg0 - 1)
            while True:  # block $label4
                if v9:
                    break
                if (u(v3) <= u(v7)):
                    break
                if ((v5 | v7) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + v7)))
                if (load8s((v8 + ((v3 * v5) + v7))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # block $label5
                if v10:
                    break
                if (u(v3) <= u(v7)):
                    break
                if ((arg1 | v7) < 0):
                    break
                v4 = load8s((v8 + ((arg1 * v3) + v7)))
                if (load8s((v8 + ((arg1 * v3) + v7))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # block $label6
                v5 = (arg1 + 1)
                v9 = (u(v3) <= u((arg1 + 1)))
                if (u(v3) <= u((arg1 + 1))):
                    break
                if (u(v3) <= u(v7)):
                    break
                if ((v5 | v7) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + v7)))
                if (load8s((v8 + ((v3 * v5) + v7))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            while True:  # block $label7
                if v9:
                    break
                if (u(arg0) >= u(v3)):
                    break
                if ((arg0 | v5) < 0):
                    break
                v4 = load8s((v8 + ((v3 * v5) + arg0)))
                if (load8s((v8 + ((v3 * v5) + arg0))) < 0):
                    break
                if (arg2 != v4):
                    break
                break
            arg1 = -1
            if v9:
                break
            if (u(v3) <= u(v6)):
                break
            if ((v5 | v6) < 0):
                break
            v4 = load8s((v8 + ((v3 * v5) + v6)))
            if (load8s((v8 + ((v3 * v5) + v6))) < 0):
                break
            if (arg2 == v4):
                break
            break
        arg1 = v4
        break
    return arg1

# ------------------------------------------------------------
# $func374
# ------------------------------------------------------------
def func374(arg0, arg1):
    v2 = load32(9561692)
    while True:  # block $label4
        if (arg1 == 0):
            v5 = (v2 + (arg0 * 286704))
            while True:  # $label3
                while True:  # block $label0
                    v2 = load32(((v5 + (v4 << 2)) + 284636))
                    if (load32(((v5 + (v4 << 2)) + 284636)) == 0):
                        break
                    arg0 = 0
                    arg1 = load32(v2 + 8)
                    if (load32(v2 + 8) == 0):
                        break
                    while True:  # $label2
                        while True:  # block $label1
                            v3 = load32((load32(v2) + (arg0 << 2)))
                            if (load32((load32(v2) + (arg0 << 2))) == 0):
                                break
                            v3 = (load32(9671128) + (v3 * 132))
                            if load32((load32(9671128) + (v3 * 132)) + 36):
                                break
                            func118(v3)
                            arg1 = load32(v2 + 8)
                            break
                        arg0 = (arg0 + 1)
                        if (u((arg0 + 1)) < u(arg1)):
                            continue
                        break
                    break
                v4 = (v4 + 1)
                if ((v4 + 1) != 255):
                    continue
                break
            break
        v5 = (v2 + (arg0 * 286704))
        while True:  # $label8
            while True:  # block $label5
                v2 = load32(((v5 + (v4 << 2)) + 284636))
                if (load32(((v5 + (v4 << 2)) + 284636)) == 0):
                    break
                arg0 = 0
                arg1 = load32(v2 + 8)
                if (load32(v2 + 8) == 0):
                    break
                while True:  # $label7
                    while True:  # block $label6
                        v3 = load32((load32(v2) + (arg0 << 2)))
                        if (load32((load32(v2) + (arg0 << 2))) == 0):
                            break
                        v3 = (load32(9671128) + (v3 * 132))
                        if load32((load32(9671128) + (v3 * 132)) + 36):
                            break
                        func118(v3)
                        arg1 = load32(v2 + 8)
                        break
                    arg0 = (arg0 + 1)
                    if (u((arg0 + 1)) < u(arg1)):
                        continue
                    break
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != 255):
                continue
            break
        break

# ------------------------------------------------------------
# $func375
# ------------------------------------------------------------
def func375(arg0, arg1):
    v3 = func244(load32(9142588))
    # TODO: f32.convert_i32_u []
    # TODO: f32.convert_i32_u []
    # TODO: f32.convert_i32_u []
    while True:  # block $label0
        arg0 = load32(9142588)
        if (load32(9142588) == 0):
            break
        arg1 = load32(arg0 + 16)
        arg0 = load32(arg0 + 24)
        if (load32(arg0 + 24) >= 100):
            v4 = load32((((arg0 + arg1) << 2) + 32700))
            if (((load32((((arg0 + arg1) << 2) + 32700)) < 4294967300.0) & (v4 >= 0.0)) == 0):
                break
            # TODO: i32.trunc_f32_u []
            v2 = v4
            break
        v2 = ((arg1 * 1000) // arg0)
        break

# ------------------------------------------------------------
# $func376
# ------------------------------------------------------------
def func376(arg0, arg1):
    v3 = (load32(arg1 + 52) + load32(arg0 + 52))
    store32(arg1 + 52, (load32(arg1 + 52) + load32(arg0 + 52)))
    v4 = (load32(arg1 + 60) + load32(arg0 + 60))
    store32(arg1 + 60, (load32(arg1 + 60) + load32(arg0 + 60)))
    if load32(arg0 + 84):
        v2 = load32(arg1 + 84)
        v7 = load32(9561692)
        while True:  # $label0
            store32(arg1 + 80, 0)
            v5 = (v2 + 1)
            store32(arg1 + 84, (v2 + 1))
            v2 = (v7 + (load16u(arg1 + 110) * 286704))
            v6 = ((v7 + (load16u(arg1 + 110) * 286704)) + 281672)
            store32(((v7 + (load16u(arg1 + 110) * 286704)) + 281672), (load32(v6) + 1))
            if (load32((v2 + 284388)) == v5):
                func201(arg1)
                store32(v2 + 283936, (load32(v2 + 283936) + 1))
                v3 = (v2 + 281636)
                store32((v2 + 281636), (load32(v3) + 1))
                v4 = load32(arg1 + 60)
                v7 = load32(9561692)
                v3 = load32(arg1 + 52)
            v2 = (v2 + 284020)
            store32(arg1 + 64, (load32(arg1 + 64) + load32((v2 + 284020))))
            store32(arg1 + 68, (load32(arg1 + 68) + load32(v2)))
            v2 = load32(arg1 + 84)
            v5 = (v2 & 1)
            v6 = (load32(((load8u(arg1 + 122) * 404) + 9568096) + 224) > 1)
            v4 = ((((load32(arg1 + 84) & 3) == 1) if (load32(((load8u(arg1 + 122) * 404) + 9568096) + 224) > 1) else (v2 & 1)) + v4)
            store32(arg1 + 60, ((((load32(arg1 + 84) & 3) == 1) if (load32(((load8u(arg1 + 122) * 404) + 9568096) + 224) > 1) else (v2 & 1)) + v4))
            v3 = ((v5 if v6 else 1) + v3)
            store32(arg1 + 52, ((v5 if v6 else 1) + v3))
            v8 = (v8 + 1)
            if (u((v8 + 1)) < u(load32(arg0 + 84))):
                continue
            break
    v2 = load32(arg1 + 72)
    while True:  # block $label1
        v3 = load32(arg0 + 72)
        if (load32(arg0 + 72) == 0):
            break
        if v2:
            break
        v2 = load32(arg1 + 72)
        v3 = load32(arg0 + 72)
        break
    store32(arg1 + 72, (v2 + v3))
    store32(arg1 + 76, (load32(arg1 + 76) + load32(arg0 + 76)))
    arg0 = load32(arg0 + 80)
    store32(arg1 + 64, (load32(arg0 + 80) + load32(arg1 + 64)))
    store32(arg1 + 68, (arg0 + load32(arg1 + 68)))
    while True:  # block $label2
        if (load32(arg1 + 92) == 0):
            break
        if load32(9140316):
            if (load32(9140320) != load32(arg1 + 28)):
                break
        break

# ------------------------------------------------------------
# $func377
# ------------------------------------------------------------
def func377(arg0, param1):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v1 = load32(9671128)
    v1 = (load32(9671128) + (load32((load32(load32((v1 + (load32(9173808) * 132)) + 16)) + ((load32(9213816) + (load32(9147120) * load32(9143000))) << 2))) * 132))
    v2 = load32((load32(9671128) + (load32((load32(load32((v1 + (load32(9173808) * 132)) + 16)) + ((load32(9213816) + (load32(9147120) * load32(9143000))) << 2))) * 132)) + 28)
    store32(arg0 + 12, load32((load32(9671128) + (load32((load32(load32((v1 + (load32(9173808) * 132)) + 16)) + ((load32(9213816) + (load32(9147120) * load32(9143000))) << 2))) * 132)) + 28))
    while True:  # block $label1
        while True:  # block $label0
            v3 = load8u(v1 + 122)
            v4 = load32(((load8u(v1 + 122) * 404) + 9568096) + 172)
            if (load32(((load8u(v1 + 122) * 404) + 9568096) + 172) == 0):
                break
            if load32(9213812):
                break
            if load8u(9163793):
                if (u(load32(((v3 * 404) + 9568096) + 268)) > u(1)):
                    break
                if load8u(9147210):
                    func41(39, (arg0 + 12), 1, 0, 0)
                    break
                v1 = func26(4)
                store32(func26(4), v2)
                # call_indirect[load32(9214136)]
                break
            v2 = ((v4 * 132) + 9216080)
            # call_indirect[load32(v2)]
            store32(9142896, load32(v1 + 28))
            break
            break
        if load8u(9147210):
            func41(1, (arg0 + 12), 1, 0, 0)
            break
        v1 = func26(4)
        store32(func26(4), v2)
        # call_indirect[load32(9213832)]
        break
    G.global0 = (arg0 + 16)

# ------------------------------------------------------------
# $func378
# ------------------------------------------------------------
def func378(arg0, arg1):
    func29((load32(9671128) + (arg0 * 132)), 1)

# ------------------------------------------------------------
# $rc
# Export: rc
# ------------------------------------------------------------
def rc(arg0, arg1, arg2, arg3, param4, param5):
    """Exported as rc."""
    v8 = (G.global0 - 40000)
    G.global0 = (G.global0 - 40000)
    while True:  # block $label0
        if (load32(51776) == 0):
            store8(9215872, 1)
            func216(9216024, arg0, arg1, arg2, arg3)
            break
        arg1 = (arg1 == 2147483647)
        store32(9213812, (0 if (arg1 == 2147483647) else arg1))
        if arg2:
            v11 = ((arg2 * 132) + 9216080)
            if (load8u(((arg2 * 132) + 9216080) + 23) == 0):
                break
            v4 = load32(9142872)
            v6 = load32(9561692)
            v5 = load32(9213808)
            if load32(9213808):
                # TODO: memory.copy []
            store32(9213808, 0)
            while True:  # block $label1
                v7 = load32((((v6 + (v4 * 286704)) + (arg3 << 2)) + 284636))
                if (load32((((v6 + (v4 * 286704)) + (arg3 << 2)) + 284636)) == 0):
                    break
                arg0 = load32(v7 + 8)
                if (load32(v7 + 8) == 0):
                    break
                arg1 = 0
                v9 = load32(9671128)
                v10 = load32(v7)
                while True:  # block $label4
                    if (load8u(9147152) == 0):
                        v6 = ((v6 + (v4 * 286704)) + 283908)
                        v12 = load32(9215884)
                        v13 = load32(9142892)
                        v14 = load32(9143008)
                        arg3 = 0
                        while True:  # $label3
                            while True:  # block $label2
                                v4 = load32((v10 + (arg1 << 2)))
                                if (load32((v10 + (arg1 << 2))) == 0):
                                    break
                                v4 = (v9 + (v4 * 132))
                                if (load8u((v14 + (load32(v6) + (v13 * load16u((v9 + (v4 * 132)) + 110))))) == 0):
                                    break
                                if (load32((v12 + (load32(v4 + 44) << 4)) + 4) == 20):
                                    break
                                if (load8u(v4 + 127) == 6):
                                    break
                                store32(((arg3 << 2) + 9173808), load32(v4 + 28))
                                arg3 = (arg3 + 1)
                                store32(9213808, (arg3 + 1))
                                arg0 = load32(v7 + 8)
                                break
                            arg1 = (arg1 + 1)
                            if (u((arg1 + 1)) < u(arg0)):
                                continue
                            break
                        break
                    arg3 = 0
                    while True:  # $label5
                        v4 = load32((v10 + (arg1 << 2)))
                        if load32((v10 + (arg1 << 2))):
                            store32(((arg3 << 2) + 9173808), load32((v9 + (v4 * 132)) + 28))
                            arg3 = (arg3 + 1)
                            store32(9213808, (arg3 + 1))
                            arg0 = load32(v7 + 8)
                        arg1 = (arg1 + 1)
                        if (u((arg1 + 1)) < u(arg0)):
                            continue
                        break
                    break
                if (arg3 == 0):
                    break
                arg0 = load32(v11)
                if (load32(v11) == 12):
                    store32(9213808, 0)
                # call_indirect[arg0]
                break
            if v5:
                # TODO: memory.copy []
            store32(9213808, v5)
            break
        while True:  # block $label6
            arg2 = ((0 if arg1 else (load32(9143000) * load32(9147120))) + arg0)
            arg3 = load32(9671120)
            if (u(((0 if arg1 else (load32(9143000) * load32(9147120))) + arg0)) >= u(load32(9671120))):
                arg1 = load32(9681836)
                if ((load32(9681836) | load8u(9147141)) == 0):
                    break
                if (u(arg0) < u(arg3)):
                    break
                break
            arg1 = load32(9681836)
            break
        store32(9213816, arg0)
        if arg1:
            arg0 = (G.global0 - 16)
            G.global0 = (G.global0 - 16)
            func45()
            arg1 = load32(9143000)
            store32(9143000, 0)
            arg2 = (load32(9213816) + (arg1 * load32(9147120)))
            if (u((load32(9213816) + (arg1 * load32(9147120)))) <= u(load32(9681836))):
                while True:  # block $label8
                    while True:  # block $label9
                        while True:  # block $label7
                            arg1 = load32(9671128)
                            arg3 = load32((load32(9681828) + (arg2 << 2)))
                            arg2 = (load32(9671128) + (load32((load32(9681828) + (arg2 << 2))) * 132))
                            if (load32(((load8u((load32(9671128) + (load32((load32(9681828) + (arg2 << 2))) * 132)) + 122) * 404) + 9568096) + 264) != 2):
                                break
                            v5 = load32(arg2 + 36)
                            if (load32(arg2 + 36) == 0):
                                break
                            arg1 = (arg1 + (v5 * 132))
                            func44((arg1 + (v5 * 132)), 0)
                            if load8u(9142917):
                                break
                            arg2 = load32(arg1 + 36)
                            arg1 = (load32(9671128) + ((load32(arg1 + 36) if arg2 else load32(arg1 + 28)) * 132))
                            arg2 = load8u((load32(9671128) + ((load32(arg1 + 36) if arg2 else load32(arg1 + 28)) * 132)) + 122)
                            arg3 = (((load32(((load8u((load32(9671128) + ((load32(arg1 + 36) if arg2 else load32(arg1 + 28)) * 132)) + 122) * 404) + 9568096) + 220) << 4) & 2147483632) + (load16u(arg1 + 114) << 5))
                            break
                            break
                        func44(arg2, 0)
                        if load8u(9142917):
                            break
                        arg1 = (arg1 + (arg3 * 132))
                        arg2 = load32((arg1 + (arg3 * 132)) + 36)
                        arg1 = (load32(9671128) + ((load32((arg1 + (arg3 * 132)) + 36) if arg2 else load32(arg1 + 28)) * 132))
                        arg2 = load8u((load32(9671128) + ((load32((arg1 + (arg3 * 132)) + 36) if arg2 else load32(arg1 + 28)) * 132)) + 122)
                        arg3 = (((load32(((load8u((load32(9671128) + ((load32((arg1 + (arg3 * 132)) + 36) if arg2 else load32(arg1 + 28)) * 132)) + 122) * 404) + 9568096) + 220) << 4) & 2147483632) + (load16u(arg1 + 114) << 5))
                        break
                    arg1 = (arg1 + 112)
                    arg2 = load32(((arg2 * 404) + 9568096) + 216)
                    arg1 = load16u(arg1)
                    store32(arg0 + 4, arg3)
                    store32(arg0, (((arg2 << 4) & 2147483632) + (arg1 << 5)))
                    break
            G.global0 = (arg0 + 16)
            break
        if load8u(9147141):
            func377(func28(0, 0), arg1)
            break
        arg0 = load32(((arg2 << 2) + 9263072))
        if (load32(((arg2 << 2) + 9263072)) == 0):
            break
        arg1 = load32(arg0)
        while True:  # block $label10
            if load8u(arg0 + 20):
                # call_indirect[arg1]
                break
            while True:  # block $label11
                if (arg1 != 5):
                    break
                if (load32(9213812) != 2):
                    break
                func242(load32(arg0 + 4))
                break
            break
        break
    G.global0 = (v8 + 40000)
    return indirect_call(arg1)