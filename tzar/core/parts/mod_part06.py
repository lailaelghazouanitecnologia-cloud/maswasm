"""
Tzar Engine - Core module (part 6).
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
# $func223
# ----------------------------------------------------------
def func223(arg0):
    arg0 = 0
    store32(9671124, 96)
    store32(9671120, 0)
    while True:  # $label0
        v3 = entities[load32(9173808)]
        v1 = load32(entities[load32(9173808)].z)
        if not load32(entities[load32(9173808)].z):
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
        if not load32(v1 + 60):
            break
        store32(((arg0 << 2) + 9263072), load32(((v1 * 404) + 9567872)))
        store32(9671120, (arg0 + 1))
        break
    return func46(0, 1)

# ----------------------------------------------------------
# $func224
# ----------------------------------------------------------
def func224(arg0, arg1, arg2):
    v4 = load32(9142440)
    v6 = (load32(9142440) + 2)
    v7 = ((load32(9142440) + 2) if (arg1 != 2) else 0)
    v5 = ((load8u(arg0 + 122) * 404) + ENTITY_TYPES)
    v8 = (load16u(arg0 + 114) + ((load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 220) & 0xFFFFFFFF) >> 1))
    v9 = (load16u(arg0 + 112) + ((load32(v5 + 216) & 0xFFFFFFFF) >> 1))
    v5 = load32(ENTITIES)
    v10 = load32(9142840)
    while True:  # $label1
        while True:  # $label3
            if arg2:
                while True:  # $label2
                    while True:  # $label0
                        arg0 = v3
                        v3 = (v3 << 2)
                        arg1 = (v8 + load32((((v3 << 2) | 4) + 8611904)))
                        if (u32(v4) <= u32((v8 + load32((((v3 << 2) | 4) + 8611904))))):
                            break
                        v3 = (v9 + load32((v3 + 8611904)))
                        if (u32(v4) <= u32((v9 + load32((v3 + 8611904))))):
                            break
                        if ((arg1 | v3) < 0):
                            break
                        v3 = load32((((v3 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4)
                        if (load8u((v5 + (load32((((v3 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4) * 132)) + 122) == arg2):
                            break
                        break
                    v3 = (arg0 + 2)
                    if (u32(arg0) <= u32(717)):
                        continue
                    break
                    break
                raise Unreachable()
            if (arg1 == 2):
                v11 = load32(9142848)
                v12 = load32(38500)
                while True:  # $label5
                    while True:  # $label4
                        arg0 = v3
                        arg2 = (v3 << 2)
                        arg1 = (v8 + load32((((v3 << 2) | 4) + 8611904)))
                        if (u32(v4) <= u32((v8 + load32((((v3 << 2) | 4) + 8611904))))):
                            break
                        arg2 = (v9 + load32((arg2 + 8611904)))
                        if (u32(v4) <= u32((v9 + load32((arg2 + 8611904))))):
                            break
                        if ((arg1 | arg2) < 0):
                            break
                        v3 = load32((((arg2 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4)
                        arg1 = (v5 + (load32((((arg2 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4) * 132))
                        if (v12 != load8u((v5 + (load32((((arg2 + (((arg1 + v7) + 1) * v6)) << 2) + v10) + 4) * 132)) + 122)):
                            break
                        arg1 = load32(arg1 + 88)
                        if not load32(arg1 + 88):
                            break
                        if (u32(((v11 - arg1) * 25)) > u32(25000)):
                            break
                        break
                    v3 = (arg0 + 2)
                    if (u32(arg0) <= u32(717)):
                        continue
                    break
                break
            v11 = load32(38448)
            arg0 = 0
            if (arg1 == 1):
                while True:  # $label7
                    while True:  # $label6
                        arg1 = arg0
                        arg2 = (arg0 << 2)
                        arg0 = (v8 + load32((((arg0 << 2) | 4) + 8611904)))
                        if (u32(v4) <= u32((v8 + load32((((arg0 << 2) | 4) + 8611904))))):
                            break
                        arg2 = (v9 + load32((arg2 + 8611904)))
                        if (u32(v4) <= u32((v9 + load32((arg2 + 8611904))))):
                            break
                        if ((arg0 | arg2) < 0):
                            break
                        v3 = load32((((arg2 + (((arg0 + v7) + 1) * v6)) << 2) + v10) + 4)
                        if (v11 == load8u((v5 + (load32((((arg2 + (((arg0 + v7) + 1) * v6)) << 2) + v10) + 4) * 132)) + 122)):
                            break
                        break
                    arg0 = (arg1 + 2)
                    if (u32(arg1) <= u32(717)):
                        continue
                    break
                    break
                raise Unreachable()
            v12 = load32(38504)
            v13 = load32(38508)
            while True:  # $label11
                while True:  # $label8
                    arg2 = arg0
                    v3 = (arg0 << 2)
                    arg0 = (v8 + load32((((arg0 << 2) | 4) + 8611904)))
                    if (u32(v4) <= u32((v8 + load32((((arg0 << 2) | 4) + 8611904))))):
                        break
                    v3 = (v9 + load32((v3 + 8611904)))
                    if (u32(v4) <= u32((v9 + load32((v3 + 8611904))))):
                        break
                    if ((arg0 | v3) < 0):
                        break
                    v3 = load32((((v3 + (((arg0 + v7) + 1) * v6)) << 2) + v10) + 4)
                    while True:  # $label10
                        while True:  # $label9
                            # br_table arg1
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
                if (u32(arg2) <= u32(717)):
                    continue
                break
            break
        return 0
        break
    return load32((v5 + (v3 * 132)) + 28)

# ----------------------------------------------------------
# $func225
# ----------------------------------------------------------
def func225(arg0, arg1, arg2, arg3):
    v6 = load32(9142440)
    v12 = load16u(arg2 + 114)
    v13 = load16u(arg2 + 112)
    while True:  # $label9
        while True:  # $label0
            v11 = v4
            v4 = (v4 << 2)
            v7 = (load32((((v4 << 2) | 4) + 8611904)) + v12)
            if (u32(v6) <= u32((load32((((v4 << 2) | 4) + 8611904)) + v12))):
                break
            v8 = (load32((v4 + 8611904)) + v13)
            if (u32(v6) <= u32((load32((v4 + 8611904)) + v13))):
                break
            if ((v7 | v8) < 0):
                break
            while True:  # $label1
                v4 = (v6 + 2)
                v4 = load32((load32(9142840) + ((v8 + (((v7 + (v6 + 2)) + 1) * v4)) << 2)) + 4)
                if not load32((load32(9142840) + ((v8 + (((v7 + (v6 + 2)) + 1) * v4)) << 2)) + 4):
                    break
                v4 = entities[v4]
                if (load8u(entities[v4] + 129) == 10):
                    break
                if (load32(38528) != load8u(v4 + 122)):
                    break
                break
            v4 = func56(v8, v7, arg3, load16u(arg2 + 110), 0, 0, 1, 1, 0)
            v6 = load32(9142440)
            if not v4:
                break
            while True:  # $label8
                while True:  # $label5
                    while True:  # $label4
                        while True:  # $label2
                            while True:  # $label3
                                v5 = ((load8u(arg2 + 122) * 404) + ENTITY_TYPES)
                                # br_table load32(((load8u(arg2 + 122) * 404) + ENTITY_TYPES) + 264)
                                break
                                break
                            v14 = load32(v5 + 216)
                            if not load32(v5 + 216):
                                v4 = load32(9142432)
                                break
                            v4 = load32(9142432)
                            v15 = load32(v5 + 220)
                            if not load32(v5 + 220):
                                break
                            v5 = load32(9215880)
                            if not load32(9215880):
                                break
                            if not v4:
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
                                    if not load32((v18 + (load32((v4 + ((v19 + ((v9 + v16) * v6)) << 2))) << 2))):
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
                        if not load32(9142432):
                            break
                        v10 = load32((v4 + ((load16u(arg2 + 112) + (v6 * load16u(arg2 + 114))) << 2)))
                        break
                        break
                    v10 = 0
                    if not v4:
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
        if (u32(v11) < u32(5198)):
            continue
        break
    return 0

# ----------------------------------------------------------
# $func226
# ----------------------------------------------------------
def func226(arg0, arg1):
    store32(arg0 + 8, 0)
    store64(arg0, 0)
    v2 = load32(arg1 + 4)
    v4 = load32(arg1)
    v5 = (load32(arg1 + 4) - load32(arg1))
    v3 = ((load32(arg1 + 4) - load32(arg1)) // 196)
    while True:  # $label2
        while True:  # $label0
            if (v2 != v4):
                if (u32(v3) >= u32(21913099)):
                    break
                v2 = func26(v5)
                store32(arg0 + 4, func26(v5))
                store32(arg0, v2)
                store32(arg0 + 8, (v2 + (v3 * 196)))
                v3 = load32(arg1)
                v4 = load32(arg1 + 4)
                if (load32(arg1) != load32(arg1 + 4)):
                    while True:  # $label1
                        # TODO: memory.copy
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
                if (u32(v3) >= u32(21913099)):
                    break
                v2 = func26(v5)
                store32(arg0 + 16, func26(v5))
                store32(arg0 + 12, v2)
                store32(arg0 + 20, (v2 + (v3 * 196)))
                v3 = load32(arg1 + 12)
                v4 = load32(arg1 + 16)
                if (load32(arg1 + 12) != load32(arg1 + 16)):
                    while True:  # $label3
                        # TODO: memory.copy
                        v2 = (v2 + 196)
                        v3 = (v3 + 196)
                        if ((v3 + 196) != v4):
                            continue
                        break
                store32(arg0 + 16, v2)
            # TODO: memory.copy
            return arg0
            break
        func42()
        raise Unreachable()
        break
    func42()
    raise Unreachable()
    return 104

# ----------------------------------------------------------
# $func227
# ----------------------------------------------------------
def func227():
    while True:  # $label0
        if load8u(9142411):
            break
        if not load32(load32(GAME_STATE) + 48):
            break
        while True:  # $label1
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
                    while True:  # $label2
                        v4 = (v1 + 2)
                        v3 = (v3 + 1)
                        v0 = load32((v2 + ((((v1 + 2) * (v3 + 1)) + v6) << 2)))
                        if (u32(load32((v2 + ((((v1 + 2) * (v3 + 1)) + v6) << 2)))) < u32(3)):
                            break
                        v0 = entities[v0]
                        if load32(entities[v0].target_id):
                            break
                        v1 = load32(9142440)
                        v4 = (load32(9142440) + 2)
                        v2 = load32(9142840)
                        break
                    while True:  # $label3
                        v0 = load32((v2 + ((((v3 + v4) * v4) + v6) << 2)))
                        if (u32(load32((v2 + ((((v3 + v4) * v4) + v6) << 2)))) < u32(3)):
                            break
                        v0 = entities[v0]
                        if load32(entities[v0].target_id):
                            break
                        v1 = load32(9142440)
                        v4 = (load32(9142440) + 2)
                        v2 = load32(9142840)
                        break
                    while True:  # $label4
                        v0 = load32((v2 + (((((v4 << 1) + v3) * v4) + v6) << 2)))
                        if (u32(load32((v2 + (((((v4 << 1) + v3) * v4) + v6) << 2)))) < u32(3)):
                            break
                        v0 = entities[v0]
                        if load32(entities[v0].target_id):
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

# ----------------------------------------------------------
# $func228
# ----------------------------------------------------------
def func228(arg0, arg1, arg2):
    v9 = (i32(arg1) * 132)
    v5 = i32((i32(arg1) * 132))
    v3 = (i32((i32(arg1) * 132)) + 4)
    v3 = func26((-1 if i32(((v9 & 0xFFFFFFFF) >> 32)) else (-1 if (u32(v3) < u32(v5)) else (i32((i32(arg1) * 132)) + 4))))
    store32(func26((-1 if i32(((v9 & 0xFFFFFFFF) >> 32)) else (-1 if (u32(v3) < u32(v5)) else (i32((i32(arg1) * 132)) + 4)))), arg1)
    v5 = (v3 + 4)
    if arg1:
        v7 = (v5 + (arg1 * 132))
        arg1 = v5
        while True:  # $label0
            # TODO: memory.fill
            v4 = func26(4)
            store32(arg1 + 4, func26(4))
            store32(arg1, v4)
            store32(arg1 + 8, (v4 + 4))
            arg1 = (arg1 + 132)
            if ((arg1 + 132) != v7):
                continue
            break
    while True:  # $label5
        while True:  # $label2
            if arg2:
                if (arg0 != v5):
                    arg1 = 0
                    while True:  # $label1
                        v3 = (arg1 * 132)
                        v4 = (v5 + (arg1 * 132))
                        v3 = (arg0 + v3)
                        # TODO: memory.copy
                        arg1 = (arg1 + 1)
                        if ((arg1 + 1) != arg2):
                            continue
                        break
                    break
                v4 = (arg2 & 3)
                v3 = (v3 + 16)
                v7 = 0
                arg1 = 0
                if (u32(arg2) >= u32(4)):
                    v8 = (arg2 & -4)
                    arg2 = 0
                    while True:  # $label3
                        v6 = (arg1 * 132)
                        # TODO: memory.copy
                        v6 = ((arg1 | 1) * 132)
                        # TODO: memory.copy
                        v6 = ((arg1 | 2) * 132)
                        # TODO: memory.copy
                        v6 = ((arg1 | 3) * 132)
                        # TODO: memory.copy
                        arg1 = (arg1 + 4)
                        arg2 = (arg2 + 4)
                        if ((arg2 + 4) != v8):
                            continue
                        break
                if not v4:
                    break
                while True:  # $label4
                    arg2 = (arg1 * 132)
                    # TODO: memory.copy
                    arg1 = (arg1 + 1)
                    v7 = (v7 + 1)
                    if ((v7 + 1) != v4):
                        continue
                    break
                break
            if not arg0:
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

# ----------------------------------------------------------
# $hd
# Export: hd
# ----------------------------------------------------------
def hd():
    """Export: hd"""
    v2 = 3
    if (u32(load32(9671136)) > u32(3)):
        while True:  # $label1
            while True:  # $label0
                v0 = entities[v2]
                if not load32(entities[v2].max_hp):
                    break
                if not load32(v0 + 40):
                    break
                if not load32(v0 + 64):
                    if (load32(38448) != load8u(v0 + 122)):
                        break
                    break
                v3 = load32(v0 + 48)
                v1 = load32(load32(v0 + 48) + 20)
                v4 = load8u(v0 + 124)
                if (load32(load32(v0 + 48) + 20) <= load8u(v0 + 124)):
                    v1 = (v4 % v1)
                    store8(v0 + 124, ((3 if (u32(v1) < u32(3)) else (v4 % v1)) if (load32(38448) == load8u(v0 + 122)) else v1))
                v0 = load8u(v0 + 125)
                break
            v2 = (v2 + 1)
            if (u32((v2 + 1)) < u32(load32(9671136))):
                continue
            break
    func320(1)

# ----------------------------------------------------------
# $func230
# ----------------------------------------------------------
def func230(arg0):
    v4 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v6 = players[load16u(arg0 + 110)]
    v1 = load32(arg0 + 20)
    while True:  # $label10
        while True:  # $label0
            while True:  # $label9
                while True:  # $label8
                    v2 = load32(load32(v1))
                    if (u32(load32(load32(v1))) < u32(2147483647)):
                        break
                    v2 = ((v2 - 2147483647) if (u32(v2) > u32(2147483646)) else v2)
                    v1 = load32(((v6 + (((v2 - 2147483647) if (u32(v2) > u32(2147483646)) else v2) * 36)) + 269376))
                    v3 = (load32(((v6 + (((v2 - 2147483647) if (u32(v2) > u32(2147483646)) else v2) * 36)) + 269376)) if v1 else 100)
                    v1 = ((v2 * 404) + ENTITY_TYPES)
                    store32(v4, (((load32(((v6 + (((v2 - 2147483647) if (u32(v2) > u32(2147483646)) else v2) * 36)) + 269376)) if v1 else 100) * load32(((v2 * 404) + ENTITY_TYPES) + 68)) // 100))
                    store32(v4 + 4, ((load32(v1 + 72) * v3) // 100))
                    store32(v4 + 8, ((load32(v1 + 76) * v3) // 100))
                    store32(v4 + 12, ((load32(v1 + 80) * v3) // 100))
                    while True:  # $label6
                        while True:  # $label2
                            while True:  # $label1
                                v7 = load32(v1 + 180)
                                if not load8u(load32(v1 + 180) + 23):
                                    break
                                v1 = load32(v7 + 4)
                                if (load32(((load32(v7 + 4) * 404) + ENTITY_TYPES) + 264) != 3):
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
                                    v10 = load32(((load32((v7 + (v3 << 2)) + 28) * 404) + ENTITY_TYPES) + 264)
                                    v11 = (load32(((load32((v7 + (v3 << 2)) + 28) * 404) + ENTITY_TYPES) + 264) == 1)
                                    while True:  # $label4
                                        while True:  # $label3
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
                                if not (((v5 & v8) if (v1 & 1) else v5) & 1):
                                    break
                            if not func66(v6, v4, 0, 1):
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
                                if (u32(v3) < u32(load32(v1 + 8))):
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
            if not load32(arg0 + 92):
                break
            v1 = load8u(9147141)
            if load32(9140316):
                if (load32(9140320) != load32(arg0 + 28)):
                    break
            break
            break
        v1 = ((v2 * 404) + ENTITY_TYPES)
        v1 = ((load32(((v2 * 404) + ENTITY_TYPES) + 116) * load32((load32(GAME_STATE) + (132 if load32(v1 + 264) else 128)))) * 1000)
        v2 = (u32(((load32(((v2 * 404) + ENTITY_TYPES) + 116) * load32((load32(GAME_STATE) + (132 if load32(v1 + 264) else 128)))) * 1000)) < u32(100))
        # TODO: i32.div_u
        v1 = 100
        while True:  # $label11
            if (load32(CURRENT_PLAYER) != load16u(arg0 + 110)):
                break
            v3 = load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 180)
            if not load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 180):
                break
            break
        v1 = (25 if v2 else v1)
        v2 = load32(arg0 + 44)
        if load32(arg0 + 44):
            # TODO: i32.div_u
            store32(load32(9142848), (v1 + 25))
            break
        func63((load32(9215884) + (v2 << 4)), arg0, 2, 0, v1)
        break
    G.global0 = (v4 + 16)

# ----------------------------------------------------------
# $func231
# ----------------------------------------------------------
def func231(arg0):
    v1 = (G.global0 - 48)
    G.global0 = (G.global0 - 48)
    v2 = (v1 + 4)
    # TODO: memory.fill
    # TODO: memory.copy
    func436(9688272)
    store32(arg0, load32(52428))
    store32(arg0 + 4, load32(52432))
    func266(9688272)
    G.global0 = (v1 + 48)

# ----------------------------------------------------------
# $func232
# ----------------------------------------------------------
def func232(arg0):
    while True:  # $label0
        if not arg0:
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
            while True:  # $label3
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
                        while True:  # $label4
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

# ----------------------------------------------------------
# $func233
# ----------------------------------------------------------
def func233(arg0, arg1):
    v2 = load32(ENTITIES)
    v5 = entities[arg0]
    if (load8u(entities[arg0].unit_class) != 3):
        return 0
    v4 = load16u(v5 + 116)
    if not load16u(v5 + 116):
        return 0
    while True:  # $label0
        arg0 = (load16u((v2 + (arg0 * 132)) + 110) << 2)
        if not load32(((load16u((v2 + (arg0 * 132)) + 110) << 2) + load32(arg1 + 48))):
            if not load32((load32(9142420) + arg0)):
                break
        v6 = load16u((v2 + (v4 * 132)) + 110)
        if not load32((load32(arg1 + 64) + (load16u((v2 + (v4 * 132)) + 110) << 2))):
            if not load32((load32(9142420) + (v6 << 2))):
                break
        while True:  # $label11
            while True:  # $label10
                while True:  # $label5
                    while True:  # $label4
                        while True:  # $label1
                            while True:  # $label3
                                while True:  # $label2
                                    # br_table load32(arg1 + 8)
                                    break
                                    break
                                v7 = load32(arg1 + 104)
                                if not load32(arg1 + 104):
                                    break
                                v2 = load32((v2 + (v4 * 132)) + 28)
                                arg1 = load32(arg1 + 96)
                                arg0 = 0
                                break
                                break
                            arg1 = load32(9140300)
                            if not load32(9140300):
                                break
                            v2 = load32((v2 + (v4 * 132)) + 28)
                            arg0 = 0
                            break
                            break
                        arg1 = load32(arg1 + 36)
                        if (u32(load32(arg1 + 36)) <= u32(3)):
                            v2 = (v2 + (v4 * 132))
                            arg0 = load8u((v2 + (v4 * 132)) + 122)
                            while True:  # $label9
                                while True:  # $label7
                                    while True:  # $label8
                                        while True:  # $label6
                                            # br_table (arg1 - 1)
                                            break
                                            break
                                        arg1 = ((arg0 * 404) + ENTITY_TYPES)
                                        if load32(((arg0 * 404) + ENTITY_TYPES) + 264):
                                            return 0
                                        if (load32(arg1 + 268) == 1):
                                            break
                                        if not load32(((arg0 * 404) + ENTITY_TYPES) + 92):
                                            break
                                        if (load32(38456) == arg0):
                                            break
                                        if (load32(38764) != arg0):
                                            break
                                        break
                                        break
                                    if (load32(((arg0 * 404) + ENTITY_TYPES) + 264) == 1):
                                        break
                                    break
                                    break
                                if load32(((arg0 * 404) + ENTITY_TYPES) + 264):
                                    break
                                break
                            arg0 = 0
                            v2 = load32(v2 + 28)
                            arg1 = load32(9140300)
                            if (u32(load32(9684388)) >= u32(2)):
                                if not arg1:
                                    arg1 = 0
                                    break
                                while True:  # $label12
                                    if (load32(((arg0 << 2) + 8451904)) == v2):
                                        break
                                    arg0 = (arg0 + 1)
                                    if ((arg0 + 1) != arg1):
                                        continue
                                    break
                            if (u32(arg1) < u32(40000)):
                                break
                            break
                        v2 = (v2 + (v4 * 132))
                        if (load8u((v2 + (v4 * 132)) + 122) != (arg1 - 4)):
                            break
                        arg0 = 0
                        v2 = load32(v2 + 28)
                        arg1 = load32(9140300)
                        if (u32(load32(9684388)) >= u32(2)):
                            if not arg1:
                                arg1 = 0
                                break
                            while True:  # $label13
                                if (load32(((arg0 << 2) + 8451904)) == v2):
                                    break
                                arg0 = (arg0 + 1)
                                if ((arg0 + 1) != arg1):
                                    continue
                                break
                        if (u32(arg1) < u32(40000)):
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
                    if (u32(load32(9684388)) >= u32(2)):
                        if not arg1:
                            arg1 = 0
                            break
                        while True:  # $label15
                            if (load32(((arg0 << 2) + 8451904)) == v2):
                                break
                            arg0 = (arg0 + 1)
                            if ((arg0 + 1) != arg1):
                                continue
                            break
                    if (u32(arg1) < u32(40000)):
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
                if (u32(load32(9684388)) > u32(1)):
                    while True:  # $label17
                        if (load32(((arg0 << 2) + 8451904)) == v2):
                            break
                        arg0 = (arg0 + 1)
                        if ((arg0 + 1) != arg1):
                            continue
                        break
                if (u32(arg1) > u32(39999)):
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

# ----------------------------------------------------------
# $func234
# ----------------------------------------------------------
def func234(arg0, arg1):
    v7 = (arg0 - 16)
    if load32((arg0 - 16)):
        while True:  # $label28
            v2 = (arg0 + (v5 * 60))
            store32(9681920, (load32(9681920) + ((load32((arg0 + (v5 * 60))) * load32(v2 + 4)) << 2)))
            v3 = load32(v2 + 28)
            while True:  # $label1
                while True:  # $label3
                    while True:  # $label2
                        while True:  # $label0
                            v6 = load32(v2 + 32)
                            # br_table (load32(v2 + 32) - 23)
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
            while True:  # $label27
                if (u32(v3) <= u32(9999)):
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
                                                                    while True:  # $label14
                                                                        while True:  # $label13
                                                                            while True:  # $label12
                                                                                while True:  # $label11
                                                                                    while True:  # $label10
                                                                                        while True:  # $label9
                                                                                            while True:  # $label8
                                                                                                while True:  # $label7
                                                                                                    while True:  # $label6
                                                                                                        while True:  # $label5
                                                                                                            while True:  # $label4
                                                                                                                # br_table v6
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
                                                                                        v4 = ((v3 * 404) + ENTITY_TYPES)
                                                                                        v6 = load32(v4 + 20)
                                                                                        store32(((v3 * 404) + ENTITY_TYPES) + 20, (load32(v4 + 20) + 1))
                                                                                        store32((v4 + (v6 << 2)), v2)
                                                                                        break
                                                                                        break
                                                                                    v4 = ((v3 * 404) + ENTITY_TYPES)
                                                                                    v6 = load32(v4 + 20)
                                                                                    store32(((v3 * 404) + ENTITY_TYPES) + 20, (load32(v4 + 20) + 1))
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
                    v4 = ((v3 * 404) + ENTITY_TYPES)
                    v6 = load32(v4 + 20)
                    store32(((v3 * 404) + ENTITY_TYPES) + 20, (load32(v4 + 20) + 1))
                    store32((v4 + (v6 << 2)), v2)
                    break
                if (u32(v3) > u32(19999)):
                    break
                v3 = (v3 - 10000)
                if (u32((v3 - 10000)) > u32(95)):
                    break
                store32(((v3 << 2) + 9142448), v2)
                break
            store32(v2 + 28, 2147483647)
            v5 = (v5 + 1)
            if (u32((v5 + 1)) < u32(load32(v7))):
                continue
            break
    while True:  # $label31
        if arg1:
            arg0 = 0
            while True:  # $label30
                arg1 = ((arg0 * 72) + 9263856)
                if not load32(((arg0 * 72) + 9263856)):
                    store32(arg1, load32(arg1 + 4))
                while True:  # $label29
                    v4 = load32(arg1 + 8)
                    if not load32(arg1 + 8):
                        if load32(((arg0 * 404) + ENTITY_TYPES) + 264):
                            break
                        v4 = load32(arg1 + 12)
                        store32(arg1 + 8, load32(arg1 + 12))
                        if not v4:
                            break
                    arg1 = load32(((arg0 * 404) + ENTITY_TYPES) + 276)
                    if not load32(((arg0 * 404) + ENTITY_TYPES) + 276):
                        break
                    if (load32(v4 + 24) > 99):
                        break
                    # TODO: i32.div_u
                    store32((load32(v4 + 16) * 1000) + 24, arg1)
                    break
                arg0 = (arg0 + 1)
                if ((arg0 + 1) != 255):
                    continue
                break
            break
        v2 = ((v3 * 404) + ENTITY_TYPES)
        arg1 = ((v3 * 72) + 9263856)
        arg0 = 0
        while True:  # $label33
            while True:  # $label32
                if (arg0 != v3):
                    break
                if not load32(arg1):
                    store32(arg1, load32(arg1 + 4))
                v5 = load32(arg1 + 8)
                if not load32(arg1 + 8):
                    if load32(v2 + 264):
                        break
                    v5 = load32(arg1 + 12)
                    store32(arg1 + 8, load32(arg1 + 12))
                    if not v5:
                        break
                v4 = load32(v2 + 276)
                if not load32(v2 + 276):
                    break
                if (load32(v5 + 24) > 99):
                    break
                # TODO: i32.div_u
                store32((load32(v5 + 16) * 1000) + 24, v4)
                break
            arg0 = (arg0 + 1)
            if ((arg0 + 1) != 255):
                continue
            break
        break
    return v3

# ----------------------------------------------------------
# $func235
# ----------------------------------------------------------
def func235(arg0, arg1, arg2, arg3, arg4):
    v17 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    v12 = load16u(arg3 + 112)
    while True:  # $label0
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
        v6 = ((load8u(arg2 + 122) * 404) + ENTITY_TYPES)
        v20 = load32(((load8u(arg2 + 122) * 404) + ENTITY_TYPES) + 212)
        v21 = load32(v6 + 208)
        v23 = load16u(arg2 + 114)
        v27 = load16u(arg2 + 112)
        v24 = (v12 - 1)
        v14 = load16u(arg3 + 114)
        v22 = (load16u(arg3 + 114) - 1)
        if (load32(((v25 * 404) + ENTITY_TYPES) + 264) == 2):
            arg2 = 1
            v8 = load32(9142840)
            v6 = (v12 + 1)
            arg4 = (v14 + 1)
            v5 = load32(9142440)
            arg3 = (load32(9142440) + 2)
            if not load32((load32(9142840) + (((v12 + 1) + (((v14 + 1) + (load32(9142440) + 2)) * arg3)) << 2))):
                store32(arg0, v12)
                store32(arg1, v14)
                break
            arg2 = (v24 - v27)
            v7 = ((v24 - v27) * arg2)
            arg2 = 2147483647
            while True:  # $label1
                if (u32(v5) <= u32(v22)):
                    break
                if ((v22 | v24) < 0):
                    break
                if (u32(v5) <= u32(v24)):
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
            while True:  # $label2
                if (u32(v5) <= u32(v14)):
                    break
                if not v12:
                    break
                if (u32(v5) <= u32(v24)):
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
            while True:  # $label3
                if (u32(arg4) >= u32(v5)):
                    break
                if ((arg4 | v24) < 0):
                    break
                if (u32(v5) <= u32(v24)):
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
            while True:  # $label4
                if (u32(v5) <= u32(v22)):
                    break
                if not v14:
                    break
                if (u32(v5) <= u32(v12)):
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
            while True:  # $label5
                if (u32(v5) <= u32(v14)):
                    break
                if (u32(v5) <= u32(v12)):
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
            while True:  # $label6
                if (u32(arg4) >= u32(v5)):
                    break
                if (u32(v5) <= u32(v12)):
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
            while True:  # $label7
                if (u32(v5) <= u32(v22)):
                    break
                if ((v6 | v22) < 0):
                    break
                if (u32(v5) <= u32(v6)):
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
            while True:  # $label8
                if (u32(v5) <= u32(v14)):
                    break
                if (u32(v5) <= u32(v6)):
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
            while True:  # $label9
                if (u32(arg4) >= u32(v5)):
                    break
                if (u32(v5) <= u32(v6)):
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
        while True:  # $label10
            if (v25 != load32(38508)):
                if (load32(38504) != v25):
                    break
            while True:  # $label11
                # br_table (load8u(arg2 + 129) - 1)
                break
                break
            v29 = ((v26 * 404) + 9568312)
            v5 = load32(9142440)
            v6 = 0
            while True:  # $label29
                while True:  # $label12
                    v8 = v6
                    v6 = (v6 << 2)
                    v9 = (load32((((v6 << 2) | 4) + 9488)) + load16u(arg3 + 114))
                    v10 = ((load32((((v6 << 2) | 4) + 9488)) + load16u(arg3 + 114)) - 1)
                    if (u32(v5) <= u32(((load32((((v6 << 2) | 4) + 9488)) + load16u(arg3 + 114)) - 1))):
                        break
                    v7 = (load32((v6 + 9488)) + load16u(arg3 + 112))
                    v13 = ((load32((v6 + 9488)) + load16u(arg3 + 112)) - 1)
                    if (u32(v5) <= u32(((load32((v6 + 9488)) + load16u(arg3 + 112)) - 1))):
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
                        if not v6:
                            break
                        v15 = load32(9142840)
                    v6 = (v5 + 2)
                    v18 = load16u(arg2 + 110)
                    v19 = load32(ENTITIES)
                    while True:  # $label15
                        while True:  # $label13
                            v30 = (u32(v5) <= u32(v10))
                            if (u32(v5) <= u32(v10)):
                                break
                            if (u32(v5) <= u32(v7)):
                                break
                            if ((v7 | v10) < 0):
                                break
                            v11 = (v19 + (load32((((v7 + ((v6 + v9) * v6)) << 2) + v15) + 4) * 132))
                            if (load16u((v19 + (load32((((v7 + ((v6 + v9) * v6)) << 2) + v15) + 4) * 132)) + 110) != v18):
                                break
                            while True:  # $label14
                                # br_table load32(((load8u(v11 + 122) * 404) + ENTITY_TYPES) + 192)
                                break
                                break
                            if not load8u(v11 + 125):
                                break
                            break
                        while True:  # $label16
                            v16 = (v9 - 2)
                            v28 = (u32(v5) <= u32((v9 - 2)))
                            if (u32(v5) <= u32((v9 - 2))):
                                break
                            if (u32(v5) <= u32(v7)):
                                break
                            if ((v7 | v16) < 0):
                                break
                            v11 = (v19 + (load32((((v7 + ((v6 + v10) * v6)) << 2) + v15) + 4) * 132))
                            if (load16u((v19 + (load32((((v7 + ((v6 + v10) * v6)) << 2) + v15) + 4) * 132)) + 110) != v18):
                                break
                            while True:  # $label17
                                # br_table load32(((load8u(v11 + 122) * 404) + ENTITY_TYPES) + 192)
                                break
                                break
                            if not load8u(v11 + 125):
                                break
                            break
                        while True:  # $label18
                            if v28:
                                break
                            if (u32(v5) <= u32(v13)):
                                break
                            if ((v13 | v16) < 0):
                                break
                            v11 = (v19 + (load32((v15 + ((v7 + ((v6 + v10) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v7 + ((v6 + v10) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # $label19
                                # br_table load32(((load8u(v11 + 122) * 404) + ENTITY_TYPES) + 192)
                                break
                                break
                            if not load8u(v11 + 125):
                                break
                            break
                        v11 = (v7 - 2)
                        while True:  # $label20
                            if v28:
                                break
                            if (u32(v5) <= u32(v11)):
                                break
                            if ((v11 | v16) < 0):
                                break
                            v16 = (v19 + (load32((v15 + ((v13 + ((v6 + v10) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v13 + ((v6 + v10) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # $label21
                                # br_table load32(((load8u(v16 + 122) * 404) + ENTITY_TYPES) + 192)
                                break
                                break
                            if not load8u(v16 + 125):
                                break
                            break
                        while True:  # $label22
                            if v30:
                                break
                            if (u32(v5) <= u32(v11)):
                                break
                            if ((v10 | v11) < 0):
                                break
                            v16 = (v19 + (load32((v15 + ((v13 + ((v6 + v9) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v13 + ((v6 + v9) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # $label23
                                # br_table load32(((load8u(v16 + 122) * 404) + ENTITY_TYPES) + 192)
                                break
                                break
                            if not load8u(v16 + 125):
                                break
                            break
                        while True:  # $label24
                            v16 = (u32(v5) <= u32(v9))
                            if (u32(v5) <= u32(v9)):
                                break
                            if (u32(v5) <= u32(v11)):
                                break
                            if ((v9 | v11) < 0):
                                break
                            v11 = (v19 + (load32((v15 + ((v13 + (((v6 + v9) + 1) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v13 + (((v6 + v9) + 1) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # $label25
                                # br_table load32(((load8u(v11 + 122) * 404) + ENTITY_TYPES) + 192)
                                break
                                break
                            if not load8u(v11 + 125):
                                break
                            break
                        while True:  # $label26
                            if v16:
                                break
                            if (u32(v5) <= u32(v13)):
                                break
                            if ((v9 | v13) < 0):
                                break
                            v11 = (v19 + (load32((v15 + ((v7 + (((v6 + v9) + 1) * v6)) << 2))) * 132))
                            if (load16u((v19 + (load32((v15 + ((v7 + (((v6 + v9) + 1) * v6)) << 2))) * 132)) + 110) != v18):
                                break
                            while True:  # $label27
                                # br_table load32(((load8u(v11 + 122) * 404) + ENTITY_TYPES) + 192)
                                break
                                break
                            if not load8u(v11 + 125):
                                break
                            break
                        if v16:
                            break
                        if (u32(v5) <= u32(v7)):
                            break
                        if ((v7 | v9) < 0):
                            break
                        v6 = (v19 + (load32((((v7 + (((v6 + v9) + 1) * v6)) << 2) + v15) + 4) * 132))
                        if (load16u((v19 + (load32((((v7 + (((v6 + v9) + 1) * v6)) << 2) + v15) + 4) * 132)) + 110) != v18):
                            break
                        while True:  # $label28
                            # br_table load32(((load8u(v6 + 122) * 404) + ENTITY_TYPES) + 192)
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
                if (u32(v8) < u32(38)):
                    continue
                break
            break
        v6 = ((v25 * 404) + ENTITY_TYPES)
        v13 = (load32(((v25 * 404) + ENTITY_TYPES) + 220) + 2)
        v7 = (load32(v6 + 216) + 2)
        while True:  # $label30
            if not arg4:
                break
            arg3 = (v7 * v13)
            if not (v7 * v13):
                break
            # TODO: memory.fill
            break
        arg3 = 2147483647
        v28 = load32(v6 + 60)
        if load32(v6 + 60):
            v29 = ((v26 * 404) + 9568312)
            v30 = ((v25 * 404) + 9568152)
            v5 = 0
            while True:  # $label41
                while True:  # $label31
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
                    if (u32(load32(9142440)) <= u32(v18)):
                        break
                    if ((v18 | v19) < 0):
                        break
                    if (u32(v10) <= u32(v19)):
                        break
                    v10 = (v10 + 2)
                    v10 = load32((load32(9142840) + (((v9 + v12) + (((v8 + v14) + ((v10 + 2) * v21)) * v10)) << 2)))
                    if (v20 != load32((load32(9142840) + (((v9 + v12) + (((v8 + v14) + ((v10 + 2) * v21)) * v10)) << 2)))):
                        if (v10 == -1):
                            break
                        if (load8u(entities[v10].unit_class) != 1):
                            break
                    while True:  # $label32
                        if not arg4:
                            break
                        while True:  # $label33
                            if not v5:
                                break
                            v10 = (v9 + 1)
                            while True:  # $label34
                                v16 = (v9 < -1)
                                if (v9 < -1):
                                    break
                                if (v8 < 0):
                                    break
                                if (v7 <= v10):
                                    break
                                if (v8 >= v13):
                                    break
                                # br_table (load32(((((v7 * v8) + v10) << 2) + 8451904)) - 1)
                                break
                                break
                            v11 = (v8 - 1)
                            while True:  # $label35
                                v31 = (v9 < 0)
                                if (v9 < 0):
                                    break
                                if (v8 <= 0):
                                    break
                                if (v7 <= v9):
                                    break
                                if (v8 > v13):
                                    break
                                # br_table (load32(((((v7 * v11) + v9) << 2) + 8451904)) - 1)
                                break
                                break
                            v25 = (v9 - 1)
                            while True:  # $label36
                                v26 = (v9 <= 0)
                                if (v9 <= 0):
                                    break
                                if (v8 < 0):
                                    break
                                if (v7 < v9):
                                    break
                                if (v8 >= v13):
                                    break
                                # br_table (load32(((((v7 * v8) + v25) << 2) + 8451904)) - 1)
                                break
                                break
                            v15 = (v8 + 1)
                            while True:  # $label37
                                if v31:
                                    break
                                if (v8 < -1):
                                    break
                                if (v7 <= v9):
                                    break
                                if (v13 <= v15):
                                    break
                                # br_table (load32(((((v7 * v15) + v9) << 2) + 8451904)) - 1)
                                break
                                break
                            while True:  # $label38
                                if v16:
                                    break
                                if (v8 <= 0):
                                    break
                                if (v7 <= v10):
                                    break
                                if (v8 > v13):
                                    break
                                # br_table (load32(((((v7 * v11) + v10) << 2) + 8451904)) - 1)
                                break
                                break
                            while True:  # $label39
                                if v26:
                                    break
                                if (v8 <= 0):
                                    break
                                if (v7 < v9):
                                    break
                                if (v8 > v13):
                                    break
                                # br_table (load32(((((v7 * v11) + v25) << 2) + 8451904)) - 1)
                                break
                                break
                            while True:  # $label40
                                if v26:
                                    break
                                if (v8 < -1):
                                    break
                                if (v7 < v9):
                                    break
                                if (v13 <= v15):
                                    break
                                # br_table (load32(((((v7 * v15) + v25) << 2) + 8451904)) - 1)
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
                            # br_table (load32(((((v7 * v15) + v10) << 2) + 8451904)) - 1)
                            break
                            break
                        store32(v17 + 4, 0)
                        store8(v17 + 3, 0)
                        v8 = func177(load16u(arg2 + 112), load16u(arg2 + 114), v19, v18, v20, v21, (v17 + 12), (v17 + 8), load32(v29), (v17 + 4), (v17 + 3), 1)
                        store32(((((v7 * v8) + v9) << 2) + 8451904), (2 if func177(load16u(arg2 + 112), load16u(arg2 + 114), v19, v18, v20, v21, (v17 + 12), (v17 + 8), load32(v29), (v17 + 4), (v17 + 3), 1) else 1))
                        if not v8:
                            break
                        break
                    store32(arg0, v19)
                    store32(arg1, v18)
                    arg3 = v6
                    break
                v5 = (v5 + 2)
                if (u32((v5 + 2)) < u32(v28)):
                    continue
                break
        arg2 = (arg3 != 2147483647)
        break
    G.global0 = (v17 + 16)
    return arg2

# ----------------------------------------------------------
# $func236
# ----------------------------------------------------------
def func236(arg0, arg1):
    v3 = load32(9142440)
    v4 = (load32(9142440) + 2)
    v5 = load32(arg0 + 28)
    v6 = load32(ENTITIES)
    v7 = load32(9142840)
    v8 = load16u(arg1 + 114)
    v9 = load16u(arg1 + 112)
    v10 = load16u(arg1 + 110)
    v11 = load8u(arg1 + 122)
    arg0 = 0
    while True:  # $label1
        while True:  # $label2
            while True:  # $label0
                arg1 = arg0
                v2 = (arg0 << 2)
                arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v8)
                if (u32(v3) <= u32((load32((((arg0 << 2) | 4) + 8611904)) + v8))):
                    break
                v2 = (load32((v2 + 8611904)) + v9)
                if (u32(v3) <= u32((load32((v2 + 8611904)) + v9))):
                    break
                if ((arg0 | v2) < 0):
                    break
                arg0 = load32((((v2 + (((arg0 + v4) + 1) * v4)) << 2) + v7) + 4)
                if not load32((((v2 + (((arg0 + v4) + 1) * v4)) << 2) + v7) + 4):
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
            if (u32(arg1) < u32(878)):
                continue
            break
        arg0 = 0
        while True:  # $label4
            while True:  # $label3
                arg1 = arg0
                v2 = (arg0 << 2)
                arg0 = (load32((((arg0 << 2) | 4) + 8611904)) + v8)
                if (u32(v3) <= u32((load32((((arg0 << 2) | 4) + 8611904)) + v8))):
                    break
                v2 = (load32((v2 + 8611904)) + v9)
                if (u32(v3) <= u32((load32((v2 + 8611904)) + v9))):
                    break
                if ((arg0 | v2) < 0):
                    break
                arg0 = load32((((v2 + (((arg0 + v4) + 1) * v4)) << 2) + v7) + 4)
                if not load32((((v2 + (((arg0 + v4) + 1) * v4)) << 2) + v7) + 4):
                    break
                if (arg0 == v5):
                    break
                v2 = (v6 + (arg0 * 132))
                if (load16u((v6 + (arg0 * 132)) + 110) != v10):
                    break
                if not load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 264):
                    break
                break
            arg0 = (arg1 + 2)
            if (u32(arg1) < u32(878)):
                continue
            break
        arg0 = 0
        break
    return arg0

# ----------------------------------------------------------
# $func238
# ----------------------------------------------------------
def func238(arg0, arg1, arg2):
    v5 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label0
        v6 = load32(PLAYERS)
        v3 = players[arg1]
        v7 = ((players[arg1] + (arg0 << 2)) + 281808)
        if load32(((players[arg1] + (arg0 << 2)) + 281808)):
            break
        if (load32(v3 + 283908) == load32(CURRENT_PLAYER)):
            store32(v5 + 16, load32(39232))
            a_b()
        v4 = load32(((arg0 * 404) + ENTITY_TYPES) + 368)
        if (not arg2 & (load32(((arg0 * 404) + ENTITY_TYPES) + 368) == 55)):
            break
        v3 = (v3 + 283908)
        while True:  # $label1
            if v4:
                if (v4 == 55):
                    break
            store32(v7, 1)
            if (load32(v3) == load32(CURRENT_PLAYER)):
                store32(v5, (load32(load32(((arg0 * 404) + ENTITY_TYPES) + 180) + 8) * 48))
                a_b()
            if load8u(9142905):
                break
            # TODO: i32.div_u
            store32((load32(9142848) * 25), (((load32(((arg0 * 404) + ENTITY_TYPES) + 116) * load32(load32(GAME_STATE) + 132)) * 1000) - 100))
            break
        store32((((v6 + (arg1 * 286704)) + (arg0 << 2)) + 282828), 0)
        if (load32(v3) != load32(CURRENT_PLAYER)):
            break
        arg2 = ((arg0 * 404) + ENTITY_TYPES)
        if not load32(((arg0 * 404) + ENTITY_TYPES) + 244):
            break
        arg1 = 0
        while True:  # $label5
            v6 = load32((load32(arg2 + 240) + (arg1 << 2)))
            while True:  # $label2
                if load8u(9147141):
                    break
                arg0 = 0
                v3 = load32(9671120)
                if not load32(9671120):
                    break
                while True:  # $label4
                    while True:  # $label3
                        v4 = load32(((arg0 << 2) + 9263072))
                        if not load32(((arg0 << 2) + 9263072)):
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
            if (u32((arg1 + 1)) < u32(load32(arg2 + 244))):
                continue
            break
        break
    G.global0 = (v5 + 32)

# ----------------------------------------------------------
# $func239
# ----------------------------------------------------------
def func239(arg0):
    v2 = (arg0 * 286704)
    v1 = ((arg0 * 286704) + load32(PLAYERS))
    store32((((arg0 * 286704) + load32(PLAYERS)) + 281784), arg0)
    if not load32(9147132):
        arg0 = load32(PLAYER_COUNT)
        arg0 = (-1 if (u32((arg0 * 255)) > u32(1073741823)) else (load32(PLAYER_COUNT) * 1020))
        v3 = func26((-1 if (u32((arg0 * 255)) > u32(1073741823)) else (load32(PLAYER_COUNT) * 1020)))
        # TODO: memory.fill
        store32(v1 + 278556, v3)
        v1 = func26(arg0)
        # TODO: memory.fill
        store32(((load32(PLAYERS) + v2) + 278560), v1)
        v1 = func26(arg0)
        # TODO: memory.fill
        store32(((load32(PLAYERS) + v2) + 278564), v1)
        v1 = func26(arg0)
        # TODO: memory.fill
        store32(((load32(PLAYERS) + v2) + 278568), v1)
        arg0 = func26(16)
        store32(func26(16) + 4, 21000)
        store32(arg0, func26(84000))
        store64(arg0 + 8, 90194313216000)
        store32(((load32(PLAYERS) + v2) + 278572), arg0)

# ----------------------------------------------------------
# $func240
# ----------------------------------------------------------
def func240(arg0, arg1, arg2):
    v3 = load8u(arg0 + 122)
    v4 = load32(PLAYERS)
    v5 = load16u(arg0 + 110)
    func156(0, arg0, arg1)
    arg1 = ((v3 * 404) + ENTITY_TYPES)
    if (load32(((v3 * 404) + ENTITY_TYPES) + 264) == 4):
        store8(9671157, 1)
    if (load32(arg1 + 208) == 2):
        store8(9671158, 1)
    func144(((v5 * 286704) + v4), load32(arg0 + 28), arg2)
    while True:  # $label0
        if not load32(arg0 + 76):
            break
        if (load32(38528) == load8u(arg0 + 122)):
            break
        break
    while True:  # $label1
        if (load8u(arg0 + 126) != 2):
            break
        if (load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264) == 2):
            break
        break
    arg1 = load8u(arg0 + 122)
    if (load8u(arg0 + 122) == load32(38996)):
        arg1 = load8u(arg0 + 122)
    while True:  # $label3
        while True:  # $label2
            if (load32(38540) == arg1):
                break
            if (load32(38812) == arg1):
                break
            if (load32(38888) != arg1):
                break
            break
        while True:  # $label4
            # br_table (load8u(arg0 + 125) - 4)
            break
            break
        break

# ----------------------------------------------------------
# $func241
# ----------------------------------------------------------
def func241(arg0, arg1, arg2, arg3, arg4, arg5):
    v6 = (G.global0 + -64)
    store64((G.global0 + -64) + 48, 0)
    store64(v6 + 56, 0)
    store64(v6 + 32, 0)
    store64(v6 + 40, 0)
    while True:  # $label7
        while True:  # $label4
            while True:  # $label5
                while True:  # $label2
                    while True:  # $label3
                        if arg2:
                            if (u32(arg2) >= u32(4)):
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
                    if not load16u(v6 + 34):
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
                v13 = (v9 if (u32(v9) < u32(v11)) else v11)
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
            if (u32(load16u(v6 + 34)) > u32(2)):
                break
            v10 = load16u(v6 + 36)
            v12 = (load16u(v6 + 36) + (v14 << 1))
            if (u32((load16u(v6 + 36) + (v14 << 1))) > u32(4)):
                break
            v27 = load16u(v6 + 38)
            v12 = (load16u(v6 + 38) + (v12 << 1))
            if (u32((load16u(v6 + 38) + (v12 << 1))) > u32(8)):
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
            if (u32((v26 << 1)) < u32(v7)):
                break
            if ((v7 != v26) if (not arg0 | v15) else 0):
                break
            v15 = (u32(v9) < u32(v13))
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
            while True:  # $label8
                if not arg2:
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
                if not (arg2 & 1):
                    break
                arg2 = load16u((arg1 + (v8 << 1)))
                if not load16u((arg1 + (v8 << 1))):
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
            while True:  # $label10
                while True:  # $label12
                    while True:  # $label11
                        # br_table arg0
                        break
                        break
                    v8 = 1
                    if (u32(v10) > u32(9)):
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
                if (u32(v10) > u32(9)):
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
                while True:  # $label16
                    while True:  # $label17
                        v13 = (v9 - v16)
                        while True:  # $label13
                            v7 = load16u((arg5 + (v20 << 1)))
                            if (u32((load16u((arg5 + (v20 << 1))) + 1)) < u32(v21)):
                                break
                            if (u32(v7) < u32(v21)):
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
                        if not (v8 & 65535):
                            if (v9 == v11):
                                break
                            v9 = load16u((arg1 + (load16u((arg5 + (v20 << 1))) << 1)))
                        if (u32(v9) <= u32(v10)):
                            continue
                        arg2 = (v15 & v24)
                        if ((v15 & v24) == arg0):
                            continue
                        break
                    v16 = (v16 if v16 else v10)
                    v7 = (v9 - (v16 if v16 else v10))
                    v13 = (1 << (v9 - (v16 if v16 else v10)))
                    if (u32(v9) < u32(v11)):
                        arg0 = (v11 - v16)
                        v8 = v9
                        while True:  # $label18
                            while True:  # $label19
                                v8 = (v13 - load16u(((v6 + 32) + (v8 << 1))))
                                if ((v13 - load16u(((v6 + 32) + (v8 << 1)))) <= 0):
                                    break
                                v13 = (v8 << 1)
                                v7 = (v7 + 1)
                                v8 = ((v7 + 1) + v16)
                                if (u32(((v7 + 1) + v16)) < u32(v11)):
                                    continue
                                break
                            v7 = arg0
                            break
                        v13 = (1 << v7)
                    v8 = 1
                    v18 = (v13 + v18)
                    if (v17 & (u32((v13 + v18)) > u32(852))):
                        break
                    if (v22 & (u32(v18) > u32(592))):
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

# ----------------------------------------------------------
# $func242
# ----------------------------------------------------------
def func242(arg0):
    v2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label2
        while True:  # $label1
            while True:  # $label0
                v1 = load8u(entities[load32(9173808)].sub_state)
                if (load8u(entities[load32(9173808)].sub_state) == load32(38540)):
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
                v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                if arg0:
                    # TODO: memory.copy
                break
            if v1:
                func41(8, 9173808, arg0, (v2 + 4), 1)
                break
            v3 = (arg0 << 2)
            v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
            if arg0:
                # TODO: memory.copy
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
        v1 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
        if arg0:
            # TODO: memory.copy
        break
    G.global0 = (v2 + 16)

# ----------------------------------------------------------
# $func243
# ----------------------------------------------------------
def func243(arg0, arg1, arg2):
    v6 = (load32(PLAYER_COUNT) * arg2)
    v19 = load32(9142440)
    v10 = (load32(9142440) + 2)
    v21 = ((load32(9142440) + 2) << 1)
    v12 = load32(38564)
    v13 = load32(38620)
    v14 = load32(38560)
    v7 = load32(9143004)
    v15 = load32(38500)
    v16 = load32(ENTITIES)
    v17 = load32(9142840)
    arg2 = 0
    while True:  # $label2
        while True:  # $label7
            while True:  # $label0
                v20 = arg2
                v3 = (arg2 << 2)
                arg2 = (load32((((arg2 << 2) | 4) + 8611904)) + arg1)
                if (u32(v19) <= u32((load32((((arg2 << 2) | 4) + 8611904)) + arg1))):
                    break
                v3 = (load32((v3 + 8611904)) + arg0)
                if (u32(v19) <= u32((load32((v3 + 8611904)) + arg0))):
                    break
                if ((arg2 | v3) < 0):
                    break
                while True:  # $label1
                    v8 = (v3 + 1)
                    v11 = (arg2 + 1)
                    arg2 = load32((v17 + (((v3 + 1) + ((arg2 + 1) * v10)) << 2)))
                    if (u32(load32((v17 + (((v3 + 1) + ((arg2 + 1) * v10)) << 2)))) < u32(3)):
                        break
                    v3 = (v16 + (arg2 * 132))
                    if (u32(load32((v16 + (arg2 * 132)) + 64)) >= u32(load32(v3 + 68))):
                        break
                    v4 = load8u(v3 + 122)
                    v9 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                    if not load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 300):
                        break
                    if (v4 == v15):
                        break
                    v5 = load16u(v3 + 110)
                    while True:  # $label3
                        v18 = load16u(v3 + 120)
                        if load16u(v3 + 120):
                        else:
                        if not load8u(((v18 if load8u((v7 + (v5 + v6))) else v5) + (v5 + v6))):
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
                while True:  # $label4
                    arg2 = load32((v17 + ((v8 + ((v10 + v11) * v10)) << 2)))
                    if (u32(load32((v17 + ((v8 + ((v10 + v11) * v10)) << 2)))) < u32(3)):
                        break
                    v3 = (v16 + (arg2 * 132))
                    if (u32(load32((v16 + (arg2 * 132)) + 64)) >= u32(load32(v3 + 68))):
                        break
                    v4 = load8u(v3 + 122)
                    v9 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                    if not load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 300):
                        break
                    if (v4 == v15):
                        break
                    v5 = load16u(v3 + 110)
                    while True:  # $label5
                        v18 = load16u(v3 + 120)
                        if load16u(v3 + 120):
                        else:
                        if load8u(((v18 if load8u((v7 + (v5 + v6))) else v5) + (v5 + v6))):
                            if not load8u(v3 + 128):
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
                if (u32(load32((v17 + ((v8 + ((v11 + v21) * v10)) << 2)))) < u32(3)):
                    break
                v3 = (v16 + (arg2 * 132))
                if (u32(load32((v16 + (arg2 * 132)) + 64)) >= u32(load32(v3 + 68))):
                    break
                v5 = load8u(v3 + 122)
                v8 = ((load8u(v3 + 122) * 404) + ENTITY_TYPES)
                if not load32(((load8u(v3 + 122) * 404) + ENTITY_TYPES) + 300):
                    break
                if (v5 == v15):
                    break
                v4 = load16u(v3 + 110)
                while True:  # $label6
                    v11 = load16u(v3 + 120)
                    if load16u(v3 + 120):
                    else:
                    if load8u(((v11 if load8u((v7 + (v4 + v6))) else v4) + (v4 + v6))):
                        if not load8u(v3 + 128):
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
            if (u32(v20) < u32(1678)):
                continue
            break
        arg2 = 0
        break
    return arg2

# ----------------------------------------------------------
# $func244
# ----------------------------------------------------------
def func244(arg0):
    v2 = (G.global0 - 32)
    G.global0 = (G.global0 - 32)
    while True:  # $label2
        while True:  # $label0
            if not load8u(9142916):
                break
            arg0 = load32(arg0 + 32)
            if ((load32(arg0 + 32) != 27) & (arg0 != 6)):
                break
            while True:  # $label1
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
                if (u32(arg0) < u32(load32(9163788))):
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
        if (u32(arg0) < u32(load32(9163784))):
            break
        store32(v2, v3)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    G.global0 = (v2 + 32)
    return v1

# ----------------------------------------------------------
# $func245
# ----------------------------------------------------------
def func245():
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label0
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
        if (u32(v2) < u32(load32(9163784))):
            break
        store32(v1, v3)
        a_b()
        store32(9163784, (load32(9163784) + 40000))
        break
    G.global0 = (v1 + 16)
    return v0

# ----------------------------------------------------------
# $func246
# ----------------------------------------------------------
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

# ----------------------------------------------------------
# $func247
# ----------------------------------------------------------
def func247(arg0, arg1):
    v6 = (G.global0 + -64)
    G.global0 = (G.global0 + -64)
    while True:  # $label0
        if (load8u(arg1 + 125) == 3):
            break
        v9 = load32(arg0 + 16)
        while True:  # $label5
            while True:  # $label6
                while True:  # $label4
                    while True:  # $label3
                        while True:  # $label2
                            while True:  # $label1
                                # br_table load32(arg0 + 8)
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
                    if not load32(arg0 + 104):
                        break
                    v11 = load32(arg0 + 96)
                    v12 = load16u(arg1 + 114)
                    v13 = load16u(arg1 + 112)
                    v14 = load32(ENTITIES)
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
                if not load32(9140300):
                    break
                v11 = load16u(arg1 + 114)
                v12 = load16u(arg1 + 112)
                v13 = load32(ENTITIES)
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
            if not v7:
                break
            break
        while True:  # $label18
            while True:  # $label10
                while True:  # $label17
                    while True:  # $label16
                        while True:  # $label15
                            while True:  # $label14
                                while True:  # $label13
                                    while True:  # $label12
                                        while True:  # $label11
                                            while True:  # $label9
                                                # br_table v9
                                                break
                                                break
                                            if not v7:
                                                v7 = 0
                                                break
                                            store32(v6 + 32, load32(arg1 + 28))
                                            v5 = func161(entities[v7], (v6 + 32), 1)
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
                        arg0 = entities[v7]
                        v2 = ((load8u(entities[v7].sub_state) * 404) + ENTITY_TYPES)
                        v3 = (((load32(((load8u(entities[v7].sub_state) * 404) + ENTITY_TYPES) + 220) & 0xFFFFFFFF) >> 1) + load16u(arg0 + 114))
                        v2 = (load16u(arg0 + 112) + ((load32(v2 + 216) & 0xFFFFFFFF) >> 1))
                    store64(v6 + 52, 0)
                    store64(v6 + 44, 0)
                    store32(v6 + 40, -1)
                    store32(v6 + 36, v3)
                    store32(v6 + 32, v2)
                    store32(v6 + 28, load32(arg1 + 28))
                    break
                    break
                while True:  # $label19
                    if (v9 != 8):
                        break
                    if not v7:
                        break
                    while True:  # $label22
                        while True:  # $label21
                            while True:  # $label20
                                v2 = load32(arg1 + 20)
                                if not load32(arg1 + 20):
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
                                if not load32(v2 + 4):
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
                        v4 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                        arg0 = v2
                        if v9:
                            v3 = load32(v2 + 8)
                            arg0 = load32(arg1 + 20)
                        store32(v2, v4)
                        break
                    store32(v5, (v3 + 1))
                    store32((v4 + (v3 << 2)), 1)
                    while True:  # $label23
                        v3 = load32(arg0 + 8)
                        if (load32(arg0 + 8) != load32(arg0 + 4)):
                            v4 = load32(arg0)
                            v2 = arg0
                            break
                        v2 = (load32(arg0 + 12) + v3)
                        store32(arg0 + 4, (load32(arg0 + 12) + v3))
                        v5 = load32(arg0)
                        v4 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                        if v3:
                            # TODO: memory.copy
                        v2 = arg0
                        if v5:
                            v3 = load32(arg0 + 8)
                            v2 = load32(arg1 + 20)
                        store32(arg0, v4)
                        break
                    store32(arg0 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 2)
                    while True:  # $label24
                        v3 = load32(v2 + 8)
                        if (load32(v2 + 8) != load32(v2 + 4)):
                            v4 = load32(v2)
                            arg0 = v2
                            break
                        arg0 = (load32(v2 + 12) + v3)
                        store32(v2 + 4, (load32(v2 + 12) + v3))
                        v5 = load32(v2)
                        v4 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                        if v3:
                            # TODO: memory.copy
                        arg0 = v2
                        if v5:
                            v3 = load32(v2 + 8)
                            arg0 = load32(arg1 + 20)
                        store32(v2, v4)
                        break
                    store32(v2 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 0)
                    while True:  # $label25
                        v3 = load32(arg0 + 8)
                        if (load32(arg0 + 8) != load32(arg0 + 4)):
                            v4 = load32(arg0)
                            v2 = arg0
                            break
                        v2 = (load32(arg0 + 12) + v3)
                        store32(arg0 + 4, (load32(arg0 + 12) + v3))
                        v5 = load32(arg0)
                        v4 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                        if v3:
                            # TODO: memory.copy
                        v2 = arg0
                        if v5:
                            v3 = load32(arg0 + 8)
                            v2 = load32(arg1 + 20)
                        store32(arg0, v4)
                        break
                    store32(arg0 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 0)
                    while True:  # $label26
                        v3 = load32(v2 + 8)
                        if (load32(v2 + 8) != load32(v2 + 4)):
                            v4 = load32(v2)
                            arg0 = v2
                            break
                        arg0 = (load32(v2 + 12) + v3)
                        store32(v2 + 4, (load32(v2 + 12) + v3))
                        v5 = load32(v2)
                        v4 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                        if v3:
                            # TODO: memory.copy
                        arg0 = v2
                        if v5:
                            v3 = load32(v2 + 8)
                            arg0 = load32(arg1 + 20)
                        store32(v2, v4)
                        break
                    store32(v2 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), v7)
                    while True:  # $label27
                        v3 = load32(arg0 + 8)
                        if (load32(arg0 + 8) != load32(arg0 + 4)):
                            v4 = load32(arg0)
                            v2 = arg0
                            break
                        v2 = (load32(arg0 + 12) + v3)
                        store32(arg0 + 4, (load32(arg0 + 12) + v3))
                        v5 = load32(arg0)
                        v4 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                        if v3:
                            # TODO: memory.copy
                        v2 = arg0
                        if v5:
                            v3 = load32(arg0 + 8)
                            v2 = load32(arg1 + 20)
                        store32(arg0, v4)
                        break
                    store32(arg0 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 0)
                    while True:  # $label28
                        v3 = load32(v2 + 8)
                        if (load32(v2 + 8) != load32(v2 + 4)):
                            v4 = load32(v2)
                            arg0 = v2
                            break
                        arg0 = (load32(v2 + 12) + v3)
                        store32(v2 + 4, (load32(v2 + 12) + v3))
                        v5 = load32(v2)
                        v4 = func26((-1 if (u32(arg0) > u32(1073741823)) else (arg0 << 2)))
                        if v3:
                            # TODO: memory.copy
                        arg0 = v2
                        if v5:
                            v3 = load32(v2 + 8)
                            arg0 = load32(arg1 + 20)
                        store32(v2, v4)
                        break
                    store32(v2 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 0)
                    while True:  # $label29
                        v3 = load32(arg0 + 8)
                        if (load32(arg0 + 8) != load32(arg0 + 4)):
                            v4 = load32(arg0)
                            v2 = arg0
                            break
                        v2 = (load32(arg0 + 12) + v3)
                        store32(arg0 + 4, (load32(arg0 + 12) + v3))
                        v5 = load32(arg0)
                        v4 = func26((-1 if (u32(v2) > u32(1073741823)) else (v2 << 2)))
                        if v3:
                            # TODO: memory.copy
                        v2 = arg0
                        if v5:
                            v3 = load32(arg0 + 8)
                            v2 = load32(arg1 + 20)
                        store32(arg0, v4)
                        break
                    store32(arg0 + 8, (v3 + 1))
                    store32((v4 + (v3 << 2)), 5)
                    while True:  # $label30
                        arg0 = load32(v2 + 8)
                        if (load32(v2 + 8) != load32(v2 + 4)):
                            v3 = load32(v2)
                            break
                        v3 = (load32(v2 + 12) + arg0)
                        store32(v2 + 4, (load32(v2 + 12) + arg0))
                        v4 = load32(v2)
                        v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                        if arg0:
                            # TODO: memory.copy
                        if v4:
                            arg0 = load32(v2 + 8)
                        store32(v2, v3)
                        break
                    store32(v2 + 8, (arg0 + 1))
                    store32((v3 + (arg0 << 2)), 0)
                    break
                    break
                arg0 = (v9 - 9)
                if (u32((v9 - 9)) > u32(21)):
                    break
                v5 = load32(((arg0 << 2) + 10196))
                break
            if not v7:
                break
            if not load8u(((v5 * 40) + 9671200) + 16):
                break
            arg0 = (v7 * 132)
            v7 = 0
            arg0 = (arg0 + load32(ENTITIES))
            v2 = ((load8u((arg0 + load32(ENTITIES)) + 122) * 404) + ENTITY_TYPES)
            v3 = (((load32(((load8u((arg0 + load32(ENTITIES)) + 122) * 404) + ENTITY_TYPES) + 220) & 0xFFFFFFFF) >> 1) + load16u(arg0 + 114))
            v2 = (load16u(arg0 + 112) + ((load32(v2 + 216) & 0xFFFFFFFF) >> 1))
            break
        break
    G.global0 = (v6 - -64)

# ----------------------------------------------------------
# $func248
# ----------------------------------------------------------
def func248(arg0, param1):
    v1 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    store32(arg0 + 32, 1)
    v2 = (arg0 + 4)
    if (load32(arg0 + 44) != load32(arg0 + 48)):
        while True:  # $label0
            func392((v1 + 4), arg0)
            func54(v2)
            if (load32(arg0 + 44) != load32(arg0 + 48)):
                continue
            break
    func54(v2)
    store32(arg0 + 32, 0)
    G.global0 = (v1 + 16)

# ----------------------------------------------------------
# $func249
# ----------------------------------------------------------
def func249(arg0):
    v1 = (G.global0 - 144)
    G.global0 = (G.global0 - 144)
    # TODO: memory.fill
    store32(v1 + 52, 5522759)
    store32(v1 + 92, 56)
    store32(v1 + 88, 57)
    store32(v1 + 104, (1 if load8u(59184) else (5 if load8u(59185) else 1)))
    v2 = (v1 + 12)
    while True:  # $label3
        arg0 = load8u(9681935)
        v3 = (i32(load8u(9681935)) < 0)
        v5 = (load32(9681924) if (i32(load8u(9681935)) < 0) else 9681924)
        arg0 = (load32(9681928) if v3 else arg0)
        v6 = (G.global0 - 16)
        G.global0 = (G.global0 - 16)
        while True:  # $label0
            if ((load8u(v2 + 11) & 0xFFFFFFFF) >> 7):
                break
            break
        v3 = (load8u(v2 + 11) & 127)
        if (u32((load8u(v2 + 11) & 127)) >= u32(0)):
            while True:  # $label1
                if ((load8u(v2 + 11) & 0xFFFFFFFF) >> 7):
                else:
                v4 = 10
                if (u32(((load32(v2 + 8) & 2147483647) - 1)) <= u32((10 - v3))):
                    if not arg0:
                        break
                    while True:  # $label2
                        if ((load8u(v2 + 11) & 0xFFFFFFFF) >> 7):
                            break
                        break
                    v4 = v2
                    if v3:
                        # TODO: memory.copy
                    else:
                    # TODO: memory.copy
                    arg0 = (arg0 + v3)
                    func312(v2, (arg0 + v3))
                    store8(v6 + 15, 0)
                    store8((arg0 + v4), load8u(v6 + 15))
                    break
                break
            G.global0 = (v6 + 16)
            break
        a_g()
        raise Unreachable()
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

# ----------------------------------------------------------
# $func250
# ----------------------------------------------------------
def func250(arg0, arg1, arg2):
    v13 = load32(9142440)
    v5 = (load32(9142440) + 2)
    v20 = load32(38564)
    v14 = load32(ENTITIES)
    v9 = load32(9142840)
    while True:  # $label10
        while True:  # $label0
            v15 = v3
            v3 = (v3 << 2)
            v7 = (load32((((v3 << 2) | 4) + 8611904)) + arg1)
            if (u32(v13) <= u32((load32((((v3 << 2) | 4) + 8611904)) + arg1))):
                break
            v8 = (load32((v3 + 8611904)) + arg0)
            if (u32(v13) <= u32((load32((v3 + 8611904)) + arg0))):
                break
            if ((v7 | v8) < 0):
                break
            v16 = (v7 + 1)
            v21 = load32((((v8 + (((v7 + 1) + v5) * v5)) << 2) + v9) + 4)
            v3 = (v14 + (load32((((v8 + (((v7 + 1) + v5) * v5)) << 2) + v9) + 4) * 132))
            if (v20 != load8u((v14 + (load32((((v8 + (((v7 + 1) + v5) * v5)) << 2) + v9) + 4) * 132)) + 122)):
                break
            while True:  # $label1
                # br_table (load8u(v3 + 125) - 4)
                break
                break
            v10 = (v8 + 2)
            v17 = (v8 if (v8 > v10) else (v8 + 2))
            v11 = 1
            v18 = (v7 - 1)
            v4 = (v8 - 1)
            v19 = ((v5 + v7) * v5)
            while True:  # $label2
                v3 = (v7 + 2)
                v12 = (v7 if (v3 < v7) else (v7 + 2))
                if ((v16 == (v7 if (v3 < v7) else (v7 + 2))) | (v7 > 2147483645)):
                    while True:  # $label5
                        v6 = (v4 + 1)
                        v3 = v18
                        while True:  # $label4
                            if (v4 != v8):
                                while True:  # $label3
                                    v3 = (v3 + 1)
                                    v4 = load32((v9 + (((((v3 + 1) + v5) * v5) + v6) << 2)))
                                    if not load32((v9 + (((((v3 + 1) + v5) * v5) + v6) << 2))):
                                        break
                                    if (arg2 == v4):
                                        break
                                    if (v3 != v12):
                                        continue
                                    break
                                    break
                                raise Unreachable()
                            v3 = load32((v9 + ((v6 + v19) << 2)))
                            if not load32((v9 + ((v6 + v19) << 2))):
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
                    raise Unreachable()
                while True:  # $label9
                    v6 = (v4 + 1)
                    v3 = v18
                    while True:  # $label7
                        if (v4 == v8):
                            v4 = load32((v9 + ((v6 + v19) << 2)))
                            if not load32((v9 + ((v6 + v19) << 2))):
                                break
                            v3 = v16
                            if (arg2 == v4):
                                break
                            while True:  # $label6
                                v4 = (v3 + 1)
                                if (v3 != v7):
                                    v3 = load32((v9 + ((((v4 + v5) * v5) + v6) << 2)))
                                    if not load32((v9 + ((((v4 + v5) * v5) + v6) << 2))):
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
                            if not load32((v9 + (((((v3 + 1) + v5) * v5) + v6) << 2))):
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
            if not v11:
                break
            return load32((v14 + (v21 * 132)) + 28)
            break
        v3 = (v15 + 2)
        if (u32(v15) < u32(878)):
            continue
        break
    return 0

# ----------------------------------------------------------
# $func252
# ----------------------------------------------------------
def func252(arg0, arg1):
    while True:  # $label1
        while True:  # $label0
            if not arg0:
                break
            v3 = (i32(arg0) * i32(arg1))
            v2 = i32((i32(arg0) * i32(arg1)))
            if (u32((arg0 | arg1)) < u32(65536)):
                break
            break
        v2 = (-1 if i32(((v3 & 0xFFFFFFFF) >> 32)) else v2)
        arg0 = e()
        if not e():
            break
        if not (load8u((arg0 - 4)) & 3):
            break
        func98(arg0, 0, v2)
        break
    return arg0

# ----------------------------------------------------------
# $func254
# ----------------------------------------------------------
def func254(arg0, arg1):
    while True:  # $label0
        if not arg0:
            break
        v3 = load32(arg0 + 16)
        arg0 = load32(arg0 + 24)
        if (load32(arg0 + 24) >= 100):
            v4 = loadf32((((arg0 + v3) << 2) + 32700))
            if not ((loadf32((((arg0 + v3) << 2) + 32700)) < 4294967300.0) & (v4 >= 0.0)):
                break
            v2 = i32(v4)
            break
        v2 = ((v3 * 1000) // arg0)
        break

# ----------------------------------------------------------
# $func255
# ----------------------------------------------------------
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
            while True:  # $label0
                v2 = load32(arg0 + 56)
                if (load32(arg0 + 56) != load32(arg0 + 52)):
                    v3 = load32(arg0 + 48)
                    break
                v3 = (load32(arg0 + 60) + v2)
                store32(arg0 + 52, (load32(arg0 + 60) + v2))
                v5 = load32(arg0 + 48)
                v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                if v2:
                    # TODO: memory.copy
                if v5:
                    v2 = load32(arg0 + 56)
                store32(arg0 + 48, v3)
                break
            store32(arg0 + 56, (v2 + 1))
            store32((v3 + (v2 << 2)), v6)
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(load32(arg1 + 56))):
                continue
            break
    if load32(arg1 + 72):
        v4 = 0
        while True:  # $label3
            v6 = load32((load32(arg1 + 64) + (v4 << 2)))
            while True:  # $label2
                v2 = load32(arg0 + 72)
                if (load32(arg0 + 72) != load32(arg0 + 68)):
                    v3 = load32(arg0 + 64)
                    break
                v3 = (load32(arg0 + 76) + v2)
                store32(arg0 + 68, (load32(arg0 + 76) + v2))
                v5 = load32(arg0 + 64)
                v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                if v2:
                    # TODO: memory.copy
                if v5:
                    v2 = load32(arg0 + 72)
                store32(arg0 + 64, v3)
                break
            store32(arg0 + 72, (v2 + 1))
            store32((v3 + (v2 << 2)), v6)
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(load32(arg1 + 72))):
                continue
            break
    if load32(arg1 + 88):
        v4 = 0
        while True:  # $label5
            v6 = load32((load32(arg1 + 80) + (v4 << 2)))
            while True:  # $label4
                v2 = load32(arg0 + 88)
                if (load32(arg0 + 88) != load32(arg0 + 84)):
                    v3 = load32(arg0 + 80)
                    break
                v3 = (load32(arg0 + 92) + v2)
                store32(arg0 + 84, (load32(arg0 + 92) + v2))
                v5 = load32(arg0 + 80)
                v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                if v2:
                    # TODO: memory.copy
                if v5:
                    v2 = load32(arg0 + 88)
                store32(arg0 + 80, v3)
                break
            store32(arg0 + 88, (v2 + 1))
            store32((v3 + (v2 << 2)), v6)
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(load32(arg1 + 88))):
                continue
            break
    if load32(arg1 + 104):
        v4 = 0
        while True:  # $label7
            v6 = load32((load32(arg1 + 96) + (v4 << 2)))
            while True:  # $label6
                v2 = load32(arg0 + 104)
                if (load32(arg0 + 104) != load32(arg0 + 100)):
                    v3 = load32(arg0 + 96)
                    break
                v3 = (load32(arg0 + 108) + v2)
                store32(arg0 + 100, (load32(arg0 + 108) + v2))
                v5 = load32(arg0 + 96)
                v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
                if v2:
                    # TODO: memory.copy
                if v5:
                    v2 = load32(arg0 + 104)
                store32(arg0 + 96, v3)
                break
            store32(arg0 + 104, (v2 + 1))
            store32((v3 + (v2 << 2)), v6)
            v4 = (v4 + 1)
            if (u32((v4 + 1)) < u32(load32(arg1 + 104))):
                continue
            break
    while True:  # $label8
        v3 = load32(arg1 + 192)
        if not load32(arg1 + 192):
            break
        v2 = 0
        if (u32(v3) >= u32(4)):
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
        if not (v3 & 3):
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

# ----------------------------------------------------------
# $func256
# ----------------------------------------------------------
def func256(arg0, arg1):
    v2 = load32(arg0 + 24)
    if not load32(arg0 + 24):
        v2 = func26(16)
        store64(func26(16), 0)
        store64(v2 + 8, 0)
        store32(arg0 + 24, v2)
    while True:  # $label1
        while True:  # $label0
            arg0 = load32(v2 + 8)
            if not load32(v2 + 8):
                arg0 = func26(16)
                store32(func26(16) + 4, arg1)
                v3 = func26((-1 if (u32(arg1) > u32(1073741823)) else (arg1 << 2)))
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
            if (u32(load32(arg0 + 4)) > u32(arg1)):
                break
            break
        v3 = (load32(arg0 + 12) + (arg1 + v3))
        store32(arg0 + 4, (load32(arg0 + 12) + (arg1 + v3)))
        v4 = load32(arg0)
        v3 = func26((-1 if (u32(v3) > u32(1073741823)) else (v3 << 2)))
        if v4:
        store32(arg0, v3)
        break
    while True:  # $label2
        if not arg1:
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
        if not v4:
            break
        arg0 = load32(((arg0 << 2) + 9147392))
        arg1 = load32(v2)
        store32(v2, (load32(v2) + 1))
        store32((v3 + (arg1 << 2)), arg0)
        break

# ----------------------------------------------------------
# $func257
# ----------------------------------------------------------
def func257(arg0, arg1):
    while True:  # $label0
        v3 = load32(9142840)
        arg0 = (arg0 + 1)
        v4 = (arg1 + 1)
        arg1 = (load32(9142440) + 2)
        v2 = load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))
        if (u32(load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))) < u32(3)):
            break
        v2 = entities[v2]
        if load32(entities[v2].target_id):
            break
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # $label1
        v2 = load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))
        if (u32(load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))) < u32(3)):
            break
        v2 = entities[v2]
        if load32(entities[v2].target_id):
            break
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # $label2
        arg0 = load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))
        if (u32(load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))) < u32(3)):
            break
        arg0 = entities[arg0]
        if load32(entities[arg0].target_id):
            break
        break

# ----------------------------------------------------------
# $func258
# ----------------------------------------------------------
def func258(arg0, arg1):
    while True:  # $label0
        v3 = load32(9142840)
        arg0 = (arg0 + 1)
        v4 = (arg1 + 1)
        arg1 = (load32(9142440) + 2)
        v2 = load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))
        if (u32(load32((load32(9142840) + (((arg0 + 1) + ((arg1 + 1) * (load32(9142440) + 2))) << 2)))) < u32(3)):
            break
        v2 = entities[v2]
        if load32(entities[v2].target_id):
            break
        if not load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 264):
            break
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # $label1
        v2 = load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))
        if (u32(load32((v3 + ((arg0 + ((arg1 + v4) * arg1)) << 2)))) < u32(3)):
            break
        v2 = entities[v2]
        if load32(entities[v2].target_id):
            break
        if not load32(((load8u(v2 + 122) * 404) + ENTITY_TYPES) + 264):
            break
        arg1 = (load32(9142440) + 2)
        v3 = load32(9142840)
        break
    while True:  # $label2
        arg0 = load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))
        if (u32(load32((v3 + ((arg0 + ((v4 + (arg1 << 1)) * arg1)) << 2)))) < u32(3)):
            break
        arg0 = entities[arg0]
        if load32(entities[arg0].target_id):
            break
        if not load32(((load8u(arg0 + 122) * 404) + ENTITY_TYPES) + 264):
            break
        break

# ----------------------------------------------------------
# $func259
# ----------------------------------------------------------
def func259(arg0, arg1):
    v2 = (G.global0 - 128)
    G.global0 = (G.global0 - 128)
    while True:  # $label1
        v4 = ((load32((arg0 + (v7 << 2))) * 404) + ENTITY_TYPES)
        v3 = load32(((load32((arg0 + (v7 << 2))) * 404) + ENTITY_TYPES) + 84)
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
                    v3 = ((load32(v6 + 4) * 404) + ENTITY_TYPES)
                    v8 = load32(((load32(v6 + 4) * 404) + ENTITY_TYPES) + 84)
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
                if (u32((v5 + 1)) < u32(v3)):
                    continue
                break
        v7 = (v7 + 1)
        if ((v7 + 1) != 15):
            continue
        break
    G.global0 = (v2 + 128)

# ----------------------------------------------------------
# $func260
# ----------------------------------------------------------
def func260(arg0, arg1):
    v10 = (G.global0 - 32)
    v9 = load32(arg1)
    v2 = load32(arg1 + 8)
    v4 = load32(load32(arg1 + 8))
    v8 = load32(v2 + 12)
    store64(arg0 + 5200, 2461016260608)
    v14 = -1
    v2 = 0
    while True:  # $label2
        if (v8 > 0):
            while True:  # $label1
                while True:  # $label0
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
        while True:  # $label4
            v3 = (v2 << 1)
            v5 = load32(arg0 + 5200)
            if ((v2 << 1) > load32(arg0 + 5200)):
                break
            v11 = ((arg0 + v6) + 5208)
            v12 = (v9 + (v6 << 2))
            v4 = v7
            while True:  # $label7
                while True:  # $label5
                    if (v3 >= v5):
                        v2 = v3
                        break
                    v2 = (arg0 + 2908)
                    v5 = (v3 | 1)
                    v13 = load32(((arg0 + 2908) + ((v3 | 1) << 2)))
                    v15 = load16u((v9 + (load32(((arg0 + 2908) + ((v3 | 1) << 2))) << 2)))
                    v16 = load32((v2 + (v3 << 2)))
                    v2 = load16u((v9 + (load32((v2 + (v3 << 2))) << 2)))
                    if (u32(load16u((v9 + (load32(((arg0 + 2908) + ((v3 | 1) << 2))) << 2)))) >= u32(load16u((v9 + (load32((v2 + (v3 << 2))) << 2))))):
                        if (v2 != v15):
                            v2 = v3
                            break
                        v2 = v3
                        v3 = (arg0 + 5208)
                        if (u32(load8u(((arg0 + 5208) + v13))) > u32(load8u((v3 + v16)))):
                            break
                    v2 = v5
                    break
                v5 = load16u(v12)
                v3 = load32(((arg0 + (v2 << 2)) + 2908))
                v13 = load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2)))
                if (u32(load16u(v12)) < u32(load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2))))):
                    v2 = v4
                    break
                while True:  # $label6
                    if (v5 != v13):
                        break
                    if (u32(load8u(v11)) > u32(load8u(((arg0 + v3) + 5208)))):
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
        while True:  # $label9
            if (v3 < 3):
                break
            v6 = ((arg0 + v11) + 5208)
            v3 = 2
            v13 = (v9 + (v11 << 2))
            v4 = 1
            while True:  # $label12
                while True:  # $label10
                    if (v3 >= v5):
                        v2 = v3
                        break
                    v2 = (arg0 + 2908)
                    v8 = (v3 | 1)
                    v5 = load32(((arg0 + 2908) + ((v3 | 1) << 2)))
                    v15 = load16u((v9 + (load32(((arg0 + 2908) + ((v3 | 1) << 2))) << 2)))
                    v16 = load32((v2 + (v3 << 2)))
                    v2 = load16u((v9 + (load32((v2 + (v3 << 2))) << 2)))
                    if (u32(load16u((v9 + (load32(((arg0 + 2908) + ((v3 | 1) << 2))) << 2)))) >= u32(load16u((v9 + (load32((v2 + (v3 << 2))) << 2))))):
                        if (v2 != v15):
                            v2 = v3
                            break
                        v2 = v3
                        v3 = (arg0 + 5208)
                        if (u32(load8u(((arg0 + 5208) + v5))) > u32(load8u((v3 + v16)))):
                            break
                    v2 = v8
                    break
                v8 = load16u(v13)
                v3 = load32(((arg0 + (v2 << 2)) + 2908))
                v5 = load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2)))
                if (u32(load16u(v13)) < u32(load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2))))):
                    v2 = v4
                    break
                while True:  # $label11
                    if (v5 != v8):
                        break
                    if (u32(load8u(v6)) > u32(load8u(((arg0 + v3) + 5208)))):
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
        store8(((arg0 + 5208) + v7), ((load8u((v11 + v12)) if (u32(v2) < u32(v5)) else load8u((v2 + v11))) + 1))
        store16(v4 + 2, v7)
        store16(v8 + 2, v7)
        store32(arg0 + 2912, v7)
        v4 = 1
        v2 = 1
        while True:  # $label13
            v5 = load32(arg0 + 5200)
            if (load32(arg0 + 5200) < 2):
                break
            while True:  # $label16
                while True:  # $label14
                    if (v3 >= v5):
                        break
                    v8 = (v3 | 1)
                    v5 = load32((v6 + ((v3 | 1) << 2)))
                    v2 = load16u((v9 + (load32((v6 + ((v3 | 1) << 2))) << 2)))
                    v12 = load32((v6 + (v3 << 2)))
                    v16 = load16u((v9 + (load32((v6 + (v3 << 2))) << 2)))
                    if (u32(load16u((v9 + (load32((v6 + ((v3 | 1) << 2))) << 2)))) >= u32(load16u((v9 + (load32((v6 + (v3 << 2))) << 2))))):
                        if (v2 != v16):
                            break
                        if (u32(load8u((v5 + v11))) > u32(load8u((v11 + v12)))):
                            break
                    break
                v2 = v8
                v8 = load16u(v13)
                v3 = load32(((arg0 + (v2 << 2)) + 2908))
                v5 = load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2)))
                if (u32(load16u(v13)) < u32(load16u((v9 + (load32(((arg0 + (v2 << 2)) + 2908)) << 2))))):
                    v2 = v4
                    break
                while True:  # $label15
                    if (v5 != v8):
                        break
                    if (u32(load8u(v15)) > u32(load8u(((arg0 + v3) + 5208)))):
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
    while True:  # $label18
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
            while True:  # $label19
                if (arg1 > v5):
                    break
                v6 = ((arg0 + (v15 << 1)) + 2876)
                store16(((arg0 + (v15 << 1)) + 2876), (load16u(v6) + 1))
                v6 = 0
                if (arg1 >= v11):
                    v6 = load32((v16 + ((arg1 - v11) << 2)))
                arg1 = load16u(v13)
                store32(arg0 + 5800, (load32(arg0 + 5800) + (load16u(v13) * (v6 + v15))))
                if not v12:
                    break
                store32(arg0 + 5804, (load32(arg0 + 5804) + ((v6 + load16u((v12 + v21) + 2)) * arg1)))
                break
            v4 = (v4 + v22)
            v2 = (v2 + 1)
            if ((v2 + 1) != 573):
                continue
            break
        if not v4:
            break
        v6 = ((arg0 + (v3 << 1)) + 2876)
        while True:  # $label22
            v2 = v3
            while True:  # $label21
                arg1 = v2
                v2 = (v2 - 1)
                v11 = ((arg0 + ((v2 - 1) << 1)) + 2876)
                v12 = load16u(((arg0 + ((v2 - 1) << 1)) + 2876))
                if not load16u(((arg0 + ((v2 - 1) << 1)) + 2876)):
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
        if not v3:
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
                while True:  # $label25
                    if (u32(arg0) < u32(4)):
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

# ----------------------------------------------------------
# $func261
# ----------------------------------------------------------
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

# ----------------------------------------------------------
# $func262
# ----------------------------------------------------------
def func262(arg0, arg1):
    # TODO: i64.reinterpret_f64
    # TODO: i64.reinterpret_f64
    if not ((u32((arg0 & 9223372036854775807)) < u32(9218868437227405313)) & (u32((arg1 & 9223372036854775807)) <= u32(9218868437227405312))):
        return (arg0 + arg1)
    # TODO: i64.reinterpret_f64
    v7 = arg1
    v2 = i32(((arg1 & 0xFFFFFFFF) >> 32))
    v5 = i32(v7)
    if not ((i32(((arg1 & 0xFFFFFFFF) >> 32)) - 1072693248) | i32(v7)):
        return func424(arg0)
    v6 = (((v2 & 0xFFFFFFFF) >> 30) & 2)
    # TODO: i64.reinterpret_f64
    v7 = arg0
    v3 = ((((v2 & 0xFFFFFFFF) >> 30) & 2) | i32(((arg0 & 0xFFFFFFFF) >> 63)))
    while True:  # $label2
        v4 = (i32(((v7 & 0xFFFFFFFF) >> 32)) & 2147483647)
        if not ((i32(((v7 & 0xFFFFFFFF) >> 32)) & 2147483647) | i32(v7)):
            while True:  # $label1
                while True:  # $label0
                    # br_table (v3 - 2)
                    break
                    break
                return 3.141592653589793
                break
            return -3.141592653589793
        v2 = (v2 & 2147483647)
        if not ((v2 & 2147483647) | v5):
            # TODO: f64.copysign
            return arg0
        while True:  # $label3
            if (v2 == 2146435072):
                if (v4 != 2146435072):
                    break
                return loadf64(((v3 << 3) + 28800))
            if not ((v4 != 2146435072) & (u32((v2 + 67108864)) >= u32(v4))):
                # TODO: f64.copysign
                return arg0
            while True:  # $label4
                if v6:
                    if (u32((v4 + 67108864)) < u32(v2)):
                        break
                break
            arg0 = func424(abs((arg0 / arg1)))
            while True:  # $label7
                while True:  # $label6
                    while True:  # $label5
                        # br_table v3
                        break
                        break
                    return neg(arg0)
                    break
                return (3.141592653589793 - (arg0 + -1.2246467991473532e-16))
                break
            return ((arg0 + -1.2246467991473532e-16) + -3.141592653589793)
            break
        arg0 = loadf64(((v3 << 3) + 28832))
        break
    return arg0

# ----------------------------------------------------------
# $func263
# ----------------------------------------------------------
def func263():
    v0 = load32(9688312)
    if load32(9688312):
        store32(9688312, (v0 - 1))
        return
    atomic_store(9688308, 0)
    if load32(9688316):
        func97(9688308)

# ----------------------------------------------------------
# $func264
# ----------------------------------------------------------
def func264():
    v0 = load32(G.global3 + 24)
    if (load32(G.global3 + 24) != load32(9688308)):
        # TODO: i32.atomic.rmw.cmpxchg
        v1 = v0
        if v0:
            while True:  # $label0
                # TODO: i32.atomic.rmw.cmpxchg
                v1 = v0
                if v0:
                    continue
                break
        return
    store32(9688312, (load32(9688312) + 1))

# ----------------------------------------------------------
# $func265
# ----------------------------------------------------------
def func265(arg0, arg1, arg2):
    arg2 = (G.global0 - 16)
    G.global0 = (G.global0 - 16)
    while True:  # $label2
        while True:  # $label3
            while True:  # $label1
                while True:  # $label0
                    v3 = G.global5
                    if G.global5:
                        break
                    v4 = G.global3
                    if (load8u(G.global3 + 40) != 1):
                        break
                    if (load8u(v4 + 41) != 1):
                        break
                    break
                v5 = i32((1 if v3 else 100))
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

# ----------------------------------------------------------
# $func266
# ----------------------------------------------------------
def func266(arg0):
    if (load32(arg0 + 12) == load32(G.global3 + 24)):
        store32(arg0 + 12, 0)
    while True:  # $label0
        v3 = load32(arg0 + 4)
        v1 = load32(arg0)
        v2 = (v1 & 2147483647)
        v4 = (((v1 - 1) if ((v1 & 2147483647) != 1) else 0) if (v2 != 2147483647) else 0)
        # TODO: i32.atomic.rmw.cmpxchg
        if ((((v1 - 1) if ((v1 & 2147483647) != 1) else 0) if (v2 != 2147483647) else 0) != v1):
            continue
        break
    while True:  # $label1
        if v4:
            break
        if (not v3 & (v1 >= 0)):
            break
        func111(arg0, v2)
        break

# ----------------------------------------------------------
# $func267
# ----------------------------------------------------------
def func267(arg0):
    while True:  # $label0
        while True:  # $label1
            while True:  # $label3
                v2 = 6
                v3 = 10
                while True:  # $label2
                    v1 = load32(arg0)
                    # br_table ((load32(arg0) & 2147483647) - 2147483646)
                    break
                    break
                # TODO: i32.atomic.rmw.cmpxchg
                if (v1 != (v1 + 1)):
                    continue
                break
            v3 = 0
            break
        v2 = v3
        break
    return v2

# ----------------------------------------------------------
# $func268
# ----------------------------------------------------------
def func268(arg0, arg1, arg2, arg3, arg4, arg5):
    while True:  # $label1
        while True:  # $label0
            if not arg0:
                break
            if not arg2:
                break
            v6 = (arg1 >> 31)
            if (((arg1 ^ (arg1 >> 31)) - v6) < arg4):
                break
            v6 = (arg3 >> 31)
            if (((arg3 ^ (arg3 >> 31)) - v6) < arg4):
                break
            while True:  # $label2
                if (arg5 <= 0):
                    break
                while True:  # $label3
                    v8 = (arg5 & 3)
                    if not (arg5 & 3):
                        v6 = arg5
                        break
                    v6 = arg5
                    while True:  # $label4
                        # TODO: memory.copy
                        arg2 = (arg2 + arg3)
                        arg0 = (arg0 + arg1)
                        v6 = (v6 - 1)
                        v7 = (v7 + 1)
                        if ((v7 + 1) != v8):
                            continue
                        break
                    break
                if (u32(arg5) < u32(4)):
                    break
                while True:  # $label5
                    # TODO: memory.copy
                    arg2 = (arg2 + arg3)
                    arg0 = (arg0 + arg1)
                    # TODO: memory.copy
                    arg2 = (arg2 + arg3)
                    arg0 = (arg0 + arg1)
                    # TODO: memory.copy
                    arg2 = (arg2 + arg3)
                    arg0 = (arg0 + arg1)
                    # TODO: memory.copy
                    arg2 = (arg2 + arg3)
                    arg0 = (arg0 + arg1)
                    arg5 = (v6 - 5)
                    v6 = (v6 - 4)
                    if (u32(arg5) < u32(-2)):
                        continue
                    break
                break
            return
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func269
# ----------------------------------------------------------
def func269(arg0, arg1, arg2):
    while True:  # $label1
        while True:  # $label0
            if arg0:
                if not arg1:
                    break
                if (u32(arg2) >= u32(-8)):
                    break
                store64(arg0 + 20, 0)
                store32(arg0 + 12, arg2)
                store32(arg0 + 8, arg1)
                while True:  # $label2
                    arg2 = (8 if (u32(arg2) >= u32(8)) else arg2)
                    if not (8 if (u32(arg2) >= u32(8)) else arg2):
                        break
                    v3 = load8u(arg1)
                    if (arg2 == 1):
                        break
                    v3 = ((load8u(arg1 + 1) << 8) | v3)
                    if (arg2 == 2):
                        break
                    v3 = ((load8u(arg1 + 2) << 16) | v3)
                    if (arg2 == 3):
                        break
                    v3 = ((load8u(arg1 + 3) << 24) | v3)
                    if (arg2 == 4):
                        break
                    v3 = ((load8u(arg1 + 4) << 32) | v3)
                    if (arg2 == 5):
                        break
                    v3 = ((load8u(arg1 + 5) << 40) | v3)
                    if (arg2 == 6):
                        break
                    v3 = ((load8u(arg1 + 6) << 48) | v3)
                    if (arg2 == 7):
                        break
                    break
                v3 = ((load8u(arg1 + 7) << 56) | v3)
                store32(arg0 + 16, arg2)
                store64(arg0, v3)
                return
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()
    return 3628

# ----------------------------------------------------------
# $func270
# ----------------------------------------------------------
def func270(arg0, arg1, arg2):
    while True:  # $label1
        while True:  # $label0
            if arg0:
                if not arg1:
                    break
                if (arg2 < 0):
                    break
                store32(arg0 + 28, 0)
                store64(arg0, 0)
                store64(arg0 + 8, -34359738114)
                store32(arg0 + 16, arg1)
                v4 = (arg1 + arg2)
                store32(arg0 + 20, (arg1 + arg2))
                v4 = ((v4 - 7) if (u32(arg2) > u32(7)) else arg1)
                store32(arg0 + 24, ((v4 - 7) if (u32(arg2) > u32(7)) else arg1))
                if (u32(arg1) < u32(v4)):
                    v3 = load64(arg1)
                    store32(arg0 + 12, 48)
                    store32(arg0 + 16, (arg1 + 7))
                    store64(arg0, ((((((v3 << 56) | ((v3 & 65280) << 40)) | (((v3 & 16711680) << 24) | ((v3 & 4278190080) << 8))) | ((((v3 & 0xFFFFFFFF) >> 40) & 65280) | ((((v3 & 0xFFFFFFFF) >> 8) & 4278190080) | (((v3 & 0xFFFFFFFF) >> 24) & 16711680)))) & 0xFFFFFFFF) >> 8))
                    return
                store32(arg0 + 12, 0)
                if arg2:
                    store32(arg0 + 16, (arg1 + 1))
                    store64(arg0, load8u(arg1))
                    return
                store32(arg0 + 28, 1)
                return
            a_c()
            raise Unreachable()
            break
        a_c()
        raise Unreachable()
        break
    a_c()
    raise Unreachable()

# ----------------------------------------------------------
# $func271
# ----------------------------------------------------------
def func271():
    store32(9622092, 3)
    store32(9621944, 45)
    store64(9621904, 0)
    store64(9621896, 400)
    store32(9622496, 3)
    store32(9622348, 20)
    store64(9622308, 0)
    store64(9622300, 400)
    store32(9622072, 1)
    store32(9622068, 51380)
    store32(9622900, 3)
    store32(9622752, 20)
    store64(9622712, 0)
    store64(9622704, 400)
    store32(9622600, 60)
    store32(9622444, 0)
    store32(9622324, 2)
    store32(9623304, 3)
    store32(9623156, 20)
    store64(9623116, 0)
    store64(9623108, 400)
    store32(9623004, 60)
    store32(9622848, 3)
    store32(9622728, 2)
    store64(9623520, 0)
    store64(9623512, 400)
    store32(9623708, 3)
    store32(9623560, 30)
    store32(9623408, 60)
    store32(9623252, 1)
    store32(9623132, 2)
    store32(9623688, 1)
    store32(9623684, 51384)
    store32(9623536, 1)
    store32(9623812, 61)
    store32(9624112, 3)
    store32(9623964, 30)
    store64(9623924, 0)
    store64(9623916, 400)
    store32(9623680, 27)
    store32(9623676, 58592)
    store32(9624092, 1)
    store32(9624088, 51388)
    store32(9624084, 31)
    store32(9624080, 58960)
    store32(9624516, 3)
    store32(9624368, 30)
    store64(9624328, 0)
    store64(9624320, 400)
    store32(9624216, 61)
    store32(9623948, 1)
    store32(9624920, 3)
    store32(9624772, 20)
    store64(9624732, 0)
    store64(9624724, 300)
    store32(9624496, 2)
    store32(9624492, 51392)
    store32(9625324, 3)
    store32(9625176, 20)
    store64(9625136, 0)
    store64(9625128, 400)
    store32(9624900, 1)
    store32(9624896, 51400)
    store32(9625304, 1)
    store32(9625300, 51404)
    store32(9625728, 3)
    store32(9625580, 30)
    store64(9625540, 0)
    store64(9625532, 400)
    store32(9625428, 60)
    store32(9625272, 2)
    store32(9625152, 2)
    store32(9625700, 31)
    store32(9625696, 58960)
    store32(9626132, 3)
    store32(9625984, 60)
    store64(9625944, 0)
    store64(9625936, 800)
    store32(9625832, 61)
    store32(9625564, 2)
    store32(9626536, 3)
    store32(9626388, 30)
    store64(9626348, 0)
    store64(9626340, 400)
    store32(9626112, 1)
    store32(9626108, 51408)
    store32(9626508, 7)
    store32(9626504, 58560)
    store32(9626940, 3)
    store32(9626792, 30)
    store64(9626752, 0)
    store64(9626744, 300)
    store32(9626640, 61)
    store32(9626364, 1)
    store32(9626920, 1)
    store32(9626916, 51412)
    store32(9626912, 3)
    store32(9626908, 58896)
    store32(9627344, 3)
    store32(9627196, 30)
    store64(9627156, 0)
    store64(9627148, 300)
    store32(9627044, 62)
    store32(9626768, 80)
    store32(9627324, 5)
    store32(9627320, 51424)
    store32(9627748, 3)
    store32(9627600, 30)
    store64(9627560, 0)
    store64(9627552, 400)
    store32(9627448, 60)
    store32(9627292, 5)
    store32(9627172, 50)
    store32(9627728, 3)
    store32(9627724, 51444)
    store32(9628556, 3)
    store32(9628408, 30)
    store64(9628368, 0)
    store64(9628360, 800)
    store32(9628152, 3)
    store32(9628004, 30)
    store64(9627964, 0)
    store64(9627956, 400)
    store32(9627852, 60)
    store32(9627696, 6)
    store32(9627576, 1)
    store32(9628960, 3)
    store32(9628812, 30)
    store64(9628772, 0)
    store64(9628764, 400)
    store32(9628536, 1)
    store32(9628532, 51456)
    store32(9629768, 3)
    store32(9629620, 30)
    store64(9629580, 0)
    store64(9629572, 300)
    store32(9629364, 3)
    store32(9629216, 30)
    store64(9629176, 0)
    store64(9629168, 400)
    store32(9628940, 4)
    store32(9628936, 51472)
    store32(9630172, 3)
    store32(9630024, 30)
    store64(9629984, 0)
    store64(9629976, 500)
    store32(9629748, 2)
    store32(9629744, 51488)
    store32(9630152, 1)
    store32(9630148, 51496)
    store32(9630576, 3)
    store32(9630428, 60)
    store64(9630388, 0)
    store64(9630380, 600)
    store32(9630276, 60)
    store32(9630120, 4)
    store32(9630000, 125)
    store32(9630980, 3)
    store32(9630832, 30)
    store64(9630792, 0)
    store64(9630784, 500)
    store32(9630556, 1)
    store32(9630552, 51500)
    store32(9630960, 1)
    store32(9630956, 51504)
    store32(9631384, 3)
    store32(9631236, 30)
    store64(9631196, 0)
    store64(9631188, 400)
    store32(9631084, 60)
    store32(9630928, 7)
    store32(9630808, 2147483647)
    store32(9631364, 1)
    store32(9631360, 51508)
    store32(9631788, 3)
    store32(9631640, 30)
    store64(9631600, 0)
    store64(9631592, 800)
    store32(9631488, 60)
    store32(9631332, 6)
    store32(9631212, 1)
    store32(9631768, 2)
    store32(9631764, 51512)
    store32(9632192, 3)
    store32(9632044, 30)
    store64(9632004, 0)
    store64(9631996, 600)
    store32(9631892, 60)
    store32(9631736, 6)
    store32(9631616, 1)
    store32(9632596, 3)
    store32(9632448, 30)
    store64(9632408, 0)
    store64(9632400, 800)
    store32(9632172, 2)
    store32(9632168, 51520)
    store32(9633000, 3)
    store32(9632852, 30)
    store64(9632812, 0)
    store64(9632804, 500)
    store32(9632576, 2)
    store32(9632572, 51528)
    store32(9633404, 3)
    store32(9633256, 60)
    store64(9633216, 0)
    store64(9633208, 1200)
    store32(9633104, 60)
    store32(9632948, 8)
    store32(9632828, 4)
    store32(9633808, 3)
    store32(9633660, 60)
    store64(9633620, 0)
    store64(9633612, 800)
    store32(9633384, 1)
    store32(9633380, 51536)
    store32(9634212, 3)
    store32(9634064, 30)
    store64(9634024, 0)
    store64(9634016, 400)
    store32(9633912, 60)
    store32(9633756, 9)
    store32(9633636, 5)
    store32(9634616, 3)
    store32(9634468, 30)
    store64(9634428, 0)
    store64(9634420, 400)
    store32(9634192, 1)
    store32(9634188, 51540)
    store32(9635020, 3)
    store32(9634872, 180)
    store64(9634832, 0)
    store64(9634824, 1200)
    store32(9634596, 2)
    store32(9634592, 51544)
    store32(9635424, 3)
    store32(9635276, 30)
    store64(9635236, 0)
    store64(9635228, 400)
    store32(9635000, 1)
    store32(9634996, 51552)
    store32(9635396, 3)
    store32(9635392, 58852)
    store32(9635828, 3)
    store32(9635680, 30)
    store64(9635640, 0)
    store64(9635632, 400)
    store32(9635528, 61)
    store32(9635252, 5)
    store32(9636232, 3)
    store32(9636084, 30)
    store64(9636044, 0)
    store64(9636036, 500)
    store32(9635808, 2)
    store32(9635804, 51556)
    store32(9636636, 3)
    store32(9636488, 30)
    store64(9636448, 0)
    store64(9636440, 400)
    store32(9636336, 60)
    store32(9636180, 10)
    store32(9636060, 5)
    store32(9637040, 3)
    store32(9636892, 30)
    store64(9636852, 0)
    store64(9636844, 500)
    store32(9636616, 1)
    store32(9636612, 51564)
    store32(9637444, 3)
    store32(9637296, 240)
    store64(9637256, 0)
    store64(9637248, 400)
    store32(9637020, 1)
    store32(9637016, 51568)
    store32(9637848, 3)
    store32(9637700, 30)
    store64(9637660, 0)
    store64(9637652, 800)
    store32(9637424, 2)
    store32(9637420, 51572)
    store32(9638252, 3)
    store32(9638104, 30)
    store64(9638064, 0)
    store64(9638056, 400)
    store32(9637828, 1)
    store32(9637824, 51580)
    store32(9638656, 3)
    store32(9638508, 120)
    store64(9638468, 0)
    store64(9638460, 800)
    store32(9638232, 1)
    store32(9638228, 51584)
    store32(9639060, 3)
    store32(9638912, 20)
    store64(9638872, 0)
    store64(9638864, 2576980377600)
    store32(9638636, 1)
    store32(9638632, 51588)
    v0 = load32(38596)
    store32(9639464, 3)
    store32(9639316, 30)
    store64(9639276, 2147483648000)
    store64(9639268, 0)
    store32(9639164, 55)
    store32(9638888, v0)
    v0 = load32(38640)
    store32(9639868, 3)
    store32(9639720, 30)
    store64(9639680, 2147483648000)
    store64(9639672, 0)
    store32(9639568, 55)
    store32(9639292, v0)
    v0 = load32(38644)
    store32(9640272, 3)
    store32(9640124, 30)
    store64(9640084, 0)
    store64(9640076, 400)
    store32(9639972, 55)
    store32(9639696, v0)
    store64(9640488, 0)
    store64(9640480, 400)
    store32(9640676, 3)
    store32(9640528, 30)
    store32(9640252, 1)
    store32(9640248, 51592)
    store64(9640892, 0)
    store64(9640884, 400)
    store32(9641080, 3)
    store32(9640932, 30)
    store32(9640656, 1)
    store32(9640652, 51596)
    store32(9641052, 2)
    store32(9641048, 58876)
    store32(9641456, 10)
    store32(9641452, 59088)
    store64(9641296, 0)
    store64(9641288, 600)
    store32(9641184, 61)
    store32(9640908, 5)
    store32(9641888, 3)
    store32(9641740, 30)
    store64(9641700, 0)
    store64(9641692, 500)
    store32(9641588, 63)
    store32(9641484, 3)
    store32(9641336, 30)
    store32(9641324, 30)
    store32(9642292, 3)
    store32(9642144, 30)
    store64(9642104, 0)
    store64(9642096, 400)
    store32(9641868, 3)
    store32(9641864, 51600)
    store32(9642696, 3)
    store32(9642548, 60)
    store64(9642508, 0)
    store64(9642500, 500)
    store32(9642396, 60)
    store32(9642240, 2)
    store32(9642120, 12)
    store32(9643100, 3)
    store32(9642952, 30)
    store64(9642912, 0)
    store64(9642904, 300)
    store32(9642676, 1)
    store32(9642672, 51612)
    store32(9643080, 1)
    store32(9643076, 51616)
    store32(9643072, 1)
    store32(9643068, 38924)
    store32(9643504, 3)
    store32(9643356, 30)
    store64(9643316, 0)
    store64(9643308, 400)
    store32(9643204, 62)
    store32(9642928, 75)
    store32(9643484, 3)
    store32(9643480, 51620)
    store32(9643608, 61)
    store32(9643332, 1)
    store32(9644312, 3)
    store32(9644164, 30)
    store64(9644124, 0)
    store64(9644116, 400)
    store32(9643908, 3)
    store32(9643760, 30)
    store64(9643720, 0)
    store64(9643712, 800)
    store32(9643476, 3)
    store32(9643472, 58884)
    store32(9644292, 1)
    store32(9644288, 51632)
    store32(9644416, 61)
    store32(9644160, 2)
    store32(9644716, 3)
    store32(9644568, 30)
    store64(9644528, 0)
    store64(9644520, 500)
    store32(9644284, 2)
    store32(9644280, 58908)
    store32(9645120, 3)
    store32(9644972, 30)
    store64(9644932, 0)
    store64(9644924, 500)
    store32(9644696, 1)
    store32(9644692, 51636)
    store32(9645524, 3)
    store32(9645376, 80)
    store64(9645336, 0)
    store64(9645328, 600)
    store32(9645100, 1)
    store32(9645096, 51640)
    store32(9645504, 1)
    store32(9645500, 51644)
    store32(9645928, 3)
    store32(9645780, 30)
    store64(9645740, 0)
    store64(9645732, 400)
    store32(9645628, 60)
    store32(9645472, 21)
    store32(9645352, 4)
    store32(9646332, 3)
    store32(9646184, 30)
    store64(9646144, 0)
    store64(9646136, 300)
    store32(9645908, 1)
    store32(9645904, 51648)
    store32(9646736, 3)
    store32(9646588, 300)
    store64(9646548, 0)
    store64(9646540, 800)
    store32(9646312, 1)
    store32(9646308, 51652)
    store32(9647140, 3)
    store32(9646992, 30)
    store64(9646952, 0)
    store64(9646944, 300)
    store32(9646716, 1)
    store32(9646712, 51656)
    store32(9647544, 3)
    store32(9647396, 30)
    store64(9647356, 0)
    store64(9647348, 400)
    store32(9647120, 1)
    store32(9647116, 51660)
    store32(9647948, 3)
    store32(9647800, 30)
    store64(9647760, 0)
    store64(9647752, 400)
    store32(9647524, 2)
    store32(9647520, 51664)
    store32(9648756, 3)
    store32(9648608, 30)
    store64(9648568, 0)
    store64(9648560, 500)
    store32(9648352, 3)
    store32(9648204, 30)
    store64(9648164, 0)
    store64(9648156, 600)
    store32(9647928, 3)
    store32(9647924, 51672)
    store32(9648736, 1)
    store32(9648732, 51684)
    store32(9648860, 61)
    store32(9648584, 1)
    store32(9649160, 3)
    store32(9649012, 30)
    store64(9648972, 0)
    store64(9648964, 500)
    store32(9648728, 7)
    store32(9648724, 58560)
    store32(9649564, 3)
    store32(9649416, 30)
    store64(9649376, 0)
    store64(9649368, 500)
    store32(9649264, 60)
    store32(9649108, 4)
    store32(9648988, 120)
    store32(9649544, 1)
    store32(9649540, 51688)
    store32(9649668, 61)
    store32(9649392, 10)
    store32(9649968, 3)
    store32(9649820, 30)
    store64(9649780, 0)
    store64(9649772, 800)
    store32(9649536, 1)
    store32(9649532, 38644)
    store32(9650372, 3)
    store32(9650224, 120)
    store64(9650184, 0)
    store64(9650176, 800)
    store32(9649948, 1)
    store32(9649944, 51692)
    store32(9650776, 3)
    store32(9650628, 30)
    store64(9650588, 0)
    store64(9650580, 600)
    store32(9650352, 1)
    store32(9650348, 51696)
    store32(9651584, 3)
    store32(9651436, 30)
    store64(9651396, 0)
    store64(9651388, 800)
    store32(9651180, 3)
    store32(9651032, 30)
    store64(9650992, 0)
    store64(9650984, 500)
    store32(9650756, 1)
    store32(9650752, 51700)
    store32(9652392, 3)
    store32(9652244, 30)
    store64(9652204, 0)
    store64(9652196, 500)
    store32(9651988, 3)
    store32(9651840, 30)
    store64(9651800, 0)
    store64(9651792, 200)
    store32(9651688, 60)
    store32(9651532, 6)
    store32(9651412, 1)
    store32(9652364, 3)
    store32(9652360, 58916)
    store32(9652796, 3)
    store32(9652648, 30)
    store64(9652608, 0)
    store64(9652600, 400)
    store32(9652496, 62)
    store32(9652220, 75)
    store32(9652776, 1)
    store32(9652772, 51704)
    store32(9652900, 61)
    store32(9652624, 1)
    store32(9653200, 3)
    store32(9653052, 30)
    store64(9653012, 0)
    store64(9653004, 1200)
    store32(9652768, 27)
    store32(9652764, 58592)
    store32(9653604, 3)
    store32(9653456, 30)
    store64(9653416, 0)
    store64(9653408, 300)
    store32(9653180, 2)
    store32(9653176, 51708)
    store32(9654008, 3)
    store32(9653860, 180)
    store64(9653820, 0)
    store64(9653812, 1200)
    store32(9653584, 2)
    store32(9653580, 51716)
    store32(9654412, 3)
    store32(9654264, 60)
    store64(9654224, 0)
    store64(9654216, 800)
    store32(9653988, 1)
    store32(9653984, 51724)
    store32(9654816, 3)
    store32(9654668, 30)
    store64(9654628, 0)
    store64(9654620, 400)
    store32(9654392, 1)
    store32(9654388, 51728)
    store32(9655220, 3)
    store32(9655072, 30)
    store64(9655032, 0)
    store64(9655024, 400)
    store32(9654796, 1)
    store32(9654792, 51732)
    store32(9655624, 3)
    store32(9655476, 300)
    store64(9655436, 0)
    store64(9655428, 600)
    store32(9655200, 1)
    store32(9655196, 51736)
    store32(9656028, 3)
    store32(9655880, 30)
    store64(9655840, 0)
    store64(9655832, 800)
    store32(9655604, 1)
    store32(9655600, 51740)
    store32(9656432, 3)
    store32(9656284, 30)
    store64(9656244, 0)
    store64(9656236, 500)
    store32(9656132, 60)
    store32(9655976, 29)
    store32(9655856, 1)
    store32(9656412, 1)
    store32(9656408, 51744)
    store32(9656404, 3)
    store32(9656400, 58916)
    store32(9656836, 3)
    store32(9656688, 120)
    store64(9656648, 0)
    store64(9656640, 1200)
    store32(9656536, 61)
    store32(9656268, 1)
    store32(9656260, 2)
    store32(9657240, 3)
    store32(9657092, 30)
    store64(9657052, 0)
    store64(9657044, 200)
    store32(9656816, 1)
    store32(9656812, 51748)
    store32(9657212, 3)
    store32(9657208, 58896)
    store32(9668956, 3)
    store32(9668808, 1)
    store64(9668768, 85899345920)
    store64(9668760, 0)
    store32(9657344, 62)
    store32(9657068, 64)
    v0 = load32(38600)
    store32(9670168, 3)
    store32(9670020, 1)
    store64(9669980, 858993459200)
    store64(9669972, 0)
    store32(9669360, 3)
    store32(9669212, 30)
    store64(9669172, 0)
    store64(9669164, 300)
    store32(9669060, 55)
    store32(9668784, v0)
    v0 = load32(38624)
    store32(9670272, 55)
    store32(9669996, v0)
    store32(9621912, 207)
    store32(9622316, 208)
    store32(9622720, 209)
    store32(9623124, 210)
    store32(9623528, 211)
    store32(9623932, 212)
    store32(9624336, 213)
    store32(9624740, 214)
    store32(9625144, 215)
    store32(9625548, 216)
    store32(9625952, 217)
    store32(9626356, 218)
    store32(9626760, 219)
    store32(9627164, 220)
    store32(9627568, 221)
    store32(9627972, 222)
    store32(9628376, 223)
    store32(9628780, 224)
    store32(9629184, 225)
    store32(9629588, 226)
    store32(9629992, 227)
    store32(9630396, 228)
    store32(9630800, 229)
    store32(9631204, 230)
    store32(9631608, 231)
    store32(9632012, 232)
    store32(9632416, 233)
    store32(9632820, 234)
    store32(9633224, 235)
    store32(9633628, 236)
    store32(9634032, 237)
    store32(9634436, 238)
    store32(9634840, 239)
    store32(9635244, 240)
    store32(9635648, 241)
    store32(9636052, 242)
    store32(9636456, 243)
    store32(9636860, 244)
    store32(9637264, 192)
    store32(9637668, 245)
    store32(9638072, 246)
    store32(9638476, 191)
    store32(9638880, 247)
    store32(9639284, 248)
    store32(9639688, 249)
    store32(9640092, 250)
    store32(9640496, 175)
    store32(9640900, 251)
    store32(9641304, 252)
    store32(9641708, 253)
    store32(9642112, 254)
    store32(9642516, 255)
    store32(9642920, 256)
    store32(9643324, 257)
    store32(9643728, 258)
    store32(9644132, 259)
    store32(9644536, 260)
    store32(9644940, 261)
    store32(9645344, 262)
    store32(9645748, 263)
    store32(9646152, 264)
    store32(9646556, 204)
    store32(9646960, 265)
    store32(9647364, 266)
    store32(9647768, 267)
    store32(9648172, 268)
    store32(9648576, 269)
    store32(9648980, 270)
    store32(9649384, 271)
    store32(9649788, 272)
    store32(9650192, 273)
    store32(9650596, 274)
    store32(9651000, 275)
    store32(9651404, 276)
    store32(9651808, 277)
    store32(9652212, 278)
    store32(9652616, 279)
    store32(9653020, 280)
    store32(9653424, 281)
    store32(9653828, 200)
    store32(9654232, 282)
    store32(9654636, 283)
    store32(9655040, 284)
    store32(9655444, 206)
    store32(9655848, 392)
    store32(9656252, 285)
    store32(9656656, 197)
    store32(9657060, 286)
    store32(9668776, 830)
    store32(9669180, 402)
    store32(9669988, 439)
    store32(9669184, 403)
    store32(9657064, 298)
    store32(9656660, 362)
    store32(9656256, 361)
    store32(9655852, 360)
    store32(9655448, 359)
    store32(9655044, 358)
    store32(9654640, 357)
    store32(9653832, 356)
    store32(9653428, 355)
    store32(9653024, 354)
    store32(9652620, 353)
    store32(9652216, 352)
    store32(9651812, 351)
    store32(9651408, 350)
    store32(9651004, 349)
    store32(9650600, 348)
    store32(9650196, 347)
    store32(9649792, 346)
    store32(9649388, 345)
    store32(9648984, 305)
    store32(9648580, 297)
    store32(9648176, 303)
    store32(9647772, 344)
    store32(9647368, 343)
    store32(9646964, 342)
    store32(9646560, 341)
    store32(9646156, 340)
    store32(9645752, 339)
    store32(9645348, 338)
    store32(9644944, 337)
    store32(9644540, 336)
    store32(9644136, 335)
    store32(9643732, 334)
    store32(9643328, 333)
    store32(9642924, 332)
    store32(9642520, 331)
    store32(9642116, 330)
    store32(9641712, 329)
    store32(9641308, 328)
    store32(9640904, 327)
    store32(9640500, 326)
    store32(9638480, 325)
    store32(9638076, 324)
    store32(9637672, 323)
    store32(9637268, 322)
    store32(9636864, 321)
    store32(9636460, 320)
    store32(9636056, 319)
    store32(9635652, 318)
    store32(9635248, 317)
    store32(9634844, 316)
    store32(9634440, 315)
    store32(9634036, 314)
    store32(9633632, 313)
    store32(9633228, 312)
    store32(9632824, 311)
    store32(9632420, 310)
    store32(9632016, 309)
    store32(9631612, 308)
    store32(9631208, 308)
    store32(9630804, 307)
    store32(9630400, 306)
    store32(9629996, 305)
    store32(9629592, 304)
    store32(9629188, 303)
    store32(9628784, 302)
    store32(9628380, 301)
    store32(9627572, 300)
    store32(9627168, 299)
    store32(9626764, 298)
    store32(9626360, 297)
    store32(9625956, 296)
    store32(9625552, 292)
    store32(9625148, 295)
    store32(9624744, 294)
    store32(9624340, 293)
    store32(9623936, 292)
    store32(9623532, 291)
    store32(9623128, 290)
    store32(9622724, 289)
    store32(9622320, 288)
    store32(9621916, 287)
    v0 = ((load32(38944) * 404) + ENTITY_TYPES)
    store32(((load32(38944) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 363)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1181116006400)
    store32(v0 + 152, 8)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 200)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 199)
    store64(v0 + 76, 0)
    v0 = ((load32(38948) * 404) + ENTITY_TYPES)
    store32(((load32(38948) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 364)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 957777707008)
    store32(v0 + 152, 14)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 200)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 205)
    store64(v0 + 76, 0)
    v0 = ((load32(38988) * 404) + ENTITY_TYPES)
    store32(((load32(38988) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 365)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 962072674304)
    store32(v0 + 152, 15)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 120)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 206)
    store64(v0 + 76, 0)
    v0 = ((load32(38992) * 404) + ENTITY_TYPES)
    store32(((load32(38992) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 366)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1000727379968)
    store32(v0 + 152, 16)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 40)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 208)
    store64(v0 + 76, 0)
    v0 = ((load32(39000) * 404) + ENTITY_TYPES)
    store32(((load32(39000) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 367)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 979252543488)
    store32(v0 + 152, 22)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 320)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 215)
    store64(v0 + 76, 0)
    v0 = ((load32(39004) * 404) + ENTITY_TYPES)
    store32(((load32(39004) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 368)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1172526071808)
    store32(v0 + 152, 25)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 320)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 218)
    store64(v0 + 76, 0)
    v0 = ((load32(39008) * 404) + ENTITY_TYPES)
    store32(((load32(39008) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 369)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 992137445376)
    store32(v0 + 152, 17)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 480)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 209)
    store64(v0 + 76, 0)
    v0 = ((load32(39012) * 404) + ENTITY_TYPES)
    store32(((load32(39012) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 370)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 987842478080)
    store32(v0 + 152, 12)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 40)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 203)
    store64(v0 + 76, 0)
    v0 = ((load32(39016) * 404) + ENTITY_TYPES)
    store32(((load32(39016) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 371)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1168231104512)
    store32(v0 + 152, 11)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 320)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 202)
    store64(v0 + 76, 0)
    v0 = ((load32(39020) * 404) + ENTITY_TYPES)
    store32(((load32(39020) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 372)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 983547510784)
    store32(v0 + 152, 9)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 80)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 200)
    store64(v0 + 76, 0)
    v0 = ((load32(39024) * 404) + ENTITY_TYPES)
    store32(((load32(39024) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 373)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 395136991232)
    store32(v0 + 152, 24)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 20)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 217)
    store64(v0 + 76, 0)
    v0 = ((load32(39028) * 404) + ENTITY_TYPES)
    store32(((load32(39028) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 374)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1185410973696)
    store32(v0 + 152, 19)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 40)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 211)
    store64(v0 + 76, 0)
    v0 = ((load32(39032) * 404) + ENTITY_TYPES)
    store32(((load32(39032) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 375)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1176821039104)
    store32(v0 + 152, 18)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 20)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 210)
    store64(v0 + 76, 0)
    v0 = ((load32(39036) * 404) + ENTITY_TYPES)
    store32(((load32(39036) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 376)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 390842023936)
    store32(v0 + 152, 10)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 20)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 201)
    store64(v0 + 76, 0)
    v0 = ((load32(39040) * 404) + ENTITY_TYPES)
    store32(((load32(39040) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 377)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 403726925824)
    store32(v0 + 152, 13)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 20)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 204)
    store64(v0 + 76, 0)
    v0 = ((load32(39044) * 404) + ENTITY_TYPES)
    store32(((load32(39044) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 378)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 970662608896)
    store32(v0 + 152, 21)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 80)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 214)
    store64(v0 + 76, 0)
    v0 = ((load32(39048) * 404) + ENTITY_TYPES)
    store32(((load32(39048) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 379)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 974957576192)
    store32(v0 + 152, 23)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 120)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 216)
    store64(v0 + 76, 0)
    v0 = ((load32(39052) * 404) + ENTITY_TYPES)
    store32(((load32(39052) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 380)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 966367641600)
    store32(v0 + 152, 20)
    store64(v0 + 264, 4294967298)
    store64(v0 + 68, 40)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 213)
    store64(v0 + 76, 0)
    v0 = ((load32(38952) * 404) + ENTITY_TYPES)
    store32(((load32(38952) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 381)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 0)
    store32(v0 + 152, 5)
    store64(v0 + 264, 8589934594)
    store64(v0 + 68, 10)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 16)
    store64(v0 + 76, 0)
    v0 = ((load32(38960) * 404) + ENTITY_TYPES)
    store32(((load32(38960) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 170)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 0)
    store32(v0 + 152, 6)
    store64(v0 + 264, 8589934594)
    store64(v0 + 68, 10)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 4)
    store64(v0 + 76, 0)
    v0 = ((load32(38956) * 404) + ENTITY_TYPES)
    store32(((load32(38956) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 171)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 0)
    store32(v0 + 152, 7)
    store64(v0 + 264, 8589934594)
    store64(v0 + 68, 10)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 1)
    store64(v0 + 76, 0)
    v0 = ((load32(38964) * 404) + ENTITY_TYPES)
    store32(((load32(38964) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 4)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1391569403905)
    store32(v0 + 152, 0)
    store64(v0 + 264, 2)
    store64(v0 + 68, 10)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 191)
    store64(v0 + 76, 0)
    v0 = ((load32(38968) * 404) + ENTITY_TYPES)
    store32(((load32(38968) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 382)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1391569403906)
    store32(v0 + 152, 1)
    store64(v0 + 264, 2)
    store64(v0 + 68, 10)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 192)
    store64(v0 + 76, 0)
    v0 = ((load32(38972) * 404) + ENTITY_TYPES)
    store32(((load32(38972) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 7)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1391569403909)
    store32(v0 + 152, 3)
    store64(v0 + 264, 2)
    store64(v0 + 68, 10)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 194)
    store64(v0 + 76, 0)
    v0 = ((load32(38976) * 404) + ENTITY_TYPES)
    store32(((load32(38976) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 5)
    store64(v0 + 104, 107374182425)
    store32(v0 + 188, 55)
    store64(v0 + 168, 1391569403910)
    store32(v0 + 152, 4)
    store64(v0 + 264, 2)
    store64(v0 + 68, 10)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 195)
    store64(v0 + 76, 0)
    v3 = ((load32(38980) * 404) + ENTITY_TYPES)
    store32(((load32(38980) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v3 + 84, 383)
    store32(v3 + 188, 55)
    store64(v3 + 168, 1391569403904)
    store32(v3 + 152, 2)
    store64(v3 + 264, 2)
    store64(v3 + 68, 10)
    store32(v3 + 372, 40384)
    store64(v3 + 216, 4294967297)
    store32(v3 + 144, 193)
    store64(v3 + 76, 0)
    v0 = ((load32(38984) * 404) + ENTITY_TYPES)
    store32(((load32(38984) * 404) + ENTITY_TYPES) + 196, 3)
    store32(v0 + 84, 384)
    store64(v0 + 168, 0)
    store32(v0 + 152, 0)
    store64(v0 + 264, 12884901890)
    store64(v0 + 68, 10)
    store32(v0 + 372, 40384)
    store64(v0 + 216, 4294967297)
    store32(v0 + 144, 14)
    store64(v0 + 76, 0)
    v1 = ((load32(39064) * 404) + ENTITY_TYPES)
    store32(((load32(39064) * 404) + ENTITY_TYPES) + 144, 20)
    store32(v1 + 372, 40384)
    store64(v1 + 216, 4294967297)
    store64(v1 + 68, 10)
    store32(v1 + 152, 0)
    store64(v1 + 168, 0)
    store32(v1 + 196, 3)
    store64(v1 + 264, 12884901890)
    store32(v1 + 84, 909)
    store64(v1 + 76, 0)
    v2 = ((load32(39060) * 404) + ENTITY_TYPES)
    store32(((load32(39060) * 404) + ENTITY_TYPES) + 144, 22)
    store32(v2 + 372, 40384)
    store64(v2 + 216, 4294967297)
    store64(v2 + 68, 10)
    store32(v2 + 152, 0)
    store64(v2 + 168, 0)
    store32(v2 + 196, 3)
    store64(v2 + 264, 12884901890)
    store32(v2 + 84, 910)
    store64(v2 + 76, 0)
    v4 = ((load32(38952) * 404) + ENTITY_TYPES)
    store64(((load32(38952) * 404) + ENTITY_TYPES) + 104, 107374182425)
    v5 = ((load32(38960) * 404) + ENTITY_TYPES)
    store64(((load32(38960) * 404) + ENTITY_TYPES) + 104, 107374182425)
    v6 = ((load32(38956) * 404) + ENTITY_TYPES)
    store64(((load32(38956) * 404) + ENTITY_TYPES) + 104, 107374182425)
    store64(((load32(38964) * 404) + ENTITY_TYPES) + 104, 107374182425)
    v7 = ((load32(38968) * 404) + ENTITY_TYPES)
    store64(((load32(38968) * 404) + ENTITY_TYPES) + 104, 107374182425)
    v8 = ((load32(38972) * 404) + ENTITY_TYPES)
    store64(((load32(38972) * 404) + ENTITY_TYPES) + 104, 107374182425)
    v9 = ((load32(38976) * 404) + ENTITY_TYPES)
    store64(((load32(38976) * 404) + ENTITY_TYPES) + 104, 107374182425)
    store32(v3 + 108, 25)
    store32(v3 + 104, 25)
    store32(v0 + 188, 2)
    store32(v0 + 108, 25)
    store32(v0 + 104, 25)
    store32(v0 + 156, 15)
    store32(v0 + 92, 10)
    store32(v1 + 188, 0)
    store32(v1 + 108, 25)
    store32(v1 + 104, 25)
    store32(v1 + 156, 10)
    store32(v1 + 92, 10)
    store32(v2 + 188, 3)
    store32(v2 + 108, 25)
    store32(v2 + 104, 25)
    store32(v2 + 156, 11)
    store32(v2 + 92, 10)
    v0 = ((load32(38980) * 404) + ENTITY_TYPES)
    store32(((load32(38980) * 404) + ENTITY_TYPES) + 128, 100)
    store32(v0 + 120, 100)
    store32(v8 + 92, 4)
    store32(v9 + 100, 4)
    store32(v7 + 112, 1)
    store32(v4 + 92, 5)
    store32(v5 + 92, 5)
    store32(v6 + 100, 5)
    store32(((load32(38640) * 404) + ENTITY_TYPES) + 268, 1)
    store32(((load32(38644) * 404) + ENTITY_TYPES) + 268, 1)
    store32(((load32(38648) * 404) + ENTITY_TYPES) + 268, 1)
    store32(((load32(38548) * 404) + ENTITY_TYPES) + 268, 1)
    store32(((load32(38596) * 404) + ENTITY_TYPES) + 268, 1)
