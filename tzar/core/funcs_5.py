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
# $sc
# Export: sc
# ------------------------------------------------------------
def sc(arg0):
    """Exported as sc."""
    v12 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    if (arg0 == 0):
        func45()
    if load8u(9147152):
        store32(9147132, load8u(9216060))
    if load8u(9142917):
        store32(load32(9142424) + 48, load32(9142832))
    v9 = load32(9142892)
    v31 = (load32(9142892) * 3020)
    v34 = load32(9681936)
    v35 = (load32(load32(9681936) + 8) * 3)
    v17 = (((load32(load32(9681936) + 8) * 3) & 0xFFFFFFFF) >> 2)
    v21 = load32(9142440)
    v11 = (load32(9142440) * v21)
    v25 = ((((load32(9142440) * v21) & 0xFFFFFFFF) >> 2) + 1)
    v7 = load32(9142848)
    v26 = load32(9215892)
    v10 = (v9 * v9)
    v36 = load32(9671136)
    v22 = load32(9142912)
    v27 = load32(9684484)
    v28 = load32(9684468)
    v29 = load32(9684452)
    v30 = (load32(9684484) + (load32(9684468) + load32(9684452)))
    while True:  # block $label0
        v13 = load32(9147132)
        if load32(9147132):
            break
        if (v7 == 0):
            break
        if (u((load32(load32(9142424) + 48) - 1)) > u(1)):
            break
        break
    v33 = (((v11 & 0xFFFFFFFF) >> 5) + 1)
    v5 = (v17 - -64)
    v23 = (load32(9142912) + ((load32(9684484) + (load32(9684468) + load32(9684452))) + ((((v11 & 0xFFFFFFFF) >> 5) + 1) + (((((v17 - -64) + v31) + v26) + (v10 << 2)) + v25))))
    v24 = load32(9142428)
    v3 = load32(9568068)
    v32 = load32(9568064)
    v14 = ((load32(9568068) - load32(9568064)) >> 7)
    v39 = (v3 == v32)
    if ((v3 == v32) == 0):
        v15 = (1 if (u(v14) <= u(1)) else v14)
        while True:  # $label3
            v3 = (v32 + (v8 << 7))
            v2 = ((v2 + load32((v32 + (v8 << 7)) + 104)) + 8)
            v4 = load32(v3 + 4)
            v6 = load32(v3)
            if (load32(v3 + 4) != load32(v3)):
                v4 = ((v4 - v6) // 196)
                v19 = (1 if (u(v4) <= u(1)) else ((v4 - v6) // 196))
                v1 = 0
                while True:  # $label1
                    v4 = (v6 + (v1 * 196))
                    v2 = ((((((v2 + load32((v6 + (v1 * 196)) + 192)) + load32(v4 + 56)) + load32(v4 + 72)) + load32(v4 + 88)) + load32(v4 + 104)) + 19)
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v19):
                        continue
                    break
            v1 = load32(v3 + 16)
            v4 = load32(v3 + 12)
            if (load32(v3 + 16) != load32(v3 + 12)):
                v3 = ((v1 - v4) // 196)
                v6 = (1 if (u(v3) <= u(1)) else ((v1 - v4) // 196))
                v1 = 0
                while True:  # $label2
                    v3 = (v4 + (v1 * 196))
                    v2 = ((((((v2 + load32((v4 + (v1 * 196)) + 192)) + load32(v3 + 56)) + load32(v3 + 72)) + load32(v3 + 88)) + load32(v3 + 104)) + 19)
                    v1 = (v1 + 1)
                    if ((v1 + 1) != v6):
                        continue
                    break
            v8 = (v8 + 1)
            if ((v8 + 1) != v15):
                continue
            break
    v6 = (v23 + v24)
    v3 = 0
    while True:  # block $label4
        if (v36 == 0):
            v8 = 0
            v23 = 0
            break
        v23 = 0
        v15 = load32(38448)
        v19 = load32(9671128)
        v8 = 0
        v1 = 0
        while True:  # $label6
            while True:  # block $label5
                v4 = (v19 + (v1 * 132))
                if (load8u((v19 + (v1 * 132)) + 122) == v15):
                    v8 = (v8 + 4)
                    break
                v18 = load32(v4 + 16)
                if load32(v4 + 16):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v18 = load32(v4 + 20)
                if load32(v4 + 20):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v23 = (v23 + 33)
                v4 = load32(v4 + 24)
                if (load32(v4 + 24) == 0):
                    break
                v18 = load32(v4)
                if load32(v4):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v18 = load32(v4 + 12)
                if load32(v4 + 12):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v18 = load32(v4 + 8)
                if load32(v4 + 8):
                    v6 = ((v6 + load32(v18 + 8)) + 1)
                v4 = load32(v4 + 4)
                if (load32(v4 + 4) == 0):
                    break
                v6 = ((v6 + load32(v4 + 8)) + 1)
                break
            v1 = (v1 + 1)
            if ((v1 + 1) != v36):
                continue
            break
        break
    v15 = (((802 if v13 else ((v9 * 1020) + 802)) * v9) if (v7 | v13) else 0)
    if v9:
        v19 = (v9 + 1)
        v18 = ((v7 == 0) | (v13 != 0))
        v37 = load32(9561692)
        v1 = 0
        while True:  # $label8
            v4 = (v37 + (v1 * 286704))
            v20 = load32((v37 + (v1 * 286704)) + 281788)
            if load32((v37 + (v1 * 286704)) + 281788):
                v3 = ((v3 + load32(v20 + 8)) + 1)
            v20 = load32(v4 + 281792)
            if load32(v4 + 281792):
                v3 = ((v3 + load32(v20 + 8)) + 1)
            v20 = load32(v4 + 281796)
            if load32(v4 + 281796):
                v3 = ((v3 + load32(v20 + 8)) + 1)
            v20 = load32(v4 + 286680)
            if load32(v4 + 286680):
                v3 = ((v3 + load32(v20 + 8)) + 1)
            v20 = (v19 if load32(v4 + 281800) else 0)
            while True:  # block $label7
                if v18:
                    break
                v4 = load32((v4 + 278572))
                if (load32((v4 + 278572)) == 0):
                    break
                v15 = ((v15 + load32(v4 + 8)) + 1)
                break
            v3 = (v3 + v20)
            v1 = (v1 + 1)
            if ((v1 + 1) != v9):
                continue
            break
    v1 = 0
    v18 = (((((v2 + v6) + v8) + v23) + v3) + v15)
    v37 = ((((((v2 + v6) + v8) + v23) + v3) + v15) << 2)
    v3 = (-1 if (u(v18) > u(1073741823)) else ((((((v2 + v6) + v8) + v23) + v3) + v15) << 2))
    v4 = func26((-1 if (u(v18) > u(1073741823)) else ((((((v2 + v6) + v8) + v23) + v3) + v15) << 2)))
    # TODO: memory.fill []
    v3 = load32(9142872)
    v6 = load32(59168)
    store32(v4 + 4, v17)
    store32(v4, v6)
    v6 = load8u(9147208)
    store32(v4 + 24, v22)
    store32(v4 + 20, v27)
    store32(v4 + 16, v28)
    store32(v4 + 12, v29)
    store32(v4 + 8, v6)
    store32(v4 + 28, (0 if v13 else load32(9142952)))
    v6 = load32(9142956)
    store32(v4 + 40, v26)
    store32(v4 + 36, v9)
    store32(v4 + 32, (0 if v13 else v6))
    v9 = load32(9163776)
    store32(v4 + 68, (0 if v13 else v3))
    store32(v4 + 64, v36)
    store32(v4 + 60, v23)
    store32(v4 + 56, v8)
    store32(v4 + 52, v7)
    store32(v4 + 48, v21)
    store32(v4 + 44, (0 if v13 else v9))
    v3 = load32(9561752)
    store32(v4 + 76, v2)
    store32(v4 + 72, v3)
    v21 = load32(9142424)
    v3 = load32(load32(9142424) + 48)
    store32(v4 + 84, v24)
    store32(v4 + 80, v3)
    store32(v4 + 88, load32(9684364))
    store32(v4 + 92, load32(9684368))
    store32(v4 + 96, load32(9684372))
    store32(v4 + 100, load32(9684340))
    store32(v4 + 104, load32(9684344))
    store32(v4 + 108, load32(9684348))
    store32(v4 + 112, load32(9684352))
    store32(v4 + 116, load32(9684356))
    store32(v4 + 120, load32(9684360))
    store32(v4 + 124, load8u(9147209))
    store32(v4 + 128, load32(9147312))
    store32(v4 + 132, load32(9147316))
    store32(v4 + 136, load32(9147320))
    v3 = load32(9147324)
    store32(v4 + 152, v31)
    store32(v4 + 148, v13)
    store32(v4 + 144, v15)
    store32(v4 + 140, v3)
    v20 = (v5 + v30)
    v25 = (v2 + (v5 + v30))
    v2 = (v24 + (v2 + (v5 + v30)))
    v24 = (v25 + (v24 + (v2 + (v5 + v30))))
    v27 = ((v25 + (v24 + (v2 + (v5 + v30)))) + v10)
    v28 = (((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10)
    v29 = ((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10)
    v30 = (((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10)
    v19 = ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)
    v22 = (v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26))
    v9 = ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33)
    v40 = (v31 + ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33))
    v31 = (v8 + (v31 + ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33)))
    v3 = ((v8 + (v31 + ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33))) + v23)
    store32(v12 + 28, (v15 + ((v8 + (v31 + ((v22 + ((((((v25 + (v24 + (v2 + (v5 + v30)))) + v10) + v10) + v10) + v10) + v26)) + v33))) + v23)))
    while True:  # block $label9
        if (v11 == 0):
            break
        v2 = (v4 + (v2 << 2))
        v6 = load32(9147288)
        if (u(v11) >= u(4)):
            v8 = (v11 & -4)
            v7 = 0
            while True:  # $label10
                v16 = load8s((v1 + v6))
                store8((v1 + v2), (((load8s((v1 + v6)) & 0xFFFFFFFF) >> 7) ^ v16))
                v16 = (v1 | 1)
                v16 = load8s((v6 + v16))
                store8((v2 + (v1 | 1)), (((load8s((v6 + v16)) & 0xFFFFFFFF) >> 7) ^ v16))
                v16 = (v1 | 2)
                v16 = load8s((v6 + v16))
                store8((v2 + (v1 | 2)), (((load8s((v6 + v16)) & 0xFFFFFFFF) >> 7) ^ v16))
                v16 = (v1 | 3)
                v16 = load8s((v6 + v16))
                store8((v2 + (v1 | 3)), (((load8s((v6 + v16)) & 0xFFFFFFFF) >> 7) ^ v16))
                v1 = (v1 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v8):
                    continue
                break
        v8 = (v11 & 3)
        if ((v11 & 3) == 0):
            break
        v7 = 0
        while True:  # $label11
            v16 = load8s((v1 + v6))
            store8((v1 + v2), (((load8s((v1 + v6)) & 0xFFFFFFFF) >> 7) ^ v16))
            v1 = (v1 + 1)
            v7 = (v7 + 1)
            if ((v7 + 1) != v8):
                continue
            break
        break
    while True:  # block $label12
        if (v33 == 0):
            break
        v1 = load32(9147376)
        if (load32(9147376) == 0):
            break
        if v13:
            break
        if (v11 == 0):
            break
        v6 = (v4 + (v22 << 2))
        v2 = 0
        if (v11 != 1):
            v13 = (v11 & -2)
            v7 = 0
            while True:  # $label13
                v8 = (v6 + (((v2 & 0xFFFFFFFF) >> 3) & 536870908))
                v22 = (load32(v8) | ((load16u((v1 + (v2 << 1))) != 0) << (v2 & 30)))
                store32((v6 + (((v2 & 0xFFFFFFFF) >> 3) & 536870908)), (load32(v8) | ((load16u((v1 + (v2 << 1))) != 0) << (v2 & 30))))
                v8 = (v2 | 1)
                store32(v8, (((load16u((v1 + ((v2 | 1) << 1))) != 0) << v8) | v22))
                v2 = (v2 + 2)
                v7 = (v7 + 2)
                if ((v7 + 2) != v13):
                    continue
                break
        if ((v11 & 1) == 0):
            break
        v6 = (v6 + (((v2 & 0xFFFFFFFF) >> 3) & 536870908))
        store32((v6 + (((v2 & 0xFFFFFFFF) >> 3) & 536870908)), (load32(v6) | ((load16u((v1 + (v2 << 1))) != 0) << v2)))
        break
    if (u(v35) >= u(4)):
        v7 = load32(v34)
        v2 = 0
        while True:  # $label14
            v6 = (v2 << 2)
            v1 = ((v2 << 2) + v4)
            # TODO: i32.div_u []
            v6 = (v6 + (3 << 2))
            store32(v7 + 256, load32((v6 + (3 << 2))))
            store32(v1 + 260, load32(v6 + 4))
            store32(v1 + 264, load32(v6 + 8))
            v2 = (v2 + 3)
            if (u((v2 + 3)) < u(v17)):
                continue
            break
    while True:  # block $label15
        v2 = load32(9684452)
        if (load32(9684452) == 0):
            break
        v13 = (v2 & 3)
        v8 = 0
        v1 = load32(9684444)
        while True:  # block $label16
            if (u(v2) < u(4)):
                v2 = 0
                break
            v17 = (v2 & -4)
            v2 = 0
            v7 = 0
            while True:  # $label17
                v6 = (v4 + (v5 << 2))
                v11 = (v2 << 2)
                store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
                store32(v6 + 4, load32((v1 + (v11 | 4))))
                store32(v6 + 8, load32((v1 + (v11 | 8))))
                store32(v6 + 12, load32((v1 + (v11 | 12))))
                v2 = (v2 + 4)
                v5 = (v5 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v17):
                    continue
                break
            break
        if (v13 == 0):
            break
        while True:  # $label18
            store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
            v2 = (v2 + 1)
            v5 = (v5 + 1)
            v8 = (v8 + 1)
            if ((v8 + 1) != v13):
                continue
            break
        break
    while True:  # block $label19
        v2 = load32(9684468)
        if (load32(9684468) == 0):
            break
        v13 = (v2 & 3)
        v8 = 0
        v1 = load32(9684460)
        while True:  # block $label20
            if (u(v2) < u(4)):
                v2 = 0
                break
            v17 = (v2 & -4)
            v2 = 0
            v7 = 0
            while True:  # $label21
                v6 = (v4 + (v5 << 2))
                v11 = (v2 << 2)
                store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
                store32(v6 + 4, load32((v1 + (v11 | 4))))
                store32(v6 + 8, load32((v1 + (v11 | 8))))
                store32(v6 + 12, load32((v1 + (v11 | 12))))
                v2 = (v2 + 4)
                v5 = (v5 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v17):
                    continue
                break
            break
        if (v13 == 0):
            break
        while True:  # $label22
            store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
            v2 = (v2 + 1)
            v5 = (v5 + 1)
            v8 = (v8 + 1)
            if ((v8 + 1) != v13):
                continue
            break
        break
    while True:  # block $label23
        v2 = load32(9684484)
        if (load32(9684484) == 0):
            break
        v13 = (v2 & 3)
        v8 = 0
        v1 = load32(9684476)
        while True:  # block $label24
            if (u(v2) < u(4)):
                v2 = 0
                break
            v17 = (v2 & -4)
            v2 = 0
            v7 = 0
            while True:  # $label25
                v6 = (v4 + (v5 << 2))
                v11 = (v2 << 2)
                store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
                store32(v6 + 4, load32((v1 + (v11 | 4))))
                store32(v6 + 8, load32((v1 + (v11 | 8))))
                store32(v6 + 12, load32((v1 + (v11 | 12))))
                v2 = (v2 + 4)
                v5 = (v5 + 4)
                v7 = (v7 + 4)
                if ((v7 + 4) != v17):
                    continue
                break
            break
        if (v13 == 0):
            break
        while True:  # $label26
            store32((v4 + (v5 << 2)), load32((v1 + (v2 << 2))))
            v2 = (v2 + 1)
            v5 = (v5 + 1)
            v8 = (v8 + 1)
            if ((v8 + 1) != v13):
                continue
            break
        break
    store32(v12 + 24, v20)
    if (v39 == 0):
        v14 = (1 if (u(v14) <= u(1)) else v14)
        v13 = 0
        while True:  # $label30
            v2 = load32(v12 + 24)
            v1 = (v4 + (load32(v12 + 24) << 2))
            v8 = (v32 + (v13 << 7))
            v17 = load32((v32 + (v13 << 7)) + 4)
            v7 = load32(v8)
            store32((v4 + (load32(v12 + 24) << 2)), ((load32((v32 + (v13 << 7)) + 4) - load32(v8)) // 196))
            v11 = load32(v8 + 16)
            v5 = load32(v8 + 12)
            store32(v1 + 4, ((load32(v8 + 16) - load32(v8 + 12)) // 196))
            store32(v1 + 8, load32(v8 + 104))
            v1 = (v2 + 3)
            if load32(v8 + 104):
                v6 = 0
                while True:  # $label27
                    store32((v4 + (v1 << 2)), load16u((v8 + (v6 << 1)) + 24))
                    v1 = (v1 + 1)
                    v6 = (v6 + 1)
                    if (u((v6 + 1)) < u(load32(v8 + 104))):
                        continue
                    break
            v2 = (v4 + (v1 << 2))
            store32((v4 + (v1 << 2)), load32(v8 + 108))
            store32(v2 + 4, load32(v8 + 112))
            store32(v2 + 8, load32(v8 + 116))
            store32(v2 + 12, load32(v8 + 120))
            v6 = load32(v8 + 124)
            store32(v12 + 24, (v1 + 5))
            store32(v2 + 16, v6)
            v1 = 0
            v2 = 0
            if (v7 != v17):
                while True:  # $label28
                    func382((v7 + (v1 * 196)), v4, (v12 + 24))
                    v1 = (v1 + 1)
                    v7 = load32(v8)
                    if (u((v1 + 1)) < u(((load32(v8 + 4) - load32(v8)) // 196))):
                        continue
                    break
                v11 = load32(v8 + 16)
                v5 = load32(v8 + 12)
            if (v5 != v11):
                while True:  # $label29
                    func382((v5 + (v2 * 196)), v4, (v12 + 24))
                    v2 = (v2 + 1)
                    v5 = load32(v8 + 12)
                    if (u((v2 + 1)) < u(((load32(v8 + 16) - load32(v8 + 12)) // 196))):
                        continue
                    break
            v13 = (v13 + 1)
            if ((v13 + 1) != v14):
                continue
            break
    while True:  # block $label31
        if (v15 == 0):
            break
        v8 = 0
        v17 = load32(9142892)
        if (load32(9142892) == 0):
            break
        v1 = (v17 * 255)
        v1 = (1 if (u(v1) <= u(1)) else (v17 * 255))
        v13 = ((1 if (u(v1) <= u(1)) else (v17 * 255)) & -4)
        v11 = (v1 & 3)
        v33 = load32(9147132)
        v32 = load32(9561692)
        v34 = (v1 - 1)
        v35 = (u((v1 - 1)) > u(2))
        while True:  # $label45
            while True:  # block $label32
                if v33:
                    break
                v15 = (v32 + (v8 * 286704))
                v6 = load32((v32 + (v8 * 286704)) + 278556)
                v7 = 0
                v2 = 0
                v1 = 0
                if v35:
                    while True:  # $label33
                        v14 = (v4 + (v3 << 2))
                        v5 = (v2 << 2)
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        store32(v14 + 4, load32((v6 + (v5 | 4))))
                        store32(v14 + 8, load32((v6 + (v5 | 8))))
                        store32(v14 + 12, load32((v6 + (v5 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v13):
                            continue
                        break
                if v11:
                    while True:  # $label34
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v6 = load32((v15 + 278560))
                v7 = 0
                v2 = 0
                v1 = 0
                v22 = (u(v34) < u(3))
                if ((u(v34) < u(3)) == 0):
                    while True:  # $label35
                        v14 = (v4 + (v3 << 2))
                        v5 = (v2 << 2)
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        store32(v14 + 4, load32((v6 + (v5 | 4))))
                        store32(v14 + 8, load32((v6 + (v5 | 8))))
                        store32(v14 + 12, load32((v6 + (v5 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v13):
                            continue
                        break
                if v11:
                    while True:  # $label36
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v6 = load32((v15 + 278564))
                v7 = 0
                v2 = 0
                v1 = 0
                if (v22 == 0):
                    while True:  # $label37
                        v14 = (v4 + (v3 << 2))
                        v5 = (v2 << 2)
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        store32(v14 + 4, load32((v6 + (v5 | 4))))
                        store32(v14 + 8, load32((v6 + (v5 | 8))))
                        store32(v14 + 12, load32((v6 + (v5 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v13):
                            continue
                        break
                if v11:
                    while True:  # $label38
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v6 = load32((v15 + 278568))
                v7 = 0
                v2 = 0
                v1 = 0
                if (v22 == 0):
                    while True:  # $label39
                        v5 = (v4 + (v3 << 2))
                        v14 = (v2 << 2)
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        store32(v5 + 4, load32((v6 + (v14 | 4))))
                        store32(v5 + 8, load32((v6 + (v14 | 8))))
                        v5 = (v3 + 3)
                        store32((v4 + ((v3 + 3) << 2)), load32((v6 + (v14 | 12))))
                        v2 = (v2 + 4)
                        v3 = (v3 + 4)
                        v1 = (v1 + 4)
                        if ((v1 + 4) != v13):
                            continue
                        break
                if v11:
                    while True:  # $label40
                        v5 = v3
                        store32((v4 + (v3 << 2)), load32((v6 + (v2 << 2))))
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v11):
                            continue
                        break
                v1 = load32((v15 + 278572))
                store32((v4 + (v3 << 2)), load32(load32((v15 + 278572)) + 8))
                v3 = (v5 + 2)
                if (load32(v1 + 8) == 0):
                    break
                v5 = load32(v1)
                v2 = 0
                while True:  # $label41
                    store32((v4 + (v3 << 2)), load32((v5 + (v2 << 2))))
                    v3 = (v3 + 1)
                    v2 = (v2 + 1)
                    if (u((v2 + 1)) < u(load32(v1 + 8))):
                        continue
                    break
                break
            v1 = 0
            v6 = 0
            while True:  # $label42
                v5 = (v4 + (v3 << 2))
                v2 = (v32 + (v8 * 286704))
                v7 = ((v32 + (v8 * 286704)) + (v6 << 2))
                store32((v4 + (v3 << 2)), load32((((v32 + (v8 * 286704)) + (v6 << 2)) + 278576)))
                store32(v5 + 4, load32((v7 + 278580)))
                store32(v5 + 8, load32((v7 + 278584)))
                v3 = (v3 + 3)
                v6 = (v6 + 3)
                if ((v6 + 3) != 255):
                    continue
                break
            while True:  # $label43
                v5 = (v4 + (v3 << 2))
                v6 = (v2 + (v1 << 2))
                store32((v4 + (v3 << 2)), load32(((v2 + (v1 << 2)) + 279596)))
                store32(v5 + 4, load32((v6 + 279600)))
                store32(v5 + 8, load32((v6 + 279604)))
                v3 = (v3 + 3)
                v1 = (v1 + 3)
                if ((v1 + 3) != 255):
                    continue
                break
            v6 = 0
            while True:  # $label44
                v5 = v3
                v1 = (v4 + (v3 << 2))
                v3 = (v2 + (v6 << 2))
                store32((v4 + (v3 << 2)), load32(((v2 + (v6 << 2)) + 280616)))
                store32(v1 + 4, load32((v3 + 280620)))
                store32(v1 + 8, load32((v3 + 280624)))
                v3 = (v5 + 3)
                v6 = (v6 + 3)
                if ((v6 + 3) != 255):
                    continue
                break
            store32((v4 + (v3 << 2)), load32((v2 + 281636)))
            store32(v1 + 16, load32((v2 + 281640)))
            store32(v1 + 20, load32((v2 + 281644)))
            store32(v1 + 24, load32((v2 + 281648)))
            store32(v1 + 28, load32((v2 + 281652)))
            store32(v1 + 32, load32((v2 + 281656)))
            store32(v1 + 36, load32((v2 + 281660)))
            store32(v1 + 40, load32((v2 + 281664)))
            store32(v1 + 44, load32((v2 + 281668)))
            store32(v1 + 48, load32((v2 + 281672)))
            store32(v1 + 52, load32((v2 + 281676)))
            store32(v1 + 56, load32((v2 + 281680)))
            store32(v1 + 60, load32((v2 + 281684)))
            store32((v1 - -64), load32((v2 + 281688)))
            store32(v1 + 68, load32((v2 + 281692)))
            store32(v1 + 72, load32((v2 + 281696)))
            store32(v1 + 76, load32((v2 + 281700)))
            store32(v1 + 80, load32((v2 + 281704)))
            store32(v1 + 84, load32((v2 + 281708)))
            store32(v1 + 88, load32((v2 + 281712)))
            store32(v1 + 92, load32((v2 + 281716)))
            store32(v1 + 96, load32((v2 + 281720)))
            store32(v1 + 100, load32((v2 + 281724)))
            store32(v1 + 104, load32((v2 + 281728)))
            store32(v1 + 108, load32((v2 + 281732)))
            store32(v1 + 112, load32((v2 + 281736)))
            store32(v1 + 116, load32((v2 + 281740)))
            store32(v1 + 120, load32((v2 + 281744)))
            store32(v1 + 124, load32((v2 + 281748)))
            store32(v1 + 128, load32((v2 + 281752)))
            store32(v1 + 132, load32((v2 + 281756)))
            store32(v1 + 136, load32((v2 + 281760)))
            store32(v1 + 140, load32((v2 + 281764)))
            store32(v1 + 144, load32((v2 + 281768)))
            store32(v1 + 148, load32((v2 + 281772)))
            store32(v1 + 152, load32((v2 + 281776)))
            store32(v1 + 156, load32((v2 + 281780)))
            v3 = (v5 + 40)
            v8 = (v8 + 1)
            if ((v8 + 1) != v17):
                continue
            break
        break
    v3 = 0
    while True:  # block $label46
        v5 = load32(9142428)
        if (load32(9142428) == 0):
            break
        if (u(v5) >= u(4)):
            v1 = (v5 & -4)
            v2 = 0
            while True:  # $label47
                store32((v4 + ((v3 + v25) << 2)), load32((v21 + (v3 << 2))))
                v6 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v25) << 2)), load32((v21 + (v6 << 2))))
                v6 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v25) << 2)), load32((v21 + (v6 << 2))))
                v6 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v25) << 2)), load32((v21 + (v6 << 2))))
                v3 = (v3 + 4)
                v2 = (v2 + 4)
                if ((v2 + 4) != v1):
                    continue
                break
        v5 = (v5 & 3)
        if ((v5 & 3) == 0):
            break
        v2 = 0
        while True:  # $label48
            store32((v4 + ((v3 + v25) << 2)), load32((v21 + (v3 << 2))))
            v3 = (v3 + 1)
            v2 = (v2 + 1)
            if ((v2 + 1) != v5):
                continue
            break
        break
    while True:  # block $label49
        if (v10 == 0):
            break
        v1 = 0
        v5 = load32(9143004)
        v3 = 0
        if (u(v10) >= u(4)):
            v2 = (v10 & -4)
            v6 = 0
            while True:  # $label50
                store32((v4 + ((v3 + v24) << 2)), load8u((v3 + v5)))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v24) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v24) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v24) << 2)), load8u((v5 + v7)))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v10 & 3)
        if (v10 & 3):
            while True:  # $label51
                store32((v4 + ((v3 + v24) << 2)), load8u((v3 + v5)))
                v3 = (v3 + 1)
                v1 = (v1 + 1)
                if ((v1 + 1) != v2):
                    continue
                break
        if (v10 == 0):
            break
        v1 = 0
        v5 = load32(9143008)
        v3 = 0
        if (u(v10) >= u(4)):
            v2 = (v10 & -4)
            v6 = 0
            while True:  # $label52
                store32((v4 + ((v3 + v27) << 2)), load8u((v3 + v5)))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v27) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v27) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v27) << 2)), load8u((v5 + v7)))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v10 & 3)
        if (v10 & 3):
            while True:  # $label53
                store32((v4 + ((v3 + v27) << 2)), load8u((v3 + v5)))
                v3 = (v3 + 1)
                v1 = (v1 + 1)
                if ((v1 + 1) != v2):
                    continue
                break
        if (v10 == 0):
            break
        v1 = 0
        v5 = load32(9143012)
        v3 = 0
        if (u(v10) >= u(4)):
            v2 = (v10 & -4)
            v6 = 0
            while True:  # $label54
                store32((v4 + ((v3 + v28) << 2)), load8u((v3 + v5)))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v28) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v28) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v28) << 2)), load8u((v5 + v7)))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v10 & 3)
        if (v10 & 3):
            while True:  # $label55
                store32((v4 + ((v3 + v28) << 2)), load8u((v3 + v5)))
                v3 = (v3 + 1)
                v1 = (v1 + 1)
                if ((v1 + 1) != v2):
                    continue
                break
        if (v10 == 0):
            break
        v1 = 0
        v5 = load32(9143016)
        v3 = 0
        if (u(v10) >= u(4)):
            v2 = (v10 & -4)
            v6 = 0
            while True:  # $label56
                store32((v4 + ((v3 + v29) << 2)), load8u((v3 + v5)))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v29) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v29) << 2)), load8u((v5 + v7)))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v29) << 2)), load8u((v5 + v7)))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v10 & 3)
        if ((v10 & 3) == 0):
            break
        while True:  # $label57
            store32((v4 + ((v3 + v29) << 2)), load8u((v3 + v5)))
            v3 = (v3 + 1)
            v1 = (v1 + 1)
            if ((v1 + 1) != v2):
                continue
            break
        break
    while True:  # block $label58
        if (v26 == 0):
            break
        v1 = 0
        v5 = load32(9215884)
        v3 = 0
        if (u(v26) >= u(4)):
            v2 = (v26 & -4)
            v6 = 0
            while True:  # $label59
                store32((v4 + ((v3 + v30) << 2)), load32((v5 + (v3 << 2))))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v30) << 2)), load32((v5 + (v7 << 2))))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v30) << 2)), load32((v5 + (v7 << 2))))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v30) << 2)), load32((v5 + (v7 << 2))))
                v3 = (v3 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v2):
                    continue
                break
        v2 = (v26 & 3)
        if ((v26 & 3) == 0):
            break
        while True:  # $label60
            store32((v4 + ((v3 + v30) << 2)), load32((v5 + (v3 << 2))))
            v3 = (v3 + 1)
            v1 = (v1 + 1)
            if ((v1 + 1) != v2):
                continue
            break
        break
    v3 = 0
    while True:  # block $label61
        v2 = load32(9142912)
        if (load32(9142912) == 0):
            break
        v5 = load32(9142908)
        if (u(v2) >= u(4)):
            v6 = (v2 & -4)
            v1 = 0
            while True:  # $label62
                store32((v4 + ((v3 + v19) << 2)), load32((v5 + (v3 << 2))))
                v7 = (v3 | 1)
                store32((v4 + (((v3 | 1) + v19) << 2)), load32((v5 + (v7 << 2))))
                v7 = (v3 | 2)
                store32((v4 + (((v3 | 2) + v19) << 2)), load32((v5 + (v7 << 2))))
                v7 = (v3 | 3)
                store32((v4 + (((v3 | 3) + v19) << 2)), load32((v5 + (v7 << 2))))
                v3 = (v3 + 4)
                v1 = (v1 + 4)
                if ((v1 + 4) != v6):
                    continue
                break
        v2 = (v2 & 3)
        if ((v2 & 3) == 0):
            break
        v1 = 0
        while True:  # $label63
            store32((v4 + ((v3 + v19) << 2)), load32((v5 + (v3 << 2))))
            v3 = (v3 + 1)
            v1 = (v1 + 1)
            if ((v1 + 1) != v2):
                continue
            break
        break
    if load8u(9142917):
        store32(v21 + 48, 0)
    v6 = 0
    v7 = 0
    if load32(9142892):
        v3 = v9
        while True:  # $label78
            v9 = (v4 + ((v3 + v6) << 2))
            v1 = (load32(9561692) + (v7 * 286704))
            store32((v4 + ((v3 + v6) << 2)), load32((load32(9561692) + (v7 * 286704))))
            store32(v9 + 4, load32(v1 + 4))
            store32(v9 + 8, load32(v1 + 8))
            store32(v9 + 12, load32(v1 + 12))
            store32(v9 + 16, load32(v1 + 16))
            store32(v9 + 20, load32(v1 + 20))
            store32(v9 + 24, load32(v1 + 24))
            store32(v9 + 28, load32(v1 + 28))
            store32(v9 + 32, load32(v1 + 32))
            store32(v9 + 36, load32(v1 + 36))
            while True:  # block $label64
                v2 = load32(v1 + 281788)
                if (load32(v1 + 281788) == 0):
                    break
                store32(v9 + 40, load32(v12 + 28))
                v5 = load32(v2 + 8)
                v8 = load32(v12 + 28)
                store32(v12 + 28, (load32(v12 + 28) + 1))
                store32((v4 + (v8 << 2)), v5)
                if (load32(v2 + 8) == 0):
                    break
                v8 = load32(v2)
                v5 = 0
                while True:  # $label65
                    v10 = load32((v8 + (v5 << 2)))
                    v11 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v11 << 2)), v10)
                    v5 = (v5 + 1)
                    if (u((v5 + 1)) < u(load32(v2 + 8))):
                        continue
                    break
                break
            while True:  # block $label66
                v2 = load32(v1 + 281792)
                if (load32(v1 + 281792) == 0):
                    break
                store32(v9 + 44, load32(v12 + 28))
                v5 = load32(v2 + 8)
                v8 = load32(v12 + 28)
                store32(v12 + 28, (load32(v12 + 28) + 1))
                store32((v4 + (v8 << 2)), v5)
                if (load32(v2 + 8) == 0):
                    break
                v8 = load32(v2)
                v5 = 0
                while True:  # $label67
                    v10 = load32((v8 + (v5 << 2)))
                    v11 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v11 << 2)), v10)
                    v5 = (v5 + 1)
                    if (u((v5 + 1)) < u(load32(v2 + 8))):
                        continue
                    break
                break
            while True:  # block $label68
                v2 = load32(v1 + 281796)
                if (load32(v1 + 281796) == 0):
                    break
                store32(v9 + 48, load32(v12 + 28))
                v5 = load32(v2 + 8)
                v8 = load32(v12 + 28)
                store32(v12 + 28, (load32(v12 + 28) + 1))
                store32((v4 + (v8 << 2)), v5)
                if (load32(v2 + 8) == 0):
                    break
                v8 = load32(v2)
                v5 = 0
                while True:  # $label69
                    v10 = load32((v8 + (v5 << 2)))
                    v11 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v11 << 2)), v10)
                    v5 = (v5 + 1)
                    if (u((v5 + 1)) < u(load32(v2 + 8))):
                        continue
                    break
                break
            while True:  # block $label70
                v2 = load32(v1 + 286680)
                if (load32(v1 + 286680) == 0):
                    break
                store32(v9 + 52, load32(v12 + 28))
                v5 = load32(v2 + 8)
                v9 = load32(v12 + 28)
                store32(v12 + 28, (load32(v12 + 28) + 1))
                store32((v4 + (v9 << 2)), v5)
                if (load32(v2 + 8) == 0):
                    break
                v9 = load32(v2)
                v5 = 0
                while True:  # $label71
                    v8 = load32((v9 + (v5 << 2)))
                    v10 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v10 << 2)), v8)
                    v5 = (v5 + 1)
                    if (u((v5 + 1)) < u(load32(v2 + 8))):
                        continue
                    break
                break
            v5 = (v6 + 14)
            v6 = 0
            while True:  # $label72
                v9 = v5
                v5 = (v4 + ((v5 + v3) << 2))
                v2 = (v1 + (v6 * 36))
                store32((v4 + ((v5 + v3) << 2)), load32(((v1 + (v6 * 36)) + 269376)))
                store32(v5 + 4, load32((v2 + 269380)))
                store32(v5 + 8, load32((v2 + 269384)))
                store32(v5 + 12, load32((v2 + 269388)))
                store32(v5 + 16, load32((v2 + 269392)))
                store32(v5 + 20, load32((v2 + 269396)))
                store32(v5 + 24, load32((v2 + 269400)))
                store32(v5 + 28, load32((v2 + 269404)))
                store32(v5 + 32, load32((v2 + 269408)))
                v5 = (v9 + 9)
                v6 = (v6 + 1)
                if ((v6 + 1) != 255):
                    continue
                break
            v6 = (v3 + v5)
            v5 = 0
            while True:  # $label73
                v2 = (v1 + 281808)
                store32((v4 + ((v5 + v6) << 2)), load32(((v1 + 281808) + (v5 << 2))))
                v8 = (v5 + 1)
                store32((v4 + ((v6 + (v5 + 1)) << 2)), load32((v2 + (v8 << 2))))
                v8 = (v5 + 2)
                store32((v4 + ((v6 + (v5 + 2)) << 2)), load32((v2 + (v8 << 2))))
                v5 = (v5 + 3)
                if ((v5 + 3) != 255):
                    continue
                break
            v2 = (v6 + 255)
            v5 = 0
            while True:  # $label74
                v8 = (v1 + 282828)
                store32((v4 + ((v2 + v5) << 2)), load32(((v1 + 282828) + (v5 << 2))))
                v10 = (v5 + 1)
                store32((v4 + ((v2 + (v5 + 1)) << 2)), load32((v8 + (v10 << 2))))
                v10 = (v5 + 2)
                store32((v4 + ((v2 + (v5 + 2)) << 2)), load32((v8 + (v10 << 2))))
                v5 = (v5 + 3)
                if ((v5 + 3) != 255):
                    continue
                break
            v2 = ((v6 << 2) + v4)
            store32((((v6 << 2) + v4) + 2040), load32(v1 + 283848))
            store32((v2 + 2044), load32((v1 + 283852)))
            store32((v2 + 2048), load32((v1 + 283856)))
            store32((v2 + 2052), load32((v1 + 283860)))
            store32((v2 + 2056), load32(v1 + 283864))
            if load8u(9147152):
                func425(v1)
            v5 = 0
            if load32(9147132):
            else:
            store32(0, load32(v1 + 283872))
            if load32(9147132):
            else:
            store32(0, load32(v1 + 283876))
            store32((v2 + 2068), load32(v1 + 283960))
            store32((v2 + 2072), load32(v1 + 283968))
            store32((v2 + 2076), (load16u(v1 + 283972) | (load8u((v1 + 283974)) << 16)))
            v6 = (v6 + 520)
            while True:  # $label75
                v8 = (v1 + 283984)
                store32((v4 + ((v5 + v6) << 2)), load32(((v1 + 283984) + (v5 << 2))))
                v10 = (v5 | 1)
                store32((v4 + ((v6 + (v5 | 1)) << 2)), load32((v8 + (v10 << 2))))
                v10 = (v5 | 2)
                store32((v4 + ((v6 + (v5 | 2)) << 2)), load32((v8 + (v10 << 2))))
                v8 = (v5 | 3)
                if ((v5 | 3) != 155):
                    store32((v4 + ((v6 + v8) << 2)), load32(((v1 + (v8 << 2)) + 283984)))
                    v5 = (v5 + 4)
                    continue
                break
            store32((v2 + 2700), load32(v1 + 283868))
            store32((v2 + 2704), load32(v1 + 283912))
            store32((v2 + 2708), load32(v1 + 283916))
            store32((v2 + 2712), load32(v1 + 283920))
            store32((v2 + 2716), load32(v1 + 283964))
            store32((v2 + 2720), load32(v1 + 283904))
            store32((v2 + 2724), load32(v1 + 283880))
            store32((v2 + 2728), load32(v1 + 283940))
            store32((v2 + 2732), load32(v1 + 281804))
            store32((v2 + 2736), load32(v1 + 283924))
            store32((v2 + 2740), load32(v1 + 283936))
            store32((v2 + 2744), load32(v1 + 283948))
            store32((v2 + 2748), load32(v1 + 283956))
            store32((v2 + 2752), load32(v1 + 284616))
            store32((v2 + 2756), load8u(v1 + 286700))
            store32((v2 + 2760), load8u(v1 + 286701))
            store32((v2 + 2764), load8u(v1 + 286699))
            store32((v2 + 2768), load8u(v1 + 92))
            store32((v2 + 2772), load8u(v1 + 93))
            store32((v2 + 2776), load32(v1 + 283964))
            store32((v2 + 2780), load32(v1 + 283952))
            store32((v2 + 2784), load32(v1 + 80))
            store32((v2 + 2788), load32(v1 + 84))
            store32((v2 + 2792), load32(v1 + 88))
            while True:  # block $label76
                v6 = load32(v1 + 281800)
                if (load32(v1 + 281800) == 0):
                    break
                store32((v2 + 2796), load32(v12 + 28))
                v5 = 0
                if (load32(9142892) == 0):
                    break
                while True:  # $label77
                    v8 = load32((v6 + (v5 << 2)))
                    v10 = load32(v12 + 28)
                    store32(v12 + 28, (load32(v12 + 28) + 1))
                    store32((v4 + (v10 << 2)), v8)
                    v5 = (v5 + 1)
                    if (u((v5 + 1)) < u(load32(9142892))):
                        continue
                    break
                break
            store32((v2 + 2800), load32(v1 + 284608))
            store32((v2 + 2804), load32(v1 + 286684))
            store32((v2 + 2808), load8u(v1 + 286696))
            store32((v2 + 2812), load32(v1 + 283976))
            store32((v2 + 2816), load32(v1 + 283980))
            store32((v2 + 2820), load32(v1 + 286688))
            if load32(9147132):
            else:
            store32(0, load32(v1 + 283896))
            if load32(9147132):
            else:
            store32(0, load32(v1 + 283900))
            v6 = (v9 + 717)
            v7 = (v7 + 1)
            if (u((v7 + 1)) < u(load32(9142892))):
                continue
            break
    if (u(v36) >= u(4)):
        # TODO: i32.div_u []
        v9 = 33
        v26 = (33 << 5)
        v23 = (v9 * 31)
        v15 = (v9 * 30)
        v21 = (v9 * 29)
        v25 = (v9 * 28)
        v24 = (v9 * 27)
        v27 = (v9 * 26)
        v28 = (v9 * 25)
        v29 = (v9 * 24)
        v30 = (v9 * 23)
        v19 = (v9 * 22)
        v14 = (v9 * 21)
        v17 = (v9 * 20)
        v32 = (v9 * 19)
        v22 = (v9 * 18)
        v33 = (v9 * 17)
        v34 = (v9 << 4)
        v35 = (v9 * 15)
        v39 = (v9 * 14)
        v20 = (v9 * 13)
        v16 = (v9 * 12)
        v41 = (v9 * 11)
        v42 = (v9 * 10)
        v43 = (v9 * 9)
        v8 = 3
        v44 = (v9 << 3)
        v45 = (v9 * 7)
        v46 = (v9 * 6)
        v47 = (v9 * 5)
        v48 = (v9 << 2)
        v49 = (v9 * 3)
        v50 = (v9 << 1)
        v13 = load32(9147132)
        v51 = load32(38448)
        v52 = load32(9671128)
        v3 = load32(v12 + 28)
        v7 = 0
        v11 = 0
        while True:  # $label92
            while True:  # block $label79
                v5 = (v52 + (v8 * 132))
                v10 = load8u((v52 + (v8 * 132)) + 122)
                if (load8u((v52 + (v8 * 132)) + 122) == v51):
                    v1 = (v4 + ((v11 + v40) << 2))
                    store32((v4 + ((v11 + v40) << 2)), load32(v5 + 28))
                    store32(v1 + 4, load32(v5 + 64))
                    store32(v1 + 8, load8u(v5 + 124))
                    store32(v1 + 12, load32(v5 + 112))
                    v11 = (v11 + 4)
                    break
                while True:  # block $label80
                    v2 = load32(v5 + 16)
                    if (load32(v5 + 16) == 0):
                        break
                    store32((v4 + ((v7 + v31) << 2)), v3)
                    store32((v4 + (v3 << 2)), load32(v2 + 8))
                    v3 = (v3 + 1)
                    if (load32(v2 + 8) == 0):
                        break
                    v6 = load32(v2)
                    v1 = 0
                    while True:  # $label81
                        store32((v4 + (v3 << 2)), load32((v6 + (v1 << 2))))
                        v3 = (v3 + 1)
                        v1 = (v1 + 1)
                        if (u((v1 + 1)) < u(load32(v2 + 8))):
                            continue
                        break
                    break
                while True:  # block $label82
                    v2 = load32(v5 + 20)
                    if (load32(v5 + 20) == 0):
                        break
                    store32((v4 + (((v7 + v31) + v9) << 2)), v3)
                    store32((v4 + (v3 << 2)), load32(v2 + 8))
                    v3 = (v3 + 1)
                    if (load32(v2 + 8) == 0):
                        break
                    v6 = load32(v2)
                    v1 = 0
                    while True:  # $label83
                        store32((v4 + (v3 << 2)), load32((v6 + (v1 << 2))))
                        v3 = (v3 + 1)
                        v1 = (v1 + 1)
                        if (u((v1 + 1)) < u(load32(v2 + 8))):
                            continue
                        break
                    break
                while True:  # block $label84
                    v2 = load32(v5 + 24)
                    if (load32(v5 + 24) == 0):
                        break
                    v6 = load32(v2)
                    if (load32(v2) == 0):
                        break
                    store32((v4 + (((v7 + v31) + v50) << 2)), v3)
                    store32((v4 + (v3 << 2)), load32(v6 + 8))
                    v3 = (v3 + 1)
                    if (load32(v6 + 8) == 0):
                        break
                    v38 = load32(v6)
                    v1 = 0
                    while True:  # $label85
                        store32((v4 + (v3 << 2)), load32((v38 + (v1 << 2))))
                        v3 = (v3 + 1)
                        v1 = (v1 + 1)
                        if (u((v1 + 1)) < u(load32(v6 + 8))):
                            continue
                        break
                    break
                v1 = (v7 + v31)
                store32((v4 + (((v7 + v31) + v49) << 2)), load32(v5 + 28))
                store32((v4 + ((v1 + v48) << 2)), load32(v5 + 32))
                store32((v4 + ((v1 + v47) << 2)), load32(v5 + 36))
                store32((v4 + ((v1 + v46) << 2)), (0 if v13 else load32(v5 + 40)))
                store32((v4 + ((v1 + v45) << 2)), load32(v5 + 44))
                v6 = load32(v5 + 48)
                if load32(v5 + 48):
                    if v13:
                    else:
                    store32(0, load32(v6 + 32))
                store32((v4 + ((v1 + v43) << 2)), load32(v5 + 52))
                store32((v4 + ((v1 + v42) << 2)), load32(v5 + 60))
                store32((v4 + ((v1 + v41) << 2)), load32(v5 + 64))
                store32((v4 + ((v1 + v16) << 2)), load32(v5 + 68))
                store32((v4 + ((v1 + v20) << 2)), load32(v5 + 72))
                store32((v4 + ((v1 + v39) << 2)), load32(v5 + 76))
                store32((v4 + ((v1 + v35) << 2)), load32(v5 + 80))
                store32((v4 + ((v1 + v34) << 2)), load32(v5 + 84))
                store32((v4 + ((v1 + v33) << 2)), load32(v5 + 88))
                store32((v4 + ((v1 + v22) << 2)), (0 if v13 else load32(v5 + 92)))
                store32((v4 + ((v1 + v32) << 2)), load32(v5 + 108))
                store32((v4 + ((v1 + v17) << 2)), load32(v5 + 112))
                store32((v4 + ((v1 + v14) << 2)), load32(v5 + 116))
                store32((v4 + ((v1 + v19) << 2)), load16u(v5 + 120))
                store32((v4 + ((v1 + v30) << 2)), ((((load8u(v5 + 123) << 8) | (load8u(v5 + 124) << 16)) | (load8u(v5 + 125) << 24)) | v10))
                store32((v4 + ((v1 + v29) << 2)), load32(v5 + 126))
                store32((v4 + ((v1 + v28) << 2)), load32(v5 + 96))
                store32((v4 + ((v1 + v27) << 2)), load32(v5 + 56))
                while True:  # block $label86
                    if (v2 == 0):
                        break
                    while True:  # block $label87
                        v10 = load32(v2 + 12)
                        if (load32(v2 + 12) == 0):
                            break
                        store32((v4 + ((v1 + v24) << 2)), v3)
                        store32((v4 + (v3 << 2)), load32(v10 + 8))
                        v3 = (v3 + 1)
                        if (load32(v10 + 8) == 0):
                            break
                        v38 = load32(v10)
                        v6 = 0
                        while True:  # $label88
                            store32((v4 + (v3 << 2)), load32((v38 + (v6 << 2))))
                            v3 = (v3 + 1)
                            v6 = (v6 + 1)
                            if (u((v6 + 1)) < u(load32(v10 + 8))):
                                continue
                            break
                        break
                    while True:  # block $label89
                        v10 = load32(v2 + 8)
                        if (load32(v2 + 8) == 0):
                            break
                        store32((v4 + ((v1 + v25) << 2)), v3)
                        store32((v4 + (v3 << 2)), load32(v10 + 8))
                        v3 = (v3 + 1)
                        if (load32(v10 + 8) == 0):
                            break
                        v38 = load32(v10)
                        v6 = 0
                        while True:  # $label90
                            store32((v4 + (v3 << 2)), load32((v38 + (v6 << 2))))
                            v3 = (v3 + 1)
                            v6 = (v6 + 1)
                            if (u((v6 + 1)) < u(load32(v10 + 8))):
                                continue
                            break
                        break
                    v2 = load32(v2 + 4)
                    if (load32(v2 + 4) == 0):
                        break
                    store32((v4 + ((v1 + v21) << 2)), v3)
                    store32((v4 + (v3 << 2)), load32(v2 + 8))
                    v3 = (v3 + 1)
                    if (load32(v2 + 8) == 0):
                        break
                    v10 = load32(v2)
                    v6 = 0
                    while True:  # $label91
                        store32((v4 + (v3 << 2)), load32((v10 + (v6 << 2))))
                        v3 = (v3 + 1)
                        v6 = (v6 + 1)
                        if (u((v6 + 1)) < u(load32(v2 + 8))):
                            continue
                        break
                    break
                store32((v4 + ((v1 + v15) << 2)), load32(v5 + 100))
                store32((v4 + ((v1 + v23) << 2)), load32(v5 + 104))
                store32((v4 + ((v1 + v26) << 2)), load8u(v5 + 130))
                v7 = (v7 + 1)
                break
            v8 = (v8 + 1)
            if ((v8 + 1) != v36):
                continue
            break
    v5 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    v5 = func26(v37)
    store32(9687204, func26(v37))
    store32(v5, v18)
    store32(v12 + 24, v37)
    store32(9147396, v18)
    v5 = (load32(v12 + 24) + 4)
    store32(9147392, (load32(v12 + 24) + 4))
    store32(v12 + 24, v5)
    v9 = load32(9687204)
    while True:  # block $label93
        if (arg0 == 0):
            v5 = v9
            break
        v5 = 0
        v3 = 0
        arg0 = load32(v12 + 24)
        if load32(v12 + 24):
            v1 = -1
            while True:  # $label94
                v4 = (v1 ^ load8u((v3 + v9)))
                v1 = (((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1)
                v4 = (((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v4 = (((((((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v1 = (((((((((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1)
                v1 = (((((((((((((((((((((((((((((((((v1 ^ load8u((v3 + v9))) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1) & 0xFFFFFFFF) >> 1) ^ -306674912) if (v4 & 1) else v1)
                v3 = (v3 + 1)
                if ((v3 + 1) != arg0):
                    continue
                break
            v3 = (v1 ^ -1)
        store32(v12, v9)
        store32(v12 + 4, arg0)
        store32(v12 + 8, v3)
        # TODO: i32.div_u []
        store32(load32(9142848) + 12, 10)
        break
    G.global0 = (v12 + 32)
    return v5

# ------------------------------------------------------------
# $qc
# Export: qc
# ------------------------------------------------------------
def qc(arg0, arg1):
    """Exported as qc."""
    if (load32(51776) == 0):
        store8(9215872, 1)
        while True:  # block $label0
            v2 = load32(9216016)
            if (load32(9216016) != load32(9216012)):
                v3 = load32(9216008)
                break
            v3 = (load32(9216020) + v2)
            store32(9216012, (load32(9216020) + v2))
            v4 = load32(9216008)
            v3 = func26((-1 if (u(v3) > u(1073741823)) else (v3 << 2)))
            if v2:
                # TODO: memory.copy []
            if v4:
                v2 = load32(9216016)
            store32(9216008, v3)
            break
        store32(9216016, (v2 + 1))
        store32((v3 + (v2 << 2)), arg0)
        while True:  # block $label1
            arg0 = load32(9216016)
            if (load32(9216016) != load32(9216012)):
                v2 = v3
                break
            v2 = (load32(9216020) + arg0)
            store32(9216012, (load32(9216020) + arg0))
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy []
            store32(9216008, v2)
            arg0 = load32(9216016)
            break
        store32(9216016, (arg0 + 1))
        store32((v2 + (arg0 << 2)), arg1)
        return
    while True:  # block $label2
        if arg1:
            arg1 = (arg0 + 9686896)
            if load8u((arg0 + 9686896)):
                break
            store8(arg1, 1)
            arg1 = load32(((arg0 << 2) + 9685872))
            if (load32(((arg0 << 2) + 9685872)) == 0):
                break
            # call_indirect[arg1]
            return
        store8((arg0 + 9686896), 0)
        arg1 = load32(((arg0 << 2) + 9685872))
        if (load32(((arg0 << 2) + 9685872)) == 0):
            break
        # call_indirect[arg1]
        break

# ------------------------------------------------------------
# $func343
# ------------------------------------------------------------
def func343():
    while True:  # block $label0
        v0 = load32(9142440)
        # TODO: f64.convert_i32_u []
        # TODO: f32.demote_f64 []
        # TODO: f32.convert_i32_u []
        v9 = (((((load32(9142440) * v0) * 1.52587890625e-05) * (load32(load32(9142424) + 60) * 160)) / 40.0) + 0.5)
        if (((((((load32(9142440) * v0) * 1.52587890625e-05) * (load32(load32(9142424) + 60) * 160)) / 40.0) + 0.5) < 4294967300.0) & (v9 >= 0.0)):
            # TODO: i32.trunc_f32_u []
            break
        break
    v7 = 0
    if 0:
        while True:  # $label3
            v2 = load32(9142440)
            while True:  # block $label2
                v8 = load32(load32(9142424) + 64)
                if load32(load32(9142424) + 64):
                    v3 = load32(9147312)
                    v0 = load32(9147324)
                    v0 = ((load32(9147324) << 11) ^ v0)
                    v1 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v0)
                    v4 = ((v2 & 0xFFFFFFFF) >> 1)
                    v9 = float(((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v0) % (((v2 & 0xFFFFFFFF) >> 1) - 20)))
                    v5 = load32(9147320)
                    v2 = load32(9147316)
                    while True:  # block $label1
                        v0 = load32(9142416)
                        if (load32(9142416) == 0):
                            v0 = (load32(41092) if load8u(9147210) else (load32(9142892) - 1))
                        # TODO: f32.convert_i32_u []
                        v0 = ((v5 << 11) ^ v5)
                        v0 = (((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1)
                        v10 = (((6.28318548 / (4 if (u(v0) < u(3)) else (v0 << (v0 & 1)))) * float(((((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1) % 100000))) / 100000.0)
                        # TODO: f64.promote_f32 []
                        # TODO: f64.convert_i32_u []
                        v11 = v4
                        v12 = (((func48((((6.28318548 / (4 if (u(v0) < u(3)) else (v0 << (v0 & 1)))) * float(((((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1) % 100000))) / 100000.0)) * v9) + 0.5) + v4)
                        if (abs((((func48((((6.28318548 / (4 if (u(v0) < u(3)) else (v0 << (v0 & 1)))) * float(((((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1) % 100000))) / 100000.0)) * v9) + 0.5) + v4)) < 2147483648.0):
                            break
                        break
                    v5 = -2147483648
                    # TODO: f64.promote_f32 []
                    v11 = (((func49(v10) * v9) + 0.5) + v11)
                    if (abs((((func49(v10) * v9) + 0.5) + v11)) < 2147483648.0):
                        v4 = int(v11)
                        break
                    v4 = -2147483648
                    break
                v0 = load32(9147320)
                v0 = ((load32(9147320) << 11) ^ v0)
                v3 = load32(9147312)
                v1 = load32(9147324)
                v1 = ((load32(9147324) << 11) ^ v1)
                v1 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v1) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v1)
                v0 = (((((((load32(9147320) << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ (((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v1) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v1) & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1)
                v5 = ((((((((load32(9147320) << 11) ^ v0) & 0xFFFFFFFF) >> 8) ^ (((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v1) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v1) & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1) % v2)
                v4 = (v1 % v2)
                v2 = load32(9147316)
                break
            store32(9147320, v0)
            store32(9147324, v1)
            v0 = ((v2 << 11) ^ v2)
            v0 = ((v0 ^ (((v0 & 0xFFFFFFFF) >> 19) ^ ((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8))) ^ v0)
            store32(9147316, ((v0 ^ (((v0 & 0xFFFFFFFF) >> 19) ^ ((((v2 << 11) ^ v2) & 0xFFFFFFFF) >> 8))) ^ v0))
            v1 = ((v3 << 11) ^ v3)
            v1 = (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v0 & 0xFFFFFFFF) >> 19)) ^ v1) ^ v0)
            store32(9147312, (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v0 & 0xFFFFFFFF) >> 19)) ^ v1) ^ v0))
            v6 = (v6 + 1)
            if ((v6 + 1) != v7):
                continue
            break
    return func126(v4, v5, ((v0 % 25) + 10), ((v1 % 25) + 10), (v8 != 0))

# ------------------------------------------------------------
# $func344
# ------------------------------------------------------------
def func344():
    v0 = load32(9561704)
    store32(9561716, load32(9561704))
    while True:  # block $label0
        if (load32(9561700) != v0):
            v1 = load32(9561696)
            break
        v1 = (load32(9561708) + v0)
        store32(9561700, (load32(9561708) + v0))
        v2 = load32(9561696)
        v1 = func26((-1 if (u(v1) > u(1073741823)) else (v1 << 2)))
        if v0:
            # TODO: memory.copy []
        if v2:
            v0 = load32(9561704)
        store32(9561696, v1)
        break
    store32(9561704, (v0 + 1))
    store32((v1 + (v0 << 2)), 0)
    v3 = (load32(9142848) + 10)
    store32(9561712, (load32(9142848) + 10))
    while True:  # block $label1
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
    store32((v2 + (v0 << 2)), v3)
    while True:  # block $label2
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
    store32((v1 + (v0 << 2)), 3)

# ------------------------------------------------------------
# $func346
# ------------------------------------------------------------
def func346():
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        if (load8u(9216060) == 0):
            break
        if (load32(9142872) == 0):
            break
        if load8u(9142917):
            break
        while True:  # block $label1
            if (u(load32(9142892)) < u(2)):
                break
            v4 = load32(9561692)
            v2 = 1
            while True:  # $label4
                v5 = (v4 + (v2 * 286704))
                store32((v4 + (v2 * 286704)) + 283944, 1)
                v3 = load32(9142892)
                if (u(load32(9142892)) > u(1)):
                    v8 = (v5 + 283944)
                    v7 = 1
                    v0 = 1
                    while True:  # $label3
                        while True:  # block $label2
                            if (v0 == v2):
                                break
                            v6 = (v4 + (v0 * 286704))
                            if (load32((v4 + (v0 * 286704)) + 284616) == 0):
                                break
                            v6 = func88(v6)
                            v9 = func88(v5)
                            if (u(func88(v6)) <= u(func88(v5))):
                                if (v6 != v9):
                                    break
                                if (u(v0) <= u(v2)):
                                    break
                            v7 = (v7 + 1)
                            store32(v8, (v7 + 1))
                            v3 = load32(9142892)
                            break
                        v0 = (v0 + 1)
                        if (u((v0 + 1)) < u(v3)):
                            continue
                        break
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(v3)):
                    continue
                break
            if (u(v3) < u(2)):
                break
            v4 = load32(9561692)
            v2 = 1
            while True:  # $label5
                v0 = (v4 + (v2 * 286704))
                v5 = load32((v4 + (v2 * 286704)) + 284616)
                if load32((v4 + (v2 * 286704)) + 284616):
                    v4 = func88(v0)
                    v7 = load8u(v0 + 283972)
                    v8 = load32(v0 + 283944)
                    v3 = load32(v0 + 283908)
                    v6 = load8u((v0 + 283974))
                    store32(v1 + 16, load8u((v0 + 283973)))
                    store32(v1 + 20, v6)
                    store32(v1 + 24, v5)
                    store32(v1 + 28, v3)
                    v5 = load32(9142872)
                    store32(v1 + 32, ((load32(9142872) != 0) & (v3 == v5)))
                    store32(v1, v4)
                    store32(v1 + 4, v8)
                    store32(v1 + 8, v0)
                    store32(v1 + 12, v7)
                    a_b()
                    v4 = load32(9561692)
                    v3 = load32(9142892)
                v2 = (v2 + 1)
                if (u((v2 + 1)) < u(v3)):
                    continue
                break
            break
        a_b()
        break
    G.global0 = (v1 + 48)

# ------------------------------------------------------------
# $func347
# ------------------------------------------------------------
def func347(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    store32(59204, arg3)
    store32(59200, arg2)
    arg2 = 0
    v12 = 2
    while True:  # block $label1
        while True:  # $label3
            arg3 = arg2
            arg2 = (arg2 + 2)
            arg3 = (arg3 << 2)
            v13 = load32(((arg3 << 2) + 59200))
            v14 = load32(((arg3 | 4) + 59200))
            arg3 = 0
            while True:  # $label2
                while True:  # block $label0
                    v10 = (arg3 << 2)
                    v11 = (load32(((arg3 << 2) + 9072)) + v13)
                    v9 = ((load32(((arg3 << 2) + 9072)) + v13) - arg4)
                    v10 = (load32((v10 + 9104)) + v14)
                    v9 = ((load32((v10 + 9104)) + v14) - arg5)
                    if ((((((load32(((arg3 << 2) + 9072)) + v13) - arg4) * v9) + (((load32((v10 + 9104)) + v14) - arg5) * v9)) - 1) > 1600):
                        break
                    v9 = load32(9142440)
                    if (u(load32(9142440)) <= u(v10)):
                        break
                    if ((v10 | v11) < 0):
                        break
                    if (u(v9) <= u(v11)):
                        break
                    if (load16u((load32(9142436) + (((v9 * v10) + v11) << 1))) == arg8):
                        break
                    v9 = (v9 + 2)
                    v9 = load32((load32(9142840) + ((v11 + (((v10 + ((v9 + 2) * load32(arg7 + 208))) + 1) * v9)) << 2)) + 4)
                    if (u(load32((load32(9142840) + ((v11 + (((v10 + ((v9 + 2) * load32(arg7 + 208))) + 1) * v9)) << 2)) + 4)) <= u(2)):
                        if (load32(arg7 + 212) != v9):
                            break
                    if (u(v9) >= u(3)):
                        if func205((load32(9671128) + (v9 * 132)), load16u(arg6 + 110)):
                            break
                    if func56(v11, v10, arg7, load16u(arg6 + 110), 0, 0, 1, 1, 0):
                        break
                    store16((load32(9142436) + (((load32(9142440) * v10) + v11) << 1)), arg8)
                    v9 = ((v12 << 2) + 59200)
                    store32(((v12 << 2) + 59200) + 4, v10)
                    store32(v9, v11)
                    v12 = (v12 + 2)
                    break
                arg3 = (arg3 + 1)
                if ((arg3 + 1) != 8):
                    continue
                break
            if (u(arg2) < u(v12)):
                continue
            break
        return 0
        break
    store32(arg0, v11)
    store32(arg1, v10)
    return 1

# ------------------------------------------------------------
# $ve
# Export: ve
# ------------------------------------------------------------
def ve(arg0):
    """Exported as ve."""
    v10 = load32(arg0 + 32)
    v4 = load32(arg0 + 12)
    store32(9140308, 0)
    v2 = (v4 + 16)
    v3 = load32(v4)
    while True:  # block $label37
        while True:  # block $label8
            v6 = load32(v4 + 12)
            if load32(v4 + 12):
                v1 = load32(v4 + 8)
                store32(9147292, load32(v4 + 4))
                store32(9147296, v1)
                v7 = load32(9687256)
                store32(9687256, arg0)
                store32(9140324, 0)
                if v3:
                    v9 = (v3 & 1)
                    while True:  # block $label0
                        if (v3 == 1):
                            arg0 = 0
                            break
                        v8 = (v3 & -2)
                        arg0 = 0
                        v1 = 0
                        while True:  # $label5
                            while True:  # block $label2
                                while True:  # block $label1
                                    v11 = ((v5 * 60) + v2)
                                    # br_table[(load32(((v5 * 60) + v2) + 32) - 23)]
                                    break
                                    break
                                arg0 = (arg0 + 1)
                                store32(9140324, (arg0 + 1))
                                break
                            while True:  # block $label4
                                while True:  # block $label3
                                    # br_table[(load32(v11 + 92) - 23)]
                                    break
                                    break
                                arg0 = (arg0 + 1)
                                store32(9140324, (arg0 + 1))
                                break
                            v5 = (v5 + 2)
                            v1 = (v1 + 2)
                            if ((v1 + 2) != v8):
                                continue
                            break
                        break
                    v1 = ((v5 * 15) + 8)
                    while True:  # block $label6
                        if (v9 == 0):
                            break
                        while True:  # block $label7
                            # br_table[(load32((v2 + (v1 << 2))) - 23)]
                            break
                            break
                        arg0 = (arg0 + 1)
                        store32(9140324, (arg0 + 1))
                        break
                else:
                store32((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)), func26(0))
                store32(9684504, (v4 + v6))
                store32(9684500, v2)
                store32(9687244, v3)
                store32(9147300, (((v10 - v6) & 0xFFFFFFFF) >> 2))
                store32(9140324, 0)
                if (v7 == 0):
                    break
                while True:  # block $label9
                    if (v3 == 0):
                        break
                    arg0 = 0
                    if (v3 != 1):
                        v5 = (v3 & -2)
                        v1 = 0
                        while True:  # $label12
                            while True:  # block $label10
                                v4 = (v2 + (arg0 * 60))
                                v10 = load32((v2 + (arg0 * 60)) + 28)
                                if (u(load32((v2 + (arg0 * 60)) + 28)) > u(9999)):
                                    break
                                v9 = load32(v4 + 32)
                                if (u(load32(v4 + 32)) > u(22)):
                                    break
                                if (((1 << v9) & 4194400) == 0):
                                    break
                                store32(((v10 * 404) + 9568096) + 20, 0)
                                break
                            while True:  # block $label11
                                v10 = load32(v4 + 88)
                                if (u(load32(v4 + 88)) > u(9999)):
                                    break
                                v4 = load32(v4 + 92)
                                if (u(load32(v4 + 92)) > u(22)):
                                    break
                                if (((1 << v4) & 4194400) == 0):
                                    break
                                store32(((v10 * 404) + 9568096) + 20, 0)
                                break
                            arg0 = (arg0 + 2)
                            v1 = (v1 + 2)
                            if ((v1 + 2) != v5):
                                continue
                            break
                        arg0 = (arg0 * 15)
                    if ((v3 & 1) == 0):
                        break
                    arg0 = (v2 + (arg0 << 2))
                    v1 = load32((v2 + (arg0 << 2)) + 28)
                    if (u(load32((v2 + (arg0 << 2)) + 28)) > u(9999)):
                        break
                    arg0 = load32(arg0 + 32)
                    if (u(load32(arg0 + 32)) > u(22)):
                        break
                    if (((1 << arg0) & 4194400) == 0):
                        break
                    store32(((v1 * 404) + 9568096) + 20, 0)
                    break
                v4 = 1
                while True:  # block $label13
                    if load8u(59182):
                        break
                    v2 = load32(9671136)
                    if (u(load32(9671136)) < u(4)):
                        break
                    v5 = load32(9671128)
                    arg0 = 3
                    while True:  # $label36
                        while True:  # block $label14
                            v3 = (v5 + (arg0 * 132))
                            if (load8u((v5 + (arg0 * 132)) + 125) == 3):
                                break
                            v10 = load32(v3 + 48)
                            if (load32(v3 + 48) == 0):
                                break
                            v1 = load8u(v3 + 122)
                            while True:  # block $label35
                                while True:  # block $label34
                                    while True:  # block $label33
                                        while True:  # block $label32
                                            while True:  # block $label31
                                                while True:  # block $label30
                                                    while True:  # block $label29
                                                        while True:  # block $label28
                                                            while True:  # block $label27
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
                                                                                                                # br_table[load32(v10 + 32)]
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
                                    break
                                break
                            store32(((v1 * 72) + 9263872) + 48, load32(((v1 * 72) + 9263880)))
                            break
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != v2):
                            continue
                        break
                    break
                func383(((v1 * 72) + 9263924), v7)
                break
            store32(9687248, v3)
            store32(9684496, v2)
            break
        v4 = 0
        break
    v3 = load32(9142524)
    v2 = load32(9142532)
    arg0 = 0
    while True:  # $label44
        while True:  # block $label38
            v5 = ((arg0 * 404) + 9568096)
            if (load32(((arg0 * 404) + 9568096) + 264) != 2):
                break
            v1 = v2
            while True:  # block $label39
                while True:  # block $label40
                    # br_table[load32(v5 + 268)]
                    break
                    break
                v1 = v3
                break
            store32(((arg0 * 72) + 9263856), v1)
            break
        v5 = (arg0 | 1)
        if ((arg0 | 1) != 255):
            while True:  # block $label41
                v7 = ((v5 * 404) + 9568096)
                if (load32(((v5 * 404) + 9568096) + 264) != 2):
                    break
                v1 = v2
                while True:  # block $label42
                    while True:  # block $label43
                        # br_table[load32(v7 + 268)]
                        break
                        break
                    v1 = v3
                    break
                store32(((v5 * 72) + 9263856), v1)
                break
            arg0 = (arg0 + 2)
            continue
        break
    if (((v6 == 0) | v4) == 0):
        if load8u(9687269):
            v3 = 3
            if (u(load32(9671136)) > u(3)):
                while True:  # $label50
                    arg0 = (load32(9671128) + (v3 * 132))
                    func157((load32(9671128) + (v3 * 132)))
                    v1 = load32(arg0 + 20)
                    if load32(arg0 + 20):
                        store32(v1 + 8, 0)
                    store32(arg0 + 44, 0)
                    if (load8u(arg0 + 125) != 4):
                        store8(arg0 + 125, 0)
                    store8(arg0 + 123, 0)
                    store16(arg0 + 108, 0)
                    store32(arg0 + 88, 0)
                    store32(arg0 + 96, 0)
                    while True:  # block $label45
                        if (load8u(arg0 + 126) != 1):
                            break
                        v1 = (load32(9671128) + (load32(arg0 + 28) * 132))
                        store8((load32(9671128) + (load32(arg0 + 28) * 132)) + 126, 0)
                        # TODO: i32.div_u []
                        store32(load32(v1 + 52) + 52, ((load32(((load8u(v1 + 122) * 404) + 9568096) + 296) * load32(((load32(9561692) + (load16u(v1 + 110) * 286704)) + 284144))) - 100))
                        if (load32(v1 + 92) == 0):
                            break
                        if load32(9140316):
                            if (load32(9140320) != load32(v1 + 28)):
                                break
                        break
                    store64(arg0 + 100, 0)
                    store32(arg0 + 56, 0)
                    store16(arg0 + 127, 0)
                    store32(arg0 + 32, -1)
                    if (load8u(arg0 + 129) != 8):
                        store8(arg0 + 129, 0)
                    while True:  # block $label46
                        if (load32(9147132) == 0):
                            break
                        if (load32(38788) != load8u(arg0 + 122)):
                            break
                        store32(arg0 + 84, (load32(arg0 + 84) + 1))
                        break
                    while True:  # block $label49
                        while True:  # block $label47
                            while True:  # block $label48
                                # br_table[(load8u(arg0 + 125) - 4)]
                                break
                                break
                            v1 = load16u(arg0 + 110)
                            v2 = load8u(arg0 + 122)
                            v4 = load32(9561692)
                            break
                            break
                        v4 = load32(9561692)
                        v1 = load16u(arg0 + 110)
                        v2 = load8u(arg0 + 122)
                        arg0 = (((load32(9561692) + (load16u(arg0 + 110) * 286704)) + (load8u(arg0 + 122) << 2)) + 282828)
                        store32((((load32(9561692) + (load16u(arg0 + 110) * 286704)) + (load8u(arg0 + 122) << 2)) + 282828), (load32(arg0) + 1))
                        break
                    arg0 = (v4 + (v1 * 286704))
                    v2 = load32(((v2 * 404) + 9568096) + 280)
                    v1 = (load32(((v2 * 404) + 9568096) + 280) + load32(arg0 + 283976))
                    store32((v4 + (v1 * 286704)) + 283976, (load32(((v2 * 404) + 9568096) + 280) + load32(arg0 + 283976)))
                    if (v2 < 0):
                        store8(arg0 + 286700, 1)
                    arg0 = (arg0 + 281748)
                    if (u(v1) > u(load32((arg0 + 281748)))):
                        store32(arg0, v1)
                    v3 = (v3 + 1)
                    if (u((v3 + 1)) < u(load32(9671136))):
                        continue
                    break
        store8(9687268, 1)
        v2 = 0
        v10 = 0
        v13 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        while True:  # $label83
            v5 = ((v10 * 404) + 9568096)
            v17 = load32(((v10 * 404) + 9568096) + 224)
            arg0 = load32(v5 + 200)
            v18 = (load32(v5 + 200) if (u(arg0) > u(v2)) else v2)
            v19 = (load32(((v10 * 404) + 9568096) + 224) > (load32(v5 + 200) if (u(arg0) > u(v2)) else v2))
            v20 = load32(v5 + 216)
            if load32(v5 + 216):
                v21 = load32(v5 + 220)
                v4 = 0
                while True:  # block $label51
                    v1 = load32(v5 + 216)
                    v22 = (load32(v5 + 216) + 2)
                    if ((load32(v5 + 216) + 2) <= 0):
                        break
                    v3 = load32(v5 + 220)
                    v11 = (load32(v5 + 220) + 2)
                    if ((load32(v5 + 220) + 2) <= 0):
                        break
                    v2 = load32(v5 + 372)
                    v23 = ((v1 != 0) & (v3 != 0))
                    while True:  # $label73
                        while True:  # block $label57
                            while True:  # block $label53
                                while True:  # block $label52
                                    if (v4 == 0):
                                        if (v23 == 0):
                                            break
                                        if (load8u(v2) == 0):
                                            break
                                        v4 = 0
                                        arg0 = 0
                                        break
                                    while True:  # block $label54
                                        v12 = (v4 - 1)
                                        v14 = (u((v4 - 1)) >= u(v1))
                                        if (u((v4 - 1)) >= u(v1)):
                                            break
                                        if (v3 == 0):
                                            break
                                        if (load8u((v2 + v12)) == 0):
                                            break
                                        arg0 = 0
                                        break
                                        break
                                    v6 = (v4 - 2)
                                    while True:  # block $label55
                                        v24 = (v4 == 1)
                                        if (v4 == 1):
                                            break
                                        if (u(v1) <= u(v6)):
                                            break
                                        if (v3 == 0):
                                            break
                                        if (load8u((v2 + v6)) == 0):
                                            break
                                        arg0 = 0
                                        break
                                        break
                                    while True:  # block $label56
                                        v15 = (u(v1) <= u(v4))
                                        if (u(v1) <= u(v4)):
                                            break
                                        if (v3 == 0):
                                            break
                                        if (load8u((v2 + v4)) == 0):
                                            break
                                        arg0 = 0
                                        break
                                        break
                                    arg0 = 1
                                    if (v11 == 1):
                                        break
                                    while True:  # $label67
                                        v9 = (arg0 - 1)
                                        while True:  # block $label59
                                            while True:  # block $label58
                                                if v14:
                                                    break
                                                if (u(v3) <= u(v9)):
                                                    break
                                                if load8u((v2 + ((v1 * v9) + v12))):
                                                    break
                                                break
                                            while True:  # block $label60
                                                if v15:
                                                    break
                                                if (u(v3) <= u(v9)):
                                                    break
                                                if load8u((v2 + ((v1 * v9) + v4))):
                                                    break
                                                break
                                            v8 = (arg0 - 2)
                                            while True:  # block $label61
                                                v16 = (u(arg0) < u(2))
                                                if (u(arg0) < u(2)):
                                                    break
                                                if v14:
                                                    break
                                                if (u(v3) <= u(v8)):
                                                    break
                                                if load8u((v2 + ((v1 * v8) + v12))):
                                                    break
                                                break
                                            v7 = 0
                                            while True:  # block $label62
                                                if v24:
                                                    break
                                                v7 = 1
                                                if (u(v1) <= u(v6)):
                                                    break
                                                if (u(v3) <= u(v9)):
                                                    break
                                                if load8u((v2 + ((v1 * v9) + v6))):
                                                    break
                                                break
                                            while True:  # block $label63
                                                if v14:
                                                    break
                                                if (u(arg0) >= u(v3)):
                                                    break
                                                if load8u((v2 + ((arg0 * v1) + v12))):
                                                    break
                                                break
                                            while True:  # block $label64
                                                if v16:
                                                    break
                                                while True:  # block $label65
                                                    if v15:
                                                        break
                                                    if (u(v3) <= u(v8)):
                                                        break
                                                    if load8u((v2 + ((v1 * v8) + v4))):
                                                        break
                                                    break
                                                if ((v7 == 0) | v16):
                                                    break
                                                if (u(v1) <= u(v6)):
                                                    break
                                                if (u(v3) <= u(v8)):
                                                    break
                                                if load8u((v2 + ((v1 * v8) + v6))):
                                                    break
                                                break
                                            while True:  # block $label66
                                                if (v7 == 0):
                                                    break
                                                if (u(v1) <= u(v6)):
                                                    break
                                                if (u(arg0) >= u(v3)):
                                                    break
                                                if load8u((v2 + ((arg0 * v1) + v6))):
                                                    break
                                                break
                                            if v15:
                                                break
                                            if (u(arg0) >= u(v3)):
                                                break
                                            if load8u((v2 + ((arg0 * v1) + v4))):
                                                break
                                            break
                                        arg0 = (arg0 + 1)
                                        if ((arg0 + 1) != v11):
                                            continue
                                        break
                                    break
                                    break
                                arg0 = 1
                                if (v11 == 1):
                                    break
                                while True:  # $label72
                                    while True:  # block $label71
                                        while True:  # block $label69
                                            while True:  # block $label68
                                                if (v1 == 0):
                                                    break
                                                v6 = (arg0 - 1)
                                                if (u((arg0 - 1)) >= u(v3)):
                                                    break
                                                if load8u((v2 + (v1 * v6))):
                                                    break
                                                break
                                            while True:  # block $label70
                                                if (u(arg0) < u(2)):
                                                    break
                                                if (v1 == 0):
                                                    break
                                                v6 = (arg0 - 2)
                                                if (u((arg0 - 2)) >= u(v3)):
                                                    break
                                                if load8u((v2 + (v1 * v6))):
                                                    break
                                                break
                                            if (v1 == 0):
                                                break
                                            if (u(arg0) >= u(v3)):
                                                break
                                            if (load8u((v2 + (arg0 * v1))) == 0):
                                                break
                                            break
                                        v4 = 0
                                        break
                                        break
                                    arg0 = (arg0 + 1)
                                    if (v11 != (arg0 + 1)):
                                        continue
                                    break
                                break
                                break
                            store32(v13 + 12, v4)
                            store32(v13 + 8, arg0)
                            break
                            break
                        v4 = (v4 + 1)
                        if ((v4 + 1) != v22):
                            continue
                        break
                    break
                v11 = (v21 + 2)
                v7 = (v20 + 2)
                arg0 = ((v21 + 2) * (v20 + 2))
                v9 = func26((-1 if (arg0 & 1610612736) else (((v21 + 2) * (v20 + 2)) << 3)))
                store32(v5 + 56, func26((-1 if (arg0 & 1610612736) else (((v21 + 2) * (v20 + 2)) << 3))))
                v1 = load32(v13 + 12)
                store32(v9, load32(v13 + 12))
                v3 = load32(v13 + 8)
                store32(v9 + 4, load32(v13 + 8))
                if arg0:
                    # TODO: memory.fill []
                v6 = 2
                store32(((((v3 * v7) + v1) << 2) + 59200), 1)
                v1 = 0
                while True:  # $label82
                    v4 = v1
                    v1 = (v1 << 2)
                    arg0 = load32((v9 + (v1 << 2)))
                    v2 = load32((v9 + (v1 | 4)))
                    v3 = (arg0 + 1)
                    v8 = ((((load32((v9 + (v1 << 2))) > -2) & (load32((v9 + (v1 | 4))) >= 0)) & ((arg0 + 1) < v7)) & (v2 < v11))
                    v1 = (v4 + 2)
                    while True:  # block $label77
                        while True:  # block $label78
                            if v4:
                                while True:  # block $label74
                                    if (v8 == 0):
                                        break
                                    v4 = ((((v2 * v7) + v3) << 2) + 59200)
                                    if load32(((((v2 * v7) + v3) << 2) + 59200)):
                                        break
                                    if (func93(v3, v2, v5) == 0):
                                        break
                                    v8 = (v9 + (v6 << 2))
                                    store32((v9 + (v6 << 2)), v3)
                                    store32(v8 + 4, v2)
                                    store32(v4, 1)
                                    v6 = (v6 + 2)
                                    break
                                while True:  # block $label75
                                    v4 = (arg0 < 0)
                                    if (arg0 < 0):
                                        break
                                    if (v2 <= 0):
                                        break
                                    if (arg0 >= v7):
                                        break
                                    if (v2 > v11):
                                        break
                                    v3 = (v2 - 1)
                                    v8 = (((((v2 - 1) * v7) + arg0) << 2) + 59200)
                                    if load32((((((v2 - 1) * v7) + arg0) << 2) + 59200)):
                                        break
                                    if (func93(arg0, v3, v5) == 0):
                                        break
                                    v12 = (v9 + (v6 << 2))
                                    store32((v9 + (v6 << 2)), arg0)
                                    store32(v12 + 4, v3)
                                    store32(v8, 1)
                                    v6 = (v6 + 2)
                                    break
                                while True:  # block $label76
                                    if (arg0 <= 0):
                                        break
                                    if (v2 < 0):
                                        break
                                    if (arg0 > v7):
                                        break
                                    if (v2 >= v11):
                                        break
                                    v3 = (arg0 - 1)
                                    v8 = ((((arg0 - 1) + (v2 * v7)) << 2) + 59200)
                                    if load32(((((arg0 - 1) + (v2 * v7)) << 2) + 59200)):
                                        break
                                    if (func93(v3, v2, v5) == 0):
                                        break
                                    v12 = (v9 + (v6 << 2))
                                    store32((v9 + (v6 << 2)), v3)
                                    store32(v12 + 4, v2)
                                    store32(v8, 1)
                                    v6 = (v6 + 2)
                                    break
                                if v4:
                                    break
                                if (v2 < -1):
                                    break
                                if (arg0 >= v7):
                                    break
                                v2 = (v2 + 1)
                                if ((v2 + 1) >= v11):
                                    break
                                v8 = ((((v2 * v7) + arg0) << 2) + 59200)
                                if load32(((((v2 * v7) + arg0) << 2) + 59200)):
                                    break
                                if func93(arg0, v2, v5):
                                    break
                                break
                            while True:  # block $label79
                                if (v8 == 0):
                                    break
                                v8 = ((((v2 * v7) + v3) << 2) + 59200)
                                if load32(((((v2 * v7) + v3) << 2) + 59200)):
                                    break
                                if (func93(v3, v2, v5) == 0):
                                    break
                                arg0 = v3
                                break
                                break
                            while True:  # block $label80
                                v4 = (arg0 < 0)
                                if (arg0 < 0):
                                    break
                                if (v2 <= 0):
                                    break
                                if (arg0 >= v7):
                                    break
                                if (v2 > v11):
                                    break
                                v3 = (v2 - 1)
                                v8 = (((((v2 - 1) * v7) + arg0) << 2) + 59200)
                                if load32((((((v2 - 1) * v7) + arg0) << 2) + 59200)):
                                    break
                                if (func93(arg0, v3, v5) == 0):
                                    break
                                v2 = v3
                                break
                                break
                            while True:  # block $label81
                                if (arg0 <= 0):
                                    break
                                if (v2 < 0):
                                    break
                                if (arg0 > v7):
                                    break
                                if (v2 >= v11):
                                    break
                                v3 = (arg0 - 1)
                                v8 = ((((arg0 - 1) + (v2 * v7)) << 2) + 59200)
                                if load32(((((arg0 - 1) + (v2 * v7)) << 2) + 59200)):
                                    break
                                if (func93(v3, v2, v5) == 0):
                                    break
                                arg0 = v3
                                break
                                break
                            if v4:
                                break
                            if (v2 < -1):
                                break
                            if (arg0 >= v7):
                                break
                            v2 = (v2 + 1)
                            if ((v2 + 1) >= v11):
                                break
                            v8 = ((((v2 * v7) + arg0) << 2) + 59200)
                            if load32(((((v2 * v7) + arg0) << 2) + 59200)):
                                break
                            if (func93(arg0, v2, v5) == 0):
                                break
                            break
                        v3 = (v9 + (v6 << 2))
                        store32((v9 + (v6 << 2)), arg0)
                        store32(v3 + 4, v2)
                        store32(v8, 1)
                        v6 = (v6 + 2)
                        break
                    if (u(v1) < u(v6)):
                        continue
                    break
                store32(v5 + 60, v6)
            v2 = (v17 if v19 else v18)
            v10 = (v10 + 1)
            if ((v10 + 1) != 255):
                continue
            break
        arg0 = 0
        v25 = (i64((v2 + 5)) * 80)
        v1 = (-1 if i32(((v25 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64((v2 + 5)) * 80)))
        v3 = func26((-1 if i32(((v25 & 0xFFFFFFFFFFFFFFFF) >> 32)) else i32((i64((v2 + 5)) * 80))))
        # TODO: memory.fill []
        store32(9142836, v3)
        while True:  # $label84
            v1 = ((arg0 * 404) + 9568096)
            v3 = load32(((arg0 * 404) + 9568096) + 200)
            if load32(((arg0 * 404) + 9568096) + 200):
                func232(v3)
                func232((load32(v1 + 200) + 4))
            v7 = 1
            func232(load32(v1 + 224))
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != 255):
                continue
            break
        v3 = -1
        v10 = 2
        v6 = 0
        v2 = 0
        while True:  # $label90
            v4 = (v3 + 1)
            v9 = (v10 - 1)
            arg0 = (v6 << 1)
            v11 = ((v6 << 1) + 2)
            v12 = ((arg0 - 1) & 3)
            v1 = v3
            while True:  # $label89
                v8 = 0
                while True:  # block $label86
                    if (((v1 != v9) & (v1 != v3)) == 0):
                        arg0 = v3
                        while True:  # $label85
                            v5 = ((v2 << 2) + 8611904)
                            store32(((v2 << 2) + 8611904), v1)
                            store32(v5 + 4, arg0)
                            arg0 = (arg0 + 1)
                            v2 = (v2 + 2)
                            v8 = (v8 + 1)
                            if ((v8 + 1) != v12):
                                continue
                            break
                        if (u(v11) < u(3)):
                            break
                        while True:  # $label87
                            v5 = ((v2 << 2) + 8611904)
                            store32(((v2 << 2) + 8611904), v1)
                            store32(v5 + 28, (arg0 + 3))
                            store32(v5 + 24, v1)
                            store32(v5 + 20, (arg0 + 2))
                            store32(v5 + 16, v1)
                            store32(v5 + 12, (arg0 + 1))
                            store32(v5 + 8, v1)
                            store32(v5 + 4, arg0)
                            v2 = (v2 + 8)
                            arg0 = (arg0 + 4)
                            if ((arg0 + 4) != v10):
                                continue
                            break
                        break
                    arg0 = ((v2 << 2) + 8611904)
                    store32(((v2 << 2) + 8611904), v1)
                    store32(arg0 + 4, v3)
                    v2 = (v2 + 2)
                    arg0 = v4
                    if (v6 == -1):
                        break
                    while True:  # $label88
                        if (arg0 == v9):
                            v5 = ((v2 << 2) + 8611904)
                            store32(((v2 << 2) + 8611904), v1)
                            store32(v5 + 4, arg0)
                            v2 = (v2 + 2)
                        v5 = (arg0 + 1)
                        if (v9 == (arg0 + 1)):
                            v8 = ((v2 << 2) + 8611904)
                            store32(((v2 << 2) + 8611904), v1)
                            store32(v8 + 4, v5)
                            v2 = (v2 + 2)
                        arg0 = (arg0 + 2)
                        if ((arg0 + 2) != v10):
                            continue
                        break
                    break
                v1 = (v1 + 1)
                if ((v1 + 1) != v10):
                    continue
                break
            v6 = (v6 + 1)
            v3 = (v7 ^ -1)
            v7 = (v7 + 1)
            v10 = (v10 + 1)
            if ((v10 + 1) != 129):
                continue
            break
        G.global0 = (v13 + 16)
        while True:  # block $label91
            if load8u(9147212):
                break
            if load8u(9147213):
                break
            if load8u(9147152):
                break
            arg0 = load32(load32(9142424) + 184)
            store32(9147312, load32(load32(9142424) + 184))
            store32(9147324, (arg0 ^ -1))
            store32(9147320, (arg0 ^ -1515870811))
            store32(9147316, (arg0 ^ 1515870810))
            Nb()
            break
    store32(9687252, (load32(9687252) + 1))
    return func350()