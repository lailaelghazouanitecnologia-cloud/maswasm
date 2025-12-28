"""
Tzar Engine - Core module (part 1).
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
# $func599
# ----------------------------------------------------------
def func599(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func333(-1)

# ----------------------------------------------------------
# $func600
# ----------------------------------------------------------
def func600(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func334(arg0)

# ----------------------------------------------------------
# $func601
# ----------------------------------------------------------
def func601(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()

# ----------------------------------------------------------
# $func602
# ----------------------------------------------------------
def func602(arg0, arg1):
    if arg0:
        if not load8u(9147152):
            func52((207 if load8u(9143020) else 0), 0)
            a_b()
        func331(arg0)

# ----------------------------------------------------------
# $func603
# ----------------------------------------------------------
def func603(arg0):
    if not load8u(9163793):
        store8(9216068, 1)
        a_b()

# ----------------------------------------------------------
# $func604
# ----------------------------------------------------------
def func604(arg0):
    v7 = load32(PLAYERS)
    while True:  # $label4
        while True:  # $label0
            arg0 = ((v3 * 404) + ENTITY_TYPES)
            if (load32(((v3 * 404) + ENTITY_TYPES) + 264) != 2):
                break
            if (u32(load32(arg0 + 268)) > u32(2)):
                break
            v4 = load32(((v7 + (v3 << 2)) + 284636))
            if not load32(((v7 + (v3 << 2)) + 284636)):
                break
            v5 = 0
            arg0 = load32(v4 + 8)
            if not load32(v4 + 8):
                break
            while True:  # $label3
                while True:  # $label1
                    v1 = load32((load32(v4) + (v5 << 2)))
                    if not load32((load32(v4) + (v5 << 2))):
                        break
                    v2 = load32(ENTITIES)
                    v1 = entities[v1]
                    v6 = load32(entities[v1].action)
                    if not load32(entities[v1].action):
                        break
                    if (load32(CURRENT_PLAYER) != load16u((v2 + (v6 * 132)) + 110)):
                        break
                    v6 = load32(v1 + 28)
                    while True:  # $label2
                        v1 = load32(9681836)
                        if (load32(9681836) != load32(9681832)):
                            arg0 = load32(9681828)
                            break
                        arg0 = (load32(9681840) + v1)
                        store32(9681832, (load32(9681840) + v1))
                        v2 = load32(9681828)
                        arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                        if v1:
                            # TODO: memory.copy
                        if v2:
                            v1 = load32(9681836)
                        store32(9681828, arg0)
                        break
                    store32(9681836, (v1 + 1))
                    store32((arg0 + (v1 << 2)), v6)
                    arg0 = load32(v4 + 8)
                    break
                v5 = (v5 + 1)
                if (u32((v5 + 1)) < u32(arg0)):
                    continue
                break
            break
        v3 = (v3 + 1)
        if ((v3 + 1) != 255):
            continue
        break
    func172(1)

# ----------------------------------------------------------
# $xc
# Export: xc
# ----------------------------------------------------------
def xc(arg0, arg1):
    """Export: xc"""
    while True:  # $label0
        v3 = load32(9142844)
        if (u32(load32(9142844)) < u32(4)):
            break
        v4 = load32(ENTITIES)
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

# ----------------------------------------------------------
# $pd
# Export: pd
# ----------------------------------------------------------
def pd(arg0):
    """Export: pd"""
    store32(9143000, 0)
    v1 = load32(9213820)
    if load32(9213820):
        func47(entities[v1])
        store32(9213820, 0)
    func45()
    store8(9142906, arg0)

# ----------------------------------------------------------
# $ad
# Export: ad
# ----------------------------------------------------------
def ad(arg0, arg1, arg2):
    """Export: ad"""
    if (arg0 >= 0):
        store32(load32(9568076) + 108, arg0)
    if (arg1 >= 0):
        store32(load32(9568076) + 112, arg1)
    if (arg2 >= 0):
        store32(load32(9568076) + 116, arg2)

# ----------------------------------------------------------
# $zd
# Export: zd
# ----------------------------------------------------------
def zd(arg0):
    """Export: zd"""
    v4 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label0
        v1 = load32(9568088)
        if load32(load32(9568088) + 104):
            arg0 = load32(v1 + 96)
            break
        v3 = load32(v1 + 100)
        while True:  # $label2
            while True:  # $label1
                if not arg0:
                    if not v3:
                        break
                    v3 = load32(v1 + 96)
                    arg0 = 0
                    break
                while True:  # $label3
                    if v3:
                        v3 = load32(v1 + 96)
                        arg0 = 0
                        break
                    arg0 = load32(v1 + 108)
                    store32(v1 + 100, load32(v1 + 108))
                    v2 = load32(v1 + 96)
                    v3 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                    if v2:
                    else:
                    arg0 = 0
                    store32(v1 + 96, v3)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v3 + (arg0 << 2)), 2147483647)
                while True:  # $label4
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v2 = v3
                        break
                    v2 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy
                    store32(v1 + 96, v2)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v2 + (arg0 << 2)), 2147483647)
                while True:  # $label5
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v3 = v2
                        break
                    v3 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                    if arg0:
                        # TODO: memory.copy
                    store32(v1 + 96, v3)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v3 + (arg0 << 2)), 2147483647)
                while True:  # $label6
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v2 = v3
                        break
                    v2 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy
                    store32(v1 + 96, v2)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v2 + (arg0 << 2)), 2147483647)
                while True:  # $label7
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v3 = v2
                        break
                    v3 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                    if arg0:
                        # TODO: memory.copy
                    store32(v1 + 96, v3)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v3 + (arg0 << 2)), 2147483647)
                while True:  # $label8
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v2 = v3
                        break
                    v2 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                    if arg0:
                        # TODO: memory.copy
                    store32(v1 + 96, v2)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v2 + (arg0 << 2)), 2147483647)
                while True:  # $label9
                    arg0 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        v3 = v2
                        break
                    v3 = (load32(v1 + 108) + arg0)
                    store32(v1 + 100, (load32(v1 + 108) + arg0))
                    v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                    if arg0:
                        # TODO: memory.copy
                    store32(v1 + 96, v3)
                    arg0 = load32(v1 + 104)
                    break
                store32(v1 + 104, (arg0 + 1))
                store32((v3 + (arg0 << 2)), 2147483647)
                while True:  # $label10
                    v2 = load32(v1 + 104)
                    if (load32(v1 + 104) != load32(v1 + 100)):
                        arg0 = v3
                        break
                    arg0 = (load32(v1 + 108) + v2)
                    store32(v1 + 100, (load32(v1 + 108) + v2))
                    arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                    if v2:
                        # TODO: memory.copy
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
            v3 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if v2:
            else:
            arg0 = 0
            store32(v1 + 96, v3)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v3 + (arg0 << 2)), 0)
        while True:  # $label11
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v2 = v3
                break
            v2 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(v1 + 96, v2)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v2 + (arg0 << 2)), 0)
        while True:  # $label12
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v3 = v2
                break
            v3 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(v1 + 96, v3)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v3 + (arg0 << 2)), 0)
        while True:  # $label13
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v2 = v3
                break
            v2 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(v1 + 96, v2)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v2 + (arg0 << 2)), 0)
        while True:  # $label14
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v3 = v2
                break
            v3 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(v1 + 96, v3)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v3 + (arg0 << 2)), 0)
        while True:  # $label15
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v2 = v3
                break
            v2 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(v1 + 96, v2)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v2 + (arg0 << 2)), 0)
        while True:  # $label16
            arg0 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                v3 = v2
                break
            v3 = (load32(v1 + 108) + arg0)
            store32(v1 + 100, (load32(v1 + 108) + arg0))
            v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
            if arg0:
                # TODO: memory.copy
            store32(v1 + 96, v3)
            arg0 = load32(v1 + 104)
            break
        store32(v1 + 104, (arg0 + 1))
        store32((v3 + (arg0 << 2)), 0)
        while True:  # $label17
            v2 = load32(v1 + 104)
            if (load32(v1 + 104) != load32(v1 + 100)):
                arg0 = v3
                break
            arg0 = (load32(v1 + 108) + v2)
            store32(v1 + 100, (load32(v1 + 108) + v2))
            arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if v2:
                # TODO: memory.copy
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

# ----------------------------------------------------------
# $dd
# Export: dd
# ----------------------------------------------------------
def dd(arg0):
    """Export: dd"""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    arg0 = ((9684460 if (arg0 == 1) else 9684476) if arg0 else 9684444)
    v2 = load32(((9684460 if (arg0 == 1) else 9684476) if arg0 else 9684444))
    store32(v1 + 4, load32(arg0 + 8))
    store32(v1, v2)
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $be
# Export: be
# ----------------------------------------------------------
def be():
    """Export: be"""
    while True:  # $label0
        v0 = load32(9142440)
        if (load32(9142440) <= 0):
            v1 = v0
            break
        v4 = load32(ENTITIES)
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
                    v4 = load32(ENTITIES)
                    v5 = load32(9142840)
                    v1 = load32(9142440)
                if (v0 != v3):
                    continue
                break
            if (v0 != v6):
                continue
            break
        break
    if (u32(((v1 * v1) * 80)) > u32(65535)):
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
            if (u32((v7 + 1)) < u32(((((load32(9142440) * v1) * 80) & 0xFFFFFFFF) >> 16))):
                continue
            break

# ----------------------------------------------------------
# $ae
# Export: ae
# ----------------------------------------------------------
def ae():
    """Export: ae"""
    v1 = load32(9142440)
    if (load32(9142440) > 0):
        v5 = load32(ENTITIES)
        v6 = load32(9142840)
        v0 = v1
        while True:  # $label1
            v4 = (v4 + 1)
            v3 = 0
            while True:  # $label0
                v2 = (v0 + 2)
                v3 = (v3 + 1)
                v2 = (v5 + (load32((v6 + ((v4 + (((v0 + 2) + (v3 + 1)) * v2)) << 2))) * 132))
                if (u32(((load8u((v5 + (load32((v6 + ((v4 + (((v0 + 2) + (v3 + 1)) * v2)) << 2))) * 132)) + 122) - 21) & 255)) <= u32(1)):
                    store8(v2 + 122, 0)
                    v5 = load32(ENTITIES)
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
    if (u32(((load32(9142440) << 3) * v0)) >= u32(65536)):
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

# ----------------------------------------------------------
# $bd
# Export: bd
# ----------------------------------------------------------
def bd(arg0, arg1, arg2):
    """Export: bd"""
    v3 = (G.global0 - 336)
    G.global0 = (G.global0 - 336)
    while True:  # $label5
        if not arg1:
            while True:  # $label2
                while True:  # $label1
                    while True:  # $label0
                        # br_table arg0
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
                            # TODO: memory.copy
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
                # TODO: memory.copy
                store32(v6 + 4, (arg1 + ((arg0 // 196) * 196)))
                break
                break
            v6 = load32(9568076)
            arg1 = (load32(load32(9568076) + 12) + (arg2 * 196))
            arg0 = (arg1 + 196)
            arg0 = (load32(v6 + 16) - arg0)
            # TODO: memory.copy
            store32(v6 + 16, (arg1 + ((arg0 // 196) * 196)))
            break
        v7 = load32(9568076)
        if not load32(9568076):
            break
        while True:  # $label18
            while True:  # $label20
                while True:  # $label12
                    while True:  # $label9
                        while True:  # $label11
                            if not arg0:
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
                                while True:  # $label6
                                    v8 = load32(v7 + 104)
                                    if not load32(v7 + 104):
                                        break
                                    if (u32(v8) >= u32(4)):
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
                                    if not (v8 & 3):
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
                                    while True:  # $label10
                                        if (arg0 != v4):
                                            # TODO: memory.copy
                                            arg0 = (arg0 + 196)
                                            store32(v3 + 212, (arg0 + 196))
                                            break
                                        v4 = (v4 - arg1)
                                        v5 = ((v4 - arg1) // 196)
                                        v6 = (((v4 - arg1) // 196) + 1)
                                        if (u32((((v4 - arg1) // 196) + 1)) >= u32(21913099)):
                                            break
                                        arg0 = (v5 << 1)
                                        v8 = (21913098 if (u32(v5) >= u32(10956549)) else ((v5 << 1) if (u32(arg0) > u32(v6)) else v6))
                                        if (21913098 if (u32(v5) >= u32(10956549)) else ((v5 << 1) if (u32(arg0) > u32(v6)) else v6)):
                                            if (u32(v8) >= u32(21913099)):
                                                break
                                        else:
                                        arg0 = 0
                                        v5 = (0 + (v5 * 196))
                                        # TODO: memory.copy
                                        v6 = (v5 + ((v4 // -196) * 196))
                                        # TODO: memory.copy
                                        v4 = (arg0 + (v8 * 196))
                                        store32(v3 + 216, (arg0 + (v8 * 196)))
                                        arg0 = (v5 + 196)
                                        store32(v3 + 212, (v5 + 196))
                                        store32(v3 + 208, v6)
                                        if arg1:
                                        arg1 = v6
                                        break
                                    arg2 = (arg2 + 1)
                                    if (u32((arg2 + 1)) < u32(((load32(v7 + 4) - load32(v7)) // 196))):
                                        continue
                                    break
                                break
                            arg2 = load32(9568088)
                            if not load32(9568088):
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
                            while True:  # $label14
                                arg2 = load32(v11 + 4)
                                arg1 = load32(v11 + 8)
                                if (u32(load32(v11 + 4)) < u32(load32(v11 + 8))):
                                    if (arg2 == v7):
                                        # TODO: memory.copy
                                        store32(v11 + 4, (v7 + 196))
                                        break
                                    arg0 = arg2
                                    v6 = (v7 + 196)
                                    v5 = (arg2 - (v7 + 196))
                                    arg1 = (v7 + (((arg2 - (v7 + 196)) // 196) * 196))
                                    if (u32(arg2) > u32((v7 + (((arg2 - (v7 + 196)) // 196) * 196)))):
                                        while True:  # $label15
                                            # TODO: memory.copy
                                            arg0 = (arg0 + 196)
                                            arg1 = (arg1 + 196)
                                            if (u32((arg1 + 196)) < u32(arg2)):
                                                continue
                                            break
                                    store32(v11 + 4, arg0)
                                    if (arg2 != v6):
                                        # TODO: memory.copy
                                    else:
                                    # TODO: memory.copy
                                    break
                                while True:  # $label16
                                    v6 = (((arg2 - arg0) // 196) + 1)
                                    if (u32((((arg2 - arg0) // 196) + 1)) < u32(21913099)):
                                        arg2 = ((arg1 - arg0) // 196)
                                        arg1 = (((arg1 - arg0) // 196) << 1)
                                        arg2 = (21913098 if (u32(arg2) >= u32(10956549)) else ((((arg1 - arg0) // 196) << 1) if (u32(arg1) > u32(v6)) else v6))
                                        if (21913098 if (u32(arg2) >= u32(10956549)) else ((((arg1 - arg0) // 196) << 1) if (u32(arg1) > u32(v6)) else v6)):
                                            if (u32(arg2) >= u32(21913099)):
                                                break
                                        else:
                                        v8 = 0
                                        v6 = (v4 * 196)
                                        arg1 = (v8 + (v4 * 196))
                                        while True:  # $label17
                                            arg2 = (arg2 * 196)
                                            if (v6 != (arg2 * 196)):
                                                arg2 = (arg2 + v8)
                                                break
                                            if (u32(arg1) > u32(v8)):
                                                arg2 = arg1
                                                arg1 = (arg1 + (((v4 + 1) // -2) * 196))
                                                break
                                            v6 = (1 if (u32((v5 + 195)) < u32(391)) else (v4 << 1))
                                            if (u32((1 if (u32((v5 + 195)) < u32(391)) else (v4 << 1))) >= u32(21913099)):
                                                break
                                            arg2 = (v6 * 196)
                                            arg1 = func26((v6 * 196))
                                            arg2 = (func26((v6 * 196)) + arg2)
                                            arg1 = (arg1 + (((v6 & 0xFFFFFFFF) >> 2) * 196))
                                            if not v8:
                                                break
                                            arg0 = load32(v11)
                                            break
                                        # TODO: memory.copy
                                        v5 = (v7 - arg0)
                                        v6 = (arg1 + (((v7 - arg0) // -196) * 196))
                                        # TODO: memory.copy
                                        arg1 = (arg1 + 196)
                                        arg0 = (load32(v11 + 4) - v7)
                                        # TODO: memory.copy
                                        store32(v11 + 8, arg2)
                                        arg2 = load32(v11)
                                        store32(v11, v6)
                                        store32(v11 + 4, (arg1 + ((arg0 // 196) * 196)))
                                        if arg2:
                                        break
                                    func42()
                                    raise Unreachable()
                                    break
                                func68()
                                raise Unreachable()
                                break
                            break
                            break
                        func42()
                        raise Unreachable()
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
                        while True:  # $label19
                            if (arg0 != v4):
                                # TODO: memory.copy
                                arg0 = (arg0 + 196)
                                store32(v3 + 224, (arg0 + 196))
                                break
                            v4 = (v4 - arg1)
                            v5 = ((v4 - arg1) // 196)
                            v6 = (((v4 - arg1) // 196) + 1)
                            if (u32((((v4 - arg1) // 196) + 1)) >= u32(21913099)):
                                break
                            arg0 = (v5 << 1)
                            v8 = (21913098 if (u32(v5) >= u32(10956549)) else ((v5 << 1) if (u32(arg0) > u32(v6)) else v6))
                            if (21913098 if (u32(v5) >= u32(10956549)) else ((v5 << 1) if (u32(arg0) > u32(v6)) else v6)):
                                if (u32(v8) >= u32(21913099)):
                                    break
                            else:
                            arg0 = 0
                            v5 = (0 + (v5 * 196))
                            # TODO: memory.copy
                            v6 = (v5 + ((v4 // -196) * 196))
                            # TODO: memory.copy
                            v4 = (arg0 + (v8 * 196))
                            store32(v3 + 228, (arg0 + (v8 * 196)))
                            arg0 = (v5 + 196)
                            store32(v3 + 224, (v5 + 196))
                            store32(v3 + 220, v6)
                            if arg1:
                            arg1 = v6
                            break
                        arg2 = (arg2 + 1)
                        if (u32((arg2 + 1)) < u32(((load32(v7 + 16) - load32(v7 + 12)) // 196))):
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
        v11 = load32(9568064)
        arg0 = (load32(9568064) + (load32(9568080) << 7))
        v6 = (v3 + 208)
        v12 = (G.global0 - 32)
        G.global0 = (G.global0 - 32)
        v7 = ((arg0 - v11) >> 7)
        while True:  # $label36
            while True:  # $label26
                while True:  # $label25
                    while True:  # $label22
                        arg1 = load32(9568068)
                        arg2 = load32(9568072)
                        if (u32(load32(9568068)) < u32(load32(9568072))):
                            if (arg0 == arg1):
                                store32(9568068, (func226(arg0, v6) + 128))
                                break
                            v5 = load32(9568068)
                            v9 = load32(9568068)
                            arg2 = arg0
                            v8 = (arg0 + 128)
                            arg0 = (arg0 + (v5 - (arg0 + 128)))
                            if (u32(arg1) > u32((arg0 + (v5 - (arg0 + 128))))):
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
                                    # TODO: memory.copy
                                    v9 = (v9 + 128)
                                    v4 = (v4 + 128)
                                    if (u32((v4 + 128)) < u32(arg1)):
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
                                    # TODO: memory.copy
                                    v5 = arg1
                                    arg0 = v4
                                    if (v4 != arg2):
                                        continue
                                    break
                            arg0 = (v6 + (((u32(arg2) <= u32(v6)) & (u32(load32(9568068)) > u32(v6))) << 7))
                            if ((v6 + (((u32(arg2) <= u32(v6)) & (u32(load32(9568068)) > u32(v6))) << 7)) != arg2):
                            # TODO: memory.copy
                            break
                        v5 = (((arg1 - v11) >> 7) + 1)
                        if (u32((((arg1 - v11) >> 7) + 1)) >= u32(33554432)):
                            break
                        store32(v12 + 28, 9568072)
                        arg2 = (arg2 - v11)
                        arg1 = ((arg2 - v11) >> 6)
                        v5 = (33554431 if (u32(arg2) >= u32(2147483520)) else (((arg2 - v11) >> 6) if (u32(arg1) > u32(v5)) else v5))
                        if (33554431 if (u32(arg2) >= u32(2147483520)) else (((arg2 - v11) >> 6) if (u32(arg1) > u32(v5)) else v5)):
                            if (u32(v5) >= u32(33554432)):
                                break
                        else:
                        arg2 = 0
                        store32(func26((v5 << 7)) + 12, 0)
                        arg1 = (arg2 + (v7 << 7))
                        store32(v12 + 20, (arg2 + (v7 << 7)))
                        store32(v12 + 24, (arg2 + (v5 << 7)))
                        store32(v12 + 16, arg1)
                        while True:  # $label27
                            arg2 = (v12 + 12)
                            v11 = load32((v12 + 12) + 8)
                            if (load32((v12 + 12) + 8) != load32(arg2 + 12)):
                                break
                            v10 = load32(arg2 + 4)
                            v7 = load32(arg2)
                            if (u32(load32(arg2 + 4)) > u32(load32(arg2))):
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
                                        # TODO: memory.copy
                                        arg1 = (arg1 + 128)
                                        v10 = (v10 + 128)
                                        if ((v10 + 128) != v11):
                                            continue
                                        break
                                    v11 = load32(arg2 + 4)
                                store32(arg2 + 8, arg1)
                                store32(arg2 + 4, (v5 + v11))
                                break
                            while True:  # $label31
                                while True:  # $label29
                                    v5 = (1 if (v7 == v11) else ((v11 - v7) >> 6))
                                    if (u32((1 if (v7 == v11) else ((v11 - v7) >> 6))) < u32(33554432)):
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
                                            # TODO: memory.copy
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
                                    raise Unreachable()
                                    break
                                store32(arg2 + 12, v8)
                                store32(arg2 + 8, v5)
                                store32(arg2 + 4, v5)
                                store32(arg2, v9)
                                break
                            if not v7:
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
                                # TODO: memory.copy
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
                                # TODO: memory.copy
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
                        if not load32(v12 + 12):
                            break
                        break
                    G.global0 = (v12 + 32)
                    break
                    break
                func42()
                raise Unreachable()
                break
            func68()
            raise Unreachable()
            break
        arg0 = load32(v3 + 220)
        if load32(v3 + 220):
            store32(v3 + 224, arg0)
        arg0 = load32(v3 + 208)
        if not load32(v3 + 208):
            break
        store32(v3 + 212, arg0)
        break
    G.global0 = (v3 + 336)
    return af(arg0)

# ----------------------------------------------------------
# $func620
# ----------------------------------------------------------
def func620(arg0):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store64(v1 + 8, 0)
    arg0 = load32(9213808)
    while True:  # $label0
        if load8u(9147210):
            func41(38, 9173808, arg0, (v1 + 8), 2)
            break
        v3 = (arg0 << 2)
        v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy
        break
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func622
# ----------------------------------------------------------
def func622(arg0, arg1):
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        v3 = load32(ENTITIES)
        v4 = entities[arg0]
        if (load8u(entities[arg0].unit_class) == 3):
            break
        if arg1:
            if (load8u((v3 + (arg0 * 132)) + 127) != 6):
                break
        arg1 = (v3 + (arg0 * 132))
        store8((v3 + (arg0 * 132)) + 127, 0)
        while True:  # $label1
            if not load8u(9142916):
                break
            v5 = load32(arg1 + 40)
            if not load32(arg1 + 40):
                break
            store32(v2 + 4, v5)
            store32(v2, 0)
            a_b()
            break
        func29(v4, 1)
        if not load32(arg1 + 92):
            break
        arg1 = load8u(9147141)
        if load32(9140316):
            if (load32(9140320) != load32((v3 + (arg0 * 132)) + 28)):
                break
        break
    G.global0 = (v2 + 16)

# ----------------------------------------------------------
# $func623
# ----------------------------------------------------------
def func623(arg0, arg1):
    arg0 = entities[arg0]
    if (load8u(entities[arg0] + 127) == 2):
        store8(arg0 + 127, arg1)

# ----------------------------------------------------------
# $func624
# ----------------------------------------------------------
def func624(arg0, arg1):
    while True:  # $label0
        v3 = load32(PLAYERS)
        arg1 = players[arg0]
        if load32(((players[arg0] + (load32(38452) << 2)) + 281808)):
            break
        v2 = (load32(arg1 + 283868) + 1)
        store32(arg1 + 283868, (load32(arg1 + 283868) + 1))
        while True:  # $label1
            if (u32(v2) >= u32((load32((arg1 + 284372)) + (load32((arg1 + 284380)) * load32(arg1 + 283864))))):
                break
            arg1 = (v3 + (arg0 * 286704))
            if (u32(v2) >= u32(load32(((v3 + (arg0 * 286704)) + 284376)))):
                break
            break
        arg0 = 0
        arg1 = load32(9213808)
        if not load32(9213808):
            break
        v2 = load32(38464)
        v3 = load32(ENTITIES)
        while True:  # $label2
            if (load8u((v3 + (load32(((arg0 << 2) + 9173808)) * 132)) + 122) != v2):
                arg0 = (arg0 + 1)
                if (arg1 != (arg0 + 1)):
                    continue
                break
            break
        break

# ----------------------------------------------------------
# $func625
# ----------------------------------------------------------
def func625(arg0, arg1):
    while True:  # $label0
        if (arg0 == arg1):
            break
        v2 = load32(ENTITIES)
        v3 = entities[arg0]
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
            v4 = ((load8u(v4 + 122) * 404) + ENTITY_TYPES)
            if load32(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 216):
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
                        if (u32(arg0) < u32(load32(v4 + 216))):
                            continue
                        break
                    if (u32(v5) < u32(v6)):
                        continue
                    break
            func138(v3)
            while True:  # $label3
                arg0 = (v2 + (arg1 * 132))
                if not load32((v2 + (arg1 * 132)) + 92):
                    break
                if load32(9140316):
                    if (load32(9140320) != load32((v2 + (arg1 * 132)) + 28)):
                        break
                break
            while True:  # $label4
                if not load8u(9147141):
                    break
                if not load32(arg0 + 92):
                    break
                if not load8u(9147152):
                    arg0 = (v2 + (arg1 * 132))
                    if not load8u((load32(9143008) + (load32(CURRENT_PLAYER) + (load32(PLAYER_COUNT) * load16u((v2 + (arg1 * 132)) + 110))))):
                        break
                    if (load32((load32(9215884) + (load32(arg0 + 44) << 4)) + 4) == 20):
                        break
                    if (load8u((v2 + (arg1 * 132)) + 127) == 6):
                        break
                arg0 = load32((v2 + (arg1 * 132)) + 16)
                if not load32((v2 + (arg1 * 132)) + 16):
                    break
                if not load32(arg0 + 8):
                    break
                Ya(1)
                break
            v3 = (v2 + (arg1 * 132))
            if not load32((v2 + (arg1 * 132)) + 88):
                break
            if (load32(((v8 * 404) + ENTITY_TYPES) + 264) != 4):
                break
            arg0 = (v2 + (arg1 * 132))
            if (load8u((v2 + (arg1 * 132)) + 129) != 7):
                store8(arg0 + 129, 7)
            v4 = load32(arg0 + 16)
            if load32(arg0 + 16):
            else:
            v5 = (v2 + (arg1 * 132))
            if (u32(0) < u32(load32((v2 + (arg1 * 132)) + 80))):
                break
            arg1 = load32(v3 + 88)
            if not load32(v3 + 88):
                break
            v2 = load32(9142440)
            store32(v5 + 80, 0)
            store32(v3 + 88, 0)
            store8(arg0 + 129, 0)
            # TODO: i32.div_u
            arg0 = v2
            return load32(v4 + 8)
        func29(v3, 1)
        break
    return func28(1, 1)

# ----------------------------------------------------------
# $func626
# ----------------------------------------------------------
def func626(arg0, arg1, arg2, arg3, arg4):
    arg2 = 1
    while True:  # $label0
        arg3 = load32(ENTITIES)
        v5 = load8u(entities[arg0].sub_state)
        arg1 = load32(arg1)
        v6 = (arg3 + (load32(arg1) * 132))
        arg4 = load8u((arg3 + (load32(arg1) * 132)) + 122)
        if (load8u(entities[arg0].sub_state) == load8u((arg3 + (load32(arg1) * 132)) + 122)):
            break
        if (load32(((arg4 * 404) + ENTITY_TYPES) + 140) == 2):
            if (u32(load32(((v5 * 404) + ENTITY_TYPES) + 216)) > u32(1)):
                break
        if (load32((arg3 + (arg0 * 132)) + 36) == arg1):
            break
        arg2 = 0
        if not load32((load32(PLAYERS) + (load16u((arg3 + (arg1 * 132)) + 110) * 286704)) + 286684):
            break
        if (load32(((arg4 * 404) + ENTITY_TYPES) + 264) != 4):
            break
        arg1 = (arg3 + (arg1 * 132))
        if load8u((arg3 + (arg1 * 132)) + 125):
            break
        if (load8u(arg1 + 129) == 7):
            break
        break
    return arg2

# ----------------------------------------------------------
# $func627
# ----------------------------------------------------------
def func627(arg0):
    v2 = load32(ENTITIES)
    v3 = load32(arg0 + 32)
    v1 = entities[load32(arg0 + 32)]
    while True:  # $label0
        v5 = load32(PLAYERS)
        if not load32(players[load16u(arg0 + 110)] + 286684):
            v6 = load32(v1 + 16)
            if not load32(v1 + 16):
                break
            v2 = (v2 + (v3 * 132))
            v3 = load32(((load8u((v2 + (v3 * 132)) + 122) * 404) + ENTITY_TYPES) + 136)
            # TODO: i32.div_u
            if (u32((load32(((load8u((v2 + (v3 * 132)) + 122) * 404) + ENTITY_TYPES) + 136) * 150)) < u32((100 if (load32((((v5 + (load16u(v2 + 110) * 286704)) + (load32(39216) << 2)) + 281808)) == 1) else v3))):
                break
            while True:  # $label3
                v9 = load16u(v1 + 110)
                v10 = ((players[load16u(v1 + 110)] + (load32(39216) << 2)) + 281808)
                v3 = load32(9142440)
                v5 = (load32(9142440) + 2)
                v11 = load8u(v1 + 122)
                v6 = ((load8u(v1 + 122) * 404) + ENTITY_TYPES)
                v7 = load32(ENTITIES)
                v12 = load32(9142840)
                v13 = load16u(v1 + 114)
                v14 = load16u(v1 + 112)
                v1 = 0
                while True:  # $label4
                    while True:  # $label1
                        v2 = v1
                        v4 = (v1 << 2)
                        v1 = (load32((((v1 << 2) | 4) + 8611904)) + v13)
                        if (u32(v3) <= u32((load32((((v1 << 2) | 4) + 8611904)) + v13))):
                            break
                        v4 = (load32((v4 + 8611904)) + v14)
                        if (u32(v3) <= u32((load32((v4 + 8611904)) + v14))):
                            break
                        if ((v1 | v4) < 0):
                            break
                        v4 = load32((((v4 + (((v1 + (load32(v6 + 208) * v5)) + 1) * v5)) << 2) + v12) + 4)
                        v1 = (v7 + (load32((((v4 + (((v1 + (load32(v6 + 208) * v5)) + 1) * v5)) << 2) + v12) + 4) * 132))
                        if (load8u((v7 + (load32((((v4 + (((v1 + (load32(v6 + 208) * v5)) + 1) * v5)) << 2) + v12) + 4) * 132)) + 122) != v11):
                            break
                        if (load16u(v1 + 110) != v9):
                            break
                        while True:  # $label2
                            # br_table (load8u(v1 + 125) - 4)
                            break
                            break
                        v1 = load32(v1 + 16)
                        if load32(v1 + 16):
                            v15 = load32(v6 + 136)
                            # TODO: i32.div_u
                            if (u32((load32(v6 + 136) * 150)) >= u32((100 if (load32(v10) == 1) else v15))):
                                break
                        break
                        break
                    v1 = (v2 + 2)
                    if (u32(v2) < u32(1918)):
                        continue
                    break
                break
            v1 = 0
            if not 0:
                break
            store32(arg0 + 32, v1)
            return 0
        if (load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 264) != 4):
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

# ----------------------------------------------------------
# $func628
# ----------------------------------------------------------
def func628(arg0):
    atomic_store(arg0, 1)
    func248(0, arg0)
    # TODO: i32.atomic.rmw.cmpxchg

# ----------------------------------------------------------
# $func629
# ----------------------------------------------------------
def func629(arg0, arg1, arg2):
    v3 = load32(arg0)
    v4 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    v4 = func26((v3 + 4))
    store32(9687208, v3)
    store32(9687204, v4)
    if arg2:
        # TODO: memory.copy
    arg1 = 0
    arg2 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    arg0 = load32(arg0 + 8)
    store32(9147312, load32(arg0 + 8))
    store32(9147324, (arg0 ^ -1))
    store32(9147320, (arg0 ^ -1515870811))
    store32(9147316, (arg0 ^ 1515870810))
    while True:  # $label0
        arg0 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        arg2 = load32(9142384)
        v3 = load32(PLAYERS)
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
    store32(CURRENT_PLAYER, arg1)
    if not load8u(9147208):
        arg0 = load32(PLAYER_COUNT)
    if (u32(arg0) >= u32(2)):
        v3 = load32(PLAYERS)
        arg1 = 1
        while True:  # $label3
            while True:  # $label2
                arg2 = (v3 + (arg1 * 286704))
                if not load32((v3 + (arg1 * 286704)) + 284616):
                    break
                if not load32(arg2 + 286684):
                    break
                store32((arg2 + 286684), 0)
                arg0 = load32(PLAYER_COUNT)
                break
            arg1 = (arg1 + 1)
            if (u32((arg1 + 1)) < u32(arg0)):
                continue
            break

# ----------------------------------------------------------
# $func632
# ----------------------------------------------------------
def func632(arg0, arg1):
    while True:  # $label0
        arg1 = load32(ENTITIES)
        v2 = entities[arg0]
        v3 = load8u(entities[arg0].unit_class)
        if (load8u(entities[arg0].unit_class) == 3):
            break
        if load16u(v2 + 110):
            break
        v4 = (arg1 + (arg0 * 132))
        while True:  # $label1
            if (u32(v3) > u32(1)):
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
            v2 = (((v5 + (arg0 % 21)) - 10) if (u32(arg0) > u32(v2)) else (load32(9142440) - 1))
            arg1 = ((v6 + (arg1 % 21)) - 10)
            arg0 = (((v6 + (arg1 % 21)) - 10) if (u32(arg0) > u32(arg1)) else v3)
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

# ----------------------------------------------------------
# $func634
# ----------------------------------------------------------
def func634(arg0, arg1):
    arg1 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v2 = entities[arg0]
    v5 = load16u(v2 + 116)
    v6 = load16u(v2 + 118)
    while True:  # $label0
        v2 = load32(9142440)
        if (u32(load32(9142440)) <= u32(v6)):
            break
        if (u32(v2) <= u32(v5)):
            break
        while True:  # $label1
            v4 = ((v5 << 5) - load32(9142952))
            v4 = ((v6 << 5) - load32(9142956))
            if ((((((v5 << 5) - load32(9142952)) * v4) + (((v6 << 5) - load32(9142956)) * v4)) - 1) > 9000000):
                break
            v4 = load32(39940)
            while True:  # $label2
                v3 = load32(load32(GAME_STATE) + 48)
                if not load32(load32(GAME_STATE) + 48):
                    break
                if load8u(9147152):
                    break
                v2 = load16u((load32(9147376) + (((v2 * v6) + v5) << 1)))
                if (v3 == 2):
                    if (u32(v2) > u32(1)):
                        break
                    break
                if not v2:
                    break
                break
            store32(arg1 + 56, v6)
            store32(arg1 + 52, v5)
            store32(arg1 + 48, v4)
            a_b()
            break
        v9 = load32(9671136)
        if (u32(load32(9671136)) < u32(4)):
            break
        v4 = 3
        while True:  # $label7
            while True:  # $label3
                v7 = (v4 * 132)
                v2 = ((v4 * 132) + load32(ENTITIES))
                if (load8u(((v4 * 132) + load32(ENTITIES)) + 125) != 3):
                    break
                if (u32(((load32(9142848) - load32(v2 + 68)) * 25)) > u32(6999)):
                    break
                v3 = (load16u(v2 + 112) - v5)
                v3 = (load16u(v2 + 114) - v6)
                v3 = load32((players[load16u(v2 + 110)] + 284348))
                if (((((load16u(v2 + 112) - v5) * v3) + ((load16u(v2 + 114) - v6) * v3)) - 1) > (load32((players[load16u(v2 + 110)] + 284348)) * v3)):
                    break
                if not load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 348):
                    break
                while True:  # $label4
                    v3 = load32(v2 + 40)
                    if not load32(v2 + 40):
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
                if not func34(load32(38660), load16u(entities[arg0] + 110), load16u(v2 + 112), load16u(v2 + 114), 0, 1):
                    break
                v3 = (load32(ENTITIES) + v7)
                v2 = load16u((load32(ENTITIES) + v7) + 114)
                v3 = load16u(v3 + 112)
                while True:  # $label6
                    while True:  # $label5
                        v10 = load32(load32(GAME_STATE) + 48)
                        if load32(load32(GAME_STATE) + 48):
                            if not load8u(9147152):
                                break
                        v7 = load32(9142440)
                        break
                        break
                    v7 = load32(9142440)
                    v8 = load16u((load32(9147376) + (((load32(9142440) * v2) + v3) << 1)))
                    if (v10 == 2):
                        if (u32(v8) > u32(1)):
                            break
                        break
                    if not v8:
                        break
                    break
                func80(i32(v3), i32(v2), load32(9142536), 32.0, i32((v7 * 96)))
                break
            v4 = (v4 + 1)
            if ((v4 + 1) != v9):
                continue
            break
        break
    G.global0 = (arg1 - -64)

# ----------------------------------------------------------
# $func635
# ----------------------------------------------------------
def func635(arg0, arg1):
    while True:  # $label0
        v5 = load32(ENTITIES)
        v7 = entities[arg0]
        if load8u(entities[arg0].link_prev):
            break
        arg1 = load8u(v7 + 125)
        if ((u32(load8u(v7 + 125)) <= u32(14)) if ((1 << arg1) & 16408) else 0):
            break
        arg1 = -1
        v10 = func106(v7, -1, -1, -1)
        if not func106(v7, -1, -1, -1):
            break
        while True:  # $label1
            v14 = (v5 + (arg0 * 132))
            if (load8u((v5 + (arg0 * 132)) + 129) == 6):
                break
            arg1 = 5
            if (load32(((load8u(v14 + 122) * 404) + ENTITY_TYPES) + 264) == 1):
                break
            v2 = entities[v10]
            v19 = (entities[v10] - -64)
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
                    while True:  # $label2
                        v4 = (v6 - load16u(v11 + 112))
                        v4 = arg1
                        arg1 = (arg1 - load16u(v11 + 114))
                        if (((((v6 - load16u(v11 + 112)) * v4) + ((arg1 - load16u(v11 + 114)) * arg1)) - 1) > 25):
                            break
                        v12 = load32(9142440)
                        if (u32(load32(9142440)) <= u32(v4)):
                            break
                        if ((v4 | v6) < 0):
                            break
                        if (u32(v6) >= u32(v12)):
                            break
                        v22 = (v4 + 1)
                        arg1 = 0
                        v16 = load32(9142840)
                        while True:  # $label5
                            while True:  # $label3
                                v3 = (v12 + 2)
                                v3 = load32((v16 + ((v15 + ((v22 + ((v12 + 2) * arg1)) * v3)) << 2)))
                                if (u32(load32((v16 + ((v15 + ((v22 + ((v12 + 2) * arg1)) * v3)) << 2)))) < u32(3)):
                                    break
                                if (arg0 == v3):
                                    break
                                v8 = load8u(v2 + 122)
                                if (load8u(v2 + 122) == load32(38500)):
                                    break
                                v13 = load16u(v2 + 110)
                                v9 = entities[v3]
                                v17 = (load32(PLAYER_COUNT) * load16u(entities[v3] + 110))
                                v18 = load32(9143004)
                                while True:  # $label4
                                    v3 = load16u(v2 + 120)
                                    if load16u(v2 + 120):
                                    else:
                                    if not load8u(((v3 if load8u((v18 + (v13 + v17))) else v13) + (v13 + v17))):
                                        if (load8u(v2 + 127) != 6):
                                            break
                                        if not load8u(v2 + 128):
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
                                v3 = ((v8 * 404) + ENTITY_TYPES)
                                if (load32(((v8 * 404) + ENTITY_TYPES) + 264) == 2):
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
                if not arg1:
                    continue
                break
            arg1 = (-1 if (load8u(v14 + 129) == 6) else 5)
            break
        return
        break
    store32((load32(9215884) + (load32(v7 + 44) << 4)), (load32(9142848) + (80 if load8u(9216060) else 40)))

# ----------------------------------------------------------
# $func638
# ----------------------------------------------------------
def func638(arg0, arg1, param2):
    while True:  # $label0
        v4 = load32(ENTITIES)
        arg1 = entities[arg0]
        v3 = load32(entities[arg0].z)
        if not load32(entities[arg0].z):
            break
        if (u32(load32(v3 + 8)) < u32(5)):
            break
        v2 = load32(load32(v3) + 16)
        break
    while True:  # $label1
        if (load8u(arg1 + 125) == 1):
            v2 = (v4 + (arg0 * 132))
            v3 = load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32)
            if load32(((load32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)) + 4) * 40) + 9671200) + 32):
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
                while True:  # $label2
                    if not arg0:
                        break
                    if (u32(load32(arg0 + 8)) < u32(5)):
                        break
                    store32(load32(arg0) + 16, v4)
                    break
                return
            store32(arg0 + 8, 0)
            func29(arg1, 1)
            return
        store32((load32(9215884) + (load32((v4 + (arg0 * 132)) + 44) << 4)), (load32(9142848) + 40))
        break

# ----------------------------------------------------------
# $func639
# ----------------------------------------------------------
def func639(arg0):
    while True:  # $label0
        v1 = entities[load32(arg0 + 32)]
        if (load8u(entities[load32(arg0 + 32)].unit_class) != 3):
            break
        v1 = func236(arg0, v1)
        if func236(arg0, v1):
            store32(arg0 + 32, v1)
            arg0 = load32(arg0 + 20)
            if not load32(arg0 + 20):
                break
            if (u32(load32(arg0 + 8)) < u32(5)):
                break
            store32(load32(arg0) + 16, v1)
            return 0
        v2 = 1
        arg0 = load32(arg0 + 20)
        if not load32(arg0 + 20):
            break
        store32(arg0 + 8, 0)
        break
    return v2

# ----------------------------------------------------------
# $func641
# ----------------------------------------------------------
def func641(arg0):
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    while True:  # $label0
        if load8u(9163793):
            break
        v4 = entities[load32(9173808)]
        arg0 = load16u(entities[load32(9173808)].rally_y)
        v3 = (load16u(entities[load32(9173808)].rally_y) - 2)
        v5 = ((load8u(v4 + 122) * 404) + ENTITY_TYPES)
        v7 = ((arg0 + load32(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 216)) + 2)
        if ((load16u(entities[load32(9173808)].rally_y) - 2) >= ((arg0 + load32(((load8u(v4 + 122) * 404) + ENTITY_TYPES) + 216)) + 2)):
            break
        v6 = ((load32(v5 + 220) + load16u(v4 + 114)) + 2)
        while True:  # $label6
            v5 = (v3 + 1)
            arg0 = (load16u(v4 + 114) - 2)
            if (v6 > (load16u(v4 + 114) - 2)):
                while True:  # $label5
                    while True:  # $label3
                        while True:  # $label2
                            while True:  # $label1
                                v2 = load32(9142440)
                                if (u32(load32(9142440)) <= u32(arg0)):
                                    break
                                if ((arg0 | v3) < 0):
                                    break
                                if (u32(v2) > u32(v3)):
                                    break
                                break
                            break
                            break
                        while True:  # $label4
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
                            v2 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                            if arg0:
                                # TODO: memory.copy
                            break
                        break
                    arg0 = v8
                    if (call_table(load32(9213856)) != v8):
                        continue
                    break
            v3 = v5
            if (v5 != v7):
                continue
            break
        break
    G.global0 = (v1 + 48)
    return arg0

# ----------------------------------------------------------
# $func645
# ----------------------------------------------------------
def func645(arg0, arg1, arg2):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    if load8u(9142388):
        store32(arg0, load32(59164))
    G.global0 = (arg0 + 16)

# ----------------------------------------------------------
# $ce
# Export: ce
# ----------------------------------------------------------
def ce():
    """Export: ce"""
    store8(9147213, 1)
    store8(9147152, 0)
    store8(9681884, 0)
    v0 = load32(9142440)
    v0 = (load32(9142440) * v0)
    v0 = (-1 if (v0 < 0) else ((load32(9142440) * v0) << 1))
    v1 = func26((-1 if (v0 < 0) else ((load32(9142440) * v0) << 1)))
    # TODO: memory.fill
    store32(9142436, v1)
    v0 = load32(CURRENT_PLAYER)
    if not ((load32(CURRENT_PLAYER) != 2147483647) if v0 else 0):
        store32(CURRENT_PLAYER, 1)
    la()
    if not load8u(9147152):
        func52((207 if load8u(9143020) else 0), 0)
        a_b()
    v1 = load32(9671136)
    if (u32(load32(9671136)) >= u32(4)):
        v2 = load32(ENTITIES)
        v0 = 3
        while True:  # $label1
            while True:  # $label0
                v3 = (v2 + (v0 * 132))
                if (load8u((v2 + (v0 * 132)) + 125) == 3):
                    break
                if not load32(v3 + 28):
                    break
                if (load32(v3 + 32) != -1):
                    break
                store32(v3 + 32, 0)
                func240(v3, 500, 0)
                v1 = load32(9671136)
                v2 = load32(ENTITIES)
                break
            v0 = (v0 + 1)
            if (u32((v0 + 1)) < u32(v1)):
                continue
            break
    while True:  # $label2
        v0 = load32(GAME_STATE)
        if not load32(load32(GAME_STATE) + 48):
            break
        while True:  # $label3
            if load32(9147376):
            else:
                v2 = load32(9142440)
                v2 = ((load32(9142440) * v2) + 2)
                v2 = (-1 if (v2 < 0) else (((load32(9142440) * v2) + 2) << 1))
                v3 = func26((-1 if (v2 < 0) else (((load32(9142440) * v2) + 2) << 1)))
                # TODO: memory.fill
                store32(9147376, v3)
            if not (load32(v0 + 48) != 0):
                break
            if load8u(9147152):
                break
            if (u32(v1) < u32(4)):
                break
            v2 = load32(ENTITIES)
            v0 = 3
            while True:  # $label5
                while True:  # $label4
                    v3 = (v2 + (v0 * 132))
                    if (load8u((v2 + (v0 * 132)) + 125) == 3):
                        break
                    if not load32(v3 + 28):
                        break
                    if load32(v3 + 36):
                        break
                    v1 = load32(9671136)
                    v2 = load32(ENTITIES)
                    break
                v0 = (v0 + 1)
                if (u32((v0 + 1)) < u32(v1)):
                    continue
                break
            break
        if (u32(v1) < u32(4)):
            break
        v0 = 3
        while True:  # $label7
            while True:  # $label6
                v1 = entities[v0]
                if (load8u(entities[v0].unit_class) == 3):
                    break
                if not load32(v1 + 28):
                    break
                if func292(v1):
                    break
                func158(v1)
                break
            v0 = (v0 + 1)
            if (u32((v0 + 1)) < u32(load32(9671136))):
                continue
            break
        break
    return 0

# ----------------------------------------------------------
# $func648
# ----------------------------------------------------------
def func648(arg0, arg1, arg2):
    arg1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
        arg0 = players[load32(arg0)]
        arg2 = load32(players[load32(arg0)] + 284616)
        if not load32(players[load32(arg0)] + 284616):
            La(load32(arg0 + 283908), 1)
            break
        store32(arg1, arg2)
        break
    G.global0 = (arg1 + 16)

# ----------------------------------------------------------
# $func649
# ----------------------------------------------------------
def func649(arg0, arg1, arg2):
    arg0 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(arg0 + 12, 0)
    func71(31, (arg0 + 12), 1, 0, 0, 1)
    G.global0 = (arg0 + 16)

# ----------------------------------------------------------
# $func650
# ----------------------------------------------------------
def func650(arg0, arg1, arg2):
    arg2 = 0
    v3 = load32(PLAYERS)
    while True:  # $label0
        v4 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
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

# ----------------------------------------------------------
# $ea
# Export: ea
# ----------------------------------------------------------
def ea(arg0):
    """Export: ea"""
    while True:  # $label0
        v2 = load32(PLAYER_COUNT)
        if (u32(load32(PLAYER_COUNT)) < u32(2)):
            break
        v3 = load32(PLAYERS)
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

# ----------------------------------------------------------
# $ja
# Export: ja
# ----------------------------------------------------------
def ja(arg0, arg1, arg2, arg3):
    """Export: ja"""
    v6 = load32(PLAYER_COUNT)
    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
        v5 = load32(PLAYERS)
        v4 = 1
        while True:  # $label0
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

# ----------------------------------------------------------
# $ia
# Export: ia
# ----------------------------------------------------------
def ia(arg0, arg1):
    """Export: ia"""
    v4 = load32(PLAYER_COUNT)
    if (u32(load32(PLAYER_COUNT)) >= u32(2)):
        v3 = load32(PLAYERS)
        v2 = 1
        while True:  # $label0
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

# ----------------------------------------------------------
# $func654
# ----------------------------------------------------------
def func654(arg0, arg1):
    v5 = load32(ENTITIES)
    v8 = entities[arg0]
    v9 = (v5 + (arg1 * 132))
    v2 = load8u((v5 + (arg1 * 132)) + 122)
    while True:  # $label0
        if not load8u(9216060):
            break
        if (load32(39064) != v2):
            break
        v12 = (v5 + (arg1 * 132))
        while True:  # $label1
            v2 = load32(PLAYERS)
            v13 = (v5 + (arg0 * 132))
            v6 = load16u((v5 + (arg0 * 132)) + 110)
            arg1 = (load32(PLAYERS) + (load16u((v5 + (arg0 * 132)) + 110) * 286704))
            v3 = load32((load32(PLAYERS) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + 283848)
            if (load32((load32(PLAYERS) + (load16u((v5 + (arg0 * 132)) + 110) * 286704)) + 283848) == 2147483647):
                break
            store32((arg1 + 283848), (load32(v12 + 52) + v3))
            v3 = 1
            store8(arg1 + 286701, 1)
            v4 = load32(PLAYER_COUNT)
            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                break
            v10 = (v4 - 1)
            v14 = ((v4 - 1) & 1)
            v6 = (load32((v2 + (v6 * 286704)) + 283908) * v4)
            v2 = 0
            v7 = load32(PLAYERS)
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
            if not v14:
                break
            if not load8u((v11 + (v3 + v6))):
                break
            store8((v7 + (v3 * 286704)) + 286701, 1)
            break
        arg1 = (arg1 + 281640)
        store32((arg1 + 281640), (load32(arg1) + load32(v12 + 52)))
        while True:  # $label3
            if load8u(9142917):
                break
            if (load32(CURRENT_PLAYER) != load16u(v13 + 110)):
                break
            a_b()
            break
        arg0 = (v5 + (arg0 * 132))
        store8((v5 + (arg0 * 132)) + 125, 0)
        v6 = load32(9142440)
        v12 = (load32(9142440) + 2)
        v13 = load8u(v9 + 122)
        v10 = ((load32(9142440) + 2) * load32(((load8u(v9 + 122) * 404) + ENTITY_TYPES) + 208))
        v7 = load16u(arg0 + 112)
        v14 = (load16u(arg0 + 112) + 12)
        v11 = load16u(arg0 + 114)
        v16 = (load16u(arg0 + 114) + 12)
        v9 = (v11 - 12)
        v2 = (v7 - 12)
        v17 = load32(ENTITIES)
        v18 = load32(9142840)
        v4 = 2147483647
        arg0 = 0
        while True:  # $label6
            v5 = (v2 + 1)
            if (u32(v2) < u32(v6)):
                arg1 = (v7 - v2)
                v19 = ((v7 - v2) * arg1)
                arg1 = v9
                while True:  # $label5
                    while True:  # $label4
                        v3 = arg1
                        if (u32(v6) <= u32(arg1)):
                            break
                        if ((v2 | v3) < 0):
                            break
                        arg1 = (v11 - v3)
                        v15 = (((v11 - v3) * arg1) + v19)
                        if ((((v11 - v3) * arg1) + v19) >= v4):
                            break
                        arg1 = load32((v18 + (((((v3 + v10) + 1) * v12) + v5) << 2)))
                        if not load32((v18 + (((((v3 + v10) + 1) * v12) + v5) << 2))):
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
    while True:  # $label7
        v6 = ((v2 * 404) + ENTITY_TYPES)
        if (load32(((v2 * 404) + ENTITY_TYPES) + 268) != 3):
            break
        while True:  # $label8
            while True:  # $label9
                v3 = (v5 + (arg0 * 132))
                v4 = load8u((v5 + (arg0 * 132)) + 122)
                # br_table (load8u((v5 + (arg0 * 132)) + 122) + -64)
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
        store32(load32(((v2 * 404) + ENTITY_TYPES) + 188) + 88, (3 + (v2 << 16)))
        arg1 = (v5 + (arg1 * 132))
        func207(v8, load32((v5 + (arg1 * 132)) + 28))
        store8(v4 + 125, 0)
        v5 = ((load8u(v9 + 122) * 404) + ENTITY_TYPES)
        if load32(((load8u(v9 + 122) * 404) + ENTITY_TYPES) + 216):
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
                    if (u32(v3) < u32(load32(v5 + 216))):
                        continue
                    break
                if (u32(v2) < u32(v10)):
                    continue
                break
        func138(v9)
        store32(arg1 + 36, arg0)
        if (load8u(v6 + 125) != 10):
        else:
        arg0 = func166(load16u(v4 + 114), load16u(v4 + 110), load32(((load8u(v9 + 122) * 404) + ENTITY_TYPES) + 188), 3)
        if func166(load16u(v4 + 114), load16u(v4 + 110), load32(((load8u(v9 + 122) * 404) + ENTITY_TYPES) + 188), 3):
            return (v5 + (arg0 * 132))
        func29(v8, 1)
        return func32(0, v9, 1)
        break
    while True:  # $label12
        if not func297(v8, arg1):
            break
        v4 = ((load8u(v9 + 122) * 404) + ENTITY_TYPES)
        if load32(((load8u(v9 + 122) * 404) + ENTITY_TYPES) + 216):
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
                    if (u32(v3) < u32(load32(v4 + 216))):
                        continue
                    break
                if (u32(v2) < u32(v10)):
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
        if not load32(v8 + 24):
            v3 = func26(16)
            store64(func26(16), 0)
            store64(v3 + 8, 0)
            store32(v8 + 24, v3)
        while True:  # $label16
            while True:  # $label15
                arg1 = load32(v3 + 4)
                if not load32(v3 + 4):
                    arg1 = func26(16)
                    store32(func26(16) + 4, 2)
                    store32(arg1, func26(8))
                    store64(arg1 + 8, 8589934592)
                    store32(v3 + 4, arg1)
                    break
                v4 = load32(arg1 + 8)
                if not load32(arg1 + 8):
                    break
                v7 = load32(arg1)
                while True:  # $label17
                    if not load32((v7 + (v2 << 2))):
                        break
                    v2 = (v2 + 2)
                    if (u32((v2 + 2)) < u32(v4)):
                        continue
                    break
                break
            while True:  # $label18
                if not load32(v8 + 40):
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
                if (u32(v2) < u32(load32(9163784))):
                    break
                store32(v6, v4)
                a_b()
                store32(9163784, (load32(9163784) + 40000))
                v3 = load32(v8 + 24)
                arg1 = load32(load32(v8 + 24) + 4)
                break
            while True:  # $label19
                v2 = load32(arg1 + 8)
                if (load32(arg1 + 8) != load32(arg1 + 4)):
                    v4 = load32(arg1)
                    break
                v4 = (load32(arg1 + 12) + v2)
                store32(arg1 + 4, (load32(arg1 + 12) + v2))
                v7 = load32(arg1)
                v4 = func26((-1 if (u32(v4) > u32(1073741823)) else (v4 << 2)))
                if v2:
                    # TODO: memory.copy
                if v7:
                    v3 = load32(v8 + 24)
                    v2 = load32(arg1 + 8)
                store32(arg1, v4)
                break
            v3 = load32(v3 + 4)
            store32(arg1 + 8, (v2 + 1))
            store32((v4 + (v2 << 2)), 0)
            while True:  # $label20
                arg1 = load32(v3 + 8)
                if (load32(v3 + 8) != load32(v3 + 4)):
                    v2 = load32(v3)
                    break
                v2 = (load32(v3 + 12) + arg1)
                store32(v3 + 4, (load32(v3 + 12) + arg1))
                v4 = load32(v3)
                v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                if arg1:
                    # TODO: memory.copy
                if v4:
                    arg1 = load32(v3 + 8)
                store32(v3, v2)
                break
            store32(v3 + 8, (arg1 + 1))
            store32((v2 + (arg1 << 2)), v9)
            if not load32(v8 + 40):
                break
            arg1 = (load16u(v8 + 114) << 5)
            break
        G.global0 = (v6 + 16)
        while True:  # $label21
            if not load32((v5 + (arg0 * 132)) + 92):
                break
            if load32(9140316):
                if (load32(9140320) != load32((v5 + (arg0 * 132)) + 28)):
                    break
            break
        if not load8u(9147141):
            break
        if (load32(9173808) != load32((v5 + (arg0 * 132)) + 28)):
            break
        Ya(1)
        break
    func29(v8, 1)
    return func28(1, 1)

# ----------------------------------------------------------
# $func655
# ----------------------------------------------------------
def func655(arg0, arg1, arg2, arg3, arg4):
    arg3 = 1
    while True:  # $label0
        arg2 = load32(ENTITIES)
        arg4 = load8u(entities[arg0].sub_state)
        if not load32(((load8u(entities[arg0].sub_state) * 404) + ENTITY_TYPES) + 136):
            break
        arg1 = load32(arg1)
        v5 = load8u((arg2 + (load32(arg1) * 132)) + 122)
        if not load32(((load8u((arg2 + (load32(arg1) * 132)) + 122) * 404) + ENTITY_TYPES) + 208):
            if (load32(((arg4 * 404) + ENTITY_TYPES) + 208) == 2):
                break
        while True:  # $label1
            if (u32(load32(9142848)) >= u32((load32(load32(GAME_STATE) + 72) * 2400))):
                break
            arg1 = load32((arg2 + (arg1 * 132)) + 56)
            if not load32((arg2 + (arg1 * 132)) + 56):
                break
            if (arg1 == load16u((arg2 + (arg0 * 132)) + 110)):
                break
            if (load32(38984) != v5):
                break
            break
        arg3 = 0
        break
    return arg3

# ----------------------------------------------------------
# $func656
# ----------------------------------------------------------
def func656(arg0):
    while True:  # $label0
        v8 = load32(ENTITIES)
        v13 = load32(arg0 + 32)
        v1 = entities[load32(arg0 + 32)]
        if not load32(entities[load32(arg0 + 32)].action):
            if (load8u(v1 + 125) != 3):
                break
        while True:  # $label1
            v5 = load8u(v1 + 122)
            if (load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 268) != 3):
                break
            while True:  # $label2
                while True:  # $label3
                    while True:  # $label4
                        v1 = load8u(arg0 + 122)
                        # br_table (load8u(arg0 + 122) + -64)
                        break
                        break
                    if (v1 == 10):
                        break
                    break
                if not load8u(9216060):
                    break
                break
            v9 = load32(9142440)
            v14 = (load32(9142440) + 2)
            v15 = ((load32(9142440) + 2) * load32(((v5 * 404) + ENTITY_TYPES) + 208))
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
                if (u32(v2) < u32(v9)):
                    v1 = (v10 - v2)
                    v20 = ((v10 - v2) * v1)
                    v1 = v18
                    while True:  # $label6
                        while True:  # $label5
                            v3 = v1
                            if (u32(v9) <= u32(v1)):
                                break
                            if ((v2 | v3) < 0):
                                break
                            v1 = (v11 - v3)
                            v7 = (((v11 - v3) * v1) + v20)
                            if ((((v11 - v3) * v1) + v20) >= v6):
                                break
                            v1 = load32((v19 + (((((v3 + v15) + 1) * v14) + v12) << 2)))
                            if not load32((v19 + (((((v3 + v15) + 1) * v14) + v12) << 2))):
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

# ----------------------------------------------------------
# $na
# Export: na
# ----------------------------------------------------------
def na(arg0):
    """Export: na"""
    if (arg0 == 1):
    store32(9561704, 0)
    func344()

# ----------------------------------------------------------
# $qa
# Export: qa
# ----------------------------------------------------------
def qa():
    """Export: qa"""
    v3 = load32(9561728)
    while True:  # $label0
        v1 = load32(9561704)
        if not load32(9561704):
            break
        v4 = load32(v3 + 4)
        v5 = load32(9561696)
        while True:  # $label1
            v6 = ((v0 << 2) + v5)
            if (u32(load32(((v0 << 2) + v5) + 4)) >= u32(v4)):
                break
            v0 = (load32(v6 + 8) + v0)
            if (u32((load32(v6 + 8) + v0)) < u32(v1)):
                continue
            break
        v0 = 0
        break
    store32(9561704, v0)
    if load32(9561732):
        while True:  # $label3
            v5 = load32((v3 + (v2 << 2)))
            while True:  # $label2
                if (load32(9561700) != v0):
                    v1 = load32(9561696)
                    break
                v1 = (load32(9561708) + v0)
                store32(9561700, (load32(9561708) + v0))
                v4 = load32(9561696)
                v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                if v0:
                    # TODO: memory.copy
                if v4:
                    v3 = load32(9561728)
                    v0 = load32(9561704)
                store32(9561696, v1)
                break
            store32(9561704, (v0 + 1))
            store32((v1 + (v0 << 2)), v5)
            v0 = load32(9561704)
            v2 = (v2 + 1)
            if (u32((v2 + 1)) < u32(load32(9561732))):
                continue
            break
    store32(9561828, v0)
    while True:  # $label4
        if (load32(9561700) != v0):
            v2 = load32(9561696)
            break
        v2 = (load32(9561708) + v0)
        store32(9561700, (load32(9561708) + v0))
        v1 = load32(9561696)
        v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
        if v0:
            # TODO: memory.copy
        if v1:
            v3 = load32(9561728)
            v0 = load32(9561704)
        store32(9561696, v2)
        break
    store32(9561704, (v0 + 1))
    store32((v2 + (v0 << 2)), 0)
    v3 = (load32((((load32(9561732) << 2) + v3) - 8)) + 10)
    while True:  # $label5
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
    store32((v1 + (v0 << 2)), v3)
    while True:  # $label6
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
    store32((v2 + (v0 << 2)), 3)
    v2 = load32(9561728)
    if load32(9561728):
        store32(9561728, 0)

# ----------------------------------------------------------
# $pa
# Export: pa
# ----------------------------------------------------------
def pa(arg0):
    """Export: pa"""
    arg0 = (load32(9561836) + arg0)
    store32(9561824, (load32(9561836) + arg0))
    # TODO: i32.div_u
    v3 = 25
    store32((arg0 * 250), 25)
    while True:  # $label1
        while True:  # $label0
            arg0 = load32(59160)
            if (u32(load32(59160)) < u32(v3)):
                if (u32(((v3 - arg0) * 25)) > u32(249)):
                    break
                break
            if (u32(arg0) <= u32(v3)):
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
    while True:  # $label2
        if (load32(9561700) != arg0):
            v2 = load32(9561696)
            break
        v1 = (load32(9561708) + arg0)
        store32(9561700, (load32(9561708) + arg0))
        v4 = load32(9561696)
        v2 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
        if arg0:
            # TODO: memory.copy
        if v4:
            arg0 = load32(9561704)
        store32(9561696, v2)
        break
    store32(9561704, (arg0 + 1))
    store32((v2 + (arg0 << 2)), 0)
    v4 = (v3 + 10)
    while True:  # $label3
        arg0 = load32(9561704)
        if (load32(9561704) != load32(9561700)):
            v1 = v2
            break
        v1 = (load32(9561708) + arg0)
        store32(9561700, (load32(9561708) + arg0))
        v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
        if arg0:
            # TODO: memory.copy
        store32(9561696, v1)
        arg0 = load32(9561704)
        break
    store32(9561704, (arg0 + 1))
    store32((v1 + (arg0 << 2)), v4)
    while True:  # $label4
        arg0 = load32(9561704)
        if (load32(9561704) != load32(9561700)):
            v2 = v1
            break
        v2 = (load32(9561708) + arg0)
        store32(9561700, (load32(9561708) + arg0))
        v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
        if arg0:
            # TODO: memory.copy
        store32(9561696, v2)
        arg0 = load32(9561704)
        break
    store32(9561704, (arg0 + 1))
    store32((v2 + (arg0 << 2)), 3)

# ----------------------------------------------------------
# $func664
# ----------------------------------------------------------
def func664(arg0, arg1, arg2):
    v5 = load32(arg1)
    store32(41092, load32(arg1 + 4))
    store8(9147212, (load32(arg1 + 8) != 0))
    store8(9561848, (load32(arg1 + 12) != 0))
    v3 = load32(PLAYER_COUNT)
    while True:  # $label1
        while True:  # $label0
            if not load8u(9147210):
                if v3:
                    store32(PLAYER_COUNT, 0)
                    arg0 = load32(PLAYERS)
                    if load32(PLAYERS):
                        store32(PLAYERS, 0)
                store32(PLAYER_COUNT, v5)
                store8(9147210, 1)
                v9 = (i32(v5) * 286704)
                arg0 = (-1 if i32(((v9 & 0xFFFFFFFF) >> 32)) else i32((i32(v5) * 286704)))
                arg2 = func26((-1 if i32(((v9 & 0xFFFFFFFF) >> 32)) else i32((i32(v5) * 286704))))
                # TODO: memory.fill
                break
            if (v3 == v5):
                break
            arg0 = 0
            store32(PLAYER_COUNT, v5)
            v9 = (i32(v5) * 286704)
            v7 = (-1 if i32(((v9 & 0xFFFFFFFF) >> 32)) else i32((i32(v5) * 286704)))
            arg2 = func26((-1 if i32(((v9 & 0xFFFFFFFF) >> 32)) else i32((i32(v5) * 286704))))
            # TODO: memory.fill
            v7 = load32(PLAYERS)
            while True:  # $label3
                v3 = (v3 if (u32(v3) < u32(v5)) else v5)
                if (v3 if (u32(v3) < u32(v5)) else v5):
                    if (u32(v3) >= u32(4)):
                        v8 = (v3 & -4)
                        v5 = 0
                        while True:  # $label2
                            v4 = (arg0 * 286704)
                            # TODO: memory.copy
                            v4 = ((arg0 | 1) * 286704)
                            # TODO: memory.copy
                            v4 = ((arg0 | 2) * 286704)
                            # TODO: memory.copy
                            v4 = ((arg0 | 3) * 286704)
                            # TODO: memory.copy
                            arg0 = (arg0 + 4)
                            v5 = (v5 + 4)
                            if ((v5 + 4) != v8):
                                continue
                            break
                    v3 = (v3 & 3)
                    if not (v3 & 3):
                        break
                    v5 = 0
                    while True:  # $label4
                        v8 = (arg0 * 286704)
                        # TODO: memory.copy
                        arg0 = (arg0 + 1)
                        v5 = (v5 + 1)
                        if ((v5 + 1) != v3):
                            continue
                        break
                    break
                if not v7:
                    break
                break
            v5 = load32(PLAYER_COUNT)
            break
        store32(PLAYERS, arg2)
        break
    v7 = 1
    arg0 = load8u(9147212)
    v8 = (v5 if load8u(9147212) else load32(41092))
    if (u32((v5 if load8u(9147212) else load32(41092))) > u32(1)):
        v5 = 4
        while True:  # $label5
            arg2 = (arg1 + (v5 << 2))
            v3 = load32((arg1 + (v5 << 2)) + 12)
            v4 = load32(arg2)
            v6 = load32(arg2 + 4)
            arg0 = players[v7]
            store16(players[v7].team, load32(arg2 + 8))
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

# ----------------------------------------------------------
# $ra
# Export: ra
# ----------------------------------------------------------
def ra(arg0):
    """Export: ra"""
    while True:  # $label4
        while True:  # $label0
            while True:  # $label1
                v1 = load32(9561728)
                if (load32(load32(9561728) + 4) == -1):
                    arg0 = load32(v1 + 8)
                    store32(59164, load32(v1 + 8))
                    if (arg0 == load32(9142384)):
                        break
                    arg0 = 3
                    v4 = load32(9561732)
                    if (u32(load32(9561732)) <= u32(3)):
                        break
                    while True:  # $label3
                        v2 = (v1 + (arg0 << 2))
                        v3 = load32((v1 + (arg0 << 2)) + 4)
                        v5 = (arg0 + 3)
                        v6 = (load32((v1 + (arg0 << 2)) + 4) + (arg0 + 3))
                        v7 = load32(v2 + 8)
                        arg0 = ((load32((v1 + (arg0 << 2)) + 4) + (arg0 + 3)) + load32(v2 + 8))
                        while True:  # $label2
                            v2 = load32(v2)
                            if (u32(load32(v2)) > u32(255)):
                                break
                            v2 = ((v2 << 3) + 9213824)
                            v8 = load32(((v2 << 3) + 9213824))
                            if not load32(((v2 << 3) + 9213824)):
                                break
                            v6 = ((v1 + (v6 << 2)) if v7 else 0)
                            v5 = ((v1 + (v5 << 2)) if v3 else 0)
                            v7 = load32(v2 + 4)
                            if load32(v2 + 4):
                                if not call_table(v7):
                                    break
                            else:
                            break
                        if (u32(arg0) < u32(v4)):
                            continue
                        break
                    store32(59164, 0)
                    v1 = load32(9561728)
                    if load32(9561728):
                        break
                    break
                if load8u(9140304):
                    break
                while True:  # $label5
                    v1 = load32(9561704)
                    if (load32(9561704) != load32(9561700)):
                        v3 = load32(9561696)
                        break
                    v3 = (load32(9561708) + v1)
                    store32(9561700, (load32(9561708) + v1))
                    v2 = load32(9561696)
                    v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                    if v1:
                        # TODO: memory.copy
                    if v2:
                        v1 = load32(9561704)
                    store32(9561696, v3)
                    break
                store32(9561704, (v1 + 1))
                v4 = 2
                store32((v3 + (v1 << 2)), arg0)
                v1 = load32(9561728)
                if (u32(load32(9561732)) > u32(2)):
                    while True:  # $label6
                        v5 = load32((v1 + (v4 << 2)))
                        arg0 = load32(9561704)
                        if (load32(9561704) == load32(9561700)):
                            v2 = (load32(9561708) + arg0)
                            store32(9561700, (load32(9561708) + arg0))
                            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                            if arg0:
                                # TODO: memory.copy
                            store32(9561696, v2)
                            v1 = load32(9561728)
                            v3 = v2
                            arg0 = load32(9561704)
                        store32(9561704, (arg0 + 1))
                        store32((v3 + (arg0 << 2)), v5)
                        v4 = (v4 + 1)
                        if (u32((v4 + 1)) < u32(load32(9561732))):
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

# ----------------------------------------------------------
# $func669
# ----------------------------------------------------------
def func669(arg0, arg1, arg2):
    while True:  # $label0
        v6 = load32(ENTITIES)
        v3 = entities[arg0]
        if (not arg2 & (load8u(entities[arg0].unit_class) == 3)):
            break
        arg2 = load32(v3 + 44)
        v4 = (load32(v3 + 44) << 2)
        v5 = load32(9215884)
        arg2 = load32((load32(9215884) + (arg2 << 4)) + 12)
        while True:  # $label6
            while True:  # $label5
                while True:  # $label4
                    while True:  # $label3
                        while True:  # $label2
                            while True:  # $label1
                                # br_table load32(arg1 + 28)
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
            if not load32((v6 + (arg0 * 132)) + 36):
                break
            break
        while True:  # $label15
            arg0 = 0
            while True:  # $label7
                if not arg2:
                    break
                if (load32(v3 + 28) == arg2):
                    break
                v3 = load32(ENTITIES)
                while True:  # $label8
                    if load32(arg1 + 8):
                        arg0 = load32(arg1 + 104)
                        if not load32(arg1 + 104):
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
                    if (u32(load32(arg1 + 36)) <= u32(3)):
                        while True:  # $label13
                            while True:  # $label12
                                while True:  # $label11
                                    while True:  # $label10
                                        # br_table (arg1 - 1)
                                        break
                                        break
                                    arg0 = 1
                                    while True:  # $label14
                                        arg1 = ((arg2 * 404) + ENTITY_TYPES)
                                        if load32(((arg2 * 404) + ENTITY_TYPES) + 264):
                                            break
                                        if (load32(arg1 + 268) == 1):
                                            break
                                        arg0 = not load32(((arg2 * 404) + ENTITY_TYPES) + 92)
                                        break
                                    arg0 = ((arg0 | (load32(38456) == arg2)) | (load32(38764) == arg2))
                                    break
                                    break
                                arg0 = (load32(((arg2 * 404) + ENTITY_TYPES) + 264) != 0)
                                break
                                break
                            arg0 = (load32(((arg2 * 404) + ENTITY_TYPES) + 264) != 1)
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

# ----------------------------------------------------------
# $func670
# ----------------------------------------------------------
def func670(arg0, arg1, arg2):
    while True:  # $label0
        v4 = load32(ENTITIES)
        if (not arg2 & (load8u(entities[arg0].unit_class) == 3)):
            break
        arg2 = load32(arg1 + 96)
        while True:  # $label4
            while True:  # $label3
                while True:  # $label2
                    while True:  # $label1
                        # br_table load32(arg1 + 36)
                        break
                        break
                    arg1 = (v4 + (arg0 * 132))
                    v3 = load32(arg2)
                    if (load32(arg2) != 2147483647):
                        if (u32(load32(arg1 + 52)) < u32(v3)):
                            break
                    v3 = load32(arg2 + 4)
                    if (load32(arg2 + 4) != 2147483647):
                        if (u32(load32(arg1 + 60)) < u32(v3)):
                            break
                    arg1 = load32(arg2 + 8)
                    v3 = (load32(arg2 + 8) == 2147483647)
                    if not (load32(arg2 + 8) == 2147483647):
                        if (u32(load32((v4 + (arg0 * 132)) + 64)) < u32(arg1)):
                            break
                    if not v3:
                        if (u32(load32((v4 + (arg0 * 132)) + 68)) < u32(load32(arg2 + 12))):
                            break
                    arg1 = load32(arg2 + 16)
                    v3 = (load32(arg2 + 16) == 2147483647)
                    if not (load32(arg2 + 16) == 2147483647):
                        if (u32(load32((v4 + (arg0 * 132)) + 72)) < u32(arg1)):
                            break
                    if not v3:
                        if (u32(load32((v4 + (arg0 * 132)) + 76)) < u32(load32(arg2 + 20))):
                            break
                    arg1 = load32(arg2 + 24)
                    if (load32(arg2 + 24) == 2147483647):
                        break
                    if (u32(load32((v4 + (arg0 * 132)) + 84)) >= u32(arg1)):
                        break
                    break
                    break
                arg1 = (v4 + (arg0 * 132))
                v3 = load32(arg2)
                if (load32(arg2) != 2147483647):
                    if (u32(load32(arg1 + 52)) > u32(v3)):
                        break
                v3 = load32(arg2 + 4)
                if (load32(arg2 + 4) != 2147483647):
                    if (u32(load32(arg1 + 60)) > u32(v3)):
                        break
                arg1 = load32(arg2 + 8)
                v3 = (load32(arg2 + 8) == 2147483647)
                if not (load32(arg2 + 8) == 2147483647):
                    if (u32(load32((v4 + (arg0 * 132)) + 64)) > u32(arg1)):
                        break
                if not v3:
                    if (u32(load32((v4 + (arg0 * 132)) + 68)) > u32(load32(arg2 + 12))):
                        break
                arg1 = load32(arg2 + 16)
                v3 = (load32(arg2 + 16) == 2147483647)
                if not (load32(arg2 + 16) == 2147483647):
                    if (u32(load32((v4 + (arg0 * 132)) + 72)) > u32(arg1)):
                        break
                if not v3:
                    if (u32(load32((v4 + (arg0 * 132)) + 76)) > u32(load32(arg2 + 20))):
                        break
                arg1 = load32(arg2 + 24)
                if (load32(arg2 + 24) == 2147483647):
                    break
                if (u32(load32((v4 + (arg0 * 132)) + 84)) <= u32(arg1)):
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
            if not (load32(arg2 + 8) == 2147483647):
                if (load32((v4 + (arg0 * 132)) + 64) != arg1):
                    break
            if not v3:
                if (load32((v4 + (arg0 * 132)) + 68) != load32(arg2 + 12)):
                    break
            arg1 = load32(arg2 + 16)
            v3 = (load32(arg2 + 16) == 2147483647)
            if not (load32(arg2 + 16) == 2147483647):
                if (load32((v4 + (arg0 * 132)) + 72) != arg1):
                    break
            if not v3:
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

# ----------------------------------------------------------
# $func671
# ----------------------------------------------------------
def func671(arg0, arg1, arg2):
    while True:  # $label0
        v6 = load32(ENTITIES)
        if (not arg2 & (load8u(entities[arg0].unit_class) == 3)):
            break
        while True:  # $label1
            if not load32(arg1 + 8):
                v5 = load32(arg1 + 104)
                if not load32(arg1 + 104):
                    break
                v4 = (v6 + (arg0 * 132))
                arg2 = (load32(arg1 + 28) << 1)
                v9 = ((load32(arg1 + 28) << 1) * arg2)
                v10 = load32(arg1 + 96)
                arg2 = 0
                if load32(arg1 + 36):
                    break
                while True:  # $label3
                    while True:  # $label2
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
            v5 = load32(PLAYER_COUNT)
            if not load32(PLAYER_COUNT):
                break
            v9 = load32(arg1 + 64)
            v10 = (load32(arg1 + 64) + (v5 << 2))
            v4 = (v6 + (arg0 * 132))
            v3 = 1
            arg0 = (load32(arg1 + 28) << 1)
            v7 = ((load32(arg1 + 28) << 1) * arg0)
            arg0 = 0
            v15 = load32(PLAYERS)
            v16 = load32(9142420)
            arg1 = load32(arg1 + 36)
            if (u32(load32(arg1 + 36)) <= u32(3)):
                v12 = load32(38764)
                v13 = load32(38456)
                v11 = (arg1 - 1)
                while True:  # $label13
                    while True:  # $label4
                        arg1 = (arg0 << 2)
                        if not load32((v9 + (arg0 << 2))):
                            if not load32(v10):
                                break
                            if not load32((arg1 + v16)):
                                break
                        arg1 = 0
                        while True:  # $label12
                            while True:  # $label9
                                while True:  # $label8
                                    while True:  # $label5
                                        while True:  # $label6
                                            while True:  # $label7
                                                # br_table v11
                                                break
                                                break
                                            if (load32(((arg1 * 404) + ENTITY_TYPES) + 264) == 1):
                                                break
                                            break
                                            break
                                        if not load32(((arg1 * 404) + ENTITY_TYPES) + 264):
                                            break
                                        break
                                        break
                                    arg2 = ((arg1 * 404) + ENTITY_TYPES)
                                    if load32(((arg1 * 404) + ENTITY_TYPES) + 264):
                                        break
                                    if (load32(arg2 + 268) == 1):
                                        break
                                    if not load32(arg2 + 92):
                                        break
                                    if (arg1 == v13):
                                        break
                                    if (arg1 == v12):
                                        break
                                    break
                                arg2 = load32((((v15 + (arg0 * 286704)) + (arg1 << 2)) + 284636))
                                if not load32((((v15 + (arg0 * 286704)) + (arg1 << 2)) + 284636)):
                                    break
                                v17 = load32(arg2 + 8)
                                if not load32(arg2 + 8):
                                    break
                                v18 = load32(arg2)
                                arg2 = 0
                                while True:  # $label11
                                    while True:  # $label10
                                        v8 = load32((v18 + (arg2 << 2)))
                                        if not load32((v18 + (arg2 << 2))):
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
                    v3 = (u32((arg0 + 1)) < u32(v5))
                    if (arg0 != v5):
                        continue
                    break
                break
            v8 = ((arg1 - 4) << 2)
            while True:  # $label17
                while True:  # $label14
                    arg1 = (arg0 << 2)
                    if not load32((v9 + (arg0 << 2))):
                        if not load32(v10):
                            break
                        if not load32((arg1 + v16)):
                            break
                    arg1 = load32((((v15 + (arg0 * 286704)) + v8) + 284636))
                    if not load32((((v15 + (arg0 * 286704)) + v8) + 284636)):
                        break
                    v12 = load32(arg1 + 8)
                    if not load32(arg1 + 8):
                        break
                    v13 = load32(arg1)
                    arg2 = 0
                    while True:  # $label16
                        while True:  # $label15
                            arg1 = load32((v13 + (arg2 << 2)))
                            if not load32((v13 + (arg2 << 2))):
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
                v3 = (u32((arg0 + 1)) < u32(v5))
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

# ----------------------------------------------------------
# $func672
# ----------------------------------------------------------
def func672(arg0, arg1, arg2):
    while True:  # $label0
        v3 = entities[arg0]
        if (load8u(entities[arg0].unit_class) != 3):
            break
        if arg2:
            break
        return 0
        break
    arg0 = load16u(v3 + 114)
    v5 = load16u(v3 + 112)
    arg2 = load32(arg1 + 20)
    while True:  # $label2
        while True:  # $label4
            while True:  # $label3
                v3 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                v6 = (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 216) - 1)
                if (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 216) - 1):
                    v3 = load32(v3 + 220)
                    while True:  # $label1
                        v7 = (u32(arg2) > u32(v5))
                        if (u32(arg2) > u32(v5)):
                            break
                        if (u32((load32(arg1 + 28) + arg2)) <= u32(v5)):
                            break
                        v8 = load32(arg1 + 24)
                        if (u32(load32(arg1 + 24)) > u32(arg0)):
                            break
                        v4 = 1
                        if (u32((load32(arg1 + 40) + v8)) > u32(arg0)):
                            break
                        break
                    v3 = (v3 - 1)
                    v4 = (v5 + v6)
                    if (u32(arg2) > u32((v5 + v6))):
                        break
                    if (u32((load32(arg1 + 28) + arg2)) <= u32(v4)):
                        break
                    v6 = load32(arg1 + 24)
                    if (u32(arg0) >= u32(load32(arg1 + 24))):
                        v4 = 1
                        if (u32((load32(arg1 + 40) + v6)) > u32(arg0)):
                            break
                    v6 = load32(arg1 + 24)
                    arg0 = (arg0 + v3)
                    if (u32(load32(arg1 + 24)) > u32((arg0 + v3))):
                        break
                    v4 = 1
                    if (u32((load32(arg1 + 40) + v6)) > u32(arg0)):
                        break
                    break
                if (u32(arg2) > u32(v5)):
                    break
                if (u32((load32(arg1 + 28) + arg2)) <= u32(v5)):
                    break
                arg2 = load32(arg1 + 24)
                if (u32(load32(arg1 + 24)) > u32(arg0)):
                    break
                v4 = (u32((load32(arg1 + 40) + arg2)) > u32(arg0))
                break
                break
            arg0 = (arg0 + v3)
            break
        if v7:
            return 0
        if (u32(v5) >= u32((load32(arg1 + 28) + arg2))):
            return 0
        v4 = 0
        arg2 = load32(arg1 + 24)
        if (u32(load32(arg1 + 24)) > u32(arg0)):
            break
        return (u32((load32(arg1 + 40) + arg2)) > u32(arg0))
        break
    return v4

# ----------------------------------------------------------
# $le
# Export: le
# ----------------------------------------------------------
def le(arg0):
    """Export: le"""
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(9142912, arg0)
    v2 = (arg0 << 2)
    v3 = (-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2))
    arg0 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
    # TODO: memory.fill
    store32(9142908, arg0)
    store32(v1 + 12, v2)
    arg0 = load32(9142908)
    G.global0 = (v1 + 16)
    return arg0

# ----------------------------------------------------------
# $ke
# Export: ke
# ----------------------------------------------------------
def ke():
    """Export: ke"""
    v0 = load32(9687204)
    if load32(9687204):
        store32(9687204, 0)
    v0 = load32(9687216)
    v1 = func26(load32(9687216))
    store32(9687204, func26(load32(9687216)))
    store32(9147392, load32(9687216))
    return load32(9687204)

# ----------------------------------------------------------
# $je
# Export: je
# ----------------------------------------------------------
def je(arg0):
    """Export: je"""
    store32(9687216, arg0)
    arg0 = func26(arg0)
    store32(9687212, func26(arg0))
    return arg0

# ----------------------------------------------------------
# $oe
# Export: oe
# ----------------------------------------------------------
def oe(arg0):
    """Export: oe"""
    arg0 = func26(arg0)
    store32(9687232, func26(arg0))
    return arg0

# ----------------------------------------------------------
# $pe
# Export: pe
# ----------------------------------------------------------
def pe(arg0):
    """Export: pe"""
    arg0 = func26(arg0)
    store32(9687236, func26(arg0))
    return arg0

# ----------------------------------------------------------
# $ib
# Export: ib
# ----------------------------------------------------------
def ib(arg0):
    """Export: ib"""
    store32(9681464, arg0)
    v1 = 9681776
    while True:  # $label3
        while True:  # $label0
            while True:  # $label1
                while True:  # $label2
                    # br_table arg0
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
    store32(100, load32(((load32(9681696) * 404) + ENTITY_TYPES) + 68))
    return 9681472

# ----------------------------------------------------------
# $jb
# Export: jb
# ----------------------------------------------------------
def jb(arg0):
    """Export: jb"""
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
    store32(100, load32(((load32((load32(9681476) + (v1 << 2))) * 404) + ENTITY_TYPES) + 68))
    return 9681472

# ----------------------------------------------------------
# $nc
# Export: nc
# ----------------------------------------------------------
def nc():
    """Export: nc"""
    v9 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    if load8u(9684336):
        a_b()
        store8(9684336, 0)
    while True:  # $label0
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
        if not load32(51776):
            break
        if load8u(9215872):
            if load32(9215984):
                v1 = 0
                while True:  # $label1
                    v0 = load32(9215976)
                    v2 = (v1 << 2)
                    v1 = (v1 + 8)
                    if (u32((v1 + 8)) < u32(load32(9215984))):
                        continue
                    break
            v1 = 0
            store32(9215984, 0)
            if load32(9216000):
                while True:  # $label2
                    v0 = (load32(9215992) + (v1 << 2))
                    v1 = (v1 + 3)
                    if (u32((v1 + 3)) < u32(load32(9216000))):
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
                    if (u32((v1 + 2)) < u32(load32(9216016))):
                        continue
                    break
            v1 = 0
            store32(9216016, 0)
            if load32(9216032):
                while True:  # $label4
                    v0 = load32(9216024)
                    v2 = (v1 << 2)
                    v1 = (v1 + 4)
                    if (u32((v1 + 4)) < u32(load32(9216032))):
                        continue
                    break
            store32(9216032, 0)
            store8(9215872, 0)
        v1 = load32(9142848)
        while True:  # $label5
            if not load8u(9147210):
                break
            if not v1:
                break
            if ((v1 * 25) % 250):
                break
            if (u32(v1) <= u32(load32(59148))):
                break
            if (not load8u(9142388) | not load8u(9147125)):
                if (u32(load32(59176)) < u32(v1)):
                    break
            v1 = (G.global0 - 80)
            G.global0 = (G.global0 - 80)
            while True:  # $label6
                if not load32(9561792):
                    break
                while True:  # $label25
                    while True:  # $label7
                        v0 = load32(9561784)
                        v2 = (v10 << 2)
                        v3 = (load32(9561784) + (v10 << 2))
                        v5 = load32((load32(9561784) + (v10 << 2)))
                        if not load32((load32(9561784) + (v10 << 2))):
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
                        while True:  # $label17
                            while True:  # $label12
                                while True:  # $label19
                                    while True:  # $label16
                                        while True:  # $label8
                                            v2 = load32(PLAYER_COUNT)
                                            v4 = (u32(load32(PLAYER_COUNT)) < u32(2))
                                            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                break
                                            v3 = load32(PLAYERS)
                                            v0 = 1
                                            while True:  # $label11
                                                while True:  # $label10
                                                    while True:  # $label9
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
                                            v3 = load32(PLAYERS)
                                            v0 = 1
                                            while True:  # $label18
                                                while True:  # $label14
                                                    while True:  # $label13
                                                        v4 = (v3 + (v0 * 286704))
                                                        if not load32((v3 + (v0 * 286704)) + 283976):
                                                            if load8u(v4 + 286699):
                                                                break
                                                        if load32(v4 + 284616):
                                                            break
                                                        break
                                                    v3 = load32(v4 + 283908)
                                                    v0 = load32(v4 + 281800)
                                                    if load32(v4 + 281800):
                                                        store32((v4 + 281800), 0)
                                                        v2 = load32(PLAYER_COUNT)
                                                    v0 = 1
                                                    if (u32(v2) >= u32(2)):
                                                        while True:  # $label15
                                                            if (v0 != v3):
                                                                func176(v3, v0, 1)
                                                                v2 = load32(PLAYER_COUNT)
                                                            v0 = (v0 + 1)
                                                            if (u32((v0 + 1)) < u32(v2)):
                                                                continue
                                                            break
                                                    v0 = load32(9142384)
                                                    if not v3:
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
                        v0 = players[v3]
                        store32(v1 + 64, players[v3])
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
                            store32(CURRENT_PLAYER, load32(v0 + 283908))
                            v4 = load32(PLAYER_COUNT)
                            if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                                v6 = load32(PLAYERS)
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
                                        v6 = load32(PLAYERS)
                                        v4 = load32(PLAYER_COUNT)
                                    v2 = (v2 + 1)
                                    if (u32((v2 + 1)) < u32(v4)):
                                        continue
                                    break
                            func346()
                            if not load32(v0 + 283976):
                                break
                            while True:  # $label21
                                v0 = load32(((v0 + (load32(9671152) << 2)) + 284636))
                                if not load32(((v0 + (load32(9671152) << 2)) + 284636)):
                                    break
                                v2 = load32(v0 + 8)
                                if not load32(v0 + 8):
                                    break
                                v3 = load32(v0)
                                v0 = 0
                                while True:  # $label22
                                    v4 = load32((v3 + (v0 << 2)))
                                    if not load32((v3 + (v0 << 2))):
                                        v0 = (v0 + 1)
                                        if (v2 != (v0 + 1)):
                                            continue
                                        break
                                    break
                                if load8u(9142917):
                                    break
                                v0 = load32(ENTITIES)
                                v0 = (v0 + (v4 * 132))
                                v2 = load32((v0 + (v4 * 132)) + 36)
                                v0 = entities[(load32((v0 + (v4]
                                v2 = ((load8u(entities[(load32((v0 + (v4].sub_state) * 404) + ENTITY_TYPES)
                                v3 = load32(((load8u(entities[(load32((v0 + (v4].sub_state) * 404) + ENTITY_TYPES) + 220)
                                v4 = load16u(v0 + 114)
                                store32(v1, (((load32(v2 + 216) << 4) & 2147483632) + (load16u(v0 + 112) << 5)))
                                store32(v1 + 4, (((v3 << 4) & 2147483632) + (v4 << 5)))
                                break
                            if not load32(load32(GAME_STATE) + 48):
                                break
                            if load8u(9147152):
                                break
                            v4 = load32(9671136)
                            if (u32(load32(9671136)) < u32(4)):
                                break
                            v6 = load32(ENTITIES)
                            v2 = 3
                            while True:  # $label24
                                while True:  # $label23
                                    v0 = (v6 + (v2 * 132))
                                    if (load8u((v6 + (v2 * 132)) + 125) == 3):
                                        break
                                    if not load32(v0 + 28):
                                        break
                                    if load32(v0 + 36):
                                        break
                                    v4 = load32(9671136)
                                    v6 = load32(ENTITIES)
                                    break
                                v2 = (v2 + 1)
                                if (u32((v2 + 1)) < u32(v4)):
                                    continue
                                break
                            break
                        break
                    v13 = (v13 + (v5 != 0))
                    v10 = (v10 + 8)
                    if (u32((v10 + 8)) < u32(load32(9561792))):
                        continue
                    break
                if v13:
                    break
                store32(9561792, 0)
                break
            G.global0 = (v1 + 80)
            while True:  # $label26
                if load8u(9147125):
                    break
                if not load32(9561776):
                    break
                v1 = load32(9561768)
                while True:  # $label29
                    v3 = (v8 << 2)
                    v5 = load32((v1 + (v8 << 2)))
                    v4 = (load32((v1 + (v8 << 2))) != 0)
                    while True:  # $label27
                        if not v5:
                            break
                        if (load32((v1 + (v3 | 4))) != load32(9142848)):
                            break
                        v6 = load32(PLAYER_COUNT)
                        if (u32(load32(PLAYER_COUNT)) < u32(2)):
                            break
                        v10 = load32(PLAYERS)
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
                    if (u32((v8 + 2)) < u32(load32(9561776))):
                        continue
                    break
                if v7:
                    break
                store32(9561776, 0)
                break
            v1 = load32(59172)
            v0 = (load32(9561696) + (load32(59172) << 2))
            v3 = load32((load32(9561696) + (load32(59172) << 2)) + 8)
            if (u32(load32((load32(9561696) + (load32(59172) << 2)) + 8)) >= u32(4)):
                v1 = 3
                while True:  # $label31
                    v2 = (v0 + (v1 << 2))
                    store32(59164, load32((v0 + (v1 << 2))))
                    v7 = load32(v2 + 8)
                    v5 = (v1 + 4)
                    v8 = (load32(v2 + 8) + (v1 + 4))
                    v4 = load32(v2 + 12)
                    v1 = ((load32(v2 + 8) + (v1 + 4)) + load32(v2 + 12))
                    while True:  # $label30
                        v2 = load32(v2 + 4)
                        if (u32(load32(v2 + 4)) > u32(255)):
                            break
                        v2 = ((v2 << 3) + 9213824)
                        v6 = load32(((v2 << 3) + 9213824))
                        if not load32(((v2 << 3) + 9213824)):
                            break
                        v8 = ((v0 + (v8 << 2)) if v4 else 0)
                        v5 = ((v0 + (v5 << 2)) if v7 else 0)
                        v4 = load32(v2 + 4)
                        if load32(v2 + 4):
                            if not call_table(v4):
                                break
                        else:
                        break
                    store32(59164, 0)
                    if (u32(v1) < u32(v3)):
                        continue
                    break
            else:
            store32(load32(59172), (v1 + v3))
            v1 = load32(9142848)
            break
        while True:  # $label32
            if not load32(9147132):
                break
            if load8u(9684337):
                break
            if (u32(v1) < u32(11)):
                break
            if (u32(load32(59160)) > u32((v1 + 1))):
                break
            a_b()
            store8(9684337, 1)
            if load32(players[load32(CURRENT_PLAYER)].total_resources):
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
        while True:  # $label38
            if not load32(9684288):
                v8 = 0
                v7 = -1
                v0 = (G.global0 - 16)
                G.global0 = (G.global0 - 16)
                store32(v0 + 12, 0)
                func175(9684320)
                v1 = load32(9684308)
                v2 = (load32(9684308) != 0)
                while True:  # $label33
                    if not v1:
                        break
                    while True:  # $label35
                        while True:  # $label34
                            # TODO: i32.atomic.rmw.cmpxchg
                            if 1:
                                store32(v0 + 12, (load32(v0 + 12) + 1))
                                store32(v1 + 16, (v0 + 12))
                                break
                            v8 = (v8 if v8 else v1)
                            v7 = (v7 - 1)
                            break
                        v1 = load32(v1)
                        v2 = (load32(v1) != 0)
                        if not v7:
                            break
                        if v1:
                            continue
                        break
                    break
                while True:  # $label36
                    if v2:
                        v7 = (v1 + 4)
                        v2 = load32(v1 + 4)
                        if not load32(v1 + 4):
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
                # TODO: i32.atomic.rmw.add
                func111(9684296, 2147483647)
            break
        func54(9684264)
        break
    G.global0 = (v9 + 48)
    return 9684296

# ----------------------------------------------------------
# $func688
# ----------------------------------------------------------
def func688(arg0):
    arg0 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    v1 = load32(59160)
    v2 = load32(9142848)
    v53 = (u32((load32(59160) - load32(9142848))) > u32(5))
    if (u32(v1) > u32(v2)):
        while True:  # $label607
            a_b()
            func152()
            if load8u(9140312):
                store32(51776, 1)
                while True:  # $label0
                    if load32(51776):
                        continue
                    break
                func54(9684264)
            v2 = 0
            v4 = 0
            v5 = 0
            v13 = (G.global0 - 112)
            G.global0 = (G.global0 - 112)
            while True:  # $label7
                while True:  # $label2
                    while True:  # $label1
                        v3 = load8u(9147210)
                        if not load8u(9147210):
                            break
                        v1 = load32(9142848)
                        if not load32(9142848):
                            break
                        if not load32(CURRENT_PLAYER):
                            break
                        if ((v1 * 25) % 10000):
                            break
                        v1 = (G.global0 - 32)
                        G.global0 = (G.global0 - 32)
                        while True:  # $label6
                            while True:  # $label3
                                v6 = load32(PLAYER_COUNT)
                                if not load32(PLAYER_COUNT):
                                    break
                                v7 = load32(9682200)
                                v10 = load32(9682204)
                                v9 = load32(CURRENT_PLAYER)
                                v16 = load32(PLAYERS)
                                while True:  # $label5
                                    while True:  # $label4
                                        if not v5:
                                            break
                                        if (v5 == v9):
                                            break
                                        v3 = (v16 + (v5 * 286704))
                                        if not load32((v16 + (v5 * 286704)) + 284616):
                                            break
                                        if load8u(v3 + 286699):
                                            break
                                        if (load32(v3 + 283932) != v10):
                                            break
                                        if (v7 == load32(v3 + 283928)):
                                            v2 = (v2 + 1)
                                            break
                                        v2 = (v2 - 1)
                                        break
                                    v5 = (v5 + 1)
                                    if ((v5 + 1) != v6):
                                        continue
                                    break
                                if (v2 >= 0):
                                    break
                                a_b()
                                store64(v1 + 8, 13)
                                store64(v1, 532575944827)
                                a_b()
                                a_b()
                                break
                                break
                            v2 = cc()
                            store32(9682200, cc())
                            v5 = load32(9142848)
                            store32(9682204, load32(9142848))
                            store32(v1 + 28, v5)
                            store32(v1 + 24, v2)
                            if load8u(9147210):
                                func41(20, 0, 0, (v1 + 24), 2)
                                break
                            break
                        G.global0 = (v1 + 32)
                        v3 = load8u(9147210)
                        break
                    if not (v3 & 255):
                        break
                    break
                if not load8u(9216060):
                    break
                v1 = load32(9142848)
                if not load32(9142848):
                    break
                if ((v1 * 25) % 60000):
                    break
                if not load32(CURRENT_PLAYER):
                    break
                if load8u(9561832):
                    break
                if load8u(9561801):
                    store32(v13 + 80, load32(9142840))
                    v1 = (load32(9142440) + 2)
                    store32(v13 + 84, (((load32(9142440) + 2) * v1) * 3))
                break
            v1 = load32(9568068)
            v2 = load32(9568064)
            if (load32(9568068) != load32(9568064)):
                v1 = ((v1 - v2) >> 7)
                v29 = (1 if (u32(v1) <= u32(1)) else ((v1 - v2) >> 7))
                while True:  # $label114
                    while True:  # $label8
                        v10 = (load32(9568064) + (v4 << 7))
                        if (u32((load32((load32(9568064) + (v4 << 7)) + 108) - 1)) < u32(load32(v10 + 120))):
                            break
                        v1 = load32(9142848)
                        v2 = load32(v10 + 116)
                        if load32(v10 + 116):
                            if ((v1 * 25) % v2):
                                break
                        if v1:
                            if (u32(load32(v10 + 112)) > u32(((v1 - load32(v10 + 124)) * 25))):
                                break
                        v1 = load32(v10 + 4)
                        v5 = load32(v10)
                        v2 = ((load32(v10 + 4) - load32(v10)) // 196)
                        store32(9684388, ((load32(v10 + 4) - load32(v10)) // 196))
                        store32(9140300, 0)
                        store32(9684384, 0)
                        if load32(PLAYER_COUNT):
                            v3 = 0
                            v6 = load32(9142420)
                            while True:  # $label9
                                store32((v6 + (v3 << 2)), 0)
                                v3 = (v3 + 1)
                                if (u32((v3 + 1)) < u32(load32(PLAYER_COUNT))):
                                    continue
                                break
                        while True:  # $label10
                            v5 = (v1 == v5)
                            if (v1 == v5):
                                break
                            v6 = (1 if (u32(v2) <= u32(1)) else v2)
                            v1 = 0
                            v3 = 0
                            while True:  # $label13
                                while True:  # $label12
                                    while True:  # $label11
                                        v7 = (load32(v10) + (v3 * 196))
                                        if not load8u((load32(v10) + (v3 * 196)) + 44):
                                            if not func380(v7):
                                                break
                                        v3 = (v3 + 1)
                                        v1 = (u32((v3 + 1)) >= u32(v2))
                                        if (v3 != v6):
                                            continue
                                        break
                                        break
                                    break
                                v2 = (v1 & 1)
                                v1 = 1
                                if v2:
                                    break
                                v1 = 0
                                store32(9684384, 0)
                                store32(9140300, 0)
                                if not load32(PLAYER_COUNT):
                                    break
                                v2 = load32(9142420)
                                v3 = 0
                                while True:  # $label14
                                    store32((v2 + (v3 << 2)), 0)
                                    v3 = (v3 + 1)
                                    if (u32((v3 + 1)) < u32(load32(PLAYER_COUNT))):
                                        continue
                                    break
                                break
                            if v5:
                                break
                            v3 = 0
                            while True:  # $label15
                                v2 = (load32(v10) + (v3 * 196))
                                if load8u((load32(v10) + (v3 * 196)) + 44):
                                    v1 = (func380(v2) | v1)
                                v3 = (v3 + 1)
                                if ((v3 + 1) != v6):
                                    continue
                                break
                            if not ((v1 | v5) & 1):
                                break
                            break
                        v24 = load32(v10 + 16)
                        v28 = load32(v10 + 12)
                        v1 = ((load32(v10 + 16) - load32(v10 + 12)) // 196)
                        v23 = (1 if (u32(v1) <= u32(1)) else ((load32(v10 + 16) - load32(v10 + 12)) // 196))
                        v5 = 0
                        while True:  # $label113
                            v3 = 0
                            if (v24 != v28):
                                while True:  # $label112
                                    v6 = (load32(v10 + 12) + (v3 * 196))
                                    v1 = 0
                                    v16 = 0
                                    v15 = (G.global0 - 32)
                                    G.global0 = (G.global0 - 32)
                                    while True:  # $label32
                                        while True:  # $label33
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
                                                                                                            # br_table load32(v6)
                                                                                                            break
                                                                                                            break
                                                                                                        v1 = load32(v6 + 32)
                                                                                                        if (load32(v6 + 32) != 2147483646):
                                                                                                            break
                                                                                                        v2 = load32(PLAYER_COUNT)
                                                                                                        if not load32(PLAYER_COUNT):
                                                                                                            break
                                                                                                        v7 = load32(9142420)
                                                                                                        v1 = 0
                                                                                                        while True:  # $label34
                                                                                                            if load32((v7 + (v1 << 2))):
                                                                                                                v7 = load32(9142420)
                                                                                                                v2 = load32(PLAYER_COUNT)
                                                                                                            v1 = (v1 + 1)
                                                                                                            if (u32((v1 + 1)) < u32(v2)):
                                                                                                                continue
                                                                                                            break
                                                                                                        break
                                                                                                        break
                                                                                                    while True:  # $label38
                                                                                                        while True:  # $label37
                                                                                                            while True:  # $label36
                                                                                                                while True:  # $label35
                                                                                                                    # br_table load32(v6 + 4)
                                                                                                                    break
                                                                                                                    break
                                                                                                                func299(v6, 71)
                                                                                                                break
                                                                                                                break
                                                                                                            v2 = load32(v6 + 88)
                                                                                                            if not load32(v6 + 88):
                                                                                                                break
                                                                                                            v7 = load32(ENTITIES)
                                                                                                            while True:  # $label39
                                                                                                                v9 = (v7 + (load32((load32(v6 + 80) + (v1 << 2))) * 132))
                                                                                                                if (load8u((v7 + (load32((load32(v6 + 80) + (v1 << 2))) * 132)) + 125) != 3):
                                                                                                                    func247(v6, v9)
                                                                                                                    v7 = load32(ENTITIES)
                                                                                                                    v2 = load32(v6 + 88)
                                                                                                                v1 = (v1 + 1)
                                                                                                                if (u32((v1 + 1)) < u32(v2)):
                                                                                                                    continue
                                                                                                                break
                                                                                                            break
                                                                                                            break
                                                                                                        v2 = load32(9140300)
                                                                                                        if not load32(9140300):
                                                                                                            break
                                                                                                        v7 = load32(9142420)
                                                                                                        v9 = load32(ENTITIES)
                                                                                                        while True:  # $label40
                                                                                                            v16 = (v9 + (load32(((v1 << 2) + 8451904)) * 132))
                                                                                                            if load32((v7 + (load16u((v9 + (load32(((v1 << 2) + 8451904)) * 132)) + 110) << 2))):
                                                                                                                func247(v6, v16)
                                                                                                                v7 = load32(9142420)
                                                                                                                v9 = load32(ENTITIES)
                                                                                                                v2 = load32(9140300)
                                                                                                            v1 = (v1 + 1)
                                                                                                            if (u32((v1 + 1)) < u32(v2)):
                                                                                                                continue
                                                                                                            break
                                                                                                        break
                                                                                                    break
                                                                                                    break
                                                                                                func123(v6, 72)
                                                                                                break
                                                                                                break
                                                                                            while True:  # $label43
                                                                                                while True:  # $label41
                                                                                                    while True:  # $label42
                                                                                                        # br_table load32(v6 + 4)
                                                                                                        break
                                                                                                        break
                                                                                                    v1 = load32(PLAYER_COUNT)
                                                                                                    if not load32(PLAYER_COUNT):
                                                                                                        break
                                                                                                    while True:  # $label53
                                                                                                        while True:  # $label44
                                                                                                            v2 = load32(v6 + 48)
                                                                                                            v7 = (v16 << 2)
                                                                                                            if not load32((load32(v6 + 48) + (v16 << 2))):
                                                                                                                if not load32((v2 + (v1 << 2))):
                                                                                                                    break
                                                                                                                if not load32((load32(9142420) + v7)):
                                                                                                                    break
                                                                                                            v2 = 0
                                                                                                            v11 = load32(PLAYERS)
                                                                                                            v12 = load32(v6 + 32)
                                                                                                            if (u32(load32(v6 + 32)) <= u32(3)):
                                                                                                                while True:  # $label51
                                                                                                                    while True:  # $label49
                                                                                                                        while True:  # $label48
                                                                                                                            while True:  # $label46
                                                                                                                                while True:  # $label47
                                                                                                                                    while True:  # $label45
                                                                                                                                        # br_table (v12 - 1)
                                                                                                                                        break
                                                                                                                                        break
                                                                                                                                    v1 = ((v2 * 404) + ENTITY_TYPES)
                                                                                                                                    if load32(((v2 * 404) + ENTITY_TYPES) + 264):
                                                                                                                                        break
                                                                                                                                    if (load32(v1 + 268) == 1):
                                                                                                                                        break
                                                                                                                                    if not load32(v1 + 92):
                                                                                                                                        break
                                                                                                                                    if (load32(38456) == v2):
                                                                                                                                        break
                                                                                                                                    if (load32(38764) != v2):
                                                                                                                                        break
                                                                                                                                    break
                                                                                                                                    break
                                                                                                                                if (load32(((v2 * 404) + ENTITY_TYPES) + 264) == 1):
                                                                                                                                    break
                                                                                                                                break
                                                                                                                                break
                                                                                                                            if load32(((v2 * 404) + ENTITY_TYPES) + 264):
                                                                                                                                break
                                                                                                                            break
                                                                                                                        v9 = load32((((v11 + (v16 * 286704)) + (v2 << 2)) + 284636))
                                                                                                                        if not load32((((v11 + (v16 * 286704)) + (v2 << 2)) + 284636)):
                                                                                                                            break
                                                                                                                        v1 = 0
                                                                                                                        v7 = load32(v9 + 8)
                                                                                                                        if not load32(v9 + 8):
                                                                                                                            break
                                                                                                                        while True:  # $label50
                                                                                                                            v14 = load32((load32(v9) + (v1 << 2)))
                                                                                                                            if load32((load32(v9) + (v1 << 2))):
                                                                                                                                v7 = load32(v9 + 8)
                                                                                                                            v1 = (v1 + 1)
                                                                                                                            if (u32((v1 + 1)) < u32(v7)):
                                                                                                                                continue
                                                                                                                            break
                                                                                                                        break
                                                                                                                    v2 = (v2 + 1)
                                                                                                                    if ((v2 + 1) != 255):
                                                                                                                        continue
                                                                                                                    break
                                                                                                                    break
                                                                                                                raise Unreachable()
                                                                                                            v2 = load32((((v11 + (v16 * 286704)) + (v12 << 2)) + 284620))
                                                                                                            if not load32((((v11 + (v16 * 286704)) + (v12 << 2)) + 284620)):
                                                                                                                break
                                                                                                            v1 = 0
                                                                                                            v7 = load32(v2 + 8)
                                                                                                            if not load32(v2 + 8):
                                                                                                                break
                                                                                                            while True:  # $label52
                                                                                                                v9 = load32((load32(v2) + (v1 << 2)))
                                                                                                                if load32((load32(v2) + (v1 << 2))):
                                                                                                                    v7 = load32(v2 + 8)
                                                                                                                v1 = (v1 + 1)
                                                                                                                if (u32((v1 + 1)) < u32(v7)):
                                                                                                                    continue
                                                                                                                break
                                                                                                            break
                                                                                                        v16 = (v16 + 1)
                                                                                                        v1 = load32(PLAYER_COUNT)
                                                                                                        if (u32((v16 + 1)) < u32(load32(PLAYER_COUNT))):
                                                                                                            continue
                                                                                                        break
                                                                                                    break
                                                                                                    break
                                                                                                v2 = load32(v6 + 88)
                                                                                                if not load32(v6 + 88):
                                                                                                    break
                                                                                                v7 = load32(ENTITIES)
                                                                                                while True:  # $label54
                                                                                                    v9 = (v7 + (load32((load32(v6 + 80) + (v1 << 2))) * 132))
                                                                                                    if (load8u((v7 + (load32((load32(v6 + 80) + (v1 << 2))) * 132)) + 125) != 3):
                                                                                                        v7 = load32(ENTITIES)
                                                                                                        v2 = load32(v6 + 88)
                                                                                                    v1 = (v1 + 1)
                                                                                                    if (u32((v1 + 1)) < u32(v2)):
                                                                                                        continue
                                                                                                    break
                                                                                                break
                                                                                                break
                                                                                            v2 = load32(9140300)
                                                                                            if not load32(9140300):
                                                                                                break
                                                                                            v7 = load32(9142420)
                                                                                            v6 = load32(ENTITIES)
                                                                                            while True:  # $label55
                                                                                                v9 = (v6 + (load32(((v1 << 2) + 8451904)) * 132))
                                                                                                if load32((v7 + (load16u((v6 + (load32(((v1 << 2) + 8451904)) * 132)) + 110) << 2))):
                                                                                                    v7 = load32(9142420)
                                                                                                    v6 = load32(ENTITIES)
                                                                                                    v2 = load32(9140300)
                                                                                                v1 = (v1 + 1)
                                                                                                if (u32((v1 + 1)) < u32(v2)):
                                                                                                    continue
                                                                                                break
                                                                                            break
                                                                                            break
                                                                                        func123(v6, 73)
                                                                                        break
                                                                                        break
                                                                                    func123(v6, 74)
                                                                                    break
                                                                                    break
                                                                                func123(v6, 75)
                                                                                break
                                                                                break
                                                                            v2 = load32(PLAYER_COUNT)
                                                                            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                                                break
                                                                            v1 = 1
                                                                            while True:  # $label57
                                                                                while True:  # $label56
                                                                                    v7 = load32(v6 + 48)
                                                                                    v9 = (v1 << 2)
                                                                                    if not load32((load32(v6 + 48) + (v1 << 2))):
                                                                                        if not load32((v7 + (v2 << 2))):
                                                                                            break
                                                                                        if not load32((load32(9142420) + v9)):
                                                                                            break
                                                                                    v7 = players[v1]
                                                                                    if load8u(players[v1] + 286696):
                                                                                        break
                                                                                    if load8u(v7 + 286697):
                                                                                        break
                                                                                    store8((v7 + 286697), 1)
                                                                                    if (load32(v7 + 283908) == load32(CURRENT_PLAYER)):
                                                                                        a_b()
                                                                                    v9 = load32(v7 + 284628)
                                                                                    v2 = load32(v7 + 284616)
                                                                                    store32(v15 + 4, v7)
                                                                                    store32(v15, 119)
                                                                                    store32(v15 + 8, (v2 if v2 else v9))
                                                                                    a_b()
                                                                                    func227()
                                                                                    v2 = load32(PLAYER_COUNT)
                                                                                    break
                                                                                v1 = (v1 + 1)
                                                                                if (u32((v1 + 1)) < u32(v2)):
                                                                                    continue
                                                                                break
                                                                            if (u32(v2) < u32(2)):
                                                                                break
                                                                            v7 = load32(PLAYERS)
                                                                            v1 = 1
                                                                            while True:  # $label58
                                                                                v6 = (v7 + (v1 * 286704))
                                                                                if not load8u((v7 + (v1 * 286704)) + 286697):
                                                                                    v7 = load32(PLAYERS)
                                                                                    v2 = load32(PLAYER_COUNT)
                                                                                v1 = (v1 + 1)
                                                                                if (u32((v1 + 1)) < u32(v2)):
                                                                                    continue
                                                                                break
                                                                            break
                                                                            break
                                                                        v2 = load32(PLAYER_COUNT)
                                                                        if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                                            break
                                                                        v1 = 1
                                                                        while True:  # $label60
                                                                            while True:  # $label59
                                                                                v7 = load32(v6 + 48)
                                                                                v9 = (v1 << 2)
                                                                                if not load32((load32(v6 + 48) + (v1 << 2))):
                                                                                    if not load32((v7 + (v2 << 2))):
                                                                                        break
                                                                                    if not load32((load32(9142420) + v9)):
                                                                                        break
                                                                                v2 = load32(PLAYER_COUNT)
                                                                                break
                                                                            v1 = (v1 + 1)
                                                                            if (u32((v1 + 1)) < u32(v2)):
                                                                                continue
                                                                            break
                                                                        break
                                                                        break
                                                                    v2 = load32(PLAYER_COUNT)
                                                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                                        break
                                                                    v1 = 1
                                                                    while True:  # $label62
                                                                        while True:  # $label61
                                                                            v7 = load32(v6 + 48)
                                                                            v9 = (v1 << 2)
                                                                            if not load32((load32(v6 + 48) + (v1 << 2))):
                                                                                if not load32((v7 + (v2 << 2))):
                                                                                    break
                                                                                if not load32((load32(9142420) + v9)):
                                                                                    break
                                                                            if (load32(players[v1] + 283908) != load32(CURRENT_PLAYER)):
                                                                                break
                                                                            v2 = load32(v6 + 80)
                                                                            store32(v15 + 20, load32(v6 + 88))
                                                                            store32(v15 + 16, v2)
                                                                            a_b()
                                                                            v2 = load32(PLAYER_COUNT)
                                                                            break
                                                                        v1 = (v1 + 1)
                                                                        if (u32((v1 + 1)) < u32(v2)):
                                                                            continue
                                                                        break
                                                                    break
                                                                    break
                                                                v2 = load32(PLAYER_COUNT)
                                                                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                                    break
                                                                v1 = 1
                                                                while True:  # $label70
                                                                    while True:  # $label63
                                                                        v7 = load32(v6 + 48)
                                                                        v9 = (v1 << 2)
                                                                        if not load32((load32(v6 + 48) + (v1 << 2))):
                                                                            if not load32((v7 + (v2 << 2))):
                                                                                break
                                                                            if not load32((load32(9142420) + v9)):
                                                                                break
                                                                        v2 = players[v1]
                                                                        v7 = load32(v6 + 80)
                                                                        while True:  # $label69
                                                                            while True:  # $label68
                                                                                while True:  # $label67
                                                                                    while True:  # $label66
                                                                                        while True:  # $label65
                                                                                            while True:  # $label64
                                                                                                # br_table load32(v6 + 16)
                                                                                                break
                                                                                                break
                                                                                            v9 = load32(v7)
                                                                                            if (load32(v7) != -2147483647):
                                                                                                store32(v2 + 283848, v9)
                                                                                            v9 = load32(v7 + 4)
                                                                                            if (load32(v7 + 4) != -2147483647):
                                                                                                store32((v2 + 283852), v9)
                                                                                            v9 = load32(v7 + 8)
                                                                                            if (load32(v7 + 8) != -2147483647):
                                                                                                store32((v2 + 283856), v9)
                                                                                            v7 = load32(v7 + 12)
                                                                                            if (load32(v7 + 12) == -2147483647):
                                                                                                break
                                                                                            store32((v2 + 283860), v7)
                                                                                            break
                                                                                            break
                                                                                        v9 = load32(v7)
                                                                                        if (load32(v7) != -2147483647):
                                                                                            store32(v2 + 283848, (load32(v2 + 283848) + v9))
                                                                                        v9 = load32(v7 + 4)
                                                                                        if (load32(v7 + 4) != -2147483647):
                                                                                            v16 = (v2 + 283852)
                                                                                            store32((v2 + 283852), (load32(v16) + v9))
                                                                                        v9 = load32(v7 + 8)
                                                                                        if (load32(v7 + 8) != -2147483647):
                                                                                            v16 = (v2 + 283856)
                                                                                            store32((v2 + 283856), (load32(v16) + v9))
                                                                                        v7 = load32(v7 + 12)
                                                                                        if (load32(v7 + 12) == -2147483647):
                                                                                            break
                                                                                        v2 = (v2 + 283860)
                                                                                        store32((v2 + 283860), (load32(v2) + v7))
                                                                                        break
                                                                                        break
                                                                                    v9 = load32(v7)
                                                                                    if (load32(v7) != -2147483647):
                                                                                        store32(v2 + 283848, (load32(v2 + 283848) - v9))
                                                                                    v9 = load32(v7 + 4)
                                                                                    if (load32(v7 + 4) != -2147483647):
                                                                                        v16 = (v2 + 283852)
                                                                                        store32((v2 + 283852), (load32(v16) - v9))
                                                                                    v9 = load32(v7 + 8)
                                                                                    if (load32(v7 + 8) != -2147483647):
                                                                                        v16 = (v2 + 283856)
                                                                                        store32((v2 + 283856), (load32(v16) - v9))
                                                                                    v7 = load32(v7 + 12)
                                                                                    if (load32(v7 + 12) == -2147483647):
                                                                                        break
                                                                                    v2 = (v2 + 283860)
                                                                                    store32((v2 + 283860), (load32(v2) - v7))
                                                                                    break
                                                                                    break
                                                                                v9 = load32(v7)
                                                                                if (load32(v7) != -2147483647):
                                                                                    store32(v2 + 283848, (load32(v2 + 283848) * v9))
                                                                                v9 = load32(v7 + 4)
                                                                                if (load32(v7 + 4) != -2147483647):
                                                                                    v16 = (v2 + 283852)
                                                                                    store32((v2 + 283852), (load32(v16) * v9))
                                                                                v9 = load32(v7 + 8)
                                                                                if (load32(v7 + 8) != -2147483647):
                                                                                    v16 = (v2 + 283856)
                                                                                    store32((v2 + 283856), (load32(v16) * v9))
                                                                                v7 = load32(v7 + 12)
                                                                                if (load32(v7 + 12) == -2147483647):
                                                                                    break
                                                                                v2 = (v2 + 283860)
                                                                                store32((v2 + 283860), (load32(v2) * v7))
                                                                                break
                                                                                break
                                                                            v9 = load32(v7)
                                                                            if (load32(v7) != -2147483647):
                                                                                store32(v2 + 283848, (load32(v2 + 283848) // v9))
                                                                            v9 = load32(v7 + 4)
                                                                            if (load32(v7 + 4) != -2147483647):
                                                                                v16 = (v2 + 283852)
                                                                                store32((v2 + 283852), (load32(v16) // v9))
                                                                            v9 = load32(v7 + 8)
                                                                            if (load32(v7 + 8) != -2147483647):
                                                                                v16 = (v2 + 283856)
                                                                                store32((v2 + 283856), (load32(v16) // v9))
                                                                            v7 = load32(v7 + 12)
                                                                            if (load32(v7 + 12) == -2147483647):
                                                                                break
                                                                            v2 = (v2 + 283860)
                                                                            store32((v2 + 283860), (load32(v2) // v7))
                                                                            break
                                                                        v2 = load32(PLAYER_COUNT)
                                                                        break
                                                                    v1 = (v1 + 1)
                                                                    if (u32((v1 + 1)) < u32(v2)):
                                                                        continue
                                                                    break
                                                                break
                                                                break
                                                            if (u32(load32(v6 + 4)) <= u32(2)):
                                                                func123(v6, 76)
                                                                break
                                                            v2 = load32(PLAYER_COUNT)
                                                            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                                break
                                                            v1 = 1
                                                            while True:  # $label80
                                                                while True:  # $label71
                                                                    v7 = load32(v6 + 48)
                                                                    v9 = (v1 << 2)
                                                                    if not load32((load32(v6 + 48) + (v1 << 2))):
                                                                        if not load32((v7 + (v2 << 2))):
                                                                            break
                                                                        if not load32((load32(9142420) + v9)):
                                                                            break
                                                                    v12 = 0
                                                                    v16 = players[v1]
                                                                    if not load32(players[v1] + 286680):
                                                                        v2 = func26(16)
                                                                        store32(func26(16) + 4, 16)
                                                                        store32(v2, func26(64))
                                                                        store64(v2 + 8, 4294967296)
                                                                        store32(v16 + 286680, v2)
                                                                        while True:  # $label73
                                                                            while True:  # $label72
                                                                                v2 = load32(v16 + 286680)
                                                                                v7 = load32(load32(v16 + 286680) + 8)
                                                                                if (load32(load32(v16 + 286680) + 8) != load32(v2 + 4)):
                                                                                    v9 = load32(v2)
                                                                                    break
                                                                                v9 = (load32(v2 + 12) + v7)
                                                                                store32(v2 + 4, (load32(v2 + 12) + v7))
                                                                                v11 = load32(v2)
                                                                                v9 = func26((-1 if (u32(v9) > u32(1073741823)) else (v9 << 2)))
                                                                                if v7:
                                                                                    # TODO: memory.copy
                                                                                if v11:
                                                                                    v7 = load32(v2 + 8)
                                                                                store32(v2, v9)
                                                                                break
                                                                            store32(v2 + 8, (v7 + 1))
                                                                            store32((v9 + (v7 << 2)), 0)
                                                                            v12 = (v12 + 1)
                                                                            if ((v12 + 1) != 16):
                                                                                continue
                                                                            break
                                                                    v7 = load32(v16 + 286680)
                                                                    v2 = load32(v6 + 8)
                                                                    if (u32(load32(v6 + 8)) >= u32(16777216)):
                                                                        v2 = load32(((load32(v7) + (v2 << 2)) - 67108864))
                                                                    v9 = load32(v6 + 36)
                                                                    while True:  # $label79
                                                                        while True:  # $label78
                                                                            while True:  # $label77
                                                                                while True:  # $label76
                                                                                    while True:  # $label75
                                                                                        while True:  # $label74
                                                                                            # br_table load32(v6 + 28)
                                                                                            break
                                                                                            break
                                                                                        store32((load32(v7) + (v9 << 2)), v2)
                                                                                        break
                                                                                        break
                                                                                    v7 = (load32(v7) + (v9 << 2))
                                                                                    store32((load32(v7) + (v9 << 2)), (load32(v7) + v2))
                                                                                    break
                                                                                    break
                                                                                v7 = (load32(v7) + (v9 << 2))
                                                                                store32((load32(v7) + (v9 << 2)), (load32(v7) - v2))
                                                                                break
                                                                                break
                                                                            v7 = (load32(v7) + (v9 << 2))
                                                                            store32((load32(v7) + (v9 << 2)), (load32(v7) * v2))
                                                                            break
                                                                            break
                                                                        v7 = (load32(v7) + (v9 << 2))
                                                                        # TODO: i32.div_u
                                                                        store32(load32(v7), v2)
                                                                        break
                                                                    v2 = load32(PLAYER_COUNT)
                                                                    break
                                                                v1 = (v1 + 1)
                                                                if (u32((v1 + 1)) < u32(v2)):
                                                                    continue
                                                                break
                                                            break
                                                            break
                                                        v2 = load32(PLAYER_COUNT)
                                                        if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                            break
                                                        v1 = 1
                                                        while True:  # $label90
                                                            while True:  # $label81
                                                                v7 = load32(v6 + 48)
                                                                v9 = (v1 << 2)
                                                                if not load32((load32(v6 + 48) + (v1 << 2))):
                                                                    if not load32((v7 + (v2 << 2))):
                                                                        break
                                                                    if not load32((load32(9142420) + v9)):
                                                                        break
                                                                v12 = players[v1]
                                                                v16 = 0
                                                                v7 = load32(v6 + 88)
                                                                if load32(v6 + 88):
                                                                    while True:  # $label89
                                                                        while True:  # $label82
                                                                            v18 = (v16 << 2)
                                                                            if not load32(((v16 << 2) + load32(v6 + 80))):
                                                                                break
                                                                            if (u32(v16) > u32(254)):
                                                                                break
                                                                            if load32(((v12 + v18) + 282828)):
                                                                                v9 = ((v16 * 404) + 9568164)
                                                                                v14 = 0
                                                                                while True:  # $label88
                                                                                    while True:  # $label83
                                                                                        v17 = load32(((v12 + (v14 << 2)) + 284636))
                                                                                        if not load32(((v12 + (v14 << 2)) + 284636)):
                                                                                            break
                                                                                        v20 = 0
                                                                                        if not load32(v17 + 8):
                                                                                            break
                                                                                        while True:  # $label87
                                                                                            while True:  # $label84
                                                                                                v2 = load32((load32(v17) + (v20 << 2)))
                                                                                                if not load32((load32(v17) + (v20 << 2))):
                                                                                                    break
                                                                                                v26 = load32(9215884)
                                                                                                v11 = entities[v2]
                                                                                                v2 = load32(entities[v2].target_x)
                                                                                                if (load32((load32(9215884) + (load32(entities[v2].target_x) << 4)) + 4) != 5):
                                                                                                    break
                                                                                                if (load32((v26 + ((v2 << 4) | 12))) != v16):
                                                                                                    break
                                                                                                store8(v11 + 125, 0)
                                                                                                v2 = players[load16u(v11 + 110)]
                                                                                                store32(((players[load16u(v11 + 110)] + v18) + 282828), 0)
                                                                                                v7 = load32(v2 + 283848)
                                                                                                if (load32(v2 + 283848) != 2147483647):
                                                                                                    store32((v2 + 283848), (load32(v9) + v7))
                                                                                                v7 = (v2 + 283852)
                                                                                                v21 = load32((v2 + 283852))
                                                                                                if (load32((v2 + 283852)) != 2147483647):
                                                                                                    store32(v7, (load32(v9 + 4) + v21))
                                                                                                v7 = (v2 + 283856)
                                                                                                v21 = load32((v2 + 283856))
                                                                                                if (load32((v2 + 283856)) != 2147483647):
                                                                                                    store32(v7, (load32(v9 + 8) + v21))
                                                                                                v7 = (v2 + 283860)
                                                                                                v21 = load32((v2 + 283860))
                                                                                                if (load32((v2 + 283860)) != 2147483647):
                                                                                                    store32(v7, (load32(v9 + 12) + v21))
                                                                                                v7 = (v2 + 281692)
                                                                                                store32((v2 + 281692), (load32(v7) - load32(v9)))
                                                                                                v7 = (v2 + 281696)
                                                                                                store32((v2 + 281696), (load32(v7) - load32(v9 + 4)))
                                                                                                v7 = (v2 + 281700)
                                                                                                store32((v2 + 281700), (load32(v7) - load32(v9 + 8)))
                                                                                                v7 = load32(v9 + 12)
                                                                                                store8(v2 + 286701, 1)
                                                                                                v21 = (v2 + 281704)
                                                                                                store32((v2 + 281704), (load32(v21) - v7))
                                                                                                while True:  # $label85
                                                                                                    v21 = load32(PLAYER_COUNT)
                                                                                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                                                                        break
                                                                                                    v7 = 1
                                                                                                    v40 = (v21 - 1)
                                                                                                    v43 = ((v21 - 1) & 1)
                                                                                                    v2 = (load32(v2 + 283908) * v21)
                                                                                                    v8 = load32(PLAYERS)
                                                                                                    v19 = load32(9143016)
                                                                                                    if (v21 != 2):
                                                                                                        v40 = (v40 & -2)
                                                                                                        v21 = 0
                                                                                                        while True:  # $label86
                                                                                                            if load8u((v19 + (v2 + v7))):
                                                                                                                store8((v8 + (v7 * 286704)) + 286701, 1)
                                                                                                            v30 = (v7 + 1)
                                                                                                            if load8u((v19 + ((v7 + 1) + v2))):
                                                                                                                store8((v8 + (v30 * 286704)) + 286701, 1)
                                                                                                            v7 = (v7 + 2)
                                                                                                            v21 = (v21 + 2)
                                                                                                            if ((v21 + 2) != v40):
                                                                                                                continue
                                                                                                            break
                                                                                                    if not v43:
                                                                                                        break
                                                                                                    if not load8u((v19 + (v2 + v7))):
                                                                                                        break
                                                                                                    store8((v8 + (v7 * 286704)) + 286701, 1)
                                                                                                    break
                                                                                                v2 = load32(v11 + 44)
                                                                                                if load32(v11 + 44):
                                                                                                    store32((v26 + (v2 << 4)), 0)
                                                                                                store32(v11 + 44, 0)
                                                                                                if not load32(v11 + 92):
                                                                                                    break
                                                                                                v2 = load8u(9147141)
                                                                                                if load32(9140316):
                                                                                                    if (load32(9140320) != load32(v11 + 28)):
                                                                                                        break
                                                                                                break
                                                                                            v20 = (v20 + 1)
                                                                                            if (u32((v20 + 1)) < u32(load32(v17 + 8))):
                                                                                                continue
                                                                                            break
                                                                                        break
                                                                                    v14 = (v14 + 1)
                                                                                    if ((v14 + 1) != 255):
                                                                                        continue
                                                                                    break
                                                                            func238(v16, load32(v12 + 283908), 0)
                                                                            v7 = load32(v6 + 88)
                                                                            break
                                                                        v16 = (v16 + 1)
                                                                        if (u32((v16 + 1)) < u32(v7)):
                                                                            continue
                                                                        break
                                                                v2 = load32(PLAYER_COUNT)
                                                                break
                                                            v1 = (v1 + 1)
                                                            if (u32((v1 + 1)) < u32(v2)):
                                                                continue
                                                            break
                                                        break
                                                        break
                                                    v2 = load32(PLAYER_COUNT)
                                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                        break
                                                    v1 = 1
                                                    while True:  # $label103
                                                        while True:  # $label91
                                                            v7 = load32(v6 + 48)
                                                            v9 = (v1 << 2)
                                                            if not load32((load32(v6 + 48) + (v1 << 2))):
                                                                if not load32((v7 + (v2 << 2))):
                                                                    break
                                                                if not load32((load32(9142420) + v9)):
                                                                    break
                                                            v11 = players[v1]
                                                            v16 = (G.global0 - 32)
                                                            G.global0 = (G.global0 - 32)
                                                            while True:  # $label92
                                                                if (load32(v6 + 88) != 7):
                                                                    break
                                                                v2 = load32(PLAYER_COUNT)
                                                                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                                    break
                                                                v7 = 1
                                                                while True:  # $label102
                                                                    while True:  # $label93
                                                                        v9 = load32(v6 + 64)
                                                                        v12 = (v7 << 2)
                                                                        if not load32((load32(v6 + 64) + (v7 << 2))):
                                                                            if not load32((v9 + (v2 << 2))):
                                                                                break
                                                                            if not load32((load32(9142420) + v12)):
                                                                                break
                                                                        v12 = load32(v11 + 283908)
                                                                        if (load32(v11 + 283908) == v7):
                                                                            break
                                                                        while True:  # $label94
                                                                            v9 = load32(v6 + 80)
                                                                            v14 = load32(load32(v6 + 80))
                                                                            if (load32(load32(v6 + 80)) == 2147483647):
                                                                                break
                                                                            v17 = load32(9143004)
                                                                            v20 = (load32(9143004) + (v12 + (v2 * v7)))
                                                                            if (v14 == load8u((load32(9143004) + (v12 + (v2 * v7))))):
                                                                                break
                                                                            v9 = (v14 != 0)
                                                                            store8(v20, (v14 != 0))
                                                                            store8((v17 + ((v2 * v12) + v7)), v9)
                                                                            la()
                                                                            v9 = load32(v6 + 80)
                                                                            break
                                                                        while True:  # $label95
                                                                            v2 = load32(v9 + 4)
                                                                            if (load32(v9 + 4) == 2147483647):
                                                                                break
                                                                            v12 = load32(v11 + 283908)
                                                                            if (v2 == load8u((load32(9143012) + (load32(v11 + 283908) + (load32(PLAYER_COUNT) * v7))))):
                                                                                break
                                                                            func414(3, v2, v7, v12, 1)
                                                                            v9 = load32(v6 + 80)
                                                                            break
                                                                        while True:  # $label96
                                                                            v2 = load32(v9 + 8)
                                                                            if (load32(v9 + 8) == 2147483647):
                                                                                break
                                                                            v12 = load32(v11 + 283908)
                                                                            if (load32(v11 + 283908) == v7):
                                                                                break
                                                                            v14 = load32(PLAYER_COUNT)
                                                                            if (u32(load32(PLAYER_COUNT)) <= u32(v7)):
                                                                                break
                                                                            v14 = (load32(9143008) + ((v12 * v14) + v7))
                                                                            if (v2 == load8u((load32(9143008) + ((v12 * v14) + v7)))):
                                                                                break
                                                                            if load32(9147132):
                                                                                if (load32(9142440) == 4096):
                                                                                    break
                                                                            store8(v14, (v2 != 0))
                                                                            if (load32(CURRENT_PLAYER) != v7):
                                                                                break
                                                                            v9 = players[v12]
                                                                            v14 = load32(players[v12] + 284628)
                                                                            v12 = load32(v9 + 284616)
                                                                            store32(v16 + 16, (450 if v2 else 532))
                                                                            store32(v16 + 20, v9)
                                                                            store32(v16 + 24, (v12 if v12 else v14))
                                                                            a_b()
                                                                            v9 = load32(v6 + 80)
                                                                            break
                                                                        while True:  # $label98
                                                                            v2 = load32(v9 + 12)
                                                                            if (load32(v9 + 12) == 2147483647):
                                                                                while True:  # $label97
                                                                                    if (load32(v9 + 16) != 2147483647):
                                                                                        break
                                                                                    if (load32(v9 + 20) != 2147483647):
                                                                                        break
                                                                                    if (load32(v9 + 24) == 2147483647):
                                                                                        break
                                                                                    break
                                                                                v17 = load32(PLAYER_COUNT)
                                                                                v12 = load32(v11 + 283908)
                                                                                v20 = (load32(9143016) + ((load32(PLAYER_COUNT) * load32(v11 + 283908)) + v7))
                                                                                v14 = load8u((load32(9143016) + ((load32(PLAYER_COUNT) * load32(v11 + 283908)) + v7)))
                                                                                break
                                                                            v17 = load32(PLAYER_COUNT)
                                                                            v12 = load32(v11 + 283908)
                                                                            v20 = (load32(9143016) + ((load32(PLAYER_COUNT) * load32(v11 + 283908)) + v7))
                                                                            v14 = load8u((load32(9143016) + ((load32(PLAYER_COUNT) * load32(v11 + 283908)) + v7)))
                                                                            if v2:
                                                                                break
                                                                            break
                                                                        v2 = (v14 & 254)
                                                                        while True:  # $label99
                                                                            v21 = load32(v9 + 16)
                                                                            if (load32(v9 + 16) == 2147483647):
                                                                                break
                                                                            if not v21:
                                                                                v2 = (v2 & 253)
                                                                                break
                                                                            v2 = (v2 | 2)
                                                                            break
                                                                        while True:  # $label100
                                                                            v21 = load32(v9 + 20)
                                                                            if (load32(v9 + 20) == 2147483647):
                                                                                break
                                                                            if not v21:
                                                                                v2 = (v2 & 251)
                                                                                break
                                                                            v2 = (v2 | 4)
                                                                            break
                                                                        while True:  # $label101
                                                                            v9 = load32(v9 + 24)
                                                                            if (load32(v9 + 24) == 2147483647):
                                                                                break
                                                                            if not v9:
                                                                                v2 = (v2 & 247)
                                                                                break
                                                                            v2 = (v2 | 8)
                                                                            break
                                                                        if (v7 == v12):
                                                                            break
                                                                        if (u32(v7) >= u32(v17)):
                                                                            break
                                                                        if (v2 == v14):
                                                                            break
                                                                        v9 = load32(GAME_STATE)
                                                                        if load32(load32(GAME_STATE) + 180):
                                                                            if (u32(load32(9142848)) < u32((load32(v9 + 72) * 2400))):
                                                                                break
                                                                        if load32(9147132):
                                                                            if (load32(9142440) == 4096):
                                                                                break
                                                                        store8(v20, v2)
                                                                        v9 = load32(PLAYERS)
                                                                        store8(players[v7] + 286701, 1)
                                                                        if (load32(CURRENT_PLAYER) != v7):
                                                                            break
                                                                        v9 = (v9 + (v12 * 286704))
                                                                        v14 = load32((v9 + (v12 * 286704)) + 284628)
                                                                        v12 = load32(v9 + 284616)
                                                                        store32(v16 + 4, v9)
                                                                        store32(v16, v2)
                                                                        store32(v16 + 8, (v12 if v12 else v14))
                                                                        a_b()
                                                                        break
                                                                    v7 = (v7 + 1)
                                                                    v2 = load32(PLAYER_COUNT)
                                                                    if (u32((v7 + 1)) < u32(load32(PLAYER_COUNT))):
                                                                        continue
                                                                    break
                                                                break
                                                            G.global0 = (v16 + 32)
                                                            v2 = load32(PLAYER_COUNT)
                                                            break
                                                        v1 = (v1 + 1)
                                                        if (u32((v1 + 1)) < u32(v2)):
                                                            continue
                                                        break
                                                    break
                                                    break
                                                func123(v6, 77)
                                                break
                                                break
                                            v2 = load32(PLAYER_COUNT)
                                            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                                break
                                            v7 = load32(PLAYERS)
                                            v11 = load32(9142420)
                                            v16 = load32(v6 + 48)
                                            v1 = 1
                                            while True:  # $label111
                                                while True:  # $label104
                                                    v9 = (v1 << 2)
                                                    if not load32((v16 + (v1 << 2))):
                                                        if not load32((v16 + (v2 << 2))):
                                                            break
                                                        if not load32((v9 + v11)):
                                                            break
                                                    v2 = load32(v6 + 32)
                                                    v9 = load32(v6 + 28)
                                                    while True:  # $label110
                                                        while True:  # $label109
                                                            while True:  # $label108
                                                                while True:  # $label107
                                                                    while True:  # $label106
                                                                        while True:  # $label105
                                                                            # br_table load32(v6 + 16)
                                                                            break
                                                                            break
                                                                        store32((((v7 + (v1 * 286704)) + (v9 << 2)) + 283984), v2)
                                                                        break
                                                                        break
                                                                    v9 = (((v7 + (v1 * 286704)) + (v9 << 2)) + 283984)
                                                                    store32((((v7 + (v1 * 286704)) + (v9 << 2)) + 283984), (load32(v9) + v2))
                                                                    break
                                                                    break
                                                                v9 = (((v7 + (v1 * 286704)) + (v9 << 2)) + 283984)
                                                                store32((((v7 + (v1 * 286704)) + (v9 << 2)) + 283984), (load32(v9) - v2))
                                                                break
                                                                break
                                                            v9 = (((v7 + (v1 * 286704)) + (v9 << 2)) + 283984)
                                                            store32((((v7 + (v1 * 286704)) + (v9 << 2)) + 283984), (load32(v9) * v2))
                                                            break
                                                            break
                                                        v9 = (((v7 + (v1 * 286704)) + (v9 << 2)) + 283984)
                                                        # TODO: i32.div_u
                                                        store32(load32(v9), v2)
                                                        break
                                                    v2 = load32(PLAYER_COUNT)
                                                    break
                                                v1 = (v1 + 1)
                                                if (u32((v1 + 1)) < u32(v2)):
                                                    continue
                                                break
                                            break
                                            break
                                        break
                                    G.global0 = (v15 + 32)
                                    v3 = (v3 + 1)
                                    if ((v3 + 1) != v23):
                                        continue
                                    break
                            v1 = (load32(v10 + 120) + 1)
                            store32(v10 + 120, (load32(v10 + 120) + 1))
                            v5 = (v5 + 1)
                            if (u32((v5 + 1)) < u32(load32(9684384))):
                                if (u32((load32(v10 + 108) - 1)) >= u32(v1)):
                                    continue
                            break
                        store32(v10 + 124, load32(9142848))
                        break
                    v4 = (v4 + 1)
                    if ((v4 + 1) != v29):
                        continue
                    break
            while True:  # $label115
                v4 = load32(PLAYER_COUNT)
                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                    break
                v3 = load32(9142848)
                v14 = (load32(load32(GAME_STATE) + 120) - 1)
                v10 = 1
                while True:  # $label165
                    v6 = players[v10]
                    while True:  # $label116
                        if not v3:
                            break
                        while True:  # $label119
                            while True:  # $label118
                                while True:  # $label117
                                    # br_table v14
                                    break
                                    break
                                if not ((v3 * 25) % 1000):
                                    break
                                break
                                break
                            if ((v3 * 25) % 60000):
                                break
                            break
                        store8(v6 + 286701, 1)
                        while True:  # $label120
                            if (u32(v4) < u32(2)):
                                break
                            v3 = 1
                            v1 = (v4 - 1)
                            v9 = ((v4 - 1) & 1)
                            v2 = (load32(v6 + 283908) * v4)
                            v5 = load32(PLAYERS)
                            v7 = load32(9143016)
                            if (v4 != 2):
                                v4 = (v1 & -2)
                                v1 = 0
                                while True:  # $label121
                                    if load8u((v7 + (v2 + v3))):
                                        store8((v5 + (v3 * 286704)) + 286701, 1)
                                    v16 = (v3 + 1)
                                    if load8u((v7 + ((v3 + 1) + v2))):
                                        store8((v5 + (v16 * 286704)) + 286701, 1)
                                    v3 = (v3 + 2)
                                    v1 = (v1 + 2)
                                    if ((v1 + 2) != v4):
                                        continue
                                    break
                            if not v9:
                                break
                            if not load8u((v7 + (v2 + v3))):
                                break
                            store8((v5 + (v3 * 286704)) + 286701, 1)
                            break
                        v1 = load32(GAME_STATE)
                        store32(v6 + 283848, (load32(v6 + 283848) + load32(load32(GAME_STATE) + 100)))
                        v2 = (v6 + 283852)
                        store32((v6 + 283852), (load32(v2) + load32(v1 + 104)))
                        v2 = (v6 + 283856)
                        store32((v6 + 283856), (load32(v2) + load32(v1 + 108)))
                        v2 = (v6 + 283860)
                        store32((v6 + 283860), (load32(v2) + load32(v1 + 112)))
                        break
                    if load8u(v6 + 286700):
                        v7 = (v6 + 286700)
                        while True:  # $label122
                            v1 = load32(v6 + 281788)
                            if not load32(v6 + 281788):
                                break
                            v3 = load32(v1 + 8)
                            if not load32(v1 + 8):
                                break
                            v9 = (v6 + 281788)
                            v2 = (v1 + 8)
                            v16 = (v6 + 284000)
                            v15 = (v6 + 284136)
                            v11 = (v6 + 283980)
                            v12 = (v6 + 283976)
                            while True:  # $label125
                                v5 = load32(v12)
                                if (u32(load32(v12)) >= u32((load32(v15) + load32(v11)))):
                                    break
                                if (u32(v5) >= u32(load32(v16))):
                                    break
                                v5 = load32(v1)
                                v4 = load32(load32(v1))
                                v17 = (v3 - 1)
                                store32(v2, (v3 - 1))
                                v3 = 0
                                if v17:
                                    while True:  # $label123
                                        v3 = (v3 + 1)
                                        store32((v5 + (v3 << 2)), load32((v5 + ((v3 + 1) << 2))))
                                        if (u32(v3) < u32(load32(v2))):
                                            continue
                                        break
                                while True:  # $label124
                                    v2 = entities[v4]
                                    v5 = load8u(entities[v4].unit_class)
                                    if (load8u(entities[v4].unit_class) == 3):
                                        break
                                    v3 = load32(v2 + 20)
                                    if not load32(v2 + 20):
                                        break
                                    if not load32(v3 + 8):
                                        break
                                    if (v5 != 7):
                                        break
                                    store8(v2 + 125, 6)
                                    v1 = load32(v9)
                                    break
                                v2 = (v1 + 8)
                                v3 = load32(v1 + 8)
                                if load32(v1 + 8):
                                    continue
                                break
                            break
                        store8(v7, 0)
                    if load8u(v6 + 286701):
                        v2 = 0
                        v5 = (G.global0 - 80)
                        G.global0 = (G.global0 - 80)
                        while True:  # $label126
                            v1 = load32(v6 + 281796)
                            if not load32(v6 + 281796):
                                break
                            if not load32(v1 + 8):
                                break
                            while True:  # $label138
                                v1 = (load32(v1) + (v2 << 2))
                                v3 = entities[load32((load32(v1) + (v2 << 2)))]
                                while True:  # $label127
                                    v9 = load32(v1 + 4)
                                    if (load32(v1 + 4) == -1):
                                        v4 = load8u(v3 + 122)
                                        v1 = load32(((v6 + (load8u(v3 + 122) * 36)) + 269376))
                                        v1 = (load32(((v6 + (load8u(v3 + 122) * 36)) + 269376)) if v1 else 100)
                                        v4 = ((v4 * 404) + ENTITY_TYPES)
                                        v7 = ((load32(((v6 + (load8u(v3 + 122) * 36)) + 269376)) if v1 else 100) * load32(((v4 * 404) + ENTITY_TYPES) + 68))
                                        v9 = (((load32(((v6 + (load8u(v3 + 122) * 36)) + 269376)) if v1 else 100) * load32(((v4 * 404) + ENTITY_TYPES) + 68)) // 100)
                                        store32(v5 + 48, (((load32(((v6 + (load8u(v3 + 122) * 36)) + 269376)) if v1 else 100) * load32(((v4 * 404) + ENTITY_TYPES) + 68)) // 100))
                                        v16 = (load32(v4 + 72) * v1)
                                        v15 = ((load32(v4 + 72) * v1) // 100)
                                        store32(v5 + 52, ((load32(v4 + 72) * v1) // 100))
                                        v11 = (load32(v4 + 76) * v1)
                                        v12 = ((load32(v4 + 76) * v1) // 100)
                                        store32(v5 + 56, ((load32(v4 + 76) * v1) // 100))
                                        v1 = (load32(v4 + 80) * v1)
                                        v4 = ((load32(v4 + 80) * v1) // 100)
                                        store32(v5 + 60, ((load32(v4 + 80) * v1) // 100))
                                        if (u32((v7 - 100)) <= u32(-200)):
                                            if (load32(v5 + 64) < v9):
                                                break
                                        if (u32((v16 - 100)) <= u32(-200)):
                                            if (load32(v5 + 68) < v15):
                                                break
                                        if (u32((v11 - 100)) <= u32(-200)):
                                            if (load32(v5 + 72) < v12):
                                                break
                                        if (u32((v1 - 100)) <= u32(-200)):
                                            if (load32(v5 + 76) < v4):
                                                break
                                        if func66(v6, (v5 + 48), 1, 1):
                                            break
                                        store8(v3 + 125, 4)
                                        while True:  # $label128
                                            v1 = load32(v3 + 40)
                                            if not load32(v3 + 40):
                                                break
                                            if not load8u(9142916):
                                                break
                                            v4 = load32(v3 + 92)
                                            store32(v5 + 36, v1)
                                            store32(v5 + 32, ((v4 != 0) | 1024))
                                            a_b()
                                            v1 = load32(v3 + 40)
                                            break
                                        store8(v3 + 127, 0)
                                        while True:  # $label129
                                            if not v1:
                                                break
                                            if load8u(9142916):
                                                store32(v5 + 20, v1)
                                                store32(v5 + 16, 0)
                                                a_b()
                                                break
                                            v3 = load16u(v3 + 110)
                                            store32(v5 + 4, v1)
                                            store32(v5, (v3 + 16))
                                            a_b()
                                            break
                                        v3 = load32(v6 + 281796)
                                        v4 = (load32(v3 + 8) - 1)
                                        store32(load32(v6 + 281796) + 8, (load32(v3 + 8) - 1))
                                        if (u32(v2) < u32(v4)):
                                            v7 = load32(v3)
                                            v1 = v2
                                            while True:  # $label130
                                                v1 = (v1 + 1)
                                                store32((v7 + (v1 << 2)), load32((v7 + ((v1 + 1) << 2))))
                                                v4 = load32(v3 + 8)
                                                if (u32(v1) < u32(load32(v3 + 8))):
                                                    continue
                                                break
                                        v1 = (v4 - 1)
                                        store32(v3 + 8, (v4 - 1))
                                        if (u32(v1) > u32(v2)):
                                            v4 = load32(v3)
                                            v1 = v2
                                            while True:  # $label131
                                                v1 = (v1 + 1)
                                                store32((v4 + (v1 << 2)), load32((v4 + ((v1 + 1) << 2))))
                                                if (u32(v1) < u32(load32(v3 + 8))):
                                                    continue
                                                break
                                        v2 = (v2 - 2)
                                        break
                                    v1 = load32(((v6 + (v9 * 36)) + 269376))
                                    v4 = (load32(((v6 + (v9 * 36)) + 269376)) if v1 else 100)
                                    v1 = ((v9 * 404) + ENTITY_TYPES)
                                    v7 = ((load32(((v6 + (v9 * 36)) + 269376)) if v1 else 100) * load32(((v9 * 404) + ENTITY_TYPES) + 68))
                                    v16 = (((load32(((v6 + (v9 * 36)) + 269376)) if v1 else 100) * load32(((v9 * 404) + ENTITY_TYPES) + 68)) // 100)
                                    store32(v5 + 48, (((load32(((v6 + (v9 * 36)) + 269376)) if v1 else 100) * load32(((v9 * 404) + ENTITY_TYPES) + 68)) // 100))
                                    v15 = (load32(v1 + 72) * v4)
                                    v11 = ((load32(v1 + 72) * v4) // 100)
                                    store32(v5 + 52, ((load32(v1 + 72) * v4) // 100))
                                    v12 = (load32(v1 + 76) * v4)
                                    v17 = ((load32(v1 + 76) * v4) // 100)
                                    store32(v5 + 56, ((load32(v1 + 76) * v4) // 100))
                                    v4 = (load32(v1 + 80) * v4)
                                    v20 = ((load32(v1 + 80) * v4) // 100)
                                    store32(v5 + 60, ((load32(v1 + 80) * v4) // 100))
                                    if (u32((v7 - 100)) <= u32(-200)):
                                        if (load32(v5 + 64) < v16):
                                            break
                                    if (u32((v15 - 100)) <= u32(-200)):
                                        if (load32(v5 + 68) < v11):
                                            break
                                    if (u32((v12 - 100)) <= u32(-200)):
                                        if (load32(v5 + 72) < v17):
                                            break
                                    if (u32((v4 - 100)) <= u32(-200)):
                                        if (load32(v5 + 76) < v20):
                                            break
                                    while True:  # $label132
                                        v16 = load32(v1 + 180)
                                        if not load8u(load32(v1 + 180) + 23):
                                            break
                                        v1 = load32(v16 + 4)
                                        if (load32(((load32(v16 + 4) * 404) + ENTITY_TYPES) + 264) != 3):
                                            break
                                        if load32(((v6 + (v1 << 2)) + 281808)):
                                            break
                                        break
                                    v17 = load32(v16 + 68)
                                    if load32(v16 + 68):
                                        v1 = 0
                                        v7 = 1
                                        v4 = 0
                                        v15 = 0
                                        while True:  # $label135
                                            v20 = load32((v16 + (v1 << 2)) + 28)
                                            v11 = load32(((load32((v16 + (v1 << 2)) + 28) * 404) + ENTITY_TYPES) + 264)
                                            v12 = (load32(((load32((v16 + (v1 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) == 1)
                                            while True:  # $label134
                                                while True:  # $label133
                                                    v20 = load32(((v6 + (v20 << 2)) + 281808))
                                                    if (load32(((v6 + (v20 << 2)) + 281808)) == 1):
                                                        break
                                                    v7 = ((v11 != 3) & v7)
                                                    if v20:
                                                        break
                                                    v7 = ((v11 != 0) & v7)
                                                    break
                                                    break
                                                v15 = (v12 | v15)
                                                break
                                            v4 = (v4 | v12)
                                            v1 = (v1 + 1)
                                            if ((v1 + 1) != v17):
                                                continue
                                            break
                                        if not (((v7 & v15) if (v4 & 1) else v7) & 1):
                                            break
                                    if not func183(v3, v6, v9, 0, 1, 1, 0, 1, 0):
                                        break
                                    v7 = load32(v6 + 281796)
                                    v4 = (load32(v7 + 8) - 1)
                                    store32(load32(v6 + 281796) + 8, (load32(v7 + 8) - 1))
                                    if (u32(v2) < u32(v4)):
                                        v9 = load32(v7)
                                        v1 = v2
                                        while True:  # $label136
                                            v1 = (v1 + 1)
                                            store32((v9 + (v1 << 2)), load32((v9 + ((v1 + 1) << 2))))
                                            v4 = load32(v7 + 8)
                                            if (u32(v1) < u32(load32(v7 + 8))):
                                                continue
                                            break
                                    v1 = (v4 - 1)
                                    store32(v7 + 8, (v4 - 1))
                                    if (u32(v1) > u32(v2)):
                                        v4 = load32(v7)
                                        v1 = v2
                                        while True:  # $label137
                                            v1 = (v1 + 1)
                                            store32((v4 + (v1 << 2)), load32((v4 + ((v1 + 1) << 2))))
                                            if (u32(v1) < u32(load32(v7 + 8))):
                                                continue
                                            break
                                    v2 = (v2 - 2)
                                    if not load32(v3 + 92):
                                        break
                                    v1 = load8u(9147141)
                                    if load32(9140316):
                                        if (load32(9140320) != load32(v3 + 28)):
                                            break
                                    break
                                v2 = (v2 + 2)
                                v1 = load32(v6 + 281796)
                                if (u32((v2 + 2)) < u32(load32(load32(v6 + 281796) + 8))):
                                    continue
                                break
                            break
                        G.global0 = (v5 + 80)
                        store8((v6 + 286701), 0)
                    while True:  # $label139
                        v3 = load32(9142848)
                        if ((load32(9142848) * 25) % 10000):
                            break
                        if load8u(9142905):
                            break
                        if load8u(9216060):
                            break
                        v7 = func88(v6)
                        while True:  # $label140
                            v4 = load32((v6 + 278572))
                            v3 = load32(load32((v6 + 278572)) + 8)
                            if (load32(load32((v6 + 278572)) + 8) != load32(v4 + 4)):
                                v5 = load32(v4)
                                break
                            v2 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v1 = load32(v4)
                            v5 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                            if v3:
                                # TODO: memory.copy
                            if v1:
                                v3 = load32(v4 + 8)
                            store32(v4, v5)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v5 + (v3 << 2)), v7)
                        v3 = 0
                        v7 = load32(38528)
                        v2 = 0
                        while True:  # $label143
                            while True:  # $label141
                                if (load32(((v3 * 404) + ENTITY_TYPES) + 264) & -5):
                                    break
                                if (v3 == v7):
                                    break
                                v2 = (load32(((v6 + (v3 << 2)) + 278576)) + v2)
                                break
                            v1 = (v3 | 1)
                            if ((v3 | 1) != 255):
                                while True:  # $label142
                                    if (load32(((v1 * 404) + ENTITY_TYPES) + 264) & -5):
                                        break
                                    if (v1 == v7):
                                        break
                                    v2 = (load32(((v6 + (v1 << 2)) + 278576)) + v2)
                                    break
                                v3 = (v3 + 2)
                                continue
                            break
                        while True:  # $label144
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v1 = v5
                                break
                            v1 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                            if v3:
                                # TODO: memory.copy
                            if v5:
                                v3 = load32(v4 + 8)
                            store32(v4, v1)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v1 + (v3 << 2)), v2)
                        v2 = 0
                        v7 = load32(PLAYER_COUNT)
                        if load32(PLAYER_COUNT):
                            v2 = load32((v6 + 281784))
                            v9 = (load32((v6 + 281784)) * 255)
                            v11 = (v2 * v7)
                            v5 = 0
                            v12 = load32(PLAYERS)
                            v17 = load32(9143004)
                            v2 = 0
                            while True:  # $label147
                                while True:  # $label145
                                    if not load8u((v17 + (v5 + v11))):
                                        break
                                    v16 = ((v12 + (v5 * 286704)) + 278568)
                                    v3 = 0
                                    while True:  # $label146
                                        if (load32(((v3 * 404) + ENTITY_TYPES) + 264) != 1):
                                            v2 = (load32((load32(v16) + ((v3 + v9) << 2))) + v2)
                                        v15 = (v3 | 1)
                                        if ((v3 | 1) == 255):
                                            break
                                        if (load32(((v15 * 404) + ENTITY_TYPES) + 264) != 1):
                                            v2 = (load32((load32(v16) + ((v9 + v15) << 2))) + v2)
                                        v3 = (v3 + 2)
                                        continue
                                        break
                                    raise Unreachable()
                                    break
                                v5 = (v5 + 1)
                                if ((v5 + 1) != v7):
                                    continue
                                break
                        while True:  # $label148
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v5 = v1
                                break
                            v5 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                            if v3:
                                # TODO: memory.copy
                            if v1:
                                v3 = load32(v4 + 8)
                            store32(v4, v5)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v5 + (v3 << 2)), v2)
                        v2 = 0
                        v11 = load32(PLAYER_COUNT)
                        if load32(PLAYER_COUNT):
                            v9 = load32((v6 + 278568))
                            v7 = 0
                            v16 = load32(38528)
                            while True:  # $label152
                                v15 = (v7 * 255)
                                v3 = 0
                                while True:  # $label151
                                    while True:  # $label149
                                        if (load32(((v3 * 404) + ENTITY_TYPES) + 264) == 1):
                                            break
                                        if (v3 == v16):
                                            break
                                        v2 = (load32((v9 + ((v3 + v15) << 2))) + v2)
                                        break
                                    v1 = (v3 | 1)
                                    if ((v3 | 1) != 255):
                                        while True:  # $label150
                                            if (load32(((v1 * 404) + ENTITY_TYPES) + 264) == 1):
                                                break
                                            if (v1 == v16):
                                                break
                                            v2 = (load32((v9 + ((v1 + v15) << 2))) + v2)
                                            break
                                        v3 = (v3 + 2)
                                        continue
                                    break
                                v7 = (v7 + 1)
                                if ((v7 + 1) != v11):
                                    continue
                                break
                        while True:  # $label153
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v1 = v5
                                break
                            v1 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                            if v3:
                                # TODO: memory.copy
                            if v5:
                                v3 = load32(v4 + 8)
                            store32(v4, v1)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v1 + (v3 << 2)), v2)
                        v5 = (load32((v6 + 281676)) + load32((v6 + 281640)))
                        while True:  # $label154
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v2 = v1
                                break
                            v2 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v2)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v2 + (v3 << 2)), v5)
                        v5 = (load32((v6 + 281680)) + load32((v6 + 281644)))
                        while True:  # $label155
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v1 = v2
                                break
                            v1 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v1)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v1 + (v3 << 2)), v5)
                        v5 = (load32((v6 + 281656)) + (load32((v6 + 281660)) + (load32((v6 + 281652)) + (load32((v6 + 281684)) + load32((v6 + 281648))))))
                        while True:  # $label156
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v2 = v1
                                break
                            v2 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v2)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v2 + (v3 << 2)), v5)
                        v5 = (load32((v6 + 281688)) + load32((v6 + 281664)))
                        while True:  # $label157
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v1 = v2
                                break
                            v1 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v1)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v1 + (v3 << 2)), v5)
                        v5 = load32(v6 + 283976)
                        while True:  # $label158
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v2 = v1
                                break
                            v2 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v2)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v2 + (v3 << 2)), v5)
                        v1 = (v6 + 281808)
                        v5 = ((load32(((v6 + 281808) + (load32(38732) << 2))) + load32((v1 + (load32(38460) << 2)))) + load32((v1 + (load32(38672) << 2))))
                        while True:  # $label159
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v1 = v2
                                break
                            v1 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v1)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v1 + (v3 << 2)), v5)
                        v5 = load32(v6 + 283936)
                        while True:  # $label160
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v2 = v1
                                break
                            v2 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v2)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v2 + (v3 << 2)), v5)
                        v5 = load32(v13 + 96)
                        while True:  # $label161
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v1 = v2
                                break
                            v1 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v1)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v1 + (v3 << 2)), v5)
                        v5 = load32(v13 + 100)
                        while True:  # $label162
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v2 = v1
                                break
                            v2 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v2)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v2 + (v3 << 2)), v5)
                        v5 = load32(v13 + 104)
                        while True:  # $label163
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v1 = v2
                                break
                            v1 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v1 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v1)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v1 + (v3 << 2)), v5)
                        v5 = load32(v13 + 108)
                        while True:  # $label164
                            v3 = load32(v4 + 8)
                            if (load32(v4 + 8) != load32(v4 + 4)):
                                v2 = v1
                                break
                            v2 = (load32(v4 + 12) + v3)
                            store32(v4 + 4, (load32(v4 + 12) + v3))
                            v2 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                            if v3:
                                # TODO: memory.copy
                            store32(v4, v2)
                            v3 = load32(v4 + 8)
                            break
                        store32(v4 + 8, (v3 + 1))
                        store32((v2 + (v3 << 2)), v5)
                        v3 = load32(9142848)
                        break
                    v10 = (v10 + 1)
                    v4 = load32(PLAYER_COUNT)
                    if (u32((v10 + 1)) < u32(load32(PLAYER_COUNT))):
                        continue
                    break
                if (u32(v4) < u32(2)):
                    break
                v2 = load32(39164)
                v1 = load32(PLAYERS)
                v3 = 1
                while True:  # $label167
                    while True:  # $label166
                        v5 = (v1 + (v3 * 286704))
                        if (load32((((v1 + (v3 * 286704)) + (v2 << 2)) + 281808)) != 1):
                            break
                        v6 = load32((v5 + 284240))
                        if ((load32(9142848) * 25) % (load32((v5 + 284240)) - (v6 % 25))):
                            break
                        v4 = load32(PLAYER_COUNT)
                        v2 = load32(39164)
                        v1 = load32(PLAYERS)
                        break
                    v3 = (v3 + 1)
                    if (u32((v3 + 1)) < u32(v4)):
                        continue
                    break
                break
            while True:  # $label168
                if ((load32(9142848) * 25) % 2000):
                    break
                func346()
                v4 = load32(PLAYER_COUNT)
                if (u32(load32(PLAYER_COUNT)) < u32(2)):
                    break
                v7 = 1
                while True:  # $label173
                    v4 = 0
                    v10 = load32(PLAYERS)
                    while True:  # $label172
                        while True:  # $label169
                            v2 = ((v4 * 404) + ENTITY_TYPES)
                            if (load32(((v4 * 404) + ENTITY_TYPES) + 264) != 1):
                                break
                            if not load32(v2 + 112):
                                break
                            v5 = load32((((v10 + (v7 * 286704)) + (v4 << 2)) + 284636))
                            if not load32((((v10 + (v7 * 286704)) + (v4 << 2)) + 284636)):
                                break
                            v9 = load32(v5 + 8)
                            if not load32(v5 + 8):
                                break
                            v3 = 0
                            while True:  # $label171
                                while True:  # $label170
                                    v1 = load32((load32(v5) + (v3 << 2)))
                                    if not load32((load32(v5) + (v3 << 2))):
                                        break
                                    v1 = entities[v1]
                                    v16 = load32(entities[v1].frame)
                                    v6 = load32(v2 + 112)
                                    if (u32(load32(entities[v1].frame)) >= u32(load32(v2 + 112))):
                                        break
                                    v16 = (v16 + 10)
                                    store32(v1 + 84, ((v16 + 10) if (u32(v6) > u32(v16)) else v6))
                                    if not load32(v1 + 92):
                                        break
                                    if load32(9140316):
                                        if (load32(9140320) != load32(v1 + 28)):
                                            break
                                    break
                                v3 = (v3 + 1)
                                if ((v3 + 1) != v9):
                                    continue
                                break
                            break
                        v4 = (v4 + 1)
                        if ((v4 + 1) != 255):
                            continue
                        break
                    v7 = (v7 + 1)
                    v4 = load32(PLAYER_COUNT)
                    if (u32((v7 + 1)) < u32(load32(PLAYER_COUNT))):
                        continue
                    break
                break
            while True:  # $label174
                v3 = (load32(9142848) * 25)
                if ((load32(9142848) * 25) % 7000):
                    break
                store32(9684392, 0)
                if load8u(9216060):
                    break
                if not v4:
                    v4 = 0
                    break
                v10 = load32(9143004)
                v2 = load32(PLAYERS)
                v7 = 0
                while True:  # $label178
                    v1 = 0
                    v6 = 0
                    v5 = 0
                    while True:  # $label177
                        v3 = 0
                        if load8u((v10 + ((v4 * v5) + v7))):
                            while True:  # $label176
                                while True:  # $label175
                                    v9 = ((v3 * 404) + ENTITY_TYPES)
                                    v16 = load32(((v3 * 404) + ENTITY_TYPES) + 264)
                                    if (load32(((v3 * 404) + ENTITY_TYPES) + 264) == 3):
                                        break
                                    if (load32(v9 + 188) != 55):
                                        break
                                    if (v16 == 2):
                                        break
                                    v1 = (load32((((v2 + (v5 * 286704)) + (v3 << 2)) + 281808)) + v1)
                                    break
                                v3 = (v3 + 1)
                                if ((v3 + 1) != 255):
                                    continue
                                break
                            v6 = (v6 + 1)
                        v5 = (v5 + 1)
                        if ((v5 + 1) != v4):
                            continue
                        break
                    store32((v2 + (v7 * 286704)) + 283924, (v1 + (v6 * 255)))
                    v7 = (v7 + 1)
                    v4 = load32(PLAYER_COUNT)
                    if (u32((v7 + 1)) < u32(load32(PLAYER_COUNT))):
                        continue
                    break
                v3 = (load32(9142848) * 25)
                break
            while True:  # $label179
                if (v3 % 1025):
                    break
                if load8u(9216060):
                    store8(9682192, 1)
                    v7 = load32(9142428)
                    if (u32(load32(9142428)) >= u32(48)):
                        v1 = load32(9142440)
                        v16 = ((load32(9142440) & 0xFFFFFFFF) >> 1)
                        # TODO: f32.demote_f64
                        v66 = (i32((v1 * v1)) * 1.52587890625e-05)
                        # TODO: i32.div_u
                        v1 = 100
                        v17 = (100 * v1)
                        v3 = 47
                        while True:  # $label193
                            v2 = (load32(GAME_STATE) + (v3 << 2))
                            v20 = load32((load32(GAME_STATE) + (v3 << 2)) + 16)
                            v21 = ((v3 + 7) if load32((load32(GAME_STATE) + (v3 << 2)) + 16) else v3)
                            while True:  # $label180
                                v1 = load32(v2 + 4)
                                if (load32(v2 + 4) == 1):
                                    break
                                v4 = load32(v2 + 8)
                                v15 = (2147483647 if (v1 == 2) else v1)
                                while True:  # $label181
                                    v1 = load32(v2)
                                    # TODO: f64.promote_f32
                                    v5 = load32(v2 + 12)
                                    v105 = (((v66 * i32(load32(v2))) + 0.5) if load32(v2 + 12) else i32(v1))
                                    if (((((v66 * i32(load32(v2))) + 0.5) if load32(v2 + 12) else i32(v1)) < 4294967296.0) & (v105 >= 0.0)):
                                        break
                                    break
                                v1 = 0
                                v11 = ((0 if v1 else 1) if v5 else v1)
                                v10 = load32(PLAYERS)
                                v9 = (v4 << 2)
                                v6 = load32(((load32(PLAYERS) + (v4 << 2)) + 281808))
                                while True:  # $label182
                                    if (v15 != 2147483647):
                                        break
                                    if (load32(((v4 * 404) + ENTITY_TYPES) + 264) != 1):
                                        break
                                    v1 = load32(PLAYER_COUNT)
                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                        break
                                    v5 = (v1 - 1)
                                    v12 = ((v1 - 1) & 3)
                                    v3 = 1
                                    if (u32((v1 - 2)) >= u32(3)):
                                        v14 = (v5 & -4)
                                        v5 = 0
                                        while True:  # $label183
                                            v1 = ((v10 + (v3 * 286704)) + v9)
                                            v6 = (load32((((v10 + (v3 * 286704)) + v9) + 1141920)) + (load32((v1 + 855216)) + (load32((v1 + 568512)) + (load32((v1 + 281808)) + v6))))
                                            v3 = (v3 + 4)
                                            v5 = (v5 + 4)
                                            if ((v5 + 4) != v14):
                                                continue
                                            break
                                    v1 = 0
                                    if not v12:
                                        break
                                    while True:  # $label184
                                        v6 = (load32((((v10 + (v3 * 286704)) + v9) + 281808)) + v6)
                                        v3 = (v3 + 1)
                                        v1 = (v1 + 1)
                                        if ((v1 + 1) != v12):
                                            continue
                                        break
                                    break
                                if (u32(v6) >= u32(v11)):
                                    break
                                v8 = (v2 + 20)
                                v12 = ((v4 * 404) + ENTITY_TYPES)
                                v5 = 0
                                while True:  # $label192
                                    v1 = load32(9147324)
                                    v3 = load32(9147316)
                                    store32(9147324, load32(9147316))
                                    v7 = load32(9147320)
                                    v10 = load32(9147312)
                                    store32(9147320, load32(9147312))
                                    v1 = (v1 ^ (v1 << 11))
                                    v2 = ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((v1 ^ (v1 << 11)) & 0xFFFFFFFF) >> 8))) ^ v1)
                                    store32(9147316, ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((v1 ^ (v1 << 11)) & 0xFFFFFFFF) >> 8))) ^ v1))
                                    v1 = (v7 ^ (v7 << 11))
                                    v1 = ((((((v7 ^ (v7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v1) ^ v2)
                                    store32(9147312, ((((((v7 ^ (v7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v2 & 0xFFFFFFFF) >> 19)) ^ v1) ^ v2))
                                    v14 = load32(9142440)
                                    v7 = (v1 % load32(9142440))
                                    while True:  # $label188
                                        while True:  # $label185
                                            v9 = (v2 % v14)
                                            while True:  # $label187
                                                while True:  # $label186
                                                    v19 = load32(v12 + 264)
                                                    if (u32((load32(v12 + 264) - 1)) >= u32(2)):
                                                        if (load8u((load32(9147288) + ((v7 * v14) + v9))) != 3):
                                                            break
                                                        if v19:
                                                            break
                                                        store32(9147320, v2)
                                                        store32(9147324, v10)
                                                        store32(9147316, v1)
                                                        v2 = ((v3 << 11) ^ v3)
                                                        v1 = (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v1)
                                                        store32(9147312, (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v1))
                                                        break
                                                    v14 = (v9 - v16)
                                                    v14 = (v7 - v16)
                                                    if (((((v9 - v16) * v14) + ((v7 - v16) * v14)) - 1) <= v17):
                                                        break
                                                    break
                                                if (v4 != load32(38504)):
                                                    break
                                                store32(9147320, v2)
                                                store32(9147324, v10)
                                                store32(9147316, v1)
                                                v2 = ((v3 << 11) ^ v3)
                                                v1 = (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v1)
                                                store32(9147312, (((((((v3 << 11) ^ v3) & 0xFFFFFFFF) >> 8) ^ ((v1 & 0xFFFFFFFF) >> 19)) ^ v2) ^ v1))
                                                break
                                            v1 = func34(v15, (v2 % v14), v7, (v1 & 7), (v1 % 3), 1)
                                            if not func34(v15, (v2 % v14), v7, (v1 & 7), (v1 % 3), 1):
                                                break
                                            if v20:
                                                func148(v1, v8, 1)
                                            while True:  # $label189
                                                if (load32(v12 + 216) != 1):
                                                    break
                                                while True:  # $label191
                                                    while True:  # $label190
                                                        v2 = load32(load32(GAME_STATE) + 48)
                                                        if load32(load32(GAME_STATE) + 48):
                                                            if not load8u(9147152):
                                                                break
                                                        v3 = load32(9142440)
                                                        break
                                                        break
                                                    v3 = load32(9142440)
                                                    v1 = load16u((load32(9147376) + (((load32(9142440) * v7) + v9) << 1)))
                                                    if (v2 == 2):
                                                        if (u32(v1) > u32(1)):
                                                            break
                                                        break
                                                    if not v1:
                                                        break
                                                    break
                                                func80(i32(v9), i32(v7), load32(9142536), 32.0, i32((v3 * 96)))
                                                break
                                            v6 = (v6 + 1)
                                            break
                                        v5 = (v5 + 1)
                                        break
                                    if ((u32(v6) < u32(v11)) & (u32(v5) < u32(200))):
                                        continue
                                    break
                                v7 = load32(9142428)
                                break
                            v3 = (v21 + 5)
                            if (u32((v21 + 5)) < u32(v7)):
                                continue
                            break
                        v4 = load32(PLAYER_COUNT)
                    store8(9682192, 0)
                v5 = 1
                if (u32(v4) > u32(1)):
                    while True:  # $label201
                        while True:  # $label194
                            v4 = load32(((players[v5] + (load32(38528) << 2)) + 284636))
                            if not load32(((players[v5] + (load32(38528) << 2)) + 284636)):
                                break
                            v3 = 0
                            v7 = 0
                            v9 = load32(v4 + 8)
                            if not load32(v4 + 8):
                                break
                            while True:  # $label200
                                while True:  # $label195
                                    v1 = load32((load32(v4) + (v3 << 2)))
                                    if not load32((load32(v4) + (v3 << 2))):
                                        break
                                    while True:  # $label196
                                        while True:  # $label198
                                            while True:  # $label197
                                                v2 = load32(ENTITIES)
                                                v10 = (v2 + (v1 * 132))
                                                v16 = load32((v2 + (v1 * 132)) + 28)
                                                v1 = entities[load32((v2 + (v1]
                                                v15 = load8u(entities[load32((v2 + (v1].unit_class)
                                                # br_table (load8u(entities[load32((v2 + (v1].unit_class) - 3)
                                                break
                                                break
                                            v6 = load32(v1 + 72)
                                            v2 = load32(v1 + 76)
                                            if (u32(load32(v1 + 72)) < u32(load32(v1 + 76))):
                                                v6 = (load32((players[load16u(v1 + 110)] + 284072)) + v6)
                                                v6 = ((load32((players[load16u(v1 + 110)] + 284072)) + v6) if (u32(v2) > u32(v6)) else v2)
                                                store32(v1 + 72, ((load32((players[load16u(v1 + 110)] + 284072)) + v6) if (u32(v2) > u32(v6)) else v2))
                                            while True:  # $label199
                                                v11 = load32(v1 + 96)
                                                if not load32(v1 + 96):
                                                    break
                                                v11 = entities[v11]
                                                if ((load8u(entities[v11].unit_class) & 251) != 3):
                                                    if (load32(v11 + 32) == v16):
                                                        break
                                                store32(v1 + 96, 0)
                                                break
                                            v16 = 0
                                            if (v15 == 1):
                                                break
                                            if (v2 != v6):
                                                break
                                            if v16:
                                                break
                                            if load32(v1 + 36):
                                                break
                                            func403(v1)
                                            break
                                        v6 = load32(v1 + 80)
                                        v16 = players[load16u(v1 + 110)]
                                        v2 = load32((players[load16u(v1 + 110)] + 284320))
                                        if (u32(load32(v1 + 80)) >= u32(load32((players[load16u(v1 + 110)] + 284320)))):
                                            break
                                        v1 = (load32((v16 + 284076)) + v6)
                                        store32(v1 + 80, ((load32((v16 + 284076)) + v6) if (u32(v1) < u32(v2)) else v2))
                                        break
                                    if not load32(v10 + 92):
                                        break
                                    if load32(9140316):
                                        if (load32(9140320) != load32(v10 + 28)):
                                            break
                                    v7 = 1
                                    break
                                v3 = (v3 + 1)
                                if ((v3 + 1) != v9):
                                    continue
                                break
                            if not (v7 & 1):
                                break
                            break
                        v5 = (v5 + 1)
                        if (u32((v5 + 1)) < u32(load32(PLAYER_COUNT))):
                            continue
                        break
                v3 = load32(GAME_STATE)
                v9 = load32(load32(GAME_STATE) + 32)
                if not load32(load32(GAME_STATE) + 32):
                    break
                v1 = (load32(9142848) * 25)
                v16 = load32(v3 + 56)
                if (u32((load32(9142848) * 25)) < u32((load32(v3 + 56) * 1000))):
                    break
                v2 = load32(9684364)
                v4 = load32(v3 + 84)
                while True:  # $label202
                    while True:  # $label205
                        while True:  # $label203
                            while True:  # $label204
                                v5 = load32(9684372)
                                if (u32(load32(9684372)) <= u32(v1)):
                                    if ((u32(v2) >= u32(v4)) if v2 else 0):
                                        break
                                    v6 = load32(9142440)
                                    v67 = i32((load32(9142440) << 4))
                                    v66 = (i32((load32(9142440) << 4)) * 1.41421294)
                                    if v2:
                                        break
                                    v70 = v66
                                    break
                                if v2:
                                    break
                                v6 = load32(9142440)
                                v67 = i32((load32(9142440) << 4))
                                v70 = (i32((load32(9142440) << 4)) * 1.41421294)
                                v66 = (i32((load32(9142440) << 4)) * 1.41421294)
                                break
                            v2 = 0
                            storef32(9684348, v67)
                            storef32(9684356, v70)
                            storef32(9684352, v67)
                            break
                            break
                        v70 = loadf32(9684360)
                        storef32(9684356, loadf32(9684360))
                        v67 = loadf32(9684352)
                        break
                    v68 = loadf32(9684348)
                    storef32(9684344, v67)
                    storef32(9684340, v68)
                    v5 = (v2 + 1)
                    store32(9684364, (v2 + 1))
                    v66 = ((floor((((v66 * i32((v4 - v5))) / i32(v4)) * 0.03125)) * 32.0) + 0.5)
                    storef32(9684360, ((floor((((v66 * i32((v4 - v5))) / i32(v4)) * 0.03125)) * 32.0) + 0.5))
                    v71 = i32((load32(v3 + 92) << 5))
                    if (i32((load32(v3 + 92) << 5)) > v66):
                        storef32(9684360, v71)
                        v66 = v71
                    v69 = v67
                    v71 = v68
                    while True:  # $label208
                        while True:  # $label210
                            while True:  # $label207
                                while True:  # $label206
                                    # br_table (load32(v3 + 20) - 1)
                                    break
                                    break
                                v4 = load32(9147324)
                                store32(9147324, load32(9147316))
                                v7 = load32(9147320)
                                v10 = load32(9147312)
                                store32(9147320, load32(9147312))
                                v4 = (v4 ^ (v4 << 11))
                                v4 = ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((v4 ^ (v4 << 11)) & 0xFFFFFFFF) >> 8))) ^ v4)
                                store32(9147316, ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((v4 ^ (v4 << 11)) & 0xFFFFFFFF) >> 8))) ^ v4))
                                v7 = (v7 ^ (v7 << 11))
                                v7 = ((((((v7 ^ (v7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v7) ^ v4)
                                store32(9147312, ((((((v7 ^ (v7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v7) ^ v4))
                                v10 = (v6 << 5)
                                v69 = i32(((v6 << 5) - 32))
                                while True:  # $label209
                                    v71 = (i32(v6) * 32.0)
                                    v71 = (((i32(v6) * 32.0) if (v70 > v71) else v70) - v66)
                                    if (abs((((i32(v6) * 32.0) if (v70 > v71) else v70) - v66)) < 2147483650.0):
                                        break
                                    break
                                v4 = -2147483648
                                v4 = (i32(v71) if (v4 <= 2) else -2147483648)
                                v71 = (v4 + i32((((2 % (i32(v71) if (v4 <= 2) else -2147483648)) << 1) - v4)))
                                v71 = (v68 if (v71 < 0.0) else (v4 + i32((((2 % (i32(v71) if (v4 <= 2) else -2147483648)) << 1) - v4))))
                                v73 = i32(v10)
                                v71 = ((floor(((0.0 if (v71 >= i32(v10)) else (v68 if (v71 < 0.0) else (v4 + i32((((2 % (i32(v71) if (v4 <= 2) else -2147483648)) << 1) - v4))))) * 0.03125)) * 32.0) + 0.5)
                                storef32(i32(((v6 << 5) - 32)), ((floor(((0.0 if (v71 >= i32(v10)) else (v68 if (v71 < 0.0) else (v4 + i32((((2 % (i32(v71) if (v4 <= 2) else -2147483648)) << 1) - v4))))) * 0.03125)) * 32.0) + 0.5))
                                v69 = (v67 + i32((((v7 % v4) << 1) - v4)))
                                v69 = (0.0 if (v69 < 0.0) else (v67 + i32((((v7 % v4) << 1) - v4))))
                                break
                                break
                            v4 = load32(9147324)
                            store32(9147324, load32(9147316))
                            v7 = load32(9147320)
                            v10 = load32(9147312)
                            store32(9147320, load32(9147312))
                            v4 = (v4 ^ (v4 << 11))
                            v4 = ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((v4 ^ (v4 << 11)) & 0xFFFFFFFF) >> 8))) ^ v4)
                            store32(9147316, ((v10 ^ (((v10 & 0xFFFFFFFF) >> 19) ^ (((v4 ^ (v4 << 11)) & 0xFFFFFFFF) >> 8))) ^ v4))
                            v6 = (v6 << 5)
                            v71 = (i32((v4 % (v6 << 5))) + 0.5)
                            storef32(9684348, (i32((v4 % (v6 << 5))) + 0.5))
                            v7 = (v7 ^ (v7 << 11))
                            v4 = ((((((v7 ^ (v7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v7) ^ v4)
                            store32(9147312, ((((((v7 ^ (v7 << 11)) & 0xFFFFFFFF) >> 8) ^ ((v4 & 0xFFFFFFFF) >> 19)) ^ v7) ^ v4))
                            break
                        v69 = (i32((v4 % v6)) + 0.5)
                        storef32(((floor(((v69 if (v69 >= v73) else (0.0 if (v69 < 0.0) else (v67 + i32((((v7 % v4) << 1) - v4))))) * 0.03125)) * 32.0) + 0.5), (i32((v4 % v6)) + 0.5))
                        break
                    store32(9684368, v1)
                    v3 = load32(v3 + 96)
                    if v2:
                        v1 = ((v3 * 1000) + v1)
                        store32(9684368, ((v3 * 1000) + v1))
                    # TODO: f64.promote_f32
                    storef64(v13 + 32, v70)
                    store32(v13 + 40, v1)
                    store32(v13 + 76, v5)
                    # TODO: f64.promote_f32
                    storef64(v13 + 48, (v71 - v68))
                    # TODO: f64.promote_f32
                    storef64(v13 + 56, (v69 - v67))
                    # TODO: f64.promote_f32
                    storef64((v13 - -64), (v66 - v70))
                    v2 = ((((v2 * v3) + v16) * 1000) + ((v5 * v9) * 60000))
                    store32(9684372, ((((v2 * v3) + v16) * 1000) + ((v5 * v9) * 60000)))
                    store32(v13 + 72, (v2 - v1))
                    # TODO: f64.promote_f32
                    storef64(v13 + 16, v68)
                    # TODO: f64.promote_f32
                    storef64(v13 + 24, v67)
                    a_b()
                    v1 = (load32(9142848) * 25)
                    v5 = load32(9684372)
                    break
                v67 = 1.0
                while True:  # $label211
                    v1 = load32(9684368)
                    v66 = (i32(v1) - i32(load32(9684368)))
                    v70 = i32((v5 - v1))
                    if ((i32(v1) - i32(load32(9684368))) > i32((v5 - v1))):
                        break
                    if (v1 == v5):
                        break
                    v67 = 0.0
                    if (v66 < 0.0):
                        break
                    v67 = (v66 / v70)
                    break
                if (u32(load32(9671136)) < u32(4)):
                    break
                while True:  # $label212
                    v66 = loadf32(9684344)
                    # TODO: f64.promote_f32
                    v105 = (((((loadf32(9684352) - loadf32(9684344)) * v67) + v66) + 0.5) * 0.03125)
                    if (abs((((((loadf32(9684352) - loadf32(9684344)) * v67) + v66) + 0.5) * 0.03125)) < 2147483648.0):
                        break
                    break
                v4 = (-2147483648 << 1)
                while True:  # $label213
                    v66 = loadf32(9684340)
                    # TODO: f64.promote_f32
                    v105 = (((((loadf32(9684348) - loadf32(9684340)) * v67) + v66) * 0.03125) + 0.5)
                    if (abs((((((loadf32(9684348) - loadf32(9684340)) * v67) + v66) * 0.03125) + 0.5)) < 2147483648.0):
                        break
                    break
                v6 = (-2147483648 << 1)
                while True:  # $label214
                    v66 = loadf32(9684356)
                    # TODO: f64.promote_f32
                    v105 = (((((loadf32(9684360) - loadf32(9684356)) * v67) + v66) * 0.03125) + 0.5)
                    if (abs((((((loadf32(9684360) - loadf32(9684356)) * v67) + v66) * 0.03125) + 0.5)) < 2147483648.0):
                        break
                    break
                v1 = (-2147483648 << 1)
                v7 = ((-2147483648 << 1) * v1)
                v3 = 3
                while True:  # $label216
                    while True:  # $label215
                        v3 = ((load32(9684380) if (v3 == load32(9684376)) else 0) + v3)
                        v1 = entities[((load32(9684380) if (v3 == load32(9684376)) else 0) + v3)]
                        if (load8u(entities[((load32(9684380) if (v3 == load32(9684376)) else 0) + v3)].unit_class) == 3):
                            break
                        v2 = ((load8u(v1 + 122) * 404) + ENTITY_TYPES)
                        v5 = ((load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 220) - v4) + (load16u(v1 + 114) << 1))
                        v5 = ((load32(v2 + 216) - v6) + (load16u(v1 + 112) << 1))
                        if ((((((load32(((load8u(v1 + 122) * 404) + ENTITY_TYPES) + 220) - v4) + (load16u(v1 + 114) << 1)) * v5) + (((load32(v2 + 216) - v6) + (load16u(v1 + 112) << 1)) * v5)) - 1) <= v7):
                            break
                        v5 = load32(v2 + 264)
                        if ((load32(v2 + 264) == 1) & (load32(v2 + 188) != 55)):
                            break
                        if (v5 == 2):
                            break
                        if (load32(v1 + 64) == -1):
                            break
                        if load32(v1 + 36):
                            break
                        func103(v1)
                        if (load8u(v1 + 125) == 3):
                            break
                        v2 = (v1 - -64)
                        v10 = load32((v1 - -64))
                        v5 = load32(load32(GAME_STATE) + 88)
                        if (u32(load32((v1 - -64))) <= u32(load32(load32(GAME_STATE) + 88))):
                            store32(v2, 0)
                            break
                        store32(v2, (v10 - v5))
                        if not load32(v1 + 92):
                            break
                        if load8u(9147141):
                            break
                        store32(v13, v5)
                        a_b()
                        break
                    v3 = (v3 + 1)
                    if (u32((v3 + 1)) < u32(load32(9671136))):
                        continue
                    break
                break
            G.global0 = (v13 + 112)
            store8(9147140, 1)
            if (u32(load32(9215892)) >= u32(5)):
                v1 = load32(9215884)
                v2 = 4
                while True:  # $label218
                    while True:  # $label217
                        v5 = (v2 << 2)
                        if (load32((v1 + (v2 << 2))) != load32(9142848)):
                            break
                        store32(9671116, v2)
                        v3 = ((v2 | 2) << 2)
                        v4 = ((v2 | 3) << 2)
                        v6 = ((v2 | 1) << 2)
                        v1 = load32(9215884)
                        v5 = (load32(9215884) + v5)
                        if (load32((load32(9215884) + v5)) == load32(9142848)):
                            store32(v5, 0)
                        if not load8u(59128):
                            break
                        v5 = load32((v1 + v4))
                        v3 = load32((v1 + v3))
                        v4 = load32((v1 + v6))
                        v6 = load32((load32(ENTITIES) + 1690568))
                        store32(arg0 + 48, load32((v1 + (load32((load32(ENTITIES) + 1690568)) << 4))))
                        store32(arg0 + 52, v6)
                        store32(arg0 + 56, load32(9142848))
                        store32(arg0 + 32, load32(9671116))
                        store32(arg0 + 36, v4)
                        store32(arg0 + 40, v3)
                        store32(arg0 + 44, v5)
                        v1 = load32(9215884)
                        break
                    v2 = (v2 + 4)
                    if (u32((v2 + 4)) < u32(load32(9215892))):
                        continue
                    break
            v1 = load32(9142848)
            v2 = (load32(9142848) + 1)
            store32(9142848, (load32(9142848) + 1))
            store8(9147140, 0)
            v2 = (v2 * 25)
            if (((v2 * 25) % 1025) if v1 else 0):
            else:
                while True:  # $label219
                    if (load32(9213808) != 1):
                        break
                    v1 = entities[load32(9173808)]
                    if (load32(((load8u(entities[load32(9173808)].sub_state) * 404) + ENTITY_TYPES) + 264) != 1):
                        break
                    v2 = load32(v1 + 44)
                    if not load32(v1 + 44):
                        break
                    while True:  # $label220
                        while True:  # $label221
                            v2 = load32((load32(9215884) + (v2 << 4)) + 4)
                            # br_table (load32((load32(9215884) + (v2 << 4)) + 4) - 2)
                            break
                            break
                        if (v2 != 34):
                            break
                        break
                    if not load32(v1 + 92):
                        break
                    if load32(9140316):
                        if (load32(9140320) != load32(v1 + 28)):
                            break
                    break
                v51 = 0
                v54 = 0
                v55 = 0
                v56 = 0
                v57 = 0
                v58 = 0
                v59 = 0
                v60 = 0
                v61 = 0
                v19 = (G.global0 - 96)
                G.global0 = (G.global0 - 96)
                if (u32(load32(PLAYER_COUNT)) >= u32(2)):
                    v40 = 1
                    while True:  # $label602
                        while True:  # $label222
                            v62 = (v40 * 286704)
                            v8 = ((v40 * 286704) + load32(PLAYERS))
                            if not load32(((v40 * 286704) + load32(PLAYERS)) + 286684):
                                break
                            v9 = (v8 + 283960)
                            v1 = load32(v8 + 283960)
                            if (u32(load32(v8 + 283960)) >= u32(3)):
                                func425(v8)
                                v1 = load32(v9)
                                if (u32(load32(v9)) > u32(2)):
                                    break
                            v13 = load32(((v1 << 2) + 9940))
                            if not load32(v8 + 283872):
                                if not load32(v8 + 283876):
                                    break
                            v5 = (v8 + 286684)
                            store64(v19 + 72, 0)
                            store64(v19 + 64, 0)
                            v12 = load32(v19 + 80)
                            v14 = load32(v19 + 84)
                            v11 = load32(v19 + 88)
                            v17 = load32(v19 + 92)
                            storef32(v19 + 48, i32(load32(v8 + 283984)))
                            storef32(v19 + 52, i32(load32((v8 + 283988))))
                            storef32(v19 + 56, i32(load32((v8 + 283992))))
                            v1 = load32((v8 + 283996))
                            v2 = 0
                            store32(9140296, 0)
                            storef32(v19 + 60, i32(v1))
                            while True:  # $label223
                                v1 = (v8 + (v2 * 1056))
                                v3 = ((v8 + (v2 * 1056)) + 1150)
                                if load8u(((v8 + (v2 * 1056)) + 1150)):
                                    store8((v1 + 1151), 0)
                                    store32((v1 + 1140), 0)
                                    store32(v1 + 624, 0)
                                    store32(v1 + 96, 0)
                                    store64(v1 + 104, 0)
                                    store8(v3, 0)
                                v2 = (v2 + 1)
                                if ((v2 + 1) != 255):
                                    continue
                                break
                            v16 = 0
                            v6 = load32(load32(GAME_STATE) + 40)
                            while True:  # $label224
                                if (load32(v9) == load32(39224)):
                                    break
                                v16 = 1
                                v1 = (v8 + (load32(38528) << 2))
                                if (load32(((v8 + (load32(38528) << 2)) + 282828)) != (0 - load32((v1 + 281808)))):
                                    break
                                if (v11 > 999):
                                    break
                                v1 = (v8 + (load32(38500) << 2))
                                v16 = (u32((load32(((v8 + (load32(38500) << 2)) + 282828)) + load32((v1 + 281808)))) > u32(14))
                                break
                            v7 = (u32(load32(v8 + 283976)) < u32(200))
                            while True:  # $label225
                                if not load32(v8 + 283940):
                                    break
                                v1 = load32(38720)
                                v2 = (v8 + (load32(38720) << 2))
                                v4 = (load32(((v8 + (load32(38720) << 2)) + 282828)) + load32((v2 + 281808)))
                                v3 = 3
                                v2 = ((v1 * 404) + ENTITY_TYPES)
                                if (u32(load32(((v1 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                    v3 = (load32(v5) * 3)
                                    # TODO: i32.div_u
                                    v3 = ((load32(v5) * 3) if (u32(v3) < u32(100)) else 100)
                                while True:  # $label226
                                    if (u32(v3) <= u32(v4)):
                                        break
                                    if load8u(v2 + 354):
                                        break
                                    v2 = (v8 + (v1 * 1056))
                                    store8(((v8 + (v1 * 1056)) + 1150), 1)
                                    v4 = (v3 - v4)
                                    store32(v2 + 108, (v3 - v4))
                                    v66 = i32(v3)
                                    storef32(v2 + 100, (280.0 / i32(v3)))
                                    storef32(v2 + 96, ((i32(v4) * 280.0) / v66))
                                    v2 = load32(9140296)
                                    store32(9140296, (load32(9140296) + 1))
                                    store32(((v2 << 2) + 8451904), v1)
                                    break
                                v3 = 2
                                v1 = load32(38716)
                                v2 = (v8 + (load32(38716) << 2))
                                v4 = (load32(((v8 + (load32(38716) << 2)) + 282828)) + load32((v2 + 281808)))
                                v2 = ((v1 * 404) + ENTITY_TYPES)
                                if (u32(load32(((v1 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                    v3 = (load32(v5) << 1)
                                    # TODO: i32.div_u
                                    v3 = ((load32(v5) << 1) if (u32(v3) < u32(100)) else 100)
                                if (u32(v3) <= u32(v4)):
                                    break
                                if load8u(v2 + 354):
                                    break
                                v2 = (v8 + (v1 * 1056))
                                store8(((v8 + (v1 * 1056)) + 1150), 1)
                                v4 = (v3 - v4)
                                store32(v2 + 108, (v3 - v4))
                                v66 = i32(v3)
                                storef32(v2 + 100, (220.0 / i32(v3)))
                                storef32(v2 + 96, ((i32(v4) * 220.0) / v66))
                                v2 = load32(9140296)
                                store32(9140296, (load32(9140296) + 1))
                                store32(((v2 << 2) + 8451904), v1)
                                break
                            v1 = (200 if v7 else v6)
                            while True:  # $label258
                                while True:  # $label257
                                    v2 = load32(v9)
                                    if (load32(v9) == load32(57156)):
                                        v4 = load32(38444)
                                        v2 = (v8 + (load32(38444) << 2))
                                        v6 = load32(((v8 + (load32(38444) << 2)) + 281808))
                                        v7 = load32((v2 + 282828))
                                        while True:  # $label227
                                            # TODO: i32.div_u
                                            v1 = 100
                                            # TODO: i32.div_u
                                            v2 = 100
                                            v48 = ((v1 * 35) - 100)
                                            v106 = i32(((v1 * 35) - 100))
                                            v105 = (i32(((v1 * 35) - 100)) * 0.2)
                                            if (((i32(((v1 * 35) - 100)) * 0.2) < 4294967296.0) & (v105 >= 0.0)):
                                                break
                                            break
                                        v1 = 0
                                        v3 = 0
                                        v10 = ((v4 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v4 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v3 = (load32(v5) * v1)
                                            # TODO: i32.div_u
                                            v3 = ((load32(v5) * v1) if (u32(v3) < u32(100)) else 100)
                                        while True:  # $label228
                                            v7 = (v6 + v7)
                                            if (u32((v6 + v7)) >= u32(v3)):
                                                break
                                            if load8u(v10 + 354):
                                                break
                                            v6 = (v8 + (v4 * 1056))
                                            store8(((v8 + (v4 * 1056)) + 1150), 1)
                                            v7 = (v3 - v7)
                                            store32(v6 + 108, (v3 - v7))
                                            v66 = i32(v3)
                                            storef32(v6 + 100, (90.0 / i32(v3)))
                                            storef32(v6 + 96, ((i32(v7) * 90.0) / v66))
                                            v3 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v3 << 2) + 8451904), v4)
                                            break
                                        v4 = load32(38436)
                                        v3 = (v8 + (load32(38436) << 2))
                                        v6 = load32(((v8 + (load32(38436) << 2)) + 281808))
                                        v7 = load32((v3 + 282828))
                                        v10 = ((v4 * 404) + ENTITY_TYPES)
                                        v15 = (u32(load32(((v4 * 404) + ENTITY_TYPES) + 264)) > u32(1))
                                        while True:  # $label229
                                            v105 = (v106 * 0.4)
                                            if (((v106 * 0.4) < 4294967296.0) & (v105 >= 0.0)):
                                                break
                                            break
                                        v3 = 0
                                        if not v15:
                                            v3 = (load32(v5) * v3)
                                            # TODO: i32.div_u
                                            v3 = ((load32(v5) * v3) if (u32(v3) < u32(100)) else 100)
                                        while True:  # $label230
                                            v7 = (v6 + v7)
                                            if (u32((v6 + v7)) >= u32(v3)):
                                                break
                                            if load8u(v10 + 354):
                                                break
                                            v6 = (v8 + (v4 * 1056))
                                            store8(((v8 + (v4 * 1056)) + 1150), 1)
                                            v7 = (v3 - v7)
                                            store32(v6 + 108, (v3 - v7))
                                            v66 = i32(v3)
                                            storef32(v6 + 100, (120.0 / i32(v3)))
                                            storef32(v6 + 96, ((i32(v7) * 120.0) / v66))
                                            v3 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v3 << 2) + 8451904), v4)
                                            break
                                        v4 = load32(57152)
                                        v3 = (v8 + (load32(57152) << 2))
                                        v7 = (load32(((v8 + (load32(57152) << 2)) + 282828)) + load32((v3 + 281808)))
                                        v3 = v1
                                        v6 = ((v4 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v4 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v3 = (load32(v5) * v1)
                                            # TODO: i32.div_u
                                            v3 = ((load32(v5) * v1) if (u32(v3) < u32(100)) else 100)
                                        while True:  # $label231
                                            if (u32(v3) <= u32(v7)):
                                                break
                                            if load8u(v6 + 354):
                                                break
                                            v6 = (v8 + (v4 * 1056))
                                            store8(((v8 + (v4 * 1056)) + 1150), 1)
                                            v7 = (v3 - v7)
                                            store32(v6 + 108, (v3 - v7))
                                            v66 = i32(v3)
                                            storef32(v6 + 100, (120.0 / i32(v3)))
                                            storef32(v6 + 96, ((i32(v7) * 120.0) / v66))
                                            v3 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v3 << 2) + 8451904), v4)
                                            break
                                        v3 = load32(38424)
                                        v4 = (v8 + (load32(38424) << 2))
                                        v6 = (load32(((v8 + (load32(38424) << 2)) + 282828)) + load32((v4 + 281808)))
                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) * v1)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) * v1) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label232
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (80.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 80.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        while True:  # $label233
                                            v1 = load32(v8 + 283868)
                                            if (load32(v8 + 283868) != (load32((v8 + 284372)) + (load32((v8 + 284380)) * load32(v8 + 283864)))):
                                                if (u32(v1) < u32(load32((v8 + 284376)))):
                                                    break
                                            v3 = load32(38636)
                                            v1 = (v8 + (load32(38636) << 2))
                                            v6 = (load32(((v8 + (load32(38636) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v4 = ((v3 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (46.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 46.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v3 = load32(38476)
                                        v1 = (v8 + (load32(38476) << 2))
                                        v6 = (load32(((v8 + (load32(38476) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 34
                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) * 34)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) * 34) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label234
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (121.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 121.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v1 = (v8 + (v13 << 2))
                                        v3 = (load32(((v8 + (v13 << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = ((v13 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v13 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v2 = (load32(v5) * v2)
                                            # TODO: i32.div_u
                                            v2 = ((load32(v5) * v2) if (u32(v2) < u32(100)) else 100)
                                        while True:  # $label235
                                            if (u32(v2) <= u32(v3)):
                                                break
                                            if load8u(v1 + 354):
                                                break
                                            v1 = (v8 + (v13 * 1056))
                                            store8(((v8 + (v13 * 1056)) + 1150), 1)
                                            v3 = (v2 - v3)
                                            store32(v1 + 108, (v2 - v3))
                                            v66 = i32(v2)
                                            storef32(v1 + 100, (400.0 / i32(v2)))
                                            storef32(v1 + 96, ((i32(v3) * 400.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v13)
                                            break
                                        while True:  # $label237
                                            while True:  # $label236
                                                if (v11 <= 1999):
                                                    v2 = load32(39096)
                                                    v1 = (v8 + (load32(39096) << 2))
                                                    v4 = (load32(((v8 + (load32(39096) << 2)) + 282828)) + load32((v1 + 281808)))
                                                    v1 = 1
                                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                        v1 = load32(v5)
                                                        # TODO: i32.div_u
                                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                                    if (u32(v1) <= u32(v4)):
                                                        break
                                                    if load8u(v3 + 354):
                                                        break
                                                    v3 = (v8 + (v2 * 1056))
                                                    store8(((v8 + (v2 * 1056)) + 1150), 1)
                                                    v4 = (v1 - v4)
                                                    store32(v3 + 108, (v1 - v4))
                                                    v66 = i32(v1)
                                                    storef32(v3 + 100, (1001.0 / i32(v1)))
                                                    storef32(v3 + 96, ((i32(v4) * 1001.0) / v66))
                                                    v1 = load32(9140296)
                                                    store32(9140296, (load32(9140296) + 1))
                                                    store32(((v1 << 2) + 8451904), v2)
                                                    break
                                                if (u32(v11) > u32(7999999)):
                                                    break
                                                break
                                            while True:  # $label239
                                                if v16:
                                                    v2 = load32(38528)
                                                    v1 = (v8 + (load32(38528) << 2))
                                                    v4 = (load32(((v8 + (load32(38528) << 2)) + 282828)) + load32((v1 + 281808)))
                                                    v1 = 60
                                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                        v1 = (load32(v5) * 60)
                                                        # TODO: i32.div_u
                                                        v1 = ((load32(v5) * 60) if (u32(v1) < u32(100)) else 100)
                                                    while True:  # $label238
                                                        if (u32(v1) <= u32(v4)):
                                                            break
                                                        if load8u(v3 + 354):
                                                            break
                                                        v3 = (v8 + (v2 * 1056))
                                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                                        v4 = (v1 - v4)
                                                        store32(v3 + 108, (v1 - v4))
                                                        v66 = i32(v1)
                                                        storef32(v3 + 100, (200.0 / i32(v1)))
                                                        storef32(v3 + 96, ((i32(v4) * 200.0) / v66))
                                                        v1 = load32(9140296)
                                                        store32(9140296, (load32(9140296) + 1))
                                                        store32(((v1 << 2) + 8451904), v2)
                                                        break
                                                    v1 = load32(38512)
                                                    v2 = (v8 + (load32(38512) << 2))
                                                    v3 = (load32(((v8 + (load32(38512) << 2)) + 282828)) + load32((v2 + 281808)))
                                                    v2 = 14
                                                    v4 = ((v1 * 404) + ENTITY_TYPES)
                                                    if (u32(load32(((v1 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                        v2 = (load32(v5) * 14)
                                                        # TODO: i32.div_u
                                                        v2 = ((load32(v5) * 14) if (u32(v2) < u32(100)) else 100)
                                                    if (u32(v2) <= u32(v3)):
                                                        break
                                                    if load8u(v4 + 354):
                                                        break
                                                    v66 = 301.0
                                                    v67 = i32(v2)
                                                    storef32((v8 + (v1 * 1056)) + 100, (301.0 / i32(v2)))
                                                    break
                                                v1 = load32(38500)
                                                v2 = (v8 + (load32(38500) << 2))
                                                v3 = (load32(((v8 + (load32(38500) << 2)) + 282828)) + load32((v2 + 281808)))
                                                v2 = 15
                                                v4 = ((v1 * 404) + ENTITY_TYPES)
                                                if (u32(load32(((v1 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                    v2 = (load32(v5) * 15)
                                                    # TODO: i32.div_u
                                                    v2 = ((load32(v5) * 15) if (u32(v2) < u32(100)) else 100)
                                                if (u32(v2) <= u32(v3)):
                                                    break
                                                if load8u(v4 + 354):
                                                    break
                                                v66 = 800.0
                                                v67 = i32(v2)
                                                storef32((v8 + (v1 * 1056)) + 100, (800.0 / i32(v2)))
                                                break
                                            v2 = (v2 - v3)
                                            v3 = (v8 + (v1 * 1056))
                                            store8(((v8 + (v1 * 1056)) + 1150), 1)
                                            store32(v3 + 108, v2)
                                            storef32(v3 + 96, ((v66 * i32(v2)) / v67))
                                            v2 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v2 << 2) + 8451904), v1)
                                            break
                                        while True:  # $label240
                                            if (v14 > 79999):
                                                break
                                            v2 = load32(39076)
                                            v1 = (v8 + (load32(39076) << 2))
                                            v4 = (load32(((v8 + (load32(39076) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v3 = ((v2 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (152.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 152.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39100)
                                        v1 = (v8 + (load32(39100) << 2))
                                        v4 = (load32(((v8 + (load32(39100) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label241
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (151.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 151.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        while True:  # $label242
                                            if (v12 > 79999):
                                                break
                                            v2 = load32(39068)
                                            v1 = (v8 + (load32(39068) << 2))
                                            v4 = (load32(((v8 + (load32(39068) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v3 = ((v2 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (150.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 150.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        while True:  # $label243
                                            if (v17 > 39999):
                                                break
                                            v2 = load32(39072)
                                            v1 = (v8 + (load32(39072) << 2))
                                            v4 = (load32(((v8 + (load32(39072) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v3 = ((v2 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (110.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 110.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        while True:  # $label244
                                            if v16:
                                                break
                                            v2 = load32(39084)
                                            v1 = (v8 + (load32(39084) << 2))
                                            v4 = (load32(((v8 + (load32(39084) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v3 = ((v2 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (200.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 200.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(38492)
                                        v1 = (v8 + (load32(38492) << 2))
                                        v4 = (load32(((v8 + (load32(38492) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 7
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) * 7)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) * 7) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label245
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (800.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 800.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39088)
                                        v1 = (v8 + (load32(39088) << 2))
                                        v4 = (load32(((v8 + (load32(39088) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label246
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (95.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 95.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39080)
                                        v1 = (v8 + (load32(39080) << 2))
                                        v4 = (load32(((v8 + (load32(39080) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label247
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (95.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 95.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39092)
                                        v1 = (v8 + (load32(39092) << 2))
                                        v4 = (load32(((v8 + (load32(39092) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label248
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (95.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 95.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39112)
                                        v1 = (v8 + (load32(39112) << 2))
                                        v4 = (load32(((v8 + (load32(39112) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label249
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (40.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 40.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39124)
                                        v1 = (v8 + (load32(39124) << 2))
                                        v4 = (load32(((v8 + (load32(39124) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label250
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (41.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 41.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39116)
                                        v1 = (v8 + (load32(39116) << 2))
                                        v4 = (load32(((v8 + (load32(39116) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label251
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (42.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 42.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39180)
                                        v1 = (v8 + (load32(39180) << 2))
                                        v4 = (load32(((v8 + (load32(39180) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label252
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (40.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 40.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39140)
                                        v1 = (v8 + (load32(39140) << 2))
                                        v4 = (load32(((v8 + (load32(39140) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label253
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (41.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 41.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39148)
                                        v1 = (v8 + (load32(39148) << 2))
                                        v4 = (load32(((v8 + (load32(39148) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label254
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (31.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 31.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(38440)
                                        v1 = (v8 + (load32(38440) << 2))
                                        v4 = (load32(((v8 + (load32(38440) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 3
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) * 3)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) * 3) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label255
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (30.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 30.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v1 = 2
                                        v2 = load32(38808)
                                        v3 = (v8 + (load32(38808) << 2))
                                        v4 = (load32(((v8 + (load32(38808) << 2)) + 282828)) + load32((v3 + 281808)))
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) << 1)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) << 1) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label256
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (71.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 71.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(38456)
                                        v1 = (v8 + (load32(38456) << 2))
                                        v4 = (load32(((v8 + (load32(38456) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 5
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) * 5)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) * 5) if (u32(v1) < u32(100)) else 100)
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (70.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 70.0) / v66))
                                        v3 = load32(9140296)
                                        v1 = (load32(9140296) + 1)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v3 << 2) + 8451904), v2)
                                        break
                                    if (load32(39220) == v2):
                                        v4 = load32(38756)
                                        v2 = (v8 + (load32(38756) << 2))
                                        v6 = load32(((v8 + (load32(38756) << 2)) + 281808))
                                        v7 = load32((v2 + 282828))
                                        while True:  # $label259
                                            # TODO: i32.div_u
                                            v1 = 100
                                            # TODO: i32.div_u
                                            v2 = 100
                                            v48 = ((v1 * 35) - 100)
                                            v106 = i32(((v1 * 35) - 100))
                                            v105 = (i32(((v1 * 35) - 100)) * 0.3)
                                            if (((i32(((v1 * 35) - 100)) * 0.3) < 4294967296.0) & (v105 >= 0.0)):
                                                break
                                            break
                                        v1 = 0
                                        v3 = 0
                                        v10 = ((v4 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v4 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v3 = (load32(v5) * v1)
                                            # TODO: i32.div_u
                                            v3 = ((load32(v5) * v1) if (u32(v3) < u32(100)) else 100)
                                        while True:  # $label260
                                            v7 = (v6 + v7)
                                            if (u32((v6 + v7)) >= u32(v3)):
                                                break
                                            if load8u(v10 + 354):
                                                break
                                            v6 = (v8 + (v4 * 1056))
                                            store8(((v8 + (v4 * 1056)) + 1150), 1)
                                            v7 = (v3 - v7)
                                            store32(v6 + 108, (v3 - v7))
                                            v66 = i32(v3)
                                            storef32(v6 + 100, (90.0 / i32(v3)))
                                            storef32(v6 + 96, ((i32(v7) * 90.0) / v66))
                                            v3 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v3 << 2) + 8451904), v4)
                                            break
                                        v4 = load32(38740)
                                        v3 = (v8 + (load32(38740) << 2))
                                        v6 = load32(((v8 + (load32(38740) << 2)) + 281808))
                                        v7 = load32((v3 + 282828))
                                        v10 = ((v4 * 404) + ENTITY_TYPES)
                                        v15 = (u32(load32(((v4 * 404) + ENTITY_TYPES) + 264)) > u32(1))
                                        while True:  # $label261
                                            v105 = (v106 * 0.1)
                                            if (((v106 * 0.1) < 4294967296.0) & (v105 >= 0.0)):
                                                break
                                            break
                                        v3 = 0
                                        if not v15:
                                            v3 = (load32(v5) * v3)
                                            # TODO: i32.div_u
                                            v3 = ((load32(v5) * v3) if (u32(v3) < u32(100)) else 100)
                                        while True:  # $label262
                                            v7 = (v6 + v7)
                                            if (u32((v6 + v7)) >= u32(v3)):
                                                break
                                            if load8u(v10 + 354):
                                                break
                                            v6 = (v8 + (v4 * 1056))
                                            store8(((v8 + (v4 * 1056)) + 1150), 1)
                                            v7 = (v3 - v7)
                                            store32(v6 + 108, (v3 - v7))
                                            v66 = i32(v3)
                                            storef32(v6 + 100, (120.0 / i32(v3)))
                                            storef32(v6 + 96, ((i32(v7) * 120.0) / v66))
                                            v3 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v3 << 2) + 8451904), v4)
                                            break
                                        v4 = load32(38736)
                                        v3 = (v8 + (load32(38736) << 2))
                                        v7 = (load32(((v8 + (load32(38736) << 2)) + 282828)) + load32((v3 + 281808)))
                                        v3 = v1
                                        v6 = ((v4 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v4 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v3 = (load32(v5) * v1)
                                            # TODO: i32.div_u
                                            v3 = ((load32(v5) * v1) if (u32(v3) < u32(100)) else 100)
                                        while True:  # $label263
                                            if (u32(v3) <= u32(v7)):
                                                break
                                            if load8u(v6 + 354):
                                                break
                                            v6 = (v8 + (v4 * 1056))
                                            store8(((v8 + (v4 * 1056)) + 1150), 1)
                                            v7 = (v3 - v7)
                                            store32(v6 + 108, (v3 - v7))
                                            v66 = i32(v3)
                                            storef32(v6 + 100, (120.0 / i32(v3)))
                                            storef32(v6 + 96, ((i32(v7) * 120.0) / v66))
                                            v3 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v3 << 2) + 8451904), v4)
                                            break
                                        v3 = load32(38776)
                                        v4 = (v8 + (load32(38776) << 2))
                                        v6 = (load32(((v8 + (load32(38776) << 2)) + 282828)) + load32((v4 + 281808)))
                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) * v1)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) * v1) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label264
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (80.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 80.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v3 = load32(38820)
                                        v6 = ((load32(38820) * 404) + ENTITY_TYPES)
                                        v7 = load32(((load32(38820) * 404) + ENTITY_TYPES) + 264)
                                        while True:  # $label265
                                            while True:  # $label266
                                                v1 = (v8 + (v3 << 2))
                                                v4 = (load32(((v8 + (v3 << 2)) + 282828)) + load32((v1 + 281808)))
                                                if (u32((load32(((v8 + (v3 << 2)) + 282828)) + load32((v1 + 281808)))) <= u32(16)):
                                                    v1 = 17
                                                    if (u32(v7) <= u32(1)):
                                                        v1 = (load32(v5) * 17)
                                                        # TODO: i32.div_u
                                                        v1 = ((load32(v5) * 17) if (u32(v1) < u32(100)) else 100)
                                                    if (u32(v1) <= u32(v4)):
                                                        break
                                                    if load8u(v6 + 354):
                                                        break
                                                    v67 = 130.0
                                                    break
                                                v1 = 34
                                                if (u32(v7) <= u32(1)):
                                                    v1 = (load32(v5) * 34)
                                                    # TODO: i32.div_u
                                                    v1 = ((load32(v5) * 34) if (u32(v1) < u32(100)) else 100)
                                                if (u32(v1) <= u32(v4)):
                                                    break
                                                if load8u(v6 + 354):
                                                    break
                                                v67 = 20.0
                                                break
                                            v66 = i32(v1)
                                            v6 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v1 = (v1 - v4)
                                            store32(v6 + 108, (v1 - v4))
                                            storef32(v6 + 100, (v67 / v66))
                                            storef32(v6 + 96, ((v67 * i32(v1)) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v3 = load32(38800)
                                        v1 = (v8 + (load32(38800) << 2))
                                        v6 = (load32(((v8 + (load32(38800) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label267
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (181.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 181.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v3 = load32(38824)
                                        v1 = (v8 + (load32(38824) << 2))
                                        v6 = (load32(((v8 + (load32(38824) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label268
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (180.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 180.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v3 = load32(38812)
                                        v1 = (v8 + (load32(38812) << 2))
                                        v6 = (load32(((v8 + (load32(38812) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label269
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (180.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 180.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v3 = load32(39192)
                                        v1 = (v8 + (load32(39192) << 2))
                                        v6 = (load32(((v8 + (load32(39192) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label270
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (95.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 95.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v3 = load32(38848)
                                        v1 = (v8 + (load32(38848) << 2))
                                        v6 = (load32(((v8 + (load32(38848) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label271
                                            if (u32(v1) <= u32(v6)):
                                                break
                                            if load8u(v4 + 354):
                                                break
                                            v4 = (v8 + (v3 * 1056))
                                            store8(((v8 + (v3 * 1056)) + 1150), 1)
                                            v6 = (v1 - v6)
                                            store32(v4 + 108, (v1 - v6))
                                            v66 = i32(v1)
                                            storef32(v4 + 100, (131.0 / i32(v1)))
                                            storef32(v4 + 96, ((i32(v6) * 131.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v3)
                                            break
                                        v1 = (v8 + (v13 << 2))
                                        v3 = (load32(((v8 + (v13 << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = ((v13 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v13 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v2 = (load32(v5) * v2)
                                            # TODO: i32.div_u
                                            v2 = ((load32(v5) * v2) if (u32(v2) < u32(100)) else 100)
                                        while True:  # $label272
                                            if (u32(v2) <= u32(v3)):
                                                break
                                            if load8u(v1 + 354):
                                                break
                                            v1 = (v8 + (v13 * 1056))
                                            store8(((v8 + (v13 * 1056)) + 1150), 1)
                                            v3 = (v2 - v3)
                                            store32(v1 + 108, (v2 - v3))
                                            v66 = i32(v2)
                                            storef32(v1 + 100, (400.0 / i32(v2)))
                                            storef32(v1 + 96, ((i32(v3) * 400.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v13)
                                            break
                                        while True:  # $label273
                                            if (load32((v8 + 283856)) > 1999):
                                                break
                                            v2 = load32(39212)
                                            v1 = (v8 + (load32(39212) << 2))
                                            v4 = (load32(((v8 + (load32(39212) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v3 = ((v2 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (1001.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 1001.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        while True:  # $label274
                                            if (v11 > 7999999):
                                                break
                                            while True:  # $label277
                                                if v16:
                                                    v2 = load32(38528)
                                                    v4 = ((load32(38528) * 404) + ENTITY_TYPES)
                                                    v6 = load32(((load32(38528) * 404) + ENTITY_TYPES) + 264)
                                                    while True:  # $label275
                                                        while True:  # $label276
                                                            v1 = (v8 + (v2 << 2))
                                                            v3 = (load32(((v8 + (v2 << 2)) + 282828)) + load32((v1 + 281808)))
                                                            if (u32((load32(((v8 + (v2 << 2)) + 282828)) + load32((v1 + 281808)))) <= u32(8)):
                                                                v1 = 60
                                                                if (u32(v6) <= u32(1)):
                                                                    v1 = (load32(v5) * 60)
                                                                    # TODO: i32.div_u
                                                                    v1 = ((load32(v5) * 60) if (u32(v1) < u32(100)) else 100)
                                                                if (u32(v1) <= u32(v3)):
                                                                    break
                                                                if load8u(v4 + 354):
                                                                    break
                                                                v67 = 200.0
                                                                break
                                                            v1 = 60
                                                            if (u32(v6) <= u32(1)):
                                                                v1 = (load32(v5) * 60)
                                                                # TODO: i32.div_u
                                                                v1 = ((load32(v5) * 60) if (u32(v1) < u32(100)) else 100)
                                                            if (u32(v1) <= u32(v3)):
                                                                break
                                                            if load8u(v4 + 354):
                                                                break
                                                            v67 = 80.0
                                                            break
                                                        v66 = i32(v1)
                                                        v4 = (v8 + (v2 * 1056))
                                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                                        v1 = (v1 - v3)
                                                        store32(v4 + 108, (v1 - v3))
                                                        storef32(v4 + 100, (v67 / v66))
                                                        storef32(v4 + 96, ((v67 * i32(v1)) / v66))
                                                        v1 = load32(9140296)
                                                        store32(9140296, (load32(9140296) + 1))
                                                        store32(((v1 << 2) + 8451904), v2)
                                                        break
                                                    v1 = load32(38792)
                                                    v2 = (v8 + (load32(38792) << 2))
                                                    v3 = (load32(((v8 + (load32(38792) << 2)) + 282828)) + load32((v2 + 281808)))
                                                    v2 = 14
                                                    v4 = ((v1 * 404) + ENTITY_TYPES)
                                                    if (u32(load32(((v1 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                        v2 = (load32(v5) * 14)
                                                        # TODO: i32.div_u
                                                        v2 = ((load32(v5) * 14) if (u32(v2) < u32(100)) else 100)
                                                    if (u32(v2) <= u32(v3)):
                                                        break
                                                    if load8u(v4 + 354):
                                                        break
                                                    v66 = 275.0
                                                    v67 = i32(v2)
                                                    storef32((v8 + (v1 * 1056)) + 100, (275.0 / i32(v2)))
                                                    break
                                                v2 = load32(38500)
                                                v1 = (v8 + (load32(38500) << 2))
                                                v4 = (load32(((v8 + (load32(38500) << 2)) + 282828)) + load32((v1 + 281808)))
                                                v1 = 15
                                                v3 = ((v2 * 404) + ENTITY_TYPES)
                                                if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                    v1 = (load32(v5) * 15)
                                                    # TODO: i32.div_u
                                                    v1 = ((load32(v5) * 15) if (u32(v1) < u32(100)) else 100)
                                                while True:  # $label278
                                                    if (u32(v1) <= u32(v4)):
                                                        break
                                                    if load8u(v3 + 354):
                                                        break
                                                    v3 = (v8 + (v2 * 1056))
                                                    store8(((v8 + (v2 * 1056)) + 1150), 1)
                                                    v4 = (v1 - v4)
                                                    store32(v3 + 108, (v1 - v4))
                                                    v66 = i32(v1)
                                                    storef32(v3 + 100, (800.0 / i32(v1)))
                                                    storef32(v3 + 96, ((i32(v4) * 800.0) / v66))
                                                    v1 = load32(9140296)
                                                    store32(9140296, (load32(9140296) + 1))
                                                    store32(((v1 << 2) + 8451904), v2)
                                                    break
                                                v1 = load32(39084)
                                                v2 = (v8 + (load32(39084) << 2))
                                                v3 = (load32(((v8 + (load32(39084) << 2)) + 282828)) + load32((v2 + 281808)))
                                                v2 = 1
                                                v4 = ((v1 * 404) + ENTITY_TYPES)
                                                if (u32(load32(((v1 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                    v2 = load32(v5)
                                                    # TODO: i32.div_u
                                                    v2 = (load32(v5) if (u32(v2) < u32(100)) else 100)
                                                if (u32(v2) <= u32(v3)):
                                                    break
                                                if load8u(v4 + 354):
                                                    break
                                                v66 = 200.0
                                                v67 = i32(v2)
                                                storef32((v8 + (v1 * 1056)) + 100, (200.0 / i32(v2)))
                                                break
                                            v2 = (v2 - v3)
                                            v3 = (v8 + (v1 * 1056))
                                            store8(((v8 + (v1 * 1056)) + 1150), 1)
                                            store32(v3 + 108, v2)
                                            storef32(v3 + 96, ((v66 * i32(v2)) / v67))
                                            v2 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v2 << 2) + 8451904), v1)
                                            break
                                        while True:  # $label279
                                            if (v14 > 79999):
                                                break
                                            v2 = load32(39076)
                                            v1 = (v8 + (load32(39076) << 2))
                                            v4 = (load32(((v8 + (load32(39076) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v3 = ((v2 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (152.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 152.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        while True:  # $label280
                                            if (v12 > 79999):
                                                break
                                            v2 = load32(39068)
                                            v1 = (v8 + (load32(39068) << 2))
                                            v4 = (load32(((v8 + (load32(39068) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v3 = ((v2 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (150.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 150.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        while True:  # $label281
                                            if (v17 > 39999):
                                                break
                                            v2 = load32(39072)
                                            v1 = (v8 + (load32(39072) << 2))
                                            v4 = (load32(((v8 + (load32(39072) << 2)) + 282828)) + load32((v1 + 281808)))
                                            v1 = 1
                                            v3 = ((v2 * 404) + ENTITY_TYPES)
                                            if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                                v1 = load32(v5)
                                                # TODO: i32.div_u
                                                v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (125.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 125.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(38788)
                                        v1 = (v8 + (load32(38788) << 2))
                                        v4 = (load32(((v8 + (load32(38788) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 4
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) << 2)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) << 2) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label282
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (800.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 800.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39204)
                                        v1 = (v8 + (load32(39204) << 2))
                                        v4 = (load32(((v8 + (load32(39204) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label283
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (125.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 125.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39112)
                                        v1 = (v8 + (load32(39112) << 2))
                                        v4 = (load32(((v8 + (load32(39112) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label284
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (60.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 60.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39080)
                                        v1 = (v8 + (load32(39080) << 2))
                                        v4 = (load32(((v8 + (load32(39080) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label285
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (95.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 95.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39088)
                                        v1 = (v8 + (load32(39088) << 2))
                                        v4 = (load32(((v8 + (load32(39088) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label286
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (95.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 95.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39196)
                                        v1 = (v8 + (load32(39196) << 2))
                                        v4 = (load32(((v8 + (load32(39196) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label287
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (95.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 95.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39092)
                                        v1 = (v8 + (load32(39092) << 2))
                                        v4 = (load32(((v8 + (load32(39092) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label288
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (50.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 50.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39116)
                                        v1 = (v8 + (load32(39116) << 2))
                                        v4 = (load32(((v8 + (load32(39116) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label289
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (44.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 44.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39120)
                                        v1 = (v8 + (load32(39120) << 2))
                                        v4 = (load32(((v8 + (load32(39120) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label290
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (44.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 44.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39180)
                                        v1 = (v8 + (load32(39180) << 2))
                                        v4 = (load32(((v8 + (load32(39180) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label291
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (40.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 40.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39140)
                                        v1 = (v8 + (load32(39140) << 2))
                                        v4 = (load32(((v8 + (load32(39140) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label292
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (42.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 42.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39208)
                                        v1 = (v8 + (load32(39208) << 2))
                                        v4 = (load32(((v8 + (load32(39208) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label293
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (75.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 75.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(39200)
                                        v1 = (v8 + (load32(39200) << 2))
                                        v4 = (load32(((v8 + (load32(39200) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label294
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (31.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 31.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(38772)
                                        v1 = (v8 + (load32(38772) << 2))
                                        v4 = (load32(((v8 + (load32(38772) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 3
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) * 3)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) * 3) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label295
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (30.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 30.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(38836)
                                        v1 = (v8 + (load32(38836) << 2))
                                        v4 = (load32(((v8 + (load32(38836) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 1
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = load32(v5)
                                            # TODO: i32.div_u
                                            v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label296
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (37.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 37.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v1 = 2
                                        v2 = load32(38808)
                                        v3 = (v8 + (load32(38808) << 2))
                                        v4 = (load32(((v8 + (load32(38808) << 2)) + 282828)) + load32((v3 + 281808)))
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) << 1)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) << 1) if (u32(v1) < u32(100)) else 100)
                                        while True:  # $label297
                                            if (u32(v1) <= u32(v4)):
                                                break
                                            if load8u(v3 + 354):
                                                break
                                            v3 = (v8 + (v2 * 1056))
                                            store8(((v8 + (v2 * 1056)) + 1150), 1)
                                            v4 = (v1 - v4)
                                            store32(v3 + 108, (v1 - v4))
                                            v66 = i32(v1)
                                            storef32(v3 + 100, (36.0 / i32(v1)))
                                            storef32(v3 + 96, ((i32(v4) * 36.0) / v66))
                                            v1 = load32(9140296)
                                            store32(9140296, (load32(9140296) + 1))
                                            store32(((v1 << 2) + 8451904), v2)
                                            break
                                        v2 = load32(38764)
                                        v1 = (v8 + (load32(38764) << 2))
                                        v4 = (load32(((v8 + (load32(38764) << 2)) + 282828)) + load32((v1 + 281808)))
                                        v1 = 5
                                        v3 = ((v2 * 404) + ENTITY_TYPES)
                                        if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                            v1 = (load32(v5) * 5)
                                            # TODO: i32.div_u
                                            v1 = ((load32(v5) * 5) if (u32(v1) < u32(100)) else 100)
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (35.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 35.0) / v66))
                                        v3 = load32(9140296)
                                        v1 = (load32(9140296) + 1)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v3 << 2) + 8451904), v2)
                                        break
                                    v3 = load32(38692)
                                    v2 = (v8 + (load32(38692) << 2))
                                    v4 = load32(((v8 + (load32(38692) << 2)) + 281808))
                                    v6 = load32((v2 + 282828))
                                    while True:  # $label298
                                        # TODO: i32.div_u
                                        v1 = 100
                                        # TODO: i32.div_u
                                        v2 = 100
                                        v48 = ((v1 * 35) - 100)
                                        v106 = i32(((v1 * 35) - 100))
                                        v105 = (i32(((v1 * 35) - 100)) * 0.4)
                                        if (((i32(((v1 * 35) - 100)) * 0.4) < 4294967296.0) & (v105 >= 0.0)):
                                            break
                                        break
                                    v1 = 0
                                    v7 = ((v3 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = (load32(v5) * v1)
                                        # TODO: i32.div_u
                                        v1 = ((load32(v5) * v1) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label299
                                        v6 = (v4 + v6)
                                        if (u32((v4 + v6)) >= u32(v1)):
                                            break
                                        if load8u(v7 + 354):
                                            break
                                        v4 = (v8 + (v3 * 1056))
                                        store8(((v8 + (v3 * 1056)) + 1150), 1)
                                        v6 = (v1 - v6)
                                        store32(v4 + 108, (v1 - v6))
                                        v66 = i32(v1)
                                        storef32(v4 + 100, (90.0 / i32(v1)))
                                        storef32(v4 + 96, ((i32(v6) * 90.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v3)
                                        break
                                    v4 = load32(38684)
                                    v1 = (v8 + (load32(38684) << 2))
                                    v6 = load32(((v8 + (load32(38684) << 2)) + 281808))
                                    v7 = load32((v1 + 282828))
                                    v10 = ((v4 * 404) + ENTITY_TYPES)
                                    v15 = (u32(load32(((v4 * 404) + ENTITY_TYPES) + 264)) > u32(1))
                                    while True:  # $label300
                                        v105 = (v106 * 0.3)
                                        if (((v106 * 0.3) < 4294967296.0) & (v105 >= 0.0)):
                                            break
                                        break
                                    v1 = 0
                                    v3 = 0
                                    if not v15:
                                        v3 = (load32(v5) * v1)
                                        # TODO: i32.div_u
                                        v3 = ((load32(v5) * v1) if (u32(v3) < u32(100)) else 100)
                                    while True:  # $label301
                                        v7 = (v6 + v7)
                                        if (u32((v6 + v7)) >= u32(v3)):
                                            break
                                        if load8u(v10 + 354):
                                            break
                                        v6 = (v8 + (v4 * 1056))
                                        store8(((v8 + (v4 * 1056)) + 1150), 1)
                                        v7 = (v3 - v7)
                                        store32(v6 + 108, (v3 - v7))
                                        v66 = i32(v3)
                                        storef32(v6 + 100, (120.0 / i32(v3)))
                                        storef32(v6 + 96, ((i32(v7) * 120.0) / v66))
                                        v3 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v3 << 2) + 8451904), v4)
                                        break
                                    v3 = load32(38680)
                                    v4 = (v8 + (load32(38680) << 2))
                                    v6 = (load32(((v8 + (load32(38680) << 2)) + 282828)) + load32((v4 + 281808)))
                                    v4 = ((v3 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = (load32(v5) * v1)
                                        # TODO: i32.div_u
                                        v1 = ((load32(v5) * v1) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label302
                                        if (u32(v1) <= u32(v6)):
                                            break
                                        if load8u(v4 + 354):
                                            break
                                        v4 = (v8 + (v3 * 1056))
                                        store8(((v8 + (v3 * 1056)) + 1150), 1)
                                        v6 = (v1 - v6)
                                        store32(v4 + 108, (v1 - v6))
                                        v66 = i32(v1)
                                        storef32(v4 + 100, (120.0 / i32(v1)))
                                        storef32(v4 + 96, ((i32(v6) * 120.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v3)
                                        break
                                    v3 = load32(38700)
                                    v1 = (v8 + (load32(38700) << 2))
                                    v6 = (load32(((v8 + (load32(38700) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 17
                                    v4 = ((v3 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v3 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = (load32(v5) * 17)
                                        # TODO: i32.div_u
                                        v1 = ((load32(v5) * 17) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label303
                                        if (u32(v1) <= u32(v6)):
                                            break
                                        if load8u(v4 + 354):
                                            break
                                        v4 = (v8 + (v3 * 1056))
                                        store8(((v8 + (v3 * 1056)) + 1150), 1)
                                        v6 = (v1 - v6)
                                        store32(v4 + 108, (v1 - v6))
                                        v66 = i32(v1)
                                        storef32(v4 + 100, (130.0 / i32(v1)))
                                        storef32(v4 + 96, ((i32(v6) * 130.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v3)
                                        break
                                    v1 = (v8 + (v13 << 2))
                                    v3 = (load32(((v8 + (v13 << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = ((v13 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v13 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v2 = (load32(v5) * v2)
                                        # TODO: i32.div_u
                                        v2 = ((load32(v5) * v2) if (u32(v2) < u32(100)) else 100)
                                    while True:  # $label304
                                        if (u32(v2) <= u32(v3)):
                                            break
                                        if load8u(v1 + 354):
                                            break
                                        v1 = (v8 + (v13 * 1056))
                                        store8(((v8 + (v13 * 1056)) + 1150), 1)
                                        v3 = (v2 - v3)
                                        store32(v1 + 108, (v2 - v3))
                                        v66 = i32(v2)
                                        storef32(v1 + 100, (1000.0 / i32(v2)))
                                        storef32(v1 + 96, ((i32(v3) * 1000.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v13)
                                        break
                                    v2 = load32(39096)
                                    v1 = (v8 + (load32(39096) << 2))
                                    v4 = (load32(((v8 + (load32(39096) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label305
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (1001.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 1001.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(38500)
                                    v1 = (v8 + (load32(38500) << 2))
                                    v4 = (load32(((v8 + (load32(38500) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 24
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = (load32(v5) * 24)
                                        # TODO: i32.div_u
                                        v1 = ((load32(v5) * 24) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label306
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (800.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 800.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39172)
                                    v1 = (v8 + (load32(39172) << 2))
                                    v4 = (load32(((v8 + (load32(39172) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label307
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (50.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 50.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39176)
                                    v1 = (v8 + (load32(39176) << 2))
                                    v4 = (load32(((v8 + (load32(39176) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label308
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (40.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 40.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39076)
                                    v1 = (v8 + (load32(39076) << 2))
                                    v4 = (load32(((v8 + (load32(39076) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label309
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (50.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 50.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39068)
                                    v1 = (v8 + (load32(39068) << 2))
                                    v4 = (load32(((v8 + (load32(39068) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label310
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (50.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 50.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39072)
                                    v1 = (v8 + (load32(39072) << 2))
                                    v4 = (load32(((v8 + (load32(39072) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label311
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (50.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 50.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39084)
                                    v1 = (v8 + (load32(39084) << 2))
                                    v4 = (load32(((v8 + (load32(39084) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label312
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (60.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 60.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39152)
                                    v1 = (v8 + (load32(39152) << 2))
                                    v4 = (load32(((v8 + (load32(39152) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label313
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (59.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 59.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    while True:  # $label314
                                        v1 = load32(38864)
                                        v2 = ((load32(38864) * 404) + ENTITY_TYPES)
                                        if (u32(load32(((load32(38864) * 404) + ENTITY_TYPES) + 264)) > u32(1)):
                                            break
                                        v3 = (v8 + (v1 << 2))
                                        if (load32(((v8 + (v1 << 2)) + 282828)) != (0 - load32((v3 + 281808)))):
                                            break
                                        if load8u(v2 + 354):
                                            break
                                        v2 = (v8 + (v1 * 1056))
                                        store8(((v8 + (v1 * 1056)) + 1150), 1)
                                        store32(v2 + 108, 1)
                                        store64(v2 + 96, 4692750812812673024)
                                        v2 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v2 << 2) + 8451904), v1)
                                        break
                                    v2 = load32(39080)
                                    v1 = (v8 + (load32(39080) << 2))
                                    v4 = (load32(((v8 + (load32(39080) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label315
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (50.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 50.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39088)
                                    v1 = (v8 + (load32(39088) << 2))
                                    v4 = (load32(((v8 + (load32(39088) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label316
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (50.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 50.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39092)
                                    v1 = (v8 + (load32(39092) << 2))
                                    v4 = (load32(((v8 + (load32(39092) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label317
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (50.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 50.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39116)
                                    v1 = (v8 + (load32(39116) << 2))
                                    v4 = (load32(((v8 + (load32(39116) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label318
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (46.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 46.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39184)
                                    v1 = (v8 + (load32(39184) << 2))
                                    v4 = (load32(((v8 + (load32(39184) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label319
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (46.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 46.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39180)
                                    v1 = (v8 + (load32(39180) << 2))
                                    v4 = (load32(((v8 + (load32(39180) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label320
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (42.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 42.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39160)
                                    v1 = (v8 + (load32(39160) << 2))
                                    v4 = (load32(((v8 + (load32(39160) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label321
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (31.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 31.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(39156)
                                    v1 = (v8 + (load32(39156) << 2))
                                    v4 = (load32(((v8 + (load32(39156) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 1
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = load32(v5)
                                        # TODO: i32.div_u
                                        v1 = (load32(v5) if (u32(v1) < u32(100)) else 100)
                                    while True:  # $label322
                                        if (u32(v1) <= u32(v4)):
                                            break
                                        if load8u(v3 + 354):
                                            break
                                        v3 = (v8 + (v2 * 1056))
                                        store8(((v8 + (v2 * 1056)) + 1150), 1)
                                        v4 = (v1 - v4)
                                        store32(v3 + 108, (v1 - v4))
                                        v66 = i32(v1)
                                        storef32(v3 + 100, (25.0 / i32(v1)))
                                        storef32(v3 + 96, ((i32(v4) * 25.0) / v66))
                                        v1 = load32(9140296)
                                        store32(9140296, (load32(9140296) + 1))
                                        store32(((v1 << 2) + 8451904), v2)
                                        break
                                    v2 = load32(38928)
                                    v1 = (v8 + (load32(38928) << 2))
                                    v4 = (load32(((v8 + (load32(38928) << 2)) + 282828)) + load32((v1 + 281808)))
                                    v1 = 3
                                    v3 = ((v2 * 404) + ENTITY_TYPES)
                                    if (u32(load32(((v2 * 404) + ENTITY_TYPES) + 264)) <= u32(1)):
                                        v1 = (load32(v5) * 3)
                                        # TODO: i32.div_u
                                        v1 = ((load32(v5) * 3) if (u32(v1) < u32(100)) else 100)
                                    if (u32(v1) <= u32(v4)):
                                        break
                                    if load8u(v3 + 354):
                                        break
                                    v3 = (v8 + (v2 * 1056))
                                    store8(((v8 + (v2 * 1056)) + 1150), 1)
                                    v4 = (v1 - v4)
                                    store32(v3 + 108, (v1 - v4))
                                    v66 = i32(v1)
                                    storef32(v3 + 100, (30.0 / i32(v1)))
                                    storef32(v3 + 96, ((i32(v4) * 30.0) / v66))
                                    v3 = load32(9140296)
                                    v1 = (load32(9140296) + 1)
                                    store32(9140296, (load32(9140296) + 1))
                                    store32(((v3 << 2) + 8451904), v2)
                                    break
                                    break
                                v1 = load32(9140296)
                                break
                            v15 = 0
                            v73 = 0.0
                            v75 = 0.0
                            v76 = 0.0
                            v80 = 0.0
                            v68 = 0.0
                            v66 = 0.0
                            v67 = 0.0
                            v70 = 0.0
                            if v1:
                                while True:  # $label328
                                    v1 = load32(((v15 << 2) + 8451904))
                                    v20 = (v8 + (load32(((v15 << 2) + 8451904)) * 1056))
                                    v71 = loadf32((v8 + (load32(((v15 << 2) + 8451904)) * 1056)) + 96)
                                    v2 = ((v1 * 404) + ENTITY_TYPES)
                                    v3 = load32(((v1 * 404) + ENTITY_TYPES) + 180)
                                    v10 = load32(load32(((v1 * 404) + ENTITY_TYPES) + 180) + 112)
                                    if load32(load32(((v1 * 404) + ENTITY_TYPES) + 180) + 112):
                                        v69 = (v71 + 1.0)
                                        v1 = 0
                                        while True:  # $label324
                                            v6 = load32((v3 + (v1 << 2)) + 72)
                                            v21 = ((load32((v3 + (v1 << 2)) + 72) * 404) + ENTITY_TYPES)
                                            if (load32(((load32((v3 + (v1 << 2)) + 72) * 404) + ENTITY_TYPES) + 196) == load32(v9)):
                                                while True:  # $label323
                                                    v4 = (v8 + (v6 * 1056))
                                                    v26 = ((v8 + (v6 * 1056)) + 1150)
                                                    if load8u(((v8 + (v6 * 1056)) + 1150)):
                                                        break
                                                    v7 = (v8 + (v6 << 2))
                                                    v18 = (load32(((v8 + (v6 << 2)) + 282828)) + load32((v7 + 281808)))
                                                    v7 = 1
                                                    if (u32(load32(v21 + 264)) <= u32(1)):
                                                        v7 = load32(v5)
                                                        # TODO: i32.div_u
                                                        v7 = (load32(v5) if (u32(v7) < u32(100)) else 100)
                                                    if (u32(v7) <= u32(v18)):
                                                        break
                                                    if load8u(v21 + 354):
                                                        break
                                                    v10 = (v7 - v18)
                                                    store32(v4 + 108, (v7 - v18))
                                                    v74 = i32(v7)
                                                    storef32(v4 + 100, (v69 / i32(v7)))
                                                    store8(v26, 1)
                                                    storef32(v4 + 96, ((v69 * i32(v10)) / v74))
                                                    v7 = load32(9140296)
                                                    store32(9140296, (load32(9140296) + 1))
                                                    store32(((v7 << 2) + 8451904), v6)
                                                    v10 = load32(v3 + 112)
                                                    break
                                                store32(v4 + 104, (load32(v4 + 104) + (load32(v20 + 108) * load32(v2 + 116))))
                                            v1 = (v1 + 1)
                                            if (u32((v1 + 1)) < u32(v10)):
                                                continue
                                            break
                                    v6 = load32(v3 + 68)
                                    if load32(v3 + 68):
                                        v71 = (v71 + 1.0)
                                        v1 = 0
                                        while True:  # $label327
                                            while True:  # $label325
                                                v7 = load32((v3 + (v1 << 2)) + 28)
                                                v10 = (v8 + (load32((v3 + (v1 << 2)) + 28) * 1056))
                                                v18 = ((v8 + (load32((v3 + (v1 << 2)) + 28) * 1056)) + 1150)
                                                if load8u(((v8 + (load32((v3 + (v1 << 2)) + 28) * 1056)) + 1150)):
                                                    break
                                                v4 = (v8 + (v7 << 2))
                                                if (load32(((v8 + (v7 << 2)) + 282828)) != (0 - load32((v4 + 281808)))):
                                                    break
                                                v4 = 1
                                                while True:  # $label326
                                                    v21 = ((v7 * 404) + ENTITY_TYPES)
                                                    v26 = load32(((v7 * 404) + ENTITY_TYPES) + 264)
                                                    if (load32(((v7 * 404) + ENTITY_TYPES) + 264) == 3):
                                                        break
                                                    if (load32(v21 + 196) != load32(v9)):
                                                        break
                                                    if (u32(v26) > u32(1)):
                                                        break
                                                    v26 = load32(v5)
                                                    if (u32(load32(v5)) < u32(100)):
                                                        break
                                                    # TODO: i32.div_u
                                                    v4 = 100
                                                    break
                                                if load8u(v21 + 354):
                                                    break
                                                store32(v10 + 108, v4)
                                                v69 = i32(v4)
                                                storef32(v10 + 100, (v71 / i32(v4)))
                                                store8(v18, 1)
                                                storef32(v10 + 96, ((v71 * v69) / v69))
                                                v4 = load32(9140296)
                                                store32(9140296, (load32(9140296) + 1))
                                                store32(((v4 << 2) + 8451904), v7)
                                                v6 = load32(v3 + 68)
                                                break
                                            v1 = (v1 + 1)
                                            if (u32((v1 + 1)) < u32(v6)):
                                                continue
                                            break
                                    v1 = load32(v20 + 108)
                                    v71 = i32((load32(v20 + 108) * load32(v2 + 80)))
                                    v68 = (v68 + i32((load32(v20 + 108) * load32(v2 + 80))))
                                    v69 = i32((v1 * load32(v2 + 76)))
                                    v66 = (v66 + i32((v1 * load32(v2 + 76))))
                                    v74 = i32((v1 * load32(v2 + 72)))
                                    v67 = (v67 + i32((v1 * load32(v2 + 72))))
                                    v79 = i32((v1 * load32(v2 + 68)))
                                    v70 = (v70 + i32((v1 * load32(v2 + 68))))
                                    v71 = loadf32(v20 + 96)
                                    v73 = ((v71 * loadf32(v20 + 96)) + v73)
                                    v75 = ((v69 * v71) + v75)
                                    v76 = ((v74 * v71) + v76)
                                    v80 = ((v79 * v71) + v80)
                                    v15 = (v15 + 1)
                                    if (u32((v15 + 1)) < u32(load32(9140296))):
                                        continue
                                    break
                            v43 = (v8 + 283872)
                            v3 = 0
                            while True:  # $label332
                                v74 = i32(v17)
                                v68 = (v68 - i32(v17))
                                v79 = (0.0 if (v68 < 0.0) else (v68 - i32(v17)))
                                v90 = loadf32(v19 + 60)
                                while True:  # $label331
                                    v81 = i32(v11)
                                    v66 = (v66 - i32(v11))
                                    v82 = (0.0 if (v66 < 0.0) else (v66 - i32(v11)))
                                    v91 = loadf32(v19 + 56)
                                    while True:  # $label330
                                        v71 = i32(v14)
                                        v66 = (v67 - i32(v14))
                                        v83 = (0.0 if (v66 < 0.0) else (v67 - i32(v14)))
                                        v92 = loadf32(v19 + 52)
                                        while True:  # $label329
                                            v84 = i32(v12)
                                            v66 = (v70 - i32(v12))
                                            v85 = (0.0 if (v66 < 0.0) else (v70 - i32(v12)))
                                            v93 = loadf32(v19 + 48)
                                            v1 = (v8 + (v13 * 1056))
                                            v66 = (((0.0 if (v66 < 0.0) else (v70 - i32(v12))) / (loadf32(v19 + 48) / loadf32(9682176))) + i32(load32((v8 + (v13 * 1056)) + 104)))
                                            if (((((0.0 if (v66 < 0.0) else (v70 - i32(v12))) / (loadf32(v19 + 48) / loadf32(9682176))) + i32(load32((v8 + (v13 * 1056)) + 104))) < 4294967300.0) & (v66 >= 0.0)):
                                                break
                                            break
                                        v66 = (i32(v66) + i32(0))
                                        if (((i32(v66) + i32(0)) < 4294967300.0) & (v66 >= 0.0)):
                                            break
                                        break
                                    v66 = (i32(v66) + i32(0))
                                    if (((i32(v66) + i32(0)) < 4294967300.0) & (v66 >= 0.0)):
                                        break
                                    break
                                v66 = (i32(v66) + i32(0))
                                if (((i32(v66) + i32(0)) < 4294967300.0) & (v66 >= 0.0)):
                                    store32(v1 + 104, i32(v66))
                                    break
                                store32(v1 + 104, 0)
                                break
                            v1 = 0
                            while True:  # $label333
                                v2 = (v8 + (v1 << 2))
                                v2 = ((load32(((v1 * 404) + ENTITY_TYPES) + 280) * (load32(((v8 + (v1 << 2)) + 281808)) + load32((v2 + 282828)))) + v3)
                                v5 = (v1 | 1)
                                if ((v1 | 1) != 255):
                                    v5 = (v8 + (v5 << 2))
                                    v3 = (v2 + (load32(((v5 * 404) + ENTITY_TYPES) + 280) * (load32(((v8 + (v5 << 2)) + 281808)) + load32((v5 + 282828)))))
                                    v1 = (v1 + 2)
                                    continue
                                break
                            v1 = 0
                            v3 = load32(load32(GAME_STATE) + 36)
                            while True:  # $label334
                                v5 = load32(((v1 * 404) + ENTITY_TYPES) + 176)
                                if load32(((v1 * 404) + ENTITY_TYPES) + 176):
                                    v4 = (v8 + (v1 << 2))
                                    v3 = (v3 + (v5 * (load32(((v8 + (v1 << 2)) + 281808)) + load32((v4 + 282828)))))
                                v5 = (v1 | 1)
                                if ((v1 | 1) != 255):
                                    v4 = load32(((v5 * 404) + ENTITY_TYPES) + 176)
                                    if load32(((v5 * 404) + ENTITY_TYPES) + 176):
                                        v5 = (v8 + (v5 << 2))
                                        v3 = ((v4 * (load32(((v8 + (v5 << 2)) + 281808)) + load32((v5 + 282828)))) + v3)
                                    v1 = (v1 + 2)
                                    continue
                                break
                            while True:  # $label335
                                if (u32((v2 + 10)) <= u32(v3)):
                                    break
                                v2 = load32(((v8 + (v13 << 2)) + 284636))
                                if not load32(((v8 + (v13 << 2)) + 284636)):
                                    break
                                while True:  # $label338
                                    v4 = load32(v2 + 8)
                                    if load32(v2 + 8):
                                        v3 = 0
                                        v6 = load32(9215884)
                                        v7 = load32(ENTITIES)
                                        v10 = load32(v2)
                                        v1 = 0
                                        while True:  # $label337
                                            while True:  # $label336
                                                v5 = load32((v10 + (v1 << 2)))
                                                if not load32((v10 + (v1 << 2))):
                                                    break
                                                v5 = (v7 + (v5 * 132))
                                                v15 = load32((v7 + (v5 * 132)) + 44)
                                                if not ((load32((v6 + (load32((v7 + (v5 * 132)) + 44) << 4)) + 4) == 22) | not v15):
                                                    break
                                                if load8u(v5 + 125):
                                                    break
                                                if load32(v5 + 36):
                                                    break
                                                v3 = (v3 if (load8u(v5 + 129) == 10) else load32(v5 + 28))
                                                break
                                            v1 = (v1 + 1)
                                            if ((v1 + 1) != v4):
                                                continue
                                            break
                                        if v3:
                                            break
                                        if not v2:
                                            break
                                    v4 = load32(v2 + 8)
                                    if not load32(v2 + 8):
                                        break
                                    v6 = load32(v8 + 283876)
                                    v7 = load32(v43)
                                    v3 = 0
                                    v10 = load32(ENTITIES)
                                    v15 = load32(v2)
                                    v2 = 2147483647
                                    v1 = 0
                                    while True:  # $label339
                                        v5 = load32((v15 + (v1 << 2)))
                                        if load32((v15 + (v1 << 2))):
                                            v5 = (v10 + (v5 * 132))
                                            v11 = (v6 - load16u((v10 + (v5 * 132)) + 114))
                                            v11 = (v7 - load16u(v5 + 112))
                                            v11 = (((v6 - load16u((v10 + (v5 * 132)) + 114)) * v11) + ((v7 - load16u(v5 + 112)) * v11))
                                            v11 = (v2 > v11)
                                            v2 = ((((v6 - load16u((v10 + (v5 * 132)) + 114)) * v11) + ((v7 - load16u(v5 + 112)) * v11)) if (v2 > v11) else v2)
                                            v3 = (load32(v5 + 28) if v11 else v3)
                                        v1 = (v1 + 1)
                                        if ((v1 + 1) != v4):
                                            continue
                                        break
                                    if not v3:
                                        break
                                    break
                                break
                            v52 = (v8 + 283876)
                            v7 = load32(v8 + 283876)
                            v2 = 0
                            v10 = load32(9142848)
                            v6 = load32(ENTITIES)
                            v9 = load32(v43)
                            v5 = 2147483647
                            v12 = 0
                            while True:  # $label343
                                while True:  # $label340
                                    v1 = load32(((v8 + (v12 << 2)) + 284636))
                                    if not load32(((v8 + (v12 << 2)) + 284636)):
                                        break
                                    v15 = load32(v1 + 8)
                                    if not load32(v1 + 8):
                                        break
                                    v11 = load32(v1)
                                    v1 = 0
                                    while True:  # $label342
                                        while True:  # $label341
                                            v3 = load32((v11 + (v1 << 2)))
                                            if not load32((v11 + (v1 << 2))):
                                                break
                                            v4 = (v6 + (v3 * 132))
                                            v3 = (v7 - load16u((v6 + (v3 * 132)) + 114))
                                            v3 = (v9 - load16u(v4 + 112))
                                            v3 = (((v7 - load16u((v6 + (v3 * 132)) + 114)) * v3) + ((v9 - load16u(v4 + 112)) * v3))
                                            if ((((v7 - load16u((v6 + (v3 * 132)) + 114)) * v3) + ((v9 - load16u(v4 + 112)) * v3)) >= v5):
                                                break
                                            if (load8u(v4 + 125) != 4):
                                                break
                                            if (u32(((v10 - load32(v4 + 88)) * 25)) < u32(30001)):
                                                break
                                            v2 = load32(v4 + 28)
                                            v5 = v3
                                            break
                                        v1 = (v1 + 1)
                                        if ((v1 + 1) != v15):
                                            continue
                                        break
                                    break
                                v12 = (v12 + 1)
                                if ((v12 + 1) != 132):
                                    continue
                                break
                            while True:  # $label344
                                if not v2:
                                    break
                                v5 = load32(((v8 + (v13 << 2)) + 284636))
                                if not load32(((v8 + (v13 << 2)) + 284636)):
                                    break
                                v3 = load32(v5 + 8)
                                if not load32(v5 + 8):
                                    break
                                v10 = (v6 + (v2 * 132))
                                v9 = load16u((v6 + (v2 * 132)) + 114)
                                v15 = load16u(v10 + 112)
                                v7 = 0
                                v11 = load32(9215884)
                                v12 = load32(v5)
                                v4 = 2147483647
                                v1 = 0
                                while True:  # $label346
                                    while True:  # $label345
                                        v2 = load32((v12 + (v1 << 2)))
                                        if not load32((v12 + (v1 << 2))):
                                            break
                                        v2 = (v6 + (v2 * 132))
                                        v14 = load32((v6 + (v2 * 132)) + 44)
                                        if not ((load32((v11 + (load32((v6 + (v2 * 132)) + 44) << 4)) + 4) == 22) | not v14):
                                            break
                                        if load8u(v2 + 125):
                                            break
                                        if load32(v2 + 36):
                                            break
                                        v14 = (v9 - load16u(v2 + 114))
                                        v14 = (v15 - load16u(v2 + 112))
                                        v14 = (((v9 - load16u(v2 + 114)) * v14) + ((v15 - load16u(v2 + 112)) * v14))
                                        v14 = (v4 > v14)
                                        v4 = ((((v9 - load16u(v2 + 114)) * v14) + ((v15 - load16u(v2 + 112)) * v14)) if (v4 > v14) else v4)
                                        v7 = (load32(v2 + 28) if v14 else v7)
                                        break
                                    v1 = (v1 + 1)
                                    if ((v1 + 1) != v3):
                                        continue
                                    break
                                if not v7:
                                    if not v3:
                                        break
                                    v4 = load32(v5)
                                    v7 = 0
                                    v2 = 2147483647
                                    v1 = 0
                                    while True:  # $label347
                                        v5 = load32((v4 + (v1 << 2)))
                                        if load32((v4 + (v1 << 2))):
                                            v5 = (v6 + (v5 * 132))
                                            v11 = (v9 - load16u((v6 + (v5 * 132)) + 114))
                                            v11 = (v15 - load16u(v5 + 112))
                                            v11 = (((v9 - load16u((v6 + (v5 * 132)) + 114)) * v11) + ((v15 - load16u(v5 + 112)) * v11))
                                            v11 = (v2 > v11)
                                            v2 = ((((v9 - load16u((v6 + (v5 * 132)) + 114)) * v11) + ((v15 - load16u(v5 + 112)) * v11)) if (v2 > v11) else v2)
                                            v7 = (load32(v5 + 28) if v11 else v7)
                                        v1 = (v1 + 1)
                                        if ((v1 + 1) != v3):
                                            continue
                                        break
                                    if not v7:
                                        break
                                v1 = (v6 + (v7 * 132))
                                store8((v6 + (v7 * 132)) + 129, 0)
                                break
                            store64(v19 + 40, 0)
                            store64(v19 + 32, 0)
                            v12 = 0
                            while True:  # $label348
                                v30 = (v8 + (v13 << 2))
                                v49 = ((v8 + (v13 << 2)) + 284636)
                                v1 = load32(((v8 + (v13 << 2)) + 284636))
                                if not load32(((v8 + (v13 << 2)) + 284636)):
                                    break
                                v5 = load32(v1 + 8)
                                if not load32(v1 + 8):
                                    break
                                v3 = load32(ENTITIES)
                                v4 = load32(v1)
                                v1 = 0
                                while True:  # $label350
                                    while True:  # $label349
                                        v2 = load32((v4 + (v1 << 2)))
                                        if not load32((v4 + (v1 << 2))):
                                            break
                                        v2 = load8u((v3 + (v2 * 132)) + 129)
                                        if (u32(((load8u((v3 + (v2 * 132)) + 129) - 1) & 255)) <= u32(3)):
                                            v2 = ((v2 << 2) - 4)
                                            v6 = (((v2 << 2) - 4) + (v19 + 32))
                                            storef32((((v2 << 2) - 4) + (v19 + 32)), (loadf32(v6) + 1.0))
                                            v6 = ((v19 - -64) + v2)
                                            storef32(((v19 - -64) + v2), (loadf32(v6) + (loadf32(((v19 + 48) + v2)) / (loadf32((v2 + 9682176)) + 3.0))))
                                            break
                                        if (v2 != 10):
                                            break
                                        storef32(v19 + 40, (loadf32(v19 + 40) + 1.0))
                                        # TODO: f64.promote_f32
                                        # TODO: f32.demote_f64
                                        storef32(v19 + 72, (loadf32(v19 + 72) + 1.1904761904761905))
                                        v12 = (v12 + 1)
                                        break
                                    v1 = (v1 + 1)
                                    if ((v1 + 1) != v5):
                                        continue
                                    break
                                break
                            v86 = (loadf32(v19 + 76) + 9.99999975e-06)
                            v87 = (loadf32(v19 + 72) + 9.99999975e-06)
                            v88 = (loadf32(v19 + 68) + 9.99999975e-06)
                            v89 = (loadf32(v19 + 64) + 9.99999975e-06)
                            v63 = (v8 + 283908)
                            v44 = (v8 + 283860)
                            v31 = (v8 + 283856)
                            v32 = (v8 + 283852)
                            v33 = (v8 + 283848)
                            v26 = load32(9140296)
                            v94 = neg(v74)
                            v95 = neg(v81)
                            v96 = neg(v71)
                            v97 = neg(v84)
                            while True:  # $label378
                                if (v26 >= 2):
                                    v13 = (v26 - 2)
                                    v1 = 0
                                    while True:  # $label355
                                        while True:  # $label351
                                            v2 = v1
                                            if ((v26 - v1) < 2):
                                                break
                                            v4 = 1
                                            v5 = (v26 + (v2 ^ -1))
                                            v10 = ((v26 + (v2 ^ -1)) & 1)
                                            v1 = load32(8451904)
                                            if (v2 != v13):
                                                v9 = (v5 & -2)
                                                v6 = 0
                                                while True:  # $label354
                                                    while True:  # $label352
                                                        v7 = (v8 + 96)
                                                        v3 = ((v4 << 2) + 8451904)
                                                        v5 = load32(((v4 << 2) + 8451904))
                                                        if not (loadf32(((v8 + 96) + (v1 * 1056))) < loadf32((v7 + (load32(((v4 << 2) + 8451904)) * 1056)))):
                                                            v1 = v5
                                                            break
                                                        store32((v3 - 4), v5)
                                                        store32(v3, v1)
                                                        break
                                                    while True:  # $label353
                                                        v5 = load32(v3 + 4)
                                                        if not (loadf32((v7 + (v1 * 1056))) < loadf32((v7 + (load32(v3 + 4) * 1056)))):
                                                            v1 = v5
                                                            break
                                                        store32(v3, v5)
                                                        store32(v3 + 4, v1)
                                                        break
                                                    v4 = (v4 + 2)
                                                    v6 = (v6 + 2)
                                                    if ((v6 + 2) != v9):
                                                        continue
                                                    break
                                            if not v10:
                                                break
                                            v3 = (v8 + 96)
                                            v5 = ((v4 << 2) + 8451904)
                                            v4 = load32(((v4 << 2) + 8451904))
                                            if not (loadf32(((v8 + 96) + (v1 * 1056))) < loadf32((v3 + (load32(((v4 << 2) + 8451904)) * 1056)))):
                                                break
                                            store32((v5 - 4), v4)
                                            store32(v5, v1)
                                            break
                                        v1 = (v2 + 1)
                                        if (v2 != v13):
                                            continue
                                        break
                                if v26:
                                    v15 = 0
                                    v21 = load32(PLAYERS)
                                    v27 = load32(9143016)
                                    v18 = load32(PLAYER_COUNT)
                                    v34 = load32(9142848)
                                    v25 = load32(9215884)
                                    v22 = load32(ENTITIES)
                                    v45 = load32(38788)
                                    v46 = load32(38864)
                                    v36 = load32(38492)
                                    v39 = load32(38500)
                                    while True:  # $label383
                                        while True:  # $label356
                                            v11 = load32(((v15 << 2) + 8451904))
                                            if (load32(((v15 << 2) + 8451904)) == v39):
                                                break
                                            if (v11 == v36):
                                                break
                                            if (v11 == v46):
                                                break
                                            if (v11 == v45):
                                                break
                                            v3 = 2147483647
                                            v17 = 0
                                            v4 = 0
                                            v5 = ((v11 * 404) + ENTITY_TYPES)
                                            v20 = load32(((v11 * 404) + ENTITY_TYPES) + 180)
                                            v13 = load32(load32(((v11 * 404) + ENTITY_TYPES) + 180) + 112)
                                            if load32(load32(((v11 * 404) + ENTITY_TYPES) + 180) + 112):
                                                while True:  # $label364
                                                    while True:  # $label357
                                                        v1 = load32(((v8 + (load32((v20 + (v4 << 2)) + 72) << 2)) + 284636))
                                                        if not load32(((v8 + (load32((v20 + (v4 << 2)) + 72) << 2)) + 284636)):
                                                            break
                                                        v10 = load32(v1 + 8)
                                                        if not load32(v1 + 8):
                                                            break
                                                        v9 = load32(v1)
                                                        v1 = 0
                                                        while True:  # $label363
                                                            v2 = v3
                                                            while True:  # $label358
                                                                v3 = load32((v9 + (v1 << 2)))
                                                                if not load32((v9 + (v1 << 2))):
                                                                    v3 = v2
                                                                    break
                                                                while True:  # $label362
                                                                    while True:  # $label361
                                                                        v6 = (v22 + (v3 * 132))
                                                                        v7 = load8u((v22 + (v3 * 132)) + 125)
                                                                        if not ((u32(load8u((v22 + (v3 * 132)) + 125)) <= u32(14)) if ((1 << v7) & 17424) else 0):
                                                                            v3 = load32(v6 + 44)
                                                                            while True:  # $label360
                                                                                while True:  # $label359
                                                                                    if v7:
                                                                                        break
                                                                                    if not (not v3 | (load32((v25 + (v3 << 4)) + 4) == 22)):
                                                                                        break
                                                                                    if load32(v6 + 36):
                                                                                        break
                                                                                    if (load8u(v6 + 129) != 10):
                                                                                        break
                                                                                    break
                                                                                v3 = (((v3 - v34) * 25) + 1)
                                                                                if (u32((((v3 - v34) * 25) + 1)) < u32(v2)):
                                                                                    break
                                                                                v3 = v2
                                                                                break
                                                                                break
                                                                            v3 = 0
                                                                            if v2:
                                                                                break
                                                                            break
                                                                        v3 = (2147483647 if (u32(v2) >= u32(2147483647)) else v2)
                                                                        break
                                                                        break
                                                                    if v3:
                                                                        break
                                                                    break
                                                                v17 = load32(v6 + 28)
                                                                v3 = 0
                                                                break
                                                            v1 = (v1 + 1)
                                                            if ((v1 + 1) != v10):
                                                                continue
                                                            break
                                                        break
                                                    v4 = (v4 + 1)
                                                    if ((v4 + 1) != v13):
                                                        continue
                                                    break
                                            v14 = (v8 + (v11 * 1056))
                                            v1 = load32(((v8 + (v11 * 36)) + 269376))
                                            v1 = (load32(((v8 + (v11 * 36)) + 269376)) if v1 else 100)
                                            v35 = ((load32(((v8 + (v11 * 36)) + 269376)) if v1 else 100) * load32(v5 + 80))
                                            v29 = (((load32(((v8 + (v11 * 36)) + 269376)) if v1 else 100) * load32(v5 + 80)) // 100)
                                            v41 = (load32(v5 + 76) * v1)
                                            v24 = ((load32(v5 + 76) * v1) // 100)
                                            v38 = (load32(v5 + 72) * v1)
                                            v28 = ((load32(v5 + 72) * v1) // 100)
                                            v42 = (v1 * load32(v5 + 68))
                                            v23 = ((v1 * load32(v5 + 68)) // 100)
                                            while True:  # $label365
                                                if not v15:
                                                    break
                                                if (v11 == -1):
                                                    break
                                                v98 = neg((v74 - i32(v29)))
                                                v99 = neg((v81 - i32(v24)))
                                                v100 = neg((v71 - i32(v28)))
                                                v101 = neg((v84 - i32(v23)))
                                                v102 = loadf32(v14 + 96)
                                                v4 = 0
                                                while True:  # $label368
                                                    v5 = load32(((v4 << 2) + 8451904))
                                                    v1 = ((load32(((v4 << 2) + 8451904)) * 404) + ENTITY_TYPES)
                                                    v2 = load32(((v8 + (v5 * 36)) + 269376))
                                                    v2 = (load32(((v8 + (v5 * 36)) + 269376)) if v2 else 100)
                                                    v5 = (v8 + (v5 * 1056))
                                                    v66 = i32(load32((v8 + (v5 * 1056)) + 108))
                                                    v66 = ceil((i32(load32((v8 + (v5 * 1056)) + 108)) - ((v102 * v66) / loadf32(v5 + 96))))
                                                    v103 = (i32(((load32(((load32(((v4 << 2) + 8451904)) * 404) + ENTITY_TYPES) + 80) * (load32(((v8 + (v5 * 36)) + 269376)) if v2 else 100)) // 100)) * ceil((i32(load32((v8 + (v5 * 1056)) + 108)) - ((v102 * v66) / loadf32(v5 + 96)))))
                                                    v70 = ((i32(((load32(((load32(((v4 << 2) + 8451904)) * 404) + ENTITY_TYPES) + 80) * (load32(((v8 + (v5 * 36)) + 269376)) if v2 else 100)) // 100)) * ceil((i32(load32((v8 + (v5 * 1056)) + 108)) - ((v102 * v66) / loadf32(v5 + 96))))) + v94)
                                                    v72 = (i32(((load32(v1 + 76) * v2) // 100)) * v66)
                                                    v69 = ((i32(((load32(v1 + 76) * v2) // 100)) * v66) + v95)
                                                    v5 = (((i32(((load32(v1 + 76) * v2) // 100)) * v66) + v95) < 0.0)
                                                    v77 = (i32(((load32(v1 + 72) * v2) // 100)) * v66)
                                                    v67 = ((i32(((load32(v1 + 72) * v2) // 100)) * v66) + v96)
                                                    v68 = (0.0 if (v67 < 0.0) else ((i32(((load32(v1 + 72) * v2) // 100)) * v66) + v96))
                                                    v67 = 0.0
                                                    v104 = (i32(((v2 * load32(v1 + 68)) // 100)) * v66)
                                                    v78 = ((i32(((v2 * load32(v1 + 68)) // 100)) * v66) + v97)
                                                    v78 = (0.0 if (v78 < 0.0) else ((i32(((v2 * load32(v1 + 68)) // 100)) * v66) + v97))
                                                    if ((0.0 if (v78 < 0.0) else ((i32(((v2 * load32(v1 + 68)) // 100)) * v66) + v97)) > 0.0):
                                                        v67 = (v78 / v89)
                                                        v67 = ((v78 / v89) if (v67 > 0.0) else 0.0)
                                                    if (v68 > 0.0):
                                                        v68 = (v68 / v88)
                                                        v67 = ((v68 / v88) if (v67 < v68) else v67)
                                                    v68 = (0.0 if v5 else v69)
                                                    if ((0.0 if v5 else v69) > 0.0):
                                                        v68 = (v68 / v87)
                                                        v67 = ((v68 / v87) if (v67 < v68) else v67)
                                                    v70 = (0.0 if (v70 < 0.0) else v70)
                                                    if ((0.0 if (v70 < 0.0) else v70) > 0.0):
                                                        v70 = (v70 / v86)
                                                        v67 = ((v70 / v86) if (v67 < v70) else v67)
                                                    v1 = load32(v1 + 116)
                                                    v69 = i32(load32(v1 + 116))
                                                    v70 = v66
                                                    while True:  # $label366
                                                        if not v1:
                                                            break
                                                        v70 = (v67 / v69)
                                                        if not ((v67 / v69) > v66):
                                                            break
                                                        v70 = v66
                                                        break
                                                    v78 = (v72 + v99)
                                                    v2 = ((v72 + v99) < 0.0)
                                                    v68 = (v77 + v100)
                                                    v72 = (0.0 if (v68 < 0.0) else (v77 + v100))
                                                    v68 = 0.0
                                                    v77 = (v104 + v101)
                                                    v77 = (0.0 if (v77 < 0.0) else (v104 + v101))
                                                    if ((0.0 if (v77 < 0.0) else (v104 + v101)) > 0.0):
                                                        v68 = (v77 / v89)
                                                        v68 = ((v77 / v89) if (v68 > 0.0) else 0.0)
                                                    if (v72 > 0.0):
                                                        v72 = (v72 / v88)
                                                        v68 = ((v72 / v88) if (v68 < v72) else v68)
                                                    v72 = (0.0 if v2 else v78)
                                                    if ((0.0 if v2 else v78) > 0.0):
                                                        v72 = (v72 / v87)
                                                        v68 = ((v72 / v87) if (v68 < v72) else v68)
                                                    v72 = (v103 + v98)
                                                    v72 = (0.0 if (v72 < 0.0) else (v103 + v98))
                                                    if ((0.0 if (v72 < 0.0) else (v103 + v98)) > 0.0):
                                                        v72 = (v72 / v86)
                                                        v68 = ((v72 / v86) if (v68 < v72) else v68)
                                                    v70 = ((((v66 - v70) + 1.0) * v69) + v67)
                                                    v67 = v66
                                                    while True:  # $label367
                                                        if not v1:
                                                            break
                                                        v67 = (v68 / v69)
                                                        if not ((v68 / v69) > v66):
                                                            break
                                                        v67 = v66
                                                        break
                                                    if (v70 < 0.0):
                                                        break
                                                    if (abs((v70 - ((((v66 - v67) + 1.0) * v69) + v68))) > 1.0):
                                                        break
                                                    v4 = (v4 + 1)
                                                    if ((v4 + 1) != v15):
                                                        continue
                                                    break
                                                break
                                            if not v17:
                                                break
                                            v9 = load32(v44)
                                            v10 = load32(v31)
                                            v13 = load32(v32)
                                            v5 = load32(v33)
                                            if (u32(v18) >= u32(2)):
                                                v37 = load32(v63)
                                                v1 = 1
                                                v2 = v9
                                                v3 = v10
                                                v4 = v13
                                                v6 = v5
                                                while True:  # $label373
                                                    while True:  # $label369
                                                        v7 = load8u((v27 + ((v1 * v18) + v37)))
                                                        if not (load8u((v27 + ((v1 * v18) + v37))) & 1):
                                                            break
                                                        if (v6 == 2147483647):
                                                            break
                                                        v5 = load32((v21 + (v1 * 286704)) + 283848)
                                                        v5 = (2147483647 if (v5 == 2147483647) else (load32((v21 + (v1 * 286704)) + 283848) + v6))
                                                        break
                                                    v6 = (2147483647 if (v5 == 2147483647) else (load32((v21 + (v1 * 286704)) + 283848) + v6))
                                                    while True:  # $label370
                                                        if not (v7 & 2):
                                                            break
                                                        if (v4 == 2147483647):
                                                            break
                                                        v13 = load32(((v21 + (v1 * 286704)) + 283852))
                                                        v13 = (2147483647 if (v13 == 2147483647) else (v4 + load32(((v21 + (v1 * 286704)) + 283852))))
                                                        break
                                                    v4 = (2147483647 if (v13 == 2147483647) else (v4 + load32(((v21 + (v1 * 286704)) + 283852))))
                                                    while True:  # $label371
                                                        if not (v7 & 4):
                                                            break
                                                        if (v3 == 2147483647):
                                                            break
                                                        v10 = load32(((v21 + (v1 * 286704)) + 283856))
                                                        v10 = (2147483647 if (v10 == 2147483647) else (v3 + load32(((v21 + (v1 * 286704)) + 283856))))
                                                        break
                                                    v3 = (2147483647 if (v10 == 2147483647) else (v3 + load32(((v21 + (v1 * 286704)) + 283856))))
                                                    while True:  # $label372
                                                        if not (v7 & 8):
                                                            break
                                                        if (v2 == 2147483647):
                                                            break
                                                        v7 = load32(((v21 + (v1 * 286704)) + 283860))
                                                        v9 = (2147483647 if (v7 == 2147483647) else (v2 + load32(((v21 + (v1 * 286704)) + 283860))))
                                                        break
                                                    v2 = (2147483647 if (v7 == 2147483647) else (v2 + load32(((v21 + (v1 * 286704)) + 283860))))
                                                    v1 = (v1 + 1)
                                                    if ((v1 + 1) != v18):
                                                        continue
                                                    break
                                            if ((v5 < v23) & (u32((v42 - 100)) <= u32(-200))):
                                                break
                                            if ((v13 < v28) & (u32((v38 - 100)) <= u32(-200))):
                                                break
                                            if ((v10 < v24) & (u32((v41 - 100)) <= u32(-200))):
                                                break
                                            if ((v9 < v29) & (u32((v35 - 100)) <= u32(-200))):
                                                break
                                            while True:  # $label374
                                                if not load8u(v20 + 23):
                                                    break
                                                v1 = load32(v20 + 4)
                                                if (load32(((load32(v20 + 4) * 404) + ENTITY_TYPES) + 264) != 3):
                                                    break
                                                if load32(((v8 + (v1 << 2)) + 281808)):
                                                    break
                                                break
                                            v4 = load32(v20 + 68)
                                            if load32(v20 + 68):
                                                v1 = 0
                                                v7 = 1
                                                v3 = 0
                                                v6 = 0
                                                while True:  # $label377
                                                    v13 = load32((v20 + (v1 << 2)) + 28)
                                                    v2 = load32(((load32((v20 + (v1 << 2)) + 28) * 404) + ENTITY_TYPES) + 264)
                                                    v5 = (load32(((load32((v20 + (v1 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) == 1)
                                                    while True:  # $label376
                                                        while True:  # $label375
                                                            v13 = load32(((v8 + (v13 << 2)) + 281808))
                                                            if (load32(((v8 + (v13 << 2)) + 281808)) == 1):
                                                                break
                                                            v7 = ((v2 != 3) & v7)
                                                            if v13:
                                                                break
                                                            v7 = ((v2 != 0) & v7)
                                                            break
                                                            break
                                                        v6 = (v5 | v6)
                                                        break
                                                    v3 = (v3 | v5)
                                                    v1 = (v1 + 1)
                                                    if ((v1 + 1) != v4):
                                                        continue
                                                    break
                                                if not (((v6 & v7) if (v3 & 1) else v7) & 1):
                                                    break
                                            if not func461(v11, v17, v8):
                                                v2 = load32(9140296)
                                                v26 = (load32(9140296) - 1)
                                                store32(9140296, (load32(9140296) - 1))
                                                if (u32(v15) >= u32(v26)):
                                                    continue
                                                v5 = ((v2 - v15) - 2)
                                                v1 = 0
                                                v2 = ((v2 + (v15 ^ -1)) & 3)
                                                if ((v2 + (v15 ^ -1)) & 3):
                                                    while True:  # $label379
                                                        v15 = (v15 + 1)
                                                        store32(((v15 << 2) + 8451904), load32((((v15 + 1) << 2) + 8451904)))
                                                        v1 = (v1 + 1)
                                                        if ((v1 + 1) != v2):
                                                            continue
                                                        break
                                                if (u32(v5) < u32(3)):
                                                    continue
                                                while True:  # $label380
                                                    v1 = ((v15 << 2) + 8451904)
                                                    v107 = load64(((v15 << 2) + 8451904) + 4)
                                                    store32(v1 + 8, load32(v1 + 12))
                                                    store64(v1, v107)
                                                    v15 = (v15 + 4)
                                                    store32(v1 + 12, load32((((v15 + 4) << 2) + 8451904)))
                                                    if (v15 != v26):
                                                        continue
                                                    break
                                                continue
                                            v1 = (load32(v14 + 108) - 1)
                                            store32(v14 + 108, (load32(v14 + 108) - 1))
                                            storef32(v14 + 96, (loadf32(v14 + 96) - loadf32(v14 + 100)))
                                            v2 = load32(9140296)
                                            v26 = load32(9140296)
                                            if v1:
                                                continue
                                            v26 = (v2 - 1)
                                            store32(9140296, (v2 - 1))
                                            if (u32(v15) >= u32(v26)):
                                                continue
                                            v5 = ((v2 - v15) - 2)
                                            v1 = 0
                                            v2 = ((v2 + (v15 ^ -1)) & 3)
                                            if ((v2 + (v15 ^ -1)) & 3):
                                                while True:  # $label381
                                                    v15 = (v15 + 1)
                                                    store32(((v15 << 2) + 8451904), load32((((v15 + 1) << 2) + 8451904)))
                                                    v1 = (v1 + 1)
                                                    if ((v1 + 1) != v2):
                                                        continue
                                                    break
                                            if (u32(v5) < u32(3)):
                                                continue
                                            while True:  # $label382
                                                v1 = ((v15 << 2) + 8451904)
                                                v107 = load64(((v15 << 2) + 8451904) + 4)
                                                store32(v1 + 8, load32(v1 + 12))
                                                store64(v1, v107)
                                                v15 = (v15 + 4)
                                                store32(v1 + 12, load32((((v15 + 4) << 2) + 8451904)))
                                                if (v15 != v26):
                                                    continue
                                                break
                                            continue
                                            break
                                        v15 = (v15 + 1)
                                        if ((v15 + 1) != v26):
                                            continue
                                        break
                                break
                            while True:  # $label384
                                if not v16:
                                    break
                                v1 = (v8 + (load32(38528) << 2))
                                v2 = load32(((v8 + (load32(38528) << 2)) + 284636))
                                if not load32(((v8 + (load32(38528) << 2)) + 284636)):
                                    break
                                v4 = load32(v2 + 8)
                                if not load32(v2 + 8):
                                    break
                                v5 = (500 if (u32(load32((v1 + 281808))) > u32(24)) else 452)
                                v1 = 0
                                while True:  # $label386
                                    while True:  # $label385
                                        v3 = load32((load32(v2) + (v1 << 2)))
                                        if not load32((load32(v2) + (v1 << 2))):
                                            break
                                        v3 = entities[v3]
                                        if (u32(load32(entities[v3].animation)) < u32(v5)):
                                            break
                                        v4 = load32(v2 + 8)
                                        break
                                    v1 = (v1 + 1)
                                    if (u32((v1 + 1)) < u32(v4)):
                                        continue
                                    break
                                break
                            while True:  # $label388
                                while True:  # $label387
                                    if (v85 != 0.0):
                                        break
                                    if (v83 != 0.0):
                                        break
                                    if (v82 != 0.0):
                                        break
                                    if (v79 == 0.0):
                                        break
                                    break
                                while True:  # $label389
                                    v17 = load32(((v8 + (load32(38528) << 2)) + 281808))
                                    if (u32(load32(((v8 + (load32(38528) << 2)) + 281808))) < u32(8)):
                                        break
                                    if (u32(v17) < u32(40)):
                                        # TODO: i32.div_u
                                        v17 = 108
                                        break
                                    # TODO: i32.div_u
                                    v17 = 120
                                    break
                                while True:  # $label390
                                    v66 = ((v73 * v79) / (v90 / loadf32(9682188)))
                                    v70 = ((v80 * v85) / (v93 / loadf32(9682176)))
                                    v68 = (((v76 * v83) / (v92 / loadf32(9682180))) * 2.5)
                                    v69 = ((v75 * v82) / (v91 / loadf32(9682184)))
                                    v66 = (v66 + (((((v80 * v85) / (v93 / loadf32(9682176))) + 0.0) + (((v76 * v83) / (v92 / loadf32(9682180))) * 2.5)) + ((v75 * v82) / (v91 / loadf32(9682184)))))
                                    v73 = (((v73 * v79) / (v90 / loadf32(9682188))) / (v66 + (((((v80 * v85) / (v93 / loadf32(9682176))) + 0.0) + (((v76 * v83) / (v92 / loadf32(9682180))) * 2.5)) + ((v75 * v82) / (v91 / loadf32(9682184))))))
                                    v67 = i32(load32((v30 + 281808)))
                                    # TODO: f64.promote_f32
                                    v105 = (((((v73 * v79) / (v90 / loadf32(9682188))) / (v66 + (((((v80 * v85) / (v93 / loadf32(9682176))) + 0.0) + (((v76 * v83) / (v92 / loadf32(9682180))) * 2.5)) + ((v75 * v82) / (v91 / loadf32(9682184)))))) * i32(load32((v30 + 281808)))) + 0.5)
                                    if (((((((v73 * v79) / (v90 / loadf32(9682188))) / (v66 + (((((v80 * v85) / (v93 / loadf32(9682176))) + 0.0) + (((v76 * v83) / (v92 / loadf32(9682180))) * 2.5)) + ((v75 * v82) / (v91 / loadf32(9682184)))))) * i32(load32((v30 + 281808)))) + 0.5) < 4294967296.0) & (v105 >= 0.0)):
                                        break
                                    break
                                v3 = 0
                                store32(i32(v105) + 28, 0)
                                while True:  # $label391
                                    v69 = (v69 / v66)
                                    # TODO: f64.promote_f32
                                    v105 = (((v69 / v66) * v67) + 0.5)
                                    if (((((v69 / v66) * v67) + 0.5) < 4294967296.0) & (v105 >= 0.0)):
                                        break
                                    break
                                v1 = 0
                                store32(i32(v105) + 24, 0)
                                while True:  # $label392
                                    v68 = (v68 / v66)
                                    # TODO: f64.promote_f32
                                    v105 = (((v68 / v66) * v67) + 0.5)
                                    if (((((v68 / v66) * v67) + 0.5) < 4294967296.0) & (v105 >= 0.0)):
                                        break
                                    break
                                v2 = 0
                                store32(i32(v105) + 20, 0)
                                while True:  # $label393
                                    v70 = (v70 / v66)
                                    # TODO: f64.promote_f32
                                    v105 = (((v70 / v66) * v67) + 0.5)
                                    if (((((v70 / v66) * v67) + 0.5) < 4294967296.0) & (v105 >= 0.0)):
                                        break
                                    break
                                v5 = 0
                                store32(i32(v105) + 16, 0)
                                while True:  # $label394
                                    v66 = (loadf32(v19 + 40) - i32(v12))
                                    if (((loadf32(v19 + 40) - i32(v12)) < 4294967300.0) & (v66 >= 0.0)):
                                        break
                                    break
                                v4 = 0
                                while True:  # $label395
                                    if v16:
                                        v10 = (v4 + v17)
                                        if (u32(v1) < u32((v4 + v17))):
                                            v10 = v1
                                            break
                                        store32(v19 + 24, v10)
                                        while True:  # $label396
                                            v66 = i32((v1 - v10))
                                            v67 = (1.0 - v69)
                                            # TODO: f64.promote_f32
                                            v105 = ((((v73 * i32((v1 - v10))) / (1.0 - v69)) + 0.5) + i32(v3))
                                            if ((((((v73 * i32((v1 - v10))) / (1.0 - v69)) + 0.5) + i32(v3)) < 4294967296.0) & (v105 >= 0.0)):
                                                break
                                            break
                                        v3 = 0
                                        store32(i32(v105) + 28, 0)
                                        while True:  # $label397
                                            # TODO: f64.promote_f32
                                            v105 = ((((v68 * v66) / v67) + 0.5) + i32(v2))
                                            if ((((((v68 * v66) / v67) + 0.5) + i32(v2)) < 4294967296.0) & (v105 >= 0.0)):
                                                break
                                            break
                                        v2 = 0
                                        store32(i32(v105) + 20, 0)
                                        # TODO: f64.promote_f32
                                        v105 = ((((v70 * v66) / v67) + 0.5) + i32(v5))
                                        if ((((((v70 * v66) / v67) + 0.5) + i32(v5)) < 4294967296.0) & (v105 >= 0.0)):
                                            v5 = i32(v105)
                                            store32(v19 + 16, i32(v105))
                                            break
                                        v5 = 0
                                        store32(v19 + 16, 0)
                                        break
                                    v6 = load32(((load32(38500) * 404) + 9568168))
                                    if load32(((load32(38500) * 404) + 9568168)):
                                        while True:  # $label398
                                            if ((v71 < 4294967300.0) & (v71 >= 0.0)):
                                                break
                                            break
                                        # TODO: i32.div_u
                                    else:
                                    v10 = (200 + v4)
                                    if (u32(v6) < u32((200 + v4))):
                                        v10 = v1
                                        break
                                    store32(v19 + 24, v10)
                                    while True:  # $label399
                                        v66 = (i32((v1 - v10)) + i32(v2))
                                        if (((i32((v1 - v10)) + i32(v2)) < 4294967300.0) & (v66 >= 0.0)):
                                            break
                                        break
                                    v2 = 0
                                    store32(i32(v66) + 20, 0)
                                    break
                                while True:  # $label400
                                    v7 = load32(v49)
                                    if not load32(v49):
                                        break
                                    v6 = load32(v7 + 8)
                                    if not load32(v7 + 8):
                                        break
                                    v73 = i32(v3)
                                    v75 = i32(v2)
                                    v76 = i32(v5)
                                    v71 = i32(v10)
                                    v3 = 0
                                    while True:  # $label437
                                        while True:  # $label401
                                            v1 = load32((load32(v7) + (v3 << 2)))
                                            if not load32((load32(v7) + (v3 << 2))):
                                                break
                                            v5 = 1
                                            v2 = 2
                                            while True:  # $label410
                                                while True:  # $label409
                                                    while True:  # $label407
                                                        while True:  # $label403
                                                            while True:  # $label404
                                                                while True:  # $label406
                                                                    while True:  # $label405
                                                                        while True:  # $label402
                                                                            v1 = entities[v1]
                                                                            v10 = load8u(entities[v1] + 129)
                                                                            # br_table (load8u(entities[v1] + 129) - 1)
                                                                            break
                                                                            break
                                                                        v2 = 0
                                                                        break
                                                                        break
                                                                    v2 = 3
                                                                    break
                                                                    break
                                                                v2 = 55
                                                                break
                                                            if (loadf32(v19 + 36) != 0.0):
                                                                break
                                                            while True:  # $label408
                                                                # br_table v2
                                                                break
                                                                break
                                                            v4 = load32(9142840)
                                                            v13 = (load32(9142440) + 2)
                                                            v9 = ((load32(9142440) + 2) + load16u(v1 + 114))
                                                            v14 = ((((load32(9142440) + 2) + load16u(v1 + 114)) + 1) * v13)
                                                            v5 = load16u(v1 + 112)
                                                            v15 = (load16u(v1 + 112) + 2)
                                                            if not load32((load32(9142840) + ((((((load32(9142440) + 2) + load16u(v1 + 114)) + 1) * v13) + (load16u(v1 + 112) + 2)) << 2))):
                                                                v5 = v2
                                                                break
                                                            v11 = (v9 * v13)
                                                            if not load32((v4 + (((v9 * v13) + v15) << 2))):
                                                                v5 = v2
                                                                break
                                                            v20 = (v5 + 1)
                                                            if not load32((v4 + ((v11 + (v5 + 1)) << 2))):
                                                                v5 = v2
                                                                break
                                                            if not load32((v4 + ((v5 + v11) << 2))):
                                                                v5 = v2
                                                                break
                                                            if not load32((v4 + ((v5 + v14) << 2))):
                                                                v5 = v2
                                                                break
                                                            v13 = ((v9 + 2) * v13)
                                                            if not load32((v4 + ((((v9 + 2) * v13) + v5) << 2))):
                                                                v5 = v2
                                                                break
                                                            if not load32((v4 + ((v13 + v20) << 2))):
                                                                v5 = v2
                                                                break
                                                            v5 = v2
                                                            if load32((v4 + ((v13 + v15) << 2))):
                                                                break
                                                            break
                                                        v2 = (v5 << 2)
                                                        if (loadf32(((v5 << 2) + (v19 + 32))) > i32(load32(((v19 + 16) + v2)))):
                                                            break
                                                        v2 = v5
                                                        break
                                                    if (v10 == 10):
                                                        break
                                                    v5 = load32(v1 + 44)
                                                    if not ((load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 22) | not v5):
                                                        break
                                                    if load8u(v1 + 125):
                                                        break
                                                    if not load32(v1 + 36):
                                                        break
                                                    break
                                                    break
                                                if (v10 != 10):
                                                    v2 = v5
                                                    break
                                                v2 = load32(v1 + 44)
                                                if not ((load32((load32(9215884) + (load32(v1 + 44) << 4)) + 4) == 22) | not v2):
                                                    break
                                                if load8u(v1 + 125):
                                                    break
                                                v2 = v5
                                                if load32(v1 + 36):
                                                    break
                                                break
                                            store32(v19 + 12, 0)
                                            v66 = loadf32(v19 + 40)
                                            if ((loadf32(v19 + 40) >= v71) & v16):
                                                store8(v19 + 14, 1)
                                            v66 = ((v66 + 1.0) / v71)
                                            v67 = ((loadf32(v19 + 32) + 1.0) / v76)
                                            v5 = (v67 < 99999.0)
                                            v68 = (((loadf32(v19 + 32) + 1.0) / v76) if (v67 < 99999.0) else 99999.0)
                                            v4 = not v2
                                            v15 = (not v2 | (load8u(v19 + 12) != 0))
                                            v70 = (99999.0 if (not v2 | (load8u(v19 + 12) != 0)) else (((loadf32(v19 + 32) + 1.0) / v76) if (v67 < 99999.0) else 99999.0))
                                            v67 = ((loadf32(v19 + 36) + 1.0) / v75)
                                            v11 = (v67 < v70)
                                            v13 = (v2 == 1)
                                            v14 = ((v2 == 1) | (load8u(v19 + 13) != 0))
                                            v69 = ((99999.0 if (not v2 | (load8u(v19 + 12) != 0)) else (((loadf32(v19 + 32) + 1.0) / v76) if (v67 < 99999.0) else 99999.0)) if ((v2 == 1) | (load8u(v19 + 13) != 0)) else (((loadf32(v19 + 36) + 1.0) / v75) if (v67 < v70) else v70))
                                            v6 = (((v66 + 1.0) / v71) < ((99999.0 if (not v2 | (load8u(v19 + 12) != 0)) else (((loadf32(v19 + 32) + 1.0) / v76) if (v67 < 99999.0) else 99999.0)) if ((v2 == 1) | (load8u(v19 + 13) != 0)) else (((loadf32(v19 + 36) + 1.0) / v75) if (v67 < v70) else v70)))
                                            v9 = (v2 == 2)
                                            v10 = ((v2 == 2) | (load8u(v19 + 14) != 0))
                                            v5 = (0 if v5 else 5)
                                            v70 = ((loadf32(v19 + 44) + 1.0) / v73)
                                            v20 = load32(v1 + 28)
                                            v21 = load8u(v1 + 129)
                                            while True:  # $label416
                                                while True:  # $label417
                                                    while True:  # $label418
                                                        while True:  # $label414
                                                            while True:  # $label412
                                                                while True:  # $label411
                                                                    if load8u(v19 + 15):
                                                                        break
                                                                    if (v2 == 3):
                                                                        break
                                                                    if (v70 < (v69 if v10 else (v66 if v6 else v69))):
                                                                        break
                                                                    break
                                                                while True:  # $label413
                                                                    while True:  # $label415
                                                                        v15 = (5 if v15 else v5)
                                                                        v15 = ((5 if v15 else v5) if v14 else (1 if v11 else v15))
                                                                        # br_table (((5 if v15 else v5) if v14 else (1 if v11 else v15)) if v10 else (2 if v6 else v15))
                                                                        break
                                                                        break
                                                                    v6 = 2
                                                                    v10 = 1
                                                                    if func143(v1, v16):
                                                                        break
                                                                    break
                                                                    break
                                                                v10 = 0
                                                                v6 = 0
                                                                if func87(v1, load32(38504)):
                                                                    break
                                                                break
                                                                break
                                                            v10 = 0
                                                            v6 = 3
                                                            if not func87(v1, load32(38508)):
                                                                break
                                                            break
                                                            break
                                                        v6 = 1
                                                        v10 = 0
                                                        if func142(v1, 0):
                                                            break
                                                        break
                                                    store8(entities[v20] + 129, v21)
                                                    store8(((v19 + 12) | v6), 1)
                                                    v15 = ((load8u(v19 + 12) != 0) | v4)
                                                    v69 = (99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68)
                                                    v11 = (v67 < v69)
                                                    v14 = ((load8u(v19 + 13) != 0) | v13)
                                                    v69 = ((99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68) if ((load8u(v19 + 13) != 0) | v13) else (v67 if (v67 < v69) else v69))
                                                    v6 = (v66 < ((99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68) if ((load8u(v19 + 13) != 0) | v13) else (v67 if (v67 < v69) else v69)))
                                                    v10 = ((load8u(v19 + 14) != 0) | v9)
                                                    v20 = load8u(v1 + 129)
                                                    v21 = load32(v1 + 28)
                                                    while True:  # $label424
                                                        while True:  # $label420
                                                            while True:  # $label419
                                                                if load8u(v19 + 15):
                                                                    break
                                                                if (v2 == 3):
                                                                    break
                                                                if (v70 < (v69 if v10 else (v66 if v6 else v69))):
                                                                    break
                                                                break
                                                            while True:  # $label422
                                                                while True:  # $label423
                                                                    while True:  # $label421
                                                                        v15 = (5 if v15 else v5)
                                                                        v15 = ((5 if v15 else v5) if v14 else (1 if v11 else v15))
                                                                        # br_table (((5 if v15 else v5) if v14 else (1 if v11 else v15)) if v10 else (2 if v6 else v15))
                                                                        break
                                                                        break
                                                                    v10 = 0
                                                                    v6 = 0
                                                                    if func87(v1, load32(38504)):
                                                                        break
                                                                    break
                                                                    break
                                                                v6 = 2
                                                                v10 = 1
                                                                if func143(v1, v16):
                                                                    break
                                                                break
                                                                break
                                                            v6 = 1
                                                            v10 = 0
                                                            if func142(v1, 0):
                                                                break
                                                            break
                                                            break
                                                        v10 = 0
                                                        v6 = 3
                                                        if func87(v1, load32(38508)):
                                                            break
                                                        break
                                                    store8(entities[v21] + 129, v20)
                                                    store8(((v19 + 12) | v6), 1)
                                                    v15 = ((load8u(v19 + 12) != 0) | v4)
                                                    v69 = (99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68)
                                                    v11 = (v67 < v69)
                                                    v14 = ((load8u(v19 + 13) != 0) | v13)
                                                    v69 = ((99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68) if ((load8u(v19 + 13) != 0) | v13) else (v67 if (v67 < v69) else v69))
                                                    v6 = (v66 < ((99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68) if ((load8u(v19 + 13) != 0) | v13) else (v67 if (v67 < v69) else v69)))
                                                    v10 = ((load8u(v19 + 14) != 0) | v9)
                                                    v20 = load8u(v1 + 129)
                                                    v21 = load32(v1 + 28)
                                                    while True:  # $label430
                                                        while True:  # $label426
                                                            while True:  # $label425
                                                                if load8u(v19 + 15):
                                                                    break
                                                                if (v2 == 3):
                                                                    break
                                                                if (v70 < (v69 if v10 else (v66 if v6 else v69))):
                                                                    break
                                                                break
                                                            while True:  # $label428
                                                                while True:  # $label429
                                                                    while True:  # $label427
                                                                        v15 = (5 if v15 else v5)
                                                                        v15 = ((5 if v15 else v5) if v14 else (1 if v11 else v15))
                                                                        # br_table (((5 if v15 else v5) if v14 else (1 if v11 else v15)) if v10 else (2 if v6 else v15))
                                                                        break
                                                                        break
                                                                    v10 = 0
                                                                    v6 = 0
                                                                    if func87(v1, load32(38504)):
                                                                        break
                                                                    break
                                                                    break
                                                                v6 = 2
                                                                v10 = 1
                                                                if func143(v1, v16):
                                                                    break
                                                                break
                                                                break
                                                            v6 = 1
                                                            v10 = 0
                                                            if func142(v1, 0):
                                                                break
                                                            break
                                                            break
                                                        v10 = 0
                                                        v6 = 3
                                                        if func87(v1, load32(38508)):
                                                            break
                                                        break
                                                    store8(entities[v21] + 129, v20)
                                                    store8(((v19 + 12) | v6), 1)
                                                    v10 = ((load8u(v19 + 12) != 0) | v4)
                                                    v68 = (99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68)
                                                    v15 = (v67 < v68)
                                                    v13 = ((load8u(v19 + 13) != 0) | v13)
                                                    v67 = ((99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68) if ((load8u(v19 + 13) != 0) | v13) else (v67 if (v67 < v68) else v68))
                                                    v4 = (v66 < ((99999.0 if ((load8u(v19 + 12) != 0) | v4) else v68) if ((load8u(v19 + 13) != 0) | v13) else (v67 if (v67 < v68) else v68)))
                                                    v6 = ((load8u(v19 + 14) != 0) | v9)
                                                    v9 = load8u(v1 + 129)
                                                    v11 = load32(v1 + 28)
                                                    while True:  # $label436
                                                        while True:  # $label432
                                                            while True:  # $label431
                                                                if load8u(v19 + 15):
                                                                    break
                                                                if (v2 == 3):
                                                                    break
                                                                if (v70 < (v67 if v6 else (v66 if v4 else v67))):
                                                                    break
                                                                break
                                                            while True:  # $label434
                                                                while True:  # $label435
                                                                    while True:  # $label433
                                                                        v5 = (5 if v10 else v5)
                                                                        v5 = ((5 if v10 else v5) if v13 else (1 if v15 else v5))
                                                                        # br_table (((5 if v10 else v5) if v13 else (1 if v15 else v5)) if v6 else (2 if v4 else v5))
                                                                        break
                                                                        break
                                                                    v10 = 0
                                                                    v6 = 0
                                                                    if func87(v1, load32(38504)):
                                                                        break
                                                                    break
                                                                    break
                                                                v6 = 2
                                                                v10 = 1
                                                                if func143(v1, v16):
                                                                    break
                                                                break
                                                                break
                                                            v6 = 1
                                                            v10 = 0
                                                            if func142(v1, 0):
                                                                break
                                                            break
                                                            break
                                                        v10 = 0
                                                        v6 = 3
                                                        if func87(v1, load32(38508)):
                                                            break
                                                        break
                                                    store8(entities[v11] + 129, v9)
                                                    store8(((v19 + 12) | v6), 1)
                                                    break
                                                    break
                                                if (u32(v2) <= u32(3)):
                                                    v1 = ((v19 + 32) + (v2 << 2))
                                                    storef32(((v19 + 32) + (v2 << 2)), (loadf32(v1) + -1.0))
                                                v1 = (v6 << 2)
                                                v2 = ((v6 << 2) | (v19 + 32))
                                                storef32(((v6 << 2) | (v19 + 32)), (loadf32(v2) + 1.0))
                                                v2 = ((v19 - -64) | v1)
                                                storef32(((v19 - -64) | v1), (loadf32(v2) + (loadf32(((v19 + 48) | v1)) / loadf32((v1 + 9682176)))))
                                                v12 = (v12 + (v10 & v16))
                                                break
                                            v6 = load32(v7 + 8)
                                            break
                                        v3 = (v3 + 1)
                                        if (u32((v3 + 1)) < u32(v6)):
                                            continue
                                        break
                                    break
                                if not (v16 & not v12):
                                    break
                                if not v17:
                                    break
                                v1 = load32(v49)
                                if not load32(v49):
                                    break
                                v5 = load32(v1 + 8)
                                if not load32(v1 + 8):
                                    break
                                v4 = 0
                                v6 = load32(ENTITIES)
                                v7 = load32(v1)
                                v3 = 2147483647
                                v1 = 0
                                while True:  # $label438
                                    v2 = load32((v7 + (v1 << 2)))
                                    if load32((v7 + (v1 << 2))):
                                        v2 = (v6 + (v2 * 132))
                                        v13 = (load16u((v6 + (v2 * 132)) + 114) - load32(v52))
                                        v13 = (load16u(v2 + 112) - load32(v43))
                                        v13 = (((load16u((v6 + (v2 * 132)) + 114) - load32(v52)) * v13) + ((load16u(v2 + 112) - load32(v43)) * v13))
                                        v13 = (not load8u(v2 + 125) & (v3 > v13))
                                        v3 = ((((load16u((v6 + (v2 * 132)) + 114) - load32(v52)) * v13) + ((load16u(v2 + 112) - load32(v43)) * v13)) if (not load8u(v2 + 125) & (v3 > v13)) else v3)
                                        v4 = (load32(v2 + 28) if v13 else v4)
                                    v1 = (v1 + 1)
                                    if ((v1 + 1) != v5):
                                        continue
                                    break
                                if not v4:
                                    break
                                break
                            v44 = 0
                            v16 = 0
                            v26 = 0
                            while True:  # $label543
                                while True:  # $label439
                                    v3 = load32(((v26 * 404) + ENTITY_TYPES) + 264)
                                    if (load32(((v26 * 404) + ENTITY_TYPES) + 264) != 1):
                                        break
                                    v2 = load32(((v8 + (v26 << 2)) + 284636))
                                    if not load32(((v8 + (v26 << 2)) + 284636)):
                                        break
                                    v4 = load32(v2 + 8)
                                    if not load32(v2 + 8):
                                        break
                                    v1 = 0
                                    v6 = load32(ENTITIES)
                                    v7 = load32(v2)
                                    while True:  # $label441
                                        while True:  # $label440
                                            v2 = load32((v7 + (v1 << 2)))
                                            if not load32((v7 + (v1 << 2))):
                                                break
                                            v5 = (v6 + (v2 * 132))
                                            v2 = load32((v6 + (v2 * 132)) + 68)
                                            v13 = load32(v5 + 64)
                                            if (u32(load32((v6 + (v2 * 132)) + 68)) <= u32(load32(v5 + 64))):
                                                break
                                            v2 = (v2 - v13)
                                            if (u32((v2 - v13)) <= u32(v16)):
                                                break
                                            v61 = load32(v5 + 28)
                                            v16 = v2
                                            break
                                        v1 = (v1 + 1)
                                        if ((v1 + 1) != v4):
                                            continue
                                        break
                                    break
                                while True:  # $label442
                                    if v3:
                                        break
                                    if (v26 == load32(38460)):
                                        break
                                    if (v26 == load32(38732)):
                                        break
                                    if (v26 == load32(38672)):
                                        break
                                    v45 = load32(((v8 + (v26 << 2)) + 284636))
                                    if not load32(((v8 + (v26 << 2)) + 284636)):
                                        break
                                    v46 = 0
                                    if not load32(v45 + 8):
                                        break
                                    while True:  # $label542
                                        while True:  # $label443
                                            v1 = load32((load32(v45) + (v46 << 2)))
                                            if not load32((load32(v45) + (v46 << 2))):
                                                break
                                            v29 = load32(ENTITIES)
                                            v18 = entities[v1]
                                            v44 = (v44 + not load8u(entities[v1] + 129))
                                            if (load8u(v18 + 127) == 6):
                                                break
                                            while True:  # $label444
                                                if (v26 != load32(38440)):
                                                    break
                                                v2 = load16u(v18 + 110)
                                                v5 = players[load16u(v18 + 110)]
                                                if (u32(load32(v18 + 72)) < u32(load32((players[load16u(v18 + 110)] + 284168)))):
                                                    break
                                                v36 = load16u(v18 + 114)
                                                v39 = load16u(v18 + 112)
                                                while True:  # $label445
                                                    v1 = load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200)
                                                    if (load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200) < 0):
                                                        break
                                                    v20 = (v36 - v1)
                                                    v3 = ((v1 << 1) | 1)
                                                    v42 = ((v36 - v1) + ((v1 << 1) | 1))
                                                    v13 = (v39 - v1)
                                                    v37 = ((v39 - v1) + v3)
                                                    v6 = 0
                                                    v24 = (load32(PLAYER_COUNT) * v2)
                                                    v31 = load32(9142440)
                                                    v30 = (load32(9142440) + 2)
                                                    v47 = ((load32(9142440) + 2) << 1)
                                                    v41 = load32((v5 + 284180))
                                                    v2 = (load32((v5 + 284180)) - 3)
                                                    v9 = (((load32((v5 + 284180)) - 3) + v39) - v1)
                                                    v21 = ((v2 + v36) - v1)
                                                    v32 = load32(38564)
                                                    v33 = load32(38620)
                                                    v27 = load32(38560)
                                                    v28 = load32(9143004)
                                                    v34 = load32(38500)
                                                    v25 = load32(9142840)
                                                    while True:  # $label462
                                                        v11 = (v13 + 1)
                                                        if (u32(v13) < u32(v31)):
                                                            v12 = (v13 - 3)
                                                            v64 = ((v13 - 3) + v41)
                                                            v7 = v21
                                                            v2 = v20
                                                            while True:  # $label461
                                                                v10 = v2
                                                                v2 = (v2 + 1)
                                                                while True:  # $label446
                                                                    if (u32(v10) >= u32(v31)):
                                                                        break
                                                                    if ((v10 | v13) < 0):
                                                                        break
                                                                    v14 = (v10 - 3)
                                                                    v65 = ((v12 >= v64) | ((v10 - 3) >= (v14 + v41)))
                                                                    v5 = 1
                                                                    while True:  # $label460
                                                                        while True:  # $label447
                                                                            v1 = load32((v25 + ((v11 + ((v2 + (v5 * v30)) * v30)) << 2)))
                                                                            if (u32(load32((v25 + ((v11 + ((v2 + (v5 * v30)) * v30)) << 2)))) < u32(3)):
                                                                                break
                                                                            v1 = (v29 + (v1 * 132))
                                                                            v3 = load8u((v29 + (v1 * 132)) + 122)
                                                                            if (v34 == load8u((v29 + (v1 * 132)) + 122)):
                                                                                break
                                                                            v4 = load16u(v1 + 110)
                                                                            while True:  # $label448
                                                                                v15 = load16u(v1 + 120)
                                                                                if load16u(v1 + 120):
                                                                                else:
                                                                                if load8u(((v15 if load8u((v28 + (v4 + v24))) else v4) + (v4 + v24))):
                                                                                    if not load8u(v1 + 128):
                                                                                        break
                                                                                    break
                                                                                if (load8u(v1 + 127) != 6):
                                                                                    break
                                                                                if load8u(v1 + 128):
                                                                                    break
                                                                                break
                                                                            if (load8u(v1 + 125) == 10):
                                                                                break
                                                                            if (load8u(v1 + 126) == 2):
                                                                                break
                                                                            if (load32(v1 + 64) == -1):
                                                                                break
                                                                            v1 = ((v3 * 404) + ENTITY_TYPES)
                                                                            if (load32(((v3 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                break
                                                                            if (load32(v1 + 188) != 55):
                                                                                break
                                                                            if (v3 == v27):
                                                                                break
                                                                            if (v3 == v33):
                                                                                break
                                                                            if (v3 == v32):
                                                                                break
                                                                            if not load32(v1 + 288):
                                                                                break
                                                                            v3 = 0
                                                                            v4 = v12
                                                                            if not v65:
                                                                                while True:  # $label459
                                                                                    v15 = (v4 + 1)
                                                                                    v1 = v14
                                                                                    if (u32(v4) < u32(v31)):
                                                                                        while True:  # $label458
                                                                                            v17 = v1
                                                                                            v1 = (v1 + 1)
                                                                                            while True:  # $label449
                                                                                                if (u32(v17) >= u32(v31)):
                                                                                                    break
                                                                                                if ((v4 | v17) < 0):
                                                                                                    break
                                                                                                while True:  # $label450
                                                                                                    v17 = load32((v25 + ((v15 + (v1 * v30)) << 2)))
                                                                                                    if (u32(load32((v25 + ((v15 + (v1 * v30)) << 2)))) <= u32(2)):
                                                                                                        break
                                                                                                    v23 = (v29 + (v17 * 132))
                                                                                                    v22 = load8u((v29 + (v17 * 132)) + 122)
                                                                                                    v38 = ((load8u((v29 + (v17 * 132)) + 122) * 404) + ENTITY_TYPES)
                                                                                                    if not load32(((load8u((v29 + (v17 * 132)) + 122) * 404) + ENTITY_TYPES) + 288):
                                                                                                        break
                                                                                                    if (load8u(v23 + 125) == 10):
                                                                                                        break
                                                                                                    v17 = -4
                                                                                                    while True:  # $label451
                                                                                                        if (v22 == v34):
                                                                                                            break
                                                                                                        v35 = load16u(v23 + 110)
                                                                                                        while True:  # $label452
                                                                                                            v50 = load16u(v23 + 120)
                                                                                                            if load16u(v23 + 120):
                                                                                                            else:
                                                                                                            if load8u(((v50 if load8u((v28 + (v24 + v35))) else v35) + (v35 + v24))):
                                                                                                                if not load8u(v23 + 128):
                                                                                                                    break
                                                                                                                break
                                                                                                            if (load8u(v23 + 127) != 6):
                                                                                                                break
                                                                                                            if load8u(v23 + 128):
                                                                                                                break
                                                                                                            break
                                                                                                        if (load8u(v23 + 126) == 2):
                                                                                                            break
                                                                                                        if (load32(v23 + 64) == -1):
                                                                                                            break
                                                                                                        if (load32(v38 + 264) == 2):
                                                                                                            break
                                                                                                        if (load32(v38 + 188) != 55):
                                                                                                            break
                                                                                                        if (v22 == v27):
                                                                                                            break
                                                                                                        if (v22 == v33):
                                                                                                            break
                                                                                                        v17 = (1 if (v22 != v32) else -4)
                                                                                                        break
                                                                                                    v3 = (v3 + v17)
                                                                                                    break
                                                                                                while True:  # $label453
                                                                                                    v17 = load32((v25 + ((v15 + ((v1 + v30) * v30)) << 2)))
                                                                                                    if (u32(load32((v25 + ((v15 + ((v1 + v30) * v30)) << 2)))) < u32(3)):
                                                                                                        break
                                                                                                    v23 = (v29 + (v17 * 132))
                                                                                                    v22 = load8u((v29 + (v17 * 132)) + 122)
                                                                                                    v38 = ((load8u((v29 + (v17 * 132)) + 122) * 404) + ENTITY_TYPES)
                                                                                                    if not load32(((load8u((v29 + (v17 * 132)) + 122) * 404) + ENTITY_TYPES) + 288):
                                                                                                        break
                                                                                                    if (load8u(v23 + 125) == 10):
                                                                                                        break
                                                                                                    v17 = -4
                                                                                                    while True:  # $label454
                                                                                                        if (v22 == v34):
                                                                                                            break
                                                                                                        v35 = load16u(v23 + 110)
                                                                                                        while True:  # $label455
                                                                                                            v50 = load16u(v23 + 120)
                                                                                                            if load16u(v23 + 120):
                                                                                                            else:
                                                                                                            if load8u(((v50 if load8u((v28 + (v24 + v35))) else v35) + (v35 + v24))):
                                                                                                                if not load8u(v23 + 128):
                                                                                                                    break
                                                                                                                break
                                                                                                            if (load8u(v23 + 127) != 6):
                                                                                                                break
                                                                                                            if load8u(v23 + 128):
                                                                                                                break
                                                                                                            break
                                                                                                        if (load8u(v23 + 126) == 2):
                                                                                                            break
                                                                                                        if (load32(v23 + 64) == -1):
                                                                                                            break
                                                                                                        if (load32(v38 + 264) == 2):
                                                                                                            break
                                                                                                        if (load32(v38 + 188) != 55):
                                                                                                            break
                                                                                                        if (v22 == v27):
                                                                                                            break
                                                                                                        if (v22 == v33):
                                                                                                            break
                                                                                                        v17 = (1 if (v22 != v32) else -4)
                                                                                                        break
                                                                                                    v3 = (v3 + v17)
                                                                                                    break
                                                                                                v17 = load32((v25 + ((v15 + ((v1 + v47) * v30)) << 2)))
                                                                                                if (u32(load32((v25 + ((v15 + ((v1 + v47) * v30)) << 2)))) < u32(3)):
                                                                                                    break
                                                                                                v23 = (v29 + (v17 * 132))
                                                                                                v22 = load8u((v29 + (v17 * 132)) + 122)
                                                                                                v38 = ((load8u((v29 + (v17 * 132)) + 122) * 404) + ENTITY_TYPES)
                                                                                                if not load32(((load8u((v29 + (v17 * 132)) + 122) * 404) + ENTITY_TYPES) + 288):
                                                                                                    break
                                                                                                if (load8u(v23 + 125) == 10):
                                                                                                    break
                                                                                                v17 = -4
                                                                                                while True:  # $label456
                                                                                                    if (v22 == v34):
                                                                                                        break
                                                                                                    v35 = load16u(v23 + 110)
                                                                                                    while True:  # $label457
                                                                                                        v50 = load16u(v23 + 120)
                                                                                                        if load16u(v23 + 120):
                                                                                                        else:
                                                                                                        if load8u(((v50 if load8u((v28 + (v24 + v35))) else v35) + (v35 + v24))):
                                                                                                            if not load8u(v23 + 128):
                                                                                                                break
                                                                                                            break
                                                                                                        if (load8u(v23 + 127) != 6):
                                                                                                            break
                                                                                                        if load8u(v23 + 128):
                                                                                                            break
                                                                                                        break
                                                                                                    if (load8u(v23 + 126) == 2):
                                                                                                        break
                                                                                                    if (load32(v23 + 64) == -1):
                                                                                                        break
                                                                                                    if (load32(v38 + 264) == 2):
                                                                                                        break
                                                                                                    if (load32(v38 + 188) != 55):
                                                                                                        break
                                                                                                    if (v22 == v27):
                                                                                                        break
                                                                                                    if (v22 == v33):
                                                                                                        break
                                                                                                    v17 = (1 if (v22 != v32) else -4)
                                                                                                    break
                                                                                                v3 = (v3 + v17)
                                                                                                break
                                                                                            if (v1 != v7):
                                                                                                continue
                                                                                            break
                                                                                    v4 = v15
                                                                                    if (v15 != v9):
                                                                                        continue
                                                                                    break
                                                                            v1 = (v3 > v6)
                                                                            v54 = (v13 if (v3 > v6) else v54)
                                                                            v55 = (v10 if v1 else v55)
                                                                            v6 = (v3 if v1 else v6)
                                                                            break
                                                                        v5 = (v5 + 1)
                                                                        if ((v5 + 1) != 3):
                                                                            continue
                                                                        break
                                                                    break
                                                                v7 = (v7 + 1)
                                                                if (v2 < v42):
                                                                    continue
                                                                break
                                                        v9 = (v9 + 1)
                                                        v13 = v11
                                                        if (v11 < v37):
                                                            continue
                                                        break
                                                    if not v6:
                                                        break
                                                    break
                                                    break
                                                if (load8u(v18 + 123) != 14):
                                                    break
                                                store16(v18 + 118, v36)
                                                store16(v18 + 116, v39)
                                                store32(v18 + 32, 0)
                                                store8(v18 + 123, 0)
                                                break
                                                break
                                            while True:  # $label463
                                                if (v26 != load32(38772)):
                                                    break
                                                v5 = load16u(v18 + 110)
                                                if (u32(load32(v18 + 72)) < u32(load32((players[load16u(v18 + 110)] + 284252)))):
                                                    break
                                                v22 = load16u(v18 + 114)
                                                v36 = load16u(v18 + 112)
                                                while True:  # $label464
                                                    v1 = load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200)
                                                    if (load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200) < 0):
                                                        break
                                                    v9 = (v22 - v1)
                                                    v3 = ((v1 << 1) | 1)
                                                    v39 = ((v22 - v1) + ((v1 << 1) | 1))
                                                    v2 = (v36 - v1)
                                                    v35 = (v3 + (v36 - v1))
                                                    v28 = 0
                                                    v14 = (load32(PLAYER_COUNT) * v5)
                                                    v23 = load32(9142440)
                                                    v21 = (load32(9142440) + 2)
                                                    v41 = ((load32(9142440) + 2) << 1)
                                                    v34 = load32(9147132)
                                                    v30 = load32(38564)
                                                    v31 = load32(38620)
                                                    v32 = load32(38560)
                                                    v20 = load32(9143004)
                                                    v33 = load32(38500)
                                                    v27 = load32(9142840)
                                                    while True:  # $label482
                                                        v10 = (v2 + 1)
                                                        if (u32(v2) < u32(v23)):
                                                            v15 = (v2 - 3)
                                                            v38 = (v2 + 3)
                                                            v3 = v9
                                                            while True:  # $label481
                                                                v7 = v3
                                                                v3 = (v3 + 1)
                                                                while True:  # $label465
                                                                    if (u32(v7) >= u32(v23)):
                                                                        break
                                                                    if ((v2 | v7) < 0):
                                                                        break
                                                                    v42 = (v7 + 4)
                                                                    v11 = (v7 - 3)
                                                                    v17 = 1
                                                                    while True:  # $label480
                                                                        while True:  # $label466
                                                                            v1 = load32((v27 + ((v10 + ((v3 + (v17 * v21)) * v21)) << 2)))
                                                                            if (u32(load32((v27 + ((v10 + ((v3 + (v17 * v21)) * v21)) << 2)))) < u32(3)):
                                                                                break
                                                                            v1 = (v29 + (v1 * 132))
                                                                            v6 = load8u((v29 + (v1 * 132)) + 122)
                                                                            if (v33 == load8u((v29 + (v1 * 132)) + 122)):
                                                                                break
                                                                            v5 = load16u(v1 + 110)
                                                                            while True:  # $label467
                                                                                v4 = load16u(v1 + 120)
                                                                                if load16u(v1 + 120):
                                                                                else:
                                                                                if load8u(((v4 if load8u((v20 + (v5 + v14))) else v5) + (v5 + v14))):
                                                                                    if not load8u(v1 + 128):
                                                                                        break
                                                                                    break
                                                                                if (load8u(v1 + 127) != 6):
                                                                                    break
                                                                                if load8u(v1 + 128):
                                                                                    break
                                                                                break
                                                                            if (load8u(v1 + 125) == 10):
                                                                                break
                                                                            if (load8u(v1 + 126) == 2):
                                                                                break
                                                                            if (load32(v1 + 64) == -1):
                                                                                break
                                                                            v1 = ((v6 * 404) + ENTITY_TYPES)
                                                                            if (load32(((v6 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                break
                                                                            if (load32(v1 + 188) != 55):
                                                                                break
                                                                            if (v6 == v32):
                                                                                break
                                                                            if (v6 == v31):
                                                                                break
                                                                            v5 = 0
                                                                            v4 = v15
                                                                            if (v6 == v30):
                                                                                break
                                                                            while True:  # $label479
                                                                                v13 = (v4 + 1)
                                                                                v1 = v11
                                                                                if (u32(v4) < u32(v23)):
                                                                                    while True:  # $label478
                                                                                        v6 = v1
                                                                                        v1 = (v1 + 1)
                                                                                        while True:  # $label468
                                                                                            if (u32(v6) >= u32(v23)):
                                                                                                break
                                                                                            if ((v4 | v6) < 0):
                                                                                                break
                                                                                            v12 = load32((v27 + ((v13 + (v1 * v21)) << 2)))
                                                                                            if (u32(load32((v27 + ((v13 + (v1 * v21)) << 2)))) > u32(2)):
                                                                                                v6 = -4
                                                                                                while True:  # $label469
                                                                                                    v12 = (v29 + (v12 * 132))
                                                                                                    v24 = load8u((v29 + (v12 * 132)) + 122)
                                                                                                    if (v33 == load8u((v29 + (v12 * 132)) + 122)):
                                                                                                        break
                                                                                                    v25 = load16u(v12 + 110)
                                                                                                    while True:  # $label470
                                                                                                        v37 = load16u(v12 + 120)
                                                                                                        if load16u(v12 + 120):
                                                                                                        else:
                                                                                                        if load8u(((v37 if load8u((v20 + (v14 + v25))) else v25) + (v25 + v14))):
                                                                                                            if not load8u(v12 + 128):
                                                                                                                break
                                                                                                            break
                                                                                                        if (load8u(v12 + 127) != 6):
                                                                                                            break
                                                                                                        if load8u(v12 + 128):
                                                                                                            break
                                                                                                        break
                                                                                                    if (load8u(v12 + 125) == 10):
                                                                                                        break
                                                                                                    if (load8u(v12 + 126) == 2):
                                                                                                        break
                                                                                                    if (load32(v12 + 64) == -1):
                                                                                                        break
                                                                                                    v25 = ((v24 * 404) + ENTITY_TYPES)
                                                                                                    if (load32(((v24 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                        break
                                                                                                    if (load32(v25 + 188) != 55):
                                                                                                        break
                                                                                                    if (v24 == v32):
                                                                                                        break
                                                                                                    if (v24 == v31):
                                                                                                        break
                                                                                                    v6 = (1 if (v24 != v30) else -4)
                                                                                                    break
                                                                                                while True:  # $label471
                                                                                                    if v34:
                                                                                                        break
                                                                                                    v25 = load32(v12 + 64)
                                                                                                    if (load32(((v24 * 404) + ENTITY_TYPES) + 264) != 1):
                                                                                                        break
                                                                                                    # TODO: i32.div_u
                                                                                                    break
                                                                                                v5 = (v25 + (800 * v6))
                                                                                            v12 = load32((v27 + ((v13 + ((v1 + v21) * v21)) << 2)))
                                                                                            if (u32(load32((v27 + ((v13 + ((v1 + v21) * v21)) << 2)))) >= u32(3)):
                                                                                                v6 = -4
                                                                                                while True:  # $label472
                                                                                                    v12 = (v29 + (v12 * 132))
                                                                                                    v24 = load8u((v29 + (v12 * 132)) + 122)
                                                                                                    if (v33 == load8u((v29 + (v12 * 132)) + 122)):
                                                                                                        break
                                                                                                    v25 = load16u(v12 + 110)
                                                                                                    while True:  # $label473
                                                                                                        v37 = load16u(v12 + 120)
                                                                                                        if load16u(v12 + 120):
                                                                                                        else:
                                                                                                        if load8u(((v37 if load8u((v20 + (v14 + v25))) else v25) + (v25 + v14))):
                                                                                                            if not load8u(v12 + 128):
                                                                                                                break
                                                                                                            break
                                                                                                        if (load8u(v12 + 127) != 6):
                                                                                                            break
                                                                                                        if load8u(v12 + 128):
                                                                                                            break
                                                                                                        break
                                                                                                    if (load8u(v12 + 125) == 10):
                                                                                                        break
                                                                                                    if (load8u(v12 + 126) == 2):
                                                                                                        break
                                                                                                    if (load32(v12 + 64) == -1):
                                                                                                        break
                                                                                                    v25 = ((v24 * 404) + ENTITY_TYPES)
                                                                                                    if (load32(((v24 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                        break
                                                                                                    if (load32(v25 + 188) != 55):
                                                                                                        break
                                                                                                    if (v24 == v32):
                                                                                                        break
                                                                                                    if (v24 == v31):
                                                                                                        break
                                                                                                    v6 = (1 if (v24 != v30) else -4)
                                                                                                    break
                                                                                                while True:  # $label474
                                                                                                    if v34:
                                                                                                        break
                                                                                                    v25 = load32(v12 + 64)
                                                                                                    if (load32(((v24 * 404) + ENTITY_TYPES) + 264) != 1):
                                                                                                        break
                                                                                                    # TODO: i32.div_u
                                                                                                    break
                                                                                                v5 = (v25 + (800 * v6))
                                                                                            v12 = load32((v27 + ((v13 + ((v1 + v41) * v21)) << 2)))
                                                                                            if (u32(load32((v27 + ((v13 + ((v1 + v41) * v21)) << 2)))) < u32(3)):
                                                                                                break
                                                                                            v6 = -4
                                                                                            while True:  # $label475
                                                                                                v12 = (v29 + (v12 * 132))
                                                                                                v24 = load8u((v29 + (v12 * 132)) + 122)
                                                                                                if (v33 == load8u((v29 + (v12 * 132)) + 122)):
                                                                                                    break
                                                                                                v25 = load16u(v12 + 110)
                                                                                                while True:  # $label476
                                                                                                    v37 = load16u(v12 + 120)
                                                                                                    if load16u(v12 + 120):
                                                                                                    else:
                                                                                                    if load8u(((v37 if load8u((v20 + (v14 + v25))) else v25) + (v25 + v14))):
                                                                                                        if not load8u(v12 + 128):
                                                                                                            break
                                                                                                        break
                                                                                                    if (load8u(v12 + 127) != 6):
                                                                                                        break
                                                                                                    if load8u(v12 + 128):
                                                                                                        break
                                                                                                    break
                                                                                                if (load8u(v12 + 125) == 10):
                                                                                                    break
                                                                                                if (load8u(v12 + 126) == 2):
                                                                                                    break
                                                                                                if (load32(v12 + 64) == -1):
                                                                                                    break
                                                                                                v25 = ((v24 * 404) + ENTITY_TYPES)
                                                                                                if (load32(((v24 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                    break
                                                                                                if (load32(v25 + 188) != 55):
                                                                                                    break
                                                                                                if (v24 == v32):
                                                                                                    break
                                                                                                if (v24 == v31):
                                                                                                    break
                                                                                                v6 = (1 if (v24 != v30) else -4)
                                                                                                break
                                                                                            while True:  # $label477
                                                                                                if v34:
                                                                                                    break
                                                                                                v25 = load32(v12 + 64)
                                                                                                if (load32(((v24 * 404) + ENTITY_TYPES) + 264) != 1):
                                                                                                    break
                                                                                                # TODO: i32.div_u
                                                                                                break
                                                                                            v5 = (v25 + (800 * v6))
                                                                                            break
                                                                                        if (v1 < v42):
                                                                                            continue
                                                                                        break
                                                                                v1 = (v4 < v38)
                                                                                v4 = v13
                                                                                if v1:
                                                                                    continue
                                                                                break
                                                                            v1 = (v5 > v28)
                                                                            v56 = (v2 if (v5 > v28) else v56)
                                                                            v57 = (v7 if v1 else v57)
                                                                            v28 = (v5 if v1 else v28)
                                                                            break
                                                                        v17 = (v17 + 1)
                                                                        if ((v17 + 1) != 3):
                                                                            continue
                                                                        break
                                                                    break
                                                                if (v3 < v39):
                                                                    continue
                                                                break
                                                        v2 = v10
                                                        if (v10 < v35):
                                                            continue
                                                        break
                                                    if (v28 < 191):
                                                        break
                                                    break
                                                    break
                                                if (load8u(v18 + 123) != 26):
                                                    break
                                                store16(v18 + 118, v22)
                                                store16(v18 + 116, v36)
                                                store32(v18 + 32, 0)
                                                store8(v18 + 123, 0)
                                                break
                                                break
                                            while True:  # $label483
                                                if (v26 != load32(38928)):
                                                    break
                                                v1 = load32(v18 + 72)
                                                v2 = load16u(v18 + 110)
                                                v5 = players[load16u(v18 + 110)]
                                                if (u32(load32(v18 + 72)) >= u32(load32((players[load16u(v18 + 110)] + 284280)))):
                                                    v36 = load16u(v18 + 114)
                                                    v39 = load16u(v18 + 112)
                                                    while True:  # $label484
                                                        v1 = load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200)
                                                        if (load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200) < 0):
                                                            break
                                                        v15 = (v36 - v1)
                                                        v3 = ((v1 << 1) | 1)
                                                        v35 = ((v36 - v1) + ((v1 << 1) | 1))
                                                        v13 = (v39 - v1)
                                                        v41 = ((v39 - v1) + v3)
                                                        v34 = load32((v5 + 284272))
                                                        v24 = 0
                                                        v17 = (load32(PLAYER_COUNT) * v2)
                                                        v28 = load32(9142440)
                                                        v21 = (load32(9142440) + 2)
                                                        v38 = ((load32(9142440) + 2) << 1)
                                                        v25 = load32(9147132)
                                                        v23 = load32(38564)
                                                        v30 = load32(38620)
                                                        v31 = load32(38560)
                                                        v20 = load32(9143004)
                                                        v32 = load32(38500)
                                                        v33 = load32(9142840)
                                                        while True:  # $label499
                                                            v9 = (v13 + 1)
                                                            if (u32(v13) < u32(v28)):
                                                                v11 = (v13 - 2)
                                                                v42 = ((v13 - 2) + v34)
                                                                v6 = v15
                                                                while True:  # $label498
                                                                    v4 = v6
                                                                    v6 = (v6 + 1)
                                                                    while True:  # $label485
                                                                        if (u32(v4) >= u32(v28)):
                                                                            break
                                                                        if ((v4 | v13) < 0):
                                                                            break
                                                                        v12 = (v4 - 2)
                                                                        v37 = ((v4 - 2) + v34)
                                                                        v10 = 1
                                                                        while True:  # $label497
                                                                            while True:  # $label486
                                                                                v1 = load32((v33 + ((v9 + ((v6 + (v10 * v21)) * v21)) << 2)))
                                                                                if (u32(load32((v33 + ((v9 + ((v6 + (v10 * v21)) * v21)) << 2)))) < u32(3)):
                                                                                    break
                                                                                v1 = (v29 + (v1 * 132))
                                                                                v2 = load8u((v29 + (v1 * 132)) + 122)
                                                                                if (v32 == load8u((v29 + (v1 * 132)) + 122)):
                                                                                    break
                                                                                v5 = load16u(v1 + 110)
                                                                                while True:  # $label487
                                                                                    v3 = load16u(v1 + 120)
                                                                                    if load16u(v1 + 120):
                                                                                    else:
                                                                                    if load8u(((v3 if load8u((v20 + (v5 + v17))) else v5) + (v5 + v17))):
                                                                                        if not load8u(v1 + 128):
                                                                                            break
                                                                                        break
                                                                                    if (load8u(v1 + 127) != 6):
                                                                                        break
                                                                                    if load8u(v1 + 128):
                                                                                        break
                                                                                    break
                                                                                v5 = load8u(v1 + 125)
                                                                                if (load8u(v1 + 125) == 10):
                                                                                    break
                                                                                if (load8u(v1 + 126) == 2):
                                                                                    break
                                                                                if (load32(v1 + 64) == -1):
                                                                                    break
                                                                                v1 = ((v2 * 404) + ENTITY_TYPES)
                                                                                if (load32(((v2 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                    break
                                                                                if (load32(v1 + 188) != 55):
                                                                                    break
                                                                                if (v2 == v31):
                                                                                    break
                                                                                if (v2 == v30):
                                                                                    break
                                                                                if (v2 == v23):
                                                                                    break
                                                                                if not load32(v1 + 344):
                                                                                    break
                                                                                if (u32(((v5 - 11) & 255)) > u32(253)):
                                                                                    break
                                                                                v5 = 0
                                                                                v3 = v11
                                                                                if (v34 > 0):
                                                                                    while True:  # $label496
                                                                                        v7 = (v3 + 1)
                                                                                        v1 = v12
                                                                                        if (u32(v3) < u32(v28)):
                                                                                            while True:  # $label495
                                                                                                v2 = v1
                                                                                                v1 = (v1 + 1)
                                                                                                while True:  # $label488
                                                                                                    if (u32(v2) >= u32(v28)):
                                                                                                        break
                                                                                                    if ((v2 | v3) < 0):
                                                                                                        break
                                                                                                    v14 = load32((v33 + ((v7 + (v1 * v21)) << 2)))
                                                                                                    if (u32(load32((v33 + ((v7 + (v1 * v21)) << 2)))) > u32(2)):
                                                                                                        v2 = 0
                                                                                                        while True:  # $label489
                                                                                                            v14 = (v29 + (v14 * 132))
                                                                                                            if (load8u((v29 + (v14 * 132)) + 127) == 6):
                                                                                                                break
                                                                                                            v2 = -4
                                                                                                            v27 = load8u(v14 + 122)
                                                                                                            if (v32 == load8u(v14 + 122)):
                                                                                                                break
                                                                                                            v22 = load16u(v14 + 110)
                                                                                                            v47 = load16u(v14 + 120)
                                                                                                            if load16u(v14 + 120):
                                                                                                            else:
                                                                                                            if not load8u(((v47 if load8u((v20 + (v17 + v22))) else v22) + (v22 + v17))):
                                                                                                                break
                                                                                                            if load8u(v14 + 128):
                                                                                                                break
                                                                                                            if (load8u(v14 + 125) == 10):
                                                                                                                break
                                                                                                            if (load8u(v14 + 126) == 2):
                                                                                                                break
                                                                                                            if (load32(v14 + 64) == -1):
                                                                                                                break
                                                                                                            v22 = ((v27 * 404) + ENTITY_TYPES)
                                                                                                            if (load32(((v27 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                                break
                                                                                                            if (load32(v22 + 188) != 55):
                                                                                                                break
                                                                                                            if (v27 == v31):
                                                                                                                break
                                                                                                            if (v27 == v30):
                                                                                                                break
                                                                                                            v2 = (1 if (v23 != v27) else -4)
                                                                                                            break
                                                                                                        while True:  # $label490
                                                                                                            if v25:
                                                                                                                break
                                                                                                            v27 = load32(v14 + 64)
                                                                                                            if (load32(((load8u(v14 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                                                                                                break
                                                                                                            # TODO: i32.div_u
                                                                                                            break
                                                                                                        v5 = (v27 + (800 * v2))
                                                                                                    v14 = load32((v33 + ((v7 + ((v1 + v21) * v21)) << 2)))
                                                                                                    if (u32(load32((v33 + ((v7 + ((v1 + v21) * v21)) << 2)))) >= u32(3)):
                                                                                                        v2 = 0
                                                                                                        while True:  # $label491
                                                                                                            v14 = (v29 + (v14 * 132))
                                                                                                            if (load8u((v29 + (v14 * 132)) + 127) == 6):
                                                                                                                break
                                                                                                            v2 = -4
                                                                                                            v27 = load8u(v14 + 122)
                                                                                                            if (v32 == load8u(v14 + 122)):
                                                                                                                break
                                                                                                            v22 = load16u(v14 + 110)
                                                                                                            v47 = load16u(v14 + 120)
                                                                                                            if load16u(v14 + 120):
                                                                                                            else:
                                                                                                            if not load8u(((v47 if load8u((v20 + (v17 + v22))) else v22) + (v22 + v17))):
                                                                                                                break
                                                                                                            if load8u(v14 + 128):
                                                                                                                break
                                                                                                            if (load8u(v14 + 125) == 10):
                                                                                                                break
                                                                                                            if (load8u(v14 + 126) == 2):
                                                                                                                break
                                                                                                            if (load32(v14 + 64) == -1):
                                                                                                                break
                                                                                                            v22 = ((v27 * 404) + ENTITY_TYPES)
                                                                                                            if (load32(((v27 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                                break
                                                                                                            if (load32(v22 + 188) != 55):
                                                                                                                break
                                                                                                            if (v27 == v31):
                                                                                                                break
                                                                                                            if (v27 == v30):
                                                                                                                break
                                                                                                            v2 = (1 if (v23 != v27) else -4)
                                                                                                            break
                                                                                                        while True:  # $label492
                                                                                                            if v25:
                                                                                                                break
                                                                                                            v27 = load32(v14 + 64)
                                                                                                            if (load32(((load8u(v14 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                                                                                                break
                                                                                                            # TODO: i32.div_u
                                                                                                            break
                                                                                                        v5 = (v27 + (800 * v2))
                                                                                                    v14 = load32((v33 + ((v7 + ((v1 + v38) * v21)) << 2)))
                                                                                                    if (u32(load32((v33 + ((v7 + ((v1 + v38) * v21)) << 2)))) < u32(3)):
                                                                                                        break
                                                                                                    v2 = 0
                                                                                                    while True:  # $label493
                                                                                                        v14 = (v29 + (v14 * 132))
                                                                                                        if (load8u((v29 + (v14 * 132)) + 127) == 6):
                                                                                                            break
                                                                                                        v2 = -4
                                                                                                        v27 = load8u(v14 + 122)
                                                                                                        if (v32 == load8u(v14 + 122)):
                                                                                                            break
                                                                                                        v22 = load16u(v14 + 110)
                                                                                                        v47 = load16u(v14 + 120)
                                                                                                        if load16u(v14 + 120):
                                                                                                        else:
                                                                                                        if not load8u(((v47 if load8u((v20 + (v17 + v22))) else v22) + (v22 + v17))):
                                                                                                            break
                                                                                                        if load8u(v14 + 128):
                                                                                                            break
                                                                                                        if (load8u(v14 + 125) == 10):
                                                                                                            break
                                                                                                        if (load8u(v14 + 126) == 2):
                                                                                                            break
                                                                                                        if (load32(v14 + 64) == -1):
                                                                                                            break
                                                                                                        v22 = ((v27 * 404) + ENTITY_TYPES)
                                                                                                        if (load32(((v27 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                            break
                                                                                                        if (load32(v22 + 188) != 55):
                                                                                                            break
                                                                                                        if (v27 == v31):
                                                                                                            break
                                                                                                        if (v27 == v30):
                                                                                                            break
                                                                                                        v2 = (1 if (v23 != v27) else -4)
                                                                                                        break
                                                                                                    while True:  # $label494
                                                                                                        if v25:
                                                                                                            break
                                                                                                        v27 = load32(v14 + 64)
                                                                                                        if (load32(((load8u(v14 + 122) * 404) + ENTITY_TYPES) + 264) != 1):
                                                                                                            break
                                                                                                        # TODO: i32.div_u
                                                                                                        break
                                                                                                    v5 = (v27 + (800 * v2))
                                                                                                    break
                                                                                                if (v1 < v37):
                                                                                                    continue
                                                                                                break
                                                                                        v3 = v7
                                                                                        if (v7 < v42):
                                                                                            continue
                                                                                        break
                                                                                v1 = (v5 > v24)
                                                                                v24 = (v5 if (v5 > v24) else v24)
                                                                                v58 = (v4 if v1 else v58)
                                                                                v59 = (v13 if v1 else v59)
                                                                                break
                                                                            v10 = (v10 + 1)
                                                                            if ((v10 + 1) != 3):
                                                                                continue
                                                                            break
                                                                        break
                                                                    if (v6 < v35):
                                                                        continue
                                                                    break
                                                            v13 = v9
                                                            if (v9 < v41):
                                                                continue
                                                            break
                                                        if not v24:
                                                            break
                                                        break
                                                        break
                                                    if (load8u(v18 + 123) != 39):
                                                        break
                                                    store16(v18 + 118, v36)
                                                    store16(v18 + 116, v39)
                                                    store32(v18 + 32, 0)
                                                    store8(v18 + 123, 0)
                                                    break
                                                if (u32(v1) < u32(load32((v5 + 284284)))):
                                                    break
                                                v11 = load16u(v18 + 114)
                                                v12 = load16u(v18 + 112)
                                                while True:  # $label500
                                                    v1 = load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200)
                                                    if (load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200) < 0):
                                                        break
                                                    v3 = (v11 - v1)
                                                    v5 = ((v1 << 1) | 1)
                                                    v33 = ((v11 - v1) + ((v1 << 1) | 1))
                                                    v7 = (v12 - v1)
                                                    v27 = ((v12 - v1) + v5)
                                                    v13 = 0
                                                    v10 = (load32(PLAYER_COUNT) * v2)
                                                    v20 = load32(9142440)
                                                    v14 = (load32(9142440) + 2)
                                                    v34 = ((load32(9142440) + 2) << 1)
                                                    v21 = load32(38456)
                                                    v24 = load32(38764)
                                                    v28 = load32(38564)
                                                    v23 = load32(38620)
                                                    v30 = load32(38560)
                                                    v9 = load32(9143004)
                                                    v31 = load32(38500)
                                                    v32 = load32(9142840)
                                                    v4 = 0
                                                    while True:  # $label505
                                                        v2 = (v7 + 1)
                                                        if (u32(v7) < u32(v20)):
                                                            v1 = (v7 - v12)
                                                            v25 = ((v7 - v12) * v1)
                                                            v1 = v3
                                                            while True:  # $label504
                                                                v5 = v1
                                                                v1 = (v1 + 1)
                                                                while True:  # $label501
                                                                    if (u32(v5) >= u32(v20)):
                                                                        break
                                                                    if ((v5 | v7) < 0):
                                                                        break
                                                                    v5 = (v5 - v11)
                                                                    v15 = (((v5 - v11) * v5) + v25)
                                                                    while True:  # $label502
                                                                        v5 = load32((v32 + ((v2 + ((v1 + v14) * v14)) << 2)))
                                                                        if (u32(load32((v32 + ((v2 + ((v1 + v14) * v14)) << 2)))) <= u32(2)):
                                                                            break
                                                                        v5 = (v29 + (v5 * 132))
                                                                        v6 = load8u((v29 + (v5 * 132)) + 122)
                                                                        if (v31 == load8u((v29 + (v5 * 132)) + 122)):
                                                                            break
                                                                        v17 = load16u(v5 + 110)
                                                                        while True:  # $label503
                                                                            v22 = load16u(v5 + 120)
                                                                            if load16u(v5 + 120):
                                                                            else:
                                                                            if load8u(((v22 if load8u((v9 + (v10 + v17))) else v17) + (v17 + v10))):
                                                                                if not load8u(v5 + 128):
                                                                                    break
                                                                                break
                                                                            if (load8u(v5 + 127) != 6):
                                                                                break
                                                                            if load8u(v5 + 128):
                                                                                break
                                                                            break
                                                                        if (load8u(v5 + 125) == 10):
                                                                            break
                                                                        if (load8u(v5 + 126) == 2):
                                                                            break
                                                                        if (load32(v5 + 64) == -1):
                                                                            break
                                                                        v17 = ((v6 * 404) + ENTITY_TYPES)
                                                                        if (load32(((v6 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                            break
                                                                        if (load32(v17 + 188) != 55):
                                                                            break
                                                                        if (v6 == v30):
                                                                            break
                                                                        if (v6 == v23):
                                                                            break
                                                                        if (v6 == v28):
                                                                            break
                                                                        if not load32(v17 + 340):
                                                                            break
                                                                        if ((v6 != v24) & (v6 != v21)):
                                                                            break
                                                                        v5 = (v13 > v15)
                                                                        v4 = (load32(v5 + 28) if (v13 > v15) else v4)
                                                                        v13 = (v15 if v5 else v13)
                                                                        break
                                                                    v5 = load32((v32 + ((v2 + ((v1 + v34) * v14)) << 2)))
                                                                    if (u32(load32((v32 + ((v2 + ((v1 + v34) * v14)) << 2)))) < u32(3)):
                                                                        break
                                                                    v5 = (v29 + (v5 * 132))
                                                                    v6 = load8u((v29 + (v5 * 132)) + 122)
                                                                    if (v31 == load8u((v29 + (v5 * 132)) + 122)):
                                                                        break
                                                                    v17 = load16u(v5 + 110)
                                                                    v22 = load16u(v5 + 120)
                                                                    if load16u(v5 + 120):
                                                                    else:
                                                                    if not load8u(((v22 if load8u((v9 + (v10 + v17))) else v17) + (v17 + v10))):
                                                                        if (load8u(v5 + 127) != 6):
                                                                            break
                                                                    if load8u(v5 + 128):
                                                                        break
                                                                    if (load8u(v5 + 125) == 10):
                                                                        break
                                                                    if (load8u(v5 + 126) == 2):
                                                                        break
                                                                    if (load32(v5 + 64) == -1):
                                                                        break
                                                                    v17 = ((v6 * 404) + ENTITY_TYPES)
                                                                    if (load32(((v6 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                        break
                                                                    if (load32(v17 + 188) != 55):
                                                                        break
                                                                    if (v6 == v30):
                                                                        break
                                                                    if (v6 == v23):
                                                                        break
                                                                    if (v6 == v28):
                                                                        break
                                                                    if not load32(v17 + 340):
                                                                        break
                                                                    if ((v6 != v24) & (v6 != v21)):
                                                                        break
                                                                    v5 = (v13 > v15)
                                                                    v4 = (load32(v5 + 28) if (v13 > v15) else v4)
                                                                    v13 = (v15 if v5 else v13)
                                                                    break
                                                                if (v1 < v33):
                                                                    continue
                                                                break
                                                        v7 = v2
                                                        if (v2 < v27):
                                                            continue
                                                        break
                                                    if not v13:
                                                        break
                                                    break
                                                    break
                                                if (load8u(v18 + 123) != 40):
                                                    break
                                                store16(v18 + 118, v11)
                                                store16(v18 + 116, v12)
                                                store32(v18 + 32, 0)
                                                store8(v18 + 123, 0)
                                                break
                                                break
                                            if (load32(38456) != v26):
                                                if (v26 != load32(38764)):
                                                    break
                                            while True:  # $label507
                                                while True:  # $label506
                                                    v23 = load32(9215884)
                                                    v1 = load32(v18 + 44)
                                                    v2 = load32((load32(9215884) + (load32(v18 + 44) << 4)) + 4)
                                                    if not ((load32((load32(9215884) + (load32(v18 + 44) << 4)) + 4) == 22) | not v1):
                                                        break
                                                    if load8u(v18 + 125):
                                                        break
                                                    if not load32(v18 + 36):
                                                        break
                                                    break
                                                if (v2 == 69):
                                                    break
                                                if (load8u(v18 + 123) != 69):
                                                    break
                                                break
                                            while True:  # $label508
                                                v5 = load16u(v18 + 110)
                                                v3 = players[load16u(v18 + 110)]
                                                if (u32(load32(v18 + 72)) < u32(load32((players[load16u(v18 + 110)] + 284148)))):
                                                    break
                                                v1 = load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200)
                                                if (load32(((load8u(v18 + 122) * 404) + ENTITY_TYPES) + 200) < 0):
                                                    break
                                                v2 = (load16u(v18 + 114) - v1)
                                                v4 = ((v1 << 1) | 1)
                                                v36 = ((load16u(v18 + 114) - v1) + ((v1 << 1) | 1))
                                                v13 = (load16u(v18 + 112) - v1)
                                                v41 = ((load16u(v18 + 112) - v1) + v4)
                                                v30 = load32((v3 + 284140))
                                                v39 = ((load32((v3 + 284140)) & 0xFFFFFFFF) >> 1)
                                                v17 = 0
                                                v20 = (load32(PLAYER_COUNT) * v5)
                                                v28 = load32(9142440)
                                                v14 = (load32(9142440) + 2)
                                                v35 = ((load32(9142440) + 2) << 1)
                                                v31 = load32(38564)
                                                v32 = load32(38620)
                                                v33 = load32(38560)
                                                v21 = load32(9143004)
                                                v27 = load32(38500)
                                                v24 = load32(9142840)
                                                while True:  # $label526
                                                    v5 = v13
                                                    v13 = (v13 + 1)
                                                    while True:  # $label509
                                                        if (u32(v5) >= u32(v28)):
                                                            break
                                                        if (v30 <= 0):
                                                            v1 = v2
                                                            while True:  # $label511
                                                                v3 = v1
                                                                v1 = (v1 + 1)
                                                                while True:  # $label510
                                                                    if (u32(v3) >= u32(v28)):
                                                                        break
                                                                    if ((v3 | v5) < 0):
                                                                        break
                                                                    v3 = ((v17 if (v17 > 0) else 0) if (u32(load32((v24 + ((v13 + ((v1 + v14) * v14)) << 2)))) > u32(2)) else v17)
                                                                    v17 = ((((v17 if (v17 > 0) else 0) if (u32(load32((v24 + ((v13 + ((v1 + v14) * v14)) << 2)))) > u32(2)) else v17) if (v3 > 0) else 0) if (u32(load32((v24 + ((v13 + ((v1 + v35) * v14)) << 2)))) > u32(2)) else v3)
                                                                    break
                                                                if (v1 < v36):
                                                                    continue
                                                                break
                                                            break
                                                        v9 = (v5 - v39)
                                                        v38 = ((v5 - v39) + v30)
                                                        v6 = v2
                                                        while True:  # $label525
                                                            v3 = v6
                                                            v6 = (v6 + 1)
                                                            while True:  # $label512
                                                                if (u32(v3) >= u32(v28)):
                                                                    break
                                                                if ((v3 | v5) < 0):
                                                                    break
                                                                v15 = (v3 - v39)
                                                                v42 = ((v3 - v39) + v30)
                                                                v34 = 1
                                                                while True:  # $label524
                                                                    v1 = load32((v24 + ((v13 + ((v6 + (v14 * v34)) * v14)) << 2)))
                                                                    if (u32(load32((v24 + ((v13 + ((v6 + (v14 * v34)) * v14)) << 2)))) >= u32(3)):
                                                                        v11 = (v29 + (v1 * 132))
                                                                        v25 = ((v29 + (v1 * 132)) - -64)
                                                                        v12 = 0
                                                                        v7 = v9
                                                                        while True:  # $label523
                                                                            v4 = (v7 + 1)
                                                                            v1 = v15
                                                                            if (u32(v7) < u32(v28)):
                                                                                while True:  # $label522
                                                                                    v10 = v1
                                                                                    v1 = (v1 + 1)
                                                                                    while True:  # $label513
                                                                                        if (u32(v10) >= u32(v28)):
                                                                                            break
                                                                                        if ((v7 | v10) < 0):
                                                                                            break
                                                                                        while True:  # $label514
                                                                                            if (u32(load32((v24 + ((v4 + (v1 * v14)) << 2)))) <= u32(2)):
                                                                                                break
                                                                                            while True:  # $label515
                                                                                                v10 = load8u(v11 + 122)
                                                                                                if (v27 == load8u(v11 + 122)):
                                                                                                    break
                                                                                                v22 = load16u(v11 + 110)
                                                                                                while True:  # $label516
                                                                                                    v37 = load16u(v11 + 120)
                                                                                                    if load16u(v11 + 120):
                                                                                                    else:
                                                                                                    if load8u(((v37 if load8u((v21 + (v20 + v22))) else v22) + (v22 + v20))):
                                                                                                        if not load8u(v11 + 128):
                                                                                                            break
                                                                                                        break
                                                                                                    if (load8u(v11 + 127) != 6):
                                                                                                        break
                                                                                                    if load8u(v11 + 128):
                                                                                                        break
                                                                                                    break
                                                                                                if (load8u(v11 + 125) == 10):
                                                                                                    break
                                                                                                if (load8u(v11 + 126) == 2):
                                                                                                    break
                                                                                                if (load32(v25) == -1):
                                                                                                    break
                                                                                                v22 = ((v10 * 404) + ENTITY_TYPES)
                                                                                                if (load32(((v10 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                    break
                                                                                                if (load32(v22 + 188) != 55):
                                                                                                    break
                                                                                                if (v10 == v33):
                                                                                                    break
                                                                                                if (v10 == v32):
                                                                                                    break
                                                                                                if (v10 != v31):
                                                                                                    break
                                                                                                break
                                                                                            if (load32((v23 + (load32(v11 + 44) << 4)) + 4) != 6):
                                                                                                if (load8u(v11 + 123) != 6):
                                                                                                    break
                                                                                            v12 = (v12 + (load8u(v11 + 126) != 1))
                                                                                            break
                                                                                        while True:  # $label517
                                                                                            if (u32(load32((v24 + ((v4 + ((v1 + v14) * v14)) << 2)))) < u32(3)):
                                                                                                break
                                                                                            while True:  # $label518
                                                                                                v10 = load8u(v11 + 122)
                                                                                                if (v27 == load8u(v11 + 122)):
                                                                                                    break
                                                                                                v22 = load16u(v11 + 110)
                                                                                                while True:  # $label519
                                                                                                    v37 = load16u(v11 + 120)
                                                                                                    if load16u(v11 + 120):
                                                                                                    else:
                                                                                                    if load8u(((v37 if load8u((v21 + (v20 + v22))) else v22) + (v22 + v20))):
                                                                                                        if not load8u(v11 + 128):
                                                                                                            break
                                                                                                        break
                                                                                                    if (load8u(v11 + 127) != 6):
                                                                                                        break
                                                                                                    if load8u(v11 + 128):
                                                                                                        break
                                                                                                    break
                                                                                                if (load8u(v11 + 125) == 10):
                                                                                                    break
                                                                                                if (load8u(v11 + 126) == 2):
                                                                                                    break
                                                                                                if (load32(v25) == -1):
                                                                                                    break
                                                                                                v22 = ((v10 * 404) + ENTITY_TYPES)
                                                                                                if (load32(((v10 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                    break
                                                                                                if (load32(v22 + 188) != 55):
                                                                                                    break
                                                                                                if (v10 == v33):
                                                                                                    break
                                                                                                if (v10 == v32):
                                                                                                    break
                                                                                                if (v10 != v31):
                                                                                                    break
                                                                                                break
                                                                                            if (load32((v23 + (load32(v11 + 44) << 4)) + 4) != 6):
                                                                                                if (load8u(v11 + 123) != 6):
                                                                                                    break
                                                                                            v12 = (v12 + (load8u(v11 + 126) != 1))
                                                                                            break
                                                                                        if (u32(load32((v24 + ((v4 + ((v1 + v35) * v14)) << 2)))) < u32(3)):
                                                                                            break
                                                                                        while True:  # $label520
                                                                                            v10 = load8u(v11 + 122)
                                                                                            if (v27 == load8u(v11 + 122)):
                                                                                                break
                                                                                            v22 = load16u(v11 + 110)
                                                                                            while True:  # $label521
                                                                                                v37 = load16u(v11 + 120)
                                                                                                if load16u(v11 + 120):
                                                                                                else:
                                                                                                if load8u(((v37 if load8u((v21 + (v20 + v22))) else v22) + (v22 + v20))):
                                                                                                    if not load8u(v11 + 128):
                                                                                                        break
                                                                                                    break
                                                                                                if (load8u(v11 + 127) != 6):
                                                                                                    break
                                                                                                if load8u(v11 + 128):
                                                                                                    break
                                                                                                break
                                                                                            if (load8u(v11 + 125) == 10):
                                                                                                break
                                                                                            if (load8u(v11 + 126) == 2):
                                                                                                break
                                                                                            if (load32(v25) == -1):
                                                                                                break
                                                                                            v22 = ((v10 * 404) + ENTITY_TYPES)
                                                                                            if (load32(((v10 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                                                break
                                                                                            if (load32(v22 + 188) != 55):
                                                                                                break
                                                                                            if (v10 == v33):
                                                                                                break
                                                                                            if (v10 == v32):
                                                                                                break
                                                                                            if (v10 != v31):
                                                                                                break
                                                                                            break
                                                                                        if (load32((v23 + (load32(v11 + 44) << 4)) + 4) != 6):
                                                                                            if (load8u(v11 + 123) != 6):
                                                                                                break
                                                                                        v12 = (v12 + (load8u(v11 + 126) != 1))
                                                                                        break
                                                                                    if (v1 < v42):
                                                                                        continue
                                                                                    break
                                                                            v7 = v4
                                                                            if (v4 < v38):
                                                                                continue
                                                                            break
                                                                        v1 = (v12 > v17)
                                                                        v17 = (v12 if (v12 > v17) else v17)
                                                                        v60 = (v5 if v1 else v60)
                                                                        v51 = (v3 if v1 else v51)
                                                                    v34 = (v34 + 1)
                                                                    if ((v34 + 1) != 3):
                                                                        continue
                                                                    break
                                                                break
                                                            if (v6 < v36):
                                                                continue
                                                            break
                                                        break
                                                    if (v13 < v41):
                                                        continue
                                                    break
                                                if not v17:
                                                    break
                                                break
                                            if (load8u(v18 + 123) == 9):
                                                break
                                            v2 = 0
                                            v5 = load32(ENTITIES)
                                            while True:  # $label530
                                                while True:  # $label529
                                                    while True:  # $label527
                                                        v1 = ((v2 * 404) + ENTITY_TYPES)
                                                        if load32(((v2 * 404) + ENTITY_TYPES) + 264):
                                                            break
                                                        if (load32(v1 + 268) == 1):
                                                            break
                                                        if not load32(v1 + 92):
                                                            break
                                                        v1 = load32(((v8 + (v2 << 2)) + 284636))
                                                        if not load32(((v8 + (v2 << 2)) + 284636)):
                                                            break
                                                        v3 = load32(v1 + 8)
                                                        if not load32(v1 + 8):
                                                            break
                                                        v4 = load32(v1)
                                                        v1 = 0
                                                        while True:  # $label528
                                                            v6 = load32((v4 + (v1 << 2)))
                                                            if not load32((v4 + (v1 << 2))):
                                                                v1 = (v1 + 1)
                                                                if (v3 != (v1 + 1)):
                                                                    continue
                                                                break
                                                            break
                                                        v7 = load32((v5 + (v6 * 132)) + 28)
                                                        if (load32((v5 + (v6 * 132)) + 28) == load32(v18 + 28)):
                                                            break
                                                        if v7:
                                                            break
                                                        break
                                                    v2 = (v2 + 1)
                                                    if ((v2 + 1) != 132):
                                                        continue
                                                    break
                                                    break
                                                break
                                            while True:  # $label533
                                                while True:  # $label532
                                                    while True:  # $label531
                                                        v2 = load32(v18 + 20)
                                                        if not load32(v18 + 20):
                                                            v2 = func26(16)
                                                            store32(func26(16) + 4, 7)
                                                            store32(v2, func26(28))
                                                            store64(v2 + 8, 4294967296)
                                                            store32(v18 + 20, v2)
                                                            v5 = (v2 + 8)
                                                            break
                                                        store32(v2 + 8, 0)
                                                        v5 = (v2 + 8)
                                                        if not load32(v2 + 4):
                                                            break
                                                        break
                                                    v6 = load32(v2)
                                                    v3 = 0
                                                    break
                                                    break
                                                v1 = load32(v2 + 12)
                                                store32(v2 + 4, load32(v2 + 12))
                                                v3 = load32(v2)
                                                v6 = func26((-1 if (u32(v1) > u32(1073741823)) else (v1 << 2)))
                                                if v3:
                                                else:
                                                v3 = 0
                                                store32(v2, v6)
                                                v2 = load32(v18 + 20)
                                                break
                                            store32(v5, (v3 + 1))
                                            store32((v6 + (v3 << 2)), 1)
                                            while True:  # $label534
                                                v6 = load32(v2 + 8)
                                                if (load32(v2 + 8) != load32(v2 + 4)):
                                                    v5 = load32(v2)
                                                    break
                                                v5 = (load32(v2 + 12) + v6)
                                                store32(v2 + 4, (load32(v2 + 12) + v6))
                                                v1 = load32(v2)
                                                v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                                                if v6:
                                                    # TODO: memory.copy
                                                if v1:
                                                    v6 = load32(v2 + 8)
                                                store32(v2, v5)
                                                break
                                            v1 = load32(v18 + 20)
                                            store32(v2 + 8, (v6 + 1))
                                            store32((v5 + (v6 << 2)), 2)
                                            while True:  # $label535
                                                v6 = load32(v1 + 8)
                                                if (load32(v1 + 8) != load32(v1 + 4)):
                                                    v5 = load32(v1)
                                                    break
                                                v5 = (load32(v1 + 12) + v6)
                                                store32(v1 + 4, (load32(v1 + 12) + v6))
                                                v2 = load32(v1)
                                                v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                                                if v6:
                                                    # TODO: memory.copy
                                                if v2:
                                                    v6 = load32(v1 + 8)
                                                store32(v1, v5)
                                                break
                                            v2 = load32(v18 + 20)
                                            store32(v1 + 8, (v6 + 1))
                                            store32((v5 + (v6 << 2)), 0)
                                            while True:  # $label536
                                                v6 = load32(v2 + 8)
                                                if (load32(v2 + 8) != load32(v2 + 4)):
                                                    v5 = load32(v2)
                                                    break
                                                v5 = (load32(v2 + 12) + v6)
                                                store32(v2 + 4, (load32(v2 + 12) + v6))
                                                v1 = load32(v2)
                                                v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                                                if v6:
                                                    # TODO: memory.copy
                                                if v1:
                                                    v6 = load32(v2 + 8)
                                                store32(v2, v5)
                                                break
                                            v1 = load32(v18 + 20)
                                            store32(v2 + 8, (v6 + 1))
                                            store32((v5 + (v6 << 2)), 0)
                                            while True:  # $label537
                                                v6 = load32(v1 + 8)
                                                if (load32(v1 + 8) != load32(v1 + 4)):
                                                    v5 = load32(v1)
                                                    break
                                                v5 = (load32(v1 + 12) + v6)
                                                store32(v1 + 4, (load32(v1 + 12) + v6))
                                                v2 = load32(v1)
                                                v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                                                if v6:
                                                    # TODO: memory.copy
                                                if v2:
                                                    v6 = load32(v1 + 8)
                                                store32(v1, v5)
                                                break
                                            v2 = load32(v18 + 20)
                                            store32(v1 + 8, (v6 + 1))
                                            store32((v5 + (v6 << 2)), v7)
                                            while True:  # $label538
                                                v6 = load32(v2 + 8)
                                                if (load32(v2 + 8) != load32(v2 + 4)):
                                                    v5 = load32(v2)
                                                    break
                                                v5 = (load32(v2 + 12) + v6)
                                                store32(v2 + 4, (load32(v2 + 12) + v6))
                                                v1 = load32(v2)
                                                v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                                                if v6:
                                                    # TODO: memory.copy
                                                if v1:
                                                    v6 = load32(v2 + 8)
                                                store32(v2, v5)
                                                break
                                            v1 = load32(v18 + 20)
                                            store32(v2 + 8, (v6 + 1))
                                            store32((v5 + (v6 << 2)), 0)
                                            while True:  # $label539
                                                v6 = load32(v1 + 8)
                                                if (load32(v1 + 8) != load32(v1 + 4)):
                                                    v5 = load32(v1)
                                                    break
                                                v5 = (load32(v1 + 12) + v6)
                                                store32(v1 + 4, (load32(v1 + 12) + v6))
                                                v2 = load32(v1)
                                                v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                                                if v6:
                                                    # TODO: memory.copy
                                                if v2:
                                                    v6 = load32(v1 + 8)
                                                store32(v1, v5)
                                                break
                                            v2 = load32(v18 + 20)
                                            store32(v1 + 8, (v6 + 1))
                                            store32((v5 + (v6 << 2)), 0)
                                            while True:  # $label540
                                                v6 = load32(v2 + 8)
                                                if (load32(v2 + 8) != load32(v2 + 4)):
                                                    v5 = load32(v2)
                                                    break
                                                v5 = (load32(v2 + 12) + v6)
                                                store32(v2 + 4, (load32(v2 + 12) + v6))
                                                v1 = load32(v2)
                                                v5 = func26((-1 if (u32(v5) > u32(1073741823)) else (v5 << 2)))
                                                if v6:
                                                    # TODO: memory.copy
                                                if v1:
                                                    v6 = load32(v2 + 8)
                                                store32(v2, v5)
                                                break
                                            v1 = load32(v18 + 20)
                                            store32(v2 + 8, (v6 + 1))
                                            store32((v5 + (v6 << 2)), 5)
                                            while True:  # $label541
                                                v2 = load32(v1 + 8)
                                                if (load32(v1 + 8) != load32(v1 + 4)):
                                                    v4 = load32(v1)
                                                    break
                                                v3 = (load32(v1 + 12) + v2)
                                                store32(v1 + 4, (load32(v1 + 12) + v2))
                                                v5 = load32(v1)
                                                v4 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                                                if v2:
                                                    # TODO: memory.copy
                                                if v5:
                                                    v2 = load32(v1 + 8)
                                                store32(v1, v4)
                                                break
                                            store32(v1 + 8, (v2 + 1))
                                            store32((v4 + (v2 << 2)), 0)
                                            break
                                        v46 = (v46 + 1)
                                        if (u32((v46 + 1)) < u32(load32(v45 + 8))):
                                            continue
                                        break
                                    break
                                v26 = (v26 + 1)
                                if ((v26 + 1) != 132):
                                    continue
                                break
                            while True:  # $label544
                                if not v16:
                                    break
                                v5 = load32(v49)
                                if not load32(v49):
                                    break
                                v1 = 0
                                v6 = load32(v5 + 8)
                                if not load32(v5 + 8):
                                    break
                                while True:  # $label546
                                    while True:  # $label545
                                        v2 = load32((load32(v5) + (v1 << 2)))
                                        if not load32((load32(v5) + (v1 << 2))):
                                            break
                                        v2 = entities[v2]
                                        v3 = load32(entities[v2].target_x)
                                        if not ((load32((load32(9215884) + (load32(entities[v2].target_x) << 4)) + 4) == 22) | not v3):
                                            break
                                        if load8u(v2 + 125):
                                            break
                                        if load32(v2 + 36):
                                            break
                                        if (load8u(v2 + 129) == 10):
                                            break
                                        store8(v2 + 129, 0)
                                        v6 = load32(v5 + 8)
                                        break
                                    v1 = (v1 + 1)
                                    if (u32((v1 + 1)) < u32(v6)):
                                        continue
                                    break
                                break
                            if not v44:
                                break
                            v33 = load32(v8 + 286688)
                            # TODO: i32.div_u
                            v27 = 100
                            v9 = 0
                            v34 = (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400)))
                            if not (u32(load32(9142848)) < u32((load32(load32(GAME_STATE) + 72) * 2400))):
                                v4 = 0
                                while True:  # $label548
                                    while True:  # $label547
                                        v105 = (sqrt(i32(load32(v8 + 283880))) + 9.0)
                                        if (abs((sqrt(i32(load32(v8 + 283880))) + 9.0)) < 2147483648.0):
                                            break
                                        break
                                    v25 = -2147483648
                                    if (-2147483648 < 2):
                                        break
                                    v24 = load32(v8 + 283872)
                                    v5 = (load32(v8 + 283872) - 1)
                                    v28 = load32(v8 + 283876)
                                    v3 = (load32(v8 + 283876) - 1)
                                    v10 = (v24 + 2)
                                    v13 = (v28 + 2)
                                    v9 = (load32(PLAYER_COUNT) * load32(v8 + 283908))
                                    v23 = load32(9142440)
                                    v15 = (load32(9142440) + 2)
                                    v22 = ((load32(9142440) + 2) << 1)
                                    v14 = load32(38564)
                                    v17 = load32(38620)
                                    v20 = load32(38560)
                                    v16 = load32(9143004)
                                    v21 = load32(38500)
                                    v18 = load32(ENTITIES)
                                    v26 = load32(9142840)
                                    v11 = 1
                                    while True:  # $label561
                                        while True:  # $label549
                                            if (v5 >= v10):
                                                break
                                            if (v3 >= v13):
                                                break
                                            v48 = (v10 - 1)
                                            v49 = (v13 - 1)
                                            v30 = 1
                                            v1 = v5
                                            while True:  # $label560
                                                while True:  # $label559
                                                    v6 = v1
                                                    v1 = (v1 + 1)
                                                    while True:  # $label550
                                                        if (u32(v6) >= u32(v23)):
                                                            break
                                                        v45 = (v6 == v48)
                                                        v46 = (v5 == v6)
                                                        v31 = 1
                                                        v2 = v3
                                                        while True:  # $label558
                                                            while True:  # $label554
                                                                while True:  # $label551
                                                                    if not (v45 | ((v46 | (v2 == v3)) | (v2 == v49))):
                                                                        break
                                                                    if (u32(v2) >= u32(v23)):
                                                                        break
                                                                    if ((v2 | v6) < 0):
                                                                        break
                                                                    while True:  # $label552
                                                                        v32 = (v2 + 1)
                                                                        v4 = load32((v26 + ((v1 + ((v2 + 1) * v15)) << 2)))
                                                                        if (u32(load32((v26 + ((v1 + ((v2 + 1) * v15)) << 2)))) <= u32(2)):
                                                                            break
                                                                        v7 = (v18 + (v4 * 132))
                                                                        v12 = load8u((v18 + (v4 * 132)) + 122)
                                                                        if (v21 == load8u((v18 + (v4 * 132)) + 122)):
                                                                            break
                                                                        v29 = load16u(v7 + 110)
                                                                        while True:  # $label553
                                                                            v36 = load16u(v7 + 120)
                                                                            if load16u(v7 + 120):
                                                                            else:
                                                                            if load8u(((v36 if load8u((v16 + (v9 + v29))) else v29) + (v29 + v9))):
                                                                                if not load8u(v7 + 128):
                                                                                    break
                                                                                break
                                                                            if (load8u(v7 + 127) != 6):
                                                                                break
                                                                            if load8u(v7 + 128):
                                                                                break
                                                                            break
                                                                        if (load8u(v7 + 125) == 10):
                                                                            break
                                                                        if (load8u(v7 + 126) == 2):
                                                                            break
                                                                        if (load32(v7 + 64) == -1):
                                                                            break
                                                                        v7 = ((v12 * 404) + ENTITY_TYPES)
                                                                        if (load32(((v12 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                            break
                                                                        if (load32(v7 + 188) != 55):
                                                                            break
                                                                        if (v12 == v20):
                                                                            break
                                                                        if (v12 == v17):
                                                                            break
                                                                        if (v12 != v14):
                                                                            break
                                                                        break
                                                                    while True:  # $label555
                                                                        v4 = load32((v26 + ((v1 + ((v15 + v32) * v15)) << 2)))
                                                                        if (u32(load32((v26 + ((v1 + ((v15 + v32) * v15)) << 2)))) < u32(3)):
                                                                            break
                                                                        v7 = (v18 + (v4 * 132))
                                                                        v12 = load8u((v18 + (v4 * 132)) + 122)
                                                                        if (v21 == load8u((v18 + (v4 * 132)) + 122)):
                                                                            break
                                                                        v29 = load16u(v7 + 110)
                                                                        while True:  # $label556
                                                                            v36 = load16u(v7 + 120)
                                                                            if load16u(v7 + 120):
                                                                            else:
                                                                            if load8u(((v36 if load8u((v16 + (v9 + v29))) else v29) + (v29 + v9))):
                                                                                if not load8u(v7 + 128):
                                                                                    break
                                                                                break
                                                                            if (load8u(v7 + 127) != 6):
                                                                                break
                                                                            if load8u(v7 + 128):
                                                                                break
                                                                            break
                                                                        if (load8u(v7 + 125) == 10):
                                                                            break
                                                                        if (load8u(v7 + 126) == 2):
                                                                            break
                                                                        if (load32(v7 + 64) == -1):
                                                                            break
                                                                        v7 = ((v12 * 404) + ENTITY_TYPES)
                                                                        if (load32(((v12 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                            break
                                                                        if (load32(v7 + 188) != 55):
                                                                            break
                                                                        if (v12 == v20):
                                                                            break
                                                                        if (v12 == v17):
                                                                            break
                                                                        if (v12 != v14):
                                                                            break
                                                                        break
                                                                    v4 = load32((v26 + ((v1 + ((v22 + v32) * v15)) << 2)))
                                                                    if (u32(load32((v26 + ((v1 + ((v22 + v32) * v15)) << 2)))) < u32(3)):
                                                                        break
                                                                    v7 = (v18 + (v4 * 132))
                                                                    v12 = load8u((v18 + (v4 * 132)) + 122)
                                                                    if (v21 == load8u((v18 + (v4 * 132)) + 122)):
                                                                        break
                                                                    v29 = load16u(v7 + 110)
                                                                    while True:  # $label557
                                                                        v32 = load16u(v7 + 120)
                                                                        if load16u(v7 + 120):
                                                                        else:
                                                                        if load8u(((v32 if load8u((v16 + (v9 + v29))) else v29) + (v29 + v9))):
                                                                            if not load8u(v7 + 128):
                                                                                break
                                                                            break
                                                                        if (load8u(v7 + 127) != 6):
                                                                            break
                                                                        if load8u(v7 + 128):
                                                                            break
                                                                        break
                                                                    if (load8u(v7 + 125) == 10):
                                                                        break
                                                                    if (load8u(v7 + 126) == 2):
                                                                        break
                                                                    if (load32(v7 + 64) == -1):
                                                                        break
                                                                    v7 = ((v12 * 404) + ENTITY_TYPES)
                                                                    if (load32(((v12 * 404) + ENTITY_TYPES) + 264) == 2):
                                                                        break
                                                                    if (load32(v7 + 188) != 55):
                                                                        break
                                                                    if (v12 == v20):
                                                                        break
                                                                    if (v12 == v17):
                                                                        break
                                                                    if (v12 != v14):
                                                                        break
                                                                    break
                                                                v2 = (v2 + 1)
                                                                v31 = ((v2 + 1) < v13)
                                                                if (v2 != v13):
                                                                    continue
                                                                break
                                                                break
                                                            break
                                                        if v31:
                                                            break
                                                        break
                                                    v30 = (v1 < v10)
                                                    if (v1 != v10):
                                                        continue
                                                    break
                                                    break
                                                break
                                            if v30:
                                                break
                                            break
                                        v13 = (v13 + 1)
                                        v10 = (v10 + 1)
                                        v11 = (v11 + 1)
                                        v3 = (v28 - (v11 + 1))
                                        v5 = (v24 - v11)
                                        if (v11 != v25):
                                            continue
                                        break
                                    v4 = 0
                                    break
                                v9 = v4
                            while True:  # $label563
                                while True:  # $label562
                                    if not v33:
                                        break
                                    if (u32(v44) <= u32((v27 + 55))):
                                        break
                                    if v9:
                                        break
                                    if v34:
                                        break
                                    v6 = load32(PLAYER_COUNT)
                                    if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                        break
                                    v13 = (v6 * v40)
                                    v7 = load32(PLAYERS)
                                    v1 = (load32(PLAYERS) + v62)
                                    v9 = ((load32(PLAYERS) + v62) + 283876)
                                    v16 = (v1 + 283872)
                                    v3 = 0
                                    v15 = load32(9143004)
                                    v2 = 1
                                    v10 = 2147483647
                                    while True:  # $label568
                                        while True:  # $label564
                                            if (v2 == v40):
                                                break
                                            v5 = (v7 + (v2 * 286704))
                                            if load8u((v7 + (v2 * 286704)) + 286696):
                                                break
                                            if not load8u((v15 + (v2 + v13))):
                                                break
                                            v1 = (load32(v5 + 283876) - load32(v9))
                                            v1 = (load32(v5 + 283872) - load32(v16))
                                            v11 = (((load32(v5 + 283876) - load32(v9)) * v1) + ((load32(v5 + 283872) - load32(v16)) * v1))
                                            if ((((load32(v5 + 283876) - load32(v9)) * v1) + ((load32(v5 + 283872) - load32(v16)) * v1)) >= v10):
                                                break
                                            v1 = 0
                                            v4 = 1
                                            while True:  # $label567
                                                while True:  # $label565
                                                    if load32(((v5 + (v1 << 2)) + 281808)):
                                                        if not load8u(((v1 * 404) + ENTITY_TYPES) + 376):
                                                            break
                                                    while True:  # $label566
                                                        v4 = (v1 | 1)
                                                        if not load32(((v5 + ((v1 | 1) << 2)) + 281808)):
                                                            break
                                                        if load8u(((v4 * 404) + ENTITY_TYPES) + 376):
                                                            break
                                                        v4 = 1
                                                        break
                                                        break
                                                    v4 = (u32(v4) < u32(131))
                                                    v1 = (v1 + 2)
                                                    if ((v1 + 2) != 132):
                                                        continue
                                                    break
                                                break
                                            v1 = (v4 & 1)
                                            v3 = (v2 if (v4 & 1) else v3)
                                            v10 = (v11 if v1 else v10)
                                            break
                                        v2 = (v2 + 1)
                                        if ((v2 + 1) != v6):
                                            continue
                                        break
                                    if not v3:
                                        break
                                    store32(v8 + 283904, v3)
                                    v13 = (v7 + (v3 * 286704))
                                    v11 = ((v7 + (v3 * 286704)) + 283880)
                                    v12 = (v13 + 283876)
                                    v14 = (v13 + 283872)
                                    v5 = 0
                                    v17 = load32(38564)
                                    v20 = load32(38620)
                                    v21 = load32(38560)
                                    v18 = load32(PLAYER_COUNT)
                                    v16 = load32(9143004)
                                    v26 = load32(38500)
                                    v29 = load32(ENTITIES)
                                    v1 = load32(9142440)
                                    v24 = (load32(9142440) * v1)
                                    v7 = 2147483647
                                    v9 = 0
                                    while True:  # $label574
                                        while True:  # $label569
                                            v1 = load32(((v13 + (v5 << 2)) + 284636))
                                            if not load32(((v13 + (v5 << 2)) + 284636)):
                                                break
                                            v28 = load32(v1 + 8)
                                            if not load32(v1 + 8):
                                                break
                                            v23 = load32(v1)
                                            v2 = 0
                                            while True:  # $label573
                                                while True:  # $label570
                                                    v1 = load32((v23 + (v2 << 2)))
                                                    if not load32((v23 + (v2 << 2))):
                                                        break
                                                    v3 = (v29 + (v1 * 132))
                                                    v1 = load16u((v29 + (v1 * 132)) + 114)
                                                    v4 = (load16u((v29 + (v1 * 132)) + 114) - load32(v12))
                                                    v4 = load16u(v3 + 112)
                                                    v6 = (load16u(v3 + 112) - load32(v14))
                                                    v1 = (v1 - load32(v52))
                                                    v1 = (v4 - load32(v43))
                                                    v6 = load8u(v3 + 122)
                                                    v30 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                                                    v44 = load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264)
                                                    v1 = ((v24 if ((((load16u((v29 + (v1 * 132)) + 114) - load32(v12)) * v4) + ((load16u(v3 + 112) - load32(v14)) * v6)) > (load32(v11) + 100)) else 0) + ((((v1 - load32(v52)) * v1) + ((v4 - load32(v43)) * v1)) * (3 if (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264) == 4) else 1)))
                                                    if (((v24 if ((((load16u((v29 + (v1 * 132)) + 114) - load32(v12)) * v4) + ((load16u(v3 + 112) - load32(v14)) * v6)) > (load32(v11) + 100)) else 0) + ((((v1 - load32(v52)) * v1) + ((v4 - load32(v43)) * v1)) * (3 if (load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 264) == 4) else 1))) >= v7):
                                                        break
                                                    v4 = 0
                                                    while True:  # $label571
                                                        if (v6 == v26):
                                                            break
                                                        v10 = load16u(v3 + 110)
                                                        v15 = (v18 * load32(v63))
                                                        while True:  # $label572
                                                            v31 = load16u(v3 + 120)
                                                            if load16u(v3 + 120):
                                                            else:
                                                            if not load8u(((v31 if load8u((v16 + (v10 + v15))) else v10) + (v10 + v15))):
                                                                if (load8u(v3 + 127) != 6):
                                                                    break
                                                                if not load8u(v3 + 128):
                                                                    break
                                                                break
                                                            if load8u(v3 + 128):
                                                                break
                                                            break
                                                        if (load8u(v3 + 125) == 10):
                                                            break
                                                        if (load8u(v3 + 126) == 2):
                                                            break
                                                        if (load32(v3 + 64) == -1):
                                                            break
                                                        if (v44 == 2):
                                                            break
                                                        v4 = ((((load32(v30 + 188) == 55) & (v6 != v21)) & (v6 != v20)) & (v6 != v17))
                                                        break
                                                    if not v4:
                                                        break
                                                    if load32(v3 + 36):
                                                        break
                                                    if (load8u(v3 + 125) == 10):
                                                        break
                                                    v9 = load32(v3 + 28)
                                                    v7 = v1
                                                    break
                                                v2 = (v2 + 1)
                                                if ((v2 + 1) != v28):
                                                    continue
                                                break
                                            break
                                        v5 = (v5 + 1)
                                        if ((v5 + 1) != 132):
                                            continue
                                        break
                                    break
                                if not v9:
                                    break
                                v2 = 0
                                v11 = (v9 * 132)
                                v7 = load8u(((v9 * 132) + load32(ENTITIES)) + 122)
                                v16 = ((load8u(((v9 * 132) + load32(ENTITIES)) + 122) * 404) + ENTITY_TYPES)
                                while True:  # $label589
                                    while True:  # $label575
                                        v1 = ((v2 * 404) + ENTITY_TYPES)
                                        if load32(((v2 * 404) + ENTITY_TYPES) + 264):
                                            break
                                        if (load32(v1 + 268) == 1):
                                            break
                                        if not load32(v1 + 92):
                                            break
                                        if (load32(38456) == v2):
                                            break
                                        if (load32(38764) == v2):
                                            break
                                        v15 = load32(((v8 + (v2 << 2)) + 284636))
                                        if not load32(((v8 + (v2 << 2)) + 284636)):
                                            break
                                        v1 = 0
                                        v6 = load32(v15 + 8)
                                        if not load32(v15 + 8):
                                            break
                                        while True:  # $label588
                                            while True:  # $label576
                                                v5 = load32((load32(v15) + (v1 << 2)))
                                                if not load32((load32(v15) + (v1 << 2))):
                                                    break
                                                v12 = load32(ENTITIES)
                                                v4 = entities[v5]
                                                if load8u(entities[v5] + 129):
                                                    break
                                                if load32(v4 + 36):
                                                    break
                                                while True:  # $label577
                                                    if (u32(load32(9142848)) >= u32((load32(load32(GAME_STATE) + 72) * 2400))):
                                                        break
                                                    if (load32(v4 + 56) == 1):
                                                    else:
                                                    if 0:
                                                        break
                                                    if (load32(38564) != v7):
                                                        break
                                                    break
                                                v3 = load8u(v4 + 122)
                                                v13 = load32(v16 + 264)
                                                while True:  # $label578
                                                    if (load32(v16 + 188) == 55):
                                                        break
                                                    if (v13 != 1):
                                                        break
                                                    if (load32(38500) != v7):
                                                        break
                                                    break
                                                if (v13 == 4):
                                                    if (load32(((v3 * 404) + ENTITY_TYPES) + 224) == 1):
                                                        break
                                                while True:  # $label579
                                                    v5 = ((v3 * 404) + ENTITY_TYPES)
                                                    if not load32(((v3 * 404) + ENTITY_TYPES) + 272):
                                                        if (load32(38648) != v3):
                                                            break
                                                    if (load32(v16 + 208) == 2):
                                                        break
                                                    break
                                                while True:  # $label580
                                                    if (load32(38564) != v7):
                                                        break
                                                    if load8u(v5 + 334):
                                                        break
                                                    if (load32(v5 + 268) != 2):
                                                        break
                                                    break
                                                while True:  # $label581
                                                    if (v3 != load32(38728)):
                                                        if (load32(38996) != v3):
                                                            break
                                                    if v13:
                                                        break
                                                    if (load32(v16 + 268) == 2):
                                                        break
                                                    break
                                                if load8u(v5 + 379):
                                                    break
                                                while True:  # $label582
                                                    v3 = load32(v5 + 24)
                                                    if not load32(v5 + 24):
                                                        break
                                                    v10 = 0
                                                    v13 = load32(v5 + 364)
                                                    if not load32(v5 + 364):
                                                        break
                                                    while True:  # $label583
                                                        if (load32((v3 + (v10 << 2))) == v7):
                                                            break
                                                        v10 = (v10 + 1)
                                                        if (v13 != (v10 + 1)):
                                                            continue
                                                        break
                                                    break
                                                    break
                                                if load8u(v4 + 123):
                                                    break
                                                if not load8u(9147152):
                                                    if not load8u((load32(9143008) + (load16u(v4 + 110) * (load32(PLAYER_COUNT) + 1)))):
                                                        break
                                                    if (load32((load32(9215884) + (load32(v4 + 44) << 4)) + 4) == 20):
                                                        break
                                                    if (load8u(v4 + 127) == 6):
                                                        break
                                                while True:  # $label584
                                                    v5 = load32(v5 + 228)
                                                    if not load32(v5 + 228):
                                                        break
                                                    v3 = (v11 + v12)
                                                    v10 = load32(((load8u((v11 + v12) + 122) * 404) + ENTITY_TYPES) + 216)
                                                    if not load32(((load8u((v11 + v12) + 122) * 404) + ENTITY_TYPES) + 216):
                                                        break
                                                    v12 = load16u(v3 + 114)
                                                    v14 = load16u(v4 + 114)
                                                    v17 = load16u(v3 + 112)
                                                    v20 = load16u(v4 + 112)
                                                    v21 = (v5 * v5)
                                                    v3 = 0
                                                    v13 = 1
                                                    while True:  # $label587
                                                        v5 = (v14 - (v3 + v12))
                                                        v18 = ((v14 - (v3 + v12)) * v5)
                                                        v5 = 0
                                                        while True:  # $label586
                                                            while True:  # $label585
                                                                v26 = (v20 - (v5 + v17))
                                                                if (u32(v21) > u32((((v20 - (v5 + v17)) * v26) + v18))):
                                                                    v5 = (v5 + 1)
                                                                    if (v10 != (v5 + 1)):
                                                                        continue
                                                                    break
                                                                break
                                                            if not (v13 & 1):
                                                                break
                                                            break
                                                            break
                                                        v3 = (v3 + 1)
                                                        v13 = (u32((v3 + 1)) < u32(v10))
                                                        if (v3 != v10):
                                                            continue
                                                        break
                                                    break
                                                    break
                                                store8(v4 + 129, 5)
                                                v6 = load32(v15 + 8)
                                                break
                                            v1 = (v1 + 1)
                                            if (u32((v1 + 1)) < u32(v6)):
                                                continue
                                            break
                                        break
                                    v2 = (v2 + 1)
                                    if ((v2 + 1) != 132):
                                        continue
                                    break
                                break
                                break
                            v6 = load32(PLAYER_COUNT)
                            if (u32(load32(PLAYER_COUNT)) < u32(2)):
                                break
                            v13 = (v6 * v40)
                            v7 = load32(PLAYERS)
                            v1 = (load32(PLAYERS) + v62)
                            v9 = ((load32(PLAYERS) + v62) + 283876)
                            v16 = (v1 + 283872)
                            v3 = 0
                            v15 = load32(9143004)
                            v2 = 1
                            v10 = 2147483647
                            while True:  # $label594
                                while True:  # $label590
                                    if (v2 == v40):
                                        break
                                    v5 = (v7 + (v2 * 286704))
                                    if load8u((v7 + (v2 * 286704)) + 286696):
                                        break
                                    if not load8u((v15 + (v2 + v13))):
                                        break
                                    v1 = (load32(v5 + 283876) - load32(v9))
                                    v1 = (load32(v5 + 283872) - load32(v16))
                                    v11 = (((load32(v5 + 283876) - load32(v9)) * v1) + ((load32(v5 + 283872) - load32(v16)) * v1))
                                    if ((((load32(v5 + 283876) - load32(v9)) * v1) + ((load32(v5 + 283872) - load32(v16)) * v1)) >= v10):
                                        break
                                    v1 = 0
                                    v4 = 1
                                    while True:  # $label593
                                        while True:  # $label591
                                            if load32(((v5 + (v1 << 2)) + 281808)):
                                                if not load8u(((v1 * 404) + ENTITY_TYPES) + 376):
                                                    break
                                            while True:  # $label592
                                                v4 = (v1 | 1)
                                                if not load32(((v5 + ((v1 | 1) << 2)) + 281808)):
                                                    break
                                                if load8u(((v4 * 404) + ENTITY_TYPES) + 376):
                                                    break
                                                v4 = 1
                                                break
                                                break
                                            v4 = (u32(v4) < u32(131))
                                            v1 = (v1 + 2)
                                            if ((v1 + 2) != 132):
                                                continue
                                            break
                                        break
                                    v1 = (v4 & 1)
                                    v3 = (v2 if (v4 & 1) else v3)
                                    v10 = (v11 if v1 else v10)
                                    break
                                v2 = (v2 + 1)
                                if ((v2 + 1) != v6):
                                    continue
                                break
                            if not v3:
                                break
                            v1 = (v7 + (v3 * 286704))
                            v2 = load32((v7 + (v3 * 286704)) + 283876)
                            v5 = load32(v52)
                            v2 = (v5 - v2)
                            v2 = load32(v43)
                            v1 = load32(v1 + 283872)
                            v5 = (load32(v43) - load32(v1 + 283872))
                            # TODO: f32.demote_f64
                            v66 = sqrt(i32((((v5 - v2) * v2) + ((load32(v43) - load32(v1 + 283872)) * v5))))
                            v67 = ((i32(load32((v7 + (v3 * 286704)) + 283876)) - i32(load32(v52))) / sqrt(i32((((v5 - v2) * v2) + ((load32(v43) - load32(v1 + 283872)) * v5)))))
                            v66 = ((i32(v1) - i32(v2)) / v66)
                            # TODO: f32.demote_f64
                            v70 = sqrt(i32(load32(v8 + 283880)))
                            v1 = 0
                            while True:  # $label601
                                while True:  # $label595
                                    v2 = ((v1 * 404) + ENTITY_TYPES)
                                    if load32(((v1 * 404) + ENTITY_TYPES) + 264):
                                        break
                                    if (load32(v2 + 268) == 1):
                                        break
                                    if not load32(v2 + 92):
                                        break
                                    if (load32(38456) == v1):
                                        break
                                    if (load32(38764) == v1):
                                        break
                                    while True:  # $label596
                                        v68 = (v70 + i32((6 if (load32(v2 + 224) > 1) else 10)))
                                        # TODO: f64.promote_f32
                                        v105 = ((v66 * (v70 + i32((6 if (load32(v2 + 224) > 1) else 10)))) + 0.5)
                                        if (abs(((v66 * (v70 + i32((6 if (load32(v2 + 224) > 1) else 10)))) + 0.5)) < 2147483648.0):
                                            break
                                        break
                                    v5 = -2147483648
                                    v4 = load32(v43)
                                    v2 = load32(9142440)
                                    while True:  # $label597
                                        # TODO: f64.promote_f32
                                        v105 = ((v67 * v68) + 0.5)
                                        if (abs(((v67 * v68) + 0.5)) < 2147483648.0):
                                            break
                                        break
                                    v3 = (-2147483648 + load32(v52))
                                    if (u32(i32(v105)) <= u32((-2147483648 + load32(v52)))):
                                        break
                                    v4 = (v4 + v5)
                                    if (u32(v2) <= u32((v4 + v5))):
                                        break
                                    if ((v3 | v4) < 0):
                                        break
                                    v2 = load8s((load32(9147288) + ((v2 * v3) + v4)))
                                    if (load8s((load32(9147288) + ((v2 * v3) + v4))) >= 0):
                                        if (load32(load32((load32(9140332) + ((v2 & 255) << 2))) + 32) == 23):
                                            break
                                    v7 = load32(((v8 + (v1 << 2)) + 284636))
                                    if not load32(((v8 + (v1 << 2)) + 284636)):
                                        break
                                    v6 = load32(v7 + 8)
                                    if not load32(v7 + 8):
                                        break
                                    v13 = (v3 if (u32(v3) > u32(v4)) else v4)
                                    v2 = 0
                                    while True:  # $label600
                                        while True:  # $label598
                                            v5 = load32((load32(v7) + (v2 << 2)))
                                            if not load32((load32(v7) + (v2 << 2))):
                                                break
                                            v5 = entities[v5]
                                            if load8u(entities[v5] + 129):
                                                break
                                            if load32(v5 + 36):
                                                break
                                            if load8u(v5 + 123):
                                                break
                                            while True:  # $label599
                                                if not load8u(9147152):
                                                    if not load8u((load32(9143008) + (load16u(v5 + 110) * (load32(PLAYER_COUNT) + 1)))):
                                                        break
                                                    if (load32((load32(9215884) + (load32(v5 + 44) << 4)) + 4) == 20):
                                                        break
                                                    if (load8u(v5 + 127) == 6):
                                                        break
                                                    if (u32(load32(9142440)) > u32(v13)):
                                                        break
                                                    break
                                                if (u32(load32(9142440)) <= u32(v13)):
                                                    break
                                                break
                                            v10 = (load16u(v5 + 112) - v4)
                                            v10 = (load16u(v5 + 114) - v3)
                                            if (((((load16u(v5 + 112) - v4) * v10) + ((load16u(v5 + 114) - v3) * v10)) - 1) < 37):
                                                break
                                            v6 = load32(v7 + 8)
                                            break
                                        v2 = (v2 + 1)
                                        if (u32((v2 + 1)) < u32(v6)):
                                            continue
                                        break
                                    break
                                v1 = (v1 + 1)
                                if ((v1 + 1) != 132):
                                    continue
                                break
                            break
                        v40 = (v40 + 1)
                        if (u32((v40 + 1)) < u32(load32(PLAYER_COUNT))):
                            continue
                        break
                store32(9687188, (load32(9687188) + 1))
                G.global0 = (v19 + 96)
            if not ((load32(9142848) * 25) % 5000):
                a_b()
                v53 = 0
            if load8u(59128):
                store32(arg0 + 16, load32((load32(9215884) + (load32((load32(ENTITIES) + 1690568)) << 4))))
                store32(arg0 + 20, load32(9142848))
            jc((load32(9142848) * 25))
            if load8u(9147124):
                store8(9147124, 0)
            while True:  # $label603
                if not load8u(9142904):
                    break
                if load8u(9147152):
                    break
                if (((load32(9142848) * 25) - 25) % load32(51788)):
                    break
                store32(arg0, load32(9147376))
                store32(arg0 + 4, load32(9142440))
                store32(arg0 + 8, load32(40608))
                store32(arg0 + 12, load32(40612))
                a_b()
                store32(40608, 2147483647)
                store32(40612, -2147483647)
                store8(9142904, 0)
                break
            if load8u(9147210):
            else:
            v5 = not 1
            a_b()
            v2 = load32(59160)
            v1 = load32(9142848)
            while True:  # $label605
                while True:  # $label604
                    if v5:
                        break
                    if (u32(v1) >= u32(v2)):
                        break
                    if not load8u(9215872):
                        break
                    break
                if ((u32((v1 + 20)) < u32(v2)) & v5):
                    a_b()
                store32(51776, 1)
                while True:  # $label606
                    if load32(51776):
                        continue
                    break
                func54(9684264)
                v2 = load32(59160)
                v1 = load32(9142848)
                break
            if (u32(v1) < u32(v2)):
                continue
            break
    if v53:
        a_b()
    G.global0 = (arg0 - -64)
    return 0
