"""
Tzar Engine - Core module (part 10).
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

from tzar.core.templates import (
    ENTITIES, PLAYERS, ENTITY_TYPES,
    EntityField, PlayerField, EntityTypeField,
    get_entity_ptr, get_player_ptr, get_entity_type_ptr,
    entity_hp, entity_state, entity_action, entity_owner,
    entity_x, entity_y, entity_type_id,
    iter_entities, iter_entity_ptrs,
)

# Known addresses
GAME_STATE = 9142424
CURRENT_PLAYER = 9142872
PLAYER_COUNT = 9142892
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
# $qc
# Export: qc
# ----------------------------------------------------------
def qc(arg0, arg1):
    """Export: qc"""
    if not load32(51776):
        store8(9215872, 1)
        while True:  # $label0
            v2 = load32(9216016)
            if (load32(9216016) != load32(9216012)):
                v3 = load32(9216008)
                break
            v3 = (load32(9216020) + v2)
            store32(9216012, (load32(9216020) + v2))
            v4 = load32(9216008)
            v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
            if v2:
                # TODO: memory.copy
            if v4:
                v2 = load32(9216016)
            store32(9216008, v3)
            break
        store32(9216016, (v2 + 1))
        store32((v3 + (v2 << 2)), arg0)
        while True:  # $label1
            arg0 = load32(9216016)
            if (load32(9216016) != load32(9216012)):
                v2 = v3
                break
            v2 = (load32(9216020) + arg0)
            store32(9216012, (load32(9216020) + arg0))
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(9216008, v2)
            arg0 = load32(9216016)
            break
        store32(9216016, (arg0 + 1))
        store32((v2 + (arg0 << 2)), arg1)
        return
    while True:  # $label2
        if arg1:
            arg1 = (arg0 + 9686896)
            if load8u((arg0 + 9686896)):
                break
            store8(arg1, 1)
            arg1 = load32(((arg0 << 2) + 9685872))
            if not load32(((arg0 << 2) + 9685872)):
                break
            return
        store8((arg0 + 9686896), 0)
        arg1 = load32(((arg0 << 2) + 9685872))
        if not load32(((arg0 << 2) + 9685872)):
            break
        break

# ----------------------------------------------------------
# $func343
# ----------------------------------------------------------
def func343():
    while True:  # $label0
        v0 = load32(9142440)
        # TODO: f32.demote_f64
        v9 = ((((i32((load32(9142440) * v0)) * 1.52587890625e-05) * i32((load32(load32(GAME_STATE) + 60) * 160))) / 40.0) + 0.5)
        if ((((((i32((load32(9142440) * v0)) * 1.52587890625e-05) * i32((load32(load32(GAME_STATE) + 60) * 160))) / 40.0) + 0.5) < 4294967300.0) & (v9 >= 0.0)):
            break
        break
    v7 = 0
    if 0:
        while True:  # $label3
            v2 = load32(9142440)
            while True:  # $label2
                v8 = load32(load32(GAME_STATE) + 64)
                if load32(load32(GAME_STATE) + 64):
                    v3 = load32(9147312)
                    v0 = load32(9147324)
                    v0 = ((load32(9147324) << 11) ^ v0)
                    v1 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v0)
                    v4 = ((v2 & 0xFFFFFFFF) >> 1)
                    v9 = i32(((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v0) & 0xFFFFFFFF) >> 8)) ^ v3) ^ v0) % (((v2 & 0xFFFFFFFF) >> 1) - 20)))
                    v5 = load32(9147320)
                    v2 = load32(9147316)
                    while True:  # $label1
                        v0 = load32(9142416)
                        if not load32(9142416):
                            v0 = (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))
                        v0 = ((v5 << 11) ^ v5)
                        v0 = (((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1)
                        v10 = (((6.28318548 / i32((4 if (u32(v0) < u32(3)) else (v0 << (v0 & 1))))) * i32(((((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1) % 100000))) / 100000.0)
                        # TODO: f64.promote_f32
                        v11 = i32(v4)
                        v12 = (((func48((((6.28318548 / i32((4 if (u32(v0) < u32(3)) else (v0 << (v0 & 1))))) * i32(((((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1) % 100000))) / 100000.0)) * v9) + 0.5) + i32(v4))
                        if (abs((((func48((((6.28318548 / i32((4 if (u32(v0) < u32(3)) else (v0 << (v0 & 1))))) * i32(((((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v0) ^ v1) % 100000))) / 100000.0)) * v9) + 0.5) + i32(v4))) < 2147483648.0):
                            break
                        break
                    v5 = -2147483648
                    # TODO: f64.promote_f32
                    v11 = (((func49(v10) * v9) + 0.5) + v11)
                    if (abs((((func49(v10) * v9) + 0.5) + v11)) < 2147483648.0):
                        v4 = i32(v11)
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

# ----------------------------------------------------------
# $func344
# ----------------------------------------------------------
def func344():
    v0 = load32(9561704)
    store32(9561716, load32(9561704))
    while True:  # $label0
        if (load32(9561700) != v0):
            v1 = load32(9561696)
            break
        v1 = (load32(9561708) + v0)
        store32(9561700, (load32(9561708) + v0))
        v2 = load32(9561696)
        v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
        if v0:
            # TODO: memory.copy
        if v2:
            v0 = load32(9561704)
        store32(9561696, v1)
        break
    store32(9561704, (v0 + 1))
    store32((v1 + (v0 << 2)), 0)
    v3 = (load32(9142848) + 10)
    store32(9561712, (load32(9142848) + 10))
    while True:  # $label1
        v0 = load32(9561704)
        if (load32(9561704) != load32(9561700)):
            v2 = v1
            break
        v2 = (load32(9561708) + v0)
        store32(9561700, (load32(9561708) + v0))
        v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
        if v0:
            # TODO: memory.copy
        store32(9561696, v2)
        v0 = load32(9561704)
        break
    store32(9561704, (v0 + 1))
    store32((v2 + (v0 << 2)), v3)
    while True:  # $label2
        v0 = load32(9561704)
        if (load32(9561704) != load32(9561700)):
            v1 = v2
            break
        v1 = (load32(9561708) + v0)
        store32(9561700, (load32(9561708) + v0))
        v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
        if v0:
            # TODO: memory.copy
        store32(9561696, v1)
        v0 = load32(9561704)
        break
    store32(9561704, (v0 + 1))
    store32((v1 + (v0 << 2)), 3)

# ----------------------------------------------------------
# $ac
# Export: ac
# ----------------------------------------------------------
def ac(arg0, arg1):
    """Export: ac"""
    func38(arg0)

# ----------------------------------------------------------
# $func346
# ----------------------------------------------------------
def func346():
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label0
        if not load8u(9216060):
            break
        if not load32(CURRENT_PLAYER):
            break
        if load8u(9142917):
            break
        while True:  # $label1
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v4 = load32(PLAYERS)
            v2 = 1
            while True:  # $label4
                v5 = (v4 + (v2 * 286704))
                store32((v4 + (v2 * 286704)) + 283944, 1)
                v3 = load32(PLAYER_COUNT)
                if (u32(load32(PLAYER_COUNT)) > u32(1)):
                    v8 = (v5 + 283944)
                    v7 = 1
                    v0 = 1
                    while True:  # $label3
                        while True:  # $label2
                            if (v0 == v2):
                                break
                            v6 = (v4 + (v0 * 286704))
                            if not load32((v4 + (v0 * 286704)) + 284616):
                                break
                            v6 = func88(v6)
                            v9 = func88(v5)
                            if (u32(func88(v6)) <= u32(func88(v5))):
                                if (v6 != v9):
                                    break
                                if (u32(v0) <= u32(v2)):
                                    break
                            v7 = (v7 + 1)
                            store32(v8, (v7 + 1))
                            v3 = load32(PLAYER_COUNT)
                            break
                        v0 = (v0 + 1)
                        if (u32((v0 + 1)) < u32(v3)):
                            continue
                        break
                v2 = (v2 + 1)
                if (u32((v2 + 1)) < u32(v3)):
                    continue
                break
            if (u32(v3) < u32(2)):
                break
            v4 = load32(PLAYERS)
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
                    v5 = load32(CURRENT_PLAYER)
                    store32(v1 + 32, ((load32(CURRENT_PLAYER) != 0) & (v3 == v5)))
                    store32(v1, v4)
                    store32(v1 + 4, v8)
                    store32(v1 + 8, v0)
                    store32(v1 + 12, v7)
                    a_b()
                    v4 = load32(PLAYERS)
                    v3 = load32(PLAYER_COUNT)
                v2 = (v2 + 1)
                if (u32((v2 + 1)) < u32(v3)):
                    continue
                break
            break
        a_b()
        break
    G.global0 = (v1 + 48)

# ----------------------------------------------------------
# $func347
# ----------------------------------------------------------
def func347(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    store32(59204, arg3)
    store32(59200, arg2)
    arg2 = 0
    v12 = 2
    while True:  # $label1
        while True:  # $label3
            arg3 = arg2
            arg2 = (arg2 + 2)
            arg3 = (arg3 << 2)
            v13 = load32(((arg3 << 2) + 59200))
            v14 = load32(((arg3 | 4) + 59200))
            arg3 = 0
            while True:  # $label2
                while True:  # $label0
                    v10 = (arg3 << 2)
                    v11 = (load32(((arg3 << 2) + 9072)) + v13)
                    v9 = ((load32(((arg3 << 2) + 9072)) + v13) - arg4)
                    v10 = (load32((v10 + 9104)) + v14)
                    v9 = ((load32((v10 + 9104)) + v14) - arg5)
                    if ((((((load32(((arg3 << 2) + 9072)) + v13) - arg4) * v9) + (((load32((v10 + 9104)) + v14) - arg5) * v9)) - 1) > 1600):
                        break
                    v9 = load32(9142440)
                    if (u32(load32(9142440)) <= u32(v10)):
                        break
                    if ((v10 | v11) < 0):
                        break
                    if (u32(v9) <= u32(v11)):
                        break
                    if (load16u((load32(9142436) + (((v9 * v10) + v11) << 1))) == arg8):
                        break
                    v9 = (v9 + 2)
                    v9 = load32((load32(9142840) + ((v11 + (((v10 + ((v9 + 2) * load32(arg7 + 208))) + 1) * v9)) << 2)) + 4)
                    if (u32(load32((load32(9142840) + ((v11 + (((v10 + ((v9 + 2) * load32(arg7 + 208))) + 1) * v9)) << 2)) + 4)) <= u32(2)):
                        if (load32(arg7 + 212) != v9):
                            break
                    if (u32(v9) >= u32(3)):
                        if func205(entities[v9], load16u(arg6 + 110)):
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
            if (u32(arg2) < u32(v12)):
                continue
            break
        return 0
        break
    store32(arg0, v11)
    store32(arg1, v10)
    return 1

# ----------------------------------------------------------
# $ve
# Export: ve
# ----------------------------------------------------------
def ve(arg0):
    """Export: ve"""
    v10 = load32(arg0 + 32)
    v4 = load32(arg0 + 12)
    store32(9140308, 0)
    v2 = (v4 + 16)
    v3 = load32(v4)
    while True:  # $label37
        while True:  # $label8
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
                    while True:  # $label0
                        if (v3 == 1):
                            arg0 = 0
                            break
                        v8 = (v3 & -2)
                        arg0 = 0
                        v1 = 0
                        while True:  # $label5
                            while True:  # $label2
                                while True:  # $label1
                                    v11 = ((v5 * 60) + v2)
                                    # br_table (load32(((v5 * 60) + v2) + 32) - 23)
                                    break
                                    break
                                arg0 = (arg0 + 1)
                                store32(9140324, (arg0 + 1))
                                break
                            while True:  # $label4
                                while True:  # $label3
                                    # br_table (load32(v11 + 92) - 23)
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
                    while True:  # $label6
                        if not v9:
                            break
                        while True:  # $label7
                            # br_table (load32((v2 + (v1 << 2))) - 23)
                            break
                            break
                        arg0 = (arg0 + 1)
                        store32(9140324, (arg0 + 1))
                        break
                else:
                store32((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)), func26(0))
                store32(9684504, (v4 + v6))
                store32(9684500, v2)
                store32(9687244, v3)
                store32(9147300, (((v10 - v6) & 0xFFFFFFFF) >> 2))
                store32(9140324, 0)
                if not v7:
                    break
                while True:  # $label9
                    if not v3:
                        break
                    arg0 = 0
                    if (v3 != 1):
                        v5 = (v3 & -2)
                        v1 = 0
                        while True:  # $label12
                            while True:  # $label10
                                v4 = (v2 + (arg0 * 60))
                                v10 = load32((v2 + (arg0 * 60)) + 28)
                                if (u32(load32((v2 + (arg0 * 60)) + 28)) > u32(9999)):
                                    break
                                v9 = load32(v4 + 32)
                                if (u32(load32(v4 + 32)) > u32(22)):
                                    break
                                if not ((1 << v9) & 4194400):
                                    break
                                store32(((v10 * 404) + ENTITY_TYPES) + 20, 0)
                                break
                            while True:  # $label11
                                v10 = load32(v4 + 88)
                                if (u32(load32(v4 + 88)) > u32(9999)):
                                    break
                                v4 = load32(v4 + 92)
                                if (u32(load32(v4 + 92)) > u32(22)):
                                    break
                                if not ((1 << v4) & 4194400):
                                    break
                                store32(((v10 * 404) + ENTITY_TYPES) + 20, 0)
                                break
                            arg0 = (arg0 + 2)
                            v1 = (v1 + 2)
                            if ((v1 + 2) != v5):
                                continue
                            break
                        arg0 = (arg0 * 15)
                    if not (v3 & 1):
                        break
                    arg0 = (v2 + (arg0 << 2))
                    v1 = load32((v2 + (arg0 << 2)) + 28)
                    if (u32(load32((v2 + (arg0 << 2)) + 28)) > u32(9999)):
                        break
                    arg0 = load32(arg0 + 32)
                    if (u32(load32(arg0 + 32)) > u32(22)):
                        break
                    if not ((1 << arg0) & 4194400):
                        break
                    store32(((v1 * 404) + ENTITY_TYPES) + 20, 0)
                    break
                v4 = 1
                while True:  # $label13
                    if load8u(59182):
                        break
                    v2 = load32(9671136)
                    if (u32(load32(9671136)) < u32(4)):
                        break
                    v5 = load32(ENTITIES)
                    arg0 = 3
                    while True:  # $label36
                        while True:  # $label14
                            v3 = (v5 + (arg0 * 132))
                            if (load8u((v5 + (arg0 * 132)) + 125) == 3):
                                break
                            v10 = load32(v3 + 48)
                            if not load32(v3 + 48):
                                break
                            v1 = load8u(v3 + 122)
                            while True:  # $label35
                                while True:  # $label34
                                    while True:  # $label33
                                        while True:  # $label32
                                            while True:  # $label31
                                                while True:  # $label30
                                                    while True:  # $label29
                                                        while True:  # $label28
                                                            while True:  # $label27
                                                                while True:  # $label26
                                                                    while True:  # $label25
                                                                        while True:  # $label24
                                                                            while True:  # $label23
                                                                                while True:  # $label22
                                                                                    while True:  # $label21
                                                                                        while True:  # $label20
                                                                                            while True:  # $label19
                                                                                                while True:  # $label18
                                                                                                    while True:  # $label17
                                                                                                        while True:  # $label16
                                                                                                            while True:  # $label15
                                                                                                                # br_table load32(v10 + 32)
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
        while True:  # $label38
            v5 = ((arg0 * 404) + ENTITY_TYPES)
            if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) != 2):
                break
            v1 = v2
            while True:  # $label39
                while True:  # $label40
                    # br_table load32(v5 + 268)
                    break
                    break
                v1 = v3
                break
            store32(((arg0 * 72) + 9263856), v1)
            break
        v5 = (arg0 | 1)
        if ((arg0 | 1) != 255):
            while True:  # $label41
                v7 = ((v5 * 404) + ENTITY_TYPES)
                if (load32(((v5 * 404) + ENTITY_TYPES) + 264) != 2):
                    break
                v1 = v2
                while True:  # $label42
                    while True:  # $label43
                        # br_table load32(v7 + 268)
                        break
                        break
                    v1 = v3
                    break
                store32(((v5 * 72) + 9263856), v1)
                break
            arg0 = (arg0 + 2)
            continue
        break
    if not (not v6 | v4):
        if load8u(9687269):
            v3 = 3
            if (u32(load32(9671136)) > u32(3)):
                while True:  # $label50
                    arg0 = entities[v3]
                    func157(entities[v3])
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
                    while True:  # $label45
                        if (load8u(arg0 + 126) != 1):
                            break
                        v1 = entities[load32(arg0 + 28)]
                        store8(entities[load32(arg0 + 28)] + 126, 0)
                        # TODO: i32.div_u
                        store32(load32(v1 + 52) + 52, ((load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 296) * load32((players[load16u(v1 + 110)] + 284144))) - 100))
                        if not load32(v1 + 92):
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
                    while True:  # $label46
                        if not load32(9147132):
                            break
                        if (load32(38788) != load8u(arg0 + 122)):
                            break
                        store32(arg0 + 84, (load32(arg0 + 84) + 1))
                        break
                    while True:  # $label49
                        while True:  # $label47
                            while True:  # $label48
                                # br_table (load8u(arg0 + 125) - 4)
                                break
                                break
                            v1 = load16u(arg0 + 110)
                            v2 = load8u(arg0 + 122)
                            v4 = load32(PLAYERS)
                            break
                            break
                        v4 = load32(PLAYERS)
                        v1 = load16u(arg0 + 110)
                        v2 = load8u(arg0 + 122)
                        arg0 = ((players[load16u(arg0 + 110)] + (load8u(arg0 + 122) << 2)) + 282828)
                        store32(((players[load16u(arg0 + 110)] + (load8u(arg0 + 122) << 2)) + 282828), (load32(arg0) + 1))
                        break
                    arg0 = (v4 + (v1 * 286704))
                    v2 = load32(((v2 * 404) + ENTITY_TYPES) + 280)
                    v1 = (load32(((v2 * 404) + ENTITY_TYPES) + 280) + load32(arg0 + 283976))
                    store32((v4 + (v1 * 286704)) + 283976, (load32(((v2 * 404) + ENTITY_TYPES) + 280) + load32(arg0 + 283976)))
                    if (v2 < 0):
                        store8(arg0 + 286700, 1)
                    arg0 = (arg0 + 281748)
                    if (u32(v1) > u32(load32((arg0 + 281748)))):
                        store32(arg0, v1)
                    v3 = (v3 + 1)
                    if (u32((v3 + 1)) < u32(load32(9671136))):
                        continue
                    break
        store8(9687268, 1)
        v2 = 0
        v10 = 0
        v13 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        while True:  # $label83
            v5 = ((v10 * 404) + ENTITY_TYPES)
            v17 = load32(((v10 * 404) + ENTITY_TYPES) + 224)
            arg0 = load32(v5 + 200)
            v18 = (load32(v5 + 200) if (u32(arg0) > u32(v2)) else v2)
            v19 = (load32(((v10 * 404) + ENTITY_TYPES) + 224) > (load32(v5 + 200) if (u32(arg0) > u32(v2)) else v2))
            v20 = load32(v5 + 216)
            if load32(v5 + 216):
                v21 = load32(v5 + 220)
                v4 = 0
                while True:  # $label51
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
                        while True:  # $label57
                            while True:  # $label53
                                while True:  # $label52
                                    if not v4:
                                        if not v23:
                                            break
                                        if not load8u(v2):
                                            break
                                        v4 = 0
                                        arg0 = 0
                                        break
                                    while True:  # $label54
                                        v12 = (v4 - 1)
                                        v14 = (u32((v4 - 1)) >= u32(v1))
                                        if (u32((v4 - 1)) >= u32(v1)):
                                            break
                                        if not v3:
                                            break
                                        if not load8u((v2 + v12)):
                                            break
                                        arg0 = 0
                                        break
                                        break
                                    v6 = (v4 - 2)
                                    while True:  # $label55
                                        v24 = (v4 == 1)
                                        if (v4 == 1):
                                            break
                                        if (u32(v1) <= u32(v6)):
                                            break
                                        if not v3:
                                            break
                                        if not load8u((v2 + v6)):
                                            break
                                        arg0 = 0
                                        break
                                        break
                                    while True:  # $label56
                                        v15 = (u32(v1) <= u32(v4))
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if not v3:
                                            break
                                        if not load8u((v2 + v4)):
                                            break
                                        arg0 = 0
                                        break
                                        break
                                    arg0 = 1
                                    if (v11 == 1):
                                        break
                                    while True:  # $label67
                                        v9 = (arg0 - 1)
                                        while True:  # $label59
                                            while True:  # $label58
                                                if v14:
                                                    break
                                                if (u32(v3) <= u32(v9)):
                                                    break
                                                if load8u((v2 + ((v1 * v9) + v12))):
                                                    break
                                                break
                                            while True:  # $label60
                                                if v15:
                                                    break
                                                if (u32(v3) <= u32(v9)):
                                                    break
                                                if load8u((v2 + ((v1 * v9) + v4))):
                                                    break
                                                break
                                            v8 = (arg0 - 2)
                                            while True:  # $label61
                                                v16 = (u32(arg0) < u32(2))
                                                if (u32(arg0) < u32(2)):
                                                    break
                                                if v14:
                                                    break
                                                if (u32(v3) <= u32(v8)):
                                                    break
                                                if load8u((v2 + ((v1 * v8) + v12))):
                                                    break
                                                break
                                            v7 = 0
                                            while True:  # $label62
                                                if v24:
                                                    break
                                                v7 = 1
                                                if (u32(v1) <= u32(v6)):
                                                    break
                                                if (u32(v3) <= u32(v9)):
                                                    break
                                                if load8u((v2 + ((v1 * v9) + v6))):
                                                    break
                                                break
                                            while True:  # $label63
                                                if v14:
                                                    break
                                                if (u32(arg0) >= u32(v3)):
                                                    break
                                                if load8u((v2 + ((arg0 * v1) + v12))):
                                                    break
                                                break
                                            while True:  # $label64
                                                if v16:
                                                    break
                                                while True:  # $label65
                                                    if v15:
                                                        break
                                                    if (u32(v3) <= u32(v8)):
                                                        break
                                                    if load8u((v2 + ((v1 * v8) + v4))):
                                                        break
                                                    break
                                                if (not v7 | v16):
                                                    break
                                                if (u32(v1) <= u32(v6)):
                                                    break
                                                if (u32(v3) <= u32(v8)):
                                                    break
                                                if load8u((v2 + ((v1 * v8) + v6))):
                                                    break
                                                break
                                            while True:  # $label66
                                                if not v7:
                                                    break
                                                if (u32(v1) <= u32(v6)):
                                                    break
                                                if (u32(arg0) >= u32(v3)):
                                                    break
                                                if load8u((v2 + ((arg0 * v1) + v6))):
                                                    break
                                                break
                                            if v15:
                                                break
                                            if (u32(arg0) >= u32(v3)):
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
                                    while True:  # $label71
                                        while True:  # $label69
                                            while True:  # $label68
                                                if not v1:
                                                    break
                                                v6 = (arg0 - 1)
                                                if (u32((arg0 - 1)) >= u32(v3)):
                                                    break
                                                if load8u((v2 + (v1 * v6))):
                                                    break
                                                break
                                            while True:  # $label70
                                                if (u32(arg0) < u32(2)):
                                                    break
                                                if not v1:
                                                    break
                                                v6 = (arg0 - 2)
                                                if (u32((arg0 - 2)) >= u32(v3)):
                                                    break
                                                if load8u((v2 + (v1 * v6))):
                                                    break
                                                break
                                            if not v1:
                                                break
                                            if (u32(arg0) >= u32(v3)):
                                                break
                                            if not load8u((v2 + (arg0 * v1))):
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
                    # TODO: memory.fill
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
                    while True:  # $label77
                        while True:  # $label78
                            if v4:
                                while True:  # $label74
                                    if not v8:
                                        break
                                    v4 = ((((v2 * v7) + v3) << 2) + 59200)
                                    if load32(((((v2 * v7) + v3) << 2) + 59200)):
                                        break
                                    if not func93(v3, v2, v5):
                                        break
                                    v8 = (v9 + (v6 << 2))
                                    store32((v9 + (v6 << 2)), v3)
                                    store32(v8 + 4, v2)
                                    store32(v4, 1)
                                    v6 = (v6 + 2)
                                    break
                                while True:  # $label75
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
                                    if not func93(arg0, v3, v5):
                                        break
                                    v12 = (v9 + (v6 << 2))
                                    store32((v9 + (v6 << 2)), arg0)
                                    store32(v12 + 4, v3)
                                    store32(v8, 1)
                                    v6 = (v6 + 2)
                                    break
                                while True:  # $label76
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
                                    if not func93(v3, v2, v5):
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
                            while True:  # $label79
                                if not v8:
                                    break
                                v8 = ((((v2 * v7) + v3) << 2) + 59200)
                                if load32(((((v2 * v7) + v3) << 2) + 59200)):
                                    break
                                if not func93(v3, v2, v5):
                                    break
                                arg0 = v3
                                break
                                break
                            while True:  # $label80
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
                                if not func93(arg0, v3, v5):
                                    break
                                v2 = v3
                                break
                                break
                            while True:  # $label81
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
                                if not func93(v3, v2, v5):
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
                            if not func93(arg0, v2, v5):
                                break
                            break
                        v3 = (v9 + (v6 << 2))
                        store32((v9 + (v6 << 2)), arg0)
                        store32(v3 + 4, v2)
                        store32(v8, 1)
                        v6 = (v6 + 2)
                        break
                    if (u32(v1) < u32(v6)):
                        continue
                    break
                store32(v5 + 60, v6)
            v2 = (v17 if v19 else v18)
            v10 = (v10 + 1)
            if ((v10 + 1) != 255):
                continue
            break
        arg0 = 0
        v25 = (i32((v2 + 5)) * 80)
        v1 = (-1 if i32(((v25 & 0xFFFFFFFF) >> 32)) else i32((i32((v2 + 5)) * 80)))
        v3 = func26((-1 if i32(((v25 & 0xFFFFFFFF) >> 32)) else i32((i32((v2 + 5)) * 80))))
        # TODO: memory.fill
        store32(9142836, v3)
        while True:  # $label84
            v1 = ((arg0 * 404) + ENTITY_TYPES)
            v3 = load32(((arg0 * 404) + ENTITY_TYPES) + 200)
            if load32(((arg0 * 404) + ENTITY_TYPES) + 200):
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
                while True:  # $label86
                    if not ((v1 != v9) & (v1 != v3)):
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
                        if (u32(v11) < u32(3)):
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
        while True:  # $label91
            if load8u(9147212):
                break
            if load8u(9147213):
                break
            if load8u(9147152):
                break
            arg0 = load32(load32(GAME_STATE) + 184)
            store32(9147312, load32(load32(GAME_STATE) + 184))
            store32(9147324, (arg0 ^ -1))
            store32(9147320, (arg0 ^ -1515870811))
            store32(9147316, (arg0 ^ 1515870810))
            Nb()
            break
    store32(9687252, (load32(9687252) + 1))
    return func350()

# ----------------------------------------------------------
# $func350
# ----------------------------------------------------------
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
                while True:  # $label0
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
                if (u32((v0 + 1)) < u32(v16)):
                    continue
                break
            v1 = v2
            if (u32(v2) < u32(v16)):
                continue
            break
    v11 = load32(GAME_STATE)
    v0 = load32(load32(GAME_STATE) + 164)
    if not load32(load32(GAME_STATE) + 164):
        store32(v11 + 164, 100)
        v0 = 100
    v1 = ((load32(38448) * 404) + ENTITY_TYPES)
    store32(((load32(38448) * 404) + ENTITY_TYPES) + 104, v0)
    store32(v1 + 108, load32(v11 + 164))
    v17 = (v16 * v16)
    v15 = load32(v11 + 116)
    while True:  # $label25
        while True:  # $label69
            while True:  # $label68
                while True:  # $label67
                    while True:  # $label63
                        while True:  # $label3
                            while True:  # $label4
                                if load32(v11 + 68):
                                    v0 = load32(PLAYER_COUNT)
                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                        break
                                    v1 = (v0 - 1)
                                    v4 = ((v0 - 1) & 3)
                                    v3 = 0
                                    v6 = load32(PLAYERS)
                                    if (u32((v0 - 2)) < u32(3)):
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
                                        v1 = (load32(v1 + 284608) if (u32(v1) > u32(v12)) else v12)
                                        v1 = (load32((v1 + 571312)) if (u32(v1) < u32(v10)) else (load32(v1 + 284608) if (u32(v1) > u32(v12)) else v12))
                                        v1 = (load32((v1 + 858016)) if (u32(v1) < u32(v8)) else (load32((v1 + 571312)) if (u32(v1) < u32(v10)) else (load32(v1 + 284608) if (u32(v1) > u32(v12)) else v12)))
                                        v12 = (load32(((v6 + (v2 * 286704)) + 1144720)) if (u32(v1) < u32(v7)) else (load32((v1 + 858016)) if (u32(v1) < u32(v8)) else (load32((v1 + 571312)) if (u32(v1) < u32(v10)) else (load32(v1 + 284608) if (u32(v1) > u32(v12)) else v12))))
                                        v2 = (v2 + 4)
                                        v9 = (v9 + 4)
                                        if ((v9 + 4) != v5):
                                            continue
                                        break
                                    break
                                while True:  # $label6
                                    if load32(v11 + 64):
                                        v7 = 1
                                        v33 = i32((((v16 & 0xFFFFFFFF) >> 1) - 37))
                                        v34 = ((i32((((v16 & 0xFFFFFFFF) >> 1) - 37)) * 3.14159274) * v33)
                                        v1 = load32(9142416)
                                        v0 = load32(PLAYER_COUNT)
                                        v2 = (load32(PLAYER_COUNT) - 1)
                                        v1 = (load32(9142416) if v1 else (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1)))
                                        v37 = i32((4 if (u32(v1) < u32(3)) else ((load32(9142416) if v1 else (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))) << (v1 & 1))))
                                        v33 = (v33 + -15.0)
                                        v36 = (6.28318548 / i32(v2))
                                        v38 = ((6.28318548 / i32(v2)) * 0.5)
                                        v9 = load8u(9147127)
                                        if (u32(v0) < u32(2)):
                                            break
                                        v2 = load32(PLAYERS)
                                        v6 = load32(PLAYERS)
                                        v11 = 1
                                        while True:  # $label14
                                            while True:  # $label7
                                                if v9:
                                                    if (load32((v6 + (v11 * 286704)) + 284608) != 1):
                                                        break
                                                while True:  # $label8
                                                    v35 = ((v36 * i32((v7 - 1))) + v38)
                                                    v39 = i32(((load32(9142440) & 0xFFFFFFFF) >> 1))
                                                    v40 = ((v33 * func48(((v36 * i32((v7 - 1))) + v38))) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))
                                                    if (abs(((v33 * func48(((v36 * i32((v7 - 1))) + v38))) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))) < 2147483650.0):
                                                        break
                                                    break
                                                v4 = -2147483648
                                                while True:  # $label10
                                                    while True:  # $label9
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
                                                            while True:  # $label11
                                                                v5 = (v0 - v4)
                                                                if ((v13 + ((v0 - v4) * v5)) > 625):
                                                                    break
                                                                v5 = load32(9142440)
                                                                if (u32(load32(9142440)) <= u32(v0)):
                                                                    break
                                                                if ((v0 | v1) < 0):
                                                                    break
                                                                if (u32(v1) >= u32(v5)):
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
                                                    v2 = load32(PLAYERS)
                                                    break
                                                v7 = (v7 + 1)
                                                v0 = (v6 + (v11 * 286704))
                                                store32((v6 + (v11 * 286704)) + 283900, v4)
                                                store32(v0 + 283896, v12)
                                                store32(v0 + 283876, v4)
                                                store32(v0 + 283872, v12)
                                                v0 = load32(PLAYER_COUNT)
                                                v6 = v2
                                                break
                                            v11 = (v11 + 1)
                                            if (u32((v11 + 1)) < u32(v0)):
                                                continue
                                            break
                                        break
                                    while True:  # $label24
                                        while True:  # $label15
                                            v20 = load32(v11 + 168)
                                            if not load32(v11 + 168):
                                                break
                                            while True:  # $label20
                                                while True:  # $label16
                                                    v2 = load32(PLAYER_COUNT)
                                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                        break
                                                    v0 = (v2 - 1)
                                                    v4 = ((v2 - 1) & 3)
                                                    v3 = 0
                                                    v6 = load32(PLAYERS)
                                                    while True:  # $label17
                                                        if (u32((v2 - 2)) < u32(3)):
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
                                                            v1 = (load32(v1 + 284608) if (u32(v1) > u32(v8)) else v8)
                                                            v1 = (load32((v1 + 571312)) if (u32(v1) < u32(v11)) else (load32(v1 + 284608) if (u32(v1) > u32(v8)) else v8))
                                                            v1 = (load32((v1 + 858016)) if (u32(v1) < u32(v5)) else (load32((v1 + 571312)) if (u32(v1) < u32(v11)) else (load32(v1 + 284608) if (u32(v1) > u32(v8)) else v8)))
                                                            v8 = (load32(((v6 + (v0 * 286704)) + 1144720)) if (u32(v1) < u32(v9)) else (load32((v1 + 858016)) if (u32(v1) < u32(v5)) else (load32((v1 + 571312)) if (u32(v1) < u32(v11)) else (load32(v1 + 284608) if (u32(v1) > u32(v8)) else v8))))
                                                            v0 = (v0 + 4)
                                                            v10 = (v10 + 4)
                                                            if ((v10 + 4) != v12):
                                                                continue
                                                            break
                                                        break
                                                    if v4:
                                                        while True:  # $label19
                                                            v1 = load32((v6 + (v0 * 286704)) + 284608)
                                                            v8 = (load32((v6 + (v0 * 286704)) + 284608) if (u32(v1) > u32(v8)) else v8)
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
                                                # TODO: memory.fill
                                                store32(9142416, 0)
                                                v3 = load32(PLAYERS)
                                                v0 = 0
                                                v9 = 0
                                                while True:  # $label23
                                                    v1 = v0
                                                    v0 = 1
                                                    while True:  # $label21
                                                        if (u32(v2) <= u32(1)):
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
                                            if not v20:
                                                break
                                            if load8u(9147127):
                                                break
                                            break
                                        v7 = load32(PLAYER_COUNT)
                                        if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                            break
                                        v14 = load32(9142416)
                                        v12 = load32(9147316)
                                        v0 = load32(9147320)
                                        v5 = load32(9147312)
                                        v2 = load32(9147324)
                                        v10 = load32(PLAYERS)
                                        v6 = v16
                                        v3 = 1
                                        while True:  # $label38
                                            while True:  # $label31
                                                while True:  # $label28
                                                    if v20:
                                                        v1 = ((v6 & 0xFFFFFFFF) >> 1)
                                                        v13 = (((v6 & 0xFFFFFFFF) >> 1) - 35)
                                                        v34 = (6.28318548 / i32(v14))
                                                        v36 = ((6.28318548 / i32(v14)) + -0.122173049)
                                                        v19 = ((v10 + (v3 * 286704)) + 284608)
                                                        v33 = i32(v1)
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
                                                            while True:  # $label26
                                                                v38 = i32(((v5 % v13) + 22))
                                                                # TODO: f64.promote_f32
                                                                # TODO: f64.promote_f32
                                                                # TODO: f32.demote_f64
                                                                v37 = (((v36 * i32((v12 % 360))) / 360.0) + ((v34 * i32(load32(((v9 << 2) + 59200)))) + 0.122173049))
                                                                v35 = ((i32(((v5 % v13) + 22)) * func48((((v36 * i32((v12 % 360))) / 360.0) + ((v34 * i32(load32(((v9 << 2) + 59200)))) + 0.122173049)))) + v33)
                                                                if (abs(((i32(((v5 % v13) + 22)) * func48((((v36 * i32((v12 % 360))) / 360.0) + ((v34 * i32(load32(((v9 << 2) + 59200)))) + 0.122173049)))) + v33)) < 2147483650.0):
                                                                    break
                                                                break
                                                            v8 = -2147483648
                                                            while True:  # $label27
                                                                v38 = ((v38 * func49(v37)) + v33)
                                                                if (abs(((v38 * func49(v37)) + v33)) < 2147483650.0):
                                                                    break
                                                                break
                                                            v9 = -2147483648
                                                            if (u32(v3) < u32(2)):
                                                                break
                                                            v0 = ((-15 if (u32(v4) > u32(55)) else 0) + v15)
                                                            v2 = (((-15 if (u32(v4) > u32(55)) else 0) + v15) * v0)
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
                                                    if (u32(v3) >= u32(2)):
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
                                                            v0 = ((-15 if (u32(v13) > u32(55)) else 0) + v15)
                                                            v2 = (((-15 if (u32(v13) > u32(55)) else 0) + v15) * v0)
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
                                                v12 = load32(PLAYERS)
                                                while True:  # $label34
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
                                                            while True:  # $label35
                                                                v6 = (v0 - v8)
                                                                if ((v7 + ((v0 - v8) * v6)) > 625):
                                                                    break
                                                                v6 = load32(9142440)
                                                                if (u32(load32(9142440)) <= u32(v0)):
                                                                    break
                                                                if ((v0 | v1) < 0):
                                                                    break
                                                                if (u32(v1) >= u32(v6)):
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
                                                v7 = load32(PLAYER_COUNT)
                                                v6 = load32(9142440)
                                                v14 = load32(9142416)
                                                v12 = load32(9147316)
                                                v0 = load32(9147320)
                                                v5 = load32(9147312)
                                                v2 = load32(9147324)
                                                v10 = load32(PLAYERS)
                                                break
                                            v3 = (v3 + 1)
                                            if (u32((v3 + 1)) < u32(v7)):
                                                continue
                                            break
                                        break
                                        break
                                    # TODO: i32.div_u
                                    v10 = 90
                                    # TODO: i32.div_u
                                    v19 = 90
                                    v12 = (((load32(PLAYER_COUNT) - 1) & 0xFFFFFFFF) >> 1)
                                    # TODO: i32.div_u
                                    v0 = v10
                                    v24 = (v10 + (v12 != (v0 * v10)))
                                    if not (v10 + (v12 != (v0 * v10))):
                                        break
                                    v25 = (((v16 & 0xFFFFFFFF) >> 1) - 82)
                                    v26 = (0 - v19)
                                    v27 = ((v19 & 0xFFFFFFFF) >> 1)
                                    v3 = v12
                                    v4 = 0
                                    v15 = 0
                                    while True:  # $label52
                                        v0 = (v12 - (v10 * v15))
                                        v0 = ((v12 - (v10 * v15)) if (u32(v0) < u32(v10)) else v10)
                                        if ((v12 - (v10 * v15)) if (u32(v0) < u32(v10)) else v10):
                                            v28 = (v3 if (u32(v3) < u32(v10)) else v10)
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
                                                while True:  # $label39
                                                    v1 = load32(PLAYER_COUNT)
                                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                        break
                                                    v0 = 1
                                                    v7 = (v1 - 1)
                                                    v8 = ((v1 - 1) & 1)
                                                    v6 = load32(PLAYERS)
                                                    if (v1 != 2):
                                                        v14 = (v7 & -2)
                                                        v1 = 0
                                                        while True:  # $label40
                                                            v7 = (v6 + (v0 * 286704))
                                                            if (load32((v6 + (v0 * 286704)) + 284608) == 1):
                                                                v7 = load32(v7 + 284620)
                                                                v7 = ((u32(v2) < u32(v7)) & (u32(v4) > u32(v7)))
                                                                v4 = (load32(v7 + 284620) if ((u32(v2) < u32(v7)) & (u32(v4) > u32(v7))) else v4)
                                                                v5 = (v0 if v7 else v5)
                                                            v18 = (v0 + 1)
                                                            v7 = (v6 + ((v0 + 1) * 286704))
                                                            if (load32((v6 + ((v0 + 1) * 286704)) + 284608) == 1):
                                                                v7 = load32(v7 + 284620)
                                                                v7 = ((u32(v2) < u32(v7)) & (u32(v4) > u32(v7)))
                                                                v4 = (load32(v7 + 284620) if ((u32(v2) < u32(v7)) & (u32(v4) > u32(v7))) else v4)
                                                                v5 = (v18 if v7 else v5)
                                                            v0 = (v0 + 2)
                                                            v1 = (v1 + 2)
                                                            if ((v1 + 2) != v14):
                                                                continue
                                                            break
                                                    if not v8:
                                                        break
                                                    v1 = (v6 + (v0 * 286704))
                                                    if (load32((v6 + (v0 * 286704)) + 284608) != 1):
                                                        break
                                                    v1 = load32(v1 + 284620)
                                                    v1 = ((u32(v1) < u32(v4)) & (u32(v1) > u32(v2)))
                                                    v4 = (load32(v1 + 284620) if ((u32(v1) < u32(v4)) & (u32(v1) > u32(v2))) else v4)
                                                    v5 = (v0 if v1 else v5)
                                                    break
                                                v20 = (v20 + 1)
                                                v8 = ((((load32(9142440) & 0xFFFFFFFF) >> 1) - v29) + ((v19 if (v20 & 1) else v26) * (((v20 + 1) & 0xFFFFFFFF) >> 1)))
                                                v7 = load32(PLAYERS)
                                                while True:  # $label41
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
                                                            while True:  # $label42
                                                                v6 = (v0 - v13)
                                                                if ((v18 + ((v0 - v13) * v6)) > 625):
                                                                    break
                                                                v6 = load32(9142440)
                                                                if (u32(load32(9142440)) <= u32(v0)):
                                                                    break
                                                                if ((v0 | v1) < 0):
                                                                    break
                                                                if (u32(v1) >= u32(v6)):
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
                                                v14 = load32(PLAYERS)
                                                v7 = -1
                                                while True:  # $label45
                                                    v1 = load32(PLAYER_COUNT)
                                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
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
                                                                v1 = ((u32(v1) < u32(v7)) & (u32(v1) > u32(v9)))
                                                                v7 = (load32(v1 + 284620) if ((u32(v1) < u32(v7)) & (u32(v1) > u32(v9))) else v7)
                                                                v6 = (v0 if v1 else v6)
                                                            v22 = (v0 + 1)
                                                            v1 = (v14 + ((v0 + 1) * 286704))
                                                            if (load32((v14 + ((v0 + 1) * 286704)) + 284608) == 2):
                                                                v1 = load32(v1 + 284620)
                                                                v1 = ((u32(v1) < u32(v7)) & (u32(v1) > u32(v9)))
                                                                v7 = (load32(v1 + 284620) if ((u32(v1) < u32(v7)) & (u32(v1) > u32(v9))) else v7)
                                                                v6 = (v22 if v1 else v6)
                                                            v0 = (v0 + 2)
                                                            v2 = (v2 + 2)
                                                            if ((v2 + 2) != v18):
                                                                continue
                                                            break
                                                    if not v5:
                                                        break
                                                    v1 = (v14 + (v0 * 286704))
                                                    if (load32((v14 + (v0 * 286704)) + 284608) != 2):
                                                        break
                                                    v1 = load32(v1 + 284620)
                                                    v1 = ((u32(v1) < u32(v7)) & (u32(v1) > u32(v9)))
                                                    v7 = (load32(v1 + 284620) if ((u32(v1) < u32(v7)) & (u32(v1) > u32(v9))) else v7)
                                                    v6 = (v0 if v1 else v6)
                                                    break
                                                v5 = (load32(9142440) - v13)
                                                while True:  # $label47
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
                                                            while True:  # $label48
                                                                v18 = (v0 - v5)
                                                                if ((v30 + ((v0 - v5) * v18)) > 625):
                                                                    break
                                                                v18 = load32(9142440)
                                                                if (u32(load32(9142440)) <= u32(v0)):
                                                                    break
                                                                if ((v0 | v1) < 0):
                                                                    break
                                                                if (u32(v1) >= u32(v18)):
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
                                while True:  # $label53
                                    if not v9:
                                        break
                                    if (u32(v0) < u32(2)):
                                        break
                                    v2 = load32(PLAYERS)
                                    v6 = load32(PLAYERS)
                                    v11 = 1
                                    while True:  # $label61
                                        while True:  # $label54
                                            if v9:
                                                if (load32((v6 + (v11 * 286704)) + 284608) != 2):
                                                    break
                                            while True:  # $label55
                                                v37 = ((v36 * i32((v7 - 1))) + v38)
                                                v35 = i32(((load32(9142440) & 0xFFFFFFFF) >> 1))
                                                v39 = ((v33 * func48(((v36 * i32((v7 - 1))) + v38))) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))
                                                if (abs(((v33 * func48(((v36 * i32((v7 - 1))) + v38))) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))) < 2147483650.0):
                                                    break
                                                break
                                            v4 = -2147483648
                                            while True:  # $label57
                                                while True:  # $label56
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
                                                        while True:  # $label58
                                                            v5 = (v0 - v4)
                                                            if ((v13 + ((v0 - v4) * v5)) > 625):
                                                                break
                                                            v5 = load32(9142440)
                                                            if (u32(load32(9142440)) <= u32(v0)):
                                                                break
                                                            if ((v0 | v1) < 0):
                                                                break
                                                            if (u32(v1) >= u32(v5)):
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
                                                v2 = load32(PLAYERS)
                                                break
                                            v7 = (v7 + 1)
                                            v0 = (v6 + (v11 * 286704))
                                            store32((v6 + (v11 * 286704)) + 283900, v4)
                                            store32(v0 + 283896, v12)
                                            store32(v0 + 283876, v4)
                                            store32(v0 + 283872, v12)
                                            v0 = load32(PLAYER_COUNT)
                                            v6 = v2
                                            break
                                        v11 = (v11 + 1)
                                        if (u32((v11 + 1)) < u32(v0)):
                                            continue
                                        break
                                    break
                                if ((v34 < 4294967300.0) & (v34 >= 0.0)):
                                    v17 = i32(v34)
                                    break
                                v17 = 0
                                break
                                break
                            if v4:
                                while True:  # $label62
                                    v1 = load32((v6 + (v2 * 286704)) + 284608)
                                    v12 = (load32((v6 + (v2 * 286704)) + 284608) if (u32(v1) > u32(v12)) else v12)
                                    v2 = (v2 + 1)
                                    v3 = (v3 + 1)
                                    if ((v3 + 1) != v4):
                                        continue
                                    break
                            v6 = -1
                            if (v12 == -1):
                                break
                            break
                        # TODO: memory.fill
                        store32(9142416, 0)
                        v3 = load32(PLAYERS)
                        v2 = 0
                        v4 = 0
                        while True:  # $label66
                            v1 = v2
                            v2 = 1
                            while True:  # $label64
                                if (u32(v0) <= u32(1)):
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
                    if not load32(v11 + 64):
                        break
                    break
                    break
                if not load32(v11 + 64):
                    break
                v1 = (v0 - 1)
                v10 = ((v0 - 1) & -4)
                v7 = (v1 & 3)
                v5 = 0
                v8 = load32(PLAYERS)
                v13 = (u32((v0 - 2)) > u32(2))
                v1 = 0
                while True:  # $label73
                    if load32(((v1 << 2) + 59200)):
                        v3 = 0
                        while True:  # $label70
                            if (u32(v0) < u32(2)):
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
                            if not v7:
                                break
                            while True:  # $label72
                                v3 = (v3 + (load32((v8 + (v2 * 286704)) + 284608) == v1))
                                v2 = (v2 + 1)
                                v9 = (v9 + 1)
                                if ((v9 + 1) != v7):
                                    continue
                                break
                            break
                        v5 = (v3 if (u32(v3) > u32(v5)) else v5)
                    v2 = (v1 == v12)
                    v1 = (v1 + 1)
                    if not v2:
                        continue
                    break
                v1 = 0
                v6 = v12
                break
            while True:  # $label74
                v2 = v4
                if not v4:
                    v2 = (load32(41092) if load8u(9147210) else (v0 - 1))
                # TODO: f64.promote_f32
                # TODO: f32.demote_f64
                v33 = ((i32(((v16 & 0xFFFFFFFF) >> 1)) + (((20.0 if (u32(v5) < u32(5)) else 14.0) * i32(v5)) / -6.2831854820251465)) + -8.0)
                v34 = ((((i32(((v16 & 0xFFFFFFFF) >> 1)) + (((20.0 if (u32(v5) < u32(5)) else 14.0) * i32(v5)) / -6.2831854820251465)) + -8.0) * (v33 * 3.14159274)) / i32((4 if (u32(v2) < u32(3)) else (v2 << (v2 & 1)))))
                if ((((((i32(((v16 & 0xFFFFFFFF) >> 1)) + (((20.0 if (u32(v5) < u32(5)) else 14.0) * i32(v5)) / -6.2831854820251465)) + -8.0) * (v33 * 3.14159274)) / i32((4 if (u32(v2) < u32(3)) else (v2 << (v2 & 1))))) < 4294967300.0) & (v34 >= 0.0)):
                    break
                break
            v17 = 0
            if v1:
                break
            v38 = (6.28318548 / i32(v4))
            v37 = ((6.28318548 / i32(v4)) * 0.5)
            v12 = 0
            v7 = 0
            while True:  # $label88
                if load32(((v7 << 2) + 59200)):
                    while True:  # $label78
                        while True:  # $label75
                            if (u32(v0) < u32(2)):
                                v34 = 0.0
                                v41 = 0.0
                                break
                            v3 = (v0 - 1)
                            v4 = ((v0 - 1) & 3)
                            v8 = 0
                            v9 = load32(PLAYERS)
                            v2 = 1
                            v1 = 0
                            if (u32((v0 - 2)) >= u32(3)):
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
                            v34 = i32(v1)
                            # TODO: f64.promote_f32
                            v41 = i32(v1)
                            if (u32(v1) > u32(4)):
                                break
                            break
                        break
                    v42 = 20.0
                    if (u32(v0) >= u32(2)):
                        v13 = 0
                        v11 = 1
                        v34 = (6.28318548 / v34)
                        # TODO: f32.demote_f64
                        v36 = ((v42 * v41) / 6.2831854820251465)
                        while True:  # $label79
                            v35 = ((v38 * i32(v12)) + v37)
                            # TODO: f64.promote_f32
                            v41 = i32(((load32(9142440) & 0xFFFFFFFF) >> 1))
                            v42 = (((v33 * func48(((v38 * i32(v12)) + v37))) + 0.5) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))
                            if (abs((((v33 * func48(((v38 * i32(v12)) + v37))) + 0.5) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))) < 2147483648.0):
                                break
                            break
                        v42 = i32(-2147483648)
                        while True:  # $label80
                            # TODO: f64.promote_f32
                            v41 = (((v33 * func49(v35)) + 0.5) + v41)
                            if (abs((((v33 * func49(v35)) + 0.5) + v41)) < 2147483648.0):
                                break
                            break
                        v41 = i32(-2147483648)
                        v35 = (v34 * 0.5)
                        v2 = load32(PLAYERS)
                        while True:  # $label87
                            v9 = (v2 + (v11 * 286704))
                            if (v7 == load32((v2 + (v11 * 286704)) + 284608)):
                                while True:  # $label81
                                    v39 = ((v34 * i32(v13)) + v35)
                                    # TODO: f64.promote_f32
                                    v43 = (((func48(((v34 * i32(v13)) + v35)) * v36) + 0.5) + v42)
                                    if (abs((((func48(((v34 * i32(v13)) + v35)) * v36) + 0.5) + v42)) < 2147483648.0):
                                        break
                                    break
                                v4 = -2147483648
                                while True:  # $label83
                                    while True:  # $label82
                                        # TODO: f64.promote_f32
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
                                            while True:  # $label84
                                                v8 = (v0 - v4)
                                                if ((v20 + ((v0 - v4) * v8)) > 625):
                                                    break
                                                v8 = load32(9142440)
                                                if (u32(load32(9142440)) <= u32(v0)):
                                                    break
                                                if ((v0 | v1) < 0):
                                                    break
                                                if (u32(v1) >= u32(v8)):
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
                                    v2 = load32(PLAYERS)
                                    break
                                store32(v9 + 283900, v4)
                                store32(v9 + 283896, v5)
                                store32(v9 + 283876, v4)
                                store32(v9 + 283872, v5)
                                v13 = (v13 + 1)
                                v0 = load32(PLAYER_COUNT)
                            v11 = (v11 + 1)
                            if (u32((v11 + 1)) < u32(v0)):
                                continue
                            break
                    v12 = (v12 + 1)
                v1 = (v6 == v7)
                v7 = (v7 + 1)
                if not v1:
                    continue
                break
            break
            break
        v20 = (v15 * v15)
        v2 = 0
        while True:  # $label106
            while True:  # $label89
                v7 = v2
                if not load32(((v2 << 2) + 59200)):
                    break
                v2 = load32(PLAYERS)
                while True:  # $label94
                    while True:  # $label93
                        while True:  # $label90
                            if (u32(v0) < u32(2)):
                                v33 = 0.0
                                v41 = 0.0
                                break
                            v4 = (v0 - 1)
                            v6 = ((v0 - 1) & 3)
                            v1 = 1
                            v9 = 0
                            v3 = 0
                            if (u32((v0 - 2)) >= u32(3)):
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
                            v33 = i32(v3)
                            # TODO: f64.promote_f32
                            v41 = i32(v3)
                            if (u32(v3) > u32(4)):
                                break
                            break
                        break
                    # TODO: f32.demote_f64
                    v34 = ((20.0 * v41) / 6.2831854820251465)
                    v36 = (((20.0 * v41) / 6.2831854820251465) + 8.0)
                    if (abs((((20.0 * v41) / 6.2831854820251465) + 8.0)) < 2147483650.0):
                        break
                    break
                v1 = -2147483648
                v13 = -2147483633
                v6 = 0
                v15 = ((load32(9142440) - v1) - 30)
                v4 = load32(9147316)
                v1 = load32(9147320)
                v11 = load32(9147312)
                v3 = load32(9147324)
                while True:  # $label98
                    if (u32(v0) >= u32(2)):
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
                                while True:  # $label95
                                    v3 = (v2 + (v1 * 286704))
                                    v14 = load32((v2 + (v1 * 286704)) + 283872)
                                    if not load32((v2 + (v1 * 286704)) + 283872):
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
                        raise Unreachable()
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
                if (u32(v0) < u32(2)):
                    break
                v33 = (6.28318548 / v33)
                v36 = ((6.28318548 / v33) * 0.5)
                v41 = i32(v9)
                v42 = i32(v10)
                v11 = 1
                v13 = 0
                while True:  # $label105
                    v6 = (v2 + (v11 * 286704))
                    if (v7 == load32((v2 + (v11 * 286704)) + 284608)):
                        while True:  # $label99
                            v38 = ((v33 * i32(v13)) + v36)
                            # TODO: f64.promote_f32
                            v43 = (((func48(((v33 * i32(v13)) + v36)) * v34) + 0.5) + v41)
                            if (abs((((func48(((v33 * i32(v13)) + v36)) * v34) + 0.5) + v41)) < 2147483648.0):
                                break
                            break
                        v4 = -2147483648
                        while True:  # $label101
                            while True:  # $label100
                                # TODO: f64.promote_f32
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
                                    while True:  # $label102
                                        v5 = (v0 - v4)
                                        if ((v15 + ((v0 - v4) * v5)) > 625):
                                            break
                                        v5 = load32(9142440)
                                        if (u32(load32(9142440)) <= u32(v0)):
                                            break
                                        if ((v0 | v1) < 0):
                                            break
                                        if (u32(v1) >= u32(v5)):
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
                        v2 = load32(PLAYERS)
                        v0 = load32(PLAYER_COUNT)
                    v11 = (v11 + 1)
                    if (u32((v11 + 1)) < u32(v0)):
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
                while True:  # $label107
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
                if (u32(v0) < u32(v2)):
                    continue
                break
            v3 = v4
            if (u32(v4) < u32(v2)):
                continue
            break
    v0 = 1
    if (u32(load32(PLAYER_COUNT)) > u32(1)):
        while True:  # $label110
            v1 = players[v0]
            if not load32(v1 + 284624):
            v0 = (v0 + 1)
            if (u32((v0 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
    v0 = 47
    v8 = load32(9142428)
    if (u32(load32(9142428)) > u32(47)):
        v36 = (i32(v17) * 1.52587891e-05)
        while True:  # $label145
            v13 = (load32(GAME_STATE) + (v0 << 2))
            v26 = load32((load32(GAME_STATE) + (v0 << 2)) + 16)
            v27 = ((v0 + 7) if load32((load32(GAME_STATE) + (v0 << 2)) + 16) else v0)
            while True:  # $label111
                v0 = load32(v13 + 4)
                if (load32(v13 + 4) == 1):
                    break
                v6 = load32(v13 + 8)
                while True:  # $label112
                    v1 = load32(v13)
                    # TODO: f64.promote_f32
                    v2 = load32(v13 + 12)
                    v41 = (((v36 * i32(load32(v13))) + 0.5) if load32(v13 + 12) else i32(v1))
                    if (((((v36 * i32(load32(v13))) + 0.5) if load32(v13 + 12) else i32(v1)) < 4294967296.0) & (v41 >= 0.0)):
                        break
                    break
                v1 = 0
                v28 = ((0 if v1 else 1) if v2 else v1)
                if not ((0 if v1 else 1) if v2 else v1):
                    break
                v11 = (2147483647 if (v0 == 2) else v0)
                v12 = 0
                while True:  # $label144
                    v0 = 0
                    while True:  # $label139
                        v1 = 0
                        while True:  # $label113
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
                        while True:  # $label114
                            if not load32(load32(GAME_STATE) + 64):
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
                            if not v1:
                                v2 = (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))
                            v33 = (6.28318548 / i32((4 if (u32(v2) < u32(3)) else (v2 << (v2 & 1)))))
                            v9 = load32(9147312)
                            v2 = load32(9147324)
                            v2 = ((load32(9147324) << 11) ^ v2)
                            v4 = (((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v9) ^ v2)
                            v7 = ((((((load32(9147312) & 0xFFFFFFFF) >> 19) ^ ((((load32(9147324) << 11) ^ v2) & 0xFFFFFFFF) >> 8)) ^ v9) ^ v2) % ((load32(9142440) & 0xFFFFFFFF) >> 1))
                            v8 = load32(9147316)
                            v5 = load32(9147320)
                            v2 = v1
                            if not v1:
                                v2 = (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))
                            v34 = i32(v7)
                            store32(9147320, v9)
                            store32(9147324, v8)
                            store32(9147316, v4)
                            v9 = ((v5 << 11) ^ v5)
                            v4 = (((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v9) ^ v4)
                            store32(9147312, (((((((v5 << 11) ^ v5) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v9) ^ v4))
                            v38 = (((6.28318548 / i32((4 if (u32(v2) < u32(3)) else (v2 << (v2 & 1))))) * i32((v4 % 100000))) / 100000.0)
                            v37 = (v33 - (((6.28318548 / i32((4 if (u32(v2) < u32(3)) else (v2 << (v2 & 1))))) * i32((v4 % 100000))) / 100000.0))
                            v10 = ((v6 * 404) + ENTITY_TYPES)
                            v29 = (v3 & 255)
                            while True:  # $label138
                                if not v1:
                                    v1 = (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))
                                if (u32((4 if (u32(v1) < u32(3)) else (v1 << (v1 & 1)))) > u32(v15)):
                                    v35 = ((v33 * i32(v15)) + (v37 if (v15 & 1) else v38))
                                    v39 = func48(((v33 * i32(v15)) + (v37 if (v15 & 1) else v38)))
                                    while True:  # $label115
                                        # TODO: f64.promote_f32
                                        v41 = i32(((load32(9142440) & 0xFFFFFFFF) >> 1))
                                        v42 = (((0.5 - (i32(load32(v10 + 220)) * 0.5)) + (v39 * v34)) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))
                                        if (abs((((0.5 - (i32(load32(v10 + 220)) * 0.5)) + (v39 * v34)) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))) < 2147483648.0):
                                            break
                                        break
                                    v9 = -2147483648
                                    v35 = func49(v35)
                                    while True:  # $label123
                                        while True:  # $label116
                                            # TODO: f64.promote_f32
                                            v41 = (((0.5 - (i32(load32(v10 + 216)) * 0.5)) + (v35 * v34)) + v41)
                                            if (abs((((0.5 - (i32(load32(v10 + 216)) * 0.5)) + (v35 * v34)) + v41)) < 2147483648.0):
                                                break
                                            break
                                        v7 = -2147483648
                                        if not func56(-2147483648, v9, v10, v11, 0, 0, 1, 1, 0):
                                            v1 = 0
                                            v17 = load32(9142440)
                                            while True:  # $label137
                                                while True:  # $label117
                                                    v8 = v1
                                                    v1 = (v1 << 2)
                                                    v2 = (load32((((v1 << 2) | 4) + 8611904)) + v9)
                                                    if (u32(v17) <= u32((load32((((v1 << 2) | 4) + 8611904)) + v9))):
                                                        break
                                                    v4 = (load32((v1 + 8611904)) + v7)
                                                    if (u32(v17) <= u32((load32((v1 + 8611904)) + v7))):
                                                        break
                                                    if ((v2 | v4) < 0):
                                                        break
                                                    while True:  # $label122
                                                        while True:  # $label121
                                                            while True:  # $label120
                                                                while True:  # $label119
                                                                    while True:  # $label118
                                                                        v1 = load32(v10 + 248)
                                                                        # br_table (load32(v10 + 248) - 1)
                                                                        break
                                                                        break
                                                                    if not func282(v4, v2, v10, 0, 0, 1):
                                                                        break
                                                                    break
                                                                    break
                                                                if not func283(v4, v2, v10, 0, 0, 1, 1):
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
                                                                while True:  # $label126
                                                                    if (u32(v3) < u32(v17)):
                                                                        while True:  # $label125
                                                                            while True:  # $label124
                                                                                if not load8u((v21 + (((v1 - v2) * v14) + v18))):
                                                                                    v1 = (v1 + 1)
                                                                                    break
                                                                                if (u32(v1) >= u32(v17)):
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
                                                                        raise Unreachable()
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
                                                        if not load32(v10 + 208):
                                                            v14 = load32(v10 + 216)
                                                            if (load32(v10 + 216) <= 0):
                                                                break
                                                            v21 = (load32(v10 + 220) + v2)
                                                            if ((load32(v10 + 220) + v2) <= v2):
                                                                break
                                                            v22 = (v4 + v14)
                                                            v18 = load32(v10 + 372)
                                                            v19 = (v17 + 2)
                                                            v23 = load32(ENTITIES)
                                                            v24 = load32(9142840)
                                                            v3 = v4
                                                            while True:  # $label133
                                                                v5 = (v3 + 1)
                                                                v25 = (v3 - v4)
                                                                v1 = v2
                                                                while True:  # $label131
                                                                    if (u32(v3) < u32(v17)):
                                                                        while True:  # $label130
                                                                            while True:  # $label129
                                                                                if not load8u((v18 + (((v1 - v2) * v14) + v25))):
                                                                                    v1 = (v1 + 1)
                                                                                    break
                                                                                if (u32(v1) >= u32(v17)):
                                                                                    break
                                                                                if ((v1 | v3) < 0):
                                                                                    break
                                                                                v1 = (v1 + 1)
                                                                                if load32((v24 + ((((v1 + 1) * v19) + v5) << 2))):
                                                                                    break
                                                                                if (load32(((load8u((v23 + (load32((v24 + ((((v1 + v19) * v19) + v5) << 2))) * 132)) + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                                                                                    break
                                                                                break
                                                                            if (v1 != v21):
                                                                                continue
                                                                            break
                                                                            break
                                                                        raise Unreachable()
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
                                                        while True:  # $label136
                                                            while True:  # $label135
                                                                while True:  # $label134
                                                                    # br_table (v1 - 4)
                                                                    break
                                                                    break
                                                                if not func193(v4, v2, v10, v11, 0, 0, 1, 0):
                                                                    break
                                                                break
                                                                break
                                                            if not func194(v4, v2, v10, v11, 0, 0, 1):
                                                                break
                                                            break
                                                            break
                                                        if (u32(v3) > u32(2)):
                                                            break
                                                        if func73(v4, v2, v10, 0, 0, 1):
                                                            break
                                                        break
                                                    v17 = load32(9142440)
                                                    break
                                                v1 = (v8 + 2)
                                                if (u32(v8) < u32(5198)):
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
                        if not v20:
                            v2 = (u32(v0) < u32(24))
                            v0 = (v0 + 1)
                            if v2:
                                continue
                        break
                    while True:  # $label140
                        if not v26:
                            break
                        if not v1:
                            break
                        v0 = entities[v1]
                        v1 = load32(v13 + 20)
                        if (u32(load32(v13 + 20)) <= u32(2147483646)):
                            store32(v0 + 52, v1)
                        v1 = load32(v13 + 24)
                        if (u32(load32(v13 + 24)) <= u32(2147483646)):
                            store32(v0 + 60, v1)
                        while True:  # $label141
                            v1 = load32(v13 + 28)
                            if (u32(load32(v13 + 28)) > u32(2147483646)):
                                break
                            store32(v0 + 64, v1)
                            if (u32(load32(v13 + 28)) > u32(2147483646)):
                                break
                            store32(v0 + 68, load32(v13 + 32))
                            break
                        v2 = load32(v0 + 76)
                        while True:  # $label142
                            v1 = load32(v13 + 36)
                            if (u32(load32(v13 + 36)) > u32(2147483646)):
                                break
                            store32(v0 + 72, v1)
                            if (u32(load32(v13 + 36)) > u32(2147483646)):
                                break
                            store32(v0 + 76, load32(v13 + 40))
                            break
                        v1 = load32(v13 + 44)
                        if (u32(load32(v13 + 44)) <= u32(2147483646)):
                            store32(v0 + 84, v1)
                        v3 = ((load8u(v0 + 122) * 404) + ENTITY_TYPES)
                        v1 = load32(((load8u(v0 + 122) * 404) + ENTITY_TYPES) + 264)
                        while True:  # $label143
                            if not load32(v3 + 92):
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
                        if not v1:
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
            if (u32((v27 + 5)) < u32(v8)):
                continue
            break
    store32(9684376, load32(9671136))
    while True:  # $label146
        if (u32((load32(load32(GAME_STATE) + 60) << 1)) < u32(200)):
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
    if (u32(load32(PLAYER_COUNT)) > u32(1)):
        while True:  # $label163
            while True:  # $label149
                v4 = players[v11]
                if not load32(players[v11] + 284624):
                    break
                while True:  # $label150
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
                            while True:  # $label151
                                v3 = (v0 - v12)
                                if ((v10 + ((v0 - v12) * v3)) > 625):
                                    break
                                v3 = load32(9142440)
                                if (u32(load32(9142440)) <= u32(v0)):
                                    break
                                if ((v0 | v9) < 0):
                                    break
                                if (u32(v3) <= u32(v9)):
                                    break
                                v3 = (v3 + 2)
                                v3 = entities[load32((load32(9142840) + ((v1 + (((v0 + (v3 + 2)) + 1) * v3)) << 2)))]
                                if (load32(38448) != load8u(entities[load32((load32(9142840) + ((v1 + (((v0 + (v3 + 2)) + 1) * v3)) << 2)))].sub_state)):
                                    break
                                v5 = func26(4)
                                v13 = (func26(4) + 4)
                                v16 = load32(v3)
                                if load32(v3):
                                    store32(v3 + 4, v16)
                                store32(v3 + 8, v13)
                                store32(v3 + 4, v5)
                                store32(v3, v5)
                                # TODO: memory.fill
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
                v0 = load32(GAME_STATE)
                if (u32((load32(load32(GAME_STATE) + 60) << 1)) < u32(5)):
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
                    v33 = ((i32((v0 % 100)) / 100.0) * 6.28318548)
                    v0 = load32(9142440)
                    while True:  # $label155
                        while True:  # $label154
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
                        if (u32(v0) <= u32(v1)):
                            continue
                        while True:  # $label156
                            v34 = (func48(v34) * 20.0)
                            if (abs((func48(v34) * 20.0)) < 2147483650.0):
                                break
                            break
                        v2 = (-2147483648 + v3)
                        if ((-2147483648 + v3) <= 0):
                            continue
                        if (u32(v0) <= u32(v2)):
                            continue
                        break
                    v16 = (v2 - 10)
                    v7 = (v1 - 10)
                    v10 = 0
                    v8 = load32(load32(GAME_STATE) + 64)
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
                        while True:  # $label157
                            if not v8:
                                break
                            v0 = load32(9142416)
                            v2 = load32(9142416)
                            if not v0:
                                v2 = (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))
                            v34 = (6.28318548 / i32((4 if (u32(v2) < u32(3)) else (v2 << (v2 & 1)))))
                            v2 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                            v6 = (v6 - ((load32(9142440) & 0xFFFFFFFF) >> 1))
                            v3 = (v3 - v2)
                            # TODO: f32.demote_f64
                            v33 = func262(i32((v6 - ((load32(9142440) & 0xFFFFFFFF) >> 1))), i32((v3 - v2)))
                            if ((6.28318548 / i32((4 if (u32(v2) < u32(3)) else (v2 << (v2 & 1))))) < func262(i32((v6 - ((load32(9142440) & 0xFFFFFFFF) >> 1))), i32((v3 - v2)))):
                                break
                            if (v33 < 0.0):
                                break
                            # TODO: f32.demote_f64
                            v36 = sqrt(i32(((v3 * v3) + (v6 * v6))))
                            if (sqrt(i32(((v3 * v3) + (v6 * v6)))) >= i32(v2)):
                                break
                            v38 = (v34 - v33)
                            v3 = ((v1 * 404) + ENTITY_TYPES)
                            v2 = 0
                            while True:  # $label160
                                if not v0:
                                    v0 = (load32(41092) if load8u(9147210) else (load32(PLAYER_COUNT) - 1))
                                if (u32(v2) >= u32((4 if (u32(v0) < u32(3)) else (v0 << (v0 & 1))))):
                                    break
                                v37 = ((v34 * i32(v2)) + (v38 if (v2 & 1) else v33))
                                v35 = func48(((v34 * i32(v2)) + (v38 if (v2 & 1) else v33)))
                                while True:  # $label158
                                    # TODO: f64.promote_f32
                                    v41 = i32(((load32(9142440) & 0xFFFFFFFF) >> 1))
                                    v42 = (((0.5 - (i32(load32(v3 + 220)) * 0.5)) + (v35 * v36)) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))
                                    if (abs((((0.5 - (i32(load32(v3 + 220)) * 0.5)) + (v35 * v36)) + i32(((load32(9142440) & 0xFFFFFFFF) >> 1)))) < 2147483648.0):
                                        break
                                    break
                                v0 = -2147483648
                                v37 = func49(v37)
                                while True:  # $label159
                                    # TODO: f64.promote_f32
                                    v41 = (((0.5 - (i32(load32(v3 + 216)) * 0.5)) + (v37 * v36)) + v41)
                                    if (abs((((0.5 - (i32(load32(v3 + 216)) * 0.5)) + (v37 * v36)) + v41)) < 2147483648.0):
                                        break
                                    break
                                v2 = (v2 + 1)
                                v0 = load32(9142416)
                                continue
                                break
                            raise Unreachable()
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
            if (u32((v11 + 1)) < u32(load32(PLAYER_COUNT))):
                continue
            break
    while True:  # $label164
        v0 = load32(GAME_STATE)
        if (u32((load32(load32(GAME_STATE) + 60) << 1)) <= u32(4)):
            break
        if not load32(v0 + 64):
            break
        v0 = load32(PLAYERS)
        v3 = load32((load32(PLAYERS) + 570580))
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
        v33 = ((i32((v0 % 100)) / 100.0) * 6.28318548)
        v0 = load32(9142440)
        while True:  # $label166
            while True:  # $label165
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
            if (u32(v0) <= u32(v1)):
                continue
            while True:  # $label167
                v34 = (func48(v34) * 20.0)
                if (abs((func48(v34) * 20.0)) < 2147483650.0):
                    break
                break
            v2 = (-2147483648 + v3)
            if ((-2147483648 + v3) <= 0):
                continue
            if (u32(v0) <= u32(v2)):
                continue
            break
        v0 = load32(PLAYERS)
        v3 = load32((load32(PLAYERS) + 570580))
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
        v33 = ((i32((v0 % 100)) / 100.0) * 6.28318548)
        v0 = load32(9142440)
        while True:  # $label169
            while True:  # $label168
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
            if (u32(v0) <= u32(v1)):
                continue
            while True:  # $label170
                v34 = (func48(v34) * 20.0)
                if (abs((func48(v34) * 20.0)) < 2147483650.0):
                    break
                break
            v2 = (-2147483648 + v3)
            if ((-2147483648 + v3) <= 0):
                continue
            if (u32(v0) <= u32(v2)):
                continue
            break
        v0 = load32(PLAYERS)
        v3 = load32((load32(PLAYERS) + 570580))
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
        v33 = ((i32((v0 % 100)) / 100.0) * 6.28318548)
        v0 = load32(9142440)
        while True:  # $label172
            while True:  # $label171
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
            if (u32(v0) <= u32(v1)):
                continue
            while True:  # $label173
                v34 = (func48(v34) * 20.0)
                if (abs((func48(v34) * 20.0)) < 2147483650.0):
                    break
                break
            v2 = (-2147483648 + v3)
            if ((-2147483648 + v3) <= 0):
                continue
            if (u32(v0) <= u32(v2)):
                continue
            break
        v0 = load32(PLAYERS)
        v3 = load32((load32(PLAYERS) + 570580))
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
        v33 = ((i32((v0 % 100)) / 100.0) * 6.28318548)
        v0 = load32(9142440)
        while True:  # $label175
            while True:  # $label174
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
            if (u32(v0) <= u32(v1)):
                continue
            while True:  # $label176
                v34 = (func48(v34) * 20.0)
                if (abs((func48(v34) * 20.0)) < 2147483650.0):
                    break
                break
            v2 = (-2147483648 + v3)
            if ((-2147483648 + v3) <= 0):
                continue
            if (u32(v0) <= u32(v2)):
                continue
            break
        break
    v0 = 0
    while True:  # $label177
        v2 = load32(PLAYERS)
        v1 = load32(((load32(PLAYERS) + (load32(38508) << 2)) + 284636))
        if not load32(((load32(PLAYERS) + (load32(38508) << 2)) + 284636)):
            break
        v3 = load32(v1 + 8)
        if not load32(v1 + 8):
            break
        while True:  # $label178
            v2 = load32((load32(v1) + (v0 << 2)))
            if load32((load32(v1) + (v0 << 2))):
                func408(load32(38492), entities[v2])
            v0 = (v0 + 1)
            if ((v0 + 1) != v3):
                continue
            break
        v2 = load32(PLAYERS)
        break
    v0 = 0
    while True:  # $label179
        v1 = load32(((v2 + (load32(38504) << 2)) + 284636))
        if not load32(((v2 + (load32(38504) << 2)) + 284636)):
            break
        v2 = load32(v1 + 8)
        if not load32(v1 + 8):
            break
        while True:  # $label180
            v3 = load32((load32(v1) + (v0 << 2)))
            if load32((load32(v1) + (v0 << 2))):
                func408(load32(38492), entities[v3])
            v0 = (v0 + 1)
            if ((v0 + 1) != v2):
                continue
            break
        break
    return func126(v1, v2, 13, 13, (load32(load32(GAME_STATE) + 64) != 0))

# ----------------------------------------------------------
# $func351
# ----------------------------------------------------------
def func351(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10):
    v14 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    v19 = load8u(arg0 + 122)
    while True:  # $label0
        v11 = load32(ENTITIES)
        v18 = entities[arg3]
        v12 = load8u(entities[arg3].sub_state)
        if ((arg4 != -1) & (load8u(entities[arg3].sub_state) != arg4)):
            break
        v16 = load16u(v18 + 110)
        while True:  # $label1
            if (load32(38500) == v12):
                break
            v13 = (load32(PLAYER_COUNT) * arg6)
            v15 = load32(9143004)
            while True:  # $label2
                v17 = load16u((v11 + (arg3 * 132)) + 120)
                if load16u((v11 + (arg3 * 132)) + 120):
                else:
                if not load8u(((v17 if load8u((v15 + (v13 + v16))) else v16) + (v16 + v13))):
                    arg5 = (v11 + (arg3 * 132))
                    if (not arg5 & (load8u((v11 + (arg3 * 132)) + 127) != 6)):
                        break
                    if not load8u(arg5 + 128):
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
            arg5 = ((v12 * 404) + ENTITY_TYPES)
            v17 = load32(((v12 * 404) + ENTITY_TYPES) + 264)
            if (load32(((v12 * 404) + ENTITY_TYPES) + 264) == 2):
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
            if not func162(arg0, v12, v13, load32((v11 + (arg3 * 132)) + 28)):
                break
            v21 = load32(arg8 + 286684)
            if load32(arg8 + 286684):
                while True:  # $label5
                    while True:  # $label3
                        while True:  # $label4
                            # br_table v17
                            break
                            break
                        arg8 = ((v12 * 404) + ENTITY_TYPES)
                        v22 = load32(((v12 * 404) + ENTITY_TYPES) + 216)
                        if not load32(((v12 * 404) + ENTITY_TYPES) + 216):
                            arg5 = 0
                            break
                        arg5 = 0
                        v23 = load32(arg8 + 220)
                        if not load32(arg8 + 220):
                            break
                        arg8 = load32(9215880)
                        if not load32(9215880):
                            break
                        v24 = load32(9142432)
                        if not load32(9142432):
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
                                if not load32((v28 + (load32((v24 + ((v29 + ((arg8 + v25) * v27)) << 2))) << 2))):
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
                    if not load32(9142432):
                        break
                    arg5 = (v11 + (arg3 * 132))
                    arg5 = load32((arg8 + (((load32(9142440) * load16u((v11 + (arg3 * 132)) + 114)) + load16u(arg5 + 112)) << 2)))
                    break
                if (arg5 != arg7):
                    break
            while True:  # $label8
                if (arg4 != -1):
                    break
                if v21:
                    break
                if not load8u(((v12 * 404) + ENTITY_TYPES) + 380):
                    break
                if (u32(v15) > u32(1)):
                    break
                break
            arg4 = load32(((v19 * 404) + ENTITY_TYPES) + 228)
            if load32(((v19 * 404) + ENTITY_TYPES) + 228):
                arg5 = (load16u(arg0 + 114) - arg10)
                arg5 = (load16u(arg0 + 112) - arg9)
                if (u32((((load16u(arg0 + 114) - arg10) * arg5) + ((load16u(arg0 + 112) - arg9) * arg5))) < u32((arg4 * arg4))):
                    break
            arg4 = load32((v11 + (arg3 * 132)) + 100)
            if load32((v11 + (arg3 * 132)) + 100):
                arg4 = (v11 + (arg4 * 132))
                # TODO: i32.div_u
                if (u32((load32((((load8u((v11 + (arg4 * 132)) + 122) * 1020) + 9299904) + (v12 << 2))) * load32(arg4 + 52))) < u32(100)):
                    break
            if (v17 == 1):
                if (u32(load32((v11 + (arg3 * 132)) + 84)) < u32(load32(((v12 * 404) + ENTITY_TYPES) + 112))):
                    break
            arg5 = entities[v20]
            arg4 = (load16u(arg0 + 114) - load16u(entities[v20] + 114))
            arg4 = (load16u(arg0 + 112) - load16u(arg5 + 112))
            arg4 = (((load16u(arg0 + 114) - load16u(entities[v20] + 114)) * arg4) + ((load16u(arg0 + 112) - load16u(arg5 + 112)) * arg4))
            arg5 = ((load8u(arg5 + 122) * 404) + ENTITY_TYPES)
            if (load32(((load8u(arg5 + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                arg4 = (arg4 if (load32(arg5 + 268) == 1) else (arg4 + 100))
            if (load32(arg1) <= arg4):
                break
            if (load32(arg0 + 28) == arg3):
                break
            store32(arg2, arg3)
            store32(arg1, arg4)
            break
        if not load8u(((v19 * 404) + ENTITY_TYPES) + 336):
            break
        if not load8u((load32(9143004) + ((load32(PLAYER_COUNT) * v16) + arg6))):
            break
        while True:  # $label9
            arg0 = (v11 + (arg3 * 132))
            if (load8u((v11 + (arg3 * 132)) + 125) == 3):
                break
            if not load8u(arg0 + 128):
                break
            arg1 = (v11 + (arg3 * 132))
            store8((v11 + (arg3 * 132)) + 127, 0)
            while True:  # $label10
                arg1 = load32(arg1 + 40)
                if not load32(arg1 + 40):
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

# ----------------------------------------------------------
# $func352
# ----------------------------------------------------------
def func352(arg0, arg1, arg2, arg3, arg4):
    v7 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    store32(v7 + 76, arg1)
    v21 = (v7 + 55)
    v17 = (v7 + 56)
    while True:  # $label65
        while True:  # $label62
            while True:  # $label15
                while True:  # $label0
                    while True:  # $label4
                        v9 = arg1
                        if (v5 > (v13 ^ 2147483647)):
                            break
                        v13 = (v5 + v13)
                        while True:  # $label18
                            while True:  # $label21
                                while True:  # $label10
                                    v5 = v9
                                    v6 = load8u(v9)
                                    if load8u(v9):
                                        while True:  # $label64
                                            while True:  # $label2
                                                while True:  # $label1
                                                    arg1 = (v6 & 255)
                                                    if not (v6 & 255):
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
                                                while True:  # $label5
                                                    if (u32((load8s(arg1 + 1) - 48)) >= u32(10)):
                                                        break
                                                    if (load8u(arg1 + 2) != 36):
                                                        break
                                                    v5 = (arg1 + 3)
                                                    v15 = (load8s(arg1 + 1) - 48)
                                                    v18 = 1
                                                    break
                                                store32(v7 + 76, v5)
                                                v11 = 0
                                                while True:  # $label6
                                                    v6 = load8s(v5)
                                                    arg1 = (load8s(v5) - 32)
                                                    if (u32((load8s(v5) - 32)) > u32(31)):
                                                        v10 = v5
                                                        break
                                                    v10 = v5
                                                    arg1 = (1 << arg1)
                                                    if not ((1 << arg1) & 75913):
                                                        break
                                                    while True:  # $label7
                                                        v10 = (v5 + 1)
                                                        store32(v7 + 76, (v5 + 1))
                                                        v11 = (arg1 | v11)
                                                        v6 = load8s(v5 + 1)
                                                        arg1 = (load8s(v5 + 1) - 32)
                                                        if (u32((load8s(v5 + 1) - 32)) >= u32(32)):
                                                            break
                                                        v5 = v10
                                                        arg1 = (1 << arg1)
                                                        if ((1 << arg1) & 75913):
                                                            continue
                                                        break
                                                    break
                                                while True:  # $label11
                                                    if (v6 == 42):
                                                        while True:  # $label9
                                                            while True:  # $label8
                                                                if (u32((load8s(v10 + 1) - 48)) >= u32(10)):
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
                                                            if not arg0:
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
                                                while True:  # $label12
                                                    if (load8u(v6) != 46):
                                                        arg1 = v6
                                                        break
                                                    if (load8u(v6 + 1) == 42):
                                                        while True:  # $label14
                                                            while True:  # $label13
                                                                if (u32((load8s(v6 + 2) - 48)) >= u32(10)):
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
                                                            if not arg0:
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
                                                    if (u32((load8s(arg1) - 123)) < u32(-58)):
                                                        break
                                                    arg1 = (v12 + 1)
                                                    v5 = load8u(((v5 + (v14 * 58)) + 31711))
                                                    if (u32((load8u(((v5 + (v14 * 58)) + 31711)) - 1)) < u32(8)):
                                                        continue
                                                    break
                                                store32(v7 + 76, arg1)
                                                while True:  # $label19
                                                    while True:  # $label17
                                                        if (v5 != 27):
                                                            if not v5:
                                                                break
                                                            if (v15 >= 0):
                                                                store32((arg4 + (v15 << 2)), v5)
                                                                store64(v7 + 64, load64((arg3 + (v15 << 3))))
                                                                break
                                                            if not arg0:
                                                                break
                                                            func353((v7 - -64), v5, arg2)
                                                            break
                                                        if (v15 >= 0):
                                                            break
                                                        break
                                                    v5 = 0
                                                    if not arg0:
                                                        continue
                                                    break
                                                v6 = (v11 & -65537)
                                                v11 = ((v11 & -65537) if (v11 & 8192) else v11)
                                                v15 = 0
                                                v20 = 2107
                                                v10 = v17
                                                while True:  # $label23
                                                    while True:  # $label22
                                                        while True:  # $label58
                                                            while True:  # $label57
                                                                while True:  # $label31
                                                                    while True:  # $label33
                                                                        while True:  # $label28
                                                                            while True:  # $label43
                                                                                while True:  # $label34
                                                                                    while True:  # $label24
                                                                                        while True:  # $label26
                                                                                            while True:  # $label20
                                                                                                while True:  # $label27
                                                                                                    while True:  # $label25
                                                                                                        while True:  # $label29
                                                                                                            while True:  # $label30
                                                                                                                v5 = load8s(v12)
                                                                                                                v5 = (((load8s(v12) & -33) if ((v5 & 15) == 3) else v5) if v14 else v5)
                                                                                                                # br_table ((((load8s(v12) & -33) if ((v5 & 15) == 3) else v5) if v14 else v5) - 88)
                                                                                                                break
                                                                                                                break
                                                                                                            while True:  # $label32
                                                                                                                # br_table (v5 - 65)
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
                                                                                                    while True:  # $label41
                                                                                                        while True:  # $label40
                                                                                                            while True:  # $label39
                                                                                                                while True:  # $label38
                                                                                                                    while True:  # $label37
                                                                                                                        while True:  # $label36
                                                                                                                            while True:  # $label35
                                                                                                                                # br_table (v14 & 255)
                                                                                                                                break
                                                                                                                                break
                                                                                                                            store32(load32(v7 + 64), v13)
                                                                                                                            continue
                                                                                                                            break
                                                                                                                        store32(load32(v7 + 64), v13)
                                                                                                                        continue
                                                                                                                        break
                                                                                                                    store64(load32(v7 + 64), i32(v13))
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
                                                                                                    store64(load32(v7 + 64), i32(v13))
                                                                                                    continue
                                                                                                    break
                                                                                                v8 = (8 if (u32(v8) <= u32(8)) else v8)
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
                                                                                                    v6 = (u32(v23) > u32(15))
                                                                                                    v23 = ((v23 & 0xFFFFFFFF) >> 4)
                                                                                                    if v6:
                                                                                                        continue
                                                                                                    break
                                                                                            if not load64(v7 + 64):
                                                                                                break
                                                                                            if not (v11 & 8):
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
                                                                                                v9 = (u32(v23) > u32(7))
                                                                                                v23 = ((v23 & 0xFFFFFFFF) >> 3)
                                                                                                if v9:
                                                                                                    continue
                                                                                                break
                                                                                        v9 = v5
                                                                                        if not (v11 & 8):
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
                                                                                while True:  # $label45
                                                                                    if (u32(v23) < u32(4294967296)):
                                                                                        v24 = v23
                                                                                        break
                                                                                    while True:  # $label46
                                                                                        v6 = (v6 - 1)
                                                                                        # TODO: i64.div_u
                                                                                        v24 = 10
                                                                                        store8(v23, (i32((v23 - (10 * 10))) | 48))
                                                                                        v5 = (u32(v23) > u32(42949672959))
                                                                                        v23 = v24
                                                                                        if v5:
                                                                                            continue
                                                                                        break
                                                                                    break
                                                                                v9 = i32(v24)
                                                                                if i32(v24):
                                                                                    while True:  # $label47
                                                                                        v6 = (v6 - 1)
                                                                                        # TODO: i32.div_u
                                                                                        v5 = 10
                                                                                        store8(v9, ((v9 - (10 * 10)) | 48))
                                                                                        v12 = (u32(v9) > u32(9))
                                                                                        v9 = v5
                                                                                        if v12:
                                                                                            continue
                                                                                        break
                                                                                v9 = v6
                                                                                break
                                                                            if (v19 if (v8 < 0) else 0):
                                                                                break
                                                                            v11 = ((v11 & -65537) if v19 else v11)
                                                                            while True:  # $label48
                                                                                v24 = load64(v7 + 64)
                                                                                if (load64(v7 + 64) != 0):
                                                                                    break
                                                                                if v8:
                                                                                    break
                                                                                v9 = v17
                                                                                v8 = 0
                                                                                break
                                                                                break
                                                                            v5 = (not v24 + (v17 - v9))
                                                                            v8 = (v8 if (v5 < v8) else (not v24 + (v17 - v9)))
                                                                            break
                                                                            break
                                                                        while True:  # $label55
                                                                            v10 = (2147483647 if (u32(v8) >= u32(2147483647)) else v8)
                                                                            v12 = (2147483647 if (u32(v8) >= u32(2147483647)) else v8)
                                                                            v11 = ((2147483647 if (u32(v8) >= u32(2147483647)) else v8) != 0)
                                                                            while True:  # $label52
                                                                                while True:  # $label50
                                                                                    while True:  # $label49
                                                                                        v5 = load32(v7 + 64)
                                                                                        v9 = (load32(v7 + 64) if v5 else 8568)
                                                                                        v14 = (load32(v7 + 64) if v5 else 8568)
                                                                                        if not ((load32(v7 + 64) if v5 else 8568) & 3):
                                                                                            break
                                                                                        if not v12:
                                                                                            break
                                                                                        while True:  # $label51
                                                                                            if not load8u(v14):
                                                                                                break
                                                                                            v12 = (v12 - 1)
                                                                                            v11 = ((v12 - 1) != 0)
                                                                                            v14 = (v14 + 1)
                                                                                            if not ((v14 + 1) & 3):
                                                                                                break
                                                                                            if v12:
                                                                                                continue
                                                                                            break
                                                                                        break
                                                                                    if not v11:
                                                                                        break
                                                                                    while True:  # $label53
                                                                                        if not load8u(v14):
                                                                                            break
                                                                                        if (u32(v12) < u32(4)):
                                                                                            break
                                                                                        while True:  # $label54
                                                                                            v5 = load32(v14)
                                                                                            if (((load32(v14) ^ -1) & (v5 - 16843009)) & -2139062144):
                                                                                                break
                                                                                            v14 = (v14 + 4)
                                                                                            v12 = (v12 - 4)
                                                                                            if (u32((v12 - 4)) > u32(3)):
                                                                                                continue
                                                                                            break
                                                                                        break
                                                                                    if not v12:
                                                                                        break
                                                                                    break
                                                                                while True:  # $label56
                                                                                    if not load8u(v14):
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
                                                            while True:  # $label59
                                                                while True:  # $label61
                                                                    v9 = load32(v6)
                                                                    if not load32(v6):
                                                                        break
                                                                    while True:  # $label60
                                                                        v10 = func278((v7 + 4), v9)
                                                                        v9 = (func278((v7 + 4), v9) < 0)
                                                                        if (func278((v7 + 4), v9) < 0):
                                                                            break
                                                                        if (u32(v10) > u32((v8 - v5))):
                                                                            break
                                                                        v6 = (v6 + 4)
                                                                        v5 = (v5 + v10)
                                                                        if (u32(v8) > u32((v5 + v10))):
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
                                                            if not v5:
                                                                v5 = 0
                                                                break
                                                            v10 = 0
                                                            v6 = load32(v7 + 64)
                                                            while True:  # $label63
                                                                v9 = load32(v6)
                                                                if not load32(v6):
                                                                    break
                                                                v9 = func278((v7 + 4), v9)
                                                                v10 = (func278((v7 + 4), v9) + v10)
                                                                if (u32((func278((v7 + 4), v9) + v10)) > u32(v5)):
                                                                    break
                                                                v6 = (v6 + 4)
                                                                if (u32(v5) > u32(v10)):
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
                                                    raise Unreachable()
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
                                        raise Unreachable()
                                    if arg0:
                                        break
                                    if not v18:
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
                                    if (u32(v5) >= u32(10)):
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

# ----------------------------------------------------------
# $func353
# ----------------------------------------------------------
def func353(arg0, arg1, arg2):
    while True:  # $label3
        while True:  # $label2
            while True:  # $label1
                while True:  # $label10
                    while True:  # $label9
                        while True:  # $label8
                            while True:  # $label7
                                while True:  # $label6
                                    while True:  # $label5
                                        while True:  # $label4
                                            while True:  # $label0
                                                # br_table (arg1 - 9)
                                                break
                                                break
                                            arg1 = load32(arg2)
                                            store32(arg2, (load32(arg2) + 4))
                                            store32(arg0, load32(arg1))
                                            return
                                            break
                                        arg1 = load32(arg2)
                                        store32(arg2, (load32(arg2) + 4))
                                        store64(arg0, load16s(arg1))
                                        return
                                        break
                                    arg1 = load32(arg2)
                                    store32(arg2, (load32(arg2) + 4))
                                    store64(arg0, load16u(arg1))
                                    return
                                    break
                                arg1 = load32(arg2)
                                store32(arg2, (load32(arg2) + 4))
                                store64(arg0, load8s(arg1))
                                return
                                break
                            arg1 = load32(arg2)
                            store32(arg2, (load32(arg2) + 4))
                            store64(arg0, load8u(arg1))
                            return
                            break
                        arg1 = ((load32(arg2) + 7) & -8)
                        store32(arg2, (((load32(arg2) + 7) & -8) + 8))
                        storef64(arg0, loadf64(arg1))
                        return
                        break
                    raise Unreachable()
                    break
                return
                break
            arg1 = load32(arg2)
            store32(arg2, (load32(arg2) + 4))
            store64(arg0, load32(arg1))
            return
            break
        arg1 = load32(arg2)
        store32(arg2, (load32(arg2) + 4))
        store64(arg0, load32(arg1))
        return
        break
    arg1 = ((load32(arg2) + 7) & -8)
    store32(arg2, (((load32(arg2) + 7) & -8) + 8))
    store64(arg0, load64(arg1))

# ----------------------------------------------------------
# $func355
# ----------------------------------------------------------
def func355(arg0, arg1, arg2):
    v9 = (G.global0 - 80)
    G.global0 = (G.global0 - 80)
    v6 = (arg1 // 32)
    v3 = load32(9681892)
    v4 = load32(9142880)
    while True:  # $label1
        while True:  # $label0
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
        while True:  # $label2
            if (v3 < 0):
                v3 = (load32(9681888) << 4)
                v5 = (arg1 - (load32(9681888) << 4))
                v3 = (arg0 - v3)
                if not load8u(9142916):
                    break
                break
            v3 = (load32(9681888) << 4)
            v5 = ((v6 << 5) - (load32(9681888) << 4))
            v3 = ((v7 << 5) - v3)
            if not load8u(9142916):
                break
            break
        v13 = ((0.0 / i32((load32(9142440) * 96))) + 0.25)
        store32(v9 + 72, v4)
        # TODO: f64.promote_f32
        storef64((v9 - -64), v13)
        # TODO: f64.promote_f32
        storef64(v9 + 56, i32(v5))
        # TODO: f64.promote_f32
        storef64(v9 + 48, i32(v3))
        a_b()
        if not load8u(9142916):
            store64(v9 + 16, 0)
            store64(v9 + 24, 0)
            store32(v9 + 32, v4)
            # TODO: f32.demote_f64
            v13 = (i32((load32(9681888) << 5)) + 0.5)
            # TODO: f64.promote_f32
            storef64(v9 + 8, (i32((load32(9681888) << 5)) + 0.5))
            # TODO: f64.promote_f32
            storef64(v9, neg(v13))
            a_b()
        if not ((not load32(9142900) & (load8u(9142409) != 0)) | arg2):
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
        while True:  # $label4
            while True:  # $label10
                while True:  # $label3
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
                                while True:  # $label7
                                    while True:  # $label6
                                        while True:  # $label5
                                            if (u32(arg1) <= u32(arg2)):
                                                break
                                            if ((arg0 | arg2) < 0):
                                                break
                                            if (u32(arg0) < u32(arg1)):
                                                break
                                            break
                                        break
                                        break
                                    v5 = load32(9142840)
                                    arg1 = (arg1 + 2)
                                    v4 = (arg2 + 1)
                                    v11 = (load32(9142840) + ((((arg1 + 2) * (arg2 + 1)) + v3) << 2))
                                    if not load32((load32(9142840) + ((((arg1 + 2) * (arg2 + 1)) + v3) << 2))):
                                        store32(v11, 1)
                                        arg1 = (load32(9142440) + 2)
                                    arg1 = (((arg1 + v4) * arg1) + v3)
                                    v11 = load32((v5 + ((((arg1 + v4) * arg1) + v3) << 2)))
                                    if (u32(load32((v5 + ((((arg1 + v4) * arg1) + v3) << 2)))) >= u32(3)):
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
                            while True:  # $label13
                                while True:  # $label12
                                    while True:  # $label11
                                        if (u32(arg1) <= u32(arg2)):
                                            break
                                        if ((arg0 | arg2) < 0):
                                            break
                                        if (u32(arg0) < u32(arg1)):
                                            break
                                        break
                                    arg2 = (arg2 + 1)
                                    break
                                    break
                                arg2 = (arg2 + 1)
                                v8 = (arg1 + 2)
                                v8 = load32((load32(9142840) + ((v3 + (((arg2 + 1) + (arg1 + 2)) * v8)) << 2)))
                                if (u32(load32((load32(9142840) + ((v3 + (((arg2 + 1) + (arg1 + 2)) * v8)) << 2)))) < u32(3)):
                                    break
                                v10 = load32(38448)
                                v8 = entities[v8]
                                if (load32(38448) != load8u(entities[v8].sub_state)):
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
                            while True:  # $label16
                                if (u32(arg1) <= u32(arg2)):
                                    break
                                if ((arg0 | arg2) < 0):
                                    break
                                if (u32(arg0) >= u32(arg1)):
                                    break
                                v3 = load32(9681892)
                                v12 = (load32(9681892) != load32(38448))
                                if not (load32(9681892) != load32(38448)):
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
                                    v5 = ((v3 * 404) + ENTITY_TYPES)
                                    if (v11 % (load32(((v3 * 404) + ENTITY_TYPES) + 216) + v4)):
                                        break
                                    if ((arg2 - v6) % (load32(v5 + 220) + v4)):
                                        break
                                arg1 = 0
                                if not v12:
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
                        while True:  # $label21
                            while True:  # $label20
                                while True:  # $label19
                                    if (u32(arg1) <= u32(arg2)):
                                        break
                                    if ((arg0 | arg2) < 0):
                                        break
                                    if (u32(arg0) < u32(arg1)):
                                        break
                                    break
                                break
                                break
                            v5 = load32(9142840)
                            v4 = (arg2 + 1)
                            v8 = (((arg2 + 1) * (arg1 + 2)) + v3)
                            v12 = entities[load32((load32(9142840) + ((((arg2 + 1) * (arg1 + 2)) + v3) << 2)))]
                            if (load32(((load8u(entities[load32((load32(9142840) + ((((arg2 + 1) * (arg1 + 2)) + v3) << 2)))].sub_state) * 404) + ENTITY_TYPES) + 264) == 4):
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
                    while True:  # $label24
                        if (u32(arg1) <= u32(arg2)):
                            break
                        if ((arg0 | arg2) < 0):
                            break
                        if (u32(arg0) >= u32(arg1)):
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

# ----------------------------------------------------------
# $oc
# Export: oc
# ----------------------------------------------------------
def oc(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, param8):
    """Export: oc"""
    v8 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    while True:  # $label0
        if load8u(9684432):
            break
        if not load32(51776):
            store8(9215872, 1)
            while True:  # $label1
                v9 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    v10 = load32(9215976)
                    break
                v10 = (load32(9215988) + v9)
                store32(9215980, (load32(9215988) + v9))
                v11 = load32(9215976)
                v10 = func26((-1 if (u32(v10) > u32(1073741823)) else (v10 << 2)))
                if v9:
                    # TODO: memory.copy
                if v11:
                    v9 = load32(9215984)
                store32(9215976, v10)
                break
            store32(9215984, (v9 + 1))
            store32((v10 + (v9 << 2)), arg0)
            while True:  # $label2
                arg0 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    v9 = v10
                    break
                v9 = (load32(9215988) + arg0)
                store32(9215980, (load32(9215988) + arg0))
                v9 = func26((-1 if (u32(v9) > u32(1073741823)) else (v9 << 2)))
                if arg0:
                    # TODO: memory.copy
                store32(9215976, v9)
                arg0 = load32(9215984)
                break
            store32(9215984, (arg0 + 1))
            store32((v9 + (arg0 << 2)), arg1)
            while True:  # $label3
                arg1 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg0 = v9
                    break
                arg0 = (load32(9215988) + arg1)
                store32(9215980, (load32(9215988) + arg1))
                arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                if arg1:
                    # TODO: memory.copy
                store32(9215976, arg0)
                arg1 = load32(9215984)
                break
            store32(9215984, (arg1 + 1))
            store32((arg0 + (arg1 << 2)), arg2)
            while True:  # $label4
                arg1 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg2 = arg0
                    break
                arg2 = (load32(9215988) + arg1)
                store32(9215980, (load32(9215988) + arg1))
                arg2 = func26((-1 if (u32(arg2) > u32(1073741823)) else (arg2 << 2)))
                if arg1:
                    # TODO: memory.copy
                store32(9215976, arg2)
                arg1 = load32(9215984)
                break
            store32(9215984, (arg1 + 1))
            store32((arg2 + (arg1 << 2)), arg3)
            while True:  # $label5
                arg1 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg0 = arg2
                    break
                arg0 = (load32(9215988) + arg1)
                store32(9215980, (load32(9215988) + arg1))
                arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                if arg1:
                    # TODO: memory.copy
                store32(9215976, arg0)
                arg1 = load32(9215984)
                break
            store32(9215984, (arg1 + 1))
            store32((arg0 + (arg1 << 2)), arg4)
            while True:  # $label6
                arg4 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg1 = arg0
                    break
                arg1 = (load32(9215988) + arg4)
                store32(9215980, (load32(9215988) + arg4))
                arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                if arg4:
                    # TODO: memory.copy
                store32(9215976, arg1)
                arg4 = load32(9215984)
                break
            store32(9215984, (arg4 + 1))
            store32((arg1 + (arg4 << 2)), arg5)
            while True:  # $label7
                arg4 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg0 = arg1
                    break
                arg0 = (load32(9215988) + arg4)
                store32(9215980, (load32(9215988) + arg4))
                arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                if arg4:
                    # TODO: memory.copy
                store32(9215976, arg0)
                arg4 = load32(9215984)
                break
            store32(9215984, (arg4 + 1))
            store32((arg0 + (arg4 << 2)), arg6)
            while True:  # $label8
                arg4 = load32(9215984)
                if (load32(9215984) != load32(9215980)):
                    arg1 = arg0
                    break
                arg1 = (load32(9215988) + arg4)
                store32(9215980, (load32(9215988) + arg4))
                arg1 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
                if arg4:
                    # TODO: memory.copy
                store32(9215976, arg1)
                arg4 = load32(9215984)
                break
            store32(9215984, (arg4 + 1))
            store32((arg1 + (arg4 << 2)), arg7)
            break
        store8(9163793, arg6)
        store8(9163792, arg5)
        store8(9163794, arg7)
        while True:  # $label9
            if arg3:
                break
            if load8u(9142409):
                break
            if not arg4:
                break
            break
        store8(9142409, 0)
        while True:  # $label10
            if not load8u(9142410):
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
        while True:  # $label11
            if arg4:
                break
            while True:  # $label12
                v19 = i32(load32(9142860))
                v19 = loadf32(40616)
                v21 = loadf32(9671164)
                v20 = (((i32(load32(9142860)) - ((v19 * loadf32(40616)) / loadf32(9671164))) * 0.5) + ((v19 * i32(arg1)) + i32(load32(9142956))))
                if (abs((((i32(load32(9142860)) - ((v19 * loadf32(40616)) / loadf32(9671164))) * 0.5) + ((v19 * i32(arg1)) + i32(load32(9142956))))) < 2147483650.0):
                    break
                break
            arg1 = -2147483648
            v20 = i32(load32(9142856))
            v19 = (((v19 * i32(arg0)) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v19 * v20) / v21)) * 0.5))
            if (abs((((v19 * i32(arg0)) + i32(load32(9142952))) + ((i32(load32(9142856)) - ((v19 * v20) / v21)) * 0.5))) < 2147483650.0):
                arg0 = i32(v19)
                break
            arg0 = -2147483648
            break
        store32(59144, arg1)
        store32(59136, arg0)
        if load32(9684792):
            break
        arg4 = load8u(9681884)
        while True:  # $label13
            arg7 = load32(9671176)
            if load32(9671176):
                break
            if arg4:
                break
            if arg2:
                break
            if not load8u(59183):
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
        while True:  # $label14
            if (arg2 != 2):
                break
            if not arg4:
                break
            arg1 = load32(9142880)
            arg0 = (G.global0 - 48)
            G.global0 = (G.global0 - 48)
            while True:  # $label15
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
        arg4 = ((u32(load32(9142440)) > u32(((arg1 & 0xFFFFFFFF) >> 5))) & (u32(arg3) > u32(((arg0 & 0xFFFFFFFF) >> 5))))
        while True:  # $label18
            if (arg2 == 2):
                if not arg4:
                    break
                arg4 = load8u(9147152)
                while True:  # $label17
                    while True:  # $label16
                        if not load32(load32(GAME_STATE) + 48):
                            break
                        if arg4:
                            break
                        if not load16u((load32(9147376) + (((arg3 * arg6) + arg5) << 1))):
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
                    while True:  # $label19
                        if not load32(9142396):
                            break
                        while True:  # $label20
                            func38(load32((load32(9142392) + (arg0 << 2))))
                            arg0 = (arg0 + 1)
                            if (u32((arg0 + 1)) < u32(load32(9142396))):
                                continue
                            break
                        store32(9142396, 0)
                        arg0 = load32(9142392)
                        if not load32(9142392):
                            break
                        break
                    arg0 = 0
                    while True:  # $label21
                        if not load32(9671176):
                            break
                        if load32(9671192):
                            while True:  # $label22
                                func38(load32((load32(9671184) + (arg0 << 2))))
                                arg0 = (arg0 + 1)
                                if (u32((arg0 + 1)) < u32(load32(9671192))):
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
                    break
                arg7 = load32(9213808)
                if not load32(9213808):
                    break
                if arg4:
                    break
                arg4 = 0
                arg3 = 0
                v9 = load32(ENTITIES)
                v10 = (arg2 if load32(entities[arg2].target_id) else 0)
                if (arg2 if load32(entities[arg2].target_id) else 0):
                    while True:  # $label23
                        arg3 = (v9 + (v10 * 132))
                        arg4 = func161((v9 + (v10 * 132)), 9173808, arg7)
                        if not func161((v9 + (v10 * 132)), 9173808, arg7):
                            arg7 = 0
                            v11 = load8u(arg3 + 122)
                            if (load8u(arg3 + 122) == load32(38560)):
                                break
                            if (load32(38620) == v11):
                                break
                        if load32(arg3 + 40):
                            arg7 = (v9 + (v10 * 132))
                            func415((func295(arg3, load32(CURRENT_PLAYER)) | not load16u(arg7 + 110)), load32(arg3 + 40))
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
                    arg1 = load32(ENTITIES)
                    if arg4:
                        arg2 = (arg1 + (arg4 * 132))
                        arg3 = ((load8u((arg1 + (arg4 * 132)) + 122) * 404) + ENTITY_TYPES)
                        arg6 = (((load32(((load8u((arg1 + (arg4 * 132)) + 122) * 404) + ENTITY_TYPES) + 220) & 0xFFFFFFFF) >> 1) + load16u(arg2 + 114))
                    else:
                    break
                store32(v8 + 108, arg3)
                store32(v8 + 104, arg4)
                store32(v8 + 100, arg6)
                store32(v8 + 96, arg5)
                store32(v8 + 112, 0)
                store32(v8 + 116, load8u(9163793))
                store32(v8 + 120, load8u(9163794))
                func360((v8 + 96), load32(9213808))
                arg2 = ((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES)
                arg5 = load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 64)
                if load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 64):
                    store32(v8, load32((load32(arg2 + 52) + ((load32(9142848) % arg5) << 2))))
                    a_b()
                if (arg3 | arg4):
                    break
                arg2 = func245()
                func254(load32(9142576), arg2)
                break
            if not arg4:
                if not load8u(9142410):
                    break
                break
            arg2 = load8u(9147152)
            while True:  # $label25
                while True:  # $label24
                    if not load32(load32(GAME_STATE) + 48):
                        break
                    if arg2:
                        break
                    if not load16u((load32(9147376) + (((arg3 * arg6) + arg5) << 1))):
                        break
                    break
                break
            arg3 = func141(arg0, arg1)
            arg0 = load32(9216064)
            if load32(9216064):
                store32(9216064, 0)
                break
            while True:  # $label26
                while True:  # $label27
                    while True:  # $label28
                        # br_table arg7
                        break
                        break
                    if load8u(9142412):
                        break
                    arg0 = load32(load32(9671168))
                    if (load32(load32(9671168)) == load32(38600)):
                        break
                    if (arg0 == load32(38472)):
                        break
                    if not load32(9684800):
                        break
                    arg2 = players[load32((load32(9215960) if load32(9215968) else CURRENT_PLAYER))]
                    arg1 = load32(((players[load32((load32(9215960) if load32(9215968) else CURRENT_PLAYER))] + (arg0 * 36)) + 269376))
                    arg1 = (load32(((players[load32((load32(9215960) if load32(9215968) else CURRENT_PLAYER))] + (arg0 * 36)) + 269376)) if arg1 else 100)
                    arg0 = ((arg0 * 404) + ENTITY_TYPES)
                    store32(v8 + 96, (((load32(((players[load32((load32(9215960) if load32(9215968) else CURRENT_PLAYER))] + (arg0 * 36)) + 269376)) if arg1 else 100) * load32(((arg0 * 404) + ENTITY_TYPES) + 68)) // 100))
                    store32(v8 + 100, ((load32(arg0 + 72) * arg1) // 100))
                    store32(v8 + 104, ((load32(arg0 + 76) * arg1) // 100))
                    store32(v8 + 108, ((load32(arg0 + 80) * arg1) // 100))
                    if load8u(9163793):
                        break
                    arg0 = (G.global0 - 80)
                    G.global0 = (G.global0 - 80)
                    while True:  # $label29
                        arg1 = load32(v8 + 96)
                        if not load32(v8 + 96):
                            break
                        if (load32(arg0 + 64) >= arg1):
                            break
                        store32(arg0 + 48, 0)
                        a_b()
                        break
                    while True:  # $label30
                        arg1 = load32(v8 + 100)
                        if not load32(v8 + 100):
                            break
                        if (load32(arg0 + 68) >= arg1):
                            break
                        store32(arg0 + 32, 1)
                        a_b()
                        break
                    while True:  # $label31
                        arg1 = load32(v8 + 104)
                        if not load32(v8 + 104):
                            break
                        if (load32(arg0 + 72) >= arg1):
                            break
                        store32(arg0 + 16, 2)
                        a_b()
                        break
                    while True:  # $label32
                        arg1 = load32(v8 + 108)
                        if not load32(v8 + 108):
                            break
                        if (load32(arg0 + 76) >= arg1):
                            break
                        store32(arg0, 3)
                        a_b()
                        break
                    while True:  # $label33
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
                    if not arg1:
                        break
                    break
                arg6 = 0
                arg4 = (G.global0 - 48)
                G.global0 = (G.global0 - 48)
                arg7 = load32(9671176)
                if (u32(load32(9671176)) >= u32(3)):
                    while True:  # $label41
                        arg0 = (load32(9671168) + (arg6 * 12))
                        arg2 = (load32(9684776) + load32((load32(9671168) + (arg6 * 12)) + 8))
                        arg3 = (load32(9684772) + load32(arg0 + 4))
                        while True:  # $label36
                            while True:  # $label35
                                while True:  # $label34
                                    v9 = load32(arg0)
                                    if ((load32(arg0) != load32(38472)) & (v9 != load32(38600))):
                                        break
                                    if not load8u(9142410):
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
                                if not load32(load32(GAME_STATE) + 48):
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
                                arg0 = ((v9 * 404) + ENTITY_TYPES)
                                arg1 = load32(((v9 * 404) + ENTITY_TYPES) + 216)
                                if (load32(((v9 * 404) + ENTITY_TYPES) + 216) <= 0):
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
                                    if (u32(arg1) < u32(v14)):
                                        while True:  # $label38
                                            while True:  # $label37
                                                if (u32(arg0) >= u32(v14)):
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
                            arg2 = load32((CURRENT_PLAYER if arg0 else (arg3 if arg2 else CURRENT_PLAYER)))
                            store32(arg4 + 32, v10)
                            store32(arg4 + 28, v11)
                            store32(arg4 + 24, v12)
                            store32(arg4 + 20, v13)
                            store32(arg4 + 16, v15)
                            store32(arg4 + 12, arg2)
                            store32(arg4 + 40, load8u(9163793))
                            store32(arg4 + 36, (((2 if (arg1 == v9) else arg5) if (u32(arg7) > u32(3)) else arg5) if arg6 else arg5))
                            while True:  # $label40
                                if arg0:
                                    if load8u(9147210):
                                        func41(4, 0, 0, arg4, 11)
                                        break
                                    break
                                arg0 = load32(9213808)
                                if load8u(9147210):
                                    func41(4, 9173808, arg0, arg4, 11)
                                    break
                                arg2 = (arg0 << 2)
                                arg1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                                if arg0:
                                    # TODO: memory.copy
                                break
                            arg7 = load32(9671176)
                            break
                        arg6 = (arg6 + 1)
                        # TODO: i32.div_u
                        if (u32(arg7) < u32(3)):
                            continue
                        break
                while True:  # $label42
                    if load8u(9163792):
                        if (load32(load32(9671168)) != load32(38636)):
                            break
                    if not arg7:
                        break
                    if load32(9671192):
                        arg0 = 0
                        while True:  # $label43
                            func38(load32((load32(9671184) + (arg0 << 2))))
                            arg0 = (arg0 + 1)
                            if (u32((arg0 + 1)) < u32(load32(9671192))):
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
                arg0 = 0
                while True:  # $label44
                    if not load32(9142396):
                        break
                    while True:  # $label45
                        func38(load32((load32(9142392) + (arg0 << 2))))
                        arg0 = (arg0 + 1)
                        if (u32((arg0 + 1)) < u32(load32(9142396))):
                            continue
                        break
                    store32(9142396, 0)
                    arg0 = load32(9142392)
                    if not load32(9142392):
                        break
                    break
                store32(9684784, 1)
                store32(9684780, 1)
                G.global0 = (arg4 + 48)
                break
                break
            while True:  # $label46
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
                if not load8u(9163792):
                    store32(40604, -1)
                    store32(41088, 2)
                    store32(9142896, 0)
                    store64(v8 + 48, 2)
                while True:  # $label47
                    if not arg1:
                        break
                    arg2 = entities[arg1]
                    if not load32(entities[arg1].target_id):
                        break
                    func415((func295(arg2, load32(CURRENT_PLAYER)) | not load16u(arg2 + 110)), load32(arg2 + 40))
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
                arg0 = ((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES)
                arg1 = load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 64)
                if not load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 64):
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
