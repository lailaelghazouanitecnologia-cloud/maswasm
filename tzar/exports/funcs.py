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
# $Ya
# Export: Ya
# ------------------------------------------------------------
def Ya(arg0):
    """Exported as Ya."""
    v1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # block $label0
        if (load32(9213808) != 1):
            break
        v2 = load32(9671128)
        v3 = load32(9173808)
        if ((0 if arg0 else load8u(9147141)) == 0):
            v3 = (v2 + (v3 * 132))
            v2 = load32((v2 + (v3 * 132)) + 16)
            if (load32((v2 + (v3 * 132)) + 16) == 0):
                break
            if (load32(v2 + 8) == 0):
                break
            v2 = 0
            a_b()
            store8(9147141, 1)
            if (arg0 == 0):
                store32(9143000, 0)
            store32(9671120, 0)
            while True:  # block $label1
                arg0 = load32(9147120)
                if (load32(9147120) == 0):
                    break
                while True:  # $label2
                    arg0 = ((load32(9143000) * arg0) + v2)
                    v4 = load32(v3 + 16)
                    if (u(((load32(9143000) * arg0) + v2)) >= u(load32(load32(v3 + 16) + 8))):
                        break
                    store32(9671120, (load32(9671120) + 1))
                    arg0 = load32(((load8u((load32(9671128) + (load32((load32(v4) + (arg0 << 2))) * 132)) + 122) * 404) + 9568096) + 144)
                    store64(v1 + 32, 1)
                    store64(v1 + 40, 0)
                    store64(v1 + 48, 0)
                    store64(v1 + 56, 4294967295)
                    store64(v1 + 24, 1)
                    store32(v1 + 20, (0 - arg0))
                    store32(v1 + 16, v2)
                    a_b()
                    v2 = (v2 + 1)
                    arg0 = load32(9147120)
                    if (u((v2 + 1)) < u(load32(9147120))):
                        continue
                    break
                break
            arg0 = load32(load32(v3 + 16) + 8)
            store32(v1, load32(9143000))
            store32(v1 + 4, arg0)
            a_b()
            break
        store8(9147141, 0)
        store32(9143000, 0)
        if (load32((v2 + (v3 * 132)) + 92) == 0):
            break
        if load32(9140316):
            if (load32(9140320) != load32((v2 + (v3 * 132)) + 28)):
                break
        break
    G.global0 = (v1 - -64)

# ------------------------------------------------------------
# $La
# Export: La
# ------------------------------------------------------------
def La(arg0, arg1):
    """Exported as La."""
    if load32(9147132):
        while True:  # block $label0
            arg1 = load32(9561776)
            if (load32(9561776) != load32(9561772)):
                v2 = load32(9561768)
                break
            v2 = (load32(9561780) + arg1)
            store32(9561772, (load32(9561780) + arg1))
            v3 = load32(9561768)
            v2 = func26((-1 if (u(v2) > u(1073741823)) else (v2 << 2)))
            if arg1:
                # TODO: memory.copy []
            if v3:
                arg1 = load32(9561776)
            store32(9561768, v2)
            break
        store32(9561776, (arg1 + 1))
        store32((v2 + (arg1 << 2)), arg0)
        v3 = (load32(59176) + 10)
        while True:  # block $label1
            arg1 = load32(9561776)
            if (load32(9561776) != load32(9561772)):
                arg0 = v2
                break
            arg0 = (load32(9561780) + arg1)
            store32(9561772, (load32(9561780) + arg1))
            arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
            if arg1:
                # TODO: memory.copy []
            store32(9561768, arg0)
            arg1 = load32(9561776)
            break
        store32(9561776, (arg1 + 1))
        store32((arg0 + (arg1 << 2)), v3)
        return
    while True:  # block $label2
        while True:  # block $label3
            if (arg1 == 0):
                v2 = load32(9142892)
                if (u(load32(9142892)) < u(2)):
                    break
                v3 = load32(9561692)
                arg1 = 1
                while True:  # $label4
                    if (arg0 == load32((v3 + (arg1 * 286704)) + 284616)):
                        arg0 = arg1
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v2):
                        continue
                    break
                break
            if (arg0 == 0):
                break
            break
        if ((load8u(9147213) | load8u(9147214)) == 0):
            break
        if (u(load32(9142892)) > u((arg0 - 1))):
            while True:  # block $label8
                arg1 = load32(9561692)
                while True:  # block $label5
                    if (load8u(9147125) | (load8u(9147213) == 0)):
                        if (load8u(9147126) == 0):
                            break
                    v3 = load32((arg1 + (arg0 * 286704)) + 284616)
                    while True:  # block $label6
                        v2 = load32(9561776)
                        if (load32(9561776) != load32(9561772)):
                            arg0 = load32(9561768)
                            break
                        arg0 = (load32(9561780) + v2)
                        store32(9561772, (load32(9561780) + v2))
                        arg1 = load32(9561768)
                        arg0 = func26((-1 if (u(arg0) > u(1073741823)) else (arg0 << 2)))
                        if v2:
                            # TODO: memory.copy []
                        if arg1:
                            v2 = load32(9561776)
                        store32(9561768, arg0)
                        break
                    store32(9561776, (v2 + 1))
                    store32((arg0 + (v2 << 2)), v3)
                    v3 = (load32(59176) + 10)
                    while True:  # block $label7
                        v2 = load32(9561776)
                        if (load32(9561776) != load32(9561772)):
                            arg1 = arg0
                            break
                        arg1 = (load32(9561780) + v2)
                        store32(9561772, (load32(9561780) + v2))
                        arg1 = func26((-1 if (u(arg1) > u(1073741823)) else (arg1 << 2)))
                        if v2:
                            # TODO: memory.copy []
                        store32(9561768, arg1)
                        v2 = load32(9561776)
                        break
                    store32(9561776, (v2 + 1))
                    store32((arg1 + (v2 << 2)), v3)
                    break
                    break
                arg0 = (arg0 * 286704)
                arg0 = (load32(9561692) + arg0)
                store32((load32(9561692) + arg0) + 284628, load32(arg0 + 284616))
                store32(arg0 + 284616, 0)
                break
        break

# ------------------------------------------------------------
# $Hc
# Export: Hc
# ------------------------------------------------------------
def Hc():
    """Exported as Hc."""
    return load32(load32(9142424) + 48)

# ------------------------------------------------------------
# $Kb
# Export: Kb
# ------------------------------------------------------------
def Kb(arg0, arg1, arg2):
    """Exported as Kb."""
    store8(9147214, 1)
    store8(9147210, 1)

# ------------------------------------------------------------
# $Sb
# Export: Sb
# ------------------------------------------------------------
def Sb(arg0, arg1):
    """Exported as Sb."""
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # block $label0
        if load8u(9147152):
            break
        if load32(9147132):
            break
        if arg0:
            v23 = load32(9561692)
            v18 = load32(9142872)
            v22 = (load32(9561692) + (load32(9142872) * 286704))
            arg0 = ((load32(9561692) + (load32(9142872) * 286704)) + (load32(9681952) << 2))
            v24 = load32((((load32(9561692) + (load32(9142872) * 286704)) + (load32(9681952) << 2)) + 281808))
            v14 = load32(38508)
            v15 = load32(38500)
            v7 = load32(38448)
            v19 = load32(38504)
            v20 = load32(38528)
            v3 = load32(9215884)
            v6 = load32(9671128)
            while True:  # block $label1
                arg0 = load32((arg0 + 284636))
                if (load32((arg0 + 284636)) == 0):
                    break
                v16 = load32(arg0 + 8)
                if (load32(arg0 + 8) == 0):
                    break
                v21 = load32(arg0)
                arg1 = 0
                while True:  # $label10
                    while True:  # block $label2
                        arg0 = load32((v21 + (arg1 << 2)))
                        if (load32((v21 + (arg1 << 2))) == 0):
                            break
                        while True:  # block $label5
                            while True:  # block $label9
                                while True:  # block $label8
                                    while True:  # block $label7
                                        while True:  # block $label6
                                            while True:  # block $label3
                                                while True:  # block $label4
                                                    v2 = (v6 + (arg0 * 132))
                                                    v5 = load8u((v6 + (arg0 * 132)) + 123)
                                                    if (load8u((v6 + (arg0 * 132)) + 123) != 1):
                                                        arg0 = load32(v2 + 44)
                                                        v17 = load32((v3 + (load32(v2 + 44) << 4)) + 4)
                                                        if ((load32((v3 + (load32(v2 + 44) << 4)) + 4) != 1) & (v5 != 3)):
                                                            break
                                                        if (v17 == 1):
                                                            break
                                                        break
                                                    break
                                                arg0 = load8u((v6 + (load32(v2 + 32) * 132)) + 122)
                                                if (load16u(v2 + 90) == load8u((v6 + (load32(v2 + 32) * 132)) + 122)):
                                                    break
                                                if (arg0 == v19):
                                                    break
                                                if (arg0 == v7):
                                                    break
                                                if (arg0 == v15):
                                                    break
                                                if (arg0 == v14):
                                                    break
                                                break
                                            if (load8u(v2 + 129) == 10):
                                                break
                                            if (v5 == 4):
                                                break
                                            arg0 = load32((v3 + (load32(v2 + 44) << 4)) + 4)
                                            if (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 4):
                                                break
                                            v13 = (v13 + ((v5 == 6) | (arg0 == 6)))
                                            break
                                            break
                                        v9 = (v9 + 1)
                                        break
                                        break
                                    v8 = (v8 + 1)
                                    break
                                    break
                                v11 = (v11 + 1)
                                break
                                break
                            v10 = (v10 + 1)
                            break
                            break
                        v12 = (v12 + 1)
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v16):
                        continue
                    break
                break
            arg0 = (v22 + (load32(9681956) << 2))
            v22 = load32(((v22 + (load32(9681956) << 2)) + 281808))
            while True:  # block $label11
                arg0 = load32((arg0 + 284636))
                if (load32((arg0 + 284636)) == 0):
                    break
                v16 = load32(arg0 + 8)
                if (load32(arg0 + 8) == 0):
                    break
                v21 = load32(arg0)
                arg1 = 0
                while True:  # $label20
                    while True:  # block $label12
                        arg0 = load32((v21 + (arg1 << 2)))
                        if (load32((v21 + (arg1 << 2))) == 0):
                            break
                        while True:  # block $label15
                            while True:  # block $label16
                                while True:  # block $label17
                                    while True:  # block $label18
                                        while True:  # block $label19
                                            while True:  # block $label13
                                                while True:  # block $label14
                                                    v2 = (v6 + (arg0 * 132))
                                                    v5 = load8u((v6 + (arg0 * 132)) + 123)
                                                    if (load8u((v6 + (arg0 * 132)) + 123) != 1):
                                                        arg0 = load32(v2 + 44)
                                                        v17 = (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 1)
                                                        if (((load32((v3 + (load32(v2 + 44) << 4)) + 4) == 1) == 0) & (v5 != 3)):
                                                            break
                                                        if (v17 == 0):
                                                            break
                                                        break
                                                    break
                                                arg0 = load8u((v6 + (load32(v2 + 32) * 132)) + 122)
                                                if (load8u((v6 + (load32((v3 + ((arg0 << 4) | 12))) * 132)) + 122) == load8u((v6 + (load32(v2 + 32) * 132)) + 122)):
                                                    break
                                                if (arg0 == v19):
                                                    break
                                                if (arg0 == v7):
                                                    break
                                                if (arg0 == v15):
                                                    break
                                                if (arg0 == v14):
                                                    break
                                                break
                                            if (load8u(v2 + 129) == 10):
                                                break
                                            if (v5 == 4):
                                                break
                                            arg0 = load32((v3 + (load32(v2 + 44) << 4)) + 4)
                                            if (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 4):
                                                break
                                            v13 = (v13 + ((v5 == 6) | (arg0 == 6)))
                                            break
                                            break
                                        v10 = (v10 + 1)
                                        break
                                        break
                                    v11 = (v11 + 1)
                                    break
                                    break
                                v8 = (v8 + 1)
                                break
                                break
                            v9 = (v9 + 1)
                            break
                            break
                        v12 = (v12 + 1)
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v16):
                        continue
                    break
                break
            v16 = (v23 + (v18 * 286704))
            arg0 = ((v23 + (v18 * 286704)) + (load32(9681960) << 2))
            v21 = load32((((v23 + (v18 * 286704)) + (load32(9681960) << 2)) + 281808))
            while True:  # block $label21
                arg0 = load32((arg0 + 284636))
                if (load32((arg0 + 284636)) == 0):
                    break
                v17 = load32(arg0 + 8)
                if (load32(arg0 + 8) == 0):
                    break
                v25 = load32(arg0)
                arg1 = 0
                while True:  # $label30
                    while True:  # block $label22
                        arg0 = load32((v25 + (arg1 << 2)))
                        if (load32((v25 + (arg1 << 2))) == 0):
                            break
                        while True:  # block $label25
                            while True:  # block $label26
                                while True:  # block $label27
                                    while True:  # block $label28
                                        while True:  # block $label29
                                            while True:  # block $label23
                                                while True:  # block $label24
                                                    v2 = (v6 + (arg0 * 132))
                                                    v5 = load8u((v6 + (arg0 * 132)) + 123)
                                                    if (load8u((v6 + (arg0 * 132)) + 123) != 1):
                                                        arg0 = load32(v2 + 44)
                                                        v26 = (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 1)
                                                        if (((load32((v3 + (load32(v2 + 44) << 4)) + 4) == 1) == 0) & (v5 != 3)):
                                                            break
                                                        if (v26 == 0):
                                                            break
                                                        break
                                                    break
                                                arg0 = load8u((v6 + (load32(v2 + 32) * 132)) + 122)
                                                if (load8u((v6 + (load32((v3 + ((arg0 << 4) | 12))) * 132)) + 122) == load8u((v6 + (load32(v2 + 32) * 132)) + 122)):
                                                    break
                                                if (arg0 == v19):
                                                    break
                                                if (arg0 == v7):
                                                    break
                                                if (arg0 == v15):
                                                    break
                                                if (arg0 == v14):
                                                    break
                                                break
                                            if (load8u(v2 + 129) == 10):
                                                break
                                            if (v5 == 4):
                                                break
                                            arg0 = load32((v3 + (load32(v2 + 44) << 4)) + 4)
                                            if (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 4):
                                                break
                                            v13 = (v13 + ((v5 == 6) | (arg0 == 6)))
                                            break
                                            break
                                        v10 = (v10 + 1)
                                        break
                                        break
                                    v11 = (v11 + 1)
                                    break
                                    break
                                v8 = (v8 + 1)
                                break
                                break
                            v9 = (v9 + 1)
                            break
                            break
                        v12 = (v12 + 1)
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v17):
                        continue
                    break
                break
            v3 = 0
            v2 = 0
            v14 = 0
            v15 = 0
            while True:  # block $label31
                arg0 = (load32(9142848) * 25)
                # TODO: i32.div_u []
                arg1 = (10000 * 15)
                v7 = load32((v16 + 278572))
                if (u((10000 * 15)) >= u(load32(load32((v16 + 278572)) + 8))):
                    break
                if (u(arg0) < u(40000)):
                    break
                arg0 = (load32(v7) + (arg1 << 2))
                v15 = (load32((load32(v7) + (arg1 << 2)) + 28) - load32((arg0 - 212)))
                v14 = (load32(arg0 + 24) - load32((arg0 - 216)))
                v2 = (load32(arg0 + 20) - load32((arg0 - 220)))
                break
            v6 = (load32(arg0 + 16) - load32((arg0 - 224)))
            v19 = load32(9142892)
            if (u(load32(9142892)) >= u(2)):
                v20 = (v18 * v19)
                v5 = load32(9143004)
                arg1 = 1
                while True:  # $label33
                    while True:  # block $label32
                        arg0 = (v23 + (arg1 * 286704))
                        if load8u((v5 + (load32((v23 + (arg1 * 286704)) + 283908) + v20))):
                            break
                        if (u(v3) > u(999)):
                            break
                        v18 = load8u(arg0 + 283972)
                        v16 = load8u((arg0 + 283974))
                        v17 = load8u((arg0 + 283973))
                        v7 = ((v3 << 2) + 9147392)
                        store32(((v3 << 2) + 9147392) + 4, arg0)
                        store32(v7, ((v16 | (v17 << 8)) | (v18 << 16)))
                        v18 = load32(arg0 + 284616)
                        store32(v7 + 8, (load32(arg0 + 284616) if v18 else load32(arg0 + 284628)))
                        v3 = (v3 + 7)
                        break
                    arg1 = (arg1 + 1)
                    if ((arg1 + 1) != v19):
                        continue
                    break
            store32(v4 + 44, v3)
            store32(v4 + 40, v15)
            store32(v4 + 36, v14)
            store32(v4 + 32, v2)
            store32(v4 + 28, v6)
            store32(v4 + 24, ((v22 + v24) + v21))
            store32(v4 + 20, v13)
            store32(v4 + 16, v12)
            store32(v4 + 12, v10)
            store32(v4 + 8, v11)
            store32(v4 + 4, v8)
            store32(v4, v9)
            a_b()
            break
        a_b()
        break
    G.global0 = (v4 + 48)
    return 0

# ------------------------------------------------------------
# $Pd
# Export: Pd
# ------------------------------------------------------------
def Pd(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    """Exported as Pd."""
    v7 = (G.global0 - 176)
    G.global0 = (G.global0 - 176)
    v8 = load32(9561692)
    v10 = ((arg0 * 132) + 9216080)
    while True:  # block $label0
        v15 = (0 if arg6 else load32(9671124))
        if (u(((0 if arg6 else load32(9671124)) - 97)) > u(-3)):
            break
        v13 = load32(v10 + 68)
        if (load32(v10 + 68) == 0):
            break
        v14 = load32(9147132)
        v16 = ((arg0 * 132) + 9216080)
        v17 = (v8 + (arg3 * 286704))
        arg6 = 0
        while True:  # $label3
            while True:  # block $label2
                while True:  # block $label1
                    v18 = load32((v16 + (arg6 << 2)) + 28)
                    v9 = ((load32((v16 + (arg6 << 2)) + 28) * 404) + 9568096)
                    if (load32(((load32((v16 + (arg6 << 2)) + 28) * 404) + 9568096) + 196) == arg2):
                        break
                    if v14:
                        break
                    # br_table[load32(v9 + 264)]
                    break
                    break
                if load8u(v9 + 354):
                    break
                v12 = ((v11 << 2) + 9147392)
                store32(((v11 << 2) + 9147392), load32(v9 + 84))
                v9 = load32(v9 + 180)
                store32(v12 + 4, load32(load32(v9 + 180) + 8))
                store32(v12 + 8, load32(v9 + 12))
                store32(v12 + 12, load32(((v17 + (v18 << 2)) + 281808)))
                v11 = (v11 + 4)
                break
            arg6 = (arg6 + 1)
            if ((arg6 + 1) != v13):
                continue
            break
        break
    v9 = load32(v10 + 12)
    store64(v7 + 168, 0)
    store64(v7 + 160, 0)
    while True:  # block $label7
        if load8u(v10 + 23):
            arg1 = load32(((arg0 * 132) + 9216080) + 4)
            while True:  # block $label4
                if (arg4 == 0):
                    arg4 = load32((((v8 + (arg3 * 286704)) + (arg1 * 36)) + 269376))
                    arg4 = (load32((((v8 + (arg3 * 286704)) + (arg1 * 36)) + 269376)) if arg4 else 100)
                    arg5 = ((arg1 * 404) + 9568096)
                    # TODO: i32.div_u []
                    v12 = 100
                    # TODO: i32.div_u []
                    v13 = 100
                    # TODO: i32.div_u []
                    v14 = 100
                    # TODO: i32.div_u []
                    break
                if (v15 != 95):
                    arg4 = ((arg1 * 404) + 9568096)
                    v14 = (((load32(((arg1 * 404) + 9568096) + 68) * 36) // 10) + 620)
                    v12 = ((load32(arg4 + 80) * 36) // 10)
                    v13 = ((load32(arg4 + 72) * 36) // 10)
                    break
                arg4 = ((arg1 * 404) + 9568096)
                v14 = (((load32(((arg1 * 404) + 9568096) + 68) * 144) // 10) + (120 if (load32((((v8 + (arg3 * 286704)) + (load32(39136) << 2)) + 281808)) == 1) else 0))
                v12 = ((load32(arg4 + 80) * 144) // 10)
                v13 = ((load32(arg4 + 72) * 144) // 10)
                break
            v15 = ((load32(arg4 + 76) * 144) // 10)
            while True:  # block $label5
                arg5 = ((arg1 * 404) + 9568096)
                v17 = load32(((arg1 * 404) + 9568096) + 264)
                if (load32(((arg1 * 404) + 9568096) + 264) != 3):
                    break
                arg4 = load32(arg5 + 368)
                if (load32(arg5 + 368) == 60):
                    break
                if (arg4 == 61):
                    break
                if (arg4 == 63):
                    break
                if (arg4 == 62):
                    break
                if (arg4 == 55):
                    break
                break
            arg4 = (6 if arg4 else 5)
            v16 = 0
            while True:  # block $label6
                arg6 = load32(v10)
                if (load32(v10) == 5):
                    break
                if (arg6 == 12):
                    break
                if (arg6 == 7):
                    break
                break
            v9 = (3 if (arg6 == 15) else (3 if (arg6 == 1) else (3 if (arg6 == 16) else -1)))
            v18 = load32(arg5 + 116)
            v19 = load32(arg5 + 236)
            v20 = load32(arg5 + 232)
            v21 = load32(arg5 + 244)
            v22 = load32(arg5 + 240)
            arg6 = ((arg1 * 404) + 9568096)
            v23 = load32(((arg1 * 404) + 9568096) + 144)
            if (v17 == 1):
                arg3 = func180((v8 + (arg3 * 286704)), arg1)
                v8 = load32(arg6 + 204)
            else:
            store32((load32(arg6 + 204) if (u(arg3) >= u(v8)) else 0) + 144, 0)
            store32(v7 + 140, arg2)
            store32(v7 + 136, v23)
            store32(v7 + 132, v9)
            store32(v7 + 128, v18)
            store32(v7 + 124, v19)
            store32(v7 + 120, v20)
            store32(v7 + 116, v21)
            store32(v7 + 112, v22)
            arg3 = load32(arg6 + 88)
            arg6 = load32(arg6 + 84)
            v8 = load32(v10 + 12)
            arg2 = 0
            if (load32(arg5 + 264) == 3):
                arg2 = load32(((arg1 * 404) + 9568096) + 120)
            v24 = load64(((arg0 * 132) + 9216080) + 124)
            arg0 = ((arg1 * 404) + 9568096)
            arg1 = load32(((arg1 * 404) + 9568096) + 92)
            arg5 = load32(arg0 + 100)
            v10 = load32(arg0 + 104)
            arg0 = load32(arg0 + 212)
            store32((v7 - -64), v8)
            store32(v7 + 68, arg6)
            store32(v7 + 72, arg3)
            store32(v7 + 76, v11)
            store32(v7 + 80, arg2)
            store32(v7 + 108, arg0)
            store32(v7 + 104, v10)
            store32(v7 + 100, arg5)
            store32(v7 + 96, arg1)
            store32(v7 + 92, arg4)
            store64(v7 + 84, v24)
            store32(v7 + 52, v13)
            store32(v7 + 56, v15)
            store32(v7 + 60, v12)
            store32(v7 + 48, v14)
            break
        arg6 = 0
        while True:  # block $label8
            arg2 = load32(v10)
            if ((load32(v10) != 1) & (arg2 != 13)):
                break
            arg2 = load32(((arg0 * 132) + 9216080) + 4)
            if (load32(((arg0 * 132) + 9216080) + 4) == 0):
                break
            arg4 = ((arg2 * 40) + 9671200)
            arg2 = load32(((arg2 * 40) + 9671200) + 12)
            if load32(((arg2 * 40) + 9671200) + 12):
                store64(v7 + 160, load64(arg2))
                store64(v7 + 168, load64(arg2 + 8))
            arg2 = load32(arg4 + 8)
            if (load32(arg4 + 8) == 0):
                break
            arg6 = load32((((v8 + (load16u((load32(9671128) + (load32(9173808) * 132)) + 110) * 286704)) + (arg2 << 2)) + 283984))
            break
        while True:  # block $label9
            if (v15 != 240):
                break
            if (load32(38892) != arg5):
                break
            arg2 = load32((v8 + (arg3 * 286704)) + 281792)
            if (load32((v8 + (arg3 * 286704)) + 281792) == 0):
                break
            if (u(load32(arg2 + 8)) <= u(arg1)):
                break
            arg1 = load32((load32(arg2) + (arg1 << 2)))
            arg2 = ((load32((load32(arg2) + (arg1 << 2))) & 0xFFFFFFFF) >> 16)
            while True:  # block $label12
                while True:  # block $label10
                    while True:  # block $label11
                        arg4 = (arg1 & 65535)
                        arg1 = (((arg1 & 65535) * 404) + 9568096)
                        # br_table[load32((((arg1 & 65535) * 404) + 9568096) + 268)]
                        break
                        break
                    arg2 = (arg2 * 150)
                    # TODO: i32.div_u []
                    store32(((arg2 * 150) * load32(arg1 + 68)) + 160, 100)
                    # TODO: i32.div_u []
                    store32((load32(arg1 + 72) * arg2) + 164, 100)
                    # TODO: i32.div_u []
                    store32((load32(arg1 + 76) * arg2) + 168, 100)
                    # TODO: i32.div_u []
                    store32((load32(arg1 + 80) * arg2) + 172, 100)
                    break
                    break
                while True:  # block $label14
                    while True:  # block $label13
                        if (load32(38972) == arg4):
                            break
                        if (load32(38976) == arg4):
                            break
                        break
                        break
                    break
                store32((20 if (load32(38968) == arg4) else 4) + 160, (8 * arg2))
                break
                break
            store32(v7 + 160, (arg2 << 4))
            break
        if (v9 == 323):
            arg1 = (v8 + (arg3 * 286704))
            store32(((v7 + 160) + (load32((v8 + (arg3 * 286704)) + 283920) << 2)), load32(arg1 + 283916))
        arg0 = load32(((arg0 * 132) + 9216080) + 120)
        store32(v7 + 16, load32(v10 + 12))
        store32(v7 + 20, arg0)
        store32(v7 + 24, 0)
        store32(v7 + 28, v11)
        store32(v7 + 32, arg6)
        store64(v7, load64(v7 + 160))
        store64(v7 + 8, load64(v7 + 168))
        break
    if v11:
        # TODO: memory.fill []
    G.global0 = (v7 + 176)
    return (v11 << 2)

# ------------------------------------------------------------
# $Za
# Export: Za
# ------------------------------------------------------------
def Za():
    """Exported as Za."""
    if load8u(9147210):
        func41(44, 0, 0, 0, 0)
        return
    # call_indirect[load32(9214176)]

# ------------------------------------------------------------
# $D
# Export: D
# ------------------------------------------------------------
def D(arg0):
    """Exported as D."""
    v3 = load64(9147316)
    v1 = load32(9147312)
    store32(9147316, load32(9147312))
    v2 = load32(9147324)
    store64(9147320, v3)
    v2 = (v2 ^ (v2 << 11))
    v1 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2)
    store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2))
    return (v1 % arg0)