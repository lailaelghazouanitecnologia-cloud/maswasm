"""
Tzar Engine - Api module.
Auto-generated from WebAssembly.
"""
from tzar.runtime import (
    load32, load64, load8u, load8s, load16u, load16s,
    loadf32, loadf64,
    store32, store64, store8, store16, storef32, storef64,
    atomic_load, atomic_store,
    i32, i64, u32, u64, f32,
    rotl, rotr, clz, ctz, popcnt,
    sqrt, abs, ceil, floor, trunc,
    G, mem_size, mem_grow, call_table,
)

# Known addresses
GAME_STATE = 9142424
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892
PLAYERS = 9561692
ENTITY_TYPES = 9568096
ENTITIES = 9671128
HEAP_FREELIST = 9690464
HEAP_TREE = 9690468
FREE_SIZE = 9690472
HEAP_TOTAL = 9690476
HEAP_BASE = 9690480
HEAP_TOP = 9690484
HEAP_END = 9690488
ALLOC_COUNT = 9690496
MEM_FLAGS = 9690908
MEM_MUTEX = 9690912
ALLOC_HANDLER = 9690984

class Unreachable(Exception):
    pass


# ----------------------------------------------------------
# $Ya
# Export: Ya
# ----------------------------------------------------------
def Ya(arg0):
    """Export: Ya"""
    v1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        if (load32(9213808) != 1):
            break
        v2 = load32(ENTITIES)
        v3 = load32(9173808)
        if not (0 if arg0 else load8u(9147141)):
            v3 = (v2 + (v3 * 132))
            v2 = load32((v2 + (v3 * 132)) + 16)
            if not load32((v2 + (v3 * 132)) + 16):
                break
            if not load32(v2 + 8):
                break
            v2 = 0
            a_b()
            store8(9147141, 1)
            if not arg0:
                store32(9143000, 0)
            store32(9671120, 0)
            while True:  # $label1
                arg0 = load32(9147120)
                if not load32(9147120):
                    break
                while True:  # $label2
                    arg0 = ((load32(9143000) * arg0) + v2)
                    v4 = load32(v3 + 16)
                    if (u32(((load32(9143000) * arg0) + v2)) >= u32(load32(load32(v3 + 16) + 8))):
                        break
                    store32(9671120, (load32(9671120) + 1))
                    arg0 = load32(((load8u(entities[load32((load32(v4) + (arg0 << 2)))].sub_state) * 404) + ENTITY_TYPES) + 144)
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
                    if (u32((v2 + 1)) < u32(load32(9147120))):
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
        if not load32((v2 + (v3 * 132)) + 92):
            break
        if load32(9140316):
            if (load32(9140320) != load32((v2 + (v3 * 132)) + 28)):
                break
        break
    G.global0 = (v1 - -64)

# ----------------------------------------------------------
# $La
# Export: La
# ----------------------------------------------------------
def La(arg0, arg1):
    """Export: La"""
    if load32(9147132):
        while True:  # $label0
            arg1 = load32(9561776)
            if (load32(9561776) != load32(9561772)):
                v2 = load32(9561768)
                break
            v2 = (load32(9561780) + arg1)
            store32(9561772, (load32(9561780) + arg1))
            v3 = load32(9561768)
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if arg1:
                # TODO: memory.copy
            if v3:
                arg1 = load32(9561776)
            store32(9561768, v2)
            break
        store32(9561776, (arg1 + 1))
        store32((v2 + (arg1 << 2)), arg0)
        v3 = (load32(59176) + 10)
        while True:  # $label1
            arg1 = load32(9561776)
            if (load32(9561776) != load32(9561772)):
                arg0 = v2
                break
            arg0 = (load32(9561780) + arg1)
            store32(9561772, (load32(9561780) + arg1))
            arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg1:
                # TODO: memory.copy
            store32(9561768, arg0)
            arg1 = load32(9561776)
            break
        store32(9561776, (arg1 + 1))
        store32((arg0 + (arg1 << 2)), v3)
        return
    while True:  # $label2
        while True:  # $label3
            if not arg1:
                v2 = load32(PLAYER_COUNT)
                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                    break
                v3 = load32(PLAYERS)
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
            if not arg0:
                break
            break
        if not (load8u(9147213) | load8u(9147214)):
            break
        if (u32(load32(PLAYER_COUNT)) > u32((arg0 - 1))):
            while True:  # $label8
                arg1 = load32(PLAYERS)
                while True:  # $label5
                    if (load8u(9147125) | not load8u(9147213)):
                        if not load8u(9147126):
                            break
                    v3 = load32((arg1 + (arg0 * 286704)) + 284616)
                    while True:  # $label6
                        v2 = load32(9561776)
                        if (load32(9561776) != load32(9561772)):
                            arg0 = load32(9561768)
                            break
                        arg0 = (load32(9561780) + v2)
                        store32(9561772, (load32(9561780) + v2))
                        arg1 = load32(9561768)
                        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                        if v2:
                            # TODO: memory.copy
                        if arg1:
                            v2 = load32(9561776)
                        store32(9561768, arg0)
                        break
                    store32(9561776, (v2 + 1))
                    store32((arg0 + (v2 << 2)), v3)
                    v3 = (load32(59176) + 10)
                    while True:  # $label7
                        v2 = load32(9561776)
                        if (load32(9561776) != load32(9561772)):
                            arg1 = arg0
                            break
                        arg1 = (load32(9561780) + v2)
                        store32(9561772, (load32(9561780) + v2))
                        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                        if v2:
                            # TODO: memory.copy
                        store32(9561768, arg1)
                        v2 = load32(9561776)
                        break
                    store32(9561776, (v2 + 1))
                    store32((arg1 + (v2 << 2)), v3)
                    break
                    break
                arg0 = (arg0 * 286704)
                arg0 = (load32(PLAYERS) + arg0)
                store32((load32(PLAYERS) + arg0) + 284628, load32(arg0 + 284616))
                store32(arg0 + 284616, 0)
                break
        break

# ----------------------------------------------------------
# $Kb
# Export: Kb
# ----------------------------------------------------------
def Kb(arg0, arg1, arg2):
    """Export: Kb"""
    store8(9147214, 1)
    store8(9147210, 1)

# ----------------------------------------------------------
# $Sb
# Export: Sb
# ----------------------------------------------------------
def Sb(arg0, arg1):
    """Export: Sb"""
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label0
        if load8u(9147152):
            break
        if load32(9147132):
            break
        if arg0:
            v23 = load32(PLAYERS)
            v18 = load32(CURRENT_PLAYER)
            v22 = players[load32(CURRENT_PLAYER)]
            arg0 = (players[load32(CURRENT_PLAYER)] + (load32(9681952) << 2))
            v24 = load32(((players[load32(CURRENT_PLAYER)] + (load32(9681952) << 2)) + 281808))
            v14 = load32(38508)
            v15 = load32(38500)
            v7 = load32(38448)
            v19 = load32(38504)
            v20 = load32(38528)
            v3 = load32(9215884)
            v6 = load32(ENTITIES)
            while True:  # $label1
                arg0 = load32((arg0 + 284636))
                if not load32((arg0 + 284636)):
                    break
                v16 = load32(arg0 + 8)
                if not load32(arg0 + 8):
                    break
                v21 = load32(arg0)
                arg1 = 0
                while True:  # $label10
                    while True:  # $label2
                        arg0 = load32((v21 + (arg1 << 2)))
                        if not load32((v21 + (arg1 << 2))):
                            break
                        while True:  # $label5
                            while True:  # $label9
                                while True:  # $label8
                                    while True:  # $label7
                                        while True:  # $label6
                                            while True:  # $label3
                                                while True:  # $label4
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
            while True:  # $label11
                arg0 = load32((arg0 + 284636))
                if not load32((arg0 + 284636)):
                    break
                v16 = load32(arg0 + 8)
                if not load32(arg0 + 8):
                    break
                v21 = load32(arg0)
                arg1 = 0
                while True:  # $label20
                    while True:  # $label12
                        arg0 = load32((v21 + (arg1 << 2)))
                        if not load32((v21 + (arg1 << 2))):
                            break
                        while True:  # $label15
                            while True:  # $label16
                                while True:  # $label17
                                    while True:  # $label18
                                        while True:  # $label19
                                            while True:  # $label13
                                                while True:  # $label14
                                                    v2 = (v6 + (arg0 * 132))
                                                    v5 = load8u((v6 + (arg0 * 132)) + 123)
                                                    if (load8u((v6 + (arg0 * 132)) + 123) != 1):
                                                        arg0 = load32(v2 + 44)
                                                        v17 = (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 1)
                                                        if (not (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 1) & (v5 != 3)):
                                                            break
                                                        if not v17:
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
            while True:  # $label21
                arg0 = load32((arg0 + 284636))
                if not load32((arg0 + 284636)):
                    break
                v17 = load32(arg0 + 8)
                if not load32(arg0 + 8):
                    break
                v25 = load32(arg0)
                arg1 = 0
                while True:  # $label30
                    while True:  # $label22
                        arg0 = load32((v25 + (arg1 << 2)))
                        if not load32((v25 + (arg1 << 2))):
                            break
                        while True:  # $label25
                            while True:  # $label26
                                while True:  # $label27
                                    while True:  # $label28
                                        while True:  # $label29
                                            while True:  # $label23
                                                while True:  # $label24
                                                    v2 = (v6 + (arg0 * 132))
                                                    v5 = load8u((v6 + (arg0 * 132)) + 123)
                                                    if (load8u((v6 + (arg0 * 132)) + 123) != 1):
                                                        arg0 = load32(v2 + 44)
                                                        v26 = (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 1)
                                                        if (not (load32((v3 + (load32(v2 + 44) << 4)) + 4) == 1) & (v5 != 3)):
                                                            break
                                                        if not v26:
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
            while True:  # $label31
                arg0 = (load32(9142848) * 25)
                # TODO: i32.div_u
                arg1 = (10000 * 15)
                v7 = load32((v16 + 278572))
                if (u32((10000 * 15)) >= u32(load32(load32((v16 + 278572)) + 8))):
                    break
                if (u32(arg0) < u32(40000)):
                    break
                arg0 = (load32(v7) + (arg1 << 2))
                v15 = (load32((load32(v7) + (arg1 << 2)) + 28) - load32((arg0 - 212)))
                v14 = (load32(arg0 + 24) - load32((arg0 - 216)))
                v2 = (load32(arg0 + 20) - load32((arg0 - 220)))
                break
            v6 = (load32(arg0 + 16) - load32((arg0 - 224)))
            v19 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                v20 = (v18 * v19)
                v5 = load32(9143004)
                arg1 = 1
                while True:  # $label33
                    while True:  # $label32
                        arg0 = (v23 + (arg1 * 286704))
                        if load8u((v5 + (load32((v23 + (arg1 * 286704)) + 283908) + v20))):
                            break
                        if (u32(v3) > u32(999)):
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

# ----------------------------------------------------------
# $Pd
# Export: Pd
# ----------------------------------------------------------
def Pd(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    """Export: Pd"""
    v7 = (G.global0 - 176)
    G.global0 = (G.global0 - 176)
    v8 = load32(PLAYERS)
    v10 = ((arg0 * 132) + 9216080)
    while True:  # $label0
        v15 = (0 if arg6 else load32(9671124))
        if (u32(((0 if arg6 else load32(9671124)) - 97)) > u32(-3)):
            break
        v13 = load32(v10 + 68)
        if not load32(v10 + 68):
            break
        v14 = load32(9147132)
        v16 = ((arg0 * 132) + 9216080)
        v17 = (v8 + (arg3 * 286704))
        arg6 = 0
        while True:  # $label3
            while True:  # $label2
                while True:  # $label1
                    v18 = load32((v16 + (arg6 << 2)) + 28)
                    v9 = ((load32((v16 + (arg6 << 2)) + 28) * 404) + ENTITY_TYPES)
                    if (load32(((load32((v16 + (arg6 << 2)) + 28) * 404) + ENTITY_TYPES) + 196) == arg2):
                        break
                    if v14:
                        break
                    # br_table load32(v9 + 264)
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
    while True:  # $label7
        if load8u(v10 + 23):
            arg1 = load32(((arg0 * 132) + 9216080) + 4)
            while True:  # $label4
                if not arg4:
                    arg4 = load32((((v8 + (arg3 * 286704)) + (arg1 * 36)) + 269376))
                    arg4 = (load32((((v8 + (arg3 * 286704)) + (arg1 * 36)) + 269376)) if arg4 else 100)
                    arg5 = ((arg1 * 404) + ENTITY_TYPES)
                    # TODO: i32.div_u
                    v12 = 100
                    # TODO: i32.div_u
                    v13 = 100
                    # TODO: i32.div_u
                    v14 = 100
                    # TODO: i32.div_u
                    break
                if (v15 != 95):
                    arg4 = ((arg1 * 404) + ENTITY_TYPES)
                    v14 = (((load32(((arg1 * 404) + ENTITY_TYPES) + 68) * 36) // 10) + 620)
                    v12 = ((load32(arg4 + 80) * 36) // 10)
                    v13 = ((load32(arg4 + 72) * 36) // 10)
                    break
                arg4 = ((arg1 * 404) + ENTITY_TYPES)
                v14 = (((load32(((arg1 * 404) + ENTITY_TYPES) + 68) * 144) // 10) + (120 if (load32((((v8 + (arg3 * 286704)) + (load32(39136) << 2)) + 281808)) == 1) else 0))
                v12 = ((load32(arg4 + 80) * 144) // 10)
                v13 = ((load32(arg4 + 72) * 144) // 10)
                break
            v15 = ((load32(arg4 + 76) * 144) // 10)
            while True:  # $label5
                arg5 = ((arg1 * 404) + ENTITY_TYPES)
                v17 = load32(((arg1 * 404) + ENTITY_TYPES) + 264)
                if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) != 3):
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
            while True:  # $label6
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
            arg6 = ((arg1 * 404) + ENTITY_TYPES)
            v23 = load32(((arg1 * 404) + ENTITY_TYPES) + 144)
            if (v17 == 1):
                arg3 = func180((v8 + (arg3 * 286704)), arg1)
                v8 = load32(arg6 + 204)
            else:
            store32((load32(arg6 + 204) if (u32(arg3) >= u32(v8)) else 0) + 144, 0)
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
                arg2 = load32(((arg1 * 404) + ENTITY_TYPES) + 120)
            v24 = load64(((arg0 * 132) + 9216080) + 124)
            arg0 = ((arg1 * 404) + ENTITY_TYPES)
            arg1 = load32(((arg1 * 404) + ENTITY_TYPES) + 92)
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
        while True:  # $label8
            arg2 = load32(v10)
            if ((load32(v10) != 1) & (arg2 != 13)):
                break
            arg2 = load32(((arg0 * 132) + 9216080) + 4)
            if not load32(((arg0 * 132) + 9216080) + 4):
                break
            arg4 = ((arg2 * 40) + 9671200)
            arg2 = load32(((arg2 * 40) + 9671200) + 12)
            if load32(((arg2 * 40) + 9671200) + 12):
                store64(v7 + 160, load64(arg2))
                store64(v7 + 168, load64(arg2 + 8))
            arg2 = load32(arg4 + 8)
            if not load32(arg4 + 8):
                break
            arg6 = load32((((v8 + (load16u(entities[load32(9173808)] + 110) * 286704)) + (arg2 << 2)) + 283984))
            break
        while True:  # $label9
            if (v15 != 240):
                break
            if (load32(38892) != arg5):
                break
            arg2 = load32((v8 + (arg3 * 286704)) + 281792)
            if not load32((v8 + (arg3 * 286704)) + 281792):
                break
            if (u32(load32(arg2 + 8)) <= u32(arg1)):
                break
            arg1 = load32((load32(arg2) + (arg1 << 2)))
            arg2 = ((load32((load32(arg2) + (arg1 << 2))) & 0xFFFFFFFF) >> 16)
            while True:  # $label12
                while True:  # $label10
                    while True:  # $label11
                        arg4 = (arg1 & 65535)
                        arg1 = (((arg1 & 65535) * 404) + ENTITY_TYPES)
                        # br_table load32((((arg1 & 65535) * 404) + ENTITY_TYPES) + 268)
                        break
                        break
                    arg2 = (arg2 * 150)
                    # TODO: i32.div_u
                    store32(((arg2 * 150) * load32(arg1 + 68)) + 160, 100)
                    # TODO: i32.div_u
                    store32((load32(arg1 + 72) * arg2) + 164, 100)
                    # TODO: i32.div_u
                    store32((load32(arg1 + 76) * arg2) + 168, 100)
                    # TODO: i32.div_u
                    store32((load32(arg1 + 80) * arg2) + 172, 100)
                    break
                    break
                while True:  # $label14
                    while True:  # $label13
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
        # TODO: memory.fill
    G.global0 = (v7 + 176)
    return (v11 << 2)

# ----------------------------------------------------------
# $Za
# Export: Za
# ----------------------------------------------------------
def Za():
    """Export: Za"""
    if load8u(9147210):
        func41(44, 0, 0, 0, 0)
        return

# ----------------------------------------------------------
# $D
# Export: D
# ----------------------------------------------------------
def D(arg0):
    """Export: D"""
    v3 = load64(9147316)
    v1 = load32(9147312)
    store32(9147316, load32(9147312))
    v2 = load32(9147324)
    store64(9147320, v3)
    v2 = (v2 ^ (v2 << 11))
    v1 = ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2)
    store32(9147312, ((v1 ^ (((v1 & 0xFFFFFFFF) >> 19) ^ (((v2 ^ (v2 << 11)) & 0xFFFFFFFF) >> 8))) ^ v2))
    return (v1 % arg0)

# ----------------------------------------------------------
# $Te
# Export: Te
# ----------------------------------------------------------
def Te(arg0, arg1, arg2, arg3, arg4, arg5, arg6):
    """Export: Te"""
    v11 = (G.global0 - 400)
    G.global0 = (G.global0 - 400)
    store8(9687269, arg5)
    store32(9687272, arg0)
    store32(v11 + 396, arg0)
    arg0 = (-1 if (u32(arg0) > u32(-5)) else ((arg0 & -4) + 4))
    v10 = func26((-1 if (u32(arg0) > u32(-5)) else ((arg0 & -4) + 4)))
    # TODO: memory.fill
    v15 = load32(v10)
    store32(9684508, load32(v10))
    while True:  # $label2
        while True:  # $label3
            while True:  # $label1
                if load8u(9147152):
                    while True:  # $label0
                        if (u32(v15) >= u32(467)):
                            arg0 = load32(v10 + 72)
                            store32(9561760, load32(v10 + 72))
                            break
                        arg0 = load32(9561760)
                        break
                    if not arg0:
                        break
                    if not arg3:
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
        if ((u32(load32(v10 + 36)) <= u32(arg2)) & (u32(arg2) >= u32(2))):
            break
        arg1 = load32(9687204)
        if load32(9687204):
            store32(9687204, 0)
        store32(PLAYER_COUNT, arg0)
        arg1 = load32(v10 + 68)
        store32(CURRENT_PLAYER, ((1 if (u32(arg0) <= u32(arg1)) else load32(v10 + 68)) if arg1 else 1))
        v56 = (i32(arg0) * 286704)
        arg1 = (-1 if i32(((v56 & 0xFFFFFFFF) >> 32)) else i32((i32(arg0) * 286704)))
        arg3 = func26((-1 if i32(((v56 & 0xFFFFFFFF) >> 32)) else i32((i32(arg0) * 286704))))
        # TODO: memory.fill
        store32(PLAYERS, arg3)
        arg1 = load32(v10 + 48)
        store32(9142440, load32(v10 + 48))
        v21 = (v10 + 4)
        while True:  # $label6
            while True:  # $label7
                while True:  # $label5
                    while True:  # $label4
                        if (u32(v15) >= u32(491)):
                            v13 = load32(v10 + 76)
                            v20 = load32(v10 + 60)
                            v35 = load32(v10 + 56)
                            arg6 = load32(v10 + 24)
                            if (u32(v15) <= u32(551)):
                                arg3 = (arg0 - 1)
                                v8 = ((((arg1 * arg1) & 0xFFFFFFFF) >> 2) + 1)
                                v12 = (arg0 * arg0)
                                v23 = arg6
                                break
                            v23 = 1
                            v8 = ((((arg1 * arg1) & 0xFFFFFFFF) >> 2) + 1)
                            v12 = (arg0 * arg0)
                            v29 = load32(v10 + 144)
                            if (u32(v15) < u32(565)):
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
                        if (u32(v15) < u32(473)):
                            break
                        break
                    arg6 = v23
                    v23 = 0
                    break
                    break
                arg3 = arg0
                break
            v33 = ((3019 if (u32(v15) > u32(555)) else 3011) * arg3)
            break
        v36 = 0
        v9 = load32(v10 + 12)
        v24 = load32(v10 + 16)
        v19 = load32(v10 + 20)
        v14 = load32(v21)
        v22 = load32(v10 + 40)
        v18 = load32(v10 + 84)
        store8(9147212, 1)
        while True:  # $label8
            if (u32(v15) < u32(460)):
                break
            store8(9147208, (load32(v10 + 8) != 0))
            store8(9147209, (load32(v10 + 124) != 0))
            if (u32(v15) < u32(467)):
                break
            break
        store32(9561752, load32(v10 + 72))
        v30 = load32(v10 + 148)
        store32(9561764, 0)
        store32(9142952, load32(v10 + 28))
        store32(9142956, load32(v10 + 32))
        store32(9147220, load32(v10 + 44))
        arg0 = 0
        if not arg5:
            arg0 = load32(v10 + 52)
        store32(59148, arg0)
        store32(9142848, arg0)
        store32(59176, arg0)
        arg0 = load32(v10 + 64)
        store32(9671136, load32(v10 + 64))
        if (u32(load32(9671132)) < u32(arg0)):
            arg0 = (arg0 + 10000)
            store32(9671132, (arg0 + 10000))
            arg4 = load32(ENTITIES)
            v56 = (i32(arg0) * 132)
            arg1 = i32((i32(arg0) * 132))
            arg3 = (i32((i32(arg0) * 132)) + 4)
            arg1 = func26((-1 if i32(((v56 & 0xFFFFFFFF) >> 32)) else (-1 if (u32(arg1) > u32(arg3)) else (i32((i32(arg0) * 132)) + 4))))
            store32(func26((-1 if i32(((v56 & 0xFFFFFFFF) >> 32)) else (-1 if (u32(arg1) > u32(arg3)) else (i32((i32(arg0) * 132)) + 4)))), arg0)
            arg3 = (arg1 + 4)
            if arg0:
                v7 = (arg3 + (arg0 * 132))
                arg0 = arg3
                while True:  # $label9
                    # TODO: memory.fill
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
            store32(ENTITIES, arg3)
        store32(9684364, load32(v10 + 88))
        store32(9684368, load32(v10 + 92))
        store32(9684372, load32(v10 + 96))
        storef32(9684340, loadf32(v10 + 100))
        storef32(9684344, loadf32(v10 + 104))
        storef32(9684348, loadf32(v10 + 108))
        storef32(9684352, loadf32(v10 + 112))
        storef32(9684356, loadf32(v10 + 116))
        storef32(9684360, loadf32(v10 + 120))
        if v23:
            store32(9147312, load32(v10 + 128))
            store32(9147316, load32(v10 + 132))
            store32(9147320, load32(v10 + 136))
            store32(9147324, load32(v10 + 140))
        v16 = ((v9 + v24) + v19)
        v17 = (32 if (u32(v15) < u32(552)) else 64)
        v19 = ((32 if (u32(v15) < u32(552)) else 64) + v14)
        v27 = (((v9 + v24) + v19) + ((32 if (u32(v15) < u32(552)) else 64) + v14))
        arg3 = ((((v9 + v24) + v19) + ((32 if (u32(v15) < u32(552)) else 64) + v14)) + v13)
        while True:  # $label11
            arg0 = load32(v10 + 84)
            if load32(v10 + 84):
                arg1 = load32(GAME_STATE)
                if load32(GAME_STATE):
                    store32(GAME_STATE, 0)
                arg4 = (arg0 << 2)
                arg1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                store32(9142428, arg0)
                store32(GAME_STATE, arg1)
                # TODO: memory.copy
                store32(v11 + 52, arg0)
                store32(v11 + 48, arg1)
                break
            arg0 = load32(GAME_STATE)
            if load32(GAME_STATE):
                store32(GAME_STATE, 0)
            arg0 = func26(188)
            store32(9142428, 47)
            store32(GAME_STATE, arg0)
            # TODO: memory.copy
            break
        arg0 = load32(GAME_STATE)
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
            store32(((load32(38460) * 404) + ENTITY_TYPES) + 244, 0)
            store32(((load32(38672) * 404) + ENTITY_TYPES) + 244, 0)
            store32(((load32(38732) * 404) + ENTITY_TYPES) + 244, 0)
        if v7:
            store32(CURRENT_PLAYER, 0)
        v18 = (arg3 + v18)
        while True:  # $label12
            if not load32(arg0 + 32):
                break
            if load32(9684368):
                break
            store32(9684368, (load32(arg0 + 56) * 1000))
            break
        while True:  # $label13
            if (u32(v15) >= u32(556)):
                v24 = 0
                if v30:
                    break
                if not load32(9142848):
                    break
            v24 = 0
            if (u32((load32(arg0 + 48) - 1)) > u32(1)):
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
                if (u32((arg0 + 1)) < u32((load32(9142440) * arg3))):
                    continue
                break
        if v14:
            arg0 = load32(9681936)
            if not load32(9681936):
                arg0 = func26(16)
                arg1 = (v14 << 2)
                # TODO: i32.div_u
                arg3 = 3
                store32((v14 << 2) + 4, 3)
                store32(arg0, func26((-1 if (u32(arg1) > u32(-1073741825)) else (arg3 << 2))))
                store64(arg0 + 8, 206158430208)
                store32(9681936, arg0)
            arg4 = 0
            while True:  # $label19
                v9 = (v10 + ((arg4 + v17) << 2))
                v25 = load32((v10 + ((arg4 + v17) << 2)))
                while True:  # $label15
                    arg3 = load32(arg0 + 8)
                    if (load32(arg0 + 8) != load32(arg0 + 4)):
                        v7 = load32(arg0)
                        break
                    v7 = (load32(arg0 + 12) + arg3)
                    store32(arg0 + 4, (load32(arg0 + 12) + arg3))
                    arg1 = load32(arg0)
                    v7 = func26((-1 if (u32(v7) > u32(1073741823)) else (v7 << 2)))
                    if arg3:
                        # TODO: memory.copy
                    if arg1:
                        arg3 = load32(arg0 + 8)
                    store32(arg0, v7)
                    break
                arg1 = load32(9681936)
                store32(arg0 + 8, (arg3 + 1))
                store32((v7 + (arg3 << 2)), v25)
                v25 = load32(v9 + 4)
                while True:  # $label16
                    arg3 = load32(arg1 + 8)
                    if (load32(arg1 + 8) != load32(arg1 + 4)):
                        v7 = load32(arg1)
                        break
                    v7 = (load32(arg1 + 12) + arg3)
                    store32(arg1 + 4, (load32(arg1 + 12) + arg3))
                    arg0 = load32(arg1)
                    v7 = func26((-1 if (u32(v7) > u32(1073741823)) else (v7 << 2)))
                    if arg3:
                        # TODO: memory.copy
                    if arg0:
                        arg3 = load32(arg1 + 8)
                    store32(arg1, v7)
                    break
                arg0 = load32(9681936)
                store32(arg1 + 8, (arg3 + 1))
                store32((v7 + (arg3 << 2)), v25)
                v7 = load32(v9 + 8)
                while True:  # $label17
                    arg3 = load32(arg0 + 8)
                    if (load32(arg0 + 8) != load32(arg0 + 4)):
                        v9 = load32(arg0)
                        break
                    v9 = (load32(arg0 + 12) + arg3)
                    store32(arg0 + 4, (load32(arg0 + 12) + arg3))
                    arg1 = load32(arg0)
                    v9 = func26((-1 if (u32(v9) > u32(1073741823)) else (v9 << 2)))
                    if arg3:
                        # TODO: memory.copy
                    if arg1:
                        arg3 = load32(arg0 + 8)
                    store32(arg0, v9)
                    break
                arg1 = load32(9681936)
                store32(arg0 + 8, (arg3 + 1))
                store32((v9 + (arg3 << 2)), v7)
                while True:  # $label18
                    arg3 = load32(arg1 + 8)
                    if (load32(arg1 + 8) != load32(arg1 + 4)):
                        v9 = load32(arg1)
                        break
                    v9 = (load32(arg1 + 12) + arg3)
                    store32(arg1 + 4, (load32(arg1 + 12) + arg3))
                    arg0 = load32(arg1)
                    v9 = func26((-1 if (u32(v9) > u32(1073741823)) else (v9 << 2)))
                    if arg3:
                        # TODO: memory.copy
                    if arg0:
                        arg3 = load32(arg1 + 8)
                    store32(arg1, v9)
                    break
                arg0 = load32(9681936)
                store32(arg1 + 8, (arg3 + 1))
                store32((v9 + (arg3 << 2)), 0)
                arg4 = (arg4 + 3)
                if (u32((arg4 + 3)) < u32(v14)):
                    continue
                break
        v25 = (v8 + v18)
        v31 = ((v8 + v18) + v12)
        v32 = (((v8 + v18) + v12) + (v12 if (u32(v15) > u32(466)) else 0))
        v34 = ((((v8 + v18) + v12) + (v12 if (u32(v15) > u32(466)) else 0)) + v12)
        v9 = (((((v8 + v18) + v12) + (v12 if (u32(v15) > u32(466)) else 0)) + v12) + v12)
        v14 = ((((((v8 + v18) + v12) + (v12 if (u32(v15) > u32(466)) else 0)) + v12) + v12) + v22)
        store32(9142912, arg6)
        while True:  # $label20
            if arg6:
                arg0 = load32(9142908)
                if load32(9142908):
                    store32(9142908, 0)
                arg0 = (arg6 << 2)
                arg1 = func26((-1 if (u32(arg6) > u32(1073741823)) else (arg6 << 2)))
                store32(9142908, func26((-1 if (u32(arg6) > u32(1073741823)) else (arg6 << 2))))
                # TODO: memory.copy
                if not load8u(9687268):
                    break
                break
            if not load8u(9687268):
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
        while True:  # $label21
            if (u32(v15) < u32(460)):
                break
            if not v16:
                break
            v18 = load32(v10 + 16)
            arg0 = load32(9684448)
            arg3 = load32(9684452)
            arg1 = load32(v10 + 12)
            if (u32(load32(9684448)) <= u32((load32(9684452) + load32(v10 + 12)))):
                arg4 = (load32(9684456) + (arg0 + arg1))
                store32(9684448, (load32(9684456) + (arg0 + arg1)))
                arg0 = load32(9684444)
                arg4 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                if arg3:
                    # TODO: memory.copy
                if arg0:
                store32(9684444, arg4)
            while True:  # $label22
                if not arg1:
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
                if not (arg1 & 1):
                    break
                arg0 = load32((arg3 + (arg0 << 2)))
                arg3 = load32(9684452)
                store32(9684452, (load32(9684452) + 1))
                store32((v8 + (arg3 << 2)), arg0)
                break
            arg0 = load32(9684464)
            arg4 = load32(9684468)
            arg3 = load32(v10 + 16)
            if (u32(load32(9684464)) <= u32((load32(9684468) + load32(v10 + 16)))):
                v8 = (load32(9684472) + (arg0 + arg3))
                store32(9684464, (load32(9684472) + (arg0 + arg3)))
                arg0 = load32(9684460)
                v8 = func26((-1 if (u32(v8) > u32(1073741823)) else (v8 << 2)))
                if arg4:
                    # TODO: memory.copy
                if arg0:
                store32(9684460, v8)
            v19 = (arg1 + v19)
            while True:  # $label24
                if not arg3:
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
                if not (arg3 & 1):
                    break
                arg0 = load32((arg1 + (arg0 << 2)))
                arg1 = load32(9684468)
                store32(9684468, (load32(9684468) + 1))
                store32((v8 + (arg1 << 2)), arg0)
                break
            arg0 = load32(9684480)
            arg3 = load32(9684484)
            arg1 = load32(v10 + 20)
            if (u32(load32(9684480)) <= u32((load32(9684484) + load32(v10 + 20)))):
                arg4 = (load32(9684488) + (arg0 + arg1))
                store32(9684480, (load32(9684488) + (arg0 + arg1)))
                arg0 = load32(9684476)
                arg4 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                if arg3:
                    # TODO: memory.copy
                if arg0:
                store32(9684476, arg4)
            if not arg1:
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
            if not (arg1 & 1):
                break
            arg0 = load32((arg3 + (arg0 << 2)))
            arg1 = load32(9684484)
            store32(9684484, (load32(9684484) + 1))
            store32((v8 + (arg1 << 2)), arg0)
            break
        v19 = (arg6 + v14)
        while True:  # $label27
            if not v24:
                break
            arg0 = 0
            store8(9142904, 1)
            arg1 = load32(9142440)
            arg1 = (load32(9142440) * arg1)
            arg3 = ((load32(9142440) * arg1) + 2)
            arg4 = func26((-1 if (arg3 < 0) else (((load32(9142440) * arg1) + 2) << 1)))
            store32(9147376, func26((-1 if (arg3 < 0) else (((load32(9142440) * arg1) + 2) << 1))))
            if not arg1:
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
            if not (arg1 & 1):
                break
            store16((arg4 + (arg0 << 1)), (((load32((v7 + (((arg0 & 0xFFFFFFFF) >> 3) & 536870908))) & 0xFFFFFFFF) >> arg0) & 1))
            break
        while True:  # $label71
            while True:  # $label90
                while True:  # $label44
                    while True:  # $label42
                        if v13:
                            arg3 = (v10 + (v27 << 2))
                            arg6 = (v11 + 288)
                            v27 = (u32(v15) > u32(563))
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
                                while True:  # $label29
                                    if not arg1:
                                        break
                                    v17 = (arg1 & 3)
                                    v8 = 0
                                    while True:  # $label30
                                        if (u32(arg1) < u32(4)):
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
                                    if not v17:
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
                                while True:  # $label38
                                    while True:  # $label40
                                        while True:  # $label36
                                            while True:  # $label33
                                                if not v18:
                                                    break
                                                while True:  # $label37
                                                    while True:  # $label35
                                                        func381((v11 + 68), arg3, (v11 + 392), 1, v15)
                                                        while True:  # $label34
                                                            arg0 = load32(v11 + 268)
                                                            v8 = load32(v11 + 272)
                                                            if (u32(load32(v11 + 268)) < u32(load32(v11 + 272))):
                                                                # TODO: memory.copy
                                                                store32(v11 + 268, (arg0 + 196))
                                                                break
                                                            arg0 = load32(v11 + 264)
                                                            v7 = (arg0 - load32(v11 + 264))
                                                            v14 = ((arg0 - load32(v11 + 264)) // 196)
                                                            arg1 = (((arg0 - load32(v11 + 264)) // 196) + 1)
                                                            if (u32((((arg0 - load32(v11 + 264)) // 196) + 1)) >= u32(21913099)):
                                                                break
                                                            v8 = ((v8 - arg0) // 196)
                                                            v17 = (((v8 - arg0) // 196) << 1)
                                                            arg1 = (21913098 if (u32(v8) >= u32(10956549)) else ((((v8 - arg0) // 196) << 1) if (u32(arg1) < u32(v17)) else arg1))
                                                            if (21913098 if (u32(v8) >= u32(10956549)) else ((((v8 - arg0) // 196) << 1) if (u32(arg1) < u32(v17)) else arg1)):
                                                                if (u32(arg1) >= u32(21913099)):
                                                                    break
                                                            else:
                                                            v17 = 0
                                                            v8 = (0 + (v14 * 196))
                                                            # TODO: memory.copy
                                                            v14 = (v8 + ((v7 // -196) * 196))
                                                            # TODO: memory.copy
                                                            store32(v11 + 272, (v17 + (arg1 * 196)))
                                                            store32(v11 + 268, (v8 + 196))
                                                            store32(v11 + 264, v14)
                                                            if not arg0:
                                                                break
                                                            break
                                                        arg4 = (arg4 + 1)
                                                        if (v18 != (arg4 + 1)):
                                                            continue
                                                        break
                                                        break
                                                    break
                                                func42()
                                                raise Unreachable()
                                                break
                                            arg4 = 0
                                            if not v16:
                                                break
                                            while True:  # $label41
                                                func381((v11 + 68), arg3, (v11 + 392), 0, v15)
                                                while True:  # $label39
                                                    arg0 = load32(v11 + 280)
                                                    v8 = load32(v11 + 284)
                                                    if (u32(load32(v11 + 280)) < u32(load32(v11 + 284))):
                                                        # TODO: memory.copy
                                                        store32(v11 + 280, (arg0 + 196))
                                                        break
                                                    arg0 = load32(v11 + 276)
                                                    v7 = (arg0 - load32(v11 + 276))
                                                    v14 = ((arg0 - load32(v11 + 276)) // 196)
                                                    arg1 = (((arg0 - load32(v11 + 276)) // 196) + 1)
                                                    if (u32((((arg0 - load32(v11 + 276)) // 196) + 1)) >= u32(21913099)):
                                                        break
                                                    v8 = ((v8 - arg0) // 196)
                                                    v18 = (((v8 - arg0) // 196) << 1)
                                                    arg1 = (21913098 if (u32(v8) >= u32(10956549)) else ((((v8 - arg0) // 196) << 1) if (u32(arg1) < u32(v18)) else arg1))
                                                    if (21913098 if (u32(v8) >= u32(10956549)) else ((((v8 - arg0) // 196) << 1) if (u32(arg1) < u32(v18)) else arg1)):
                                                        if (u32(arg1) >= u32(21913099)):
                                                            break
                                                    else:
                                                    v18 = 0
                                                    v8 = (0 + (v14 * 196))
                                                    # TODO: memory.copy
                                                    v14 = (v8 + ((v7 // -196) * 196))
                                                    # TODO: memory.copy
                                                    store32(v11 + 284, (v18 + (arg1 * 196)))
                                                    store32(v11 + 280, (v8 + 196))
                                                    store32(v11 + 276, v14)
                                                    if not arg0:
                                                        break
                                                    break
                                                arg4 = (arg4 + 1)
                                                if (v16 != (arg4 + 1)):
                                                    continue
                                                break
                                            break
                                            break
                                        func68()
                                        raise Unreachable()
                                        break
                                    func42()
                                    raise Unreachable()
                                    break
                                while True:  # $label46
                                    v7 = load32(9568068)
                                    if (load32(9568068) != load32(9568072)):
                                        store32(v7 + 8, 0)
                                        store64(v7, 0)
                                        arg0 = load32(v11 + 268)
                                        arg4 = load32(v11 + 264)
                                        v8 = (load32(v11 + 268) - load32(v11 + 264))
                                        arg1 = ((load32(v11 + 268) - load32(v11 + 264)) // 196)
                                        if (arg0 != arg4):
                                            if (u32(arg1) >= u32(21913099)):
                                                break
                                            arg0 = func26(v8)
                                            store32(v7 + 4, func26(v8))
                                            store32(v7, arg0)
                                            store32(v7 + 8, (arg0 + (arg1 * 196)))
                                            arg1 = load32(v11 + 264)
                                            arg4 = load32(v11 + 268)
                                            if (load32(v11 + 264) != load32(v11 + 268)):
                                                while True:  # $label43
                                                    # TODO: memory.copy
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
                                            if (u32(arg1) >= u32(21913099)):
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
                                                    # TODO: memory.copy
                                                    arg0 = (arg0 + 196)
                                                    arg1 = (arg1 + 196)
                                                    if ((arg1 + 196) != arg4):
                                                        continue
                                                    break
                                            store32(v7 + 16, arg0)
                                        # TODO: memory.copy
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
                                if (u32(load32(v11 + 392)) < u32(v13)):
                                    continue
                                break
                        arg0 = 0
                        arg1 = func26(v12)
                        # TODO: memory.fill
                        store32(9143004, arg1)
                        arg1 = func26(v12)
                        # TODO: memory.fill
                        store32(9143012, arg1)
                        arg1 = func26(v12)
                        # TODO: memory.fill
                        store32(9143008, arg1)
                        arg1 = func26(v12)
                        # TODO: memory.fill
                        store32(9143016, arg1)
                        if v12:
                            arg1 = (u32(v15) < u32(467))
                            while True:  # $label48
                                store8((load32(9143004) + arg0), (load32((v10 + ((arg0 + v25) << 2))) != 0))
                                if not arg1:
                                    store8((load32(9143012) + arg0), (load32((v10 + ((arg0 + v32) << 2))) != 0))
                                store8((load32(9143016) + arg0), load32((v10 + ((arg0 + v34) << 2))))
                                store8((load32(9143008) + arg0), (load32((v10 + ((arg0 + v31) << 2))) != 0))
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != v12):
                                    continue
                                break
                        arg4 = load32(PLAYER_COUNT)
                        if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                            v12 = (arg4 + 1)
                            arg0 = (arg4 - 1)
                            v7 = ((arg4 - 1) & -4)
                            arg6 = (arg0 & 3)
                            v13 = (u32((arg4 - 2)) < u32(3))
                            arg1 = 1
                            while True:  # $label53
                                arg3 = 0
                                v8 = (load32(9143012) + (arg1 * v12))
                                arg0 = 1
                                if not v13:
                                    while True:  # $label51
                                        while True:  # $label50
                                            while True:  # $label49
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
                        while True:  # $label54
                            if (u32(v15) > u32(466)):
                                break
                            arg0 = 0
                            arg3 = (arg4 * arg4)
                            arg1 = func26((arg4 * arg4))
                            # TODO: memory.fill
                            store32(9143012, arg1)
                            if not arg3:
                                break
                            v7 = (arg3 & 3)
                            arg6 = load32(9143004)
                            if (u32(arg3) >= u32(4)):
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
                            if not v7:
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
                        if (u32(load32(9215888)) <= u32(arg1)):
                            arg0 = (arg1 + 1024)
                            store32(9215888, (arg1 + 1024))
                            arg3 = load32(9215884)
                            arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                            if arg3:
                            store32(9215884, arg0)
                        v14 = (v19 + v24)
                        v33 = ((v19 + v24) + v33)
                        arg6 = 0
                        while True:  # $label57
                            if not load32(9142848):
                                store32(9215892, 4)
                                v24 = 1
                                break
                            if not arg1:
                                v24 = 1
                                break
                            v7 = (arg1 & 3)
                            arg3 = 0
                            arg6 = load32(9215884)
                            arg0 = 0
                            if (u32(arg1) >= u32(4)):
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
                            v24 = not arg1
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
                        v13 = (253 if (u32(v15) < u32(552)) else 255)
                        v8 = 0
                        arg1 = load32(PLAYER_COUNT)
                        while True:  # $label60
                            if v29:
                                if not arg1:
                                    break
                                arg0 = (v20 + v22)
                                while True:  # $label68
                                    v7 = load32(PLAYERS)
                                    if not v30:
                                        arg3 = (v7 + (v8 * 286704))
                                        arg1 = (arg1 * v13)
                                        arg1 = (-1 if (u32(arg1) > u32(1073741823)) else ((arg1 * v13) << 2))
                                        store32((v7 + (v8 * 286704)) + 278556, func26((-1 if (u32(arg1) > u32(1073741823)) else ((arg1 * v13) << 2))))
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
                                            v18 = load32(PLAYER_COUNT)
                                            if (u32((arg1 + 1)) < u32((load32(PLAYER_COUNT) * 255))):
                                                continue
                                            break
                                        while True:  # $label62
                                            if not v18:
                                                break
                                            arg4 = load32(arg4)
                                            arg1 = 0
                                            while True:  # $label63
                                                store32((arg4 + (arg1 << 2)), load32((v10 + (arg0 << 2))))
                                                arg0 = (arg0 + 1)
                                                arg1 = (arg1 + 1)
                                                v19 = load32(PLAYER_COUNT)
                                                if (u32((arg1 + 1)) < u32((load32(PLAYER_COUNT) * 255))):
                                                    continue
                                                break
                                            if not v19:
                                                break
                                            v9 = load32(v9)
                                            arg1 = 0
                                            while True:  # $label64
                                                store32((v9 + (arg1 << 2)), load32((v10 + (arg0 << 2))))
                                                arg0 = (arg0 + 1)
                                                arg1 = (arg1 + 1)
                                                v19 = load32(PLAYER_COUNT)
                                                arg4 = (load32(PLAYER_COUNT) * 255)
                                                if (u32((arg1 + 1)) < u32((load32(PLAYER_COUNT) * 255))):
                                                    continue
                                                break
                                            if not v19:
                                                break
                                            arg1 = (1 if (u32(arg4) <= u32(1)) else arg4)
                                            # TODO: memory.copy
                                            arg0 = (arg0 + arg1)
                                            break
                                        v12 = (arg0 << 2)
                                        arg1 = load32((v10 + (arg0 << 2)))
                                        arg4 = func26(16)
                                        v9 = (arg1 + 21000)
                                        store32(func26(16) + 4, (arg1 + 21000))
                                        v9 = func26((-1 if (u32(v9) > u32(1073741823)) else (v9 << 2)))
                                        store32(arg4 + 12, 21000)
                                        store32(arg4, v9)
                                        store32((arg3 + 278572), arg4)
                                        arg0 = (arg0 + 1)
                                        if arg1:
                                            # TODO: memory.copy
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
                                    if not arg5:
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
                                    arg1 = load32(PLAYER_COUNT)
                                    if (u32((v8 + 1)) < u32(load32(PLAYER_COUNT))):
                                        continue
                                    break
                                break
                            if not arg1:
                                break
                            arg0 = 0
                            while True:  # $label69
                                func239(arg0)
                                arg0 = (arg0 + 1)
                                if (u32((arg0 + 1)) < u32(load32(PLAYER_COUNT))):
                                    continue
                                break
                            break
                        arg1 = load32(PLAYERS)
                        arg0 = 39
                        while True:  # $label70
                            arg3 = (arg0 << 2)
                            arg4 = ((arg1 + (arg0 << 2)) + 283984)
                            if not load32(((arg1 + (arg0 << 2)) + 283984)):
                                store32(arg4, load32((arg3 + 9561072)))
                            arg3 = ((arg0 + 1) << 2)
                            arg4 = ((arg1 + ((arg0 + 1) << 2)) + 283984)
                            if not load32(((arg1 + ((arg0 + 1) << 2)) + 283984)):
                                store32(arg4, load32((arg3 + 9561072)))
                            arg0 = (arg0 + 2)
                            if ((arg0 + 2) != 155):
                                continue
                            break
                        v12 = (u32(v15) < u32(552))
                        if (u32((u32(v15) < u32(552))) >= u32(load32(PLAYER_COUNT))):
                            break
                        arg0 = (v10 + (v14 << 2))
                        v21 = (v13 & 3)
                        v14 = (155 if (u32(v15) > u32(481)) else 40)
                        v34 = ((155 if (u32(v15) > u32(481)) else 40) & 184)
                        v19 = (v14 & 3)
                        v18 = (u32(v15) < u32(473))
                        v26 = (u32(v15) < u32(482))
                        v37 = (u32(v15) < u32(491))
                        v38 = (u32(v15) < u32(556))
                        arg3 = 0
                        while True:  # $label89
                            v7 = players[v12]
                            store32(players[v12] + 283908, v12)
                            arg1 = ((arg3 << 2) + arg0)
                            while True:  # $label72
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
                            while True:  # $label73
                                arg4 = load32(arg1 + 40)
                                if not load32(arg1 + 40):
                                    break
                                if arg5:
                                    break
                                v16 = (v10 + (arg4 << 2))
                                arg4 = load32((v10 + (arg4 << 2)))
                                v8 = func26(16)
                                store32(func26(16) + 4, arg4)
                                v17 = (arg4 << 2)
                                v9 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                                store32(v8 + 12, 20)
                                store32(v8, v9)
                                store32(v8 + 8, arg4)
                                if arg4:
                                    # TODO: memory.copy
                                store32(v7 + 281788, v8)
                                break
                            while True:  # $label74
                                arg4 = load32(arg1 + 44)
                                if not load32(arg1 + 44):
                                    break
                                if arg5:
                                    break
                                v16 = (v10 + (arg4 << 2))
                                arg4 = load32((v10 + (arg4 << 2)))
                                v8 = func26(16)
                                v9 = (arg4 + 8)
                                store32(func26(16) + 4, (arg4 + 8))
                                v9 = func26((-1 if (u32(v9) > u32(1073741823)) else (v9 << 2)))
                                store32(v8 + 12, 20)
                                store32(v8, v9)
                                store32(v8 + 8, arg4)
                                if arg4:
                                    # TODO: memory.copy
                                store32(v7 + 281792, v8)
                                break
                            v9 = (arg3 + 12)
                            if not v18:
                                while True:  # $label75
                                    arg4 = load32((arg0 + (v9 << 2)))
                                    if not load32((arg0 + (v9 << 2))):
                                        break
                                    if arg5:
                                        break
                                    v16 = (v10 + (arg4 << 2))
                                    arg4 = load32((v10 + (arg4 << 2)))
                                    v8 = func26(16)
                                    store32(func26(16) + 4, arg4)
                                    v17 = (arg4 << 2)
                                    v9 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                                    store32(v8 + 12, 20)
                                    store32(v8, v9)
                                    store32(v8 + 8, arg4)
                                    if arg4:
                                        # TODO: memory.copy
                                    store32(v7 + 281796, v8)
                                    break
                                arg1 = load32(arg1 + 52)
                                if load32(arg1 + 52):
                                    v9 = (v10 + (arg1 << 2))
                                    arg1 = load32((v10 + (arg1 << 2)))
                                    arg4 = func26(16)
                                    store32(func26(16) + 4, arg1)
                                    v16 = (arg1 << 2)
                                    v8 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                                    store32(arg4 + 12, 20)
                                    store32(arg4, v8)
                                    store32(arg4 + 8, arg1)
                                    if arg1:
                                        # TODO: memory.copy
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
                            if not arg5:
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
                            while True:  # $label86
                                while True:  # $label85
                                    while True:  # $label84
                                        if not v37:
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
                                while True:  # $label87
                                    if not v30:
                                        if not load8u(9561832):
                                            break
                                    store32(arg4, load32(arg3 + 24))
                                    break
                                store8(v7 + 286700, (load32(arg3 + 28) != 0))
                                store8(v7 + 286701, (load32(arg3 + 32) != 0))
                                arg3 = (arg1 + 9)
                            if not v38:
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
                            while True:  # $label88
                                if not v36:
                                    arg4 = arg3
                                    break
                                arg4 = (arg3 + 1)
                                arg3 = load32((arg0 + (arg3 << 2)))
                                if not load32((arg0 + (arg3 << 2))):
                                    break
                                if arg5:
                                    break
                                arg1 = load32(PLAYER_COUNT)
                                v8 = (load32(PLAYER_COUNT) << 2)
                                v9 = func26((-1 if (u32(arg1) > u32(1073741823)) else (load32(PLAYER_COUNT) << 2)))
                                store32(v7 + 281800, func26((-1 if (u32(arg1) > u32(1073741823)) else (load32(PLAYER_COUNT) << 2))))
                                if not arg1:
                                    break
                                # TODO: memory.copy
                                break
                            arg1 = (arg0 + (arg4 << 2))
                            store32(v7 + 284608, load32((arg0 + (arg4 << 2))))
                            store32(v7 + 286684, load32(arg1 + 4))
                            store8(v7 + 286696, (load32(arg1 + 8) != 0))
                            if not arg5:
                                store32(v7 + 283976, load32(arg1 + 12))
                            store32(v7 + 283980, load32(arg1 + 16))
                            store32(v7 + 286688, load32(arg1 + 20))
                            store32(v7 + 283896, load32(arg1 + 24))
                            store32(v7 + 283900, load32(arg1 + 28))
                            if arg5:
                                store8(v7 + 286699, 1)
                            arg3 = (arg4 + 8)
                            v12 = (v12 + 1)
                            if (u32((v12 + 1)) < u32(load32(PLAYER_COUNT))):
                                continue
                            break
                        break
                        break
                    func42()
                    raise Unreachable()
                    break
                func42()
                raise Unreachable()
                break
            arg1 = load32(PLAYERS)
            break
        store16(arg1 + 283972, 65535)
        store8((arg1 + 283974), 255)
        arg0 = ((25 if (u32(v15) < u32(473)) else 30) if (u32(v15) < u32(552)) else (33 if (u32(v15) > u32(581)) else 32))
        # TODO: i32.div_u
        v8 = ((25 if (u32(v15) < u32(473)) else 30) if (u32(v15) < u32(552)) else (33 if (u32(v15) > u32(581)) else 32))
        if arg5:
            arg1 = load32(9671136)
            v7 = func26((-1 if (u32(arg1) > u32(1073741823)) else (load32(9671136) << 2)))
        arg4 = 3
        if (u32(arg0) <= u32(v20)):
            v9 = (v10 + (v22 << 2))
            v19 = (1 if (u32(v8) <= u32(1)) else v8)
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
            v54 = (u32(v15) < u32(473))
            v55 = (u32(v15) < u32(582))
            arg0 = 0
            while True:  # $label99
                while True:  # $label91
                    arg3 = load32((v9 + ((arg0 + v52) << 2)))
                    if not load32((v9 + ((arg0 + v52) << 2))):
                        break
                    if (u32(arg3) >= u32(v12)):
                        break
                    v20 = (v9 + ((arg0 + v53) << 2))
                    arg1 = load32((v9 + ((arg0 + v53) << 2)))
                    v14 = ((load32((v9 + ((arg0 + v53) << 2))) & 0xFFFFFFFF) >> 24)
                    if (arg5 & (((load32((v9 + ((arg0 + v53) << 2))) & 0xFFFFFFFF) >> 24) == 3)):
                        break
                    v21 = load32((v9 + ((arg0 + v51) << 2)))
                    if (arg5 & not load32((v9 + ((arg0 + v51) << 2)))):
                        break
                    while True:  # $label92
                        if not arg5:
                            break
                        if not load32(9147132):
                            break
                        if (load32(38788) != (arg1 & 255)):
                            break
                        if (u32(load32((v9 + ((arg0 + v30) << 2)))) > u32(2002)):
                            break
                        break
                    while True:  # $label93
                        if not arg5:
                            arg1 = arg4
                            arg4 = arg3
                            break
                        store32((v7 + (arg3 << 2)), arg4)
                        arg1 = (arg4 + 1)
                        break
                    arg3 = entities[arg4]
                    store32(entities[arg4].max_hp, arg4)
                    arg4 = load32((v9 + (arg0 << 2)))
                    if load32((v9 + (arg0 << 2))):
                        v22 = (v10 + (arg4 << 2))
                        arg4 = load32((v10 + (arg4 << 2)))
                        v12 = func26(16)
                        store32(func26(16) + 4, arg4)
                        v28 = (arg4 << 2)
                        v13 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                        store32(v12 + 12, 20)
                        store32(v12, v13)
                        store32(v12 + 8, arg4)
                        if arg4:
                            # TODO: memory.copy
                        store32(arg3 + 16, v12)
                    arg4 = load32((v9 + ((arg0 + v8) << 2)))
                    if load32((v9 + ((arg0 + v8) << 2))):
                        v22 = (v10 + (arg4 << 2))
                        arg4 = load32((v10 + (arg4 << 2)))
                        v12 = func26(16)
                        store32(func26(16) + 4, arg4)
                        v28 = (arg4 << 2)
                        v13 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                        store32(v12 + 12, 20)
                        store32(v12, v13)
                        store32(v12 + 8, arg4)
                        if arg4:
                            # TODO: memory.copy
                        store32(arg3 + 20, v12)
                    arg4 = load32((v9 + ((arg0 + v50) << 2)))
                    if load32((v9 + ((arg0 + v50) << 2))):
                        v22 = (v10 + (arg4 << 2))
                        arg4 = load32((v10 + (arg4 << 2)))
                        if not load32(arg3 + 24):
                            v12 = func26(16)
                            store64(func26(16), 0)
                            store64(v12 + 8, 0)
                            store32(arg3 + 24, v12)
                        v12 = func26(16)
                        store32(func26(16) + 4, arg4)
                        v28 = (arg4 << 2)
                        v13 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                        store32(v12 + 12, 20)
                        store32(v12, v13)
                        store32(v12 + 8, arg4)
                        if arg4:
                            # TODO: memory.copy
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
                    while True:  # $label94
                        if not load8u(9142916):
                            break
                        v13 = (((arg4 & 0xFFFFFFFF) >> 8) & 255)
                        if (u32((((arg4 & 0xFFFFFFFF) >> 8) & 255)) > u32(12)):
                            break
                        if not ((1 << v13) & 7184):
                            break
                        store8(arg3 + 127, 0)
                        break
                    store8(arg3 + 129, ((arg4 & 0xFFFFFFFF) >> 24))
                    store8(arg3 + 128, ((arg4 & 0xFFFFFFFF) >> 16))
                    while True:  # $label95
                        if v54:
                            break
                        store32(arg3 + 96, load32((v9 + ((arg0 + v32) << 2))))
                        store32(arg3 + 56, load32((v9 + ((arg0 + v31) << 2))))
                        arg4 = load32((v9 + ((arg0 + v25) << 2)))
                        if load32((v9 + ((arg0 + v25) << 2))):
                            v14 = (v10 + (arg4 << 2))
                            arg4 = load32((v10 + (arg4 << 2)))
                            if not load32(arg3 + 24):
                                v13 = func26(16)
                                store64(func26(16), 0)
                                store64(v13 + 8, 0)
                                store32(arg3 + 24, v13)
                            v13 = func26(16)
                            store32(func26(16) + 4, arg4)
                            v21 = (arg4 << 2)
                            v20 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                            store32(v13 + 12, 20)
                            store32(v13, v20)
                            store32(v13 + 8, arg4)
                            if arg4:
                                # TODO: memory.copy
                            store32(load32(arg3 + 24) + 12, v13)
                        arg4 = load32((v9 + ((arg0 + v27) << 2)))
                        if load32((v9 + ((arg0 + v27) << 2))):
                            v14 = (v10 + (arg4 << 2))
                            arg4 = load32((v10 + (arg4 << 2)))
                            if not load32(arg3 + 24):
                                v13 = func26(16)
                                store64(func26(16), 0)
                                store64(v13 + 8, 0)
                                store32(arg3 + 24, v13)
                            v13 = func26(16)
                            store32(func26(16) + 4, arg4)
                            v21 = (arg4 << 2)
                            v20 = func26((-1 if (u32(arg4) > u32(1073741823)) else (arg4 << 2)))
                            store32(v13 + 12, 20)
                            store32(v13, v20)
                            store32(v13 + 8, arg4)
                            if arg4:
                                # TODO: memory.copy
                            store32(load32(arg3 + 24) + 8, v13)
                        while True:  # $label96
                            arg4 = load32((v9 + ((arg0 + v29) << 2)))
                            if not load32((v9 + ((arg0 + v29) << 2))):
                                break
                            v14 = (v10 + (arg4 << 2))
                            v13 = load32((v10 + (arg4 << 2)))
                            if not load32(arg3 + 24):
                                arg4 = func26(16)
                                store64(func26(16), 0)
                                store64(arg4 + 8, 0)
                                store32(arg3 + 24, arg4)
                            arg4 = func26(16)
                            store32(func26(16) + 4, v13)
                            v21 = (v13 << 2)
                            v20 = func26((-1 if (u32(v13) > u32(1073741823)) else (v13 << 2)))
                            store32(arg4 + 12, 20)
                            store32(arg4, v20)
                            store32(arg4 + 8, v13)
                            if not v13:
                                store32(load32(arg3 + 24) + 4, arg4)
                                break
                            # TODO: memory.copy
                            store32(load32(arg3 + 24) + 4, arg4)
                            v22 = ((((v13 - 1) & 0xFFFFFFFF) >> 1) + 1)
                            v21 = (((((v13 - 1) & 0xFFFFFFFF) >> 1) + 1) & 3)
                            v14 = 0
                            arg4 = 0
                            if (u32(v13) >= u32(7)):
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
                            if not v21:
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
        while True:  # $label100
            if load32(9142848):
                break
            if (u32(v15) > u32(518)):
                break
            if not v24:
                arg1 = load32(9215884)
                arg0 = 0
                while True:  # $label101
                    arg3 = (arg0 << 2)
                    if (load32((arg1 + ((arg0 << 2) | 4))) == 22):
                        store32((arg1 + arg3), 0)
                    arg0 = (arg0 + 4)
                    if (u32((arg0 + 4)) < u32(arg6)):
                        continue
                    break
            arg0 = load32(9671136)
            if (u32(load32(9671136)) < u32(4)):
                break
            v23 = (arg0 - 3)
            arg3 = ((arg0 - 3) & 7)
            arg6 = load32(ENTITIES)
            arg1 = 3
            if (u32((arg0 - 4)) >= u32(7)):
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
            if not arg3:
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
            v23 = load32(ENTITIES)
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
                    store32(arg0 + 68, load32(((load32(38448) * 404) + ENTITY_TYPES) + 104))
                    store8(arg0 + 124, load32((arg3 + (arg6 | 8))))
                    store32(arg0 + 112, load32((arg3 + (arg6 | 12))))
                    store8(arg0 + 122, load32(38448))
                arg1 = (arg1 + 4)
                if (u32((arg1 + 4)) < u32(v35)):
                    continue
                break
        while True:  # $label105
            if not arg5:
                break
            store32(9671136, arg4)
            if (u32(arg4) >= u32(4)):
                arg3 = load32(ENTITIES)
                v9 = 3
                while True:  # $label108
                    arg0 = (arg3 + (v9 * 132))
                    arg1 = load32((arg3 + (v9 * 132)) + 36)
                    if load32((arg3 + (v9 * 132)) + 36):
                        store32(arg0 + 36, load32((v7 + (arg1 << 2))))
                    while True:  # $label106
                        arg1 = load32(arg0 + 16)
                        if not load32(arg0 + 16):
                            break
                        if not load32(arg1 + 8):
                            break
                        arg4 = load32(arg1)
                        arg0 = 0
                        while True:  # $label107
                            arg5 = (arg4 + (arg0 << 2))
                            store32((arg4 + (arg0 << 2)), load32((v7 + (load32(arg5) << 2))))
                            arg0 = (arg0 + 1)
                            if (u32((arg0 + 1)) < u32(load32(arg1 + 8))):
                                continue
                            break
                        arg4 = load32(9671136)
                        break
                    v9 = (v9 + 1)
                    if (u32((v9 + 1)) < u32(arg4)):
                        continue
                    break
            if not v7:
                break
            break
        v7 = 1
        if not arg2:
            break
        store32(v11 + 32, (load32(PLAYER_COUNT) - 1))
        while True:  # $label109
            arg3 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            arg0 = load32(PLAYERS)
            if not load32((load32(PLAYERS) + 570612)):
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
                arg3 = load32(PLAYER_COUNT)
                if (u32((arg1 + 1)) >= u32(load32(PLAYER_COUNT))):
                    break
                arg0 = load32(PLAYERS)
                if load32(players[arg1] + 283908):
                    continue
                break
            break
        store32(v11, (arg3 - 1))
        break
    G.global0 = (v11 + 400)
    return v7

# ----------------------------------------------------------
# $Fb
# Export: Fb
# ----------------------------------------------------------
def Fb():
    """Export: Fb"""
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store64(v5 + 20, 0)
    store32(v5 + 28, 0)
    v8 = load32(9687244)
    v0 = (load32(9687244) + load32(9687248))
    if (load32(9687244) + load32(9687248)):
        while True:  # $label0
            v3 = load32(v5 + 28)
            v8 = load32(v5 + 24)
            if (u32(v0) <= u32(((load32(v5 + 28) - load32(v5 + 24)) // 20))):
                if v0:
                    v0 = ((v0 * 20) - 20)
                    v0 = ((((v0 * 20) - 20) - (v0 % 20)) + 20)
                    # TODO: memory.fill
                else:
                store32((v0 + v8) + 24, v8)
                break
            while True:  # $label1
                v8 = load32(v5 + 20)
                v4 = (v8 - load32(v5 + 20))
                v6 = ((v8 - load32(v5 + 20)) // 20)
                v2 = (((v8 - load32(v5 + 20)) // 20) + v0)
                if (u32((((v8 - load32(v5 + 20)) // 20) + v0)) < u32(214748365)):
                    v3 = ((v3 - v8) // 20)
                    v7 = (((v3 - v8) // 20) << 1)
                    v2 = (214748364 if (u32(v3) >= u32(107374182)) else ((((v3 - v8) // 20) << 1) if (u32(v2) < u32(v7)) else v2))
                    if (214748364 if (u32(v3) >= u32(107374182)) else ((((v3 - v8) // 20) << 1) if (u32(v2) < u32(v7)) else v2)):
                        if (u32(v2) >= u32(214748365)):
                            break
                        v9 = func26((v2 * 20))
                    v3 = ((v6 * 20) + v9)
                    v0 = ((v0 * 20) - 20)
                    v0 = ((((v0 * 20) - 20) - (v0 % 20)) + 20)
                    # TODO: memory.fill
                    v6 = (v3 + ((v4 // -20) * 20))
                    # TODO: memory.copy
                    store32(v5 + 28, (v9 + (v2 * 20)))
                    store32(v5 + 24, (v0 + v3))
                    store32(v5 + 20, v6)
                    if v8:
                    break
                func42()
                raise Unreachable()
                break
            func68()
            raise Unreachable()
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
            if (u32((v1 + 1)) < u32(load32(9687244))):
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
            if (u32((v8 + 1)) < u32(load32(9687248))):
                continue
            break
    store32(v5 + 16, 0)
    store64(v5 + 8, 0)
    while True:  # $label4
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
            # TODO: i32.div_u
            v6 = (v6 * v7)
            if v0:
                v0 = (v0 + v8)
                while True:  # $label9
                    while True:  # $label7
                        while True:  # $label8
                            while True:  # $label6
                                v7 = (v8 * 3)
                                v10 = load32(v2)
                                while True:  # $label5
                                    v3 = load32(v5 + 16)
                                    if (u32(load32(v5 + 16)) > u32(v1)):
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
                                    if (u32((((v1 - load32(v5 + 8)) // 28) + 1)) >= u32(153391690)):
                                        break
                                    v3 = ((v3 - v4) // 28)
                                    v14 = (((v3 - v4) // 28) << 1)
                                    v3 = (153391689 if (u32(v3) >= u32(76695844)) else ((((v3 - v4) // 28) << 1) if (u32(v1) < u32(v14)) else v1))
                                    if (153391689 if (u32(v3) >= u32(76695844)) else ((((v3 - v4) // 28) << 1) if (u32(v1) < u32(v14)) else v1)):
                                        if (u32(v3) >= u32(153391690)):
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
                                    # TODO: memory.copy
                                    store32(v5 + 16, (v14 + (v3 * 28)))
                                    v1 = (v1 + 28)
                                    store32(v5 + 12, (v1 + 28))
                                    store32(v5 + 8, v7)
                                    if not v4:
                                        break
                                    break
                                v8 = (v8 + 1)
                                if (v0 != (v8 + 1)):
                                    continue
                                break
                                break
                            break
                        func42()
                        raise Unreachable()
                        break
                    func68()
                    raise Unreachable()
                    break
                v3 = load32(v5 + 20)
                v4 = load32(v5 + 24)
                v8 = v0
            v9 = (v9 + 1)
            if (u32((v9 + 1)) < u32(((v4 - v3) // 20))):
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
    v19 = func26((-1 if (u32((v1 * 3)) > u32(1073741823)) else (((load32(v5 + 12) - load32(v5 + 8)) // 28) * 12)))
    store32(9687240, func26((-1 if (u32((v1 * 3)) > u32(1073741823)) else (((load32(v5 + 12) - load32(v5 + 8)) // 28) * 12))))
    store32(v2 + 20, 0)
    store64(v2 + 12, 0)
    v9 = load32(v5 + 8)
    v20 = load32(v5 + 12)
    if (load32(v5 + 8) != load32(v5 + 12)):
        while True:  # $label28
            while True:  # $label27
                while True:  # $label11
                    v7 = (load32(v9 + 8) + 8)
                    v15 = load32(v2 + 28)
                    if ((load32(v9 + 8) + 8) > load32(v2 + 28)):
                        break
                    v10 = (load32(v9 + 12) + 8)
                    v17 = load32(v2 + 24)
                    if ((load32(v9 + 12) + 8) > load32(v2 + 24)):
                        break
                    while True:  # $label17
                        while True:  # $label16
                            while True:  # $label18
                                v3 = load32(v2 + 16)
                                v18 = load32(v2 + 12)
                                if (load32(v2 + 16) != load32(v2 + 12)):
                                    v1 = ((v3 - v18) >> 5)
                                    v21 = (1 if (u32(v1) <= u32(1)) else ((v3 - v18) >> 5))
                                    v11 = 0
                                    while True:  # $label19
                                        while True:  # $label12
                                            v1 = (v18 + (v11 << 5))
                                            v0 = load32((v18 + (v11 << 5)) + 24)
                                            v12 = load32(v1 + 20)
                                            if (load32((v18 + (v11 << 5)) + 24) == load32(v1 + 20)):
                                                break
                                            v0 = ((v0 - v12) >> 4)
                                            v22 = (1 if (u32(v0) <= u32(1)) else ((v0 - v12) >> 4))
                                            v6 = 2147483647
                                            v0 = 0
                                            v4 = -1
                                            while True:  # $label14
                                                while True:  # $label13
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
                                            while True:  # $label15
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
                                                if (u32((((v0 - load32(v1 + 8)) >> 4) + 1)) >= u32(268435456)):
                                                    break
                                                v6 = (v4 >> 3)
                                                v3 = (268435455 if (u32(v4) >= u32(2147483632)) else ((v4 >> 3) if (u32(v3) < u32(v6)) else v3))
                                                if (268435455 if (u32(v4) >= u32(2147483632)) else ((v4 >> 3) if (u32(v3) < u32(v6)) else v3)):
                                                    if (u32(v3) >= u32(268435456)):
                                                        break
                                                else:
                                                v6 = 0
                                                v7 = (0 + (v7 << 4))
                                                store64((0 + (v7 << 4)), load64(v2 + 32))
                                                store64(v7 + 8, load64(v2 + 40))
                                                # TODO: memory.copy
                                                store32(v1 + 8, v6)
                                                store32(v1 + 12, (v7 + 16))
                                                store32(v1 + 16, (v6 + (v3 << 4)))
                                                if not v0:
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
                                while True:  # $label20
                                    if (u32(load32(v2 + 20)) > u32(v3)):
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
                                v11 = (1 if (u32(v0) <= u32(1)) else ((v0 - v3) >> 4))
                                v6 = 2147483647
                                v0 = 0
                                v4 = -1
                                while True:  # $label22
                                    while True:  # $label21
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
                                while True:  # $label26
                                    while True:  # $label25
                                        while True:  # $label24
                                            while True:  # $label23
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
                                                if (u32((((v4 - load32(v1 + 8)) >> 4) + 1)) >= u32(268435456)):
                                                    break
                                                v10 = (v6 >> 3)
                                                v7 = (268435455 if (u32(v6) >= u32(2147483632)) else ((v6 >> 3) if (u32(v7) < u32(v10)) else v7))
                                                if (268435455 if (u32(v6) >= u32(2147483632)) else ((v6 >> 3) if (u32(v7) < u32(v10)) else v7)):
                                                    if (u32(v7) >= u32(268435456)):
                                                        break
                                                else:
                                                v10 = 0
                                                v11 = (0 + (v11 << 4))
                                                store64((0 + (v11 << 4)), load64(v0))
                                                store64(v11 + 8, load64(v0 + 8))
                                                # TODO: memory.copy
                                                store32(v1 + 16, (v10 + (v7 << 4)))
                                                store32(v1 + 12, (v11 + 16))
                                                store32(v1 + 8, v10)
                                                if not v4:
                                                    break
                                                break
                                            G.global0 = (v3 + 16)
                                            break
                                            break
                                        func42()
                                        raise Unreachable()
                                        break
                                    func68()
                                    raise Unreachable()
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
                            storef32((v19 + (load32(v9 + 4) << 2)), i32(v1))
                            storef32(v3 + 4, i32(v0))
                            store32((v4 + load32(9687240)) + 8, v11)
                            break
                            break
                        func42()
                        raise Unreachable()
                        break
                    func68()
                    raise Unreachable()
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

# ----------------------------------------------------------
# $Nb
# Export: Nb
# ----------------------------------------------------------
def Nb():
    """Export: Nb"""
    while True:  # $label0
        v1 = load8u(9147210)
        if not load8u(9147210):
            store32(CURRENT_PLAYER, 1)
            break
        while True:  # $label1
            v2 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v4 = load32(9142384)
            v5 = load32(PLAYERS)
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
        store32(CURRENT_PLAYER, v0)
        store32(PLAYER_COUNT, load32(41092))
        break
    v10 = load32(PLAYERS)
    store16(load32(PLAYERS) + 283972, 65535)
    store8((v10 + 283974), 255)
    v3 = load32(GAME_STATE)
    v4 = load32(load32(GAME_STATE) + 16)
    v0 = (load32(load32(GAME_STATE) + 16) == 991915600)
    store8(9216060, (load32(load32(GAME_STATE) + 16) == 991915600))
    v6 = load32(v3 + 4)
    v11 = load32(v3 + 4)
    v7 = load32(v3 + 8)
    v12 = load32(v3 + 8)
    v8 = load32(v3 + 12)
    v9 = load32(v3 + 12)
    v5 = v4
    v2 = load32(v3 + 44)
    if (u32(load32(v3 + 44)) >= u32(101)):
        v2 = ((v2 * 15) - 1500)
        # TODO: i32.div_u
        v5 = (100 + v4)
        # TODO: i32.div_u
        v12 = (100 + v7)
        # TODO: i32.div_u
        v11 = (100 + v6)
        # TODO: i32.div_u
        v9 = (100 + v8)
    while True:  # $label3
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v4 = (0 if v0 else v4)
        v2 = 1
        if not v1:
            while True:  # $label6
                while True:  # $label4
                    v0 = (v10 + (v2 * 286704))
                    if (u32(load32((v10 + (v2 * 286704)) + 283960)) <= u32(2)):
                        v1 = load32(v0 + 284616)
                        break
                    v1 = load32(v0 + 284616)
                    store32((v0 + 283960), ((load32(v0 + 284616) + load32(v3 + 184)) % 3))
                    break
                while True:  # $label5
                    if not (not v1 & (u32(v2) > u32(1))):
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
                if (u32((v2 + 1)) < u32(load32(PLAYER_COUNT))):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label9
            while True:  # $label7
                v0 = (v10 + (v2 * 286704))
                if (u32(load32((v10 + (v2 * 286704)) + 283960)) <= u32(2)):
                    v1 = load32(v0 + 284616)
                    break
                v1 = load32(v0 + 284616)
                store32((v0 + 283960), ((load32(v0 + 284616) + load32(v3 + 184)) % 3))
                break
            while True:  # $label8
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
            if (u32((v2 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
        break

# ----------------------------------------------------------
# $Gb
# Export: Gb
# ----------------------------------------------------------
def Gb(arg0):
    """Export: Gb"""
    v3 = load32(9142440)
    if (load32(9142440) > 0):
        while True:  # $label3
            v4 = (v1 + 1)
            arg0 = 0
            while True:  # $label2
                v2 = load32(9142440)
                v5 = ((load32(9142440) * arg0) + v1)
                v6 = load32(9147288)
                while True:  # $label1
                    while True:  # $label0
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
                if (u32((arg0 + 4)) < u32(load32(load32(9681936) + 8))):
                    continue
                break
        store32(v1 + 8, 0)
        store32(9140328, 0)
    store8(9681940, 1)

# ----------------------------------------------------------
# $Xc
# Export: Xc
# ----------------------------------------------------------
def Xc(arg0):
    """Export: Xc"""
    v1 = (G.global0 - 96)
    G.global0 = (G.global0 - 96)
    while True:  # $label0
        v2 = load32(9568088)
        v3 = load32(load32(9568088) + 28)
        if not load32(load32(9568088) + 28):
            break
        v5 = i32((v3 << 5))
        v6 = i32((load32(v2 + 40) << 5))
        v7 = i32((load32(v2 + 24) << 5))
        v8 = i32((load32(v2 + 20) << 5))
        if not load8u(9142917):
            while True:  # $label1
                v4 = ((v6 * 0.5) + v7)
                if ((((v6 * 0.5) + v7) < 4294967300.0) & (v4 >= 0.0)):
                    break
                break
            store32(i32(v4) + 84, 0)
            while True:  # $label2
                v4 = ((v5 * 0.5) + v8)
                if ((((v5 * 0.5) + v8) < 4294967300.0) & (v4 >= 0.0)):
                    break
                break
            store32(i32(v4) + 80, 0)
        if not arg0:
            store8(9684432, 1)
        arg0 = load32(9142876)
        if load8u(9142916):
            # TODO: f64.promote_f32
        else:
        v9 = 0.0
        store32(v1 + 72, arg0)
        storef64((v1 - -64), v9)
        # TODO: f64.promote_f32
        storef64(v1 + 56, v7)
        # TODO: f64.promote_f32
        storef64(v1 + 48, v8)
        a_b()
        if load8u(9142916):
            break
        store64(v1 + 16, 0)
        store64(v1 + 24, 0)
        store32(v1 + 32, load32(9142876))
        # TODO: f64.promote_f32
        storef64(v1 + 8, v6)
        # TODO: f64.promote_f32
        storef64(v1, neg(v5))
        a_b()
        break
    G.global0 = (v1 + 96)
    return v1

# ----------------------------------------------------------
# $Xb
# Export: Xb
# ----------------------------------------------------------
def Xb(arg0):
    """Export: Xb"""
    v6 = load32(PLAYER_COUNT)
    v3 = (load32(PLAYER_COUNT) + 1)
    store32(PLAYER_COUNT, (load32(PLAYER_COUNT) + 1))
    v12 = (i32(v3) * 286704)
    v3 = (-1 if i32(((v12 & 0xFFFFFFFF) >> 32)) else i32((i32(v3) * 286704)))
    v4 = func26((-1 if i32(((v12 & 0xFFFFFFFF) >> 32)) else i32((i32(v3) * 286704))))
    # TODO: memory.fill
    v1 = load32(PLAYERS)
    while True:  # $label4
        while True:  # $label3
            while True:  # $label1
                if v6:
                    if (u32(v6) >= u32(4)):
                        v5 = (v6 & -4)
                        v3 = 0
                        while True:  # $label0
                            v7 = (v2 * 286704)
                            # TODO: memory.copy
                            v7 = ((v2 | 1) * 286704)
                            # TODO: memory.copy
                            v7 = ((v2 | 2) * 286704)
                            # TODO: memory.copy
                            v7 = ((v2 | 3) * 286704)
                            # TODO: memory.copy
                            v2 = (v2 + 4)
                            v3 = (v3 + 4)
                            if ((v3 + 4) != v5):
                                continue
                            break
                    v6 = (v6 & 3)
                    if not (v6 & 3):
                        break
                    v3 = 0
                    while True:  # $label2
                        v5 = (v2 * 286704)
                        # TODO: memory.copy
                        v2 = (v2 + 1)
                        v3 = (v3 + 1)
                        if ((v3 + 1) != v6):
                            continue
                        break
                    break
                if v1:
                    break
                v3 = 0
                store32(PLAYERS, v4)
                v2 = (v4 + (v6 * 286704))
                v6 = 1
                break
                break
            store32(PLAYERS, v4)
            v6 = load32(PLAYER_COUNT)
            v3 = (load32(PLAYER_COUNT) - 1)
            v2 = (v4 + ((load32(PLAYER_COUNT) - 1) * 286704))
            if (u32(v3) <= u32(8)):
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
    while True:  # $label5
        v1 = (v6 * 20)
        v5 = ((v6 * 20) - 60)
        if (u32(((v6 * 20) - 60)) < u32(load16u(9142944))):
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
    # TODO: memory.copy
    v2 = load32(GAME_STATE)
    store32((v1 + 284000), load32(load32(GAME_STATE) + 40))
    store32((v1 + 284136), load32(v2 + 36))
    if (u32(v6) >= u32(3)):
        store32(v1 + 283848, load32((v4 + 570552)))
        store32((v1 + 283852), load32((v4 + 570556)))
        store32((v1 + 283856), load32((v4 + 570560)))
        store32((v1 + 283860), load32((v4 + 570564)))
    v3 = load32(PLAYER_COUNT)
    if load32(PLAYER_COUNT):
        v2 = load32(PLAYERS)
        v5 = 0
        while True:  # $label10
            v1 = (v2 + (v5 * 286704))
            if load32((v2 + (v5 * 286704)) + 281800):
                v2 = (-1 if (u32(v3) > u32(1073741823)) else (v3 << 2))
                v4 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                # TODO: memory.fill
                v10 = (v1 + 281800)
                v1 = load32((v1 + 281800))
                while True:  # $label9
                    while True:  # $label7
                        v7 = (v3 - 1)
                        if (v3 - 1):
                            v9 = 0
                            v2 = 0
                            if (u32((v3 - 2)) >= u32(3)):
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
                            if not (v7 & 3):
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
                        if not v1:
                            break
                        break
                    v3 = load32(PLAYER_COUNT)
                    break
                store32(v10, v4)
                v2 = load32(PLAYERS)
            v5 = (v5 + 1)
            if (u32((v5 + 1)) < u32(v3)):
                continue
            break
    if (arg0 != 5):
    func284(0)
    return 0

# ----------------------------------------------------------
# $Rc
# Export: Rc
# ----------------------------------------------------------
def Rc(arg0):
    """Export: Rc"""
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v3 = load32(ENTITIES)
    if not load8u(9142917):
        v2 = (v3 + (arg0 * 132))
        v4 = load32((v3 + (arg0 * 132)) + 36)
        v2 = (v3 + ((load32((v3 + (arg0 * 132)) + 36) if v4 else load32(v2 + 28)) * 132))
        v4 = ((load8u((v3 + ((load32((v3 + (arg0 * 132)) + 36) if v4 else load32(v2 + 28)) * 132)) + 122) * 404) + ENTITY_TYPES)
        v5 = load32(((load8u((v3 + ((load32((v3 + (arg0 * 132)) + 36) if v4 else load32(v2 + 28)) * 132)) + 122) * 404) + ENTITY_TYPES) + 216)
        v6 = load16u(v2 + 112)
        store32(v1 + 36, (((load32(v4 + 220) << 4) & 2147483632) + (load16u(v2 + 114) << 5)))
        store32(v1 + 32, (((v5 << 4) & 2147483632) + (v6 << 5)))
    while True:  # $label0
        arg0 = load32((v3 + (arg0 * 132)) + 40)
        if not load32((v3 + (arg0 * 132)) + 40):
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

# ----------------------------------------------------------
# $Ca
# Export: Ca
# ----------------------------------------------------------
def Ca(arg0):
    """Export: Ca"""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v1 + 12, arg0)
    func71(21, 0, 0, (v1 + 12), 1, 0)
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $Aa
# Export: Aa
# ----------------------------------------------------------
def Aa(arg0, arg1):
    """Export: Aa"""
    while True:  # $label0
        v3 = (arg0 + arg1)
        if not (arg0 + arg1):
            break
        v4 = load8u(9147212)
        if (u32(v3) >= u32(load32((PLAYER_COUNT if load8u(9147212) else 41092)))):
            break
        v2 = load32(PLAYERS)
        arg1 = players[arg0]
        v5 = load32(players[arg0] + 284616)
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
        while True:  # $label1
            if not v4:
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
                # TODO: memory.copy
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
                store32((load32(PLAYERS) + v30) + 283908, v3)
                break
            v4 = (arg1 + 284616)
            arg0 = (v2 + (v3 * 286704))
            v2 = ((v2 + (v3 * 286704)) + 284616)
            while True:  # $label2
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

# ----------------------------------------------------------
# $Nd
# Export: Nd
# ----------------------------------------------------------
def Nd(arg0):
    """Export: Nd"""
    store8(9216068, arg0)
    if arg0:
        while True:  # $label0
            v1 = (v1 + 1)
            if ((v1 + 1) != 356):
                continue
            break

# ----------------------------------------------------------
# $Td
# Export: Td
# ----------------------------------------------------------
def Td():
    """Export: Td"""
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                v0 = ((v3 * 404) + ENTITY_TYPES)
                # br_table load32(((v3 * 404) + ENTITY_TYPES) + 264)
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
                # TODO: i32.div_u
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

# ----------------------------------------------------------
# $Ib
# Export: Ib
# ----------------------------------------------------------
def Ib(arg0, arg1, arg2):
    """Export: Ib"""
    while True:  # $label0
        arg0 = ((arg2 * 404) + ENTITY_TYPES)
        if (arg0 != load32(((arg2 * 404) + ENTITY_TYPES) + 196)):
            break
        if (load32(arg0 + 264) != arg1):
            break
        while True:  # $label1
            arg0 = ((arg2 * 404) + ENTITY_TYPES)
            if (load32(((arg2 * 404) + ENTITY_TYPES) + 188) == 55):
                break
            if (load32(38528) == arg2):
                break
            if (load32(38768) != arg2):
                break
            break
        if load8u(arg0 + 378):
            break
        v3 = load32(((arg2 * 404) + ENTITY_TYPES) + 84)
        break
    return v3

# ----------------------------------------------------------
# $Yd
# Export: Yd
# ----------------------------------------------------------
def Yd():
    """Export: Yd"""
    while True:  # $label1
        while True:  # $label0
            v1 = ((v2 * 404) + ENTITY_TYPES)
            if (load32(((v2 * 404) + ENTITY_TYPES) + 264) != 3):
                break
            if not load32(v1 + 180):
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
    v6 = func26((-1 if (u32(v0) > u32(1073741823)) else (v0 << 2)))
    store32(9685864, func26((-1 if (u32(v0) > u32(1073741823)) else (v0 << 2))))
    while True:  # $label12
        while True:  # $label2
            v1 = ((v11 * 404) + ENTITY_TYPES)
            if (load32(((v11 * 404) + ENTITY_TYPES) + 264) != 3):
                break
            if not load32(v1 + 180):
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
            while True:  # $label3
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
            while True:  # $label4
                if not v4:
                    break
                v10 = (v4 & 3)
                v3 = load32(v1 + 240)
                v8 = 0
                while True:  # $label5
                    if (u32(v4) < u32(4)):
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
                if not v10:
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
            while True:  # $label8
                if not v5:
                    break
                v7 = (v5 & 3)
                v1 = load32(v1 + 232)
                v8 = 0
                while True:  # $label9
                    if (u32(v5) < u32(4)):
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
                if not v7:
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

# ----------------------------------------------------------
# $Gd
# Export: Gd
# ----------------------------------------------------------
def Gd(arg0):
    """Export: Gd"""
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

# ----------------------------------------------------------
# $Va
# Export: Va
# ----------------------------------------------------------
def Va(arg0, arg1):
    """Export: Va"""
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

# ----------------------------------------------------------
# $Rb
# Export: Rb
# ----------------------------------------------------------
def Rb():
    """Export: Rb"""
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v3 = load32(PLAYERS)
        v1 = 1
        while True:  # $label1
            v0 = (v3 + (v1 * 286704))
            v4 = func88(v0)
            store32((v3 + (v1 * 286704)) + 283884, func88(v0))
            store32(v0 + 283892, v4)
            v1 = (v1 + 1)
            v0 = load32(PLAYER_COUNT)
            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
        if (u32(v0) < u32(2)):
            break
        v4 = 1
        while True:  # $label4
            v0 = (v3 + (v4 * 286704))
            store32((v3 + (v4 * 286704)) + 283944, 1)
            v1 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                v5 = (v0 + 283944)
                v7 = (v0 + 283884)
                v6 = 1
                v0 = 1
                while True:  # $label3
                    while True:  # $label2
                        if (v0 == v4):
                            break
                        v9 = load32((v3 + (v0 * 286704)) + 283884)
                        v8 = load32(v7)
                        if (u32(load32((v3 + (v0 * 286704)) + 283884)) <= u32(load32(v7))):
                            if (v8 != v9):
                                break
                            if (u32(v0) <= u32(v4)):
                                break
                        v6 = (v6 + 1)
                        store32(v5, (v6 + 1))
                        v1 = load32(PLAYER_COUNT)
                        break
                    v0 = (v0 + 1)
                    if (u32((v0 + 1)) < u32(v1)):
                        continue
                    break
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(v1)):
                continue
            break
        if (u32(v1) < u32(2)):
            break
        v4 = 1
        while True:  # $label10
            v5 = load32(PLAYERS)
            v0 = 1
            while True:  # $label5
                if (u32(v1) <= u32(1)):
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
            while True:  # $label7
                if load32(9147132):
                    if not load32(v3 + 284616):
                        break
                v6 = 0
                while True:  # $label8
                    v7 = load32(CURRENT_PLAYER)
                    v9 = ((load32(CURRENT_PLAYER) * v1) + v0)
                    if not load8u((((load32(CURRENT_PLAYER) * v1) + v0) + load32(9143004))):
                        break
                    v6 = 1
                    v8 = load32(v3 + 281800)
                    if not load32(v3 + 281800):
                        break
                    v8 = load32((v8 + (v7 << 2)))
                    if not load32((v8 + (v7 << 2))):
                        break
                    v6 = (3 if (u32(((load32(9142848) - v8) * 25)) < u32(60000)) else 2)
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
                while True:  # $label9
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
                v1 = load32(PLAYER_COUNT)
                break
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(v1)):
                continue
            break
        break
    G.global0 = (v2 - -64)
    return v2

# ----------------------------------------------------------
# $N
# Export: N
# ----------------------------------------------------------
def N(arg0, arg1):
    """Export: N"""
    if not arg0:
        return (load8u(9147209) != 0)
    store8(9147209, arg1)
    arg0 = 0
    v2 = load32(PLAYER_COUNT)
    v3 = (load32(PLAYER_COUNT) * v2)
    v2 = func26((load32(PLAYER_COUNT) * v2))
    # TODO: memory.fill
    store32(9143012, v2)
    while True:  # $label0
        if not v3:
            break
        v4 = load32(9143004)
        if (u32(v3) >= u32(4)):
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
        if not (v3 & 3):
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

# ----------------------------------------------------------
# $Tb
# Export: Tb
# ----------------------------------------------------------
def Tb(arg0, arg1, arg2, arg3, arg4):
    """Export: Tb"""
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    store32(v5 + 16, arg4)
    store32(v5 + 12, arg3)
    store32(v5 + 8, arg2)
    store32(v5 + 4, arg1)
    store32(v5, arg0)
    while True:  # $label0
        if load8u(9147210):
            func41(41, 0, 0, v5, 5)
            break
        break
    G.global0 = (v5 + 32)

# ----------------------------------------------------------
# $Zc
# Export: Zc
# ----------------------------------------------------------
def Zc(arg0, arg1, arg2):
    """Export: Zc"""
    v3 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    store32(9684428, arg1)
    v4 = load32((load32(9568076) + (12 if (arg1 != 1) else 0)))
    store32(9568084, arg0)
    arg0 = (v4 + (arg0 * 196))
    store32(9568088, (v4 + (arg0 * 196)))
    if not arg2:
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

# ----------------------------------------------------------
# $Nc
# Export: Nc
# ----------------------------------------------------------
def Nc():
    """Export: Nc"""
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
            if (u32((v1 + 1)) < u32(((load32(9568068) - load32(9568064)) >> 7))):
                continue
            break
    G.global0 = (v0 + 16)

# ----------------------------------------------------------
# $Ic
# Export: Ic
# ----------------------------------------------------------
def Ic(arg0):
    """Export: Ic"""
    while True:  # $label0
        if not load32(PLAYER_COUNT):
            break
        v1 = load32(PLAYERS)
        if not load32(PLAYERS):
            break
        break
    arg0 = (arg0 + 1)
    store32(PLAYER_COUNT, (arg0 + 1))
    v2 = (i32(arg0) * 286704)
    arg0 = (-1 if i32(((v2 & 0xFFFFFFFF) >> 32)) else i32((i32(arg0) * 286704)))
    v1 = func26((-1 if i32(((v2 & 0xFFFFFFFF) >> 32)) else i32((i32(arg0) * 286704))))
    # TODO: memory.fill
    store32(PLAYERS, v1)

# ----------------------------------------------------------
# $Cb
# Export: Cb
# ----------------------------------------------------------
def Cb():
    """Export: Cb"""
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

# ----------------------------------------------------------
# $Mb
# Export: Mb
# ----------------------------------------------------------
def Mb(arg0):
    """Export: Mb"""
    v2 = (arg0 << 2)
    v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
    if arg0:
        # TODO: memory.copy
    func318(arg0, v1, arg0)

# ----------------------------------------------------------
# $Lc
# Export: Lc
# ----------------------------------------------------------
def Lc(arg0):
    """Export: Lc"""
    v1 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    store64(v1 + 8, 0)
    store64(v1 + 16, 0)
    store64(v1, 0)
    store64(v1 + 104, 4294967296)
    store64(v1 + 120, 0)
    store64(v1 + 112, 2147483648000)
    while True:  # $label2
        while True:  # $label0
            while True:  # $label4
                v3 = load32(9568068)
                if (load32(9568068) != load32(9568072)):
                    store32(v3 + 8, 0)
                    store64(v3, 0)
                    v4 = load32(v1 + 4)
                    v2 = load32(v1)
                    v5 = (load32(v1 + 4) - load32(v1))
                    arg0 = ((load32(v1 + 4) - load32(v1)) // 196)
                    if (v2 != v4):
                        if (u32(arg0) >= u32(21913099)):
                            break
                        v2 = func26(v5)
                        store32(v3 + 4, func26(v5))
                        store32(v3, v2)
                        store32(v3 + 8, (v2 + (arg0 * 196)))
                        arg0 = load32(v1)
                        v4 = load32(v1 + 4)
                        if (load32(v1) != load32(v1 + 4)):
                            while True:  # $label1
                                # TODO: memory.copy
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
                        if (u32(arg0) >= u32(21913099)):
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
                                # TODO: memory.copy
                                v2 = (v2 + 196)
                                arg0 = (arg0 + 196)
                                if ((arg0 + 196) != v5):
                                    continue
                                break
                        store32(v3 + 16, v2)
                    # TODO: memory.copy
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
        raise Unreachable()
        break
    func42()
    raise Unreachable()
    return af(v4)

# ----------------------------------------------------------
# $Ha
# Export: Ha
# ----------------------------------------------------------
def Ha():
    """Export: Ha"""
    v0 = load32(PLAYERS)
    if load32(PLAYERS):
        store32(PLAYERS, 0)
    store8(9147212, 0)
    store32(9142912, 0)
    store32(PLAYER_COUNT, 0)

# ----------------------------------------------------------
# $Be
# Export: Be
# ----------------------------------------------------------
def Be():
    """Export: Be"""
    func169()

# ----------------------------------------------------------
# $Ad
# Export: Ad
# ----------------------------------------------------------
def Ad(arg0):
    """Export: Ad"""
    v1 = load32(9568088)
    if (load32(load32(9568088) + 88) if arg0 else 1):
        return load32(v1 + 80)
    while True:  # $label1
        while True:  # $label0
            v3 = load32(v1 + 88)
            if (load32(v1 + 88) != load32(v1 + 84)):
                v2 = load32(v1 + 80)
                break
            v2 = (load32(v1 + 92) + v3)
            store32(v1 + 84, (load32(v1 + 92) + v3))
            v4 = load32(v1 + 80)
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if v3:
                # TODO: memory.copy
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

# ----------------------------------------------------------
# $Cd
# Export: Cd
# ----------------------------------------------------------
def Cd(arg0):
    """Export: Cd"""
    v1 = load32(9568088)
    if (load32(load32(9568088) + 104) if arg0 else 1):
        return load32(v1 + 96)
    while True:  # $label1
        while True:  # $label0
            v3 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v2 = load32(v1 + 96)
                break
            v2 = (load32(v1 + 108) + v3)
            store32(v1 + 100, (load32(v1 + 108) + v3))
            v4 = load32(v1 + 96)
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if v3:
                # TODO: memory.copy
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

# ----------------------------------------------------------
# $Re
# Export: Re
# ----------------------------------------------------------
def Re(arg0):
    """Export: Re"""
    v1 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    v1 = func26((arg0 + 4))
    store32(9687208, arg0)
    store32(9687204, v1)
    return v1

# ----------------------------------------------------------
# $Sa
# Export: Sa
# ----------------------------------------------------------
def Sa(arg0, arg1):
    """Export: Sa"""
    v7 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label1
        while True:  # $label0
            if (load8u(9147212) | load8u(9147210)):
                if not load32(PLAYER_COUNT):
                    break
                store32(PLAYER_COUNT, 0)
                v2 = load32(PLAYERS)
                if load32(PLAYERS):
                    store32(PLAYERS, 0)
            v4 = load32(PLAYER_COUNT)
            if load32(PLAYER_COUNT):
                break
            break
        v4 = 6
        break
    v2 = 0
    arg0 = (arg0 + v4)
    v5 = (2 if (arg0 <= 2) else (arg0 + v4))
    store32(PLAYER_COUNT, (2 if (arg0 <= 2) else (arg0 + v4)))
    arg0 = load32(PLAYERS)
    v11 = (i32(v5) * 286704)
    v6 = (-1 if i32(((v11 & 0xFFFFFFFF) >> 32)) else i32((i32(v5) * 286704)))
    v3 = func26((-1 if i32(((v11 & 0xFFFFFFFF) >> 32)) else i32((i32(v5) * 286704))))
    # TODO: memory.fill
    if arg0:
        v5 = (v5 if (u32(v4) > u32(v5)) else v4)
        v4 = ((v5 if (u32(v4) > u32(v5)) else v4) & 3)
        if (u32((v5 - 1)) >= u32(3)):
            v6 = (v5 & 2147483644)
            v5 = 0
            while True:  # $label2
                v8 = (v2 * 286704)
                # TODO: memory.copy
                v8 = ((v2 | 1) * 286704)
                # TODO: memory.copy
                v8 = ((v2 | 2) * 286704)
                # TODO: memory.copy
                v8 = ((v2 | 3) * 286704)
                # TODO: memory.copy
                v2 = (v2 + 4)
                v5 = (v5 + 4)
                if ((v5 + 4) != v6):
                    continue
                break
        if v4:
            v5 = 0
            while True:  # $label3
                v6 = (v2 * 286704)
                # TODO: memory.copy
                v2 = (v2 + 1)
                v5 = (v5 + 1)
                if ((v5 + 1) != v4):
                    continue
                break
        v5 = load32(PLAYER_COUNT)
    store32(PLAYERS, v3)
    store32(v7 + 32, (v5 - 1))
    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
        arg0 = 1
        while True:  # $label10
            v2 = players[arg0]
            v8 = (players[arg0] + 283908)
            while True:  # $label4
                if load32(v2 + 283908):
                    v5 = (arg0 - 1)
                    v4 = load8u(v2 + 283972)
                    v6 = load8u((v2 + 283973))
                    v3 = load8u((v2 + 283974))
                    break
                store64(v2 + 283848, 1717986918800)
                v5 = (arg0 - 1)
                # TODO: i32.div_u
                store32((arg0 - 1) + 284608, 4)
                store64((v2 + 283856), 1717986918800)
                while True:  # $label5
                    if (u32(arg0) <= u32(1)):
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
                        if (u32(arg1) >= u32(3)):
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
                    while True:  # $label6
                        if (u32(arg0) <= u32(8)):
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
                    while True:  # $label9
                        while True:  # $label8
                            while True:  # $label7
                                # br_table load32(v6)
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
            if (u32((arg0 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
    G.global0 = (v7 + 48)
    return v7

# ----------------------------------------------------------
# $Ae
# Export: Ae
# ----------------------------------------------------------
def Ae(arg0):
    """Export: Ae"""
    if load8u(9142916):
        store32(9603804, 0)
        store32(9577140, 0)
        store32(9576736, 0)
        store32(9571080, 0)
    v1 = load8u(9147152)
    while True:  # $label3
        while True:  # $label1
            while True:  # $label0
                if not load8u(9147212):
                    if v1:
                        break
                    break
                while True:  # $label2
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
            store32(CURRENT_PLAYER, 1)
            v3 = load32(9142440)
            if (load32(9142440) * v3):
                while True:  # $label4
                    store8((load32(9147288) + v1), load32(9147292))
                    v1 = (v1 + 1)
                    v3 = load32(9142440)
                    if (u32((v1 + 1)) < u32((load32(9142440) * v3))):
                        continue
                    break
            store32(9147312, arg0)
            store32(PLAYER_COUNT, 2)
            store32(9147324, (arg0 ^ -1))
            store32(9147320, (arg0 ^ -1515870811))
            store32(9147316, (arg0 ^ 1515870810))
            arg0 = load32(PLAYERS)
            if load32(PLAYERS):
            else:
            v5 = (i32(2) * 286704)
            v1 = (load32(PLAYER_COUNT) if i32(((v5 & 0xFFFFFFFF) >> 32)) else i32((i32(2) * 286704)))
            arg0 = func26((load32(PLAYER_COUNT) if i32(((v5 & 0xFFFFFFFF) >> 32)) else i32((i32(2) * 286704))))
            # TODO: memory.fill
            store32(PLAYERS, arg0)
            store32((arg0 + 571312), 1)
            store32((arg0 + 286712), 6553701)
            store64((arg0 + 286704), 32088563964837972)
            store32((arg0 + 570612), 1)
            store32((arg0 + 570572), load32(9561460))
            # TODO: memory.copy
            v1 = load32(GAME_STATE)
            store32((arg0 + 570704), load32(load32(GAME_STATE) + 40))
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
        v3 = load32(PLAYER_COUNT)
        store32(9142420, func26((-1 if (u32(v3) > u32(1073741823)) else (load32(PLAYER_COUNT) << 2))))
        arg0 = load32(GAME_STATE)
        v2 = load32(load32(GAME_STATE) + 136)
        # TODO: i32.div_u
        store32(1, (1 if (u32(v2) <= u32(99)) else (load32(load32(GAME_STATE) + 136) if load8u(9147210) else 100)))
        v2 = load32(arg0 + 140)
        store32(51760, (load32(arg0 + 140) * 1000))
        storef32(9682176, i32(v2))
        v2 = load32(arg0 + 144)
        store32(51764, (load32(arg0 + 144) * 1000))
        storef32(9682180, i32(v2))
        v2 = load32(arg0 + 148)
        store32(51768, (load32(arg0 + 148) * 1000))
        storef32(9682184, i32(v2))
        arg0 = load32(arg0 + 152)
        store32(51772, (load32(arg0 + 152) * 1000))
        storef32(9682188, i32(arg0))
        if v4:
            break
        if not v3:
            break
        while True:  # $label5
            func239(v1)
            v1 = (v1 + 1)
            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
        break
    return 40592

# ----------------------------------------------------------
# $We
# Export: We
# ----------------------------------------------------------
def We():
    """Export: We"""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v3 + 12, 0)
    func71(30, (v3 + 12), 1, 0, 0, 1)
    while True:  # $label0
        v4 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v5 = load32(PLAYERS)
        v1 = 1
        while True:  # $label2
            while True:  # $label1
                v2 = (v5 + (v1 * 286704))
                v6 = load32((v5 + (v1 * 286704)) + 284616)
                if not load32((v5 + (v1 * 286704)) + 284616):
                    break
                if not load32(v2 + 284604):
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
        if not v0:
            break
        func71(32, 8447808, v0, 0, 0, 1)
        v2 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v0 = load32(PLAYERS)
        v1 = 1
        while True:  # $label4
            v4 = (v0 + (v1 * 286704))
            if not load8u((v0 + (v1 * 286704)) + 286699):
                v2 = load32(v4 + 284604)
                while True:  # $label3
                    if not load8u(9147210):
                        break
                    if (load32(v4 + 284616) != load32(9561844)):
                        if (load32(CURRENT_PLAYER) != v1):
                            break
                        if not load8u(9142388):
                            break
                    v2 = 2147483647
                    break
                store32(v3 + 4, v2)
                store32(v3, v1)
                a_b()
                v2 = load32(PLAYER_COUNT)
                v0 = load32(PLAYERS)
            v1 = (v1 + 1)
            if (u32((v1 + 1)) < u32(v2)):
                continue
            break
        break
    G.global0 = (v3 + 16)

# ----------------------------------------------------------
# $Ve
# Export: Ve
# ----------------------------------------------------------
def Ve(arg0):
    """Export: Ve"""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v4 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v5 = load32(PLAYERS)
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
            v3 = (u32((v1 + 1)) < u32(v4))
            if (v1 != v4):
                continue
            break
        break
    G.global0 = (v2 + 16)
    return v3

# ----------------------------------------------------------
# $Rd
# Export: Rd
# ----------------------------------------------------------
def Rd(arg0, arg1):
    """Export: Rd"""
    v3 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    if not load8u(9216068):
        arg1 = load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 196)
    while True:  # $label0
        v2 = ((arg0 * 132) + 9216080)
        if not load8u(((arg0 * 132) + 9216080) + 23):
            v5 = 1
            v7 = 2147483647
            break
        v5 = 1
        while True:  # $label1
            v7 = load32(v2 + 4)
            v4 = ((load32(v2 + 4) * 404) + ENTITY_TYPES)
            if (load32(((load32(v2 + 4) * 404) + ENTITY_TYPES) + 264) == 3):
                break
            arg0 = load32(v4 + 196)
            if (load32(v4 + 196) == arg1):
                break
            if (u32(arg0) > u32(2)):
                break
            v5 = (load32(9147132) != 0)
            break
        v6 = load32(v4 + 144)
        v8 = load32(v4 + 88)
        v5 = (not load8u(v4 + 354) & v5)
        break
    arg1 = load32(v4 + 84)
    arg0 = load32(v2 + 8)
    while True:  # $label2
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

# ----------------------------------------------------------
# $Ea
# Export: Ea
# ----------------------------------------------------------
def Ea(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12):
    """Export: Ea"""
    if arg6:
        while True:  # $label0
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg4 = load32(9561784)
                break
            arg1 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg0 = load32(9561784)
            arg4 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
            if arg6:
                # TODO: memory.copy
            if arg0:
                arg6 = load32(9561792)
            store32(9561784, arg4)
            break
        store32(9561792, (arg6 + 1))
        store32((arg4 + (arg6 << 2)), arg3)
        arg1 = (load32(59176) + 10)
        while True:  # $label1
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg3 = arg4
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg3 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy
            store32(9561784, arg3)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg3 + (arg6 << 2)), arg1)
        while True:  # $label2
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg4 = arg3
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg4 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy
            store32(9561784, arg4)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg4 + (arg6 << 2)), arg5)
        while True:  # $label3
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg3 = arg4
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg3 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy
            store32(9561784, arg3)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg3 + (arg6 << 2)), arg2)
        while True:  # $label4
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg4 = arg3
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg4 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy
            store32(9561784, arg4)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg4 + (arg6 << 2)), arg8)
        while True:  # $label5
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg3 = arg4
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg3 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy
            store32(9561784, arg3)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg3 + (arg6 << 2)), arg7)
        while True:  # $label6
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg4 = arg3
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg4 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy
            store32(9561784, arg4)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg4 + (arg6 << 2)), arg9)
        while True:  # $label7
            arg6 = load32(9561792)
            if (load32(9561792) != load32(9561788)):
                arg3 = arg4
                break
            arg0 = (load32(9561796) + arg6)
            store32(9561788, (load32(9561796) + arg6))
            arg3 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg6:
                # TODO: memory.copy
            store32(9561784, arg3)
            arg6 = load32(9561792)
            break
        store32(9561792, (arg6 + 1))
        store32((arg3 + (arg6 << 2)), arg10)
        return 0
    arg6 = 0
    if not load8u(9561832):
        v13 = load32(PLAYERS)
        v14 = (arg11 + 1)
        arg11 = ((arg11 + 1) * 286704)
        arg6 = players[(arg11 + 1)]
        store32(players[(arg11 + 1)] + 283908, v14)
        v15 = load8u(9147212)
        store32(arg6 + 286684, (not load8u(9147212) & arg4))
        if not arg4:
            store32((arg11 + v13) + 284616, arg3)
        arg11 = (arg11 + v13)
        store32((arg11 + v13) + 283952, arg8)
        store32(arg11 + 283948, arg5)
        store32(arg11 + 284620, (arg12 + 1))
        store32(arg11 + 283964, arg9)
        store8(arg11 + 93, arg10)
        store8(arg11 + 92, arg7)
        while True:  # $label8
            if (arg3 != load32(9142384)):
                if load8u(9147210):
                    break
                if arg4:
                    break
            store32(CURRENT_PLAYER, v14)
            break
        if not v15:
            arg3 = (v13 + (v14 * 286704))
            store32((v13 + (v14 * 286704)) + 284608, arg0)
            store32(arg3 + 283960, (arg1 if (u32(arg1) <= u32(4)) else 0))
            store8(arg3 + 283972, ((arg2 & 0xFFFFFFFF) >> 16))
            store8((arg3 + 283974), arg2)
            store8((arg3 + 283973), ((arg2 & 0xFFFFFFFF) >> 8))
        store32(41092, (load32(41092) + 1))
    return arg6

# ----------------------------------------------------------
# $Ia
# Export: Ia
# ----------------------------------------------------------
def Ia():
    """Export: Ia"""
    while True:  # $label0
        if load8u(9147212):
            break
        v1 = load32(41092)
        if (u32(load32(41092)) < u32(2)):
            break
        v0 = (v1 - 1)
        v3 = ((v1 - 1) & 3)
        v5 = load32(PLAYERS)
        while True:  # $label1
            if (u32((v1 - 2)) < u32(3)):
                v1 = 1
                v0 = 0
                break
            v7 = (v0 & -4)
            v0 = 0
            v1 = 1
            while True:  # $label2
                v2 = (v5 + (v1 * 286704))
                v0 = ((((v0 + not load32((v5 + (v1 * 286704)) + 284616)) + not load32((v2 + 571320))) + not load32((v2 + 858024))) + not load32((v2 + 1144728)))
                v1 = (v1 + 4)
                v6 = (v6 + 4)
                if ((v6 + 4) != v7):
                    continue
                break
            break
        if not v3:
            break
        while True:  # $label3
            v0 = (v0 + not load32((v5 + (v1 * 286704)) + 284616))
            v1 = (v1 + 1)
            v4 = (v4 + 1)
            if ((v4 + 1) != v3):
                continue
            break
        break
    return v0

# ----------------------------------------------------------
# $Od
# Export: Od
# ----------------------------------------------------------
def Od(arg0):
    """Export: Od"""
    if load8u(9147141):

# ----------------------------------------------------------
# $Qd
# Export: Qd
# ----------------------------------------------------------
def Qd(arg0):
    """Export: Qd"""
    arg0 = ((load32(9143000) * load32(9147120)) + arg0)
    while True:  # $label0
        if load8u(9147141):
            v1 = load32(entities[load32(9173808)].y)
            if not load32(entities[load32(9173808)].y):
                break
            if (u32(arg0) >= u32(load32(v1 + 8))):
                break
            return
        if (u32(arg0) >= u32(load32(9671120))):
            break
        if load32(9681836):
            return
        v1 = entities[load32(9173808)]
        v3 = load16u(entities[load32(9173808)] + 110)
        v4 = load32(load32(((arg0 << 2) + 9263072)) + 12)
        v1 = load8u(v1 + 122)
        v5 = load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 196)
        v2 = 1
        while True:  # $label1
            if (load32(38540) == v1):
                break
            if (load32(38812) == v1):
                break
            v2 = (load32(38888) == v1)
            break
        break

# ----------------------------------------------------------
# $Id
# Export: Id
# ----------------------------------------------------------
def Id(arg0, arg1, arg2):
    """Export: Id"""
    v3 = (G.global0 - 144)
    G.global0 = (G.global0 - 144)
    while True:  # $label0
        if load8u(9684432):
            break
        store32(9142900, arg2)
        store8(9142409, 1)
        while True:  # $label1
            v14 = loadf32(40616)
            v15 = i32(load32(9142856))
            v15 = loadf32(9671164)
            v16 = (((loadf32(40616) * i32(arg0)) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v14 * v15) / loadf32(9671164))) * 0.5))
            if (abs((((loadf32(40616) * i32(arg0)) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v14 * v15) / loadf32(9671164))) * 0.5))) < 2147483650.0):
                break
            break
        arg0 = -2147483648
        store32(i32(v16), -2147483648)
        while True:  # $label2
            v16 = i32(load32(9142860))
            v14 = (((i32(load32(9142860)) - ((v14 * v16) / v15)) * 0.5) + ((v14 * i32(arg1)) + i32(load32(9142956))))
            if (abs((((i32(load32(9142860)) - ((v14 * v16) / v15)) * 0.5) + ((v14 * i32(arg1)) + i32(load32(9142956))))) < 2147483650.0):
                break
            break
        arg1 = -2147483648
        store32(i32(v14), -2147483648)
        v4 = load32(9684792)
        if not load32(9684792):
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
        while True:  # $label6
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
                    while True:  # $label4
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
                if not v8:
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

# ----------------------------------------------------------
# $Ee
# Export: Ee
# ----------------------------------------------------------
def Ee(arg0):
    """Export: Ee"""
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v1 = 9143012
    if (u32(arg0) <= u32(2)):
        v1 = load32(((arg0 << 2) + 10284))
    v3 = 1
    v2 = load32(PLAYER_COUNT)
    if (u32(load32(PLAYER_COUNT)) > u32(1)):
        v6 = load32(v1)
        while True:  # $label3
            v8 = players[v3]
            while True:  # $label0
                if (u32(v2) < u32(2)):
                    break
                v4 = (v2 - 1)
                v9 = ((v2 - 1) & 3)
                v1 = 1
                if (u32((v2 - 2)) >= u32(3)):
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
                if not v9:
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
            v2 = load32(PLAYER_COUNT)
            if (u32((v3 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
    G.global0 = (v5 + 16)

# ----------------------------------------------------------
# $Fd
# Export: Fd
# ----------------------------------------------------------
def Fd(arg0):
    """Export: Fd"""
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    store32(40600, arg0)
    while True:  # $label0
        if not arg0:
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

# ----------------------------------------------------------
# $Wd
# Export: Wd
# ----------------------------------------------------------
def Wd():
    """Export: Wd"""
    while True:  # $label3
        while True:  # $label1
            while True:  # $label0
                v3 = ((v1 * 404) + ENTITY_TYPES)
                # br_table load32(((v1 * 404) + ENTITY_TYPES) + 264)
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
    v5 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
    store32(9685864, func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2))))
    while True:  # $label16
        while True:  # $label5
            while True:  # $label4
                v1 = ((v10 * 404) + ENTITY_TYPES)
                # br_table load32(((v10 * 404) + ENTITY_TYPES) + 264)
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
            while True:  # $label7
                v2 = load32(v1 + 236)
                if not load32(v1 + 236):
                    break
                v8 = (v2 & 3)
                v0 = load32(v1 + 232)
                v4 = 0
                while True:  # $label8
                    if (u32(v2) < u32(4)):
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
                if not v8:
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
            while True:  # $label11
                v0 = load32(v1 + 364)
                if not load32(v1 + 364):
                    break
                v7 = (v0 & 3)
                v1 = load32(v1 + 24)
                v8 = 0
                while True:  # $label12
                    if (u32(v0) < u32(4)):
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
                if not v7:
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

# ----------------------------------------------------------
# $Ud
# Export: Ud
# ----------------------------------------------------------
def Ud(arg0):
    """Export: Ud"""
    while True:  # $label0
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
    arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
    store32(9142908, func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2))))
    return arg0

# ----------------------------------------------------------
# $Ze
# Export: Ze
# ----------------------------------------------------------
def Ze(arg0, arg1):
    """Export: Ze"""
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
    while True:  # $label0
        arg1 = load32(9215892)
        if (load32(9215892) != load32(9215888)):
            arg0 = load32(9215884)
            break
        arg0 = (load32(9215896) + arg1)
        store32(9215888, (load32(9215896) + arg1))
        v2 = load32(9215884)
        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg1:
            # TODO: memory.copy
        if v2:
            arg1 = load32(9215892)
        store32(9215884, arg0)
        break
    store32(9215892, (arg1 + 1))
    store32((arg0 + (arg1 << 2)), 0)
    while True:  # $label1
        arg1 = load32(9215892)
        if (load32(9215892) != load32(9215888)):
            v2 = arg0
            break
        v2 = (load32(9215896) + arg1)
        store32(9215888, (load32(9215896) + arg1))
        v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
        if arg1:
            # TODO: memory.copy
        store32(9215884, v2)
        arg1 = load32(9215892)
        break
    store32(9215892, (arg1 + 1))
    store32((v2 + (arg1 << 2)), 0)
    while True:  # $label2
        arg1 = load32(9215892)
        if (load32(9215892) != load32(9215888)):
            arg0 = v2
            break
        arg0 = (load32(9215896) + arg1)
        store32(9215888, (load32(9215896) + arg1))
        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg1:
            # TODO: memory.copy
        store32(9215884, arg0)
        arg1 = load32(9215892)
        break
    store32(9215892, (arg1 + 1))
    store32((arg0 + (arg1 << 2)), 0)
    while True:  # $label3
        arg1 = load32(9215892)
        if (load32(9215892) != load32(9215888)):
            v2 = arg0
            break
        v2 = (load32(9215896) + arg1)
        store32(9215888, (load32(9215896) + arg1))
        v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
        if arg1:
            # TODO: memory.copy
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
    store32(GAME_STATE, func26(188))
    # TODO: memory.copy
    store32(9142428, 47)
    v3 = load32(38868)
    while True:  # $label4
        arg1 = load32(9681452)
        arg0 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg1 = load32(9681448)
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        v2 = load32(9681448)
        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if arg0:
            # TODO: memory.copy
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
    while True:  # $label5
        arg0 = load32(9681452)
        v2 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg0 = arg1
            break
        arg0 = ((arg0 + load32(9681460)) + 3)
        store32(9681452, ((arg0 + load32(9681460)) + 3))
        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if v2:
            # TODO: memory.copy
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
    while True:  # $label6
        arg1 = load32(9681452)
        v2 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg1 = arg0
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy
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
    while True:  # $label7
        arg0 = load32(9681452)
        v2 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg0 = arg1
            break
        arg0 = ((arg0 + load32(9681460)) + 3)
        store32(9681452, ((arg0 + load32(9681460)) + 3))
        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if v2:
            # TODO: memory.copy
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
    while True:  # $label8
        arg1 = load32(9681452)
        v2 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg1 = arg0
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy
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
    while True:  # $label9
        arg0 = load32(9681452)
        v2 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg0 = arg1
            break
        arg0 = ((arg0 + load32(9681460)) + 3)
        store32(9681452, ((arg0 + load32(9681460)) + 3))
        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if v2:
            # TODO: memory.copy
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
    while True:  # $label10
        arg1 = load32(9681452)
        v2 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg1 = arg0
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy
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
    while True:  # $label11
        arg0 = load32(9681452)
        v2 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg0 = arg1
            break
        arg0 = ((arg0 + load32(9681460)) + 3)
        store32(9681452, ((arg0 + load32(9681460)) + 3))
        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if v2:
            # TODO: memory.copy
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
    while True:  # $label12
        arg1 = load32(9681452)
        v2 = load32(9681456)
        if (u32(load32(9681452)) > u32((load32(9681456) + 3))):
            arg1 = arg0
            break
        arg1 = ((arg1 + load32(9681460)) + 3)
        store32(9681452, ((arg1 + load32(9681460)) + 3))
        arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
        if v2:
            # TODO: memory.copy
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

# ----------------------------------------------------------
# $Je
# Export: Je
# ----------------------------------------------------------
def Je(arg0):
    """Export: Je"""
    arg0 = players[arg0]
    return (((load8u((players[arg0] + 283973)) << 8) | load8u((arg0 + 283974))) | (load8u(arg0 + 283972) << 16))

# ----------------------------------------------------------
# $Q
# Export: Q
# ----------------------------------------------------------
def Q(arg0, arg1, arg2):
    """Export: Q"""
    v3 = load32(PLAYERS)
    if arg2:
        store32((((v3 + (arg0 * 286704)) + (arg1 << 2)) + 283984), (arg2 - 1))
    if (arg1 == 97):
        arg2 = (v3 + (arg0 * 286704))
        store32((v3 + (arg0 * 286704)) + 283868, load32((arg2 + 284372)))
    return load32((((v3 + (arg0 * 286704)) + (arg1 << 2)) + 283984))

# ----------------------------------------------------------
# $R
# Export: R
# ----------------------------------------------------------
def R(arg0, arg1, arg2, arg3):
    """Export: R"""
    v4 = load32(PLAYERS)
    while True:  # $label0
        if not arg1:
            break
        v5 = (v4 + (arg0 * 286704))
        arg1 = (arg1 - 1)
        store32(((v4 + (arg0 * 286704)) + (286688 if arg2 else 286684)), (100 if (u32(arg1) >= u32(100)) else (arg1 - 1)))
        if not arg3:
            break
        if load32(v5 + 286688):
            break
        store32((v5 + 286688), 100)
        break
    return load32(((v4 + (arg0 * 286704)) + (286688 if arg2 else 286684)))

# ----------------------------------------------------------
# $De
# Export: De
# ----------------------------------------------------------
def De(arg0, arg1, arg2):
    """Export: De"""
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
                while True:  # $label0
                    if (u32(v3) <= u32(v7)):
                        break
                    if (u32(v3) <= u32(v4)):
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
                    while True:  # $label3
                        if (u32(v5) <= u32(v7)):
                            break
                        if (u32(v4) >= u32(v5)):
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
        v12 = (u32(v4) < u32(4))
        v3 = 0
        while True:  # $label12
            while True:  # $label9
                if not ((arg1 < v3) & (v3 < v8)):
                    arg0 = 0
                    v5 = 0
                    if (v4 != 1):
                        while True:  # $label8
                            while True:  # $label6
                                if (arg0 <= arg1):
                                    break
                                if (arg0 >= v8):
                                    break
                                store8((load32(9147288) + ((load32(9142440) * arg0) + v3)), 3)
                                break
                            while True:  # $label7
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
                    if not v11:
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
                if not v12:
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
                if not arg2:
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
    # TODO: i32.div_u
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
                while True:  # $label13
                    v4 = (arg0 - v7)
                    if ((v8 + ((arg0 - v7) * v4)) > v5):
                        break
                    v4 = load32(9142440)
                    if (u32(load32(9142440)) <= u32(arg0)):
                        break
                    if ((arg0 | arg1) < 0):
                        break
                    if (u32(arg1) >= u32(v4)):
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
    # TODO: i32.div_u
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
                while True:  # $label16
                    v6 = (arg0 - v7)
                    if ((v5 + ((arg0 - v7) * v6)) > v4):
                        break
                    v6 = load32(9142440)
                    if (u32(load32(9142440)) <= u32(arg0)):
                        break
                    if ((arg0 | arg1) < 0):
                        break
                    if (u32(arg1) >= u32(v6)):
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
                while True:  # $label19
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
                if (u32((arg0 + 1)) < u32(v3)):
                    continue
                break
            v5 = arg1
            if (u32(arg1) < u32(v3)):
                continue
            break
    func169()
    return func343()

# ----------------------------------------------------------
# $Zd
# Export: Zd
# ----------------------------------------------------------
def Zd():
    """Export: Zd"""
    while True:  # $label1
        v3 = ((v1 * 404) + ENTITY_TYPES)
        if (load32(((v1 * 404) + ENTITY_TYPES) + 264) == 1):
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
    v6 = func26((-1 if (u32(v0) > u32(1073741823)) else (v0 << 2)))
    store32(9685864, func26((-1 if (u32(v0) > u32(1073741823)) else (v0 << 2))))
    while True:  # $label16
        v1 = 0
        v0 = 0
        v2 = ((v11 * 404) + ENTITY_TYPES)
        if (load32(((v11 * 404) + ENTITY_TYPES) + 264) == 1):
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
            # TODO: memory.fill
            while True:  # $label3
                if not v4:
                    break
                v10 = (v4 & 3)
                v5 = load32(v2 + 232)
                v1 = 0
                while True:  # $label4
                    if (u32(v4) < u32(4)):
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
                if not v10:
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
            while True:  # $label7
                if not v8:
                    break
                v7 = (v8 & 3)
                v4 = load32(v2 + 372)
                v10 = 0
                while True:  # $label8
                    if (u32(v8) < u32(4)):
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
                if not v7:
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
            while True:  # $label11
                if not v9:
                    break
                v5 = (v9 & 3)
                v2 = load32(v2 + 24)
                v8 = 0
                while True:  # $label12
                    if (u32(v9) < u32(4)):
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
                if not v5:
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

# ----------------------------------------------------------
# $Sd
# Export: Sd
# ----------------------------------------------------------
def Sd(arg0, arg1, arg2):
    """Export: Sd"""
    while True:  # $label0
        v3 = ((arg0 * 404) + ENTITY_TYPES)
        if load8u(((arg0 * 404) + ENTITY_TYPES) + 378):
            break
        v3 = load32(v3 + 264)
        while True:  # $label1
            if arg2:
                if not v3:
                    break
                break
            if (v3 != 1):
                break
            break
        arg2 = 0
        while True:  # $label3
            while True:  # $label2
                if load8u(((arg2 * 404) + ENTITY_TYPES) + 378):
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

# ----------------------------------------------------------
# $Bb
# Export: Bb
# ----------------------------------------------------------
def Bb(arg0):
    """Export: Bb"""
    while True:  # $label0
        v1 = ((arg0 * 404) + ENTITY_TYPES)
        arg0 = load32(((arg0 * 404) + ENTITY_TYPES) + 236)
        if not load32(((arg0 * 404) + ENTITY_TYPES) + 236):
            arg0 = 0
            break
        v5 = (arg0 & 1)
        v2 = load32(v1 + 232)
        while True:  # $label1
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
        if not v5:
            break
        v1 = load32((v2 + (v1 << 2)))
        if not load8u(((load32((v2 + (v1 << 2))) * 132) + 9216080) + 23):
            break
        store32(((arg0 << 2) + 9147392), v1)
        arg0 = (arg0 + 1)
        break
    store32(((arg0 << 2) + 9147392), -1)

# ----------------------------------------------------------
# $Ce
# Export: Ce
# ----------------------------------------------------------
def Ce(arg0):
    """Export: Ce"""
    func182()
    if not arg0:
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
                    while True:  # $label0
                        if (u32(v1) >= u32(v2)):
                            break
                        if (u32(v2) <= u32(v4)):
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

# ----------------------------------------------------------
# $Zb
# Export: Zb
# ----------------------------------------------------------
def Zb(arg0):
    """Export: Zb"""
    while True:  # $label2
        while True:  # $label0
            v1 = load32(((arg0 + (v2 << 2)) + 284636))
            if not load32(((arg0 + (v2 << 2)) + 284636)):
                break
            v3 = load32(v1 + 8)
            if not load32(v1 + 8):
                break
            v4 = load32(v1)
            v1 = 0
            while True:  # $label1
                v5 = load32((v4 + (v1 << 2)))
                if not load32((v4 + (v1 << 2))):
                    v1 = (v1 + 1)
                    if (v3 != (v1 + 1)):
                        continue
                    break
                break
            v2 = entities[v5]
            v1 = ((load8u(entities[v5].sub_state) * 404) + ENTITY_TYPES)
            store32(arg0 + 283896, (((load32(((load8u(entities[v5].sub_state) * 404) + ENTITY_TYPES) + 216) & 0xFFFFFFFF) >> 1) + load16u(v2 + 112)))
            store32(arg0 + 283900, (load16u(v2 + 114) + ((load32(v1 + 220) & 0xFFFFFFFF) >> 1)))
            return
            break
        v2 = (v2 + 1)
        if ((v2 + 1) != 255):
            continue
        break

# ----------------------------------------------------------
# $Ne
# Export: Ne
# ----------------------------------------------------------
def Ne():
    """Export: Ne"""
    v0 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)

# ----------------------------------------------------------
# $Mc
# Export: Mc
# ----------------------------------------------------------
def Mc(arg0):
    """Export: Mc"""
    v10 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    v3 = func26(4)
    v7 = func26(4)
    v8 = func26(4)
    v9 = func26(4)
    v1 = load32(9568076)
    while True:  # $label5
        while True:  # $label2
            while True:  # $label1
                while True:  # $label3
                    if (arg0 == 1):
                        while True:  # $label0
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
                                # TODO: memory.copy
                                store32(arg0 + 192, 0)
                                arg0 = (arg0 + 196)
                                store32(v1 + 16, (arg0 + 196))
                                break
                            v4 = load32((v1 + 12))
                            v6 = (arg0 - load32((v1 + 12)))
                            arg0 = ((arg0 - load32((v1 + 12))) // 196)
                            v2 = (((arg0 - load32((v1 + 12))) // 196) + 1)
                            if (u32((((arg0 - load32((v1 + 12))) // 196) + 1)) >= u32(21913099)):
                                break
                            v11 = (arg0 << 1)
                            v2 = (21913098 if (u32(arg0) >= u32(10956549)) else ((arg0 << 1) if (u32(v2) < u32(v11)) else v2))
                            if (21913098 if (u32(arg0) >= u32(10956549)) else ((arg0 << 1) if (u32(v2) < u32(v11)) else v2)):
                                if (u32(v2) >= u32(21913099)):
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
                            # TODO: memory.copy
                            store32(v1 + 20, (v5 + (v2 * 196)))
                            arg0 = (arg0 + 196)
                            store32(v1 + 16, (arg0 + 196))
                            store32(v1 + 12, v3)
                            if not v4:
                                break
                            v1 = load32(9568076)
                            arg0 = load32(load32(9568076) + 16)
                            break
                        v1 = (v1 + 12)
                        break
                    while True:  # $label4
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
                            # TODO: memory.copy
                            store32(arg0 + 192, 0)
                            store32(v1 + 4, (arg0 + 196))
                            break
                        v4 = load32(v1)
                        v6 = (arg0 - load32(v1))
                        arg0 = ((arg0 - load32(v1)) // 196)
                        v2 = (((arg0 - load32(v1)) // 196) + 1)
                        if (u32((((arg0 - load32(v1)) // 196) + 1)) >= u32(21913099)):
                            break
                        v11 = (arg0 << 1)
                        v2 = (21913098 if (u32(arg0) >= u32(10956549)) else ((arg0 << 1) if (u32(v2) < u32(v11)) else v2))
                        if (21913098 if (u32(arg0) >= u32(10956549)) else ((arg0 << 1) if (u32(v2) < u32(v11)) else v2)):
                            if (u32(v2) >= u32(21913099)):
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
                        # TODO: memory.copy
                        store32(v1 + 8, (v5 + (v2 * 196)))
                        store32(v1 + 4, (arg0 + 196))
                        store32(v1, v3)
                        if not v4:
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
            raise Unreachable()
            break
        func68()
        raise Unreachable()
        break
    func42()
    raise Unreachable()
    return af(v4)

# ----------------------------------------------------------
# $S
# Export: S
# ----------------------------------------------------------
def S(arg0, arg1):
    """Export: S"""
    v6 = load32(PLAYERS)
    if not arg1:
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
        arg1 = load32(PLAYER_COUNT)
        if load32(PLAYER_COUNT):
            v9 = (v6 + (arg0 * 286704))
            v10 = ((v6 + (arg0 * 286704)) + 286688)
            v11 = (v9 + 286684)
            v4 = 0
            while True:  # $label3
                v2 = (v6 + (v4 * 286704))
                if (arg0 != load32((v6 + (v4 * 286704)) + 283908)):
                    while True:  # $label1
                        arg1 = load32(v11)
                        if not load32(v11):
                            break
                        if not v4:
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
                    arg1 = load32(PLAYER_COUNT)
                v4 = (v4 + 1)
                if (u32((v4 + 1)) < u32(arg1)):
                    continue
                break
        return
    arg0 = (v6 + (arg0 * 286704))
    store32((v6 + (arg0 * 286704)) + 283868, load32(9561460))
    # TODO: memory.copy
    arg1 = load32(GAME_STATE)
    store32((arg0 + 284000), load32(load32(GAME_STATE) + 40))
    store32((arg0 + 284136), load32(arg1 + 36))

# ----------------------------------------------------------
# $Hd
# Export: Hd
# ----------------------------------------------------------
def Hd(arg0):
    """Export: Hd"""
    v1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    store32(9684792, load32(((arg0 << 2) + 9140336)))
    store8(9681884, 0)
    arg0 = load32(9142880)
    while True:  # $label0
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
    if not load32(9684796):
        while True:  # $label1
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
            if (u32(v2) < u32(load32(9163784))):
                break
            store32(v1, v3)
            a_b()
            store32(9163784, (load32(9163784) + 40000))
            break
        store32(9684796, arg0)
    G.global0 = (v1 - -64)

# ----------------------------------------------------------
# $Oc
# Export: Oc
# ----------------------------------------------------------
def Oc(arg0, arg1):
    """Export: Oc"""
    if arg1:
        v5 = load32(9568088)
        while True:  # $label0
            if not arg0:
                break
            arg1 = 0
            if (u32(arg0) >= u32(4)):
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
            if not (arg0 & 3):
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
    while True:  # $label3
        if not arg0:
            break
        arg1 = 0
        if (u32(arg0) >= u32(4)):
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
        if not (arg0 & 3):
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

# ----------------------------------------------------------
# $Fe
# Export: Fe
# ----------------------------------------------------------
def Fe(arg0):
    """Export: Fe"""
    v2 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        v4 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v3 = 1
        v1 = 1
        while True:  # $label1
            while True:  # $label3
                while True:  # $label2
                    # br_table arg0
                    break
                    break
                v10 = (arg0 - 2)
                v11 = (arg0 - 1)
                while True:  # $label7
                    store8(9147208, 1)
                    v8 = players[arg0]
                    while True:  # $label4
                        if (u32(arg0) <= u32(1)):
                            break
                        v3 = (v6 + v11)
                        v9 = ((v6 + v11) & 3)
                        v5 = load32(9143004)
                        v1 = 1
                        if (u32((v6 + v10)) >= u32(3)):
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
                        if not v9:
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
                    v4 = load32(PLAYER_COUNT)
                    if (u32((arg0 + 1)) < u32(load32(PLAYER_COUNT))):
                        continue
                    break
                break
                break
            while True:  # $label8
                arg0 = players[v3]
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
                if (u32((v3 + 1)) < u32(load32(PLAYER_COUNT))):
                    continue
                break
            break
            break
        while True:  # $label9
            arg0 = players[v1]
            v3 = load8u(players[v1] + 283972)
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
            if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
        break
    G.global0 = (v2 - -64)

# ----------------------------------------------------------
# $Ye
# Export: Ye
# ----------------------------------------------------------
def Ye():
    """Export: Ye"""
    v5 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v3 = load32(9684496)
        v1 = load32((load32(9684496) - 16))
        if not load32((load32(9684496) - 16)):
            break
        if (u32(v1) >= u32(4)):
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
        if not (v1 & 3):
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
    while True:  # $label3
        v3 = load32(9140328)
        if not load32(9140328):
            break
        v6 = 0
        v0 = load32(9142440)
        v2 = (load32(9142440) * v0)
        v0 = 0
        if (u32(v3) >= u32(4)):
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
        if not (v3 & 3):
            break
        while True:  # $label5
            v1 = ((((v2 * load32(load32(((v0 << 2) + 9140336)) + 44)) & 0xFFFFFFFF) >> 16) + v1)
            v0 = (v0 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v3):
                continue
            break
        break
    if not load32(9681936):
        v0 = func26(16)
        v2 = (v1 << 2)
        store32(func26(16) + 4, (v1 << 2))
        store32(v0, func26((-1 if (u32(v2) > u32(1073741823)) else (v1 << 4))))
        store64(v0 + 8, 206158430208)
        store32(9681936, v0)
    store8(59182, 0)
    if not load8u(9142917):
        v0 = (load32(9142440) << 4)
        store32(v5, (load32(9142440) << 4))
        store32(v5 + 4, v0)
    G.global0 = (v5 + 16)

# ----------------------------------------------------------
# $Vb
# Export: Vb
# ----------------------------------------------------------
def Vb(arg0, arg1, arg2):
    """Export: Vb"""
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        if not load8u(9147210):
            func176(arg2, load32(CURRENT_PLAYER), not arg1)
            break
        while True:  # $label1
            if not arg1:
                break
            if not load32(9147132):
                break
            if (load32(9142440) != 4096):
                break
            v5 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            arg2 = 1
            v6 = (v5 - 1)
            v10 = ((v5 - 1) & 1)
            v7 = load32(players[load32(CURRENT_PLAYER)] + 283908)
            v8 = (load32(players[load32(CURRENT_PLAYER)] + 283908) * v5)
            v9 = load32(9143004)
            if (v5 != 2):
                v6 = (v6 & -2)
                v5 = 0
                while True:  # $label2
                    v3 = (arg2 + 1)
                    v3 = ((v3 + (not load8u((v9 + (arg2 + v8))) & (arg2 != v7))) + (not load8u((v9 + ((arg2 + 1) + v8))) & (v3 != v7)))
                    arg2 = (arg2 + 2)
                    v5 = (v5 + 2)
                    if ((v5 + 2) != v6):
                        continue
                    break
            if v10:
            else:
            if (u32(v3) < u32(3)):
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

# ----------------------------------------------------------
# $Ub
# Export: Ub
# ----------------------------------------------------------
def Ub(arg0, arg1, arg2):
    """Export: Ub"""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(v3 + 12, arg2)
    store32(v3 + 8, arg1)
    store32(v3 + 4, arg0)
    while True:  # $label0
        if load8u(9147210):
            func41(40, 0, 0, (v3 + 4), 3)
            break
        break
    G.global0 = (v3 + 16)

# ----------------------------------------------------------
# $W
# Export: W
# ----------------------------------------------------------
def W(arg0, arg1):
    """Export: W"""
    arg0 = players[arg0]
    if load8u(players[arg0] + 286699):

# ----------------------------------------------------------
# $Ue
# Export: Ue
# ----------------------------------------------------------
def Ue(arg0, arg1):
    """Export: Ue"""
    if (load32(9142912) if arg0 else 1):
        arg0 = load32(9142908)
        if load32(9142908):
            store32(9142908, 0)
        store32(9142912, 0)
        func272()
        func271()
        func220()
        func218()

# ----------------------------------------------------------
# $Ma
# Export: Ma
# ----------------------------------------------------------
def Ma():
    """Export: Ma"""
    v1 = load32(PLAYER_COUNT)
    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
        v2 = load32(PLAYERS)
        v0 = 1
        while True:  # $label1
            while True:  # $label0
                v3 = (v2 + (v0 * 286704))
                v4 = load32((v2 + (v0 * 286704)) + 284616)
                if not load32((v2 + (v0 * 286704)) + 284616):
                    break
                if load32(v3 + 284632):
                    break
                if (load32(v3 + 283908) == load32(CURRENT_PLAYER)):
                    break
                La(v4, 0)
                v1 = load32(PLAYER_COUNT)
                v2 = load32(PLAYERS)
                break
            v0 = (v0 + 1)
            if (u32((v0 + 1)) < u32(v1)):
                continue
            break

# ----------------------------------------------------------
# $Qc
# Export: Qc
# ----------------------------------------------------------
def Qc(arg0):
    """Export: Qc"""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(9684424)
    while True:  # $label0
        if arg0:
            v5 = load32(v2 + 8)
            if not load32(v2 + 8):
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
            if (u32(arg0) <= u32(v1)):
                break
            while True:  # $label2
                v1 = (v1 + 1)
                store32((v4 + (v1 << 2)), load32((v4 + ((v1 + 1) << 2))))
                if (u32(v1) < u32(load32(v2 + 8))):
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

# ----------------------------------------------------------
# $Yb
# Export: Yb
# ----------------------------------------------------------
def Yb(arg0):
    """Export: Yb"""
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v2 = 3
    v1 = load32(PLAYER_COUNT)
    if (u32(load32(PLAYER_COUNT)) >= u32(3)):
        if (u32(load32(9671136)) > u32(3)):
            while True:  # $label2
                while True:  # $label0
                    v1 = entities[v2]
                    if (load8u(entities[v2].unit_class) == 3):
                        break
                    v3 = load16u(v1 + 110)
                    if (arg0 == load16u(v1 + 110)):
                        break
                    if (u32(arg0) >= u32(v3)):
                        break
                    v4 = (v3 - 1)
                    store16(v1 + 110, (v3 - 1))
                    store8(v1 + 127, 0)
                    while True:  # $label1
                        v3 = load32(v1 + 40)
                        if not load32(v1 + 40):
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
                    if not load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 20):
                        break
                    break
                v2 = (v2 + 1)
                if (u32((v2 + 1)) < u32(load32(9671136))):
                    continue
                break
            v1 = load32(PLAYER_COUNT)
        v9 = (v1 - 1)
        if (u32((v1 - 1)) >= u32(2)):
            v4 = load32(9143004)
            v10 = (v1 & 1)
            v12 = (v1 - 3)
            v11 = (v1 - 2)
            v13 = ((v1 - 2) & -2)
            v3 = 1
            while True:  # $label4
                v6 = (v3 + (u32(arg0) <= u32(v3)))
                v8 = 0
                v2 = 1
                if v12:
                    while True:  # $label3
                        v7 = (v2 + 1)
                        store8((v4 + ((v1 * v2) + v3)), load8u((v4 + (v6 + ((v2 if (u32(arg0) > u32(v2)) else (v2 + 1)) * v1)))))
                        v2 = (v2 + 2)
                        store8((v4 + ((v1 * v7) + v3)), load8u((v4 + (v6 + ((v7 if (u32(arg0) > u32(v7)) else (v2 + 2)) * v1)))))
                        v8 = (v8 + 2)
                        if ((v8 + 2) != v13):
                            continue
                        break
                if v10:
                    store8((v4 + ((v1 * v2) + v3)), load8u((v4 + (v6 + ((v2 + (u32(arg0) <= u32(v2))) * v1)))))
                v3 = (v3 + 1)
                if ((v3 + 1) != v9):
                    continue
                break
            v10 = (v11 & -2)
            v11 = (v1 & 1)
            v4 = load32(9143012)
            v3 = 1
            while True:  # $label6
                v6 = (v3 + (u32(arg0) <= u32(v3)))
                v2 = 1
                v8 = 0
                if v12:
                    while True:  # $label5
                        v7 = (v2 + 1)
                        store8((v4 + ((v1 * v2) + v3)), load8u((v4 + (v6 + ((v2 if (u32(arg0) > u32(v2)) else (v2 + 1)) * v1)))))
                        v2 = (v2 + 2)
                        store8((v4 + ((v1 * v7) + v3)), load8u((v4 + (v6 + ((v7 if (u32(arg0) > u32(v7)) else (v2 + 2)) * v1)))))
                        v8 = (v8 + 2)
                        if ((v8 + 2) != v10):
                            continue
                        break
                if v11:
                    store8((v4 + ((v1 * v2) + v3)), load8u((v4 + (v6 + ((v2 + (u32(arg0) <= u32(v2))) * v1)))))
                v3 = (v3 + 1)
                if ((v3 + 1) != v9):
                    continue
                break
        store32(PLAYER_COUNT, v9)
        if (u32(arg0) < u32(v9)):
            v3 = load32(PLAYERS)
            v1 = arg0
            while True:  # $label7
                v2 = (v3 + (v1 * 286704))
                # TODO: memory.copy
                store32(v2 + 283908, v1)
                v1 = (v1 + 1)
                v2 = load32(PLAYER_COUNT)
                if (u32((v1 + 1)) < u32(load32(PLAYER_COUNT))):
                    continue
                break
        else:
        func284(arg0)
    G.global0 = (v5 + 32)
    return 0

# ----------------------------------------------------------
# $Kc
# Export: Kc
# ----------------------------------------------------------
def Kc():
    """Export: Kc"""
    v0 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v2 = 1
    if (u32(load32(PLAYER_COUNT)) > u32(1)):
        while True:  # $label0
            v1 = players[v2]
            v3 = load32(players[v2] + 283908)
            v4 = load32(v1 + 284608)
            v5 = load8u((v1 + 283974))
            v6 = load8u((v1 + 283973))
            store32(v0 + 16, load8u(v1 + 283972))
            store32(v0 + 20, v6)
            store32(v0 + 24, v5)
            store32(v0, v2)
            store32(v0 + 4, v1)
            store32(v0 + 8, v4)
            store32(v0 + 12, (v3 == load32(CURRENT_PLAYER)))
            v2 = (v2 + 1)
            if (u32((v2 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
    G.global0 = (v0 + 32)

# ----------------------------------------------------------
# $Sc
# Export: Sc
# ----------------------------------------------------------
def Sc(arg0):
    """Export: Sc"""
    v3 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v4 = load32(9568088)
    v6 = ((load32(9568088) + 96) if arg0 else (v4 + 80))
    store32(9684424, ((load32(9568088) + 96) if arg0 else (v4 + 80)))
    v5 = load32(v6 + 8)
    if load32(v6 + 8):
        v7 = load32((v4 + (96 if arg0 else 80)))
        v8 = load32(ENTITIES)
        v2 = v5
        while True:  # $label1
            if (load8u((v8 + (load32((v7 + (v1 << 2))) * 132)) + 125) == 3):
                v2 = (v2 - 1)
                store32(v6 + 8, (v2 - 1))
                arg0 = v1
                if (u32(v1) < u32(v2)):
                    while True:  # $label0
                        arg0 = (arg0 + 1)
                        store32((v7 + (arg0 << 2)), load32((v7 + ((arg0 + 1) << 2))))
                        v2 = load32(v6 + 8)
                        if (u32(arg0) < u32(load32(v6 + 8))):
                            continue
                        break
                v1 = (v1 - 1)
            v1 = (v1 + 1)
            if (u32((v1 + 1)) < u32(v2)):
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

# ----------------------------------------------------------
# $Pc
# Export: Pc
# ----------------------------------------------------------
def Pc(arg0):
    """Export: Pc"""
    v3 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    while True:  # $label2
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
                    v1 = entities[load32((load32(v6) + (v2 << 2)))]
                    v4 = load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 156)
                    store8(entities[load32((load32(v6) + (v2 << 2)))] + 127, load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 156))
                    while True:  # $label0
                        v5 = load32(v1 + 40)
                        if not load32(v1 + 40):
                            break
                        v1 = (v4 if v4 else (load16u(v1 + 110) + 16))
                        if load8u(9142916):
                            v4 = 0
                            if (u32(v1) <= u32(15)):
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
                    if (u32((v2 + 1)) < u32(load32(v6 + 8))):
                        continue
                    break
            G.global0 = (arg0 + 32)
            break
        if not load32(9213808):
            break
        v2 = load32(9684424)
        if not arg0:
            while True:  # $label7
                v4 = load32(((v6 << 2) + 9173808))
                v7 = load32(ENTITIES)
                while True:  # $label3
                    v5 = load32(v2 + 8)
                    if not load32(v2 + 8):
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
                    if (u32(arg0) >= u32(v5)):
                        break
                    while True:  # $label5
                        arg0 = (arg0 + 1)
                        store32((v1 + (arg0 << 2)), load32((v1 + ((arg0 + 1) << 2))))
                        if (u32(arg0) < u32(load32(v2 + 8))):
                            continue
                        break
                    break
                arg0 = (v7 + (v4 * 132))
                v1 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 156)
                store8((v7 + (v4 * 132)) + 127, load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 156))
                while True:  # $label6
                    v4 = load32(arg0 + 40)
                    if not load32(arg0 + 40):
                        break
                    arg0 = (v1 if v1 else (load16u(arg0 + 110) + 16))
                    if load8u(9142916):
                        v1 = 0
                        if (u32(arg0) <= u32(15)):
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
                if (u32((v6 + 1)) < u32(load32(9213808))):
                    continue
                break
                break
            raise Unreachable()
        while True:  # $label12
            v4 = load32(((v6 << 2) + 9173808))
            v7 = load32(ENTITIES)
            while True:  # $label8
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
                while True:  # $label10
                    if (load32(v2 + 4) != v1):
                        arg0 = load32(v2)
                        break
                    arg0 = (load32(v2 + 12) + v1)
                    store32(v2 + 4, (load32(v2 + 12) + v1))
                    v5 = load32(v2)
                    arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                    if v1:
                        # TODO: memory.copy
                    if v5:
                        v1 = load32(v2 + 8)
                    store32(v2, arg0)
                    break
                store32(v2 + 8, (v1 + 1))
                store32((arg0 + (v1 << 2)), v4)
                break
            while True:  # $label11
                arg0 = load32((v7 + (v4 * 132)) + 40)
                if not load32((v7 + (v4 * 132)) + 40):
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
            if (u32((v6 + 1)) < u32(load32(9213808))):
                continue
            break
        break
    G.global0 = (v3 + 80)

# ----------------------------------------------------------
# $Tc
# Export: Tc
# ----------------------------------------------------------
def Tc(arg0):
    """Export: Tc"""
    arg0 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v1 = load32(9684424)
    if load32(load32(9684424) + 8):
        while True:  # $label1
            while True:  # $label0
                v1 = load32(entities[load32((load32(v1) + (v2 << 2)))].target_id)
                if not load32(entities[load32((load32(v1) + (v2 << 2)))].target_id):
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
            if (u32((v2 + 1)) < u32(load32(load32(9684424) + 8))):
                continue
            break
    G.global0 = (arg0 + 32)

# ----------------------------------------------------------
# $Ka
# Export: Ka
# ----------------------------------------------------------
def Ka(arg0):
    """Export: Ka"""
    while True:  # $label1
        while True:  # $label0
            if arg0:
                if not load8u(9147212):
                    break
            v1 = load32(PLAYER_COUNT)
            break
            break
        v1 = load32(41092)
        store32(PLAYER_COUNT, load32(41092))
        break
    store32(41092, 1)
    store8(9147210, 0)
    store8(9142388, 0)
    store32(9142384, 0)
    while True:  # $label2
        if arg0:
            break
        if not v1:
            break
        store32(PLAYER_COUNT, 0)
        arg0 = load32(PLAYERS)
        if load32(PLAYERS):
            store32(PLAYERS, 0)
        break

# ----------------------------------------------------------
# $Xe
# Export: Xe
# ----------------------------------------------------------
def Xe(arg0):
    """Export: Xe"""
    store32(9687276, arg0)
    if not arg0:
        la()

# ----------------------------------------------------------
# $Qa
# Export: Qa
# ----------------------------------------------------------
def Qa(arg0):
    """Export: Qa"""
    v2 = 1
    while True:  # $label0
        v3 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v4 = load32(PLAYERS)
        v1 = 1
        while True:  # $label1
            if (arg0 != load32((v4 + (v1 * 286704)) + 284616)):
                v1 = (v1 + 1)
                if ((v1 + 1) != v3):
                    continue
                break
            break
        v2 = (load8u((load32(9143004) + (load32((v4 + (v1 * 286704)) + 283908) + (load32(CURRENT_PLAYER) * v3)))) != 0)
        break
    return v2

# ----------------------------------------------------------
# $Vc
# Export: Vc
# ----------------------------------------------------------
def Vc(arg0, arg1):
    """Export: Vc"""
    v3 = (64 if arg1 else 48)
    while True:  # $label0
        v2 = load32(9568088)
        v4 = ((load32(9568088) - -64) if arg1 else (v2 + 48))
        arg1 = load32(((load32(9568088) - -64) if arg1 else (v2 + 48)) + 8)
        if (u32(arg0) < u32(load32(((load32(9568088) - -64) if arg1 else (v2 + 48)) + 8))):
            v2 = load32((v2 + v3))
            break
        while True:  # $label1
            v6 = load32(PLAYER_COUNT)
            v7 = (load32(PLAYER_COUNT) + 1)
            if (u32((load32(PLAYER_COUNT) + 1)) <= u32(arg1)):
                v2 = load32((v2 + v3))
                break
            v3 = (v2 + v3)
            while True:  # $label3
                while True:  # $label2
                    if (load32(v4 + 4) != arg1):
                        v2 = load32(v3)
                        break
                    v2 = (load32(v4 + 12) + arg1)
                    store32(v4 + 4, (load32(v4 + 12) + arg1))
                    v5 = load32(v3)
                    v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                    if arg1:
                        # TODO: memory.copy
                    if v5:
                        arg1 = load32(v4 + 8)
                    store32(v3, v2)
                    break
                store32(v4 + 8, (arg1 + 1))
                store32((v2 + (arg1 << 2)), 1)
                arg1 = load32(v4 + 8)
                if (u32(load32(v4 + 8)) < u32(v7)):
                    continue
                break
            break
        store32((v2 + (v6 << 2)), 0)
        break
    return load32((v2 + (arg0 << 2)))

# ----------------------------------------------------------
# $Uc
# Export: Uc
# ----------------------------------------------------------
def Uc(arg0, arg1, arg2):
    """Export: Uc"""
    v9 = (64 if arg2 else 48)
    v5 = load32(9568088)
    v3 = ((load32(9568088) - -64) if arg2 else (v5 + 48))
    arg2 = load32(((load32(9568088) - -64) if arg2 else (v5 + 48)) + 8)
    v6 = (load32(PLAYER_COUNT) + 1)
    if (u32(load32(((load32(9568088) - -64) if arg2 else (v5 + 48)) + 8)) < u32((load32(PLAYER_COUNT) + 1))):
        v7 = (v5 + v9)
        while True:  # $label1
            while True:  # $label0
                if (load32(v3 + 4) != arg2):
                    v4 = load32(v7)
                    break
                v4 = (load32(v3 + 12) + arg2)
                store32(v3 + 4, (load32(v3 + 12) + arg2))
                v8 = load32(v7)
                v4 = func26((-1 if (u32(v4) > u32(1073741823)) else (v4 << 2)))
                if arg2:
                    # TODO: memory.copy
                if v8:
                    arg2 = load32(v3 + 8)
                store32(v7, v4)
                break
            store32(v3 + 8, (arg2 + 1))
            store32((v4 + (arg2 << 2)), 1)
            arg2 = load32(v3 + 8)
            if (u32(load32(v3 + 8)) < u32(v6)):
                continue
            break
    if (u32(arg2) > u32(v6)):
        store32(v3 + 8, v6)
    store32((load32((v5 + v9)) + (arg0 << 2)), arg1)

# ----------------------------------------------------------
# $Wc
# Export: Wc
# ----------------------------------------------------------
def Wc(arg0):
    """Export: Wc"""
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

# ----------------------------------------------------------
# $Ie
# Export: Ie
# ----------------------------------------------------------
def Ie(arg0, arg1, arg2, arg3):
    """Export: Ie"""
    while True:  # $label1
        while True:  # $label2
            while True:  # $label0
                # br_table arg3
                break
                break
            arg3 = load32(9143004)
            v4 = load32(PLAYER_COUNT)
            arg0 = (arg0 != 0)
            store8((load32(9143004) + ((load32(PLAYER_COUNT) * arg1) + arg2)), (arg0 != 0))
            store8((arg3 + ((arg2 * v4) + arg1)), arg0)
            return
            break
        store8((load32(9143012) + ((load32(PLAYER_COUNT) * arg1) + arg2)), (arg0 != 0))
        break

# ----------------------------------------------------------
# $Z
# Export: Z
# ----------------------------------------------------------
def Z(arg0, arg1):
    """Export: Z"""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg0 = players[arg0]
    arg1 = ((load32(arg0 + 283960) + arg1) & 3)
    store32(players[arg0] + 283960, ((load32(arg0 + 283960) + arg1) & 3))
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

# ----------------------------------------------------------
# $Y
# Export: Y
# ----------------------------------------------------------
def Y(arg0, arg1):
    """Export: Y"""
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v5 = load32(PLAYERS)
        v3 = players[arg0]
        v6 = load32(players[arg0] + 284608)
        if (not load32(players[arg0] + 284608) & (arg1 < 0)):
            break
        v3 = (v3 + 284608)
        v4 = ((arg1 + v6) % 17)
        store32((v3 + 284608), ((arg1 + v6) % 17))
        if not load8u(9147210):
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

# ----------------------------------------------------------
# $Md
# Export: Md
# ----------------------------------------------------------
def Md(arg0, arg1):
    """Export: Md"""
    while True:  # $label0
        if arg0:
            break
        if load8u(9147210):
            break
        arg1 = load32(PLAYERS)
        v3 = load32(CURRENT_PLAYER)
        arg0 = players[load32(CURRENT_PLAYER)]
        v2 = load32(players[load32(CURRENT_PLAYER)] + 283848)
        if (load32(players[load32(CURRENT_PLAYER)] + 283848) != 2147483647):
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
        arg1 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v5 = (arg1 - 1)
        v6 = ((arg1 - 1) & 1)
        v3 = (load32(v3 + 283908) * arg1)
        v2 = load32(PLAYERS)
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
        if not v6:
            break
        if not load8u((v4 + (arg0 + v3))):
            break
        store8((v2 + (arg0 * 286704)) + 286701, 1)
        break

# ----------------------------------------------------------
# $Bc
# Export: Bc
# ----------------------------------------------------------
def Bc(arg0, arg1, arg2, arg3, arg4):
    """Export: Bc"""
    v5 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    if not load8u(9142916):
        store32(v5 + 32, arg3)
        # TODO: f64.promote_f32
        storef64(v5 + 24, arg4)
        # TODO: f64.promote_f32
        storef64(v5 + 16, arg2)
        # TODO: f64.promote_f32
        storef64(v5 + 8, arg1)
        # TODO: f64.promote_f32
        storef64(v5, arg0)
        a_b()
    G.global0 = (v5 + 48)

# ----------------------------------------------------------
# $M
# Export: M
# ----------------------------------------------------------
def M(arg0):
    """Export: M"""
    v2 = func26(arg0)
    while True:  # $label0
        if not arg0:
            break
        v4 = (arg0 & 3)
        if (u32(arg0) >= u32(4)):
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
        if not v4:
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

# ----------------------------------------------------------
# $Xd
# Export: Xd
# ----------------------------------------------------------
def Xd():
    """Export: Xd"""
    while True:  # $label1
        v2 = ((v0 * 404) + ENTITY_TYPES)
        if (load32(((v0 * 404) + ENTITY_TYPES) + 264) == 1):
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
    v7 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
    store32(9685864, func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2))))
    while True:  # $label20
        v0 = 0
        v1 = 0
        v2 = ((v11 * 404) + ENTITY_TYPES)
        if (load32(((v11 * 404) + ENTITY_TYPES) + 264) == 1):
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
            while True:  # $label3
                v1 = load32(v2 + 236)
                if not load32(v2 + 236):
                    break
                v9 = (v1 & 3)
                v4 = load32(v2 + 232)
                v0 = 0
                while True:  # $label4
                    if (u32(v1) < u32(4)):
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
                if not v9:
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
            while True:  # $label7
                v1 = (load32(v2 + 220) * load32(v2 + 216))
                if not (load32(v2 + 220) * load32(v2 + 216)):
                    break
                v8 = (v1 & 3)
                v4 = load32(v2 + 372)
                v5 = 0
                while True:  # $label8
                    if (u32(v1) < u32(4)):
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
                if not v8:
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
            while True:  # $label11
                v1 = load32(v2 + 364)
                if not load32(v2 + 364):
                    break
                v9 = (v1 & 3)
                v4 = load32(v2 + 24)
                v0 = 0
                while True:  # $label12
                    if (u32(v1) < u32(4)):
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
                if not v9:
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
            while True:  # $label16
                v1 = load32(v2 + 244)
                if not load32(v2 + 244):
                    break
                v6 = (v1 & 3)
                v2 = load32(v2 + 240)
                v8 = 0
                while True:  # $label17
                    if (u32(v1) < u32(4)):
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
                if not v6:
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

# ----------------------------------------------------------
# $Yc
# Export: Yc
# ----------------------------------------------------------
def Yc(arg0):
    """Export: Yc"""
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    store8(59183, arg0)
    while True:  # $label1
        if not arg0:
            arg0 = load32(9142876)
            while True:  # $label0
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

# ----------------------------------------------------------
# $Ed
# Export: Ed
# ----------------------------------------------------------
def Ed(arg0, arg1):
    """Export: Ed"""
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v2 = load32(9568088)
    while True:  # $label0
        if arg1:
            arg0 = load32(v2 + 80)
            store32(v4 + 4, load32(v2 + 88))
            store32(v4, arg0)
            break
        store32(v2 + 88, 0)
        arg1 = load32(v2 + 84)
        if (u32(arg0) >= u32(load32(v2 + 84))):
            arg1 = (load32(v2 + 92) + (arg0 + arg1))
            store32(v2 + 84, (load32(v2 + 92) + (arg0 + arg1)))
            v3 = load32(v2 + 80)
            arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
            if v3:
            store32(v2 + 80, arg1)
        if not arg0:
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
        if not v7:
            break
        arg0 = load32(((arg1 << 2) + 9147392))
        arg1 = load32(v2 + 88)
        store32(v2 + 88, (load32(v2 + 88) + 1))
        store32((v3 + (arg1 << 2)), arg0)
        break
    G.global0 = (v4 + 16)

# ----------------------------------------------------------
# $B
# Export: B
# ----------------------------------------------------------
def B():
    """Export: B"""
    G.global8 = 9756528
    G.global7 = 9690992
    a_A(9688092)
    store32(9688092, 9688092)
    v0 = G.global8
    store32(9688144, G.global8)
    store32(9688124, 2)
    store32(9688148, (v0 - G.global7))
    store32(9688168, 9688168)
    store32(9688188, 9688068)
    store32(9688116, 42)
    store32(9688164, 9688336)
    store32(9688104, 9688092)
    store32(9688100, 9688092)
    func430(9688092)
    a_s(9688092)
    store32(57168, load32(39400))
    store32(57172, load32(39404))
    store32(57176, load32(39408))
    store32(57180, load32(39412))
    store32(57184, load32(39416))
    store32(57188, load32(39420))
    store32(57192, load32(39424))
    store32(57196, load32(39428))
    store32(57200, load32(39432))
    store32(57204, load32(39436))
    store32(57208, load32(39440))
    store32(57212, load32(39444))
    store32(57216, load32(39448))
    store32(57220, load32(39452))
    store32(57224, load32(39456))
    store32(57228, load32(39460))
    store32(57232, load32(39464))
    store32(57248, load32(39468))
    store32(57252, load32(39472))
    store32(57256, load32(39476))
    store32(57260, load32(39480))
    store32(57264, load32(39484))
    store32(57268, load32(39488))
    store32(57272, load32(39492))
    v0 = load32(39752)
    store32(57280, load32(39752))
    v1 = load32(39756)
    store32(57284, load32(39756))
    v3 = load32(39760)
    store32(57288, load32(39760))
    v2 = load32(39764)
    store32(57292, load32(39764))
    v4 = load32(39768)
    store32(57296, load32(39768))
    v5 = load32(39772)
    store32(57300, load32(39772))
    store32(57304, load32(39776))
    store32(57308, load32(39780))
    store32(57312, load32(39784))
    store32(57316, load32(39788))
    store32(57320, load32(40376))
    store32(57348, v5)
    store32(57344, v4)
    store32(57340, v2)
    store32(57336, v3)
    store32(57332, v1)
    store32(57328, v0)
    store32(57360, load32(39652))
    store32(57364, load32(39656))
    store32(57368, load32(39660))
    store32(57372, load32(39664))
    store32(57376, load32(39668))
    store32(57380, load32(39672))
    store32(57384, load32(39676))
    store32(57388, load32(39680))
    store32(57392, load32(39684))
    store32(57396, load32(39688))
    store32(57400, load32(39692))
    store32(57404, load32(39696))
    store32(57408, load32(39700))
    store32(57412, load32(39704))
    store32(57416, load32(39708))
    store32(57420, load32(39712))
    store32(57424, load32(39716))
    store32(57428, load32(39720))
    store32(57432, load32(39724))
    store32(57436, load32(39728))
    store32(57440, load32(39732))
    store32(57444, load32(39736))
    store32(57448, load32(39740))
    store32(57452, load32(39648))
    store32(57456, load32(39512))
    store32(57460, load32(39516))
    store32(57464, load32(39520))
    store32(57468, load32(39524))
    store32(57472, load32(39528))
    store32(57476, load32(39532))
    store32(57480, load32(39536))
    store32(57484, load32(39540))
    store32(57488, load32(39544))
    store32(57492, load32(39548))
    store32(57496, load32(39552))
    store32(57500, load32(39556))
    store32(57504, load32(39560))
    store32(57508, load32(39564))
    store32(57512, load32(39568))
    store32(57516, load32(39572))
    store32(57520, load32(39608))
    store32(57524, load32(39612))
    store32(57528, load32(39616))
    store32(57532, load32(39584))
    store32(57536, load32(39588))
    store32(57540, load32(39592))
    store32(57544, load32(39596))
    store32(57548, load32(39600))
    store32(57552, load32(39604))
    store32(57568, load32(39620))
    store32(57572, load32(39624))
    store32(57576, load32(39628))
    store32(57580, load32(39632))
    store32(57584, load32(39636))
    store32(57588, load32(39640))
    store32(57592, load32(39644))
    v0 = load32(39496)
    store32(57596, load32(39496))
    v1 = load32(39500)
    store32(57600, load32(39500))
    store32(57604, load32(39576))
    store32(57608, load32(39816))
    store32(57612, load32(39824))
    store32(57616, load32(39856))
    store32(57620, load32(39820))
    store32(57632, load32(40068))
    store32(57636, load32(40072))
    store32(57640, load32(40076))
    store32(57644, load32(40080))
    store32(57648, load32(40012))
    store32(57652, load32(40016))
    store32(57656, load32(40020))
    store32(57660, load32(40024))
    store32(57664, load32(40028))
    store32(57668, load32(40032))
    store32(57672, load32(40036))
    store32(57676, load32(40040))
    store32(57680, load32(40044))
    store32(57684, load32(40048))
    v3 = load32(39960)
    store32(57696, load32(39960))
    v2 = load32(39964)
    store32(57700, load32(39964))
    v4 = load32(39968)
    store32(57704, load32(39968))
    v5 = load32(39972)
    store32(57708, load32(39972))
    v6 = load32(39976)
    store32(57712, load32(39976))
    v7 = load32(39980)
    store32(57716, load32(39980))
    v8 = load32(39984)
    store32(57720, load32(39984))
    v9 = load32(39988)
    store32(57724, load32(39988))
    v10 = load32(39992)
    store32(57728, load32(39992))
    v11 = load32(39996)
    store32(57732, load32(39996))
    store32(57736, load32(39504))
    store32(57740, load32(39508))
    store32(57744, load32(39932))
    store32(57748, load32(39928))
    store32(57752, load32(39924))
    store32(57756, load32(39920))
    store32(57760, load32(39916))
    store32(57764, load32(39912))
    store32(57768, load32(39908))
    store32(57772, load32(39904))
    store32(57776, load32(39900))
    store32(57780, load32(39896))
    store32(57788, v1)
    store32(57784, v0)
    store32(57792, load32(40244))
    store32(57796, load32(40248))
    store32(57800, load32(40252))
    store32(57808, load32(40084))
    store32(57812, load32(40088))
    store32(57816, load32(40092))
    store32(57820, load32(40096))
    store32(57824, load32(40056))
    store32(57828, load32(40060))
    store32(57832, load32(40204))
    store32(57836, load32(40208))
    store32(57840, load32(39744))
    store32(57844, load32(39748))
    store32(57848, load32(40196))
    store32(57852, load32(40200))
    store32(57856, load32(40000))
    store32(57860, load32(40004))
    store32(57908, v11)
    store32(57904, v10)
    store32(57900, v9)
    store32(57896, v8)
    store32(57892, v7)
    store32(57888, v6)
    store32(57884, v5)
    store32(57880, v4)
    store32(57876, v2)
    store32(57872, v3)
    store32(57912, load32(40064))
    store32(57916, load32(40344))
    store32(57920, load32(40104))
    store32(57924, load32(40108))
    store32(57928, load32(40112))
    store32(57932, load32(40116))
    store32(57936, load32(40120))
    store32(57940, load32(39840))
    store32(57944, load32(39848))
    store32(57948, load32(39844))
    store32(57952, load32(39852))
    store32(57968, load32(39792))
    store32(57972, load32(39796))
    store32(57976, load32(39800))
    store32(57980, load32(39804))
    store32(57984, load32(39808))
    v0 = load32(39320)
    store32(58000, load32(39320))
    v1 = load32(39324)
    store32(58004, load32(39324))
    v3 = load32(39328)
    store32(58008, load32(39328))
    v2 = load32(39332)
    store32(58012, load32(39332))
    v4 = load32(39336)
    store32(58016, load32(39336))
    store32(58032, load32(39348))
    store32(58036, load32(39352))
    store32(58040, load32(39356))
    store32(58044, load32(39360))
    store32(58048, load32(39364))
    store32(58052, load32(39252))
    store32(58056, load32(39260))
    store32(58060, load32(39376))
    store32(58064, load32(39380))
    store32(58068, load32(39396))
    store32(58072, load32(39392))
    store32(58076, load32(39292))
    store32(58080, load32(39300))
    store32(58084, load32(39312))
    store32(58088, load32(39372))
    store32(58092, load32(40052))
    v5 = load32(39580)
    store32(58096, load32(39580))
    store32(58100, load32(40380))
    store32(58104, load32(39244))
    store32(58108, load32(39248))
    store32(58112, load32(39368))
    store32(58116, load32(39308))
    store32(58120, load32(39272))
    store32(58124, load32(39276))
    store32(58128, load32(39280))
    store32(58160, v4)
    store32(58156, v2)
    store32(58152, v3)
    store32(58148, v1)
    store32(58144, v0)
    store32(58164, load32(39340))
    store32(58168, load32(39344))
    store32(58172, load32(39288))
    store32(58176, load32(39256))
    store32(58180, load32(40352))
    store32(58184, load32(39388))
    store32(58188, load32(39304))
    store32(58192, load32(39296))
    v0 = load32(39384)
    store32(58196, load32(39384))
    store32(58200, load32(39812))
    store32(58204, load32(39284))
    store32(58208, load32(39264))
    store32(58212, v0)
    store32(58216, load32(39240))
    store32(58220, load32(40348))
    store32(58224, load32(39268))
    store32(58240, load32(40304))
    store32(58244, load32(40308))
    store32(58248, load32(40312))
    store32(58252, load32(40316))
    store32(58256, load32(40320))
    store32(58260, load32(40324))
    store32(58272, load32(40260))
    store32(58276, load32(40264))
    store32(58280, load32(40268))
    store32(58284, load32(40272))
    store32(58288, load32(40280))
    store32(58292, load32(40284))
    store32(58296, load32(40288))
    store32(58300, load32(40292))
    store32(58304, load32(40296))
    store32(58308, load32(40160))
    store32(58320, load32(40212))
    store32(58324, load32(40216))
    store32(58328, load32(40220))
    store32(58332, load32(40224))
    store32(58336, load32(40228))
    store32(58340, load32(40232))
    store32(58344, load32(40236))
    store32(58348, load32(40240))
    store32(58352, load32(40148))
    store32(58356, load32(40152))
    store32(58360, load32(40124))
    store32(58364, load32(40128))
    store32(58368, load32(40132))
    store32(58384, load32(40180))
    store32(58388, load32(40184))
    store32(58392, load32(40188))
    store32(58396, load32(40192))
    store32(58400, load32(39944))
    store32(58404, load32(39948))
    store32(58408, load32(39952))
    store32(58412, load32(39956))
    store32(58416, load32(40164))
    store32(58420, load32(40168))
    store32(58424, load32(40172))
    store32(58428, load32(40176))
    store32(58432, load32(40328))
    store32(58436, load32(40332))
    store32(58440, load32(40276))
    store32(58444, load32(40256))
    store32(58448, load32(40008))
    store32(58452, load32(40156))
    store32(58456, load32(40100))
    store32(58460, v5)
    store32(58464, load32(40356))
    store32(58468, load32(40360))
    store32(58472, load32(40364))
    store32(58476, load32(40368))
    store32(58480, load32(40372))
    store32(58484, load32(40300))
    store32(58488, load32(40336))
    store32(58492, load32(40340))
    store32(58496, load32(40140))
    store32(58500, load32(40136))
    store32(58504, load32(40144))
    store32(58508, load32(39316))
    store32(58512, load32(38936))
    store32(58516, load32(38724))
    v3 = load32(38652)
    store32(58520, load32(38652))
    v6 = load32(38656)
    store32(58524, load32(38656))
    v7 = load32(38660)
    store32(58528, load32(38660))
    v8 = load32(38580)
    store32(58532, load32(38580))
    store32(58536, load32(38932))
    v12 = load32(38940)
    store32(58540, load32(38940))
    v25 = load32(38728)
    store32(58544, load32(38728))
    v26 = load32(38440)
    store32(58548, load32(38440))
    v27 = load32(38772)
    store32(58552, load32(38772))
    v28 = load32(38928)
    store32(58556, load32(38928))
    v9 = load32(38436)
    store32(58560, load32(38436))
    v29 = load32(38444)
    store32(58564, load32(38444))
    v30 = load32(38740)
    store32(58568, load32(38740))
    v10 = load32(38756)
    store32(58572, load32(38756))
    v31 = load32(38684)
    store32(58576, load32(38684))
    v11 = load32(38692)
    store32(58580, load32(38692))
    v32 = load32(38572)
    store32(58584, load32(38572))
    v13 = load32(57152)
    store32(58592, load32(57152))
    v14 = load32(38432)
    store32(58596, load32(38432))
    v33 = load32(38496)
    store32(58600, load32(38496))
    v34 = load32(38452)
    store32(58604, load32(38452))
    v2 = load32(38460)
    store32(58608, load32(38460))
    v15 = load32(38424)
    store32(58612, load32(38424))
    v16 = load32(38760)
    store32(58616, load32(38760))
    v17 = load32(38752)
    store32(58620, load32(38752))
    v18 = load32(38736)
    store32(58624, load32(38736))
    v19 = load32(38776)
    store32(58628, load32(38776))
    v4 = load32(38732)
    store32(58632, load32(38732))
    v20 = load32(38748)
    store32(58636, load32(38748))
    v21 = load32(38744)
    store32(58640, load32(38744))
    v22 = load32(38680)
    store32(58644, load32(38680))
    v35 = load32(38704)
    store32(58648, load32(38704))
    v0 = load32(38924)
    store32(58652, load32(38924))
    v23 = load32(38688)
    store32(58656, load32(38688))
    v1 = load32(38672)
    store32(58660, load32(38672))
    v36 = load32(38696)
    store32(58664, load32(38696))
    v24 = load32(38676)
    store32(58668, load32(38676))
    v5 = load32(38428)
    store32(58696, v12)
    store32(58692, v25)
    store32(58688, v6)
    store32(58684, v3)
    store32(58680, v8)
    store32(58676, v7)
    store32(58672, v5)
    store32(58820, v28)
    store32(58816, v27)
    store32(58812, v26)
    store32(58808, v10)
    store32(58804, v30)
    store32(58800, v11)
    store32(58796, v31)
    store32(58792, v29)
    store32(58788, v9)
    store32(58784, v1)
    store32(58780, v24)
    store32(58776, v36)
    store32(58772, v22)
    store32(58768, v23)
    store32(58764, v0)
    store32(58760, v35)
    store32(58756, v5)
    store32(58752, v21)
    store32(58748, v20)
    store32(58744, v4)
    store32(58740, v2)
    store32(58736, v19)
    store32(58732, v18)
    store32(58728, v17)
    store32(58724, v16)
    store32(58720, v15)
    store32(58716, v34)
    store32(58712, v33)
    store32(58708, v14)
    store32(58704, v13)
    store32(58836, v7)
    store32(58840, v8)
    store32(58844, v3)
    store32(58848, v6)
    store32(58864, v32)
    v6 = load32(38456)
    store32(58824, load32(38456))
    v7 = load32(38764)
    store32(58828, load32(38764))
    v3 = load32(38920)
    store32(58832, load32(38920))
    store32(58852, v6)
    store32(58856, v7)
    store32(58860, v3)
    v8 = load32(38568)
    store32(58868, load32(38568))
    v12 = load32(38576)
    store32(58872, load32(38576))
    store32(58876, v8)
    store32(58880, v12)
    store32(58892, v3)
    store32(58888, v0)
    store32(58884, v1)
    store32(58904, v1)
    store32(58900, v4)
    store32(58896, v2)
    store32(58908, v0)
    store32(58912, v3)
    store32(58924, v11)
    store32(58920, v17)
    store32(58916, v10)
    store32(58928, load32(38584))
    store32(58932, load32(38796))
    store32(58936, load32(38872))
    store32(58940, load32(38708))
    store32(58944, load32(38720))
    store32(58948, load32(38716))
    store32(58976, v6)
    store32(58972, v15)
    store32(58968, v14)
    store32(58964, v9)
    store32(58960, v13)
    v6 = load32(38440)
    store32(58984, v2)
    store32(58980, v6)
    v2 = load32(38444)
    store32(58992, v18)
    store32(58988, v2)
    v2 = load32(38740)
    store32(59016, v7)
    store32(59012, v20)
    store32(59008, v4)
    store32(59004, v19)
    store32(59000, v16)
    store32(58996, v2)
    v2 = load32(38772)
    store32(59028, v22)
    store32(59024, v21)
    store32(59020, v2)
    v2 = load32(38684)
    store32(59044, v1)
    store32(59040, v24)
    store32(59036, v23)
    store32(59032, v2)
    v1 = load32(38928)
    store32(59060, v5)
    store32(59056, v0)
    store32(59052, v3)
    store32(59048, v1)
    store32(59064, load32(38660))
    store32(59068, load32(38580))
    store32(59072, load32(38652))
    store32(59076, load32(38656))
    store32(59080, load32(38940))
    store32(59088, load32(38472))
    store32(59092, load32(38600))
    store32(59096, load32(38640))
    store32(59100, load32(38548))
    store32(59104, load32(38596))
    store32(59108, load32(38644))
    store32(59112, load32(38604))
    store32(59116, load32(38608))
    store32(59120, load32(38612))
    store32(59124, load32(38616))
    store32(9681696, load32(38944))
    store32(9681700, load32(39020))
    store32(9681704, load32(39036))
    store32(9681708, load32(39016))
    store32(9681712, load32(39012))
    store32(9681716, load32(39040))
    store32(9681720, load32(38948))
    store32(9681724, load32(38988))
    store32(9681728, load32(38992))
    store32(9681732, load32(39008))
    store32(9681736, load32(39032))
    store32(9681740, load32(39028))
    store32(9681744, load32(39052))
    store32(9681748, load32(39044))
    store32(9681752, load32(39000))
    store32(9681756, load32(39048))
    store32(9681760, load32(39024))
    store32(9681764, load32(39004))
    store32(9681776, load32(38968))
    store32(9681780, load32(38972))
    store32(9681784, load32(38976))
    store32(9681788, load32(38980))
    store32(9681792, load32(38952))
    store32(9681796, load32(38960))
    store32(9681800, load32(38956))
    store32(9687164, load32(38492))
    store32(9687168, load32(38788))
    store32(9687172, load32(38864))
    store32(9687152, load32(38480))
    store32(9687156, load32(38784))
    store32(9687160, load32(38860))
    store32(9687176, load32(38512))
    store32(9687180, load32(38792))
    store32(9687184, load32(38868))
    store32(9671152, load32(38460))
    store8(9147209, 0)
    store8(9147208, 0)
    store32(9215888, 1024)
    v0 = func26(4096)
    store32(9215896, 1024)
    store32(9215884, v0)
    store32(9215892, 0)
    store32(9215948, 64)
    v0 = func26(256)
    store32(9215956, 1024)
    store32(9215944, v0)
    store32(9215952, 0)
    store32(9215964, 3)
    v0 = func26(12)
    store32(9215972, 10)
    store32(9215960, v0)
    store32(9215968, 0)
    store32(9215980, 1)
    v0 = func26(4)
    store32(9215988, 128)
    store32(9215976, v0)
    store32(9215984, 0)
    store32(9215996, 1)
    v0 = func26(4)
    store32(9216004, 128)
    store32(9215992, v0)
    store32(9216000, 0)
    store32(9216012, 1)
    v0 = func26(4)
    store32(9216020, 128)
    store32(9216008, v0)
    store32(9216016, 0)
    store32(9216028, 1)
    v0 = func26(4)
    store32(9216036, 128)
    store32(9216024, v0)
    store32(9216032, 0)
    store32(9216044, 1024)
    v0 = func26(4096)
    store32(9216052, 1024)
    store32(9216040, v0)
    store32(9216048, 0)
    store64(9216084, 1125281431552)
    store32(9216080, 1)
    store32(9216148, 0)
    store32(9216212, 1)
    store32(9216200, 408)
    store32(9216192, 0)
    store8(9216103, 0)
    store8(9216100, 1)
    store32(9216344, 1)
    v0 = load32(9216056)
    store32(9216092, load32(9216056))
    store32(9216280, 0)
    store64(9216216, 1073741824006)
    store32(9216412, 0)
    store64(9216348, 1017907249221)
    store32(9216332, 409)
    store32(9216324, 0)
    store8(9216235, 0)
    store8(9216232, 1)
    store32(9216224, (v0 + 1))
    store32(9216356, (v0 + 2))
    store32(9216544, 0)
    store32(9216488, (v0 + 3))
    store64(9216480, 1022202216513)
    store32(9216476, 1)
    store32(9216464, 632)
    store32(9216456, 0)
    store8(9216367, 0)
    store8(9216364, 1)
    store32(9216588, 0)
    store32(9216596, 418)
    store32(9216608, 2)
    store32(9216620, (v0 + 4))
    store32(9216676, 0)
    store64(9216612, 1030792151040)
    store8(9216499, 0)
    store8(9216496, 1)
    store32(9216720, 0)
    store32(9216728, 813)
    store32(9216740, 1)
    store32(9216752, (v0 + 5))
    store32(9216808, 0)
    store64(9216744, 171798691903)
    store8(9216631, 0)
    store8(9216628, 1)
    store32(9216940, 0)
    store32(9216884, (v0 + 6))
    store64(9216876, 687194767360)
    store32(9216872, 3)
    store32(9216860, 410)
    store32(9216852, 0)
    store8(9216763, 0)
    store8(9216760, 1)
    store8(9216895, 0)
    store8(9216892, 1)
    store64(9217008, 115964116992)
    store32(9217072, 0)
    store32(9217016, (v0 + 7))
    store32(9217004, 4)
    store32(9216992, 411)
    store32(9216984, 0)
    store8(9217027, 0)
    store8(9217024, 1)
    store64(9217140, 429496729600)
    store32(9217204, 0)
    store32(9217148, (v0 + 8))
    store32(9217136, 2)
    store32(9217124, 436)
    store32(9217116, 0)
    store32(9217336, 0)
    store32(9217280, (v0 + 9))
    store64(9217272, 90194313216)
    store32(9217268, 2)
    store32(9217256, 0)
    store32(9217248, 0)
    store8(9217159, 0)
    store8(9217156, 1)
    store32(9217468, 0)
    store32(9217412, (v0 + 10))
    store64(9217404, 515396075578)
    store32(9217400, 5)
    store32(9217388, 0)
    store32(9217380, 0)
    store8(9217291, 0)
    store8(9217288, 1)
    store32(9217600, 0)
    store32(9217544, (v0 + 11))
    store64(9217536, 502511173691)
    store32(9217532, 5)
    store32(9217520, 0)
    store32(9217512, 0)
    store8(9217423, 1)
    store8(9217420, 1)
    store32(9217732, 0)
    store32(9217676, (v0 + 12))
    store64(9217668, 373662154812)
    store32(9217664, 5)
    store32(9217652, 0)
    store32(9217644, 0)
    store8(9217555, 1)
    store8(9217552, 1)
    store32(9217864, 0)
    store32(9217808, (v0 + 13))
    store64(9217800, 953482739752)
    store32(9217796, 5)
    store32(9217784, 0)
    store32(9217776, 0)
    store8(9217687, 1)
    store8(9217684, 1)
    store32(9217996, 0)
    store32(9217940, (v0 + 14))
    store64(9217932, 781684047872)
    store32(9217928, 5)
    store32(9217916, 0)
    store32(9217908, 0)
    store8(9217819, 1)
    store8(9217816, 1)
    store32(9218128, 0)
    store32(9218072, (v0 + 15))
    store64(9218064, 794568949764)
    store32(9218060, 5)
    store32(9218048, 0)
    store32(9218040, 0)
    store8(9217951, 1)
    store8(9217948, 1)
    store32(9218260, 0)
    store32(9218204, (v0 + 16))
    store64(9218196, 798863917059)
    store32(9218192, 5)
    store32(9218180, 0)
    store32(9218172, 0)
    store8(9218083, 1)
    store8(9218080, 1)
    store32(9218392, 0)
    store32(9218336, (v0 + 17))
    store64(9218328, 785979015169)
    store32(9218324, 5)
    store32(9218312, 0)
    store32(9218304, 0)
    store8(9218215, 1)
    store8(9218212, 1)
    store32(9218524, 0)
    store32(9218468, (v0 + 18))
    store64(9218460, 790273982470)
    store32(9218456, 5)
    store32(9218444, 0)
    store32(9218436, 0)
    store8(9218347, 1)
    store8(9218344, 1)
    store32(9218656, 0)
    store32(9218600, (v0 + 19))
    store64(9218592, 773094113299)
    store32(9218588, 5)
    store32(9218576, 0)
    store32(9218568, 0)
    store8(9218479, 1)
    store8(9218476, 1)
    store32(9218788, 0)
    store32(9218732, (v0 + 20))
    store64(9218724, 0)
    store32(9218720, 2)
    store32(9218708, 0)
    store32(9218700, 0)
    store8(9218611, 1)
    store8(9218608, 1)
    store32(9218920, 0)
    store32(9218864, (v0 + 21))
    store64(9218856, 0)
    store32(9218852, 2)
    store32(9218840, 0)
    store32(9218832, 0)
    store8(9218743, 0)
    store8(9218740, 1)
    store32(9219052, 0)
    store32(9218996, (v0 + 22))
    store64(9218988, 210453397504)
    store32(9218984, 2)
    store32(9218972, 0)
    store32(9218964, 0)
    store8(9218875, 0)
    store8(9218872, 1)
    store32(9219184, 0)
    store32(9219128, (v0 + 23))
    store64(9219120, 223338299392)
    store32(9219116, 2)
    store32(9219104, 0)
    store32(9219096, 0)
    store8(9219007, 0)
    store8(9219004, 1)
    store32(9219316, 0)
    store32(9219260, (v0 + 24))
    store64(9219252, 498216206336)
    store32(9219248, 2)
    store32(9219236, 0)
    store32(9219228, 0)
    store8(9219139, 0)
    store8(9219136, 1)
    store32(9219448, 0)
    store32(9219392, (v0 + 25))
    store64(9219384, 223338299392)
    store32(9219380, 2)
    store32(9219368, 0)
    store32(9219360, 0)
    store8(9219271, 0)
    store8(9219268, 1)
    store32(9219580, 0)
    store32(9219524, (v0 + 26))
    store64(9219516, 571230650368)
    store32(9219512, 2)
    store32(9219500, 0)
    store32(9219492, 0)
    store8(9219403, 0)
    store8(9219400, 1)
    store32(9219712, 0)
    store32(9219656, (v0 + 27))
    store64(9219648, 528280977408)
    store32(9219644, 2)
    store32(9219632, 0)
    store32(9219624, 0)
    store8(9219535, 0)
    store8(9219532, 1)
    store32(9219844, 0)
    store32(9219788, (v0 + 28))
    store64(9219780, 1013612281856)
    store32(9219776, 2)
    store32(9219764, 0)
    store32(9219756, 0)
    store8(9219667, 0)
    store8(9219664, 1)
    store32(9219976, 0)
    store32(9219920, (v0 + 29))
    store64(9219912, 210453397504)
    store32(9219908, 2)
    store32(9219896, 0)
    store32(9219888, 0)
    store8(9219799, 0)
    store8(9219796, 1)
    store32(9220108, 0)
    store32(9220052, (v0 + 30))
    store64(9220044, 223338299392)
    store32(9220040, 2)
    store32(9220028, 0)
    store32(9220020, 0)
    store8(9219931, 0)
    store8(9219928, 1)
    store32(9220240, 0)
    store32(9220184, (v0 + 31))
    store64(9220176, 498216206336)
    store32(9220172, 2)
    store32(9220160, 0)
    store32(9220152, 0)
    store8(9220063, 0)
    store8(9220060, 1)
    store32(9220372, 0)
    store32(9220316, (v0 + 32))
    store64(9220308, 223338299392)
    store32(9220304, 2)
    store32(9220292, 0)
    store32(9220284, 0)
    store8(9220195, 0)
    store8(9220192, 1)
    store32(9220504, 0)
    store32(9220448, (v0 + 33))
    store64(9220440, 571230650368)
    store32(9220436, 2)
    store32(9220424, 0)
    store32(9220416, 0)
    store8(9220327, 0)
    store8(9220324, 1)
    store32(9220636, 0)
    store32(9220580, (v0 + 34))
    store64(9220572, 528280977408)
    store32(9220568, 2)
    store32(9220556, 0)
    store32(9220548, 0)
    store8(9220459, 0)
    store8(9220456, 1)
    store32(9220768, 0)
    store32(9220712, (v0 + 35))
    store64(9220704, 1013612281856)
    store32(9220700, 2)
    store32(9220688, 0)
    store32(9220680, 0)
    store8(9220591, 0)
    store8(9220588, 1)
    store32(9220900, 0)
    store32(9220844, (v0 + 36))
    store64(9220836, 781684047872)
    store32(9220832, 2)
    store32(9220820, 0)
    store32(9220812, 0)
    store8(9220723, 0)
    store8(9220720, 1)
    store32(9221032, 0)
    store32(9220976, (v0 + 37))
    store64(9220968, 794568949760)
    store32(9220964, 2)
    store32(9220952, 0)
    store32(9220944, 0)
    store8(9220855, 0)
    store8(9220852, 1)
    store32(9221164, 0)
    store32(9221108, (v0 + 38))
    store64(9221100, 798863917056)
    store32(9221096, 2)
    store32(9221084, 0)
    store32(9221076, 0)
    store8(9220987, 0)
    store8(9220984, 1)
    store32(9221296, 0)
    store32(9221240, (v0 + 39))
    store64(9221232, 785979015168)
    store32(9221228, 2)
    store32(9221216, 0)
    store32(9221208, 0)
    store8(9221119, 0)
    store8(9221116, 1)
    store32(9221428, 0)
    store32(9221372, (v0 + 40))
    store64(9221364, 790273982464)
    store32(9221360, 2)
    store32(9221348, 0)
    store32(9221340, 0)
    store8(9221251, 0)
    store8(9221248, 1)
    store32(9221560, 0)
    store32(9221504, (v0 + 41))
    store64(9221496, 773094113280)
    store32(9221492, 2)
    store32(9221480, 0)
    store32(9221472, 0)
    store8(9221383, 0)
    store8(9221380, 1)
    store32(9221692, 0)
    store32(9221636, (v0 + 42))
    store64(9221628, 781684047872)
    store32(9221624, 2)
    store32(9221612, 0)
    store32(9221604, 0)
    store8(9221515, 0)
    store8(9221512, 1)
    store32(9221824, 0)
    store32(9221768, (v0 + 43))
    store64(9221760, 794568949760)
    store32(9221756, 2)
    store32(9221744, 0)
    store32(9221736, 0)
    store8(9221647, 0)
    store8(9221644, 1)
    store32(9221956, 0)
    store32(9221900, (v0 + 44))
    store64(9221892, 798863917056)
    store32(9221888, 2)
    store32(9221876, 0)
    store32(9221868, 0)
    store8(9221779, 0)
    store8(9221776, 1)
    store32(9222088, 0)
    store32(9222032, (v0 + 45))
    store64(9222024, 785979015168)
    store32(9222020, 2)
    store32(9222008, 0)
    store32(9222000, 0)
    store8(9221911, 0)
    store8(9221908, 1)
    store32(9222220, 0)
    store32(9222164, (v0 + 46))
    store64(9222156, 790273982464)
    store32(9222152, 2)
    store32(9222140, 0)
    store32(9222132, 0)
    store8(9222043, 0)
    store8(9222040, 1)
    store32(9222352, 0)
    store32(9222296, (v0 + 47))
    store64(9222288, 773094113280)
    store32(9222284, 2)
    store32(9222272, 0)
    store32(9222264, 0)
    store8(9222175, 0)
    store8(9222172, 1)
    store32(9222484, 0)
    store32(9222428, (v0 + 48))
    store64(9222420, 227633266688)
    store32(9222416, 2)
    store32(9222404, 0)
    store32(9222396, 0)
    store8(9222307, 0)
    store8(9222304, 1)
    store32(9222616, 0)
    store32(9222560, (v0 + 49))
    store64(9222552, 523986010112)
    store32(9222548, 2)
    store32(9222536, 0)
    store32(9222528, 0)
    store8(9222439, 0)
    store8(9222436, 1)
    store32(9222748, 0)
    store32(9222692, (v0 + 50))
    store64(9222684, 519691042816)
    store32(9222680, 2)
    store32(9222668, 0)
    store32(9222660, 0)
    store8(9222571, 0)
    store8(9222568, 1)
    store32(9222880, 0)
    store32(9222824, (v0 + 51))
    store64(9222816, 231928233984)
    store32(9222812, 2)
    store32(9222800, 0)
    store32(9222792, 0)
    store8(9222703, 0)
    store8(9222700, 1)
    store32(9223012, 0)
    store32(9222956, (v0 + 52))
    store64(9222948, 223338299392)
    store32(9222944, 2)
    store32(9222932, 0)
    store32(9222924, 0)
    store8(9222835, 0)
    store8(9222832, 1)
    store32(9223144, 0)
    store32(9223088, (v0 + 53))
    store64(9223080, 339302416384)
    store32(9223076, 2)
    store32(9223064, 0)
    store32(9223056, 0)
    store8(9222967, 0)
    store8(9222964, 1)
    store32(9223276, 0)
    store32(9223220, (v0 + 54))
    store64(9223212, 227633266688)
    store32(9223208, 2)
    store32(9223196, 0)
    store32(9223188, 0)
    store8(9223099, 0)
    store8(9223096, 1)
    store32(9223408, 0)
    store32(9223352, (v0 + 55))
    store64(9223344, 523986010112)
    store32(9223340, 2)
    store32(9223328, 0)
    store32(9223320, 0)
    store8(9223231, 0)
    store8(9223228, 1)
    store32(9223540, 0)
    store32(9223484, (v0 + 56))
    store64(9223476, 519691042816)
    store32(9223472, 2)
    store32(9223460, 0)
    store32(9223452, 0)
    store8(9223363, 0)
    store8(9223360, 1)
    store32(9223672, 0)
    store32(9223616, (v0 + 57))
    store64(9223608, 231928233984)
    store32(9223604, 2)
    store32(9223592, 0)
    store32(9223584, 0)
    store8(9223495, 0)
    store8(9223492, 1)
    store32(9223804, 0)
    store32(9223748, (v0 + 58))
    store64(9223740, 223338299392)
    store32(9223736, 2)
    store32(9223724, 0)
    store32(9223716, 0)
    store8(9223627, 0)
    store8(9223624, 1)
    store32(9223936, 0)
    store32(9223880, (v0 + 59))
    store64(9223872, 339302416384)
    store32(9223868, 2)
    store32(9223856, 0)
    store32(9223848, 0)
    store8(9223759, 0)
    store8(9223756, 1)
    store32(9224068, 0)
    store32(9224012, (v0 + 60))
    store64(9224004, 803158884362)
    store32(9224000, 5)
    store32(9223988, 0)
    store32(9223980, 0)
    store8(9223891, 0)
    store8(9223888, 1)
    store32(9224200, 0)
    store32(9224144, (v0 + 61))
    store64(9224136, 352187318272)
    store32(9224132, 2)
    store32(9224120, 0)
    store32(9224112, 0)
    store8(9224023, 1)
    store8(9224020, 1)
    store32(9224332, 0)
    store32(9224276, (v0 + 62))
    store64(9224268, 377957122048)
    store32(9224264, 2)
    store32(9224252, 0)
    store32(9224244, 0)
    store8(9224155, 0)
    store8(9224152, 1)
    store32(9224464, 0)
    store32(9224408, (v0 + 63))
    store64(9224400, 695784701954)
    store32(9224396, 5)
    store32(9224384, 0)
    store32(9224376, 0)
    store8(9224287, 0)
    store8(9224284, 1)
    store32(9224596, 0)
    store32(9224540, (v0 - -64))
    store64(9224532, 1120986464256)
    store32(9224528, 6)
    store32(9224516, 0)
    store32(9224508, 0)
    store8(9224419, 1)
    store8(9224416, 1)
    store32(9224728, 0)
    store32(9224672, (v0 + 65))
    store64(9224664, 1000727380113)
    store32(9224660, 7)
    store32(9224648, 814)
    store32(9224640, 0)
    store8(9224551, 0)
    store8(9224548, 1)
    store32(9224860, 0)
    store32(9224804, (v0 + 66))
    store64(9224796, 970662609042)
    store32(9224792, 7)
    store32(9224780, 0)
    store32(9224772, 0)
    store8(9224683, 1)
    store8(9224680, 1)
    store32(9224992, 0)
    store32(9224936, (v0 + 67))
    store64(9224928, 554050781331)
    store32(9224924, 7)
    store32(9224912, 0)
    store32(9224904, 0)
    store8(9224815, 1)
    store8(9224812, 1)
    store32(9225124, 0)
    store32(9225068, (v0 + 68))
    store64(9225060, 236223201344)
    store32(9225056, 5)
    store32(9225044, 0)
    store32(9225036, 0)
    store8(9224947, 1)
    store8(9224944, 1)
    store32(9225256, 0)
    store32(9225200, (v0 + 69))
    store64(9225192, 566935683151)
    store32(9225188, 5)
    store32(9225176, 0)
    store32(9225168, 0)
    store8(9225079, 1)
    store8(9225076, 1)
    store32(9225388, 0)
    store32(9225332, (v0 + 70))
    store64(9225324, 219043332161)
    store32(9225320, 5)
    store32(9225308, 0)
    store32(9225300, 0)
    store8(9225211, 1)
    store8(9225208, 1)
    store32(9225520, 0)
    store32(9225464, (v0 + 71))
    store64(9225456, 339302416568)
    store32(9225452, 7)
    store32(9225440, 0)
    store32(9225432, 0)
    store8(9225343, 1)
    store8(9225340, 1)
    store32(9225652, 0)
    store32(9225596, (v0 + 72))
    store64(9225588, 545460846770)
    store32(9225584, 7)
    store32(9225572, 0)
    store32(9225564, 0)
    store8(9225475, 1)
    store8(9225472, 1)
    store32(9225784, 0)
    store32(9225728, (v0 + 73))
    store64(9225720, 343597383861)
    store32(9225716, 7)
    store32(9225704, 0)
    store32(9225696, 0)
    store8(9225607, 1)
    store8(9225604, 1)
    store32(9225916, 0)
    store32(9225860, (v0 + 74))
    store64(9225852, 274877907126)
    store32(9225848, 7)
    store32(9225836, 0)
    store32(9225828, 0)
    store8(9225739, 1)
    store8(9225736, 1)
    store32(9226048, 0)
    store32(9225992, (v0 + 75))
    store64(9225984, 309237645495)
    store32(9225980, 7)
    store32(9225968, 0)
    store32(9225960, 0)
    store8(9225871, 1)
    store8(9225868, 1)
    store32(9226180, 0)
    store32(9226124, (v0 + 76))
    store64(9226116, 532575944789)
    store32(9226112, 5)
    store32(9226100, 0)
    store32(9226092, 0)
    store8(9226003, 1)
    store8(9226000, 1)
    store32(9226312, 0)
    store32(9226256, (v0 + 77))
    store64(9226248, 304942678201)
    store32(9226244, 7)
    store32(9226232, 0)
    store32(9226224, 0)
    store8(9226135, 1)
    store8(9226132, 1)
    store32(9226444, 0)
    store32(9226388, (v0 + 78))
    store64(9226380, 979252543674)
    store32(9226376, 7)
    store32(9226364, 0)
    store32(9226356, 0)
    store8(9226267, 1)
    store8(9226264, 1)
    store32(9226576, 0)
    store32(9226520, (v0 + 79))
    store64(9226512, 313532612795)
    store32(9226508, 7)
    store32(9226496, 0)
    store32(9226488, 0)
    store8(9226399, 1)
    store8(9226396, 1)
    store32(9226708, 0)
    store32(9226652, (v0 + 80))
    store64(9226644, 292057776316)
    store32(9226640, 7)
    store32(9226628, 0)
    store32(9226620, 0)
    store8(9226531, 1)
    store8(9226528, 1)
    store32(9226840, 0)
    store32(9226784, (v0 + 81))
    store64(9226776, 240518168765)
    store32(9226772, 7)
    store32(9226760, 0)
    store32(9226752, 0)
    store8(9226663, 1)
    store8(9226660, 1)
    store32(9226972, 0)
    store32(9226916, (v0 + 82))
    store64(9226908, 296352743614)
    store32(9226904, 7)
    store32(9226892, 0)
    store32(9226884, 0)
    store8(9226795, 1)
    store8(9226792, 1)
    store32(9227104, 0)
    store32(9227048, (v0 + 83))
    store64(9227040, 249108103302)
    store32(9227036, 7)
    store32(9227024, 0)
    store32(9227016, 0)
    store8(9226927, 1)
    store8(9226924, 1)
    store32(9227236, 0)
    store32(9227180, (v0 + 84))
    store64(9227172, 244813136007)
    store32(9227168, 7)
    store32(9227156, 0)
    store32(9227148, 0)
    store8(9227059, 1)
    store8(9227056, 1)
    store32(9227368, 0)
    store32(9227312, (v0 + 85))
    store64(9227304, 949187772470)
    store32(9227300, 8)
    store32(9227288, 0)
    store32(9227280, 0)
    store8(9227191, 1)
    store8(9227188, 1)
    store32(9227500, 0)
    store32(9227444, (v0 + 86))
    store64(9227436, 1009317314724)
    store32(9227432, 7)
    store32(9227420, 0)
    store32(9227412, 0)
    store8(9227323, 1)
    store8(9227320, 1)
    store32(9227632, 0)
    store32(9227576, (v0 + 87))
    store64(9227568, 399431958693)
    store32(9227564, 7)
    store32(9227552, 0)
    store32(9227544, 0)
    store8(9227455, 1)
    store8(9227452, 1)
    store32(9227764, 0)
    store32(9227708, (v0 + 88))
    store64(9227700, 923417968803)
    store32(9227696, 7)
    store32(9227684, 0)
    store32(9227676, 0)
    store8(9227587, 1)
    store8(9227584, 1)
    store32(9227896, 0)
    store32(9227840, (v0 + 89))
    store64(9227832, 416611827878)
    store32(9227828, 7)
    store32(9227816, 0)
    store32(9227808, 0)
    store8(9227719, 1)
    store8(9227716, 1)
    store32(9228028, 0)
    store32(9227972, (v0 + 90))
    store64(9227964, 940597837991)
    store32(9227960, 7)
    store32(9227948, 0)
    store32(9227940, 0)
    store8(9227851, 1)
    store8(9227848, 1)
    store32(9228160, 0)
    store32(9228104, (v0 + 91))
    store64(9228096, 940597837837)
    store32(9228092, 1)
    store32(9228080, 0)
    store32(9228072, 0)
    store8(9227983, 1)
    store8(9227980, 1)
    store32(9228292, 0)
    store32(9228236, (v0 + 92))
    store64(9228228, 98784247854)
    store32(9228224, 1)
    store32(9228212, 376)
    store32(9228204, 0)
    store8(9228115, 0)
    store8(9228112, 1)
    store32(9228424, 0)
    store32(9228368, (v0 + 93))
    store64(9228360, 682899800233)
    store32(9228356, 7)
    store32(9228344, 373)
    store32(9228336, 0)
    store8(9228247, 0)
    store8(9228244, 1)
    store32(9228556, 0)
    store32(9228500, (v0 + 94))
    store64(9228492, 682899800073)
    store32(9228488, 1)
    store32(9228476, 0)
    store32(9228468, 0)
    store8(9228379, 1)
    store8(9228376, 1)
    store32(9228688, 0)
    store32(9228632, (v0 + 95))
    store64(9228624, 944892805288)
    store32(9228620, 7)
    store32(9228608, 377)
    store32(9228600, 0)
    store8(9228511, 0)
    store8(9228508, 1)
    store32(9228820, 0)
    store32(9228764, (v0 + 96))
    store64(9228756, 670014898181)
    store32(9228752, 5)
    store32(9228740, 0)
    store32(9228732, 0)
    store8(9228643, 1)
    store8(9228640, 1)
    store32(9228952, 0)
    store32(9228896, (v0 + 97))
    store64(9228888, 721554505899)
    store32(9228884, 7)
    store32(9228872, 0)
    store32(9228864, 0)
    store8(9228775, 1)
    store8(9228772, 1)
    store32(9229084, 0)
    store32(9229028, (v0 + 98))
    store64(9229020, 511101108398)
    store32(9229016, 7)
    store32(9229004, 0)
    store32(9228996, 0)
    store8(9228907, 1)
    store8(9228904, 1)
    store32(9229216, 0)
    store32(9229160, (v0 + 99))
    store64(9229152, 932007903402)
    store32(9229148, 7)
    store32(9229136, 0)
    store32(9229128, 0)
    store8(9229039, 1)
    store8(9229036, 1)
    store32(9229348, 0)
    store32(9229292, (v0 + 100))
    store64(9229284, 614180323501)
    store32(9229280, 7)
    store32(9229268, 0)
    store32(9229260, 0)
    store8(9229171, 1)
    store8(9229168, 1)
    store32(9229480, 0)
    store32(9229424, (v0 + 101))
    store64(9229416, 558345748652)
    store32(9229412, 7)
    store32(9229400, 0)
    store32(9229392, 0)
    store8(9229303, 1)
    store8(9229300, 1)
    store32(9229612, 0)
    store32(9229556, (v0 + 102))
    store64(9229548, 584115552411)
    store32(9229544, 7)
    store32(9229532, 0)
    store32(9229524, 0)
    store8(9229435, 1)
    store8(9229432, 1)
    store32(9229744, 0)
    store32(9229688, (v0 + 103))
    store64(9229680, 463856468124)
    store32(9229676, 7)
    store32(9229664, 0)
    store32(9229656, 0)
    store8(9229567, 1)
    store8(9229564, 1)
    store32(9229876, 0)
    store32(9229820, (v0 + 104))
    store64(9229812, 1103806595229)
    store32(9229808, 7)
    store32(9229796, 0)
    store32(9229788, 0)
    store8(9229699, 1)
    store8(9229696, 1)
    store32(9230008, 0)
    store32(9229952, (v0 + 105))
    store64(9229944, 408021893278)
    store32(9229940, 7)
    store32(9229928, 0)
    store32(9229920, 0)
    store8(9229831, 1)
    store8(9229828, 1)
    store32(9230140, 0)
    store32(9230084, (v0 + 106))
    store64(9230076, 412316860575)
    store32(9230072, 7)
    store32(9230060, 0)
    store32(9230052, 0)
    store8(9229963, 1)
    store8(9229960, 1)
    store32(9230272, 0)
    store32(9230216, (v0 + 107))
    store64(9230208, 476741370016)
    store32(9230204, 7)
    store32(9230192, 0)
    store32(9230184, 0)
    store8(9230095, 1)
    store8(9230092, 1)
    store32(9230404, 0)
    store32(9230348, (v0 + 108))
    store64(9230340, 1108101562529)
    store32(9230336, 7)
    store32(9230324, 0)
    store32(9230316, 0)
    store8(9230227, 1)
    store8(9230224, 1)
    store32(9230536, 0)
    store32(9230480, (v0 + 109))
    store64(9230472, 433791697058)
    store32(9230468, 7)
    store32(9230456, 0)
    store32(9230448, 0)
    store8(9230359, 1)
    store8(9230356, 1)
    store32(9230668, 0)
    store32(9230612, (v0 + 110))
    store64(9230604, 665719930889)
    store32(9230600, 5)
    store32(9230588, 0)
    store32(9230580, 0)
    store8(9230491, 1)
    store8(9230488, 1)
    store32(9230800, 0)
    store32(9230744, (v0 + 111))
    store64(9230736, 700079669275)
    store32(9230732, 5)
    store32(9230720, 0)
    store32(9230712, 0)
    store8(9230623, 1)
    store8(9230620, 1)
    store32(9230932, 0)
    store32(9230876, (v0 + 112))
    store64(9230868, 974957576333)
    store32(9230864, 7)
    store32(9230852, 0)
    store32(9230844, 0)
    store8(9230755, 1)
    store8(9230752, 1)
    store32(9231064, 0)
    store32(9231008, (v0 + 113))
    store64(9231000, 674309865612)
    store32(9230996, 7)
    store32(9230984, 0)
    store32(9230976, 0)
    store8(9230887, 1)
    store8(9230884, 1)
    store32(9231196, 0)
    store32(9231140, (v0 + 114))
    store64(9231132, 382252089493)
    store32(9231128, 7)
    store32(9231116, 0)
    store32(9231108, 0)
    store8(9231019, 1)
    store8(9231016, 1)
    store32(9231328, 0)
    store32(9231272, (v0 + 115))
    store64(9231264, 438086664342)
    store32(9231260, 7)
    store32(9231248, 0)
    store32(9231240, 0)
    store8(9231151, 1)
    store8(9231148, 1)
    store32(9231460, 0)
    store32(9231404, (v0 + 116))
    store64(9231396, 472446402711)
    store32(9231392, 7)
    store32(9231380, 0)
    store32(9231372, 0)
    store8(9231283, 1)
    store8(9231280, 1)
    store32(9231592, 0)
    store32(9231536, (v0 + 117))
    store64(9231528, 450971566232)
    store32(9231524, 7)
    store32(9231512, 0)
    store32(9231504, 0)
    store8(9231415, 1)
    store8(9231412, 1)
    store32(9231724, 0)
    store32(9231668, (v0 + 118))
    store64(9231660, 266287972505)
    store32(9231656, 7)
    store32(9231644, 0)
    store32(9231636, 0)
    store8(9231547, 1)
    store8(9231544, 1)
    store32(9231856, 0)
    store32(9231800, (v0 + 119))
    store64(9231792, 468151435418)
    store32(9231788, 7)
    store32(9231776, 0)
    store32(9231768, 0)
    store8(9231679, 1)
    store8(9231676, 1)
    store32(9231988, 0)
    store32(9231932, (v0 + 120))
    store64(9231924, 549755813950)
    store32(9231920, 1)
    store32(9231908, 0)
    store32(9231900, 0)
    store8(9231811, 1)
    store8(9231808, 1)
    store32(9232120, 0)
    store32(9232064, (v0 + 121))
    store64(9232056, 725849473085)
    store32(9232052, 5)
    store32(9232040, 437)
    store32(9232032, 0)
    store8(9231943, 0)
    store8(9231940, 1)
    store32(9232252, 0)
    store32(9232196, (v0 + 122))
    store64(9232188, 575525617754)
    store32(9232184, 5)
    store32(9232172, 0)
    store32(9232164, 0)
    store8(9232075, 1)
    store8(9232072, 1)
    store32(9232384, 0)
    store32(9232328, (v0 + 123))
    store64(9232320, 210453397584)
    store32(9232316, 5)
    store32(9232304, 0)
    store32(9232296, 0)
    store8(9232207, 1)
    store8(9232204, 1)
    store32(9232516, 0)
    store32(9232460, (v0 + 124))
    store64(9232452, 184683593809)
    store32(9232448, 5)
    store32(9232436, 0)
    store32(9232428, 0)
    store8(9232339, 1)
    store8(9232336, 1)
    store32(9232648, 0)
    store32(9232592, (v0 + 125))
    store64(9232584, 498216206419)
    store32(9232580, 5)
    store32(9232568, 0)
    store32(9232560, 0)
    store8(9232471, 1)
    store8(9232468, 1)
    store32(9232780, 0)
    store32(9232724, (v0 + 126))
    store64(9232716, 180388626514)
    store32(9232712, 5)
    store32(9232700, 0)
    store32(9232692, 0)
    store8(9232603, 1)
    store8(9232600, 1)
    store32(9232912, 0)
    store32(9232856, (v0 + 127))
    store64(9232848, 571230650452)
    store32(9232844, 5)
    store32(9232832, 0)
    store32(9232824, 0)
    store8(9232735, 1)
    store8(9232732, 1)
    store32(9233044, 0)
    store32(9232988, (v0 + 128))
    store64(9232980, 528280977499)
    store32(9232976, 5)
    store32(9232964, 0)
    store32(9232956, 0)
    store8(9232867, 1)
    store8(9232864, 1)
    store32(9233176, 0)
    store32(9233120, (v0 + 129))
    store64(9233112, 1013612281942)
    store32(9233108, 5)
    store32(9233096, 0)
    store32(9233088, 0)
    store8(9232999, 1)
    store8(9232996, 1)
    store32(9233308, 0)
    store32(9233252, (v0 + 130))
    store64(9233244, 691489734656)
    store32(9233240, 9)
    store32(9233228, 0)
    store32(9233220, 0)
    store8(9233131, 1)
    store8(9233128, 1)
    store32(9233440, 0)
    store32(9233384, (v0 + 131))
    store64(9233376, 635655159846)
    store32(9233372, 1)
    store32(9233360, 816)
    store32(9233352, 0)
    store8(9233263, 0)
    store8(9233260, 1)
    store32(9233572, 0)
    store32(9233516, (v0 + 132))
    store64(9233508, 408021893120)
    store32(9233504, 10)
    store32(9233492, 812)
    store32(9233484, 0)
    store8(9233395, 0)
    store8(9233392, 1)
    store32(9233704, 0)
    store32(9233648, (v0 + 133))
    store64(9233640, 412316860416)
    store32(9233636, 11)
    store32(9233624, 434)
    store32(9233616, 0)
    store8(9233527, 0)
    store8(9233524, 1)
    store32(9233836, 0)
    store32(9233780, (v0 + 134))
    store64(9233772, 734439407791)
    store32(9233768, 7)
    store32(9233756, 435)
    store32(9233748, 0)
    store8(9233659, 0)
    store8(9233656, 1)
    store32(9233968, 0)
    store32(9233912, (v0 + 135))
    store64(9233904, 760209211568)
    store32(9233900, 7)
    store32(9233888, 0)
    store32(9233880, 0)
    store8(9233791, 1)
    store8(9233788, 1)
    store32(9234100, 0)
    store32(9234044, (v0 + 136))
    store64(9234036, 764504178865)
    store32(9234032, 7)
    store32(9234020, 0)
    store32(9234012, 0)
    store8(9233923, 1)
    store8(9233920, 1)
    store32(9234232, 0)
    store32(9234176, (v0 + 137))
    store64(9234168, 652835029029)
    store32(9234164, 5)
    store32(9234152, 0)
    store32(9234144, 0)
    store8(9234055, 1)
    store8(9234052, 1)
    store32(9234364, 0)
    store32(9234308, (v0 + 138))
    store64(9234300, 657129996327)
    store32(9234296, 5)
    store32(9234284, 0)
    store32(9234276, 0)
    store8(9234187, 1)
    store8(9234184, 1)
    store32(9234496, 0)
    store32(9234440, (v0 + 139))
    store64(9234432, 661424963622)
    store32(9234428, 5)
    store32(9234416, 0)
    store32(9234408, 0)
    store8(9234319, 1)
    store8(9234316, 1)
    store32(9234628, 0)
    store32(9234572, (v0 + 140))
    store64(9234564, 395136991412)
    store32(9234560, 7)
    store32(9234548, 0)
    store32(9234540, 0)
    store8(9234451, 1)
    store8(9234448, 1)
    store32(9234760, 0)
    store32(9234704, (v0 + 141))
    store64(9234696, 764504178867)
    store32(9234692, 7)
    store32(9234680, 0)
    store32(9234672, 0)
    store8(9234583, 1)
    store8(9234580, 1)
    store32(9234892, 0)
    store32(9234836, (v0 + 142))
    store64(9234828, 562640715919)
    store32(9234824, 7)
    store32(9234812, 0)
    store32(9234804, 0)
    store8(9234715, 1)
    store8(9234712, 1)
    store32(9235024, 0)
    store32(9234968, (v0 + 143))
    store64(9234960, 1142461300873)
    store32(9234956, 7)
    store32(9234944, 0)
    store32(9234936, 0)
    store8(9234847, 1)
    store8(9234844, 1)
    store32(9235156, 0)
    store32(9235100, (v0 + 144))
    store64(9235092, 485331304587)
    store32(9235088, 7)
    store32(9235076, 0)
    store32(9235068, 0)
    store8(9234979, 1)
    store8(9234976, 1)
    store32(9235288, 0)
    store32(9235232, (v0 + 145))
    store64(9235224, 1078036791434)
    store32(9235220, 7)
    store32(9235208, 0)
    store32(9235200, 0)
    store8(9235111, 1)
    store8(9235108, 1)
    store32(9235420, 0)
    store32(9235364, (v0 + 146))
    store64(9235356, 1082331758734)
    store32(9235352, 7)
    store32(9235340, 0)
    store32(9235332, 0)
    store8(9235243, 1)
    store8(9235240, 1)
    store32(9235552, 0)
    store32(9235496, (v0 + 147))
    store64(9235488, 1112396529797)
    store32(9235484, 7)
    store32(9235472, 0)
    store32(9235464, 0)
    store8(9235375, 1)
    store8(9235372, 1)
    store32(9235684, 0)
    store32(9235628, (v0 + 148))
    store64(9235620, 459561500808)
    store32(9235616, 7)
    store32(9235604, 0)
    store32(9235596, 0)
    store8(9235507, 1)
    store8(9235504, 1)
    store32(9235816, 0)
    store32(9235760, (v0 + 149))
    store64(9235752, 481036337296)
    store32(9235748, 7)
    store32(9235736, 0)
    store32(9235728, 0)
    store8(9235639, 1)
    store8(9235636, 1)
    store32(9235948, 0)
    store32(9235892, (v0 + 150))
    store64(9235884, 206158430282)
    store32(9235880, 5)
    store32(9235868, 0)
    store32(9235860, 0)
    store8(9235771, 1)
    store8(9235768, 1)
    store32(9236080, 0)
    store32(9236024, (v0 + 151))
    store64(9236016, 712964571212)
    store32(9236012, 5)
    store32(9236000, 0)
    store32(9235992, 0)
    store8(9235903, 1)
    store8(9235900, 1)
    store32(9236212, 0)
    store32(9236156, (v0 + 152))
    store64(9236148, 1151051235328)
    store32(9236144, 2)
    store32(9236132, 0)
    store32(9236124, 0)
    store8(9236035, 1)
    store8(9236032, 1)
    store32(9236344, 0)
    store32(9236288, (v0 + 153))
    store64(9236280, 176093659136)
    store32(9236276, 2)
    store32(9236264, 0)
    store32(9236256, 0)
    store8(9236167, 0)
    store8(9236164, 1)
    store32(9236476, 0)
    store32(9236420, (v0 + 154))
    store64(9236412, 708669603915)
    store32(9236408, 5)
    store32(9236396, 0)
    store32(9236388, 0)
    store8(9236299, 0)
    store8(9236296, 1)
    store32(9236608, 0)
    store32(9236552, (v0 + 155))
    store64(9236544, 704374636617)
    store32(9236540, 5)
    store32(9236528, 0)
    store32(9236520, 0)
    store8(9236431, 1)
    store8(9236428, 1)
    store32(9236740, 0)
    store32(9236684, (v0 + 156))
    store64(9236676, 420906795258)
    store32(9236672, 7)
    store32(9236660, 0)
    store32(9236652, 0)
    store8(9236563, 1)
    store8(9236560, 1)
    store32(9236872, 0)
    store32(9236816, (v0 + 157))
    store64(9236808, 322122547391)
    store32(9236804, 7)
    store32(9236792, 0)
    store32(9236784, 0)
    store8(9236695, 1)
    store8(9236692, 1)
    store32(9237004, 0)
    store32(9236948, (v0 + 158))
    store64(9236940, 326417514688)
    store32(9236936, 7)
    store32(9236924, 0)
    store32(9236916, 0)
    store8(9236827, 1)
    store8(9236824, 1)
    store32(9237136, 0)
    store32(9237080, (v0 + 159))
    store64(9237072, 335007449281)
    store32(9237068, 7)
    store32(9237056, 0)
    store32(9237048, 0)
    store8(9236959, 1)
    store8(9236956, 1)
    store32(9237268, 0)
    store32(9237212, (v0 + 160))
    store64(9237204, 493921239234)
    store32(9237200, 7)
    store32(9237188, 0)
    store32(9237180, 0)
    store8(9237091, 1)
    store8(9237088, 1)
    store32(9237400, 0)
    store32(9237344, (v0 + 161))
    store64(9237336, 330712481987)
    store32(9237332, 7)
    store32(9237320, 0)
    store32(9237312, 0)
    store8(9237223, 1)
    store8(9237220, 1)
    store32(9237532, 0)
    store32(9237476, (v0 + 162))
    store64(9237468, 107374182596)
    store32(9237464, 7)
    store32(9237452, 0)
    store32(9237444, 0)
    store8(9237355, 1)
    store8(9237352, 1)
    store32(9237664, 0)
    store32(9237608, (v0 + 163))
    store64(9237600, 987842478277)
    store32(9237596, 7)
    store32(9237584, 0)
    store32(9237576, 0)
    store8(9237487, 1)
    store8(9237484, 1)
    store32(9237796, 0)
    store32(9237740, (v0 + 164))
    store64(9237732, 317827580102)
    store32(9237728, 7)
    store32(9237716, 0)
    store32(9237708, 0)
    store8(9237619, 1)
    store8(9237616, 1)
    store32(9237928, 0)
    store32(9237872, (v0 + 165))
    store64(9237864, 966367641799)
    store32(9237860, 7)
    store32(9237848, 0)
    store32(9237840, 0)
    store8(9237751, 1)
    store8(9237748, 1)
    store32(9238060, 0)
    store32(9238004, (v0 + 166))
    store64(9237996, 287762809032)
    store32(9237992, 7)
    store32(9237980, 0)
    store32(9237972, 0)
    store8(9237883, 1)
    store8(9237880, 1)
    store32(9238192, 0)
    store32(9238136, (v0 + 167))
    store64(9238128, 910533066953)
    store32(9238124, 7)
    store32(9238112, 0)
    store32(9238104, 0)
    store8(9238015, 1)
    store8(9238012, 1)
    store32(9238324, 0)
    store32(9238268, (v0 + 168))
    store64(9238260, 201863463114)
    store32(9238256, 7)
    store32(9238244, 0)
    store32(9238236, 0)
    store8(9238147, 1)
    store8(9238144, 1)
    store32(9238456, 0)
    store32(9238400, (v0 + 169))
    store64(9238392, 257698037963)
    store32(9238388, 7)
    store32(9238376, 0)
    store32(9238368, 0)
    store8(9238279, 1)
    store8(9238276, 1)
    store32(9238588, 0)
    store32(9238532, (v0 + 170))
    store64(9238524, 489626271948)
    store32(9238520, 7)
    store32(9238508, 0)
    store32(9238500, 0)
    store8(9238411, 1)
    store8(9238408, 1)
    store32(9238720, 0)
    store32(9238664, (v0 + 171))
    store64(9238656, 403726926029)
    store32(9238652, 7)
    store32(9238640, 0)
    store32(9238632, 0)
    store8(9238543, 1)
    store8(9238540, 1)
    store32(9238852, 0)
    store32(9238796, (v0 + 172))
    store64(9238788, 283467841742)
    store32(9238784, 7)
    store32(9238772, 0)
    store32(9238764, 0)
    store8(9238675, 1)
    store8(9238672, 1)
    store32(9238984, 0)
    store32(9238928, (v0 + 173))
    store64(9238920, 231928234050)
    store32(9238916, 5)
    store32(9238904, 0)
    store32(9238896, 0)
    store8(9238807, 1)
    store8(9238804, 1)
    store32(9239116, 0)
    store32(9239060, (v0 + 174))
    store64(9239052, 227633266755)
    store32(9239048, 5)
    store32(9239036, 0)
    store32(9239028, 0)
    store8(9238939, 1)
    store8(9238936, 1)
    store32(9239248, 0)
    store32(9239192, (v0 + 175))
    store64(9239184, 523986010180)
    store32(9239180, 5)
    store32(9239168, 0)
    store32(9239160, 0)
    store8(9239071, 1)
    store8(9239068, 1)
    store32(9239380, 0)
    store32(9239324, (v0 + 176))
    store64(9239316, 223338299461)
    store32(9239312, 5)
    store32(9239300, 0)
    store32(9239292, 0)
    store8(9239203, 1)
    store8(9239200, 1)
    store32(9239512, 0)
    store32(9239456, (v0 + 177))
    store64(9239448, 193273528448)
    store32(9239444, 5)
    store32(9239432, 0)
    store32(9239424, 0)
    store8(9239335, 1)
    store8(9239332, 1)
    store32(9239644, 0)
    store32(9239588, (v0 + 178))
    store64(9239580, 214748364929)
    store32(9239576, 5)
    store32(9239564, 0)
    store32(9239556, 0)
    store8(9239467, 1)
    store8(9239464, 1)
    store32(9239776, 0)
    store32(9239720, (v0 + 179))
    store64(9239712, 188978561151)
    store32(9239708, 5)
    store32(9239696, 0)
    store32(9239688, 0)
    store8(9239599, 1)
    store8(9239596, 1)
    store32(9239908, 0)
    store32(9239852, (v0 + 180))
    store64(9239844, 536870912087)
    store32(9239840, 5)
    store32(9239828, 0)
    store32(9239820, 0)
    store8(9239731, 1)
    store8(9239728, 1)
    store32(9240040, 0)
    store32(9239984, (v0 + 181))
    store64(9239976, 133143986176)
    store32(9239972, 2)
    store32(9239960, 0)
    store32(9239952, 0)
    store8(9239863, 1)
    store8(9239860, 1)
    store32(9240172, 0)
    store32(9240116, (v0 + 182))
    store64(9240108, 128849018880)
    store32(9240104, 2)
    store32(9240092, 0)
    store32(9240084, 0)
    store8(9239995, 0)
    store8(9239992, 1)
    store32(9240304, 0)
    store32(9240248, (v0 + 183))
    store64(9240240, 519691042886)
    store32(9240236, 5)
    store32(9240224, 0)
    store32(9240216, 0)
    store8(9240127, 0)
    store8(9240124, 1)
    store32(9240436, 0)
    store32(9240380, (v0 + 184))
    store64(9240372, 339302416456)
    store32(9240368, 5)
    store32(9240356, 0)
    store32(9240348, 0)
    store8(9240259, 1)
    store8(9240256, 1)
    store32(9240568, 0)
    store32(9240512, (v0 + 185))
    store64(9240504, 687194767360)
    store32(9240500, 2)
    store32(9240488, 0)
    store32(9240480, 0)
    store8(9240391, 1)
    store8(9240388, 1)
    store32(9240700, 0)
    store32(9240644, (v0 + 186))
    store64(9240636, 622770257920)
    store32(9240632, 2)
    store32(9240620, 0)
    store32(9240612, 0)
    store8(9240523, 0)
    store8(9240520, 1)
    store32(9240832, 0)
    store32(9240776, (v0 + 187))
    store64(9240768, 1069446856758)
    store32(9240764, 1)
    store32(9240752, 0)
    store32(9240744, 0)
    store8(9240655, 0)
    store8(9240652, 1)
    store32(9240964, 0)
    store32(9240908, (v0 + 188))
    store64(9240900, 1116691496960)
    store32(9240896, 2)
    store32(9240884, 730)
    store32(9240876, 0)
    store8(9240787, 0)
    store8(9240784, 1)
    store32(9241096, 0)
    store32(9241040, (v0 + 189))
    store64(9241032, 880468295694)
    store32(9241028, 12)
    store32(9241016, 0)
    store32(9241008, 0)
    store8(9240919, 0)
    store8(9240916, 1)
    store32(9241228, 0)
    store32(9241172, (v0 + 190))
    store64(9241164, 880468295751)
    store32(9241160, 12)
    store32(9241148, 0)
    store32(9241140, 0)
    store8(9241051, 1)
    store8(9241048, 1)
    store32(9241360, 0)
    store32(9241304, (v0 + 191))
    store64(9241296, 880468295782)
    store32(9241292, 12)
    store32(9241280, 0)
    store32(9241272, 0)
    store8(9241183, 1)
    store8(9241180, 1)
    store32(9241492, 0)
    store32(9241436, (v0 + 192))
    store64(9241428, 730144440352)
    store32(9241424, 12)
    store32(9241412, 0)
    store32(9241404, 0)
    store8(9241315, 1)
    store8(9241312, 1)
    store32(9241624, 0)
    store32(9241568, (v0 + 193))
    store64(9241560, 858993459218)
    store32(9241556, 12)
    store32(9241544, 0)
    store32(9241536, 0)
    store8(9241447, 1)
    store8(9241444, 1)
    store32(9241756, 0)
    store32(9241700, (v0 + 194))
    store64(9241692, 854698491919)
    store32(9241688, 12)
    store32(9241676, 0)
    store32(9241668, 0)
    store8(9241579, 1)
    store8(9241576, 1)
    store32(9241888, 0)
    store32(9241832, (v0 + 195))
    store64(9241824, 854698491997)
    store32(9241820, 12)
    store32(9241808, 0)
    store32(9241800, 0)
    store8(9241711, 1)
    store8(9241708, 1)
    store32(9242020, 0)
    store32(9241964, (v0 + 196))
    store64(9241956, 1138166333460)
    store32(9241952, 12)
    store32(9241940, 0)
    store32(9241932, 0)
    store8(9241843, 1)
    store8(9241840, 1)
    store32(9242152, 0)
    store32(9242096, (v0 + 197))
    store64(9242088, 884763262988)
    store32(9242084, 12)
    store32(9242072, 0)
    store32(9242064, 0)
    store8(9241975, 1)
    store8(9241972, 1)
    store32(9242284, 0)
    store32(9242228, (v0 + 198))
    store64(9242220, 884763263038)
    store32(9242216, 12)
    store32(9242204, 0)
    store32(9242196, 0)
    store8(9242107, 1)
    store8(9242104, 1)
    store32(9242416, 0)
    store32(9242360, (v0 + 199))
    store64(9242352, 884763263039)
    store32(9242348, 12)
    store32(9242336, 0)
    store32(9242328, 0)
    store8(9242239, 1)
    store8(9242236, 1)
    store32(9242548, 0)
    store32(9242492, (v0 + 200))
    store64(9242484, 876173328401)
    store32(9242480, 12)
    store32(9242468, 0)
    store32(9242460, 0)
    store8(9242371, 1)
    store8(9242368, 1)
    store32(9242680, 0)
    store32(9242624, (v0 + 201))
    store64(9242616, 820338753547)
    store32(9242612, 12)
    store32(9242600, 0)
    store32(9242592, 0)
    store8(9242503, 1)
    store8(9242500, 1)
    store32(9242812, 0)
    store32(9242756, (v0 + 202))
    store64(9242748, 811748819050)
    store32(9242744, 12)
    store32(9242732, 0)
    store32(9242724, 0)
    store8(9242635, 1)
    store8(9242632, 1)
    store32(9242944, 0)
    store32(9242888, (v0 + 203))
    store64(9242880, 850403524632)
    store32(9242876, 12)
    store32(9242864, 0)
    store32(9242856, 0)
    store8(9242767, 1)
    store8(9242764, 1)
    store32(9243076, 0)
    store32(9243020, (v0 + 204))
    store64(9243012, 850403524716)
    store32(9243008, 12)
    store32(9242996, 0)
    store32(9242988, 0)
    store8(9242899, 1)
    store8(9242896, 1)
    store32(9243208, 0)
    store32(9243152, (v0 + 205))
    store64(9243144, 846108557337)
    store32(9243140, 12)
    store32(9243128, 0)
    store32(9243120, 0)
    store8(9243031, 1)
    store8(9243028, 1)
    store32(9243340, 0)
    store32(9243284, (v0 + 206))
    store64(9243276, 833223655457)
    store32(9243272, 12)
    store32(9243260, 0)
    store32(9243252, 0)
    store8(9243163, 1)
    store8(9243160, 1)
    store32(9243472, 0)
    store32(9243416, (v0 + 207))
    store64(9243408, 824633720848)
    store32(9243404, 12)
    store32(9243392, 0)
    store32(9243384, 0)
    store8(9243295, 1)
    store8(9243292, 1)
    store32(9243604, 0)
    store32(9243548, (v0 + 208))
    store64(9243540, 824633720939)
    store32(9243536, 12)
    store32(9243524, 0)
    store32(9243516, 0)
    store8(9243427, 1)
    store8(9243424, 1)
    store32(9243736, 0)
    store32(9243680, (v0 + 209))
    store64(9243672, 279172874276)
    store32(9243668, 12)
    store32(9243656, 0)
    store32(9243648, 0)
    store8(9243559, 1)
    store8(9243556, 1)
    store32(9243868, 0)
    store32(9243812, (v0 + 210))
    store64(9243804, 828928688151)
    store32(9243800, 12)
    store32(9243788, 0)
    store32(9243780, 0)
    store8(9243691, 1)
    store8(9243688, 1)
    store32(9244000, 0)
    store32(9243944, (v0 + 211))
    store64(9243936, 867583393818)
    store32(9243932, 12)
    store32(9243920, 0)
    store32(9243912, 0)
    store8(9243823, 1)
    store8(9243820, 1)
    store32(9244132, 0)
    store32(9244076, (v0 + 212))
    store64(9244068, 863288426525)
    store32(9244064, 12)
    store32(9244052, 0)
    store32(9244044, 0)
    store8(9243955, 1)
    store8(9243952, 1)
    store32(9244264, 0)
    store32(9244208, (v0 + 213))
    store64(9244200, 863288426594)
    store32(9244196, 12)
    store32(9244184, 0)
    store32(9244176, 0)
    store8(9244087, 1)
    store8(9244084, 1)
    store32(9244396, 0)
    store32(9244340, (v0 + 214))
    store64(9244332, 841813590044)
    store32(9244328, 12)
    store32(9244316, 0)
    store32(9244308, 0)
    store8(9244219, 1)
    store8(9244216, 1)
    store32(9244528, 0)
    store32(9244472, (v0 + 215))
    store64(9244464, 841813590119)
    store32(9244460, 12)
    store32(9244448, 0)
    store32(9244440, 0)
    store8(9244351, 1)
    store8(9244348, 1)
    store32(9244660, 0)
    store32(9244604, (v0 + 216))
    store64(9244596, 893353197598)
    store32(9244592, 12)
    store32(9244580, 0)
    store32(9244572, 0)
    store8(9244483, 1)
    store8(9244480, 1)
    store32(9244792, 0)
    store32(9244736, (v0 + 217))
    store64(9244728, 837518622751)
    store32(9244724, 12)
    store32(9244712, 0)
    store32(9244704, 0)
    store8(9244615, 1)
    store8(9244612, 1)
    store32(9244924, 0)
    store32(9244868, (v0 + 218))
    store64(9244860, 807453851689)
    store32(9244856, 12)
    store32(9244844, 0)
    store32(9244836, 0)
    store8(9244747, 1)
    store8(9244744, 1)
    store32(9245056, 0)
    store32(9245000, (v0 + 219))
    store64(9244992, 678604832802)
    store32(9244988, 12)
    store32(9244976, 0)
    store32(9244968, 0)
    store8(9244879, 1)
    store8(9244876, 1)
    store32(9245188, 0)
    store32(9245132, (v0 + 220))
    store64(9245124, 901943132173)
    store32(9245120, 12)
    store32(9245108, 0)
    store32(9245100, 0)
    store8(9245011, 1)
    store8(9245008, 1)
    store32(9245320, 0)
    store32(9245264, (v0 + 221))
    store64(9245256, 897648164910)
    store32(9245252, 12)
    store32(9245240, 0)
    store32(9245232, 0)
    store8(9245143, 1)
    store8(9245140, 1)
    store32(9245452, 0)
    store32(9245396, (v0 + 222))
    store64(9245388, 755914244131)
    store32(9245384, 12)
    store32(9245372, 0)
    store32(9245364, 0)
    store8(9245275, 1)
    store8(9245272, 1)
    store32(9245584, 0)
    store32(9245528, (v0 + 223))
    store64(9245520, 425201762318)
    store32(9245516, 1)
    store32(9245504, 0)
    store32(9245496, 0)
    store8(9245407, 1)
    store8(9245404, 1)
    store32(9245716, 0)
    store32(9245660, (v0 + 224))
    store64(9245652, 326417514535)
    store32(9245648, 1)
    store32(9245636, 245)
    store32(9245628, 0)
    store8(9245539, 0)
    store8(9245536, 1)
    store32(9245848, 0)
    store32(9245792, (v0 + 225))
    store64(9245784, 330712481832)
    store32(9245780, 1)
    store32(9245768, 412)
    store32(9245760, 0)
    store8(9245671, 0)
    store8(9245668, 1)
    store32(9245980, 0)
    store32(9245924, (v0 + 226))
    store64(9245916, 335007449129)
    store32(9245912, 1)
    store32(9245900, 265)
    store32(9245892, 0)
    store8(9245803, 0)
    store8(9245800, 1)
    store32(9246112, 0)
    store32(9246056, (v0 + 227))
    store64(9246048, 107374182442)
    store32(9246044, 1)
    store32(9246032, 413)
    store32(9246024, 0)
    store8(9245935, 0)
    store8(9245932, 1)
    store32(9246244, 0)
    store32(9246188, (v0 + 228))
    store64(9246180, 493921239083)
    store32(9246176, 13)
    store32(9246164, 266)
    store32(9246156, 0)
    store8(9246067, 0)
    store8(9246064, 1)
    store32(9246376, 0)
    store32(9246320, (v0 + 229))
    store64(9246312, 1129576398865)
    store32(9246308, 1)
    store32(9246296, 417)
    store32(9246288, 0)
    store8(9246199, 0)
    store8(9246196, 1)
    store32(9246508, 0)
    store32(9246452, (v0 + 230))
    store64(9246444, 721554505744)
    store32(9246440, 13)
    store32(9246428, 246)
    store32(9246420, 0)
    store8(9246331, 0)
    store8(9246328, 1)
    store32(9246640, 0)
    store32(9246584, (v0 + 231))
    store64(9246576, 511101108239)
    store32(9246572, 13)
    store32(9246560, 414)
    store32(9246552, 0)
    store8(9246463, 0)
    store8(9246460, 1)
    store32(9246772, 0)
    store32(9246716, (v0 + 232))
    store64(9246708, 932007903233)
    store32(9246704, 14)
    store32(9246692, 415)
    store32(9246684, 0)
    store8(9246595, 0)
    store8(9246592, 1)
    store32(9246904, 0)
    store32(9246848, (v0 + 233))
    store64(9246840, 932007903250)
    store32(9246836, 15)
    store32(9246824, 244)
    store32(9246816, 0)
    store8(9246727, 0)
    store8(9246724, 1)
    store32(9247036, 0)
    store32(9246980, (v0 + 234))
    store64(9246972, 137438953495)
    store32(9246968, 1)
    store32(9246956, 244)
    store32(9246948, 0)
    store8(9246859, 0)
    store8(9246856, 1)
    store32(9247168, 0)
    store32(9247112, (v0 + 235))
    store64(9247104, 141733920768)
    store32(9247100, 16)
    store32(9247088, 416)
    store32(9247080, 0)
    store8(9246991, 0)
    store8(9246988, 1)
    store32(9247300, 0)
    store32(9247244, (v0 + 236))
    store64(9247236, 837518622831)
    store32(9247232, 12)
    store32(9247220, 426)
    store32(9247212, 0)
    store8(9247123, 0)
    store8(9247120, 1)
    store32(9247432, 0)
    store32(9247376, (v0 + 237))
    store64(9247368, 837518622812)
    store32(9247364, 12)
    store32(9247352, 0)
    store32(9247344, 0)
    store8(9247255, 1)
    store8(9247252, 1)
    store32(9247564, 0)
    store32(9247508, (v0 + 238))
    store64(9247500, 854698492016)
    store32(9247496, 12)
    store32(9247484, 0)
    store32(9247476, 0)
    store8(9247387, 1)
    store8(9247384, 1)
    store32(9247696, 0)
    store32(9247640, (v0 + 239))
    store64(9247632, 858993459313)
    store32(9247628, 12)
    store32(9247616, 0)
    store32(9247608, 0)
    store8(9247519, 1)
    store8(9247516, 1)
    store32(9247828, 0)
    store32(9247772, (v0 + 240))
    store64(9247764, 858993459294)
    store32(9247760, 12)
    store32(9247748, 0)
    store32(9247740, 0)
    store8(9247651, 1)
    store8(9247648, 1)
    store32(9247960, 0)
    store32(9247904, (v0 + 241))
    store64(9247896, 828928688242)
    store32(9247892, 12)
    store32(9247880, 0)
    store32(9247872, 0)
    store8(9247783, 1)
    store8(9247780, 1)
    store32(9248092, 0)
    store32(9248036, (v0 + 242))
    store64(9248028, 828928688223)
    store32(9248024, 12)
    store32(9248012, 0)
    store32(9248004, 0)
    store8(9247915, 1)
    store8(9247912, 1)
    store32(9248224, 0)
    store32(9248168, (v0 + 243))
    store64(9248160, 807453851763)
    store32(9248156, 12)
    store32(9248144, 0)
    store32(9248136, 0)
    store8(9248047, 1)
    store8(9248044, 1)
    store32(9248356, 0)
    store32(9248300, (v0 + 244))
    store64(9248292, 807453851744)
    store32(9248288, 12)
    store32(9248276, 0)
    store32(9248268, 0)
    store8(9248179, 1)
    store8(9248176, 1)
    store32(9248488, 0)
    store32(9248432, (v0 + 245))
    store64(9248424, 867583393908)
    store32(9248420, 12)
    store32(9248408, 0)
    store32(9248400, 0)
    store8(9248311, 1)
    store8(9248308, 1)
    store32(9248620, 0)
    store32(9248564, (v0 + 246))
    store64(9248556, 867583393889)
    store32(9248552, 12)
    store32(9248540, 0)
    store32(9248532, 0)
    store8(9248443, 1)
    store8(9248440, 1)
    store32(9248752, 0)
    store32(9248696, (v0 + 247))
    store64(9248688, 863288426613)
    store32(9248684, 12)
    store32(9248672, 0)
    store32(9248664, 0)
    store8(9248575, 1)
    store8(9248572, 1)
    store32(9248884, 0)
    store32(9248828, (v0 + 248))
    store64(9248820, 846108557430)
    store32(9248816, 12)
    store32(9248804, 0)
    store32(9248796, 0)
    store8(9248707, 1)
    store8(9248704, 1)
    store32(9249016, 0)
    store32(9248960, (v0 + 249))
    store64(9248952, 846108557411)
    store32(9248948, 12)
    store32(9248936, 0)
    store32(9248928, 0)
    store8(9248839, 1)
    store8(9248836, 1)
    store32(9249148, 0)
    store32(9249092, (v0 + 250))
    store64(9249084, 893353197687)
    store32(9249080, 12)
    store32(9249068, 0)
    store32(9249060, 0)
    store8(9248971, 1)
    store8(9248968, 1)
    store32(9249280, 0)
    store32(9249224, (v0 + 251))
    store64(9249216, 893353197668)
    store32(9249212, 12)
    store32(9249200, 0)
    store32(9249192, 0)
    store8(9249103, 1)
    store8(9249100, 1)
    store32(9249412, 0)
    store32(9249356, (v0 + 252))
    store64(9249348, 833223655544)
    store32(9249344, 12)
    store32(9249332, 0)
    store32(9249324, 0)
    store8(9249235, 1)
    store8(9249232, 1)
    store32(9249544, 0)
    store32(9249488, (v0 + 253))
    store64(9249480, 833223655525)
    store32(9249476, 12)
    store32(9249464, 0)
    store32(9249456, 0)
    store8(9249367, 1)
    store8(9249364, 1)
    store32(9249676, 0)
    store32(9249620, (v0 + 254))
    store64(9249612, 841813590137)
    store32(9249608, 12)
    store32(9249596, 0)
    store32(9249588, 0)
    store8(9249499, 1)
    store8(9249496, 1)
    store32(9249808, 0)
    store32(9249752, (v0 + 255))
    store64(9249744, 678604832890)
    store32(9249740, 12)
    store32(9249728, 0)
    store32(9249720, 0)
    store8(9249631, 1)
    store8(9249628, 1)
    store32(9249940, 0)
    store32(9249884, (v0 + 256))
    store64(9249876, 678604832872)
    store32(9249872, 12)
    store32(9249860, 0)
    store32(9249852, 0)
    store8(9249763, 1)
    store8(9249760, 1)
    store32(9250072, 0)
    store32(9250016, (v0 + 257))
    store64(9250008, 816043786363)
    store32(9250004, 12)
    store32(9249992, 0)
    store32(9249984, 0)
    store8(9249895, 1)
    store8(9249892, 1)
    store32(9250204, 0)
    store32(9250148, (v0 + 258))
    store64(9250140, 824633720956)
    store32(9250136, 12)
    store32(9250124, 0)
    store32(9250116, 0)
    store8(9250027, 1)
    store8(9250024, 1)
    store32(9250336, 0)
    store32(9250280, (v0 + 259))
    store64(9250272, 85899345920)
    store32(9250268, 17)
    store32(9250256, 0)
    store32(9250248, 0)
    store8(9250159, 1)
    store8(9250156, 1)
    store32(9250468, 0)
    store32(9250412, (v0 + 260))
    store64(9250404, 197568495726)
    store32(9250400, 12)
    store32(9250388, 815)
    store32(9250380, 0)
    store8(9250291, 0)
    store8(9250288, 1)
    store32(9250600, 0)
    store32(9250544, (v0 + 261))
    store64(9250536, 850403524733)
    store32(9250532, 12)
    store32(9250520, 0)
    store32(9250512, 0)
    store8(9250423, 1)
    store8(9250420, 1)
    store32(9250732, 0)
    store32(9250676, (v0 + 262))
    store64(9250668, 876173328510)
    store32(9250664, 12)
    store32(9250652, 0)
    store32(9250644, 0)
    store8(9250555, 1)
    store8(9250552, 1)
    store32(9250864, 0)
    store32(9250808, (v0 + 263))
    store64(9250800, 876173328493)
    store32(9250796, 12)
    store32(9250784, 0)
    store32(9250776, 0)
    store8(9250687, 1)
    store8(9250684, 1)
    store32(9250996, 0)
    store32(9250940, (v0 + 264))
    store64(9250932, 201863462969)
    store32(9250928, 12)
    store32(9250916, 0)
    store32(9250908, 0)
    store8(9250819, 1)
    store8(9250816, 1)
    store32(9251128, 0)
    store32(9251072, (v0 + 265))
    store64(9251064, 120259084335)
    store32(9251060, 1)
    store32(9251048, 0)
    store32(9251040, 0)
    store8(9250951, 1)
    store8(9250948, 1)
    store32(9251180, 799)
    store32(9251172, 0)
    store8(9251083, 0)
    store8(9251080, 1)
    v1 = load32(38760)
    store32(9251260, 0)
    store32(9251204, (v0 + 266))
    store32(9251200, 236)
    store32(9251196, v1)
    store32(9251192, 18)
    store8(9251212, 1)
    store8(9251215, 0)
    store64(9251328, 73014444032)
    store32(9251304, 0)
    store32(9251312, 447)
    store32(9251324, 19)
    store32(9251336, (v0 + 267))
    store32(9251392, 0)
    store8(9251347, 0)
    store8(9251344, 1)
    store32(9251524, 0)
    store32(9251468, (v0 + 268))
    store32(9251456, 20)
    store32(9251444, 109)
    store32(9251436, 0)
    store64(9251460, 64424509440)
    store32(9251656, 0)
    store32(9251600, (v0 + 269))
    store64(9251592, 68719476736)
    store32(9251588, 21)
    store32(9251576, 843)
    store32(9251568, 0)
    store8(9251479, 0)
    store8(9251476, 1)
    store32(9251788, 0)
    store32(9251732, (v0 + 270))
    store64(9251724, 1052266987520)
    store32(9251720, 22)
    store32(9251708, 844)
    store32(9251700, 0)
    store8(9251611, 0)
    store8(9251608, 1)
    store32(9251920, 0)
    store32(9251864, (v0 + 271))
    store64(9251856, 1095216660480)
    store32(9251852, 2)
    store32(9251840, 425)
    store32(9251832, 0)
    store8(9251743, 0)
    store8(9251740, 1)
    store32(9252052, 0)
    store32(9251996, (v0 + 272))
    store64(9251988, 627065225244)
    store32(9251984, 13)
    store32(9251972, 0)
    store32(9251964, 0)
    store8(9251875, 0)
    store8(9251872, 1)
    store32(9252184, 0)
    store32(9252128, (v0 + 273))
    store64(9252120, 506806140955)
    store32(9252116, 13)
    store32(9252104, 371)
    store32(9252096, 0)
    store8(9252007, 0)
    store8(9252004, 1)
    store32(9252316, 0)
    store32(9252260, (v0 + 274))
    store64(9252252, 957777707038)
    store32(9252248, 1)
    store32(9252236, 368)
    store32(9252228, 0)
    store8(9252139, 0)
    store8(9252136, 1)
    store32(9252448, 0)
    store32(9252392, (v0 + 275))
    store64(9252384, 1133871366170)
    store32(9252380, 1)
    store32(9252368, 375)
    store32(9252360, 0)
    store8(9252271, 0)
    store8(9252268, 1)
    store32(9252580, 0)
    store32(9252524, (v0 + 276))
    store64(9252516, 373662154781)
    store32(9252512, 1)
    store32(9252500, 363)
    store32(9252492, 0)
    store8(9252403, 0)
    store8(9252400, 1)
    store32(9252712, 0)
    store32(9252656, (v0 + 277))
    store64(9252648, 541165879385)
    store32(9252644, 5)
    store32(9252632, 374)
    store32(9252624, 0)
    store8(9252535, 0)
    store8(9252532, 1)
    store32(9252844, 0)
    store32(9252788, (v0 + 278))
    store64(9252780, 365072220367)
    store32(9252776, 7)
    store32(9252764, 0)
    store32(9252756, 0)
    store8(9252667, 1)
    store8(9252664, 1)
    store32(9252976, 0)
    store32(9252920, (v0 + 279))
    store64(9252912, 992137445584)
    store32(9252908, 7)
    store32(9252896, 0)
    store32(9252888, 0)
    store8(9252799, 1)
    store8(9252796, 1)
    store32(9253108, 0)
    store32(9253052, (v0 + 280))
    store64(9253044, 360777253073)
    store32(9253040, 7)
    store32(9253028, 0)
    store32(9253020, 0)
    store8(9252931, 1)
    store8(9252928, 1)
    store32(9253240, 0)
    store32(9253184, (v0 + 281))
    store64(9253176, 1013612282066)
    store32(9253172, 7)
    store32(9253160, 0)
    store32(9253152, 0)
    store8(9253063, 1)
    store8(9253060, 1)
    store32(9253372, 0)
    store32(9253316, (v0 + 282))
    store64(9253308, 627065225427)
    store32(9253304, 7)
    store32(9253292, 0)
    store32(9253284, 0)
    store8(9253195, 1)
    store8(9253192, 1)
    store32(9253504, 0)
    store32(9253448, (v0 + 283))
    store64(9253440, 369367187668)
    store32(9253436, 7)
    store32(9253424, 0)
    store32(9253416, 0)
    store8(9253327, 1)
    store8(9253324, 1)
    store32(9253636, 0)
    store32(9253580, (v0 + 284))
    store64(9253572, 1133871366357)
    store32(9253568, 7)
    store32(9253556, 0)
    store32(9253548, 0)
    store8(9253459, 1)
    store8(9253456, 1)
    store32(9253768, 0)
    store32(9253712, (v0 + 285))
    store64(9253704, 962072674518)
    store32(9253700, 7)
    store32(9253688, 0)
    store32(9253680, 0)
    store8(9253591, 1)
    store8(9253588, 1)
    store32(9253900, 0)
    store32(9253844, (v0 + 286))
    store64(9253836, 373662154967)
    store32(9253832, 7)
    store32(9253820, 0)
    store32(9253812, 0)
    store8(9253723, 1)
    store8(9253720, 1)
    store32(9254032, 0)
    store32(9253976, (v0 + 287))
    store64(9253968, 506806141144)
    store32(9253964, 7)
    store32(9253952, 0)
    store32(9253944, 0)
    store8(9253855, 1)
    store8(9253852, 1)
    store32(9254164, 0)
    store32(9254108, (v0 + 288))
    store64(9254100, 455266533593)
    store32(9254096, 7)
    store32(9254084, 0)
    store32(9254076, 0)
    store8(9253987, 1)
    store8(9253984, 1)
    store32(9254296, 0)
    store32(9254240, (v0 + 289))
    store64(9254232, 996432412890)
    store32(9254228, 7)
    store32(9254216, 0)
    store32(9254208, 0)
    store8(9254119, 1)
    store8(9254116, 1)
    store32(9254428, 0)
    store32(9254372, (v0 + 290))
    store64(9254364, 347892351195)
    store32(9254360, 7)
    store32(9254348, 0)
    store32(9254340, 0)
    store8(9254251, 1)
    store8(9254248, 1)
    store32(9254560, 0)
    store32(9254504, (v0 + 291))
    store64(9254496, 85899345920)
    store32(9254492, 2)
    store32(9254480, 0)
    store32(9254472, 0)
    store8(9254383, 1)
    store8(9254380, 1)
    store32(9254692, 0)
    store32(9254636, (v0 + 292))
    store64(9254628, 579820585180)
    store32(9254624, 7)
    store32(9254612, 0)
    store32(9254604, 0)
    store8(9254515, 0)
    store8(9254512, 1)
    store32(9254824, 0)
    store32(9254768, (v0 + 293))
    store64(9254760, 687194767360)
    store32(9254756, 2)
    store32(9254744, 0)
    store32(9254736, 0)
    store8(9254647, 1)
    store8(9254644, 1)
    store32(9254956, 0)
    store32(9254900, (v0 + 294))
    store64(9254892, 64424509440)
    store32(9254888, 23)
    store32(9254876, 0)
    store32(9254868, 0)
    store8(9254779, 0)
    store8(9254776, 1)
    store32(9255088, 0)
    store32(9255032, (v0 + 295))
    store64(9255024, 73014444032)
    store32(9255020, 24)
    store32(9255008, 843)
    store32(9255000, 0)
    store8(9254911, 0)
    store8(9254908, 1)
    store32(9255220, 0)
    store32(9255164, (v0 + 296))
    store64(9255156, 64424509440)
    store32(9255152, 25)
    store32(9255140, 109)
    store32(9255132, 0)
    store8(9255043, 0)
    store8(9255040, 1)
    store32(9255352, 0)
    store32(9255296, (v0 + 297))
    store64(9255288, 73014444032)
    store32(9255284, 26)
    store32(9255272, 843)
    store32(9255264, 0)
    store8(9255175, 0)
    store8(9255172, 1)
    store32(9255484, 0)
    store32(9255428, (v0 + 298))
    store64(9255420, 68719476736)
    store32(9255416, 27)
    store32(9255404, 109)
    store32(9255396, 0)
    store8(9255307, 0)
    store8(9255304, 1)
    store32(9255616, 0)
    store32(9255560, (v0 + 299))
    store64(9255552, 68719476736)
    store32(9255548, 28)
    store32(9255536, 844)
    store32(9255528, 0)
    store8(9255439, 0)
    store8(9255436, 1)
    store32(9255748, 0)
    store32(9255692, (v0 + 300))
    store64(9255684, 1052266987520)
    store32(9255680, 29)
    store32(9255668, 844)
    store32(9255660, 0)
    store8(9255571, 0)
    store8(9255568, 1)
    store32(9255880, 0)
    store32(9255824, (v0 + 301))
    store64(9255816, 1052266987520)
    store32(9255812, 30)
    store32(9255800, 425)
    store32(9255792, 0)
    store8(9255703, 0)
    store8(9255700, 1)
    store32(9256012, 0)
    store32(9255956, (v0 + 302))
    store64(9255948, 94489280512)
    store32(9255944, 31)
    store32(9255932, 425)
    store32(9255924, 0)
    store8(9255835, 0)
    store8(9255832, 1)
    store32(9256144, 0)
    store32(9256088, (v0 + 303))
    store64(9256080, 1030792151040)
    store32(9256076, 32)
    store32(9256064, 0)
    store32(9256056, 0)
    store8(9255967, 0)
    store8(9255964, 1)
    store32(9256276, 0)
    store32(9256220, (v0 + 304))
    store64(9256212, 1026497183744)
    store32(9256208, 2)
    store32(9256196, 875)
    store32(9256188, 0)
    store8(9256099, 0)
    store8(9256096, 1)
    store32(9256408, 0)
    store32(9256352, (v0 + 305))
    store64(9256344, 0)
    store32(9256340, 33)
    store32(9256328, 0)
    store32(9256320, 0)
    store8(9256231, 0)
    store8(9256228, 1)
    store32(9256540, 0)
    store32(9256484, (v0 + 306))
    store64(9256476, 983547510826)
    store32(9256472, 5)
    store32(9256460, 875)
    store32(9256452, 0)
    store8(9256363, 0)
    store8(9256360, 1)
    store32(9256672, 0)
    store32(9256616, (v0 + 307))
    store64(9256608, 747324309753)
    store32(9256604, 7)
    store32(9256592, 0)
    store32(9256584, 0)
    store8(9256495, 1)
    store8(9256492, 1)
    store32(9256804, 0)
    store32(9256748, (v0 + 308))
    store64(9256740, 644245094400)
    store32(9256736, 34)
    store32(9256724, 0)
    store32(9256716, 0)
    store8(9256627, 1)
    store8(9256624, 1)
    store32(9256936, 0)
    store32(9256880, (v0 + 309))
    store64(9256872, 695784701952)
    store32(9256868, 35)
    store32(9256856, 431)
    store32(9256848, 0)
    store8(9256759, 0)
    store8(9256756, 1)
    store32(9257068, 0)
    store32(9257012, (v0 + 310))
    store64(9257004, 639950127104)
    store32(9257000, 36)
    store32(9256988, 430)
    store32(9256980, 0)
    store8(9256891, 0)
    store8(9256888, 1)
    store32(9257200, 0)
    store32(9257144, (v0 + 311))
    store64(9257136, 103079215104)
    store32(9257132, 37)
    store32(9257120, 429)
    store32(9257112, 0)
    store8(9257023, 0)
    store8(9257020, 1)
    store32(9257332, 0)
    store32(9257276, (v0 + 312))
    store64(9257268, 4294967296)
    store32(9257264, 38)
    store32(9257252, 432)
    store32(9257244, 0)
    store8(9257155, 0)
    store8(9257152, 1)
    store32(9257464, 0)
    store32(9257408, (v0 + 313))
    store64(9257400, 803158884352)
    store32(9257396, 39)
    store32(9257384, 873)
    store32(9257376, 0)
    store8(9257287, 0)
    store8(9257284, 1)
    store32(9257596, 0)
    store32(9257540, (v0 + 314))
    store64(9257532, 1155346202624)
    store32(9257528, 40)
    store32(9257516, 427)
    store32(9257508, 0)
    store8(9257419, 0)
    store8(9257416, 1)
    store32(9257728, 0)
    store32(9257672, (v0 + 315))
    store64(9257664, 1065151889408)
    store32(9257660, 41)
    store32(9257648, 428)
    store32(9257640, 0)
    store8(9257551, 0)
    store8(9257548, 1)
    store32(9257860, 0)
    store32(9257804, (v0 + 316))
    store64(9257796, 77309411329)
    store32(9257792, 41)
    store32(9257780, 0)
    store32(9257772, 0)
    store8(9257683, 0)
    store8(9257680, 1)
    store32(9257992, 0)
    store32(9257936, (v0 + 317))
    store64(9257928, 399431958528)
    store32(9257924, 42)
    store32(9257912, 0)
    store32(9257904, 0)
    store8(9257815, 0)
    store8(9257812, 1)
    store32(9258124, 0)
    store32(9258068, (v0 + 318))
    store64(9258060, 163208757248)
    store32(9258056, 43)
    store32(9258044, 433)
    store32(9258036, 0)
    store8(9257947, 0)
    store8(9257944, 1)
    store32(9258256, 0)
    store32(9258200, (v0 + 319))
    store64(9258192, 150323855360)
    store32(9258188, 44)
    store32(9258176, 419)
    store32(9258168, 0)
    store8(9258079, 0)
    store8(9258076, 1)
    store32(9258388, 0)
    store32(9258332, (v0 + 320))
    store64(9258324, 146028888065)
    store32(9258320, 44)
    store32(9258308, 420)
    store32(9258300, 0)
    store8(9258211, 0)
    store8(9258208, 1)
    store32(9258520, 0)
    store32(9258464, (v0 + 321))
    store64(9258456, 158913789954)
    store32(9258452, 44)
    store32(9258440, 423)
    store32(9258432, 0)
    store8(9258343, 0)
    store8(9258340, 1)
    store32(9258652, 0)
    store32(9258596, (v0 + 322))
    store64(9258588, 154618822659)
    store32(9258584, 44)
    store32(9258572, 422)
    store32(9258564, 0)
    store8(9258475, 0)
    store8(9258472, 1)
    store32(9258784, 0)
    store32(9258728, (v0 + 323))
    store64(9258720, 167503724544)
    store32(9258716, 45)
    store32(9258704, 421)
    store32(9258696, 0)
    store8(9258607, 0)
    store8(9258604, 1)
    store32(9258916, 0)
    store32(9258860, (v0 + 324))
    store64(9258852, 167503724581)
    store32(9258848, 1)
    store32(9258836, 424)
    store32(9258828, 0)
    store8(9258739, 0)
    store8(9258736, 1)
    store32(9259048, 0)
    store32(9258992, (v0 + 325))
    store64(9258984, 1133871366170)
    store32(9258980, 2)
    store32(9258968, 0)
    store32(9258960, 0)
    store8(9258871, 0)
    store8(9258868, 1)
    store32(9259180, 0)
    store32(9259124, (v0 + 326))
    store64(9259116, 425201762318)
    store32(9259112, 2)
    store32(9259100, 0)
    store32(9259092, 0)
    store8(9259003, 0)
    store8(9259000, 1)
    store32(9259312, 0)
    store32(9259256, (v0 + 327))
    store64(9259248, 326417514535)
    store32(9259244, 2)
    store32(9259232, 245)
    store32(9259224, 0)
    store8(9259135, 0)
    store8(9259132, 1)
    store32(9259444, 0)
    store32(9259388, (v0 + 328))
    store64(9259380, 107374182442)
    store32(9259376, 2)
    store32(9259364, 412)
    store32(9259356, 0)
    store8(9259267, 0)
    store8(9259264, 1)
    store32(9259576, 0)
    store32(9259520, (v0 + 329))
    store64(9259512, 493921239083)
    store32(9259508, 2)
    store32(9259496, 266)
    store32(9259488, 0)
    store8(9259399, 0)
    store8(9259396, 1)
    store32(9259708, 0)
    store32(9259652, (v0 + 330))
    store64(9259644, 506806140955)
    store32(9259640, 2)
    store32(9259628, 417)
    store32(9259620, 0)
    store8(9259531, 0)
    store8(9259528, 1)
    store32(9259840, 0)
    store32(9259784, (v0 + 331))
    store64(9259776, 511101108239)
    store32(9259772, 2)
    store32(9259760, 0)
    store32(9259752, 0)
    store8(9259663, 0)
    store8(9259660, 1)
    store32(9259972, 0)
    store32(9259916, (v0 + 332))
    store64(9259908, 627065225244)
    store32(9259904, 2)
    store32(9259892, 415)
    store32(9259884, 0)
    store8(9259795, 0)
    store8(9259792, 1)
    store32(9260104, 0)
    store32(9260048, (v0 + 333))
    store64(9260040, 721554505744)
    store32(9260036, 2)
    store32(9260024, 0)
    store32(9260016, 0)
    store8(9259927, 0)
    store8(9259924, 1)
    store32(9260236, 0)
    store32(9260180, (v0 + 334))
    store64(9260172, 682899800073)
    store32(9260168, 2)
    store32(9260156, 414)
    store32(9260148, 0)
    store8(9260059, 0)
    store8(9260056, 1)
    store32(9260368, 0)
    store32(9260312, (v0 + 335))
    store64(9260304, 932007903250)
    store32(9260300, 2)
    store32(9260288, 0)
    store32(9260280, 0)
    store8(9260191, 0)
    store8(9260188, 1)
    store32(9260500, 0)
    store32(9260444, (v0 + 336))
    store64(9260436, 940597837837)
    store32(9260432, 2)
    store32(9260420, 244)
    store32(9260412, 0)
    store8(9260323, 0)
    store8(9260320, 1)
    store32(9260632, 0)
    store32(9260576, (v0 + 337))
    store64(9260568, 98784247854)
    store32(9260564, 2)
    store32(9260552, 0)
    store32(9260544, 0)
    store8(9260455, 0)
    store8(9260452, 1)
    store32(9260764, 0)
    store32(9260708, (v0 + 338))
    store64(9260700, 1129576398865)
    store32(9260696, 2)
    store32(9260684, 0)
    store32(9260676, 0)
    store8(9260587, 0)
    store8(9260584, 1)
    store32(9260896, 0)
    store32(9260840, (v0 + 339))
    store64(9260832, 330712481832)
    store32(9260828, 2)
    store32(9260816, 246)
    store32(9260808, 0)
    store8(9260719, 0)
    store8(9260716, 1)
    store32(9261028, 0)
    store32(9260972, (v0 + 340))
    store64(9260964, 957777707038)
    store32(9260960, 2)
    store32(9260948, 265)
    store32(9260940, 0)
    store8(9260851, 0)
    store8(9260848, 1)
    store32(9261160, 0)
    store32(9261104, (v0 + 341))
    store64(9261096, 373662154781)
    store32(9261092, 2)
    store32(9261080, 0)
    store32(9261072, 0)
    store8(9260983, 0)
    store8(9260980, 1)
    store32(9261292, 0)
    store32(9261236, (v0 + 342))
    store64(9261228, 335007449129)
    store32(9261224, 2)
    store32(9261212, 0)
    store32(9261204, 0)
    store8(9261115, 0)
    store8(9261112, 1)
    store32(9261424, 0)
    store32(9261368, (v0 + 343))
    store64(9261360, 751619277052)
    store32(9261356, 7)
    store32(9261344, 413)
    store32(9261336, 0)
    store8(9261247, 0)
    store8(9261244, 1)
    store32(9261556, 0)
    store32(9261500, (v0 + 344))
    store64(9261492, 906238099708)
    store32(9261488, 46)
    store32(9261476, 439)
    store32(9261468, 0)
    store8(9261379, 1)
    store8(9261376, 1)
    store32(9261688, 0)
    store32(9261632, (v0 + 345))
    store64(9261624, 1056561954816)
    store32(9261620, 47)
    store32(9261608, 0)
    store32(9261600, 0)
    store8(9261511, 0)
    store8(9261508, 1)
    store32(9261820, 0)
    store32(9261764, (v0 + 346))
    store64(9261756, 21474836480)
    store32(9261752, 48)
    store32(9261740, 462)
    store32(9261732, 0)
    store8(9261643, 0)
    store8(9261640, 1)
    store32(9261952, 0)
    store32(9261896, (v0 + 347))
    store64(9261888, 352187318272)
    store32(9261884, 49)
    store32(9261872, 512)
    store32(9261864, 0)
    store8(9261775, 0)
    store8(9261772, 1)
    store32(9262084, 0)
    store32(9262028, (v0 + 348))
    store64(9262020, 25769803776)
    store32(9262016, 50)
    store32(9262004, 513)
    store32(9261996, 0)
    store8(9261907, 0)
    store8(9261904, 1)
    store32(9262216, 0)
    store32(9262160, (v0 + 349))
    store64(9262152, 30064771072)
    store32(9262148, 51)
    store32(9262136, 514)
    store32(9262128, 0)
    store8(9262039, 0)
    store8(9262036, 1)
    store32(9262268, 515)
    store32(9262260, 0)
    store8(9262171, 0)
    store8(9262168, 1)
    v1 = load32(38920)
    store32(9262348, 0)
    store32(9262292, (v0 + 350))
    store32(9262288, 44)
    store32(9262284, v1)
    store32(9262280, 18)
    store8(9262300, 1)
    store8(9262303, 0)
    store64(9262416, 38654705664)
    store32(9262392, 0)
    store32(9262400, 518)
    store32(9262412, 52)
    store32(9262424, (v0 + 351))
    store32(9262480, 0)
    store8(9262435, 0)
    store8(9262432, 1)
    store32(9262612, 0)
    store32(9262556, (v0 + 352))
    store32(9262544, 53)
    store32(9262532, 527)
    store32(9262524, 0)
    store64(9262548, 34359738368)
    store32(9262664, 528)
    store32(9262656, 0)
    store8(9262567, 0)
    store8(9262564, 1)
    v1 = load32(38832)
    store32(9262744, 0)
    store32(9262688, (v0 + 353))
    store32(9262684, 218)
    store32(9262680, v1)
    store32(9262676, 12)
    store8(9262696, 1)
    store8(9262699, 1)
    store64(9262812, 1052266987520)
    store32(9262788, 0)
    store32(9262796, 0)
    store32(9262808, 54)
    store32(9262820, (v0 + 354))
    store32(9262876, 0)
    store8(9262831, 0)
    store8(9262828, 1)
    store32(9262940, 14)
    store32(9262928, 425)
    store32(9262920, 0)
    store64(9262944, 141733920770)
    store32(9216056, (v0 + 356))
    store32(9263008, 0)
    store32(9262952, (v0 + 355))
    store8(9262960, 1)
    store8(9262963, 0)
    store32(9263052, 0)
    store32(9263060, 887)
    store32(9299860, 1024)
    v0 = func26(4096)
    store32(9299868, 1024)
    store32(9299856, v0)
    store32(9299864, 0)
    store32(9299876, 400)
    v0 = func26(1600)
    store32(9299884, 400)
    store32(9299872, v0)
    store32(9299880, 0)
    store32(9299892, 400)
    v0 = func26(1600)
    store32(9299900, 400)
    store32(9299888, v0)
    store32(9299896, 0)
    store32(9561040, load32(38604))
    store32(9561044, load32(38608))
    store32(9561048, load32(38612))
    store32(9561052, load32(38616))
    store32(9561056, load32(38624))
    store32(9561060, load32(38628))
    store32(9561064, load32(38632))
    store32(9561068, load32(39056))
    store32(9561700, 1)
    v0 = func26(4)
    store32(9561708, 2048)
    store32(9561696, v0)
    store32(9561704, 0)
    store32(9561772, 1)
    v0 = func26(4)
    store32(9561780, 4)
    store32(9561768, v0)
    store32(9561776, 0)
    store32(9561788, 1)
    v0 = func26(4)
    store32(9561796, 4)
    store32(9561784, v0)
    store32(9561792, 0)
    store32(9561812, 1000000)
    v0 = func26(4000000)
    store32(9561820, 1000000)
    store32(9561808, v0)
    store32(9561816, 0)
    store32(9568072, 0)
    store32(9568068, 0)
    store32(9568064, 0)
    store32(9671132, 4)
    v0 = func26(532)
    store32(func26(532), 4)
    v3 = (v0 + 4)
    # TODO: memory.fill
    v1 = func26(4)
    store32(v0 + 8, func26(4))
    store32(v0 + 4, v1)
    store32(v0 + 12, (v1 + 4))
    # TODO: memory.fill
    v1 = func26(4)
    store32(v0 + 140, func26(4))
    store32(v0 + 136, v1)
    store32(v0 + 144, (v1 + 4))
    # TODO: memory.fill
    v1 = func26(4)
    store32(v0 + 272, func26(4))
    store32(v0 + 268, v1)
    store32(v0 + 276, (v1 + 4))
    # TODO: memory.fill
    v1 = func26(4)
    store32(v0 + 404, func26(4))
    store32(v0 + 400, v1)
    store32(v0 + 408, (v1 + 4))
    store32(ENTITIES, v3)
    store64(9671136, 42949672960003)
    store32(9671172, 3)
    v0 = func26(12)
    store32(9671180, 30)
    store32(9671168, v0)
    store32(9671176, 0)
    store32(9671188, 4)
    v0 = func26(16)
    store32(9671196, 4)
    store32(9671184, v0)
    store32(9671192, 0)
    store32(9681452, 27)
    v0 = func26(108)
    store32(9681460, 1)
    store32(9681448, v0)
    store32(9681456, 0)
    store32(9681488, load32(38460))
    store32(9681492, load32(38732))
    store32(9681496, load32(38672))
    v0 = load32(38468)
    store32(9681500, load32(38468))
    v1 = load32(38668)
    store32(9681504, load32(38668))
    v3 = load32(38664)
    store32(9681508, load32(38664))
    v2 = load32(38476)
    store32(9681512, load32(38476))
    v4 = load32(38820)
    store32(9681516, load32(38820))
    v5 = load32(38700)
    store32(9681520, load32(38700))
    store32(9681524, load32(38512))
    store32(9681528, load32(38792))
    store32(9681532, load32(38868))
    store32(9681536, load32(38488))
    store32(9681540, load32(38848))
    store32(9681544, load32(38916))
    store32(9681548, load32(38464))
    store32(9681552, load32(38836))
    store32(9681556, load32(38904))
    store32(9681560, load32(38516))
    store32(9681564, load32(38844))
    store32(9681568, load32(38912))
    store32(9681572, load32(38484))
    store32(9681576, load32(38840))
    store32(9681580, load32(38908))
    store32(9681584, load32(38536))
    store32(9681588, load32(38804))
    store32(9681592, load32(38880))
    store32(9681596, load32(38540))
    store32(9681600, load32(38812))
    store32(9681604, load32(38888))
    store32(9681608, load32(38492))
    store32(9681612, load32(38788))
    store32(9681616, load32(38864))
    store32(9681620, load32(38556))
    store32(9681624, load32(38828))
    store32(9681628, load32(38900))
    store32(9681632, load32(38524))
    store32(9681636, load32(38800))
    store32(9681640, load32(38876))
    store32(9681644, load32(38532))
    store32(9681648, load32(38824))
    store32(9681652, load32(38896))
    store32(9681656, load32(38544))
    store32(9681660, load32(38780))
    store32(9681664, load32(38856))
    store32(9681668, load32(38480))
    store32(9681672, load32(38784))
    store32(9681676, load32(38860))
    store32(9681832, 1)
    v6 = func26(4)
    store32(9681840, 128)
    store32(9681828, v6)
    store32(9681836, 0)
    store32(9681880, v5)
    store32(9681876, v4)
    store32(9681872, v2)
    store32(9681868, v3)
    store32(9681864, v1)
    store32(9681860, v0)
    store64(9681924, 0)
    store32(9681932, 0)
    store32(9681856, load32(38832))
    store32(9681952, load32(38460))
    store32(9681956, load32(38732))
    store32(9681960, load32(38672))
    store32(9681964, load32(38468))
    store32(9681968, load32(38668))
    store32(9681972, load32(38664))
    store32(9682096, load32(57152))
    store32(9682100, load32(38496))
    store32(9682104, load32(38436))
    store32(9682108, load32(38444))
    store32(9682112, load32(38432))
    store32(9682116, load32(38424))
    store32(9682120, load32(38680))
    store32(9682124, load32(38684))
    store32(9682128, load32(38688))
    store32(9682132, load32(38696))
    store32(9682136, load32(38692))
    store32(9682140, load32(38704))
    store32(9682144, load32(38740))
    store32(9682148, load32(38736))
    store32(9682152, load32(38744))
    store32(9682156, load32(38756))
    store32(9682160, load32(38752))
    store32(9682164, load32(38760))
    store32(9682168, load32(38776))
    store32(9681984, load32(38944))
    store32(9681988, load32(39020))
    store32(9681992, load32(39036))
    store32(9681996, load32(39016))
    store32(9682000, load32(39012))
    store32(9682004, load32(39040))
    store32(9682008, load32(38948))
    store32(9682012, load32(38988))
    store32(9682016, load32(38992))
    store32(9682020, load32(39008))
    store32(9682024, load32(39032))
    store32(9682028, load32(39028))
    store32(9682032, load32(39052))
    store32(9682036, load32(39044))
    store32(9682040, load32(39000))
    store32(9682044, load32(39048))
    store32(9682048, load32(39024))
    store32(9682052, load32(39004))
    store32(9682064, load32(38972))
    store32(9682068, load32(38964))
    store32(9682072, load32(38980))
    store32(9682076, load32(38976))
    store32(9682080, load32(38968))
    store32(9682084, load32(38952))
    store32(9682088, load32(38956))
    store32(9682092, load32(38960))
    store32(9684448, 1)
    v0 = func26(4)
    store32(9684456, 32)
    store32(9684444, v0)
    store32(9684452, 0)
    store32(9684464, 1)
    v0 = func26(4)
    store32(9684472, 32)
    store32(9684460, v0)
    store32(9684468, 0)
    store32(9684480, 1)
    v0 = func26(4)
    store32(9684488, 32)
    store32(9684476, v0)
    store32(9684484, 0)
    store32(9684816, 1)
    v0 = func26(4)
    store32(9684824, 64)
    store32(9684812, v0)
    store32(9684820, 0)
    store32(9687192, load32(38544))
    store32(9687196, load32(38780))
    store32(9687200, load32(38856))

# ----------------------------------------------------------
# $L
# Export: L
# ----------------------------------------------------------
def L(arg0):
    """Export: L"""
    v2 = func26(arg0)
    while True:  # $label0
        if not arg0:
            break
        v4 = (arg0 & 3)
        if (u32(arg0) >= u32(4)):
            v5 = (arg0 & -4)
            arg0 = 0
            while True:  # $label1
                store8((v1 + v2), load32(((v1 << 2) + 9147392)))
                v3 = (v1 | 1)
                store8((v2 + (v1 | 1)), load32(((v3 << 2) + 9147392)))
                v3 = (v1 | 2)
                store8((v2 + (v1 | 2)), load32(((v3 << 2) + 9147392)))
                v3 = (v1 | 3)
                store8((v2 + (v1 | 3)), load32(((v3 << 2) + 9147392)))
                v1 = (v1 + 4)
                arg0 = (arg0 + 4)
                if ((arg0 + 4) != v5):
                    continue
                break
        if not v4:
            break
        while True:  # $label2
            store8((v1 + v2), load32(((v1 << 2) + 9147392)))
            v1 = (v1 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v4):
                continue
            break
        break
    return v2

# ----------------------------------------------------------
# $J
# Export: J
# ----------------------------------------------------------
def J(arg0):
    """Export: J"""
    v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
    if arg0:
        while True:  # $label0
            v1 = (v1 << 2)
            store32((v2 + (v1 << 2)), load32((v1 + 9147392)))
            v3 = (v3 + 1)
            v1 = ((v3 + 1) & 65535)
            if (u32(((v3 + 1) & 65535)) < u32(arg0)):
                continue
            break
    return v2

# ----------------------------------------------------------
# $K
# Export: K
# ----------------------------------------------------------
def K(arg0):
    """Export: K"""
    v2 = func26((-1 if (arg0 < 0) else (arg0 << 1)))
    while True:  # $label0
        if not arg0:
            break
        v4 = (arg0 & 3)
        if (u32(arg0) >= u32(4)):
            v5 = (arg0 & -4)
            arg0 = 0
            while True:  # $label1
                store16((v2 + (v1 << 1)), load32(((v1 << 2) + 9147392)))
                v3 = (v1 | 1)
                store16((v2 + ((v1 | 1) << 1)), load32(((v3 << 2) + 9147392)))
                v3 = (v1 | 2)
                store16((v2 + ((v1 | 2) << 1)), load32(((v3 << 2) + 9147392)))
                v3 = (v1 | 3)
                store16((v2 + ((v1 | 3) << 1)), load32(((v3 << 2) + 9147392)))
                v1 = (v1 + 4)
                arg0 = (arg0 + 4)
                if ((arg0 + 4) != v5):
                    continue
                break
        if not v4:
            break
        while True:  # $label2
            store16((v2 + (v1 << 1)), load32(((v1 << 2) + 9147392)))
            v1 = (v1 + 1)
            v6 = (v6 + 1)
            if ((v6 + 1) != v4):
                continue
            break
        break
    return v2

# ----------------------------------------------------------
# $T
# Export: T
# ----------------------------------------------------------
def T(arg0, arg1):
    """Export: T"""
    store32(players[arg0] + 284608, arg1)

# ----------------------------------------------------------
# $U
# Export: U
# ----------------------------------------------------------
def U(arg0):
    """Export: U"""
    arg0 = players[arg0]
    store16(players[arg0], load32(9147392))
    store16(arg0 + 2, load32(9147396))
    store16(arg0 + 4, load32(9147400))
    store16(arg0 + 6, load32(9147404))
    store16(arg0 + 8, load32(9147408))
    store16(arg0 + 10, load32(9147412))
    store16(arg0 + 12, load32(9147416))
    store16(arg0 + 14, load32(9147420))
    store16(arg0 + 16, load32(9147424))
    store16(arg0 + 18, load32(9147428))
    store16(arg0 + 20, load32(9147432))
    store16(arg0 + 22, load32(9147436))
    store16(arg0 + 24, load32(9147440))
    store16(arg0 + 26, load32(9147444))
    store16(arg0 + 28, load32(9147448))
    store16(arg0 + 30, load32(9147452))
    store16(arg0 + 32, load32(9147456))
    store16(arg0 + 34, load32(9147460))
    store16(arg0 + 36, load32(9147464))
    store16(arg0 + 38, load32(9147468))

# ----------------------------------------------------------
# $Ab
# Export: Ab
# ----------------------------------------------------------
def Ab(arg0, arg1):
    """Export: Ab"""
    arg0 = players[arg0]
    store8(players[arg0] + 283972, ((arg1 & 0xFFFFFFFF) >> 16))
    store8((arg0 + 283974), arg1)
    store8((arg0 + 283973), ((arg1 & 0xFFFFFFFF) >> 8))
    while True:  # $label2
        while True:  # $label0
            v4 = load32(((arg0 + (v3 << 2)) + 284636))
            if not load32(((arg0 + (v3 << 2)) + 284636)):
                break
            arg1 = 0
            v2 = load32(v4 + 8)
            if not load32(v4 + 8):
                break
            while True:  # $label1
                v5 = load32((load32(v4) + (arg1 << 2)))
                if load32((load32(v4) + (arg1 << 2))):
                    v2 = entities[v5]
                    v2 = load32(v4 + 8)
                arg1 = (arg1 + 1)
                if (u32((arg1 + 1)) < u32(v2)):
                    continue
                break
            break
        v3 = (v3 + 1)
        if ((v3 + 1) != 255):
            continue
        break

# ----------------------------------------------------------
# $Wb
# Export: Wb
# ----------------------------------------------------------
def Wb(arg0):
    """Export: Wb"""
    v3 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label0
        if load8u(9147210):
            break
        if (load32(9681888) >= 2):
            store32(9681892, arg0)
            store8(9681884, 1)
            store8(9681885, 0)
            break
        if load8u(9681884):
            v1 = load32(9142880)
            while True:  # $label1
                if load8u(9142916):
                    store32(v3 + 32, v1)
                    a_b()
                    break
                store32(v3 + 24, v1)
                store64(v3 + 16, -4602115869219225600)
                store64(v3 + 8, 0)
                store64(v3, 0)
                a_b()
                break
            store8(9681884, 0)
        while True:  # $label2
            if not load32(9671176):
                break
            if load32(9671192):
                v1 = 0
                while True:  # $label3
                    func38(load32((load32(9671184) + (v1 << 2))))
                    v1 = (v1 + 1)
                    if (u32((v1 + 1)) < u32(load32(9671192))):
                        continue
                    break
            store32(9671192, 0)
            store32(9671176, 0)
            store8(9142412, 0)
            if not load8u(9684396):
                break
            store8(9684396, 0)
            a_b()
            break
        v1 = load32(9671176)
        while True:  # $label4
            v2 = load32(9671172)
            if (u32(load32(9671172)) > u32((v1 + 3))):
                v2 = load32(9671168)
                break
            v2 = ((v2 + load32(9671180)) + 3)
            store32(9671172, ((v2 + load32(9671180)) + 3))
            v4 = load32(9671168)
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if v1:
                # TODO: memory.copy
            if v4:
                v1 = load32(9671176)
            store32(9671168, v2)
            break
        store32(9671176, (v1 + 1))
        store32((v2 + (v1 << 2)), arg0)
        arg0 = load32(9671176)
        store32(9671176, (load32(9671176) + 1))
        store32((v2 + (arg0 << 2)), 0)
        arg0 = load32(9671176)
        store32(9671176, (load32(9671176) + 1))
        store32((v2 + (arg0 << 2)), 0)
        store8(9142412, 1)
        break
    G.global0 = (v3 + 48)
    return af(v4)